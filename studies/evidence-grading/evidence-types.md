# Evidence types: problems and worked examples

Companion to `GRADING-SCALE.md`. One section per evidence type from Q2 of the
proposal, plus two types the test set needed (repeated direct measurement,
and general observational statistics). Each section gives the start level
used in the scale, the known ways the type misleads, what moves it, and a
worked example. Facts come from the four researcher notes in `sources/`
(letter in brackets). [S] means the researcher saw only a search snippet,
not the page. "(unverified)" means nothing fetched confirmed it. Start levels
and "what moves it" are the scale's design choices, built from these facts.

---

## 1. Replications and registered reports

**Start:** High for a large preregistered multi-lab replication or a
registered report that tested the claim.

**Known problems**
- "Replicated" is not one test. The Open Science Collaboration (OSC 2015)
  project reported 36% of replications significant (vs 97% of originals),
  47% of original effect sizes inside the replication's 95% confidence
  interval [S], and 39% rated as replicated by the teams [S]. Same project,
  three rates (A).
- Replicated effects are smaller. OSC: about half the original size. Camerer
  et al. 2016 (economics): 11 of 18 (61%) replicated, mean effect 66% of the
  original. SCORE (released April 2026): about half of claims replicated
  with significant same-direction results, median effect more than 50% below
  the original (A).
- Registered reports report far fewer positive results: 44% vs 96% in
  standard reports (Scheel et al. 2021, 71 vs 152 papers) [S]. The authors
  say this does not directly prove less bias (A).
- Ecology has almost no direct replications: 9 of 38,730 open-access ecology
  and evolution papers (0.023%) call themselves replications (Kelly 2019) (C).

**What moves it:** a replication that found nothing, with the power to rule
out the claimed size, triggers the refuted override (Very low, status
`failed`). An underpowered null gives `inconclusive` and imprecision. A replication that found a much
smaller effect gives status `smaller` and imprecision if the claim states a
size.

**Worked example.** Many Labs 2: 28 findings, 125 samples, 15,305
participants. 15 (54%) significant in the original direction; median
Cohen's d 0.60 original vs 0.15 replication; variation was "attributable more to the
effect being studied than to the sample or setting" [S] (A). A claim
tested there that failed is Very low / `failed`. One that held but shrank is
graded on the replication's size, status `smaller`.

## 2. Meta-analyses

**Start:** the level of the studies pooled, never higher.

**Known problems**
- Meta-analyses overstate effects compared with big preregistered
  replications. Kvarven et al. 2020: 12 of 15 pairs differed significantly;
  meta-analytic effects were almost three times as large on average; three
  bias-correction methods did not fix it (A).
- The cause of that gap is disputed. Lewis et al. 2022 point to real effect
  differences between studies and protocols, not only publication bias. The
  two estimates still correlate r = 0.72, so they agree on rank order more
  than size (A).
- Bias-correction methods disagree. In simulations reported by a Carter et
  al. author, naive random-effects and trim-and-fill had false-positive rates
  "approaching 100%" under publication bias; PET/PEESE could err in either
  direction; p-curve and p-uniform failed under heterogeneity (A). In the
  ego-depletion data, a selection model gave d about .3 and PET-PEESE about
  −.3 [S] (A).
- Ecology: across 87 meta-analyses, correcting for publication bias made 66%
  (33 of 50) of significant means non-significant; average power was 15%,
  with about 4x exaggeration of effect size (Yang et al. 2023) (C).

**What moves it:** rate down for selective reporting when the pooled studies
are unregistered and no bias check was done, or when bias correction
removes or flips the effect. Start from the pooled studies' type and judge
indirectness once, pooled studies against the claim.

**Worked example (generic).** A meta-analysis pools unregistered single lab
experiments (start Moderate). No bias check was run: −1 selective reporting.
If a bias check was run and correction flipped the sign, that is the same
selective-reporting −1, not a second reason. A later large preregistered replication of the same
effect, if one exists, outranks the meta-analysis as the start point.

## 3. Natural experiments and quasi-experiments

**Start:** Moderate if as-if random assignment was checked (a balance test
passed, or the design matched a randomised benchmark). Low otherwise.

**Known problems**
- Real randomisation is not enough. Sekhon and Titiunik 2012 examined four
  published natural experiments and found that in each, random assignment
  "is not sufficient to provide an unbiased estimate of the causal effect".
  The groups the intervention makes comparable may not be the groups the
  question needs. Even their reanalysis of randomised electoral quotas in
  India found weaker evidence than first reported (B).
- As-if random is a matter of degree. Dunning calls it a "continuum of
  plausibility". John Snow's cholera study is his strong case; the 2003
  polling-place closures had small pre-treatment imbalances (B).
- Local effects may not carry over. Sekhon and Titiunik call this "a tension
  between internal validity and substantive relevance". No fetched source
  measured how often local effects fail to generalise (unverified) (B).

**What moves it:** up for a benchmark match; down for a broken assumption
(as-if random not shown) and indirectness (the effect is local to the cut-off
or setting).

**Worked example.** Close-election regression discontinuity. In US House
races 1942-2008 bare winners and losers differed on pre-election traits
(Caughey and Sekhon), so a claim resting on that design is −1 broken
assumption. In Finland, tie-break lotteries gave a randomised benchmark:
conventional RD showed a moderate incumbency advantage, the lottery showed
none, and bias-corrected RD agreed with the lottery (Hyytinen et al.) (B).
Bias-corrected RD there earns the benchmark-match rate-up; conventional RD
does not.

## 4. Comparative and cross-cultural databases

**Start:** Low.

**Known problems**
- **Missing data coding.** In the moralising-gods case, Beheim et al. found
  61% of Seshat moralising-gods data points had no value, the original paper
  coded them as absent, and using recorded data only or standard imputation
  reversed the finding. Nature retracted the 2019 paper in July 2021; three
  authors disagreed with the retraction [S]; the authors published a 2022
  "retake" saying the main finding stands (a claim by the original authors)
  (B).
- **Databases disagree with each other.** Database of Religious History
  historians and the Seshat team dispute codes such as Late Shang China. The
  account found comes from Turchin, a party to the dispute; no independent
  referee was found. A snippet says over two-thirds of Seshat data did not
  match equivalent DRH entries [S] (B).
- **Time focus.** In the Ethnographic Atlas (inside D-PLACE), 69% of focal
  years fall in 1900-1950. Focal years for the same society can differ
  between datasets by more than 50 years. The authors say coder and
  ethnographer bias affects the data (Kirby et al. 2016) (B).
- **Galton's problem** (related or neighbouring cultures are not independent
  samples). Phylogenetic methods handle shared descent but not borrowing
  between neighbours; in simulations, false-positive rates rose with
  borrowing (Nunn et al. 2010) (B). SCCS tries to reduce relatedness by
  taking one society per culture area (186 societies) (B).
- How Pulotu, DRH and eHRAF code data was not researched (unverified) (B).

**What moves it:** down for broken assumption (missing coded as absent),
non-independent samples (no relatedness control), inconsistency (databases
disagree). Up when independent datasets or other evidence types agree.
Record "retracted, republished by the same authors" in the claim row, and
mark contested.

**Worked example (generic).** A database regression whose key variable was
mostly missing and coded as "absent": start Low, −1 broken assumption. If the
same societies were counted as separate cases with no control for
relatedness, also −1 non-independent samples. A retraction followed by a
same-author republication is recorded in the claim row and meets the
contested-flag test (section 6 of the scale). (The moralising-gods test claim
itself is left for the blind graders.)

## 5. Archaeology

**Start:** Low.

**Known problems**
- **Dating.** Radiocarbon dates must be calibrated. On a plateau in the
  calibration curve, one date can mean two calendar ranges. At an Ontario
  village site, short-lived plant remains gave about equal probability near
  AD 1500 or AD 1600; after more dates and modelling it was placed at about
  AD 1595-1626 (95.4%). The authors warn Bayesian (OxCal) results for short
  sites can be "overly compressed" and drift from the real age (Manning and
  Birch 2022). One site and one period, not a general error rate (B).
- **What survives.** Geology decides which sites survive and get found,
  which biases population estimates built from counts of radiocarbon dates.
  Local landform-age corrections beat global or no correction in a
  simulated case (Contreras and Codding) (B).
- Reading social structure from remains: no fetched source (unverified) (B).

**What moves it:** down for imprecision (dates on a plateau), indirectness
(one site for a regional claim). Up when independent lines agree (for
example a tree-ring wiggle-match, which the authors call the best fix where
available).

**Worked example.** A claim that a village dated to "about AD 1500" based on
plant-remain dates from the plateau: −1 imprecision, giving Very low until
extra dates or a wiggle-match are added.

## 6. Ethnography

**Start:** Low.

**Known problems**
- **Single observer.** In the Mead-Freeman dispute both sides drew on one
  observer's record. Shankman (2009) reports Freeman "cherry picked" and that
  transcripts of Freeman's own interviews with his key informant were
  contradictory; he also says Mead's work was "not flawless". Orans (1996)
  re-read Mead's notes and argued the data support several conclusions [S]
  (B).
- **The ethnographic present** (describing a group as timeless). Fabian
  (1983) named it [S]. The Atlas focal years (69% in 1900-1950) show which
  "present" a database actually codes (B).
- No fetched estimate of how often restudies disagree (unverified) (B).

**What moves it:** down for weak source (single observer, no restudy). Up
when archival material or another observer independently confirms.

**Worked example.** A claim from one ethnographer, never restudied, about a
custom: Low −1 weak source = Very low. With an independent restudy that
agrees: Low +1 = Moderate, subject to the Moderate check.

## 7. Historical written sources

**Start:** Low.

**Known problems**
- **Numbers in old sources.** Herodotus gives 1,700,000 fighting men for
  Xerxes' land army; Delbrück (1887) argued for at most about 55,000; a
  historiographical article reports agreement on 50,000-100,000 [S, all from
  snippets and non-scholarly pages; treat as leads]. Proposed reasons for
  inflation include the king's interest in a large army and the difficulty of
  counting a marching column [S] (B).
- "Who wrote it and why" beyond this example: no fetched source (unverified)
  (B).

**What moves it:** down for weak source (a number with no independent
check). Up when independent sources, archaeology or other evidence agree.

**Worked example.** "Xerxes led 1.7 million soldiers": Low −1 weak source,
and modern estimates are far lower, so the refuted override applies: Very
low, `failed`.

## 8. Field ecology and animal observation

**Start:** Low for observation and citizen-science records; Moderate for a
field experiment with controls.

**Known problems**
- **Questionable research practices.** Of 807 ecologists and evolutionary
  biologists surveyed (15% response rate, self-report), 64% admitted not
  reporting non-significant results, 42% collecting more data after checking
  significance, 51% presenting an unexpected finding as predicted (Fraser et
  al. 2018) (C).
- **Same data, different answers.** 174 teams (246 analysts) analysed two
  ecology datasets. On one, estimates ran from large negative to near zero,
  some significant in the opposite direction; on the other, about a third of
  estimates were significant in one direction or the other (Gould et al.) (C).
- **Citizen-science bias.** In 1,107,224 iNaturalist bird records compared
  with eBird, large-bodied birds and birds in large flocks were
  over-represented (Callaghan et al. 2021) (C).
- **eDNA.** Even low false-positive rates bias occupancy estimates, and
  throwing out single detections by hand also biases them (Lahoz-Monfort et
  al. 2016) (C).
- **Short studies.** Long-term datasets are exceptions because studies
  outlast funding cycles [S]. No verified share of short studies
  (unverified). LTER not researched (C).

**What moves it:** down for indirectness (one site for a broad claim),
inconsistency (separate studies disagree; analysts disagreeing over the same
data is a contested-flag question only), selective reporting. Fenced plots
start Moderate only for the link they test (browsing); for a claim about
what caused the browsing change, use the type covering the whole claim. Up when long-term
data and experiments agree.

**Worked example (evidence only, no grade).** Yellowstone wolves. Ripple et al.
(2025) claimed a 1,500% rise in willow crown volume. MacNulty and Cooper
(2025) call it circular because plant height was both input and predictor,
and argue the response is "more modest and spatially variable". Hobbs et al.
(2024), 20 years of field data, found only weak cascade effects (source is a
press release from one side) (C). This shows the parts a contested-claim row
needs: named camps, the point of dispute (here method: a circular volume
estimate vs long-term field data, reported as fenced plots [S]), and what result would settle it
(for example matched plots and an analysis that does not use height on both
sides). The test claim itself is left for the blind graders.

## 9. Lab and field experiments (single study)

**Start:** Moderate.

**Known problems**
- Single published social-science results reproduce about 36-62% of the time
  across the big projects (OSC 36%, Camerer 2016 61%, Camerer 2018 about
  62%), with effects around half the original (A).
- WEIRD samples: listed in the proposal; the notes did not research it
  (unverified).
- Analytic flexibility: in Silberzahn et al. 2018, 29 teams analysing one
  dataset split 20 (69%) significant positive vs 9 not, with odds ratios from
  0.89 to 2.93 (D). Breznau et al. 2022 (73 teams) left over 95% of the
  variance in results unexplained after coding every identifiable analytic
  choice (D).

**Why Moderate, not High as in GRADE.** GRADE starts randomised trials at
High (A). The replication rates above say a single unreplicated
social-science experiment is closer to a coin flip, so the scale starts it
one level lower.

**What moves it:** down for imprecision (small sample), indirectness (lab
task, WEIRD sample), selective reporting (unregistered single positive
result). Up for a preregistered replication that agrees.

**Worked example (generic).** A single unregistered lab study with a student
sample, for a claim about all humans: Moderate −1 indirectness −1 selective
reporting = Very low. The checks in section 5 of the scale can only lower a
level, never raise it, so the result stays Very low.

## 10. Models and simulations

**Start:** Very low for an untested theory model; Low for a model fitted to
data but not tested on new data; Moderate for a model checked against
patterns it was not fitted to, or an ensemble checked against observations.

**Known problems**
- A model cannot be verified, only partly confirmed. Oreskes et al. 1994:
  "Verification and validation of numerical models of natural systems is
  impossible"; "confirmation is inherently partial"; "the primary value of
  models is heuristic" (C).
- Ensembles are not equal votes. Roughly 10 of 55 CMIP6 climate models have
  climate sensitivity above 5 °C and run too hot; AR6 weighted models by how
  well they matched past temperatures (secondary source) (C). Models share
  code and parts, so model count overstates independent estimates [S] (C).
- Mupepele et al. 2016 grade models by testing: untested theory model LoE4,
  data-parameterised LoE3b, validated LoE3a, confirmed by several unrelated
  datasets LoE2b (C). The scale's three model start levels follow this.

**What moves it:** up when the patterns the model was checked against are
independent real data (the ODD protocol's first element asks the modeller to
name those patterns) (C). Down for indirectness when the model is applied
outside the conditions it was checked in.

**Worked example.** A battle model fitted to a set of historical battles but
not tested on others starts Low. If it was later tested on battles it was
not fitted to and matched, it starts Moderate. If tests on new battles fit
poorly across the board, the refuted override applies. If it fits some and
not others, status `inconclusive`.

## 11. Repeated direct measurement (added)

**Start:** High.

This covers instrument records, counts and standard monitoring of the
claimed quantity itself, repeated by independent groups (earth-science
measurement in the test set). It applies to descriptive claims only (how
much, how often, what makes up a group). A causal claim resting on repeated
observation starts Low. None of the
four notes researched it. Starting it at High is the writer's design choice,
by analogy with GRADE's rule that the strongest design starts at the top.
The pilot should test it.

**What moves it:** down for indirectness when the claim is broader than what
was measured (for example a global average stated as a rule for every
place), and imprecision when the claim's number sits outside the measured
range.

**Paleoclimate proxies are not direct measurement.** They start Low. Tree
rings at northern sites stopped tracking warming from about the
mid-20th century, causes uncertain; a PAGES 2k analysis found tree rings lack
a pre-industrial cooling that ice, marine and lake records show [S, all
snippets] (C). Rate up when proxy types agree; rate down for indirectness
when one region's records support a worldwide claim.

## 12. Observational statistics (added)

**Start:** Low.

Surveys, cohort and twin studies, cross-national statistics, conflict
datasets and comparative regressions. GRADE starts observational studies at
Low (A). The notes did not research these types one by one. Critics say
GRADE rates observational evidence too low for fields where trials can't be
run, and a 2023 environmental-health paper argues some observational studies
can be high-confidence [S] (A). The rate-up reasons (independent lines,
large consistent effect, dose-response) are how such evidence climbs.
Many-analyst results (section 9) show a single observational analysis is
one draw from a range. Since the pilot, analyses of the same data that
disagree do not count as inconsistency; they go to the contested flag.
Conflicting results from separate datasets still do.
