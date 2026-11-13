import subprocess,time,sys
from playwright.sync_api import sync_playwright
from PIL import Image
srv=subprocess.Popen([sys.executable,'-m','http.server','8783','--bind','127.0.0.1','-d','site'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
time.sleep(1);U='http://127.0.0.1:8783/index.html'
def crop(p):
    im=Image.open(p);w,h=im.size;return im.crop((w//2-110,h//2-230,w//2+110,h//2+10))
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-proxy-server'])
    errs=[]
    ctx=b.new_context(viewport={'width':400,'height':860},device_scale_factor=2)
    ctx.route('**/mqtt.min.js',lambda r:r.abort())
    A=ctx.new_page();A.on('pageerror',lambda e:errs.append(str(e)));A.goto(U);A.wait_for_timeout(1500)
    A.click('label[for=hero0]');A.evaluate("document.getElementById('b-go').click()");A.wait_for_timeout(3600)
    A.evaluate("()=>{__d.xp(1500);}")
    fr=[]
    for i in range(8):A.wait_for_timeout(150);A.screenshot(path='s3.png');fr.append(crop('s3.png'))
    A.keyboard.down('KeyD')
    for i in range(8):A.wait_for_timeout(60);A.screenshot(path='s3.png');fr.append(crop('s3.png'))
    A.keyboard.up('KeyD');A.keyboard.down('KeyA')
    for i in range(8):A.wait_for_timeout(30);A.screenshot(path='s3.png');fr.append(crop('s3.png'))
    A.keyboard.up('KeyA')
    A.evaluate("()=>{const c=__d.G.creeps.find(c=>c.alive&&c.kd===2);__d.H.x=c.x-70;__d.H.y=c.y}")
    A.wait_for_timeout(500)
    for i in range(8):A.wait_for_timeout(25);A.screenshot(path='s3.png');fr.append(crop('s3.png'))
    print('errs',errs);b.close()
srv.kill()
w=Image.new('RGB',(220*8,240*4))
for i,f in enumerate(fr):w.paste(f,((i%8)*220,(i//8)*240))
w.save('a3_strip.jpg',quality=80)
