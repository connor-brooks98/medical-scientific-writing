# Pattern catalog

Every pattern named in SKILL.md, with what it looks like, why it matters, and a before/after pair. All examples are invented for illustration (the drugs, numbers, and studies are fictional unless named as real). In each pair the facts are the same; the After never adds information that was not in the Before. Where an After needs information the Before lacked, it uses a placeholder, exactly as you should.

Evidence labels:
- **[StoryScope]**: a quantitative finding from Russell et al., *StoryScope: Investigating idiosyncrasies in AI fiction* (arXiv:2604.03136). That study analyzed fiction, so its application to scientific prose is an adaptation, stated as such.
- **[Editors]**: patterns documented across the source skills (Wikipedia's "Signs of AI writing" lineage, medical-editing practice, Sainani's *Writing in the Sciences*). These are practitioner observations, not measured effect sizes.

## Contents

- Layer D, discourse and structure: D1 to D11, plus the swap test
- Layer S, sentences: S1 to S13
- Layer W, words and marks: W1 to W9
- Over-correction patterns: O1 to O6
- A full worked example (case report Discussion)

---

## Layer D: discourse and structure

The StoryScope result that motivates this layer: classifiers using only narrative-structure features separated human from AI stories at 93.2% macro-F1, and when an editing system removed surface artifacts (cliché, purple prose) from AI stories, structure-based detection fell only from 95.5% to 93.9%. Surface edits leave the structural signature intact. The AI profile was consistent: explicit thematic framing, tight causality, linear plots with few subplots, protagonist-driven resolution, tidy endings, and a narrow, homogeneous region of "narrative space". Each D pattern below translates one of those tendencies into its scientific-writing form.

### D1. Stated moral (explicit theme)

[StoryScope] Narrators explicitly stated the theme in 77% of AI stories vs 52% of human stories; AI scored about 20% higher on thematic explicitness.

In scientific prose this is the sentence, usually paragraph-final or section-final, that tells the reader what to conclude instead of giving them the evidence and letting the inference stand. It is especially common at the end of case reports and Discussion paragraphs.

Watch for: "This case highlights/underscores/illustrates the importance of...", "These findings emphasize the need for...", "This serves as a reminder that...", "Clinicians should be aware that..." (with no specific action), "...is crucial for optimal patient outcomes."

Before:
> The patient's hyponatremia resolved after discontinuation of the thiazide. This case highlights the importance of maintaining a high index of suspicion for drug-induced electrolyte disturbances and underscores the critical role of thorough medication reconciliation in elderly patients.

After:
> The patient's hyponatremia resolved after the thiazide was stopped. In older adults started on a thiazide, a sodium level within the first 2 weeks [CITATION NEEDED: monitoring interval] would have detected this before she became confused.

Why the After is better: it replaces a moral that fits every adverse-drug-event report with a specific, checkable implication (which patients, which test, when). If the author has no specific implication, delete the moral; the case stands without it.

### D2. Vague allusion instead of named specifics

[StoryScope] AI stories used vague allusions more (72% vs 50%); human stories referenced specific named works at nearly twice the rate (47% vs 24%).

Scientific form: unattributed consensus. "Studies have shown", "a growing body of evidence", "the literature suggests", "experts recommend", "it is well established", with no named study, design, population, or number, and often no citation.

Before:
> A growing body of evidence suggests that early mobilization improves outcomes in critically ill patients. Several studies have demonstrated benefits across multiple domains.

After (user supplied one trial):
> In a multicentre trial of 200 mechanically ventilated adults, early mobilization shortened ICU stay by a median of 3 days compared with usual care (ref). [CITATION NEEDED: any additional trials, with their outcomes]

"Prior studies have shown that X (refs 3 to 6)" is acceptable academic phrasing **when** the citations are present and X is specific. The pattern is the vagueness, not the phrase.

### D3. Tidy causal story

[StoryScope] AI plots showed tighter causal chains and fewer subplots (79% "no subplots" vs 57%); human stories integrated subplots twice as often (42% vs 21%).

Scientific form: a narrative in which every result points the same way. The secondary outcome that was null disappears from the Abstract. The subgroup in which the effect was weaker is "consistent with" the main result. One mechanism is offered as if established. In case reports, the diagnostic course becomes a straight line from presentation to correct diagnosis, omitting the initial misdiagnosis, the test that was falsely reassuring, or the week of uncertainty.

Before:
> Treatment with the intervention reduced 30-day readmission (HR 0.78, 95% CI 0.64 to 0.95). These results demonstrate the effectiveness of structured discharge planning, likely mediated by improved medication adherence.

After (input data also contained a null mortality result and no adherence measure):
> Structured discharge planning was associated with fewer 30-day readmissions (HR 0.78, 95% CI 0.64 to 0.95). Mortality at 90 days did not differ between groups (HR 1.02, 95% CI 0.81 to 1.29). We did not measure adherence, so we cannot say whether it explains the difference in readmissions.

Rule: if a result exists in the input, it exists in the output, with comparable prominence. When drafting, list the inconvenient results before you write.

### D4. Study-as-hero resolution

[StoryScope] AI favored protagonist-driven resolutions (69% vs 46%).

Scientific form: the paper resolves the field's problem single-handedly. "Our study fills this critical gap", "overcomes the limitations of previous work", "provides definitive evidence", and a Limitations section in which each limitation is neutralized.

Before:
> To address this critical gap, we conducted the first comprehensive study to definitively characterize...

After:
> We measured X in Y patients at Z centres. [If "first" matters: "We found no previous report of X in a search of MEDLINE and Embase to [date]" (cite the search), or drop the claim.]

### D5. Reassuring or promotional coda

[StoryScope] AI resolutions favored internal acceptance (47% vs 27%); humans used more ambiguous endings. Model fingerprints included extended denouements and frequent epilogues.

Scientific form: the closing sentence or paragraph that resolves everything into promise or reassurance. "These findings pave the way for...", "offer a promising avenue for future research", "hold great potential to transform clinical practice", "Further research is warranted", "The future looks bright".

Before:
> In conclusion, point-of-care ultrasound represents a promising tool that may transform the diagnosis of pediatric pneumonia. Further research is needed to fully elucidate its potential.

After:
> In children aged 1 to 5 years presenting to one emergency department, point-of-care ultrasound detected radiographic pneumonia with a sensitivity of 0.91 (95% CI 0.84 to 0.95). A multicentre study with chest radiography as the reference standard in all participants would show whether this sensitivity holds outside a single expert group.

A conclusion is either the finding (with its scope) plus a specific next study (design, population, outcome), or the finding plus the clinical action it supports. "More research is needed" is neither.

### D6. Generic preamble

[StoryScope] Some model fingerprints included front-loading context; across all models, AI stories sat in denser, more generic regions of narrative space.

Scientific form: the first sentence or paragraph that could open any paper in the specialty. Burden-of-disease boilerplate, "In recent years, X has gained increasing attention", "X is a major public health concern worldwide."

Before:
> Diabetes mellitus is a chronic metabolic disorder that represents a significant global health burden, affecting millions of individuals worldwide. In recent years, there has been growing interest in the role of continuous glucose monitoring.

After:
> Continuous glucose monitors are now prescribed to many adults with type 2 diabetes who do not use insulin [CITATION NEEDED: uptake figure], but whether they lower HbA1c in this group is uncertain: trials have enrolled mainly insulin users (refs).

Burden statistics are legitimate motivation when they are specific and cited; the pattern is the unanchored generality and the slow approach to the question.

### D7. Uniform architecture and certainty

[StoryScope] Claude had the most uniform narrative voice of the five models; across models, AI features co-occurred as a recognizable profile. [Editors] "Epistemic uniformity" and "structural predictability" are named patterns in the source skills.

Scientific form: every paragraph follows topic sentence, evidence, "These findings suggest", bridge sentence. Every claim has the same hedge, whether it is a replicated RCT result or a speculation about mechanism.

Fix: let each paragraph's job set its shape. Some paragraphs state a claim and defend it; some present conflicting evidence and weigh it; some are two sentences. Grade certainty claim by claim: "showed" for the randomized primary result, "was associated with" for observational findings, "may" for mechanism, "we speculate" for speculation.

### D8. Advocacy and asymmetric reporting

[Editors, from medical-AI manuscript review] Authors (and models imitating them) write about their own work as advocates. Signals: evaluative adjectives on favorable results; unfavorable results hedged ("only slightly lower", "remained competitive") or moved to the Supplement; each limitation followed by reassurance; comparators described pejoratively; "we believe", "we are confident"; single-centre results extended to "clinical practice".

Before:
> Although performance was slightly lower in women (AUROC 0.84 vs 0.90), this difference is unlikely to be clinically meaningful, and the model remained highly accurate across all subgroups. The retrospective design is a minor limitation that does not detract from these robust findings.

After:
> AUROC was lower in women than in men (0.84 vs 0.90). Data were collected retrospectively at a single centre, which may overstate performance relative to prospective use.

### D9. Restatement and paraphrastic repetition

Scientific form: a closing sentence that restates the paragraph in abstract terms; "In other words", "That is", "Put differently", "Essentially" followed by the same claim; the Introduction's description of a dataset repeated in Methods and again in Discussion.

Before:
> Sleep duration under 6 hours was associated with higher systolic pressure. In other words, shorter sleep appears to be linked to elevated blood pressure. These findings demonstrate an important relationship between sleep and cardiovascular health.

After:
> Sleep duration under 6 hours was associated with higher systolic pressure.

Keep a second sentence only if it adds a mechanism, comparison, magnitude translation ("an HR of 0.65 means 35% fewer events"), or qualification.

### D10. Padding and negative space

[Editors] AI-assisted drafts measured against author targets ran 2 to 11 times over budget in Methods and Results.

Delete on sight:
- Rationale for standard methods ("We used AUROC, which is well suited to...").
- Pedagogy (defining a p value, explaining what a confidence interval is).
- Pre-emptive defence against an imagined reviewer (if it's a real limitation, one sentence in Limitations).
- Meta-commentary on the authors' own approach ("This approach allowed for a rigorous and comprehensive assessment").
- Negative-space sentences: "No sample size calculation was performed." "We did not report F1."

Keep a negative only when its absence would let a reader over-read the result: no multiplicity correction, how missing data were handled, absence of prospective validation (in Limitations).

Test: if the sentence would be equally true of a paper whose authors never thought about the issue, delete it.

Never delete a fact without a destination. Detail removed from the main text goes to a named supplementary table, cited at the point of removal.

### D11. Template scaffolding

Scientific form: outline-like headings ("Challenges and Future Directions", "Key Takeaways"), bold inline labels followed by a reworded explanation ("**Mechanism:** The mechanism involves..."), bulleted Results or Discussion, a heading immediately followed by a sentence that restates it, title case in headings.

Fix: prose paragraphs in Abstract, Introduction, Results, Discussion. Bullets only for inclusion/exclusion criteria, materials lists, and checklists. Use only the headings the journal requires. Sentence-case headings unless the journal says otherwise.

### The swap test

[StoryScope] The five AI sources formed a tight cluster; the mean human-to-AI centroid distance was 1.6 times the mean AI-to-AI distance; human stories were rarer (rarity percentile 0.71 vs 0.49, Cohen's d = 0.83).

Practical translation: generic sentences are interchangeable across papers. For every sentence ask whether it could be pasted, unchanged, into a different paper on a different study. "Further studies are needed to confirm these findings" passes the swap test for every paper ever written; it says nothing. "A trial randomizing insulin-naive adults to CGM or usual care, with HbA1c at 6 months as the primary outcome, would answer this" does not; it belongs to this paper. Specificity is the most reliable single marker of human expert prose.

---

## Layer S: sentences

### S1. Superficial -ing tails

Watch for: ", highlighting...", ", underscoring...", ", emphasizing...", ", reflecting...", ", suggesting a potential role for...", ", contributing to...", ", ensuring...".

Before:
> Median time to antibiotics fell from 94 to 61 minutes after the sepsis alert was introduced, highlighting the effectiveness of electronic decision support in improving sepsis care.

After:
> Median time to antibiotics fell from 94 to 61 minutes after the sepsis alert was introduced.

Deleting the tail usually leaves a complete sentence; end it there. Do not refill the space with ", and this...". If the tail carried real content (a mechanism, a comparison), give it a clause with a named relation or its own sentence.

### S2. Copula avoidance

Watch for: serves as, stands as, functions as, acts as, represents, constitutes, marks, boasts, features.

Before: "Troponin serves as the cornerstone biomarker for the diagnosis of myocardial infarction."
After: "Troponin is the reference biomarker for diagnosing myocardial infarction."

Keep "serves as" when the serving relationship is the science ("the hinge region serves as a flexible linker").

### S3. Negative parallelism

Before: "SGLT2 inhibitors are not merely glucose-lowering agents; they are cardiorenal protective therapies."
After: "SGLT2 inhibitors lower glucose and also reduce heart failure hospitalization and kidney function decline (refs)."

Also flag tailing negations ("...with no guesswork") and "It's not about X, it's about Y."

### S4. Reflexive triads

Before: "This approach is safe, effective, and scalable." "The intervention improved physical, emotional, and social well-being."
After: say what the data show. If safety and efficacy were measured and scalability was not, write two items. If five domains improved, list five.

The rule of three is a legitimate rhetorical device; the AI pattern is the triad produced by habit, often with a third item that has no support.

### S5. Synonym cycling (the banana rule)

Before: "Patients in the intervention arm had lower readmission rates. Participants also reported better quality of life. Subjects in this group..."
After: one term ("patients") throughout. Same for variable names, group names, outcome labels, and techniques. If Methods defines "the obese group", Results must not switch to "heavier participants". A reader cannot tell a stylistic synonym from a new category.

### S6. Miscalibrated hedging

Two opposite failures:

Stacked hedges (too weak):
> These findings may suggest that vitamin D supplementation could potentially have a possible beneficial effect in select populations.
> → These findings suggest that vitamin D supplementation may reduce falls in [specific population].

Bare causal claims (too strong, observational data):
> Statin use reduces dementia risk in older adults.
> → Statin use was associated with lower dementia incidence in older adults (HR 0.82, 95% CI 0.74 to 0.91).

One hedge per claim, sized to the design. See the calibration table in `evidence-and-reporting.md`. For an observational finding framed as an interventional implication, a two-word cushion is appropriate ("may help reduce"); that is calibration, not stacking.

### S7. Clause chaining and stacked predicates

Watch for: ", and this...", ", and it...", ", and these...", two or more ", and" clause joins in a paragraph, one subject carrying three or more predicates separated by statistics or citation blocks, lists nested inside lists.

Before:
> Delirium was more common in the intervention group, and this was most pronounced in patients over 80, and it was associated with longer length of stay.

After:
> Delirium was more common in the intervention group, most of all in patients over 80. Patients with delirium stayed longer in hospital.

Decide the relation first (cause: because; contrast: whereas; concession: although; location or degree: "particularly in"; closely related facts: semicolon). Nested lists get semicolons between outer items.

### S8. Uniform rhythm (low burstiness)

[Editors] AI paragraphs cluster in a narrow 15 to 25-word band with uniform subject-verb-object openings; well-written medical papers range from about 10 to 55 words within a paragraph. In one source skill's testing, restructuring rhythm accounted for most of the measurable reduction in detector scores, more than vocabulary changes did.

Criterion: a paragraph of three or more sentences is too uniform if all sentences fall within a 5-word range. Also flag three consecutive sentences opening with the same word or a bare noun-phrase subject.

How to vary, without hurting clarity:
1. Split a sentence that stacks several conditions or comparisons (this improves clarity too).
2. Join adjacent supporting sentences that share a relation, using a conjunction that names it or a semicolon.
3. Open one sentence with a prepositional phrase or subordinate clause ("In patients over 65, ...", "Although the sample was small, ...").
4. Move a qualifier from the end of a sentence to the start, or the reverse.

Do not merge a short sentence that states a claim ("Mortality did not differ.") into its neighbour. Do not add new dramatic fragments ("The result? Striking."). After deleting ornamental adverbs, re-check rhythm; deletion often leaves uniform sentences.

### S9. Smothered verbs, buried predicates, noun stacks

Before: "An assessment of renal function was performed in all participants prior to the administration of contrast."
After: "We measured creatinine in all participants before giving contrast."

Before (buried predicate): "One retrospective study of 1,240 adults with heart failure with preserved ejection fraction admitted to three academic centres between 2015 and 2020 found..."
After: "One retrospective study found that, among 1,240 adults with HFpEF admitted to three academic centres in 2015 to 2020, ..."

Before (noun stack): "post-discharge risk-stratified intervention allocation"
After: "After discharge, we assigned patients to an intervention according to their readmission risk."

### S10. Hidden or wrong actor

Name the actor when a judgment or decision is involved, especially in Discussion and reviewer responses:
- "Patients with incomplete diaries were excluded" (Methods procedure: passive is fine).
- "The analysis determined that the effect was not clinically meaningful" → "We judged the effect not clinically meaningful because it was below the 5-point minimal important difference."
- "The revised manuscript clarifies the inclusion criteria" (reviewer response) → "We have clarified the inclusion criteria in Methods (lines 112 to 118)."

Keep conventional inanimate subjects with display verbs: "Figure 2 shows", "These data suggest", "The test discriminates A from B".

### S11. Signposting and announcements

Before: "It is important to note that adverse events were rare. In this section, we discuss the implications of these findings."
After: "Adverse events were rare (4 of 312 patients)."

Also: "Let us now turn to", "As mentioned above", "As previously discussed", "Here's what this means".

### S12. False ranges

Before: "Applications of liquid biopsy span from early cancer detection to treatment monitoring, from minimal residual disease to resistance profiling."
After: "Liquid biopsy is used to monitor treatment response and detect minimal residual disease (refs). Its use for early detection is under study (ref)."

### S13. Compressed meaning

Compression that omits an actor, comparator, condition, or outcome forces the reader to reconstruct it. It is the over-correction of concision.

- "The intervention adds value beyond usual care." → which outcome, compared with what? "Patients receiving the intervention reported less pain at 6 weeks than those receiving usual care."
- "The model outperformed baseline." → on which metric, at which threshold, on which data?
- "Bidirectional associations suggest mutual reinforcement." → "Each behaviour predicted the other at the next time point, which is consistent with a self-reinforcing cycle."

If the input lacks the missing element, ask with `[DATA NEEDED: outcome and comparator]`. Do not supply one.

---

## Layer W: words and marks

### W1. AI vocabulary

Candidates (examine in context; they are not banned): delve, tapestry, landscape (abstract), realm, pivotal, crucial, paramount, intricate/intricacies, multifaceted, interplay, nuanced, holistic, foster, garner, showcase, underscore, highlight (verb), testament, leverage, utilize, robust (vague), comprehensive (vague), seamless, notable, meticulous, myriad, commendable, embark, navigate (figurative), unlock, harness, elucidate, shed light on, pave the way, a deeper understanding.

These words appear at elevated frequency in post-2023 scientific text and tend to co-occur. Replace with the plain word you mean: use (utilize), examine (delve into), important or a specific reason (crucial), show (showcase), or delete.

Technical uses stay: "comprehensive geriatric assessment", "robust variance estimator", "highlighted in red in Figure 2".

### W2. Inflation, promotion, evaluation

groundbreaking, remarkable, striking, impressive, excellent, outstanding, exceptional, unprecedented, transformative, revolutionary, powerful, compelling, exciting, encouraging, promising, near-perfect, game-changer, landmark (for your own work), novel (without stated literature search), first (without stated search).

Before: "The model achieved an excellent AUROC of 0.94."
After: "The model achieved an AUROC of 0.94 (95% CI 0.92 to 0.96)."

### W3. Ornamental adverbs

Delete-test: remove the adverb; if no information is lost, it was ornamental. markedly, remarkably, strikingly, dramatically, profoundly, critically, fundamentally, increasingly, vastly, deeply, exceptionally, clearly, substantially/significantly (with no number or test).

Functional adverbs carry magnitude, frequency, or calibration and stay: approximately, slightly, modestly, consistently, almost, only, largely, relatively, statistically significantly (with a test).

### W4. Filler

See the full table in `clarity-toolkit.md`. Most common: in order to (to), due to the fact that (because), a majority of (most), it is important to note that (delete), has the ability to (can), in terms of (rewrite), at the present time (now, or delete), with respect to (for).

### W5. Rationed connectives

Additive and attention-directing openers are AI crutches when used mechanically: Additionally, Furthermore, Moreover, Notably, Importantly, Interestingly, In conclusion (outside the final paragraph), In summary, Overall.

Default: at most one of these per paragraph; never as the opener of consecutive paragraphs; "Notably/Importantly/Interestingly" only when followed by a concrete datum that genuinely departs from expectation, and never applied only to favorable findings (that is D8).

Logical connectives are not tells and should stay: however, although, whereas, thus, therefore, in contrast, conversely, consequently, taken together. Removing them produces choppy prose (see O1).

### W6. Marks and formatting

- **Em dashes:** replace all in manuscript prose by default. Parenthetical: commas. Aside: parentheses. Explanation or list: colon. Clause break: period or semicolon. (If the journal or author style uses em dashes, at most one per section.)
- **Curly quotes** to straight quotes in plain-text and Markdown deliverables (keep whatever the author's word processor uses in .docx).
- **Title Case Headings** to sentence case unless the journal requires otherwise.
- **Boldface**: none in body prose except field conventions (bold vectors, required labels).
- **Emojis**, decorative symbols, arrows in prose: remove.

### W7. AI-favored word choices

- "linked to" for a statistical association → "associated with". Keep "linked" for data linkage (or use "merged") and for the noun ("the link between").
- "via" → "through", "by", "using" (keep in established technical phrases: "via the femoral artery").
- "yield" for analytic output → produce, give, provide (keep for chemical or diagnostic yield).
- "Beyond X," as a transition → "In addition to X,".
- ", where..." and ", in which..." as loose connectors (no location or condition) → "with...", a prepositional phrase, or a new sentence.
- "remain" + adjective ("remain unclear") is fine occasionally; repeated, it becomes a tic.

### W8. Chatbot residue and sycophancy

Remove: "Certainly!", "Great question", "I hope this helps", "Feel free to", "As an AI", "As of my knowledge cutoff", "This is indeed an important area", reviewer-response openers that praise the comment instead of answering it. A response to reviewers can thank once at the top; each response then states what was changed and where.

### W9. Buzzword compounds

cutting-edge, state-of-the-art, data-driven, next-generation, best-in-class, world-class, used as praise. Replace with the specific property ("trained on 1.2 million ECGs from 4 hospitals"). Real compound modifiers keep their hyphens per AMA style: "10-year risk", "placebo-controlled", "low-dose".

### Also flag (statistical language)

- "trend toward significance", "marginally significant", "approached significance", "borderline significant".
- "significant" or "significantly" without a reported test.
- "numerically superior", "comparable" without an equivalence margin.
- "proves", "confirms", "establishes", "definitively" from a single study.

---

## Over-correction patterns

Clumsy de-AI editing leaves its own signature. These are failures of the edit, not of the original.

### O1. Bare-deleted connectives

Before (AI):
> Additionally, apixaban reduced major bleeding, highlighting its favorable safety profile. Additionally, the benefit appeared within 3 months.

Wrong fix (choppy):
> Apixaban reduced major bleeding. The benefit appeared within 3 months.

Right fix:
> Apixaban also reduced major bleeding. This difference appeared within 3 months.

When you remove a transition, restore the logical link with a better connective, an echoed key noun, or a restructured sentence.

### O2. Manufactured voice

Generic humanizers advise adding opinions, humor, first-person feelings, tangents, and "mess". In a manuscript, case report, or grant this is wrong. The human quality to aim for is intellectual commitment calibrated to evidence ("We interpret this as evidence that the effect is mediated by..."), field-specific precision, and willingness to state what remains unknown.

### O3. Over-hedging strong evidence

A significant primary endpoint of an adequately powered RCT is stated directly: "Dapagliflozin reduced the primary composite outcome (HR 0.74, 95% CI 0.65 to 0.85)." Adding "may" here is miscalibration in the other direction.

### O4. Staccato drama

Strings of new very short sentences for rhetorical punch read as a different kind of machine style. Keep the author's short claim sentences; don't manufacture new ones for effect.

### O5. Mechanical voice and subject flipping

Do not convert every passive into "We..." or every inanimate subject into "the authors". Methods passive is conventional. "Figure 1 shows" and "These data suggest" are correct. Change voice only when the actor matters to meaning or accountability.

### O6. Rewriting what already works

Edit the flagged spans. A sentence that is clear and specific stays, even if it contains a listed word for a legitimate reason. Preserve the author's terminology, structure, and voice elsewhere. Homogenizing the whole text into one "clean" register is itself a tell.

---

## Full worked example: case report Discussion

Before (AI-styled draft):
> Pembrolizumab-induced myocarditis represents a rare but potentially life-threatening immune-related adverse event that has garnered increasing attention in the evolving landscape of immuno-oncology. Our patient, a 67-year-old man with metastatic melanoma, presented with dyspnea and elevated troponin 3 weeks after his first dose—a timeline consistent with previous reports. Prompt initiation of high-dose corticosteroids led to rapid clinical improvement, underscoring the critical importance of early recognition and treatment.
>
> Studies have shown that immune checkpoint inhibitor myocarditis carries a mortality rate of up to 50%. Notably, our patient's favorable outcome highlights the pivotal role of a multidisciplinary approach. Furthermore, this case emphasizes the need for heightened vigilance among oncologists, cardiologists, and emergency physicians alike.
>
> In conclusion, this case serves as a valuable reminder that clinicians must maintain a high index of suspicion for ICI myocarditis. Further research is needed to establish optimal screening and management strategies.

(The case section of the input also stated: initial ECG was read as normal; the first troponin was attributed to demand ischemia; diagnosis was made on day 4 by cardiac MRI; troponin peaked at 1,840 ng/L; the patient developed a new right bundle branch block on day 2; pembrolizumab was permanently discontinued.)

After:
> Our patient developed myocarditis 3 weeks after his first dose of pembrolizumab. Myocarditis from immune checkpoint inhibitors is uncommon, but reported mortality is high [CITATION NEEDED: incidence and mortality figures, with the source of the "up to 50%" estimate].
>
> The diagnosis was delayed by 4 days. His first troponin was attributed to demand ischemia and his initial ECG was read as normal; the new right bundle branch block on day 2 was the first sign that the process was myocardial. Cardiac MRI on day 4 confirmed myocarditis, by which point troponin had reached 1,840 ng/L. He improved after high-dose corticosteroids, and pembrolizumab was permanently discontinued. We cannot tell from a single case whether earlier treatment would have changed his course.
>
> In patients receiving a checkpoint inhibitor who present with dyspnea and a raised troponin in the first weeks of treatment, a new conduction abnormality should prompt evaluation for myocarditis, including cardiac MRI, rather than attribution to demand ischemia. Whether routine troponin measurement before each early dose detects myocarditis sooner [CITATION NEEDED: existing screening studies] is a question for prospective cohorts.

What changed:
- **D1, D5:** removed three stated morals ("underscoring the critical importance", "serves as a valuable reminder", "heightened vigilance") and the generic "further research is needed" coda. Replaced them with one specific clinical implication drawn from the case and one specific open question.
- **D3:** restored the diagnostic detour (normal ECG, troponin attributed to demand, 4-day delay), which was in the case section but missing from the Discussion. This is the teaching content of the case.
- **D2:** "Studies have shown... up to 50%" had no citation; flagged rather than kept or invented.
- **D4, S10:** removed the claim that the outcome "highlights the pivotal role of a multidisciplinary approach" (not supported by one case) and added the limit of inference from a single case.
- **D6:** removed the "evolving landscape of immuno-oncology" opener.
- **W1, W5, W6:** removed garnered, evolving landscape, pivotal, notably, furthermore, the em dash, and the triad of specialties.
- **Fidelity:** every number in the After (3 weeks, day 2, day 4, 1,840 ng/L) appears in the input. One unsupported statistic was converted to a placeholder.
- **Author queries:** the clinical implication in the final paragraph and the screening question are interpretations drawn from the case, not facts from the input. List them for the author to confirm, soften, or delete. An editor proposes interpretation; the author owns it.
