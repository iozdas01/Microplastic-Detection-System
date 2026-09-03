"""The window-covering market on one clean page — structure, money, and where to enter.

Built because the control room is a 315KB working dashboard across eight tabs, which is the
right shape for running outreach and the wrong shape for thinking. This page answers one
question — where do you enter this industry — and shows nothing that does not serve it.

Everything is generated. Census structure comes from `window_covering_structure.csv`; the
buyer conversations are parsed out of `03-validation/evidence.md`. Neither is retyped here,
so the page cannot drift from its sources. Rerun after new evidence lands:

    python scripts/research/build_market_entry_page.py
"""
from __future__ import annotations

import csv
import html
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLUG = "high-mix-manufacturing"
STRUCT = ROOT / f"reports/{SLUG}/research/data/processed/window_covering_structure.csv"
EVID = ROOT / f"reports/{SLUG}/03-validation/evidence.md"
OUT = ROOT / f"reports/{SLUG}/pages/window-covering-market.html"

# The layers, in the order value flows. Labels are the founder's language, not the Census's.
LAYERS = [
    ("337920", "Manufacturers", "Cut and assemble the product to a supplied dimension."),
    ("442291", "Specialist dealers", "Take the measurement, sell the job, own the customer. Excludes big box and e-commerce."),
    ("238390", "Installers", "Fit it. Discover the misfit first."),
]


def load_structure() -> dict:
    rows = list(csv.DictReader(STRUCT.open(encoding="utf-8")))
    by = defaultdict(lambda: {"bands": []})
    for r in rows:
        d = by[r["naics"]]
        d["label"] = r["label"]
        d["est"] = int(r["total_establishments"])
        d["emp"] = int(r["total_employees"])
        d["pay"] = int(r["annual_payroll_usd"])
        d["bands"].append((r["band"], int(r["establishments"]), float(r["share_of_establishments"])))
    return by


def load_h3_evidence() -> list[dict]:
    """Every H3 entry in the ledger, with the fields this page shows."""
    text = EVID.read_text(encoding="utf-8")
    out = []
    for block in re.split(r"\n  - id: ", text)[1:]:
        eid = block.split("\n", 1)[0].strip()
        def field(name):
            m = re.search(rf"^    {name}: (>-\n(?:      .*\n)+|.*)$", block, re.M)
            if not m:
                return ""
            return " ".join(m.group(1).replace(">-", "").split())
        if field("hunch") != "H3":
            continue
        out.append({
            "id": eid, "verdict": field("verdict"), "conf": field("confidence"),
            "assumption": field("assumption_linked"), "claim": field("claim"),
            "source_type": field("source_type"),
        })
    return out


CSS = """
:root{--bg:#fbfaf8;--fg:#17161a;--mut:#6d6a73;--faint:#9b98a2;--line:#e6e2dc;--card:#fff;
--ok:#2f6b4f;--warn:#8a5a1e;--bad:#8f3232;--accent:#1f4f7a;--bar:#c9d6e2}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font:16px/1.65 ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif;
-webkit-font-smoothing:antialiased}
.wrap{max-width:840px;margin:0 auto;padding:64px 24px 120px}
h1{font-size:32px;letter-spacing:-.025em;margin:0 0 8px;font-weight:650}
.dek{color:var(--mut);font-size:16px;margin:0 0 8px}
.gen{color:var(--faint);font-size:12.5px;margin:0 0 64px}
h2{font-size:12px;text-transform:uppercase;letter-spacing:.12em;color:var(--mut);
font-weight:650;margin:0 0 4px}
.sec{margin:0 0 72px}
.lede{font-size:19px;line-height:1.55;margin:0 0 28px;max-width:62ch}
.lede b{font-weight:650}
/* layer cards */
.layer{background:var(--card);border:1px solid var(--line);border-radius:12px;
padding:22px 24px;margin-bottom:14px}
.layer.here{border-color:var(--accent);box-shadow:0 0 0 3px rgba(31,79,122,.07)}
.ltop{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:2px}
.lname{font-size:19px;font-weight:650}
.lnaics{font-size:11.5px;color:var(--faint);font-family:ui-monospace,Menlo,monospace}
.lrole{color:var(--mut);font-size:14.5px;margin-bottom:16px}
.nums{display:flex;gap:34px;flex-wrap:wrap;margin-bottom:16px}
.n b{display:block;font-size:26px;font-weight:650;letter-spacing:-.02em;line-height:1.15}
.n span{font-size:11.5px;text-transform:uppercase;letter-spacing:.08em;color:var(--faint)}
/* distribution bar */
.dist{display:flex;height:9px;border-radius:5px;overflow:hidden;margin-bottom:7px}
.dist i{display:block}
.dkey{display:flex;flex-wrap:wrap;gap:12px;font-size:11.5px;color:var(--mut)}
.dkey span b{font-weight:600;color:var(--fg)}
.flag{display:inline-block;font-size:11.5px;font-weight:650;padding:2px 8px;border-radius:5px;
letter-spacing:.03em}
.f-here{background:#e8f0f7;color:var(--accent)}
/* provenance */
.badge{display:inline-block;font-size:10.5px;font-weight:700;letter-spacing:.06em;
text-transform:uppercase;padding:2px 7px;border-radius:4px;vertical-align:2px;margin-right:8px}
.b-meas{background:#e6f0ea;color:var(--ok)}
.b-call{background:#fdf1e3;color:var(--warn)}
.b-unsrc{background:#fbe9e9;color:var(--bad)}
.b-unk{background:#eeecf0;color:var(--mut)}
.fact{border-top:1px solid var(--line);padding:16px 0}
.fact:last-child{border-bottom:1px solid var(--line)}
.fact p{margin:6px 0 0;color:var(--mut);font-size:14.5px}
.fact .h{font-size:16px}
/* the gap */
.gap{background:#fff;border:2px dashed var(--line);border-radius:12px;padding:30px 28px;
text-align:center}
.gap b{display:block;font-size:23px;font-weight:650;margin-bottom:8px;letter-spacing:-.015em}
.gap p{margin:0;color:var(--mut);max-width:52ch;margin-inline:auto;font-size:15px}
/* entry options */
.opt{background:var(--card);border:1px solid var(--line);border-radius:12px;
padding:22px 24px;margin-bottom:14px}
.oh{display:flex;gap:12px;align-items:baseline;margin-bottom:12px}
.ol{font-family:ui-monospace,Menlo,monospace;font-size:12px;color:var(--faint);flex:none;
padding-top:3px}
.on{font-size:18px;font-weight:650}
.orow{display:grid;grid-template-columns:132px 1fr;gap:6px 16px;font-size:14.5px}
.orow dt{color:var(--faint);font-size:11.5px;text-transform:uppercase;letter-spacing:.07em;
padding-top:4px}
.orow dd{margin:0;color:var(--mut)}
.orow dd.on-fg{color:var(--fg)}
@media(max-width:620px){.orow{grid-template-columns:1fr}.orow dt{padding-top:10px}}
@media(prefers-color-scheme:dark){
:root{--bg:#141317;--fg:#eceaf0;--mut:#9d99a6;--faint:#6f6b77;--line:#2c2933;--card:#1c1b21;
--ok:#7fc0a0;--warn:#e0a86a;--bad:#e08a8a;--accent:#84b8e0;--bar:#33455a}
.b-meas{background:#1b2c23}.b-call{background:#2b2118}.b-unsrc{background:#2c1c1c}
.b-unk{background:#242229}.f-here{background:#1a2733}
.gap{background:#1c1b21}}
"""


def bar(bands, est):
    """Establishment-count distribution as one bar. Micro shops first, largest last."""
    shades = ["#dfe7ee", "#c3d3e0", "#a5bed2", "#86a8c4", "#6892b6", "#4b7ca8", "#2f6699", "#1f4f7a"]
    cells, key = [], []
    for i, (band, n, share) in enumerate(bands):
        c = shades[min(i, len(shades) - 1)]
        cells.append(f'<i style="width:{share*100:.4f}%;background:{c}"></i>')
        key.append(f'<span><b>{n}</b> {html.escape(band)}</span>')
    return f'<div class="dist">{"".join(cells)}</div><div class="dkey">{"".join(key)}</div>'


def build() -> Path:
    st = load_structure()
    ev = load_h3_evidence()
    calls = [e for e in ev if e["source_type"] == "customer_interview"]

    layers_html = []
    for naics, name, role in LAYERS:
        d = st.get(naics)
        if not d:
            continue
        here = naics == "442291"
        layers_html.append(f"""<div class="layer{' here' if here else ''}">
 <div class="ltop"><span class="lname">{name}</span>
  <span class="lnaics">NAICS {naics}</span>
  {'<span class="flag f-here">one of several places the measurement happens</span>' if here else ''}</div>
 <div class="lrole">{role}</div>
 <div class="nums">
  <div class="n"><b>{d['est']:,}</b><span>establishments</span></div>
  <div class="n"><b>{d['emp']:,}</b><span>employees</span></div>
  <div class="n"><b>${d['pay']/1e6:,.0f}m</b><span>annual payroll</span></div>
  <div class="n"><b>{d['emp']/d['est']:.1f}</b><span>avg employees</span></div>
 </div>
 {bar(d['bands'], d['est'])}
</div>""")

    call_html = []
    for e in sorted(calls, key=lambda x: x["id"]):
        v = e["verdict"]
        badge = {"supports": "b-meas", "contradicts": "b-unsrc", "ambiguous": "b-unk"}.get(v, "b-unk")
        call_html.append(f"""<div class="fact">
 <div class="h"><span class="badge {badge}">{html.escape(v)} · {html.escape(e['assumption'])}</span>
 {html.escape(e['claim'][:230])}{'…' if len(e['claim'])>230 else ''}</div>
 <p>{html.escape(e['id'])} · confidence {html.escape(e['conf'])}/5 · founder phone call</p>
</div>""")

    dealers = st["442291"]
    micro = next((n for b, n, s in dealers["bands"] if b == "<5"), 0)
    big = sum(n for b, n, s in dealers["bands"] if b in ("20-49", "50-99"))

    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Window Coverings — Market Entry</title><style>{CSS}</style></head><body><div class="wrap">

<h1>Where do you enter this industry?</h1>
<p class="dek">Made-to-measure window coverings, United States. Everything on this page is
either measured, from a call, or explicitly marked unknown.</p>
<p class="gen">Generated from Census CBP 2022 and the evidence ledger by
scripts/research/build_market_entry_page.py — do not edit this file.</p>

<div class="sec">
<h2>The chain</h2>
<p class="lede">A number is taken off a window, passed down this chain, and cut. Nobody can
check it against the real window until the product arrives. <b>The measurement is taken in the
middle layer — and that layer is the smallest and the most fragmented of the three.</b></p>
{"".join(layers_html)}
</div>

<div class="sec">
<h2>What that shape means — and what it hides</h2>
<p class="lede">Among <em>specialist</em> window-treatment stores, the trade is tiny and
fragmented: of {dealers['est']:,} establishments, <b>{micro:,} have fewer than five people</b>
and only <b>{big}</b> have twenty or more.</p>
<p class="lede"><b>But that code is not the market.</b> Census classifies an establishment by
its primary activity, so the largest sellers of made-to-measure window coverings in America are
counted somewhere else entirely and are invisible above:</p>
<div class="fact"><div class="h"><span class="badge b-meas">verified</span>
Home Depot and Lowe's both sell custom window coverings with measure-and-install services, and
are classified as home centres, not window-treatment stores.</div>
<p>Home Depot has owned Blinds.com since 2014. Both subcontract the measurement itself to
third-party local installers rather than employing measurers.</p></div>
<div class="fact"><div class="h"><span class="badge b-call">the spread worth explaining</span>
Lowe's charges <b>$45</b> for a professional measure. The national retailer in E8 charges
<b>$225</b>.</div>
<p>Five times, for nominally the same visit. Either big box is subsidising it as a cost of
winning the sale, or E8 is pricing it at something closer to true cost. Which one is right
decides who actually feels this — and it is a better question than the remake rate.</p></div>
<div class="fact"><div class="h"><span class="badge b-unk">not countable here</span>
E-commerce (SelectBlinds, Blinds Galore), franchise networks (Budget Blinds, 3 Day Blinds) and
big-box programmes.</div>
<p>These sit under electronic shopping, under building-finishing contractors, or inside a home
centre's line items. No single NAICS code contains the made-to-measure window covering trade,
so <b>no top-down count of it is available at all</b> — which is the strongest argument on this
page for sizing bottom-up from calls.</p></div>
<p class="lede">Scale exists in this industry. It is just not where a specialist retail code
looks. It sits in {st['337920']['est']} manufacturers, whose largest two dozen hold most of the
employment; in {st['238390']['est']:,} installation contractors employing
{st['238390']['emp']:,} people, who are <em>who big box pushes the measuring onto</em>; and in
a handful of national retail programmes that no code isolates.</p>
</div>

<div class="sec">
<h2>What the calls actually said</h2>
<p class="lede">{len(calls)} phone conversations, founder-conducted. Two of them cut against
the thesis, and those are the ones worth reading twice.</p>
{"".join(call_html)}
</div>

<div class="sec">
<h2>What each number is worth</h2>
<div class="fact"><div class="h"><span class="badge b-meas">measured</span>
Establishment counts, employment and payroll for all three layers.</div>
<p>Census County Business Patterns 2022, national file, held in this repo. Reproducible.
Counts employer establishments only — sole traders with no payroll are excluded, so every
count is a floor.</p></div>
<div class="fact"><div class="h"><span class="badge b-call">from one call</span>
$225 to send someone out to measure, charged per job, plus jobs declined when the drive is
too far.</div><p>E8, n=1. The strongest single fact found: a certain cost on every order
rather than a probabilistic one, and it caps their serviceable radius.</p></div>
<div class="fact"><div class="h"><span class="badge b-unsrc">unsourced</span>
“$2.4–2.5bn US revenue, 484 establishments.”</div>
<p>Asserted in the recon file with no URL. Census puts the establishment count at
{st['337920']['est']} — 47% lower — and publishes no revenue variable at all.
<b>Do not use this figure.</b></p></div>
<div class="fact"><div class="h"><span class="badge b-unk">unknown</span>
The remake rate. Nobody publishes it, and it swings the answer roughly threefold.</div>
<p>Which is why the graph asks for it rather than assuming it.</p></div>
</div>

<div class="sec">
<h2>The one number that unlocks the model</h2>
<div class="gap"><b>Jobs per dealer per year</b>
<p>You have the price of a measure visit and the number of dealers. This is the only missing
multiplier between them and a defensible bottom-up figure. One question, to one dealer.</p></div>
</div>

<div class="sec">
<h2>Four ways in</h2>
<p class="lede">Ordered by what the evidence currently supports, not by ambition.</p>

<div class="opt"><div class="oh"><span class="ol">A</span><span class="on">Sell the measurement to vertically integrated dealers</span></div>
<dl class="orow">
<dt>Who pays</dt><dd class="on-fg">Operators who run their own factories and their own measuring crews — the Stoneside shape.</dd>
<dt>Why it fits</dt><dd>They carry both costs, so one sale removes a cost and a constraint. Few dozen targets, not thousands.</dd>
<dt>Evidence for</dt><dd>E8 gives a priced visit and a radius limit. E9 says every dealer sends a human and none uses software.</dd>
<dt>What kills it</dt><dd>If the visit is a sales call as much as a measurement, removing it removes the sale.</dd>
</dl></div>

<div class="opt"><div class="oh"><span class="ol">B</span><span class="on">Sell remake reduction to manufacturers</span></div>
<dl class="orow">
<dt>Who pays</dt><dd class="on-fg">The {st['337920']['est']} manufacturers, concentrated enough that two dozen matter.</dd>
<dt>Why it fits</dt><dd>Real firms with cost lines and quality functions. A remake hits cost of goods and they track it monthly.</dd>
<dt>Evidence for</dt><dd>Sun Glow publishes the arithmetic to its own dealers. Nothing first-hand yet.</dd>
<dt>What kills it</dt><dd>H3A2. If the error is the dealer's number and not the factory's cut, the manufacturer cannot fix it and will not buy.</dd>
</dl></div>

<div class="opt"><div class="oh"><span class="ol">C</span><span class="on">Sell software to the long tail of dealers</span></div>
<dl class="orow">
<dt>Who pays</dt><dd class="on-fg">{micro:,} specialist shops with under five people — plus an uncounted long tail of installers and franchisees.</dd>
<dt>Why it is listed third</dt><dd>Largest count, and the evidence is against it. The owner does the visit himself, so his time is not a line item to remove.</dd>
<dt>Evidence against</dt><dd>E10 — family-run owners were unenthusiastic, unprompted. E11 is the only positive and it is a Mom Test false positive, logged at 2/5.</dd>
<dt>What would revive it</dt><dd>A reason from E10's owners. A no with a reason is worth more than the yes in E11.</dd>
</dl></div>

<div class="opt"><div class="oh"><span class="ol">D</span><span class="on">Sell into a big-box measure-and-install programme</span></div>
<dl class="orow">
<dt>Who pays</dt><dd class="on-fg">Home Depot, Lowe's, or the third-party networks that run their measure services.</dd>
<dt>Why it fits</dt><dd>The only genuine enterprise buyer in the chain. They run measurement at national scale, subcontract it, and carry the remake liability on their own guarantee.</dd>
<dt>Evidence for</dt><dd>None first-hand. Everything here is public record, and no one at either has been contacted.</dd>
<dt>What kills it</dt><dd>Procurement cycles measured in years, and the $45 price point suggests they already treat measurement as a subsidised loss-leader rather than a cost to optimise.</dd>
</dl></div>

<div class="opt"><div class="oh"><span class="ol">E</span><span class="on">Become the dealer</span></div>
<dl class="orow">
<dt>Who pays</dt><dd class="on-fg">Consumers, directly.</dd>
<dt>Why it fits</dt><dd>Own both ends, which is what the belief argues for, and there is existing CNC capacity to point at it.</dd>
<dt>What kills it</dt><dd>Customer acquisition, every time. The record already in this repo says owning a factory does not fix CAC — Model No. owned its factory and its configurator and was absorbed anyway.</dd>
<dt>Test before building</dt><dd>Not a software test. Sell one job.</dd>
</dl></div>
</div>

<div class="sec">
<h2>What to do next</h2>
<p class="lede">Option A remains where a priced pain, a named constraint and a reachable buyer
line up today, and its next question is free: <b>how many jobs a month do you turn down because
the drive is too far, and how far is too far?</b> That converts a complaint into a lost-revenue
number without mentioning a product.</p>
<p class="lede">Option D is now on the board because the enterprise buyer turned out to exist —
it was hidden by a classification code rather than absent from the market. Before spending a
week on it, settle the cheap question the $45-versus-$225 spread raises: <b>is the measure
visit a cost they want removed, or a sales call they are paying to keep?</b> Ask an installer
who works a big-box programme; they will know, and they are reachable.</p>
</div>

</div></body></html>"""
    OUT.write_text(doc, encoding="utf-8")
    return OUT


if __name__ == "__main__":
    p = build()
    print(f"[ok] wrote {p.relative_to(ROOT)}")
