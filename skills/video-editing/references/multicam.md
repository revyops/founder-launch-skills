# Multi-camera talking head (front camera plus side angles)

Use this for a vertical video cut from a front camera and one or two side cameras. Placement numbers are in `framing.md`.

## Start here

1. Build the cut from a plan and run a gate before any render (see `lessons.md`, section 6).
2. Treat the first edit as a template. Keep the scripts that worked and change only the per-video values.
3. The speaker gets one version, after up to two full review rounds and a spot check.

## Choosing and cutting angles

- **The front camera is home.** Open on it, talking. A side camera that shows the back of the head is worse than a close front shot.
- **Side shots are visits of 3 to 4 seconds** ("one Mississippi, two, three"), then back. Front shots run about 4 to 7 seconds. Never hold a side angle 7 to 10 seconds. Never leave the front camera still: push in, pull out, step in on a strong line, change zoom at every jump cut.
- **Switch angles on a new thought.** Use the side angle for emotional lines and an over-the-shoulder angle when the talk is about the screen or the work. Never the same angle twice in a row.
- **Only talking shots.** Never show the speaker not talking, except in named bloopers and B-roll.
- **Use a side angle only where the hands are down.** Hands cross a side lens often. Check each side shot for a hand over the lens, even for half a second.
- **The face is centred in every side shot.** Find the face in each shot (not one fixed spot for the whole video), frame it medium with eyes about 31% down, and check a phone-size still of each. The face is never cut off outside the bloopers. Never go outside the frame.
- **Move the front face up** about 20 px when it sits low in the raw frame.
- **B-roll plays where the speaker names it** (full frame, about 3 s) and ends on that sentence's full stop, so the face is back for the next line.
- **Bloopers at the end:** tease them early with a card, label the reel, cut pauses short, use a new angle each take. Walking in or out of frame is part of the joke, so do not cut a take for that. The label sits on a take where the eyes are below the card, for about 2.5 s.
- **Colour:** do not colour-match side cameras with your own LUTs. It made skin look red. Fix differences at the shoot (below).

## Sync and file checks

- Line the cameras up from their sound and one clap. A weak sync score (under about 2 times) means a wrong file: stop and ask.
- **Check every file by byte size, length and date, not by name.** Two blind rebuilds used an old clip because of its name. A file that syncs weakly is the clue.
- **The offset sign flips.** If the sync tool says a camera is 40 s early, the source offset in your script is plus 40 s. A first cut came out 80 s off for this reason. Check one still per angle at the same spoken line before going on.
- Confirm sync by eye: lips and the clap line up in every angle.

## Filming (a fix in the camera beats a fix in the edit)

- Film the same on every camera: 4K, 29.97 fps (called "30" on most cameras. 30 and 29.97 drift about 0.6 s over a 10-minute take), the standard colour profile (not log), white balance locked at the same Kelvin on every camera (5500 K worked, since an action camera steps in 500 K), exposure locked, shutter 1/60. Never auto white balance.
- Turn HDR off on a phone side camera, or film in a manual camera app with a standard colour profile. Hold the phone upright for a vertical shoot, and film 3 s to check the file size and rotation tag.
- Record each camera to its own card. A USB recording into an editing app can be a scaled-up 720p file.
- Set every light to the same colour temperature. No daylight from one side only. No light stand or monitor in any angle.
- Hold a grey or white card in front of each lens at the clap. Film 10 seconds on all cameras and compare stills side by side before the real shoot.
- Do one clap that all cameras see. Before each story say "Card 4." and pause two seconds, so the edit can find each story in one long file. If you fluff a line, pause and say it again. Never stop the cameras.
- Lenses at eye level, never looking up (a low phone showed the ceiling). Use the long end (a 2x or 3x lens, or the main camera at 35 to 50 mm and moved back). Keep hands below the side lens. Leave a little room around the head, since the edit crops to the standard.
- **Light check, three numbers:** face about 150 of 255 (cheeks and forehead). A thin bright line on the hair and shoulders from a back light. A wall about half as bright as the face (about 60 to 90 of 255), never black. Get light first (the key 2 to 3 feet from the face), then raise ISO. A black or charcoal shirt vanishes into a dark room, so wear a mid-tone.
- Three lights, no more: key at 45 degrees and a little above the eyes, a back or hair light, and one or two small coloured lights washing the wall. No fill. Turn off overhead lights.
- **If the footage is dark, flat or the face melts into the wall, say so and ask for a refilm.** No edit fixes it. Cut-outs, depth words and room swaps all fail on dark footage.
- Check light on one still per angle before you cut.

## The editor's 18-line checklist (talking head)

Tick each line with proof.

1. Restarts and double takes found from the audio, last clean take kept.
2. No doubled word at a join.
3. No "So" or "Now" opener that adds nothing.
4. Ums, uhs and stutters out, each cut in quiet.
5. Pauses over 0.24 s inside a line shrunk to 0.14 s. No long silence outside the bloopers. Joins 0.20 s or less for lines filmed one at a time.
6. No clipped word ends.
7. Every swear bleeped.
8. Colour passed through. No grade.
9. Lanczos scaling, low zoom, high-quality intermediates.
10. Face in frame and centred in every shot (bloopers excepted).
11. Only talking shots (bloopers and named B-roll excepted).
12. Title on the forehead, big, centred, top at y 400 or lower.
13. Labels and arrows centred, arrows pointing at the head, 110 px from the side edges.
14. Cards and title boxes centred and big enough to read on a phone, never at an edge, never over the eyes. They fade in.
15. Captions two or three words, names right, on one fixed line 55 to 61% down.
16. Music: the approved bed, low under the voice, never restarted. A little up in bloopers and on the end card.
17. The brand's end card, if the video is not a Short.
18. Voice about -14 LUFS, true peak below -1 dB.

## What a three-version review taught

The first versions were rejected for: restarts left in, red skin from our own colour match, a title too high, side angles held too long, no zoom movement, a low face, off-centre side shots, "So" and "now" openers, doubled lines, clipped word ends, a face cut off, and showing the speaker not talking. Almost all of these are mechanical. A script finds them in seconds. That is why the gate exists.
