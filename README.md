# Agent Skills

A collection of agent skills that work in Claude Code, Claude.ai and any agent that supports the
[Agent Skills](https://agentskills.io) format. Each skill lives in its own folder under `skills/` and can be
installed on its own.

## Skills

| Skill | What it does |
|---|---|
| [`retrokh-design`](#retrokh-design) | Designs and builds websites and apps in a Khmer old-school, 1970s print style |

More skills will be added here over time.

## Install

Install every skill in this repo:
```bash
npx skills add <your-github-user>/skills
```

Install one skill only:
```bash
npx skills add <your-github-user>/skills --skill retrokh-design
```

To see what's available without installing anything:
```bash
npx skills add <your-github-user>/skills --list
```

Manual install for Claude Code:
```bash
git clone https://github.com/<your-github-user>/skills
cp -r skills/skills/<skill-name> ~/.claude/skills/
```

For Claude.ai, zip one skill's folder (for example `skills/retrokh-design`) and upload it under
**Settings → Capabilities → Skills**.

## Repository layout

```
skills/
└── <skill-name>/          # one folder per skill (this is what gets installed)
    ├── SKILL.md           # required: frontmatter (name, description) + instructions
    ├── references/        # optional: docs the agent reads on demand
    ├── assets/            # optional: files the agent copies into projects
    └── examples/          # optional: working reference output
docs/
└── <skill-name>/          # screenshots for this README (not installed)
```

---

## retrokh-design

Designs and builds **websites and apps** in **RetroKh**, a Khmer old-school, 1970s print style. It looks like cream
paper and dark-brown ink with red, turmeric and teal spot colours, a single typeface (Google Sans, Khmer + Latin) set
big and bold, square corners, hard offset shadows, zigzag, halftone and sunburst patterns, and rubber-stamp labels.

Use it for personal profiles and CVs, company profiles, organisation, NGO and school sites, restaurants and shops,
events, blogs, landing pages, dashboards and app screens. It produces HTML/CSS, Tailwind (v3 and v4) or Vue 3, and
writes Khmer-first copy with English or bilingual support.

![RetroKh company profile](docs/retrokh-design/company-profile.png)

<details><summary>Personal profile (English-primary)</summary>

![RetroKh personal profile](docs/retrokh-design/personal-profile.png)
</details>

### Use

Ask for anything in the style, for example:
- "Build my personal profile website in Khmer retro style"
- "Make a company profile site for my print shop, RetroKh style, Khmer and English"
- "Create an NGO website that looks like a 1970s Cambodian poster"
- "Build a Khmer retro login page in Vue + Tailwind"
- "Make this dashboard look like an old-school Khmer print, keep it bilingual"
- "Design a restaurant menu page / wedding invitation site, RetroKh style"

The skill triggers on phrases such as *Khmer retro*, *old school Khmer*, *Cambodian vintage*, *60s/70s Khmer*,
*golden era* and *RetroKh*, or you can call it directly with `/retrokh-design`.

### What's inside

```
skills/retrokh-design/
├── SKILL.md                    # laws, workflow, token table, signature moves, checklist
├── references/
│   ├── tokens.md               # palette + roles + contrast, dark mode, shape, space, token JSON
│   ├── typography.md           # Google Sans roles (weight/size/case), Khmer script rules, numerals, voice
│   ├── patterns.md             # zigzag, halftone, rays, ruled, diamonds, seal, stamps, official header
│   ├── components.md           # buttons, inputs, tabs, header, ledger nav, drawer, cards, tables, states
│   ├── websites.md             # site planning, section catalogue, recipes per site type, images
│   ├── layouts.md              # app shell, phone, splash, dashboard, form, style tile
│   ├── tailwind.md             # v3 preset + v4 @theme recipes
│   └── vue.md                  # Vue 3 components incl. RkSiteNav / RkSection, khmer digit helper
├── assets/
│   ├── retrokh.css             # drop-in tokens, patterns, app + website components (light + dark)
│   ├── tailwind.preset.js      # Tailwind v3
│   └── tailwind.v4.css         # Tailwind v4
└── examples/
    ├── company-profile.html    # Khmer company site (nav, hero, services, timeline, news, FAQ, contact)
    └── personal-profile.html   # English-primary profile / CV
```

### Palette

| paper | sheet | ink | red | turmeric | teal |
|---|---|---|---|---|---|
| `#F1E4C6` | `#FBF5E6` | `#2A1D14` | `#9E2F18` | `#E0A526` | `#245A57` |

Every text pair meets WCAG AA (ink on paper 12.9:1, red on paper 5.8:1, teal on paper 6.2:1).

### Credits

Distilled from the *Dobpi* 1970s Khmer Retro design canvas. The only typeface is Google Sans (Khmer + Latin),
from Google Fonts under the SIL Open Font License.

---

## Adding a new skill

1. Create `skills/<skill-name>/SKILL.md`. The folder name must match the `name:` in its frontmatter (lowercase,
   hyphens). Write a `description:` that says what the skill does **and** when it should trigger (max 1024 characters).
2. Put long docs in `references/`, reusable files in `assets/` and working output in `examples/`. Keep `SKILL.md` short
   and point to those files from it.
3. Put README screenshots in `docs/<skill-name>/`, not inside the skill folder, so they aren't installed.
4. Add a row to the [Skills](#skills) table and a `## <skill-name>` section below it.
5. Check the repo still lists every skill:
   ```bash
   npx skills add . --list
   ```

## License

MIT
