# Medical & Scientific Writing Skill

An agent skill for writing, revising, and auditing medical and scientific prose: research manuscripts, case reports, abstracts, reviews, grant aims, cover letters, reviewer responses, and lay summaries. It removes the patterns that make text read as AI-generated, and it avoids them when drafting from scratch. Every number and citation is checked so that nothing gets invented along the way.

It works with Claude (claude.ai, Claude Desktop, Claude Code) and with any agent that reads `SKILL.md` skills (Codex, Cursor, Gemini CLI, OpenCode, and others).

It brings together seven open skills and one research paper:

- the  [StoryScope](https://arxiv.org/abs/2604.03136) study of AI-written text
- [blader/humanizer](https://github.com/blader/humanizer)
- [humanizer_academic](https://github.com/matsuikentaro1/humanizer_academic)
- [scientific-paper-writer](https://github.com/eniktab/scientific-paper-writer)
- [ai-writing-skills](https://github.com/HeartWise-AI/ai-writing-skills)
- [Skills-for-MedicalResearch-writing](https://github.com/noora-noureldin2000/Skills-for-MedicalResearch-writing)
- [Writing-in-the-Sciences](https://github.com/quanghuy0497/Writing-in-the-Sciences)
- [karpathy-output-style](https://github.com/ashryaagr/karpathy-output-style)

[Sources and Credits](#sources-and-credits) says what came from each.

**Results across 9 test cases and 8 models from 5 providers** (OpenAI, Google, xAI, DeepSeek, Qwen):
- Pass rate on the graded checks rose from 84% without the skill to 93% with v1.0 and 97% with v1.1.
- v1.1 scored at least as well as v1.0 on every model.
- Every model's revisions came out shorter with the skill than without it.
- No revision lost a number from the original.
- Separate Claude Opus 5.5 and Haiku 5.5 runs showed the same pattern.

[Details below](#benchmark-results).

> **What this is not.** It is not a detector-evasion tool and makes no promises about AI-detector scores. It improves writing quality. Disclosing AI assistance is still the author's job: ICMJE and most journals require it, and the skill reminds the author once per submission-bound task.

---

## Contents

- [Install](#install)
- [Why Structure Matters More Than Vocabulary](#why-structure-matters-more-than-vocabulary)
- [What the Skill Does](#what-the-skill-does)
- [Before and After](#before-and-after)
- [Benchmark Results](#benchmark-results)
- [Usage](#usage)
- [Repository Layout](#repository-layout)
- [Sources and Credits](#sources-and-credits)
- [Caveats](#caveats)
- [Disclaimer](#disclaimer)
- [License](#license)

---

## Install

[`skills/medical-scientific-writing/`](skills/medical-scientific-writing/).

### Claude Code (plugin marketplace)

Install from Claude Code plugin marketplace.

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

1. Download `medical-scientific-writing.zip` from the [latest release](https://github.com/connor-brooks98/medical-scientific-writing/releases/latest), or from [`dist/medical-scientific-writing.zip`](dist/medical-scientific-writing.zip) (click **Download raw file**).
2. Make sure code execution and file creation are turned on in your settings.
3. Go to **Customize > Skills**, click **+**, choose **Create skill > Upload a skill**, and select the zip.

> **Don't use GitHub's green "Code > Download ZIP" button for this.** That zip wraps the whole repository in a folder, so the uploader can't find `SKILL.md` and rejects it with "The archive must contain a .claude-plugin/plugin.json manifest, or a top-level SKILL.md". The release zip has `SKILL.md` at its top level, which is what the uploader needs.

Skills you enable on claude.ai also load in Claude Code when you sign in with the same account.

### Other agents (Codex, Cursor, Gemini CLI, OpenCode, GitHub Copilot, ...)

Use the open-source [`skills` CLI](https://github.com/vercel-labs/skills), which installs `SKILL.md` skills from GitHub into whichever agents it detects:

```bash
npx skills add connor-brooks98/medical-scientific-writing
```

### Any chat interface

Upload `SKILL.md` and the files in `references/` with your text, and ask the model to apply the skill. The checker script is optional; the skill does the checks by hand when it can't run code.

---

## Why Structure Matters More Than Vocabulary

Most "humanizer" tools swap words: *delve*  for  *examine*, em dashes for commas. The skill's design starts from a 2026 study of AI-written fiction: Russell et al., [*StoryScope: Investigating idiosyncrasies in AI fiction*](https://arxiv.org/abs/2604.03136), from the University of Maryland and Google DeepMind. The authors compared 10,272 human stories with 51,336 AI "mirror" stories written to the same prompts by five models. They found:

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

## What the Skill Does

**Three jobs**, picked from the request:

| You give it | It does |
|---|---|
| A draft to fix ("humanize", "tighten", "clean up") | **Revise**: rewrites, then reports what changed and confirms that numbers and citations are intact |
| Data, notes, or a request for new text | **Draft**: writes from an outline that lists the inconvenient results first, so they don't get dropped |
| A draft plus "review" or "audit" | **Audit**: a findings table with severity ratings and the five most valuable fixes |

**Three layers of patterns**, 35 in all, each with medical before/after examples in [`references/pattern-catalog.md`](skills/medical-scientific-writing/references/pattern-catalog.md):

- **Discourse (D1 to D11):** stated morals, vague allusions, tidy causal stories, the study as hero, reassuring endings, generic openings, uniform paragraph architecture, advocacy and asymmetric reporting, restatement, padding, template scaffolding. Plus the *swap test*: if a sentence could appear unchanged in a different paper, it says nothing about this one.
- **Sentence (S1 to S15):** -ing tails, "serves as", "not only... but", reflexive triads, synonym cycling, stacked or missing hedges, ", and this" chains, uniform rhythm, smothered verbs, hidden actors, signposting, false ranges, over-compressed meaning, staged run-ups and aphorisms, arguing with objections no one raised.
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

## Before and After

Every "after" below is an unedited model output from the benchmark runs. The inputs are AI-styled drafts written for testing. Full outputs for every model and configuration are in [`benchmarks/`](benchmarks/).

### 1. A Discussion that argues with no one (Claude Opus 5.5, skill v1.1)

This case tests the patterns added in v1.1:
- **Staged run-up:** "At its core, the central question..."
- **Aphorism:** "Mobility is the currency of recovery"
- **Rebutting objections nobody raised:** "This is not to say...", "One might argue..."
- **Split negative:** "does not mean X. It means Y."
- **Closing verdicts:** "The key point is...", "Overall..."
- **Gap-filling guess:** treating missing data as evidence

<details open>
<summary><b>Before</b>: AI-styled draft (199 words)</summary>

> At its core, the central question of this study was whether early mobilization is safe after hip fracture surgery in patients with dementia. Mobility is the currency of recovery in older adults. In this retrospective cohort of 1,146 patients with dementia, mobilization within 24 hours of surgery was associated with lower 30-day mortality (6.2% vs 9.8%; adjusted odds ratio, 0.61; 95% CI, 0.39–0.95) and shorter length of stay (median 8 vs 11 days). This illustrates the importance of early mobilization in this vulnerable population.
>
> This is not to say that delayed mobilization is always harmful. One might argue that patients with severe dementia cannot participate in early physiotherapy, but our findings suggest otherwise. Delirium incidence did not differ between groups (31% vs 29%). A lack of difference in delirium does not mean that early mobilization has no cognitive effects. It means that our study could not detect them.
>
> The table below compares our findings with previous cohorts. Information on preoperative ambulatory status was not recorded for 18% of patients, suggesting that these patients were likely nonambulatory before the fracture. The key point is that early mobilization was feasible for most patients. Overall, early mobilization appears to be beneficial.

</details>

<details open>
<summary><b>After</b>: with the skill (174 words, not counting placeholders)</summary>

> In this retrospective cohort of 1,146 patients with dementia, mobilization within 24 hours of hip fracture surgery was associated with lower 30-day mortality (6.2% vs 9.8%; adjusted odds ratio, 0.61; 95% CI, 0.39–0.95) and shorter length of stay (median 8 vs 11 days).
>
> Delirium incidence did not differ between groups (31% vs 29%). This null result does not exclude a cognitive effect of early mobilization; the 95% CI for the difference [DATA NEEDED: risk difference or odds ratio for delirium, with 95% CI] shows how large an effect in either direction these data can rule out. Of the 1,146 patients, [DATA NEEDED: n (%)] were mobilized within 24 hours, including [DATA NEEDED: n/N (%)] of those with severe dementia.
>
> Table [X] compares these estimates with previous cohorts [CITATION NEEDED: the cohorts shown in the table]. Preoperative ambulatory status was not recorded for 18% of patients [DATA NEEDED: how missing ambulatory status was handled in the adjusted model]. If patients who walked before the fracture were both mobilized earlier and less likely to die, incomplete adjustment for ambulatory status would exaggerate the association between early mobilization and lower mortality. On the safety question that motivated this study, mobilization within 24 hours was not associated with higher mortality or more delirium in patients with dementia.

</details>

**What changed:**
- **Removed:** the aphorism, both strawman rebuttals, and the closing verdicts.
- **Missing data:** the "likely nonambulatory" guess is gone. In its place is a real limitation: which way the missing data would bias the result.
- **Unsupported claims:** "feasible for most patients" and the severe-dementia claim had no numbers behind them, so both became placeholders.
- **Ending:** the causal "appears to be beneficial" became an associational answer to the safety question the study asked.
- **Kept:** all nine numbers.

### 2. Case report Discussion and Conclusion (Claude Opus 5.5, skill v1.1)

<details>
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

<details>
<summary><b>After</b>: with the skill (308 words)</summary>

> **Discussion**
>
> Euglycemic diabetic ketoacidosis (euDKA) is a rare but potentially life-threatening complication of sodium-glucose cotransporter-2 (SGLT2) inhibitors, which are used in type 2 diabetes, heart failure, and chronic kidney disease. By causing glycosuria, these drugs lower insulin requirements and promote ketogenesis, so ketoacidosis can develop without marked hyperglycemia. The risk of DKA has been reported to be up to three-fold higher in patients taking an SGLT2 inhibitor [CITATION NEEDED: source of the three-fold estimate]. Surgical stress, prolonged fasting, and reduced carbohydrate intake are recognized precipitants [CITATION NEEDED: perioperative precipitants of SGLT2 inhibitor-associated DKA].
>
> Our patient had two risk factors before the operation began. She was told to hold metformin on the morning of surgery, but empagliflozin was continued until the day before surgery, and she then fasted for 14 hours. The FDA recommends stopping empagliflozin at least 3 days before scheduled surgery [5]. Continuing the drug this close to surgery likely contributed to her euDKA, although a single case cannot separate its effect from that of fasting and surgical stress.
>
> The diagnosis was delayed. Her nausea, vomiting, and abdominal discomfort on POD 1 were attributed to postoperative ileus and opioid analgesia, and her capillary glucose was 182 mg/dL. A venous gas obtained that evening, after she became tachypneic, showed an anion gap acidosis (pH 7.12, anion gap 24 mmol/L) with a lactate of 1.4 mmol/L. The diagnosis of euDKA was made approximately 14 hours later, on the morning of POD 2 (beta-hydroxybutyrate 6.8 mmol/L). After insulin and dextrose were started, the anion gap closed after 38 hours.
>
> **Conclusion**
>
> In this patient, euDKA after laparoscopic cholecystectomy followed continuation of empagliflozin until the day before surgery, and her early symptoms were attributed to ileus and opioids. A capillary glucose of 182 mg/dL did not exclude DKA. For patients taking an SGLT2 inhibitor, preoperative instructions should state when to stop the drug, and postoperative nausea, vomiting, or malaise should prompt measurement of ketones.

</details>

**What changed:**
- **Removed:** the morals and the "further research is needed" ending.
- **Corrected:** the draft claimed "prompt recognition", which the case itself contradicts. The 14-hour diagnostic delay, taken from the Case Presentation, is now the teaching point.
- **Flagged:** the uncited "three-fold" figure now carries a placeholder.
- **Bounded:** the text now says what a single case can't show.
- **Kept:** reference [5] and every number.

### 3. Same model, with and without the skill (Qwen4 Max)

Each model got the same introduction to make publication-ready. Without the skill, Qwen4 Max more than doubled it, from 220 to 536 words, adding guideline claims and screening-strategy arguments the author never made. With skill v1.1, it returned 213 words that open on the population, mark every claim needing support, and end on the aim:

> Atrial fibrillation (AF), the most common sustained cardiac arrhythmia, is most prevalent in adults aged 75 years and older, who also carry the highest risk of AF-related stroke [CITATION NEEDED: age-specific AF prevalence and stroke risk]. ...
>
> We prospectively evaluated a commercially available smartwatch [DATA NEEDED: device model and algorithm version] for detecting AF in adults aged 75 years and older, using 14-day continuous patch monitoring as the reference standard. We aimed to estimate sensitivity and specificity for AF over the 14-day monitoring period.

### 4. What v1.1 added over v1.0

**Writing like the author (Grok 4.7).** The author supplied an excerpt from their own paper, which uses em dashes ("confined to patients discharged on weekdays — a pattern we did not anticipate"), and asked for a new paragraph in their voice. v1.0 applied its default no-em-dash rule anyway. v1.1 lets the author's sample override the defaults:

| | Last sentence of the revised paragraph |
|---|---|
| v1.0 | "Second, the effect was larger in patients taking 10 or more medications (risk difference, -6.1 percentage points)." |
| v1.1 | "Second, the effect was larger in patients taking 10 or more medications — risk difference, -6.1 percentage points." |

**Reviewer responses lead with the decision (Claude Opus 5.5).**

| | Response to "report the number lost to follow-up in each group" |
|---|---|
| Before (draft) | "We sincerely thank the reviewer for this insightful and valuable comment, which has greatly helped us to improve the quality of our manuscript. Loss to follow-up is indeed an important consideration in any longitudinal study... Therefore, we have now added..." |
| After (v1.1) | "We agree and have added the number of patients lost to follow-up in each group to the CONSORT diagram (Figure 1) and to the Results (page 9, lines 182–184): 14 patients (4.1%) in the intervention group and 17 patients (5.0%) in the control group." |

### Pattern snippets

| Pattern | Before | After |
|---|---|---|
| D1 Stated moral | "This case highlights the importance of thorough medication reconciliation in elderly patients." | "In older adults started on a thiazide, a sodium level within the first 2 weeks [CITATION NEEDED] would have detected this before she became confused." |
| D3 Tidy story | "These results demonstrate the effectiveness of structured discharge planning, likely mediated by improved adherence." | "...was associated with fewer readmissions (HR 0.78...). Mortality at 90 days did not differ (HR 1.02...). We did not measure adherence." |
| D5 Reassuring coda | "...a promising tool that may transform diagnosis. Further research is needed." | "...sensitivity 0.91 (95% CI 0.84 to 0.95). A multicentre study with radiography in all participants would show whether this holds outside one expert group." |
| D8 Advocacy | "Although performance was slightly lower in women (0.84 vs 0.90), this is unlikely to be clinically meaningful." | "AUROC was lower in women than in men (0.84 vs 0.90)." |
| S1 -ing tail | "Time to antibiotics fell from 94 to 61 minutes, highlighting the effectiveness of decision support." | "Time to antibiotics fell from 94 to 61 minutes." |
| S6 Hedge stack | "may suggest that X could potentially have a possible beneficial effect" | "suggest that X may reduce falls in [population]" |
| S14 Staging | "At its core, the central question of this study was whether..." | (deleted; the paragraph opens on the finding) |
| S15 Strawman | "One might argue that patients with severe dementia cannot participate, but our findings suggest otherwise." | "Of the 1,146 patients, [DATA NEEDED: n (%)] were mobilized within 24 hours, including [DATA NEEDED: n/N (%)] of those with severe dementia." |

[`examples/README.md`](examples/README.md) has more examples from v1.0 with change notes.

## Benchmark Results

The skill was tested in three passes. Every output, grade, judge verdict, and script is in [`benchmarks/`](benchmarks/).

| Pass | Skill versions | Models | Cases | Runs |
|---|---|---|---|---|
| 1 | v1.0 vs no skill (after a v0.9 pilot) | Claude Opus 5.5, Claude Haiku 5.5 | 3 | 18 (6 of them in the v0.9 pilot) |
| 2 | v1.1 vs no skill | Claude Opus 5.5 | 9 | 18 |
| 3 | v1.1 vs v1.0 vs no skill | 8 models via OpenRouter (below) | 9 | 216 |

### The test cases

Each case is a realistic request with a set of pass/fail assertions, 63 in total, defined in [`skills/medical-scientific-writing/evals/`](skills/medical-scientific-writing/evals/).

| Case | What it tests |
|---|---|
| Case report Discussion | Rewrite an AI-styled draft without inventing facts; flag an uncited statistic; restore the diagnostic delay the draft glossed over |
| Cohort Results + Discussion | Draft from bullet-point data with null secondary outcomes and a non-significant subgroup interaction; one supplied reference doesn't support the claim made about it |
| Introduction, no references | Tighten without inventing citations; end on the aim |
| Clean human abstract | **Over-editing check:** a well-written human abstract should come back almost untouched |
| Staging and strawman Discussion | The v1.1 patterns: staged run-ups, aphorisms, rebutting objections nobody raised, closing verdicts, guessing at missing data |
| LaTeX file, edited in place | Every `\cite`, `\ref`, `\label` and the equation kept byte-identical; prose fixed |
| Reviewer response | Lead each reply with the decision, cut the flattery, and describe no change the authors didn't make |
| Author's own voice | Match a writing sample from the author, including the em dashes the default rules would remove |
| Audit only | Produce a findings table without rewriting; rate the causal overclaim as the most severe; leave correct "associated with" alone |

### Pass 1: v1.0 on Claude (3 cases)

| Model | With skill v1.0 | Without skill |
|---|---|---|
| Claude Opus 5.5 | 23/23 | 22/23 |
| Claude Haiku 5.5 | 23/23 | 22/23 |

Revisions with the skill took the AI-styled drafts from 20 and 13 pattern phrases down to 0, and came out 26–58% shorter than revisions without it. Each task took 51–82 seconds longer and used 36–45k more tokens, because the skill reads its references and runs its checker.

### Pass 2: v1.1 on Claude Opus 5.5 (9 cases)

| | With skill v1.1 | Without skill |
|---|---|---|
| Assertions passed | **63/63** | 62/63 |

Words in the finished text:

| Case | Draft | With skill | Without skill |
|---|---|---|---|
| Clean human abstract | 230 | 230 (unchanged) | 230 (unchanged) |
| Case report Discussion | 248 | 308 | 409 |
| Introduction | 220 | 124 | 304 |
| Staging/strawman Discussion | 199 | 174 | 382 |
| LaTeX Results | 136 | 101 | 97 |
| Reviewer response | 374 | 248 | 221 |
| Author's voice paragraph | 101 | 68 | 86 |

- **No over-editing:** both configurations returned the clean abstract byte-identical and told the author it was already fine.
- **No ballooning:** without the skill, Opus expanded three of the seven revisions by 38–92%, mostly by adding interpretation and limitations nobody asked for.
- **v1.1 is tighter than v1.0:** on the two cases both versions ran, v1.1's output was shorter (case report 327 → 308 words, introduction 151 → 124).

### Pass 3: eight models from five providers, three configurations

Models, all accessed through OpenRouter:

| Provider | Models |
|---|---|
| OpenAI | GPT-6.2 Sol, GPT-6.2 Astra, GPT-6.1 Terra |
| Google | Gemini 4 Neon |
| xAI | Grok 4.7 |
| DeepSeek | DeepSeek V4.1 Flash |
| Qwen | Qwen4 Max, Qwen 3.8 27B (a popular local model) |

These models can't load Claude skills. Each one got `SKILL.md` and the reference files as its system prompt, with no tools, so it couldn't run the checker script or search the literature. That makes this a harder test than the Claude passes.

**Assertions passed (of 63):**

| Model | No skill | Skill v1.0 | Skill v1.1 |
|---|---|---|---|
| GPT-6.2 Sol | 53 | 57 | 60 |
| GPT-6.2 Astra | 52 | 56 | 60 |
| GPT-6.1 Terra | 54 | 58 | 61 |
| Gemini 4 Neon | 57 | 62 | 62 |
| Grok 4.7 | 52 | 61 | 62 |
| DeepSeek V4.1 Flash | 51 | 60 | 60 |
| Qwen4 Max | 51 | 56 | 62 |
| Qwen 3.8 27B | 51 | 58 | 61 |
| **All models** | **421/504 (84%)** | **468/504 (93%)** | **488/504 (97%)** |

**By case (all 8 models):**

| Case | No skill | v1.0 | v1.1 |
|---|---|---|---|
| Case report Discussion | 44/56 | 55/56 | 56/56 |
| Cohort Results + Discussion | 57/64 | 61/64 | 62/64 |
| Introduction, no references | 51/64 | 64/64 | 63/64 |
| Clean human abstract | 38/56 | 47/56 | 50/56 |
| Staging and strawman Discussion | 57/64 | 57/64 | **63/64** |
| LaTeX file, edited in place | 54/56 | 56/56 | 56/56 |
| Reviewer response | 39/48 | 40/48 | **44/48** |
| Author's own voice | 34/40 | 34/40 | **38/40** |
| Audit only | 47/56 | 54/56 | 56/56 |

The v1.1 gains came on the three cases that test what v1.1 added (in bold), which suggests they come from the new rules rather than noise.

**Length, leftover patterns, and over-editing:**

| Model | Median length change on revisions: none / v1.0 / v1.1 | Leftover AI-pattern phrases: none / v1.0 / v1.1 | Clean-abstract similarity: none / v1.0 / v1.1 |
|---|---|---|---|
| GPT-6.2 Sol | −22% / −31% / −31% | 1 / 0 / 0 | 0.77 / 0.80 / 0.79 |
| GPT-6.2 Astra | −19% / −25% / −32% | 0 / 2 / 0 | 0.78 / 0.80 / 0.80 |
| GPT-6.1 Terra | −29% / −33% / −36% | 5 / 2 / 0 | 0.93 / 0.95 / 0.96 |
| Gemini 4 Neon | −18% / −33% / −32% | 2 / 2 / 1 | 1.00 / 1.00 / 1.00 |
| Grok 4.7 | 0% / −40% / −29% | 4 / 2 / 0 | 0.85 / 1.00 / 0.98 |
| DeepSeek V4.1 Flash | −2% / −18% / −19% | 12 / 0 / 1 | 0.98 / 0.93 / 0.97 |
| Qwen4 Max | +82% / −22% / −26% | 6 / 0 / 0 | 0.84 / 0.88 / 0.88 |
| Qwen 3.8 27B | +10% / −30% / −30% | 15 / 5 / 2 | 0.91 / 1.00 / 0.97 |

"Similarity" is the difflib character ratio between the clean human abstract and the returned version, where 1.00 means untouched. Leftover phrases are summed over the seven revision cases.

### How the outputs were judged

- **Script-graded checks:** 45 of the 63 assertions per run are checked by script ([`benchmarks/tools/`](benchmarks/tools/)). Examples: numbers kept, no invented numbers, LaTeX commands byte-identical, word counts, and banned phrases.
- **Judged checks:** the other 18 need reading. Examples: does the audit rate "prevents death" as the most severe problem, does each reviewer reply open with the decision, does the cohort draft name a study the author didn't supply.
- **Two blind judges:** in pass 3, those 18 were graded by two judges from different providers, Claude Opus 5.5 and GPT-6.2 Sol. Each judge saw the task, the input files, and the output, but never the model name or configuration.
- **Strict pass rule:** an assertion passes only if **both** judges pass it.
- **Agreement:** the judges agreed on 417 of 432 verdicts (96.5%). Most disagreements were GPT-6.2 Sol failing replies that open with "We agree." and name the change in the next sentence.
- **Script checks alone give the same ordering:** 87% no skill, 94% v1.0, 97% v1.1.
- **In passes 1 and 2,** the judged checks were graded by hand with quoted evidence, recorded in each round's `manual.json`.

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

## Repository Layout

```
.claude-plugin/              plugin + marketplace manifests (Claude Code)
skills/medical-scientific-writing/
  SKILL.md                   workflow, integrity rules, pattern index
  references/                pattern catalog, section guide, evidence & reporting,
                             clarity toolkit, source notes
  scripts/check_patterns.py  mechanical checker (Python 3, standard library)
  evals/                     9 test cases (runnable with `claude plugin eval`)
examples/                    more before/after examples with change notes
benchmarks/
  iteration-1, -2, -2-haiku  pass 1: v0.9 pilot and v1.0 on Claude Opus and Haiku
  iteration-3/               pass 2: v1.1 on Claude Opus, 9 cases
  cross-model/               pass 3: 8 models x 3 configurations, judge verdicts, harness
  tools/                     grading and metrics scripts
dist/                        zip for claude.ai / Claude Desktop upload
```

To rerun the test cases with Claude Code: `cd skills/medical-scientific-writing && claude plugin eval . --allow-tools Write,Edit,Bash --scaffold`. These are billed model runs.

## Sources and Credits

The skill combines and reconciles these sources. Where they conflict, [`references/source-notes.md`](skills/medical-scientific-writing/references/source-notes.md) records the decision and the reason. For example, the em dash, "Notably", and "add personality" rules are resolved there.

| Source | What it contributed |
|---|---|
| Russell J, Rajendhran R, Pham CM, Iyyer M, Wieting J. [*StoryScope: Investigating idiosyncrasies in AI fiction.*](https://arxiv.org/abs/2604.03136) arXiv:2604.03136 (CC0) | The discourse layer (D1 to D7) and the swap test |
| [blader/humanizer](https://github.com/blader/humanizer) (MIT), built on Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | Upstream of the humanizer patterns. v4.0.0 was reviewed for v1.1.0 and contributed evidence tiers, staging and aphorisms, arguing with no one, split negatives, gap-filling guesses, and the author-sample override |
| [matsuikentaro1/humanizer_academic](https://github.com/matsuikentaro1/humanizer_academic) (MIT) | The strict fidelity rule and `[DATA NEEDED]` placeholders, calibrated hedging, connective-preserving edits, the sentence-rhythm criterion, and the design of the checker script |
| [eniktab/scientific-paper-writer](https://github.com/eniktab/scientific-paper-writer) (MIT) | Integrity rules (verified citations only), outline-then-prose drafting, IMRaD tense and voice, Introduction and Discussion moves, grant, cover-letter, and reviewer-response templates |
| [HeartWise-AI/ai-writing-skills](https://github.com/HeartWise-AI/ai-writing-skills) (MIT) | The advocacy check, symmetric reporting, limitations without rebuttal, the length and density check, and the clinical-meaning check |
| [noora-noureldin2000/Skills-for-MedicalResearch-writing](https://github.com/noora-noureldin2000/Skills-for-MedicalResearch-writing) | Gap and purpose-statement formulas, CARE case reports, ICMJE requirements including AI disclosure, a five-pass clarity audit, and overclaiming checks |
| [quanghuy0497/Writing-in-the-Sciences](https://github.com/quanghuy0497/Writing-in-the-Sciences) | Notes on Kristin Sainani's Stanford course *Writing in the Sciences*: cutting clutter, active voice and strong verbs, paragraph structure, and writing for lay readers |
| [ashryaagr/karpathy-output-style](https://github.com/ashryaagr/karpathy-output-style) (MIT), with ASD-STE100 Simplified Technical English, Issue 9 | The plain-English mode for lay summaries |

The patterns were rewritten and reorganized, and all examples were newly written. No source text was copied wholesale.

## Caveats

- **GPT-6.2 models changed the most.** GPT-6.2 Sol and GPT-6.2 Astra rewrote the clean human abstract in every configuration, including with v1.1, to a similarity of about 0.8. They restructured sentences and swapped out the correct statistical phrase "associated with" (4 occurrences down to 2 for Astra and 3 for Sol with v1.1), even though v1.1 has a rule protecting it. No numbers were lost, but they did not do the light touch a clean draft needs. With the skill, Gemini 4 Neon, Grok 4.7, DeepSeek V4.1 Flash, Qwen 3.8 27B, and GPT-6.1 Terra left it nearly untouched (similarity 0.96 to 1.00). If you use a GPT-6.2 model, check its edits against your original.
- **The skill doesn't fix everything.** v1.1 still missed 16 of 504 checks across the eight models. The most common misses:
  - GPT-6.2 over-editing the clean abstract (5);
  - reviewer replies that open with "We agree." or background before stating the decision (4);
  - the author's em dashes dropped by GPT-6.1 Terra and Qwen 3.8 27B (2);
  - GPT-6.x drafts hedging the null secondary outcomes instead of stating them plainly (2).
- **One run per cell.** Each model, configuration, and case ran once. A one- or two-assertion difference for a single model is within noise; the totals and the per-case pattern are more reliable.
- **The author wrote the tests.** The skill's author wrote the cases and assertions, and the leftover-pattern counts use the skill's own phrase list. No blinded human editors have rated the outputs yet.
- **One judge is a Claude model,** the same family that helped write the skill. That's why a second judge from another provider was used and both had to agree. The script-graded checks alone show the same ordering.
- **Pass 3 used no tools.** The OpenRouter models got the skill as a system prompt and couldn't run the checker or search PubMed. The Claude passes ran as agents with tools. Results across passes aren't directly comparable.
- **Format failures were retried.** Four of 216 runs didn't return their file on the first try (Grok 4.7 twice, Qwen 3.8 27B twice) and got one retry. The first attempts are kept in `benchmarks/cross-model/results/` as `*.attempt1`.
- **One grader was fixed after the run.** The case-report check for the FDA recommendation now also accepts "US Food and Drug Administration". GPT-6.2 Sol spelled it out in all three configurations.
- **Model names and prices change.** The models were current on OpenRouter on 2026-11-20. Pass 3 cost $18.58 in API credit, judging included.

## Disclaimer

This skill helps with writing. It doesn't provide medical advice, and it doesn't replace author responsibility, peer review, or a journal's own requirements. Verify every placeholder, every suggested reference, and every clinical statement before submission.

## License

[MIT](LICENSE)
