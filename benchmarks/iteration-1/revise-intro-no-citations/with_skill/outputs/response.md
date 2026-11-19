I treated this as a revision of the Introduction for a prospective diagnostic accuracy study (STARD 2015), in US English and AMA style with no specific journal. The revised version is saved to `intro_revised.txt`:

---

Introduction

Atrial fibrillation (AF) is the most common sustained cardiac arrhythmia, and its prevalence rises with age [CITATION NEEDED: age-specific AF prevalence, including adults aged 75 years and older]. Earlier detection of AF may lead to better outcomes, including lower stroke risk [CITATION NEEDED: outcome data from AF screening studies]. Smartwatches equipped with photoplethysmography (PPG) and single-lead electrocardiography (ECG) can detect AF outside the clinic, and their use among older adults is increasing [DATA NEEDED: ownership or use figure for adults aged 75 years and older, with source].

In validation studies, smartwatch algorithms have detected AF with high sensitivity ([DATA NEEDED: range]) and specificity ([DATA NEEDED: range]) [CITATION NEEDED: key validation studies, with design, population, and reference standard for each]. Few of these studies have reported accuracy separately in adults aged 75 years and older [CITATION NEEDED: age distribution of participants in the cited validation studies], so how well the devices perform in the age group in which AF is most prevalent is uncertain. Older adults often have tremor, peripheral vascular disease, or frequent ectopy. Tremor can add motion artifact to PPG and ECG recordings, and peripheral vascular disease can weaken the PPG signal; frequent ectopy produces an irregular rhythm that an algorithm may classify as AF [CITATION NEEDED: studies of these sources of error in wearable AF detection]. Accuracy estimates from younger cohorts may therefore not hold in older adults.

We prospectively evaluated the diagnostic accuracy of a commercially available smartwatch [DATA NEEDED: device model, software or algorithm version, and detection mode (PPG irregular-rhythm notification, ECG, or both)] for detecting AF in adults aged 75 years and older, using 14-day continuous patch monitoring as the reference standard.

---

**What changed**

- **Structure:** I cut the generic opening ("major global health burden, affecting millions", "growing interest in recent years") and the first paragraph now gets to age, earlier detection, and smartwatches within three sentences. The Introduction ends on the study aim. I deleted the last sentence ("not only fills an important gap... pave the way for future research") because it is self-promotion and does not belong in an Introduction.
- **Unsupported claims:** "Studies have shown" and "a growing body of evidence" now say what each claim needs (numbers, design, population) and have placeholders where the references go. "Remains poorly understood" is now a specific gap: few studies report accuracy separately for adults aged 75 years and older.
- **The comorbidity sentence:** the ", highlighting the need for..." tail is gone. I matched each comorbidity to how it causes error: tremor causes motion artifact, peripheral vascular disease weakens the PPG signal, and frequent ectopy causes misclassification. Ectopy confuses the algorithm's rhythm classification rather than degrading signal quality, so "affect signal quality" was slightly wrong for it. Please confirm you agree.
- **Word level:** I removed the em dash, "Furthermore" and "Moreover" (two in one paragraph), "promising tools that could potentially transform the landscape" (a stacked hedge plus filler), "critical gap", "comprehensive", and "pave the way".
- **Aim sentence:** I changed it to "We prospectively evaluated" and added a placeholder for the index test details that STARD expects in the Introduction and Methods.

**Fidelity:** the meaning of every claim in the draft is kept, including the 75-year threshold, the PPG/ECG modalities, the three comorbidities, and the 14-day patch reference standard. I added no numbers or references, and the checker found nothing added or lost. The prose without placeholders is shorter than your draft. The word count went up from 220 to 278 only because of the bracketed placeholders.

**Placeholders and author queries**

1. Nine placeholders are in the text (7 claims need a citation, plus 2 sensitivity/specificity ranges). Replace each with the specific study and its numbers, not just a reference number. For example: "In [study], [n] participants, [reference standard], sensitivity X% (95% CI)."
2. **Stroke benefit of screening:** keep the "may". As far as I know, the trial evidence on whether screening-detected AF reduces stroke is mixed. Cite it as it stands instead of implying an established benefit, or frame it as a hypothesis.
3. **Smartwatch use among older adults:** your draft said "growing interest", and I made it "use... is increasing" so the sentence can carry an actual number. If you have no figure, delete the clause.
4. **"Few of these studies have reported accuracy separately in adults aged 75 years and older":** this is how I read your "remains poorly understood". It only holds if the age distributions of the cited cohorts support it, so check it against the studies you cite.
5. **Aim:** if you have a prespecified primary measure, state it here: sensitivity and specificity, per participant or per episode, and any target sensitivity used for the sample size.

**Candidates for you to verify** (from memory, not checked, and not in the text):
- Validation and large cohort studies: Apple Heart Study (Perez et al., NEJM 2019), Fitbit Heart Study (Lubitz et al., Circulation 2022), Huawei Heart Study (Guo et al., JACC 2019). Older adults may be a small fraction of participants in these, which would support point 4.
- Screening outcome trials and guidance: STROKESTOP (Svennberg et al., Lancet 2021), LOOP (Svendsen et al., Lancet 2021), GUARD-AF, and the 2022 USPSTF statement on AF screening.
- Age-specific prevalence: ATRIA (Go et al., JAMA 2001).

One more thing for submission: most journals, and the ICMJE recommendations, require you to disclose AI-assisted writing.
