import subprocess,time,sys
from playwright.sync_api import sync_playwright
from PIL import Image
srv=subprocess.Popen([sys.executable,'-m','http.server','8786','--bind','127.0.0.1','-d','site'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
time.sleep(1);U='http://127.0.0.1:8786/index.html'
def crop(p):
    im=Image.open(p);w,h=im.size;return im.crop((w//2-130,h//2-250,w//2+130,h//2+10))
rows=[];errs=[]
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-proxy-server'])
    for hero in [int(x) for x in sys.argv[1:]]:
        ctx=b.new_context(viewport={'width':400,'height':860},device_scale_factor=2)
        ctx.route('**/mqtt.min.js',lambda r:r.abort())
        A=ctx.new_page();A.on('pageerror',lambda e:errs.append(str(e)));A.goto(U);A.wait_for_timeout(1500)
        A.click('label[for=hero%d]'%hero);A.evaluate("document.getElementById('b-go').click()");A.wait_for_timeout(3600)
        A.evaluate("()=>{__d.xp(1500);__d.G.creeps.forEach(c=>{c.x=60;c.y=60})}");A.wait_for_timeout(2800)
        fr=[]
        A.keyboard.press('KeyE')
        for i in range(7):A.screenshot(path='s6.png');fr.append(crop('s6.png'))
        rows.append(fr);ctx.close()
    b.close()
srv.kill();print('errs',errs)
w=Image.new('RGB',(260*7,260*len(rows)))
for j,fr in enumerate(rows):
    for i,f in enumerate(fr):w.paste(f,(i*260,j*260))
w.resize((w.width*2//3,w.height*2//3)).save('a7_cast.jpg',quality=78)
