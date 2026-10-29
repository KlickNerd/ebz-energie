"""Ratgeber: Photovoltaik-Förderung Österreich 2026 (Bundesförderung EAG + Überblick Länder).

Migriert von /photovoltaik-foerderung-oesterreich-2026/ (Dez. 2025). Die Fördersätze der
Quelle (160 €/kWp, Bonus bis 20 %) stammen aus der Zeit vor der EAG-Novelle; sie wurden
auf die mit 16. Jänner 2026 kundgemachten Werte (150/140/130/120 €/kWp, 10 % je Komponente)
angeglichen, damit der Artikel zu den Bundesland-Ratgebern und zum Landesförderungs-Überblick
passt. Details im Migrationsbericht.
Stand ab 23.10.2026: 3. und letzter Call lief 8. bis 22.10.2026, kein weiterer Call im alten System,
derzeit kein Bundeszuschuss fuer neue Anlagen; Ausblick 2027 Systemfoerderung laut BMWET (geplant, nicht
beschlossen). Kaernten 2. Call 12.10. bis 31.12.2026.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "photovoltaik-foerderung-oesterreich-2026",
    "path": "/photovoltaik-foerderung-oesterreich-2026/",
    "title": "PV-Förderung Österreich: Call beendet, Ausblick 2027 | EBZ",
    "description": ("PV-Förderung Österreich: Der letzte Bundescall 2026 endete am 22. Oktober. Was jetzt gilt, "
                    "Kärnten 3.000 €, Systemförderung 2027 und alle 9 Länder."),
    "eyebrow": "Förderung · Österreich",
    "crumb_label": "PV-Förderung Österreich 2026",
    "h1": "Photovoltaik-Förderung Österreich 2026: Bundescall beendet, was jetzt noch gilt und was 2027 geplant ist",
    "lead": ("Der Nullsteuersatz ist Geschichte, 2026 zahlte der Bund wieder Investitionszuschüsse: 150 Euro "
             "je kWp für Anlagen bis 10 kWp, 150 Euro je kWh Speicher und 10 Prozent Made-in-Europe-Bonus. Der "
             "dritte und letzte Fördercall lief vom 8. bis 22. Oktober 2026, neue Anlagen bekommen derzeit keinen "
             "Bundeszuschuss; ab 2027 ist laut BMWET eine Systemförderung geplant, aber nicht beschlossen. Dieser "
             "Ratgeber erklärt die Sätze und Termine 2026, was jetzt noch beantragbar ist und die Landesförderungen."),
    "chips": [
        "Call 2026: <b>150 €/kWp</b> bis 10 kWp",
        "Call 2026: <b>150 €/kWh</b> Speicher",
        "Letzter Call: <b>8. bis 22. Oktober 2026</b>, beendet",
        "Kärnten: <b>3.000 €</b> mit Speicher bis 31.12.2026",
    ],
    "date_published": "2025-12-15",
    "date_modified": "2026-10-21",
    "hero_img": "foerderung",
    "hero_alt": "Beratungsgespräch bei EBZ Energie zur Photovoltaik-Förderung in Österreich 2026",

    "tldr": [
        "Seit 1. April 2025 gilt für PV-Anlagen wieder 20 Prozent Umsatzsteuer. Als Ausgleich lief 2026 die "
        "EAG-Investitionsförderung mit 60 Millionen Euro Budget, fixiert durch die Verordnungsnovelle vom "
        "16. Jänner 2026. Der letzte Call endete am 22. Oktober 2026, derzeit ist kein Bundeszuschuss beantragbar.",
        "Fördersätze im Call 2026: 150 Euro je kWp bis 10 kWp (Kategorie A), 140 Euro je kWp bis 20 kWp (B), bis "
        "130 Euro (C) und bis 120 Euro (D). Speicher: 150 Euro je kWh bis 50 kWh, nur mit PV-Neuerrichtung oder "
        "-Erweiterung und mindestens 0,5 kWh je kWp.",
        "Drei Fördercalls 2026: 23. April bis 11. Mai, 16. bis 30. Juni und 8. bis 22. Oktober, jeweils mit "
        "Ticketziehung und Antrag vor Inbetriebnahme, dazu 10 Prozent Made-in-Europe-Bonus je Komponente. Im "
        "bisherigen System gibt es keinen weiteren Call.",
        "Ab 2027 ist laut BMWET eine Systemförderung geplant (nicht beschlossen): Speicher mit intelligenter "
        "Steuerung, Antrag nach Installation und Rechnung, Projekte ab 1. November 2026 sollen beantragbar sein. "
        "Die Höhe ist offen.",
        "Rechenbeispiel 10 kWp mit 10 kWh: Im Call 2026 gab es 3.000 Euro vom Bund plus rund 450 Euro Bonus. "
        "Aktuell in Kärnten: 3.000 Euro Landespauschale (2. Call 12. Oktober bis 31. Dezember 2026), der Bund ist "
        "derzeit nicht beantragbar.",
    ],
    "kpis": [
        ("150 €/kWp", "EAG-Bund bis 10 kWp im Call 2026"),
        ("150 €/kWh", "Speicher im Call 2026, bis 50 kWh"),
        ("60 Mio. €", "Bundesbudget 2026"),
        ("22.10.2026", "Ende des letzten Fördercalls 2026"),
    ],

    "sections": [
        ("Was sich 2026 ändert: Zuschuss statt Steuerbefreiung", "aenderungen", f"""
<p>2024 und bis Ende März 2025 war die Anschaffung einer PV-Anlage bis 35 kWp für Private umsatzsteuerfrei.
Dieser Nullsteuersatz ist mit 1. April 2025 ausgelaufen, seither gilt wieder der reguläre Satz von 20 Prozent
auf Komponenten und Montage. Die Photovoltaik-Förderung in Österreich lief 2026 daher wieder über
den klassischen Weg: Sie zahlten den Angebotspreis, der Bund zahlte nach Inbetriebnahme einen
Investitionszuschuss zurück. Der dritte und letzte Call 2026 endete am 22. Oktober 2026; im bisherigen
System gibt es keinen weiteren Call, neue Anlagen bekommen derzeit keinen Bundeszuschuss.</p>
<p>Das Rückgrat ist das Erneuerbaren-Ausbau-Gesetz (EAG). Die Konditionen für das Förderjahr wurden mit
der EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026 am 16. Jänner 2026 kundgemacht, das Budget
betrug 60 Millionen Euro. Abgewickelt wurde die Förderung von der EAG-Abwicklungsstelle bei der OeMAG,
online und mit Ticketsystem. Das Verfahren war bürokratischer als der Nullsteuersatz, die Förderung war
auf systemdienliche Anlagen mit Speicher ausgerichtet. Diese Richtung soll laut BMWET ab 2027 die
geplante Systemförderung fortsetzen (Details weiter unten, nicht beschlossen).</p>
<p>Die wirtschaftliche Betrachtung verschiebt sich damit: Entscheidend ist jetzt die Gesamtrechnung aus
Landesförderung, Eigenverbrauchsquote und Strompreis. Wer den eigenen Strom nutzt, statt ihn für 6 bis 10 Cent
einzuspeisen (OeMAG-Marktpreis 2026), spart 25 bis 35 Cent je Kilowattstunde Netzbezug, ganz ohne Bundeszuschuss.</p>
"""),
        ("EAG-Bundesförderung 2026: Sätze und Kategorien", "eag-saetze", f"""
<p>Im Call 2026 waren die Fördersätze nach Anlagengröße in vier Kategorien gestaffelt. Für private
Dachanlagen waren die Kategorien A und B relevant, Gewerbeanlagen fielen in C und D. Die Sätze sind derzeit
nicht beantragbar, der letzte Call endete am 22. Oktober 2026:</p>
{A.table(
    ["Kategorie", "Anlagengröße", "Fördersatz PV", "Speicher", "Vergabe"],
    [
        ["A", "bis 10 kWp", "150 €/kWp", "150 €/kWh, max. 50 kWh", "First-Come-First-Served, Ticket"],
        ["B", "über 10 bis 20 kWp", "140 €/kWp", "150 €/kWh, max. 50 kWh", "First-Come-First-Served, Ticket"],
        ["C", "über 20 bis 100 kWp", "max. 130 €/kWp", "150 €/kWh, max. 50 kWh", "Bieterverfahren"],
        ["D", "über 100 bis 1.000 kWp", "max. 120 €/kWp", "150 €/kWh, max. 50 kWh", "Bieterverfahren"],
    ],
    hl_cols=(2, 3),
)}
<p>Für den Speicher galten 2026 zwei Bedingungen: Er wurde nur gemeinsam mit einer PV-Neuerrichtung oder
-Erweiterung gefördert, und die Kapazität musste mindestens 0,5 kWh je kWp installierter PV-Leistung
betragen. Ein nachgerüsteter Speicher erhielt keinen EAG-Zuschuss; laut BMWET soll die Nachrüstung von
Speicher und Energiemanagement ab 2027 förderbar werden (geplant, nicht beschlossen). Eigene Programme gibt es
in einigen Bundesländern (siehe {a('/foerderung-fuer-pv-speicher/', 'Förderung für PV-Speicher')}).</p>
<p>Mit der EAG-Novelle 2026 war die Kombination mit Landesförderungen für Anlagen bis 100 kWp
ausdrücklich erlaubt, sofern die beihilferechtlichen Höchstgrenzen eingehalten wurden. Ob das jeweilige
Land zusätzlich zahlt, regelt dessen Richtlinie.</p>
"""),
        ("Made-in-Europe-Bonus: 10 Prozent je Komponente", "made-in-europe", f"""
<p>Im Call 2026 honorierte der Bund europäische Wertschöpfung: Für PV-Module, Wechselrichter und Speicher,
die auf der White List der EAG-Abwicklungsstelle standen, erhöhte sich der jeweilige Zuschuss um 10 Prozent
je Komponente. Für die PV-Anlage waren damit bis zu 20 Prozent Bonus möglich (Module plus Wechselrichter),
für den Speicher weitere 10 Prozent.</p>
<p>Für die Systemförderung ab 2027 ist laut BMWET wieder ein Europa-Bonus geplant, Höhe und Kriterien sind
offen. Der Blick auf die Herkunft der Komponenten lohnt sich daher weiter: Europäische Produkte bringen oft
längere Garantien. EBZ Energie berücksichtigt die Herkunft bereits bei der Angebotslegung.</p>
"""),
        ("Die drei Fördercalls 2026: Termine und Ablauf", "foerdercalls", f"""
<p>Die Fördermittel wurden 2026 nicht durchgehend, sondern in drei Antragsfenstern vergeben. Alle drei
Calls sind abgeschlossen:</p>
{A.table(
    ["Fördercall", "Zeitraum", "Hinweis"],
    [
        ["1. Call", "23. April bis 11. Mai 2026", "größtes Budgetvolumen, beendet"],
        ["2. Call", "16. bis 30. Juni 2026", "für Projekte, die im April noch nicht antragsreif waren, beendet"],
        ["3. Call", "8. bis 22. Oktober 2026", "Ticketziehung ab 8. Oktober 17:00 Uhr, letzter Call im bisherigen System, beendet"],
    ],
    hl_cols=(1,),
)}
<p><b>Stand ab 23. Oktober 2026:</b> Der dritte Call lief vom 8. bis 22. Oktober 2026 und war der letzte im
bisherigen System. Neue Anlagen bekommen derzeit keinen Bundeszuschuss. Ab 2027 ist laut Eckpunkten des
BMWET eine Systemförderung geplant, aber nicht beschlossen: Antrag nach Installation und Rechnung statt
Fördercall und Ticketziehung, gefördert werden sollen Speicher mit intelligenter Steuerung, auch als
Nachrüstung; Projekte mit intelligentem Speicher, die ab 1. November 2026 in Betrieb gehen, sollen 2027
beantragbar sein. Höhe und Technikkriterien sind noch offen.</p>
<p>Wer jetzt plant, baut deshalb sinnvoll mit Speicher und Energiemanagement: Das wahrt die Chance auf die
Systemförderung 2027, und Kärnten zahlt die 3.000 Euro Landespauschale nur mit Speicher.</p>
<p>So lief der Antrag im Call 2026: In den Kategorien A und B galt First-Come-First-Served. Beim Start des
Calls zogen Antragsteller online ein Ticket, die Reihung erfolgte nach Eingang. War das Budget eines Calls
ausgeschöpft, wurden auch fristgerechte Anträge abgelehnt.</p>
{A.steps([
    ("Angebot und Zählpunkt vorbereiten",
     "Nötig waren ein Angebot des Fachbetriebs und die Zählpunktnummer aus dem Netzzutrittsantrag beim "
     "Netzbetreiber, beides vor dem Call-Start."),
    ("Ticket ziehen und Antrag stellen",
     "Am Starttag des Calls (23. April, 16. Juni oder 8. Oktober 2026) online bei der EAG-Abwicklungsstelle "
     "registrieren und den Antrag mit Anlagendaten, Speicherkapazität und Komponentenliste einreichen."),
    ("Anlage errichten",
     "Erst nach der Antragstellung durfte die Anlage in Betrieb gehen. Die Montage konnte vorbereitet werden, "
     "die Inbetriebnahme musste nach dem Antrag liegen."),
    ("Endabrechnung einreichen",
     "Nach Inbetriebnahme folgten Rechnungen, Fertigstellungsmeldung des Netzbetreibers und die "
     "Nachweise für den Made-in-Europe-Bonus. Danach wurde der Zuschuss ausbezahlt."),
])}
{A.box_dark("Reihenfolge: 2026 und ab 2027 verschieden",
    "Im Call 2026 musste der EAG-Antrag <b>vor der Inbetriebnahme</b> gestellt werden. Für die geplante "
    "Systemförderung 2027 soll der Antrag laut BMWET erst <b>nach</b> Installation und Rechnung kommen (nicht "
    "beschlossen). Bei den Landesförderungen wird schon jetzt nach Fertigstellung beantragt, in Kärnten zum "
    "Beispiel. EBZ Energie stimmt Montagetermin und Anträge so ab, dass die Fristen passen.")}
"""),
        ("Rechenbeispiel: 10 kWp mit 10 kWh Speicher", "rechenbeispiel", f"""
<p>Für eine typische Einfamilienhaus-Anlage mit 10 kWp und 10 kWh Speicher, Richtpreis rund 15.000 bis
22.000 Euro vor Förderung, ergab sich im Call 2026 folgende Förderung. Die Bundesposten sind derzeit nicht
beantragbar, die Kärntner Pauschale schon:</p>
{A.table(
    ["Förderung", "Rechnung", "Betrag*"],
    [
        ["EAG-Bund, PV-Anlage (Kategorie A), im Call 2026", "10 kWp × 150 €", "1.500 €"],
        ["EAG-Bund, Speicher, im Call 2026", "10 kWh × 150 €", "1.500 €"],
        ["Made-in-Europe-Bonus, im Call 2026", "10 % auf Modul-, Wechselrichter- und Speicherzuschuss", "rund 450 €"],
        ["Zwischensumme Bund im Call 2026", "", "rund 3.450 €"],
        ["Landespauschale Kärnten", "PV ab 5 kWp mit Speicher ab 5 kWh, 2. Landes-Call 12. Oktober bis 31. Dezember 2026", "3.000 €"],
        ["Summe in Kärnten im Call 2026", "", "rund 6.450 €"],
        ["Aktuell in Kärnten (Bund derzeit nicht beantragbar)", "nur Landespauschale", "3.000 €"],
    ],
    hl_cols=(2,),
)}
<p>Manche Gemeinden zahlen dazu einen eigenen Zuschuss. Bei 18.500 Euro Anlagenpreis blieben in
Kärnten im Call 2026 rund 12.000 Euro Investition, mit der aktuellen Landespauschale allein sind es rund
15.500 Euro. Mit hohem Eigenverbrauch amortisiert sich die Anlage in
EBZ-Projekten typischerweise in 4 bis 6 Jahren, die vollständige Rechnung finden Sie im Ratgeber
{a('/kosten-einer-solaranlage/', 'Kosten einer Solaranlage')}.</p>
<p><small>*Beispielkonditionen nach EAG-Investitionszuschüsseverordnung 2026 (Call 2026, beendet) und
Kärntner Landesrichtlinie, Stand Oktober 2026. Der Bonus setzte Komponenten von der White List voraus.</small></p>
{A.cta("Jetzt mit Speicher planen",
       "Wir reichen die Kärntner Landespauschale ein und planen Speicher und Energiemanagement so, dass Ihre "
       "Anlage für die geplante Systemförderung 2027 in Frage kommt. Sie müssen sich um nichts kümmern.",
       secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
        ("Föderalismus: So unterschiedlich fördern die Bundesländer", "bundeslaender", f"""
<p>Während der Bund 2026 überall gleich förderte, setzen die neun Länder eigene Akzente, von einer
Pauschale mit Speicherpflicht über Sanierungsprogramme bis zur kompletten Einstellung. Der Überblick mit
Link zum jeweiligen Detail-Ratgeber:</p>
{A.table(
    ["Bundesland", "Landesförderung 2026 (Kurzfassung)", "Mit Bund kombinierbar"],
    [
        [a('/photovoltaik-foerderung-kaernten/', 'Kärnten'), "3.000 € Pauschale für PV ab 5 kWp mit Speicher ab 5 kWh, 2. Landes-Call 12. Oktober bis 31. Dezember 2026, Antrag nach Fertigstellung; Nachrüstung 1.000 €", "ja"],
        [a('/foerderung-photovoltaik-steiermark/', 'Steiermark'), "derzeit keine PV-Landesförderung offen: Sanierungsbonus (bis 15 %, Fenster 1. April bis 15. Mai 2026) beendet, Ökofonds ohne PV-Ausschreibung", "entfällt"],
        [a('/photovoltaik-foerderung-wien/', 'Wien'), "Stadtförderung ab 1. Mai 2026, Fokus auf Gründächer, Fassaden und Mehrparteienhäuser", "nein"],
        [a('/photovoltaik-foerderung-niederoesterreich/', 'Niederösterreich'), "über die Wohnbauförderung, Punktesystem", "ja"],
        [a('/photovoltaik-foerderung-oberoesterreich/', 'Oberösterreich'), "Speicher-Nachrüstung 150 €/kWh bis 2.250 € für Bestandsanlagen vor 1. Jänner 2026", "nein beim Speicher"],
        [a('/photovoltaik-foerderung-salzburg/', 'Salzburg'), "private PV-Landesförderung mit Jahresende 2025 eingestellt, 2026 nur EAG", "entfällt"],
        [a('/photovoltaik-foerderung-tirol/', 'Tirol'), "bis 125 €/kWp über die Wohnhaussanierung, Speicher 100 €/kWh bis 1.000 €", "ja"],
        [a('/photovoltaik-foerderung-vorarlberg/', 'Vorarlberg'), "Landesprogramm für PV und Speicher", "ja"],
        [a('/photovoltaik-foerderung-burgenland/', 'Burgenland'), "Speicher 100 €/kWh bis 2.000 €, Bund vor Land", "nur wenn EAG nicht möglich"],
    ],
)}
<p>Die Spalte zur Kombination beschreibt die Regeln für den Call 2026; derzeit ist kein Bundeszuschuss
beantragbar. Die Kombination war nicht überall erlaubt: Wien schloss sie aus, Oberösterreich beim Speicher, im
Burgenland galt Bund vor Land. Den vollständigen Vergleich aller neun Regelwerke finden Sie im Ratgeber
{a('/photovoltaik-landesfoerderungen/', 'Photovoltaik-Landesförderungen: alle 9 Bundesländer')}.</p>
<p><small>Stand: Oktober 2026. Maßgeblich sind die jeweils gültigen Landesrichtlinien.</small></p>
"""),
        ("Wirtschaftlichkeit 2026: Förderung plus Eigenverbrauch", "wirtschaftlichkeit", f"""
<p>Lohnt sich Photovoltaik, wenn die Einspeisevergütung sinkt, die Umsatzsteuer wieder gilt und der
Bundeszuschuss derzeit fehlt? Ja, aber die Rechnung hat sich verschoben. Förderungen dämpfen die
Anfangskosten, der eigentliche Hebel ist der Eigenverbrauch: Netzstrom kostet 25 bis 35 Cent je
Kilowattstunde inklusive Netzgebühren und Steuern, die Gestehungskosten des eigenen Solarstroms lagen im
Call 2026 dank Förderung oft nur bei 6 bis 8 Cent. Der OeMAG-Marktpreis
für eingespeisten Strom lag im Juli 2026 bei 6,146 Cent und im September 2026 bei 10,168 Cent, mehr dazu im Ratgeber
{a('/einspeisetarif-fuer-photovoltaik/', 'Einspeisetarif für Photovoltaik')}.</p>
<p>Genau deshalb förderte der Bund den Speicher 2026 mit 150 Euro je kWh, und auch die für 2027 geplante
Systemförderung setzt laut BMWET auf Speicher mit intelligenter Steuerung: Er hebt den Eigenverbrauch von
rund 30 auf 60 bis 80 Prozent und senkt die Stromrechnung um bis zu 85 Prozent. Dazu kommt die
Einkommensteuerbefreiung für Einspeiseerlöse bis 12.500 kWh pro Jahr bei Anlagen bis 35 kWp. Wer heute
investiert, friert seine Stromkosten für die nächsten 25 Jahre auf einem niedrigen Niveau ein und steigert
den Wert der Immobilie.</p>
{A.cta("Förderung und Anlage aus einer Hand",
       "Wir prüfen Bundes-, Landes- und Gemeindeförderung für Ihren Standort, wählen förderfähige Komponenten "
       "und halten alle Fristen ein.",
       primary=("kontakt", "Kostenlose Förderberatung"), secondary=("finanzierung", "Finanzierung ab 147 €/Monat"))}
"""),
        ("Fazit: Fristen kennen, Reihenfolge einhalten", "fazit", f"""
<p>Die Photovoltaik-Förderung in Österreich war 2026 mit 150 Euro je kWp, 150 Euro je kWh Speicher und dem
Made-in-Europe-Bonus solide ausgestattet. Der letzte Call endete am 22. Oktober 2026, neue Anlagen bekommen
derzeit keinen Bundeszuschuss. Beantragbar bleibt in Kärnten die höchste Landespauschale Österreichs mit
3.000 Euro (2. Landes-Call bis 31. Dezember 2026, nur mit Speicher). Ab 2027 soll sich der Ablauf laut BMWET
drehen: Antrag nach der Installation, Fokus auf Speicher mit intelligenter Steuerung (geplant, nicht
beschlossen, Höhe offen). Wer jetzt plant, baut mit Speicher und Energiemanagement und senkt seine
Stromkosten dauerhaft.</p>
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Förderung und Photovoltaik: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und montiert Photovoltaikanlagen mit Speicher in Kärnten und der "
                 "Steiermark, mit zertifizierten Fachkräften und über 300 "
                 "dokumentierten Projekten. Die Förderabwicklung ist Teil des Pakets: Netzzutritt, Landes- und "
                 "Gemeindeanträge, die Endabrechnung und die Vorbereitung auf die geplante Systemförderung 2027."),
        "grid": [
            ("Fristen im Griff", "Kärntner Landes-Call bis 31. Dezember 2026, Inbetriebnahme und Antrag richtig abgestimmt."),
            ("Zukunftsfähige Technik", "Speicher mit Energiemanagement, europäische Komponenten, Blick auf die Kriterien 2027."),
            ("Land und Gemeinde", "Kärntner Pauschale, Stand der steirischen Programme und Gemeindeförderung geprüft."),
            ("Endabrechnung inklusive", "Rechnungen, Fertigstellungsmeldung und Nachweise reichen wir für Sie ein."),
        ],
    },

    "faq": [
        ("Wann liefen die Fördercalls 2026?",
         "Der erste und volumenstärkste EAG-Call lief vom 23. April bis 11. Mai 2026, der zweite vom 16. bis "
         "30. Juni, der dritte und letzte vom 8. bis 22. Oktober 2026 (Ticketziehung ab 8. Oktober, 17:00 Uhr). "
         "Im bisherigen System gibt es keinen weiteren Call, neue Anlagen bekommen derzeit keinen Bundeszuschuss."),
        ("Wie geht es mit der PV-Förderung 2027 weiter?",
         "Laut Eckpunkten des BMWET (Oktober 2026) ist für 2027 eine Systemförderung geplant, beschlossen ist sie "
         "nicht: Der Antrag soll nach Installation und Rechnung gestellt werden, nicht mehr im Fördercall. "
         "Gefördert werden sollen Speicher mit intelligenter Steuerung, auch als Nachrüstung, ein Europa-Bonus ist "
         "geplant. Projekte mit intelligentem Speicher, die ab 1. November 2026 in Betrieb gehen, sollen 2027 "
         "beantragbar sein. Höhe und Kriterien sind noch offen."),
        ("Gilt die 0 Prozent Umsatzsteuer für Photovoltaik noch?",
         "Nein. Der Nullsteuersatz für PV-Anlagen bis 35 kWp ist mit 1. April 2025 ausgelaufen, seither gilt "
         "wieder 20 Prozent auf Komponenten und Montage. Als Ausgleich wurde 2026 die EAG-Investitionsförderung "
         "wieder voll aktiviert: ein Zuschuss nach Inbetriebnahme statt einer Steuerbefreiung auf der Rechnung. "
         "Der letzte Call dafür endete am 22. Oktober 2026."),
        ("Wie hoch war die Förderung für eine private PV-Anlage 2026?",
         "Im Call 2026 gab es 150 Euro je kWp bis 10 kWp (Kategorie A) und 140 Euro je kWp bis 20 kWp (Kategorie B), "
         "also 1.500 bis 2.800 Euro, dazu 150 Euro je kWh Speicher bis 50 kWh und 10 Prozent Made-in-Europe-Bonus "
         "je Komponente. Für 10 kWp mit 10 kWh ergab das rund 3.450 Euro vom Bund. Derzeit ist kein Bundeszuschuss "
         "beantragbar, in Kärnten gibt es 3.000 Euro Landespauschale."),
        ("Gibt es aktuell eine Förderung für einen Stromspeicher?",
         "Vom Bund derzeit nicht: Die 150 Euro je kWh galten im Call 2026, der am 22. Oktober 2026 endete. Laut "
         "BMWET ist ab 2027 eine Systemförderung für Speicher mit intelligenter Steuerung geplant, auch als "
         "Nachrüstung (nicht beschlossen, Höhe offen). In Kärnten gibt es 3.000 Euro Landespauschale für PV mit "
         "Speicher ab 5 kWh bzw. 1.000 Euro für die Nachrüstung, Einreichung bis 31. Dezember 2026."),
        ("Kann ich die Bundesförderung mit der Landesförderung kombinieren?",
         "Im Call 2026 ging das in den meisten Bundesländern, etwa in Kärnten, Niederösterreich, Tirol und "
         "Vorarlberg; Wien schloss die Kombination aus, Oberösterreich beim Speicher, im Burgenland galt Bund vor "
         "Land. Derzeit ist kein Bundeszuschuss beantragbar, in der Steiermark ist auch keine PV-Landesförderung "
         "offen. Wie die geplante Systemförderung 2027 mit Landesförderungen zusammenspielt, ist offen."),
        ("Was bedeutete der Made-in-Europe-Bonus?",
         "Im Call 2026 erhöhte sich für Module, Wechselrichter und Speicher von der White List der "
         "EAG-Abwicklungsstelle der jeweilige Zuschuss um 10 Prozent. Für die PV-Anlage waren so bis zu 20 Prozent "
         "Bonus möglich, für den Speicher weitere 10 Prozent, bei 10 kWp mit 10 kWh rund 450 Euro. Für 2027 ist "
         "laut BMWET wieder ein Europa-Bonus geplant, Höhe offen."),
        ("Was passiert mit Projekten, die im Call 2026 nicht zum Zug kamen?",
         "Im bisherigen System gibt es keinen weiteren Call, ein neuer Antrag beim Bund ist derzeit nicht möglich. "
         "Projekte mit intelligentem Speicher, die ab 1. November 2026 in Betrieb gehen bzw. abgerechnet werden, "
         "sollen laut BMWET 2027 in der geplanten Systemförderung beantragbar sein (nicht beschlossen). In Kärnten "
         "bleibt die Landespauschale bis 31. Dezember 2026 beantragbar."),
        ("Muss der Antrag vor der Inbetriebnahme gestellt werden?",
         "Im Call 2026 ja: Der EAG-Antrag musste vor der Inbetriebnahme eingereicht werden, sonst entfiel die "
         "Bundesförderung. Für die geplante Systemförderung 2027 soll der Antrag laut BMWET nach Installation und "
         "Rechnung kommen. Bei Landesförderungen wie in Kärnten wird nach Fertigstellung beantragt."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team hat über 300 PV-Projekte in "
                    "6 Bundesländern umgesetzt und wickelt Bundes-, Landes- und Gemeindeförderungen für Kunden in "
                    "Kärnten und der Steiermark ab. Die Werte in diesem Ratgeber werden nach den Veröffentlichungen "
                    "der EAG-Abwicklungsstelle aktualisiert. Keine Rechts- oder Steuerberatung, maßgeblich sind die "
                    "offiziellen Förderrichtlinien."),
    "sources": [
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("EAG-Abwicklungsstelle (OeMAG)", "https://www.eag-abwicklungsstelle.at/"),
        ("Förderportal des Landes Kärnten", "https://www.ktn.gv.at/"),
        ("Förderportal des Landes Steiermark", "https://www.steiermark.at/"),
    ],
    "related": [
        ("/photovoltaik-landesfoerderungen/", "PV-Landesförderungen: alle 9 Bundesländer"),
        ("/photovoltaik-foerderung-kaernten/", "Photovoltaik-Förderung Kärnten 2026"),
        ("/foerderung-photovoltaik-steiermark/", "Photovoltaik-Förderung Steiermark 2026"),
        ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage 2026"),
    ],
    "cta": {
        "h3": "Förderung nicht verschenken",
        "text": "Bundescall 2026 beendet, Kärnten zahlt bis 31. Dezember 2026: Wir reichen den Landesantrag ein und planen mit Speicher für die Systemförderung 2027.",
        "primary": ("kontakt", "Kostenlose Förderberatung"),
    },
    "final_h2": "Ihre Förderung, richtig beantragt",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
