# empurrões, puxões e o salto da Caçadora deixam de ser instantâneos: o personagem desliza até o destino (~0,3 s), com poeira.
# Também corrige a rede da Caçadora, que não prendia heróis de outros jogadores (o aviso de rede era descartado ao chegar).
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    rep("if(t.kind==='creep'){const n=dist?Math.ceil(dist/8):Math.ceil(dd/8);for(let s2=0;s2<n&&Math.hypot(t.x-qx,t.y-qy)>t.r+6;s2++){const a2=Math.atan2(qy-t.y,qx-t.x);moveC(t,Math.cos(a2)*8,Math.sin(a2)*8,Math.min(t.r,14))}t.aggro=1}",
        "if(t.kind==='creep'){const d0=Math.hypot(t.x-qx,t.y-qy);if(d0>t.r+6)t.kn={x:qx,y:qy,v:Math.max(420,d0/.32),t:.5};t.aggro=1}")
    rep("if(c.root>0)c.root-=dt;","if(c.root>0)c.root-=dt;if(c.kn){const K=c.kn,d=Math.hypot(K.x-c.x,K.y-c.y);K.t-=dt;if(d<=c.r+6||K.t<=0)c.kn=null;else{const st=Math.min(d,K.v*dt),a=Math.atan2(K.y-c.y,K.x-c.x);moveC(c,Math.cos(a)*st,Math.sin(a)*st,Math.min(c.r,14));if(Math.random()<.5)part(c.x,c.y-3,0,-12,.3,2.4,'#6e665c')}}")
    rep("const st=Math.min(d,1400*dt),a=Math.atan2(P2.y-H.y,P2.x-H.x)","const st=Math.min(d,800*dt),a=Math.atan2(P2.y-H.y,P2.x-H.x)")
    rep("H.pull={x:tx,y:ty,t:.22}","H.pull={x:tx,y:ty,t:.42}")
    rep("const bx=-Math.cos(ang)*13,by=-Math.sin(ang)*13;for(let q=0;q<10;q++)moveC(H,bx,by,13)}","H.dash={vx:-Math.cos(ang)*590,vy:-Math.sin(ang)*590,t:.22}}")
    rep("    if(H.pull){const P2=H.pull","    if(H.dash){const D=H.dash,st=Math.min(D.t,dt);moveC(H,D.vx*st,D.vy*st,13);D.t-=dt;if(D.t<=0)H.dash=null;if(Math.random()<.7)part(H.x,H.y-3,0,-14,.3,2.6,'#6e665c')}\n    if(H.pull){const P2=H.pull")
    rep("pull:null,tw:null","pull:null,dash:null,tw:null")
    rep("H.pull=null;respawnFx","H.pull=null;H.dash=null;respawnFx")
    rep("h[3]===1?1:h[3]===2?2:0)","h[3]===1?1:h[3]===2?2:h[3]===3?3:0)")
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok (patch28)')
