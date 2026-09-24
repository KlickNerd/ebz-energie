/* EBZ Energie  globales Verhalten. Vanilla JS, keine Abhaengigkeiten. */
(function(){
  "use strict";

  /* Mobile-Navigation */
  var toggle = document.querySelector(".nav-toggle");
  var body = document.body;
  if(toggle){
    toggle.addEventListener("click", function(){
      var open = body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.querySelectorAll(".nav a").forEach(function(link){
      link.addEventListener("click", function(){ body.classList.remove("nav-open"); });
    });
  }

  /* Reveal + Balken/Hub-Animation beim Scrollen */
  var revealEls = document.querySelectorAll(".eg-reveal");
  if("IntersectionObserver" in window && revealEls.length){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting){ e.target.classList.add("eg-inview"); io.unobserve(e.target); }
      });
    }, {threshold:.16, rootMargin:"0px 0px -8% 0px"});
    revealEls.forEach(function(el){ io.observe(el); });
  } else {
    revealEls.forEach(function(el){ el.classList.add("eg-inview"); });
  }

  /* KPI-Zahlen hochzaehlen (nur wenn data-count gesetzt) */
  var counters = document.querySelectorAll("[data-count]");
  if("IntersectionObserver" in window && counters.length){
    var co = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(!e.isIntersecting) return;
        var el = e.target, target = parseFloat(el.getAttribute("data-count")),
            suffix = el.getAttribute("data-suffix") || "", dur = 1200, t0 = null;
        function step(ts){
          if(!t0) t0 = ts;
          var p = Math.min((ts - t0)/dur, 1);
          var val = Math.round(target * (0.5 - Math.cos(Math.PI*p)/2));
          el.textContent = val.toLocaleString("de-AT") + suffix;
          if(p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step); co.unobserve(el);
      });
    }, {threshold:.5});
    counters.forEach(function(el){ co.observe(el); });
  }

  /* Reviews-Slider: Pfeile, Autoplay (Pause bei Hover), reduced-motion-sicher */
  document.querySelectorAll(".rev-slider").forEach(function(s){
    var track = s.querySelector(".rev-track");
    if(!track) return;
    var nav = s.querySelector(".rev-nav");
    function scrollable(){ return track.scrollWidth - track.clientWidth > 4; }
    function step(){
      var card = track.querySelector(".rev-card");
      return card ? card.offsetWidth + 22 : track.clientWidth;
    }
    // Nav nur zeigen, wenn es etwas zu scrollen gibt
    function syncNav(){ if(nav) nav.style.display = scrollable() ? "flex" : "none"; }
    syncNav();
    window.addEventListener("resize", syncNav);

    var prev = s.querySelector(".rev-prev"), next = s.querySelector(".rev-next");
    if(prev) prev.addEventListener("click", function(){ track.scrollBy({left:-step(),behavior:"smooth"}); });
    if(next) next.addEventListener("click", function(){ track.scrollBy({left:step(),behavior:"smooth"}); });

    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if(!reduce){
      var timer = null;
      function start(){ if(!timer && scrollable()) timer = setInterval(tick, 5000); }
      function stop(){ if(timer){ clearInterval(timer); timer = null; } }
      function tick(){
        if(document.hidden || !scrollable()) return;
        if(track.scrollLeft + track.clientWidth >= track.scrollWidth - 4){
          track.scrollTo({left:0, behavior:"smooth"});
        } else {
          track.scrollBy({left:step(), behavior:"smooth"});
        }
      }
      start();
      s.addEventListener("mouseenter", stop);
      s.addEventListener("mouseleave", start);
    }
  });

  /* Sticky Mobile-CTA erst nach dem Hero zeigen */
  // Ratgeber-Hub: Live-Filter ueber Titel, Beschreibung und Cluster
  var rgInput = document.querySelector(".rg-search input");
  var rgRoot = document.querySelector(".rg-root");
  if(rgInput && rgRoot){
    var cards = Array.prototype.slice.call(rgRoot.querySelectorAll(".rg-card"));
    var sections = Array.prototype.slice.call(rgRoot.querySelectorAll(".rg-section"));
    var norm = function(s){ return (s || "").toLowerCase().replace(/ä/g,"ae").replace(/ö/g,"oe").replace(/ü/g,"ue").replace(/ß/g,"ss"); };
    cards.forEach(function(c){ c.dataset.q = norm(c.textContent); });
    var apply = function(){
      var q = norm(rgInput.value.trim());
      if(!q){ rgRoot.classList.remove("rg-filtering","rg-nothing"); cards.forEach(function(c){ c.classList.remove("is-hidden"); }); sections.forEach(function(s){ s.classList.remove("is-empty"); }); return; }
      rgRoot.classList.add("rg-filtering");
      var words = q.split(/\s+/), any = false;
      cards.forEach(function(c){
        var hit = words.every(function(w){ return c.dataset.q.indexOf(w) !== -1; });
        c.classList.toggle("is-hidden", !hit); if(hit) any = true;
      });
      sections.forEach(function(s){ s.classList.toggle("is-empty", !s.querySelector(".rg-card:not(.is-hidden)")); });
      rgRoot.classList.toggle("rg-nothing", !any);
    };
    rgInput.addEventListener("input", apply);
  }

  var sticky = document.querySelector(".sticky-cta");
  var hero = document.querySelector(".hero");
  if(sticky && hero && "IntersectionObserver" in window){
    var so = new IntersectionObserver(function(entries){
      sticky.style.transform = entries[0].isIntersecting ? "translateY(120%)" : "translateY(0)";
    }, {threshold:0});
    so.observe(hero);
  }
})();
