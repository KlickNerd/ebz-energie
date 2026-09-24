"""Ratgeber: Smart Meter Opt-out (Rechte, Ablauf, Folgen).

Migriert von ebz-photovoltaik.at/smart-meter-opt-out/ (Stand der Quelle: Juli 2026).
Inhalte aus den Cluster-Quellen (Smart Meter Österreich, Auslesen, dynamischer Tarif,
EMS-Förderung).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "smart-meter-opt-out",
    "path": "/smart-meter-opt-out/",
    "title": "Smart Meter Opt-out: Rechte, Ablauf und Folgen | EBZ",
    "description": ("Smart Meter Opt-out: Übertragung 1x jährlich statt alle 15 Minuten, Antrag "
                    "in 4 Schritten und die Folgen für dynamische Tarife, Energiegemeinschaft und EMS."),
    "eyebrow": "Smart Meter · Datenschutz",
    "crumb_label": "Smart Meter Opt-out",
    "h1": "Smart Meter Opt-out: Ihre Rechte, der Antrag in 4 Schritten und die Folgen",
    "lead": ("Sie möchten nicht, dass Ihr Smart Meter alle 15 Minuten Daten überträgt? In Österreich haben "
             "Sie ein Recht auf den Opt-out. Dieser Ratgeber erklärt, was das bedeutet, wie Sie ihn beim "
             "Netzbetreiber beantragen und was Sie damit für Tarife und Energiemanagement aufgeben."),
    "chips": [
        "Übertragung: <b>1x jährlich</b> statt alle 15 Min.",
        "Antrag: <b>formlos beim Netzbetreiber</b>",
        "Zähler ablehnen: <b>nicht möglich</b>",
        "Rückwechsel: <b>in der Regel möglich</b>",
    ],
    "date_published": "2026-07-14",
    "date_modified": "2026-09-24",
    "hero_img": "gen_detail",
    "hero_alt": "Detailansicht einer Photovoltaikmontage, deren Einspeisung über den Smart Meter abgerechnet wird",

    "tldr": [
        "Beim Opt-out wird der digitale Zähler installiert, überträgt Ihre Werte aber nur eingeschränkt, in "
        "der Regel als Jahreswert statt als Viertelstundenwert.",
        "Ein vollständiges Ablehnen des Geräts ist in Österreich nicht möglich, der Zählertausch ist "
        "gesetzlich vorgesehen.",
        "Beantragt wird der Opt-out beim zuständigen Netzbetreiber, meist formlos oder per Online-Formular. "
        "Die Entscheidung lässt sich in der Regel später wieder ändern.",
        "Die Kehrseite: Mit Opt-out sind dynamische Stromtarife, die Teilnahme an einer Energiegemeinschaft "
        "und ein Energiemanagementsystem nur eingeschränkt oder gar nicht nutzbar.",
    ],
    "kpis": [
        ("1x", "Übertragung pro Jahr beim Opt-out"),
        ("96", "Übertragungen pro Tag im Standard"),
        ("4", "Schritte bis zum Opt-out"),
        ("3", "Anwendungen, die wegfallen: Tarif, EG, EMS"),
    ],

    "sections": [
        ("Was bedeutet der Smart-Meter-Opt-out?", "definition", f"""
<p>Der Opt-out ist Ihr Recht, die häufige Datenübertragung des Smart Meters zu reduzieren. Der digitale
Zähler wird trotzdem installiert, überträgt Ihre Verbrauchswerte dann aber nur eingeschränkt, in der
Regel als Jahreswert statt viertelstündlich. Ein vollständiges Ablehnen des Zählertauschs ist in
Österreich hingegen nicht vorgesehen: Der {a('/smart-meter/', 'Smart-Meter-Rollout')} ist gesetzlich
vorgeschrieben, die Netzbetreiber statten den Großteil der Zählpunkte mit digitalen Geräten aus.</p>
<p>Der Zähler selbst bleibt also gleich. Was sich ändert, ist die Konfiguration: Statt 96 Messwerten pro
Tag, die verschlüsselt an den Netzbetreiber gehen, wird nur noch der Jahresverbrauch übermittelt, so wie
beim alten Ferraris-Zähler.</p>
"""),
        ("Standard oder Opt-out: der Unterschied", "vergleich", f"""
{A.table(
    ["Merkmal", "Standard-Konfiguration", "Opt-out"],
    [
        ["Zähler", "digital", "digital"],
        ["Datenübertragung", "viertelstündlich (96 Werte pro Tag)", "stark reduziert (z. B. jährlich)"],
        ["Verbrauch im Portal", "tagesaktuell und fein aufgelöst", "nur eingeschränkt"],
        ["Dynamischer Tarif", "sinnvoll nutzbar", "kaum nutzbar"],
        ["Energiegemeinschaft", "Zuordnung viertelstundengenau möglich", "keine Zuordnung möglich"],
        ["Energiemanagement", "optimale Datenbasis", "eingeschränkte Optimierung"],
        ["EMS-Förderung 2026", "Voraussetzungen erfüllbar", "Messung von Bezug und Einspeisung fehlt"],
    ],
    hl_cols=(1,),
)}
"""),
        ("So beantragen Sie den Opt-out", "antrag", f"""
{A.steps([
    ("Netzbetreiber ermitteln",
     "Zuständig ist der Netzbetreiber Ihrer Region, nicht Ihr Stromlieferant. Sie finden ihn auf Ihrer "
     "Stromrechnung, ebenso Ihre Zählpunktnummer, die im Antrag abgefragt wird."),
    ("Antrag stellen",
     "Der Opt-out wird meist formlos oder über ein Online-Formular beim Netzbetreiber beantragt. Geben Sie "
     "Zählpunktnummer und Adresse an."),
    ("Bestätigung abwarten",
     "Der Netzbetreiber setzt die reduzierte Datenübertragung um und bestätigt Ihnen die Umstellung. Der "
     "Zähler bleibt eingebaut."),
    ("Bei Bedarf zurückwechseln",
     "In der Regel können Sie die Entscheidung später wieder ändern, etwa wenn Sie doch einen dynamischen "
     "Tarif nutzen, einer Energiegemeinschaft beitreten oder ein Energiemanagementsystem einbauen möchten."),
])}
"""),
        ("Welche Folgen hat der Opt-out?", "folgen", f"""
<p>Sowohl ein dynamischer Stromtarif als auch ein Energiemanagementsystem brauchen feingranulare Daten,
um Verbrauch und Ladevorgänge in die günstigsten Zeitfenster zu verschieben. Mit Opt-out fällt dieser
Hebel weitgehend weg. Konkret:</p>
<ul>
  <li><b>Dynamischer Stromtarif:</b> Der Preis richtet sich stündlich nach der Strombörse. Ohne
  Viertelstundenwerte kann der Lieferant nicht stundengenau abrechnen. Ein
  {a('/dynamischer-stromtarif/', 'dynamischer Tarif')} ist daher kaum nutzbar. Ein
  {a('/flexibler-stromtarif/', 'flexibler Tarif')} mit monatlicher Preisanpassung bleibt dagegen möglich.</li>
  <li><b>Energiegemeinschaft:</b> Die {a('eg', 'Energiegemeinschaft')} ordnet den Strom viertelstundengenau
  den Mitgliedern zu. Ohne diese Werte ist eine Teilnahme nicht möglich.</li>
  <li><b>Energiemanagement:</b> Ein {a('ems', 'EMS')} kann seltener auf Basis aktueller Werte optimieren.
  Die {a('/ems-foerderung/', 'EMS-Förderung 2026')} setzt zudem voraus, dass Bezug und Einspeisung am
  Netzanschluss gemessen werden.</li>
  <li><b>Transparenz:</b> Im Portal sehen Sie nur noch Jahreswerte, Stromfresser und Verbrauchsmuster
  bleiben verborgen. Wie Sie die Daten sonst nutzen, zeigt der Ratgeber
  {a('/smart-meter-auslesen/', 'Smart Meter auslesen')}.</li>
</ul>
<p>Auch die Einspeisung Ihrer {a('photovoltaik', 'PV-Anlage')} wird beim Opt-out nur als Jahreswert
übermittelt. Die Jahresabrechnung von Bezug und Einspeisung funktioniert weiterhin, Sie sehen aber nicht
mehr, zu welchen Stunden Überschuss ins Netz fließt. Genau diese Information bräuchten Sie, um Speicher,
Wärmepumpe oder Wallbox in die Mittagsstunden zu legen. Das Display am Zähler zeigt weiterhin die
aktuellen Zählerstände und die momentane Leistung an, einen Verlauf speichert es nicht.</p>
{A.box_dark("Für PV-Haushalte besonders relevant",
    "Wer eine Photovoltaikanlage mit Speicher betreibt und den Eigenverbrauch maximieren möchte, "
    "verzichtet mit dem Opt-out auf die größten Sparhebel: dynamische Tarife, das Teilen von Überschuss in "
    "der Energiegemeinschaft und die automatische Optimierung durch ein Energiemanagementsystem.")}
"""),
        ("Sollten Sie den Opt-out nutzen?", "entscheidung", f"""
<p>Der Opt-out ist sinnvoll, wenn Ihnen die häufige Datenübertragung grundsätzlich unangenehm ist und Sie
auf moderne Tarife und Automatisierung bewusst verzichten möchten. Wollen Sie dagegen Kosten senken und
Ihren PV-Eigenverbrauch maximieren, ist die Standardkonfiguration die bessere Wahl.</p>
<p>Zur Einordnung beim Datenschutz: Die Erfassung, Übertragung und Speicherung der Daten ist gesetzlich
geregelt, die Übermittlung erfolgt verschlüsselt an den Netzbetreiber. Der Opt-out ist eine zusätzliche
Möglichkeit für alle, die die häufige Übertragung trotzdem nicht wünschen.</p>
{A.cta("Neutral beraten lassen",
       "Wir zeigen Ihnen kostenlos, welche Zählerkonfiguration und welcher Tarif zu Ihren Zielen passen, "
       "und was Sie mit Standardkonfiguration und Energiemanagement konkret sparen.",
       secondary=("ems", "Zum Energiemanagementsystem"))}
"""),
        ("Fazit", "fazit", f"""
<p>Der Opt-out ist Ihr gutes Recht und schnell beantragt. Bedenken Sie aber die Kehrseite: Ohne
feingranulare Daten verzichten Sie auf die größten Sparhebel, dynamische Tarife, Energiegemeinschaft und
die automatische Optimierung durch ein Energiemanagementsystem. Wägen Sie ab, was Ihnen wichtiger ist.
Die Entscheidung ist in der Regel nicht endgültig.</p>
{A.cta("Unsicher, welche Konfiguration zu Ihnen passt?",
       "Kostenlose Erstberatung: Wir rechnen mit Ihrem Verbrauchsprofil, ob und wie sich dynamische "
       "Tarife und ein Energiemanagement für Sie lohnen.",
       primary=("kontakt", "Kostenlose Beratung anfragen"), secondary=("photovoltaik", "Zur Photovoltaik"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Zählerkonfiguration und Energiemanagement: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("Wir beraten Sie neutral: Wenn Ihr Ziel maximale Ersparnis ist, zeigen wir Ihnen, wie Sie "
                 "mit der Standardkonfiguration, einem passenden Tarif und einem Energiemanagementsystem am "
                 "meisten herausholen. Die Technik dahinter installiert EBZ Energie aus Villach komplett aus "
                 "einer Hand, mit einem festangestellten Team aus zertifizierten Fachkräften in Kärnten und "
                 "der Steiermark."),
        "grid": [
            ("Neutrale Beratung", "Wir sagen ehrlich, was der Opt-out Sie an Ersparnis kostet."),
            ("Verbrauchsanalyse", "Kostenlose Auswertung Ihres Profils und Ihrer Anlage."),
            ("Energiemanagement", "Förderfähige Systeme für PV, Speicher, Wärmepumpe und Wallbox."),
            ("Regional", "Planung und Montage in Kärnten und der Steiermark."),
        ],
    },

    "faq": [
        ("Was bedeutet der Smart-Meter-Opt-out?",
         "Beim Opt-out wird der digitale Zähler zwar installiert, überträgt Ihre Verbrauchswerte aber nur "
         "eingeschränkt, in der Regel als Jahres- statt als Viertelstundenwert. Sie behalten also einen "
         "digitalen Zähler, reduzieren aber die häufige Datenübertragung."),
        ("Kann ich den Smart Meter komplett ablehnen?",
         "Nein. Der Austausch des Zählers ist gesetzlich vorgesehen, ein vollständiges Ablehnen des Geräts "
         "ist nicht möglich. Sie können aber die Datenübertragung per Opt-out auf ein Minimum reduzieren."),
        ("Wie beantrage ich den Opt-out?",
         "Der Opt-out wird beim zuständigen Netzbetreiber beantragt, meist formlos oder über ein Formular "
         "auf dessen Website. Sie brauchen dafür Ihre Zählpunktnummer von der Stromrechnung. Die "
         "Entscheidung lässt sich in der Regel später wieder ändern."),
        ("Welche Nachteile hat der Opt-out?",
         "Ohne feingranulare Daten können Sie keinen dynamischen Stromtarif sinnvoll nutzen, nicht an einer "
         "Energiegemeinschaft teilnehmen, und ein Energiemanagementsystem kann seltener auf Basis aktueller "
         "Werte optimieren. Wer den Eigenverbrauch maximieren möchte, fährt mit der Standardkonfiguration "
         "besser."),
        ("Kann ich mit Opt-out einer Energiegemeinschaft beitreten?",
         "Nein. Die Energiegemeinschaft ordnet erzeugten und verbrauchten Strom viertelstundengenau zu. Dafür "
         "braucht jeder Zählpunkt einen Smart Meter mit aktiver Datenübertragung."),
        ("Kann ich den Opt-out später rückgängig machen?",
         "In der Regel ja. Sie können beim Netzbetreiber wieder auf die Standardkonfiguration wechseln, "
         "etwa wenn Sie einen dynamischen Tarif abschließen oder ein Energiemanagementsystem einbauen "
         "möchten."),
        ("Betrifft der Opt-out auch meine PV-Einspeisung?",
         "Ja. Der Smart Meter erfasst Bezug und Einspeisung, beim Opt-out werden beide nur als Jahreswert "
         "übermittelt. Die Abrechnung funktioniert weiterhin, Sie sehen im Portal aber nicht mehr, wann "
         "Überschuss anfällt. Für die Optimierung des Eigenverbrauchs fehlt damit die Datenbasis."),
        ("Ist meine Privatsphäre auch ohne Opt-out geschützt?",
         "Die Erfassung, Übertragung und Speicherung der Daten ist gesetzlich geregelt, die Übermittlung "
         "an den Netzbetreiber erfolgt verschlüsselt. Der Opt-out ist eine zusätzliche Möglichkeit für "
         "alle, die die häufige Übertragung grundsätzlich nicht wünschen."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Photovoltaik, Speicher, Wärmepumpen und Energiemanagementsysteme in Kärnten und der "
                    "Steiermark und berät neutral, welche Zählerkonfiguration zu Ihren Zielen passt. Angaben "
                    "zum Opt-out beruhen auf den Informationen von E-Control und oesterreich.gv.at, "
                    "maßgeblich sind die Bedingungen Ihres Netzbetreibers. Keine Rechtsberatung."),
    "sources": [
        ("E-Control: Regulierungsbehörde für Strom und Gas", "https://www.e-control.at/"),
        ("oesterreich.gv.at: Informationen zum Smart Meter", "https://www.oesterreich.gv.at/"),
    ],
    "related": [
        ("/smart-meter/", "Smart Meter in Österreich: Funktion, Rollout und Nutzen"),
        ("/dynamischer-stromtarif/", "Dynamischer Stromtarif: Wann sich Spotpreise lohnen"),
        ("/smart-meter-auslesen/", "Smart Meter auslesen: So sehen Sie Ihren Verbrauch"),
        ("eg", "Energiegemeinschaft: Strom teilen mit Nachbarn"),
    ],
    "cta": {
        "h3": "Neutral beraten lassen",
        "text": "Wir zeigen Ihnen kostenlos, welche Konfiguration und welcher Tarif zu Ihren Zielen passen.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Unsicher, welche Konfiguration zu Ihnen passt?",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das neutral sagt, "
                   "ob sich dynamische Tarife und Energiemanagement für Sie lohnen."),
}
