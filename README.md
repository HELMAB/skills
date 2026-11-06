# Agent Skills

Agent skills for Claude Code, Claude.ai and any agent that supports the [Agent Skills](https://agentskills.io) format.
Each skill is a self-contained folder in `skills/` that you can install on its own.

## Install

```bash
npx skills add helmab/skills                         # all skills
npx skills add helmab/skills --skill retrokh-design  # one skill
npx skills add helmab/skills --list                  # list only
```

- **Claude Code (manual):** copy a skill folder to `~/.claude/skills/`, for example `cp -r skills/retrokh-design ~/.claude/skills/`.
- **Claude.ai:** zip a skill folder and upload it under **Settings → Capabilities → Skills**.

## Skills

| Skill | What it does |
|---|---|
| [`retrokh-design`](#retrokh-design) | Builds websites and UIs that look like 1960s–70s Cambodian golden-era print |
| [`retrokh-social`](#retrokh-social) | Makes TikTok, YouTube and Facebook thumbnails, covers and posters in the same golden-era style |

### retrokh-design

Gives a website or app the look of 1960s–70s Cambodian golden-era print: cinema bills, Khmer pop record sleeves, school
textbooks. The pages are still modern, accessible and fast. You describe the site, and the skill picks the layout, colours
and Khmer typography. It builds in your project's own stack and checks its work before handing it over.

- **Style:** cream paper, brown ink, red, turmeric and teal spot colours, Google Sans, square corners, hard shadows, halftone and sunburst bands, rubber stamps.
- **Good for:** personal profiles and CVs, company and NGO sites, shops, events, blogs, landing pages and dashboards.
- **Works with:** HTML/CSS, Tailwind, Vue 3, Laravel Blade, Bootstrap and shadcn. Khmer-first, with English and bilingual support.

**Try:** *"Build my personal profile website in Khmer retro style"* or *"Make a company profile for my print shop, RetroKh style, Khmer and English."*
Call it directly with `/retrokh-design`.

| paper | sheet | ink | red | turmeric | teal |
|---|---|---|---|---|---|
| `#F1E4C6` | `#FBF5E6` | `#2A1D14` | `#9E2F18` | `#E0A526` | `#245A57` |

All text colours meet WCAG AA. Evals are in [`evals/retrokh-design/`](evals/retrokh-design/).

### retrokh-social

Makes social images that look printed in 1960s Phnom Penh: record sleeves, song books and cinema bills. You describe the post, and
the skill writes one artwork, then renders and checks a PNG at each platform's exact size.

- **Styles:** sunburst, giant type, night press, torn collage, song book and halftone noir, with drawn motifs or your own photo.
- **Font:** Google Sans only, for Khmer and Latin. The renderer rejects anything else.
- **Formats:** YouTube thumbnail, banner, Shorts cover and community post; TikTok cover and poster; Facebook post, story, link image, event banner and page cover.
- **Checks:** text inside each safe area, clear of platform UI, large enough to read, fonts loaded, file size within limits.
- **Needs:** Chrome or Chromium and network access to Google Fonts. Pillow is optional, for small previews and JPEG output.

**Try:** *"Make a YouTube thumbnail for my Khmer classic songs video"* or *"Vintage Khmer promo images for our jazz night, for YouTube, TikTok and Facebook."*
Call it directly with `/retrokh-social`.

Evals are in [`evals/retrokh-social/`](evals/retrokh-social/).

---

## License

[MIT](LICENSE) © 2026 Hel Mab. Each skill also declares `license: MIT` in its `SKILL.md`, so the licence still applies when a
single skill is installed on its own. No fonts are bundled; Google Sans loads from Google Fonts under the
[SIL Open Font License](https://openfontlicense.org).
