# Tailwind CSS

## Contents

- [Setup](#setup)
- [Class recipes](#class-recipes)
- [Rules for Tailwind output](#rules-for-tailwind-output)
- [Website sections](#website-sections)

## Setup

- **v4**: copy `assets/tailwind.v4.css` into the project (e.g. `src/styles/retrokh.css`) and add
  `@import "./retrokh.css";` after `@import "tailwindcss";`. It defines the `rk-*` colours, sets `font-sans`
  to Google Sans (the only typeface), the `shadow-rk-1` and `shadow-rk-2` shadows, the pattern utilities (`bg-rk-zigzag`…), `press`,
  and resets every radius to 0.
- **v3**: copy `assets/tailwind.preset.js` and add `presets: [require('./retrokh.preset.js')]`. For dark mode
  and the semantic `rk-accent`/`rk-surface`/`rk-text` colours, also include the `:root` variable blocks from
  `assets/retrokh.css` (sections 1 and 2) in your global CSS.
- Both: add `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400..700&display=swap">`
  and set `<html lang="km">`. Type roles come from weight: `font-normal` (body), `font-medium` (Latin caps labels),
  `font-bold` (headings and numerals, plus `tabular-nums` for numerals).

Dark mode in v4 is class-based via `data-theme="dark"`. Use `dark:` variants with the night values:
`bg-rk-paper dark:bg-rk-ink`, `text-rk-ink dark:text-rk-paper`, `bg-rk-red dark:bg-rk-red-night`,
`shadow-rk-2 dark:shadow-rk-black-2`, `border-rk-ink dark:border-rk-edge-night`.

## Class recipes

```html
<!-- App root -->
<body class="bg-rk-ground text-rk-ink font-sans text-base leading-km">

<!-- Header + zigzag -->
<header class="flex flex-wrap items-center gap-4 bg-rk-ink px-6 py-3 text-rk-paper max-sm:px-2.5 max-sm:py-2">
  <button aria-label="បើកបញ្ជីឯកសារ" class="grid size-touch place-items-center border-2 border-rk-paper-muted">…</button>
  <div class="flex flex-col">
    <span class="font-bold text-xl leading-normal">បាក់ឌុប</span>
    <span class="text-xs font-medium uppercase tracking-latin text-rk-paper-muted">DOBPI</span>
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

<!-- Counter: bold tabular figures -->
<span class="font-bold tabular-nums text-lg">១៣៣ / ១៣៨</span>
```

## Rules for Tailwind output

- Never emit `rounded-*` except `rounded-full` on radios and seals. The v4 theme removes the radius scale on purpose.
- Never emit `shadow-sm|md|lg|xl` or `blur-*`. Use only `shadow-rk-1`, `shadow-rk-2` and `shadow-rk-primary`.
- Never emit `bg-gradient-*`; the only allowed gradients are the `bg-rk-*` pattern utilities.
- Use only `font-sans` (Google Sans) and only the weights `font-normal`, `font-medium` and `font-bold`. Never use `font-serif`, `font-mono`,
  `font-extrabold` or `font-black`.
- Khmer headings: `font-bold` with `leading-[1.5]`–`leading-[1.7]`, never `leading-none` or `leading-tight` (those are for Latin only).
- No `tracking-*` or `uppercase` on Khmer; `tracking-latin uppercase` is only for short Latin labels.

## Website sections

Websites can mix both approaches: import `retrokh.css` for the section classes in `websites.md`, and use Tailwind for
layout. Or build them in pure utilities:

```html
<!-- Sticky site nav (phone menu: toggle `hidden` on #links with a button + aria-expanded) -->
<header class="sticky top-0 z-20 bg-rk-ink text-rk-paper">
  <div class="mx-auto flex min-h-[68px] w-[min(100%-32px,1200px)] flex-wrap items-center gap-x-4 gap-y-2 py-2">
    <a href="/" class="mr-auto font-bold text-xl leading-normal">[ ឈ្មោះ ]</a>
    <ul id="links" class="flex flex-wrap gap-1 max-md:hidden max-md:w-full max-md:flex-col">
      <li><a aria-current="page" class="flex min-h-touch items-center bg-rk-red px-3 font-bold">ទំព័រដើម</a></li>
      <li><a href="#about" class="flex min-h-touch items-center border-b-[3px] border-transparent px-3 font-bold hover:border-rk-turmeric">អំពីយើង</a></li>
    </ul>
  </div>
</header>
<div class="h-3.5 bg-rk-zigzag max-sm:h-2.5" aria-hidden="true"></div>

<!-- Hero: copy on a plate over rays -->
<section class="bg-rk-rays py-[72px] max-md:py-10">
  <div class="mx-auto grid w-[min(100%-32px,1200px)] items-center gap-12 md:grid-cols-[1.1fr_.9fr]">
    <div class="flex flex-col items-start gap-4 border-2 border-rk-ink bg-rk-sheet p-10 shadow-rk-2 max-md:p-6">
      <span class="font-bold tabular-nums text-[17px] text-rk-red">០១ · ស្វាគមន៍</span>
      <h1 class="font-bold text-[clamp(32px,5vw,56px)] leading-[1.5]">…</h1>
      <p class="max-w-[62ch] text-lg leading-[1.8] text-rk-ink-muted">…</p>
    </div>
    <!-- printed photo -->
    <figure class="-rotate-[1.5deg] border-2 border-rk-ink bg-rk-sheet p-2.5 shadow-rk-2">
      <img src="…" alt="…" class="aspect-[4/3] w-full border-2 border-rk-ink object-cover [filter:sepia(.35)_saturate(.85)_contrast(1.05)]">
      <figcaption class="pt-2 text-sm text-rk-ink-muted">…</figcaption>
    </figure>
  </div>
</section>

<!-- Section head -->
<div class="mb-9 flex flex-col gap-1">
  <span class="font-bold tabular-nums text-[17px] text-rk-red">០២ · សេវាកម្ម</span>
  <h2 class="border-b-[3px] border-double border-rk-ink pb-2.5 font-bold text-[clamp(24px,3.2vw,34px)] leading-[1.6]">…</h2>
</div>

<!-- CTA band between zigzags -->
<div class="h-3.5 bg-rk-zigzag" aria-hidden="true"></div>
<section class="bg-rk-ink py-14 text-center text-rk-paper">…
  <a class="press inline-flex min-h-touch-lg items-center border-2 border-rk-paper bg-rk-paper px-5 font-bold text-rk-ink shadow-rk-primary">…</a>
</section>
<div class="h-3.5 bg-rk-zigzag" aria-hidden="true"></div>
```
English-primary pages: on Latin headings use `uppercase leading-[1.1] tracking-[-.015em]` (poster caps). Add
`[text-shadow:3px_3px_0_#E0A526]` to the hero title for the off-register misprint.
