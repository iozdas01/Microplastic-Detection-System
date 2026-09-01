---
name: Paper-Mining Emails
category: customer-validation
applicable_at: [validation]
assumption_categories_it_helps: [pain, willingness_to_pay]
---

## Core Insight

Corporate research labs print institutional emails on their papers. Email mined this
way is the one outreach channel with no rate limit, and "I read your paper" plus a
credible academic address is the highest-converting cold opener available to a
technical founder. `scripts/data/openalex.py` automates the target-first version.

## Method

why: >
  Corporate research labs print institutional emails on their papers. This is the only outreach
  channel with no rate limit, and a cantab.ac.uk address plus "I read your paper" is the
  highest-converting cold email available to this founder.
method: >
  1. Search for the topic plus a company name, e.g. "arxiv robot data quality Siemens".
  2. Take the arXiv ID from the result.
  3. Fetch arxiv.org/html/{id} — NOT /abs/{id}. This is the whole trick. The abstract page strips
     affiliations and emails; the HTML render carries the author footnote where the addresses
     live. Verified 2026-08-06 on 2605.26349 and 2604.22235, both worked.
  4. Read the footnote. Corporate papers usually compress a shared domain, e.g.
     "firstname.lastname, firstname.lastname@company.com" — expand each name against the domain.
  5. Screen env_control BEFORE writing. A vendor deploying in its own factory is a control case,
     not a pain case.
beats_linkedin_because: >
  No weekly cap, no connection request, no acceptance wait, and the grounded clause writes itself
  because you are referencing their own published work.
