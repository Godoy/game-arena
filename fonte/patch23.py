# roda por último: melhora o visual desenhado por código (versão de gráfico simples), mantendo o traço plano:
# chão com piso de lajes / grama / terra menos repetitivos, bordas onduladas entre terrenos (com cantos),
# sombra de bloco mais leve e árvores que balançam. Na v2 (arte pintada) o chão pintado continua valendo.
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
FL=r"""  const sh=(b,d)=>'rgb('+b.map(v=>Math.max(0,Math.min(255,Math.round(v+d)))).join(',')+')';
  const blot=(x,n,a)=>{for(let j=0;j<n;j++){const cx=11+r()*26,cy=11+r()*26,rad=8+r()*8,dk=r()<.5,c=dk?'0,0,0':'255,255,255',g=x.createRadialGradient(cx,cy,0,cx,cy,rad);g.addColorStop(0,'rgba('+c+','+(dk?a:a*.55)+')');g.addColorStop(1,'rgba('+c+',0)');x.fillStyle=g;x.fillRect(cx-rad,cy-rad,rad*2,rad*2)}};
  const tuft=(x,gx,gy,h,col)=>{x.strokeStyle=col;x.lineWidth=1.5;x.lineCap='round';x.beginPath();x.moveTo(gx,gy);x.lineTo(gx-2.6,gy-h*.8);x.moveTo(gx,gy);x.lineTo(gx,gy-h);x.moveTo(gx,gy);x.lineTo(gx+2.6,gy-h*.75);x.stroke()};
  SPR.fl=BIO.map((b,bi)=>[0,1,2,3,4,5].map(v=>mk(TILE,TILE,x=>{x.fillStyle=sh(b,0);x.fillRect(0,0,TILE,TILE);
    if(bi===0){x.fillStyle=sh(b,-15);x.fillRect(0,0,TILE,TILE);const mx=19+r()*10,my=19+r()*10;
      for(const[ax,ay,bx,by]of[[0,0,mx,my],[mx,0,TILE,my],[0,my,mx,TILE],[mx,my,TILE,TILE]]){rr(x,ax+1.2,ay+1.2,bx-ax-2.4,by-ay-2.4,5);x.fillStyle=sh(b,-4+r()*9);x.fill();x.fillStyle='rgba(255,255,255,.055)';rr(x,ax+3,ay+2.4,bx-ax-6,2.6,1.3);x.fill()}
      blot(x,2,.08);
      if(v===4){x.strokeStyle='rgba(0,0,0,.26)';x.lineWidth=1.1;x.lineCap='round';x.beginPath();const ox=8+r()*10,oy=8+r()*8;x.moveTo(ox,oy);x.lineTo(ox+11,oy+12);x.lineTo(ox+8,oy+24);x.moveTo(ox+11,oy+12);x.lineTo(ox+24,oy+16);x.stroke();tuft(x,10+r()*28,TILE-4,4,'#3f7a5a')}
      if(v===5){x.fillStyle='rgba(226,178,76,.24)';poly(x,[[24,11],[27,21],[37,24],[27,27],[24,37],[21,27],[11,24],[21,21]]);x.fill()}}
    else if(bi===1){blot(x,3,.1);for(let j=0;j<(v>=4?7:3);j++)tuft(x,6+r()*36,13+r()*31,4+r()*3.5,r()<.5?'#4f9f78':'#2c6a50');
      if(v===4)for(let j=0;j<5;j++){x.fillStyle='rgba(120,200,150,.5)';circ(x,14+r()*20,14+r()*20,1.3+r())}
      if(v===5)for(let j=0;j<3;j++){const gx=9+r()*30,gy=12+r()*27;x.strokeStyle='#2c6a50';x.lineWidth=1.2;x.beginPath();x.moveTo(gx,gy);x.lineTo(gx,gy+4);x.stroke();x.fillStyle=['#ffd27a','#f2ead8','#ff9ac0'][j];circ(x,gx,gy,2.2);x.fillStyle='rgba(255,255,255,.75)';circ(x,gx-.5,gy-.5,.8)}}
    else{blot(x,3,.11);for(let j=0;j<(v>=4?6:1+(v&1));j++){const gx=7+r()*34,gy=7+r()*34,w=1.6+r()*2.6;x.fillStyle='rgba(0,0,0,.26)';ell(x,gx+.6,gy+1,w,w*.7);x.fillStyle=r()<.5?'#a8928a':'#6e5e60';ell(x,gx,gy,w,w*.7);x.fillStyle='rgba(255,255,255,.18)';ell(x,gx-w*.3,gy-w*.25,w*.4,w*.25)}
      if(v===5){tuft(x,12+r()*24,20+r()*20,5,'#5a8f5e');tuft(x,12+r()*24,20+r()*20,4,'#3f7a5a')}
      if(v===4){x.strokeStyle='rgba(40,28,26,.45)';x.lineWidth=1.6;x.lineCap='round';x.beginPath();const ox=10+r()*14,oy=14+r()*18;x.moveTo(ox,oy);x.lineTo(ox+12,oy+4);x.moveTo(ox+7,oy+2.4);x.lineTo(ox+10,oy-3);x.stroke()}}})));
  const wav=u=>7+2.6*Math.sin(u/TILE*TAU*2+1)+1.4*Math.sin(u/TILE*TAU*3+2),turn=(x,q)=>{x.translate(TILE/2,TILE/2);x.rotate(q*Math.PI/2);x.translate(-TILE/2,-TILE/2)};
  SPR.ed=BIO.map(b=>[0,1,2,3].map(dir=>mk(TILE,TILE,x=>{turn(x,dir);
    x.beginPath();for(let u=-1;u<=TILE+1;u+=2)u<0?x.moveTo(u,wav(u)+1.2):x.lineTo(u,wav(u)+1.2);x.strokeStyle='rgba(8,10,20,.3)';x.lineWidth=2.4;x.stroke();
    x.beginPath();x.moveTo(-1,-1);x.lineTo(TILE+1,-1);for(let u=TILE+1;u>=-1;u-=2)x.lineTo(u,wav(u));x.closePath();x.fillStyle=sh(b,0);x.fill();
    x.beginPath();for(let u=-1;u<=TILE+1;u+=2)u<0?x.moveTo(u,wav(u)-1.6):x.lineTo(u,wav(u)-1.6);x.strokeStyle='rgba(255,255,255,.07)';x.lineWidth=1.6;x.stroke()})));
  SPR.edc=BIO.map(b=>[0,1,2,3].map(q=>mk(TILE,TILE,x=>{turn(x,q);const R=wav(0);x.beginPath();x.arc(0,0,R+1.2,0,Math.PI/2);x.strokeStyle='rgba(8,10,20,.3)';x.lineWidth=2.4;x.stroke();x.beginPath();x.moveTo(-1,-1);x.lineTo(R,-1);x.arc(0,0,R,0,Math.PI/2);x.lineTo(-1,R);x.closePath();x.fillStyle=sh(b,0);x.fill()})));
"""
CORN="if(!SPR.flT[b]){const E=SPR.edc;let q;if(ty>0&&tx>0&&(q=B[i-N-1])>b&&B[i-N]<=b&&B[i-1]<=b)ctx.drawImage(E[q][0],X,Y,W,W);if(ty>0&&tx+1<N&&(q=B[i-N+1])>b&&B[i-N]<=b&&B[i+1]<=b)ctx.drawImage(E[q][1],X,Y,W,W);if(ty+1<N&&tx+1<N&&(q=B[i+N+1])>b&&B[i+N]<=b&&B[i+1]<=b)ctx.drawImage(E[q][2],X,Y,W,W);if(ty+1<N&&tx>0&&(q=B[i+N-1])>b&&B[i+N]<=b&&B[i-1]<=b)ctx.drawImage(E[q][3],X,Y,W,W)}\n      "
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    a=s.index("  SPR.fl=BIO.map((b,bi)=>[0,1,2,3,4,5].map(v=>mk(TILE,TILE,x=>{x.fillStyle='rgb('+b+')'");b=s.index("  SPR.ao=[mk(",a);s=s[:a]+FL+s[b:]
    rep("      if(k===0){const u=ty>0?m.g[i-N]:3,l=tx>0?m.g[i-1]:3;","      "+CORN+"if(k===0){const u=ty>0?m.g[i-N]:3,l=tx>0?m.g[i-1]:3;")
    rep("const g=x.createLinearGradient(0,0,0,24);g.addColorStop(0,'rgba(6,8,16,.55)');g.addColorStop(1,'rgba(6,8,16,0)');x.fillStyle=g;x.fillRect(0,0,TILE,24)","const g=x.createLinearGradient(0,0,0,15);g.addColorStop(0,'rgba(6,8,16,.3)');g.addColorStop(1,'rgba(6,8,16,0)');x.fillStyle=g;x.fillRect(0,0,TILE,15)")
    rep("const g=x.createLinearGradient(0,0,16,0);g.addColorStop(0,'rgba(6,8,16,.3)');","const g=x.createLinearGradient(0,0,12,0);g.addColorStop(0,'rgba(6,8,16,.16)');")
    rep("      else ctx.drawImage(s,tx*TILE+24-s.w/2,ty*TILE+TILE+4-s.h,s.w,s.h);","      else{ctx.save();ctx.translate(tx*TILE+24,ty*TILE+TILE+4);const z=.92+((dd>>4)%4)*.06;ctx.scale(z,z);if(!still())ctx.rotate(Math.sin(t/1100+tx*1.7+ty*.9)*.02);ctx.drawImage(s,-s.w/2,-s.h,s.w,s.h);ctx.restore()}")
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok (patch23)')
