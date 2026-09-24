"""Ratgeber: Solarenergie und Photovoltaik: Grundlagen.

Zusammengeführt aus drei generischen Live-Artikeln:
  /solarenergie/ (Dez. 2025), /erneuerbare-energien/ (Juli 2025), /photovoltaik-oesterreich/ (Juli 2025).
Nur das Substanzielle übernommen (Funktionsweise, Komponenten, Österreich-Zahlen, Solarthermie
vs. Photovoltaik, Vorteile und Grenzen), Marketing-Fließtext gestrichen. Ziel 1.800 bis 2.200 Wörter.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "solarenergie",
    "path": "/solarenergie/",
    "title": "Solarenergie und Photovoltaik: Grundlagen | EBZ Energie",
    "description": ("Solarenergie erklärt: Wie Photovoltaik Strom erzeugt, Unterschied zur Solarthermie, 10 kWp "
                    "liefern rund 10.000 kWh, Österreichs Strommix, Vorteile, Grenzen."),
    "eyebrow": "Photovoltaik · Grundlagen",
    "crumb_label": "Solarenergie: Grundlagen",
    "h1": "Solarenergie und Photovoltaik: Grundlagen, Technik und Zahlen für Österreich",
    "lead": ("Solarenergie ist die Energie der Sonnenstrahlung, Photovoltaik macht daraus Strom, Solarthermie "
             "Wärme. Dieser Grundlagen-Ratgeber erklärt die Technik, die Komponenten einer Anlage, die "
             "wichtigsten Zahlen für Österreich und wo die Grenzen liegen."),
    "chips": [
        "10 kWp: <b>rund 10.000 kWh</b> pro Jahr",
        "Eigenverbrauch mit Speicher: <b>60 bis 80 %</b>",
        "Module: <b>25 bis 30 Jahre</b> Lebensdauer",
        "Wasserkraft in Österreich: <b>rund 60 %</b> des Stroms",
    ],
    "date_published": "2025-05-10",
    "date_modified": "2026-09-24",
    "hero_img": "pv_card",
    "hero_alt": "Photovoltaikmodule auf einem Dach in der Sonne: Grundlagen der Solarenergie",

    "tldr": [
        "Photovoltaik wandelt Licht über den photoelektrischen Effekt in Siliziumzellen direkt in Gleichstrom um, "
        "der Wechselrichter macht daraus Haushaltsstrom. Solarthermie erzeugt dagegen Warmwasser und Heizwärme.",
        "Eine 10-kWp-Anlage braucht 50 bis 60 Quadratmeter Dach und liefert in Österreich rund 10.000 kWh pro "
        "Jahr. Ideal sind Süddächer mit rund 30 Grad Neigung, Ost-West-Dächer verteilen den Ertrag über den Tag.",
        "Ohne Speicher nutzt ein Haushalt rund 30 Prozent des Solarstroms selbst, mit Speicher 60 bis 80 Prozent. "
        "Übers Jahr sind 70 bis 80 Prozent Autarkie erreichbar, im Winter bleibt Netzbezug nötig.",
        "Österreich erzeugt rund 60 Prozent seines Stroms aus Wasserkraft, Windkraft liefert 10 bis 12 Prozent, "
        "Photovoltaik 5 bis 7 Prozent mit stark wachsendem Anteil (Stand 2025).",
        "Module halten 25 bis 30 Jahre, der Wechselrichter 10 bis 15 Jahre. Die Anlage hat nach wenigen Jahren "
        "mehr Energie erzeugt, als ihre Herstellung gebraucht hat.",
    ],
    "kpis": [
        ("10.000 kWh", "Jahresertrag einer 10-kWp-Anlage"),
        ("60 bis 80 %", "Eigenverbrauch mit Speicher"),
        ("25 bis 30 Jahre", "Lebensdauer der Module"),
        ("5 bis 7 %", "PV-Anteil am Strom in Österreich (2025)"),
    ],

    "sections": [
        ("Was ist Solarenergie? Photovoltaik und Solarthermie", "definition", f"""
<p>Solarenergie ist die Strahlungsenergie der Sonne. Sie lässt sich auf zwei Arten nutzen: Photovoltaik
(PV) erzeugt daraus elektrischen Strom, Solarthermie erwärmt Wasser für Heizung und Brauchwasser. Im
Alltag werden die Begriffe oft vermischt, technisch sind es zwei verschiedene Anlagen mit unterschiedlichen
Aufgaben:</p>
{A.table(
    ["", "Photovoltaik", "Solarthermie"],
    [
        ["Erzeugt", "Strom (Gleichstrom, per Wechselrichter Wechselstrom)", "Wärme (Warmwasser, Heizungsunterstützung)"],
        ["Nutzung", "alle Geräte, Wärmepumpe, E-Auto, Einspeisung ins Netz", "nur Wärme, Speicherung im Pufferspeicher"],
        ["Speicher", "Batteriespeicher, Netz", "Warmwasser- oder Pufferspeicher"],
        ["Typische Größe Einfamilienhaus", "5 bis 15 kWp, 25 bis 80 m²", "4 bis 12 m² Kollektorfläche"],
        ["Kombination", "mit Wärmepumpe deckt PV auch den Wärmebedarf", "mit Öl-, Gas- oder Pelletsheizung"],
    ],
    hl_cols=(1,),
)}
<p>Für Eigenheime, die unabhängig werden wollen, steht heute die Photovoltaik im Vordergrund: Strom ist
universell einsetzbar, und in Kombination mit einer {a('waermepumpe', 'Wärmepumpe')} deckt eine PV-Anlage
auch den Wärmebedarf. Solarthermie bleibt sinnvoll, wenn eine bestehende Heizung ergänzt werden soll. Der
Rest dieses Ratgebers konzentriert sich auf die Photovoltaik.</p>
"""),
        ("Wie Photovoltaik funktioniert", "funktionsweise", f"""
<p>Die Umwandlung von Licht in Strom beruht auf dem photoelektrischen Effekt. Trifft Sonnenlicht auf eine
Solarzelle aus Silizium, einem Halbleiter, gibt es Energie an die Elektronen im Material ab und setzt sie in
Bewegung. Es entsteht eine Gleichspannung. Viele Zellen werden zu einem Modul verschaltet, viele Module zu
einer Anlage. Der Vorgang kommt ohne bewegliche Teile und ohne Verbrennung aus, deshalb sind PV-Anlagen
leise, wartungsarm und langlebig.</p>
<p>Der erzeugte Gleichstrom kann im Haus nicht direkt genutzt werden, weil das Stromnetz mit Wechselstrom
arbeitet. Der Wechselrichter wandelt ihn um, überwacht die Anlage, optimiert den Ertrag bei Teilverschattung
und sorgt für die Sicherheit des Systems. Von dort fließt der Strom zu den Verbrauchern im Haus, in den
Speicher oder ins öffentliche Netz.</p>
{A.net([
    ("☀", "Module", "Siliziumzellen erzeugen Gleichstrom, Leistung in kWp"),
    ("◎", "Wechselrichter", "wandelt in Wechselstrom, überwacht und steuert"),
    ("▮", "Speicher", "hält den Mittagsstrom für Abend und Nacht bereit"),
    ("⌂", "Verbraucher", "Haushalt, Wärmepumpe, E-Auto, Rest ins Netz"),
], "So fließt der Sonnenstrom",
   "Priorität hat der Direktverbrauch, dann wird der Speicher geladen, erst der Rest wird eingespeist.")}
<p>Moderne Module nutzen nicht nur direktes Sonnenlicht, sondern auch diffuse Strahlung bei Bewölkung. Der
Ertrag ist an sonnigen Tagen am höchsten, aber auch bei bedecktem Himmel produziert die Anlage
kontinuierlich Strom.</p>
"""),
        ("Die Komponenten einer Photovoltaikanlage", "komponenten", f"""
<h3>Solarmodule</h3>
<p>Heute sind monokristalline Siliziummodule Standard, weil sie den höchsten Wirkungsgrad bieten und auch bei
diffusem Licht gut arbeiten. Die Nennleistung wird in Kilowatt-Peak (kWp) angegeben, der Leistung unter
Standardtestbedingungen. Glas-Glas-Module sind robuster und langlebiger als Glas-Folie-Module, bifaziale
Module nehmen zusätzlich Licht über die Rückseite auf. Full-Black-Module fügen sich unauffällig ins Dachbild.</p>
<h3>Wechselrichter</h3>
<p>String-Wechselrichter schalten mehrere Module in Reihe und sind der Standard für Dächer ohne Verschattung.
Modulwechselrichter oder Leistungsoptimierer arbeiten je Modul und bringen bei komplexen Dachflächen oder
Teilverschattung Vorteile, kosten aber mehr. Bei Anlagen mit Speicher kommt ein Hybrid-Wechselrichter zum
Einsatz, der PV und Batterie gemeinsam steuert. Die Lebensdauer liegt bei 10 bis 15 Jahren, ein Tausch
sollte eingeplant werden.</p>
<h3>Batteriespeicher</h3>
<p>Die Sonne scheint vor allem tagsüber, wenn viele nicht zu Hause sind. Ein {a('batteriespeicher', 'Batteriespeicher')}
nimmt den Mittagsüberschuss auf und gibt ihn abends und nachts ab. Der Eigenverbrauch steigt damit von rund
30 auf 60 bis 80 Prozent. Üblich sind 5 bis 10 kWh bei einer 10-kWp-Anlage, moderne Systeme auf
Lithium-Eisenphosphat-Basis sind modular erweiterbar und halten 10 bis 15 Jahre.</p>
<h3>Energiemanagement</h3>
<p>Ein {a('ems', 'Energiemanagementsystem')} verbindet alle Komponenten. Es priorisiert den Direktverbrauch,
lädt dann den Speicher und speist erst den Rest ein. Es kann Wärmepumpe oder Wallbox gezielt dann
einschalten, wenn viel Solarstrom verfügbar ist, und verarbeitet dynamische Stromtarife.</p>
"""),
        ("Solarenergie in Österreich: die wichtigsten Zahlen", "oesterreich", f"""
<p>Österreich hat bei der Stromerzeugung eine gute Ausgangslage: Rund 60 Prozent des Stroms stammen aus
Wasserkraft, die grundlastfähig rund um die Uhr liefert. Pumpspeicherkraftwerke in den Alpen gleichen die
Schwankungen von Wind und Sonne aus. Windkraft, vor allem im Osten des Landes, trägt 10 bis 12 Prozent bei
und ist im Winter stark, wenn die Sonne wenig liefert. Photovoltaik liegt bei 5 bis 7 Prozent, wächst aber
von allen Quellen am schnellsten (Stand 2025).</p>
{A.table(
    ["Energieträger", "Hauptnutzung", "Anteil an der Stromerzeugung (ca., 2025)"],
    [
        ["Wasserkraft", "Strom", "rund 60 %"],
        ["Windenergie", "Strom", "10 bis 12 %, wachsend"],
        ["Photovoltaik", "Strom", "5 bis 7 %, stark wachsend"],
        ["Biomasse", "Wärme und Strom", "stabil, vor allem im Wärmesektor"],
        ["Geothermie", "Wärme", "gering, mit Potenzial"],
    ],
    hl_cols=(2,),
)}
<p>Für die einzelne Dachanlage sind diese Richtwerte entscheidend:</p>
<ul>
  <li><b>Ertrag:</b> Eine 10-kWp-Anlage erzeugt in Österreich rund 10.000 kWh pro Jahr, je nach Standort,
  Ausrichtung und Neigung. Ein Referenzprojekt von EBZ Energie in Villach mit 10 kWp in Ost-West-Ausrichtung
  liefert rund 11.000 kWh.</li>
  <li><b>Fläche:</b> 10 kWp benötigen 50 bis 60 Quadratmeter Dachfläche, das sind 22 bis 25 Module.</li>
  <li><b>Ausrichtung:</b> Ideal ist Süd mit rund 30 Grad Neigung. Ost-West-Dächer liefern morgens und abends
  Strom, genau dann, wenn der Bedarf hoch ist, und erhöhen so den Eigenverbrauch.</li>
  <li><b>Verbrauch:</b> Ein Vier-Personen-Haushalt braucht rund 4.500 kWh im Jahr, mit Wärmepumpe und E-Auto
  8.000 kWh und mehr.</li>
  <li><b>Verschattung und Statik:</b> Bäume, Nachbargebäude und Kamine mindern den Ertrag, das Dach muss die
  Last tragen. Beides klärt ein Projektbericht mit 3D-Belegplan und Statikreport.</li>
</ul>
"""),
        ("Vorteile der Solarenergie", "vorteile", f"""
<ul>
  <li><b>Niedrige Stromkosten:</b> Eine Kilowattstunde vom eigenen Dach kostet in der Gestehung einen Bruchteil
  des Netzbezugs von rund 32 Cent. Mit Speicher sinkt die Stromrechnung um bis zu 85 Prozent.</li>
  <li><b>Unabhängigkeit:</b> Selbst erzeugter Strom ist von Preisschwankungen am Markt und von Importen
  unabhängig. Nach der Anfangsinvestition liefert die Sonne kostenlos.</li>
  <li><b>Klimaschutz:</b> PV erzeugt im Betrieb kein CO₂, keinen Feinstaub und keinen Lärm. Die Energiebilanz
  ist nach wenigen Betriebsjahren positiv, danach liefert die Anlage Jahrzehnte netto saubere Energie.</li>
  <li><b>Dezentralität:</b> Viele kleine Anlagen erzeugen Strom dort, wo er verbraucht wird, das entlastet
  Netze und reduziert Übertragungsverluste.</li>
  <li><b>Wertsteigerung:</b> Ein Haus mit niedrigen Energiekosten und moderner Technik erzielt am Markt höhere
  Preise.</li>
  <li><b>Recycling:</b> Module bestehen überwiegend aus Glas, Aluminium und Silizium und sind zu einem hohen
  Anteil recycelbar.</li>
</ul>
{A.cta("Was liefert Ihr Dach?",
       "Wir prüfen Ausrichtung, Fläche und Verschattung und erstellen einen Projektbericht mit 3D-Belegplan "
       "und Statikreport, kostenlos und unverbindlich.",
       secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
        ("Grenzen und ehrliche Einordnung", "grenzen", f"""
<p>Solarenergie hat physikalische Grenzen, die eine seriöse Planung berücksichtigt:</p>
<ul>
  <li><b>Winter:</b> Kurze Tage und flache Sonne bedeuten im Dezember und Jänner nur einen Bruchteil des
  Sommerertrags. Eine 100-prozentige Autarkie ist mit Dachanlage und Batteriespeicher nicht erreichbar, übers
  Jahr sind 70 bis 80 Prozent realistisch.</li>
  <li><b>Speichergrenzen:</b> Ein Batteriespeicher überbrückt Stunden, keine Wochen. Ein zu großer Speicher wird
  im Winter nie voll, ein zu kleiner ist im Sommer schnell am Limit.</li>
  <li><b>Einspeisung bringt wenig:</b> Der OeMAG-Marktpreis für eingespeisten Strom lag im Juli 2026 bei
  6,146 Cent je kWh. Wirtschaftlich zählt der Eigenverbrauch, nicht der Verkauf (siehe
  {a('/einspeisetarif-fuer-photovoltaik/', 'Einspeisetarif für Photovoltaik')}).</li>
  <li><b>Netz:</b> Viele Anlagen in einem Netzabschnitt können die Leitungen an die Grenze bringen. Speicher,
  Energiemanagement und {a('eg', 'Energiegemeinschaften')} helfen, Erzeugung und Verbrauch lokal abzustimmen.</li>
  <li><b>Verschleißteile:</b> Der Wechselrichter muss nach 10 bis 15 Jahren meist getauscht werden, der Speicher
  verliert nach 10 bis 15 Jahren an Kapazität. Beides gehört in die Kalkulation.</li>
</ul>
"""),
        ("Wirtschaftlichkeit und Förderung in Kürze", "wirtschaftlichkeit", f"""
<p>Eine 10-kWp-Anlage kostet 2026 ohne Speicher rund 10.000 bis 15.000 Euro, mit Speicher rund 15.000 bis
22.000 Euro vor Förderung. Der Bund zahlt 150 Euro je kWp bis 10 kWp und 150 Euro je kWh Speicher, in Kärnten
kommen 3.000 Euro Landespauschale dazu. Einnahmen aus der Einspeisung sind für Private bis 12.500 kWh pro
Jahr einkommensteuerfrei. In EBZ-Projekten mit hohem Eigenverbrauch amortisiert sich die Anlage
typischerweise in 4 bis 6 Jahren, danach liefert sie noch zwei Jahrzehnte nahezu kostenlosen Strom.</p>
<p>Die Details finden Sie in den Ratgebern {a('/kosten-einer-solaranlage/', 'Kosten einer Solaranlage')}
und {a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}, die
Komplettanlage im Ratgeber
{a('/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/', 'Photovoltaik-Komplettanlage 10 kWp mit Speicher und Montage')}.</p>
"""),
        ("Pflege und Lebensdauer", "pflege", f"""
<p>Photovoltaikanlagen sind wartungsarm, weil keine beweglichen Teile verschleißen. Module haben meist 20 bis
25 Jahre Leistungsgarantie und halten in der Praxis 30 Jahre und länger, EBZ Energie gibt bis zu 30 Jahre
Leistungsgarantie. Regen reinigt die Module bei ausreichender Neigung von selbst, nur in der Nähe von
Landwirtschaft oder Industrie lohnt sich alle paar Jahre eine professionelle Reinigung. Eine Sichtprüfung
der Anlage und des Wechselrichters im Abstand einiger Jahre sichert den Ertrag, das Monitoring per App
zeigt Abweichungen sofort.</p>
{A.cta("Von der Grundlage zur eigenen Anlage",
       "Kostenlose Beratung, Projektbericht mit 3D-Belegplan und Statikreport und Montage durch unser "
       "eigenes Team in Kärnten und der Steiermark.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("referenzen", "Referenzen ansehen"))}
"""),
        ("Fazit", "fazit", f"""
<p>Solarenergie ist die am schnellsten wachsende Stromquelle Österreichs und für Eigenheime die einfachste
Möglichkeit, selbst zum Erzeuger zu werden. Die Technik ist ausgereift: 10 kWp auf 50 bis 60 Quadratmetern
liefern rund 10.000 kWh im Jahr, ein Speicher hebt den Eigenverbrauch auf 60 bis 80 Prozent, die Module halten
25 bis 30 Jahre. Die Grenzen liegen im Winter und beim Speicher, nicht in der Technik selbst. Wer die Anlage
auf den eigenen Verbrauch plant, holt das Maximum aus jedem Quadratmeter Dach.</p>
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik: EBZ Energie aus Villach",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie plant und montiert Photovoltaikanlagen, Speicher und Wärmepumpen in Kärnten und der "
                 "Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften und über 300 "
                 "dokumentierten Projekten in 6 Bundesländern. Jede Anlage wird auf Dach und Verbrauch geplant, "
                 "mit Projektbericht, 3D-Belegplan und Statikreport."),
        "grid": [
            ("Individuelle Planung", "Ausrichtung, Verschattung, Statik und Verbrauch vor Ort geprüft."),
            ("Alles aus einer Hand", "Module, Wechselrichter, Speicher, Montage, Netzzutritt und Förderung."),
            ("Garantie", "Bis zu 30 Jahre Leistungsgarantie, mindestens 10 Jahre Produktgarantie."),
            ("Regional", "Villach, Kärnten und Steiermark: kurze Wege bei Montage und Service."),
        ],
    },

    "faq": [
        ("Was ist der Unterschied zwischen Photovoltaik und Solarthermie?",
         "Photovoltaik wandelt Sonnenlicht in Strom um, der alle Geräte, eine Wärmepumpe oder ein E-Auto versorgt "
         "und ins Netz eingespeist werden kann. Solarthermie erwärmt Wasser für Heizung und Brauchwasser. Für "
         "Eigenheime, die unabhängig werden wollen, ist heute Photovoltaik die erste Wahl, mit Wärmepumpe deckt "
         "sie auch den Wärmebedarf."),
        ("Wie funktioniert eine Photovoltaikanlage?",
         "Sonnenlicht setzt in Siliziumzellen Elektronen in Bewegung, es entsteht Gleichstrom. Der Wechselrichter "
         "wandelt ihn in Wechselstrom für den Haushalt um. Was nicht direkt verbraucht wird, lädt den Speicher, der "
         "Rest fließt ins Netz. Der Vorgang kommt ohne bewegliche Teile aus."),
        ("Wie viel Strom liefert eine Solaranlage in Österreich?",
         "Eine 10-kWp-Anlage erzeugt rund 10.000 kWh pro Jahr, das entspricht dem Bedarf eines Vier-Personen-"
         "Haushalts mit Reserve für Wärmepumpe oder E-Auto. Süddächer liefern die höchsten Spitzen, Ost-West-"
         "Anlagen verteilen den Ertrag gleichmäßiger über den Tag."),
        ("Lohnt sich Solarenergie auch bei bewölktem Himmel?",
         "Ja. Module nutzen auch die diffuse Strahlung, die durch Wolken dringt. Der Ertrag ist an sonnigen Tagen "
         "am höchsten, aber auch bei bedecktem Himmel produziert die Anlage. Im Jahresmittel deckt eine gut geplante "
         "Anlage in Österreich einen Großteil des Eigenbedarfs."),
        ("Kann ich mein ganzes Haus mit Solarstrom versorgen?",
         "Im Sommer meist ja, besonders mit Speicher. Im Winter reicht der Ertrag nicht, dann wird Strom aus dem "
         "Netz bezogen. Übers Jahr sind 70 bis 80 Prozent Autarkie erreichbar, eine 100-prozentige Versorgung ist "
         "mit Dachanlage und Batteriespeicher nicht realistisch."),
        ("Ist mein Dach für Photovoltaik geeignet?",
         "Die meisten Dächer sind geeignet. Ideal ist Süd mit rund 30 Grad Neigung, Ost-West-Dächer sind ebenfalls "
         "rentabel. Wichtig sind wenig Verschattung durch Bäume oder Nachbargebäude und eine ausreichende "
         "Statik. Beides prüft ein Fachbetrieb vor Ort, bei EBZ Energie mit 3D-Belegplan und Statikreport."),
        ("Wie lange hält eine Photovoltaikanlage?",
         "Module halten 25 bis 30 Jahre, oft länger, mit bis zu 30 Jahren Leistungsgarantie. Der Wechselrichter "
         "muss nach 10 bis 15 Jahren meist getauscht werden, der Speicher verliert nach 10 bis 15 Jahren an "
         "Kapazität. Da keine beweglichen Teile verbaut sind, ist der Verschleiß minimal."),
        ("Wie wichtig ist Photovoltaik im österreichischen Strommix?",
         "Rund 60 Prozent des Stroms kommen aus Wasserkraft, 10 bis 12 Prozent aus Windkraft und 5 bis 7 Prozent "
         "aus Photovoltaik (Stand 2025). Photovoltaik wächst von allen Quellen am schnellsten, weil sie dezentral "
         "auf Dächern ausgebaut werden kann und im Sommer die Wasserkraft ergänzt."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team hat über 300 Photovoltaikanlagen "
                    "in 6 Bundesländern geplant und montiert. Die Zahlen in diesem Grundlagen-Ratgeber stammen aus "
                    "der Projektpraxis und öffentlichen Statistiken zum österreichischen Strommix, Stand 2025."),
    "sources": [
        ("E-Control: Statistik zur Stromerzeugung in Österreich", "https://www.e-control.at/"),
        ("OeMAG: Marktpreis für Photovoltaik", "https://www.oemag.at/"),
    ],
    "related": [
        ("photovoltaik", "Photovoltaik: Planung und Montage"),
        ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage 2026"),
        ("/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/", "Komplettanlage 10 kWp mit Speicher"),
        ("/einspeisetarif-fuer-photovoltaik/", "Einspeisetarif für Photovoltaik"),
    ],
    "cta": {
        "h3": "Vom Wissen zur Anlage",
        "text": "Kostenlose Beratung und Projektbericht mit 3D-Belegplan und Statikreport für Ihr Dach.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Machen Sie Ihr Dach zum Kraftwerk",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
