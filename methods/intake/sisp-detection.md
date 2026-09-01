---
name: SISP Detection
category: inversion
excluded_because: "solution-bias context and an independent research test for the shotgun"
applicable_at: [validation, assumption_extraction, ideation]
assumption_categories_it_helps: [pain, buyer, market]
source:
  title: "How to Get Startup Ideas (Startup School 2020)"
  author: "Jared Friedman (YC)"
  url: ""
  date: "2020"
---

## Core Insight

A SISP — **Solution In Search of a Problem** — begins with a favored solution, technology, or analogy ("Uber for plumbers") and reasons backward to a problem that would justify it. The important input is the founder's path to the idea: what they noticed first, what solution they already favor, and whether they can describe an independently observed problem without that solution.

That path lives in the founder's memory and only surfaces through conversation, so this is an onboarding method. It does not reject solution-first ideas. It records the possible bias before research begins so the shotgun can search for the problem independently rather than quietly treating the proposed solution as evidence.

## Process

Ask one question at a time and preserve the founder's answers in their words:

1. Capture the founder's starting idea verbatim, including any product, technology, feature set, or analogy.
2. Ask: **"What came first for you: something you observed people struggling with, or this solution/technology/analogy?"**
3. Ask: **"Can you describe the problem without mentioning the solution, product, technology, or analogy?"**
4. Ask for the specific past observation behind that problem: who experienced it, what happened, and what they did instead. Do not convert a hypothetical story into an observation.
5. Classify the starting point:
   - `problem_observed` — a specific problem or behavior came first;
   - `solution_or_analogy_first` — the solution, technology, or analogy came first;
   - `mixed` — both evolved together;
   - `unclear` — the founder cannot yet tell.
6. Record the SISP status:
   - `not_indicated` — an independently stated problem and a specific observation exist;
   - `possible` — the solution came first, but an independent problem can be stated;
   - `probable` — the founder cannot state a problem except as the absence of the proposed solution;
   - `unresolved` — there is not enough information.
7. Write the solution-free problem, founder-reported observations, and the exact uncertainty the shotgun must test into `input-context/{slug}/belief.md`. Founder-reported observations are context, not independent external evidence.

Do not resolve the SISP status with desk reasoning during intake. The shotgun tests whether the problem appears in public behavior and community language without depending on the proposed solution's vocabulary.

## Example

Founder: "I want to build Uber for plumbers."

- Starting solution or analogy: "Uber for plumbers"
- Origin: `solution_or_analogy_first`
- Solution-free problem: `[founder cannot yet state one]`
- SISP status: `probable`
- Shotgun test required: Search plumber and customer workflows without using "Uber for plumbers" or marketplace language. Determine whether a recurring coordination, discovery, scheduling, trust, or payment problem appears independently. These are search directions, not assumed problems.

## Limitations

- Not every solution-first idea is doomed; a new capability can reveal a latent problem. `possible` means "test independently," not "kill."
- A fluent solution-free problem statement is still only the founder's claim. It is not evidence that other people experience the problem.
- The classification depends on honest recall and may remain `unresolved`.
- SISP Detection does not establish market size, urgency, willingness to pay, or solution fit.

## Connection to the Loop

Run this during **belief intake**, especially when the founder arrives with a product, technology, feature set, or "X for Y" analogy. Its output is context for the ideation shotgun. The shotgun searches for the problem independently and may return a hunch that uses the starting solution, changes it, or ignores it entirely.
