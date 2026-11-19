# Evidence, statistics, and reporting

How strongly to state a claim, how to report numbers, and which reporting guideline applies. The journal's instructions override the formatting defaults here.

## Contents

1. Evidence-matched verbs
2. Hedging calibration
3. Statistical reporting
4. Number and unit formatting
5. Reporting guidelines by design
6. Length budgets (defaults when the journal is silent)
7. Integrity checklist

---

## 1. Evidence-matched verbs

The verb follows the design, not the authors' confidence.

| Design and claim | Use | Avoid |
|---|---|---|
| RCT, primary (or prespecified key secondary) endpoint, significant | reduced, increased, improved, prevented | "may reduce" (over-hedged), "proved" |
| RCT, secondary or post hoc endpoint | was associated with, was lower in, exploratory analysis suggested | causal verbs |
| RCT, null primary endpoint | did not reduce, did not differ (estimate, CI) | "trended toward", "failed to reach significance but..." |
| Observational cohort or case-control | was associated with, was more common in, predicted | reduces, prevents, causes, protects, "linked to" |
| Mendelian randomization, natural experiment, difference-in-differences | genetically predicted X was associated with; may have a causal effect, stated with the design's assumptions | unqualified causal claims |
| Cross-sectional | was associated with, co-occurred with | predicted (implies temporality), led to |
| Diagnostic or prognostic model, retrospective internal validation | discriminated, achieved an AUROC of, identified | demonstrates clinical utility, outperforms clinicians, generalizes |
| Model, external validation | maintained (or did not maintain) discrimination in the [named] cohort | robust across settings, generalizes |
| Reader study or silent deployment | changed reader sensitivity by, agreed with | improves outcomes |
| Case report or series | suggests, raises the possibility, is consistent with | demonstrates efficacy, establishes, should be first-line |
| In vitro or animal | in [cell line / model], X increased Y | implies the human effect |
| Overlapping 95% CIs without a paired test | numerically higher, with overlapping 95% CIs; the difference was X (95% CI) | higher, better, superior |
| No equivalence or non-inferiority margin | did not differ significantly | comparable, equivalent, as effective as |

Single studies "show" or "indicate"; replicated findings "demonstrate"; preliminary observations "suggest". Reserve "proves", "confirms", "establishes", "definitively" for mathematics and replicated, convergent evidence.

## 2. Hedging calibration

One hedge per claim, sized to the evidence.

| Strength of evidence | Typical phrasing |
|---|---|
| Strong, direct (RCT primary result) | "X reduced Y." |
| Moderate (well-designed observational, consistent with prior work) | "X was associated with lower Y." "These findings suggest that X reduces Y." |
| Interventional implication from observational data | "Reducing X may help lower Y." |
| Mechanism with indirect support | "One possible explanation is..." "X may act through..." |
| Speculation | "We speculate that..." "It is possible that..." |

Stacked hedges ("may suggest that X could potentially have a possible effect") are one failure; bare causal claims from observational data are the opposite failure. Both are miscalibration. Preserve an author's explicitly stated opinion or expectation ("We expect this marker to become central to...") as opinion; don't flatten it into a hedge, and don't let it masquerade as a finding.

## 3. Statistical reporting

Every inferential result: estimate, measure of precision, and test where relevant.

- **Effect estimate with 95% CI** for every primary and secondary comparison: risk difference, RR, OR, HR, mean difference, with the CI. "HR 0.86 (95% CI 0.66 to 1.12)", never "HR 0.86 (NS)".
- **Exact p values** ("P = 0.03"), except "P < 0.001" for very small values. Not "P < 0.05". Not "P = 0.000".
- **Test statistic and degrees of freedom** where the field expects them: t(18) = 4.3, F(2, 87) = 5.1, χ²(1) = 6.2.
- **Absolute as well as relative effects** for clinical outcomes: event rates in each group, absolute risk difference, and number needed to treat where sensible.
- **Lead with the finding, not the test.** "Mortality was lower with X (8.1% vs 11.4%; HR 0.70, 95% CI 0.58 to 0.85)."
- **Survival**: median with 95% CI, HR with 95% CI, numbers at risk under Kaplan-Meier curves.
- **Regression**: what was adjusted for, and why (prespecified, DAG, or data-driven); unstandardized coefficients with CIs.
- **Diagnostic accuracy**: sensitivity, specificity, PPV, NPV at a stated threshold, with how the threshold was chosen, plus prevalence; AUROC with CI. Translate to counts per 1,000 tested when discussing clinical meaning.
- **Prediction models**: discrimination and calibration (calibration plot, slope, intercept); decision-curve analysis where clinical use is claimed.
- **Agreement**: Bland-Altman limits of agreement, not correlation alone.
- **Multiplicity**: state the correction method or that none was applied; label exploratory analyses.
- **Missing data**: amount per variable and how handled.
- **Meta-analysis**: pooled estimate with CI, prediction interval where useful, I² and tau², number of studies and participants, certainty (GRADE).
- **Bayesian**: posterior summary with credible interval, prior specification, and probability of benefit if relevant.

Never write: "trend toward significance", "marginally significant", "approached significance", "borderline significant", "significant" without a test, or "clinically significant" without a stated threshold.

## 4. Number and unit formatting

Defaults (AMA-style); the journal wins.

- Numerals for all measurements, units, percentages, ages, and numbers 10 and above; spell out numbers below 10 when not attached to units. Spell out any number that begins a sentence, or rephrase.
- Leading zero for decimals below 1 (0.03), unless the journal style drops it for p values.
- Decimal places consistent with measurement precision: usually one for percentages, two for ratios and AUROC.
- CIs in a consistent format: "0.79 to 0.91" or "0.79-0.91" per journal; never mix within a manuscript.
- Means with SD as "mean (SD)" or "mean ± SD" per journal; medians with IQR.
- SI units (with conventional units in parentheses if the journal requires).
- Generic drug names; brand names only when scientifically necessary.
- Every abbreviation defined at first use in the Abstract and again in the main text; avoid non-standard abbreviations; don't start a sentence with one. Dataset and cohort short names (MIMIC-IV, UK Biobank conventions) also need expansion at first use.
- Person-first and precise language: "patients with diabetes" not "diabetics", "adults aged 65 years or older" not "the elderly", "participants" or "patients" not "subjects" for humans.

## 5. Reporting guidelines by design

Name the guideline and satisfy its items (check the current version at equator-network.org).

| Design | Guideline | Items commonly missed |
|---|---|---|
| Randomized trial | CONSORT 2025 (or 2010 if the journal specifies) | Flow diagram, allocation concealment, blinding of whom, ITT, harms, registration |
| Trial protocol | SPIRIT | Schedule of assessments, sample size assumptions, data monitoring |
| Observational (cohort, case-control, cross-sectional) | STROBE | Source population, exposure definition, confounder selection, loss to follow-up |
| Systematic review / meta-analysis | PRISMA 2020 | Full search strategy, risk-of-bias tool, certainty (GRADE), protocol registration |
| Diagnostic accuracy | STARD 2015 | Reference standard in all participants, blinding, threshold prespecification |
| Prediction model, including AI/ML | TRIPOD+AI | Development vs validation, calibration, sample size, handling of missing data, fairness |
| AI interventions in trials | CONSORT-AI / SPIRIT-AI | Version of the AI, human-AI interaction, input and output handling |
| Case report | CARE | Timeline, diagnostic reasoning and challenges, patient perspective, consent |
| Quality improvement | SQUIRE 2.0 | Context, intervention description, study of the intervention |
| Qualitative | COREQ or SRQR | Reflexivity, sampling and saturation, participant checking |
| Animal research | ARRIVE 2.0 | Sample size, randomization, blinding, exclusions |
| Economic evaluation | CHEERS 2022 | Perspective, time horizon, discount rate, sensitivity analysis |

## 6. Length budgets (defaults when the journal is silent)

AI-assisted drafts usually run long, often several times over these figures. Measure before polishing.

| Unit | Typical budget |
|---|---|
| Abstract | Journal limit (commonly 250 to 300 words) |
| Introduction | 400 to 700 words, 3 to 4 paragraphs |
| Methods | 800 to 1,200 words in the main text; detail to Supplement |
| Results | 500 to 1,000 words excluding tables |
| Discussion | 900 to 1,500 words; Limitations around 200 |
| Case report main text | Commonly 1,500 to 2,500 words (check journal) |
| Results paragraph | One claim and its numbers |
| Discussion paragraph | One point, usually 4 to 8 sentences |

When cutting to a limit, cut in this order: repeated summaries and previews; lower-priority sentences and topics; redundant phrases. Keep actors, comparators, conditions, and outcomes. After shortening, re-read for new pronouns and clause chains (S7, S13). If the limit cannot be met without losing meaning, tell the author the trade-off instead of silently exceeding it or compressing into ambiguity.

## 7. Integrity checklist

Before delivering:
- [ ] Every number, statistic, and citation in the output exists in the input or a retrieved source.
- [ ] Every result in the input still appears (nulls and adverse events included).
- [ ] Verbs match the design for every claim.
- [ ] No spin language; no "significant" without a test.
- [ ] Abstract numbers match the body.
- [ ] Abbreviations expanded at first use.
- [ ] Placeholders listed for the author.
- [ ] If tools are available (PubMed, CrossRef, web search), check that each supplied citation exists and says what the sentence claims. A reference goes into the text only if the user asked for literature or it replaces a citation that does not support its claim; it must have been retrieved and checked, and it is marked `[ADDED: verified, DOI]`. Every other candidate goes in a separate list. Prefer primary sources over reviews for statistics ("telephone game" errors propagate through secondary citations).
- [ ] AI-use disclosure mentioned once if the text is headed for submission.
