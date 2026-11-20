# Audit: introduction.txt

Scope: two-paragraph Introduction (about 155 words). Audit only, no rewrite.
Design implied: single-centre retrospective cohort of 2,914 patients with septic shock, exposure = norepinephrine within 1 hour of shock onset, outcome = 28-day mortality.
Document type: Introduction to an original research manuscript.

## Summary

The paragraph structure is the main problem, not the vocabulary. The background is built from four unattributed generalities, the paper's own result appears in the Introduction, and the section closes with a promise ("pave the way") where an aim and hypothesis should be. Three sentences state the same claim at three different levels of certainty (established fact, "was associated with", "prevents"), and the section contains no citation markers at all. Most of the surface vocabulary issues (pivotal, evolving landscape, comprehensive, pave the way) sit on sentences that should be deleted outright, so fixing words first would waste the effort.

## Findings

| # | Location | Quoted text | Pattern | Severity | Suggested fix |
|---|---|---|---|---|---|
| 1 | ¶1 S1 | "Sepsis remains a leading cause of death worldwide" | D6, D2 | Major | Passes the swap test: it could open any sepsis paper. Either give the specific burden figure with its source, or cut and start with the uncertainty about timing. |
| 2 | ¶1 S1 | ", representing a pivotal challenge in the evolving landscape of critical care" | S1, W1 | Major | -ing tail carrying no data, plus two abstractions ("pivotal", "evolving landscape"). Delete; the sentence is complete without it and loses nothing. |
| 3 | ¶1 S1 | "remains" | W7 | Minor | "remains" + abstract noun is a mild tic. Only worth changing as part of rewriting the sentence anyway. |
| 4 | ¶1 S2 | "In recent years, there has been growing interest in the role of early vasopressor initiation" | D6, D2, W4 | Major | Interest by whom? Replace with the specific state of the evidence (what trials or cohorts have tested timing, with what result), or delete and let the next sentence carry the background. |
| 5 | ¶1 S2, S4 | "early vasopressor initiation"; "delayed vasopressor therapy" | S13 | Major | "Early" and "delayed" have no threshold and no comparator here. The 1-hour cut-off appears only in ¶2. Define the exposure window the first time the concept appears, and say what the comparator is. |
| 6 | ¶1 S3 | "Studies have shown that early norepinephrine improves survival in septic shock" | D2, S6 | Critical | Unnamed studies and a causal verb with no citation. This verb is also inconsistent with your own retrospective design. Name the studies (design, n, effect), or insert [CITATION NEEDED], and use "has been associated with". |
| 7 | ¶1 S4 | "Furthermore, a growing body of evidence suggests" | W5, D2 | Major | Additive opener plus an unnamed body of evidence. If the relation is real (it qualifies the previous sentence), signal it with a connective that carries meaning ("In contrast", "However") or fold both sentences into one. |
| 8 | ¶1 S4 | "may potentially be associated with" | S6 | Major | Two hedges stacked on one claim. One hedge, sized to the observational design. |
| 9 | ¶1 S4 | "in some patients" | S13 | Major | Which patients? Name the subgroup and its result, or delete. As written it weakens the claim without saying anything. |
| 10 | ¶1 S3 with S4 | "improves survival" then "may potentially be associated with worse outcomes" | D9, D7 | Major | Sentences 3 and 4 make the same directional claim twice, at two different certainty levels. Merge into one sentence at one certainty. |
| 11 | ¶2 S1 | The 2,914-patient effect estimate and 95% CI | Structure (section guide §4, §6) | Critical | The Introduction is reporting a study result. Decide whether this manuscript is the retrospective analysis or the prospective study: if the former, the estimate belongs in the Abstract and Results and the Introduction should state the question; if the latter, this result is prior work and needs its own framing and citation. |
| 12 | ¶2 S1 | "at our institution" | S10, S13 | Major | Which centre, what dates, what source population? Also check whether overlapping settings make the study identifiable. A single unnamed centre also limits what the estimate can support later. |
| 13 | ¶2 S1 | "adjusted odds ratio, 0.78; 95% CI, 0.64–0.94" | Statistical reporting | Major | What was adjusted for, and why those covariates? For a 28-day mortality outcome with censoring, an OR from logistic regression discards time to event; consider whether a hazard ratio is the estimate you want. The en dash in the CI is correct typography and should stay. |
| 14 | ¶2 S2 | "Early norepinephrine therefore prevents death in septic shock" | S6, D8 | Critical | A bare causal claim from a single-centre adjusted OR, with a scope leap from your cohort to all septic shock. "Therefore" is doing unsupported work. Either state the association with its scope or move the inference to the Discussion with its uncertainty. |
| 15 | ¶2 S3 | "To address this critical gap" | D4, D2 | Critical | Which gap? The preceding sentence asserts the question is settled, so the paragraph has just closed the gap it now proposes to fill. The gap has to be named and has to exist. |
| 16 | ¶2 S3 | "we designed a comprehensive prospective study" | D4, W2, tense | Critical | Mixes a completed action ("designed") with a future one ("will fill"), and never says what the study will measure, in whom, against what comparator, or with what hypothesis. This is where the aim and hypothesis belong. |
| 17 | ¶2 S3 | "will not only fill an important gap in the literature but also pave the way for improved outcomes" | S3, D5, W1, W2 | Critical | Negative parallelism plus a promise coda. No reader learns anything from it. Delete; replace with the specific aim and the one outcome that will test it. |
| 18 | Whole section | No citation markers anywhere | D2 | Critical | A background paragraph with four evidence claims and zero references. Every one of claims 1, 4 and 6 needs a named source or a [CITATION NEEDED] placeholder. |
| 19 | ¶1 S1 vs ¶2 | "Sepsis" then "septic shock" | S5 | Minor | One term per concept. Fix which population the paper is about and use it from the first sentence. |

## Author queries (content the audit cannot resolve)

1. Is this manuscript the retrospective analysis, or the prospective study the last sentence describes? The Introduction currently belongs to both and states an aim for neither.
2. How is time zero ("shock onset") defined in the data, and how confident are you in that timestamp? This determines whether the 1-hour threshold is measurable and whether immortal-time bias or misclassification is a threat.
3. Why 1 hour rather than 3 or 6? Is the cut-off prespecified, data-driven, or taken from a guideline? If a guideline, cite it.
4. What covariates are in the adjusted model, and were they prespecified?
5. Is logistic regression the right model for 28-day mortality, or did you also fit a Cox model? If both, report the one that matches the hypothesis.
6. Has this retrospective analysis been reported or presented elsewhere? If so, it needs a citation rather than a bare restatement.
7. If you keep the burden-of-disease opening, which source (WHO, GBD, or a sepsis-specific estimate) do you want to cite?

## What to keep

- "was associated with lower 28-day mortality": correctly calibrated to the design. Do not convert this to a causal verb, and do not weaken it further.
- The estimate, 95% CI, sample size, and 28-day endpoint: all correctly formatted, and the en dash in the confidence interval is right.
- The 1-hour exposure window: this is the one specific, falsifiable element in the section. Give it a definition and a rationale and it carries the whole Introduction.

## The five revisions that would most improve the piece

1. **Pick one study and give it an aim.** State which manuscript this is, name the gap in one sentence, and end the Introduction with the question, population, exposure window, comparator, and primary outcome. This single change resolves findings 11, 15, 16 and 17.
2. **Make the verbs match the design.** Keep "was associated with" for your own estimate, remove "improves survival" and "prevents death", and stop stating the same claim at three certainty levels.
3. **Replace every unnamed source with a named one.** "Studies have shown", "growing interest", and "a growing body of evidence" become either cited specifics (design, n, effect) or [CITATION NEEDED].
4. **Move the 2,914-patient result out of the Introduction** and let the Introduction pose the question the result will answer. As written, the result arrives before the reader knows what was asked.
5. **Delete the preamble and the closing promise** ("pivotal challenge in the evolving landscape", "not only fill an important gap but also pave the way"). That removes most of the AI-favored vocabulary as a side effect, without a word-level hunt.
