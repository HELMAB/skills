# Stacks

Follow the project's own conventions (file locations, TypeScript or JS, Composition or Options API, lint rules). Classes
from `classes.md` work in any framework that renders HTML; in JSX, write `className`.

## Contents
- [Tailwind v4](#tailwind-v4) · [Tailwind v3](#tailwind-v3) · [Vue 3](#vue-3) · [shadcn / shadcn-vue](#shadcn--shadcn-vue) · [Bootstrap 5 / 4](#bootstrap-5--4)

## Tailwind v4
`cp assets/tailwind.v4.css src/styles/retrokh.css`, then add `@import "./retrokh.css";` after `@import "tailwindcss";`.
For dark mode, set `data-theme="dark"` on `<html>` and use `dark:` variants.

| Need | Utilities |
|---|---|
| Colours | `bg-rk-{ground,paper,sheet,ink,red,turmeric,teal,plum,night}`, `text-rk-ink-muted`, `border-rk-ink`, `dark:bg-rk-ink` |
| Shadows | `shadow-rk-1` (controls), `shadow-rk-2` (sheets), `shadow-rk-primary`; dark mode `shadow-rk-black-1` / `shadow-rk-black-2` |
| Patterns | `bg-rk-zigzag` `bg-rk-halftone` `bg-rk-halftone-night` `bg-rk-rays` `bg-rk-ruled` `bg-rk-diamonds` `bg-rk-hatch` |
| Misc | `press` (3px press), `border-rk-double`, `min-h-touch` / `min-h-touch-lg` (44/48px), `tracking-latin`, `rk-stamp` |
| Type | `font-sans` (Google Sans), `font-normal` / `font-medium` / `font-bold`, `tabular-nums`; Khmer headings `leading-[1.5]` |

```html
<button class="press inline-flex min-h-touch-lg items-center gap-1.5 border-2 border-rk-ink bg-rk-ink px-[18px] font-bold text-rk-paper shadow-rk-primary">បន្ទាប់</button>
<article class="border-2 border-rk-ink bg-rk-sheet p-6 shadow-rk-2"><h3 class="font-bold leading-[1.7]">…</h3></article>
<span class="rk-stamp text-rk-teal" aria-hidden="true">ថ្មី</span>
```
Banned: `rounded-*` (except `rounded-full` for radios and seals), `shadow-sm` through `shadow-2xl`, `blur-*`, `bg-gradient-*`,
`font-serif`, `font-mono`, `font-light`, `font-extrabold`, `font-black`, `bg-white`, `bg-black`. `check_retrokh.py` flags them.

## Tailwind v3
`cp assets/tailwind.preset.js retrokh.preset.js`, then add `presets: [require('./retrokh.preset.js')]` to the config. Colours,
`shadow-rk-1/2/primary`, the patterns (except `bg-rk-halftone-night`), `press`, `min-h-touch` and `rk-stamp` match v4. There are no
`shadow-rk-black-*` utilities in v3: copy `assets/retrokh.css` for its `:root` variables and dark mode, and use `rk-accent` / `rk-text` / `rk-surface`.

## Vue 3
Use `<script setup lang="ts">` (or JS if that's what the project uses). Put components where the project keeps them. The skin
comes from `retrokh.css` or Tailwind, so components stay thin. Write the helper once:
```ts
// khmer.ts
const KM = '០១២៣៤៥៦៧៨៩';
export const toKhmerDigits = (v: string | number) => String(v).replace(/[0-9]/g, (d) => KM[+d]);
```
```vue
<!-- RkButton.vue: primary | system | accent | raised | ghost | paper -->
<script setup lang="ts">
withDefaults(defineProps<{ variant?: 'primary' | 'system' | 'accent' | 'raised' | 'ghost' | 'paper';
  iconOnly?: boolean; label?: string; href?: string }>(), { variant: 'ghost' });
</script>
<template>
  <component :is="href ? 'a' : 'button'" :href="href" :aria-label="iconOnly ? label : undefined"
    :class="['rk-btn', `rk-btn-${variant}`, { 'rk-btn-icon': iconOnly }]"><slot name="icon" /><slot v-if="!iconOnly" /></component>
</template>
```
```vue
<!-- RkSection.vue -->
<script setup lang="ts">
import { useId } from 'vue';
withDefaults(defineProps<{ eyebrow?: string; title: string; tone?: 'ground' | 'paper' | 'ink' | 'halftone'; center?: boolean; id?: string }>(),
  { tone: 'ground' });
const hid = useId();
</script>
<template>
  <section :id="id" :aria-labelledby="hid" :class="['rk-section', { 'rk-section-paper': tone === 'paper',
    'rk-section-ink': tone === 'ink', 'rk-halftone': tone === 'halftone' }]">
    <div class="rk-container">
      <div :class="['rk-section-head', { 'is-center': center }]">
        <span v-if="eyebrow" class="rk-eyebrow">{{ eyebrow }}</span>
        <h2 :id="hid" class="rk-section-title">{{ title }}</h2>
      </div>
      <slot />
    </div>
  </section>
</template>
```
```vue
<!-- RkSiteNav.vue: add document.documentElement.classList.add('js') once in main.ts -->
<script setup lang="ts">
import { ref } from 'vue';
defineProps<{ brand: string; links: { label: string; href: string; current?: boolean }[] }>();
const open = ref(false);
</script>
<template>
  <header class="rk-nav" :data-open="open || undefined"><div class="rk-container rk-nav-inner">
    <a class="rk-nav-brand" href="/"><span class="rk-display">{{ brand }}</span></a>
    <button class="rk-btn rk-btn-ghost rk-btn-icon rk-nav-toggle" aria-label="ម៉ឺនុយ" :aria-expanded="open"
      aria-controls="rk-links" @click="open = !open">
      <svg class="rk-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16" /></svg>
    </button>
    <nav style="display:contents"><ul id="rk-links" class="rk-nav-links">
      <li v-for="l in links" :key="l.href"><a :href="l.href" :aria-current="l.current ? 'page' : undefined" @click="open = false">{{ l.label }}</a></li>
    </ul></nav>
  </div></header>
  <div class="rk-zigzag" aria-hidden="true"></div>
</template>
```
For anything else (inputs, stamps, pager, ledger), build a thin component around the markup in `classes.md`. Use `v-model` for
fields, and give every icon-only button a Khmer `aria-label`. Drawers and dialogs need a focus trap, Esc to close and focus returned on close.

## shadcn / shadcn-vue
Keep the kit (it handles a11y) and swap only the skin. In the global CSS:
```css
:root {
  --background:#EADBB8; --foreground:#2A1D14; --card:#FBF5E6; --card-foreground:#2A1D14; --popover:#FBF5E6;
  --popover-foreground:#2A1D14; --primary:#2A1D14; --primary-foreground:#F1E4C6; --secondary:#F1E4C6;
  --secondary-foreground:#2A1D14; --muted:#F1E4C6; --muted-foreground:#5A4632; --accent:#E0A526; --accent-foreground:#2A1D14;
  --destructive:#9E2F18; --border:#2A1D14; --input:#2A1D14; --ring:#9E2F18; --radius:0rem;
}
.dark { --background:#1C130D; --foreground:#F1E4C6; --card:#E6DCC4; --card-foreground:#2A1D14; --primary:#E2735A;
  --primary-foreground:#1C130D; --border:#6E5B45; --input:#6E5B45; --ring:#E0A526; --muted:#2A1D14; --muted-foreground:#D9C7A0; }
body { font-family: 'Google Sans', sans-serif; }
```
Then make borders `border-2` and swap the kit's `shadow-*` for `shadow-rk-1` / `shadow-rk-2` on cards, buttons and popovers.

## Bootstrap 5 / 4
Override the Sass variables before the import. This works in Bootstrap-Vue (Bootstrap 4) and Bootstrap 5:
```scss
$font-family-sans-serif: "Google Sans", sans-serif;
$enable-rounded: false; $enable-gradients: false; $enable-shadows: true;
$body-bg: #EADBB8; $body-color: #2A1D14; $border-color: #2A1D14; $border-width: 2px;
$primary: #2A1D14; $secondary: #5A4632; $danger: #9E2F18; $warning: #E0A526; $info: #245A57; $success: #245A57;
$light: #F1E4C6; $dark: #2A1D14; $link-color: #9E2F18; $headings-font-weight: 700; $font-weight-bold: 700;
$card-bg: #FBF5E6; $input-bg: #FBF5E6; $input-border-color: #2A1D14; $dropdown-bg: #FBF5E6; $modal-content-bg: #FBF5E6;
$box-shadow-sm: 3px 3px 0 #2A1D14; $box-shadow: 8px 8px 0 #2A1D14; $box-shadow-lg: 8px 8px 0 #2A1D14;
$btn-box-shadow: 3px 3px 0 #2A1D14; $input-box-shadow: none; $input-focus-box-shadow: 0 0 0 3px #9E2F18;
@import "bootstrap/scss/bootstrap";
.btn-primary { box-shadow: 3px 3px 0 #9E2F18; }
.card, .dropdown-menu, .modal-content { box-shadow: 8px 8px 0 #2A1D14; }
```
If the project already has a brand palette, keep its primary as the accent only when it reaches 4.5:1 on paper. Otherwise ask before overriding it.
