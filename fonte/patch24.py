# roda por último: mais variedade no cenário desenhado por código e polimento dos heróis (versão de gráfico simples).
#  - "árvores" por região: grama = árvores; piso de pedra = coluna quebrada, cristais, árvore seca; terra = árvore de outono, cogumelo gigante, arbusto
#  - pedras com 3 formatos; beirada do mapa irregular e pedras flutuando no vazio
#  - heróis um pouco maiores, poeira ao andar, ícones do menu sem os estilhaços por cima
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
TREES=r"""  {const shd=(x,w)=>{x.fillStyle='rgba(0,0,0,.36)';ell(x,39,88,w,7)},br=(x,p,w,col)=>{x.strokeStyle=col;x.lineWidth=w;x.lineCap='round';x.lineJoin='round';x.beginPath();x.moveTo(p[0][0],p[0][1]);for(let j=1;j<p.length;j++)x.lineTo(p[j][0],p[j][1]);x.stroke()};
  const g=SPR.tree,stone=[mk(78,96,x=>{shd(x,24);rr(x,22,77,34,11,3);fs(x,'#56628a');rr(x,27,34,24,45,2);fs(x,'#7684ad');x.fillStyle='#93a1cc';x.fillRect(29,36,5,42);x.fillStyle='rgba(16,19,31,.22)';x.fillRect(44,36,6,42);
      for(const y of[45,57,69]){x.fillStyle='rgba(16,19,31,.3)';x.fillRect(27.6,y,22.8,1.5)}
      poly(x,[[26,36],[26,31],[31,25],[36,31],[41,21],[46,30],[52,26],[52,36]]);fs(x,'#7684ad');x.fillStyle='#93a1cc';tri(x,28,35,31,27,33,35);
      x.fillStyle='#3f7a5a';ell(x,33,78,8,3);ell(x,47,59,4,2.4);x.fillStyle='#56628a';rr(x,54,82,9,6,2);x.fill();rr(x,14,84,7,5,2);x.fill()}),
    mk(78,96,x=>{shd(x,25);const cr=(bx,by,w,h,ln,c1,c2)=>{const p=[[bx-w,by],[bx-w*.6+ln,by-h*.75],[bx+ln*1.3,by-h],[bx+w*.7+ln,by-h*.7],[bx+w,by]];poly(x,p);fs(x,c1);x.fillStyle=c2;poly(x,[p[0],p[1],p[2],[bx+ln*.4,by]]);x.fill();poly(x,p);x.strokeStyle=OUT;x.lineWidth=1.3;x.stroke()};
      cr(25,87,9,34,-5,'#3d66b0','#63c7d6');cr(53,87,9,40,6,'#4a4fb0','#8c9cf0');cr(39,89,12,62,0,'#3f7fc0','#9fe8f5');x.fillStyle='#ffffff';circ(x,36,42,1.6);circ(x,23,66,1.1);circ(x,55,58,1.2)}),
    mk(78,96,x=>{shd(x,20);for(const[col,d]of[['#161b2e',2.6],['#6b6f8c',0]]){br(x,[[39,88],[38,60],[41,40]],9+d,col);br(x,[[40,58],[54,44],[60,30]],5+d,col);br(x,[[39,50],[26,38],[20,24]],5+d,col);br(x,[[41,40],[44,26],[40,14]],4+d,col);br(x,[[54,44],[65,42]],3+d,col);br(x,[[26,38],[17,40]],3+d,col)}
      br(x,[[36,86],[35,62]],2.5,'#8d91ad')})],
   dirt=[mk(78,96,x=>{shd(x,25);x.fillStyle='#4f3524';x.fillRect(34,60,10,28);x.fillStyle='#6b4a32';x.fillRect(34,60,4,28);
      canopy(x,[[39,42,27,'#8a3b1f'],[25,48,17,'#a8502a'],[53,46,18,'#a8502a'],[38,32,21,'#c96f33'],[30,25,11,'#e39a4c'],[47,30,8,'#e39a4c']]);x.strokeStyle='#3a1a10';x.lineWidth=1.4;x.beginPath();x.arc(39,42,27,0,TAU);x.stroke();
      for(const[lx,ly]of[[20,84],[58,86],[50,80]]){x.fillStyle='#c96f33';ell(x,lx,ly,3,1.6)}}),
    mk(78,96,x=>{shd(x,22);rr(x,32,50,14,38,5);fs(x,'#e8dcc6');x.fillStyle='rgba(16,19,31,.18)';x.fillRect(41,52,4,34);
      x.beginPath();x.ellipse(39,54,29,26,0,Math.PI,0);x.closePath();fs(x,'#b0413e');x.save();x.beginPath();x.ellipse(39,54,29,26,0,Math.PI,0);x.closePath();x.clip();x.fillStyle='#cf5a50';ell(x,30,36,16,9);x.fillStyle='#f2ead8';circ(x,27,40,4.5);circ(x,46,34,3.6);circ(x,55,46,3);circ(x,38,47,2.2);circ(x,17,49,2.4);x.restore();
      rr(x,54,78,7,10,3);fs(x,'#e8dcc6');x.beginPath();x.ellipse(57.5,79,9,7,0,Math.PI,0);x.closePath();fs(x,'#b0413e')}),
    mk(78,96,x=>{shd(x,24);canopy(x,[[39,72,19,'#4f5028'],[25,76,12,'#63642f'],[53,76,13,'#63642f'],[39,63,13,'#808238'],[31,60,7,'#9c9e48']]);x.strokeStyle='#22230f';x.lineWidth=1.4;x.beginPath();x.arc(39,72,19,Math.PI,0);x.stroke();
      for(const[bx,by]of[[30,70],[46,66],[40,78],[54,74],[24,78]]){x.fillStyle='#d9534a';circ(x,bx,by,2.2);x.fillStyle='#ffb0a0';circ(x,bx-.6,by-.6,.8)}})];
  SPR.tree=stone.concat(g,dirt);
  SPR.cliff=[0,1,2,3].map(()=>mk(TILE,TILE,x=>{const p=[[0,0],[TILE,0],[TILE,21]];for(let u=TILE-6;u>=6;u-=6)p.push([u,21+((u/6)&1?8+r()*10:2+r()*5)]);p.push([0,21]);poly(x,p);x.fillStyle='#1a2034';x.fill();x.fillStyle='rgba(12,15,29,.5)';x.fillRect(0,17,TILE,4);
    x.fillStyle='#2a3350';x.fillRect(0,0,TILE,5);x.fillStyle='rgba(255,255,255,.06)';x.fillRect(0,5,TILE,1.4);x.strokeStyle='rgba(8,10,20,.55)';x.lineWidth=1.2;for(let j=0;j<3;j++){const ux=6+r()*36;x.beginPath();x.moveTo(ux,7);x.lineTo(ux+(r()-.5)*5,16+r()*8);x.stroke()}}));
  SPR.flo=[0,1].map(v=>mk(34,30,x=>{poly(x,[[4,10],[30,10],[27,18],[20,27],[13,22],[8,25],[5,16]]);x.fillStyle='#232b45';x.fill();x.strokeStyle='#0c0f1d';x.lineWidth=1.2;x.stroke();rr(x,3,6,28,7,3);x.fillStyle=v?'#2f6e52':'#4a5578';x.fill();x.stroke();x.fillStyle='rgba(255,255,255,.12)';x.fillRect(6,7.5,18,1.5)}))}
"""
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    a=s.index("  SPR.chest=[[");s=s[:a]+TREES+s[a:]
    rep("SPR.tree[dd%3]","SPR.tree[(SPR.tree.length>3?m.bio[ty*N+tx]*3:0)+dd%3]")
    rep("[0,1,2].map(()=>mk(62,70,x=>{x.fillStyle='rgba(0,0,0,.38)';ell(x,31,61,27,7);\n    const pts=[];for(let j=0;j<9;j++){const a=j/9*TAU,rad=22+r()*7;pts.push([31+Math.cos(a)*rad*1.08,37+Math.sin(a)*rad])}",
        "[0,1,2].map(vj=>mk(62,70,x=>{x.fillStyle='rgba(0,0,0,.38)';ell(x,31,61,vj===1?22:27,7);\n    const pts=[];for(let j=0;j<9;j++){const a=j/9*TAU,rad=22+r()*7;pts.push(vj===1?[31+Math.cos(a)*rad*.8,33+Math.sin(a)*rad*1.16]:vj===2?[31+Math.cos(a)*rad*1.16,41+Math.sin(a)*rad*.82]:[31+Math.cos(a)*rad*1.08,37+Math.sin(a)*rad])}")
    rep("ctx.fillStyle='#1a2034';ctx.fillRect(X,Y,TILE+.6,22);ctx.fillStyle='#262e48';ctx.fillRect(X,Y,TILE+.6,5);ctx.fillStyle='rgba(12,15,29,.6)';ctx.fillRect(X,Y+22,TILE+.6,8)","ctx.drawImage(SPR.cliff[(tx*7+ty*3)&3],X,Y,TILE+.6,TILE+.6)")
    rep("ctx.fillRect(X+(d*7)%40+3,Y+(d*13)%34+12,big?3:2,big?3:2)}continue}","ctx.fillRect(X+(d*7)%40+3,Y+(d*13)%34+12,big?3:2,big?3:2)}else if(d>=249&&!(inb&&ty>0&&m.g[(ty-1)*N+tx]!==3)){const f=SPR.flo[d&1];ctx.drawImage(f,X+7,Y+9+(still()?0:Math.sin(t/900+tx*2.1+ty)*3),f.w,f.h)}continue}")
    # heróis
    rep("c.save();c.translate(o.x,o.y);c.scale(1.12,1.12);","if(!o.icon&&!AIH&&mv>.6&&!still()&&Math.random()<.06)part(o.x-dir*5,o.y-1,-dir*14,-10,.4,2.2,'#6e665c');\n  c.save();c.translate(o.x,o.y);c.scale(AIH?1.12:1.2,AIH?1.12:1.2);")
    rep("  const dir=o.dr,la=Math.atan2(Math.sin(o.face),cf*dir),mv=o.mv||0,wp=o.walk||0;","  const dir=o.dr,la=Math.atan2(Math.sin(o.face),cf*dir),mv=o.mv||0,wp=o.walk||0,AIH=!!ANIM['h'+o.cls];")
    rep("if(o.lv>=10&&!AI){","if(o.lv>=10&&!AI&&!o.icon){")
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok (patch24)')
