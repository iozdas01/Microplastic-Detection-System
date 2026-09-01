---
name: startup-extract-method
description: >-
  Extracts reusable startup method cards from an article, essay, talk transcript, or pasted founder advice. Use when the user asks to extract methods, add material to the methods library, identify frameworks in a source, or pastes substantial startup-advice content with an extraction intent. Checks for duplicates, writes each distinct method to the appropriate ideation, validation, or mutation folder, and updates methods/index.md. Do not use when the user only wants to read or discuss the source.
---

# startup-extract-method

Extract structured method cards from a pasted article or transcript and add them to the methods library at `methods/`.

## What you're doing

The methods library is a structured collection of reusable startup techniques — for generating ideas, testing assumptions, and mutating a thesis after evidence comes in. Each card captures not just steps but the *mechanism*: why the method works, and exactly when in the assumption-testing loop to use it.

Your job: read the article carefully, identify what's genuinely new, and write clean cards for each new method — in a format consistent with the rest of the library.

---

## Step 1: Read the existing library

Before extracting anything, read `methods/index.md` in full. This is non-negotiable — many articles draw from overlapping sources (PG essays, YC canon, etc.), and a method that looks new might already be captured under a different name.

---

## Step 2: Identify candidate methods

Read the article and find **discrete, executable methods** — not observations or general advice, but techniques a founder could actually follow.

A method has all of:
- A clear trigger (when to use it)
- A process or steps
- A mechanism (why it works)
- At least one example

**Filter out** things that are not methods:
- General principles ("think carefully") — advice, not a method
- Mindset points ("be ambitious") — not a method
- Observations about successful companies — unless the reasoning is extractable as a repeatable process

Name each candidate method concisely (3–6 words). Group overlapping concepts if they're really the same technique described twice.

---

## Step 3: Duplicate check

For each candidate, compare against `methods/index.md`. Ask:
- Is this already in the library under a different name?
- Is this a minor variant of an existing method, or genuinely distinct?

If it's a variant: skip creating a new card. If the variant adds something meaningful, note it briefly at the bottom of the existing card.

If it's genuinely new: proceed.

Tell the user: "Found X candidate methods. Y already exist in the library. Creating Z new cards."

---

## Step 4: Route each method to the right folder

Assign each method to its *primary* phase:

- **ideation/** — for generating new ideas or reframing existing ones
- **validation/** — for testing a specific assumption
- **mutation/** — for updating the thesis after evidence changes your view

A method that spans phases goes to its most natural home; the `applicable_at` field captures the full list.

---

## Step 5: Write the method cards

Use this exact structure — match the style of existing cards:

```
---
name: [Method Name — 3–6 words, title case]
category: [exactly one — vocab:method_category in schemas/vocabularies.yaml; meanings in schemas/method.md]
applicable_at: [[ideation], [validation], [thesis_mutation] — all that apply]
assumption_categories_it_helps: [subset of vocab:assumption_category]
source:
  title: "[Article or talk title]"
  author: "[Author name]"
  url: ""
  date: ""
---

## Core Insight

[1–3 paragraphs. The mechanism — WHY this method works, not just what it does. The reader should understand the underlying theory well enough to apply it to a case not mentioned in the article.]

## Process

[Numbered steps. Concrete enough to follow without re-reading the source. Usually 3–6 steps.]

1. ...
2. ...

## Example

[A concrete example, ideally from the article. Name specific companies, decisions, and outcomes. Avoid hypotheticals — they don't build conviction.]

## Limitations

[When NOT to use this. Where it breaks down. What it doesn't validate. What you still need to do after using it.]

## Connection to the Loop

[One short paragraph: exactly when in the assumption-testing loop to reach for this method, and what question it answers. Be specific — "use at ideation when X" beats "useful for founders".]
```

Write each card as if explaining to a smart founder who hasn't read the article. The card should be fully self-contained.

---

## Step 6: Save the files

Save each card to:
- `methods/ideation/[kebab-case-name].md`
- `methods/validation/[kebab-case-name].md`
- `methods/mutation/[kebab-case-name].md`

---

## Step 7: Update methods/index.md

Add a row for each new method in the correct section:

```
| Method Name | category | other phases (or —) | [filename.md](path/filename.md) |
```

---

## Quality bar

A good card:
- Explains the mechanism (not just restates the steps)
- Cites a real, named example with outcome
- Clearly states when NOT to use it
- Is specific about which assumption categories it helps

A bad card:
- Copies the article's sentences without synthesis
- Has vague steps like "think about the problem"
- Misses the Connection to the Loop section
- Creates a card for general advice instead of a method
