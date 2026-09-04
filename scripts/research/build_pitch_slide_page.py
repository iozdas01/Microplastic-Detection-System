"""Render the pitch as one slide — the EF Form SCI submission format.

The five fields the form asks for (one-liner, problem, solution, team, market) plus the open
questions, because the brief says gaps are expected and that trying to paper over them is what
the panel sees through. Authored in the `slide:` block of
`outreach/copy/H3-discovery-pitch.md`; this only renders it, so the pitch has one author and
the slide cannot drift from it.

Fixed 16:9. Cmd-P gives exactly one landscape page with no browser furniture, which is the
artefact the form wants uploaded.

    .venv/bin/python scripts/research/build_pitch_slide_page.py
"""
from __future__ import annotations

import re
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import PAGES, ROOT, log  # noqa: E402
from page_kit import esc  # noqa: E402

import yaml  # noqa: E402

SRC = ROOT / "reports/high-mix-manufacturing/outreach/copy/H3-discovery-pitch.md"
OUT = PAGES / "pitch-slide.html"

# Where a claim comes from. Colour is doing real work here: on a slide read by someone
# deciding whether to believe you, "a customer said this" and "we think this" must not look
# the same. Anything with no badge is a statement about intent, which needs no source.
BADGE = {
    "ledger": ("said in a call / measured", "cite-ledger"),
    "recon":  ("public source", "cite-recon"),
    "edge":   ("about us", "cite-edge"),
    "lineage": ("our claim, untested", "cite-open"),
}


def badge(cite: str | None):
    if not cite:
        return ""
    ids = [c.strip() for c in str(cite).split(",") if c.strip()]
    kind = "ledger" if any(re.fullmatch(r"E\d+", i) for i in ids) else ids[0]
    label, cls = BADGE.get(kind, BADGE["ledger"])
    shown = " ".join(i for i in ids if re.fullmatch(r"E\d+", i)) or label
    return f'<span class="cite {cls}" title="{esc(label)}">{esc(shown)}</span>'


def items(rows) -> str:
    out = []
    for r in rows or []:
        if isinstance(r, str):
            r = {"text": r}
        out.append(f'<li>{esc(r["text"])} {badge(r.get("cite"))}</li>')
    return "\n".join(out)


def main() -> int:
    text = SRC.read_text(encoding="utf-8")
    blocks = re.findall(r"```yaml\n(.*?)\n```", text, re.S)
    slide = None
    for b in blocks:
        try:
            data = yaml.safe_load(b)
        except yaml.YAMLError:
            continue
        if isinstance(data, dict) and data.get("slide"):
            slide = data["slide"]
    if not slide:
        log(f"build_pitch_slide_page: no `slide:` block in {SRC.name}")
        return 1

    html = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pitch slide — {esc(slide.get('event', 'one slide'))}</title>
<style>
  :root {{
    --ink:#14161a; --mut:#5d646e; --line:#e2e5ea; --bg:#f4f5f7; --card:#fff;
    --ledger:#0b6b4f; --ledger-bg:#e3f3ec; --recon:#7a5a12; --recon-bg:#faf0d8;
    --edge:#1f4f8f; --edge-bg:#e6eefa; --open:#8a3312; --open-bg:#fbe9e2;
  }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--ink);
    font:14px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif; }}
  .wrap {{ padding:24px; display:flex; justify-content:center; }}
  .slide {{ width:1280px; height:720px; background:var(--card); padding:34px 40px 28px;
    display:flex; flex-direction:column; box-shadow:0 2px 18px rgba(0,0,0,.13);
    border-radius:4px; }}
  header {{ display:flex; justify-content:space-between; align-items:baseline;
    border-bottom:2px solid var(--ink); padding-bottom:9px; margin-bottom:14px; }}
  h1 {{ font-size:25px; margin:0; letter-spacing:-.3px; }}
  .meta {{ font-size:11px; color:var(--mut); text-align:right; line-height:1.4; }}
  .one {{ font-size:15.5px; line-height:1.4; margin:0 0 13px; padding:9px 13px;
    background:#f7f9fb; border-left:3px solid var(--ink); }}
  .cols {{ display:grid; grid-template-columns:1.3fr 1fr 0.92fr 1.02fr; gap:18px;
    flex:1; min-height:0; }}
  h2 {{ font-size:10px; text-transform:uppercase; letter-spacing:.11em; color:var(--mut);
    margin:0 0 7px; padding-bottom:4px; border-bottom:1px solid var(--line); }}
  .lead {{ margin:0 0 8px; font-size:12.2px; line-height:1.44; }}
  ul {{ margin:0; padding-left:14px; }}
  li {{ font-size:11.4px; line-height:1.4; margin-bottom:5.5px; }}
  .stack > * + * {{ margin-top:13px; }}
  .cite {{ display:inline-block; font-size:9px; font-weight:600; padding:.5px 4px;
    border-radius:3px; vertical-align:1px; white-space:nowrap; }}
  .cite-ledger {{ color:var(--ledger); background:var(--ledger-bg); }}
  .cite-recon  {{ color:var(--recon);  background:var(--recon-bg); }}
  .cite-edge   {{ color:var(--edge);   background:var(--edge-bg); }}
  .cite-open   {{ color:var(--open);   background:var(--open-bg); }}
  .open {{ margin-top:13px; padding:10px 13px; background:#fdf6f3;
    border:1px solid #f2d9cf; border-radius:3px; }}
  .open h2 {{ color:var(--open); border-bottom-color:#f2d9cf; }}
  .open ul {{ columns:2; column-gap:26px; }}
  .open li {{ break-inside:avoid; }}
  footer {{ margin-top:10px; font-size:9.5px; color:var(--mut);
    display:flex; justify-content:space-between; }}
  #overflow {{ display:none; position:fixed; top:0; left:0; right:0; z-index:9;
    background:#b3261e; color:#fff; padding:7px 14px; font-size:12px; font-weight:600; }}
  @media print {{
    @page {{ size:1280px 720px; margin:0; }}
    body {{ background:#fff; }} .wrap {{ padding:0; }}
    .slide {{ box-shadow:none; border-radius:0; }}
  }}
</style>

<div id="overflow"></div>
<div class="wrap"><div class="slide">
  <header>
    <h1>{esc(slide.get('headline', ''))}</h1>
    <div class="meta">{esc(slide.get('event', ''))}<br>due {esc(slide.get('due', ''))}</div>
  </header>

  <p class="one">{esc(slide.get('one_liner', ''))}</p>

  <div class="cols">
    <section>
      <h2>Problem</h2>
      <p class="lead">{esc((slide.get('problem') or {}).get('lead', ''))}</p>
      <ul>
{items((slide.get('problem') or {}).get('learned'))}
      </ul>
    </section>

    <section>
      <h2>Solution</h2>
      <p class="lead">{esc((slide.get('solution') or {}).get('lead', ''))}</p>
      <ul>
{items((slide.get('solution') or {}).get('points'))}
      </ul>
    </section>

    <section>
      <h2>Team</h2>
      <ul>
{items(slide.get('team'))}
      </ul>
    </section>

    <section>
      <h2>Market</h2>
      <ul>
{items(slide.get('market'))}
      </ul>
    </section>
  </div>

  <div class="open">
    <h2>What we do not know yet</h2>
    <ul>
{items(slide.get('open_questions'))}
    </ul>
  </div>

  <footer>
    <span>Green = someone told us or we measured it · blue = about us ·
      amber = public source · red = our claim, untested</span>
    <span>Generated by scripts/research/build_pitch_slide_page.py</span>
  </footer>
</div></div>

<script>
  // The slide is a fixed 16:9 box, so anything that does not fit is simply not there.
  // Measure the three columns against the space the grid actually gave them and say so.
  (function () {{
    var over = [].slice.call(document.querySelectorAll('.cols section, .open'))
      .filter(function (el) {{ return el.scrollHeight - el.clientHeight > 1; }});
    var cols = document.querySelector('.cols');
    if (cols && cols.scrollHeight - cols.clientHeight > 1) over.push(cols);
    if (!over.length) return;
    var b = document.getElementById('overflow');
    b.textContent = 'Content is overflowing the slide and is being clipped — trim the '
      + 'slide: block in outreach/copy/H3-discovery-pitch.md and rebuild.';
    b.style.display = 'block';
  }})();
</script>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html)
    log(f"  {OUT.relative_to(ROOT)} written ({len(html):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
