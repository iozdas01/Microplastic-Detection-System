"""Render the inbound demand map — where "make me this" demand actually arrives.

Answers one question the founder asked directly: if we put up a website and manufacture
what people ask for, which category brings the most people to it?

Everything is computed from data/processed/demand_sweep_ranking.csv and
demand_sweep_families.csv. Change the sweep, re-run, and this page rewrites itself.
"""
from __future__ import annotations

import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import PAGES, ROOT, TODAY, log, read_csv  # noqa: E402
from page_kit import Raw, bar_cell, esc, note, stat, table  # noqa: E402

HERE = __import__("pathlib").Path(__file__).parent
OUT = PAGES / "inbound-demand-map.html"
MONTHS = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

FAMILY_LABEL = {
    "sign_display": "Signs & display",
    "wood_panel": "Cabinets, closets & built-ins",
    "auto_moto": "Automotive & powersports",
    "trailer_equip": "Trailers & truck equipment",
    "additive": "3D printing services",
    "plastics": "Plastics & acrylic",
    "metal_fab": "Metal fabrication",
    "machining": "Machining",
    "stone_surface": "Stone & surfaces",
    "industrial": "Industrial hardware",
    "cutting": "Laser & waterjet cutting",
    "parts_repair": "Blocked & obsolete parts",
    "soft_goods_cal": "Soft goods (calibration)",
    "anchor": "Anchor term",
}


def pretty_date():
    y, mo, dd = (int(x) for x in TODAY.split("-"))
    return f"{dd} {MONTHS[mo]} {y}"


def fnum(v, dp=3, dash="—"):
    try:
        return f"{float(v):.{dp}f}"
    except (TypeError, ValueError):
        return dash


def fpct(v, dash="—"):
    try:
        return f"{float(v) * 100:.0f}%"
    except (TypeError, ValueError):
        return dash


def main() -> None:
    rank = read_csv("demand_sweep_ranking")
    fams = read_csv("demand_sweep_families")
    if not rank:
        log("build_demand_map_page: run analyse_demand_sweep.py first")
        return

    def istrue(v):
        return str(v).lower() == "true"

    # The anchor is a scale reference, not a swept category — counting it as one made the
    # lede and the stat tiles disagree.
    rank = [r for r in rank if r["family"] != "anchor"]
    measured = [r for r in rank if r["verdict"] == "measured"]
    contaminated = [r for r in rank if r["verdict"] == "contaminated"]
    unmeasured = [r for r in rank if r["verdict"] == "unmeasured"]
    real_fams = [f for f in fams
                 if not istrue(f["calibration_only"]) and float(f["family_adjusted"]) > 0]
    top = real_fams[0] if real_fams else None

    # The commercial-intent inversion is the finding that changes what to build, so it is
    # computed rather than asserted: the terms with the highest buying intent are the ones
    # with the least volume.
    intent = [r for r in rank if r["commercial_share"] not in ("", None)]
    high_intent = sorted(intent, key=lambda r: -float(r["commercial_share"]))
    hi_thin = [r for r in high_intent
               if float(r["commercial_share"]) >= 0.7 and r["verdict"] == "unmeasured"]

    L: list[str] = []
    Add = L.append

    Add(f"""
  <header>
    <h1>Where "make me this" demand actually arrives</h1>
    <p class="lede">{len(rank)} search terms across every machinable material, anchored on
    a single term so they are comparable to each other, then discounted by how much of each
    term means something other than manufacturing. United States, five years, to
    {esc(pretty_date())}.</p>
  </header>

  <div class="stats">
    {stat(FAMILY_LABEL.get(top["family"], top["family"]) if top else "—",
          "Largest measurable family",
          f'{fnum(top["family_adjusted"]) if top else "—"}× the anchor, adjusted')}
    {stat(str(len(measured)), "Terms that measured anything",
          f"of {len(rank)} swept — {len(unmeasured)} sat at the resolution floor")}
    {stat(f"{len([r for r in measured if r['family'] == 'parts_repair'])} of "
          f"{len([r for r in rank if r['family'] == 'parts_repair'])}",
          "Blocked-part terms measurable",
          "the lane H2 is testing has no inbound web demand", negative=True)}
  </div>

  <h2>The instrument, and what it cannot see</h2>

  <p>Google Trends returns an integer 0-100 index scaled to the largest term in each batch.
  Query five terms of wildly different size together and the small ones quantise to zero —
  not because they are small, but because the instrument has run out of resolution. So every
  batch here carries the same anchor, <b>"custom furniture"</b>, and every term is reported
  as a ratio to it. Any term sitting at or below 1 for more than half the weeks is marked
  <b>unmeasured</b> rather than ranked, because a series that is mostly zeros has no
  recoverable ordering.</p>

  <p><b>This measures arrival by search, and nothing else.</b> A maintenance engineer whose
  production line is down does not open Google and type "cnc machining service" — they phone
  a shop they already use, or they email the OEM. A zero here is evidence that a category
  does not arrive through a search box. It is <i>not</i> evidence that the pain is absent,
  and reading it that way would be the single biggest mistake available on this page.</p>
""")

    frows = []
    fmax = max((float(f["family_adjusted"]) for f in fams), default=1.0) or 1.0
    for f in fams:
        if istrue(f["calibration_only"]):
            label = FAMILY_LABEL.get(f["family"], f["family"]) + " — calibration only"
        elif f["family"] == "anchor":
            continue
        else:
            label = FAMILY_LABEL.get(f["family"], f["family"])
        adj = float(f["family_adjusted"])
        frows.append([
            label,
            Raw(f'{bar_cell(adj / fmax)} {fnum(adj)}'),
            f'{f["terms_measured"]} of {f["terms_swept"]}',
            f["buyer_mix"],
            f["best_term"],
        ])

    Add(f"""
  <h2>Families, ranked</h2>

  {table("Adjusted demand by family — measured terms only, anchor = 1.000",
         ["Family", "Adjusted", "Terms measured", "Buyer", "Entry term"], frows,
         # `.num` sets padding-right:0, so a num column must never be followed by a
         # text one — it renders as "4 of 4consumer/mixed". The num columns in the term
         # tables below are contiguous and last, which is why only this table is affected.
         aligns=["wrap", "", "", "", "wrap"],
         row_classes=["lead"] + [None] * (len(frows) - 1))}

  <p>Soft goods are in the table but excluded from the ranking. They are not machinable and
  are carried only as calibration: a category known to sustain real made-to-order web
  businesses, so the machinable families can be read against something whose demand is
  proven rather than against zero.</p>
""")

    def term_rows(rows):
        out = []
        for r in rows:
            out.append([
                r["keyword"],
                FAMILY_LABEL.get(r["family"], r["family"]),
                r["buyer"],
                fnum(r["raw_vs_anchor"], 2),
                fnum(r["adjusted_vs_anchor"]),
                fpct(r["on_topic_share"]),
                fpct(r["commercial_share"]),
                fpct(r["momentum_yoy"]),
            ])
        return out

    Add(f"""
  <h2>Terms that measured something</h2>

  {table("Measured terms — adjusted for contamination",
         ["Term", "Family", "Buyer", "Raw", "Adjusted", "On-topic",
          "Buying intent", "YoY"],
         term_rows(measured),
         aligns=["wrap", "wrap", "", "num", "num", "num", "num", "num"],
         row_classes=["lead"] + [None] * (len(measured) - 1))}

  <p><b>On-topic</b> is the share of a term's own related queries that are actually about
  having something made. It is the correction that matters most, because two terms near the
  top of the raw index are not what they appear to be.</p>
""")

    crows = term_rows(contaminated)
    Add(f"""
  <h2>What the raw index got wrong</h2>

  <p><b>"custom wheels"</b> looked like the second-largest category in the whole sweep at
  1.52× the anchor. Its top related queries are <span class="mono">hot wheels custom
  wheels</span> — a die-cast toy — and <span class="mono">rimtyme custom wheels and
  tires</span>, a tire retail chain. Half the term is not manufacturing demand.</p>

  <p><b>"machine shop near me"</b> looked like the strongest trade term at 0.46×. Its
  related queries are <span class="mono">sewing machine shop near me</span>,
  <span class="mono">washing machine shop near me</span> and <span class="mono">diesel
  machine shop near me</span>. Three quarters of it is appliance and engine repair. The
  machining share is a minority of a term that was never large.</p>

  {table("Terms discounted below half their raw value",
         ["Term", "Family", "Buyer", "Raw", "Adjusted", "On-topic",
          "Buying intent", "YoY"], crows,
         aligns=["wrap", "wrap", "", "num", "num", "num", "num", "num"])
     if crows else ""}
""")

    hirows = [[r["keyword"], FAMILY_LABEL.get(r["family"], r["family"]), r["buyer"],
               fnum(r["adjusted_vs_anchor"]), fpct(r["commercial_share"]),
               r["verdict"]] for r in hi_thin]

    Add(f"""
  <h2>The inversion: intent runs opposite to volume</h2>

  <p>The trade terms are tiny and almost every searcher is a buyer. The consumer terms are
  large and most searchers are browsing. <span class="mono">custom signs</span> is the
  biggest measured term on the page and only 21% of its related queries carry buying
  intent. <span class="mono">waterjet cutting service</span> is the smallest term in the
  entire sweep and 100% of its related queries do.</p>

  {table("High buying intent, below the resolution floor",
         ["Term", "Family", "Buyer", "Adjusted", "Verdict", "Buying intent"],
         [[r[0], r[1], r[2], r[3], r[5], r[4]] for r in hirows],
         aligns=["wrap", "wrap", "", "", "", "num"])
     if hirows else ""}

  <p>These are not small markets — machining and fabrication are enormous industries. They
  are markets that <b>do not arrive through a search box</b>, which is a statement about
  channel, not about size. A website is the wrong instrument to catch them with.</p>
""")

    urows = term_rows(unmeasured)
    Add(f"""
  <h2>Below the floor</h2>

  <p>Reported, not ranked. Momentum figures on these rows are computed against a baseline
  near zero and are noise — a term moving from 0.02 to 0.7 reads as +3450% and means
  nothing.</p>

  {table("Terms that did not resolve",
         ["Term", "Family", "Buyer", "Raw", "Adjusted", "On-topic",
          "Buying intent", "YoY"], urows,
         aligns=["wrap", "wrap", "", "num", "num", "num", "num", "num"])}

  <p class="note">Source — Google Trends, United States, five years, collected by
  scripts/research/t1_demand_sweep.py and scored by scripts/research/analyse_demand_sweep.py.
  The off-topic vocabulary used for the contamination discount is declared in that second
  file and is auditable line by line. Compiled {esc(pretty_date())}.</p>

  <footer>
    <p class="note">Generated by scripts/research/build_demand_map_page.py from
    data/processed/demand_sweep_ranking.csv and demand_sweep_families.csv. Re-run the sweep
    and this page rewrites itself.</p>
  </footer>""")

    head = (HERE / "page.head.demand.html").read_text().strip()
    css = (HERE / "page.css").read_text().strip()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(f"{head}\n\n<style>\n{css}\n</style>\n\n"
                   f'<div class="page flow">\n' + "\n".join(L) + "\n\n</div>\n")
    log(f"  {OUT.relative_to(ROOT)} written ({len(OUT.read_text()):,} bytes)")


if __name__ == "__main__":
    main()
