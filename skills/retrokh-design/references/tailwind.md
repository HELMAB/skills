# Tailwind CSS

## Setup

- **v4**: copy `assets/tailwind.v4.css` into the project (e.g. `src/styles/retrokh.css`) and add
  `@import "./retrokh.css";` after `@import "tailwindcss";`. It defines the `rk-*` colours, `font-display`,
  `font-numeral`, `font-body`, `font-latin`, the `shadow-rk-1` and `shadow-rk-2` shadows, the pattern utilities (`bg-rk-zigzag`…), `press`,
  and resets every radius to 0.
- **v3**: copy `assets/tailwind.preset.js` and add `presets: [require('./retrokh.preset.js')]`. For dark mode
  and the semantic `rk-accent`/`rk-surface`/`rk-text` colours, also include the `:root` variable blocks from
  `assets/retrokh.css` (sections 1 and 2) in your global CSS.
- Both: add the Google Fonts `<link>` and set `<html lang="km">`.

Dark mode in v4 is class-based via `data-theme="dark"`. Use `dark:` variants with the night values:
`bg-rk-paper dark:bg-rk-ink`, `text-rk-ink dark:text-rk-paper`, `bg-rk-red dark:bg-rk-red-night`,
`shadow-rk-2 dark:shadow-rk-black-2`, `border-rk-ink dark:border-rk-edge-night`.

## Class recipes

```html
<!-- App root -->
<body class="bg-rk-ground text-rk-ink font-body text-base leading-km">

<!-- Header + zigzag -->
<header class="flex flex-wrap items-center gap-4 bg-rk-ink px-6 py-3 text-rk-paper max-sm:px-2.5 max-sm:py-2">
  <button aria-label="បើកបញ្ជីឯកសារ" class="grid size-touch place-items-center border-2 border-rk-paper-muted">…</button>
  <div class="flex flex-col">
    <span class="font-display text-xl leading-normal">បាក់ឌុប</span>
    <span class="font-latin text-xs tracking-latin text-rk-paper-muted">DOBPI</span>
  </div>
</header>
<div class="h-3.5 bg-rk-zigzag max-sm:h-2.5" aria-hidden="true"></div>

<!-- Primary button -->
<button class="press inline-flex min-h-touch-lg items-center gap-1.5 border-2 border-rk-ink bg-rk-ink px-[18px] font-bold text-rk-paper shadow-rk-primary">
  បន្ទាប់ <svg …/>
</button>

<!-- Ghost / secondary -->
<button class="press inline-flex min-h-touch items-center gap-1.5 border-2 border-rk-ink bg-transparent px-4">ទាញយក</button>

<!-- System -->
<button class="press min-h-touch border-2 border-rk-ink bg-rk-teal px-4 font-bold text-rk-paper shadow-rk-1">ទាញយកទាំងអស់</button>

<!-- Search input -->
<label for="q" class="text-sm font-bold text-rk-ink-muted">ស្វែងរក</label>
<div class="flex h-touch items-center gap-2 border-2 border-rk-ink bg-rk-sheet px-3 shadow-rk-1 focus-within:outline-3 focus-within:outline-offset-2 focus-within:outline-rk-red">
  <svg …/><input id="q" type="search" class="min-w-0 flex-1 bg-transparent outline-none placeholder:text-rk-ink-faint" placeholder="មុខវិជ្ជា ឬឆ្នាំ…">
</div>

<!-- Tabs -->
<div role="tablist" class="grid grid-cols-2">
  <button role="tab" aria-selected="false" class="min-h-touch-lg border-2 border-rk-ink bg-rk-sheet font-bold">សង្គម</button>
  <button role="tab" aria-selected="true"  class="min-h-touch-lg border-2 border-l-0 border-rk-ink bg-rk-red font-bold text-rk-paper">វិទ្យាសាស្ត្រពិត</button>
</div>

<!-- Ledger row + current item -->
<nav class="bg-rk-ruled flex flex-col">
  <li class="flex h-touch items-center">
    <span class="h-touch w-[84px] shrink-0 border-r-2 border-rk-red" aria-hidden="true"></span>
    <a href="#" aria-current="page" class="mx-3 flex h-9 flex-1 items-center bg-rk-red px-3 font-bold text-rk-paper shadow-rk-1">២. គណិតវិទ្យា</a>
  </li>
</nav>

<!-- Sheet on halftone -->
<main class="bg-rk-halftone flex flex-col items-center gap-8 px-6 pt-10">
  <article class="w-full max-w-[720px] border-2 border-rk-ink bg-rk-sheet p-14 shadow-rk-2 max-sm:p-6">…</article>
</main>

<!-- Stamp -->
<span class="rk-stamp text-rk-teal" aria-hidden="true">បានទាញយក</span>

<!-- Card with ink head -->
<section class="flex flex-col border-2 border-rk-ink bg-rk-sheet shadow-rk-2">
  <h2 class="bg-rk-ink px-3 py-1 text-sm font-bold text-rk-paper">១ · កំពុងផ្ទុក</h2>
  <div class="p-4">…</div>
</section>

<!-- Koulen counter -->
<span class="font-numeral text-lg">១៣៣ / ១៣៨</span>
```

## Rules for Tailwind output

- Never emit `rounded-*` except `rounded-full` on radios and seals. The v4 theme removes the radius scale on purpose.
- Never emit `shadow-sm|md|lg|xl` or `blur-*`. Use only `shadow-rk-1`, `shadow-rk-2` and `shadow-rk-primary`.
- Never emit `bg-gradient-*`; the only allowed gradients are the `bg-rk-*` pattern utilities.
- `font-display` is only for text ≥16px (`text-base` and up). Pair it with `leading-[1.6]`–`leading-[1.8]`, never `leading-none` or `leading-tight`.
- No `tracking-*` or `uppercase` on Khmer; `tracking-latin uppercase` only goes with `font-latin`.
