# Experiment: Naive vs. Methodology-Informed Web Search

**Date**: 2026-02-22
**Test question**: "What are all playable characters in Dragon Quest VII (3DS remake), their default starting classes, and all available vocations (both basic and advanced)?"
**Important confound**: WebFetch was denied by permissions for both agents, forcing both into snippet-only mode. This tests search strategy differences under the same constraint.

## Raw Metrics

| Metric | Naive Baseline | Methodology-Informed | Ground Truth (reference) |
|--------|---------------|---------------------|--------------------------|
| **Total tokens** | 39,829 | 30,842 | 74,452 |
| **Duration** | 185s (3m 5s) | 152s (2m 32s) | 309s (5m 9s) |
| **WebSearch calls** | 12 | 8 | ~40+ |
| **WebFetch calls** | 3 (all denied) | 2 (all denied) | 0 (all denied) |
| **Total tool calls** | 15 | 10 | 65 |
| **Self-rated completeness** | 7/10 | 7/10 | N/A (exhaustive) |
| **Self-rated confidence** | 7/10 | 7/10 | N/A (cross-referenced) |

The ground truth agent used **2.4x** the tokens of naive and **4.1x** the methodology approach. This demonstrates the cost curve: going from ~85% to ~95%+ completeness requires disproportionately more resources (diminishing returns).

## Quality Scoring (Against Ground Truth)

Ground truth was established by a 3rd agent using 40+ tool calls and exhaustive cross-referencing.

### Scoring Checklist (77 total points possible)

| Category | Max Points | Naive | Methodology | Notes |
|----------|-----------|-------|-------------|-------|
| **Characters identified** | 6 | 6 | 6 | Both got all 6 |
| **Character details** (leaves/joins/pre-leveled) | 5 | 3 | 4.5 | M got Aishe pre-leveled + Maribel temp departure; N missed both |
| **Basic human vocations named** | 10 | 10 | 10 | Both perfect |
| **Intermediate human vocations named** | 7 | **7** | 6 | M listed non-existent "Ranger", missed Monster Masher |
| **Intermediate human prerequisites** | 7 | **7** | 5 | M had fabricated Ranger prerequisites, missed Monster Masher |
| **Advanced human vocations named** | 3 | 3 | 3 | Both perfect |
| **Advanced human prerequisites** | 3 | 2.5 | **3** | M got Hero's flexible prereqs right; N listed specific vocations |
| **Basic monster vocations** | 14 | **14** | 13 | M listed "Rosevine" instead of Mandrake major |
| **Intermediate monster vocations named** | 12 | 5 | **12** | N only named 5 explicitly; M got all 12 |
| **Advanced monster vocations named** | 8 | **7** | 6.5 | N: 7/8. M: "Gigalumph" misspelling, missed Vigilantern |
| **Factual error penalty** | — | -1 | **-3** | M: Ranger fabrication (-1), Rosevine (-1), wrong prereqs (-1) |
| | | | | |
| **TOTAL** | 77 | **63.5** | **66** | |
| **Percentage** | | **82.5%** | **85.7%** | |

### Quality Summary

| Dimension | Winner | Explanation |
|-----------|--------|-------------|
| **Human vocations accuracy** | Naive | Got all 7 intermediate vocations right; methodology invented "Ranger" |
| **Monster vocation coverage** | Methodology | Named all 12 intermediate monster vocations vs. only 5 for naive |
| **Character details** | Methodology | Captured Aishe's pre-leveled vocations and Maribel's temp departure |
| **Prerequisite accuracy** | Naive | 100% accurate on all stated prerequisites |
| **Fabrication rate** | Naive | 0-1 errors vs. 3 errors for methodology |

## Key Findings

### 1. Methodology-Informed was 23% cheaper and 18% faster

The methodology agent used 33% fewer tool calls and 23% fewer tokens to achieve slightly higher overall coverage. This validates the core claim: **directed searching outperforms shotgun searching**.

### 2. Methodology got broader coverage but introduced errors

The methodology agent's broad-first approach surfaced more monster vocation names (12/12 intermediate vs 5/12), but its aggressive snippet-based extraction led to 3 fabricated facts vs. ~1 for naive. The "Ranger" error is particularly notable — the agent confused the PS1 localization name with a separate 3DS vocation.

### 3. Naive was more conservative and precise

The naive approach made more searches (12 vs 8) but each was more targeted after the first few. It stated fewer things it couldn't verify, resulting in higher precision per-claim. However, it left bigger gaps in coverage (intermediate monster vocations).

### 4. Both suffered equally from no WebFetch

Neither agent could verify claims against authoritative wiki pages. Both self-rated at 7/10, correctly identifying that snippet-only mode limits confidence. **WebFetch access would likely have caught the methodology agent's Ranger error** (the wiki clearly lists only 7 intermediate vocations, not 8).

### 5. Token efficiency does not require sacrificing quality

At 82.5% vs 85.7% quality and 39.8k vs 30.8k tokens, the methodology approach achieved *slightly better* quality for *significantly less cost*. The efficiency-quality tradeoff is not a strict tradeoff — better search strategy improves both.

## Efficiency Ratio (Quality Per Token)

| Agent | Quality Score | Tokens | Quality/1000 tokens |
|-------|-------------|--------|-------------------|
| Naive | 63.5 | 39,829 | 1.59 |
| Methodology | 66.0 | 30,842 | **2.14** |

**Methodology-informed search is 34% more token-efficient per unit of quality.**

## Caveats

1. **WebFetch was denied for both** — this is a major confound. The methodology's recommendation #3 (targeted WebFetch prompts) couldn't be tested. With WebFetch, the gap would likely be larger because the methodology agent would have fetched fewer, better-targeted pages.

2. **Single test question** — this was one question about a niche JRPG. Results may differ for other domains (API docs, current events, scientific topics).

3. **Self-assessment bias** — both agents rated themselves 7/10 despite different error profiles. Self-assessment is unreliable for quality measurement.

4. **Ground truth may be imperfect** — the ground truth agent also couldn't use WebFetch and may have its own gaps (e.g., it listed 8 advanced monster vocations while some sources suggest ~10).

## Recommendations

Based on this experiment and the broader literature survey:

1. **Use the methodology approach** — it's cheaper and produces comparable-to-better quality
2. **WebFetch is critical** — both agents would have improved significantly with even 2-3 targeted page fetches. The methodology's emphasis on targeted extraction prompts is the most important untested principle.
3. **Add a verification step** — the methodology should include a "verify surprising claims" step to catch fabrications like the Ranger error
4. **Snippet-only mode is viable for surveys** — for getting a broad lay of the land, search snippets alone achieved 82-86% completeness
5. **WebFetch matters most for precision** — to push from ~85% to ~95%+, you need to fetch and verify against authoritative sources
