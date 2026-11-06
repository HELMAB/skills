# Vue components

Components sit on `assets/retrokh.css` (import it once at the app root) so components stay thin. If the project
uses Tailwind, swap the `rk-*` classes for the recipes in `tailwind.md`. Keep the props and the a11y the same.

## Shared helper

```ts
// khmer.ts
const KM = '០១២៣៤៥៦៧៨៩';
export const toKhmerDigits = (v: string | number) => String(v).replace(/[0-9]/g, (d) => KM[+d]);
export const kmCount = (a: number, b: number) => `${toKhmerDigits(a)} / ${toKhmerDigits(b)}`;
```

## Component set

| Component | Props | Renders |
|---|---|---|
| `RkButton` | `variant: 'primary'\|'system'\|'accent'\|'raised'\|'ghost'`, `iconOnly?`, `label` (aria for icon-only), `as?: 'button'\|'a'`, `href?`; slots: default, `icon` | `.rk-btn .rk-btn-{variant}` |
| `RkHeader` | `title`, `subtitle?`; slots: `start`, `actions` | ink bar + zigzag |
| `RkSheet` | `as?` | `.rk-sheet` |
| `RkCard` | `title?` (ink head), `index?` (Khmer-numbered `១ · title`) | `.rk-card` |
| `RkInput` | `id`, `label`, `v-model`, `error?`, `hideLabel?`; slot: `icon` | label + `.rk-input` + error text |
| `RkTabs` | `items: {id,label}[]`, `v-model` | `.rk-tabs` with roving tabindex |
| `RkLedger` | `groups: {key, sub?, count, items: {label, href, current?, saved?}[]}[]`, `label` | ruled ledger nav |
| `RkStamp` | `tone: 'saved'\|'fail'`, `text` | `.rk-stamp` (aria-hidden) |
| `RkPager` | `current`, `total`, `prevHref`, `nextHref` | segmented pager with Koulen counter |
| `RkProgress` | `value` 0–100, `label`, `tone?: 'ink'\|'system'`, `striped?` | `.rk-progress` + `role="progressbar"` |
| `RkToast` | `message`, `v-model:open` | `.rk-toast` in a `role="status"` region |
| `RkEmpty` | `title`, `hint` | `.rk-empty` |
| `RkDrawer` | `v-model:open`, `title`; emits `close` | scrim + `.rk-drawer` (focus trap, Esc) |
| `RkMenu` | `items: {label, icon?}[]`; emits `select` | `.rk-menu` with arrow keys |

## Vue 3 (`<script setup>`) examples

```vue
<!-- RkButton.vue -->
<script setup lang="ts">
withDefaults(defineProps<{
  variant?: 'primary' | 'system' | 'accent' | 'raised' | 'ghost';
  iconOnly?: boolean;
  label?: string;          // required when iconOnly: becomes the aria-label
  as?: 'button' | 'a';
  href?: string;
}>(), { variant: 'ghost', as: 'button' });
</script>
<template>
  <component :is="as" :href="as === 'a' ? href : undefined" :aria-label="iconOnly ? label : undefined"
    :class="['rk-btn', `rk-btn-${variant}`, { 'rk-btn-icon': iconOnly }]">
    <slot name="icon" /><slot v-if="!iconOnly" />
  </component>
</template>
```

```vue
<!-- RkHeader.vue -->
<script setup lang="ts">
defineProps<{ title: string; subtitle?: string }>();
</script>
<template>
  <header class="rk-header">
    <slot name="start" />
    <div style="flex:1 1 240px;min-width:0;display:flex;flex-direction:column;align-items:center;text-align:center">
      <span class="rk-display" style="font-size:20px">{{ title }}</span>
      <span v-if="subtitle" class="rk-small" style="color:var(--rk-paper-muted)">{{ subtitle }}</span>
    </div>
    <div style="display:flex;gap:8px"><slot name="actions" /></div>
  </header>
  <div class="rk-zigzag" aria-hidden="true"></div>
</template>
```

```vue
<!-- RkStamp.vue -->
<script setup lang="ts">
withDefaults(defineProps<{ tone?: 'saved' | 'fail'; text: string }>(), { tone: 'saved' });
</script>
<template>
  <span :class="['rk-stamp', `rk-stamp-${tone}`]" aria-hidden="true">{{ text }}</span>
</template>
```

```vue
<!-- RkPager.vue -->
<script setup lang="ts">
import { toKhmerDigits } from './khmer';
defineProps<{ current: number; total: number; prevHref: string; nextHref: string }>();
</script>
<template>
  <nav class="rk-segmented" aria-label="មុន និងបន្ទាប់">
    <a :href="prevHref">
      <svg class="rk-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" aria-hidden="true"><path d="M15 6l-6 6 6 6" /></svg>មុន
    </a>
    <span class="rk-numeral" style="font-size:18px;font-weight:400">{{ toKhmerDigits(current) }} / {{ toKhmerDigits(total) }}</span>
    <a :href="nextHref" class="is-primary">បន្ទាប់
      <svg class="rk-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" aria-hidden="true"><path d="M9 6l6 6-6 6" /></svg>
    </a>
  </nav>
</template>
```

```vue
<!-- RkProgress.vue -->
<script setup lang="ts">
import { toKhmerDigits } from './khmer';
withDefaults(defineProps<{ value: number; label: string; tone?: 'ink' | 'system'; striped?: boolean }>(), { tone: 'ink' });
</script>
<template>
  <div :class="['rk-progress', { 'is-system': tone === 'system', 'is-striped': striped }]"
    role="progressbar" :aria-label="label" aria-valuemin="0" aria-valuemax="100"
    :aria-valuenow="value" :aria-valuetext="`${toKhmerDigits(value)}%`">
    <span :style="{ width: `${value}%` }"></span>
  </div>
</template>
```

```vue
<!-- RkInput.vue -->
<script setup lang="ts">
defineProps<{ id: string; label: string; placeholder?: string; error?: string; hideLabel?: boolean }>();
const model = defineModel<string>();
</script>
<template>
  <div class="rk-field">
    <label :for="id" :class="hideLabel ? 'rk-sr' : 'rk-label'">{{ label }}</label>
    <div class="rk-input" :class="{ 'is-invalid': error }">
      <slot name="icon" />
      <input :id="id" v-model="model" :placeholder="placeholder"
             :aria-invalid="!!error" :aria-describedby="error ? `${id}-err` : undefined" />
    </div>
    <span v-if="error" :id="`${id}-err`" class="rk-error-text">{{ error }}</span>
  </div>
</template>
```

```vue
<!-- RkLedger.vue -->
<script setup lang="ts">
import { ref } from 'vue';
import { toKhmerDigits } from './khmer';
type Item = { label: string; href: string; current?: boolean; saved?: boolean };
type Group = { key: string | number; sub?: string; count: string; items: Item[] };
const props = defineProps<{ groups: Group[]; label: string }>();
const open = ref(props.groups.findIndex(g => g.items.some(i => i.current)));
</script>
<template>
  <nav class="rk-ruled" :aria-label="label">
    <template v-for="(g, gi) in groups" :key="gi">
      <button class="rk-ledger-row" :aria-expanded="open === gi" @click="open = open === gi ? -1 : gi">
        <span class="rk-ledger-key">{{ toKhmerDigits(g.key) }}
          <small v-if="g.sub" style="font-family:var(--rk-font-body);font-size:12px;font-weight:700">{{ g.sub }}</small>
        </span>
        <span class="rk-ledger-text rk-muted">{{ g.count }}</span>
      </button>
      <ol v-if="open === gi" class="rk-ledger">
        <li v-for="it in g.items" :key="it.href" class="rk-ledger-row">
          <span class="rk-ledger-key" aria-hidden="true"></span>
          <a v-if="it.current" :href="it.href" aria-current="page" class="rk-current">{{ it.label }}</a>
          <a v-else :href="it.href" class="rk-ledger-text" style="color:inherit;text-decoration:none"
             :aria-label="it.saved ? `${it.label} — បានទាញយក` : undefined">
            {{ it.label }}<span v-if="it.saved" class="rk-stamp rk-stamp-saved" aria-hidden="true">បានទាញយក</span>
          </a>
        </li>
      </ol>
    </template>
  </nav>
</template>
```

## shadcn-vue / Reka UI / headless kits

If the project already has a component kit, **restyle it rather than replacing it**. Set the CSS variables to
RetroKh values (`--radius: 0`, background → paper, foreground → ink, primary → ink, accent → red, ring → red),
override the shadows to the two hard levels, and swap the fonts. Keep the kit's a11y behaviour (focus traps, roving
tabindex) and change only the skin.

## Behaviour notes

- Drawer and dialog: trap focus, close on Esc and scrim click, and return focus to the trigger. Lock body scroll.
- Toasts: one live region (`role="status"`), at least 5s, and pause on hover or focus.
- The pager counter and every Koulen number go through `toKhmerDigits`. `aria-valuetext` uses Khmer digits too.
- Theme toggle: set `document.documentElement.dataset.theme = 'dark' | 'light'`. The default follows `prefers-color-scheme`.
