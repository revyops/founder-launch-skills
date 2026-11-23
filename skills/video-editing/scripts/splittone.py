"""Split-tone one frame range so a shot left outside the new room sits with the room:
shadows toward the room's blue, highlights a little warmer, ramped in/out over 0 frames (hard cut shot).
Usage: python splittone.py in.mp4 out.mp4 first last"""
import cv2, numpy as np, subprocess, sys
inp, outp, a, b = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); W, H = 1080, 1920
r = subprocess.Popen(["ffmpeg","-v","error","-i",inp,"-f","rawvideo","-pix_fmt","bgr24","-"], stdout=subprocess.PIPE)
w = subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","bgr24","-s",f"{W}x{H}","-r","30","-i","-",
                      "-c:v","libx264","-crf","12","-pix_fmt","yuv420p",outp], stdin=subprocess.PIPE)
blue = np.array([0.55, 0.22, 0.05], np.float32)   # BGR push for shadows (set this to your room's shadow colour)
warm = np.array([-0.04, 0.02, 0.07], np.float32)  # BGR push for highlights
n = 0
while True:
    buf = r.stdout.read(W*H*3)
    if len(buf) < W*H*3: break
    f = np.frombuffer(buf, np.uint8).reshape(H, W, 3)
    if a <= n <= b:
        x = f.astype(np.float32) / 255; L = x.mean(2, keepdims=True)
        sh = np.clip(1 - L / 0.45, 0, 1) ** 1.5; hi = np.clip((L - 0.45) / 0.55, 0, 1)
        x = x * (1 - 0.25 * sh) + sh * blue * 0.18 + hi * warm
        f = (np.clip(x, 0, 1) * 255).astype(np.uint8)
    w.stdin.write(f.tobytes()); n += 1
w.stdin.close(); w.wait(); print("frames", n)
