"""Where the window-covering companies the founder has actually spoken to physically are.

Replaces call-log.html, which was a blank notes template and held no company data at all.

The point of putting them on a map rather than in a list: the three with a San Francisco
street address sit on three DIFFERENT layers of the trade — a 1934 independent, a designer's
workroom, and a national's appointment-only suite — and they are within four miles of each
other. That is a one-day driving loop covering three layers, which a list does not show you.

Companies, addresses, coordinates and layer assignment are authored in outreach/companies.md.
What each layer MEANS is authored in build_players_page.py. This file owns neither; it only
projects one onto a map.

    .venv/bin/python scripts/research/build_field_map_page.py
"""
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLUG = "high-mix-manufacturing"
SRC = ROOT / f"reports/{SLUG}/outreach/companies.md"
OUT = ROOT / f"reports/{SLUG}/pages/field-map.html"

# Layer names are a short label for the map only. build_players_page.py is the author of what
# each layer is; anything longer than a label belongs there, not here.
LAYER_LABEL = {
    "1": "Workroom that fabricates",
    "2": "Authorised independent dealer",
    "3": "Franchise network",
    "4": "Vertically integrated national",
    "5": "Big box",
    "6": "Online, customer self-measures",
    "7": "Manufacturer",
    "unpinned": "Not yet identified",
}
LAYER_COLOR = {
    "1": "#1f6f4f", "2": "#2f7fa8", "3": "#7a4fa0", "4": "#a8571e",
    "5": "#8a6a12", "6": "#a03050", "7": "#4a5568", "unpinned": "#8b8792",
}

# Stylised San Francisco coastline, (lon, lat), traced coarsely from the city outline.
# Schematic — good enough to locate a pin by neighbourhood, not a survey.
SF = [
    (-122.478, 37.810), (-122.445, 37.807), (-122.420, 37.808), (-122.400, 37.808),
    (-122.393, 37.800), (-122.386, 37.790), (-122.387, 37.782), (-122.390, 37.776),
    (-122.385, 37.770), (-122.377, 37.762), (-122.383, 37.750), (-122.395, 37.735),
    (-122.405, 37.708), (-122.470, 37.708), (-122.505, 37.708), (-122.510, 37.735),
    (-122.512, 37.770), (-122.510, 37.790), (-122.492, 37.805),
]
LON0, LON1 = -122.525, -122.370
LAT0, LAT1 = 37.700, 37.820
W, H = 660, 645
PAD_R = 230  # room for labels to the right of the easternmost pin, so none is clipped

# Neighbourhood ticks, purely so a pin is placeable by eye.
MARKS = [
    (-122.4194, 37.7749, "Civic Center"),
    (-122.4064, 37.7946, "Financial District"),
    (-122.4148, 37.7599, "Mission"),
    (-122.4477, 37.7694, "Haight"),
    (-122.3893, 37.7749, "Mission Bay"),
    (-122.4830, 37.7694, "Sunset"),
]


def px(lon: float, lat: float) -> tuple[float, float]:
    return ((lon - LON0) / (LON1 - LON0) * W, (LAT1 - lat) / (LAT1 - LAT0) * H)


def parse(md: str) -> list[dict]:
    out = []
    for block in re.split(r"\n## ", md)[1:]:
        lines = block.split("\n")
        rec: dict[str, str] = {"heading": lines[0].strip()}
        for ln in lines[1:]:
            m = re.match(r"^([a-z_]+): *(.*)$", ln)
            if m and m.group(2) not in (">", ">-"):
                rec[m.group(1)] = m.group(2).strip().strip('"')
        if rec.get("window_layer"):
            out.append(rec)
    return out


def esc(x) -> str:
    return html.escape(str(x or ""))


def tag(layer: str) -> str:
    """Layer chip. `unpinned` is not a number, so it must not render as "Lunpinned"."""
    return "Unpinned" if layer == "unpinned" else f"L{esc(layer)}"


def build() -> Path:
    cos = parse(SRC.read_text(encoding="utf-8"))
    mapped = [c for c in cos if c.get("geo_status") == "mapped"]
    offmap = [c for c in cos if c.get("geo_status") != "mapped"]
    mapped.sort(key=lambda c: c.get("window_layer", ""))

    pins, cards = [], []
    # Labels are placed away from the map's right edge and nudged apart when two pins sit
    # close together — Art Shade Shop and the Natoma workroom are under a mile apart and
    # their labels collided at the first render.
    placed: list[tuple[float, float]] = []
    for i, c in enumerate(mapped, 1):
        x, y = px(float(c["lon"]), float(c["lat"]))
        col = LAYER_COLOR.get(c["window_layer"], "#888")
        left = x > W * 0.88                      # flip inward only at the far edge
        ly = y + 4
        while any(abs(ly - py_) < 19 and abs(x - px_) < 210 for px_, py_ in placed):
            ly += 20
        placed.append((x, ly))
        pins.append(
            f'<g><circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="{col}" fill-opacity=".16"/>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6.5" fill="{col}" stroke="var(--card)" '
            f'stroke-width="2"/><text x="{x:.1f}" y="{y+3.4:.1f}" text-anchor="middle" '
            f'font-size="8.5" font-weight="700" fill="#fff">{i}</text></g>'
        )
        if abs(ly - (y + 4)) > 2:                # leader line to a nudged label
            lx = x - 16 if left else x + 16
            pins.append(f'<path d="M{x:.1f},{y+7:.1f} L{lx:.1f},{ly-4:.1f}" stroke="{col}" '
                        f'stroke-width="1" fill="none" stroke-opacity=".55"/>')
        pins.append(
            f'<text x="{(x-16) if left else (x+16):.1f}" y="{ly:.1f}" '
            f'text-anchor="{"end" if left else "start"}" font-size="11.5" font-weight="600" '
            f'fill="var(--fg)">{esc(c["canonical_name"] or c["heading"])}</text>'
        )

    for i, c in enumerate(mapped + offmap, 1):
        L = c["window_layer"]
        col = LAYER_COLOR.get(L, "#888")
        name = c["canonical_name"] or c["heading"]
        addr = c.get("address") or "&mdash; no address established"
        ev = esc(c.get("known_contacts", "")).strip("[]")
        off = c.get("geo_status") != "mapped"
        cards.append(f"""<div class="co{' off' if off else ''}">
  <div class="con"><span class="num" style="background:{col}">{i}</span>
    <span class="nm">{esc(name)}</span>
    <span class="lay" style="color:{col};border-color:{col}">{tag(L)} &middot; {esc(LAYER_LABEL.get(L,''))}</span></div>
  <div class="addr">{esc(addr) if addr.startswith('&') is False else addr}</div>
  <div class="ev">{('evidence ' + ev) if ev else 'no ledger entry'}</div>
</div>""")

    marks = "".join(
        f'<circle cx="{px(lo,la)[0]:.1f}" cy="{px(lo,la)[1]:.1f}" r="1.8" fill="var(--faint)"/>'
        f'<text x="{px(lo,la)[0]+5:.1f}" y="{px(lo,la)[1]+3:.1f}" font-size="9.5" '
        f'fill="var(--faint)">{esc(n)}</text>'
        for lo, la, n in MARKS
    )
    poly = " ".join(f"{px(lo,la)[0]:.1f},{px(lo,la)[1]:.1f}" for lo, la in SF)
    legend = "".join(
        f'<li><span class="sw" style="background:{LAYER_COLOR[k]}"></span>{tag(k)} &middot; {v}</li>'
        for k, v in LAYER_LABEL.items()
        if any(c["window_layer"] == k for c in cos)
    )

    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Who We Have Actually Spoken To</title><style>
:root{{--bg:#fbfaf8;--fg:#17161a;--mut:#6d6a73;--faint:#9b98a2;--line:#e6e2dc;--card:#fff;
--water:#eef2f5;--land:#f6f4f0}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--fg);
font:16px/1.62 ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:880px;margin:0 auto;padding:64px 24px 110px}}
h1{{font-size:31px;letter-spacing:-.025em;margin:0 0 10px;font-weight:650}}
.dek{{color:var(--mut);margin:0 0 8px;max-width:62ch}}
.gen{{color:var(--faint);font-size:12.5px;margin:0 0 46px}}
h2{{font-size:12px;text-transform:uppercase;letter-spacing:.12em;color:var(--mut);
font-weight:650;margin:0 0 14px}}
.sec{{margin:0 0 56px}}
.mapbox{{background:var(--card);border:1px solid var(--line);border-radius:12px;
padding:16px;overflow-x:auto}}
svg{{display:block;min-width:700px}}
ul.leg{{list-style:none;display:flex;flex-wrap:wrap;gap:8px 22px;padding:0;margin:16px 0 0;
font-size:13px;color:var(--mut)}}
ul.leg li{{display:flex;align-items:center;gap:7px}}
.sw{{width:11px;height:11px;border-radius:3px;flex:none}}
.co{{background:var(--card);border:1px solid var(--line);border-radius:10px;
padding:14px 16px;margin-bottom:9px}}
.co.off{{background:transparent;border-style:dashed}}
.con{{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:5px}}
.num{{width:20px;height:20px;border-radius:5px;color:#fff;font-size:11px;font-weight:700;
display:grid;place-items:center;flex:none}}
.nm{{font-weight:650;font-size:16px}}
.lay{{font-size:10.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;
border:1px solid;border-radius:5px;padding:2px 7px}}
.addr{{font-size:14px;color:var(--mut)}}
.ev{{font-size:12px;color:var(--faint);font-family:ui-monospace,Menlo,monospace;margin-top:3px}}
.lede{{font-size:17.5px;line-height:1.55;margin:0 0 22px;max-width:64ch}}
.hint{{color:var(--faint);font-size:13.5px;margin-top:12px;max-width:64ch}}
b{{font-weight:650}}
@media(prefers-color-scheme:dark){{
:root{{--bg:#141317;--fg:#eceaf0;--mut:#9d99a6;--faint:#6f6b77;--line:#2c2933;--card:#1c1b21;
--water:#191c21;--land:#22212a}}}}
</style></head><body><div class="wrap">

<h1>Everyone we have spoken to, and where they are</h1>
<p class="dek">The five window-covering companies behind the H3 evidence, placed by layer.
Three have a San Francisco street address and sit on three different layers of the trade,
within about four miles of each other.</p>
<p class="gen">Generated from outreach/companies.md by scripts/research/build_field_map_page.py
&mdash; do not edit this file. Coordinates are approximate, derived from public addresses for
plotting only; none has been verified by visiting.</p>

<div class="sec">
<div class="mapbox">
<svg viewBox="0 0 {W + PAD_R} {H}" width="100%" role="img"
 aria-label="Schematic map of San Francisco with the window-covering companies spoken to, marked by layer.">
 <rect x="0" y="0" width="{W + PAD_R}" height="{H}" fill="var(--water)"/>
 <polygon points="{poly}" fill="var(--land)" stroke="var(--line)" stroke-width="1.5"/>
 {marks}
 {"".join(pins)}
</svg>
<ul class="leg">{legend}</ul>
</div>
<p class="hint">The layers are the seven declared in window-covering-players.html. Colour is
the layer, not the strength of the relationship.</p>
</div>

<div class="sec">
<h2>The companies</h2>
{"".join(cards)}
<p class="hint">Dashed = cannot be placed. Blinds.com is run from Houston but services San
Francisco and Oakland with its own technicians, which is where the in-person evidence came
from. The $225 company was recorded in the founder's notes only as "the national blinds guys"
and has never been identified &mdash; it carries the sharpest number in the thesis.</p>
</div>

<div class="sec">
<h2>What the map is for</h2>
<p class="lede">Three layers of the same trade, four miles apart, all walkable in a day:
a <b>1934 independent</b> on 14th Street, a <b>designer's workroom</b> on Natoma, and a
<b>national's appointment-only suite</b> on California Street. Each carries the same failure
on a completely different P&amp;L.</p>
<p class="hint">Two gaps are visible rather than hidden. Art Shade Shop's layer is a guess
&mdash; whether they fabricate in-house or only sell and fit decides layer 1 versus layer 2,
and it is answerable by walking in. And no franchise network, big box or manufacturer has been
reached at all, which is layers 3, 5 and 7 empty.</p>
</div>

</div></body></html>"""
    OUT.write_text(doc, encoding="utf-8")
    return OUT


if __name__ == "__main__":
    print(f"wrote {build().relative_to(ROOT)}")
