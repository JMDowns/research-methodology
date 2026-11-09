# Experiment Round 2: Naive vs. Methodology-Informed (WebFetch Enabled)

**Date**: 2026-02-23
**Test question**: Same as Round 1 — "What are all playable characters in Dragon Quest VII (3DS remake), their default starting classes, and all available vocations (both basic and advanced)?"
**Key change from Round 1**: WebFetch was approved and functional. Both agents could fetch page content.

## Raw Metrics

| Metric | Naive (R2) | Methodology (R2) | Ratio |
|--------|-----------|------------------|-------|
| **Total tokens** | 49,624 | 18,868 | **2.6x cheaper** |
| **Duration** | 374s (6m 14s) | 85s (1m 25s) | **4.4x faster** |
| **WebSearch calls** | 10 | 1 | 10x fewer |
| **WebFetch calls** | 14 attempted (4 succeeded) | 2 succeeded | — |
| **Effective fetches** | 4 (Fandom wiki pages) | 2 (Fandom wiki pages) | — |
| **Self-rated completeness** | 8/10 | 7/10 | — |
| **Self-rated confidence** | 8/10 | 8/10 | — |

## Quality Scoring (Against Ground Truth, 77 points)

| Category | Max | Naive R2 | Meth R2 | Notes |
|----------|-----|----------|---------|-------|
| Characters identified | 6 | 6 | 6 | Both perfect |
| Character details | 5 | **5** | 3.5 | N: Aishe pre-leveled at Dancer mastered + Warrior 3-star (from WebFetch!). M: missed Aishe detail |
| Basic human vocations | 10 | 10 | 10 | Both perfect |
| Intermediate human named | 7 | 7 | 7 | Both perfect |
| Intermediate human prereqs | 7 | **7** | 6 | M: Luminary listed as Dancer + Gadabout only (missing Troubadour — requires all 3) |
| Advanced human named | 3 | 3 | 3 | Both perfect |
| Advanced human prereqs | 3 | **3** | 2 | M: said Hero requires Champion + Sage. Correct: any 3 intermediate OR 2 int + 1 adv |
| Basic monster vocations | 14 | 14 | 14 | Both perfect |
| Intermediate monster named | 12 | 12 | 12 | Both perfect |
| Advanced monster named | 8 | 6.5 | 6.5 | Both: "Gigalumph" (should be Galumph), "Djinn Genie" (should be Vigilantern) |
| **Subtotal** | **77** | **73.5** | **70** | |
| Error penalty | — | -1.5 | -3.5 | M: Aishe "NPC in PS1" (fabricated, -1), Luminary prereqs (-already counted), Hero prereqs (-already counted) |
| **FINAL SCORE** | **77** | **72.0 (93.5%)** | **66.5 (86.4%)** | |

## Efficiency Ratio (Quality Per Token)

| Agent | Quality | Tokens | Quality/1000 tokens |
|-------|---------|--------|-------------------|
| Naive R2 | 72.0 | 49,624 | 1.45 |
| Methodology R2 | 66.5 | 18,868 | **3.52** |

**Methodology is 2.4x more token-efficient per unit of quality**, despite achieving lower absolute quality.

## Cross-Round Comparison (All Runs)

| Run | Tokens | Duration | Tool Calls | Quality (%) | Quality/1k tokens |
|-----|--------|----------|-----------|-------------|-------------------|
| R1 Naive (no fetch) | 39,829 | 185s | 15 | 82.5% | 1.59 |
| R1 Methodology (no fetch) | 30,842 | 152s | 10 | 85.7% | 2.14 |
| **R2 Naive (with fetch)** | **49,624** | **374s** | **24** | **93.5%** | **1.45** |
| **R2 Methodology (with fetch)** | **18,868** | **85s** | **3** | **86.4%** | **3.52** |
| Ground Truth (exhaustive) | 74,452 | 309s | 65 | ~95%+ | ~0.98 |

## Key Findings

### 1. WebFetch dramatically improved quality for naive but not methodology

- Naive: 82.5% → 93.5% (+11 points) — the extra fetched pages filled in critical details
- Methodology: 85.7% → 86.4% (+0.7 points) — nearly identical despite having WebFetch

**Why?** The naive agent fetched 4 different Fandom wiki pages (vocation system, character list, Aishe, Hero vocation, Champion, Druid) and extracted detailed info from each. The methodology agent only fetched 2 pages and relied on those plus training knowledge. It was too conservative — it stopped too early.

### 2. Methodology's token efficiency advantage grew even larger

- R1: methodology was 34% more efficient per quality point
- R2: methodology was **143% more efficient** per quality point (3.52 vs 1.45)

The methodology agent achieved 86.4% quality with just 3 tool calls and 18,868 tokens. That's extraordinary efficiency.

### 3. The "optimal stopping" tradeoff is real

The methodology agent's biggest weakness was stopping too early. It used only 1 search + 2 fetches, then synthesized. This missed:
- Aishe's pre-leveled vocation details
- Correct Luminary prerequisites (3 vocations, not 2)
- Correct Hero vocation prerequisites

The naive agent's willingness to keep fetching (14 attempts, 4 succeeded) caught these details. **The methodology needs a "minimum fetch" rule**: always verify at least 2-3 key claims with dedicated fetches, even if you think you have enough.

### 4. WebFetch makes the naive approach MORE expensive, not less

Counter-intuitively, the naive agent used MORE tokens with WebFetch (49,624) than without (39,829). Each fetch attempt costs tokens even when denied, and successful fetches inject page content into the context. The methodology approach went the other direction — fewer, better-targeted fetches = fewer total tokens.

### 5. Both agents shared the same monster vocation errors

Both listed "Gigalumph" (should be Galumph) and "Djinn Genie" (should be Vigilantern). These errors likely come from training data, not search results. Neither agent verified the advanced monster vocation names — this is where the "verify surprising claims" step would help.

## Updated Recommendations

1. **Methodology approach is still better overall** — 2.4x more efficient per quality point
2. **Add a "minimum verification" rule**: After initial search+fetch, always do 1-2 targeted verification fetches for prerequisites, counts, and names
3. **Aim for 3-5 fetches on Tier 2 questions**, not 1-2 — the methodology was too aggressive about minimizing fetches
4. **Target the RIGHT pages**: Both agents succeeded with Fandom wiki but failed on most other sites. The methodology should prioritize Fandom wiki (dragonquest.fandom.com) for gaming topics
5. **The sweet spot is ~25,000-35,000 tokens** for a Tier 2 question — enough for 2-3 searches and 3-5 fetches with verification
