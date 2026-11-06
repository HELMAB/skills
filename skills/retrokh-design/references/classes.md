# Class reference (`assets/retrokh.css`)

Every class in `retrokh.css`, one line each. You don't need to read the CSS itself.

## Contents
- [Root and theme](#root-and-theme) · [Type](#type) · [Patterns](#patterns) · [Surfaces](#surfaces) · [Buttons](#buttons)
- [Forms](#forms) · [Navigation and overlays](#navigation-and-overlays) · [Marks and feedback](#marks-and-feedback) · [Data](#data)
- [Website sections](#website-sections) · [Skeletons](#skeletons) · [Icons](#icons) · [States](#states)

## Root and theme
- `body.rk` (or `.rk-root` on an app root): font, colours, line-height 1.7, `overflow-wrap:anywhere`. A custom ink bar can add `.rk-bar-ink` for a turmeric focus ring. Put `lang="km"` or `lang="en"` on `<html>`.
- `html[data-theme="dark"|"light"]` forces a theme; with neither, it follows `prefers-color-scheme`. `[data-accent="teal"|"plum"]` swaps the accent.
- `html.js` lets the site nav collapse on phones (`<script>document.documentElement.classList.add('js')</script>` in `<head>`).
- Light blocks (`.rk-sheet`, cards, inputs, menus, tables, the hero plate…) stay light in dark mode and reset their text to ink.
  For a custom light block, add `.rk-paper-context`. Ink contexts (`.rk-nav`, `.rk-pagehead`, `.rk-section-ink`, `.rk-cta`,
  `.rk-footer`) flip their text to paper by themselves.

## Type
`.rk-display` (700, 1.6; set the size) · `.rk-title` (22px) · `.rk-numeral` (700 tabular) · `.rk-eyebrow` (17px numeral, accent) ·
`.rk-lead` (18px muted) · `.rk-small` (14px) · `.rk-label` (14px 700 muted) · `.rk-muted` · `.rk-latin` (12px 500 caps .18em, **Latin only**) ·
`.rk-misprint` (turmeric off-register shadow, hero titles only) · `.rk-hl` (accent word inside a hero title) · `mark`/`.rk-mark` (turmeric) ·
`.rk-sr` (visually hidden) · `.rk-skip` (skip link).

## Patterns
All are decorative: add `aria-hidden="true"`.
`.rk-zigzag` (14px strip, 10px on phones: under the nav and around the CTA) · `.rk-rays` (hero or splash background) ·
`.rk-halftone` (one band, or behind sheets) · `.rk-ruled` (44px lines behind lists) · `.rk-ruled-tight` (22px) ·
`.rk-diamonds` (12px divider; set `width:120px`) · `.rk-hatch` (loading fill).

## Surfaces
`.rk-sheet` (sheet + 2px border + 8px shadow) · `.rk-card` > `.rk-card-head` (ink strip, `១ · title`) + `.rk-card-body` ·
`.rk-frame` (4px double) · `.rk-panel-dashed` (dashed teal panel) · `hr.rk-rule-double` · `hr.rk-divider-dashed`.

## Buttons
`.rk-btn` + one of: `-primary` (48px ink, red shadow; one per view) · `-system` (teal) · `-accent` · `-raised` (sheet) · `-ghost` ·
`-paper` (on ink bands). Add `.rk-btn-icon` (44px square, needs `aria-label`) and `.rk-btn-lg` (48px). Use `.rk-icon` on the SVG.
Group with `.rk-actions`. Pager or zoom: `.rk-segmented` > `a|button|span`, with the forward item `.is-primary`.

## Forms
`.rk-field` > `label.rk-label[for]` + `.rk-input` (a wrapper holding an icon SVG and the `input`/`select`) · invalid: `aria-invalid="true"` or
`.is-invalid` on `.rk-input`, plus `.rk-error-text` linked by `aria-describedby` · `textarea.rk-textarea` (ruled) ·
`label.rk-check` > `input[type=checkbox|radio]` + text · `.rk-tabs[role=tablist]` > `button[role=tab][aria-selected]`.

## Navigation and overlays
App bar: `.rk-header` (ink) + `.rk-zigzag`. Ledger list: `.rk-ruled` > `.rk-ledger-row`, with nested groups in `ol.rk-ledger`; each row holds `.rk-ledger-key` (84px numerals) +
`.rk-ledger-text`; the current item is `a.rk-current[aria-current=page]` (the only accent block on screen). Menu:
`ul.rk-menu[role=menu]` > `li` > `button[role=menuitem]`. Drawer: `.rk-scrim` + `.rk-drawer[role=dialog][aria-modal]` (trap focus, Esc
closes). Dialog: `dialog.rk-dialog` (use `showModal()`). Breadcrumb: `ol.rk-breadcrumb`.

## Marks and feedback
`.rk-stamp.rk-stamp-saved` (teal) / `.rk-stamp-fail` (red, bigger); stamps are `aria-hidden`, so repeat the meaning in an `aria-label` ·
`.rk-chip-ink` (`ទំព័រ <b>១ / ៤</b>`) · `.rk-tag` · `.rk-banner` (ink ribbon at −2°, once per page) · `.rk-progress` > `span[style=width:%]`
(add `.is-striped` or `.is-system`; `role=progressbar`) · `.rk-toast` (`role=status`) · `.rk-alert-system` (offline) / `-ok` / `-warn` ·
`.rk-empty` > `.rk-empty-title` + hint.

## Data
`.rk-table` (ink header, dashed rows; `td.num` for numerals) inside `.rk-table-wrap` (scrolls on phones) · `.rk-stat` > label + `.rk-stat-value`.

## Website sections
`.rk-container` (1200px) / `.rk-narrow` (760px) · nav `.rk-nav` · inner-page header `.rk-pagehead` (`h1` + `.rk-breadcrumb`) ·
`.rk-hero` + `.rk-rays` > `.rk-hero-grid` > `.rk-hero-plate` + media · `.rk-section` (+ `-paper` | `-sheet` | `-ink`) ·
`.rk-section-head` (`.is-center`) > `.rk-eyebrow` + `h2.rk-section-title` · `.rk-grid` (`--rk-min:260px`) · `.rk-split` (2 columns) ·
`.rk-feature` > `.rk-feature-num` + `h3` + `p` · `.rk-stats` > `div` > `b` + `span` · `ol.rk-timeline` > `li` > `.rk-timeline-year` +
`.rk-timeline-body` · `figure.rk-quote` > `blockquote` + `figcaption` · `ul.rk-logos` > `li` · `.rk-cta` (ink; zigzag strips before and after) ·
`.rk-faq` > `details` > `summary` + `div` · `article.rk-post` > `.rk-photo-frame` + `.rk-post-body` (`time`, `h3 a`, `p`) ·
`.rk-ticket` > `.rk-ticket-stub` (`b` day, `span` month) + `.rk-ticket-body` · `ul.rk-contact` > `li` > `.rk-contact-icon` + `span` ·
`.rk-prose` (long text) · `footer.rk-footer` > `.rk-footer-grid` + `.rk-footer-base`.
Photos: `figure.rk-photo` (`.is-tilted` once per page) > `.rk-photo-frame` (`--rk-ratio:4/3`; an `img`, or `span.rk-photo-label` with
`[ … ]` when there is no image) + `figcaption`. Round portrait: `.rk-portrait` (`--rk-size:160px`).

## Skeletons
```html
<header class="rk-nav"><div class="rk-container rk-nav-inner">
  <a class="rk-nav-brand" href="/"><span class="rk-display">[ ឈ្មោះ ]</span></a>
  <button class="rk-btn rk-btn-ghost rk-btn-icon rk-nav-toggle" aria-label="ម៉ឺនុយ" aria-expanded="false" aria-controls="links"><svg class="rk-icon" …menu path…></svg></button>
  <nav aria-label="ម៉ឺនុយមេ" style="display:contents"><ul class="rk-nav-links" id="links">
    <li><a href="/" aria-current="page">ទំព័រដើម</a></li><li><a href="#about">អំពីយើង</a></li></ul></nav>
</div></header>
<div class="rk-zigzag" aria-hidden="true"></div>
<script>const n=document.querySelector('.rk-nav'),t=n.querySelector('.rk-nav-toggle');
t.onclick=()=>t.setAttribute('aria-expanded',String(n.toggleAttribute('data-open')));</script>

<section class="rk-hero rk-rays"><div class="rk-container rk-hero-grid">
  <div class="rk-hero-plate"><span class="rk-eyebrow">…</span><h1 class="rk-hero-title rk-misprint">… <span class="rk-hl">…</span></h1>
    <p class="rk-lead">…</p><div class="rk-actions"><a class="rk-btn rk-btn-primary" href="#contact">…</a></div></div>
  <figure class="rk-photo is-tilted"><div class="rk-photo-frame"><span class="rk-photo-label">[ រូបថត ]</span></div><figcaption>…</figcaption></figure>
</div></section>
```

## Icons
Inline SVG, `viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"` (2.6 for chevrons), `aria-hidden="true"`.
menu `M4 6h16M4 12h16M4 18h16` · close `M6 6l12 12M18 6L6 18` · next `M9 6l6 6-6 6` · prev `M15 6l-6 6 6 6` · up `M6 15l6-6 6 6` ·
down `M6 9l6 6 6-6` · check `M5 12l5 5 9-10` · plus `M5 12h14M12 5v14` · download `M12 4v11M7 10l5 5 5-5M4 20h16` ·
search `<circle cx=11 cy=11 r=6.5/>` + `M16 16l5 5` · mail `M3 5h18v14H3zM3 5l9 8 9-8` ·
pin `M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z` + `<circle cx=12 cy=9.5 r=2.5/>` ·
moon `M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z`.

## States
- **Loading:** a halftone band holding a small `.rk-sheet` with "កំពុងផ្ទុក ៤២%" and `.rk-progress.is-striped`, all inside `role=status`.
- **Error:** `role=alert`, then `.rk-stamp-fail` "បរាជ័យ", a bold message, a muted remedy and a primary "ព្យាយាមម្ដងទៀត" button.
- **Empty:** `.rk-empty`, a title, and a hint with an example in «».
- **Offline:** `.rk-alert-system`; back online: `.rk-alert-ok`.
- **Toast:** `.rk-toast` for ≥5s.
- **App screens:** an ink `.rk-header` + zigzag; a paper sidebar (`border-right:4px double`) holding the ledger; main content on
  `.rk-halftone` with stacked `.rk-sheet`s; a sticky pager. On phones the sidebar becomes `.rk-drawer`.
