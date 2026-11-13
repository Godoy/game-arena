# novo herói (as duas versões): Zero, o demolidor. Corpo a corpo fraco; Mina invisível para inimigos (até 3) e TNT Gigante.
# Explosões não ferem o próprio herói nem aliados. Cada inimigo pego por mina dá +6% de dano por 8 s (até +30%).
# Rede: sx[4]=5 avisa "mina explodiu em x,y" (sx[3] = raio). Zonas novas: 'mine' e 'tnt'.
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
FN=r"""/* Herói Zero: minas e TNT. */
function boomFx(x,y,R,big){fx('flash',x,y,{r:R*1.2,T:.3,col:'#ffd27a'});fx('ring',x,y,{r:R,T:.45,col:'#ff9a4a'});fx('ring',x,y,{r:R*.6,T:.6,col:'#fff3c4'});fx('star',x,y,{r:R*.8,T:.4,col:'#ffe9a0'});burst(x,y-10,big?30:16,'#ff9a4a',big?360:260,.6,5);burst(x,y-8,big?18:10,'#4a3a34',big?240:180,.8,5,1,420);if(H&&Math.hypot(H.x-x,H.y-y)<520)shake(big?12:5)}
function mineTick(z){if(z.t>=z.T+z.dur)return true;if(!z.mine||z.t<z.T||!H||H.dead&&0)return false;
  let hit=false,n=0;each(q=>{const d=Math.hypot(q.x-z.x,q.y-z.y);if(d<z.r+q.r)hit=true;if(d<z.R+q.r)n++});if(!hit)return false;
  aoe(z.x,z.y,z.R,z.bd,null,z.flag);boomFx(z.x,z.y,z.R);
  if(n){const e=now();H.boomN=Math.min(5,(e<H.boomT?H.boomN:0)+n);H.boomT=e+8000;ftext(H.x,H.y-84,'+'+H.boomN*6+'% de dano','#ffb36a')}
  lastSkill=[++sseq,z.x|0,z.y|0,Math.round(z.R),5];pushPresence();return true}
function tntTick(z){if(z.t<z.T)return false;if(z.mine)aoe(z.x,z.y,z.r,z.d,null,z.flag);boomFx(z.x,z.y,z.r,true);return true}
function drawMine(c,z,t){const arm=z.t>=z.T,bl=arm&&Math.sin(t/160)>0;c.globalAlpha=z.mine?1:.7;c.fillStyle='rgba(0,0,0,.35)';ell(c,z.x,z.y+2,12,5);c.beginPath();c.ellipse(z.x,z.y-2,10,6.5,0,0,TAU);fs(c,'#3a4636');c.beginPath();c.ellipse(z.x,z.y-4,6,3.6,0,0,TAU);fs(c,'#56684e');c.fillStyle=bl?'#ff5a4a':'#7a2a24';circ(c,z.x,z.y-5,2.2);if(bl)glow(c,z.x,z.y-5,9,'#ff5a4a',.6);
  if(z.mine){c.strokeStyle='rgba(255,154,74,.3)';c.lineWidth=1.5;c.setLineDash([6,8]);c.beginPath();c.ellipse(z.x,z.y,z.R,z.R*.92,0,0,TAU);c.stroke();c.setLineDash([])}c.globalAlpha=1}
function drawTnt(c,z,t){const p=clamp(z.t/z.T,0,1),f=Math.min(1,z.t/.45),x=z.ox+(z.x-z.ox)*f,gy=z.oy+30+(z.y-z.oy-30)*f,y=gy-Math.sin(f*Math.PI)*90;
  c.fillStyle='rgba(255,90,74,'+(.06+.1*p)+')';ell(c,z.x,z.y,z.r,z.r*.92);c.strokeStyle='rgba(255,90,74,.7)';c.lineWidth=2;c.setLineDash([12,9]);c.lineDashOffset=-t/14;c.beginPath();c.ellipse(z.x,z.y,z.r,z.r*.92,0,0,TAU);c.stroke();c.setLineDash([]);c.lineDashOffset=0;c.beginPath();c.ellipse(z.x,z.y,z.r*p,z.r*.92*p,0,0,TAU);c.stroke();
  const w=38*(1+(f>=1?Math.sin(t/(90-50*p))*.05*(1+p):0)),bl=f>=1&&Math.sin(t/(110-70*p))>0;
  c.fillStyle='rgba(0,0,0,.35)';ell(c,x,gy+2,22,8);rr(c,x-w/2,y-w,w,w,4);fs(c,bl?'#fff3c4':'#c9433a');c.fillStyle='#f2ead8';c.fillRect(x-w/2+1.2,y-w*.64,w-2.4,w*.28);c.fillStyle='#2a2018';c.font='900 '+Math.round(w*.25)+'px sans-serif';c.textAlign='center';c.textBaseline='middle';c.fillText('TNT',x,y-w*.49);c.textBaseline='alphabetic';
  c.strokeStyle='#2a2018';c.lineWidth=2;c.lineCap='round';c.beginPath();c.moveTo(x,y-w);c.quadraticCurveTo(x+6,y-w-8,x+3,y-w-13);c.stroke();glow(c,x+3,y-w-13,8,'#ffd27a',.9)}
"""
HERO=r"""  }else if(o.cls===5){
    legs(c,wp,mv,S.cloth2,S.dark);
    rr(c,-13,-30+b,8,14,2.5);fs(c,'#7a5334');c.fillStyle='#c9433a';c.fillRect(-12,-33+b,2.4,5);c.fillRect(-8.6,-34+b,2.4,6);
    c.beginPath();c.moveTo(-8,-31+b);c.lineTo(8,-31+b);c.lineTo(11,-11);c.lineTo(-11,-11);c.closePath();fs(c,S.cloth);c.fillStyle=S.cloth2;c.fillRect(-10,-15,20,3);c.fillStyle=S.trim;circ(c,0,-25+b,1.6);circ(c,0,-20+b,1.6);
    c.beginPath();c.arc(0,-39+b,9.5,0,TAU);fs(c,S.cloth);c.beginPath();c.ellipse(1.5,-38+b,6.6,5.6,0,0,TAU);fs(c,S.dark);
    c.fillStyle=S.glow;circ(c,-.6,-38.5+b,2.7);circ(c,5,-38.5+b,2.7);c.fillStyle='#fff3c4';circ(c,-1.3,-39.3+b,.9);circ(c,4.3,-39.3+b,.9);
    c.strokeStyle='#2a2018';c.lineWidth=1.8;c.lineCap='round';c.beginPath();c.moveTo(-2,-48+b);c.quadraticCurveTo(-6,-55+b,-3-sway,-58+b);c.stroke();glow(c,-3-sway,-58+b,5+Math.sin(t/90)*1.5,'#ffd27a',.9);c.fillStyle='#fff3c4';circ(c,-3-sway,-58+b,1.5);
    const th=sp>=0?-2.2+sp*3:cp>=0?-1.9:la*.4-.2;c.save();c.translate(6,-25+b);c.rotate(th);c.strokeStyle=S.cloth2;c.lineWidth=4;c.lineCap='round';c.beginPath();c.moveTo(0,0);c.lineTo(11,0);c.stroke();
    c.beginPath();c.arc(15,0,5.2,0,TAU);fs(c,'#2a2f3a');c.fillStyle='rgba(255,255,255,.3)';circ(c,13.6,-1.6,1.4);c.strokeStyle='#8a6a4a';c.lineWidth=1.4;c.beginPath();c.moveTo(18,-4);c.lineTo(21,-7);c.stroke();glow(c,21,-7,4,'#ffd27a',.9);c.restore();
  }else{
    const hem=Math.sin(wp)*2*mv;"""
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    rep("[{t:'cone',r:280,h:.62},null]];","[{t:'cone',r:280,h:.62},null],[null,{t:'zone',r:210}]];")  # mira dos botões: sem esta linha os botões do Zero não respondiam
    rep("vira cura.'}}];","vira cura.'}},\n {n:'Zero',hp:470,dmg:24,range:66,itv:.8,spd:192,arm:2,proj:0,\n  s1:{n:'Mina',cd:5,d:'planta uma mina que os inimigos não veem (até 3 no chão). Explode quando alguém chega perto; cada inimigo atingido dá +6% de dano por 8 s (até +30%).'},s2:{n:'TNT Gigante',cd:60,d:'arremessa um TNT enorme que pisca e explode numa área grande. Suas explosões não ferem você nem aliados.'}}];")
    rep("blade:'#ff5a5a',glow:'#ff4a4a'}];","blade:'#ff5a5a',glow:'#ff4a4a'},\n {cloth:'#4f9a4a',cloth2:'#2f6b36',dark:'#1d2a1c',trim:'#e2b24c',glow:'#ff9a4a'}];")
    rep("empurra os inimigos para longe e fere mais.'}]];","empurra os inimigos para longe e fere mais.'}],\n [{n:'Mina Pesada',d:'Explosão maior e mais forte, que deixa lento; a mina dura 30 s.'},{n:'Campo Minado',d:'Planta duas minas de uma vez (até 4 no chão), cada uma com menos dano.'}]];")
    a=s.index('const TAL=[');b=s.index(']}]];',a)+3
    s=s[:b]+""",
 [{b:'Pólvora',n:[{id:'dmg',n:'Pavio Curto',m:3,d:'+8% de dano por ponto'},{id:'crit',n:'Faísca',m:3,d:'10% de chance de dano em dobro por ponto'},{id:'exec',n:'Demolidor',m:1,d:'+35% de dano em alvos com menos de 35% de vida'}]},
  {b:'Casca',n:[{id:'hp',n:'Casca Grossa',m:3,d:'+10% de vida por ponto'},{id:'spd',n:'Pés Ligeiros',m:3,d:'+5% de movimento por ponto'},{id:'dodge',n:'Esquiva',m:1,d:'20% de chance de evitar um golpe'}]},
  {b:'Arsenal',n:[{id:'s1',n:'Carga Extra',m:3,d:'+20% de dano da Mina por ponto'},{id:'cdr',n:'Mãos Rápidas',m:3,d:'-8% de recarga das habilidades por ponto'},{id:'ult',n:'Megaton',m:1,d:'TNT Gigante com área maior, que deixa os atingidos lentos'}]}]"""+s[b:]
    rep("const EDC=new Map();",FN+"const EDC=new Map();")
    rep("  else G.zones.push({kind:'slam',","  else if(kind==='mine'){const cap2=ev===2?4:3,my=G.zones.filter(z=>z.kind==='mine'&&z.by===a);if(my.length>=cap2)G.zones.splice(G.zones.indexOf(my[0]),1);G.zones.push({kind,x,y,by:a,r:46,R:ev===1?150:120,t:0,T:.7,d:0,bd:d,dur:ev===1?30:20,mine,flag:ev===1?1:0,col:'#ff9a4a'})}\n  else if(kind==='tnt')G.zones.push({kind,x,y,ox:a.x,oy:a.y-30,r:cap?250:210,t:0,T:1.4,d,mine,flag:cap?1:0,col:'#ff5a4a'});\n  else G.zones.push({kind:'slam',")
    rep("  else{if(!k)mkZone('nova',x,y,mine,","  else if(cls===5){\n    if(!k){if(mine||ally(o)){const n=ev===2?2:1;for(let j=0;j<n;j++){const q=n>1?(j?34:-34):0;mkZone('mine',clamp(x-Math.sin(ang)*q,TILE,WORLD-TILE),clamp(y+Math.cos(ang)*q,TILE,WORLD-TILE),mine,m*(ev===1?3.6:ev===2?2.2:3)*s1m,false,o,null,ev)}}if(mine)burst(o.x,o.y-6,6,'#56684e',90,.3,3)}\n    else{mkZone('tnt',x,y,mine,m*8,k===2,o);burst(o.x,o.y-40,8,'#ffd27a',120,.4,3)}}\n  else{if(!k)mkZone('nova',x,y,mine,")
    rep("const zone=H.cls===2||(H.cls===1&&i),","const zone=H.cls===2||((H.cls===1||H.cls===5)&&i),")
    rep("for(let i=G.zones.length-1;i>=0;i--){const z=G.zones[i];z.t+=dt;","for(let i=G.zones.length-1;i>=0;i--){const z=G.zones[i];z.t+=dt;if(z.kind==='mine'||z.kind==='tnt'){if(z.t>=0&&(z.kind==='mine'?mineTick(z):tntTick(z)))G.zones.splice(i,1);continue}")
    rep("for(const z of G.zones){if(z.t<0)continue;const p=clamp(z.t/z.T,0,1),on=z.t>=z.T;","for(const z of G.zones){if(z.t<0)continue;if(z.kind==='mine'){drawMine(ctx,z,t);continue}if(z.kind==='tnt'){drawTnt(ctx,z,t);continue}const p=clamp(z.t/z.T,0,1),on=z.t>=z.T;")
    rep("let d=base*(e<H.fury?2:1)*(e<H.wrath?1.3:1)*(e<H.bless?1.25:1);","let d=base*(e<H.fury?2:1)*(e<H.wrath?1.3:1)*(e<H.bless?1.25:1)*(e<H.boomT?1+.06*H.boomN:1);")
    rep("slow:0,chill:0,root:0,free:0,","slow:0,chill:0,root:0,boomN:0,boomT:0,free:0,")
    rep("const kr=clamp(num(s.sx[4])|0,0,4),k=kr>=3?0:kr;o.ct=o.ctD=k?.8:.4;o.ck=k?1:0;\n      doSkill(o,o.cls,k,clamp(num(s.sx[1]),0,WORLD),clamp(num(s.sx[2]),0,WORLD),num(s.sx[3])/100,false,0,1,kr>=3?kr-2:0)}",
        "const kr=clamp(num(s.sx[4])|0,0,5),k=kr>=3?0:kr,sx1=clamp(num(s.sx[1]),0,WORLD),sy1=clamp(num(s.sx[2]),0,WORLD);\n      if(kr===5){const zi=G.zones.findIndex(z=>z.kind==='mine'&&!z.mine&&Math.hypot(z.x-sx1,z.y-sy1)<24);if(zi>=0)G.zones.splice(zi,1);boomFx(sx1,sy1,clamp(num(s.sx[3]),60,200))}\n      else{o.ct=o.ctD=k?.8:.4;o.ck=k?1:0;doSkill(o,o.cls,k,sx1,sy1,num(s.sx[3])/100,false,0,1,kr>=3?kr-2:0)}}")
    rep("  }else{\n    const hem=Math.sin(wp)*2*mv;",HERO)
    rep('<b>Sombrio</b><span>Corpo a corpo, puxa e rouba vida</span></label>','<b>Sombrio</b><span>Corpo a corpo, puxa e rouba vida</span></label>\n          <input type="radio" name="hero" id="hero5" value="5"><label for="hero5"><canvas width="160" height="168" id="ic5"></canvas><b>Zero</b><span>Minas invisíveis e TNT gigante</span></label>')
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok (patch27)')
