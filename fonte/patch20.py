# roda depois do patch19.py (e do edgefade.py, que marca os quadros cortados nos .json):
#  - mistura quadros vizinhos ao andar (e em conjuração de herói / ataque de chefe) para o movimento não pular de pose em pose
#  - criaturas respiram quando paradas
#  - esfuma a borda dos quadros de ataque cujo efeito foi cortado no vídeo de origem (meta.ef)
#  - botões de ação em bloco no canto direito (retrato); Fechar da árvore embaixo à direita; tocar fora da árvore fecha
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    # ---- motor de animação
    rep("const EDC=new Map();","""/* Esfuma a borda dos quadros marcados em meta.ef (efeito que saía do vídeo de origem). */
function animPrep(im,M){const ef=M.ef;if(!ef||!Object.keys(ef).length)return im;
  const cv=document.createElement('canvas');cv.width=im.width;cv.height=im.height;const x=cv.getContext('2d');x.drawImage(im,0,0);x.globalCompositeOperation='destination-out';
  for(const k in ef){const i=+k,X=(i%M.cols)*M.fw,Y=Math.floor(i/M.cols)*M.fh,w=Math.max(10,Math.round(M.fw*.17)),h=Math.max(10,Math.round(M.fh*.17));
    for(const sd of ef[k]){let g,r;if(sd==='R'){g=x.createLinearGradient(X+M.fw-w,0,X+M.fw,0);r=[X+M.fw-w,Y,w,M.fh]}else if(sd==='L'){g=x.createLinearGradient(X+w,0,X,0);r=[X,Y,w,M.fh]}else{g=x.createLinearGradient(0,Y+h,0,Y);r=[X,Y,M.fw,h]}
      g.addColorStop(0,'rgba(0,0,0,0)');g.addColorStop(.55,'rgba(0,0,0,.55)');g.addColorStop(1,'rgba(0,0,0,1)');x.fillStyle=g;x.fillRect(r[0],r[1],r[2],r[3])}}
  return cv}
/* Desenha o quadro fa; se fb>=0, mistura fa e fb (peso q de fb) num rascunho antes, para a silhueta não ficar translúcida. */
function animDraw(c,AN,fa,fb,q,dx,dy,dw,dh){const M=AN.m,im=AN.img,W=M.fw,Hh=M.fh;
  if(fb<0||fb===fa||q<.06){c.drawImage(im,(fa%M.cols)*W,Math.floor(fa/M.cols)*Hh,W,Hh,dx,dy,dw,dh);return}
  if(q>.94){c.drawImage(im,(fb%M.cols)*W,Math.floor(fb/M.cols)*Hh,W,Hh,dx,dy,dw,dh);return}
  if(!AN.bx){const b=document.createElement('canvas');b.width=W;b.height=Hh;AN.bl=b;AN.bx=b.getContext('2d')}
  const x=AN.bx;x.globalCompositeOperation='copy';x.globalAlpha=1-q;x.drawImage(im,(fa%M.cols)*W,Math.floor(fa/M.cols)*Hh,W,Hh,0,0,W,Hh);
  x.globalCompositeOperation='lighter';x.globalAlpha=q;x.drawImage(im,(fb%M.cols)*W,Math.floor(fb/M.cols)*Hh,W,Hh,0,0,W,Hh);
  c.drawImage(AN.bl,0,0,W,Hh,dx,dy,dw,dh)}
const EDC=new Map();""")
    rep("im.onload=()=>{ANIM[k]={img:im,m:ANIM_META[k]}}","im.onload=()=>{ANIM[k]={img:animPrep(im,ANIM_META[k]),m:ANIM_META[k]}}")
    # andar (herói e criatura usam o mesmo trecho)
    rep("else if(mv>.3){const A=M.a.walk;fr=A[0]+Math.floor(((wp/TAU)%1+1)%1*A[1])}",
        "else if(mv>.3){const A=M.a.walk,p=((wp/TAU)%1+1)%1*A[1],i=Math.floor(p)%A[1];fr=A[0]+i;fb=A[0]+(i+1)%A[1];bq=p-Math.floor(p)}",2)
    # herói
    rep("f=(o.icon?56:74)/M.h;let fr;","f=(o.icon?56:74)/M.h;let fr,fb=-1,bq=0;")
    rep("q=sp>=0?sp:cp;fr=A[0]+Math.min(A[1]-1,Math.floor(q*A[1]))}","q=sp>=0?sp:cp,p=q*A[1],i=Math.min(A[1]-1,Math.floor(p));fr=A[0]+i;if(sp<0&&i<A[1]-1){fb=fr+1;bq=p-i}}")
    rep("c.drawImage(AI.img,(fr%M.cols)*M.fw,Math.floor(fr/M.cols)*M.fh,M.fw,M.fh,-M.ax*f,-M.ay*f*by+3,M.fw*f,M.fh*f*by);","animDraw(c,AI,fr,fb,bq,-M.ax*f,-M.ay*f*by+3,M.fw*f,M.fh*f*by);")
    # chefe
    rep("let fr;if(sp>=0){const A=M.a.atk;fr=A[0]+Math.min(A[1]-1,Math.floor(sp*A[1]))}else if((B.mv||0)>.3){const A=M.a.walk;fr=A[0]+Math.floor((((B.walk||0)/TAU)%1+1)%1*A[1])}else fr=M.a.idle[0];",
        "let fr,fb=-1,bq=0;if(sp>=0){const A=M.a.atk,p=sp*A[1],i=Math.min(A[1]-1,Math.floor(p));fr=A[0]+i;if(i<A[1]-1){fb=fr+1;bq=p-i}}else if((B.mv||0)>.3){const A=M.a.walk,p=(((B.walk||0)/TAU)%1+1)%1*A[1],i=Math.floor(p)%A[1];fr=A[0]+i;fb=A[0]+(i+1)%A[1];bq=p-Math.floor(p)}else fr=M.a.idle[0];")
    rep("c.drawImage(BA.img,(fr%M.cols)*M.fw,Math.floor(fr/M.cols)*M.fh,M.fw,M.fh,-M.ax*f,-M.ay*f*by+8,M.fw*f,M.fh*f*by);","animDraw(c,BA,fr,fb,bq,-M.ax*f,-M.ay*f*by+8,M.fw*f,M.fh*f*by);")
    # criatura (com respiração quando parada)
    rep("f=T.h*1.65/M.h;let fr;","f=T.h*1.65/M.h;let fr,fb=-1,bq=0;")
    rep("c.drawImage(CA.img,(fr%M.cols)*M.fw,Math.floor(fr/M.cols)*M.fh,M.fw,M.fh,-M.ax*f,-M.ay*f+3,M.fw*f,M.fh*f)}",
        "const by=(sp<0&&mv<=.3)?1+.014*Math.sin(t/560+k.hx*.05):1;animDraw(c,CA,fr,fb,bq,-M.ax*f,-M.ay*f*by+3,M.fw*f,M.fh*f*by)}")
    # ---- interface
    rep("#b-tal[data-n]:not([data-n=\"0\"])::before{","""/* retrato: ações em bloco de duas colunas no canto direito, longe do polegar que move o herói */
@media (max-aspect-ratio:1/1){.pad{grid-template-columns:auto auto;grid-template-areas:"shop tal" "pot pick" "ult skill";gap:8px 10px;justify-items:center;align-items:center}
#b-shop{grid-area:shop}#b-tal{grid-area:tal}#b-pot{grid-area:pot}#b-pick{grid-area:pick}#b-ult{grid-area:ult}#b-skill{grid-area:skill}}
#b-tal[data-n]:not([data-n=\"0\"])::before{""")
    rep("#tal .attr{display:grid;gap:5px}","""#tal .attr{display:grid;gap:5px}
#tal .tal-foot{display:flex;align-items:center;gap:10px;position:sticky;bottom:0;margin:0 -12px -12px;padding:8px 12px 10px;background:var(--stone);border-top:1px solid var(--line);border-radius:0 0 12px 12px}
#tal .tal-foot .label{flex:1;min-width:0}
#tal .tal-x{flex:none;min-width:132px;min-height:46px;padding:10px 18px;font:800 16px var(--ui);letter-spacing:.05em;text-transform:uppercase;color:var(--gold-ink);background:var(--gold);border:0;border-radius:8px}
#tal .tal-x:active{filter:brightness(.9)}""")
    rep('<span class="gold" id="t-pts"></span><button class="ghost" id="b-tclose" type="button">Fechar</button></div>','<span class="gold" id="t-pts"></span></div>')
    rep('<div class="attr"><span class="label" id="t-amsg"></span><div class="attr-row" id="t-attr"></div></div>',
        '<div class="attr"><div class="attr-row" id="t-attr"></div></div>\n      <div class="tal-foot"><span class="label" id="t-amsg"></span><button class="tal-x" id="b-tclose" type="button">Fechar</button></div>')
    rep("$('b-tclose').addEventListener('click',()=>sheet(''));","$('b-tclose').addEventListener('click',()=>sheet(''));$('tal').addEventListener('click',e=>{if(e.target===e.currentTarget)sheet('')});")
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok')
