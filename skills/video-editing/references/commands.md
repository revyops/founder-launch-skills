# Commands and helpers

All paths assume you are inside `work/<clip>/` and the original is `../../clip.mov`. Replace names. Use `python3 -I` only for scripts that read untrusted files you did not write; the scripts below are safe to run normally.

## 1. Inspect

```bash
ffprobe -v error -show_entries stream=index,codec_type,codec_name,width,height,r_frame_rate:stream_side_data=rotation:format=duration -of default=nw=1 ../../clip.mov
```

A still to see the real orientation:

```bash
ffmpeg -y -ss 1 -i ../../clip.mov -frames:v 1 still_src.png
```

## 2. Transcribe with word timestamps

Whisper tidies filler words away unless the prompt contains them. Use this prompt to keep them:

```bash
ffmpeg -y -i ../../clip.mov -vn -ac 1 -ar 16000 audio.wav

whisper audio.wav --model small.en --language en \
  --word_timestamps True --output_format json --output_dir . \
  --initial_prompt "Um, uh, so, you know, I, I was, like, er, the, uh, the thing is."
```

Use `--model medium.en` for a harder recording. The result is `audio.json`: `segments[].words[]` with `word`, `start`, `end`. Also write the plain text and read all of it:

```bash
python3 - <<'PY'
import json
d = json.load(open("audio.json"))
for s in d["segments"]:
    print(f'{s["start"]:7.2f}  {s["text"].strip()}')
PY
```

whisper.cpp alternative: `whisper-cli -m models/ggml-small.en.bin -f audio.wav -ojf -ml 1 --prompt "Um, uh, so, you know"` gives word-level JSON. The helper scripts below expect the openai-whisper shape, so convert if you use it.

## 3. Find the quiet gaps

```bash
ffmpeg -i audio.wav -af silencedetect=noise=-35dB:d=0.2 -f null - 2> silence.log
```

If speech is quiet or the room is noisy, try `-30dB` or `-40dB`. Each gap shows as `silence_start`, `silence_end` lines in `silence.log`.

## 4. Choose cuts and snap the edges to gaps

Write `keep.json` by hand as source seconds taken from the transcript, for example:

```json
[[2.10, 9.80], [12.45, 20.30], [31.00, 44.60]]
```

Each pair is the first word's start and the last word's end of a whole thought. Then snap the edges to the silences:

```python
# snap.py  -  python3 snap.py keep.json silence.log > keep_snapped.json
import json, re, sys

keep = json.load(open(sys.argv[1]))
log = open(sys.argv[2]).read()
starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
gaps = list(zip(starts, ends))          # (gap_start, gap_end)

AFTER, BEFORE, WINDOW = 0.15, 0.12, 0.45

def snap_start(t):
    # the gap that ends nearest to t: the piece starts just after it ends
    cands = [(abs(e - t), g) for g in gaps for e in [g[1]] if abs(e - t) <= WINDOW]
    if not cands:
        return max(0.0, t - BEFORE)
    g = min(cands)[1]
    return max(g[0], g[1] - BEFORE)       # BEFORE seconds of quiet, never before the gap opens

def snap_end(t):
    # the gap that starts nearest to t: the piece ends just after speech stops
    cands = [(abs(s - t), g) for g in gaps for s in [g[0]] if abs(s - t) <= WINDOW]
    if not cands:
        return t + AFTER
    g = min(cands)[1]
    return min(g[1], g[0] + AFTER)        # AFTER seconds of quiet, never past the gap's end

out = [[round(snap_start(a), 3), round(snap_end(b), 3)] for a, b in keep]
json.dump(out, sys.stdout)
```

Print the gaps between pieces (`next_start - prev_end` in the output timeline is the join beat, which is simply the sum of the two padding values, about 0.27 s) and list any piece shorter than 1 second. Show the user the planned cuts as text before rendering.

## 5. Cut, join, crop, normalise in one pass

Generate the filter graph from the keep list. One pass keeps audio and video the same length.

```python
# build_cut.py  -  python3 build_cut.py keep_snapped.json > cut.sh
import json, sys

keep = json.load(open(sys.argv[1]))
SRC = "../../clip.mov"
FPS = 30

v, a, labels = [], [], []
for i, (s, e) in enumerate(keep):
    v.append(f"[0:v]trim=start={s}:end={e},setpts=PTS-STARTPTS[v{i}]")
    a.append(f"[0:a]atrim=start={s}:end={e},asetpts=PTS-STARTPTS,"
             f"afade=t=in:d=0.01,afade=t=out:st={max(0,e-s-0.01):.3f}:d=0.01[a{i}]")
    labels.append(f"[v{i}][a{i}]")
n = len(keep)
chain = ";".join(v + a) + ";" + "".join(labels) + f"concat=n={n}:v=1:a=1[vj][aj]"
# 9:16 crop from the centre (change x to move the crop toward the face), then scale
chain += (";[vj]crop=w='trunc(ih*9/16/2)*2':h=ih:x='(iw-out_w)/2':y=0,"
          f"scale=1080:1920:flags=lanczos,fps={FPS},setsar=1[vout]")
chain += ";[aj]loudnorm=I=-14:TP=-1.5:LRA=11[aout]"

print(f"""#!/bin/sh
ffmpeg -y -i {SRC} -filter_complex "{chain}" -map "[vout]" -map "[aout]" \\
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p \\
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart cut.mp4""")
```

Run `sh cut.sh`. Notes:

- The 10 ms fades on every piece edge stop clicks.
- If the phone clip is already vertical, remove the `crop` step and keep the `scale`. If it is vertical but not exactly 9:16, use `scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920`.
- For a face that is not centred, set `x` to a number: `x=300` is 300 px from the left of the source frame. Check a still.
- For a long keep list the graph is long but fine. If ffmpeg complains about the command line, write the graph to a file and use `-filter_complex_script graph.txt`.
- A lifted hook is just a keep pair placed first in the list. Do not repeat it later unless the user wants the line twice.
- Two-pass loudness: if the level matters, run `loudnorm` once with `print_format=json` to measure, then pass `measured_I`, `measured_TP`, `measured_LRA`, `measured_thresh` back in. Single pass is fine for a social clip.

## 6. Re-transcribe the cut to get caption timing

```bash
ffmpeg -y -i cut.mp4 -vn -ac 1 -ar 16000 cut.wav
whisper cut.wav --model small.en --language en --word_timestamps True \
  --output_format json --output_dir . \
  --initial_prompt "Um, uh, so, you know, I, I was, like, er, the, uh, the thing is."
```

This gives `cut.json`, with word times on the final timeline. Read the plain text. Any leftover filler or repeated word means a cut is missing: fix `keep.json` and go back to step 5.

For the captions themselves, transcribe once more without the filler prompt so the words read cleanly, and use that file as `captions_src.json`.

## 7. Build the .ass file: captions and hook title

The ASS format gives exact control of font, outline, box and margin. This script groups words into 1 to 3 word captions, folds single-word captions, and adds the hook title for the first seconds.

```python
# make_ass.py  -  python3 make_ass.py captions_src.json "I stopped sending weekly reports" 3.0 > captions.ass
import json, sys

src, TITLE, TITLE_SECS = sys.argv[1], sys.argv[2], float(sys.argv[3])
words = []
for seg in json.load(open(src))["segments"]:
    for w in seg["words"]:
        t = w["word"].strip()
        if t:
            words.append((t, w["start"], w["end"]))

# group into captions of 1-3 words; break after punctuation or a pause
groups, cur = [], []
for i, (t, s, e) in enumerate(words):
    cur.append((t, s, e))
    nxt_gap = (words[i + 1][1] - e) if i + 1 < len(words) else 9
    if len(cur) == 3 or t[-1] in ".,?!;:" or nxt_gap > 0.35:
        groups.append(cur); cur = []
if cur:
    groups.append(cur)

# fold single-word captions into the previous one (max 4 words)
merged = []
for g in groups:
    if len(g) == 1 and merged and len(merged[-1]) < 4:
        merged[-1] += g
    else:
        merged.append(g)

def ts(x):
    x = max(0.0, x)
    h, m, s = int(x // 3600), int(x % 3600 // 60), x % 60
    return f"{h}:{m:02d}:{s:05.2f}"

lines = []
for g in merged:
    text = " ".join(t for t, _, _ in g).replace(" %", "%")
    start, end = g[0][1], g[-1][2]
    lines.append(f"Dialogue: 0,{ts(start)},{ts(end + 0.05)},Cap,,0,0,0,,{text}")

title = TITLE.replace("\\", "").replace("{", "").replace("}", "")
lines.insert(0, f"Dialogue: 1,{ts(0)},{ts(TITLE_SECS)},Title,,0,0,0,,{title}")

header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Cap,Montserrat ExtraBold,84,&H00FFFFFF,&H000000FF,&H00000000,&H90000000,0,0,0,0,100,100,0,0,1,5,3,2,130,130,520,1
Style: Title,Montserrat ExtraBold,92,&H00202020,&H000000FF,&H00FFFFFF,&H00000000,0,0,0,0,100,100,0,0,3,22,0,8,130,130,360,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""
print(header + "\n".join(lines))
```

What the styles mean:

- **Cap:** white text, black outline 5 px, soft shadow 3 px. Alignment 2 is bottom centre. `MarginV` 520 puts the text's bottom edge 520 px up from the bottom, inside the safe zone (the bottom no-go zone starts 480 px up). Side margins 130 px.
- **Title:** `BorderStyle 3` draws an opaque box, using the outline colour as the box colour. Dark text on a white box. Alignment 8 is top centre, `MarginV` 360 puts it below the top no-go zone. Move it so it clears the face: check a still.
- For a caption box over a busy page, make a third style like `Cap` with `BorderStyle 3`, `OutlineColour` the box colour (white `&H00FFFFFF` or dark `&H00202020`) and `Outline 14`, and set `PrimaryColour` to the contrasting text colour.
- Colours are `&HAABBGGRR` (blue, green, red order). `&H00FFFFFF` is white, `&H00000000` black.
- The `Fontname` must match the font's family name. Check it with `fc-scan fonts/Montserrat-ExtraBold.ttf | grep family`. If the family is "Montserrat" and the weight is ExtraBold, use `Fontname Montserrat` and `Bold 1`, or use "Montserrat ExtraBold" if that is the family name listed.
- Font size 84 on a 1920-high frame is big enough to read on a phone. Drop to 76 if a three-word caption exceeds the side margins.

Manual line breaks in the title use `\N`: `"I stopped sending\Nweekly reports"`. Keep a title to two lines.

## 8. Burn the captions

```bash
ffmpeg -y -i cut.mp4 -vf "ass=captions.ass:fontsdir=fonts" \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -c:a copy -movflags +faststart final_9x16.mp4
```

The video is encoded twice in total (once in the cut, once here). That is fine. To avoid it, put the `ass=` filter at the end of the filter graph in step 5 and render once, after building the captions from a draft cut.

## 9. Preview under 30 MB

```bash
ffmpeg -y -i final_9x16.mp4 -vf scale=720:1280 -c:v libx264 -preset medium -crf 26 \
  -c:a aac -b:a 128k -movflags +faststart final_preview.mp4
ls -l final_preview.mp4
```

Raise `-crf` if it is over 30 MB.

## 10. The checks

Zones image (red is the no-go area):

```bash
ffmpeg -y -ss 1.5 -i final_9x16.mp4 -frames:v 1 -vf \
"drawbox=x=0:y=0:w=iw:h=ih*0.13:color=red@0.35:t=fill,\
drawbox=x=0:y=ih*0.75:w=iw:h=ih*0.25:color=red@0.35:t=fill,\
drawbox=x=0:y=0:w=iw*0.12:h=ih:color=red@0.35:t=fill,\
drawbox=x=iw*0.88:y=0:w=iw*0.12:h=ih:color=red@0.35:t=fill" zones.png
```

Look at `zones.png`. Title and captions should sit in the clear area. Make one at the title time (`-ss 1.5`), one at a caption time, and one near the end.

Stills at key moments:

```bash
for t in 0.3 3.5 10 20; do ffmpeg -y -ss $t -i final_9x16.mp4 -frames:v 1 still_$t.png; done
ffmpeg -y -sseof -0.5 -i final_9x16.mp4 -frames:v 1 still_end.png
```

Black frames and silence at the edges:

```bash
ffmpeg -i final_9x16.mp4 -vf blackdetect=d=0.1:pix_th=0.1 -an -f null - 2>&1 | grep black
ffmpeg -i final_9x16.mp4 -af silencedetect=noise=-40dB:d=0.4 -f null - 2>&1 | grep silence
```

Loudness:

```bash
ffmpeg -i final_9x16.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -n 12
```

Integrated loudness should read near -14 LUFS, and true peak below -1 dBTP.

Re-transcribe the output both ways (with the filler prompt, then without) and read both.

Final facts:

```bash
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate:format=duration -of default=nw=1 final_9x16.mp4
```

Expect 1080 by 1920, 30 fps, an audio stream, and the length you planned.

## 11. Landscape YouTube clip

Skip the crop: replace the crop and scale step in the filter graph with `scale=1920:1080:flags=lanczos`. Use a PlayRes of 1920 by 1080 in the ASS header, caption font size around 60, bottom margin about 140, side margins about 200. Keep text out of the bottom 10% where the player controls sit.

## 12. Troubleshooting

- `Unknown filter 'ass'`: this ffmpeg has no libass. Install a full build (`brew install ffmpeg-full`, or a static build) and check with `ffmpeg -filters | grep -w ass`.
- Captions show the wrong font: the font file is missing or the family name differs. Check `fc-scan`, and point `fontsdir` at the folder that holds the `.ttf`.
- Audio drifts from video: do not cut pieces separately and join them with stream copy. Use the single-pass graph above.
- Captions are late or early: build them from a transcript of the cut file, not the original.
- Words clipped at a cut: the gap was too small. Widen the padding for that edge or move the edge into a longer gap.
- Whisper missed fillers: they were removed from the text but still sound in the audio. Re-run with the filler prompt and cross-check with `silencedetect` energy before cutting.
- The crop cuts off the face: change `x` in the crop and check a still.

## 13. More checks

Cover safe box (1080x1920 cover, the words must stay inside the clear area; red is the no-go area):

```bash
ffmpeg -y -i cover.png -vf "drawbox=x=0:y=0:w=iw:h=340:color=red@0.35:t=fill,\
drawbox=x=0:y=1500:w=iw:h=420:color=red@0.35:t=fill,\
drawbox=x=0:y=0:w=110:h=ih:color=red@0.35:t=fill,\
drawbox=x=970:y=0:w=110:h=ih:color=red@0.35:t=fill" cover_zones.png
```

Crops of the profile grid (3:4) and feed (4:5) views of a 1080x1920 cover, and a 420 px wide feed-size copy:

```bash
ffmpeg -y -i cover.png -vf crop=1080:1440:0:240 cover_grid.png
ffmpeg -y -i cover.png -vf crop=1080:1350:0:285 cover_feed.png
ffmpeg -y -i cover.png -vf scale=420:-1 cover_420.png
```

Join gaps on the finished cut (each gap should be about 0.1 to 0.25 s, and none over 0.25 s for lines filmed one at a time):

```bash
ffmpeg -i cut.mp4 -af silencedetect=noise=-40dB:d=0.08 -f null - 2>&1 | grep -E "silence_(start|end|duration)"
```

Audio and video must be the same length, or captions drift:

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=duration -of csv=p=0 final_9x16.mp4
ffprobe -v error -select_streams a:0 -show_entries stream=duration -of csv=p=0 final_9x16.mp4
```

Check each camera file before a multi-camera cut. The real frame rate (29.97 and 30 drift apart), size, rotation and length:

```bash
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate:stream_side_data=rotation:format=duration:format=size -of default=nw=1 file.mov
```

Hold the last frame 0.4 s and end the audio exactly with the video (holds the last picture, and pads the audio with silence so both end together):

```bash
ffmpeg -y -i final_9x16.mp4 -vf tpad=stop_mode=clone:stop_duration=0.4 -af apad -shortest -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart final_held.mp4
```

Only use that last one as part of the single render. Do not re-encode a finished final.

A 540p preview (about 4 MB for a Short) when storage or a page is full:

```bash
ffmpeg -y -i final_9x16.mp4 -vf scale=540:960 -c:v libx264 -preset medium -crf 30 -c:a aac -b:a 96k -movflags +faststart final_540.mp4
```
