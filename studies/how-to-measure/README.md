---
title: "How to Measure a Research Method: Benefits, Tradeoffs, and Metrics"
date: 2026-11-09
status: complete
confidence: high
confidence_reason: "Backed by 18 primary benchmark and evaluation papers fetched from arXiv/PMC/Anthropic (including 4 human-validated 2025–2026 deep-research benchmarks: DeepResearch Bench I & II, ResearchRubrics, DeepScholar-Bench, and Mind2Web 2), a 5-repository GitHub API probe, and 4 internal empirical studies."
completeness: 90
completeness_reason: "Covers all 14 method-level benefit/cost dimensions, 7 measured tradeoffs, the 5-repo probe, gaming vulnerabilities, the 3-tier operational scorecard (SCORECARD.md), the 2-agent blind inter-rater exam (85.0% agreement), and baseline numbers for all 4 internal pipeline variants. Missing: whole-pipeline multi-run consistency (k>=3) on our post-fix hybrid method, logged human minutes, and a populated claim-calibration ledger."
category: methodology
tier: 3
objective: "Determine what an AI research method can be good or bad at, how to measure each dimension and its tradeoffs, and which measurements can be applied fairly from outside to external GitHub repos and to our own research pipeline."
summary: "No single benchmark grades a whole research method, and a 5-repo probe shows only 2 of 5 public repos publish sample outputs and 1 of 5 publishes costs. We build a 3-tier scorecard (SCORECARD.md): an 8-item binary Desk audit for any repo (validated at 85.0% blind 2-agent agreement), a 6-item Output rubric (binary checklists + claim-entailment spot-checks + length control), and a 6-item Run protocol (token/dollar Pareto frontier + pass^k consistency)."
why: "Unblocks the GitHub research-methods survey (01-github-research-methods-survey) with a fair, repeatable scorecard and defines which method-level metrics we record on our own studies."
blockers: []
source_count: 26
known_gaps:
  - "Whole-pipeline multi-run consistency (pass^3) has only been measured at the single-researcher level (Q5: k=2 runs across 3 tasks), not yet across full multi-agent + writer + Opus-checker studies."
  - "Post-fix hybrid README (with the <=3,500-word cap, answer-first structure, and Opus faithfulness pass adopted on 2026-11-08) has not yet been re-scored in a blind pairwise judge or post-checker claim spot-check."
  - "Human effort (minutes spent scoping/reviewing proposals and auditing finished reports) is unmeasured across all internal pipeline runs."
  - "Calibration error (Brier / ECE) cannot be computed for our method until the claim ledger accumulates resolved predictions across 10+ studies."
  - "Pre-commit deterministic gate scripts (HTTP 200 link check, paragraph citation check, domain diversity check) are specified in SCORECARD.md but not yet wired into automated repo CI."
next_steps:
  - "Use SCORECARD.md Tier A (D1–D8) and Tier B (O1–O6, where sample outputs exist) to score all candidate repositories in 01-github-research-methods-survey."
  - "Log end-to-end token spend, wall time, and post-checker claim support on the next 3 Tier-3 studies to fill the post-fix hybrid baseline gaps in SCORECARD.md."
  - "Add a human-minutes field (scoping_minutes, review_minutes) to study run logs so R4 (Human Effort) can be compared against token spend."
quality_checklist:
  sourced_claims: true
  cross_referenced: true
  flagged_contradictions: true
  verified_surprising: true
  noted_confidence: true
  listed_gaps: true
  targeted_prompts: true
  within_budget: true
---

# How to Measure a Research Method: Benefits, Tradeoffs, and Metrics

## Short answer

**What can a research method be good or bad at?**
An earlier study in this repo (`[repo: research-quality-metrics/README.md]`) defined seven dimensions for grading **one finished report**. Grading a **research method** is broader because a method is a repeatable process with resource costs and run-to-run variance. Across 18 primary evaluation papers and 4 internal studies ([sources/a-benchmarks-and-metrics.md](sources/a-benchmarks-and-metrics.md)), what a research method can be good or bad at decomposes into **14 dimensions across four families**:
1. **Output Quality (7):** Factual accuracy (world truth), citation faithfulness (source entailment vs. post-rationalization), coverage/recall of vital sub-questions, source quality/diversity/independence, confidence calibration, analytical depth & decision actionability, and readability/length discipline.
2. **Efficiency & Cost (3):** Total token and API dollar spend, wall-clock latency, and human effort (minutes spent guiding the run and verifying outputs).
3. **Reliability & Reuse (2):** Run-to-run repeatability across trials ($\text{pass}^k$ consistency and cost variance) and cross-study reuse without propagating errors.
4. **Engineering & Adoption (2):** Failure behaviour under dead ends or unanswerable queries (bounded budgets + explicit abstention) and ease of adoption / audit-trail persistence.

**How do you measure each of those things — and can we just use an existing benchmark?**
No single published benchmark measures a whole research method. Four major benchmarks for deep-research agents launched in 2025–2026 — **DeepResearch Bench I & II** ([Du et al. 2025](https://arxiv.org/html/2506.11763v1) — accessed 2026-11-09; [Li et al. 2026](https://arxiv.org/html/2601.08536v3) — accessed 2026-11-09), **ResearchRubrics** ([Sharma et al. 2025](https://arxiv.org/html/2511.07685v1) — accessed 2026-11-09), **DeepScholar-Bench** ([Patel et al. 2025](https://arxiv.org/html/2508.20033v2) — accessed 2026-11-09), and **Mind2Web 2** ([Gou et al. 2025](https://arxiv.org/html/2506.21506v1) — accessed 2026-11-09) — and all four validate their automated judges against human experts. However, none is used by 3+ independent open-source methods, and all four grade **single outputs** rather than method-level token cost, human time, desk architecture, or multi-run consistency. Short-answer browsing benchmarks like **BrowseComp** ([Wei et al. 2025](https://arxiv.org/html/2504.12516v1) — accessed 2026-11-09) and **GAIA** ([Mialon et al. 2023](https://arxiv.org/abs/2311.12983) — accessed 2026-11-09) test needle-in-a-haystack lookup but miss synthesis, coverage, and citation faithfulness.

Instead of adopting one benchmark, we combine the **three best-validated measurement instruments** from that literature:
- **Fine-grained binary (`0`/`1`) rubric checklists** (`ResearchRubrics`, `DRB II`, `Mind2Web 2`) for coverage and analysis — binary grading beats partial-credit scales by **~20 percentage points** in human–LLM agreement (`0.72–0.76` vs `0.53–0.57` Macro F1 in [ResearchRubrics, Sharma et al. 2025](https://arxiv.org/html/2511.07685v1) — accessed 2026-11-09; `91.75%` accuracy in [DeepResearch Bench II, Li et al. 2026](https://arxiv.org/html/2601.08536v3) — accessed 2026-11-09).
- **Claim-level URL entailment checks** (`ALCE`, `FACT`, `Mind2Web 2`, `PaperQA2`) that fetch the cited URL and verify whether it supports the sentence — catching citation drift that holistic LLM judges miss ([ALCE, Gao et al. 2023](https://ar5iv.labs.arxiv.org/html/2305.14627) — accessed 2026-11-09; `[repo: research-pipeline-hybrid-comparison/README.md]`).
- **2D Pareto cost curves and multi-trial consistency ($\text{pass}^k$)** ([AI Agents That Matter, Kapoor et al. 2024](https://arxiv.org/html/2407.01502v1) — accessed 2026-11-09; [$\tau$-bench, Yao et al. 2024](https://arxiv.org/html/2406.12045v1) — accessed 2026-11-09) so a method cannot win simply by burning 15×–50× more tokens or getting lucky once.

**Which measurements can we actually apply to other people's repos vs. our own?**
Our 5-repo probe ([sources/b-tradeoffs-and-probe.md](sources/b-tradeoffs-and-probe.md)) found that **only 2 of 5 public repos commit sample long-form reports**, **only 2 of 5 publish in-repo evaluation numbers (on incompatible tasks)**, and **only 1 of 5 (`gpt-researcher`) publishes dollar or token costs**. Because public repos rarely publish enough to score outputs or costs from outside, **[SCORECARD.md](SCORECARD.md)** splits measurement into three tiers:
1. **Tier A — Desk Scorecard (`D1–D8`, 8 binary items):** Applied to **every repo** in 5 minutes for $0 by inspecting code and prompts.
2. **Tier B — Output Scorecard (`O1–O6`, 6 gated items):** Applied whenever a repo commits sample outputs (or after a test run): link resolution, domain diversity, sampled claim-entailment spot-check, binary checklist coverage, gap honesty, and length-controlled readability.
3. **Tier C — Run Scorecard (`R1–R6`, 6 items):** Applied to our own pipeline and top external finalists by running them on shared questions: total tokens/USD, quality per 100k tokens, wall time, human minutes, $\text{pass}^3$ consistency, and calibration error.

---

## 1. Benefits, Costs, and Metrics Across All 14 Dimensions

Full formulas are in [sources/a-benchmarks-and-metrics.md](sources/a-benchmarks-and-metrics.md); operational scoring rules are in [SCORECARD.md](SCORECARD.md).

| Family | Dimension | Best Published Metric / Benchmark | Human Validation | Access Tier | How Gamed & Countermeasure |
|---|---|---|---|---|---|
| **Output Quality** | **1. Factual accuracy** | **SAFE + LongFact** ($\text{F1}@K$, [Wei et al. 2024](https://arxiv.org/html/2403.18802v2) — accessed 2026-11-09); **BrowseComp** ([Wei et al. 2025](https://arxiv.org/html/2504.12516v1) — accessed 2026-11-09); **LitQA2** ([Skarlinski et al. 2024](https://arxiv.org/html/2409.13740v2) — accessed 2026-11-09) | SAFE agrees with humans 72.0% ($n=16,011$) and wins 76% of disputes at $0.19 vs $4.00/response | Output / Run | *Gaming:* Outputting only 3 safe truisms (100% precision).<br>*Fix:* Pair precision with recall ($\text{F1}@K$ or `O4`). |
| | **2. Citation faithfulness** | **ALCE** ([Gao et al. 2023](https://ar5iv.labs.arxiv.org/html/2305.14627) — accessed 2026-11-09); **DRB I `FACT`** ([Du et al. 2025](https://arxiv.org/html/2506.11763v1) — accessed 2026-11-09); **Mind2Web 2 Attribution** ([Gou et al. 2025](https://arxiv.org/html/2506.21506v1) — accessed 2026-11-09); **Counterfactual test** ([Wallat et al. 2024](https://arxiv.org/html/2412.18004v1) — accessed 2026-11-09) | ALCE $\kappa = 0.698$ (recall), $0.525$ (precision); Mind2Web 2 verifier 98.89% accurate ($712/720$) | Output (`O1`, `O3`) | *Gaming:* Decorative refs ([GPT-Researcher](https://github.com/assafelovic/gpt-researcher/blob/main/evals/README.md) — accessed 2026-11-09) or post-rationalized citations (57% in [Wallat et al. 2024](https://arxiv.org/html/2412.18004v1) — accessed 2026-11-09).<br>*Fix:* Fetch URL and verify numbers/quotes (`O3`). |
| | **3. Coverage & recall** | **DRB II InfoRecall** (9,430 binary rubrics, [Li et al. 2026](https://arxiv.org/html/2601.08536v3) — accessed 2026-11-09); **ResearchRubrics** (2,593 criteria, [Sharma et al. 2025](https://arxiv.org/html/2511.07685v1) — accessed 2026-11-09); **DeepScholar Nugget Cov.** ([Patel et al. 2025](https://arxiv.org/html/2508.20033v2) — accessed 2026-11-09) | DRB II 91.75% ACC / 89.57% F1 ($0.25/task); ResearchRubrics 0.72–0.76 Macro F1; DeepScholar 83.3% agreement | Output / Run (`O4`) | *Gaming:* Writing 7,500+ words to hit more items ($r=0.24\text{--}0.28$).<br>*Fix:* Cap length at $\le 3,500$ words (`O6`). |
| | **4. Source quality & diversity** | **Domain diversity & entropy** (`[repo: research-quality-metrics/README.md]`; [GPT-Researcher](https://github.com/assafelovic/gpt-researcher/blob/main/evals/README.md) — accessed 2026-11-09); **DeepScholar `Doc. Imp.`** ([Patel et al. 2025](https://arxiv.org/html/2508.20033v2) — accessed 2026-11-09) | DeepScholar Reference Importance 65.9% human agreement; domain diversity is deterministic | Output (`O2`) | *Gaming:* Citing 10 mirrors of one press release.<br>*Fix:* Cap single domain $\le 40\%$ and check independence. |
| | **5. Calibration & gap honesty** | **Brier Score / ECE** (`[repo: research-quality-metrics/README.md]`; [BrowseComp](https://arxiv.org/html/2504.12516v1) — accessed 2026-11-09); **PaperQA2 abstention & `ContraCrow`** ([Skarlinski et al. 2024](https://arxiv.org/html/2409.13740v2) — accessed 2026-11-09) | ContraCrow 70% human-validated ($\text{F1}=0.82$, $p=10^{-4}$); Brier is a proper scoring rule | Desk (`D5`) + Output (`O5`) + Run (`R6`) | *Gaming:* Guessing when unsure (BrowseComp DR calibration error = 91%) or generic disclaimers.<br>*Fix:* Reward abstention / `(unverified)` markers; track Brier. |
| | **6. Analytical depth & usefulness** | **DRB I `RACE` Depth** ([Du et al. 2025](https://arxiv.org/html/2506.11763v1) — accessed 2026-11-09); **DRB II Analysis** ([Li et al. 2026](https://arxiv.org/html/2601.08536v3) — accessed 2026-11-09); **Pairwise Actionability Judge** (`[repo: research-pipeline-hybrid-comparison/README.md]`) | DRB I RACE 71.33% pairwise agreement with experts (vs 68.44% human inter-agreement) | Output (`O4`, `O6`) | *Gaming:* Fluent summary without synthesis.<br>*Fix:* Require synthesis items in `O4` and `ai-instructions.md`. |
| | **7. Readability & length control** | **AlpacaEval-LC** ([Dubois et al. 2024](https://arxiv.org/html/2404.04475v2) — accessed 2026-11-09); **STORM Organization** ([Shao et al. 2024](https://arxiv.org/html/2402.14207v2) — accessed 2026-11-09); **DeepScholar `Org.`** ([Patel et al. 2025](https://arxiv.org/html/2508.20033v2) — accessed 2026-11-09) | AlpacaEval-LC Spearman $r=0.98$ with Chatbot Arena; DeepScholar `Org.` 71.43% agreement (raw 1–7 human ratings in STORM had $\alpha=0.221$) | Output (`O6`) | *Gaming:* Verbosity bias (shifts judge win rate from 22.9% to 64.3%) and position bias.<br>*Fix:* Swap order, cap words, and gate on `O1–O4` first. |
| **Efficiency & Cost** | **8. Token & dollar cost** | **Accuracy-vs-Cost Pareto Curve** ([Kapoor et al. 2024](https://arxiv.org/html/2407.01502v1) — accessed 2026-11-09); **Quality per 1k tokens** (`[repo: web-search-methodology/README.md]`) | Exact billing/token logs | Desk (`D3`, `D8`) + Run (`R1`, `R2`) | *Gaming:* Omitting subagent/pre-filter tokens or burning 50× compute for +1% accuracy.<br>*Fix:* Log wall-to-wall tokens + USD. |
| | **9. Wall-clock latency** | **End-to-end elapsed minutes** ([Mind2Web 2](https://arxiv.org/html/2506.21506v1) — accessed 2026-11-09; `[repo: research-pipeline-hybrid-comparison/README.md]`) | Exact timer | Run (`R3`) | *Gaming:* Over-parallelizing past HTTP 429 limits.<br>*Fix:* Log failed/rate-limited calls. |
| | **10. Human effort** | **Active human minutes** ([Millard et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6911272) — accessed 2026-11-08 `[repo: research-duplication-and-reuse/README.md]`) | Exact stopwatch log | Run (`R4`) | *Gaming:* Ignoring post-run human fact-check time.<br>*Fix:* Sum pre-run scoping + post-run audit minutes. |
| **Reliability & Reuse** | **11. Repeatability** | **$\text{pass}^k$ consistency** ([$\tau$-bench, Yao et al. 2024](https://arxiv.org/html/2406.12045v1) — accessed 2026-11-09); **Pass@3 & SD** ([Mind2Web 2](https://arxiv.org/html/2506.21506v1) — accessed 2026-11-09) | Exact over $k$ trials | Run (`R5`) | *Gaming:* Cherry-picking best of 5 runs.<br>*Fix:* Report mean $\pm$ SD and $\text{pass}^3$. |
| | **12. Reuse & memory** | **Proposal overlap recall (`find_prior.py`) & A/B token savings** (`[repo: research-duplication-and-reuse/README.md]`; [Xiong et al. 2025](https://arxiv.org/html/2505.16067v1) — accessed 2026-11-09) | Empirically tested in repo (`Q1`, `Q4`, `Q5`) | Desk + Run | *Gaming:* Feeding unverified old notes to researchers (saved 3% tokens, copied 1 error).<br>*Fix:* Cut scope at proposal time; re-verify `[repo: ...]` claims. |
| **Engineering & Adoption** | **13. Failure behaviour** | **Turn caps (`D3`) + abstention (`D5`) + perturbation test** ([GPT-Researcher `perturbation.py`](https://github.com/assafelovic/gpt-researcher/blob/main/evals/README.md) — accessed 2026-11-09) | Deterministic desk/code check | Desk (`D3`, `D5`) | *Gaming:* Silent fallback to guessing when search fails.<br>*Fix:* Inspect code for hard caps and abstention prompts. |
| | **14. Adoption & auditability** | **PRISMA 2020 provenance items** ([Page et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/) — accessed 2026-11-09); **Desk items `D6–D8`** ([SCORECARD.md](SCORECARD.md)) | Deterministic desk inspection | Desk (`D6–D8`) | *Gaming:* Keeping Heavy Mode or eval data closed ([Alibaba-NLP/DeepResearch FAQ](https://github.com/Alibaba-NLP/DeepResearch/blob/main/FAQ.md) — accessed 2026-11-09).<br>*Fix:* Score only files committed in git. |

---

## 2. Seven Measured Tradeoffs Every Method Faces

Full evidence tables are in [sources/b-tradeoffs-and-probe.md](sources/b-tradeoffs-and-probe.md):

1. **Token spend vs. coverage (and saturation on simple facts):**
   In Anthropic's BrowseComp analysis, **token usage alone explained 80% of performance variance** (tool calls and model choice explained another 15%); multi-agent (`Claude Opus 4` lead + `Sonnet 4` subagents) beat single-agent `Opus 4` by **90.2%** but used **~15× more tokens than chat** (vs. **~4×** for a single agent) ([Anthropic Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system) — accessed 2026-11-09). In `gpt-researcher` ($n=8$ open-ended tasks), passing all scraped pages unfiltered ($0.284/report) beat embedding-filtered context ($0.155/report) **8–0** at **65–83% higher cost**, yet on factual lookups (`SimpleQA`, $n=20$) every strategy scored **18–20/20** ([GPT-Researcher Context Filter Benchmark](https://github.com/assafelovic/gpt-researcher/blob/main/evals/context_filter/README.md) — accessed 2026-11-09). In `[repo: web-search-methodology/README.md]`, directed R3 search matched naive quality (**93.5%**) at **53% of the token cost** (26.2k vs 49.6k tokens).
2. **Citation breadth vs. citation faithfulness ("citation theater"):**
   In both **DeepResearch Bench I** and **ResearchRubrics**, `Gemini DR` averaged **111 citations at 81% accuracy**, whereas `Perplexity DR` averaged **31 citations at 90% accuracy** ([Du et al. 2025](https://arxiv.org/html/2506.11763v1) — accessed 2026-11-09; [Sharma et al. 2025](https://arxiv.org/html/2511.07685v1) — accessed 2026-11-09). On **DeepScholar-Bench**, `OpenAI DeepResearch` led on coverage (`Nug. Cov.` 0.392) but fell to **0.399 Citation Precision and 0.138 Claim Coverage**, while `DeepScholar-ref (GPT-4.1, Claude)` hit **0.944 Citation Precision and 0.895 Claim Coverage** ([Patel et al. 2025](https://arxiv.org/html/2508.20033v2) — accessed 2026-11-09). In `gpt-researcher`, sample runs achieved **0.94 bibliography citation faithfulness** while **53.5% of claims were unsupported** ([GPT-Researcher Evals README](https://github.com/assafelovic/gpt-researcher/blob/main/evals/README.md) — accessed 2026-11-09), and **up to 57% of RAG citations are post-rationalized** ([Wallat et al. 2024](https://arxiv.org/html/2412.18004v1) — accessed 2026-11-09).
3. **Report length & surface polish vs. human usability & recall:**
   In **DeepResearch Bench II** (132 tasks, 9,430 binary rubrics), all agents scored **74.6%–91.9% on Presentation**, yet even the top agent (`OpenAI-GPT-o3 DR`) passed only **45.4% of rubrics overall** (**40.0% InfoRecall**, **49.9% Analysis**) ([Li et al. 2026](https://arxiv.org/html/2601.08536v3) — accessed 2026-11-09). In **Mind2Web 2**, humans achieved **54% success in 186 words**, `OpenAI DR` got **28% in 559 words**, and `Gemini DR` wrote **3,357 words (18× longer) for 18% success** ([Gou et al. 2025](https://arxiv.org/html/2506.21506v1) — accessed 2026-11-09). In `[repo: research-pipeline-hybrid-comparison/README.md]`, Arm C's 7,739-word README scored 5/5 on coverage but **2/5 on readability**.
4. **Separate writer isolation vs. synthesis claim drift:**
   In `[repo: research-pipeline-hybrid-comparison/README.md]`, handing researcher notes to a separate writer won full-package usefulness (**2/2**) **but introduced claim drift**: Arm A (same-session writer) had **94% (15/16) fully supported claims**, vs. **81% (26/32)** for Arm C and **74% (26/35)** for Arm B. The blind LLM judge gave Arm B **4–5/5 on groundedness**, proving holistic judges miss claim drift without a dedicated source-verification pass.
5. **Web browsing access vs. confidence calibration error:**
   On **BrowseComp**, web browsing raised accuracy from **0.6%** (`GPT-4o`) and **9.9%** (`o1`) to **51.5%** (`OpenAI DR`), **but worsened calibration error from 65–69% to 82% (`GPT-4o w/ browsing`) and 91% (`OpenAI DR`)** ([Wei et al. 2025](https://arxiv.org/html/2504.12516v1) — accessed 2026-11-09). Conversely, **PaperQA2** beat Biology PhDs on `LitQA2` precision (**85.2% vs 73.8%**, $p=0.0036$) by abstaining on **21.9%** of questions ([Skarlinski et al. 2024](https://arxiv.org/html/2409.13740v2) — accessed 2026-11-09).
6. **In-run note reuse vs. error propagation:**
   In `[repo: research-duplication-and-reuse/README.md]`, telling a 30-turn researcher to read prior repo notes saved only **3% of tokens** (830k vs 858k) and **copied an old repo error (`rho = .724`) into a headline** ([Xiong et al. 2025](https://arxiv.org/html/2505.16067v1) — accessed 2026-11-09).
7. **Single-run cost vs. run-to-run variance:**
   On $\tau$-bench, `gpt-4o` dropped from **~61% $\text{pass}^1$** to **<25% $\text{pass}^8$** ([Yao et al. 2024](https://arxiv.org/html/2406.12045v1) — accessed 2026-11-09). In our `Q5` baseline pairs (`[repo: research-duplication-and-reuse/README.md]`), identical runs varied by **1.56× in tokens (855k vs 1,334k)**, **9 vs 15 new sources**, and **4% vs 12% claim change rate**.

---

## 3. 5-Repo Probe & Baseline Summary

Full item-by-item scoring is in **[SCORECARD.md](SCORECARD.md)**:

| Method / Repository | Sample Outputs in Repo (`D7`)? | Eval Numbers in Repo? | Cost Figures in Repo (`D8`)? | Tier A Desk Score (`0–8`) | Key Baseline / Probe Findings ([SCORECARD.md](SCORECARD.md)) |
|---|---|---|---|---|---|
| **Our Current Hybrid + R3 Standard** (`[repo: CLAUDE.md]`) | **Yes** (100+ studies) | **Yes** (`scoring/` & `probe/`) | **Yes** (~548k tok pre-fix; 858k/researcher in Q5) | **8 / 8** | Widest sourcing (88 URLs/36 sites), 100% link resolution, won pairwise package **2/2**. **Named gaps:** post-Opus-checker final claim rate, post-fix readability score, human minutes, whole-study $\text{pass}^3$, and Brier ledger. |
| **Our Repo Default (Arm A)** & **Skill (Arm B)** (`[repo: research-pipeline-hybrid-comparison/README.md]`) | **Yes** | **Yes** | **Yes** (~373k & ~382k tok; ~5–5.5 min) | **7 / 8** (A)<br>**6 / 8** (B) | Arm A had cleanest claims (**94% full support**) without a verifier pass; Arm B won single-report readability (**39 & 37/40**) but had highest claim drift (**74% full support**). |
| [`assafelovic/gpt-researcher`](https://github.com/assafelovic/gpt-researcher) — accessed 2026-11-09 | **Yes** (`evals/` JSON/fixtures) | **Yes** (`SimpleQA` 0.929, `context_filter`, 6-metric eval) | **Yes** (`~$0.40` deep, `$0.096–$0.284` evals) | **7 / 8** | Only probed repo publishing outputs, evals, and costs. Misses `D5` (no default inline abstention/unverified rule). |
| [`Weizhena/Deep-Research-skills`](https://github.com/Weizhena/Deep-Research-skills) — accessed 2026-11-09 | **No** | **No** (schema tests only) | **No** | **6 / 8** | Passes `D1–D6` (outline, item subagents, caps, cross-check, missing-field rules, saved JSONs); zero published outputs or evals (`D7=0, D8=0`). |
| [`stanford-oval/storm`](https://github.com/stanford-oval/storm) — accessed 2026-11-09 | **No** (links to HF `FreshWiki`) | **No** in repo (in NAACL paper) | **No** | **4 / 8** | Passes `D1–D3` and `D6`; no post-draft claim verifier (`D4=0`), no abstention (`D5=0`), no in-repo outputs/costs (`D7=0, D8=0`). |
| [`Alibaba-NLP/DeepResearch`](https://github.com/Alibaba-NLP/DeepResearch) — accessed 2026-11-09 | **No** (`.gitkeep` only) | **Yes** (`benchmark.png`, `Tech_Report.pdf`) | **No** (`D8=0`, cost omitted) | **4 / 8** | Passes `D1–D3` and `D6` (trajectories); fails `D4, D5, D7, D8`. Requires 30B local weights + 5 external APIs. |
| [`dzhng/deep-research`](https://github.com/dzhng/deep-research) — accessed 2026-11-09 | **Yes** (`report.md`, 14.9 KB) | **No** | **No** | **4 / 8** | Minimal recursive TS agent: passes `D1–D3` and `D7` (`report.md`); fails `D4–D6` and `D8`. |

**Inter-Rater Exam Result (`SCORECARD.md` §Inter-Rater Agreement Exam):** A second independent agent blind-scored the 5 probed repositories on Desk items `D1–D8` (40 binary cells) using only the operational rules in [SCORECARD.md](SCORECARD.md) and the raw probe evidence in [sources/b-tradeoffs-and-probe.md](sources/b-tradeoffs-and-probe.md). The two agents achieved **34 / 40 (85.0%) exact cell agreement** (Cohen's $\kappa = 0.70$), passing the proposal's $\ge 80\%$ (`32/40`) success metric (`100%` agreement on `storm` and `dzhng/deep-research`, `87.5%` on `gpt-researcher`, `75.0%` on `Alibaba-NLP/DeepResearch`, and `62.5%` on `Weizhena/Deep-Research-skills` where the probe summary omitted internal skill-file rules).

---

## Confidence and completeness

- **Confidence: High.** All benchmark metrics, human-correlation statistics, and tradeoff figures come from primary papers fetched on 2026-11-09, direct GitHub API inspection of 5 repositories, and 4 internal experimental studies, verified in a separate fact-check pass and a blind 2-agent scoring exam (85.0% agreement).
- **Completeness: ~90%.** All five proposal questions (Q0–Q5), the 5-repo probe, [SCORECARD.md](SCORECARD.md), the 2-agent inter-rater exam, and baseline tables with named gaps are complete. The remaining 10% consists of new runs (post-fix Opus-checked claim rates, human minutes, whole-study $\text{pass}^3$, and automated CI gate scripts) that were out of scope for this study.

## Known gaps

- Whole-pipeline multi-run consistency ($\text{pass}^3$) has only been measured at the single-researcher level (`[repo: research-duplication-and-reuse/README.md]` Q5: $k=2$ runs across 3 tasks), not across full multi-agent + writer + Opus-checker studies.
- Post-fix hybrid `README.md` (with the $\le 3,500$-word cap, answer-first structure, and Opus faithfulness pass) has not yet been re-scored in a blind pairwise judge or post-checker claim spot-check.
- Human effort (minutes spent scoping/reviewing proposals and auditing finished reports) is unmeasured across all internal pipeline runs.
- Calibration error (Brier / ECE) cannot be computed for our method until a claim ledger accumulates resolved predictions across 10+ studies (`[repo: research-quality-metrics/README.md]`).
- Pre-commit deterministic gate scripts (`O1` HTTP 200 check, `O2` citation/diversity check) are specified in [SCORECARD.md](SCORECARD.md) but not yet wired into automated repo CI.

## Self-check

1. When surveying 15 open-source deep-research repositories on GitHub, why can't we rank them by running our report-quality judge (`research-quality-metrics/`) on their published sample reports and dividing by their reported cost per run?
2. Agent X generates a 6,500-word report with 110 inline citations (all returning `HTTP 200` and matching the bibliography) and scores 90% on an LLM judge's Presentation and Groundedness rubrics. Based on measured evidence in this study, name three specific ways Agent X's report can still be badly wrong, and which scorecard metrics catch them.
3. Why does `SCORECARD.md` use binary (`0`/`1`) checklist items for Desk (`D1–D8`) and Coverage (`O4`) instead of 1–5 partial-credit scales, and why do we track $\text{pass}^k$ instead of $\text{pass}@k$?

<details><summary>Answers</summary>

1. In our 5-repo probe, **only 2 of 5 repos published sample long-form reports** in their repository (on different topics), and **only 1 of 5 (`gpt-researcher`) published dollar or token cost figures**. That is why [SCORECARD.md](SCORECARD.md) splits evaluation into **Tier A (Desk-measurable on 100% of repos)**, **Tier B (Output-measurable when sample reports exist)**, and **Tier C (Run-measurable on shared tasks)**.
2. First, **citation breadth trades off against accuracy and hides unsupported claims**: `Gemini DR` averaged 111 citations at 81% accuracy while `gpt-researcher` showed 94% bibliography formatting faithfulness alongside a **53.5% unsupported claim rate**, and holistic LLM judges missed Arm B's 26% claim drift. Second, **up to 57% of RAG citations are post-rationalized** (Wallat et al. 2024). Third, **length and presentation fool judges while recall fails**: in `DRB II`, models scored 75–92% on Presentation while failing more than half of Information Recall (23–40%), and verbose prompts shift naive judge win rates from 22.9% to 64.3% (`AlpacaEval-LC`). Metrics **O3** (sampled claim-entailment check), **O4** (binary recall checklist), and **O6** ($\le 3,500$-word length control) catch these failures.
3. In `ResearchRubrics`, binary (`0`/`1`) grading improved human–LLM judge agreement by **~20 percentage points** over ternary partial-credit grading (0.72–0.76 vs 0.53–0.57 Macro F1), and in `STORM` 1–7 human scales had low inter-rater agreement ($\alpha = 0.221\text{--}0.388$). We track **$\text{pass}^k$** (probability *all $k$* runs succeed, from $\tau$-bench) rather than $\text{pass}@k$ because research tasks have no unit-test verifier at runtime — a user gets one run and needs every run to be reliable.

</details>

## Sources

Detailed extraction tables and the 5-repo probe log are in [sources/a-benchmarks-and-metrics.md](sources/a-benchmarks-and-metrics.md), [sources/b-tradeoffs-and-probe.md](sources/b-tradeoffs-and-probe.md), and [SCORECARD.md](SCORECARD.md).

- [DeepResearch Bench — Du et al. 2025 (arXiv:2506.11763v1)](https://arxiv.org/html/2506.11763v1) — accessed 2026-11-09
- [DeepResearch Bench II — Li et al. 2026 (arXiv:2601.08536v3)](https://arxiv.org/html/2601.08536v3) — accessed 2026-11-09
- [ResearchRubrics — Sharma et al. 2025 (arXiv:2511.07685v1)](https://arxiv.org/html/2511.07685v1) — accessed 2026-11-09
- [DeepScholar-Bench — Patel et al. 2025 (arXiv:2508.20033v2)](https://arxiv.org/html/2508.20033v2) — accessed 2026-11-09
- [Mind2Web 2 — Gou et al. 2025 (arXiv:2506.21506v1)](https://arxiv.org/html/2506.21506v1) — accessed 2026-11-09
- [BrowseComp — Wei et al. 2025 (arXiv:2504.12516v1)](https://arxiv.org/html/2504.12516v1) — accessed 2026-11-09
- [GAIA — Mialon et al. 2023 (arXiv:2311.12983)](https://arxiv.org/abs/2311.12983) — accessed 2026-11-09
- [STORM / FreshWiki — Shao et al. 2024 (arXiv:2402.14207v2)](https://arxiv.org/html/2402.14207v2) — accessed 2026-11-09
- [SAFE & LongFact — Wei et al. 2024 (arXiv:2403.18802v2)](https://arxiv.org/html/2403.18802v2) — accessed 2026-11-09
- [PaperQA2 — Skarlinski et al. 2024 (arXiv:2409.13740v2)](https://arxiv.org/html/2409.13740v2) — accessed 2026-11-09
- [FActScore — Min et al. 2023 (arXiv:2305.14251)](https://ar5iv.labs.arxiv.org/html/2305.14251) — accessed 2026-11-09
- [ALCE — Gao et al. 2023 (arXiv:2305.14627)](https://ar5iv.labs.arxiv.org/html/2305.14627) — accessed 2026-11-09
- [RAGAS — Es et al. 2023 (arXiv:2309.15217)](https://ar5iv.labs.arxiv.org/html/2309.15217) — accessed 2026-11-09
- [Correctness is not Faithfulness in RAG Attributions — Wallat et al. 2024 (arXiv:2412.18004v1)](https://arxiv.org/html/2412.18004v1) — accessed 2026-11-09
- [Length-Controlled AlpacaEval — Dubois et al. 2024 (arXiv:2404.04475v2)](https://arxiv.org/html/2404.04475v2) — accessed 2026-11-09
- [AI Agents That Matter — Kapoor et al. 2024 (arXiv:2407.01502v1)](https://arxiv.org/html/2407.01502v1) — accessed 2026-11-09
- [$\tau$-bench — Yao et al. 2024 (arXiv:2406.12045v1)](https://arxiv.org/html/2406.12045v1) — accessed 2026-11-09
- [How Memory Management Impacts LLM Agents — Xiong et al. 2025 (arXiv:2505.16067v1)](https://arxiv.org/html/2505.16067v1) — accessed 2026-11-09
- [AMSTAR 2 — Shea et al. 2017 (PMC5833365)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5833365/) — accessed 2026-11-09
- [PRISMA 2020 — Page et al. 2021 (PMC8005924)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/) — accessed 2026-11-09
- [Anthropic Engineering — Multi-Agent Research System (2025)](https://www.anthropic.com/engineering/multi-agent-research-system) — accessed 2026-11-09
- [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) — accessed 2026-11-09
- [stanford-oval/storm](https://github.com/stanford-oval/storm) — accessed 2026-11-09
- [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) — accessed 2026-11-09
- [dzhng/deep-research](https://github.com/dzhng/deep-research) — accessed 2026-11-09
- [Weizhena/Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills) — accessed 2026-11-09
- Internal studies (`[repo: ...]`): `[repo: research-quality-metrics/README.md]`, `[repo: research-pipeline-hybrid-comparison/README.md]`, `[repo: research-duplication-and-reuse/README.md]`, `[repo: web-search-methodology/README.md]`

---

## Appendix: Audit of Prior, Disconfirmer, Rival Hypotheses, and Kill Criterion

| Proposal Item (`00-how-to-measure-a-research-method-2026-11-09.md`) | Outcome & Evidence |
|---|---|
| **Riskiest assumption probe:** Take 5 repos of different types and record whether each publishes sample outputs, evaluation numbers, or cost figures ($<2$ of 5 triggers split scorecard). | **Triggered.** Only **2 of 5** commit sample long-form reports (`gpt-researcher`, `dzhng/deep-research`), **2 of 5** publish in-repo eval numbers (`gpt-researcher`, `Alibaba-NLP/DeepResearch`, on incompatible tasks), and **1 of 5** publishes cost figures (`gpt-researcher`). [SCORECARD.md](SCORECARD.md) is split into Tier A (Desk), Tier B (Output), and Tier C (Run). |
| **Prior:** No standard metric exists for a whole research method; scorecard will be small (faithfulness, checklist coverage, tokens, wall time, human time); stars and self-reported benchmarks are weak evidence. | **Confirmed.** All 2025–2026 benchmarks (`DRB I/II`, `ResearchRubrics`, `DeepScholar-Bench`, `Mind2Web 2`) grade single outputs, not whole methods. High-star repos (19k–31k stars) omit cost figures or eval logs, and Kapoor et al. (2024) showed self-reported scores often exceed 5-run reproduction maximums. |
| **Disconfirmer:** A published benchmark for long-form research used by $\ge 3$ independent projects and validated against human ratings. | **Did not fire.** Four benchmarks have human validation, but **0 of the 5 probed repos** use any of them in-repo, and none covers method-level costs, desk architecture, or multi-run consistency. |
| **Rival Hypothesis A:** Human usefulness ratings are the only measure that matters, and automated metrics barely track them. | **Refuted for decomposed binary/entailment metrics; partly supported for holistic 1–7 scales.** Holistic 1–7 human ratings have low inter-rater agreement ($\alpha = 0.221\text{--}0.388$ in `STORM`), and naive LLM judges miss claim drift (`Arm B`). However, binary rubrics achieve **89.6% F1** (`DRB II`) and **95.1%–98.9% node agreement** (`Mind2Web 2`) with humans, `AlpacaEval-LC` reaches **0.98 Spearman**, and `SAFE` beats crowdsourced humans **76% to 19%** on disputes. |
| **Rival Hypothesis B:** Differences between methods are smaller than differences between runs of one method. | **Partly supported for small (<15–20%) differences; refuted for large structural differences.** Identical runs vary by $\pm 22\text{--}26\%$ in tokens (`855k vs 1,334k` in `Q5`), $\pm 4\text{--}8\text{ pp}$ in claim error rate, and 7 points on single-order judge runs (`Arm A`), while $\tau$-bench `gpt-4o` drops from 61% $\text{pass}^1$ to <25% $\text{pass}^8$. Small single-run gaps sit inside noise, whereas large architectural gaps (+90.2% multi-agent gain; 88 vs 40 cited URLs in `Arm C vs Arm B`) exceed run variance. |
| **Kill / pivot criterion:** Stop if no metric covers method-level comparison after ~30 sources. | **Did not fire.** Method-level instruments for Pareto cost-efficiency (`Kapoor et al. 2024`), $\text{pass}^k$ consistency (`Yao et al. 2024`), counterfactual citation faithfulness (`Wallat et al. 2024`), and binary checklist trees (`DRB II`, `ResearchRubrics`, `Mind2Web 2`) extended the scorecard well beyond `research-quality-metrics/`. |
| **Success metric (the exam):** Two fresh agents score the same 5 repos with `SCORECARD.md` alone and agree on $\ge 80\%$ of desk items; scorecard filled in for our hybrid comparison with every gap named. | **Passed (85.0% agreement, 34 / 40 binary cells, $\kappa = 0.70$).** Blind second-scorer test exceeded the 80% (`32/40`) bar (`storm` 8/8, `dzhng/deep-research` 8/8, `gpt-researcher` 7/8, `Alibaba-NLP/DeepResearch` 6/8, `Weizhena/Deep-Research-skills` 5/8), and all 20 metrics (`D1–D8`, `O1–O6`, `R1–R6`) are populated for Arms A, B, C, and Current Hybrid in [SCORECARD.md](SCORECARD.md) with every unmeasured cell marked `GAP`. |

---

## Fact-check

- **Standard & scope:** Checked on 2026-11-09 per `AUTONOMOUS-RESEARCH-STANDARD.md` §3 against [sources/a-benchmarks-and-metrics.md](sources/a-benchmarks-and-metrics.md), [sources/b-tradeoffs-and-probe.md](sources/b-tradeoffs-and-probe.md), and 5 internal repository files (`research-pipeline-hybrid-comparison/README.md` + `scoring/judge_run*.json`, `research-duplication-and-reuse/README.md`, `web-search-methodology/README.md`, `research-quality-metrics/README.md`, `CLAUDE.md`).
- **Claims checked:** **28 claim groups (86 specific numerical values and attributions)** covering all headline figures, the 14 dimensions, the 5-repo probe counts and repo stats, all 7 tradeoffs (`DeepResearch Bench I & II`, `ResearchRubrics`, `DeepScholar-Bench`, `Mind2Web 2`, `BrowseComp`, `GAIA`, `STORM`, `SAFE/LongFact`, `FActScore`, `ALCE`, `RAGAS`, `PaperQA2`, `Wallat et al.`, `AlpacaEval-LC`, `Kapoor et al.`, `$\tau$-bench`, `AMSTAR 2`, `PRISMA 2020`, `Anthropic Multi-Agent`, `gpt-researcher` evals), and all internal baseline numbers.
- **Claims changed:** **0 errors in `README.md`; 3 minor transcription fixes in `SCORECARD.md` (3.5% of 86 checked numbers, 0 headline changes):**
  1. `SCORECARD.md` (`R3` Evidence Strength): Changed `Mind2Web 2: 2.6–13.7 min` to `5.7–13.7 min` (`Perplexity DR` 5.67 min to `HF Open DR` 13.65 min in `sources/a-benchmarks-and-metrics.md` §3.5 Table 3).
  2. `SCORECARD.md` (`O4` Baseline Table): Unswapped 3-way judge Coverage scores for Arm A (`4 & 5/5`, mean 4.5) and Arm B (`4 & 4/5` in 3-way; `4 & 5/5` on pairwise question coverage) per `research-pipeline-hybrid-comparison/scoring/judge_run1.json` and `judge_run2.json`.
  3. `SCORECARD.md` (`O5` Baseline Table): Listed both 3-way (`5 & 4/5`) and pairwise (`4 & 4/5`) Gap Honesty scores for Arm B.
- **Quality guard verdict:** **Passed** (`3.5%` fix rate, well below the `10%` guard threshold; zero headline errors).
