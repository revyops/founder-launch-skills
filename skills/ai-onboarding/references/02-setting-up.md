# Setting up

Setup is the most annoying part. You spend it connecting tools and loading history, and none of it feels like progress. Everything after it is faster because of it.

## 1. Install three things

| Install | What for |
|---|---|
| **Claude desktop app** | Needs a paid Claude plan. Check the current plans on Anthropic's pricing page. A lighter plan is fine to try it. Heavy all-day use needs a higher one |
| **A notes vault app** (Obsidian is a good free choice) | Shows your folder of notes. Claude reads and writes the files directly; the app just makes them easy for you to browse |
| **A voice dictation tool** | You will talk to Claude far more than you type. Good dictation removes the "um"s, tidies the sentence and works in any app. The dictation built into your computer also works, though it may drop out |

### Use Code mode

The desktop app has two modes: Cowork, made for office work, and Code, made for developers. Use Code. It looks almost the same, but it handles your computer and browser well and shows its thinking clearly. You will never have to read the code it writes.

Claude Code also runs in a terminal (the black text window). Use the desktop app instead. It gives you readable reports, a built-in browser, scheduled jobs and chats you can group by project.

## 2. Change the settings

In the Claude desktop app, open Settings and find the Claude Code section. Look for settings like these, and check the wording on screen:

| Setting | Why |
|---|---|
| Keep computer awake while Claude works | Scheduled jobs only run when your computer is awake |
| Remote control | Lets you check on and answer Claude from your phone |
| Allow bypass permissions mode | Lets Claude work without asking you to approve every step. See below |

### Permissions: start careful, then let it run

By default Claude asks before each action: every file it writes, every command, every tool call. Leave it that way for your first few hours while you watch what it does.

After that you will want fewer prompts. Approving everything by hand gets old within a day, and Claude cannot work overnight if it is waiting for a click. Move to "always allow" on the connectors you trust, and consider bypass permissions mode once you are comfortable.

Keep your hand on the irreversible buttons. Even with fewer prompts, set it up so Claude drafts and you approve anything that:

- **Sends** to a customer or a public channel (emails, posts, support replies)
- **Spends money** (launching ads, raising a budget, paying a bill)
- **Deletes** or overwrites records in a live system
- **Publishes** anything public

Tell Claude once, for example "never send, spend, publish or delete without showing me first", and have it save that as a standing rule (see `05-teaching-it-to-remember.md`).

## 3. Make your vault

A vault is a folder of notes.

1. In your notes app, create a vault inside your Documents folder.
2. In Claude desktop, start a new Code session with that folder selected as the working folder. Claude now works inside your vault.
3. Ask Claude to set up the folder structure with you (below).

### Lay it out before it grows

Claude will happily create a new folder for every idea. Within a few weeks you have a sprawl. Set the shape early:

- One top-level folder per area: the company, each client, your own playbooks, personal.
- Inside a company, one folder per function: sales, support, marketing, product, finance.
- Every folder opens with a `00 - Start Here` note that says what is in it and where to start reading.
- Number the notes (`01`, `02`) so the reading order is obvious.
- Tell Claude: "Do not create a new top-level folder without asking me." Have it save that rule.

### Sharing with a team

Most notes apps can sync a vault between people and devices. Each person adds their own folder (product, support, finance) to the shared vault, and anyone's Claude can then answer from all of it. A new account manager can ask "where are we with this customer, and what went wrong last time?" and get the history.

If your team already lives in a shared workspace tool, connect that to Claude instead and keep shared knowledge there. A common split: the shared tool for what the team edits together, your vault for your own working notes. Pick one home for each kind of note so nothing is written twice.

Send any sync or encryption password privately, never in a recorded meeting or a shared channel.

Your computer is a single point of failure. If the vault only exists on your laptop and the laptop is lost, the vault is gone. Sync or another backup fixes that.

## 4. Connect your tools

A connector lets Claude reach into a tool and use it the way you would, through the tool's own back door rather than by clicking around a web page.

Two ways to add one:

- **Ask Claude.** "Connect to my help desk." It finds the connector and gives you a Connect button. A sign-in window opens, you approve the access, and you are done. Some tools ask for an API key, a long password the tool generates for you. Paste it only into the tool's own setup screen, never into a chat.
- **Add it yourself** in the desktop app under Customize, then Connectors. Popular tools are listed there. Less common ones are added as a custom connector with a web address.

Each connector lists permissions: what Claude may read and do inside the tool. Allow them unless something is truly sensitive, and keep the rule about irreversible actions from section 2.

### Connect these first

| Connector | Why it is worth it early |
|---|---|
| Your meeting recorder | Claude can find and read every recorded call, so you never paste a transcript again |
| Slack or Teams | History of decisions; Claude can also post drafts for you to approve |
| Email and calendar | Context on every relationship |
| Your CRM | The customer and prospect record |
| The one tool your first use case depends on | The help desk, the ad account, the analytics tool |

### When there is no connector

Claude can use a browser like a person does. The desktop app has a built-in browser. Claude opens the site, you sign in yourself, you say "I'm in", and it carries on.

- Sign in yourself. Never type a password into the chat.
- Give the browser enough room on screen. Squeezed into a small panel it gets stuck.
- Some sites log you out often, so expect to sign in again. A connector avoids this.

### Desktop apps

Claude can also use apps on your computer when no connector or website does the job. You approve each app once per chat.

- Do not put apps in full screen with the green button. Full screen gives each app its own desktop, and Claude cannot reach a window on a different desktop. To fill the screen, double-click the window's title bar instead.
- Tell Claude which app to use if you keep a tool signed in as a desktop app rather than in the browser, and have it save that.

## 5. Organise your chats

You will soon have several conversations going at once. Group them by project. One chat per piece of work keeps each short and focused, which also saves money (see `07-long-chats-and-tokens.md`).
