# roda por último (versão de gráfico simples): vida nas criaturas (respirar, esticar no ataque, recuar ao apanhar, surgir crescendo),
# estilhaços flutuando atrás do Guardião do Núcleo, golpe dos heróis com mais peso e efeitos (corte, cone, anel) mais desenhados.
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    rep("c.scale(dir,1);\n  const AM=ART['m'+k.kd],CA=ANIM['m'+k.kd];","c.scale(dir,1);\n  const AM=ART['m'+k.kd],CA=ANIM['m'+k.kd];\n  if(!AM&&!CA){const at=sp>=0?Math.sin(sp*Math.PI):0,br=still()?0:Math.sin(t/360+k.hx*.07)*.035*(1-mv),hf=k.flash>0?Math.min(1,k.flash*8):0,bn=k.born>0?Math.min(1,k.born/.5):0,z=1-bn*.45;c.rotate(at*.1-hf*.12);c.scale((1+at*.1-br+hf*.06)*z,(1-at*.07+br-hf*.08)*z)}")
    rep("  c.fillStyle='#3a1420';c.beginPath();c.moveTo(-18,-62);c.lineTo(18,-62);","  for(const sd of[-1,1])for(let i=0;i<3;i++){const a=-.2-i*.4+fl*.05*(i+1),R=50+i*6,x=sd*Math.cos(a)*R,y=-74+Math.sin(a)*R+Math.sin(t/300+i*1.7)*2.5;glow(c,x,y,13,'#ff7a4a',.28);c.save();c.translate(x,y);c.rotate(sd*(1.1-i*.4));c.beginPath();c.moveTo(0,-17+i*2);c.lineTo(5.5,0);c.lineTo(0,17-i*2);c.lineTo(-5.5,0);c.closePath();fs(c,i===0?'#ff9a5a':i===1?'#c2453c':'#8a2c34');c.fillStyle='rgba(255,255,255,.25)';tri(c,0,-17+i*2,-5.5,0,0,0);c.restore()}\n  c.fillStyle='#3a1420';c.beginPath();c.moveTo(-18,-62);c.lineTo(18,-62);")
    rep("?Math.sin(sp*Math.PI)*4:0,ult?-7*Math.sin(cp*Math.PI):0);","?Math.sin(sp*Math.PI)*4:0,ult?-7*Math.sin(cp*Math.PI):0);if(!AIH&&sp>=0){const at=Math.sin(sp*Math.PI);c.rotate(at*.08);c.scale(1+at*.07,1-at*.05)}")
    rep("ctx.arc(-15,0,22+p*6,1,-1,true);ctx.closePath();ctx.fill();ctx.restore()}","ctx.arc(-15,0,22+p*6,1,-1,true);ctx.closePath();ctx.fill();ctx.fillStyle='#ffffff';ctx.globalAlpha=(1-p)*.5;ctx.beginPath();ctx.arc(-9,0,21+p*6,-.8,.8);ctx.arc(-12.5,0,21+p*6,.74,-.74,true);ctx.closePath();ctx.fill();ctx.restore()}")
    rep("ctx.arc(f.x,f.y,f.r*(.5+.5*p),f.a-f.half,f.a+f.half);ctx.closePath();ctx.fill()}","ctx.arc(f.x,f.y,f.r*(.5+.5*p),f.a-f.half,f.a+f.half);ctx.closePath();ctx.fill();ctx.globalAlpha=(1-p)*.8;ctx.strokeStyle=f.col;ctx.lineCap='round';ctx.lineWidth=3;ctx.beginPath();ctx.arc(f.x,f.y,f.r*(.5+.5*p),f.a-f.half,f.a+f.half);ctx.stroke();ctx.lineWidth=1.6;ctx.beginPath();ctx.arc(f.x,f.y,f.r*(.5+.5*p)*.72,f.a-f.half*.8,f.a+f.half*.8);ctx.stroke()}")
    rep("      ctx.lineWidth=5*(1-p)+1;ctx.beginPath();ctx.ellipse(f.x,f.y,R,R*.92,0,0,TAU);ctx.stroke()}","      ctx.lineWidth=5*(1-p)+1;ctx.beginPath();ctx.ellipse(f.x,f.y,R,R*.92,0,0,TAU);ctx.stroke();if(f.r>=40){ctx.lineCap='round';ctx.lineWidth=2.6*(1-p)+.6;ctx.beginPath();for(let j=0;j<10;j++){const a=j*TAU/10+f.x*.013;ctx.moveTo(f.x+Math.cos(a)*R*1.07,f.y+Math.sin(a)*R*.98);ctx.lineTo(f.x+Math.cos(a)*R*1.2,f.y+Math.sin(a)*R*1.1)}ctx.stroke()}}")
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok (patch25)')
