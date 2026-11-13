import subprocess,time,sys
from playwright.sync_api import sync_playwright
from PIL import Image
out=sys.argv[1]
srv=subprocess.Popen([sys.executable,'-m','http.server','8782','--bind','127.0.0.1','-d','site'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
time.sleep(1);U='http://127.0.0.1:8782/index.html'
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-proxy-server'])
    errs=[]
    ctx=b.new_context(viewport={'width':400,'height':860},device_scale_factor=2)
    ctx.route('**/mqtt.min.js',lambda r:r.abort())
    A=ctx.new_page();A.on('pageerror',lambda e:errs.append(str(e)));A.goto(U);A.wait_for_timeout(1500)
    A.click('label[for=hero0]');A.wait_for_timeout(600);A.screenshot(path=out+'_menu.png')
    A.evaluate("document.getElementById('b-go').click()");A.wait_for_timeout(3600)
    A.evaluate("()=>{__d.xp(1500);__d.H.inv=1e12}");A.wait_for_timeout(300);A.screenshot(path=out+'_p1.png')
    A.keyboard.down('KeyD');A.wait_for_timeout(700);A.screenshot(path=out+'_walk.png');A.keyboard.up('KeyD')
    A.evaluate("()=>{const c=__d.G.creeps.find(c=>c.alive&&c.kd===2);__d.H.x=c.x+110;__d.H.y=c.y+30}");A.wait_for_timeout(1500);A.screenshot(path=out+'_wolf.png');A.wait_for_timeout(350);A.screenshot(path=out+'_wolf2.png')
    A.evaluate("()=>{const c=__d.G.creeps.find(c=>c.alive&&c.kd===3);if(c){__d.H.x=c.x+120;__d.H.y=c.y+40}}");A.wait_for_timeout(1700);A.screenshot(path=out+'_golem.png')
    A.evaluate("()=>{__d.cast(0)}");A.wait_for_timeout(200);A.screenshot(path=out+'_skill.png')
    print('errs',errs);b.close()
srv.kill()
fs=['menu','p1','walk','wolf','wolf2','golem','skill']
w=Image.new('RGB',(400*len(fs),860))
for i,f in enumerate(fs):w.paste(Image.open(out+'_'+f+'.png').resize((400,860)),(i*400,0))
w.save(out+'_sheet.png');Image.open(out+'_wolf.png').crop((0,460,800,1260)).save(out+'_zoom.png');Image.open(out+'_golem.png').crop((0,460,800,1260)).save(out+'_zoom2.png')
