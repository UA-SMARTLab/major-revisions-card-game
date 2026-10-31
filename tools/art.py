"""Vector art primitives for Major Revisions cards (shared with Methodical, the first SMART-Lab Science Game Kit game).

Every illustration is drawn in a 200 x 150 art box (viewBox "0 0 200 150") as light line art on the
card's coloured background. Functions return SVG fragments (strings); `frame()` wraps a fragment into a
complete <svg> with the background, so art can be previewed or embedded anywhere.

Style rules (keep new art consistent):
  * main lines and figures in INK, highlights in ACC (amber), "bad"/outcome marks in HOT (rose),
    secondary or background elements in DIM;
  * stroke width 3 for main lines, 2 for detail; round caps and joins;
  * leave ~10 px margin to the art-box edge; one clear idea per picture.
"""
import math

INK = "#F8FAFC"
DIM = "rgba(248,250,252,.38)"
FAINT = "rgba(248,250,252,.16)"
ACC = "#FCD34D"
HOT = "#FB7185"
COOL = "#7DD3FC"


def _f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


# --------------------------------------------------------------------------- primitives
def line(pts, c=INK, w=3, dash=None, fill="none", close=False, o=1):
    d = " ".join(f"{_f(x)},{_f(y)}" for x, y in pts)
    tag = "polygon" if close else "polyline"
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<{tag} points="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" '
            f'stroke-linejoin="round" opacity="{o}"{da}/>')


def path(d, c=INK, w=3, fill="none", dash=None, o=1):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" '
            f'stroke-linejoin="round" opacity="{o}"{da}/>')


def circle(x, y, r, fill=INK, stroke="none", w=2, o=1, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<circle cx="{_f(x)}" cy="{_f(y)}" r="{_f(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{w}" opacity="{o}"{da}/>'


def rect(x, y, w, h, fill="none", stroke=INK, sw=3, rx=3, o=1, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{_f(x)}" y="{_f(y)}" width="{_f(w)}" height="{_f(h)}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}" opacity="{o}"{da}/>')


# Labels drawn inside pictures, translated per language by the build (i18n/<code>/ui.json, "art" section).
TR = {}


def text(x, y, s, size=14, c=INK, anchor="middle", weight=700, family="'Barlow Condensed', 'Arial Narrow', sans-serif", o=1):
    s = TR.get(s, s)
    s = s.replace("&", "&amp;").replace("<", "&lt;")
    return (f'<text x="{_f(x)}" y="{_f(y)}" font-size="{size}" fill="{c}" text-anchor="{anchor}" '
            f'font-weight="{weight}" font-family="{family}" opacity="{o}">{s}</text>')


def arrow(x1, y1, x2, y2, c=INK, w=3, dash=None, head=8, o=1):
    a = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * 0.8 * math.cos(a), y2 - head * 0.8 * math.sin(a)
    p1 = (x2 - head * math.cos(a - 0.45), y2 - head * math.sin(a - 0.45))
    p2 = (x2 - head * math.cos(a + 0.45), y2 - head * math.sin(a + 0.45))
    return (line([(x1, y1), (bx, by)], c, w, dash, o=o)
            + line([p1, (x2, y2), p2], c, w, fill=c, close=True, o=o))


def carrow(x1, y1, cx, cy, x2, y2, c=INK, w=3, dash=None, head=8, o=1):
    """Quadratic curved arrow from (x1,y1) to (x2,y2) bending toward control point (cx,cy)."""
    a = math.atan2(y2 - cy, x2 - cx)
    p1 = (x2 - head * math.cos(a - 0.45), y2 - head * math.sin(a - 0.45))
    p2 = (x2 - head * math.cos(a + 0.45), y2 - head * math.sin(a + 0.45))
    return (path(f"M{_f(x1)},{_f(y1)} Q{_f(cx)},{_f(cy)} {_f(x2)},{_f(y2)}", c, w, dash=dash, o=o)
            + line([p1, (x2, y2), p2], c, w, fill=c, close=True, o=o))


def person(x, y, s=1.0, c=INK, o=1):
    """Pictogram person standing with feet near y + 9s, head centred on x."""
    return (circle(x, y - 9 * s, 4.3 * s, c, o=o)
            + f'<path d="M{_f(x - 7 * s)},{_f(y + 9 * s)} V{_f(y + 2 * s)} Q{_f(x - 7 * s)},{_f(y - 3 * s)} {_f(x)},{_f(y - 3 * s)} '
              f'Q{_f(x + 7 * s)},{_f(y - 3 * s)} {_f(x + 7 * s)},{_f(y + 2 * s)} V{_f(y + 9 * s)} Z" fill="{c}" opacity="{o}"/>')


def crowd(x0, y0, cols, rows, dx=18, dy=24, s=0.8, color=lambda i, j: INK):
    return "".join(person(x0 + i * dx, y0 + j * dy, s, color(i, j)) for j in range(rows) for i in range(cols))


def dice(x, y, size=34, face=5, c=INK, pip="#0f172a", rot=-12):
    h = size / 2
    pos = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)],
           5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)], 6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}[face]
    pips = "".join(circle(x + px * size * 0.27, y + py * size * 0.27, size * 0.085, pip) for px, py in pos)
    return (f'<g transform="rotate({rot} {_f(x)} {_f(y)})">' + rect(x - h, y - h, size, size, c, "none", 0, rx=size * 0.18)
            + pips + "</g>")


def doc(x, y, w=26, h=34, c=INK, lines=3, fill="none", sw=2.5, lc=None):
    fold = w * 0.3
    out = path(f"M{_f(x)},{_f(y)} H{_f(x + w - fold)} L{_f(x + w)},{_f(y + fold)} V{_f(y + h)} H{_f(x)} Z", c, sw, fill=fill)
    out += path(f"M{_f(x + w - fold)},{_f(y)} V{_f(y + fold)} H{_f(x + w)}", c, sw * 0.8)
    for i in range(lines):
        ly = y + fold + 5 + i * (h - fold - 8) / max(lines, 1)
        out += line([(x + 5, ly), (x + w - 5 - (i % 2) * 5, ly)], lc or c, 2)
    return out


def axes(x, y, w, h, c=INK, sw=2.5):
    return arrow(x, y + h, x, y, c, sw, head=6) + arrow(x, y + h, x + w, y + h, c, sw, head=6)


def cylinder(x, y, w=40, h=46, c=INK, fill="none"):
    ry = w * 0.18
    out = path(f"M{_f(x)},{_f(y + ry)} V{_f(y + h - ry)} A{_f(w / 2)},{_f(ry)} 0 0 0 {_f(x + w)},{_f(y + h - ry)} V{_f(y + ry)}", c, 2.5, fill=fill)
    out += f'<ellipse cx="{_f(x + w / 2)}" cy="{_f(y + ry)}" rx="{_f(w / 2)}" ry="{_f(ry)}" fill="{fill}" stroke="{c}" stroke-width="2.5"/>'
    for k in (1, 2):
        yy = y + ry + k * (h - 2 * ry) / 3
        out += path(f"M{_f(x)},{_f(yy)} A{_f(w / 2)},{_f(ry)} 0 0 0 {_f(x + w)},{_f(yy)}", c, 2, o=.7)
    return out


def building(x, y, w=34, h=30, c=INK, fill="none", roof=12):
    return (path(f"M{_f(x)},{_f(y + h)} V{_f(y + roof)} L{_f(x + w / 2)},{_f(y)} L{_f(x + w)},{_f(y + roof)} V{_f(y + h)} Z", c, 2.5, fill=fill))


def magnifier(x, y, r=16, c=INK, w=3.5):
    a = math.radians(45)
    return circle(x, y, r, "none", c, w) + line([(x + r * math.cos(a), y + r * math.sin(a)), (x + r * 2 * math.cos(a), y + r * 2 * math.sin(a))], c, w + 2)


def bubble(x, y, w, h, c=INK, fill="none", tail="left", sw=2.5):
    tx = x + w * 0.25 if tail == "left" else x + w * 0.75
    td = -8 if tail == "left" else 8
    return path(f"M{_f(x + 6)},{_f(y)} H{_f(x + w - 6)} Q{_f(x + w)},{_f(y)} {_f(x + w)},{_f(y + 6)} V{_f(y + h - 6)} "
                f"Q{_f(x + w)},{_f(y + h)} {_f(x + w - 6)},{_f(y + h)} H{_f(tx + 6)} L{_f(tx + td)},{_f(y + h + 9)} L{_f(tx - 2)},{_f(y + h)} "
                f"H{_f(x + 6)} Q{_f(x)},{_f(y + h)} {_f(x)},{_f(y + h - 6)} V{_f(y + 6)} Q{_f(x)},{_f(y)} {_f(x + 6)},{_f(y)} Z", c, sw, fill=fill)


def pill(x, y, w=34, h=14, rot=-25, c1=INK, c2=ACC):
    r = h / 2
    return (f'<g transform="rotate({rot} {_f(x)} {_f(y)})">'
            f'<path d="M{_f(x)},{_f(y - r)} H{_f(x - w / 2 + r)} A{_f(r)},{_f(r)} 0 0 0 {_f(x - w / 2 + r)},{_f(y + r)} H{_f(x)} Z" fill="{c1}"/>'
            f'<path d="M{_f(x)},{_f(y - r)} H{_f(x + w / 2 - r)} A{_f(r)},{_f(r)} 0 0 1 {_f(x + w / 2 - r)},{_f(y + r)} H{_f(x)} Z" fill="{c2}"/></g>')


def star(x, y, r=8, c=ACC, pts=5):
    p = []
    for k in range(pts * 2):
        rr = r if k % 2 == 0 else r * 0.45
        a = -math.pi / 2 + k * math.pi / pts
        p.append((x + rr * math.cos(a), y + rr * math.sin(a)))
    return line(p, c, 1, fill=c, close=True)


def check(x, y, s=10, c="#86EFAC", w=3.5):
    return line([(x - s * 0.6, y), (x - s * 0.15, y + s * 0.5), (x + s * 0.7, y - s * 0.5)], c, w)


def cross(x, y, s=8, c=HOT, w=3.5):
    return line([(x - s, y - s), (x + s, y + s)], c, w) + line([(x - s, y + s), (x + s, y - s)], c, w)


def clock(x, y, r=14, c=INK, h1=-60, h2=60, sw=2.5):
    a1, a2 = math.radians(h1 - 90), math.radians(h2 - 90)
    return (circle(x, y, r, "none", c, sw) + line([(x, y), (x + r * .5 * math.cos(a1), y + r * .5 * math.sin(a1))], c, sw)
            + line([(x, y), (x + r * .75 * math.cos(a2), y + r * .75 * math.sin(a2))], c, sw))


def hourglass(x, y, s=1.0, c=INK, sand=ACC):
    w, h = 14 * s, 20 * s
    return (line([(x - w, y - h), (x + w, y - h)], c, 3) + line([(x - w, y + h), (x + w, y + h)], c, 3)
            + path(f"M{_f(x - w + 2)},{_f(y - h)} Q{_f(x - w + 2)},{_f(y)} {_f(x)},{_f(y)} Q{_f(x - w + 2)},{_f(y)} {_f(x - w + 2)},{_f(y + h)} "
                   f"M{_f(x + w - 2)},{_f(y - h)} Q{_f(x + w - 2)},{_f(y)} {_f(x)},{_f(y)} Q{_f(x + w - 2)},{_f(y)} {_f(x + w - 2)},{_f(y + h)}", c, 2.5)
            + path(f"M{_f(x - w * .55)},{_f(y + h - 1)} Q{_f(x)},{_f(y + h * .35)} {_f(x + w * .55)},{_f(y + h - 1)} Z", sand, 1, fill=sand))


def gear(x, y, r=14, c=INK, teeth=8, fill="none", sw=2.5):
    p = []
    for k in range(teeth * 4):
        a = k * 2 * math.pi / (teeth * 4)
        rr = r if (k % 4) in (0, 1) else r * 0.78
        p.append((x + rr * math.cos(a), y + rr * math.sin(a)))
    return line(p, c, sw, fill=fill, close=True) + circle(x, y, r * 0.32, "none", c, sw)


def flask(x, y, s=1.0, c=INK, liquid=ACC):
    n, b = 6 * s, 20 * s
    top, neck, bot = y - 22 * s, y - 6 * s, y + 18 * s
    return (path(f"M{_f(x - b * .5)},{_f(bot - 10 * s)} L{_f(x - n)},{_f(neck)} V{_f(top)}", c, 0)
            + path(f"M{_f(x - b + 6 * s)},{_f(y + 6 * s)} L{_f(x + b - 6 * s)},{_f(y + 6 * s)} L{_f(x + b)},{_f(bot)} H{_f(x - b)} Z", liquid, 0, fill=liquid, o=.9)
            + path(f"M{_f(x - n)},{_f(top)} V{_f(neck)} L{_f(x - b)},{_f(bot)} H{_f(x + b)} L{_f(x + n)},{_f(neck)} V{_f(top)}", c, 3)
            + line([(x - n - 4 * s, top), (x + n + 4 * s, top)], c, 3))


def eye(x, y, s=1.0, c=INK, pupil=ACC):
    w, h = 22 * s, 12 * s
    return (path(f"M{_f(x - w)},{_f(y)} Q{_f(x)},{_f(y - h * 2)} {_f(x + w)},{_f(y)} Q{_f(x)},{_f(y + h * 2)} {_f(x - w)},{_f(y)} Z", c, 3)
            + circle(x, y, 7 * s, pupil) + circle(x, y, 3 * s, "#0f172a"))


def globe(x, y, r=22, c=INK):
    return (circle(x, y, r, "none", c, 3) + f'<ellipse cx="{_f(x)}" cy="{_f(y)}" rx="{_f(r * .45)}" ry="{_f(r)}" fill="none" stroke="{c}" stroke-width="2"/>'
            + line([(x - r, y), (x + r, y)], c, 2) + path(f"M{_f(x - r * .87)},{_f(y - r * .5)} Q{_f(x)},{_f(y - r * .3)} {_f(x + r * .87)},{_f(y - r * .5)}", c, 2)
            + path(f"M{_f(x - r * .87)},{_f(y + r * .5)} Q{_f(x)},{_f(y + r * .7)} {_f(x + r * .87)},{_f(y + r * .5)}", c, 2))


def bolt(x, y, s=1.0, c=ACC):
    return line([(x + 3 * s, y - 16 * s), (x - 7 * s, y + 2 * s), (x, y + 2 * s), (x - 4 * s, y + 16 * s), (x + 8 * s, y - 3 * s), (x + 1 * s, y - 3 * s)], c, 1.5, fill=c, close=True)


def helix(x0, y0, x1, h=18, turns=3, c1=INK, c2=ACC):
    n = 60
    out1, out2, rungs = [], [], ""
    for k in range(n + 1):
        t = k / n
        xx = x0 + (x1 - x0) * t
        ph = t * turns * 2 * math.pi
        out1.append((xx, y0 + h * math.sin(ph)))
        out2.append((xx, y0 - h * math.sin(ph)))
        if k % 4 == 2:
            rungs += line([(xx, y0 + h * math.sin(ph)), (xx, y0 - h * math.sin(ph))], DIM, 2)
    return rungs + line(out1, c1, 3) + line(out2, c2, 3)


def node(x, y, label, r=13, fill="none", c=INK, tc=None, size=14):
    return circle(x, y, r, fill, c, 2.5) + text(x, y + size * 0.36, label, size, tc or c)


def scatter(points, r=2.6, c=INK, o=1):
    return "".join(circle(x, y, r, c, o=o) for x, y in points)


def lcg(seed):
    """Tiny deterministic random generator, so art is identical on every build."""
    state = [seed]

    def rnd():
        state[0] = (state[0] * 1103515245 + 12345) % 2 ** 31
        return state[0] / 2 ** 31
    return rnd


# --------------------------------------------------------------------------- frame
def frame(inner, uid, c1="#334155", c2="#0f172a", pattern=True, vb="0 0 200 150"):
    """Wrap art into a full SVG with a two-tone gradient background and a faint blueprint dot grid."""
    pat = (f'<pattern id="d{uid}" width="10" height="10" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".9" fill="#fff" opacity=".13"/></pattern>'
           if pattern else "")
    return (f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" role="img">'
            f'<defs><linearGradient id="g{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>{pat}'
            f'<radialGradient id="r{uid}" cx=".5" cy=".42" r=".65"><stop offset="0" stop-color="#fff" stop-opacity=".18"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient></defs>'
            f'<rect width="100%" height="100%" fill="url(#g{uid})"/>'
            + (f'<rect width="100%" height="100%" fill="url(#d{uid})"/>' if pattern else "")
            + f'<rect width="100%" height="100%" fill="url(#r{uid})"/>{inner}</svg>')


def shade(hex_color, f):
    """Mix a hex colour toward black (f<0) or white (f>0)."""
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    t = 255 if f > 0 else 0
    f = abs(f)
    return "#%02x%02x%02x" % tuple(round(v + (t - v) * f) for v in (r, g, b))


# --------------------------------------------------------------------------- small icons (24x24, currentColor)
def _icon(body):
    return (f'<svg viewBox="0 0 24 24" class="ic" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')
