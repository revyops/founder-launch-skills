import cv2, numpy as np, subprocess, sys
# facelift.py in.mp4 out.mp4 [strength]
# Soft face key (brighter, warmer, a bit more colour), face only. Two passes so it never flickers:
# 1) find the face in every frame, split into shots at cuts, fill gaps and smooth the box inside each shot;
# 2) apply a steady light. A shot where the face is found in under 40% of frames gets no light at all.
inp,outp=sys.argv[1],sys.argv[2]; S=float(sys.argv[3]) if len(sys.argv)>3 else 1.0
W,H=1080,1920
casc=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
prof=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_profileface.xml')
def frames():
    p=subprocess.Popen(['ffmpeg','-v','error','-i',inp,'-vf',f'fps=30,scale={W}:{H}:flags=lanczos','-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
    while True:
        b=p.stdout.read(W*H*3)
        if len(b)<W*H*3: return
        yield np.frombuffer(b,np.uint8).reshape(H,W,3)
boxes=[];cuts=[0];prev=None
for i,f in enumerate(frames()):
    s=cv2.resize(f,(W//4,H//4)); g=cv2.cvtColor(s,cv2.COLOR_BGR2GRAY)
    if prev is not None and np.abs(s.astype(np.int16)-prev).mean()>28: cuts.append(i)
    prev=s.astype(np.int16)
    d=list(casc.detectMultiScale(g,1.1,5,minSize=(40,40)))
    if not d:
        d=list(prof.detectMultiScale(g,1.1,4,minSize=(40,40)))+[(W//4-x-w,y,w,h) for (x,y,w,h) in prof.detectMultiScale(cv2.flip(g,1),1.1,4,minSize=(40,40))]
    boxes.append(np.array(max(d,key=lambda r:r[2]*r[3]),np.float32)*4 if d else None)
n=len(boxes); cuts.append(n); final=[None]*n
for a,b in zip(cuts[:-1],cuts[1:]):
    idx=[i for i in range(a,b) if boxes[i] is not None]
    if len(idx) < 0.4*(b-a): continue
    arr=np.array([boxes[i] for i in idx])
    med=np.median(arr,axis=0); keep=[k for k,i in enumerate(idx) if np.abs(arr[k]-med).max()<med[2]*0.6]
    idx=[idx[k] for k in keep]; arr=arr[keep]
    full=np.stack([np.interp(np.arange(a,b),idx,arr[:,j]) for j in range(4)],1)
    k=np.ones(15)/15; pad=np.pad(full,((7,7),(0,0)),mode='edge')
    sm=np.stack([np.convolve(pad[:,j],k,'valid') for j in range(4)],1)
    for t in range(a,b): final[t]=sm[t-a]
print('frames',n,'cuts',cuts,'lit',sum(x is not None for x in final))
wr=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','30','-i','-','-c:v','libx264','-crf','16','-pix_fmt','yuv420p',outp],stdin=subprocess.PIPE)
yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
for i,f in enumerate(frames()):
    out=f.astype(np.float32)/255
    if final[i] is not None:
        x,y,w,h=final[i]; cx,cy=x+w/2,y+h*0.55; rx,ry=w*0.85,h*1.05
        m=np.exp(-(((xx-cx)/rx)**2+((yy-cy)/ry)**2)*1.6)[...,None]*S
        lifted=out*1.22+0.015
        lifted=lifted*np.array([0.97,1.0,1.06])
        gray=lifted.mean(axis=2,keepdims=True); lifted=gray+(lifted-gray)*1.15
        lifted=np.minimum(lifted,out+0.25)
        out=out*(1-m)+np.clip(lifted,0,1)*m
    wr.stdin.write((np.clip(out,0,1)*255).astype(np.uint8).tobytes())
wr.stdin.close(); wr.wait()
