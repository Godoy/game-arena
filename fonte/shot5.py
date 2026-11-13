import subprocess,time,sys
from playwright.sync_api import sync_playwright
from PIL import Image
srv=subprocess.Popen([sys.executable,'-m','http.server','8785','--bind','127.0.0.1','-d','site'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
time.sleep(1);U='http://127.0.0.1:8785/index.html'
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-proxy-server'])
    errs=[]
    ctx=b.new_context(viewport={'width':400,'height':860},device_scale_factor=2)
    ctx.route('**/mqtt.min.js',lambda r:r.abort())
    A=ctx.new_page();A.on('pageerror',lambda e:errs.append(str(e)));A.goto(U);A.wait_for_timeout(1500)
    A.click('label[for=hero0]');A.evaluate("document.getElementById('b-go').click()");A.wait_for_timeout(3600)
    print(A.evaluate("()=>{const H=__d.H,G=__d.G;__d.H.inv=1e12;G.creeps.forEach(c=>{c.x=50;c.y=50});const cs=G.chests.slice(0,5);cs.forEach((c,i)=>{c.q=i;c.x=H.x-120+i*60;c.y=H.y-90});const ev=G.ev;ev.forEach((v,i)=>{v.st=2;v.x=H.x-70+i*140;v.y=H.y+110});return ev.map(v=>v.type+':'+v.st).slice(0,4)}"))
    A.wait_for_timeout(120);A.screenshot(path='a6_props.png')
    A.evaluate("()=>{const B=__d.G.bosses[2];__d.H.x=B.x-90;__d.H.y=B.y+60}");A.wait_for_timeout(700);A.screenshot(path='a6_b2.png')
    print('errs',errs);b.close()
srv.kill()
w=Image.new('RGB',(800,860))
for i,f in enumerate(['props','b2']):w.paste(Image.open('a6_%s.png'%f).resize((400,860)),(i*400,0))
w.save('a6_sheet.jpg',quality=82)
