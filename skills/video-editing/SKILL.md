---
name: video-editing
description: Turns a raw phone video into a captioned 9:16 Short using only free tools (ffmpeg and local Whisper). Transcribes with word timestamps, picks whole-thought cuts at audio gaps, removes filler, burns bold captions, adds a hook title, crops to vertical inside safe zones, and checks frames before calling it done. Use when the user gives a .mov or .mp4 and asks to edit, cut, caption or subtitle it, make a Short or reel, or add a hook.
---

# Video editing: raw phone clip to a Short

## What this does

Claude writes and runs the commands. The tools are free and common: ffmpeg, ffprobe and a local Whisper. Nothing is uploaded anywhere.

The standard: a strong on-screen hook from the first frame, one clear argument made of whole thoughts, no filler words, natural short beats between cuts, clean captions, and nothing covering the face or sitting under the app's buttons.

Read `references/commands.md` before the first command. It holds the exact ffmpeg patterns, the Python helpers for cutting and captions, and the ASS caption template. Do not guess flags from memory.

## Set up once

Check that these exist, and install what is missing with the user's yes:

- `ffmpeg` and `ffprobe` (`brew install ffmpeg` on macOS, `apt install ffmpeg` on Linux).
- Burned-in captions need ffmpeg built with libass. Check with `ffmpeg -filters | grep -w ass`. If it prints nothing, install a full build (on macOS `brew install ffmpeg-full`, or a static build from the ffmpeg download page).
- Whisper: `pip install openai-whisper` (needs Python and ffmpeg). Alternative: whisper.cpp or `faster-whisper` if the user already has them.
- The font Montserrat ExtraBold as a `.ttf` in `fonts/` inside the working folder (free from Google Fonts). If it cannot be had, use any bold sans the user has, and say so.

Make a working folder next to the clip, for example `work/<clip-name>/`. Keep every intermediate file there. Never overwrite the original.

## Steps

1. **Inspect the file.** Run `ffprobe` for length, size, frame rate and audio. Phone files are often variable frame rate and may carry a rotation flag. ffmpeg applies rotation on its own. Check the real frame size with a still.
2. **Transcribe with word timestamps.** Use a prompt that keeps filler words, or Whisper will tidy them away. Read the whole transcript.
3. **Find the quiet gaps** with `silencedetect`. Every cut will sit in one of them.
4. **Plan, in plain sentences, and show the user:**
   - the **hook title**: under 8 words, first person, naming the viewer's problem. Write three, keep one.
   - the **shape**: list, steps or story. A story keeps its conflict, decision and lesson.
   - the **spoken hook**: 3 to 5 seconds, a self-contained claim, from the strongest line anywhere in the clip. If the best line already opens the clip, use no extra hook.
   - the **body**: whole thoughts only, in the order spoken.
   - **what is cut**: filler, false starts, repeats, dead air.
   Write the keep list to `work/<clip>/keep.json` as `[start, end]` pairs in source seconds, so it can be re-run.
5. **Snap each edge to a real gap.** Use the helper in the commands file. Keep about 0.15 s after the last word of a piece and 0.12 s before the first word of the next. Whisper word times can be off by a few tenths of a second, so trust the silence, not the word time.
6. **Cut and crop in one pass.** Build one ffmpeg filter graph from the keep list: trim each piece, join them, crop to 9:16, scale to 1080x1920, normalise loudness. One pass keeps audio and video the same length.
7. **Transcribe the output.** Run Whisper on the rendered cut. Use those fresh word times to build the captions. This also proves the cuts read cleanly.
8. **Build the captions and hook title** as one `.ass` file. Burn it in.
9. **Check** (below). Fix and re-render until it passes.
10. **Deliver.** Tell the user which file is final. Also write a 720p preview under 30 MB. Never upload or post anything for the user.

## Optional: relight into a better room

When the user wants the "before and after" studio look (a new room and real light on the face), do it as the last step, after the edit is locked. Follow `references/relight.md` and use the two scripts in `scripts/`. It needs an AI relighting tool, which is paid after any free tier, so ask the user first.

## Cutting rules

- Cut whole thoughts. Never splice a half sentence, and never cut on Whisper's word time alone.
- Cut in the quiet after a word's last sound, not on the word.
- A join carries a beat of about a quarter second. Half a second or more feels like an awkward gap. Cutting right against the words sounds jarring. After a dry run, the median gap should be about 0.25 s.
- Avoid pieces under about 1 second unless a filler cut forces one.
- Remove: um, uh, er, the first of a stutter ("is, is"), "you know", and a "so" or "and" that opens a passage when a gap follows it. Cut the filler as a burst of sound, from the quiet before it to the quiet after.
- Tell a leftover "uh" (low pitch, short, isolated) from a word ending (an "s" is high pitch) before cutting it.
- Leave no false start or half-said aside at a join. Cut it whole and go to the clean line.
- Never stack a new hook on top of the source's first line. If the hook is lifted from later in the clip, it should run naturally into the next line with no repeated words at the join.

## Captions

- Font: Montserrat ExtraBold, sentence case, white, a thin dark outline and a soft shadow.
- One to three words per caption, breaking at punctuation and pauses. Never a single-word caption: fold a lone word into the one before it. Keep symbols attached ("80%", not "80 %").
- Captions sit in the lower middle, above the bottom no-go zone, wrapped inside the side margins.
- Over a busy page or screen recording, put the captions in a solid box that contrasts with the page: white box with dark text on a dark page, dark box with white text on a light page. Never an accent colour.

## Hook title

- Shown from the first frame for about 2.5 to 3.5 seconds, then it goes away.
- Large, centred, in the clear strip of the frame, away from the face and away from the captions, so the two read as separate things.
- Never over the eyes, nose or mouth.

## Safe zones for 9:16 (the strictest of Reels, TikTok and Shorts)

| Zone | Size of the 1080x1920 frame | Why |
|---|---|---|
| Top | 13% (about 250 px) | App header and tabs |
| Bottom | 25% (about 480 px) | Caption, username, audio line |
| Sides | 12% each (about 130 px) | Like, comment and share buttons |

All text lives inside x 130 to 950 and y 250 to 1440. Ask for a landscape clip? Keep 16:9, skip the crop, and note that YouTube's controls cover the bottom 10%.

## Check before saying done

1. **Zones image.** Draw the no-go zones on a still and look at it (command in the commands file). Title and captions must be inside the clear area.
2. **Stills** from the hook, the first caption, a mid-clip frame and the last frame. Look at each one.
3. **Re-transcribe the output** two ways: with the filler prompt (no fillers or repeats left) and without (the story reads cleanly with no clipped words). Listen to or re-check every changed join, the close above all.
4. **Black-frame scan** and a quick loudness check.
5. **Length and size.** Duration, 1080x1920, audio present, plays from the start.
6. **Edges.** Every cut edge sits in quiet. No clipped consonants at the starts and ends of pieces.

If a check fails, fix it and re-render. Do not tell the user it is done until all six pass. Say what was checked, and name anything you could not check.

## Never

- Re-encode the final more than once. Render from the original each time.
- Crop a landscape export to make a Short when the story needs a proper vertical cut. If the source is landscape, put the speaker in the crop and check the face is not cut off.
- Put text over eyes, nose or mouth, or inside the app zones.
- Fade to black at the end without a reason. End on the last spoken line plus a short hold, or on an end card with one clear ask.
- Add a channel-specific ask ("comment below") to a video that will go on several platforms.
- Post or upload anything. The user does that.
- Say it is finished without looking at frames.
