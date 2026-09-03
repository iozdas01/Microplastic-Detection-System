"""Who is actually in the window-covering market, and which call sizes which layer.

The founder's framing, and it is the right one: the same failure — a wrong measurement —
has a DIFFERENT cost structure at every layer of this trade. A mom-and-pop that fabricates
its own product eats material, labour and a lost day. A big-box chain eats a subcontractor
invoice and a guarantee. An online retailer eats a free remake and nothing else. So each
layer needs its own sizing arithmetic, its own number, and its own person to phone.

That makes bottom-up sizing tractable: you do not need one number for "the market", you need
seven small ones, and each is obtainable in a single conversation with someone reachable.

Census counts come from `window_covering_structure.csv` so they stay generated. The taxonomy
and the sizing formulas are judgement and are authored here.

    python scripts/research/build_players_page.py
"""
from __future__ import annotations

import csv
import html
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLUG = "high-mix-manufacturing"
STRUCT = ROOT / f"reports/{SLUG}/research/data/processed/window_covering_structure.csv"
OUT = ROOT / f"reports/{SLUG}/pages/window-covering-players.html"

# leverage: how many businesses one conversation tells you about.
LAYERS = [
    dict(n="1", name="Independent workroom that fabricates",
         what="Makes the product, measures it, fits it. One P&amp;L carries the whole chain.",
         feels="Everything. Material and labour twice on a remake, plus the measuring visit itself.",
         formula="jobs/yr × $225 ÷ annual revenue = share of revenue spent measuring",
         have="<b>$225 per visit</b> — E8, n=1",
         need="jobs per year · annual revenue",
         who="The owner. Answers the phone himself.",
         reach="easy", leverage=1,
         note="This is the layer the founder has already reached. Two more questions finish it."),
    dict(n="2", name="Authorised independent dealer",
         what="Buys product from Hunter Douglas, Springs or similar. Measures, sells, installs. Does not fabricate.",
         feels="The measuring visit, and the reorder cost when the wrong number was theirs.",
         formula="jobs/yr × visit cost + remakes/yr × reorder cost",
         have="nothing first-hand",
         need="jobs per year · who is billed when the number was wrong",
         who="Dealer principal.",
         reach="easy", leverage=1,
         note="The bulk of the specialist retail count. Same call shape as layer 1."),
    dict(n="3", name="Franchise network",
         what="Budget Blinds (Home Franchise Concepts), Bloomin' Blinds, Made in the Shade. Franchisee owns the local P&amp;L and buys through franchisor agreements.",
         feels="Franchisee feels it locally. <b>The franchisor sees it across every territory.</b>",
         formula="territories × jobs/territory/yr × visit cost",
         have="nothing first-hand",
         need="aggregate remake rate across the network · territory count · jobs per territory",
         who="A franchisee first, because they are reachable and will talk. Then franchisor operations or vendor management.",
         reach="franchisee easy · franchisor medium", leverage=1000,
         note="THE HIGHEST-LEVERAGE CALL IN THE MARKET. A franchisor already aggregates this across a four-figure number of businesses, because remakes hit the product orders they negotiate. One conversation replaces a hundred."),
    dict(n="4", name="Vertically integrated national",
         what="3 Day Blinds (owned by Hunter Douglas), Stoneside. Own factories, own measurers, own installers.",
         feels="All of it, on one P&amp;L, and they can attribute it properly because they own every step.",
         formula="remake cost + measure cost, both as a share of revenue",
         have="Stoneside: free measure visit, customer liable if they self-measure, 4–5 week lead time — E7, E9",
         need="remake rate · what the measure operation costs as a share of revenue",
         who="Operations director. Stoneside is already a warm contact.",
         reach="medium", leverage=1,
         note="Best single P&amp;L to understand, because nobody else can separate the costs cleanly."),
    dict(n="5", name="Big box",
         what="Home Depot (owns Blinds.com since 2014), Lowe's, Costco. Sell manufacturer product; subcontract measure and install to third-party local installers.",
         feels="A subcontractor invoice and a guarantee liability. They have pushed the labour off their own books.",
         formula="measure jobs/yr × subcontract rate + guarantee claims × remake cost",
         have="<b>Lowe's charges $45</b> for a professional measure — public",
         need="is $45 the true cost or a subsidised loss-leader · remake rate on the programme",
         who="<b>Not corporate.</b> An installer who works the programme. They know the rate and the economics and they are reachable.",
         reach="installer easy · corporate very hard", leverage=100,
         note="The $45-versus-$225 spread is the sharpest open question in this market. Five times, for nominally the same visit."),
    dict(n="6", name="Online, customer self-measures",
         what="Blinds.com, SelectBlinds, Blinds Galore, Wayfair. No visit at all — the buyer measures their own window.",
         feels="Pure remake liability through the fit guarantees. SelectBlinds' FIT Protection and Blinds.com's SureFit both pay for the CUSTOMER'S error.",
         formula="orders/yr × guarantee claim rate × remake cost",
         have="the guarantees exist and are given away at checkout — public record",
         need="what share of orders are remade under the guarantee",
         who="Operations or customer service manager.",
         reach="hard", leverage=100,
         note="<b>The cleanest number in the entire market.</b> No professional visit confounds it, so their remake rate is a direct measurement of how often a human mismeasures a window. Every other layer's rate is contaminated by the visit."),
    dict(n="7", name="Manufacturers",
         what="Hunter Douglas (largest worldwide), Springs Window Fashions, Norman, plus the long tail. Cut to a dimension somebody else supplied.",
         feels="Product and labour twice when the fault is theirs; they bill the dealer when it is not.",
         formula="orders/yr × remake rate × (material + labour)",
         have="Sun Glow publishes the dealer arithmetic: one remake wipes 1.0–2.3 comparable jobs by margin",
         need="remake rate as a share of orders · the split between own-fault and dealer-fault",
         who="Production or quality manager. They track it monthly; it hits cost of goods.",
         reach="medium", leverage=1,
         note="H3A1 as written targets this layer. The calls so far have all been the retail side."),
]

CSS = """
:root{--bg:#fbfaf8;--fg:#17161a;--mut:#6d6a73;--faint:#9b98a2;--line:#e6e2dc;--card:#fff;
--accent:#1f4f7a;--hot:#8a5a1e;--ok:#2f6b4f}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font:16px/1.65 ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:880px;margin:0 auto;padding:64px 24px 120px}
h1{font-size:32px;letter-spacing:-.025em;margin:0 0 10px;font-weight:650}
.dek{color:var(--mut);margin:0 0 8px;max-width:64ch}
.gen{color:var(--faint);font-size:12.5px;margin:0 0 56px}
h2{font-size:12px;text-transform:uppercase;letter-spacing:.12em;color:var(--mut);font-weight:650;margin:0 0 14px}
.sec{margin:0 0 64px}
.lede{font-size:18px;line-height:1.55;margin:0 0 26px;max-width:64ch}
.L{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:24px 26px;margin-bottom:16px}
.L.hot{border-color:var(--hot);box-shadow:0 0 0 3px rgba(138,90,30,.08)}
.Lh{display:flex;gap:14px;align-items:baseline;margin-bottom:4px;flex-wrap:wrap}
.Ln{font-family:ui-monospace,Menlo,monospace;font-size:12px;color:var(--faint);flex:none}
.Lt{font-size:20px;font-weight:650;letter-spacing:-.015em}
.pill{font-size:10.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
padding:3px 8px;border-radius:5px;background:#fdf1e3;color:var(--hot)}
.Lw{color:var(--mut);font-size:15px;margin:0 0 18px;max-width:70ch}
dl{display:grid;grid-template-columns:150px 1fr;gap:9px 18px;margin:0;font-size:14.5px}
dt{color:var(--faint);font-size:11px;text-transform:uppercase;letter-spacing:.08em;padding-top:3px}
dd{margin:0;color:var(--fg)}
dd.m{color:var(--mut)}
code{font-family:ui-monospace,Menlo,monospace;font-size:13px;background:#f1efeb;
padding:2px 6px;border-radius:4px}
.note{margin-top:16px;padding-top:14px;border-top:1px solid var(--line);font-size:14px;color:var(--mut)}
table{border-collapse:collapse;width:100%;font-size:14.5px;margin-top:8px}
th,td{text-align:right;padding:9px 12px;border-bottom:1px solid var(--line)}
th:first-child,td:first-child{text-align:left}
th{font-size:11px;text-transform:uppercase;letter-spacing:.07em;color:var(--faint);font-weight:650}
td.big{font-weight:650}
.hint{color:var(--faint);font-size:13px;margin-top:10px}
@media(max-width:640px){dl{grid-template-columns:1fr}dt{padding-top:12px}}
@media(prefers-color-scheme:dark){
:root{--bg:#141317;--fg:#eceaf0;--mut:#9d99a6;--faint:#6f6b77;--line:#2c2933;--card:#1c1b21;
--accent:#84b8e0;--hot:#e0a86a;--ok:#7fc0a0}
code{background:#26242c}.pill{background:#2b2118}}
"""


def counts():
    by = defaultdict(dict)
    for r in csv.DictReader(STRUCT.open(encoding="utf-8")):
        by[r["naics"]] = {"est": int(r["total_establishments"]), "emp": int(r["total_employees"])}
    return by


def build() -> Path:
    c = counts()
    cards = []
    for L in LAYERS:
        hot = L["leverage"] > 1
        pill = f'<span class="pill">1 call ≈ {L["leverage"]:,} businesses</span>' if hot else ""
        cards.append(f"""<div class="L{' hot' if hot else ''}">
 <div class="Lh"><span class="Ln">LAYER {L['n']}</span><span class="Lt">{L['name']}</span>{pill}</div>
 <p class="Lw">{L['what']}</p>
 <dl>
  <dt>Feels</dt><dd class="m">{L['feels']}</dd>
  <dt>Sizing formula</dt><dd><code>{L['formula']}</code></dd>
  <dt>Already have</dt><dd class="m">{L['have']}</dd>
  <dt>Still need</dt><dd>{L['need']}</dd>
  <dt>Who to call</dt><dd class="m">{L['who']}</dd>
  <dt>Reachability</dt><dd class="m">{L['reach']}</dd>
 </dl>
 <div class="note">{L['note']}</div>
</div>""")

    # Worked example. Two framings, because one of them needs a variable fewer.
    #
    # Share of revenue is really $225 / average job value — the jobs/yr term cancels. That
    # collapses a two-unknown model to one unknown, and the surviving unknown (what a job is
    # worth) is the easier of the two to ask for and the easier to sanity-check.
    per_job = []
    for jv in (750, 1000, 1500, 2500, 4000, 6000):
        per_job.append(f"<tr><td>${jv:,} job</td><td class='big'>{225/jv*100:.1f}%</td>"
                       f"<td>{'yes' if 225/jv > 0.08 else 'marginal'}</td></tr>")
    annual = []
    for jobs in (100, 200, 400, 800):
        annual.append(f"<tr><td>{jobs:,} jobs</td><td class='big'>${jobs*225:,}</td>"
                      f"<td>${jobs*225/12:,.0f}</td></tr>")

    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Window Coverings — Who to Call</title><style>{CSS}</style></head><body><div class="wrap">

<h1>Seven layers, seven numbers, seven calls</h1>
<p class="dek">The same failure — a wrong measurement — costs something different at every
layer of this trade. So you do not need one number for "the market". You need seven small
ones, and each is obtainable from one conversation with someone reachable.</p>
<p class="gen">Census counts generated from window_covering_structure.csv. Taxonomy and sizing
formulas authored in scripts/research/build_players_page.py — do not edit this file.</p>

<div class="sec">
<h2>Why layer by layer</h2>
<p class="lede">A top-down number does not exist here: no single NAICS code contains this
trade, and the biggest sellers are filed under home centres. That is usually bad news. Here it
is not, because <b>every layer's cost shows up on a different line and each one is separately
askable.</b> Size them one at a time and they cross-check each other.</p>
</div>

<div class="sec">
<h2>The layers</h2>
{"".join(cards)}
</div>

<div class="sec">
<h2>Worked example — layer 1, the founder's own</h2>
<p class="lede">The obvious model has two unknowns — jobs per year and annual revenue — but
they cancel. <b>Measuring as a share of revenue is just $225 divided by what an average job is
worth.</b> One unknown, and it is the easier one to ask for:</p>
<table>
<tr><th>Average job value</th><th>Share of revenue spent measuring</th><th>Worth removing?</th></tr>
{"".join(per_job)}
</table>
<p class="hint">This is the number that decides whether layer 1 is a business or a rounding
error, and it swings by <b>eight times</b> across a plausible range of job values. On a small
single-room job the visit eats a fifth of the revenue; on a whole-house job it is noise. So
the question is not "how big is the market" but <b>"how small are the jobs"</b> — which is
also, neatly, why big box can charge $45 and E8 charges $225.</p>
<p class="lede">Jobs per year is still needed, but only for the absolute figure:</p>
<table>
<tr><th>Jobs per year</th><th>Spent measuring, annually</th><th>Per month</th></tr>
{"".join(annual)}
</table>
<p class="hint">$225 per visit is measured (E8, n=1). Both remaining unknowns — average job
value and jobs per year — come from one conversation with any independent, and the founder has
already had four of these calls without asking either.</p>
</div>

<div class="sec">
<h2>Which calls to make first</h2>
<p class="lede">Not in layer order. In leverage order.</p>
<table>
<tr><th>Call</th><th>Layer</th><th>Tells you about</th><th>Reachability</th></tr>
<tr><td>A Budget Blinds franchisee, then their franchisor</td><td>3</td><td class="big">~1,000 businesses</td><td>easy → medium</td></tr>
<tr><td>An installer working a Home Depot or Lowe's programme</td><td>5</td><td class="big">a national programme</td><td>easy</td></tr>
<tr><td>Ops or CS at an online retailer</td><td>6</td><td class="big">the uncontaminated rate</td><td>hard</td></tr>
<tr><td>Stoneside operations</td><td>4</td><td>one full P&amp;L</td><td>warm already</td></tr>
<tr><td>Two more independents</td><td>1</td><td>finishes the worked example</td><td>easy</td></tr>
</table>
<p class="hint">The franchise call is the outlier and it is worth saying plainly: a franchisor
already aggregates remake data across a four-figure number of businesses, because remakes flow
through the product orders they negotiate on the network's behalf. That is a published-nowhere
number that one person can hand you.</p>
</div>

<div class="sec">
<h2>The one number that is cleanest</h2>
<p class="lede">Layer 6. An online retailer's remake rate is the only figure in this market
<b>uncontaminated by a professional visit</b> — the customer measured, so a remake means a
human mismeasured a window, full stop. Every other layer's rate mixes customer error, surveyor
error, factory tolerance and out-of-square openings. If one number is worth being persistent
for, it is that one.</p>
</div>

<div class="sec">
<h2>Census counts, for the two layers a code can see</h2>
<table>
<tr><th>Population</th><th>Establishments</th><th>Employees</th></tr>
<tr><td>Blind &amp; shade manufacturers (337920)</td><td>{c['337920']['est']:,}</td><td>{c['337920']['emp']:,}</td></tr>
<tr><td>Specialist window-treatment stores (442291)</td><td>{c['442291']['est']:,}</td><td>{c['442291']['emp']:,}</td></tr>
<tr><td>Other building finishing contractors (238390)</td><td>{c['238390']['est']:,}</td><td>{c['238390']['emp']:,}</td></tr>
</table>
<p class="hint">Layers 3, 5 and 6 appear in none of these. 238390 is a broad trade code and
only a fraction of it fits window coverings, so treat it as an upper bound on installers
rather than a count of them. Employer establishments only — sole traders are excluded, so
every figure is a floor.</p>
</div>

</div></body></html>"""
    OUT.write_text(doc, encoding="utf-8")
    return OUT


if __name__ == "__main__":
    print(f"[ok] wrote {build().relative_to(ROOT)}")
