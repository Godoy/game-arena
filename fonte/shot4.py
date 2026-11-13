import subprocess,time,sys
from playwright.sync_api import sync_playwright
from PIL import Image
srv=subprocess.Popen([sys.executable,'-m','http.server','8784','--bind','127.0.0.1','-d','site'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
time.sleep(1);U='http://127.0.0.1:8784/index.html'
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-proxy-server'])
    errs=[]
    ctx=b.new_context(viewport={'width':400,'height':860},device_scale_factor=2)
    ctx.route('**/mqtt.min.js',lambda r:r.abort())
    A=ctx.new_page();A.on('pageerror',lambda e:errs.append(str(e)));A.goto(U);A.wait_for_timeout(1500)
    A.click('label[for=hero0]');A.evaluate("document.getElementById('b-go').click()");A.wait_for_timeout(3600)
    A.evaluate("()=>{__d.xp(1500);__d.H.inv=1e12;const cs=__d.G.creeps.filter(c=>c.alive).slice(0,8);cs.forEach((c,i)=>{c.kd=i+1;c.x=__d.H.x-150+(i%4)*100;c.y=__d.H.y-150+((i/4)|0)*110;c.hp=c.mhp=1e9;c.dmg=0})}")
    A.wait_for_timeout(250);A.screenshot(path='a5_creeps.png')
    fr=[]
    for i in range(3):
        A.evaluate("(i)=>{const B=__d.G.bosses[i];__d.H.x=B.x-90;__d.H.y=B.y+60}",i);A.wait_for_timeout(700);A.screenshot(path='a5_b%d.png'%i)
    print('errs',errs);b.close()
srv.kill()
w=Image.new('RGB',(1600,860))
for i,f in enumerate(['creeps','b0','b1','b2']):w.paste(Image.open('a5_%s.png'%f).resize((400,860)),(i*400,0))
w.save('a5_sheet.jpg',quality=80)
