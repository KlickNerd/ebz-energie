"""Ratgeber: Photovoltaik-Komplettanlage 10 kWp mit Speicher und Montage (Preis-Anker-Seite).

Migriert von /photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/ (Dez. 2025).
Keyword-Stuffing der Quelle entfernt, Preis auf den freigegebenen EBZ-Richtpreis
(15.000 bis 22.000 Euro vor Förderung), Förderung 2026 und Garantien nach EBZ-Fakten.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage",
    "path": "/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/",
    "cluster": "Photovoltaik",
    "title": "PV-Komplettanlage 10 kWp mit Speicher und Montage | EBZ",
    "description": ("PV-Komplettanlage 10 kWp mit Speicher und Montage: 15.000 bis 22.000 € vor Förderung, "
                    "10.000 kWh pro Jahr, 2 bis 3 Tage Montage. Lieferumfang und Preis."),
    "eyebrow": "Photovoltaik · Komplettanlage",
    "crumb_label": "Komplettanlage 10 kWp",
    "h1": "Photovoltaik-Komplettanlage 10 kWp mit Speicher und Montage: Preis, Lieferumfang, Ertrag",
    "lead": ("Die 10-kWp-Anlage mit Speicher ist der Standard für Einfamilienhäuser in Österreich: rund 10.000 "
             "Kilowattstunden Ertrag pro Jahr, Eigenverbrauch bis 80 Prozent und ein Komplettpreis von rund "
             "15.000 bis 22.000 Euro vor Förderung. Dieser Ratgeber zeigt, was im Paket steckt und was es bringt."),
    "chips": [
        "Komplettpreis: <b>15.000 bis 22.000 €</b> vor Förderung",
        "Ertrag: <b>rund 10.000 kWh</b> pro Jahr",
        "Montage: <b>2 bis 3 Tage</b> vor Ort",
        "Garantie: <b>bis 30 Jahre</b> Leistung",
    ],
    "date_published": "2025-12-19",
    "date_modified": "2026-09-24",
    "hero_img": "gen_detail",
    "hero_alt": "Montage einer Photovoltaik-Komplettanlage mit 10 kWp auf einem Einfamilienhausdach",

    "tldr": [
        "Eine Komplettanlage mit 10 kWp und Speicher kostet bei EBZ Energie rund 15.000 bis 22.000 Euro vor "
        "Förderung, inklusive Module, Hybrid-Wechselrichter, Speicher, Montage, Elektroinstallation und "
        "Anmeldung beim Netzbetreiber.",
        "22 bis 25 Module auf 50 bis 60 Quadratmetern Dach liefern in Österreich rund 10.000 kWh pro Jahr, "
        "mehr als ein durchschnittlicher Haushalt verbraucht, mit Reserve für Wärmepumpe und E-Auto.",
        "Ein Speicher mit 5 bis 10 kWh hebt den Eigenverbrauch von rund 30 auf 60 bis 80 Prozent, die "
        "Stromrechnung sinkt um bis zu 85 Prozent.",
        "Förderung 2026: 1.500 Euro für die PV-Anlage plus 150 Euro je kWh Speicher vom Bund, in Kärnten "
        "zusätzlich 3.000 Euro Landespauschale.",
        "Die Montage dauert 2 bis 3 Tage, es ist keine Baugenehmigung nötig, nur der Netzzutrittsantrag. "
        "Finanzierung ab 147 Euro im Monat, die Anlage gehört Ihnen ab Tag 1.",
    ],
    "kpis": [
        ("15.000 bis 22.000 €", "Komplettpreis vor Förderung"),
        ("10.000 kWh", "Jahresertrag bei 10 kWp"),
        ("bis 85 %", "weniger Stromkosten"),
        ("2 bis 3 Tage", "Montage und Inbetriebnahme"),
    ],

    "sections": [
        ("Warum 10 kWp die richtige Größe für das Einfamilienhaus ist", "warum-10-kwp", f"""
<p>Für die meisten Einfamilienhäuser in Österreich hat sich eine Anlagenleistung von rund 10 Kilowatt-Peak
(kWp) als Optimum herauskristallisiert. Je nach Standort, Ausrichtung und Neigung erzeugt eine solche
Anlage etwa 10.000 Kilowattstunden Strom pro Jahr. Das ist mehr, als ein durchschnittlicher Haushalt mit
4.000 bis 5.000 kWh verbraucht, und lässt Reserven für eine Wärmepumpe oder ein E-Auto.</p>
<p>Gleichzeitig ist 10 kWp die Grenze der Förderkategorie A des Bundes, in der 2026 der höchste Fördersatz
gilt, und die Fixkosten für Gerüst, Wechselrichter und Elektroanschluss verteilen sich auf genügend
Module, sodass der Preis je kWp günstig ausfällt. Benötigt werden rund 50 bis 60 Quadratmeter Dachfläche
für 22 bis 25 Module. Auch Ost-West-Dächer eignen sich gut: Sie liefern morgens und abends Strom, genau
dann, wenn der Haushalt ihn braucht.</p>
<p>Der Speicher ist der zweite Baustein. Ohne ihn fließt der Mittagsüberschuss für 5 bis 10 Cent je
Kilowattstunde ins Netz, während Sie abends Strom für rund 32 Cent zukaufen. Mit Speicher nutzen Sie den
Sonnenstrom bis in die Nacht und steigern den Eigenverbrauch von rund 30 auf 60 bis 80 Prozent.</p>
"""),
        ("Was in der Komplettanlage enthalten ist", "lieferumfang", f"""
<p>Der Vorteil eines Komplettpakets liegt in der Abstimmung: Module, Wechselrichter und Speicher passen
zusammen, und Sie koordinieren weder Dachdecker noch Elektriker. Bei EBZ Energie umfasst die
Komplettanlage folgende Leistungen:</p>
{A.table(
    ["Position", "Inhalt"],
    [
        ["Planung", "Projektbericht mit 3D-Belegplan und Statikreport, Beratung vor Ort"],
        ["Solarmodule", "22 bis 25 Hochleistungsmodule, meist Glas-Glas und Full Black"],
        ["Wechselrichter", "Hybrid-Wechselrichter für PV und Speicher, App-Monitoring"],
        ["Batteriespeicher", "5 bis 10 kWh, modular erweiterbar, Lithium-Eisenphosphat"],
        ["Montage", "Unterkonstruktion, Gerüst, Verkabelung, Blech-Ersatzziegel statt bearbeiteter Dachziegel"],
        ["Elektroinstallation", "Anschluss von Wechselrichter und Speicher, Prüfung des Zählerschranks"],
        ["Anmeldung", "Netzzutrittsantrag, Fertigstellungsmeldung, Förderanträge"],
        ["Inbetriebnahme", "Einrichtung, Einweisung, Übergabe der Dokumentation"],
    ],
)}
<p>Nicht enthalten sind bauliche Sonderleistungen wie eine Zählerschrank-Erneuerung (oft über 1.000 Euro)
oder Sonderdächer mit Blechfalz und Schiefer. Diese Positionen weisen wir im Angebot getrennt aus, damit
Sie Angebote vergleichen können.</p>
"""),
        ("Was die Komplettanlage kostet", "preis", f"""
<p>Der Richtpreis für eine 10-kWp-Komplettanlage mit Speicher und Montage liegt bei EBZ Energie bei rund
15.000 bis 22.000 Euro vor Förderung. Innerhalb dieser Spanne entscheiden Speichergröße, Modultyp,
Dachform und Extras wie Notstrom oder Wallbox über den Endpreis. Ohne Speicher liegt eine 10-kWp-Anlage
bei rund 10.000 bis 15.000 Euro.</p>
{A.table(
    ["Förderung für 10 kWp + 10 kWh (2026)", "Betrag*"],
    [
        ["EAG-Bund, PV-Anlage (150 €/kWp)", "1.500 €"],
        ["EAG-Bund, Speicher (150 €/kWh)", "1.500 €"],
        ["Made-in-Europe-Bonus (10 % je Komponente)", "rund 450 €"],
        ["Landespauschale Kärnten (PV ab 5 kWp mit Speicher ab 5 kWh)", "3.000 €"],
        ["Summe in Kärnten", "rund 6.450 €"],
    ],
    hl_cols=(1,),
)}
<p>Nach Abzug der Förderung bleiben in Kärnten also rund 9.000 bis 15.500 Euro, in der Steiermark und den
anderen Bundesländern rund 12.000 bis 18.500 Euro. Seit 1. April 2025 gilt wieder der reguläre
Umsatzsteuersatz von 20 Prozent, der Nullsteuersatz ist ausgelaufen. Die vollständige Aufschlüsselung
finden Sie im Ratgeber {a('/kosten-einer-solaranlage/', 'Kosten einer Solaranlage')}, die Fördertermine
im Ratgeber {a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}.</p>
<p><small>*Beispielkonditionen nach EAG-Investitionszuschüsseverordnung 2026 und Kärntner Landesrichtlinie,
Stand Juni 2026. Der EAG-Antrag muss vor Inbetriebnahme gestellt werden.</small></p>
{A.cta("Komplettanlage für Ihr Dach berechnen",
       "Wir liefern Ihnen ein Festpreisangebot mit Projektbericht, 3D-Belegplan und Statikreport und "
       "prüfen alle Förderungen für Ihren Standort.",
       secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
        ("Die Technik: Module, Wechselrichter und Speicher", "technik", f"""
<h3>Hochleistungsmodule</h3>
<p>Die Basis jeder Anlage sind die Module. EBZ Energie setzt häufig auf Module von Trina Solar, etwa aus
der Serie Vertex S+, die auch bei schwachem Licht Strom liefern. Die Glas-Glas-Bauweise schützt die Zellen
besser vor Witterung und verlängert die Lebensdauer, die Full-Black-Optik fügt sich unauffällig ins
Dachbild. Auf 10 kWp kommen 22 bis 25 Module.</p>
<h3>Hybrid-Wechselrichter und Speicher</h3>
<p>Der Wechselrichter wandelt den Gleichstrom der Module in Wechselstrom um und steuert Einspeisung,
Hausverbrauch und Speicherladung. In Komplettanlagen kommt meist ein Hybrid-Wechselrichter zum Einsatz,
zum Beispiel von Huawei. Der passende Speicher, etwa der modulare Huawei LUNA2000, lässt sich bei Bedarf
um weitere Batteriemodule erweitern. Per App sehen Sie jederzeit, wie viel Strom Sie produzieren und wie
voll der Speicher ist.</p>
<h3>Wie groß sollte der Speicher sein?</h3>
<p>Bei 10 kWp sind 5 bis 10 kWh üblich. Ein 5-kWh-Speicher deckt den Nachtbedarf im Sommer, wer eine
Wärmepumpe betreibt oder das Auto zu Hause lädt, greift zu 10 kWh. Als Faustregel gilt 1:1, also 10 kWh
Speicher für 10 kWp. Bei der Dimensionierung hilft der Ratgeber
{a('/ab-wann-lohnt-sich-photovoltaik-mit-speicher/', 'Ab wann lohnt sich Photovoltaik mit Speicher')}.</p>
{A.net([
    ("☀", "22 bis 25 Module", "Glas-Glas, Full Black, rund 10.000 kWh pro Jahr"),
    ("◎", "Hybrid-Wechselrichter", "steuert Einspeisung, Verbrauch und Speicher, App-Monitoring"),
    ("▮", "Speicher 5 bis 10 kWh", "modular erweiterbar, Notstrom optional"),
    ("⌖", "Wallbox und Wärmepumpe", "nutzen den Überschuss, jederzeit nachrüstbar"),
], "Ein abgestimmtes System",
   "Alle Komponenten kommen vom selben Fachbetrieb, sind aufeinander abgestimmt und über Jahre erweiterbar.")}
"""),
        ("Wirtschaftlichkeit: Was die Anlage jedes Jahr bringt", "wirtschaftlichkeit", f"""
<p>Die Rechnung ist einfach: Jede selbst verbrauchte Kilowattstunde ersetzt Netzstrom für rund 32 Cent,
jede eingespeiste bringt aktuell rund 6 Cent (OeMAG-Marktpreis Juli 2026: 6,146 Cent). Mit Speicher und
60 bis 80 Prozent Eigenverbrauch sinkt die Stromrechnung um bis zu 85 Prozent. Ein Beispiel aus den
{a('referenzen', 'EBZ-Referenzen')}: Ein Einfamilienhaus in Villach mit 10 kWp in Ost-West-Ausrichtung,
Speicher und Notstrom erzeugt rund 11.000 kWh pro Jahr und hat seine Stromkosten um etwa 80 Prozent
gesenkt.</p>
<p>In EBZ-Projekten mit hohem Eigenverbrauch liegt die Amortisation typischerweise bei 4 bis 6 Jahren.
Danach produziert die Anlage noch zwei Jahrzehnte nahezu kostenlosen Strom. Dazu kommt der Wertzuwachs
der Immobilie: Ein Haus mit niedrigen Energiekosten ist am Markt gefragter. Und die Einnahmen aus der
Einspeisung sind für Privatpersonen bis 12.500 kWh pro Jahr einkommensteuerfrei (Anlagen bis 35 kWp),
mehr dazu im Ratgeber {a('/einspeisetarif-fuer-photovoltaik/', 'Einspeisetarif für Photovoltaik')}.</p>
"""),
        ("Ablauf: Von der Beratung bis zum ersten Sonnenstrom", "ablauf", f"""
{A.steps([
    ("Beratung und Dachanalyse",
     "Wir prüfen Dach, Verbrauch und Zählerschrank vor Ort und klären, ob Wärmepumpe, Wallbox oder Notstrom "
     "mitgeplant werden sollen."),
    ("Angebot mit Projektbericht",
     "Sie erhalten ein Festpreisangebot mit Projektbericht, 3D-Belegplan und Statikreport, inklusive "
     "Förderübersicht für Ihren Standort."),
    ("Netzzutritt und Förderung",
     "Wir stellen den Netzzutrittsantrag beim Netzbetreiber und den EAG-Antrag im Fördercall, beides vor "
     "der Inbetriebnahme. Eine Baugenehmigung ist für Dachanlagen in der Regel nicht nötig."),
    ("Montage in 2 bis 3 Tagen",
     "Unterkonstruktion und Module sind meist in ein bis zwei Tagen montiert, Wechselrichter und Speicher "
     "werden parallel oder am Folgetag installiert."),
    ("Inbetriebnahme",
     "Fertigstellungsmeldung an den Netzbetreiber, Zählertausch, App-Einrichtung und Übergabe. Danach "
     "kümmern wir uns um die Endabrechnung der Landesförderung."),
])}
{A.box_dark("Reihenfolge beachten",
    "Der EAG-Förderantrag muss <b>vor der Inbetriebnahme</b> im Fördercall gestellt werden (2026: 23. April "
    "bis 11. Mai, 16. bis 30. Juni, ab 8. Oktober). Die Kärntner Landesförderung wird dagegen erst nach "
    "Fertigstellung beantragt. Wir stimmen Montagetermin und Anträge so ab, dass keine Förderung verloren geht.")}
"""),
        ("Garantie und Lebensdauer", "garantie", f"""
<p>Eine Komplettanlage ist auf Jahrzehnte ausgelegt. EBZ Energie gibt bis zu 30 Jahre Leistungsgarantie
auf die Module und mindestens 10 Jahre Produktgarantie auf die Komponenten. Hersteller wie Huawei bieten
auf Wechselrichter meist 10 Jahre, die sich verlängern lassen, Speicher haben in der Regel 10 Jahre
Garantie auf eine bestimmte Restkapazität.</p>
{A.table(
    ["Komponente", "Typische Lebensdauer", "Garantie"],
    [
        ["Solarmodule", "25 bis 30 Jahre, oft länger", "bis zu 30 Jahre Leistungsgarantie"],
        ["Wechselrichter", "rund 15 Jahre", "mindestens 10 Jahre Produktgarantie"],
        ["Batteriespeicher", "10 bis 15 Jahre", "mindestens 10 Jahre Produktgarantie"],
    ],
)}
<p>Die laufenden Kosten sind gering: rund 1 bis 2 Prozent der Anschaffungskosten pro Jahr für Wartung,
Reinigung und Rücklagen. Die fachgerechte Montage durch zertifizierte Fachkräfte sichert dabei die
vollen Herstellergarantien.</p>
"""),
        ("Zukunftssicher und finanzierbar: Wallbox, Wärmepumpe, Rate ab 147 Euro", "erweiterbarkeit", f"""
<p>Mit 10 kWp haben Sie genug Überschuss, um in die Sektorenkopplung einzusteigen. Eine Wallbox lädt das
E-Auto mit Sonnenstrom, eine {a('waermepumpe', 'Wärmepumpe')} heizt damit das Haus. Ein
{a('ems', 'Energiemanagementsystem')} verschiebt diese Verbraucher automatisch in die Sonnenstunden und
wird 2026 vom Klima- und Energiefonds mit bis zu 600 Euro gefördert.</p>
<p>Die Speichersysteme sind modular: Steigt der Bedarf in fünf Jahren, weil ein zweites E-Auto dazukommt,
rüsten Sie Batteriemodule nach. Viele Wechselrichter bieten zudem eine Notstromfunktion, die bei
Netzausfall die wichtigsten Verbraucher weiterversorgt. Wer den Speicher erst später nachrüsten will,
findet die Details im Ratgeber {a('/pv-speicher-nachruesten/', 'PV-Speicher nachrüsten')}.</p>
<h3>Finanzierung: ab 147 Euro im Monat</h3>
<p>Sie müssen die Komplettanlage nicht auf einmal bezahlen. Mit der
{a('finanzierung', 'EBZ-Finanzierung')} zahlen Sie ab 147 Euro im Monat inklusive Speicher. Die Anlage
gehört Ihnen ab dem ersten Tag, Sie erhalten die volle Förderung als Privatperson, ohne strenge
Bonitätsprüfung und ohne Datenbankeintrag. In vielen Haushalten liegt die Rate unter der bisherigen
Stromrechnung.</p>
{A.cta("Jetzt Komplettanlage anfragen",
       "Kostenlose Beratung, Festpreisangebot mit Projektbericht, 3D-Belegplan und Statikreport, Montage "
       "durch unser eigenes Team in Kärnten und der Steiermark.",
       primary=("kontakt", "Angebot anfordern"), secondary=("finanzierung", "Zur Finanzierung"))}
"""),
        ("Fazit: Das Standardpaket, das sich rechnet", "fazit", f"""
<p>Die Photovoltaik-Komplettanlage mit 10 kWp, Speicher und Montage ist für die meisten Einfamilienhäuser
die wirtschaftlichste Lösung: rund 10.000 kWh Ertrag, bis zu 85 Prozent weniger Stromkosten, 2 bis 3 Tage
Montage und ein Komplettpreis von rund 15.000 bis 22.000 Euro, von dem Bund und Land 2026 bis zu
6.450 Euro übernehmen. Entscheidend ist ein Partner, der Planung, Montage, Netzzutritt und Förderung aus
einer Hand liefert und auch nach der Inbetriebnahme erreichbar bleibt.</p>
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für die Komplettanlage: EBZ Energie aus Villach",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie plant und montiert Photovoltaik-Komplettanlagen mit Speicher in Kärnten und der "
                 "Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften und über 300 "
                 "dokumentierten Projekten in 6 Bundesländern. Von der Dachanalyse über den Projektbericht mit "
                 "3D-Belegplan und Statikreport bis zu Netzzutritt, Förderung und Inbetriebnahme haben Sie "
                 "einen Ansprechpartner."),
        "grid": [
            ("Alles aus einer Hand", "Planung, Montage, Elektro, Anmeldung und Förderabwicklung vom selben Team."),
            ("Markenqualität", "Module von Trina Solar, Hybrid-Wechselrichter und Speicher von Huawei."),
            ("Garantie", "Bis zu 30 Jahre Leistungsgarantie, mindestens 10 Jahre Produktgarantie."),
            ("Regional vor Ort", "Villach, Kärnten und Steiermark: kurze Wege bei Montage und Service."),
        ],
    },

    "faq": [
        ("Was kostet eine Photovoltaik-Komplettanlage mit 10 kWp und Speicher?",
         "Bei EBZ Energie liegt der Richtpreis bei rund 15.000 bis 22.000 Euro vor Förderung, inklusive Module, "
         "Hybrid-Wechselrichter, Speicher, Montage, Elektroinstallation und Anmeldung. Bund und Land übernehmen "
         "2026 je nach Bundesland 3.000 bis 6.450 Euro davon."),
        ("Wie viel Strom erzeugt eine 10-kWp-Anlage im Jahr?",
         "In Österreich durchschnittlich rund 10.000 kWh pro Jahr. Süddächer liefern die höchsten Spitzen, "
         "Ost-West-Anlagen verteilen den Ertrag gleichmäßiger über den Tag. Ein Referenzprojekt in Villach mit "
         "10 kWp Ost-West erzeugt rund 11.000 kWh jährlich."),
        ("Wie groß muss der Speicher für eine 10-kWp-Anlage sein?",
         "Üblich sind 5 bis 10 kWh. Ein 5-kWh-Speicher deckt den Nachtbedarf im Sommer, mit Wärmepumpe oder "
         "E-Auto empfehlen sich 10 kWh. Als Faustregel gilt 1:1, also 10 kWh Speicher zu 10 kWp Leistung. "
         "Modulare Systeme lassen sich später erweitern."),
        ("Wie lange dauert die Montage der Komplettanlage?",
         "Unterkonstruktion und Module sind meist in ein bis zwei Tagen montiert, die Elektroinstallation von "
         "Wechselrichter und Speicher dauert etwa einen weiteren Tag. In der Regel ist die Anlage nach 2 bis 3 "
         "Tagen betriebsbereit. Ein Mehrfamilienhaus in Krumpendorf mit 25 kWp und 25 kWh wurde in 4 Tagen "
         "fertiggestellt."),
        ("Brauche ich eine Genehmigung für die PV-Anlage?",
         "Für Dachanlagen dieser Größe ist in Österreich in der Regel keine Baugenehmigung nötig. Zwingend ist "
         "der Netzzutrittsantrag beim Netzbetreiber und, für die Bundesförderung, der EAG-Antrag vor der "
         "Inbetriebnahme. Beides übernimmt EBZ Energie für Sie."),
        ("Welche Garantie habe ich auf die Komponenten?",
         "EBZ Energie gibt bis zu 30 Jahre Leistungsgarantie auf die Module und mindestens 10 Jahre "
         "Produktgarantie auf die Komponenten. Wechselrichter von Huawei haben meist 10 Jahre Garantie, "
         "verlängerbar, Speicher 10 Jahre auf eine definierte Restkapazität."),
        ("Wie schnell amortisiert sich die Komplettanlage?",
         "Mit Speicher und 60 bis 80 Prozent Eigenverbrauch sinkt die Stromrechnung um bis zu 85 Prozent. In "
         "EBZ-Projekten mit hohem Eigenverbrauch liegt die Amortisation typischerweise bei 4 bis 6 Jahren, "
         "danach liefert die Anlage noch rund 20 Jahre nahezu kostenlosen Strom."),
        ("Kann ich die Komplettanlage finanzieren?",
         "Ja, ab 147 Euro im Monat inklusive Speicher. Die Anlage gehört Ihnen ab dem ersten Tag, Sie erhalten "
         "die volle private Förderung, ohne strenge Bonitätsprüfung und ohne Datenbankeintrag."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team hat über 300 Photovoltaikanlagen "
                    "geplant und montiert, die 10-kWp-Komplettanlage mit Speicher ist das meistgebaute Paket. "
                    "Preise und Förderwerte in diesem Ratgeber sind Richtwerte aus der laufenden Angebotspraxis, "
                    "Stand September 2026."),
    "sources": [
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("OeMAG: Marktpreis für Photovoltaik", "https://www.oemag.at/"),
    ],
    "related": [
        ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage 2026"),
        ("/photovoltaik-foerderung-oesterreich-2026/", "Photovoltaik-Förderung Österreich 2026"),
        ("batteriespeicher", "Batteriespeicher: Kapazität und Technik"),
        ("referenzen", "Referenzen: über 300 Projekte"),
    ],
    "cta": {
        "h3": "Festpreis für Ihre Komplettanlage",
        "text": "Kostenlose Beratung und Angebot mit Projektbericht, 3D-Belegplan und Statikreport.",
        "primary": ("kontakt", "Angebot anfordern"),
    },
    "final_h2": "Ihre 10-kWp-Anlage aus einer Hand",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
