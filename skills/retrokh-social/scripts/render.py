#!/usr/bin/env python3
"""Render one RetroKh Social artwork to exact platform sizes and check each result.

Usage:
    python3 scripts/render.py art.html --formats youtube-thumbnail,tiktok-cover --out out/
    python3 scripts/render.py art.html --formats all --guides
    python3 scripts/render.py --list

Writes <stem>-<format>.png (or .jpg when a PNG would break the platform's file limit). --guides also
writes <stem>-<format>.guides.png with the safe area drawn on it. YouTube thumbnails also get a
-small.png at the size viewers really see, when Pillow is installed.

Exit code 0 when there are no ERRORs, 1 when there are, 2 on bad usage. Needs Chrome or Chromium.
Pillow is optional; it is only used for the small preview and the JPEG fallback.
"""
import argparse
import glob
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
ASSETS = SKILL_DIR / "assets"

# width, height, safe insets (top, right, bottom, left), smallest text px, file limit MB, keep-out rects (x, y, w, h)
FORMATS = {
    "youtube-thumbnail": (1280, 720, (40, 40, 40, 40), 30, 2, [(1090, 630, 190, 90)]),
    "youtube-banner": (2560, 1440, (509, 507, 509, 507), 40, 6, []),
    "youtube-shorts-cover": (1080, 1920, (420, 150, 420, 150), 34, 20, []),
    "youtube-community": (1080, 1080, (64, 64, 64, 64), 30, 16, []),
    "tiktok-cover": (1080, 1920, (420, 150, 420, 150), 34, 20, []),
    "tiktok-poster": (1080, 1920, (150, 150, 400, 60), 34, 20, []),
    "facebook-post": (1080, 1350, (64, 64, 64, 64), 30, 30, []),
    "facebook-square": (1080, 1080, (64, 64, 64, 64), 30, 30, []),
    "facebook-story": (1080, 1920, (260, 64, 340, 64), 34, 30, []),
    "facebook-link": (1200, 630, (44, 44, 44, 44), 28, 8, []),
    "facebook-event": (1920, 1005, (70, 90, 70, 90), 36, 30, []),
    "facebook-page-cover": (1640, 924, (160, 90, 160, 90), 32, 30, [(90, 580, 360, 190)]),
}

CHECK_JS = r"""
(function () {
  var cfg = __CFG__;
  var out = [];

  function add(level, msg) { if (out.indexOf(level + '|' + msg) < 0) { out.push(level + '|' + msg); } }

  function families(el) {
    return getComputedStyle(el).fontFamily.split(',').map(function (f) { return f.trim().replace(/^["']|["']$/g, ''); });
  }

  function loaded(name) {
    return Array.from(document.fonts).some(function (f) {
      return f.family.replace(/^["']|["']$/g, '') === name && f.status === 'loaded';
    });
  }

  function hit(a, b) { return a.left < b.x + b.w && a.right > b.x && a.top < b.y + b.h && a.bottom > b.y; }

  function run() {
    var safe = { left: cfg.l, top: cfg.t, right: cfg.w - cfg.r, bottom: cfg.h - cfg.b };
    var walk = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    var node;

    while ((node = walk.nextNode())) {
      var el = node.parentElement;
      var text = node.nodeValue.trim();

      if (!text || /^(SCRIPT|STYLE)$/.test(el.tagName) || el.closest('svg')) { continue; }

      var range = document.createRange();
      range.selectNodeContents(node);
      var rect = range.getBoundingClientRect();
      var label = text.slice(0, 28);

      if (!rect.width) { continue; }

      // Range boxes use font metrics, which run far taller than the line in Khmer fonts. Measure the line box.
      var lines = range.getClientRects();
      var lineHeight = parseFloat(getComputedStyle(el).lineHeight) || rect.height;
      var excess = Math.max(0, (lines[0].height - lineHeight) / 2);

      rect = { left: rect.left, right: rect.right, top: rect.top + excess, bottom: rect.bottom - excess };

      if (rect.left < safe.left - 1 || rect.top < safe.top - 1 || rect.right > safe.right + 1 || rect.bottom > safe.bottom + 1) {
        add('ERROR', 'safe-area: "' + label + '" reaches outside the safe area -> shorten it or reduce its size');
      }

      cfg.keep.forEach(function (k) {
        if (hit(rect, { x: k[0], y: k[1], w: k[2], h: k[3] })) {
          add('ERROR', 'keep-out: "' + label + '" sits under platform UI -> move it');
        }
      });

      var size = parseFloat(getComputedStyle(el).fontSize);

      if (size < cfg.min) {
        add('ERROR', 'small-text: "' + label + '" is ' + Math.round(size) + 'px, minimum ' + cfg.min + 'px -> enlarge or delete it');
      }

      var names = families(el);
      var weight = parseInt(getComputedStyle(el).fontWeight, 10);

      if (names[0] !== 'Google Sans') {
        add('ERROR', 'font: "' + label + '" uses ' + names[0] + ' -> this skill allows Google Sans only');
      } else if (!loaded('Google Sans')) {
        add('ERROR', 'font: Google Sans did not load for "' + label + '" -> check the Google Fonts link and the network');
      }

      if (weight < 400 || weight > 700) {
        add('ERROR', 'font: "' + label + '" uses weight ' + weight + ' -> Google Sans has weights 400 to 700');
      }
    }

    var title = document.querySelector('.rs-title');

    if (title && cfg.w >= cfg.h && title.textContent.trim().split(/\s+/).length > 5) {
      add('WARN', 'title: more than 5 words -> a landscape title must read at thumbnail size');
    }

    if (/\[ /.test(document.querySelector('.rs-canvas').textContent)) { add('WARN', 'placeholder: [ … ] text is still in the artwork'); }

    var report = document.createElement('pre');
    report.id = 'rs-report';
    report.textContent = JSON.stringify(out);
    report.style.display = 'none';
    document.body.appendChild(report);

    if (cfg.guides) {
      var g = document.createElement('div');
      g.style.cssText = 'position:fixed;z-index:99;box-sizing:border-box;border:6px dashed #0FF;outline:3px solid #000;left:' + cfg.l + 'px;top:' + cfg.t + 'px;width:' + (cfg.w - cfg.l - cfg.r) + 'px;height:' + (cfg.h - cfg.t - cfg.b) + 'px';
      document.body.appendChild(g);
      cfg.keep.forEach(function (k) {
        var box = document.createElement('div');
        box.style.cssText = 'position:fixed;z-index:99;background:rgba(255,0,0,.45);left:' + k[0] + 'px;top:' + k[1] + 'px;width:' + k[2] + 'px;height:' + k[3] + 'px';
        document.body.appendChild(box);
      });
    }
  }

  document.fonts.ready.then(function () { setTimeout(run, 50); });
})();
"""


def find_chrome():
    configured = os.environ.get("CHROME_PATH")
    if configured:
        return configured

    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"):
        found = shutil.which(name)
        if found:
            return found

    patterns = (
        "~/.cache/ms-playwright/chromium-*/chrome-linux*/chrome",
        "~/Library/Caches/ms-playwright/chromium-*/chrome-mac*/*.app/Contents/MacOS/*",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    )
    for pattern in patterns:
        matches = sorted(glob.glob(os.path.expanduser(pattern)))
        if matches:
            return matches[-1]

    return None


def shape_of(width, height, insets):
    top, right, bottom, left = insets
    ratio = (width - left - right) / (height - top - bottom)
    if ratio >= 2.2:
        return "banner"
    if ratio >= 1.3:
        return "landscape"
    if ratio >= 0.85:
        return "square"
    return "portrait"


def inline_motifs(source):
    def replace(match):
        path = ASSETS / "motifs" / f"{match.group(1)}.svg"
        if not path.exists():
            names = ", ".join(sorted(p.stem for p in (ASSETS / "motifs").glob("*.svg")))
            sys.exit(f"Unknown motif '{match.group(1)}'. Available: {names}")
        return path.read_text(encoding="utf-8")

    return re.sub(r'<rs-motif\s+name="([a-z-]+)"\s*>\s*</rs-motif>', replace, source)


def build_page(source, name, guides):
    width, height, insets, min_px, _, keep = FORMATS[name]
    top, right, bottom, left = insets
    short_side = min(width - left - right, height - top - bottom)
    shape = shape_of(width, height, insets)

    page = inline_motifs(source)
    tokens = (
        f":root{{--u:{short_side / 100:.2f}px;--safe-t:{top}px;--safe-r:{right}px;"
        f"--safe-b:{bottom}px;--safe-l:{left}px}}"
        # Chrome's viewport differs between --dump-dom and --screenshot, so never size from vh.
        f".rs-canvas{{width:{width}px;height:{height}px}}"
    )
    # Tokens follow social.css so they override its defaults; the artwork's own <style> still wins.
    head = f"<style>{(ASSETS / 'social.css').read_text(encoding='utf-8')}{tokens}</style>"
    page = re.sub(r"(<head[^>]*>)", lambda m: m.group(1) + head, page, count=1)
    if name == "facebook-page-cover":
        # The profile photo covers the lower left, so the artwork goes there and the copy goes right.
        page = re.sub(r'(<html\b[^>]*?)data-layout="[^"]*"', r"\1", page, count=1)
        page = re.sub(r"<html\b", '<html data-layout="art-left"', page, count=1)

    page = re.sub(
        r"<html\b",
        f'<html data-shape="{shape}" data-format="{html.escape(name)}"',
        page,
        count=1,
    )

    config = {
        "w": width, "h": height, "t": top, "r": right, "b": bottom, "l": left,
        "min": min_px, "keep": keep, "guides": guides,
    }
    scripts = (
        f"<script>{(ASSETS / 'fit.js').read_text(encoding='utf-8')}</script>"
        f"<script>{CHECK_JS.replace('__CFG__', json.dumps(config))}</script>"
    )
    return page.replace("</body>", scripts + "</body>")


def chrome(binary, page_path, width, height, *extra):
    base = [
        binary, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
        "--force-device-scale-factor=1", "--virtual-time-budget=9000", f"--window-size={width},{height}",
        *extra, page_path.as_uri(),
    ]
    with tempfile.TemporaryDirectory() as profile:
        command = base[:1] + [f"--user-data-dir={profile}"] + base[1:]
        result = subprocess.run(command, capture_output=True, text=True, timeout=120)
        if result.returncode == 0:
            return result
        # Containers usually cannot use Chrome's sandbox.
        return subprocess.run(command[:1] + ["--no-sandbox"] + command[1:], capture_output=True, text=True, timeout=120)


def read_findings(dom):
    match = re.search(r'<pre id="rs-report"[^>]*>(.*?)</pre>', dom, re.S)
    if not match:
        return ["ERROR|render: the page did not finish -> check the artwork's HTML"]
    return json.loads(html.unescape(match.group(1)))


def save_small_preview(png, target):
    try:
        from PIL import Image
    except ImportError:
        return False
    Image.open(png).convert("RGB").resize((168, 94), Image.LANCZOS).save(target)
    return True


def enforce_limit(png, limit_mb, findings):
    size_mb = png.stat().st_size / 1_048_576
    if size_mb <= limit_mb:
        return png, size_mb

    try:
        from PIL import Image
    except ImportError:
        findings.append(f"ERROR|file-size: {size_mb:.1f}MB is over {limit_mb}MB -> install Pillow or reduce grain")
        return png, size_mb

    jpg = png.with_suffix(".jpg")
    image = Image.open(png).convert("RGB")
    for quality in (92, 86, 80, 74):
        image.save(jpg, quality=quality, optimize=True, subsampling=0)
        if jpg.stat().st_size / 1_048_576 <= limit_mb:
            png.unlink()
            return jpg, jpg.stat().st_size / 1_048_576

    findings.append(f"ERROR|file-size: over {limit_mb}MB even as JPEG -> reduce grain")
    return jpg, jpg.stat().st_size / 1_048_576


def render(source_path, name, out_dir, binary, guides):
    width, height, _, _, limit_mb, _ = FORMATS[name]
    source = source_path.read_text(encoding="utf-8")
    # The temporary page sits beside the artwork so relative image paths keep working.
    temp = source_path.parent / f".render-{source_path.stem}-{name}.html"
    png = out_dir / f"{source_path.stem}-{name}.png"

    try:
        temp.write_text(build_page(source, name, False), encoding="utf-8")
        findings = read_findings(chrome(binary, temp, width, height, "--dump-dom").stdout)
        chrome(binary, temp, width, height, f"--screenshot={png}")

        if not png.exists():
            return [f"ERROR|render: Chrome wrote no image for {name}"], None

        if guides:
            temp.write_text(build_page(source, name, True), encoding="utf-8")
            chrome(binary, temp, width, height, f"--screenshot={png.with_suffix('.guides.png')}")
    finally:
        temp.unlink(missing_ok=True)

    if name == "youtube-thumbnail":
        save_small_preview(png, png.with_name(f"{png.stem}-small.png"))

    final, size_mb = enforce_limit(png, limit_mb, findings)
    print(f"{final}  {width}x{height}  {size_mb:.1f}MB")
    return findings, final


def main():
    parser = argparse.ArgumentParser(description="Render a RetroKh Social artwork to platform sizes.")
    parser.add_argument("html", nargs="?", type=Path)
    parser.add_argument("--formats", default="all", help="comma-separated names, or all")
    parser.add_argument("--out", type=Path, default=Path("social-out"))
    parser.add_argument("--guides", action="store_true", help="also write a copy with the safe area drawn on it")
    parser.add_argument("--list", action="store_true", help="list formats and exit")
    args = parser.parse_args()

    if args.list:
        for name, spec in FORMATS.items():
            print(f"{name:24} {spec[0]}x{spec[1]}")
        return 0

    if not args.html or not args.html.exists():
        parser.print_usage(sys.stderr)
        return 2

    names = list(FORMATS) if args.formats == "all" else [n.strip() for n in args.formats.split(",")]
    unknown = [n for n in names if n not in FORMATS]
    if unknown:
        print(f"Unknown format: {', '.join(unknown)}. Run --list.", file=sys.stderr)
        return 2

    binary = find_chrome()
    if not binary:
        print("Chrome or Chromium not found. Install it or set CHROME_PATH.", file=sys.stderr)
        return 2

    args.out.mkdir(parents=True, exist_ok=True)
    errors = 0
    for name in names:
        findings, _ = render(args.html.resolve(), name, args.out.resolve(), binary, args.guides)
        for finding in findings:
            level, message = finding.split("|", 1)
            print(f"{name}: {level} {message}")
            errors += level == "ERROR"

    print(f"{len(names)} format(s), {errors} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
