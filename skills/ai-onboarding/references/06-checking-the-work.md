# Checking the work

Claude will sometimes state things that are not true, with complete confidence. It fills gaps with guesses that sound right. You cannot switch this off. You can make it rare and catch it when it happens.

## Make it rare

- **Give it the real data**, read live from the tool that owns it. Most made-up answers come from missing or stale information.
- **Ask for sources.** "Cite where each number came from." A claim with no source is a guess.
- **Tell it to stop rather than guess.** Add a standing rule: "If you cannot get the data, say so and ask me. Never estimate, average or fill in."
- **Keep the vault clean** (see `05-teaching-it-to-remember.md`). An outdated note produces an outdated answer.

## Catch it when it happens

- **Spot-check numbers against the source.** Open the tool and look at two or three figures yourself, especially the first time a report runs.
- **Ask it to check itself.** "Go back through what you just told me and verify every claim against the source. List anything you are not sure of." It finds a surprising amount.
- **Be suspicious of round, tidy answers** and of anything that confirms exactly what you hoped.
- **Watch it when it works inside a live system.** Look at what it built before it goes live.

## Audit reality first

Before you ask Claude to improve something, have it establish what is true today. Pull the real numbers, read the real history, list what exists. Then compare against the outside baseline. Recommendations built on an audit are worth having. Recommendations built on assumptions are not.

## Watch your scheduled jobs

Jobs fail quietly. A report that did not run looks the same as a report you have not opened yet.

- Check the scheduled jobs list for anything marked skipped or failed. The usual cause is a computer that went to sleep. Press Run now.
- Once you have a few jobs, build a review job whose only task is to read the other jobs' output each morning and tell you what ran, what looks wrong and what is waiting on you:

> "Create a daily job that runs after all my other jobs. It checks each one ran, flags anything that looks off, and gives me a short to-do list of what needs me today."

## The weekly question

Once a week ask: "What have you been unsure about this week, and what did you assume rather than check?" The answers tell you where the vault needs work.
