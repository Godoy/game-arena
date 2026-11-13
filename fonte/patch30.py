# novo herói (v1): Sentinela, robô blindado de longo alcance. Lento e resistente, tiro rápido e fraco.
# Raio Perfurante: linha longa que atravessa e deixa um pouco lento. Modo Cerco (6 s): atira 80% mais rápido, +70 de alcance,
# -30% de dano sofrido, metade da velocidade. bf: 256 = cerco, 512 = escudo (evolução Protocolo de Proteção).
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
HERO=r"""  }else if(o.cls===7){const eye=(o.bf&256)?'#ff5a4a':S.glow;
    legs(c,wp,mv,S.metal2,S.dark);
    rr(c,-9,-32+b,18,20,4);fs(c,S.metal);c.fillStyle=S.metal2;c.fillRect(-8,-17+b,16,3);c.fillStyle='rgba(255,255,255,.25)';c.fillRect(-7,-30+b,4,13);
    c.beginPath();c.arc(1,-24+b,3.2,0,TAU);fs(c,S.dark);c.fillStyle=eye;circ(c,1,-24+b,1.8);glow(c,1,-24+b,7,eye,.5);
    for(const sd of[-1,1]){c.beginPath();c.arc(sd*10.5,-30+b,4.2,0,TAU);fs(c,S.cloth)}
    c.strokeStyle=OUT;c.lineWidth=1.6;c.lineCap='round';c.beginPath();c.moveTo(-3,-47+b);c.lineTo(-5,-54+b);c.stroke();c.fillStyle=eye;circ(c,-5,-55+b,1.7);
    rr(c,-7,-47+b,14,13,5);fs(c,S.metal);rr(c,-3,-43+b,11,5,2.5);fs(c,S.dark);c.fillStyle=eye;circ(c,4.5,-40.5+b,2);glow(c,4.5,-40.5+b,8,eye,.7);
    const th=sp>=0?la:cp>=0?la:la*.6,rc=sp>=0?Math.sin(sp*Math.PI)*3:0;c.save();c.translate(7,-27+b);c.rotate(th);
    rr(c,-2-rc,-3.4,17,6.8,2.5);fs(c,S.cloth);rr(c,13-rc,-2.4,8,4.8,1.5);fs(c,S.dark);c.fillStyle=eye;c.fillRect(19.5-rc,-1.2,2,2.4);if(sp>=0&&sp<.4)glow(c,23,0,9,eye,.9);if(cp>=0)glow(c,23,0,12,eye,.8);c.restore();
  }else{
    const hem=Math.sin(wp)*2*mv;"""
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    rep("acelera os aliados próximos por 3 s.'}}];","acelera os aliados próximos por 3 s.'}},\n {n:'Sentinela',hp:540,dmg:16,range:210,itv:.42,spd:172,arm:3,proj:7,\n  s1:{n:'Raio Perfurante',cd:8,d:'dispara um raio reto e longo que atravessa todos os inimigos na linha e os deixa um pouco lentos.'},s2:{n:'Modo Cerco',cd:60,d:'por 6 s você atira 80% mais rápido, alcança mais longe e sofre 30% menos dano, mas anda à metade da velocidade.'}}];")
    rep("stripe:'#e39a4c'}];","stripe:'#e39a4c'},\n {metal:'#aab4c8',metal2:'#6f7a94',dark:'#1c2233',trim:'#e2b24c',glow:'#7fe3ff',cloth:'#39445e'}];")
    rep("acelera os aliados próximos por 3 s.'}]];","acelera os aliados próximos por 3 s.'}],\n [{n:'Sobrecarga',d:'Raio mais largo, mais longo e com 40% mais dano.'},{n:'Protocolo de Proteção',d:'Raio mais fraco, mas você ganha um escudo (40% menos dano por 3 s) e cura 6% da vida dos aliados próximos.'}]];")
    rep("[{t:'cone',r:200,h:.55},null]];","[{t:'cone',r:200,h:.55},null],[{t:'cone',r:420,h:.07},null]];")
    a=s.index('const TAL=[');b=s.index(']}]];',a)+3
    s=s[:b]+""",
 [{b:'Arsenal',n:[{id:'dmg',n:'Calibre Pesado',m:3,d:'+8% de dano por ponto'},{id:'crit',n:'Mira Assistida',m:3,d:'10% de chance de dano em dobro por ponto'},{id:'exec',n:'Sentença',m:1,d:'+35% de dano em alvos com menos de 35% de vida'}]},
  {b:'Blindagem',n:[{id:'hp',n:'Chapa Reforçada',m:3,d:'+10% de vida por ponto'},{id:'ward',n:'Campo Defletor',m:3,d:'-6% de dano sofrido por ponto'},{id:'aegis',n:'Reinício de Emergência',m:1,d:'Com menos de 30% de vida, fica invulnerável por 2 s (uma vez por minuto)'}]},
  {b:'Sistemas',n:[{id:'s1',n:'Capacitor',m:3,d:'+20% de dano do Raio por ponto'},{id:'cdr',n:'Resfriamento',m:3,d:'-8% de recarga das habilidades por ponto'},{id:'ult',n:'Cerco Total',m:1,d:'Modo Cerco dura 3 s a mais'}]}]"""+s[b:]
    rep("PK={2:'#8fd8f5',","PK={7:'#7fe3ff',2:'#8fd8f5',")
    rep("spd:k===1?720:k===6?640:520,k,mine:true","spd:k===1?720:k===6?640:k===7?950:520,k,mine:true")
    rep("spd:o.cls===1?720:o.cls===3?640:520,","spd:o.cls===1?720:o.cls===3?640:o.cls===7?950:520,")
    rep("if(H.cls===6&&H.rapOn){H.range=70;H.spd*=1.3;H.itv/=1.3;H.dmg*=1.15}}","if(H.cls===6&&H.rapOn){H.range=70;H.spd*=1.3;H.itv/=1.3;H.dmg*=1.15}if(H.cls===7&&H.siOn){H.itv/=1.8;H.range+=70;H.spd*=.5}}")
    rep("|(H.rapOn?128:0);","|(H.rapOn?128:0)|(H.siOn?256:0)|(e<H.shield?512:0);{const si=H.cls===7&&e<H.siege&&!H.dead;if(si!==!!H.siOn){H.siOn=si;stats()}}")
    rep("rap:0,rapOn:false,","rap:0,rapOn:false,siege:0,siOn:false,shield:0,")
    rep("*(e<H.wrath?.65:1)*(by&&G.mod===6?1.4:1)","*(e<H.wrath?.65:1)*(e<H.siege?.7:1)*(e<H.shield?.6:1)*(by&&G.mod===6?1.4:1)")
    rep("  if(H.cls===6){H.rap=e+","  if(H.cls===7){if(i){H.siege=e+6000+3000*tr('ult');if(!H.siOn){H.siOn=true;stats()}}else if(H.evo===2){H.shield=e+3000;for(const a of G.allies)if(Math.hypot(a.x-H.x,a.y-H.y)<240)allyFx(a,9,6)}}\n  if(H.cls===6){H.rap=e+")
    rep("  else if(cls===6){\n","  else if(cls===7){\n    if(!k){const L=ev===1?460:420,hf=ev===1?.12:.07;if(mine)cone(o.x,o.y,ang,L,hf,m*(ev===1?5.8:ev===2?3.2:4.2)*s1m,2);fx('cone',o.x,o.y,{a:ang,r:L,half:hf,T:.3,col:'#7fe3ff'});for(let q=1;q<16;q++)part(o.x+Math.cos(ang)*q*L/16,o.y-26+Math.sin(ang)*q*L/16,0,-10,.3+q*.015,ev===1?6:4.5,q%2?'#7fe3ff':'#ffffff');\n      G.proj.push({x:o.x,y:o.y-27,t:null,tx:o.x+Math.cos(ang)*L,ty:o.y-27+Math.sin(ang)*L,d:0,spd:1700,k:7,mine:false,a:ang,w:0});if(ev===2){fx('ring',o.x,o.y,{r:240,T:.5,col:'#7fe3ff'});fx('circle',o.x,o.y,{r:60,T:.8,col:'#7fe3ff'})}shake(3)}\n    else{fx('ring',o.x,o.y,{r:90,T:.5,col:'#ff5a4a'});fx('circle',o.x,o.y,{r:110,T:1.2,col:'#ff9a4a'});burst(o.x,o.y-24,16,'#ff9a4a',200,.6,4);shake(5)}}\n  else if(cls===6){\n")
    rep("  if(o.bf&64)netFx(c,o.x,o.y-26,19);","  if(o.bf&512){c.strokeStyle='rgba(127,227,255,.8)';c.lineWidth=2;c.beginPath();c.ellipse(o.x,o.y-26,24,34,0,0,TAU);c.stroke();glow(c,o.x,o.y-26,36,'#7fe3ff',.2)}\n  if(o.bf&256){c.strokeStyle='rgba(255,90,74,.75)';c.lineWidth=2;c.setLineDash([8,6]);c.beginPath();c.ellipse(o.x,o.y,27,10.5,0,0,TAU);c.stroke();c.setLineDash([])}\n  if(o.bf&64)netFx(c,o.x,o.y-26,19);")
    rep("  }else{\n    const hem=Math.sin(wp)*2*mv;",HERO)
    rep('<b>Garra</b><span>Metamorfa: lança de longe, vira raptor</span></label>','<b>Garra</b><span>Metamorfa: lança de longe, vira raptor</span></label>\n          <input type="radio" name="hero" id="hero7" value="7"><label for="hero7"><canvas width="160" height="168" id="ic7"></canvas><b>Sentinela</b><span>Robô blindado: tiro rápido e raio</span></label>')
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok (patch30)')
