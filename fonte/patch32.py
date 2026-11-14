# progresso entre partidas (v1), salvo no aparelho (localStorage 'arena-nexus-meta'):
# nível de conta, maestria por herói, 3 missões do dia + 1 da semana, baú de fim de partida (moedas), recordes e conquistas.
# Sem punição por faltar: só bônus de +50% na primeira partida do dia. Moedas ainda não têm loja (próxima rodada).
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
CSS=r"""
.meta-bar{display:grid;grid-template-columns:1fr auto;gap:6px 12px;align-items:center;padding:10px 12px;border:1px solid var(--line);border-radius:10px;background:rgba(255,255,255,.03);margin:2px 0 4px}
.meta-bar b{font:800 15px var(--ui);color:var(--gold)}.meta-bar .mb-c{font:700 13px var(--ui);color:var(--ink)}.meta-bar .mb-m{grid-column:1/-1;font:600 12px var(--ui);color:var(--muted)}
.xbar{height:7px;border-radius:4px;background:rgba(255,255,255,.1);overflow:hidden;margin-top:5px}.xbar i{display:block;height:100%;background:var(--gold);border-radius:4px}
#prof{position:fixed;inset:0;z-index:60;background:rgba(6,8,16,.8);display:grid;place-items:center;padding:12px}#prof[hidden]{display:none}
#prof .pf{width:min(100%,440px);max-height:100%;overflow-y:auto;background:var(--stone);border:1px solid var(--line);border-radius:12px;padding:14px;display:grid;gap:12px}
#prof h2{margin:0;font:800 20px var(--ui);color:var(--gold)}#prof h3{margin:6px 0 0;font:800 12px var(--ui);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.pf-row{display:grid;grid-template-columns:1fr auto;gap:2px 10px;align-items:center;font:600 13px var(--ui);color:var(--ink)}.pf-row small{color:var(--muted);font-weight:600}.pf-row .xbar{grid-column:1/-1;margin-top:3px}
.pf-row.ok{color:var(--gold)}.pf-ach{display:flex;flex-wrap:wrap;gap:6px}.pf-ach span{font:700 11px var(--ui);padding:5px 8px;border-radius:999px;border:1px solid var(--line);color:var(--muted);opacity:.55}.pf-ach span.on{color:var(--gold);border-color:var(--gold);opacity:1}
.pf-foot{position:sticky;bottom:-14px;margin:0 -14px -14px;padding:10px 14px;background:var(--stone);border-top:1px solid var(--line);display:flex;justify-content:flex-end}
#end-meta{display:grid;gap:8px;margin:4px 0 10px;padding:12px;border:1px solid var(--line);border-radius:10px;background:rgba(255,255,255,.03);font:600 13px var(--ui);color:var(--ink)}#end-meta:empty{display:none}
#end-meta b{color:var(--gold)}#end-meta .em-ch{display:flex;align-items:center;gap:10px}#end-meta .em-ch button{flex:none}
@keyframes empop{0%{transform:scale(.6);opacity:0}60%{transform:scale(1.12)}100%{transform:scale(1);opacity:1}}.em-pop{animation:empop .45s ease-out}
@media (prefers-reduced-motion:reduce){.em-pop{animation:none}}
"""
JS=r"""/* ---------- progresso entre partidas (salvo no aparelho) ---------- */
const MK='arena-nexus-meta';let MT=null;
/* quem já tinha o jogo salvo antes de existirem heróis bloqueados mantém todos (lido antes de o jogo gravar qualquer coisa) */
const OLDP=(()=>{try{return!!localStorage.getItem('arena-celeste')}catch(_){return false}})();
const MLV=x=>{let l=1;while(x>=100+50*(l-1)){x-=100+50*(l-1);l++}return[l,x,100+50*(l-1)]};
const HLV=x=>{let l=0;while(x>=150*(l+1)){x-=150*(l+1);l++}return[l,x,150*(l+1)]};
const MTIT=[[16,'Lenda'],[12,'Mestre'],[8,'Especialista'],[5,'Veterano'],[3,'Aprendiz'],[1,'Iniciado'],[0,'Novato']],mtit=l=>MTIT.find(a=>l>=a[0])[1];
const CHN=['Baú Comum','Baú Raro','Baú Épico','Baú Mítico'],CHC=['#c9cedb','#63c7d6','#c58cf0','#ffd27a'];
function metaLoad(){if(MT)return MT;let s={};try{s=JSON.parse(localStorage.getItem(MK)||'{}')||{}}catch(_){}
  const ob=v=>v&&typeof v==='object'&&!Array.isArray(v)?v:{};
  MT={xp:Math.max(0,num(s.xp)|0),coins:Math.max(0,num(s.coins)|0),hx:Array.isArray(s.hx)?s.hx.map(v=>Math.max(0,num(v)|0)):[],rec:ob(s.rec),tot:ob(s.tot),ach:ob(s.ach),day:ob(s.day),week:ob(s.week),own:ob(s.own),eq:Array.isArray(s.eq)?s.eq:[],un:Array.isArray(s.un)?s.un.filter(v=>v>=0&&v<CLS.length):null};
  if(!MT.un){MT.un=OLDP||MT.xp>0?CLS.map((_,i)=>i):[0,1,2,3];metaSave()}return MT}
function metaSave(){try{localStorage.setItem(MK,JSON.stringify(MT))}catch(_){}}
const dayKey=()=>{const d=new Date();return d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate()},weekKey=()=>{const d=new Date();return Math.floor((Date.UTC(d.getFullYear(),d.getMonth(),d.getDate())/864e5+3)/7)};
const DPOOL=[{k:'mk',n:40,t:'Derrote 40 criaturas'},{k:'bk',n:2,t:'Derrote 2 chefes'},{k:'ch',n:5,t:'Abra 5 baús'},{k:'pl',n:2,t:'Jogue 2 partidas'},{k:'lv',n:10,mx:1,t:'Chegue ao nível 10 em uma partida'},{k:'gl',n:400,mx:1,t:'Faça 400 de glória em uma partida'},{k:'hero',n:1,t:'Jogue uma partida com '}];
const WPOOL=[{k:'pl',n:10,t:'Jogue 10 partidas'},{k:'bk',n:12,t:'Derrote 12 chefes'},{k:'ch',n:30,t:'Abra 30 baús'},{k:'mk',n:300,t:'Derrote 300 criaturas'}];
function metaMissions(){const M=metaLoad(),dk=dayKey(),wk=weekKey();
  if(M.day.k!==dk||!Array.isArray(M.day.ms)){let h=hashStr('d'+dk)>>>0;const pool=DPOOL.slice(),ms=[];for(let i=0;i<3;i++){const p=pool.splice(h%pool.length,1)[0];h=(Math.imul(h^(h>>>7),2654435761)>>>0)||7;const hc=p.k==='hero'?(h>>>9)%CLS.length:-1;ms.push({k:p.k,n:p.n,mx:p.mx||0,t:hc>=0?p.t+CLS[hc].n:p.t,hc,p:0,d:0})}M.day={k:dk,ms,first:0};metaSave()}
  if(M.week.k!==wk||!Array.isArray(M.week.ms)){const p=WPOOL[wk%WPOOL.length];M.week={k:wk,ms:[{k:p.k,n:p.n,mx:0,t:p.t,hc:-1,p:0,d:0}]};metaSave()}return M}
const ACH=[{id:'p1',t:'Primeira partida',c:M=>M.tot.pl>=1},{id:'p25',t:'25 partidas',c:M=>M.tot.pl>=25},{id:'b1',t:'Primeiro chefe',c:M=>M.tot.bk>=1},{id:'b10',t:'10 chefes',c:M=>M.tot.bk>=10},{id:'c50',t:'50 baús abertos',c:M=>M.tot.ch>=50},
  {id:'l20',t:'Nível 20 numa partida',c:(M,x)=>x.lv>=20},{id:'g1k',t:'1000 de glória numa partida',c:(M,x)=>x.gl>=1000},{id:'all',t:'Jogou com todos os heróis',c:M=>CLS.every((_,i)=>(M.hx[i]|0)>0)},{id:'m5',t:'Maestria 5 com um herói',c:M=>M.hx.some(v=>HLV(v|0)[0]>=5)},
  {id:'a10',t:'Conta nível 10',c:M=>MLV(M.xp)[0]>=10},{id:'ep',t:'Achou um baú épico',c:(M,x)=>x.chest>=2},{id:'w1',t:'Primeira vitória contra amigos',c:M=>M.tot.win>=1}];
function metaEnd(){if(!H||G.metaMid===G.mid)return;G.metaMid=G.mid;const M=metaMissions(),gl=glory(),st={mk:H.mk|0,bk:H.bk|0,ch:G.myCc.length,pl:1,lv:H.lv,gl,hero:1};
  let foes=0,top=true;others.forEach(o=>{if(!o.gone&&o.mid===G.mid){foes++;if(o.sc>gl)top=false}});const win=foes>0&&top;
  let xp=30+Math.round(gl*.15)+25*st.bk+(win?40:0);const first=!M.day.first;if(first){xp=Math.round(xp*1.5);M.day.first=1}
  const r=Math.random(),ch=r<.01?[3,400]:r<.1?[2,150+Math.floor(Math.random()*51)]:r<.4?[1,60+Math.floor(Math.random()*31)]:[0,20+Math.floor(Math.random()*21)];
  const done=[];for(const m of M.day.ms.concat(M.week.ms)){if(m.d||(m.k==='hero'&&m.hc!==H.cls))continue;const v=st[m.k]|0;m.p=m.mx?Math.max(m.p,v):m.p+v;if(m.p>=m.n){m.d=1;const wkm=M.week.ms.includes(m);xp+=wkm?200:40;M.coins+=wkm?150:30;done.push(m.t)}}
  const l0=MLV(M.xp)[0],h0=HLV(M.hx[H.cls]|0)[0];while(M.hx.length<CLS.length)M.hx.push(0);M.xp+=xp;M.hx[H.cls]=(M.hx[H.cls]|0)+xp;M.coins+=ch[1];
  const R=M.rec[H.cls]||(M.rec[H.cls]={gl:0,lv:0,mk:0});let nr=false;if(gl>R.gl){nr=R.gl>0;R.gl=gl}if(H.lv>R.lv)R.lv=H.lv;if(st.mk>R.mk)R.mk=st.mk;
  const T=M.tot;T.pl=(T.pl|0)+1;T.win=(T.win|0)+(win?1:0);T.bk=(T.bk|0)+st.bk;T.ch=(T.ch|0)+st.ch;T.mk=(T.mk|0)+st.mk;
  const na=[];for(const a of ACH)if(!M.ach[a.id]&&a.c(M,{lv:H.lv,gl,chest:ch[0]})){M.ach[a.id]=1;na.push(a.t)}
  metaSave();const l1=MLV(M.xp)[0],h1=HLV(M.hx[H.cls])[0];metaEndUI({xp,first,ch,done,lu:l1>l0?l1:0,hu:h1>h0?h1:0,nr,na,cls:H.cls})}
function metaEl(tag,txt,cls){const e=document.createElement(tag);if(txt!=null)e.textContent=txt;if(cls)e.className=cls;return e}
function metaBar(v,n){const b=metaEl('div',null,'xbar'),i=document.createElement('i');i.style.width=Math.round(clamp(v/n,0,1)*100)+'%';b.appendChild(i);return b}
function metaEndUI(R){const box=$('end-meta'),M=MT,L=MLV(M.xp);box.textContent='';
  const a=metaEl('div');a.append(metaEl('b','+'+R.xp+' de experiência'),R.first?' (bônus da primeira partida do dia)':'');box.appendChild(a);
  const lv=metaEl('div');lv.append('Conta nível '+L[0]+' ('+L[1]+'/'+L[2]+')',metaBar(L[1],L[2]));box.appendChild(lv);
  const cw=metaEl('div',null,'em-ch'),bt=metaEl('button','Abrir baú','alt'),out=metaEl('span','Você ganhou um baú.');bt.type='button';cw.append(bt,out);box.appendChild(cw);
  bt.addEventListener('click',()=>{bt.remove();out.textContent='';const n=metaEl('b',CHN[R.ch[0]]);n.style.color=CHC[R.ch[0]];out.append(n,': +'+R.ch[1]+' moedas (total '+M.coins+')');out.className='em-pop'});
  if(R.lu)box.appendChild(metaEl('div','Sua conta subiu para o nível '+R.lu+'!'));
  if(R.hu)box.appendChild(metaEl('div','Maestria de '+CLS[R.cls].n+' subiu para '+R.hu+' ('+mtit(R.hu)+').'));
  if(R.nr)box.appendChild(metaEl('div','Novo recorde de glória com '+CLS[R.cls].n+'!'));
  for(const d of R.done)box.appendChild(metaEl('div','Missão concluída: '+d));
  for(const d of R.na)box.appendChild(metaEl('div','Conquista: '+d))}
function metaMenu(){const M=metaMissions(),L=MLV(M.xp),dn=M.day.ms.filter(m=>m.d).length;$('mb-lv').textContent='Nível '+L[0];$('mb-c').textContent=M.coins+' moedas';$('mb-x').style.width=Math.round(L[1]/L[2]*100)+'%';
  $('mb-m').textContent='Missões de hoje: '+dn+'/3'+(M.day.first?'':' · primeira partida do dia vale +50% de experiência')}
function metaProf(on){const P2=$('prof');P2.hidden=!on;if(!on)return;const M=metaMissions(),L=MLV(M.xp),B=$('pf-body');B.textContent='';
  const row=(a,b,v,n,ok)=>{const r=metaEl('div',null,'pf-row'+(ok?' ok':''));r.append(metaEl('span',a),metaEl('small',b));if(n)r.appendChild(metaBar(v,n));return r};
  B.appendChild(row('Conta nível '+L[0],M.coins+' moedas',L[1],L[2]));
  B.appendChild(metaEl('h3','Missões de hoje'));for(const m of M.day.ms)B.appendChild(row(m.t,m.d?'concluída':Math.min(m.p,m.n)+'/'+m.n+' · 40 exp, 30 moedas',m.p,m.n,m.d));
  B.appendChild(metaEl('h3','Missão da semana'));for(const m of M.week.ms)B.appendChild(row(m.t,m.d?'concluída':Math.min(m.p,m.n)+'/'+m.n+' · 200 exp, 150 moedas',m.p,m.n,m.d));
  B.appendChild(metaEl('h3','Maestria e recordes por herói'));CLS.forEach((C,i)=>{const h=HLV(M.hx[i]|0),R=M.rec[i];B.appendChild(row(C.n+' · '+mtit(h[0])+' '+h[0],R?'recorde: '+R.gl+' de glória, nível '+R.lv:'ainda não jogou',h[1],h[2]))});
  const T=M.tot;B.appendChild(metaEl('h3','Totais'));B.appendChild(row((T.pl|0)+' partidas, '+(T.win|0)+' vitórias contra amigos',(T.bk|0)+' chefes · '+(T.ch|0)+' baús · '+(T.mk|0)+' criaturas'));
  B.appendChild(metaEl('h3','Conquistas ('+ACH.filter(a=>M.ach[a.id]).length+'/'+ACH.length+')'));const g=metaEl('div',null,'pf-ach');for(const a of ACH)g.appendChild(metaEl('span',a.t,M.ach[a.id]?'on':''));B.appendChild(g)}
"""
def patch(s,test):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    rep("#b-tal[data-n]:not([data-n=\"0\"])::before{",CSS+"#b-tal[data-n]:not([data-n=\"0\"])::before{")
    a=s.index('id="t-menu">Arena Nexus</h1>');b=s.index('</p>',a)+4
    s=s[:b]+'\n      <div class="meta-bar"><div><b id="mb-lv"></b><div class="xbar"><i id="mb-x"></i></div></div><div style="display:grid;gap:6px;justify-items:end"><span class="mb-c" id="mb-c"></span><button class="alt" id="b-prof" type="button">Perfil e missões</button></div><span class="mb-m" id="mb-m"></span></div>'+s[b:]
    rep('<p class="lede" id="end-line"></p>','<p class="lede" id="end-line"></p>\n      <div id="end-meta"></div>')
    rep('<script src="https://unpkg.com/mqtt','<div id="prof" hidden><div class="pf"><h2>Perfil</h2><div id="pf-body" style="display:grid;gap:8px"></div><div class="pf-foot"><button class="go" id="b-pclose" type="button" style="width:auto;min-width:132px">Fechar</button></div></div></div>\n<script src="https://unpkg.com/mqtt')
    rep("function endMatch(){setState('end');",JS+("window.__end=()=>endMatch();\n" if test else "")+"function endMatch(){setState('end');metaEnd();")
    rep("function setState(s){G.state=s;","function setState(s){G.state=s;if(s==='menu')metaMenu();")
    rep("selectHero(P.cls);drawIcons(0);","selectHero(P.cls);drawIcons(0);$('b-prof').addEventListener('click',()=>metaProf(true));$('b-pclose').addEventListener('click',()=>metaProf(false));$('prof').addEventListener('click',e=>{if(e.target===e.currentTarget)metaProf(false)});metaMenu();")
    return s
s=patch(s,False);t=patch(t,True)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok (patch32)')
