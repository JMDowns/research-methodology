# Source Notes A: Deep-Research Benchmarks, Faithfulness Metrics, and Method Standards (Q0, Q1, Q2)

**Date:** 2026-11-09
**Scope:** Inclusion test and stopping rule (Q0), full list of method-level benefits and costs (Q1), and published benchmarks, faithfulness/attribution metrics, and human systematic-review standards (Q2).

---

## 1. Inclusion Test and Stopping Rule (Q0)

- **Inclusion rule:** A metric or benchmark dimension is included only if it has (a) a written definition and (b) at least one published empirical use or an explicit formula/protocol to compute it.
- **Stopping rule check:** Across 18 primary sources fetched in this study (7 deep-research benchmarks, 6 faithfulness/attribution frameworks, 3 agent cost/reliability/gaming studies, 2 systematic-review appraisal standards) plus 5 probed GitHub repositories and 4 internal repo studies, all candidate dimensions map onto **14 method-level dimensions** grouped into four families: **Output Quality (7)**, **Efficiency & Cost (3)**, **Method Reliability & Reuse (2)**, and **Engineering & Adoption (2)**. The final three sources examined (`tau-bench`, `Wallat et al.`, and `PRISMA 2020`) refined how existing dimensions (repeatability, citation faithfulness, and process transparency) are measured and gamed, without adding a 15th top-level dimension, satisfying the stopping rule ("2 more sources in a row add no new dimension").

---

## 2. Full List of Method-Level Benefits and Costs (Q1)

Earlier work in this repository (`[repo: research-quality-metrics/README.md]`) established seven dimensions for grading **one finished report** (accuracy/groundedness, coverage, source quality/diversity, calibration, reproducibility/traceability, relevance-to-question, honesty about gaps). However, grading a **research method** requires evaluating the *process generator* across multiple tasks, runs, and budgets.

Combining systematic review methodology ([AMSTAR 2, Shea et al. 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5833365/) — accessed 2026-11-09; [PRISMA 2020, Page et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/) — accessed 2026-11-09), cost-aware agent evaluation ([AI Agents That Matter, Kapoor et al. 2024](https://arxiv.org/html/2407.01502v1) — accessed 2026-11-09), multi-trial reliability ([$\tau$-bench, Yao et al. 2024](https://arxiv.org/html/2406.12045v1) — accessed 2026-11-09), and deep-research benchmarks ([DeepResearch Bench, Du et al. 2025](https://arxiv.org/html/2506.11763v1) — accessed 2026-11-09; [DeepResearch Bench II, Li et al. 2026](https://arxiv.org/html/2601.08536v3) — accessed 2026-11-09; [ResearchRubrics, Sharma et al. 2025](https://arxiv.org/html/2511.07685v1) — accessed 2026-11-09; [DeepScholar-Bench, Patel et al. 2025](https://arxiv.org/html/2508.20033v2) — accessed 2026-11-09; [Mind2Web 2, Gou et al. 2025](https://arxiv.org/html/2506.21506v1) — accessed 2026-11-09), a research method's benefits and costs decompose into **14 dimensions across 4 families**:

| Family | # | Dimension | What a method can be good or bad at | Report-level vs Method-level |
|---|---|---|---|---|
| **A. Output Quality** (covered in `research-quality-metrics/`, extended with 2025–2026 DRA benchmarks) | 1 | **Factual accuracy (world truth)** | Producing statements that are objectively true in the external world, not merely consistent with a bad source ([SAFE/LongFact, Wei et al. 2024](https://arxiv.org/html/2403.18802v2) — accessed 2026-11-09; [BrowseComp, Wei et al. 2025](https://arxiv.org/html/2504.12516v1) — accessed 2026-11-09). | Report metric aggregated over a task suite |
| | 2 | **Citation faithfulness & attribution** | Ensuring every claim is entailed by its cited source (*correctness/recall*), every citation is load-bearing (*precision*), and citations reflect actual causal use rather than post-rationalization ([ALCE, Gao et al. 2023](https://ar5iv.labs.arxiv.org/html/2305.14627) — accessed 2026-11-09; [Wallat et al. 2024](https://arxiv.org/html/2412.18004v1) — accessed 2026-11-09). | Report metric + pipeline verification architecture |
| | 3 | **Coverage & information recall** | Finding all vital sub-questions, perspectives, and counter-evidence without omitting critical facts ([DeepResearch Bench II, Li et al. 2026](https://arxiv.org/html/2601.08536v3) — accessed 2026-11-09; [STORM, Shao et al. 2024](https://arxiv.org/html/2402.14207v2) — accessed 2026-11-09). | Report metric driven by search breadth/depth |
| | 4 | **Source quality, diversity & independence** | Retrieving primary, authoritative, high-impact, and independent domains rather than single-domain monocultures or secondary mirrors ([DeepScholar-Bench, Patel et al. 2025](https://arxiv.org/html/2508.20033v2) — accessed 2026-11-09; [GPT-Researcher evals](https://github.com/assafelovic/gpt-researcher/blob/main/evals/README.md) — accessed 2026-11-09). | Report metric + retrieval filter design |
| | 5 | **Calibration & gap honesty** | Matching stated confidence to actual accuracy, abstaining when evidence is insufficient, and surfacing contradictions/unverified claims ([BrowseComp, Wei et al. 2025](https://arxiv.org/html/2504.12516v1) — accessed 2026-11-09; [PaperQA2, Skarlinski et al. 2024](https://arxiv.org/html/2409.13740v2) — accessed 2026-11-09). | Method-level over a corpus of predictions |
| | 6 | **Analytical depth & decision usefulness (actionability)** | Going beyond source summaries to synthesize non-obvious insights, resolve implicit constraints, and provide artefacts a practitioner can act on ([ResearchRubrics, Sharma et al. 2025](https://arxiv.org/html/2511.07685v1) — accessed 2026-11-09; `[repo: research-pipeline-hybrid-comparison/README.md]`). | Report metric + output schema design |
| | 7 | **Readability & organization** | Clear structure, appropriate length, and low cognitive load for human readers ([DeepResearch Bench II, Li et al. 2026](https://arxiv.org/html/2601.08536v3) — accessed 2026-11-09; [STORM, Shao et al. 2024](https://arxiv.org/html/2402.14207v2) — accessed 2026-11-09). | Report metric |
| **B. Efficiency & Cost** | 8 | **Token & dollar cost** | Total input/output/cached tokens, search/scraping API spend, and tool calls required per completed study ([AI Agents That Matter, Kapoor et al. 2024](https://arxiv.org/html/2407.01502v1) — accessed 2026-11-09; [Anthropic Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system) — accessed 2026-11-09). | **Method-level** (Pareto frontier with quality) |
| | 9 | **Wall-clock latency** | End-to-end elapsed time from prompt to finished report ([Mind2Web 2, Gou et al. 2025](https://arxiv.org/html/2506.21506v1) — accessed 2026-11-09; [PaperQA2, Skarlinski et al. 2024](https://arxiv.org/html/2409.13740v2) — accessed 2026-11-09). | **Method-level** |
| | 10 | **Human effort (in-the-loop & verification time)** | Human minutes required before/during execution (scoping, outline approval) and after execution (reading verbosity, checking citations) ([Mind2Web 2, Gou et al. 2025](https://arxiv.org/html/2506.21506v1) — accessed 2026-11-09; `[repo: research-duplication-and-reuse/README.md]`). | **Method-level** |
| **C. Reliability & Reuse** | 11 | **Repeatability (run-to-run variance)** | Consistency of success rate, claim accuracy, and cost across $k$ independent trials on the same query ([$\tau$-bench, Yao et al. 2024](https://arxiv.org/html/2406.12045v1) — accessed 2026-11-09; [BrowseComp, Wei et al. 2025](https://arxiv.org/html/2504.12516v1) — accessed 2026-11-09). | **Method-level** |
| | 12 | **Reuse & cumulative memory** | Ability to detect prior work at scoping time, share method components, or reuse verified findings across studies without propagating errors (`[repo: research-duplication-and-reuse/README.md]`). | **Method-level** |
| **D. Engineering & Adoption** | 13 | **Failure behaviour & budget bounding** | Graceful degradation under dead ends, rate limits, paywalls, or unanswerable queries; explicit turn/token caps; abstention vs fabrication ([PaperQA2, Skarlinski et al. 2024](https://arxiv.org/html/2409.13740v2) — accessed 2026-11-09; [Anthropic Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system) — accessed 2026-11-09). | **Method-level** (desk + run) |
| | 14 | **Ease of adoption & auditability** | Dependency footprint (API keys, custom sandboxes, local weights), model-agnosticism, and whether intermediate search/source traces are saved for audit ([PRISMA 2020, Page et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/) — accessed 2026-11-09; 5-repo probe in `sources/b-tradeoffs-and-probe.md`). | **Method-level** (desk-measurable) |

---

## 3. Published Deep-Research Benchmarks (Q2)

### 3.1 DeepResearch Bench (DRB I) — Du et al., June 2025
- **Source:** [DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents (arXiv:2506.11763v1)](https://arxiv.org/html/2506.11763v1) — accessed 2026-11-09; code at `https://github.com/Ayanami0730/deep_research_bench`.
- **What it tests:** 100 PhD-level open-ended research tasks across 22 distinct domains (50 English, 50 Chinese), filtered from 44,019 real user queries.
- **How it is computed:** Two automated frameworks:
  1. **RACE (Reference-based Adaptive Criteria-driven Evaluation with Dynamic Weighting):** An LLM judge dynamically generates task-specific criteria and weights across 4 dimensions — **Comprehensiveness (Comp.)**, **Insight/Depth (Depth)**, **Instruction-Following (Inst.)**, and **Readability (Read.)** — and scores the target report relative to a high-quality reference report $R_{\text{ref}}$ (because isolated scoring yields uniformly high, non-discriminative scores).
  2. **FACT (Factual Abundance and Citation Trustworthiness):** Extracts and deduplicates `(statement, URL)` pairs from the report, scrapes the cited URLs, uses an LLM judge to test whether the web page supports the statement, and computes two metrics: **Citation Accuracy (`C. Acc.`, %)** and **Average Effective Citations per Task (`E. Cit.`)**.
- **Human validation:** Validated on 50 Chinese tasks × 4 agents scored by 70+ domain experts with Master's degrees (3 annotators per task). After filtering to 37 tasks with non-negative Intraclass Correlation Coefficient ($\text{ICC} \ge 0$), **RACE (Full)** achieved **71.33% Pairwise Agreement Rate (PAR)** with humans — higher than **Human Inter-Agreement (68.44%)** — along with **99.54% Overall Pearson Correlation (OPC)**, **60.24% Filtered Average Pearson (FAP)**, and **59.12% Filtered Average Spearman (FAS)**. Removing the reference report (`- No Reference`) dropped PAR to 66.56% and FAS to 51.23%; a vanilla prompt achieved only 58.89% PAR, 40.30% FAP, and 43.75% FAS.
- **Key published numbers (Table 1):**
  - `Gemini-2.5-Pro Deep Research`: RACE Overall **48.88** (Comp. 48.53, Depth 48.50, Inst. 49.18, Read. 49.44); FACT `C. Acc.` **81.44%**, `E. Cit.` **111.21**.
  - `OpenAI Deep Research`: RACE Overall **46.98** (Comp. 46.87, Depth 45.25, Inst. 49.27, Read. 47.14); FACT `C. Acc.` **77.96%**, `E. Cit.` **40.79**.
  - `Perplexity Deep Research`: RACE Overall **42.25** (Comp. 40.69, Depth 39.39, Inst. 46.40, Read. 44.28); FACT `C. Acc.` **90.24%**, `E. Cit.` **31.26**.
  - `Grok Deeper Search`: RACE Overall **40.24**; FACT `C. Acc.` **83.59%**, `E. Cit.` **8.15**.
  - `Claude-3.7-Sonnet w/Search`: RACE Overall **40.67**; FACT `C. Acc.` **93.68%**, `E. Cit.` **32.48**.
  - `Perplexity-Sonar-Reasoning-Pro(high)`: RACE Overall **40.22**; FACT `C. Acc.` **39.36%**, `E. Cit.` **8.35**.

### 3.2 DeepResearch Bench II (DRB II) — Li et al., January 2026
- **Source:** [DeepResearch Bench II: Diagnosing Deep Research Agents via Rubrics from Expert Reports (arXiv:2601.08536v3)](https://arxiv.org/html/2601.08536v3) — accessed 2026-11-09.
- **Why it replaced DRB I's dynamic criteria:** The same research group noted that LLM-defined coarse criteria in prior benchmarks are hard to verify and can diverge from human expert judgment. DRB II grounds evaluation in **132 expert-written investigative articles** across 22 domains (66 English, 66 Chinese), constructing **9,430 fine-grained binary rubrics** (~71 binary items per task) through a 4-stage pipeline (LLM extraction, self-evaluation filtering, manual revision, domain-expert review) across three dimensions: **Information Recall**, **Analysis**, and **Presentation**.
- **How it is computed & cost:** Evaluates rubrics in batches of 50 using `Gemini-2.5-Pro` as the judge at an average evaluation cost of **$0.2513 per task** (Table 4).
- **Human validation:** On 10 multi-format reports labeled by humans, `Gemini-2.5-Pro` at batch size 50 achieved **91.75% accuracy and 89.57% F1** against human labels (outperforming `Gemini-2.5-Flash` at 89.45% ACC / 79.79% F1 and `GPT-5` at 88.36% ACC / 78.28% F1, Table 5).
- **Key published numbers (Table 3):**
  - `OpenAI-GPT-o3 Deep Research`: Total **45.40%** (InfoRecall **39.98%**, Analysis **49.85%**, Presentation **89.16%**).
  - `Gemini-3-Pro Deep Research`: Total **44.60%** (InfoRecall **39.09%**, Analysis **48.94%**, Presentation **91.85%**).
  - `Gemini-2.5-Pro Deep Research`: Total **41.98%** (InfoRecall **34.91%**, Analysis **51.91%**, Presentation **90.24%**).
  - `Doubao Deep Research`: Total **40.99%** (InfoRecall 34.83%, Analysis 49.43%, Presentation 83.51%).
  - `Qwen3-Max Deep Research`: Total **39.25%** (InfoRecall 34.18%, Analysis 48.04%, Presentation 74.59%).
  - `Grok Deep Search`: Total **39.23%** (InfoRecall 33.52%, Analysis 42.50%, Presentation **91.42%**).
  - `Perplexity Research`: Total **38.58%** (InfoRecall 33.05%, Analysis 44.47%, Presentation 79.34%).
  - `Tongyi Deep Research`: Total **29.89%** (InfoRecall **22.95%**, Analysis **35.89%**, Presentation **86.13%**).
  - **Diagnostic takeaway:** Every evaluated agent scores high on **Presentation (74.59%–91.85%)**, yet even the best agent fails more than half of the rubrics overall (**45.40%**), with severe deficits in **Information Recall (22.95%–39.98%)** and **Analysis (35.89%–51.91%)**.

### 3.3 ResearchRubrics — Sharma et al. (Scale AI), November 2025
- **Source:** [ResearchRubrics: A Benchmark of Prompts and Rubrics For Evaluating Deep Research Agents (arXiv:2511.07685v1)](https://arxiv.org/html/2511.07685v1) — accessed 2026-11-09.
- **What it tests:** 101 realistic single-turn deep-research prompts across 9 domains (AI & ML, Business Planning, Historical Analysis, STEM, etc.), paired with **2,593 expert-written fine-grained rubric criteria** (20–43 criteria per prompt, divided into mandatory and optional criteria), built with **2,800+ hours of human labor**. Tasks are stratified along three complexity axes: *Conceptual Breadth*, *Logical Nesting*, and *Exploration*.
- **How it is computed:** LLM-as-a-judge grades each criterion under binary (`Pass`/`Fail`) or ternary (`Pass`/`Partial`/`Fail`) compliance.
- **Human validation & rubric design ablations (Tables 6–7):**
  - Binary grading achieves **0.717–0.760 Macro F1** alignment with human annotators across `GPT-5`, `Claude-4.5`, and `Gemini-2.5-Pro` judges (with `Gemini-2.5-Pro` reaching **0.760** on Gemini DR outputs, exceeding HealthBench's 0.709 Macro F1).
  - Shifting from binary to ternary grading (partial credit) **drops human-LLM agreement by ~20 percentage points** (down to **0.527–0.567 Macro F1**), showing that partial credit introduces rubric ambiguity without improving discriminative power.
  - Adding brief concrete inline examples to rubric criteria improves human-LLM alignment by **3–4% (binary)** and **2–3% (ternary)**, whereas **automated LLM rubric augmentation (prompting an LLM to expand/elaborate criteria) catastrophically degrades human-LLM alignment by 15–20%**.
- **Key published numbers:** State-of-the-art DR agents (`Gemini DR`, `OpenAI DR`, `Perplexity DR`) achieve **under 68% average compliance**, failing primarily on implicit context and reasoning over retrieved evidence.

### 3.4 DeepScholar-Bench — Patel et al. (UC Berkeley Sky Lab), August 2025
- **Source:** [DeepScholar-Bench: A Live Benchmark and Automated Evaluation for Generative Research Synthesis (arXiv:2508.20033v2)](https://arxiv.org/html/2508.20033v2) — accessed 2026-11-09.
- **What it tests:** Live academic literature synthesis: given a recent arXiv paper's title and abstract, retrieve prior literature (filtering out papers published on or after the query paper's date to prevent contamination) and generate a cohesive, cited **"Related Work" section**.
- **How it is computed:** Evaluates against the human-written Related Work section and its bibliography across **3 pillars (7 automated metrics)**, summarized by their unweighted **Geometric Mean**:
  1. **Knowledge Synthesis:**
     - *Organization (`Org.`):* Pairwise LLM judge comparing structural coherence against the human exemplar (0–1 win rate).
     - *Nugget Coverage (`Nug. Cov.`):* LLM extracts atomic facts ("nuggets") from the human Related Work, labels them `Vital` or `Okay`, and computes the fraction of vital nuggets covered in the generated report.
  2. **Retrieval Quality:**
     - *Relevance Rate (`Rel. Rate`):* Fraction of retrieved/cited papers relevant to the query topic.
     - *Reference Coverage (`Ref. Cov.`):* Recall of important references cited in the human Related Work section.
     - *Document Importance (`Doc. Imp.`):* Citation velocity (citations per year via OpenAlex) of cited papers relative to human exemplars.
  3. **Verifiability (ALCE-adapted):**
     - *Citation Precision (`Cite-P`):* Fraction of cited sources that entail their accompanying claim.
     - *Claim Coverage (`Claim Cov.`):* Fraction of claims fully supported by their cited sources.
- **Human validation (Table 4):** Validated with 11 CS PhD students across 4 North American universities (>300 annotations). Automated LLM judges achieved **71.43% agreement** with the human majority vote on pairwise Organization, **83.33% agreement** on Nugget Importance (`Vital` vs `Okay`), and **65.9% agreement** on Reference Importance.
- **Key published numbers (`DeepScholar-June-2025`, Table 2):**
  - `Human-written Exemplars`: Geo. Mean **0.782** (`Org.` 0.500, `Nug. Cov.` 1.000, `Rel. Rate` 0.585, `Ref. Cov.` 1.000, `Doc. Imp.` 1.000, manual `Cite-P` ~0.900, `Claim Cov.` ~0.850).
  - `OpenAI DeepResearch`: Geo. Mean **0.309** (`Org.` **0.857**, `Nug. Cov.` **0.392**, `Rel. Rate` **0.629**, `Ref. Cov.` **0.187**, `Doc. Imp.` **0.124**, `Cite-P` **0.399**, `Claim Cov.` **0.138**).
  - `Search Agent (o3)`: Geo. Mean **0.287** (`Org.` 0.849, `Nug. Cov.` 0.348, `Cite-P` 0.425, `Claim Cov.` 0.495).
  - `DeepScholar-ref (GPT-4.1, Claude)`: Geo. Mean **0.286** (`Org.` 0.698, `Nug. Cov.` 0.307, `Cite-P` **0.944**, `Claim Cov.` **0.895**).
  - `STORM (Llama-4)`: Geo. Mean **0.073** (`Org.` 0.119, `Nug. Cov.` 0.183, `Ref. Cov.` 0.003, `Cite-P` 0.238, `Claim Cov.` 0.586).

### 3.5 Mind2Web 2 — Gou et al. (OSU NLP Group & Amazon AGI), June 2025
- **Source:** [Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge (arXiv:2506.21506v1)](https://arxiv.org/html/2506.21506v1) — accessed 2026-11-09.
- **What it tests:** 130 realistic, long-horizon, time-varying agentic search tasks across 6 broad domains and 24 sub-domains, built with **1,000+ hours of human labor**. On Subset-30, human annotators averaged **18 minutes** (min 8, max 44), visiting **8 websites** and **110 webpages** per task (Table 2).
- **How it is computed (Agent-as-a-Judge):** Each task has a custom Python judge-agent script implementing a **tree-structured rubric** (average **34 leaf nodes**, **50 total nodes**, depth 4; max 357 leaf nodes). The judge agent scrapes/caches cited URLs in real time and evaluates every leaf node binary check across two axes: **Correctness** (satisfies task constraints, with critical gates that zero out parent nodes if violated) and **Attribution** (whether the cited URL actually supports the extracted claim). Reports **Partial Completion** (0–1 average across root rubric nodes) and **Full-Task Success Rate** (all critical nodes passed, score = 1).
- **Human validation (Section 4.4):** On 15 randomly sampled tasks (30 agent answers, **720 leaf-node binary verifications**), an independent human verifier agreed with the judge agent on **685 of 720 nodes (95.14%)**, and audit of the 35 discrepancies showed 27 were human evaluator errors (the judge agent was correct on **712 of 720 nodes, 98.89%**).
- **Key published numbers (Table 3):**
  - `Human (Subset-30)`: Partial Completion **0.79 ± 0.01**, Success Rate **54% ± 7%**, Pass@3 **0.83**, Time **18.40 ± 1.61 min**, Answer Length **186 ± 27 words**.
  - `OpenAI Deep Research`: Partial Completion **0.54 ± 0.04**, Success Rate **28% ± 4%**, Pass@3 **0.40**, Time **8.40 ± 0.71 min**, Answer Length **559 ± 19 words**.
  - `Grok DeeperSearch`: Partial Completion **0.52 ± 0.02**, Success Rate **27% ± 3%**, Pass@3 **0.40**, Time **5.72 ± 0.27 min**, Answer Length **1,362 ± 24 words**.
  - `Gemini Deep Research`: Partial Completion **0.45 ± 0.03**, Success Rate **18% ± 2%**, Pass@3 **0.30**, Time **7.38 ± 0.58 min**, Answer Length **3,357 ± 49 words**.
  - `Perplexity Deep Research`: Partial Completion **0.42 ± 0.03**, Success Rate **15% ± 3%**, Pass@3 **0.26**, Time **5.67 ± 0.13 min**, Answer Length **585 ± 13 words**.
  - `HF Open Deep Research`: Partial Completion **0.26 ± 0.01**, Success Rate **11% ± 1%**, Pass@3 **0.18**, Time **13.65 ± 0.07 min**, Answer Length **209 ± 3 words**.
  - `ChatGPT Search`: Partial Completion **0.26 ± 0.01**, Success Rate **6% ± 1%**, Time **<1 min**, Answer Length **314 ± 4 words**.

### 3.6 BrowseComp & GAIA — Short-Answer Multi-Hop Browsing Benchmarks
- **BrowseComp** ([BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents, Wei et al. 2025 (arXiv:2504.12516v1)](https://arxiv.org/html/2504.12516v1) — accessed 2026-11-09; hosted in `https://github.com/openai/simple-evals`):
  - **What it tests:** 1,266 hard-to-find, multi-hop web browsing questions created by human trainers such that another person could not solve them within 10 minutes and five simple Google searches did not surface the answer on page 1. Human trainers given up to 2 hours gave up on **70.8% (888/1,255)** and solved **29.2% (367/1,255)** (Table 2).
  - **How it is computed:** Short, self-contained predicted answers + stated confidence (0–100%), graded binary `CORRECT`/`INCORRECT` against reference answers by an LLM grader, plus **Calibration Error (%)**.
  - **Key published numbers (Table 3):** `GPT-4o` **0.6%** accuracy (69% calibration error); `GPT-4o w/ browsing` **1.9%** accuracy (82% calibration error); `GPT-4.5` **0.9%** (68% calibration error); `OpenAI o1` **9.9%** (65% calibration error); `OpenAI Deep Research` **51.5%** accuracy (**91% calibration error**).
- **GAIA** ([GAIA: a benchmark for General AI Assistants, Mialon et al. 2023 (arXiv:2311.12983v1)](https://arxiv.org/abs/2311.12983) — accessed 2026-11-09):
  - **What it tests:** 466 real-world assistant questions (Levels 1–3) requiring web browsing, multi-modality, and tool use, with unambiguous short ground-truth answers (exact match). Humans score **92%** vs **15%** for early `GPT-4` with plugins.
- **Fit to long-form research:** Both BrowseComp and GAIA test *needle-in-a-haystack multi-hop retrieval* with short exact answers. They are easy and cheap to grade, but they **do not measure synthesis, coverage of competing hypotheses, citation faithfulness in prose, or report usability**.

### 3.7 FreshWiki / STORM — Shao et al. (Stanford OVAL), February 2024
- **Source:** [Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models (arXiv:2402.14207v2)](https://arxiv.org/html/2402.14207v2) — accessed 2026-11-09.
- **What it tests:** Generating full-length, cited Wikipedia-like articles from scratch on 100 recent high-quality Wikipedia topics (`FreshWiki`).
- **Metrics & Human Validation:**
  - *Outline stage:* **Heading Soft Recall** (Sentence-BERT cosine similarity against human Wikipedia headings) and **Heading Entity Recall** (FLAIR NER entity recall).
  - *Article stage:* **ROUGE-1 (45.82)**, **ROUGE-L (16.70)**, **Article Entity Recall (14.10%)**, **Prometheus-13B 1–5 rubric grading** (Interest Level, Organization, Relevance, Coverage), and **Mistral-7B-Instruct NLI Citation Recall (84.83%) / Citation Precision (85.18%)** (Tables 2, 4).
  - *Human validation (Table 6):* 10 experienced Wikipedia editors (>500 edits) rated 20 paired articles (`STORM` vs `oRAG`) on a 1–7 scale. Editors preferred `STORM` 26 to 14 and rated Organization significantly higher (4.00 vs 3.25, $p=0.005$), **but inter-annotator agreement (Krippendorff's $\alpha$) across the five 1–7 dimensions was low: 0.221 (Organization), 0.256 (Relevance), 0.346 (Coverage), 0.349 (Interest Level), and 0.388 (Verifiability)**. Moreover, `STORM` showed no human-ratedVerifiability gain over `oRAG` (3.80 vs 3.85, $p=0.843$).

---

## 4. Faithfulness, Factuality, and Attribution Metrics (Q2)

*(Note: `FActScore`, `ALCE`, and `RAGAS` were summarized in `[repo: research-quality-metrics/README.md]`; per R3 rules, their primary arXiv sources were re-fetched and verified on 2026-11-09 alongside the new frameworks `SAFE/LongFact`, `PaperQA2`, and `Wallat et al.`)*

| Metric / Framework | Primary Source | What It Measures | How Computed | Human Validation & Cost | Critical Limitation / Gaming Risk |
|---|---|---|---|---|---|
| **FActScore** | [Min et al. 2023 (arXiv:2305.14251)](https://ar5iv.labs.arxiv.org/html/2305.14251) — accessed 2026-11-09 | **Atomic factual precision** against a fixed reference knowledge source (e.g., Wikipedia). | Decomposes generation into atomic facts; checks if each is supported by the reference source. | **<2% error** vs human judgment (`[repo: research-quality-metrics/README.md]`); human annotation costs **$4.00/response** ([Wei et al. 2024](https://arxiv.org/html/2403.18802v2) — accessed 2026-11-09). Commercially available LMs scored 42% (InstructGPT), 58% (ChatGPT), 71% (PerplexityAI), dropping from 80% to 16% on rare entities. | Assumes a single static reference corpus (fails when facts sit on the open web); measures precision only, so an agent can game it by outputting 2 ultra-safe generic sentences. |
| **SAFE + LongFact** | [Wei et al. 2024, Google DeepMind (arXiv:2403.18802v2)](https://arxiv.org/html/2403.18802v2) — accessed 2026-11-09 | **Open-web long-form factuality** (Precision, Recall@$K$, and $\text{F1}@K$ over 2,280 prompts in 38 topics). | LLM agent decomposes response into atomic facts, revises pronouns into self-contained claims, issues multi-step Google Search queries (via Serper), and classifies each fact as `Supported`, `Not Supported`, or `Irrelevant`. Combines precision $P$ with recall $R_K = \min(S/K, 1)$ relative to preferred length $K$ into $\text{F1}@K = \frac{2 P R_K}{P + R_K}$. | On **16,011 atomic facts**, SAFE agreed with crowdsourced humans **72.0%** of the time (11,528/16,011). On 100 sampled disagreement cases audited with full internet access, **SAFE was right 76% of the time vs 19% for humans** (4:1 win ratio). Costs **$0.19/response** ($64.57 GPT-3.5-Turbo + $31.74 Serper over 496 responses) vs **$4.00/response** for humans (>20× cheaper). | Checks whether *Google Search* supports the claim, **not** whether the *report's own cited URL* supports it. Can be gamed by stating widely repeated web myths or padding with trivial true facts to hit $K$. |
| **ALCE** | [Gao et al. 2023 (arXiv:2305.14627)](https://ar5iv.labs.arxiv.org/html/2305.14627) — accessed 2026-11-09 | **Citation Recall** (do cited passages entail the sentence?) and **Citation Precision** (is every citation in the bracket necessary/load-bearing?). | Runs NLI (`TRUE` / T5-11B) over concatenated cited passages vs sentence (Recall), and leave-one-out ablation per citation (Precision). | Human agreement **Cohen's $\kappa = 0.698$** (recall) and **$\kappa = 0.525$** (precision); automatic accuracy **85.1%** (recall) and **77.6%** (precision) against human gold labels. | Evaluates sentence-level NLI against retrieved snippets; does not check whether the cited source itself is authoritative or whether the model post-rationalized the citation. |
| **RAGAS** | [Es et al. 2023 (arXiv:2309.15217)](https://ar5iv.labs.arxiv.org/html/2309.15217) — accessed 2026-11-09 | **Reference-free RAG triad:** Faithfulness (supported claims / total claims), Answer Relevance (cosine similarity of reverse-generated questions to prompt), Context Relevance (extracted relevant sentences / total context sentences). | LLM extracts statements from answer and verifies each against retrieved context (`Faithfulness`); embeds reverse-generated questions (`Answer Relevance`). | On `WikiEval` (50 post-2022 Wikipedia pages, 90–95% inter-annotator agreement), pairwise accuracy with humans is **0.95 (Faithfulness)**, **0.78 (Answer Relevance)**, and **0.70 (Context Relevance)**, beating direct GPT Score (0.72 / 0.52 / 0.63) and GPT Ranking (0.54 / 0.40 / 0.52) (Table 1). | Reference-free: cannot detect *missing* perspectives that were never retrieved in context (`Context Recall` requires ground truth). |
| **PaperQA2 (LitQA2, WikiCrow, ContraCrow)** | [Skarlinski et al. 2024, FutureHouse (arXiv:2409.13740v2)](https://arxiv.org/html/2409.13740v2) — accessed 2026-11-09 | **Scientific retrieval precision/accuracy + DOI attribution** (`LitQA2`), **cited statement support** (`WikiCrow`), and **literature contradiction rate** (`ContraCrow`). | Parses full PDFs with GROBID, summarizes/reranks chunks with metadata (`RCS`), traverses citation graphs, and grades claims on an 11-point contradiction Likert scale. | On `LitQA2` (248 questions), PaperQA2 achieved **85.2% ± 1.1% precision** and **66.0% ± 1.2% accuracy** (abstaining 21.9%), beating incentivized Biology PhDs (**73.8% ± 9.6% precision**, $p=0.0036$; **67.7% ± 11.9% accuracy**). On `WikiCrow` (375 blinded statements across 240 gene articles, costing **$4.48 ± $1.02** and **491.5 ± 324.0s** per 1,219-word article), human experts found **86.1% citation precision vs 71.2% for Wikipedia** ($p=0.0013$), and **13.5% vs 24.9% cited-and-unsupported statements** ($p=0.0075$). On `ContraCrow` (100 flagged claims across 93 biology papers), experts validated **70%** (**F1 = 0.82**, $p=10^{-4}$), finding **1.64 validated contradictions per paper**. | High compute/API cost ($4.48/article, ~8.2 min); requires full-text PDF access. |
| **Counterfactual Citation Faithfulness** | [Wallat et al. 2024 (arXiv:2412.18004v1)](https://arxiv.org/html/2412.18004v1) — accessed 2026-11-09 | Disentangles **Citation Correctness** (does the cited passage support the claim?) from **Citation Faithfulness** (did the model *causally rely* on that passage, vs post-rationalizing from parametric memory?). | Injects adversarial/forged documents into the RAG context: (a) random docs, (b) relevant but previously uncited docs, (c) docs cited for a different claim. | Models cited random documents in **12% (116/936)** of cases, but post-rationalized citations to relevant-uncited documents in **57%** of cases and documents cited for other reasons in **55%** of cases. | Shows that static NLI checks (like ALCE/FACT) only measure *citation correctness*, not *causal faithfulness* — up to **57% of "correct-looking" citations are post-rationalized**. |

---

## 5. Method-Level Appraisal, Reliability, and Cost Standards (Q1, Q2)

### 5.1 Human Research Standards: PRISMA 2020 vs AMSTAR 2
- **PRISMA 2020** ([Page et al. 2021, BMJ 372:n71 / PMC8005924](https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/) — accessed 2026-11-09) is a **27-item reporting guideline** (plus flow diagram) specifying what a systematic review must *disclose* so a reader can audit and reproduce it: explicit eligibility criteria, full search strategy for each database, selection process, data collection process, risk-of-bias assessment, effect measures, synthesis methods, certainty assessment, and competing interests.
- **AMSTAR 2** ([Shea et al. 2017, BMJ 358:j4008 / PMC5833365](https://pmc.ncbi.nlm.nih.gov/articles/PMC5833365/) — accessed 2026-11-09) is a **16-item methodological appraisal tool** with **7 critical domains** (protocol registered before commencement, adequacy of literature search, justification for excluding individual studies, risk of bias from individual studies, appropriateness of meta-analytical methods, consideration of risk of bias when interpreting results, assessment of presence and likely impact of publication bias).
- **Why both matter for AI research methods:** AMSTAR 2 explicitly warns: *"The quality of reporting of a systematic review may, however, more accurately reflect authors' ability to write in a comprehensible manner rather than the way they conducted their review."* AMSTAR 2 refuses to average its 16 items into a composite score; instead, **1 critical flaw caps confidence at Low, and >1 critical flaw caps it at Critically Low**. For AI research repos, PRISMA maps to **audit trail completeness** (does the method save queries, fetched URLs, and intermediate notes?), while AMSTAR 2 maps to **multiplicative critical gates** (a polished report with hallucinated links or unverified claims fails the gate regardless of readability).

### 5.2 Multi-Trial Agent Consistency: $\tau$-bench's $\text{pass}^k$
- **Source:** [$\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains, Yao et al. 2024 (arXiv:2406.12045v1)](https://arxiv.org/html/2406.12045v1) — accessed 2026-11-09.
- **Definition:** Whereas code-generation benchmarks use $\text{pass}@k$ (the probability that *at least 1* of $k$ i.i.d. trials succeeds — which rewards high-variance guessing when a unit-test verifier exists), research agents have no automatic ground-truth verifier at runtime. A user gets *one* run and needs every run to be reliable. $\tau$-bench defines **$\text{pass}^k$** (pass-hat-$k$) as the probability that **all $k$ i.i.d. trials succeed on the same task**: given $N$ total trials on a task with $c$ successes, $\text{pass}^k = \binom{c}{k} / \binom{N}{k}$ (or approx $p^k$).
- **Key empirical result:** Even the best `gpt-4o` function-calling agent, which achieved **>60% ($\sim 61\%$) single-run success ($\text{pass}^1$)** on $\tau$-retail, dropped to **<25% ($\text{pass}^8$)** over 8 trials (and from ~35% $\text{pass}^1$ on $\tau$-airline down toward near-zero consistency).

### 5.3 Cost-Controlled Agent Evaluation & Reproducibility: Kapoor et al. ("AI Agents That Matter")
- **Source:** [AI Agents That Matter, Kapoor et al. 2024 (arXiv:2407.01502v1)](https://arxiv.org/html/2407.01502v1) — accessed 2026-11-09.
- **Core findings:**
  1. **Accuracy-only leaderboards incentivize unbounded cost:** Without cost controls, complex agent architectures (reflexion, tree search, multi-agent retry loops) burn 50×–100× more inference dollars than simple baselines (such as zero-shot or temperature-0/warming retry) to achieve similar or lower accuracy on benchmarks like HumanEval and HotPotQA.
  2. **Non-determinism even at temperature 0:** LLM APIs are not deterministic even at `temperature=0` (Section 2.2 / A.1), so simply retrying a zero-shot model up to 5 times beats complex agent scaffolding at a fraction of the cost.
  3. **Reproducibility failures across agent papers:** Single evaluation runs can cost >$100, so agent papers rarely report error bars across multiple runs. When Kapoor et al. ran 5 reproduction trials per agent, they found *"many reported accuracy scores were above the maximum of five runs that we performed in our reproduction attempts, and the reported baselines were in some cases lower than the minimum of our five runs"* (Section 2.2), and documented pervasive standardization/reproducibility flaws in Table A6.
  4. **Prescription:** Every method comparison must plot **Quality vs Inference Cost (USD / tokens) as a 2D Pareto curve** with multi-run confidence intervals, rather than a 1D leaderboard score.

---

## Sources

- [AMSTAR 2 — Shea et al. 2017, BMJ 358:j4008 (PMC5833365)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5833365/) — accessed 2026-11-09
- [PRISMA 2020 — Page et al. 2021, BMJ 372:n71 (PMC8005924)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/) — accessed 2026-11-09
- [DeepResearch Bench — Du et al. 2025 (arXiv:2506.11763v1)](https://arxiv.org/html/2506.11763v1) — accessed 2026-11-09
- [DeepResearch Bench II — Li et al. 2026 (arXiv:2601.08536v3)](https://arxiv.org/html/2601.08536v3) — accessed 2026-11-09
- [ResearchRubrics — Sharma et al. 2025, Scale AI (arXiv:2511.07685v1)](https://arxiv.org/html/2511.07685v1) — accessed 2026-11-09
- [DeepScholar-Bench — Patel et al. 2025, UC Berkeley (arXiv:2508.20033v2)](https://arxiv.org/html/2508.20033v2) — accessed 2026-11-09
- [Mind2Web 2 — Gou et al. 2025, OSU & Amazon AGI (arXiv:2506.21506v1)](https://arxiv.org/html/2506.21506v1) — accessed 2026-11-09
- [BrowseComp — Wei et al. 2025, OpenAI (arXiv:2504.12516v1)](https://arxiv.org/html/2504.12516v1) — accessed 2026-11-09
- [GAIA — Mialon et al. 2023 (arXiv:2311.12983)](https://arxiv.org/abs/2311.12983) — accessed 2026-11-09
- [STORM / FreshWiki — Shao et al. 2024, Stanford OVAL (arXiv:2402.14207v2)](https://arxiv.org/html/2402.14207v2) — accessed 2026-11-09
- [FActScore — Min et al. 2023 (arXiv:2305.14251)](https://ar5iv.labs.arxiv.org/html/2305.14251) — accessed 2026-11-09
- [SAFE & LongFact — Wei et al. 2024, Google DeepMind (arXiv:2403.18802v2)](https://arxiv.org/html/2403.18802v2) — accessed 2026-11-09
- [ALCE — Gao et al. 2023 (arXiv:2305.14627)](https://ar5iv.labs.arxiv.org/html/2305.14627) — accessed 2026-11-09
- [RAGAS — Es et al. 2023 (arXiv:2309.15217)](https://ar5iv.labs.arxiv.org/html/2309.15217) — accessed 2026-11-09
- [PaperQA2 — Skarlinski et al. 2024, FutureHouse (arXiv:2409.13740v2)](https://arxiv.org/html/2409.13740v2) — accessed 2026-11-09
- [Correctness is not Faithfulness in RAG Attributions — Wallat et al. 2024 (arXiv:2412.18004v1)](https://arxiv.org/html/2412.18004v1) — accessed 2026-11-09
- [AI Agents That Matter — Kapoor et al. 2024, Princeton (arXiv:2407.01502v1)](https://arxiv.org/html/2407.01502v1) — accessed 2026-11-09
- [$\tau$-bench — Yao et al. 2024 (arXiv:2406.12045v1)](https://arxiv.org/html/2406.12045v1) — accessed 2026-11-09
- [Anthropic Engineering — How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — accessed 2026-11-09
- [GPT-Researcher Evaluations README](https://github.com/assafelovic/gpt-researcher/blob/main/evals/README.md) — accessed 2026-11-09
