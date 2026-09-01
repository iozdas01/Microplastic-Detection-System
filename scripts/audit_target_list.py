#!/usr/bin/env python3
"""Audit contacts.md against the ICP declared on each assumption in graph.md.

Usage:
    python3 scripts/audit_target_list.py <slug>
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from scripts.idea import parse_contacts_md as _load_contacts  # noqa: E402


VAGUE_RATIONALE_PATTERNS = [
    r"\badjacent\b", r"\bmight help\b", r"\bpossibly\b", r"\bcould intro\b",
    r"\bwarm path\b(?!.*specific)", r"batch-added",
]


def parse_assumption_icp(graph_text: str, aid: str) -> dict:
    m = re.search(rf"^\s*- id:\s*{re.escape(aid)}\s*$", graph_text, re.MULTILINE)
    if not m:
        return {}
    next_m = re.search(r"^\s*- id:\s*A", graph_text[m.end():], re.MULTILINE)
    end = m.end() + next_m.start() if next_m else len(graph_text)
    block = graph_text[m.start():end]

    icp = {}
    seg_m = re.search(r"icp_segment:\s*>\s*\n((?:\s+.*\n)+)", block)
    if seg_m:
        icp["icp_segment"] = " ".join(l.strip() for l in seg_m.group(1).splitlines()).strip()
    else:
        seg_m = re.search(r"icp_segment:\s*(.+)", block)
        if seg_m:
            icp["icp_segment"] = seg_m.group(1).strip()

    # Two icp_valid_tiers shapes are in use: an inline flat list, e.g.
    #   icp_valid_tiers: [robot_oem_deployment, industrial_automation_provider]
    # and a multi-line list of {name, side} dicts, e.g.
    #   icp_valid_tiers:
    #     - {name: robot_oem_deployment, side: supply}
    #     - {name: enterprise_physical_ai_lab, side: demand}   # trailing comment
    # Only the tier name is needed here — side is what downstream skills use to
    # route demand vs. supply, not what this audit checks a contact's tier against.
    inline_m = re.search(r"icp_valid_tiers:\s*\[(.*?)\]", block)
    if inline_m:
        icp["icp_valid_tiers"] = [t.strip() for t in inline_m.group(1).split(",") if t.strip()]
    else:
        block_m = re.search(r"icp_valid_tiers:\s*\n((?:\s+-\s+.*\n)+)", block)
        icp["icp_valid_tiers"] = (
            re.findall(r"name:\s*([A-Za-z0-9_]+)", block_m.group(1))
            if block_m else []
        )

    titles_m = re.search(r"icp_valid_titles:\s*\n((?:\s+-\s+.*\n)+)", block)
    icp["icp_valid_titles"] = (
        [re.sub(r"^\s+-\s+", "", ln).strip() for ln in titles_m.group(1).splitlines() if ln.strip()]
        if titles_m else []
    )

    scope_m = re.search(r"icp_out_of_scope:\s*\n((?:\s+-\s+.*\n)+)", block)
    if scope_m:
        raw = re.findall(r'\s+-\s+"?([^"\n]+?)"?\s*$', scope_m.group(1), re.MULTILINE)
        icp["icp_out_of_scope"] = [x.strip() for x in raw]
    else:
        icp["icp_out_of_scope"] = []
    return icp


def parse_contacts_md(contacts_path: Path):
    """Thin wrapper over the shared loader (scripts/idea.py) — one parser repo-wide.

    The audit's checks only read scalar fields, so any non-string values the
    shared parser produces (lists, nested maps) are stringified defensively.
    """
    _, contacts = _load_contacts(contacts_path)
    for c in contacts:
        for k, v in list(c.items()):
            if k in ("assumptions_tested", "interviews"):
                continue
            if not isinstance(v, str):
                c[k] = str(v)
    return contacts


def audit(slug: str):
    graph_path = REPO / "reports" / slug / "02-assumptions" / "graph.md"
    contacts_path = REPO / "reports" / slug / "outreach" / "contacts.md"

    if not graph_path.exists() or not contacts_path.exists():
        print(f"[error] missing graph.md or contacts.md for {slug}", file=sys.stderr)
        return [], [], [], []

    graph_text = graph_path.read_text()
    contacts = parse_contacts_md(contacts_path)

    all_aids = {a for c in contacts for a in c["assumptions_tested"]}
    icps = {aid: parse_assumption_icp(graph_text, aid) for aid in all_aids}
    missing_icp = [aid for aid, icp in icps.items() if not icp.get("icp_valid_tiers")]

    hard_fails = []
    tier_soft_fails = []
    rationale_soft_fails = []

    for c in contacts:
        for aid in c["assumptions_tested"]:
            icp = icps.get(aid, {})
            if not icp.get("icp_valid_tiers"):
                continue

            # Off-scope is whatever THIS assumption declares in graph.md, never a
            # hardcoded keyword list — a fixed list drifts the moment a second idea
            # uses this script. An earlier version hardcoded one vertical's terms,
            # which would have hard-failed every contact on the next idea.
            # icp_out_of_scope entries are short phrases ("Greenfield-only
            # automation providers with no completed brownfield deployments"), so
            # match on their distinctive content words rather than the whole phrase.
            primary_role = c["role"][:80].lower()
            company_lower = c["company"].lower()
            STOPWORDS = {
                "a", "an", "the", "and", "or", "with", "without", "no", "not",
                "for", "of", "in", "on", "to", "that", "who", "they", "their",
                "they're", "is", "are", "own", "separate", "unless", "also",
            }
            for pattern in icp.get("icp_out_of_scope", []):
                words = [w for w in re.findall(r"[a-z']+", pattern.lower())
                         if len(w) > 3 and w not in STOPWORDS]
                hits = sum(1 for w in words if w in primary_role or w in company_lower)
                if words and hits / len(words) >= 0.5:
                    hard_fails.append({
                        "contact": c, "aid": aid,
                        "reason": f"matches {aid}'s icp_out_of_scope: \"{pattern}\"",
                    })
                    break

            tier = c["tier"].lower()
            valid = [t.lower() for t in icp["icp_valid_tiers"]]
            if tier and tier not in valid:
                if tier == "other":
                    tier_soft_fails.append({
                        "contact": c, "aid": aid,
                        "reason": f"tier=other (assumption {aid} requires {icp['icp_valid_tiers']})",
                    })
                else:
                    hard_fails.append({
                        "contact": c, "aid": aid,
                        "reason": f"tier={tier} not in {icp['icp_valid_tiers']}",
                    })

            r = c["validation_rationale"].strip()
            if not r or r == ">" or len(r) < 20:
                rationale_soft_fails.append({
                    "contact": c, "aid": aid,
                    "reason": "validation_rationale empty or too short",
                })
            else:
                for pat in VAGUE_RATIONALE_PATTERNS:
                    if re.search(pat, r, re.IGNORECASE):
                        rationale_soft_fails.append({
                            "contact": c, "aid": aid,
                            "reason": f"vague rationale pattern: {pat}",
                        })
                        break

    return hard_fails, tier_soft_fails, rationale_soft_fails, missing_icp


def write_report(slug, hard, tier_soft, rationale_soft, missing_icp) -> Path:
    report_path = REPO / "reports" / slug / "outreach" / f"target-list-audit-{date.today().isoformat()}.md"
    lines = [
        f"# Target list audit — {slug} — {date.today().isoformat()}",
        "",
        f"Hard fails: {len(hard)} · Tier soft fails: {len(tier_soft)} · "
        f"Rationale soft fails: {len(rationale_soft)} · Assumptions missing ICP: {len(missing_icp)}",
        "",
    ]
    if missing_icp:
        lines += ["## Assumptions missing ICP declaration", ""]
        for aid in missing_icp:
            lines.append(f"- **{aid}** — fill in ICP fields in graph.md before adding contacts.")
        lines.append("")
    if hard:
        lines += ["## ❌ HARD FAILS — off-scope (must remove)", ""]
        for f in hard:
            c = f["contact"]
            lines += [
                f"### {c['name']} ({c['id']}) — for {f['aid']}",
                f"- Reason: {f['reason']}",
                f"- Role: {c['role'][:150]}",
                f"- Company: {c['company']}",
                f"- LinkedIn: {c['linkedin_url']}",
                "",
            ]
    if tier_soft:
        lines += ["## ⚠️  tier=other (needs manual classification)", ""]
        for f in tier_soft:
            c = f["contact"]
            lines.append(f"- **{c['id']}** {c['name']} — {c['role'][:100]}")
    if rationale_soft:
        lines += ["", "## ⚠️  missing/vague rationale", ""]
        for f in rationale_soft:
            c = f["contact"]
            lines.append(f"- **{c['id']}** {c['name']} — {f['reason']}")
    report_path.write_text("\n".join(lines))
    return report_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    args = parser.parse_args()

    hard, tier_soft, rationale_soft, missing_icp = audit(args.slug)

    print(f"=== Target list audit — {args.slug} ===")
    print(f"Hard fails (off-scope):        {len(hard)}")
    print(f"Tier soft fails (tier=other):  {len(tier_soft)}")
    print(f"Missing/vague rationale:       {len(rationale_soft)}")
    print(f"Assumptions missing ICP:       {len(missing_icp)}")

    report = write_report(args.slug, hard, tier_soft, rationale_soft, missing_icp)
    print(f"\nReport: {report}")


if __name__ == "__main__":
    main()
