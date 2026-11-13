# edgefade.py: marca no .json os quadros cujo conteúdo encosta na borda (efeito cortado no vídeo de origem).
# O motor esfuma essas bordas ao carregar o atlas (meta.ef = {quadro: "LRT"}; só ataque e conjuração; a borda de baixo fica de fora para não apagar os pés). Não altera os PNG; pode rodar sempre.
import os,glob,json,numpy as np
from PIL import Image
for f in sorted(glob.glob('anim_final/*.json')):
    k=os.path.basename(f)[:-5];m=json.load(open(f))
    if 'a' not in m:continue  # atlas de parado
    a=np.array(Image.open('anim_final/%s.png'%k).convert('RGBA'))[...,3]
    fw,fh,c=m['fw'],m['fh'],m['cols'];ef={}
    for nm,(st,ln) in m['a'].items():
        if nm in('idle','walk'):continue  # corpo em ciclo: esfumar faria piscar
        for i in range(st,st+ln):
            x,y=(i%c)*fw,(i//c)*fh;op=a[y:y+fh,x:x+fw]>60
            s=''.join(q for q,l in(('L',op[:,:2].any(1)),('R',op[:,-2:].any(1)),('T',op[:2].any(0))) if l.sum()>3)
            if s:ef[str(i)]=s
    m['ef']=ef;json.dump(m,open(f,'w'));print(k,ef)
