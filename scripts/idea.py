#!/usr/bin/env python3
"""One loader for the idea's artifacts — the single parsing authority.

Every consumer of an idea's files (`build_control_room.py`, `build_brief.py`,
`validate_repo.py`, `audit_target_list.py`) imports from here, so there is exactly
one implementation of each parse. This exists because there used to be three:
the tracker's record parser dropped every folded scalar (`key: >`), the audit
script had its own correct one for a single field, and the validator rolled its
own frontmatter reader — so the dashboard rendered blank rationale cards while
the audit read the same lines fine.

Two sanctioned encodings (see ARCHITECTURE.md → Folder Structure):

1. **YAML-block artifacts** — frontmatter + fenced ```yaml lists in the body
   (`graph.md` uses an unfenced `assumptions:` document; `evidence.md` and
   `offerings.md` use fences). Parsed by `parse_yaml_blocks` / `parse_graph_md`.
2. **Record files** — `## Heading` sections of `key: value` lines, folded
   scalars (`>` / `|`), inline `[a, b]` lists, `- item` block lists, and one
   level of nested mapping (`contacts.md`, `companies.md`, `transaction-map.md`).
   Parsed by `parse_record_file`.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
    _HAS_YAML = True
except ImportError:
    _HAS_YAML = False

REPO = Path(__file__).resolve().parent.parent
REPORTS = REPO / "reports"
INPUT_CONTEXT = REPO / "input-context"
BELIEF = INPUT_CONTEXT / "belief.md"

# A path segment carrying a date — `2026-08-06/`, `A5-2026-08-06/`,
# `audit-2026-08-09.md`. Dated artifacts are immutable snapshots: the brief
# collapses them, the validator does not ask them to declare a purpose. Living
# artifacts are everything else. Both consumers must agree on the definition,
# so it is declared once here.
DATED_PART = re.compile(r"(^|[-/])\d{4}-\d{2}(-\d{2})?([-/.]|$)")


# ─── frontmatter ─────────────────────────────────────────────────────────────


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split leading `---` YAML frontmatter from the body."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm = yaml.safe_load(text[3:end]) if _HAS_YAML else {}
    body = text[end + 4:]
    return (fm if isinstance(fm, dict) else {}), body.lstrip("\n")


def idea_name() -> str:
    """The idea's display name — `idea:` in belief.md frontmatter, else the repo folder.

    One idea per repo, so there is no slug: the folder IS the idea. The name is read
    from the belief file because that is the one founder-authored file that exists
    before anything else, and the repo folder name is the fallback for a repo with no
    belief yet.
    """
    if BELIEF.exists():
        fm, _ = parse_frontmatter(BELIEF.read_text(encoding="utf-8"))
        name = str(fm.get("idea") or "").strip()
        if name:
            return name
    return REPO.name


IDEA_NAME = None  # resolved lazily; import `idea_name()` for the live value


# ─── record files (## Heading + key: value) ──────────────────────────────────

# Keys that must always be lists even when empty, so `  - item` continuation
# lines never hit a str.
_LIST_KEYS = {"interviews", "assumptions_tested", "known_contacts"}


def _strip_quotes(v: str) -> str:
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in ("'", '"'):
        return v[1:-1]
    return v


def _parse_inline(v: str):
    """One inline value: quoted string, [a, b] list, or bare scalar."""
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        return [_strip_quotes(x) for x in inner.split(",") if x.strip()] if inner else []
    return _strip_quotes(v)


def parse_record_block(block: str, list_keys: frozenset | set = frozenset()) -> dict:
    """Parse one `## Heading` record into a dict.

    Handles: `key: value` · `key: >` / `key: |` folded scalars (text joined) ·
    `key:` + `- item` lists · `key:` + indented mapping (parsed as YAML, falls
    back to raw text) · legacy bare continuation lines after `signal_excerpt:`.
    """
    list_keys = set(list_keys) | _LIST_KEYS
    out: dict = {k: [] for k in list_keys if k in ("interviews", "assumptions_tested")}
    lines = block.splitlines()
    i = 0
    if lines and lines[0].startswith("## "):
        out["_heading"] = lines[0][3:].strip()
        i = 1

    def indented_block(start: int) -> tuple[list[str], int]:
        """Collect lines until the next column-0 content line."""
        got, j = [], start
        while j < len(lines):
            ln = lines[j]
            if ln.strip() == "":
                got.append("")
                j += 1
                continue
            if not ln.startswith((" ", "\t")):
                break
            got.append(ln)
            j += 1
        while got and got[-1] == "":
            got.pop()
        return got, j

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped or line.startswith((" ", "\t")) or ":" not in stripped:
            i += 1
            continue
        k, _, v = stripped.partition(":")
        k, v = k.strip(), v.strip()

        if v in (">", "|", ">-", "|-"):
            body, i = indented_block(i + 1)
            out[k] = " ".join(x.strip() for x in body if x.strip())
            continue

        if v == "":
            body, nxt = indented_block(i + 1)
            content = [x for x in body if x.strip()]
            if not content:
                out[k] = [] if k in list_keys else ""
            elif all(x.strip().startswith("- ") for x in content):
                out[k] = [_strip_quotes(x.strip()[2:]) for x in content]
            else:
                parsed = None
                if _HAS_YAML:
                    try:
                        doc = yaml.safe_load("\n".join(body))
                        if isinstance(doc, (dict, list)):
                            parsed = doc
                    except yaml.YAMLError:
                        parsed = None
                out[k] = parsed if parsed is not None else " ".join(
                    x.strip() for x in content)
            i = nxt
            continue

        out[k] = _parse_inline(v)
        # Legacy: bare indented continuation lines after an inline value
        # (historic signal_excerpt entries predate the `>` convention).
        if k == "signal_excerpt":
            body, i = indented_block(i + 1)
            extra = " ".join(x.strip() for x in body if x.strip())
            if extra:
                out[k] = f"{out[k]} {extra}".strip()
            continue
        i += 1
    return out


def parse_record_file(path: Path,
                      list_keys: frozenset | set = frozenset()) -> tuple[dict, list[dict]]:
    """Parse a record file into (frontmatter, records)."""
    if not path.exists():
        return {}, []
    text = path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    records = []
    for block in re.split(r"^## ", body, flags=re.MULTILINE)[1:]:
        records.append(parse_record_block("## " + block, list_keys))
    return frontmatter, records


def parse_contacts_md(path: Path) -> tuple[dict, list[dict]]:
    """Contacts: records keyed by `id:`, `name` mirrored from the heading."""
    frontmatter, records = parse_record_file(path)
    contacts = []
    for r in records:
        if not r.get("id"):
            continue
        r.setdefault("name", r.get("_heading", ""))
        contacts.append(r)
    return frontmatter, contacts


def parse_space_map(path: Path) -> list[dict]:
    """companies.md / transaction-map.md records. Tolerant: a company missing
    the mapping dimensions still appears, under 'unmapped'."""
    _, records = parse_record_file(path)
    return [c for c in records if c.get("canonical_name") or c.get("_heading")]


# ─── YAML-block artifacts ────────────────────────────────────────────────────


def parse_yaml_blocks(text: str) -> list:
    """All parsed ```yaml fences in a body, bad blocks skipped with a warning."""
    if not _HAS_YAML:
        return []
    out = []
    for block in re.findall(r"```yaml\n(.*?)```", text, re.S):
        try:
            out.append(yaml.safe_load(block) or {})
        except yaml.YAMLError as e:
            print(f"[warn] yaml block failed to parse: {e}", file=sys.stderr)
    return out


def parse_evidence_md(path: Path) -> tuple[list[dict], list[dict]]:
    """(patterns, entries) from the yaml blocks in 03-validation/evidence.md."""
    if not path.exists() or not _HAS_YAML:
        return [], []
    patterns: list[dict] = []
    entries: list[dict] = []
    for data in parse_yaml_blocks(path.read_text(encoding="utf-8")):
        if isinstance(data, dict):
            patterns.extend(data.get("patterns") or [])
            entries.extend(data.get("entries") or [])
    return patterns, entries


def parse_graph_md(path: Path) -> tuple[dict, list[dict]]:
    """(frontmatter, assumptions) from 02-assumptions/graph.md.

    The body carries prose (as `#` comments) before an unfenced YAML document,
    so the assumptions list is sliced from the `assumptions:` key.
    """
    if not path.exists() or not _HAS_YAML:
        return {}, []
    text = path.read_text(encoding="utf-8")
    fm, _ = parse_frontmatter(text)
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
    """(frontmatter, offerings) from 04-mutation/offerings.md."""
    if not path.exists() or not _HAS_YAML:
        return {}, []
    text = path.read_text(encoding="utf-8")
    fm, _ = parse_frontmatter(text)
    for data in parse_yaml_blocks(text):
        if isinstance(data, dict) and data.get("offerings"):
            return fm, data["offerings"]
    return fm, []


def extract_belief(path: Path) -> str:
    """The founder-confirmed belief — first prose block under `# Belief`.

    Accepts a blockquote or a plain paragraph. Intake records the founder's words
    verbatim and is told not to tidy them, so the `> ` marker is not guaranteed;
    requiring it made the brief announce "No belief.md — run /startup-belief-intake"
    for a belief that was present and confirmed, which misroutes the next session.
    """
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    m = re.search(r"(?m)^# Belief\s*\n+((?:> .*\n)+)", text)
    if m:
        return " ".join(l.lstrip("> ").strip() for l in m.group(1).splitlines()).strip()
    m = re.search(r"(?m)^# Belief\s*\n+(.+?)(?=\n\s*\n|\n#|\n<!--|\Z)", text, re.S)
    if not m:
        return ""
    body = re.sub(r"<!--.*?-->", "", m.group(1), flags=re.S)
    return " ".join(line.strip() for line in body.splitlines() if line.strip()).strip()


def parse_lineage_md(path: Path) -> tuple[dict, list[dict]]:
    """(frontmatter, hunches) from 01-ideation/hunch-lineage.md.

    Deliberately a light regex parse, not YAML — the lineage file is prose-first
    by design; only the leading key: value lines under each `## H{n}` heading
    are structured.
    """
    if not path.exists():
        return {}, []
    text = path.read_text(encoding="utf-8")
    fm, _ = parse_frontmatter(text)
    hunches = []
    for m in re.finditer(r"(?m)^## (H\d+)(?: —.*)?$", text):
        hid = m.group(1)
        nxt = text.find("\n## ", m.end())
        block = text[m.end(): nxt if nxt != -1 else len(text)]

        def fieldval(k, default=""):
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
        hunches.append({
            "id": hid,
            "status": fieldval("status", "unknown"),
            "created": fieldval("created"),
            "parent": fieldval("parent_hunch"),
            "change_reason": fieldval("change_reason"),
            "superseded_by": fieldval("superseded_by"),
            "statement": stmt,
        })
    hunches.sort(key=lambda h: h["id"])
    return fm, hunches


# ─── outreach funnel stats ───────────────────────────────────────────────────

STATUS_ORDER = ["pending", "invited", "accepted", "email_drafted", "email_sent",
                "questions_by_email", "replied", "scheduled", "done", "no_reply",
                "declined", "off_scope"]
ROLE_ORDER = ["buyer", "practitioner", "expert", "influencer"]
SIGNAL_ORDER = ["post_engagement", "comment_signal", "job_posting", "profile_fit"]

# A completed call is `interviewed`, and a sent message is `msg{N}_sent`. Both were
# once missing from these sets, so the one interview that actually happened counted
# as neither contacted, replied nor booked. Any msg{N}_sent counts as contacted.
#
# `accepted` is NOT contacted. A first invite carries no note (copy-rules LR-B29), so
# an accepted connection request is an opened door, not a message — the Msg 1 that
# follows lands as `msg1_sent`. Counting it here put nine people who had never been
# written to into the reply-rate denominator and turned 1 reply from 1 real message
# into a 10% reply rate. They still count as `outreach_started`, which is labelled
# "messaged or invited" and is true of them.
CONTACTED_STATUSES = {
    "replied", "scheduled", "done", "no_reply", "declined", "interviewed",
}
OUTREACH_STARTED_STATUSES = CONTACTED_STATUSES | {"invited", "accepted"}
REPLIED_STATUSES = {"replied", "scheduled", "done", "interviewed"}
SCHEDULED_STATUSES = {"scheduled", "done", "interviewed"}
CALL_PROGRESS_STAGES = {"offered_by_contact", "asked_by_founder", "scheduled", "completed"}
_MSG_SENT_RE = re.compile(r"^msg(\d+)_sent$")


def _non_customer_relationships() -> set[str]:
    """Which relationship_type values are excluded from qualified replies.

    Read from schemas/vocabularies.yaml (`non_customer: true`) rather than restated
    here: this set decides a headline number, and a hardcoded copy is exactly the
    kind of second author that drifts silently. Falls back to the one value that has
    always been in it if the vocabulary cannot be read, so a missing PyYAML degrades
    the stat rather than inverting it.
    """
    fallback = {"peer_founder_competitor"}
    if not _HAS_YAML:
        return fallback
    try:
        data = yaml.safe_load((REPO / "schemas" / "vocabularies.yaml").read_text(encoding="utf-8"))
        values = (data or {}).get("vocabularies", {}).get("relationship_type", {}).get("values", {})
    except (OSError, yaml.YAMLError):
        return fallback
    if not isinstance(values, dict):
        return fallback
    return {k for k, v in values.items() if isinstance(v, dict) and v.get("non_customer")} or fallback


NON_CUSTOMER_RELATIONSHIPS = _non_customer_relationships()


def _is_contacted(status) -> bool:
    """True once a message has actually gone out. Accepts any msg{N}_sent so a
    new message stage never silently drops contacts out of the funnel."""
    s = str(status or "")
    return s in CONTACTED_STATUSES or bool(_MSG_SENT_RE.match(s))


def _has_replied(status) -> bool:
    """True once the contact has answered at least once.

    msg2_sent and beyond imply a reply: the reply skill only drafts Msg 2 after a
    reply lands, so the arc stage is itself the evidence. Without this the reply
    count fell every time a thread advanced, because REPLIED_STATUSES is a plain
    set and msg{N}_sent is not in it.
    """
    s = str(status or "")
    if s in REPLIED_STATUSES:
        return True
    m = _MSG_SENT_RE.match(s)
    return bool(m) and int(m.group(1)) >= 2


def compute_stats(contacts: list[dict]) -> dict:
    from collections import Counter
    tiers = Counter((c.get("tier") or "other") for c in contacts)
    stats = {
        "total": len(contacts),
        "by_status": {s: 0 for s in STATUS_ORDER},
        "by_tier": {t: 0 for t, _ in sorted(tiers.items(), key=lambda kv: (-kv[1], kv[0]))},
        "by_role": {r: 0 for r in ROLE_ORDER},
        "by_signal": {s: 0 for s in SIGNAL_ORDER},
        "by_assumption": Counter(),
    }
    for c in contacts:
        for key, vocab_default, bucket in (
            ("outreach_status", "pending", "by_status"),
            ("tier", "other", "by_tier"),
            ("contact_role", "practitioner", "by_role"),
            ("signal_type", "profile_fit", "by_signal"),
        ):
            val = c.get(key) or vocab_default
            stats[bucket][val] = stats[bucket].get(val, 0) + 1
        for a in c.get("assumptions_tested", []):
            stats["by_assumption"][a] += 1
    stats["by_assumption"] = dict(stats["by_assumption"])
    return stats


DEFAULT_CHANNEL = "linkedin"


def _channel(c: dict) -> str:
    """How the contact was reached. Absent means linkedin, so old cards need no backfill."""
    return str(c.get("channel") or DEFAULT_CHANNEL)


def compute_conversion_stats(contacts: list[dict],
                             channel: str | None = DEFAULT_CHANNEL) -> dict:
    """The outreach funnel, without treating bare invites as messages.

    SCOPED BY CHANNEL. Five contacts reached by telephone were logged
    `outreach_status: replied` on 2026-09-03; being the only contacts with any status past
    `pending`, they made the LinkedIn funnel read 5 contacted / 5 replied = 100%. Someone
    who answered the phone has not replied to a LinkedIn message. Pass `channel=None` to
    compute across every channel at once.

    Call progression (offered/asked/booked) is deliberately separate from
    confirmed scheduling, so an accepted call invitation cannot render as 0%.
    """
    if channel is not None:
        contacts = [c for c in contacts if _channel(c) == channel]
    outreach_started = [
        c for c in contacts
        if c.get("outreach_status") in OUTREACH_STARTED_STATUSES
        or _is_contacted(c.get("outreach_status"))
    ]
    contacted = [c for c in contacts if _is_contacted(c.get("outreach_status"))]
    replied = [c for c in contacts if _has_replied(c.get("outreach_status"))]
    qualified_replied = [
        c for c in replied
        if c.get("relationship_type") not in NON_CUSTOMER_RELATIONSHIPS
    ]
    call_progressed = [
        c for c in replied
        if c.get("call_stage") in CALL_PROGRESS_STAGES
        or c.get("outreach_status") in SCHEDULED_STATUSES
    ]
    scheduled = [c for c in contacts if c.get("outreach_status") in SCHEDULED_STATUSES]

    def pct(n: int, d: int) -> float | None:
        return round(100 * n / d, 1) if d else None

    by_assumption = {}
    for aid in sorted({a for c in contacts for a in (c.get("assumptions_tested") or [])}):
        cohort = [c for c in contacts if aid in (c.get("assumptions_tested") or [])]
        cohort_contacted = [c for c in cohort if _is_contacted(c.get("outreach_status"))]
        cohort_replied = [c for c in cohort if _has_replied(c.get("outreach_status"))]
        cohort_qualified = [
            c for c in cohort_replied
            if c.get("relationship_type") not in NON_CUSTOMER_RELATIONSHIPS
        ]
        by_assumption[aid] = {
            "targeted": len(cohort),
            "contacted": len(cohort_contacted),
            "replied": len(cohort_replied),
            "qualified_replied": len(cohort_qualified),
            "reply_rate": pct(len(cohort_replied), len(cohort_contacted)),
            "qualified_reply_rate": pct(len(cohort_qualified), len(cohort_contacted)),
        }

    return {
        "targeted": len(contacts),
        "outreach_started": len(outreach_started),
        "contacted": len(contacted),
        "replied": len(replied),
        "qualified_replied": len(qualified_replied),
        "call_progressed": len(call_progressed),
        "scheduled": len(scheduled),
        "target_to_contact_rate": pct(len(outreach_started), len(contacts)),
        "reply_rate": pct(len(replied), len(contacted)),
        "qualified_reply_rate": pct(len(qualified_replied), len(contacted)),
        "reply_to_call_rate": pct(len(call_progressed), len(replied)),
        "reply_to_scheduled_rate": pct(len(scheduled), len(replied)),
        "by_assumption": by_assumption,
    }


# ─── derived assumption evidence (the one evidence scale) ────────────────────


def derive_assumption_evidence(assumptions: list[dict], entries: list[dict]) -> None:
    """Annotate each assumption with evidence strength derived from its entries.

    The per-entry `confidence` 1–5 is the ONE hand-assigned evidence grade in
    the repo (schemas/vocabularies.yaml → evidence_confidence). Everything at
    assumption level is computed here and never hand-written, so it cannot
    drift from the ledger:

      evidence_n            linked entry count
      evidence_best         max linked confidence (0 = no evidence)
      evidence_supports / evidence_contradicts / evidence_ambiguous
      confidence            low (best ≤2) · medium (=3) · high (≥4)
    """
    by_aid: dict[str, list[dict]] = {}
    for e in entries:
        aid = str(e.get("assumption_linked") or "")
        if aid:
            by_aid.setdefault(aid, []).append(e)
    for a in assumptions:
        mine = by_aid.get(str(a.get("id") or ""), [])
        confs = [e.get("confidence") for e in mine if isinstance(e.get("confidence"), int)]
        best = max(confs, default=0)
        a["evidence_n"] = len(mine)
        a["evidence_best"] = best
        for verdict in ("supports", "contradicts", "ambiguous"):
            a[f"evidence_{verdict}"] = sum(
                1 for e in mine if (e.get("verdict") or "").strip() == verdict)
        a["confidence"] = "high" if best >= 4 else ("medium" if best == 3 else "low")


def evidence_label(a: dict) -> str:
    """Short human form of the derived strength, e.g. `4/5 · 9E (5+/3-)`."""
    n = a.get("evidence_n") or 0
    if not n:
        return "none"
    return "%d/5 · %dE (%d+/%d-)" % (
        a.get("evidence_best") or 0, n,
        a.get("evidence_supports") or 0, a.get("evidence_contradicts") or 0)


# ─── the loader ──────────────────────────────────────────────────────────────


@dataclass
class Idea:
    name: str
    belief: str = ""
    lineage_fm: dict = field(default_factory=dict)
    hunches: list = field(default_factory=list)
    graph_fm: dict = field(default_factory=dict)
    assumptions: list = field(default_factory=list)
    patterns: list = field(default_factory=list)
    evidence: list = field(default_factory=list)
    offerings_fm: dict = field(default_factory=dict)
    offerings: list = field(default_factory=list)
    contacts_fm: dict = field(default_factory=dict)
    contacts: list = field(default_factory=list)
    companies: list = field(default_factory=list)

    @property
    def idea_dir(self) -> Path:
        return REPORTS


def load_idea() -> Idea:
    """Load every parsed artifact for the idea. Missing files load as empty."""
    idea_dir = REPORTS
    lineage_fm, hunches = parse_lineage_md(idea_dir / "01-ideation" / "hunch-lineage.md")
    graph_fm, assumptions = parse_graph_md(idea_dir / "02-assumptions" / "graph.md")
    patterns, evidence = parse_evidence_md(idea_dir / "03-validation" / "evidence.md")
    offerings_fm, offerings = parse_offerings_md(idea_dir / "04-mutation" / "offerings.md")
    contacts_fm, contacts = parse_contacts_md(idea_dir / "outreach" / "contacts.md")
    companies = parse_space_map(idea_dir / "outreach" / "companies.md")
    derive_assumption_evidence(assumptions, evidence)
    return Idea(
        name=idea_name(),
        belief=extract_belief(BELIEF),
        lineage_fm=lineage_fm, hunches=hunches,
        graph_fm=graph_fm, assumptions=assumptions,
        patterns=patterns, evidence=evidence,
        offerings_fm=offerings_fm, offerings=offerings,
        contacts_fm=contacts_fm, contacts=contacts,
        companies=companies,
    )
