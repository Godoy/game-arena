# novo herói (v1): Garra, a metamorfa. Forma humana: lança de longe. Bote do Raptor: vira raptor por 6 s e salta à frente.
# Como raptor: corpo a corpo, 30% mais rápida (andar e atacar), +15% de dano. Rugido Alfa: dano e lentidão em volta, acelera aliados.
# Estado da forma viaja no bit 128 de bf. Raptor de desenho próprio (escamas verdes, listras e crista laranja).
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
HERO=r"""  }else if(o.cls===6){
    if(o.bf&128){const bt=sp>=0?Math.sin(sp*Math.PI):0,tl=[[-8,-22+b],[-24,-24+b],[-35,-15+b+sway]];
      for(const[col,w]of[[OUT,9],[S.scale,6.5]]){c.strokeStyle=col;c.lineWidth=w;c.lineCap='round';c.beginPath();c.moveTo(tl[0][0],tl[0][1]);c.quadraticCurveTo(tl[1][0],tl[1][1],tl[2][0],tl[2][1]);c.stroke()}
      for(const sd of[-1,1]){const ph=wp+(sd>0?0:Math.PI),dx=Math.sin(ph)*7*mv,dy=-Math.max(0,Math.cos(ph))*4*mv;for(const[col,w]of[[OUT,6],[S.scale2,4]]){c.strokeStyle=col;c.lineWidth=w;c.lineJoin='round';c.beginPath();c.moveTo(-2+sd*2,-16+b);c.lineTo(-5+sd*2+dx*.4,-8+dy);c.lineTo(1+sd*2+dx,-1+dy);c.lineTo(5+sd*2+dx,-1+dy);c.stroke()}}
      c.beginPath();c.ellipse(0,-22+b,14,9,-.15,0,TAU);fs(c,S.scale);c.fillStyle='rgba(255,255,255,.16)';ell(c,1,-17.5+b,9,3);
      c.strokeStyle=S.stripe;c.lineWidth=2.2;c.lineCap='round';for(const q of[-8,-2,4]){c.beginPath();c.moveTo(q,-30+b);c.lineTo(q-2,-24+b);c.stroke()}
      c.strokeStyle=S.scale2;c.lineWidth=3;c.beginPath();c.moveTo(8,-19+b);c.lineTo(13,-14+b-bt*4);c.stroke();
      c.save();c.translate(10,-28+b);c.rotate(-.5+la*.35-bt*.3);for(const[col,w]of[[OUT,9],[S.scale,6.5]]){c.strokeStyle=col;c.lineWidth=w;c.beginPath();c.moveTo(0,0);c.lineTo(9,-7);c.stroke()}
      c.translate(9,-8);c.rotate(.5);c.fillStyle=S.stripe;tri(c,-4,-5,-10,-10,-1,-5.5);tri(c,-1,-5.5,-5,-12,3,-5);
      c.save();c.rotate(.12+bt*.55+(cp>=0?.6:0));c.beginPath();c.moveTo(-2,1);c.lineTo(12,2);c.lineTo(11,4.6);c.lineTo(-2,4);c.closePath();fs(c,S.scale2);c.restore();
      c.beginPath();c.moveTo(-4,-5);c.lineTo(12,-3.5);c.lineTo(14.5,0);c.lineTo(-3,1.2);c.closePath();fs(c,S.scale);c.fillStyle=S.bone;for(const q of[4,7,10])tri(c,q,.6,q+1.6,.6,q+.8,2.8);
      c.fillStyle='#fff3c4';circ(c,3,-2.2,1.6);c.fillStyle='#1a1410';circ(c,3.5,-2.2,.75);c.restore();
    }else{legs(c,wp,mv,S.cloth2,S.dark);
      c.beginPath();c.moveTo(-7,-31+b);c.lineTo(7,-31+b);c.lineTo(9,-12);c.lineTo(-9,-12);c.closePath();fs(c,S.cloth);c.fillStyle=S.scale;c.fillRect(-8.5,-17,17,3.4);c.fillStyle=S.bone;for(const q of[-5,0,5])tri(c,q-1.7,-28+b,q+1.7,-28+b,q,-23.5+b);
      c.beginPath();c.arc(0,-38+b,7,0,TAU);fs(c,S.skin);c.fillStyle=S.dark;circ(c,2.6,-38+b,1.1);circ(c,5.6,-38+b,1);
      c.fillStyle=S.stripe;tri(c,-7,-47+b,-14-sway,-53+b,-4,-49+b);tri(c,-8,-43+b,-16-sway,-45+b,-7,-46.5+b);
      c.beginPath();c.moveTo(-8,-39+b);c.quadraticCurveTo(-7,-50+b,3,-48+b);c.lineTo(13,-43+b);c.lineTo(11,-40.5+b);c.lineTo(-8,-41+b);c.closePath();fs(c,S.bone);c.fillStyle=S.dark;circ(c,4,-44.6+b,1.5);
      const th=sp>=0?-2.4+sp*2.8:cp>=0?-1.2:-.5+la*.3;c.save();c.translate(6,-26+b);c.rotate(th);c.strokeStyle=OUT;c.lineWidth=4;c.lineCap='round';c.beginPath();c.moveTo(-12,0);c.lineTo(20,0);c.stroke();c.strokeStyle='#8a6a4a';c.lineWidth=2.2;c.beginPath();c.moveTo(-12,0);c.lineTo(20,0);c.stroke();c.fillStyle=S.bone;tri(c,19,-3.6,28,0,19,3.6);c.fillStyle=S.skin;circ(c,2,0,3);c.restore()}
  }else{
    const hem=Math.sin(wp)*2*mv;"""
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    rep("não ferem você nem aliados.'}}];","não ferem você nem aliados.'}},\n {n:'Garra',hp:450,dmg:26,range:200,itv:.8,spd:190,arm:1,proj:1,\n  s1:{n:'Bote do Raptor',cd:10,d:'vira raptor por 6 s e salta à frente rasgando quem está no caminho. Como raptor você luta corpo a corpo, anda e ataca 30% mais rápido e causa 15% mais dano.'},s2:{n:'Rugido Alfa',cd:60,d:'vira raptor por 8 s e ruge: fere e deixa lentos os inimigos em volta e acelera os aliados próximos por 3 s.'}}];")
    rep("glow:'#ff9a4a'}];","glow:'#ff9a4a'},\n {cloth:'#8a5a2e',cloth2:'#5e3c1f',dark:'#2a1d12',trim:'#e2b24c',glow:'#9fd86a',skin:'#d9a878',bone:'#efe6cf',scale:'#5f8f4a',scale2:'#3f6a38',stripe:'#e39a4c'}];")
    rep("cada uma com menos dano.'}]];","cada uma com menos dano.'}],\n [{n:'Emboscada',d:'Bote mais longo e com 45% mais dano.'},{n:'Matilha',d:'Bote mais fraco, mas cura 8% da sua vida e acelera os aliados próximos por 3 s.'}]];")
    rep("[null,{t:'zone',r:210}]];","[null,{t:'zone',r:210}],[{t:'cone',r:200,h:.55},null]];")
    a=s.index('const TAL=[');b=s.index(']}]];',a)+3
    s=s[:b]+""",
 [{b:'Presa',n:[{id:'dmg',n:'Garras Afiadas',m:3,d:'+8% de dano por ponto'},{id:'crit',n:'Ponto Fraco',m:3,d:'10% de chance de dano em dobro por ponto'},{id:'exec',n:'Predadora',m:1,d:'+35% de dano em alvos com menos de 35% de vida'}]},
  {b:'Instinto',n:[{id:'spd',n:'Passada Larga',m:3,d:'+5% de movimento por ponto'},{id:'aspd',n:'Frenesi',m:3,d:'+8% de velocidade de ataque por ponto'},{id:'dodge',n:'Reflexo',m:1,d:'20% de chance de evitar um golpe'}]},
  {b:'Matilha',n:[{id:'s1',n:'Bote Feroz',m:3,d:'+20% de dano do Bote por ponto'},{id:'cdr',n:'Faro',m:3,d:'-8% de recarga das habilidades por ponto'},{id:'ult',n:'Alfa',m:1,d:'Rugido Alfa com área maior, e a forma de raptor dele dura 4 s a mais'}]}]"""+s[b:]
    rep("H.range=c.range}","H.range=c.range;if(H.cls===6&&H.rapOn){H.range=70;H.spd*=1.3;H.itv/=1.3;H.dmg*=1.15}}")
    rep("|(e<H.root?64:0);","|(e<H.root?64:0)|(H.rapOn?128:0);{const rp=H.cls===6&&e<H.rap&&!H.dead;if(rp!==!!H.rapOn){H.rapOn=rp;stats();burst(H.x,H.y-24,12,'#9fd86a',160,.5,4)}}")
    rep("boomN:0,boomT:0,","boomN:0,boomT:0,rap:0,rapOn:false,")
    rep("  if(C.proj===0){dealt(t,d,0,crit);","  if(C.proj===0||H.rapOn){dealt(t,d,0,crit);")
    rep("if(CLS[o.cls].proj===0)fx('slash',x,y-26,","if(CLS[o.cls].proj===0||(o.bf&128))fx('slash',x,y-26,")
    rep("  doSkill(H,H.cls,k,px,py,ang,true,outDmg(null,H.dmg),1+.2*tr('s1'),i?0:H.evo);","  if(H.cls===6){H.rap=e+(i?8000+4000*tr('ult'):6000);if(!H.rapOn){H.rapOn=true;stats()}if(!i){const v=H.evo===1?800:640;H.dash={vx:Math.cos(ang)*v,vy:Math.sin(ang)*v,t:.25};if(H.evo===2){H.hp=Math.min(H.mhp,H.hp+H.mhp*.08);for(const a of G.allies)if(Math.hypot(a.x-H.x,a.y-H.y)<240)allyFx(a,8,0)}}else for(const a of G.allies)if(Math.hypot(a.x-H.x,a.y-H.y)<260)allyFx(a,8,0)}\n  doSkill(H,H.cls,k,px,py,ang,true,outDmg(null,H.dmg),1+.2*tr('s1'),i?0:H.evo);")
    rep("  else if(cls===5){\n","  else if(cls===6){\n    if(!k){const L=ev===1?250:200;if(mine)cone(o.x,o.y,ang,L,.55,m*(ev===1?3.2:ev===2?1.8:2.2)*s1m,0);fx('cone',o.x,o.y,{a:ang,r:L,half:.55,T:.3,col:'#ffb36a'});fx('ring',o.x,o.y,{r:46,T:.35,col:'#9fd86a'});burst(o.x,o.y-24,14,'#9fd86a',200,.5,4);for(let j=0;j<3;j++)fx('slash',o.x+Math.cos(ang)*(50+j*42),o.y-26+Math.sin(ang)*(50+j*42),{a:ang+(j-1)*.3,T:.25+j*.06,col:'#fff3c4',s:1.2});if(ev===2)fx('ring',o.x,o.y,{r:240,T:.5,col:'#9fd86a'});shake(4)}\n    else{const R=k===2?270:220;if(mine)aoe(o.x,o.y,R,m*4,null,1);fx('ring',o.x,o.y,{r:R,T:.6,col:'#ffb36a'});fx('ring',o.x,o.y,{r:R*.66,T:.8,col:'#fff3c4'});fx('ring',o.x,o.y,{r:R*.33,T:1,col:'#ffb36a'});fx('flash',o.x,o.y,{r:R,T:.3,col:'#ffd27a'});burst(o.x,o.y-30,24,'#ffb36a',300,.7,5);shake(9)}}\n  else if(cls===5){\n")
    rep("  }else{\n    const hem=Math.sin(wp)*2*mv;",HERO)
    rep('<b>Zero</b><span>Minas invisíveis e TNT gigante</span></label>','<b>Zero</b><span>Minas invisíveis e TNT gigante</span></label>\n          <input type="radio" name="hero" id="hero6" value="6"><label for="hero6"><canvas width="160" height="168" id="ic6"></canvas><b>Garra</b><span>Metamorfa: lança de longe, vira raptor</span></label>')
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok (patch29)')
