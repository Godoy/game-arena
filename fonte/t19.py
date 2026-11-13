import subprocess,time,sys
from playwright.sync_api import sync_playwright
from PIL import Image
srv=subprocess.Popen([sys.executable,'-m','http.server','8781','--bind','127.0.0.1','-d','site'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
time.sleep(1);U='http://127.0.0.1:8781/index.html'
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-proxy-server'])
    errs=[];shots=[]
    for (W,Hh) in ((360,640),(400,780)):
        ctx=b.new_context(viewport={'width':W,'height':Hh},device_scale_factor=2)
        ctx.route('**/mqtt.min.js',lambda r:r.abort())
        A=ctx.new_page();A.on('pageerror',lambda e:errs.append(str(e)));A.goto(U);A.wait_for_timeout(1500)
        A.screenshot(path='m%d_a.png'%W);shots.append('m%d_a'%W)
        A.click('#opts summary');A.wait_for_timeout(200);A.evaluate("document.getElementById('menu').scrollTop=380");A.wait_for_timeout(200);A.screenshot(path='m%d_b.png'%W);shots.append('m%d_b'%W)
        A.click('#opts summary')
        for cls in (2,0):
            A.evaluate("document.getElementById('menu').scrollTop=0");A.click('label[for=hero%d]'%cls);A.evaluate("document.getElementById('b-go').click()");A.wait_for_timeout(3300)
            hh=lambda:A.evaluate("()=>{const r=document.querySelector('#tal .inner').getBoundingClientRect();return [Math.round(r.height),Math.round(r.top),innerHeight]}")
            A.click('#b-tal');A.wait_for_timeout(250);print(W,cls,'lv1',hh())
            A.click('#b-tclose');A.evaluate("()=>__d.xp(700)");A.click('#b-tal');A.wait_for_timeout(250);print(W,cls,'lv5 evo pending',hh(),A.evaluate("()=>__d.H.lv"))
            if cls==2:A.screenshot(path='t%d_evo.png'%W);shots.append('t%d_evo'%W)
            A.evaluate("()=>__d.pick(0)");A.wait_for_timeout(200)
            # learn everything
            A.evaluate("()=>__d.xp(40000)")
            for q in range(30):
                n=A.evaluate("()=>{const b=[...document.querySelectorAll('#t-tree .node')].find(b=>!b.disabled);if(b){b.click();return 1}return 0}")
                if not n:break
            A.wait_for_timeout(250);print(W,cls,'full+attrs',hh())
            if cls==2:A.screenshot(path='t%d_full.png'%W);shots.append('t%d_full'%W)
            A.click('#b-tclose');A.screenshot(path='h%d_%d.png'%(W,cls))
            if cls==0:shots.append('h%d_0'%W)
            A.click('#b-menu');A.click('#b-quit');A.wait_for_timeout(300)
        ctx.close()
    print('errs',errs);b.close()
srv.kill()
w=Image.new('RGB',(400*len(shots),780),'#000')
for i,f in enumerate(shots):
    im=Image.open(f+'.png');im=im.resize((im.width//2,im.height//2));w.paste(im,(i*400,0))
w.save('s19sheet.png')
