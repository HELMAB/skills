# Websites

Plans and recipes for public sites. Classes are in `classes.md`. For a whole page, copy a template from
`assets/templates/` and edit it rather than writing from scratch.

## Plan
1. Pick the **recipe** below. Pick an **accent**: red (commerce, culture, food), teal (professional, NGO, school, health) or
   plum (arts, events). Then pick the **language**: `km`, `en`, or Khmer headings with English labels.
2. Pick **2–4 signature moves** and repeat them on every page: rays hero with a printed plate · zigzag seams · printed
   sepia photos (one tilted) · numbered heads `០១ · …` · ledger timeline · stamps (`ថ្មី`, `ពេញនិយម`, `អស់ហើយ`) · seal logo
   (an accent disc with a dashed ring and a Khmer initial) · official header (civic and school sites only).
3. List the facts you need from the owner. Use `[ … ]` for anything you don't have.

## Rhythm
- Alternate the backgrounds: ground → `.rk-section-paper` → ground.
- Use rays only in the hero, at most **one** halftone band (quotes or gallery) and **one** ink band (the CTA, between zigzags).
- Never put two patterned sections next to each other.
- Inner pages use `.rk-pagehead` + a breadcrumb + a zigzag instead of a hero. Keep the nav, footer and accent the same on every page.

## Recipes (section order; ‡ = optional)
- **Personal profile / CV / portfolio** (teal or plum): nav → hero (`.rk-portrait` + plate: name, role, city, Contact,
  `<a download>` CV) → about (`.rk-prose`) beside skills (`.rk-tag`, language `.rk-progress`) → work (`.rk-post` grid) →
  experience and education `.rk-timeline` → ‡quotes → CTA (email) → slim footer. Keep it to one page with anchors.
- **Company profile** (red): nav → hero (plate + tilted premises photo) → `.rk-stats` → services (`.rk-feature` ×3 or ×6) →
  about split + history timeline → ‡team (`.rk-photo` grid) → quotes on halftone → `.rk-logos` → news `.rk-post` + events
  `.rk-ticket` → `.rk-faq` → CTA → contact (`.rk-contact` + form + ‡map) → footer with columns.
- **Organisation / NGO / school** (teal): mission hero → programmes (`.rk-feature`) → impact stats (real and sourced, with
  the year) → stories → milestones timeline → partners → events → get-involved CTA (Donate/Join as `.rk-btn-paper`) →
  footer with the registration number. Civic and school sites may top the plate with the official header (style.md).
- **Restaurant / café / shop** (red): hero (dish or storefront, Order/Call) → menu as `.rk-table` with tabular prices in
  Khmer digits plus riel or USD → tilted gallery → opening hours (stamp `ថ្ងៃនេះ` on today) → map → footer.
- **Event / wedding** (plum or red): hero with a big tabular date and a `.rk-banner` → programme timeline (times) →
  venue split + map → gallery → RSVP form on a `.rk-sheet` → footer. Bilingual is common here.
- **Blog / news**: featured `.rk-post` in `.rk-split` → latest grid → `.rk-tag` categories → newsletter CTA. Article page:
  `.rk-pagehead` (title, date, author) → `article.rk-narrow.rk-prose` → related posts.
- **Product landing**: plate + a screenshot in `.rk-photo` → features → steps as a timeline (`១ ២ ៣`) → pricing (`.rk-card`,
  with a stamp on the recommended plan, never a glow) → FAQ → CTA.

## Images
- Every image sits in `.rk-photo`, `.rk-post` or `.rk-portrait`, which adds the sepia, halftone, paper border and hard shadow.
- With no real image, use a `.rk-photo-label` placeholder. Never use stock-photo URLs or AI faces presented as real people.
- Write `alt` in the page's language (`alt=""` for decoration). Add `loading="lazy"` below the fold, and `width`/`height` or `aspect-ratio`.
- Partner logos go through `.rk-logos img`. The owner's own logo keeps its true colours.

## Page must-haves
`<html lang>` · `.rk-skip` link · `header`, `nav`, `main` and `footer` · one `h1` · `<title>` as `Page · Brand` · meta description and
og:title/og:image · preconnect plus the Google Sans link · forms with a visible `<label>`, `autocomplete`, `.rk-error-text` and a
real `action` · underlined body links · at 390px: the nav collapses, grids go to 1 column, no horizontal scroll.
