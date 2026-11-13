# roda depois do patch20.py: animação de parado em laço quando existir anim_final/<chave>i (heróis hN, chefes bN)
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    rep("const EDC=new Map();","""/* Parado em laço: atlas próprio <chave>i com n quadros; devolve false se o personagem ainda não tem. */
function idleDraw(c,k,t,ph,disp,oy){const AN=ANIM[k+'i'];if(!AN)return false;const M=AN.m,f=disp/M.h,p=((t/1000*M.fps+ph)%M.n+M.n)%M.n,i=Math.floor(p);
  animDraw(c,AN,i,(i+1)%M.n,p-i,-M.ax*f,-M.ay*f+oy,M.fw*f,M.fh*f);return true}
const EDC=new Map();""")
    rep("animDraw(c,AI,fr,fb,bq,-M.ax*f,-M.ay*f*by+3,M.fw*f,M.fh*f*by);","if(!(sp<0&&cp<0&&mv<=.3&&idleDraw(c,'h'+o.cls,t,o.x*.013,o.icon?56:74,3)))animDraw(c,AI,fr,fb,bq,-M.ax*f,-M.ay*f*by+3,M.fw*f,M.fh*f*by);")
    rep("animDraw(c,BA,fr,fb,bq,-M.ax*f,-M.ay*f*by+8,M.fw*f,M.fh*f*by);","if(!(sp<0&&(B.mv||0)<=.3&&idleDraw(c,'b'+B.ty,t,0,D.h*1.3,8)))animDraw(c,BA,fr,fb,bq,-M.ax*f,-M.ay*f*by+8,M.fw*f,M.fh*f*by);")
    assert s.count('Arena Celeste')>=2;s=s.replace('Arena Celeste','Arena Nexus')  # nome do jogo (o tópico MQTT arenaceleste3 fica)
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok (patch21)')
