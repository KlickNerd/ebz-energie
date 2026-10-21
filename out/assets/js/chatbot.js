(function(){
  var WORKER_URL = "https://ebzbot.klicknerds.workers.dev"; /* aus common.CHATBOT_URL */

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
