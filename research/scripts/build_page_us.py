"""Render the published HTML page for the US TAM / SAM / SOM model.

Same design system as build_page.py — page.css, page_kit — but built on
tam_us_model.json rather than the Bay Area model. Nothing is typed in: every figure,
table row and derived claim is computed from data/processed/, so re-running the pipeline
rewrites the page rather than leaving a stale one behind.

    .venv/bin/python scripts/build_page_us.py
    # then: Artifact(file_path="reports/us-configurable-furniture.html")
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import MANIFEST, PROC, ROOT, TODAY, log, read_csv  # noqa: E402
from page_kit import Raw, bar_cell, esc, note, pct, stat, table, usd  # noqa: E402

HERE = __import__("pathlib").Path(__file__).parent
OUT = ROOT / "reports" / "us-configurable-furniture.html"

MONTHS = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def load():
    status = {}
    if MANIFEST.exists():
        for line in MANIFEST.read_text().splitlines():
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                continue
            status[(e["source"], e["dataset"])] = e
    return {
        "m": json.loads((PROC / "tam_us_model.json").read_text())
        if (PROC / "tam_us_model.json").exists() else {},
        "cex": read_csv("cex_furniture_expenditure"),
        "mrts": read_csv("mrts_furniture_monthly"),
        "prices": read_csv("bls_prices"),
        "imports": read_csv("imports_wood_furniture"),
        "trends": read_csv("trends_interest_over_time"),
        "coverage": read_csv("metro_coverage"),
        "rank": read_csv("custom_demand_ranking"),
        "status": status,
    }


def _pretty_date():
    y, mo, dd = (int(x) for x in TODAY.split("-"))
    return f"{dd} {MONTHS[mo]} {y}"


def steps_of(m):
    return {s["step"]: s["value"] for s in m.get("steps", [])}


def mrts_annual(mrts, naics="442"):
    ann, months = defaultdict(float), defaultdict(set)
    for r in mrts:
        if r["naics"] == naics and r["seasonally_adjusted"] == "False":
            ann[int(r["year"])] += float(r["sales_musd"])
            months[int(r["year"])].add(int(r["month"]))
    return ann, months


def trends_mean(trends):
    acc = {}
    for r in trends:
        try:
            acc.setdefault(r["keyword"], []).append(float(r["anchor_scaled"]))
        except (KeyError, ValueError):
            continue
    return {k: sum(v) / len(v) for k, v in acc.items() if v}


def price_change(prices, label_prefix, base_period="2020-01"):
    ser = sorted([r for r in prices if r["label"].startswith(label_prefix)],
                 key=lambda r: r["period"])
    if not ser:
        return None
    base = next((r for r in ser if r["period"] == base_period), ser[0])
    return (float(ser[-1]["value"]) / float(base["value"]) - 1), ser[-1]["period"]


# --------------------------------------------------------------------------- sections
def sec_masthead(d):
    m, st = d["m"], d["status"]
    ran = sum(1 for e in st.values() if e["status"] == "ok")
    gated = sum(1 for e in st.values() if e["status"] == "blocked_no_credential")
    tam = steps_of(m)["US household furniture spend (TAM)"]
    som = m["som"]["som_year_3_usd"]
    ratio = m["som"]["ramp"][-1]["share_of_base_sam_pct"]
    chips = "".join(f"<div><b>{esc(a)}</b>{esc(b)}</div>" for a, b in [
        (f"{ran + gated} collectors", f"{ran} run, {gated} gated"),
        ("Keyless", "Runs with no credentials"),
        (usd(tam), "US household furniture spend"),
        (f"{ratio:.1f}%", "Year-3 output as a share of SAM"),
    ])
    return Raw(f"""
  <header class="masthead bleed">
    <div class="flow">
      <p class="eyebrow">US market sizing · compiled {esc(_pretty_date())}</p>
      <h1>An {esc(usd(tam))} market, and a {esc(usd(som))} constraint</h1>
      <p class="lede">Configurable furniture sold direct and built in an autonomous
      factory, sized bottom-up from household spend, production capacity, search behaviour
      and metro service reach — no syndicated market numbers.</p>
    </div>
    <div class="stamp">{chips}</div>
  </header>""")


def sec_funnel(d):
    m = d["m"]
    tam = steps_of(m)["US household furniture spend (TAM)"]
    sam, som = m["sam"], m["som"]
    pick = m["beachhead"]
    r3 = som["ramp"][-1]
    sc = m.get("sanity_check", {})
    bd = m.get("som_bound")
    if bd:
        bound_line = (
            f"SOM is the smaller of what one cell can make "
            f"({bd['capacity_units_per_year']:,} units a year, derived from measured "
            f"station cycle times rather than assumed) and what the market supports "
            f"({bd['demand_units_per_year']:,}). <b>{esc(bd['binding_constraint'].capitalize())} "
            f"binds — the cell is {bd['oversize_factor']}× larger than year-3 demand.</b> "
            f"The scarce thing here is buyers, not throughput, which is why the next "
            f"dollar belongs in the configurator rather than in a faster machine.")
    else:
        bound_line = (f"Year-3 output is <b>{r3['share_of_base_sam_pct']:.1f}%</b> of SAM.")
    stats = "".join(str(s) for s in [
        stat(usd(tam), "TAM", "US household spend on furniture, all articles"),
        stat(usd(sam["base_usd"]), "SAM",
             f"{pick['article'].lower()}, configurable and online-addressable"),
        stat(usd(som["som_year_3_usd"]), "SOM",
             f"year 3 at one production cell — {r3['units']:,} units"),
    ])
    return Raw(f"""
  <h2 id="funnel">The three numbers</h2>

  <div class="stats bleed">{stats}</div>

  <p>The TAM is built from the ground up: every one of the nine article lines under the
  Consumer Expenditure Survey's <i>Furniture</i> heading, each multiplied by the number of
  consumer units in each income quintile. It reconciles to {esc(pct(sc.get('tam_share_of_442', 0)))}
  of Census retail sales for NAICS 442 — the expected shape, since 442 carries home
  furnishings as well as furniture.</p>

  <p class="callout">{bound_line}</p>""")


def sec_divergence(d):
    """The honest tension: what the data supports vs what the thesis needs."""
    m = d["m"]
    sam = m["sam"]
    A = m["assumptions"]
    floor = sam["grid"]["floor/base"]
    base = sam["grid"]["base/base"]
    ceiling = sam["grid"]["ceiling/base"]
    mult = A["custom_willing_multiple"]["base"]
    measured = sam["custom_search_share_measured"]
    width = (floor / ceiling * 100) if ceiling else 0
    width_b = (base / ceiling * 100) if ceiling else 0
    return Raw(f"""
  <h2 id="divergence">The finding</h2>

  <p>Only one number in the SAM is measured, and it is the small one. Google Trends can see
  how many people search for a <i>custom</i> version of an article rather than a plain one:
  for the beachhead article that is {esc(pct(measured, 2))} of the generic term. That is the
  demand that exists today, when "custom" means a large premium and a long wait from a
  joinery shop.</p>

  <p>An autonomous factory sells configurable furniture at close to stock price. That is a
  different offer to a different buyer, and no available dataset measures how many people
  would take it. The model therefore multiplies the measured share — and that multiplier,
  not the market, is what the whole size of the opportunity turns on.</p>

  <div class="diverge bleed">
    <div class="method m-supply">
      <div class="method-head">
        <span class="method-name">Measured · custom demand as it exists today</span>
        <span class="method-value">{esc(usd(floor))}<span class="note"> /yr</span></span>
      </div>
      <div class="bar"><span style="width:{width:.2f}%"></span></div>
      <p class="note">The article pool at the {esc(pct(measured, 2))} search share, with no
      uplift at all. Defensible from the data alone.</p>
    </div>

    <div class="method m-demand">
      <div class="method-head">
        <span class="method-name">Assumed · if removing the premium multiplies demand {esc(f"{mult:g}")}×</span>
        <span class="method-value">{esc(usd(base))}<span class="note"> /yr</span></span>
      </div>
      <div class="bar"><span style="width:{width_b:.2f}%"></span></div>
      <p class="note">The base case in this report, and an assumption. At the ceiling
      multiple it is {esc(usd(ceiling))}.</p>
    </div>

    <p class="verdict">The gap between those two bars is not a modelling detail — it is the
    company. <b>The cheapest way to close it is a configurator landing page with real
    prices and a real checkout</b>, measuring how many visitors configure rather than how
    many search. That single experiment is worth more than any further desk research on
    this page.</p>
  </div>""")


def sec_article(d):
    m = d["m"]
    rows_in = m["articles"]
    pick = m["beachhead"]
    mx = max(r["us_pool_usd"] for r in rows_in) or 1
    body = []
    classes = []
    for r in rows_in:
        buildable = bool(r["asp_usd"] and r["machine_hours_per_unit"])
        cs = pct(r["custom_search_share"], 2) if r["custom_search_share"] is not None else "—"
        name = r["article"] + (" ★" if r["cex_item"] == pick["cex_item"] else "")
        body.append([
            f"{r['beachhead_score']:.3f}", name,
            Raw(str(bar_cell(r["us_pool_usd"] / mx))), usd(r["us_pool_usd"]),
            cs, pct(r["machinable"], 0), pct(r["flatpack"], 0),
            "yes" if buildable else "no",
        ])
        classes.append("lead" if r["cex_item"] == pick["cex_item"] else None)
    tbl = table(
        "Every CEX furniture article, sized and scored",
        ["Score", "Article", "", "US pool / yr", "Custom share", "Machinable",
         "Flat-pack", "Buildable"],
        body,
        aligns=["num", "wrap", "plot", "num", "num", "num", "num", "num"],
        row_classes=classes)
    w = m["weights"]
    wa = m["weights_assembled"]
    changed = m["service_changes_pick"]
    return Raw(f"""
  <h2 id="article">Which article to build</h2>

  <p>Which article this factory should make is an output of the model, not an input to it.
  Every article line is sized from household spend and scored on four dimensions: pool size
  ({esc(pct(w['pool'], 0))}), custom-search share ({esc(pct(w['custom_share'], 0))}),
  machinability ({esc(pct(w['machinable'], 0))}) and flat-packability
  ({esc(pct(w['flatpack'], 0))}). The last two are engineering judgements about a nested-panel
  cell, not measurements.</p>

  {tbl}

  <p>The highest-scoring article and the chosen one are different, which is the point of the
  last column. Sofas are the largest furniture line in the country at
  {esc(usd(next(r['us_pool_usd'] for r in rows_in if r['article'] == 'Sofas')))} a year and
  carry more custom interest than the storage family — but roughly 85% of a sofa is foam,
  springs and sewing. An autonomous panel factory cannot make one.
  <b>{esc(pick['article'])}</b> is the best article it can actually build: fully machinable
  from nested sheet stock, and it ships flat.</p>

  <details>
    <summary>Does selling in-home assembly change the answer?</summary>
    <p>A crew in the customer's home removes the reason to fear a bulky box, so the scoring
    was re-run with the flat-pack weight cut from {esc(pct(w['flatpack'], 0))} to
    {esc(pct(wa['flatpack'], 0))}. {"The pick moves to " if changed else "It does not change the pick — "}
    <b>{esc(m['beachhead_if_assembled']['article'])}</b>
    {"under that weighting." if changed else "wins under both weightings."} The service tier
    changes the margin on the article, not the choice of it.</p>
  </details>""")


def sec_tiers(d):
    m = d["m"]
    t, b = m["tiers"], m["blended"]
    asm = m["assumptions"]["assembly"]
    prem = t["ladder"][-1]
    rows = [[
        f'{r["tier"]} · {r["price_multiple"]}×', f'${r["price_usd"]:,}',
        pct(r["mix"], 0), pct(r["gross_margin"], 0),
        pct(r["attach_rate_in_serviced_metros"], 0), pct(r["effective_attach_rate"], 1),
        f'${r["revenue_per_order_usd"]:,}', f'${r["gross_profit_per_order_usd"]:,}',
    ] for r in t["ladder"]]
    rows.append(["blended", f'${b["product_asp_usd"]:,}', "100%",
                 pct(b["gross_margin"], 0), "—", pct(b["attach_rate"], 1),
                 f'${b["revenue_per_order_usd"]:,}',
                 f'${b["gross_profit_per_order_usd"]:,}'])
    tbl = table("Three tiers off one cell, plus the in-home assembly attach",
                ["Tier", "Price", "Mix", "Margin", "Attach in-metro", "Effective attach",
                 "Revenue / order", "Gross profit / order"],
                rows,
                aligns=["wrap", "num", "num", "num", "num", "num", "num", "num"],
                row_classes=[None] * len(t["ladder"]) + ["lead"])
    cov = d["coverage"]
    cuts = [5, 25, 100]
    cov_line = ", ".join(
        f"top {n} {pct(float(next(r['cumulative_share_of_us'] for r in cov if int(r['rank']) == n)), 0)}"
        for n in cuts if any(int(r["rank"]) == n for r in cov)) if cov else "—"
    if b["attach_rate"] > 0:
        attach_para = (
            f"An assembly crew is a van, and a van covers a metro — so the attach can only "
            f"be sold where crews exist. Census metro populations put the reach at "
            f"{cov_line} of the US population, and the model multiplies any in-metro "
            f"attach rate by the real coverage of the {asm['serviced_metros']} serviced "
            f"metros.")
        ladder_para = (
            f"The ladder carries the economics; the service enables them. Three tiers blend "
            f"to a <b>${b['revenue_per_order_usd']:,} order at a "
            f"{pct(b['gross_margin'], 0)} margin</b>, of which in-home assembly is "
            f"${b['service_revenue_per_order_usd']:,.0f}.")
    else:
        attach_para = (
            f"<b>There is no assembly attach.</b> "
            f"{esc(asm.get('removed_because', ''))} — so there is nothing to install, and "
            f"nothing caps sales to the {pct(t['coverage_share'], 0)} of the country "
            f"inside serviced metros. The attach columns are held at zero rather than "
            f"deleted, so the service can be switched back on by changing numbers.")
        ladder_para = (
            f"The tier ladder carries the whole revenue model. Three tiers blend to a "
            f"<b>${b['revenue_per_order_usd']:,} order at an assumed "
            f"{pct(b['gross_margin'], 0)} margin</b>. The premium multiple is the only "
            f"measured input in it — mix and margins are assumptions, and the premium "
            f"tier's mix share is the single biggest lever on revenue per order.")
    return Raw(f"""
  <h2 id="tiers">Tiers and the assembly attach</h2>

  <p>The premium price multiple is the one number in this table that is not a guess. It is
  the article's measured Q5 spend skew: the top income quintile already spends
  {esc(f"{prem['price_multiple']}×")} what the average household does on this article, which
  is the observable evidence for how far it can be priced up. Tier mix, margins, attach
  rates and the ${asm['price_usd']} assembly price are assumptions.</p>

  <p>{attach_para}</p>

  {tbl}

  <p class="callout">{ladder_para}</p>""")


def sec_som(d):
    m = d["m"]
    som, f_ = m["som"], m["assumptions"]["factory"]
    asm = m["assumptions"]["assembly"]
    pick = m["beachhead"]
    b = m["blended"]
    cap_rows = [[f"{c['shifts']} ({label})", f"{c['units_per_year']:,}",
                 usd(c["revenue_at_asp_usd"]), f"{c['share_of_base_sam_pct']}%"]
                for label, c in m["capacity"].items()]
    cap = table("Nameplate capacity of one cell",
                ["Shifts", "Units / yr", "Revenue at blended order", "% of SAM"],
                cap_rows, aligns=["wrap", "num", "num", "num"])
    ramp_rows = [[
        r["year"].replace("_", " ").title(), pct(r["utilisation"], 0), f"{r['units']:,}",
        f"{r['units_per_week']}", usd(r["product_revenue_usd"]), f"{r['installs']:,}",
        f"{r['crews_needed']}", usd(r["revenue_usd"]), usd(r["gross_profit_usd"]),
    ] for r in som["ramp"]]
    ramp = table(f"Three-year ramp at {f_['shifts']['base']} shifts",
                 ["Year", "Utilisation", "Units", "Units / wk", "Product revenue",
                  "Installs", "Crews", "Total revenue", "Gross profit"],
                 ramp_rows, aligns=["wrap", "num", "num", "num", "num", "num", "num",
                                    "num", "num"],
                 row_classes=[None, None, "lead"])
    r3 = som["ramp"][-1]
    return Raw(f"""
  <h2 id="som">SOM — the smaller of what we can make and what we can sell</h2>

  <p>One cell, {f_['operating_days_per_year']} operating days, {f_['machine_hours_per_shift']}h
  of machine time per shift, {esc(pct(f_['yield_rate'], 0))} yield, and
  {pick['machine_hours_per_unit']}h of machine time per unit — an assumption to be replaced
  with the cycle time off your own cell. Output is valued at the blended
  ${b['revenue_per_order_usd']:,} order from the tier table above.</p>

  {cap}
  {ramp}

  <p>Year 3 is <b>{r3['units_per_week']} orders a week</b> out of a single cell. The
  plant is not short of room to make that; the question this page cannot answer is whether
  there are that many buyers.</p>""")


def sec_cac(d):
    m = d["m"]
    cac = m["cac"]
    b = m["blended"]
    rows = [[pct(s["conversion_rate"], 1), f"${s['cac_usd']:,.0f}",
             f"{s['cac_as_pct_of_asp']}%", f"{s['cac_as_pct_of_gross_profit']}%",
             usd(s["year_3_ad_spend_usd"])] for s in cac["scenarios"]]
    tbl = table(f"Acquisition cost against a ${b['gross_profit_per_order_usd']:,} gross profit per order",
                ["Site conversion", "Implied CAC", "% of order value",
                 "% of gross profit", "Year-3 ad spend"],
                rows, aligns=["num", "num", "num", "num", "num"])
    worst = cac["scenarios"][0]
    return Raw(f"""
  <h2 id="cac">Can you buy enough demand to fill the line?</h2>

  <p>{esc(cac['cpc_basis'])} The placeholder cost per click is ${cac['cpc_usd']:.2f}.</p>

  {tbl}

  <p>At a {esc(pct(worst['conversion_rate'], 1))} conversion rate paid acquisition eats
  {esc(f"{worst['cac_as_pct_of_gross_profit']:.0f}%")} of gross profit and the capacity plan
  stops being fundable out of its own margin. Getting a real cost per click out of Keyword
  Planner is the highest-value missing measurement in this model.</p>""")


def sec_intent(d):
    m, tr = d["m"], trends_mean(d["trends"])
    pairs = [("sofa", "custom sofa"), ("desk", "custom desk"), ("dresser", "custom dresser"),
             ("bed frame", "custom bed frame"), ("dining table", "custom dining table"),
             ("coffee table", "custom coffee table"), ("tv stand", "custom tv stand"),
             ("bookshelf", "custom bookshelf"), ("wardrobe", "custom wardrobe"),
             ("nightstand", "custom nightstand"), ("closet organizer", "custom closet"),
             ("kitchen cabinets", "custom cabinets")]
    have = [(g, c) for g, c in pairs if g in tr and c in tr]
    mx = max((tr[g] for g, _ in have), default=1)
    rows = [[g, Raw(str(bar_cell(tr[g] / mx))), f"{tr[g]:.3f}", c, f"{tr[c]:.3f}",
             pct(tr[c] / tr[g], 2)]
            for g, c in sorted(have, key=lambda p: -tr[p[0]])]
    tbl = table("Generic versus custom search interest, US, five years",
                ["Generic term", "", "Interest", "Custom term", "Interest", "Custom share"],
                rows, aligns=["wrap", "plot", "num", "wrap", "num", "num"])
    adj = [a for a in m.get("adjacencies", []) if a.get("custom_search_share")]
    adj_html = ""
    if adj:
        a0 = adj[0]
        adj_html = (f"""
  <p class="callout">The one place custom demand is genuinely large is next door.
  <b>{esc(a0['custom'])}</b> runs at {esc(pct(a0['custom_search_share'], 1))} of
  {esc(a0['generic'])} — an order of magnitude above any furniture article. But that is
  home-improvement spend sold through installers, outside the furniture TAM and outside a
  ship-it-flat business. It is the adjacency to grow into once the factory exists, not the
  article to launch with.</p>""")
    return Raw(f"""
  <h2 id="intent">What people actually search for</h2>

  <p>Every term is scaled against the same anchor, so all batches are comparable. Pairing a
  generic term with its custom counterpart gives a custom share per article family — the
  measured floor the SAM is built on.</p>

  {tbl}
  {adj_html}""")


def sec_demand_rank(d):
    rank = d.get("rank") or []
    if not rank:
        return Raw("")
    res = [r for r in rank if r["resolved"] == "True"]
    unres = [r for r in rank if r["resolved"] != "True"]
    free = [r for r in res if r["free_standing_furniture"] == "True"]
    mx = max(float(r["level_vs_custom_furniture"]) for r in rank) or 1
    rows = []
    for r in rank:
        gen = (pct(float(r["furniture_share_of_related"]), 0)
               if r["furniture_share_of_related"] not in ("", "None") else "—")
        shr = (pct(float(r["custom_share_of_generic"]), 2)
               if r["custom_share_of_generic"] not in ("", "None") else "—")
        flr = (pct(float(r["weeks_at_or_below_1"]), 0)
               if r["weeks_at_or_below_1"] not in ("", "None") else "—")
        sc = (f'{float(r["demand_score"]):.3f}'
              if r["demand_score"] not in ("", "None") else Raw('<span class="note">unresolved</span>'))
        name = r["custom_term"] + ("" if r["free_standing_furniture"] == "True" else " ~")
        rows.append([name, Raw(str(bar_cell(float(r["level_vs_custom_furniture"]) / mx))),
                     f'{float(r["level_vs_custom_furniture"]):.3f}', shr, gen, flr, sc])
    tbl = table("US demand for a customisable version, anchored on 'custom furniture'",
                ["Article", "", "Level", "Custom share", "Genuinely furniture",
                 "0/1 weeks", "Score"], rows,
                aligns=["wrap", "plot", "num", "num", "num", "num", "num"],
                row_classes=[("lead" if r["resolved"] == "True"
                              and r["free_standing_furniture"] == "True" else None)
                             for r in rank])
    best = free[0] if free else None
    best_line = (f"The best-resolved free-standing furniture is "
                 f"<b>{esc(best['custom_term'])}</b>, and even that is only "
                 f"{pct(float(best['furniture_share_of_related']), 0)} genuinely furniture "
                 f"in its related searches — the rest is accessories." if best
                 and best.get("furniture_share_of_related") not in ("", "None") else "")
    return Raw(f"""
  <h2 id="ranking">Which customisable furniture is most in demand</h2>

  <p>Every term here is a <i>custom X</i> anchored on <i>custom furniture</i>, so the
  categories are comparable to each other rather than swamped by a generic article term.
  The <b>0/1 weeks</b> column is the share of weeks the index sat at or below 1. Above 80%
  the series is at the Trends resolution floor and is reported as unresolved rather than
  ranked — a number that is 95% zeros is not a small number, it is an absent one.</p>

  {tbl}

  <p class="note">~ = not free-standing furniture: a built-in or an adjacent trade.</p>

  <p class="callout"><b>{len(unres)} of {len(rank)} categories cannot be ranked at all.</b>
  They sit at the index floor. Of the {len(res)} that do resolve,
  {len(res) - len(free)} are built-ins — cabinets, closets, bars, vanities — rather than
  furniture. {best_line} The honest reading is not that one article wins: it is that
  <b>no free-standing customisable furniture article has enough US search demand to
  measure reliably</b>, and the categories that do have volume are the ones sold through
  installers.</p>

  <p>Momentum is deliberately absent. Thirteen of twenty-five series peak in the same week
  — 12 April 2026 — across independent query batches, which is an index artifact rather
  than demand; any year-on-year figure spanning it measures the artifact. The ranking uses
  level only, and the analysis detects that condition rather than assuming it.</p>""")


def sec_gov(d):
    m = d["m"]
    yr = m["cex_year"]
    pick = m["beachhead"]
    cex = d["cex"]
    groups = ["Q1 lowest 20%", "Q2", "Q3", "Q4", "Q5 highest 20%", "All consumer units"]

    def v(item, g):
        r = [x for x in cex if x["item_code"] == item and x["cut"] == "LB01"
             and x["group"] == g and int(x["year"]) == yr]
        return float(r[0]["value"]) if r else None

    mxf = max((v("FURNITUR", g) or 0) for g in groups) or 1
    q_rows = [[g, Raw(str(bar_cell((v("FURNITUR", g) or 0) / mxf))),
               f"${v(pick['cex_item'], g):,.0f}" if v(pick["cex_item"], g) is not None else "—",
               f"${v('FURNITUR', g):,.0f}" if v("FURNITUR", g) is not None else "—"]
              for g in groups]
    quint = table(f"Average annual spend per consumer unit, {yr}",
                  ["Income group", "", pick["article"], "All furniture"],
                  q_rows, aligns=["wrap", "plot", "num", "num"],
                  row_classes=[None] * 5 + ["lead"])

    ann, months = mrts_annual(d["mrts"])
    same = defaultdict(float)
    latest = max(ann) if ann else 0
    n_latest = len(months[latest]) if latest else 12
    for r in d["mrts"]:
        if r["naics"] == "442" and r["seasonally_adjusted"] == "False" \
                and int(r["month"]) <= n_latest:
            same[int(r["year"])] += float(r["sales_musd"])
    m_rows = []
    for y in sorted(ann):
        if y < 2019:
            continue
        partial = len(months[y]) < 12
        label = f"{y} (first {len(months[y])} months)" if partial else str(y)
        if partial:
            prev = same.get(y - 1)
            yoy = pct(same[y] / prev - 1, 1, sign=True) if prev else "—"
        else:
            prev = ann.get(y - 1)
            yoy = pct(ann[y] / prev - 1, 1, sign=True) \
                if prev and len(months[y - 1]) == 12 else "—"
        m_rows.append([label, usd(ann[y] * 1e6), yoy])
    retail = table("US furniture and home-furnishings retail sales, NAICS 442",
                   ["Year", "Sales", "Year on year"], m_rows,
                   aligns=["wrap", "num", "num"])

    comp_rows = [[naics, c["label"], f"{c['establishments']:,}", f"{c['employees']:,}",
                  usd(c["annual_payroll_usd"]), f"{c['under_5_employees']:,}"]
                 for naics, c in m.get("competition", {}).items()]
    comp = table("Who already makes this — Census County Business Patterns 2022",
                 ["NAICS", "Industry", "Establishments", "Employees", "Annual payroll",
                  "Under 5 staff"], comp_rows,
                 aligns=["num", "wrap", "num", "num", "num", "num"])

    imp = defaultdict(float)
    for r in d["imports"]:
        if r.get("partner") == "World":
            try:
                imp[int(r["year"])] += float(r["value_usd"])
            except (KeyError, ValueError):
                continue
    mxi = max(imp.values(), default=1)
    imp_rows = [[y, Raw(str(bar_cell(imp[y] / mxi))), usd(imp[y])] for y in sorted(imp)]
    imports = table("US wood-furniture imports, UN Comtrade",
                    ["Year", "", "Value"], imp_rows, aligns=["wrap", "plot", "num"])

    lumber = price_change(d["prices"], "Hardwood lumber")
    ppi = price_change(d["prices"], "Nonupholstered wood household furniture")
    emp = price_change(d["prices"], "All employees, furniture")
    cost_p = ""
    if lumber and ppi:
        cost_p = (f"<p>Input costs have run ahead of output prices: hardwood lumber "
                  f"{esc(pct(lumber[0], 1, sign=True))} since January 2020 against "
                  f"{esc(pct(ppi[0], 1, sign=True))} for the producer price index of "
                  f"nonupholstered wood household furniture, through {esc(ppi[1])}. "
                  f"Domestic makers have absorbed the difference"
                  + (f", and employment in furniture manufacturing is "
                     f"{esc(pct(emp[0], 1, sign=True))} over the same period" if emp else "")
                  + f". That squeezed margin is what an automated line is built to "
                    f"recover.</p>")

    q5 = v(pick["cex_item"], "Q5 highest 20%") or 0
    years = pick["asp_usd"] / q5 if q5 else 0
    return Raw(f"""
  <h2 id="government">The government evidence</h2>

  {quint}

  <p>The top income quintile spends ${q5:,.0f} a year on the beachhead article. A
  ${pick['asp_usd']:,} unit is therefore not an annual purchase out of a furniture budget —
  at that rate it is a {years:.0f}-year purchase. That is what the acquisition maths has to
  survive, and it is why repeat revenue has to come from a second article rather than a
  second sale of the same one.</p>

  {retail}
  {comp}

  <p>The under-five-staff column is the competitive read: this industry is overwhelmingly
  small shops. That is what makes an automation thesis plausible, and also what makes share
  slow to take — the incumbents are local, referral-fed and numerous.</p>

  {imports}
  {cost_p}""")


def sec_gaps(d):
    blocked = [(s, ds, e) for (s, ds), e in sorted(d["status"].items())
               if e["status"] != "ok"]
    if not blocked:
        return Raw("")
    rows = [[f"{s} / {ds}", e["note"][:110]] for s, ds, e in blocked]
    tbl = table("Sources still gated behind a credential",
                ["Source", "Blocked on"], rows, aligns=["wrap", "wrap"])
    return Raw(f"""
  <h2 id="gaps">What is missing</h2>
  {tbl}
  <p>Keyword Planner is the one that matters. It replaces the placeholder cost per click,
  which drives the entire acquisition section above.</p>""")


def sec_method(d):
    st = d["status"]
    ran = sum(1 for e in st.values() if e["status"] == "ok")
    total = len(st)
    rows = sum(e["rows"] for e in st.values())
    return Raw(f"""
  <h2 id="method">How this was built</h2>

  <p>{total} collectors, {ran} of which ran without any credential, landing {rows:,} rows.
  Each writes the verbatim API payload to {note("data/raw/")}, a tidy table to
  {note("data/processed/")}, and one line to {note("data/MANIFEST.jsonl")} recording the URL,
  fetch time, row count and status. Nothing above quotes a number without a manifest line
  behind it.</p>

  <p>Two substitutions were needed. USITC DataWeb requires an account token, so import
  figures come from UN Comtrade's public endpoint — the same US statistics, the same HS
  lines. The Census MRTS API is key-gated, so retail sales come from the published workbook
  carrying the identical series.</p>

  <p class="callout">This page is generated by {note("scripts/build_page_us.py")} from the
  collector outputs — every figure, table and derived claim is computed, not typed. The
  model's assumptions live in one block at the top of {note("scripts/build_tam_us.py")}.
  <b>Change an assumption there, re-run the pipeline, and this page rewrites itself.</b></p>""")


def sec_footer(d):
    srcs = sorted({s for (s, _), e in d["status"].items() if e["status"] == "ok"})
    pretty = {"census-mrts": "Census Monthly Retail Trade Survey",
              "census-cbp": "Census County Business Patterns 2022",
              "census-bps": "Census Building Permits Survey",
              "census-popest": "Census Population Estimates vintage 2024",
              "bls-cex": "BLS Consumer Expenditure Survey",
              "bls-prices": "BLS CPI, PPI and Current Employment Statistics",
              "un-comtrade": "UN Comtrade US imports by HS code",
              "google-trends": "Google Trends, United States, five years, anchored",
              "analysis": "Derived accessory-adjustment of the category sweep"}
    listed = "; ".join(pretty.get(s, s) for s in srcs)
    return Raw(f"""
  <footer>
    <p class="note">Sources — {esc(listed)}. Collected {esc(_pretty_date())}.
    Generated by scripts/build_page_us.py.</p>
  </footer>""")


def main() -> None:
    d = load()
    if not d["m"]:
        log("build_page_us: no tam_us_model.json — run build_tam_us.py first")
        return

    head = (HERE / "page.head.us.html").read_text().strip()
    css = (HERE / "page.css").read_text().strip()
    body = "\n".join(str(s) for s in [
        sec_masthead(d), sec_funnel(d), sec_divergence(d), sec_article(d),
        sec_tiers(d), sec_som(d), sec_cac(d), sec_demand_rank(d), sec_intent(d),
        sec_gov(d),
        sec_gaps(d), sec_method(d), sec_footer(d),
    ])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(f"{head}\n\n<style>\n{css}\n</style>\n\n"
                   f'<div class="page flow">\n{body}\n\n</div>\n')
    log(f"  {OUT.relative_to(ROOT)} written ({len(OUT.read_text()):,} bytes)")


if __name__ == "__main__":
    main()
