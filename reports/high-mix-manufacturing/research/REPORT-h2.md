---
purpose: Bottom-up market size for H2 — machined replacements for parts blocked in the supply chain.
generated: 2026-09-02 by scripts/research/build_tam_h2.py
---

# Machined replacements for blocked parts — EU market size

**Generated file. Do not hand-edit — fix the script and rerun.**

> **Read the assumption flags before quoting any number here.** The plant count is
> measured. The three rates that turn plants into revenue are guesses, and each one is
> exactly what an H2 assumption is being tested to settle. This model is a way of seeing
> which unknown matters most, not a market size to put in a deck.

## The three numbers

| | Value | What it is |
| --- | ---: | --- |
| **TAM** | €190.6m/yr | Every 20+ employee manufacturer in the EU/EFTA, at the assumed event rate |
| **SAM** | €105.1m/yr | 50+ employee plants in the ten largest EU manufacturing economies |
| **SOM** | €0.3m/yr | Year 3, capacity-bound |

Measured: **192,834** manufacturing enterprises of 20+ employees across EU/EFTA,
of which **61,749** sit in the SAM cut. Everything after that is assumption.

## What actually drives the answer

| Input | Value | Status | Settled by |
| --- | ---: | --- | --- |
| Plants, 20+ employees | 192,834 | **measured** (Eurostat SBS 2022) | — |
| Blocked-part events per plant per year | 4.0 (50-249 band) | **assumption** | H2A1 |
| Share answerable by machining | 25% | **assumption** | H2A2 |
| Order value | €1,200 | **assumption** | H2A3 |

Three of the four inputs are unmeasured, so the output moves by more than an order of
magnitude across reasonable ranges. **The model's only honest use is ranking which
interview question is worth asking first**, and on that it is unambiguous: the machinable
share (H2A2) is the input that can take the whole thing to zero. A plant that has ten
blocked parts a year and will not accept a non-OEM replacement for any of them is worth
nothing, whatever the other numbers say.

## Where the SAM sits

| Country | 50+ plants | Addressable at assumed rates |
| --- | ---: | ---: |
| DE | 18,915 | €33.4m |
| IT | 10,759 | €16.6m |
| PL | 7,419 | €12.8m |
| FR | 6,075 | €10.9m |
| ES | 5,998 | €9.7m |
| CZ | 3,790 | €6.6m |
| RO | 3,005 | €5.2m |
| NL | 2,402 | €3.8m |
| AT | 1,940 | €3.5m |
| SE | 1,446 | €2.6m |

## Capacity

At 4000 machine-hours a year, 65% utilisation and
6 hours a job, one machine-equivalent clears **433 jobs a year**,
or €0.5m at the assumed order value. At a 60% year-3 ramp that is
€0.3m, and **capacity binds**.

Those capacity figures are placeholders. The shop's real machine list, machine-hour rate
and setup times replace them, and until they do the SOM line is arithmetic rather than a
forecast.

## What would change this most

1. **Ten calls settling the event rate (H2A1).** The cheapest input to move and it scales
   the whole model linearly.
2. **One clear answer on non-OEM acceptance (H2A2)** in a regulated environment. This one
   is not linear: it either opens the market or closes it.
3. **Five real quotes** priced against the shop's actual cost, which replaces the order
   value assumption and tells you whether speed or price is what binds (H2A3).

Sources: Eurostat `sbs_sc_ovw` (NACE C, 2022), retrieved 2026-09-02. Raw response in
`data/raw/eurostat/`, parsed counts in `data/processed/h2_plants_by_size.csv`.
