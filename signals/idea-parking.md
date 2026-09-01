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

---

## Review history

_(no review passes yet)_
