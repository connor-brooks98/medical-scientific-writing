# Medical & Scientific Writing Skill

An agent skill for writing, revising, and auditing medical and scientific prose: research manuscripts, case reports, abstracts, reviews, grant aims, cover letters, reviewer responses, and lay summaries. It removes the patterns that make text read as AI-generated, and it avoids them when drafting from scratch. Every number and citation is checked so that nothing gets invented along the way.

It works with Claude (claude.ai, Claude Desktop, Claude Code) and with any agent that reads `SKILL.md` skills (Codex, Cursor, Gemini CLI, OpenCode, and others).

> **What this is not.** It is not a detector-evasion tool and makes no promises about AI-detector scores. It improves writing quality. Disclosing AI assistance is still the author's job: ICMJE and most journals require it, and the skill reminds the author once per submission-bound task.

---

## Contents

- [Why structure matters more than vocabulary](#why-structure-matters-more-than-vocabulary)
- [What the skill does](#what-the-skill-does)
- [Before and after](#before-and-after)
- [Benchmark results](#benchmark-results)
- [Install](#install)
- [Usage](#usage)
- [Repository layout](#repository-layout)
- [Sources and credits](#sources-and-credits)
- [License](#license)

---

## Why structure matters more than vocabulary

Most "humanizer" tools swap words: *delve* for *examine*, em dashes for commas. The skill's design starts from a 2026 study of AI-written fiction: Russell et al., [*StoryScope: Investigating idiosyncrasies in AI fiction*](https://arxiv.org/abs/2604.03136), from the University of Maryland and Google DeepMind. The authors compared 10,272 human stories with 51,336 AI "mirror" stories written to the same prompts by five models. They found:

- AI text could be identified from **discourse-level choices alone** (93.2% macro-F1 with style features removed).
- **Removing surface artifacts barely changed detection.** After an editing system stripped cliché and purple prose, structure-based detection fell only from 95.5% to 93.9%.
- AI stories stated their theme outright more often (77% vs 52%), used vague allusions instead of named works (humans named specific works about twice as often), had tighter cause-and-effect with fewer subplots, and favored neat, accepting endings.

The study is about fiction, so this skill translates its findings into the scientific-writing forms they take. The skill's own source notes record which parts are direct findings and which are adaptations:

| StoryScope finding | What it looks like in a manuscript |
|---|---|
| States the theme explicitly | "This case highlights the importance of a high index of suspicion." |
| Vague allusions, few named works | "Studies have shown...", "a growing body of evidence..." with no named study |
| Tight causality, no subplots | The null secondary outcome, the weaker subgroup, or the diagnostic detour quietly disappears |
| Protagonist resolves everything | "Our study fills this critical gap", every limitation followed by a rebuttal |
| Neat, accepting endings | "These findings pave the way...", "Further research is needed." |
| AI texts cluster tightly | Sentences generic enough to paste into any paper on the topic |

So the skill fixes the argument first, then the sentences, then the words.

## What the skill does

**Three jobs**, picked from the request:

| You give it | It does |
|---|---|
| A draft to fix ("humanize", "tighten", "clean up") | **Revise**: rewrites, then reports what changed and confirms that numbers and citations are intact |
| Data, notes, or a request for new text | **Draft**: writes from an outline that lists the inconvenient results first, so they don't get dropped |
| A draft plus "review" or "audit" | **Audit**: a findings table with severity ratings and the five most valuable fixes |

**Three layers of patterns**, 33 in all, each with medical before/after examples in [`references/pattern-catalog.md`](skills/medical-scientific-writing/references/pattern-catalog.md):

- **Discourse (D1 to D11):** stated morals, vague allusions, tidy causal stories, the study as hero, reassuring endings, generic openings, uniform paragraph architecture, advocacy and asymmetric reporting, restatement, padding, template scaffolding. Plus the *swap test*: if a sentence could appear unchanged in a different paper, it says nothing about this one.
- **Sentence (S1 to S13):** -ing tails, "serves as", "not only... but", reflexive triads, synonym cycling, stacked or missing hedges, ", and this" chains, uniform rhythm, smothered verbs, hidden actors, signposting, false ranges, over-compressed meaning.
- **Word (W1 to W9):** AI vocabulary, inflation, ornamental adverbs, filler, rationed connectives, em dashes and formatting, AI-favored word choices, chatbot residue, buzzword compounds.

**Integrity rules that override style:**
- No invented numbers, studies, or references. Missing support becomes `[DATA NEEDED: ...]` or `[CITATION NEEDED: ...]`.
- Verbs match the study design: causal verbs only for randomized endpoints; "was associated with" for observational data.
- Null and unfavorable results get the same prominence as favorable ones.
- No "trend toward significance".
- The journal's instructions win over the skill's defaults.

**Guards against over-correction.** Clumsy de-AI editing leaves its own fingerprints: choppy prose with the connectives stripped out, manufactured "voice", over-hedged RCT results, staccato drama. The skill explicitly avoids each of these.

**A checker script** (`scripts/check_patterns.py`, standard-library Python) counts what language models miscount:
- sentence-length uniformity per paragraph, em dashes, repeated openers, and hedge stacks;
- uncited attributions and candidate pattern phrases;
- numbers or citations added to or lost from the original.

**Reference material** for IMRaD sections, CARE case reports, reviews, grants, cover letters, reviewer responses, lay summaries, statistical reporting, reporting guidelines (CONSORT, STROBE, PRISMA, STARD, TRIPOD+AI, and others), and plain-English writing.

## Before and after

Both "after" texts below are unedited outputs of Claude Opus 5.5 using the skill. [`examples/README.md`](examples/README.md) has the full set with change notes, and the same tasks run without the skill are in [`benchmarks/`](benchmarks/).

### Case report Discussion and Conclusion (euglycemic DKA after cholecystectomy)

<details open>
<summary><b>Before</b>: AI-styled draft (248 words)</summary>

> **Discussion**
>
> Euglycemic diabetic ketoacidosis (euDKA) represents a rare but potentially life-threatening complication of sodium-glucose cotransporter-2 (SGLT2) inhibitor therapy that has garnered increasing attention in the evolving landscape of diabetes management. SGLT2 inhibitors—which have revolutionized the treatment of type 2 diabetes, heart failure, and chronic kidney disease—promote glycosuria, reduce insulin requirements, and enhance ketogenesis, creating a perfect storm for ketoacidosis in the perioperative setting.
>
> Studies have shown that the risk of DKA is increased up to three-fold in patients receiving SGLT2 inhibitors. Notably, the absence of marked hyperglycemia can delay diagnosis, highlighting the critical importance of measuring ketones in any patient on these agents who presents with nausea, vomiting, or malaise. Furthermore, surgical stress, prolonged fasting, and reduced carbohydrate intake serve as key precipitating factors, underscoring the need for comprehensive perioperative protocols.
>
> The FDA recommends that empagliflozin be discontinued at least 3 days before scheduled surgery [5]. In our patient, the drug was continued until the day before surgery, and this likely contributed to the development of euDKA. Prompt recognition and initiation of insulin and dextrose therapy led to complete resolution, demonstrating the effectiveness of a multidisciplinary approach.
>
> **Conclusion**
>
> This case highlights the importance of maintaining a high index of suspicion for euDKA in postoperative patients taking SGLT2 inhibitors. It serves as a valuable reminder that normal glucose levels do not exclude DKA. Clinicians, surgeons, and anesthesiologists must work together to ensure safe perioperative management. Further research is needed to establish optimal strategies for preventing this potentially fatal complication.

</details>

<details open>
<summary><b>After</b>: with the skill (327 words)</summary>

> **Discussion**
>
> On the first day after laparoscopic cholecystectomy, our patient developed euglycemic diabetic ketoacidosis (euDKA), an uncommon but life-threatening complication of sodium-glucose cotransporter-2 (SGLT2) inhibitor therapy [CITATION NEEDED: incidence and outcome data for euDKA with SGLT2 inhibitors]. The risk of DKA has been reported to be up to three-fold higher in patients taking these drugs [CITATION NEEDED: source of the three-fold estimate]. SGLT2 inhibitors, used in type 2 diabetes, heart failure, and chronic kidney disease, promote glycosuria, reduce insulin requirements, and enhance ketogenesis, so ketoacidosis can develop while glucose is only modestly raised. Surgical stress, prolonged fasting, and reduced carbohydrate intake are recognized precipitants; our patient had surgery after a 14-hour fast and was vomiting on POD 1.
>
> The diagnosis was delayed. Her nausea, vomiting, and abdominal discomfort were attributed to postoperative ileus and opioid analgesia, and without marked hyperglycemia (capillary glucose 182 mg/dL) there was no prompt to look for ketoacidosis. The venous blood gas that evening showed an anion-gap acidosis (pH 7.12, anion gap 24 mmol/L, lactate 1.4 mmol/L), but euDKA was diagnosed approximately 14 hours later. Measuring ketones in a patient taking an SGLT2 inhibitor who presents with nausea, vomiting, or malaise identifies ketoacidosis regardless of the glucose value. We cannot tell from one case whether doing so when her symptoms began would have shortened her course.
>
> The FDA recommends that empagliflozin be discontinued at least 3 days before scheduled surgery [5]. Our patient was instructed to hold metformin on the morning of surgery, but empagliflozin was continued until the day before surgery; taking it inside the recommended window likely contributed to euDKA. She recovered with an insulin infusion and concurrent 10% dextrose; the anion gap closed after 38 hours.
>
> **Conclusion**
>
> A modestly raised glucose, such as this patient's 182 mg/dL, does not exclude DKA in patients taking SGLT2 inhibitors, and postoperative nausea, vomiting, or malaise in these patients should prompt ketone measurement even when another cause seems likely. Preoperative instructions should address SGLT2 inhibitors as explicitly as this patient's instructions addressed metformin, using the FDA's 3-day discontinuation interval [5].

</details>

**What changed:**
- **Removed:** the morals and the "further research is needed" coda.
- **Corrected:** the draft's claim of "prompt recognition", which the case itself contradicts. The 14-hour diagnostic delay is now the teaching point.
- **Flagged:** the uncited "three-fold" statistic gets a placeholder instead of being kept as fact.
- **Bounded:** what one case can show is now stated.
- **Preserved:** every number and the reference [5].

### Introduction for a diagnostic-accuracy study (no references yet)

<details>
<summary><b>Before</b>: AI-styled draft (220 words)</summary>

> Atrial fibrillation (AF) is the most common sustained cardiac arrhythmia and represents a major global health burden, affecting millions of individuals worldwide. In recent years, there has been growing interest in the role of wearable devices in the detection and management of AF. Smartwatches equipped with photoplethysmography (PPG) and single-lead electrocardiography (ECG) have emerged as promising tools that could potentially transform the landscape of arrhythmia screening.
>
> Studies have shown that smartwatch-based algorithms can detect AF with high sensitivity and specificity. Furthermore, a growing body of evidence suggests that early detection of AF may lead to improved outcomes, including reduced stroke risk. However, the accuracy of these devices in older adults—who bear the greatest burden of AF—remains poorly understood. Moreover, older adults often have comorbidities such as tremor, peripheral vascular disease, and frequent ectopy that may affect signal quality, highlighting the need for population-specific validation.
>
> To address this critical gap, we conducted a comprehensive prospective study to evaluate the diagnostic accuracy of a commercially available smartwatch for detecting AF in adults aged 75 years and older, using 14-day continuous patch monitoring as the reference standard. This study not only fills an important gap in the literature but also provides valuable insights that will inform clinical practice and pave the way for future research in this rapidly evolving field.

</details>

<details>
<summary><b>After</b>: with the skill (151 words of prose)</summary>

The full text is in [`benchmarks/iteration-2/revise-intro-no-citations/with_skill/outputs/intro_revised.txt`](benchmarks/iteration-2/revise-intro-no-citations/with_skill/outputs/intro_revised.txt) and is reproduced in [`examples/README.md`](examples/README.md#2-introduction-with-no-references-yet). In short:
- **Cut:** the generic burden opener and the closing "fills an important gap / pave the way" sentence. The intro now ends on the aim.
- **Replaced:** every vague "studies have shown" with a specific placeholder. No reference was invented.
- **Sharpened:** "poorly understood" now says which age groups earlier studies enrolled.

</details>

### Pattern snippets

| Pattern | Before | After |
|---|---|---|
| D1 Stated moral | "This case highlights the importance of thorough medication reconciliation in elderly patients." | "In older adults started on a thiazide, a sodium level within the first 2 weeks [CITATION NEEDED] would have detected this before she became confused." |
| D3 Tidy story | "These results demonstrate the effectiveness of structured discharge planning, likely mediated by improved adherence." | "...was associated with fewer readmissions (HR 0.78...). Mortality at 90 days did not differ (HR 1.02...). We did not measure adherence." |
| D5 Reassuring coda | "...a promising tool that may transform diagnosis. Further research is needed." | "...sensitivity 0.91 (95% CI 0.84 to 0.95). A multicentre study with radiography in all participants would show whether this holds outside one expert group." |
| D8 Advocacy | "Although performance was slightly lower in women (0.84 vs 0.90), this is unlikely to be clinically meaningful." | "AUROC was lower in women than in men (0.84 vs 0.90)." |
| S1 -ing tail | "Time to antibiotics fell from 94 to 61 minutes, highlighting the effectiveness of decision support." | "Time to antibiotics fell from 94 to 61 minutes." |
| S6 Hedge stack | "may suggest that X could potentially have a possible beneficial effect" | "suggest that X may reduce falls in [population]" |

## Benchmark results

### Method

- **Test cases:** three, defined in [`skills/medical-scientific-writing/evals/`](skills/medical-scientific-writing/evals/):
  1. Rewrite an AI-styled case report Discussion and Conclusion.
  2. Draft Results, Discussion, and Limitations for a retrospective cohort from bullet-point data. The data include null secondary outcomes and a non-significant subgroup interaction.
  3. Rewrite an AI-styled Introduction that has no references.
- **Setup:** each case was run in a fresh agent session with the skill and again without it, with the same model and the same prompt.
- **Grading:** 23 pass/fail assertions (fidelity, invented facts, specific patterns, reporting nulls, association language), plus objective counts from the checker's pattern lexicon.
- **Rounds:**
  - Round 1 used the first draft of the skill (v0.9).
  - Its results led to two fixes: a length rule, and a clearer rule for adding references the model has checked in PubMed.
  - Round 2 used v1.0 on Claude Opus 5.5 and on the smaller Claude Haiku 5.5.

All outputs, grades, timings, and the grading and metrics scripts are in [`benchmarks/`](benchmarks/).

### 1. AI-pattern phrases: draft vs revision

Counts of the checker's AI-pattern phrases. The "Discourse" column counts discourse-level phrases (stated morals, vague attributions, "fills the gap", "further research is needed", generic openers).

| Case | Text | Words | Pattern phrases | Discourse | Em dashes |
|---|---|---|---|---|---|
| Case report | **AI-styled draft (before)** | 248 | **20** | **5** | 2 |
| | Opus + skill (after) | 327 | **0** | **0** | 0 |
| | Opus, no skill | 439 | 0 | 0 | 0 |
| | Haiku + skill | 274 | **0** | **0** | 0 |
| | Haiku, no skill | 370 | 2 | 1 | 0 |
| Introduction | **AI-styled draft (before)** | 220 | **13** | **5** | 2 |
| | Opus + skill (after) | 151 | **0** | **0** | 0 |
| | Opus, no skill | 357 | 0 | 0 | 0 |
| | Haiku + skill | 139 | 1 | 1 | 0 |
| | Haiku, no skill | 210 | 2 | 1 | 0 |

### 2. Pass rate on the 23 assertions

| Round | Model | With skill | Without skill |
|---|---|---|---|
| 1 (skill v0.9) | Opus 5.5 | 23/23 (100%) | 21/23 (91%) |
| 2 (skill v1.0) | Opus 5.5 | 23/23 (100%) | 22/23 (96%) |
| 2 (skill v1.0) | Haiku 5.5 | 23/23 (100%) | 22/23 (96%) |

Every baseline failure came from the Introduction case. In round 1, the model without the skill added two facts that were not in the draft and doubled its length. In round 2, it again ran longer than the draft.

### 3. Length of the finished text (words of prose)

| Case | Opus + skill | Opus, no skill | Change | Haiku + skill | Haiku, no skill | Change |
|---|---|---|---|---|---|---|
| Case report revision | 327 | 439 | −26% | 274 | 370 | −26% |
| Cohort Results/Discussion draft | 745 | 1,077 | −31% | 655 | 1,029 | −36% |
| Introduction revision | 151 | 357 | −58% | 139 | 210 | −34% |

### 4. Cost

| Model | Extra time per task | Extra tokens per task |
|---|---|---|
| Opus 5.5 | +82 s | +36k |
| Haiku 5.5 | +51 s | +45k |

The skill reads its reference files and runs the checker, so each task costs a little more.

### What the numbers show, and what they don't

- **Against an AI-styled draft, the improvement is large.** Revisions with the skill (v1.0, Opus) brought the pattern phrases from 20 and 13 down to 0. Every number and citation survived.
- **Against the same strong model without the skill, the improvement is real but modest.** Opus 5.5 on its own already strips most surface tells and reports null results honestly. The skill's consistent, measurable advantages:
  - **Tighter text:** 26 to 58% fewer words, with identical fidelity results.
  - **Revisions that don't balloon:** without the skill, both Opus Introduction rewrites ran 60 to 95% longer than the draft. They added claims the author never made (guideline positions, screening-trial results, an "approximately fivefold" stroke risk), each with a reference placeholder. Some of that may be useful content, but a revision shouldn't add it unasked.
  - **More consistent placeholders** in place of invented support.
- **Smaller models gain more at the discourse level.** Without the skill, Haiku ended the case report with a "further study is needed" coda and a surgeons-anesthesiologists-prescribers "should agree" sentence. With the skill, it ended on the clinical lesson. With the skill, Haiku did keep one generic opener in the Introduction, so smaller models follow the guidance less completely.
- **Limitations of this benchmark:**
  - Three cases, one run per configuration per round.
  - The assertions were written by the skill's author and sit near ceiling for a strong model.
  - The pattern counts use the skill's own lexicon.
  - No blinded human rating has been done yet.

  Treat these results as evidence that the skill does what it claims on these tasks, not as proof of a general effect size. Contributions of new test cases and blinded human ratings are welcome.

## Install

The skill is the folder [`skills/medical-scientific-writing/`](skills/medical-scientific-writing/). There's no package registry to publish to: GitHub is the distribution point, and every route below installs from this repository or its release zip.

### Claude Code (plugin marketplace)

This repository is its own plugin marketplace.

```bash
claude plugin marketplace add connor-brooks98/medical-scientific-writing
claude plugin install medical-scientific-writing@medical-scientific-writing
```

Or inside a session:

```
/plugin marketplace add connor-brooks98/medical-scientific-writing
/plugin install medical-scientific-writing@medical-scientific-writing
```

Update later with `claude plugin update medical-scientific-writing@medical-scientific-writing`.

### Claude Code (manual)

```bash
git clone https://github.com/connor-brooks98/medical-scientific-writing.git
mkdir -p ~/.claude/skills
cp -r medical-scientific-writing/skills/medical-scientific-writing ~/.claude/skills/
```

### claude.ai and Claude Desktop

1. Download `medical-scientific-writing.zip` from the [latest release](https://github.com/connor-brooks98/medical-scientific-writing/releases/latest), or from [`dist/`](dist/).
2. Make sure code execution and file creation are turned on in your settings.
3. Go to **Customize > Skills**, click **+**, choose **Create skill > Upload a skill**, and select the zip.

Skills you enable on claude.ai also load in Claude Code when you sign in with the same account.

### Other agents (Codex, Cursor, Gemini CLI, OpenCode, GitHub Copilot, ...)

Use the open-source [`skills` CLI](https://github.com/vercel-labs/skills), which installs `SKILL.md` skills from GitHub into whichever agents it detects:

```bash
npx skills add connor-brooks98/medical-scientific-writing
```

This is the closest thing to `npm install`. The CLI runs through npx, but the skill itself is fetched from GitHub; it is not an npm package.

### Any chat interface

Upload `SKILL.md` and the files in `references/` with your text, and ask the model to apply the skill. The checker script is optional; the skill does the checks by hand when it can't run code.

## Usage

The skill triggers on its own for manuscript work. Some prompts that work well:

```
Rewrite the Discussion of my case report so it reads like a real case report. Keep every fact.
Draft the Results and Limitations from these numbers for JAMA Network Open: ...
Audit this abstract for AI-writing patterns and overclaiming. Don't rewrite it yet.
Tighten this Introduction to 400 words. I don't have references yet.
Write a plain-language summary of this trial for patients.
```

Run the checker yourself on any revision:

```bash
python3 skills/medical-scientific-writing/scripts/check_patterns.py revised.txt --original original.txt
```

## Repository layout

```
.claude-plugin/              plugin + marketplace manifests (Claude Code)
skills/medical-scientific-writing/
  SKILL.md                   workflow, integrity rules, pattern index
  references/                pattern catalog, section guide, evidence & reporting,
                             clarity toolkit, source notes
  scripts/check_patterns.py  mechanical checker (Python 3, standard library)
  evals/                     test cases (runnable with `claude plugin eval`)
examples/                    before/after examples with change notes
benchmarks/                  every run's outputs, grades, timings, and scripts
dist/                        zip for claude.ai / Claude Desktop upload
```

To rerun the test cases with Claude Code: `cd skills/medical-scientific-writing && claude plugin eval . --allow-tools Write,Edit,Bash --scaffold`. These are billed model runs.

## Sources and credits

The skill combines and reconciles these sources. Where they conflict, [`references/source-notes.md`](skills/medical-scientific-writing/references/source-notes.md) records the decision and the reason. For example, the em dash, "Notably", and "add personality" rules are resolved there.

- Russell J, Rajendhran R, Pham CM, Iyyer M, Wieting J. *StoryScope: Investigating idiosyncrasies in AI fiction.* arXiv:2604.03136 (CC0)
- [matsuikentaro1/humanizer_academic](https://github.com/matsuikentaro1/humanizer_academic) (MIT), based on [blader/humanizer](https://github.com/blader/humanizer) and Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [eniktab/scientific-paper-writer](https://github.com/eniktab/scientific-paper-writer) (MIT)
- [HeartWise-AI/ai-writing-skills](https://github.com/HeartWise-AI/ai-writing-skills) (MIT)
- [noora-noureldin2000/Skills-for-MedicalResearch-writing](https://github.com/noora-noureldin2000/Skills-for-MedicalResearch-writing)
- [quanghuy0497/Writing-in-the-Sciences](https://github.com/quanghuy0497/Writing-in-the-Sciences), notes on Kristin Sainani's Stanford course *Writing in the Sciences*
- [ashryaagr/karpathy-output-style](https://github.com/ashryaagr/karpathy-output-style) (MIT), with ASD-STE100 Simplified Technical English, Issue 9

The patterns were rewritten and reorganized, and all examples were newly written. No source text was copied wholesale.

## Disclaimer

This skill helps with writing. It doesn't provide medical advice, and it doesn't replace author responsibility, peer review, or a journal's own requirements. Verify every placeholder, every suggested reference, and every clinical statement before submission.

## License

[MIT](LICENSE)
