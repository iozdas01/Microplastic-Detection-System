---
name: JTBD and Current Substitute Map
category: jtbd
applicable_at: [ideation, assumption_extraction]
assumption_categories_it_helps: [pain, buyer, market, competition, distribution]
shotgun_role: primary
shotgun_family: job_and_substitute
requires: [belief, current_hunch, pain_clusters]
source:
  title: "Jobs-to-be-Done statement lens with substitute mapping"
  author: "Sunita Mohanty / Reid Marcos"
  note: "Consolidates Jobs-to-be-Done Statement and Substitute Mapping."
---

## Core Insight

A job and its current substitute are two halves of one observation. The job
describes the progress a person is trying to make in a specific circumstance;
the substitute shows what they already hire—software, a service, a spreadsheet,
manual labor, delay, or non-consumption—to make that progress today. Separating
them creates duplicate analysis and hides the most useful comparison: what the
current approach accomplishes, where it fails, and what makes switching hard.

## Process

1. Start from one evidence-backed pain cluster and its verbatim records.
2. Write the job without naming a proposed solution:

   > **When I** [context]  
   > **But** [barrier]  
   > **Help me** [progress sought]  
   > **So I** [desired outcome]

3. Cite the records supporting each line. If the outcome is inferred rather
   than stated, label it `[hypothesis]`.
4. Map what is currently hired for the job:
   - direct products or vendors;
   - adjacent tools used outside their intended purpose;
   - spreadsheets, email, and manual coordination;
   - contractors or internal headcount;
   - postponement, acceptance of loss, or non-consumption.
5. For each substitute, record evidence of effort, failure, embedded data,
   training, organizational memory, trust, and other switching costs.
6. Identify the sharpest unresolved step in the substitute workflow. This is a
   candidate wedge, not a product recommendation.
7. Produce multiple job/substitute maps when different segments hire different
   approaches. Do not average them into one generic user.

## Output

```text
Segment:
Job statement:
Supporting verbatims:
Current substitutes:
What each substitute does well:
Where each fails:
Behavioral effort already spent:
Switching costs:
Unresolved workflow step:
Unknowns requiring interviews:
```

## Example

A team may hire nested Google Docs, Trello, and Confluence to keep project
knowledge coordinated. The job is not "use a better wiki"; it is to preserve
shared context while work changes. The substitute map reveals that the largest
barrier is organizational memory embedded in existing tools, making import and
migration part of the real job.

## Limitations

- Community posts can support a provisional job statement, but interviews are
  stronger evidence of circumstance and desired progress.
- A named substitute does not prove dissatisfaction; people may prefer it.
- Switching-cost analysis is easy to understate without direct workflow access.
- This method does not rank jobs, establish market size, or validate willingness
  to pay.

## Connection to the Loop

Run after public-signal clusters exist. During a shotgun, examine the active
hunch's segment, problem, and workaround rather than selecting a different job.
The output shows whether that hunch expresses a solution-independent need and
where its substitute account is incomplete.
