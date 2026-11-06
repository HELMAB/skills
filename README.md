# Agent Skills

Agent skills for Claude Code, Claude.ai and any agent that supports the [Agent Skills](https://agentskills.io) format.
Each skill is a self-contained folder in `skills/` that you can install on its own.

| Skill | What it does |
|---|---|
| [`retrokh-design`](#retrokh-design) | Builds websites and UIs that look like 1960s–70s Cambodian golden-era print |

## Install

```bash
npx skills add helmab/skills                         # all skills
npx skills add helmab/skills --skill retrokh-design  # one skill
npx skills add helmab/skills --list                  # list only
```

- **Claude Code (manual):** copy a skill folder to `~/.claude/skills/`, for example `cp -r skills/retrokh-design ~/.claude/skills/`.
- **Claude.ai:** zip a skill folder and upload it under **Settings → Capabilities → Skills**.

## Layout

```
skills/<name>/   SKILL.md + references/ scripts/ assets/   ← installed
evals/<name>/    test scenarios and how to run them        ← not installed
```

---

## retrokh-design

RetroKh makes a screen look like a Cambodian print from the 1960s and early '70s:
- **Look:** cream paper and brown ink, with red, turmeric and teal spot colours. One typeface (Google Sans) set big and bold.
- **Print details:** square corners, hard offset shadows, zigzag, halftone and sunburst bands, sepia photos and rubber stamps.
- **Language:** Khmer-first, with English and bilingual support.
- **Output:** plain HTML/CSS, Tailwind v3/v4 or Vue 3. It can also restyle existing Bootstrap or shadcn projects.

**Try:**
- "Build my personal profile website in Khmer retro style"
- "Make a company profile for my print shop, RetroKh style, Khmer and English"
- "Create an NGO site that looks like a 1970s Cambodian poster"
- "Restyle this Vue + Tailwind dashboard as old-school Khmer print"

It triggers on phrases like *Khmer retro*, *vintage Cambodian*, *old-school Khmer* and *RetroKh*, or you can call it with `/retrokh-design`.

**How it keeps token use low:**
- `SKILL.md` is about 1.6k tokens and routes each task to the one reference file it needs.
- The stylesheet and the page templates are installed with `cp`, so they never enter the context.
- It finishes by running `scripts/check_retrokh.py` (Python 3.8+), fixing what the script reports and re-running until it shows 0 errors.

| paper | sheet | ink | red | turmeric | teal |
|---|---|---|---|---|---|
| `#F1E4C6` | `#FBF5E6` | `#2A1D14` | `#9E2F18` | `#E0A526` | `#245A57` |

Every text pair meets WCAG AA. Eval scenarios are in [`evals/retrokh-design/`](evals/retrokh-design/). The style was distilled from
the *Dobpi* 1970s Khmer Retro design canvas. Google Sans is used under the SIL Open Font License.

---

## Adding a skill

1. Create `skills/<name>/SKILL.md`, where `name:` matches the folder name (lowercase and hyphens). Write the `description:` in
   the third person, and say what the skill does and when to use it, in 1024 characters or fewer.
2. Keep `SKILL.md` lean. The [best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
   cap it at 500 lines. Put the details in `references/`, one level deep, with a table of contents for any file over 100 lines.
   Put files the agent should copy (not read) in `assets/`.
3. Add at least three scenarios to `evals/<name>/evals.json`.
4. Add a row to the table above and a `## <name>` section.
5. Validate:
   ```bash
   uvx --from skills-ref agentskills validate skills/<name>
   npx skills add . --list
   ```

## License

MIT
