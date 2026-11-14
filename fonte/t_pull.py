import subprocess,time,sys
from playwright.sync_api import sync_playwright
srv=subprocess.Popen([sys.executable,'-m','http.server','8779','--bind','127.0.0.1','-d','site'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
time.sleep(1);U='http://127.0.0.1:8779/index.html';fake=open('fakemqtt.js').read()
try:
  with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-proxy-server']);errs=[]
    ctx=b.new_context(viewport={'width':400,'height':860});ctx.route('**/mqtt.min.js',lambda r:r.fulfill(body=fake,content_type='application/javascript'));ctx.route('**/fonts.googleapis.com/**',lambda r:r.abort())
    ctx.add_init_script("if(!localStorage.getItem('arena-celeste'))localStorage.setItem('arena-celeste','{}')")
    def pg():
        p=ctx.new_page();p.on('pageerror',lambda e:errs.append(str(e)));return p
    A=pg();A.goto(U);A.wait_for_timeout(500);A.fill('#nick','Ana');A.click('label[for=hero4]');A.click('#b-host');A.wait_for_timeout(600);code=A.inner_text('#room-code')
    B=pg();B.goto(U+'#'+code);B.wait_for_timeout(900);B.fill('#nick','Beto');B.click('label[for=hero0]');B.wait_for_timeout(1500)
    A.bring_to_front();A.wait_for_timeout(2300);print('sala:',A.inner_text('#room-list').replace('\n',' | '));A.click('#b-go');A.wait_for_timeout(500)
    t0=time.time()
    while time.time()-t0<14:
        for p in (B,A):p.bring_to_front();p.wait_for_timeout(800)
    pos=lambda p:p.evaluate("()=>[__d.H.x|0,__d.H.y|0,__d.H.hp|0]")
    print('estados',A.evaluate("()=>[__d.G.state,__d.G.foes.length]"),B.evaluate("()=>[__d.G.state,__d.G.foes.length]"))
    ax,ay,_=pos(A)
    B.bring_to_front();B.evaluate("([x,y])=>{const H=__d.H;H.x=x+200;H.y=y;H.inv=0;H.hurtAt=1e12}",[ax,ay]);B.wait_for_timeout(900);b0=pos(B)
    A.bring_to_front();A.wait_for_timeout(1200);print('A vê B em',A.evaluate("()=>__d.G.foes.map(f=>[f.x|0,f.y|0,f.bf])"),'A em',pos(A)[:2])
    A.evaluate("([x,y])=>{const H=__d.H;H.cd1=0;H.face=Math.atan2(y-H.y,x-H.x);__d.cast(0,{a:H.face,d:1})}",b0[:2]);A.wait_for_timeout(500)
    B.bring_to_front();B.wait_for_timeout(1200);b1=pos(B)
    print('B antes',b0,'depois',b1,'distância até A:',int(((b0[0]-ax)**2+(b0[1]-ay)**2)**.5),'->',int(((b1[0]-ax)**2+(b1[1]-ay)**2)**.5))
    # fim de partida: B sai e A deve manter B no ranking
    A.bring_to_front();A.evaluate("()=>__end()");A.wait_for_timeout(1200);n0=A.evaluate("()=>document.querySelectorAll('#rank tbody tr').length")
    B.bring_to_front();B.evaluate("()=>__end()");B.wait_for_timeout(500);B.click('#b-again');B.wait_for_timeout(1500)
    A.bring_to_front();A.wait_for_timeout(3500);print('ranking de A: antes',n0,'depois de B sair',A.evaluate("()=>document.querySelectorAll('#rank tbody tr').length"),A.inner_text('#rank tbody').replace('\n',' ').replace('\t',' '))
    A.click('#b-again');A.wait_for_timeout(600);A.evaluate("document.getElementById('menu').scrollTop=0");A.screenshot(path='/home/claude/work/menu_room.png')
    S=pg();S.goto(U);S.wait_for_timeout(900);S.screenshot(path='/home/claude/work/menu_new.png',full_page=False)
    S.evaluate("document.getElementById('b-go').click()");S.wait_for_timeout(3800);print('pedra: golpes necessários (amostra)',S.evaluate("()=>{const m=__d.G.map,o=[];for(let i=0;i<m.g.length&&o.length<8;i++)if(m.g[i]===1)o.push(3+m.deco[i]%3);return o}"))
    print('errs',errs);b.close()
finally:srv.kill()
