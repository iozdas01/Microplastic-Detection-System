from __future__ import annotations

import unittest
from unittest.mock import patch

from scripts.data.community_recon import collect, dry_run, validate_plan


class CommunityReconTests(unittest.TestCase):
    def setUp(self) -> None:
        self.plan = validate_plan({
            "belief": "Operational teams will need new coordination tools.",
            "current_hunch": {
                "id": "H1",
                "statement": (
                    "Operations teams lose time because manual review queues "
                    "require repeated handoffs."
                ),
            },
            "mode": "initial_test",
            "hypotheses": [{
                "id": "P1",
                "label": "Manual review bottleneck",
                "queries": [
                    "manual review workaround",
                    "review process nightmare",
                ],
                "subreddits": ["operations"],
            }],
        })

    def test_plan_validation_and_dry_run(self) -> None:
        result = dry_run(self.plan, {"reddit", "hn"})
        self.assertTrue(result["valid"])
        self.assertEqual(result["planned_calls"]["reddit"], 1)
        self.assertEqual(result["planned_calls"]["hacker_news"], 1)
        self.assertEqual(result["plan"]["current_hunch"]["id"], "H1")

    def test_plan_requires_active_hunch(self) -> None:
        with self.assertRaisesRegex(ValueError, "current_hunch is required"):
            validate_plan({
                "belief": "A belief",
                "hypotheses": [{"id": "P1", "queries": ["workflow pain"]}],
            })

    def test_plan_requires_queries(self) -> None:
        with self.assertRaisesRegex(ValueError, "has no queries"):
            validate_plan({
                "belief": "A belief",
                "current_hunch": {
                    "id": "H1",
                    "statement": "A founder-confirmed hunch",
                },
                "hypotheses": [{"id": "P1", "queries": []}],
            })

    @patch("scripts.data.community_recon.is_enabled", return_value=True)
    @patch("scripts.data.community_recon.search_hn")
    @patch("scripts.data.community_recon.search_reddit")
    def test_extracted_reddit_text_can_supply_behavioral_workaround(
        self,
        reddit_search,
        hn_search,
        _is_enabled,
    ) -> None:
        reddit_search.return_value = [{
            "title": "Closed systems create handoffs",
            "selftext": (
                "The CRM cannot talk to dispatch, so we built a spreadsheet "
                "and manually copy every record before each shift."
            ),
            "url": "https://reddit.com/r/operations/comments/workaround",
            "subreddit": "operations",
            "query": "manual review workaround",
            "comments": [],
            "provider": "firecrawl",
        }]
        hn_search.return_value = {"comments": [], "stories": [], "errors": []}

        result = collect(self.plan, sources={"reddit"}, reddit_limit=5)

        self.assertEqual(result["summary"]["workaround_records"], 1)
        self.assertIn(
            "we built a spreadsheet",
            result["records"][0]["workaround_snippets"][0].lower(),
        )

    @patch("scripts.data.community_recon.is_enabled", return_value=True)
    @patch("scripts.data.community_recon.search_hn")
    @patch("scripts.data.community_recon.search_reddit")
    def test_collect_normalizes_and_deduplicates(
        self,
        reddit_search,
        hn_search,
        _is_enabled,
    ) -> None:
        reddit_search.return_value = [{
            "title": "How do you handle manual review?",
            "selftext": "Our queue takes days.",
            "url": "https://reddit.com/r/operations/comments/example",
            "score": 12,
            "num_comments": 7,
            "created_utc": "2026-07-01T00:00:00",
            "subreddit": "operations",
            "query": "manual review workaround",
            "flair": "Ops manager",
            "comments": [{
                "body": "We built a spreadsheet and a script.",
                "score": 8,
                "is_workaround": True,
            }],
        }]
        hn_search.return_value = {
            "comments": [{
                "type": "comment",
                "query": "manual review workaround",
                "body": "We rolled our own review queue.",
                "points": 3,
                "created_utc": "2026-07-02T00:00:00",
                "story_title": "Review tooling",
                "comment_url": "https://news.ycombinator.com/item?id=123",
                "object_id": "123",
                "is_workaround": True,
            }],
            "stories": [],
            "errors": [],
        }

        result = collect(self.plan, reddit_limit=5, hn_hits=10)

        self.assertEqual(result["summary"]["records"], 2)
        self.assertEqual(result["summary"]["workaround_records"], 2)
        self.assertEqual(result["status"]["reddit"]["records"], 1)
        self.assertEqual(result["status"]["hacker_news"]["records"], 1)
        reddit_record = next(
            record for record in result["records"] if record["source"] == "reddit"
        )
        self.assertEqual(reddit_record["hypothesis_ids"], ["P1"])
        self.assertEqual(reddit_record["provider"], "unknown")
        self.assertIn("spreadsheet", reddit_record["workaround_snippets"][0])


if __name__ == "__main__":
    unittest.main()


class HnRelevanceFilterTests(unittest.TestCase):
    """Algolia's removeWordsIfNoResults silently degrades long queries to
    near-anything (a 2026-08-20 recon run shipped 1,475 HN records led by TTRPG
    tools). matches_query re-imposes relevance client-side."""

    def test_requires_half_the_content_words(self) -> None:
        from scripts.data.hn import matches_query

        self.assertTrue(matches_query(
            "verify toolpath before cutting",
            "I always verify the toolpath in Vericut before cutting real stock"))
        self.assertFalse(matches_query(
            "verify toolpath before cutting",
            "Show HN: an AI campaign memory engine for tabletop games"))
        self.assertFalse(matches_query(
            "not worth automating low volume",
            "hyperscalers are toast, on-prem efficiency"))

    def test_single_word_and_empty_queries_stay_permissive(self) -> None:
        from scripts.data.hn import matches_query

        self.assertTrue(matches_query("spreadsheet", "we track it in a spreadsheet"))
        self.assertTrue(matches_query("the of an", "anything at all"))
