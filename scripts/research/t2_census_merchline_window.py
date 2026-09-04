"""Tier 2 — Economic Census merchandise lines: how window treatments actually reach buyers.

Answers the question `t2_census_arts_ecommerce.py` had to leave open. ARTS reports
e-commerce by the SELLER's kind of business, so it can say what share of *furniture stores'*
sales are online but never what share of *window coverings* are. Merchandise-line detail —
one product line split across the industries that sell it — lives in the Economic Census,
which needs CENSUS_API_KEY.

WHICH YEAR MEASURES IT, AND WHY IT IS NOT 2022. The line is NAPCS 5000625000, "Retail sales
of window treatments, including rods, poles, and fixtures". In 2017 NAICS the online-only
sellers sat in their own industry, 454110 Electronic shopping and mail-order houses, so the
line's split across industries IS a channel split. The 2022 NAICS revision dissolved
subsector 454 and reclassified online sellers into whichever retail industry matches what
they sell — Blinds.com lands in 449122 Window Treatment Retailers alongside the storefronts.
So 2022 gives a better product total and a WORSE channel answer: the online row is gone,
absorbed. 2017 is the last year the question is answerable, and 2022 is collected anyway to
show the absorption rather than assert it.

WHAT THE LINE IS NOT. It bundles a $12 curtain rod with a motorised made-to-measure shade.
Nothing in the Economic Census isolates made-to-measure, so the share below is the online
share of the window-treatment CATEGORY, never of the made-to-measure part of it.

The 2012 run is a third, looser reading: product line 20280 is broader still (it folds in
slipcovers and bed and table coverings), and the tighter 2012 line — 20282, blinds and shades
only — is published for store industries with no nonstore row at all, so it cannot yield a
share. Both are collected so the limit is visible in the data rather than only in this note.

NATIONAL ONLY, by construction. `ecnnapcsprd` publishes no geography below the nation, and
there is no point wanting one: a retail establishment is counted where the SELLER is, not
where the customer is, so an online retailer's whole book lands in one state and a state-level
channel share means nothing. `ecnnapcsind` does carry state, but publishes the line for
California only through the channels with physical presence.

Requires CENSUS_API_KEY (free, instant: https://api.census.gov/data/key_signup.html).

    .venv/bin/python scripts/research/t2_census_merchline_window.py
"""
from __future__ import annotations

import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import (ENV, census_rows, get, guard, log, read_csv, record,  # noqa: E402
                    save_csv, save_raw)

SOURCE = "census-merchline"

# One product line, three vintages of the classification that carries it.
PULLS = [
    {"year": 2017, "dataset": "ecnnapcsprd", "code_var": "NAPCS2017", "naics_var": "NAICS2017",
     "code": "5000625000",
     "label": "Retail sales of window treatments, including rods, poles, and fixtures",
     "dollars": "NAPCSDOL", "share": "NAICSALL_PCT"},
    {"year": 2022, "dataset": "ecnnapcsprd", "code_var": "NAPCS2022", "naics_var": "NAICS2022",
     "code": "5000625000",
     "label": "Retail sales of window treatments, including rods, poles, and fixtures",
     "dollars": "NAPCSDOL", "share": "NAICSALL_PCT"},
    {"year": 2012, "dataset": "ecnlines", "code_var": "PSCODE2012", "naics_var": "NAICS2012",
     "code": "20280",
     "label": "Curtains, draperies, blinds, slipcovers, bed & table coverings",
     "dollars": "RCPTOT", "share": "KB_PCT"},
]

# Which industries are a person standing at the window, and which are not. Assigned by NAICS
# rather than inferred, because the whole point is that the 2022 revision moved the boundary.
CHANNEL = {
    # 2017 / 2012 NAICS — the years where the online sellers are separable
    "454110": "online_and_mail_order", "4541": "online_and_mail_order",
    "45411": "online_and_mail_order", "454111": "online_and_mail_order",
    "454113": "online_and_mail_order", "454": "nonstore_all",
    "454390": "direct_selling_in_home", "45439": "direct_selling_in_home",
    "4543": "direct_selling_in_home",
    "442291": "window_treatment_specialist",
    "444110": "home_center", "4441": "home_center",
    # 2022 NAICS — 449122 now contains BOTH the storefronts and the online-only sellers
    "449122": "window_treatment_specialist_incl_online",
}


def _pull(p: dict) -> list[dict]:
    base = f"https://api.census.gov/data/{p['year']}/{p['dataset']}"
    fields = [p["naics_var"], f"{p['naics_var']}_LABEL", p["code_var"],
              p["dollars"], p["share"], "ESTAB"]
    params = {"get": ",".join(fields), p["code_var"]: p["code"], "for": "us:*",
              "key": ENV["CENSUS_API_KEY"]}
    recs = census_rows(get(base, params=params, timeout=90).json())
    save_raw(SOURCE, f"{p['year']}-{p['code']}", recs)

    rows = []
    for r in recs:
        naics = r.get(p["naics_var"], "")
        try:
            dollars = float(r.get(p["dollars"]) or 0)
        except ValueError:
            dollars = 0.0
        try:
            share = float(r.get(p["share"]) or 0)
        except ValueError:
            share = 0.0
        rows.append({
            "year": p["year"], "product_code": p["code"], "product_line": p["label"],
            "naics": naics, "naics_label": r.get(f"{p['naics_var']}_LABEL", ""),
            "channel": CHANNEL.get(naics, ""),
            "sales_usd_k": dollars, "share_of_line_pct": share,
            "establishments": r.get("ESTAB", ""),
        })
    record(SOURCE, f"{p['year']}-window-treatment-line", base, len(rows),
           note=f"{p['dataset']} {p['year']} product line {p['code']} by industry")
    return rows


def main() -> None:
    if not ENV.get("CENSUS_API_KEY"):
        log(f"→ {SOURCE}: SKIPPED — no CENSUS_API_KEY "
            "(free, instant: https://api.census.gov/data/key_signup.html)")
        record(SOURCE, "window-treatment-line", "https://api.census.gov/data/2017/ecnnapcsprd",
               0, status="blocked_no_credential", note="CENSUS_API_KEY not set")
        return

    with guard(SOURCE, "window-treatment-line", "https://api.census.gov/data/2017/ecnnapcsprd"):
        rows = []
        for p in PULLS:
            try:
                rows += _pull(p)
            except Exception as exc:  # noqa: BLE001 — one vintage failing must not lose the rest
                log(f"  {p['year']}/{p['dataset']}: {str(exc)[:100]}")
        save_csv("window_treatment_merch_line", rows)

        # The all-retail rate for the SAME year, so the category's share means something.
        # Owned by t2_census_arts_ecommerce.py; read, never re-parsed.
        benchmark = {int(r["year"]): float(r["ecommerce_share"])
                     for r in read_csv("retail_ecommerce_total_by_year") if r.get("year")}

        summary = []
        for p in PULLS:
            year_rows = [r for r in rows if r["year"] == p["year"]]
            if not year_rows:
                continue
            # The "total for all sectors" row, where the census publishes one.
            total = next((r["sales_usd_k"] for r in year_rows
                          if r["naics"] in ("00", "44-45")), 0.0)
            # 6-digit rows only: the parent codes repeat their children's dollars.
            def channel_sum(*names):
                return sum(r["sales_usd_k"] for r in year_rows
                           if r["channel"] in names and len(r["naics"]) == 6)

            # Under 2022 NAICS no industry isolates the online sellers, so the answer is
            # "not separable" — which is not the same as zero and must never print as 0%.
            separable = any(r["channel"] == "online_and_mail_order" for r in year_rows)
            online = channel_sum("online_and_mail_order") if separable else None
            visit = channel_sum("direct_selling_in_home", "window_treatment_specialist")
            bench = benchmark.get(p["year"])
            share = round(online / total, 4) if separable and total else None
            summary.append({
                "year": p["year"], "product_code": p["code"], "product_line": p["label"],
                "line_total_usd_k": total,
                "channel_separable": separable,
                "online_and_mail_order_usd_k": online,
                "online_share_of_line": share,
                "visit_channels_usd_k": visit if separable else None,
                "visit_share_of_line": (round(visit / total, 4)
                                        if separable and total else None),
                "all_retail_ecommerce_share": bench,
                "ratio_to_all_retail": round(share / bench, 2) if share and bench else None,
            })
        save_csv("window_treatment_online_share", summary)
        record(SOURCE, "window-treatment-online-share", "derived", len(summary),
               note="online share of the window-treatment line vs the all-retail rate")

        log("")
        for s in summary:
            log(f"  {s['year']} · {s['product_line'][:58]}")
            log(f"    line total            ${s['line_total_usd_k']*1000/1e9:>6.2f}bn")
            if s["online_share_of_line"] is not None:
                log(f"    online + mail order   ${s['online_and_mail_order_usd_k']*1000/1e9:>6.2f}bn"
                    f"   {s['online_share_of_line']:>6.1%}")
                log(f"    visit-based channels  ${s['visit_channels_usd_k']*1000/1e9:>6.2f}bn"
                    f"   {s['visit_share_of_line']:>6.1%}")
                log(f"    all US retail online              {s['all_retail_ecommerce_share']:>6.1%}"
                    f"   ({s['ratio_to_all_retail']}x)")
            else:
                log("    online share          not separable — 2022 NAICS folded the "
                    "online-only sellers into the storefront industries")
            log("")


if __name__ == "__main__":
    main()
