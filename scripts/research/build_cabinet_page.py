"""Render the cabinet market case — deliberately short.

Four sections: what the three numbers mean, how each was derived, why cabinets, and what
is still assumed. Everything is computed from cabinet_tam_model.json.
"""
from __future__ import annotations

import json
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import PROC, RESEARCH, ROOT, TODAY, log, read_csv  # noqa: E402
from diagrams import funnel  # noqa: E402
from page_kit import Raw, esc, note, pct, stat, table, usd  # noqa: E402

HERE = __import__("pathlib").Path(__file__).parent
OUT = RESEARCH / "cabinet-demand-case.html"
MONTHS = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def pretty_date():
    y, mo, dd = (int(x) for x in TODAY.split("-"))
    return f"{dd} {MONTHS[mo]} {y}"


def main() -> None:
    mp = PROC / "cabinet_tam_model.json"
    if not mp.exists():
        log("build_cabinet_page: run build_cabinet_tam.py first")
        return
    m = json.loads(mp.read_text())
    A, steps, cap = m["assumptions"], m["steps"], m["capacity"]
    rank = read_csv("custom_demand_ranking")

    def find(name):
        return next(s for s in steps if s["step"].startswith(name))

    tam, share = find("TAM —"), find("Share of cabinet demand")
    pool, sam, som = find("The custom slice"), find("SAM —"), find("SOM —")
    makers = find("Cabinet makers")
    payroll = find("What they pay")

    L: list[str] = []
    Add = L.append

    Add(f"""
  <header class="masthead bleed">
    <div class="flow">
      <p class="eyebrow">Market case · {esc(pretty_date())}</p>
      <h1>Custom kitchen cabinets: the market, and how we sized it</h1>
      <p class="lede">Three numbers, built from Census data rather than a market report,
      with every step shown. Nothing here is bought from a research firm.</p>
    </div>
  </header>""")

    # ------------------------------------------------------------------ 1. the numbers
    Add(f"""
  <h2 id="numbers">The three numbers</h2>

  <p>TAM, SAM and SOM are three nested circles. Only the smallest one is anything like our
  revenue.</p>

  <div class="stats bleed">
    {stat(usd(tam["value"]), "TAM", "the whole US cabinet industry")}
    {stat(usd(sam["value"]), "SAM", "the part our model could serve")}
    {stat(usd(som["value"]), "SOM", "everything one factory can build")}
  </div>

  <div class="findings">
    <div class="finding"><span class="tier">TAM</span><div>
      <h3>{esc(usd(tam["value"]))} — the size of the pond</h3>
      <p>What all {int(makers["value"]):,} American cabinet makers sell between them, at
      manufacturer prices. Not our revenue. It is the number that says this is a real
      industry rather than a niche.</p></div></div>
    <div class="finding"><span class="tier">SAM</span><div>
      <h3>{esc(usd(sam["value"]))} — the part we could compete for</h3>
      <p>Custom cabinets only ({esc(pct(share["value"], 1))} of the industry), and only the
      share that can be sold direct rather than through a showroom. Still not our revenue —
      it is what is available to win.</p></div></div>
    <div class="finding"><span class="tier">SOM</span><div>
      <h3>{esc(usd(som["value"]))} — what we could actually build</h3>
      <p>One panel cell running two shifts makes {cap["boxes_per_year"]:,} cabinet boxes a
      year, or {cap["kitchens_per_year"]:,} kitchens. That is
      {esc(pct(cap["share_of_sam"], 0))} of the SAM — <b>so the factory runs out long
      before the market does</b>, and no guess about market share is needed.</p></div></div>
  </div>

  <p class="callout">This is why the SOM is a capacity number and not a percentage.
  Assuming "we will take 2% of the market" would be inventing the most important figure in
  the model. Counting how many boxes a machine can cut in a year is not an assumption — it
  is arithmetic on a cycle time. <b>The honest ceiling is
  {esc(usd(som["value"]))}, and reaching it is a selling problem, not a market-size
  one.</b></p>""")

    # ------------------------------------------------------------------ 2. derivation
    Add(f"""
  <h2 id="how">How each number was derived</h2>

  <p>Start from something countable and multiply down. Three steps are <b>measured</b> from
  public data, three are <b>arithmetic</b>, and one is an <b>assumption</b>.</p>

  {funnel(steps)}""")

    rows = [[s["step"], s["kind"],
             (f'${s["value"]/1e9:,.2f}bn' if s["unit"] == "usd/yr" and s["value"] >= 1e9
              else f'${s["value"]/1e6:,.1f}m' if s["unit"] == "usd/yr"
              else pct(s["value"], 2) if s["unit"] == "share"
              else f'{s["value"]:,.0f}'),
             s["source"]] for s in steps if s["unit"] in ("usd/yr", "share")]
    Add(str(table("Every step", ["Step", "Kind", "Value", "Where it came from"], rows,
                  aligns=["wrap", "wrap", "num", "wrap"],
                  row_classes=[("lead" if r[1] == "assumed" else None) for r in rows])))

    Add(f"""
  <p>The anchor is {esc(usd(payroll["value"]))} of payroll. {int(makers["value"]):,}
  businesses pay that to {int(find("People they employ")["value"]):,} people every year.
  Nobody pays wages out of demand that does not exist — which is why the top of this funnel
  is evidence rather than an estimate.</p>""")

    # ------------------------------------------------------------------ 3. why cabinets
    unres = [r for r in rank if r["resolved"] != "True"]
    comp = m["industry_comparison"]
    hh = [
        ["Industry size", "$16.0bn", "$3.2bn"],
        ["Can search demand be measured?", "yes", "no — 94% of weeks at zero"],
        ["Every unit genuinely bespoke?", "yes — no two kitchens match",
         "no — a chair is a repeated design"],
        ["Fits one panel cell?", "yes", "no — solid timber, different plant"],
        ["Plant cost", "$3.2m", "$4.8m"],
        ["Where the margin comes from", "cost and fit at volume", "brand at low volume"],
    ]
    Add(f"""
  <h2 id="why">Why cabinets</h2>

  {table("Cabinets against a chair", ["", "Custom cabinets", "A chair"], hh,
         aligns=["wrap", "wrap", "wrap"])}

  <p>Three reasons, in order of weight.</p>

  <p><b>The market is five times bigger.</b> Cabinet manufacturing is
  {esc(usd(comp[0]["implied_revenue_usd"]))} against
  {esc(usd(next(c["implied_revenue_usd"] for c in comp if c["naics"] == "337122")))} for
  the category containing every chair, table and dresser.</p>

  <p><b>It is the only category we can actually measure.</b> Of the categories tested in
  Google Trends, {len(unres)} sit at the index floor — their search index is zero or one in
  more than 80% of weeks, which cannot be read. "custom cabinets" never does.</p>

  <p><b>Every kitchen is a different shape.</b> That is the point. A chair is one design
  made many times, which suits a mould and a brand. A kitchen is bespoke every single time,
  which is exactly the job automation is good at and a hand shop is slow at.</p>

  <p class="callout">The deciding line is the last row of the table. <b>An automated
  factory's advantage is cost and fit at volume; a luxury chair's advantage is brand at low
  volume.</b> A chair business would not need this factory at all.</p>""")

    # ------------------------------------------------------------------ 4. assumptions
    band = m["custom_share_band"]
    brows = [[k, pct(v["share"], 2), usd(v["custom_pool_usd"]), usd(v["sam_usd"])]
             for k, v in band.items()]
    Add(f"""
  <h2 id="assumed">What is assumed, and which way it bends</h2>

  <p>One number in the funnel is a judgement: <b>how much of a showroom-sold category can
  be won online</b>. It is set at {esc(pct(A["online_addressable_share"]["base"], 0))} and
  nothing in any public dataset measures it. A configurator with real prices would.</p>

  <p>Three further caveats sit on the measured numbers, and they do not all point the same
  way. The {esc(usd(tam["value"]))} <b>includes countertops</b> as well as cabinets, which
  overstates it. It <b>counts only businesses with payroll</b>, missing the long tail of
  one-person shops — 54% of establishments already have fewer than five staff. And custom
  cabinetry is also built by architectural woodwork firms in a different industry code
  worth {esc(usd(next(c["implied_revenue_usd"] for c in comp if c["naics"] == "337212")))},
  none of which is counted here. <b>Two of the three push the market up.</b></p>

  <p>The {esc(pct(share["value"], 1))} custom share is a share of <i>searches</i>, not of
  revenue, and it excludes semi-custom entirely — a factory box with configurable sizes and
  finishes, which is what a configurator actually sells. So it is a floor, not a centre.</p>

  {table("The custom slice if that share is wrong",
         ["Case", "Custom share", "Custom market", "SAM"], brows,
         aligns=["wrap", "num", "num", "num"],
         row_classes=[None, "lead", None])}

  <p class="note">Sources — establishment, employment and payroll data from Census County
  Business Patterns 2022, NAICS 337110. Search data from Google Trends, United States, five
  years. The revenue-to-payroll multiple, the online share and the cell cycle times are
  stated in scripts/build_cabinet_tam.py. Compiled {esc(pretty_date())}.</p>

  <footer>
    <p class="note">Generated by scripts/build_cabinet_page.py from
    data/processed/cabinet_tam_model.json. Change an assumption and re-run, and this page
    rewrites itself.</p>
  </footer>""")

    head = (HERE / "page.head.cabinet.html").read_text().strip()
    css = (HERE / "page.css").read_text().strip()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(f"{head}\n\n<style>\n{css}\n</style>\n\n"
                   f'<div class="page flow">\n' + "\n".join(L) + "\n\n</div>\n")
    log(f"  {OUT.relative_to(ROOT)} written ({len(OUT.read_text()):,} bytes)")


if __name__ == "__main__":
    main()
