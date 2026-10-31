# Major Revisions: working notes for Claude

Major Revisions is the second game of the **SMART-Lab Science Game Kit**. The kit conventions (architecture, card
look, app behaviour, content rules, licence) are defined in Methodical's CLAUDE.md:
`C:\Users\A-Bag\Desktop\methodical-card-game\CLAUDE.md`. Follow them; this file adds only what is specific to this
game. My general rules are in `~/.claude/CLAUDE.md`.

## The game
- A deduction game about peer review. A fictional study is dealt as five face-down Manuscript cards (Question,
  Method, Sample, Measurement, Analysis); one or two carry a planted flaw. Reviewers spend Requests to reveal answers,
  then name the flawed card(s) and give a Verdict (Accept, Minor, Major, Reject). Rules: RULES.md. Design: DESIGN.md.
- Verdict rule: the worst planted flaw decides (reject > major > minor); no flaw, accept.

## Data (`data/`)
- `studies.json`: per study, per slot, the *As submitted* line and 1–2 facts `{request, sound, flaw?}`; at most one
  flawed fact per slot; at least 3 flawable slots per study. Flaw `{type, severity, text, why}`.
- `requests.json`: each request belongs to one slot; `items` maps guideline id → checklist item(s). Item numbers were
  verified against the checklists on 2026-10-31 (CONSORT 2025, not 2010). Never change one from memory.
- `flaws.json`: flaw types with a Crossref-checked `ref`. Which flaws a request "catches" is derived from the studies.
- `guidelines.json`: guideline name, checklist URL and key paper.

## Code
- `tools/build.py` validates and generates; `tools/cards.py` renders cards (kit frame and CSS copied from Methodical,
  then this game's types); `tools/art.py` holds the shared drawing primitives; `tools/art_mr.py` this game's pictures;
  `tools/i18n.py` the kit's i18n with this game's text fields.
- `tools/check_cards.py`: every printed card in headless Chrome/Edge, fails on overflow. `tools/test_app.py`: plays
  the app headless (dealing, verdict rule, scoring, viewer); `--shots DIR` saves desktop/phone, light/dark screenshots.
  Phone widths are shown in an iframe because desktop Chrome won't open a window narrower than about 500 px.
- The app deals deterministically: `deal(seed, expert)` with mulberry32; `#m=1234` (or `#m=1234x` for expert) in the
  URL reopens a manuscript.

## Look
- Accent: card #C2410C, UI #9A3412 (light) / #FDBA74 (dark). Manuscript cards share one neutral colour (#57534E) so
  colour never tells a flawed card from a sound one; Requests take their slot's colour; Studies #7C2D12; back
  #431407 with the kit mark "SMART-LAB SCIENCE GAME KIT".

## Repo
- Local only for now (no GitHub repo, nothing public). `.claude/launch.json` serves `app/` on 127.0.0.1:8793.
- Overnight work is logged in NIGHT-LOG.md.
