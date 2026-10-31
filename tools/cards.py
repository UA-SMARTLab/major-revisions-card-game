"""Trading-card renderer for Major Revisions.

Each card is plain HTML + inline SVG art. Every size is a multiple of the CSS variable --u, which is 1mm in
print (cards are 63 x 88 u, standard poker size) and can be set to any pixel size on screen. The card frame, fonts
and fitting script are the SMART-Lab Science Game Kit's, shared with Methodical; only the colours, the card types
and the back are this game's own.
"""
import html

import art
from art_mr import REQUEST_ART, REQUEST_ICON, SLOT_ART, SLOT_ICONS, STUDY_ART, STUDY_ICON, VERDICT_ART, VERDICT_ICON
from i18n import Strings

e = html.escape

# Card labels by key, set by the build for each language (see tools/i18n.py and i18n/<code>/ui.json).
S = Strings({})


def L(key, **kw):
    return e(S(key, **kw))


# Manuscript cards share one neutral colour, so a card's colour never tells whether it is flawed.
MANUSCRIPT_COLOR = "#57534E"
STUDY_COLOR = "#7C2D12"
REFERENCE_COLOR = "#334155"
BACK_COLOR = "#431407"
ACCENT = "#C2410C"

FONTS_URL = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800"
             "&family=Barlow+Condensed:wght@600;700&family=IBM+Plex+Sans+Condensed:ital,wght@0,400;0,600;1,400&display=swap")

# Translations can run longer than English. After cards are on the page, shrink a card's main text a little at a time
# until its text box fits (down to 70%). Used by the print sheets and the app (which also runs it on new cards).
FIT_JS = """
function fitCards(root) {
  (root || document).querySelectorAll(".tcg .tb").forEach(tb => {
    let k = 1;
    tb.style.removeProperty("--fit");
    while (tb.scrollHeight > tb.clientHeight + 1 && k > 0.72) { k -= 0.04; tb.style.setProperty("--fit", k.toFixed(2)); }
  });
}
if (document.readyState === "loading") addEventListener("DOMContentLoaded", () => fitCards()); else fitCards();
if (document.fonts) document.fonts.ready.then(() => fitCards());
"""

CARD_CSS = """
.tcg { --u: var(--card-u, 1mm); --hi: color-mix(in srgb, var(--c) 72%, #fff); --lo: color-mix(in srgb, var(--c) 55%, #000);
  box-sizing: border-box; width: calc(var(--u) * 63); height: calc(var(--u) * 88); flex: none;
  border-radius: calc(var(--u) * 3.2); padding: calc(var(--u) * 2.3); position: relative; overflow: hidden;
  display: flex; flex-direction: column; gap: calc(var(--u) * 1.2); color: #16181d; text-align: start;
  background: linear-gradient(160deg, var(--hi), var(--c) 42%, var(--lo));
  box-shadow: inset 0 0 0 calc(var(--u) * .45) rgba(0,0,0,.45), inset 0 0 0 calc(var(--u) * 1) rgba(255,255,255,.14);
  font-family: "IBM Plex Sans Condensed", "Arial Narrow", sans-serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.tcg *, .tcg *::before { box-sizing: border-box; }
.tcg::before { content: ""; position: absolute; inset: 0; pointer-events: none; opacity: .5;
  background: repeating-linear-gradient(135deg, rgba(255,255,255,.07) 0 calc(var(--u) * .5), transparent calc(var(--u) * .5) calc(var(--u) * 1.6)); }
.tcg > * { position: relative; }
.tcg .nm { height: calc(var(--u) * 8.4); flex: none; display: flex; align-items: center; justify-content: space-between; gap: calc(var(--u) * 1.4);
  padding: 0 calc(var(--u) * 1.4) 0 calc(var(--u) * 2.2); border-radius: calc(var(--u) * 1.4);
  background: linear-gradient(#ffffff, #e4e8ee); box-shadow: inset 0 calc(var(--u) * -.45) 0 rgba(0,0,0,.14), 0 calc(var(--u) * .35) calc(var(--u) * .8) rgba(0,0,0,.35); }
.tcg .nm b { font: 800 calc(var(--u) * 4.4)/1 "Bricolage Grotesque", "Arial Narrow", sans-serif; letter-spacing: -.02em; overflow: hidden; }
.tcg .nm b.s1 { font-size: calc(var(--u) * 3.95); } .tcg .nm b.s2 { font-size: calc(var(--u) * 3.45); } .tcg .nm b.s3 { font-size: calc(var(--u) * 3.0); line-height: 1.05; } .tcg .nm b.s4 { font-size: calc(var(--u) * 2.6); line-height: 1.05; }
.tcg .attr { flex: none; width: calc(var(--u) * 5.8); height: calc(var(--u) * 5.8); border-radius: 50%; display: grid; place-items: center;
  background: radial-gradient(circle at 35% 30%, var(--hi), var(--lo)); color: #fff; box-shadow: 0 0 0 calc(var(--u) * .4) #fff, 0 0 0 calc(var(--u) * .7) rgba(0,0,0,.35); }
.tcg .attr .ic, .tcg .sb .ic { width: 62%; height: 62%; }
.tcg .lv { height: calc(var(--u) * 4.6); flex: none; display: flex; align-items: center; justify-content: space-between; gap: calc(var(--u) * 1); color: #fff;
  font: 700 calc(var(--u) * 2.5)/1 "Barlow Condensed", "Arial Narrow", sans-serif; letter-spacing: .08em; text-transform: uppercase; }
.tcg .lv > span { display: flex; align-items: center; gap: calc(var(--u) * .8); }
.tcg .sb { width: calc(var(--u) * 4.4); height: calc(var(--u) * 4.4); border-radius: 50%; display: grid; place-items: center; color: #fff;
  background: var(--s); box-shadow: 0 0 0 calc(var(--u) * .35) #fff; }
.tcg .coin { width: calc(var(--u) * 2.8); height: calc(var(--u) * 2.8); border-radius: 50%; background: radial-gradient(circle at 35% 30%, #fff3b0, #e0a800);
  box-shadow: 0 0 0 calc(var(--u) * .25) rgba(0,0,0,.45); }
.tcg .tick { width: calc(var(--u) * 2.2); height: calc(var(--u) * 2.2); transform: rotate(45deg); background: #fff; box-shadow: 0 0 0 calc(var(--u) * .25) rgba(0,0,0,.45); }
.tcg .off { opacity: .28; }
.tcg .star { color: #fde047; font-size: calc(var(--u) * 3.6); line-height: 1; text-shadow: 0 0 calc(var(--u) * .5) rgba(0,0,0,.6); }
.tcg .art { flex: none; height: calc(var(--u) * 37.5); border-radius: calc(var(--u) * .7); overflow: hidden; background: #0f172a;
  box-shadow: 0 0 0 calc(var(--u) * .55) rgba(255,255,255,.9), 0 0 0 calc(var(--u) * .9) rgba(0,0,0,.45); margin: calc(var(--u) * .5) calc(var(--u) * .9); }
.tcg .art svg { width: 100%; height: 100%; display: block; }
/* Pictures keep left-to-right coordinates in right-to-left languages, so labels stay anchored where they were drawn. */
.tcg .art svg, .mat .art svg, .tcg.back svg { direction: ltr; }
.tcg.tcg-q .art { height: calc(var(--u) * 31); }
.tcg.tcg-t .art { height: calc(var(--u) * 43); }
.tcg.tcg-s .art { height: calc(var(--u) * 40.5); }
.tcg.tcg-x .art { height: calc(var(--u) * 41); }
.tcg .tb { flex: 1; min-height: 0; display: flex; flex-direction: column; gap: calc(var(--u) * .7); padding: calc(var(--u) * 1.1) calc(var(--u) * 1.7) calc(var(--u) * 1);
  border-radius: calc(var(--u) * 1); background: linear-gradient(#f8f9f6, #eceee8); box-shadow: inset 0 0 0 calc(var(--u) * .3) rgba(0,0,0,.28); }
.tcg .ty { font: 700 calc(var(--u) * 2.45)/1.1 "Barlow Condensed", "Arial Narrow", sans-serif; letter-spacing: .05em; text-transform: uppercase; color: #3b3f47; }
.tcg .fx { margin: 0; font-size: calc(var(--u) * 2.95 * var(--fit, 1)); line-height: 1.24; }
.tcg.tcg-q .fx { font-size: calc(var(--u) * 2.75 * var(--fit, 1)); line-height: 1.25; }
.tcg .row { display: flex; flex-wrap: wrap; align-items: center; gap: calc(var(--u) * .6) calc(var(--u) * 1.2);
  font: 700 calc(var(--u) * 2.3 * (0.4 + 0.6 * var(--fit, 1)))/1.15 "Barlow Condensed", "Arial Narrow", sans-serif; letter-spacing: .04em; text-transform: uppercase; color: #4b5059; }
.tcg .row .ic { width: calc(var(--u) * 3.5); height: calc(var(--u) * 3.5); }
/* "Good for" / "Struggles with": each situation spelled out after its icon, a little tighter than the other rows */
.tcg .row.cons { column-gap: calc(var(--u) * .9); letter-spacing: .02em; }
.tcg .row .yes, .tcg .row .no { display: inline-flex; gap: calc(var(--u) * .3); align-items: center; }
.tcg .row .yes { color: #0f7a3c; } .tcg .row .no { color: #b42318; }
.tcg .row .yes .ic, .tcg .row .no .ic { width: calc(var(--u) * 2.7); height: calc(var(--u) * 2.7); }
.tcg .row .k { color: #8a8f98; }
/* label then plain text: the text starts on the label's line instead of dropping below it */
.tcg .row.flow { display: block; } .tcg .row.flow .k { margin-inline-end: calc(var(--u) * .9); }
.tcg .chip { display: inline-flex; align-items: center; gap: calc(var(--u) * .5); padding: calc(var(--u) * .3) calc(var(--u) * 1.1) calc(var(--u) * .3) calc(var(--u) * .6);
  border-radius: calc(var(--u) * 3); background: #1f2937; color: #fff; font: 600 calc(var(--u) * 2.4)/1 "Barlow Condensed", "Arial Narrow", sans-serif; letter-spacing: .03em; text-transform: uppercase; }
.tcg .chip .ic { width: calc(var(--u) * 3); height: calc(var(--u) * 3); color: #fcd34d; }
.tcg .dot { display: inline-block; width: calc(var(--u) * 2.6); height: calc(var(--u) * 2.6); border-radius: 50%; box-shadow: 0 0 0 calc(var(--u) * .25) rgba(0,0,0,.35); }
.tcg .ft { margin-top: auto; display: flex; justify-content: space-between; gap: calc(var(--u) * 1); padding-top: calc(var(--u) * .5);
  border-top: calc(var(--u) * .25) solid rgba(0,0,0,.18); font: 600 calc(var(--u) * 2.1)/1 "Barlow Condensed", "Arial Narrow", sans-serif; letter-spacing: .06em; color: #6b7079; text-transform: uppercase; }
.tcg .ref { margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: calc(var(--u) * .7); font-size: calc(var(--u) * 2.45); line-height: 1.2; }
.tcg .ref li { display: flex; gap: calc(var(--u) * 1); align-items: flex-start; }
.tcg .ref .ic { flex: none; width: calc(var(--u) * 3.4); height: calc(var(--u) * 3.4); }
/* card back */
.tcg.back { padding: calc(var(--u) * 3); background: radial-gradient(circle at 50% 42%, #24345a, #0f172a 70%); }
.tcg.back .bk { flex: 1; border-radius: calc(var(--u) * 2); border: calc(var(--u) * .5) solid rgba(252,211,77,.75); display: grid; place-items: center; overflow: hidden;
  background: repeating-conic-gradient(from 0deg at 50% 45%, rgba(255,255,255,.035) 0 10deg, transparent 10deg 20deg); }
.tcg.back svg { width: 86%; }
.tcg.back { background: radial-gradient(circle at 50% 42%, #9A3412, #431407 72%); }
.tcg.back .bk { border-color: rgba(253,186,116,.8); }
/* Major Revisions card types */
.tcg.tcg-m .art { height: calc(var(--u) * 17); }
.tcg.tcg-r .art { height: calc(var(--u) * 27); }
.tcg.tcg-v .art { height: calc(var(--u) * 33); }
.tcg.tcg-p .art { height: calc(var(--u) * 37); }
.tcg.tcg-m .tb { gap: calc(var(--u) * .9); }
.tcg.tcg-m .fx { font-size: calc(var(--u) * 2.85 * var(--fit, 1)); line-height: 1.22; font-style: italic; }
.tcg .ans { margin: 0; font-size: calc(var(--u) * 2.8 * var(--fit, 1)); line-height: 1.22; }
.tcg .ans .k { font: 700 calc(var(--u) * 2.25 * (0.4 + 0.6 * var(--fit, 1)))/1 "Barlow Condensed", "Arial Narrow", sans-serif; letter-spacing: .04em;
  text-transform: uppercase; color: #8a8f98; margin-inline-end: calc(var(--u) * .8); }
.tcg .ans.bad .k { color: #b42318; }
.tcg .ans .ans-t:empty::before { content: "▮▮▮▮▮ ▮▮▮▮ ▮▮▮▮▮▮ ▮▮▮"; color: #c9ccd2; letter-spacing: .05em; }
.tcg .ans.open { background: #fff7d6; border-radius: calc(var(--u) * .6); box-shadow: 0 0 0 calc(var(--u) * .5) #fff7d6; }
.tcg .sb { box-shadow: 0 0 0 calc(var(--u) * .35) #fff; }
.tcg .tag { display: inline-flex; align-items: center; gap: calc(var(--u) * .6); }
.tcg .bad-tag { background: #b42318; color: #fff; border-radius: calc(var(--u) * 2); padding: calc(var(--u) * .4) calc(var(--u) * 1.2); }
.tcg .ok-tag { background: #0f7a3c; color: #fff; border-radius: calc(var(--u) * 2); padding: calc(var(--u) * .4) calc(var(--u) * 1.2); }
.tcg .ref.rules li b { font-weight: 600; }
.tcg.tcg-m .lv > span:first-child { min-width: 0; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; }
.tcg .tag { white-space: nowrap; }
.tcg .items { text-transform: none; letter-spacing: .02em; }
.tcg.tcg-ref .ref { font-size: calc(var(--u) * 3); gap: calc(var(--u) * 1.6); }
"""


def _name(s):
    n = len(s)
    cls = "s4" if n > 38 else "s3" if n > 30 else "s2" if n > 24 else "s1" if n > 18 else ""
    return f'<b class="{cls}">{e(s)}</b>'


def _art(fn, uid, color):
    inner = fn() if fn else art.text(100, 82, "ART", 16, art.DIM)
    return f'<div class="art">{art.frame(inner, uid, art.shade(color, .12), art.shade(color, -.45))}</div>'


class Ctx:
    """Lookup tables the renderers need (built once from the card data)."""

    def __init__(self, d):
        self.meta = d["meta"]
        self.SLOT = {s["id"]: s for s in d["meta"]["slots"]}
        self.VERDICT = {v["id"]: v for v in d["meta"]["verdicts"]}
        self.R = {r["id"]: r for r in d["requests"]}
        self.F = {f["id"]: f for f in d["flaws"]}
        self.G = {g["id"]: g for g in d["guidelines"]}
        self.rnum = {r["id"]: i + 1 for i, r in enumerate(d["requests"])}
        # Which flaws each request can catch: derived from the studies, the single source of truth.
        self.catches = {r["id"]: [] for r in d["requests"]}
        for st in d["studies"]:
            for slot in st["slots"].values():
                for f in slot["facts"]:
                    if "flaw" in f and f["flaw"]["type"] not in self.catches[f["request"]]:
                        self.catches[f["request"]].append(f["flaw"]["type"])


def slot_badge(cx, sid):
    s = cx.SLOT[sid]
    return f'<span class="sb" style="--s:{s["color"]}" title="{e(s["name"])}">{SLOT_ICONS[sid]}</span>'


def study_card(cx, st):
    g = cx.G[st["guideline"]]
    return f'''<div class="tcg tcg-p" style="--c:{STUDY_COLOR}">
  <div class="nm">{_name(st["title"])}<span class="attr">{STUDY_ICON}</span></div>
  <div class="lv"><span>{L("card.study")}</span><span>{e(g["name"])}</span></div>
  {_art(STUDY_ART.get(st["id"]), "p-" + st["id"], STUDY_COLOR)}
  <div class="tb">
    <div class="ty">[ {e(st["field"])} / {e(st["design"])} ]</div>
    <p class="fx">{e(st["claim"])}</p>
    <div class="row flow"><span class="k">{L("card.report_with")}</span> {e(g["name"])}</div>
    <div class="ft"><span>MR-P{st["id"][1:].zfill(2)}</span><span>{L("card.fictional")}</span></div>
  </div>
</div>'''


def manuscript_card(cx, st, sid, flawed=False, masked=False):
    """One slot of a study. flawed: the variant with the planted flaw. masked: as a reviewer first sees it
    (answers hidden, to be filled in by the app when a request is made; identical for both variants)."""
    slot = st["slots"][sid]
    s = cx.SLOT[sid]
    rows = ""
    planted = None
    for f in slot["facts"]:
        r = cx.R[f["request"]]
        bad = flawed and "flaw" in f
        if bad:
            planted = f["flaw"]
        txt = "" if masked else e(f["flaw"]["text"] if bad else f["sound"])
        rows += (f'<p class="ans{" bad" if bad else ""}" data-req="{r["id"]}"><span class="k">{"⚠ " if bad else ""}{e(r["name"])}</span>'
                 f'<span class="ans-t">{txt}</span></p>')
    if masked:
        state = L("card.under_review")
    elif planted:
        state = f'<span class="tag bad-tag">⚠ {L("card.flawed_" + planted["severity"])}</span>'
    else:
        state = f'<span class="tag ok-tag">✓ {L("card.sound")}</span>'
    flaw_row = (f'<div class="row flow"><span class="k">{L("card.planted")}</span> {e(cx.F[planted["type"]]["name"])}</div>'
                if planted and not masked else "")
    code = f'MR-{st["id"][1:]}{s["name"][0]}{"" if masked else ("-F" if flawed else "-S")}'
    return f'''<div class="tcg tcg-m" style="--c:{MANUSCRIPT_COLOR}" data-study="{st["id"]}" data-slot="{sid}">
  <div class="nm">{_name(s["name"])}<span class="attr" style="--hi:{s["color"]};--lo:{art.shade(s["color"], -.35)}">{SLOT_ICONS[sid]}</span></div>
  <div class="lv"><span>{e(st["title"])}</span><span>{state}</span></div>
  {_art(SLOT_ART[sid], f'm-{st["id"]}-{sid}-{"x" if masked else "f" if flawed else "s"}', MANUSCRIPT_COLOR)}
  <div class="tb">
    <div class="ty">[ {L("card.as_submitted")} ]</div>
    <p class="fx">{e(slot["submitted"])}</p>
    {rows}{flaw_row}
    <div class="ft"><span>{code}</span><span>{L("card.read_only")}</span></div>
  </div>
</div>'''


def request_card(cx, r):
    s = cx.SLOT[r["slot"]]
    catches = " · ".join(e(cx.F[f]["name"]) for f in cx.catches[r["id"]][:3])
    items = " · ".join(f'{e(cx.G[g]["name"].split()[0])} {e(n)}' for g, n in r["items"].items())
    return f'''<div class="tcg tcg-r" style="--c:{s["color"]}">
  <div class="nm">{_name(r["name"])}<span class="attr">{REQUEST_ICON}</span></div>
  <div class="lv"><span>{slot_badge(cx, r["slot"])} {L("card.ask_of", slot=s["name"])}</span><span>{L("card.request")}</span></div>
  {_art(REQUEST_ART.get(r["id"]), "r-" + r["id"], s["color"])}
  <div class="tb">
    <div class="ty">[ {L("card.request")} / {e(s["name"])} ]</div>
    <p class="fx">{e(r["ask"])}</p>
    {f'<div class="row flow"><span class="k">{L("card.catches")}</span> {catches}</div>' if catches else ""}
    <div class="row flow"><span class="k">{L("card.asked_by")}</span> <span class="items">{items}</span></div>
    <div class="ft"><span>MR-R{cx.rnum[r["id"]]:02d}</span><span>{L("card.costs_round")}</span></div>
  </div>
</div>'''


def verdict_card(cx, v, n):
    return f'''<div class="tcg tcg-v" style="--c:{v["color"]}">
  <div class="nm">{_name(v["name"])}<span class="attr">{VERDICT_ICON}</span></div>
  <div class="lv"><span>{L("card.verdict")}</span><span>{"●" * n}{"○" * (4 - n)}</span></div>
  {_art(VERDICT_ART.get(v["id"]), "v-" + v["id"], v["color"])}
  <div class="tb">
    <div class="ty">[ {L("card.verdict")} ]</div>
    <p class="fx">{e(v["short"])}</p>
    <p class="ans"><span class="k">{L("card.when")}</span>{e(v["when"])}</p>
    <div class="ft"><span>MR-V{n}</span><span>{L("card.with_report")}</span></div>
  </div>
</div>'''


def reference_cards(cx):
    sc = cx.meta["scoring"]

    def card(title, body):
        return f'''<div class="tcg tcg-ref" style="--c:{REFERENCE_COLOR}"><div class="nm"><b class="s1">{e(title)}</b></div>
  <div class="tb">{body}</div></div>'''
    slots = "".join(f'<li>{slot_badge(cx, s["id"])}<span><b>{e(s["name"])}</b> {e(s["ask"])}</span></li>' for s in cx.meta["slots"])
    steps = "".join(f"<li><span><b>{k + 1}.</b> {L('card.step' + str(k + 1))}</span></li>" for k in range(5))
    score = (f'<ul class="ref rules"><li><span><b>{L("card.sc_found")}</b> +{sc["flaw_found"]}</span></li>'
             f'<li><span><b>{L("card.sc_wrong")}</b> {sc["wrong_card"]}</span></li>'
             f'<li><span><b>{L("card.sc_verdict")}</b> +{sc["verdict"]}</span></li>'
             f'<li><span><b>{L("card.sc_unused")}</b> +{sc["unused_request"]}</span></li>'
             f'<li><span><b>{L("card.sc_author")}</b> +{sc["author_per_flaw"]}</span></li></ul>')
    return [card(S("card.ref_slots"), f'<ul class="ref">{slots}</ul>'),
            card(S("card.ref_turn"), f'<ul class="ref rules">{steps}</ul>'),
            card(S("card.ref_score"), score)]


def card_back():
    logo = ('<svg viewBox="0 0 120 150" xmlns="http://www.w3.org/2000/svg">'
            '<g transform="rotate(-10 60 64)"><circle cx="60" cy="64" r="40" fill="none" stroke="#FDBA74" stroke-width="3"/>'
            '<circle cx="60" cy="64" r="34" fill="none" stroke="#FDBA74" stroke-width="1.2"/>'
            '<text x="60" y="78" font-size="38" fill="#FFF7ED" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="800">MR</text></g>'
            # textLength keeps the two-word title inside the frame whatever the font's real width.
            '<text x="60" y="122" font-size="12.5" fill="#FFF7ED" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="800" textLength="108" lengthAdjust="spacingAndGlyphs">MAJOR REVISIONS</text>'
            '<text x="60" y="137" font-size="6.6" fill="#FDBA74" text-anchor="middle" font-family="Barlow Condensed, sans-serif" font-weight="700" letter-spacing="1.2">' + L("card.back_kit") + '</text></svg>')
    return f'<div class="tcg back" style="--c:{BACK_COLOR}"><div class="bk">{logo}</div></div>'
