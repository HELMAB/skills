# Patterns and ornaments

Every pattern is pure CSS (no images), decorative, and marked `aria-hidden="true"`. Text never sits directly
on a pattern. Put a paper or sheet block between them.

| Pattern | Class | Where it belongs | Never |
|---|---|---|---|
| Zigzag | `.rk-zigzag` | A 14px (phone 10px) strip directly under the ink header or drawer header; top of the splash | as a full background |
| Halftone | `.rk-halftone` | Backdrop of the reading or compare area behind sheets; behind a modal or drawer | behind body text |
| Rays (sunburst) | `.rk-rays` | Splash, onboarding, hero, celebration screens | on working screens |
| Ruled paper | `.rk-ruled` | Navigation lists, ledgers (44px pitch, aligned to row height) | misaligned with rows |
| Ruled tight | `.rk-ruled-tight` | Notebook-like textareas, specimen swatches (22px pitch) | |
| Diamonds | `.rk-diamonds` | A 120×12px centred divider under official headers and section titles | full-width or tall |
| Hatch | `.rk-hatch` | The fill of an indeterminate or loading progress bar | large areas |

## CSS

```css
/* Zigzag: turmeric teeth on red */
.rk-zigzag{height:14px;background:
  linear-gradient(135deg,#E0A526 25%,transparent 25%) -10px 0/20px 20px,
  linear-gradient(225deg,#E0A526 25%,transparent 25%) -10px 0/20px 20px,#9E2F18}

/* Halftone: teal print screen, 8px dot pitch */
.rk-halftone{background:radial-gradient(circle,rgba(20,52,50,.25) 1.3px,transparent 1.6px) 0 0/8px 8px,#2F6E6A}
/* dark */ .rk-halftone{background:radial-gradient(circle,rgba(47,110,106,.35) 1.3px,transparent 1.6px) 0 0/8px 8px,#14100C}

/* Rays: 18° stripes; the origin sits behind the seal/title (50% 38% on a phone splash, 50% 100% for a horizon) */
.rk-rays{background:repeating-conic-gradient(from 0deg at 50% 38%,#E0A526 0deg 9deg,#E9B94A 9deg 18deg)}

/* Ruled: one teal hairline every 44px */
.rk-ruled{background:repeating-linear-gradient(to bottom,transparent 0 43px,rgba(36,90,87,.22) 43px 44px)}

/* Diamonds: an ink lattice */
.rk-diamonds{height:12px;background:
  linear-gradient(45deg,transparent 42%,#2A1D14 42% 58%,transparent 58%) 0 0/12px 12px,
  linear-gradient(-45deg,transparent 42%,#2A1D14 42% 58%,transparent 58%) 0 0/12px 12px}

/* Hatch: loading fill */
.rk-hatch{background:repeating-linear-gradient(-45deg,#2A1D14 0 6px,#5A4632 6px 12px)}
```

## Seal (round brand mark)

A round seal like a rubber stamp or coin is the brand mark. Use an accent disc, a dashed paper inner ring and
a paper glyph or monogram centred. With a 3px ink outline it works on the splash; without one it works in the header.

```html
<svg width="48" height="48" viewBox="-14 -14 128 128" aria-hidden="true">
  <circle cx="50" cy="50" r="62" fill="var(--rk-accent)" stroke="#2A1D14" stroke-width="3"/>
  <circle cx="50" cy="50" r="55" fill="none" stroke="#F1E4C6" stroke-width="1.6" stroke-dasharray="3 3"/>
  <!-- your monogram: a Khmer letter set in bold Google Sans, or a simple paper-coloured path -->
  <text x="50" y="50" text-anchor="middle" dominant-baseline="central" fill="#F1E4C6"
        font-family="Google Sans" font-weight="700" font-size="44">ក</text>
</svg>
```
Header seal: 48px. Splash seal: about 150px. Never put a photo or gradient in a seal.

## Stamps

Rubber-stamp marks for **status that has already happened** (saved, failed, approved, paid, archived).
```html
<span class="rk-stamp rk-stamp-saved" aria-hidden="true">បានទាញយក</span>   <!-- teal, 2px, −5° -->
<span class="rk-stamp rk-stamp-fail" aria-hidden="true">បរាជ័យ</span>      <!-- red, 3px, 20px, −4° -->
```
The stamp is visual. Put the same meaning in the parent's `aria-label` or in visible text
(`aria-label="គណិតវិទ្យា — បានទាញយក"`). Use at most one rotation angle family per screen (−4° to −5°).

## Banner (rotated ribbon)

An ink block in bold 16px, rotated −2°, with a `3px 3px 0` accent shadow. Use it once, on a splash or hero, as a
tagline. Class: `.rk-banner`.

## Official-document header

Use it only for genuinely formal content (exam papers, certificates, government-style forms):
```html
<div style="display:flex;flex-direction:column;align-items:center;text-align:center">
  <span class="rk-display" style="font-size:18px;line-height:1.8">ព្រះរាជាណាចក្រកម្ពុជា</span>
  <span style="font-weight:700">ជាតិ សាសនា ព្រះមហាក្សត្រ</span>
  <div class="rk-diamonds" style="width:120px;margin-top:6px" aria-hidden="true"></div>
</div>
<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:4px 24px;padding:12px 0;
            border-top:3px double #2A1D14;border-bottom:3px double #2A1D14">
  <span>វិញ្ញាសា៖ <b>…</b></span><span style="text-align:right">សម័យប្រឡង៖ <b>…</b></span>
</div>
```

## Placeholder text bars

For mock document content, use 8–10px ink bars at 16% opacity with varied widths (94%, 88%, 60%…), under a
bold roman numeral (I. II. III.). Use a dashed 2px box with a bracketed label for image placeholders
(`[ រូបភាព / ក្រាប ]`). Never use lorem ipsum.

## Optional extensions (keep the same restraint)

- **Misregistration**: offset a heading's text-shadow by 2px in turmeric (`text-shadow: 2px 2px 0 #E0A526`) on
  splash titles only.
- **Perforation edge** for tickets and receipts: `border-top: 2px dashed` on a sheet section, with a small
  ground-coloured circle cut out at each end.
- **Kbach-inspired corners**: a small 16px ink diamond at the corners of a frame. Keep it geometric;
  don't imitate temple carvings.
