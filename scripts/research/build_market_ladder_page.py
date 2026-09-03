"""Render the window-coverings market as a ladder — smallest business to enterprise.

Answers the founder's question in the order it was asked: size the smallest business, go one
layer up, keep going, and say whether enterprise even has the measurement problem or simply
does not care.

Computed from data/processed/market_ladder_susb.csv and market_ladder_ranked.csv. Re-run the
collector and this page rewrites itself.
"""
from __future__ import annotations

import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import PAGES, ROOT, TODAY, log, read_csv  # noqa: E402
from page_kit import Raw, bar_cell, esc, stat, table  # noqa: E402

HERE = __import__("pathlib").Path(__file__).parent
OUT = PAGES / "market-ladder.html"
MONTHS = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
LAYER = {"337920": "Blind & shade manufacturers", "442291": "Window treatment stores"}


def pretty_date():
    y, mo, dd = (int(x) for x in TODAY.split("-"))
    return f"{dd} {MONTHS[mo]} {y}"


def usd(v):
    v = float(v)
    if abs(v) >= 1e9:
        return f"${v/1e9:,.2f}bn"
    if abs(v) >= 1e6:
        return f"${v/1e6:,.1f}m"
    if abs(v) >= 1e3:
        return f"${v/1e3:,.0f}k"
    return f"${v:,.0f}"


def main() -> None:
    ranked = read_csv("market_ladder_ranked")
    raw = read_csv("market_ladder_susb")
    if not ranked:
        log("build_market_ladder_page: run analyse_market_ladder.py first")
        return

    def n(v):
        try:
            return float(v)
        except (TypeError, ValueError):
            return 0.0

    tot = {r["naics"]: r for r in raw if r["bucket_order"] == "01"}
    blinds_rc = sum(n(tot[c]["receipts_usd_000"]) * 1000 for c in LAYER)
    adj = sorted([r for r in raw if r["role"] == "adjacent_mtm" and r["bucket_order"] == "01"],
                 key=lambda r: -n(r["receipts_usd_000"]))
    adj_rc = sum(n(r["receipts_usd_000"]) * 1000 for r in adj)
    soft = sum(n(r["modelled_layer_arr_usd"]) for r in ranked)
    top_mfg = next(r for r in ranked
                   if r["naics"] == "337920" and r["receipts_band_usd_000"].endswith("+"))

    L: list[str] = []
    Add = L.append

    Add(f"""
  <header>
    <h1>The window-coverings market, smallest business to enterprise</h1>
    <p class="lede">Every US firm in the trade, bucketed by its own annual receipts, with what
    a remake costs a business at each rung. Census SUSB 2022 — the only free source that
    reports receipts by firm size. Compiled {esc(pretty_date())}.</p>
  </header>

  <div class="stats">
    {stat(usd(blinds_rc), "US blinds trade",
          "manufacturing plus specialty retail, 2,203 firms")}
    {stat(f"{n(top_mfg['share_of_industry']):.0%}", "held by 10 manufacturers",
          "of all US blind and shade manufacturing revenue")}
    {stat(usd(soft) + " ARR", "Software ceiling, blinds only",
          "every firm buying, no competitor, no churn", negative=True)}
  </div>

  <h2>Why this question has a structural answer</h2>

  <p>The founder's question was whether even enterprise has the measurement problem, or
  whether they simply do not care. The ladder answers it, but not in the shape the question
  assumed. <b>The pain concentrates exactly where the buyers are fewest, and the buyers
  concentrate exactly where the pain is trivial.</b></p>

  <p>Ten manufacturers hold {n(top_mfg['share_of_industry']):.1%} of a
  {usd(n(tot['337920']['receipts_usd_000'])*1000)} industry. Each of those ten carries
  {usd(n(top_mfg['remade_per_firm_lo_usd']))}&ndash;{usd(n(top_mfg['remade_per_firm_hi_usd']))}
  of remade order value a year. At the other end of the same ladder, 27 manufacturers under
  $100k of receipts carry about $1,700&ndash;$5,800 each. A firm losing five thousand dollars a
  year cannot buy anything. A firm losing fifteen million can buy almost anything.</p>
""")

    for code in ("337920", "442291"):
        rows = [r for r in ranked if r["naics"] == code]
        mx = max((n(r["receipts_usd"]) for r in rows), default=1) or 1
        body = [[
            r["receipts_band_usd_000"],
            f"{int(n(r['firms'])):,}",
            Raw(f"{bar_cell(n(r['receipts_usd'])/mx)} {usd(n(r['receipts_usd']))}"),
            f"{n(r['share_of_industry']):.1%}",
            usd(n(r["receipts_per_firm_usd"])),
            f"{usd(n(r['remade_per_firm_lo_usd']))} – {usd(n(r['remade_per_firm_hi_usd']))}",
        ] for r in rows]
        t = tot[code]
        Add(f"""
  <h2>{esc(LAYER[code])} <span class="note">NAICS {code}</span></h2>

  <p>{int(n(t['firms'])):,} firms · {int(n(t['establishments'])):,} establishments ·
  {usd(n(t['receipts_usd_000'])*1000)} receipts</p>

  {table(f"{LAYER[code]} by firm receipts band",
         ["Band ($k)", "Firms", "Receipts", "% of industry", "Per firm",
          "Remade per firm, 3–10%"], body,
         # `.num` sets padding-right:0 — a num column followed by a text one
         # renders as "27$1.6m". Firms stays left-aligned beside the bar cell.
         aligns=["", "", "", "num", "num", "num"],
         row_classes=[("lead" if r["receipts_band_usd_000"].endswith("+") else None)
                      for r in rows])}
""")

    Add(f"""
  <h2>The venture question</h2>

  <p>Price every firm in both industries at what its revenue could carry — nothing below
  $500k of receipts, $3k up to $2.5m, $12k to $10m, $40k to $30m, $150k above that — assume
  <i>all</i> of them buy, assume no competitor and no churn, and a blinds-only software
  business tops out at <b>{usd(soft)} of ARR</b>. That is a ceiling nobody reaches, and it is
  not a venture outcome.</p>

  <p>The value being destroyed is much larger than the fee anyone would pay to stop it:
  <b>{usd(blinds_rc*0.03)}&ndash;{usd(blinds_rc*0.10)}</b> of order value is remade each year
  across the trade. Charging against that value rather than per seat is a different
  calculation, and it has not been run.</p>

  <h2>Where it could be venture-scale</h2>

  <p>Every industry below cuts a product to a dimension somebody took at a site — the same
  measure-to-machine path, in a different material. Blinds is
  {blinds_rc/(blinds_rc+adj_rc):.1%} of the pool.</p>

  {table("Adjacent made-to-measure industries, US 2022",
         ["NAICS", "Industry", "Firms", "Receipts"],
         [[r["naics"], r["industry"], f"{int(n(r['firms'])):,}",
           usd(n(r["receipts_usd_000"])*1000)] for r in adj]
         + [["", Raw("<b>Adjacent total</b>"), "",
             Raw(f"<b>{usd(adj_rc)}</b>")]],
         aligns=["", "wrap", "num", "num"])}

  <p>Three routes survive the arithmetic, and they are three different companies. Take
  manufacturing revenue rather than a tool fee, against a
  {usd(n(tot['337920']['receipts_usd_000'])*1000)} manufacturing TAM where one percent is
  {usd(n(tot['337920']['receipts_usd_000'])*1000*0.01)}. Generalise the measure-to-machine
  path across made-to-measure generally, against {usd(adj_rc + blinds_rc)}. Or go global.
  Blinds survives as a <b>beachhead</b> — 302 manufacturers is a countable market to learn in
  — but the ladder says it is not the destination.</p>

  <h2>What the first five calls already say</h2>

  <p>Five founder-conducted phone calls into US dealers and workrooms, logged as E7&ndash;E11,
  complicate this before any of it is acted on. Stoneside measures free but makes the
  <i>customer</i> liable when the customer supplied the dimensions — one cited case ran to 23
  windows reordered. A national retailer charges <b>$225 to send a measurer</b>, says it is
  "not accurate enough", and <b>declines jobs outright</b> when the travel is too far. Every
  dealer contacted sends a human to the window and none uses software to capture or verify.
  And the family-run owners were <b>not enthusiastic</b> about a software fix.</p>

  <p>Read together with the ladder, those calls point away from the remake as the thing to
  sell against. The dealer has already transferred remake liability to the customer where it
  can. What it has not solved is the <b>truck roll</b>: $225 a visit, and revenue simply
  refused when the window is too far away. That is a cost the dealer cannot push onto anyone,
  and it is not what this page sized.</p>

  <p class="note">Source — US Census SUSB 2022, "Number of Firms and Establishments,
  Employment, Annual Payroll and Receipts by Industry and Enterprise Receipts Size", keyless
  bulk workbook. Collected by scripts/research/t2_susb_market_ladder.py, laddered by
  scripts/research/analyse_market_ladder.py. The 3–10% remake rate is ASSUMED, not measured —
  it is what H3A1 exists to settle, and every dollar figure here moves linearly with it. Seat
  prices are modelled. NAICS undercounts the trade: Budget Blinds franchisees and the
  big-box channel appear in neither code.</p>

  <footer>
    <p class="note">Generated by scripts/research/build_market_ladder_page.py.</p>
  </footer>""")

    head = (HERE / "page.head.market.html").read_text().strip()
    css = (HERE / "page.css").read_text().strip()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(f"{head}\n\n<style>\n{css}\n</style>\n\n"
                   f'<div class="page flow">\n' + "\n".join(L) + "\n\n</div>\n")
    log(f"  {OUT.relative_to(ROOT)} written ({len(OUT.read_text()):,} bytes)")


if __name__ == "__main__":
    main()
