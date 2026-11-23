# Relight: put the speaker in a better room

How a plain phone clip gets a new room and real studio light on the face: the "before and after" look. This is everything learned from four rounds of tests in November 2026. Prices and free tiers are as of then; check the tool's page before you spend.

## The short version

- **Use Higgsfield's Editing Room › Change location**, with one studio picture you made as the reference. It relights the person to match the room, the room moves (haze, neon), and the face and lips hold.
- **Relight last.** Lock the edit first, relight the clean base, then put titles and captions back on.
- **Then fix three things in code:** put the cuts back on the source frames (`relight_align.py`), upscale 720p to 1080 (`relight_assemble.py`), and lift the face a little (`facelift.py`).
- **Check every shot** against the source. Redo a bad shot at most twice.

## Why not a colour grade or a background swap

A better-looking clip comes from the person being **relit to match a better room**. A LUT or grade on the camera file can't add light that was never there, and it shifts skin colour (a grade once turned a speaker red). Never grade the face.

A plain background swap (cut the person out, put a new room behind) looks pasted on: the light on the face doesn't match the room, and a strong coloured room glows round the head. If you must swap without a relighting tool: zoom the room to close-up scale (about 1.4x), blur it like a fast lens, darken it (about 0.6x), take out half its colour, warm it slightly, and let about 25% of the room's colour onto the outer few pixels of the speaker (light wrap). It still won't match a real relight.

**Dark room and dark hair or top: don't swap at all.** The cut-out can't tell black hair from a black room, so the outline flickers and the speaker "disappears into the background". Keep the real room.

## What we tested (so you don't have to)

| Way | Result | Use it? |
|---|---|---|
| Kling Omni Edit with a text prompt only ("bright office") | Relit, but flat and video-call-like; mouth drifts on some frames; face a bit waxy close up | No |
| Omni Edit with a detailed studio prompt | Premium room, but face goes soft and waxy, mouth drifts | Only for an ad hook |
| Omni Edit with your own studio picture as reference | Best face and lips of the Omni tests, room matches the picture. But the background is frozen: haze and neon never move, and the light on the face is weak | No, for moving rooms |
| **Editing Room › Change location** with the studio picture | Haze and neon move, real warm/cool split on the face with a hair rim, likeness and lips hold even close up. Only gap: 720p | **Yes** |
| Image-to-video of the studio picture, then our own cut-out composite | The set moves, but the person looks pasted on; the light sits on the skin, not in it | Only if the Editing Room is not an option |

**Rule:** to change the room and the light, use the Editing Room (Change location, or Relight for light only), not Omni Edit. Omni Edit keeps the source's stillness, so its background never moves.

## What it costs (Nov 2026)

- Change location: about 7 credits a second at 720p, 20 a second at 1080p.
- There was a free window of 50 seconds at 720p, then up to 5 free seconds a job.
- Omni Edit at 1080p: about 10 credits for 5 seconds, 25 for 10 seconds.
- Video Relight on its own: about 135 credits per 15 seconds outside free time.
- A full 10-second run takes about 5 to 15 minutes.
- Ask the user before spending credits.

## Make the room once

1. Generate one empty studio picture, 9:16, with an image model. Describe the layers, not just "office": back wall (brick, slats), shelves, practical lights (hanging bulbs, LED strips, a neon panel), haze, depth and bokeh, a warm key side and a cool rim side.
2. Reuse that same picture in every video, so your videos share one set.
3. A plain prompt like "office" gives a flat result. Write the studio.

## Steps

1. **Lock the edit.** Cuts, angles, captions and sound all approved. Export a clean base (`base.mp4`, 1080x1920, no titles, no captions, no sound). Never relight the final with titles on it.
2. **Test 6 to 8 seconds** that cross every camera angle and at least two cuts. Check: one room across angles, colour on the face, no holes or white patches, the face still looks like the person. The speaker approves the test before the full run.
3. **Run the full clip in parts of 30 seconds or less,** split on a cut. Use the same reference picture and the same prompt, word for word, on every part. In the prompt, name:
   - the motion in the room (drifting haze, pulsing neon, flickering bulbs),
   - the light on the person (warm orange on one cheek, cool blue on the other, bright hair and shoulder rim, shirt lit),
   - what must not change ("keep face, lips, motion and framing exactly the same").
   A part under about 3 seconds won't upload on its own: add it as a second edit inside the next part's job.
4. **Download and look at the file.** The editor's preview thumbnail can show the reference picture, not your result.
5. **Rebuild the base.** The tool returns 720p at 24 fps. List each part with where it starts and how many 30 fps frames it must fill, then run
   `python scripts/relight_assemble.py pieces.json relit_raw.mp4`
   It retimes to 30 fps, upscales to 1080x1920 (Lanczos plus light sharpening) and holds the last frame if a part comes back a frame short.
6. **Put the cuts back on the source frames.** The tool keeps the picture in time but moves each cut 2 to 3 frames late, so lips drift. Run
   `python scripts/relight_align.py base.mp4 relit_raw.mp4 aligned.mp4`
   Per shot it finds the relit cut, measures the lip lag from motion and writes the source's exact frame count.
7. **Lift the face.** The relit face, looking at the camera, often comes back too dark and grey ("skin looks dead"). Run
   `python scripts/facelift.py aligned.mp4 lit.mp4`
   It adds a soft face-only key: about a third of a stop, slightly warmer, about 15% more colour, highlights capped, room untouched. It works in two passes so it never flickers: first it finds the face in every frame and splits into shots at the cuts, then inside each shot it fills gaps, drops stray boxes and smooths the box over 15 frames. A shot where the face is found in under 40% of frames gets no light at all.
8. **Check every shot, not a few frames.** One frame per shot against the source. Faults we saw:
   - a shot left on a plain grey backdrop (a low side camera looking up),
   - a see-through desk over the chest,
   - a side angle turned into a front view by a redo,
   - a part that came back framed wider than the source.
   Redo with the fault named in the prompt ("no desk", "keep the low side camera, do not turn it into a front view"). A redo can change the angle, so check it the same way.
9. **Two failed redos of one shot: stop paying.** Keep the original shot and tone it toward the room:
   `python scripts/splittone.py in.mp4 out.mp4 FIRST_FRAME LAST_FRAME`
   (shadows toward the room's colour, highlights a little warm; set the colours at the top of the script). A low camera looking up at a dark ceiling passes this way.
   **Framed wider:** measure the face size in the source and the relit part and punch in to match (one part needed 1.57x).
10. **Put everything back on.** Re-make any cut-out (for words behind the head) from the relit base, then re-render the same titles, captions and effects with the relit base swapped in. Nothing else changes.
11. **Compare frame by frame** with the approved edit at every caption and title time, then have a second checker go through the list below.

## Checks before calling it done

- Cuts land on the source frames, within one frame.
- Lips stay in sync for the whole clip, watched at full speed.
- Inside a shot, no frame-to-frame brightness jump on the face above about 5 (out of 255). The first version hit 20 and visibly flickered.
- One room across every angle; no grey backdrop, ghost furniture or changed angle.
- The face is the brightest thing on screen; the room is never sharper or brighter than the face.
- The face still looks like the person, skin colour unchanged.

## Filming so the relight works

- Light the hair and the edge of the head, and sit about a metre from the wall. A clean edge sells it.
- Aim for the face around 150 of 255 in brightness, a bright hair edge, and the wall about half as bright as the face.
- Dark, plain tops work best.
