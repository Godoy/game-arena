import subprocess,time,sys
from playwright.sync_api import sync_playwright
from PIL import Image
srv=subprocess.Popen([sys.executable,'-m','http.server','8775','--bind','127.0.0.1','-d','site'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
time.sleep(1);U='http://127.0.0.1:8775/index.html'
fake=open('fakemqtt.js').read()
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-proxy-server'])
    errs=[]
    ctx=b.new_context(viewport={'width':400,'height':860},device_scale_factor=2)
    ctx.route('**/mqtt.min.js',lambda r:r.fulfill(body=fake,content_type='application/javascript'))
    ctx.route('**/fonts.googleapis.com/**',lambda r:r.abort())
    def pg():
        p=ctx.new_page();p.on('pageerror',lambda e:errs.append(str(e)));return p
    A=pg();A.goto(U);A.wait_for_timeout(400);A.fill('#nick','Ana');A.click('label[for=hero0]');A.click('label[for=size1]')
    A.click('#b-host');A.wait_for_timeout(500);code=A.inner_text('#room-code')
    B=pg();B.goto(U+'#'+code);B.wait_for_timeout(800);B.fill('#nick','Beto');B.click('label[for=hero1]');B.wait_for_timeout(1500)
    A.bring_to_front();A.wait_for_timeout(2300);A.click('#b-go')
    t0=time.time()
    while time.time()-t0<14:
        for p in (B,A):p.bring_to_front();p.wait_for_timeout(1000)
    print('ev A',A.evaluate("()=>__d.G.ev.map(v=>[v.k,v.type,v.t0/1000,v.x|0,v.y|0])"));print('ev B',B.evaluate("()=>__d.G.ev.map(v=>[v.k,v.type,v.x|0,v.y|0])"))
    print('portals',A.evaluate("()=>__d.G.portals.map(p=>[p.x|0,p.y|0])"),B.evaluate("()=>__d.G.portals.map(p=>[p.x|0,p.y|0])"))
    # portal
    A.bring_to_front();A.evaluate("()=>{const p=__d.G.portals[0];__d.H.x=p.x+60;__d.H.y=p.y}");A.wait_for_timeout(300);A.screenshot(path='s15portal.png')
    A.evaluate("()=>{const p=__d.G.portals[0];__d.H.x=p.x;__d.H.y=p.y}");A.wait_for_timeout(300)
    print('after portal',A.evaluate("()=>{const p=__d.G.portals[1];return [Math.hypot(__d.H.x-p.x,__d.H.y-p.y)|0]}"))
    # jump time to 66s on both
    for p in (A,B):p.bring_to_front();p.evaluate("()=>__d.setOff(66000-(__d.G.off+performance.now()))");p.wait_for_timeout(600)
    A.bring_to_front();A.wait_for_timeout(700);print('A toasts',A.inner_text('#toasts').replace('\n',' / '))
    A.evaluate("()=>{const v=__d.G.ev[0];__d.H.x=v.x+40;__d.H.y=v.y+150;__d.H.inv=1e12}");A.wait_for_timeout(500);A.screenshot(path='s15ann.png')
    for q in range(12):
        for p in (B,A):p.bring_to_front();p.wait_for_timeout(700)
        if A.evaluate("()=>__d.G.ev[0].st")==2:break
    A.wait_for_timeout(600);A.screenshot(path='s15altar.png');print('guards',A.evaluate("()=>__d.G.creeps.filter(c=>c.ev===0).map(c=>[c.id,c.alive,c.hp|0])"))
    A.evaluate("()=>{const v=__d.G.ev[0];__d.H.x=v.x;__d.H.y=v.y+30}");A.wait_for_timeout(400);print('note',A.evaluate("()=>__d.G.ev[0].note"))
    A.evaluate("()=>{__d.G.creeps.forEach(c=>{if(c.ev===0&&c.alive)__d.kill(c)})}")
    for q in range(3):
        A.wait_for_timeout(400)
        if not A.evaluate("()=>__d.G.creeps.some(c=>c.ev===0&&c.alive)"):break
    print('guards dead after',q,'note',A.evaluate("()=>[__d.G.ev[0].note,__d.G.ev[0].cap.toFixed(2)]"))
    # B comes in -> contested
    B.bring_to_front();B.wait_for_timeout(500);print('B guards',B.evaluate("()=>__d.G.creeps.filter(c=>c.ev===0).map(c=>c.alive)"),'B sees prog',B.evaluate("()=>__d.others.values().next().value.ea"))
    B.evaluate("()=>{const v=__d.G.ev[0];__d.H.x=v.x+20;__d.H.y=v.y-30;__d.H.inv=1e12}");B.wait_for_timeout(800);B.screenshot(path='s15contest.png')
    A.bring_to_front();A.wait_for_timeout(1200);print('contested note',A.evaluate("()=>[__d.G.ev[0].note,__d.G.ev[0].cap.toFixed(2)]"))
    B.bring_to_front();B.evaluate("()=>{__d.H.x+=400}");B.wait_for_timeout(600)
    A.bring_to_front()
    for q in range(30):
        A.wait_for_timeout(400)
        if A.evaluate("()=>__d.G.ev[0].st")==3:break
    A.wait_for_timeout(200);A.screenshot(path='s15won.png');print('A won',A.evaluate("()=>[__d.G.ev[0].by,__d.H.bless>0,document.getElementById('h-gl').textContent,document.getElementById('h-st').textContent]"))
    B.bring_to_front();B.wait_for_timeout(700);print('B sees',B.evaluate("()=>[__d.G.ev[0].st,__d.G.ev[0].by]"),B.inner_text('#toasts').replace('\n',' / '))
    # cursed chest at 195s
    for p in (A,B):p.bring_to_front();p.evaluate("()=>__d.setOff(187000-(__d.G.off+performance.now()))");p.wait_for_timeout(500)
    for q in range(16):
        for p in (B,A):p.bring_to_front();p.wait_for_timeout(600)
        if B.evaluate("()=>__d.G.ev[1].st")==2:break
    B.bring_to_front();B.evaluate("()=>{const v=__d.G.ev[1];__d.H.x=v.x+70;__d.H.y=v.y+40}");B.wait_for_timeout(500);B.screenshot(path='s15chest.png')
    B.evaluate("()=>{const v=__d.G.ev[1];__d.H.x=v.x;__d.H.y=v.y+10}");B.wait_for_timeout(700);B.screenshot(path='s15cursed.png')
    print('B cursed',B.evaluate("()=>[__d.H.curse>0,Object.keys(__d.H.rel),document.getElementById('h-st').textContent]"))
    A.bring_to_front();A.wait_for_timeout(900);print('A sees',A.evaluate("()=>[__d.G.ev[1].st,__d.G.ev[1].by,__d.others.values().next().value.bf&16]"),A.inner_text('#toasts').replace('\n',' / '));A.screenshot(path='s15amap.png')
    print('errs',errs);b.close()
srv.kill()
fs=['s15portal','s15ann','s15altar','s15contest','s15won','s15chest','s15cursed','s15amap']
w=Image.new('RGB',(3200,860))
for i,f in enumerate(fs):w.paste(Image.open(f+'.png').resize((400,860)),(i*400,0))
w.save('s15sheet.png')
