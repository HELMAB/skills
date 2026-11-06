---
name: retrokh-design
description: Designs and builds websites and UIs in RetroKh, the look of 1960s–70s Cambodian golden-era print (cream paper, brown ink, red/turmeric/teal spot colours, Google Sans, square corners, hard offset shadows, zigzag/halftone/sunburst bands, sepia photos, rubber stamps). Use it when the user wants a Khmer retro, vintage Cambodian or old-school Khmer (ខ្មែរសម័យ ៦០–៧០) site, page, component or restyle, or names RetroKh. Khmer-first; HTML/CSS, Tailwind, Vue, Bootstrap, shadcn.
license: MIT
metadata:
  version: "2.1.0"
---

# RetroKh

Make the screen look like a Cambodian print from the 1960s and early '70s, pressed on cream stock with two or three flat inks.

## The era

- **Evoke:** cinema bills, Khmer pop record sleeves, school textbooks and exam papers, ministry bulletins, shop signs, and the
  breeze-block screens and crisp geometry of New Khmer Architecture. Show flat spot inks, halftone photos, slight
  misregistration, rubber stamps, ruled ledgers, Khmer numerals and ornament bands.
- **Never:** modern gloss (gradients, blur, glass, rounded corners, soft shadows), emoji, Western disco or psychedelic
  70s clichés, Thai or Lao motifs passed off as Khmer, the flag, royal arms or Angkor silhouettes as decoration, and any war or
  1975–79 imagery.

## Rules

1. **One job per colour.** Paper is for surfaces. Ink is for text and primary actions. Red marks *you are here* and the brand.
   Turmeric is only for highlights and ornament. Teal is for system, saved and success states.
2. **Hard shadows, no blur.** Controls get `3px 3px 0`; sheets and menus get `8px 8px 0`. The primary button's shadow is red.
3. **Square corners.** `50%` is only for radios, seals and portraits.
4. **Google Sans only, weights 400, 500 and 700.** Headings and numerals are 700 (numerals `tabular-nums`), body text is 400,
   and Latin caps labels are 500 with `.18em` tracking.
5. **Khmer needs room.** Line-height ≥1.5 for headings and ≥1.7 for body. No letter-spacing or caps on Khmer, and never
   clip it. Show Khmer digits with `toKhmerDigits()` at render time; keep the data in ASCII.
6. **Patterns are `aria-hidden` bands.** Copy sits on a sheet or plate, never directly on a pattern. Per page: rays only in the
   hero, at most one halftone band and one ink band.
7. **Never invent facts** (stats, quotes, clients, prices, contacts). Write `[ … ]` placeholders in the page's language and
   list them for the owner.

## Workflow

Paths like `assets/…`, `references/…` and `scripts/…` are relative to this skill's folder.

1. **Inspect the project before writing** (≤5 reads): the manifest (`package.json`, `composer.json`), the framework and version,
   the CSS approach, existing tokens and components, i18n setup, folder layout and lint config. Then:
   - Follow its conventions (JS or TS, file locations, naming), and add no dependency it doesn't already need.
   - If `retrokh.css` or the `--rk-*` tokens are already there, reuse them and don't copy them again.
   - If it has i18n (vue-i18n, Laravel `lang/`), put copy in its locale files, `km` first, instead of hard-coding strings.
   - If its brand colour reaches 4.5:1 on paper, use it as `--rk-accent`; otherwise ask.
   - With no project, build standalone HTML.
2. **Choose a mode and defaults without asking**, and state them in one line:
   - Mode: *new* (a page or site) or *restyle* (keep the structure and behaviour, change only the skin).
   - Language: `km`, or `en` if the user writes in English or asks for it.
   - Accent: red for commerce and culture, teal (`data-accent="teal"`) for professional, NGO and education, plum for arts and events.
   - Signature moves: pick 2–4 for the whole site.
3. **Install by copying, never by reading.** Use `cp` from this skill's folder. Copied files cost no tokens; reading
   `retrokh.css` costs about 9k. For plain HTML or any JSX or templates, copy `assets/retrokh.css`. For Tailwind, Vue, Laravel
   Blade, Bootstrap or shadcn, `references/stacks.md` says which files to copy.
4. **Read only what the task needs.**

   | Task | Read |
   |---|---|
   | Which class or component to use, states, icons | `references/classes.md` |
   | A website: profile, company, NGO, school, shop, event, blog, landing page | `references/websites.md` |
   | Colour extras, dark mode, type scale, Khmer text, voice, ornament | `references/style.md` |
   | Any stack besides plain HTML | `references/stacks.md` |

   For a whole page, copy `assets/templates/company-profile.html` (Khmer) or `personal-profile.html` (English) into the same
   folder as `retrokh.css`, then edit it in place. That's cheaper than writing a page from scratch.
5. **Build** with semantic tokens (`--rk-surface`, `--rk-text`, `--rk-accent`…), real `<button>`, `<a href>` and `<label>`
   elements, Khmer `aria-label`s, 44px hit targets (48px for primary) and a visible focus outline.
6. **Verify in a loop.** Run `python3 <this skill>/scripts/check_retrokh.py <changed files>`, fix every ERROR, and re-run until it
   reports 0 errors. Add a `retrokh-ignore` comment only for a deliberate exception. Then check what the script can't:
   colour roles, the layout at 390px (nav collapses, no horizontal scroll) and dark mode (follows the OS; lock it with
   `data-theme="light"`). End with the files changed, the defaults you chose and the placeholders the owner must fill.

## Tokens

| Token | Light | Dark | Role |
|---|---|---|---|
| ground | `#EADBB8` | `#1C130D` | page background |
| paper | `#F1E4C6` | `#2A1D14` | surfaces; text on ink |
| sheet | `#FBF5E6` | `#E6DCC4` | cards, inputs, plates (stay light) |
| ink | `#2A1D14` | `#F1E4C6` | text, borders, shadows, primary, ink bars |
| ink-muted | `#5A4632` | `#D9C7A0` | secondary text (7.1:1) |
| red | `#9E2F18` | `#E2735A` | accent: current item, brand, error (5.8:1) |
| turmeric | `#E0A526` / `#E9B94A` | same | `<mark>`, zigzag, rays, breeze block; ink text on it |
| teal | `#245A57` | `#6FB3AD` | saved, system, offline; halftone base `#2F6E6A` |
| plum | `#7A3E8E` | | alternate accent |

Font: `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400..700&display=swap">`
(it covers Khmer and Latin). Spacing runs on a 4px base. Borders are `2px solid` ink, `4px double` for structural edges and
`3px double` under titles.
