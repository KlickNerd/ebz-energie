"""Ratgeber: Marktpreis 2026 (Lohnt sich Photovoltaik noch?).

Migriert von ebz-photovoltaik.at/marktpreis-2026/ (Stand der Quelle: Dezember 2025).
Aktualisiert mit den OeMAG-Werten Stand September 2026: PV-Marktpreis Juli 2026
6,146 ct/kWh (gesetzliche Untergrenze), Q3-2026-Quartalsmarktpreis der E-Control
10,923 ct/kWh. Historische Werte der Quelle (Q4 2025: 9,17 ct) bleiben als Verlauf.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "marktpreis-2026",
    "path": "/marktpreis-2026/",
    "title": "Marktpreis 2026: Lohnt sich Photovoltaik noch? | EBZ Energie",
    "description": ("OeMAG-Marktpreis Juli 2026: 6,146 ct/kWh, Q3-Marktpreis 10,923 ct. Warum Eigenverbrauch "
                    "die Einspeisung schlägt und wie sich PV mit Speicher 2026 noch rechnet."),
    "eyebrow": "Markt · Einspeisetarif und Förderung",
    "crumb_label": "Marktpreis 2026",
    "h1": "Marktpreis 2026: Lohnt sich Photovoltaik bei 6,146 Cent Einspeisetarif noch?",
    "lead": ("Der OeMAG-Marktpreis für PV-Strom lag im Juli 2026 bei 6,146 Cent je Kilowattstunde, der "
             "Netzbezug kostet rund 30 Cent. Diese Schere entscheidet über die Strategie: Nicht die "
             "Einspeisung bringt die Rendite, sondern jede selbst verbrauchte Kilowattstunde."),
    "chips": [
        "OeMAG Juli 2026: <b>6,146 ct/kWh</b>",
        "Q3-Marktpreis: <b>10,923 ct/kWh</b>",
        "Netzbezug: <b>rund 30 ct/kWh</b>*",
        "Förderung: <b>EAG-Calls 2026</b>",
    ],
    "date_published": "2025-12-10",
    "date_modified": "2026-09-24",
    "hero_img": "pv_card",
    "hero_alt": "Photovoltaikanlage von EBZ Energie auf einem Wohnhausdach in Kärnten",

    "tldr": [
        "Stand September 2026: Der OeMAG-Marktpreis für Photovoltaik lag im Juli 2026 bei 6,146 Cent je "
        "Kilowattstunde, das ist die gesetzliche Untergrenze von 60 Prozent des Quartalsmarktpreises der "
        "E-Control (Q3 2026: 10,923 Cent). Im 4. Quartal 2025 lag der Marktpreis noch bei 9,17 Cent.",
        "Netzbezug kostet inklusive Netzentgelten, Abgaben und Steuern im Schnitt rund 30 bis 35 Cent je "
        "Kilowattstunde*. Die Differenz zur Einspeisung beträgt damit über 24 Cent: Eigenverbrauch schlägt "
        "Einspeisung um ein Vielfaches.",
        "Mit dem Bundesgesetzblatt I Nr. 69/2025 ist die EAG-Novelle kundgemacht: Statt des Nullsteuersatzes, "
        "der im April 2025 ausgelaufen ist, gibt es 2026 wieder Investitionszuschüsse über Fördercalls.",
        "Ohne Speicher nutzen typische Haushalte nur rund 30 Prozent ihres Solarstroms selbst, mit passend "
        "dimensioniertem Speicher 70 bis 80 Prozent*. Der Speicher ist damit der Rendite-Hebel.",
        "Wer wartet, spart nicht: Hardware ist günstig, Lohnkosten steigen, und Netzkapazitäten in Kärnten "
        "und der Steiermark werden knapper.",
    ],
    "kpis": [
        ("6,146 ct", "OeMAG-Marktpreis PV, Juli 2026"),
        ("10,923 ct", "Quartalsmarktpreis E-Control, Q3 2026"),
        ("30 bis 35 ct", "Netzbezug je kWh inkl. Abgaben*"),
        ("70 bis 80 %", "Eigenverbrauch mit Speicher*"),
    ],

    "sections": [
        ("Der Marktpreis 2026: aktuelle Werte und Verlauf", "marktpreis", f"""
<p>Die OeMAG (Abwicklungsstelle für Ökostrom AG) ist gesetzlich verpflichtet, Strom aus PV-Anlagen zum
sogenannten Marktpreis abzunehmen. Dieser Preis wird monatlich im Nachhinein aus den Börsenpreisen zu
den Einspeisestunden berechnet und in einen Korridor gezwängt: nach oben begrenzt durch den
Quartalsmarktpreis der E-Control, nach unten durch 60 Prozent davon.</p>
<p><b>Stand September 2026:</b> Für Juli 2026 beträgt der OeMAG-Marktpreis für Photovoltaik 6,146 Cent
je Kilowattstunde. Das ist die Untergrenze, weil die Börsenpreise zur Mittagszeit wegen des vielen
Solarstroms seit dem Frühjahr darunter liegen. Der Quartalsmarktpreis der E-Control für das dritte
Quartal 2026 liegt bei 10,923 Cent (109,23 Euro je MWh).</p>
{A.table(
    ["Zeitraum", "Wert", "Einordnung"],
    [
        ["2019 (vor der Krise)", "3 bis 4 ct/kWh", "langjähriges Niveau"],
        ["2022/23 (Energiekrise)", "30 bis 40 ct/kWh", "historische Ausnahme"],
        ["Q4 2025 (Quartalsmarktpreis)", "9,17 ct/kWh", "Stand bei Erstveröffentlichung dieses Artikels"],
        ["Q3 2026 (Quartalsmarktpreis E-Control)", "10,923 ct/kWh", "Obergrenze für den OeMAG-Tarif"],
        ["Juli 2026 (OeMAG-Marktpreis PV)", "6,146 ct/kWh", "gesetzliche Untergrenze (60 %)"],
    ],
    hl_cols=(1,),
)}
<p>Die Ära der Krisenpreise ist vorbei, und der Trend zeigt für PV-Einspeisung nach unten: Solange
mittags viel Solarstrom im Netz ist, klebt der OeMAG-Tarif an der Untergrenze. Wie die Berechnung im
Detail funktioniert und welche Alternativen es gibt, lesen Sie im Ratgeber
{a('/oemag-einspeisetarif/', 'OeMAG-Einspeisetarif')} und im Vergleich
{a('/einspeisetarif-fuer-photovoltaik/', 'Einspeisetarif für Photovoltaik')}.</p>
"""),
        ("Das neue Rechenmodell: Eigenverbrauch schlägt Einspeisung", "eigenverbrauch", f"""
<p>Was bedeuten 6 Cent für Ihre Strategie? Sie bedeuten, dass das alte Modell „Dach vollmachen und
alles verkaufen“ nicht mehr funktioniert. Die Rechnung:</p>
<ul>
  <li>Eine Kilowattstunde vom Netzbetreiber kostet inklusive Netzgebühren, Abgaben und Steuern im Schnitt
  rund 30 bis 35 Cent*.</li>
  <li>Eine selbst produzierte Kilowattstunde bringt bei der OeMAG 6,146 Cent (Juli 2026).</li>
  <li>Die Differenz, der „Spread“, beträgt also über 24 Cent je Kilowattstunde.</li>
</ul>
<p>Jede Kilowattstunde, die Sie selbst verbrauchen, spart rund 30 Cent Ausgabe. Jede Kilowattstunde,
die Sie einspeisen, bringt gut 6 Cent Einnahme. Der Wert des selbst verbrauchten Stroms ist damit rund
fünfmal so hoch wie der des eingespeisten. Der Gewinn Ihrer Anlage liegt nicht mehr im Verkauf von
Energie, sondern in der Vermeidung von Zukauf: Ihre PV-Anlage ist keine Einnahmequelle für
Einspeisevergütungen, sondern eine Sparbüchse für Ihre Betriebskosten.</p>
{A.box("Wer Überschuss lieber an Nachbarn oder Familie verkauft als an die OeMAG, findet in der "
       + a('eg', 'Energiegemeinschaft') + " eine Alternative: Typische EG-Einspeisepreise liegen bei "
       "8 bis 12 Cent, zusätzlich sparen Mitglieder im Nahbereich bis zu 57 Prozent der Netzentgelte "
       "(siehe " + a('/energiegemeinschaft-netzkosten/', 'Netzkosten in der Energiegemeinschaft') + ").",
       label="Alternative:")}
<p><small>*Richtwerte für Haushaltskunden inklusive Netzentgelte, Abgaben und Steuern. Der tatsächliche
Bezugspreis hängt von Lieferant, Tarif und Netzgebiet ab.</small></p>
"""),
        ("Die Rückkehr der Förder-Calls (BGBl. I Nr. 69/2025)", "foerderung", f"""
<p>Bis April 2025 galt in Österreich ein Umsatzsteuersatz von 0 Prozent auf PV-Anlagen: Der Preis auf der
Rechnung war netto gleich brutto. Diese Regelung ist ausgelaufen und wurde nicht verlängert, seither gilt
wieder der reguläre Steuersatz von 20 Prozent. Ist PV damit 20 Prozent teurer geworden? Unter dem Strich
nein. Denn mit der Novelle des Erneuerbaren-Ausbau-Gesetzes (EAG), kundgemacht im Bundesgesetzblatt I
Nr. 69/2025, ist die Finanzierung der klassischen Investitionszuschüsse für 2026 gesichert.</p>
{A.steps([
    ("Brutto bezahlen",
     "Sie bezahlen zunächst die Bruttosumme inklusive 20 Prozent Umsatzsteuer."),
    ("Antrag im Fördercall einreichen",
     "Es gibt feste Zeitfenster („Calls“), in denen Anträge gestellt werden müssen. Wer das Fenster "
     "verpasst oder Formfehler macht, geht leer aus (Reihung nach Eingang beziehungsweise Förderbedarf). "
     "EBZ Energie bereitet den Antrag vor und reicht ihn zur Call-Öffnung ein."),
    ("Zuschuss erhalten",
     "Sie erhalten einen fixen Zuschuss pro installiertem Kilowattpeak (kWp) und pro Kilowattstunde (kWh) "
     "Speicherkapazität zurücküberwiesen."),
])}
<p>Die Republik Österreich hat sich europarechtlich verpflichtet, den Ausbau der Erneuerbaren
voranzutreiben. Ein Förderstopp ist damit vom Tisch. Die Details zu Bund und Ländern finden Sie in den
Ratgebern {a('foerderung_at', 'Photovoltaik-Förderung Österreich')},
{a('foerderung_kaernten', 'Förderung Kärnten')} und {a('foerderung_steiermark', 'Förderung Steiermark')}.</p>
"""),
        ("Die Konsequenz für die Technik: Der Speicher ist der Rendite-Hebel", "speicher", f"""
<p>Aus Förder- und Marktsituation ergibt sich für 2026 eine klare technische Marschrichtung: Wer heute
eine PV-Anlage ohne {a('batteriespeicher', 'Batteriespeicher')} plant, verschenkt das größte
Sparpotenzial. Zwei Faktoren haben sich geändert:</p>
<ul>
  <li><b>Hardware-Preise:</b> Die Preise für Lithium-Eisenphosphat-Speicher (LFP) sind in den letzten
  24 Monaten deutlich gefallen.</li>
  <li><b>Marktpreis-Schere:</b> Der Wert des selbst verbrauchten Stroms ist ein Vielfaches des
  eingespeisten.</li>
</ul>
{A.table(
    ["Konfiguration", "Eigenverbrauchsanteil*", "Was mit dem Rest passiert"],
    [
        ["PV ohne Speicher", "rund 30 %", "70 % Einspeisung zu 6,146 ct"],
        ["PV mit passend dimensioniertem Speicher", "70 bis 80 %", "Mittagsstrom wird abends genutzt"],
        ["PV, Speicher und Energiemanagement", "noch höher", "Überschuss geht in Wärmepumpe und Wallbox"],
    ],
    hl_cols=(1,),
)}
<p>Ohne Speicher nutzen typische Haushalte nur rund 30 Prozent ihres Solarstroms selbst, weil die Sonne
scheint, während Sie bei der Arbeit sind. Mit einem passend dimensionierten Speicher steigt dieser Wert
auf 70 bis 80 Prozent. Sie retten den Mittagsstrom in den Abend, um zu kochen, zu waschen oder das
E-Auto zu laden.</p>
<h3>Intelligentes Energiemanagement</h3>
<p>Ist der Speicher im Sommer schon um 11 Uhr voll, soll der Überschuss nicht für 6 Cent ins Netz
fließen. Stattdessen gibt ein {a('ems', 'Energiemanagementsystem')} der Wärmepumpe das Signal, jetzt
Warmwasser zu bereiten, oder der Wallbox, das E-Auto zu laden. So wird Ihr Dach zur Energiequelle für
Wärme und Mobilität. Seit Juni 2026 fördert der Klimafonds solche Systeme mit bis zu 600 Euro für
Haushalte (siehe {a('/ems-foerderung/', 'EMS-Förderung 2026')}). In Kombination mit einem
{a('/dynamischer-stromtarif/', 'dynamischen Stromtarif')} legt das EMS auch den Zukauf in die
günstigsten Stunden.</p>
<p><small>*Richtwerte aus der Praxis. Der tatsächliche Eigenverbrauchsanteil hängt von Verbrauchsprofil,
Anlagengröße und Speicherkapazität ab.</small></p>
{A.cta("Rechnen wir mit Ihren Zahlen",
       "Wir erstellen für Ihr Dach einen Projektbericht mit 3D-Belegplan und Statikreport, mit den "
       "aktuellen OeMAG-Werten, Ihrem Lastprofil und der passenden Speichergröße.",
       secondary=("batteriespeicher", "Zum Batteriespeicher"))}
"""),
        ("Warum Warten keine Option mehr ist", "warten", f"""
<p>In Beratungsgesprächen hören wir oft: „Vielleicht wird die Technik nächstes Jahr noch billiger oder
die Förderung besser.“ Drei Gründe sprechen gegen diese Strategie:</p>
<ul>
  <li><b>Die Lohnkosten steigen:</b> Module und Speicher sind günstig, der größte Kostenblock einer
  Installation ist mittlerweile die Handwerksleistung. Montage, Verkabelung und Dacharbeiten sind
  qualifizierte Facharbeit, und die Lohnkosten in Österreich steigen inflationsbedingt weiter.</li>
  <li><b>Der Netzzugang wird enger:</b> Das Stromnetz in der Steiermark und in Kärnten füllt sich. In
  manchen Regionen gibt es bereits Einschränkungen bei der Einspeiseleistung. Mit dem neuen
  {a('/elwg-beschluss-oesterreich/', 'ElWG')} dürfen Netzbetreiber neue Anlagen zudem auf 70 Prozent der
  Leistung begrenzen. Wer jetzt ans Netz geht, sichert sich seine Kapazität.</li>
  <li><b>Der Vorsprung-Effekt:</b> Jeder Monat ohne PV-Anlage bedeutet die volle Stromrechnung an den
  Versorger. Eine Anlage, die im Frühjahr 2026 gebaut wird, hat bis Sommer 2027 über ein Jahr Erträge
  erwirtschaftet. Diesen Vorsprung holt eine spätere, vielleicht minimal günstigere Anlage nie auf.</li>
</ul>
"""),
        ("Fazit: Die Ampel steht auf Grün", "fazit", f"""
<p>2026 ist ein gutes Jahr für Photovoltaik, aber mit anderer Logik als 2022: Das Gesetz ist fixiert und
die Fördermittel sind da. Die Technik ist ausgereift und preiswert. Der Strompreis ist hoch genug, um
Sparen attraktiv zu machen, während der Einspeisetarif mit 6,146 Cent so niedrig ist, dass Eigenverbrauch
über Speicher und Energiemanagement zur Pflicht wird. Bei EBZ Energie liegt eine 10-kWp-Anlage mit
Speicher je nach Dach bei rund 15.000 bis 22.000 Euro vor Förderung, die Amortisation typischerweise bei
4 bis 6 Jahren.</p>
{A.cta("Lassen Sie uns gemeinsam rechnen",
       "Ehrlich, transparent und auf Basis der aktuellen Gesetzeslage und OeMAG-Werte: Wir zeigen Ihnen, "
       "wie hoch Förderung und Ersparnis für Ihr Dach konkret ausfallen.",
       primary=("kontakt", "Unverbindliches Angebot anfordern"), secondary=("photovoltaik", "Zur Photovoltaik"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner in einem komplexen Umfeld: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("Neue Gesetze, volatile Marktpreise, technische Anforderungen: Sie brauchen einen Partner, der "
                 "mehr bietet als einen Webshop. EBZ Energie ist in Villach verwurzelt und hat über 300 Projekte "
                 "in 6 Bundesländern umgesetzt. Wir verbauen standardmäßig Glas-Glas-Module, die "
                 "widerstandsfähiger gegen Hagel, Schneedruck und Ammoniak sind, mit bis zu 30 Jahren "
                 "Leistungsgarantie und mindestens 10 Jahren Produktgarantie."),
        "grid": [
            ("Regional verankert", "Wenn es ein Problem gibt, kommen wir vorbei."),
            ("Langlebig statt billig", "Glas-Glas-Module und geprüfte Speicher, damit die Rendite hält."),
            ("Alles aus einer Hand", "Vom Drohnen-Aufmaß über den Projektbericht bis zur Förder-Einreichung."),
            ("Fördermanagement", "Wir kennen die Call-Termine 2026 und reichen fristgerecht ein."),
        ],
    },

    "faq": [
        ("Wie hoch ist der OeMAG-Marktpreis aktuell?",
         "Stand September 2026: Für Juli 2026 beträgt der OeMAG-Marktpreis für Photovoltaik 6,146 Cent je "
         "Kilowattstunde. Das ist die gesetzliche Untergrenze von 60 Prozent des Quartalsmarktpreises der "
         "E-Control, der für das dritte Quartal 2026 bei 10,923 Cent liegt. Im vierten Quartal 2025 lag der "
         "Marktpreis noch bei 9,17 Cent."),
        ("Bekomme ich 2026 noch eine Förderung, obwohl die 0 Prozent Umsatzsteuer weg sind?",
         "Ja. Die Art der Förderung hat sich geändert: Statt des Nullsteuersatzes beim Kauf greift 2026 "
         "wieder das EAG mit Investitionszuschüssen über Fördercalls. Das Budget wurde im Bundesgesetzblatt "
         "I Nr. 69/2025 bestätigt. Sie strecken die Umsatzsteuer vor und bekommen über den Call einen Teil "
         "der Investitionskosten zurück. EBZ Energie übernimmt die Antragstellung."),
        ("Lohnt sich eine Anlage noch, wenn ich nur rund 6 Cent für die Einspeisung bekomme?",
         "Ja, aber die Strategie ändert sich. Da der Netzbezug rund 30 Cent kostet, ist jede selbst "
         "verbrauchte Kilowattstunde etwa fünfmal so viel wert wie eine eingespeiste. Die Rendite entsteht "
         "durch Einsparung, nicht durch Verkauf. Eine passend dimensionierte Anlage mit Speicher "
         "amortisiert sich bei EBZ Energie typischerweise in 4 bis 6 Jahren."),
        ("Ist ein Batteriespeicher jetzt Pflicht?",
         "Rechtlich nein, wirtschaftlich fast immer ja. Der Speicher hebt den Eigenverbrauch von rund "
         "30 auf 70 bis 80 Prozent und rettet den Mittagsstrom in den Abend. Zudem sind systemdienliche "
         "Speicher laut ElWG 20 Jahre von Infrastrukturbeiträgen befreit."),
        ("Was passiert, wenn ich den Förder-Call verpasse?",
         "Die Mittel sind budgetiert. Wer zu spät kommt oder Fehler im Antrag hat, muss auf den nächsten "
         "Call warten oder geht im schlimmsten Fall für das Jahr leer aus. EBZ Energie bereitet alle "
         "Unterlagen vor und reicht sie zur Call-Öffnung ein."),
        ("Soll ich noch warten, ob die Preise für PV-Anlagen weiter fallen?",
         "Wir raten davon ab. Die Hardwarepreise haben einen Boden erreicht, gleichzeitig steigen Lohn- "
         "und Montagekosten jährlich. Zudem riskieren Sie bei längerem Warten, dass Netzkapazitäten in "
         "Ihrer Region erschöpft sind. Preis, Förderung und Verfügbarkeit passen aktuell zusammen."),
        ("Gibt es Alternativen zur OeMAG-Einspeisung?",
         "Ja. In einer Energiegemeinschaft verkaufen Sie Überschuss an Nachbarn oder Familie, typischerweise "
         "zu 8 bis 12 Cent, und sparen im Nahbereich bis zu 57 Prozent der Netzentgelte. Der OeMAG-Vertrag "
         "bleibt als Auffangnetz für den Rest bestehen. Auch andere Lieferanten bieten Einspeisetarife an."),
        ("Wie oft ändert sich der Marktpreis?",
         "Der OeMAG-Marktpreis wird seit Jänner 2024 monatlich im Nachhinein festgelegt. Die Ober- und "
         "Untergrenze setzt die E-Control mit dem Quartalsmarktpreis. Wir aktualisieren die Werte in "
         "diesem Ratgeber laufend."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Photovoltaik, Speicher, Wärmepumpen und Energiemanagementsysteme in Kärnten und der "
                    "Steiermark und rechnet jedes Projekt mit den aktuellen OeMAG-Werten. Marktpreise werden "
                    "monatlich anhand der Veröffentlichungen von OeMAG und E-Control aktualisiert. Keine "
                    "Rechts- oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("Bundesgesetzblatt I Nr. 69/2025 (RIS, PDF)",
         "https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2025_I_69/BGBLA_2025_I_69.pdf"),
        ("OeMAG: Marktpreis-Übersicht", "https://www.oem-ag.at/marktpreis"),
    ],
    "related": [
        ("/oemag-einspeisetarif/", "OeMAG-Einspeisetarif: Berechnung und Alternativen"),
        ("/elwg-beschluss-oesterreich/", "ElWG-Beschluss: Was PV-Betreiber wissen müssen"),
        ("batteriespeicher", "Batteriespeicher: Mittagsstrom für den Abend"),
        ("foerderung_at", "Photovoltaik-Förderung Österreich"),
    ],
    "cta": {
        "h3": "Mit aktuellen Zahlen rechnen",
        "text": "Projektbericht mit 3D-Belegplan und Statikreport, auf Basis der aktuellen OeMAG-Werte.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Die Zeit der Unsicherheit ist vorbei",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
