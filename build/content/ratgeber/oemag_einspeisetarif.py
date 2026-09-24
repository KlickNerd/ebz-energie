"""Ratgeber: OeMAG-Einspeisetarif 2026 und die Energiegemeinschaft als Alternative.

Migriert von ebz-photovoltaik.at/oemag-einspeisetarif/ (Stand August 2026).
Marktpreise: Juli 2026 = 6,146 ct (Untergrenze), Q3 2026 = 10,923 ct. Ältere Werte
der Quelle bleiben als Verlauf. Folgemonate nach OeMAG-Veröffentlichung nachtragen.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "oemag-einspeisetarif",
    "path": "/oemag-einspeisetarif/",
    "title": "OeMAG-Einspeisetarif 2026: aktuell 6,146 ct | EBZ Energie",
    "description": ("OeMAG-Einspeisetarif Photovoltaik: Juli 2026 6,146 ct/kWh, Q3-Marktpreis 10,923 ct. "
                    "Berechnung, warum er an der Untergrenze klebt, was die EG bringt."),
    "eyebrow": "Einspeisetarif · OeMAG",
    "crumb_label": "OeMAG-Einspeisetarif 2026",
    "h1": "OeMAG-Einspeisetarif 2026: 6,146 Cent je kWh, warum er so niedrig ist und was Sie stattdessen tun können",
    "lead": ("Rund 3.000 Österreicher suchen jeden Monat nach dem aktuellen OeMAG-Tarif, und die meisten sind "
             "enttäuscht. Hier stehen die Zahlen, die Berechnung und die Alternative, die für den zugeordneten "
             "Überschuss bis zum Doppelten bringt."),
    "chips": [
        "Juli 2026: <b>6,146 ct/kWh</b>",
        "Q3-Marktpreis: <b>10,923 ct/kWh</b>",
        "Untergrenze: <b>60 %</b> des Marktpreises",
        "EG-Einspeisung: <b>8 bis 12 ct</b>",
    ],
    "date_published": "2026-08-20",
    "date_modified": "2026-09-24",
    "hero_img": "pv_card",
    "hero_alt": "Photovoltaikanlage, deren Überschuss zum OeMAG-Marktpreis oder in einer Energiegemeinschaft vergütet wird",

    "tldr": [
        "Der OeMAG-Einspeisetarif für Photovoltaik lag im Juli 2026 bei 6,146 Cent je kWh. Das ist die gesetzliche "
        "Untergrenze, weil die Börsenpreise zur Mittagszeit seit dem Frühjahr darunter liegen. Stand: September 2026.",
        "Der Tarif wird monatlich im Nachhinein aus dem Day-Ahead-Preis berechnet, begrenzt durch den "
        "Quartalsmarktpreis der E-Control (Obergrenze, Q3 2026: 10,923 Cent) und 60 Prozent davon (Untergrenze), "
        "abzüglich 0,408 Cent Ausgleichsenergiekosten.",
        "In einer Energiegemeinschaft verkaufen Sie den Überschuss zu einem selbst vereinbarten Preis, typisch "
        "8 bis 12 Cent, an Nachbarn. Was nicht zugeordnet wird, geht weiterhin an die OeMAG. Sie können also "
        "nur gewinnen.",
        "Bei 7.000 kWh Überschuss und 60 Prozent Zuordnung bringt die Gemeinschaft rund 160 Euro* Mehrerlös im "
        "Jahr, plus den Vorteil beim eigenen Bezug. EBZ Energie kombiniert PV, Speicher, Energiemanagement und "
        "Energiegemeinschaft in Kärnten und der Steiermark.",
    ],
    "kpis": [
        ("6,146 ct", "OeMAG-Tarif Juli 2026 (Photovoltaik)"),
        ("10,923 ct", "Quartalsmarktpreis Q3 2026 (Obergrenze)"),
        ("0,408 ct", "Abzug Ausgleichsenergie PV 2026"),
        ("60 %", "gesetzliche Untergrenze des Quartalsmarktpreises"),
    ],

    "sections": [
        ("Der aktuelle OeMAG-Einspeisetarif", "aktueller-tarif", f"""
<p>Die OeMAG, die Abwicklungsstelle für Ökostrom, ist gesetzlich verpflichtet, Strom aus PV-Anlagen zum
sogenannten Marktpreis abzunehmen. Seit Jänner 2024 wird dieser Preis monatlich und rückwirkend
festgelegt. Für Juli 2026 beträgt er 6,146 Cent je Kilowattstunde für Photovoltaik, der Juni lag bei
6,772 Cent. Der Quartalsmarktpreis der E-Control, der als Obergrenze dient, liegt für das dritte Quartal
2026 bei 10,923 Cent (109,23 Euro je MWh), im zweiten Quartal waren es 11,967 Cent.</p>
{A.table(
    ["Zeitraum 2026", "Quartalsmarktpreis (Obergrenze)", "Untergrenze PV (60 % minus 0,408 ct)", "OeMAG-Tarif PV"],
    [
        ["Q1 (Jänner bis März)", "9,250 ct", "5,142 ct", "Jänner und Februar nahe Obergrenze, März deutlich darunter"],
        ["Q2 (April bis Juni)", "11,967 ct", "6,772 ct", "Mai und Juni exakt an der Untergrenze: 6,772 ct"],
        ["Q3 (Juli bis September)", "10,923 ct", "6,146 ct", "Juli 6,146 ct; August und September nach Veröffentlichung durch die OeMAG"],
    ],
    hl_cols=(3,),
)}
<p>Quelle: OeMAG Marktpreis-Übersicht, E-Control. Werte gelten für Photovoltaik, der Windtarif liegt
geringfügig darunter. Stand: September 2026, die Folgemonate tragen wir nach ihrer Veröffentlichung
nach. Die Einordnung für Kärnten und die Steiermark finden Sie in unserem
{a('/marktpreis-2026/', 'Marktpreis-Überblick 2026')}.</p>
"""),
        ("So wird der OeMAG-Tarif berechnet", "berechnung", f"""
<p>Die Berechnung hat drei Stufen, und jede davon drückt den Tarif in Sommermonaten nach unten:</p>
{A.steps([
    ("Quartalsmarktpreis der E-Control",
     "Am Ende jedes Quartals ermittelt die E-Control aus den Terminmarktpreisen an der Strombörse EEX den "
     "Marktpreis gemäß Paragraf 41 Ökostromgesetz für das folgende Quartal. Für Q3 2026 sind das 10,923 Cent."),
    ("Monatlicher Day-Ahead-Durchschnitt der OeMAG",
     "Die OeMAG berechnet für jeden Monat den mengengewichteten Durchschnitt der Day-Ahead-Stundenpreise, "
     "also den Preis, der zu den Stunden gilt, in denen PV-Anlagen tatsächlich einspeisen. Mittags ist so "
     "viel Solarstrom im Netz, dass diese Preise niedrig oder sogar negativ sind."),
    ("Korridor und Abzug",
     "Der Monatswert wird in einen Korridor gezwängt: nach oben begrenzt durch den Quartalsmarktpreis, nach "
     "unten durch 60 Prozent davon. Seit 2026 werden zusätzlich die Kosten für Ausgleichsenergie abgezogen, "
     "bei PV 0,408 Cent je Kilowattstunde. Ergebnis für Juli 2026: 10,923 × 0,6 minus 0,408 = 6,146 Cent."),
])}
<p>Solange die Mittagspreise an der Börse wegen des vielen Solarstroms niedrig sind, klebt der Tarif an der
Untergrenze. Und die Untergrenze sinkt mit jedem Quartal, in dem der Terminmarkt nachgibt. Eine Erholung
ist nur in den Wintermonaten zu erwarten, in denen PV-Anlagen ohnehin wenig liefern.</p>
"""),
        ("Was die Alternativen bringen", "alternativen", f"""
<p>Wer mit dem OeMAG-Tarif unzufrieden ist, hat drei Hebel. Der erste ist der Einspeisevertrag mit einem
Energielieferanten wie Kelag, Energie Steiermark, Verbund oder einem der vielen Online-Anbieter. Diese
Tarife liegen teils über der OeMAG, sind aber meist an den Bezugstarif gekoppelt, oft befristet und
folgen mit Verzögerung demselben Börsenpreis. Der zweite Hebel ist der Eigenverbrauch: Jede
Kilowattstunde, die Sie selbst nutzen, ersetzt Strom zu 25 bis 35 Cent brutto. {a('batteriespeicher', 'Speicher')},
Wärmepumpe, Wallbox und Energiemanagement sind die Werkzeuge dafür. Der dritte Hebel ist die
{a('eg', 'Energiegemeinschaft')}, und sie setzt genau dort an, wo die ersten beiden aufhören: beim
Überschuss, der trotz Speicher übrig bleibt.</p>
{A.table(
    ["Wo der Überschuss landet", "Cent je kWh", "Wer bekommt oder zahlt"],
    [
        ["OeMAG-Tarif (Juli 2026)", "6,146 ct", "Erzeuger bekommt"],
        ["EG-Einspeisung (Beispiel*)", "10 ct", "Erzeuger bekommt"],
        ["EG-Bezug (Beispiel*)", "14 ct", "Abnehmer zahlt"],
        ["Lieferant, Arbeitspreis netto (Beispiel*)", "17 ct", "Abnehmer zahlt"],
    ],
    hl_cols=(1,),
)}
<p>Zwischen OeMAG-Tarif und Haushaltsstrompreis liegt eine Spanne von rund 10 Cent. Die Energiegemeinschaft
teilt diese Spanne zwischen Erzeuger und Abnehmer auf. Der Vergleich der Optionen im Überblick:</p>
{A.table(
    ["Option", "Preis je kWh Überschuss", "Bindung", "Risiko"],
    [
        ["OeMAG-Marktpreis", "6,1 bis 9,7 ct (2026)", "keine, jederzeit kündbar", "folgt der Börse, sinkt im Sommer"],
        ["Einspeisevertrag Lieferant", "5 bis 12 ct, oft befristet", "meist an Bezugstarif gekoppelt", "Aktionspreise laufen aus"],
        ["Energiegemeinschaft (EEG)", "8 bis 12 ct, selbst vereinbart", "1 bis 3 Monate Kündigungsfrist", "nur zugeordnete Menge, Rest an OeMAG"],
        ["Eigenverbrauch", "25 bis 35 ct brutto vermieden", "Investition in Speicher/EMS", "begrenzt durch Ihren Verbrauch"],
    ],
    hl_cols=(1,),
)}
<p><small>*EG-Preise und Lieferantenpreis sind Beispielwerte aus dem Markt, jede Gemeinschaft legt sie selbst
fest. Lieferantenpreis netto ohne Netz und Abgaben.</small></p>
"""),
        ("Warum die Energiegemeinschaft den OeMAG-Vertrag ergänzt, nicht ersetzt", "ergaenzung", f"""
<p>Ein Missverständnis, das wir in Beratungen oft ausräumen: Sie müssen den OeMAG-Vertrag nicht kündigen,
um einer Energiegemeinschaft beizutreten. Im Gegenteil. Die Gemeinschaft ordnet nur die Menge zu, die in
derselben Viertelstunde von einem Mitglied verbraucht wird. Alles andere bleibt Überschuss im Netz und
wird von Ihrem bestehenden Abnahmevertrag, also der OeMAG oder Ihrem Lieferanten, zum dortigen Tarif
vergütet. Die Energiegemeinschaft legt sich wie eine zweite Schicht darüber: Was sie abnimmt, bekommt den
besseren Preis, was sie nicht abnimmt, läuft wie bisher.</p>
{A.box("Rechnerisch bei 7.000 kWh Überschuss und 60 Prozent Zuordnung: 4.200 kWh zu 10 Cent* statt "
       "6,146 Cent ergeben 162 Euro Mehrerlös im Jahr. Dazu kommt der Abnehmervorteil in den Stunden, in "
       "denen Sie selbst aus der Gemeinschaft beziehen: bis zu 57 Prozent weniger Netzentgelt und keine "
       "Elektrizitätsabgabe im Nahbereich.", label="Beispiel:")}
<p>Der Netzentgelt-Abschlag gilt nur im Nahbereich, also am selben Trafo oder Umspannwerk. Wie er sich
zusammensetzt, steht im Artikel {a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft und Netzkosten')}.
Wie sich das mit Ihren Zahlen rechnet, zeigt der {a('eg_rechner', 'Energiegemeinschaft-Rechner')}.</p>
{A.cta("Mehr als den OeMAG-Tarif für Ihren Überschuss",
       "EBZ nimmt Sie in Kärnten und der Steiermark in eine Energiegemeinschaft auf. Ihr OeMAG-Vertrag "
       "bleibt als Auffangnetz bestehen.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("eg_rechner", "Ersparnis berechnen"))}
<p><small>*Beispielwert, jede Gemeinschaft legt den Einspeisepreis selbst fest.</small></p>
"""),
        ("Steuer und Versorgungsinfrastrukturbeitrag", "steuer", f"""
<p>Einspeiseerlöse sind für Privatpersonen bis 12.500 kWh im Jahr und bis 35 kWp Anlagenleistung
einkommensteuerfrei. Das gilt auch für Erlöse aus der Energiegemeinschaft, solange die Gesamtmenge unter
der Grenze bleibt. Neu durch das ElWG ist der Versorgungsinfrastrukturbeitrag für Einspeiser mit mehr als
20 kW: Er ist mit durchschnittlich 0,5 Euro je Megawattstunde gedeckelt, also 0,05 Cent je
Kilowattstunde, und ändert an der Rechnung praktisch nichts. Für eine typische Einfamilienhaus-Anlage
ist er nicht relevant. Keine Steuerberatung, maßgeblich sind die Informationen des Finanzministeriums
(siehe Quellen).</p>
"""),
        ("Fazit: OeMAG-Einspeisetarif und Energiegemeinschaft", "fazit", f"""
<p>Der OeMAG-Tarif ist 2026 kein Ertragsmodell mehr, sondern ein Auffangnetz auf gesetzlichem
Mindestniveau. Wer seinen Überschuss besser verwerten will, erhöht zuerst den Eigenverbrauch und verkauft
den Rest in einer Energiegemeinschaft an die Nachbarschaft. Beides zusammen bringt einen dreistelligen
Betrag im Jahr und macht Sie unabhängiger von der Börse. Die OeMAG bleibt im Hintergrund für alles, was
übrig ist. Den Beitritt beschreibt der Artikel {a('/energiegemeinschaft-beitreten/', 'Energiegemeinschaft beitreten')}.</p>
{A.cta("Überschuss neu verwerten: Speicher, EMS, Energiegemeinschaft",
       "Wir prüfen Ihre bestehende Anlage und zeigen, welcher Hebel bei Ihnen am meisten bringt.",
       primary=("kontakt", "Anlagencheck anfragen"), secondary=("eg_privat", "Zur Energiegemeinschaft mit EBZ"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Energiegemeinschaft: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und Wallboxen "
                 "in Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. "
                 "Dazu kommt die Energiegemeinschaft: Wir nehmen Sie in eine bestehende Gemeinschaft auf oder bauen "
                 "mit Ihnen eine eigene auf, abgerechnet über die Plattform unseres Partners energyfamily."),
        "grid": [
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EG-Anbindung vom selben Team."),
            ("Regional verankert", "Sitz in Villach, Montage in ganz Kärnten und der Steiermark."),
            ("Abrechnung inklusive", "Zählpunktfreigabe, Aufnahme und monatliche Abrechnung über energyfamily."),
            ("Auch für Bestandsanlagen", "Anlagencheck, Speicher-Nachrüstung und EG-Anbindung für bestehende PV."),
        ],
    },

    "faq": [
        ("Wie hoch ist der OeMAG-Einspeisetarif aktuell?",
         "Für Juli 2026 beträgt der OeMAG-Marktpreis für Photovoltaik 6,146 Cent je Kilowattstunde (Stand: "
         "September 2026). Die Folgemonate können gesetzlich nicht unter dieser Untergrenze liegen, solange der "
         "Q3-Marktpreis von 10,923 Cent gilt."),
        ("Warum ist der OeMAG-Tarif so niedrig?",
         "Weil er dem Börsenpreis zu den Stunden folgt, in denen PV-Anlagen einspeisen. Mittags ist so viel "
         "Solarstrom im Netz, dass die Day-Ahead-Preise niedrig oder negativ sind. Die gesetzliche Untergrenze "
         "von 60 Prozent des Quartalsmarktpreises verhindert, dass der Tarif noch weiter fällt."),
        ("Muss ich den OeMAG-Vertrag kündigen, wenn ich einer Energiegemeinschaft beitrete?",
         "Nein. Die Gemeinschaft ordnet nur den zeitgleich verbrauchten Anteil zu. Der restliche Überschuss wird "
         "weiterhin über den OeMAG-Vertrag zum Marktpreis vergütet. Der OeMAG-Vertrag bleibt als Auffangnetz "
         "bestehen."),
        ("Wie viel mehr bringt eine Energiegemeinschaft gegenüber der OeMAG?",
         "Typische EG-Einspeisepreise liegen bei 8 bis 12 Cent gegenüber 6,146 Cent bei der OeMAG im Juli 2026. "
         "Bei 7.000 kWh Überschuss und 60 Prozent Zuordnung sind das rund 160 Euro Mehrerlös im Jahr, plus den "
         "Vorteil beim eigenen Bezug aus der Gemeinschaft."),
        ("Ist ein Einspeisevertrag beim Lieferanten besser als die OeMAG?",
         "Teils liegen diese Tarife mit 5 bis 12 Cent über der OeMAG, sie sind aber meist an den Bezugstarif "
         "gekoppelt, oft befristet und folgen mit Verzögerung demselben Börsenpreis. Vergleichen Sie immer "
         "Einspeise- und Bezugspreis gemeinsam."),
        ("Sind Einspeiseerlöse steuerpflichtig?",
         "Für Privatpersonen sind Erlöse bis 12.500 kWh im Jahr bei Anlagen bis 35 kWp einkommensteuerfrei. Das "
         "gilt auch für Erlöse aus Energiegemeinschaften. Darüber hinausgehende Mengen sind steuerpflichtig. "
         "Keine Steuerberatung."),
        ("Wann wird der OeMAG-Tarif wieder steigen?",
         "Erst wenn die Mittagspreise an der Börse über die Untergrenze steigen, was typischerweise in den "
         "Wintermonaten der Fall ist. Für die Sommermonate ist bis auf Weiteres mit Werten an der Untergrenze zu "
         "rechnen, im Q3 2026 also 6,146 Cent."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert PV-Anlagen, "
                    "Speicher und Energiemanagementsysteme in Kärnten und der Steiermark und begleitet Kunden beim "
                    "Einstieg in Energiegemeinschaften. Die Marktpreise werden monatlich anhand der Veröffentlichungen "
                    "von OeMAG und E-Control aktualisiert. Keine Rechts- oder Steuerberatung."),
    "sources": [
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/marktpreis"),
        ("E-Control: Aktueller Marktpreis gemäß § 41 ÖSG",
         "https://www.e-control.at/industrie/oeko-energie/oekostrommarkt/marktpreise-gem-paragraph-20"),
        ("BMF: Steuerliche Aspekte bei Photovoltaikanlagen",
         "https://www.bmf.gv.at/themen/klimapolitik/steuerliche-aspekte-bei-photovoltaikanlagen-von-privatpersonen.html"),
        ("Koordinationsstelle: FAQs zum ElWG", "https://energiegemeinschaften.gv.at/faqs-zum-elwg/"),
    ],
    "related": [
        ("/marktpreis-2026/", "Marktpreis 2026: Lohnt sich Photovoltaik noch?"),
        ("/energiegemeinschaft-netzkosten/", "Netzkosten: Was in der Energiegemeinschaft günstiger wird"),
        ("/energiegemeinschaft-beitreten/", "Energiegemeinschaft beitreten: Ablauf in vier Schritten"),
        ("eg", "Energiegemeinschaft: Der Leitartikel"),
    ],
    "cta": {
        "h3": "Mehr für Ihren Überschuss",
        "text": "Anlagencheck, Speicher, Energiemanagement und Energiegemeinschaft: Wir zeigen, welcher Hebel bei Ihnen am meisten bringt.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Überschuss besser verwerten",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, Montage "
                   "und EG-Anbindung aus einer Hand übernimmt."),
}
