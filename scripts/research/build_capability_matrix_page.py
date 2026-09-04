#!/usr/bin/env python3
"""Build pages/capability-matrix.html — what the window-covering trade's software does.

Company rows, capability marks, revenue and size are all parsed from
outreach/companies.md. Nothing about a company is authored here.

What IS authored here, and nowhere else:
  * CAPABILITY_LABELS — the human name and pipeline order of each capability axis.
    The axis VALUES are declared in companies.md frontmatter `map_vocabularies.capability`;
    this file only names them for display and fixes their left-to-right order.
  * PROPOSED — the capability row for the product under design. It is a design intention,
    not an observation, so it has no place in the company registry. It is rendered in its
    own band, labelled as proposed.

Run: .venv/bin/python scripts/research/build_capability_matrix_page.py
"""
from __future__ import annotations

import re
from html import escape
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SLUG = "high-mix-manufacturing"
SRC = REPO / "reports" / SLUG / "outreach" / "companies.md"
OUT = REPO / "reports" / SLUG / "pages" / "capability-matrix.html"

# Pipeline order, left to right. Keys must exist in companies.md `map_vocabularies.capability`.
CAPABILITY_LABELS = [
    ("remote_capture", "Measure with<br>no one on site"),
    ("onsite_measure_app", "On-site<br>measuring app"),
    ("quoting", "Quoting"),
    ("dealer_orders", "Dealer<br>orders"),
    ("deductions_cutlist", "Deductions<br>→ cut list"),
    ("machine_file_out", "File out<br>to machine"),
    ("production_scheduling", "Production<br>scheduling"),
    ("inventory", "Inventory"),
    ("machine_readback", "Read back<br>from machine"),
    ("cross_shop_routing", "Route across<br>shops"),
]

# The product under design. Authored here; see module docstring for why.
PROPOSED = {
    "name": "Proposed product",
    "have": ["remote_capture", "onsite_measure_app", "dealer_orders"],
    "partial": ["machine_readback", "cross_shop_routing"],
    "note": (
        "Capture is the build. Dealer orders is the integration surface into whichever ERP "
        "the shop already runs. Read-back and routing are marked partial because both are "
        "intended and neither is reachable yet - routing needs order volume that only "
        "capture produces, and read-back needs machines with a programmable interface."
    ),
}

# Display names and reading order for the relationship axis. The VALUES are declared in
# companies.md frontmatter `map_vocabularies.relationship`; only their labels and the order
# they are read in are authored here.
RELATIONSHIPS = [
    ("competitor", "Competitor", "Same job, same buyer, same budget line."),
    ("platform_risk", "Platform risk", "Not competing today. Owns distribution and could bundle."),
    ("rails", "Rails", "Owns the stage after ours. Our Order goes into them."),
    ("analogue", "Analogue", "A different trade. Proof the shape works, not a rival."),
    ("floor", "Floor", "Marks the category baseline, not a player."),
]

DECLARED_RE = re.compile(r"^  capability: \[(.+?)\]$", re.M)
REL_DECLARED_RE = re.compile(r"^  relationship: \[(.+?)\]$", re.M)


def parse_declared() -> list[str]:
    m = DECLARED_RE.search(SRC.read_text(encoding="utf-8"))
    if not m:
        raise SystemExit("companies.md frontmatter has no `capability:` vocabulary line")
    return [v.strip() for v in m.group(1).split(",")]


def parse_companies() -> list[dict]:
    text = SRC.read_text(encoding="utf-8")
    out = []
    for block in text.split("\n## ")[1:]:
        name, _, body = block.partition("\n")
        rec = {"name": name.strip()}
        for m in re.finditer(r"^([a-z_]+): (?!>)(.*)$", body, re.M):
            rec[m.group(1)] = m.group(2).strip().strip('"')
        for m in re.finditer(r"^([a-z_]+): >\n((?:[ ]{2,}.*\n?)+)", body, re.M):
            rec[m.group(1)] = " ".join(m.group(2).split())
        if rec.get("capabilities_have") or rec.get("capabilities_partial"):
            rec["have"] = [v.strip() for v in rec.get("capabilities_have", "").split(",") if v.strip()]
            rec["partial"] = [v.strip() for v in rec.get("capabilities_partial", "").split(",") if v.strip()]
            out.append(rec)
    return out


def money(v: str) -> str:
    try:
        n = int(v)
    except (TypeError, ValueError):
        return ""
    if not n:
        return ""
    if n >= 1_000_000_000:
        return f"${n/1e9:.1f}bn"
    if n >= 1_000_000:
        return f"${n/1e6:.0f}m"
    return f"${n:,}"


CSS = """
:root{
  --bg:#fbfaf8; --fg:#17161a; --mut:#6d6a73; --faint:#9b98a2; --line:#e6e2dc;
  --card:#fff; --sunk:#f4f2ee;
  --accent:#1f4f7a; --hot:#8a5a1e; --ok:#2f6b4f;
  --accent-wash:#eaf1f7; --hot-wash:#fdf1e3; --ok-wash:#e9f2ed;
}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --bg:#141317; --fg:#eceaf0; --mut:#9d99a6; --faint:#6f6b77; --line:#2c2933;
  --card:#1c1b21; --sunk:#201f26;
  --accent:#84b8e0; --hot:#e0a86a; --ok:#7fc0a0;
  --accent-wash:#1a2733; --hot-wash:#2b2118; --ok-wash:#182620;}}
:root[data-theme="dark"]{
  --bg:#141317; --fg:#eceaf0; --mut:#9d99a6; --faint:#6f6b77; --line:#2c2933;
  --card:#1c1b21; --sunk:#201f26;
  --accent:#84b8e0; --hot:#e0a86a; --ok:#7fc0a0;
  --accent-wash:#1a2733; --hot-wash:#2b2118; --ok-wash:#182620;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
  font:16px/1.65 "IBM Plex Sans",ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif;
  -webkit-font-smoothing:antialiased}
.wrap{max-width:1080px;margin:0 auto;padding:64px 24px 120px}
h1{font-size:36px;line-height:1.14;letter-spacing:-.03em;margin:0 0 14px;font-weight:600;text-wrap:balance}
.dek{color:var(--mut);margin:0 0 10px;max-width:64ch;font-size:17px}
.gen{color:var(--faint);font-size:12.5px;margin:0;font-family:"IBM Plex Mono",ui-monospace,monospace}
hr.rule{height:1px;background:var(--line);border:0;margin:44px 0 0}
h2{font-size:11.5px;text-transform:uppercase;letter-spacing:.14em;color:var(--mut);
  font-weight:600;margin:0 0 16px;font-family:"IBM Plex Mono",ui-monospace,monospace}
.sec{margin:56px 0 0}
.lede{font-size:17px;line-height:1.6;margin:0 0 24px;max-width:66ch}
p{max-width:68ch}
.scroll{overflow-x:auto;border:1px solid var(--line);border-radius:12px;background:var(--card)}
table{border-collapse:separate;border-spacing:0;width:100%;font-size:13.5px;min-width:940px}
th,td{padding:10px 8px;border-bottom:1px solid var(--line);text-align:center;vertical-align:middle}
thead th{font-size:10px;line-height:1.35;text-transform:uppercase;letter-spacing:.05em;
  color:var(--faint);font-weight:600;font-family:"IBM Plex Mono",ui-monospace,monospace;
  vertical-align:bottom;padding-bottom:12px}
th.co,td.co{text-align:left;position:sticky;left:0;background:var(--card);z-index:2;
  min-width:190px;padding-left:16px;border-right:1px solid var(--line)}
tbody tr:hover td{background:var(--sunk)}
tbody tr:hover td.co{background:var(--sunk)}
.nm{font-weight:600;font-size:14.5px;letter-spacing:-.01em}
.sub{color:var(--faint);font-size:11px;font-family:"IBM Plex Mono",ui-monospace,monospace;
  display:block;margin-top:2px}
.mark{font-size:15px;line-height:1;font-weight:600}
.yes{color:var(--ok)}
.part{color:var(--hot)}
.non{color:var(--line)}
th.empty-col{color:var(--accent)}
td.empty-col{background:var(--accent-wash)}
tbody tr:hover td.empty-col{background:var(--accent-wash)}
tr.band td{background:var(--sunk);border-bottom:1px solid var(--line);padding:7px 8px}
tr.band td.band-co{background:var(--sunk);font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:10.5px;text-transform:uppercase;letter-spacing:.1em;color:var(--fg);font-weight:600}
tr.band td.band-note{text-align:left;font-size:12px;color:var(--mut);padding-left:14px}
tbody tr.band:hover td{background:var(--sunk)}
tr.us td{background:var(--hot-wash);border-top:2px solid var(--hot);border-bottom:0}
tr.us td.co{background:var(--hot-wash)}
tr.us .nm{color:var(--hot)}
tbody tr:hover.us td{background:var(--hot-wash)}
.legend{display:flex;flex-wrap:wrap;gap:8px 24px;margin:16px 0 0;padding:0;list-style:none;
  font-size:13px;color:var(--mut)}
.legend li{display:flex;align-items:center;gap:8px}
.note{margin-top:18px;padding:14px 16px;border-left:2px solid var(--accent);
  background:var(--accent-wash);border-radius:0 8px 8px 0;font-size:14.5px;max-width:72ch}
.note.warm{border-left-color:var(--hot);background:var(--hot-wash)}
.note b{color:var(--accent)}
.note.warm b{color:var(--hot)}
.cards{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:20px 22px}
.card h3{margin:0 0 6px;font-size:16px;font-weight:600}
.card p{margin:0;color:var(--mut);font-size:14px;max-width:none}
.big{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:26px;font-weight:600;
  letter-spacing:-.02em;display:block;margin-bottom:2px}
@media(max-width:640px){.wrap{padding:40px 18px 90px}h1{font-size:28px}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}
"""


def mark(cap: str, rec: dict) -> tuple[str, str]:
    if cap in rec["have"]:
        return "&#10003;", "yes"
    if cap in rec["partial"]:
        return "&#9683;", "part"
    return "&ndash;", "non"


def cells_for(rec: dict, empty: list[str]) -> str:
    out = []
    for k, _ in CAPABILITY_LABELS:
        sym, cls = mark(k, rec)
        out.append(f'<td class="{"empty-col" if k in empty else ""}">'
                   f'<span class="mark {cls}">{sym}</span></td>')
    return "".join(out)


def build() -> Path:
    text = SRC.read_text(encoding="utf-8")

    declared = parse_declared()
    for key, _ in CAPABILITY_LABELS:
        if key not in declared:
            raise SystemExit(f"capability '{key}' is not declared in companies.md frontmatter")

    m = REL_DECLARED_RE.search(text)
    if not m:
        raise SystemExit("companies.md frontmatter has no `relationship:` vocabulary line")
    rel_declared = [v.strip() for v in m.group(1).split(",")]
    for key, _, _ in RELATIONSHIPS:
        if key not in rel_declared:
            raise SystemExit(f"relationship '{key}' is not declared in companies.md frontmatter")

    rows = parse_companies()
    rows.sort(key=lambda r: -int(r.get("revenue_usd") or 0))
    untagged = [r["name"] for r in rows if r.get("relationship") not in rel_declared]
    if untagged:
        raise SystemExit(f"capability data but no relationship: {untagged}")

    # A column is "empty" only among companies IN THIS TRADE. Analogues are scored on the
    # same axes deliberately — the finding is that they occupy remote_capture and the
    # in-trade companies do not, and folding them into this count would erase it.
    in_trade = [r for r in rows if r.get("relationship") != "analogue"]
    empty = [k for k, _ in CAPABILITY_LABELS
             if not any(k in r["have"] or k in r["partial"] for r in in_trade)]

    head = "".join(f'<th class="{"empty-col" if k in empty else ""}">{lbl}</th>'
                   for k, lbl in CAPABILITY_LABELS)

    body = []
    for rkey, rname, rdesc in RELATIONSHIPS:
        group = [r for r in rows if r.get("relationship") == rkey]
        if not group:
            continue
        body.append(f'<tr class="band"><td class="co band-co">{escape(rname)}</td>'
                    f'<td class="band-note" colspan="{len(CAPABILITY_LABELS)}">'
                    f'{escape(rdesc)}</td></tr>')
        for r in group:
            rev = money(r.get("revenue_usd", ""))
            src = r.get("revenue_source", "")
            meta = " \u00b7 ".join(x for x in [
                r.get("country", ""),
                f"founded {r['founded']}" if r.get("founded") not in ("", "0", None) else "",
                f"{rev} ({src})" if rev else "",
            ] if x)
            body.append(f'<tr><td class="co"><span class="nm">{escape(r["name"])}</span>'
                        f'<span class="sub">{escape(meta)}</span></td>'
                        f'{cells_for(r, empty)}</tr>')

    body.append(f'<tr class="band"><td class="co band-co">Us</td>'
                f'<td class="band-note" colspan="{len(CAPABILITY_LABELS)}">'
                f'Not built. A design intention, not an observation.</td></tr>')
    body.append(f'<tr class="us"><td class="co"><span class="nm">{escape(PROPOSED["name"])}</span>'
                f'<span class="sub">proposed</span></td>'
                f'{cells_for(PROPOSED, empty)}</tr>')

    labels = dict(CAPABILITY_LABELS)
    empty_names = [labels[k].replace("<br>", " ") for k in empty]
    empty_line = (
        f'<b>{len(empty)} column{"s" if len(empty) != 1 else ""} nobody in this trade '
        f'occupies:</b> ' + ", ".join(f"<b>{escape(n)}</b>" for n in empty_names) + "."
        if empty else
        "<b>Every capability here is occupied by somebody in this trade.</b> "
        "That is a finding, and not a comfortable one.")

    n_analogue = sum(1 for r in rows if r.get("relationship") == "analogue")
    remote_elsewhere = [r["name"] for r in rows
                        if r.get("relationship") == "analogue" and "remote_capture" in r["have"]]
    total_rev = sum(int(r.get("revenue_usd") or 0) for r in in_trade)
    priced = [r for r in in_trade if int(r.get("revenue_usd") or 0)]

    html = f"""<meta charset="utf-8">
<title>Who Does What in Blinds Software</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>{CSS}</style>
<div class="wrap">

<h1>Who does what in blinds software</h1>
<p class="dek">Ten jobs sit between a customer wanting a blind and a machine cutting one. Here
is who does each &mdash; grouped by what each company actually is to us, because most of them
are not competitors. The columns that come out empty are the reason this page exists.</p>
<p class="gen">Generated by scripts/research/build_capability_matrix_page.py from
outreach/companies.md &middot; {len(in_trade)} in-trade companies, {n_analogue} analogues from
other trades &middot; do not edit this file</p>

<hr class="rule">

<div class="sec">
<h2>01 &middot; The matrix</h2>
<p class="lede">Within each band, largest revenue first. Figures marked <code>estimate</code>
come from aggregators with no filing behind them &mdash; read those as bands, not numbers.
Analogues are scored on the same ten axes even though they sell into other trades; that is
the comparison, not a category error.</p>
<div class="scroll">
<table>
<thead><tr><th class="co">Company</th>{head}</tr></thead>
<tbody>{"".join(body)}</tbody>
</table>
</div>
<ul class="legend">
  <li><span class="mark yes">&#10003;</span> ships it</li>
  <li><span class="mark part">&#9683;</span> partial or unconfirmed</li>
  <li><span class="mark non">&ndash;</span> does not</li>
  <li><span style="display:inline-block;width:16px;height:12px;background:var(--accent-wash);border:1px solid var(--accent)"></span> empty among in-trade companies</li>
</ul>
<div class="note">{empty_line} And the left-hand one is <b>not</b> empty among the analogues
&mdash; {escape(", ".join(remote_elsewhere))} all capture without a person on site, in their
own trades. The job is removable. Nobody has removed it here.</div>
</div>

<div class="sec">
<h2>02 &middot; What the money says</h2>
<div class="cards">
  <div class="card"><h3><span class="big">{money(str(total_rev))}</span> in-trade revenue</h3>
    <p>Across the {len(priced)} in-trade companies with any revenue figure at all. Software for
    made-to-order home products is a real market, and none of that revenue comes from measuring
    anything.</p></div>
  <div class="card"><h3><span class="big">$9&ndash;$87</span> per measurement report</h3>
    <p>EagleView&rsquo;s published 2026 residential pricing, in roofing. The comparable
    window-covering figure on file is <b>$225 for one measuring visit</b> (E8).</p></div>
  <div class="card"><h3><span class="big">1983</span> oldest incumbent</h3>
    <p>Windowmaker has sold measuring software into the window trade for forty-three years,
    and a person is still on the ladder.</p></div>
</div>
</div>

<div class="sec">
<h2>03 &middot; Reading the two empty ends</h2>
<div class="note warm"><b>Left end &mdash; capture.</b> Every in-trade product begins after a
human has arrived with numbers. The on-site apps make the recording better: laser pairing,
cross-validating readings, deriving frame sizes from clearances. None removes the person.
Forty-three years of that is either proof the visit cannot be removed at the accuracy this
trade needs, or proof that nobody holding that distribution ever tried. A website cannot tell
you which, and failed attempts do not publish.</div>
<div class="note"><b>Right end &mdash; across shops.</b> The fulfilment stack is solved
<i>inside one building</i>: order in, deductions applied, cut list out to the cutting table by
XML or CSV. Nothing reads a machine back, and nothing routes a job to a different shop. An ERP
in every shop is the precondition for routing, not a competitor to it.</div>
<div class="note warm"><b>Read the bands, not just the marks.</b> Capability and relationship
are independent, and the table is only honest with both on it. The most capable in-trade
company is <i>rails</i> &mdash; we integrate into it rather than beat it. The only true
competitor ships fewer capabilities than three companies below it. And the platform risk is not
that Cyncly out-builds us; it is that an ERP the shop already pays for bundles a mediocre
capture, because good-enough-and-included beats better-and-another-invoice. The defence is to
be in the catalogue before someone builds against us.</div>
</div>

</div>
"""
    OUT.write_text(html, encoding="utf-8")
    return OUT


if __name__ == "__main__":
    out = build()
    print(f"[ok] wrote {out.relative_to(REPO)}")
