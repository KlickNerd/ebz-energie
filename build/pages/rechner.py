"""Rechner-Seiten: /solarrechner/ (PV-Rechner) und /energiegemeinschaft-rechner/.

Reine Browser-Rechner (Vanilla JS, keine Datenuebertragung). Alle Annahmen sind Richtwerte aus
freigegebenen Fakten bzw. den Ratgebern und stehen sichtbar auf der Seite (Methodik-Tabelle), die
Beispieltabellen werden zur Build-Zeit mit derselben Rechenlogik erzeugt (Python-Spiegel der JS-Formeln).
Ergebnis fuehrt immer in die kostenlose Beratung (Kontakt mit Vorbelegung).

OeMAG-Marktpreis: September 2026 = 10,168 ct (Stand Oktober 2026, build/seo/_fakten_2026-10.md); Juli 2026
6,146 ct nur als Verlaufswert. SEO/GEO-Briefings: build/seo/solarrechner.{json,md} (Primaer "pv rechner
oesterreich") und build/seo/eg_rechner.{json,md} (Primaer "energiegemeinschaft rechner").
Alter Slug /ebz-solarrechner/ -> 301 auf /solarrechner/ (build/redirects.txt).
"""

from common import IMG, NAP, FINANZIERUNG as F, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, href, write_page
from layout import page
import components as C

OEMAG = 10.168          # ct/kWh, OeMAG-Marktpreis Photovoltaik September 2026
OEMAG_STR = "10,168"
OEMAG_JULI_STR = "6,146"
ERTRAG_KWP = 1000       # kWh je kWp und Jahr, Rechenwert Kaernten/Steiermark
M2_KWP = 5.5            # m2 Dachflaeche je kWp
NETZ_NE7 = 8.7          # ct/kWh Netznutzung 8 + Netzverlust 0,7, Netzebene 7 (Richtwerte Ratgeber Netzkosten)
E_ABGABE = 1.5          # ct/kWh Elektrizitaetsabgabe, entfaellt in der EEG
FOERDERBEITRAG = 1.0    # ct/kWh Erneuerbaren-Foerderbeitrag (Richtwert), entfaellt in der EEG
EG_EINSP = 10.0         # ct/kWh Beispiel EG-Einspeisepreis*
EG_BEZUG = 14.0         # ct/kWh Beispiel EG-Bezugspreis*
LIEFERANT = 17.0        # ct/kWh Beispiel Energiepreis Lieferant*
BEITRAG = 48            # EUR/Jahr Beispiel Mitgliedsbeitrag (4 EUR je Monat)*
RABATT = {"lokal": 0.57, "regional": 0.28, "ne45": 0.64, "at": 0.0}


def _eur(v):
    return f"{round(v):,} €".replace(",", ".")


def _ct(v):
    return f"{v:g}".replace(".", ",")


def _kwh(v):
    return f"{round(v):,} kWh".replace(",", ".")


def _table(headers, rows, note=""):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join(
        "<tr>" + "".join(f'<td class="{"hl" if i == 0 else ""}">{c}</td>' for i, c in enumerate(r)) + "</tr>"
        for r in rows
    )
    note_html = f'<p class="form-note center eg-reveal" style="margin-top:18px">{note}</p>' if note else ""
    return (f'<div class="art-tablewrap eg-reveal" style="margin-top:32px">'
            f'<table class="art-table"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>{note_html}')


def _table_section(eyebrow, h2, intro, headers, rows, note="", anchor="", white=True):
    anchor_attr = f' id="{anchor}"' if anchor else ""
    style = ' style="background:#fff;border-block:1px solid var(--line)"' if white else ""
    return f"""
  <section class="section"{anchor_attr}{style}>
    <div class="wrap">
      <p class="eyebrow center eg-reveal">{eyebrow}</p>
      <h2 class="center eg-reveal">{h2}</h2>
      <p class="lead center eg-reveal" style="max-width:72ch;margin-inline:auto">{intro}</p>
      {_table(headers, rows, note)}
    </div>
  </section>"""


def _calc_section(title, intro, form_html, result_html, assumptions, script):
    li = "".join(f"<li>{x}</li>" for x in assumptions)
    return f"""
  <section class="section" id="rechner">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Rechner · kostenlos, ohne Anmeldung</p>
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


# --- Solarrechner / PV-Rechner ------------------------------------------------

AUSRICHTUNG = {"sued": 1.0, "ostwest": 0.9, "einseitig": 0.85}


def solar_calc(verbrauch, gewerbe=False, speicher=True, preis_ct=28.0, ausrichtung="sued"):
    """Python-Spiegel der JS-Logik (fuer die Beispieltabelle)."""
    verbrauch = max(1000, min(60000, verbrauch))
    preis = max(10, min(60, preis_ct)) / 100
    kwp = max(5, min(30, round(verbrauch / 1000 * 2) / 2))
    ertrag = kwp * ERTRAG_KWP * AUSRICHTUNG[ausrichtung]
    quote = (0.8 if gewerbe else 0.7) if speicher else (0.5 if gewerbe else 0.3)
    eigen = min(ertrag * quote, verbrauch * (0.8 if speicher else 0.45))
    einsp = ertrag - eigen
    ersparnis = eigen * preis + einsp * OEMAG / 100
    kwh_sp = kwp if speicher else 0
    inv_min = kwp * (1500 if speicher else 1000)
    inv_max = kwp * (2200 if speicher else 1500)
    inv_mid = (inv_min + inv_max) / 2
    foerd = (min(kwp, 10) * 150 + max(0, kwp - 10) * 140) + min(kwh_sp, kwp * 0.5) * 150
    amort = (inv_mid - foerd) / max(ersparnis, 1)
    amort_ktn = (inv_mid - foerd - 3000) / max(ersparnis, 1)
    rate = (inv_mid - foerd) / 25000 * 164
    return dict(kwp=kwp, ertrag=ertrag, eigen=eigen, einsp=einsp, quote=eigen / ertrag, autark=eigen / verbrauch,
                ersparnis=ersparnis, inv_min=inv_min, inv_max=inv_max, foerd=foerd, amort=amort,
                amort_ktn=amort_ktn, rate=rate, flaeche=kwp * M2_KWP)


SOLAR_FORM = """
  <div class="field"><label for="s-verbrauch">Jahresstromverbrauch (kWh)</label>
    <input id="s-verbrauch" type="number" min="1000" max="60000" step="100" value="4500" inputmode="numeric">
    <p class="calc__hint">Steht auf Ihrer Jahresabrechnung. 4-Personen-Haushalt: rund 4.500 kWh, mit Wärmepumpe oder E-Auto deutlich mehr.</p></div>
  <div class="field field--row">
    <div><label for="s-typ">Gebäude</label>
      <select id="s-typ"><option value="efh">Eigenheim</option><option value="gewerbe">Betrieb (Verbrauch tagsüber)</option></select></div>
    <div><label for="s-ausrichtung">Dachausrichtung</label>
      <select id="s-ausrichtung"><option value="sued">Süd (auch Südost, Südwest)</option><option value="ostwest">Ost-West</option><option value="einseitig">Nur Ost oder nur West</option></select></div>
  </div>
  <div class="field"><label for="s-speicher">Batteriespeicher</label>
    <select id="s-speicher"><option value="1">Ja, mit Speicher</option><option value="0">Nein, ohne Speicher</option></select></div>
  <div class="field"><label for="s-preis">Ihr Strompreis (ct/kWh)</label>
    <input id="s-preis" type="number" min="10" max="60" step="0.5" value="28" inputmode="decimal">
    <p class="calc__hint">Österreich-Durchschnitt rund 28 ct je kWh inklusive Netz und Abgaben (E-Control).</p></div>
  <p class="form-note">Der PV-Rechner läuft nur in Ihrem Browser, es werden keine Daten übertragen. Kostenlos, ohne Anmeldung.</p>
"""

SOLAR_RESULT = f"""
  <h3>Ihr Richtwert</h3>
  <p class="calc__big"><span id="s-ersparnis">0 €</span><small>Stromkosten-Ersparnis pro Jahr*</small></p>
  <div class="calc__grid">
    <div><b id="s-kwp">0 kWp</b><span>empfohlene Anlagengröße</span></div>
    <div><b id="s-flaeche">0 m²</b><span>benötigte Dachfläche*</span></div>
    <div><b id="s-ertrag">0 kWh</b><span>Jahresertrag*</span></div>
    <div><b id="s-quote">0 %</b><span>Eigenverbrauchsquote*</span></div>
    <div><b id="s-autark">0 %</b><span>Autarkiegrad (weniger Netzstrom)</span></div>
    <div><b id="s-invest">0 €</b><span>Richtpreis vor Förderung*</span></div>
    <div><b id="s-foerder">0 €</b><span>Bundesförderung (EAG 2026)*</span></div>
    <div><b id="s-amort">0 Jahre</b><span>Amortisation nach Förderung*</span></div>
    <div><b id="s-rate">0 €</b><span>Finanzierung pro Monat*</span></div>
    <div><b id="s-einsp">0 €</b><span>Einspeisung zu {OEMAG_STR} ct (OeMAG, Sept. 2026)*</span></div>
  </div>
  <a class="btn btn--primary btn--lg" id="s-cta" href="/kontakt/">Dieses Ergebnis kostenlos prüfen lassen</a>
  <a class="btn btn--light" href="/finanzierung/">Finanzierung ansehen</a>
  <p class="calc__note">*Richtwerte, kein Angebot. Ihr Projektbericht mit 3D-Belegplan und Statikreport zeigt die echten Zahlen für Ihr Dach.</p>
"""

SOLAR_ASSUMPTIONS = [
    "Jahresertrag rund 1.000 kWh je kWp in Kärnten und der Steiermark bei Südausrichtung (Richtwert 950 bis 1.100), Ost-West minus 10 %, nur Ost oder nur West minus 15 %.",
    "Anlagengröße: etwa 1 kWp je 1.000 kWh Jahresverbrauch, mindestens 5 kWp, höchstens 30 kWp. Dachfläche rund 5,5 m² je kWp.",
    "Eigenverbrauchsquote: ohne Speicher rund 30 % (Betrieb 50 %), mit Speicher bis zu 70 % (Betrieb 80 %). Mehr geht nur mit Energiemanagement.",
    f"Einspeisung des Überschusses zum OeMAG-Marktpreis von {OEMAG_STR} ct je kWh (September 2026; Juli 2026: {OEMAG_JULI_STR} ct, der Wert schwankt monatlich).",
    "Richtpreis: 10 kWp mit Speicher rund 15.000 bis 22.000 € vor Förderung, ohne Speicher rund 10.000 bis 15.000 €; linear skaliert.",
    "Bundesförderung 2026 (EAG): 150 € je kWp bis 10 kWp, darüber 140 € je kWp, plus 150 € je kWh Speicher (bis 0,5 kWh je kWp). Landesförderungen kommen zusätzlich dazu.",
    "Finanzierung: fixe Rate über 25 Jahre, Richtwert aus den Beispielen des Finanzierungspartners (ab 102 € für 15.000 €, ab 164 € für 25.000 €), linear skaliert. Rate abhängig von Angebot und Laufzeit.",
    "Strompreissteigerungen, Wartung und Modulalterung sind nicht eingerechnet.",
]

SOLAR_JS = r"""
(function(){
  var OEMAG=__OEMAG__, M2=__M2__, AUS={sued:1,ostwest:0.9,einseitig:0.85};
  var $=function(id){return document.getElementById(id);};
  var eur=function(v){return Math.round(v).toLocaleString("de-DE")+" €";};
  var kwh=function(v){return Math.round(v).toLocaleString("de-DE")+" kWh";};
  function calc(){
    var verbrauch=Math.max(1000,Math.min(60000,+$("s-verbrauch").value||4500));
    var gewerbe=$("s-typ").value==="gewerbe", speicher=$("s-speicher").value==="1";
    var aus=AUS[$("s-ausrichtung").value]||1;
    var preis=Math.max(10,Math.min(60,+$("s-preis").value||28))/100;
    var kwp=Math.max(5,Math.min(30,Math.round(verbrauch/1000*2)/2));
    var ertrag=kwp*1000*aus;
    var quote=speicher?(gewerbe?0.8:0.7):(gewerbe?0.5:0.3);
    var eigen=Math.min(ertrag*quote, verbrauch*(speicher?0.8:0.45));
    var einsp=ertrag-eigen;
    var ersparnis=eigen*preis+einsp*OEMAG/100;
    var kwhSp=speicher?kwp:0;
    var invMin=kwp*(speicher?1500:1000), invMax=kwp*(speicher?2200:1500), invMid=(invMin+invMax)/2;
    var foerd=(Math.min(kwp,10)*150+Math.max(0,kwp-10)*140)+Math.min(kwhSp,kwp*0.5)*150;
    var amort=(invMid-foerd)/Math.max(ersparnis,1);
    var rate=(invMid-foerd)/25000*164;
    $("s-ersparnis").textContent=eur(ersparnis);
    $("s-kwp").textContent=kwp.toLocaleString("de-DE")+" kWp";
    $("s-flaeche").textContent="rund "+Math.round(kwp*M2)+" m²";
    $("s-ertrag").textContent=kwh(ertrag);
    $("s-quote").textContent=Math.round(eigen/ertrag*100)+" %";
    $("s-autark").textContent=Math.round(eigen/verbrauch*100)+" %";
    $("s-invest").textContent=eur(invMin)+" bis "+eur(invMax);
    $("s-foerder").textContent=eur(foerd);
    $("s-amort").textContent=(Math.round(amort*10)/10).toLocaleString("de-DE")+" Jahre";
    $("s-rate").textContent="ab "+eur(rate);
    $("s-einsp").textContent=eur(einsp*OEMAG/100)+" ("+kwh(einsp)+")";
    var cta=$("s-cta"); var base=cta.getAttribute("href").split("?")[0];
    cta.setAttribute("href", base+"?anliegen="+encodeURIComponent("PV-Rechner: "+verbrauch+" kWh, "+kwp+" kWp"+(speicher?" mit Speicher":" ohne Speicher")+", Richtwert "+Math.round(ersparnis)+" €/Jahr"));
  }
  ["s-verbrauch","s-typ","s-ausrichtung","s-speicher","s-preis"].forEach(function(id){ var el=$(id); if(el){ el.addEventListener("input",calc); el.addEventListener("change",calc);} });
  if($("s-verbrauch")) calc();
})();
""".replace("__OEMAG__", str(OEMAG)).replace("__M2__", str(M2_KWP))

SOLAR_FAQ = [
    ("Wie genau ist der PV-Rechner?",
     "Er rechnet mit Richtwerten: 1.000 kWh Ertrag je kWp, Eigenverbrauch 30 bis 70 Prozent, Richtpreise aus über 300 Projekten. "
     "Standortgenaue Werkzeuge wie PVGIS, der SonnenKlar PV-Rechner (PV Austria) oder der klimaaktiv PV-Rechner liefern die Globalstrahlung, "
     "die echten Zahlen für Ihr Dach liefert der Projektbericht mit 3D-Belegplan und Statikreport nach der kostenlosen Beratung."),
    ("Wie viel kWp brauche ich für mein Haus?",
     "Als Faustregel 1 kWp je 1.000 kWh Jahresstromverbrauch: Ein 4-Personen-Haushalt mit 4.500 kWh kommt mit 5 kWp aus, mit Wärmepumpe "
     "und E-Auto sind 8 bis 10 kWp sinnvoll. Nach oben begrenzt meist das Dach, nach unten lohnt sich wegen der Fixkosten selten weniger als 5 kWp."),
    ("Wie viel Dachfläche braucht 1 kWp?",
     "Mit aktuellen Modulen (rund 440 Wp je 2 m²) etwa 5 bis 6 m² je kWp. Eine 10-kWp-Anlage braucht also rund 50 bis 60 m² Dachfläche, "
     "bei Ost-West-Belegung auf beiden Dachhälften. Der Rechner setzt 5,5 m² je kWp an."),
    ("Wie viel Ertrag bringt 1 kWp in Kärnten oder der Steiermark pro Jahr?",
     "Rund 1.000 kWh je kWp bei Südausrichtung und 30 bis 35 Grad Dachneigung, in sonnenreichen Lagen Kärntens bis 1.100 kWh. Ost-West-Dächer "
     "liefern rund 10 Prozent weniger, dafür gleichmäßiger über den Tag. Quelle für Standortwerte: PVGIS der EU-Kommission."),
    ("Wie groß sollte der Speicher zur Anlage sein?",
     "Richtwert 1 kWh Speicher je kWp Anlagenleistung, bei 10 kWp also rund 10 kWh. Der EAG-Zuschuss fördert mindestens 0,5 kWh je kWp mit "
     "150 € je kWh. Größere Speicher lohnen sich mit Wärmepumpe, E-Auto oder Notstromwunsch."),
    ("Wie wird die Amortisation berechnet?",
     "Richtpreis minus Förderung, geteilt durch die jährliche Ersparnis (selbst verbrauchter Strom zum eigenen Strompreis plus Einspeisung zum "
     f"OeMAG-Marktpreis von {OEMAG_STR} ct). Bei 10 kWp mit Speicher ergibt das rund 7 Jahre, mit der Kärntner Landespauschale von 3.000 € "
     "rund 6 Jahre. Strompreissteigerungen verkürzen die Dauer, sind aber nicht eingerechnet."),
    ("Berücksichtigt der Rechner Wärmepumpe und E-Auto / Wallbox?",
     "Indirekt über den Jahresstromverbrauch: Geben Sie den Gesamtverbrauch inklusive Wärmepumpe und E-Auto / Wallbox ein, der Rechner skaliert die "
     "Anlage mit. Das Lastprofil / Standardlastprofil eines Haushalts mit Wärmepumpe unterscheidet sich aber, deshalb rechnen wir das im "
     "Projektbericht mit Ihren echten Verbrauchsdaten nach."),
    ("Sind Landesförderungen eingerechnet?",
     "Nein, nur die Bundesförderung nach EAG. Die Landespauschale Kärnten 3.000 € (Neuanlage ab 5 kWp mit 5 kWh Speicher, Call 12. Oktober bis "
     "31. Dezember 2026) und die Landesförderung Steiermark kommen zusätzlich dazu und verkürzen die Amortisation weiter."),
]


def _solar_examples():
    rows = []
    for kwp_target, label in [(5, "4-Personen-Haushalt"), (8, "Haushalt mit E-Auto"), (10, "Haushalt mit Wärmepumpe"), (15, "großes Haus oder kleiner Betrieb")]:
        r = solar_calc(kwp_target * 1000)
        rows.append((f"{kwp_target} kWp mit {kwp_target} kWh Speicher",
                     f"{_kwh(kwp_target * 1000)} ({label})",
                     f"{_kwh(r['ertrag'])} / rund {round(r['flaeche'])} m²",
                     f"{round(r['quote'] * 100)} % / {round(r['autark'] * 100)} %",
                     _eur(r["ersparnis"]),
                     f"{_eur(r['inv_min'])} bis {_eur(r['inv_max'])}",
                     _eur(r["foerd"]),
                     f"{r['amort']:.1f} Jahre, mit Kärnten-Pauschale {r['amort_ktn']:.1f} Jahre".replace(".", ",")))
    return rows


def _solar_page():
    examples = _solar_examples()
    body = "".join([
        C.page_hero(
            eyebrow="PV-Rechner Österreich · kostenlos, ohne Anmeldung",
            h1="PV-Rechner für Österreich: Was bringt Photovoltaik auf Ihrem Dach in Kärnten und der Steiermark?",
            lead=("Jahresstromverbrauch, Dachausrichtung und Strompreis eingeben, sofort Richtwerte für Anlagengröße in kWp, "
                  "Ertrag, Eigenverbrauch, Ersparnis, Richtpreis, Förderung 2026 und Amortisation ablesen. Der "
                  "Photovoltaik-Rechner rechnet mit Werten aus über 300 Projekten, nicht mit Verkaufsversprechen."),
            cta=("#rechner", "Jetzt rechnen"), cta2=("kontakt", "Lieber beraten lassen"),
        ),
        _calc_section("Ihr Richtwert in 30 Sekunden",
                      "Fünf Angaben reichen. Das Ergebnis aktualisiert sich sofort und ist ein ehrlicher Richtwert, kein Verkaufsversprechen.",
                      SOLAR_FORM, SOLAR_RESULT, SOLAR_ASSUMPTIONS, SOLAR_JS),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Was ist ein PV-Rechner?",
            paragraphs=[
                ("Ein PV-Rechner (Photovoltaik-Rechner, Solarrechner) ist ein Online-Werkzeug, das aus Jahresstromverbrauch, "
                 "Dachausrichtung und Standort Richtwerte für Anlagengröße in kWp, Jahresertrag, Eigenverbrauchsquote, Kosten, "
                 "Förderung und Amortisation berechnet. Der EBZ-PV-Rechner rechnet mit 1.000 kWh je kWp für Kärnten und die "
                 f"Steiermark, dem EAG-Zuschuss 2026 von 150 € je kWp und dem OeMAG-Marktpreis von {OEMAG_STR} ct je kWh "
                 "(September 2026, Stand Oktober 2026)."),
                ("Ob Sie PV Anlage Rechner, Photovoltaik Rechner kostenlos oder Solarrechner suchen: Gemeint ist dasselbe Werkzeug. "
                 "Anders als die Wirtschaftlichkeitsberechnung im Projektbericht kennt der PV Rechner weder Ihre Dachneigung noch "
                 "Verschattung oder Ihr Lastprofil. Er ist der ehrliche Einstieg: Wer danach wissen will, was sein Dach wirklich "
                 "kann, bekommt von uns den Projektbericht mit 3D-Belegplan und Statikreport, kostenlos."),
            ],
        ),
        _table_section(
            eyebrow="Methodik",
            h2="So rechnet der PV-Rechner: Ertrag in kWh/kWp, Eigenverbrauch, Strompreis, Förderung",
            intro=("Jede Zahl im Ergebnis folgt einer offenen Annahme. Hier stehen alle Rechenwerte mit Quelle, Stand Oktober 2026, "
                   "damit Sie das Ergebnis nachrechnen und mit anderen Photovoltaik Rechnern vergleichen können."),
            headers=["Größe", "Rechenwert", "Herkunft"],
            rows=[
                ("kWh/kWp spezifischer Ertrag (950 bis 1.200 kWh/kWp)", "1.000 kWh je kWp (Süd); Ost-West minus 10 %, nur Ost oder West minus 15 %",
                 "Globalstrahlung / Sonnenstunden Kärnten und Steiermark, PVGIS; Praxiswerte EBZ"),
                ("Dachausrichtung (Süd, Ost-West, Azimut)", "drei Stufen wählbar; Dachneigung 30 bis 35 Grad als Normalfall angenommen",
                 "Richtwert; die Neigung prüfen wir im 3D-Belegplan"),
                ("Anlagengröße und Dachfläche (5 bis 6 m² je kWp)", "1 kWp je 1.000 kWh Verbrauch, 5 bis 30 kWp; 5,5 m² je kWp",
                 "Faustregel EBZ, Modulgröße rund 2 m² bei 440 Wp"),
                ("Eigenverbrauchsquote und Autarkiegrad", "ohne Speicher 30 % (Betrieb 50 %), mit Speicher 70 % (Betrieb 80 %); Autarkie = Eigenverbrauch / Jahresverbrauch",
                 "Richtwerte aus EBZ-Projekten; Lastprofil / Standardlastprofil nicht einzeln modelliert"),
                ("Strompreis ct/kWh", "Vorgabe 28 ct inklusive Netz und Abgaben, frei änderbar",
                 "Österreich-Durchschnitt Haushalt, E-Control 2026"),
                ("Einspeisung / OeMAG-Marktpreis", f"{OEMAG_STR} ct je kWh für den Überschuss",
                 f"OeMAG-Marktpreis September 2026 (Juli 2026: {OEMAG_JULI_STR} ct), oem-ag.at"),
                ("Richtpreis vor Förderung", "mit Speicher 1.500 bis 2.200 € je kWp, ohne Speicher 1.000 bis 1.500 € je kWp",
                 "EBZ-Richtpreis 10 kWp mit Speicher 15.000 bis 22.000 €, linear skaliert"),
                ("EAG-Investitionszuschuss 150 €/kWp", "bis 10 kWp 150 €, bis 20 kWp 140 € je kWp; Speicher 150 € je kWh (mind. 0,5 kWh je kWp); Made-in-Europe-Bonus nicht eingerechnet",
                 "EAG-Abwicklungsstelle, Fördersätze 2026"),
                ("Amortisation und Rendite", "(Richtpreis minus Förderung) / Ersparnis pro Jahr; ohne Strompreissteigerung, Wartung, Degradation",
                 "konservative Wirtschaftlichkeitsberechnung, Landesförderungen separat"),
                ("Finanzierung", f"Rate linear aus {F['beispiel_gross']['rate']} für {F['beispiel_gross']['betrag']} über 25 Jahre",
                 f"Finanzierungspartner {F['partner']}, Beispiele Stand September 2026"),
            ],
            note="Alle Werte sind Richtwerte. Speichergröße kWh wird mit 1 kWh je kWp angesetzt, die Förderung greift auf 0,5 kWh je kWp.",
            anchor="methodik",
        ),
        _table_section(
            eyebrow="Beispielrechnungen",
            h2="Beispielrechnungen: 5, 8, 10 und 15 kWp mit Speicher",
            intro=("Vier typische Anlagen, gerechnet mit genau der Logik des Rechners: Eigenheim, Südausrichtung, 28 ct Strompreis, "
                   "Speicher 1 kWh je kWp, Verbrauch passend zur Anlagengröße. PV Rechner mit Speicher und ohne unterscheiden sich "
                   "vor allem in der Eigenverbrauchsquote: 30 statt 70 Prozent."),
            headers=["Anlage", "Jahresverbrauch", "Ertrag / Dachfläche*", "Eigenverbrauch / Autarkie*", "Ersparnis pro Jahr*",
                     "Richtpreis vor Förderung*", "EAG 2026", "Amortisation*"],
            rows=examples,
            note=(f"*Richtwerte, Stand Oktober 2026. Einspeisung zu {OEMAG_STR} ct (OeMAG September 2026). Kärnten-Pauschale: 3.000 € "
                  "Landesförderung für Neuanlagen ab 5 kWp mit 5 kWh Speicher, Call 12. Oktober bis 31. Dezember 2026. Ohne Speicher sinkt der "
                  "Richtpreis auf 1.000 bis 1.500 € je kWp, die Eigenverbrauchsquote auf rund 30 %."),
            anchor="beispiele",
            white=False,
        ),
        C.media_text(
            eyebrow="Förderung 2026",
            h2="Welche Förderung ist eingerechnet: EAG 2026, Landespauschale Kärnten, Steiermark",
            paragraphs=[
                ("Eingerechnet ist nur der Bundeszuschuss nach EAG: 150 € je kWp bis 10 kWp (Kategorie A), 140 € bis 20 kWp, 130 € bis 100 kWp, "
                 "dazu 150 € je kWh Speicher. Der dritte Fördercall 2026 läuft bis 22. Oktober 2026, danach stellt der Bund laut BMWET ab 2027 "
                 "auf eine Systemförderung für Speicher mit intelligenter Steuerung um, bei der der Antrag erst nach der Installation erfolgt."),
                ("Nicht eingerechnet, aber zusätzlich möglich: die Landespauschale Kärnten 3.000 € für Neuanlagen ab 5 kWp mit mindestens 5 kWh "
                 "Speicher (Antrag 12. Oktober bis 31. Dezember 2026, maximal 50 Prozent der Kosten) und die Landesförderung Steiermark. "
                 "Beides verkürzt die Amortisation um ein bis zwei Jahre. Wir stellen die Anträge mit Ihnen."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Photovoltaik-Förderung 2026 in Kärnten und der Steiermark",
            bullets=[
                a("foerderung_at", "EAG-Fördercall 2026: Termine und Sätze"),
                a("foerderung_kaernten", "Förderung Kärnten 2026: 3.000 € Pauschale"),
                a("foerderung_steiermark", "Förderung Steiermark: aktuelle Programme"),
            ],
            cta=("foerderung_at", "Förderungen 2026 im Überblick"),
        ),
        C.media_text(
            eyebrow="Vom Richtwert zum Projekt",
            h2="Vom Richtwert zum Projektbericht mit 3D-Belegplan und Statikreport",
            paragraphs=[
                ("Der Rechner sagt, ob sich Photovoltaik für Sie rechnet. Ob Ihr Dach das trägt, wie viele Module wirklich Platz haben und "
                 "was Verschattung durch Kamin oder Nachbarhaus kostet, zeigt erst der Projektbericht: 3D-Belegplan Ihres Dachs, "
                 "Statikreport, Stückliste und Angebot mit Förderung. Kostenlos, nach einem Termin vor Ort in Kärnten oder der Steiermark."),
                ("Referenz: Einfamilienhaus Villach, 10 kWp Ost-West mit Notstrom, rund 11.000 kWh im Jahr und etwa 80 Prozent weniger Stromkosten. "
                 "Über 300 dokumentierte Projekte in 6 Bundesländern, 4,9 Sterne auf Google, bis zu 30 Jahre Leistungsgarantie."),
            ],
            img=IMG["ref_villach"],
            alt="Photovoltaikanlage auf einem Einfamilienhaus in Villach, 10 kWp Ost-West mit Notstrom",
            bullets=[
                "3D-Belegplan und Statikreport statt Schätzung",
                "Förderanträge Bund und Land inklusive",
                a("referenzen", "Referenzen") + " mit echten Erträgen",
            ],
            reverse=True,
            cta=("kontakt", "Projektbericht anfragen"),
        ),
        C.faq_section(SOLAR_FAQ),
        C.linkgrid_section("Weiterlesen", [
            ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage 2026"),
            ("/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/", "10 kWp mit Speicher: Preis"),
            ("foerderung_kaernten", "Förderung Kärnten 2026"),
            ("foerderung_steiermark", "Förderung Steiermark"),
            ("/ab-wann-lohnt-sich-photovoltaik-mit-speicher/", "Ab wann lohnt sich PV mit Speicher"),
            ("batteriespeicher", "Batteriespeicher"),
            ("photovoltaik", "Photovoltaikanlage"),
            ("eg_rechner", "Energiegemeinschaft-Rechner"),
        ]),
        C.contact_section("Ergebnis prüfen lassen, kostenlos und ehrlich",
                          "Schicken Sie uns Ihr Ergebnis, wir rechnen es mit echten Dachdaten und aktuellen Förderungen nach.",
                          page_label="PV-Rechner"),
        C.finalcta("Vom Richtwert zum echten Projekt",
                   "Beratung vor Ort in Kärnten und der Steiermark, Projektbericht mit 3D-Belegplan und Statikreport, Förderabwicklung inklusive."),
        f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte, kein Angebot. Rechenwerte laut Methodik-Tabelle, Stand Oktober 2026. OeMAG-Marktpreis
      September 2026: {OEMAG_STR} ct je kWh (oem-ag.at). Fördersätze laut EAG-Abwicklungsstelle und Land Kärnten 2026. Fachlich
      geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>""",
    ])
    path = "/solarrechner/"
    title = "PV-Rechner Österreich: Ertrag, Kosten, Ersparnis | EBZ"
    desc = ("Kostenloser PV-Rechner für Österreich ohne Anmeldung: kWp, Ertrag, Ersparnis, Richtpreis, Förderung 2026 und "
            "Amortisation. Richtwerte aus 300+ Projekten.")
    html = page(title, desc, path, body, faq_jsonld_str=faq_jsonld(u(path), SOLAR_FAQ), og_image=IMG["gen_eigenheim"])
    return write_page("solarrechner/index.html", html)


# --- EG-Rechner ---------------------------------------------------------------

def eg_calc(ueb, bez, quote, bereich, einsp_ct=EG_EINSP, bezug_ct=EG_BEZUG):
    """Python-Spiegel der JS-Logik (fuer die Beispieltabellen)."""
    netz = NETZ_NE7 * RABATT[bereich]
    abgabe = 0 if bereich == "at" else (E_ABGABE + FOERDERBEITRAG)
    zug_u, zug_b = ueb * quote, bez * quote
    mehr = zug_u * (einsp_ct - OEMAG) / 100
    energie = zug_b * (LIEFERANT - bezug_ct) / 100
    netz_e = zug_b * netz / 100
    abg_e = zug_b * abgabe / 100
    return dict(zug_u=zug_u, zug_b=zug_b, mehr=mehr, energie=energie, netz=netz_e, abgabe=abg_e,
                bezv=energie + netz_e + abg_e, gesamt=mehr + energie + netz_e + abg_e - BEITRAG)


EG_FORM = f"""
  <div class="field"><label for="e-rolle">Ihre Rolle in der Energiegemeinschaft</label>
    <select id="e-rolle"><option value="beide">Ich habe PV und beziehe auch Strom</option><option value="erzeuger">Ich speise nur Überschuss ein</option><option value="abnehmer">Ich beziehe nur Strom (keine PV)</option></select></div>
  <div class="field field--row">
    <div><label for="e-ueberschuss">Überschuss pro Jahr (kWh)</label><input id="e-ueberschuss" type="number" min="0" max="200000" step="100" value="4000" inputmode="numeric"></div>
    <div><label for="e-bezug">Netzbezug pro Jahr (kWh)</label><input id="e-bezug" type="number" min="0" max="200000" step="100" value="2500" inputmode="numeric"></div>
  </div>
  <div class="field"><label for="e-bereich">Nahbereich und Netzebene</label>
    <select id="e-bereich"><option value="lokal">Lokal: selber Trafo, Netzebene 7, Netzentgelt minus 57 %</option><option value="regional">Regional: selbes Umspannwerk, minus 28 %</option><option value="ne45">Netzebene 4/5 (Mittelspannung, Betrieb): minus 64 %</option><option value="at">Österreichweit (Bürgerenergiegemeinschaft), kein Rabatt</option></select></div>
  <div class="field"><label for="e-quote">Zuordnungsquote (%)</label>
    <input id="e-quote" type="number" min="10" max="100" step="5" value="50" inputmode="numeric">
    <p class="calc__hint">Anteil Ihres Stroms, der zeitgleich in der Gemeinschaft erzeugt oder verbraucht wird. Typisch 25 bis 60 %.</p></div>
  <div class="field field--row">
    <div><label for="e-einsp">EG-Einspeisepreis (ct/kWh)*</label><input id="e-einsp" type="number" min="0" max="30" step="0.5" value="{EG_EINSP:g}" inputmode="decimal"></div>
    <div><label for="e-bezugpreis">EG-Bezugspreis (ct/kWh)*</label><input id="e-bezugpreis" type="number" min="0" max="40" step="0.5" value="{EG_BEZUG:g}" inputmode="decimal"></div>
  </div>
  <p class="form-note">*Beispielkonditionen: {EG_EINSP:g} ct Einspeisung, {EG_BEZUG:g} ct Bezug, 4 € Beitrag pro Monat. Jede Gemeinschaft legt ihre Preise selbst fest. Der Rechner läuft nur in Ihrem Browser.</p>
"""

EG_RESULT = f"""
  <h3>Ihr Richtwert</h3>
  <p class="calc__big"><span id="e-gesamt">0 €</span><small>Vorteil pro Jahr nach Beitrag*</small></p>
  <div class="calc__grid">
    <div><b id="e-mehr">0 €</b><span>Einspeisung: EG-Preis gegenüber OeMAG {OEMAG_STR} ct (Sept. 2026)*</span></div>
    <div><b id="e-bezugv">0 €</b><span>Ersparnis Bezug (Energiepreis + Netzentgelt + Abgaben)*</span></div>
    <div><b id="e-zug">0 kWh</b><span>zugeordnete kWh pro Jahr</span></div>
    <div><b id="e-beitrag">{BEITRAG} €</b><span>Jahresbeitrag Plattform*</span></div>
  </div>
  <p class="calc__note" id="e-hinweis"></p>
  <a class="btn btn--primary btn--lg" id="e-cta" href="/kontakt/">Energiegemeinschaft in meiner Nähe anfragen</a>
  <a class="btn btn--light" href="/leistungen/energiegemeinschaft/">So funktioniert der Beitritt</a>
  <p class="calc__note">*Richtwerte mit Beispielkonditionen. Die echten Preise legt die jeweilige Gemeinschaft fest, den Nahbereich prüft der Netzbetreiber.</p>
"""

EG_ASSUMPTIONS = [
    f"Einspeisung in der Gemeinschaft {EG_EINSP:g} ct je kWh (Beispiel, änderbar) gegenüber OeMAG-Marktpreis {OEMAG_STR} ct (September 2026; Juli 2026: {OEMAG_JULI_STR} ct). Liegt der EG-Preis unter dem Marktpreis, wird die Differenz negativ ausgewiesen.",
    f"Bezug in der Gemeinschaft {EG_BEZUG:g} ct je kWh (Beispiel, änderbar) statt rund {LIEFERANT:g} ct Energiepreis beim Lieferanten.",
    f"Netznutzungs- und Netzverlustentgelt zusammen rund {_ct(NETZ_NE7)} ct je kWh (Netzebene 7): minus 57 % lokal, minus 28 % regional, minus 64 % bei ausschließlicher Teilnahme auf Netzebene 4/5, kein Abschlag österreichweit (SNE-VO, E-Control).",
    f"Elektrizitätsabgabe {_ct(E_ABGABE)} ct und Erneuerbaren-Förderbeitrag rund {_ct(FOERDERBEITRAG)} ct je kWh entfallen für Strom aus Erneuerbare-Energie-Gemeinschaften (nicht in der Bürgerenergiegemeinschaft).",
    "Zuordnungsquote: Nur zeitgleich erzeugter und verbrauchter Strom wird zugeordnet; typisch 25 bis 60 %, mit Speicher oder Energiemanagement mehr.",
    "Mitgliedsbeitrag 4 € pro Monat (Beispiel der Abrechnungsplattform), einmalige Kosten nicht eingerechnet. Umsatzsteuer 20 % nicht berücksichtigt, Haushalte sparen brutto entsprechend mehr.",
]

EG_JS = r"""
(function(){
  var OEMAG=__OEMAG__, NETZ=__NETZ__, ABG=__ABG__, LIEF=__LIEF__, BEITRAG=__BEITRAG__;
  var RAB={lokal:0.57,regional:0.28,ne45:0.64,at:0};
  var $=function(id){return document.getElementById(id);};
  var eur=function(v){return Math.round(v).toLocaleString("de-DE")+" €";};
  var sgn=function(v){return (v<0?"minus ":"")+eur(Math.abs(v));};
  function calc(){
    var rolle=$("e-rolle").value, bereich=$("e-bereich").value;
    var quote=Math.max(10,Math.min(100,+$("e-quote").value||50))/100;
    var einsp=Math.max(0,Math.min(30,+$("e-einsp").value||0));
    var bezp=Math.max(0,Math.min(40,+$("e-bezugpreis").value||0));
    var ueb=rolle==="abnehmer"?0:Math.max(0,+$("e-ueberschuss").value||0);
    var bez=rolle==="erzeuger"?0:Math.max(0,+$("e-bezug").value||0);
    $("e-ueberschuss").disabled=rolle==="abnehmer"; $("e-bezug").disabled=rolle==="erzeuger";
    var netz=NETZ*(RAB[bereich]||0);
    var abgabe=bereich==="at"?0:ABG;
    var zugU=ueb*quote, zugB=bez*quote;
    var mehr=zugU*(einsp-OEMAG)/100;
    var bezv=zugB*((LIEF-bezp)+netz+abgabe)/100;
    var gesamt=mehr+bezv-BEITRAG;
    $("e-mehr").textContent=sgn(mehr); $("e-bezugv").textContent=eur(bezv);
    $("e-zug").textContent=Math.round(zugU+zugB).toLocaleString("de-DE")+" kWh";
    $("e-beitrag").textContent=eur(BEITRAG);
    $("e-gesamt").textContent=sgn(gesamt);
    var hint="";
    if(zugU>0 && einsp<OEMAG){ hint="Hinweis: Ihr EG-Einspeisepreis liegt unter dem OeMAG-Marktpreis von "+OEMAG.toLocaleString("de-DE")+" ct (September 2026). Der Vorteil kommt dann aus Bezug und Netzentgelt; im Juli 2026 lag der Marktpreis bei 6,146 ct, er schwankt monatlich."; }
    if(bereich==="at"){ hint+=(hint?" ":"")+"Österreichweit teilen ist möglich, der Netzentgelt-Rabatt und die Abgabenbefreiung gelten aber nur im Nahbereich."; }
    $("e-hinweis").textContent=hint;
    var cta=$("e-cta"); var base=cta.getAttribute("href").split("?")[0];
    cta.setAttribute("href", base+"?anliegen="+encodeURIComponent("EG-Rechner: "+ueb+" kWh Überschuss, "+bez+" kWh Bezug, "+bereich+", Richtwert "+Math.round(gesamt)+" €/Jahr"));
  }
  ["e-rolle","e-ueberschuss","e-bezug","e-bereich","e-quote","e-einsp","e-bezugpreis"].forEach(function(id){ var el=$(id); if(el){ el.addEventListener("input",calc); el.addEventListener("change",calc);} });
  if($("e-rolle")) calc();
})();
""".replace("__OEMAG__", str(OEMAG)).replace("__NETZ__", str(NETZ_NE7)).replace("__ABG__", str(E_ABGABE + FOERDERBEITRAG)).replace("__LIEF__", str(LIEFERANT)).replace("__BEITRAG__", str(BEITRAG))

EG_FAQ = [
    ("Wie viel bringt eine Energiegemeinschaft pro Jahr?",
     "Als Abnehmer sparen Sie auf jede zugeordnete Kilowattstunde rund 10 ct* (günstigerer Energiepreis, 57 Prozent weniger Netzentgelt "
     "lokal, keine Elektrizitätsabgabe und kein Förderbeitrag). Ein 4-Personen-Haushalt mit 4.725 kWh und 50 Prozent Zuordnung kommt so auf "
     "rund 200 € im Jahr nach Beitrag*, ein 1-Personen-Haushalt auf rund 55 €*. Laut Erfahrungsberichten liegen Haushalte bei 100 bis 300 € im Jahr."),
    ("Wie hoch ist der Strompreis in einer Energiegemeinschaft?",
     f"Den Energiepreis legt jede Gemeinschaft selbst fest, der EG-Preis 8 bis 12 ct ist für Erzeuger üblich, Abnehmer zahlen typisch 12 bis "
     f"14 ct* statt rund {LIEFERANT:g} ct beim Lieferanten. Dazu kommen Netzentgelt (im Nahbereich reduziert), Abgaben (in der EEG befreit) "
     "und Umsatzsteuer 20 %. Vergleichswerte für Ihren Lieferanten finden Sie im E-Control Preisportal."),
    ("Energiegemeinschaft oder OeMAG: was bringt mehr für meinen Überschuss?",
     f"Im September 2026 zahlt die OeMAG {OEMAG_STR} ct je kWh, im Juli waren es {OEMAG_JULI_STR} ct. Ein EG-Preis von 10 ct* liegt also je nach "
     "Monat über oder unter dem Marktpreis. Der Unterschied: Der EG-Preis ist fix vereinbart, der Marktpreis schwankt. Dazu kommt, dass Sie als "
     "Erzeuger meist auch Abnehmer sind und dort sicher sparen. Der OeMAG-Vertrag bleibt für den nicht zugeordneten Rest bestehen."),
    ("Lohnt sich eine Energiegemeinschaft ohne eigene PV-Anlage?",
     "Ja, als reiner Abnehmer. Sie sparen Netzentgelt, Abgaben und die Differenz zwischen Lieferanten- und EG-Preis auf den zugeordneten Strom, "
     "ohne Investition und mit ein bis drei Monaten Kündigungsfrist. Entscheidend ist der Tagesverbrauch: Wer mittags Strom braucht "
     "(Homeoffice, Wärmepumpe, E-Auto), bekommt mehr zugeordnet."),
    ("Was kostet die Teilnahme pro Monat (Mitgliedsbeitrag)?",
     "Typisch 2 bis 8 € je Zählpunkt und Monat für Plattform und Abrechnung, manchmal stattdessen 0,5 bis 2 ct je abgerechneter Kilowattstunde. "
     "Einrichtungs- und Austrittsgebühren sind unüblich. Der Rechner setzt 4 € je Monat an, also 48 € im Jahr.*"),
    ("Was ist die Zuordnungsquote und warum ist sie so wichtig?",
     "Nur Strom, der in derselben Viertelstunde in der Gemeinschaft erzeugt und verbraucht wird, kann zugeordnet werden: Gleichzeitigkeit von "
     "Erzeugung und Verbrauch zählt. Bei einem Haushalt mit PV und Abendverbrauch sind das oft nur 25 Prozent, mit Wärmepumpe, E-Auto, Homeoffice "
     "oder Energiemanagement 40 bis 60 Prozent. Der Rest läuft wie bisher über Lieferant und OeMAG."),
    ("Kann ich meinen Solarstrom an den Nachbarn verkaufen?",
     "Ja, über eine Erneuerbare-Energie-Gemeinschaft im Nahbereich oder seit 1. Oktober 2026 per Peer-to-Peer-Vertrag direkt an eine Person, "
     "auch ohne Verein. Den Netzentgelt-Rabatt gibt es in beiden Fällen nur im Nahbereich, österreichweites Teilen läuft als "
     "Bürgerenergiegemeinschaft ohne Netzrabatt."),
    ("Welche Nachteile hat eine Energiegemeinschaft?",
     "Der Vorteil hängt an der Zuordnungsquote, der Rabatt gilt nur im Nahbereich, die Zählpunktanmeldung dauert bis zum Monatsersten, und der "
     "EG-Preis kann in einzelnen Monaten unter dem OeMAG-Marktpreis liegen. Dazu kommen 2 bis 8 € Beitrag im Monat. Alle sieben Punkte bewertet der "
     "Ratgeber " + a("/energiegemeinschaft-nachteile/", "Energiegemeinschaft: Nachteile") + "."),
]


def _eg_examples():
    rows = []
    for label, kwh, quote, bereich in [("1-Personen-Haushalt", 1927, 0.5, "lokal"), ("4-Personen-Haushalt", 4725, 0.5, "lokal"),
                                       ("Betrieb 24.740 kWh (70 % EG-Anteil)", 24740, 0.7, "lokal")]:
        r = eg_calc(0, kwh, quote, bereich)
        rows.append((label, _kwh(kwh), f"{round(quote * 100)} % / {_kwh(r['zug_b'])}", _eur(r["energie"]), _eur(r["netz"]),
                     _eur(r["abgabe"]), f"minus {BEITRAG} €", f"<b>{_eur(r['gesamt'])}</b>"))
    return rows


def _eg_detail_rows():
    netz_l = NETZ_NE7 * (1 - RABATT["lokal"])
    return [
        ("Arbeitspreis ct/kWh (Energie)", f"{LIEFERANT:g} ct*", f"{EG_BEZUG:g} ct* (EG-Preis)", f"{LIEFERANT - EG_BEZUG:g} ct"),
        ("Netznutzungsentgelt (bis 57 % lokal, 28 % regional, 64 % Netzebene 4/5)", "8 ct", "3,44 ct (lokal, minus 57 %)", "4,56 ct"),
        ("Netzverlustentgelt", "0,7 ct", "0,30 ct (minus 57 %)", "0,40 ct"),
        ("Elektrizitätsabgabe", f"{_ct(E_ABGABE)} ct", "0 ct (EEG befreit)", f"{_ct(E_ABGABE)} ct"),
        ("Erneuerbaren-Förderbeitrag", f"rund {FOERDERBEITRAG:g} ct", "0 ct (EEG befreit)", f"rund {FOERDERBEITRAG:g} ct"),
        ("Summe je zugeordneter kWh (netto)", f"rund {LIEFERANT + NETZ_NE7 + E_ABGABE + FOERDERBEITRAG:.1f} ct".replace(".", ","),
         f"rund {EG_BEZUG + netz_l:.1f} ct".replace(".", ","), f"<b>rund {LIEFERANT - EG_BEZUG + NETZ_NE7 - netz_l + E_ABGABE + FOERDERBEITRAG:.1f} ct</b>".replace(".", ",")),
        ("Umsatzsteuer 20 %", "auf alles", "auf alles", "Ersparnis brutto plus 20 %"),
        ("Mitgliedsbeitrag (€/Jahr)", "0 €", f"{BEITRAG} €*", f"minus {BEITRAG} €"),
    ]


def _eg_page():
    body = "".join([
        C.page_hero(
            eyebrow="Energiegemeinschaft Rechner · kostenlos, ohne Anmeldung",
            h1="Energiegemeinschaft-Rechner: Was bringt Strom teilen pro Jahr?",
            lead=("Überschuss, Netzbezug, Nahbereich und EG-Preise eingeben, Vorteil pro Jahr ablesen. Der Rechner trennt sauber "
                  f"zwischen Einspeisung (EG-Preis gegenüber OeMAG-Marktpreis {OEMAG_STR} ct) und Ersparnis beim Bezug, und er sagt "
                  "ehrlich, wenn sich etwas nicht rechnet."),
            cta=("#rechner", "Jetzt rechnen"), cta2=("kontakt", "Lieber beraten lassen"),
        ),
        _calc_section("Ihr Vorteil pro Jahr",
                      "Der Rechner zieht den Mitgliedsbeitrag ab, rechnet den Netzentgelt-Rabatt je Netzebene und weist eine negative Einspeise-Differenz offen aus.",
                      EG_FORM, EG_RESULT, EG_ASSUMPTIONS, EG_JS),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Was ist ein Energiegemeinschaft-Rechner?",
            paragraphs=[
                ("Ein Energiegemeinschaft-Rechner berechnet aus Überschuss, Netzbezug, Zuordnungsquote und Nahbereich den jährlichen Vorteil "
                 "des Stromteilens: Mehrerlös oder Mindererlös für den PV-Überschuss gegenüber dem OeMAG-Marktpreis, Ersparnis beim Bezug durch "
                 "EG-Preis, bis zu 57 Prozent weniger Netzentgelt (lokal) und entfallende Abgaben, abzüglich Mitgliedsbeitrag. Der EBZ-Rechner "
                 f"nutzt die Netzentgelte laut SNE-VO der E-Control und den OeMAG-Marktpreis {OEMAG_STR} ct (September 2026, Stand Oktober 2026)."),
                ("Die häufigste Frage lautet schlicht: Energiegemeinschaft lohnt sich? Die ehrliche Antwort hängt an drei Zahlen: der "
                 "Zuordnungsquote (Gleichzeitigkeit von Erzeugung und Verbrauch), dem Nahbereich (Netzebene und Rabatt) und dem Abstand "
                 "zwischen EG-Preis und Marktpreis. Beispielwerte sind mit Sternchen markiert, die echten Konditionen legt jede Gemeinschaft fest."),
            ],
        ),
        _table_section(
            eyebrow="Energiegemeinschaft Netzkosten Ersparnis je Netzebene",
            h2="So rechnet der Energiegemeinschaft-Rechner: Zuordnungsquote, EG-Preis, Netzentgelt",
            intro=("Jede Position im Ergebnis folgt einer offenen Annahme. Quellen: E-Control (SNE-VO, Preisportal), oem-ag.at, Ratgeber "
                   "Netzkosten und Kosten von EBZ. Stand Oktober 2026."),
            headers=["Größe", "Rechenwert", "Herkunft"],
            rows=[
                ("Zuordnungsquote", "Vorgabe 50 %, 10 bis 100 % wählbar; zugeordnet = Überschuss bzw. Netzbezug mal Quote",
                 "Viertelstundenwerte des Smart Meters; statische und dynamische Zuteilung je Gemeinschaft, Standardlastprofil nicht modelliert"),
                ("EG-Preis 8 bis 12 ct (Einspeisung)", f"{EG_EINSP:g} ct* vorgegeben, änderbar; Differenz zu OeMAG {OEMAG_STR} ct",
                 f"OeMAG-Marktpreis September 2026 (Juli: OeMAG-Marktpreis {OEMAG_JULI_STR} ct), oem-ag.at"),
                ("Bezugspreis / Reststrom vom Lieferanten", f"{EG_BEZUG:g} ct* EG-Bezug gegenüber {LIEFERANT:g} ct* Energiepreis Lieferant",
                 "marktübliche Spannen, E-Control Preisportal"),
                ("Netznutzungsentgelt und Netzverlustentgelt", f"{_ct(NETZ_NE7)} ct je kWh (Netzebene 7: 8 + 0,7); minus 57 % lokal, 28 % regional, 64 % Netzebene 4/5, 0 % österreichweit",
                 "SNE-VO (E-Control), Ratgeber Netzkosten"),
                ("Elektrizitätsabgabe und Erneuerbaren-Förderbeitrag", f"{_ct(E_ABGABE)} ct + rund {_ct(FOERDERBEITRAG)} ct entfallen in der EEG, nicht in der BEG",
                 "Elektrizitätsabgabegesetz, EAG"),
                ("Mitgliedsbeitrag (€/Jahr)", f"{BEITRAG} €* (4 € je Monat)", "Beispiel der Abrechnungsplattform, marktüblich 2 bis 8 € je Monat"),
                ("Nicht eingerechnet", "Umsatzsteuer 20 %, Einrichtungskosten, Eigendeckung durch eigenen Speicher, Peer-to-Peer-Verträge",
                 "konservative Rechnung; Vergleich: Benefit-Tool energiegemeinschaften.gv.at"),
            ],
            anchor="methodik",
        ),
        _table_section(
            eyebrow="Energiegemeinschaft Ersparnis in drei Beispielen",
            h2="Drei Beispiele: 1-Personen-Haushalt, 4-Personen-Haushalt, Betrieb",
            intro=("Jahresverbrauch 1.927 kWh (1 Person) und 4.725 kWh (4 Personen) laut E-Control, Betrieb mit 24.740 kWh und 70 Prozent "
                   "EG-Anteil. Alle drei als reine Abnehmer in einer lokalen EEG (Netzebene 7), gerechnet mit der Logik des Rechners.*"),
            headers=["Beispiel", "Netzbezug", "Zuordnung / zugeordnete kWh", "Energiepreis-Vorteil*", "Netzentgelt minus 57 %", "Abgaben entfallen",
                     "Beitrag*", "Vorteil pro Jahr*"],
            rows=_eg_examples(),
            note=(f"*Beispielkonditionen: EG-Bezug {EG_BEZUG:g} ct statt {LIEFERANT:g} ct, Netzentgelt {_ct(NETZ_NE7)} ct minus 57 %, Elektrizitätsabgabe "
                  f"{_ct(E_ABGABE)} ct und Förderbeitrag rund {_ct(FOERDERBEITRAG)} ct entfallen, Beitrag {BEITRAG} € im Jahr, netto ohne Umsatzsteuer. "
                  "Mit eigener PV-Anlage (etwa 10 kWp, 4.000 kWh Überschuss) kommt die Einspeise-Differenz dazu, die bei 10 ct* gegenüber dem Marktpreis September 2026 leicht negativ ist."),
            anchor="beispiele",
            white=False,
        ),
        _table_section(
            eyebrow="Energiegemeinschaft Strompreis im Detail",
            h2="Bisher vs. mit Energiegemeinschaft: die Rechnung je Kilowattstunde",
            intro=("Was ein Haushalt je bezogener Kilowattstunde zahlt, bisher beim Lieferanten und mit zugeordnetem EG-Strom in einer lokalen "
                   "Erneuerbare-Energie-Gemeinschaft. Netzebene 7, Richtwerte 2026, netto."),
            headers=["Position", "Bisher (Lieferant)", "Mit Energiegemeinschaft (lokal)", "Ersparnis"],
            rows=_eg_detail_rows(),
            note=("Richtwerte laut Ratgeber " + a("/energiegemeinschaft-netzkosten/", "Netzkosten in der Energiegemeinschaft") + " und "
                  + a("/energiegemeinschaft-kosten/", "Kosten und Abrechnung") + ". Regional: Netzentgelte minus 28 %, Netzebene 4/5: minus 64 %."),
            anchor="detail",
        ),
        C.split_section(
            left={
                "title": "Energiegemeinschaft Vorteile ohne eigene PV-Anlage: lohnt sich das?",
                "dark": True,
                "items": [
                    "Ja, als Abnehmer: rund 10 ct* Ersparnis je zugeordneter kWh aus Energiepreis, Netzentgelt und Abgaben",
                    "Keine Investition, kein Lieferantenwechsel, Kündigungsfrist ein bis drei Monate",
                    "Je mehr Tagesverbrauch (Homeoffice, Wärmepumpe, E-Auto), desto höher die Zuordnung",
                    "Rabatt nur im Nahbereich: Nahbereichsabfrage beim Netzbetreiber zuerst",
                    a("eg_privat", "So treten Sie einer Gemeinschaft bei"),
                ],
            },
            right={
                "title": "Energiegemeinschaft Einspeisetarif oder OeMAG-Einspeisung?",
                "items": [
                    f"OeMAG-Marktpreis schwankt monatlich: {OEMAG_JULI_STR} ct im Juli, {OEMAG_STR} ct im September 2026",
                    "EG-Preis fix vereinbart, typisch 8 bis 12 ct*: in manchen Monaten darüber, in manchen darunter",
                    "Der OeMAG-Vertrag bleibt für den nicht zugeordneten Überschuss bestehen",
                    "Mit eigenem Speicher steigt die Eigendeckung, der Überschuss sinkt: erst Speicher, dann Gemeinschaft rechnen",
                    a("/oemag-einspeisetarif/", "OeMAG-Einspeisetarif aktuell"),
                ],
                "note": "*Beispielkonditionen, jede Gemeinschaft legt ihre Preise selbst fest. Der Vorteil für Erzeuger entsteht aus Planbarkeit und aus dem eigenen Bezug, nicht aus einem garantierten Mehrerlös.",
            },
        ),
        C.faq_section(EG_FAQ),
        C.linkgrid_section("Weiterlesen", [
            ("eg_privat", "Energiegemeinschaft beitreten"),
            ("eg_gewerbe", "Energiegemeinschaft für Betriebe und Gemeinden"),
            ("/energiegemeinschaft-kosten/", "Kosten und Abrechnung"),
            ("/energiegemeinschaft-netzkosten/", "Netzentgelt-Rabatt nach Netzebene"),
            ("/energiegemeinschaft-nachteile/", "7 Nachteile ehrlich bewertet"),
            ("/oemag-einspeisetarif/", "OeMAG-Einspeisetarif aktuell"),
            ("/energiegemeinschaft-privat/", "Energiegemeinschaft privat"),
            ("solarrechner", "PV-Rechner"),
        ]),
        C.contact_section("Ergebnis prüfen lassen, kostenlos und ehrlich",
                          "Nennen Sie uns Zählpunkt, Postleitzahl und Verbrauch: Wir fragen den Nahbereich beim Netzbetreiber ab und nennen die echten Konditionen der Gemeinschaft in Ihrer Nähe.",
                          page_label="Energiegemeinschaft-Rechner"),
        C.finalcta("Vom Richtwert zur passenden Gemeinschaft",
                   "Nahbereichsabfrage in einem Werktag, Abrechnung über energyfamily, Beratung aus Villach für Kärnten und die Steiermark."),
        f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Beispielkonditionen und Richtwerte, kein Angebot. OeMAG-Marktpreis September 2026: {OEMAG_STR} ct je kWh
      (Stand Oktober 2026, oem-ag.at); Juli 2026: {OEMAG_JULI_STR} ct. Netzentgelt-Abschlag und Abgabenbefreiung nur für die zugeordnete
      Menge und nur im Nahbereich (lokal 57 %, regional 28 %, Netzebene 4/5 bis 64 %), Richtwerte laut SNE-VO (E-Control) 2026.
      Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>""",
    ])
    path = "/energiegemeinschaft-rechner/"
    title = "Energiegemeinschaft-Rechner: Ersparnis pro Jahr | EBZ"
    desc = ("Energiegemeinschaft-Rechner: Ersparnis pro Jahr aus günstigerem Bezug, bis zu 57 % weniger Netzentgelt im Nahbereich "
            "und EG-Preis statt OeMAG-Marktpreis.")
    html = page(title, desc, path, body, faq_jsonld_str=faq_jsonld(u(path), EG_FAQ), og_image=IMG["eg_drohne"])
    return write_page("energiegemeinschaft-rechner/index.html", html)


def build():
    errors = []
    errors += _solar_page()
    errors += _eg_page()
    return errors
