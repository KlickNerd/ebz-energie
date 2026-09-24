"""Ratgeber: Dynamischer Stromtarif (Börsenpreis stündlich).

Migriert von ebz-photovoltaik.at/dynamischer-stromtarif/ (Stand der Quelle: Juli 2026).
Abgrenzung: dynamisch = stündlicher Börsenpreis; flexibel = Oberbegriff für
marktorientierte Tarife mit seltenerer Anpassung (siehe /flexibler-stromtarif/).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "dynamischer-stromtarif",
    "path": "/dynamischer-stromtarif/",
    "title": "Dynamischer Stromtarif: Wann sich Spotpreise lohnen | EBZ",
    "description": ("Dynamischer Stromtarif: stündlicher Börsenpreis statt Fixpreis. Für wen er sich lohnt, "
                    "welche Risiken es gibt und wie ein EMS das Sparen automatisiert."),
    "eyebrow": "Stromtarife · Dynamisch",
    "crumb_label": "Dynamischer Stromtarif",
    "h1": "Dynamischer Stromtarif: Wann sich stündliche Börsenpreise wirklich lohnen",
    "lead": ("Bei einem dynamischen Stromtarif zahlen Sie den echten Börsenpreis, Stunde für Stunde. Wer "
             "Wärmepumpe, E-Auto oder Speicher in günstige Stunden verschieben kann, spart spürbar. Wer "
             "starr verbraucht, trägt nur das Risiko der Preisspitzen."),
    "chips": [
        "Preis ändert sich <b>stündlich</b>",
        "Voraussetzung: <b>Smart Meter</b>",
        "Ideal für <b>WP, E-Auto, Speicher</b>",
        "Am besten <b>per EMS automatisiert</b>",
    ],
    "date_published": "2026-07-17",
    "date_modified": "2026-09-24",
    "hero_img": "speicher",
    "hero_alt": "Batteriespeicher im Eigenheim, der bei dynamischem Stromtarif in günstigen Stunden lädt",

    "tldr": [
        "Ein dynamischer Stromtarif bildet den Börsenpreis (Day-Ahead-Markt) ab und ändert sich in der "
        "Regel stündlich: nachts und mittags bei viel Sonne günstig, am Abend am teuersten.",
        "Er lohnt sich vor allem für flexible Verbraucher: Wärmepumpe, E-Auto und Batteriespeicher. Wer "
        "seinen Verbrauch nicht verschieben kann, spart wenig.",
        "Voraussetzung ist ein Smart Meter mit aktiver Datenübertragung, also ohne Opt-out, und ein "
        "Lieferant, der dynamische Tarife anbietet.",
        "Den größten Nutzen bringt ein Energiemanagementsystem, das flexible Verbraucher automatisch in "
        "die günstigsten Stunden legt und teure Stunden meidet. Der Klimafonds fördert solche Systeme mit "
        "bis zu 600 Euro.",
    ],
    "kpis": [
        ("24", "Preise pro Tag statt ein Fixpreis"),
        ("15 Min.", "Messintervall des Smart Meters"),
        ("3", "typische Flexverbraucher: WP, E-Auto, Speicher"),
        ("600 €", "max. EMS-Förderung 2026 für Haushalte"),
    ],

    "sections": [
        ("Was ist ein dynamischer Stromtarif?", "definition", f"""
<p>Bei einem dynamischen Stromtarif richtet sich der Preis pro Kilowattstunde nach dem aktuellen
Strombörsenpreis und ändert sich in der Regel stündlich. Ist viel günstiger Strom im Netz, etwa nachts
oder mittags bei viel Sonne, ist er billig. In Zeiten hoher Nachfrage, typischerweise am Abend, wird er
teurer. Statt eines festen Preises zahlen Sie also 24 verschiedene Preise pro Tag, die der Lieferant
meist am Vortag veröffentlicht.</p>
<p>Die Abgrenzung ist wichtig, weil die Begriffe oft vermischt werden: „Flexibel“ oder „variabel“ ist der
Oberbegriff für alle Tarife, die den Preis an den Markt anpassen. Ein
{a('/flexibler-stromtarif/', 'flexibler Stromtarif')} ändert den Preis aber selten, etwa monatlich, und
kommt meist ohne Smart Meter aus. Der dynamische Tarif ist die feinste Stufe: stündlicher Börsenpreis,
Smart Meter zwingend.</p>
{A.table(
    ["Tageszeit", "Börsenpreis (schematisch)", "Grund"],
    [
        ["0 bis 6 Uhr", "günstig", "wenig Nachfrage, Grundlastkraftwerke laufen"],
        ["10 bis 15 Uhr", "günstig bis sehr günstig", "viel Solarstrom im Netz, an sonnigen Tagen auch negativ"],
        ["17 bis 21 Uhr", "teuer", "hohe Nachfrage, kaum Sonne"],
    ],
    hl_cols=(1,),
)}
<p><small>Schematischer Tagesverlauf. Die tatsächlichen Preise schwanken je nach Wetter, Wochentag und
Jahreszeit.</small></p>
"""),
        ("Für wen lohnt sich ein dynamischer Stromtarif?", "fuer-wen", f"""
<p>Der Preisvorteil entsteht nur, wenn Sie Verbrauch in günstige Stunden verschieben können. Deshalb
lohnt sich ein dynamischer Tarif besonders für:</p>
<ul>
  <li><b>Wärmepumpen-Haushalte:</b> Wärme und Warmwasser lassen sich in günstige Zeitfenster legen, das
  Gebäude und der Pufferspeicher halten die Wärme über die teuren Abendstunden.</li>
  <li><b>E-Auto-Besitzer:</b> Das Laden wird automatisch in die billigsten Stunden verschoben, meist
  nachts.</li>
  <li><b>Haushalte mit {a('batteriespeicher', 'Batteriespeicher')}:</b> Der Speicher lädt günstig aus dem
  Netz oder aus der PV-Anlage und versorgt Sie in teuren Stunden.</li>
  <li><b>PV-Anlagen:</b> In Kombination mit Eigenverbrauch und Speicher wird der Reststrom, den Sie
  zukaufen müssen, in die günstigen Stunden gelegt.</li>
</ul>
<p>Ehrlich gesagt: Wer keinen flexiblen Verbrauch hat und den Strom nicht verschieben kann, spart mit
einem dynamischen Tarif wenig. Die Flexibilität ist der entscheidende Hebel, nicht der Tarif selbst.</p>
"""),
        ("Chancen und Risiken im Überblick", "vergleich", f"""
{A.table(
    ["Merkmal", "Fixtarif", "Dynamischer Tarif"],
    [
        ["Preis pro kWh", "konstant", "stündlich schwankend"],
        ["Sparpotenzial", "gering", "hoch bei flexiblem Verbrauch"],
        ["Planbarkeit", "hoch", "geringer (Preisspitzen möglich)"],
        ["Ideal für", "starre Verbraucher", "Wärmepumpe, E-Auto, Speicher"],
        ["Voraussetzung", "keine besondere", "Smart Meter mit aktiver Datenübertragung"],
        ["Aufwand", "keiner", "ohne EMS: täglich Preise prüfen; mit EMS: keiner"],
    ],
    hl_cols=(2,),
)}
{A.box("Der Preis kann in Spitzenzeiten deutlich höher liegen als bei einem Fixtarif. Wer abends kocht, "
       "wäscht und das E-Auto lädt, zahlt dann mehr. Das Risiko lässt sich stark reduzieren, indem ein "
       "Energiemanagementsystem flexible Verbraucher automatisch in günstige Stunden verschiebt und teure "
       "Stunden meidet.", label="Risiko Preisspitzen:")}
"""),
        ("Voraussetzung: Smart Meter mit aktiver Datenübertragung", "voraussetzung", f"""
<p>Damit der Lieferant stundengenau abrechnen kann, braucht er die Viertelstundenwerte Ihres
{a('/smart-meter/', 'Smart Meters')}. Der Rollout läuft in Österreich gesetzlich vorgeschrieben, der
Tausch erfolgt durch den Netzbetreiber ohne gesonderte Kosten. Wichtig: Beim
{a('/smart-meter-opt-out/', 'Opt-out')} überträgt der Zähler nur einen Jahreswert, ein dynamischer Tarif
ist dann nicht sinnvoll nutzbar. Wer den Opt-out gewählt hat, kann beim Netzbetreiber in der Regel wieder
auf die Standardkonfiguration wechseln.</p>
<p>Zweite Voraussetzung ist ein Anbieter, der dynamische Tarife anbietet. Prüfen Sie dabei neben dem
Börsenpreis auch die fixen Bestandteile: Netzentgelte, Abgaben und Steuern bleiben unabhängig vom
Tarif gleich, verhandelt wird nur der Energiepreis.</p>
"""),
        ("So automatisiert ein Energiemanagementsystem das Sparen", "ems", f"""
<p>Sie müssen nicht selbst ständig auf die Strompreise schauen. Genau das übernimmt ein
{a('ems', 'Energiemanagementsystem')}: Es kennt die Preise für die kommenden Stunden und verschiebt
flexible Verbraucher automatisch in die günstigsten Fenster, während teure Stunden gemieden werden. So
nutzen Sie die Vorteile eines dynamischen Tarifs, ohne das Risiko der Preisspitzen voll zu tragen.</p>
{A.net([
    ("☀", "PV-Anlage", "Eigenverbrauch hat immer Vorrang"),
    ("▮", "Batteriespeicher", "lädt bei Niedrigpreis, entlädt bei Hochpreis"),
    ("♨", "Wärmepumpe", "heizt und bereitet Warmwasser in günstigen Stunden"),
    ("⌖", "Wallbox", "lädt das E-Auto in den billigsten Nachtstunden"),
], "Das EMS kennt den Preis von morgen",
   "Es verarbeitet die Börsenpreise, misst Bezug und Einspeisung am Smart Meter und steuert die Verbraucher "
   "lokal, auch ohne Internet.")}
<p>Seit Juni 2026 fördert der Klima- und Energiefonds solche Systeme: Private Haushalte erhalten
50 Prozent der Kosten, maximal 600 Euro. Eine der sechs Verpflichtungsoptionen ist genau der dynamische
Liefervertrag. Voraussetzungen und Ablauf finden Sie im Ratgeber
{a('/ems-foerderung/', 'EMS-Förderung 2026')}.</p>
{A.cta("Dynamische Tarife automatisch nutzen",
       "Wir zeigen Ihnen kostenlos, wie ein Energiemanagementsystem Ihren Verbrauch in die günstigsten "
       "Stunden verschiebt, und ob sich ein dynamischer Tarif bei Ihrem Profil rechnet.",
       secondary=("ems", "Zum Energiemanagementsystem"))}
"""),
        ("Dynamischer Tarif und PV-Einspeisung", "einspeisung", f"""
<p>Der Börsenpreis wirkt in beide Richtungen. Wer PV-Strom einspeist, bekommt beim
{a('/oemag-einspeisetarif/', 'OeMAG-Marktpreis')} einen Tarif, der ebenfalls dem Börsenpreis zu den
Einspeisestunden folgt: Im Juli 2026 lag er bei 6,146 Cent je Kilowattstunde, weil die Mittagspreise
wegen des vielen Solarstroms niedrig sind. Genau diese günstigen Mittagsstunden sind beim dynamischen
Bezugstarif Ihr Vorteil. Die Konsequenz für PV-Haushalte: möglichst viel selbst verbrauchen, den Rest
über den Speicher in den Abend retten und Zukauf in die günstigen Stunden legen. Mehr dazu im
{a('/marktpreis-2026/', 'Marktpreis-Überblick 2026')}.</p>
"""),
        ("Fazit", "fazit", f"""
<p>Ein dynamischer Stromtarif kann bares Geld sparen, aber nur, wenn Sie Verbrauch flexibel verschieben
können. Mit Wärmepumpe, E-Auto oder Speicher und einem Energiemanagementsystem, das die günstigen Stunden
automatisch nutzt, wird aus dem schwankenden Börsenpreis ein klarer Vorteil. Ohne Flexibilität bleibt ein
{a('/flexibler-stromtarif/', 'flexibler Tarif')} oder ein Fixtarif die sicherere Wahl.</p>
{A.cta("Spotpreise automatisch ausnutzen",
       "Kostenlose Erstberatung: Wir rechnen mit Ihrem Verbrauchsprofil, ob sich ein dynamischer Tarif "
       "lohnt und welche Technik dafür nötig ist.",
       primary=("kontakt", "Kostenlose Beratung anfragen"), secondary=("batteriespeicher", "Zum Batteriespeicher"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Tarif und Technik: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("Ein dynamischer Tarif entfaltet seinen Wert erst mit der richtigen Technik. EBZ Energie aus "
                 "Villach verbindet als herstellerunabhängiger Fachbetrieb Ihre PV-Anlage, Ihren Speicher, "
                 "Ihre Wärmepumpe und Ihre Wallbox über ein Energiemanagementsystem, das den dynamischen "
                 "Tarif automatisch ausnutzt. Planung und Installation übernehmen wir in Kärnten und der "
                 "Steiermark aus einer Hand, mit einem festangestellten Team aus zertifizierten Fachkräften."),
        "grid": [
            ("Tarifcheck", "Wir rechnen, ob dynamisch, flexibel oder fix zu Ihrem Profil passt."),
            ("Förderfähiges EMS", "Systeme, die Preissignale verarbeiten und lokal steuern."),
            ("Speicher richtig dimensioniert", "Damit Niedrigpreisstunden auch genutzt werden können."),
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EMS vom selben Team."),
        ],
    },

    "faq": [
        ("Was ist ein dynamischer Stromtarif?",
         "Bei einem dynamischen Stromtarif richtet sich der Strompreis nach dem aktuellen Börsenpreis und "
         "ändert sich meist stündlich. Statt eines festen Preises pro Kilowattstunde zahlen Sie 24 "
         "verschiedene Preise pro Tag, je nachdem, wie viel Strom gerade verfügbar und nachgefragt ist."),
        ("Für wen lohnt sich ein dynamischer Stromtarif?",
         "Vor allem für Haushalte und Betriebe mit flexiblen Verbrauchern wie Wärmepumpe, E-Auto oder "
         "Batteriespeicher. Wer einen großen Teil seines Verbrauchs in günstige Stunden verschieben kann, "
         "spart am meisten. Ohne Flexibilität ist der Vorteil begrenzt."),
        ("Welche Voraussetzungen brauche ich?",
         "Sie benötigen einen Smart Meter mit aktiver Datenübertragung, also ohne Opt-out, und einen "
         "Anbieter, der dynamische Tarife anbietet. Für den maximalen Nutzen empfiehlt sich ein "
         "Energiemanagementsystem, das den Verbrauch automatisch steuert."),
        ("Ist ein dynamischer Tarif nicht riskant?",
         "Der Preis kann in Spitzenzeiten, meist am Abend, deutlich höher liegen als bei einem Fixtarif. Das "
         "Risiko lässt sich stark reduzieren, indem ein Energiemanagementsystem flexible Verbraucher "
         "automatisch in günstige Stunden verschiebt und teure Stunden meidet."),
        ("Was ist der Unterschied zu einem flexiblen Stromtarif?",
         "Ein dynamischer Tarif bildet den Börsenpreis stündlich ab und braucht einen Smart Meter. Ein "
         "flexibler oder variabler Tarif ist der Oberbegriff für marktorientierte Tarife und passt den Preis "
         "seltener an, etwa monatlich, meist ohne Smart Meter. Mehr dazu im Ratgeber zum flexiblen Stromtarif."),
        ("Wann ist Strom bei einem dynamischen Tarif am günstigsten?",
         "In der Regel nachts, wenn wenig nachgefragt wird, und mittags, wenn viel Solarstrom im Netz ist. Am "
         "teuersten ist er typischerweise am Abend zwischen 17 und 21 Uhr. Die genauen Preise "
         "veröffentlicht der Lieferant meist am Vortag."),
        ("Wird ein Energiemanagementsystem für dynamische Tarife gefördert?",
         "Ja. Der Klima- und Energiefonds fördert seit Juni 2026 Energiemanagementsysteme für Haushalte mit "
         "50 Prozent, maximal 600 Euro. Der dynamische Liefervertrag ist eine der sechs Optionen für die "
         "fünfjährige Betriebsverpflichtung."),
        ("Brauche ich für einen dynamischen Tarif eine PV-Anlage?",
         "Nein. Ein dynamischer Tarif funktioniert auch ohne PV, entscheidend sind flexible Verbraucher. "
         "Mit PV-Anlage und Speicher steigt der Nutzen aber, weil Sie mittags eigenen Strom nutzen und den "
         "Zukauf in günstige Stunden legen."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Photovoltaik, Speicher, Wärmepumpen und Energiemanagementsysteme in Kärnten und der "
                    "Steiermark und richtet die Steuerung auf dynamische Tarife aus. Tarifbedingungen und "
                    "Preise unterscheiden sich je nach Lieferant, maßgeblich sind dessen Angaben und die "
                    "Informationen der E-Control."),
    "sources": [
        ("E-Control: Regulierungsbehörde für Strom und Gas", "https://www.e-control.at/"),
        ("oesterreich.gv.at: Informationen zu Strom und Smart Meter", "https://www.oesterreich.gv.at/"),
    ],
    "related": [
        ("/flexibler-stromtarif/", "Flexibler Stromtarif: Fix, flexibel und dynamisch im Vergleich"),
        ("/smart-meter/", "Smart Meter in Österreich: die technische Voraussetzung"),
        ("/ems-foerderung/", "EMS-Förderung 2026: bis zu 600 Euro"),
        ("ems", "Energiemanagementsystem: Funktion und Nutzen"),
    ],
    "cta": {
        "h3": "Dynamische Tarife automatisch nutzen",
        "text": "Wir zeigen Ihnen kostenlos, wie ein EMS Ihren Verbrauch in die günstigsten Stunden verschiebt.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Spotpreise automatisch ausnutzen",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Tarif, Speicher "
                   "und Energiemanagement aufeinander abstimmt."),
}
