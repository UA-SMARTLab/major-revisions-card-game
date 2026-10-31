#!/usr/bin/env python3
"""Validate the Major Revisions card data and generate, for every language in i18n/languages.json,
the printable deck, the flaw key and the web app (plus the English ANSWER_KEY.md).

Usage:  python3 tools/build.py   (from anywhere)
Only the Python standard library is needed.
"""
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SEVERITY = ["minor", "major", "reject"]
SLOTS = ["question", "method", "sample", "measurement", "analysis"]


def load(name):
    return json.loads((DATA / f"{name}.json").read_text(encoding="utf-8"))


meta = load("meta")
studies = load("studies")
requests = load("requests")
flaws = load("flaws")
guidelines = load("guidelines")

R = {r["id"]: r for r in requests}
F = {f["id"]: f for f in flaws}
G = {g["id"]: g for g in guidelines}


# --------------------------------------------------------------------------- validation
errors, warnings = [], []


def need_ref(x, where):
    if not (x.get("ref") or {}).get("url", "").startswith("https://"):
        errors.append(f"{where}: no key reference (ref.url must start with https://)")


for coll, name in [(studies, "study"), (requests, "request"), (flaws, "flaw"), (guidelines, "guideline")]:
    dupes = [i for i, n in Counter(x["id"] for x in coll).items() if n > 1]
    if dupes:
        errors.append(f"duplicate {name} ids: {dupes}")
if [s["id"] for s in meta["slots"]] != SLOTS:
    errors.append(f"meta.slots must be, in order: {SLOTS}")
if [v["id"] for v in meta["verdicts"]] != ["accept"] + SEVERITY:
    errors.append("meta.verdicts must be accept, minor, major, reject (in that order)")

for g in guidelines:
    need_ref(g, f"guideline {g['id']}")
    if not g.get("checklist", "").startswith("https://"):
        errors.append(f"guideline {g['id']}: no checklist link")
for f in flaws:
    need_ref(f, f"flaw {f['id']}")
    if len(f["name"]) > 30:
        warnings.append(f"flaw {f['id']}: name is {len(f['name'])} chars (may crowd the card)")
for r in requests:
    if r["slot"] not in SLOTS:
        errors.append(f"request {r['id']}: unknown slot {r['slot']}")
    for g in r["items"]:
        if g not in G:
            errors.append(f"request {r['id']}: unknown guideline {g}")
    if len(r["ask"]) > 100:
        warnings.append(f"request {r['id']}: ask is {len(r['ask'])} chars (may overflow card)")

used_flaws, used_requests = Counter(), Counter()
for st in studies:
    w = f"study {st['id']}"
    if st["guideline"] not in G:
        errors.append(f"{w}: unknown guideline {st['guideline']}")
    if sorted(st["slots"]) != sorted(SLOTS):
        errors.append(f"{w}: needs exactly the slots {SLOTS}")
        continue
    if len(st["claim"]) > 130:
        warnings.append(f"{w}: claim is {len(st['claim'])} chars (may overflow card)")
    flawable = 0
    for sid in SLOTS:
        slot = st["slots"][sid]
        ws = f"{w} {sid}"
        if not 1 <= len(slot["facts"]) <= 2:
            errors.append(f"{ws}: needs 1 or 2 facts (a card holds two answers)")
        if len(slot["submitted"]) > 110:
            warnings.append(f"{ws}: submitted text is {len(slot['submitted'])} chars (may overflow card)")
        reqs = [f["request"] for f in slot["facts"]]
        if len(set(reqs)) != len(reqs):
            errors.append(f"{ws}: a request answered twice")
        # Both answers of a slot may carry a flaw: each becomes its own flawed card (F, F2), so a card still
        # carries at most one flaw.
        flawable += any("flaw" in f for f in slot["facts"])
        for f in slot["facts"]:
            used_requests[f["request"]] += 1
            if f["request"] not in R:
                errors.append(f"{ws}: unknown request {f['request']}")
                continue
            if R[f["request"]]["slot"] != sid:
                errors.append(f"{ws}: request {f['request']} belongs on the {R[f['request']]['slot']} card")
            texts = [f["sound"]] + ([f["flaw"]["text"]] if "flaw" in f else [])
            for t in texts:
                if len(t) > 120:
                    warnings.append(f"{ws} {f['request']}: answer is {len(t)} chars (may overflow card)")
            if "flaw" in f:
                fl = f["flaw"]
                used_flaws[fl["type"]] += 1
                if fl["type"] not in F:
                    errors.append(f"{ws}: unknown flaw type {fl['type']}")
                if fl["severity"] not in SEVERITY:
                    errors.append(f"{ws}: severity must be one of {SEVERITY}")
                if st["guideline"] not in R[f["request"]]["items"]:
                    errors.append(f"{ws}: the request that catches this flaw ({f['request']}) has no {st['guideline']} item")
                if not fl.get("why"):
                    errors.append(f"{ws}: flaw needs a 'why' (what is wrong and whether it can be fixed)")
    if flawable < 3:
        errors.append(f"{w}: only {flawable} cards can carry a flaw; at least 3 are needed for varied deals")

for f in flaws:
    if not used_flaws[f["id"]]:
        warnings.append(f"flaw {f['id']} is planted in no study")
for r in requests:
    if not used_requests[r["id"]]:
        warnings.append(f"request {r['id']} is answered by no study")


# --------------------------------------------------------------------------- languages
sys.path.insert(0, str(Path(__file__).resolve().parent))
import art  # noqa: E402  (needs the tools/ folder on sys.path)
import cards  # noqa: E402
import i18n  # noqa: E402

e = html.escape
DATA_ALL = {"meta": meta, "studies": studies, "requests": requests, "flaws": flaws, "guidelines": guidelines}


class Lang:
    """Everything one language's outputs need: translated data, its strings, and where its files go."""

    def __init__(self, info):
        self.code, self.info = info["code"], info
        self.rtl = info.get("dir") == "rtl"
        self.d = i18n.translated(DATA_ALL, self.code)
        table = i18n.ui_strings(self.code)
        self.ui, self.art = table["ui"], table["art"]
        self.S = i18n.Strings(self.ui)
        sub = "" if self.code == "en" else self.code
        self.print_dir = ROOT / "print" / sub
        self.app_dir = ROOT / "app" / sub

    def activate(self):
        """Point the card renderer at this language and return its rendering context."""
        cards.S = self.S
        art.TR = self.art
        return cards.Ctx(self.d)

    def html_attrs(self):
        return f'lang="{self.code}" dir="{"rtl" if self.rtl else "ltr"}"'

    def fonts(self):
        extra = self.info.get("font")
        return cards.FONTS_URL + (f"&family={extra.replace(' ', '+')}:wght@400;600;700" if extra else "")

    def extra_font_link(self):
        extra = self.info.get("font")
        return f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={extra.replace(" ", "+")}:wght@400;600;700&display=swap">' if extra else ""

    def lang_css(self):
        extra = self.info.get("font")
        if not extra:
            return ""
        return (f'html[lang="{self.code}"] body, html[lang="{self.code}"] body * {{ font-family: "{extra}", "IBM Plex Sans", system-ui, sans-serif !important;'
                " letter-spacing: 0 !important; }"
                f' html[lang="{self.code}"] .tcg .nm b {{ line-height: 1.45; padding-block: .1em; }}')


SHEET_CSS = """
@page { size: A4; margin: 0; }
body { margin: 0; background: #d7dbe0; font-family: "IBM Plex Sans Condensed", "Arial Narrow", sans-serif; }
.sheet { width: 210mm; height: 297mm; margin: 0 auto 8mm; background: #fff; position: relative; break-after: page; display: grid; place-items: center; }
.grid { display: grid; grid-template-columns: repeat(3, 63mm); grid-auto-rows: 88mm; gap: 1mm; }
.label { position: absolute; top: 6mm; inset-inline-start: 10mm; font-size: 8pt; color: #888; }
.cover, .key { width: 210mm; min-height: 297mm; margin: 0 auto 8mm; background: #fff; padding: 16mm; box-sizing: border-box; break-after: page; font-size: 10pt; line-height: 1.45; }
.cover h1, .key h1 { font: 800 26pt/1.1 "Bricolage Grotesque", sans-serif; margin: 0 0 4mm; }
.cover table { border-collapse: collapse; margin: 4mm 0; } .cover td { padding: 1mm 6mm 1mm 0; border-bottom: .2mm solid #ddd; }
.key table { border-collapse: collapse; width: 100%; font-size: 8.4pt; }
.key th, .key td { text-align: start; vertical-align: top; padding: 1.2mm 2mm; border-bottom: .2mm solid #ddd; }
.key th { font: 700 8pt "Barlow Condensed", sans-serif; letter-spacing: .06em; text-transform: uppercase; color: #555; }
.key td.id { font-weight: 600; white-space: nowrap; } .key .reject { color: #991b1b; font-weight: 600; } .key .minor { color: #4d7c0f; }
.key h2 { font: 700 13pt "Barlow Condensed", sans-serif; letter-spacing: .04em; text-transform: uppercase; margin: 5mm 0 1mm; }
.key a { color: #9a3412; }
.langs { float: inline-end; font-size: 9pt; } .langs a { margin-inline-start: 2mm; color: #9a3412; }
@media print { body { background: #fff; } .sheet, .cover, .key { margin: 0; } .label, .langs { display: none; } }
"""


def lang_links(g, langs, page_name):
    up = "" if g.code == "en" else "../"
    return '<span class="langs">' + "".join(
        f'<a href="{up}{"" if x["code"] == "en" else x["code"] + "/"}{page_name}" hreflang="{x["code"]}">{e(x["name"])}</a>'
        for x in langs if x["code"] != g.code) + "</span>"


def sheets(g, cards_html, title, per=9):
    out = []
    for k in range(0, len(cards_html), per):
        out.append(f'<section class="sheet"><div class="label">{e(g.S("print.page", deck=title, n=k // per + 1))}</div>'
                   f'<div class="grid">{"".join(cards_html[k:k + per])}</div></section>')
    return "".join(out)


def page(g, title, body):
    return f"""<!doctype html>
<html {g.html_attrs()}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title><link rel="stylesheet" href="{g.fonts()}">
<style>{cards.CARD_CSS}{SHEET_CSS}{g.lang_css()}</style></head><body>{body}<script>{cards.FIT_JS}</script></body></html>"""


def manuscript_deck(cx, d):
    """Per study, the sound card of each slot, then its flawed cards (F, then F2) where the slot has flaws."""
    out = []
    for st in d["studies"]:
        for sid in SLOTS:
            out.append(cards.manuscript_card(cx, st, sid))
            for k in range(len(cards.flawed_facts(st["slots"][sid]))):
                out.append(cards.manuscript_card(cx, st, sid, k))
    return out


def build_print(g, langs):
    cx = g.activate()
    d, S = g.d, g.S
    decks = [
        (S("print.reference"), cards.reference_cards(cx)),
        (S("deck.studies"), [cards.study_card(cx, st) for st in d["studies"]]),
        (S("deck.requests"), [cards.request_card(cx, r) for r in d["requests"]]),
        (S("deck.verdicts"), [cards.verdict_card(cx, v, i + 1) for i, v in enumerate(d["meta"]["verdicts"])]),
        (S("deck.manuscripts"), manuscript_deck(cx, d)),
    ]
    total = sum(len(c) for _, c in decks)
    rows = "".join(f'<tr><td>{e(n)}</td><td>{e(S("print.cards", n=len(c)))}</td><td>{e(S("print.pages", n=-(-len(c) // 9)))}</td></tr>' for n, c in decks)
    title = d["meta"]["title"]
    cover = f"""<div class="cover">{lang_links(g, langs, "cards.html")}<h1>{e(S("print.title", game=title))}</h1>
<p>{e(S("print.intro", tagline=d["meta"]["tagline"], version=d["meta"]["version"], total=total))}</p>
<table>{rows}</table>
<p>{S("print.printing_html")}</p>
<p>{S("print.answers_html")}</p></div>"""
    body = cover + "".join(sheets(g, c, n) for n, c in decks)
    g.print_dir.mkdir(parents=True, exist_ok=True)
    out = g.print_dir / "cards.html"
    out.write_text(page(g, f"{title}: print sheets", body), encoding="utf-8")
    (g.print_dir / "backs.html").write_text(page(g, f"{title}: card backs", sheets(g, [cards.card_back()] * 9, S("print.backs"))), encoding="utf-8")
    build_flaw_key(g, langs)
    return out, total


def planted(st):
    """(slot, fact, variant) for every answer in a study that can carry a flaw; variant k is the slot's k-th
    flawed card (0 is F, 1 is F2)."""
    return [(sid, st["slots"][sid]["facts"][i], k) for sid in SLOTS for k, i in enumerate(cards.flawed_facts(st["slots"][sid]))]


def build_flaw_key(g, langs):
    cx = g.activate()
    d, S = g.d, g.S
    slot_name = {s["id"]: s["name"] for s in d["meta"]["slots"]}
    verdict = {v["id"]: v["name"] for v in d["meta"]["verdicts"]}
    body = (f'<div class="key">{lang_links(g, langs, "answer-key.html")}<h1>{e(S("print.key_title", game=d["meta"]["title"]))}</h1>'
            f'<p>{e(S("print.key_intro"))}</p>')
    head = "".join(f"<th>{e(S(k))}</th>" for k in ("print.key_card", "print.key_flaw", "print.key_verdict", "print.key_caught", "print.key_why"))
    for st in d["studies"]:
        gl = cx.G[st["guideline"]]
        body += f'<h2>{st["id"]} · {e(st["title"])} ({e(st["design"])}, {e(gl["name"])})</h2><table><tr>{head}</tr>'
        for sid, f, k in planted(st):
            fl = f["flaw"]
            r = cx.R[f["request"]]
            body += (f'<tr><td class="id">{e(slot_name[sid])}<br>{e(cards.card_code(st, slot_name[sid], k))}</td><td>{e(cx.F[fl["type"]]["name"])}: {e(fl["text"])}</td>'
                     f'<td class="{fl["severity"]}">{e(verdict[fl["severity"]])}</td>'
                     f'<td>{e(r["name"])} ({e(gl["name"])} {e(S("print.item", n=r["items"][st["guideline"]]))})</td>'
                     f'<td>{e(fl["why"])} <a href="{e(cx.F[fl["type"]]["ref"]["url"])}">{e(cx.F[fl["type"]]["ref"]["cite"].split(". ")[0])}</a></td></tr>')
        body += "</table>"
    (g.print_dir / "answer-key.html").write_text(page(g, S("print.key_title", game=d["meta"]["title"]), body), encoding="utf-8")


def build_answer_key():
    slot_name = {s["id"]: s["name"] for s in meta["slots"]}
    verdict = {v["id"]: v["name"] for v in meta["verdicts"]}
    L = [f"# {meta['title']}: flaw key", "",
         "Generated from `data/` by `tools/build.py`. Don't edit by hand.", "",
         "The verdict for a manuscript is the most severe verdict among its planted flaws "
         "(Reject > Major revisions > Minor revisions); a manuscript with no flaw gets Accept.", ""]
    for st in studies:
        gl = G[st["guideline"]]
        L += [f"## {st['id']} · {st['title']} ({st['design']}, {gl['name']})", "", f"> {st['claim']}", ""]
        for sid in SLOTS:
            slot = st["slots"][sid]
            L.append(f"**{slot_name[sid]}.** *As submitted:* {slot['submitted']}")
            L.append("")
            variant = {i: k for k, i in enumerate(cards.flawed_facts(slot))}
            for i, f in enumerate(slot["facts"]):
                r = R[f["request"]]
                item = r["items"].get(st["guideline"])
                where = f" ({gl['name']} item {item})" if item else ""
                L.append(f"- {r['name']}{where}: sound: {f['sound']}")
                if "flaw" in f:
                    fl = f["flaw"]
                    code = cards.card_code(st, slot_name[sid], variant[i])
                    L.append(f"  - **Flawed, card {code} ({F[fl['type']]['name']}, {verdict[fl['severity']]}):** {fl['text']}")
                    L.append(f"  - *Why:* {fl['why']} See [{F[fl['type']]['ref']['cite']}]({F[fl['type']]['ref']['url']}).")
            L.append("")
    L += ["## Coverage", "", "| Request | Card | Answered in | Catches |", "|---|---|---|---|"]
    for r in requests:
        where = [st["id"] for st in studies for f in st["slots"][r["slot"]]["facts"] if f["request"] == r["id"]]
        catches = sorted({F[f["flaw"]["type"]]["name"] for st in studies for f in st["slots"][r["slot"]]["facts"] if f["request"] == r["id"] and "flaw" in f})
        L.append(f"| {r['name']} | {slot_name[r['slot']]} | {', '.join(where)} | {', '.join(catches)} |")
    (ROOT / "ANSWER_KEY.md").write_text("\n".join(L) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- web app
def fill_template(tpl, g):
    """Replace {{key}} in the page template with this language's string (escaped, unless the key ends in _html)."""
    def sub(m):
        key = m.group(1)
        if key not in g.ui:
            raise KeyError(f"app/template.html uses unknown string key {key!r}; add it to i18n/en/ui.json")
        return g.ui[key] if key.endswith("_html") else e(g.ui[key])
    return re.sub(r"\{\{([\w.]+)\}\}", sub, tpl)


def build_app(g, langs):
    cx = g.activate()
    d = g.d
    tpl = fill_template((ROOT / "app" / "template.html").read_text(encoding="utf-8"), g)
    variants = lambda st, sid: range(len(cards.flawed_facts(st["slots"][sid])))
    rendered = {
        "studies": {st["id"]: cards.study_card(cx, st) for st in d["studies"]},
        "requests": {r["id"]: cards.request_card(cx, r) for r in d["requests"]},
        "verdicts": {v["id"]: cards.verdict_card(cx, v, i + 1) for i, v in enumerate(d["meta"]["verdicts"])},
        "masked": {st["id"]: {sid: cards.manuscript_card(cx, st, sid, masked=True) for sid in SLOTS} for st in d["studies"]},
        # flawed[k]: the card whose k-th flawed answer is planted (empty for a slot without a flaw)
        "full": {st["id"]: {sid: {"sound": cards.manuscript_card(cx, st, sid),
                                  "flawed": [cards.manuscript_card(cx, st, sid, k) for k in variants(st, sid)]}
                            for sid in SLOTS} for st in d["studies"]},
        "back": cards.card_back(),
    }
    bundle = {**d, "catches": cx.catches, "cards": rendered}

    def href(x):
        return ("" if g.code == "en" else "../") + ("" if x["code"] == "en" else x["code"] + "/")

    def js(v):
        return json.dumps(v, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    lang = {"code": g.code, "dir": "rtl" if g.rtl else "ltr",
            "langs": [{"code": x["code"], "name": x["name"], "href": href(x), "current": x["code"] == g.code} for x in langs]}
    body = (tpl.replace("/*__DATA__*/null", js(bundle))
            .replace("/*__CARD_CSS__*/", cards.CARD_CSS + g.lang_css())
            .replace("/*__UI__*/{}", js(g.ui))
            .replace("/*__LANG__*/{}", js(lang))
            .replace("/*__FIT__*/", cards.FIT_JS)
            .replace("<!--__EXTRA_FONTS__-->", g.extra_font_link()))
    # The template is page content only (a hosted version can wrap it); the local copy gets its own skeleton.
    g.app_dir.mkdir(parents=True, exist_ok=True)
    out = g.app_dir / "index.html"
    out.write_text(f'<!doctype html>\n<html {g.html_attrs()}><head><meta charset="utf-8">'
                   '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
                   '<style>[hidden]{display:none!important}body{margin:0}</style></head><body>\n'
                   + body + "\n</body></html>\n", encoding="utf-8")
    return out


def manuscripts_possible():
    """How many different manuscripts the app can deal: per study, every choice of 1 or 2 flawed slots, times the
    flawed cards each chosen slot has (one or two)."""
    n = 0
    for st in studies:
        v = [len(cards.flawed_facts(st["slots"][sid])) for sid in SLOTS]
        n += sum(v) + sum(v[i] * v[j] for i in range(len(v)) for j in range(i + 1, len(v)))
    return n


if __name__ == "__main__":
    for w in warnings:
        print("warning:", w)
    for err in errors:
        print("ERROR:", err)
    if errors:
        sys.exit(1)
    i18n.write_source(DATA_ALL)
    langs = i18n.languages()
    bad = [msg for info in langs if info["code"] != "en" for msg in i18n.problems(info["code"])]
    for msg in bad:
        print("ERROR:", msg)
    if bad:
        sys.exit(1)
    build_answer_key()
    for info in langs:
        g = Lang(info)
        _, n = build_print(g, langs)
        if (ROOT / "app" / "template.html").exists():
            build_app(g, langs)
        if info["code"] == "en":
            print(f"ok: {len(studies)} studies, {len(requests)} requests, {len(flaws)} flaw types, "
                  f"{manuscripts_possible()} possible flawed manuscripts ({n} printable cards)")
            print("  en: source language")
        else:
            total, done = i18n.coverage(info["code"])
            print(f"  {info['code']}: {100 * done // max(total, 1)}% translated ({done}/{total} strings)")
