---
name: The Well Test
category: customer-validation
excluded_because: "tests demand *shape* for a named idea after its core problem has been interpreted"
applicable_at: [validation, assumption_extraction]
assumption_categories_it_helps: [pain, buyer, market]
source:
  title: "How to Get Startup Ideas"
  author: Paul Graham
  url: http://paulgraham.com/startupideas.html
  note: accessed via personal notes summary
---

## Core Insight

Demand for a startup idea has a shape. "Broad and shallow" looks appealing — millions of people might use this — but it's the shape of bad ideas. "Narrow and deep" looks small but is the shape of good ones: a specific group of people who want this right now so urgently that they'll use a crappy v1 from a two-person startup they've never heard of.

The mechanism behind this: if something that large numbers of people urgently needed could be built with startup-level effort, it would probably already exist. So genuine startup opportunities almost always start small and urgent — not large and mild. The initial group is small for a reason, and that reason is the key to everything.

Applied to assumption testing: the pain assumption isn't "do people have this problem?" It's "is there a specific group who has this problem so badly that our bar for the product can be very low?" If you can't name that group and describe their urgency, the pain assumption is probably broad-and-shallow.

## Process

1. Name the most specific possible user who has this problem — not "enterprises" or "people who X" but a concrete archetype with a concrete situation
2. Ask: would they use a v1 that barely works, built by people they've never heard of?
3. If yes: what makes it urgent enough? What happens to them if they don't solve this?
4. If no: is this actually broad-and-shallow demand? What would make it urgent?
5. Test the size claim: is this group really small? If the answer is "millions of people need this," that's usually the broad-and-shallow shape in disguise

## Example

Dropbox: Drew Houston kept forgetting his USB stick. The specific user was a programmer who worked across multiple machines and kept losing access to files mid-work. That user would use a barely-functional file sync tool immediately. The initial group was small (developers) but the urgency was real — and it turned out the group was much larger once the product worked.

Airbnb: initially just people who needed a cheap place to stay during sold-out conferences. Tiny group, urgent need, terrible product experience (air mattresses on strangers' floors). The well was narrow and deep. The market turned out to be enormous, but that wasn't knowable at the start.

## Limitations

- Narrow-and-deep initial demand doesn't guarantee the market expands — you still need to validate whether there's a path out
- Can be misapplied: "there are 10 people who desperately need this" can be true but the group is too small to build a company on
- Urgency can be manufactured through framing — push hard to find cases where users would actually use a barely-working product, not where they say they would

## Connection to the Loop

This is the primary test for the **pain assumption** and the **buyer assumption**. Before asking any other question about an idea, ask: can I describe a specific group who wants this urgently enough to use a v1? If you can't, the pain assumption is untested. Use this to anchor assumption extraction — the specific group and their urgency is assumption A2.
