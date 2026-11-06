# Vue and React components

Both builds sit on `assets/retrokh.css` (import it once at the app root) so components stay thin. If the project
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
| `RkButton` | `variant: 'primary'\|'system'\|'accent'\|'raised'\|'ghost'`, `icon?`, `iconOnly?`, `label` (aria for icon-only), `as?: 'button'\|'a'` | `.rk-btn .rk-btn-{variant}` |
| `RkHeader` | `title`, `subtitle?`, `brand?`, slots: `start`, `actions` | ink bar + zigzag |
| `RkSheet` | `as?` | `.rk-sheet` |
| `RkCard` | `title?` (ink head), `index?` (Khmer-numbered `១ · title`) | `.rk-card` |
| `RkInput` | `id`, `label`, `modelValue`/`value`, `icon?`, `error?`, `hideLabel?` | label + `.rk-input` + error text |
| `RkTabs` | `items: {id,label}[]`, `modelValue`/`value` | `.rk-tabs` with roving tabindex |
| `RkLedger` | `groups: {key, sub?, count, items: {label, href, current?, saved?}[]}[]` | ruled ledger nav |
| `RkStamp` | `tone: 'saved'\|'fail'`, `text` | `.rk-stamp` (aria-hidden) |
| `RkPager` | `current`, `total`, `prevHref`, `nextHref` | segmented pager with Koulen counter |
| `RkProgress` | `value` 0–100, `tone?: 'ink'\|'system'`, `striped?` | `.rk-progress` + `role="progressbar"` |
| `RkToast` | `message`, `open` | `.rk-toast` in a `role="status"` region |
| `RkEmpty` | `title`, `hint` | `.rk-empty` |
| `RkDrawer` | `open`, `title`, `@close` | scrim + `.rk-drawer` (focus trap, Esc) |
| `RkMenu` | `items: {label, icon?, onSelect}[]` | `.rk-menu` with arrow keys |

## React examples

```tsx
import { toKhmerDigits } from './khmer';
import type { ReactNode, ButtonHTMLAttributes } from 'react';

type Variant = 'primary' | 'system' | 'accent' | 'raised' | 'ghost';
export function RkButton({ variant = 'ghost', icon, iconOnly, label, children, ...rest }:
  ButtonHTMLAttributes<HTMLButtonElement> & { variant?: Variant; icon?: ReactNode; iconOnly?: boolean; label?: string }) {
  return (
    <button {...rest} aria-label={iconOnly ? label : undefined}
      className={`rk-btn rk-btn-${variant}${iconOnly ? ' rk-btn-icon' : ''} ${rest.className ?? ''}`}>
      {icon}{!iconOnly && children}
    </button>
  );
}

export function RkHeader({ title, subtitle, start, actions }:
  { title: string; subtitle?: string; start?: ReactNode; actions?: ReactNode }) {
  return (<>
    <header className="rk-header">
      {start}
      <div style={{ flex: '1 1 240px', minWidth: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
        <span className="rk-display" style={{ fontSize: 20 }}>{title}</span>
        {subtitle && <span className="rk-small" style={{ color: 'var(--rk-paper-muted)' }}>{subtitle}</span>}
      </div>
      <div style={{ display: 'flex', gap: 8 }}>{actions}</div>
    </header>
    <div className="rk-zigzag" aria-hidden="true" />
  </>);
}

export function RkStamp({ tone = 'saved', text }: { tone?: 'saved' | 'fail'; text: string }) {
  return <span className={`rk-stamp rk-stamp-${tone}`} aria-hidden="true">{text}</span>;
}

export function RkPager({ current, total, prevHref, nextHref }:
  { current: number; total: number; prevHref: string; nextHref: string }) {
  return (
    <nav className="rk-segmented" aria-label="មុន និងបន្ទាប់">
      <a href={prevHref}><Chevron dir="left" />មុន</a>
      <span className="rk-numeral" style={{ fontSize: 18 }}>{toKhmerDigits(current)} / {toKhmerDigits(total)}</span>
      <a href={nextHref} className="is-primary">បន្ទាប់<Chevron dir="right" /></a>
    </nav>
  );
}

export function RkProgress({ value, label, tone = 'ink', striped }:
  { value: number; label: string; tone?: 'ink' | 'system'; striped?: boolean }) {
  return (
    <div className={`rk-progress${tone === 'system' ? ' is-system' : ''}${striped ? ' is-striped' : ''}`}
      role="progressbar" aria-label={label} aria-valuemin={0} aria-valuemax={100} aria-valuenow={value}
      aria-valuetext={`${toKhmerDigits(value)}%`}>
      <span style={{ width: `${value}%` }} />
    </div>
  );
}

const Chevron = ({ dir }: { dir: 'left' | 'right' }) => (
  <svg className="rk-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2.6} aria-hidden="true">
    <path d={dir === 'left' ? 'M15 6l-6 6 6 6' : 'M9 6l6 6-6 6'} />
  </svg>
);
```

## Vue 3 (`<script setup>`) examples

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

## shadcn-vue / shadcn/ui / headless kits

If the project already has a component kit, **restyle it rather than replacing it**. Set the CSS variables to
RetroKh values (`--radius: 0`, background → paper, foreground → ink, primary → ink, accent → red, ring → red),
override the shadows to the two hard levels, and swap the fonts. Keep the kit's a11y behaviour (focus traps, roving
tabindex) and change only the skin.

## Behaviour notes

- Drawer and dialog: trap focus, close on Esc and scrim click, and return focus to the trigger. Lock body scroll.
- Toasts: one live region (`role="status"`), at least 5s, and pause on hover or focus.
- The pager counter and every Koulen number go through `toKhmerDigits`. `aria-valuetext` uses Khmer digits too.
- Theme toggle: set `document.documentElement.dataset.theme = 'dark' | 'light'`. The default follows `prefers-color-scheme`.
