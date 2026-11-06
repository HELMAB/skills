#!/usr/bin/env python3
"""Lint RetroKh output for rule breaks that can be detected mechanically.

Usage:
    python3 scripts/check_retrokh.py <file-or-folder> [...]

Scans .html .htm .css .scss .vue .jsx .tsx .svelte .astro and .blade.php files (folders recursively,
skipping node_modules, dist, build, .git). Prints one line per finding:

    path:line: ERROR <rule>: <what is wrong> -> <how to fix>

Exit code 0 when there are no ERRORs (WARNs are allowed), 1 when there are ERRORs,
2 on bad usage. Standard library only (Python 3.8+).

What it cannot judge (still check by hand, see SKILL.md "Delivery checklist"):
colour roles, contrast of custom colours, copy quality, layout at 390px.
"""
import re
import sys
from pathlib import Path

EXTENSIONS = {".html", ".htm", ".css", ".scss", ".vue", ".jsx", ".tsx", ".svelte", ".astro"}
SKIP_DIRS = {"node_modules", "dist", "build", ".git", ".nuxt", ".next", "vendor"}

# Google Sans ships 400-700. Anything outside that range is synthesised or silently falls back.
MIN_WEIGHT, MAX_WEIGHT = 400, 700
TW_BAD_WEIGHTS = {"font-thin", "font-extralight", "font-light", "font-extrabold", "font-black"}
TW_BAD_FONTS = {"font-serif", "font-mono"}
# Tailwind default shadows are blurred; only shadow-rk-* (hard offsets) and shadow-none are allowed.
TW_BLUR_SHADOWS = {"shadow", "shadow-sm", "shadow-md", "shadow-lg", "shadow-xl", "shadow-2xl", "shadow-inner"}
ALLOWED_RADII = {"0", "0px", "50%", "inherit", "initial", "unset"}
LENGTH = re.compile(r"^-?\d*\.?\d+(px|rem|em|%)?$")
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF]")

findings = []


def report(path, line, level, rule, msg):
    findings.append((str(path), line, level, rule, msg))


def split_top_level(value, sep=","):
    """Split on commas that are not inside parentheses (rgba(), var())."""
    parts, depth, cur = [], 0, ""
    for ch in value:
        depth += ch == "("
        depth -= ch == ")"
        if ch == sep and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    return [p.strip() for p in parts if p.strip()]


def blur_of(shadow):
    """Return the blur length of one shadow layer, or None if it cannot be read (e.g. var())."""
    if "var(" in shadow:
        return None
    tokens = re.sub(r"\([^)]*\)", "", shadow).split()  # drop colour functions
    lengths = [t for t in tokens if LENGTH.match(t)]
    return lengths[2] if len(lengths) >= 3 else "0"


CLASS_ATTR = re.compile(r"""(?:\bclass|\bclassName|:class)\s*=\s*["'`{]([^"'`}]*)""")
APPLY = re.compile(r"@apply\s+([^;]+)")


def class_tokens(line):
    """Tailwind-style class names from class/className/:class attributes and @apply on this line."""
    chunks = CLASS_ATTR.findall(line) + APPLY.findall(line)
    return [t for chunk in chunks for t in chunk.split()]


def check_line(path, n, line, is_html):
    classes = class_tokens(line)
    # 1. Fonts: Google Sans only.
    for m in re.finditer(r"(?<![-\w])font-family\s*[:=]\s*[\"']?([^;\"'}>]+(?:'[^']*'[^;\"'}>]*)*)", line):
        value = m.group(1).strip()
        if not ("Google Sans" in value or value.startswith(("var(", "inherit", "initial", "unset"))):
            report(path, n, "ERROR", "font", f"font-family '{value[:40]}' -> use Google Sans only (var(--rk-font))")
    for m in re.finditer(r"fonts\.googleapis\.com/css2?\?([^\"'\s)>]+)", line):
        families = re.findall(r"family=([^:&]+)", m.group(1))
        others = [f for f in families if f.replace("+", " ") != "Google Sans"]
        if others:
            report(path, n, "ERROR", "font", f"Google Fonts loads {', '.join(others)} -> load only family=Google+Sans:wght@400..700")
    for cls in classes:
        if cls.split(":")[-1] in TW_BAD_FONTS | TW_BAD_WEIGHTS:
            report(path, n, "ERROR", "font", f"Tailwind class {cls} -> use font-sans with font-normal/font-medium/font-bold")

    # 2. Weights 400-700.
    for m in re.finditer(r"(?<![-\w])font-weight\s*[:=]\s*[\"']?(\d{3}|bolder|lighter)", line):
        w = m.group(1)
        if not w.isdigit() or not MIN_WEIGHT <= int(w) <= MAX_WEIGHT:
            report(path, n, "ERROR", "weight", f"font-weight {w} -> use 400, 500 or 700")

    # 3. Square corners.
    for m in re.finditer(r"(?<![-\w])border-(?:\w+-)*radius\s*:\s*([^;\"}]+)", line):
        value = m.group(1).strip()
        if value not in ALLOWED_RADII and not value.startswith("var("):
            report(path, n, "ERROR", "radius", f"border-radius {value} -> 0 (50% only for radios, seals, portraits)")
    for cls in classes:
        base = cls.split(":")[-1]
        if base.startswith("rounded") and base not in ("rounded-none", "rounded-full"):
            report(path, n, "ERROR", "radius", f"Tailwind class {cls} -> rounded-none (rounded-full only for radios/seals)")

    # 4. Hard shadows: no blur.
    for prop in ("box-shadow", "text-shadow"):
        for m in re.finditer(rf"(?<![-\w]){prop}\s*:\s*([^;\"}}]+)", line):
            for layer in split_top_level(m.group(1)):
                if layer in ("none", "inherit", "initial", "unset"):
                    continue
                blur = blur_of(layer)
                if blur not in (None, "0", "0px"):
                    report(path, n, "ERROR", "shadow", f"{prop} '{layer[:40]}' has blur {blur} -> use 3px 3px 0 or 8px 8px 0")
    for cls in classes:
        if cls.split(":")[-1] in TW_BLUR_SHADOWS:
            report(path, n, "ERROR", "shadow", f"Tailwind class {cls} -> shadow-rk-1 / shadow-rk-2")
    if re.search(r"(?:backdrop-)?filter\s*:[^;]*\bblur\(", line) or any(
            c.split(":")[-1].startswith(("blur", "backdrop-blur")) for c in classes):
        report(path, n, "ERROR", "shadow", "blur filter -> RetroKh is printed: no blur anywhere")

    # 5. No pure white / black surfaces.
    if re.search(r"(?<![-\w])background(?:-color)?\s*:\s*(#fff\b|#ffffff\b|white\b|#000\b|#000000\b|black\b)", line, re.I) \
            or any(c.split(":")[-1] in ("bg-white", "bg-black") for c in classes):
        report(path, n, "ERROR", "colour", "pure white/black surface -> use paper #F1E4C6 / sheet #FBF5E6 / ink #2A1D14")

    # 6. HTML basics.
    if is_html and re.search(r"<html(?![^>]*\blang=)", line, re.I):
        report(path, n, "ERROR", "lang", "<html> without lang -> lang=\"km\" (or \"en\" for English-primary)")
    if EMOJI.search(line) and not line.lstrip().startswith(("/*", "//", "<!--", "*")):
        report(path, n, "WARN", "icon", "emoji found -> use inline stroke SVG icons")


def is_markup(path):
    return path.suffix in EXTENSIONS or path.name.endswith(".blade.php")


def check_file(path):
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        report(path, 0, "ERROR", "read", f"cannot read file: {exc}")
        return
    is_html = path.suffix in {".html", ".htm", ".vue", ".svelte", ".astro"} or path.name.endswith(".blade.php")
    for n, line in enumerate(text.splitlines(), 1):
        if "retrokh-ignore" in line:  # escape hatch for a deliberate exception
            continue
        check_line(path, n, line, is_html)


def collect(args):
    files = []
    for arg in args:
        p = Path(arg)
        if p.is_dir():
            files += [f for f in sorted(p.rglob("*"))
                      if is_markup(f) and f.is_file() and not SKIP_DIRS & set(f.parts)]
        elif p.is_file():
            files.append(p)
        else:
            print(f"check_retrokh: no such file or folder: {arg}", file=sys.stderr)
            sys.exit(2)
    return files


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__.strip())
        sys.exit(2)
    files = collect(sys.argv[1:])
    if not files:
        print("check_retrokh: no .html/.css/.vue/.blade.php/... files found", file=sys.stderr)
        sys.exit(2)
    for f in files:
        check_file(f)
    for path, line, level, rule, msg in findings:
        print(f"{path}:{line}: {level} {rule}: {msg}")
    errors = sum(1 for f in findings if f[2] == "ERROR")
    warns = len(findings) - errors
    print(f"check_retrokh: {len(files)} file(s), {errors} error(s), {warns} warning(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
