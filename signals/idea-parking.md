# Idea Parking

Standing, cross-idea, append-only. The destination `signals/gaps-log.md` points at when an
observation has already hardened into a **conclusion** — "there's a business in X".

`gaps-log.md` holds observations and explicitly forbids conclusions. This file holds the
conclusions: half-formed ideas the founder wants recorded so a future pivot has somewhere to
pivot *to*. Neither file evaluates. Recording an idea here is not a claim that it is good.

## What goes in

Ideas, as the founder had them, in their own words. One entry each. **No evaluation, no
research, no scoring** — capture is the whole job. A commentary line may be attached, but it
is marked as commentary and never rewrites the founder's version.

## What must never go in

Same boundary as `gaps-log.md`, for the same reason — this file is cross-idea, so it is a
back door for context bleed:

- **No findings about any active idea.** No assumption IDs, no confidence scores, no evidence
  grades. Those live in `reports/{slug}/`.
- **No research.** If an idea gets researched, it has graduated — it goes through
  `/startup-belief-intake` and becomes `reports/{slug}/`, and this entry gets
  `status: promoted → reports/{slug}/`.
- **Nothing from a private conversation** that isn't already anonymized to a role and a
  company category.

## Entry format

```markdown
- YYYY-MM-DD — <the idea, in the founder's words>
  source: <where it came from — a post, a conversation, mid-work>
  trigger: <the specific thing that prompted it, with a URL if there is one>
  status: parked | promoted → reports/{slug}/ | dismissed (<one-line reason>)
  note: <optional, one line, marked as commentary — never replaces the founder's version>
```

`status` starts `parked`. Entries are never deleted — a dismissed idea that recurs in two
years is itself a signal.

## Review

Reviewed at the same cadence as `gaps-log.md`, and ideally in the same pass, since a parked
idea that a cluster of gap observations independently points at is much stronger than either
alone. Do not review more often than the file grows.

---

## Entries

- 2026-08-09 — An AI-native manufacturing machine: pick whichever machine on the floor needs
  reprogramming first, and build the machine around being trainable rather than programmed.
  Dymtri can train it.
  source: founder, mid-conversation
  trigger: TRUMPF/ASML EUV post — https://x.com/IlirAliu_/status/2086360929302679702
  status: parked
  note: (commentary) The selection rule — "whichever needs reprogramming first" — is an
        economic filter, not a technical one: it selects machines whose setup cost per job
        exceeds their run time. Untested.

- 2026-09-03 — "The OpenRouter for machines." Anthropic just published a standard driver spec
  so agents can read from and write to physical equipment; if that spec spreads, the layer
  above it — one endpoint that routes a job to whichever machine, anywhere, can actually run
  it — is the thing worth owning.
  source: founder, mid-conversation, reacting to the MHS announcement
  trigger: Model Hardware Standard research preview, announced 2026-08-27 —
           https://www.anthropic.com/news/model-hardware-standard-research-preview
  status: parked
  note: (commentary) OpenRouter's business exists because model APIs converged on one request
        shape; the analogue here needs MHS adoption wide enough that machines are substitutable
        at the interface, which the preview does not yet establish. Untested.

- 2026-09-03 — do the whole thing with a world model instead: reconstruct the opening as a
  scene rather than a number, and let the model reason about whether the product will actually
  fit, rather than encoding deductions by hand.
  source: founder, mid-conversation, after the MHS strategic read
  trigger: the finding that half of wrong-size orders trace to a trained technician holding a
           tape — i.e. the error is judgement, not metrology
  status: parked (founder: "right now that cannot be the wedge")
  note: (commentary) Cuts against two positions taken the same day — a vision-driven model
        routes around machines with no programmable interface, so "the installed base is not
        MHS-ready" is a barrier with a clock on it; and "knowing what to send the machines" is
        the training target rather than a durable edge. Current world models are weak on precise
        metric geometry, which is the part that has to be right, so the plausible shape is
        hybrid — metrology for the number, model for the judgement. Untested, no evidence.

- 2026-09-03 — vibe coded furniture D2C
  source: founder, mid-conversation, unprompted
  trigger: (none given)
  status: parked
  note: (commentary) Worth checking against the active idea's own belief file before treating
        this as new — that belief records "vibe manufacturing" as its starting solution, in the
        founder's words, meaning a D2C site where a customer specifies what they need and a
        factory the company owns makes it. If those are the same idea this is a restatement
        rather than a candidate, and the parking file should not hold a second copy of a live
        one. If the difference is that the customer DESCRIBES the piece in natural language
        rather than configuring it from options, that is a real distinction and worth its own
        entry — the founder is the one who can say which.

---

## Review history

_(no review passes yet)_
