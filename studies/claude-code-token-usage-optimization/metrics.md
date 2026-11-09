# Effectiveness metrics: full table

Companion to `README.md`, Question 2. Source notes: `sources/q6-measuring-effectiveness.md`.

## What counts as a "task"

A task is one owner request that ends in a deliverable. Cheap first version: one user text turn that is not a task-notification or tool result, plus all work (main thread and its subagents) until the next such turn. Long orchestrator sessions like project A make task boundaries fuzzy, so a better rule (merge turns until "done", a commit or a new topic) is still needed.

## Metrics

| Metric | Formula | Data source |
|---|---|---|
| Cost-weight per task (main cost metric) | Sum over all turns, including subagents, of input + 1.25 x cache write (5 min) or 2 x cache write (1 h) + 0.1 x cache read + 5 x output, in input-price units. (On the API, cache read is 0.05 x for Opus 5.5 and Sonnet 5.5, so use 0.05 there if you want API-price weights.) Or USD from the tracker's `pricing.py`. | Session JSONL / token tracker DB |
| Tokens per finished task | All tokens in the task, including failed and restarted agents, / number of finished tasks | JSONL |
| Failure overhead | Tokens in agents that were later followed by a restart or continuation / all tokens | JSONL (baseline: 18 "restart" agents, 52 continuation-type) |
| Restart rate | Restart or redo subagents / all subagents | JSONL |
| Correction rate | Owner turns with correction cues (keyword or LLM tagged, spot-checked by hand) / owner turns. Also count tool-use interrupts. | JSONL |
| Tool error rate | Tool results with errors / tool calls. Also count repeated identical failing calls. | JSONL |
| Test fail-then-fix | Test commands with non-zero exit followed by an edit and a pass, per task. Also tasks that end with failing tests. | JSONL Bash results |
| Revert / rework rate | Commits reverted, or files re-edited within 24 h of a commit / commits | git log in the project repos |
| Edit rejection | Rejected or aborted edits / edit decisions | JSONL, or OTel `claude_code.code_edit_tool.decision` |
| Fixed-task bank score | Checklist pass fraction per trial, pass^k over k = 3, plus tokens per trial | A/B harness (Q5) |
| Wake-ups per task | Task-notification turns / task | JSONL |
| Cache read per user turn, per subagent | Cache read / owner turns; cache read / subagents | JSONL (the study's success metric) |

**Rule:** a token saving counts only if cost per task falls and correction, restart, revert and bank score do not get worse beyond the noise band.

## Why these, with sources

- SWE-Effi plots resolved issues against tokens per issue, and finds failed attempts cost far more than successes (8.8 M vs 1.8 M tokens in its headline example). So failures must be included in tokens per finished task. [SWE-Effi](https://arxiv.org/html/2509.09853v2) — accessed 2026-11-07
- Anthropic's eval guidance: track tokens, cost per task, turns, tool calls and latency next to the grade. Run several trials per task. Use pass^k for repeatable work. Start each trial from a clean environment. Grade outputs, not the path. Give the judge an "Unknown" option, one judge per dimension, and calibrate against human grades. [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — accessed 2026-11-07
- Claude Code OpenTelemetry has `claude_code.token.usage` (input/output/cacheRead/cacheCreation), `claude_code.cost.usage` (with query_source main/subagent/auxiliary), `claude_code.code_edit_tool.decision`, and `tool_result` / `api_request` events. Prompt and tool content are off by default. [Claude Code monitoring](https://code.claude.com/docs/en/monitoring-usage) — accessed 2026-11-07
- The next user prompt gave a satisfaction signal in about 8% of interactions, over 13x the rate of explicit feedback. [Reading Between the Lines](https://arxiv.org/abs/2509.18361) — accessed 2026-11-07
- LLM judges have position, verbosity and self-enhancement bias. [MT-Bench](https://arxiv.org/abs/2306.05685) — accessed 2026-11-07; [Self-Preference Bias](https://arxiv.org/html/2410.21819v1) — accessed 2026-11-07
- "Evaluations are experiments": use error bars and plan the sample size. [Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640) — accessed 2026-11-07. A search summary says the paper recommends paired per-question differences and warns about clustered items (unverified, full paper not read).

## Statistics rules (researcher's suggestion, unverified)

These did not come from a fetched source:

- Use medians and a paired design on the task bank.
- Bootstrap the per-task ratio (resample tasks 10,000 times, report a 95% interval).
- Expect to need roughly 20-30 tasks per arm to see a large (25%+) effect in heavy-tailed token data. Small effects need more.
- Compare the same task types on both sides (project A, project B, project C separately). Do not compare day totals.
- Run a null check first: split the baseline period in two halves and see how big the "difference" is with no change.
- Label about 50 tasks by hand to check that restart and correction signals agree with real quality.

## Possible token-tracker additions (not built)

Task segmentation table; per-subagent flags (model, restart/continuation, parent task); outcome events (tool error, test fail/pass, interrupt, correction tag, commit sha); a `compare` command for two date ranges with median + bootstrap interval; a change log ("change X applied at time T"). The tracker DB schema could not be read, so these are suggestions only.
