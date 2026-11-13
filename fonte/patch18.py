import re,json,base64,os,sys
s=open('index-v17.bak.html',encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a))
    s=s.replace(a,b)
# embedded art: every file in art_final/ named <key>.png|jpg
src={}
for f in ([] if os.environ.get('LITE') else sorted(os.listdir('art_final'))):  # LITE=1: versão de gráfico simples, sem arte embutida
    k,ext=os.path.splitext(f);mime={'.png':'image/png','.jpg':'image/jpeg','.webp':'image/webp'}[ext]
    src[k]='data:%s;base64,%s'%(mime,base64.b64encode(open('art_final/'+f,'rb').read()).decode())
rep("function makeSprites(){","""/* Arte pintada (piloto): imagens embutidas no arquivo. O que não tiver imagem continua desenhado por código.
   Chaves: h<classe><i|w|x|a> = herói parado, passo, passo oposto, ataque; m<tipo> = criatura; texS/texG/texD = chão; rock, tree. */
const ART={},ART_SRC=%s;
function artReady(k,im){ART[k]=im;
  const b={texS:0,texG:1,texD:2}[k];
  if(b!=null){const q=im.width/4;SPR.fl[b]=Array.from({length:16},(_,i)=>mk(TILE,TILE,x=>x.drawImage(im,(i%%4)*q,(i>>2)*q,q,q,0,0,TILE,TILE)));SPR.flT[b]=true;
    const c1=document.createElement('canvas');c1.width=c1.height=1;const g=c1.getContext('2d');g.drawImage(im,0,0,1,1);const d=g.getImageData(0,0,1,1).data,col='rgb('+d[0]+','+d[1]+','+d[2]+')';
    SPR.ed[b]=[0,1,2,3].map(dir=>mk(TILE,TILE,x=>{x.fillStyle=col;x.globalAlpha=.85;for(let j=0;j<8;j++){const u=j/7*TILE,w=7+Math.random()*9,dp=1+Math.random()*5,cx=dir%%2===0?u:(dir===1?TILE-dp+3:dp-3),cy=dir===0?dp-3:dir===2?TILE-dp+3:u;x.beginPath();x.ellipse(cx,cy,dir%%2?w*.75:w,dir%%2?w:w*.75,0,0,TAU);x.fill()}}))}
  if(k==='rock'){const w=70,h=Math.round(w*im.height/im.width);SPR.rock=SPR.rock.map(()=>mk(w,h+6,x=>{x.fillStyle='rgba(0,0,0,.4)';ell(x,w/2,h-4,w*.42,9);x.drawImage(im,0,0,w,h)}))}
  if(k==='tree'){const w=92,h=Math.round(w*im.height/im.width);SPR.tree=SPR.tree.map(()=>mk(w,h+4,x=>{x.fillStyle='rgba(0,0,0,.4)';ell(x,w/2,h-6,w*.3,8);x.drawImage(im,0,0,w,h)}))}}
function loadArt(){SPR.flT=[false,false,false];for(const k in ART_SRC){const im=new Image();im.onload=()=>artReady(k,im);im.src=ART_SRC[k]}}
function makeSprites(){"""%json.dumps(src))
rep("ctx.drawImage(SPR.fl[b][d<7?5:d<22?4:(d>>2)%4],X,Y,W,W);","ctx.drawImage(SPR.flT[b]?SPR.fl[b][(tx&3)+(ty&3)*4]:SPR.fl[b][d<7?5:d<22?4:(d>>2)%4],X,Y,W,W);")
rep("      else ctx.drawImage(s,tx*TILE+24-s.w/2,ty*TILE+TILE+4-s.h,s.w,s.h);","      else if(ART.tree){ctx.save();ctx.translate(tx*TILE+24,ty*TILE+TILE+6);const z=.9+((dd>>4)%4)*.08;ctx.scale((dd>>3)&1?-z:z,z);ctx.drawImage(s,-s.w/2,-s.h,s.w,s.h);ctx.restore()}\n      else ctx.drawImage(s,tx*TILE+24-s.w/2,ty*TILE+TILE+4-s.h,s.w,s.h);")
# heroes
rep("  if(o.lv>=4)wings(c,o.lv,t,ult?Math.sin(cp*Math.PI):(o.bf&8)?.5:0);\n  if(o.cls===0){","""  const AI=ART['h'+o.cls+'i'];
  if(AI){const k='h'+o.cls,ph=((wp%TAU)+TAU)%TAU/TAU,pk=(sp>=0&&sp<.75)||cp>=0?'a':mv>.3?(ph<.25?'w':ph<.5?'i':ph<.75?'x':'i'):'i',ky=ART[k+pk]?k+pk:k+'i',im=ART[ky],f=(o.icon?58:90)/AI.height,w=im.width*f,hh=im.height*f;
    if(ult)glow(c,0,-30,40,S.glow||'#ffe9a0',.5);c.translate(0,3+b*.8);if(mv>.3)c.rotate(Math.sin(wp)*.03);c.drawImage(im,-w*(ART_AX[ky]||.5),-hh,w,hh)}
  else if(o.lv>=4)wings(c,o.lv,t,ult?Math.sin(cp*Math.PI):(o.bf&8)?.5:0);
  if(AI){}
  else if(o.cls===0){""")
rep("const ART={},ART_SRC=","const ART_AX=%s,ART={},ART_SRC="%json.dumps(json.load(open('art_final_meta.json'))))
# creeps
rep("  if(k.kd===1){\n","""  const AM=ART['m'+k.kd];
  if(AM){const hh=T.h*1.65,w=hh*AM.width/AM.height;c.translate(sp>=0?Math.sin(sp*Math.PI)*8:0,Math.sin(wp*2)*1.5*mv);c.rotate(Math.sin(wp)*.035*mv-(sp>=0?Math.sin(sp*Math.PI)*.12:0));c.drawImage(AM,-w/2,-hh+5,w,hh)}
  else if(k.kd===1){
""")
rep("makeSprites();","makeSprites();loadArt();")
rep("function loadArt(){","""const EDC=new Map();
function edTile(b,dir,tx,ty){if(!SPR.flT[b]||!ART_TEX[b])return SPR.ed[b][dir];const idx=(tx&3)+(ty&3)*4,key=b*64+idx*4+dir;let c=EDC.get(key);if(c)return c;const im=ART_TEX[b],q=im.width/4;
  c=mk(TILE,TILE,x=>{x.fillStyle='#000';for(let j=0;j<9;j++){const u=j/8*TILE,h=((j*37+dir*11+idx*7)%9)/8,w=8+h*9,dp=3+h*7,cx=dir%2===0?u:(dir===1?TILE-dp+5:dp-5),cy=dir===0?dp-5:dir===2?TILE-dp+5:u;
      const g=x.createRadialGradient(cx,cy,w*.35,cx,cy,w*1.25);g.addColorStop(0,'rgba(0,0,0,1)');g.addColorStop(1,'rgba(0,0,0,0)');x.fillStyle=g;x.fillRect(cx-w*1.3,cy-w*1.3,w*2.6,w*2.6)}
    x.globalCompositeOperation='source-in';x.drawImage(im,(idx%4)*q,(idx>>2)*q,q,q,0,0,TILE,TILE)});EDC.set(key,c);return c}
const ART_TEX=[null,null,null];
function loadArt(){""")
rep("  if(b!=null){const q=im.width/4;","  if(b!=null){ART_TEX[b]=im;EDC.clear();const q=im.width/4;")
rep("if(ty>0&&B[i-N]>b)ctx.drawImage(SPR.ed[B[i-N]][0],X,Y,W,W);if(tx+1<N&&B[i+1]>b)ctx.drawImage(SPR.ed[B[i+1]][1],X,Y,W,W);if(ty+1<N&&B[i+N]>b)ctx.drawImage(SPR.ed[B[i+N]][2],X,Y,W,W);if(tx>0&&B[i-1]>b)ctx.drawImage(SPR.ed[B[i-1]][3],X,Y,W,W);",
    "if(ty>0&&B[i-N]>b)ctx.drawImage(edTile(B[i-N],0,tx,ty),X,Y,W,W);if(tx+1<N&&B[i+1]>b)ctx.drawImage(edTile(B[i+1],1,tx,ty),X,Y,W,W);if(ty+1<N&&B[i+N]>b)ctx.drawImage(edTile(B[i+N],2,tx,ty),X,Y,W,W);if(tx>0&&B[i-1]>b)ctx.drawImage(edTile(B[i-1],3,tx,ty),X,Y,W,W);")
rep("bar(o.x,o.y-74,36,o.hp/o.mh,ally(o)?'#6fb7ff':'#d9534a');ctx.font='700 12px '+FONT;ctx.textAlign='center';ctx.fillStyle='#10131f';ctx.fillText(o.name+' '+o.lv,o.x+1,o.y-78);ctx.fillStyle=ally(o)?'#bfe0ff':'#f2ead8';ctx.fillText(o.name+' '+o.lv,o.x,o.y-79);",
    "{const ao=ART['h'+o.cls+'i']?34:0;bar(o.x,o.y-74-ao,36,o.hp/o.mh,ally(o)?'#6fb7ff':'#d9534a');ctx.font='700 12px '+FONT;ctx.textAlign='center';ctx.fillStyle='#10131f';ctx.fillText(o.name+' '+o.lv,o.x+1,o.y-78-ao);ctx.fillStyle=ally(o)?'#bfe0ff':'#f2ead8';ctx.fillText(o.name+' '+o.lv,o.x,o.y-79-ao)}")
rep("bar(H.x,H.y-74,38,H.hp/H.mhp,'#74c365');","bar(H.x,H.y-74-(ART['h'+H.cls+'i']?34:0),38,H.hp/H.mhp,'#74c365');")
rep("if(o.hp<o.mhp)bar(o.x,o.y-MON[o.kd].h-8,o.r*2.4,o.hp/o.mhp,'#d9534a')}","if(o.hp<o.mhp)bar(o.x,o.y-MON[o.kd].h*(ART['m'+o.kd]?1.9:1)-8,o.r*2.4,o.hp/o.mhp,'#d9534a')}")
rep("const d={x:34,y:74,cls:i,lv:12,","const d={icon:1,x:ART['h'+i+'i']?40:34,y:74,cls:i,lv:12,")
rep("  if(o.lv>=10){const hy=o.cls===2?-66:-53;","  if(o.lv>=10&&!AI){const hy=o.cls===2?-66:-53;")
open('index.html','w',encoding='utf-8').write(s)
open('game18.js','w',encoding='utf-8').write(re.findall(r'<script>(.*?)</script>',s,re.S)[-1])
a="  netInit();refreshMenu();"
s=s.replace(a,"  window.__d={P,pick:i=>pickEvo(i),xp:v=>gainXp(v),kill:c=>killCreep(c,true),bossDown:()=>{const B=G.bosses[0];B.my=B.mhp;B.hp=0;bossDown(B,now())},get G(){return G},get H(){return H},others,cast:(i,a)=>cast(i,a),solid:(x,y)=>solid(x,y),N:()=>N,TILE,hurt:(d,by)=>hurt(d,by,true),setOff:ms=>{G.off+=ms}};\n"+a)
open('site/index.html','w',encoding='utf-8').write(s)
print(len(s)//1024,'KB',list(src))
