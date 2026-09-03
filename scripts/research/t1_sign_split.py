"""Tier 1 — is "custom signs" a fabrication market or a printing market?

The cross-material sweep put signs & display at the top of measurable made-to-order demand
(2.43x the "custom furniture" anchor). That number is only useful if the demand is for
something a CNC machine makes. A printed yard sign on corrugated plastic is a wide-format
printer and a knife; a channel-letter storefront sign is bent aluminium, a router, acrylic
and an LED harness. Those are different companies, and the sweep scored them as one.

So this splits the family in two and measures each side:

  printed      wide-format ink on a flat substrate — vinyl, corrugated plastic, fabric.
               No machining. If the family's demand lives here, signs are not our market.
  fabricated   cut, bent, routed, engraved or assembled — metal, acrylic, wood, neon/LED.
               This is the side a machine shop can actually serve.

ANCHOR NOTE: anchored on "custom neon sign" (mean index 5.4), NOT on "custom signs" (39.4).
The parent term is 7x the largest sub-term, and anchoring on it quantised every fabricated
sub-term to zero — "channel letter sign" measured 0.19 against it. The anchor is therefore
mid-scale within the family, and `custom signs` is carried in the term list itself so the
chain back to the cross-material sweep stays computable rather than assumed.
"""
from __future__ import annotations

import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import guard, log, record  # noqa: E402
from t1_demand_sweep import run_sweep  # noqa: E402
from t1_google_trends import GEO, TIMEFRAME, Trends  # noqa: E402

SOURCE = "google-trends"
# Mid-scale within the family. See the ANCHOR NOTE above before changing this.
ANCHOR = "custom neon sign"

# (term, side, buyer, vocabulary) — `side` is the whole point of this sweep.
TERMS: list[tuple[str, str, str, str]] = [
    # ── the parent term, carried so the scale chains back to the wider sweep ──
    ("custom signs",            "parent",     "mixed",    "object"),

    # ── PRINTED — ink on a flat substrate, no machining ───────────────────
    ("custom yard signs",       "printed",    "mixed",    "object"),
    ("custom banners",          "printed",    "mixed",    "object"),
    ("custom stickers",         "printed",    "mixed",    "object"),
    ("custom decals",           "printed",    "mixed",    "object"),
    ("custom vinyl signs",      "printed",    "mixed",    "object"),
    ("custom car magnets",      "printed",    "business", "object"),

    # ── FABRICATED — cut, bent, routed, engraved, assembled ───────────────
    ("custom metal signs",      "fabricated", "mixed",    "object"),
    ("custom wood signs",       "fabricated", "consumer", "object"),
    ("custom acrylic sign",     "fabricated", "mixed",    "object"),
    ("custom led signs",        "fabricated", "mixed",    "object"),
    ("channel letter sign",     "fabricated", "business", "object"),
    ("dimensional letters",     "fabricated", "business", "object"),
    ("custom monument sign",    "fabricated", "business", "object"),
    ("custom lobby sign",       "fabricated", "business", "object"),
    ("custom address plaque",   "fabricated", "consumer", "object"),
    ("custom door sign",        "fabricated", "business", "object"),

    # ── AMBIGUOUS — could be either; measured rather than assigned ────────
    ("custom business signs",   "ambiguous",  "business", "object"),
    ("custom storefront sign",  "ambiguous",  "business", "object"),
    ("custom bar sign",         "ambiguous",  "consumer", "object"),
]

META = {t: (side, buyer, vocab) for t, side, buyer, vocab in TERMS}


def main() -> None:
    with guard(SOURCE, "sign-split", "trends.google.com"):
        tr = Trends()
        # Longer batch sleep than the wide sweep: the wide sweep plus the magnitude probes
        # already drew a 429 from this IP today.
        rows, related = run_sweep(tr, ANCHOR, META, "sign-split", "sign_split",
                                  batch_sleep=6.0)
        record(SOURCE, "sign-split", "trends.google.com", len(rows) + len(related),
               note=f"anchor='{ANCHOR}' geo={GEO} timeframe={TIMEFRAME} "
                    f"terms={len(META)} resolved={sum(1 for r in rows if r['resolved'])}")

        sides: dict[str, list[dict]] = {}
        for r in rows:
            sides.setdefault(r["family"], []).append(r)

        log("")
        log(f"  Interest relative to '{ANCHOR}' = 1.000 ({GEO}, {TIMEFRAME}):")
        log(f"    {'keyword':<26}{'side':<12}{'buyer':<10}{'vs':>8}  {'res':<5}{'yoy':>8}")
        for r in rows:
            yoy = f"{r['momentum_yoy']:+.0%}" if r["momentum_yoy"] is not None else "    —"
            flag = "ok" if r["resolved"] else "THIN"
            log(f"    {r['keyword']:<26}{r['family']:<12}{r['buyer']:<10}"
                f"{r['vs_anchor']:>8.3f}  {flag:<5}{yoy:>8}")

        log("")
        log("  SIDE TOTALS — resolved terms only")
        for side in ("printed", "fabricated", "ambiguous", "parent"):
            rs = [r for r in sides.get(side, []) if r["resolved"]]
            allr = sides.get(side, [])
            tot = sum(r["vs_anchor"] for r in rs)
            log(f"    {side:<12}{tot:>8.3f}  ({len(rs)} of {len(allr)} terms resolved)")


if __name__ == "__main__":
    main()
