---
name: medical-scientific-writing
description: Write, revise, or audit medical and scientific prose (manuscripts, case reports, abstracts, grants, reviewer replies) without AI-writing patterns. Use for any journal-bound draft or humanize request.
---

# Medical and scientific writing

This skill produces the kind of prose an experienced journal editor would accept without rewriting: specific, economical, calibrated to the evidence, and free of the patterns that mark text as machine-generated. It merges six writing skills and one detection study (see `references/source-notes.md`) into one workflow.

The organizing idea comes from the StoryScope study of AI-written fiction (Russell et al., arXiv:2604.03136). AI text was identifiable from *discourse-level choices* alone (93% macro-F1 with style features removed), and removing surface artifacts barely changed detection (95.5% to 93.9%). In other words, AI writing differs mainly in what it chooses to say and how it shapes the argument; the vocabulary sits on top of that. A draft that swaps "delve" for "examine" but keeps the tidy, moralizing, generic structure still reads as AI to an expert. So this skill works top-down:

1. **Discourse layer (D)**: what is said, what is left out, how the argument resolves. Fix first.
2. **Sentence layer (S)**: syntax, rhythm, hedging, voice.
3. **Word layer (W)**: vocabulary, punctuation, formatting. Fix last.

These patterns are worth removing because they are bad scientific writing: they waste the reader's time, overstate evidence, or hide the actual finding. The aim is better papers. The skill does not hide AI involvement (see Integrity rule 6).

## Choose the job

| The user gives you... | Job | Output |
|---|---|---|
| Existing text to improve ("fix", "humanize", "tighten", "edit") | **Revise** | Revised text + short change log |
| Facts, data, notes, or a request for new text | **Draft** | New text written to avoid the patterns |
| Text plus "review", "audit", "what's wrong with this" | **Audit** | Findings table, no rewrite unless asked |

If the document type, study design, or target journal changes what you would write and you cannot infer it, ask one short question. Otherwise take the most reasonable reading, say which reading you took in one line, and proceed.

## Integrity rules (these override everything else)

1. **Never invent facts.** No number, statistic, named study, drug, dose, date, or reference that is not in the user's material. Where a claim needs support you do not have, insert `[DATA NEEDED: what]` or `[CITATION NEEDED: what claim]`. Sources you recall or find go under "Candidates for the author to verify", not into the text. There are two exceptions, and both apply only to a source you actually retrieved and checked (PubMed, CrossRef, the publisher's page), never one from memory: the user asked you to find literature, or a citation the user supplied does not say what the text claims and you are replacing it. Mark each such source `[ADDED: verified, DOI]` in the reference list and explain it in the author queries. Place placeholders on specific, checkable claims (an incidence, a risk estimate, a guideline position, a named finding). Textbook mechanism does not need a tag on every sentence.
2. **Preserve every datum when revising.** Numbers, units, CIs, p values, n, citations, figure and table references, and defined abbreviations survive unchanged unless the user asks otherwise. Run the checker with `--original` to confirm.
3. **The verb follows the study design, not the author's enthusiasm.** Causal verbs (reduces, improves, prevents) only for randomized comparisons of the randomized endpoint. Observational data: "was associated with". See `references/evidence-and-reporting.md`.
4. **Symmetric reporting.** Unfavorable, null, and inconvenient results get the same plainness and prominence as favorable ones. Removing a null result to make the story cleaner is a fidelity failure, not an edit.
5. **No significance spin.** Never "trend toward significance", "marginally significant", "approached significance", or "significant" without a test behind it.
6. **Disclosure stays the author's obligation.** This skill improves writing. It does not make AI assistance undisclosable, and you should not promise detector outcomes. When the text is for submission, mention once (not repeatedly) that most journals and ICMJE require disclosure of AI-assisted writing.
7. **Journal instructions and the author's explicit house style win** over the defaults here (em dashes, "vs.", passive voice, citation style, word budgets).

## Layer D: discourse and structure (fix first)

Read `references/pattern-catalog.md` for before/after examples of each. In brief:

| ID | Pattern | What it looks like | Fix |
|---|---|---|---|
| D1 | **Stated moral** | Sentence that tells the reader what to conclude: "This case highlights the importance of a high index of suspicion." "These findings underscore the need for..." AI narrators state the theme outright 77% of the time vs 52% for humans. | Delete, or replace with the concrete implication: who should do what, at which threshold, in which patients. |
| D2 | **Vague allusion** | "Previous studies have shown", "a growing body of evidence", "experts suggest", with no named study. Humans cite specific named works about twice as often (47% vs 24%). | Name the study, design, population, and number, with the citation. If none is supplied, `[CITATION NEEDED]`. |
| D3 | **Tidy causal story** | Every result supports the hypothesis; one mechanism; the null outcome, the weaker subgroup, the diagnostic detour are missing or explained away. AI shows tighter causal chains and fewer subplots. | Restore the "subplots": secondary and negative findings, competing explanations, uncertainty in the timeline. Keep them plain. |
| D4 | **Study-as-hero resolution** | "Our study fills this gap", "overcomes the limitations of prior work", every limitation resolved. | State what the study did and what it leaves unresolved. |
| D5 | **Reassuring coda** | Endings that resolve into acceptance or promise: "offers a promising avenue", "paves the way", "more research is needed". AI endings favor neat resolution; some models habitually add an epilogue. | End on the finding, then either the specific next study (design and outcome) or the clinical action. Otherwise stop. |
| D6 | **Generic preamble** | Openings that could begin any paper in the field ("Cardiovascular disease remains a leading cause of death worldwide"). | Narrow within one or two sentences to the specific question. Apply the swap test. |
| D7 | **Uniform architecture** | Every paragraph runs topic, evidence, "this suggests", bridge; every claim at the same certainty. | Let logic set the shape. Grade certainty claim by claim. |
| D8 | **Advocacy** | Favorable results get adjectives and their own sentence; limitations get a rebuttal ("a minor limitation that does not detract from..."). | Same sentence structure for good and bad news. Limitations stand alone, with the expected direction of bias. |
| D9 | **Restatement** | Paragraph-final summaries, "In other words", Introduction material re-described in Methods and Discussion. | Say it once, in the best place. |
| D10 | **Padding and negative space** | Explaining standard methods, defining AUROC, defending against imagined reviewers, sentences that only say what was not done. AI drafts commonly run 2 to 10 times over budget. | Cut the explanation, keep the facts. Keep a negative only when it changes interpretation (no multiplicity correction, missing-data handling). |
| D11 | **Template scaffolding** | "Challenges and Future Directions" headings, bold inline headers, bulleted Discussion, a heading followed by a sentence restating it. | Prose in IMRaD sections. Headings the journal requires, nothing more. |

**The swap test** (from the homogeneity finding: AI texts cluster tightly, human texts are rarer and more dispersed). For any sentence, ask: could it appear unchanged in a different paper on a different study? If yes, it carries no information about *this* work. Make it specific or cut it.

## Layer S: sentences

| ID | Pattern | Fix |
|---|---|---|
| S1 | **-ing tails**: ", highlighting the...", ", underscoring...", ", suggesting a role for..." | End the sentence at the data. If the tail had real content, give it its own clause with a named relation. |
| S2 | **Copula avoidance**: "serves as", "stands as", "represents", "functions as" | Use "is". |
| S3 | **Negative parallelism**: "not only X but also Y", "This is not merely X; it is Y" | State the positive claim directly. One measured "not only...but also" per section is acceptable. |
| S4 | **Reflexive triads**: three adjectives or three benefits by habit | List what is true, whether that is two items or five. |
| S5 | **Synonym cycling**: patients/participants/subjects/individuals for one cohort | One term per concept, throughout (the "banana rule"). Repetition is a feature. |
| S6 | **Miscalibrated hedging**: stacked hedges ("may potentially suggest a possible role") or bare causal claims from observational data | One hedge, sized to the design. Strong designs get direct statements. |
| S7 | **Clause chaining**: ", and this...", ", and it...", one subject carrying three predicates, lists nested in lists | Name the relation (because, whereas, although), split, or use semicolons for nested lists. |
| S8 | **Uniform rhythm**: every sentence 15 to 25 words with subject-verb-object openings | In paragraphs of 3+ sentences, avoid all sentences within a 5-word range. Get variation by splitting stacked conditions or joining supporting facts, never by adding staccato drama. |
| S9 | **Smothered verbs and buried predicates**: "performed an analysis of", 12+ words between subject and verb, noun stacks | Resurrect the verb. Bring subject and verb together early. Unstack nouns. |
| S10 | **Hidden or wrong actor**: passive that hides who decided; a figure or report that "determines" or "acknowledges" | Name the actor where judgment is involved ("We excluded..."). Passive is fine in Methods when the procedure matters more than the actor. |
| S11 | **Signposting**: "It is important to note that", "In this section, we will", "Let us now consider" | Just say the thing. |
| S12 | **False ranges**: "from molecular mechanisms to population health" | Name the actual items, or cut. |
| S13 | **Compressed meaning**: missing comparator, condition, or outcome ("The model outperformed baseline") | Restore what was compared, on what, under which condition. |

## Layer W: words and marks

- **W1 AI vocabulary.** delve, tapestry, landscape (abstract), pivotal, crucial, intricate, multifaceted, interplay, nuanced, holistic, foster, garner, showcase, underscore, highlight (verb), testament, realm, paramount, leverage, utilize, robust (vague), comprehensive (vague), seamless, notable, meticulous, myriad, shed light on, pave the way. Replace with the plain word you mean, or delete. These are candidates to examine in context; they are not banned. "Comprehensive geriatric assessment" and "robust standard errors" are technical terms and stay.
- **W2 Inflation and evaluation.** groundbreaking, remarkable, striking, impressive, excellent, unprecedented, transformative, promising, exciting, near-perfect, novel (unsupported), first-ever. Let the number carry the claim.
- **W3 Ornamental adverbs.** markedly, remarkably, dramatically, critically, profoundly, substantially or significantly with no number or test. Keep functional adverbs that carry magnitude or frequency (approximately, slightly, consistently, only).
- **W4 Filler.** "in order to", "due to the fact that", "a number of", "it is worth noting that", "has the ability to", "in terms of". See the replacement table in `references/clarity-toolkit.md`.
- **W5 Rationed connectives.** "Additionally", "Furthermore", "Moreover", "Notably", "Importantly", "Interestingly": at most one per paragraph, never as the opener of consecutive paragraphs, and only where the relation is real. Logical connectives (however, thus, although, whereas, in contrast) are not tells; keep them.
- **W6 Marks and formatting.** No em dashes in manuscript prose by default (commas, parentheses, colons, or a new sentence); straight quotes; sentence-case headings; no decorative bold; no emojis.
- **W7 AI-favored word choices.** "linked to" for a statistical association (use "associated with"), "via" (through, by), "yield" for analytic output (produce, give), "beyond" as a transition (in addition to), "where" or "in which" as loose connectors.
- **W8 Chatbot residue.** "Certainly", "I hope this helps", "Great question", knowledge-cutoff disclaimers, sycophantic reviewer-response openers.
- **W9 Buzzword compounds.** cutting-edge, state-of-the-art, data-driven, next-generation, used as praise. Keep correct hyphenation of real compound modifiers ("10-year risk", "placebo-controlled").

## Over-correction is also a tell

Clumsy de-AI editing leaves its own signature. Avoid these:

- **Bare-deleting connectives.** Choppy, connective-stripped prose reads as automated cleanup. When you remove a transition, restore the link with a better connective, an echoed key noun, or a restructured sentence.
- **Manufactured voice.** Generic humanizers recommend opinions, humor, asides, and "letting some mess in". That advice is wrong for manuscripts. The human quality you want is *intellectual commitment calibrated to evidence*: "We interpret this as evidence that X," not jokes or feelings.
- **Over-hedging strong results.** A significant primary endpoint in an RCT is stated directly.
- **Staccato drama.** Strings of new short sentences for effect. Keep short sentences that state a claim; don't create theatrical ones.
- **Mechanical voice flipping.** Converting every Methods passive to "We..." or every inanimate subject to "We". Change voice only when the actor matters.
- **Banning legitimate academic phrasing.** "Prior studies have shown [refs]", "In contrast", "Taken together" are fine when followed by specifics.
- **Rewriting what works.** Touch the flagged spans. Preserve the author's voice, terminology, and structure elsewhere.

## Workflow: Revise

1. **Read the whole piece first.** Identify document type, section, study design, audience, and journal if known. Note every number and citation.
2. **Discourse pass (D1 to D11).** Decide what to delete (morals, restatements, padding), what to restore (a null result, a comparator, a limitation the text glossed), and what to reorder. Do this before polishing sentences that may disappear.
3. **Sentence pass (S1 to S13).** Repair hedging, chaining, rhythm, verbs, actors.
4. **Word pass (W1 to W9).** Vocabulary, connectives, punctuation.
5. **Fidelity check.** Every number, citation, and named entity in your output exists in the input or the user's sources. Every finding in the input still exists in the output. Run:
   ```bash
   python3 scripts/check_patterns.py revised.txt --original original.txt
   ```
   (Path is relative to this skill's folder; use stdin with `===ORIGINAL===` / `===REVISED===` markers if you have no files.) Read the report as candidates, not verdicts. Run it at most twice. If Python is unavailable, do the checks by hand.
6. **Length check.** A revision should normally be the same length as the original or shorter (count words outside placeholders). It can run longer only to restore content the original left out (D3) or a qualification the evidence requires. Say so in the change log when that happens. If the revision has grown otherwise, cut the lowest-value sentences first: background the reader already knows, and interpretation the author did not ask for.
7. **Editor's audit.** Ask: "What would still make an experienced journal editor suspect this was machine-generated, or overstated?" List the survivors to yourself, fix them, and re-check fidelity.
8. **Deliver** (format below).

## Workflow: Draft

1. **Collect the material.** Data, design, population, comparators, references, target journal, word limit, reporting guideline. Ask only for what blocks writing; use placeholders for the rest.
2. **Pre-write (most of the work).** Complete the central-claim sentence: "This [study/case] shows [X] in [population], based on [evidence], which means [Z] for [who]." Outline each section using `references/section-guide.md`. Write down the results that *don't* fit the story (null outcomes, weaker subgroups, adverse events, diagnostic detours) so they get a place in the outline before drafting starts.
3. **Draft in the natural order** for full papers: tables and figures, Results, Methods, Introduction, Discussion, Abstract last.
4. **Draft against the patterns.** The traps that most often appear at draft time: a theme-stating last sentence (D1), unnamed "studies" (D2), a missing null result (D3), a promise-shaped ending (D5), a generic first sentence (D6), and -ing tails (S1). Prefer one specific number over one adjective.
5. **Audit as in Revise steps 5 and 7.** For drafts, keep within the journal's limit or the budgets in `references/evidence-and-reporting.md`.

## Workflow: Audit

Return a table: location, quoted text, pattern ID, severity, suggested fix. Severity: **Critical** (misleads: wrong verb for the design, dropped result, spin, fabricated or missing support), **Major** (impairs clarity or credibility: morals, vague allusions, padding, chaining), **Minor** (style: vocabulary, connectives, marks). End with the five revisions that would most improve the piece.

## Output format

For **Revise**:
1. The revised text, ready to paste.
2. **What changed**: 3 to 8 bullets grouped by layer, describing the kinds of changes (not every edit).
3. **Fidelity**: one line confirming numbers, citations, and findings are preserved, or naming what was reverted.
4. **Placeholders and author queries**: every `[DATA NEEDED]` / `[CITATION NEEDED]`, and any claim you think the evidence does not support.

For **Draft**: the text, then placeholders, then any assumptions you made (design, journal, word limit) in one or two lines.

Keep the commentary short. The text is the deliverable. If the user asks for only the text, give only the text.

When the user works with files (.docx, .md, .tex), edit in that format. For .docx, tracked changes let the author accept or reject each edit.

## Reference files

Load these as needed. They are where the detail lives.

- `references/pattern-catalog.md`: every D, S, and W pattern with medical before/after examples and the evidence behind it. **Read it for any Revise or Audit job longer than a paragraph, and before your first Draft in a session.**
- `references/section-guide.md`: IMRaD section moves, tense table, case reports (CARE), abstracts, narrative and systematic reviews, grant aims, cover letters, reviewer responses, posters, lay summaries.
- `references/evidence-and-reporting.md`: evidence-matched verbs by design, hedging calibration, statistical reporting formats, reporting guidelines (CONSORT, STROBE, PRISMA, CARE, STARD, TRIPOD+AI, and others), number formatting, length budgets.
- `references/clarity-toolkit.md`: clutter, verbs, nominalizations, buried predicates, paragraphs, punctuation, parallelism, reader clarity before compression, and plain-English mode for lay or instructional text.
- `references/source-notes.md`: notes on the StoryScope paper and the six source skills, and how their conflicts were resolved.
- `scripts/check_patterns.py`: mechanical checker for counts a model gets wrong (sentence lengths, em dashes, openers, hedge stacks, candidate vocabulary, numbers and citations added or lost).
