---
name: retrokh-design
description: Design and build UI in the "RetroKh" style, a Khmer old-school, 1970s print look (cream paper, dark-brown ink, spot red/turmeric/teal, Moul and Koulen Khmer display type, square corners, hard offset shadows, zigzag/halftone/sunburst patterns, rubber-stamp labels). Use whenever the user asks for Khmer retro, Cambodian vintage, 60s/70s Khmer, "old school Khmer", golden-era, letterpress or RetroKh styling, or wants a Khmer-language (km) app, page, dashboard, poster or component to feel nostalgic or print-like. Covers HTML/CSS, Tailwind, Vue, React and Flutter, with Khmer-first bilingual typography rules.
license: MIT
metadata:
  version: "1.0.0"
  source: "Distilled from the Dobpi 1970s Khmer Retro design canvas"
---

# RetroKh: Khmer 1970s print design system

RetroKh makes a screen look like a 1970s Cambodian printed page: a school exam paper, a
cinema bill, a ministry form or a record sleeve. It uses cream stock, dark-brown ink and
three spot colours laid down flat. Everything is **printed, not rendered**: no blur, no
rounded corners, no gradients except the printed patterns, and shadows that look like a
second plate slightly out of register.

## The six laws

1. **Every colour has exactly one job.** Paper is for surfaces, ink is for text and primary
   actions, red marks *where you are*, turmeric is for highlight and ornament, and teal is
   for system, offline and saved states. Never use a spot colour just for decoration on a control.
2. **There are two shadow levels and no blur.** Controls get `3px 3px 0`. Sheets, panels and
   menus get `8px 8px 0`. Shadows are ink colour (black in dark mode). The primary button's
   shadow is red.
3. **Corners are square, everywhere.** `border-radius: 0`. The only round things are radio
   buttons, seals and logos.
4. **Moul is only for big headings (≥16px).** Koulen is for numerals, counters and stamps.
   Battambang is for everything else. Special Elite is only for short Latin labels.
5. **Khmer needs vertical room.** Keep line-height between 1.6 and 1.8, never clip Khmer text
   with a fixed height plus `overflow:hidden`, and never letter-space Khmer.
6. **Ornament is a band, never a backdrop under text.** Use the zigzag strip under the header,
   sunburst rays on a splash, halftone behind the document reader and diamonds as a divider.
   Patterns are always `aria-hidden`, and body text never sits directly on a pattern.

## Workflow

1. **Choose the stack and load the tokens.**
   - Plain HTML, or any framework that takes CSS: copy `assets/retrokh.css`, add the Google
     Fonts link from its header, then wrap the app in `class="rk"` and set `lang="km"`.
   - Tailwind: see `references/tailwind.md` and `assets/tailwind.preset.js` (v3) or
     `assets/tailwind.v4.css` (v4).
   - Vue or React: see `references/vue-react.md`. It covers the components and the
     `toKhmerDigits` helper.
   - Flutter: see `references/flutter.md` and `assets/retrokh_theme.dart`.
2. **Read the reference for the task.**
   - `references/tokens.md` has the full palette, roles, contrast ratios, dark mode and accent swaps.
   - `references/typography.md` covers Khmer and Latin pairing, the size scale, numerals, line breaking and copy tone.
   - `references/patterns.md` covers the zigzag, halftone, rays, ruled paper, diamonds, seals and stamps, and where each one goes.
   - `references/components.md` has the anatomy and exact specs of every component, plus states (loading, error, empty, offline, toast).
   - `references/layouts.md` has page skeletons (app shell, sidebar ledger, reader, splash, dashboard, form, landing) and responsive rules.
3. **Build** using the semantic tokens (`--rk-surface`, `--rk-text`, `--rk-accent`…) rather than raw hex values, so dark mode and accent swaps work.
4. **Check the result against the checklist below** before you hand it over.
   `examples/showcase.html` is a working reference page to copy from.

## Core tokens (quick reference)

| Token | Light | Dark | Role |
|---|---|---|---|
| ground | `#EADBB8` | `#1C130D` | page background behind panels |
| paper | `#F1E4C6` | `#2A1D14` | default surface; text on ink |
| sheet | `#FBF5E6` | `#E6DCC4` | raised sheet, inputs, cards (stays light) |
| ink | `#2A1D14` | `#F1E4C6` | text, primary action, header bar |
| ink-muted | `#5A4632` | `#D9C7A0` | secondary text (7.1:1) |
| ink-faint | `#6E5B45` | (edge) | placeholders, hints (5.1:1); dark-mode borders |
| paper-muted | `#D9C7A0` | | secondary text and outlines on ink |
| red (accent) | `#9E2F18` | `#E2735A` | current item, brand mark, error (5.8:1) |
| turmeric | `#E0A526` (+`#E9B94A`) | same | `<mark>`, zigzag, rays (ink text on it) |
| teal | `#245A57` (halftone `#2F6E6A`) | same | offline, saved, system, success |
| plum | `#7A3E8E` | | optional alternate accent |

Fonts: `Moul` (display), `Koulen` (numerals/stamps), `Battambang` 400/700 (body), `Special Elite` (Latin labels).
Google Fonts: `family=Moul&family=Koulen&family=Battambang:wght@400;700&family=Special+Elite&display=swap`.

Sizes: 44px minimum hit target, 48px for primary actions. Spacing runs on a 4px base: 4·8·12·16·20·24·32·40·56.
Borders are `2px solid` ink. Use `4px double` for structural edges (the sidebar edge, the outer frame) and `3px double`
for title rules. Use `2px dashed` for secondary containers and dividers inside segmented controls, and `1px dashed`
between list or menu rows.

## Signature moves (use 2–4 per screen, not all)

- An **ink header bar** with a **14px zigzag strip** (red/turmeric) directly under it.
- A **ledger rail**: an 84px numeral column in Koulen with an accent right rule, on 44px ruled paper.
- The **current item** as a filled accent tab with a `3px 3px 0` ink shadow. It is the only red block on the screen.
- **Rubber stamps**: Koulen in a 2px box rotated −5°, teal for "saved" (បានទាញយក) and red for "failed" (បរាជ័យ).
- A **printed sheet** in `#FBF5E6` with a 2px ink border and an `8px 8px 0` shadow, sitting on a halftone teal backdrop.
- A **splash** with a sunburst-rays background, a giant Moul title with a `3px 3px 0` paper text-shadow and an ink banner rotated −2°.
- An **official-document header** (only for formal or civic content): ព្រះរាជាណាចក្រកម្ពុជា / ជាតិ សាសនា ព្រះមហាក្សត្រ,
  then a diamond divider and a double-ruled meta grid.
- A **segmented control** (pager, zoom) in one bordered box with 2px dashed inner dividers and Koulen counters such as `១៣៣ / ១៣៨`.

## Khmer-first bilingual rules

- Set `lang="km"` on the root and `lang="en"` on English runs. Use Khmer copy by default and English only where the user asks for it.
- Use Khmer numerals (០១២៣៤៥៦៧៨៩) in Khmer UI, especially Koulen counters, years and page numbers. Convert at render
  time with `toKhmerDigits()`. Never store them; keep data in ASCII digits.
- Latin brand words and codes (DOBPI, URLs, hex values) go in Special Elite, 12px, uppercase, `letter-spacing: 3px`, muted.
- Use the polite, concise government/school register: «សូមពិនិត្យអ៊ីនធឺណិត ហើយព្យាយាមម្ដងទៀត». Labels are verbs or nouns, not sentences.
- Write a separate Khmer `aria-label` for every icon-only button (បិទ, ទាញយក, ស្វែងរក, ម៉ឺនុយ…).

## Anti-patterns (reject these)

- Rounded corners, pill buttons, soft or blurred shadows, glassmorphism, neumorphism.
- Gradient washes, pure `#FFFFFF` or `#000000` surfaces (black is allowed only as the dark-mode shadow), emoji as icons.
- Moul for body text, buttons or anything under 16px. Bold weights on Moul or Koulen (they have one weight; set `font-synthesis: none`).
- `letter-spacing` or `text-transform` on Khmer. Line-height below 1.5. Truncating Khmer titles mid-cluster.
- Turmeric or teal used as a text colour on paper for body copy (turmeric fails contrast; teal is reserved for status).
- More than one red "current" block on a screen. Patterns behind paragraphs.
- Decorating with the national flag, the royal coat of arms or Angkor Wat silhouettes. These are national symbols, not
  ornaments. The only exception is the official-document header pattern, used for genuinely formal content.

## Delivery checklist

- [ ] Fonts loaded (Moul, Koulen, Battambang, Special Elite) with fallbacks; `lang="km"`.
- [ ] Only token colours are used, and each colour is in its single role. Text pairs ≥4.5:1 (see the tokens table).
- [ ] `border-radius: 0`; only the two shadow levels; no blur anywhere.
- [ ] Moul ≥16px for headings only; numerals in Koulen; Khmer line-height ≥1.6; no clipped Khmer.
- [ ] Hit targets ≥44px (48px primary); real `<button>`, `<a href>` and `<label>`; Khmer `aria-label` on icon buttons.
- [ ] Visible focus: a 3px outline in red on paper, or in turmeric on ink bars and in dark mode.
- [ ] Patterns are `aria-hidden` and never sit behind text; at most 2–4 signature moves.
- [ ] Dark mode via tokens (night ground `#1C130D`, accent `#E2735A`, sheets stay light `#E6DCC4`).
- [ ] Phone width: header wraps, drawer replaces the sidebar, zigzag drops to 10px, tables scroll inside a box.
- [ ] `prefers-reduced-motion` respected; the only motion is the 3px "press" translate on buttons.
