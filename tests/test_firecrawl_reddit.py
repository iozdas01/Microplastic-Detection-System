from __future__ import annotations

import unittest
from unittest.mock import Mock, patch

from scripts.data.firecrawl import search_reddit
from scripts.data.reddit import search


class FirecrawlAdapterTests(unittest.TestCase):
    @patch("scripts.data.firecrawl.is_enabled", return_value=True)
    @patch("scripts.data.firecrawl.requests.post")
    def test_search_normalizes_only_reddit_results(
        self,
        post: Mock,
        _enabled: Mock,
    ) -> None:
        response = Mock(status_code=200)
        response.json.return_value = {
            "success": True,
            "data": {
                "web": [
                    {
                        "title": "Manual review is exhausting",
                        "description": "We still reconcile this in a spreadsheet.",
                        "markdown": (
                            "The original post describes manual review.\n\n"
                            "Comments Section\n\nWe built a spreadsheet workaround."
                        ),
                        "url": (
                            "https://www.reddit.com/r/operations/"
                            "comments/example/manual_review/"
                        ),
                    },
                    {
                        "title": "Unrelated",
                        "description": "Not Reddit",
                        "url": "https://example.com/manual-review",
                    },
                ],
            },
        }
        post.return_value = response

        rows = search_reddit(
            "manual review workaround",
            subreddit="operations",
            limit=5,
            time_filter="year",
        )

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["provider"], "firecrawl")
        self.assertEqual(rows[0]["subreddit"], "operations")
        self.assertIn("Comments Section", rows[0]["selftext"])
        request = post.call_args
        self.assertTrue(request.args[0].endswith("/v2/search"))
        self.assertEqual(request.kwargs["json"]["includeDomains"], ["reddit.com"])
        self.assertEqual(
            request.kwargs["json"]["scrapeOptions"],
            {"formats": ["markdown"], "onlyMainContent": True},
        )
        self.assertEqual(
            request.kwargs["json"]["query"],
            "manual review workaround operations",
        )
        self.assertEqual(request.kwargs["json"]["tbs"], "qdr:y")

    @patch("scripts.data.firecrawl.is_enabled", return_value=True)
    @patch("scripts.data.firecrawl.requests.post")
    def test_search_falls_back_from_v2_to_v1(
        self,
        post: Mock,
        _enabled: Mock,
    ) -> None:
        missing = Mock(status_code=404)
        success = Mock(status_code=200)
        success.json.return_value = {
            "success": True,
            "data": [{
                "title": "A Reddit result",
                "url": "https://reddit.com/r/startups/comments/example/",
            }],
        }
        post.side_effect = [missing, success]

        rows = search_reddit("workflow pain", subreddit="startups")

        self.assertEqual(len(rows), 1)
        self.assertTrue(post.call_args_list[1].args[0].endswith("/v1/search"))

    @patch("scripts.data.firecrawl.is_enabled", return_value=True)
    @patch("scripts.data.firecrawl.requests.post")
    def test_empty_subreddit_hint_retries_unscoped_query(
        self,
        post: Mock,
        _enabled: Mock,
    ) -> None:
        empty = Mock(status_code=200)
        empty.json.return_value = {"success": True, "data": {"web": []}}
        success = Mock(status_code=200)
        success.json.return_value = {
            "success": True,
            "data": {
                "web": [{
                    "title": "A broader Reddit result",
                    "url": "https://reddit.com/r/operations/comments/example/",
                }],
            },
        }
        post.side_effect = [empty, success]

        rows = search_reddit("workflow pain", subreddit="startups")

        self.assertEqual(len(rows), 1)
        self.assertEqual(post.call_count, 2)
        self.assertEqual(
            post.call_args_list[0].kwargs["json"]["query"],
            "workflow pain startups",
        )
        self.assertEqual(
            post.call_args_list[1].kwargs["json"]["query"],
            "workflow pain",
        )


class RedditProviderOrderTests(unittest.TestCase):
    @patch("scripts.data.reddit._json_fallback_scrape")
    @patch("scripts.data.reddit._try_praw")
    @patch("scripts.data.reddit.search_firecrawl")
    @patch("scripts.data.reddit.is_enabled", return_value=True)
    def test_firecrawl_is_primary(
        self,
        _enabled: Mock,
        firecrawl: Mock,
        praw: Mock,
        json_fallback: Mock,
    ) -> None:
        firecrawl.return_value = [{
            "title": "Result",
            "url": "https://reddit.com/r/startups/comments/example/",
            "provider": "firecrawl",
        }]

        rows = search(["startups"], ["workflow pain"], limit_top=5)

        self.assertEqual(rows[0]["provider"], "firecrawl")
        praw.assert_not_called()
        json_fallback.assert_not_called()

    @patch("scripts.data.reddit._json_fallback_scrape")
    @patch("scripts.data.reddit._try_praw", return_value=None)
    @patch("scripts.data.reddit.search_firecrawl")
    @patch("scripts.data.reddit.is_enabled", return_value=True)
    def test_json_remains_last_fallback(
        self,
        _enabled: Mock,
        firecrawl: Mock,
        _praw: Mock,
        json_fallback: Mock,
    ) -> None:
        firecrawl.return_value = [{
            "error": "service unavailable",
            "provider": "firecrawl",
        }]
        json_fallback.return_value = [{
            "title": "Fallback",
            "provider": "reddit_json",
        }]

        rows = search(["startups"], ["workflow pain"], limit_top=5)

        self.assertEqual(rows[0]["provider"], "reddit_json")
        self.assertEqual(rows[1]["provider"], "firecrawl")


if __name__ == "__main__":
    unittest.main()
