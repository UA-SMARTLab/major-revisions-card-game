#!/usr/bin/env python3
"""Test the built app (app/index.html) in headless Chrome or Edge: dealing is deterministic and well-formed,
the verdict rule and scoring give the right results, a full review can be played through, and the page throws no
errors. Optionally saves screenshots (desktop and phone width, light and dark) for a visual check.

Usage:  python3 tools/test_app.py [--shots DIR]      (run python3 tools/build.py first)
Expected results come from the rules in RULES.md (by definition) and from hand-checked cases in data/studies.json.
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_cards import chrome  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# Runs inside the app page after it has started. Each check pushes [name, passed, detail].
TESTS = r"""
(async () => {
const out = [], ok = (name, pass, detail = "") => out.push([name, !!pass, String(detail)]);
try {
  // 1. Determinism: the same number deals the same manuscript.
  const a = deal(42, false), b = deal(42, false);
  ok("same seed, same deal", a.st.id === b.st.id && a.flawed.join() === b.flawed.join() && a.hand.join() === b.hand.join() && JSON.stringify(a.planted) === JSON.stringify(b.planted), a.st.id + " " + a.flawed);
  const key = d => JSON.stringify([d.st.id, d.flawed, d.planted, d.hand]);
  let drift = [];
  for (let s = 1; s <= 600; s++) for (const ex of [false, true]) if (key(deal(s, ex)) !== key(deal(s, ex))) drift.push(s + (ex ? "x" : ""));
  ok("600 seeds each deal the same manuscript twice, flawed card variants included", !drift.length, drift.slice(0, 5).join());
  ok("seed and expert flag both matter", JSON.stringify(deal(42, true).hand) !== JSON.stringify(a.hand) || deal(42, true).st.id !== a.st.id || deal(43, false).hand.join() !== a.hand.join());
  // 2. Every deal is well formed.
  let bad = [], sound = 0, studiesSeen = new Set();
  for (let s = 1; s <= 600; s++) for (const ex of [false, true]) {
    const d = deal(s, ex), own = SLOTS.flatMap(sid => d.st.slots[sid].facts.map(f => f.request));
    studiesSeen.add(d.st.id);
    if (!ex && (d.flawed.length < 1 || d.flawed.length > 2)) bad.push(`#${s}: ${d.flawed.length} flaws`);
    if (ex && d.flawed.length > 2) bad.push(`#${s}x: ${d.flawed.length} flaws`);
    if (ex && !d.flawed.length) sound++;
    if (d.flawed.some(sid => !d.st.slots[sid].facts.some(f => f.flaw))) bad.push(`#${s}: flaw on a card without a flawed variant`);
    if (Object.keys(d.planted).sort().join() !== d.flawed.slice().sort().join()) bad.push(`#${s}: planted variants don't match the flawed cards`);
    if (d.flawed.some(sid => !(d.planted[sid] >= 0 && d.planted[sid] < variantsOf(d.st, sid).length))) bad.push(`#${s}: variant out of range`);
    if (new Set(d.hand).size !== d.hand.length) bad.push(`#${s}: duplicate request in hand`);
    if (!own.every(r => d.hand.includes(r))) bad.push(`#${s}: hand misses one of the study's requests`);
    if (d.hand.length !== own.length + meta.app.hand_decoys) bad.push(`#${s}: hand has ${d.hand.length} cards`);
  }
  ok("600 deals well formed (normal and expert)", !bad.length, bad.slice(0, 5).join("; "));
  ok("every study gets dealt", studiesSeen.size === studies.length, studiesSeen.size);
  ok("expert mode sometimes deals a sound manuscript (about 1 in 5)", sound > 60 && sound < 180, sound + " of 600");
  // 3. Verdict rule (by definition: the worst planted flaw; none planted, accept). Hand-checked against data/studies.json S1.
  const s1 = ST.S1, v = flawed => rightVerdict({ st: s1, flawed });
  ok("verdict: S1 method (predictable allocation) is reject", v(["method"]) === "reject", v(["method"]));
  ok("verdict: S1 question (switched registration) is major", v(["question"]) === "major", v(["question"]));
  ok("verdict: S1 sample (hand-picked) is minor", v(["sample"]) === "minor", v(["sample"]));
  ok("verdict: minor + major gives major", v(["sample", "question"]) === "major", v(["sample", "question"]));
  ok("verdict: nothing planted gives accept", v([]) === "accept", v([]));
  // Slots with two flawed cards: the dealt variant sets the verdict. Hand-checked against data/studies.json S1:
  // method F is predictable allocation (reject), method F2 an undescribed intervention (minor); sample F is
  // hand-picked participants (minor), sample F2 an unreported flow (minor).
  const vp = (flawed, planted) => rightVerdict({ st: s1, flawed, planted });
  ok("verdict: S1 method F (predictable allocation) is reject", vp(["method"], { method: 0 }) === "reject", vp(["method"], { method: 0 }));
  ok("verdict: S1 method F2 (intervention not described) is minor", vp(["method"], { method: 1 }) === "minor", vp(["method"], { method: 1 }));
  ok("verdict: only minor flaws planted (S1 method F2 + sample F2) gives minor revisions", vp(["method", "sample"], { method: 1, sample: 1 }) === "minor", vp(["method", "sample"], { method: 1, sample: 1 }));
  ok("verdict: S1 method F2 + question (major) gives major", vp(["method", "question"], { method: 1, question: 0 }) === "major");
  // Every flawed card of every two-flaw slot gets dealt.
  const seen = new Set(), want = new Set();
  for (const st of studies) for (const sid of SLOTS) variantsOf(st, sid).forEach((f, k) => want.add(`${st.id}/${sid}/${k}`));
  let minorDeals = 0;
  for (let s = 1; s <= 4000; s++) { const d = deal(s, false); for (const sid of d.flawed) seen.add(`${d.st.id}/${sid}/${d.planted[sid]}`); minorDeals += rightVerdict(d) === "minor"; }
  const unseen = [...want].filter(x => !seen.has(x));
  ok("4000 deals reach every flawed card, F2 included", !unseen.length && [...seen].some(x => x.endsWith("/1")), unseen.join());
  // Expected share by definition: enumerate the dealing rule (study uniform; 1 or 2 flawed slots, each half the time;
  // slots uniform; flawed card uniform per slot) and add up the deals whose worst flaw is minor. 15.4% with today's data.
  let exact = 0;
  for (const st of studies) {
    const vs = flawable(st).map(sid => variantsOf(st, sid).map(f => f.flaw.severity));
    const allMinor = v => v.filter(s => s === "minor").length / v.length;
    const pairs = vs.flatMap((a, i) => vs.slice(i + 1).map(b => [a, b]));
    exact += (0.5 * vs.reduce((n, v) => n + allMinor(v), 0) / vs.length + 0.5 * pairs.reduce((n, [a, b]) => n + allMinor(a) * allMinor(b), 0) / pairs.length) / studies.length;
  }
  ok("minor revisions is right as often as the dealing rule predicts (within 2 points)", Math.abs(minorDeals / 4000 - exact) < 0.02 && exact > 0.12, `${minorDeals} of 4000 dealt; expected ${(100 * exact).toFixed(1)}%`);
  // 4. Scoring (by definition, meta.scoring): +3 per flaw found, -1 per sound card marked, +2 right verdict,
  //    +1 per unused request only when the report is fully right.
  const sc = (flawed, marks, verdict, left) => scoreOf({ st: s1, flawed, marks: new Set(marks), verdict, left });
  ok("score: perfect with 4 unused requests = 3 + 2 + 4", sc(["method"], ["method"], "reject", 4).total === 9, sc(["method"], ["method"], "reject", 4).total);
  ok("score: flaw found, wrong verdict = 3, no bonus", sc(["method"], ["method"], "major", 4).total === 3, sc(["method"], ["method"], "major", 4).total);
  ok("score: false alarm costs 1 and cancels the bonus", sc(["method"], ["method", "sample"], "reject", 2).total === 4, sc(["method"], ["method", "sample"], "reject", 2).total);
  ok("score: missed flaw, right verdict = 2", sc(["method"], [], "reject", 0).total === 2, sc(["method"], [], "reject", 0).total);
  // 5. A full review through the interface functions.
  show("play"); newGame(7, false);
  const g = game, first = g.hand.slice(0, 5);
  first.forEach(ask);
  const answered = first.filter(r => factOf(g.st, r)).length;
  ok("five requests spend all rounds", g.left === 0 && g.asked.length === 5, g.left);
  ok("each answered request opens its answer on the right card", document.querySelectorAll("#ms .ans.open").length === answered, document.querySelectorAll("#ms .ans.open").length + " of " + answered);
  ok("revealed text matches the dealt variant", first.filter(r => factOf(g.st, r)).every(r => { const h = factOf(g.st, r); return document.querySelector(`#ms .slot[data-slot="${h.sid}"] .ans[data-req="${r}"] .ans-t`).textContent === answerText(g, h.sid, h.f); }));
  ok("masked cards show no flaw label", !document.querySelector("#ms .bad-tag, #ms .ok-tag, #ms .ans.bad"));
  ok("the log has one entry per request", g.log.filter(l => l.head).length === 5, g.log.length);
  ok("report button is offered once requests run out", !!document.querySelector("#b-report.primary"));
  startReport();
  g.flawed.forEach(sid => document.querySelector(`#ms .cardbtn[data-slot="${sid}"]`).click());
  ok("marking toggles cards", [...g.marks].sort().join() === g.flawed.slice().sort().join(), [...g.marks].join());
  ok("four verdict cards offered", document.querySelectorAll("#verdicts .cardbtn").length === 4);
  finish(rightVerdict(g));
  ok("perfect report scores flaws + verdict", g.score.perfect && g.score.total === g.flawed.length * 3 + 2, JSON.stringify(g.score));
  ok("result shows full cards with badges", document.querySelectorAll("#ms .badge").length === 5 && document.querySelectorAll("#ms .tcg-m .ok-tag, #ms .tcg-m .bad-tag").length === 5);
  ok("result names the guideline item that catches each flaw", document.querySelectorAll("#desk .flawbox").length === g.flawed.length && /item/.test(document.querySelector("#desk .flawbox .meta").textContent));
  // An F2 card: the result shows the dealt flawed card and explains its own flaw, not the slot's first one.
  let f2 = 1; while (!Object.values(deal(f2, false).planted).includes(1)) f2++;
  newGame(f2, false);
  const sid2 = game.flawed.find(sid => game.planted[sid] === 1), fact2 = variantsOf(game.st, sid2)[1];
  game.hand.filter(r => r === fact2.request).forEach(ask);
  ok("F2: asking its request reveals the second flawed answer", game.log.some(l => l.text === esc(fact2.flaw.text)), `#${f2} ${sid2}`);
  startReport(); game.flawed.forEach(sid => game.marks.add(sid)); finish(rightVerdict(game));
  const shown = document.querySelector(`#ms .slot[data-slot="${sid2}"] .tcg`);
  ok("F2: the result shows card F2 with its flawed answer", /-F2$/.test(shown.querySelector(".ft span").textContent) && shown.querySelector(".ans.bad .ans-t").textContent === fact2.flaw.text, shown.querySelector(".ft span").textContent);
  const box = [...document.querySelectorAll("#desk .flawbox")].find(b => b.querySelector("h4").textContent.startsWith(SLOT[sid2].name));
  ok("F2: the result explains the F2 flaw, its verdict and request", box && box.textContent.includes(fact2.flaw.why) && box.textContent.includes(F[fact2.flaw.type].name) && box.textContent.includes(R[fact2.request].name), `#${f2} ${sid2}`);
  // A flaw with its own source (the diagnostic study's flow flaw cites STARD's explanation paper, not the RCT paper
  // its type cites): the result links that source.
  const ownRef = d => d.flawed.find(sid => plantedFact(d, sid).flaw.ref);
  let rs = 1; while (!ownRef(deal(rs, false))) rs++;
  newGame(rs, false); startReport(); game.flawed.forEach(sid => game.marks.add(sid)); finish(rightVerdict(game));
  const rsid = ownRef(game), rfl = plantedFact(game, rsid).flaw;
  const rbox = [...document.querySelectorAll("#desk .flawbox")].find(b => b.querySelector("h4").textContent.startsWith(SLOT[rsid].name));
  ok("a flaw's own source replaces its type's in the result", rbox && [...rbox.querySelectorAll("a")].some(a => a.href === rfl.ref.url) && ![...rbox.querySelectorAll("a")].some(a => a.href === F[rfl.type].ref.url), `#${rs} ${rsid}`);
  // A manuscript whose planted flaws are all minor: Minor revisions is the right verdict, and giving it scores.
  let mn = 1; while (rightVerdict(deal(mn, false)) !== "minor") mn++;
  newGame(mn, false); startReport(); game.flawed.forEach(sid => game.marks.add(sid)); finish("minor");
  ok("all-minor manuscript: Minor revisions is right and scores", game.flawed.every(sid => plantedFact(game, sid).flaw.severity === "minor") && game.score.verdictOk && game.score.perfect, `#${mn}`);
  // A decoy request is answered "not applicable" and still costs a round.
  newGame(7, false);
  const decoy = game.hand.find(r => !factOf(game.st, r));
  ask(decoy);
  ok("decoy request: not applicable, round spent", game.left === 4 && game.log[0].na, decoy);
  // The interface path: tapping a request opens the viewer; only the green button sends it, and not in the first moment.
  newGame(8, false);
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  document.querySelector("#hand .cardbtn").click();
  ok("tapping a request opens the full-screen viewer", !!document.querySelector(".viewer.choosing .v-pick"));
  document.querySelector(".v-pick").click();
  ok("an instant press on the green button is ignored", game.asked.length === 0);
  await sleep(400);
  document.querySelector(".viewer.choosing .v-nav[data-step='1']").click();
  await sleep(400);
  document.querySelector(".v-pick").click();
  await sleep(300);
  ok("the green button sends the request shown", game.asked.length === 1 && game.asked[0] === game.hand[1], game.asked.join());
  ok("the viewer closes after sending", !document.querySelector(".viewer:not(.out)"));
  document.querySelector("#b-report").click();
  document.querySelector("#verdicts .cardbtn").click();
  await sleep(400);
  ok("verdict viewer offers 'Give this verdict'", /verdict/i.test(document.querySelector(".v-pick").textContent));
  dispatchEvent(new KeyboardEvent("keydown", { key: "Escape" }));
  await sleep(300);
  ok("Escape closes the viewer without a verdict", !document.querySelector(".viewer:not(.out)") && game.phase === "report");
  // 6. Browse: every deck renders its cards.
  show("decks");
  for (const k of ["studies", "requests", "verdicts", "manuscripts"]) { deck = k; renderDecks(); ok(`decks: ${k} render`, document.querySelectorAll("#cards .tcg").length === DECK_ITEMS[k].length, document.querySelectorAll("#cards .tcg").length); }
  show("home");
  ok("home: quick question and fan render", document.querySelectorAll("#quick .tcg").length === 1 && document.querySelectorAll("#hero-fan .tcg").length === 5);
} catch (err) { ok("no exception", false, err.stack); }
ok("no page errors", !window.__errors.length, window.__errors.join(" | "));
const pre = document.createElement("pre"); pre.id = "probe"; pre.textContent = JSON.stringify(out); document.body.appendChild(pre);
})();
"""

ERRORS = "<script>window.__errors = []; addEventListener('error', e => window.__errors.push(e.message));</script>"

# The result of the first manuscript that plants an F2 card and whose right verdict is Minor revisions, answered right.
MINOR_F2 = ('show("play"); let s = 1; for (;; s++) { const d = deal(s, false); if (Object.values(d.planted).includes(1) && rightVerdict(d) === "minor") break; }'
            ' newGame(s, false); game.hand.slice(0, 5).forEach(ask); startReport(); game.flawed.forEach(x => game.marks.add(x)); finish("minor"); scrollTo(0, 0)')

# Screenshot set-ups: (name, width, height, theme, script run after the app starts)
SHOTS = [
    ("home", 1280, 1500, "light", 'show("home")'),
    ("play", 1280, 1700, "light", 'show("play"); newGame(7, false); game.hand.slice(0, 3).forEach(ask); scrollTo(0, 0)'),
    ("play-dark", 1280, 1700, "dark", 'show("play"); newGame(7, false); game.hand.slice(0, 3).forEach(ask); scrollTo(0, 0)'),
    ("report", 1280, 1900, "light", 'show("play"); newGame(7, false); game.hand.slice(0, 2).forEach(ask); startReport(); game.marks.add("method"); renderManuscript(); renderLower(); scrollTo(0, 0)'),
    ("result", 1280, 1900, "light", 'show("play"); newGame(7, false); game.hand.slice(0, 5).forEach(ask); startReport(); game.marks.add(game.flawed[0]); finish("major"); scrollTo(0, 0)'),
    ("result-dark", 1280, 1900, "dark", 'show("play"); newGame(7, false); game.hand.slice(0, 5).forEach(ask); startReport(); game.marks.add(game.flawed[0]); finish("major"); scrollTo(0, 0)'),
    ("phone-play", 390, 2600, "light", 'show("play"); newGame(7, false); game.hand.slice(0, 2).forEach(ask); scrollTo(0, 0)'),
    ("phone-play-dark", 390, 2600, "dark", 'show("play"); newGame(7, false); game.hand.slice(0, 2).forEach(ask); scrollTo(0, 0)'),
    ("phone-home", 390, 2200, "light", 'show("home")'),
    ("phone-result-dark", 390, 2600, "dark", 'show("play"); newGame(7, false); game.hand.slice(0, 5).forEach(ask); startReport(); game.marks.add(game.flawed[0]); finish("reject"); scrollTo(0, 0)'),
    ("minor-f2", 1280, 1900, "light", MINOR_F2),
    ("minor-f2-dark", 1280, 1900, "dark", MINOR_F2),
    ("phone-minor-f2", 390, 2600, "light", MINOR_F2),
    ("phone-minor-f2-dark", 390, 2600, "dark", MINOR_F2),
    ("decks", 1280, 1400, "light", 'show("decks"); deck = "requests"; renderDecks()'),
    ("phone-decks-dark", 390, 1600, "dark", 'show("decks"); deck = "manuscripts"; renderDecks()'),
]


def run(exe, html, args, phone=None):
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "index.html"
        page.write_text(html, encoding="utf-8")
        if phone:
            # Desktop Chrome won't make its window narrower than about 500 px, so a phone is an iframe of that width.
            w, h = phone
            page = Path(tmp) / "phone.html"
            page.write_text(f'<!doctype html><body style="margin:0;background:#888"><iframe src="index.html" style="width:{w}px;height:{h}px;border:0;display:block"></iframe></body>', encoding="utf-8")
        base = [exe, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=12000", f"--user-data-dir={Path(tmp) / 'p'}"]
        return subprocess.run(base + args + [page.as_uri()], capture_output=True, text=True, encoding="utf-8", timeout=180).stdout


def inject(src, script, theme="light"):
    pre = ERRORS + (f'<script>document.documentElement.dataset.theme = "{theme}";</script>')
    src = src.replace("<body>", "<body>" + pre, 1)
    return src.replace("</body></html>", f"<script>{script}</script></body></html>")


if __name__ == "__main__":
    exe = chrome()
    app = ROOT / "app" / "index.html"
    if not app.exists():
        sys.exit("No app/index.html yet: run python3 tools/build.py first.")
    src = app.read_text(encoding="utf-8")
    dom = run(exe, inject(src, TESTS), ["--dump-dom"])
    m = re.search(r'<pre id="probe">(.*?)</pre>', dom, re.S)
    if not m:
        sys.exit("The tests did not report back (did the page load?)")
    results = json.loads(m.group(1).replace("&quot;", '"').replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">"))
    failed = 0
    for name, passed, detail in results:
        failed += not passed
        print(("ok    " if passed else "FAIL  ") + name + ("" if passed or not detail else f"  ({detail})"))
    if "--shots" in sys.argv:
        out = Path(sys.argv[sys.argv.index("--shots") + 1])
        out.mkdir(parents=True, exist_ok=True)
        for name, w, h, theme, script in SHOTS:
            phone = (w, h) if w < 500 else None
            run(exe, inject(src, script, theme), [f"--window-size={max(w, 500)},{h}", f"--screenshot={out / (name + '.png')}"], phone)
        print(f"screenshots in {out}")
    if failed:
        sys.exit(f"{failed} test(s) failed")
    print(f"ok: {len(results)} tests passed")
