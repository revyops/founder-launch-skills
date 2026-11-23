"""Put a Higgsfield relit part back on the source's exact frames.
Higgsfield returns 24 fps and can move a cut by 2-3 frames. For each shot of the source
(30 fps, cuts found by frame difference) this finds the same shot in the relit clip,
measures the lag of the motion inside the shot (so lips stay in sync), and builds a
30 fps 1080x1920 clip with exactly the source's frame count and cuts on the source's frames.
Usage: python relight_align.py source.mp4 relit.mp4 out.mp4
"""
import cv2, numpy as np, subprocess, sys
src_p, rel_p, out_p = sys.argv[1:4]
W, H = 1080, 1920

def load(p, size):
    cap = cv2.VideoCapture(p); fps = cap.get(5); fr = []
    while True:
        ok, im = cap.read()
        if not ok: break
        fr.append(im if size is None else cv2.resize(im, size))
    return fps, fr

sfps, ssmall = load(src_p, (90, 160))
rfps, rfull = load(rel_p, None)
rsmall = [cv2.resize(f, (90, 160)) for f in rfull]

def diffs(fr):
    return np.array([0] + [np.abs(fr[i].astype(np.int16) - fr[i - 1]).mean() for i in range(1, len(fr))])

def cuts(d, fps):
    return [i / fps for i in range(1, len(d)) if d[i] > 20 and d[i] > 4 * np.median(d[max(1, i - 6):i + 6])]

sd, rd = diffs(ssmall), diffs(rsmall)
sc, rc = cuts(sd, sfps), cuts(rd, rfps)
sdur, rdur = len(ssmall) / sfps, len(rsmall) / rfps
pairs = []
for t in sc:
    near = [r for r in rc if abs(r - t) < 0.25]
    if not near: sys.exit(f"no relit cut near source cut {t:.3f}  (relit cuts {rc})")
    pairs.append((t, min(near, key=lambda r: abs(r - t))))
bounds = [(0.0, 0.0)] + pairs + [(sdur, rdur)]

# motion signal (centre of frame, where the person is) on a fine common grid
def motion(fr):
    c = [f[30:150, 15:75].astype(np.int16) for f in fr]
    return np.array([0] + [np.abs(c[i] - c[i - 1]).mean() for i in range(1, len(c))])
sm, rm = motion(ssmall), motion(rsmall)

n_out = len(ssmall); src_t = np.arange(n_out) / sfps; rel_t = np.zeros(n_out)
report = []
for (s0, r0), (s1, r1) in zip(bounds[:-1], bounds[1:]):
    grid = np.arange(s0 + 0.1, s1 - 0.1, 1 / 120)
    best = s0 - r0; conf = float('nan')
    if len(grid) > 24:
        a = np.interp(grid, np.arange(len(sm)) / sfps, sm)
        lags = np.arange(-0.17, 0.171, 1 / 120); sc_ = []
        for L in lags:
            b = np.interp(grid - s0 + r0 + L, np.arange(len(rm)) / rfps, rm)
            sc_.append(np.corrcoef(a, b)[0, 1] if a.std() > 0 and b.std() > 0 else -1)
        k = int(np.argmax(sc_)); best = lags[k] if sc_[k] >= 0.6 else (s0 - r0)   # weak match: keep the source's own timing (Higgsfield keeps content in time and only moves the cut)
        conf = sc_[k]
    idx = (src_t >= s0) & (src_t < s1)
    # relit time for each source frame: same offset into the shot, plus the measured lag,
    # kept inside the relit shot so a cut never shows the wrong camera
    t = src_t[idx] - s0 + r0 + best
    rel_t[idx] = np.clip(t, r0, r1 - 1 / rfps)
    report.append(f"shot {s0:6.3f}-{s1:6.3f}s  relit {r0:6.3f}-{r1:6.3f}s  lag {best*1000:+.0f} ms (match {conf:.2f})")
print("\n".join(report))

wr = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", "30",
                       "-i", "-", "-vf", "unsharp=5:5:0.4", "-c:v", "libx264", "-crf", "12", "-pix_fmt", "yuv420p", out_p],
                      stdin=subprocess.PIPE)
for t in rel_t:
    i = min(int(round(t * rfps)), len(rfull) - 1)
    wr.stdin.write(cv2.resize(rfull[i], (W, H), interpolation=cv2.INTER_LANCZOS4).tobytes())
wr.stdin.close(); wr.wait()
print(f"wrote {out_p}: {n_out} frames (source {len(ssmall)})")
