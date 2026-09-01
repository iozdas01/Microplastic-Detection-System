---
name: Cross-Domain Persona
category: analogical
excluded_because: "Pure generation with no evidence source — *'pick 5 archetypes… don't filter, just generate.'* The one thing an LLM does most fluently and least informatively; output is unfalsifiable but formatted like a finding. Still useful to a human at a whiteboard."
applicable_at: [ideation, thesis_mutation]
assumption_categories_it_helps: [pain, distribution, technical, market]
source:
  title: "Come Up with a Startup Idea"
  author: Rebekah Emanuel
  url: https://innovationlabs.harvard.edu/come-up-with-a-startup-idea/
  publisher: Harvard Innovation Labs
---

## Core Insight

Domain expertise creates mental constraints. An insider pattern-matches to known solutions in their field. An outsider with a completely different background reaches for their own toolkit — and that toolkit often contains exactly the tool the domain never thought to import.

The method works because different fields have already solved analogous problems using completely different mechanisms. A gamer's intuition about engagement loops, a nurse's intuition about triage and escalation, a plumber's intuition about flow and pressure — these are frameworks developed over years that the domain hasn't borrowed yet.

Applied to the assumption loop: when you're stuck on how to test an assumption or reframe a thesis, forcing yourself to think from a radically different domain can surface an approach that domain insiders would never reach for.

## Process

1. State the problem clearly in one sentence
2. Pick 5 very different archetypes — maximize distance from the domain
   (child, street performer, plumber, game designer, trauma nurse, military logistics officer, etc.)
3. For each archetype, ask:
   - What tools are natural to them?
   - How would they frame this problem in their own language?
   - What would they try first?
4. Write 1–2 sentences per archetype — don't filter, just generate
5. Look across the 5 answers for the one that changes your thinking

## Example

**Problem:** Bad air quality in a city

- Meteorologist: "I'd track how it moves with wind and time of day to find the source" → dispersion-based source mapping
- Plumber: "You find the source by tracing back from where it collects" → emissions source mapping
- Game designer: "Make people compete to report pollution events" → crowdsourced monitoring app
- Nurse: "Triage: find who's most affected and protect them first" → exposure mapping for vulnerable populations

## Limitations

- Generates a high volume of low-signal ideas — needs strong filtering judgment
- Works better for reframing and direction-finding than for specific technical solutions
- The best outputs are usually structural insights ("approach it like a flow problem"), not literal solutions ("build a specific gadget")
- Less useful when the domain constraint is genuinely technical (physics doesn't change because a plumber wouldn't know about it)
- Requires you to actually know enough about the domain to evaluate which borrowed ideas have merit

## Connection to the Loop

Use at:
- **Ideation:** when generating ideas in a space, cross-domain personas break industry-local thinking
- **Thesis mutation:** when evidence has narrowed your solution space, a different domain frame may reopen it
