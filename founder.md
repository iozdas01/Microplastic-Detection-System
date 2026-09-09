---
team: two
founders:
  - name: Sandra Zalas
    profile: founders/sandra-zalas.md
    status: confirmed
    role: CEO
  - name: Izgin Ozdas
    profile: founders/izgin-ozdas.md
    status: confirmed
    role: ""            # not yet recorded — Izgin sets this
---

# Founders

This project has **two founders** (from 2026-09-09). Sandra Zalas is CEO of Baltic
Jungle Lab, the company this repo tests; her profile was drafted from her public LinkedIn
and awaits her confirmation. Izgin's role and title in the company are not recorded yet.
Every skill or script that reads `founder.md` must load every profile listed above:

| Founder | Role | Status | Profile |
|---|---|---|---|
| Sandra Zalas | CEO | confirmed (profile unverified by her) | [founders/sandra-zalas.md](founders/sandra-zalas.md) |
| Izgin Ozdas | — | confirmed | [founders/izgin-ozdas.md](founders/izgin-ozdas.md) |

Each profile is the durable, cross-idea record of that founder's experience,
access, and founder-market-fit inputs. Use the records as context, not proof:
firsthand experience justifies where to look and whom a founder can reach; it
does not validate a market, pain, buyer, or willingness-to-pay assumption.

**Adding a founder:** write `founders/{name-slug}.md` in the same schema as the
existing profile, add them to the frontmatter list and the table above, and set
`team:` accordingly. The consumer rules below are already written for multiple
founders and need no change — they degrade correctly to one.

## Rules for consumers

- **Affiliation scoring (outreach):** a contact earns `affiliation_boost` if
  they match ANY founder's `affiliations` / `affiliation_scoring` entries.
  When several founders match, use the single strongest boost — do not stack.
- **Outreach copy:** write from whichever founder has the genuine affinity
  with the contact (shared employer, school, language, nationality). Never
  reference one founder's affiliation in a message sent as another.
- **Founder-market fit (intake, ideation, assumption extraction):** evaluate
  against the union of all founders' `capability_domains`,
  `firsthand_problem_environments`, and `likely_unfair_access`. A gap covered
  by any founder is covered; a claim none can support is unsupported.
- **Warm intros:** `warm_intro_paths` are per-founder; only the owning founder
  may reference their mutuals.
- **Outreach identity:** each profile carries `outreach_identity` — LinkedIn
  account name, the credibility hook used in copy, and a booking link. Skills read
  it from there; a skill that hardcodes a founder's account, hook or link breaks
  as soon as a second founder exists.
- **LinkedIn outreach:** every `contacts.md` row records `linkedin_account`
  (schemas/contact.md) — whose network the contact lives on. `degree`,
  `mutuals_count`, and `outreach_status` are meaningless without it. Do not
  assume a single default account even while the team is one person; a skill
  that hardcodes one founder's account breaks on the next one.
