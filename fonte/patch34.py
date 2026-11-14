# v1: (1) puxão em heróis mais firme e visível; (2) ranking final guarda quem já saiu; (3) pedra quebra com 3 a 5 picaretadas;
# (4) página inicial enxuta: título + cartão de perfil numa linha, heróis em grade compacta de 5 colunas, nome do jogador mais abaixo.
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
CSS=r"""
.mtop{display:flex;align-items:center;justify-content:space-between;gap:10px}
#menu .mtop h1{margin:0;font-size:25px;line-height:1.1}
.mchip{display:grid;gap:4px;min-width:150px;max-width:56%;padding:8px 10px;text-align:left;background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:10px;color:var(--ink);font:600 12px var(--ui);cursor:pointer}
.mchip .mc1{display:flex;justify-content:space-between;gap:8px}.mchip b{color:var(--gold);font:800 13px var(--ui)}.mchip .xbar{display:block;margin:0}.mchip .mb-m{color:var(--muted);font:600 11px var(--ui)}
#menu .heroes{grid-template-columns:repeat(5,minmax(0,1fr));gap:6px}#menu .heroes label{padding:4px 2px 6px;gap:1px}#menu .heroes label canvas{width:100%;max-width:58px;height:auto}#menu .heroes label b{font-size:11px;line-height:1.15}#menu .heroes label span{display:none}
#menu .heroes label.locked::after{content:'300';font-size:10px}
"""
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    # 1) puxão
    rep("H.pull={x:tx,y:ty,t:.42}","H.pull={x:tx,y:ty,t:.6};ftext(H.x,H.y-84,'puxado!','#ff8a7a')")
    rep("if(d<20||P2.t<=0)H.pull=null;","if(d<20||P2.t<=0){H.pull=null;H.root=Math.max(H.root,e+300)}")
    # 2) ranking final
    rep("function renderEnd(){const l=board(),","function endBoard(){if(G.endMid!==G.mid){G.endMid=G.mid;G.endL=new Map()}for(const r of board())G.endL.set(r.me?'*':r.name+'|'+r.cls,r);return[...G.endL.values()].sort((a,b)=>b.sc-a.sc||b.k-a.k)}\nfunction renderEnd(){const l=endBoard(),")
    # 3) picareta
    rep("const RKHP=10;","const RKHP=5,rkNeed=i=>3+(G.map.deco[i]%3);")
    rep("if(v>=RKHP)breakRock(i);","if(v>=rkNeed(i))breakRock(i);")
    rep("q=v/RKHP,d0=m.deco[ty*N+tx]","q=v/rkNeed(ty*N+tx),d0=m.deco[ty*N+tx]")
    rep("$('h-pick').textContent=ri>=0&&v?v+'/'+RKHP:''","$('h-pick').textContent=ri>=0&&v?v+'/'+rkNeed(ri):''")
    # 4) página inicial
    a=s.index('<h1 id="t-menu">');b=s.index('<div class="field">\n        <label class="label" for="nick">');c=s.index('<div class="field">\n        <span class="label" id="l-hero">')
    nick=s[b:c].rstrip()
    s=s[:a]+'<div class="mtop"><h1 id="t-menu">Arena Nexus</h1><button class="mchip" id="b-prof" type="button" aria-label="Perfil e missões"><span class="mc1"><b id="mb-lv"></b><span id="mb-c"></span></span><span class="xbar"><i id="mb-x"></i></span><span class="mb-m" id="mb-m"></span></button></div>\n      '+s[c:]
    rep('<div class="friends" id="room-ctl">',nick+'\n      <div class="friends" id="room-ctl">')
    rep("$('mb-m').textContent='Missões de hoje: '+dn+'/3'+(M.day.first?'':' · primeira partida do dia vale +50% de experiência')","$('mb-m').textContent='Missões '+dn+'/3'+(M.day.first?'':' · bônus do dia')+' · ver perfil'")
    rep(".pf-foot{",CSS+".pf-foot{")
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok (patch34)')
