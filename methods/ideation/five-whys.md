---
name: Five Whys
category: root-cause
applicable_at: [assumption_extraction, ideation]
assumption_categories_it_helps: [pain, market, technical, buyer]
shotgun_family: root_cause
shotgun_role: primary
requires: [belief, current_hunch, pain_clusters]
source:
  title: "Come Up with a Startup Idea"
  author: Rebekah Emanuel
  url: https://innovationlabs.harvard.edu/come-up-with-a-startup-idea/
  publisher: Harvard Innovation Labs
---

## Core Insight

Surface observations may be symptoms of a deeper causal mechanism. Five Whys follows the causal chain without steering it: preserve the observation, ask only **WHY?**, record the answer, then ask only **WHY?** again. Expanding or paraphrasing the question introduces assumptions about the cause and biases the next answer.

The answers may expose a deeper cause, but the method does not guarantee one. Each answer is evidence or a hypothesis to validate—not a fact merely because it appears later in the chain.

## Process

1. Copy the starting observation verbatim. Do not improve, narrow, or reinterpret it.
2. Ask exactly: **WHY?**
3. Record the answer from the available context or evidence.
4. Treat that answer as the current statement and ask exactly: **WHY?** again. Do not turn it into a longer or more specific question.
5. Continue until five **WHY?** prompts have been answered.
6. Label each answer as `[evidence]` when directly supported or `[hypothesis]` when inferred. Include the supporting source beside evidence-backed answers.
7. If there is not enough basis for the next answer, write `[unknown — evidence needed]` and stop. Never invent an answer merely to reach five.
8. Interpret the chain only after it is complete. Keep conclusions, opportunities, and proposed solutions outside the chain.

The questioning operator is always the single word **WHY?** Do not generate questions such as “Why does this require manual work?”, “Why have incumbents not solved it?”, or “Why now?”. Those phrasings add a causal frame that the preceding answer did not necessarily establish. “Why now?” and “Why has nobody solved this?” belong to separate ideation methods.

## Output Format

```text
Observation: [verbatim starting observation]

WHY?
Answer 1: [evidence | hypothesis] ...

WHY?
Answer 2: [evidence | hypothesis] ...

WHY?
Answer 3: [evidence | hypothesis] ...

WHY?
Answer 4: [evidence | hypothesis] ...

WHY?
Answer 5: [evidence | hypothesis] ...

Interpretation:
- Deepest supported causal hypothesis:
- Unsupported links requiring validation:
- Assumption worth testing:
```

## Example

```text
Observation: Many companies are hiring robotics integrators.

WHY?
Answer 1: [hypothesis] There is a large need for those people in the industry.

WHY?
Answer 2: [hypothesis] The robotic-integration process requires extensive manual handling.

WHY?
Answer 3: [hypothesis] Each deployment has to be adapted to its particular environment.

WHY?
Answer 4: [hypothesis] The relevant equipment, interfaces, layouts, and operating constraints vary between environments.

WHY?
Answer 5: [unknown — evidence needed]

Interpretation:
- Deepest supported causal hypothesis: None yet; the current answers are hypotheses.
- Unsupported links requiring validation: Answers 1–4.
- Assumption worth testing: Integration demand is driven by repeated manual adaptation between deployment environments.
```

The example demonstrates the format, not verified facts about robotics integration. Research or interviews must supply the answers and may produce a completely different chain.

## Limitations

- Five answers don't guarantee you've hit the root — some causal chains are longer, some shorter
- Neutral questioning does not make the answers neutral; answers still reflect the evidence and reasoning available
- Can produce circular or tautological answers ("there is hiring because people are needed"); label these and seek evidence rather than repairing them with a leading question
- Requires domain knowledge or external evidence to know whether an answer is correct
- Works better for operational/physical problems than for behavioral or social ones where causality is diffuse
- A causal chain may branch. Preserve competing evidence-supported chains separately; do not merge them by rewriting the next question
- Later answers are not automatically more fundamental or more true than earlier answers

## Connection to the Loop

During a shotgun, copy the current hunch's problem observation verbatim and
examine that same claim. Do not select a different cluster. Feed the chain with
public evidence, interviews, or other research where available. Return
unsupported links as assumptions; do not treat the deepest answer as a new
hunch until synthesis and founder confirmation.
