# Audit: introduction.txt

Scope: audit only, no rewrite. Read as the Introduction to a primary-research manuscript (or protocol) on early norepinephrine in septic shock. One structural ambiguity affects several findings below and is listed first as an author query.

**Author query that changes the audit:** the second paragraph reports a retrospective analysis of 2,914 patients "at our institution" with an effect estimate, then says "we designed a comprehensive prospective study that will...". I cannot tell whether (a) the retrospective analysis is your prior published work, cited as motivation for the new prospective study, or (b) it is the present study, in which case the future tense and the "prospective" label are wrong. If (a), the analysis needs a citation and the estimate probably belongs in compressed form or not at all. If (b), the results do not belong in the Introduction at all, and the whole second paragraph needs to be rebuilt as a question-and-approach paragraph. Findings 3, 4, and 12 depend on which reading is correct.

## Findings

| # | Location | Quoted text | Pattern | Severity | Suggested fix (action, not replacement prose) |
|---|---|---|---|---|---|
| 1 | ¶2, sentence 2 | "Early norepinephrine therefore prevents death in septic shock." | S6, evidence-matched verbs; integrity rule 3 | Critical | Delete the causal claim. A single retrospective adjusted odds ratio cannot support "prevents death", and "therefore" asserts an inference the design does not license. If you keep an interpretive sentence here at all, restrict it to association and to the population studied; better, remove interpretation from the Introduction entirely and let the gap statement carry the paragraph. |
| 2 | ¶1, sentence 3 | "Studies have shown that early norepinephrine improves survival in septic shock." | D2; unsupported causal claim | Critical | Name the studies (design, population, n, effect) with citations, and match the verb to each design. As written this is an unattributed causal claim; an editor will read it as either uncited or overread from observational data. If no supporting trial exists, say what the evidence actually is and mark the claim `[CITATION NEEDED]` rather than asserting it. |
| 3 | ¶2, sentence 1 | "In a retrospective analysis of 2,914 patients with septic shock at our institution, norepinephrine started within 1 hour of shock onset was associated with lower 28-day mortality (adjusted odds ratio, 0.78; 95% CI, 0.64–0.94)." | Section guide (Introduction presents no results); D2 if prior work | Critical (conditional) | Resolve the author query above. If this is your prior work, cite it and reduce it to the specific finding that motivates the new study. If it is the present study, move it to Results/Abstract. Either way an uncited institutional dataset with a full effect estimate reads as a result smuggled into the Introduction. |
| 4 | ¶2, sentence 3 | "we designed a comprehensive prospective study that will not only fill an important gap in the literature but also pave the way for improved outcomes" | Missing third Introduction move; D4; D5 | Critical | The Introduction never states the question, the hypothesis, or the approach. Replace this sentence with the actual aim: design, population, exposure and comparator, primary outcome, and timing. Right now a reader finishes the Introduction unable to say what the study tests. |
| 5 | ¶2, sentence 3 | "To address this critical gap" / "fill an important gap in the literature" | D4; D9 | Major | No gap has been named anywhere in the text, so "this critical gap" has no referent. State the gap explicitly and by type (knowledge, methodological, population) in the preceding sentence, then state it once. The two gap phrases in one sentence are also a restatement. |
| 6 | ¶1, sentence 4 | "a growing body of evidence suggests that delayed vasopressor therapy may potentially be associated with worse outcomes in some patients" | D2; S6 (stacked hedges); S13 | Major | Name the evidence and cite it. Strip the hedge stack to one hedge sized to the design ("suggests that... may potentially be associated with" is three). Specify which patients and which outcomes; "some patients" and "worse outcomes" are uncheckable. |
| 7 | ¶1, sentences 3–4 | "early norepinephrine improves survival" / "delayed vasopressor therapy may... be associated with worse outcomes" | D3; D8 | Major | Both sentences point the same way and no counter-evidence or uncertainty appears. If trials or cohorts disagree, or if the retrospective association is vulnerable to confounding by indication or to time-related bias (patients who die earliest have least opportunity to receive norepinephrine), name that here as the reason a prospective study is needed. That is the strongest available motivation and it is currently missing. Do not invent citations; mark what you need. |
| 8 | ¶2, sentence 1 | "within 1 hour of shock onset" | S13; STROBE exposure definition | Major | "Shock onset" is not defined and is the crux of the whole question. Say how onset was identified retrospectively (first hypotension, lactate, clinician recognition, chart timestamp) and whether the 1-hour window runs from onset or from recognition. Without this the estimate is uninterpretable and the gap cannot be located. |
| 9 | ¶2, sentence 1 | "lower 28-day mortality (adjusted odds ratio, 0.78; 95% CI, 0.64–0.94)" | Statistical reporting; S13 | Major | An odds ratio describes odds, not mortality risk; either report the event rates in both groups alongside the OR or reword the outcome claim. State what the model adjusted for, or cite the source that does. No absolute rates appear anywhere in the Introduction. |
| 10 | ¶1, sentence 1 | "Sepsis remains a leading cause of death worldwide, representing a pivotal challenge in the evolving landscape of critical care." | D6; S1; S2; W1 | Major (first clause); Minor (wording) | Fails the swap test: this could open any critical-care paper. Narrow to the specific contested relationship within one sentence. If you keep a burden figure, give a number and a citation. Delete the ", representing..." tail (it adds nothing) and the vocabulary "pivotal" and "evolving landscape". |
| 11 | ¶1, sentence 2 | "In recent years, there has been growing interest in the role of early vasopressor initiation." | D6; W4; D2 | Major | Carries no information: no time frame, no source, no content. Replace with the specific thing that changed (a trial, a guideline position, a practice shift) and cite it, or cut the sentence and let sentence 3 open. |
| 12 | ¶2, sentence 3 | "a comprehensive prospective study" | D10; W1 | Major | "Comprehensive" is自我评价, not design. Name the design instead (single-centre cohort, randomized trial, stepped-wedge, registry-embedded trial) and the primary outcome. Whether the present work is a protocol or a completed study also needs to be settled; see the author query. |
| 13 | ¶1 vs ¶2 | "early vasopressor initiation" / "early norepinephrine" / "delayed vasopressor therapy" | S5 | Minor | Fix one term per concept. Vasopressors as a class and norepinephrine specifically are not interchangeable exposures; decide which the paper is about and use it consistently, including in the definition of "early". |
| 14 | ¶2, sentence 3 | "will not only fill an important gap in the literature but also pave the way for improved outcomes" | S3; D5; W1 | Minor (form); Major (already counted at #4) | Negative parallelism plus a promise-shaped coda. Delete rather than rephrase; the aim statement required at #4 takes its place. |
| 15 | ¶1, sentence 4 | "Furthermore," | W5 | Minor | The relation is not additive but evidential; either name the real relation to the preceding claim or drop the connective and let the cited evidence follow. Do not leave the sentences merely juxtaposed. |
| 16 | ¶2, sentence 1 | "0.64–0.94" | W6; number formatting | Minor | En dash in a CI range is fine if the journal uses it; check the target journal and use one CI format throughout ("0.64 to 0.94" vs "0.64–0.94"). Also confirm the journal's style for "adjusted odds ratio" vs "aOR" at first use. |

## What is missing rather than wrong

The draft is about 155 words in two paragraphs, well under a typical 400 to 700-word Introduction. Padding is not the main problem here; absent content is. Before rewriting, decide:

1. **The gap, named.** What specifically is unknown, and of what type? Given the material present, the honest candidates are methodological (retrospective timing of onset, confounding by indication, no randomized comparison) rather than a blank spot in the literature.
2. **The question and approach.** Design, population, exposure and comparator, primary outcome and time point, and how the design addresses the named gap.
3. **Named prior evidence.** At least one or two specific studies with design, population, and effect, cited. The Introduction currently contains zero citations for three evidence claims.
4. **The counterweight.** Any trial or cohort that did not find benefit, and the specific bias that makes the retrospective estimate uncertain. This is what earns the prospective study.
5. **A reporting guideline.** STROBE if observational, CONSORT (or SPIRIT for a protocol) if randomized; this determines what the aim sentence must specify.

## Five revisions that would most improve the piece

1. Delete "Early norepinephrine therefore prevents death in septic shock" and stop interpreting results in the Introduction (#1).
2. Settle whether the 2,914-patient analysis is prior work or the present study, then cite it or move it out of the Introduction (#3, author query).
3. Replace the final sentence with a real aim: design, population, exposure/comparator, primary outcome, timing (#4, #12, #14).
4. Name the gap explicitly and once, immediately before the aim, and make it a methodological gap grounded in the limits of the retrospective estimate (#5, #7, #8).
5. Replace both vague allusions with named, cited studies and one calibrated verb each; cut the generic first two sentences so the paragraph reaches the contested question by sentence two (#2, #6, #10, #11).

## Placeholders to insert while rewriting

- `[CITATION NEEDED: studies supporting an effect of early norepinephrine on survival, with design and effect size]`
- `[CITATION NEEDED: evidence on delayed vasopressor timing and outcomes, specifying population and outcome]`
- `[CITATION NEEDED: source of the 2,914-patient retrospective analysis, if prior work]`
- `[DATA NEEDED: definition of septic shock onset and how it was timed]`
- `[DATA NEEDED: 28-day mortality rates in each timing group; covariates in the adjusted model]`
- `[DATA NEEDED: design, population, comparator, and primary outcome of the prospective study]`
- `[CITATION NEEDED: sepsis mortality burden figure, if a burden opening is retained]`

No text was rewritten and no facts, numbers, or citations were added. All quoted material is verbatim from introduction.txt.
