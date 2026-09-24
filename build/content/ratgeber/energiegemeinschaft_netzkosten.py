"""Ratgeber: Energiegemeinschaft und Netzkosten.

Migriert von ebz-photovoltaik.at/energiegemeinschaft-netzkosten/ (Stand August 2026),
Inhalt freigegeben, auf die Ratgeber-Vorlage umgestellt. Richtwerte der Netzentgelte und
EG-Preise (14 ct Bezug, 17 ct Lieferant) als Beispielwerte gekennzeichnet.
Glatte Euro-Beträge ohne Nachkommastellen geschrieben (Validator-Regel gegen die Bewertungszahl).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "energiegemeinschaft-netzkosten",
    "path": "/energiegemeinschaft-netzkosten/",
    "title": "Energiegemeinschaft Netzkosten: bis 57 % weniger | EBZ",
    "description": "Netzkosten in der Energiegemeinschaft: Netznutzung und Netzverlust minus 57 % lokal, 28 % regional, Elektrizitätsabgabe entfällt. Rechenbeispiel je kWh.",
    "eyebrow": "Energiegemeinschaft · Netzkosten",
    "crumb_label": "Energiegemeinschaft und Netzkosten",
    "h1": "Energiegemeinschaft und Netzkosten: bis zu 57 Prozent weniger Netzentgelt, Position für Position",
    "lead": ("Der Netzentgelt-Abschlag ist das stärkste Argument für die Energiegemeinschaft und gleichzeitig das am "
             "häufigsten missverstandene. Hier ist die Rechnung, Position für Position."),
    "chips": [
        "Netznutzung: <b>minus 57 %</b> lokal",
        "Netzverlust: <b>minus 57 %</b> lokal",
        "E-Abgabe 1,5 ct: <b>entfällt</b>",
        "Förderbeitrag: <b>entfällt</b>",
    ],
    "date_published": "2026-08-15",
    "date_modified": "2026-09-24",
    "hero_img": "gen_gewerbe",
    "hero_alt": "Photovoltaikanlage auf einem Gewerbedach, im Hintergrund Trafostation und Wohnsiedlung",

    "tldr": [
        "Auf EG-Strom sinkt der Arbeitspreis des Netznutzungs- und Netzverlustentgelts um 57 Prozent (lokal) oder "
        "28 Prozent (regional). Die Grundpauschale und der Leistungspreis bleiben unverändert.",
        "Bei Erneuerbaren-Energie-Gemeinschaften entfallen zusätzlich die Elektrizitätsabgabe von 1,5 Cent pro kWh "
        "und der Erneuerbaren-Förderbeitrag. Bürgerenergiegemeinschaften bekommen das nicht.",
        "In Summe werden aus typisch 11 bis 13 Cent Netz- und Abgabenanteil je Kilowattstunde rund 4 bis 6 Cent. Dazu "
        "kommt der meist günstigere EG-Strompreis.",
        "Rechenbeispiel 1.000 kWh aus einer lokalen EEG: rund 105 Euro Ersparnis im Jahr, also 10,5 Cent je "
        "zugeordneter Kilowattstunde, davon 7,5 Cent aus Netz und Abgaben.",
        "Der Abschlag gilt nur für die zugeordnete Menge. Wie viel das ist, hängt von Ihrem Verbrauchsprofil und der "
        "Gemeinschaft ab: 25 Prozent ohne Tagesverbrauch, 40 bis 60 Prozent mit Wärmepumpe, E-Auto oder Homeoffice.",
    ],
    "kpis": [
        ("57 %", "Abschlag lokal (selber Trafo)"),
        ("28 %", "Abschlag regional (selbes Umspannwerk)"),
        ("1,5 ct", "Elektrizitätsabgabe entfällt je kWh (EEG)"),
        ("~10,5 ct", "Ersparnis je zugeordneter kWh im Beispiel*"),
    ],

    "sections": [
        ("Woraus Ihre Stromrechnung besteht", "stromrechnung", f"""
<p>Um den Vorteil der Energiegemeinschaft zu verstehen, muss man die Stromrechnung in ihre drei Teile zerlegen.
Erstens der Energiepreis, den Ihr Lieferant verlangt, aktuell je nach Tarif 12 bis 20 Cent netto pro Kilowattstunde.
Zweitens die Netzkosten, die der Netzbetreiber nach der Systemnutzungsentgelte-Verordnung der E-Control verrechnet:
Netznutzungsentgelt, Netzverlustentgelt und eine Grundpauschale. Drittens Steuern und Abgaben: Elektrizitätsabgabe,
Erneuerbaren-Förderbeitrag, Erneuerbaren-Förderpauschale und die Umsatzsteuer auf alles. Die Energiegemeinschaft
greift bei Teil zwei und drei an, und zwar nur bei den Positionen, die je Kilowattstunde verrechnet werden.</p>
{A.table(
    ["Position je kWh", "Richtwert Haushalt 2026*", "Lokale EEG", "Regionale EEG", "BEG im Nahbereich"],
    [
        ["Netznutzungsentgelt (Arbeit)", "7 bis 10 ct", "minus 57 %", "minus 28 %", "minus 57 / 28 % ab Okt. 2026"],
        ["Netzverlustentgelt", "0,5 bis 1 ct", "minus 57 %", "minus 28 %", "minus 57 / 28 % ab Okt. 2026"],
        ["Elektrizitätsabgabe", "1,5 ct", "entfällt", "entfällt", "bleibt"],
        ["Erneuerbaren-Förderbeitrag", "ca. 1 ct", "entfällt", "entfällt", "bleibt"],
        ["Grundpauschale, Leistungspreis, Förderpauschale", "fix pro Jahr", "unverändert", "unverändert", "unverändert"],
    ],
    hl_cols=(2, 3),
)}
<p><small>*Richtwerte, sie schwanken je nach Netzgebiet. Die exakten Sätze Ihres Netzgebiets stehen auf Ihrer
Netzrechnung und in der jeweils gültigen Systemnutzungsentgelte-Verordnung der E-Control.</small></p>
"""),
        ("Lokal oder regional: Der Nahbereich bestimmt den Abschlag", "nahbereich", f"""
<p>Der Abschlag von 57 Prozent gilt für den Lokalbereich, also wenn Erzeuger und Verbraucher an derselben
Trafostation auf der Niederspannungsebene hängen. Der Abschlag von 28 Prozent gilt für den Regionalbereich, wenn
beide am selben Umspannwerk auf der Mittelspannungsebene angeschlossen sind. Wer ausschließlich auf den Netzebenen
4 und 5 teilnimmt, was nur für größere Betriebe relevant ist, kann bis zu 64 Prozent erreichen. Die Logik dahinter:
Strom, der im Ortsnetz bleibt, belastet die übergeordneten Netzebenen nicht, deshalb müssen Teilnehmer diese auch
nicht mitbezahlen.</p>
{A.box("Der Abschlag ist an den Nahbereich gebunden. Wer Strom österreichweit teilt, etwa in einer "
       "Bürgerenergiegemeinschaft mit Verwandten in einem anderen Bundesland, zahlt das volle Netzentgelt. Der "
       "Vorteil liegt dann allein im vereinbarten Strompreis.", label="Wichtig:")}
<p>Ob Ihr Zählpunkt lokal oder regional mit einer Gemeinschaft verbunden ist, prüft der Netzbetreiber bei der
Anmeldung. Wie Sie die passende Gemeinschaft finden, steht im Artikel
{a('/energiegemeinschaft-finden/', 'Energiegemeinschaft finden')}.</p>
"""),
        ("Rechenbeispiel: 1.000 kWh aus der Gemeinschaft", "rechenbeispiel", f"""
<p>Nehmen wir einen Haushalt in Kärnten, der 1.000 kWh im Jahr aus einer lokalen Erneuerbaren-Energie-Gemeinschaft
zugeordnet bekommt. Als Richtwerte setzen wir 8 Cent Netznutzung, 0,7 Cent Netzverlust, 1,5 Cent Elektrizitätsabgabe
und 1 Cent Förderbeitrag an, dazu 17 Cent Arbeitspreis beim Lieferanten und 14 Cent EG-Preis*.</p>
{A.table(
    ["Position", "Normalbezug", "Lokale EEG", "Ersparnis"],
    [
        ["Netznutzung 1.000 kWh", "80 €", "34,40 €", "45,60 €"],
        ["Netzverlust 1.000 kWh", "7 €", "3,01 €", "3,99 €"],
        ["Elektrizitätsabgabe", "15 €", "0 €", "15 €"],
        ["Erneuerbaren-Förderbeitrag", "10 €", "0 €", "10 €"],
        ["Energiepreis (17 ct Lieferant vs. 14 ct EG)", "170 €", "140 €", "30 €"],
        ["Summe netto", "282 €", "177,41 €", "104,59 €"],
    ],
    hl_cols=(3,),
)}
<p>Rund 10,5 Cent Ersparnis je zugeordneter Kilowattstunde, davon etwa 7,5 Cent aus Netz und Abgaben und 3 Cent aus
dem günstigeren Energiepreis. Bei einer regionalen Gemeinschaft sind es rund 8 Cent. Die Zahl, die am Ende zählt,
ist aber die zugeordnete Menge: 1.000 kWh entsprechen bei einem 4.000-kWh-Haushalt einer Zuordnungsquote von
25 Prozent, was für einen Haushalt ohne Tagesverbrauch realistisch ist. Mit Wärmepumpe, E-Auto oder Homeoffice sind
40 bis 60 Prozent erreichbar. Den Effekt für Ihren Haushalt zeigt der
{a('eg_rechner', 'Energiegemeinschaft-Rechner')}.</p>
<p><small>*Beispielkonditionen: EG-Bezugspreis 14 Cent, Lieferantenpreis 17 Cent netto je kWh, Netzentgelt-Richtwerte
2026. Jede Gemeinschaft legt ihre Preise selbst fest, die Konditionen bei EBZ nennen wir im Erstgespräch.</small></p>
{A.cta("Netzkosten senken, ohne den Lieferanten zu wechseln",
       "Die Energiegemeinschaft wirkt auf der Netzrechnung, nicht beim Lieferanten. EBZ bringt Sie in Kärnten und der "
       "Steiermark in eine passende Gemeinschaft.",
       secondary=("eg_rechner", "Ersparnis berechnen"))}
"""),
        ("Was auf der Netzrechnung zu sehen ist", "netzrechnung", f"""
<p>Nach dem Beitritt weist der Netzbetreiber auf der Netzrechnung zwei Positionen aus: den Normalbezug mit vollem
Tarif und den EG-Bezug mit reduziertem Arbeitspreis. Die Abgabenbefreiung erscheint ebenfalls dort. Der Energiepreis
für den EG-Strom kommt dagegen nicht vom Netzbetreiber, sondern von der Gemeinschaft, in der Regel über die
Abrechnungsplattform. Sie haben also drei Rechnungen: Netzbetreiber, Lieferant für den Reststrom und Gemeinschaft für
den EG-Strom. Plattformen wie energyfamily stellen die Gemeinschaftsabrechnung monatlich in der App dar. Welche
Gebühren dafür üblich sind, steht im Artikel {a('/energiegemeinschaft-kosten/', 'Was eine Energiegemeinschaft kostet')}.</p>
"""),
        ("Gilt das auch für Erzeuger?", "erzeuger", f"""
<p>Der Netzentgelt-Abschlag betrifft den Bezug, nicht die Einspeisung. Als Erzeuger profitieren Sie davon in den
Stunden, in denen Sie selbst aus der Gemeinschaft beziehen, also abends und im Winter. Auf der Einspeiseseite liegt
Ihr Vorteil im höheren EG-Preis gegenüber dem OeMAG-Tarif, den Vergleich zieht der Artikel
{a('/oemag-einspeisetarif/', 'OeMAG-Einspeisetarif oder Energiegemeinschaft')}.</p>
<p>Eine Neuerung des ElWG betrifft größere Einspeiser: Für Anlagen mit mehr als 20 kW eingespeister Leistung wird ein
Versorgungsinfrastrukturbeitrag fällig, gedeckelt mit durchschnittlich 0,5 Euro je Megawattstunde, also 0,05 Cent je
Kilowattstunde. Er gilt auch innerhalb von Energiegemeinschaften, fällt aber wirtschaftlich kaum ins Gewicht.</p>
"""),
        ("Was sich ab 2027 ändern könnte", "ab-2027", f"""
<p>Das ElWG ermächtigt die E-Control, die Höhe der Abschläge per Verordnung neu festzulegen. Die neue
Netzentgeltstruktur tritt mit 1. Jänner 2027 in Kraft, ob sie die 57 und 28 Prozent verändert, ist offen.
Gleichzeitig erhalten Bürgerenergiegemeinschaften und Peer-to-Peer-Verträge ab Oktober 2026 im Nahbereich ebenfalls
den reduzierten Netztarif.</p>
{A.box_dark("Die EEG bleibt das stärkste Modell",
    "Die Abgabenbefreiung bleibt ausdrücklich den Erneuerbaren-Energie-Gemeinschaften vorbehalten, was die EEG "
    "auch künftig zum wirtschaftlich stärksten Modell macht. Wir aktualisieren diesen Artikel, sobald die Verordnung "
    "vorliegt.")}
"""),
        ("Fazit: Netzkosten in der Energiegemeinschaft", "fazit", f"""
<p>Der Netzentgelt-Abschlag ist kein Rabatt auf die ganze Rechnung, sondern eine deutliche Ersparnis auf die
zugeordnete Menge: rund 7 bis 8 Cent je Kilowattstunde aus Netz und Abgaben, plus den Preisvorteil beim EG-Strom.
Wer seinen Verbrauch in die Erzeugungszeiten legt, macht aus einem kleinen Vorteil einen großen. Genau dafür sind
{a('batteriespeicher', 'Speicher')} und Energiemanagement da, für Letzteres gibt es 2026 sogar eine eigene
{a('/ems-foerderung/', 'EMS-Förderung')}. Wie der Einstieg abläuft, steht im Artikel
{a('/energiegemeinschaft-beitreten/', 'Energiegemeinschaft beitreten')}.</p>
{A.cta("Rechnen Sie Ihre Netzersparnis nach",
       "Der Rechner berücksichtigt Netzebene, Abgaben und Ihre Zuordnungsquote.",
       primary=("kontakt", "Beratung anfragen"), secondary=("eg_rechner", "Zum Rechner"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Energiegemeinschaft: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und Wallboxen in "
                 "Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. Dazu kommt "
                 "die Energiegemeinschaft: Wir nehmen Sie in eine bestehende Gemeinschaft auf oder bauen mit Ihnen eine "
                 "eigene auf, abgerechnet über die Plattform unseres Partners energyfamily."),
        "grid": [
            ("Netzebene geprüft", "Wir fragen ab, ob Ihr Zählpunkt lokal (57 %) oder regional (28 %) verbunden ist."),
            ("Verbrauch in die Sonne gelegt", "Speicher, Wallbox und EMS heben Ihre Zuordnungsquote."),
            ("Abrechnung inklusive", "Zählpunktfreigabe, Aufnahme und monatliche Abrechnung über energyfamily."),
            ("Kostenlose Erstberatung", "Wir rechnen Ihre Netzersparnis mit echten Richtwerten durch."),
        ],
    },

    "faq": [
        ("Wie viel Netzentgelt spare ich in einer Energiegemeinschaft?",
         "Auf den EG-Strom 57 Prozent des Arbeitspreises von Netznutzungs- und Netzverlustentgelt im Lokalbereich, "
         "28 Prozent im Regionalbereich. Grundpauschale und Leistungspreis bleiben unverändert."),
        ("Entfällt die Elektrizitätsabgabe in jeder Energiegemeinschaft?",
         "Nein. Die Befreiung von Elektrizitätsabgabe (1,5 Cent je kWh) und Erneuerbaren-Förderbeitrag gilt nur für "
         "Erneuerbare-Energie-Gemeinschaften und gemeinschaftliche Erzeugungsanlagen, nicht für "
         "Bürgerenergiegemeinschaften. Das bleibt auch nach dem ElWG so."),
        ("Sinkt das Netzentgelt auf meine gesamte Stromrechnung?",
         "Nein, nur auf die Menge, die Ihnen aus der Gemeinschaft zugeordnet wird. Alles, was Sie aus dem "
         "öffentlichen Netz von Ihrem Lieferanten beziehen, wird weiterhin zum vollen Tarif verrechnet."),
        ("Wie viel Cent je kWh spare ich insgesamt?",
         "Bei Richtwerten von 8 Cent Netznutzung, 0,7 Cent Netzverlust, 1,5 Cent Elektrizitätsabgabe und 1 Cent "
         "Förderbeitrag sind es in einer lokalen EEG rund 7,5 Cent aus Netz und Abgaben. Dazu kommt die Differenz "
         "zwischen Lieferantenpreis und EG-Preis, typisch 2 bis 4 Cent."),
        ("Gilt der Abschlag auch beim Stromteilen über Bundesländer hinweg?",
         "Nein. Der Abschlag ist an den Nahbereich gebunden. Eine Bürgerenergiegemeinschaft, die österreichweit "
         "funktioniert, zahlt außerhalb des Nahbereichs das volle Netzentgelt. Der Vorteil liegt dann nur im "
         "vereinbarten Strompreis."),
        ("Ändert das ElWG die Netzentgelt-Abschläge?",
         "Das ElWG ermächtigt die E-Control, die Abschläge per Verordnung neu festzulegen, die neue "
         "Netzentgeltstruktur gilt ab 1. Jänner 2027. Ob sich die 57 und 28 Prozent ändern, ist derzeit offen."),
        ("Was ist der Versorgungsinfrastrukturbeitrag?",
         "Eine Neuerung des ElWG für Anlagen mit mehr als 20 kW eingespeister Leistung, gedeckelt mit "
         "durchschnittlich 0,5 Euro je Megawattstunde (0,05 Cent je kWh). Er gilt auch in Energiegemeinschaften, "
         "fällt wirtschaftlich aber kaum ins Gewicht."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und errichtet Photovoltaik-, "
                    "Speicher- und Wärmepumpensysteme in Kärnten und der Steiermark und begleitet Kunden beim Einstieg "
                    "in Energiegemeinschaften. Inhalte werden regelmäßig anhand der Vorgaben von E-Control, OeMAG und "
                    "energiegemeinschaften.gv.at aktualisiert. Keine Rechts- oder Steuerberatung, maßgeblich ist die "
                    "jeweils gültige Systemnutzungsentgelte-Verordnung."),
    "sources": [
        ("E-Control: Energiegemeinschaften und Netzentgelte", "https://www.e-control.at/energiegemeinschaften"),
        ("CMS: Gemeinsame Energienutzung im ElWG",
         "https://cms.law/de/aut/legal-updates/gemeinsame-energienutzung-welche-moeglichkeiten-schafft-das-elwg"),
        ("Koordinationsstelle: FAQs zum ElWG", "https://energiegemeinschaften.gv.at/faqs-zum-elwg/"),
    ],
    "related": [
        ("/oemag-einspeisetarif/", "OeMAG-Einspeisetarif oder Energiegemeinschaft"),
        ("/energiegemeinschaft-kosten/", "Energiegemeinschaft: Kosten"),
        ("/energiegemeinschaft-kaernten/", "Energiegemeinschaft Kärnten"),
        ("eg", "Energiegemeinschaft: Überblick"),
    ],
    "cta": {
        "h3": "Netzersparnis für Ihren Haushalt",
        "text": "Wir prüfen Ihre Netzebene und rechnen mit den Richtwerten Ihres Netzgebiets durch.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Weniger Netzentgelt, gleicher Lieferant",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Anlage und "
                   "Energiegemeinschaft aus einer Hand liefert."),
}
