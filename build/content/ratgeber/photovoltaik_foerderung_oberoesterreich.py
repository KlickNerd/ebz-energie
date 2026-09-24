"""Ratgeber: Photovoltaik-Förderung Oberösterreich 2026.

Migriert von ebz-photovoltaik.at/photovoltaik-foerderung-oberoesterreich/ (Stand Juni 2026),
inhaltlich bereinigt und auf die Ratgeber-Vorlage umgestellt.
Zahlen: EAG-Investitionszuschüsseverordnung 2026, OÖ Sonderförderprogramm Speicher-Nachrüstung (ab 1. März 2026).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "photovoltaik-foerderung-oberoesterreich",
    "path": "/photovoltaik-foerderung-oberoesterreich/",
    "title": "PV-Förderung Oberösterreich 2026: EAG + Speicher | EBZ",
    "description": ("PV-Förderung Oberösterreich 2026: keine Landespauschale, EAG-Bund 150 €/kWp, "
                    "Speicher-Nachrüstung 150 €/kWh bis 2.250 €. Kombinierbarkeit und Fristen."),
    "eyebrow": "Förderung · Oberösterreich",
    "crumb_label": "PV-Förderung Oberösterreich 2026",
    "h1": "Photovoltaik-Förderung Oberösterreich 2026: EAG-Zuschuss und bis zu 2.250 Euro für die Speicher-Nachrüstung",
    "lead": ("Oberösterreich zahlt 2026 keine PV-Pauschale für Privathaushalte. Neue Anlagen laufen über die "
             "EAG-Bundesförderung, für Bestandsanlagen gibt es seit 1. März 2026 eine Speicher-Nachrüstung mit "
             "150 Euro je kWh. Beide Speicherförderungen schließen sich gegenseitig aus."),
    "chips": [
        "EAG-Bund: <b>150 €/kWp</b> bis 10 kWp",
        "OÖ-Speicher: <b>150 €/kWh</b>, max. 2.250 €",
        "Nur Bestand: PV in Betrieb <b>vor 1.1.2026</b>",
        "<b>Nicht</b> mit EAG-Speicher kombinierbar",
    ],
    "date_published": "2026-05-15",
    "date_modified": "2026-09-24",
    "hero_img": "gewerbe_dach",
    "hero_alt": "Photovoltaikanlage auf einem Gewerbedach in Oberösterreich, Ost-West-Ausrichtung auf Trapezblech",

    "tldr": [
        "Oberösterreich bietet 2026 keine direkte PV-Förderung pro kWp für Privathaushalte. Neuanlagen werden über "
        "den EAG-Investitionszuschuss des Bundes gefördert: 150 Euro je kWp bis 10 kWp, 150 Euro je kWh Speicher, "
        "plus Made-in-Europe-Bonus.",
        "Die Landesförderung „Nachrüstung von systemdienlichen Solarstromspeichern“ gilt seit 1. März 2026: "
        "150 Euro je kWh Nennkapazität, maximal 15 kWh, maximal 40 Prozent der Bruttokosten, also bis zu "
        "2.250 Euro.",
        "Voraussetzung für die Speicherförderung: Die PV-Anlage ist vor dem 1. Jänner 2026 mit Netzzugangsvertrag "
        "in Betrieb gegangen. Antragsberechtigt sind Privatpersonen, Gemeinden und Vereine, keine Betriebe.",
        "Knackpunkt: Die OÖ-Speicherförderung ist nicht mit der EAG-Speicherförderung kombinierbar. Neuanlage "
        "gleich EAG, Bestandsanlage gleich Land.",
        "Für eine Neuanlage mit 10 kWp und 10 kWh sind rund 3.000 bis 4.500 Euro Gesamtförderung realistisch, "
        "primär aus der EAG-Förderung, ergänzt um Made-in-Europe-Bonus und Gemeindezuschuss.",
    ],
    "kpis": [
        ("150 €/kWp", "EAG-Bundesförderung bis 10 kWp"),
        ("150 €/kWh", "OÖ-Speicher-Nachrüstung, max. 15 kWh"),
        ("2.250 €", "maximaler Landeszuschuss Speicher"),
        ("01.03.2026", "Start der OÖ-Speicherförderung"),
    ],

    "sections": [
        ("Die Photovoltaik-Förderung Oberösterreich 2026 im Überblick", "ueberblick", f"""
<p>Oberösterreich verfolgt mit der PV-Strategie 2030 ambitionierte Ausbauziele und arbeitet an
Beschleunigungszonen, die Genehmigungen ab 2026 vereinfachen. Bei der direkten Förderung setzt das Land
aber anders an als Kärnten oder Tirol: Es gibt keine Landespauschale pro Kilowattpeak für
Privathaushalte. Die Förderlandschaft funktioniert zweigleisig.</p>
{A.table(
    ["Förderschiene", "Für wen", "Förderhöhe 2026", "Hinweis"],
    [
        ["EAG-Investitionszuschuss (Bund)", "Neue PV-Anlage, mit oder ohne Speicher", "150 €/kWp (Kat. A) + 150 €/kWh Speicher + Made-in-Europe-Bonus", "Antrag vor Inbetriebnahme, 3 Calls 2026"],
        ["OÖ-Speicher-Nachrüstung (Land)", "Bestandsanlage, in Betrieb vor 1.1.2026", "150 €/kWh Nennkapazität, max. 15 kWh, max. 40 % der Bruttokosten, bis 2.250 €", "seit 1. März 2026, nicht mit EAG-Speicher kombinierbar"],
        ["OÖ Dächer-Prüfung und -Ertüchtigung (Land)", "Dächer, die für PV verstärkt werden müssen", "Zuschuss für Statik und bauliche Maßnahmen", "zusätzlich zur EAG möglich"],
        ["Gemeindeförderung", "je nach Wohnsitzgemeinde", "Fixzuschuss, Speicherbonus oder Prozentanteil", "laufend, gemeindeabhängig"],
    ],
    hl_cols=(2,),
)}
<p>Wer eine Bestandsanlage besitzt und einen Speicher nachrüsten will, bekommt in Oberösterreich einen der
höchsten Speicherzuschüsse Österreichs. Wer neu baut, stützt sich auf die EAG-Bundesförderung. Dazu
kommen die Förderung für Dächer-Prüfung und -Ertüchtigung sowie die PV-Beschleunigungs- und
Ausschlusszonen, die bis 21. Februar 2026 beschlossen werden mussten.</p>
<p><small>Stand: Juni 2026. Maßgeblich sind die jeweils gültigen Richtlinien der EAG-Abwicklungsstelle und des
Landes Oberösterreich.</small></p>
"""),
        ("EAG-Bundesförderung 2026: der Hauptzuschuss für Neuanlagen", "eag", f"""
<p>Ohne Landespauschale ist der EAG-Investitionszuschuss der zentrale Förderhebel für oberösterreichische
Hausbesitzer. Mit der EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026, kundgemacht am
16. Jänner 2026, sind die Konditionen fixiert. Insgesamt stehen 60 Millionen Euro Bundesmittel bereit.</p>
{A.table(
    ["Kategorie", "Anlagengröße", "Fördersatz PV", "Vergabe"],
    [
        ["A", "bis 10 kWp", "150 €/kWp", "First-Come-First-Served mit Ticket"],
        ["B", "über 10 bis 20 kWp", "140 €/kWp", "First-Come-First-Served mit Ticket"],
        ["C", "über 20 bis 100 kWp", "max. 130 €/kWp", "Bieterverfahren"],
        ["D", "über 100 bis 1.000 kWp", "max. 120 €/kWp", "Bieterverfahren"],
    ],
    hl_cols=(2,),
)}
<p>Stromspeicher fördert der Bund mit 150 Euro je kWh bis maximal 50 kWh, nur in Kombination mit einer
PV-Neuerrichtung oder -Erweiterung. Der Made-in-Europe-Bonus bringt jeweils 10 Prozent pro Komponente
(Module, Wechselrichter, Speicher) von der White List. Für Anlagen auf landwirtschaftlich genutzten
Flächen oder Grünland gilt ein Abschlag von 25 Prozent auf den Fördersatz, ausgenommen Agri-PV.</p>
<p>Die drei EAG-Fördercalls 2026 laufen vom 23. April bis 11. Mai, vom 16. bis 30. Juni sowie ab
8. Oktober. Der Antrag muss vor Inbetriebnahme der Anlage online bei der EAG-Abwicklungsstelle gestellt
werden. Mehr dazu im Ratgeber {a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}.</p>
"""),
        ("Speicher-Nachrüstung Oberösterreich 2026 im Detail", "speicher", f"""
<p>Das Herzstück der oberösterreichischen Landesförderung ist das Sonderförderprogramm „Nachrüstung von
systemdienlichen Solarstromspeichern“. Die Richtlinie ist mit 1. März 2026 in Kraft getreten und richtet
sich an Hausbesitzer, die zu einer bestehenden PV-Anlage erstmals einen Stromspeicher nachrüsten.</p>
{A.table(
    ["Kriterium", "Regelung Oberösterreich 2026"],
    [
        ["Förderhöhe", "150 € je kWh Nennkapazität"],
        ["Obergrenzen", "max. 15 kWh gefördert (größere Speicher erlaubt), max. 40 % der förderungsfähigen Bruttoinvestitionskosten, bis 2.250 €"],
        ["Dimensionierung", "Richtwert rund 1,5 kWh je kWp PV-Leistung, mindestens 0,5 kWh je kWp"],
        ["Antragsberechtigt", "Privatpersonen, Gemeinden, Vereine nach Vereinsgesetz; keine Betriebe"],
        ["Bestandsanlage", "PV-Inbetriebnahme vor dem 1. Jänner 2026, Nachweis über Netzzugangsvertrag (Netzzusage reicht nicht)"],
        ["Betrieb", "netzdienlich, Be- und Entladen variabel einstellbar, mindestens 5 Jahre zweckentsprechend"],
        ["Ausschlüsse", "nur ein Speicher je Anlage und Standort, Erweiterungen bestehender Speicher nicht förderfähig"],
        ["Antrag", "online beim Amt der OÖ Landesregierung nach Umsetzung der Maßnahme"],
    ],
    hl_cols=(1,),
)}
<p>Ein Prüfprotokoll nach OVE E 8101 (Elektro-Befund) durch eine befugte Elektrofachkraft ist
erforderlich, die Errichtung muss durch ein gewerblich befugtes Unternehmen erfolgen. Welche Speicher
sich netzdienlich steuern lassen, erklärt die Leistungsseite {a('batteriespeicher', 'Batteriespeicher')}.</p>
"""),
        ("Der Knackpunkt: keine Kombination mit der EAG-Speicherförderung", "knackpunkt", f"""
<p>Die oberösterreichische Speicher-Nachrüstungsförderung ist nicht mit der EAG-Speicherförderung des
Bundes kombinierbar. Auch andere Bundesförderungen für denselben Speicher sind ausgeschlossen. Sie
müssen sich für eine Schiene entscheiden, in der Praxis ergibt sich die Wahl aber von selbst:</p>
{A.table(
    ["Ihre Situation", "Richtige Förderschiene"],
    [
        ["Neue PV-Anlage 2026 mit Speicher", "EAG-Bundesförderung für PV und Speicher (150 €/kWp + 150 €/kWh)"],
        ["Bestandsanlage (in Betrieb vor 1.1.2026), Speicher nachrüsten", "OÖ-Speicherförderung (150 €/kWh, bis 2.250 €), EAG greift bei reiner Nachrüstung nicht"],
        ["Dach muss statisch ertüchtigt werden", "OÖ Dächer-Förderung, zusätzlich zur EAG"],
    ],
    hl_cols=(1,),
)}
{A.box("Wer 2026 neu baut, kommt für die OÖ-Speicherförderung nicht infrage, weil die Anlage erst 2026 in "
       "Betrieb geht. Wer eine Bestandsanlage hat, kann die EAG-Speicherförderung nicht nutzen, weil sie eine "
       "PV-Neuerrichtung oder -Erweiterung voraussetzt. Die beiden Programme ergänzen sich also, sie "
       "überschneiden sich nicht.")}
{A.cta("Speicher nachrüsten oder neu bauen? Wir rechnen beide Varianten",
       "EBZ Energie prüft, welche Förderschiene für Ihre Anlage greift, und dimensioniert den Speicher "
       "förderfähig mit rund 1,5 kWh je kWp.",
       secondary=("batteriespeicher", "Mehr zum Batteriespeicher"))}
"""),
        ("Antragstellung: Reihenfolge für Neuanlage und Nachrüstung", "antrag", f"""
<p>Die beiden Schienen haben unterschiedliche Zeitpunkte: EAG vor Inbetriebnahme, OÖ-Speicherförderung
nach Umsetzung. So läuft es je nach Fall ab:</p>
{A.steps([
    ("Neuanlage: EAG-Ticket im Call ziehen",
     "Am ersten Tag eines EAG-Calls (23. April, 16. Juni oder 8. Oktober 2026) Ticket ziehen und den Antrag "
     "mit Genehmigungen, Zählpunkt und Angebot einreichen. Erst danach errichten und in Betrieb nehmen."),
    ("Neuanlage: Endabrechnung beim Bund",
     "Nach Inbetriebnahme Rechnungen, Zahlungsbelege und Fotos innerhalb der Frist bei der "
     "EAG-Abwicklungsstelle einreichen, dann wird der Zuschuss ausbezahlt."),
    ("Nachrüstung: Speicher errichten lassen",
     "Speicher durch ein gewerblich befugtes Unternehmen installieren, netzdienliche Steuerung einrichten "
     "und Prüfprotokoll nach OVE E 8101 ausstellen lassen."),
    ("Nachrüstung: Landesantrag nach Umsetzung",
     "Online beim Amt der OÖ Landesregierung einreichen: Netzzugangsvertrag der PV-Anlage (Inbetriebnahme vor "
     "1. Jänner 2026), Rechnung, Zahlungsnachweis und Prüfprotokoll."),
    ("Gemeindeförderung prüfen",
     "In beiden Fällen bei der Wohnsitzgemeinde nachfragen, viele oberösterreichische Gemeinden zahlen "
     "zusätzlich einen Fixbetrag oder Speicherbonus."),
])}
<h3>Voraussetzungen im Überblick</h3>
<ul>
  <li><b>EAG-Bundesförderung:</b> netzgekoppelte Anlage, Antrag vor Inbetriebnahme, alle Genehmigungen oder
  Anzeigen in erster Instanz liegen bei Antragstellung vor, Stand der Technik, Freiflächenanlagen
  rückstandslos rückbaubar mit mindestens 80 cm Abstand der Modulunterkante zum Boden.</li>
  <li><b>OÖ-Speicherförderung:</b> PV-Inbetriebnahme vor dem 1. Jänner 2026 mit Netzzugangsvertrag, systemdienlicher
  Betrieb mit variabler Be- und Entladesteuerung, Prüfprotokoll nach OVE E 8101, Errichtung durch ein
  gewerblich befugtes Unternehmen.</li>
</ul>
"""),
        ("Dächer-Förderung, Beschleunigungszonen und Gemeinden", "ergaenzungen", f"""
<h3>Förderung für Dächer-Prüfung und -Ertüchtigung</h3>
<p>Das Land Oberösterreich fördert bauliche Maßnahmen zur Erhöhung der Dachtragfähigkeit sowie statische
Berechnungen, die für eine PV-Errichtung nötig sind. Die EAG-Bundesförderung deckt diese Vorbereitung
nicht ab, beide Töpfe lassen sich deshalb parallel nutzen. Gerade bei älteren Häusern oder besonderen
Dachkonstruktionen senkt das die Einstiegshürde.</p>
<h3>PV-Beschleunigungs- und Ausschlusszonen</h3>
<p>Auf Basis der EU-Richtlinie RED III, die bis 21. Februar 2026 umzusetzen war, bereitet Oberösterreich
eine Verordnung für PV-Beschleunigungs- und Ausschlusszonen vor. Die öffentliche Auflage des
Planungsberichts zur Strategischen Umweltprüfung lief von 16. Oktober bis 11. Dezember 2025. In
ausgewiesenen Beschleunigungsgebieten gelten PV-Anlagen und Batteriespeicher als widmungsneutrale
Bauwerke, das Widmungserfordernis entfällt. Für größere Anlagen kann das die Genehmigung deutlich
verkürzen, sofern der Standort in einem solchen Gebiet liegt.</p>
<h3>Gemeindeförderungen</h3>
<p>Viele oberösterreichische Gemeinden bieten eigene PV-Programme: pauschale Fixzuschüsse, Speicherboni
oder prozentuale Beteiligungen, teils mit Schwerpunkt auf E-Mobilität und Wallboxen. Weil sich diese
Programme jährlich ändern, lohnt sich ein Anruf bei der Wohnsitzgemeinde. Der OÖ Energiesparverband
berät kostenlos zu allen Förderfragen und kennt die regionalen Programme.</p>
"""),
        ("Photovoltaik und Wärmepumpe: die Kombination mit dem größten Hebel", "waermepumpe", f"""
<p>Wer die Energiekosten dauerhaft senken will, kombiniert die PV-Anlage mit einer
{a('waermepumpe', 'Wärmepumpe')}. Die PV-Anlage liefert tagsüber Sonnenstrom, die Wärmepumpe deckt
Heizung und Warmwasser damit. Nach Erfahrungswerten von EBZ Energie sind so bis zu 85 Prozent Ersparnis
bei den Energiekosten möglich.</p>
<p>Für die Wärmepumpe gibt es eigene Förderschienen wie die Sanierungsoffensive des Bundes oder „Sauber
Heizen für Alle“. Das Land Oberösterreich fördert zusätzlich Maßnahmen zur Verbesserung des Wärmeschutzes
betrieblich genutzter Gebäude. Ein {a('ems', 'Energiemanagementsystem')}, das Speicher und Wärmepumpe
netzdienlich steuert, erfüllt gleichzeitig die Systemdienlichkeits-Anforderung der OÖ-Speicherförderung
und wird seit Juni 2026 vom Klima- und Energiefonds gefördert (siehe {a('/ems-foerderung/', 'EMS-Förderung 2026')}).</p>
"""),
        ("Fazit: Mit der richtigen Schiene zur maximalen Förderung", "fazit", f"""
<p>Die Photovoltaik-Förderung in Oberösterreich 2026 ist anders aufgebaut als in den meisten anderen
Bundesländern (Vergleich: {a('/photovoltaik-landesfoerderungen/', 'PV-Landesförderungen aller neun Bundesländer')}).
Der Schlüssel ist die Wahl der passenden Schiene: EAG-Bundesförderung für Neuanlagen,
OÖ-Speicher-Nachrüstung für Bestandsanlagen. Beide zugleich gehen nicht.</p>
{A.table(
    ["Beispiel Neuanlage 10 kWp + 10 kWh*", "Betrag"],
    [
        ["EAG-Bund, PV-Anlage (10 × 150 €)", "1.500 €"],
        ["EAG-Bund, Speicher (10 × 150 €)", "1.500 €"],
        ["Made-in-Europe-Bonus (10 % je Komponente)", "bis rund 450 €"],
        ["Gemeindezuschuss (je nach Gemeinde)", "bis rund 1.000 €"],
        ["<b>Gesamtförderung</b>", "<b>rund 3.000 bis 4.500 €</b>"],
    ],
    hl_cols=(1,),
)}
<p>Wer eine Bestandsanlage besitzt und nur einen Speicher nachrüstet, erhält vom Land bis zu 2.250 Euro.
Zum Vergleich: Der Richtpreis für eine 10-kWp-Anlage mit Speicher liegt bei rund 15.000 bis 22.000 Euro vor
Förderung.</p>
<p><small>*Beispielkonditionen. Der Made-in-Europe-Bonus setzt Komponenten von der White List voraus, die
Gemeindeförderung hängt vom Wohnort ab.</small></p>
{A.cta("Jetzt Förderung und Technik aus einer Hand",
       "Wir prüfen Ihre Förderschiene, dimensionieren Speicher und Anlage förderfähig und übernehmen die "
       "Anträge beim Bund, beim Land und bei der Gemeinde.",
       primary=("kontakt", "Kostenlose Beratung anfragen"), secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Förderung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie GmbH aus Villach plant und montiert Photovoltaikanlagen, Speicher und Wärmepumpen in "
                 "Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. "
                 "Referenzprojekte gibt es in sechs Bundesländern, darunter eine 40-kWp-Gewerbeanlage in "
                 "Oberösterreich mit Ost-West-Ausrichtung auf Trapezblech und 40-kWh-Speicher: rund 40.000 kWh "
                 "Jahresertrag und 13.500 Euro Ersparnis pro Jahr. Für Projekte außerhalb unseres Montagegebiets "
                 "sprechen Sie uns an, wir prüfen die Machbarkeit im Einzelfall. Für Privathaushalte in Oberösterreich "
                 "berät der OÖ Energiesparverband kostenlos zu allen Förderfragen."),
        "grid": [
            ("Förderabwicklung komplett", "EAG-Ticket, Landesantrag, Gemeindeförderung und Endabrechnung."),
            ("Referenz Oberösterreich", "40 kWp Gewerbe mit 40-kWh-Speicher, 13.500 € Ersparnis pro Jahr."),
            ("300+ Projekte", "Referenzen in sechs Bundesländern, typische Amortisation 4 bis 6 Jahre."),
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und Energiemanagement vom selben Team."),
        ],
    },

    "faq": [
        ("Gibt es in Oberösterreich 2026 eine direkte PV-Pauschalförderung?",
         "Nein. Oberösterreich zahlt 2026 keine eigene PV-Förderung pro Kilowattpeak für Privathaushalte. Neue "
         "Anlagen werden über die EAG-Bundesförderung gefördert, die für Privatanlagen zwischen 1.500 und 2.800 Euro "
         "Direktzuschuss plus Made-in-Europe-Bonus bringt. Die Landesförderung konzentriert sich auf die "
         "Speicher-Nachrüstung bei Bestandsanlagen."),
        ("Wie hoch ist die Speicher-Nachrüstungsförderung in Oberösterreich?",
         "150 Euro je kWh Nennkapazität, gedeckelt bei 40 Prozent der förderfähigen Bruttoinvestitionskosten und "
         "maximal 15 kWh, also bis zu 2.250 Euro. Voraussetzung: Die PV-Anlage ist vor dem 1. Jänner 2026 mit "
         "Netzzugangsvertrag in Betrieb gegangen. Antragsberechtigt sind Privatpersonen, Gemeinden und Vereine."),
        ("Kann ich die OÖ-Speicherförderung mit der EAG-Speicherförderung kombinieren?",
         "Nein, das ist ausdrücklich ausgeschlossen. Wer neu baut, nutzt die EAG-Bundesförderung für PV und "
         "Speicher. Wer eine Bestandsanlage (in Betrieb vor 1. Jänner 2026) um einen Speicher ergänzt, beantragt die "
         "Landesförderung. Andere Bundesförderungen für denselben Speicher sind ebenfalls ausgeschlossen."),
        ("Wie groß sollte der nachgerüstete Speicher sein?",
         "Die Richtlinie nennt rund 1,5 kWh Nennkapazität je kWp installierter PV-Leistung als Orientierung, "
         "mindestens 0,5 kWh je kWp. Gefördert werden maximal 15 kWh, größere Speicher sind erlaubt, aber nur "
         "die ersten 15 kWh werden bezuschusst."),
        ("Wann und wo stelle ich den Antrag für die OÖ-Speicherförderung?",
         "Der Antrag wird nach Umsetzung der Maßnahme online beim Amt der OÖ Landesregierung gestellt. Sie "
         "brauchen den Netzzugangsvertrag der PV-Anlage, die Rechnung, den Zahlungsnachweis und ein Prüfprotokoll "
         "nach OVE E 8101 einer befugten Elektrofachkraft."),
        ("Was sind PV-Beschleunigungszonen in Oberösterreich?",
         "Gebiete, in denen Genehmigungsverfahren für PV-Anlagen deutlich vereinfacht sind. Die Verordnung basiert "
         "auf der EU-Richtlinie RED III, die bis 21. Februar 2026 umzusetzen war. In ausgewiesenen "
         "Beschleunigungsgebieten gelten PV-Anlagen und Batteriespeicher als widmungsneutrale Bauwerke, das "
         "Widmungserfordernis entfällt."),
        ("Welche Gesamtförderung ist für eine Neuanlage in Oberösterreich realistisch?",
         "Für 10 kWp mit 10 kWh Speicher rund 3.000 bis 4.500 Euro: 1.500 Euro EAG für die PV-Anlage, 1.500 Euro "
         "EAG für den Speicher, bis rund 450 Euro Made-in-Europe-Bonus und je nach Gemeinde bis rund 1.000 Euro "
         "Gemeindezuschuss."),
        ("Wer hilft bei der Förderabwicklung in Oberösterreich?",
         "Für Privathaushalte in Oberösterreich berät der OÖ Energiesparverband kostenlos. EBZ Energie mit Sitz in "
         "Villach montiert in Kärnten und der Steiermark und hat Referenzprojekte in sechs Bundesländern, darunter "
         "eine 40-kWp-Gewerbeanlage in Oberösterreich. Für Projekte außerhalb des Montagegebiets prüfen wir die "
         "Machbarkeit auf Anfrage."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und montiert PV-Anlagen, "
                    "Speicher und Wärmepumpen in Kärnten und der Steiermark und hat unter anderem eine "
                    "40-kWp-Gewerbeanlage in Oberösterreich umgesetzt. Die Angaben werden anhand der offiziellen "
                    "Richtlinien der EAG-Abwicklungsstelle und des Landes Oberösterreich aktualisiert. Keine Rechts- "
                    "oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("Land Oberösterreich: Nachrüstung von systemdienlichen Solarstromspeichern",
         "https://www.land-oberoesterreich.gv.at/554598.htm"),
        ("OÖ Energiesparverband", "https://www.energiesparverband.at/"),
    ],
    "related": [
        ("/photovoltaik-landesfoerderungen/", "PV-Landesförderungen: alle 9 Bundesländer"),
        ("/foerderung-fuer-pv-speicher/", "Förderung für PV-Speicher"),
        ("/photovoltaik-foerderung-salzburg/", "Photovoltaik-Förderung Salzburg 2026"),
        ("referenzen", "Referenz: 40 kWp Gewerbeanlage Oberösterreich"),
    ],
    "cta": {
        "h3": "Welche Schiene passt zu Ihrer Anlage?",
        "text": "Wir prüfen EAG, Landesförderung und Gemeinde und dimensionieren den Speicher förderfähig.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre PV-Anlage, förderoptimiert geplant",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
