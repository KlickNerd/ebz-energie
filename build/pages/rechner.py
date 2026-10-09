"""Rechner-Seiten: /solarrechner/ und /energiegemeinschaft-rechner/.

Reine Browser-Rechner (Vanilla JS, keine Datenuebertragung). Alle Annahmen sind
Richtwerte aus freigegebenen Fakten bzw. den Ratgebern und stehen sichtbar unter
dem Rechner. Ergebnis fuehrt immer in die kostenlose Beratung (Kontakt mit Vorbelegung).
"""

from common import IMG, NAP, FINANZIERUNG as F, faq_jsonld, u, a, href, write_page
from layout import page
import components as C

OEMAG = 6.146


def _calc_section(title, intro, form_html, result_html, assumptions, script):
    li = "".join(f"<li>{x}</li>" for x in assumptions)
    return f"""
  <section class="section" id="rechner">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Rechner</p>
      <h2 class="center eg-reveal">{title}</h2>
      <p class="lead center eg-reveal" style="max-width:66ch;margin-inline:auto">{intro}</p>
      <div class="calc" style="margin-top:36px">
        <form class="form-card eg-reveal js-calc" onsubmit="return false">{form_html}</form>
        <div>
          <div class="calc__res eg-reveal">{result_html}</div>
          <details class="calc__assume"><summary>Annahmen und Richtwerte*</summary><ul>{li}</ul></details>
        </div>
      </div>
    </div>
  </section>
  <script>{script}</script>"""


# --- Solarrechner ------------------------------------------------------------

SOLAR_FORM = """
  <div class="field"><label for="s-verbrauch">Stromverbrauch pro Jahr (kWh)</label>
    <input id="s-verbrauch" type="number" min="1000" max="60000" step="100" value="4500" inputmode="numeric">
    <p class="calc__hint">Steht auf Ihrer Jahresabrechnung. 4-Personen-Haushalt: rund 4.500 kWh, mit Wärmepumpe oder E-Auto deutlich mehr.</p></div>
  <div class="field"><label for="s-typ">Gebäude</label>
    <select id="s-typ"><option value="efh">Eigenheim</option><option value="gewerbe">Betrieb (Verbrauch tagsüber)</option></select></div>
  <div class="field"><label for="s-speicher">Batteriespeicher</label>
    <select id="s-speicher"><option value="1">Ja, mit Speicher</option><option value="0">Nein, ohne Speicher</option></select></div>
  <div class="field"><label for="s-preis">Ihr Strompreis (ct/kWh)</label>
    <input id="s-preis" type="number" min="10" max="60" step="0.5" value="28" inputmode="decimal">
    <p class="calc__hint">Österreich-Durchschnitt rund 28 ct je kWh inklusive Netz und Abgaben.</p></div>
  <p class="form-note">Der Rechner läuft nur in Ihrem Browser, es werden keine Daten übertragen.</p>
"""

SOLAR_RESULT = """
  <h3>Ihr Richtwert</h3>
  <p class="calc__big"><span id="s-ersparnis">0 €</span><small>Stromkosten-Ersparnis pro Jahr*</small></p>
  <div class="calc__grid">
    <div><b id="s-kwp">0 kWp</b><span>empfohlene Anlagengröße</span></div>
    <div><b id="s-ertrag">0 kWh</b><span>Jahresertrag*</span></div>
    <div><b id="s-quote">0 %</b><span>Eigenverbrauchsquote*</span></div>
    <div><b id="s-autark">0 %</b><span>weniger Netzstrom</span></div>
    <div><b id="s-invest">0 €</b><span>Richtpreis vor Förderung*</span></div>
    <div><b id="s-foerder">0 €</b><span>Bundesförderung (EAG)*</span></div>
    <div><b id="s-amort">0 Jahre</b><span>Amortisation nach Förderung*</span></div>
    <div><b id="s-rate">0 €</b><span>Finanzierung pro Monat*</span></div>
  </div>
  <a class="btn btn--primary btn--lg" id="s-cta" href="/kontakt/">Dieses Ergebnis kostenlos prüfen lassen</a>
  <a class="btn btn--light" href="/finanzierung/">Finanzierung ansehen</a>
  <p class="calc__note">*Richtwerte, kein Angebot. Ihr Projektbericht mit 3D-Belegplan und Statikreport zeigt die echten Zahlen für Ihr Dach.</p>
"""

SOLAR_ASSUMPTIONS = [
    "Jahresertrag rund 1.000 kWh je kWp in Kärnten und der Steiermark (Richtwert 950 bis 1.100).",
    "Anlagengröße: etwa 1 kWp je 1.000 kWh Jahresverbrauch, mindestens 5 kWp, höchstens 30 kWp.",
    "Eigenverbrauchsquote: ohne Speicher rund 30 % (Betrieb 50 %), mit Speicher bis zu 70 % (Betrieb 80 %). Mehr geht nur mit Energiemanagement.",
    "Einspeisung des Überschusses zum OeMAG-Marktpreis von 6,146 ct je kWh (Juli 2026).",
    "Richtpreis: 10 kWp mit Speicher rund 15.000 bis 22.000 € vor Förderung, ohne Speicher rund 10.000 bis 15.000 €; linear skaliert.",
    "Bundesförderung 2026 (EAG): 150 € je kWp bis 10 kWp, darüber 140 € je kWp, plus 150 € je kWh Speicher (bis 0,5 kWh je kWp). Landesförderungen kommen zusätzlich dazu.",
    "Finanzierung: fixe Rate über 25 Jahre, Richtwert aus den Beispielen des Finanzierungspartners (ab 102 € für 15.000 €, ab 164 € für 25.000 €), linear skaliert. Rate abhängig von Angebot und Laufzeit.",
    "Strompreissteigerungen, Wartung und Modulalterung sind nicht eingerechnet.",
]

SOLAR_JS = r"""
(function(){
  var $=function(id){return document.getElementById(id);};
  var eur=function(v){return Math.round(v).toLocaleString("de-DE")+" €";};
  var kwh=function(v){return Math.round(v).toLocaleString("de-DE")+" kWh";};
  function calc(){
    var verbrauch=Math.max(1000,Math.min(60000,+$("s-verbrauch").value||4500));
    var gewerbe=$("s-typ").value==="gewerbe", speicher=$("s-speicher").value==="1";
    var preis=Math.max(10,Math.min(60,+$("s-preis").value||28))/100;
    var kwp=Math.max(5,Math.min(30,Math.round(verbrauch/1000*2)/2));
    var ertrag=kwp*1000;
    var quote=speicher?(gewerbe?0.8:0.7):(gewerbe?0.5:0.3);
    var eigen=Math.min(ertrag*quote, verbrauch*(speicher?0.8:0.45));
    var einsp=ertrag-eigen;
    var ersparnis=eigen*preis+einsp*0.06146;
    var kwhSp=speicher?kwp:0;
    var invMin=kwp*(speicher?1500:1000), invMax=kwp*(speicher?2200:1500), invMid=(invMin+invMax)/2;
    var foerd=(Math.min(kwp,10)*150+Math.max(0,kwp-10)*140)+Math.min(kwhSp,kwp*0.5)*150;
    var amort=(invMid-foerd)/Math.max(ersparnis,1);
    var rate=(invMid-foerd)/25000*164;
    $("s-ersparnis").textContent=eur(ersparnis);
    $("s-kwp").textContent=kwp.toLocaleString("de-DE")+" kWp";
    $("s-ertrag").textContent=kwh(ertrag);
    $("s-quote").textContent=Math.round(eigen/ertrag*100)+" %";
    $("s-autark").textContent=Math.round(eigen/verbrauch*100)+" %";
    $("s-invest").textContent=eur(invMin)+" bis "+eur(invMax);
    $("s-foerder").textContent=eur(foerd);
    $("s-amort").textContent=(Math.round(amort*10)/10).toLocaleString("de-DE")+" Jahre";
    $("s-rate").textContent="ab "+eur(rate);
    var cta=$("s-cta"); var base=cta.getAttribute("href").split("?")[0];
    cta.setAttribute("href", base+"?anliegen="+encodeURIComponent("Solarrechner: "+verbrauch+" kWh, "+kwp+" kWp"+(speicher?" mit Speicher":" ohne Speicher")+", Richtwert "+Math.round(ersparnis)+" €/Jahr"));
  }
  ["s-verbrauch","s-typ","s-speicher","s-preis"].forEach(function(id){ var el=$(id); if(el){ el.addEventListener("input",calc); el.addEventListener("change",calc);} });
  if($("s-verbrauch")) calc();
})();
"""

SOLAR_FAQ = [
    ("Wie genau ist der Solarrechner?",
     "Er rechnet mit Richtwerten (1.000 kWh Ertrag je kWp, Eigenverbrauch 30 bis 70 Prozent, Richtpreise aus über 300 Projekten). "
     "Die echten Zahlen für Ihr Dach liefert der Projektbericht mit 3D-Belegplan und Statikreport nach der kostenlosen Beratung."),
    ("Warum empfiehlt der Rechner einen Speicher?",
     "Ohne Speicher nutzen Haushalte meist nur rund 30 Prozent des eigenen Sonnenstroms, der Rest geht für 6,146 ct je kWh ins Netz. "
     "Mit Speicher steigt der Eigenverbrauch auf bis zu 70 bis 80 Prozent, und jede selbst genutzte Kilowattstunde ersetzt Netzstrom für rund 28 ct."),
    ("Sind Landesförderungen eingerechnet?",
     "Nein, nur die Bundesförderung nach EAG. Landesförderungen wie die Kärntner Speicherpauschale kommen zusätzlich dazu und verkürzen die Amortisation weiter."),
]


# --- EG-Rechner ---------------------------------------------------------------

EG_FORM = """
  <div class="field"><label for="e-rolle">Ihre Rolle in der Energiegemeinschaft</label>
    <select id="e-rolle"><option value="beide">Ich habe PV und beziehe auch Strom</option><option value="erzeuger">Ich speise nur Überschuss ein</option><option value="abnehmer">Ich beziehe nur Strom (keine PV)</option></select></div>
  <div class="field field--row">
    <div><label for="e-ueberschuss">Überschuss pro Jahr (kWh)</label><input id="e-ueberschuss" type="number" min="0" max="200000" step="100" value="4000" inputmode="numeric"></div>
    <div><label for="e-bezug">Netzbezug pro Jahr (kWh)</label><input id="e-bezug" type="number" min="0" max="200000" step="100" value="2500" inputmode="numeric"></div>
  </div>
  <div class="field"><label for="e-bereich">Nahbereich zur Gemeinschaft</label>
    <select id="e-bereich"><option value="lokal">Lokal: selber Trafo, Netzentgelt minus 57 %</option><option value="regional">Regional: selbes Umspannwerk, minus 28 %</option><option value="at">Österreichweit (Bürgerenergiegemeinschaft), kein Rabatt</option></select></div>
  <div class="field"><label for="e-quote">Zuordnungsquote (%)</label>
    <input id="e-quote" type="number" min="10" max="100" step="5" value="50" inputmode="numeric">
    <p class="calc__hint">Anteil Ihres Stroms, der zeitgleich in der Gemeinschaft erzeugt oder verbraucht wird. Typisch 25 bis 60 %.</p></div>
  <p class="form-note">Beispielkonditionen: 10 ct Einspeisung, 14 ct Bezug, 4 € Beitrag pro Monat. Der Rechner läuft nur in Ihrem Browser.</p>
"""

EG_RESULT = """
  <h3>Ihr Richtwert</h3>
  <p class="calc__big"><span id="e-gesamt">0 €</span><small>Vorteil pro Jahr nach Beitrag*</small></p>
  <div class="calc__grid">
    <div><b id="e-mehr">0 €</b><span>Mehrerlös Einspeisung (10 ct statt 6,146 ct)*</span></div>
    <div><b id="e-bezugv">0 €</b><span>Ersparnis Bezug (Energie + Netz + Abgabe)*</span></div>
    <div><b id="e-zug">0 kWh</b><span>zugeordnete kWh pro Jahr</span></div>
    <div><b id="e-beitrag">48 €</b><span>Jahresbeitrag Plattform*</span></div>
  </div>
  <a class="btn btn--primary btn--lg" id="e-cta" href="/kontakt/">Energiegemeinschaft in meiner Nähe anfragen</a>
  <a class="btn btn--light" href="/leistungen/energiegemeinschaft/">So funktioniert der Beitritt</a>
  <p class="calc__note">*Richtwerte mit Beispielkonditionen. Die echten Preise legt die jeweilige Gemeinschaft fest, den Nahbereich prüft der Netzbetreiber.</p>
"""

EG_ASSUMPTIONS = [
    "Einspeisung in der Gemeinschaft 10 ct je kWh (Beispiel) statt OeMAG-Marktpreis 6,146 ct (Juli 2026): Mehrerlös 3,85 ct je zugeordneter kWh.",
    "Bezug in der Gemeinschaft 14 ct je kWh (Beispiel) statt rund 17 ct Energiepreis beim Lieferanten: 3 ct Ersparnis.",
    "Netznutzungs- und Netzverlustentgelt zusammen rund 9,25 ct je kWh (Netzebene 7): minus 57 % lokal, minus 28 % regional, kein Abschlag österreichweit.",
    "Elektrizitätsabgabe 1,5 ct je kWh entfällt für Strom aus Erneuerbare-Energie-Gemeinschaften (lokal und regional).",
    "Zuordnungsquote: Nur zeitgleich erzeugter und verbrauchter Strom wird zugeordnet; typisch 25 bis 60 %, mit Speicher oder Energiemanagement mehr.",
    "Mitgliedsbeitrag 4 € pro Monat (Beispiel der Abrechnungsplattform), einmalige Kosten nicht eingerechnet.",
]

EG_JS = r"""
(function(){
  var $=function(id){return document.getElementById(id);};
  var eur=function(v){return Math.round(v).toLocaleString("de-DE")+" €";};
  function calc(){
    var rolle=$("e-rolle").value, bereich=$("e-bereich").value;
    var quote=Math.max(10,Math.min(100,+$("e-quote").value||50))/100;
    var ueb=rolle==="abnehmer"?0:Math.max(0,+$("e-ueberschuss").value||0);
    var bez=rolle==="erzeuger"?0:Math.max(0,+$("e-bezug").value||0);
    $("e-ueberschuss").disabled=rolle==="abnehmer"; $("e-bezug").disabled=rolle==="erzeuger";
    var netz=9.25*(bereich==="lokal"?0.57:bereich==="regional"?0.28:0);
    var abgabe=bereich==="at"?0:1.5;
    var zugU=ueb*quote, zugB=bez*quote;
    var mehr=zugU*(10-6.146)/100;
    var bezv=zugB*(3+netz+abgabe)/100;
    var beitrag=48;
    var gesamt=mehr+bezv-beitrag;
    $("e-mehr").textContent=eur(mehr); $("e-bezugv").textContent=eur(bezv);
    $("e-zug").textContent=Math.round(zugU+zugB).toLocaleString("de-DE")+" kWh";
    $("e-beitrag").textContent=eur(beitrag);
    $("e-gesamt").textContent=(gesamt<0?"minus ":"")+eur(Math.abs(gesamt));
    var cta=$("e-cta"); var base=cta.getAttribute("href").split("?")[0];
    cta.setAttribute("href", base+"?anliegen="+encodeURIComponent("EG-Rechner: "+ueb+" kWh Überschuss, "+bez+" kWh Bezug, "+bereich+", Richtwert "+Math.round(gesamt)+" €/Jahr"));
  }
  ["e-rolle","e-ueberschuss","e-bezug","e-bereich","e-quote"].forEach(function(id){ var el=$(id); if(el){ el.addEventListener("input",calc); el.addEventListener("change",calc);} });
  if($("e-rolle")) calc();
})();
"""

EG_FAQ = [
    ("Was ist die Zuordnungsquote und warum ist sie so wichtig?",
     "Nur Strom, der in derselben Viertelstunde in der Gemeinschaft erzeugt und verbraucht wird, kann zugeordnet werden. Bei einem Haushalt mit PV und "
     "Abendverbrauch sind das oft nur 25 Prozent, mit Wärmepumpe, E-Auto, Homeoffice oder Energiemanagement 40 bis 60 Prozent. Der Rest läuft wie bisher über Lieferant und OeMAG."),
    ("Gilt der Netzentgelt-Rabatt überall?",
     "Nein. Minus 57 Prozent gibt es nur lokal am selben Trafo, minus 28 Prozent regional am selben Umspannwerk. Wer Strom österreichweit teilt, zum Beispiel mit "
     "Verwandten in Wien, nutzt eine Bürgerenergiegemeinschaft ohne Netzentgelt-Rabatt; der Vorteil kommt dann nur aus dem Strompreis."),
    ("Woher kommen die 10 und 14 Cent?",
     "Das sind Beispielkonditionen, wie sie in vielen Gemeinschaften üblich sind. Die tatsächlichen Preise legt jede Gemeinschaft selbst fest. "
     "EBZ Energie nennt Ihnen vor dem Beitritt die echten Konditionen der Gemeinschaft in Ihrer Nähe."),
]


def _page(path, title, desc, hero_h1, hero_lead, calc_html, faq, links, og):
    body = "".join([
        C.page_hero(eyebrow="Kostenlos und unverbindlich", h1=hero_h1, lead=hero_lead,
                    cta=("#rechner", "Jetzt rechnen"), cta2=("kontakt", "Lieber beraten lassen")),
        calc_html,
        C.faq_section(faq),
        C.linkgrid_section("Weiterlesen", links),
        C.contact_section("Ergebnis prüfen lassen, kostenlos und ehrlich",
                          "Schicken Sie uns Ihr Ergebnis, wir rechnen es mit echten Dachdaten und aktuellen Förderungen nach.",
                          page_label=title.split("|")[0].strip()),
        C.finalcta("Vom Richtwert zum echten Projekt",
                   "Beratung vor Ort in Kärnten und der Steiermark, Projektbericht mit 3D-Belegplan und Statikreport, Förderabwicklung inklusive."),
    ])
    html = page(title, desc, path, body, faq_jsonld_str=faq_jsonld(u(path), faq), og_image=og)
    return write_page(path.strip("/") + "/index.html", html)


def build():
    errors = []
    errors += _page(
        "/solarrechner/",
        "Solarrechner: Ertrag, Kosten, Ersparnis in 30 Sekunden | EBZ",
        "Kostenloser Solarrechner für Kärnten und die Steiermark: Anlagengröße, Ertrag, Ersparnis, Richtpreis, Förderung und Amortisation. Richtwerte aus 300+ Projekten.",
        "Solarrechner: Was bringt Photovoltaik auf Ihrem Dach?",
        "Geben Sie Ihren Stromverbrauch ein und sehen Sie sofort Richtwerte für Anlagengröße, Ersparnis, Kosten, Förderung und Finanzierungsrate.",
        _calc_section("Ihr Richtwert in 30 Sekunden",
                      "Vier Angaben reichen. Das Ergebnis aktualisiert sich sofort und ist ein ehrlicher Richtwert, kein Verkaufsversprechen.",
                      SOLAR_FORM, SOLAR_RESULT, SOLAR_ASSUMPTIONS, SOLAR_JS),
        SOLAR_FAQ,
        [("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"), ("batteriespeicher", "Batteriespeicher"),
         ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage"), ("foerderung_at", "Förderung 2026")],
        IMG["gen_eigenheim"],
    )
    errors += _page(
        "/energiegemeinschaft-rechner/",
        "Energiegemeinschaft-Rechner: Ihr Vorteil pro Jahr | EBZ Energie",
        "Rechnen Sie in 30 Sekunden aus, was eine Energiegemeinschaft bringt: Mehrerlös für PV-Überschuss, günstigerer Bezug, bis zu 57 % weniger Netzentgelt im Nahbereich.",
        "Energiegemeinschaft-Rechner: Was bringt Strom teilen?",
        "Überschuss, Bezug und Nahbereich eingeben, Vorteil pro Jahr ablesen. Mit Beispielkonditionen und allen Annahmen offen gelegt.",
        _calc_section("Ihr Vorteil pro Jahr",
                      "Der Rechner trennt sauber zwischen Mehrerlös für Ihren Überschuss und Ersparnis beim Bezug, und zieht den Beitrag ab.",
                      EG_FORM, EG_RESULT, EG_ASSUMPTIONS, EG_JS),
        EG_FAQ,
        [("eg_privat", "Energiegemeinschaft für Private"), ("eg_gewerbe", "Für Betriebe und Gemeinden"),
         ("/energiegemeinschaft-netzkosten/", "Netzkosten in der Energiegemeinschaft"), ("/energiegemeinschaft-beitreten/", "Beitritt in 4 Schritten")],
        IMG["eg_drohne"],
    )
    return errors
