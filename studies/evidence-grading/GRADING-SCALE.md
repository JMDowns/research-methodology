# Evidence grading scale (v0.4, 2026-11-09)

## 1. The claim

- Grade each claim exactly as written, number included: a pattern as a pattern, not as an inferred cause.
- If you write the claim sentence yourself, use the popular wording. Don't narrow it or add a number the popular claim doesn't have.
- **Negated claims.** If the claim denies a cause, an ability or an existence ("X does not feel pain", "Y has no effect", "leaders rarely matter"), rewrite it as the positive claim it denies and grade that. Note "stated as negation" in the row. In rule 2, the negated claim is the rival. A claim about how often an event happens ("democracies rarely fight each other") is a rate, not a negation: grade it as stated.

## 2. Levels

- **High:** very unlikely to change.
- **Moderate:** probably right; size or scope could change.
- **Low:** could well be wrong; the number may be unsupported.
- **Very low:** no real data, data saying false, or data too flawed for any reading.

## 3. Start levels

Step 1: start at the strongest evidence type that tests the claim.

- **High:** preregistered multi-lab replication or registered report; repeated direct measurement by independent groups.
- **Moderate:** randomised experiment; natural experiment with as-if random checked; controlled field experiment (fenced plots, before-after-control); model checked on data it wasn't fitted to.
- **Low:** unchecked natural experiment; fitted, untested model; observational data (surveys, cohort, twin, cross-national); cross-cultural databases (Seshat, D-PLACE, SCCS, eHRAF); field observation, citizen science; archaeology, paleoclimate proxies, ethnography, historical sources.
- **Very low:** untested theory, expert opinion, mechanism-only reasoning, popular story.
- **Meta-analysis:** the pooled studies' start, never higher.

Tie-breakers, in order:
1. A design counts only if it tests the cause the claim names. If it tests one link, use the type covering the whole claim.
2. **Repeated direct measurement** means instruments or counts of the claimed quantity by two or more independent teams, for descriptive claims only. Coded categories (war, democracy) are observational. Causal claims from observation stay Low.
3. **Measured totals and fitted coefficients.** A total or ratio built from measured inputs by a standard accounting or budget method (GDP, wages, trade volume, population count, an energy budget, a transfer efficiency) counts as repeated direct measurement when the claim is about that total or ratio itself and two or more independent teams or agencies produced it. A total for places or times without records (historical GDP, ancient population) is a reconstruction: Low. A coefficient fitted across many units (scaling exponent, elasticity, heritability, growth effect) is a fitted pattern from observational data: Low, however well each unit is measured. Fitting the same coefficient again on another country's data is a repeat, not "a model checked on data it wasn't fitted to".
4. Two types still fit? Take the lower.

## 4. Move the grade (checklist)

Step 2: answer every item and write the codes that fired in the row. One problem counts once. Unsure? Don't apply it, and write "unsure" beside the code.

Down (−1 each):
- **D1 Broken assumption:** as-if random not shown; missing data coded as a value; confounding ignored.
- **D2 Inconsistency:** do separate studies or datasets conflict on direction, or give values that don't include the claim's number? Check the claim's number against each study's figure. Same direction, different size → status `smaller`, no −1. Two analyses of the *same* data → contested flag only.
- **D3 Indirectness:** population, setting or measure differs from the claim's. Lab-versus-field gaps are indirectness only. For meta-analyses, judge pooled studies against the claim once.
- **D4 Imprecision:** few cases; status `unclear`; or the number outside the supported range.
- **D5 Selective reporting:** is the claim backed by one positive result that no other team or design has repeated (any design or date)? Or unregistered studies with no bias check, or bias correction removes or flips the effect?
- **D6 Non-independent samples:** related cultures counted separately, no relatedness control.
- **D7 Weak source:** single observer; unchecked old number; key paper retracted. Your own access limits (you reached only a Wikipedia page or a snippet) are not D7: mark the source [S] and grade what it reports.

Up (+1 each, at most +2):
- **U1** Independent lines agree (no shared origin; not lines rated down under D2).
- **U2** Large consistent effect.
- **U3** Dose-response.
- **U4** Matches a randomised benchmark.

## 5. Checks (yes/no)

Step 3: failing one drops to the highest level that passes.

- **C1 Refuted:** did the strongest test find the claim false, with power to see it (interval rules out the claimed size, or opposite found)? Yes → Very low, `failed`, stop. An underpowered null is `unclear` (D4).
- **C2 Absence** is a test only if people looked where it would show and would have recorded it; then apply C1. Otherwise Very low, `untested`.
- **C3 High** needs: two or more independent sources agree; one design rules out the main rival explanation; no unanswered published critique.
- **C4 Moderate** needs: a well-run study tests the claim as written, and no equal-quality evidence against it.
- **C5 Low** needs: some data bear directly on the claim.

## 6. Status and contested flag

**Status** (pick one):
- `holds`: the evidence supports the claim as written.
- `smaller`: direction holds, size well below.
- `mixed`: tested; holds in some named cases (places, groups, eras) and not others. No rate-down for this alone. If the claim says "all", "always" or "worldwide", the failing cases are a test of it: apply C1.
- `unclear`: tested, but the evidence can't decide. An underpowered or small test whose interval covers both no effect and the claimed effect, or a result whose direction flips (effect goes away or reverses) with analysis choices on the same data, such as missing-data handling or coding. Apply D4.
- `conflicting`: separate studies or datasets disagree on direction or on the claim's number. Apply D2, not also D4.
- `failed`, `untested`, `n/a` (one past event no study could retest).

**Contested = yes** only if (a) named researchers publish a current differing reading of similar evidence, and (b) nothing settled it. A large preregistered test or field consensus settles it unless objectors bring new data. Retracted-then-republished counts. `failed` claims can be contested. The flag never moves the grade. Name camps and what would settle it.

## 8. Claim row

Columns: claim, grade, evidence type, key source, status, contested, camps/settles, checklist codes fired (D, U, C).

Inline: `[V] [grade: moderate · meta-analysis · smaller · contested]`
