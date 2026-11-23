# Relight: put the speaker in a better room

This is how a plain phone clip gets a new room and studio light on the face (the "before and after" look). It is the last step, after the edit is locked.

## What you need

- A locked edit with no captions or titles on it (`base.mp4`, 1080x1920, no sound).
- An AI video relighting tool that can change the location and relight the person. We use Higgsfield's Editing Room, "Change location". Any tool that relights the person to the new room works. A tool that only swaps the background looks pasted on.
- Python with `opencv-python` and `numpy`, plus ffmpeg, for the two scripts in `scripts/`.

## Why not a colour grade

The better colour comes from relighting the person to match a better room. A LUT or grade on the camera file cannot add light that was never there, and it shifts skin colour. Never grade the face.

## Steps

1. **Lock the edit.** Cuts, captions and sound approved. Relight the clean base, never the final with titles on it.
2. **Make the room once.** Generate one empty studio picture (9:16) and reuse it in every video, so your videos share one set. Describe the layers: back wall, shelves, practical lights, haze, a rim light. A prompt that only says "office" gives a flat, video-call look.
3. **Test 6 to 8 seconds** that cross every camera angle and at least two cuts. Check: one room across angles, colour on the face, no holes or white patches, the face still looks like the person. Approve the test before the full run.
4. **Run the full clip in parts of 30 seconds or less,** split on a cut, with the same reference picture and the same prompt word for word. Name the light on the person in the prompt (warm on one cheek, cool on the other, a bright hair and shoulder rim) and the motion in the room (haze, pulsing neon).
5. **Put the cuts back on the source frames.** Relighting tools often return 24 fps and move each cut 2 to 3 frames late, so lips drift. Run:
   `python scripts/relight_align.py base.mp4 relit.mp4 aligned.mp4`
   It finds each shot, measures the lip lag and writes a clip with the source's exact frame count.
6. **Lift the face.** Relit faces often come back a little dark and grey. Run:
   `python scripts/facelift.py aligned.mp4 lit.mp4`
   It adds a soft, face-only light (about a third of a stop, a little warmer). It tracks the face in two passes so the light never flickers, and skips any shot where it cannot find the face reliably.
7. **Check every shot against the source,** one frame each. Common faults: a shot left on a plain grey backdrop, a see-through desk, a side angle turned into a front view, a part framed wider than the source. Redo with the fault named in the prompt. After two failed redos of one shot, keep the original shot.
8. **Put the titles and captions back on** over the relit clip, then compare frame by frame with the approved edit.

## Checks before calling it done

- Cuts land on the same frames as the source (within one frame).
- Lips stay in sync across the whole clip.
- No frame-to-frame brightness jump on the face inside a shot.
- The room is never sharper or brighter than the face.
