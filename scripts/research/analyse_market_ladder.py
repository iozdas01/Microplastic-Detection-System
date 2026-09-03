"""Is made-to-measure window coverings a venture-scale opportunity, layer by layer?

Reads the SUSB receipts ladder and answers the founder's question in the order it was asked:
size the smallest business, go one layer up, keep going to enterprise, and say at each layer
what a remake actually costs that business and whether anyone there could plausibly pay.

Three things are MEASURED and three are MODELLED, and they are never mixed in a column:

  MEASURED   firms, establishments, employment, payroll, receipts per size band (SUSB 2022)
  MEASURED   revenue concentration — what share sits in the largest firms
  MEASURED   receipts of the adjacent made-to-measure industries

  MODELLED   remake rate. THIS IS THE WHOLE UNKNOWN. H3A1 exists because no published source
             gives it. Everything downstream is a range across 3%-10%, and the range is wide
             on purpose: a single conversation that produces a real rate collapses it.
  MODELLED   what a software seat could cost per layer — illustrative, to test whether a
             tool-shaped business can clear a venture bar at all.
  MODELLED   the share of remade value a vendor could capture.

The verdict this prints is arithmetic, not opinion. If the arithmetic says a blinds-only
software company tops out in the single-digit millions, that is worth knowing BEFORE fifty
outreach messages go out, not after.
"""
from __future__ import annotations

import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import log, read_csv, record, save_csv  # noqa: E402

BLINDS = {"337920": "manufacturers", "442291": "retail dealers"}
REMAKE_LO, REMAKE_HI = 0.03, 0.10   # UNMEASURED — this is exactly what H3A1 must settle

# Illustrative annual software spend a firm in each receipts band could carry. Anchored on
# the ordinary SMB-software rule that a tool is affordable at roughly 0.5-1% of revenue, then
# rounded to plausible price points. Modelled, never measured — labelled as such everywhere.
def seat_price(mid_receipts_usd: float) -> float:
    if mid_receipts_usd < 500_000:
        return 0            # a sub-$500k firm buys nothing recurring
    if mid_receipts_usd < 2_500_000:
        return 3_000
    if mid_receipts_usd < 10_000_000:
        return 12_000
    if mid_receipts_usd < 30_000_000:
        return 40_000
    return 150_000


def band_midpoint(band: str) -> float:
    """Receipts-band label ('1,000-2,499', '100,000+') -> midpoint in dollars."""
    b = band.replace(",", "").replace("$", "").strip()
    if b.startswith("<"):
        return float(b[1:]) * 1000 / 2
    if b.endswith("+"):
        return float(b[:-1]) * 1000 * 2.5   # open-ended top band, deliberately crude
    if "-" in b:
        lo, hi = b.split("-")
        return (float(lo) + float(hi)) / 2 * 1000
    return 0.0


def main() -> None:
    rows = read_csv("market_ladder_susb")
    if not rows:
        log("analyse_market_ladder: run t2_susb_market_ladder.py first")
        return

    def num(v):
        try:
            return float(v)
        except (TypeError, ValueError):
            return 0.0

    out, totals = [], {}
    for code, role in BLINDS.items():
        bands = [r for r in rows if r["naics"] == code and r["bucket_order"] != "01"]
        tot = next(r for r in rows if r["naics"] == code and r["bucket_order"] == "01")
        tot_rc = num(tot["receipts_usd_000"]) * 1000
        totals[code] = {"firms": num(tot["firms"]), "receipts": tot_rc,
                        "estabs": num(tot["establishments"]), "role": role}
        for b in bands:
            rc = num(b["receipts_usd_000"]) * 1000
            firms = num(b["firms"])
            mid = band_midpoint(b["receipts_band_usd_000"])
            price = seat_price(mid)
            out.append({
                "naics": code,
                "layer": role,
                "receipts_band_usd_000": b["receipts_band_usd_000"],
                "firms": int(firms),
                "establishments": int(num(b["establishments"])),
                "receipts_usd": int(rc),
                "share_of_industry": round(rc / tot_rc, 4) if tot_rc else 0,
                "receipts_per_firm_usd": int(rc / firms) if firms else 0,
                "remade_value_lo_usd": int(rc * REMAKE_LO),
                "remade_value_hi_usd": int(rc * REMAKE_HI),
                "remade_per_firm_lo_usd": int(rc * REMAKE_LO / firms) if firms else 0,
                "remade_per_firm_hi_usd": int(rc * REMAKE_HI / firms) if firms else 0,
                "modelled_seat_price_usd": int(price),
                "modelled_layer_arr_usd": int(price * firms),
            })
    save_csv("market_ladder_ranked", out)

    blinds_rc = sum(t["receipts"] for t in totals.values())
    adj = [r for r in rows if r["role"] == "adjacent_mtm" and r["bucket_order"] == "01"]
    adj_rc = sum(num(r["receipts_usd_000"]) * 1000 for r in adj)
    soft_arr = sum(r["modelled_layer_arr_usd"] for r in out)

    record("census-susb", "market-ladder-ranked", "derived", len(out),
           note=f"blinds trade ${blinds_rc/1e9:.2f}bn · adjacent MTM ${adj_rc/1e9:.2f}bn · "
                f"modelled software ceiling ${soft_arr/1e6:.1f}m ARR")

    for code, t in totals.items():
        log("")
        log(f"  {code} — {t['role']}: {t['firms']:,.0f} firms, ${t['receipts']/1e9:.2f}bn")
        log(f"    {'band ($k)':<16}{'firms':>7}{'receipts':>12}{'%ind':>7}"
            f"{'per firm':>12}{'remade/firm 3-10%':>26}")
        for r in [x for x in out if x["naics"] == code]:
            log(f"    {r['receipts_band_usd_000']:<16}{r['firms']:>7,}"
                f"{r['receipts_usd']/1e6:>11,.1f}m{r['share_of_industry']:>7.1%}"
                f"{r['receipts_per_firm_usd']/1e6:>11,.2f}m"
                f"{'$' + format(r['remade_per_firm_lo_usd'], ',') :>15}"
                f"{' - $' + format(r['remade_per_firm_hi_usd'], ','):>11}")

    log("")
    log("  ── CONCENTRATION ──")
    for code, t in totals.items():
        top = [x for x in out if x["naics"] == code and x["receipts_band_usd_000"].endswith("+")]
        if top:
            x = top[0]
            log(f"    {code}: the largest {x['firms']} firms hold "
                f"{x['share_of_industry']:.1%} of ${t['receipts']/1e9:.2f}bn "
                f"across {x['establishments']} establishments")

    log("")
    log("  ── THE VENTURE QUESTION ──")
    log(f"    US blinds trade (mfg + specialty retail)   ${blinds_rc/1e9:>8.2f}bn receipts")
    log(f"    Value remade each year at 3%-10%           "
        f"${blinds_rc*REMAKE_LO/1e6:>8.0f}m - ${blinds_rc*REMAKE_HI/1e6:,.0f}m")
    log(f"    Modelled software ceiling, ALL US blinds   ${soft_arr/1e6:>8.1f}m ARR")
    log("      ^ every firm in both industries buying, at modelled prices, with no competitor")
    log("        and no churn. A ceiling nobody reaches, not a forecast.")
    log("")
    log(f"    Adjacent made-to-measure industries        ${adj_rc/1e9:>8.2f}bn receipts")
    for r in sorted(adj, key=lambda x: -num(x["receipts_usd_000"])):
        log(f"      {r['naics']}  {r['industry'][:44]:<46}"
            f"${num(r['receipts_usd_000'])/1e6:>7,.2f}bn  {int(num(r['firms'])):>7,} firms")
    log(f"    Blinds as a share of that wider pool       "
        f"{blinds_rc/(blinds_rc+adj_rc):>8.1%}")


if __name__ == "__main__":
    main()
