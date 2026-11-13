# roda depois do patch18.py: troca as poses soltas por animação quadro a quadro (atlas em anim_final/<chave>.png + .json)
import re,json,base64,os
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
src={};meta={}
for f in ([] if os.environ.get('LITE') else sorted(os.listdir('anim_final'))):  # LITE=1: sem animações embutidas
    k,ext=os.path.splitext(f)
    if ext=='.png':src[k]='data:image/png;base64,'+base64.b64encode(open('anim_final/'+f,'rb').read()).decode()
    elif ext=='.json':meta[k]=json.load(open('anim_final/'+f))
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:80],s.count(a));s=s.replace(a,b)
    rep("const EDC=new Map();","/* Animação quadro a quadro: uma folha por personagem, com parado, andar e atacar. */\nconst ANIM={},ANIM_SRC=%s,ANIM_META=%s;\nconst EDC=new Map();"%(json.dumps(src),json.dumps(meta)))
    rep("function loadArt(){SPR.flT=[false,false,false];","function loadArt(){SPR.flT=[false,false,false];for(const k in ANIM_SRC){const im=new Image();im.onload=()=>{ANIM[k]={img:im,m:ANIM_META[k]}};im.src=ANIM_SRC[k]}")
    a=s.index("  const AI=ART['h'+o.cls+'i'];");b=s.index("  else if(o.lv>=4)wings(c,o.lv,t,ult?")
    s=s[:a]+"""  const AI=ANIM['h'+o.cls];
  if(AI){const M=AI.m,f=(o.icon?56:74)/M.h;let fr;
    if(sp>=0||cp>=0){const A=(sp<0&&M.a.cast)||M.a.atk,q=sp>=0?sp:cp;fr=A[0]+Math.min(A[1]-1,Math.floor(q*A[1]))}
    else if(mv>.3){const A=M.a.walk;fr=A[0]+Math.floor(((wp/TAU)%1+1)%1*A[1])}
    else{const A=M.a.idle,n=A[1],P=Math.max(1,2*n-2);let k=Math.floor(t/1000*M.ifps+o.x*.013)%P;if(k>=n)k=P-k;fr=A[0]+k}
    if(o.lv>=4&&!o.icon){glow(c,0,-4,24+Math.min(16,o.lv),S.glow||'#ffe9a0',.22+.1*Math.sin(t/400))}
    const sh=o.lv>=10&&!o.icon?3:0,sa=t/900;for(let j=0;j<sh;j++){const a=sa+j*TAU/3;if(Math.sin(a)<0){const x=Math.cos(a)*24,y=-38+Math.sin(a)*6;c.fillStyle=S.glow||'#ffe9a0';c.beginPath();c.moveTo(x,y-6);c.lineTo(x+3,y);c.lineTo(x,y+6);c.lineTo(x-3,y);c.closePath();c.fill()}}
    if(ult)glow(c,0,-28,38,S.glow||'#ffe9a0',.5);
    const by=(sp<0&&cp<0&&mv<=.3&&M.a.idle[1]===1)?1+.013*Math.sin(t/560+o.x*.01):1;c.drawImage(AI.img,(fr%M.cols)*M.fw,Math.floor(fr/M.cols)*M.fh,M.fw,M.fh,-M.ax*f,-M.ay*f*by+3,M.fw*f,M.fh*f*by);
    for(let j=0;j<sh;j++){const a=sa+j*TAU/3;if(Math.sin(a)>=0){const x=Math.cos(a)*24,y=-38+Math.sin(a)*6;glow(c,x,y,9,S.glow||'#ffe9a0',.5);c.fillStyle='#ffffff';c.beginPath();c.moveTo(x,y-6);c.lineTo(x+3,y);c.lineTo(x,y+6);c.lineTo(x-3,y);c.closePath();c.fill()}}}
"""+s[b:]
    rep("c.scale(dir,1);c.translate((o.cls===0||o.cls===4)&&sp>=0","c.scale(dir,1);c.translate((o.cls===0||o.cls===4)&&sp>=0&&!ANIM['h'+o.cls]")
    rep("const ao=ART['h'+o.cls+'i']?34:0;","const ao=ANIM['h'+o.cls]?14:0;")
    rep("bar(H.x,H.y-74-(ART['h'+H.cls+'i']?34:0),","bar(H.x,H.y-74-(ANIM['h'+H.cls]?14:0),")
    rep("x:ART['h'+i+'i']?40:34,","x:ANIM['h'+i]?40:34,")
    rep("  if(B.ty===0){if(B.hp<B.mhp*.5)glow(c,B.x,B.y-70,120,'#d9534a',.3);drawArch(c,B,t)}else if(B.ty===1)","  const AB=ART['b'+B.ty],BA=ANIM['b'+B.ty];\n  if(BA){const M=BA.m,f=D.h*1.3/M.h,cf=Math.cos(B.face);if(Math.abs(cf)>.2||!B.dr)B.dr=cf<0?-1:1;const sp=B.sw>0?1-B.sw/B.swD:-1;let fr;if(sp>=0){const A=M.a.atk;fr=A[0]+Math.min(A[1]-1,Math.floor(sp*A[1]))}else if((B.mv||0)>.3){const A=M.a.walk;fr=A[0]+Math.floor((((B.walk||0)/TAU)%1+1)%1*A[1])}else fr=M.a.idle[0];const by=(sp<0&&(B.mv||0)<=.3)?1+.012*Math.sin(t/620):1;if(B.ty===0&&B.hp<B.mhp*.5)glow(c,B.x,B.y-70,120,'#d9534a',.3);c.save();c.translate(B.x,B.y);c.fillStyle='rgba(0,0,0,.4)';ell(c,0,0,D.r*1.3,D.r*.45);c.scale(B.dr,1);c.drawImage(BA.img,(fr%M.cols)*M.fw,Math.floor(fr/M.cols)*M.fh,M.fw,M.fh,-M.ax*f,-M.ay*f*by+8,M.fw*f,M.fh*f*by);c.restore()}\n  else if(AB){const hh=D.h*1.3,w=hh*AB.width/AB.height,cf=Math.cos(B.face);if(Math.abs(cf)>.2||!B.dr)B.dr=cf<0?-1:1;const sp=B.sw>0?1-B.sw/B.swD:-1;if(B.ty===0&&B.hp<B.mhp*.5)glow(c,B.x,B.y-70,120,'#d9534a',.3);c.save();c.translate(B.x,B.y);c.fillStyle='rgba(0,0,0,.4)';ell(c,0,0,D.r*1.3,D.r*.45);c.scale(B.dr,1);c.translate(sp>=0?Math.sin(sp*Math.PI)*10:0,Math.sin((B.walk||0)*2)*2*(B.mv||0)+Math.sin(t/500)*1.5);c.rotate(-(sp>=0?Math.sin(sp*Math.PI)*.1:0));c.drawImage(AB,-w/2,-hh+8,w,hh);c.restore()}\n  else if(B.ty===0){if(B.hp<B.mhp*.5)glow(c,B.x,B.y-70,120,'#d9534a',.3);drawArch(c,B,t)}else if(B.ty===1)")
    rep("function artReady(k,im){ART[k]=im;","function artReady(k,im){ART[k]=im;\n  {const cq={c0:0,c1:1,c2:2,c3:3,c4:4,c5:5}[k];if(cq!=null)SPR.chest[cq]=mk(96,96,x=>{const s=Math.min(96/im.width,96/im.height),w=im.width*s,h=im.height*s;x.drawImage(im,(96-w)/2,96-h,w,h)})}")
    rep("ctx.drawImage(SPR.chest[q],o.x-17,o.y-28+pl,34,34)","ctx.drawImage(SPR.chest[q],o.x-23,o.y-38+pl,46,46)")
    rep("ctx.drawImage(SPR.chest[5],x-17,y-30,34,34)","ctx.drawImage(SPR.chest[5],x-25,y-42,50,50)")
    rep("if(o.type==='altar'){ctx.fillStyle='rgba(0,0,0,.35)';ell(ctx,x,y+3,28,9);rr(ctx,x-21,y-11,42,14,3);fs(ctx,'#4a5270');rr(ctx,x-15,y-23,30,14,3);fs(ctx,'#5c6588');ctx.fillStyle='#e2b24c';ctx.fillRect(x-15,y-13,30,2.5);\n        const by=y-50+","if(o.type==='altar'){const AA=ART.altar;ctx.fillStyle='rgba(0,0,0,.35)';if(AA){const w=84,h=w*AA.height/AA.width;ell(ctx,x,y+3,38,11);ctx.drawImage(AA,x-w/2,y+12-h,w,h)}else{ell(ctx,x,y+3,28,9);rr(ctx,x-21,y-11,42,14,3);fs(ctx,'#4a5270');rr(ctx,x-15,y-23,30,14,3);fs(ctx,'#5c6588');ctx.fillStyle='#e2b24c';ctx.fillRect(x-15,y-13,30,2.5)}\n        const by=y-(AA?78:50)+")
    rep("const AM=ART['m'+k.kd];\n  if(AM){","const AM=ART['m'+k.kd],CA=ANIM['m'+k.kd];\n  if(CA){const M=CA.m,f=T.h*1.65/M.h;let fr;if(sp>=0){const A=M.a.atk;fr=A[0]+Math.min(A[1]-1,Math.floor(sp*A[1]))}else if(mv>.3){const A=M.a.walk;fr=A[0]+Math.floor(((wp/TAU)%1+1)%1*A[1])}else fr=M.a.idle[0];c.drawImage(CA.img,(fr%M.cols)*M.fw,Math.floor(fr/M.cols)*M.fh,M.fw,M.fh,-M.ax*f,-M.ay*f+3,M.fw*f,M.fh*f)}\n  else if(AM){")
    # tema A Convergência: sai o vocabulário de anjos
    for x,y in [("Arcanjo Caído","Guardião do Núcleo"),("row('Arcanjo'","row('Guardião'"),("lendária (Arcanjo)","lendária (Guardião)"),
      ("Seu santuário","Sua âncora"),("Retorno ao santuário","Retorno à âncora"),("Ira Celestial","Ira Solar"),("explosão sagrada","explosão solar"),
      ("Lâmina Sagrada","Lâmina Solar"),("Julgamento Sagrado","Julgamento Solar"),("Asas do Serafim","Manto do Vendaval"),
      ("Nível 4: suas asas despontaram.","Nível 4: sua ressonância despertou."),("Nível 10: você ganhou a auréola.","Nível 10: estilhaços da Convergência orbitam você."),
      ("P.name='Anjo'+","P.name='Herói'+"),("||'Anjo';","||'Herói';"),
      ('h1::before{content:"";position:absolute;left:4px;top:0;width:58px;height:15px;border:3px solid var(--gold);border-radius:50%;transform:rotate(-8deg);opacity:.9}',''),
      ("color:var(--gold);text-wrap:balance;position:relative;padding-top:18px}","color:var(--gold);text-wrap:balance;position:relative}")]:
        assert x in s,x;s=s.replace(x,y)
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
open('game19.js','w',encoding='utf-8').write(re.findall(r'<script>(.*?)</script>',s,re.S)[-1])
print(len(s)//1024,'KB',list(src),meta)
