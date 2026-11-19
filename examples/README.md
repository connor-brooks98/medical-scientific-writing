# Before and after examples

All three inputs are AI-styled drafts written for testing. The "after" texts are real outputs from the benchmark runs (Claude Opus 5.5 with this skill, v1.0), copied unedited from `benchmarks/iteration-2/`. The same task run without the skill is in the matching `without_skill/` folder, so you can compare all three versions.

## 1. Case report Discussion and Conclusion

Task given to the model: "I used ChatGPT to help draft the discussion and conclusion and honestly it reads super AI. Can you rewrite the Discussion and Conclusion so it sounds like an actual case report a journal would take? Keep all the facts the same." The full draft, including the Case Presentation the rewrite draws on, is in `skills/medical-scientific-writing/evals/revise-case-report-discussion/files/case_report_draft.md`.

### Before (AI-styled draft, 248 words)

**Discussion**

Euglycemic diabetic ketoacidosis (euDKA) represents a rare but potentially life-threatening complication of sodium-glucose cotransporter-2 (SGLT2) inhibitor therapy that has garnered increasing attention in the evolving landscape of diabetes management. SGLT2 inhibitors—which have revolutionized the treatment of type 2 diabetes, heart failure, and chronic kidney disease—promote glycosuria, reduce insulin requirements, and enhance ketogenesis, creating a perfect storm for ketoacidosis in the perioperative setting.

Studies have shown that the risk of DKA is increased up to three-fold in patients receiving SGLT2 inhibitors. Notably, the absence of marked hyperglycemia can delay diagnosis, highlighting the critical importance of measuring ketones in any patient on these agents who presents with nausea, vomiting, or malaise. Furthermore, surgical stress, prolonged fasting, and reduced carbohydrate intake serve as key precipitating factors, underscoring the need for comprehensive perioperative protocols.

The FDA recommends that empagliflozin be discontinued at least 3 days before scheduled surgery [5]. In our patient, the drug was continued until the day before surgery, and this likely contributed to the development of euDKA. Prompt recognition and initiation of insulin and dextrose therapy led to complete resolution, demonstrating the effectiveness of a multidisciplinary approach.

**Conclusion**

This case highlights the importance of maintaining a high index of suspicion for euDKA in postoperative patients taking SGLT2 inhibitors. It serves as a valuable reminder that normal glucose levels do not exclude DKA. Clinicians, surgeons, and anesthesiologists must work together to ensure safe perioperative management. Further research is needed to establish optimal strategies for preventing this potentially fatal complication.

### After (with the skill, 327 words)

**Discussion**

On the first day after laparoscopic cholecystectomy, our patient developed euglycemic diabetic ketoacidosis (euDKA), an uncommon but life-threatening complication of sodium-glucose cotransporter-2 (SGLT2) inhibitor therapy [CITATION NEEDED: incidence and outcome data for euDKA with SGLT2 inhibitors]. The risk of DKA has been reported to be up to three-fold higher in patients taking these drugs [CITATION NEEDED: source of the three-fold estimate]. SGLT2 inhibitors, used in type 2 diabetes, heart failure, and chronic kidney disease, promote glycosuria, reduce insulin requirements, and enhance ketogenesis, so ketoacidosis can develop while glucose is only modestly raised. Surgical stress, prolonged fasting, and reduced carbohydrate intake are recognized precipitants; our patient had surgery after a 14-hour fast and was vomiting on POD 1.

The diagnosis was delayed. Her nausea, vomiting, and abdominal discomfort were attributed to postoperative ileus and opioid analgesia, and without marked hyperglycemia (capillary glucose 182 mg/dL) there was no prompt to look for ketoacidosis. The venous blood gas that evening showed an anion-gap acidosis (pH 7.12, anion gap 24 mmol/L, lactate 1.4 mmol/L), but euDKA was diagnosed approximately 14 hours later. Measuring ketones in a patient taking an SGLT2 inhibitor who presents with nausea, vomiting, or malaise identifies ketoacidosis regardless of the glucose value. We cannot tell from one case whether doing so when her symptoms began would have shortened her course.

The FDA recommends that empagliflozin be discontinued at least 3 days before scheduled surgery [5]. Our patient was instructed to hold metformin on the morning of surgery, but empagliflozin was continued until the day before surgery; taking it inside the recommended window likely contributed to euDKA. She recovered with an insulin infusion and concurrent 10% dextrose; the anion gap closed after 38 hours.

**Conclusion**

A modestly raised glucose, such as this patient's 182 mg/dL, does not exclude DKA in patients taking SGLT2 inhibitors, and postoperative nausea, vomiting, or malaise in these patients should prompt ketone measurement even when another cause seems likely. Preoperative instructions should address SGLT2 inhibitors as explicitly as this patient's instructions addressed metformin, using the FDA's 3-day discontinuation interval [5].

### What changed

- **Stated morals removed (D1):** "highlights the importance of maintaining a high index of suspicion", "serves as a valuable reminder", "must work together".
- **Contradicted claim removed:** the draft credited "prompt recognition". The Case Presentation shows the symptoms were first attributed to ileus and opioids and that the diagnosis came about 14 hours after the first abnormal gas. That delay is the teaching point, and it now has its own paragraph (D3).
- **Unsupported claim removed:** "demonstrating the effectiveness of a multidisciplinary approach" was replaced with what one case can and cannot show (D4).
- **Uncited statistic flagged:** "Studies have shown ... up to three-fold" now carries a `[CITATION NEEDED]` placeholder instead of an unnamed source (D2).
- **Coda replaced:** "Further research is needed" became two concrete clinical actions (D5).
- **Surface tells removed:** em dashes, "evolving landscape", "garnered", "revolutionized", "perfect storm", "Notably", "Furthermore", and the -ing tails ("highlighting...", "underscoring...").
- **Fidelity:** every number and the citation [5] survive. The numbers added to the Discussion (182 mg/dL, pH 7.12, 14 hours, 38 hours) come from the draft's own Case Presentation.

## 2. Introduction with no references yet

Task: "can you make this intro publication ready? it's for a diagnostic accuracy study (smartwatch AF detection in 75+). I haven't added refs yet."

### Before (AI-styled draft, 220 words)

Introduction

Atrial fibrillation (AF) is the most common sustained cardiac arrhythmia and represents a major global health burden, affecting millions of individuals worldwide. In recent years, there has been growing interest in the role of wearable devices in the detection and management of AF. Smartwatches equipped with photoplethysmography (PPG) and single-lead electrocardiography (ECG) have emerged as promising tools that could potentially transform the landscape of arrhythmia screening.

Studies have shown that smartwatch-based algorithms can detect AF with high sensitivity and specificity. Furthermore, a growing body of evidence suggests that early detection of AF may lead to improved outcomes, including reduced stroke risk. However, the accuracy of these devices in older adults—who bear the greatest burden of AF—remains poorly understood. Moreover, older adults often have comorbidities such as tremor, peripheral vascular disease, and frequent ectopy that may affect signal quality, highlighting the need for population-specific validation.

To address this critical gap, we conducted a comprehensive prospective study to evaluate the diagnostic accuracy of a commercially available smartwatch for detecting AF in adults aged 75 years and older, using 14-day continuous patch monitoring as the reference standard. This study not only fills an important gap in the literature but also provides valuable insights that will inform clinical practice and pave the way for future research in this rapidly evolving field.

### After (with the skill, 151 words outside placeholders)

Introduction

Atrial fibrillation (AF) is the most common sustained cardiac arrhythmia, and its prevalence is highest in older adults [CITATION NEEDED: AF prevalence by age, ideally in adults aged 75 years and older]. Detecting AF earlier may reduce stroke risk [CITATION NEEDED: screening trials reporting stroke outcomes]. Smartwatches can now screen for AF using photoplethysmography (PPG), single-lead electrocardiography (ECG), or both.

In validation studies, smartwatch algorithms detected AF with a sensitivity of [DATA NEEDED: sensitivity] and a specificity of [DATA NEEDED: specificity] [CITATION NEEDED: key validation studies, with design, population, and reference standard]. However, few of these studies enrolled adults aged 75 years and older [CITATION NEEDED: age distribution of validation cohorts], so their estimates may not apply to the age group in which AF is most common. Older adults also often have conditions that can impair detection. Tremor and peripheral vascular disease can degrade the PPG and ECG signal, and frequent ectopy produces irregular rhythms that an algorithm may misclassify as AF.

We conducted a prospective study of the diagnostic accuracy of a commercially available smartwatch for detecting AF in adults aged 75 years and older, with 14-day continuous patch monitoring as the reference standard.

### What changed

- **Generic preamble cut (D6):** "a major global health burden, affecting millions of individuals worldwide" and "In recent years, there has been growing interest".
- **Vague allusions turned into placeholders (D2):** "Studies have shown" and "a growing body of evidence" now say exactly what each claim needs a citation for. No reference was invented.
- **Gap made specific:** "remains poorly understood" became a checkable claim about which age groups earlier validation studies enrolled. The comorbidity sentence now says how each condition causes error.
- **Self-praise removed (D4, D5):** "To address this critical gap, we conducted a comprehensive...", "not only fills an important gap", "pave the way". The intro now ends on the aim.
- **Shorter:** 151 words of prose against 220. The same model without the skill produced 357.

## 3. Hand-written illustration (immune checkpoint inhibitor myocarditis)

This example was written for the skill's pattern catalog to show every layer at once. See the end of `skills/medical-scientific-writing/references/pattern-catalog.md`.

## 4. Drafting from data (no "before")

For new writing, the skill drafts against the patterns from the start. `benchmarks/iteration-2/draft-cohort-results-discussion/with_skill/outputs/draft_sections.md` is a Results, Discussion, and Limitations draft for a retrospective cohort, written from bullet-point data. It reports the null secondary outcomes and the non-significant sex interaction as plainly as the primary result, uses association language throughout, and flags that one of the user's supplied citations does not say what the user thought it said.
