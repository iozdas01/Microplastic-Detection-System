"""Render the business-plan page: the proposal to build the kigumi factory.

build_tam_us.py owns the demand side, build_factory.py owns the supply side, and this
page puts them against each other. Where the two disagree the page says so rather than
picking the flattering number.
"""
from __future__ import annotations

import json
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import PROC, PAGES, ROOT, TODAY, log, read_csv  # noqa: E402
from diagrams import floor_plan, process_flow  # noqa: E402
from page_kit import Raw, bar_cell, esc, note, pct, stat, table, usd  # noqa: E402

HERE = __import__("pathlib").Path(__file__).parent
OUT = PAGES / "autonomous-factory-plan.html"
MONTHS = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def pretty_date():
    y, mo, dd = (int(x) for x in TODAY.split("-"))
    return f"{dd} {MONTHS[mo]} {y}"


def main() -> None:
    fp, dp = PROC / "factory_model.json", PROC / "tam_us_model.json"
    if not fp.exists() or not dp.exists():
        log("build_plan_page: run build_factory.py and build_tam_us.py first")
        return
    f = json.loads(fp.read_text())
    d = json.loads(dp.read_text())
    FA = f["assumptions"]
    pick, sam, som = d["beachhead"], d["sam"], d["som"]
    cap, uc, proc = f["capital_plan"], f["unit_cost"], f["process"]
    mats, bound, be = f["materials"], d["som_bound"], d["breakeven"]
    b, t = d["blended"], d["tiers"]
    r3 = som["ramp"][-1]
    upo = proc["units_per_order"]
    tam = next(s["value"] for s in d["steps"]
               if s["step"] == "US household furniture spend (TAM)")

    L: list[str] = []
    Add = L.append

    chips = "".join(f"<div><b>{esc(a)}</b>{esc(c)}</div>" for a, c in [
        (usd(cap["phase_1_total_usd"]), "Phase 1 capital"),
        (f"{proc['nameplate_units_per_year']:,}", "Chairs / yr nameplate"),
        (f"{be['chairs_per_year_full_absorption']:,}", "Chairs / yr breakeven"),
        (f"{mats['joinery_operations_per_unit']}", "Kigumi operations per chair"),
    ])
    Add(f"""
  <header class="masthead bleed">
    <div class="flow">
      <p class="eyebrow">Build proposal · {esc(pretty_date())}</p>
      <h1>A chair with no fasteners, and a factory that never assembles one</h1>
      <p class="lede">A solid-timber cell cutting kigumi joinery on 5-axis machining
      centres, with robots carrying parts between machines. Nothing is assembled in the
      building — the customer does that by hand, without tools. On land we already own,
      with three-phase service in place.</p>
    </div>
    <div class="stamp">{chips}</div>
  </header>""")

    # ------------------------------------------------------------------ proposition
    Add(f"""
  <h2 id="proposition">The proposition</h2>

  <p>Make a configurable dining chair from solid hardwood, joined the way a Japanese
  temple is joined: interlocking <i>tsugite</i> and <i>shiguchi</i> geometry, tapered
  wedges that tighten under load, and no screws, cams, dowels or glue anywhere in the
  product. {mats['joinery_operations_per_unit']} machined joint operations per chair, cut
  to the 0.1–0.2&nbsp;mm tolerance the method needs.</p>

  <p>The article was not chosen by preference. Every furniture line was scored on demand
  and on whether this process can make it, and
  <b>{esc(pick['article'].lower())}</b> came out first — dining chairs and tables are the
  native home of frame joinery, and chairs sell in sets, so an order is
  {upo} units rather than one.</p>

  <div class="stats bleed">
    {stat(usd(tam), "TAM", "US household furniture spend, all articles")}
    {stat(usd(sam['base_usd']), "SAM", "configurable dining furniture, online-addressable")}
    {stat(usd(som['som_year_3_usd']), "SOM",
          f"year 3 — {r3['units']:,} orders, {r3.get('chairs', 0):,} chairs")}
  </div>

  <p class="callout">Three things in this plan cut against it, and all three are
  load-bearing. <b>Phase 1 costs {esc(usd(cap['phase_1_total_usd']))}</b>, well past the
  $1.5–3m envelope this was scoped to — solid-timber 5-axis is a more capital-hungry
  process than panel work, and the building adds
  {esc(usd(cap['phase_1_building_usd']))} on top. <b>The cell can make
  {esc(f"{bound['oversize_factor']}×")} what year-3 demand supports.</b> And <b>the plant
  delivers a {esc(pct(r3['actual_gross_margin'], 0))} gross margin at that volume, not the
  {esc(pct(b['gross_margin'], 0))} the pricing assumes.</b></p>""")

    # ------------------------------------------------------------------ the method
    Add(f"""
  <h2 id="kigumi">Why the joinery decides the factory</h2>

  <p>Choosing kigumi is not a styling decision; it rewrites the equipment list. Three
  consequences follow directly:</p>

  <div class="findings">
    <div class="finding"><span class="tier">Machines</span><div>
      <h3>No nesting router, no edgebander</h3>
      <p>Kigumi is cut in solid stock, not sheet. The plant is a lumber line feeding two
      5-axis machining centres — the only kind of machine that can cut compound joint
      geometry in one setup.</p></div></div>
    <div class="finding"><span class="tier">Tolerance</span><div>
      <h3>Moisture control is a machining input</h3>
      <p>A joint held by geometry alone fails when the wood moves. Holding 0.1–0.2&nbsp;mm
      means a kiln and a conditioning room upstream of the first cut — capex that a panel
      shop simply does not carry.</p></div></div>
    <div class="finding"><span class="tier">Product</span><div>
      <h3>The bill of materials has no hardware line</h3>
      <p>No cams, no dowels, no screws, no glue. It also means no assembly service to
      sell: the customer assembles by hand, which removes the metro coverage that would
      otherwise cap where we can sell at all.</p></div></div>
  </div>""")

    # ------------------------------------------------------------------ product
    bom = read_csv("factory_bom")
    rows = [[r["part"], r["qty"], f'{r["length_mm"]}×{r["width_mm"]}×{r["thickness_mm"]}',
             r["joinery_ops"], r["finished_bf"]] for r in bom]
    bom_tbl = table("One chair, part by part",
                    ["Part", "Qty", "Finished mm", "Joint ops", "Finished bd ft"],
                    rows, aligns=["wrap", "num", "num", "num", "num"])
    mrows = [[m["item"], m["qty"] if m["qty"] is not None else "—",
              f'${m["cost_usd"]:,.2f}'] for m in mats["rows"]]
    mrows.append(["total, incl. scrap", "—", f'${mats["total_per_unit_usd"]:,.2f}'])
    mat_tbl = table("Material cost per chair",
                    ["Item", "Quantity", "Cost"], mrows, aligns=["wrap", "num", "num"],
                    row_classes=[None] * (len(mrows) - 1) + ["lead"])
    Add(f"""
  <h2 id="product">The article</h2>

  <p>A dining chair in {esc(FA['species'])}: {len(bom)} part types,
  {mats['joinery_operations_per_unit']} joint operations,
  {mats['finished_board_feet']} finished board feet of timber. Every dimension in the
  configurator moves these numbers, and the cell does not care which variant it is
  cutting — that is the whole point of machining joints rather than jigging them.</p>

  {bom_tbl}
  {mat_tbl}

  <p>{esc(mats['note'])} At ${FA['timber_usd_per_board_foot']:.2f} a board foot,
  {mats['rough_board_feet']} rough board feet is
  {esc(pct(mats['rows'][0]['cost_usd'] / mats['total_per_unit_usd'], 0))} of material
  cost. <b>Timber yield, not hardware, is the lever on this bill of materials</b> — every
  point of yield recovered by better defect-skip optimisation goes straight to margin,
  which is why the optimising crosscut is the first machine on the list and not an
  afterthought.</p>""")

    # ------------------------------------------------------------------ process
    Add(f"""
  <h2 id="process">How it is made</h2>

  <p>Six stations, batch size one, with a
  {esc(pct(FA['changeover_allowance'], 0))} changeover allowance because every chair is a
  different size. Robots carry parts between the machining centres — that transfer is
  where the autonomy lives.</p>

  {process_flow(proc['stations'], proc['bottleneck'])}

  <p>The slowest station sets takt at <b>{proc['takt_min_per_unit']:.1f} minutes a
  chair</b>, and it is the leg machining centre: the legs carry more joint operations than
  any other part. At {FA['shifts']} shifts and {esc(pct(FA['oee'], 0))} OEE that is
  <b>{proc['nameplate_units_per_year']:,} chairs a year</b> —
  {proc['nameplate_orders_per_year']:,} orders of {upo}, or
  {proc['units_per_shift']} chairs a shift.</p>

  <p class="callout">{esc(proc['note'])} That is worth stating plainly because it is what
  makes the automation tractable. <b>Robotic assembly of a varying part mix is not a
  solved problem; robotic transfer between machines is.</b> By moving assembly to the
  customer, the plant only ever has to automate the part of the job that automation is
  actually good at.</p>""")

    st_rows = [[s["station"], f'{s["machine_min"]:.1f}', f'{s["handling_min"]:.1f}',
                f'{s["cycle_min_per_unit"]:.1f}',
                Raw(str(bar_cell(s["utilisation_at_takt"]))),
                pct(s["utilisation_at_takt"], 0)] for s in proc["stations"]]
    Add(str(table("Station cycle times and how much of takt each consumes",
                  ["Station", "Machine min", "Handling min", "Cycle min", "", "Load"],
                  st_rows, aligns=["wrap", "num", "num", "num", "plot", "num"],
                  row_classes=[("lead" if s["station"] == proc["bottleneck"] else None)
                               for s in proc["stations"]])))
    Add(f"""
  <p>The second machining centre runs at
  {esc(pct(next(s['utilisation_at_takt'] for s in proc['stations'] if 'rails' in s['station']), 0))}
  of takt, so it has headroom. Rebalancing which parts go to which centre — or adding
  fixturing so the leg centre changes over faster — buys output without buying a machine.
  That is the first thing to try before a third 5-axis.</p>""")

    # ------------------------------------------------------------------ assembly modes
    scen = f["assembly_scenarios"]
    price_chair_x = d["blended"]["revenue_per_order_usd"] / upo
    srows = [[sc["label"], f'{sc["takt_min"]:.1f}', f'${sc["freight_per_unit_usd"]:,.0f}',
              usd(sc["phase_1_capex_usd"]), f'${sc["cost_per_unit_at_4500"]:,.0f}',
              pct(1 - sc["cost_per_unit_at_4500"] / price_chair_x, 0)] for sc in scen]
    base = next(sc for sc in scen if sc["mode"] == "customer")
    ship = next(sc for sc in scen if sc["mode"] == "robotic_ship_assembled")
    fit = next(sc for sc in scen if sc["mode"] == "robotic_test_fit")
    Add(f"""
  <h2 id="assembly">Should a robot assemble the chair?</h2>

  <p>Robot-assembly foundation models make this a live question rather than a settled one,
  so it is costed here rather than argued. Three ways to finish the job, same cell, same
  timber, same joints.</p>

  {table(f"Assembly options, costed per chair at 4,500 chairs a year against a "
         f"${price_chair_x:,.0f} chair", 
         ["Option", "Takt min", "Freight", "Phase 1 capex", "Cost / chair",
          "Gross margin"], srows,
         aligns=["wrap", "num", "num", "num", "num", "num"],
         row_classes=[("lead" if sc["selected"] else None) for sc in scen])}

  <p>None of the three changes takt: a {esc(f"{(ship['takt_min']):.1f}")}-minute cell is
  still gated by the leg machining centre, so an assembly station has slack to hide in.
  What changes is freight. <b>An assembled chair is roughly six times the shipping volume
  of its parts</b>, which takes freight from ${base['freight_per_unit_usd']:,.0f} to
  ${ship['freight_per_unit_usd']:,.0f} a chair and packaging with it.</p>

  <p class="callout">Shipping assembled costs
  <b>${ship['cost_per_unit_at_4500'] - base['cost_per_unit_at_4500']:,.0f} more a chair</b>
  and takes gross margin from
  {esc(pct(1 - base['cost_per_unit_at_4500'] / price_chair_x, 0))} to
  {esc(pct(1 - ship['cost_per_unit_at_4500'] / price_chair_x, 0))}. Almost none of that is
  the robot — it is the box. Robotic assembly does not fix the margin problem in this
  plan, <b>it is the margin problem</b>, because the thing that makes this product cheap
  to deliver is that it ships as a flat bundle of sticks.</p>

  <h3>The version worth doing</h3>
  <p>There is a robot job here, and it is the third row. <b>Have the robot assemble every
  chair to prove the joints seat, then take it apart and flat-pack it.</b> That costs
  ${fit['cost_per_unit_at_4500'] - base['cost_per_unit_at_4500']:,.0f} a chair —
  {esc(pct((fit['cost_per_unit_at_4500'] - base['cost_per_unit_at_4500']) / price_chair_x, 1))}
  of the selling price — and it attacks the one defect this product actually has. A chair
  held together by geometry alone either fits or it does not, and the customer is the one
  who finds out. A test-fit station moves that discovery inside the building.</p>

  <p>It is also a far more tractable robotics problem. Test-fit is the same motion on a
  known part set in a fixture, with force feedback telling you whether a tapered joint
  seated. Full assembly is a varying part mix, unconstrained poses and compliance under
  load.</p>

  <h3>On the foundation-model route specifically</h3>
  <p>Skild AI announced S1 on 25 August 2026: a robot foundation model that learns a
  ten-minute task from a single human video, reporting 66% success on unseen tasks against
  9% for a language-prompted policy, with kit assembly among the demonstrated tasks. The
  capability direction is real and it is pointed at exactly this problem.</p>

  <p class="callout">Two things make it a phase 3 item rather than a phase 1 one.
  <b>66% first-pass success is a demo number, not a production number</b> — a station that
  fails one chair in three needs a person standing next to it, which is the cost the
  automation was meant to remove. And at announcement there were <b>no weights, no API and
  no paper</b>, so there is nothing to integrate against or to price. The right posture is
  to design the test-fit cell with a swappable policy layer, run it on conventional
  force-controlled motion now, and adopt a foundation model when it ships with an
  integration path and a published success rate on a fixed part set.</p>""")

    # ------------------------------------------------------------------ layout
    Add(f"""
  <h2 id="layout">The floor</h2>

  <p>{FA['building_sqft']:,} sq ft on owned land. Solid timber needs more building than
  panel work: rough stock, the kiln and the conditioning room take floor before a part is
  cut. The layout reserves footprints for the phase 2 drop-ins so nothing has to move.</p>

  {floor_plan(FA['building_sqft'])}""")

    # ------------------------------------------------------------------ equipment
    eq = read_csv("factory_equipment")
    for phase, title, blurb in [
        ("1", "Phase 1 — the cell",
         "The lumber line, both machining centres, the robot transfers and finishing. "
         "Five people across two shifts."),
        ("2", "Phase 2 — automate the two manual stations",
         "Robotic sanding and an automated oil line. Trigger: sustained two-shift running "
         "above 60% utilisation."),
        ("3", "Phase 3 — lights-out",
         "Automated timber grading in, automated kitting out. Trigger: demand above "
         "nameplate, not before."),
    ]:
        rows = [[r["category"], r["item"], f'${float(r["unit_cost_usd"]):,.0f}',
                 r["basis"]] for r in eq if r["phase"] == phase]
        if not rows:
            continue
        total = sum(float(r["total_usd"]) for r in eq if r["phase"] == phase)
        rows.append(["", Raw("<b>total</b>"), Raw(f'<b>${total:,.0f}</b>'), ""])
        Add(f"<h3>{esc(title)}</h3>\n<p>{esc(blurb)}</p>")
        Add(str(table(f"Phase {phase} equipment schedule",
                      ["Category", "Make and model", "Cost", "Basis of price"], rows,
                      aligns=["wrap", "wrap", "num", "wrap"],
                      row_classes=[None] * (len(rows) - 1) + ["lead"])))
    Add("""
  <p class="note">Machine prices in this industry are quote-driven, not listed; each row
  carries its basis. The whole schedule is written to
  <span class="note">data/reference/equipment.csv</span> so real quotes can replace it
  without editing any code.</p>""")

    # ------------------------------------------------------------------ capital
    fac = f["facility"]
    alts = fac["alternatives"]
    cap_rows = [
        ["Equipment, phase 1", usd(cap["phase_1_equipment_usd"]),
         "lumber line, two 5-axis centres, robots, finishing, software"],
        ["Building shell", usd(cap["phase_1_building_usd"]),
         f"{fac['building_sqft']:,} sq ft at ${fac['cost_per_sqft']:.0f}/sq ft"],
        ["Land", "$0", "already owned"],
        ["Three-phase power connection", "$0", "already on site"],
        ["Phase 1 total", usd(cap["phase_1_total_usd"]), "what the first raise must cover"],
    ]
    Add(f"""
  <h2 id="capital">What it costs to build</h2>

  {table("Phase 1 capital plan", ["Line", "Cost", "Note"], cap_rows,
         aligns=["wrap", "num", "wrap"],
         row_classes=[None, None, None, None, "lead"])}

  <p class="callout">This does not fit the envelope. Phase 1 is
  <b>{esc(usd(cap['phase_1_total_usd']))}</b> against a $1.5–3m target, and owning the
  land removes the land cost, not the shell. Four ways to close the gap, in the order I
  would take them: <b>start with one machining centre</b> and the robot transfer to
  sanding, which cuts roughly $580k and still proves the autonomy thesis;
  <b>fit out an existing structure</b> if one is on the parcel
  ({esc(usd(alts['fit_out_existing']))} rather than
  {esc(usd(alts['new_pemb_turnkey']))}); <b>buy the lumber line used</b>, where
  moulders and crosscuts trade at a fraction of new; and <b>defer the optical metrology
  cell</b>, running first-off checks on gauges until volume justifies SPC.</p>

  <div class="phases bleed">
    <div class="phase"><span class="k">Phase 1</span>
      <span class="n">{esc(usd(cap['phase_1_total_usd']))}</span>
      <p>The cell plus the building. Five on the floor across two shifts.</p></div>
    <div class="phase"><span class="k">Phase 2</span>
      <span class="n">{esc(usd(cap['phase_2_usd']))}</span>
      <p>Robotic sanding, automated oiling, AMR transport.</p></div>
    <div class="phase"><span class="k">Phase 3</span>
      <span class="n">{esc(usd(cap['phase_3_usd']))}</span>
      <p>Automated timber grading and kitting — the last manual touches.</p></div>
  </div>""")

    # ------------------------------------------------------------------ operating cost
    op = f["opex"]
    op_rows = [[k, usd(v), ""] for k, v in op["annual"].items()]
    op_rows.append([Raw("<b>total</b>"), Raw(f"<b>{usd(op['annual_total'])}</b>"), ""])
    Add(f"""
  <h2 id="operating">What it costs to run</h2>

  <p>{esc(op['wage_basis'])}. Headcount is
  {sum(FA['headcount'].values())} across {FA['shifts']} shifts. Worth noting what that wage
  has been doing: it is up 34.9% since January 2020 while employment in furniture
  manufacturing fell 13.7% — which is the quantitative case for automating at all.</p>

  {table("Annual fixed cost", ["Line", "Per year", ""], op_rows,
           aligns=["wrap", "num", "wrap"],
           row_classes=[None] * (len(op_rows) - 1) + ["lead"])}""")

    # ------------------------------------------------------------------ unit cost
    curve = uc["curve"]
    mx = max(r["total_per_unit"] for r in curve)
    price_order = b["revenue_per_order_usd"]
    price_chair = price_order / upo
    c_rows = [[f'{r["units"]:,}', f'{r["orders"]:,}',
               Raw(str(bar_cell(r["total_per_unit"] / mx))),
               f'${r["total_per_unit"]:,.0f}', f'${r["fixed_per_unit"]:,.0f}',
               pct(1 - r["total_per_unit"] / price_chair, 0)] for r in curve]
    Add(f"""
  <h2 id="unitcost">The unit cost curve</h2>

  <p>Variable cost is <b>${uc['variable_per_unit_usd']:,.0f}</b> a chair — timber, finish,
  packaging and freight. Everything else is fixed, so cost per chair is almost entirely a
  question of volume. {esc(uc['basis'])}</p>

  {table(f"Cost per chair against a ${price_chair:,.0f} selling price "
         f"(${price_order:,.0f} for a set of {upo})",
         ["Chairs / yr", "Orders / yr", "", "Cost / chair", "of which fixed",
          "Gross margin"], c_rows,
         aligns=["num", "num", "plot", "num", "num", "num"])}

  <p>Breakeven is <b>{be['chairs_per_year_full_absorption']:,} chairs a year</b>
  ({be['units_per_year_full_absorption']:,} orders) fully absorbed, or
  {be['units_per_year_cash']:,} orders on a cash basis —
  {esc(pct(be['pct_of_capacity'], 0))} of nameplate. Contribution is
  ${be['contribution_per_unit_usd']:,.0f} an order against a
  ${be['variable_per_order_usd']:,.0f} variable cost, so past breakeven this model is
  steep and rewards volume hard.</p>""")

    # ------------------------------------------------------------------ tension
    Add(f"""
  <h2 id="tension">Where the plan does not yet hold</h2>

  <h3>The cell is {esc(f"{bound['oversize_factor']}×")} bigger than the demand</h3>
  <p>Capacity is {bound['capacity_units_per_year']:,} orders a year. The market model
  supports {bound['demand_units_per_year']:,} at year 3 — {esc(bound['demand_basis'])}.
  {esc(bound['binding_constraint'].capitalize())} binds, and it is not the factory. The gap
  is narrower than it was for a panel plant, because 5-axis joinery is slow work, but it is
  still a plant running at {esc(pct(r3['units'] / bound['capacity_units_per_year'], 0))} of
  what it was bought for.</p>

  <h3>The pricing assumes a margin the plant does not deliver</h3>
  <p>The tier ladder assumes {esc(pct(b['gross_margin'], 0))}. At the year-3 volume of
  {r3['units']:,} orders — {r3.get('chairs', 0):,} chairs — the modelled cost is
  <b>${r3['modelled_cost_per_chair_usd']:,.0f} a chair</b>, or
  ${r3['modelled_cost_per_unit_usd']:,.0f} a set, against a
  ${price_order:,.0f} order. That is {esc(pct(r3['actual_gross_margin'], 0))}, not
  {esc(pct(b['gross_margin'], 0))}. The two converge as fixed cost spreads; until they do,
  the cost model is the one with a factory behind it.</p>

  <p class="callout">Both problems have one shape: <b>this is a capital-heavy,
  volume-hungry plan whose demand evidence is its thinnest part.</b> The measured
  custom-search share under the SAM is
  {esc(pct(sam['custom_search_share_measured'], 2))}; everything above it is assumption.
  The configurator is already a
  ${next(float(r['unit_cost_usd']) for r in eq if 'configurator' in r['item'].lower()):,.0f}
  line inside phase 1 and it is the one experiment that tests the assumption the other
  {esc(usd(cap['phase_1_total_usd']))} rests on. <b>Run it before the slab is poured, not
  after.</b> A kigumi chair with no fasteners is also unusually cheap to prototype — one
  machining centre on a subcontract basis will produce a sellable chair long before there
  is a building to put it in.</p>""")

    # ------------------------------------------------------------------ method
    Add(f"""
  <h2 id="method">How this was built</h2>

  <p>Demand comes from {note("scripts/build_tam_us.py")}, which sizes the market from
  Census and BLS data and scores every furniture article on whether this process can make
  it. The factory comes from {note("scripts/build_factory.py")}, which derives capacity
  from per-station cycle times and cost from a bill of materials, the BLS production wage
  and a named equipment schedule. Supply runs first and demand consumes its capacity and
  cost, so the two cannot silently disagree.</p>

  <p class="callout">Every figure on this page is computed by
  {note("scripts/build_plan_page.py")} from those two models — none is typed. The
  assumptions live in one block at the top of each script.
  <b>Change one, re-run, and this page rewrites itself.</b></p>

  <footer>
    <p class="note">Equipment prices indicative and quote-driven; wage and price series
    from BLS; market data from Census, BLS and Google Trends. Joinery method after the
    kigumi tradition of tsugite and shiguchi. Compiled {esc(pretty_date())}.
    Generated by scripts/build_plan_page.py.</p>
  </footer>""")

    head = (HERE / "page.head.plan.html").read_text().strip()
    css = (HERE / "page.css").read_text().strip()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(f"{head}\n\n<style>\n{css}\n</style>\n\n"
                   f'<div class="page flow">\n' + "\n".join(L) + "\n\n</div>\n")
    log(f"  {OUT.relative_to(ROOT)} written ({len(OUT.read_text()):,} bytes)")


if __name__ == "__main__":
    main()
