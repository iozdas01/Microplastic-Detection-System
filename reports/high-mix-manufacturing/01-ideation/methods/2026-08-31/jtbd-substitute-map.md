---
method: jtbd-substitute-map
run_id: "2026-08-31"
mode: explore
card: methods/ideation/jtbd-substitute-map.md
queries_derived_from: card evidence needs (job statement + substitute set + switching costs)
counter_query_run: yes - "who says their current tool is fine"
verbatim_source: corpus-pool.json -> verbatims (direct page fetch, not snippets)
---

# JTBD and current substitute map

Two maps, not averaged. Different segments hire different things, and the card forbids
collapsing them into one generic user.

---

## MAP A — Custom / commercial millwork (one-off work)

**Segment:** commercial millwork and custom cabinet shops where the majority of work is
one-off, room-specific product. Affected role: the owner or CNC programmer who converts a
job into machine-ready parts.

**Job statement**

> **When I** take on a custom job that is not a standard box — 25 rooms, 20 materials, parts
> that do not sit on a grid —
> **But** my cabinet software handles boxes well and fights me on anything custom, so I place
> parts by typing x, y, z coordinates and allocate materials room by room on paper,
> **Help me** get from the job as designed to machine-ready parts without doing the
> engineering by hand,
> **So I** can take custom work without it eating the margin that made it worth taking. `[hypothesis]`

**Supporting verbatims** (all from cncpgmr, 30-year commercial millwork veteran,
[WOODWEB CNC 843629](https://www.woodweb.com/forum_fdse_files/cnc/843629.html)):

- *"Mozaik is great for boxes, when you get into custom building, it is garbage...80% of my
  company's business is custom, 1 off product. It is horrendous to custom build with."*
- *"Think about the time it takes to move every part by numerical coordinates. x,y,and z.
  instead of the ability to drag to position from any view."*
- *"I have a job with 25 rooms, and 20 different materials...I have to figure out what I need
  for that room, write them down, and make sure I only use materials needed for that room."*

The `So I` line is marked `[hypothesis]` — he describes the effort, never the consequence.
Nobody in the corpus said custom work loses money.

**Current substitutes**

| Hired | Does well | Fails at | Switching cost |
|---|---|---|---|
| Mozaik ($125/mo) | boxes, standard construction, CNC output for 1-20 person shops | custom one-off — "garbage", "horrendous" | low price, high embedded method: *"it will adapt to the way YOU build cabinets"* |
| Cabinet Vision (Hexagon) | depth, complex joinery, commercial | usability; 1-25 employee shops give one-star reviews, some never got it working | very high — seats bought, training sunk |
| Manual coordinate entry | total control | it is the failure being described | zero to leave, but it is inside the tool |
| Paper material allocation | works | does not scale past a few rooms | zero |

**Behavioural effort already spent:** he owns the software, learned it, runs 80% custom
through it anyway, and has done so for 30 years. That is a *lot* of effort spent working
around the gap — the strongest kind of signal this card looks for.

**Unresolved workflow step (candidate wedge):** placing and allocating parts for a
*non-standard* job. Standard boxes are solved and cheap. **The gap is precisely at custom.**

**Unknowns requiring interviews:** whether this costs money or only annoyance; whether
cncpgmr is representative or an outlier with an unusual workflow; what he would pay.

---

## MAP B — Estimating / quoting (cabinet shops)

**Segment:** owner-estimators at small cabinet shops. Affected role: whoever prices the job.

**Job statement**

> **When I** get a request to price a kitchen,
> **But** the requests arrive faster than I can work through drawings, and most of them do not
> convert,
> **Help me** return a number the client will accept without spending my week on it,
> **So I** stop losing evenings to bids that go nowhere. `[hypothesis]`

**Supporting verbatims** ([WOODWEB Business 843811, "Too much time estimating"](https://woodweb.com/cgi-bin/forums/business.pl?read=843811)):

- Chris (OP): *"The requests are getting out of hand and I am overwhelmed."*
- Chris: *"All this takes time and it's exhausting."*
- Chris: *"72 bids"* of which *"42 were accepted"* — **30 bids a year produced nothing.**
- Rich C.: *"I was constantly bombarded with a 'just give me a ball park number'."*
- David B: *"I always tended to 'estimate' too low."*

**The contradiction this card must not average away.** Time per kitchen, from the same thread:

| Who | Time to quote a kitchen |
|---|---|
| Joe | *"5-15 minutes for a normal kitchen. 30 minutes off plans."* |
| Eddie | *"about an hour to go thru the drawings and plug on my Excel"* |
| (reported elsewhere in thread) | 6-7 hours pencil and paper |

**A 25-to-80-fold spread.** The pain is real for some and trivial for others, and the prior
belief's 13.5-hour design-labour figure is not supported by anyone here. Whether the spread
tracks shop size, job complexity or method is unknown and is the single most useful thing an
interview could settle.

**Current substitutes:** Excel + PDF + email (Eddie); price-per-inch and per-foot scales;
reference models showing price ranges (Derrek); ballpark numbers given verbally; and
*estimating too low* — a substitute that transfers the cost to margin instead of time.

**Unresolved workflow step:** not the arithmetic. It is **triage** — 30 of 72 bids were
wasted, and nothing in the substitute set helps decide which requests deserve the hour.

---

## COUNTER-QUERY (mandatory) — who says their current tool is fine

Run, and it returned real counter-evidence:

- dconti, Mozaik user of 2.5 years: *"It is a cabinet to cnc program it does that very well.
  It covers all different types of construction methods and it will adapt to the way YOU build
  cabinets."*
- Ryan: *"We own 2 seats of cabinet vision... I can't remember the last time it was even
  opened... but Mozaik is used all day everyday."*
- Stephen Williams: *"I used CV for donkey's years and switched to Mozaik as I was tired of
  being gouged. I find Mozaik easier to use than CV."*

**Reading:** for standard box work the design-to-CNC coupling is solved, cheap, and users are
actively happy. Any claim that "software and machines don't talk" fails here. It survives
**only** in the custom one-off pocket described in Map A.

## Limitations (per the card)

- Forum posts support a provisional job statement; interviews are stronger.
- A named substitute does not prove dissatisfaction — dconti demonstrates the opposite.
- Switching costs are understated without workflow access.
- This method does not rank jobs, size the market, or establish willingness to pay. It has
  done none of those.
