"""Ratgeber: OeMAG-Einspeisetarif 2026 und die Energiegemeinschaft als Alternative.

Migriert von ebz-photovoltaik.at/oemag-einspeisetarif/ (Stand August 2026).
Marktpreise (Stand November 2026): Oktober 2026 = 14,874 ct (aktueller Wert),
September 2026 = 10,168 ct und Juli 2026 = 6,146 ct (Verlaufswerte), Q3 2026 = 10,923 ct,
Q4 2026 = 15,282 ct (E-Control, 152,82 EUR/MWh, abgerufen 19.11.2026). Andere Monate
ohne belegten Wert, daher nicht genannt. Folgemonate nach OeMAG-Veröffentlichung nachtragen.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "oemag-einspeisetarif",
    "path": "/oemag-einspeisetarif/",
    "title": "OeMAG-Einspeisetarif 2026: aktuell 14,874 ct | EBZ Energie",
    "description": ("OeMAG-Einspeisetarif Photovoltaik: Oktober 2026 14,874 ct/kWh, September 10,168 ct, "
                    "Juli 6,146 ct. Berechnung, warum er schwankt, was die EG bringt."),
    "eyebrow": "Einspeisetarif · OeMAG",
    "crumb_label": "OeMAG-Einspeisetarif 2026",
    "h1": "OeMAG-Einspeisetarif 2026: 14,874 Cent je kWh im Oktober, warum er monatlich schwankt und was Sie stattdessen tun können",
    "lead": ("Rund 3.000 Österreicher suchen jeden Monat nach dem aktuellen OeMAG-Tarif, und die meisten sind "
             "überrascht, wie stark er schwankt. Hier stehen die aktuellen Zahlen, die Berechnung und die "
             "Alternative Energiegemeinschaft, die den Überschuss planbar macht und beim Bezug Netzentgelte spart."),
    "chips": [
        "Oktober 2026: <b>14,874 ct/kWh</b>",
        "September 2026: <b>10,168 ct/kWh</b>",
        "Juli 2026: <b>6,146 ct/kWh</b>",
        "EG-Einspeisung: <b>8 bis 12 ct</b>",
    ],
    "date_published": "2026-08-20",
    "date_modified": "2026-11-20",
    "hero_img": "pv_card",
    "hero_alt": "Photovoltaikanlage, deren Überschuss zum OeMAG-Marktpreis oder in einer Energiegemeinschaft vergütet wird",

    "tldr": [
        "Der OeMAG-Einspeisetarif für Photovoltaik beträgt für Oktober 2026 14,874 Cent je kWh (Stand November 2026). "
        "Im September 2026 lag er bei 10,168 Cent, im Juli 2026 mit 6,146 Cent an der gesetzlichen Untergrenze. Der "
        "Wert schwankt monatlich mit den Börsenpreisen zu den Einspeisestunden.",
        "Der Tarif wird monatlich im Nachhinein aus dem Day-Ahead-Preis berechnet, begrenzt durch den "
        "Quartalsmarktpreis der E-Control (Obergrenze, Q3 2026: 10,923 Cent, Q4 2026: 15,282 Cent) und 60 Prozent "
        "davon (Untergrenze), "
        "abzüglich 0,408 Cent Ausgleichsenergiekosten.",
        "In einer Energiegemeinschaft verkaufen Sie den Überschuss zu einem selbst vereinbarten, fixen Preis, typisch "
        "8 bis 12 Cent*, an Nachbarn. Was nicht zugeordnet wird, geht weiterhin an die OeMAG. Der OeMAG-Vertrag "
        "bleibt als Auffangnetz bestehen.",
        "Ob der Erzeuger mehr bekommt als bei der OeMAG, hängt vom Monat ab: Gegenüber dem Juli-Wert bringt ein "
        "EG-Preis von 10 Cent* ein Plus, gegenüber dem September-Wert nicht und gegenüber dem Oktober-Wert ein Minus. Verlässlich sind der Bezugsvorteil "
        "(in einer lokalen Erneuerbare-Energie-Gemeinschaft bis zu 57 Prozent weniger Netzentgelt) und die "
        "Planbarkeit. EBZ Energie kombiniert PV, "
        "Speicher, Energiemanagement und Energiegemeinschaft in Kärnten und der Steiermark.",
    ],
    "kpis": [
        ("14,874 ct", "OeMAG-Tarif Oktober 2026 (Photovoltaik)"),
        ("6,146 ct", "OeMAG-Tarif Juli 2026 (Untergrenze)"),
        ("15,282 ct", "Quartalsmarktpreis Q4 2026 (Obergrenze)"),
        ("0,408 ct", "Abzug Ausgleichsenergie PV 2026"),
    ],

    "sections": [
        ("Der aktuelle OeMAG-Einspeisetarif", "aktueller-tarif", f"""
<p><b>Der OeMAG-Marktpreis für Photovoltaik beträgt für Oktober 2026 14,874 Cent je Kilowattstunde</b>
(Quelle: oem-ag.at/marktpreis, monatlich im Nachhinein veröffentlicht, Stand 19. November 2026). Im September
2026 lag er bei 10,168 Cent, im Juli 2026 bei 6,146 Cent, der Untergrenze des dritten Quartals. Der Marktpreis gilt für Anlagen im
OeMAG-Marktpreismodell, nicht für alte Fördertarife nach Paragraf 12 Ökostromgesetz.</p>
<p>Die OeMAG, die Abwicklungsstelle für Ökostrom, ist gesetzlich verpflichtet, Strom aus PV-Anlagen zum
sogenannten Marktpreis abzunehmen. Seit Jänner 2024 wird dieser Preis monatlich und rückwirkend
festgelegt. Der Juli 2026 lag bei 6,146 Cent, der September bei 10,168 Cent, der Oktober bei 14,874 Cent.
Der Quartalsmarktpreis der E-Control, der als Obergrenze dient, liegt für das vierte Quartal
2026 bei 15,282 Cent (152,82 Euro je MWh), im dritten Quartal waren es 10,923 Cent (109,23 Euro je MWh).</p>
{A.table(
    ["Zeitraum 2026", "Quartalsmarktpreis (Obergrenze)", "Untergrenze PV (60 % minus 0,408 ct)", "OeMAG-Tarif PV"],
    [
        ["Q3 (Juli bis September)", "10,923 ct", "6,146 ct", "Juli 6,146 ct (Untergrenze), September 10,168 ct (nahe Obergrenze)"],
        ["Q4 (Oktober bis Dezember)", "15,282 ct", "8,761 ct", "Oktober 14,874 ct (an der Obergrenze, 15,282 minus 0,408 ct)"],
    ],
    hl_cols=(3,),
)}
<p>Quelle: OeMAG Marktpreis-Übersicht, E-Control. Werte gelten für Photovoltaik, der Windtarif liegt
geringfügig darunter. Stand: November 2026, die Folgemonate tragen wir nach ihrer Veröffentlichung
nach. Die Einordnung für Kärnten und die Steiermark finden Sie in unserem
{a('/marktpreis-2026/', 'Marktpreis-Überblick 2026')}.</p>
"""),
        ("So wird der OeMAG-Tarif berechnet", "berechnung", f"""
<p>Die Berechnung hat drei Stufen, und jede davon drückt den Tarif in Sommermonaten nach unten:</p>
{A.steps([
    ("Quartalsmarktpreis der E-Control",
     "Am Ende jedes Quartals ermittelt die E-Control aus den Terminmarktpreisen an der Strombörse EEX den "
     "Marktpreis gemäß Paragraf 41 Ökostromgesetz für das folgende Quartal. Für Q3 2026 sind das 10,923 Cent, "
     "für Q4 2026 15,282 Cent."),
    ("Monatlicher Day-Ahead-Durchschnitt der OeMAG",
     "Die OeMAG berechnet für jeden Monat den mengengewichteten Durchschnitt der Day-Ahead-Stundenpreise, "
     "also den Preis, der zu den Stunden gilt, in denen PV-Anlagen tatsächlich einspeisen. Mittags ist so "
     "viel Solarstrom im Netz, dass diese Preise niedrig oder sogar negativ sind."),
    ("Korridor und Abzug",
     "Der Monatswert wird in einen Korridor gezwängt: nach oben begrenzt durch den Quartalsmarktpreis, nach "
     "unten durch 60 Prozent davon. Seit 2026 werden zusätzlich die Kosten für Ausgleichsenergie abgezogen, "
     "bei PV 0,408 Cent je Kilowattstunde. Ergebnis für Juli 2026: 10,923 × 0,6 minus 0,408 = 6,146 Cent. "
     "Im September 2026 lag der Monatswert mit 10,168 Cent dagegen nahe der Obergrenze, im Oktober 2026 mit "
     "14,874 Cent genau an der Obergrenze des vierten Quartals: 15,282 minus 0,408 = 14,874 Cent."),
])}
<p>In Monaten mit viel Solarstrom und niedrigen Mittagspreisen fällt der Tarif auf die Untergrenze, wie im
Juli 2026. Steigen die Börsenpreise zu den Einspeisestunden, nähert er sich der Obergrenze, wie im
September 2026, oder erreicht sie, wie im Oktober 2026. Planbar ist er damit nicht: Innerhalb des dritten
Quartals 2026 schwankte er um rund 4 Cent, von Juli bis Oktober 2026 um rund 8,7 Cent. Die Untergrenze selbst sinkt zudem mit jedem Quartal, in dem der Terminmarkt nachgibt.</p>
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
        ["OeMAG-Tarif (Oktober 2026)", "14,874 ct", "Erzeuger bekommt"],
        ["OeMAG-Tarif (September 2026)", "10,168 ct", "Erzeuger bekommt"],
        ["OeMAG-Tarif (Juli 2026)", "6,146 ct", "Erzeuger bekommt"],
        ["EG-Einspeisung (Beispiel*)", "10 ct", "Erzeuger bekommt"],
        ["EG-Bezug (Beispiel*)", "14 ct", "Abnehmer zahlt"],
        ["Lieferant, Arbeitspreis netto (Beispiel*)", "17 ct", "Abnehmer zahlt"],
    ],
    hl_cols=(1,),
)}
<p>Zwischen OeMAG-Tarif und Haushaltsstrompreis liegt je nach Monat eine Spanne von rund 2 bis 11 Cent. Die
Energiegemeinschaft teilt diese Spanne zwischen Erzeuger und Abnehmer auf. Liegt der Marktpreis wie im
September 2026 (10,168 Cent) oder Oktober 2026 (14,874 Cent) auf oder über dem EG-Einspeisepreis von 10 Cent*,
bringt die Gemeinschaft dem Erzeuger keinen Mehrerlös, im Oktober sogar weniger als die OeMAG.
Der Vorteil der Gemeinschaft liegt dann beim Abnehmer (Bezugspreis unter dem Lieferantentarif,
Netzentgelt-Rabatt in der EEG im Nahbereich) und in der Planbarkeit: Der EG-Preis ist fix vereinbart, der OeMAG-Tarif
schwankt monatlich. Der Vergleich der Optionen im Überblick:</p>
{A.table(
    ["Option", "Preis je kWh Überschuss", "Bindung", "Risiko"],
    [
        ["OeMAG-Marktpreis", "6,1 bis 14,9 ct (2026)", "keine, jederzeit kündbar", "folgt der Börse, schwankt monatlich"],
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
fix vereinbarten Preis, was sie nicht abnimmt, läuft wie bisher.</p>
{A.box("Rechnerisch bei 7.000 kWh Überschuss und 60 Prozent Zuordnung: 4.200 kWh zu 10 Cent* bringen "
       "420 Euro im Jahr. Bei der OeMAG wären es je nach Monatswert 258 Euro (Juli 2026: 6,146 Cent) bis "
       "625 Euro (Oktober 2026: 14,874 Cent). Der Erzeugervorteil hängt also vom Marktpreis ab und kann sich in "
       "Monaten mit hohem Tarif ins Gegenteil drehen; dafür ist der EG-Preis fix und planbar. Verlässlich ist der Abnehmervorteil in den Stunden, in denen Sie "
       "selbst aus der Gemeinschaft beziehen: in einer lokalen EEG bis zu 57 Prozent weniger Netzentgelt und "
       "keine Elektrizitätsabgabe.", label="Beispiel:")}
<p>Der Netzentgelt-Abschlag gilt nur im Nahbereich, also am selben Trafo oder Umspannwerk, und bis Ende 2026 nur
für Mitglieder einer Erneuerbare-Energie-Gemeinschaft. Bürgerenergiegemeinschaften und Peer-to-Peer-Verträge
sollen ihn im Nahbereich nach heutigem Stand ab 1. Jänner 2027 erhalten, die Höhe legt die E-Control fest.
Wie er sich zusammensetzt, steht im Artikel {a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft und Netzkosten')}.
Wie sich das mit Ihren Zahlen rechnet, zeigt der {a('eg_rechner', 'Energiegemeinschaft-Rechner')}, welche
Einspeise- und Bezugspreise bestehende Gemeinschaften zahlen, der
{a('/energiegemeinschaft-vergleich/', 'Energiegemeinschaft-Vergleich')}.</p>
{A.cta("Ein planbarer Preis für Ihren Überschuss",
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
<p>Der OeMAG-Tarif ist 2026 kein planbares Ertragsmodell, sondern ein Auffangnetz, das zwischen
6,146 Cent (Juli) und 14,874 Cent (Oktober) schwankte. Wer seinen Überschuss besser
verwerten will, erhöht zuerst den Eigenverbrauch und teilt den Rest in einer Energiegemeinschaft mit der
Nachbarschaft: zu einem fix vereinbarten Preis und mit Netzentgelt-Rabatt beim Bezug. Beides zusammen
macht Sie unabhängiger von der Börse. Die OeMAG bleibt im Hintergrund für alles, was
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
                 "in Kärnten und der Steiermark, mit zertifizierten Fachkräften. "
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
         "Für Oktober 2026 beträgt der OeMAG-Marktpreis für Photovoltaik 14,874 Cent je Kilowattstunde (Stand: "
         "November 2026). Im September 2026 lag er bei 10,168 Cent, im Juli 2026 mit 6,146 Cent an der gesetzlichen "
         "Untergrenze. Der Wert schwankt monatlich innerhalb des Korridors aus Quartalsmarktpreis (Q4 2026: "
         "15,282 Cent) und 60 Prozent davon."),
        ("Warum schwankt der OeMAG-Tarif so stark?",
         "Weil er dem Börsenpreis zu den Stunden folgt, in denen PV-Anlagen einspeisen. In Monaten mit viel "
         "Mittagssolarstrom sind die Day-Ahead-Preise niedrig oder negativ, der Tarif fällt auf die Untergrenze "
         "(Juli 2026: 6,146 Cent). Ziehen die Börsenpreise an, nähert er sich der Obergrenze (September 2026: "
         "10,168 Cent) oder erreicht sie (Oktober 2026: 14,874 Cent). Die gesetzliche Untergrenze von 60 Prozent des Quartalsmarktpreises begrenzt den Absturz."),
        ("Muss ich den OeMAG-Vertrag kündigen, wenn ich einer Energiegemeinschaft beitrete?",
         "Nein. Die Gemeinschaft ordnet nur den zeitgleich verbrauchten Anteil zu. Der restliche Überschuss wird "
         "weiterhin über den OeMAG-Vertrag zum Marktpreis vergütet. Der OeMAG-Vertrag bleibt als Auffangnetz "
         "bestehen."),
        ("Wie viel mehr bringt eine Energiegemeinschaft gegenüber der OeMAG?",
         "Das hängt vom Monat ab. Typische EG-Einspeisepreise liegen bei 8 bis 12 Cent (Beispielwerte). Gegenüber "
         "dem Juli-Wert der OeMAG von 6,146 Cent ist das ein Plus, gegenüber dem September-Wert von 10,168 Cent "
         "kaum und gegenüber dem Oktober-Wert von 14,874 Cent nicht. Verlässlich sind der fixe Preis, der Bezugsvorteil mit bis zu 57 Prozent weniger Netzentgelt in "
         "einer lokalen EEG und die wegfallende Elektrizitätsabgabe."),
        ("Ist ein Einspeisevertrag beim Lieferanten besser als die OeMAG?",
         "Diese Tarife liegen meist bei 5 bis 12 Cent und damit je nach Monat über oder unter der OeMAG, sie sind "
         "aber häufig an den Bezugstarif "
         "gekoppelt, oft befristet und folgen mit Verzögerung demselben Börsenpreis. Vergleichen Sie immer "
         "Einspeise- und Bezugspreis gemeinsam."),
        ("Sind Einspeiseerlöse steuerpflichtig?",
         "Für Privatpersonen sind Erlöse bis 12.500 kWh im Jahr bei Anlagen bis 35 kWp einkommensteuerfrei. Das "
         "gilt auch für Erlöse aus Energiegemeinschaften. Darüber hinausgehende Mengen sind steuerpflichtig. "
         "Keine Steuerberatung."),
        ("Wie entwickelt sich der OeMAG-Tarif?",
         "Er folgt den Börsenpreisen zu den Einspeisestunden. Im Juli 2026 lag er an der Untergrenze (6,146 Cent), "
         "im September 2026 mit 10,168 Cent nahe der Obergrenze von 10,923 Cent, im Oktober 2026 mit 14,874 Cent "
         "an der Obergrenze des vierten Quartals (15,282 Cent minus 0,408 Cent). In Monaten mit viel "
         "Mittagssolarstrom ist mit niedrigen Werten zu rechnen, eine verlässliche Prognose für einzelne Monate "
         "gibt es nicht. Wir aktualisieren die Werte monatlich nach Veröffentlichung durch die OeMAG."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert PV-Anlagen, "
                    "Speicher und Energiemanagementsysteme in Kärnten und der Steiermark und begleitet Kunden beim "
                    "Einstieg in Energiegemeinschaften. Die Marktpreise werden monatlich anhand der Veröffentlichungen "
                    "von OeMAG und E-Control aktualisiert, Stand November 2026. Keine Rechts- oder Steuerberatung."),
    "sources": [
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/marktpreis"),
        ("E-Control: Aktueller Marktpreis gemäß § 41 ÖSG",
         "https://www.e-control.at/marktteilnehmer/oeko-energie/marktpreis"),
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
