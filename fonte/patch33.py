# v1: Zero vira herói de longo alcance e frágil (bombinhas com estilhaço); abraço do Grude visível (bit 1024 de bf) e efeito de mordida;
# loja de visuais (2 variações de cor por herói, pagas com moedas), heróis a desbloquear (300 moedas; quem já jogava mantém os 9),
# nível da conta ao lado do nome na sala.
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
JS=r"""/* visuais (variações de cor) e heróis liberados */
const SKC={},SKN=[['Padrão',0],['Eco',250],['Prisma',400]],HPRICE=300;
function hueShift(hex,deg){let r=parseInt(hex.slice(1,3),16)/255,g=parseInt(hex.slice(3,5),16)/255,b=parseInt(hex.slice(5,7),16)/255;const mx=Math.max(r,g,b),mn=Math.min(r,g,b),l=(mx+mn)/2,d=mx-mn;let h=0,sa=0;
  if(d){sa=d/(1-Math.abs(2*l-1));h=mx===r?((g-b)/d)%6:mx===g?(b-r)/d+2:(r-g)/d+4;h*=60}h=((h+deg)%360+360)%360;const C=(1-Math.abs(2*l-1))*sa,X=C*(1-Math.abs((h/60)%2-1)),m=l-C/2;
  [r,g,b]=h<60?[C,X,0]:h<120?[X,C,0]:h<180?[0,C,X]:h<240?[0,X,C]:h<300?[X,0,C]:[C,0,X];return'#'+[r,g,b].map(v=>Math.round((v+m)*255).toString(16).padStart(2,'0')).join('')}
function skinOf(c,k){if(!k)return SKIN[c];const id=c+'_'+k;if(SKC[id])return SKC[id];const o={},deg=k===1?150:-75;for(const key in SKIN[c]){const v=SKIN[c][key];o[key]=key==='skin'||key==='bone'||key==='dark'||typeof v!=='string'||v.length!==7?v:hueShift(v,deg)}return SKC[id]=o}
const metaOk=c=>metaLoad().un.includes(c),metaSkin=c=>{const M=metaLoad(),k=M.eq[c]|0;return k&&M.own[c+'_'+k]?k:0};
function metaLock(){const M=metaLoad();for(let i=0;i<CLS.length;i++)$('hero'+i).nextElementSibling.classList.toggle('locked',!metaOk(i));
  $('lock-note').textContent=metaOk(P.cls)?'':CLS[P.cls].n+' está bloqueado. Toque no botão abaixo para liberar por '+HPRICE+' moedas (você tem '+M.coins+').'}
function metaShop(B,M){B.appendChild(metaEl('h3','Visuais dos heróis'));CLS.forEach((C,i)=>{if(!metaOk(i))return;const r=metaEl('div',null,'pf-row');r.appendChild(metaEl('span',C.n));const w=metaEl('div',null,'pf-sk');
  SKN.forEach(([nm,pr],k)=>{const own=!k||!!M.own[i+'_'+k],eq=metaSkin(i)===k,bt=metaEl('button',eq?nm+' (em uso)':own?nm:nm+' · '+pr,'alt'+(eq?' on':''));bt.type='button';bt.disabled=!own&&M.coins<pr;
    bt.addEventListener('click',()=>{if(!own){if(M.coins<pr)return;M.coins-=pr;M.own[i+'_'+k]=1}while(M.eq.length<CLS.length)M.eq.push(0);M.eq[i]=k;metaSave();metaMenu();metaProf(true);pushPresence()});w.appendChild(bt)});r.appendChild(w);B.appendChild(r)})}
"""
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    # Zero de longe
    rep("{n:'Zero',hp:470,dmg:24,range:66,itv:.8,spd:192,arm:2,proj:0,","{n:'Zero',hp:400,dmg:22,range:200,itv:.85,spd:192,arm:1,proj:8,")
    rep('<b>Zero</b><span>Minas invisíveis e TNT gigante</span>','<b>Zero</b><span>Frágil: bombas de longe, minas e TNT</span>')
    rep("PK={7:'#7fe3ff',","PK={8:'#ff9a4a',7:'#7fe3ff',")
    rep("      if(p.mine){if(live)dealt(tg,p.d,0,p.crit);","      if(p.k===8){fx('ring',p.tx,p.ty+10,{r:38,T:.25,col:'#ff9a4a'});burst(p.tx,p.ty,6,'#ff9a4a',130,.3,3)}\n      if(p.mine){if(live)dealt(tg,p.d,0,p.crit);if(p.k===8&&live)aoe(p.gx,p.gy,58,p.d*.4,tg);")
    # Grude
    rep("|(H.siOn?256:0)|(e<H.shield?512:0);","|(H.siOn?256:0)|(e<H.shield?512:0)|(H.hug?1024:0);")
    rep("if(f.k==='slash'){const s=f.s||1;","if(f.k==='bite'){const q=Math.min(1,p*2.2),g=(1-q)*f.r*.6,W2=f.r*.2;ctx.save();ctx.translate(f.x,f.y);ctx.globalAlpha=p<.75?1:(1-p)/.25;ctx.fillStyle='#ffffff';ctx.strokeStyle='#3a1230';ctx.lineWidth=1.6;ctx.lineJoin='round';for(const sd of[-1,1])for(let j=-3;j<=3;j++){const x=j*W2,L2=f.r*.36*(1-Math.abs(j)*.1);ctx.beginPath();ctx.moveTo(x-W2*.5,sd*(g+L2));ctx.lineTo(x,sd*g);ctx.lineTo(x+W2*.5,sd*(g+L2));ctx.closePath();ctx.fill();ctx.stroke()}ctx.restore()}\n    if(f.k==='slash'){const s=f.s||1;")
    # visuais, heróis liberados, nível na sala
    rep("function metaEl(tag,txt,cls){",JS+"function metaEl(tag,txt,cls){")
    rep("  const S=SKIN[o.cls],cf=Math.cos(o.face);","  const S=skinOf(o.cls,o.sk|0),cf=Math.cos(o.face);")
    rep("const d={icon:1,","const d={icon:1,sk:metaSkin(i),")
    rep("{n:P.name,c:P.cls,","{n:P.name,al:MLV(metaLoad().xp)[0],sk:metaSkin(P.cls),c:P.cls,",2)
    rep("o.cls=clamp(num(s.c)|0,0,CLS.length-1);","o.cls=clamp(num(s.c)|0,0,CLS.length-1);o.al=clamp(num(s.al)|0,0,999);o.sk=clamp(num(s.sk)|0,0,2);")
    rep("add(P.name+' (você) · '+TEAMS[P.team],true);list.forEach(o=>add(o.name+' · '+TEAMS[o.team]+","add(P.name+' (você) · nv. '+MLV(metaLoad().xp)[0]+' · '+TEAMS[P.team],true);list.forEach(o=>add(o.name+(o.al?' · nv. '+o.al:'')+' · '+TEAMS[o.team]+")
    rep("function newHero(){H={kind:'me',r:13,cls:P.cls,","function newHero(){H={kind:'me',r:13,cls:metaOk(P.cls)?P.cls:0,sk:metaOk(P.cls)?metaSkin(P.cls):0,")
    rep("$('mb-m').textContent='Missões de hoje: '","metaLock();$('mb-m').textContent='Missões de hoje: '")
    rep("const T=M.tot;B.appendChild(metaEl('h3','Totais'));","metaShop(B,M);const T=M.tot;B.appendChild(metaEl('h3','Totais'));")
    rep("$('b-prof').addEventListener('click',()=>metaProf(true));","$('b-prof').addEventListener('click',()=>metaProf(true));for(let i=0;i<CLS.length;i++)$('hero'+i).addEventListener('change',metaLock);\n  $('b-go').addEventListener('click',ev=>{if(metaOk(P.cls))return;ev.stopImmediatePropagation();const M=metaLoad();if(M.coins>=HPRICE){M.coins-=HPRICE;M.un.push(P.cls);metaSave();metaMenu();$('lock-note').textContent=CLS[P.cls].n+' liberado!'}else $('lock-note').textContent='Faltam '+(HPRICE-M.coins)+' moedas para liberar '+CLS[P.cls].n+'. Jogue partidas e cumpra missões para ganhar mais.'},true);")
    rep('<p id="skill-line"></p>','<p id="skill-line"></p>\n        <p class="note left" id="lock-note" style="color:var(--gold)"></p>')
    rep(".pf-foot{",".heroes label.locked{opacity:.55}.heroes label.locked::after{content:'300 moedas';font:800 11px var(--ui);color:var(--gold)}\n.pf-sk{display:flex;gap:4px;flex-wrap:wrap;justify-content:flex-end}.pf-sk button{padding:5px 8px;font-size:11px;min-height:0;width:auto}.pf-sk button.on{border-color:var(--gold);color:var(--gold)}.pf-sk button:disabled{opacity:.4}\n.pf-foot{")
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok (patch33)')
