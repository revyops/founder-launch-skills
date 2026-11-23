# Proof panels, callouts, big words and sound

For a talking-head Short where the speaker gives numbers, lists or a before and after. In the owner's own data, split-screen Shorts (the speaker in the bottom half, the thing they talk about on top) got several times the views of face-only Shorts. So every number or claim that can be shown gets a picture. Placement numbers are in `framing.md`.

## 1. Plan the panels before writing any code

Read the transcript line by line. Write a table: time, the words, what shows, and where each label comes from (transcript time, the brief, or the speaker's own panel words). A label with no source is a question for the speaker, not a guess.

| When the speaker says... | Show |
|---|---|
| The hook (first line) | A title opener, then a half panel that proves the hook's numbers (a counter, one mark per unit) |
| The line after the hook | A name card in the opener's spot, about 1 s |
| A big number or date about themselves that is in the brief | A callout card above the forehead |
| A correction ("10 times... probably 100") | A struck-out number: the big word lands, a line strikes it, the new number pops in with a hit |
| A list of things | A half panel, one card per item on its word, a closing chip |
| Work the viewer cannot see | A slow pan across the real thing (a screenshot, never a mock-up) with the speaker's own work steps ticking in |
| Old results (before) | Old clips playing muted in tiles, view counts as chips, a red "what was wrong" chip, a round badge with a cross |
| The new test or the turn | One full-screen beat of about 3 s |
| A key word with no panel | A swirl word (at most 5 in a minute) |

A 51-second Short had 4 panels, 2 callouts, 1 struck number, 1 swirl word, an opener and a name card. Something showed on about two thirds of the lines. Panels never overlap a callout. A number the speaker says with no fact in the brief (for example "nearly a thousand views") stays in the captions. A hook with nothing to count uses a gradient number or a short chip line plus one picture, or no panel. Never a fake count.

## 2. Panel types

- **Half panel:** a brand-coloured panel slides down over the top half (y 0 to 960) and pushes the speaker about 560 px down, so the eyes sit near 0.66 and the chin stays in frame. Captions stay on their line under the panel edge. Slide in about 0.35 s, out about 0.4 s, eased both ways.
- **Full panel:** one beat of 2 to 3 seconds to break the video up. It fades in and out as one piece with a 40 px rise. It never slides off, because sliding crops numbers at the top. Captions pause. Nothing important below about y 1400.
- **Unseen work gets shown.** When the speaker names work the viewer cannot see, show the real thing: a slow pan across a screenshot with held stops, and the speaker's own steps ticking in beside it about one line every 0.7 s. Give it at least 7 seconds of the speaker talking, hold the last line about 2 seconds, and let it run over the next line so no time is added. In a test, squeezing it into 6 s read as too fast. The lines are the speaker's work steps, never the screenshot's headings.
- **One panel can flow into the next.** Cross-fade inside the same panel. Never slide out and back in.
- **Callout above the forehead** for a big number or date the speaker says. A white card: a small grey lead-in, the big number in the gradient, an optional short line. A date gets a calendar icon. It pops in on the word with a soft whoosh, holds about 1.7 to 2.3 seconds, and leaves before a cut that would put it over the eyes (find cuts with a scene detector or the shot list). Its top is below y 290 and its bottom is above the eyes in every shot it spans. It sits inside x 110 to 970. Keep it modest. A first card reached y 275 and another ran x 78 to 1000. Both were too big.

## 3. Panel design: one look, with room to breathe

- **One kit per brand:** white cards with a soft shadow, small chips, gradient numbers and icon circles, a thin gradient rule where the panel meets the video. One font family for panels and big words (make big words large and scale them down, never up, so they stay sharp). Red only for "wrong".
- **Labels belong to the layout.** A panel's title is a chip right above its content. A closing line is a chip right under it. A view count is a white chip on the clip's bottom edge. What was wrong is a red chip on the clip. Never a loose grey word floating above or below things. No empty gap between a row and its label.
- **Elegant spacing.** At least about 30 px of air on each side of the longest line in any card or chip. Widen the card before shrinking the text. Card rows sit about 60 px from the screen edge (full-width rows are fine for cards, since the x 110 to 970 rule is for text floating over the face).
- **Cross-outs are a clean badge:** a round red badge (about 112 px) with a thin white cross and a soft shadow, and the thing behind it dims. Never thick drawn X lines. They look tacky.
- **No half-built rows.** When cards pop in on the word, each slot shows a soft empty card first, so a lone card never sits on a blank panel.
- **Motion:** items fade in, rise about 28 px, and settle from 0.86 to 1 with a soft overshoot. No wobble and no hard pops. Counters count up.
- **Let it land.** Every panel holds about 1 second after its last item before it leaves. The one exception is a hook panel that must leave early for the name card. Without a hold, "the text barely lands and you are already off the page".
- Spacing numbers that worked: navy chips with bold 40 px text, 34 px padding each side, height 1.9 times the text size. Channel cards 300x440, gap 30. Red chips bold 30 px, 24 px padding, 58 px tall.
- Check a still of every panel at its settled frame and its exit frame.

## 4. Big words (animated words)

- **Few.** About one every 12 to 15 seconds, never more than 5 in a minute. Put them on the lines that carry the story: the answer to the hook, the key numbers, the target. A first cut had 15 big words behind the head with a whoosh each. It read as "highlighting words randomly".
- **Swirl in front of the speaker** from low on one side, tilting from about 40 degrees to level, landing centred on the caption line in about 0.5 s, and standing in for that caption. Alternate sides. Only on front-camera shots. Side angles get captions only.
- The whole path stays inside x 110 to 970 and below the nose. A first swirl crossed the mouth and beard.
- One font. One accent word per clip: the number or word to remember.

## 5. Big word behind the head (depth captions)

A style where a big word sits behind the head and small captions sit in front. It works only on well-lit footage with a clear edge.

- **Film for it:** leave about a fifth of the frame above the head. Light the hair and the edge of the head. Keep the speaker about a metre from the wall. Dark, plain tops help.
- **A dark room with dark hair or a dark top: do not swap the room.** The cut-out tool cannot tell black hair from a black room, so the outline flickers and the shoulder vanishes into the new room. Keep every pixel the camera's own. Use the cut-out only inside the big word's letters, to decide which letter pixels the head hides. Only the lit head hides letters.
- **Never shrink the speaker** to make room. Copying edge columns outward smears at the sides.
- **Place the big word from the lit head top on every frame the word is up.** Use the highest the head gets (2nd percentile), not the middle. The head should cover only the bottom about 20% of the letters (about 10% for the key number), so the word still reads at phone size. Cap height at most about 230 px. Top at y 340 or lower.
- **Check the edge on every frame:** edge width about 4.5 px or less, no old-room colour, no copied edge rows. Smooth the cut-out in time (a 3-frame median inside each shot, never across a cut). A fixed mask from one frame is wrong. Look at 3 to 5 frames in a row at each word and cut for flicker.
- **Test on real footage:** an effect tried only on lit footage can fail on the real, darker footage.
- **Storyboard first:** a still for each big word before the full render.
- Soft shadow of the speaker on the letters. Pop in 80% to 105% to 100% over 6 frames. A soft whoosh per word about 24 dB under, a low hit on the accent word.

## 6. Sound for panels

- Sound marks ideas, not words. A soft whoosh (about -33 dB) on each panel and callout entrance and exit, about 0.02 s early. One hit (about -27 dB) when a struck-out number lands. Nothing on plain words and nothing on camera changes.
- One quiet bed about 19 dB under the voice. Voice about -14 LUFS.
- A Short ends about 0.6 s after the payoff line. A copy for a site or LinkedIn can add the end card.

## 7. Accuracy rules

- Every on-screen label is the speaker's own words, a fact in the brief, or the speaker's panel words. List any label you add so they can confirm it. Two labels that nobody said were flagged by a reviewer.
- A date goes on screen only after it is checked against the brief and a calendar. If two dates disagree, ask before rendering.
- Put facts (a launch date, a count) in the brief once, before the work starts.
- Clear out the old video's words, dates and numbers before you reuse its template. Search the files for them. Zero hits before the first render.

## 8. Build order for a panel Short

1. Cut, audio and captions first.
2. **Hook first.** Render the first 10 seconds and look at stills at 0.5, 1.5, 2.5, 3.5 and 4.2 s. Fix before building the rest. The speaker asked to see the first 10 seconds before the rest, and it saved a full round.
3. Write the panels from the map. After each one, look at stills.
4. Full render and mix.
5. Frame gate, edit gate, reviewer (`lessons.md`, section 6).
6. Cover (`covers.md`).
7. Send one version. Open the preview on the speaker's computer as well as sending it, if they ask for that.
