---
name: social-posting
description: Helps a person run their own LinkedIn after the content is written. Posts an approved piece with the link in the first comment, replies to and likes comments at a human pace, runs "comment WORD" keyword posts with a public reply and tracked opt-in link to each requester, tags links with UTMs, and logs requests in a CSV. Use for "post this to LinkedIn", "reply to my comments", "run a keyword post", "track my post links".
---

# Social posting for LinkedIn: posts, replies, keyword DMs

## What this does

It helps the user run their own LinkedIn account once the content is already written and approved:

1. Post an approved piece, with any link in the first comment.
2. Reply to and like comments on the user's own posts, at a human pace.
3. Run a keyword post ("comment WORD and I'll send you X") where each requester gets a public reply with a tracked opt-in link.
4. Tag every link with UTMs so sign-ups trace back to the post.
5. Log requests in a simple CSV in the user's project.

Writing the post itself is a separate job. If the `copy-doctrine` skill is installed, use it for the text. Otherwise follow the voice notes below.

## Safety rules (read first, they hold for everything below)

- **The user's own signed-in browser only.** Work in the browser tab the user has open and signed in. Never ask for a password. Never run anything from another account.
- **Nothing is sent without the user's yes.** Show the exact text for each post, reply or message and wait for a clear yes for that piece. A yes to one post is not a yes to the next. Ask once before a batch of replies, showing every reply, then post them.
- **Own posts and own account only.** Reply to people who commented on the user's own posts. Do not comment on other people's posts, send cold messages, follow, or accept or send connection requests unless the user asks for that specific action.
- **Small caps and random gaps.** Keep volume low and spacing uneven. Reply gaps of 45 to 150 seconds, at most 20 replies an hour, and on a keyword post at most 10 an hour. Post one piece at a time, at least 2 hours apart. Work in normal waking hours. A long queue is never a reason to speed up.
- **Type, do not paste.** Enter text in small chunks, the way a person types.
- **Stop at the first warning.** A sign-in page, a captcha, a limit notice, an "unusual activity" message or any LinkedIn warning: stop at once, do nothing more, tell the user. Never try to solve a captcha. Never retry in a loop.
- **No deleting or reposting to fix a mistake** (for example a first comment that failed). Leave the post, tell the user, and let them decide.
- **Only what the user switched on.** Do not like, comment, message or follow anything the user did not ask for.
- **No scripts that read or collect LinkedIn data in bulk.** Read comments by looking at the post in the browser, the way the user would.

## Setup

Ask the user, once:

1. Which of the three jobs they want: posting, replies, keyword posts.
2. For replies: approve each reply first, or let you post after they have seen the batch.
3. Where the link goes (the page people should land on), and the base URL for it.

Create a `social/` folder in the project with:

- `social/requests.csv` with the header: `date,post,keyword,first_name,profile_url,comment_url,link_sent,status,notes`
- `social/posts.csv` with the header: `date,post_url,topic,first_comment_added,utm_content,notes`

Keep both files plain, and never write a password, token or private message text into them.

## Job 1: Post an approved piece

Needs: the final text, any image or document, and the link (if there is one).

1. Build the tracked link (see "Tracked links" below). The body of the post never carries it.
2. Show the user the final text, the media and the first comment text. Get a yes.
3. In the user's browser, open the post box, type the text, attach the media, and publish. Public. Do not add hashtags the user did not write.
4. A post with a link in its body reaches fewer people, and a link in the post looks like an ad. If the post needs a link, end the body with a line such as "link in the comments".
5. Open the new post. Add the first comment with the tracked link. Reload the page and confirm it shows.
6. Record the post URL and time in `social/posts.csv`.
7. Rules for media: a carousel goes up as a PDF document upload, and the document title is the hook. A video goes up as the original file, not re-encoded. If the video has a designed cover image, set it in the composer before posting, because the cover cannot be changed after. If the cover cannot be set, wait and ask.
8. If anything is off (sign-in page, upload failure, text changed since approval), do not post. Tell the user.

## Job 2: Reply to and like comments

Reply only on the user's own posts, and only where someone else spoke last.

1. Open each recent post (last 14 days) in the browser and read the comments on the page. Note each commenter's first name and what they said.
2. Draft one reply per open thread. Show all drafts to the user for a yes.
3. Post each reply, then like that comment. Check the like button first: a second click removes the like.
4. Like every comment you handled, including ones that need no reply, so an unliked comment means nobody has looked at it. Never like spam or a pitch.
5. Skip company pages, spam, pitches, and threads where the user spoke last. Skip comments older than 14 days unless they ask a direct question.
6. Leave real conversations alone. If the person wrote last and it needs thought, tell the user.

**Voice for replies.**

- Write the way the user talks. Use their own words from the post and their notes.
- Start with the person's first name, then go straight to the answer. Do not echo their words back ("Great point", "Brutal is the word").
- Often one or two sentences. Many end on a statement. Ask a question only when the user truly wants the answer.
- Use only facts the user has given you. Any other claim waits for the user to confirm.
- No links in replies, except on a keyword post (below).
- No two replies on one post open the same way. Do not give every reply the same shape.
- No em dashes, no rhetorical questions, no stock idioms. Do not name a person's company unless they named it.

## Job 3: Keyword posts ("comment WORD")

A keyword post offers something (a guide, a template, a checklist) to anyone who comments a chosen word. This setup delivers it with a public reply that carries a tracked opt-in link, so the person still gives their email, and nobody needs to be a connection.

Before the post goes out, make sure these exist:

- The offer is ready, and a page where people can opt in to get it. The page has one call to action: its opt-in, nothing else.
- A tracked link to that page for replies (see "Tracked links").
- At least five reply wordings, each using the person's first name. Examples: "Hi {first_name}, here is the sign-up page for the guide: {link}", "{first_name}, you can grab it here: {link}", "Sent. {first_name}, the link is {link}", "{first_name}, it's on this page: {link}", "Thanks {first_name}. Opt in here and it lands in your inbox: {link}". Add more of your own. Never paste the same text many times, because LinkedIn notices identical text repeated.
- The user's written yes to replying to everyone who comments the word.

Run it:

1. Read the post's comments in the browser. Find comments that contain the exact word, from the last 14 days.
2. One reply per person per word, ever. Skip anyone already in `requests.csv` for this word.
3. Pick a wording that differs from the last two used. Fill in the first name and the tracked link.
4. Show the user the batch of replies and get a yes.
5. Post each reply at the keyword pace (at most 10 an hour, with random gaps), and like the comment.
6. Add one row per person to `social/requests.csv` with status `link replied`.
7. If the user wants a follow-up, draft it as a note for the user to send. Do not message anyone yourself unless the user asks for that specific message and gives a yes.

Do not send the resource itself in a reply. Send the opt-in page, so the person opts in to get it.

## Tracked links

Tag every link so a sign-up traces back to its source. Use UTMs on the URL:

`https://example.com/page?utm_source=linkedin&utm_medium=social&utm_campaign=<campaign>&utm_content=<post-slug>-<where>`

- `utm_source` is `linkedin`. `utm_medium` is `social`.
- `utm_campaign` names the offer or theme, in lowercase with hyphens.
- `utm_content` names the post and where the link sits, for example `guide-launch-firstcomment` or `guide-launch-reply`, so the first comment and the replies can be told apart.
- Lowercase, no spaces, no personal data in any parameter.
- Record each tracked link in `social/posts.csv` (`utm_content` column), so results can be matched later.

## Reading results

When the user asks how a post did, give: what was posted and when, replies and requests logged, sign-ups per `utm_content` if they can share the count, and one line on what to change. Say "not read" for anything you cannot see.

## Done-check

- Nothing was posted, replied or liked without the user's yes for that piece.
- Each post shows as live with its link, and the first comment shows after a reload.
- Every link in a comment carries UTMs, and the body of every post is link-free.
- Every comment handled has a like, and every keyword requester has one reply and one CSV row.
- No two replies on a post open the same way, and no reply echoes the commenter's words.
- Pace stayed inside the caps. If a warning appeared, work stopped and the user was told.
- `social/requests.csv` and `social/posts.csv` match what happened.
