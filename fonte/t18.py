import subprocess,time,sys
from playwright.sync_api import sync_playwright
from PIL import Image
srv=subprocess.Popen([sys.executable,'-m','http.server','8778','--bind','127.0.0.1','-d','site'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
time.sleep(1);U='http://127.0.0.1:8778/index.html'
fake=open('fakemqtt.js').read()
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-proxy-server'])
    errs=[]
    def mk():
        ctx=b.new_context(viewport={'width':400,'height':860},device_scale_factor=2)
        ctx.route('**/mqtt.min.js',lambda r:r.fulfill(body=fake,content_type='application/javascript'))
        ctx.route('**/fonts.googleapis.com/**',lambda r:r.abort());return ctx
    ctx=mk()
    def pg():
        p=ctx.new_page();p.on('pageerror',lambda e:errs.append(str(e)));return p
    # --- solo co-op first
    S=pg();S.goto(U);S.wait_for_timeout(400);S.click('#opts summary');S.click('label[for=mode2]');S.wait_for_timeout(200);print('note:',S.inner_text('#mode-note'))
    S.evaluate("document.getElementById('menu').scrollTop=700");S.screenshot(path='s18menu.png')
    S.click('#b-go');S.wait_for_timeout(3500);S.screenshot(path='s18coop.png');print('coop board:',S.inner_text('#h-board').replace('\n',' | '))
    S.evaluate("()=>__d.bossDown()");S.wait_for_timeout(600);S.screenshot(path='s18win.png');S.wait_for_timeout(3800)
    print('end:',S.inner_text('#t-end'),'|',S.inner_text('#end-line'));S.close()
    # --- 3 players, teams + chaos (localStorage is shared, so set options per page right before use)
    A=pg();A.goto(U);A.wait_for_timeout(400);A.fill('#nick','Ana');A.click('label[for=hero0]');A.click('#b-host');A.wait_for_timeout(500);code=A.inner_text('#room-code')
    B=pg();B.goto(U+'#'+code);B.wait_for_timeout(900);B.fill('#nick','Beto');B.click('label[for=hero3]');B.click('label[for=team0]')
    C=pg();C.goto(U+'#'+code);C.wait_for_timeout(900);C.fill('#nick','Caio');C.click('label[for=hero4]');C.click('label[for=team1]');C.wait_for_timeout(1500)
    B.bring_to_front();B.wait_for_timeout(300);B.evaluate("()=>{__d.P.team=0}");B.click('label[for=team1]');B.click('label[for=team0]')
    A.bring_to_front();A.wait_for_timeout(2300);A.click('label[for=team1]');A.click('label[for=team0]');A.click('#opts summary');A.click('label[for=mode1]');A.click('label[for=rules1]');A.wait_for_timeout(2300)
    print('lobby A:',A.inner_text('#room-list').replace('\n',' | '))
    A.click('#b-go');A.wait_for_timeout(500);print('cd:',A.inner_text('#cd-t'))
    t0=time.time()
    while time.time()-t0<15:
        for p in (B,C,A):p.bring_to_front();p.wait_for_timeout(800)
    st=lambda p:p.evaluate("()=>({s:__d.G.state,mode:__d.G.mode,rules:__d.G.rules,team:__d.G.team,sp:__d.G.spawnI,ev:__d.G.ev.length,foes:__d.G.foes.length,allies:__d.G.allies.length})")
    for n,p in (('A',A),('B',B),('C',C)):p.bring_to_front();p.wait_for_timeout(900);print(n,st(p))
    pos=lambda p:p.evaluate("()=>[__d.H.x|0,__d.H.y|0,__d.H.hp|0,__d.H.mhp]")
    # level everyone to 5 and pick evolutions
    for p,ev in ((A,1),(B,1),(C,1)):
        p.bring_to_front();p.evaluate("()=>{__d.xp(2000)}");p.wait_for_timeout(200)
        if p is A:
            p.click('#b-tal');p.wait_for_timeout(300);p.screenshot(path='s18tal.png');p.click('#b-tclose')
        p.evaluate("(i)=>__d.pick(i)",ev);p.wait_for_timeout(200);print('evo',p.evaluate("()=>[__d.H.lv,__d.H.evo]"))
    # gather: A at its spot; B (ally) and C (enemy) nearby
    ax,ay,_,_=pos(A)
    B.bring_to_front();B.evaluate("([x,y])=>{const H=__d.H;H.x=x+60;H.y=y;H.hp=H.mhp*.5;H.hurtAt=1e12;H.inv=0}",[ax,ay]);B.wait_for_timeout(700)
    C.bring_to_front();C.evaluate("([x,y])=>{const H=__d.H;H.x=x-70;H.y=y;H.inv=0;H.hurtAt=1e12}",[ax,ay]);C.wait_for_timeout(700)
    A.bring_to_front();A.wait_for_timeout(900);b0=None
    B.bring_to_front();b0=pos(B);C.bring_to_front();c0=pos(C)
    A.bring_to_front();A.wait_for_timeout(500);A.evaluate("()=>{__d.H.cd1=0;__d.cast(0)}");A.wait_for_timeout(300);A.screenshot(path='s18sagrado.png');A.wait_for_timeout(500)
    B.bring_to_front();B.wait_for_timeout(700);b1=pos(B);C.bring_to_front();C.wait_for_timeout(700);c1=pos(C)
    print('ally B hp',b0[2],'->',b1[2],'(heal expected) | enemy C hp',c0[2],'->',c1[2],'(damage expected)')
    # B wind: A should get haste
    B.bring_to_front();B.evaluate("()=>{__d.H.cd1=0;__d.cast(0)}");B.wait_for_timeout(500)
    A.bring_to_front();A.wait_for_timeout(700);print('A haste from ally:',A.evaluate("()=>__d.H.haste>__d.G.off+performance.now()"),'A hp',pos(A)[2:])
    # C repulsion on A
    C.bring_to_front();cx,cy,_,_=pos(C);a0=pos(A)
    C.evaluate("()=>{__d.H.cd1=0}");C.evaluate("([x,y])=>{const H=__d.H;H.face=Math.atan2(y-H.y,x-H.x);__d.cast(0,{a:H.face,d:1})}",a0[:2]);C.wait_for_timeout(250);C.screenshot(path='s18push.png');C.wait_for_timeout(400)
    A.bring_to_front();A.wait_for_timeout(900);a1=pos(A);print('A pushed: dist to C',int(((a0[0]-cx)**2+(a0[1]-cy)**2)**.5),'->',int(((a1[0]-cx)**2+(a1[1]-cy)**2)**.5),'hp',a0[2],'->',a1[2])
    print('boards:',A.inner_text('#h-board').replace('\n',' | '),'||',C.inner_text('#h-board').replace('\n',' | '))
    # chaos modifier at wave 1
    for p in (A,B,C):p.bring_to_front();p.evaluate("()=>__d.setOff(41000-(__d.G.off+performance.now()))");p.wait_for_timeout(500)
    for n,p in (('A',A),('B',B),('C',C)):p.bring_to_front();p.wait_for_timeout(700);print(n,'wave/mod',p.evaluate("()=>[__d.G.wave,__d.G.mod]"),p.inner_text('#h-mod'),'| ev states',p.evaluate("()=>__d.G.ev.slice(0,3).map(v=>v.st)"))
    A.bring_to_front();A.wait_for_timeout(300);A.screenshot(path='s18chaos.png')
    # end
    for p in (A,B,C):p.bring_to_front();p.evaluate("()=>__d.setOff(__d.G.dur+500-(__d.G.off+performance.now()))");p.wait_for_timeout(600)
    A.bring_to_front();A.wait_for_timeout(2500);print('end:',A.inner_text('#end-line'));A.screenshot(path='s18end.png')
    print('errs',errs);b.close()
srv.kill()
fs=['s18menu','s18coop','s18win','s18tal','s18sagrado','s18push','s18chaos','s18end']
w=Image.new('RGB',(3200,860))
for i,f in enumerate(fs):w.paste(Image.open(f+'.png').resize((400,860)),(i*400,0))
w.save('s18sheet.png')
