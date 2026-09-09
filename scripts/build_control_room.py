#!/usr/bin/env python3
"""Regenerate the idea's single unified dashboard.

ONE HTML, five tabs, in pipeline order:

    Hunches  →  Pain Patterns  →  Offerings  →  Email  →  Contacts
    believe     what repeats     what we'd     sent /   who we asked
                                 sell          replied

Reads:
    input-context/belief.md                  the durable belief
    reports/01-ideation/hunch-lineage.md     hunch tree + active hunch
    reports/02-assumptions/graph.md          assumptions, status, icp_valid_tiers
    reports/03-validation/evidence.md        pain patterns + entries
    reports/04-mutation/offerings.md         offerings derived from patterns
    reports/outreach/contacts.md             contacts
    reports/outreach/email/*/email-log.csv   email delivery and reply state

Writes:
    reports/control-room.html                the artifact
    reports/outreach/results-{A_ID}.md       per-assumption outreach results

Overwrite is always safe — the HTML is a pure projection of the markdown. Nothing
is authored here, so anything wrong on the page is wrong in a source file.

Usage:
    python3 scripts/build_control_room.py

Idea-agnostic by construction: the only market vocabulary it routes on is
`tier_side` (vocab:tier_side), resolved from the idea's own `icp_valid_tiers`.
No tab hardcodes a vertical.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from html import escape, unescape
from pathlib import Path

# compute_conversion_stats lives in scripts/idea.py — the declared parsing
# authority. A second copy lived here until 2026-09-03 and had already drifted:
# only one of the two knew about channels, so the brief and the results files
# disagreed about the same contacts.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.idea import (  # noqa: E402
    BELIEF,
    CONTACTED_STATUSES,
    DEFAULT_CHANNEL,
    _channel,
    compute_conversion_stats,
    derive_assumption_evidence,
    idea_name,
)

try:
    import yaml  # PyYAML — gates graph.md, offerings.md, evidence.md AND the intel files.
                 # Without it four of the five tabs render empty; main() hard-stops instead.
    _HAS_YAML = True
except ImportError:
    _HAS_YAML = False

REPO = Path(__file__).resolve().parent.parent
REPORTS = REPO / "reports"


# ─── parsing ─────────────────────────────────────────────────────────────────


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split leading `---` YAML frontmatter from the body.

    PyYAML rather than a hand-rolled reader: the old one returned the literal
    ">" or "|" for block scalars, so a multi-line `notes:` rendered as a single
    punctuation mark, and it left surrounding quotes on quoted values.
    """
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    fm = yaml.safe_load(text[3:end]) if _HAS_YAML else {}
    return (fm if isinstance(fm, dict) else {}), text[end + 3:].lstrip("\n")


def parse_contact_block(block: str) -> dict:
    """Parse a single contact block (fields after '## Name' heading)."""
    out: dict = {"assumptions_tested": [], "interviews": []}
    lines = block.splitlines()
    if lines and lines[0].startswith("## "):
        out["name"] = lines[0][3:].strip()
    current_key = None
    block_scalar_key = None
    block_scalar_style = None
    for line in lines[1:]:
        stripped = line.strip()
        if not stripped:
            continue
        # YAML-style folded/literal block scalar continuation. Contact records use
        # these for notes, rationales and excerpts; treating only signal_excerpt
        # meant the dashboard silently discarded the other long-form fields.
        if line.startswith("  ") and block_scalar_key:
            existing = out.get(block_scalar_key, "")
            joiner = "\n" if block_scalar_style == "|" else " "
            out[block_scalar_key] = (existing + joiner + stripped).strip()
            continue
        if line.startswith("  - ") and current_key in ("interviews",):
            item = stripped.lstrip("- ").strip().strip('"')
            out.setdefault(current_key, []).append(item)
            continue
        if ":" not in stripped:
            continue
        k, _, v = stripped.partition(":")
        k = k.strip()
        v = v.strip()
        current_key = k
        block_scalar_key = k if v in (">", "|") else None
        block_scalar_style = v if block_scalar_key else None
        if v == "":
            # `key:` with nothing after it is how a block list opens (`interviews:`
            # then `  - path`), so list-typed keys must stay lists or the `  - `
            # branch above hits a str and blows up.
            out[k] = [] if k in ("interviews", "assumptions_tested") else ""
        elif v.startswith("[") and v.endswith("]"):
            inner = v[1:-1].strip()
            out[k] = [x.strip() for x in inner.split(",") if x.strip()] if inner else []
        elif v in (">", "|"):
            out[k] = ""
        else:
            # Strip a matched surrounding quote pair. Contact records quote any value that
            # could be read as something else — `degree: "1st"`, `notes: "..."` — and keeping
            # the quotes meant normalize_degree() saw '"1st"', matched nothing, and filed every
            # quoted contact as inmail_only. That silently emptied the degree tabs and hid the
            # whole 1st-degree batch from the task panel.
            if len(v) >= 2 and v[0] == v[-1] and v[0] in ("\"", "'"):
                v = v[1:-1]
            out[k] = v
    return out


def parse_contacts_md(path: Path) -> tuple[dict, list[dict]]:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)

    contacts: list[dict] = []
    blocks = re.split(r"^## ", body, flags=re.MULTILINE)
    for block in blocks[1:]:
        contact = parse_contact_block("## " + block)
        if contact.get("id"):
            contacts.append(contact)
    return frontmatter, contacts


def _parse_email_drafts(path: Path) -> dict[str, dict]:
    """Return archived draft copy keyed by E-id without treating it as sent copy."""
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    out: dict[str, dict] = {}
    for match in re.finditer(r"^## (E\d+) — .*?\n(.*?)(?=^## E\d+ — |\Z)", text, re.M | re.S):
        draft_id, block = match.group(1), match.group(2)
        subject = re.search(r"^subject:\s*(.+)$", block, re.M)
        body = re.search(r"^### Email\s*\n\n(.*?)(?=\n\n### )", block, re.M | re.S)
        fragment = re.search(r"^### Visible sent fragment\s*\n\n(.*?)(?=\n\n)", block, re.M | re.S)
        trace_rows = re.findall(r"^\|\s*([^|]+?)\s*\|\s*(https?://[^|\s]+)\s*\|", block, re.M)
        paper_note, paper_url = "", ""
        if trace_rows:
            def paper_score(item: tuple[str, str]) -> int:
                claim, url = item
                haystack = (claim + " " + url).lower()
                score = 10 if "arxiv.org" in url else 0
                score += 4 if any(k in haystack for k in ("paper", "editorial", "argument", "roboballet", "whirl", "fast", "graspgen", "robocrowd", "polaris", "dqaf", "work studies")) else 0
                score += 2 if url.lower().endswith(".pdf") else 0
                score -= 6 if any(k in claim.lower() for k in ("email", "current role", "current institutional", "current professional", "shared research correspondence", "leads", "professor", "heads")) else 0
                return score
            paper_note, paper_url = max(trace_rows, key=paper_score)
            paper_note = paper_note.strip()
        out[draft_id] = {
            "draft_subject": subject.group(1).strip() if subject else "",
            "draft_body": body.group(1).strip() if body else "",
            "visible_sent_fragment": fragment.group(1).strip() if fragment else "",
            "paper_url": paper_url,
            "paper_note": paper_note,
        }
    return out


def _parse_email_replies(path: Path) -> dict[str, dict]:
    """Parse the small human-audited reply archive keyed by target id."""
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    out: dict[str, dict] = {}
    for match in re.finditer(r"^## (T\d+) — .*?\n(.*?)(?=^## T\d+ — |\Z)", text, re.M | re.S):
        target_id, block = match.group(1), match.group(2)
        reply = re.search(r"^### Reply\s*\n\n(.*?)(?=\n\n### )", block, re.M | re.S)
        sent = re.search(r"^### Exact sent message supplied with the reply\s*\n\n(.*?)(?=\n\n### )", block, re.M | re.S)
        next_email = re.search(r"^### Proposed next email — unsent\s*\n\n(.*?)(?=\n\n### )", block, re.M | re.S)
        next_body = next_email.group(1).strip() if next_email else ""
        next_status = ""
        if next_body.startswith("draft_status:"):
            status_line, _, next_body = next_body.partition("\n")
            next_status = status_line.partition(":")[2].strip()
            next_body = next_body.strip()
        out[target_id] = {
            "reply_body": reply.group(1).strip() if reply else "",
            "exact_sent_copy": sent.group(1).strip() if sent else "",
            "next_draft_body": next_body,
            "next_draft_status": next_status,
        }
    return out


def _parse_campaign_drafts(path: Path) -> dict[str, dict]:
    """Draft copy from an email campaign's drafts.md, keyed by draft_ref.

    The campaigns author `## A1 · Name — Org · `addr`` with a `**Subject:**` line and the body
    as a blockquote. That is a different shape from the LinkedIn copy archives, which is why
    the older `_parse_email_drafts` never matched a single one of these files.
    """
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    out: dict[str, dict] = {}
    blocks = re.split(r"^## (?=[A-Z]\d)", text, flags=re.M)[1:]
    for block in blocks:
        head, _, rest = block.partition("\n")
        m = re.match(r"([A-Za-z0-9-]+)", head.strip())
        if not m:
            continue
        subject = re.search(r"^\*\*Subject:\*\*\s*(.+)$", rest, re.M)
        quoted = re.findall(r"^>\s?(.*)$", rest, re.M)
        body = "\n".join(quoted).strip()
        out[m.group(1)] = {
            "draft_subject": subject.group(1).strip() if subject else "",
            "draft_body": body,
        }
    return out


def parse_email_campaign() -> list[dict]:
    """Project durable email campaign files into dashboard-ready records.

    Driven by `targets.csv`, which the campaigns declare as their state — their own logs say
    so ("targets.csv is the state; this file is the dated history"). An earlier version drove
    off `*/email-log.csv`, a file no campaign in this repo has ever written, so the tab
    rendered empty however many targets existed.
    """
    root = REPORTS / "outreach" / "email"
    records: list[dict] = []
    if not root.exists():
        return records
    for target_path in sorted(root.glob("*/targets.csv")):
        campaign_dir = target_path.parent
        drafts = _parse_campaign_drafts(campaign_dir / "drafts.md")
        replies = _parse_email_replies(campaign_dir / "replies.md")
        with target_path.open(encoding="utf-8", newline="") as fh:
            for row in csv.DictReader(fh):
                target_id = row.get("target_id", "")
                if not target_id:
                    continue
                ref = row.get("draft_ref", "")
                draft = drafts.get(ref, {})
                if not draft and ref:
                    base = re.split(r"[-_]", ref)[0]
                    draft = drafts.get(base, {})
                reply = replies.get(target_id, {})
                sent_at = row.get("sent_on", "")
                reply_at = row.get("replied_on", "")
                status = row.get("outreach_status", "")
                state = ("replied" if reply_at or status == "replied"
                         else "sent" if sent_at or status in ("email_sent", "sent")
                         else "draft")
                records.append({
                    "campaign_id": campaign_dir.name,
                    "target_id": target_id,
                    "draft_id": row.get("draft_ref", ""),
                    "contact_id": row.get("contact_id", ""),
                    "name": row.get("name", ""),
                    "company": row.get("org", ""),
                    "role": row.get("theme", "") or row.get("degree", ""),
                    "email": row.get("email", ""),
                    "profile_url": row.get("linkedin_url", ""),
                    "paper_url": row.get("paper_url", ""),
                    "paper_note": row.get("arxiv_id", ""),
                    "draft_subject": draft.get("draft_subject", ""),
                    "sent_subject": draft.get("draft_subject", "") if sent_at else "",
                    "draft_body": draft.get("draft_body", ""),
                    "visible_sent_fragment": "",
                    "exact_sent_copy": reply.get("exact_sent_copy", ""),
                    "copy_kind": "exact_sent" if reply.get("exact_sent_copy") else "stored_draft",
                    "state": state,
                    "sent_at": sent_at,
                    "sent_account": "",
                    "reply_at": reply_at,
                    "reply_body": reply.get("reply_body", ""),
                    "next_draft_body": reply.get("next_draft_body", ""),
                    "next_draft_status": reply.get("next_draft_status", ""),
                    "followup_due": "",
                    "notes": row.get("notes", ""),
                })
    state_rank = {"replied": 0, "sent": 1, "draft": 2}
    records.sort(key=lambda r: (state_rank.get(r["state"], 9), r.get("sent_at") or "9999", r["name"]))
    return records


# ─── stats ───────────────────────────────────────────────────────────────────


def _try_int(v):
    """Coerce to int, else return None."""
    if v == "" or v is None:
        return None
    try:
        return int(v)
    except (ValueError, TypeError):
        return None


STATUS_ORDER = ["pending", "invited", "accepted", "email_drafted", "email_sent", "questions_by_email", "replied", "scheduled", "done", "no_reply", "declined", "held", "off_scope"]
ROLE_ORDER = ["buyer", "practitioner", "expert", "influencer"]
SIGNAL_ORDER = ["post_engagement", "comment_signal", "job_posting", "profile_fit"]

# Tiers are idea-defined (declared per assumption), so the dashboard derives the
# tier list from the data and assigns colors from a palette by position — nothing
# tier-specific is hardcoded.
TIER_PALETTE = ["#22d3ee", "#f472b6", "#fbbf24", "#a78bfa", "#34d399",
                "#94a3b8", "#f59e0b", "#60a5fa", "#c084fc", "#4ade80"]


def derive_tiers(contacts: list[dict]) -> list[str]:
    """Distinct tier names present, ordered by frequency desc then name."""
    counts = Counter((c.get("tier") or "other") for c in contacts)
    return [t for t, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))]


def _hex_to_rgba(hex_color: str, alpha: float) -> str:
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"


def tier_css(tiers: list[str]) -> str:
    """Generate `.tier-{name}` badge rules for whatever tiers the data contains."""
    rules = []
    for i, t in enumerate(tiers):
        c = TIER_PALETTE[i % len(TIER_PALETTE)]
        rules.append(f".tier-{t} {{background:{_hex_to_rgba(c, 0.12)};color:{c};}}")
    return "\n".join(rules)


def compute_stats(contacts: list[dict]) -> dict:
    stats = {
        "total": len(contacts),
        "by_status": {s: 0 for s in STATUS_ORDER},
        "by_tier": {t: 0 for t in derive_tiers(contacts)},
        "by_role": {r: 0 for r in ROLE_ORDER},
        "by_signal": {s: 0 for s in SIGNAL_ORDER},
        "by_assumption": Counter(),
    }
    for c in contacts:
        stats["by_status"][c.get("outreach_status") or "pending"] = (
            stats["by_status"].get(c.get("outreach_status") or "pending", 0) + 1
        )
        stats["by_tier"][c.get("tier") or "other"] = (
            stats["by_tier"].get(c.get("tier") or "other", 0) + 1
        )
        stats["by_role"][c.get("contact_role") or "practitioner"] = (
            stats["by_role"].get(c.get("contact_role") or "practitioner", 0) + 1
        )
        stats["by_signal"][c.get("signal_type") or "profile_fit"] = (
            stats["by_signal"].get(c.get("signal_type") or "profile_fit", 0) + 1
        )
        for a in c.get("assumptions_tested", []):
            stats["by_assumption"][a] += 1
    stats["by_assumption"] = dict(stats["by_assumption"])
    return stats


# CONTACTED_STATUSES and the rest of the funnel vocabulary live in scripts/idea.py,
# imported at the top of this file. A second copy lived here and was already one
# `accepted` out of step with the authority it duplicated.


# ─── helpers ─────────────────────────────────────────────────────────────────


def parse_bool(v) -> bool:
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        return v.strip().lower() in ("true", "1", "yes")
    return False


def normalize_degree(d: str) -> str:
    d = (d or "").strip().lower()
    if d == "1st":
        return "1st"
    if d == "2nd":
        return "2nd"
    if d.startswith("3rd") or d.startswith("3+"):
        return "3rd+"
    return "inmail_only"


def count_by_degree(contacts: list[dict]) -> dict:
    counts = {"1st": 0, "2nd": 0, "3rd+": 0, "inmail_only": 0}
    for c in contacts:
        counts[normalize_degree(c.get("degree", ""))] += 1
    return counts


# ─── HTML rendering ──────────────────────────────────────────────────────────


STATUS_COLORS = {
    "pending": "#94a3b8",
    "held": "#9ca3af",
    "invited": "#60a5fa",
    "accepted": "#a78bfa",
    "email_drafted": "#94a3b8",
    "email_sent": "#60a5fa",
    "questions_by_email": "#22c55e",
    "replied": "#10b981",
    "scheduled": "#f59e0b",
    "done": "#22c55e",
    "no_reply": "#64748b",
    "declined": "#ef4444",
    "off_scope": "#78716c",
}


def _load_copy_by_contact() -> dict[str, dict]:
    """
    Parse every outreach copy file into { contact_id → { msg1, msg2, msg3, header, lang } }.

    Handles two header formats:
      ## C{ID} — Name [flags]           (warm-thread or single-contact blocks)
      ## #{N} — C{ID} Name [flags]      (cold-queue with send-order prefix)

    Skips [REMOVED ...] blocks. Handles ~ prefix in char counts.
    """
    copy_dir = REPORTS / "outreach" / "copy"
    if not copy_dir.exists():
        return {}
    # Glob widened 2026-08-10: was "*-linkedin.md", which silently skipped
    # SEND-QUEUE.md and left every draft in it invisible on the page.
    paths = sorted(copy_dir.glob("*.md"))

    # Contact headers appear at ## (A2-era) or ### (batch-grouped files, where ##
    # is the batch). Requiring a C-number is what separates a contact header from
    # a "## Batch 2 — ..." section header. Optional "#3 —" prefix is send order.
    HEADER_RE = re.compile(
        r"(?m)^(#{2,3})\s+(?:#(\d+)\s*[—\-]+\s*)?(C\d+)\b[\s—\-–·]*(.*)$"
    )
    ANY_HEADING_RE = re.compile(r"(?m)^(#{1,6})\s")

    by_id: dict[str, dict] = {}
    for p in paths:
        text = p.read_text(encoding="utf-8")
        headings = [(m.start(), len(m.group(1))) for m in ANY_HEADING_RE.finditer(text)]
        contact_starts = {m.start() for m in HEADER_RE.finditer(text)}
        for m in HEADER_RE.finditer(text):
            level = len(m.group(1))
            send_order_raw = m.group(2)
            cid = m.group(3)
            header = m.group(4).strip()

            # Skip REMOVED placeholder slots
            if header.upper().startswith("[REMOVED"):
                continue

            # The block ends at the next heading that is a sibling-or-shallower
            # section, or at the next contact. Deeper headings ("### Msg 2" under
            # a "## C1" contact) are part of THIS contact's block — treating them
            # as boundaries truncates the block before its messages.
            body_end = next(
                (pos for pos, lvl in headings
                 if pos > m.end() and (lvl <= level or pos in contact_starts)),
                len(text),
            )
            body = text[m.end():body_end]
            by_id[cid] = {
                "header": header,
                "language": "TR" if (" · TR]" in header or " TR]" in header) else "EN",
                "send_order": int(send_order_raw) if send_order_raw else None,
                "is_warm": "REPLIED" in header or "← replied" in header.lower(),
                "messages": _extract_messages(body),
                "source_file": str(p.relative_to(REPORTS.parent)),
            }
    return by_id


def _extract_messages(body: str) -> list[dict]:
    """Pull sendable message bodies out of one contact's block.

    Three archive conventions are in use and all three are read here:

      * fenced code block under a `### Message N` heading, with a following
        `Char count: ~625 / 400` line (the July archives);
      * blockquote under a `### Msg N` heading or a `**Primary (439 chars):**`
        bold label (from 2026-07-28);
      * bare blockquote under a `### C9 — Name @ Co` heading, followed by a
        `225 chars · direct_question` line (the batch-grouped files).

    A contact often has alternates — a short version, a second language, a
    fallback connection note — so every quoted or fenced run is a candidate and
    the nearest preceding heading or bold label names it. Surrounding prose
    (retrospectives, traceability tables, rule-compliance notes) is neither
    quoted nor fenced, which is what keeps it out of the modal.
    """
    LABEL_RE = re.compile(r"^#{3,6}\s+(.*)$")
    BOLD_LABEL_RE = re.compile(r"^\*\*(.+?)\*\*\s*:?\s*$")
    CHARS_RE = re.compile(r"(\d{2,4})\s*chars\b")
    CHAR_COUNT_RE = re.compile(r"Char count:\s*~?(\d+)")
    # Archives also quote what the CONTACT said back. That is evidence, not copy
    # to send, and putting it in a send-this modal is how a founder pastes
    # someone's own words back at them. Match only the possessive form
    # ("Juan's reply:", "Their last reply:") — outbound drafts legitimately say
    # "send after they reply" and must not be caught by this.
    INBOUND_RE = re.compile(
        r"(\b\w+'s|\btheir\b|\bhis\b|\bher\b)\s+(?:last\s+|first\s+)?(?:reply|response)\b",
        re.I,
    )

    messages: list[dict] = []
    label = ""
    buf: list[str] = []
    in_fence = False

    def flush(joiner: str = " ") -> None:
        if not buf:
            return
        text = joiner.join(buf).strip()
        buf.clear()
        if len(text) < 40:          # table cells and one-line asides, not messages
            return
        if INBOUND_RE.search(label):
            return
        chars = CHARS_RE.search(label)
        messages.append({
            "label": re.sub(r"\s*\(\d+\s*chars\)", "", label).strip() or f"Message {len(messages) + 1}",
            "body": text,
            "chars": f"{chars.group(1)} chars" if chars else f"{len(text)} chars",
        })

    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            if in_fence:
                flush("\n")         # fenced copy keeps its paragraph breaks
            in_fence = not in_fence
            continue
        if in_fence:
            buf.append(line.rstrip())
            continue
        if stripped.startswith(">"):
            buf.append(stripped.lstrip("> ").rstrip())
            continue
        flush()
        if not stripped:
            continue
        m = LABEL_RE.match(stripped) or BOLD_LABEL_RE.match(stripped)
        if m:
            label = m.group(1).strip()
        elif messages:
            # a trailing "225 chars · direct_question" or "Char count: ~625 / 400"
            # line reports on the message just above it
            cc = CHAR_COUNT_RE.search(stripped) or (
                CHARS_RE.search(stripped) if len(stripped) < 60 else None
            )
            if cc:
                messages[-1]["chars"] = cc.group(1) + " chars"
    flush()
    return messages


def build_invite_log(contacts: list[dict]) -> tuple[str, str]:
    """Invite ledger grouped by invited_date, plus pacing against LinkedIn's limits.

    Added 2026-08-06 at founder request. Two jobs: an auditable record of which
    invites went out on which day and by whom, and a pacing guard. The binding
    LinkedIn constraint is roughly 100 invites/week (not a daily cap), and a
    large pile of unaccepted invites depresses deliverability on new ones, so
    outstanding-pending is surfaced next to the weekly count.
    """
    from datetime import date, datetime, timedelta

    WEEK_CAP = 100
    by_day: dict[str, list[dict]] = {}
    for c in contacts:
        d = (c.get("invited_date") or "").strip()
        if d:
            by_day.setdefault(d, []).append(c)
    if not by_day:
        return "", ""

    today = date.today()
    week_ago = today - timedelta(days=7)
    week_count = 0
    for d, rows in by_day.items():
        try:
            if datetime.strptime(d, "%Y-%m-%d").date() >= week_ago:
                week_count += len(rows)
        except ValueError:
            pass

    outstanding = sum(
        1 for c in contacts if (c.get("outreach_status") or "") == "invited"
    )
    pct = min(100, round(week_count / WEEK_CAP * 100))
    bar_class = "ok" if pct < 60 else ("warn" if pct < 85 else "danger")

    rows_html = []
    for d in sorted(by_day, reverse=True):
        people = by_day[d]
        chips = "".join(
            f'<span class="invite-chip">{escape(c.get("name") or c.get("id") or "?")}'
            f'<em>{escape((c.get("company") or "")[:28])}</em></span>'
            for c in sorted(people, key=lambda x: x.get("name") or "")
        )
        rows_html.append(
            f'<div class="invite-day">'
            f'<div class="invite-day-head"><span class="invite-date">{escape(d)}</span>'
            f'<span class="invite-count">{len(people)}</span></div>'
            f'<div class="invite-chips">{chips}</div></div>'
        )

    html = (
        '<section class="invite-log" aria-label="Invite log">'
        '<div class="invite-log-head">'
        '<div class="invite-log-title">Invite log '
        f'<span class="invite-total">{sum(len(v) for v in by_day.values())}</span></div>'
        f'<div class="invite-pacing">'
        f'<span class="pace-num">{week_count}</span>'
        f'<span class="pace-label">sent in last 7 days &middot; cap ~{WEEK_CAP}/wk</span>'
        f'<div class="pace-bar"><i class="{bar_class}" style="width:{pct}%"></i></div>'
        f'<span class="pace-sub">{outstanding} still awaiting acceptance</span>'
        '</div></div>'
        + "".join(rows_html)
        + "</section>"
    )

    css = """
/* ── invite log ── */
/* Panel treatment mirrors .summary-strip: this sits between two carded blocks,
   and without a surface of its own it reads as loose text on the page ground. */
.invite-log {
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:var(--r-lg);
  padding:18px 22px;
  margin:0 0 16px;
}
/* flex-start, not flex-end: the pacing block is three lines tall, so end-alignment
   pushed the section title to the card's midpoint and orphaned it there. */
.invite-log-head {display:flex;justify-content:space-between;align-items:flex-start;gap:18px;flex-wrap:wrap;margin-bottom:4px;}
/* Was .intel-section-title / .count — both orphaned when the company-intel
   section was removed, so the heading rendered as unstyled body text. */
.invite-log-title {
  font-size:10px;text-transform:uppercase;letter-spacing:0.1em;
  color:var(--text-dimmer);font-weight:600;
  display:flex;align-items:center;gap:7px;
}
.invite-total {
  font-size:10px;font-weight:700;padding:1px 7px;border-radius:9px;
  letter-spacing:0;background:var(--surface-3);color:var(--text-dim);
}
.invite-pacing {min-width:230px;}
.pace-num {font-size:20px;font-weight:700;margin-right:6px;}
.pace-label {font-size:11px;color:var(--text-dim);}
.pace-bar {height:5px;border-radius:3px;background:rgba(127,127,127,.18);margin:5px 0 3px;overflow:hidden;}
.pace-bar i {display:block;height:100%;border-radius:3px;}
.pace-bar i.ok {background:#059669;}
.pace-bar i.warn {background:#d97706;}
.pace-bar i.danger {background:#dc2626;}
.pace-sub {font-size:10.5px;color:var(--text-dim);}
.invite-day {padding:8px 0;border-top:1px solid rgba(127,127,127,.14);}
.invite-day-head {display:flex;align-items:center;gap:8px;margin-bottom:5px;}
.invite-date {font-size:12px;font-weight:600;}
.invite-count {font-size:10px;font-weight:700;padding:1px 7px;border-radius:9px;
  background:rgba(37,99,235,.12);color:#2563eb;}
.invite-chips {display:flex;flex-wrap:wrap;gap:5px;}
.invite-chip {font-size:11px;padding:2px 8px;border-radius:10px;
  background:rgba(127,127,127,.10);white-space:nowrap;}
.invite-chip em {font-style:normal;color:var(--text-dim);margin-left:5px;font-size:10px;}
"""
    return html, css


def render(
    frontmatter: dict,
    contacts: list[dict],
    copy_by_id: dict[str, dict] | None = None,
    patterns: list[dict] | None = None,
    evidence_entries: list[dict] | None = None,
    thesis: dict | None = None,
    companies: tuple[dict, list[dict]] | None = None,
) -> str:
    thesis = thesis or {}
    copy_by_id = copy_by_id or {}
    stats = compute_stats(contacts)
    conversion = compute_conversion_stats(contacts)
    tier_css_block = tier_css(list(stats["by_tier"].keys()))
    invite_log_html, invite_log_css = build_invite_log(contacts)
    tier_css_block = (tier_css_block + invite_log_css + EMAIL_CSS + TAB_CSS
                      + PATTERNS_CSS + THESIS_CSS + HUNCH_CSS + COMPANIES_CSS
                      + PAGES_CSS)

    companies_fm, companies_list = companies or ({}, [])
    companies_tab_html = render_companies_tab(companies_list, companies_fm, contacts)
    companies_count = len(companies_list)

    # Supply side on its own page — split from the company space map 2026-08-27.
    startups_tab_html = render_startups_tab(companies_fm, companies_list, contacts)
    startups_count = sum(1 for c in companies_list if _map_side(c) == "startup")

    email_campaign = parse_email_campaign()
    email_tab_html = render_email_tab(email_campaign)
    email_campaign_json = json.dumps(email_campaign, indent=2, ensure_ascii=False)
    email_count = len(email_campaign)
    email_script = _render_email_script()

    # pain-pattern tab — cross-contact layer derived from evidence.md
    sides_by_tier = tier_side_map(thesis.get("assumptions") or [])
    scored_patterns, untagged_ev = compute_pattern_stats(
        patterns or [], evidence_entries or [], contacts, sides_by_tier)
    patterns_tab_html = render_patterns_tab(
        scored_patterns, untagged_ev, len(evidence_entries or []))
    patterns_count = len(scored_patterns)

    # thesis + offerings tabs
    thesis_tab_html = render_thesis_tab(
        thesis.get("lineage_fm") or {}, thesis.get("hunches") or [],
        thesis.get("graph_fm") or {}, thesis.get("assumptions") or [],
        thesis.get("belief") or "", evidence_entries or [],
        belief_sections=thesis.get("belief_sections") or [],
        artifacts=thesis.get("artifacts") or [])
    offerings = thesis.get("offerings") or []
    offerings_tab_html = render_offerings_tab(
        offerings, scored_patterns, thesis.get("offerings_fm") or {})
    offerings_count = len(offerings)
    pages_tab_html = render_pages_tab()
    pages_count = len(list((REPORTS / "pages").glob("*.html")))
    # scalar or list — see build_brief.py, an idea may run one hunch per entry point
    _ah = (thesis.get("lineage_fm") or {}).get("active_hunch")
    _ah_list = [str(h).strip() for h in (_ah if isinstance(_ah, list) else [_ah]) if h]
    active_hunch = "+".join(_ah_list) or "?"
    deg_counts = count_by_degree(contacts)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    tab_scripts = _render_tab_scripts()

    # Top 3 contacts by response_likelihood for the priority callout
    scored = sorted(
        [c for c in contacts if _try_int(c.get("response_likelihood")) is not None],
        key=lambda c: _try_int(c.get("response_likelihood")) or 0,
        reverse=True,
    )[:3]


    def _priority_card(c: dict) -> str:
        score = _try_int(c.get("response_likelihood"))
        sclass = "score-green" if (score or 0) >= 8 else ("score-yellow" if (score or 0) >= 5 else "score-red")
        deg = normalize_degree(c.get("degree", ""))
        dc = {"1st": "deg-1st", "2nd": "deg-2nd", "3rd+": "deg-3rdplus", "inmail_only": "deg-inmail"}.get(deg, "deg-inmail")
        dl = {"1st": "1st", "2nd": "2nd", "3rd+": "3rd+", "inmail_only": "IM"}.get(deg, "?")
        name = escape(c.get("name") or "—")
        url = c.get("linkedin_url") or ""
        nh = f'<a href="{escape(url)}" target="_blank" rel="noopener">{name}</a>' if url else name
        role = escape((c.get("role") or "")[:62])
        score_str = str(score) if score is not None else "—"
        tier_key = c.get("tier") or "other"
        tl = escape(tier_key.replace("_", " "))
        return (
            f'<div class="priority-card">'
            f'<div class="priority-ring {sclass}">{score_str}</div>'
            f'<div class="priority-body">'
            f'<div class="priority-name">{nh}</div>'
            f'<div class="priority-role">{role}</div>'
            f'</div>'
            f'<div class="priority-badges">'
            f'<span class="deg-badge {dc}">{escape(dl)}</span>'
            f'<span class="tier-badge tier-{escape(tier_key)}">{tl}</span>'
            f'</div>'
            f'</div>'
        )

    priority_html = "".join(_priority_card(c) for c in scored)

    contacts_json = json.dumps(
        [
            {
                "id": c.get("id", ""),
                "name": c.get("name", ""),
                "linkedin_url": c.get("linkedin_url", ""),
                "company": c.get("company", ""),
                "role": c.get("role", ""),
                "tier": c.get("tier", "other"),
                "relationship_type": c.get("relationship_type", ""),
                "contact_role": c.get("contact_role", "practitioner"),
                "signal_type": c.get("signal_type", "profile_fit"),
                "signal_excerpt": c.get("signal_excerpt", ""),
                "degree": normalize_degree(c.get("degree", "")),
                "open_to_work": parse_bool(c.get("open_to_work", "")),
                "active_last_30d": parse_bool(c.get("active_last_30d", "")),
                "mutuals_count": _try_int(c.get("mutuals_count", "")) or 0,
                "assumptions_tested": c.get("assumptions_tested", []),
                "outreach_status": c.get("outreach_status", "pending"),
                "message_stage": c.get("message_stage", ""),
                "call_stage": c.get("call_stage", ""),
                # The task panel is a LINKEDIN worklist. Without this it listed the five
                # shops the founder phoned as "reply waiting" — conversations that already
                # happened and already produced E7-E11 and E15-E17. compute_conversion_stats
                # was channel-scoped on 2026-09-03 and this panel was not; same bug, later.
                "channel": _channel(c),
                "reply_type": c.get("reply_type", ""),
                "response_likelihood": _try_int(c.get("response_likelihood", "")),
                "likelihood_factors": c.get("likelihood_factors", ""),
                "outreach_pattern": c.get("outreach_pattern", ""),
                "validation_rationale": c.get("validation_rationale", ""),
                "notes": c.get("notes", ""),
                "found_date": c.get("found_date", ""),
            }
            for c in contacts
        ],
        indent=2,
    )

    copy_by_id_json = json.dumps(copy_by_id or {}, indent=2, ensure_ascii=False)

    # YAML coerces bare ISO dates to datetime.date, so frontmatter values are
    # str()-ed before escaping — escape() on a date hits date.replace() instead.
    idea_title = escape(
        str(frontmatter.get("campaign_name") or frontmatter.get("idea") or idea_name())
    )
    last_updated = escape(str(frontmatter.get("last_updated") or "—"))
    total = stats["total"]
    d1 = deg_counts["1st"]
    d2 = deg_counts["2nd"]
    d3 = deg_counts["3rd+"]
    dim = deg_counts["inmail_only"]
    pending_count = stats["by_status"].get("pending", 0)
    accepted_count = stats["by_status"].get("accepted", 0)
    done_count = stats["by_status"].get("done", 0)
    contacted_count = conversion["contacted"]
    replied_count = conversion["replied"]
    qualified_replied_count = conversion["qualified_replied"]
    call_progressed_count = conversion["call_progressed"]
    scheduled_count = conversion["scheduled"]
    outreach_started_count = conversion["outreach_started"]
    target_to_contact_rate = conversion["target_to_contact_rate"] or 0
    reply_rate = conversion["reply_rate"] or 0
    reply_to_call_rate = conversion["reply_to_call_rate"] or 0
    reply_to_scheduled_rate = conversion["reply_to_scheduled_rate"] or 0
    rates_confirmed_through = escape(str(frontmatter.get("rates_confirmed_through") or last_updated))
    inbox_check_status = str(frontmatter.get("inbox_check_status") or "not recorded")
    inbox_fresh = "not_run" not in inbox_check_status
    freshness_label = "Inbox checked" if inbox_fresh else "Inbox not rechecked"
    freshness_class = "fresh" if inbox_fresh else "stale"

    assumption_conversion_html = "".join(
        f'''<div class="conversion-card assumption-rate">
          <span class="conversion-eyebrow">{escape(aid)} reply rate</span>
          <strong class="conversion-rate">{row["reply_rate"] if row["reply_rate"] is not None else 0:g}%</strong>
          <span class="conversion-detail">{row["replied"]} replies ({row["qualified_replied"]} qualified) / {row["contacted"]} messaged</span>
        </div>'''
        for aid, row in conversion["by_assumption"].items()
    )

    return f"""<!doctype html>
<!-- GENERATED by scripts/build_control_room.py — DO NOT EDIT.
     Every value here is derived from reports/. Fix the source file, then:
       python3 scripts/build_control_room.py
     A hand-edit is overwritten on the next run and drifts from its source until then. -->
<html lang="en">
<head>
<meta charset="utf-8">
<title>Control room — {idea_title}</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
:root {{
  --bg: #0b0d10;
  --surface: #14171c;
  --surface-2: #1c2027;
  --surface-3: #22272f;
  --border: #262b34;
  --border-subtle: #1e2229;
  --text: #e6e9ee;
  --text-dim: #8b93a0;
  --text-dimmer: #545c6b;
  --accent: #f5ce4a;
  --deg-1st: #f5ce4a;
  --deg-2nd: #60a5fa;
  --deg-3rd: #94a3b8;
  --deg-im: #a78bfa;
  --green: #22c55e;
  --yellow: #f59e0b;
  --red: #ef4444;
  --r-sm: 6px;
  --r-md: 10px;
  --r-lg: 14px;
}}
*,*::before,*::after {{box-sizing:border-box;margin:0;padding:0;}}
a {{color:inherit;text-decoration:none;}}
body {{
  background:var(--bg);
  color:var(--text);
  font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text","Helvetica Neue",system-ui,sans-serif;
  font-size:14px;
  line-height:1.5;
  -webkit-font-smoothing:antialiased;
}}
body::before {{
  content:"";
  display:block;
  position:fixed;
  top:0;left:0;right:0;
  height:2px;
  background:linear-gradient(90deg,var(--accent) 0%,transparent 65%);
  z-index:999;
}}

/* ── card with copy ready ── */
.card.has-copy {{
  border-color:rgba(245,206,74,0.28);
}}
.card.has-copy:hover {{
  border-color:rgba(245,206,74,0.5);
}}

/* ── relationship and call-stage badges ── */
.relationship-badge,.call-badge {{
  display:inline-block;padding:2px 7px;border-radius:999px;
  font-size:10px;font-weight:700;letter-spacing:.03em;text-transform:uppercase;
}}
.relationship-badge {{background:rgba(168,85,247,.11);color:#c084fc;border:1px solid rgba(168,85,247,.22);}}
.relationship-competitor {{background:rgba(244,63,94,.10);color:#fb7185;border-color:rgba(244,63,94,.24);}}
.call-badge {{background:rgba(6,182,212,.10);color:#22d3ee;border:1px solid rgba(6,182,212,.22);}}

/* ── send-order badge (#1, #2…) ── */
.send-order-badge {{
  display:inline-flex;align-items:center;justify-content:center;
  min-width:22px;height:22px;border-radius:11px;
  padding:0 6px;
  background:var(--accent);color:#0b0d10;
  font-size:10px;font-weight:800;letter-spacing:0;
  flex-shrink:0;
}}

/* ── outreach copy trigger strip on card ── */
.card-copy-trigger {{
  margin-top:10px;
  border-top:1px dashed var(--border);
  padding-top:10px;
  display:flex;align-items:center;gap:8px;
  cursor:pointer;
  user-select:none;
}}
.card-copy-trigger:hover .copy-summary-label {{color:var(--text);}}
.copy-summary-label {{
  font-size:11px;font-weight:600;letter-spacing:0.03em;
  color:var(--text-dim);
}}
.copy-lang {{
  background:var(--surface-3);
  color:var(--text-dim);
  font-size:9px;font-weight:600;
  padding:1px 6px;border-radius:99px;
  letter-spacing:0.06em;
}}
.copy-trigger-arrow {{
  font-size:10px;color:var(--text-dimmer);
  margin-left:auto;
}}
.card-copy-empty {{
  margin-top:10px;
  padding:8px 10px;
  background:var(--surface-2);
  border:1px dashed var(--border-subtle);
  border-radius:6px;
  font-size:10px;color:var(--text-dimmer);
  line-height:1.4;
}}
.card-copy-empty code {{
  background:var(--surface);
  padding:1px 5px;border-radius:3px;
  font-family:"SF Mono","Cascadia Code",monospace;
  color:var(--accent);
  font-size:10px;
}}

/* ── copy modal ── */
.modal-backdrop {{
  display:none;
  position:fixed;inset:0;
  background:rgba(0,0,0,0.65);
  backdrop-filter:blur(3px);
  -webkit-backdrop-filter:blur(3px);
  z-index:9999;
  align-items:center;justify-content:center;
  padding:24px;
}}
.modal-backdrop.open {{display:flex;}}
.modal-box {{
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:var(--r-lg);
  width:100%;max-width:620px;
  max-height:90vh;
  display:flex;flex-direction:column;
  box-shadow:0 32px 64px rgba(0,0,0,0.55);
}}
.modal-header {{
  display:flex;align-items:center;gap:10px;
  padding:16px 20px 14px;
  border-bottom:1px solid var(--border);
  flex-shrink:0;
}}
.modal-title {{
  font-size:14px;font-weight:600;letter-spacing:-0.01em;
  flex:1;min-width:0;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
}}
.modal-close {{
  background:transparent;border:none;
  color:var(--text-dimmer);font-size:18px;
  cursor:pointer;padding:2px 6px;border-radius:4px;
  line-height:1;transition:color 0.12s,background 0.12s;
  flex-shrink:0;
}}
.modal-close:hover {{color:var(--text);background:var(--surface-2);}}
.modal-body {{
  overflow-y:auto;padding:18px 20px 22px;
  display:flex;flex-direction:column;gap:14px;
}}
.warm-badge {{
  display:inline-flex;align-items:center;gap:4px;
  padding:2px 8px;border-radius:99px;
  font-size:10px;font-weight:600;
  background:rgba(249,115,22,0.14);
  color:#f97316;border:1px solid rgba(249,115,22,0.3);
  flex-shrink:0;
}}
.copy-msg {{
  background:var(--surface-2);
  border-left:2px solid var(--accent);
  border-radius:0 6px 6px 0;
  padding:10px 14px;
}}
.copy-msg-head {{
  display:flex;align-items:center;gap:10px;
  font-size:10px;color:var(--text-dim);
  text-transform:uppercase;letter-spacing:0.06em;
  margin-bottom:8px;
}}
.copy-msg-num {{font-weight:700;color:var(--accent);}}
.copy-msg-label {{color:var(--text-dim);}}
.copy-msg-count {{
  margin-left:auto;font-size:10px;
  color:var(--text-dimmer);
  font-family:"SF Mono","Cascadia Code",monospace;
  text-transform:none;letter-spacing:0;
}}
.copy-btn {{
  background:transparent;
  border:1px solid var(--border);
  color:var(--text-dim);
  font-size:10px;
  padding:2px 8px;border-radius:4px;
  cursor:pointer;
  transition:all 0.15s;
  font:inherit;font-size:10px;font-weight:600;
  text-transform:uppercase;letter-spacing:0.05em;
}}
.copy-btn:hover {{color:var(--accent);border-color:var(--accent);}}
.copy-btn.copied {{color:var(--green);border-color:var(--green);}}
.copy-body {{
  font-family: Georgia,"Iowan Old Style",serif;
  font-size:12.5px;
  line-height:1.55;
  color:var(--text);
  white-space:pre-wrap;
  margin:0;
  padding:2px 0 4px;
}}

/* ── page shell ── */
.page {{max-width:1280px;margin:0 auto;padding:36px 24px 80px;}}

/* ── page header ── */
.page-header {{margin-bottom:22px;}}
.page-header h1 {{font-size:21px;font-weight:700;letter-spacing:-0.03em;margin-bottom:3px;}}
.page-header h1 .idea-name {{color:var(--accent);}}
.page-header .subtitle {{font-size:12px;color:var(--text-dim);}}

/* ── summary strip ── */
.summary-strip {{
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:var(--r-lg);
  padding:18px 22px;
  margin-bottom:16px;
  display:flex;
  flex-direction:column;
  gap:14px;
}}
.kpi-row {{display:flex;flex-wrap:wrap;gap:6px;align-items:center;}}
.kpi-sep {{width:1px;height:20px;background:var(--border);margin:0 3px;flex-shrink:0;}}
.kpi-item {{
  display:flex;align-items:center;gap:7px;
  padding:5px 11px;
  background:var(--surface-2);
  border:1px solid var(--border);
  border-radius:var(--r-md);
  white-space:nowrap;
}}
.kpi-value {{font-size:16px;font-weight:700;letter-spacing:-0.02em;line-height:1;}}
.kpi-label {{font-size:10px;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-dim);}}
.kpi-dot {{width:7px;height:7px;border-radius:50%;flex-shrink:0;}}

/* ── campaign conversion ── */
.conversion-section {{border-top:1px solid var(--border-subtle);padding-top:14px;}}
.conversion-header {{display:flex;justify-content:space-between;gap:12px;align-items:center;margin-bottom:10px;}}
.conversion-title {{font-size:10px;text-transform:uppercase;letter-spacing:0.1em;color:var(--text-dimmer);font-weight:700;}}
.freshness-badge {{font-size:10px;padding:3px 8px;border-radius:99px;border:1px solid;}}
.freshness-badge.fresh {{color:var(--green);border-color:rgba(34,197,94,.35);background:rgba(34,197,94,.08);}}
.freshness-badge.stale {{color:var(--yellow);border-color:rgba(245,158,11,.35);background:rgba(245,158,11,.08);}}
.conversion-grid {{display:grid;grid-template-columns:repeat(5,minmax(150px,1fr));gap:9px;}}
.conversion-card {{display:flex;flex-direction:column;gap:4px;padding:13px 14px;background:var(--surface-2);border:1px solid var(--border);border-radius:var(--r-md);}}
.conversion-card.primary {{border-color:rgba(34,197,94,.35);background:linear-gradient(145deg,rgba(34,197,94,.08),var(--surface-2) 55%);}}
.conversion-card.assumption-rate {{border-color:rgba(96,165,250,.25);}}
.conversion-eyebrow {{font-size:9px;text-transform:uppercase;letter-spacing:.09em;color:var(--text-dim);font-weight:700;}}
.conversion-rate {{font-size:25px;line-height:1;font-weight:800;letter-spacing:-.04em;}}
.conversion-detail {{font-size:10px;color:var(--text-dimmer);line-height:1.4;}}

/* ── priority callout ── */
.priority-section {{border-top:1px solid var(--border-subtle);padding-top:12px;}}
.priority-label {{
  font-size:10px;text-transform:uppercase;letter-spacing:0.1em;
  color:var(--text-dimmer);font-weight:600;margin-bottom:8px;
}}
.priority-cards {{display:flex;gap:10px;flex-wrap:wrap;}}
.priority-card {{
  display:flex;align-items:center;gap:10px;
  background:var(--surface-2);
  border:1px solid var(--border);
  border-radius:var(--r-md);
  padding:10px 14px;
  flex:1;min-width:195px;max-width:380px;
}}
.priority-body {{flex:1;min-width:0;}}
.priority-name {{
  font-size:13px;font-weight:600;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
}}
.priority-name a:hover {{color:var(--accent);text-decoration:underline;}}
.priority-role {{
  font-size:11px;color:var(--text-dim);
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
}}
.priority-badges {{display:flex;flex-direction:column;gap:4px;align-items:flex-end;flex-shrink:0;}}

/* ── score rings (shared by cards + priority) ── */
.card-score,.priority-ring {{
  width:38px;height:38px;border-radius:50%;border:2px solid;
  display:flex;align-items:center;justify-content:center;
  font-size:13px;font-weight:700;flex-shrink:0;
}}
.score-green {{border-color:var(--green);color:var(--green);background:rgba(34,197,94,0.08);}}
.score-yellow {{border-color:var(--yellow);color:var(--yellow);background:rgba(245,158,11,0.08);}}
.score-red {{border-color:var(--red);color:var(--red);background:rgba(239,68,68,0.08);}}
.score-dim {{border-color:var(--border);color:var(--text-dimmer);background:transparent;}}

/* ── degree badges ── */
.deg-badge {{
  display:inline-flex;align-items:center;
  padding:2px 7px;border-radius:999px;
  font-size:10px;font-weight:700;letter-spacing:0.04em;
  border:1px solid;flex-shrink:0;
}}
.deg-1st {{color:var(--deg-1st);border-color:rgba(245,206,74,0.4);background:rgba(245,206,74,0.1);}}
.deg-2nd {{color:var(--deg-2nd);border-color:rgba(96,165,250,0.4);background:rgba(96,165,250,0.1);}}
.deg-3rdplus {{color:var(--deg-3rd);border-color:rgba(148,163,184,0.3);background:rgba(148,163,184,0.08);}}
.deg-inmail {{color:var(--deg-im);border-color:rgba(167,139,250,0.35);background:rgba(167,139,250,0.1);}}

/* ── tier badges ── */
.tier-badge {{
  display:inline-block;padding:2px 7px;border-radius:999px;
  font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.05em;
}}
{tier_css_block}
.tier-other {{background:rgba(107,114,128,0.1);color:#9ca3af;}}

/* ── signal badges ── */
.signal-badge {{
  display:inline-flex;align-items:center;
  padding:3px 8px;border-radius:var(--r-sm);
  font-size:11px;font-weight:500;
  border:1px solid var(--border);color:var(--text-dim);background:var(--surface-2);
}}
.signal-post_engagement {{color:#f97316;border-color:rgba(249,115,22,0.3);background:rgba(249,115,22,0.07);}}
.signal-comment_signal {{color:#fb923c;border-color:rgba(251,146,60,0.3);background:rgba(251,146,60,0.07);}}
.signal-job_posting {{color:#38bdf8;border-color:rgba(56,189,248,0.3);background:rgba(56,189,248,0.07);}}

/* ── small pill badges ── */
.pill-sm {{
  display:inline-flex;align-items:center;
  padding:2px 8px;border-radius:999px;
  font-size:10px;font-weight:600;letter-spacing:0.03em;
}}
.pill-otw {{background:rgba(34,197,94,0.12);color:#4ade80;border:1px solid rgba(34,197,94,0.3);}}
.pill-active {{background:rgba(96,165,250,0.1);color:#93c5fd;border:1px solid rgba(96,165,250,0.25);}}

/* ── status badge ── */
.status-badge {{
  display:inline-flex;align-items:center;
  padding:3px 8px;border-radius:999px;
  font-size:11px;font-weight:500;border:1px solid;
}}

/* ── degree tabs ── */
.degree-tabs {{margin-bottom:14px;}}
.tab-bar {{
  display:flex;gap:2px;
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:var(--r-md);
  padding:3px;
  width:fit-content;
  flex-wrap:wrap;
}}
.tab {{
  display:flex;align-items:center;gap:6px;
  padding:6px 14px;border-radius:var(--r-sm);
  border:none;background:transparent;
  color:var(--text-dim);font-size:13px;font-weight:500;
  cursor:pointer;transition:color 0.12s,background 0.12s;
  white-space:nowrap;font-family:inherit;
}}
.tab:hover {{background:var(--surface-2);color:var(--text);}}
.tab.active {{background:var(--surface-3);color:var(--text);font-weight:600;}}
.tab-count {{
  display:inline-flex;align-items:center;justify-content:center;
  min-width:18px;padding:1px 5px;border-radius:999px;
  font-size:10px;font-weight:700;
  background:var(--surface-3);color:var(--text-dimmer);
}}
.tab.active .tab-count {{background:var(--surface-2);}}
.tab[data-degree="1st"].active {{color:var(--deg-1st);}}
.tab[data-degree="1st"].active .tab-count {{color:var(--deg-1st);background:rgba(245,206,74,0.12);}}
.tab[data-degree="2nd"].active {{color:var(--deg-2nd);}}
.tab[data-degree="2nd"].active .tab-count {{color:var(--deg-2nd);background:rgba(96,165,250,0.12);}}
.tab[data-degree="3rd+"].active {{color:var(--deg-3rd);}}
.tab[data-degree="inmail_only"].active {{color:var(--deg-im);}}
.tab[data-degree="inmail_only"].active .tab-count {{color:var(--deg-im);background:rgba(167,139,250,0.12);}}

/* ── toolbar ── */
.toolbar {{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:18px;}}
.search-wrap {{position:relative;flex:1;min-width:180px;max-width:340px;}}
.search-icon {{
  position:absolute;left:10px;top:50%;
  transform:translateY(-50%);
  color:var(--text-dimmer);pointer-events:none;
}}
#q {{
  width:100%;
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--r-md);color:var(--text);
  padding:7px 12px 7px 32px;font-size:13px;
  outline:none;transition:border-color 0.15s;font-family:inherit;
}}
#q:focus {{border-color:var(--accent);}}
#q::placeholder {{color:var(--text-dimmer);}}
/* ── pending tasks panel ── */
.task-panel {{margin:4px 0 24px;display:grid;gap:14px;max-width:820px;}}
.task-panel-head {{font-size:19px;font-weight:800;letter-spacing:-.01em;margin-bottom:2px;}}
.task-panel-head .task-auto {{display:block;font-size:11px;font-weight:500;letter-spacing:.02em;color:var(--text-dimmer);margin-top:4px;}}
.task-auto {{font-size:11px;font-weight:400;opacity:.6;margin-left:8px;}}
.task-block {{border:1px solid var(--border,#3333);border-radius:10px;padding:14px 18px;background:var(--card-bg,rgba(127,127,127,.06));}}
.task-block h3 {{font-size:12px;text-transform:uppercase;letter-spacing:.07em;margin:0 0 10px;color:var(--text-dim);}}
.task-block ul {{list-style:none;margin:0;padding:0;display:grid;gap:1px;}}
.task-block li {{font-size:13px;display:flex;gap:10px;align-items:center;flex-wrap:nowrap;
  padding:7px 0;border-top:1px solid var(--border-subtle,rgba(127,127,127,.14));}}
/* the meta column absorbs the slack so every action control lines up down the right edge */
.task-block li .task-meta {{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}}
.task-block li .task-copy-btn, .task-block li .task-approve, .task-block li > a {{flex:none;}}
.task-approve {{display:inline-flex;align-items:center;gap:5px;white-space:nowrap;font-size:12px;opacity:.8;}}
.task-block li:first-child {{border-top:0;}}
.task-block li strong {{min-width:150px;}}
.task-meta {{opacity:.65;font-size:12px;}}
.task-hint {{font-size:11.5px;opacity:.65;margin:8px 0 0;}}
.task-hot {{border-left:4px solid #e05d44;}}
.task-warm {{border-left:4px solid #d9a013;}}
.task-cool {{border-left:4px solid #6a9fb5;}}
.task-copy-btn {{font-size:11.5px;padding:2px 9px;border-radius:999px;border:1px solid var(--accent,#4a7dbd);background:none;color:var(--accent,#4a7dbd);cursor:pointer;}}
.task-copy-btn:hover {{background:var(--accent,#4a7dbd);color:#fff;}}
.task-approve {{font-size:11.5px;display:inline-flex;gap:4px;align-items:center;opacity:.85;cursor:pointer;}}
.task-approve-bar {{margin-top:10px;display:flex;gap:10px;align-items:center;}}

.filter-selects {{display:flex;gap:7px;flex-wrap:wrap;align-items:center;}}
.filter-select {{
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--r-md);color:var(--text);
  padding:7px 28px 7px 10px;font-size:12px;
  outline:none;cursor:pointer;
  appearance:none;-webkit-appearance:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%238b93a0' stroke-width='2'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 8px center;
  transition:border-color 0.15s;font-family:inherit;
}}
.filter-select:focus {{border-color:var(--accent);}}
.toolbar-count {{
  margin-left:auto;font-size:12px;color:var(--text-dim);
  white-space:nowrap;flex-shrink:0;
}}

/* ── cards grid ── */
.cards-grid {{
  display:grid;
  grid-template-columns:repeat(auto-fill,minmax(340px,1fr));
  gap:12px;
  /* Without this, one expanded card stretches every sibling in its row into a
     tall empty box, because grid items default to align-self:stretch. */
  align-items:start;
}}

/* ── contact card ── */
.card {{
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--r-lg);padding:16px;
  display:flex;flex-direction:column;gap:11px;
  transition:border-color 0.18s;
}}
.card:hover {{border-color:var(--surface-3);}}
/* Collapsed by default: 93 cards of full detail is unreadable. The header stays
   visible so the grid still scans; everything else opens on click. */
.card.is-collapsed {{gap:0;}}
.card.is-collapsed .card-body {{display:none;}}
.card-header {{
  display:flex;gap:10px;
  align-items:flex-start;justify-content:space-between;
  cursor:pointer;
}}
.card-header:hover .card-chevron {{color:var(--accent);}}
.card-body {{display:flex;flex-direction:column;gap:11px;}}
.card-chevron {{
  flex:none;color:var(--text-dim);font-size:11px;line-height:1;
  padding:3px 2px 0 4px;transition:transform 0.18s,color 0.18s;
  transform:rotate(0deg);
}}
.card:not(.is-collapsed) .card-chevron {{transform:rotate(90deg);color:var(--accent);}}
.toolbar-expand {{
  border:1px solid var(--border);background:var(--surface-2);color:var(--text-dim);
  border-radius:var(--r-md);padding:5px 10px;font:inherit;font-size:10px;font-weight:700;
  cursor:pointer;letter-spacing:0.02em;
}}
.toolbar-expand:hover {{border-color:var(--accent);color:var(--accent);}}
.card-header-main {{display:flex;gap:10px;flex:1;min-width:0;}}
.card-name-block {{flex:1;min-width:0;}}
.card-name {{
  font-size:14px;font-weight:600;letter-spacing:-0.01em;line-height:1.3;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
}}
.card-name a:hover {{color:var(--accent);text-decoration:underline;}}
.contact-thread-link {{border:0;background:none;color:inherit;padding:0;font:inherit;font-weight:inherit;text-align:left;cursor:pointer;}}
.contact-thread-link:hover,.contact-thread-link:focus-visible {{color:var(--accent);text-decoration:underline;text-underline-offset:3px;}}
.contact-thread-link:focus-visible {{outline:1px solid var(--accent);outline-offset:4px;border-radius:2px;}}
.card-role {{
  font-size:12px;color:var(--text-dim);margin-top:2px;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
}}
.card-company {{
  font-size:11px;color:var(--text-dimmer);margin-top:1px;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
}}
.card-header-badges {{
  display:flex;flex-direction:column;align-items:flex-end;
  gap:4px;flex-shrink:0;
}}

/* ── card badge row ── */
.card-badges {{display:flex;flex-wrap:wrap;gap:6px;align-items:center;}}

/* ── signal excerpt block ── */
.signal-excerpt-block {{
  background:var(--surface-2);
  border-left:3px solid #f97316;
  border-radius:0 var(--r-sm) var(--r-sm) 0;
  padding:10px 12px;
}}
.signal-excerpt-block.comment {{border-left-color:#fb923c;}}
.signal-excerpt-block blockquote {{
  font-size:12px;color:var(--text-dim);
  font-style:italic;line-height:1.65;margin:0;
}}

/* ── card rationale ── */
.card-rationale {{font-size:12px;color:var(--text-dim);line-height:1.6;}}
.card-notes {{border:1px solid var(--border-subtle);border-radius:var(--r-md);background:var(--surface-2);}}
.card-notes summary {{padding:8px 10px;color:var(--text-dim);font-size:10px;font-weight:700;cursor:pointer;list-style:none;}}
.card-notes summary::-webkit-details-marker {{display:none;}}
.card-notes summary:after {{content:"Open ↓";float:right;color:var(--accent);font-weight:600;}}
.card-notes[open] summary:after {{content:"Close ↑";}}
.card-notes p {{margin:0;padding:0 10px 10px;color:var(--text-dim);font-size:11px;line-height:1.65;white-space:pre-wrap;}}

/* ── card footer ── */
.card-footer {{
  display:flex;align-items:center;gap:7px;flex-wrap:wrap;
  border-top:1px solid var(--border-subtle);padding-top:9px;
}}
.card-footer-id {{
  font-family:"SF Mono","Cascadia Code","Fira Code",monospace;
  font-size:10px;color:var(--text-dimmer);letter-spacing:0.06em;
}}
.assumption-chip {{
  display:inline-block;padding:2px 7px;
  background:var(--surface-2);border:1px solid var(--border);border-radius:4px;
  font-size:11px;font-family:"SF Mono","Cascadia Code","Fira Code",monospace;
  color:var(--accent);letter-spacing:0.03em;
}}
.likelihood-factors {{
  margin-left:auto;font-size:10px;color:var(--text-dimmer);
  text-align:right;max-width:180px;line-height:1.4;
}}

/* ── empty state ── */
.empty-state {{
  text-align:center;padding:64px 24px;
  color:var(--text-dim);font-size:14px;
}}
.hidden {{display:none!important;}}

/* ── timestamp ── */
.page-timestamp {{
  position:fixed;bottom:10px;right:14px;z-index:20;
  font-size:10px;font-family:monospace;
  color:var(--text-dimmer);opacity:0.5;
  /* Fixed and transparent, it printed straight over whatever card scrolled
     beneath it. Backdrop makes it a chip; pointer-events keeps it inert. */
  background:var(--surface);border:1px solid var(--border-subtle);
  border-radius:9px;padding:2px 7px;pointer-events:none;
}}

/* ── responsive ── */
@media (max-width:900px) {{
  .cards-grid {{grid-template-columns:1fr 1fr;}}
  .priority-card {{min-width:160px;}}
  .conversion-grid {{grid-template-columns:repeat(2,minmax(0,1fr));}}
  .cube3d-controls {{justify-content:flex-start;}}
  .cube3d-readout {{grid-template-columns:1fr;gap:7px;}}
  .lr-grid-head {{display:none;}}
  .lr-row {{grid-template-columns:112px 1fr 1fr;}}
  .lr-money {{grid-column:1/-1;padding-top:37px!important;border-right:0!important;border-top:1px solid var(--border-subtle);}}
  .lr-flow {{padding-left:0;}}
}}
@media (max-width:600px) {{
  .page {{padding:20px 14px 64px;}}
  .cards-grid {{grid-template-columns:1fr;}}
  .priority-cards {{flex-direction:column;}}
  .priority-card {{max-width:100%;}}
  .tab-bar {{width:100%;}}
  .toolbar {{flex-direction:column;align-items:stretch;}}
  .search-wrap {{max-width:100%;}}
  .kpi-sep {{display:none;}}
  .conversion-grid {{grid-template-columns:1fr;}}
  .cube3d {{padding:13px 10px 11px;}}
  .cube3d-controls {{align-items:stretch;}}
  .cube3d-lenses,.cube3d-scope {{width:100%;}}
  .cube3d-lenses button,.cube3d-scope button {{flex:1;padding-inline:6px;}}
  .cube3d-select-label {{width:100%;}}
  .cube3d-select-label select {{width:100%;}}
  .cube3d-axis-key {{display:grid;gap:5px;}}
  .cube3d-stage svg {{min-height:340px;}}
  .cube3d-axis {{font-size:8px;}}
  .cube3d-readout {{padding-inline:4px;}}
  .cube3d-audit,.cube3d-legend {{margin-inline:4px;}}
  .lr-hero {{grid-template-columns:1fr;gap:7px;}}
  .lr-break {{height:28px;}}
  .lr-break::before {{top:50%;}}
  .lr-break span {{width:74px;height:26px;border-radius:13px;}}
  .lr-thesis {{grid-template-columns:1fr;gap:5px;}}
  .lr-thesis em {{white-space:normal;}}
  .lr-flow {{display:none;}}
  .lr-row {{grid-template-columns:1fr;}}
  .lr-row>div {{border-right:0;border-bottom:1px solid var(--border-subtle);}}
  .lr-row>div:last-child {{border-bottom:0;}}
  .lr-money {{grid-column:auto;border-top:0;}}
}}
</style>
</head>
<body>
<div class="page">

<!-- ── page header ── -->
<header class="page-header">
  <h1>Strategy control room — <span class="idea-name">{idea_title}</span></h1>
  <p class="subtitle">{total} contacts &middot; last updated {last_updated} &middot; generated {escape(now)}</p>
</header>

<!-- ── tab nav ── -->
<nav class="tab-nav">
  <button data-tab="tasks" onclick="switchTab('tasks')">To do <span class="count" id="taskTabCount">0</span></button>
  <button data-tab="thesis" onclick="switchTab('thesis')">Hunches <span class="count">{active_hunch}</span></button>
  <button data-tab="patterns" onclick="switchTab('patterns')">Pain Patterns <span class="count">{patterns_count}</span></button>
  <button data-tab="offerings" onclick="switchTab('offerings')">Offerings <span class="count">{offerings_count}</span></button>
  <button data-tab="pages" onclick="switchTab('pages')">Pages <span class="count">{pages_count}</span></button>
  <button data-tab="companies" onclick="switchTab('companies')">Companies <span class="count">{companies_count}</span></button>
  <button data-tab="startups" onclick="switchTab('startups')">Startups <span class="count">{startups_count}</span></button>
  <button data-tab="email" onclick="switchTab('email')">Research &amp; papers <span class="count">{email_count}</span></button>
  <button class="active" data-tab="contacts" onclick="switchTab('contacts')">Contacts <span class="count">{total}</span></button>
</nav>

<!-- ── pending tasks (auto-derived from contacts.md + copy archive on every rebuild) ── -->
<div class="tab-panel" data-tab="tasks">
<section class="task-panel" id="taskPanel" aria-label="Pending tasks"></section>
</div>

<div class="tab-panel" data-tab="thesis">
{thesis_tab_html}
</div><!-- /tab-panel thesis -->

<div class="tab-panel" data-tab="offerings">
{offerings_tab_html}
</div><!-- /tab-panel offerings -->

<div class="tab-panel" data-tab="pages">
{pages_tab_html}
</div><!-- /tab-panel pages -->

<div class="tab-panel" data-tab="startups">
{startups_tab_html}
</div><!-- /tab-panel startups -->

<div class="tab-panel active" data-tab="contacts">

<!-- ── summary strip ── -->
<section class="summary-strip" aria-label="Summary">
  <div class="kpi-row">
    <div class="kpi-item">
      <span class="kpi-value">{total}</span>
      <span class="kpi-label">Total</span>
    </div>
    <div class="kpi-sep"></div>
    <div class="kpi-item">
      <span class="kpi-dot" style="background:var(--deg-1st)"></span>
      <span class="kpi-value" style="color:var(--deg-1st)">{d1}</span>
      <span class="kpi-label">1st</span>
    </div>
    <div class="kpi-item">
      <span class="kpi-dot" style="background:var(--deg-2nd)"></span>
      <span class="kpi-value" style="color:var(--deg-2nd)">{d2}</span>
      <span class="kpi-label">2nd</span>
    </div>
    <div class="kpi-item">
      <span class="kpi-dot" style="background:var(--deg-3rd)"></span>
      <span class="kpi-value">{d3}</span>
      <span class="kpi-label">3rd+</span>
    </div>
    <div class="kpi-item">
      <span class="kpi-dot" style="background:var(--deg-im)"></span>
      <span class="kpi-value" style="color:var(--deg-im)">{dim}</span>
      <span class="kpi-label">InMail</span>
    </div>
    <div class="kpi-sep"></div>
    <div class="kpi-item">
      <span class="kpi-dot" style="background:#94a3b8"></span>
      <span class="kpi-value">{pending_count}</span>
      <span class="kpi-label">Pending</span>
    </div>
    <div class="kpi-item">
      <span class="kpi-dot" style="background:#22c55e"></span>
      <span class="kpi-value">{done_count}</span>
      <span class="kpi-label">Done</span>
    </div>
    <div class="kpi-item">
      <span class="kpi-dot" style="background:#a78bfa"></span>
      <span class="kpi-value">{accepted_count}</span>
      <span class="kpi-label">Accepted</span>
    </div>
  </div>
  <div class="conversion-section" aria-label="Campaign conversion rates">
    <div class="conversion-header">
      <div class="conversion-title">Campaign conversion · confirmed through {rates_confirmed_through}</div>
      <span class="freshness-badge {freshness_class}">{freshness_label}</span>
    </div>
    <div class="conversion-grid">
      <div class="conversion-card">
        <span class="conversion-eyebrow">Target coverage</span>
        <strong class="conversion-rate">{target_to_contact_rate:g}%</strong>
        <span class="conversion-detail">{outreach_started_count} messaged or invited / {total} targeted</span>
      </div>
      <div class="conversion-card primary">
        <span class="conversion-eyebrow">Reply rate</span>
        <strong class="conversion-rate">{reply_rate:g}%</strong>
        <span class="conversion-detail">{replied_count} responses ({qualified_replied_count} qualified) / {contacted_count} messaged</span>
      </div>
      <div class="conversion-card">
        <span class="conversion-eyebrow">Replies advancing to call</span>
        <strong class="conversion-rate">{reply_to_call_rate:g}%</strong>
        <span class="conversion-detail">{call_progressed_count} offered, asked or booked / {replied_count} replies</span>
      </div>
      <div class="conversion-card">
        <span class="conversion-eyebrow">Calls booked</span>
        <strong class="conversion-rate">{reply_to_scheduled_rate:g}%</strong>
        <span class="conversion-detail">{scheduled_count} scheduled / {replied_count} replies</span>
      </div>
      {assumption_conversion_html}
    </div>
  </div>
  <div class="priority-section">
    <div class="priority-label">Top priority</div>
    <div class="priority-cards">
      {priority_html}
    </div>
  </div>
</section>
{invite_log_html}

<!-- ── degree tabs ── -->
<div class="degree-tabs">
  <div class="tab-bar" role="tablist" aria-label="Filter by network degree">
    <button class="tab active" role="tab" data-degree="" aria-selected="true">
      All <span class="tab-count">{total}</span>
    </button>
    <button class="tab" role="tab" data-degree="1st" aria-selected="false">
      1st Degree <span class="tab-count">{d1}</span>
    </button>
    <button class="tab" role="tab" data-degree="2nd" aria-selected="false">
      2nd Degree <span class="tab-count">{d2}</span>
    </button>
    <button class="tab" role="tab" data-degree="3rd+" aria-selected="false">
      3rd+ Degree <span class="tab-count">{d3}</span>
    </button>
    <button class="tab" role="tab" data-degree="inmail_only" aria-selected="false">
      InMail <span class="tab-count">{dim}</span>
    </button>
  </div>
</div>

<!-- ── toolbar ── -->
<div class="toolbar">
  <div class="search-wrap">
    <svg class="search-icon" width="14" height="14" viewBox="0 0 24 24" fill="none"
         stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
    </svg>
    <input type="search" id="q" placeholder="Search name, company, role..." autocomplete="off">
  </div>
  <div class="filter-selects">
    <select id="fltTier" class="filter-select" aria-label="Filter by tier">
      <option value="">All tiers</option>
    </select>
    <select id="fltStatus" class="filter-select" aria-label="Filter by status">
      <option value="">All status</option>
    </select>
    <select id="fltSignal" class="filter-select" aria-label="Filter by signal">
      <option value="">All signals</option>
    </select>
    <select id="fltAssumption" class="filter-select" aria-label="Filter by assumption">
      <option value="">All assumptions</option>
    </select>
    <select id="fltCopy" class="filter-select" aria-label="Filter by copy status">
      <option value="">All (copy or not)</option>
      <option value="ready">✍ Copy ready to send</option>
      <option value="missing">— No copy yet</option>
    </select>
    <select id="sortBy" class="filter-select" aria-label="Sort contacts">
      <option value="score">Score high-low</option>
      <option value="activity">Active first</option>
      <option value="name">Name A-Z</option>
      <option value="copy_ready_first">Copy-ready first</option>
    </select>
  </div>
  <span class="toolbar-count" id="cnt" aria-live="polite"></span>
  <button class="toolbar-expand" id="expandAll" type="button" data-collapsed="1">Expand all</button>
</div>

<!-- ── cards ── -->
<div class="cards-grid" id="cardsGrid" role="list" aria-label="Contacts"></div>
<div class="empty-state hidden" id="emptyState" role="status">
  <p>No contacts match the current filters.</p>
</div>

</div><!-- /tab-panel contacts -->

<div class="tab-panel" data-tab="companies">
{companies_tab_html}
</div><!-- /tab-panel companies -->

<div class="tab-panel" data-tab="email">
{email_tab_html}
</div><!-- /tab-panel email -->

<div class="tab-panel" data-tab="patterns">
{patterns_tab_html}
</div><!-- /tab-panel patterns -->

</div><!-- .page -->

<div class="page-timestamp" aria-hidden="true">gen {escape(now)}</div>

<!-- ── copy modal ── -->
<div id="copyModal" class="modal-backdrop" role="dialog" aria-modal="true" aria-label="Outreach copy" onclick="modalBackdropClick(event)">
  <div class="modal-box">
    <div class="modal-header">
      <span class="modal-title" id="modalTitle"></span>
      <button class="modal-close" onclick="closeCopyModal()" aria-label="Close">&times;</button>
    </div>
    <div class="modal-body" id="modalBody"></div>
  </div>
</div>

<!-- ── shared email-thread modal: opened from Email or Contacts ── -->
<div class="email-modal-backdrop" id="emailModal" hidden>
  <section class="email-modal" role="dialog" aria-modal="true" aria-labelledby="emailModalName">
    <div id="emailModalBody"></div>
  </section>
</div>

<script>
var CONTACTS = {contacts_json};
var COPY_BY_ID = {copy_by_id_json};
var EMAIL_CAMPAIGN = {email_campaign_json};
var STATUS_COLORS = {json.dumps(STATUS_COLORS)};

var activeDegree = "";

function normDeg(d) {{
  d = (d || "").trim().toLowerCase();
  if (d === "1st") return "1st";
  if (d === "2nd") return "2nd";
  if (d.startsWith("3rd") || d.startsWith("3+")) return "3rd+";
  return "inmail_only";
}}

function degClass(deg) {{
  var m = {{"1st":"deg-1st","2nd":"deg-2nd","3rd+":"deg-3rdplus","inmail_only":"deg-inmail"}};
  return m[deg] || "deg-inmail";
}}

function degLabel(deg) {{
  var m = {{"1st":"1st","2nd":"2nd","3rd+":"3rd+","inmail_only":"InMail"}};
  return m[deg] || "—";
}}

function scoreClass(n) {{
  if (n == null) return "score-dim";
  if (n >= 8) return "score-green";
  if (n >= 5) return "score-yellow";
  return "score-red";
}}

function esc(s) {{
  return String(s || "").replace(/[&<>"']/g, function(m) {{
    var map = {{"&":"&amp;","<":"&lt;",">":"&gt;"}};
    map['"'] = "&quot;";
    map["'"] = "&#39;";
    return map[m];
  }});
}}

  function relationshipBadge(c) {{
    var k = (c.relationship_type || "").trim();
    if (!k) return "";
    var cls = k === "peer_founder_competitor" ? " relationship-competitor" : "";
    return '<span class="relationship-badge' + cls + '">' + esc(k.replace(/_/g, " ")) + "</span>";
  }}
  function callBadge(c) {{
    var k = (c.call_stage || "").trim();
    if (!k || k === "none") return "";
    return '<span class="call-badge">call: ' + esc(k.replace(/_/g, " ")) + "</span>";
  }}
function cardHtml(c) {{
  var deg = normDeg(c.degree);
  var sc = scoreClass(c.response_likelihood);
  var scoreStr = c.response_likelihood != null ? String(c.response_likelihood) : "—";
  var nameInner = esc(c.name || "—");
  var hasEmailThread = EMAIL_CAMPAIGN.some(function(r) {{ return r.contact_id === c.id; }});
  var nameHtml = hasEmailThread
    ? '<button class="contact-thread-link" type="button" data-email-contact="' + esc(c.id) + '" aria-label="Open email thread for ' + nameInner + '">' + nameInner + "</button>"
    : (c.linkedin_url
      ? '<a href="' + esc(c.linkedin_url) + '" target="_blank" rel="noopener">' + nameInner + "</a>"
      : nameInner);
  var tierKey = c.tier || "other";
  var signalKey = c.signal_type || "profile_fit";
  var statusColor = STATUS_COLORS[c.outreach_status] || "#64748b";

  var excerptHtml = "";
  if ((signalKey === "post_engagement" || signalKey === "comment_signal") && c.signal_excerpt) {{
    var exClass = signalKey === "comment_signal"
      ? "signal-excerpt-block comment"
      : "signal-excerpt-block";
    excerptHtml = '<div class="' + exClass + '"><blockquote>“' + esc(c.signal_excerpt) + '”</blockquote></div>';
  }}

  var otwHtml = c.open_to_work ? '<span class="pill-sm pill-otw">Open to work</span>' : "";
  var activeHtml = c.active_last_30d ? '<span class="pill-sm pill-active">Active 30d</span>' : "";

  var rationaleHtml = c.validation_rationale
    ? '<p class="card-rationale">' + esc(c.validation_rationale) + "</p>"
    : "";
  var notesHtml = c.notes
    ? '<details class="card-notes"><summary>Research &amp; contact notes</summary><p>' + esc(c.notes) + "</p></details>"
    : "";

  var chips = (c.assumptions_tested || []).map(function(a) {{
    return '<span class="assumption-chip">' + esc(a) + "</span>";
  }}).join("");

  var lfHtml = c.likelihood_factors
    ? '<span class="likelihood-factors">' + esc(c.likelihood_factors) + "</span>"
    : "";

  // ── Outreach copy block ──
  var copy = COPY_BY_ID[c.id];
  var copyHtml = "";
  var sendOrderHtml = "";
  if (copy) {{
    var langBadge = '<span class="copy-lang">' + esc(copy.language || "EN") + "</span>";
    var warmBadgeHtml = copy.is_warm ? '<span class="warm-badge">&#9889; Warm — reply received</span>' : "";
    sendOrderHtml = copy.send_order
      ? '<span class="send-order-badge">#' + copy.send_order + "</span>"
      : "";

    var summaryLabel = copy.is_warm
      ? "Reply — send Message 2"
      : (copy.send_order ? "Copy #" + copy.send_order + " ready" : "Copy ready");

    copyHtml =
      '<div class="card-copy-trigger" data-cid="' + esc(c.id) + '">' +
        '<span class="copy-summary-label">' + esc(summaryLabel) + "</span>" +
        langBadge + warmBadgeHtml +
        '<span class="copy-trigger-arrow">&#8599;</span>' +
      "</div>";
  }} else if (c.assumptions_tested && c.assumptions_tested.length) {{
    copyHtml =
      '<div class="card-copy-empty">' +
        '<em>No copy yet.</em> Run <code>/startup-outreach-copy ' +
        esc(c.assumptions_tested[0]) + '</code> to draft messages.' +
      "</div>";
  }}

  return (
    '<div class="card is-collapsed' + (copy ? " has-copy" : "") + '" role="listitem">' +
      '<div class="card-header" role="button" tabindex="0" aria-expanded="false"' +
           ' aria-label="Toggle details for ' + esc(c.name || c.id) + '">' +
        '<div class="card-header-main">' +
          '<span class="card-chevron" aria-hidden="true">&#9654;</span>' +
          (sendOrderHtml ? sendOrderHtml : '<div class="card-score ' + sc + '">' + scoreStr + "</div>") +
          '<div class="card-name-block">' +
            '<div class="card-name">' + nameHtml + "</div>" +
            '<div class="card-role">' + esc(c.role || "") + "</div>" +
            '<div class="card-company">' + esc(c.company || "") + "</div>" +
          "</div>" +
        "</div>" +
        '<div class="card-header-badges">' +
          (sendOrderHtml ? '<div class="card-score ' + sc + '">' + scoreStr + "</div>" : "") +
          '<span class="deg-badge ' + degClass(deg) + '">' + degLabel(deg) + "</span>" +
          '<span class="tier-badge tier-' + esc(tierKey) + '">' + esc(tierKey.replace(/_/g, " ")) + "</span>" +
          relationshipBadge(c) +
        "</div>" +
      "</div>" +
      '<div class="card-body">' +
        '<div class="card-badges">' +
          '<span class="signal-badge signal-' + esc(signalKey) + '">' + esc(signalKey.replace(/_/g, " ")) + "</span>" +
          otwHtml + activeHtml +
          '<span class="status-badge" style="border-color:' + statusColor + ";color:" + statusColor + '">' +
            esc(c.outreach_status || "pending") +
          "</span>" +
          callBadge(c) +
        "</div>" +
        excerptHtml +
        rationaleHtml +
        notesHtml +
        copyHtml +
        '<div class="card-footer">' +
          '<span class="card-footer-id">' + esc(c.id) + "</span>" +
          chips + lfHtml +
        "</div>" +
      "</div>" +
    "</div>"
  );
}}

function copyToClipboard(btn, text) {{
  navigator.clipboard.writeText(text).then(function() {{
    var orig = btn.textContent;
    btn.textContent = "✓ Copied";
    btn.classList.add("copied");
    setTimeout(function() {{ btn.textContent = orig; btn.classList.remove("copied"); }}, 1500);
  }});
}}

function openCopyModal(cid) {{
  var copy = COPY_BY_ID && COPY_BY_ID[cid];
  if (!copy) return;
  var modal = document.getElementById("copyModal");
  var titleEl = document.getElementById("modalTitle");
  var bodyEl = document.getElementById("modalBody");

  var c = CONTACTS.find(function(x) {{ return x.id === cid; }});
  var name = c ? (c.name || cid) : cid;
  var titleText = name;
  if (copy.send_order) titleText += "  ·  Copy #" + copy.send_order;
  if (copy.is_warm) titleText += "  ·  ⚡ Warm";
  titleEl.textContent = titleText;

  var msgs = copy.messages || [];
  var html = "";
  for (var i = 0; i < msgs.length; i++) {{
    var m = msgs[i];
    var bodyJson = JSON.stringify(m.body).replace(/</g, "\\u003c");
    html +=
      '<div class="copy-msg">' +
        '<div class="copy-msg-head">' +
          '<span class="copy-msg-num">' + (i + 1) + '</span>' +
          '<span class="copy-msg-label">' + esc(m.label) + '</span>' +
          (m.chars ? '<span class="copy-msg-count">' + esc(m.chars) + '</span>' : '') +
          '<button class="copy-btn" onclick="copyToClipboard(this,' + bodyJson + ')">Copy</button>' +
        '</div>' +
        '<pre class="copy-body">' + esc(m.body) + '</pre>' +
      '</div>';
  }}
  if (!html) {{
    html = '<div class="copy-msg"><pre class="copy-body">No drafted message in ' +
           esc(copy.source_file || "the copy archive") +
           ' for this contact. Messages must be quoted (&gt;) or fenced to appear here.</pre></div>';
  }}
  bodyEl.innerHTML = html;
  modal.classList.add("open");
  document.body.style.overflow = "hidden";
}}

function closeCopyModal() {{
  document.getElementById("copyModal").classList.remove("open");
  document.body.style.overflow = "";
}}

function modalBackdropClick(e) {{
  if (e.target === document.getElementById("copyModal")) closeCopyModal();
}}

document.addEventListener("keydown", function(e) {{
  if (e.key === "Escape") closeCopyModal();
}});

document.addEventListener("click", function(e) {{
  var emailContact = e.target.closest("[data-email-contact]");
  if (emailContact && window.openEmailThreadByContact) {{
    window.openEmailThreadByContact(emailContact.dataset.emailContact);
    return;
  }}
  var trigger = e.target.closest(".card-copy-trigger");
  if (trigger && trigger.dataset.cid) {{ openCopyModal(trigger.dataset.cid); return; }}
  // Card expand/collapse. Ignore clicks that landed on a real control inside the
  // header (the name link, the email-thread button) so those keep working.
  var head = e.target.closest(".card-header");
  if (head && !e.target.closest("a, button, summary, input, select")) toggleCard(head);
}});

function toggleCard(head, force) {{
  var card = head.closest(".card");
  if (!card) return;
  var collapse = force === undefined ? !card.classList.contains("is-collapsed") : force;
  card.classList.toggle("is-collapsed", collapse);
  head.setAttribute("aria-expanded", collapse ? "false" : "true");
}}

// Keyboard parity: the header is role="button", so Enter and Space must work.
document.addEventListener("keydown", function(e) {{
  if (e.key !== "Enter" && e.key !== " " && e.key !== "Spacebar") return;
  var head = e.target.closest && e.target.closest(".card-header");
  if (!head || e.target.closest("a, button, summary, input, select")) return;
  e.preventDefault();
  toggleCard(head);
}});

function setAllCards(collapse) {{
  var heads = document.querySelectorAll("#cardsGrid .card-header");
  for (var i = 0; i < heads.length; i++) toggleCard(heads[i], collapse);
  var btn = document.getElementById("expandAll");
  if (btn) {{
    btn.textContent = collapse ? "Expand all" : "Collapse all";
    btn.dataset.collapsed = collapse ? "1" : "0";
  }}
}}

function renderCards(list) {{
  var grid = document.getElementById("cardsGrid");
  var empty = document.getElementById("emptyState");
  document.getElementById("cnt").textContent = list.length + " of " + CONTACTS.length;
  if (!list.length) {{
    grid.innerHTML = "";
    empty.classList.remove("hidden");
  }} else {{
    empty.classList.add("hidden");
    grid.innerHTML = list.map(cardHtml).join("");
  }}
  // Cards re-render collapsed on every filter/sort, so the control must agree.
  var expBtn = document.getElementById("expandAll");
  if (expBtn) {{ expBtn.textContent = "Expand all"; expBtn.dataset.collapsed = "1"; }}
}}

function apply() {{
  var qv = document.getElementById("q").value.toLowerCase();
  var tv = document.getElementById("fltTier").value;
  var sv = document.getElementById("fltStatus").value;
  var sigv = document.getElementById("fltSignal").value;
  var av = document.getElementById("fltAssumption").value;
  var cv = (document.getElementById("fltCopy") || {{value:""}}).value;
  var sort = document.getElementById("sortBy").value;

  var list = CONTACTS.filter(function(c) {{
    if (activeDegree && normDeg(c.degree) !== activeDegree) return false;
    if (tv && c.tier !== tv) return false;
    if (sv && c.outreach_status !== sv) return false;
    if (sigv && c.signal_type !== sigv) return false;
    if (av && (c.assumptions_tested || []).indexOf(av) === -1) return false;
    var hasCopy = !!(COPY_BY_ID && COPY_BY_ID[c.id]);
    if (cv === "ready" && !hasCopy) return false;
    if (cv === "missing" && hasCopy) return false;
    if (qv) {{
      var hay = [c.name, c.company, c.role, c.notes, c.signal_excerpt].join(" ").toLowerCase();
      if (hay.indexOf(qv) === -1) return false;
    }}
    return true;
  }});

  list.sort(function(a, b) {{
    if (sort === "name") return (a.name || "").localeCompare(b.name || "");
    if (sort === "copy_ready_first") {{
      var ac = !!(COPY_BY_ID && COPY_BY_ID[a.id]) ? 1 : 0;
      var bc = !!(COPY_BY_ID && COPY_BY_ID[b.id]) ? 1 : 0;
      if (ac !== bc) return bc - ac;
      // Copy-ready first, then within each group sort by score desc
    }}
    if (sort === "activity") {{
      var ai = a.active_last_30d ? 1 : 0;
      var bi = b.active_last_30d ? 1 : 0;
      if (ai !== bi) return bi - ai;
    }}
    var sa = a.response_likelihood, sb = b.response_likelihood;
    if (sa == null && sb == null) return 0;
    if (sa == null) return 1;
    if (sb == null) return -1;
    return sb - sa;
  }});

  renderCards(list);
}}

// Degree tab handlers
document.querySelectorAll(".tab").forEach(function(btn) {{
  btn.addEventListener("click", function() {{
    document.querySelectorAll(".tab").forEach(function(t) {{
      t.classList.remove("active");
      t.setAttribute("aria-selected", "false");
    }});
    btn.classList.add("active");
    btn.setAttribute("aria-selected", "true");
    activeDegree = btn.dataset.degree;
    apply();
  }});
}});

// Filter / search handlers
["q", "fltTier", "fltStatus", "fltSignal", "fltAssumption", "fltCopy", "sortBy"].forEach(function(id) {{
  document.getElementById(id).addEventListener("input", apply);
}});

// Populate dropdowns
(function() {{
  var TIER_ORDER = Array.from(new Set(CONTACTS.map(function(c) {{ return c.tier; }}).filter(Boolean))).sort();
  var STATUS_ORDER_LIST = ["pending","invited","accepted","replied","scheduled","done","no_reply","declined","off_scope"];
  var SIGNAL_ORDER_LIST = ["post_engagement","comment_signal","job_posting","profile_fit"];

  var tierSel = document.getElementById("fltTier");
  TIER_ORDER.forEach(function(v) {{
    if (CONTACTS.some(function(c) {{ return c.tier === v; }})) {{
      var o = document.createElement("option");
      o.value = v; o.textContent = v.replace(/_/g, " ");
      tierSel.appendChild(o);
    }}
  }});

  var statusSel = document.getElementById("fltStatus");
  var STATUS_LABELS = {{
    pending: "not yet invited (unsent)",
    invited: "invited — awaiting accept",
    accepted: "accepted — connected",
    replied: "replied",
    scheduled: "call scheduled",
    done: "interviewed",
    no_reply: "no reply",
    declined: "declined",
    off_scope: "off scope"
  }};
  STATUS_ORDER_LIST.forEach(function(v) {{
    var n = CONTACTS.filter(function(c) {{ return c.outreach_status === v; }}).length;
    if (n > 0) {{
      var o = document.createElement("option");
      o.value = v; o.textContent = (STATUS_LABELS[v] || v) + " (" + n + ")";
      statusSel.appendChild(o);
    }}
  }});

  var signalSel = document.getElementById("fltSignal");
  SIGNAL_ORDER_LIST.forEach(function(v) {{
    if (CONTACTS.some(function(c) {{ return c.signal_type === v; }})) {{
      var o = document.createElement("option");
      o.value = v; o.textContent = v.replace(/_/g, " ");
      signalSel.appendChild(o);
    }}
  }});

  var assumSel = document.getElementById("fltAssumption");
  var assum = [];
  CONTACTS.forEach(function(c) {{
    (c.assumptions_tested || []).forEach(function(a) {{
      if (assum.indexOf(a) === -1) assum.push(a);
    }});
  }});
  assum.sort().forEach(function(a) {{
    var o = document.createElement("option");
    o.value = a; o.textContent = a;
    assumSel.appendChild(o);
  }});
}})();

// ── Pending tasks panel: derived, never hand-maintained ──
(function() {{
  var panel = document.getElementById("taskPanel");
  if (!panel) return;
  function sentMarker(c) {{ return /\\[msg\\d+ sent\\]/i.test(c.notes || ""); }}
  function hasCopy(c) {{ return !!(COPY_BY_ID && COPY_BY_ID[c.id]); }}

  var sendMsg1 = [], draftNeeded = [], replyNeeded = [], gated = [], invitesQueued = 0, awaiting = 0;
  // LR-B30: someone messaged inside the last three months with no reply must not be written to
  // again. The gate lives in the contact's notes and outlives any status change, so a re-screen
  // that flips `held` to `pending` cannot quietly put them back in a send queue.
  function b30(c) {{
    var n = c.notes || "";
    return /\\[LR-B30[^\\]]*\\]/i.test(n) && !/\\[msg\\d+ sent/i.test(n);
  }}
  CONTACTS.forEach(function(c) {{
    var s = c.outreach_status || "pending";
    if (s === "accepted") {{
      if (sentMarker(c)) return;
      if (b30(c)) gated.push(c); else (hasCopy(c) ? sendMsg1 : draftNeeded).push(c);
    }} else if (s === "replied") {{
      // Only LinkedIn threads are ours to answer here. A phone call is not an open thread.
      // Absent channel means LinkedIn - that is the declared default in vocabularies.yaml, and
      // testing === "linkedin" dropped every card that relied on it (C122, 2026-09-05).
      // A reply the founder has already answered (msg2+ sent marker) is their turn, not ours.
      var ch = c.channel || "linkedin";
      if (ch === "linkedin" && !/\\[msg[2-9] sent\\b/i.test(c.notes || "")) replyNeeded.push(c);
    }} else if (s === "pending") {{
      // A 1st-degree contact needs no invite, so a drafted message to one is a SEND, not a
      // queue entry. Without this the whole 1st-degree batch was invisible on this page.
      if (b30(c)) gated.push(c);
      else if (c.degree === "1st" && hasCopy(c)) sendMsg1.push(c);
      else if (c.degree === "1st") draftNeeded.push(c);
      else invitesQueued++;
    }} else if (s === "invited") {{
      awaiting++;
    }}
  }});

  function personLink(c, withCopy) {{
    var chip = withCopy
      ? '<button class="task-copy-btn" data-task-cid="' + esc(c.id) + '">open draft</button>'
      : '<a href="' + esc(c.linkedin_url || "#") + '" target="_blank" rel="noopener">profile</a>';
    var box = withCopy
      ? '<label class="task-approve"><input type="checkbox" class="task-approve-box" value="' + esc(c.id) + '"> approve</label>'
      : "";
    return '<li><strong>' + esc(c.name || c.id) + '</strong> <span class="task-meta">' +
           esc((c.role || "").slice(0, 38)) + (c.company ? " · " + esc(String(c.company).slice(0, 26)) : "") +
           '</span> ' + chip + box + "</li>";
  }}

  var blocks = [];
  if (sendMsg1.length) {{
    blocks.push('<div class="task-block task-hot"><h3>Send Msg 1 — accepted, draft ready (' + sendMsg1.length + ')</h3><ul>' +
      sendMsg1.map(function(c) {{ return personLink(c, true); }}).join("") +
      '</ul><div class="task-approve-bar"><button class="task-copy-btn" id="copyApproval">Copy approval message for Claude</button><span class="task-hint" id="approvalCount"></span></div>' +
      '<p class="task-hint">Read each draft, tick the ones you approve, click the button, paste the result to Claude in chat. Claude sends the approved messages verbatim and stamps the ledger (copy-rules amendment 2026-08-25). Or send by hand and tell Claude "sent to {{name}}".</p></div>');
  }}
  if (draftNeeded.length) {{
    blocks.push('<div class="task-block task-warm"><h3>Draft needed — accepted, no copy yet (' + draftNeeded.length + ')</h3><ul>' +
      draftNeeded.map(function(c) {{ return personLink(c, false); }}).join("") +
      '</ul><p class="task-hint">Ask Claude: "draft Msg 1 for the accepted contacts".</p></div>');
  }}
  if (replyNeeded.length) {{
    blocks.push('<div class="task-block task-hot"><h3>Reply waiting (' + replyNeeded.length + ')</h3><ul>' +
      replyNeeded.map(function(c) {{ return personLink(c, hasCopy(c)); }}).join("") + "</ul></div>");
  }}
  if (gated.length) {{
    blocks.push('<div class="task-block task-cool"><h3>Held by LR-B30 (' + gated.length + ')</h3><ul>' +
      gated.map(function(c) {{ return personLink(c, false); }}).join("") +
      '</ul><p class="task-hint">Messaged inside the last three months with no reply. Do not write again yet, whatever their status says.</p></div>');
  }}
  blocks.push('<div class="task-block task-cool"><h3>Queue</h3><p class="task-hint">' +
    invitesQueued + " targets waiting for the next invite window · " + awaiting + " invites out awaiting acceptance</p></div>");

  var openCount = sendMsg1.length + draftNeeded.length + replyNeeded.length;
  var badge = document.getElementById("taskTabCount");
  if (badge) badge.textContent = openCount;
  panel.innerHTML = '<div class="task-panel-head">To do <span class="task-auto">auto-generated from the ledger on every rebuild</span></div>' + blocks.join("");
  panel.addEventListener("click", function(e) {{
    var btn = e.target.closest("[data-task-cid]");
    if (btn) openCopyModal(btn.getAttribute("data-task-cid"));
    if (e.target.closest("#copyApproval")) {{
      var ids = Array.from(panel.querySelectorAll(".task-approve-box:checked")).map(function(b) {{ return b.value; }});
      var names = ids.map(function(id) {{
        var c = CONTACTS.find(function(x) {{ return x.id === id; }});
        return id + " " + (c ? (c.name || "") : "");
      }});
      var msg = ids.length
        ? "Approved to send, verbatim from the copy archive: " + names.join("; ")
        : "";
      var b = e.target.closest("#copyApproval");
      if (!ids.length) {{ b.textContent = "Tick some drafts first"; setTimeout(function() {{ b.textContent = "Copy approval message for Claude"; }}, 1500); return; }}
      copyToClipboard(b, msg);
    }}
  }});
  panel.addEventListener("change", function(e) {{
    if (!e.target.classList.contains("task-approve-box")) return;
    var n = panel.querySelectorAll(".task-approve-box:checked").length;
    var el = document.getElementById("approvalCount");
    if (el) el.textContent = n ? n + " approved" : "";
  }});
}})();

(function() {{
  var btn = document.getElementById("expandAll");
  if (btn) btn.addEventListener("click", function() {{
    setAllCards(btn.dataset.collapsed !== "1");
  }});
}})();

apply();
</script>
{email_script}
{tab_scripts}
</body>
</html>
"""


# ─── intel parsing ──────────────────────────────────────────────────────────
#
# `companies.md` and `company-intel.md` are produced by the startup-outreach-intel
# skill. Both are markdown files with per-company blocks under `## CompanyName`
# headings; each block is YAML. company-intel.md has deeply-nested structures
# (`contracts:` is a list of dicts with `title`, `value`, `role`, etc.) so we use
# PyYAML for parsing. When PyYAML isn't installed the intel tab renders an empty
# state — no crashes.


COMPANIES_CSS = """
/* ── companies registry ── */
.co-wrap {display:flex;flex-direction:column;gap:16px;}
.co-hero {border:1px solid var(--border);border-radius:var(--r-lg);background:var(--surface);padding:22px 24px;}
.co-eyebrow {font-size:10px;text-transform:uppercase;letter-spacing:.12em;color:var(--accent);font-weight:700;}
.co-hero h2 {font-family:Georgia,"Iowan Old Style",serif;font-size:26px;line-height:1.12;margin:8px 0 7px;letter-spacing:-.025em;}
.co-hero p {max-width:760px;color:var(--text-dim);font-size:12px;line-height:1.6;margin:0;}
.co-kpis {display:flex;flex-wrap:wrap;gap:8px;margin-top:18px;}
.co-kpi {min-width:110px;padding:10px 12px;border:1px solid var(--border);border-radius:var(--r-md);background:var(--surface-2);}
.co-kpi strong {display:block;font-size:20px;line-height:1;color:var(--text);font-variant-numeric:tabular-nums;}
.co-kpi span {display:block;margin-top:5px;font-size:9px;text-transform:uppercase;letter-spacing:.09em;color:var(--text-dimmer);}
.co-group {border:1px solid var(--border);border-radius:var(--r-lg);background:var(--surface);overflow:hidden;}
.co-group-head {display:flex;align-items:center;justify-content:space-between;gap:12px;padding:10px 18px;border-bottom:1px solid var(--border);background:var(--surface-2);color:var(--text-dimmer);font-size:9px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;}
.co-group-head b {color:var(--text-dim);font-weight:800;}
.co-row {--co-side:#64748b;position:relative;display:grid;grid-template-columns:minmax(0,1fr) 190px;gap:16px;padding:14px 18px 15px 21px;border-bottom:1px solid var(--border-subtle);}
.co-row:last-child {border-bottom:none;}
.co-row:before {content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--co-side);opacity:.75;}
.co-row[data-side="demand"] {--co-side:#22c55e;}
.co-row[data-side="supply"] {--co-side:#60a5fa;}
.co-row[data-side="competitor"] {--co-side:#f59e0b;}
.co-row[data-side="expert"] {--co-side:#a78bfa;}
.co-row:hover {background:rgba(148,163,184,.04);}
.co-name {display:flex;flex-wrap:wrap;align-items:baseline;gap:8px;margin:0;font-size:13.5px;line-height:1.25;color:var(--text);}
.co-id {font-size:9px;font-weight:800;letter-spacing:.07em;color:var(--text-dimmer);border:1px solid var(--border);border-radius:999px;padding:2px 7px;}
.co-flagchip {font-size:9px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--yellow);border:1px solid rgba(245,158,11,.45);border-radius:999px;padding:2px 7px;}
.co-meta {margin:5px 0 0;color:var(--text-dimmer);font-size:10px;}
.co-meta span+span:before {content:" · ";}
.co-desc {margin:8px 0 0;color:var(--text-dim);font-size:11.5px;line-height:1.55;}
.co-note {margin-top:9px;border:1px solid var(--border-subtle);border-radius:var(--r-md);background:var(--surface-2);overflow:hidden;}
.co-note summary {padding:8px 11px;cursor:pointer;list-style:none;color:var(--text-dimmer);font-size:9px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;}
.co-note summary::-webkit-details-marker {display:none;}
.co-note summary:hover {color:var(--accent);}
.co-note[open] summary {border-bottom:1px solid var(--border-subtle);}
.co-note p {margin:0;padding:11px;color:var(--text-dim);font-size:11px;line-height:1.6;white-space:pre-wrap;}
.co-side {display:flex;flex-direction:column;align-items:flex-end;gap:6px;text-align:right;}
.co-role {color:var(--text-dim);font-size:10.5px;line-height:1.45;}
.co-fig {font-size:12px;font-variant-numeric:tabular-nums;color:var(--text);font-weight:700;}
.co-score {font-size:9px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--accent);border:1px solid rgba(96,165,250,.45);border-radius:999px;padding:2px 8px;}
.co-src {color:var(--text-dimmer);font-size:9.5px;}
.co-src:hover {color:var(--accent);text-decoration:underline;}
.co-empty {padding:34px;text-align:center;color:var(--text-dimmer);}
/* HMLV company space map. The visual grammar follows the physical-AI control
   room, while every coordinate is derived from companies.md + contacts.md. */
.cmap {border:1px solid var(--border);border-radius:var(--r-lg);background:var(--surface);padding:18px 20px 20px;overflow:hidden;}
.cmap-head {display:flex;justify-content:space-between;align-items:flex-start;gap:24px;flex-wrap:wrap;}
.cmap-head h2 {font-size:19px;line-height:1.2;margin:6px 0 5px;letter-spacing:-.015em;}
.cmap-head p {max-width:720px;color:var(--text-dim);font-size:11.5px;line-height:1.55;margin:0;}
.cmap-controls {display:flex;justify-content:flex-end;align-items:flex-end;gap:9px;flex-wrap:wrap;}
.cmap-controls label {display:grid;gap:3px;color:var(--text-dimmer);font-size:8.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;}
.cmap-controls select {min-width:190px;max-width:260px;background:var(--surface);color:var(--text);border:1px solid var(--border);border-radius:var(--r-sm);padding:6px 8px;font:inherit;font-size:10px;}
.cmap-controls input {width:100px;accent-color:var(--accent);}
.cmap-lenses {display:flex;padding:3px;border:1px solid var(--border);border-radius:var(--r-md);background:var(--surface-2);}
.cmap-lenses button {border:0;border-radius:var(--r-sm);padding:6px 9px;background:transparent;color:var(--text-dim);font:inherit;font-size:10px;cursor:pointer;}
.cmap-lenses button:hover {color:var(--text);}
.cmap-lenses button.active {background:var(--surface-3);color:var(--accent);}
.cmap-kpis {display:flex;flex-wrap:wrap;gap:18px;margin:15px 0 7px;color:var(--text-dimmer);font-size:9.5px;}
.cmap-kpis span {display:inline-flex;align-items:baseline;gap:5px;}
.cmap-kpis strong {font-size:15px;color:var(--text);font-variant-numeric:tabular-nums;}
.cmap-axis-key {display:flex;gap:8px 22px;flex-wrap:wrap;padding:8px 10px;margin-top:7px;background:var(--surface-2);border-radius:var(--r-md);font-size:9.5px;color:var(--text-dimmer);}
.cmap-axis-key b {color:var(--text);margin-right:5px;}
.cmap-stage {max-width:1220px;margin:0 auto;}
.cmap-stage svg {display:block;width:100%;height:auto;max-height:620px;min-height:430px;cursor:grab;touch-action:none;}
.cmap-stage svg.dragging {cursor:grabbing;}
.cmap-edge,.cmap-gridline {fill:none;stroke:rgba(127,127,127,.29);vector-effect:non-scaling-stroke;}
.cmap-edge {stroke-width:1.15;}.cmap-gridline {stroke-width:.65;opacity:.55;}
.cmap-fence {fill:none;stroke:rgba(127,127,127,.5);stroke-width:1;stroke-dasharray:3 4;vector-effect:non-scaling-stroke;}
.cmap-axis {fill:var(--text-dimmer);font-size:8.5px;font-weight:750;letter-spacing:.075em;}
.cmap-point {cursor:pointer;}.cmap-core {stroke:var(--bg);stroke-width:1.5;vector-effect:non-scaling-stroke;}
.cmap-point.pen-1 .cmap-core,.cmap-dot.pen-1 {fill:#10b981;background:#10b981;}
.cmap-point.pen-2 .cmap-core,.cmap-dot.pen-2 {fill:#38bdf8;background:#38bdf8;}
.cmap-point.pen-3 .cmap-core,.cmap-dot.pen-3 {fill:#a78bfa;background:#a78bfa;}
.cmap-point.pen-4 .cmap-core,.cmap-dot.pen-4 {fill:#f59e0b;background:#f59e0b;}
.cmap-point.pen-5 .cmap-core,.cmap-dot.pen-5 {fill:#64748b;background:#64748b;}
.cmap-point.sells-1 .cmap-core,.cmap-dot.sells-1 {fill:#10b981;background:#10b981;}
.cmap-point.sells-2 .cmap-core,.cmap-dot.sells-2 {fill:#f43f5e;background:#f43f5e;}
.cmap-point.sells-3 .cmap-core,.cmap-dot.sells-3 {fill:#38bdf8;background:#38bdf8;}
.cmap-point.sells-4 .cmap-core,.cmap-dot.sells-4 {fill:#a78bfa;background:#a78bfa;}
.cmap-point.sells-0 .cmap-core,.cmap-dot.sells-0 {fill:#64748b;background:#64748b;}
/* Unknown headcount draws hollow, never small: absence must not read as "tiny". */
.cmap-point.cmap-nohead .cmap-core {fill:none;stroke-dasharray:2.5 2.5;stroke-width:1.4;}
.cmap-point.cmap-nohead.pen-1 .cmap-core {stroke:#10b981;}.cmap-point.cmap-nohead.pen-2 .cmap-core {stroke:#38bdf8;}
.cmap-point.cmap-nohead.pen-3 .cmap-core {stroke:#a78bfa;}.cmap-point.cmap-nohead.pen-4 .cmap-core {stroke:#f59e0b;}
.cmap-point.cmap-nohead.pen-5 .cmap-core {stroke:#64748b;}
.cmap-point.cmap-nohead.sells-1 .cmap-core {stroke:#10b981;}.cmap-point.cmap-nohead.sells-2 .cmap-core {stroke:#f43f5e;}
.cmap-point.cmap-nohead.sells-3 .cmap-core {stroke:#38bdf8;}.cmap-point.cmap-nohead.sells-4 .cmap-core {stroke:#a78bfa;}
.cmap-point.cmap-nohead.sells-0 .cmap-core {stroke:#64748b;}
.cmap-axis-title {fill:var(--text-dim);font-size:9.5px;font-weight:800;letter-spacing:.09em;}
.cmap-contact-ring {fill:none;stroke:var(--text);stroke-width:1;stroke-dasharray:2.5 2.5;opacity:.65;}
.cmap-point.selected .cmap-core {stroke:var(--accent);stroke-width:2.8;}.cmap-point.selected .cmap-contact-ring {stroke:var(--accent);stroke-width:2;stroke-dasharray:none;}
.cmap-point-label {fill:var(--text-dim);font-size:10.5px;font-weight:650;paint-order:stroke;stroke:var(--surface);stroke-width:3px;stroke-linejoin:round;pointer-events:none;}
.cmap-point-label.active {fill:var(--accent);font-weight:800;}
.cmap-readout {display:grid;grid-template-columns:minmax(0,1.35fr) minmax(280px,1fr);gap:18px;margin:2px 10px 10px;padding:11px 13px;border:1px solid var(--border-subtle);border-radius:var(--r-md);background:var(--surface-2);}
.cmap-readout>div:first-child {display:grid;grid-template-columns:max-content max-content;gap:5px 9px;align-items:baseline;}
.cmap-readout strong {font-size:12px;color:var(--text);}.cmap-readout [data-map-state] {font-size:9px;font-weight:800;text-transform:uppercase;letter-spacing:.05em;}
.cmap-readout [data-map-state].pen-1 {color:#10b981}.cmap-readout [data-map-state].pen-2 {color:#38bdf8}.cmap-readout [data-map-state].pen-3 {color:#a78bfa}.cmap-readout [data-map-state].pen-4 {color:#d97706}.cmap-readout [data-map-state].pen-5 {color:var(--text-dimmer)}.cmap-readout [data-map-state].sells-1 {color:#10b981}.cmap-readout [data-map-state].sells-2 {color:#f43f5e}.cmap-readout [data-map-state].sells-3 {color:#38bdf8}.cmap-readout [data-map-state].sells-4 {color:#a78bfa}.cmap-readout [data-map-state].sells-0 {color:var(--text-dimmer)}
.cmap-readout p {grid-column:1/-1;margin:0;color:var(--text-dim);font-size:10.5px;line-height:1.5;}
.cmap-facts {grid-column:1/-1;display:flex;flex-wrap:wrap;gap:5px 12px;margin-top:2px;color:var(--text-dimmer);font-size:9.5px;}
.cmap-facts b {color:var(--text-dim);font-size:inherit;text-transform:none;letter-spacing:0;margin-right:3px;}
.cmap-output {grid-column:1/-1;margin-top:3px;padding-top:8px;border-top:1px solid var(--border-subtle);}
.cmap-output b {display:block;margin-bottom:3px;color:var(--text-dimmer);font-size:8.5px;text-transform:uppercase;letter-spacing:.07em;}
.cmap-output span {color:var(--text-dim);font-size:10.5px;line-height:1.5;}
.cmap-readout [data-map-people] {display:flex;flex-direction:column;gap:3px;color:var(--text-dimmer);font-size:9.5px;max-height:88px;overflow:auto;}
.cmap-readout [data-map-people] b {color:var(--text-dim);font-size:9px;text-transform:uppercase;letter-spacing:.07em;}.cmap-readout [data-map-people] strong {font-size:9.5px;}
.cmap-legend {display:flex;flex-wrap:wrap;gap:7px 15px;margin:0 10px 18px;color:var(--text-dimmer);font-size:9.5px;}
/* Startup scene. Colour is liability_taken on every surface of this tab —
   the belief lives on that axis, so the palette has to answer it at a glance.
   liab-0 unmapped / 1 none / 2 warranty / 3 rework credit / 4 part guarantee /
   5 owns the outcome. Ramped slate -> amber -> emerald: carrying nothing reads
   cold, carrying the outcome reads warm. */
.cmap-point.liab-0 .cmap-core,.cmap-dot.liab-0 {fill:#64748b;background:#64748b;}
.cmap-point.liab-1 .cmap-core,.cmap-dot.liab-1 {fill:#94a3b8;background:#94a3b8;}
.cmap-point.liab-2 .cmap-core,.cmap-dot.liab-2 {fill:#a78bfa;background:#a78bfa;}
.cmap-point.liab-3 .cmap-core,.cmap-dot.liab-3 {fill:#38bdf8;background:#38bdf8;}
.cmap-point.liab-4 .cmap-core,.cmap-dot.liab-4 {fill:#f59e0b;background:#f59e0b;}
.cmap-point.liab-5 .cmap-core,.cmap-dot.liab-5 {fill:#10b981;background:#10b981;}
.cmap-readout [data-map-state].liab-0 {color:var(--text-dimmer)}
.cmap-readout [data-map-state].liab-1 {color:#94a3b8}
.cmap-readout [data-map-state].liab-2 {color:#a78bfa}
.cmap-readout [data-map-state].liab-3 {color:#38bdf8}
.cmap-readout [data-map-state].liab-4 {color:#d97706}
.cmap-readout [data-map-state].liab-5 {color:#10b981}
.smap-claim {border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:var(--r-md);
  background:var(--surface-2);padding:13px 16px;margin:0 0 16px;}
.smap-claim b {display:block;font-size:9px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;
  color:var(--accent);margin-bottom:5px;}
.smap-claim p {margin:0;font-size:12px;line-height:1.6;color:var(--text-dim);max-width:860px;}
.smap-claim em {color:var(--text);font-style:normal;font-weight:650;}
.smap-grid {display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:14px;margin-top:16px;}
.smap-card {border:1px solid var(--border);border-radius:var(--r-md);background:var(--surface);
  padding:14px 15px;display:flex;flex-direction:column;gap:9px;}
.smap-card.is-unresolved {border-style:dashed;}
.smap-card-top {display:flex;justify-content:space-between;align-items:flex-start;gap:10px;}
.smap-card h4 {margin:0;font-size:13.5px;letter-spacing:-.01em;}
.smap-card-sub {color:var(--text-dimmer);font-size:9.5px;margin-top:2px;}
.smap-liab {font-size:8.5px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;
  border-radius:999px;padding:3px 8px;white-space:nowrap;flex-shrink:0;}
.smap-liab.liab-0 {color:#64748b;border:1px solid rgba(100,116,139,.45);}
.smap-liab.liab-1 {color:#94a3b8;border:1px solid rgba(148,163,184,.45);}
.smap-liab.liab-2 {color:#a78bfa;border:1px solid rgba(167,139,250,.45);}
.smap-liab.liab-3 {color:#38bdf8;border:1px solid rgba(56,189,248,.45);}
.smap-liab.liab-4 {color:#d97706;border:1px solid rgba(245,158,11,.5);}
.smap-liab.liab-5 {color:#10b981;border:1px solid rgba(16,185,129,.5);}
.smap-work {margin:0;font-size:11.5px;line-height:1.6;color:var(--text-dim);}
.smap-meta {display:flex;flex-wrap:wrap;gap:5px;}
.smap-meta span {font-size:9px;color:var(--text-dimmer);background:var(--surface-2);
  border-radius:var(--r-sm);padding:3px 7px;}
.smap-meta span b {color:var(--text);font-weight:650;}
.smap-why {margin:0;padding-top:9px;border-top:1px solid var(--border);font-size:11px;
  line-height:1.6;color:var(--text-dim);}
.smap-why b {display:block;font-size:8.5px;font-weight:800;letter-spacing:.07em;
  text-transform:uppercase;color:var(--text-dimmer);margin-bottom:4px;}
.smap-why.is-conflict b {color:#d97706;}
.smap-matrix td a {display:inline-block;border-radius:9px;padding:3px 7px;margin:2px;
  background:rgba(127,127,127,.12);color:var(--text-dim);font-size:9.5px;text-decoration:none;}
.smap-matrix td a:hover {box-shadow:inset 0 0 0 1.5px var(--accent);color:var(--text);}
.smap-note {margin:9px 0 0;font-size:11px;line-height:1.6;color:var(--text-dim);}
.smap-note a {color:var(--text-dim);}
.smap-spaced {margin-top:24px;}
.smap-card:target {box-shadow:0 0 0 2px var(--accent);}
.smap-inspect {border:1px solid var(--border);border-radius:var(--r-md);
  background:var(--surface-2);margin:16px 0 4px;overflow:hidden;}
.smap-inspect-bar {display:flex;justify-content:space-between;align-items:center;gap:12px;
  flex-wrap:wrap;padding:10px 14px;border-bottom:1px solid var(--border);
  background:var(--surface-3);}
.smap-step {display:flex;align-items:center;gap:7px;}
.smap-step button {border:1px solid var(--border);border-radius:var(--r-sm);
  background:var(--surface);color:var(--text-dim);font:inherit;font-size:11px;
  padding:5px 10px;cursor:pointer;}
.smap-step button:hover {color:var(--text);border-color:var(--accent);}
.smap-step select {min-width:210px;background:var(--surface);color:var(--text);
  border:1px solid var(--border);border-radius:var(--r-sm);padding:6px 8px;
  font:inherit;font-size:11px;}
.smap-step-count {color:var(--text-dimmer);font-size:9.5px;font-variant-numeric:tabular-nums;}
.smap-inspect-body {padding:15px 16px 17px;}
.smap-inspect-head {display:flex;justify-content:space-between;align-items:flex-start;
  gap:12px;flex-wrap:wrap;margin-bottom:11px;}
.smap-inspect-head h4 {margin:0;font-size:17px;letter-spacing:-.015em;}
.smap-inspect-head .smap-card-sub {margin-top:3px;}
/* Exactly 5 columns for the 10 declared facts, so the grid always fills whole
   rows. auto-fit left a ragged tail that read as an unfinished row. */
.smap-facts {display:grid;grid-template-columns:repeat(5,1fr);
  gap:1px;background:var(--border);border:1px solid var(--border);
  border-radius:var(--r-sm);overflow:hidden;margin-bottom:13px;}
@media (max-width:900px) {.smap-facts {grid-template-columns:repeat(2,1fr);}}
.smap-facts div {background:var(--surface);padding:8px 10px;}
.smap-facts dt {color:var(--text-dimmer);font-size:8.5px;font-weight:800;
  letter-spacing:.07em;text-transform:uppercase;margin-bottom:3px;}
.smap-facts dd {margin:0;color:var(--text);font-size:12px;font-variant-numeric:tabular-nums;}
.smap-facts dd small {display:block;color:var(--text-dimmer);font-size:9px;
  font-variant-numeric:normal;margin-top:2px;}
.smap-facts dd.is-blank {color:var(--text-dimmer);}
.smap-services {margin:0 0 13px;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:5px;}
.smap-services li {font-size:10.5px;color:var(--text-dim);background:var(--surface);
  border:1px solid var(--border);border-radius:999px;padding:4px 10px;}
.smap-sub {font-size:8.5px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;
  color:var(--text-dimmer);margin:0 0 6px;}
.smap-srcline {margin:11px 0 0;padding-top:10px;border-top:1px solid var(--border);
  font-size:9.5px;line-height:1.6;color:var(--text-dimmer);word-break:break-word;}
.cmap-point.is-active .cmap-core {stroke:var(--accent);stroke-width:2.5;}
.smap-bars {display:grid;gap:5px;margin-top:6px;}
.smap-bar {display:grid;grid-template-columns:150px 1fr 124px;align-items:center;gap:9px;font-size:10px;}
.smap-bar-name {color:var(--text-dim);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.smap-bar-track {height:9px;border-radius:999px;background:var(--surface-2);overflow:hidden;}
.smap-bar-fill {height:100%;border-radius:999px;}
.smap-bar-val {color:var(--text-dimmer);font-variant-numeric:tabular-nums;text-align:right;}
.smap-bar.is-undisclosed .smap-bar-track {background:repeating-linear-gradient(
  90deg,var(--surface-2) 0 5px,transparent 5px 10px);}
.cmap-legend span {display:inline-flex;align-items:center;gap:5px;}.cmap-dot {display:inline-block;width:8px;height:8px;border-radius:50%;}.cmap-ring {display:inline-block;width:11px;height:11px;border:1px dashed var(--text);border-radius:50%;}.cmap-hollow {display:inline-block;width:9px;height:9px;border:1.4px dashed var(--text-dimmer);border-radius:50%;}
.cmap-matrix-head {margin-top:7px;}.cmap-matrix-head h3 {font-size:12px;margin:0 0 3px;}.cmap-matrix-head p {font-size:10.5px;color:var(--text-dimmer);margin:0 0 9px;}
.cmap-matrix {overflow-x:auto;border:1px solid var(--border);border-radius:var(--r-md);}
.cmap-matrix table {width:100%;min-width:840px;border-collapse:separate;border-spacing:2px;background:var(--surface);}
.cmap-matrix th {padding:8px 9px;color:var(--text-dimmer);font-size:9px;text-transform:uppercase;letter-spacing:.06em;text-align:left;vertical-align:top;}.cmap-matrix thead th:not(:first-child) {text-align:center;}.cmap-matrix th small {display:block;font-size:8px;font-weight:500;letter-spacing:0;text-transform:none;margin-top:2px;}
.cmap-matrix td {width:18%;padding:6px;background:var(--surface-2);vertical-align:top;}.cmap-matrix td button {display:inline-block;border:0;border-radius:9px;padding:3px 7px;margin:2px;background:rgba(127,127,127,.12);color:var(--text-dim);font:inherit;font-size:9.5px;cursor:pointer;text-align:left;}.cmap-matrix td button:hover {box-shadow:inset 0 0 0 1.5px var(--accent);color:var(--text);}.cmap-matrix td button b {display:inline-block;margin-left:3px;color:var(--accent);font-size:8.5px;}
@media (max-width:800px) {
  .co-row {grid-template-columns:minmax(0,1fr);}
  .co-side {align-items:flex-start;text-align:left;}
  .cmap {padding:14px 10px;}.cmap-controls,.cmap-lenses,.cmap-controls label {width:100%;}.cmap-lenses button {flex:1;}.cmap-controls select {width:100%;max-width:none;}.cmap-stage svg {min-height:330px;}.cmap-axis {font-size:7px;}.cmap-readout {grid-template-columns:1fr;margin-inline:2px;}.cmap-axis-key {display:grid;gap:5px;}
}
"""

# tier_side is global vocabulary (schemas/vocabularies.yaml); tier NAMES are
# per-idea and declared in graph.md, so the grouping here keys on the side only.
_CO_SIDE_ORDER = ["demand", "supply", "competitor", "expert", ""]
_CO_SIDE_LABEL = {
    "demand": "Demand side — the people who would buy",
    "supply": "Supply side",
    "competitor": "Competitors",
    "expert": "Experts and research partners",
    "": "Unassigned side",
}


def parse_companies_md(path: Path) -> tuple[dict, list[dict]]:
    """
    Return (frontmatter, companies) from `outreach/companies.md`.

    Company blocks are `## Name` headings whose body is plain (unfenced) YAML —
    the shape `startup-outreach-intel` writes. Any block that is prose rather
    than a mapping, or that carries no `id:`, is skipped rather than warned
    about: a `## Provenance` or `## Run summary` section is a normal part of the
    file, not a malformed company.
    """
    if not path.exists() or not _HAS_YAML:
        return {}, []
    text = path.read_text(encoding="utf-8")
    fm: dict = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            try:
                fm = yaml.safe_load(text[3:end]) or {}
            except yaml.YAMLError:
                fm = {}
            text = text[end + 4:]

    companies: list[dict] = []
    for chunk in re.split(r"(?m)^## ", text)[1:]:
        head, _, body = chunk.partition("\n")
        try:
            data = yaml.safe_load(body)
        except yaml.YAMLError:
            continue
        if not isinstance(data, dict) or not data.get("id"):
            continue
        data["_heading"] = head.strip()
        companies.append(data)
    return fm, companies


def _co_suffix(data: dict, suffix: str):
    """First value whose key ends in `suffix`. Keeps the renderer idea-agnostic —
    `unimaas_role` and `hmlv_relevance` are this idea's field names, not schema."""
    for k, v in data.items():
        if k.endswith(suffix) and v not in (None, "", []):
            return v
    return None


def _co_money(v) -> str:
    try:
        return "&euro;{:,}".format(int(v))
    except (TypeError, ValueError):
        return escape(str(v))


_ORG_SUFFIX_RE = re.compile(
    r"\b(?:incorporated|corporation|company|limited|holdings?|technologies|technology|"
    r"systems?|group|plc|llc|ltd|inc|corp|gmbh|ag|sa|as)\b", re.I)


def _org_key(value) -> str:
    """Loose organization key used only to join company cards to contact cards.

    The original strings remain visible. This key is intentionally conservative:
    it removes legal suffixes and parenthetical site notes, but does not fuzzy-match
    unrelated names.
    """
    value = re.sub(r"\([^)]*\)", " ", str(value or ""))
    value = value.replace("&", " and ")
    value = _ORG_SUFFIX_RE.sub(" ", value)
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def _is_real_contact_company(value) -> bool:
    raw = str(value or "").strip()
    if not raw or raw.startswith("("):
        return False
    lowered = raw.lower()
    return not any(token in lowered for token in (
        "between roles", "company on profile", "own shop", "verify on enrichment",
    ))


def _contact_access(contacts: list[dict]) -> tuple[int, str]:
    """Return access friction and the strongest relationship state.

    This is deliberately a relationship score, not a commercial attractiveness
    score. A completed interview opens a door; it does not prove the company buys.
    """
    if not contacts:
        return 5, "no mapped person"
    if any(c.get("interview_date") or c.get("interviews") or
           str(c.get("call_stage") or "").lower() == "completed" or
           str(c.get("outreach_status") or "").lower() == "interviewed"
           for c in contacts):
        return 1, "interview completed"
    if any(str(c.get("outreach_status") or "").lower() in
           {"replied", "scheduled", "done", "questions_by_email"} or
           str(c.get("call_stage") or "").lower() in
           {"offered_by_contact", "asked_by_founder", "scheduled"}
           for c in contacts):
        return 2, "active conversation"
    if any(str(c.get("outreach_status") or "").lower() == "accepted" or
           normalize_degree(c.get("degree", "")) == "1st" for c in contacts):
        return 3, "connected person"
    if any(str(c.get("outreach_status") or "").lower() in
           CONTACTED_STATUSES | {"invited", "email_drafted", "email_sent"}
           for c in contacts):
        return 4, "outreach path"
    return 4, "named person"


# ── Company space map ────────────────────────────────────────────────────────
# Every coordinate below reads a DECLARED field on the company entry. Nothing is
# inferred from prose and nothing is jittered: a company not yet mapped on an
# axis renders in that axis's explicit "unmapped" lane, never at the low end of a
# real scale. Axis vocabularies are per-idea and declared in the frontmatter of
# `outreach/companies.md` (`map_vocabularies:`) — never here, never in schemas/.

_MAP_AXES_FALLBACK = {
    "chain_position": ["oem", "tier1", "tier2", "tier3"],
    "proveout_exposure": ["none", "low", "medium", "high"],
    "integration": ["software_only", "software_plus_service", "equipment",
                    "operates_machines", "owns_factory"],
    "job_covered": ["quoting", "cam_programming", "program_verification",
                    "setup_workholding", "machine_execution", "inspection_qa",
                    "scheduling_ops"],
    "sells_to": ["shop", "oem_buyer", "machine_builder", "none_yet"],
    "liability_taken": ["none", "warranty", "rework_credit", "part_guarantee",
                        "owns_outcome"],
    "touches_proveout": ["none", "adjacent", "direct"],
    "stage": ["pre_seed", "seed", "series_a", "series_b", "series_c",
              "series_d_plus", "public", "incumbent_subsidiary"],
}

_MAP_AXIS_LABEL = {
    "chain_position": {"oem": "OEM", "tier1": "Tier 1", "tier2": "Tier 2",
                       "tier3": "Tier 3"},
    "proveout_exposure": {"none": "none stated", "low": "low", "medium": "medium",
                          "high": "high"},
    "integration": {"software_only": "software only",
                    "software_plus_service": "software + service",
                    "equipment": "equipment", "operates_machines": "operates machines",
                    "owns_factory": "owns factory"},
    "job_covered": {"quoting": "quoting", "cam_programming": "CAM programming",
                    "program_verification": "program verification",
                    "setup_workholding": "setup / workholding",
                    "machine_execution": "machine execution",
                    "inspection_qa": "inspection / QA",
                    "scheduling_ops": "scheduling / ops"},
    "sells_to": {"shop": "sells to the shop", "oem_buyer": "sells to the OEM buyer",
                 "machine_builder": "sells to machine builders",
                 "none_yet": "no customers yet"},
    "liability_taken": {"none": "carries none",
                        "warranty": "software warranty",
                        "rework_credit": "rework credit",
                        "part_guarantee": "guarantees the part",
                        "owns_outcome": "owns the outcome"},
    "touches_proveout": {"none": "does not touch prove-out",
                         "adjacent": "adjacent to prove-out",
                         "direct": "in the prove-out job"},
    "stage": {"pre_seed": "pre-seed", "seed": "seed", "series_a": "Series A",
              "series_b": "Series B", "series_c": "Series C",
              "series_d_plus": "Series D+", "public": "public",
              "incumbent_subsidiary": "incumbent subsidiary"},
}

# Revenue per employee. The band, not the number, is what gets plotted: for a
# private machine shop the underlying figure is usually an estimate, and a
# continuous axis would render that estimate as a measurement.
_RPE_BANDS = [
    (120_000, "under $120k / head"),
    (200_000, "$120k–200k / head"),
    (300_000, "$200k–300k / head"),
    (float("inf"), "over $300k / head"),
]

_UNMAPPED = "not mapped"

# Unmapped sits in a reserved gutter at the origin end of every axis, with the real
# scale starting past it. Keeping it ON the canvas but visibly fenced off is the
# point: absence has to be as legible as a value, and it must not be clipped.
_GUTTER = 0.16


def _map_vocab(fm: dict) -> dict:
    """Declared axis vocabularies, falling back to the shape this renderer expects.

    A value present on an entry but absent from the declared list is NOT silently
    placed: it lands in the unmapped lane and is counted in the coverage KPI, so a
    typo shows up as missing data rather than as a new position on the map.
    """
    declared = fm.get("map_vocabularies") if isinstance(fm, dict) else None
    vocab = dict(_MAP_AXES_FALLBACK)
    if isinstance(declared, dict):
        for axis, values in declared.items():
            if isinstance(values, list) and values:
                vocab[axis] = [str(v) for v in values]
    return vocab


def _axis_slot(value, ordered: list[str]) -> tuple[int, str, float]:
    """Position on an ordered categorical axis.

    Returns (code, label, coordinate). Code 0 is reserved for unmapped and gets a
    lane of its own at the far end, visually separated from the real values.
    """
    raw = str(value or "").strip()
    if raw and raw in ordered:
        i = ordered.index(raw)
        span = max(len(ordered) - 1, 1)
        return i + 1, raw, _GUTTER + (i / span) * (1 - _GUTTER)
    return 0, _UNMAPPED, 0.0


def _labelled(axis: str, value: str) -> str:
    return _MAP_AXIS_LABEL.get(axis, {}).get(value, value)


def _company_headcount(c: dict) -> tuple[int | None, str]:
    """Declared headcount only. No estimate is derived from prose or floor area."""
    raw = c.get("headcount")
    if isinstance(raw, (int, float)) and raw > 0:
        return int(raw), str(c.get("headcount_source") or "unstated")
    if isinstance(raw, str):
        nums = [int(n.replace(",", "")) for n in re.findall(r"\d[\d,]*", raw)]
        if nums:
            return max(nums), str(c.get("headcount_source") or "unstated")
    return None, ""


def _revenue_per_head(c: dict) -> tuple[int, str, float, str]:
    """Revenue per employee, banded. The Z axis of the client map.

    Both inputs must be declared. Revenue alone or headcount alone yields nothing:
    a half-known ratio is a guess wearing a number's clothes.
    """
    head, _ = _company_headcount(c)
    rev = c.get("revenue_usd")
    if isinstance(rev, str):
        nums = [int(n.replace(",", "")) for n in re.findall(r"\d[\d,]*", rev)]
        rev = max(nums) if nums else None
    source = str(c.get("revenue_source") or "unknown")
    if not head or not isinstance(rev, (int, float)) or rev <= 0:
        return 0, _UNMAPPED, -0.12, source
    rpe = rev / head
    for i, (ceiling, label) in enumerate(_RPE_BANDS):
        if rpe < ceiling:
            span = max(len(_RPE_BANDS) - 1, 1)
            return i + 1, f"{label} ({source})", _GUTTER + (i / span) * (1 - _GUTTER), source
    return 0, _UNMAPPED, 0.0, source


def _raised(c: dict) -> tuple[int | None, str, str]:
    """Total raised, its display label and its provenance.

    Returns (usd, label, source). A blank field is missing data and stays blank:
    a public incumbent and an unfunded startup both have no venture total, and
    rendering either as $0 would put them in the same lane as a pre-seed.
    """
    raw = c.get("total_raised_usd")
    source = str(c.get("funding_source") or "unknown")
    if isinstance(raw, str):
        digits = re.sub(r"[^0-9]", "", raw)
        raw = int(digits) if digits else None
    if not isinstance(raw, (int, float)) or raw <= 0:
        return None, "not disclosed", source
    usd = int(raw)
    if usd >= 1_000_000_000:
        label = f"${usd / 1_000_000_000:.2f}".rstrip("0").rstrip(".") + "B"
    else:
        label = f"${usd / 1_000_000:.1f}".rstrip("0").rstrip(".") + "M"
    return usd, f"{label} ({source})", source


def _startup_fields(c: dict, vocab: dict) -> dict:
    """The startup map's own columns, all read from declared fields.

    `liability_taken` is the belief's axis and therefore the colour: the claim
    under test is that the prove-out job is served only by companies carrying no
    first-run risk, so an unfilled field must read as unknown rather than as none.
    """
    liab_code, liab_raw, _ = _axis_slot(c.get("liability_taken"), vocab["liability_taken"])
    prov_code, prov_raw, _ = _axis_slot(c.get("touches_proveout"), vocab["touches_proveout"])
    stage_code, stage_raw, _ = _axis_slot(c.get("stage"), vocab["stage"])
    usd, raised_label, funding_source = _raised(c)
    return {
        "liabCode": liab_code,
        "liabLabel": _labelled("liability_taken", liab_raw) if liab_code else _UNMAPPED,
        "proveoutCode": prov_code,
        "proveoutLabel": _labelled("touches_proveout", prov_raw) if prov_code else _UNMAPPED,
        "stageCode": stage_code,
        "stageLabel": _labelled("stage", stage_raw) if stage_code else _UNMAPPED,
        "raised": usd,
        "raisedLabel": raised_label,
        "fundingSource": funding_source,
        "founded": str(c.get("founded") or ""),
        "fundingNotes": str(c.get("funding_notes") or ""),
        "liabNotes": str(c.get("liability_notes") or ""),
        "relevance": _co_suffix(c, "_relevance") or "",
        "conflict": str(c.get("identity_conflict") or ""),
        "sourceUrl": str(c.get("source_url") or ""),
        "sources": str(c.get("sources") or ""),
        "entryStatus": str(c.get("status") or ""),
        "services": [str(s) for s in (c.get("services") or []) if s],
        "headcountNote": str(c.get("headcount_note") or ""),
    }


def _map_side(c: dict) -> str:
    """Which map an entry belongs on. An explicit `map:` field always wins."""
    declared = str(c.get("map") or "").strip().lower()
    if declared in {"client", "startup", "none"}:
        return declared
    side = str(c.get("tier_side") or "").strip().lower()
    if side == "demand":
        return "client"
    if side in {"competitor", "supply"}:
        return "startup"
    return "none"


def _company_map_entities(fm: dict, companies: list[dict],
                          contacts: list[dict]) -> list[dict]:
    vocab = _map_vocab(fm)
    records = [dict(c) for c in companies]
    aliases: dict[str, int] = {}
    for i, c in enumerate(records):
        values = [c.get("_heading"), c.get("company"), c.get("canonical_name")]
        values.extend(c.get("also_known_as") or [])
        for value in values:
            key = _org_key(value)
            if key:
                aliases.setdefault(key, i)

    grouped: list[list[dict]] = [[] for _ in records]
    unmatched: dict[str, list[dict]] = {}
    unmatched_names: dict[str, str] = {}
    for contact in contacts:
        company = contact.get("company")
        if not _is_real_contact_company(company):
            continue
        key = _org_key(company)
        idx = aliases.get(key)
        if idx is not None:
            grouped[idx].append(contact)
        elif key:
            unmatched.setdefault(key, []).append(contact)
            unmatched_names.setdefault(key, str(company).strip())

    for key, people in unmatched.items():
        records.append({
            "id": f"CONTACT-{len(records) + 1}",
            "_heading": unmatched_names[key],
            "canonical_name": unmatched_names[key],
            "sector": "Contact employer — company registry enrichment pending",
            "mapping_source": "contact_only",
            "tier_side": "demand",
        })
        grouped.append(people)

    out = []
    for c, people in zip(records, grouped):
        side = _map_side(c)
        if side == "none":
            continue
        barrier, access_label = _contact_access(people)
        head, head_source = _company_headcount(c)
        name = str(c.get("_heading") or c.get("company") or c.get("canonical_name") or "?")
        missing: list[str] = []

        startup: dict = {}
        if side == "client":
            x_code, _x_raw, x = _axis_slot(c.get("chain_position"), vocab["chain_position"])
            x_label = (_labelled("chain_position", str(c.get("chain_position") or ""))
                       if x_code else _UNMAPPED)
            y_code, _y_raw, y = _axis_slot(c.get("proveout_exposure"), vocab["proveout_exposure"])
            y_label = (_labelled("proveout_exposure", str(c.get("proveout_exposure") or ""))
                       if y_code else _UNMAPPED)
            z_code, z_label, z, _rev_source = _revenue_per_head(c)
            colour = f"pen-{barrier}"
            if not x_code:
                missing.append("chain position")
            if not y_code:
                missing.append("prove-out exposure")
            if not z_code:
                missing.append("revenue per head")
        else:
            x_code, _x_raw, x = _axis_slot(c.get("job_covered"), vocab["job_covered"])
            x_label = (_labelled("job_covered", str(c.get("job_covered") or ""))
                       if x_code else _UNMAPPED)
            y_code, _y_raw, y = _axis_slot(c.get("integration"), vocab["integration"])
            y_label = (_labelled("integration", str(c.get("integration") or ""))
                       if y_code else _UNMAPPED)
            sells_code, _s_raw, _s = _axis_slot(c.get("sells_to"), vocab["sells_to"])
            z_code, z_label, z = 0, "", 0.0
            startup = _startup_fields(c, vocab)
            # Colour is liability, not customer: the belief lives on that axis, so
            # it is the one thing a glance at the map has to answer.
            colour = f"liab-{startup['liabCode']}"
            if not x_code:
                missing.append("job covered")
            if not y_code:
                missing.append("integration")
            if not sells_code:
                missing.append("who they sell to")
            if not startup["liabCode"]:
                missing.append("liability taken")
            if not startup["stageCode"]:
                missing.append("stage")
        if head is None:
            missing.append("headcount")

        out.append({
            "id": str(c.get("id") or ""), "name": name, "map": side,
            "x": x, "xCode": x_code, "xLabel": x_label,
            "y": y, "yCode": y_code, "yLabel": y_label,
            "z": z, "zCode": z_code, "zLabel": z_label,
            "colour": colour, "barrier": barrier, "accessLabel": access_label,
            "headcount": head, "headcountSource": head_source,
            "sellsTo": _labelled("sells_to", str(c.get("sells_to") or "")) if side == "startup" else "",
            "country": str(c.get("country") or ""),
            "sector": str(c.get("sector") or ""),
            "tier": str(c.get("tier") or ""),
            "missing": missing,
            "description": str(c.get("makes_or_does") or c.get("hmlv_relevance") or ""),
            "contactOnly": c.get("mapping_source") == "contact_only",
            **(startup if side == "startup" else {}),
            "contacts": [{
                "id": str(p.get("id") or ""),
                "name": str(p.get("name") or p.get("_heading") or ""),
                "role": str(p.get("role") or ""),
                "status": str(p.get("outreach_status") or "pending"),
                "interviewed": bool(p.get("interview_date") or p.get("interviews")),
            } for p in people],
        })
    return out


def render_company_space_map(fm: dict, companies: list[dict],
                             contacts: list[dict]) -> str:
    entities = _company_map_entities(fm, companies, contacts)
    data_json = json.dumps(entities, ensure_ascii=True).replace("</", "<\\/")
    template = r'''
<section class="cmap" id="company-space-map" aria-labelledby="cmap-title">
  <div class="cmap-head">
    <div>
      <div class="co-eyebrow">Client space map</div>
      <h2 id="cmap-title">Where the demand side sits</h2>
      <p>Clients by supply-chain position and prove-out exposure, with revenue per employee as depth and colour carrying how far into the company we have actually got. Every position reads a declared field &mdash; unmapped companies stand in their own lane rather than being guessed onto the scale. The supply side moved to its own <strong>Startups</strong> tab on 2026-08-27: two populations that share no axis do not belong behind one toggle.</p>
    </div>
    <div class="cmap-controls">
      <div class="cmap-lenses" role="group" aria-label="Dimensions" data-map-dimgroup>
        <button type="button" data-map-dim="3d" aria-pressed="false">3D</button>
        <button type="button" class="active" data-map-dim="2d" aria-pressed="true">2D</button>
      </div>
      <label>Inspect company<select data-map-company aria-label="Inspect company"></select></label>
      <label data-map-rotwrap>Rotate<input data-map-rotation type="range" min="-105" max="-20" value="-44" aria-label="Rotate 3D company map"></label>
    </div>
  </div>
  <div class="cmap-kpis" data-map-kpis></div>
  <div class="cmap-axis-key" data-map-axis-key></div>
  <div class="cmap-stage">
    <svg viewBox="0 0 1100 620" role="img" aria-labelledby="cmap-svg-title cmap-svg-desc">
      <title id="cmap-svg-title">Company space map</title>
      <desc id="cmap-svg-desc">Clients positioned by supply-chain position, prove-out exposure and revenue per employee.</desc>
      <g data-map-layer="grid"></g><g data-map-layer="points"></g><g data-map-layer="labels"></g>
    </svg>
  </div>
  <div class="cmap-readout" aria-live="polite">
    <div><strong data-map-name></strong><span data-map-state></span><p data-map-detail></p><div class="cmap-facts" data-map-facts></div><div class="cmap-output" data-map-output></div></div>
    <div data-map-people></div>
  </div>
  <div class="cmap-legend" data-map-legend></div>
  <div class="cmap-matrix-head"><h3 data-map-matrix-title></h3><p data-map-matrix-note></p></div>
  <div class="cmap-matrix" data-map-matrix></div>
</section>
<script>
(() => {
  const root = document.getElementById('company-space-map');
  if (!root || root.dataset.ready) return;
  root.dataset.ready = 'true';
  const all = __DATA__;
  const ns = 'http://www.w3.org/2000/svg';
  const svg = root.querySelector('svg');
  const grid = root.querySelector('[data-map-layer="grid"]');
  const points = root.querySelector('[data-map-layer="points"]');
  const labels = root.querySelector('[data-map-layer="labels"]');
  const select = root.querySelector('[data-map-company]');
  const rotation = root.querySelector('[data-map-rotation]');
  const rotwrap = root.querySelector('[data-map-rotwrap]');
  const dimGroup = root.querySelector('[data-map-dimgroup]');
  const matrix = root.querySelector('[data-map-matrix]');
  // 2D is the default view. The client map carries four facts without depth
  // (two axes, dot size, colour); 3D lifts revenue per head out of colour-free
  // space, and collapsing back never loses penetration, which lives in colour.
  const lens = 'client';  // startups render in their own tab, not behind a toggle
  let dim = '2d', selected = null;
  let yaw = Number(rotation.value) * Math.PI / 180, dragging = false, lastX = 0;
  const GUTTER = 0.16;  // matches _GUTTER in the generator
  const meta = {
    client: {x:'Supply-chain position', y:'Prove-out exposure', z:'Revenue per employee'},
    startup:{x:'Job covered', y:'Vertical integration: licence to owned factory', z:''}
  };
  const penLegend='<span><i class="cmap-dot pen-1"></i>interview completed</span><span><i class="cmap-dot pen-2"></i>active conversation</span><span><i class="cmap-dot pen-3"></i>connected person</span><span><i class="cmap-dot pen-4"></i>outreach path</span><span><i class="cmap-dot pen-5"></i>no mapped person</span><span><i class="cmap-ring"></i>contact-only, registry enrichment pending</span><span><i class="cmap-hollow"></i>headcount unknown</span>';
  const sellsLegend='<span><i class="cmap-dot sells-1"></i>sells to the shop</span><span><i class="cmap-dot sells-2"></i>sells to the OEM buyer</span><span><i class="cmap-dot sells-3"></i>sells to machine builders</span><span><i class="cmap-dot sells-4"></i>no customers yet</span><span><i class="cmap-dot sells-0"></i>not mapped</span><span><i class="cmap-hollow"></i>headcount unknown</span>';
  function node(tag, attrs={}) { const n=document.createElementNS(ns,tag); Object.entries(attrs).forEach(([k,v])=>n.setAttribute(k,String(v))); return n; }
  function current() { return all.filter(c=>c.map===lens); }
  function is3d() { return dim==='3d' && lens==='client'; }
  function project(x,y,z) {
    if (!is3d()) return {x:130+x*840,y:540-y*450,depth:0,scale:1};
    const px=(x-.5)*2, py=(y-.5)*2, pz=z*1.76;
    const rx=px*Math.cos(yaw)-py*Math.sin(yaw), depth=px*Math.sin(yaw)+py*Math.cos(yaw);
    return {x:550+rx*268,y:532-pz*244+depth*94,depth,scale:1+depth*.10};
  }
  // Dot area, not radius, tracks headcount — a 10x company should read as 10x
  // ink, not 100x. Unknown headcount draws hollow instead of small.
  function radius(c,scale) { const base=c.headcount?Math.min(15,4+Math.sqrt(c.headcount)*.42):5.5; return base*scale; }
  function line(a,b,cls='cmap-edge') { const p=project(...a),q=project(...b); grid.appendChild(node('line',{x1:p.x,y1:p.y,x2:q.x,y2:q.y,class:cls})); }
  function textAt(p,value,cls,anchor='middle',dx=0,dy=0) { const t=node('text',{x:p.x+dx,y:p.y+dy,class:cls,'text-anchor':anchor}); t.textContent=value; labels.appendChild(t); }
  function drawGrid() {
    grid.replaceChildren(); labels.replaceChildren();
    if (is3d()) {
      const corners=[[0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,1],[1,0,1],[1,1,1],[0,1,1]];
      [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]].forEach(e=>line(corners[e[0]],corners[e[1]]));
      [.25,.5,.75].forEach(n=>{line([n,0,0],[n,1,0],'cmap-gridline');line([0,n,0],[1,n,0],'cmap-gridline');line([0,0,n],[1,0,n],'cmap-gridline');});
      textAt(project(.5,-.08,0),meta[lens].x.toUpperCase(),'cmap-axis');
      textAt(project(-.12,.5,0),meta[lens].y.toUpperCase(),'cmap-axis');
      textAt(project(0,0,1.10),meta[lens].z.toUpperCase(),'cmap-axis','start',-4,-3);
      return;
    }
    line([0,0,0],[1,0,0],'cmap-gridline'); line([0,0,0],[0,1,0],'cmap-gridline');
    [.4,.6,.8,1].forEach(n=>{line([n,0,0],[n,1,0],'cmap-gridline');line([0,n,0],[1,n,0],'cmap-gridline');});
    line([GUTTER,0,0],[GUTTER,1,0],'cmap-fence'); line([0,GUTTER,0],[1,GUTTER,0],'cmap-fence');
    lanesFor('x').forEach(l=>textAt(project(l.at,-.05,0),l.label.toUpperCase(),'cmap-axis'));
    lanesFor('y').forEach(l=>textAt(project(-.012,l.at,0),l.label.toUpperCase(),'cmap-axis','end',-6,3));
    textAt(project(.5,-.13,0),meta[lens].x.toUpperCase(),'cmap-axis-title');
  }
  // Lanes come from the data, so an axis grows when the registry declares a new
  // value — the map forms as companies go in, rather than against a fixed enum.
  function lanesFor(axis) {
    const seen=new Map();
    current().forEach(c=>{const at=axis==='x'?c.x:c.y, label=axis==='x'?c.xLabel:c.yLabel; if(!seen.has(label)) seen.set(label,at);});
    return [...seen].map(([label,at])=>({label,at})).sort((a,b)=>a.at-b.at);
  }
  function esc(v){return String(v||'').replace(/[&<>"']/g,ch=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));}
  function detail(c) {
    const base=[c.sector,c.country].filter(Boolean).join(' | ');
    return base+(c.missing.length?(base?' | ':'')+'Missing: '+c.missing.join(', '):'');
  }
  function show(c) {
    // An empty lens must CLEAR the stage. Returning early here left the previous
    // lens's dots and readout on screen, which read as "these are startups".
    if (!c) {
      selected=null; select.value='';
      root.querySelector('[data-map-name]').textContent='Nothing on this map yet';
      const st=root.querySelector('[data-map-state]'); st.textContent=''; st.className='';
      root.querySelector('[data-map-detail]').textContent='No entry carries map: client yet.';
      root.querySelector('[data-map-facts]').innerHTML='';
      root.querySelector('[data-map-output]').innerHTML='';
      root.querySelector('[data-map-people]').innerHTML='';
      draw(); return;
    }
    selected=c; select.value=c.name;
    root.querySelector('[data-map-name]').textContent=c.name;
    const state=root.querySelector('[data-map-state]');
    state.textContent=lens==='client'?c.accessLabel:(c.sellsTo||'not mapped');
    state.className=c.colour;
    root.querySelector('[data-map-detail]').textContent=detail(c);
    const head=c.headcount?esc(c.headcount)+' people'+(c.headcountSource?' ('+esc(c.headcountSource)+')':''):'headcount unknown';
    root.querySelector('[data-map-facts]').innerHTML=lens==='client'
      ?'<span><b>Chain</b>'+esc(c.xLabel)+'</span><span><b>Prove-out exposure</b>'+esc(c.yLabel)+'</span><span><b>Revenue / head</b>'+esc(c.zLabel)+'</span><span><b>Size</b>'+head+'</span><span><b>Penetration</b>'+esc(c.accessLabel)+'</span>'
      :'<span><b>Job covered</b>'+esc(c.xLabel)+'</span><span><b>Integration</b>'+esc(c.yLabel)+'</span><span><b>Sells to</b>'+esc(c.sellsTo||'not mapped')+'</span><span><b>Size</b>'+head+'</span>';
    root.querySelector('[data-map-output]').innerHTML='<b>What they make or do</b><span>'+esc(c.description||'Not mapped yet.')+'</span>';
    const people=root.querySelector('[data-map-people]');
    people.innerHTML=c.contacts.length?'<b>People mapped</b>'+c.contacts.map(p=>'<span><strong>'+esc(p.name)+'</strong>'+esc(p.role?' | '+p.role:'')+' | '+esc(p.status)+(p.interviewed?' | interviewed':'')+'</span>').join(''):'<b>No people mapped</b><span>No contact card matches this company yet.</span>';
    draw();
  }
  // Categorical axes put many companies in one cell, so each cell is packed as a
  // deterministic grid ordered by name. This is a LAYOUT within a cell, not a
  // coordinate: every dot in a cell shares the same declared position, and the
  // packing is stable across rebuilds so a dot does not wander between renders.
  function packCells(rows) {
    const cells=new Map();
    rows.forEach(c=>{const k=c.xLabel+'|'+c.yLabel+'|'+c.zLabel; if(!cells.has(k))cells.set(k,[]); cells.get(k).push(c);});
    const pos=new Map();
    cells.forEach(list=>{
      list.sort((a,b)=>a.name.localeCompare(b.name));
      const n=list.length, cols=Math.max(1,Math.ceil(Math.sqrt(n))), step=15, rowsN=Math.ceil(n/cols);
      list.forEach((c,i)=>pos.set(c,{dx:((i%cols)-(cols-1)/2)*step, dy:(Math.floor(i/cols)-(rowsN-1)/2)*step}));
    });
    return pos;
  }
  function draw() {
    drawGrid(); points.replaceChildren();
    const rows=current().slice().sort((a,b)=>project(a.x,a.y,a.z).depth-project(b.x,b.y,b.z).depth);
    const pack=packCells(rows);
    rows.forEach(c=>{
      const proj=project(c.x,c.y,c.z), off=pack.get(c)||{dx:0,dy:0};
      const p={x:proj.x+off.dx*proj.scale, y:proj.y+off.dy*proj.scale, depth:proj.depth, scale:proj.scale};
      const g=node('g',{class:'cmap-point '+c.colour+(selected===c?' selected':'')+(c.headcount?'':' cmap-nohead')});
      if(c.contactOnly) g.appendChild(node('circle',{cx:p.x,cy:p.y,r:radius(c,p.scale)+5,class:'cmap-contact-ring'}));
      g.appendChild(node('circle',{cx:p.x,cy:p.y,r:radius(c,p.scale),class:'cmap-core'}));
      g.addEventListener('click',()=>show(c)); points.appendChild(g);
      if(selected===c||(lens==='client'&&c.barrier<=2)){const t=node('text',{x:p.x+radius(c,p.scale)+4,y:p.y-7,class:'cmap-point-label'+(selected===c?' active':'')});t.textContent=c.name;labels.appendChild(t);}
    });
  }
  function renderMatrix(){
    const rows=current();
    const laneOf=c=>c.xLabel, colOf=c=>lens==='client'?c.accessLabel:c.yLabel;
    const lanes=[...new Set(rows.slice().sort((a,b)=>a.x-b.x).map(laneOf))];
    const cols=[...new Set(rows.slice().sort((a,b)=>lens==='client'?a.barrier-b.barrier:a.y-b.y).map(colOf))];
    let h='<table><thead><tr><th>'+esc(meta[lens].x)+'</th>'+cols.map(n=>'<th>'+esc(n)+'</th>').join('')+'</tr></thead><tbody>';
    lanes.forEach(l=>{h+='<tr><th>'+esc(l)+'</th>';cols.forEach(n=>{const cells=rows.filter(c=>laneOf(c)===l&&colOf(c)===n);h+='<td>'+cells.map(c=>'<button type="button" data-matrix-company="'+esc(c.name)+'">'+esc(c.name)+(c.contacts.length?' <b>'+c.contacts.length+'</b>':'')+'</button>').join('')+'</td>';});h+='</tr>';});
    matrix.innerHTML=h+'</tbody></table>';
    matrix.querySelectorAll('[data-matrix-company]').forEach(b=>b.addEventListener('click',()=>show(rows.find(c=>c.name===b.dataset.matrixCompany))));
  }
  function refresh(){
    const rows=current();
    selected=rows.find(c=>c===selected)||rows.slice().sort((a,b)=>a.barrier-b.barrier||b.contacts.length-a.contacts.length)[0];
    select.innerHTML=rows.slice().sort((a,b)=>a.name.localeCompare(b.name)).map(c=>'<option>'+esc(c.name)+'</option>').join('');
    const mapped=k=>rows.filter(c=>c[k]>0).length;
    root.querySelector('[data-map-kpis]').innerHTML=lens==='client'
      ?'<span><strong>'+rows.length+'</strong> clients</span><span><strong>'+mapped('xCode')+'</strong> chain position mapped</span><span><strong>'+mapped('yCode')+'</strong> exposure mapped</span><span><strong>'+mapped('zCode')+'</strong> revenue / head mapped</span><span><strong>'+rows.filter(c=>c.headcount).length+'</strong> headcount known</span><span><strong>'+rows.filter(c=>c.barrier<=2).length+'</strong> talked with</span>'
      :'<span><strong>'+rows.length+'</strong> startups</span><span><strong>'+mapped('xCode')+'</strong> job mapped</span><span><strong>'+mapped('yCode')+'</strong> integration mapped</span><span><strong>'+rows.filter(c=>c.sellsTo).length+'</strong> customer mapped</span>';
    const key=['<span><b>X</b>'+meta[lens].x+'</span>','<span><b>Y</b>'+meta[lens].y+'</span>'];
    if(is3d()) key.push('<span><b>Z</b>'+meta[lens].z+'</span>');
    key.push('<span><b>Dot area</b>headcount</span>');
    key.push('<span><b>Colour</b>'+(lens==='client'?'penetration &mdash; kept when 3D collapses to 2D':'who they sell to')+'</span>');
    root.querySelector('[data-map-axis-key]').innerHTML=key.join('');
    root.querySelector('[data-map-legend]').innerHTML=lens==='client'?penLegend:sellsLegend;
    root.querySelector('[data-map-matrix-title]').textContent=lens==='client'?'Client penetration matrix':'Startup integration matrix';
    root.querySelector('[data-map-matrix-note]').textContent=lens==='client'
      ?'Every client appears once. Penetration records whether we have spoken; it is not a claim about buying intent.'
      :'Every startup appears once, grouped by the job it covers and how far it integrates.';
    dimGroup.style.display=lens==='client'?'':'none';
    rotwrap.style.display=is3d()?'':'none';
    renderMatrix(); show(selected);
  }
  root.querySelectorAll('[data-map-dim]').forEach(b=>b.addEventListener('click',()=>{dim=b.dataset.mapDim;root.querySelectorAll('[data-map-dim]').forEach(x=>{const on=x===b;x.classList.toggle('active',on);x.setAttribute('aria-pressed',String(on));});refresh();}));
  select.addEventListener('change',()=>show(current().find(c=>c.name===select.value)));
  rotation.addEventListener('input',()=>{yaw=Number(rotation.value)*Math.PI/180;draw();});
  svg.addEventListener('pointerdown',e=>{if(!is3d())return;dragging=true;lastX=e.clientX;svg.setPointerCapture(e.pointerId);svg.classList.add('dragging');});
  svg.addEventListener('pointermove',e=>{if(!dragging)return;yaw+=(e.clientX-lastX)*.009;lastX=e.clientX;rotation.value=String(Math.max(-105,Math.min(-20,yaw*180/Math.PI)));draw();});
  svg.addEventListener('pointerup',()=>{dragging=false;svg.classList.remove('dragging');});
  refresh();
})();
</script>'''
    return template.replace("__DATA__", data_json)


def _slug_id(name: str) -> str:
    return "su-" + re.sub(r"[^a-z0-9]+", "-", str(name).lower()).strip("-")


def _usd_short(usd: int) -> str:
    if not usd:
        return "none"
    if usd >= 1_000_000_000:
        return f"${usd / 1_000_000_000:.1f}".rstrip("0").rstrip(".") + "B"
    return f"${usd / 1_000_000:.0f}M"


def _startup_inspector(data_json: str) -> str:
    """One-company-at-a-time panel for the startup map.

    Driven by the dots, the matrix chips and its own prev/next. The stepper is
    the point: walking the population in order is how a competitive scene gets
    read, and a fifteen-anchor jump list does not do that.
    """
    template = r'''
<section class="smap-inspect" id="startup-inspector" aria-label="Inspect one startup">
  <div class="smap-inspect-bar">
    <div class="smap-step">
      <button type="button" data-su-prev aria-label="Previous startup">&#9664; Prev</button>
      <button type="button" data-su-next aria-label="Next startup">Next &#9654;</button>
      <select data-su-pick aria-label="Choose a startup to inspect"></select>
    </div>
    <div class="smap-step-count" data-su-count aria-live="polite"></div>
  </div>
  <div class="smap-inspect-body" data-su-body></div>
</section>
<script>
(() => {
  const root = document.getElementById('startup-inspector');
  if (!root || root.dataset.ready) return;
  root.dataset.ready = 'true';
  const all = __DATA__;
  if (!all.length) return;
  const body = root.querySelector('[data-su-body]');
  const pick = root.querySelector('[data-su-pick]');
  const count = root.querySelector('[data-su-count]');
  let i = 0;
  const esc = v => String(v == null ? '' : v).replace(/[&<>"']/g,
    ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
  const num = n => Number(n).toLocaleString('en-US');
  // A missing value is missing, never zero and never a dash that reads as none.
  const fact = (label, value, sub) => '<div><dt>' + esc(label) + '</dt><dd' +
    (value ? '>' : ' class="is-blank">') + esc(value || 'not recorded') +
    (sub ? '<small>' + esc(sub) + '</small>' : '') + '</dd></div>';
  const block = (label, text, cls) => text
    ? '<p class="smap-why' + (cls ? ' ' + cls : '') + '"><b>' + esc(label) + '</b>' +
      esc(text) + '</p>'
    : '';

  function render() {
    const c = all[i];
    pick.value = c.id;
    count.textContent = (i + 1) + ' of ' + all.length + ' · ' + c.id;
    const site = c.url
      ? ' · <a class="co-src" href="' + esc(c.url) + '" target="_blank" rel="noopener">site</a>'
      : '';
    const services = c.services.length
      ? '<p class="smap-sub">Services they sell</p><ul class="smap-services">' +
        c.services.map(s => '<li>' + esc(s) + '</li>').join('') + '</ul>'
      : '<p class="smap-sub">Services they sell</p><p class="smap-work">Not recorded yet.</p>';
    body.innerHTML =
      '<div class="smap-inspect-head"><div><h4>' + esc(c.name) + '</h4>' +
      '<div class="smap-card-sub">' + esc(c.sector) + site + '</div></div>' +
      '<span class="smap-liab liab-' + c.liabCode + '">' + esc(c.liab) + '</span></div>' +
      '<p class="smap-work">' + esc(c.desc || 'Not recorded.') + '</p>' +
      '<dl class="smap-facts">' +
        fact('stage', c.stage) +
        fact('total raised', c.raised) +
        fact('headcount', c.headcount ? num(c.headcount) : '', c.headSource) +
        fact('founded', c.founded) +
        fact('country', c.country) +
        fact('job covered', c.job) +
        fact('integration', c.integration) +
        fact('sells to', c.sells) +
        fact('prove-out', c.proveout) +
        fact('liability', c.liab) +
      '</dl>' + services +
      block('Unresolved identity', c.conflict, 'is-conflict') +
      block('Why it matters here', c.relevance) +
      block('Liability', c.liabNotes) +
      block('Funding', c.fundingNotes) +
      block('Headcount', c.headNote) +
      (c.missing.length
        ? block('Missing on this entry', c.missing.join(', ')) : '') +
      (c.sources ? '<p class="smap-srcline"><b>Sources</b> ' + esc(c.sources) + '</p>' : '');
    document.querySelectorAll('.cmap-point[data-su]').forEach(g =>
      g.classList.toggle('is-active', g.dataset.su === c.id));
  }
  function goto(id, scroll) {
    const n = all.findIndex(c => c.id === id);
    if (n < 0) return;
    i = n; render();
    if (scroll) root.scrollIntoView({behavior: 'smooth', block: 'nearest'});
  }
  pick.innerHTML = all.map(c =>
    '<option value="' + esc(c.id) + '">' + esc(c.name) + '</option>').join('');
  pick.addEventListener('change', () => goto(pick.value, false));
  root.querySelector('[data-su-prev]').addEventListener('click', () => {
    i = (i - 1 + all.length) % all.length; render();
  });
  root.querySelector('[data-su-next]').addEventListener('click', () => {
    i = (i + 1) % all.length; render();
  });
  // Dots and matrix chips are wired here rather than at their own render sites:
  // the inspector owns selection, so there is one place that changes it.
  document.querySelectorAll('[data-su]').forEach(el => {
    if (el.closest('#startup-inspector')) return;
    const act = ev => { ev.preventDefault(); goto(el.dataset.su, true); };
    el.addEventListener('click', act);
    el.addEventListener('keydown', ev => {
      if (ev.key === 'Enter' || ev.key === ' ') act(ev);
    });
  });
  render();
})();
</script>'''
    return template.replace("__DATA__", data_json)


def render_startups_tab(fm: dict, companies: list[dict],
                        contacts: list[dict] | None = None) -> str:
    """The supply side on its own page.

    Split out of the company space map on 2026-08-27. The two populations share
    no axis — a client is placed by where it sits in a supply chain, a startup by
    which job it automates — so one toggle over one coordinate system made each
    map read as a broken version of the other.

    Everything here is server-rendered from declared fields, with no JS: the
    matrix cells and the dots are anchors to the cards below, and each dot
    carries a native <title>. A map of fifteen companies does not need a runtime.
    """
    entities = [e for e in _company_map_entities(fm, companies, contacts or [])
                if e["map"] == "startup"]
    if not entities:
        return ('<div class="co-empty"><p>No entry in <code>outreach/companies.md</code> '
                'carries <code>map: startup</code>.</p><p>Add supply-side companies with '
                '<code>job_covered</code>, <code>integration</code> and '
                '<code>liability_taken</code> declared, and they appear here.</p></div>')

    vocab = _map_vocab(fm)
    esc = escape
    rows = sorted(entities, key=lambda e: (-(e.get("liabCode") or 0), e["name"].lower()))

    # ── the claim panel, computed rather than asserted ────────────────────────
    software = [e for e in rows if e["yLabel"] == "software only"]
    carries = [e for e in software if (e.get("liabCode") or 0) > 1]
    owns = [e for e in rows if (e.get("liabCode") or 0) == 5]
    owns_factory = [e for e in owns if e["yLabel"] == "owns factory"]
    in_job = [e for e in rows if e.get("proveoutCode") == 3]
    in_job_factory = [e for e in in_job if e["yLabel"] == "owns factory"]
    # An empty job lane is a finding, not an omission: it names the work no
    # startup on this map has taken on.
    empty_lanes = [_labelled("job_covered", j) for j in vocab["job_covered"]
                   if not any(e["xLabel"] == _labelled("job_covered", j) for e in rows)]
    by_factory = ("all " + str(len(owns_factory)) + " of them by owning the factory"
                  if owns and len(owns_factory) == len(owns)
                  else str(len(owns_factory)) + " by owning the factory")

    claim = (
        "<b>What the map currently says</b><p>"
        f"<em>{len(software)}</em> of these companies sell software only, and "
        f"<em>{len(carries)}</em> of those carry any liability for the part. "
        f"<em>{len(owns)}</em> own the outcome &mdash; {by_factory}. "
        f"<em>{len(in_job)}</em> sit directly in the prove-out job, and "
        f"<em>{len(in_job_factory)}</em> of those own their own factory. Today the way to "
        "carry the liability is to buy the machines."
        + (f" No startup here covers <em>{'</em>, <em>'.join(empty_lanes)}</em> at all."
           if empty_lanes else "")
        + "</p>")

    # ── KPI strip ────────────────────────────────────────────────────────────
    funded = [e for e in rows if e.get("raised")]
    total_raised = sum(e["raised"] for e in funded)
    kpis = "".join(f"<span><strong>{v}</strong>{k}</span>" for k, v in [
        ("mapped", len(rows)),
        ("in the prove-out job", len(in_job)),
        ("carry liability", len([e for e in rows if (e.get("liabCode") or 0) > 1])),
        ("funding disclosed", f"{len(funded)}/{len(rows)}"),
        ("capital in the space", _usd_short(total_raised)),
    ])

    # ── scatter: job covered x integration, colour = liability, size = raised ─
    jlabels = [_labelled("job_covered", j) for j in vocab["job_covered"]
               if any(e["xLabel"] == _labelled("job_covered", j) for e in rows)]
    ilabels = [_labelled("integration", i) for i in vocab["integration"]
               if any(e["yLabel"] == _labelled("integration", i) for e in rows)]
    unmapped = [e for e in rows if not e["xCode"] or not e["yCode"]]

    L, R, TOP, BOT = 156, 1068, 40, 486
    cw = (R - L) / max(len(jlabels), 1)
    rh = (BOT - TOP) / max(len(ilabels), 1)
    svg: list[str] = []
    for n, lab in enumerate(jlabels):
        svg.append(f'<line class="cmap-gridline" x1="{L + cw * n:.1f}" y1="{TOP}" '
                   f'x2="{L + cw * n:.1f}" y2="{BOT}"/>')
        svg.append(f'<text class="cmap-axis" x="{L + cw * (n + .5):.1f}" y="{BOT + 21}" '
                   f'text-anchor="middle">{esc(lab.upper())}</text>')
    for n, lab in enumerate(ilabels):
        svg.append(f'<line class="cmap-gridline" x1="{L}" y1="{BOT - rh * n:.1f}" '
                   f'x2="{R}" y2="{BOT - rh * n:.1f}"/>')
        svg.append(f'<text class="cmap-axis" x="{L - 11}" y="{BOT - rh * (n + .5) + 3:.1f}" '
                   f'text-anchor="end">{esc(lab.upper())}</text>')
    svg.append(f'<line class="cmap-edge" x1="{L}" y1="{TOP}" x2="{L}" y2="{BOT}"/>')
    svg.append(f'<line class="cmap-edge" x1="{L}" y1="{BOT}" x2="{R}" y2="{BOT}"/>')

    biggest = max((e["raised"] for e in funded), default=1)
    for jn, jl in enumerate(jlabels):
        for inn, il in enumerate(ilabels):
            cell = sorted((e for e in rows if e["xLabel"] == jl and e["yLabel"] == il),
                          key=lambda e: e["name"].lower())
            cols = max(1, math.ceil(math.sqrt(len(cell))))
            nrows = math.ceil(len(cell) / cols) if cell else 1
            for k, e in enumerate(cell):
                # Dot AREA tracks capital raised, so a $2B company reads as ~26x
                # the ink of a $3M one rather than 700x. Undisclosed draws hollow.
                r = 6 + 15 * math.sqrt(e["raised"] / biggest) if e.get("raised") else 6.5
                cx = L + cw * (jn + .5) + ((k % cols) - (cols - 1) / 2) * 62
                cy = BOT - rh * (inn + .5) + (k // cols - (nrows - 1) / 2) * 46
                hollow = "" if e.get("raised") else " cmap-nohead"
                tip = (f'{e["name"]} — {e.get("stageLabel", "")}, '
                       f'{e.get("raisedLabel", "")} — {e.get("liabLabel", "")} — '
                       f'{e.get("proveoutLabel", "")}')
                svg.append(
                    f'<g class="cmap-point liab-{e.get("liabCode") or 0}{hollow}" '
                    f'data-su="{esc(e["id"])}" tabindex="0" role="button">'
                    f'<title>{esc(tip)}</title>'
                    f'<circle class="cmap-core" cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"/>'
                    f'</g>')
                # Categorical axes put several companies in one cell, so labels
                # have to be pushed apart in two directions. Keying the
                # above/below flip to the ROW (not the sequence) is what stops a
                # lower row's label colliding with the row above it; the column
                # parity nudge then separates neighbours within a row.
                row_i, col_i = k // cols, k % cols
                out = 11 if col_i % 2 else 0
                ly = (cy - r - 6 - out if row_i % 2 == 0
                      else cy + r + 13 + out)
                svg.append(f'<text class="cmap-point-label" x="{cx:.1f}" '
                           f'y="{ly:.1f}" text-anchor="middle">'
                           f'{esc(e["name"])}</text>')

    legend = ('<span><i class="cmap-dot liab-0"></i>not mapped</span>' + "".join(
        f'<span><i class="cmap-dot liab-{n}"></i>'
        f'{esc(_labelled("liability_taken", v))}</span>'
        for n, v in enumerate(vocab["liability_taken"], start=1)) +
        '<span><i class="cmap-hollow"></i>funding not disclosed</span>')

    unmapped_note = ""
    if unmapped:
        unmapped_note = (
            '<p class="smap-note"><strong>Off the scale:</strong> ' + ", ".join(
                f'<a href="#" data-su="{esc(e["id"])}">{esc(e["name"])}</a>'
                for e in unmapped)
            + " &mdash; not plotted, because a declared axis is missing. Missing data stands "
              "outside the map rather than being guessed onto it.</p>")

    # ── liability x integration matrix: the belief's own view ────────────────
    liab_vals = ["", *vocab["liability_taken"]]
    head = "".join(
        f"<th>{esc(_labelled('liability_taken', v) if v else 'not mapped')}</th>"
        for v in liab_vals)
    body = ""
    for il in reversed(ilabels):
        body += f"<tr><th>{esc(il)}</th>"
        for v in liab_vals:
            vl = _labelled("liability_taken", v) if v else _UNMAPPED
            cells = [e for e in rows if e["yLabel"] == il and e.get("liabLabel") == vl]
            body += "<td>" + "".join(
                f'<a href="#" data-su="{esc(e["id"])}">{esc(e["name"])}</a>'
                for e in cells) + "</td>"
        body += "</tr>"
    matrix = (f'<div class="cmap-matrix smap-matrix"><table><thead><tr><th>Integration</th>'
              f'{head}</tr></thead><tbody>{body}</tbody></table></div>')

    # ── capital bars ─────────────────────────────────────────────────────────
    bars = ""
    for e in sorted(rows, key=lambda e: -(e.get("raised") or 0)):
        if e.get("raised"):
            pct = math.sqrt(e["raised"] / biggest) * 100
            fill = (f'<div class="smap-bar-fill cmap-dot liab-{e.get("liabCode") or 0}" '
                    f'style="width:{pct:.1f}%"></div>')
            cls = "smap-bar"
        else:
            fill, cls = "", "smap-bar is-undisclosed"
        bars += (f'<div class="{cls}"><div class="smap-bar-name">{esc(e["name"])}</div>'
                 f'<div class="smap-bar-track">{fill}</div>'
                 f'<div class="smap-bar-val">{esc(e.get("raisedLabel", ""))}</div></div>')

    # ── inspector payload: one company at a time, clicked or stepped ─────────
    # "Go one by one" is the actual workflow, so the panel takes prev/next as
    # well as a picker, and every dot and matrix chip above drives it.
    payload = [{
        "id": e["id"], "name": e["name"], "sector": e.get("sector") or "",
        "country": e.get("country") or "", "url": e.get("sourceUrl") or "",
        "services": e.get("services") or [], "desc": e.get("description") or "",
        "stage": e.get("stageLabel") or "", "raised": e.get("raisedLabel") or "",
        "headcount": e.get("headcount"), "headSource": e.get("headcountSource") or "",
        "headNote": e.get("headcountNote") or "", "founded": e.get("founded") or "",
        "job": e["xLabel"], "integration": e["yLabel"], "sells": e.get("sellsTo") or "",
        "liab": e.get("liabLabel") or "", "liabCode": e.get("liabCode") or 0,
        "proveout": e.get("proveoutLabel") or "", "relevance": e.get("relevance") or "",
        "liabNotes": e.get("liabNotes") or "", "fundingNotes": e.get("fundingNotes") or "",
        "conflict": e.get("conflict") or "", "sources": e.get("sources") or "",
        "missing": e.get("missing") or [],
    } for e in rows]
    inspector = _startup_inspector(json.dumps(payload, ensure_ascii=True))

    # ── the cards: what each one is actually working on ──────────────────────
    cards = ""
    for e in rows:
        meta = "".join(f"<span><b>{k}</b> {esc(v)}</span>" for k, v in [
            ("stage", e.get("stageLabel", "")),
            ("raised", e.get("raisedLabel", "")),
            ("job", e["xLabel"]),
            ("integration", e["yLabel"]),
            ("prove-out", e.get("proveoutLabel", "")),
            ("headcount", f'{e["headcount"]:,}' if e.get("headcount") else ""),
            ("founded", e.get("founded") or ""),
            ("country", e.get("country") or ""),
        ] if v)
        svc = ""
        if e.get("services"):
            svc = ('<ul class="smap-services">' + "".join(
                f"<li>{esc(s)}</li>" for s in e["services"]) + "</ul>")
        why = ""
        if e.get("conflict"):
            why += ('<p class="smap-why is-conflict"><b>Unresolved identity</b>'
                    f'{esc(e["conflict"])}</p>')
        if e.get("relevance"):
            why += f'<p class="smap-why"><b>Why it matters here</b>{esc(e["relevance"])}</p>'
        if e.get("liabNotes"):
            why += f'<p class="smap-why"><b>Liability</b>{esc(e["liabNotes"])}</p>'
        if e.get("fundingNotes"):
            why += f'<p class="smap-why"><b>Funding</b>{esc(e["fundingNotes"])}</p>'
        link = (f' &middot; <a class="co-src" href="{esc(e["sourceUrl"])}" target="_blank" '
                f'rel="noopener">site</a>') if e.get("sourceUrl") else ""
        unres = " is-unresolved" if e.get("entryStatus") == "unresolved" else ""
        cards += (
            f'<article class="smap-card{unres}" id="{_slug_id(e["name"])}">'
            f'<div class="smap-card-top"><div><h4>{esc(e["name"])}</h4>'
            f'<div class="smap-card-sub">{esc(e["id"])} &middot; '
            f'{esc(e.get("sector") or "")}{link}</div></div>'
            f'<span class="smap-liab liab-{e.get("liabCode") or 0}">'
            f'{esc(e.get("liabLabel", ""))}</span></div>'
            f'<p class="smap-work">{esc(e.get("description") or "Not recorded.")}</p>'
            f'{svc}<div class="smap-meta">{meta}</div>{why}</article>')

    return (
        '<section class="cmap" aria-labelledby="smap-title">'
        '<div class="cmap-head"><div>'
        '<div class="co-eyebrow">Startup scene</div>'
        '<h2 id="smap-title">Who is working on this, and what they carry</h2>'
        '<p>The supply side: companies selling into, or automating around, the same jobs '
        'the demand-side registry buys. Position is the job they cover against how far they '
        'vertically integrate. Dot area is capital raised. <strong>Colour is the liability '
        'they take on the part</strong>. Every value reads a declared field in '
        '<code>companies.md</code>.</p>'
        '</div></div>'
        f'<div class="smap-claim">{claim}</div>'
        f'<div class="cmap-kpis">{kpis}</div>'
        '<div class="cmap-axis-key"><span><b>X</b>job covered</span>'
        '<span><b>Y</b>vertical integration: licence to owned factory</span>'
        '<span><b>Dot area</b>total capital raised</span>'
        '<span><b>Colour</b>liability taken on the part</span></div>'
        '<div class="cmap-stage"><svg viewBox="0 0 1100 518" role="img" '
        'aria-labelledby="smap-svg-title smap-svg-desc">'
        '<title id="smap-svg-title">Startup scene map</title>'
        '<desc id="smap-svg-desc">Startups positioned by the manufacturing job they cover '
        'and how far they vertically integrate, sized by capital raised and coloured by the '
        'liability they take on the finished part.</desc>'
        f'{"".join(svg)}</svg></div>'
        f'<div class="cmap-legend">{legend}</div>{unmapped_note}'
        f'{inspector}'
        '<div class="cmap-matrix-head smap-spaced"><h3>Liability by integration depth</h3>'
        '<p>The belief&rsquo;s own view. Read along the <em>software only</em> row: while it '
        'stays entirely under <em>carries none</em>, nobody is selling a tool into this work '
        'while owning what happens on the first run.</p></div>'
        f'{matrix}'
        '<div class="cmap-matrix-head smap-spaced"><h3>Capital in the space</h3>'
        '<p>Bar length is the square root of total raised, so it stays comparable with dot '
        'area on the map. A hatched track is a company with no public figure &mdash; '
        'missing, not zero.</p></div>'
        f'<div class="smap-bars">{bars}</div>'
        '<div class="cmap-matrix-head smap-spaced"><h3>What each one is working on</h3>'
        '<p>Ordered by liability carried, heaviest first.</p></div>'
        f'<div class="smap-grid">{cards}</div>'
        '</section>')


def render_companies_tab(companies: list[dict], fm: dict, contacts: list[dict] | None = None) -> str:
    if not companies:
        return ('<div class="co-empty"><p>No <code>outreach/companies.md</code> yet.</p>'
                '<p>Run <code>/startup-outreach-intel</code>, or log companies by hand '
                'into <code>reports/outreach/companies.md</code>.</p></div>')

    def sort_key(c):
        side = str(c.get("tier_side") or "")
        score = c.get("pain_score")
        try:
            score = -float(score)
        except (TypeError, ValueError):
            score = 0.0
        return (_CO_SIDE_ORDER.index(side) if side in _CO_SIDE_ORDER else 99, score)

    ordered = sorted(companies, key=sort_key)
    countries = {str(c.get("country") or "").strip() for c in companies} - {""}
    scored = [c for c in companies if c.get("pain_score") not in (None, "")]

    kpis = [(len(companies), "Companies"), (len(countries), "Countries")]
    for side in _CO_SIDE_ORDER[:-1]:
        n = sum(1 for c in companies if str(c.get("tier_side") or "") == side)
        if n:
            kpis.append((n, side))
    if scored:
        kpis.append((len(scored), "Scored"))

    kpi_html = "".join(
        f'<div class="co-kpi"><strong>{v}</strong><span>{escape(str(label))}</span></div>'
        for v, label in kpis)

    updated = escape(str(fm.get("last_updated") or "—"))
    out = [
        '<div class="co-wrap">',
        '<div class="co-hero">',
        '<div class="co-eyebrow">Company registry</div>',
        '<h2>Who is in this market</h2>',
        '<p>One row per organisation, grouped by tier side. Sorted by <code>pain_score</code> '
        'where the intel run set one; companies logged by hand carry no score and keep file '
        f'order. Source of truth: <code>outreach/companies.md</code> &middot; last updated {updated}.</p>',
        f'<div class="co-kpis">{kpi_html}</div>',
        '</div>',
        render_company_space_map(fm, companies, contacts or []),
    ]

    for side in _CO_SIDE_ORDER:
        rows = [c for c in ordered if str(c.get("tier_side") or "") == side]
        if not rows:
            continue
        out.append('<div class="co-group">')
        out.append('<div class="co-group-head"><span>%s</span><b>%d</b></div>'
                   % (escape(_CO_SIDE_LABEL.get(side, side)), len(rows)))
        for c in rows:
            # The `## Heading` is the human-readable name; canonical_name is the
            # normalized string used for dedup and is often the legal entity.
            name = escape(str(c.get("_heading") or c.get("company")
                              or c.get("canonical_name") or "?"))
            legal = str(c.get("canonical_name") or "").strip()
            legal = escape(legal) if legal and legal != str(c.get("_heading") or "").strip() else ""
            cid = escape(str(c.get("id") or ""))
            meta = [escape(str(c[k])) for k in ("country", "sector")
                    if c.get(k) not in (None, "", [])]
            desc = c.get("makes_or_does") or c.get("rationale") or ""
            role = _co_suffix(c, "_role")
            note = _co_suffix(c, "_relevance")
            money = _co_suffix(c, "_eur")
            score = c.get("pain_score")
            src = c.get("source_url")
            flagged = "UNVERIFIED" in str(desc).upper() or "UNVERIFIED" in str(c.get("sector") or "").upper()

            out.append('<article class="co-row" data-side="%s">' % escape(str(side)))
            out.append('<div>')
            out.append('<h3 class="co-name">%s<span class="co-id">%s</span>%s</h3>' % (
                name, cid,
                '<span class="co-flagchip">unverified</span>' if flagged else ""))
            if legal:
                meta.insert(0, legal)
            if meta:
                out.append('<p class="co-meta">%s</p>'
                           % "".join("<span>%s</span>" % m for m in meta))
            if desc:
                out.append('<p class="co-desc">%s</p>' % _inline_md(str(desc).strip()))
            if note:
                out.append('<details class="co-note"><summary>Why it is on the list</summary>'
                           '<p>%s</p></details>' % _inline_md(str(note).strip()))
            out.append('</div>')

            out.append('<div class="co-side">')
            if score not in (None, ""):
                out.append('<span class="co-score">pain %s</span>' % escape(str(score)))
            if money is not None:
                out.append('<span class="co-fig">%s</span>' % _co_money(money))
            if role:
                out.append('<span class="co-role">%s</span>' % _inline_md(str(role).strip()))
            if src:
                out.append('<a class="co-src" href="%s" target="_blank" rel="noopener">source &rarr;</a>'
                           % escape(str(src)))
            out.append('</div>')
            out.append('</article>')
        out.append('</div>')

    out.append('</div>')
    return "\n".join(out)







EMAIL_CSS = """
/* ── researcher email workspace ── */
.email-workspace {display:flex;flex-direction:column;gap:16px;}
.email-hero {position:relative;overflow:hidden;border:1px solid var(--border);border-radius:var(--r-lg);background:linear-gradient(135deg,rgba(96,165,250,.10),rgba(167,139,250,.04) 52%,var(--surface) 78%);padding:24px;}
.email-hero:after {content:"PAPER  →  NOTE  →  REPLY";position:absolute;right:22px;top:20px;color:rgba(148,163,184,.28);font-size:11px;font-weight:800;letter-spacing:.18em;}
.email-eyebrow {font-size:10px;text-transform:uppercase;letter-spacing:.12em;color:var(--accent);font-weight:700;}
.email-hero h2 {font-family:Georgia,"Iowan Old Style",serif;font-size:28px;line-height:1.1;margin:8px 0 7px;letter-spacing:-.025em;}
.email-hero p {max-width:720px;color:var(--text-dim);font-size:12px;line-height:1.6;}
.email-kpis {display:flex;flex-wrap:wrap;gap:8px;margin-top:18px;}
.email-kpi {min-width:118px;padding:10px 12px;border:1px solid var(--border);border-radius:var(--r-md);background:rgba(15,23,42,.52);}
.email-kpi strong {display:block;font-size:20px;line-height:1;color:var(--text);}
.email-kpi span {display:block;margin-top:5px;font-size:9px;text-transform:uppercase;letter-spacing:.09em;color:var(--text-dimmer);}
.email-filterbar {display:flex;flex-wrap:wrap;align-items:center;gap:7px;}
.email-filter {appearance:none;border:1px solid var(--border);border-radius:999px;background:var(--surface);color:var(--text-dim);padding:7px 11px;font:inherit;font-size:10.5px;font-weight:700;cursor:pointer;}
.email-filter:hover,.email-filter.active {color:var(--text);border-color:rgba(96,165,250,.55);background:rgba(96,165,250,.09);}
.email-filter-count {font-weight:500;color:var(--text-dimmer);margin-left:3px;}
.email-ledger-wrap {overflow:hidden;border:1px solid var(--border);border-radius:var(--r-lg);background:var(--surface);}
.email-ledger-head,.email-row {display:grid;grid-template-columns:minmax(220px,1.15fr) minmax(280px,1.6fr) 165px 100px;align-items:center;gap:18px;}
.email-ledger-head {padding:10px 18px;border-bottom:1px solid var(--border);background:var(--surface-2);color:var(--text-dimmer);font-size:9px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;}
.email-ledger {display:flex;flex-direction:column;}
.email-row {--email-state:#64748b;position:relative;min-width:0;padding:13px 18px 13px 21px;border-bottom:1px solid var(--border-subtle);transition:background .14s ease;}
.email-row:last-child {border-bottom:none;}
.email-row:before {content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--email-state);opacity:.8;}
.email-row[data-state="draft"] {--email-state:#94a3b8;}
.email-row[data-state="sent"] {--email-state:#60a5fa;}
.email-row[data-state="replied"] {--email-state:#22c55e;background:rgba(34,197,94,.035);}
.email-row:hover,.email-row:focus-within {background:rgba(96,165,250,.055);}
.email-researcher-btn {min-width:0;border:0;background:none;color:var(--text);padding:0;text-align:left;font:inherit;cursor:pointer;}
.email-researcher-btn strong {display:block;overflow:hidden;text-overflow:ellipsis;font-size:13px;line-height:1.25;}
.email-researcher-btn span {display:block;margin-top:3px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--text-dimmer);font-size:10px;}
.email-researcher-btn:hover strong,.email-researcher-btn:focus-visible strong {color:var(--accent);text-decoration:underline;text-underline-offset:3px;}
.email-researcher-btn:focus-visible {outline:1px solid var(--accent);outline-offset:5px;border-radius:2px;}
.email-row-subject {min-width:0;}
.email-row-subject-text {display:block;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-family:Georgia,"Iowan Old Style",serif;color:var(--text-dim);font-size:12.5px;}
.email-row-paper {display:inline-block;margin-top:3px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:10px;color:#60a5fa;text-decoration:none;opacity:.85;}
.email-row-paper:hover {opacity:1;text-decoration:underline;}
.email-state {flex-shrink:0;border:1px solid color-mix(in srgb,var(--email-state) 50%,transparent);color:var(--email-state);border-radius:999px;padding:4px 8px;font-size:9px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;}
.email-row-addr {display:block;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:10.5px;color:#60a5fa;opacity:.85;margin-top:2px;}
.email-row-date {color:var(--text-dimmer);font-size:10px;font-variant-numeric:tabular-nums;text-align:right;}
.email-address {display:inline-block;margin-top:9px;color:var(--accent);font-size:11px;}
.email-address:hover {text-decoration:underline;}
.email-paper {display:flex;align-items:flex-start;gap:7px;margin-top:13px;padding:10px 11px;border:1px solid var(--border-subtle);border-radius:var(--r-md);background:var(--surface-2);font-size:10.5px;line-height:1.45;color:var(--text-dim);}
.email-paper b {color:var(--text-dimmer);font-size:9px;text-transform:uppercase;letter-spacing:.08em;flex-shrink:0;margin-top:1px;}
.email-paper a {color:var(--text);}
.email-paper a:hover {color:var(--accent);text-decoration:underline;}
.email-subject {font-family:Georgia,"Iowan Old Style",serif;font-size:17px;line-height:1.35;margin:14px 0 0;color:var(--text);}
.email-subject-alt {font-size:9.5px;line-height:1.45;color:var(--yellow);margin-top:5px;}
.email-meta {display:flex;flex-wrap:wrap;gap:6px 12px;margin-top:8px;color:var(--text-dimmer);font-size:9.5px;}
.email-reply {margin-top:12px;border:1px solid rgba(34,197,94,.3);border-radius:var(--r-md);background:rgba(34,197,94,.07);padding:11px 12px;}
.email-reply b {display:block;color:var(--green);font-size:9px;text-transform:uppercase;letter-spacing:.09em;margin-bottom:5px;}
.email-reply blockquote {font-family:Georgia,"Iowan Old Style",serif;font-size:13px;line-height:1.5;margin:0;color:var(--text);white-space:pre-wrap;}
.email-record-label {margin-top:17px;color:var(--text-dimmer);font-size:9px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;}
.email-thread {display:flex;flex-direction:column;gap:9px;margin-top:18px;}
.email-thread-title {color:var(--text-dimmer);font-size:9px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;}
.email-thread-item {--thread-color:#64748b;border:1px solid var(--border-subtle);border-left:3px solid var(--thread-color);border-radius:0 var(--r-md) var(--r-md) 0;background:var(--surface-2);overflow:hidden;}
.email-thread-item.sent {--thread-color:#60a5fa;}.email-thread-item.received {--thread-color:#22c55e;}.email-thread-item.unsent {--thread-color:#f59e0b;}
.email-thread-item summary {display:flex;align-items:center;justify-content:space-between;gap:14px;padding:11px 12px;cursor:pointer;list-style:none;}
.email-thread-item summary::-webkit-details-marker {display:none;}
.email-thread-item summary:hover {background:rgba(148,163,184,.045);}
.email-thread-main {min-width:0;}.email-thread-main strong {display:block;color:var(--text);font-size:11px;}.email-thread-main span {display:block;margin-top:3px;color:var(--text-dimmer);font-size:9.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.email-thread-action {flex:0 0 auto;color:var(--accent);font-size:9px;font-weight:700;}
.email-thread-item[open] .email-thread-action:after {content:"Hide ↑";}.email-thread-item:not([open]) .email-thread-action:after {content:"Read ↓";}
.email-thread-copy {position:relative;padding:13px 13px 42px;border-top:1px solid var(--border-subtle);background:#0b1220;}
.email-thread-copy pre {white-space:pre-wrap;word-break:break-word;margin:0;font:12px/1.62 Georgia,"Iowan Old Style",serif;color:var(--text);}
.email-thread-item.received .email-thread-copy {background:rgba(34,197,94,.045);}.email-thread-item.unsent .email-thread-copy {background:rgba(245,158,11,.045);}
.email-unsent-warning {margin:0;padding:9px 12px;border-top:1px solid rgba(245,158,11,.22);color:var(--yellow);font-size:9.5px;line-height:1.5;}
.email-copy-note {font-size:9.5px;color:var(--yellow);line-height:1.45;margin:10px 0 0;}
.email-body {position:relative;margin-top:10px;padding:13px 13px 40px;border-radius:var(--r-md);background:#0b1220;border:1px solid var(--border-subtle);}
.email-body pre {white-space:pre-wrap;word-break:break-word;margin:0;font:12px/1.58 Georgia,"Iowan Old Style",serif;color:var(--text);}
.email-copy-btn {position:absolute;right:9px;bottom:8px;border:1px solid var(--border);border-radius:7px;background:var(--surface-2);color:var(--text-dim);padding:5px 8px;font:inherit;font-size:9px;cursor:pointer;}
.email-copy-btn:hover {color:var(--accent);border-color:var(--accent);}
.email-empty {padding:34px;text-align:center;color:var(--text-dimmer);}
.email-modal-backdrop {position:fixed;inset:0;z-index:1000;display:grid;place-items:center;padding:24px;background:rgba(2,6,23,.78);backdrop-filter:blur(7px);}
.email-modal-backdrop[hidden] {display:none;}
.email-modal {position:relative;width:min(780px,100%);max-height:min(88vh,900px);overflow:auto;border:1px solid rgba(148,163,184,.28);border-radius:18px;background:var(--surface);box-shadow:0 28px 90px rgba(0,0,0,.55);}
.email-modal-top {position:sticky;top:0;z-index:2;display:flex;align-items:flex-start;justify-content:space-between;gap:18px;padding:21px 23px 17px;border-bottom:1px solid var(--border);background:rgba(15,23,42,.96);backdrop-filter:blur(12px);}
.email-modal-title {min-width:0;}
.email-modal-title h3 {margin:5px 0 0;font:24px/1.15 Georgia,"Iowan Old Style",serif;letter-spacing:-.02em;}
.email-modal-title p {margin-top:5px;color:var(--text-dimmer);font-size:10.5px;}
.email-modal-close {width:32px;height:32px;flex:0 0 auto;border:1px solid var(--border);border-radius:50%;background:var(--surface-2);color:var(--text-dim);font:20px/1 sans-serif;cursor:pointer;}
.email-modal-close:hover,.email-modal-close:focus-visible {color:var(--text);border-color:var(--accent);outline:none;}
.email-modal-content {padding:22px 23px 25px;}
.email-modal-links {display:flex;flex-wrap:wrap;align-items:center;gap:7px 14px;}
.email-modal-links a {color:var(--accent);font-size:11px;}
.email-modal-links a:hover {text-decoration:underline;}
.email-modal-meta {display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:17px;}
.email-modal-meta div {padding:10px 11px;border:1px solid var(--border-subtle);border-radius:var(--r-md);background:var(--surface-2);}
.email-modal-meta b {display:block;margin-bottom:4px;color:var(--text-dimmer);font-size:8.5px;letter-spacing:.08em;text-transform:uppercase;}
.email-modal-meta span {font-size:10.5px;color:var(--text-dim);}
.email-modal-meta span+span:before {content:" · ";color:var(--text-dimmer);}
@media (max-width:800px) {
  .email-hero:after {display:none;}.email-hero {padding:20px;}
  .email-ledger-head {display:none;}
  .email-row {grid-template-columns:minmax(0,1fr) auto;gap:6px 12px;padding:14px 15px 14px 19px;}
  .email-row-subject {grid-column:1/-1;grid-row:2;}
  .email-row-date {grid-column:1;grid-row:3;text-align:left;}
  .email-state {grid-column:2;grid-row:1;}
  .email-modal-backdrop {padding:8px;place-items:end center;}
  .email-modal {max-height:94vh;border-radius:16px 16px 8px 8px;}
  .email-modal-meta {grid-template-columns:1fr;}
}
@media (prefers-reduced-motion:reduce) {.email-row {transition:none;}}
"""


def render_email_tab(records: list[dict]) -> str:
    counts = Counter(r.get("state") or "draft" for r in records)
    reached = counts.get("sent", 0) + counts.get("replied", 0)
    return f'''<div class="email-workspace">
<section class="email-hero">
  <div class="email-eyebrow">Researcher outreach</div>
  <h2>The paper is the opening.</h2>
  <p>A compact campaign ledger. Select a researcher to open their paper trail, personalized copy, delivery evidence, and any reply.</p>
  <div class="email-kpis">
    <div class="email-kpi"><strong>{len(records)}</strong><span>Researchers</span></div>
    <div class="email-kpi"><strong>{reached}</strong><span>Reached</span></div>
    <div class="email-kpi"><strong>{counts.get("replied", 0)}</strong><span>Replied</span></div>
    <div class="email-kpi"><strong>{counts.get("draft", 0)}</strong><span>Still drafts</span></div>
  </div>
</section>
<div class="email-filterbar" role="group" aria-label="Filter email campaign">
  <button class="email-filter active" data-email-filter="all">All <span class="email-filter-count">{len(records)}</span></button>
  <button class="email-filter" data-email-filter="replied">Replied <span class="email-filter-count">{counts.get("replied", 0)}</span></button>
  <button class="email-filter" data-email-filter="sent">Sent <span class="email-filter-count">{counts.get("sent", 0)}</span></button>
  <button class="email-filter" data-email-filter="draft">Draft <span class="email-filter-count">{counts.get("draft", 0)}</span></button>
</div>
<div class="email-ledger-wrap">
  <div class="email-ledger-head" aria-hidden="true"><span>Researcher</span><span>Subject</span><span>State</span><span>Date</span></div>
  <div class="email-ledger" id="emailGrid" aria-live="polite"></div>
</div>
</div>'''


def _render_email_script() -> str:
    return r'''<script>
(function() {
  var activeEmailFilter = "all";
  function stateLabel(r) {
    if (r.state === "replied") return "Replied · send questions";
    if (r.state === "sent") return "Sent · awaiting reply";
    return "Draft · unsent";
  }
  function copyLabel(r) {
    if (r.copy_kind === "exact_sent") return "Exact sent copy";
    if (r.copy_kind === "partial_sent") return "Visible sent fragment";
    if (r.state === "draft") return "Personalized draft";
    return "Stored personalized draft";
  }
  function copyText(r) {
    // "Copy unavailable" read as data loss when it usually means the opposite:
    // nobody drafted it, deliberately, because a quality gate held it. Say which.
    return r.exact_sent_copy || r.draft_body || r.visible_sent_fragment
      || (r.notes ? "Not drafted — held. " + r.notes : "Not drafted, and no reason recorded.");
  }
  function compactState(r) {
    if (r.state === "replied") return "Replied";
    if (r.state === "sent") return "Sent";
    return "Draft";
  }
  function row(r, idx) {
    var date = r.reply_at || r.sent_at || "Not sent";
    return '<article class="email-row" data-state="' + esc(r.state) + '">' +
      '<button class="email-researcher-btn" type="button" data-email-open="' + idx + '" aria-label="Open outreach record for ' + esc(r.name) + '"><strong>' + esc(r.name) + '</strong><span>' + esc(r.company) + (r.role ? ' · ' + esc(r.role) : '') + '</span>' + (r.email ? '<span class="email-row-addr">' + esc(r.email) + '</span>' : '') + '</button>' +
      '<div class="email-row-subject"><span class="email-row-subject-text" title="' + esc(r.sent_subject || r.draft_subject || "Subject unavailable") + '">' + esc(r.sent_subject || r.draft_subject || "Subject unavailable") + '</span>' + (r.paper_url ? '<a class="email-row-paper" href="' + esc(r.paper_url) + '" target="_blank" rel="noopener" onclick="event.stopPropagation()" title="Open the paper">' + esc(r.paper_note || "paper") + ' \u2197</a>' : '') + '</div>' +
      '<span class="email-state">' + esc(compactState(r)) + '</span>' +
      '<time class="email-row-date">' + esc(date) + '</time>' +
      '</article>';
  }
  function threadItem(kind, title, meta, text, copyKind, warning) {
    if (!text) return '';
    var copy = copyKind
      ? '<button class="email-copy-btn" type="button" data-thread-copy="' + esc(copyKind) + '">Copy</button>'
      : '';
    var warningHtml = warning ? '<p class="email-unsent-warning">' + esc(warning) + '</p>' : '';
    return '<details class="email-thread-item ' + esc(kind) + '"><summary><span class="email-thread-main"><strong>' + esc(title) + '</strong><span>' + esc(meta) + '</span></span><span class="email-thread-action" aria-hidden="true"></span></summary>' +
      warningHtml + '<div class="email-thread-copy"><pre>' + esc(text) + '</pre>' + copy + '</div></details>';
  }
  var lastEmailFocus = null;
  function modalRecord(r, idx) {
    var profile = r.profile_url
      ? '<a href="' + esc(r.profile_url) + '" target="_blank" rel="noopener">Profile ↗</a>'
      : '';
    var paper = r.paper_url
      ? '<div class="email-paper"><b>Paper</b><a href="' + esc(r.paper_url) + '" target="_blank" rel="noopener">' + esc(r.paper_note || "Open source") + ' ↗</a></div>'
      : '';
    var meta = r.sent_at
      ? '<span>Sent ' + esc(r.sent_at) + '</span><span>from ' + esc(r.sent_account || "founder account") + '</span>'
      : '<span>Not sent</span><span>approval pending</span>';
    var altSubject = r.sent_subject && r.draft_subject && r.sent_subject !== r.draft_subject
      ? '<div class="email-subject-alt">Stored draft subject: ' + esc(r.draft_subject) + '</div>'
      : '';
    var note = '';
    if (r.copy_kind === "stored_draft" && r.state !== "draft") {
      note = '<p class="email-copy-note">The screenshot confirms delivery, but not the full sent body. This is the stored personalized draft, not claimed as exact sent copy.</p>';
    } else if (r.copy_kind === "partial_sent") {
      note = '<p class="email-copy-note">Only the fragment visible in the screenshot is archived; missing text was not reconstructed.</p>';
    }
    var text = copyText(r);
    var sentKind = r.state === "draft" ? "unsent" : "sent";
    var sentTitle = r.state === "draft" ? "Personalized draft · unsent" : copyLabel(r);
    var sentMeta = r.sent_at ? "You sent this · " + r.sent_at : "Approval pending";
    var sentWarning = r.state === "draft" ? "This message has not been sent." : "";
    var sentThread = threadItem(sentKind, sentTitle, sentMeta, text, "sent", sentWarning);
    var replyThread = threadItem("received", "Matthew replied", r.reply_at || "Date unavailable", r.reply_body, "", "");
    var nextThread = threadItem("unsent", "Proposed questions · unsent", "Pending founder approval", r.next_draft_body, "next", "Draft only. This has not been sent to the recipient.");
    return '<div class="email-modal-top"><div class="email-modal-title"><span class="email-state" style="--email-state:' + (r.state === "replied" ? "#22c55e" : r.state === "sent" ? "#60a5fa" : "#94a3b8") + '">' + esc(stateLabel(r)) + '</span><h3 id="emailModalName">' + esc(r.name) + '</h3><p>' + esc(r.role) + ' · ' + esc(r.company) + '</p></div><button class="email-modal-close" id="emailModalClose" type="button" aria-label="Close researcher record">×</button></div>' +
      '<div class="email-modal-content"><div class="email-modal-links"><a href="mailto:' + esc(r.email) + '">' + esc(r.email) + '</a>' + profile + '</div>' +
      paper +
      '<div class="email-subject">' + esc(r.sent_subject || r.draft_subject || "Subject unavailable") + '</div>' + altSubject +
      '<div class="email-modal-meta"><div><b>Delivery</b>' + meta + '</div><div><b>Record</b><span>' + esc(r.target_id) + ' / ' + esc(r.draft_id) + '</span></div></div>' +
      '<div class="email-thread"><div class="email-thread-title">Email thread</div>' + sentThread + replyThread + nextThread + '</div>' + note + '</div>';
  }
  function closeEmailModal() {
    var modal = document.getElementById("emailModal");
    if (!modal || modal.hidden) return;
    modal.hidden = true;
    document.body.style.overflow = "";
    if (lastEmailFocus) lastEmailFocus.focus();
  }
  function openEmailModal(idx) {
    var r = EMAIL_CAMPAIGN[idx];
    var modal = document.getElementById("emailModal");
    var body = document.getElementById("emailModalBody");
    if (!r || !modal || !body) return;
    lastEmailFocus = document.activeElement;
    body.innerHTML = modalRecord(r, idx);
    modal.hidden = false;
    document.body.style.overflow = "hidden";
    var close = document.getElementById("emailModalClose");
    close.addEventListener("click", closeEmailModal);
    close.focus();
    body.querySelectorAll("[data-thread-copy]").forEach(function(copy) {
      copy.addEventListener("click", function() {
        var value = copy.dataset.threadCopy === "next" ? r.next_draft_body : copyText(r);
        navigator.clipboard.writeText(value).then(function() {
          copy.textContent = "Copied";
          setTimeout(function() { copy.textContent = "Copy"; }, 1200);
        });
      });
    });
  }
  function renderEmail() {
    var rows = EMAIL_CAMPAIGN.filter(function(r) { return activeEmailFilter === "all" || r.state === activeEmailFilter; });
    var grid = document.getElementById("emailGrid");
    if (!grid) return;
    grid.innerHTML = rows.length ? rows.map(function(r) { return row(r, EMAIL_CAMPAIGN.indexOf(r)); }).join("") : '<div class="email-empty">No messages in this state.</div>';
    grid.querySelectorAll("[data-email-open]").forEach(function(btn) {
      btn.addEventListener("click", function() { openEmailModal(Number(btn.dataset.emailOpen)); });
    });
  }
  document.querySelectorAll("[data-email-filter]").forEach(function(btn) {
    btn.addEventListener("click", function() {
      document.querySelectorAll("[data-email-filter]").forEach(function(b) { b.classList.remove("active"); });
      btn.classList.add("active");
      activeEmailFilter = btn.dataset.emailFilter;
      renderEmail();
    });
  });
  var emailModal = document.getElementById("emailModal");
  if (emailModal) emailModal.addEventListener("click", function(event) {
    if (event.target === emailModal) closeEmailModal();
  });
  document.addEventListener("keydown", function(event) {
    if (event.key === "Escape") closeEmailModal();
  });
  window.openEmailThreadByContact = function(contactId) {
    var idx = EMAIL_CAMPAIGN.findIndex(function(r) { return r.contact_id === contactId; });
    if (idx >= 0) openEmailModal(idx);
  };
  window.openEmailThreadByTarget = function(targetId) {
    var idx = EMAIL_CAMPAIGN.findIndex(function(r) { return r.target_id === targetId; });
    if (idx >= 0) openEmailModal(idx);
  };
  renderEmail();
  var requestedThread = new URLSearchParams((location.hash.split("?")[1] || "")).get("email");
  if (requestedThread) setTimeout(function() { window.openEmailThreadByTarget(requestedThread); }, 0);
})();
</script>'''


TAB_CSS = """
/* ─── tab nav ─── */
.tab-nav {
  display:flex;gap:2px;
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:var(--r-md);
  padding:4px;margin-bottom:20px;
  width:fit-content;
}
.tab-nav button {
  background:transparent;border:none;
  color:var(--text-dim);cursor:pointer;
  padding:8px 18px;border-radius:6px;
  font:inherit;font-size:12px;font-weight:600;letter-spacing:0.02em;
  transition:all 0.15s ease;
}
.tab-nav button:hover {color:var(--text);}
.tab-nav button.active {
  background:var(--surface-3);color:var(--accent);
}
.tab-nav .count {
  display:inline-block;
  background:var(--surface-3);
  color:var(--text-dim);
  padding:1px 7px;border-radius:99px;
  font-size:10px;font-weight:600;
  margin-left:6px;vertical-align:1px;
}
.tab-nav button.active .count {
  background:rgba(245,206,74,0.15);color:var(--accent);
}
.tab-panel {display:none;}
.tab-panel.active {display:block;}
"""


def _render_tab_scripts() -> str:
    """Tab switching for the whole dashboard.

    This used to live inside the Company Intel script block. That tab is gone,
    but switchTab drives Thesis / Pain Patterns / Offerings / Contacts too, so
    it lives on its own now rather than inside any one tab's code.
    """
    return '''<script>
function switchTab(name) {
  document.querySelectorAll('.tab-nav button').forEach(b => b.classList.toggle('active', b.dataset.tab === name));
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.toggle('active', p.dataset.tab === name));
  history.replaceState(null, '', '#' + name);
}
window.addEventListener('hashchange', () => {
  const t = (location.hash || '#contacts').slice(1).split('?')[0];
  if (['tasks','contacts','companies','email','patterns','thesis','offerings'].includes(t)) switchTab(t);
});
['tasks','companies','email','patterns','thesis','offerings'].forEach(n => {
  if (location.hash.startsWith('#' + n)) switchTab(n);
});

function switchToContacts(cid) {
  switchTab('contacts');
  setTimeout(() => {
    const el = document.getElementById('contact-' + cid);
    if (el) el.scrollIntoView({behavior:'smooth', block:'center'});
  }, 50);
}

/* Assumption lineage chips: open the target card and walk the eye to it.
   Delegated, so it survives any future re-render of the thesis tab. */
document.addEventListener('click', (e) => {
  const chip = e.target.closest('.hx-linchip[data-goto]');
  if (!chip) return;
  const el = document.getElementById('hx-a-' + chip.dataset.goto);
  if (!el) return;
  el.open = true;
  el.scrollIntoView({behavior:'smooth', block:'center'});
  el.classList.remove('hx-lin-target');
  void el.offsetWidth;               /* restart the animation if re-clicked */
  el.classList.add('hx-lin-target');
});
</script>'''


def parse_evidence_md(path: Path) -> tuple[list[dict], list[dict]]:
    """Return (patterns, entries) from the two yaml blocks in evidence.md."""
    if not path.exists() or not _HAS_YAML:
        return [], []
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```yaml\n(.*?)```", text, re.S)
    patterns: list[dict] = []
    entries: list[dict] = []
    for block in blocks:
        try:
            data = yaml.safe_load(block) or {}
        except yaml.YAMLError as e:
            print(f"[warn] evidence.md yaml block failed to parse: {e}", file=sys.stderr)
            continue
        if isinstance(data, dict):
            patterns.extend(data.get("patterns") or [])
            entries.extend(data.get("entries") or [])
    return patterns, entries


_CID_RE = re.compile(r"\((C\d+)\)")


def tier_side_map(assumptions: list[dict]) -> dict[str, str]:
    """tier name -> structural side, from every assumption's `icp_valid_tiers`.

    Tier NAMES are idea-defined (schemas/assumptions.md); only the side vocabulary
    (vocab:tier_side) is global, so this is the one place a tier becomes routable.
    """
    out: dict[str, str] = {}
    for a in assumptions or []:
        for tier in a.get("icp_valid_tiers") or []:
            if isinstance(tier, dict):
                name, side = tier.get("name"), tier.get("side")
                if name and side:
                    out.setdefault(str(name).strip(), str(side).strip())
    return out


def compute_pattern_stats(
    patterns: list[dict],
    entries: list[dict],
    contacts: list[dict],
    sides_by_tier: dict[str, str] | None = None,
) -> tuple[list[dict], list[dict]]:
    """Score each pattern from its tagged entries. Returns (scored, untagged_entries).

    A pattern reported from more than one structural SIDE of the market (demand vs
    supply vs …) is stronger than the same count of sightings from one side, so the
    contact's tier is resolved to its declared side before counting.
    """
    sides_by_tier = sides_by_tier or {}
    env_by_cid = {}
    for c in contacts:
        tier = (c.get("tier") or "").strip()
        env_by_cid[c.get("id")] = sides_by_tier.get(tier, tier)
    name_by_cid = {c.get("id"): (c.get("name") or "").strip() for c in contacts}

    # entries carrying a P4 tag are "already-built workaround" sightings — the
    # strongest Mom Test signal short of payment, so any pattern sharing one
    # inherits the bonus.
    workaround_eids = {e.get("id") for e in entries if "P4" in (e.get("pain_pattern") or [])}

    scored = []
    for p in patterns:
        pid = p.get("id")
        mine = [e for e in entries if pid in (e.get("pain_pattern") or [])]
        if not mine:
            continue
        cids, by_env = [], {}
        for e in mine:
            m = _CID_RE.search(str(e.get("source") or ""))
            cid = m.group(1) if m else None
            if cid:
                if cid not in cids:
                    cids.append(cid)
                env = env_by_cid.get(cid) or "unknown"
                by_env.setdefault(env, []).append(e.get("id"))
        verdicts = {"supports": 0, "contradicts": 0, "ambiguous": 0}
        for e in mine:
            v = (e.get("verdict") or "ambiguous").strip()
            if v in verdicts:
                verdicts[v] += 1
        confs = [e.get("confidence") for e in mine if isinstance(e.get("confidence"), int)]
        unprompted = sum(1 for e in mine if e.get("unprompted") is True)
        sides = [k for k in by_env if k != "unknown"]
        cross_side = len(sides) >= 2
        has_workaround = any(e.get("id") in workaround_eids for e in mine)

        terms = [
            ("independent sources", len(cids), 2, 2 * len(cids)),
            ("cross-side", 1 if cross_side else 0, 3, 3 if cross_side else 0),
            ("built workaround", 1 if has_workaround else 0, 3, 3 if has_workaround else 0),
            ("unprompted", unprompted, 1, unprompted),
            ("contradicting", verdicts["contradicts"], -2, -2 * verdicts["contradicts"]),
        ]
        scored.append({
            **p,
            "entries": mine,
            "contact_ids": cids,
            "contact_names": [name_by_cid.get(c, c) for c in cids],
            "by_env": by_env,
            "verdicts": verdicts,
            "mean_confidence": round(sum(confs) / len(confs), 1) if confs else None,
            "unprompted": unprompted,
            "cross_side": cross_side,
            "has_workaround": has_workaround,
            "terms": terms,
            "strength": sum(t[3] for t in terms),
        })

    scored.sort(key=lambda s: (-s["strength"], s["id"]))
    untagged = [e for e in entries if not (e.get("pain_pattern") or [])]
    return scored, untagged


def render_patterns_tab(scored: list[dict], untagged: list[dict], entry_total: int,
                        side_order: list[str] | None = None) -> str:
    if not scored:
        return ('<div class="empty-state" role="status"><p>No tagged evidence yet. '
                'Add <code>pain_pattern:</code> tags to entries in '
                '<code>03-validation/evidence.md</code>.</p></div>')

    max_strength = max(s["strength"] for s in scored) or 1
    side_order = side_order or ["demand", "supply", "competitor", "expert"]
    seen = [k for k in side_order if any(k in s["by_env"] for s in scored)]
    extra = sorted({k for s in scored for k in s["by_env"]}
                   - set(side_order) - {"unknown", ""})
    envs_present = seen + extra
    env_label = {k: k.replace("_", " ") for k in envs_present}

    out = []

    # ── the exchange matrix ──
    out.append('<section class="pat-exchange">')
    out.append('<h2>The exchange</h2>')
    out.append(
        '<p class="pat-lede">Columns are the structural <strong>sides</strong> of this '
        'market, resolved from each contact\'s tier via <code>icp_valid_tiers</code> in '
        '<code>02-assumptions/graph.md</code>. Highlighted rows are reported from more '
        'than one column.</p>')
    out.append('<div class="pat-matrix-wrap"><table class="pat-matrix"><thead><tr><th>pattern</th>')
    for k in envs_present:
        out.append(f'<th>{escape(env_label[k])}<span class="pat-envkey">{escape(k)}</span></th>')
    out.append('<th class="pat-th-num">sources</th></tr></thead><tbody>')
    for s in scored:
        cls = " pat-row-cross" if s["cross_side"] else ""
        cut = ' <span class="pat-cuts">cuts against</span>' if s.get("cuts_against") else ""
        out.append(f'<tr class="pat-mrow{cls}"><td class="pat-mname">'
                   f'<span class="pat-pid">{escape(str(s["id"]))}</span> '
                   f'{escape(str(s.get("name", "")))}{cut}</td>')
        for k in envs_present:
            eids = s["by_env"].get(k) or []
            if eids:
                out.append(f'<td class="pat-cell pat-cell-on" title="{escape(", ".join(eids))}">'
                           f'{len(eids)}</td>')
            else:
                out.append('<td class="pat-cell">&middot;</td>')
        out.append(f'<td class="pat-th-num">{len(s["contact_ids"])}</td></tr>')
    out.append('</tbody></table></div></section>')

    # ── ranked pattern cards ──
    out.append('<section class="pat-cards"><h2>What repeats</h2>')
    out.append(f'<p class="pat-lede">{len(scored)} patterns across {entry_total} evidence '
               f'entries. Ranked by strength: <code>2&times;sources + 3&times;cross-side + '
               f'3&times;built-workaround + unprompted &minus; 2&times;contradicting</code>.</p>')

    for rank, s in enumerate(scored, 1):
        badges = []
        if s["cross_side"]:
            badges.append('<span class="pat-badge pat-badge-cross">both sides</span>')
        if s["has_workaround"]:
            badges.append('<span class="pat-badge pat-badge-work">workaround built</span>')
        if s.get("cuts_against"):
            badges.append('<span class="pat-badge pat-badge-cut">cuts against us</span>')
        if len(s["contact_ids"]) < 2:
            badges.append('<span class="pat-badge pat-badge-thin">single source</span>')
        flipped = ("cuts_against_data_frame" in s
                   and bool(s.get("cuts_against")) != bool(s.get("cuts_against_data_frame")))
        if flipped:
            badges.append('<span class="pat-badge pat-badge-flip">sign flipped</span>')

        v = s["verdicts"]
        pct = int(100 * s["strength"] / max_strength) if max_strength else 0
        # These three are built outside the f-string on purpose: nesting the same
        # quote character inside a replacement field needs Python 3.12 (PEP 701),
        # and the documented invocation is plain `python3`, which is 3.9 on macOS.
        cut_cls = " pat-card-cut" if s.get("cuts_against") else ""
        flip_lbl = ("Under the services frame &mdash; SIGN FLIPPED."
                    if flipped else "Under the services frame.")
        flip_html = ""
        if s.get("services_reading"):
            flip_html = ('<div class="pat-flip"><b>' + flip_lbl + "</b> "
                         + escape(str(s.get("services_reading", "")).strip()) + "</div>")
        out.append(f'''<article class="pat-card{cut_cls}">
  <div class="pat-head">
    <span class="pat-rank">{rank}</span>
    <div class="pat-title">
      <h3><span class="pat-pid">{escape(str(s["id"]))}</span> {escape(str(s.get("name", "")))}</h3>
      <div class="pat-badges">{"".join(badges)}</div>
    </div>
    <div class="pat-strength">
      <span class="pat-strength-num">{s["strength"]}</span>
      <span class="pat-strength-lbl">strength</span>
    </div>
  </div>
  <div class="pat-bar"><span style="width:{max(pct, 2)}%"></span></div>
  <p class="pat-statement">{escape(str(s.get("statement", "")).strip())}</p>
  <p class="pat-why"><strong>Why it matters.</strong> {escape(str(s.get("why_it_matters", "")).strip())}</p>
  {flip_html}
  <div class="pat-stats">
    <span><b>{len(s["contact_ids"])}</b> sources</span>
    <span><b>{len(s["entries"])}</b> entries</span>
    <span><b>{s["unprompted"]}</b> unprompted</span>
    <span><b>{s["mean_confidence"] if s["mean_confidence"] is not None else "&ndash;"}</b> mean conf</span>
    <span class="pat-v"><b class="v-sup">{v["supports"]}</b> supports
      <b class="v-con">{v["contradicts"]}</b> contradicts
      <b class="v-amb">{v["ambiguous"]}</b> ambiguous</span>
  </div>
  <div class="pat-math">{" ".join(
      f'<span class="{"pat-t-neg" if t[3] < 0 else ""}">{escape(t[0])} {t[1]}&times;{t[2]} = {t[3]:+d}</span>'
      for t in s["terms"])}</div>
  <details class="pat-ev">
    <summary>{len(s["entries"])} evidence entries &mdash; {escape(", ".join(s["contact_names"]))}</summary>
    <ul>''')
        for e in s["entries"]:
            m = _CID_RE.search(str(e.get("source") or ""))
            cid = m.group(1) if m else "?"
            src = str(e.get("source") or "").split("—")[0].strip()
            vd = (e.get("verdict") or "").strip()
            claim = " ".join(str(e.get("claim") or "").split())
            unp = ' <span class="pat-unp">unprompted</span>' if e.get("unprompted") else ""
            conf = escape(str(e.get("confidence", "")))  # extracted: see PEP 701 note above
            out.append(f'<li><div class="pat-ev-meta"><code>{escape(str(e.get("id")))}</code> '
                       f'<span class="pat-ev-src">{escape(src)} ({escape(cid)})</span> '
                       f'<span class="pat-vd pat-vd-{escape(vd)}">{escape(vd)}</span>'
                       f'<span class="pat-conf">conf {conf}</span>'
                       f'{unp}</div><blockquote>{escape(claim)}</blockquote></li>')
        out.append('</ul></details></article>')
    out.append('</section>')

    # ── gaps ──
    thin = [s for s in scored if len(s["contact_ids"]) < 2]
    out.append('<section class="pat-gaps"><h2>Where the pattern layer is thin</h2><ul>')
    if thin:
        out.append('<li><b>Single-source patterns</b> — not yet patterns, just one person '
                   'saying something twice: ' +
                   escape(", ".join(f'{s["id"]} ({s["contact_names"][0] if s["contact_names"] else "?"})'
                                    for s in thin)) + '.</li>')
    missing = [k.replace("_", " ") for k in side_order if k not in envs_present]
    if missing:
        out.append('<li><b>Sides with no evidence at all</b> &mdash; ' +
                   escape(", ".join(missing)) + '. Nothing they feel is in this view.</li>')
    if untagged:
        out.append(f'<li><b>{len(untagged)} untagged entries</b> &mdash; ' +
                   escape(", ".join(str(e.get("id")) for e in untagged)) +
                   '. Engagement and methodology signals, not pain claims.</li>')
    out.append('</ul></section>')
    return "\n".join(out)


PATTERNS_CSS = """
.pat-exchange, .pat-cards, .pat-gaps { margin: 0 0 30px; }
.pat-exchange h2, .pat-cards h2, .pat-gaps h2 {
  font-size: 15px; letter-spacing: .02em; margin: 0 0 8px; }
.pat-lede { color: var(--text-dim); font-size: 13px; line-height: 1.6;
  max-width: 76ch; margin: 0 0 16px; }
.pat-lede code { font-size: 11.5px; color: var(--text); }
.pat-matrix-wrap { overflow-x: auto; }
.pat-matrix { border-collapse: collapse; width: 100%; font-size: 12.5px; }
.pat-matrix th { text-align: left; padding: 8px 10px; color: var(--text-dim);
  font-weight: 500; border-bottom: 1px solid var(--border); vertical-align: bottom; }
.pat-matrix th span.pat-envkey { display: block; font-size: 10px;
  color: var(--text-dimmer); font-family: ui-monospace, monospace; }
.pat-th-num { text-align: center !important; }
.pat-matrix td { padding: 9px 10px; border-bottom: 1px solid var(--border-subtle); }
.pat-mname { white-space: nowrap; }
.pat-pid { font-family: ui-monospace, monospace; color: var(--accent); font-size: 11.5px; }
.pat-cell { text-align: center; color: var(--text-dimmer); }
.pat-cell-on { color: var(--text); font-weight: 600; background: rgba(245,206,74,.07); }
.pat-row-cross .pat-mname { color: var(--accent); }
.pat-row-cross td { background: rgba(245,206,74,.04); }
.pat-cuts { font-size: 10px; color: var(--red); border: 1px solid var(--red);
  border-radius: 3px; padding: 0 4px; margin-left: 6px; }
.pat-card { border: 1px solid var(--border); border-radius: var(--r-md);
  background: var(--surface); padding: 16px 18px; margin: 0 0 12px; }
.pat-card-cut { border-color: rgba(239,68,68,.35); }
.pat-head { display: flex; align-items: flex-start; gap: 12px; }
.pat-rank { font-size: 12px; color: var(--text-dimmer); font-family: ui-monospace, monospace;
  border: 1px solid var(--border); border-radius: 4px; padding: 1px 6px; margin-top: 2px; }
.pat-title { flex: 1; min-width: 0; }
.pat-title h3 { font-size: 14px; margin: 0 0 5px; font-weight: 600; }
.pat-badges { display: flex; flex-wrap: wrap; gap: 5px; }
.pat-badge { font-size: 10px; border-radius: 3px; padding: 1px 6px; border: 1px solid; }
.pat-badge-cross { color: var(--accent); border-color: rgba(245,206,74,.5);
  background: rgba(245,206,74,.1); }
.pat-badge-work { color: var(--green); border-color: rgba(34,197,94,.5); }
.pat-badge-cut { color: var(--red); border-color: rgba(239,68,68,.5); }
.pat-badge-thin { color: var(--text-dimmer); border-color: var(--border); }
.pat-strength { text-align: right; }
.pat-strength-num { display: block; font-size: 20px; font-weight: 600; line-height: 1; }
.pat-strength-lbl { font-size: 10px; color: var(--text-dimmer); }
.pat-bar { height: 3px; background: var(--border-subtle); border-radius: 2px;
  margin: 12px 0 12px; overflow: hidden; }
.pat-bar span { display: block; height: 100%; background: var(--accent); }
.pat-statement { font-size: 13.5px; line-height: 1.65; margin: 0 0 10px; }
.pat-why { font-size: 12.5px; line-height: 1.6; color: var(--text-dim); margin: 0 0 12px;
  max-width: 82ch; }
.pat-why strong { color: var(--text); }
.pat-stats { display: flex; flex-wrap: wrap; gap: 16px; font-size: 11.5px;
  color: var(--text-dim); padding-top: 10px; border-top: 1px solid var(--border-subtle); }
.pat-stats b { color: var(--text); }
.v-sup { color: var(--green) !important; } .v-con { color: var(--red) !important; }
.v-amb { color: var(--yellow) !important; }
.pat-math { display: flex; flex-wrap: wrap; gap: 10px; font-size: 10.5px;
  font-family: ui-monospace, monospace; color: var(--text-dimmer); margin-top: 8px; }
.pat-t-neg { color: var(--red); }
.pat-ev { margin-top: 12px; }
.pat-ev summary { cursor: pointer; font-size: 12px; color: var(--text-dim); }
.pat-ev summary:hover { color: var(--text); }
.pat-ev ul { list-style: none; padding: 0; margin: 10px 0 0; }
.pat-ev li { border-left: 2px solid var(--border); padding: 0 0 0 12px; margin: 0 0 12px; }
.pat-ev-meta { display: flex; flex-wrap: wrap; gap: 8px; align-items: center;
  font-size: 10.5px; color: var(--text-dimmer); margin-bottom: 4px; }
.pat-ev-meta code { color: var(--accent); }
.pat-ev-src { color: var(--text-dim); }
.pat-vd { border-radius: 3px; padding: 0 5px; border: 1px solid var(--border); }
.pat-vd-supports { color: var(--green); border-color: rgba(34,197,94,.4); }
.pat-vd-contradicts { color: var(--red); border-color: rgba(239,68,68,.4); }
.pat-vd-ambiguous { color: var(--yellow); border-color: rgba(245,158,11,.4); }
.pat-unp { color: var(--accent); }
.pat-ev blockquote { margin: 0; font-size: 12.5px; line-height: 1.6; color: var(--text-dim); }
.pat-gaps ul { margin: 0; padding-left: 18px; font-size: 12.5px; line-height: 1.8;
  color: var(--text-dim); max-width: 84ch; }
.pat-gaps b { color: var(--text); }
"""


# ─── thesis + offerings ──────────────────────────────────────────────────────
#
# Unified 2026-08-06. Previously the founder had two artifacts — a hand-written
# control-room.html (belief, hunch, assumptions) and this generated tracker
# (contacts, intel). Keeping the thesis in one file and the evidence for it in
# another meant the two could disagree silently, which is exactly the failure
# this repo is built to avoid. One file now, tabs in pipeline order:
#
#   Thesis  →  Pain Patterns  →  Offerings  →  Contacts  →  Company Intel
#   (what we believe) (what repeats) (what we'd sell) (who we asked) (who they are)


def parse_graph_md(path: Path) -> tuple[dict, list[dict]]:
    """Return (frontmatter, assumptions) from 02-assumptions/graph.md."""
    if not path.exists() or not _HAS_YAML:
        return {}, []
    text = path.read_text(encoding="utf-8")
    fm: dict = {}
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            try:
                fm = yaml.safe_load(text[3:end]) or {}
            except yaml.YAMLError:
                fm = {}
    # The body carries prose before the YAML, so slice from the `assumptions:` key.
    i = text.find("\nassumptions:")
    if i == -1:
        return fm, []
    try:
        data = yaml.safe_load(text[i:]) or {}
    except yaml.YAMLError as e:
        print(f"[warn] graph.md assumptions failed to parse: {e}", file=sys.stderr)
        return fm, []
    return fm, (data.get("assumptions") or [])


def parse_offerings_md(path: Path) -> tuple[dict, list[dict]]:
    """Return (frontmatter, offerings) from 04-mutation/offerings.md."""
    if not path.exists() or not _HAS_YAML:
        return {}, []
    text = path.read_text(encoding="utf-8")
    fm: dict = {}
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            try:
                fm = yaml.safe_load(text[3:end]) or {}
            except yaml.YAMLError:
                fm = {}
    blocks = re.findall(r"```yaml\n(.*?)```", text, re.S)
    for b in blocks:
        try:
            data = yaml.safe_load(b) or {}
        except yaml.YAMLError as e:
            print(f"[warn] offerings.md yaml failed to parse: {e}", file=sys.stderr)
            continue
        if isinstance(data, dict) and data.get("offerings"):
            return fm, data["offerings"]
    return fm, []


def _extract_belief(path: Path) -> str:
    """Pull the founder-confirmed belief — the first blockquote under `# Belief`."""
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    m = re.search(r"(?m)^# Belief\s*\n+((?:> .*\n)+)", text)
    if not m:
        return ""
    return " ".join(l.lstrip("> ").strip() for l in m.group(1).splitlines()).strip()


_BELIEF_SECTIONS = [
    ("boundaries", "Belief boundaries", "Where it stops — boundaries & precedent"),
    ("how", "How the founder states it", "In the founder's words"),
    ("sisp", "Starting point and SISP check", "Starting point & what must be tested independently"),
    ("threats", "What would threaten the belief itself", "What would kill the belief"),
]


def _extract_belief_sections(path: Path) -> list[tuple[str, str]]:
    """(display title, raw section text) for each belief.md section that exists.

    Rendering, not authoring: belief.md stays the single author; the tab shows it.
    """
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    out = []
    for _key, heading, title in _BELIEF_SECTIONS:
        m = re.search(rf"(?m)^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)", text, re.S)
        if m and m.group(1).strip():
            out.append((title, m.group(1).strip()))
    return out


_INLINE_BOLD = re.compile(r"\*\*(.+?)\*\*")
_INLINE_CODE = re.compile(r"`([^`]+)`")
_INLINE_LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")


def _inline_finish(e: str) -> str:
    """Re-inject inline markdown into ALREADY-ESCAPED text. Applied after folded
    lines are joined — bold that spans a soft line break never pairs per-line."""
    e = _INLINE_BOLD.sub(r"<strong>\1</strong>", e)
    e = _INLINE_CODE.sub(r"<code>\1</code>", e)
    e = _INLINE_LINK.sub(r'<a href="\2">\1</a>', e)
    return e


def _inline_md(s: str) -> str:
    return _inline_finish(escape(s))


def _md_lite(block: str) -> str:
    """Escape + minimally structure a markdown block: bullets, sub-headings, paragraphs."""
    html, bullets, para = [], [], []
    def flush_b():
        if bullets:
            html.append("<ul>" + "".join(
                f"<li>{_inline_finish(b)}</li>" for b in bullets) + "</ul>")
            bullets.clear()
    def flush_p():
        if para:
            html.append(f"<p>{_inline_finish(' '.join(para))}</p>")
            para.clear()
    for raw in block.splitlines():
        line = raw.rstrip()
        s = line.strip()
        if not s:
            flush_b(); flush_p(); continue
        e = escape(s.lstrip("-# ").strip())
        if s.startswith("### ") or s.startswith("#### "):
            flush_b(); flush_p(); html.append(f"<h4>{e}</h4>")
        elif s.startswith("- "):
            flush_p()
            if raw.startswith(("  ", "\t")) and bullets:
                bullets[-1] += f"<ul><li>{e}</li></ul>"
            else:
                bullets.append(e)
        else:
            if bullets and raw.startswith(("  ", "\t")):
                bullets[-1] += " " + e
            else:
                flush_b(); para.append(e)
    flush_b(); flush_p()
    return "".join(html)


def parse_lineage_md(path: Path) -> tuple[dict, list[dict]]:
    """Return (frontmatter, hunches) from 01-ideation/hunch-lineage.md.

    Deliberately a light regex parse, not YAML — the lineage file is prose-first
    by design (it has to be readable as a narrative) and only its leading
    key: value lines under each `## H{n}` heading are structured.
    """
    if not path.exists():
        return {}, []
    text = path.read_text(encoding="utf-8")
    fm: dict = {}
    if text.startswith("---") and _HAS_YAML:
        end = text.find("---", 3)
        if end != -1:
            try:
                fm = yaml.safe_load(text[3:end]) or {}
            except yaml.YAMLError:
                fm = {}
    hunches = []
    for m in re.finditer(r"(?m)^## (H\d+)(?: —.*)?$", text):
        hid = m.group(1)
        nxt = text.find("\n## ", m.end())
        block = text[m.end(): nxt if nxt != -1 else len(text)]
        def field(k, default=""):
            fm_ = re.search(rf"(?m)^{k}:[ \t]*(.*)$", block)
            if not fm_:
                return default
            head = fm_.group(1).strip()
            # A YAML block scalar (`key: >`) carries its value in the indented body
            # below, not on the key line. Returning the folding indicator put a bare
            # ">" into BRIEF.md where the hunch statement belonged.
            if head in (">", "|", ">-", "|-", ">+", "|+"):
                body = []
                for line in block[fm_.end():].splitlines():
                    if line.strip() and not line.startswith((" ", "\t")):
                        break
                    body.append(line.strip())
                return " ".join(x for x in body if x)
            return head

        # The statement may be a blockquote or plain prose — the shotgun writes prose.
        # Take everything under `### Statement` up to the next heading and strip any
        # quote markers, rather than requiring them and silently yielding "".
        stmt = ""
        sm = re.search(r"(?m)^### Statement[ \t]*\n(.*?)(?=^\#{2,4} |\Z)", block, re.S)
        if not sm:
            sm = re.search(r"(?m)^((?:> .+\n?)+)", block)
        if sm:
            stmt = " ".join(l.lstrip("> ").strip()
                            for l in sm.group(1).strip().splitlines() if l.strip())
        comp = ""
        cm = re.search(r"(?m)^### Components\s*\n(.*?)(?=^### |\Z)", block, re.S)
        if cm:
            comp = cm.group(1).strip()
        hunches.append({
            "id": hid,
            "status": field("status", "unknown"),
            "created": field("created"),
            "parent": field("parent_hunch"),
            "change_reason": field("change_reason"),
            "superseded_by": field("superseded_by"),
            "statement": stmt,
            "components": comp,
        })
    hunches.sort(key=lambda h: h["id"])
    return fm, hunches


_STATUS_TONE = {
    "active": "good", "superseded": "dim", "retired": "dim", "proposed": "warn",
    "untested": "warn", "dormant": "dim", "validated": "good", "killed": "bad",
}


def _assumption_score_dots(label: str, value) -> str:
    """Render a 1-5 score as filled/empty dots. Returns '' for anything unscored,
    so a node with blank scores stays visually quiet rather than showing five empties."""
    try:
        n = int(value)
    except (TypeError, ValueError):
        return ""
    n = max(0, min(5, n))
    dots = "".join(f'<i class="{"on" if i < n else "off"}"></i>' for i in range(5))
    return (f'<span class="th-score"><span class="th-score-lbl">{escape(label)}</span>'
            f'<span class="th-dots">{dots}</span></span>')


_HX_ORDER = ["supports", "ambiguous", "contradicts"]
_HX_GLYPH = {"supports": "+", "ambiguous": "~", "contradicts": "−"}

HUNCH_CSS = """
/* ── Hunches tab ──────────────────────────────────────────────────────────
   Verdict scale is DIVERGING: two poles plus a neutral midpoint. Validated
   with the dataviz palette validator against this dashboard's surface
   (#14171c) — CVD deutan dE 12.7, normal-vision dE 22.2, all steps >= 3:1.
   The neutral is deliberately achromatic; a diverging midpoint that carries
   chroma reads as a third category. No status colour is ever load-bearing on
   its own: every tally prints glyph + number + word beside the bar. */
.hx-root {--hx-pos:#0ca30c;--hx-mid:#8b93a0;--hx-neg:#ef4444;}

.hx-belief {padding:15px 17px;border:1px solid var(--border);border-left:3px solid var(--accent);
  border-radius:10px;background:var(--surface);margin-bottom:14px;}
.hx-belief b {display:block;font-size:9.5px;text-transform:uppercase;letter-spacing:.12em;
  color:var(--text-dimmer);margin-bottom:7px;}
.hx-belief blockquote {margin:0 0 8px;font-size:15px;line-height:1.5;max-width:74ch;}
.hx-belief p {margin:0;font-size:11.5px;color:var(--text-dim);max-width:74ch;}

/* belief section pills + panels */
.hx-bnav {display:flex;flex-wrap:wrap;gap:6px;margin-top:10px;}
.hx-bpill {border:1px solid var(--border);background:var(--surface-2);color:var(--text-dim);
  font:inherit;font-size:10.5px;font-weight:700;letter-spacing:.03em;padding:4px 11px;
  border-radius:999px;cursor:pointer;transition:color .15s,border-color .15s;}
.hx-bpill:hover {color:var(--text);border-color:var(--accent);}
.hx-bpill.active {color:var(--accent);border-color:var(--accent);
  background:color-mix(in srgb,var(--accent) 9%,transparent);}
.hx-bpill:focus-visible {outline:1px solid var(--accent);outline-offset:2px;}
.hx-bpanel {margin-top:9px;padding:11px 13px;border:1px solid var(--border-subtle);
  border-radius:9px;background:var(--surface-2);font-size:12px;line-height:1.65;
  color:var(--text-dim);max-width:82ch;}
.hx-bpanel p {margin:0 0 8px;} .hx-bpanel p:last-child {margin-bottom:0;}
.hx-bpanel ul {margin:0 0 8px 18px;padding:0;} .hx-bpanel li {margin:0 0 5px;}
.hx-bpanel h4 {font-size:10.5px;text-transform:uppercase;letter-spacing:.07em;
  margin:10px 0 5px;color:var(--text);}
.hx-bpanel strong {color:var(--text);}
.hx-bpanel code {font-size:11px;color:var(--text);}

/* hunch components grid */
.hx-comp {margin:7px 0 3px;}
.hx-comp summary {font-size:10.5px;font-weight:700;color:var(--text-dim);cursor:pointer;
  list-style:none;letter-spacing:.03em;}
.hx-comp summary::before {content:"▸ ";color:var(--accent);}
.hx-comp[open] summary::before {content:"▾ ";}
.hx-comp summary:focus-visible {outline:1px solid var(--accent);outline-offset:2px;border-radius:3px;}
.hx-comp-body {padding:8px 0 2px;font-size:12px;line-height:1.6;color:var(--text-dim);}
.hx-reason {margin:0 0 9px;padding:8px 11px;border-left:2px solid var(--accent);
  background:color-mix(in srgb,var(--accent) 6%,transparent);border-radius:0 7px 7px 0;
  max-width:78ch;}
.hx-kv {display:grid;grid-template-columns:max-content minmax(0,1fr);gap:5px 16px;margin:0 0 9px;}
.hx-kv dt {font-size:9.5px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;
  color:var(--text-dimmer);padding-top:2px;white-space:nowrap;}
.hx-kv dd {margin:0;max-width:70ch;}
.hx-kv dd strong {color:var(--text);}
.hx-notes {border:1px dashed var(--border);border-radius:8px;padding:8px 11px;max-width:78ch;}
.hx-notes b {display:block;font-size:9.5px;text-transform:uppercase;letter-spacing:.08em;
  color:var(--yellow);margin-bottom:5px;}
.hx-notes ul {margin:0 0 0 16px;padding:0;} .hx-notes li {margin:0 0 5px;}
.hx-notes strong {color:var(--text);}
.hx-artifacts {margin:-4px 0 14px;font-size:11.5px;color:var(--text-dim);}
.hx-artifacts b {font-size:9.5px;text-transform:uppercase;letter-spacing:.1em;color:var(--text-dimmer);margin-right:8px;}
.hx-artifacts a {color:var(--text-dim);text-decoration:underline;text-decoration-color:var(--border);text-underline-offset:2px;}
.hx-artifacts a:hover {color:var(--accent);}

.hx-topstats {display:flex;flex-wrap:wrap;align-items:center;gap:7px 20px;margin-bottom:16px;
  font-size:11.5px;color:var(--text-dim);}
.hx-topstats b {color:var(--text);font-size:13px;font-variant-numeric:tabular-nums;}
.hx-warn {padding:9px 12px;border:1px solid var(--yellow);border-radius:8px;font-size:12px;
  color:var(--text-dim);margin:0 0 14px;background:color-mix(in srgb,var(--yellow) 8%,transparent);}
.hx-warn b {color:var(--text);}

.hx-grid {display:grid;grid-template-columns:repeat(auto-fit,minmax(440px,1fr));gap:16px;
  align-items:start;}
@media (max-width:980px) {.hx-grid {grid-template-columns:1fr;}}

.hx-hunch {background:var(--surface);border:1px solid var(--border);border-radius:12px;
  overflow:hidden;}
.hx-shared {margin-top:16px;background:var(--surface-2);}
.hx-hhead {padding:16px 16px 13px;border-bottom:1px solid var(--border);}
.hx-htitle {display:flex;align-items:center;gap:8px;margin-bottom:8px;}
.hx-hid {font-size:17px;font-weight:650;letter-spacing:-.01em;}
.hx-hstmt {margin:0 0 10px;font-size:12.5px;line-height:1.6;color:var(--text-dim);max-width:64ch;}
.hx-hstats {display:flex;flex-wrap:wrap;align-items:center;gap:6px 16px;font-size:11px;
  color:var(--text-dim);}
.hx-hstats b {color:var(--text);font-variant-numeric:tabular-nums;}

.hx-direct {padding:10px 16px;border-bottom:1px solid var(--border);background:var(--surface-2);}
.hx-direct>summary {cursor:pointer;font-size:11.5px;color:var(--text-dim);}
.hx-direct>summary:hover {color:var(--text);}
.hx-direct .hx-evlist {margin-top:11px;}

.hx-chip {display:inline-flex;align-items:center;padding:1px 7px;border-radius:999px;
  font-size:10px;font-weight:500;border:1px solid var(--border);color:var(--text-dim);
  white-space:nowrap;background:var(--surface-3);}
.hx-chip-active {border-color:var(--accent);color:var(--accent);background:transparent;}
.hx-chip-lof {border-color:var(--yellow);color:var(--yellow);background:transparent;}
.hx-chip-unp {border-color:var(--hx-pos);color:var(--hx-pos);background:transparent;}

.hx-a {border-bottom:1px solid var(--border);}
.hx-a:last-child {border-bottom:0;}
.hx-a-active {box-shadow:inset 3px 0 0 var(--accent);}
.hx-a>summary {list-style:none;cursor:pointer;padding:14px 30px 14px 16px;position:relative;
  display:block;}
.hx-a>summary::-webkit-details-marker {display:none;}
.hx-a>summary:hover {background:var(--surface-2);}
.hx-a>summary::after {content:"";position:absolute;right:14px;top:18px;width:7px;height:7px;
  border-right:1.5px solid var(--text-dimmer);border-bottom:1.5px solid var(--text-dimmer);
  transform:rotate(45deg);transition:transform .15s ease;}
.hx-a[open]>summary::after {transform:rotate(-135deg);}
.hx-ahead {display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin-bottom:6px;}
.hx-aid {font-size:12px;font-weight:650;font-variant-numeric:tabular-nums;}
.hx-rank {font-size:10px;color:var(--text-dimmer);font-variant-numeric:tabular-nums;}
.hx-aclaim {display:block;font-size:12.5px;line-height:1.55;margin-bottom:10px;max-width:66ch;}
.hx-afoot {display:flex;flex-wrap:wrap;align-items:center;gap:8px 13px;}

.hx-meter {display:inline-block;width:120px;flex:none;}
.hx-track {display:block;height:6px;border-radius:3px;background:var(--surface-3);overflow:hidden;}
.hx-fill {display:flex;height:100%;min-width:6px;gap:2px;}
.hx-seg {display:block;height:100%;}
.hx-seg:first-child {border-radius:3px 0 0 3px;}
.hx-seg:last-child {border-radius:0 3px 3px 0;}
.hx-seg:only-child {border-radius:3px;}
.hx-seg-supports {background:var(--hx-pos);}
.hx-seg-ambiguous {background:var(--hx-mid);}
.hx-seg-contradicts {background:var(--hx-neg);}
.hx-meter-none {width:auto;font-size:10.5px;color:var(--text-dimmer);font-style:italic;}

.hx-tallies {display:inline-flex;flex-wrap:wrap;gap:3px 10px;}
.hx-tally {display:inline-flex;align-items:center;gap:4px;font-size:10.5px;color:var(--text-dim);
  font-variant-numeric:tabular-nums;}
.hx-glyph {display:inline-grid;place-items:center;width:12px;height:12px;border-radius:3px;
  font-size:9px;font-weight:700;font-style:normal;color:#0b0d10;line-height:1;}
.hx-tally-supports .hx-glyph {background:var(--hx-pos);color:#fff;}
.hx-tally-ambiguous .hx-glyph {background:var(--hx-mid);}
.hx-tally-contradicts .hx-glyph {background:var(--hx-neg);color:#fff;}
.hx-tally-none {color:var(--text-dimmer);font-style:italic;}
.hx-scores {display:flex;gap:8px;margin-left:auto;}

.hx-adetail {padding:2px 16px 18px;background:var(--surface-2);border-top:1px solid var(--border);}

/* ── assumption lineage (DAG edges) ──
   Structure, not history. Chips are buttons because they act on this page
   (open + reveal the target) rather than navigating away. Direction is carried
   by the LABEL ("rests on" / "carries"), never by colour or arrow alone. */
.hx-lin {margin:12px 0 10px;display:flex;flex-direction:column;gap:6px;}
.hx-linrow {display:flex;align-items:center;flex-wrap:wrap;gap:8px;}
.hx-linlbl {
  font-size:9.5px;letter-spacing:.09em;text-transform:uppercase;
  color:var(--text-dimmer);font-weight:600;min-width:58px;
}
.hx-linchips {display:flex;flex-wrap:wrap;gap:6px;}
.hx-linchip {
  display:inline-flex;align-items:center;gap:6px;
  background:var(--surface-3);border:1px solid var(--border);
  color:var(--text);border-radius:99px;padding:3px 10px;
  font:inherit;font-size:11px;font-weight:650;
  font-variant-numeric:tabular-nums;cursor:pointer;
  transition:border-color .15s ease, background .15s ease;
}
.hx-linchip:hover {border-color:var(--accent);background:var(--surface);}
.hx-linchip:focus-visible {outline:2px solid var(--accent);outline-offset:2px;}
.hx-linchip i {font-style:normal;font-size:9.5px;font-weight:500;color:var(--text-dimmer);}
.hx-linchip-gone {
  cursor:help;border-style:dashed;border-color:var(--rm-neg);
  color:var(--text-dim);
}
.hx-linchip-gone i {color:var(--rm-neg);}
.hx-linhint {font-size:10px;color:var(--text-dimmer);font-style:italic;}
.hx-linnone {font-size:10.5px;color:var(--text-dimmer);font-style:italic;}
.hx-linchip.hx-lin-flash {
  animation:hxflash 1.1s ease;
}
@keyframes hxflash {0%,100%{box-shadow:none;} 30%{box-shadow:0 0 0 3px rgba(245,206,74,.35);}}
.hx-a.hx-lin-target > summary {animation:hxflash 1.1s ease;}

/* ── test state strip ── */
.hx-tstate {
  font-size:11.5px;line-height:1.55;color:var(--text-dim);
  padding:9px 12px;border-radius:var(--r-sm);background:var(--surface);
  border:1px solid var(--border);margin-bottom:12px;
}
.hx-tstate b {color:var(--text);font-weight:650;}
.hx-tstate code {
  font-size:10.5px;background:var(--surface-3);padding:1px 5px;border-radius:4px;
}
.hx-tstate-untested {border-style:dashed;}
.hx-ameta {margin:14px 0 14px;display:grid;grid-template-columns:auto 1fr;gap:6px 14px;font-size:12px;}
.hx-ameta dt {color:var(--text-dimmer);font-size:9.5px;letter-spacing:.09em;text-transform:uppercase;
  padding-top:3px;white-space:nowrap;}
.hx-ameta dd {margin:0;color:var(--text-dim);line-height:1.6;max-width:70ch;}
@media (max-width:640px) {.hx-ameta {grid-template-columns:1fr;gap:2px 0;}
  .hx-ameta dd {margin-bottom:9px;}}
.hx-note {font-size:11.5px;line-height:1.6;color:var(--text-dim);margin:0 0 8px;max-width:74ch;}
.hx-note b {color:var(--text-dimmer);text-transform:uppercase;font-size:9.5px;letter-spacing:.08em;}

.hx-evh {font-size:9.5px;letter-spacing:.11em;text-transform:uppercase;color:var(--text-dimmer);
  margin:0 0 9px;padding-top:12px;border-top:1px solid var(--border);}
.hx-evlist {display:flex;flex-direction:column;gap:8px;}
.hx-ev {background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:10px 12px;
  border-left:3px solid var(--hx-mid);}
.hx-ev-supports {border-left-color:var(--hx-pos);}
.hx-ev-contradicts {border-left-color:var(--hx-neg);}
.hx-evhead {display:flex;flex-wrap:wrap;align-items:center;gap:7px;margin-bottom:5px;}
.hx-evid {font-size:11px;font-weight:650;font-variant-numeric:tabular-nums;}
.hx-verdict {font-size:10px;font-weight:550;}
.hx-verdict-supports {color:var(--hx-pos);}
.hx-verdict-contradicts {color:var(--hx-neg);}
.hx-verdict-ambiguous {color:var(--text-dim);}
.hx-evdate {font-size:10px;color:var(--text-dimmer);font-variant-numeric:tabular-nums;}
.hx-conf {display:inline-flex;gap:2px;align-items:center;}
.hx-dot {width:4px;height:4px;border-radius:50%;background:var(--surface-3);display:block;}
.hx-dot.on {background:var(--text-dim);}
.hx-evsrc {margin:0 0 4px;font-size:11px;color:var(--text-dim);font-weight:550;}
.hx-evtype {font-weight:400;color:var(--text-dimmer);font-size:10px;}
.hx-evclaim {margin:0;font-size:12px;line-height:1.6;max-width:74ch;}
.hx-evnotes {margin-top:6px;}
.hx-evnotes summary {cursor:pointer;font-size:10.5px;color:var(--text-dimmer);}
.hx-evnotes summary:hover {color:var(--text-dim);}
.hx-evnotes p {margin:5px 0 0;font-size:11.5px;line-height:1.6;color:var(--text-dim);max-width:74ch;}
.hx-corr {margin:7px 0 0;font-size:11px;color:var(--yellow);max-width:74ch;line-height:1.55;}
.hx-corr b {text-transform:uppercase;font-size:9.5px;letter-spacing:.08em;margin-right:5px;}
.hx-evnq {margin:7px 0 0;font-size:11px;color:var(--text-dim);}
.hx-evnq span {font-size:9px;letter-spacing:.09em;text-transform:uppercase;color:var(--text-dimmer);
  margin-right:5px;}
.hx-empty {font-size:11.5px;color:var(--text-dimmer);font-style:italic;margin:0;}

.hx-past {margin-top:16px;padding:11px 14px;border:1px solid var(--border);border-radius:10px;
  background:var(--surface);}
.hx-past>summary {cursor:pointer;font-size:11.5px;color:var(--text-dim);}
.hx-past>summary:hover {color:var(--text);}
.hx-past ul {list-style:none;margin:12px 0 0;padding:0;display:flex;flex-direction:column;gap:10px;}
.hx-past li {display:flex;flex-wrap:wrap;align-items:center;gap:7px;}
.hx-past li p {flex:1 1 100%;margin:0;font-size:11.5px;line-height:1.55;color:var(--text-dim);
  max-width:80ch;}
"""


def _hx_counts(evidence: list[dict], key: str) -> dict:
    """Verdict tally for one assumption or hunch id."""
    out: dict[str, int] = {}
    for ev in evidence:
        if ev.get("assumption_linked") == key:
            v = str(ev.get("verdict") or "ambiguous").strip()
            out[v] = out.get(v, 0) + 1
    return out


def _hx_meter(counts: dict, scale: int) -> str:
    """Stacked verdict tally — a diverging scale, two poles + neutral midpoint.

    Palette validated with the dataviz validator against this dashboard's own
    surface (#14171c): CVD deutan dE 12.7, normal-vision dE 22.2, all three steps
    clear 3:1. The neutral reads gray by design; that is what a diverging midpoint
    is, and it is why the chroma-floor check is expected to fail on it.

    Width scales against the largest single tally on the tab, so bar lengths
    compare across cards instead of each one filling its own track.
    """
    n = sum(counts.values())
    if not n:
        return '<span class="hx-meter hx-meter-none">no evidence yet</span>'
    segs = "".join(
        f'<span class="hx-seg hx-seg-{v}" style="flex:{counts[v]}"></span>'
        for v in _HX_ORDER if counts.get(v)
    )
    pct = (n / scale * 100) if scale else 0
    return (f'<span class="hx-meter"><span class="hx-track">'
            f'<span class="hx-fill" style="width:{pct:.1f}%">{segs}</span>'
            f'</span></span>')


def _hx_tallies(counts: dict) -> str:
    """Counts as text. A status colour never carries meaning alone — glyph + number + word."""
    if not sum(counts.values()):
        return '<span class="hx-tally hx-tally-none">0 entries</span>'
    return "".join(
        f'<span class="hx-tally hx-tally-{v}">'
        f'<i class="hx-glyph" aria-hidden="true">{_HX_GLYPH[v]}</i>{counts[v]} {v}</span>'
        for v in _HX_ORDER if counts.get(v)
    )


def _hx_evidence_card(ev: dict) -> str:
    verdict = str(ev.get("verdict") or "ambiguous").strip()
    conf = str(ev.get("confidence") or "")
    dots = ""
    if conf.isdigit():
        dots = ('<span class="hx-conf" title="confidence ' + conf + ' of 5">'
                + "".join(f'<i class="hx-dot{" on" if i < int(conf) else ""}"></i>'
                          for i in range(5)) + "</span>")
    unp = ('<span class="hx-chip hx-chip-unp">unprompted</span>'
           if ev.get("unprompted") in (True, "true", "True") else "")
    notes = " ".join(str(ev.get("notes") or "").split())
    nq = " ".join(str(ev.get("next_question_raised") or "").split())
    corr = " ".join(str(ev.get("correction_note") or "").split())
    return f'''<article class="hx-ev hx-ev-{escape(verdict)}">
  <div class="hx-evhead"><span class="hx-evid">{escape(str(ev.get("id") or ""))}</span>
    <span class="hx-verdict hx-verdict-{escape(verdict)}">{_HX_GLYPH.get(verdict, "~")} {escape(verdict)}</span>
    <span class="hx-evdate">{escape(str(ev.get("date") or ""))}</span>{dots}{unp}</div>
  <p class="hx-evsrc">{escape(" ".join(str(ev.get("source") or "").split()))}
    <span class="hx-evtype">{escape(str(ev.get("source_type") or ""))}</span></p>
  <p class="hx-evclaim">{escape(" ".join(str(ev.get("claim") or "").split()))}</p>
  {f'<details class="hx-evnotes"><summary>reading</summary><p>{escape(notes)}</p></details>' if notes else ""}
  {f'<p class="hx-corr"><b>corrected</b> {escape(corr)}</p>' if corr else ""}
  {f'<p class="hx-evnq"><span>opens</span> {escape(nq)}</p>' if nq else ""}
</article>'''


def _hx_lineage(a: dict, by_id: dict) -> str:
    """Parent/child edges for one assumption, as chips that jump to the target.

    This is DAG STRUCTURE, not lineage history. `hunch-lineage.md` remains the sole
    author of how the hunches got their shape and this tab still tells none of that
    story. Parent/child edges are declared only in graph.md and rendered nowhere
    else, so showing them here duplicates no other author.

    A referenced id that no longer exists renders as a flagged chip rather than
    being dropped — a dangling edge is a data bug and hiding it is how it survives.
    """
    def chips(key: str) -> str:
        out = []
        for ref in (a.get(key) or []):
            rid = str(ref).strip()
            if not rid:
                continue
            tgt = by_id.get(rid)
            if tgt is None:
                out.append(f'<span class="hx-linchip hx-linchip-gone" '
                           f'title="No assumption with id {escape(rid)} — stale reference">'
                           f'{escape(rid)}<i>missing</i></span>')
            else:
                out.append(f'<button type="button" class="hx-linchip" data-goto="{escape(rid)}">'
                           f'{escape(rid)}<i>{escape(str(tgt.get("status") or "untested"))}</i></button>')
        return "".join(out)

    up, down = chips("parent_assumptions"), chips("child_assumptions")
    if not up and not down:
        return ('<div class="hx-lin"><span class="hx-linnone">Standalone — no parent or child '
                'declared in the graph. It can be tested in any order.</span></div>')
    rows = ""
    if up:
        rows += (f'<div class="hx-linrow"><span class="hx-linlbl">Rests on</span>'
                 f'<span class="hx-linchips">{up}</span>'
                 f'<span class="hx-linhint">must hold first</span></div>')
    if down:
        rows += (f'<div class="hx-linrow"><span class="hx-linlbl">Carries</span>'
                 f'<span class="hx-linchips">{down}</span>'
                 f'<span class="hx-linhint">falls with this one</span></div>')
    return f'<div class="hx-lin">{rows}</div>'


def _hx_teststate(a: dict, mine: list[dict]) -> str:
    """One line: has this been tested, and what came back. Derived, never authored."""
    if not mine:
        return ('<p class="hx-tstate hx-tstate-untested"><b>Not tested yet.</b> '
                'Nothing in the ledger points here.</p>')
    c = _hx_counts(mine, str(a.get("id") or ""))
    latest = max(str(e.get("date") or "") for e in mine)
    parts = ", ".join(f"{c[v]} {v}" for v in _HX_ORDER if c.get(v))
    return (f'<p class="hx-tstate"><b>Tested.</b> {len(mine)} '
            f'{"entry" if len(mine) == 1 else "entries"} — {escape(parts)}. '
            f'Latest {escape(latest)}. Best grade '
            f'<code>{escape(str(a.get("evidence_quality") or "none"))}</code>.</p>')


def _hx_assumption(a: dict, evidence: list[dict], rank, active: bool, scale: int,
                   by_id: dict | None = None) -> str:
    by_id = by_id or {}
    aid = str(a.get("id") or "")
    mine = sorted((e for e in evidence if e.get("assumption_linked") == aid),
                  key=lambda e: str(e.get("date")), reverse=True)
    counts = _hx_counts(evidence, aid)
    st = str(a.get("status") or "untested")
    lof = str(a.get("quadrant") or "") == "leap_of_faith"

    scores = "".join(
        _assumption_score_dots(label, a.get(key))
        for label, key in (("kill", "kill_power"), ("uncert", "uncertainty_score"),
                           ("cost", "test_cost"))
        if a.get(key) not in (None, ""))

    meta = "".join(
        f"<dt>{lbl}</dt><dd>{escape(' '.join(str(a[k]).split()))}</dd>"
        for k, lbl in (("why_it_matters", "If false"),
                       ("disconfirmation", "Disconfirmation"),
                       ("stop_rule", "Stop rule"),
                       ("next_action", "Next action"))
        if a.get(k))

    # Founder-authored reasoning. These are the fields most often lost when the
    # graph is skimmed, and this tab is the only place they render.
    notes = "".join(
        f'<p class="hx-note"><b>{escape(lbl)}</b> {escape(" ".join(str(a[k]).split()))}</p>'
        for k, lbl in (("founder_promise", "The promise —"),
                       ("founder_framing", "Founder framing —"),
                       ("test_constraint", "Test constraint —"),
                       ("relationship_to_K2", "Kill condition —"),
                       ("scoring_note", "Scoring —"),
                       ("revival_reason", "Revived —"),
                       ("dormant_reason", "Dormant —"))
        if a.get(k))

    ev_html = "".join(_hx_evidence_card(e) for e in mine) or (
        '<p class="hx-empty">No ledger entry points at this assumption yet. Its '
        '<b>next action</b> above is how that changes.</p>')

    return f'''<details class="hx-a{" hx-a-active" if active else ""}" id="hx-a-{escape(aid)}">
  <summary>
    <span class="hx-ahead"><span class="hx-aid">{escape(aid)}</span>
      {f'<span class="hx-rank">#{rank}</span>' if rank else ""}
      {'<span class="hx-chip hx-chip-active">testing now</span>' if active else ""}
      <span class="hx-chip">{escape(st)}</span>
      <span class="hx-chip">{escape(str(a.get("evidence_quality") or "none"))}</span>
      {'<span class="hx-chip hx-chip-lof">leap of faith</span>' if lof else ""}</span>
    <span class="hx-aclaim">{escape(str(a.get("assumption") or ""))}</span>
    <span class="hx-afoot">{_hx_meter(counts, scale)}<span class="hx-tallies">{_hx_tallies(counts)}</span>
      {f'<span class="hx-scores">{scores}</span>' if scores else ""}</span>
  </summary>
  <div class="hx-adetail">
    {_hx_lineage(a, by_id)}
    {_hx_teststate(a, mine)}
    {f'<dl class="hx-ameta">{meta}</dl>' if meta else ""}
    {notes}
    <h4 class="hx-evh">Evidence &middot; {len(mine)}</h4>
    <div class="hx-evlist">{ev_html}</div>
  </div>
</details>'''


_COMP_KEY = re.compile(r"^- ([A-Z][\w'/() -]{1,44}?)(?: \(([^)]+)\))?: ?(.*)$")


def _hx_components(h: dict) -> str:
    """Per-hunch thinking: components as a key/value grid, notes flagged, reason on top."""
    comp = str(h.get("components") or "").strip()
    reason = str(h.get("change_reason") or "").strip()
    if not comp and not reason:
        return ""

    pairs: list[tuple[str, str]] = []   # (key, value-html)
    notes: list[str] = []               # flagged bullets that aren't Key: value
    # A wrapped continuation line belongs to whatever was opened LAST, so track that
    # explicitly. The previous rule appended continuations to the last pair only
    # `if pairs and not notes` — so the moment one note-shaped bullet appeared, every
    # later component lost every line but its first, and those lines piled into the note
    # as one run-on paragraph. H3 rendered "Problem: ... Sun Glow states it plainly in its
    # dealer" and dropped the sentence that carried the actual number (found 2026-09-03).
    last: str | None = None
    for raw in comp.splitlines():
        s = raw.rstrip()
        if not s.strip():
            continue
        m = _COMP_KEY.match(s)
        if m:
            key = m.group(1) + (f" ({m.group(2)})" if m.group(2) else "")
            pairs.append((key, escape(m.group(3))))
            last = "pair"
        elif s.startswith("- "):
            notes.append(escape(s[2:].strip()))
            last = "note"
        elif s.startswith(("  ", "\t")):
            if last == "pair" and pairs:
                pairs[-1] = (pairs[-1][0], pairs[-1][1] + " " + escape(s.strip()))
            elif last == "note" and notes:
                notes[-1] += " " + escape(s.strip())

    # Three separate toggles, all CLOSED by default including on the active hunch.
    # Previously this was one <details> force-opened whenever the hunch was active, which
    # meant the one hunch a reader actually cares about was the one that dumped its entire
    # body as a wall of prose above the assumptions. Splitting it lets a reader open the one
    # part they want, and keeps the card scannable.
    blocks = []
    if reason:
        blocks.append(("Why this hunch exists",
                       f'<p class="hx-reason">{_inline_md(reason)}</p>'))
    if pairs:
        rows = "".join(f"<dt>{escape(k)}</dt><dd>{_inline_finish(v)}</dd>" for k, v in pairs)
        blocks.append((f"Components ({len(pairs)})", f'<dl class="hx-kv">{rows}</dl>'))
    if notes:
        items = "".join(f'<li>{_inline_finish(n)}</li>' for n in notes)
        blocks.append((f"Open questions &amp; decisions ({len(notes)})",
                       f'<div class="hx-notes"><ul>{items}</ul></div>'))
    if not blocks:
        return ""
    return "".join(
        f'<details class="hx-comp"><summary>{label}</summary>'
        f'<div class="hx-comp-body">{body}</div></details>'
        for label, body in blocks)

_STMT_CLAMP = 320


def _hx_statement(h: dict) -> str:
    """Statement, clamped. Long statements get a lead-in plus a toggle for the rest.

    Some lineage files put explanatory prose under `### Statement` before the claim itself,
    so this block can run to several hundred words. Printing all of it pushed the assumptions
    below the fold on the one hunch that matters.
    """
    text = " ".join(str(h.get("statement") or "").split())
    if not text:
        return ""
    if len(text) <= _STMT_CLAMP:
        return f'<p class="hx-hstmt">{_inline_md(text)}</p>'
    cut = text.rfind(" ", 0, _STMT_CLAMP)
    if cut < 0:
        cut = _STMT_CLAMP
    return (f'<p class="hx-hstmt">{_inline_md(text[:cut])}&hellip;</p>'
            '<details class="hx-comp"><summary>Rest of the statement</summary>'
            f'<div class="hx-comp-body"><p>{_inline_md(text[cut:].lstrip())}</p></div></details>')


def _hx_hunch(h: dict, assumptions: list[dict], evidence: list[dict],
              ranks: dict, active_a: str, scale: int, by_id: dict | None = None) -> str:
    by_id = by_id or {}
    hid = str(h.get("id") or "")
    mine = sorted((a for a in assumptions if str(a.get("hunch") or "") == hid),
                  key=lambda a: ranks.get(str(a.get("id")), 999))
    ids = {str(a.get("id")) for a in mine} | {hid}
    counts: dict[str, int] = {}
    for ev in evidence:
        if ev.get("assumption_linked") in ids:
            v = str(ev.get("verdict") or "ambiguous").strip()
            counts[v] = counts.get(v, 0) + 1

    direct = sorted((e for e in evidence if e.get("assumption_linked") == hid),
                    key=lambda e: str(e.get("date")), reverse=True)
    direct_html = ""
    if direct:
        direct_html = (
            f'<details class="hx-direct"><summary>{len(direct)} entries filed against '
            f'{escape(hid)} itself, not a specific assumption</summary>'
            f'<div class="hx-evlist">{"".join(_hx_evidence_card(e) for e in direct)}</div></details>')

    return f'''<section class="hx-hunch" id="hx-{escape(hid)}">
  <header class="hx-hhead">
    <div class="hx-htitle"><span class="hx-hid">{escape(hid)}</span>
      <span class="hx-chip hx-chip-active">{escape(str(h.get("status") or ""))}</span></div>
    {_hx_statement(h)}
    {_hx_components(h)}
    <div class="hx-hstats"><span><b>{len(mine)}</b> assumptions</span>
      <span><b>{sum(counts.values())}</b> evidence</span>
      <span class="hx-tallies">{_hx_tallies(counts)}</span></div>
  </header>
  {direct_html}
  <div class="hx-alist">{"".join(_hx_assumption(a, evidence, ranks.get(str(a.get("id"))), str(a.get("id")) == active_a, scale, by_id) for a in mine)}</div>
</section>'''


def render_thesis_tab(lineage_fm: dict, hunches: list[dict],
                      graph_fm: dict, assumptions: list[dict],
                      belief_text: str, evidence: list[dict] | None = None,
                      belief_sections: list[tuple[str, str]] | None = None,
                      artifacts: list[tuple[str, str]] | None = None) -> str:
    """Belief -> live hunches -> their assumptions -> the evidence behind each, on click.

    This tab answers "what is under test right now and what do we know about it".
    It deliberately carries NO lineage history: `hunch-lineage.md` is the single
    author of how the lineage got its current shape, and a second narrative of the
    same events is exactly the drift this repo's single-authorship rule forbids.
    Hunches that are no longer active still appear, collapsed, so nothing is hidden
    — but as a roster, not a story.
    """
    evidence = evidence or []
    if not hunches and not assumptions:
        return ('<div class="empty-state" role="status"><p>No hunch lineage or assumption '
                'graph found for this idea.</p></div>')

    # Ranking is authored by build_brief so the tab and the brief cannot disagree
    # about which assumption is next. Imported lazily: build_brief imports this
    # module at top level, so a module-level import here would be circular.
    ranks: dict = {}
    try:
        sys.path.insert(0, str(REPO))
        from scripts.build_brief import rank_assumptions
        ranks = {str(a.get("id")): i + 1 for i, a in enumerate(rank_assumptions(assumptions))}
    except Exception:  # ranking is a nicety; the tab must render without it
        ranks = {}

    active_a = str(graph_fm.get("active_assumption") or "")
    live = [h for h in hunches if str(h.get("status") or "").strip() == "active"]
    live.sort(key=lambda h: str(h.get("id")))
    live_ids = {str(h.get("id")) for h in live}

    per: dict = {}
    for ev in evidence:
        k = ev.get("assumption_linked")
        per[k] = per.get(k, 0) + 1
    scale = max([per.get(str(a.get("id")), 0) for a in assumptions] or [1]) or 1

    out = ['<div class="hx-root">']

    secs = belief_sections or []
    if secs:
        btns = "".join(
            f'<button class="hx-bpill" data-bsec="bsec{i}" onclick="hxBsec(\'bsec{i}\')">{escape(title)}</button>'
            for i, (title, _) in enumerate(secs))
        panels = "".join(
            f'<div class="hx-bpanel" id="bsec{i}" hidden>{_md_lite(body)}</div>'
            for i, (_, body) in enumerate(secs))
        belief_details = (
            f'<div class="hx-bnav">{btns}</div>{panels}'
            '<script>function hxBsec(id){'
            'var el=document.getElementById(id); var wasHidden=el.hidden;'
            'document.querySelectorAll(".hx-bpanel").forEach(function(p){p.hidden=true;});'
            'document.querySelectorAll(".hx-bpill").forEach(function(b){b.classList.remove("active");});'
            'if(wasHidden){el.hidden=false;'
            'document.querySelector(\'[data-bsec="\'+id+\'"]\').classList.add("active");}}'
            '</script>')
    else:
        belief_details = ""
    out.append('<section class="hx-belief"><b>The durable belief</b>'
               f'<blockquote>{escape(belief_text)}</blockquote>'
               f'{belief_details}'
               '</section>')
    if artifacts:
        links = " · ".join(
            f'<a href="{escape(rel)}">{escape(label)}</a>' for rel, label in artifacts)
        out.append(f'<div class="hx-artifacts"><b>Run artifacts &amp; research</b> {links}</div>')

    tally: dict = {}
    for ev in evidence:
        v = str(ev.get("verdict") or "ambiguous").strip()
        tally[v] = tally.get(v, 0) + 1
    out.append('<div class="hx-topstats">'
               f'<span><b>{len(live)}</b> active {"hunch" if len(live) == 1 else "hunches"}</span>'
               f'<span><b>{len(assumptions)}</b> assumptions</span>'
               f'<span><b>{len(evidence)}</b> evidence entries</span>'
               f'<span class="hx-tallies">{_hx_tallies(tally)}</span></div>')

    if not live:
        out.append('<p class="hx-warn"><b>No active hunch.</b> Every hunch in the lineage is '
                   'retired, superseded or folded. Run <code>/startup-belief-intake</code>.</p>')

    if active_a in ("none_pending_extraction", "", "none"):
        out.append('<p class="hx-warn"><b>No active assumption.</b> Run '
                   '<code>/startup-idea-to-assumptions</code>.</p>')

    # id -> node, so a parent/child edge can resolve its target's status and flag
    # any reference that no longer resolves.
    by_id = {str(a.get("id")): a for a in assumptions if a.get("id")}

    out.append('<div class="hx-grid">')
    for h in live:
        out.append(_hx_hunch(h, assumptions, evidence, ranks, active_a, scale, by_id))
    out.append('</div>')

    # Assumptions serving more than one hunch, or orphaned by a retired one.
    shared = sorted((a for a in assumptions if str(a.get("hunch") or "") not in live_ids),
                    key=lambda a: ranks.get(str(a.get("id")), 999))
    if shared:
        out.append('<section class="hx-hunch hx-shared"><header class="hx-hhead">'
                   '<div class="hx-htitle"><span class="hx-hid">Shared &amp; unattached</span></div>'
                   '</header><div class="hx-alist">')
        for a in shared:
            out.append(_hx_assumption(a, evidence, ranks.get(str(a.get("id"))),
                                      str(a.get("id")) == active_a, scale, by_id))
        out.append('</div></section>')

    past = [h for h in hunches if str(h.get("status") or "").strip() != "active"]
    if past:
        rows = "".join(
            f'<li><span class="hx-hid">{escape(str(h.get("id") or ""))}</span>'
            f'<span class="hx-chip">{escape(str(h.get("status") or ""))}</span>'
            + (f'<span class="hx-chip">&rarr; {escape(str(h.get("superseded_by")))}</span>'
               if h.get("superseded_by") else "")
            + f'<p>{_inline_md(" ".join(str(h.get("statement") or "").split()))}</p></li>'
            for h in past)
        out.append(f'<details class="hx-past"><summary>{len(past)} hunches no longer active</summary>'
                   f'<ul>{rows}</ul>'
                   '<p class="hx-empty">Why each moved: '
                   '<code>01-ideation/hunch-lineage.md</code>.</p></details>')

    out.append('</div>')
    return "\n".join(out)


PAGES_CSS = """
.pg-grid {display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px;margin-top:16px;}
.pg-card {display:block;padding:16px 18px;border:1px solid var(--rule);border-radius:10px;
          background:var(--surface);text-decoration:none;color:inherit;transition:border-color .15s,transform .15s;}
.pg-card:hover {border-color:var(--accent);transform:translateY(-1px);}
.pg-title {font-weight:600;font-size:1.02rem;margin:0 0 6px;}
.pg-note {margin:0;font-size:.86rem;line-height:1.5;color:var(--muted);}
.pg-tag {display:inline-block;font-size:.68rem;letter-spacing:.06em;text-transform:uppercase;
         padding:2px 7px;border-radius:4px;margin-bottom:8px;font-weight:600;}
.pg-tag.current {background:var(--positive-soft,#E4EDE5);color:var(--positive,#3B6B46);}
.pg-tag.generated {background:var(--accent-soft,#E4E9F3);color:var(--accent-ink,#1D3560);}
.pg-tag.superseded {background:var(--surface-2);color:var(--muted);}
.pg-tag.unlisted {background:var(--negative-soft,#F5E7E4);color:var(--negative,#8C3B2F);}
.pg-group {margin-top:26px;}
.pg-group h3 {margin:0 0 2px;font-size:.95rem;}
.pg-group p.sub {margin:0;font-size:.82rem;color:var(--muted);}
"""

PAGE_GROUPS = [
    ("plan", "The plan", "What this business is and what it would take to build it."),
    ("evidence", "The evidence", "What was measured, and how every number was derived."),
    ("outreach", "Outreach", "Tools for the conversations themselves."),
]


def _page_title(path: Path) -> str:
    """A page's own <title> — read from the file so it cannot drift from a list."""
    try:
        head = path.read_text(encoding="utf-8", errors="replace")[:8000]
    except OSError:
        return path.stem
    m = re.search(r"<title[^>]*>(.*?)</title>", head, re.S | re.I)
    return unescape(re.sub(r"\s+", " ", m.group(1)).strip()) if m else path.stem


def render_pages_tab() -> str:
    """Every openable page in reports/pages/, grouped and labelled.

    The control room is the one page you open for an idea; this tab is what makes that
    true of the reports too, rather than leaving eight HTML files in a folder with names
    that do not say which of them still holds. Titles come from each file, notes and
    status from pages/pages.yaml — see that file for why the split is that way.
    """
    pages_dir = REPORTS / "pages"
    if not pages_dir.is_dir():
        return ('<div class="empty-state" role="status"><p>No <code>pages/</code> folder '
                'for this idea yet.</p></div>')

    listed: list[dict] = []
    manifest = pages_dir / "pages.yaml"
    if manifest.exists() and _HAS_YAML:
        try:
            listed = (yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}).get("pages") or []
        except yaml.YAMLError:
            listed = []
    by_file = {str(r.get("file")): r for r in listed if r.get("file")}

    on_disk = sorted(f.name for f in pages_dir.glob("*.html"))
    for name in on_disk:
        by_file.setdefault(name, {"file": name, "status": "unlisted", "group": "plan",
                                  "note": "Not listed in pages.yaml — add a row saying "
                                          "what it is and whether it still holds."})

    out = ['<section class="th-block">']
    out.append("<h2>Every page for this idea</h2>")

    for gkey, gname, gsub in PAGE_GROUPS:
        rows = [r for r in by_file.values() if (r.get("group") or "plan") == gkey
                and (pages_dir / str(r["file"])).exists()]
        if not rows:
            continue
        order = {"current": 0, "generated": 1, "unlisted": 2, "superseded": 3}
        rows.sort(key=lambda r: (order.get(str(r.get("status")), 4), str(r["file"])))
        out.append(f'<div class="pg-group"><h3>{escape(gname)}</h3>'
                   f'<p class="sub">{escape(gsub)}</p><div class="pg-grid">')
        for r in rows:
            fn = str(r["file"])
            status = str(r.get("status") or "unlisted")
            title = _page_title(pages_dir / fn)
            note = " ".join(str(r.get("note") or "").split())
            out.append(
                f'<a class="pg-card" href="pages/{escape(fn)}">'
                f'<span class="pg-tag {escape(status)}">{escape(status)}</span>'
                f'<p class="pg-title">{escape(title)}</p>'
                f'<p class="pg-note">{escape(note)}</p></a>')
        out.append("</div></div>")

    missing = [f for f in by_file if not (pages_dir / str(f)).exists()]
    if missing:
        out.append('<p class="pat-lede" style="margin-top:20px">Listed in '
                   '<code>pages.yaml</code> but not on disk: <b>'
                   + escape(", ".join(sorted(missing))) + "</b>.</p>")
    out.append("</section>")
    return "\n".join(out)


def render_offerings_tab(offerings: list[dict], scored_patterns: list[dict],
                         offerings_fm: dict) -> str:
    if not offerings:
        return ('<div class="empty-state" role="status"><p>No offerings derived yet. '
                'They live in <code>04-mutation/offerings.md</code> and are derived from '
                'the pain patterns.</p></div>')
    pat_by_id = {p["id"]: p for p in scored_patterns}

    out = ['<section class="th-block">']
    out.append('<h2>Pain patterns &rarr; candidate offerings</h2>')
    out.append('<p class="pat-lede">Status: '
               f'<b>{escape(str(offerings_fm.get("status") or "candidate"))}</b>. '
               'Each card carries the pattern and entry IDs behind it.</p>')

    # inherited strength = sum of the strengths of the patterns behind it
    for o in offerings:
        pids = o.get("derived_from") or []
        o["_inherited"] = sum(pat_by_id.get(pid, {}).get("strength", 0) for pid in pids)
    ranked = sorted(offerings, key=lambda o: -o["_inherited"])
    max_inh = max([o["_inherited"] for o in ranked] or [1]) or 1

    for o in ranked:
        pids = o.get("derived_from") or []
        gate = str(o.get("authority_gate") or "")
        gate_tone = ("bad" if gate.upper().startswith(("BLOCKING", "HIGH"))
                     else "warn" if gate.lower().startswith("medium") else "good")
        sold = str(o.get("already_sold_by") or "none identified")
        contested = not sold.lower().startswith("none")
        pat_chips = "".join(
            f'<span class="off-chip off-chip-pat" title="{escape(str(pat_by_id.get(pid, {}).get("statement", ""))[:200])}">'
            f'{escape(pid)} <b>{pat_by_id.get(pid, {}).get("strength", "?")}</b></span>'
            for pid in pids)
        ev_chips = "".join(f'<span class="off-chip">{escape(str(e))}</span>'
                           for e in (o.get("evidence") or []))
        pct = int(100 * o["_inherited"] / max_inh) if max_inh else 0
        out.append(f'''<article class="off-card">
  <div class="off-head">
    <div class="off-title">
      <h3><span class="pat-pid">{escape(str(o.get("id")))}</span> {escape(str(o.get("name") or ""))}</h3>
      <p class="off-one">{escape(" ".join(str(o.get("one_line") or "").split()))}</p>
    </div>
    <div class="pat-strength">
      <span class="pat-strength-num">{o["_inherited"]}</span>
      <span class="pat-strength-lbl">inherited</span>
    </div>
  </div>
  <div class="pat-bar"><span style="width:{max(pct, 2)}%"></span></div>
  <div class="off-chips"><span class="off-lbl">from</span>{pat_chips}
    <span class="off-lbl">evidence</span>{ev_chips}</div>
  <div class="off-grid">
    <div><span class="off-k">The case</span><p>{escape(" ".join(str(o.get("the_case") or "").split()))}</p></div>
    <div><span class="off-k">Biggest risk</span><p class="off-risk">{escape(" ".join(str(o.get("biggest_risk") or "").split()))}</p></div>
    <div><span class="off-k">Second risk</span><p class="off-risk">{escape(" ".join(str(o.get("second_risk") or "").split()))}</p></div>
  </div>
  <div class="off-foot">
    <span><b>buyer</b> {escape(str(o.get("buyer") or "?"))}</span>
    <span><b>wanted?</b> {escape(str(o.get("proof_it_is_wanted") or "?"))}</span>
    <span class="{'off-contested' if contested else ''}"><b>already sold by</b> {escape(sold)}</span>
    <span class="off-gate off-gate-{gate_tone}"><b>authority gate</b> {escape(gate)}</span>
  </div>
  <div class="off-status">{escape(str(o.get("status") or ""))}</div>
</article>''')
    out.append('</section>')
    return "\n".join(out)


THESIS_CSS = """
.th-block { margin: 0 0 30px; }
.th-block h2 { font-size: 15px; margin: 0 0 8px; }
.th-belief { margin: 0 0 12px; padding: 14px 18px; border-left: 3px solid var(--accent);
  background: var(--surface); border-radius: 0 var(--r-sm) var(--r-sm) 0;
  font-size: 15px; line-height: 1.6; }
.th-lineage { list-style: none; padding: 0; margin: 0; }
.th-hunch { border-left: 2px solid var(--border); padding: 0 0 0 16px; margin: 0 0 18px;
  position: relative; }
.th-hunch-active { border-left-color: var(--accent); }
.th-hrow { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin-bottom: 6px; }
.th-hid, .th-aid { font-family: ui-monospace, monospace; font-size: 13px; font-weight: 600; }
.th-hunch-active .th-hid { color: var(--accent); }
.th-badge { font-size: 10px; border-radius: 3px; padding: 1px 6px; border: 1px solid; }
.th-badge-good { color: var(--green); border-color: rgba(34,197,94,.5); }
.th-badge-warn { color: var(--yellow); border-color: rgba(245,158,11,.5); }
.th-badge-bad  { color: var(--red); border-color: rgba(239,68,68,.5); }
.th-badge-dim  { color: var(--text-dimmer); border-color: var(--border); }
.th-meta { font-size: 10.5px; color: var(--text-dimmer); }
.th-sup { font-size: 10.5px; color: var(--text-dim); font-family: ui-monospace, monospace; }
.th-stmt { font-size: 13px; line-height: 1.65; margin: 0 0 6px; max-width: 88ch; }
.th-dim .th-stmt { color: var(--text-dim); }
.th-reason { font-size: 11.5px; line-height: 1.6; color: var(--text-dimmer);
  margin: 0; max-width: 88ch; }
.th-warn { font-size: 12.5px; line-height: 1.6; color: var(--yellow); background: rgba(245,158,11,.07);
  border: 1px solid rgba(245,158,11,.3); border-radius: var(--r-sm); padding: 10px 14px;
  margin: 0 0 14px; }
.th-warn b { color: var(--text); }
.th-atable { display: flex; flex-direction: column; gap: 10px; }
.th-arow { border: 1px solid var(--border); border-radius: var(--r-md); padding: 12px 16px;
  background: var(--surface); }
.th-arow.th-dim { opacity: .62; }
.th-ahead { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin-bottom: 6px; }
.th-astmt { font-size: 13px; line-height: 1.6; margin: 0 0 6px; max-width: 90ch; }
.th-arow-active { border-color: rgba(99,102,241,.55); background: rgba(99,102,241,.06);
  box-shadow: 0 0 0 1px rgba(99,102,241,.16); opacity: 1; }
.th-badge-active { background: rgba(99,102,241,.18); color: #a5b4fc;
  border: 1px solid rgba(99,102,241,.45); }
.th-lof { font-size: 10.5px; letter-spacing: .04em; text-transform: uppercase;
  color: var(--red); border: 1px solid rgba(244,63,94,.32); border-radius: var(--r-sm);
  padding: 1px 7px; }
.th-scores { display: flex; flex-wrap: wrap; gap: 16px; margin: 8px 0 8px; }
.th-score { display: inline-flex; align-items: center; gap: 7px; }
.th-score-lbl { font-size: 10.5px; letter-spacing: .04em; text-transform: uppercase;
  color: var(--text-dimmer); }
.th-dots { display: inline-flex; gap: 3px; }
.th-dots i { width: 6px; height: 6px; border-radius: 50%; display: block;
  background: var(--border); }
.th-dots i.on { background: var(--text-dim); }
.th-arow-active .th-dots i.on { background: #818cf8; }
.th-why, .th-next { font-size: 12px; line-height: 1.6; margin: 0 0 5px; max-width: 88ch;
  color: var(--text-dim); }
.th-why b, .th-next b { color: var(--text-dimmer); font-weight: 600; font-size: 10.5px;
  letter-spacing: .04em; text-transform: uppercase; margin-right: 6px; }
.th-reason b { color: var(--text-dim); font-weight: 600; }
.off-card { border: 1px solid var(--border); border-radius: var(--r-md); background: var(--surface);
  padding: 16px 18px; margin: 0 0 12px; }
.off-head { display: flex; gap: 14px; align-items: flex-start; }
.off-title { flex: 1; min-width: 0; }
.off-title h3 { font-size: 14px; margin: 0 0 5px; font-weight: 600; }
.off-one { font-size: 13px; line-height: 1.6; color: var(--text-dim); margin: 0; max-width: 84ch; }
.off-chips { display: flex; flex-wrap: wrap; gap: 5px; align-items: center; margin-bottom: 12px; }
.off-lbl { font-size: 10px; color: var(--text-dimmer); text-transform: uppercase;
  letter-spacing: .06em; margin-right: 2px; }
.off-lbl:not(:first-child) { margin-left: 10px; }
.off-chip { font-size: 10.5px; font-family: ui-monospace, monospace; border: 1px solid var(--border);
  border-radius: 3px; padding: 1px 6px; color: var(--text-dim); }
.off-chip-pat { border-color: rgba(245,206,74,.4); color: var(--accent); }
.off-chip-pat b { color: var(--text); }
.off-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 14px;
  padding-top: 12px; border-top: 1px solid var(--border-subtle); }
.off-k { display: block; font-size: 10px; color: var(--text-dimmer); text-transform: uppercase;
  letter-spacing: .06em; margin-bottom: 4px; }
.off-grid p { font-size: 12px; line-height: 1.6; margin: 0; color: var(--text-dim); }
.off-grid p.off-risk { color: #f0a8a8; }
.off-foot { display: flex; flex-wrap: wrap; gap: 14px; font-size: 11px; color: var(--text-dim);
  margin-top: 12px; padding-top: 10px; border-top: 1px solid var(--border-subtle); }
.off-foot b { color: var(--text-dimmer); font-weight: 500; text-transform: uppercase;
  font-size: 9.5px; letter-spacing: .06em; margin-right: 3px; }
.off-contested { color: var(--red); }
.off-gate-bad { color: var(--red); } .off-gate-warn { color: var(--yellow); }
.off-gate-good { color: var(--green); }
.off-status { margin-top: 10px; font-size: 11px; color: var(--text-dimmer);
  font-family: ui-monospace, monospace; }
.pat-flip { border: 1px solid rgba(245,206,74,.4); background: rgba(245,206,74,.06);
  border-radius: var(--r-sm); padding: 10px 12px; margin: 10px 0 0; font-size: 12px;
  line-height: 1.6; color: var(--text-dim); }
.pat-flip b { color: var(--accent); }
.pat-badge-flip { color: var(--accent); border-color: var(--accent);
  background: rgba(245,206,74,.16); }
"""


# ─── main ────────────────────────────────────────────────────────────────────


def write_results_files(contacts: list[dict]) -> None:
    """Generate outreach/results-{A_ID}.md — a stats projection of contacts.md.

    These files used to be hand-written and drifted from the contacts they
    summarized within days (two of them disagreed on the same assumption's
    numbers). Now every figure comes from compute_conversion_stats; the
    classification and routing decisions live in contacts.md only.
    """
    conv = compute_conversion_stats(contacts)                     # LinkedIn only
    conv_phone = compute_conversion_stats(contacts, channel="phone")
    conv_all = compute_conversion_stats(contacts, channel=None)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    order = {st: i for i, st in enumerate(STATUS_ORDER)}
    # Write a file for every assumption that has ANY contact, on any channel. Skipping the
    # write when `contacted` was 0 left the previous run's file on disk claiming a 100%
    # reply rate that no longer existed — a generated file that silently fails to
    # regenerate is worse than one that says zero (found 2026-09-03).
    all_aids = sorted(set(conv["by_assumption"]) | set(conv_phone["by_assumption"])
                      | set(conv_all["by_assumption"]))
    for aid in all_aids:
        s = conv["by_assumption"].get(aid) or {
            "targeted": 0, "contacted": 0, "replied": 0, "qualified_replied": 0,
            "reply_rate": None, "qualified_reply_rate": None}
        ph = conv_phone["by_assumption"].get(aid) or {
            "targeted": 0, "contacted": 0, "replied": 0, "qualified_replied": 0,
            "reply_rate": None, "qualified_reply_rate": None}
        cohort = [c for c in contacts if aid in (c.get("assumptions_tested") or [])]
        if not cohort:
            continue
        lines = [
            "<!-- GENERATED by scripts/build_control_room.py — DO NOT EDIT.",
            "     Every value is derived from outreach/contacts.md; fix that file and",
            "     rerun: python3 scripts/build_control_room.py",
            "-->",
            f"# Outreach results — {aid} · {idea_name()}",
            "",
            f"_Generated {now}. Numbers are the funnel over contacts tagged {aid}._",
            "",
            "| channel | targeted | contacted | replied | qualified replied | reply rate |",
            "|---|---|---|---|---|---|",
            f"| LinkedIn | {s['targeted']} | {s['contacted']} | {s['replied']} "
            f"| {s['qualified_replied']} "
            f"| {str(s['reply_rate']) + '%' if s['reply_rate'] is not None else '—'} |",
            f"| phone | {ph['targeted']} | {ph['contacted']} | {ph['replied']} "
            f"| {ph['qualified_replied']} "
            f"| {str(ph['reply_rate']) + '%' if ph['reply_rate'] is not None else '—'} |",
            "",
            "_Channels are counted separately._",
            "",
            "## Contacts by status",
            "",
            "| id | name | status | call stage |",
            "|---|---|---|---|",
        ]
        for c in sorted(cohort, key=lambda c: (order.get(str(c.get("outreach_status") or "pending"), 99),
                                               str(c.get("id")))):
            lines.append(
                f"| {c.get('id', '')} | {c.get('name', '')} | {c.get('outreach_status') or 'pending'} "
                f"| {c.get('call_stage', '') or '—'} |")
        lines.append("")
        (REPORTS / "outreach" / f"results-{aid}.md").write_text(
            "\n".join(lines), encoding="utf-8")


def build() -> Path | None:
    """
    Build the single dashboard HTML.

    ONE file. Do NOT add per-assumption outputs
    (`outreach_tracker-A2.html` etc.) — the in-page Assumption filter is how you
    view a slice, and that fragmentation was explicitly rejected by the founders.
    """
    contacts_path = REPORTS / "outreach" / "contacts.md"

    contacts: list[dict] = []
    frontmatter: dict = {}
    if contacts_path.exists():
        frontmatter, contacts = parse_contacts_md(contacts_path)
    else:
        print("[info] no contacts.md yet (Contacts tab will be empty)", file=sys.stderr)

    # NO server-side per-assumption filter. Assumption filtering lives in the
    # in-page dropdown (`fltAssumption`) — one HTML per idea, always.

    # Load copy from ALL assumptions' copy files so the tracker's assumption
    # filter can flip between them without regenerating.
    copy_by_id = _load_copy_by_contact()

    # Pain patterns live in the evidence ledger, one stage up from outreach —
    # they are cross-contact findings, not outreach mechanics.
    ev_path = REPORTS / "03-validation" / "evidence.md"
    patterns, evidence_entries = parse_evidence_md(ev_path)
    if ev_path.exists() and not _HAS_YAML:
        print("[warn] evidence.md present but PyYAML not installed; "
              f"Pain Patterns tab will show empty state.", file=sys.stderr)

    # Thesis layer — belief, hunch lineage, assumption graph, derived offerings.
    lineage_fm, hunches = parse_lineage_md(
        REPORTS / "01-ideation" / "hunch-lineage.md")
    graph_fm, assumptions = parse_graph_md(
        REPORTS / "02-assumptions" / "graph.md")
    # Wire the ledger onto the nodes. Without this every assumption card rendered
    # `none` for evidence while the ledger held entries pointing straight at it — the
    # cards read "untested / none" for H3A1-H3A3 on 2026-09-03 with six linked entries
    # on file. build_brief.py already did this; the control room never did, so the two
    # generated views of the same graph disagreed. Assumption-level strength is DERIVED
    # (CLAUDE.md) — never read `evidence_for:`/`evidence_against:` off the node.
    derive_assumption_evidence(assumptions, evidence_entries)
    offerings_fm, offerings = parse_offerings_md(
        REPORTS / "04-mutation" / "offerings.md")
    belief_path = BELIEF
    belief = _extract_belief(belief_path)
    belief_sections = _extract_belief_sections(belief_path)

    # Dated run artifacts + research, linked relative to control-room.html.
    # Scanned, never registered: a new artifact appears the moment it exists.
    artifacts: list[tuple[str, str]] = []
    ideation = REPORTS / "01-ideation"
    if ideation.is_dir():
        for f in sorted(ideation.glob("*-shotgun.md")):
            artifacts.append((f"01-ideation/{f.name}", f.stem.replace("-", " ")))
        for f in sorted(ideation.glob("recon/*/*.md")):
            rel = f.relative_to(REPORTS)
            artifacts.append((str(rel), f.stem.replace("-", " ")))

    # Company registry — the outreach-side landscape. One author: companies.md.
    companies_path = REPORTS / "outreach" / "companies.md"
    companies = parse_companies_md(companies_path)
    if companies_path.exists() and not _HAS_YAML:
        print("[warn] companies.md present but PyYAML not installed; "
              f"Companies tab will show empty state.", file=sys.stderr)
    thesis = {"lineage_fm": lineage_fm, "hunches": hunches, "graph_fm": graph_fm,
              "assumptions": assumptions, "offerings": offerings,
              "offerings_fm": offerings_fm, "belief": belief,
              "belief_sections": belief_sections, "artifacts": artifacts}

    html = render(frontmatter, contacts, copy_by_id=copy_by_id,
                  patterns=patterns, evidence_entries=evidence_entries,
                  thesis=thesis, companies=companies)

    # ONE file per idea. The outreach_tracker.html redirect stub that used to be
    # written here was removed on 2026-08-07 once the skills naming that path were
    # updated — a redirect nobody follows is just a second path to keep working.
    out = REPORTS / "control-room.html"
    _check_emitted_js(html)
    out.write_text(html, encoding="utf-8")
    write_results_files(contacts)
    print(f"[ok] wrote {out} ({len(contacts)} contacts, "
          f"{len(offerings)} offerings, {len(hunches)} hunches, "
          f"{len(companies[1])} companies)")
    return out


def _check_emitted_js(html: str) -> None:
    """Syntax-check every emitted <script> block with node before writing.

    A single bad line in the shared script block blanks the whole contact grid
    (happened 2026-08-25 via template quote-escaping), so a build that fails
    this check must fail loudly rather than publish. Skips silently when node
    is not installed.
    """
    import re as _re
    import shutil as _shutil
    import subprocess as _sp
    import tempfile as _tf

    node = _shutil.which("node")
    if not node:
        return
    for i, script in enumerate(_re.findall(r"<script>(.*?)</script>", html, _re.S)):
        with _tf.NamedTemporaryFile("w", suffix=".js", delete=False) as fh:
            fh.write(script)
            path = fh.name
        result = _sp.run([node, "--check", path], capture_output=True, text=True)
        if result.returncode != 0:
            raise SystemExit(
                f"[fail] emitted <script> block {i} does not parse — refusing to "
                f"write control-room.html\n{result.stderr[:800]}"
            )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.parse_args()

    # Refuse to build without PyYAML. Without it parse_graph_md / parse_offerings_md /
    # the evidence loader all return empty, and the script cheerfully overwrites a good
    # dashboard with one that has no Thesis assumptions, no Pain Patterns, no Offerings
    # and no Company Intel. That silent gutting is not noticed until the next session,
    # so it is a hard stop rather than a warning.
    if not _HAS_YAML:
        print(
            "[fatal] PyYAML is not available to this interpreter, so the assumption graph, "
            "offerings and evidence ledger cannot be parsed.\n"
            "        Refusing to overwrite the dashboard with a page missing those tabs.\n"
            "        Use the repo venv:  .venv/bin/python3 scripts/build_control_room.py\n"
            "        (or install it:     .venv/bin/python3 -m pip install -r requirements.txt)",
            file=sys.stderr)
        raise SystemExit(1)

    build()


if __name__ == "__main__":
    main()
