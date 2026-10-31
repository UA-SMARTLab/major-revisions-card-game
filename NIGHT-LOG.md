# Night log: 2026-10-31

Built overnight by Claude, on Abdulhamid's go-ahead, in parallel with Red Flag (a separate agent and folder).
Kept local: no GitHub repository, no push, nothing published.

## What was done

1. **Research.**
   - Checked every reporting-guideline item used on the cards against the checklists themselves: CONSORT 2025,
     STROBE, PRISMA 2020, COREQ, STARD 2015 and ARRIVE 2.0.
   - Checked all 30 flaw references and 6 guideline papers by DOI in Crossref, and in PubMed where Crossref lists
     only the first author.
   - Surveyed 14 existing games and tools about peer review and research methods. Details and links are in DESIGN.md
     §6–7.
2. **Data** (`data/`):
   - 8 fictional studies, one per common design, each written up as five slots with 1–2 answers per slot;
   - 38 flawed answers drawn from 30 documented flaw types;
   - 24 requests, each with its checklist items;
   - 4 verdicts.
3. **Build** (`tools/`):
   - Methodical's scaffold, adapted. The kit's card frame, fonts and fitting script are unchanged; this game adds its
     own card types (Study, Manuscript with a masked state, Request, Verdict), an orange accent, and a card back
     carrying the kit mark.
   - Outputs: print sheets (117 cards, 13 A4 pages), card backs, the Author's flaw key (HTML and ANSWER_KEY.md), and
     the app.
   - Validation includes: every flaw's catching request has an item in the study's guideline; each study has at least
     3 flawable slots.
4. **App** (`app/`): Home, Review and Browse the decks.
   - Home has a card fan, live counts with pop-ups and a "Sound or flawed?" quick question.
   - Review deals a manuscript from a seed. The same number gives the same manuscript, and `#m=1234` reopens it.
     There is an expert mode in which a manuscript may be sound.
   - Five requests come from a hand of the study's own requests plus two that don't apply.
   - Methodical's full-screen viewer and green confirm button are used to send a request and to give a verdict.
   - Your report marks the flawed card(s). The result screen shows every card's true face, the flaw, its verdict and
     why, the request and guideline item that would have caught it, and the key reference.
5. **Docs**: CLAUDE.md (game specifics, pointing to Methodical's kit conventions), README.md, RULES.md (table play for
   3–6 players with an Author, plus variants), DESIGN.md, LICENSE.md (adapted from Methodical's).

## What was checked, and how

- `python tools/build.py`: passes with no errors and no warnings.
- `python tools/check_cards.py`:
  - Renders all 117 printed cards at print size in headless Chrome, with the real fonts loaded (Bricolage
    Grotesque, Barlow Condensed, IBM Plex Sans Condensed).
  - Result: **no card overflows**, and none needed to shrink its text.
- `python tools/test_app.py`: **38 checks pass** in headless Chrome:
  - **Deals:** dealing is deterministic, and 1,200 deals are well formed.
  - **Verdicts and scoring:** the verdict rule and scoring are checked against hand-worked cases.
  - **Full review:** revealed answers match the dealt variant, masked cards show no flaw label, and the marks,
    verdict and result screen work.
  - **Viewer:** an instant press on the green button is ignored, the arrows move between cards, and Escape closes
    the viewer.
  - **Decks and page:** every deck renders, and the page throws no errors.
- **Screenshots** (`test_app.py --shots`), all looked at:
  - Desktop 1280 px and phone 390 px, in light and dark, covering Home, Review, the report, the result and the decks.
  - The phone widths were rendered in a 390 px iframe, because desktop Chrome won't open a narrower window.
  - No horizontal scroll at phone width.
  - Two layout fixes came out of this: a long study title now gets an ellipsis, and SVG gradient ids are made unique
    so a card shown twice keeps its picture.
- No server was started (all checks open the files directly), so none needed stopping.

## What is open

- **Not playtested with people.** Table balance (6 rounds, an 8-card request menu, scoring) is a first guess.
- **Only English.** The i18n structure is in place: `i18n/en/ui.json`, a generated `i18n/en/cards.json`, and
  picture labels. French, Dutch, German and Arabic, with glossaries and an independent review, come next.
- **Only 2 Minor flaws out of 38.** More would make the Minor verdict easier to learn.
- **Two checks rest on second-hand copies:**
  - The COREQ item numbers were checked against a journal-hosted copy of the checklist, because the original OUP
    article was blocked.
  - The Braun & Clarke (2006) "pitfall" wording was checked in a non-publisher copy of the paper.
- **Not tested on a real phone or with a screen reader.** Keyboard use was not checked beyond the viewer's keys.
- **The card pictures are first drafts:** simple diagrams in the kit style. Some could be more telling (the slot
  pictures repeat the same page motif).
- **Repository and hosting** are still to decide: a private repo under UA-SMARTLab, and a private playable copy like
  Methodical's.

## Commits

See `git log`. Each finished piece was committed locally.
