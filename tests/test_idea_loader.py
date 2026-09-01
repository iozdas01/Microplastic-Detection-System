"""Tests for scripts/idea.py — the one parsing authority.

The whole generated-artifact chain (BRIEF.md, dashboard.html, the audit, the
pre-commit gate) reads through this module, and its predecessor silently
discarded every folded scalar in contacts.md. These tests pin the behaviours
that bug hid.
"""

import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.idea import (  # noqa: E402
    compute_conversion_stats,
    parse_frontmatter,
    parse_graph_md,
    parse_evidence_md,
    parse_record_block,
    parse_record_file,
)


# ─── record blocks ───────────────────────────────────────────────────────────


def test_folded_scalar_is_joined_not_dropped():
    block = textwrap.dedent("""\
        ## Jane Doe
        id: C1
        notes: >
          First line of the rationale,
          second line with detail.
        role: Robotics Lead
        """)
    rec = parse_record_block(block)
    assert rec["notes"] == "First line of the rationale, second line with detail."
    assert rec["role"] == "Robotics Lead"


def test_folded_scalar_with_blank_lines_and_colons():
    block = textwrap.dedent("""\
        ## X
        validation_rationale: >
          Paragraph one: has a colon.

          Paragraph two after a blank line.
        tier: buyer
        """)
    rec = parse_record_block(block)
    assert "Paragraph one: has a colon." in rec["validation_rationale"]
    assert "Paragraph two" in rec["validation_rationale"]
    assert rec["tier"] == "buyer"


def test_inline_and_block_lists():
    block = textwrap.dedent("""\
        ## X
        id: C2
        assumptions_tested: [A2, A4]
        interviews:
          - reports/x/notes-1.md
          - "reports/x/notes-2.md"
        """)
    rec = parse_record_block(block)
    assert rec["assumptions_tested"] == ["A2", "A4"]
    assert rec["interviews"] == ["reports/x/notes-1.md", "reports/x/notes-2.md"]


def test_empty_list_keys_stay_lists():
    rec = parse_record_block("## X\nid: C3\ninterviews:\n")
    assert rec["interviews"] == []
    assert rec["assumptions_tested"] == []


def test_nested_mapping_parses_as_dict():
    block = textwrap.dedent("""\
        ## Nike
        canonical_name: Nike
        linkedin_targets:
          titles: [Automation Engineer, Manufacturing Innovation]
          search_terms:
            - "Nike advanced manufacturing"
        pain_score: 10
        """)
    rec = parse_record_block(block)
    assert rec["linkedin_targets"]["titles"] == [
        "Automation Engineer", "Manufacturing Innovation"]
    assert rec["linkedin_targets"]["search_terms"] == ["Nike advanced manufacturing"]
    assert rec["pain_score"] == "10"


def test_signal_excerpt_legacy_continuation():
    block = textwrap.dedent("""\
        ## X
        id: C4
        signal_excerpt: started inline
          continued on the next indented line
        company: Acme
        """)
    rec = parse_record_block(block)
    assert rec["signal_excerpt"] == "started inline continued on the next indented line"
    assert rec["company"] == "Acme"


def test_quotes_are_stripped():
    rec = parse_record_block('## X\nrole: "buyer_company"\nnote: \'single\'\n')
    assert rec["role"] == "buyer_company"
    assert rec["note"] == "single"


# ─── record files ────────────────────────────────────────────────────────────


def test_record_file_frontmatter_and_records(tmp_path):
    f = tmp_path / "contacts.md"
    f.write_text(textwrap.dedent("""\
        ---
        idea: test-idea
        purpose: "Test file."
        ---

        # Contacts

        ## Alice
        id: C1
        outreach_status: replied

        ## Bob
        id: C2
        outreach_status: pending
        """))
    fm, records = parse_record_file(f)
    assert fm["idea"] == "test-idea"
    assert [r["_heading"] for r in records] == ["Alice", "Bob"]


def test_missing_file_is_empty():
    fm, records = parse_record_file(Path("/nonexistent/file.md"))
    assert fm == {} and records == []


def test_frontmatter_requires_line_start_delimiter():
    fm, body = parse_frontmatter("---\nkey: a---b\nother: 1\n---\nBody\n")
    assert fm == {"key": "a---b", "other": 1}
    assert body == "Body\n"


# ─── yaml-block artifacts ────────────────────────────────────────────────────


def test_evidence_blocks(tmp_path):
    f = tmp_path / "evidence.md"
    f.write_text(textwrap.dedent("""\
        ---
        idea: test
        ---

        ## Entries

        ```yaml
        entries:
          - id: E1
            claim: >
              Something was said.
            verdict: supports
            confidence: 3
        ```
        """))
    patterns, entries = parse_evidence_md(f)
    assert patterns == []
    assert entries[0]["id"] == "E1"
    assert entries[0]["confidence"] == 3


def test_graph_unfenced_yaml(tmp_path):
    f = tmp_path / "graph.md"
    f.write_text(textwrap.dedent("""\
        ---
        idea: test
        active_assumption: A1
        ---

        # Graph

        # prose comment line

        assumptions:
          - id: A1
            assumption: "Pain exists."
            status: untested
        """))
    fm, assumptions = parse_graph_md(f)
    assert fm["active_assumption"] == "A1"
    assert assumptions[0]["id"] == "A1"


# ─── funnel stats ────────────────────────────────────────────────────────────


def test_msg_sent_counts_as_contacted_and_arc_stage_implies_reply():
    """msg1_sent is contact only; msg2_sent implies a reply, because the reply
    skill only drafts Msg 2 after one lands. Without that, the reply count fell
    every time a thread advanced."""
    contacts = [
        {"id": "C1", "outreach_status": "msg1_sent", "assumptions_tested": ["H2A2"]},
        {"id": "C2", "outreach_status": "msg2_sent", "assumptions_tested": ["H2A2"]},
        {"id": "C3", "outreach_status": "interviewed", "assumptions_tested": ["H2A2"]},
        {"id": "C4", "outreach_status": "invited", "assumptions_tested": ["H2A2"]},
        {"id": "C5", "outreach_status": "pending", "assumptions_tested": []},
    ]
    conv = compute_conversion_stats(contacts)
    assert conv["contacted"] == 3          # msg1_sent, msg2_sent, interviewed; invited is not
    assert conv["replied"] == 2            # msg2_sent + interviewed
    assert conv["scheduled"] == 1          # interviewed counts as scheduled
    assert conv["by_assumption"]["H2A2"]["targeted"] == 4
    assert conv["by_assumption"]["H2A2"]["contacted"] == 3


def test_peer_founders_excluded_from_qualified():
    contacts = [
        {"id": "C1", "outreach_status": "replied",
         "relationship_type": "peer_founder_competitor", "assumptions_tested": ["A2"]},
        {"id": "C2", "outreach_status": "replied", "assumptions_tested": ["A2"]},
    ]
    conv = compute_conversion_stats(contacts)
    assert conv["replied"] == 2
    assert conv["qualified_replied"] == 1
