# Layouts

Layouts are fluid with `max-width` containers, flex/grid with `gap`, and wrap at phone width. Default root:
```html
<html lang="km"><body class="rk"> … </body></html>
```

## 1. App shell (desktop ≥ 900px)

```
┌──────────────────────── ink header ────────────────────────┐
│ [☰] (seal) WORDMARK      Moul title / sub       [− ១០០% +] [⤓] [⋯] │
├▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ zigzag 14px ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┤
│ sidebar (paper) ║  main (halftone or ground)                │
│ Moul title      ║   ┌─────── sheet 720 ───────┐▌           │
│ [search]        ║   │                         │▌ 8px shadow│
│ [tab|TAB]       ║   └─────────────────────────┘▌           │
│ ledger rows ... ║   ┌─────────────────────────┐            │
│ [offline panel] ║   [ ទំព័រ ១ / ៤ ]  [‹ មុន | ១៣៣/១៣៨ | បន្ទាប់ ›] [↑] │
└─────────────────╨──────────────────────────────────────────┘
```
- Body: `display:flex; flex-wrap:wrap`. The sidebar is `flex: 1 1 340px` and main is `flex: 999 1 560px`. On narrow screens
  the sidebar stacks above main, or is replaced by the drawer.
- The sidebar's right edge is `4px double ink`. Main is centred with a column gap of 32 and padding of 40/24.
- A sticky bottom toolbar inside main: `position:sticky; bottom:16px`, with the chip, pager and up button laid out with `space-between`.

## 2. Phone (390 × 844 reference)

- Header: 8/10 padding, `[☰ 44] [title stack, flex 1, ellipsis] [⤓ 44] [⋯ 44]`, then a 10px zigzag.
- Content: halftone with a sheet at full width minus 16px gutters.
- Floating row 92px above the bottom: the page chip on the left and the up button on the right.
- Bottom nav: 72px, 3 columns, `4px double` top edge (see components).
- Navigation moves into the drawer (330px, scrim, zigzag under its ink header).

## 3. Splash / first run

A rays background with the origin at 50% 38%. Inside a centred column: a 150px seal (3px ink outline), a Moul 48 title with a paper
text-shadow, a −2° ink banner tagline, and a progress bar plus status. Footer: a paper strip with a `3px double` top edge, a 15px hint and a
Special Elite URL/brand line. Use `role="status" aria-live="polite"` on the column.

## 4. Dashboard

```
ink header + zigzag
ground bg, padding 24, max-width 1280, centred
H1 Moul 26 + 3px double rule underneath, with a Special Elite eyebrow on the right
grid(auto-fit, minmax(220px,1fr)) gap 24: .rk-stat × 4      (Koulen values, accent)
grid(2fr 1fr) gap 24:
  .rk-card  ink head "១ · …"  + .rk-table (dashed rows, Koulen numerals)
  .rk-card  ink head "២ · …"  + ledger list / toasts / offline panel
```
Charts: flat fills only, using ink, red, teal, turmeric (with an ink outline) and plum in that order, with 2px ink axes, Koulen tick labels
in Khmer numerals, no gridline blur, and a 1px dashed teal-rule gridline. Bars have square ends and a 2px ink stroke.

## 5. Form page

A single sheet (max 640px) on the ground with an `8px` shadow. Optionally an official header block at the top. Fields stack with a 20px
gap; the labels are bold muted. Group related fields in a 2-column grid with `minmax(0,1fr)`, and collapse to 1 column below
600px. Footer: a `3px double` rule, then the actions aligned right (ghost Cancel, primary Submit). Show inline validation per field.

## 6. Landing / marketing

- Hero: rays background, with the seal + Moul title + banner tagline + primary CTA (48px) on a paper plate (sheet, shadow-2).
- The zigzag strip separates sections. Alternate between paper sections and ink sections (paper text, paper-muted secondary).
- Feature cards in a 3-up grid, each with an ink head strip numbered `១ · ២ · ៣` in Khmer numerals.
- Pricing or plan tables use `.rk-table`; the highlighted plan gets a red stamp ("ពេញនិយម") rather than a glow.
- Footer: an ink background, a `4px double` paper-muted top edge and Special Elite links.

## 7. Style tile (when asked to present the design system)

A 1000 × 900 sheet with a `4px double` outer frame and a header with a Special Elite eyebrow and a Moul H1 over a `3px double` rule. Sections are
numbered in Khmer: ១ colours (swatch cards with shadow-1, the role in Khmer, the hex in Special Elite), ២ type specimens (dashed
row separators), ៣ patterns (5 swatches), ៤ elevation, ៥ components, and a dark-mode strip.

## Responsive rules

- At ≤600px: the zigzag drops to 10px, the header padding to 8/10, the sidebar becomes a drawer, tables scroll in `.rk-table-wrap`, 2-column grids
  collapse to 1, sheet padding drops to 22px and the toolbars wrap.
- Keep hit targets at 44px or more at every size, and never shrink Khmer body text below 15px on phones.
- Shadows stay the same size on phones (3px and 8px). Leave 8px of right and bottom room so the shadows aren't clipped by `overflow`.
