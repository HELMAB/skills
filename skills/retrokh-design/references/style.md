# Style: colour, type, Khmer text, ornament

## Contents
- [Terms](#terms) · [Colour](#colour) · [Shape and space](#shape-and-space) · [Type](#type) · [Khmer text](#khmer-text)
- [Bilingual and English](#bilingual-and-english) · [Voice](#voice) · [Ornament](#ornament)

## Terms
**ground** is the page background. **paper** is a surface. **sheet** is a raised light surface (cards, inputs, menus). A **plate** is
a sheet holding copy over a pattern. An **ink bar or band** is an ink-coloured strip (nav, CTA, footer). A **stamp** is a rotated
bordered label. Use these words consistently.

## Colour
SKILL.md has the core tokens. The extras are `paper-muted #D9C7A0` (secondary text and outlines on ink, 9.8:1),
`ink-faint #6E5B45` (placeholders and hints, 5.1:1 on paper) and red hover `#6E1F0F`. Contrast: ink on paper is 13.0, on sheet 15.0
and on ground 11.9. Red with paper is 5.8 both ways, teal with paper 6.2 both ways, ink on turmeric 7.5, plum with paper 5.7.

- **Accent swap:** `data-accent="teal"|"plum"` changes `--rk-accent` and `--rk-mark` (the nav's current block). With a teal
  accent, offline and system states use an ink treatment, so teal keeps one job per screen.
- **Dark ("night print"):** bg `#1C130D`, surface `#2A1D14`, sheets stay light `#E6DCC4` with ink text, text `#F1E4C6`/`#D9C7A0`,
  edges `#6E5B45` (decorative only), shadows `#000`, accent and primary `#E2735A` with `#1C130D` text, saved `#6FB3AD`,
  focus `#E0A526`, halftone `#14100C` with teal dots.
- **New colours** must reach 4.5:1 for text (3:1 for large text and UI) against what they sit on. Don't tell states apart by hue alone.

## Shape and space
- Radius `0`. Borders: `2px solid` for controls and cards, `4px double` for structural edges (sidebar, frame, footer top),
  `3px double` under titles, `2px dashed` for secondary panels and segment dividers, `1px dashed` between rows.
- Shadows: `3px 3px 0` for controls, `8px 8px 0` for sheets and menus, red on the primary button, `8px 0 0 rgba(42,29,20,.6)` for drawers.
  Pressed state: `translate(3px,3px)` with no shadow.
- Spacing runs on a 4px base (4·8·12·16·20·24·32·40·56). Sections get 72px padding (48px on phones), cards 24px, and 24–28px gaps between cards.
- Hit targets are 44px (48px for primary actions); icons are 18px. Leave 8px of right and bottom room so shadows aren't clipped by `overflow`.

## Type
Google Sans only; weights 400, 500 and 700 (`font-synthesis:none`).

| Step | Weight | Size / line-height |
|---|---|---|
| Hero | 700 (+`.rk-misprint`) | 32–56 / 1.5 (Latin 1.1) |
| H1 / H2 / H3 | 700 | 26–40 / 1.6 · 20–34 / 1.6 · 16–18 / 1.7 |
| Eyebrow, numerals | 700 tabular | 15–17 eyebrow · 16–44 numerals / 1.1–1.4 |
| Body / lead / small | 400 | 16 / 1.7 · 18 / 1.8 · 14 / 1.6 |
| Label (Latin only) | 500 caps `.18em` | 12 / 1.4 |

## Khmer text
- Use line-height ≥1.5 for headings and ≥1.7 for body. Never use a fixed `height` with `overflow:hidden` on Khmer; use
  `min-height` and flex centring instead.
- No `letter-spacing` or `text-transform` on Khmer. Never use `word-break:break-all`. Khmer has no spaces, so rely on
  `overflow-wrap:anywhere` and add U+200B at word boundaries in long titles you control. Prefer wrapping to ellipsis.
- Punctuation: ` · ` separates phrases, `។` ends a sentence, `៖` follows a label, and `« »` are quotes.
  Dates: `ថ្ងៃទី ៦ ខែវិច្ឆិកា ឆ្នាំ២០២៦` or `០៦/១១/២០២៦`.
- Show digits as Khmer at render time and keep the data in ASCII: `toKhmerDigits()` in `assets/js/khmer.js` (copy it).
  Codes, URLs and versions keep ASCII digits.

## Bilingual and English
- Khmer is the default. Mark English runs `lang="en"` (it's the same font, so nothing else changes). In stacked headings, the
  Khmer is the bold display line and the English is a `.rk-latin` label or appears in bold at about 60% of the size.
- On English-primary pages (`<html lang="en">`), the CSS turns hero, section, page-head and CTA titles into uppercase poster
  caps with 1.1 leading. Keep one Khmer touch per screen: the wordmark, an eyebrow (`សួស្ដី · Hello`) or a stamp.
- English section numbers use ASCII (`01 · About`); Khmer ones use Khmer digits (`០១ · អំពីយើង`).

## Voice
Write in the polite, brief register of a school or ministry notice. Buttons: បន្ទាប់ (next) · មុន (previous) · ទាញយក (download) ·
ស្វែងរក (search) · បិទ (close) · រក្សាទុក (save) · បោះបង់ (cancel) · ផ្ញើ (send) · ព្យាយាមម្ដងទៀត (retry). A status is a bold fact plus a
muted remedy: **មិនអាចបើកឯកសារបានទេ** · សូមពិនិត្យអ៊ីនធឺណិត ហើយព្យាយាមម្ដងទៀត។ Loading: កំពុងផ្ទុក…

## Ornament
- **Seal (logo):**
  `<svg viewBox="-14 -14 128 128" aria-hidden="true"><circle cx="50" cy="50" r="62" fill="#9E2F18"/><circle cx="50" cy="50" r="55" fill="none" stroke="#F1E4C6" stroke-width="2" stroke-dasharray="4 4"/><text x="50" y="54" text-anchor="middle" dominant-baseline="middle" fill="#F1E4C6" font-family="Google Sans" font-weight="700" font-size="46">ក</text></svg>`.
  Use 44–48px in the nav and about 150px on a splash. Never put a photo or gradient inside.
- **Stamps** are for status that has already happened: saved, failed, new, sold out, popular, today. Stick to one angle family (−4° to −5°).
- **Banner** (`.rk-banner`): one tagline per page, on the hero or splash.
- **Official header**, only for genuinely formal content (exam papers, certificates, civic forms): ព្រះរាជាណាចក្រកម្ពុជា (bold 18)
  / ជាតិ សាសនា ព្រះមហាក្សត្រ / `.rk-diamonds` 120px / a two-column meta grid between `3px double` rules.
- **Breeze block** (`.rk-breeze`): the pierced screen walls of 1960s New Khmer Architecture. Use it as a 48px band (above the
  footer, or between sections that aren't patterned) or as a side panel. Never put text on it.
- **Placeholder text:** 8–10px ink bars at 16% opacity with varied widths under a bold roman numeral (I. II.). Never use lorem ipsum.
