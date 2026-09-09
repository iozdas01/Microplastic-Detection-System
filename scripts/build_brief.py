#!/usr/bin/env python3
"""Generate reports/BRIEF.md — the canonical session entry point for the idea.

WHY THIS EXISTS
---------------
Before this file, the cheapest artifact to read (`STATUS.md`, one line, hand-written)
was the stalest, while the freshest facts sat inside a 123 KB `contacts.md`. A session
that behaved economically read the wrong thing. On 2026-08-06 that cost us a real
contradiction: `STATUS.md` claimed H004 was active for a day after H004 had been folded
into an offering, while the lineage frontmatter correctly said H003.

BRIEF.md inverts the incentive. It is the cheapest thing to read AND the freshest,
because it is derived — every number here is computed from the source files at build
time, so it cannot disagree with them.

WHAT IT IS NOT
--------------
Not a hand-written "current state" file (banned by CLAUDE.md). It lives inside
`reports/` and is generated. It holds no fact that is not derived from an authored
source, so it can never become an independent source of truth. Nothing here records
which hunch is active: the hunch has exactly one author (`hunch-lineage.md`
frontmatter), which is what makes a STATUS-vs-lineage contradiction structurally
unrepresentable rather than merely fixed.

Reads (all optional — a stage not reached yet renders as "none yet"):
    input-context/belief.md                  the durable belief
    reports/01-ideation/hunch-lineage.md     hunch tree + active hunch
    reports/02-assumptions/graph.md          assumptions + status
    reports/03-validation/evidence.md        evidence ledger
    reports/04-mutation/offerings.md         candidate offerings
    reports/outreach/contacts.md             contacts

Writes:
    reports/BRIEF.md

Usage:
    python3 scripts/build_brief.py
    python3 scripts/build_brief.py --check     # exit 1 if BRIEF.md is stale

Overwrite is always safe. Anything wrong on this page is wrong in a source file.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.idea import (  # noqa: E402 — one parsing authority, see scripts/idea.py
    BELIEF,
    _HAS_YAML,
    DATED_PART,
    compute_conversion_stats,
    compute_stats,
    derive_assumption_evidence,
    evidence_label,
    extract_belief as _extract_belief,
    idea_name,
    parse_contacts_md,
    parse_evidence_md,
    parse_graph_md,
    parse_lineage_md,
    parse_offerings_md,
)

REPO = Path(__file__).resolve().parent.parent
REPORTS = REPO / "reports"

MAX_ASSUMPTIONS = 3
MAX_EVIDENCE = 4


# ─── helpers ─────────────────────────────────────────────────────────────────


def _digest(path: Path) -> str:
    """Short content hash. `--check` compares these to detect a stale brief."""
    if not path.exists():
        return "absent"
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def _as_int(v, default: int = 0) -> int:
    try:
        return int(v)
    except (TypeError, ValueError):
        return default


def _one_line(s, limit: int = 200) -> str:
    text = " ".join(str(s or "").split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def _purpose(path: Path) -> str:
    """One line saying what a file is for, authored by the file itself.

    Read in order: frontmatter `purpose:`, frontmatter `title:`, first markdown
    heading. Nothing is curated in this script on purpose — a lookup table here
    would be a second author for a fact the artifact already owns, and it would
    silently omit any artifact nobody remembered to register.
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return "—"

    lines = text.splitlines()
    start = 0
    while start < len(lines) and not lines[start].strip():
        start += 1

    fm_end = None
    if start < len(lines) and lines[start].strip() == "---":
        # Generous scan: some artifacts carry a long structured frontmatter block
        # (llm-to-robotics-map.md's plays list runs past 120 lines).
        for i in range(start + 1, min(len(lines), start + 600)):
            if lines[i].strip() == "---":
                fm_end = i
                break

    if fm_end is not None:
        for key in ("purpose", "title"):
            for i in range(start + 1, fm_end):
                stripped = lines[i].strip()
                if not stripped.startswith(key + ":"):
                    continue
                value = stripped[len(key) + 1:].strip()
                if value in (">", "|", ">-", "|-"):  # folded block: take its body
                    body = []
                    for j in range(i + 1, fm_end):
                        if lines[j].strip() and not lines[j].startswith((" ", "\t")):
                            break
                        body.append(lines[j].strip())
                    value = " ".join(b for b in body if b)
                return _one_line(value.strip("\"'"), 150) or "—"

    body_start = (fm_end + 1) if fm_end is not None else start
    for line in lines[body_start:]:
        if line.startswith("# "):
            return _one_line(line[2:], 150)
    if _is_generated(path) or path.suffix == ".html":
        return "generated — rebuild it, never edit it"
    return "—"


def _is_generated(path: Path) -> bool:
    """A generated file announces itself in its first lines; every generator here
    writes that banner. Checked separately from `_purpose` because a generated file
    also has a heading, and the heading wins there."""
    try:
        return "GENERATED" in path.read_text(encoding="utf-8", errors="replace")[:2000]
    except OSError:
        return False


_DATE_IN_NAME = re.compile(r"[-_]?(\d{4}-\d{2}-\d{2})")


def _series_rows(rel_parent: Path, files: list[Path]) -> list[tuple[str, str]]:
    """One row per artifact — except a repeated series, which gets one row for all of it.

    A directory that gains one file per run (four dated target-list audits, one
    generated results file per assumption) otherwise spends a row per run, and the
    inventory grows linearly with activity until it is too long to scan. Collapsing
    a series keeps the concept visible while the row count stays flat.

    Only same-prefix families collapse, and only at two or more members: a lone dated
    file is just an artifact, and hiding a living artifact behind a count is the exact
    failure this section exists to prevent.
    """
    groups: dict[tuple[str, str], list[Path]] = {}
    order: list[tuple[str, str]] = []
    for path in files:
        if _DATE_IN_NAME.search(path.stem):
            key = ("dated", _DATE_IN_NAME.sub("", path.stem).strip("-_") or path.stem)
        elif _is_generated(path):
            key = ("generated", path.stem.split("-")[0])
        else:
            key = ("single", path.name)
        if key not in groups:
            order.append(key)
        groups.setdefault(key, []).append(path)

    rows: list[tuple[str, str]] = []
    for key in order:
        kind, prefix = key
        members = groups[key]
        if kind == "single" or len(members) < 2:
            for path in members:
                rows.append((str(path.relative_to(REPO)), _purpose(path)))
            continue
        newest = max(members, key=lambda p: p.name)
        pattern = "%s/%s-*%s" % (rel_parent, prefix, newest.suffix)
        if kind == "dated":
            rows.append((pattern, "%d dated snapshots — latest %s · %s" % (
                len(members), _DATE_IN_NAME.search(newest.stem).group(1), _purpose(newest))))
        else:
            rows.append((pattern, "%d generated files — rebuild them, never edit" % len(members)))
    return rows


def _inventory(idea: Path, belief: Path) -> list[str]:
    """Every artifact that already exists for this idea, with its own purpose line.

    This section is the answer to "does something covering X already exist?" — the
    question that has to be answerable from the entry point, because a session that
    cannot answer it writes a second file about the same fact. Directories holding
    many same-shaped files (interviews, method runs, recon dumps) collapse to one
    counted row so the brief stays scannable.
    """
    # Collapse ONLY dated run folders (method runs, recon dumps, campaign batches),
    # never a living folder. The first version of this collapsed any folder over four
    # files and hid `outreach/companies.md` behind "9 files" — which is the exact
    # failure this section exists to prevent.
    COLLAPSE_AT = 4
    rows: list[tuple[str, str]] = []

    if belief.exists():
        rows.append((str(belief.relative_to(REPO)), _purpose(belief)))
    extra = sorted(p for p in belief.parent.glob("*") if p.is_file() and p != belief) if belief.parent.exists() else []
    if extra:
        rows.append((str(belief.parent.relative_to(REPO)) + "/", "%d%s staged input file%s" % (
            len(extra),
            " more" if belief.exists() else "",
            "" if len(extra) == 1 else "s")))

    if idea.exists():
        by_dir: dict[Path, list[Path]] = {}
        for path in sorted(idea.rglob("*")):
            if not path.is_file() or path.name == "BRIEF.md" or path.name.startswith("."):
                continue
            by_dir.setdefault(path.parent, []).append(path)

        for parent in sorted(by_dir):
            files = by_dir[parent]
            rel_parent = parent.relative_to(REPO)
            if len(files) > COLLAPSE_AT and DATED_PART.search(str(parent.relative_to(idea))):
                rows.append(("%s/" % rel_parent, "%d files — open the folder to see them" % len(files)))
                continue
            rows.extend(_series_rows(rel_parent, files))

    if not rows:
        return []

    out = ["## What already exists for this idea", ""]
    out.append("_Generated from the folder. Check here before creating a new artifact — if a file"
               " already covers the fact, add to it instead of writing a second author for it._")
    out.append("")
    out.append("| Artifact | What it holds |")
    out.append("|---|---|")
    for rel, purpose in rows:
        out.append("| `%s` | %s |" % (rel, purpose.replace("|", "\\|")))
    out.append("")
    return out


def _safe(parser, path, empty):
    """Every source is optional — an idea missing a stage renders as 'none yet'.

    `parse_contacts_md` raises on a missing file where the other parsers return
    empty, so the guard lives here rather than changing tracker behaviour the
    dashboard already depends on.
    """
    if not path.exists():
        return empty
    try:
        return parser(path)
    except Exception as e:  # a malformed source must not block the whole brief
        print("[warn] %s failed to parse: %s" % (path.name, e), file=sys.stderr)
        return empty


# ─── ranking ─────────────────────────────────────────────────────────────────


def rank_assumptions(assumptions):
    """THE authoritative implementation of the Leap-of-Faith ranking.

    1. Gate on the Leap of Faith quadrant, unsettled — everything else exits here.
    2. DAG position: roots before their unconfirmed children.
    3. kill_power tier, higher first.
    4. uncertainty tier, higher first.
    5. test_cost tie-break, cheaper first.

    `schemas/assumptions.md` states WHY these criteria in this order (a dominance
    ordering absorbs the wobble in LLM-judged scores that a ratio would propagate).
    It defers to this function for the ordering itself, so the two cannot drift into
    a disagreement that resolves silently in favour of the code.

    The procedure was specified from the day the schema was written and never
    executed until 2026-08-07, so "top 3" meant whatever the reader judged that
    session. Running it makes a mis-scored node visible as a wrong ORDER rather than
    an invisible opinion.
    """
    by_id = {a.get("id"): a for a in assumptions if a.get("id")}
    settled = {"confirmed", "killed"}

    def is_root(a):
        # A node is a root for ranking purposes when no parent is still unconfirmed.
        for pid in a.get("parent_assumptions") or []:
            parent = by_id.get(pid)
            if parent is not None and (parent.get("status") or "") not in settled:
                return False
        return True

    pool = [
        a
        for a in assumptions
        if (a.get("quadrant") or "") == "leap_of_faith"
        and (a.get("status") or "") not in settled
    ]
    return sorted(
        pool,
        key=lambda a: (
            0 if is_root(a) else 1,
            -_as_int(a.get("kill_power")),
            -_as_int(a.get("uncertainty_score")),
            _as_int(a.get("test_cost"), 99),
            str(a.get("id") or ""),
        ),
    )


# ─── rendering ───────────────────────────────────────────────────────────────


def _sources() -> dict[str, Path]:
    """The six authored files the brief is derived from. One definition, used by
    both the builder and the staleness check so they cannot disagree."""
    return {
        "belief": BELIEF,
        "lineage": REPORTS / "01-ideation" / "hunch-lineage.md",
        "graph": REPORTS / "02-assumptions" / "graph.md",
        "evidence": REPORTS / "03-validation" / "evidence.md",
        "offerings": REPORTS / "04-mutation" / "offerings.md",
        "contacts": REPORTS / "outreach" / "contacts.md",
    }


def build() -> Path:
    idea = REPORTS
    title = idea_name()
    src = _sources()

    lfm, hunches = _safe(parse_lineage_md, src["lineage"], ({}, []))
    gfm, assumptions = _safe(parse_graph_md, src["graph"], ({}, []))
    _patterns, entries = _safe(parse_evidence_md, src["evidence"], ([], []))
    derive_assumption_evidence(assumptions, entries)
    _ofm, offerings = _safe(parse_offerings_md, src["offerings"], ({}, []))
    cfm, contacts = _safe(parse_contacts_md, src["contacts"], ({}, []))

    belief = _safe(_extract_belief, src["belief"], "")
    # `active_hunch` accepts a scalar or a list. An idea probing one transaction
    # through more than one entry point runs a hunch per door in parallel; the
    # one-active-hunch rule binds shotguns, not validation (schemas/hunch.md r2).
    _ah = lfm.get("active_hunch")
    active_ids = [str(h).strip() for h in (_ah if isinstance(_ah, list) else [_ah]) if h]
    active_hunch = ", ".join(active_ids)
    active_assumption = gfm.get("active_assumption")

    L = []
    L.append("<!-- GENERATED by scripts/build_brief.py — DO NOT EDIT.")
    L.append("     Every value below is derived. Fix the source file, then rerun:")
    L.append("       python3 scripts/build_brief.py")
    L.append("-->")
    L.append("---")
    L.append("idea: %s" % title)
    L.append("generated: %s" % datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"))
    L.append("active_hunch: %s" % (active_hunch or "none"))
    L.append("active_assumption: %s" % (active_assumption or "none"))
    L.append("sources:")
    for name, path in src.items():
        L.append("  %s: %s" % (name, _digest(path)))
    L.append("---")
    L.append("")
    L.append("# %s — session brief" % title)
    L.append("")
    L.append(
        "_Generated digest. Load this first; load a full source file only for the task "
        "that needs it (pointers at the end)._"
    )
    L.append("")

    # ── belief ──
    L.append("## Belief")
    L.append("")
    if belief:
        L.append("> %s" % _one_line(belief, 400))
        L.append("")
        L.append("_Founder-owned. Changes only with explicit confirmation._ → `%s`"
                 % src["belief"].relative_to(REPO))
    else:
        L.append("_No `belief.md` — run `/startup-belief-intake` before any shotgun._")
    L.append("")

    # ── hunch ──
    L.append("## Hunch")
    L.append("")
    if hunches:
        if len(active_ids) > 1:
            L.append("_%d hunches active in parallel — one per entry point into the same "
                     "transaction. They share a root assumption; evidence on one door does "
                     "not transfer to the other._" % len(active_ids))
            L.append("")
        for hid in (active_ids or [None]):
            active = next((h for h in hunches if h.get("id") == hid), None)
            if active:
                L.append("**%s — active** · `%s`" % (active.get("id"),
                                                     active.get("validation_status") or "untested"))
                stmt = active.get("statement") or active.get("change_reason") or ""
                if stmt:
                    L.append("")
                    L.append(_one_line(stmt, 320))
                    L.append("")
            else:
                L.append("**%s** — declared active in the lineage frontmatter, but no matching "
                         "`## %s` block was found. Fix the lineage file."
                         % (hid or "none", hid or "?"))
                L.append("")
        while L and L[-1] == "":
            L.pop()
        others = [h for h in hunches if h.get("id") not in active_ids]
        if others:
            L.append("")
            L.append("Lineage: " + " · ".join(
                "%s %s" % (h.get("id"), h.get("status") or "?") for h in others))
    else:
        L.append("_No hunch yet — run `/startup-ideate-shotgun` in explore mode once a belief exists._")
    L.append("")

    # ── assumptions ──
    ranked = rank_assumptions(assumptions)
    L.append("## Assumptions — top %d of %d by the declared ranking"
             % (min(MAX_ASSUMPTIONS, len(ranked)), len(assumptions)))
    L.append("")
    if ranked:
        L.append("| # | ID | claim | status | evidence | next action |")
        L.append("|---|---|---|---|---|---|")
        for i, a in enumerate(ranked[:MAX_ASSUMPTIONS], 1):
            marker = " ←" if a.get("id") == active_assumption else ""
            L.append("| %d | **%s**%s | %s | `%s` | `%s` | %s |" % (
                i,
                a.get("id"),
                marker,
                _one_line(a.get("assumption"), 110),
                a.get("status") or "?",
                evidence_label(a),
                _one_line(a.get("next_action"), 90) or "—",
            ))
        L.append("")
        L.append("_← = `active_assumption`. Ranking: leap-of-faith gate → DAG roots first → "
                 "kill_power → uncertainty → cheapest test (`schemas/assumptions.md`)._")
        if active_assumption and ranked and ranked[0].get("id") != active_assumption:
            L.append("")
            L.append("> ⚠️ `active_assumption` is **%s** but the ranking puts **%s** first. "
                     "Either a score is wrong or the choice was deliberate — say which."
                     % (active_assumption, ranked[0].get("id")))
    elif assumptions:
        L.append("_%d assumptions, none in the leap-of-faith quadrant and unsettled — "
                 "nothing is queued for testing._" % len(assumptions))
    else:
        L.append("_No assumption graph yet — run `/startup-idea-to-assumptions`._")
    L.append("")

    # ── evidence ──
    L.append("## Evidence")
    L.append("")
    if entries:
        verdicts = {"supports": 0, "contradicts": 0, "ambiguous": 0}
        for e in entries:
            v = (e.get("verdict") or "").strip()
            if v in verdicts:
                verdicts[v] += 1
        dates = sorted(str(e.get("date")) for e in entries if e.get("date"))
        L.append("**%d entries** · %d supports / %d contradicts / %d ambiguous · latest %s"
                 % (len(entries), verdicts["supports"], verdicts["contradicts"],
                    verdicts["ambiguous"], dates[-1] if dates else "—"))
        if active_assumption:
            mine = [e for e in entries
                    if str(e.get("assumption_linked") or "") == str(active_assumption)]
            L.append("")
            L.append("For **%s**: %d entries." % (active_assumption, len(mine)))
        recent = sorted(entries, key=lambda e: str(e.get("date") or ""), reverse=True)
        L.append("")
        for e in recent[:MAX_EVIDENCE]:
            L.append("- `%s` %s → **%s** (%s) — %s" % (
                e.get("id"),
                e.get("date") or "?",
                e.get("assumption_linked") or "?",
                e.get("verdict") or "?",
                _one_line(e.get("claim"), 150),
            ))
    else:
        L.append("_No evidence ledger yet._")
    L.append("")

    # ── outreach ──
    L.append("## Outreach")
    L.append("")
    if contacts:
        st = compute_stats(contacts)
        cv = compute_conversion_stats(contacts)
        L.append("**%d targeted** · %d contacted · %d replied · %d call-progressed · %d scheduled"
                 % (cv.get("targeted", 0), cv.get("contacted", 0), cv.get("replied", 0),
                    cv.get("call_progressed", 0), cv.get("scheduled", 0)))
        L.append("")
        L.append("Reply rate %s%% of contacted · reply→call %s%%"
                 % (cv.get("reply_rate", 0), cv.get("reply_to_call_rate", 0)))
        by_a = cv.get("by_assumption") or {}
        if by_a:
            L.append("")
            L.append("By assumption: " + " · ".join(
                "%s %d/%d replied" % (k, v.get("replied", 0), v.get("contacted", 0))
                for k, v in sorted(by_a.items())))
        empty_tiers = [t for t, n in (st.get("by_tier") or {}).items() if not n]
        if empty_tiers:
            L.append("")
            L.append("Empty tiers (no contact tests these): " + ", ".join(sorted(empty_tiers)))
        for key in ("invite_cap_status", "inbox_check_status"):
            if cfm.get(key):
                L.append("")
                L.append("**%s:** %s" % (key.replace("_", " "), _one_line(cfm[key], 220)))
    else:
        L.append("_No contacts yet._")
    L.append("")

    # ── offerings ──
    if offerings:
        L.append("## Offerings")
        L.append("")
        L.append("%d candidate%s, none validated or priced: %s" % (
            len(offerings),
            "" if len(offerings) == 1 else "s",
            ", ".join("`%s`" % o.get("id") for o in offerings if o.get("id")),
        ))
        L.append("")

    # ── inventory ──
    L.extend(_inventory(idea, src["belief"]))

    # ── pointers ──
    L.append("## Load next, by task")
    L.append("")
    L.append("| Task | File |")
    L.append("|---|---|")
    for label, key in (
        ("belief / intake", "belief"),
        ("hunch work", "lineage"),
        ("assumption work", "graph"),
        ("evidence review", "evidence"),
        ("outreach", "contacts"),
        ("offerings", "offerings"),
    ):
        if src[key].exists():
            L.append("| %s | `%s` |" % (label, src[key].relative_to(REPO)))
    L.append("")
    L.append("Dashboard: `python3 scripts/build_control_room.py`")

    out = idea / "BRIEF.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    return out


def is_stale() -> bool:
    """True when BRIEF.md is missing or its recorded source hashes no longer match."""
    brief = REPORTS / "BRIEF.md"
    if not brief.exists():
        return True
    recorded = {}
    for line in brief.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("---") and recorded:
            break
        parts = stripped.split(": ")
        if len(parts) == 2 and parts[0] in (
            "belief", "lineage", "graph", "evidence", "offerings", "contacts"
        ):
            recorded[parts[0]] = parts[1]
    if not recorded:
        return True
    live = {k: _digest(v) for k, v in _sources().items()}
    return any(live[k] != v for k, v in recorded.items() if k in live)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if BRIEF.md is stale; write nothing")
    args = ap.parse_args()

    if not _HAS_YAML:
        sys.exit("PyYAML is required: pip3 install -r requirements.txt")

    if args.check:
        if is_stale():
            print("[stale] reports/BRIEF.md — run: python3 scripts/build_brief.py")
            sys.exit(1)
        print("BRIEF.md current.")
        return

    if not REPORTS.is_dir():
        sys.exit("no reports/ folder — run scripts/setup.sh")
    print("[ok] wrote %s" % build().relative_to(REPO))


if __name__ == "__main__":
    main()
