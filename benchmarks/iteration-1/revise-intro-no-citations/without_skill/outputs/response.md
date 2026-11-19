The revised intro is saved to `intro_revised.txt`. It's about 425 words in four paragraphs: burden and the screening context, what the devices do and where the current evidence falls short, why adults 75+ need their own validation, and your objectives. I marked every spot that needs a citation with `[REF]` (11 in all), and I added no numbers, so you won't have any unsourced statistics to chase down.

## What changed and why

**1. Dropped the stroke-benefit claim.** "Early detection of AF may lead to improved outcomes, including reduced stroke risk" is the claim reviewers are most likely to attack. The evidence is genuinely mixed. STROKESTOP and LOOP found small or non-significant effects. NOAH-AFNET 6 and ARTESiA found little net benefit from anticoagulation for short device-detected AF. Your study measures accuracy, not outcomes, so it doesn't need that claim. I replaced it with the guideline positions: ESC says screening can be considered at 75+, and USPSTF calls the evidence insufficient. That tells the reader the question matters and doesn't overstate the case.

**2. Made the evidence gap specific.** The draft said accuracy in older adults "remains poorly understood," which reviewers will read as filler. The revision names two concrete problems with earlier studies:
- Older adults were underrepresented in them.
- Many verified rhythm only in people who got a notification, which causes partial verification bias.

Your 14-day patch in every participant fixes the second problem directly. That's your biggest methodological strength, and the intro now sets it up.

**3. Built out the older-adult rationale.** I kept your comorbidity list and added two points that matter in this age group:
- **Usability.** Taking a 30-second ECG with tremor, arthritis, or cognitive impairment is harder.
- **Prevalence.** Predictive values change with prevalence, so PPV and NPV from younger cohorts don't carry over.

**4. Cut the promotional wording.** I removed "transform the landscape," "critical gap," "comprehensive," "rapidly evolving field," and the last sentence ("fills an important gap... pave the way for future research"). Reviewers and editors penalize these phrases, and claims about significance belong in the Discussion.

**5. Turned the closing paragraph into objectives.** It now states the index test, the reference standard, the primary endpoints (sensitivity and specificity) and the secondary endpoints. That matches STARD 2015 item 4 (study objectives and hypotheses).

## Placeholders you need to fill in
- `[DEVICE NAME, MODEL, ALGORITHM/SOFTWARE VERSION]`: algorithm version matters because accuracy changes between releases.
- `[the PPG-based irregular rhythm notification and/or the single-lead ECG classification]`: I couldn't tell from the draft which one is your index test. Pick one or both, and keep it consistent with Methods.
- **Unit of analysis.** I wrote "at the participant level." Change it if you analyzed per recording or per episode.
- **Secondary objectives and subgroups.** These are my assumptions, so cut or change them to match your protocol and SAP. Only list subgroups you actually prespecified.

## Suggested sources for the [REF] slots
These are the standard citations for each claim. Check every one, and its exact wording, before you cite it:
- **AF epidemiology and age-related prevalence:** GBD AF burden estimates, or the epidemiology section of the 2024 ESC AF guideline (Van Gelder et al., *Eur Heart J* 2024) or the 2023 ACC/AHA/ACCP/HRS guideline.
- **Undiagnosed or asymptomatic AF:** the same guidelines, or the screening literature (e.g., the AF-SCREEN collaboration).
- **ESC screening recommendation for age 75+:** 2024 ESC AF guideline. Check the exact wording and class of recommendation.
- **USPSTF:** USPSTF Recommendation Statement, *JAMA* 2022.
- **Smartwatch accuracy and the large pragmatic studies:** Apple Heart Study (Perez et al., *NEJM* 2019), Huawei Heart Study (Guo et al., *JACC* 2019), Fitbit Heart Study (Lubitz et al., *Circulation* 2022), and a recent systematic review or meta-analysis of smartwatch AF detection.
- **Older adults underrepresented / partial verification:** the Apple Heart Study's age breakdown (check the proportion aged 65 and older) and its design, where only notified participants got patches.
- **PPG signal-quality confounders and ECG usability in older adults:** smartwatch validation studies in elderly or hospitalized populations. Wording such as "frequent ectopy produces false positives" should be backed by a primary study, not only a review.

## Assumptions
- The study is finished. I kept your past tense ("we conducted").
- The target journal uses a standard clinical intro of about 300–500 words with numbered citations. If it caps the intro lower (some cap at about 250 words), the third paragraph is the easiest to shorten.
- I used US spelling and plain text to match your draft.

Optionally, if you want to acknowledge the outcome trials, you could add one sentence to the first paragraph: "Randomized screening trials have reported modest or non-significant reductions in stroke [REF]." It isn't needed for a diagnostic accuracy paper, though.
