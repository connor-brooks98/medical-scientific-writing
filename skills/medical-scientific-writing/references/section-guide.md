# Section and document guide

How each kind of medical and scientific document is built, and where the AI patterns most often show up in each. The target journal's instructions override everything here.

## Contents

1. Tense and voice table
2. Title
3. Abstract
4. Introduction
5. Methods
6. Results
7. Discussion and conclusion
8. Case reports (CARE)
9. Review articles (narrative and systematic)
10. Grant specific aims and significance
11. Cover letters
12. Responses to reviewers
13. Conference abstracts and posters
14. Lay summaries and plain-language text
15. Letters, commentaries, editorials

---

## 1. Tense and voice

| Content | Tense | Example |
|---|---|---|
| Established fact, known mechanism | Present | "Metformin lowers hepatic glucose output." |
| A body of prior work | Present perfect | "Several trials have tested..." |
| A specific prior finding | Past | "Lee et al. found..." |
| Your aim or hypothesis | Past ("aimed", "hypothesized") | "We hypothesized that..." |
| What you did (Methods) | Past | "We enrolled...", "Blood was drawn..." |
| What you found (Results) | Past | "Mortality was 12%." |
| What a table or figure shows | Present | "Table 2 shows..." |
| Your interpretation, general conclusion | Present | "These data suggest..." |
| Speculation, future work | Modal | "may", "could", "would" |

Voice: active where the actor matters ("We excluded 14 patients because..."), passive acceptable in Methods where the procedure matters more than who did it. Choose and stay consistent within a section. "We" is accurate, not informal; avoiding it does not make science more objective.

## 2. Title

- Specific and informative: population, exposure or intervention, outcome, and design where relevant. Typically 10 to 15 words (rarely over 20).
- No waste words: "A study of", "An investigation into", "Observations on", "Novel", "Comprehensive".
- Abbreviations only if universal (DNA, MRI, HIV).
- Case reports: include "case report" (CARE).
- AI tell: titles built on a colon plus a rhetorical flourish ("Beyond the Heart: Unraveling the Multifaceted Role of...").

## 3. Abstract

Write it last. It must stand alone and agree exactly with the paper (numbers, outcomes, conclusions).

- Follow the journal's structure (structured: Background, Methods, Results, Conclusions; or unstructured prose).
- Background: the specific problem and gap in one or two sentences; no burden-of-disease boilerplate unless it carries a needed number.
- Methods: design, setting, population, intervention or exposure, primary outcome, main analysis.
- Results: the primary result with effect estimate and 95% CI, then key secondary results, **including null and adverse ones**. If the abstract reports the best subgroup, it reports the worst.
- Conclusions: what the primary result means within its scope. No new claims, no "promising", no "further research is needed".
- No citations; define abbreviations at first use; stay within the limit.
- Check alignment: if Methods mentions three outcomes, Results reports three or Methods drops the extras.

## 4. Introduction

Three to four short paragraphs moving from known to unknown to the question. Not a literature review.

1. **What is known** about the *specific* relationship under study (not the disease in general). Cite specifics: design, population, magnitude.
2. **What is not known**, and why it matters. Use a gap of a named type:
   - Knowledge: "No study has measured X in Y."
   - Methodological: "Previous studies of X relied on self-report / single centres / short follow-up."
   - Population: "X has not been examined in Y."
   A useful template: "Although [known], [unknown], which matters because [consequence]."
3. **The question and approach**: "We tested whether...", "We aimed to determine...", "Our hypothesis was...". State briefly how the design addresses the gap.

Rules: do not present results; do not over-cite (representative citations, not exhaustive lists); do not open with a generic preamble (D6); name the gap precisely ("more research is needed" is not a gap).

AI traps here: D6 generic opener, D2 unnamed "studies", D4 "to address this critical gap", W1 vocabulary density.

## 5. Methods

Purpose: a competent colleague could repeat the study. Clear, complete, not discursive.

Typical order (adapt to design and journal): ethics approval and consent; design and setting; participants (eligibility, recruitment, dates); intervention or exposure (generic drug names, dose, route, schedule); outcomes (primary and secondary, exact definitions, timing, adjudication); data collection; sample size (assumptions); statistical analysis (named tests, models and covariates, handling of missing data, multiplicity, software and version, prespecified vs post hoc); AI or LLM use disclosure if the journal places it here.

Rules:
- Cite rather than restate standard or previously published methods ("as previously described (ref)").
- Never "standard statistical methods were used".
- Put long parameter lists, search strategies, and code-level detail in tables or the Supplement, cited at the point of removal.
- No rationale for standard choices, no pedagogy (D10).
- Name the reporting guideline followed and actually satisfy its items.

## 6. Results

Purpose: what was found, in the order of Methods, without interpretation.

- Open with participant flow and baseline characteristics (Table 1).
- Then the primary outcome, then secondary outcomes (all of them, including null), then safety and adverse events, then prespecified subgroup and sensitivity analyses, then exploratory analyses labelled as such.
- **Lead with the finding, not the test**: "Expression increased 3.2-fold in treated cells (P = 0.003; Fig. 1b)", not "A paired t-test revealed a significant difference...".
- Summarize tables, don't read them aloud. Point out the main contrast and one or two key numbers; cite the table. Each datum appears in one place: text, table, or figure.
- Give effect estimates with 95% CIs, not only p values.
- Reserve "significant" for statistical significance.
- No "why" sentences, no literature comparison, no rationale for analyses.

AI traps here: S1 -ing interpretation tails, W2 adjectives on favorable results, D8 asymmetric phrasing of subgroups, D3 missing nulls.

## 7. Discussion and conclusion

An inverted funnel: start narrow with the answer, broaden to context and meaning.

1. **Answer the question in the first sentence or two.** "In this cohort of 4,812 adults, X was associated with Y (effect, CI)." Do not restate the Introduction.
2. **Relate to prior evidence.** Studies that agree, studies that disagree (with plausible methodological or population reasons, not "they were wrong"), and what this study adds. Name the studies (D2).
3. **Mechanism, if supported**, with certainty labelled: "Our data show...", "These findings suggest...", "One possible mechanism is...", "We speculate...". Skip if purely speculative.
4. **Strengths, then limitations.** Specific and consequential, not generic. For each limitation: what it is, how it could bias the result and in which direction. No rebuttal sentence after it (D8). "The sample of 40 gives 80% power to detect only d ≥ 0.45" is a limitation; "the small sample size" is a placeholder for one.
5. **Implications.** For practitioners: who would use this, in which setting, at which step, and what action it would trigger. For researchers: the specific next study (design, population, outcome).
6. **Conclusion** (often the final paragraph, or a separate section): the main finding with its scope and the one implication it supports. Two to four sentences. No new data, no promise language, no "more research is needed".

Pros and cons: group the arguments rather than alternating ("bait and switch") sentence by sentence.

AI traps here: D1 morals at paragraph ends, D3 single mechanism, D4 study-as-hero, D5 coda, D7 every paragraph the same shape, D8 limitation rebuttals, W5 "Notably" stacks.

## 8. Case reports (CARE)

A case report earns publication by teaching something: an unusual presentation, a diagnostic pitfall, an unexpected adverse event, a new association, a management lesson. Write the teaching point down before drafting, as one specific sentence.

Structure (CARE checklist; confirm against the journal):
- **Title** including "case report" and the key feature.
- **Abstract**: introduction (why the case matters), case presentation (key findings, diagnosis, intervention, outcome), conclusion (the specific lesson).
- **Introduction**: one short paragraph on why this case is worth reading, with the specific background needed. Not a review of the disease.
- **Patient information**: de-identified demographics, relevant history, comorbidities, medications, family and psychosocial history as relevant.
- **Clinical findings** and **timeline** (a table or figure for anything beyond a few days).
- **Diagnostic assessment**: tests with values and reference ranges, the differential diagnosis, the reasoning, and **diagnostic challenges or errors**. This is often the most instructive part and the part AI drafts most often flatten (D3).
- **Therapeutic intervention**: drug (generic name), dose, route, duration, changes and why.
- **Follow-up and outcomes**: clinician- and patient-assessed outcomes, adherence and tolerability, adverse events, duration of follow-up.
- **Discussion**: relevant literature (named cases or series, with what they found), what is new here, the rationale for your conclusions, strengths and limits of inference from one patient.
- **Patient perspective** (where the journal includes it) and **informed consent** statement.

Past tense, chronological, explicit time intervals ("on day 3", "6 weeks after"), lab values with units and reference ranges.

Case-report-specific AI traps:
- The closing moral: "This case highlights the importance of a high index of suspicion..." (D1). Replace with the concrete lesson or delete.
- "To our knowledge, this is the first reported case" without a stated search (databases, terms, date). Either describe the search or drop the claim.
- "Rare but potentially life-threatening" stock framing without an incidence figure and citation.
- A diagnostic course written as a straight line, omitting the wrong turns (D3).
- Generalizing from one patient: "demonstrates the efficacy of", "should be considered first-line". One case supports "raises the possibility" or "suggests considering".
- A literature review that lists cases by vague allusion ("several cases have been reported") instead of naming them and their relevant details.

## 9. Review articles

**Narrative review.** Its value depends on a clearly bounded thesis ("Exercise-associated hyponatremia in endurance athletes: mechanisms and prevention", not "Hyponatremia"). Organize by theme or question, not by paper. For each section: what is known, what is contested, what would resolve it. Synthesize and critique, don't summarize paper by paper. Tables for study characteristics. The conclusion states the answer to the thesis and the specific open questions. AI traps: D6 generic openers per section, D2 unnamed evidence, W1 vocabulary, D11 "Challenges and Future Perspectives" scaffolding, false balance (every topic "remains controversial").

**Systematic review and meta-analysis.** Follow PRISMA 2020: registered protocol, full search strategy for at least one database, eligibility criteria, dual screening and extraction, risk-of-bias tool (RoB 2, ROBINS-I, QUADAS-2), synthesis method, heterogeneity (I², tau²), certainty of evidence (GRADE), flow diagram. Write the certainty of evidence into the conclusions ("low-certainty evidence suggests...").

## 10. Grant specific aims and significance

Specific Aims page (one page, NIH-style; adapt to the funder):
1. The problem and why it matters, in two or three sentences with one specific number.
2. What is known, what is not, and the critical barrier.
3. The long-term goal, the objective of this proposal, the central hypothesis, and the rationale (preliminary data in one or two sentences with numbers).
4. Two to four aims, each with a testable hypothesis and the approach in one or two sentences. Aims should not depend on each other's success.
5. Expected outcomes and the positive impact, stated specifically.

Significance and approach: specific, quantified, honest about pitfalls with alternative approaches. Grant writing is persuasive, but persuasion comes from specificity, feasibility, and preliminary data, not adjectives. AI traps: "innovative" and "transformative" used as self-description, triads of benefits, "paradigm shift", promise-shaped impact statements (D5).

## 11. Cover letters

Four short paragraphs:
1. What you submit (title, article type, journal) and the central finding with its key number.
2. Why it matters to *this journal's* readers, connected to the journal's stated scope (and, if apt, to a specific recent article in the journal).
3. Required statements: originality, no concurrent submission, all authors approved, competing interests, ethics or trial registration if required, AI-use disclosure if required.
4. Suggested or opposed reviewers if the journal asks.

No hype ("groundbreaking"), no flattery of the journal, no full summary of the paper. Sound like judgment, not marketing.

## 12. Responses to reviewers

- One brief thank-you at the top. Then every comment, numbered, quoted or paraphrased exactly, each followed by a response.
- Each response says what was changed and where (section and line numbers), and quotes the new text when it is short.
- When you disagree, give the scientific reason and evidence, and offer a compromise where possible (a clarifying sentence, a sensitivity analysis, a limitation).
- Name the actor: "We have added...", "We reanalysed...", not "The revised manuscript now addresses...".
- AI traps: "We thank the reviewer for this insightful and valuable comment" before every response (W8), defensive framing, vague "we have revised accordingly" with no location.

## 13. Conference abstracts and posters

- Abstract: tight word limit, so every sentence carries a number or a decision. Background in one sentence, methods in two, results with the primary estimate and CI, one-sentence conclusion within scope.
- Poster: the take-home message as the title or a headline sentence; figures carry the story; text in short paragraphs, not bullets of fragments; one clear take-home statement near the top.

## 14. Lay summaries and plain-language text

For patients, the public, press releases, or plain-language summaries required by journals and funders:

1. **Start with the take-home message.** Reverse the scientific order: what was found and why it matters first, then what was done.
2. **Recognize and remove jargon**, including "scientist-speak" ("cohort", "significant", "associated with" may all need translation).
3. **Explain the science without hand-waving.** You must understand it well enough to explain each step.
4. **Filter detail by layer**: big picture (treatment better than placebo) and critical details (how many people, how long, how big the effect) almost always; other meaningful details if space allows; technical and trivial details out.
5. **Get to the point faster** and trust the reader's intelligence.
6. **Keep the uncertainty honest.** "People who took X had fewer strokes, but this kind of study cannot show that X caused the difference."

For instructions (patient handouts, protocols, consent procedures), use plain-English rules: one instruction per sentence, condition before action, 20 words or fewer per instruction, 25 or fewer per descriptive sentence, one name per thing (see `clarity-toolkit.md`).

AI traps: inflated reassurance, "groundbreaking new study", false certainty, analogies that distort the mechanism.

## 15. Letters, commentaries, editorials

Usually 500 to 1,500 words with few references. One argument, stated in the first paragraph, supported by specific evidence, with the counter-argument addressed directly. Opinion is expected here, but it must be the author's, and it must be stated as a position with reasons, not as a string of evaluative adjectives.
