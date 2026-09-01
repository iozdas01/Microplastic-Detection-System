from __future__ import annotations

from pathlib import Path
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def read_skill(name: str) -> str:
    """A skill's full definition: SKILL.md plus everything in its references/.

    The contract these tests pin is about what the skill guarantees, not which
    file the sentence sits in. Skills were split into a decision procedure plus
    references/ mechanics on 2026-08-09; reading both keeps the assertions
    meaningful instead of pinning a layout.
    """
    base = ROOT / ".claude" / "skills" / name
    parts = [(base / "SKILL.md").read_text(encoding="utf-8")]
    refs = base / "references"
    if refs.is_dir():
        parts += [f.read_text(encoding="utf-8") for f in sorted(refs.glob("*.md"))]
    return "\n".join(parts)


def frontmatter(relative_path: str) -> dict:
    text = read(relative_path)
    if not text.startswith("---\n"):
        raise AssertionError(f"{relative_path} has no YAML frontmatter")
    raw = text.split("---\n", 2)[1]
    return yaml.safe_load(raw)


class FounderHunchHandoffTests(unittest.TestCase):
    def test_intake_writes_the_belief_and_never_a_hunch(self) -> None:
        """Intake owns the belief. The shotgun owns every hunch.

        Contract changed 2026-08-20 (founder decision). Intake used to end with a
        founder-confirmed H1, which meant the first hunch came from the founder's
        imagination at the moment they knew least. It now writes an empty lineage and
        hands to shotgun explore, so the first hunch is proposed from a real corpus.
        """
        skill = read_skill("startup-belief-intake")

        self.assertIn("input-context/{slug}/belief.md", skill)
        self.assertIn("reports/{slug}/01-ideation/hunch-lineage.md", skill)
        self.assertIn("active_hunch: none", skill)

        # Initialization steps that were silently missing and left every new idea's
        # brief reading `lifecycle: unknown`.
        self.assertIn("reports/lifecycle.yaml", skill)
        self.assertIn("scripts/build_brief.py", skill)

        # The drill-down and the research grounding are what replaced the funnel.
        self.assertIn("Drill down", skill)
        self.assertIn("definitional", skill)

        # No hunch may be authored here, in any form.
        self.assertNotIn("status: active", skill)
        self.assertNotIn("validation_status: untested", skill)
        self.assertNotIn("active_hunch: H1", skill)
        self.assertNotIn("Formulate the initial hunch", skill)

    def test_shotgun_scopes_the_hunch_requirement_to_the_test_modes(self) -> None:
        skill = read_skill("startup-ideate-shotgun")

        self.assertIn("Every method receives this exact manifest", skill)
        self.assertIn(
            "must not select a different hunch, segment, or pain cluster",
            skill,
        )
        self.assertIn("### 9. Founder decision gate", skill)

        # Explore mode exists...
        self.assertIn("**Explore**", skill)
        # ...and the two guardrails that make it safe are stated, not implied.
        self.assertIn("Never sets `active_hunch`", skill)
        self.assertIn("blocks explore mode", skill)

    def test_only_explore_may_omit_the_hunch(self) -> None:
        """Behavioural, not a source grep — the guard has to actually hold.

        The previous version asserted the string `"mode": "explore"` was absent from
        the collector, which pinned the old design rather than the property worth
        keeping: a mode with a hunch must carry one, and explore must not smuggle one in.
        """
        from scripts.data.community_recon import validate_plan

        hypotheses = [
            {
                "id": "P1",
                "label": "Possible workflow pain",
                "queries": ["manual reconciliation workaround"],
                "subreddits": ["operations"],
            }
        ]
        hunch = {"id": "H1", "statement": "A falsifiable claim"}

        explore = validate_plan(
            {"belief": "b", "mode": "explore", "hypotheses": hypotheses}
        )
        self.assertIsNone(explore["current_hunch"])

        tested = validate_plan(
            {
                "belief": "b",
                "mode": "initial_test",
                "current_hunch": hunch,
                "hypotheses": hypotheses,
            }
        )
        self.assertEqual(tested["current_hunch"], hunch)

        rejected = [
            ({"belief": "b", "mode": "initial_test", "hypotheses": hypotheses},
             "a test mode with no hunch"),
            ({"belief": "b", "mode": "reframe", "hypotheses": hypotheses},
             "reframe with no hunch"),
            ({"belief": "b", "mode": "explore", "current_hunch": hunch,
              "hypotheses": hypotheses},
             "explore carrying a hunch"),
            ({"belief": "", "mode": "explore", "hypotheses": hypotheses},
             "explore with no belief"),
            ({"belief": "b", "mode": "explore", "hypotheses": []},
             "explore with no hypotheses"),
        ]
        for payload, description in rejected:
            with self.subTest(plan=description):
                with self.assertRaises(ValueError):
                    validate_plan(payload)


class ShotgunRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.routing = yaml.safe_load(read("methods/shotgun-routing.yaml"))

    def test_routing_declares_three_modes_with_scoped_subjects(self) -> None:
        self.assertEqual(self.routing["version"], 5)

        modes = self.routing["run_modes"]
        self.assertEqual(
            sorted(modes), ["explore", "initial_test", "reframe"]
        )
        self.assertEqual(modes["explore"]["requires"], ["belief"])
        self.assertEqual(modes["explore"]["forbids"], ["current_hunch"])
        for name in ("initial_test", "reframe"):
            with self.subTest(mode=name):
                self.assertIn("current_hunch", modes[name]["requires"])

        self.assertEqual(self.routing["selection"]["max_parallel_agents"], 3)

    def test_explore_pool_cannot_activate_its_own_proposal(self) -> None:
        """The guardrail the whole mode rests on.

        Explore may PROPOSE hunches; only the founder promotes one to active. If this
        ever fails, a machine-generated hunch can become the run subject of its own
        test, and the pipeline is agreeing with itself.
        """
        stages = self.routing["explore_pool"]["stages"]
        self.assertEqual([s["id"] for s in stages], ["collect", "interpret", "propose"])

        propose = stages[-1]
        self.assertEqual(propose["writes"]["status"], "proposed")
        self.assertTrue(
            any("active_hunch" in rule for rule in propose["forbids"]),
            "explore_pool must explicitly forbid setting active_hunch",
        )

        # Explore runs collection plus interpretation only. None of the pressure-test
        # lenses may appear: they exist to attack a claim, and there is no claim yet.
        explore_methods = {stages[0]["method"]} | {
            m["method"] for m in stages[1]["methods"]
        }
        for banned in (
            "methods/ideation/five-whys.md",
            "methods/ideation/why-now-predecessor-analysis.md",
            "methods/ideation/inversion.md",
            "methods/ideation/nagging-number.md",
        ):
            with self.subTest(method=banned):
                self.assertNotIn(banned, explore_methods)

    def test_every_lens_requires_current_hunch_and_has_execution_metadata(
        self,
    ) -> None:
        for family_name, family in self.routing["lens_families"].items():
            with self.subTest(family=family_name):
                self.assertIn("current_hunch", family["prerequisites"])
                self.assertIn("stage", family["execution"])
                self.assertIn("mode", family["execution"])
                self.assertIn("order", family["execution"])

    def test_dependency_order_is_explicit(self) -> None:
        families = self.routing["lens_families"]

        self.assertEqual(
            families["segment_and_wedge"]["execution"]["depends_on"],
            ["job_and_substitute"],
        )
        self.assertEqual(
            families["timing_and_predecessors"]["execution"]["depends_on"],
            ["root_cause", "job_and_substitute", "segment_and_wedge"],
        )
        self.assertEqual(
            [stage["id"] for stage in self.routing["execution_stages"]],
            ["interpretation", "targeted_research", "synthesis"],
        )

    def test_every_ideation_card_is_routed_once_with_scoped_prerequisites(
        self,
    ) -> None:
        routed_paths = [self.routing["pre_lens"]["method"]]
        for family in self.routing["lens_families"].values():
            routed_paths.append(family["primary"])
            routed_paths.extend(
                alternative["method"]
                for alternative in family.get("alternatives", [])
            )

        ideation_paths = sorted(
            str(path.relative_to(ROOT))
            for path in (ROOT / "methods/ideation").glob("*.md")
        )

        self.assertEqual(sorted(routed_paths), ideation_paths)
        self.assertEqual(len(routed_paths), len(set(routed_paths)))

        # Cards the explore pool uses declare `belief` and take collected evidence as
        # their subject; every other card still requires a hunch to interpret.
        explore_stages = self.routing["explore_pool"]["stages"]
        explore_methods = {explore_stages[0]["method"]} | {
            m["method"] for m in explore_stages[1]["methods"]
        }

        for relative_path in ideation_paths:
            with self.subTest(method=relative_path):
                metadata = frontmatter(relative_path)
                requires = metadata.get("requires", [])
                self.assertIn("belief", requires)
                if relative_path not in explore_methods:
                    self.assertIn("current_hunch", requires)
                self.assertIn("shotgun_family", metadata)
                self.assertIn("shotgun_role", metadata)


if __name__ == "__main__":
    unittest.main()
