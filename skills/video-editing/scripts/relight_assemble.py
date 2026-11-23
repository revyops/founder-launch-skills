"""Join Higgsfield relit parts back into a base the same length as your locked base clip.
Each piece: (file, start seconds inside that file, number of 30 fps frames it must fill).
Retime to 30 fps, upscale to 1080x1920 (lanczos + light sharpen), take exactly N frames,
hold the last frame if the part came back a frame or two short. Output: relit_base_raw.mp4.
Usage: python relight_assemble.py pieces.json out.mp4
"""
import json, subprocess, sys, os, tempfile
pieces = json.load(open(sys.argv[1])); out = sys.argv[2]
tmp = tempfile.mkdtemp()
parts = []
for i, (f, ss, n) in enumerate(pieces):
    o = os.path.join(tmp, f"p{i}.mp4")
    vf = (f"fps=30,trim=start={ss},setpts=PTS-STARTPTS,"
          f"scale=1080:1920:flags=lanczos,unsharp=5:5:0.4,tpad=stop_mode=clone:stop=30,"
          f"trim=end_frame={n},setpts=N/30/TB")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-vf", vf, "-an", "-r", "30",
                    "-c:v", "libx264", "-crf", "12", "-pix_fmt", "yuv420p", o], check=True)
    got = int(subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v",
                              "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", o],
                             capture_output=True, text=True).stdout.strip())
    src_frames = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                       "-of", "csv=p=0", f], capture_output=True, text=True).stdout) * 30 - ss * 30
    print(f"piece {i}: {os.path.basename(f)} from {ss}s -> {got}/{n} frames (source had {src_frames:.1f}, held {max(0, n - round(src_frames))})")
    assert got == n, "frame count wrong"
    parts.append(o)
lst = os.path.join(tmp, "list.txt")
open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", out], check=True)
tot = subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v",
                      "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", out],
                     capture_output=True, text=True).stdout.strip()
print("total frames", tot, "(should equal the base clip frame count)")
