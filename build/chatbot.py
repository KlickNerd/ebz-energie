"""Website-Chatbot (EBZ Energie-Assistent): Gestaltung, Chatfenster und Skript.

Uebernommen aus dem WordPress-Snippet "ChatBot" (WPCode, ID 6745) der alten Seite am 21.10.2026 und an die neue
Website angepasst: Markenfarben und -schriften, keine Akzentstreifen, keine zusaetzliche H2 je Seite, keine
Gedankenstriche, kein Emoji, "Finanzierung" statt "Leasing", Platz fuer die mobile Anruf-/Beratungsleiste.

Das Skript spricht mit dem Cloudflare-Worker (common.CHATBOT_URL): /chat fuer Antworten, /lead fuer Anfragen
(Weiterleitung an Make, E-Mail an office@). Der Worker erlaubt nur bekannte Herkunftsadressen (CORS), siehe
chatbot/worker.js (lokal, nicht im Repo). Der Gespraechsverlauf liegt 6 Stunden im localStorage des Besuchers;
das steht in der Datenschutzerklaerung (build/pages/datenschutz.py).

Einbindung: theme.write_assets() haengt CHATBOT_CSS an styles.css an und schreibt CHATBOT_JS nach
/assets/js/chatbot.js; layout.page() setzt CHATBOT_HTML vor </body>.
"""

CHATBOT_CSS = r"""
#ebzc, #ebzc *{box-sizing:border-box;margin:0;padding:0}
#ebzc{
  --slate:#082e3d;--slate2:#0e4d64;--cream:#f5f8f9;--cream2:#e4ebed;
  --amber:#f5a623;--amberD:#e0951a;--glow:rgba(245,166,35,.32);
  --ink:#152730;--muted:#5c6f77;--line:#e4ebed;--green:#1f9d62;
  font-family:'Source Sans 3',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  position:fixed;right:22px;bottom:22px;z-index:99999;
}
#ebzc-launch{
  width:60px;height:60px;border-radius:50%;border:none;cursor:pointer;
  background:linear-gradient(150deg,var(--amber),var(--amberD));
  box-shadow:0 10px 30px var(--glow);display:flex;align-items:center;justify-content:center;
  transition:transform .18s;
}
#ebzc-launch:hover{transform:translateY(-2px) scale(1.04)}
#ebzc-launch svg{width:30px;height:30px}
#ebzc-teaser{position:absolute;right:4px;bottom:80px;width:248px;max-width:calc(100vw - 48px);box-sizing:border-box;background:#fff;color:var(--ink);border:1px solid var(--line);border-radius:16px;border-bottom-right-radius:6px;box-shadow:0 16px 38px -12px rgba(0,0,0,.32);padding:13px 32px 13px 15px;font-size:13.5px;line-height:1.45;cursor:pointer;display:none}
#ebzc.teaser-on #ebzc-teaser{display:block;animation:ebzc-pop .35s cubic-bezier(.2,.9,.3,1.3)}
#ebzc-teaser:after{content:"";position:absolute;right:22px;bottom:-7px;width:13px;height:13px;background:#fff;border-right:1px solid var(--line);border-bottom:1px solid var(--line);transform:rotate(45deg)}
#ebzc-teaser .tc{position:absolute;top:6px;right:7px;width:19px;height:19px;border:none;background:transparent;color:var(--muted);cursor:pointer;font-size:15px;line-height:1;border-radius:6px}
#ebzc-teaser .tc:hover{background:var(--cream2)}
@keyframes ebzc-pop{from{opacity:0;transform:translateY(10px) scale(.92)}to{opacity:1;transform:translateY(0) scale(1)}}
#ebzc-panel{
  position:absolute;right:0;bottom:74px;width:380px;max-width:calc(100vw - 32px);
  height:min(600px,calc(100vh - 120px));background:var(--cream);border-radius:20px;overflow:hidden;
  display:none;flex-direction:column;box-shadow:0 28px 70px -18px rgba(0,0,0,.45),0 0 0 1px rgba(0,0,0,.04);
  animation:ebzc-up .22s ease;
}
#ebzc.open #ebzc-panel{display:flex}
@keyframes ebzc-up{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
#ebzc .hd{background:linear-gradient(150deg,var(--slate),var(--slate2));padding:16px 18px;color:#fff;position:relative;flex:none}
#ebzc .hdrow{display:flex;align-items:center;gap:11px}
#ebzc .bdg{width:40px;height:40px;border-radius:12px;flex:none;background:radial-gradient(circle at 50% 38%,#ffd789,var(--amber) 58%,var(--amberD));display:flex;align-items:center;justify-content:center;box-shadow:0 6px 18px var(--glow)}
#ebzc .bdg svg{width:23px;height:23px}
#ebzc .hd .ttl{font-family:'Sora',sans-serif;font-weight:700;font-size:16px;letter-spacing:-.01em;color:#fff !important;margin:0}
#ebzc .hd .sub{font-size:12px;color:#c6dbe2;margin-top:2px;display:flex;align-items:center;gap:6px}
#ebzc .dot{width:7px;height:7px;border-radius:50%;background:var(--green);box-shadow:0 0 0 3px rgba(63,157,90,.18)}
#ebzc .x{position:absolute;top:14px;right:14px;background:rgba(255,255,255,.12);border:none;color:#fff;width:28px;height:28px;border-radius:8px;cursor:pointer;font-size:18px;line-height:1}
#ebzc .stream{flex:1;overflow-y:auto;padding:18px 14px 6px;display:flex;flex-direction:column;gap:11px;background:radial-gradient(600px 240px at 100% 0%,rgba(246,166,35,.06),transparent 60%),var(--cream)}
#ebzc .stream::-webkit-scrollbar{width:8px}
#ebzc .stream::-webkit-scrollbar-thumb{background:var(--cream2);border-radius:8px;border:2px solid var(--cream)}
#ebzc .m{max-width:85%;font-size:14px;line-height:1.5;padding:10px 13px;border-radius:15px;white-space:pre-wrap;word-wrap:break-word}
#ebzc .m.b{background:#fff;border:1px solid var(--line);border-bottom-left-radius:5px;align-self:flex-start;color:var(--ink)}
#ebzc .m.u{background:var(--slate);color:#fff;border-bottom-right-radius:5px;align-self:flex-end}
#ebzc .typ{align-self:flex-start;background:#fff;border:1px solid var(--line);border-bottom-left-radius:5px;padding:12px 15px;border-radius:15px;display:flex;gap:5px}
#ebzc .typ i{width:7px;height:7px;border-radius:50%;background:#c9bfab;animation:ebzc-bb 1.2s infinite}
#ebzc .typ i:nth-child(2){animation-delay:.18s}#ebzc .typ i:nth-child(3){animation-delay:.36s}
@keyframes ebzc-bb{0%,60%,100%{opacity:.35;transform:translateY(0)}30%{opacity:1;transform:translateY(-4px)}}
#ebzc .chips{display:flex;flex-wrap:wrap;gap:7px;padding:2px 14px 10px}
#ebzc .chip{font-size:12px;font-weight:600;color:var(--ink);background:#fff;border:1px solid var(--line);padding:7px 11px;border-radius:99px;cursor:pointer;transition:.15s;font-family:inherit}
#ebzc .chip:hover{border-color:var(--slate2);color:var(--slate2)}
#ebzc .lead{align-self:stretch;background:#fff;border:1px solid var(--line);border-radius:15px;padding:13px 15px;box-shadow:0 8px 22px -10px var(--glow)}
#ebzc .lead .t{display:flex;align-items:center;gap:8px;font-family:'Sora',sans-serif;font-weight:700;font-size:14px;color:var(--ink)}
#ebzc .lead .t svg{width:17px;height:17px}
#ebzc .lead dl{margin-top:9px;display:grid;grid-template-columns:auto 1fr;gap:4px 12px;font-size:12.5px}
#ebzc .lead dt{color:var(--muted);font-weight:600}#ebzc .lead dd{color:var(--ink)}
#ebzc .ft{flex:none;padding:11px 13px 13px;background:var(--cream);border-top:1px solid var(--line)}
#ebzc .row{display:flex;gap:8px;align-items:flex-end}
#ebzc textarea{flex:1;resize:none;border:1px solid var(--line);background:#fff;border-radius:13px;padding:10px 12px;font-family:inherit;font-size:14px;color:var(--ink);max-height:90px;line-height:1.4;outline:none;transition:.15s}
#ebzc textarea:focus{border-color:var(--amber);box-shadow:0 0 0 3px var(--glow)}
#ebzc .snd{flex:none;width:42px;height:42px;border:none;border-radius:12px;cursor:pointer;background:linear-gradient(150deg,var(--amber),var(--amberD));display:flex;align-items:center;justify-content:center;transition:.15s;box-shadow:0 5px 14px var(--glow)}
#ebzc .snd:hover{transform:translateY(-1px)}#ebzc .snd:disabled{opacity:.45;cursor:not-allowed;transform:none}
#ebzc .snd svg{width:19px;height:19px}
#ebzc .dis{text-align:center;font-size:11px;color:var(--muted);margin-top:8px}
#ebzc .m.b a{color:var(--slate2)!important;font-weight:600}
#ebzc button:focus-visible,#ebzc textarea:focus-visible{outline:3px solid var(--amber);outline-offset:2px}
@media(max-width:720px){#ebzc{right:14px;bottom:84px}#ebzc-launch{width:54px;height:54px}#ebzc-panel{bottom:66px;height:min(560px,calc(100vh - 190px))}}
@media print{#ebzc{display:none}}
"""

CHATBOT_HTML = r"""
<div id="ebzc">
  <div id="ebzc-panel">
    <div class="hd">
      <button class="x" id="ebzc-x" aria-label="Schließen">×</button>
      <div class="hdrow">
        <div class="bdg"><svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="4.5" fill="#082e3d"/><g stroke="#082e3d" stroke-width="1.8" stroke-linecap="round"><path d="M12 2.5v2.6M12 18.9v2.6M21.5 12h-2.6M5.1 12H2.5M18.7 5.3l-1.8 1.8M7.1 16.9l-1.8 1.8M18.7 18.7l-1.8-1.8M7.1 7.1L5.3 5.3"/></g></svg></div>
        <div><p class="ttl">EBZ Energie-Assistent</p><div class="sub"><span class="dot"></span> Antwortet sofort · Team Mo bis Fr 10 bis 20 Uhr</div></div>
      </div>
    </div>
    <div class="stream" id="ebzc-stream"></div>
    <div class="chips" id="ebzc-chips"></div>
    <div class="ft">
      <div class="row">
        <textarea id="ebzc-in" rows="1" placeholder="Ihre Frage zu PV, Wärmepumpe oder Förderung"></textarea>
        <button class="snd" id="ebzc-snd" aria-label="Senden"><svg viewBox="0 0 24 24" fill="none"><path d="M4 12l16-8-6 16-2.5-6.5L4 12z" fill="#082e3d"/></svg></button>
      </div>
      <div class="dis">KI-Assistent · kann Fehler machen · keine verbindliche Förderzusage</div>
    </div>
  </div>
  <div id="ebzc-teaser"><button class="tc" id="ebzc-teaser-close" aria-label="Schließen">×</button>Grüß Sie! Fragen zu Photovoltaik, Wärmepumpe oder Förderung? Ich helfe Ihnen gern weiter.</div>
  <button id="ebzc-launch" aria-label="Chat öffnen">
    <svg viewBox="0 0 24 24" fill="none"><path d="M4 5.5A2.5 2.5 0 016.5 3h11A2.5 2.5 0 0120 5.5v8A2.5 2.5 0 0117.5 16H9l-4 4v-4H6.5A2.5 2.5 0 014 13.5v-8z" fill="#082e3d"/></svg>
  </button>
</div>
"""

CHATBOT_JS = r"""
(function(){
  var WORKER_URL = "__CHATBOT_URL__"; /* aus common.CHATBOT_URL */

  var root=document.getElementById('ebzc');
  var panel=document.getElementById('ebzc-panel');
  var stream=document.getElementById('ebzc-stream');
  var chips=document.getElementById('ebzc-chips');
  var inp=document.getElementById('ebzc-in');
  var snd=document.getElementById('ebzc-snd');
  var history=[],busy=false,greeted=false,leadSent=false,restoring=false;
  var STARTERS=["Lohnt sich PV für mein Haus?","Was kostet die Finanzierung?","Welche Förderung gibt es?","Ich möchte eine Beratung"];
  var SKEY='ebzc_chat_v1', TTL=6*60*60*1000; // Verlauf 6 Stunden aufbewahren
  function saveState(){try{localStorage.setItem(SKEY,JSON.stringify({history:history,leadSent:leadSent,greeted:greeted,open:root.classList.contains('open'),ts:Date.now()}));}catch(e){}}
  function loadState(){try{var s=JSON.parse(localStorage.getItem(SKEY));if(s&&s.ts&&Date.now()-s.ts<TTL)return s;}catch(e){}return null;}

  function esc(s){return s.replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c];});}
  function render(s){s=esc(s);s=s.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,function(_,t,u){return '<a href="'+u+'" target="_blank" rel="noopener" style="text-decoration:underline">'+t+'</a>';});s=s.replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>');return s;}
  function add(role,txt){var d=document.createElement('div');d.className='m '+(role==='user'?'u':'b');if(role==='user'){d.textContent=txt;}else{d.innerHTML=render(txt);}stream.appendChild(d);if(restoring)return;if(role==='user'){stream.scrollTop=stream.scrollHeight;}else{var target=stream.scrollTop+(d.getBoundingClientRect().top-stream.getBoundingClientRect().top)-12;stream.scrollTo({top:target<0?0:target,behavior:'smooth'});}}
  function typ(on){var t=document.getElementById('ebzc-typ');if(on){if(t)return;t=document.createElement('div');t.className='typ';t.id='ebzc-typ';t.innerHTML='<i></i><i></i><i></i>';stream.appendChild(t);stream.scrollTop=stream.scrollHeight;}else if(t)t.remove();}
  function renderChips(list){chips.innerHTML='';list.forEach(function(t){var c=document.createElement('button');c.className='chip';c.textContent=t;c.onclick=function(){chips.innerHTML='';send(t);};chips.appendChild(c);});}
  function leadCard(d){
    var card=document.createElement('div');card.className='lead';
    function r(l,v){return v?'<dt>'+esc(l)+'</dt><dd>'+esc(v)+'</dd>':'';}
    card.innerHTML='<div class="t"><svg viewBox="0 0 24 24" fill="none"><path d="M5 12.5l4.5 4.5L19 6" stroke="#1f9d62" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg> Anfrage übermittelt</div>'+
      '<dl>'+r('Name',d.name)+r('Kontakt',d.kontakt)+r('Region',d.region)+r('Anliegen',d.anliegen)+r('Zeitfenster',d.zeitfenster)+'</dl>';
    stream.appendChild(card);stream.scrollTop=stream.scrollHeight;
    // Lead an den Worker, der leitet an Make weiter (E-Mail an office@)
    fetch(WORKER_URL+"/lead",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({lead:d})}).catch(function(){});
  }

  function send(text){
    if(busy)return;text=(text||'').trim();if(!text)return;
    busy=true;snd.disabled=true;chips.innerHTML='';
    add('user',text);history.push({role:'user',content:text});saveState();
    inp.value='';inp.style.height='auto';typ(true);
    fetch(WORKER_URL+"/chat",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({messages:history})})
      .then(function(r){return r.json();})
      .then(function(data){
        typ(false);
        var reply=(data&&data.reply)?data.reply:"";
        if(!reply){add('b',"Entschuldigung, das hat gerade nicht geklappt. Rufen Sie uns gern an: +43 650 220 26 26.");busy=false;snd.disabled=false;return;}
        var lead=null,m=reply.match(/<<LEAD>>\s*({[\s\S]*?})\s*$/);
        if(m){try{lead=JSON.parse(m[1]);}catch(e){}reply=reply.replace(/<<LEAD>>[\s\S]*$/,'').trim();}
        if(reply)add('b',reply);
        history.push({role:'assistant',content:reply||"…"});
        if(lead&&!leadSent){leadSent=true;leadCard(lead);}
        saveState();
        busy=false;snd.disabled=false;inp.focus();
      })
      .catch(function(){typ(false);add('b',"Verbindungsproblem. Rufen Sie uns gern direkt an: +43 650 220 26 26.");busy=false;snd.disabled=false;});
  }

  function openPanel(){
    hideTeaser(true);
    root.classList.add('open');
    if(!greeted){greeted=true;add('b',"Grüß Sie! Ich bin der Energie-Assistent von EBZ. Fragen Sie mich zu Photovoltaik, Wärmepumpe, Speicher oder Förderung, oder wir vereinbaren gleich eine kostenlose Erstberatung. Womit kann ich helfen?");renderChips(STARTERS);}
    saveState();
    setTimeout(function(){inp.focus();},120);
  }
  document.getElementById('ebzc-launch').onclick=function(){if(root.classList.contains('open')){root.classList.remove('open');saveState();}else{openPanel();}};
  document.getElementById('ebzc-x').onclick=function(){root.classList.remove('open');saveState();};
  snd.onclick=function(){send(inp.value);};
  inp.addEventListener('keydown',function(e){if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();send(inp.value);}});
  inp.addEventListener('input',function(){inp.style.height='auto';inp.style.height=Math.min(inp.scrollHeight,90)+'px';});

  // Gesprächsverlauf von vorheriger Seite wiederherstellen
  (function(){
    var s=loadState();
    if(s&&s.history&&s.history.length){
      restoring=true;
      history=s.history; leadSent=!!s.leadSent; greeted=true;
      s.history.forEach(function(m){ add(m.role==='user'?'user':'b', m.content); });
      restoring=false;
      stream.scrollTop=stream.scrollHeight;
      if(s.open){ root.classList.add('open'); setTimeout(function(){inp.focus();},150); }
    }
  })();

  // Teaser-Sprechblase über dem Icon (einmal pro Sitzung)
  function hideTeaser(seen){root.classList.remove('teaser-on');if(seen){try{sessionStorage.setItem('ebzc_teaser_seen','1');}catch(e){}}}
  (function(){
    var tb=document.getElementById('ebzc-teaser'), tc=document.getElementById('ebzc-teaser-close');
    if(tc)tc.onclick=function(e){e.stopPropagation();hideTeaser(true);};
    if(tb)tb.onclick=function(){hideTeaser(true);openPanel();};
    var seen=false; try{seen=!!sessionStorage.getItem('ebzc_teaser_seen');}catch(e){}
    if(!seen && !root.classList.contains('open')){
      setTimeout(function(){ if(!root.classList.contains('open')) root.classList.add('teaser-on'); },2500);
    }
  })();
})();
"""
