# Typography: Khmer-first, bilingual

## One typeface: Google Sans

RetroKh uses **only Google Sans**. It covers Khmer (U+1780–17FF) and Latin, and Google Fonts serves real weights
from 400 to 700. Don't add other families. The 1970s print character comes from colour, patterns, hard shadows,
stamps, rules and the off-register `.rk-misprint` shadow, not from typeface variety. Typographic roles are set
by **weight, size, case and figure style**:

| Role | Weight | Sizes | Line-height | Use |
|---|---|---|---|---|
| **Display** | 700 | 16–56px | Khmer 1.5–1.7 · Latin 1.1–1.25 | Page, section and card titles, the wordmark, splash title, banner, empty-state title |
| **Numeral** | 700 + `font-variant-numeric: tabular-nums` | 14–44px | 1.1–1.4 | Years, counters (`១ / ៤`), percentages, roman section numbers, stamps, stat values, prices: anything that is *counted* |
| **Body** | 400 (700 for emphasis, buttons and current items) | 14–18px (16 default) | 1.6–1.8 | Paragraphs, inputs, nav items, captions |
| **Label** | 500 | 12–14px | 1.4 | Latin-only caps labels: brand romanisation, URLs, codes, hex values, eyebrows. `text-transform: uppercase; letter-spacing: .18em` |

```css
--rk-font: 'Google Sans', sans-serif;
--rk-w-body: 400; --rk-w-label: 500; --rk-w-strong: 700;
```
Never ask for weights above 700. They aren't served, and `font-synthesis: none` stops the browser faking them.

Loading:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400..700&display=swap">
```
Google Fonts splits the family by script (`unicode-range`), so a Khmer page downloads the Khmer and Latin files only.
For offline apps or PWAs, self-host the Khmer and Latin `woff2` subsets. Google Sans is under the SIL Open Font License.

**Making one sans feel 1970s:**
- Set display text big and bold, with tight Latin leading and caps for English headings (poster style).
- Put the hero title on a plate with `.rk-misprint` (`text-shadow: 3px 3px 0 turmeric`), like a second ink pass slightly
  out of register.
- Use bold tabular numerals in red for years, prices and counters, and rotated stamps for status.
- Use Latin caps labels with wide tracking (`.rk-latin`) as the typewriter/letterpress accent.

## Scale

| Step | Role | Size / LH | Example use |
|---|---|---|---|
| Hero | Display 700 | 32–56 / 1.5 (Latin 1.1) | Hero or splash title, optional `.rk-misprint` |
| H1 | Display 700 | 26–40 / 1.6 | Page title above a `3px double` rule |
| H2 | Display 700 | 20–34 / 1.6–1.7 | Section titles, sidebar title, header title |
| H3 | Display 700 | 16–18 / 1.7 | Card, dialog and empty-state titles |
| Eyebrow | Numeral 700 | 15–17 / 1.5 | Numbered section heads: `០១ · សេវាកម្ម` |
| Body | Body 400 | 16 / 1.7 | Default |
| Lead | Body 400 | 18 / 1.8 | Intro paragraph under a section title (`ink-muted`) |
| Small | Body 400 | 14 / 1.6 | Meta, helper text (`ink-muted`) |
| Micro | Body 700 | 12–13 / 1.4 | Sub-labels under numerals (`លើកទី ១`). Khmer never goes below 12 |
| Numeral L | Numeral 700 | 22–44 / 1.2 | Stat values, roman section numbers, ticket dates |
| Numeral M | Numeral 700 | 16–18 / 1.1–1.3 | Ledger years, pager counters, zoom % |
| Stamp | Numeral 700 | 14 (saved) / 20 (fail) / 1.5 | Rotated stamps |
| Label | Label 500 caps | 12, `ls:.18em` | Latin brand line under a Khmer wordmark |

## Khmer script rules

- **Vertical room.** Khmer stacks subscript consonants (ជើង) and vowels above and below the baseline. Use line-height
  1.6–1.8, and never put a fixed `height` with `overflow:hidden` around a line of Khmer. Single-line
  controls use `min-height` and flex centring, not a fixed `line-height` equal to the height.
- **No letter-spacing** on Khmer runs; it breaks clusters. No `text-transform`, since Khmer has no case.
- **No faux bold.** Set `font-synthesis: none`, and use only the served weights 400, 500 and 700.
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

Latin contexts (codes, URLs, hex values, version numbers) keep ASCII digits, set as Latin caps labels (`.rk-latin`) or regular body text.

## Bilingual layout

- Default copy is Khmer. Where English is needed, either:
  - Stack it: a Khmer title in bold display, with an English sub-line as a Latin caps label (`.rk-latin`) or 14px muted body; or
  - Inline it: `<span lang="en">` inside the body text (same font, nothing to switch).
- Give Khmer the larger size. English lines are about 15–20% smaller, because Khmer reads smaller at the same px.
- `lang="km"` on `<html>`; `lang="en"` on English runs, so screen readers and hyphenation behave.
- Date format: `ថ្ងៃទី ៦ ខែវិច្ឆិកា ឆ្នាំ២០២៦`; short form `០៦/១១/២០២៦`.

## English-primary and bilingual sites

- Set `lang="en"` on `<html>` (or on a section). `retrokh.css` then tightens Latin headings: `.rk-hero-title`,
  `.rk-section-title`, `.rk-pagehead h1` and `.rk-cta h2` become **uppercase poster caps** with 1.1 leading and
  slight negative tracking. `.rk-display`, `.rk-title`, `.rk-feature h3` and `.rk-post h3` get 1.25 leading.
- Body text is the same Google Sans. Keep body line-height at 1.7 even in English, for rhythm.
- Keep one Khmer touch per screen even on English sites: the wordmark, an eyebrow (`សួស្ដី · Hello`), section
  numbers or a stamp. Mark it with `lang="km"`.
- Bilingual headings: put the Khmer in bold display, then the English underneath as a Latin caps label or in bold
  at about 60% of the size. Don't set both languages at the same size side by side.
- English section numbers use ASCII digits (`01 · About`); Khmer ones use Khmer digits (`០១ · អំពីយើង`).

## Voice

Use the formal but warm register of a 1970s school or ministry notice:
- Buttons are short verbs: បន្ទាប់ (next), មុន (previous), ទាញយក (download), ស្វែងរក (search), បិទ (close),
  ព្យាយាមម្ដងទៀត (retry), ដំឡើង (install), រក្សាទុក (save), បោះបង់ (cancel).
- Status lines are a bold statement plus a muted remedy: **មិនអាចបើកឯកសារបានទេ** / សូមពិនិត្យអ៊ីនធឺណិត ហើយព្យាយាមម្ដងទៀត។
- Loading: `កំពុងផ្ទុក…`, `កំពុងរៀបចំ…`. Empty: `រកមិនឃើញលទ្ធផល` + a concrete suggestion using «».
- Never invent statistics or names. Use bracket placeholders such as `[ … នាទី ]` or `[ YOUR PRICE ]`.
