# v1: Perfil reorganizado em 3 abas (Missões, Heróis, Conquistas) com explicação do que nível e moedas fazem; subir de nível dá 50 moedas;
# liberar herói também pelo Perfil. Sala: times Sol/Lua só aparecem quando alguém da sala escolheu a formação Times, em duas colunas.
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
PROF=r"""let PFT=0;
function metaProf(on,tab){const P2=$('prof');P2.hidden=!on;if(!on)return;if(tab!=null)PFT=tab;const M=metaMissions(),L=MLV(M.xp),B=$('pf-body');B.textContent='';
  const row=(a,b,v,n,ok,rw)=>{const r=metaEl('div',null,'pf-row'+(ok?' ok':''));r.append(metaEl('span',a),metaEl('small',b));if(n)r.appendChild(metaBar(v,n));if(rw&&!ok)r.appendChild(metaEl('span','Recompensa: '+rw,'pf-rw'));return r};
  const head=metaEl('div',null,'pf-head'),c1=metaEl('div',null,'pf-box'),c2=metaEl('div',null,'pf-box');
  c1.append(metaEl('b','Nível '+L[0]),metaBar(L[1],L[2]),metaEl('small','Faltam '+(L[2]-L[1])+' de experiência para o nível '+(L[0]+1)+'. Cada nível novo dá 50 moedas.'));
  c2.append(metaEl('b',M.coins+' moedas'),metaEl('small','Servem para liberar heróis ('+HPRICE+') e comprar visuais (250 ou 400), na aba Heróis.'));head.append(c1,c2);B.appendChild(head);
  const tabs=metaEl('div',null,'pf-tabs');['Missões','Heróis','Conquistas'].forEach((n,i)=>{const b=metaEl('button',n,i===PFT?'on':'');b.type='button';b.addEventListener('click',()=>metaProf(true,i));tabs.appendChild(b)});B.appendChild(tabs);
  if(PFT===0){B.appendChild(metaEl('p','Toda partida jogada até o fim dá experiência e um baú de moedas, e conta para as missões. Elas se concluem sozinhas.','pf-tip'));
    B.appendChild(metaEl('h3','Missões de hoje'));for(const m of M.day.ms)B.appendChild(row(m.t,m.d?'concluída':Math.min(m.p,m.n)+' de '+m.n,m.p,m.n,m.d,'40 de experiência e 30 moedas'));
    B.appendChild(metaEl('h3','Missão da semana'));for(const m of M.week.ms)B.appendChild(row(m.t,m.d?'concluída':Math.min(m.p,m.n)+' de '+m.n,m.p,m.n,m.d,'200 de experiência e 150 moedas'));
    B.appendChild(metaEl('p',M.day.first?'Bônus do dia já usado: sua primeira partida de hoje valeu 50% a mais de experiência.':'Bônus do dia disponível: sua próxima partida vale 50% a mais de experiência.','pf-tip'))}
  else if(PFT===1){B.appendChild(metaEl('p','Jogar com um herói aumenta a maestria dele. Use moedas para liberar heróis e trocar o visual.','pf-tip'));
    CLS.forEach((C,i)=>{const h=HLV(M.hx[i]|0),R=M.rec[i],ok=metaOk(i),card=metaEl('div',null,'pf-hero'+(ok?'':' lock')),top=metaEl('div',null,'pf-row');
      top.append(metaEl('span',C.n),metaEl('small',ok?'Maestria '+h[0]+' · '+mtit(h[0]):'Bloqueado'));card.appendChild(top);
      if(ok){card.appendChild(metaBar(h[1],h[2]));card.appendChild(metaEl('small',R?'Recorde: '+R.gl+' de glória, nível '+R.lv+' na partida':'Você ainda não jogou com este herói.'));
        const w=metaEl('div',null,'pf-sk');w.appendChild(metaEl('small','Visual:'));SKN.forEach(([nm,pr],k)=>{const own=!k||!!M.own[i+'_'+k],eq=metaSkin(i)===k,bt=metaEl('button',eq?nm+' (em uso)':own?nm:nm+' · '+pr+' moedas','alt'+(eq?' on':''));bt.type='button';bt.disabled=!own&&M.coins<pr;
          bt.addEventListener('click',()=>{if(!own){if(M.coins<pr)return;M.coins-=pr;M.own[i+'_'+k]=1}while(M.eq.length<CLS.length)M.eq.push(0);M.eq[i]=k;metaSave();metaMenu();metaProf(true);pushPresence()});w.appendChild(bt)});card.appendChild(w)}
      else{card.appendChild(metaEl('small',C.s1.n+' e '+C.s2.n+'.'));const bt=metaEl('button',M.coins<HPRICE?'Liberar · faltam '+(HPRICE-M.coins)+' moedas':'Liberar por '+HPRICE+' moedas','alt');bt.type='button';bt.disabled=M.coins<HPRICE;
        bt.addEventListener('click',()=>{if(M.coins<HPRICE)return;M.coins-=HPRICE;M.un.push(i);metaSave();metaMenu();metaProf(true)});card.appendChild(bt)}
      B.appendChild(card)})}
  else{const T=M.tot;B.appendChild(metaEl('h3','Seus números'));B.appendChild(row((T.pl|0)+((T.pl|0)===1?' partida · ':' partidas · ')+(T.win|0)+((T.win|0)===1?' vitória contra amigos':' vitórias contra amigos'),''));B.appendChild(row((T.bk|0)+' chefes · '+(T.ch|0)+' baús · '+(T.mk|0)+' criaturas',''));
    B.appendChild(metaEl('h3','Conquistas ('+ACH.filter(a=>M.ach[a.id]).length+' de '+ACH.length+')'));const g=metaEl('div',null,'pf-ach');for(const a of ACH)g.appendChild(metaEl('span',a.t,M.ach[a.id]?'on':''));B.appendChild(g)}}
"""
CSS=r"""
.pf-head{display:grid;grid-template-columns:1fr 1fr;gap:8px}.pf-box{display:grid;gap:6px;align-content:start;padding:10px;border:1px solid var(--line);border-radius:10px}.pf-box b{font:800 16px var(--ui);color:var(--gold)}.pf-box .xbar{margin:0}
.pf-box small,.pf-hero small,.pf-tip{font:600 11.5px/1.35 var(--ui);color:var(--muted);margin:0}
.pf-tabs{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}.pf-tabs button{padding:10px 4px;font:800 12px var(--ui);letter-spacing:.04em;text-transform:uppercase;color:var(--muted);background:transparent;border:1px solid var(--line);border-radius:8px}.pf-tabs button.on{color:var(--gold-ink);background:var(--gold);border-color:var(--gold)}
.pf-hero{display:grid;gap:6px;padding:10px;border:1px solid var(--line);border-radius:10px}.pf-hero.lock{border-style:dashed}.pf-hero .pf-sk{justify-content:flex-start;align-items:center}.pf-hero>button{width:auto;justify-self:start;padding:7px 10px;font-size:12px;min-height:0}.pf-hero>button:disabled{opacity:.5}
.pf-rw{grid-column:1/-1;font:700 11px var(--ui);color:var(--gold)}
#room-list.teams{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:0}
#room-list.teams>li.tcol{display:grid;gap:5px;align-content:start;padding:8px;border:1px solid var(--line);border-radius:8px;background:transparent;list-style:none;font:600 13px var(--ui);color:var(--ink)}
#room-list.teams>li.tcol>b{font:800 13px var(--ui);letter-spacing:.06em;text-transform:uppercase}#room-list.teams>li.t0>b{color:#ffd27a}#room-list.teams>li.t1>b{color:#7fb4ff}
#room-list.teams>li.t0.mine{border-color:#ffd27a}#room-list.teams>li.t1.mine{border-color:#7fb4ff}
#room-list.teams>li.tcol>span.you{font-weight:800}#room-list.teams>li.tcol>small{color:var(--muted);font:600 11px var(--ui)}
#room-list.teams>li.tcol>button{margin-top:2px;padding:6px 8px;font:700 12px var(--ui);color:var(--ink);background:rgba(255,255,255,.06);border:1px solid var(--line);border-radius:6px}
"""
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    a=s.index("function metaProf(on){");b=s.index("window.__end=()=>endMatch();") if "window.__end=()=>endMatch();" in s else s.index("function endMatch(){setState('end');")
    s=s[:a]+PROF+s[b:]
    rep("metaSave();const l1=MLV(M.xp)[0],h1=HLV(M.hx[H.cls])[0];metaEndUI(","const l1=MLV(M.xp)[0],h1=HLV(M.hx[H.cls])[0];if(l1>l0)M.coins+=50*(l1-l0);metaSave();metaEndUI(")
    rep("'Sua conta subiu para o nível '+R.lu+'!'","'Sua conta subiu para o nível '+R.lu+'! +50 moedas.'")
    rep(".pf-foot{",CSS+".pf-foot{")
    # sala: times só quando alguém escolheu Times; duas colunas
    rep("{n:P.name,al:MLV(metaLoad().xp)[0],sk:metaSkin(P.cls),c:P.cls,mid:''","{n:P.name,pm:P.mode,al:MLV(metaLoad().xp)[0],sk:metaSkin(P.cls),c:P.cls,mid:''")
    rep("o.al=clamp(num(s.al)|0,0,999);","o.al=clamp(num(s.al)|0,0,999);o.pm=clamp(num(s.pm)|0,0,2);")
    rep("    if(list.length){add(P.name+' (você) · nv. '+MLV(metaLoad().xp)[0]+' · '+TEAMS[P.team],true);list.forEach(o=>add(o.name+(o.al?' · nv. '+o.al:'')+' · '+TEAMS[o.team]+(o.mid&&Date.now()-o.at<4000&&o.e<o.dur?' · em partida':'')))}}",
        "    const tm=P.mode===1||list.some(o=>o.pm===1),inf=o=>o.name+(o.al?' · nv. '+o.al:'')+(o.mid&&Date.now()-o.at<4000&&o.e<o.dur?' · em partida':'');ul.classList.toggle('teams',tm);\n    if(tm){for(const k of[0,1]){const col=document.createElement('li');col.className='tcol t'+k+(P.team===k?' mine':'');const hd=document.createElement('b');hd.textContent='Time '+TEAMS[k];col.appendChild(hd);const mk=(tx,you)=>{const sp=document.createElement('span');sp.textContent=tx;if(you)sp.className='you';col.appendChild(sp)};let n=0;if(P.team===k){mk(P.name+' (você)',true);n++}list.forEach(o=>{if(o.team===k){mk(inf(o));n++}});if(!n){const sm=document.createElement('small');sm.textContent='ninguém ainda';col.appendChild(sm)}\n        if(P.team!==k){const bt=document.createElement('button');bt.type='button';bt.textContent='Ir para '+TEAMS[k];bt.addEventListener('click',()=>$('team'+k).click());col.appendChild(bt)}ul.appendChild(col)}}\n    else if(list.length){add(P.name+' (você) · nv. '+MLV(metaLoad().xp)[0],true);list.forEach(o=>add(inf(o)))}}\n  $('f-team').hidden=true;")
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok (patch35)')
