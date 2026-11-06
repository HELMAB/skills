# Websites: profiles, companies, organisations and more

RetroKh works for any public website: a personal profile, CV or portfolio, a company profile, an NGO, association,
school or ministry site, a restaurant, café or shop, an event or wedding page, a blog or news site, or a product
landing page. The site should read like a 1970s Cambodian printed piece: a cinema bill, a school prospectus, a ministry
bulletin or a record sleeve. It should not read like a modern template painted brown.

All classes below are in `assets/retrokh.css` (section 13). Working pages: `examples/company-profile.html`
(Khmer, red accent) and `examples/personal-profile.html` (English-primary, teal accent).

## Contents

- [1. Plan before building](#1-plan-before-building)
- [2. Page skeleton](#2-page-skeleton)
- [3. Section catalogue](#3-section-catalogue)
- [4. Recipes by site type](#4-recipes-by-site-type)
- [5. Signature moves for websites](#5-signature-moves-for-websites)
- [6. Images](#6-images)
- [7. Multi-page sites](#7-multi-page-sites)
- [8. Quality bar for websites](#8-quality-bar-for-websites)

## 1. Plan before building

1. **Identify the site type** and pick its recipe from section 4.
2. **Choose the accent**: red (default; warm, commercial, cultural), teal (calm; professional, health, education,
   NGO) or plum (creative, arts, events). Set it with `data-accent="teal|plum"` on `<body>`.
3. **Choose the language mode**: Khmer-first (`lang="km"`), bilingual (Khmer headings with English eyebrows), or
   English-primary (`lang="en"`, where headings switch to tighter Latin caps automatically). See `typography.md`.
4. **Pick 2–4 signature moves** for the whole site (section 5), and repeat the same ones on every page.
5. **Collect real content.** Never invent stats, testimonials, client names, prices, dates or contact details.
   Write `[ … ]` placeholders in the page's language and list what the owner must supply.

## 2. Page skeleton

```html
<!doctype html>
<html lang="km">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>[ ឈ្មោះ ] · [ ពាក្យស្លោក ]</title>
  <meta name="description" content="[ … ]">
  <meta property="og:title" content="[ … ]"><meta property="og:image" content="[ share image 1200×630 ]">
  <script>document.documentElement.classList.add('js')</script>   <!-- enables the collapsible phone menu -->
  <!-- Google Fonts link (see retrokh.css header) + retrokh.css -->
</head>
<body class="rk">
  <a class="rk-skip" href="#main">រំលងទៅមាតិកា</a>
  <header class="rk-nav">…</header>
  <div class="rk-zigzag" aria-hidden="true"></div>
  <main id="main">
    <section class="rk-hero rk-rays">…</section>
    <section class="rk-section">…</section>             <!-- alternate the ground with .rk-section-paper -->
    <section class="rk-section rk-section-paper">…</section>
    <div class="rk-zigzag" aria-hidden="true"></div>
    <section class="rk-cta">…</section>                 <!-- ink band framed by zigzags -->
    <div class="rk-zigzag" aria-hidden="true"></div>
  </main>
  <footer class="rk-footer">…</footer>
</body>
</html>
```

**Section rhythm.** Alternate the backgrounds ground → paper → ground. Use **one** halftone band (testimonials or a gallery)
and **one** ink band (the CTA) per page, and put the rays only in the hero. Never place two patterned sections next to each other.

## 3. Section catalogue

| Section | Markup | Notes |
|---|---|---|
| **Site nav** | `header.rk-nav > .rk-container.rk-nav-inner` with a brand link, a `.rk-nav-toggle` button and `ul.rk-nav-links` | Sticky ink bar; the current page is a solid `--rk-mark` block with `aria-current="page"`. On phones the links collapse behind the toggle (JS adds `data-open`; without JS they wrap) |
| **Hero** | `section.rk-hero.rk-rays > .rk-hero-grid` containing `.rk-hero-plate` and a `.rk-photo` | The copy always sits on the sheet plate, never on the rays. Plate content: `.rk-eyebrow`, `h1.rk-hero-title` (wrap one key word in `.rk-hl`), `.rk-lead`, `.rk-actions` |
| **Page header** (inner pages) | `section.rk-pagehead > .rk-container` with `h1` and `ol.rk-breadcrumb`, then a zigzag | Use it instead of a hero on About, Services, Contact and similar pages |
| **Section head** | `.rk-section-head` containing `.rk-eyebrow` (`០១ · សេវាកម្ម`) and `h2.rk-section-title` | Double rule under the title. `.is-center` drops the rule; add a `.rk-diamonds` divider below |
| **Services / features** | `.rk-grid > article.rk-feature` containing `.rk-feature-num`, `h3` and `p` | Ink number blocks in Khmer numerals. 3 or 6 items; set `--rk-min` to tune the columns |
| **About split** | `.rk-container.rk-split` with a `.rk-photo` and the text | Photo on the left, text on the right; alternate the sides further down the page |
| **Stats band** | `.rk-stats > div` containing `b` (number) and `span` (label) | bold tabular numbers in red with dashed dividers. **Real numbers only** |
| **Timeline / history / CV** | `ol.rk-timeline > li` containing `.rk-timeline-year` and `.rk-timeline-body` | A ledger rail: bold tabular years, an accent rule and diamond bullets |
| **Team** | `.rk-grid` of `.rk-photo` cards: portrait frame, then `figcaption` with the name in **bold** and the role | Or use `.rk-portrait` circles (seal-style) for small teams |
| **Testimonials** | `.rk-section.rk-halftone` with `.rk-grid` of `figure.rk-quote` | The section title sits on a sheet chip (never on the halftone). **Real, permitted quotes only** |
| **Partners / clients** | `ul.rk-logos > li` (a name or `img`) | Logos are rendered sepia/greyscale to fit the print palette |
| **News / blog list** | `.rk-grid` of `article.rk-post` containing `.rk-photo-frame` and `.rk-post-body` (`time`, `h3 a`, `p`) | Dates in bold red, in Khmer numerals and month names |
| **Events** | `article.rk-ticket` containing `.rk-ticket-stub` (`b` day, `span` month) and `.rk-ticket-body` | A perforated ticket stub |
| **Gallery / portfolio** | `.rk-grid` of `figure.rk-photo` (add `.is-tilted` to one or two) | Captions under every photo |
| **Pricing / plans** | `.rk-grid` of `.rk-card` with an ink head, a bold tabular price and a list | Mark the recommended plan with a red stamp (`ពេញនិយម`), not a glow or a scale-up |
| **FAQ** | `.rk-faq > details > summary + div` | Native disclosure; bold `+` and `−` markers |
| **CTA band** | zigzag, then `section.rk-cta` with `h2`, `p` and `.rk-actions` holding `.rk-btn-paper` + `.rk-btn-ghost`, then zigzag | One per page, near the end |
| **Contact** | `.rk-split` with `ul.rk-contact` (ink icon squares) and a `form.rk-sheet` | Every field has a visible `<label>`; `autocomplete` attributes; a primary submit button |
| **Map** | `.rk-photo` with `.rk-photo-frame` containing an embedded map or static image | Sepia filter keeps it on palette. Use an `<a>` link to the map app as a fallback |
| **Long-form article** | `article.rk-narrow.rk-prose` | bold h2s, double-ruled pull quotes, accent list markers |
| **Footer** | `footer.rk-footer` with `.rk-footer-grid` (brand + 2–3 link columns) and `.rk-footer-base` | Ink; `4px double` top edge; a Latin caps brand line |

## 4. Recipes by site type

Each recipe lists the sections in order. `‡` marks optional sections.

### Personal profile, CV or portfolio
Nav (name as brand) → hero: `.rk-portrait` + plate (name in the hero title, role, city, *Contact* + *Download CV*) →
About (`.rk-prose`) beside Skills (`.rk-tag`s, language `.rk-progress` bars) → Selected work (`.rk-post` grid) →
Experience & education (`.rk-timeline`) → ‡Testimonials → CTA band with email → slim footer.
Accent: teal or plum. Keep it to one page with anchor links. Add `<a download>` for the CV PDF.

### Company profile
Nav → hero (tagline plate + tilted photo of the premises or product) → Stats band → Services (`.rk-feature` ×3/6) →
About split + history timeline → ‡Team → Testimonials (halftone) → Partners strip → News & events → FAQ →
CTA band → Contact (details + form + ‡map) → footer with columns.
Multi-page version: Home (hero, services teaser, stats, CTA) · About (pagehead, story, timeline, team) · Services ·
News · Contact.

### Organisation, NGO, association or school
Nav (with a *Donate* or *Join* primary button styled as `.rk-btn-paper` inside the ink bar) → hero (mission statement) →
Programmes (`.rk-feature`) → Impact stats (real, sourced; add the source and year in a caption) → Stories (`.rk-post`)
→ Timeline of milestones → Partners → Events (`.rk-ticket`) → Get involved (CTA) → footer with registration
number and address. For a government or school body, the **official-document header** (`patterns.md`) may top the
hero plate. Accent: teal.

### Restaurant, café or shop
Hero (rays, dish or storefront photo, *Order*/*Call* buttons) → Menu as `.rk-table` or ledger-style lists with bold tabular
prices in Khmer numerals and riel/USD → Gallery (tilted photos) → Opening hours (`.rk-table`; mark today's row with a
red `ថ្ងៃនេះ` stamp) → Location + map → footer. Accent: red.

### Event or wedding
Hero with the date in bold tabular figures, a `.rk-banner` ribbon and a countdown-free date → Programme (`.rk-timeline` with times) →
Venue (`.rk-split` + map) → Gallery → RSVP form (`.rk-sheet`) → footer. Bilingual Khmer/English is common here.
Accent: plum or red.

### Blog, magazine or news
Nav → featured post (a large `.rk-post` in `.rk-split`) → latest grid (`.rk-post` ×6) → categories as `.rk-tag`
links → newsletter CTA → footer. Article page: `.rk-pagehead` (title, date, author) → `article.rk-narrow.rk-prose`
→ related posts.

### Product or app landing page
Hero (plate + device screenshot in a `.rk-photo` frame) → Features (`.rk-feature`) → How it works (`.rk-timeline`
with steps `១ ២ ៣` instead of years) → Pricing → FAQ → CTA band → footer.

## 5. Signature moves for websites

Pick 2–4 per site:
- **Rays hero with a printed plate**: copy on a sheet with an `8px` shadow over a sunburst.
- **Zigzag seams**: under the nav and around the CTA band.
- **Printed photos**: sepia, a fine halftone, a paper border, the hard shadow and one tilted print per page.
- **Numbered section heads**: `០១ · សេវាកម្ម` eyebrows in bold tabular figures.
- **Ledger timeline**: bold tabular years on an accent rule.
- **Stamps** for status or emphasis: `ពេញនិយម` (popular), `ថ្មី` (new), `អស់ហើយ` (sold out), `បានបញ្ចប់` (finished).
- **Official header** (civic and school sites only).
- **Seal logo**: a round accent disc with a dashed ring and a Khmer initial in bold.

## 6. Images

- Every photo goes in `.rk-photo` (or `.rk-post` / `.rk-portrait`) so it gets the print treatment
  (`sepia(.35) saturate(.85) contrast(1.05)` + a 4px halftone overlay).
- Without real images, use `.rk-photo-frame` with a `.rk-photo-label` such as `[ រូបថតហាង ]`. Never use stock-photo URLs
  or AI-generated faces passed off as real people.
- Use real `alt` text in the page's language; decorative images get `alt=""`. Add `loading="lazy"` below the fold and
  `width`/`height` (or `aspect-ratio`) to prevent layout shift.
- Logos from partners go through `.rk-logos img` (greyscale + sepia). Keep the owner's own logo in its true colours.

## 7. Multi-page sites

- Use the same nav, footer and accent on every page. Mark the current page with `aria-current="page"` in the nav.
- The home page gets the rays hero; inner pages get `.rk-pagehead` + a breadcrumb + a zigzag.
- Use one CTA band per page at most. Contact and booking pages can drop it.
- Use Khmer page `<title>`s with the brand after a middle dot, e.g. `សេវាកម្ម · ហាងបោះពុម្ព សូរិយា`.

## 8. Quality bar for websites

- [ ] Skip link, landmark elements (`header`, `nav`, `main`, `footer`) and one `h1` per page.
- [ ] Phone (390px): the nav collapses, the hero stacks (photo below the plate), grids go to 1 column and no horizontal scroll.
- [ ] Copy never sits directly on rays or halftone; it always sits on a plate, sheet or chip.
- [ ] One halftone band, one ink band and the rays only in the hero.
- [ ] No fabricated facts: placeholders are bracketed and listed for the owner.
- [ ] Forms have visible labels, `autocomplete`, inline errors (`.rk-error-text`) and a real `action`.
- [ ] Links in body text are underlined; buttons look like buttons (border + hard shadow).
- [ ] Meta description and OG tags are set; fonts are preconnected; images are lazy below the fold.
