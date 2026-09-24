"""Ratgeber: Was ist ein Smart Meter? Einfach erklärt.

Migriert von ebz-photovoltaik.at/was-ist-ein-smart-meter/ (Stand der Quelle: Juli 2026).
Einsteiger-Artikel des Clusters Smart Meter und Stromtarife; Inhalte aus den
Cluster-Quellen (Smart Meter Österreich, Auslesen, Opt-out, Tarife).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "was-ist-ein-smart-meter",
    "path": "/was-ist-ein-smart-meter/",
    "title": "Was ist ein Smart Meter? Einfach erklärt | EBZ Energie",
    "description": ("Was ist ein Smart Meter? Der digitale Stromzähler misst alle 15 Minuten, überträgt "
                    "automatisch und zeigt den Verbrauch tagesaktuell. Einfach erklärt."),
    "eyebrow": "Smart Meter · Einfach erklärt",
    "crumb_label": "Was ist ein Smart Meter?",
    "h1": "Was ist ein Smart Meter? Der digitale Stromzähler in 5 Minuten erklärt",
    "lead": ("Ein Smart Meter ist der digitale Nachfolger des alten Stromzählers. Er erfasst Ihren Verbrauch "
             "automatisch alle 15 Minuten und macht ihn tagesaktuell sichtbar, statt einmal im Jahr eine "
             "einzige Zahl zu liefern."),
    "chips": [
        "Digitaler <b>Stromzähler</b>",
        "Misst <b>alle 15 Minuten</b>",
        "Überträgt <b>automatisch</b>",
        "Tausch <b>ohne Extrakosten</b>",
    ],
    "date_published": "2026-07-11",
    "date_modified": "2026-09-24",
    "hero_img": "gen_detail",
    "hero_alt": "Montagedetail einer Photovoltaikanlage, deren Einspeisung ein Smart Meter viertelstündlich erfasst",

    "tldr": [
        "Ein Smart Meter ist ein digitaler, fernauslesbarer Stromzähler, der den alten mechanischen "
        "Ferraris-Zähler ersetzt.",
        "Er misst Ihren Verbrauch in Viertelstundenwerten und überträgt ihn verschlüsselt an den "
        "Netzbetreiber. Bei PV-Anlagen erfasst er auch die Einspeisung.",
        "Sie sehen Ihren Verbrauch tagesaktuell im Online-Portal des Netzbetreibers, statt einmal im Jahr "
        "abzulesen.",
        "Der Zähler selbst spart kein Geld. Er ist die Basis für dynamische Tarife, Energiegemeinschaften "
        "und ein Energiemanagementsystem, die den Verbrauch in günstige Stunden verschieben.",
    ],
    "kpis": [
        ("96", "Messwerte pro Tag (alle 15 Minuten)"),
        ("1", "Messwert pro Jahr beim alten Zähler"),
        ("2", "Richtungen: Bezug und Einspeisung"),
        ("0 €", "Anschaffungskosten für den Zähler"),
    ],

    "sections": [
        ("Was ist ein Smart Meter? Die Definition", "definition", f"""
<p>Ein Smart Meter (deutsch: intelligenter Stromzähler) ist ein digitaler Zähler, der Ihren
Stromverbrauch automatisch in kurzen Intervallen erfasst und die Werte an Ihren Netzbetreiber
übermittelt. Er ersetzt den alten, mechanischen Ferraris-Zähler mit der drehenden Scheibe, der nur
einmal im Jahr abgelesen wurde.</p>
<p>Vereinfacht gesagt: Der Smart Meter ist für Ihren Stromverbrauch das, was ein Fitness-Tracker für Ihre
Schritte ist. Statt am Jahresende eine einzige Zahl zu bekommen, sehen Sie laufend, wann und wie viel
Strom Sie nutzen. Bei einem Messintervall von 15 Minuten sind das 96 Werte pro Tag.</p>
"""),
        ("Was macht ein Smart Meter?", "was-macht", f"""
<p>Drei Aufgaben erledigt der Smart Meter vollautomatisch:</p>
{A.steps([
    ("Er misst",
     "Standardmäßig alle 15 Minuten wird der Verbrauch erfasst. Bei einer Photovoltaikanlage zählt der "
     "Smart Meter zusätzlich, wie viel Strom Sie ins Netz einspeisen. Der alte Zähler kannte nur den "
     "Gesamtverbrauch."),
    ("Er überträgt",
     "Die Werte werden verschlüsselt an den Netzbetreiber übermittelt. Niemand muss mehr in den Keller "
     "gehen und ablesen, und die Jahresabrechnung basiert auf tatsächlichen statt geschätzten Werten."),
    ("Er zeigt",
     "Im Online-Portal Ihres Netzbetreibers sehen Sie den Verbrauch tagesaktuell nach Tag, Monat oder "
     "Viertelstunde. Zusätzlich zeigt das Display am Gerät Zählerstand und momentane Leistung."),
])}
<p>Bei einer {a('photovoltaik', 'Photovoltaikanlage')} entsteht so ein genaues Bild von Erzeugung und
Verbrauch. Das ist die Grundlage, um den Eigenverbrauch gezielt zu steigern: Sie sehen, wann Überschuss
ins Netz fließt, und können Speicher, Wärmepumpe oder Wallbox genau in diese Stunden legen.</p>
"""),
        ("Unterschied zum alten Stromzähler", "unterschied", f"""
{A.table(
    ["Merkmal", "Alter Ferraris-Zähler", "Smart Meter"],
    [
        ["Technik", "mechanisch, drehende Scheibe", "digital, fernauslesbar"],
        ["Ablesung", "einmal jährlich, oft manuell", "automatisch, tagesaktuell"],
        ["Auflösung", "ein Jahreswert", "Viertelstundenwerte"],
        ["Einspeisung bei PV", "eigener Zähler nötig", "im selben Gerät erfasst"],
        ["Datenzugang", "Zählerstand am Gerät", "Online-Portal und Display"],
        ["Dynamischer Tarif", "nicht möglich", "möglich"],
        ["Energiemanagement", "nicht möglich", "möglich"],
    ],
    hl_cols=(2,),
)}
<p>Der entscheidende Unterschied ist nicht die Anzeige, sondern die Auflösung: Erst mit
Viertelstundenwerten können ein Stromlieferant stundengenau abrechnen, eine Energiegemeinschaft den
Strom zuordnen und ein Energiemanagementsystem automatisch steuern.</p>
"""),
        ("Warum ist das für Sie interessant?", "nutzen", f"""
<p>Der Smart Meter selbst spart noch kein Geld. Interessant wird er durch das, was er ermöglicht:</p>
<ul>
  <li><b>Stromfresser erkennen:</b> Sie sehen die Grundlast in der Nacht und verstehen, welche Geräte
  wann Strom ziehen.</li>
  <li><b>Dynamischer Stromtarif:</b> Sie können einen {a('/dynamischer-stromtarif/', 'dynamischen Stromtarif')}
  nutzen und Strom dann beziehen, wenn er an der Börse günstig ist, meist nachts und mittags bei viel
  Sonne. Ohne Smart Meter ist das nicht möglich.</li>
  <li><b>Energiemanagement:</b> Ein {a('ems', 'Energiemanagementsystem')} steuert PV-Anlage, Speicher,
  Wärmepumpe und Wallbox automatisch und erhöht den PV-Eigenverbrauch deutlich.</li>
  <li><b>Energiegemeinschaft:</b> Das Teilen von Strom mit Nachbarn in einer
  {a('eg', 'Energiegemeinschaft')} setzt einen Smart Meter mit Viertelstundenwerten voraus.</li>
</ul>
{A.cta("Smart Meter, PV und EMS sinnvoll kombinieren",
       "Wir zeigen Ihnen kostenlos, wie Sie aus Ihren Verbrauchsdaten echte Ersparnis machen: mit dem "
       "passenden Tarif, Speicher und Energiemanagement.",
       secondary=("ems", "Zum Energiemanagementsystem"))}
"""),
        ("Muss ich einen Smart Meter nehmen?", "pflicht", f"""
<p>In Österreich werden die alten Zähler flächendeckend durch Smart Meter ersetzt, der Rollout ist
gesetzlich vorgeschrieben. Der Tausch erfolgt durch Ihren Netzbetreiber, für den Zähler selbst fallen
keine gesonderten Anschaffungskosten an, die Messeinrichtung ist über die Netzentgelte abgedeckt.</p>
<p>Wer die viertelstündliche Datenübertragung nicht möchte, kann beim Netzbetreiber einen Opt-out
beantragen. Der digitale Zähler wird dann trotzdem installiert, überträgt aber nur einen Jahreswert.
Ein vollständiges Ablehnen des Geräts ist nicht vorgesehen. Bedenken Sie: Mit Opt-out sind dynamische
Tarife und Energiemanagement kaum nutzbar. Details zu Rollout und Opt-out lesen Sie in
{a('/smart-meter/', 'Smart Meter in Österreich')} und {a('/smart-meter-opt-out/', 'Smart Meter Opt-out')}.</p>
{A.box("Der Smart Meter ist ein digitaler Zähler, der Verbrauchsdaten erfasst und verschlüsselt "
       "überträgt. Erfassung, Übertragung und Speicherung sind gesetzlich geregelt. Gesundheitlich "
       "bedenklich ist das Gerät nicht.", label="Ist ein Smart Meter gefährlich?")}
"""),
        ("Wie sehe ich meine Daten?", "auslesen", f"""
<p>Zwei Wege: online über das Portal Ihres Netzbetreibers und direkt am Display des Zählers. Das Portal
ist die komfortablere Variante, weil Sie dort den zeitlichen Verlauf sehen. Für die Registrierung
brauchen Sie meist Ihre Zählpunktnummer von der Stromrechnung. Wichtig: Das Portal betreibt der
Netzbetreiber Ihrer Region, nicht Ihr Stromlieferant. Die Anleitung Schritt für Schritt finden Sie im
Ratgeber {a('/smart-meter-auslesen/', 'Smart Meter auslesen')}.</p>
"""),
        ("Fazit", "fazit", f"""
<p>Ein Smart Meter ist ein digitaler Stromzähler, der Ihren Verbrauch automatisch misst und sichtbar
macht. Er ist der erste Schritt zu mehr Transparenz, günstigeren Tarifen und einem höheren Eigenverbrauch
Ihrer PV-Anlage. Das volle Potenzial holen Sie mit einem Energiemanagementsystem heraus, das die Daten
automatisch in Entscheidungen übersetzt.</p>
{A.cta("Bereit für den nächsten Schritt?",
       "Kostenlose Erstberatung: Wir prüfen, wie sich Smart Meter, PV-Anlage und Energiemanagement bei "
       "Ihnen zu einem System verbinden lassen.",
       primary=("kontakt", "Kostenlose Beratung anfragen"), secondary=("photovoltaik", "Zur Photovoltaik"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Smart Meter und Photovoltaik: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("Damit Ihr Smart Meter mehr ist als ein digitaler Zähler, verbindet EBZ Energie aus Villach "
                 "ihn über ein Energiemanagementsystem mit Ihrer PV-Anlage, Ihrem Speicher und Ihrer "
                 "Wärmepumpe. Als herstellerunabhängiger Fachbetrieb übernehmen wir Planung und Installation "
                 "in Kärnten und der Steiermark aus einer Hand, mit einem festangestellten Team aus "
                 "zertifizierten Fachkräften."),
        "grid": [
            ("Verständlich erklärt", "Wir übersetzen Zählerdaten in konkrete Empfehlungen."),
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EMS vom selben Team."),
            ("Herstellerunabhängig", "Wir wählen das System, das zu Ihrer Anlage passt."),
            ("Regional", "Beratung und Montage in Kärnten und der Steiermark."),
        ],
    },

    "faq": [
        ("Was ist ein Smart Meter einfach erklärt?",
         "Ein Smart Meter ist ein digitaler Stromzähler, der Ihren Verbrauch automatisch alle 15 Minuten "
         "misst und die Werte an den Netzbetreiber übermittelt. Statt einmal im Jahr abzulesen, sehen Sie "
         "Ihren Verbrauch tagesaktuell im Online-Portal."),
        ("Was misst ein Smart Meter?",
         "Er misst, wie viel Strom Sie verbrauchen, in Viertelstundenwerten, also 96 Werte pro Tag. Bei einer "
         "PV-Anlage erfasst er zusätzlich, wie viel Strom Sie ins Netz einspeisen. So entsteht ein genaues "
         "Bild von Erzeugung und Verbrauch."),
        ("Was ist der Unterschied zum alten Stromzähler?",
         "Der alte Ferraris-Zähler zeigt nur den Gesamtverbrauch und wird einmal jährlich abgelesen. Der "
         "Smart Meter misst laufend, überträgt die Daten automatisch und macht den Verbrauch im Portal "
         "sichtbar. Erst damit sind dynamische Tarife und Energiemanagement möglich."),
        ("Brauche ich einen Smart Meter?",
         "In Österreich werden die alten Zähler flächendeckend durch Smart Meter ersetzt, der Rollout ist "
         "gesetzlich vorgeschrieben und für Sie ohne gesonderte Anschaffungskosten. Ein Opt-out reduziert "
         "die Datenübertragung auf einen Jahreswert, ein Ablehnen des Geräts ist nicht vorgesehen."),
        ("Ist ein Smart Meter gefährlich oder schädlich?",
         "Nein. Ein Smart Meter ist ein digitaler Zähler, der Verbrauchsdaten erfasst und verschlüsselt "
         "überträgt. Wer die häufige Datenübertragung nicht möchte, kann den Opt-out nutzen und die "
         "Übermittlung einschränken."),
        ("Was habe ich als PV-Besitzer vom Smart Meter?",
         "Sie sehen Bezug und Einspeisung viertelstundengenau und erkennen, wann Überschuss ins Netz fließt. "
         "Mit einem Energiemanagementsystem legen Sie Speicher, Wärmepumpe und Wallbox genau in diese "
         "Stunden und steigern den Eigenverbrauch deutlich."),
        ("Kann ich mit dem Smart Meter Geld sparen?",
         "Nicht durch den Zähler allein. Sparen lässt sich mit dem, was er ermöglicht: einem dynamischen "
         "Stromtarif, der Teilnahme an einer Energiegemeinschaft und einem Energiemanagementsystem, das "
         "Verbrauch automatisch in günstige und sonnenreiche Stunden verschiebt."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Photovoltaik, Speicher, Wärmepumpen und Energiemanagementsysteme in Kärnten und der "
                    "Steiermark. Angaben zu Rollout und Datenübertragung beruhen auf den Informationen "
                    "von E-Control und oesterreich.gv.at, maßgeblich sind die Bedingungen Ihres Netzbetreibers."),
    "sources": [
        ("E-Control: Regulierungsbehörde für Strom und Gas", "https://www.e-control.at/"),
        ("oesterreich.gv.at: Informationen zum Smart Meter", "https://www.oesterreich.gv.at/"),
    ],
    "related": [
        ("/smart-meter/", "Smart Meter in Österreich: Funktion, Rollout und Nutzen"),
        ("/smart-meter-auslesen/", "Smart Meter auslesen: So sehen Sie Ihren Verbrauch"),
        ("/smart-meter-opt-out/", "Smart Meter Opt-out: Rechte, Ablauf und Folgen"),
        ("ems", "Energiemanagementsystem: Funktion und Nutzen"),
    ],
    "cta": {
        "h3": "Smart Meter sinnvoll nutzen",
        "text": "Wir zeigen Ihnen kostenlos, wie aus Zählerdaten automatisierte Ersparnis wird.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Smart Meter, PV und EMS sinnvoll kombinieren",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Zähler, "
                   "Anlage und Energiemanagement aus einer Hand verbindet."),
}
