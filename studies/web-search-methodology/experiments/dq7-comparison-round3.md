# Experiment Round 3: Fixed Methodology (WebFetch Enabled)

**Date**: 2026-02-23
**Test question**: Same as R1/R2.
**Change from R2**: Updated methodology prompt with 5 specific fixes targeting R2 failures.

## What Was Fixed

R2 methodology failures and the fix for each:

| R2 Failure | Root Cause | R3 Fix |
|-----------|-----------|--------|
| Stopped at 2 fetches | Prompt said "1-3 WebFetch" | Changed budget to "3-5 WebFetch, do NOT stop at 2" |
| Luminary prereqs wrong (2 instead of 3) | Filled from training data, not source | Added Rule 5: "NEVER state something as fact unless from fetched source" |
| Hero prereqs wrong | Same — training data fill | Same rule + Rule 6: "verify counts and prerequisites explicitly" |
| Aishe "NPC in PS1" fabrication | Training data fill | Same Rule 5 |
| No cross-referencing | Only used 1 source domain | Added Rule 4: "Fetch 2-3 MORE pages to fill gaps AND cross-reference" |

## Raw Metrics

| Metric | Naive R2 | Meth R2 (broken) | Meth R3 (fixed) |
|--------|----------|-------------------|-----------------|
| **Total tokens** | 49,624 | 18,868 | 26,213 |
| **Duration** | 374s | 85s | 338s |
| **WebSearch calls** | 10 | 1 | 2 |
| **WebFetch successful** | 4 | 2 | 5 |
| **Total tool calls** | 24 | 3 | 9 |
| **Self-rated completeness** | 8/10 | 7/10 | 8/10 |
| **Self-rated confidence** | 8/10 | 8/10 | 8/10 |

## Quality Scoring (Against Ground Truth, 77 points)

| Category | Max | Naive R2 | Meth R2 | **Meth R3** |
|----------|-----|----------|---------|-------------|
| Characters identified | 6 | 6 | 6 | **6** |
| Character details | 5 | 5 | 3.5 | **5** |
| Basic human vocations | 10 | 10 | 10 | **10** |
| Intermediate human named | 7 | 7 | 7 | **7** |
| Intermediate human prereqs | 7 | 7 | 6 | **7** |
| Advanced human named | 3 | 3 | 3 | **3** |
| Advanced human prereqs | 3 | 3 | 2 | **3** |
| Basic monster vocations | 14 | 14 | 14 | **14** |
| Intermediate monster named | 12 | 12 | 12 | **12** |
| Advanced monster named | 8 | 6.5 | 6.5 | **6.5** |
| Error penalty | — | -1.5 | -3.5 | **-1.5** |
| **FINAL SCORE** | **77** | **72.0 (93.5%)** | **66.5 (86.4%)** | **72.0 (93.5%)** |

### What R3 fixed vs. R2:
- Luminary prereqs: Dancer + Gadabout (wrong) → Dancer + Troubadour + Gadabout (correct) ✓
- Hero prereqs: Champion + Sage (wrong) → any 3 intermediate/advanced (correct) ✓
- Aishe: "NPC in PS1" (fabricated) → joins with Dancer mastered + Warrior rank 3 (correct, sourced) ✓
- Maribel: no detail → "temporarily leaves when father falls ill" (correct, sourced) ✓

### What R3 still shares with naive:
- Both list "Gigalumph" (should be Galumph) and "Djinn Genie" (should be Vigilantern) for advanced monster vocations. This error comes from the Fandom wiki source itself, not training data — both agents that fetched Fandom got it.

### What R3 did that R2 didn't:
- Explicitly flagged unverified claims: "(partially unverified for 3DS)" on Druid prereqs
- Listed what was cross-referenced vs. what wasn't
- Distinguished 3DS-specific info from Reimagined version info
- Correctly identified naming differences between versions (Gadabout vs Jester, Monster Masher vs Monster Wrangler)

## Efficiency Comparison (All Runs)

| Run | Tokens | Quality | Quality/1k tokens | vs Naive R2 |
|-----|--------|---------|-------------------|-------------|
| R1 Naive (no fetch) | 39,829 | 82.5% | 1.59 | — |
| R1 Methodology (no fetch) | 30,842 | 85.7% | 2.14 | — |
| R2 Naive (with fetch) | 49,624 | 93.5% | 1.45 | baseline |
| R2 Methodology (with fetch) | 18,868 | 86.4% | 3.52 | 2.4x efficient but -7.1% quality |
| **R3 Fixed Methodology** | **26,213** | **93.5%** | **2.75** | **1.9x efficient, same quality** |
| Ground Truth | 74,452 | ~95%+ | 0.98 | — |

## Key Finding

**The fixed methodology matches naive quality (93.5%) at 53% of the token cost.**

The token budget increase from R2→R3 (18,868 → 26,213, +39%) bought a quality increase from 86.4% → 93.5% (+7.1 points). This is an excellent return — 39% more tokens for 8.2% more quality.

The remaining 1.5-point gap to ground truth (~95%) comes from advanced monster vocation naming errors that exist in the Fandom wiki source itself. Fixing this would require fetching a third source specifically for monster vocations (Woodus or Gamer Guides monster pages).

## Final Methodology Recommendations

Based on all three rounds of testing:

1. **Budget for Tier 2: 1-2 searches + 3-5 fetches** (R3 used 2 + 5 = 9 tool calls)
2. **Never fill gaps from training data** — always fetch or mark as unverified
3. **Cross-reference across 2+ source domains** — different wikis can have different errors
4. **Flag version confusion** — many DQ7 search results are for the 2025 Reimagined version, not 3DS
5. **The sweet spot is ~25-30k tokens** for a Tier 2 moderate-complexity question
