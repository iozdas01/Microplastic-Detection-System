"""The startup scene on one page — quiet at rest, everything on click.

Continues the map begun under the manufacturing-execution-layer idea. The organising axis is
the founder's own: `liability_taken`. Their note in companies.md says why —

    "Read the map by that column: if the `owns_outcome` lane holds only companies that own
     their own factory, and every `software_only` entry is `none`, that is the belief's claim
     rendered — nobody sells a tool into the prove-out job while carrying the first-run risk."

So the lanes are liability, left to right, and the page is arranged to make an empty lane
visible rather than to fill the screen. A card shows four things at rest; everything else is
one click away, because a landscape you cannot scan is not a landscape.

    python scripts/research/build_startup_map_page.py
"""
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLUG = "high-mix-manufacturing"
SRC = ROOT / f"reports/{SLUG}/outreach/companies.md"
OUT = ROOT / f"reports/{SLUG}/pages/startup-map.html"

LANES = [
    ("none", "No liability", "Sells a licence. The customer carries the first run."),
    ("warranty", "Warranty", "Stands behind the product, not the outcome."),
    ("rework_credit", "Rework credit", "Pays to redo it, but not for what it cost you."),
    ("part_guarantee", "Part guarantee", "Commits to the part inside a published, bounded envelope."),
    ("owns_outcome", "Owns the outcome", "Commits to a custom part with no published envelope. Scoping the job is part of what they carry."),
]
STAGE_LABEL = {
    "pre_seed": "Pre-seed", "seed": "Seed", "series_a": "Series A", "series_b": "Series B",
    "series_c": "Series C", "series_d_plus": "Series D+", "public": "Public",
    "incumbent_subsidiary": "Incumbent subsidiary",
}


def parse() -> list[dict]:
    text = SRC.read_text(encoding="utf-8")
    out = []
    for block in text.split("\n## ")[1:]:
        name, _, body = block.partition("\n")
        rec = {"name": name.strip()}
        # scalar fields
        for m in re.finditer(r"^([a-z_]+): (?!>)(.*)$", body, re.M):
            rec[m.group(1)] = m.group(2).strip().strip('"')
        # folded blocks
        for m in re.finditer(r"^([a-z_]+): >\n((?:[ ]{2,}.*\n?)+)", body, re.M):
            rec[m.group(1)] = " ".join(m.group(2).split())
        if rec.get("map") == "startup":
            out.append(rec)
    return out


def money(v: str) -> str:
    try:
        n = int(v)
    except (TypeError, ValueError):
        return ""
    if n >= 1_000_000_000:
        return f"${n/1e9:.1f}bn"
    if n >= 1_000_000:
        return f"${n/1e6:.0f}m"
    return f"${n:,}"


CSS = """
:root{--bg:#fbfaf8;--fg:#17161a;--mut:#6d6a73;--faint:#9b98a2;--line:#e6e2dc;--card:#fff;
--accent:#1f4f7a;--empty:#b9b4ae}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font:16px/1.6 ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:1080px;margin:0 auto;padding:60px 24px 120px}
h1{font-size:31px;letter-spacing:-.025em;margin:0 0 10px;font-weight:650}
.dek{color:var(--mut);margin:0 0 6px;max-width:66ch}
.gen{color:var(--faint);font-size:12.5px;margin:0 0 44px}
.lane{margin:0 0 44px}
.lh{display:flex;align-items:baseline;gap:12px;margin-bottom:3px}
.lt{font-size:19px;font-weight:650;letter-spacing:-.015em}
.lc{font-size:12px;color:var(--faint);font-family:ui-monospace,Menlo,monospace}
.ld{color:var(--mut);font-size:14.5px;margin:0 0 16px;max-width:70ch}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px}
.c{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:16px 18px;
cursor:pointer;transition:border-color .12s,box-shadow .12s}
.c:hover{border-color:var(--accent)}
.c.open{border-color:var(--accent);box-shadow:0 0 0 3px rgba(31,79,122,.07);
grid-column:1/-1;cursor:default}
.cn{font-size:17px;font-weight:650;letter-spacing:-.01em;margin-bottom:3px}
.cmeta{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:9px}
.st{font-size:10.5px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;
padding:2px 7px;border-radius:4px;background:#eef1f5;color:var(--accent)}
.raise{font-size:12.5px;color:var(--mut);font-family:ui-monospace,Menlo,monospace}
.cs{color:var(--mut);font-size:13.5px;line-height:1.5}
.c:not(.open) .cs{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.detail{display:none;margin-top:16px;padding-top:16px;border-top:1px solid var(--line)}
.c.open .detail{display:block}
dl{display:grid;grid-template-columns:150px 1fr;gap:9px 18px;margin:0;font-size:14.5px}
dt{color:var(--faint);font-size:11px;text-transform:uppercase;letter-spacing:.08em;padding-top:3px}
dd{margin:0;color:var(--mut)}
dd b{color:var(--fg);font-weight:600}
dd a{color:var(--accent)}
.empty{border:2px dashed var(--line);border-radius:11px;padding:26px;text-align:center;
color:var(--empty);font-size:15px}
.note{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--accent);
border-radius:0 11px 11px 0;padding:18px 22px;margin:0 0 44px;font-size:15px;color:var(--mut)}
.note b{color:var(--fg)}
.gapbox{border:2px dashed var(--line);border-radius:11px;padding:26px 24px;margin-top:8px}
.gapbox b{display:block;font-size:18px;color:var(--fg);margin-bottom:8px}
.gapbox p{margin:0;color:var(--mut);font-size:14.5px;max-width:70ch}
@media(max-width:640px){dl{grid-template-columns:1fr}dt{padding-top:11px}}
@media(prefers-color-scheme:dark){
:root{--bg:#141317;--fg:#eceaf0;--mut:#9d99a6;--faint:#6f6b77;--line:#2c2933;--card:#1c1b21;
--accent:#84b8e0;--empty:#4a4653}
.st{background:#1f2b36}}
"""

JS = """
document.addEventListener('click',e=>{
 const c=e.target.closest('.c'); if(!c) return;
 if(c.classList.contains('open') && e.target.closest('.detail')) return;
 const wasOpen=c.classList.contains('open');
 document.querySelectorAll('.c.open').forEach(o=>o.classList.remove('open'));
 if(!wasOpen) c.classList.add('open');
});
document.addEventListener('keydown',e=>{if(e.key==='Escape')
 document.querySelectorAll('.c.open').forEach(o=>o.classList.remove('open'));});
"""


def card(r: dict) -> str:
    stage = STAGE_LABEL.get(r.get("stage", ""), r.get("stage") or "stage unknown")
    raised = money(r.get("total_raised_usd", ""))
    rows = []

    def row(label, val, strong=False):
        if val:
            v = f"<b>{html.escape(val)}</b>" if strong else html.escape(val)
            rows.append(f"<dt>{label}</dt><dd>{v}</dd>")

    row("What they sell", r.get("sector", ""), True)
    row("Job covered", (r.get("job_covered") or "").replace("_", " "))
    row("Integration", (r.get("integration") or "").replace("_", " "))
    row("Sells to", (r.get("sells_to") or "").replace("_", " "))
    row("Headcount", r.get("headcount", ""))
    row("Founded", r.get("founded", ""))
    row("Country", r.get("country", ""))
    if r.get("makes_or_does"):
        row("What it actually is", r["makes_or_does"])
    if r.get("hmlv_relevance"):
        rows.append(f"<dt>Why it matters</dt><dd><b>{html.escape(r['hmlv_relevance'])}</b></dd>")
    if r.get("liability_notes"):
        row("Liability", r["liability_notes"])
    if r.get("funding_notes"):
        row("Funding", r["funding_notes"])
    if r.get("source_url"):
        u = html.escape(r["source_url"], quote=True)
        rows.append(f'<dt>Source</dt><dd><a href="{u}" target="_blank" rel="noopener">{u}</a></dd>')

    return f"""<div class="c">
 <div class="cn">{html.escape(r['name'])}</div>
 <div class="cmeta"><span class="st">{html.escape(stage)}</span>
  {f'<span class="raise">{raised} raised</span>' if raised else ''}</div>
 <div class="cs">{html.escape(r.get('sector',''))}</div>
 <div class="detail"><dl>{''.join(rows)}</dl></div>
</div>"""


def build() -> Path:
    recs = parse()
    by_lane = {k: [r for r in recs if r.get("liability_taken") == k] for k, _, _ in LANES}
    unmapped = [r for r in recs if r.get("liability_taken") not in by_lane]

    lanes_html = []
    for key, title, desc in LANES:
        rs = sorted(by_lane[key], key=lambda x: x["name"].lower())
        body = ("".join(card(r) for r in rs) if rs else "")
        inner = (f'<div class="grid">{body}</div>' if rs
                 else '<div class="empty">Nobody. This lane is empty.</div>')
        lanes_html.append(f"""<div class="lane">
 <div class="lh"><span class="lt">{title}</span><span class="lc">{key} · {len(rs)}</span></div>
 <p class="ld">{desc}</p>
 {inner}
</div>""")
    if unmapped:
        lanes_html.append(f"""<div class="lane">
 <div class="lh"><span class="lt">Ungraded</span><span class="lc">{len(unmapped)}</span></div>
 <p class="ld">No liability grade recorded yet. Counted as missing data, not as zero.</p>
 <div class="grid">{"".join(card(r) for r in unmapped)}</div>
</div>""")

    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Startup Map</title><style>{CSS}</style></head><body><div class="wrap">

<h1>Who else is doing this</h1>
<p class="dek">{len(recs)} startups, arranged by how much risk they actually take on the
outcome. Click any card for the detail; press Escape to close.</p>
<p class="gen">Generated from outreach/companies.md by
scripts/research/build_startup_map_page.py — do not edit this file.</p>

<div class="note"><b>Why the lanes are liability and not sector.</b> Sector puts rivals next to
each other; liability answers the question the belief actually asks. If every
<code>software_only</code> company sits in “no liability”, and the only companies owning the
outcome are the ones that own a factory, then <b>nobody sells a tool into this job while
carrying the risk of it being wrong</b> — which is the claim, rendered rather than argued.</div>

{"".join(lanes_html)}

<div class="lane">
<div class="lh"><span class="lt">The gap in this map</span></div>
<div class="gapbox"><b>Not one of these is a window-covering company.</b>
<p>Every entry here was researched under the CNC-machining and prove-out thesis, and the axes
were drawn for that question. The active hunch is now H3 — made-to-measure window coverings —
and the players that matter for it are absent: Hunter Douglas, Springs Window Fashions,
Budget Blinds, 3 Day Blinds, Blinds.com, SelectBlinds, Stoneside. Mapping them is what
continuing this map means, and the <code>liability_taken</code> axis transfers unchanged: a
fit guarantee that pays for the customer's own measuring error is an <code>owns_outcome</code>
commitment, and it is already being given away at checkout.</p></div>
</div>

</div><script>{JS}</script></body></html>"""
    OUT.write_text(doc, encoding="utf-8")
    return OUT


if __name__ == "__main__":
    p = build()
    print(f"[ok] wrote {p.relative_to(ROOT)} ({len(parse())} startups)")
