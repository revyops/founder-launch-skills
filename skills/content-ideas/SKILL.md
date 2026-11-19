---
name: content-ideas
description: Turns the user's work day into post ideas. While helping with any task, it notices things worth posting (something built, fixed, decided, a number, a mistake) and raises them as short idea cards at the end of the reply, logged in an ideas.md file. Use when the user says "any post ideas from this?", "what could I post about today", "turn my work into content", asks for LinkedIn, Short or YouTube ideas, or answers yes or no to an idea already raised.
---

# Content ideas

## What this does

A founder's work day is the best source of content: what they built, what broke, what they decided and why. This skill watches for those moments while you do the work they asked for. It raises the good ones as idea cards at the end of the reply. The user says yes or no. A yes gets drafted. A no gets logged and never raised again.

Claude raises. The user decides. Never publish or schedule anything.

## Set up once

Look for `ideas.md` in the project root. If it does not exist, create it, then ask the user three questions and write the answers at the top:

1. Who is the audience? (Who should read or watch this, and what do they already know?)
2. What do you sell or want to be known for?
3. What can never be posted? (Customer names, revenue, staff, anything under contract, subjects you avoid.)

The log below that header is one line per idea:

```
2025-03-04 | Fixed the double-booking bug | LinkedIn text | raised
2025-03-05 | Why I killed the weekly report | Short | yes
2025-03-06 | Pricing page teardown | LinkedIn text | no: too close to a client
```

## When to raise an idea

Raise one only when it passes all four checks:

1. **New.** Search `ideas.md` and the user's published pieces for the same point first.
2. **Useful.** It serves something the user is trying to do: a launch, explaining what they sell, answering a question a buyer would type into a search box or an AI, or telling their own story.
3. **A stranger would care.** There is a fresh event, a number, a decision with a reason, a mistake, a contrast, or a view people would argue with. A generic tip fails.
4. **It can go out.** The user can back every claim, and nothing in it is private.

Things that usually pass: something built or fixed today, something that broke and what it taught, a number that surprised, a rule the user just set and why, a before and after, a question a prospect asked, a change of mind.

## How to raise one

- Finish the work first. The idea goes at the end of the reply, under its own heading. Never interrupt a task to raise one.
- One or two ideas a turn. Three on a rich turn. Volume comes from raising them across the day, not from padding one reply.
- Quote the line the user said that sparked it. Use their words.
- Use this card every time:

> **Post idea: working title**
> **Why it fits:** the goal, play or buyer question it serves, in one line
> **Where and how:** each channel it suits and the format, such as LinkedIn text post, Short, long video segment, newsletter item, or a page answering a search question
> **Hook:** the first two lines, written out. **Or:** one alternative
> **Copy:** the shape (list, steps or story), then three to five beats, then the call to action
> **Needs from you:** nothing, a 60-second recording, or a number to confirm

- End with one line: "Say yes and I'll make it."
- Add the idea to `ideas.md` in the same turn, marked `raised`.

## Writing the hook and the copy

Read `references/hooks.md` before writing the first hook in a chat. It holds the hook rules, the three shapes and the hook checklist. Short version: every piece is a hook, a body that delivers it, and a closing line that pays off the promise.

## On a yes

Draft the piece in full from the card. Run the checklist in `references/hooks.md`. Save the draft next to the log (for example `drafts/2025-03-05-kill-the-report.md`). Update the log line with `yes` and the file name. Tell the user what is left for them to do: record, confirm a number, or post.

If the chat is busy with other work, finish that first.

## On a no, or no answer

Update the log line with the reason and never raise it again. No answer is not a yes, and is not chased. The idea stays in the log as `raised` for the user to pick up later.

## Never raise

- Anything private: a customer's name or data, staff, pay, revenue, a deal, a dispute. The lesson can go out in neutral words ("a client", "the rep"). The detail cannot.
- Anything the user listed as off limits at set up.
- A claim the user cannot back, or a story that did not happen. Never invent history, quotes or numbers.
- A pitch. The idea teaches or tells. The offer belongs in the call to action.
- A rival's name or an attack on one. Say "most tools" or "others".

## Learn from the log

When the log shows a pattern (a kind of idea the user always takes or always refuses), write one line about it at the top of `ideas.md` and raise more or fewer of that kind.

## Done check

- The work the user asked for is finished and comes first in the reply.
- Each card has all six parts, and the hook is written out.
- No idea repeats one already in the log.
- Nothing private is in any card.
- The log is updated.
