# Teaching it to remember

Claude forgets each conversation when it ends. Anything you want it to know next time has to be written down. Think of training a new hire, except you only say a thing once, as long as it gets written down.

For the first few weeks you will say "no, not like that" a lot. Then you will notice it has stopped making the same mistakes. The reason is everything you had it write down.

## Four places it remembers

| Place | What goes there | Example |
|---|---|---|
| Vault notes | Knowledge: what happened, what you decided and why, research, how a process works | "Account history for our five biggest customers" |
| Skills | Instructions for a recurring kind of work, loaded when that work comes up | "How we write copy"; "how every report is laid out"; "how to review a sales call" |
| Standing rules (a file called `CLAUDE.md` in your working folder) | The few rules that apply to everything, read at the start of every session | "Never send, spend, publish or delete without showing me first" |
| Memory | Short facts Claude keeps about you and your preferences | "Prefers tables to paragraphs" |

You do not need to manage these yourself. Say what you want kept and ask Claude where it belongs. All four are plain text you can read and edit.

## How to make a skill

After any piece of work you would want done the same way again:

> "Write a skill from this. Next time I ask for something like this, I want it done the way we just landed on."

After any correction you never want to repeat:

> "Add that to the skill so you never do it again."

### An example worth copying: writing that does not sound like AI

AI writing has tells: dashes everywhere, rhetorical questions, "it's not X, it's Y", the word "seamlessly". Feed Claude a pile of your own writing and have it build a set of copy rules. Then every time it writes copy, it checks the draft against those rules first. Build this early. It pays off in every email, post and document.

## The end-of-session habit

Before you close any conversation that taught Claude something, say:

> "Make sure everything we learned and decided in this session is saved in the vault and in the right skills. Tell me what you saved and where."

This is the difference between an assistant that improves every week and one that starts over every morning.

## Keep the knowledge clean

- **One home per fact.** If the same rule lives in two notes, they drift apart and Claude follows the wrong one. Ask it to link, not copy.
- **Record the reason**, not just the decision. A rule with no reason gets changed in six months by someone who does not know what it was protecting.
- **Date anything that will go stale:** prices, plan limits, "currently", "as of".
- **Prune.** Every month or so ask: "Review the vault for duplicates, contradictions and outdated notes, and show me what you would change."
- **Do not paste customer data exports into the vault.** Facts about people go stale within weeks. Keep them in your CRM and let Claude look them up live.
