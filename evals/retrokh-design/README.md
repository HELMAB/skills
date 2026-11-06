# retrokh-design evaluations

Three scenarios that cover the skill's main paths: a Khmer website, an English website and a framework component.
They use the eval format from Anthropic's
[skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
(`skills`, `query`, `files`, `expected_behavior`). There is no built-in eval runner, so each scenario is run and graded
by hand. This folder sits outside `skills/`, so it is not installed with the skill.

| id | Covers |
|---|---|
| `khmer-company-profile` | Khmer-first site, website recipe, no fabricated content, forms, checker loop |
| `english-personal-profile` | English-primary site, accent swap, poster-caps headings, phone nav |
| `vue-tailwind-component` | Vue 3 + Tailwind v4 output, tokens as utilities, Khmer digits, stamps, a11y |

## Run one scenario

From the repo root, for each model you plan to support (Haiku, Sonnet and Opus):

```bash
EVAL=khmer-company-profile          # id from evals.json
MODEL=claude-sonnet-5-5             # also run claude-haiku-5-5 and claude-opus-5-5
RUN=$(mktemp -d)
mkdir -p "$RUN/.claude/skills" && cp -r skills/retrokh-design "$RUN/.claude/skills/"
QUERY=$(python3 -c "import json,sys;print(next(e['query'] for e in json.load(open('evals/retrokh-design/evals.json')) if e['id']==sys.argv[1]))" "$EVAL")
(cd "$RUN" && claude -p "$QUERY" --model "$MODEL" --permission-mode acceptEdits \
   --allowedTools "Read" "Write" "Edit" "Glob" "Grep" "Bash(python3:*)")
python3 skills/retrokh-design/scripts/check_retrokh.py "$RUN"
echo "Output in $RUN"
```

For the Vue scenario, start `$RUN` from a scaffolded Vue 3 + Tailwind v4 project instead of an empty folder.

## Grade

1. Open the output in a browser at 1440px and 390px wide.
2. Mark each `expected_behavior` line **pass** or **fail**. The checker covers the mechanical lines (fonts, weights,
   corners, shadows, `lang`); judge the rest by reading the output and the transcript.
3. **Baseline:** run the same query once *without* the skill (skip the `cp` line). The skill earns its place when
   it passes clearly more lines than the baseline.
4. Record results per model. What to look for: Haiku shows whether the guidance is *enough*, Sonnet whether it is
   *clear*, and Opus whether it *over-explains*.

| Scenario | Haiku | Sonnet | Opus | Baseline |
|---|---|---|---|---|
| khmer-company-profile | – / 8 | – / 8 | – / 8 | – / 8 |
| english-personal-profile | – / 7 | – / 7 | – / 7 | – / 7 |
| vue-tailwind-component | – / 7 | – / 7 | – / 7 | – / 7 |

When a line fails, fix the skill (usually `SKILL.md` or the relevant reference), then re-run that scenario.
