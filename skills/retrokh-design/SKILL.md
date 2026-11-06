---
name: retrokh-design
description: Design and build websites and apps in the "RetroKh" style, a Khmer old-school, 1970s print look (cream paper, dark-brown ink, red/turmeric/teal spot colours, Moul and Koulen Khmer display type, square corners, hard offset shadows, zigzag/halftone/sunburst patterns, sepia printed photos, rubber-stamp labels). Use for any site or UI that should feel Khmer retro, vintage Cambodian, 60s/70s Khmer, golden-era or old-school Khmer, including personal profiles, CVs and portfolios, company profiles, organisation, NGO and school sites, restaurants and shops, events and weddings, blogs and news, landing pages, dashboards and app screens. Also use when the user names RetroKh or wants a Khmer-language (km) site to look nostalgic or print-like. Covers HTML/CSS, Tailwind and Vue; Khmer-first with English and bilingual support.
license: MIT
metadata:
  version: "1.1.0"
  source: "Distilled from the Dobpi 1970s Khmer Retro design canvas"
---

# RetroKh: Khmer 1970s print design system

RetroKh makes a website or app look like a 1970s Cambodian printed piece: a cinema bill, a school
prospectus, a ministry bulletin, a shop sign or a record sleeve. It suits any kind of site: a personal
profile, a company or organisation site, a shop, an event page, a blog or an app screen. It uses cream stock, dark-brown ink and
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
   - Vue: see `references/vue.md`. It covers the components and the
     `toKhmerDigits` helper.
2. **Identify what you are building.**
   - **A website** (profile, CV, portfolio, company, organisation, NGO, school, shop, restaurant, event,
     blog, landing page): read `references/websites.md` first. It has the plan, page skeleton, section
     catalogue, a recipe per site type, the image treatment and a quality bar.
   - **An app screen or dashboard**: read `references/layouts.md`.
3. **Read the references the task needs.**
   - `references/tokens.md` has the full palette, roles, contrast ratios, dark mode and accent swaps.
   - `references/typography.md` covers Khmer and Latin pairing, the size scale, numerals, line breaking and copy tone.
   - `references/patterns.md` covers the zigzag, halftone, rays, ruled paper, diamonds, seals and stamps, and where each one goes.
   - `references/components.md` has the anatomy and exact specs of every component, plus states (loading, error, empty, offline, toast).
   - `references/layouts.md` has app skeletons (app shell, sidebar ledger, reader, splash, dashboard, form) and responsive rules.
4. **Build** using the semantic tokens (`--rk-surface`, `--rk-text`, `--rk-accent`…) rather than raw hex values, so dark mode and accent swaps work.
5. **Check the result against the checklist below** before you hand it over. Working pages to copy from:
   `examples/company-profile.html` (Khmer company site), `examples/personal-profile.html` (English-primary
   profile/CV) and `examples/showcase.html` (app components, light and dark).

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

## Signature moves (use 2–4 per site or screen, not all)

Websites:
- A **rays hero with a printed plate**: the copy sits on a sheet with an `8px` shadow over a sunburst, never on the rays.
- **Printed photos**: sepia, a fine halftone, a paper border, the hard shadow, and one tilted print per page.
- **Numbered section heads** (`០១ · សេវាកម្ម`) over a double rule, and a **ledger timeline** with Koulen years.
- An **ink CTA band** framed by zigzag strips, and an ink footer with a `4px double` top edge.

Apps and shared:
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

- Set `lang="km"` on the root and `lang="en"` on English runs. Use Khmer copy by default. When the user wants an
  English or bilingual site, set `lang="en"` on the root: headings switch from Moul to Koulen automatically, and
  the look stays the same (see `typography.md`).
- Use Khmer numerals (០១២៣៤៥៦៧៨៩) in Khmer UI, especially Koulen counters, years and page numbers. Convert at render
  time with `toKhmerDigits()`. Never store them; keep data in ASCII digits.
- Latin brand words and codes (DOBPI, URLs, hex values) go in Special Elite, 12px, uppercase, `letter-spacing: 3px`, muted.
- Never invent facts on a website (stats, testimonials, clients, prices, dates, contacts). Use `[ … ]` placeholders
  in the page's language and list what the owner must supply.
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
- [ ] Phone width (390px): nav collapses, the hero and splits stack, grids go to 1 column, the drawer replaces the
      sidebar, the zigzag drops to 10px, tables scroll inside a box, and there is no horizontal scroll.
- [ ] Websites: skip link, landmarks, one `h1`, meta and OG tags; one halftone band, one ink band, rays only in the hero;
      every photo in a `.rk-photo` frame; no fabricated content.
- [ ] `prefers-reduced-motion` respected; the only motion is the 3px "press" translate on buttons.
