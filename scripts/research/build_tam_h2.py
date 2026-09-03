"""Bottom-up market sizing for H2 — machined replacements for blocked parts.

Chain:  reachable plants  x  blocked-part events per plant per year
        x  share where a machined replacement is viable  x  order value

The denominator is measured (Eurostat SBS, manufacturing enterprises by size band and
country). The three rates are NOT measured and are flagged as assumptions everywhere they
are used: each one is exactly what an H2 assumption is being tested to settle. Publishing
them as if they were data is the failure this header exists to prevent.

    events per plant per year          -> H2A1
    share answerable by machining      -> H2A2
    order value / whether speed or price binds -> H2A3

Run:  .venv/bin/python -m scripts.research.build_tam_h2
"""
from __future__ import annotations
import json, csv, urllib.request, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
IDEA = ROOT / "reports" / "high-mix-manufacturing" / "research"
RAW, PROC = IDEA / "data" / "raw" / "eurostat", IDEA / "data" / "processed"
TODAY = datetime.date.today().isoformat()

EUROSTAT = ("https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"
            "sbs_sc_ovw?format=JSON&lang=EN&time=2022&nace_r2=C&indic_sbs=ENT_NR")

# ── ASSUMPTIONS. Every one of these is a guess until an interview moves it. ──────────
# Blocked-part events per plant per year, by employee band. A "blocked part" is one the
# plant needed and could not get on the lead time it wanted. Scales with equipment count.
EVENTS_PER_PLANT_YR = {"20-49": 1.5, "50-249": 4.0, "GE250": 12.0}   # H2A1 — ASSUMPTION
# Of those events, the share where a machined replacement is both technically viable and
# permitted. This is where the digital-spares companies died.
MACHINABLE_SHARE = 0.25                                              # H2A2 — ASSUMPTION
# Average order value of a one-off machined replacement, including reverse engineering.
AOV_EUR = 1200.0                                                     # H2A3 — ASSUMPTION

# Plants under 20 employees are excluded: below that there is rarely a maintenance
# function, and the downtime cost that carries the premium is not there.
BANDS = ["20-49", "50-249", "GE250"]
# SAM cut: plants of 50+ in the ten largest EU manufacturing economies. 50+ is where a
# maintenance function and a budget holder reliably exist; the ten countries are where
# road freight from Türkiye is economic on a days-not-weeks timescale.
SAM_BANDS = ["50-249", "GE250"]
SAM_GEO = ["DE", "IT", "FR", "ES", "PL", "CZ", "NL", "AT", "RO", "SE"]

# ── SOM: capacity-led. PLACEHOLDER until the shop's real numbers land. ───────────────
MACHINE_HOURS_YR = 4000.0      # one machine-equivalent, two shifts, allowing downtime
UTILISATION = 0.65             # PLACEHOLDER
HOURS_PER_JOB = 6.0            # PLACEHOLDER — includes setup, programming, inspection
RAMP_YEAR_3 = 0.60             # share of capacity reached by year 3


def fetch():
    RAW.mkdir(parents=True, exist_ok=True)
    dest = RAW / f"{TODAY}-manufacturing-enterprises-by-size.json"
    if not dest.exists():
        with urllib.request.urlopen(EUROSTAT, timeout=60) as r:
            dest.write_bytes(r.read())
    return json.loads(dest.read_text())


def parse(d):
    """jsonstat -> {(geo, size_emp): enterprises}"""
    dims, sizes = d["id"], d["size"]
    idx = {k: d["dimension"][k]["category"]["index"] for k in dims}
    rev = {k: {v: kk for kk, v in idx[k].items()} for k in dims}
    strides, acc = {}, 1
    for k, n in zip(reversed(dims), reversed(sizes)):
        strides[k] = acc; acc *= n
    out = {}
    for flat, val in d["value"].items():
        f = int(flat); coord = {}
        for k in dims:
            coord[k] = rev[k][(f // strides[k]) % len(idx[k])]
        out[(coord["geo"], coord["size_emp"])] = val
    return out


def main():
    counts = parse(fetch())
    PROC.mkdir(parents=True, exist_ok=True)

    geos = sorted({g for (g, s) in counts if g not in ("EU27_2020",)})
    rows, tam_plants, tam_events, tam_eur = [], 0.0, 0.0, 0.0
    sam_plants = sam_eur = 0.0
    for g in geos:
        for b in BANDS:
            n = counts.get((g, b))
            if n is None:
                continue
            ev = n * EVENTS_PER_PLANT_YR[b]
            eur = ev * MACHINABLE_SHARE * AOV_EUR
            rows.append({"geo": g, "size_emp": b, "enterprises": int(n),
                         "events_per_yr": round(ev), "addressable_eur_yr": round(eur)})
            tam_plants += n; tam_events += ev; tam_eur += eur
            if g in SAM_GEO and b in SAM_BANDS:
                sam_plants += n; sam_eur += eur

    with (PROC / "h2_plants_by_size.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

    jobs_capacity = MACHINE_HOURS_YR * UTILISATION / HOURS_PER_JOB
    som_capacity = jobs_capacity * RAMP_YEAR_3 * AOV_EUR
    som = min(som_capacity, sam_eur)
    binds = "capacity" if som_capacity < sam_eur else "demand"

    steps = [
        ("Manufacturing enterprises, 20+ employees, EU/EFTA", round(tam_plants), "plants",
         "Eurostat sbs_sc_ovw, NACE C, 2022, size bands 20-49 / 50-249 / GE250"),
        ("Blocked-part events per year (TAM)", round(tam_events), "events/yr",
         "plants x events per plant per year — ASSUMPTION, gated on H2A1"),
        ("Share answerable by a machined replacement", MACHINABLE_SHARE, "share",
         "ASSUMPTION, gated on H2A2 — this is where digital-spares companies died"),
        ("Average order value", AOV_EUR, "eur/order",
         "ASSUMPTION, gated on H2A3 — needs real quotes from the shop"),
        ("TAM", round(tam_eur), "eur/yr", "all four lines above multiplied"),
        ("SAM plants (50+ employees, top 10 EU manufacturing economies)", round(sam_plants),
         "plants", "same source, cut to bands and countries we can serve"),
        ("SAM", round(sam_eur), "eur/yr", "SAM plants at the same assumed rates"),
        ("Capacity, year 3", round(som_capacity), "eur/yr",
         f"{MACHINE_HOURS_YR:.0f} machine-hours x {UTILISATION:.0%} utilisation / "
         f"{HOURS_PER_JOB:.0f}h per job x {RAMP_YEAR_3:.0%} ramp — PLACEHOLDER, needs the shop's real numbers"),
        ("SOM (year 3)", round(som), "eur/yr", f"smaller of capacity and SAM — {binds} binds"),
    ]
    with (PROC / "h2_tam_steps.csv").open("w", newline="") as f:
        w = csv.writer(f); w.writerow(["step", "value", "unit", "basis"]); w.writerows(steps)
    model = {"generated": TODAY, "tam_eur_yr": tam_eur, "sam_eur_yr": sam_eur,
             "som_eur_yr": som, "binds": binds, "tam_plants": tam_plants,
             "sam_plants": sam_plants, "assumptions": {
                 "events_per_plant_yr": EVENTS_PER_PLANT_YR,
                 "machinable_share": MACHINABLE_SHARE, "aov_eur": AOV_EUR}}
    (PROC / "h2_tam_model.json").write_text(json.dumps(model, indent=2))

    top = sorted(({"geo": r["geo"], "eur": r["addressable_eur_yr"], "n": r["enterprises"]}
                  for r in rows if r["geo"] in SAM_GEO and r["size_emp"] in SAM_BANDS),
                 key=lambda x: -x["eur"])
    by_geo = {}
    for t in top:
        by_geo.setdefault(t["geo"], {"eur": 0, "n": 0})
        by_geo[t["geo"]]["eur"] += t["eur"]; by_geo[t["geo"]]["n"] += t["n"]

    def m(x): return f"€{x/1e6:.1f}m" if x < 1e9 else f"€{x/1e9:.2f}bn"
    lines = [
        "---",
        "purpose: Bottom-up market size for H2 — machined replacements for parts blocked in the supply chain.",
        f"generated: {TODAY} by scripts/research/build_tam_h2.py",
        "---", "",
        "# Machined replacements for blocked parts — EU market size", "",
        "**Generated file. Do not hand-edit — fix the script and rerun.**", "",
        "> **Read the assumption flags before quoting any number here.** The plant count is",
        "> measured. The three rates that turn plants into revenue are guesses, and each one is",
        "> exactly what an H2 assumption is being tested to settle. This model is a way of seeing",
        "> which unknown matters most, not a market size to put in a deck.", "",
        "## The three numbers", "",
        "| | Value | What it is |", "| --- | ---: | --- |",
        f"| **TAM** | {m(tam_eur)}/yr | Every 20+ employee manufacturer in the EU/EFTA, at the assumed event rate |",
        f"| **SAM** | {m(sam_eur)}/yr | 50+ employee plants in the ten largest EU manufacturing economies |",
        f"| **SOM** | {m(som)}/yr | Year 3, {binds}-bound |", "",
        f"Measured: **{tam_plants:,.0f}** manufacturing enterprises of 20+ employees across EU/EFTA,",
        f"of which **{sam_plants:,.0f}** sit in the SAM cut. Everything after that is assumption.", "",
        "## What actually drives the answer", "",
        "| Input | Value | Status | Settled by |", "| --- | ---: | --- | --- |",
        f"| Plants, 20+ employees | {tam_plants:,.0f} | **measured** (Eurostat SBS 2022) | — |",
        f"| Blocked-part events per plant per year | {EVENTS_PER_PLANT_YR['50-249']} (50-249 band) | **assumption** | H2A1 |",
        f"| Share answerable by machining | {MACHINABLE_SHARE:.0%} | **assumption** | H2A2 |",
        f"| Order value | €{AOV_EUR:,.0f} | **assumption** | H2A3 |", "",
        "Three of the four inputs are unmeasured, so the output moves by more than an order of",
        "magnitude across reasonable ranges. **The model's only honest use is ranking which",
        "interview question is worth asking first**, and on that it is unambiguous: the machinable",
        "share (H2A2) is the input that can take the whole thing to zero. A plant that has ten",
        "blocked parts a year and will not accept a non-OEM replacement for any of them is worth",
        "nothing, whatever the other numbers say.", "",
        "## Where the SAM sits", "", "| Country | 50+ plants | Addressable at assumed rates |",
        "| --- | ---: | ---: |",
    ]
    for g, v in sorted(by_geo.items(), key=lambda kv: -kv[1]["eur"]):
        lines.append(f"| {g} | {v['n']:,} | {m(v['eur'])} |")
    lines += ["", "## Capacity", "",
        f"At {MACHINE_HOURS_YR:.0f} machine-hours a year, {UTILISATION:.0%} utilisation and",
        f"{HOURS_PER_JOB:.0f} hours a job, one machine-equivalent clears **{jobs_capacity:,.0f} jobs a year**,",
        f"or {m(jobs_capacity*AOV_EUR)} at the assumed order value. At a {RAMP_YEAR_3:.0%} year-3 ramp that is",
        f"{m(som_capacity)}, and **{binds} binds**.", "",
        "Those capacity figures are placeholders. The shop's real machine list, machine-hour rate",
        "and setup times replace them, and until they do the SOM line is arithmetic rather than a",
        "forecast.", "",
        "## What would change this most", "",
        "1. **Ten calls settling the event rate (H2A1).** The cheapest input to move and it scales",
        "   the whole model linearly.",
        "2. **One clear answer on non-OEM acceptance (H2A2)** in a regulated environment. This one",
        "   is not linear: it either opens the market or closes it.",
        "3. **Five real quotes** priced against the shop's actual cost, which replaces the order",
        "   value assumption and tells you whether speed or price is what binds (H2A3).", "",
        f"Sources: Eurostat `sbs_sc_ovw` (NACE C, 2022), retrieved {TODAY}. Raw response in",
        "`data/raw/eurostat/`, parsed counts in `data/processed/h2_plants_by_size.csv`.",
    ]
    (IDEA / "REPORT-h2.md").write_text("\n".join(lines) + "\n")
    print(f"[ok] TAM {m(tam_eur)} | SAM {m(sam_eur)} | SOM {m(som)} ({binds} binds)")
    print(f"[ok] wrote {IDEA/'REPORT-h2.md'} + 3 files in data/processed/")


if __name__ == "__main__":
    main()
