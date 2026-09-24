"""Ratgeber: Smart Meter in Österreich (Funktion, Rollout, Nutzen).

Migriert von ebz-photovoltaik.at/smart-meter/ (Stand der Quelle: Juli 2026).
Hub-Artikel des Clusters Smart Meter und Stromtarife. Inhalte aus den
Cluster-Quellen (Was ist ein Smart Meter, Auslesen, Opt-out, Tarife, ElWG).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "smart-meter",
    "path": "/smart-meter/",
    "title": "Smart Meter Österreich: Funktion, Rollout, Nutzen | EBZ",
    "description": ("Smart Meter in Österreich: Messung alle 15 Minuten, Rollout ohne Extrakosten, Opt-out, "
                    "Datenschutz und Nutzen für PV, dynamischen Tarif und EMS."),
    "eyebrow": "Smart Meter · Grundlagen",
    "crumb_label": "Smart Meter in Österreich",
    "h1": "Smart Meter in Österreich: Funktion, Rollout und Nutzen für Ihre PV-Anlage",
    "lead": ("Der Smart Meter ersetzt Schritt für Schritt den alten Stromzähler und misst Ihren Verbrauch "
             "in Viertelstunden statt einmal im Jahr. Er ist die technische Voraussetzung für dynamische "
             "Tarife, Energiegemeinschaften und ein Energiemanagementsystem."),
    "chips": [
        "Messung: <b>alle 15 Minuten</b>",
        "Rollout: <b>gesetzlich vorgeschrieben</b>",
        "Zähler: <b>keine Extrakosten</b>",
        "Opt-out: <b>möglich</b>",
    ],
    "date_published": "2026-07-05",
    "date_modified": "2026-09-24",
    "hero_img": "ems",
    "hero_alt": "Energiemanagementsystem verbindet Smart Meter, Photovoltaik, Speicher und Wärmepumpe im Eigenheim",

    "tldr": [
        "Ein Smart Meter ist ein digitaler, fernauslesbarer Stromzähler. Er erfasst Ihren Verbrauch "
        "viertelstündlich und übermittelt die Werte verschlüsselt an den Netzbetreiber, statt einmal im "
        "Jahr abgelesen zu werden.",
        "In Österreich ist der Rollout gesetzlich vorgeschrieben. Der Tausch erfolgt durch den "
        "Netzbetreiber, für den Zähler selbst fallen keine gesonderten Anschaffungskosten an.",
        "Ein Opt-out ist möglich: Der Zähler wird trotzdem installiert, überträgt dann aber nur einen "
        "Jahreswert statt Viertelstundenwerte. Ein vollständiges Ablehnen des Geräts ist nicht vorgesehen.",
        "Der eigentliche Nutzen liegt in dem, was der Zähler möglich macht: dynamische Stromtarife, das "
        "Teilen von Strom in einer Energiegemeinschaft und ein Energiemanagementsystem, das Verbrauch in "
        "günstige und sonnenreiche Stunden verschiebt.",
    ],
    "kpis": [
        ("15 Min.", "Messintervall des Smart Meters"),
        ("1x jährlich", "Ablesung beim alten Ferraris-Zähler"),
        ("0 €", "gesonderte Kosten für den Zählertausch"),
        ("4", "Anwendungen: Tarif, EMS, EG, Transparenz"),
    ],

    "sections": [
        ("Was ist ein Smart Meter?", "was-ist", f"""
<p>Ein Smart Meter (deutsch: intelligenter Stromzähler) ist ein digitaler, fernauslesbarer Stromzähler.
Er misst Ihren Stromverbrauch in kurzen Intervallen, standardmäßig alle 15 Minuten, und übermittelt die
Werte automatisch an den Netzbetreiber. Der alte, mechanische Ferraris-Zähler wurde dagegen einmal im
Jahr abgelesen und lieferte eine einzige Zahl: den Jahresverbrauch.</p>
<p>Bei einer {a('photovoltaik', 'Photovoltaikanlage')} erfasst der Smart Meter zusätzlich, wie viel Strom
Sie ins Netz einspeisen. So entsteht ein genaues Bild von Erzeugung und Verbrauch, die Grundlage, um den
Eigenverbrauch gezielt zu steigern. Damit ist der Smart Meter weit mehr als ein neuer Zähler: Er ist die
digitale Basis, auf der moderne Stromtarife, Energiegemeinschaften und ein Energiemanagementsystem
überhaupt erst funktionieren. Eine kompakte Erklärung ohne Fachbegriffe finden Sie im Ratgeber
{a('/was-ist-ein-smart-meter/', 'Was ist ein Smart Meter? Einfach erklärt')}.</p>
{A.table(
    ["Merkmal", "Alter Ferraris-Zähler", "Smart Meter"],
    [
        ["Ablesung", "einmal jährlich, oft manuell", "automatisch, tagesaktuell"],
        ["Auflösung", "Jahresverbrauch", "Viertelstundenwerte"],
        ["Einspeisung", "separater Zähler nötig", "Bezug und Einspeisung im selben Gerät"],
        ["Datenzugang", "keiner", "Online-Portal des Netzbetreibers"],
        ["Dynamische Tarife", "nicht möglich", "Grundvoraussetzung"],
        ["Steuerung per EMS", "nicht möglich", "möglich"],
    ],
    hl_cols=(2,),
)}
"""),
        ("Wie funktioniert ein Smart Meter?", "funktion", f"""
<p>Der Weg der Daten läuft vollautomatisch ab und besteht aus vier Schritten:</p>
{A.steps([
    ("Messung im Haushalt",
     "Der Smart Meter erfasst Ihren Stromverbrauch laufend, standardmäßig in Viertelstundenwerten. Bei "
     "PV-Anlagen zählt er Bezug und Einspeisung getrennt."),
    ("Übertragung an den Netzbetreiber",
     "Die Werte werden verschlüsselt an Ihren Netzbetreiber übermittelt. Ein manuelles Ablesen oder der "
     "Besuch eines Ablesers entfällt."),
    ("Anzeige im Kundenportal",
     "Im Online-Portal Ihres Netzbetreibers sehen Sie Ihren Verbrauch tagesaktuell nach Tag, Monat oder "
     "Viertelstunde und erkennen Muster, etwa die Grundlast in der Nacht."),
    ("Nutzung für Tarif und EMS",
     "Auf dieser Datenbasis funktionieren dynamische Stromtarife, die Abrechnung in einer "
     "Energiegemeinschaft und die automatische Steuerung durch ein Energiemanagementsystem."),
])}
<p>Wichtig für die Praxis: Das Portal betreibt Ihr Netzbetreiber, also das Unternehmen, das die
Stromleitungen in Ihrer Region betreibt. Das ist nicht zwingend Ihr Stromlieferant, bei dem Sie den
Tarif abgeschlossen haben. Für die Registrierung brauchen Sie meist Ihre Zählpunktnummer von der
Stromrechnung. Die Schritte im Detail zeigt der Ratgeber
{a('/smart-meter-auslesen/', 'Smart Meter auslesen')}.</p>
"""),
        ("Smart-Meter-Rollout in Österreich", "rollout", f"""
<p>In Österreich ist der Umstieg auf Smart Meter gesetzlich vorgeschrieben. Die Netzbetreiber tauschen
die alten Zähler flächendeckend gegen digitale Geräte aus und statten den Großteil der Zählpunkte mit
Smart Metern aus. Für Sie als Kundin oder Kunde entstehen dadurch keine gesonderten Anschaffungskosten:
Der Tausch erfolgt durch den Netzbetreiber, die Kosten für die Messeinrichtung sind wie bisher über die
Netzentgelte abgedeckt.</p>
<p>Mit dem neuen Elektrizitätswirtschaftsgesetz (ElWG), das der Nationalrat im Dezember 2025 beschlossen
hat, gelten zudem gesetzliche Fristen für Netzbetreiber. Das betrifft auch den Zählertausch, auf den
Anlagenbetreiber früher oft monatelang warten mussten. Neu errichtete PV-Anlagen müssen
kommunikationsfähig sein, der Smart Meter ist dafür der Ausgangspunkt. Details lesen Sie im Ratgeber
{a('/elwg-beschluss-oesterreich/', 'ElWG-Beschluss: Was PV-Betreiber wissen müssen')}.</p>
{A.box("Sie können einen sogenannten Opt-out wählen. Der digitale Zähler wird zwar installiert, überträgt "
       "Ihre Verbrauchswerte dann aber nur eingeschränkt, etwa als Jahreswert statt viertelstündlich. Ein "
       "vollständiges Ablehnen des Geräts ist in Österreich nicht vorgesehen. Was der Opt-out für Tarife "
       "und Energiemanagement bedeutet, erklärt der Ratgeber "
       + a('/smart-meter-opt-out/', 'Smart Meter Opt-out') + ".", label="Opt-out:")}
"""),
        ("Welchen Nutzen bringt der Smart Meter?", "nutzen", f"""
<p>Der Smart Meter selbst spart noch kein Geld. Sein Wert liegt darin, was er möglich macht:</p>
<ul>
  <li><b>Transparenz:</b> Sie sehen, wann und wofür Sie Strom verbrauchen, und decken Stromfresser auf,
  etwa eine hohe Grundlast in der Nacht oder alte Geräte im Dauerbetrieb.</li>
  <li><b>Dynamische Tarife:</b> Erst mit Smart Meter und aktiver Datenübertragung können Sie einen
  {a('/dynamischer-stromtarif/', 'dynamischen Stromtarif')} nutzen und Strom dann beziehen, wenn er an
  der Börse günstig ist, meist nachts und mittags bei viel Sonne.</li>
  <li><b>Höherer PV-Eigenverbrauch:</b> In Kombination mit einem
  {a('ems', 'Energiemanagementsystem')} lässt sich der Eigenverbrauch Ihrer Photovoltaikanlage deutlich
  steigern, weil Speicher, Wärmepumpe und Wallbox automatisch in sonnenreiche Stunden gelegt werden.</li>
  <li><b>Grundlage für die Energiegemeinschaft:</b> Auch das Teilen von Strom in einer
  {a('eg', 'Energiegemeinschaft')} setzt einen Smart Meter mit Viertelstundenwerten voraus, weil nur so
  zugeordnet werden kann, wer wann welchen Strom bezogen hat.</li>
</ul>
{A.net([
    ("☀", "PV-Anlage", "Einspeisung wird viertelstündlich erfasst"),
    ("▮", "Batteriespeicher", "lädt nach Preis und Sonnenangebot"),
    ("♨", "Wärmepumpe", "heizt in günstigen Stunden vor"),
    ("⌖", "Wallbox", "lädt das E-Auto zu Niedrigpreiszeiten"),
], "Smart Meter plus Energiemanagementsystem",
   "Der Smart Meter liefert die Messwerte, das EMS trifft auf dieser Basis die Entscheidungen: speichern, "
   "verbrauchen oder einspeisen.")}
"""),
        ("Smart Meter und dynamischer Stromtarif", "tarife", f"""
<p>Bei einem dynamischen Stromtarif richtet sich der Preis pro Kilowattstunde nach dem aktuellen
Börsenpreis und ändert sich in der Regel stündlich. Damit der Lieferant Ihren Verbrauch stundengenau
abrechnen kann, braucht er die Viertelstundenwerte des Smart Meters. Ohne aktive Datenübertragung ist
ein dynamischer Tarif deshalb nicht sinnvoll nutzbar.</p>
<p>Lohnend ist ein solcher Tarif vor allem für flexible Verbraucher: Wärmepumpe, E-Auto und
{a('batteriespeicher', 'Batteriespeicher')} lassen sich in günstige Stunden verschieben. Wer keinen
verschiebbaren Verbrauch hat, spart wenig. Ein Mittelweg ist ein
{a('/flexibler-stromtarif/', 'flexibler Stromtarif')}, der den Preis seltener anpasst, etwa monatlich, und
dafür meist keinen Smart Meter voraussetzt.</p>
{A.cta("Smart Meter, PV und EMS sinnvoll kombinieren",
       "Wir analysieren kostenlos Ihr Verbrauchsprofil und zeigen, welche Kombination aus Tarif, Speicher "
       "und Energiemanagement bei Ihnen am meisten spart.",
       secondary=("ems", "Zum Energiemanagementsystem"))}
"""),
        ("Datenschutz: Wer sieht meine Verbrauchsdaten?", "datenschutz", f"""
<p>Die Erfassung, Übertragung und Speicherung der Verbrauchsdaten ist gesetzlich geregelt. Die Werte
werden verschlüsselt an den Netzbetreiber übertragen und stehen Ihnen im Kundenportal zur Verfügung.
Wer die häufige Datenübertragung grundsätzlich nicht möchte, kann den Opt-out nutzen und die
Übermittlung auf ein Minimum reduzieren.</p>
<p>Die Kehrseite: Sowohl ein dynamischer Stromtarif als auch ein Energiemanagementsystem brauchen
feingranulare Daten, um Verbrauch und Ladevorgänge in die günstigsten Zeitfenster zu legen. Mit
Opt-out fällt dieser Hebel weitgehend weg. In der Regel lässt sich die Entscheidung später wieder
ändern, etwa wenn Sie doch einen dynamischen Tarif nutzen möchten.</p>
{A.table(
    ["Merkmal", "Standard-Konfiguration", "Opt-out"],
    [
        ["Zähler", "digital", "digital"],
        ["Datenübertragung", "viertelstündlich", "stark reduziert (z. B. jährlich)"],
        ["Verbrauch im Portal", "tagesaktuell und fein", "nur eingeschränkt"],
        ["Dynamischer Tarif", "sinnvoll nutzbar", "kaum nutzbar"],
        ["Energiegemeinschaft", "Zuordnung möglich", "nicht möglich"],
        ["Energiemanagement", "optimale Datenbasis", "eingeschränkte Optimierung"],
    ],
    hl_cols=(1,),
)}
"""),
        ("Smart Meter und EMS-Förderung 2026", "foerderung", f"""
<p>Wer den Smart Meter mit einem Energiemanagementsystem verbindet, kann seit Juni 2026 eine Förderung
des Klima- und Energiefonds nutzen: Private Haushalte erhalten 50 Prozent der Kosten, maximal 600 Euro,
wenn das EMS mindestens zwei Komponenten wie PV-Anlage, Speicher, Wärmepumpe oder Wallbox aktiv steuert,
Preissignale verarbeitet und Bezug sowie Einspeisung am Netzanschluss misst. Eine der sechs
Verpflichtungsoptionen ist ein dynamischer Liefervertrag, eine andere die Teilnahme an einer
Energiegemeinschaft. Voraussetzungen, Fristen und Ablauf finden Sie im Ratgeber
{a('/ems-foerderung/', 'EMS-Förderung 2026')}.</p>
"""),
        ("Fazit: Der Smart Meter ist der Startpunkt, nicht das Ziel", "fazit", f"""
<p>Der Smart Meter ersetzt den alten Zähler und macht Ihren Verbrauch transparent. Sein volles Potenzial
entfaltet er erst im Zusammenspiel mit einem dynamischen Stromtarif, einer Energiegemeinschaft und einem
Energiemanagementsystem. Dann wird aus reiner Messung echte Ersparnis, weil Sie Strom gezielt dann
verbrauchen und speichern, wenn er am günstigsten ist.</p>
{A.cta("Mehr aus Ihrem Smart Meter herausholen",
       "Kostenlose Analyse Ihres Verbrauchsprofils, Auswahl des passenden Energiemanagementsystems und "
       "Installation durch zertifizierte Fachkräfte aus Villach.",
       primary=("kontakt", "Kostenlose Beratung anfragen"), secondary=("photovoltaik", "Zur Photovoltaik"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner rund um Smart Meter und Photovoltaik: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("Ein Smart Meter liefert Daten. Damit daraus Ersparnis wird, braucht es die richtige Technik "
                 "dahinter. EBZ Energie aus Villach verbindet als herstellerunabhängiger Fachbetrieb Ihren "
                 "Smart Meter über ein Energiemanagementsystem mit PV-Anlage, Speicher, Wärmepumpe und "
                 "Wallbox und übernimmt Planung und Installation in Kärnten und der Steiermark aus einer Hand."),
        "grid": [
            ("Verbrauchsanalyse", "Kostenlose Auswertung Ihres Verbrauchsprofils und Ihrer Anlage."),
            ("Passendes EMS", "Auswahl und Einbindung eines förderfähigen Energiemanagementsystems."),
            ("Zertifizierte Fachkräfte", "Installation durch das festangestellte Team aus Villach."),
            ("Tarifberatung", "Welcher Tarif zu Ihrem Verbrauch passt und wie Sie die Daten nutzen."),
        ],
    },

    "faq": [
        ("Was ist ein Smart Meter?",
         "Ein Smart Meter ist ein digitaler, fernauslesbarer Stromzähler. Er erfasst den Verbrauch in "
         "Viertelstundenwerten und übermittelt sie verschlüsselt an den Netzbetreiber. Im Kundenportal sehen "
         "Sie Ihren Verbrauch tagesaktuell, statt einmal im Jahr abzulesen."),
        ("Ist der Smart Meter in Österreich Pflicht?",
         "Der Rollout ist gesetzlich vorgeschrieben, die Netzbetreiber statten den Großteil der Zählpunkte "
         "mit digitalen Zählern aus. Sie können einen Opt-out wählen: Das Gerät wird installiert, überträgt "
         "dann aber nur einen Jahreswert. Ein vollständiges Ablehnen des Geräts ist nicht vorgesehen."),
        ("Kostet mich der Smart Meter extra?",
         "Nein. Für den Zähler fallen keine gesonderten Anschaffungskosten an, er wird vom Netzbetreiber "
         "getauscht. Die Kosten der Messeinrichtung sind wie bisher über die Netzentgelte abgedeckt."),
        ("Wie kann ich meinen Smart Meter auslesen?",
         "Am einfachsten im Online-Portal Ihres Netzbetreibers: registrieren mit der Zählpunktnummer von der "
         "Stromrechnung, einloggen, Verbrauch nach Tag, Monat oder Viertelstunde ansehen. Zusätzlich zeigt "
         "das Display am Zähler Zählerstand und momentane Leistung an."),
        ("Ist der Smart Meter beim Datenschutz sicher?",
         "Die Übertragung und Speicherung der Verbrauchsdaten ist gesetzlich geregelt, die Übermittlung "
         "erfolgt verschlüsselt. Wer die viertelstündliche Übertragung nicht möchte, kann den Opt-out beim "
         "Netzbetreiber beantragen."),
        ("Brauche ich für eine Energiegemeinschaft einen Smart Meter?",
         "Ja. Die Energiegemeinschaft ordnet den erzeugten Strom viertelstundengenau den Mitgliedern zu, die "
         "ihn zeitgleich verbrauchen. Ohne Smart Meter mit aktiver Datenübertragung ist diese Zuordnung "
         "nicht möglich."),
        ("Brauche ich für einen dynamischen Stromtarif einen Smart Meter?",
         "Ja. Ein dynamischer Tarif rechnet stundengenau nach dem Börsenpreis ab und braucht dafür die "
         "Viertelstundenwerte des Smart Meters mit aktiver Datenübertragung. Ein flexibler Tarif mit "
         "monatlicher Preisanpassung kommt dagegen meist ohne Smart Meter aus."),
        ("Was bringt mir ein Smart Meter konkret?",
         "Er schafft Transparenz über Ihren Verbrauch und ist die Voraussetzung für dynamische Tarife, "
         "Energiegemeinschaften und ein Energiemanagementsystem. Erst damit lässt sich Strom gezielt dann "
         "verbrauchen, wenn er am günstigsten ist, und der Eigenverbrauch einer PV-Anlage deutlich steigern."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Photovoltaik, Speicher, Wärmepumpen und Energiemanagementsysteme in Kärnten und der "
                    "Steiermark und verbindet Smart-Meter-Daten mit der Anlagentechnik. Angaben zu Rollout "
                    "und Opt-out beruhen auf den Informationen von E-Control und oesterreich.gv.at, "
                    "maßgeblich sind die Bedingungen Ihres Netzbetreibers."),
    "sources": [
        ("E-Control: Regulierungsbehörde für Strom und Gas", "https://www.e-control.at/"),
        ("oesterreich.gv.at: Informationen zum Smart Meter", "https://www.oesterreich.gv.at/"),
    ],
    "related": [
        ("/was-ist-ein-smart-meter/", "Was ist ein Smart Meter? Einfach erklärt"),
        ("/smart-meter-auslesen/", "Smart Meter auslesen: So sehen Sie Ihren Verbrauch"),
        ("/dynamischer-stromtarif/", "Dynamischer Stromtarif: Wann sich Spotpreise lohnen"),
        ("ems", "Energiemanagementsystem: Funktion und Nutzen"),
    ],
    "cta": {
        "h3": "Aus Verbrauchsdaten wird Ersparnis",
        "text": "Wir zeigen Ihnen kostenlos, wie Smart Meter, PV-Anlage und Energiemanagement zusammenspielen.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Machen Sie aus Ihren Verbrauchsdaten echte Ersparnis",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Smart Meter, "
                   "PV-Anlage und Energiemanagement aus einer Hand verbindet."),
}
