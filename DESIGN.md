# Major Revisions: design notes

## 1. Starting point

Methodical, the kit's first game, trains choosing a method. Major Revisions trains the other half of a researcher's
methods knowledge: **reading a study critically**, the way a peer reviewer does. The agreed concept: a manuscript
dealt face down as five cards, one or two of them flawed; Request cards that reveal answers, each tied to the
reporting-guideline item that asks for it; Verdict cards; and a win by naming the flawed card and the right verdict
before the requests run out.

## 2. What a player should learn

1. Where flaws hide in each kind of study: allocation in a trial, timing in a cohort, controls in a case-control
   study, the sample in a prevalence survey, the interviewer in a qualitative study, verification in a diagnostic
   study, the search in a review, exclusions and the unit of analysis in animal work.
2. Which question exposes each flaw, and which **reporting-guideline item** requires the authors to answer it. A
   reviewer who knows that CONSORT 2025 item 18 asks for allocation concealment knows where to look.
3. **How serious** a flaw is: whether reporting, reanalysis or only a new study can fix it. The same flaw can earn
   different verdicts (unblinded assessors: Reject for a live performance test that can't be repeated, Major
   revisions for stored brain slices that can be re-measured blind).
4. That a sound answer and a flawed one can sound alike. Both versions of a card share the *As submitted* line, so
   only asking reveals the difference.

## 3. Mechanics and why

- **Five fixed slots.** Question, Method, Sample, Measurement, Analysis give every study the same shape, so players
  learn a review routine rather than a study. Each slot has one or two answers (a card holds two at most).
- **One flaw per card, one or two flawed cards per manuscript.** One keeps the deduction clean; two adds the
  question "is there another?" and teaches that the worst flaw sets the verdict.
- **Requests are tied to a slot.** A request is answered by one card, so choosing a request means choosing where to
  look. Requests that don't apply to the study cost a round ("Not applicable"): knowing that a search strategy
  belongs to a review, not a trial, is part of the skill. The app deals the study's own requests plus two such decoys.
- **Limited rounds and a bonus for unused ones.** Five requests for about ten answers forces prioritising; the bonus
  rewards stopping once the case is made, as an efficient reviewer would.
- **Verdict rule.** The worst flaw decides: Reject > Major > Minor; no flaw, Accept. Severity is set per flawed answer
  in the data (not per flaw type), with a *why* that says whether and how it can be fixed. Accept is only right in
  the expert variant, where a manuscript may be sound; this keeps the Accept card meaningful.
- **Table play.** The Author plants flaws and answers truthfully, reading only the requested answer; Reviewers race to
  report the flawed card (more points the earlier) and the Author scores for flaws that survive. This gives the
  Author a real goal: choose flaws whose catching requests are unlikely to be asked.
- **Deterministic deals.** The app deals from a number with a seeded generator (mulberry32), so a manuscript can be
  shared (`#m=1234`) and replayed, and tests are repeatable.
- **Colour never gives the answer away.** Manuscript cards share one neutral colour; the planted flaw is visible only
  on the card's face, which only the Author sees at the table and which the app masks until the end.

## 4. The studies

Eight fictional studies, one per common design, each reported with its guideline. They are labelled "Fictional
study" on the card and in the footer; none is presented as real. Their flaws are real, documented flaw types.

| Study | Design | Guideline | Flawable slots |
|---|---|---|---|
| Back on track | Randomised trial | CONSORT 2025 | 5 |
| Late-night scrolling | Cohort study | STROBE | 5 |
| Sleeping pills and hip fracture | Case-control study | STROBE | 5 |
| Burnout in the doctorate | Cross-sectional survey | STROBE | 4 |
| Moral distress in intensive care | Interview study | COREQ | 4 |
| A scan for appendicitis | Diagnostic accuracy study | STARD 2015 | 5 |
| Mindfulness apps for anxiety | Systematic review and meta-analysis | PRISMA 2020 | 5 |
| A drug for stroke mice | Animal experiment | ARRIVE 2.0 | 5 |

That gives 110 flawed manuscripts (each study with one or two flawed cards), plus sound ones in expert mode.
Severity spread over the 38 flawed answers: 8 Reject, 28 Major, 2 Minor. Minor flaws are rare on purpose (a planted flaw should
matter), but more would make the Minor card easier to learn; see §7.

## 5. Card data and tooling

As in Methodical: card text only in `data/*.json`; `tools/build.py` validates and generates the print sheets, the
flaw key, `ANSWER_KEY.md`, the app and `i18n/en/cards.json`. Checks specific to this game: a flawed answer's request
must have a checklist item in that study's guideline (so the end screen can always name it); each study needs at
least three flawable slots; each slot one or two answers. `tools/check_cards.py` renders every printed card at print
size in headless Chrome and fails if a text box or name bar overflows (all 117 cards fit at full size, none needed
shrinking). `tools/test_app.py` plays the app headless (38 checks).

The card frame, fonts, fitting script, viewer and green confirm button are the kit's, copied from Methodical. This
game adds: Study, Manuscript (with a masked state for the app), Request and Verdict card types; an orange accent
(#C2410C); a back in burnt orange with an "MR" stamp and the kit mark.

## 6. Sources and how they were checked

**Reporting guidelines.** Every checklist item number on the Request cards was checked on 2026-10-31 against the
checklist itself (not from memory), and each guideline's DOI against Crossref:

| Guideline | Key paper | Checklist checked |
|---|---|---|
| CONSORT 2025 | Hopewell et al. (2025), [doi:10.1136/bmj-2024-081123](https://doi.org/10.1136/bmj-2024-081123) | [expanded checklist PDF](https://www.consort-spirit.org/_files/ugd/b5740e_a6856e5e2cf94a1db5a8005853404160.pdf) |
| STROBE | von Elm et al. (2007), [doi:10.1016/S0140-6736(07)61602-X](https://doi.org/10.1016/S0140-6736(07)61602-X) | [combined checklist](https://www.strobe-statement.org/download/strobe-checklist-cohort-case-control-and-cross-sectional-studies-combined) |
| PRISMA 2020 | Page et al. (2021), [doi:10.1136/bmj.n71](https://doi.org/10.1136/bmj.n71) | [checklist PDF](https://www.prisma-statement.org/s/PRISMA_2020_checklist.pdf) |
| COREQ | Tong et al. (2007), [doi:10.1093/intqhc/mzm042](https://doi.org/10.1093/intqhc/mzm042) | [a journal-hosted copy of the checklist](https://www.dovepress.com/article/supplementary_file/531582/531582-additional-file-1-COREQ-checklist_1.pdf) (the original article was not reachable) |
| STARD 2015 | Bossuyt et al. (2015), [doi:10.1136/bmj.h5527](https://doi.org/10.1136/bmj.h5527) | [Table 1, PMC4623764](https://pmc.ncbi.nlm.nih.gov/articles/PMC4623764/) |
| ARRIVE 2.0 | Percie du Sert et al. (2020), [doi:10.1371/journal.pbio.3000410](https://doi.org/10.1371/journal.pbio.3000410) | [full author checklist PDF](https://arriveguidelines.org/sites/arrive/files/documents/Author%20Checklist%20-%20Full.pdf) |

Notes from that check: CONSORT 2025 has replaced CONSORT 2010 and renumbered the items (allocation 8a–10 → 17a–19,
blinding 11a–b → 20a–b, flow 13a–b → 22a–b); it adds an explicit missing-data item (21c). Its objectives item (7) no
longer mentions hypotheses. STROBE has no registration or blinding item, so those requests cite no STROBE item.
ARRIVE has no flow diagram; exclusions are items 3b–c, sample size 2b, randomisation 4a. PRISMA has no single
missing-data item (10b, 13b and 14 cover it).

**Flaw references.** All 30 flaw references were looked up by DOI in Crossref (and PubMed where Crossref lists only
the first author) on 2026-10-31; years are the journal issue year. Two papers appeared online a year before their
issue: Berger (2015, online 2013) and Saunders et al. (2018, online 2017). The claim that Braun & Clarke (2006) name
"using the interview questions as themes" as a pitfall was checked in a copy of the paper's text, not the publisher's
page; check the page number before quoting it in print.

## 7. Prior art: games about peer review and research methods

Surveyed on 2026-10-31 so that Major Revisions adds something new; no content was taken from any of them.

| Game or tool | What players do | How Major Revisions differs |
|---|---|---|
| [Dilemma Game](https://www.eur.nl/en/about-eur/strategy-and-policy/integrity/research-integrity/dilemma-game) (Erasmus University Rotterdam; cards, app since 2020) | Discuss research-integrity dilemmas and pick an action | Ethics discussion with no hidden answer to deduce |
| [p-hacker](https://shiny.psy.lmu.de/felix/p-hacker) (Schönbrodt, 2016, web) | Use analytic flexibility to push p below .05 | You commit the flaw; nobody has to detect it |
| [Guess the Correlation](https://www.guessthecorrelation.com/) (Wagih, 2016, web) | Estimate r from scatter plots | One statistical intuition, not appraisal of a study |
| [Dear Reviewer 2](https://news.mcmaster.ca/dear-reviewer-2-card-game-prepares-budding-researchers-for-peer-review/) (Chan & Preyra, McMaster, 2024, cards) | Write responses to reviewer critiques; vote on the best | You play the author answering reviews, not a reviewer hunting a flaw |
| [Peer Review Card Exchange Game](https://ease.org.uk/2018/10/a-peer-review-card-exchange-game/) (Tokalić & Marušić, EASE, 2018) | Trade and debate statements about peer review | Opinions, no manuscript, no verdict |
| [Publish or Perish card game](https://pmc.ncbi.nlm.nih.gov/articles/PMC11399718/) (Bai, 2024) | Satire: publish papers, p-hack and sabotage rivals | Satire of incentives; flaws are a tactic, not a puzzle |
| [Publish or Perish board game](https://www.thegamecrafter.com/games/publish-or-perish1) (2014) | Push manuscripts through journals; others vote on acceptance | Acceptance is a vote, not an evidence-based verdict |
| [Vote cards for RoB 2](https://abstracts.cochrane.org/2023-london/use-simulation-scenarios-and-vote-cards-teaching-critical-appraisal-randomized) (Cochrane Taiwan, 2023, classroom) | Hold up red/yellow/green cards for risk-of-bias scenarios | Closest to verdict cards, but the flaw is shown openly |
| [Serious game for critical appraisal](https://latunisiemedicale.org/index.php/tunismed/article/view/4165) (Mlika et al., 2022) | Appraise one article through a game | Mechanics unpublished; one real article |
| [Intentionally flawed manuscripts](https://doi.org/10.1002/bmb.21084) (Ferenc et al., 2018, classroom) | Teams plant errors in a manuscript; a rival team finds them | Same planted-flaw idea, as free-form prose without rules, limited requests, guideline mapping or verdicts |
| [COBPeer](https://doi.org/10.1186/s12916-019-1436-0) (Chauvin et al., 2019, online tool) | Early-career reviewers check a trial against CONSORT domains | Same guideline-to-review mapping, as a checklist tool, not a game |
| [The Lab](https://ori.hhs.gov/thelab) (US Office of Research Integrity) | Branching video about misconduct | Role-play narrative, not study design |
| [Solve the Outbreak](https://www.cdc.gov/digital-social-media-tools/mobile/applications/sto/sto-web.html) (CDC, 2013) | Spend actions to gather clues, then name the outbreak's cause | Closest mechanic (spend actions, then decide), about epidemiology, not manuscripts |
| [Catalogue of Bias](https://catalogofbias.org/about/) (Oxford CEBM; a resource, not a game) | Entries define biases with examples | A reference, not a game |

**Judgement.** No game found combines a hidden planted flaw across a structured manuscript, a limited budget of
requests tied to reporting-guideline items, and a scored editorial verdict. Ferenc et al. (planted flaws) and COBPeer
(guideline items as the unit of review) are the closest in purpose and support the educational idea.

## 8. Open questions and next steps

1. **Playtest at the table**: is 6 rounds and an 8-card request menu right for 3–6 players? Does the Author have
   enough say (choice of flaws) to be fun?
2. **More Minor flaws** (only 2 of 38) and a few more sound-only answers per study, so that asking is never certain.
3. **More studies**: a cluster or stepped-wedge trial, a prediction model (TRIPOD+AI), an economic evaluation
   (CHEERS 2022), a quality-improvement study (SQUIRE 2.0). Item numbers must be checked against each checklist.
4. **Translations** (fr, nl, de, ar) through the kit's i18n, with a GLOSSARY.md per language and an independent
   review, as in Methodical.
5. A shared online version (as Methodical's private playable copy) once the IP question allows it.
