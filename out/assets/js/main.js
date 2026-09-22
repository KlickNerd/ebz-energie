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

  /* Sticky Mobile-CTA erst nach dem Hero zeigen */
  var sticky = document.querySelector(".sticky-cta");
  var hero = document.querySelector(".hero");
  if(sticky && hero && "IntersectionObserver" in window){
    var so = new IntersectionObserver(function(entries){
      sticky.style.transform = entries[0].isIntersecting ? "translateY(120%)" : "translateY(0)";
    }, {threshold:0});
    so.observe(hero);
  }
})();
