# Audit: introduction.txt

Read as an IMRaD Introduction. No rewrite, per request. No citations are present in the text, so every reference suggestion is a placeholder.

## Findings

| # | Location | Quoted text | Pattern | Severity | Suggested fix |
|---|---|---|---|---|---|
| 1 | Para 1, sent 1 | "Sepsis remains a leading cause of death worldwide, representing a pivotal challenge in the evolving landscape of critical care." | D6 generic preamble; S1 -ing tail; W1 ("pivotal", "landscape") | Major | Fails the swap test: could open any critical-care paper. Start from the specific known/unknown about vasopressor timing and survival, not disease burden. Drop the "representing..." tail. |
| 2 | Para 1, sent 2 | "In recent years, there has been growing interest in the role of early vasopressor initiation." | D2 vague allusion; D6; W4 ("in recent years") | Major | No named study, design, or number. Replace with a precise gap statement (knowledge gap: no randomized comparison of early versus usual-time initiation with mortality as the outcome [CITATION NEEDED]). |
| 3 | Para 1, sent 3 | "Studies have shown that early norepinephrine improves survival in septic shock." | D2 unnamed "studies", no citation; Integrity rule 3 (causal verb, design unknown) | Critical | Name the study (design, population, n, effect with CI) and match the verb to its design ("was associated with" if observational). As written, the claim has no support. |
| 4 | Para 1, sent 4 | "Furthermore, a growing body of evidence suggests that delayed vasopressor therapy may potentially be associated with worse outcomes in some patients." | D2; S6 stacked hedge ("may potentially"); W5 ("Furthermore" opener); unspecified population | Major | Name the evidence; one hedge sized to the design; specify which patients or cut the qualifier. |
| 5 | Para 2, sent 1 | "In a retrospective analysis of 2,914 patients with septic shock at our institution, norepinephrine started within 1 hour of shock onset was associated with lower 28-day mortality (adjusted odds ratio, 0.78; 95% CI, 0.64–0.94)." | Structure: results in the Introduction; S13 comparator implied, not stated; number formatting (commas after "ratio"/"CI") | Major | The hedge here is correct ("was associated with") and the numbers are good. But move the result to Results, or, if this paper is a prospective protocol, cite the retrospective analysis as prior work. State the comparator (start after 1 hour / usual practice). Drop the commas after "ratio" and "CI". |
| 6 | Para 2, sent 2 | "Early norepinephrine therefore prevents death in septic shock." | Integrity rule 3 (causal verb from observational data); S6 bare causal claim | Critical | Delete. An association does not license "prevents". The most this supports: whether earlier initiation causally reduces mortality is untested, which is the gap the next sentence should actually define. |
| 7 | Para 2, sent 3 | "To address this critical gap, we designed a comprehensive prospective study that will not only fill an important gap in the literature but also pave the way for improved outcomes." | D4 study-as-hero (undefined "gap", twice); D5 "pave the way"; S3 "not only...but also"; D9 restatement; W2 "comprehensive"; mixed tense ("designed... will") | Major | One purpose sentence with the gap defined, then design, population, intervention, and primary outcome. Cut all four flagged phrases. |
| 8 | Whole intro | (no citations anywhere) | Integrity rule 1 / D2 missing support | Critical | Every prior-evidence claim needs a named reference; none is present. Insert [CITATION NEEDED] where a study does not yet exist in your sources, and obtain them before submission. |
| 9 | Whole intro | (no aim or hypothesis sentence) | Section-guide move 3 (known to unknown to question) | Major | The funnel never reaches the question. End with what this study does and how the design addresses the gap. |

## What to keep when you rewrite

- The association sentence and every number in it: 2,914 patients; norepinephrine within 1 hour of shock onset; 28-day mortality; adjusted odds ratio 0.78 (95% CI 0.64 to 0.94).
- The correct hedge "was associated with" on that sentence.
- "Patients" as the single term for the cohort.
- The design label "retrospective analysis" for that study (or whatever the final design statement is).

## The five revisions that would improve this most

1. Kill "Early norepinephrine therefore prevents death in septic shock." It is the one sentence that misstates the evidence (causal verb from observational data).
2. Move the 2,914-patient result out of the Introduction (to Results, or to a cited prior-work sentence if this manuscript is the prospective protocol) and make the comparator explicit.
3. Rebuild paragraph 1: one specific, cited sentence on what is known about vasopressor timing and survival, then the named gap (randomized evidence on whether timing causally affects mortality).
4. Name the studies behind "Studies have shown" and "a growing body of evidence" with design, population, and effect estimate; otherwise [CITATION NEEDED].
5. Replace the final sentence with a purpose statement: prospective design, population, timing of the intervention, primary outcome. No "pave the way", no "not only...but also", no "comprehensive", one "gap", not two.

Note: if this manuscript goes to submission, most journals and ICMJE require disclosure of AI-assisted writing.
