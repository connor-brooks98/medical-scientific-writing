# Audit: Introduction (early norepinephrine in septic shock)

Source: `introduction.txt` (2 paragraphs, 7 sentences). This is an audit only. Nothing has been rewritten. Where I say what a sentence needs, I describe the fix and leave the wording to you.

---

## Bottom line

There are three serious problems. Fix these first:

1. **Causal overreach from your own observational data (S6).** "Early norepinephrine therefore prevents death in septic shock" does not follow from a retrospective adjusted OR. A reviewer will flag this before anything else.
2. **The argument contradicts itself, so there is no gap left to fill.** S3 says early norepinephrine already "improves survival," and S6 says it "prevents death." If both are true, a new prospective study has no reason to exist. Then S7 refers to "this critical gap," but no gap was ever named.
3. **No citations and no stated aim.** Every factual claim in paragraph 1 has no source. The intro never says what the new study will test: no design, population, comparator, primary outcome, or hypothesis.

Below that, the prose has a lot of generic filler, stacked hedges, and promotional phrasing. Those are easy to fix once the argument is sound.

---

## Sentence-by-sentence

### Paragraph 1

**S1.** *"Sepsis remains a leading cause of death worldwide, representing a pivotal challenge in the evolving landscape of critical care."*
- First clause: a reasonable opening claim, but it has no citation and no number. A burden figure with a source (global deaths or ICU mortality) carries more weight than "a leading cause."
- Second clause: "pivotal challenge in the evolving landscape" is filler. It adds no information, and "pivotal" and "evolving landscape" read as boilerplate. The participial tag ("representing...") just repeats the first clause in inflated words.
- It opens with sepsis in general, while the study is about septic shock and vasopressor timing. That's one more step of funnel than you need.

**S2.** *"In recent years, there has been growing interest in the role of early vasopressor initiation."*
- Throat-clearing. Researchers' "interest" is not evidence. The sentence tells the reader nothing about what is known.
- "In recent years" has no time anchor and no citation.
- "Growing" comes up again in S4 ("growing body of evidence"). Repeated word.

**S3.** *"Studies have shown that early norepinephrine improves survival in septic shock."*
- Vague attribution: which studies? No citations.
- Overstated. As far as I know, the evidence for a mortality benefit from early norepinephrine is mostly observational. The main randomized trial I'm aware of (CENSER, Permpikul et al., 2019) had shock control at 6 h as its primary outcome and did not show a significant 28-day mortality difference. **Check this against the current literature yourself.** But "studies have shown ... improves survival" is a stronger claim than the evidence base probably supports.
- Logic problem: if this were already established, your study would not be needed (see Bottom line #2).
- Tone mismatch: this sentence is flatly causal, while S4, right after it, is heavily hedged. Together they read as uncertain about what the field actually knows.

**S4.** *"Furthermore, a growing body of evidence suggests that delayed vasopressor therapy may potentially be associated with worse outcomes in some patients."*
- Stacked hedges: "suggests," "may," "potentially," "associated," "in some patients." That's five qualifiers on one claim. One or two, placed carefully, would be enough. "May potentially" is redundant on its own.
- Redundant with S3: "early improves survival" and "delayed is associated with worse outcomes" are the same claim from opposite directions. As written, it adds no new information.
- "Furthermore" signals a new point, but the point isn't new.
- "Worse outcomes" and "some patients" are vague. Which outcomes, which patients? If heterogeneity matters (e.g., by lactate, source, or baseline MAP), say what it is and cite it. If it doesn't, drop the qualifier.
- "A growing body of evidence" again has no citation.

### Paragraph 2

**S5.** *"In a retrospective analysis of 2,914 patients with septic shock at our institution, norepinephrine started within 1 hour of shock onset was associated with lower 28-day mortality (adjusted odds ratio, 0.78; 95% CI, 0.64–0.94)."*
- This is the strongest sentence in the intro: specific, quantified, and correctly worded as an association. Keep the substance.
- It isn't clear whether this is published prior work (then cite it) or unpublished preliminary data (then say so). That matters for how reviewers weigh it.
- Missing context the reader needs to judge it:
  - The comparator. Within 1 h versus what: >1 h? Any later time?
  - How "shock onset" was defined. Time zero is the central methodological problem in vasopressor-timing studies.
  - The study period, and what the model adjusted for (even in brief, or point to the source).
- An odds ratio overstates relative risk when the outcome is common, and 28-day mortality in septic shock usually is. Consider whether a risk ratio or absolute risk difference would represent the effect more honestly, or at least avoid letting readers take 0.78 as a 22% risk reduction.
- This sentence is where you should set up the gap: retrospective timing analyses are open to confounding by indication (who gets norepinephrine early, and why) and to time-related biases (immortal-time and time-zero misclassification). That limitation is the honest reason a prospective study is needed. At the moment the paragraph goes the other way and treats the result as settled.

**S6.** *"Early norepinephrine therefore prevents death in septic shock."*
- **The most serious error in the text.** It turns an adjusted association from a single-center retrospective cohort into a causal, absolute claim ("prevents death"). "Therefore" marks a conclusion the data cannot support.
- It contradicts the correct "was associated with" wording in the sentence right before it.
- It undercuts your own study. If the question is settled, why run a prospective study?
- This sentence should not survive in any form that asserts causation.

**S7.** *"To address this critical gap, we designed a comprehensive prospective study that will not only fill an important gap in the literature but also pave the way for improved outcomes."*
- "This critical gap" has no referent. No gap has been stated, and S6 just claimed the question is answered.
- "critical gap" and then "important gap" in the same sentence: repeated word, and a sentence that refers back to itself.
- "Comprehensive" is a self-assessment, not a description. It tells the reader nothing about the design.
- Doesn't say what the study is. Missing: design (randomized? pragmatic? observational with prespecified time zero?), population, intervention/exposure and comparator, primary outcome, and hypothesis or aim. An introduction should usually end on that.
- "will not only ... but also pave the way for improved outcomes" is promotional and can't be tested. Claims about future impact belong in the Discussion, if anywhere, and should be modest.
- Tense: "we designed ... that will" fits a protocol or grant. If this introduces a completed study, the aim should be in past tense and the "will" language goes. (See Assumptions.)

---

## Cross-cutting issues

| Issue | Where | Severity |
|---|---|---|
| Causal claim from observational data | S6 (also S3) | High |
| Argument contradicts itself; no real gap stated | S3, S6, S7 | High |
| No citations for any claim from the literature | S1–S4 | High |
| No stated aim, hypothesis, or design | S7 | High |
| Key definitions missing from preliminary data (comparator, time zero) | S5 | Medium |
| OR presented without caution about a common outcome | S5 | Medium |
| Stacked hedging | S4 | Medium |
| Redundant claims (S3 and S4 say the same thing) | S3–S4 | Medium |
| Generic/boilerplate phrasing ("pivotal challenge," "evolving landscape," "growing interest," "growing body of evidence," "critical gap," "comprehensive," "pave the way") | S1, S2, S4, S7 | Medium |
| Repeated words ("growing" x2, "gap" x2) | S2/S4, S7 | Low |
| Funnel starts too broad (sepsis vs. septic shock) | S1 | Low |
| Inconsistent certainty: flat causal (S3, S6) next to heavy hedging (S4) | Throughout | Medium |

## Structural note

A standard introduction goes: what is known (with sources) → what is not known, and why it matters → what this study does. As written, the draft says the answer is known (S3), says it again more weakly (S4), shows your data (S5), says it is proven (S6), and then claims a gap (S7). Your rewrite should move the "unknown" part to just after S5, framed around the limits of retrospective timing data, and end on a concrete aim.

## What is worth keeping

- The S5 data point: specific, quantified, reported with a CI, and correctly worded as an association.
- The basic idea that retrospective signal justifies prospective testing is sound. The draft just doesn't say it.
- The overall length is about right for a short introduction. The problem is content, not length.

## Assumptions

- I assumed this is the introduction to a **protocol, grant, or prospective study manuscript** because of "will" in S7. If the prospective study is already done and this introduces its results, the tense and the S7 framing need more changes than noted above.
- I assumed the S5 cohort is **your group's own prior work**, published or not, because of "at our institution." I don't know which, so I flagged both cases.
- My note on the RCT evidence (S3) is from general knowledge, not a literature search done for this audit. Check it against current sources before relying on it.
- I didn't check the numbers in S5 against any source document. I only checked whether they're presented appropriately.
