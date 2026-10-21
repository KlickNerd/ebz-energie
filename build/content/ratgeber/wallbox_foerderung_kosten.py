"""Ratgeber: Wallbox, Förderung und Kosten 2026 (Kärnten und Steiermark).

Migriert von ebz-photovoltaik.at/wallbox-foerderung-kosten/ (veröffentlicht 10.09.2026).
Förderstand am 21.10.2026 an offiziellen Quellen geprüft:
  Bund: klimafonds.gv.at/foerderung/emob-private-2025/ ("Abgeschlossen", vorzeitig beendet wegen
        ausgeschöpften Budgets, Registrierungen nicht mehr möglich; Wallbox zuletzt 400 Euro).
  Steiermark: wohnbau.steiermark.at, Seite "Elektromobilität: Lastmanagementsysteme und Ladestationen"
        und Kurzinformation "Intelligente E-Ladestationen" vom 09.10.2026 (30 %, max. 300 Euro, 1.1. bis 31.12.2026).
        Das in der Quelle verlinkte Infoblatt (alte PDF-Adresse) liefert 404, ersetzt durch die neue Fassung.
  EMS: klimafonds.gv.at/foerderung/energiemanagement-haushalte-2026/ (Status "Laufend", bis 15.04.2027, 12:00 Uhr).
  Kärnten: ktn.gv.at am 21.10.2026 nicht erreichbar, Aussage "kein eigenes Programm" daher vorsichtig formuliert.
OeMAG-Wert auf September 2026 (10,168 ct) ergänzt, Beispielrechnung mit beiden Monatswerten neu gerechnet.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "wallbox-foerderung-kosten",
    "path": "/wallbox-foerderung-kosten/",
    "title": "Wallbox 2026: Kosten und Förderung bis 300 € | EBZ Energie",
    "description": ("Wallbox mit Installation: 1.200 bis 3.500 €. Bund eingestellt, Steiermark 30 % bis "
                    "300 €, EMS-Förderung bis 600 €. Mit PV-Überschuss 100 km für 1 bis 2 €."),
    "eyebrow": "E-Mobilität · Förderung",
    "crumb_label": "Wallbox: Förderung und Kosten",
    "h1": "Wallbox 2026: Kosten von 1.200 bis 3.500 Euro und welche Förderung es noch gibt",
    "lead": ("Die Bundesförderung für private Wallboxen ist beendet, die Steiermark zahlt bis zu 300 Euro und "
             "über die EMS-Förderung sind bis zu 600 Euro für die Steuerung möglich. Dieser Ratgeber zeigt, was "
             "eine Wallbox mit Installation kostet und warum Sie mit Sonnenstrom 100 Kilometer für 1 bis 2 Euro fahren."),
    "chips": [
        "Bund: <b>eingestellt</b>",
        "Steiermark: <b>30 %</b>, max. 300 €",
        "EMS-Förderung: <b>bis 600 €</b>",
        "Gesamtkosten: <b>1.200 bis 3.500 €</b>",
    ],
    "date_published": "2026-09-10",
    "date_modified": "2026-10-21",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit Photovoltaikanlage, deren Sonnenstrom über die Wallbox ins E-Auto fließt",

    "tldr": [
        "Die Bundesförderung für private Wallboxen (Klimafonds, „E-Mobilität für Private 2025“, zuletzt 400 Euro "
        "je Wallbox) wurde wegen ausgeschöpften Budgets vorzeitig beendet. Neue Registrierungen sind nicht möglich.",
        "Das Land Steiermark fördert 2026 dreiphasige, intelligente Wallboxen ab 11 kW mit höchstens 30 Prozent "
        "der anrechenbaren Kosten, maximal 300 Euro. Antrag nach Montage, binnen 6 Monaten ab Rechnungsdatum.",
        "In Kärnten gibt es nach unserem Stand kein eigenes Landesprogramm für private Wallboxen.",
        "Über die Energiemanagement-Förderung des Klimafonds sind bis zu 600 Euro für ein EMS möglich, das "
        "Wallbox, PV-Anlage oder Speicher steuert. Registrierung vor der Rechnung, längstens bis 15. April 2027.",
        "Wallbox und Installation kosten im Einfamilienhaus meist 1.200 bis 3.500 Euro*. Mit PV-Überschuss "
        "kosten 100 Kilometer rund 1 bis 2 Euro statt rund 11 Euro mit dem Benziner.",
    ],
    "kpis": [
        ("1.200 bis 3.500 €", "Wallbox mit Installation im Einfamilienhaus*"),
        ("300 €", "maximal vom Land Steiermark"),
        ("600 €", "maximal EMS-Förderung für Haushalte"),
        ("1 bis 2 €", "für 100 km mit PV-Überschuss*"),
    ],

    "sections": [
        ("Wallbox-Förderung 2026: Das hat sich geändert", "foerderung-2026", f"""
<p><b>Für private Wallboxen gibt es 2026 keine Bundesförderung mehr: Das Klimafonds-Programm „E-Mobilität für
Private 2025“ wurde wegen ausgeschöpften Budgets vorzeitig beendet, Registrierungen sind nicht mehr möglich.</b>
Das Land Steiermark zahlt für intelligente 11-kW-Wallboxen höchstens 30 Prozent der anrechenbaren Kosten,
maximal 300 Euro; die EMS-Förderung des Klimafonds bringt bis zu 600 Euro für die Steuerung (Quellen:
klimafonds.gv.at, Land Steiermark, Stand 21. Oktober 2026).</p>
<p>Wer in den Vorjahren eine Wallbox installiert hat, konnte mit einem Bundeszuschuss rechnen, zuletzt 400 Euro
je Wallbox im Programm 2025. Das Programm lief längstens bis 31. März 2026, das Budget war schon vorher
aufgebraucht. Ein Nachfolgeprogramm für Private ist beim Klimafonds derzeit nicht ausgeschrieben. Gefördert wird
heute vor allem auf Landesebene und über den Umweg der Energiemanagement-Förderung. Der Stand für unser
Einzugsgebiet:</p>
{A.table(
    ["Programm", "Förderung", "Status Oktober 2026"],
    [
        ["Bund: E-Mobilität für Private (Klimafonds)", "zuletzt 400 € je Wallbox", "vorzeitig beendet, keine neuen Registrierungen"],
        ["Land Steiermark: Intelligente E-Ladestationen", "höchstens 30 % der Kosten, max. 300 €",
         "laufend, Förderzeitraum 1. Jänner bis 31. Dezember 2026"],
        ["Land Kärnten", "kein eigenes Wallbox-Programm bekannt", "vor dem Kauf aktuellen Stand prüfen"],
        ["Klimafonds: Energiemanagement-Förderung", "50 % der EMS-Kosten, max. 600 € (Haushalte)",
         "laufend, längstens bis 15. April 2027"],
    ],
    hl_cols=(1,),
)}
<p>Mehrparteienhäuser hatten im Bundesprogramm eigene Sätze (800 Euro für Einzelanlagen, 1.500 Euro für
Gemeinschaftsanlagen). Auch diese Schiene ist mit dem Programm 2025 ausgelaufen. Einen Überblick über alle
aktuell offenen Programme für PV, Speicher, Wärmepumpe und Energiemanagement finden Sie unter
{a('foerderungen', 'Förderungen 2026')}.</p>
"""),
        ("Steiermark: 30 Prozent, maximal 300 Euro", "steiermark", f"""
<p>Das Land Steiermark fördert die Anschaffung <b>dreiphasiger, intelligenter Wallboxen mit einer möglichen
Bemessungsleistung von mindestens 11 kW</b>. Die Förderung ist mit 30 Prozent der anrechenbaren
Investitionskosten begrenzt, für die Wallbox gibt es maximal 300 Euro. Rechnerisch ist der Höchstbetrag ab
1.000 Euro anrechenbaren Kosten erreicht. Die Voraussetzungen laut Kurzinformation des Landes (Fassung vom
9. Oktober 2026):</p>
<ul>
  <li><b>Antragsteller:</b> natürliche Person mit Hauptwohnsitz in der Steiermark, auf die ein E-PKW mit
  reinem Elektroantrieb in der Steiermark zugelassen ist. Das Auto darf nicht unternehmerisch genutzt oder
  vom Arbeitgeber gestellt werden.</li>
  <li><b>Fachbetrieb:</b> Errichtung und Inbetriebnahme durch ein befugtes Elektrounternehmen, nur neue
  Komponenten. Die Wallbox muss so montiert sein, dass nur ein Elektrounternehmen sie vom Netz trennen kann.</li>
  <li><b>Strom:</b> ausschließlich Ökostrom laut E-Control, außer am Standort ist eine PV-Anlage mit mindestens
  1,5 kWp installiert. Nachweis über Liefervertrag, Stromrechnung oder Errichtungsattest der PV-Anlage.</li>
  <li><b>Betrieb:</b> mindestens sieben Jahre, bei einem Verkauf wird der Käufer auf diese Pflicht hingewiesen.</li>
  <li><b>Unterlagen:</b> Rechnung mit Zahlungsnachweis, Zulassungsschein, Meldung an den Netzbetreiber, Fotos
  und der Ausführungs- und Erstprüfungsnachweis des Elektrounternehmens.</li>
</ul>
{A.box("Der Antrag läuft einstufig und erst <b>nach</b> Montage und Rechnungslegung, online über das "
       "eGovernment-Formular des Landes, binnen sechs Monaten ab Rechnungsdatum. Die aktuelle Kurzinformation "
       "gilt vom 1. Jänner bis 31. Dezember 2026; ob das Programm 2027 weiterläuft, ist noch nicht veröffentlicht.",
       label="Reihenfolge:")}
<p>Wer in der Steiermark ohnehin eine {a('foerderung_steiermark', 'PV-Anlage')} hat oder plant, erfüllt die
Strombedingung über die 1,5-kWp-Grenze ohne eigenen Ökostromvertrag.</p>
"""),
        ("Kärnten und der Umweg über die EMS-Förderung", "ems-foerderung", f"""
<p>In Kärnten gibt es nach unserem Stand kein eigenes Landesprogramm für private Wallboxen. Weil sich
Landesprogramme kurzfristig ändern können, prüfen wir den aktuellen Stand vor jedem Angebot.</p>
<p>Für Haushalte in ganz Österreich interessant ist der Umweg über die
{a('/ems-foerderung/', 'Energiemanagement-Förderung des Klimafonds')}. Gefördert werden Energiemanagementsysteme,
die mindestens zwei Komponenten wie PV-Anlage, Speicher, Wärmepumpe oder Ladestelle aktiv und netzdienlich
steuern. Der Zuschuss beträgt <b>50 Prozent der förderfähigen EMS-Kosten, maximal 600 Euro</b>, plus 100 Euro
Bonus, wenn das Projekt für die Begleitforschung ausgewählt wird. Die Wallbox selbst wird dabei nicht bezahlt,
wohl aber die intelligente Steuerung, die sie erst wirtschaftlich macht.</p>
{A.table(
    ["EMS-Förderung für Haushalte", "Regel laut Leitfaden"],
    [
        ["Förderhöhe", "50 % der förderfähigen Kosten inkl. USt., max. 600 € (+ 100 € Begleitforschung)"],
        ["Mindestumfang", "mindestens zwei Komponenten aktiv gesteuert, zum Beispiel PV-Anlage und Wallbox"],
        ["Reihenfolge", "online registrieren vor der ersten Rechnung, danach 6 Monate für Umsetzung und Antrag"],
        ["Frist", "solange Budget vorhanden, längstens bis 15. April 2027, 12:00 Uhr"],
        ["Verpflichtung", "5 Jahre Betrieb mit einer von 6 Optionen, zum Beispiel dynamischer Stromtarif"],
    ],
    hl_cols=(1,),
)}
{A.box("Für das EMS selbst ist laut Leitfaden keine zweite Förderung erlaubt. Die Wallbox ist aber keine "
       "EMS-Position: Weisen Sie EMS und Wallbox auf der Rechnung getrennt aus. Ob in der Steiermark beide "
       "Förderungen nebeneinander möglich sind, klären wir vor der Bestellung mit Ihnen.")}
<p>Wie das System technisch funktioniert, erklärt die Seite {a('ems', 'Energiemanagementsystem')}.</p>
"""),
        ("Was kostet eine Wallbox 2026?", "kosten", f"""
<p>Die Gesamtkosten setzen sich aus dem Gerät und der Installation zusammen. Die Wallbox selbst ist gut
vergleichbar, die Installation schwankt stark mit den örtlichen Gegebenheiten.</p>
{A.kpis([
    ("500 bis 1.500 €", "Wallbox mit 11 kW*"),
    ("500 bis 2.500 €", "Installation durch den Elektriker*"),
    ("1.200 bis 3.500 €", "typisch im Einfamilienhaus*"),
    ("11 kW", "reicht für fast alle Privathaushalte"),
])}
{A.table(
    ["Situation", "Installation*", "Gesamt inkl. Wallbox*"],
    [
        ["Garage direkt neben dem Zählerkasten, Platz im Verteiler", "500 bis 900 €", "1.200 bis 2.000 €"],
        ["Carport oder Außenwand, 10 bis 20 Meter Leitung", "900 bis 1.600 €", "1.700 bis 2.800 €"],
        ["Lange Leitung mit Grabarbeiten oder Umbau des Zählerplatzes", "1.600 bis 2.500 €", "2.500 bis 3.500 € und mehr"],
    ],
    hl_cols=(2,),
)}
<p>Kostentreiber sind fast immer die <b>Leitungslänge</b>, ein <b>veralteter Zählerkasten</b> und die richtige
<b>Absicherung</b>. Jede Wallbox braucht einen eigenen Stromkreis mit Leitungsschutzschalter und einen
Fehlerstromschutz, der auch Gleichfehlerströme erkennt. Viele Wallboxen haben diese DC-Fehlerstromerkennung
bereits eingebaut, das spart einen teuren FI-Schutzschalter Typ B.</p>
<p>Wer gleichzeitig einen {a('carport', 'Photovoltaik-Carport')} plant, legt die Zuleitung in einem Zug: Die
Wallbox hängt dann direkt am Stellplatz, und die Module auf dem Dach liefern den Ladestrom.</p>
<p><small>*Richtwerte aus der Angebotspraxis, inklusive Umsatzsteuer und vor Förderung. Der tatsächliche Preis
hängt von Gerät, Leitungsweg und Zählerplatz ab und steht nach dem Vor-Ort-Check fest.</small></p>
"""),
        ("Wallbox kaufen: Worauf Sie achten sollten", "worauf-achten", f"""
<ul>
  <li><b>11 kW, dreiphasig:</b> der Standard für Privathaushalte und Voraussetzung für die steirische Förderung.</li>
  <li><b>PV-Überschussladen:</b> Die Wallbox muss mit Wechselrichter oder Energiemanagementsystem kommunizieren
  können, sonst verschenken Sie das größte Sparpotenzial.</li>
  <li><b>Phasenumschaltung:</b> Wallboxen, die zwischen ein- und dreiphasigem Laden wechseln, starten schon bei
  rund 1,4 kW Überschuss. Ohne Umschaltung braucht es meist über 4 kW.</li>
  <li><b>Lastmanagement:</b> wichtig, wenn Wärmepumpe, Herd und Auto gleichzeitig laufen, damit der
  Hausanschluss nicht überlastet wird.</li>
  <li><b>Integrierte DC-Fehlerstromerkennung:</b> spart Kosten bei der Absicherung.</li>
  <li><b>Zugangsschutz:</b> RFID-Karte oder App, wenn die Wallbox frei zugänglich im Carport hängt.</li>
  <li><b>Fest angeschlagenes Kabel:</b> im Alltag praktischer als eine Steckdose, in die das Kabel jedes Mal
  neu eingesteckt wird.</li>
</ul>
{A.cta("Wallbox inklusive Installation und Netzbetreiber-Meldung",
       "EBZ Energie installiert Ihre Wallbox in Kärnten und der Steiermark, verbindet sie mit Ihrer PV-Anlage "
       "und kümmert sich um Meldung und Förderung.",
       primary=("kontakt", "Wallbox-Angebot anfragen"), secondary=("ems", "Zum Energiemanagement"))}
"""),
        ("Laden mit Sonnenstrom: So rechnet sich die Wallbox", "pv-ueberschuss", f"""
<p>Der größte finanzielle Vorteil entsteht, wenn die Wallbox mit Ihrer eigenen Photovoltaikanlage verbunden ist.
Überschüssiger Sonnenstrom bringt bei der Einspeisung nur den
{a('/oemag-einspeisetarif/', 'OeMAG-Marktpreis')}: Im September 2026 waren das 10,168 Cent je Kilowattstunde,
im Juli 6,146 Cent (Stand Oktober 2026, der Wert schwankt monatlich). Im eigenen Auto ersetzt dieselbe
Kilowattstunde Benzin oder teuren Ladestrom.</p>
{A.table(
    ["Was kosten 100 Kilometer?", "Annahme*", "Kosten"],
    [
        ["Benziner", "7 Liter zu 1,60 €", "11,20 €"],
        ["E-Auto am Schnelllader", "18 kWh zu 0,59 €", "10,60 €"],
        ["E-Auto mit Haushaltsstrom", "18 kWh zu 0,28 €", "5,00 €"],
        ["E-Auto mit PV-Überschuss", "18 kWh, bewertet mit der entgangenen Einspeisung von 6 bis 10 ct", "1,10 bis 1,80 €"],
    ],
    hl_cols=(2,),
)}
<p>Bei 12.000 Kilometern im Jahr braucht ein Elektroauto rund 2.200 Kilowattstunden. Laden Sie davon die Hälfte
mit PV-Überschuss, sparen Sie gegenüber reinem Haushaltsstrom rund 200 bis 240 Euro und gegenüber dem Benziner
über 900 Euro pro Jahr*. In Kombination mit einem {a('/dynamischer-stromtarif/', 'dynamischen Stromtarif')}
lädt die Wallbox die restliche Energie in den günstigsten Stunden.</p>
{A.box("Wer tagsüber arbeitet und das Auto nur abends zu Hause hat, nutzt den PV-Überschuss vor allem am "
       "Wochenende. Ein " + a('batteriespeicher', 'Batteriespeicher') + " kann einen Teil puffern, ersetzt aber "
       "keine Tagesladung. Wir rechnen das bei der Planung ehrlich für Ihr Nutzungsprofil durch.",
       label="Gut zu wissen:")}
<p><small>*Beispielrechnung mit Richtwerten: Kompaktwagen, E-Auto mit 18 kWh je 100 km, Schnelllader 0,59 € je
kWh, Haushaltsstrom 0,28 € je kWh, PV-Überschuss bewertet mit dem OeMAG-Marktpreis von rund 6 Cent (Juli 2026)
bis rund 10 Cent (September 2026). Ihr Ergebnis hängt von Fahrprofil, Tarif und Anlage ab.</small></p>
"""),
        ("So läuft die Installation ab", "ablauf", f"""
{A.steps([
    ("Vor-Ort-Check", "Wir prüfen Zählerkasten, Hausanschluss, Leitungsweg und den besten Montageort."),
    ("Angebot und Förderung", "Sie bekommen ein Festpreisangebot, bei Bedarf mit Energiemanagement. Wir prüfen "
     "Landes- und EMS-Förderung und registrieren das EMS vor der ersten Rechnung."),
    ("Meldung beim Netzbetreiber", "Die Meldung der Ladeeinrichtung übernehmen wir für Sie."),
    ("Installation", "Montage der Wallbox, Leitung, Absicherung und Einbindung in die PV-Anlage, meist an einem Tag."),
    ("Inbetriebnahme", "Wir richten App und Überschussladen ein und erstellen den Prüfnachweis für Ihre "
     "Förderunterlagen."),
])}
{A.cta("Jetzt mit Sonnenstrom laden",
       "Wallbox, PV-Anlage und Energiemanagement aus einer Hand: Wir planen, installieren und übernehmen die "
       "Förderabwicklung.",
       primary=("kontakt", "Beratung anfragen"), secondary=("/ems-foerderung/", "Zur EMS-Förderung"))}
"""),
        ("Fazit: Förderung kleiner, Sparpotenzial größer", "fazit", f"""
<p>Die Bundesförderung für private Wallboxen ist Geschichte, in der Steiermark gibt es 2026 noch bis zu 300 Euro
vom Land, und die EMS-Förderung bringt bis zu 600 Euro für die Steuerung. Wirtschaftlich entscheidend ist heute
etwas anderes: Wer mit eigenem Sonnenstrom lädt, fährt 100 Kilometer für rund 1 bis 2 Euro. Eine gut geplante
Wallbox mit PV-Überschussladen und Energiemanagement holt ihre Kosten damit über die Jahre wieder herein. Wer
noch keine PV-Anlage hat, findet die Grundlagen auf der Seite {a('photovoltaik', 'Photovoltaik')}.</p>
"""),
    ],

    "partner": {
        "h2": "Ihre Wallbox vom Photovoltaik-Fachbetrieb",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach installiert Wallboxen in Kärnten und der Steiermark und verbindet sie mit "
                 "PV-Anlage, Speicher und Wärmepumpe zu einem System. Zertifizierte Fachkräfte, ein fester "
                 "Ansprechpartner von der Planung bis zur Übergabe, Netzbetreiber-Meldung und Förderabwicklung."),
        "grid": [
            ("PV-Überschussladen", "Einrichtung und Abstimmung mit Ihrem Wechselrichter."),
            ("Lastmanagement", "Kein Überlasten des Hausanschlusses, auch mit Wärmepumpe."),
            ("Meldung inklusive", "Wir melden die Ladeeinrichtung beim Netzbetreiber."),
            ("Förderung geprüft", "Landesförderung und EMS-Förderung aus einer Hand."),
        ],
    },

    "faq": [
        ("Gibt es 2026 noch eine Bundesförderung für die Wallbox?",
         "Nein. Das Klimafonds-Programm „E-Mobilität für Private 2025“ wurde wegen ausgeschöpften Budgets "
         "vorzeitig beendet, Registrierungen sind nicht mehr möglich. Zuletzt gab es 400 Euro je Wallbox. Ein "
         "Nachfolgeprogramm für Private ist derzeit nicht ausgeschrieben (Stand Oktober 2026)."),
        ("Welche Wallbox-Förderung gibt es in der Steiermark?",
         "Das Land Steiermark fördert dreiphasige, intelligente Wallboxen ab 11 kW mit höchstens 30 Prozent der "
         "anrechenbaren Kosten, maximal 300 Euro. Voraussetzungen sind unter anderem Hauptwohnsitz in der "
         "Steiermark, ein dort zugelassenes privates Elektroauto, Installation durch ein befugtes "
         "Elektrounternehmen und Ökostrom oder eine PV-Anlage ab 1,5 kWp. Der Antrag folgt binnen sechs Monaten "
         "nach dem Rechnungsdatum."),
        ("Gibt es in Kärnten eine Förderung für die Wallbox?",
         "Nach unserem Stand gibt es in Kärnten kein eigenes Landesprogramm für private Wallboxen. Über die "
         "Energiemanagement-Förderung des Klimafonds lässt sich die Steuerung mit bis zu 600 Euro fördern, wenn "
         "die Wallbox gemeinsam mit PV-Anlage oder Speicher über ein Energiemanagementsystem gesteuert wird."),
        ("Was kostet eine Wallbox mit Installation?",
         "Eine 11-kW-Wallbox kostet meist 500 bis 1.500 Euro. Die Installation liegt je nach Leitungslänge, "
         "Zählerkasten und Absicherung bei 500 bis 2.500 Euro. Für ein Einfamilienhaus sind 1.200 bis 3.500 Euro "
         "realistisch (Richtwerte)."),
        ("Reicht eine 11-kW-Wallbox oder brauche ich 22 kW?",
         "Für private Haushalte reichen 11 kW fast immer. Die meisten Elektroautos laden mit Wechselstrom ohnehin "
         "nur mit 11 kW, und über Nacht wird jeder Akku voll. 22-kW-Geräte sind teurer, brauchen eine stärkere "
         "Zuleitung und beim Netzbetreiber in der Regel eine Zustimmung."),
        ("Wie funktioniert PV-Überschussladen?",
         "Die Wallbox erfährt vom Wechselrichter oder Energiemanagementsystem, wie viel Sonnenstrom gerade übrig "
         "ist, und passt die Ladeleistung laufend an. Mit Phasenumschaltung startet das Laden schon bei rund "
         "1,4 kW Überschuss, ohne Umschaltung meist erst über 4 kW. So lädt das Auto mit Strom, der sonst für 6 "
         "bis 10 Cent eingespeist würde."),
        ("Muss ich die Wallbox beim Netzbetreiber melden?",
         "Ja, Ladeeinrichtungen werden beim Netzbetreiber gemeldet, in der Steiermark ist die Kopie dieser Meldung "
         "auch Teil der Förderunterlagen. Das übernimmt der Elektrofachbetrieb, bei EBZ Energie ist die Meldung im "
         "Angebot enthalten."),
        ("Wie bekomme ich die EMS-Förderung für meine Wallbox?",
         "Registrieren Sie das Energiemanagementsystem online bei der Umweltförderung, bevor die erste Rechnung "
         "gestellt wird. Danach bleiben sechs Monate für Installation und Antrag. Gefördert werden 50 Prozent der "
         "EMS-Kosten, maximal 600 Euro, längstens bis 15. April 2027; die Wallbox selbst ist nicht förderfähig."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. EBZ Energie plant und installiert "
                    "Photovoltaik, Batteriespeicher, Wärmepumpen und Wallboxen in Kärnten und der Steiermark und "
                    "übernimmt die komplette Förderabwicklung. Förderstand und Kosten werden anhand der offiziellen "
                    "Förderstellen und realer Installationen aktualisiert. Keine Rechts- oder Steuerberatung, "
                    "maßgeblich sind die offiziellen Förderbedingungen der jeweiligen Stelle."),
    "sources": [
        ("Klima- und Energiefonds: E-Mobilität für Private 2025 (abgeschlossen)",
         "https://www.klimafonds.gv.at/foerderung/emob-private-2025/"),
        ("Land Steiermark: Elektromobilität, Lastmanagementsysteme und Ladestationen",
         "https://www.wohnbau.steiermark.at/cms/beitrag/12856318/165238372/"),
        ("Land Steiermark: Kurzinformation Intelligente E-Ladestationen, Oktober 2026 (PDF)",
         "https://www.wohnbau.steiermark.at/cms/dokumente/12856318_165238372/ea13039e/2026-10_Infoblatt%20Intelligente%20E-Ladestationen.pdf"),
        ("Klima- und Energiefonds: Energiemanagement Haushalte 2026",
         "https://www.klimafonds.gv.at/foerderung/energiemanagement-haushalte-2026/"),
    ],
    "related": [
        ("/ems-foerderung/", "EMS-Förderung 2026: bis 600 €"),
        ("ems", "Energiemanagementsystem"),
        ("carport", "Photovoltaik-Carport mit Wallbox"),
        ("batteriespeicher", "Batteriespeicher"),
    ],
    "cta": {
        "h3": "Wallbox mit Sonnenstrom",
        "text": "Wir planen Wallbox, PV-Anlage und Energiemanagement und prüfen alle Förderungen für Ihren Standort.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Laden Sie Ihr Auto mit eigenem Strom",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein fester Ansprechpartner aus Villach, der "
                   "Planung, Montage und Förderabwicklung aus einer Hand übernimmt."),
}
