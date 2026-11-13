# mecânica (vale para as duas versões):
#  - Monge: Tornado mais forte (dano +33%, raio 120, 6 s, anda mais devagar) e o Monge sofre 25% menos dano dentro dele
#  - Caçadora: a Rajada prende os atingidos numa rede (criaturas 1,2 s; heróis 0,7 s; chefes não) e ela salta para trás
#    (Precisão não prende; Leque continua deixando lento). Julgamento do Paladino também solta da rede.
s=open('index.html',encoding='utf-8').read();t=open('site/index.html',encoding='utf-8').read()
def patch(s):
    def rep(a,b,n=1):
        nonlocal s
        assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
    # Tornado
    rep("else{mkZone('tornado',o.x,o.y,mine,m*.9,k===2,ang);","else{mkZone('tornado',o.x,o.y,mine,m*1.2,k===2,ang);")
    rep("r:110*g,t:0,T:.3,d:0,dur:5+(cap?2:0),tick:.3,tk:0,td:d,mine,flag:1,vx:Math.cos(a)*95,vy:Math.sin(a)*95","r:120*g,t:0,T:.3,d:0,dur:6+(cap?2:0),tick:.3,tk:0,td:d,mine,flag:1,vx:Math.cos(a)*78,vy:Math.sin(a)*78")
    rep("*(e<H.wrath?.65:1)*(by&&G.mod===6?1.4:1)}","*(e<H.wrath?.65:1)*(by&&G.mod===6?1.4:1)*(H.cls===3&&G.zones.some(z=>z.kind==='tornado'&&z.mine&&Math.hypot(z.x-H.x,z.y-H.y)<z.r)?.75:1)}")
    rep("um tornado avança por 5 s, suga as criaturas, fere e deixa lento quem alcança. Toque de novo","um tornado avança devagar por 6 s, suga as criaturas, fere e deixa lento quem alcança; dentro dele você sofre 25% menos dano. Toque de novo")
    # rede (flag 3)
    rep("if(flag===1)H.slow=e+1500;else if(flag===2)H.chill=e+2000}","if(flag===1)H.slow=e+1500;else if(flag===2)H.chill=e+2000;else if(flag===3){H.root=e+700;ftext(H.x,H.y-84,'preso','#e2c79a')}}")
    rep("(e<H.slow?.6:e<H.chill?.8:1),ox=H.x,oy=H.y;","(e<H.root?0:e<H.slow?.6:e<H.chill?.8:1),ox=H.x,oy=H.y;")
    rep("slow:0,chill:0,free:0,","slow:0,chill:0,root:0,free:0,")
    assert s.count("H.slow=0;H.chill=0;")>=3;s=s.replace("H.slow=0;H.chill=0;","H.slow=0;H.chill=0;H.root=0;")
    rep("if(e<H.slow||e<H.chill)ftext(","if(e<H.slow||e<H.chill||e<H.root)ftext(")
    rep("|(e<H.curse?16:0)|(e<H.bless?32:0)","|(e<H.curse?16:0)|(e<H.bless?32:0)|(e<H.root?64:0)")
    rep("if(flag===1)t.slow=1.5;else if(flag===2)t.chill=2;","if(flag===1)t.slow=1.5;else if(flag===2)t.chill=2;else if(flag===3)t.root=1.2;")
    rep("if(c.chill>0)c.chill-=dt;","if(c.chill>0)c.chill-=dt;if(c.root>0)c.root-=dt;")
    rep("spd=T.spd*(c.slow>0?.5:c.chill>0?.75:1)","spd=T.spd*(c.root>0?0:c.slow>0?.5:c.chill>0?.75:1)")
    rep("const EDC=new Map();","/* Rede da Caçadora sobre quem está preso. */\nfunction netFx(c,x,y,r){c.save();c.beginPath();c.ellipse(x,y,r,r*1.15,0,0,TAU);c.strokeStyle='rgba(226,199,154,.95)';c.lineWidth=1.8;c.stroke();c.clip();c.lineWidth=1.2;c.beginPath();for(let j=-3;j<=3;j++){c.moveTo(x+j*r*.36-r*.5,y-r*1.2);c.lineTo(x+j*r*.36+r*.5,y+r*1.2);c.moveTo(x+j*r*.36+r*.5,y-r*1.2);c.lineTo(x+j*r*.36-r*.5,y+r*1.2)}c.stroke();c.restore()}\nconst EDC=new Map();")
    rep("  if(o.bf&4){c.strokeStyle='rgba(159,232,245,.75)'","  if(o.bf&64)netFx(c,o.x,o.y-26,19);\n  if(o.bf&4){c.strokeStyle='rgba(159,232,245,.75)'")
    rep("if(o.hp<o.mhp)bar(o.x,o.y-MON[o.kd].h*","if(o.root>0)netFx(ctx,o.x,o.y-MON[o.kd].h*.5,o.r+8);if(o.hp<o.mhp)bar(o.x,o.y-MON[o.kd].h*")
    # Caçadora
    rep("*s1m,ev===2?2:0);fx('cone',o.x,o.y,{a:ang,r:L,half:hf,T:.3,col:'#bfe6a8'});","*s1m,ev===2?2:ev===1?0:3);fx('cone',o.x,o.y,{a:ang,r:L,half:hf,T:.3,col:'#bfe6a8'});")
    rep("doSkill(H,H.cls,k,px,py,ang,true,outDmg(null,H.dmg),1+.2*tr('s1'),i?0:H.evo);","doSkill(H,H.cls,k,px,py,ang,true,outDmg(null,H.dmg),1+.2*tr('s1'),i?0:H.evo);\n  if(H.cls===1&&!i){burst(H.x,H.y-8,8,'#e2c79a',120,.35,3);const bx=-Math.cos(ang)*13,by=-Math.sin(ang)*13;for(let q=0;q<10;q++)moveC(H,bx,by,13)}")
    rep("d:'leque de flechas que atinge tudo à frente.'","d:'leque de flechas que prende os atingidos numa rede por um instante, enquanto você salta para trás.'")
    rep("d:'Uma flecha longa e estreita que atravessa tudo, com dano alto.'","d:'Uma flecha longa e estreita que atravessa tudo, com dano alto, mas sem rede.'")
    rep("d:'Cone bem mais largo, que deixa os atingidos um pouco lentos.'","d:'Cone bem mais largo que, em vez de prender, deixa os atingidos um pouco lentos.'")
    rep("remove lentidão (com 2 s de imunidade)","remove lentidão e redes (com 2 s de imunidade)")
    return s
s=patch(s);t=patch(t)
open('index.html','w',encoding='utf-8').write(s);open('site/index.html','w',encoding='utf-8').write(t)
print(len(s)//1024,'KB ok (patch26)')
