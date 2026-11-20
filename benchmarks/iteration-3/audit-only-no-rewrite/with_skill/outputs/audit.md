# Audit: introduction.txt

Audit only. Nothing here is a rewrite; the "Suggested fix" column says what to change, not what to write.

**Reading taken:** Introduction to a paper or protocol on early norepinephrine in septic shock. The future tense in the last sentence ("will ... fill") suggests a protocol or grant. I assumed the 2,914-patient analysis is your group's prior work, not the results of this paper. No target journal was given, so default conventions apply.

Sentence locations: P1 = first paragraph (s1 to s4), P2 = second paragraph (s1 to s3).

Severity: **Critical** = misleads the reader (wrong verb for the design, unsupported claim, missing result). **Major** = hurts clarity or credibility. **Minor** = style.

## Findings

| # | Location | Quoted text | Pattern | Severity | Suggested fix |
|---|---|---|---|---|---|
| 1 | P1 s1 | "Sepsis remains a leading cause of death worldwide" | D6 generic preamble | Major | This sentence could open any sepsis paper (fails the swap test). Open on vasopressor timing in septic shock. If you keep a burden figure, make it a specific number with a citation; as written it has none. |
| 2 | P1 s1 | ", representing a pivotal challenge in the evolving landscape of critical care" | S1 -ing tail, S2 copula avoidance ("representing"), W1 (pivotal, landscape) | Minor | The clause has no content. Delete all of it; don't swap in synonyms. |
| 3 | P1 s2 | "In recent years, there has been growing interest in the role of early vasopressor initiation." | D6, S9 ("there has been") | Major | Other people's interest isn't evidence. Replace it with what is actually known about timing: who studied it, what design, what they found, cited. |
| 4 | P1 s3 | "Studies have shown that early norepinephrine improves survival in septic shock." | D2 vague allusion; causal verb with no design or citation behind it (Integrity rules 1 and 3) | **Critical** | This is a specific causal claim with no citation and no named study. "Improves survival" needs randomized evidence on mortality. The one randomized trial I checked did not find a 28-day mortality difference (see "Candidates to verify" below), so the claim seems to overstate the evidence. It also undercuts your own rationale: if a survival benefit were already established, there would be no gap to fill. Name the studies, their designs and effect estimates, and match the verb to each design. |
| 5 | P1 s4 | "Furthermore, a growing body of evidence suggests that delayed vasopressor therapy may potentially be associated with worse outcomes in some patients." | D2; S6 stacked hedge (suggests + may + potentially + "some patients"); S13 compressed meaning; D9 restatement; W5 | Major | This restates s3 from the other side (early helps / delayed harms). Merge the two into one cited account of the evidence. Use one hedge, sized to the design. Say which outcomes, how much delay, and which patients. |
| 6 | P1 s3 to s4 | "improves survival" vs "may potentially be associated with worse outcomes" | D7 uncalibrated certainty | Major | One claim, stated at full certainty in one sentence and heavily hedged in the next. Each statement's certainty should follow the design of the study behind it. Fixing #4 and #5 resolves this. |
| 7 | P2 s1 | "In a retrospective analysis of 2,914 patients ... (adjusted odds ratio, 0.78; 95% CI, 0.64–0.94)." | Source and placement unclear; incomplete reporting | Major | "Was associated with" is the right verb here; keep it. Three problems: (a) no citation. Cite it if published, or label it unpublished data. (b) If these are this manuscript's own results, they go in Results, not the Introduction. (c) Readers will want to know what the model adjusted for, and the absolute 28-day mortality in each group. |
| 8 | P2 s2 | "Early norepinephrine therefore prevents death in septic shock." | Causal verb from observational data (Integrity rule 3, S6); D9 restatement | **Critical** | The sentence before it can't support "prevents". Early versus late norepinephrine in a retrospective cohort is open to confounding by indication (earlier recognition, care setting, illness severity) and to bias from how the 1-hour window and shock onset were defined. Delete the sentence. The gap between this association and a causal answer is the strongest rationale your intro has (see #9). |
| 9 | P2 s3 | "To address this critical gap" | D4 study-as-hero; dangling referent; W3/W1 ("critical") | Major | No gap has been named anywhere in the text, so "this gap" points at nothing. State the gap explicitly and give its type (knowledge, methods, or population). The section guide template is: although [known], [unknown], which matters because [consequence]. Given your material, the gap is probably that the mortality evidence is retrospective and associational, and no trial was powered for mortality [CITATION NEEDED: confirm against current trial literature]. |
| 10 | P2 s3 | "we designed a comprehensive prospective study" | S13 compressed meaning; W1 ("comprehensive", vague) | Major | The reader still can't tell what the study is. Say whether it is randomized or observational, the population, early versus what comparator, and the primary outcome. Then give the aim or hypothesis in one sentence ("We tested whether..."). |
| 11 | P2 s3 | "that will not only fill an important gap in the literature but also pave the way for improved outcomes" | S3 negative parallelism; D4; D5 reassuring coda; W1 ("pave the way"); "gap" used twice in one sentence | Major | This is a promise, not content. End the Introduction on the aim and design and delete this clause. |
| 12 | Whole text | Only favorable evidence is presented | D3 tidy causal story | Major | Every cited line of evidence points the same way. A null mortality result from randomized evidence (see below) is the main reason a new prospective study is needed, so leaving it out weakens your rationale. Report it plainly. |
| 13 | Whole text | Structure: known, then own data, then "gap" | Section moves (Introduction: known, unknown, question) | Major | The "unknown" and the "question" moves are both missing. The fixes for #9 and #10 supply them. At 138 words this is short for an Introduction (usual range 400 to 700). That is fine if it's an excerpt, but the missing moves matter more than the length. |

**Counts:** 2 Critical, 10 Major, 1 Minor.

## What is already fine (leave it)

- "was associated with lower 28-day mortality" (P2 s1): correct verb for a retrospective cohort. Don't swap it for "linked to" or a causal verb.
- The effect estimate format (adjusted OR with 95% CI) and the en dash in "0.64–0.94": correct.
- The exposure definition ("within 1 hour of shock onset") and outcome ("28-day mortality") are specific. This is the most concrete material in the draft. Build the rewrite around it.
- No em dashes, and sentence rhythm is not a problem (the checker found no uniform paragraph). Don't spend effort there.

## Five revisions that would help most

1. **Remove both causal claims** (P1 s3 "improves survival", P2 s2 "prevents death"). For observational data, "was associated with" is the ceiling.
2. **Replace the unnamed evidence** ("Studies have shown", "a growing body of evidence") with named, cited studies, giving design, population, and effect estimate for each. Include the null mortality result from randomized evidence.
3. **Name the gap explicitly.** The case your material supports: retrospective data show an association, and the randomized mortality evidence is limited or null. That is why a prospective study is needed.
4. **State the question and design** in place of the final sentence: design, population, comparator, primary outcome, and the hypothesis. Delete "not only ... but also pave the way".
5. **Cut the opener** (P1 s1 to s2) and start with vasopressor timing. While restructuring, decide where the 2,914-patient analysis belongs and cite it.

## Candidates to verify (not inserted anywhere)

- Retrieved from PubMed: Permpikul C, et al. Early Use of Norepinephrine in Septic Shock Resuscitation (CENSER). A Randomized Trial. *Am J Respir Crit Care Med.* 2019;199(9):1097-1105. [doi:10.1164/rccm.201806-1034OC](https://doi.org/10.1164/rccm.201806-1034OC). Single-centre, double-blind, placebo-controlled phase II trial of 310 adults with sepsis and hypotension. The primary outcome, shock control by 6 hours, was higher with early norepinephrine (76.1% vs 48.4%). 28-day mortality did not differ (15.5% vs 21.9%; P = 0.15). This bears directly on findings #4 and #12. It is one trial from one targeted search, not a literature review; please do your own search before citing.

## Note

If any AI tool helped draft this text, most journals and the ICMJE recommendations require disclosure of AI-assisted writing at submission.
