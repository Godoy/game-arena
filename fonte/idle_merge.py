# idle_merge.py: integra o que veio do Higgsfield em idle_in/ (meta.txt + <chave>.png de parado; m3_all.png = golem refeito).
# Parado: gera anim_final/<chave>i.png/.json (12 quadros em laço), ancorado pela pose do quadro 0, igual à do atlas principal.
import os,json,re,numpy as np
from PIL import Image
if not os.path.exists('idle_in/meta.txt'):raise SystemExit
def bbox(a):
    ys,xs=np.where(a>60);return xs.min(),xs.max(),ys.min(),ys.max()
for line in open('idle_in/meta.txt',encoding='utf-8'):
    mm=re.match(r'\s*(IDLE|META)\s+(\w+)\s+(\{.*\})',line)
    if not mm:continue
    kind,k,m=mm.group(1),mm.group(2),json.loads(mm.group(3))
    if kind=='META':
        f='idle_in/%s_all.png'%k
        if os.path.exists(f):
            Image.open(f).convert('RGBA').quantize(255,method=2,dither=0).save('anim_final/%s.png'%k,optimize=True);json.dump(m,open('anim_final/%s.json'%k,'w'));print('atlas trocado',k)
        continue
    f='idle_in/%s.png'%k
    if not os.path.exists(f) or not os.path.exists('anim_final/%s.json'%k):continue
    M=json.load(open('anim_final/%s.json'%k));A=np.array(Image.open('anim_final/%s.png'%k).convert('RGBA'))
    S=Image.open(f).convert('RGBA');s=np.array(S);fw,fh=m['fw'],m['fh']
    x0,x1,y0,y1=bbox(s[:fh,:fw,3]);X0,X1,Y0,Y1=bbox(A[:M['fh'],:M['fw'],3])
    r=(Y1-Y0)/(y1-y0)
    o=Image.new('RGBA',(fw*6,fh*2),(0,0,0,0))
    for q in range(12):
        i=m['st']+q;o.paste(S.crop(((i%6)*fw,(i//6)*fh,(i%6+1)*fw,(i//6+1)*fh)),((q%6)*fw,(q//6)*fh))
    o.quantize(255,method=2,dither=0).save('anim_final/%si.png'%k,optimize=True)
    j={'fw':fw,'fh':fh,'cols':6,'n':12,'fps':round(12*24/m['span'],2),'ax':round(float(x0+(M['ax']-X0)/r),1),'ay':round(float(y1+(M['ay']-Y1)/r),1),'h':round(float(M['h']/r),1)}
    json.dump(j,open('anim_final/%si.json'%k,'w'));print('parado',k,'escala',round(float(r),3),j)
