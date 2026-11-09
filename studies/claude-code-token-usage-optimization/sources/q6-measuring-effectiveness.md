# Q6 — Measuring whether a token-saving change kept quality

Researched 2026-11-07. Facts below come from pages fetched this session. Anything marked
"(unverified)" or "(my suggestion)" did not come from a fetched page.

## Short answers

### 1. Metrics others use
- Agent benchmarks pair a pass/fail score with resource use. SWE-Effi plots "resolved issues vs
  tokens (or cost, or time) per issue" and takes the area under that curve, with caps of 2M tokens,
  $1.00 and 30 min. It finds failed attempts cost much more than successes (its headline example:
  8.8M tokens for a failure vs 1.8M for a success, SWE-Agent with GPT-4o-mini). So tokens per
  *finished* task must count the tokens of failed and restarted attempts. [SWE-Effi](https://arxiv.org/html/2509.09853v2) — accessed 2026-11-07
- Simpler convention in papers: total spend including failures divided by resolved count. Some papers
  count only resolved runs, so numbers are not comparable across papers. (search-snippet summary, not
  checked on the individual pages: [REAgent](https://arxiv.org/pdf/2604.06861), [AutoCodeRover](https://arxiv.org/pdf/2404.05427)) — accessed 2026-11-07
- Anthropic's eval guidance: once you have a fixed task bank, track tokens, cost per task, turns,
  tool calls and latency next to the grade. Run several trials per task because outputs vary.
  Use pass@k (at least one of k succeeds) or pass^k (all k succeed); for repeatable personal work
  pass^k is the more honest one. Start each trial from a clean environment; Anthropic saw an agent
  read git history left by earlier trials. [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — accessed 2026-11-07
- Terminal-Bench: could not verify scoring or cost reporting; its docs page only says it runs in Harbor.
  [Terminal-Bench docs](https://www.tbench.ai/docs) — accessed 2026-11-07 (gap)
- Claude Code OpenTelemetry (verified names, all prefixed `claude_code.`):
  metrics `session.count`, `lines_of_code.count` (type added/removed), `pull_request.count`,
  `commit.count`, `cost.usage` (USD; attrs model, query_source main/subagent/auxiliary, effort, agent.name),
  `token.usage` (type input/output/cacheRead/cacheCreation), `code_edit_tool.decision`
  (accept/reject, source incl. user_reject, user_abort), `active_time.total` (user vs cli seconds).
  Events: `user_prompt`, `tool_result` (success, error_type, duration_ms), `api_request` (cost_usd, tokens,
  cache_creation_5m/1h), `api_error`, `tool_decision`, `assistant_response`, plus a `subagent_completed`
  event named on the page whose attributes were not read. Content (prompts, tool details) is off by default
  and needs OTEL_LOG_USER_PROMPTS=1 / OTEL_LOG_TOOL_DETAILS=1. Only the first 100k of 173k characters of
  the page were read. [Claude Code monitoring](https://code.claude.com/docs/en/monitoring-usage) — accessed 2026-11-07
  Relevance: these give cost and a few outcome proxies (edit rejects, tool errors, commits) but no
  task boundary and no correctness measure. The local JSONL already holds the same facts.
- ccusage: reads local agent logs; daily/weekly/monthly/session/5-hour-block reports; cache read and
  creation kept separate; JSON output; pricing from a LiteLLM file. It says nothing about quality.
  [ccusage repo](https://github.com/ryoppippi/ccusage) — accessed 2026-11-07

### 2. Quality signals readable from transcripts
- Published work is thin. Closest: Google's Cider Chat study ran an off-the-shelf sentiment tool on
  developer prompts from 372 developers; about 8% of interactions gave a satisfaction signal, over
  13x the rate of explicit feedback, "reasonable accuracy". Idea: the next user prompt rates the previous
  answer. [Reading Between the Lines (arXiv 2509.18361)](https://arxiv.org/abs/2509.18361) — accessed 2026-11-07
- Other negative cues named in a (search-snippet-only) summary: repeat/clarify requests, rephrased
  retries, abandonment, user edits to assistant code. [Conv-to-Bench](https://arxiv.org/pdf/2605.26440) — accessed 2026-11-07 (snippet only, page not fetched)
- Rework metrics in industry: mostly vendor blogs. GitClear (211M changed lines, 2020-2024) reports
  cloned lines 8.3% to 12.3% and refactor-associated lines 25% to under 10%; its page gave no definition
  of churn. [GitClear 2025 report](https://www.gitclear.com/ai_assistant_code_quality_2025_research) — accessed 2026-11-07
  Figures like "80-90% acceptance falls to 10-30% effective acceptance" are from vendor blogs and I could
  not trace them to a study; do not rely on them.
- No fetched study validates "restart agent", "interrupt" or "reverted commit" as quality proxies on
  agent transcripts. That validation has to be done locally (spot-check, see open questions).
- Perceived vs measured effect differ a lot: in METR's RCT (16 developers, 246 tasks) developers
  expected -24% time, believed -20% afterwards, measured +19%. Reason to not trust "it felt fine".
  [METR RCT (arXiv 2507.09089)](https://arxiv.org/abs/2507.09089) — accessed 2026-11-07

### 3. Before/after with a changing workload, and judges
- Anthropic's stats paper (Evan Miller): "evaluations are experiments"; it gives formulas for error bars,
  comparing two models, and planning sample size. [Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640) — accessed 2026-11-07
  A search summary says it recommends paired per-question differences and warns that clustered items make
  standard errors too small (about 3x in one secondary claim); I did not read the full paper, so treat
  those details as unconfirmed.
- Best design for one person: a fixed bank of repeatable tasks (A/B), same tasks both arms, several
  trials each, paired comparison. Natural-workload comparison (no fixed tasks) is much weaker.
- LLM judge biases (verified from the MT-Bench abstract): position, verbosity, self-enhancement, limited
  reasoning; strong judges reach over 80% agreement with humans, similar to human-human agreement.
  [MT-Bench paper](https://arxiv.org/abs/2306.05685) — accessed 2026-11-07
  Self-preference: GPT-4 judge had the strongest self-preference of 8 judges tested; authors suggest
  judges favour lower-perplexity (familiar) text; evidence is correlational. [Self-Preference Bias](https://arxiv.org/html/2410.21819v1) — accessed 2026-11-07
  Anthropic: prefer grading outputs not the path; give the judge an "Unknown" exit; one judge per
  dimension; calibrate against human grades; read many transcripts. Same source as above.
  Implication here: Opus-vs-Sonnet outputs judged by a Claude model means self-preference risk. Use
  swapped order, a checklist with code-checkable items first, and spot-check by hand.
- Sample size rules of thumb, bootstrap, medians: (my suggestion, no fetched source) see below.

## Proposed metric set
Task = one owner request that ends in a deliverable. Define it from the main thread: user text turns
that are not task-notifications/tool results, merged until a "done"/commit/next topic (needs a rule).
Cheaper first version: task = one non-notification user turn plus all work until the next one.

| Metric | Formula | Data source |
|---|---|---|
| Cost-weight per task (primary cost) | sum over all turns incl. subagents of (input + 1.25*cache_create(5m)/2*cache_create(1h) + 0.1*cache_read + 5*output) in input-price units, or just ccusage-style USD via tracker `pricing.py`; per task window | session JSONL / tracker DB |
| Tokens per finished task | total tokens in task incl. failed and restarted agents / count of finished tasks | JSONL |
| Failure overhead | tokens spent in agents later followed by a restart/continuation / total tokens | JSONL (subagent ids, "restart" labels the proposal already counted: 18) |
| Restart rate | restart or redo subagents / all subagents | JSONL |
| Correction rate | user turns after a task that contain correction cues (LLM or keyword tagged, spot-checked) / user turns; also tool-use interrupt markers | JSONL |
| Tool error rate | tool_result errors / tool calls; repeated identical failing call count | JSONL (OTel `tool_result.success` equivalent) |
| Test fail-then-fix | Bash test commands with non-zero exit followed by edit then pass, per task; and tasks ending with failing tests | JSONL Bash results |
| Revert/rework rate | commits reverted or files re-edited within 24h of the commit / commits | git log in project repos |
| Edit rejection | `code_edit_tool.decision=reject` equivalents (user_reject/user_abort) / edit decisions | JSONL or OTel |
| Fixed-task bank score | checklist pass fraction per trial, pass^k over k=3, plus tokens per trial | A/B harness (Q5) |
| Wake-ups per task | task-notification turns / task | JSONL |

Rule: a token saving counts only if cost per task falls and correction, restart, revert and bank score
do not worsen beyond the noise band.

Stats (my suggestion, unverified): use medians and a paired design on the bank; bootstrap the
per-task ratio (resample tasks, 10k times, report 95% interval); expect to need on the order of 20-30
tasks per arm for a large effect (25%+) in heavy-tailed token data, more for small ones; use the same
task types on both sides (project A variants, project B, project C separately); do not compare day totals.
Run a null check first: split the baseline period in two halves and see how big the "difference" is
with no change.

## What claude-token-tracker could add (not changed)
Its CLAUDE.md lists: session ingester of JSONL, DB at ~/.claude-tracker/usage.db, query/report layer,
pricing.py, MCP server. I could not read the DB schema (sqlite3 returned nothing), so these are
suggestions: (1) task segmentation table (task id, start/end, user-turn text hash); (2) per-subagent
flags (model, restart/continuation, parent task); (3) outcome events table (tool error, test fail/pass,
interrupt, user correction tag, commit sha); (4) a `compare` command: two date ranges or labelled
change-tags, median + bootstrap CI per metric; (5) change log table to mark "change X applied at time T".

## Open questions
- No published validation that restart/correction/revert signals track real quality for agent work; needs a local spot-check (label ~50 tasks by hand, check agreement).
- Task boundaries in long-lived orchestrator sessions (project A) are fuzzy.
- Terminal-Bench cost reporting not verified. Bootstrap/sample-size guidance not backed by a fetched source.
- OTel page truncated at 100k chars; `subagent_completed` attributes unknown (could give per-agent tokens).
- Whether Claude judge on Claude output is acceptable for the Sonnet-vs-Opus A/B; consider a code-checkable checklist to avoid it.

## Sources
All links are inline above, each "accessed 2026-11-07". Snippet-only (not fetched): REAgent, AutoCodeRover, Conv-to-Bench.
