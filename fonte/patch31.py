# novo herói (v1): Grude, monstro peludo de braços compridos (o dono citou Huggy Wuggy como inspiração; desenho e nome próprios, tom amigável).
# Abraço: puxa quem está à frente e aperta 3 vezes (criaturas presas; heróis presos no 1º aperto e lentos nos seguintes). Mordidão: dano alto e cura 15%.
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
HERO=r"""  }else if(o.cls===8){const hugA=cp>=0&&!ult?Math.sin(cp*Math.PI):0,bite=ult?Math.sin(cp*Math.PI):0,sw2=sp>=0?Math.sin(sp*Math.PI):0;
    const arm=(ox,len,an)=>{c.save();c.translate(ox,-31+b);c.rotate(an);c.lineCap='round';c.strokeStyle=OUT;c.lineWidth=7;c.beginPath();c.moveTo(0,0);c.lineTo(len,0);c.stroke();c.strokeStyle=S.cloth;c.lineWidth=4.6;c.beginPath();c.moveTo(0,0);c.lineTo(len,0);c.stroke();c.beginPath();c.arc(len+2,0,4.6,0,TAU);fs(c,S.trim2);c.restore()};
    legs(c,wp,mv,S.cloth,S.trim2);
    arm(-6,21+hugA*26,hugA?.3-hugA*.3:1.45-sway*.03);
    rr(c,-8.5,-37+b,17,26,7);fs(c,S.cloth);c.fillStyle=S.cloth2;for(const[q,r2]of[[-5,-29],[3,-23],[-2,-17],[5,-32]])tri(c,q,r2+b,q+3,r2+b,q+1.5,r2+4+b);
    c.fillStyle=S.cloth2;tri(c,-4,-53+b,-1-sway,-61+b,2,-53.5+b);tri(c,1,-54+b,6-sway,-60+b,6,-53+b);
    c.beginPath();c.ellipse(1,-45+b,10.5,9,0,0,TAU);fs(c,S.cloth);
    c.fillStyle='#fff';circ(c,-1.5,-47.5+b,3.4);circ(c,6,-47.5+b,3.4);c.fillStyle='#1a1410';circ(c,-.6,-47+b,1.6);circ(c,6.9,-47+b,1.6);
    {const my=-40.2+b+bite*1.5,mo=1.7+bite*6+hugA*1.2;c.beginPath();c.ellipse(3,my,6.5,mo,0,0,TAU);fs(c,S.dark);c.fillStyle='#fff';for(const q of[-1.5,1.5,4.5,7.5])tri(c,q-1.2,my-mo+.5,q+1.2,my-mo+.5,q,my-mo+2.2+bite*2.4)}
    arm(6,21+hugA*26+sw2*8,hugA?-.3+hugA*.3:sp>=0?la-.7+sw2:1.35+sway*.03);
  }else{
    const hem=Math.sin(wp)*2*mv;"""
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    rep("mas anda à metade da velocidade.'}}];","mas anda à metade da velocidade.'}},\n {n:'Grude',hp:600,dmg:26,range:80,itv:.95,spd:186,arm:3,proj:0,\n  s1:{n:'Abraço',cd:9,d:'estica os braços, puxa quem estiver à frente e aperta 3 vezes antes de soltar. Criaturas ficam presas; heróis ficam presos no primeiro aperto e lentos nos outros. Você anda devagar enquanto aperta.'},s2:{n:'Mordidão',cd:60,d:'uma mordida enorme à sua frente, com dano muito alto. Se acertar alguém, você recupera 15% da vida.'}}];")
    rep("glow:'#7fe3ff',cloth:'#39445e'}];","glow:'#7fe3ff',cloth:'#39445e'},\n {cloth:'#b0489a',cloth2:'#d77ac0',dark:'#3a1230',trim:'#e2b24c',trim2:'#3fb8b0',glow:'#c58cf0'}];")
    rep("cura 6% da vida dos aliados próximos.'}]];","cura 6% da vida dos aliados próximos.'}],\n [{n:'Abraço de Urso',d:'Aperta 4 vezes, e com mais força.'},{n:'Braços Compridos',d:'Alcança bem mais longe, mas aperta mais fraco.'}]];")
    rep("[{t:'cone',r:420,h:.07},null]];","[{t:'cone',r:420,h:.07},null],[{t:'cone',r:170,h:.42},{t:'cone',r:120,h:.8}]];")
    a=s.index('const TAL=[');b=s.index(']}]];',a)+3
    s=s[:b]+""",
 [{b:'Aperto',n:[{id:'dmg',n:'Braços Fortes',m:3,d:'+8% de dano por ponto'},{id:'s1',n:'Abraço Esmagador',m:3,d:'+20% de dano do Abraço por ponto'},{id:'exec',n:'Sem Escapatória',m:1,d:'+35% de dano em alvos com menos de 35% de vida'}]},
  {b:'Pelagem',n:[{id:'hp',n:'Pelo Grosso',m:3,d:'+10% de vida por ponto'},{id:'ward',n:'Fofura Blindada',m:3,d:'-6% de dano sofrido por ponto'},{id:'aegis',n:'Segunda Pele',m:1,d:'Com menos de 30% de vida, fica invulnerável por 2 s (uma vez por minuto)'}]},
  {b:'Fome',n:[{id:'cdr',n:'Apetite',m:3,d:'-8% de recarga das habilidades por ponto'},{id:'spd',n:'Pernas Longas',m:3,d:'+5% de movimento por ponto'},{id:'ult',n:'Bocão',m:1,d:'Mordidão 40% mais forte, e deixa lento quem sobreviver'}]}]"""+s[b:]
    rep("  else if(cls===7){\n","  else if(cls===8){const inC=(q,L,hf)=>{const dx=q.x-o.x,dy=q.y-o.y,dd=Math.hypot(dx,dy)||1;if(dd>L+q.r)return false;let da=Math.atan2(dy,dx)-ang;da=Math.atan2(Math.sin(da),Math.cos(da));return Math.abs(da)<=hf||dd<=40};\n    if(!k){const L=ev===2?250:170,hf=.42,n=ev===1?4:3,d=m*(ev===1?1.25:ev===2?.9:1.1)*s1m;\n      if(mine){const ts=[];each(q=>{if(inC(q,L,hf))ts.push(q)});shove(o,ang,L,hf,d,3);if(ts.length){H.hug={ts,n:n-1,t:.5,d};H.slow=Math.max(H.slow,now()+480*n)}}\n      fx('cone',o.x,o.y,{a:ang,r:L,half:hf,T:.35,col:'#c58cf0'});for(const sd of[-1,1])for(let q=1;q<7;q++)part(o.x+Math.cos(ang+sd*.3)*q*L/7,o.y-28+Math.sin(ang+sd*.3)*q*L/7,0,-8,.3,4,'#d77ac0');shake(3)}\n    else{const L=120,hf=.8;if(mine){let hit=0;each(q=>{if(inC(q,L,hf))hit++});cone(o.x,o.y,ang,L,hf,m*(k===2?9.8:7),k===2?1:0);if(hit)H.hp=Math.min(H.mhp,H.hp+H.mhp*.15)}\n      const bx=o.x+Math.cos(ang)*60,by=o.y-26+Math.sin(ang)*60;fx('slash',bx,by,{a:ang+1.2,T:.3,col:'#ffffff',s:2});fx('slash',bx,by,{a:ang-1.2,T:.3,col:'#ffffff',s:2});fx('flash',bx,by+26,{r:110,T:.25,col:'#ff8ad0'});fx('ring',bx,by+26,{r:90,T:.4,col:'#c58cf0'});burst(bx,by,18,'#ff8ad0',260,.5,4.5);shake(8)}}\n  else if(cls===7){\n")
    rep("    if(H.dash){const D=H.dash","    if(H.hug){const U=H.hug;U.t-=dt;if(U.t<=0){U.t=.5;U.n--;for(const q of U.ts){const al=q.kind==='hero'?!q.dead&&!q.gone:q.alive!==false;if(al&&Math.hypot(q.x-H.x,q.y-H.y)<150){dealt(q,U.d,q.kind==='hero'?1:3);fx('ring',q.x,q.y-20,{r:34,T:.25,col:'#c58cf0'})}}if(U.n<=0)H.hug=null}}\n    if(H.dash){const D=H.dash")
    rep("pull:null,dash:null,tw:null","pull:null,dash:null,hug:null,tw:null")
    rep("H.pull=null;H.dash=null;respawnFx","H.pull=null;H.dash=null;H.hug=null;respawnFx")
    rep("H.mk++;toast(D.n+' tombou');","H.mk++;H.bk=(H.bk|0)+1;toast(D.n+' tombou');")
    rep("  }else{\n    const hem=Math.sin(wp)*2*mv;",HERO)
    rep('<b>Sentinela</b><span>Robô blindado: tiro rápido e raio</span></label>','<b>Sentinela</b><span>Robô blindado: tiro rápido e raio</span></label>\n          <input type="radio" name="hero" id="hero8" value="8"><label for="hero8"><canvas width="160" height="168" id="ic8"></canvas><b>Grude</b><span>Abraça, prende e morde</span></label>')
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok (patch31)')
