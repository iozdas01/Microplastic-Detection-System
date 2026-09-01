"""Rank customisable furniture by US search demand — on the instrument that can resolve it.

The obvious approach does not work, and the reason matters. Anchoring every term against
"dining table" makes the whole keyword set comparable, but Google Trends returns an
integer 0-100 index scaled to the largest term in the batch. Next to a generic article
term, "custom dining chair" quantises to zero in 95% of weeks and never exceeds 1. There
is no ordering to recover from that: it is a resolution floor, not a measurement.

So this reads two instruments and uses each for what it can actually answer:

  RANK    the custom-category sweep, where every term is a "custom X" anchored on
          "custom furniture". Terms of comparable magnitude, so the index has real
          resolution and both level and direction can be read off it.
  SHARE   the generic/custom pairs, which can still answer "is this category customised
          at all" to one significant figure — every custom term sits under 1% of its
          generic term — but cannot rank the custom terms against each other.

Every row carries the share of weeks its index sat at or below 1. Anything above the
resolution threshold is reported as unresolved rather than ranked, because a number that
is 95% zeros is not a small number, it is an absent one.
"""
from __future__ import annotations

import sys
from collections import defaultdict

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import log, read_csv, record, save_csv  # noqa: E402

# custom term -> the generic term it is a customisation of, for the share question
GENERIC_OF = {
    "custom dining table": "dining table", "custom dining chair": "dining chair",
    "custom accent chair": "accent chair", "custom coffee table": "coffee table",
    "custom console table": "console table", "custom desk": "desk",
    "custom bed frame": "bed frame", "custom dresser": "dresser",
    "custom nightstand": "nightstand", "custom bookshelf": "bookshelf",
    "custom tv stand": "tv stand", "custom wardrobe": "wardrobe",
    "custom bench": "bench", "custom sofa": "sofa",
    "custom closet": "closet organizer", "custom cabinets": "kitchen cabinets",
}
# Categories that are not free-standing furniture. Kept in the table, flagged, and
# excluded from the headline pick — they are the adjacency, not the article.
NOT_FURNITURE = {"custom cabinets", "custom closet", "custom built ins",
                 "custom kitchen island", "custom vanity", "custom mantel",
                 "custom shelving", "custom bar", "custom outdoor furniture"}

RECENT_WEEKS = 52
RESOLUTION_LIMIT = 0.80   # above this share of weeks at index <=1, treat as unresolved
COMMERCIAL = ["near me", "cost", "price", "companies", "designer", "builder",
              "installation", "quote", "contractor", "maker", "custom made"]


def mean(xs):
    xs = list(xs)
    return sum(xs) / len(xs) if xs else 0.0


def main() -> None:
    tl = read_csv("trends_custom_timeline")
    cats = read_csv("trends_custom_categories")
    pairs_ts = read_csv("trends_interest_over_time")
    adjusted = read_csv("custom_categories_adjusted")
    related = read_csv("trends_custom_related")
    if not cats:
        log("analyse_custom_demand: run t1_custom_categories.py first")
        return
    if not tl:
        log("analyse_custom_demand: no trends_custom_timeline — re-run "
            "t1_custom_categories.py to capture the weekly series")

    # --- a guard against a shared artifact ---------------------------------------------
    # If most terms peak in the same week, that is not demand. Independent queries in
    # independent batches do not agree on a single week by chance, and a synchronised
    # peak makes every year-on-year comparison a measurement of the artifact instead.
    # Detected rather than assumed, so the guard keeps working on future data.
    def peak_week(pts):
        return max(pts, key=lambda kv: kv[1])[0] if pts else None

    # --- series off the custom-category sweep (good resolution) ------------------------
    ser: dict[str, list[tuple[int, float]]] = defaultdict(list)
    for r in tl:
        try:
            ser[r["keyword"]].append((int(r["timestamp"]), float(r["raw_index"])))
        except (KeyError, ValueError):
            continue
    ser = {k: sorted(set(v)) for k, v in ser.items()}

    peaks = [peak_week(v) for v in ser.values() if v]
    shared_peak, momentum_usable = None, True
    if peaks:
        common, n = max(((p, peaks.count(p)) for p in set(peaks)), key=lambda x: x[1])
        if n / len(peaks) > 0.5:
            shared_peak, momentum_usable = common, False

    # --- the pair series, used only for the share question ---------------------------
    pair_mean: dict[str, float] = {}
    acc = defaultdict(list)
    for r in pairs_ts:
        try:
            acc[r["keyword"]].append(float(r["anchor_scaled"]))
        except (KeyError, ValueError):
            continue
    pair_mean = {k: mean(v) for k, v in acc.items()}

    furn = {r["keyword"]: r for r in adjusted}
    intent = defaultdict(int)
    for r in related:
        if r["kind"] == "top" and any(w in r["query"].lower() for w in COMMERCIAL):
            intent[r["seed_term"]] += 1

    rows = []
    for c in cats:
        term = c["keyword"]
        if c.get("is_anchor") == "True":
            continue
        pts = ser.get(term, [])
        vals = [v for _, v in pts]
        unresolved_share = (sum(1 for v in vals if v <= 1) / len(vals)) if vals else None
        resolved = unresolved_share is not None and unresolved_share <= RESOLUTION_LIMIT

        mom = None
        if momentum_usable and resolved and len(pts) >= RECENT_WEEKS * 2:
            recent = mean(vals[-RECENT_WEEKS:])
            prior = mean(vals[-RECENT_WEEKS * 2:-RECENT_WEEKS])
            mom = (recent / prior - 1) if prior else None

        generic = GENERIC_OF.get(term)
        g_lvl, c_lvl = pair_mean.get(generic), pair_mean.get(term)
        share = (c_lvl / g_lvl) if (g_lvl and c_lvl) else None

        adj = furn.get(term, {})
        try:
            fshare = float(adj["furniture_share_of_related"]) \
                if adj.get("furniture_share_of_related") not in (None, "", "None") else None
        except (KeyError, ValueError):
            fshare = None

        rows.append({
            "custom_term": term,
            "generic_term": generic or "",
            "level_vs_custom_furniture": float(c["vs_custom_furniture"]),
            "mean_index": float(c["mean_index"]),
            "weeks_at_or_below_1": round(unresolved_share, 3)
            if unresolved_share is not None else None,
            "resolved": resolved,
            "momentum_yoy": round(mom, 4) if mom is not None else None,
            "custom_share_of_generic": round(share, 5) if share else None,
            "furniture_share_of_related": fshare,
            "commercial_intent_queries": intent.get(term, 0),
            "free_standing_furniture": term not in NOT_FURNITURE,
        })

    if not rows:
        log("analyse_custom_demand: no categories to rank")
        return

    # Score only what can be resolved. Level does most of the work because the question
    # is how much demand exists; momentum tilts it toward what is growing; the accessory
    # adjustment stops "custom desk" — largely desk mats — outranking real furniture.
    scorable = [r for r in rows if r["resolved"]]
    max_lvl = max((r["level_vs_custom_furniture"] for r in scorable), default=1) or 1
    for r in rows:
        if not r["resolved"]:
            r["demand_score"] = None
            continue
        lvl = r["level_vs_custom_furniture"] / max_lvl
        genuine = 1.0 if r["furniture_share_of_related"] is None \
            else r["furniture_share_of_related"]
        if momentum_usable:
            mom_norm = min(max((r["momentum_yoy"] or 0) + 0.5, 0.0), 1.5) / 1.5
            r["demand_score"] = round(0.55 * lvl + 0.25 * mom_norm + 0.20 * genuine, 4)
        else:
            # No trustworthy direction, so level and genuineness carry the whole score.
            r["demand_score"] = round(0.70 * lvl + 0.30 * genuine, 4)

    rows.sort(key=lambda r: (-(r["demand_score"] or -1),
                             -r["level_vs_custom_furniture"]))
    save_csv("custom_demand_ranking", rows)
    record("analysis", "custom-demand-ranking", "scripts/analyse_custom_demand.py",
           len(rows), note=f"{len(scorable)} of {len(rows)} categories resolved above the "
                           f"Trends index floor; momentum "
                           f"{'used' if momentum_usable else 'suppressed (shared peak)'}")

    if shared_peak:
        import datetime as _dt
        wk = _dt.datetime.fromtimestamp(shared_peak, _dt.UTC).strftime("%Y-%m-%d")
        log(f"  !! {len([p for p in peaks if p == shared_peak])} of {len(peaks)} series "
            f"peak in the same week ({wk}) across independent batches.")
        log("     That is an index artifact, not demand. Momentum is suppressed; the "
            "ranking uses level only.")
    log("  US demand for customisable furniture (Google Trends, US, 5y, "
        "anchored on 'custom furniture'):")
    log(f"    {'term':<26}{'level':>8}{'mom':>8}{'share':>8}{'genuine':>9}"
        f"{'0/1 wks':>9}{'score':>7}")
    for r in rows:
        lvl = f"{r['level_vs_custom_furniture']:.3f}"
        mom = f"{r['momentum_yoy']:+.0%}" if r["momentum_yoy"] is not None else "  —"
        shr = f"{r['custom_share_of_generic']:.2%}" if r["custom_share_of_generic"] else "  —"
        gen = f"{r['furniture_share_of_related']:.0%}" \
            if r["furniture_share_of_related"] is not None else "  —"
        flr = f"{r['weeks_at_or_below_1']:.0%}" if r["weeks_at_or_below_1"] is not None else "—"
        sc = f"{r['demand_score']:.3f}" if r["demand_score"] is not None else "unresolved"
        mark = " " if r["free_standing_furniture"] else "~"
        log(f"   {mark}{r['custom_term'][:25]:<25}{lvl:>8}{mom:>8}{shr:>8}{gen:>9}"
            f"{flr:>9}{sc:>7}")
    log("   ~ = not free-standing furniture (built-in or adjacent trade)")

    furniture_only = [r for r in rows if r["resolved"] and r["free_standing_furniture"]]
    if furniture_only:
        top = furniture_only[0]
        log("")
        log(f"  Best-resolved free-standing furniture: {top['custom_term']} "
            f"(level {top['level_vs_custom_furniture']:.3f}, score {top['demand_score']:.3f})")
    unresolved = [r for r in rows if not r["resolved"]]
    if unresolved:
        log(f"  {len(unresolved)} of {len(rows)} categories sit at or below the Trends "
            f"index floor and cannot be ranked: "
            f"{', '.join(r['custom_term'] for r in unresolved[:6])}"
            f"{' …' if len(unresolved) > 6 else ''}")


if __name__ == "__main__":
    main()
