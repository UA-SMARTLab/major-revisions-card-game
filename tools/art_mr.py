"""Pictures for Major Revisions cards, drawn with the shared primitives in art.py.

Every picture is a diagram of the idea on the card (a flow diagram, a coding tree, a stamp), drawn by us.
Labels stay away from the top and bottom 20 units of the 200 x 150 box, which the card may crop.
"""
import math

from art import (ACC, COOL, DIM, FAINT, HOT, INK, _f, _icon, arrow, axes, check, circle, clock, cross, doc, eye, line, lcg,
                 magnifier, path, person, rect, scatter, text)

# --------------------------------------------------------------------------- slot icons (badges)
SLOT_ICONS = {
    "question": _icon('<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.4 2.3c-.6.3-.9.8-.9 1.4v.8"/><circle cx="12" cy="17" r=".7" fill="currentColor"/>'),
    "method": _icon('<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9h10M7 13h6M7 17h8"/>'),
    "sample": _icon('<circle cx="8" cy="8" r="2.6"/><circle cx="16" cy="8" r="2.6"/><path d="M3.5 19v-1.5A4.5 4.5 0 0 1 8 13a4.5 4.5 0 0 1 4 2.4A4.5 4.5 0 0 1 16 13a4.5 4.5 0 0 1 4.5 4.5V19"/>'),
    "measurement": _icon('<path d="M4 20a8 8 0 1 1 16 0"/><path d="M12 20l4-6"/><path d="M6 15l1.2.7M12 10.5V12M18 15l-1.2.7"/>'),
    "analysis": _icon('<path d="M4 20V4M4 20h16"/><path d="M7 16l4-5 3 3 5-7"/>'),
}
REQUEST_ICON = _icon('<path d="M4 5h16v11H9l-5 4z"/><path d="M9 9h6M9 12h4"/>')
VERDICT_ICON = _icon('<path d="M9 3h6v5l3 3H6l3-3z"/><path d="M5 14h14v3H5zM4 21h16"/>')
STUDY_ICON = _icon('<path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4M9 11h7M9 14h7M9 17h5"/>')

PAGE = "#0f172a66"


def _page(x, y, w, h, hi=None):
    """A manuscript page with five section bands; band `hi` (0-4) highlighted."""
    out = rect(x, y, w, h, PAGE, INK, 2.5, 4)
    bh = (h - 16) / 5
    for k in range(5):
        yy = y + 8 + k * bh
        c = ACC if k == hi else DIM
        out += line([(x + 8, yy + bh * .35), (x + w - 8, yy + bh * .35)], c, 3 if k == hi else 2)
        out += line([(x + 8, yy + bh * .7), (x + w * .6, yy + bh * .7)], c, 2)
    return out


# --------------------------------------------------------------------------- manuscript (slot) pictures
def _slot_art(k):
    def draw():
        return _page(64, 22, 72, 106, k) + arrow(150, 22 + 8 + (k + .5) * 18, 140, 22 + 8 + (k + .5) * 18, ACC, 3, head=7)
    return draw


SLOT_ART = {s: _slot_art(k) for k, s in enumerate(["question", "method", "sample", "measurement", "analysis"])}


# --------------------------------------------------------------------------- request pictures
def r_registration():
    out = doc(40, 26, 50, 66, INK, 4, PAGE) + clock(140, 58, 22, ACC, -40, 60)
    return out + arrow(96, 60, 112, 60, DIM, 2.5) + text(65, 112, "PLAN", 13, INK) + text(140, 102, "DATE", 13, ACC)


def r_hypothesis():
    out = path("M40,96 Q70,40 100,60 T160,40", DIM, 2.5, dash="5 5") + arrow(40, 96, 160, 40, ACC, 3)
    return out + text(100, 112, "H₁ BEFORE DATA", 13, INK)


def r_allocation():
    out = ""
    for k in range(6):
        out += rect(30 + k * 24, 46, 18, 26, PAGE, INK, 2, 3) + text(39 + k * 24, 65, "AB"[(k * 7 + 3) % 2], 12, ACC if k % 2 else INK)
    out += rect(22, 38, 156, 42, "none", DIM, 2, 6, dash="4 4")
    return out + text(100, 106, "SEALED SEQUENCE", 13, INK)


def r_intervention():
    out = rect(36, 30, 54, 70, PAGE, INK, 2.5, 5) + rect(110, 30, 54, 70, PAGE, INK, 2.5, 5)
    for k in range(3):
        out += line([(46, 48 + k * 16), (80, 48 + k * 16)], ACC, 2.5) + line([(120, 48 + k * 16), (154, 48 + k * 16)], DIM, 2.5)
    return out + text(63, 116, "DO THIS", 12, ACC) + text(137, 116, "OR THAT", 12, INK)


def r_timeline():
    out = arrow(24, 76, 180, 76, INK, 3)
    for x, lab, c in ((50, "13", ACC), (130, "15", INK)):
        out += circle(x, 76, 7, c) + text(x, 104, lab, 14, c)
    return out + text(50, 58, "EXPOSURE", 11, ACC) + text(130, 58, "OUTCOME", 11, INK)


def r_search():
    out = ""
    for k, x in enumerate((36, 72, 108)):
        out += path(f"M{x},44 v34 a14,5 0 0 0 28,0 v-34", INK, 2.5) + f'<ellipse cx="{x + 14}" cy="44" rx="14" ry="5" fill="none" stroke="{INK}" stroke-width="2.5"/>'
    return out + magnifier(156, 58, 14, ACC, 3.5) + text(100, 112, "EVERY SOURCE", 13, INK)


def r_reflexivity():
    out = person(64, 74, 1.7, INK) + person(136, 74, 1.7, ACC) + line([(82, 62), (118, 62)], DIM, 2.5, "4 4")
    return out + text(100, 116, "WHO ASKED?", 13, INK)


def r_reference_standard():
    out = rect(40, 34, 120, 60, PAGE, INK, 2.5, 6) + line([(52, 64), (148, 64)], DIM, 2)
    out += check(78, 52, 9) + cross(124, 78, 6)
    return out + text(100, 116, "THE TRUTH TEST", 13, ACC)


def r_recruitment():
    out = rect(26, 36, 70, 60, "none", DIM, 2, 6, dash="4 4")
    for i in range(3):
        for j in range(2):
            out += person(40 + i * 21, 56 + j * 26, .6, INK if (i + j) % 2 else DIM)
    out += arrow(102, 66, 130, 66, ACC, 3) + person(152, 72, 1.1, ACC)
    return out + text(100, 116, "WHO GOT IN?", 13, INK)


def r_flow():
    out = ""
    for y, w in ((26, 90), (60, 70), (94, 50)):
        out += rect(100 - w / 2, y, w, 20, PAGE, INK, 2.5, 3)
    out += arrow(100, 46, 100, 58, INK, 2.5, head=6) + arrow(100, 80, 100, 92, INK, 2.5, head=6)
    out += arrow(132, 70, 160, 70, HOT, 2.5, head=6) + arrow(122, 104, 160, 104, HOT, 2.5, head=6)
    return out + text(170, 74, "−", 14, HOT) + text(170, 108, "−", 14, HOT)


def r_sample_size():
    out = axes(30, 34, 140, 70, INK)
    pts = [(30 + x * 4, 104 - 70 * (1 - math.exp(-x / 9))) for x in range(0, 36)]
    out += line(pts, ACC, 3) + line([(110, 104), (110, 46)], DIM, 2, "4 4")
    return out + text(110, 116, "n", 15, ACC)


def r_saturation():
    out = axes(30, 34, 140, 70, INK)
    pts = [(30 + x * 4, 104 - 66 * (1 - math.exp(-x / 6))) for x in range(0, 36)]
    out += line(pts, ACC, 3)
    return out + text(100, 116, "NEW CODES", 12, INK)


def r_blinding():
    out = eye(100, 66, 1.6, INK, ACC) + line([(64, 98), (136, 34)], HOT, 5)
    return out + text(100, 118, "WHO KNEW?", 13, INK)


def r_instrument():
    out = path("M48,98 A52,52 0 0 1 152,98", INK, 3)
    for k in range(7):
        a = math.radians(180 + k * 30)
        out += line([(100 + 46 * math.cos(a), 98 + 46 * math.sin(a)), (100 + 52 * math.cos(a), 98 + 52 * math.sin(a))], DIM, 2)
    out += arrow(100, 98, 128, 62, ACC, 3) + circle(100, 98, 5, INK)
    return out + text(100, 116, "VALID?", 13, INK)


def r_coding():
    out = circle(100, 36, 8, ACC)
    for x in (56, 100, 144):
        out += line([(100, 44), (x, 70)], INK, 2.5) + circle(x, 76, 6, INK)
        for dx in (-12, 12):
            out += line([(x, 82), (x + dx, 100)], DIM, 2) + circle(x + dx, 104, 4, DIM)
    return out


def r_risk_of_bias():
    out = ""
    cols = (("#86EFAC", ACC, "#86EFAC", HOT), (ACC, "#86EFAC", "#86EFAC", "#86EFAC"), (HOT, HOT, ACC, "#86EFAC"))
    for j, row in enumerate(cols):
        for i, c in enumerate(row):
            out += circle(64 + i * 24, 46 + j * 24, 8, c)
        out += line([(30, 46 + j * 24), (48, 46 + j * 24)], DIM, 3)
    return out + text(100, 116, "BIAS PER STUDY", 12, INK)


def r_missing_data():
    out = ""
    rnd = lcg(7)
    for j in range(5):
        for i in range(8):
            gone = rnd() < .22
            out += rect(32 + i * 17, 30 + j * 15, 13, 11, "none" if gone else INK, HOT if gone else INK, 1.5 if gone else 0, 2, o=1 if gone else .85, dash="2 2" if gone else None)
    return out + text(100, 116, "WHO IS MISSING?", 12, INK)


def r_sensitivity():
    out = axes(30, 30, 140, 76, INK)
    for k, (y, c) in enumerate(((64, INK), (58, ACC), (70, DIM), (61, COOL))):
        out += line([(60 + k * 26, y - 10), (60 + k * 26, y + 10)], c, 2.5) + circle(60 + k * 26, y, 4.5, c)
    return out + line([(30, 92), (170, 92)], DIM, 1.5, "3 4")


def r_confounding():
    out = text(46, 104, "X", 18, INK) + text(154, 104, "Y", 18, INK) + text(100, 46, "Z", 18, HOT)
    out += arrow(92, 52, 56, 90, HOT, 2.5) + arrow(108, 52, 144, 90, HOT, 2.5) + arrow(60, 99, 140, 99, DIM, 2.5, "5 5")
    return out


def r_analysis_set():
    out = ""
    for g, x in enumerate((44, 124)):
        out += rect(x - 14, 34, 60, 66, "none", ACC if g == 0 else INK, 2.5, 6)
        for i in range(2):
            for j in range(2):
                out += person(x + 2 + i * 26, 56 + j * 28, .6, ACC if g == 0 else INK)
    return out + text(100, 116, "AS RANDOMISED", 12, INK)


def r_themes():
    out = ""
    rnd = lcg(3)
    for k in range(14):
        out += circle(30 + rnd() * 60, 36 + rnd() * 70, 3, DIM)
    out += arrow(96, 70, 120, 70, INK, 2.5)
    for k, c in enumerate((ACC, INK, COOL)):
        out += rect(128, 36 + k * 26, 46, 18, "none", c, 2.5, 9)
    return out


def r_thresholds():
    xs = [i * 3 for i in range(48)]
    a = [(40 + x, 100 - 50 * math.exp(-((x - 40) / 18) ** 2)) for x in xs]
    b = [(40 + x, 100 - 50 * math.exp(-((x - 85) / 18) ** 2)) for x in xs]
    out = line([(30, 100), (180, 100)], INK, 2.5) + line(a, INK, 3) + line(b, HOT, 3)
    return out + line([(102, 36), (102, 104)], ACC, 3, "6 4") + text(102, 116, "CUT-OFF", 12, ACC)


def r_heterogeneity():
    out = line([(100, 30), (100, 112)], DIM, 2, "4 4")
    for k, (x, w) in enumerate(((70, 18), (132, 22), (88, 14), (150, 16), (60, 20))):
        y = 38 + k * 14
        out += line([(x - w, y), (x + w, y)], INK, 2.5) + rect(x - 3, y - 3, 6, 6, INK, "none", 0, 1)
    return out + path("M86,120 L104,114 L122,120 L104,126 Z", ACC, 2, fill=ACC)


def r_reporting_bias():
    out = line([(100, 30), (100, 112)], DIM, 2) + line([(40, 112), (100, 30), (160, 112)], DIM, 2, "4 4")
    rnd = lcg(11)
    for k in range(16):
        y = 40 + rnd() * 66
        spread = (y - 30) * .62
        x = 100 + (rnd() * spread) if k % 4 else 100 - rnd() * spread * .4
        out += circle(x, y, 3.5, INK)
    return out + circle(70, 98, 5, "none", HOT, 2, dash="2 2") + circle(80, 104, 5, "none", HOT, 2, dash="2 2")


REQUEST_ART = {
    "registration": r_registration, "hypothesis": r_hypothesis, "allocation": r_allocation, "intervention": r_intervention,
    "timeline": r_timeline, "search": r_search, "reflexivity": r_reflexivity, "reference-standard": r_reference_standard,
    "recruitment": r_recruitment, "flow": r_flow, "sample-size": r_sample_size, "saturation": r_saturation,
    "blinding": r_blinding, "instrument": r_instrument, "coding": r_coding, "risk-of-bias": r_risk_of_bias,
    "missing-data": r_missing_data, "sensitivity": r_sensitivity, "confounding": r_confounding, "analysis-set": r_analysis_set,
    "themes": r_themes, "thresholds": r_thresholds, "heterogeneity": r_heterogeneity, "reporting-bias": r_reporting_bias,
}


# --------------------------------------------------------------------------- verdict stamps
def _stamp(label, mark):
    def draw():
        out = f'<g transform="rotate(-8 100 75)">' + rect(34, 44, 132, 62, "none", INK, 4, 8) + rect(40, 50, 120, 50, "none", INK, 1.5, 5)
        return out + text(100, 84, label, 22, INK) + "</g>" + mark
    return draw


VERDICT_ART = {
    "accept": _stamp("ACCEPT", check(160, 36, 12)),
    "minor": _stamp("MINOR", line([(150, 30), (174, 30)], ACC, 3)),
    "major": _stamp("MAJOR", line([(148, 28), (176, 28)], ACC, 3) + line([(148, 36), (170, 36)], ACC, 3)),
    "reject": _stamp("REJECT", cross(164, 32, 9)),
}


# --------------------------------------------------------------------------- study pictures
def s_back():
    out = path("M86,36 Q70,60 84,84 Q96,104 86,124", INK, 4)
    for k in range(5):
        out += rect(78 + (k % 2) * 3, 42 + k * 16, 16, 9, ACC if k == 3 else INK, "none", 0, 3)
    return out + person(146, 84, 1.8, DIM) + arrow(124, 60, 168, 60, ACC, 3)


def s_scroll():
    out = rect(70, 26, 50, 92, PAGE, INK, 3, 8) + circle(150, 46, 14, "none", ACC, 3) + circle(156, 42, 11, "#1c1917", "none")
    for k in range(4):
        out += line([(80, 42 + k * 16), (110, 42 + k * 16)], DIM, 3)
    return out + text(44, 80, "Zz", 18, INK)


def s_pills():
    out = path("M60,110 L84,58 L100,72 L120,40", INK, 4) + cross(84, 58, 6)
    from art import pill
    return out + pill(146, 92, 40, 16, -30) + pill(52, 46, 30, 12, 20)


def s_burnout():
    out = rect(60, 50, 80, 50, "none", INK, 3, 4) + line([(56, 100), (144, 100)], INK, 3)
    out += path("M100,64 C92,76 108,80 100,92 C116,84 112,70 100,64 Z", HOT, 2, fill=HOT)
    return out + doc(146, 30, 26, 34, DIM, 3) + doc(30, 34, 26, 34, DIM, 3)


def s_icu():
    out = rect(40, 80, 120, 18, "none", INK, 3, 4) + circle(60, 74, 8, INK)
    out += line([(130, 30), (130, 80)], DIM, 2.5) + rect(116, 30, 28, 20, "none", DIM, 2, 3)
    return out + path("M40,58 h22 l6,-12 l8,24 l6,-12 h20", ACC, 2.5)


def s_scan():
    out = path("M40,70 A60,60 0 0 1 160,70 L118,122 H82 Z", INK, 3, fill=PAGE)
    return out + circle(100, 94, 8, "none", ACC, 3) + path("M88,94 Q100,80 112,94", DIM, 2)


def s_meta():
    out = ""
    for k, (x, w) in enumerate(((84, 16), (118, 22), (96, 14), (110, 18))):
        out += line([(x - w, 36 + k * 16), (x + w, 36 + k * 16)], INK, 2.5) + rect(x - 3, 33 + k * 16, 6, 6, INK, "none", 0, 1)
    return out + path("M86,112 L106,104 L126,112 L106,120 Z", ACC, 2, fill=ACC) + line([(104, 28), (104, 124)], DIM, 2, "4 4")


def s_mouse():
    out = f'<ellipse cx="96" cy="88" rx="38" ry="22" fill="none" stroke="{INK}" stroke-width="3"/>'
    out += circle(64, 70, 9, "none", INK, 3) + circle(134, 86, 2.5, INK) + path("M58,94 Q30,100 32,120", INK, 2.5)
    return out + path("M144,40 l8,10 l-6,0 l6,12", ACC, 3)


STUDY_ART = {"S1": s_back, "S2": s_scroll, "S3": s_pills, "S4": s_burnout, "S5": s_icu, "S6": s_scan, "S7": s_meta, "S8": s_mouse}
