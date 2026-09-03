"""Build the researcher-email send sheet from the campaign's own files.

The email copy has exactly one author — `outreach/email/{campaign}/drafts.md` — and the
target state has exactly one author — `targets.csv`. This script restates neither: it parses
both and renders a working surface the founder can actually send from, with the subject and
body copyable in one click and the sent-state kept in the browser.

Rerun after any edit to the drafts or the targets; never hand-edit the output.

    python3 scripts/research/build_send_sheet.py {slug} [campaign]
"""
from __future__ import annotations

import csv
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def parse_drafts(path: Path) -> dict[str, dict]:
    """One entry per `## A1 · Name — Org · `email`` block, keyed by its draft ref."""
    text = path.read_text(encoding="utf-8")
    drafts: dict[str, dict] = {}
    # Split on the draft headings only — tier headings are `# TIER A`, one hash.
    parts = re.split(r"\n## ([AB]\d+) · ([^\n]+)\n", text)
    for i in range(1, len(parts), 3):
        ref, heading, body = parts[i], parts[i + 1], parts[i + 2]
        subject = ""
        m = re.search(r"\*\*Subject:\*\*\s*(.+)", body)
        if m:
            subject = m.group(1).strip()
        # The email itself is the blockquote run.
        quoted = [ln[2:] if ln.startswith("> ") else "" for ln in body.splitlines()
                  if ln.startswith(">")]
        # Collapse the leading/trailing blanks the markdown quoting introduces.
        while quoted and not quoted[0]:
            quoted.pop(0)
        while quoted and not quoted[-1]:
            quoted.pop()
        # The markdown hard-wraps the blockquote at ~90 chars; an email client should do its
        # own wrapping, so rejoin each paragraph into one line and keep only the blank-line
        # breaks. Pasting the wrapped version is what makes a hand-written email look bulk-sent.
        paras, cur = [], []
        for ln in quoted:
            if ln.strip():
                cur.append(ln.strip())
            elif cur:
                paras.append(" ".join(cur)); cur = []
        if cur:
            paras.append(" ".join(cur))
        papers = re.findall(r"https://arxiv\.org/abs/([0-9.]+)", body)
        why = ""
        m = re.search(r"^(Why[^:]*):\s*(.+?)(?=\n\n|\n\*\*)", body, re.S | re.M)
        if m:
            # Keep the label. The drafts continue the sentence after the colon
            # ("Why: he is a founder..."), so dropping it strands a lowercase clause.
            why = f"{m.group(1)} - " + " ".join(m.group(2).split())
        drafts[ref] = {
            "ref": ref, "heading": heading.strip(), "subject": subject,
            "body": "\n\n".join(paras), "papers": sorted(set(papers)), "why": why,
        }
    return drafts


def load_targets(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


CSS = """
:root{--bg:#faf9f7;--fg:#1b1a18;--mut:#6b6862;--line:#e2ded7;--card:#fff;
--a:#8a4b1e;--aw:#fdf3e9;--b:#2f5d50;--btn:#fff}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font:15px/1.6 ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif}
.wrap{max-width:920px;margin:0 auto;padding:40px 22px 100px}
h1{font-size:27px;margin:0 0 6px;letter-spacing:-.02em}
.sub{color:var(--mut);margin:0 0 28px;font-size:14px}
.plan{background:var(--card);border:1px solid var(--line);border-radius:10px;
padding:18px 20px;margin-bottom:34px}
.plan h2{font-size:14px;text-transform:uppercase;letter-spacing:.07em;color:var(--mut);margin:0 0 10px}
.plan ol{margin:0;padding-left:20px}.plan li{margin:5px 0}
.tier{font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:var(--mut);
margin:34px 0 14px;border-bottom:1px solid var(--line);padding-bottom:7px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;
margin-bottom:18px;overflow:hidden}
.card.done{opacity:.5}
.hd{display:flex;gap:12px;align-items:flex-start;padding:15px 18px;border-bottom:1px solid var(--line)}
.hd .who{flex:1;min-width:0}
.name{font-weight:650;font-size:15.5px}
.org{color:var(--mut);font-size:13px}
.mail{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;color:var(--a);
word-break:break-all}
.ref{background:var(--aw);color:var(--a);border-radius:5px;padding:2px 7px;font-size:11px;
font-weight:700;letter-spacing:.04em;flex:none}
.why{padding:11px 18px;font-size:13px;color:var(--mut);background:#fcfbf9;
border-bottom:1px solid var(--line)}
.subj{padding:13px 18px 0;font-size:14px}
.subj b{color:var(--mut);font-weight:600;font-size:11.5px;text-transform:uppercase;
letter-spacing:.07em;display:block;margin-bottom:3px}
pre{margin:11px 18px;padding:15px;background:#fbfaf8;border:1px solid var(--line);
border-radius:7px;white-space:pre-wrap;font:13.5px/1.62 ui-monospace,SFMono-Regular,Menlo,monospace;
overflow-x:auto}
.acts{display:flex;flex-wrap:wrap;gap:8px;padding:0 18px 16px;align-items:center}
button,a.btn{font:inherit;font-size:13px;padding:6px 13px;border-radius:6px;
border:1px solid var(--line);background:var(--btn);color:var(--fg);cursor:pointer;text-decoration:none}
button:hover,a.btn:hover{background:var(--aw);border-color:var(--a);color:var(--a)}
label.sent{margin-left:auto;font-size:13px;color:var(--mut);cursor:pointer;
display:flex;gap:6px;align-items:center}
.paper{font-size:12.5px;color:var(--mut)}
.paper a{color:var(--b)}
.note{background:var(--aw);border-left:3px solid var(--a);padding:13px 16px;border-radius:0 7px 7px 0;
margin-bottom:28px;font-size:13.5px}
@media(prefers-color-scheme:dark){
:root{--bg:#16151a;--fg:#eceaf0;--mut:#9d99a6;--line:#312e38;--card:#1e1d24;
--a:#e0a06a;--aw:#2b2119;--b:#8fc4b0;--btn:#282730}
pre{background:#191820}.why{background:#1a1920}}
"""

JS = """
const K='sendsheet.high-mix.v1';
const st=JSON.parse(localStorage.getItem(K)||'{}');
function paint(){document.querySelectorAll('.card').forEach(c=>{
 const r=c.dataset.ref;const b=st[r];c.classList.toggle('done',!!b);
 const cb=c.querySelector('input');if(cb)cb.checked=!!b;});
 const n=Object.values(st).filter(Boolean).length;
 document.getElementById('cnt').textContent=n;}
document.addEventListener('change',e=>{if(e.target.matches('.card input')){
 st[e.target.closest('.card').dataset.ref]=e.target.checked;
 localStorage.setItem(K,JSON.stringify(st));paint();}});
document.addEventListener('click',e=>{const b=e.target.closest('[data-copy]');if(!b)return;
 const c=b.closest('.card');const what=b.dataset.copy;
 const txt=what==='subject'?c.dataset.subject:c.querySelector('pre').textContent;
 navigator.clipboard.writeText(txt).then(()=>{const o=b.textContent;
  b.textContent='copied';setTimeout(()=>b.textContent=o,1100);});});
paint();
"""


def build(slug: str, campaign: str) -> Path:
    base = ROOT / "reports" / slug / "outreach" / "email" / campaign
    drafts = parse_drafts(base / "drafts.md")
    targets = load_targets(base / "targets.csv")

    # One card per DRAFT, addressed to every target that points at it.
    by_ref: dict[str, list[dict]] = {}
    for t in targets:
        ref = (t.get("draft_ref") or "").strip()
        if ref in drafts:
            by_ref.setdefault(ref, []).append(t)

    rows: list[str] = []
    for tier in ("A", "B"):
        refs = sorted((r for r in drafts if r.startswith(tier)),
                      key=lambda r: int(r[1:]))
        if not refs:
            continue
        label = ("Tier A — send first, as one wave" if tier == "A"
                 else "Tier B — send 48 hours later, regardless of replies")
        rows.append(f'<div class="tier">{html.escape(label)}</div>')
        for ref in refs:
            d = drafts[ref]
            tg = by_ref.get(ref, [])
            to = ", ".join(t["email"] for t in tg if t["email"]) or "—"
            name = tg[0]["name"] if tg else d["heading"].split("—")[0].strip()
            org = tg[0]["org"] if tg else ""
            subj = d["subject"]
            mailto = (f"mailto:{to.split(',')[0].strip()}"
                      f"?subject={html.escape(subj, quote=True).replace(' ', '%20')}")
            papers = " · ".join(
                f'<a href="https://arxiv.org/abs/{p}" target="_blank" rel="noopener">arXiv {p}</a>'
                for p in d["papers"])
            rows.append(f"""<div class="card" data-ref="{ref}" data-subject="{html.escape(subj, quote=True)}">
 <div class="hd"><span class="ref">{ref}</span><div class="who">
  <div class="name">{html.escape(name)}</div>
  <div class="org">{html.escape(org)}</div>
  <div class="mail">{html.escape(to)}</div></div></div>
 {f'<div class="why">{html.escape(d["why"])}</div>' if d["why"] else ""}
 <div class="subj"><b>Subject</b>{html.escape(subj)}</div>
 <pre>{html.escape(d["body"])}</pre>
 <div class="acts">
  <button data-copy="subject">copy subject</button>
  <button data-copy="body">copy email</button>
  <a class="btn" href="{mailto}">open in mail</a>
  <span class="paper">{papers}</span>
  <label class="sent"><input type="checkbox">sent</label>
 </div></div>""")

    n_targets = sum(1 for t in targets if t["email"])
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Researcher Send Sheet</title><style>{CSS}</style></head><body><div class="wrap">
<h1>Researcher send sheet</h1>
<p class="sub">{len(drafts)} drafts · {n_targets} contactable addresses · campaign <code>{campaign}</code>
 · <span id="cnt">0</span> marked sent</p>
<div class="note"><b>Generated from <code>drafts.md</code> and <code>targets.csv</code> —
do not edit this page.</b> Fix the source and rerun
<code>python3 scripts/research/build_send_sheet.py {slug} {campaign}</code>.
Sent-state lives in this browser only; the campaign's record of what was sent is
<code>targets.csv</code>.</div>
<div class="plan"><h2>Before the first send</h2><ol>
<li><b>Set the from address.</b> These are written to read as coming from a Cambridge address —
that is why the opener works on academics.</li>
<li><b>No scheduling link in the copy.</b> Offer times; send a link only if asked.</li>
<li><b>Send Tier A as one wave, then stop.</b> If six get no reply the opener is wrong, and you
want to learn that on six rather than on thirty.</li>
<li><b>Mind the timezone.</b> CET for KTH, Chalmers, DFKI, TUM · SGT for NTU · KST for Sling AI
and Neuromeka · ET for Sewbo, Cornell, CMU, Rice.</li>
<li><b>One address per organisation first.</b> Second authors at the same institution are held
in <code>targets.csv</code> until the first has had a week.</li>
</ol></div>
{"".join(rows)}
</div><script>{JS}</script></body></html>"""

    out = ROOT / "reports" / slug / "pages" / "outreach-send-sheet.html"
    out.write_text(doc, encoding="utf-8")
    return out


def main(argv: list[str]) -> int:
    slug = argv[0] if argv else "high-mix-manufacturing"
    campaign = argv[1] if len(argv) > 1 else "researchers-2026-09"
    out = build(slug, campaign)
    print(f"[ok] wrote {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
