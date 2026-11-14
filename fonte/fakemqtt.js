window.mqtt={connect(url,o){const h={},bc=new BroadcastChannel('mq'+url);let subs=[];
 const c={connected:false,on(e,f){(h[e]=h[e]||[]).push(f)},subscribe(t){subs.push(new RegExp('^'+t.replace('+','[^/]+')+'$'))},
  publish(t,m){bc.postMessage({t,m})},end(){setTimeout(()=>bc.close(),50);c.connected=false}};
 bc.onmessage=e=>{if(subs.some(r=>r.test(e.data.t)))(h.message||[]).forEach(f=>f(e.data.t,new TextEncoder().encode(e.data.m)))};
 if(!(window.DEADBROKER&&url.includes(window.DEADBROKER)))setTimeout(()=>{c.connected=true;(h.connect||[]).forEach(f=>f())},80);return c}};
