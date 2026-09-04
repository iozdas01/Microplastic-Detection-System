"""Render the progress log as a page — the Truth line first, because it is the one that matters.

The log's value is the diff on one line across days, and that diff is invisible in a markdown
file where Truth sits as the first of five equal-looking fields. Here every entry leads with
its Truth, and a Truth that changed from the day before is marked, so a stall (same question,
nothing learned, days running) and progress (question moved, evidence moved it) look different
at a glance instead of requiring a careful read.

Authored in reports/{slug}/progress-log.md — appended by /startup-daily-log, never here.

    .venv/bin/python scripts/research/build_progress_log_page.py
"""
from __future__ import annotations

import re
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import PAGES, ROOT, log  # noqa: E402
from page_kit import esc  # noqa: E402

SRC = ROOT / "reports/high-mix-manufacturing/progress-log.md"
OUT = PAGES / "progress-log.html"
FIELDS = ["Truth", "Moved", "Learned", "Next", "Parked"]


def parse(text: str) -> list[dict]:
    body = text.split("## Entries", 1)[-1]
    entries = []
    for chunk in re.split(r"\n### ", body):
        chunk = chunk.strip()
        m = re.match(r"(\d{4}-\d{2}-\d{2})", chunk)
        if not m:
            continue
        entry = {"date": m.group(1), "fields": {}, "extra": []}
        for para in re.split(r"\n\s*\n", chunk[len(m.group(1)):]):
            para = " ".join(para.split())
            fm = re.match(r"\*\*(\w+)\*\*\s*—\s*(.*)", para)
            if fm and fm.group(1) in FIELDS:
                entry["fields"][fm.group(1)] = fm.group(2)
            elif para.startswith("**"):
                entry["extra"].append(para)
        entries.append(entry)
    return entries


def inline(s: str) -> str:
    """Markdown bold and backticks only — the log is prose, not a document format."""
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s


def main() -> int:
    if not SRC.exists():
        log("build_progress_log_page: no progress-log.md yet")
        return 1
    entries = parse(SRC.read_text(encoding="utf-8"))
    if not entries:
        log("build_progress_log_page: no entries parsed")
        return 1

    rows = []
    prev_truth = None
    for e in reversed(entries):  # newest first
        truth = e["fields"].get("Truth", "")
        changed = prev_truth is not None and truth.strip() != prev_truth.strip()
        first = prev_truth is None
        mark = ('<span class="flag moved">Truth changed</span>' if changed else
                '' if first else '<span class="flag same">same question</span>')
        prev_truth = truth
        other = "".join(
            f'<div class="f"><span class="k">{k}</span><p>{inline(e["fields"][k])}</p></div>'
            for k in FIELDS[1:] if e["fields"].get(k))
        extra = "".join(f'<p class="extra">{inline(x)}</p>' for x in e["extra"])
        rows.append(f"""  <article>
    <header><h2>{esc(e['date'])}</h2>{mark}</header>
    <div class="truth"><span class="k">Truth</span><p>{inline(truth)}</p></div>
    {other}{extra}
  </article>""")

    # Newest first on the page, so the flag on each entry compares it to the day BELOW it.
    html = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Progress log — high-mix-manufacturing</title>
<style>
  :root {{ --ink:#14161a; --mut:#606874; --line:#e3e6ea; --bg:#f6f7f8; --card:#fff;
    --hot:#8a3312; --hot-bg:#fbeae2; --calm:#4b5563; --calm-bg:#eef0f3; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--ink);
    font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif; }}
  main {{ max-width:820px; margin:0 auto; padding:34px 22px 60px; }}
  h1 {{ font-size:22px; margin:0 0 4px; }}
  .sub {{ color:var(--mut); font-size:13px; margin:0 0 26px; }}
  article {{ background:var(--card); border:1px solid var(--line); border-radius:6px;
    padding:18px 20px; margin-bottom:16px; }}
  article header {{ display:flex; align-items:center; gap:10px; margin-bottom:12px;
    border-bottom:1px solid var(--line); padding-bottom:9px; }}
  h2 {{ font-size:15px; margin:0; font-variant-numeric:tabular-nums; }}
  .flag {{ font-size:10.5px; font-weight:600; padding:2px 7px; border-radius:10px; }}
  .moved {{ color:var(--hot); background:var(--hot-bg); }}
  .same {{ color:var(--calm); background:var(--calm-bg); }}
  .truth {{ background:#f8f9fb; border-left:3px solid var(--ink); padding:10px 13px;
    margin-bottom:13px; }}
  .truth p {{ font-size:15.5px; }}
  .k {{ display:block; font-size:10px; text-transform:uppercase; letter-spacing:.1em;
    color:var(--mut); margin-bottom:3px; }}
  .f {{ margin-bottom:11px; }}
  p {{ margin:0; }}
  .f p, .extra {{ font-size:13.5px; line-height:1.5; }}
  .extra {{ margin-top:11px; padding-top:10px; border-top:1px dashed var(--line);
    color:var(--mut); }}
  code {{ background:#eef0f3; padding:1px 4px; border-radius:3px; font-size:.9em; }}
  footer {{ color:var(--mut); font-size:11.5px; margin-top:22px; }}
</style>

<main>
  <h1>Progress log</h1>
  <p class="sub">Newest first. The flag compares each day's Truth to the entry below it — the
  diff on that one line is the whole instrument.</p>

{chr(10).join(rows)}

  <footer>Authored in reports/high-mix-manufacturing/progress-log.md via
  /startup-daily-log. Generated by scripts/research/build_progress_log_page.py.</footer>
</main>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html)
    log(f"  {OUT.relative_to(ROOT)} written ({len(entries)} entries, {len(html):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
