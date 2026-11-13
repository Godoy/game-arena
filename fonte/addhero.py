# addhero.py key blob-suffix meta-json [ax ay h]
import sys,json,glob,numpy as np
from PIL import Image
k,suf,m=sys.argv[1],sys.argv[2],json.loads(sys.argv[3])
f=glob.glob('/tmp/claude-tool-results/*/*'+suf+'*')[0]
a=Image.open(f).convert('RGBA');print(a.size)
al=np.array(a.crop((0,0,m['fw'],m['fh'])))[...,3]>60;ys,xs=np.where(al);print('idle bbox x',xs.min(),xs.max(),'y',ys.min(),ys.max(),'cx',round(xs.mean(),1))
if len(sys.argv)>4:m['ax'],m['ay'],m['h']=map(float,sys.argv[4:7])
a.quantize(255,method=2,dither=0).save('anim_final/%s.png'%k,optimize=True);json.dump(m,open('anim_final/%s.json'%k,'w'));print(m)
