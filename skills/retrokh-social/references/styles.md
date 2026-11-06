# Styles in depth

Each style sets its colours in `assets/social.css`. Override a variable on `html` in the artwork's `<style>` block, such as
`--title`, `--accent`, `--bg`, `--wear`.

## What makes the look work

- **Two or three flat inks per image.** A cheap press had few plates. If a fourth colour appears, take one away.
- **One hero.** One face, object or word. The vintage posters that feel busy still have one thing that reads first.
- **Big lettering.** Google Sans Bold at huge scale is the illustration. Make it far bigger than feels polite.
- **Print accidents.** A slight colour misprint (`--misprint`), grain and halftone dots read as age. Keep them small enough
  that the title stays crisp at thumbnail size.
- **Hard edges.** Hard offset shadows, torn paper and square plates. Never blur.

## Notes by style

- `sunburst`: rays are unreadable behind text, so copy always sits on a plate. The rays centre on the art automatically.
- `giant-type`: set `data-fit="fill"` on `.rs-title` so each line fills the width. Strongest with 1–2 short lines.
- `night-press`: the sun follows the art. Use `sugar-palms` or a cut-out in front of it. Keep the palms dark so they read as silhouettes.
- `torn-collage`: the tear sits under the headline automatically. Art may overlap the tear; text shouldn't sit on it.
- `songbook`: everything prints in one ink. Keep photos monochrome and avoid a second colour.
- `halftone-noir`: made for a strong portrait. With motifs alone it can feel empty, so prefer another style if there's no photo.

## Making a set

For a campaign, keep one style and the same title across formats, and let the renderer handle the crops. For an ongoing series,
fix the style and layout, and change only the title and the art, so viewers recognise the channel at a glance.
