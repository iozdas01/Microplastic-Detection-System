"""Inline SVG diagrams for the factory plan, drawn from the model rather than by hand.

Both figures inherit the page's foreground through `currentColor`, so they read in light
and dark alike, and reserve one hue — the alarm token — for the thing each figure argues
about: the station that actually limits the plant.
"""
from __future__ import annotations

from page_kit import Raw, esc

DEFS = """<defs>
    <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7"
            orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
    <marker id="arA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7"
            orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="var(--alarm)"/>
    </marker>
  </defs>"""

# station key -> (short name, machine, is the handoff into it done by a robot?)
SHORT = {
    "timber prep — crosscut, rip, moulder": ("Timber prep", "crosscut · rip · moulder", False),
    "5-axis joinery — legs and stiles": ("5-axis · legs", "machining centre 1", True),
    "5-axis joinery — rails, slats and keys": ("5-axis · rails", "machining centre 2", True),
    "sanding and surface prep": ("Sanding", "wide-belt + profile", True),
    "finishing — oil and cure": ("Finishing", "oil · cure racks", False),
    "QC, joint test-fit and flat-pack": ("QC + flat-pack", "no assembly here", False),
}


def process_flow(stations: list[dict], bottleneck: str) -> Raw:
    """Left-to-right station flow with cycle times, the bottleneck called out, and the
    robot transfers that make the cell autonomous shown on the arrows that have one."""
    x0, y, bw, bh, gap = 118, 168, 128, 78, 46
    parts = [DEFS]

    parts.append(f'<rect x="8" y="{y}" width="92" height="{bh}" rx="2" fill="none" '
                 f'stroke="currentColor" stroke-width="1.25" opacity="0.55"/>')
    parts.append(f'<text x="54" y="{y + 32}" text-anchor="middle" font-size="12.5" '
                 f'fill="currentColor">Kiln +</text>')
    parts.append(f'<text x="54" y="{y + 49}" text-anchor="middle" font-size="12.5" '
                 f'fill="currentColor">timber</text>')

    prev_r, last_x = 100, 100
    for i, s in enumerate(stations):
        name, machine, robot = SHORT.get(s["station"], (s["station"][:14], "", False))
        x = x0 + i * (bw + gap)
        last_x = x
        is_bn = s["station"] == bottleneck
        stroke = "var(--alarm)" if is_bn else "currentColor"
        width = "2" if is_bn else "1.25"
        parts.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="2" fill="none" '
                     f'stroke="{stroke}" stroke-width="{width}"/>')
        parts.append(f'<text x="{x + bw/2}" y="{y + 27}" text-anchor="middle" '
                     f'font-size="12.5" fill="currentColor">{esc(name)}</text>')
        parts.append(f'<text x="{x + bw/2}" y="{y + 44}" text-anchor="middle" '
                     f'font-size="9.5" fill="currentColor" opacity="0.6">{esc(machine)}</text>')
        parts.append(f'<text x="{x + bw/2}" y="{y + 66}" text-anchor="middle" '
                     f'font-size="12.5" fill="{stroke}" font-weight="600">'
                     f'{s["cycle_min_per_unit"]:.1f} min</text>')
        mid = (prev_r + x) / 2
        parts.append(f'<line x1="{prev_r + 4}" y1="{y + bh/2}" x2="{x - 6}" '
                     f'y2="{y + bh/2}" stroke="currentColor" stroke-width="1.25" '
                     f'marker-end="url(#ar)"/>')
        if robot:
            parts.append(f'<text x="{mid}" y="{y + bh/2 - 10}" text-anchor="middle" '
                         f'font-size="9.5" fill="currentColor" opacity="0.8">robot</text>')
        if is_bn:
            parts.append(f'<text x="{x + bw/2}" y="{y - 12}" text-anchor="middle" '
                         f'font-size="11.5" fill="var(--alarm)" font-weight="600">'
                         f'the constraint</text>')
        prev_r = x + bw

    ship_x = last_x + bw + gap
    parts.append(f'<line x1="{prev_r + 4}" y1="{y + bh/2}" x2="{ship_x - 6}" '
                 f'y2="{y + bh/2}" stroke="currentColor" stroke-width="1.25" '
                 f'marker-end="url(#ar)"/>')
    parts.append(f'<rect x="{ship_x}" y="{y}" width="112" height="{bh}" rx="2" fill="none" '
                 f'stroke="currentColor" stroke-width="1.25" opacity="0.55"/>')
    parts.append(f'<text x="{ship_x + 56}" y="{y + 32}" text-anchor="middle" '
                 f'font-size="12.5" fill="currentColor">Ship parts</text>')
    parts.append(f'<text x="{ship_x + 56}" y="{y + 49}" text-anchor="middle" '
                 f'font-size="10" fill="currentColor" opacity="0.6">customer assembles</text>')

    # what the robots replace, and what is still manual
    parts.append('<rect x="8" y="42" width="300" height="62" rx="2" fill="none" '
                 'stroke="currentColor" stroke-width="1.25" stroke-dasharray="5 4" '
                 'opacity="0.65"/>')
    parts.append('<text x="22" y="64" font-size="11" fill="currentColor" opacity="0.8">'
                 'THE AUTONOMY IS THE TRANSFER</text>')
    parts.append('<text x="22" y="82" font-size="11" fill="currentColor" opacity="0.7">'
                 'robots carry parts machine to machine —</text>')
    parts.append('<text x="22" y="97" font-size="11" fill="currentColor" opacity="0.7">'
                 'nothing is assembled in this building</text>')

    bx = x0 + 1 * (bw + gap)
    parts.append(f'<rect x="{bx - 24}" y="42" width="252" height="62" rx="2" fill="none" '
                 f'stroke="var(--alarm)" stroke-width="1.25" stroke-dasharray="5 4"/>')
    parts.append(f'<text x="{bx - 10}" y="64" font-size="11" fill="var(--alarm)">'
                 f'JOINT CUTTING SETS THE TAKT</text>')
    parts.append(f'<text x="{bx - 10}" y="82" font-size="11" fill="var(--alarm)" '
                 f'opacity="0.85">47 kigumi operations a chair, and the</text>')
    parts.append(f'<text x="{bx - 10}" y="97" font-size="11" fill="var(--alarm)" '
                 f'opacity="0.85">legs carry the most of them</text>')
    parts.append(f'<line x1="{bx + 64}" y1="104" x2="{bx + 64}" y2="{y - 30}" '
                 f'stroke="var(--alarm)" stroke-width="1.25" stroke-dasharray="5 4" '
                 f'marker-end="url(#arA)"/>')

    svg = (f'<svg viewBox="0 0 {ship_x + 130} 268" role="img" '
           f'aria-label="Process flow: kiln-dried timber runs through prep, two 5-axis '
           f'machining centres that cut the kigumi joints, sanding, finishing and '
           f'flat-packing. Robots carry parts between machines. The leg machining centre '
           f'has the longest cycle and sets the factory takt. No assembly station exists; '
           f'the customer assembles the chair by hand." '
           f'style="max-width:100%;height:auto">' + "".join(parts) + "</svg>")
    return Raw(
        '<figure class="bleed scroll">' + svg +
        '<figcaption>Cycle time per chair at each station, including a changeover '
        'allowance. Robots move parts between machining centres — that transfer is what '
        'makes the cell autonomous, not robotic assembly. The plant never assembles a '
        'chair: it machines, finishes, test-fits and flat-packs.</figcaption></figure>')


def floor_plan(sqft: int) -> Raw:
    """Plan view of the shell: timber in on the left, flat-packed parts out on the right."""
    W, H = 900, 440
    px, py, pw, ph = 20, 48, 860, 348
    parts = [DEFS]
    parts.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="none" '
                 f'stroke="currentColor" stroke-width="2"/>')
    parts.append(f'<text x="{px}" y="{py - 18}" font-size="12" fill="currentColor" '
                 f'opacity="0.7">{sqft:,} sq ft · owned land, three-phase service in '
                 f'place · timber in at the left, flat-packed parts out at the right</text>')

    zones = [
        (36, 64, 150, 154, "Rough timber", "racked, air-dried", False),
        (36, 232, 150, 148, "Kiln + conditioning", "6% MC, tolerance control", False),
        (206, 64, 172, 154, "Rough mill", "crosscut · rip · moulder", False),
        (206, 232, 172, 148, "Finishing + cure", "oil · racks", False),
        (398, 64, 212, 316, "5-axis joinery", "two centres, robot between", True),
        (630, 64, 232, 154, "Sanding", "wide-belt + profile", False),
        (630, 232, 232, 148, "QC, flat-pack, dock", "no assembly", False),
    ]
    for x, y, w, h, a, bl, hot in zones:
        stroke = "var(--alarm)" if hot else "currentColor"
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="none" '
                     f'stroke="{stroke}" stroke-width="{2 if hot else 1.25}" '
                     f'opacity="{1 if hot else 0.75}"/>')
        parts.append(f'<text x="{x + w/2}" y="{y + h/2 - 4}" text-anchor="middle" '
                     f'font-size="13" fill="currentColor">{esc(a)}</text>')
        parts.append(f'<text x="{x + w/2}" y="{y + h/2 + 15}" text-anchor="middle" '
                     f'font-size="10.5" fill="{stroke}" opacity="0.8">{esc(bl)}</text>')

    for x1, y1, x2, y2, label, lx, ly in [
        (186, 141, 200, 141, "boards", 190, 132),
        (292, 218, 292, 226, "blanks", 299, 226),
        (378, 141, 392, 141, "S4S", 381, 132),
        (610, 141, 624, 141, "parts", 613, 132),
        (746, 218, 746, 226, "kits", 753, 226),
    ]:
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                     f'stroke="currentColor" stroke-width="1.25" marker-end="url(#ar)"/>')
        parts.append(f'<text x="{lx}" y="{ly}" font-size="10.5" fill="currentColor" '
                     f'opacity="0.7">{esc(label)}</text>')

    # the robot that links the two machining centres
    parts.append('<circle cx="504" cy="222" r="17" fill="none" stroke="var(--alarm)" '
                 'stroke-width="1.5"/>')
    parts.append('<text x="504" y="226" text-anchor="middle" font-size="10.5" '
                 'fill="var(--alarm)">R1</text>')
    parts.append('<text x="504" y="262" text-anchor="middle" font-size="10.5" '
                 'fill="var(--alarm)" opacity="0.85">6-axis transfer</text>')

    # reserved drop-ins
    parts.append('<rect x="644" y="78" width="204" height="58" rx="2" fill="none" '
                 'stroke="currentColor" stroke-width="1.25" stroke-dasharray="5 4" '
                 'opacity="0.6"/>')
    parts.append('<text x="746" y="112" text-anchor="middle" font-size="10.5" '
                 'fill="currentColor" opacity="0.7">phase 2 · robotic sanding</text>')
    parts.append('<rect x="218" y="246" width="148" height="56" rx="2" fill="none" '
                 'stroke="currentColor" stroke-width="1.25" stroke-dasharray="5 4" '
                 'opacity="0.6"/>')
    parts.append('<text x="292" y="279" text-anchor="middle" font-size="10.5" '
                 'fill="currentColor" opacity="0.7">phase 2 · auto oil line</text>')

    svg = (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Factory floor plan: rough '
           f'timber and the kiln occupy the left of the building, the rough mill and '
           f'finishing the centre-left, two 5-axis machining centres with a robot between '
           f'them in the middle, and sanding, quality control and flat-packing on the '
           f'right beside the dock. Dashed footprints mark space reserved for phase 2 '
           f'robotic sanding and an automated oil line." '
           f'style="max-width:100%;height:auto">' + "".join(parts) + "</svg>")
    return Raw(
        '<figure class="bleed scroll">' + svg +
        '<figcaption>Timber enters at the left and leaves as flat-packed parts at the '
        'right, so nothing crosses its own path. The kiln and conditioning room sit '
        'upstream of everything: at 0.1–0.2 mm joint tolerance, moisture control is a '
        'machining input, not a storage detail.</figcaption></figure>')


def funnel(steps: list[dict]) -> Raw:
    """The TAM -> SAM -> SOM funnel, drawn to scale on a log width so a 6,000x drop is
    still visible, with each band tagged measured / derived / assumed."""
    import math
    bands = [s for s in steps if s["unit"] == "usd/yr"]
    if not bands:
        return Raw("")
    W, rowh, top = 880, 74, 58
    H = top + rowh * len(bands) + 46
    mx = max(b["value"] for b in bands)
    parts = [DEFS]
    parts.append(f'<text x="0" y="24" font-size="12" fill="currentColor" opacity="0.7">'
                 f'Bar width is logarithmic — a linear scale would make the last band '
                 f'invisible</text>')
    for i, b in enumerate(bands):
        y = top + i * rowh
        frac = math.log10(b["value"] + 1) / math.log10(mx + 1)
        w = max(60, frac ** 6 * (W - 300))
        assumed = b["kind"] == "assumed"
        stroke = "var(--alarm)" if assumed else "currentColor"
        fill_op = "0.10" if assumed else "0.06"
        parts.append(f'<rect x="0" y="{y}" width="{w:.0f}" height="42" rx="2" '
                     f'fill="{stroke}" fill-opacity="{fill_op}" stroke="{stroke}" '
                     f'stroke-width="{2 if assumed else 1.25}" '
                     f'{"stroke-dasharray=\'5 4\'" if assumed else ""}/>')
        v = b["value"]
        vs = f"${v/1e9:,.2f}bn" if v >= 1e9 else f"${v/1e6:,.1f}m"
        parts.append(f'<text x="12" y="{y + 27}" font-size="13" fill="currentColor">'
                     f'{esc(vs)}</text>')
        parts.append(f'<text x="{w + 14:.0f}" y="{y + 18}" font-size="12" '
                     f'fill="currentColor">{esc(b["step"])}</text>')
        parts.append(f'<text x="{w + 14:.0f}" y="{y + 34}" font-size="10.5" '
                     f'fill="{stroke}" opacity="0.85">{esc(b["kind"].upper())} · '
                     f'{esc(b["source"][:52])}</text>')
        if i < len(bands) - 1:
            parts.append(f'<line x1="26" y1="{y + 42}" x2="26" y2="{y + rowh - 2}" '
                         f'stroke="currentColor" stroke-width="1.25" '
                         f'marker-end="url(#ar)" opacity="0.7"/>')
    svg = (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Funnel from US cabinet '
           f'manufacturing revenue down to year-three revenue, with each step labelled '
           f'as measured, derived or assumed. The measured steps sit at the top; the '
           f'assumed steps are the last two and are drawn dashed." '
           f'style="max-width:100%;height:auto">' + "".join(parts) + "</svg>")
    return Raw('<figure class="bleed scroll">' + svg +
               '<figcaption>Solid bands are measured or arithmetic on measured numbers. '
               'Dashed bands are judgements. Notice where the dashes start: everything '
               'down to the custom cabinet market is evidence, and everything below it '
               'is an assumption waiting to be tested.</figcaption></figure>')
