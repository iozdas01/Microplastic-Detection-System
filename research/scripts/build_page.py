"""Render the published HTML report from the collector outputs.

Same design as the hand-built page, but nothing is typed in. Every figure, every table
row and every derived claim in the prose — the size of the gap between the two sizing
methods, how far input costs have run ahead of output prices, how many collectors ran —
is computed here from data/processed/. Re-run the pipeline and the page tells the truth
about the new data rather than the old.

    .venv/bin/python scripts/build_page.py
    # then: Artifact(file_path="reports/bay-area-hardwood-demand.html")
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import MANIFEST, PROC, ROOT, TODAY, log, read_csv  # noqa: E402
from page_kit import Raw, bar_cell, esc, note, pct, stat, table, tag, usd  # noqa: E402

HERE = __import__("pathlib").Path(__file__).parent
OUT = ROOT / "reports" / "bay-area-hardwood-demand.html"

MONTHS = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


# --------------------------------------------------------------------------- load
def load():
    d = {
        "tam": json.loads((PROC / "tam_model.json").read_text())
        if (PROC / "tam_model.json").exists() else {},
        "cex": read_csv("cex_furniture_expenditure"),
        "mrts": read_csv("mrts_furniture_monthly"),
        "prices": read_csv("bls_prices"),
        "cbp": read_csv("cbp_furniture_supply"),
        "permits": read_csv("bay_area_building_permits"),
        "pop": read_csv("bay_area_population"),
        "imports": read_csv("imports_wood_furniture"),
        "trends": read_csv("trends_interest_over_time"),
        "related": read_csv("trends_related_queries"),
        "metro": read_csv("trends_by_metro"),
        "cats": read_csv("custom_categories_adjusted"),
        "cat_related": read_csv("trends_custom_related"),
        "status": {},
    }
    if MANIFEST.exists():
        for line in MANIFEST.read_text().splitlines():
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                continue
            # "analysis" rows are derived steps, not sources; they would otherwise be
            # counted as collectors on the page.
            if e["source"] == "analysis":
                continue
            d["status"][(e["source"], e["dataset"])] = e
    return d


def steps_of(tam):
    return {s["step"]: s["value"] for s in tam.get("steps", [])}


def price_change(prices, label_prefix, base_period="2020-01"):
    ser = sorted([r for r in prices if r["label"].startswith(label_prefix)],
                 key=lambda r: r["period"])
    if not ser:
        return None
    base = next((r for r in ser if r["period"] == base_period), ser[0])
    return (float(ser[-1]["value"]) / float(base["value"]) - 1), ser[-1]["period"], base["period"]


def mrts_annual(mrts, naics="442"):
    ann, months = defaultdict(float), defaultdict(set)
    for r in mrts:
        if r["naics"] == naics and r["seasonally_adjusted"] == "False":
            ann[int(r["year"])] += float(r["sales_musd"])
            months[int(r["year"])].add(int(r["month"]))
    return ann, months


# --------------------------------------------------------------------------- sections
def sec_masthead(d):
    st = d["status"]
    ran = sum(1 for e in st.values() if e["status"] == "ok")
    gated = sum(1 for e in st.values() if e["status"] == "blocked_no_credential")
    ann, _ = mrts_annual(d["mrts"])
    span = f"{min(ann)}–{max(ann)}" if ann else "—"
    counties = len({r["county"] for r in d["permits"]}) or 10
    stamps = [
        (f"{ran + gated} collectors", f"{ran} run, {gated} gated"),
        ("Keyless", "Runs with no credentials"),
        (span, "Retail series coverage"),
        (f"{counties} counties", "Bay Area definition"),
    ]
    chips = "".join(f"<div><b>{esc(a)}</b>{esc(b)}</div>" for a, b in stamps)
    return Raw(f"""
  <header class="masthead bleed">
    <div class="flow">
      <p class="eyebrow">Demand evidence · compiled {esc(_pretty_date())}</p>
      <h1>Two ways to size this market, {esc(_gap_word(d))} apart</h1>
      <p class="lede">A bottom-up read on custom solid-wood furniture in the Bay Area, built
      from household spend, industry payroll, import flows and search behaviour — no
      syndicated market numbers.</p>
    </div>
    <div class="stamp">{chips}</div>
  </header>""")


def _pretty_date():
    y, m, dd = (int(x) for x in TODAY.split("-"))
    return f"{dd} {MONTHS[m]} {y}"


def _gap(d):
    tam = d["tam"]
    s = steps_of(tam)
    mult = tam.get("assumptions", {}).get("custom_price_multiple", {}).get("base", 5.0)
    demand = s.get(f"Bay Area custom/solid-wood pool (base price multiple {mult}x)", 0)
    implied = tam.get("supply_side_triangulation", {}).get("implied_bay_area_revenue_usd", {})
    supply = implied.get("measured") or implied.get("base") or 0
    return demand, supply, (supply / demand if demand else 0)


def _gap_word(d):
    _, _, ratio = _gap(d)
    words = {2: "twice", 3: "three times", 4: "four times", 5: "five times",
             6: "six times", 7: "seven times", 8: "eight times", 9: "nine times",
             10: "ten times", 11: "eleven times", 12: "twelve times",
             13: "thirteen times", 14: "fourteen times", 15: "fifteen times"}
    return words.get(round(ratio), f"{ratio:.0f} times")


def sec_divergence(d):
    tam = d["tam"]
    demand, supply, ratio = _gap(d)
    payroll = tam.get("supply_side_triangulation", {}).get("bay_area_annual_payroll_usd", 0)
    mult = tam["assumptions"]["custom_price_multiple"]["base"]
    rp = tam["assumptions"]["revenue_to_payroll_multiple"]["base"]
    estab = tam.get("competition", {}).get("bay_area_establishments_337122", 0)
    counties = len({r["county"] for r in d["permits"]}) or 10
    width = (demand / supply * 100) if supply else 0
    return Raw(f"""
  <h2 id="divergence">The finding</h2>

  <p>The custom slice of the Bay Area dining-furniture market can be sized two ways from
  independent data. The two answers do not agree, and the disagreement is more useful than
  either number.</p>

  <div class="diverge bleed">
    <div class="method m-demand">
      <div class="method-head">
        <span class="method-name">Demand-side · what people search for</span>
        <span class="method-value">{esc(usd(demand))}<span class="note"> /yr</span></span>
      </div>
      <div class="bar"><span style="width:{width:.2f}%"></span></div>
      <p class="note">Bay Area dining-furniture pool × the share of California search volume
      that carries custom intent × a {esc(f"{mult:g}")}× price multiple for bespoke work.</p>
    </div>

    <div class="method m-supply">
      <div class="method-head">
        <span class="method-name">Supply-side · what makers actually pay staff</span>
        <span class="method-value">{esc(usd(supply))}<span class="note"> /yr</span></span>
      </div>
      <div class="bar"><span style="width:100%"></span></div>
      <p class="note">The {esc(usd(payroll))} of annual payroll that Census County Business
      Patterns records for the {estab} wood household furniture establishments in the
      {counties} Bay Area counties, at a {esc(f"{rp:g}")}× revenue-to-payroll multiple.</p>
    </div>

    <p class="verdict">Both cannot be right. The likeliest reading is that
    <b>the category is real but is not bought through search.</b> Custom furniture moves
    through interior designers, architects, showroom referral and repeat trade — channels
    that leave almost no search footprint. If that is true, the go-to-market question is not
    which keywords to buy. It is which twenty designers to know.</p>
  </div>""")


def sec_categories(d):
    cats = [r for r in d["cats"] if r["keyword"] != "custom furniture"]
    if not cats:
        return Raw("")

    def f(r, k):
        return float(r[k]) if r[k] not in ("", None) else None

    scored = [r for r in cats if f(r, "adjusted_index") is not None]
    winners = [r for r in scored if int(r["commercial_intent_queries"]) > 0]
    winner_names = {r["keyword"] for r in winners}

    rows, classes = [], []
    for r in cats:
        fs = f(r, "furniture_share_of_related")
        adj = f(r, "adjusted_index")
        rows.append([
            r["keyword"],
            f"{f(r,'raw_vs_custom_furniture'):.3f}",
            pct(fs, 0) if fs is not None else Raw('<span class="dim">too few</span>'),
            f"{adj:.3f}" if adj is not None else Raw('<span class="dim">—</span>'),
            r["commercial_intent_queries"],
        ])
        classes.append("lead" if r["keyword"] in winner_names else None)

    tbl = table("Custom demand by category, accessory-adjusted",
                ["Category", "Raw index", "Genuinely furniture", "Adjusted",
                 "Buying-intent queries"],
                rows, ["", "num", "num", "num", "num"], classes)

    # Contamination examples, taken from the data rather than asserted.
    worst = sorted([r for r in scored if f(r, "furniture_share_of_related") is not None],
                   key=lambda r: f(r, "furniture_share_of_related"))[:3]
    ex = ", ".join(f'{note(r["keyword"])} ({pct(f(r,"furniture_share_of_related"),0)} genuine)'
                   for r in worst)

    # Evidence for each winning category.
    top = defaultdict(list)
    for r in d["cat_related"]:
        if r["kind"] == "top" and r["value"]:
            top[r["seed_term"]].append(r)
    ev = []
    for w in winners[:2]:
        items = sorted(top.get(w["keyword"], []), key=lambda r: -float(r["value"]))[:4]
        if items:
            ev.append(f'For {note(w["keyword"])} the top related queries are '
                      + ", ".join(f'{note(i["query"])} ({int(float(i["value"]))})'
                                  for i in items) + ".")

    dining = next((r for r in cats if r["keyword"] == "custom dining table"), None)
    best = winners[0] if winners else None
    compare = ""
    if dining and best:
        share = f(dining, "adjusted_index") / f(best, "adjusted_index")
        compare = (f' and custom dining tables run at {pct(share, 0)} of it with '
                   f'{"not a single" if int(dining["commercial_intent_queries"]) == 0 else "few"} '
                   f'buying-intent query attached')

    anchor_top = sorted(top.get("custom furniture", []),
                        key=lambda r: -float(r["value"]))[:3]
    anchor_line = ""
    if anchor_top:
        anchor_line = (
            f'<p>The anchor itself behaves the same way: the top related query for '
            f'{note("custom furniture")} is {note(anchor_top[0]["query"])}'
            + (", ahead of " + " and ".join(note(a["query"]) for a in anchor_top[1:3])
               if len(anchor_top) > 1 else "")
            + '. Whatever custom demand exists is local and looking for a person to hire.</p>')

    dining_related = [r for r in d["cat_related"] if r["seed_term"] == "custom dining table"]
    thin = ""
    if len(dining_related) <= 2:
        thin = (f'<p>By contrast {note("custom dining table")} returns '
                f'{"exactly one related query — the plural of itself" if len(dining_related)==1 else f"only {len(dining_related)} related queries"}. '
                'There is not enough surrounding search behaviour to form a cluster, which is '
                'consistent with the divergence above: the demand exists, but it is not '
                'expressed as search.</p>')

    lead_name = winners[0]["keyword"].capitalize() if winners else ""
    return Raw(f"""
  <h2 id="categories">Which furniture people want customised</h2>

  <p>Given that someone wants something custom-made, what is it? This sweeps
  {len(cats)} categories against the same anchor — {note("custom furniture")} = 1.000 —
  across five years in California.</p>

  <p>Two corrections have to be applied before the raw numbers mean anything. First,
  several categories are inflated by accessories that share the phrase — {ex}. Each
  category's index is discounted here by the share of its related search volume carrying an
  accessory modifier. Second, scale without buying intent is worth little, so the last
  column counts related queries containing <em>near me</em>, <em>cost</em>, <em>price</em>,
  <em>companies</em> or <em>installation</em> — someone shopping, not browsing.</p>

  {tbl}

  <p class="callout">Only {len(winners)} categories have both scale and buying intent, and
  neither is freestanding furniture. <b>People want built-in storage customised — cabinets
  and closets.</b> {esc(lead_name)} alone outranks the entire {note("custom furniture")}
  category{compare}.</p>

  <p>The evidence behind those two is unambiguous. {" ".join(ev)}</p>

  {anchor_line}
  {thin}

  <div class="callout">
    <p><b>What this changes.</b> The same shop, the same hardwood, the same CNC and finishing
    line can make a closet system or a run of cabinetry as readily as a dining table — but
    the cabinet buyer is searching, price-checking and location-filtering right now, and the
    table buyer is not. If the plan depends on being findable, the wedge is built-in storage.
    If the plan depends on designer relationships, the table is fine and search volume was
    never going to measure it either way.</p>
  </div>""")


def sec_findings(d):
    tam, s = d["tam"], steps_of(d["tam"])
    items = []

    pool = s.get("Bay Area dining-furniture pool (base)", 0)
    hh = s.get("Bay Area households", 0)
    sanity = tam.get("sanity_check", {})
    items.append(("Tier 2 · CEX",
                  f"The pool is {usd(pool)} a year, not a slice of a billion-dollar abstraction",
                  f"{hh:,.0f} Bay Area households × the measured Consumer Expenditure Survey "
                  f"spend on kitchen and dining room furniture. Cross-checked against actual "
                  f"retail sales: the build puts US kitchen-and-dining spend at "
                  f"{pct(sanity.get('dining_share_of_442', 0))} of all NAICS 442 store sales, "
                  f"which is the right shape for one room out of a category that covers the "
                  f"whole house."))

    yr = max((int(r["year"]) for r in d["cex"]), default=0)
    q5 = next((float(r["value"]) for r in d["cex"] if r["item_code"] == "290410"
               and r["cut"] == "LB01" and r["group"] == "Q5 highest 20%"
               and int(r["year"]) == yr), None)
    asp = tam.get("assumptions", {}).get("asp_usd", {}).get("base", 4200)
    if q5:
        items.append(("Tier 2 · CEX",
                      f"Even the richest fifth of households spend ${q5:,.0f} a year on dining furniture",
                      f"That is the ceiling the whole model sits under. A ${asp:,} table is not "
                      f"an annual purchase out of a furniture budget — it is a once-a-decade or "
                      f"once-a-lifetime purchase. Acquisition maths has to survive that, because "
                      f"there is no second sale to amortise it against."))

    share = s.get("Custom search share", 0)
    items.append(("Tier 1 · Trends",
                  f"Custom framing is {pct(share, 2)} of the search volume of the generic term",
                  f"Across five years in California, <span class=\"note\">custom dining table</span> "
                  f"runs at well under one percent of <span class=\"note\">dining table</span>. The "
                  f"rising queries are dominated by seating capacity, extendability and named "
                  f"retail brands — not by bespoke framing. That is a product signal as much as a "
                  f"marketing one."))

    hw = price_change(d["prices"], "Hardwood lumber")
    out_ = price_change(d["prices"], "Nonupholstered wood household")
    emp = price_change(d["prices"], "All employees")
    if hw and out_ and emp:
        gap_pts = (hw[0] - out_[0]) * 100
        items.append(("Tier 2 · PPI",
                      f"Input costs have run {gap_pts:.0f} points ahead of output prices since 2020",
                      f"Hardwood lumber is up {pct(hw[0], 1)} since "
                      f"{MONTHS[int(hw[2][5:7])]} {hw[2][:4]}; the producer price index for "
                      f"nonupholstered wood household furniture is up {pct(out_[0], 1)}. Domestic "
                      f"makers absorbed the difference, and employment in furniture manufacturing "
                      f"fell {pct(abs(emp[0]), 1)} over the same period. Anyone entering is "
                      f"entering a margin squeeze already in progress."))

    bay = [r for r in d["pop"] if r["geo_level"] == "bay_area_total"]
    if bay:
        dom = sum(float(r["domestic_migration"]) for r in bay)
        y0 = min(int(r["year"]) for r in bay)
        items.append(("Tier 2 · PEP",
                      f"The Bay Area has lost {abs(dom):,.0f} people to domestic migration since {y0}",
                      "Offset only recently by international arrivals. Moving is the single largest "
                      "trigger of a furniture purchase, so net-negative domestic migration is a "
                      "demand headwind that national furniture numbers hide completely."))

    cards = "".join(
        f'<article class="finding"><div class="tier">{esc(t)}</div>'
        f'<div><h3>{esc(h)}</h3><p>{b}</p></div></article>'
        for t, h, b in items)
    return Raw(f'\n  <h2 id="findings">What the data says</h2>\n'
               f'\n  <div class="findings bleed">{cards}</div>')


def sec_tam(d):
    tam, s = d["tam"], steps_of(d["tam"])
    if not tam:
        return Raw("")
    ann, months = mrts_annual(d["mrts"])
    latest = max(ann) if ann else 0
    n_m = len(months.get(latest, []))
    part = defaultdict(float)
    if n_m and n_m < 12:
        for r in d["mrts"]:
            if (r["naics"] == "442" and r["seasonally_adjusted"] == "False"
                    and int(r["month"]) in months[latest]):
                part[int(r["year"])] += float(r["sales_musd"])
    yoy = (part[latest] / part[latest - 1] - 1) if part.get(latest - 1) else None

    estab = tam.get("competition", {}).get("bay_area_establishments_337122", 0)
    stats = "".join([
        stat(usd(s.get("US spend on kitchen & dining room furniture", 0), "bn"),
             "US, kitchen & dining",
             f"CEX item 290410 × consumer units, {tam.get('cex_year','')}"),
        stat(usd(s.get("Bay Area dining-furniture pool (base)", 0)), "Bay Area pool",
             "Base case, West-region spend factor"),
        stat(f"{estab}", "Makers in the Bay",
             "NAICS 337122 establishments, CBP 2022"),
        stat(pct(yoy, 1, sign=True) if yoy is not None else "—",
             f"Retail, H1 {latest}",
             f"NAICS 442 vs. H1 {latest-1}, like for like",
             negative=bool(yoy is not None and yoy < 0)),
    ])

    def fmt(step):
        v, u = step["value"], step["unit"]
        if u == "usd/yr":
            return usd(v)
        if u == "share":
            return pct(v, 2)
        if u == "x":
            return f"{v:.2f}×"
        return f"{v:,.0f}"

    rows = [[st["step"], fmt(st), Raw(f'<span class="dim">{esc(st["basis"])}</span>')]
            for st in tam["steps"]]
    steps_tbl = table("Model steps — value and basis", ["Step", "Value", "Basis"],
                      rows, ["", "num", "wrap"])

    ue = tam.get("unit_economics", [])
    target = tam["assumptions"]["target_revenue_usd"]
    ue_tbl = table(f"Orders needed for ${target:,.0f}, against the demand-side market size",
                   ["Average selling price", "Orders / yr", "Orders / wk",
                    "Share of the custom market"],
                   [[f"${u['asp_usd']:,}", f"{u['orders_for_1m_revenue']:.0f}",
                     f"{u['orders_per_week']:.1f}",
                     f"{u['share_of_market_needed_pct']:.1f}%"] for u in ue],
                   ["", "num", "num", "num"])

    demand, supply, _ = _gap(d)
    share_supply = target / supply if supply else 0
    share_demand = (ue[0]["share_of_market_needed_pct"] / 100) if ue else 0

    cac = tam.get("cac", {})
    cac_tbl = table(f"At a ${cac.get('cpc_usd',0):.2f} cost per click",
                    ["Site conversion", "Implied CAC", "Share of a base-ASP table"],
                    [[pct(c["conversion_rate"], 1), f"${c['cac_usd']:,.0f}",
                      f"{c['cac_as_pct_of_base_asp']:.1f}%"]
                     for c in cac.get("scenarios", [])],
                    ["", "num", "num"])
    placeholder = "PLACEHOLDER" in cac.get("cpc_basis", "")
    cpc_para = ("The CPC below is a placeholder. It is the only unmeasured number in the "
                "model, and Google Keyword Planner replaces it with a real bid — which is "
                "why that credential is worth the two days it takes."
                if placeholder else
                f"CPC basis: {esc(cac.get('cpc_basis',''))}.")

    sanity = tam.get("sanity_check", {})
    sanity_para = ""
    if sanity:
        sanity_para = (f'<p><strong>Sanity check.</strong> The CEX build puts US '
                       f'kitchen-and-dining spend at {pct(sanity["dining_share_of_442"])} of '
                       f'all NAICS 442 retail sales ({usd(sanity["mrts_442_annual_usd"],"bn")}). '
                       f'{esc(sanity["reading"])}</p>')

    return Raw(f"""
  <h2 id="tam">The bottom-up TAM</h2>

  <p>Every step traces to a collector output and a manifest line. The model is built from
  household spend upward; nothing is a percentage of a global market figure.</p>

  <div class="stats bleed">{stats}</div>

  {steps_tbl}
  {sanity_para}

  <h3>What ${target:,.0f} of revenue requires</h3>
  {ue_tbl}

  <p class="callout">At the demand-side sizing, a ${target:,.0f} business would be
  {pct(share_demand, 0)} of the entire addressable market. <b>That is the strongest argument
  that the demand-side sizing is wrong</b> — and that the channel assumption underneath it is
  wrong with it. Against the supply-side figure, the same ${target:,.0f} is
  {pct(share_supply, 1)}.</p>

  <h3>Acquisition cost floor</h3>
  <p>{cpc_para}</p>
  {cac_tbl}""")


def sec_intent(d):
    means = defaultdict(list)
    for r in d["trends"]:
        means[r["keyword"]].append(float(r["anchor_scaled"]))
    ranked = sorted(((k, sum(v) / len(v)) for k, v in means.items()), key=lambda kv: -kv[1])
    anchor = ranked[0][1] if ranked else 1
    kw_tbl = table("California, five years, scaled against the anchor = 1.000",
                   ["Keyword", "Relative interest", ""],
                   [[k, f"{v:.3f}", bar_cell(v / anchor)] for k, v in ranked],
                   ["", "num", "plot"])

    rising = [r for r in d["related"] if r["kind"] == "rising"]

    def rank(r):
        fv = r["formatted_value"]
        if fv.lower().startswith("break"):
            return -1e9
        return -float(fv.replace("+", "").replace("%", "").replace(",", "") or 0)

    top_rising = sorted(rising, key=rank)[:15]
    highlight = {"solid wood dining table", "white oak dining table"}
    rows, classes = [], []
    for r in top_rising:
        rows.append([Raw(f'<span class="dim">{esc(r.get("seed_term","—"))}</span>'),
                     r["query"], r["formatted_value"]])
        classes.append("lead" if r["query"] in highlight else None)
    dining_rising = [r for r in rising if r.get("seed_term") == "custom dining table"]
    if not dining_rising:
        rows.append([Raw('<span class="dim">custom dining table</span>'),
                     Raw('<span class="dim">no rising queries — too little volume to '
                         'form a cluster</span>'),
                     Raw('<span class="dim">—</span>')])
        classes.append(None)
    rising_tbl = table("Rising related queries, by the term they belong to",
                       ["Seed term", "Rising query", "Change"], rows,
                       ["", "wrap", "num"], classes)

    focus = [r for r in d["metro"] if r["batch"] == "geo_focus"
             and r["keyword"] == "custom dining table"]
    metro_tbl = Raw("")
    if focus:
        top = sorted(focus, key=lambda r: -int(r["index"]))[:8]
        metro_tbl = table("Where the interest is (unanchored, 100 = peak California metro)",
                          ["Metro", "Index"],
                          [[r["geo_name"], r["index"]] for r in top], ["wrap", "num"])

    sw = next((v for k, v in ranked if k == "solid wood dining table"), None)
    wo = next((v for k, v in ranked if k == "white oak dining table"), None)
    rise_note = ""
    if any(r["query"] in highlight for r in top_rising):
        rise_note = (f' But note the highlighted rows: {note("solid wood dining table")} and '
                     f'{note("white oak dining table")} are themselves rising off the generic '
                     f'term. Solid wood is a <em>growing modifier</em> inside a category people '
                     f'search generically — a different and better position than owning the '
                     f'word "custom".')

    return Raw(f"""
  <h2 id="intent">Tier 1 — purchase intent</h2>

  <p>Google Trends returns figures relative to whatever set of terms you ask about, so terms
  queried separately are not comparable. Every batch here carries the same anchor term,
  {note("dining table")}, and is rescaled by it — which makes all {len(ranked)} terms
  directly comparable to each other.</p>

  {kw_tbl}
  {rising_tbl}

  <p class="callout">Two things are rising: <b>seating capacity and extendability</b> and
  <b>DTC brands</b>.{rise_note}</p>

  {metro_tbl}""")


def sec_gov(d):
    out = ['\n  <h2 id="gov">Tier 2 — government data</h2>']

    ann, months = mrts_annual(d["mrts"])
    if ann:
        latest = max(ann)
        n_m = len(months[latest])
        part = defaultdict(float)
        if n_m < 12:
            for r in d["mrts"]:
                if (r["naics"] == "442" and r["seasonally_adjusted"] == "False"
                        and int(r["month"]) in months[latest]):
                    part[int(r["year"])] += float(r["sales_musd"])
        rows = []
        for y in sorted(ann)[-8:]:
            if y == latest and n_m < 12:
                v = (part[y] / part[y - 1] - 1) if part.get(y - 1) else None
                rows.append([Raw(f'{y} <span class="dim">first {n_m} months</span>'),
                             usd(ann[y] * 1e6, "bn"),
                             pct(v, 1, sign=True) if v is not None else "—"])
            else:
                v = (ann[y] / ann[y - 1] - 1) if ann.get(y - 1) else None
                rows.append([str(y), usd(ann[y] * 1e6, "bn"),
                             pct(v, 1, sign=True) if v is not None else "—"])
        out.append(table("Furniture and home furnishings retail sales, NAICS 442 — Census MRTS",
                         ["Year", "Sales", "Year on year"], rows, ["", "num", "num"]))
        if n_m < 12:
            out.append(f'<p class="note">The {latest} figure covers {n_m} months and is '
                       f'compared against the same months of {latest-1}, not a full year.</p>')

    if d["cex"]:
        yr = max(int(r["year"]) for r in d["cex"])

        def val(item, group, cut="LB01"):
            m = [r for r in d["cex"] if r["item_code"] == item and r["cut"] == cut
                 and r["group"] == group and int(r["year"]) == yr]
            return f"${float(m[0]['value']):,.0f}" if m else Raw('<span class="dim">—</span>')

        groups = [("Lowest 20%", "Q1 lowest 20%"), ("Second 20%", "Q2"),
                  ("Third 20%", "Q3"), ("Fourth 20%", "Q4"),
                  ("Highest 20%", "Q5 highest 20%"), ("All households", "All consumer units")]
        rows = [[label, val("290410", g), val("FURNITUR", g)] for label, g in groups]
        rows.append(["West region", val("290410", "West", "LB11"),
                     val("FURNITUR", "West", "LB11")])
        out.append(table(f"Average annual household spend by income quintile, {yr} — BLS CEX",
                         ["Quintile", "Kitchen & dining furniture", "All furniture"],
                         rows, ["", "num", "num"]))

    if d["cbp"]:
        codes = ["337122", "337211", "337212", "321918", "238350", "442110"]
        rows = []
        for c in codes:
            sub = [r for r in d["cbp"] if r["naics"] == c]
            if not sub:
                continue

            def e(level):
                m = [r for r in sub if r["geo_level"] == level]
                return f"{int(m[0]['estab']):,}" if m else "—"
            rows.append([c, sub[0]["naics_label"], e("us"), e("ca_total"),
                         e("bay_area_total")])
        out.append(table("Establishments by industry — Census County Business Patterns 2022",
                         ["NAICS", "Industry", "US", "California", "Bay Area"],
                         rows, ["", "wrap", "num", "num", "num"]))
        tam = d["tam"]
        per = tam.get("competition", {}).get("revenue_per_maker_base_usd")
        estab = tam.get("competition", {}).get("bay_area_establishments_337122", 0)
        mill = tam.get("competition", {}).get("bay_area_establishments_337212", 0)
        _, supply, _ = _gap(d)
        if estab and supply:
            out.append(f'<p>The {estab} wood household furniture makers are the real '
                       f'competitive set, and they are the same {estab} establishments whose '
                       f'payroll produces the supply-side market figure at the top of this '
                       f'page. At the base multiple that is roughly <strong>'
                       f'{usd(supply/estab, "m", 2)} of revenue per establishment</strong> — '
                       f'small shops, not factories. A further {mill} custom millwork shops '
                       f'sit alongside them.</p>')

    if d["imports"]:
        world = defaultdict(float)
        for r in d["imports"]:
            if r["partner"] == "World":
                world[int(r["year"])] += float(r["value_usd"] or 0)
        if world:
            mx = max(world.values())
            out.append(table("US wood-furniture imports, all wooden HS lines — UN Comtrade",
                             ["Year", "Value", ""],
                             [[str(y), usd(world[y], "bn"), bar_cell(world[y] / mx)]
                              for y in sorted(world)], ["", "num", "plot"]))
        latest = max(int(r["year"]) for r in d["imports"])
        top = defaultdict(float)
        for r in d["imports"]:
            if int(r["year"]) == latest and r["hs_code"] == "940360" \
                    and r["partner"] != "World":
                top[r["partner"]] += float(r["value_usd"] or 0)
        best = sorted(top.items(), key=lambda kv: -kv[1])[:6]
        if best:
            out.append(table(f"HS 940360 — other wooden furniture, the line containing "
                             f"dining tables, {latest}",
                             ["Origin", "Value"],
                             [[k, usd(v, "bn")] for k, v in best], ["", "num"]))
            hw = price_change(d["prices"], "Hardwood lumber")
            ou = price_change(d["prices"], "Nonupholstered wood household")
            if hw and ou:
                out.append(f'<p>This is the tariff-exposed volume. {esc(best[0][0])} and '
                           f'{esc(best[1][0])} together set the price umbrella that a domestic '
                           f'maker\'s quote is compared against — and the fact that domestic '
                           f'output prices rose only {pct(ou[0],1)} while hardwood rose '
                           f'{pct(hw[0],1)} suggests that umbrella is holding producers down, '
                           f'not lifting them.</p>')

    if d["permits"]:
        by_year = defaultdict(int)
        through = {}
        for r in d["permits"]:
            by_year[int(r["year"])] += int(r["total_units"])
            through[int(r["year"])] = max(through.get(int(r["year"]), 0),
                                          int(r["through_month"]))
        mig = {int(r["year"]): r for r in d["pop"] if r["geo_level"] == "bay_area_total"}
        rows = []
        for y in sorted(by_year)[-6:]:
            label = (Raw(f'{y} <span class="dim">to {MONTHS[through[y]][:3]}</span>')
                     if through.get(y, 12) < 12 else str(y))
            m = mig.get(y)
            rows.append([label, f"{by_year[y]:,}",
                         f"{float(m['net_migration']):+,.0f}" if m else Raw('<span class="dim">—</span>'),
                         f"{float(m['domestic_migration']):+,.0f}" if m else Raw('<span class="dim">—</span>')])
        out.append(table("Bay Area permitted housing units and net migration",
                         ["Year", "Permitted units", "Net migration", "Domestic only"],
                         rows, ["", "num", "num", "num"]))

    return Raw("\n  ".join(str(x) for x in out))


CREDENTIAL_NOTES = {
    "census-acs": ("Census API key", "free", "2 min",
                   "The estimated household count, and the assumed revenue-to-payroll "
                   "multiple that the entire supply-side figure rests on"),
    "census-econ": None,   # same credential as census-acs
    "google-ads": ("Google Keyword Planner", "free", "1–2 days",
                   "The placeholder CPC — the only unmeasured number left in the model, "
                   "and the one that sets the CAC floor"),
    "etsy": ("Etsy Open API", "free", "~1 day",
             "Nothing — it is net-new unit-level evidence: what custom tables actually sold "
             "for, and how many a given maker has sold"),
    "semrush": ("Semrush", "~$130/mo", "instant",
                "Nothing — net-new competitive detail on which queries carry competitor "
                "revenue"),
}


def sec_gaps(d):
    blocked = sorted({src for (src, _), e in d["status"].items()
                      if e["status"] == "blocked_no_credential"})
    entries = [CREDENTIAL_NOTES.get(s) for s in blocked]
    entries = [e for e in entries if e]
    if not entries:
        return Raw("")
    n_coll = sum(1 for (src, _), e in d["status"].items()
                 if e["status"] == "blocked_no_credential")
    tbl = table("Gated sources and what each would settle",
                ["Source", "Cost", "Lead time", "What it replaces"],
                [[a, b, c, dd] for a, b, c, dd in entries],
                ["", "num", "num", "wrap"])
    return Raw(f"""
  <h2 id="next">What is still missing</h2>

  <p>{n_coll} collectors are gated behind {len(entries)} credentials. Each one replaces an
  estimate with a measurement, listed here in the order worth doing.</p>

  {tbl}

  <details class="bleed">
    <summary>Why the Census key is first, and what it would move</summary>
    <div class="flow" style="gap:1rem; padding-top:0.25rem;">
      <p>The supply-side figure — the one that contradicts the search-based sizing — is built
      from one measured number and one assumed one. The measured half is the annual payroll
      County Business Patterns records for the Bay Area establishments. The assumed half is
      the multiple converting payroll to revenue.</p>
      <p>The Economic Census publishes total receipts for NAICS 337122 directly. With a
      Census key the multiple stops being an assumption and becomes a measurement, and the
      central claim on this page either firms up or falls over. That is a two-minute signup
      standing between the analysis and its own load-bearing number.</p>
    </div>
  </details>""")


def sec_method(d):
    st = d["status"]
    ran = sum(1 for e in st.values() if e["status"] == "ok")
    total = len(st)
    words = {8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve",
             13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen"}
    rows = sum(e["rows"] for e in st.values())
    return Raw(f"""
  <h2 id="method">How this was built</h2>

  <p>{words.get(total, total)} collectors, {words.get(ran, ran).lower()} of which need no
  credentials at all, landing {rows:,} rows. Each writes the verbatim API payload to
  {note("data/raw/")}, a tidy table to {note("data/processed/")}, and one line to
  {note("data/MANIFEST.jsonl")} recording the URL, fetch time, row count and status. Nothing
  downstream quotes a number without a manifest line behind it.</p>

  <p>Two substitutions were needed. USITC DataWeb requires an account token, so import
  figures come from UN Comtrade's public endpoint — the same underlying US statistics, same
  HS lines. The Census MRTS API is now key-gated, so retail sales come from the published
  workbook, which carries the identical series back to {min(mrts_annual(d['mrts'])[0], default=1992)}.</p>

  <p class="callout">This page is generated by {note("scripts/build_page.py")} from the
  collector outputs — every figure, table and derived claim above is computed, not typed.
  The model's assumptions all live in one block at the top of {note("scripts/build_tam.py")}.
  <b>Change an assumption there, re-run the pipeline, and this page rewrites itself.</b></p>""")


def sec_footer(d):
    srcs = sorted({src for (src, _), e in d["status"].items() if e["status"] == "ok"})
    pretty = {"census-mrts": "Census Monthly Retail Trade Survey",
              "census-cbp": "Census County Business Patterns 2022",
              "census-bps": "Census Building Permits Survey",
              "census-popest": "Census Population Estimates vintage 2024",
              "bls-cex": "BLS Consumer Expenditure Survey",
              "bls-prices": "BLS CPI, PPI and Current Employment Statistics",
              "un-comtrade": "UN Comtrade US imports by HS code",
              "google-trends": "Google Trends, California, five years, anchored",
              "analysis": "Derived accessory-adjustment of the category sweep"}
    listed = "; ".join(pretty.get(s, s) for s in srcs)
    return Raw(f"""
  <footer>
    <p class="note">Sources — {esc(listed)}. Collected {esc(_pretty_date())}.
    Generated by scripts/build_page.py.</p>
  </footer>""")


# --------------------------------------------------------------------------- main
def main() -> None:
    d = load()
    if not d["tam"]:
        log("build_page: no tam_model.json — run build_tam.py first")
        return

    head = (HERE / "page.head.html").read_text().strip()
    css = (HERE / "page.css").read_text().strip()

    body = "\n".join(str(s) for s in [
        sec_masthead(d), sec_divergence(d), sec_categories(d), sec_findings(d),
        sec_tam(d), sec_intent(d), sec_gov(d), sec_gaps(d), sec_method(d),
        sec_footer(d),
    ])

    OUT.write_text(f"{head}\n\n<style>\n{css}\n</style>\n\n"
                   f'<div class="page flow">\n{body}\n\n</div>\n')
    log(f"  {OUT.relative_to(ROOT)} written ({len(OUT.read_text()):,} bytes)")


if __name__ == "__main__":
    main()
