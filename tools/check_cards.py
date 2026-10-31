#!/usr/bin/env python3
"""Check that no printed card overflows: render every print/<lang>/cards.html at print size in headless Chrome
(or Edge), let the cards shrink their text to fit as they do on paper, and report any card whose text box or
name bar still overflows. Also saves a screenshot of the first sheets for a visual check.

Usage:  python3 tools/check_cards.py            (run python3 tools/build.py first)
Set CHROME=/path/to/chrome if Chrome or Edge is not found. Needs the internet for the card fonts.
"""
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CANDIDATES = [
    os.environ.get("CHROME", ""),
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    shutil.which("google-chrome") or "", shutil.which("chromium") or "", shutil.which("chromium-browser") or "",
]

# Runs after the page's own fitCards: waits for the fonts, fits again, then measures every card.
PROBE = """<script>
(async () => {
  if (document.fonts) await document.fonts.ready;
  fitCards();
  const out = [];
  document.querySelectorAll(".tcg").forEach((c, i) => {
    const code = (c.querySelector(".ft span") || {}).textContent || (c.querySelector(".nm b") || {}).textContent || "card " + i;
    const tb = c.querySelector(".tb"), nm = c.querySelector(".nm b");
    if (tb && tb.scrollHeight > tb.clientHeight + 1) out.push({card: code, part: "text box", over: tb.scrollHeight - tb.clientHeight, fit: tb.style.getPropertyValue("--fit") || "1"});
    if (nm && nm.scrollWidth > nm.clientWidth + 1) out.push({card: code, part: "name", over: nm.scrollWidth - nm.clientWidth});
    // A picture label must lie inside the picture box: a long translation would otherwise be cut off at its edge.
    c.querySelectorAll("svg").forEach(svg => {
      const box = svg.getBoundingClientRect();
      svg.querySelectorAll("text").forEach(t => {
        const r = t.getBoundingClientRect(), over = Math.max(box.left - r.left, r.right - box.right, box.top - r.top, r.bottom - box.bottom);
        if (t.textContent.trim() && over > 1) out.push({card: code, part: `picture label "${t.textContent}"`, over: Math.round(over)});
      });
    });
  });
  const fits = [...document.querySelectorAll(".tcg .tb")].map(t => parseFloat(t.style.getPropertyValue("--fit") || "1"));
  const pre = document.createElement("pre"); pre.id = "probe";
  pre.textContent = JSON.stringify({cards: document.querySelectorAll(".tcg").length, overflow: out,
    fonts: document.fonts ? [...document.fonts].filter(f => f.status === "loaded").map(f => f.family) : [],
    shrunk: fits.filter(f => f < 1).length, smallest: Math.min(...fits)});
  document.body.appendChild(pre);
})();
</script>"""


def chrome():
    for c in CANDIDATES:
        if c and Path(c).exists():
            return c
    sys.exit("Could not find Chrome or Edge. Set CHROME=/path/to/chrome and run again.")


def check(page, exe, shot=None):
    src = page.read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as tmp:
        probe = Path(tmp) / "probe.html"
        probe.write_text(src.replace("</body>", PROBE + "</body>"), encoding="utf-8")
        args = [exe, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=15000",
                f"--user-data-dir={Path(tmp) / 'profile'}"]
        dom = subprocess.run(args + ["--dump-dom", probe.as_uri()], capture_output=True, text=True, encoding="utf-8", timeout=180).stdout
        if shot:
            subprocess.run(args + ["--window-size=1700,2400", f"--screenshot={shot}", probe.as_uri()], capture_output=True, timeout=180)
    m = re.search(r'<pre id="probe">(.*?)</pre>', dom, re.S)
    if not m:
        sys.exit(f"{page}: the probe did not report back (did the page load?)")
    return json.loads(html.unescape(m.group(1)))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")  # picture labels in any language, also on a Windows console
    exe = chrome()
    pages = sorted((ROOT / "print").glob("**/cards.html"))
    if not pages:
        sys.exit("No print/cards.html yet: run python3 tools/build.py first.")
    bad = 0
    for p in pages:
        # Not print/preview.png: that is the README's picture of the cards, drawn by the kit's tools/card_images.py.
        shot = ROOT / "print" / "check.png" if p.parent == ROOT / "print" else None
        r = check(p, exe, shot)
        rel = p.relative_to(ROOT)
        print(f"{rel}: {r['cards']} cards, {r['shrunk']} shrunk to fit (smallest {r['smallest']:.2f}), fonts: {', '.join(sorted(set(r['fonts']))) or 'NONE'}")
        for o in r["overflow"]:
            bad += 1
            print(f"  OVERFLOW {o['card']}: {o['part']} by {o['over']}px" + (f" (fit {o['fit']})" if "fit" in o else ""))
        if not r["fonts"]:
            print("  warning: card fonts did not load, so the check used fallback fonts")
    if bad:
        sys.exit(f"{bad} overflowing card part(s)")
    print("ok: no card overflows")
