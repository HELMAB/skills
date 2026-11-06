# Tokens: colour, shape, space

All values come from the source canvas. The contrast ratios were measured (WCAG 2.x relative luminance).

## Palette and roles

### Paper (surfaces)
| Name | Hex | Use |
|---|---|---|
| `ground` | `#EADBB8` | Page background behind panels (the desktop backdrop) |
| `paper` | `#F1E4C6` | Default surface: sidebar, splash footer, text colour on ink |
| `sheet` | `#FBF5E6` | Raised sheets: document pages, inputs, cards, menus, tab off-state |
| `paper-muted` | `#D9C7A0` | Secondary text and outline borders **on ink** (9.8:1 on ink) |

### Ink
| Name | Hex | On paper | On sheet | Use |
|---|---|---|---|---|
| `ink` | `#2A1D14` | 12.97 | 15.03 | Body text, borders, shadows, header bar, primary button |
| `ink-muted` | `#5A4632` | 7.07 | 8.19 | Secondary text, captions, counts |
| `ink-faint` | `#6E5B45` | 5.13 | 5.95 | Placeholder text, hints, dashed dividers on ink |

### Spot colours (one role each)
| Name | Hex | Role | Contrast |
|---|---|---|---|
| `red` | `#9E2F18` | **You are here**: current nav item, selected tab, brand seal, error stamp, link | 5.8 on paper; paper on red 5.8 |
| `red-deep` | `#6E1F0F` | Link hover | 8.9 with paper |
| `turmeric` | `#E0A526` | **Highlight and ornament**: `<mark>`, zigzag, rays. Always ink text on it | ink on turmeric 7.46 |
| `turmeric-light` | `#E9B94A` | Alternate ray stripe | decor only |
| `teal` | `#245A57` | **System**: offline banners, saved stamps, download-all, success toast shadow | 6.23 on paper; paper on teal 6.23 |
| `teal-halftone` | `#2F6E6A` + dots `rgba(20,52,50,.25)` | Halftone reader backdrop | decor only |
| `plum` | `#7A3E8E` | Alternate accent for a second product or section | paper on plum 5.73 |

### Accent swaps
`--rk-accent` defaults to red. A product or section may swap it to teal (`data-accent="teal"`) or plum
(`data-accent="plum"`). When the accent is teal, offline and system states move to an ink treatment
(an ink banner with a paper-muted border) so teal keeps a single role per screen.

## Dark mode ("night print")

The ground becomes ink, surfaces become the old ink tone, sheets stay paper-coloured (the printed page is
still paper), and red brightens.

| Token | Dark value | Notes |
|---|---|---|
| bg / ground | `#1C130D` | paper on it 14.5, paper-muted 11.0 |
| surface / raised | `#2A1D14` | |
| sheet | `#E6DCC4` | ink on it 11.99, so document pages stay light |
| text | `#F1E4C6` | |
| text-muted | `#D9C7A0` | |
| edge (borders) | `#6E5B45` | decorative only (2.8:1); never the only cue for state |
| shadow | `#000000` | |
| accent / primary | `#E2735A` | 5.95 on bg; 5.32 on surface; text on it `#1C130D` |
| focus | `#E0A526` | |
| saved (teal text/stamps) | `#6FB3AD` | 6.8 on surface, 7.6 on bg; light sheets keep `#245A57` |
| halftone | `#14100C` + dots `rgba(47,110,106,.35)` | |
| rule | `rgba(217,199,160,.18)` | |

## Shape

| Token | Value | Use |
|---|---|---|
| radius | `0` | everything (exceptions: radio dots, seals, avatars) |
| border | `2px solid ink` | controls, cards, sheets |
| border-double | `4px double ink` | structural edges: sidebar right edge, outer frame, compare split, bottom nav top |
| rule-double | `3px double ink` | under page titles, above and below document meta grids, footer top |
| dashed-2 | `2px dashed` | secondary containers (offline panel in teal), segmented-control dividers, image placeholders |
| dashed-1 | `1px dashed ink` | menu and table row separators, type-specimen rows |
| shadow-1 | `3px 3px 0 ink` | buttons, inputs, chips, current tab, small cards |
| shadow-2 | `8px 8px 0 ink` | sheets, panels, menus, cards |
| primary shadow | `3px 3px 0 red` | the primary (ink) button only |
| drawer shadow | `8px 0 0 rgba(42,29,20,.6)` | off-canvas drawer |
| scrim | `rgba(42,29,20,.55)` | behind drawers and dialogs |

Pressed state: `transform: translate(3px,3px); box-shadow: none`, as if the key prints down onto its shadow.

## Space and size

Spacing uses a 4px base: `4 8 12 16 20 24 32 40 56`.
- Page padding: 24px desktop, 16px phone. Document sheet padding: 56px desktop, 22–28px phone.
- Gaps: 8–12px inside controls, 16–24px between groups, 32px between sheets.
- Hit targets: 44px minimum, 48px for primary actions and pager buttons. Icon size 18px (20–22px in headers).
- Header: 12px × 24px padding on desktop, 8px × 10px on phone. Zigzag strip: 14px desktop, 10px phone.
- Ledger key column: 84px desktop, 72px phone.

## CSS custom properties

The canonical set lives in `assets/retrokh.css` (`--rk-*`). Use the semantic aliases (`--rk-bg`,
`--rk-surface`, `--rk-raised`, `--rk-text`, `--rk-text-muted`, `--rk-edge`, `--rk-accent`,
`--rk-primary`) in components so dark mode and accent swaps work without edits.

## Design-token JSON (for Figma / Style Dictionary)

```json
{
  "color": {
    "ground": "#EADBB8", "paper": "#F1E4C6", "sheet": "#FBF5E6", "paperMuted": "#D9C7A0",
    "ink": "#2A1D14", "inkMuted": "#5A4632", "inkFaint": "#6E5B45",
    "red": "#9E2F18", "redDeep": "#6E1F0F", "turmeric": "#E0A526", "turmericLight": "#E9B94A",
    "teal": "#245A57", "tealHalftone": "#2F6E6A", "plum": "#7A3E8E",
    "dark": { "ground": "#1C130D", "surface": "#2A1D14", "sheet": "#E6DCC4", "edge": "#6E5B45", "accent": "#E2735A", "halftone": "#14100C" }
  },
  "font": { "family": "Google Sans", "weight": { "body": 400, "label": 500, "strong": 700 }, "numeric": "tabular-nums" },
  "shadow": { "1": "3px 3px 0 #2A1D14", "2": "8px 8px 0 #2A1D14" },
  "border": { "width": 2, "doubleStructural": 4, "doubleRule": 3 },
  "radius": 0,
  "space": [4, 8, 12, 16, 20, 24, 32, 40, 56],
  "size": { "touch": 44, "touchPrimary": 48 }
}
```
