# Components

Class names refer to `assets/retrokh.css`. Each spec states the exact values so it can be rebuilt in any stack.
**Paper context:** light sheets (`.rk-sheet`, inputs, menus, tables, stats, the dashed panel) stay paper-coloured in dark mode, so
`retrokh.css` resets their text, edge and accent variables to the light-ink values. For a custom light block, add `.rk-paper-context`.

Every control is a real element (`<button>`, `<a href>`, `<input>` with a `<label>`), and every icon-only control
has a Khmer `aria-label`.

## Icons

Use inline stroke SVG on a 24×24 viewBox with `fill="none" stroke="currentColor" stroke-width="2.4"` (2.6 for chevrons and
close), and `stroke-linecap="square"` for menus and bars. Draw them at 18px (20–22px in headers). Mark them `aria-hidden="true"`. Never use emoji.
```html
<!-- menu -->    <path d="M4 6h16M4 12h16M4 18h16"/>
<!-- download --><path d="M12 4v11M7 10l5 5 5-5M4 20h16"/>
<!-- search -->  <circle cx="11" cy="11" r="6.5"/><path d="M16 16l5 5"/>
<!-- close -->   <path d="M6 6l12 12M18 6L6 18"/>
<!-- next -->    <path d="M9 6l6 6-6 6"/>    <!-- prev --> <path d="M15 6l-6 6 6 6"/>
<!-- up -->      <path d="M6 15l6-6 6 6"/>   <!-- expand --> <path d="M6 9l6 6 6-6"/>
<!-- check -->   <path d="M5 12l5 5 9-10"/>
<!-- plus -->    <path d="M5 12h14M12 5v14"/> <!-- minus --> <path d="M5 12h14"/>
<!-- more -->    <g fill="currentColor" stroke="none"><circle cx="5" cy="12" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="19" cy="12" r="2"/></g>
<!-- print -->   <path d="M7 9V3h10v6M7 17H4v-8h16v8h-3M7 14h10v7H7z"/>
<!-- moon -->    <path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/>
<!-- offline --> <path d="M3 3l18 18M8.5 16.4a5 5 0 0 1 7 0M5 12.9a10 10 0 0 1 4-2.3M19 12.9a10 10 0 0 0-2.6-1.8M2 9a15 15 0 0 1 4.3-2.6M22 9a15 15 0 0 0-9-3.9M12 20h.01"/>
```

## Buttons

| Variant | Class | Spec | Use |
|---|---|---|---|
| Primary | `.rk-btn .rk-btn-primary` | 48px min-h, 0 18px, ink bg, paper text, 700, 2px ink border, **shadow `3px 3px 0 red`** | One per view: Next, Retry, Install, Save |
| System | `.rk-btn .rk-btn-system` | 44px, teal bg, paper text, 2px ink border, shadow-1 | Download all, sync, offline actions |
| Accent | `.rk-btn .rk-btn-accent` | 44px, accent bg, on-accent text, shadow-1 | Rare; a "go to current" action |
| Raised | `.rk-btn .rk-btn-raised` | 44px, sheet bg, ink text, shadow-1 | Secondary actions on ground |
| Ghost | `.rk-btn .rk-btn-ghost` | 44px, transparent, 2px border (`paper-muted` on ink bars), 400 weight | Header actions, Cancel, Swap |
| Icon | `+ .rk-btn-icon` | 44×44 (48×48 with `.rk-btn-lg`) | Close, menu, more, back-to-top |

States: hover darkens nothing (print has no hover glow), but you may swap the ghost bg to `paper` on light
surfaces. `:active` shifts by `translate(3px,3px)` and removes the shadow. `:focus-visible` gets a 3px outline in red on paper,
or turmeric on ink. Disabled is 45% opacity with `cursor:not-allowed`.

## Segmented control (pager, zoom)

One box with a 2px border, sheet bg and shadow-1. Children are 48px tall with 2px **dashed** dividers between them. The
counter is set in Koulen 18px (`១៣៣ / ១៣៨`). The forward action is filled with ink. On an ink header, use a transparent bg and a
`paper-muted` border, with `#6E5B45` dashed dividers.

## Inputs

- **Text or search**: a `.rk-input` wrapper, 44px high, sheet bg, 2px ink border, shadow-1, 12px side padding, 18px leading icon,
  Battambang 16px, placeholder in `#6E5B45`. The visible `<label>` above it is 14px, 700, `ink-muted`; on phones it can
  be visually hidden with `.rk-sr`.
- **Invalid**: the border and shadow turn red, with a `.rk-error-text` message below (14px, 700, red) linked via `aria-describedby`.
- **Textarea**: ruled every 27px to match the line-height (`textarea.rk-textarea`).
- **Checkbox and radio**: a 22px square (round for radio), 2px ink border; when checked, an ink fill with a 3px inset sheet ring.
- **Select**: the same box as text input, with a chevron icon on the right.

## Tabs

A grid of equal columns. Each tab is 48px, sheet bg, 2px ink border (the left border is removed on siblings so the borders join),
Battambang 700. The selected tab is accent bg with on-accent text. Use `role="tablist"`, `role="tab"` and `aria-selected`.

## Header (app bar)

An ink bar (`.rk-header`): `[menu 44] [seal 48 + Moul wordmark 20 / Special Elite eyebrow 12] [centred Moul title 20 +
muted 14 subtitle] [actions]`, with 12px × 24px padding and wrapping on narrow screens. Header buttons are ghost buttons with `paper-muted`
borders. A **zigzag strip** always follows directly below it.

Phone: 8px × 10px padding, `[menu] [title stack, ellipsis] [2 icon buttons]`, and a 10px zigzag.

## Sidebar and ledger navigation

- Sidebar: paper bg, `4px double` ink right edge, 24px vertical padding, flex column with a gap of 20.
- Title block: Moul 22px in the accent colour, with a muted 14px subtitle.
- **Ledger rows** (`.rk-ledger-row`) on `.rk-ruled`, 44px high:
  `[key column 84px: Koulen 18px accent, 2px accent right rule, optional 12px 700 sub-label] [text, 16px] [chevron 16px]`.
  Group rows are `<button aria-expanded>`; children are an `<ol>` of links with an empty key column (the rule continues).
- **Current item**: a 36px filled accent tab, 12px margin from the rule, 700 weight, shadow-1, `aria-current="page"`.
- **Saved item**: a teal stamp on the right, with the meaning repeated in `aria-label`.
- An offline panel at the bottom: `.rk-panel-dashed` (2px dashed teal, sheet bg) containing a bold teal title, a muted count, a
  10px teal progress bar and a full-width system button.

## Drawer (phone)

A scrim at `rgba(42,29,20,.55)` over the content. The drawer is 330px (max 85vw), paper bg, with a `4px double` right edge and shadow
`8px 0 0 rgba(42,29,20,.6)`. Its header is an ink bar with a Moul 18 title and a 44px ghost close button, followed by a 10px zigzag. Use `role="dialog"
aria-modal="true"`, trap focus, close on Esc, and return focus to the menu button.

## Sheets and cards

- **Document sheet** (`.rk-sheet`): sheet bg, 2px ink border, `8px 8px 0` shadow, max-width 720px, 56px padding (22–28px on
  phones), stacked with a 32px gap on a halftone backdrop.
- **Card** (`.rk-card`): the same frame; the optional head strip `.rk-card-head` is an ink bar, 4px × 12px, 14px 700 paper text.
  Numbered heads use Khmer numerals: `១ · កំពុងផ្ទុក`.
- **Stat** (`.rk-stat`): sheet, shadow-1, a muted label and a Koulen 36px value in the accent colour.

## Lists, tables, menus

- **Table** (`.rk-table`): a sheet with a 2px border and shadow-2. The header row is ink with 14px 700 paper text. Rows are separated by 1px **dashed**
  ink. Numeric cells are Koulen 17px, right-aligned. Wrap the table in `.rk-table-wrap` to scroll horizontally on phones.
- **Search results**: 40px rows with 1px teal-rule separators; the matched text in `<mark>` (turmeric bg); the year on the right in
  Koulen 16 red.
- **Menu** (`.rk-menu`): sheet, 2px border, shadow-2 (`#000` when it opens over ink), 44px items with 18px icon + label,
  1px dashed separators, `role="menu"` and `role="menuitem"`, and arrow-key navigation.

## Chips and tags

- **Ink chip** (`.rk-chip-ink`): 44px, ink bg, paper 15px text with a Koulen 18 number (`ទំព័រ ១ / ៤`). When floating over sheets, add a 2px
  paper border and shadow-1.
- **Tag** (`.rk-tag`): 32px, sheet, 2px border, 14px, with an optional Koulen red index number.
- **Highlight**: `<mark>` in turmeric with ink text and 0 2px padding.

## Feedback states

| State | Recipe |
|---|---|
| Loading | Halftone backdrop; a centred card (230px, sheet, shadow-1) with "កំពុងផ្ទុក" plus a Koulen % and a 14px progress bar with a hatch fill. `role="status"` |
| Splash loading | Rays, the seal, the Moul title, then a 220px progress bar (ink fill) and a bold "កំពុងរៀបចំ…" |
| Error | `role="alert"`, centred: a red stamp "បរាជ័យ" (−4°), a bold 17px message, a muted 15px remedy, and a primary Retry button |
| Offline | `.rk-alert-system`: teal bg, paper text, offline icon, 15px message. Back online: `.rk-alert-ok` (dashed teal on paper, check icon, bold) |
| Not available offline | `.rk-alert-warn`: 2px red border with the bold red lead-in "…មិនទាន់បានរក្សាទុកទេ", then ink text |
| Empty or no results | `.rk-empty`: 2px dashed ink box, a Moul 16 title, and a muted hint with an example in «» |
| Toast | `.rk-toast`: ink bg, paper text, check icon, shadow `3px 3px 0 teal`; auto-dismiss after ≥5s in a `role="status"` region |
| Install prompt | Paper box, 2px border: bold title + muted body + a 44px ghost close button, and a full-width primary button below |

## Dialog

`<dialog class="rk-dialog">`: sheet bg, 2px border, shadow-2, max 480px. The head is an ink bar with a Moul 16–18 title and a close button.
The body has 20px padding. The footer is right-aligned: a ghost Cancel button and a primary confirm button, with a 12px gap. The backdrop is the scrim colour.

## Compare / split view

Two columns on halftone, separated by a `4px double` ink divider. Each column has a `.rk-tag` with a Koulen red index and
a sheet with shadow-1. The toolbar above it is a paper strip with a 2px bottom border and a Moul 16 title, followed by a ghost Swap button and an ink Exit button.

## Bottom navigation (phone reader)

72px, raised surface, with a `4px double` top edge and 3 columns: a Previous link, a counter (Koulen 18 red + 12px muted label) with
2px dashed side rules, and a filled primary Next button (10px inset, shadow `3px 3px 0 red`).
