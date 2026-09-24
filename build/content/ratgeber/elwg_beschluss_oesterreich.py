"""Ratgeber: ElWG-Beschluss Österreich (Was PV-Betreiber wissen müssen).

Migriert von ebz-photovoltaik.at/elwg-beschluss-oesterreich/ (Stand der Quelle: Dezember 2025).
Bereinigt: Marketing-Ton, Gedankenstriche, unbelegte Kundenanteil-Prozentangabe,
"Wirtschaftlichkeitsberechnung" durch Projektbericht ersetzt. Zahlen aus der Quelle.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "elwg-beschluss-oesterreich",
    "path": "/elwg-beschluss-oesterreich/",
    "title": "ElWG-Beschluss: Was PV-Betreiber wissen müssen | EBZ",
    "description": ("ElWG beschlossen: PV bis 20 kW ohne Infrastrukturbeitrag, 0,05 ct/kWh ab 2027 darüber, "
                    "70-Prozent-Spitzenkappung, Speicher 20 Jahre befreit. Die Folgen für Sie."),
    "eyebrow": "Recht · Elektrizitätswirtschaftsgesetz",
    "crumb_label": "ElWG-Beschluss Österreich",
    "h1": "ElWG-Beschluss Österreich: Die 4 wichtigsten Regeln für PV-Betreiber",
    "lead": ("Der Nationalrat hat im Dezember 2025 das neue Elektrizitätswirtschaftsgesetz (ElWG) beschlossen. "
             "Es ersetzt das ElWOG aus dem Jahr 2010 und regelt, wer für das Netz zahlt, wie viel eine "
             "PV-Anlage einspeisen darf und warum Batteriespeicher gesetzlich bessergestellt sind."),
    "chips": [
        "Bis <b>20 kW</b>: kein Infrastrukturbeitrag",
        "Über 20 kW: <b>0,05 ct/kWh</b> ab 2027",
        "Spitzenkappung: <b>70 %</b> der Leistung",
        "Speicher: <b>20 Jahre</b> beitragsfrei",
    ],
    "date_published": "2025-12-10",
    "date_modified": "2026-09-24",
    "hero_img": "gen_hero",
    "hero_alt": "Photovoltaikanlage auf einem Einfamilienhausdach, das unter die 20-kW-Befreiung des ElWG fällt",

    "tldr": [
        "Das ElWG wurde am 11. Dezember 2025 im Nationalrat beschlossen und ersetzt das ElWOG von 2010. Es "
        "schafft klare Spielregeln für die Integration erneuerbarer Energien ins Stromnetz.",
        "Photovoltaikanlagen mit einer Engpassleistung bis 20 kW sind vollständig vom neuen "
        "Versorgungsinfrastrukturbeitrag befreit. Das betrifft praktisch alle Einfamilienhäuser mit 8 bis "
        "15 kWp.",
        "Anlagen über 20 kW zahlen ab 2027 einen fixen Beitrag von 0,05 Cent je eingespeister "
        "Kilowattstunde. Bestehende Verträge und Förderungen haben Bestandsschutz.",
        "Netzbetreiber dürfen die Einspeiseleistung neuer Anlagen auf 70 Prozent der installierten "
        "Leistung begrenzen. Der Eigenverbrauch ist davon nicht betroffen, der rechnerische Verlust ohne "
        "Gegenmaßnahmen liegt bei 3 bis 5 Prozent des Jahresertrags.",
        "Systemdienliche Batteriespeicher sind 20 Jahre lang von Infrastrukturbeiträgen befreit und fangen "
        "die gekappten Mittagsspitzen auf.",
    ],
    "kpis": [
        ("20 kW", "Grenze für die Beitragsbefreiung"),
        ("0,05 ct/kWh", "Beitrag über 20 kW, ab 2027"),
        ("70 %", "maximale Einspeiseleistung neuer Anlagen"),
        ("3 bis 5 %", "rechnerischer Verlust ohne Speicher"),
    ],

    "sections": [
        ("Was ist das ElWG und warum war es nötig?", "was-ist", f"""
<p>Das Elektrizitätswirtschaftsgesetz (ElWG) ist das neue Grundgesetz des österreichischen Strommarkts.
Der Nationalrat hat den Kompromiss am 11. Dezember 2025 beschlossen, nach mehreren Verhandlungsrunden,
die viele Anlagenbetreiber verunsichert haben. Das ElWG ersetzt das Elektrizitätswirtschafts- und
-organisationsgesetz (ElWOG) aus dem Jahr 2010, das aus einer Zeit stammte, in der Photovoltaik noch
eine Nische war.</p>
<p>Seither sind Modulpreise gesunken und die Zahl der Anlagen ist stark gestiegen. Das Stromnetz ist
keine Einbahnstraße mehr: An sonnigen Tagen zur Mittagszeit stoßen die Netze in manchen Regionen an ihre
Grenzen. Das ElWG regelt, wer für die Netzinfrastruktur zahlt, wie viel eine Anlage einspeisen darf, und
welche Pflichten Netzbetreiber und die Regulierungsbehörde E-Control haben. Für Sie als Betreiber einer
{a('photovoltaik', 'Photovoltaikanlage')} in Kärnten oder der Steiermark sind vier Regeln entscheidend.</p>
"""),
        ("Regel 1: Kosten für die Netzinfrastruktur", "infrastrukturbeitrag", f"""
<p>Der größte Streitpunkt in den Verhandlungen war die Frage: Wer zahlt für das Netz, wenn immer mehr
Menschen ihren Strom selbst produzieren und weniger vom Versorger beziehen? Lange wurde eine
„Sonnensteuer“ befürchtet, also eine Abgabe für jeden, der Strom einspeist. Das beschlossene Gesetz
gibt Entwarnung und schützt vor allem private Hausbesitzer.</p>
<h3>Privathaushalte bis 20 kW: vollständig befreit</h3>
<p>Photovoltaikanlagen mit einer Engpassleistung bis zu 20 Kilowatt (kW) sind gänzlich vom neuen
Versorgungsinfrastrukturbeitrag befreit. Eine klassische Aufdachanlage auf einem Einfamilienhaus liegt
meist zwischen 8 und 15 kWp, fällt also klar unter diese Grenze. Sie zahlen keine laufenden Gebühren für
das Einspeisen Ihres Überschussstroms. Der Ertrag Ihrer Anlage gehört Ihnen.</p>
<h3>Gewerbe und Landwirtschaft über 20 kW: fixer Deckel ab 2027</h3>
{A.table(
    ["Anlagengröße", "Infrastrukturbeitrag", "Ab wann", "Bestandsschutz"],
    [
        ["bis 20 kW Engpassleistung", "0 ct/kWh, vollständig befreit", "sofort", "nicht nötig"],
        ["über 20 kW netzwirksame Leistung", "0,05 ct/kWh eingespeister Strom", "ab 2027", "bestehende Verträge und Förderungen bleiben"],
        ["systemdienliche Speicher", "0 ct/kWh für 20 Jahre", "sofort", "ja"],
    ],
    hl_cols=(1,),
)}
<p>Rechenbeispiel für eine Gewerbeanlage: Bei 40.000 kWh Einspeisung im Jahr ergibt der Beitrag von
0,05 Cent je Kilowattstunde 20 Euro jährlich*. Ursprünglich standen deutlich höhere und variable Beiträge
im Raum. Für Unternehmen bedeutet der Kompromiss: Die Kosten sind minimal und kalkulierbar, das Risiko
unvorhersehbarer Gebühren ist vom Tisch.</p>
<p><small>*Rechenbeispiel zur Einordnung der Größenordnung. Maßgeblich sind der Gesetzestext und die
Umsetzung durch den Netzbetreiber.</small></p>
"""),
        ("Regel 2: Die 70-Prozent-Regel (Spitzenkappung)", "spitzenkappung", f"""
<p>Um teure Netzausbauten zu begrenzen, gibt das ElWG den Netzbetreibern ein Werkzeug an die Hand: die
Spitzenkappung. Neu errichtete Anlagen können verpflichtet werden, ihre Einspeiseleistung am
Netzanschlusspunkt auf 70 Prozent der installierten Leistung zu begrenzen.</p>
<h3>Rechenbeispiel: 10-kWp-Anlage</h3>
<p>An einem perfekten Sommertag um 13:00 Uhr könnte eine 10-kWp-Anlage theoretisch 10 kW Leistung
erzeugen. Mit Spitzenkappung dürfen maximal 7 kW (70 Prozent) ins öffentliche Netz fließen. Drei Punkte
machen das in der Praxis verkraftbar:</p>
<ul>
  <li><b>Seltenes Ereignis:</b> Die volle Spitzenleistung wird nur an wenigen Stunden im Jahr überhaupt
  erreicht.</li>
  <li><b>Eigenverbrauch zählt nicht:</b> Die Begrenzung gilt nur für den Strom, der das Haus verlässt.
  Läuft mittags die Waschmaschine, lädt das E-Auto oder arbeitet die Wärmepumpe, nutzen Sie die vollen
  10 kW.</li>
  <li><b>Minimaler Verlust:</b> Simulationen zeigen, dass durch die Abregelung der Spitzen aufs Jahr
  gesehen nur etwa 3 bis 5 Prozent des Gesamtertrags verloren gehen, wenn man den Strom nicht selbst
  nutzt.</li>
</ul>
{A.box("Die 70-Prozent-Grenze ist bei richtiger Planung kaum spürbar: Ein Energiemanagementsystem legt "
       "Speicherladung, Warmwasserbereitung und E-Auto-Laden genau in die Mittagsstunden, in denen sonst "
       "gekappt würde.", label="Planungstipp:")}
"""),
        ("Regel 3: Batteriespeicher sind 20 Jahre befreit", "speicher", f"""
<p>Das ElWG ist indirekt das stärkste Argument für einen {a('batteriespeicher', 'Batteriespeicher')}, das
es bisher gab. Der Gesetzgeber hat einen echten Anreiz geschaffen: Systemdienliche Speicher sind für
20 Jahre von den Infrastrukturbeiträgen befreit. Kombiniert mit der Spitzenkappung ergeben sich zwei
Vorteile:</p>
<ul>
  <li><b>Sie umgehen die Kappung:</b> Scheint die Sonne mittags so stark, dass Sie über die
  70-Prozent-Grenze kämen, fließt der Strom nicht ins Netz (wo er gekappt würde), sondern in den
  Speicher. Sie retten den Strom für den Abend.</li>
  <li><b>Sie sparen Gebühren:</b> Durch die gesetzliche Besserstellung amortisiert sich der Speicher
  schneller.</li>
</ul>
<p>Moderne Hybrid-Wechselrichter übernehmen dieses Management vollautomatisch. Sie müssen keinen
Schalter umlegen: Die Anlage weiß selbst, wann sie speichern, verbrauchen oder einspeisen soll. Wie sich
das mit den aktuellen Einspeisetarifen rechnet, zeigt der Ratgeber
{a('/marktpreis-2026/', 'Marktpreis 2026: Lohnt sich Photovoltaik noch?')}.</p>
{A.cta("Anlage nach den neuen Regeln planen lassen",
       "Wir dimensionieren PV-Anlage und Speicher so, dass Spitzenkappung und Infrastrukturbeitrag für Sie "
       "keine Rolle spielen, und übernehmen Netzanfrage und Anmeldung.",
       secondary=("batteriespeicher", "Zum Batteriespeicher"))}
"""),
        ("Regel 4: Neue Pflichten für Netzbetreiber und Anlagen", "pflichten", f"""
<p>Das ElWG bringt auch neue Pflichten für Netzbetreiber und die Regulierungsbehörde E-Control.
Transparenz bei Netzzutrittsentgelten und klare Fristen für den Anschluss sind nun gesetzlich verankert.
Das beendet die Praxis, bei der Anlagenbetreiber oft monatelang auf ihren Zählertausch warten mussten.
Der {a('/smart-meter/', 'Smart Meter')} wird damit zum Standard am Netzanschluss.</p>
<p>Im Gegenzug steigen die technischen Anforderungen bei Anmeldung und Abnahme: Die Anlage muss
kommunikationsfähig sein („Smart Grid Ready“), den neuen Netzstandards entsprechen und korrekt gemeldet
werden. Mit einem entsprechenden Wechselrichter ist die Hardware auch für
{a('/dynamischer-stromtarif/', 'dynamische Stromtarife')} und ein
{a('ems', 'Energiemanagementsystem')} vorbereitet, das der Klimafonds seit Juni 2026 mit bis zu 600 Euro
fördert (siehe {a('/ems-foerderung/', 'EMS-Förderung 2026')}).</p>
{A.table(
    ["Bereich", "Vor dem ElWG", "Mit dem ElWG"],
    [
        ["Netzzutrittsentgelte", "wenig transparent", "Transparenzpflicht"],
        ["Anschlussfristen", "keine verbindlichen Fristen", "gesetzliche Fristen für Netzbetreiber"],
        ["Anlagenanforderung", "Module und Wechselrichter", "kommunikationsfähig, Smart Grid Ready"],
        ["Einspeiseleistung", "unbegrenzt", "bis 70 % der installierten Leistung (neue Anlagen)"],
    ],
    hl_cols=(2,),
)}
"""),
        ("Was bedeutet das für Ihre Entscheidung?", "entscheidung", f"""
<p>Im vergangenen Jahr hörten wir in Beratungen oft: „Ich warte noch ab, was das Gesetz bringt.“ Dieses
Argument ist seit dem 11. Dezember 2025 hinfällig. Der Rahmen steht, die Unsicherheit ist weg.
Solarmodule und Speicher sind aktuell günstig, und die Investitionszuschüsse des Bundes laufen weiter
(Details in der {a('foerderung_at', 'Photovoltaik-Förderung Österreich')}). Wer eine
{a('eg', 'Energiegemeinschaft')} plant, profitiert ebenfalls von den klaren Netzregeln.</p>
<p>Zur Einordnung: Bei EBZ Energie liegen 10 kWp mit Speicher je nach Dach und Komponenten bei rund
15.000 bis 22.000 Euro vor Förderung, die Amortisation typischerweise bei 4 bis 6 Jahren. Wir setzen
auf Glas-Glas-Module, die robuster gegen Hagel und Schneedruck sind, mit bis zu 30 Jahren
Leistungsgarantie und mindestens 10 Jahren Produktgarantie.</p>
"""),
        ("Fazit: Die Ampel steht auf Grün", "fazit", f"""
<p>Der Beschluss des ElWG ist der Startschuss für die nächste Phase der Energiewende in Österreich: eine
Phase der Professionalisierung und der Sicherheit. Lassen Sie sich von Begriffen wie Spitzenkappung oder
Infrastrukturbeitrag nicht verunsichern. Für private Hausbesitzer bis 20 kW ändert sich bei den Kosten
nichts, und für Unternehmer sind die Beiträge minimal und kalkulierbar. Mit Speicher und
Energiemanagement wird aus der 70-Prozent-Regel ein Planungsdetail.</p>
{A.cta("Ihr nächster Schritt zur Unabhängigkeit",
       "Wir erstellen für Ihr Dach einen Projektbericht mit 3D-Belegplan und Statikreport, abgestimmt auf "
       "die neuen gesetzlichen Regeln, Ihr Lastprofil und die passende Speichergröße.",
       primary=("kontakt", "Unverbindliches Angebot anfordern"), secondary=("referenzen", "Referenzen ansehen"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Anmeldung und Umsetzung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("Mit dem ElWG steigt die technische Komplexität bei Anmeldung und Abnahme. Für Kunden von "
                 "EBZ Energie aus Villach entsteht daraus kein Mehraufwand: Wir übernehmen die Kommunikation "
                 "mit dem Netzbetreiber, verbauen nur Komponenten, die den neuen österreichischen Standards "
                 "entsprechen, und begleiten Sie über 300 Projekte Erfahrung in Kärnten und der Steiermark "
                 "hinweg von der Netzanfrage bis zur fertigen Meldung."),
        "grid": [
            ("Netzanfrage und Förderung", "Wir kennen die Formulare und übernehmen den Papierkram."),
            ("Rechtssicher", "Nur Komponenten, die den neuen Netzstandards entsprechen."),
            ("Smart Grid Ready", "Hardware, die für dynamische Tarife und EMS vorbereitet ist."),
            ("Regional verankert", "Wir sind heute da und auch, wenn Ihre Anlage 2045 noch läuft."),
        ],
    },

    "faq": [
        ("Muss ich als privater Hausbesitzer nun Gebühren für die Einspeisung bezahlen?",
         "Nein. Photovoltaikanlagen mit einer Engpassleistung bis zu 20 kW sind vollständig vom neuen "
         "Versorgungsinfrastrukturbeitrag befreit. Sie zahlen keine laufenden Gebühren für das Einspeisen "
         "Ihres überschüssigen Sonnenstroms. Typische Einfamilienhausanlagen mit 8 bis 15 kWp liegen klar "
         "unter dieser Grenze."),
        ("Was bedeutet die 70-Prozent-Regel und verliere ich dadurch viel Strom?",
         "Netzbetreiber dürfen die Einspeisung neuer Anlagen am Netzanschlusspunkt auf 70 Prozent der "
         "installierten Leistung begrenzen. Das betrifft nur den Strom, der das Haus verlässt, nicht den "
         "Eigenverbrauch. Da Spitzenleistungen selten sind, liegt der rechnerische Verlust ohne "
         "Gegenmaßnahmen bei 3 bis 5 Prozent. Mit Batteriespeicher fangen Sie die Spitzen auf."),
        ("Lohnt sich ein Batteriespeicher durch das neue Gesetz noch mehr?",
         "Ja. Systemdienliche Speicher sind für 20 Jahre von Infrastrukturbeiträgen befreit, und der "
         "Speicher ist die technisch einfachste Antwort auf die 70-Prozent-Regel: Statt abgeregelt zu "
         "werden, lädt der Mittagsstrom den Akku und steht am Abend zur Verfügung."),
        ("Welche Kosten kommen auf Gewerbebetriebe mit Anlagen über 20 kW zu?",
         "Ein fixer Beitrag von 0,05 Cent pro eingespeister Kilowattstunde, fällig erst ab 2027. Bei "
         "40.000 kWh Einspeisung im Jahr sind das rund 20 Euro. Bestehende Förderungen und Verträge haben "
         "Bestandsschutz."),
        ("Wird die Anmeldung der PV-Anlage durch die neuen Regeln komplizierter?",
         "Die technischen Anforderungen sind gestiegen: Anlagen müssen kommunikationsfähig und Smart Grid "
         "Ready sein. Im Gegenzug gelten gesetzliche Fristen für Netzbetreiber, was Wartezeiten verkürzt. "
         "EBZ Energie übernimmt die komplette Abwicklung von der Netzanfrage bis zur Meldung."),
        ("Gilt die Spitzenkappung auch für bestehende Anlagen?",
         "Die 70-Prozent-Regel betrifft laut Gesetz neu errichtete Anlagen. Bestehende Verträge und "
         "Förderungen haben Bestandsschutz. Ob und wann Ihr Netzbetreiber die Kappung bei einer Neuanlage "
         "verlangt, klären wir in der Netzanfrage."),
        ("Ab wann gilt das ElWG?",
         "Der Nationalrat hat das Gesetz am 11. Dezember 2025 beschlossen. Die Befreiung bis 20 kW gilt "
         "damit, der Infrastrukturbeitrag für größere Anlagen wird erst ab 2027 fällig."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Photovoltaik, Speicher, Wärmepumpen und Energiemanagementsysteme in Kärnten und der "
                    "Steiermark und wickelt Netzanfrage und Anmeldung für die Kunden ab. Die Angaben beruhen "
                    "auf dem im Dezember 2025 beschlossenen Gesetzestext und werden bei Änderungen der "
                    "Durchführungsbestimmungen aktualisiert. Keine Rechtsberatung, maßgeblich sind Gesetz "
                    "und Netzbetreiber."),
    "sources": [
        ("E-Control: Regulierungsbehörde für Strom und Gas", "https://www.e-control.at/"),
    ],
    "related": [
        ("/marktpreis-2026/", "Marktpreis 2026: Lohnt sich Photovoltaik noch?"),
        ("batteriespeicher", "Batteriespeicher: Mittagsstrom für den Abend"),
        ("/energiegemeinschaft-netzkosten/", "Energiegemeinschaft: Netzkosten sparen"),
        ("foerderung_at", "Photovoltaik-Förderung Österreich"),
    ],
    "cta": {
        "h3": "Anlage nach ElWG planen",
        "text": "Wir rechnen mit den neuen Regeln, Ihrem Lastprofil und der passenden Speichergröße.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihr Dach wird zum Kraftwerk",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Netzanfrage, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
