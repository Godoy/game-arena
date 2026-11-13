# roda por último: tema A Convergência também no desenho por código (versão de gráfico simples): sem asas nem auréola
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    rep("  else if(o.lv>=4)wings(c,o.lv,t,ult?Math.sin(cp*Math.PI):(o.bf&8)?.5:0);","  else if(o.lv>=4)glow(c,0,-22,26+Math.min(16,o.lv),S.glow||'#ffe9a0',.24+.1*Math.sin(t/400)+(ult?.3:0));")
    rep("glow(c,0,hy+b,14,'#e2b24c',.5);c.strokeStyle='#e2b24c';c.lineWidth=2.4;c.beginPath();c.ellipse(0,hy+b,9,3.2,0,0,TAU);c.stroke()}","for(let j=0;j<3;j++){const a=t/900+j*TAU/3,x=Math.cos(a)*22,y=hy+18+b+Math.sin(a)*6;glow(c,x,y,8,S.glow||'#ffe9a0',.45);c.fillStyle='#ffffff';c.beginPath();c.moveTo(x,y-6);c.lineTo(x+3,y);c.lineTo(x,y+6);c.lineTo(x-3,y);c.closePath();c.fill()}}")
    a=s.index("  for(const s of[-1,1])for(let i=0;i<3;i++){c.save();c.scale(s,1);c.translate(10,-70+i*4);");b=s.index("c.stroke();c.restore()}\n",a)+len("c.stroke();c.restore()}\n");s=s[:a]+s[b:]  # Guardião do Núcleo sem asas
    rep("  glow(c,0,-131,22,'#e2b24c',.4);c.strokeStyle='#e2b24c';c.lineWidth=3.5;c.beginPath();c.ellipse(0,-131,17,5.5,0,.5,5.4);c.stroke();\n","")  # nem auréola
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok (patch22)')
