# Typography: Khmer-first, bilingual

## The four faces

| Face | Role | Sizes | Line-height | Notes |
|---|---|---|---|---|
| **Moul** | Display: page titles, section titles, brand wordmark, splash title, banner, empty-state title | 16–48px (never <16) | 1.5–1.8 | One weight (400). Never `font-weight:700`. Heavy, hand-lettered poster feel. |
| **Koulen** | Numerals and stamps: years, counters (`១ / ៤`), percentages, roman section numbers (I. II.), stamps, stat values | 14–36px | 1.1–1.5 | Condensed display; one weight. Use for anything that is *counted*. |
| **Battambang** | Body: paragraphs, labels, buttons, inputs, nav items, captions | 13–17px (16 default) | 1.6–1.7 | 400 and 700. Buttons and current items use 700. |
| **Special Elite** | Latin-only typewriter labels: brand romanisation, URLs, codes, hex values, "STYLE TILE · 1970" eyebrows | 12–16px | 1.4 | Uppercase, `letter-spacing:3px`, muted. **No Khmer glyphs** in this font. |

Font stacks:
```css
--rk-font-display: 'Moul', 'Khmer OS Muol Light', serif;
--rk-font-numeral: 'Koulen', 'Khmer OS Bokor', sans-serif;
--rk-font-body: 'Battambang', 'Noto Sans Khmer', 'Khmer OS', serif;
--rk-font-latin: 'Special Elite', 'Courier New', monospace;
```

Battambang includes Latin glyphs, so mixed Khmer and English body copy needs no second font. Use Special
Elite only when you want the typewriter-label effect.

Loading:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Moul&family=Koulen&family=Battambang:wght@400;700&family=Special+Elite&display=swap">
```
Self-host for offline apps or PWAs. All four are under the SIL Open Font License.

## Scale

| Step | Face | Size / LH | Example use |
|---|---|---|---|
| Splash | Moul | 48 / 1.5 | App name on the splash, with `text-shadow: 3px 3px 0 paper` |
| H1 | Moul | 26–30 / 1.6 | Page title above a `3px double` rule |
| H2 | Moul | 20–22 / 1.7 | Sidebar title, header title |
| H3 | Moul | 16–18 / 1.7–1.8 | Card titles, dialog titles, empty-state titles, doc header |
| Section label | Battambang 700 | 14–15 / 1.6 | Numbered section heads: `១ · ពណ៌ និងតួនាទី` |
| Body | Battambang 400 | 16 / 1.7 | Default |
| Small | Battambang 400 | 14 / 1.6 | Meta, helper text (`ink-muted`) |
| Micro | Battambang 700 | 12–13 / 1.4 | Sub-labels under numerals (`លើកទី ១`). Khmer never goes below 12 |
| Numeral L | Koulen | 22–36 / 1.2 | Stat values, roman section numbers |
| Numeral M | Koulen | 16–18 / 1.1–1.3 | Ledger years, pager counters, zoom % |
| Stamp | Koulen | 14 (saved) / 20 (fail) / 1.5 | Rotated stamps |
| Eyebrow | Special Elite | 12, `ls:3px`, uppercase | Latin brand line under a Khmer wordmark |

## Khmer script rules

- **Vertical room.** Khmer stacks subscript consonants (ជើង) and vowels above and below the baseline. Use line-height
  1.6–1.8, and never put a fixed `height` with `overflow:hidden` around a line of Khmer. Single-line
  controls use `min-height` and flex centring, not a fixed `line-height` equal to the height.
- **No letter-spacing** on Khmer runs; it breaks clusters. No `text-transform`, since Khmer has no case.
- **No faux bold.** Set `font-synthesis: none`. Moul and Koulen are already heavy.
- **Line breaking.** Khmer has no spaces between words. Chromium and Safari break Khmer using ICU
  dictionaries; also set `overflow-wrap: anywhere` as a fallback. In long titles you control,
  insert a zero-width space (U+200B) at word boundaries. **Never** `word-break: break-all`.
- **Truncation.** Prefer wrapping. If a header title must be one line, use `white-space:nowrap; overflow:hidden;
  text-overflow:ellipsis` with line-height ≥1.7 so the marks are not shaved.
- **The section separator** is a spaced middle dot ` · ` between Khmer phrases (e.g. `វិទ្យាសាស្ត្រពិត · ២០២២`).
  End sentences with `។`. Use `៖` after a label (`វិញ្ញាសា៖ គណិតវិទ្យា`). Quotes are `« »`.

## Numerals

Use Khmer digits in Khmer UI. Keep data in ASCII and convert when rendering:

```js
const KM = '០១២៣៤៥៦៧៨៩';
export const toKhmerDigits = (v) => String(v).replace(/[0-9]/g, (d) => KM[d]);
// toKhmerDigits('133 / 138') → '១៣៣ / ១៣៨'; toKhmerDigits('100%') → '១០០%'
```
`Intl.NumberFormat('km-KH', { numberingSystem: 'khmr' })` also works, but it inserts grouping separators.
Prefer the helper for counters and years.

Latin contexts (codes, URLs, hex values, version numbers) keep ASCII digits in Special Elite.

## Bilingual layout

- Default copy is Khmer. Where English is needed, either:
  - Stack it: a Khmer title in Moul, with an English sub-line in Special Elite (eyebrow style) or Battambang 14 muted; or
  - Inline it: `<span lang="en">` inside Battambang body (no font switch needed).
- Give Khmer the larger size. English lines are about 15–20% smaller, because Khmer reads smaller at the same px.
- `lang="km"` on `<html>`; `lang="en"` on English runs, so screen readers and hyphenation behave.
- Date format: `ថ្ងៃទី ៦ ខែវិច្ឆិកា ឆ្នាំ២០២៦`; short form `០៦/១១/២០២៦`.

## English-primary and bilingual sites

- Set `lang="en"` on `<html>` (or on a section). `retrokh.css` switches `.rk-display`, `.rk-hero-title`,
  `.rk-section-title`, `.rk-pagehead h1`, `.rk-cta h2`, `.rk-feature h3` and `.rk-post h3` to **Koulen**, whose
  condensed Latin reads as a 1970s poster face. Line-height drops to 1.2 for those Latin headings.
- Body text stays Battambang, which has good Latin glyphs. Keep body line-height at 1.7 even in English, for rhythm.
- Keep one Khmer touch per screen even on English sites: the wordmark, an eyebrow (`សួស្ដី · Hello`), section
  numbers or a stamp. Mark it with `lang="km"`.
- Bilingual headings: put the Khmer in Moul, then the English underneath in Special Elite (eyebrow style) or Koulen
  at about 60% of the size. Don't set both languages at the same size side by side.
- English section numbers use ASCII digits (`01 · About`); Khmer ones use Khmer digits (`០១ · អំពីយើង`).

## Voice

Use the formal but warm register of a 1970s school or ministry notice:
- Buttons are short verbs: បន្ទាប់ (next), មុន (previous), ទាញយក (download), ស្វែងរក (search), បិទ (close),
  ព្យាយាមម្ដងទៀត (retry), ដំឡើង (install), រក្សាទុក (save), បោះបង់ (cancel).
- Status lines are a bold statement plus a muted remedy: **មិនអាចបើកឯកសារបានទេ** / សូមពិនិត្យអ៊ីនធឺណិត ហើយព្យាយាមម្ដងទៀត។
- Loading: `កំពុងផ្ទុក…`, `កំពុងរៀបចំ…`. Empty: `រកមិនឃើញលទ្ធផល` + a concrete suggestion using «».
- Never invent statistics or names. Use bracket placeholders such as `[ … នាទី ]` or `[ YOUR PRICE ]`.
