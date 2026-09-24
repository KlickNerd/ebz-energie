"""Ratgeber: Smart Meter auslesen (Portal und Display).

Migriert von ebz-photovoltaik.at/smart-meter-auslesen/ (Stand der Quelle: Juli 2026).
Inhalte aus den Cluster-Quellen (Smart Meter Österreich, Was ist ein Smart Meter,
Opt-out, dynamischer Tarif).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "smart-meter-auslesen",
    "path": "/smart-meter-auslesen/",
    "title": "Smart Meter auslesen: Verbrauch in 4 Schritten sehen | EBZ",
    "description": ("Smart Meter auslesen: in 4 Schritten ins Portal des Netzbetreibers, Viertelstundenwerte "
                    "verstehen, Display ablesen und Daten mit Tarif und EMS nutzen."),
    "eyebrow": "Smart Meter · Anleitung",
    "crumb_label": "Smart Meter auslesen",
    "h1": "Smart Meter auslesen: In 4 Schritten zu Ihren Verbrauchsdaten",
    "lead": ("Ihr Smart Meter erfasst alle 15 Minuten, wie viel Strom Sie verbrauchen und einspeisen. Wo Sie "
             "diese Daten sehen und was Sie damit anfangen, zeigt dieser Ratgeber Schritt für Schritt: "
             "online im Portal und direkt am Gerät."),
    "chips": [
        "<b>4 Schritte</b> bis zum Portal",
        "Werte <b>alle 15 Minuten</b>",
        "Online <b>und am Display</b>",
        "Zugang über <b>Zählpunktnummer</b>",
    ],
    "date_published": "2026-07-08",
    "date_modified": "2026-09-24",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit Photovoltaikanlage, deren Bezug und Einspeisung ein Smart Meter erfasst",

    "tldr": [
        "Sie lesen Ihren Smart Meter am einfachsten im Online-Portal Ihres Netzbetreibers aus. Für die "
        "Registrierung brauchen Sie meist die Zählpunktnummer von Ihrer Stromrechnung.",
        "Im Portal sehen Sie den Verbrauch tagesaktuell nach Tag, Monat oder Viertelstunde, bei PV-Anlagen "
        "auch die Einspeisung.",
        "Das Display am Zähler zeigt aktuelle Werte: Zählerstand für Bezug und Einspeisung sowie die "
        "momentane Leistung.",
        "Beim Opt-out sind im Portal nur Jahreswerte sichtbar. Den größten Nutzen bringen die Daten mit "
        "einem dynamischen Tarif und einem Energiemanagementsystem.",
    ],
    "kpis": [
        ("4", "Schritte bis zur Verbrauchsübersicht"),
        ("15 Min.", "Auflösung der Daten im Portal"),
        ("2", "Wege: Online-Portal und Display"),
        ("1x", "Registrierung mit Zählpunktnummer"),
    ],

    "sections": [
        ("Wie kann ich meinen Smart Meter auslesen?", "wege", f"""
<p>Es gibt zwei Wege: online über das Portal Ihres Netzbetreibers und direkt am Display des Zählers. Das
Portal ist die komfortablere Variante, weil Sie dort den zeitlichen Verlauf Ihres Verbrauchs sehen und
nicht nur den aktuellen Zählerstand.</p>
<p>Wichtig zu wissen: Das Portal betreibt Ihr Netzbetreiber, also das Unternehmen, das die Stromleitungen
in Ihrer Region betreibt. Das ist nicht zwingend Ihr Stromlieferant, bei dem Sie den Tarif haben. Wer
für Ihre Adresse zuständig ist, steht auf der Stromrechnung. Grundlagen zum digitalen Zähler finden Sie
im Ratgeber {a('/smart-meter/', 'Smart Meter in Österreich')}.</p>
{A.table(
    ["Merkmal", "Online-Portal des Netzbetreibers", "Display am Zähler"],
    [
        ["Was Sie sehen", "Verlauf nach Tag, Monat, Viertelstunde", "Zählerstand, momentane Leistung"],
        ["Einspeisung bei PV", "als eigener Verlauf", "als eigener Zählerstand"],
        ["Zugang", "Registrierung mit Zählpunktnummer", "direkt am Gerät"],
        ["Geeignet für", "Auswertung über die Zeit", "schneller Kontrollblick"],
    ],
    hl_cols=(1,),
)}
"""),
        ("Schritt für Schritt: Verbrauch im Online-Portal ansehen", "anleitung", f"""
{A.steps([
    ("Netzbetreiber ermitteln",
     "Finden Sie heraus, welcher Netzbetreiber für Ihre Adresse zuständig ist. Diese Information steht auf "
     "Ihrer Stromrechnung, meist im Abschnitt Netz oder Netzentgelte."),
    ("Smart-Meter-Portal aufrufen",
     "Auf der Website des Netzbetreibers gibt es ein Webportal, oft „Smart-Meter-Portal“ oder "
     "„Webportal“ genannt."),
    ("Registrieren und einloggen",
     "Legen Sie ein Konto an. Dafür benötigen Sie meist Ihre Zählpunktnummer, die Sie ebenfalls auf der "
     "Rechnung finden. Nach der Bestätigung loggen Sie sich ein."),
    ("Verbrauch analysieren",
     "Jetzt sehen Sie Ihren Verbrauch nach Tag, Monat oder Viertelstunde, bei einer PV-Anlage auch Ihre "
     "Einspeisung. Vergleichen Sie einzelne Tage, um Muster zu erkennen."),
])}
{A.box("Damit im Portal fein aufgelöste Werte erscheinen, muss die viertelstündliche Datenübertragung "
       "aktiv sein. Beim " + a('/smart-meter-opt-out/', 'Smart-Meter-Opt-out') + " sind die Daten nur "
       "eingeschränkt sichtbar, in der Regel als Jahreswert.", label="Gut zu wissen:")}
"""),
        ("Direkt am Zähler ablesen", "display", f"""
<p>Am Smart Meter selbst finden Sie ein digitales Display. Dort werden aktuelle Werte angezeigt, etwa der
Zählerstand für Bezug und Einspeisung sowie die momentane Leistung. Für einen schnellen Blick ist das
praktisch, zum Beispiel um zu prüfen, ob die PV-Anlage gerade einspeist. Für die genaue Auswertung
über die Zeit ist das Online-Portal besser geeignet, weil das Display keinen Verlauf speichert.</p>
<p>Ein Praxistipp für den Kontrollblick: Schalten Sie an einem sonnigen Mittag große Verbraucher aus
und beobachten Sie die momentane Leistung am Display. Zeigt der Zähler Einspeisung an, fließt Ihr
Überschuss ins Netz. Genau in diesen Stunden lohnt es sich, Waschmaschine, Warmwasser oder das Laden
des E-Autos einzuplanen, oder ein Energiemanagementsystem übernimmt das automatisch.</p>
"""),
        ("Was die Werte bedeuten", "werte", f"""
<p>Drei Werte sind für PV-Haushalte entscheidend:</p>
<ul>
  <li><b>Bezug:</b> Strom, den Sie aus dem Netz gekauft haben. Diese Kilowattstunden zahlen Sie zum
  Tarif Ihres Lieferanten.</li>
  <li><b>Einspeisung:</b> Überschuss Ihrer PV-Anlage, der ins Netz geflossen ist. Dafür erhalten Sie
  den Einspeisetarif, etwa den {a('/oemag-einspeisetarif/', 'OeMAG-Marktpreis')}.</li>
  <li><b>Momentane Leistung:</b> Was Ihr Haushalt gerade zieht oder abgibt. Nützlich, um einzelne
  Geräte einzuordnen.</li>
</ul>
<p>Im Viertelstundenverlauf erkennen Sie typische Muster: die Grundlast in der Nacht (Kühlgeräte,
Standby), die Einspeisespitze mittags und die Bezugsspitze am Abend. Genau diese Abendspitze ist der
Hebel: Je mehr Verbrauch Sie in die Mittagsstunden legen oder über einen
{a('batteriespeicher', 'Batteriespeicher')} in den Abend retten, desto weniger Strom kaufen Sie zu.</p>
"""),
        ("Was Sie mit den Daten anfangen können", "nutzen", f"""
<p>Die reine Anzeige ist nur der Anfang. Richtig wertvoll werden die Daten, wenn Sie daraus Konsequenzen
ziehen:</p>
<ul>
  <li><b>Stromfresser finden:</b> Eine hohe Grundlast in der Nacht deutet auf alte Geräte im
  Dauerbetrieb hin.</li>
  <li><b>Verbrauch verschieben:</b> Mit einem {a('/dynamischer-stromtarif/', 'dynamischen Stromtarif')}
  nutzen Sie günstige Zeitfenster an der Strombörse, meist nachts und mittags. Voraussetzung ist die
  aktive Datenübertragung des Smart Meters.</li>
  <li><b>Automatisch optimieren:</b> Ein {a('ems', 'Energiemanagementsystem')} übernimmt das für Sie
  und steuert PV, Speicher, Wärmepumpe und Wallbox. Seit Juni 2026 fördert der Klima- und Energiefonds
  solche Systeme für Haushalte mit 50 Prozent, maximal 600 Euro (siehe
  {a('/ems-foerderung/', 'EMS-Förderung 2026')}).</li>
  <li><b>Strom teilen:</b> In einer {a('eg', 'Energiegemeinschaft')} wird Ihr Überschuss
  viertelstundengenau den Mitgliedern zugeordnet, die ihn zeitgleich verbrauchen.</li>
</ul>
{A.cta("Verbrauch verstehen, Kosten senken",
       "Wir werten Ihr Verbrauchsprofil kostenlos aus und zeigen, wie ein Energiemanagementsystem die "
       "Optimierung automatisch übernimmt.",
       secondary=("ems", "Zum Energiemanagementsystem"))}
"""),
        ("Fazit", "fazit", f"""
<p>Ihren Smart Meter lesen Sie am besten im Online-Portal Ihres Netzbetreibers aus, ergänzend zeigt das
Display am Zähler aktuelle Werte. Wirklich sparen Sie aber erst, wenn Sie aus den Daten Konsequenzen
ziehen, idealerweise automatisiert durch ein Energiemanagementsystem, das Verbrauch in günstige und
sonnenreiche Stunden verschiebt.</p>
{A.cta("Aus Verbrauchsdaten wird Ersparnis",
       "Kostenlose Erstberatung: Wir prüfen, welche Kombination aus Tarif, Speicher und Energiemanagement "
       "zu Ihrem Verbrauchsprofil passt.",
       primary=("kontakt", "Kostenlose Beratung anfragen"), secondary=("batteriespeicher", "Zum Batteriespeicher"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Energiemanagement: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("Verbrauchsdaten sind gut, automatisierte Ersparnis ist besser. EBZ Energie aus Villach "
                 "verbindet Ihren Smart Meter über ein Energiemanagementsystem mit Ihrer Anlage und "
                 "übernimmt Planung und Installation in Kärnten und der Steiermark aus einer Hand, mit einem "
                 "festangestellten Team aus zertifizierten Fachkräften. So müssen Sie nicht selbst "
                 "optimieren, das System erledigt es automatisch."),
        "grid": [
            ("Verbrauchsanalyse", "Wir lesen Ihr Profil und finden die größten Sparhebel."),
            ("Automatische Steuerung", "EMS für PV, Speicher, Wärmepumpe und Wallbox."),
            ("Förderfähig", "Systeme, die die Bedingungen der EMS-Förderung 2026 erfüllen."),
            ("Regional", "Beratung und Montage in Kärnten und der Steiermark."),
        ],
    },

    "faq": [
        ("Wie kann ich meinen Smart Meter auslesen?",
         "Am einfachsten über das Online-Portal Ihres Netzbetreibers: mit der Zählpunktnummer registrieren, "
         "einloggen und den Verbrauch tages- oder viertelstundengenau ansehen. Zusätzlich zeigt das Display "
         "am Zähler Zählerstand und momentane Leistung an."),
        ("Wo finde ich das Portal meines Netzbetreibers?",
         "Das Portal wird von dem Netzbetreiber betrieben, der für Ihre Region zuständig ist, nicht von "
         "Ihrem Stromlieferanten. Den Netzbetreiber finden Sie auf der Stromrechnung, den Zugang auf dessen "
         "Website unter Stichworten wie Smart-Meter-Portal oder Webportal."),
        ("Wo steht meine Zählpunktnummer?",
         "Die Zählpunktnummer steht auf Ihrer Stromrechnung, meist im Abschnitt zu Netz und Zählpunkt. Sie "
         "identifiziert Ihren Anschluss eindeutig und wird für die Registrierung im Portal benötigt."),
        ("Wie aktuell sind die Daten im Portal?",
         "In der Regel sehen Sie Ihre Verbrauchsdaten tagesaktuell. Ist die viertelstündliche Übertragung "
         "aktiv, können Sie den Verlauf mit 96 Werten pro Tag nachvollziehen. Beim Opt-out sind die Daten "
         "nur eingeschränkt verfügbar."),
        ("Kann ich den Verbrauch auch direkt am Zähler ablesen?",
         "Ja. Das Display des Smart Meters zeigt aktuelle Werte an, etwa den Zählerstand für Bezug und "
         "Einspeisung und die momentane Leistung. Einen Verlauf speichert das Display nicht, dafür ist das "
         "Online-Portal zuständig."),
        ("Sehe ich im Portal auch meine PV-Einspeisung?",
         "Ja. Bei einer PV-Anlage erfasst der Smart Meter Bezug und Einspeisung getrennt. Im Portal sehen "
         "Sie beide Verläufe und erkennen, wann Überschuss ins Netz fließt und wann Sie zukaufen."),
        ("Warum sehe ich im Portal keine Viertelstundenwerte?",
         "Dann ist die viertelstündliche Datenübertragung nicht aktiv, etwa weil ein Opt-out eingestellt "
         "ist. In diesem Fall überträgt der Zähler nur einen Jahreswert. Die Standardkonfiguration können Sie "
         "beim Netzbetreiber beantragen, in der Regel formlos oder per Online-Formular."),
        ("Was mache ich mit den Verbrauchsdaten?",
         "Die Daten helfen, Stromfresser zu erkennen und den Verbrauch zu verstehen. Richtig wertvoll werden "
         "sie mit einem dynamischen Tarif und einem Energiemanagementsystem, das den Verbrauch automatisch "
         "in günstige und sonnenreiche Zeiten verschiebt."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Photovoltaik, Speicher, Wärmepumpen und Energiemanagementsysteme in Kärnten und der "
                    "Steiermark und macht aus Smart-Meter-Daten automatisierte Ersparnis. Portalzugang und "
                    "Funktionsumfang unterscheiden sich je nach Netzbetreiber, maßgeblich sind dessen Angaben."),
    "sources": [
        ("E-Control: Regulierungsbehörde für Strom und Gas", "https://www.e-control.at/"),
        ("oesterreich.gv.at: Informationen zum Smart Meter", "https://www.oesterreich.gv.at/"),
    ],
    "related": [
        ("/smart-meter/", "Smart Meter in Österreich: Funktion, Rollout und Nutzen"),
        ("/was-ist-ein-smart-meter/", "Was ist ein Smart Meter? Einfach erklärt"),
        ("/dynamischer-stromtarif/", "Dynamischer Stromtarif: Wann sich Spotpreise lohnen"),
        ("ems", "Energiemanagementsystem: Funktion und Nutzen"),
    ],
    "cta": {
        "h3": "Verbrauch verstehen, Kosten senken",
        "text": "Wir zeigen Ihnen kostenlos, wie ein Energiemanagementsystem Ihren Verbrauch automatisch optimiert.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Aus Verbrauchsdaten wird Ersparnis",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Zählerdaten "
                   "in automatisierte Steuerung übersetzt."),
}
