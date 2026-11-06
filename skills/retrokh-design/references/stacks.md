# Stacks

Copy these files with `cp` from this skill's folder. Don't Read them first; this table says what each one does. Put them where
the project keeps similar files, and follow its conventions (JS or TS, lint, naming).

| Project | Copy | Then |
|---|---|---|
| Plain HTML, React/JSX, Svelte, Astro | `assets/retrokh.css` | import or link it once; use the `classes.md` classes (`className` in JSX) |
| Laravel Blade | `assets/retrokh.css` → `resources/css/` | `@import` it in `app.css` (Vite); classes go straight into Blade |
| Tailwind v4 | `assets/tailwind.v4.css` | `@import "./retrokh.css";` after `@import "tailwindcss";` |
| Tailwind v3 | `assets/tailwind.preset.js` + `assets/retrokh.css` | `presets: [require('./tailwind.preset.js')]`; the CSS adds `:root` variables and dark mode |
| Vue 3 | `assets/vue/*.vue`, `assets/js/khmer.js` + the CSS (or Tailwind) | `<script setup>` JS with runtime props, so they work in JS and TS projects |
| Vue 2 / Bootstrap-Vue | `assets/bootstrap/_retrokh.scss` | import it before Bootstrap; use the classes in templates (no `<script setup>`) |
| Bootstrap 5 | `assets/bootstrap/_retrokh.scss` | `@import "retrokh"; @import "bootstrap/scss/bootstrap";` |
| shadcn/ui, shadcn-vue | `assets/shadcn/retrokh-shadcn.css` + `tailwind.v4.css` | keep the kit; add `border-2` and swap `shadow-*` for `shadow-rk-1` / `shadow-rk-2` |

## Vue components (`assets/vue/`)
- `RkButton` (`variant`: primary · system · accent · raised · ghost · paper; `iconOnly` + `label`; `href` renders an `<a>`)
- `RkSection` (`title`, `eyebrow`, `tone`: ground · paper · ink · halftone; `center`)
- `RkSiteNav` (`brand`, `links: [{ label, href, current }]`; call `document.documentElement.classList.add('js')` once in `main.js`)

For anything else (inputs, stamps, pager, ledger, cards), write a thin component around the `classes.md` markup. Use
`v-model` for fields and show numerals with `toKhmerDigits` from `khmer.js`. Drawers and dialogs need a focus trap, Esc
to close, and focus returned to the trigger.

## Tailwind utilities (v4; v3 is the same minus `shadow-rk-black-*` and `bg-rk-halftone-night`)
- **Colours:** `bg-rk-{ground,paper,sheet,ink,red,turmeric,teal,plum,night}`, `text-rk-ink-muted`, `border-rk-ink`
- **Shadows:** `shadow-rk-1`, `shadow-rk-2`, `shadow-rk-primary`; on dark: `dark:shadow-rk-black-1` / `-2`
- **Patterns:** `bg-rk-{zigzag,halftone,rays,ruled,diamonds,hatch}`. Also `press`, `border-rk-double`,
  `min-h-touch` / `min-h-touch-lg`, `tracking-latin`, `rk-stamp`
- **Type:** `font-sans`, `font-normal` / `font-medium` / `font-bold`, `tabular-nums`; Khmer headings use `leading-[1.5]`
- **Banned (the checker flags these):** `rounded-*` (except `rounded-full`), `shadow-sm` through `shadow-2xl`, `blur-*`,
  `bg-gradient-*`, `font-serif`, `font-mono`, `font-light`, `font-extrabold`, `font-black`, `bg-white`, `bg-black`
