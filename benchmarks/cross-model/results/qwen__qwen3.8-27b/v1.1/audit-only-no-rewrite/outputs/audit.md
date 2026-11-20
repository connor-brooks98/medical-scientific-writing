# Audit: `introduction.txt` (Introduction, 2 paragraphs)

Scope: findings only, no rewrite, per request. Pattern codes: **D** = discourse/structure, **S** = sentence, **W** = word/mark, **IR** = integrity rule (evidence-matched verb), **Sec** = IMRaD section rule.

## Global observations

- Zero citations in two paragraphs. Both literature claims ("studies have shown", "a growing body of evidence") are unattributed.
- The "critical gap" invoked in paragraph 2 is never actually specified in paragraph 1; the two "evidence" sentences state the same point in two phrasings.
- Keep when rewriting: every number (2,914; 1 hour; 28-day; aOR 0.78; 95% CI 0.64–0.94), the verb "was associated with" in the retrospective-result sentence (correct for the design), and the en dash inside the CI (correct typography).

## Findings

| # | Location | Quoted text | Pattern | Severity | Suggested fix |
|---|---|---|---|---|---|
| 1 | P1 S1 | "Sepsis remains a leading cause of death worldwide, representing a pivotal challenge in the evolving landscape of critical care." | D6 | Major | Generic disease-burden opener; could begin any critical care paper (fails the swap test). Open on the specific question (does time to first vasopressor affect survival in septic shock?) and reach the unknown within one or two sentences. |
| 2 | P1 S1 | ", representing a pivotal challenge in the evolving landscape of critical care" | S1, W1 | Minor | -ing tail adds a flourish, not content; "pivotal" and "landscape" are AI-typical vocabulary. End the sentence at the fact. |
| 3 | P1 S2 | "In recent years, there has been growing interest in the role of early vasopressor initiation." | D6, D10 | Major | Second consecutive generic sentence; "growing interest" names no study or finding. Delete it, or replace with the specific unknown. |
| 4 | P1 S3 | "Studies have shown that early norepinephrine improves survival in septic shock." | D2 (+ IR3) | Major | No named study, design, population, effect size, or citation. "Improves" is a causal verb that needs a named randomized comparison; as written the support is unverifiable. Name the evidence (study, design, N, estimate) with a citation, or mark it [CITATION NEEDED]. |
| 5 | P1 S3–S4 | both sentences | D9 | Major | "Early is good" and "late is bad" are two phrasings of one claim; the paragraph repeats the point instead of stating what is actually unknown. |
| 6 | P1 S4 | "a growing body of evidence suggests that delayed vasopressor therapy may potentially be associated with worse outcomes in some patients" | D2, S6 | Major | Vague allusion with no citation; stacked hedge ("may potentially"); unspecified population ("some patients"). Cite specific studies and use one hedge sized to the design. |
| 7 | P1 S4 | "Furthermore," | W5 | Minor | Additive connective opener; keep connectives only where the relation is real. |
| 8 | P2 S1 | "In a retrospective analysis of 2,914 patients with septic shock at our institution, norepinephrine started within 1 hour of shock onset was associated with lower 28-day mortality (adjusted odds ratio, 0.78; 95% CI, 0.64–0.94)." | Sec §4 | Major | Prior result with full statistics sitting in the Introduction, uncited. If it is a published prior work, name and cite it; if not, state it in a phrase without the aOR/CI, or move it to Results. (The verb is correct; keep it.) |
| 9 | P2 S2 | "Early norepinephrine therefore prevents death in septic shock." | IR3 | **Critical** | Causal verb from a single-centre retrospective association. Observational data support "was associated with lower 28-day mortality", not "prevents death". This claim is what the prospective study exists to test; the Introduction should say so, not assert it. |
| 10 | P2 S3 | "To address this critical gap... fill an important gap" | D4, D9 | Major | Study-as-hero framing; "gap" doubled in one sentence; the gap is never specified anywhere in the Introduction. |
| 11 | P2 S3 | "...that will not only fill an important gap in the literature but also pave the way for improved outcomes" | S3, D5, W1 | Major | Negative parallelism plus a promise coda; "comprehensive" is a vague adjective and "improved outcomes" names no outcome. |
| 12 | P2 S3 | whole sentence | Sec §4, S13 | Major | No research question, design, population, comparator, or primary outcome for the prospective study. The aim must state what will be tested. |
| 13 | P1–P2 | "survival" / "28-day mortality" / "death" / "outcomes" | S5 | Minor | Four labels for the endpoint across two paragraphs. Pick one (e.g., 28-day mortality) and use it throughout. |

## The five revisions that would most improve the piece

1. **Downgrade the causal claim (row 9).** "Prevents death" cannot be stated from a retrospective study; state the association, and position the prospective study as the test of the causal question. This is the one issue an editor would most likely flag.
2. **Name the gap.** Replace "this critical gap" with one sentence stating what is actually unknown (e.g., whether earlier initiation improves survival, and at what timing threshold), so paragraph 2 hangs on something that exists.
3. **Back the literature with names.** Both unnamed-evidence sentences need specific citations (study, design, N, effect size) or [CITATION NEEDED]; delete the redundant second phrasing of the same claim.
4. **Make paragraph 1 specific.** Cut the worldwide / pivotal / evolving / in recent years / growing interest opening; reach the specific question in one or two sentences.
5. **State the aim plainly.** One sentence: what the prospective study tests, in which patients, against which comparator, with which primary outcome. Drop "comprehensive", "not only... but also", "pave the way for improved outcomes", and the doubled "gap".

Note: this text is headed for submission; most journals and ICMJE require disclosure of AI-assisted writing. If the rewrite draws on this audit, mention it once in the submission checklist.
