# Schema: Method Card

One file per method. Lives in /methods/ideation/, /methods/validation/, /methods/mutation/, or
/methods/practices/ depending on primary use — a method goes to its most natural home, even if
it spans phases. See the Folder Assignment Guide below; `practices/` is the one cut that is not
about phase.

```yaml
name: ""
category:                       # see canonical list below — pick exactly one
applicable_at:                  # see phase list below — list all that apply
assumption_categories_it_helps: # see assumption categories below — list all that apply
shotgun_family:                 # optional; family in methods/shotgun-routing.yaml
shotgun_role:                   # optional: primary / alternative / downstream
requires:                       # optional artifact prerequisites for orchestration
  - belief

core_insight: ""                # WHY this method works — the mechanism, not just the steps
process:                        # numbered steps to execute it
  - step 1
  - step 2

example: |
  # concrete illustration — ideally from a real startup or historical case, named

limitations: |
  # when NOT to use this / where it breaks down

source:
  title: ""
  author: ""
  url: ""
  date: ""
```

---

## Canonical Categories

Pick exactly one. If two apply equally, use the more specific one.

| Category | What it means |
|---|---|
| `analogical` | Draw reasoning from a similar company, domain, or historical situation |
| `inversion` | Flip the problem, frame, or assumption to reveal what's hidden |
| `constraint-removal` | Lift a binding constraint (cost, regulation, technology) and design from the relaxed world |
| `jtbd` | Jobs-to-be-done: what is the customer actually hiring a product to do? |
| `adjacency` | Look sideways — adjacent market, geography, value chain position, or customer segment |
| `market-signal` | Actively mine market signals: trends, competitor moves, communities, statistical outliers |
| `signal-detection` | Notice organic signals in lived experience — patterns, frustrations, workarounds, obsessions |
| `customer-validation` | Validate directly with potential buyers through observation or conversation |
| `timing` | Evaluate whether timing is right and what specific change would make it right |
| `historical` | Reason from past companies with similar theses — what happened and why |
| `substitute` | Map what people use instead of the non-existent solution, and why |
| `first-principles` | Reason from fundamentals; score or rate systematically rather than intuitively |
| `root-cause` | Drill to the underlying cause of a problem (Five Whys family) |
| `wedge-narrowing` | Find the minimum viable entry point that makes the larger market accessible |
| `founder-process` | How the founder works rather than what they are examining — cadence, record-keeping, and checks on their own reasoning |

---

## Applicable-At Phases

```
ideation            — generating or reframing the idea
assumption_extraction — pulling explicit assumptions out of a thesis or idea
validation          — testing a specific assumption against evidence
thesis_mutation     — updating the thesis after evidence changes your view
```

`assumption_extraction` is the phase between having an idea and having a testable assumption graph. Methods tagged here help structure vague theses into concrete, testable nodes.

---

## Assumption Categories

These match the assumption graph node categories exactly:

```
market              — who the market is and how large
pain                — whether the problem is real and expensive
buyer               — who actually pays and why
timing              — why now vs. 2 years ago or 2 years from now
technical           — whether the technical approach is feasible
trust               — whether buyers will trust the product/team
distribution        — how you reach the customer
competition         — what alternatives exist and how they fail
founder-market-fit  — whether this team has a credible path to this market
```

---

## Folder Assignment Guide

- `/ideation/` — methods for generating new ideas or reframing existing ones
- `/validation/` — methods for testing a specific assumption against evidence
- `/mutation/` — methods for updating the thesis after evidence comes in
- `/intake/` — elicitation methods run once at onboarding, input is the founder's memory
- `/practices/` — methods the founder executes in the world, not at a desk
- `/unused/` — parked cards, out of rotation and never selectable

A method goes in the folder for its primary use. The `applicable_at` field captures any secondary phases.

### When a method belongs in `/practices/`

The folder cut is on two different axes, deliberately:

- `ideation/`, `validation/`, `mutation/` split by **when in the loop** a method runs. Everything in them is desk work — reading, reasoning, and research over sources that already exist. An agent can execute them.
- `intake/`, `practices/`, `unused/` split by **where the method's input comes from**, which is what determines whether an agent can run it at all.

One test decides it: **could a research subagent, given web access and every file in this repo, produce this method's output?**

If yes → a phase folder. If no, ask what the missing input is:

| Missing input | Folder | Runner |
|---|---|---|
| the founder's memory, which only surfaces when someone asks | `intake/` | the onboarding agent, once per belief |
| something that doesn't exist until the founder creates it — traffic, a signature, a conversation, a log built over weeks | `practices/` | the founder |
| nothing; the card is simply out of rotation | `unused/` | nobody |

The practical consequence: **nothing in `/intake/`, `/practices/`, or `/unused/` is ever dispatched as a shotgun lens**, and none of those cards appear in `methods/shotgun-routing.yaml` except under `excluded_folders`. This is the reason the folders exist. A subagent handed one of these cannot say "I cannot run this"; it writes a fluent, well-structured, entirely invented result — conversion rates from a landing page never built, an LOI from a company never contacted, a founder history nobody was asked about — and that output reaches synthesis indistinguishable from evidence. Separating them by folder makes the mistake structurally hard instead of relying on a prompt to prevent it.

Intake and phase folders form a pipeline rather than a choice: intake methods
run once, write `input-context/{slug}/belief.md`, and initialize
`reports/{slug}/01-ideation/hunch-lineage.md` with founder-confirmed H1. The
shotgun reads both and gives the same belief/hunch pair to every selected
method. Re-deriving founder fit or the founder's path from solution to problem
per run is both redundant and a case where a research lens confabulates. This
is why founder-fit elicitation and SISP Detection live in `methods/intake/`
rather than the shotgun routing map.

Beware the near-misses:

- **Observes over time but computes in one sitting** (a coefficient over outreach data another process already collected) → validation. The data-gathering isn't part of the method.
- **Temporal flavour, point-in-time application** (a self-check you apply to the idea in front of you) → its phase folder.
- **Designs a field experiment without running it** (writing kill criteria before a test) → validation. Producing the plan is desk work; only executing it is a practice.

Note that `applicable_at` still describes *when in the loop* a practice is used — Mom Test Interview Script is `[validation]` and lives in `practices/`. The two axes are independent, and neither substitutes for the other.

### Retiring a card

Two ways out, and the difference matters:

- **Park it** — move to `/unused/`. The card was real but is out of rotation. Recoverable.
- **Delete it** — the card was wrong or redundant. Add a row to the "Deleted outright" table in `methods/index.md` so the absence stays traceable; otherwise a future session finds a dangling reference with no way to tell whether it was intentional.

**Either way, grep `methods/shotgun-routing.yaml` before you finish.** If the card was a family `primary` or `alternative`, the reference goes dangling, and this failure is silent by construction: the shotgun selects from the families it can resolve, produces a full-looking report, and the missing lens is never missed. A required family can lose its coverage entirely without a single error surfacing. Promote an alternative to primary, or add a replacement, in the same edit that removes the card.

A method extracted from an article goes here. A skill for *running* that method goes in `.claude/skills/` (later).

## Shotgun routing

`applicable_at` describes where a method can be useful; it is not an instruction
to run the method in every shotgun. `methods/shotgun-routing.yaml` is the
ideation-shotgun allowlist and dependency map. It selects a representative
portfolio across lens families and excludes downstream validation gates.
