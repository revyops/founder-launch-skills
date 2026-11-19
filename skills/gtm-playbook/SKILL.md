---
name: gtm-playbook
description: Starter go-to-market skill. Interviews you and writes a one-page ICP (company and buyer) plus an anti-ICP, defines a 1-5 fit score with plain criteria, grades a CSV list against it, and splits the list into named lead pools ranked by who to contact first. Use when someone says "write my ICP", "who should we sell to", "score this list", "grade these companies", "rank my leads" or "build lead pools".
---

# GTM playbook: ICP, fit score, lead pools

This skill does three jobs, in order. Do them one at a time and confirm each with the user before moving on.

1. Write the ICP and anti-ICP.
2. Define a 1-5 fit score and grade a list.
3. Split the list into lead pools.

It does nothing else. If the user asks for more, say that is outside this starter.

## Rules for you

- Ask before you write. Do not invent the user's customers, numbers or evidence.
- Every grade needs a reason and evidence (a URL or a quoted line). No evidence, no grade.
- Missing evidence is a 3, never a 2. A wrong 2 hides a good company for a long time. A wrong 4 costs one message.
- Never send, post or contact anyone. This skill only reads, scores and sorts.
- Save outputs as plain files in the user's working folder, and tell them the file names.

## Job 1: Write the ICP

An ICP answers one question: is this the kind of company we sell to? A researcher, or you, must be able to answer it from outside the company, using public evidence, before anyone has spoken to them.

### Interview

Ask these in one short message, then wait:

- What do you sell, and to whom? Who bought it and was happy?
- Who bought and regretted it, or never bought?
- What does the business model of your best customers look like?
- What size are they (employees, revenue, locations)? What can they afford?
- Which regions do you serve?
- What makes a company need this now?
- Who signs, who uses it, who blocks it?

If the user has a customer list, ask to read it and look for the pattern in the best ones.

### Write the one-page ICP

Use these headings, and keep the whole page to one screen.

**Company**
- **One-line shape:** the business model in a sentence. The model is usually the whole test.
- **Hard gates:** two or three yes/no tests. Fail one and the company is out. Each must be checkable from public sources.
- **Size and region band:** phrase it as "can they afford this?", not as a price tag.
- **Timing signals:** what says they are in market now (a new leader, a funding round, a hiring push, a public move into this area). Only a timing signal lifts a company up a grade.
- **Nice-to-haves:** positives that order companies inside a grade but never admit them.

**Buyer**
- Titles to contact first, in order. Start with the owner or the person who runs this business unit.
- Who else is involved (user, blocker).
- Record titles exactly as the person uses them. A hired CEO is "CEO", not "owner".

**Anti-ICP**
- A short list of shapes that are never a fit, each with a one-line reason. A disqualifier with no reason gets argued away.

### Rules for good gates

- A gate answers "is this the kind of company we sell to". Anything that answers "how will the sale go" belongs on the sales call, not in the gate.
- Put the size band and any ownership disqualifier (for example, owned by a much larger group) in the gates from day one.
- If a gate rejects almost everything you expected to fit, suspect the gate before the market.
- Write one test question for each category, such as "does this practitioner have an employer who buys tools?".

Save as `ICP.md`. Ask the user to correct it. Expect two or three rounds.

## Job 2: Fit score 1-5 and grade a CSV

### The scale

| Grade | Plain criteria | Action |
|---|---|---|
| 5 | Passes every gate and shows a timing signal | Contact first |
| 4 | Passes every gate, no timing signal | Contact |
| 3 | Passes every gate except one that could change, or the evidence could not be found | Hold, recheck later |
| 2 | Fails a gate but is a near miss | Hold, long recheck |
| 1 | Matches the anti-ICP | Never contact |

Fit decides whether to work a company. It does not say how warm they are. A busy company that is a bad fit is still a 1.

Store the grade as a fixed value from 1 to 5, and filter by "is one of 4, 5", never "4 or more". A numeric comparison silently drops rows with no grade.

### Grade a list

1. Ask for the CSV. Read the header and a few rows. Say which columns you will use (company name, website, size, region, title, anything else).
2. Confirm with the user which grade counts as "worth contacting" (default: 4 and 5).
3. Grade every row against the ICP. For each row add four columns: `fit`, `fit_reason` (one sentence naming which gates passed or failed), `evidence` (a URL and a short quote, or "none found"), `graded_on` (today's date).
4. Never reject on partial evidence. Read the whole page before failing a gate. If you cannot check a gate, grade 3 and say which gate.
5. Grade rejects too. Writing down the 1s and 2s stops anyone researching them again.
6. Spot-check with the user: show the 10 rows you were least sure about and ask them to correct any grade. Update the rubric if the same error repeats.
7. Optional check before trusting the rubric: grade a few past winners and a few past losers without telling yourself which is which. Winners should land mostly on 4 and 5. If not, fix the ICP first.

Save as `graded.csv`. Never overwrite the user's original file.

## Job 3: Lead pools

Split the graded list into a few named pools. Rank them by who to contact first.

Use these defaults and change them with the user:

| Rank | Pool | Who is in it |
|---|---|---|
| 1 | Best now | Grade 5, buyer title found and matches the first title in the ICP |
| 2 | Strong fit | Grade 4, buyer title found |
| 3 | Fit, wrong or missing contact | Grade 4 or 5 where the buyer is not yet found |
| 4 | Hold | Grade 3 |
| 5 | Parked | Grades 2 and 1 |

Rules:

- Each row sits in exactly one pool. Add a `pool` column and a `pool_rank` column.
- Inside a pool, order by timing signal first, then size band fit.
- One person per human: if the same person appears twice, keep one row.
- Write a short summary: how many in each pool, and the three biggest reasons companies fell out.
- Offer to run a different split if the user prefers one (for example by region or by product).

Save as `lead-pools.csv` and `lead-pools-summary.md`.

This is the starter. Sequences, statuses and scoring come later.
