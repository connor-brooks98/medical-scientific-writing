# Audit: introduction.txt

**Reading taken:** Introduction section of an original research article on early norepinephrine in septic shock, describing a single-centre retrospective analysis (n = 2,914). Journal unknown. Audit only: no rewrite is proposed; "suggested fix" columns give direction, not replacement wording. I have no literature-search tool here, so no citation is verified and every literature claim is marked `[CITATION NEEDED]` rather than filled.

## Summary

There are two structural problems and one integrity problem. Structurally, the paragraph never states a gap or a hypothesis, and the Introduction contains the study's own result, which belongs in Results. The integrity problem is the sentence "Early norepinephrine therefore prevents death in septic shock": a causal claim from a retrospective single-centre association, which contradicts the "associated with" in the sentence before it. On top of that sit the familiar surface patterns: a generic first sentence, three unnamed literature claims with no citations at all, a stacked hedge, and a closing sentence built from negative parallelism and promise language. The prose is clean at the sentence level and the study has real data; the material just needs to be in a different order and pointed at a question.

## Mechanical checks (by hand; no script run)

- Approximately 190 words, 2 paragraphs, 7 sentences. Length is not a problem.
- Reference markers: **0**. Numbers present: 2,914; 1 hour; 28-day; 0.78; 0.64–0.94.
- Em dashes: 0. Curly quotes: 0. The confidence interval uses an en dash, which is fine if used consistently (journal-dependent).
- Connectives: "In recent years" and "Furthermore" as openers; one is a real addition, the other is not.
- Hedge stacks: 1 ("may potentially be associated").
- Candidate vocabulary: pivotal, evolving landscape, growing interest, growing body of evidence, critical gap, comprehensive, fill an important gap, pave the way.
- No abbreviations needing expansion, unless OR is introduced in the rewritten text.

## Findings

| # | Location | Quoted text | Pattern | Severity | Suggested fix |
|---|---|---|---|---|---|
| 1 | P1 S1 | "Sepsis remains a leading cause of death worldwide" | D6, D2 | Major | Burden claim with no number and no source, and it could open any sepsis paper. Either give the specific figure with a citation, or start with the timing question the study actually addresses. |
| 2 | P1 S1 | ", representing a pivotal challenge in the evolving landscape of critical care" | S1, W1, W2 | Major | -ing tail that adds nothing after "worldwide"; "pivotal" and "evolving landscape" are evaluation, not information. Delete. |
| 3 | P1 S2 | "In recent years, there has been growing interest in the role of early vasopressor initiation" | D2, W4 | Major | Whose interest, measured how? No citation, no study, no finding. Replace with the specific prior findings, cited, or with the specific uncertainty. |
| 4 | P1 S3 | "Studies have shown that early norepinephrine improves survival in septic shock" | D2, verb–design mismatch | **Critical** | No study named, no design, no population, no time threshold, no effect size, no citation; and "improves" is causal. Name the study, its design, the population, the threshold used, the estimate, with the citation, and let the verb match the design. |
| 5 | P1 S4 | "Furthermore" | W5 | Minor | The sentence that follows is not an addition (see #7). If it is kept as a real second point, a relation word other than "furthermore" is probably needed. |
| 6 | P1 S4 | "a growing body of evidence suggests" | D2 | **Critical** | Unnamed evidence with no citation. Same fix as #4. |
| 7 | P1 S4 | "may potentially be associated with" | S6 | Major | Two or three hedges stacked on one claim. One hedge, sized to the design of the study being described. |
| 8 | P1 S4 | "worse outcomes in some patients" | S13 | Major | Which outcomes (mortality, AKI, ICU length of stay?), which patients, and how is "delayed" defined? Name them. |
| 9 | P1 S3–S4 as a pair | "early norepinephrine improves survival" / "delayed vasopressor therapy … worse outcomes" | D9, D3 | Major | The same timing relation stated twice, mirrored (early helps / late harms). Say it once. The mirrored form also implies a graded dose–response that the cited work may not have shown. |
| 10 | P1 throughout | "early vasopressor initiation" / "early norepinephrine" / "delayed vasopressor therapy" | S5, S13 | Major | The exposure is never operationalized: which agent(s), from what time zero (shock onset? triage? first hypotension?), within what interval. The term also cycles between the drug class and one drug. Choose one term and one definition and use them throughout; the 1-hour threshold should not appear for the first time in P2. |
| 11 | P1 as a whole | (no gap sentence) | Gap not stated | **Critical** | The paragraph ends on consensus, so there is no stated reason for the study. Add a gap of a named type (no study has X in Y; prior work relied on Z; X has not been examined in Y) before the objective. |
| 12 | P2 S1 | "In a retrospective analysis of 2,914 patients with septic shock at our institution, norepinephrine started within 1 hour … (adjusted odds ratio, 0.78; 95% CI, 0.64–0.94)." | Results in the Introduction | **Critical** | The Introduction reports the study's own primary result. It belongs in Results and the Abstract, and it makes the "gap" framing incoherent: the analysis is already done, so the paper cannot be filling a gap it has just closed. Move it; keep the numbers intact for Results. |
| 13 | P2 S1 | "at our institution" | S10, S13 | Minor | Single-centre provenance belongs in Methods; "our institution" is imprecise, and naming the site in a blinded review is avoidable. |
| 14 | P2 S1 | "(adjusted odds ratio, 0.78; 95% CI, 0.64–0.94)" | Statistical reporting | Major | No absolute event rates (odds ratios exaggerate when the outcome is common), and the adjustment set is unstated. Wherever this sentence ends up, give risk in each group plus the adjusted estimate, and state what was adjusted for (in Methods, at minimum). |
| 15 | P2 S1 | "within 1 hour of shock onset" | S13 | Major | The 1-hour cut-off appears without rationale or citation, and the justification cannot live in the Introduction once the result is moved out. Prespecification and reasoning belong in Methods, with the Intro's definition of "early" matching it. |
| 16 | P2 S2 | "Early norepinephrine therefore prevents death in septic shock" | Wrong verb for design, S6, spin | **Critical** | A retrospective single-centre association cannot support "prevents," "therefore" asserts causation, and it contradicts "was associated with" one sentence earlier. The estimate is an adjusted OR of 0.78; "prevents death" is more than the number can carry. State the association with its estimate, or drop the sentence. |
| 17 | P2 S3 | "To address this critical gap" | D4 | Major | The gap was never specified, so "critical gap" points at nothing. State the gap (#11) and refer to it. |
| 18 | P2 S3 | "a comprehensive prospective study" | W1, W2 | **Critical** | "Comprehensive" is unsupported self-praise, and "prospective" contradicts the retrospective analysis described in the previous sentence. The reader cannot tell what this paper reports. Resolve the design question first (see author queries), then state the design once, plainly. |
| 19 | P2 S3 | "will not only fill an important gap in the literature but also pave the way for improved outcomes" | S3, D4, D5, W1 | **Critical** | Negative parallelism + study-as-hero + promise coda, with no content in any of the three parts. Replace with what the study did (design, population, exposure, outcome) and the one question it answers; drop "important gap" and "pave the way." |
| 20 | P2 S3 | "we designed" … "will" | Tense | Minor | Objectives in an Introduction are conventionally past tense ("we aimed to determine whether…"), with future/present reserved for what the paper shows. The mixture also reinforces the design confusion in #18. |
| 21 | Whole file | (no citations anywhere) | D2 | **Critical** | Every literature claim in the piece is unattributed. Each needs a citation to a primary source, with design and effect, not a review. |
| 22 | Whole file | (no hypothesis or objective) | Missing move | Major | No sentence states exposure (with threshold), population, time zero, and outcome, so the reader cannot tell what is being tested even after reading twice. |
| 23 | P1 S3–S4 | "improves survival" | D3, D8 | Major | The literature is presented as uniformly favorable to early vasopressors. If any trial or cohort found no benefit, no difference, or harm (for example where vasopressors were started without measured hypoperfusion, or where diagnostic uncertainty was high), it has to appear here. Asymmetry in the Introduction signals advocacy before the reader reaches the results. |

## What works (keep it)

- The one place the verb matches the design is correct: "was associated with lower 28-day mortality," with an adjusted estimate and a 95% CI. That is the register the rest of the piece should be in.
- The study has a concrete exposure window, a concrete outcome (28-day mortality), and a large sample (2,914). Those are the specific, non-transferable facts. They currently sit in the wrong section; once moved to Results they will do the work that "comprehensive" and "critical gap" are failing to do.
- Sentence-level grammar is clean, there are no em dashes, and nothing is padded for length. The rewrite is mostly surgery on order and attribution, not line editing.

## Placeholders and author queries

1. **What does this paper report: the retrospective analysis or the prospective study?** The text narrates a retrospective result and then announces a prospective study "we designed." Tense, design, and the closing sentence must agree. Nothing else can be fixed cleanly until this is settled.
2. `[CITATION NEEDED: the burden-of-disease figure, if the opener is kept]` — which source, which year, which population?
3. `[CITATION NEEDED: the "studies" behind "early norepinephrine improves survival"]` — were they randomized or observational? The verb in your rewrite depends on the answer, and the current text implies an RCT-level claim with no trial named.
4. `[CITATION NEEDED: the "growing body of evidence" on delayed vasopressors]` — and which outcomes were worse, in which patients?
5. `[CITATION NEEDED: the rationale for a 1-hour threshold]` — is it prespecified, and why 1 hour rather than 3 or 6? Is it derived from prior work or chosen for the analysis?
6. `[AUTHOR TO SUPPLY: any prior evidence of no benefit or harm from early vasopressor initiation]` — needed for symmetry (#23). I have not searched and list no candidates, since I cannot verify any here.
7. **Which covariates were in the adjusted model, and were they prespecified?** (Needed wherever the result sentence ends up.)
8. **Is the exposure norepinephrine specifically, or vasopressors as a class?** The text uses both; pick one and define it.
9. No citation candidates are offered anywhere in this audit. All sources are left to you to retrieve and verify.

## The five changes that would most improve this piece

1. Take the study's own result out of the Introduction (#12) and end the section on the question, not the answer. The aOR belongs in Results; the gap belongs here.
2. Replace all three unnamed literature claims (#3, #4, #6) with named studies: design, population, threshold, estimate, citation, at least one of which did not find benefit (#23).
3. Delete "prevents death" (#16). An adjusted OR of 0.78 supports one verb, and the previous sentence already uses it.
4. Write one checkable gap sentence and one hypothesis sentence: exposure and threshold, time zero, population, outcome (#11, #22), after defining "early" once and using that term throughout (#10).
5. Replace the closing triad of negative parallelism, "comprehensive," and "pave the way" (#18, #19) with what the study did and the single question it answers.
