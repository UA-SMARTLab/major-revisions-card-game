# Major Revisions: flaw key

Generated from `data/` by `tools/build.py`. Don't edit by hand.

The verdict for a manuscript is the most severe verdict among its planted flaws (Reject > Major revisions > Minor revisions); a manuscript with no flaw gets Accept.

## S1 · Back on track (Randomised trial, CONSORT 2025)

> A 12-week supervised exercise programme improves physical function in adults with chronic low back pain.

**Question.** *As submitted:* Does a 12-week exercise programme improve function in chronic low back pain, compared with usual care?

- Registration (CONSORT 2025 item 2–3): sound: Registered before the first patient, with function at 12 weeks as primary outcome, as in the paper.
  - **Flawed (Switched after registration, Major revisions):** Registered with pain at 12 weeks as primary outcome. The paper makes function primary and never says why.
  - *Why:* Switching the primary outcome after seeing the data lets a chance finding pass as the main result. Fixable: report the registered outcome as primary and explain the change. See [Goldacre et al. (2019). COMPare: a prospective cohort study correcting and monitoring 58 misreported trials in real time. Trials.](https://doi.org/10.1186/s13063-019-3173-2).
- Prespecified aims (CONSORT 2025 item 7): sound: Hypothesis stated: the programme improves the function score by at least 3 points more than usual care.

**Method.** *As submitted:* Randomised trial in four clinics; patients allocated 1:1 to supervised exercise or usual care.

- Randomisation (CONSORT 2025 item 17a–19): sound: Computer-made sequence in random blocks, released by a central web service only after enrolment.
  - **Flawed (Predictable allocation, Reject):** Patients seen on Mondays and Wednesdays got exercise; patients seen on other days got usual care.
  - *Why:* Staff could foresee each allocation and steer who was enrolled on which day, so the groups may differ from the start. No reanalysis can undo that. See [Schulz et al. (1995). Empirical evidence of bias: dimensions of methodological quality associated with estimates of treatment effects in controlled trials. JAMA.](https://doi.org/10.1001/jama.1995.03520290060030).
- Intervention details (CONSORT 2025 item 13): sound: Two supervised sessions a week for 12 weeks; the full exercise protocol is in a supplement.

**Sample.** *As submitted:* 240 adults with low back pain for more than 3 months, referred by their GPs.

- Recruitment (CONSORT 2025 item 12a): sound: All consecutive referrals screened against published criteria; 240 of 412 eligible and consenting.
  - **Flawed (Hand-picked participants, Minor revisions):** Physiotherapists enrolled only patients they judged 'motivated to exercise'; no written criteria.
  - *Why:* Randomisation still balances the groups, so the comparison is fair, but the result may not apply to typical patients. Minor: report it and narrow the claims. See [Rothwell (2005). External validity of randomised controlled trials: "to whom do the results of this trial apply?" The Lancet.](https://doi.org/10.1016/S0140-6736(04)17670-8).
- Flow diagram (CONSORT 2025 item 22a–b): sound: Flow diagram: 412 screened, 240 randomised, 226 analysed; losses similar per arm, with reasons.

**Measurement.** *As submitted:* Function scored with a standard performance test at 12 weeks.

- Blinding (CONSORT 2025 item 20a–b): sound: Tests scored by assessors from another clinic who did not know anyone's group.
  - **Flawed (Unblinded assessors, Reject):** Each patient's own physiotherapist scored the test, knowing who had the exercise programme.
  - *Why:* Assessors who know the groups tend to see the effect they expect. A 12-week performance test can't be repeated blind afterwards, so the main result can't be rescued. See [Hróbjartsson et al. (2013). Observer bias in randomized clinical trials with measurement scale outcomes: a systematic review of trials with both blinded and nonblinded assessors. CMAJ.](https://doi.org/10.1503/cmaj.120744).
- Measures (CONSORT 2025 item 14): sound: The performance test has published reliability and validity in low back pain.

**Analysis.** *As submitted:* Groups compared with a linear model adjusted for baseline function.

- Missing data (CONSORT 2025 item 21c): sound: 6% of outcomes missing, handled by multiple imputation; complete-case results agree.
- Analysis set (CONSORT 2025 item 21b, 26): sound: Every randomised patient analysed in the group they were assigned to.
  - **Flawed (Per-protocol only, Major revisions):** Only patients who attended at least 80% of sessions were analysed: 61 of 120 in the exercise arm.
  - *Why:* Dropping non-adherers breaks randomisation: people who keep exercising differ from those who stop. Fixable: reanalyse everyone as randomised (intention to treat). See [Hollis & Campbell (1999). What is meant by intention to treat analysis? Survey of published randomised controlled trials. BMJ.](https://doi.org/10.1136/bmj.319.7211.670).

## S2 · Late-night scrolling (Cohort study, STROBE)

> Heavy social-media use at age 13 predicts sleep problems at age 15.

**Question.** *As submitted:* Does heavy social-media use at age 13 predict sleep problems at age 15?

- Prespecified aims (STROBE item 3): sound: Hypothesis from the funded proposal, cited: more daily use, more sleep problems at 15, in girls and boys alike.
  - **Flawed (HARKing, Major revisions):** The introduction predicts an effect in girls only. The proposal predicted it for everyone; only girls showed it.
  - *Why:* A hypothesis written after the results makes a chance subgroup finding look like a confirmed prediction. Fixable: restore the original hypothesis and label the girls-only result exploratory. See [Kerr (1998). HARKing: hypothesizing after the results are known. Personality and Social Psychology Review.](https://doi.org/10.1207/s15327957pspr0203_4).
- Registration: sound: Not preregistered; the authors say so plainly in the limitations.

**Method.** *As submitted:* Prospective school-based cohort with questionnaires at ages 13 and 15.

- Setting and dates (STROBE item 5): sound: Use measured at 13 and sleep at 15, two years apart, at the same point in the school year.
  - **Flawed (Exposure after outcome, Reject):** Both were asked at 15: pupils recalled how much they had used social media two years earlier.
  - *Why:* Use at 13 is recalled after the sleep problems began, so the timing that made it a prediction is gone. Only data collected at 13 could fix this. See [Hill (1965). The environment and disease: association or causation? Proceedings of the Royal Society of Medicine.](https://doi.org/10.1177/003591576505800503).

**Sample.** *As submitted:* 3,000 pupils from 40 schools enrolled at 13; 2,310 followed up at 15.

- Flow diagram (STROBE item 13a–c): sound: Losses shown by school and reason; leavers and stayers had similar use and sleep at 13.
  - **Flawed (Selective loss to follow-up, Major revisions):** Heavy users were twice as likely to be lost by 15; leavers and stayers are never compared.
  - *Why:* If the heavy users who left slept differently, the estimate is biased. Fixable: compare leavers with stayers and correct with weighting or imputation. See [Kristman et al. (2004). Loss to follow-up in cohort studies: how much is too much? European Journal of Epidemiology.](https://doi.org/10.1023/B:EJEP.0000036568.02655.f8).
- Sample size (STROBE item 10): sound: Size set by the parent cohort; the paper reports the precision this gives the main estimate.

**Measurement.** *As submitted:* Sleep problems at 15 measured by questionnaire.

- Measures (STROBE item 7–8): sound: A validated adolescent sleep questionnaire, plus a week of wrist actigraphy in a subsample.
  - **Flawed (Unvalidated measure, Major revisions):** One yes/no item written for this study, 'Do you often sleep badly?', with no validation.
  - *Why:* One home-made yes/no item can't show it measures sleep problems. Fixable in part: use the cohort's fuller sleep measures, or validate the item in a subsample, and temper the claims. See [Flake & Fried (2020). Measurement schmeasurement: questionable measurement practices and how to avoid them. Advances in Methods and Practices in Psychological Science.](https://doi.org/10.1177/2515245920952393).

**Analysis.** *As submitted:* Logistic regression of sleep problems on hours of use, adjusted for confounders.

- Confounder adjustment (STROBE item 12a, 16a): sound: Adjusted for sleep, mood and family income at 13, chosen in advance from a causal diagram.
- Sensitivity analysis (STROBE item 12e): sound: Results hold with use in hours per day and with cut-offs at 2, 3 and 4 hours.
  - **Flawed (p-hacking, Major revisions):** Use was split at 3 hours after trying cut-offs from 1 to 5; only the one with p < 0.05 is reported.
  - *Why:* Trying many cut-offs and reporting the one that works inflates false positives. Fixable: analyse hours as a continuous measure, or show every cut-off. See [Simmons et al. (2011). False-positive psychology. Psychological Science.](https://doi.org/10.1177/0956797611417632).

## S3 · Sleeping pills and hip fracture (Case-control study, STROBE)

> Benzodiazepine use doubles the risk of hip fracture in people over 70.

**Question.** *As submitted:* Does benzodiazepine use raise the risk of hip fracture in people over 70?

- Prespecified aims (STROBE item 3): sound: Protocol hypothesis: benzodiazepine use raises hip-fracture risk. The paper tests that one question.
  - **Flawed (p-hacking, Major revisions):** Nine sleep medicines were tested. The headline is the one significant drug, with no correction for nine tests.
  - *Why:* With nine tests, one 'significant' result is likely by chance alone. Fixable: report all nine, correct for multiple testing, and call the single-drug finding exploratory. See [Simmons et al. (2011). False-positive psychology. Psychological Science.](https://doi.org/10.1177/0956797611417632).

**Method.** *As submitted:* Case-control study: 400 hip-fracture cases and 800 matched controls from two regions.

- Setting and dates (STROBE item 5): sound: Drug use counted only in the year before each case's fracture date, with the same window for its controls.
  - **Flawed (Exposure after outcome, Major revisions):** Drug use counted from 6 months before to 1 month after the fracture, when many start sleeping pills in hospital.
  - *Why:* Pills started because of the fracture are counted as its cause. Fixable: rerun the analysis with use before the fracture date only. See [Hill (1965). The environment and disease: association or causation? Proceedings of the Royal Society of Medicine.](https://doi.org/10.1177/003591576505800503).

**Sample.** *As submitted:* Cases from hospital admissions; controls matched on age and sex.

- Recruitment (STROBE item 6a): sound: Controls drawn at random from the same regions' population register.
  - **Flawed (Unsuitable controls, Reject):** Controls were volunteers recruited at senior fitness clubs.
  - *Why:* Fitness-club members take fewer sleeping pills and fall less than the population the cases came from, so the comparison is biased from the start. New controls are needed. See [Wacholder et al. (1992). Selection of controls in case-control studies. II. Types of controls. American Journal of Epidemiology.](https://doi.org/10.1093/oxfordjournals.aje.a116397).
- Flow diagram (STROBE item 13a–c): sound: 81% of cases and 76% of controls took part; reasons for refusal are reported.

**Measurement.** *As submitted:* Benzodiazepine use assessed in the same way for cases and controls.

- Measures (STROBE item 7–8): sound: Use taken from pharmacy dispensing records for cases and controls alike.
  - **Flawed (Recall bias, Major revisions):** Use recalled in interviews: cases on the ward days after their fracture, controls by phone.
  - *Why:* Cases search their memory harder, in a different setting, so their use is over-reported. Fixable in part: check the answers against pharmacy records. See [Coughlin (1990). Recall bias in epidemiologic studies. Journal of Clinical Epidemiology.](https://doi.org/10.1016/0895-4356(90)90060-3).
- Blinding: sound: Records abstracted by staff who did not know who was a case.

**Analysis.** *As submitted:* Conditional logistic regression, adjusted for other risk factors.

- Confounder adjustment (STROBE item 12a, 16a): sound: Adjusted for dementia, frailty, previous falls and other fall-risk drugs, chosen in advance.
  - **Flawed (Uncontrolled confounding, Major revisions):** Adjusted for age and sex only. Dementia and frailty, which lead to both pills and falls, are ignored.
  - *Why:* Frail people get more sleeping pills and fall more, so part of the 'drug effect' may be frailty. Fixable if the data hold these factors: adjust for them and show both estimates. See [Kyriacou & Lewis (2016). Confounding by indication in clinical research. JAMA.](https://doi.org/10.1001/jama.2016.16435).
- Sensitivity analysis (STROBE item 12e): sound: Results similar when restricted to new users and to fractures from simple falls.

## S4 · Burnout in the doctorate (Cross-sectional survey, STROBE)

> Almost half of PhD students are burnt out, and poor supervision causes it.

**Question.** *As submitted:* How common is burnout among PhD students, and what is it associated with?

- Prespecified aims (STROBE item 3): sound: Aims: estimate prevalence and describe associations. The conclusion stays descriptive.
  - **Flawed (Overclaiming, Minor revisions):** The aim is descriptive, yet the abstract concludes that poor supervision causes burnout.
  - *Why:* A one-off survey can't show which came first, burnout or poor supervision. Minor: rewrite the conclusion as an association. See [Boutron & Ravaud (2018). Misrepresentation and distortion of research in biomedical literature. PNAS.](https://doi.org/10.1073/pnas.1710755115).

**Method.** *As submitted:* Online survey of PhD students at four universities in spring 2025.

- Setting and dates (STROBE item 5): sound: Survey open for three weeks in March 2025, away from the main submission deadlines.

**Sample.** *As submitted:* 1,260 PhD students completed the survey.

- Recruitment (STROBE item 6a): sound: All 2,100 enrolled PhD students were invited by email, with two reminders.
  - **Flawed (Self-selected sample, Reject):** The link was shared on a PhD well-being forum and on social media; anyone could answer.
  - *Why:* Whether people answer depends on how much burnout matters to them, so the prevalence can't be generalised. A new, defined sample is needed. See [Hernán et al. (2004). A structural approach to selection bias. Epidemiology.](https://doi.org/10.1097/01.ede.0000135174.63482.43).
- Flow diagram (STROBE item 13a–c): sound: Numbers who opened, started and finished the survey are reported, with the drop-off at each step.

**Measurement.** *As submitted:* Burnout measured with a questionnaire scored against a cut-off.

- Measures (STROBE item 7–8): sound: A validated burnout inventory, scored with the manual's published cut-off.
  - **Flawed (Unvalidated measure, Major revisions):** Five items written by the authors; 'burnout' means scoring above the midpoint; no validation.
  - *Why:* A prevalence is only as good as the measure and its cut-off. Fixable only in part: give validity evidence, or report scores instead of a prevalence. See [Flake & Fried (2020). Measurement schmeasurement: questionable measurement practices and how to avoid them. Advances in Methods and Practices in Psychological Science.](https://doi.org/10.1177/2515245920952393).

**Analysis.** *As submitted:* Prevalence with 95% confidence intervals; regression for associations.

- Missing data (STROBE item 12c, 14b): sound: 3% of items missing, prorated as the scale's manual specifies.
  - **Flawed (Missing data ignored, Major revisions):** The 22% who skipped any item were dropped; skipping was commonest among those reporting long hours.
  - *Why:* If the students under most pressure skipped items, dropping them biases the prevalence. Fixable: multiple imputation, and compare completers with non-completers. See [Sterne et al. (2009). Multiple imputation for missing data in epidemiological and clinical research: potential and pitfalls. BMJ.](https://doi.org/10.1136/bmj.b2393).
- Sensitivity analysis (STROBE item 12e): sound: Estimates weighted by faculty and sex give the same prevalence within 2 points.

## S5 · Moral distress in intensive care (Interview study, COREQ)

> ICU nurses' moral distress centres on staffing, families and end-of-life decisions.

**Question.** *As submitted:* How do intensive-care nurses experience moral distress around end-of-life decisions?

- Prespecified aims: sound: An exploratory aim, stated up front, and no hypothesis, as suits an interview study.

**Method.** *As submitted:* Semi-structured interviews with ICU nurses at one university hospital.

- Reflexivity (COREQ item 1–8): sound: Interviews by a researcher from another hospital with no role over the nurses; her nursing background is described.
  - **Flawed (Interviewer with power, Reject):** Every interview was done by the unit's head nurse, who also writes the nurses' appraisals.
  - *Why:* Nurses are unlikely to speak freely to the person who appraises them, so the data themselves are compromised. New interviews are needed. See [Berger (2015). Now I see it, now I don't: researcher's position and reflexivity in qualitative research. Qualitative Research.](https://doi.org/10.1177/1468794112468475).

**Sample.** *As submitted:* Fourteen nurses, chosen for a range of experience and shift patterns.

- Recruitment (COREQ item 10–11): sound: Purposive sampling by years of experience and shift pattern; 3 of 17 nurses approached declined.
- Data saturation (COREQ item 22): sound: Interviews continued until three in a row added no new codes; the paper shows how this was judged.
  - **Flawed (Saturation not reached, Major revisions):** Data collection stopped at 14 because the project ended. Saturation is claimed but not shown.
  - *Why:* Saturation means new data stop adding insight, not that time ran out. Fixable: show how completeness was judged, or add interviews. See [Saunders et al. (2018). Saturation in qualitative research: exploring its conceptualization and operationalization. Quality & Quantity.](https://doi.org/10.1007/s11135-017-0574-8).

**Measurement.** *As submitted:* Interviews audio-recorded, transcribed in full and coded.

- Coding tree (COREQ item 24–25): sound: Two researchers coded independently and met to settle differences; the coding tree is in a supplement.
  - **Flawed (Single coder, no audit trail, Major revisions):** One researcher coded every transcript. There is no coding tree and no second reader.
  - *Why:* With one coder and no audit trail, readers can't judge how the codes came from the data. Fixable: a second coder, the coding tree and an audit trail. See [O'Connor & Joffe (2020). Intercoder reliability in qualitative research: debates and practical guidelines. International Journal of Qualitative Methods.](https://doi.org/10.1177/1609406919899220).
- Measures (COREQ item 17): sound: The interview guide was piloted with two nurses and is given in full.

**Analysis.** *As submitted:* Reflexive thematic analysis produced four themes.

- Theme derivation (COREQ item 26): sound: Themes were built from codes across interviews and checked against the full data set.
  - **Flawed (Themes = interview questions, Major revisions):** The four themes are the four headings of the interview guide, although the paper says they came from the data.
  - *Why:* Using the interview questions as themes summarises the guide, not the data; Braun & Clarke (2006) name it a pitfall. Fixable: redo the analysis. See [Braun & Clarke (2006). Using thematic analysis in psychology. Qualitative Research in Psychology.](https://doi.org/10.1191/1478088706qp063oa).

## S6 · A scan for appendicitis (Diagnostic accuracy study, STARD 2015)

> Bedside ultrasound by emergency doctors detects appendicitis in children with 97% sensitivity.

**Question.** *As submitted:* How accurate is bedside ultrasound by emergency doctors for appendicitis in children?

- Registration (STARD 2015 item 28–29): sound: Registered before recruitment, with the same target condition, population and cut-off as the paper.
  - **Flawed (Switched after registration, Major revisions):** Registered for patients of all ages. The paper reports children only and never mentions the adults.
  - *Why:* Leaving out a registered group can hide results that didn't suit. Fixable: report the whole registered population, or explain why not. See [Goldacre et al. (2019). COMPare: a prospective cohort study correcting and monitoring 58 misreported trials in real time. Trials.](https://doi.org/10.1186/s13063-019-3173-2).
- Prespecified aims (STARD 2015 item 4): sound: Prespecified target: a sensitivity of at least 90%.

**Method.** *As submitted:* Every child had a scan; the diagnosis was confirmed with a reference standard.

- Reference standard (STARD 2015 item 10a–11): sound: Histology if operated on; otherwise a phone follow-up at 14 days. The same rule for every child.
  - **Flawed (Partial verification, Major revisions):** Only children with a positive scan had surgery and histology. Negatives went home without follow-up.
  - *Why:* Missed cases among the negatives are never found, so sensitivity looks too high. Fixable only if follow-up can still be obtained for the negatives. See [Begg & Greenes (1983). Assessment of diagnostic tests when disease verification is subject to selection bias. Biometrics.](https://doi.org/10.2307/2530820).

**Sample.** *As submitted:* Children aged 4 to 16 with abdominal pain, at two emergency departments.

- Recruitment (STARD 2015 item 6–7, 9): sound: Consecutive children with suspected appendicitis, on every shift.
  - **Flawed (Spectrum bias, Reject):** Children with surgically confirmed appendicitis, compared with healthy children from a school check-up.
  - *Why:* Comparing clear cases with healthy children leaves out the hard, look-alike cases, so accuracy is inflated. A new, clinically realistic sample is needed. See [Lijmer et al. (1999). Empirical evidence of design-related bias in studies of diagnostic tests. JAMA.](https://doi.org/10.1001/jama.282.11.1061).
- Flow diagram (STARD 2015 item 19): sound: Flow diagram: 412 eligible, 398 scanned, 6 without a reference standard, each explained.

**Measurement.** *As submitted:* Each scan read as positive or negative for appendicitis.

- Blinding (STARD 2015 item 13a–b): sound: Readers knew only the child's age and symptoms, not the lab results or the final diagnosis.
  - **Flawed (Unblinded test reading, Major revisions):** Stored scans were read after surgery, by doctors who knew the histology result.
  - *Why:* Readers who know the answer read the scan in its light, which inflates accuracy. Fixable: re-read the stored scans blind. See [Whiting et al. (2004). Sources of variation and bias in studies of diagnostic accuracy: a systematic review. Annals of Internal Medicine.](https://doi.org/10.7326/0003-4819-140-3-200402030-00010).

**Analysis.** *As submitted:* Sensitivity and specificity with 95% confidence intervals.

- Test cut-offs (STARD 2015 item 12a–b): sound: Positive meant an appendix wider than 6 mm, a cut-off fixed in the protocol.
  - **Flawed (Data-driven cut-off, Major revisions):** The 6 mm cut-off was picked after the data, as the one giving the best accuracy.
  - *Why:* A cut-off tuned on the same data flatters accuracy. Fixable: use a prespecified cut-off, or validate this one in new data. See [Leeflang et al. (2008). Bias in sensitivity and specificity caused by data-driven selection of optimal cutoff values: mechanisms, magnitude, and solutions. Clinical Chemistry.](https://doi.org/10.1373/clinchem.2007.096032).
- Missing data (STARD 2015 item 15–16): sound: Inconclusive scans (9%) counted as negative, and as positive in a sensitivity analysis.

## S7 · Mindfulness apps for anxiety (Systematic review and meta-analysis, PRISMA 2020)

> Mindfulness apps reduce anxiety in adults, with a moderate pooled effect.

**Question.** *As submitted:* Do mindfulness apps reduce anxiety in adults, compared with control conditions?

- Registration (PRISMA 2020 item 24a–b): sound: Registered on PROSPERO before screening; outcomes and methods match the paper.
  - **Flawed (Switched after registration, Major revisions):** PROSPERO lists depression as the primary outcome. The review leads with anxiety and doesn't say why.
  - *Why:* Choosing the headline outcome after seeing the results lets the best-looking one win. Fixable: report the registered outcome first and explain the change. See [Goldacre et al. (2019). COMPare: a prospective cohort study correcting and monitoring 58 misreported trials in real time. Trials.](https://doi.org/10.1186/s13063-019-3173-2).
- Prespecified aims (PRISMA 2020 item 4): sound: Question in PICO form: adults, app-based mindfulness, any control, anxiety symptoms.

**Method.** *As submitted:* Systematic search for randomised trials, screened by two reviewers.

- Search strategy (PRISMA 2020 item 6–7): sound: Five databases and two trial registers, no language limits; full search strings in a supplement.
  - **Flawed (Narrow search, Major revisions):** PubMed only, English only, no trial registers; the search string isn't given.
  - *Why:* One database misses many trials, and the missed ones are not a random set. Fixable: redo the search across several sources. See [Bramer et al. (2017). Optimal database combinations for literature searches in systematic reviews: a prospective exploratory study. Systematic Reviews.](https://doi.org/10.1186/s13643-017-0644-y).

**Sample.** *As submitted:* 23 randomised trials with 4,380 adults were included.

- Recruitment (PRISMA 2020 item 5): sound: Any randomised trial was eligible, published or not, including register results and theses.
  - **Flawed (Unpublished studies left out, Major revisions):** Only trials published in journals were eligible; register results and theses were excluded.
  - *Why:* Unpublished trials more often find no effect, so leaving them out inflates the pooled effect. Fixable: widen eligibility and look for them. See [Hopewell et al. (2007). Grey literature in meta-analyses of randomized trials of health care interventions. Cochrane Database of Systematic Reviews.](https://doi.org/10.1002/14651858.MR000010.pub3).
- Flow diagram (PRISMA 2020 item 16a): sound: PRISMA flow diagram: 1,204 records, 61 full texts, 23 included; every exclusion has a reason.

**Measurement.** *As submitted:* Results and study quality extracted by two reviewers.

- Risk-of-bias assessment (PRISMA 2020 item 11, 18): sound: Two reviewers applied RoB 2 to each trial independently; judgements shown domain by domain.
  - **Flawed (No risk-of-bias assessment, Major revisions):** No risk-of-bias tool was used; trials were called 'high quality' because they were peer-reviewed.
  - *Why:* Without judging each trial's bias, nobody can tell whether the effect rests on weak trials. Fixable: assess with RoB 2 and run a sensitivity analysis by risk of bias. See [Sterne et al. (2019). RoB 2: a revised tool for assessing risk of bias in randomised trials. BMJ.](https://doi.org/10.1136/bmj.l4898).

**Analysis.** *As submitted:* Random-effects meta-analysis of standardised mean differences.

- Heterogeneity (PRISMA 2020 item 13d–e): sound: I² = 34%; a subgroup analysis by type of control was planned and reported.
  - **Flawed (Unexplored heterogeneity, Major revisions):** I² = 89%, yet one pooled effect is presented as the answer, and the differences are not explored.
  - *Why:* When trials disagree this much, one average may describe none of them. Fixable: explore the causes (subgroups, meta-regression) and temper the summary. See [Higgins & Thompson (2002). Quantifying heterogeneity in a meta-analysis. Statistics in Medicine.](https://doi.org/10.1002/sim.1186).
- Reporting bias (PRISMA 2020 item 14, 21): sound: Funnel plot and Egger's test across the 23 trials show no clear asymmetry.

## S8 · A drug for stroke mice (Animal experiment, ARRIVE 2.0)

> Compound NR-4, given after a stroke, cuts brain damage in mice by 40%.

**Question.** *As submitted:* Does compound NR-4, given after a stroke, reduce brain damage in mice?

- Registration (ARRIVE 2.0 item 19): sound: Protocol registered beforehand, with infarct volume at 72 hours as primary outcome, as reported.
  - **Flawed (Switched after registration, Major revisions):** Registered with a 24-hour behaviour score as primary. The paper reports infarct volume and omits the behaviour score.
  - *Why:* Dropping the registered outcome hides a result that may not have suited. Fixable: report the behaviour score and explain the switch. See [Goldacre et al. (2019). COMPare: a prospective cohort study correcting and monitoring 58 misreported trials in real time. Trials.](https://doi.org/10.1186/s13063-019-3173-2).
- Prespecified aims (ARRIVE 2.0 item 13): sound: Hypothesis stated: NR-4 reduces infarct volume at 72 hours compared with vehicle.

**Method.** *As submitted:* Mice with an induced stroke received NR-4 or vehicle one hour later.

- Randomisation (ARRIVE 2.0 item 4a): sound: Computer-made random list, held by a colleague who did no surgery.
  - **Flawed (Predictable allocation, Reject):** The first mice taken out of each cage got NR-4; the rest got vehicle.
  - *Why:* The mice caught first can differ (calmer, slower, smaller), so the groups may differ before treatment. The experiment has to be repeated with random allocation. See [Schulz et al. (1995). Empirical evidence of bias: dimensions of methodological quality associated with estimates of treatment effects in controlled trials. JAMA.](https://doi.org/10.1001/jama.1995.03520290060030).
- Intervention details (ARRIVE 2.0 item 9a–d): sound: Dose, route, timing, vehicle and anaesthesia described; the vehicle looked identical.

**Sample.** *As submitted:* Twelve mice per group, as planned.

- Sample size (ARRIVE 2.0 item 2b): sound: Power calculation from pilot data: 12 per group to detect a 30% reduction.
- Flow diagram (ARRIVE 2.0 item 3b–c): sound: All 24 mice analysed; no deaths and no exclusions.
  - **Flawed (Unreported exclusions, Major revisions):** Five NR-4 mice died or were excluded; they were replaced and are not mentioned.
  - *Why:* Replacing animals that died hides harm and can leave only the mice that responded. Fixable: report every animal and analyse with the losses included. See [Holman et al. (2016). Where have all the rodents gone? The effects of attrition in experimental research on cancer and stroke. PLOS Biology.](https://doi.org/10.1371/journal.pbio.1002331).

**Measurement.** *As submitted:* Infarct volume measured on stained brain slices at 72 hours.

- Blinding (ARRIVE 2.0 item 5): sound: Slices were coded; the person measuring them did not know the groups.
  - **Flawed (Unblinded assessors, Major revisions):** The researcher who dosed the mice also measured the slices, knowing each group.
  - *Why:* Tracing infarct edges takes judgement that expectations can sway. Fixable here, unlike in a live test: the stored slices can be re-measured blind. See [Hróbjartsson et al. (2013). Observer bias in randomized clinical trials with measurement scale outcomes: a systematic review of trials with both blinded and nonblinded assessors. CMAJ.](https://doi.org/10.1503/cmaj.120744).
- Measures (ARRIVE 2.0 item 6a): sound: Infarct volume defined in the methods and corrected for brain swelling.

**Analysis.** *As submitted:* Groups compared with a t-test; p < 0.001.

- Analysis set (ARRIVE 2.0 item 2a, 3c): sound: Each mouse counted once, with its slices averaged: 12 per group.
  - **Flawed (Pseudoreplication, Major revisions):** Each brain slice counted as a separate observation: 120 slices instead of 24 mice.
  - *Why:* Slices from one mouse are not independent, so the p-value is far too small. Fixable: reanalyse with the mouse as the unit. See [Lazic (2010). The problem of pseudoreplication in neuroscientific studies: is it affecting your analysis? BMC Neuroscience.](https://doi.org/10.1186/1471-2202-11-5).

## Coverage

| Request | Card | Answered in | Catches |
|---|---|---|---|
| Registration | Question | S1, S2, S6, S7, S8 | Switched after registration |
| Prespecified aims | Question | S1, S2, S3, S4, S5, S6, S7, S8 | HARKing, Overclaiming, p-hacking |
| Randomisation | Method | S1, S8 | Predictable allocation |
| Intervention details | Method | S1, S8 |  |
| Setting and dates | Method | S2, S3, S4 | Exposure after outcome |
| Search strategy | Method | S7 | Narrow search |
| Reflexivity | Method | S5 | Interviewer with power |
| Reference standard | Method | S6 | Partial verification |
| Recruitment | Sample | S1, S3, S4, S5, S6, S7 | Hand-picked participants, Self-selected sample, Spectrum bias, Unpublished studies left out, Unsuitable controls |
| Flow diagram | Sample | S1, S2, S3, S4, S6, S7, S8 | Selective loss to follow-up, Unreported exclusions |
| Sample size | Sample | S2, S8 |  |
| Data saturation | Sample | S5 | Saturation not reached |
| Blinding | Measurement | S1, S3, S6, S8 | Unblinded assessors, Unblinded test reading |
| Measures | Measurement | S1, S2, S3, S4, S5, S8 | Recall bias, Unvalidated measure |
| Coding tree | Measurement | S5 | Single coder, no audit trail |
| Risk-of-bias assessment | Measurement | S7 | No risk-of-bias assessment |
| Missing data | Analysis | S1, S4, S6 | Missing data ignored |
| Sensitivity analysis | Analysis | S2, S3, S4 | p-hacking |
| Confounder adjustment | Analysis | S2, S3 | Uncontrolled confounding |
| Analysis set | Analysis | S1, S8 | Per-protocol only, Pseudoreplication |
| Theme derivation | Analysis | S5 | Themes = interview questions |
| Test cut-offs | Analysis | S6 | Data-driven cut-off |
| Heterogeneity | Analysis | S7 | Unexplored heterogeneity |
| Reporting bias | Analysis | S7 |  |
