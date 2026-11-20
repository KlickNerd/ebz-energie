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
    "description": "Netzkosten in der Energiegemeinschaft: in der EEG minus 57 % lokal, 28 % regional, E-Abgabe entfällt. Was ab 2027 für BEG und P2P gilt, Rechenbeispiel.",
    "eyebrow": "Energiegemeinschaft · Netzkosten",
    "crumb_label": "Energiegemeinschaft und Netzkosten",
    "h1": "Energiegemeinschaft und Netzkosten: bis zu 57 Prozent weniger Netzentgelt, Position für Position",
    "lead": ("Der Netzentgelt-Abschlag ist das stärkste Argument für die Energiegemeinschaft und gleichzeitig das am "
             "häufigsten missverstandene. Hier ist die Rechnung, Position für Position."),
    "chips": [
        "Netznutzung: <b>minus 57 %</b> lokal",
        "Netzverlust: <b>minus 57 %</b> lokal",
        "E-Abgabe (ab 2027 1,5 ct): <b>entfällt</b>",
        "Förderbeitrag 2027: <b>für alle ausgesetzt</b>",
    ],
    "date_published": "2026-08-15",
    "date_modified": "2026-11-20",
    "hero_img": "gen_gewerbe",
    "hero_alt": "Photovoltaikanlage auf einem Gewerbedach, im Hintergrund Trafostation und Wohnsiedlung",

    "tldr": [
        "Auf Strom aus einer Erneuerbare-Energie-Gemeinschaft (EEG) sinkt der Arbeitspreis des Netznutzungs- und "
        "Netzverlustentgelts um 57 Prozent (lokal) oder 28 Prozent (regional), Werte der geltenden SNE-VO. Die "
        "Grundpauschale und der Leistungspreis bleiben unverändert.",
        "Bis Ende 2026 bekommen nur EEG-Mitglieder diesen Abschlag. Ab 1.1.2027 sollen auch BEG, Peer-to-Peer und "
        "Eigenversorgungsanlage im Nahbereich reduzierte Netzentgelte bekommen, die Höhe legt die E-Control neu fest.",
        "Nur in der EEG entfällt zusätzlich die Elektrizitätsabgabe (2026 für Haushalte befristet 0,1 Cent, ab 2027 "
        "wieder 1,5 Cent pro kWh) und derzeit der Erneuerbaren-Förderbeitrag, den die Bundesregierung 2027 ohnehin für "
        "alle aussetzt. Bürgerenergiegemeinschaften bekommen das nicht, für Peer-to-Peer ist es nicht geregelt.",
        "Rechenbeispiel 1.000 kWh aus einer lokalen EEG (Abgaben Stand 2027): rund 95 Euro Ersparnis im Jahr, also "
        "9,5 Cent je zugeordneter Kilowattstunde, davon 6,5 Cent aus Netz und Abgaben. Aus typisch 9 bis 12,5 Cent "
        "Netz- und Abgabenanteil je Kilowattstunde werden so rund 3 bis 5 Cent.",
        "Der Abschlag gilt nur für die zugeordnete Menge. Wie viel das ist, hängt von Ihrem Verbrauchsprofil und der "
        "Gemeinschaft ab: 25 Prozent ohne Tagesverbrauch, 40 bis 60 Prozent mit Wärmepumpe, E-Auto oder Homeoffice.",
    ],
    "kpis": [
        ("57 %", "Abschlag lokal (selber Trafo)"),
        ("28 %", "Abschlag regional (selbes Umspannwerk)"),
        ("1,5 ct", "Elektrizitätsabgabe ab 2027, entfällt in der EEG"),
        ("~9,5 ct", "Ersparnis je zugeordneter kWh im Beispiel (Stand 2027)*"),
    ],

    "sections": [
        ("Woraus Ihre Stromrechnung besteht", "stromrechnung", f"""
<p><b>Eine Energiegemeinschaft ist ein Zusammenschluss von mindestens zwei Teilnehmern, die Solarstrom über das
öffentliche Netz teilen.</b> Für Mitglieder einer Erneuerbare-Energie-Gemeinschaft sinken die Netzentgelte im
Nahbereich um bis zu 57 Prozent (lokal) oder 28 Prozent (regional). Bürgerenergiegemeinschaften dürfen sich über
ganz Österreich erstrecken, außerhalb des Nahbereichs aber ohne Rabatt. Voraussetzung ist ein Smart Meter
mit Viertelstundenwerten (Quellen: E-Control SNE-VO, energiegemeinschaften.gv.at, Stand November 2026).</p>
<p>Um den Vorteil der Energiegemeinschaft zu verstehen, muss man die Stromrechnung in ihre drei Teile zerlegen.
Erstens der Energiepreis, den Ihr Lieferant verlangt, aktuell je nach Tarif 12 bis 20 Cent netto pro Kilowattstunde.
Zweitens die Netzkosten, die der Netzbetreiber nach der Systemnutzungsentgelte-Verordnung der E-Control verrechnet:
Netznutzungsentgelt, Netzverlustentgelt und eine Grundpauschale. Drittens Steuern und Abgaben: Elektrizitätsabgabe,
Erneuerbaren-Förderbeitrag, Erneuerbaren-Förderpauschale und die Umsatzsteuer auf alles. Förderbeitrag und
Förderpauschale setzt die Bundesregierung 2027 laut BMF für alle Stromkunden aus, die Elektrizitätsabgabe steigt
2027 vom befristeten Satz 0,1 Cent (Haushalte 2026) wieder auf 1,5 Cent. Die Energiegemeinschaft
greift bei Teil zwei und drei an, und zwar nur bei den Positionen, die je Kilowattstunde verrechnet werden.</p>
{A.table(
    ["Position je kWh", "Richtwert Haushalt*", "Lokale EEG", "Regionale EEG", "BEG, P2P, EVA im Nahbereich"],
    [
        ["Netznutzungsentgelt (Arbeit)", "7 bis 10 ct", "minus 57 %", "minus 28 %", "2026 voll, ab 1.1.2027 voraussichtlich reduziert"],
        ["Netzverlustentgelt", "0,5 bis 1 ct", "minus 57 %", "minus 28 %", "2026 voll, ab 1.1.2027 voraussichtlich reduziert"],
        ["Elektrizitätsabgabe", "2026: 0,1 ct (befristet), ab 2027: 1,5 ct", "entfällt", "entfällt", "bleibt (keine Befreiung zugesagt)"],
        ["Erneuerbaren-Förderbeitrag", "2026: ca. 1 ct, 2027 laut Bundesregierung ausgesetzt", "entfällt", "entfällt", "2026 voll, 2027 für alle ausgesetzt"],
        ["Grundpauschale, Leistungspreis, Förderpauschale", "fix pro Jahr (Förderpauschale 2027 ausgesetzt)", "unverändert", "unverändert", "unverändert"],
    ],
    hl_cols=(2, 3),
)}
<p><small>*Richtwerte, sie schwanken je nach Netzgebiet. Die exakten Sätze Ihres Netzgebiets stehen auf Ihrer
Netzrechnung und in der jeweils gültigen Systemnutzungsentgelte-Verordnung der E-Control. Die Abschläge von 57 und
28 Prozent stammen aus der geltenden SNE-VO, ihre Höhe ab 2027 legt die E-Control neu fest (laut E-Control-Entwurf
für 2027 49 Prozent lokal, 22 bzw. 58 Prozent regional, Entwurf). Abgaben laut Parlament (Elektrizitätsabgabe) und
BMF (Aussetzung 2027), siehe Quellen.</small></p>
"""),
        ("Lokal oder regional: Der Nahbereich bestimmt den Abschlag", "nahbereich", f"""
<p>Der Abschlag von 57 Prozent gilt für Mitglieder einer EEG im Lokalbereich, also wenn Erzeuger und Verbraucher
an derselben Trafostation auf der Niederspannungsebene hängen, meist in einem Radius von rund 1 km. Der Abschlag
von 28 Prozent gilt für den Regionalbereich, wenn beide am selben Umspannwerk auf der Mittelspannungsebene
angeschlossen sind, rund 30 km. Wer ausschließlich auf den Netzebenen
4 und 5 teilnimmt, was nur für größere Betriebe relevant ist, kann bis zu 64 Prozent erreichen. Die Logik dahinter:
Strom, der im Ortsnetz bleibt, belastet die übergeordneten Netzebenen nicht, deshalb müssen Teilnehmer diese auch
nicht mitbezahlen.</p>
{A.box("Der Abschlag ist an den Nahbereich gebunden. Wer Strom österreichweit teilt, etwa in einer " +
       a('/buergerenergiegemeinschaft/', 'Bürgerenergiegemeinschaft') +
       " mit Verwandten in einem anderen Bundesland, zahlt das volle Netzentgelt. Der "
       "Vorteil liegt dann allein im vereinbarten Strompreis. Über mehrere Netzbetreiber hinweg, etwa Kärnten und "
       "Wien, lässt sich das laut Koordinationsstelle voraussichtlich erst ab April 2027 umsetzen. Welche Modelle "
       "für Familie und Nachbarn passen, zeigt der Artikel " +
       a('/energiegemeinschaft-privat/', 'Energiegemeinschaft privat') + ".", label="Wichtig:")}
<p>Ob Ihr Zählpunkt lokal oder regional mit einer Gemeinschaft verbunden ist, prüft der Netzbetreiber bei der
Anmeldung. Wie Sie die passende Gemeinschaft finden, steht im Artikel
{a('/energiegemeinschaft-finden/', 'Energiegemeinschaft finden')}.</p>
"""),
        ("Rechenbeispiel: 1.000 kWh aus der Gemeinschaft", "rechenbeispiel", f"""
<p>Nehmen wir einen Haushalt in Kärnten, der 1.000 kWh im Jahr aus einer lokalen Erneuerbaren-Energie-Gemeinschaft
zugeordnet bekommt. Als Richtwerte setzen wir 8 Cent Netznutzung, 0,7 Cent Netzverlust und 1,5 Cent Elektrizitätsabgabe
an (Stand 2027; den Erneuerbaren-Förderbeitrag setzt die Bundesregierung 2027 aus), dazu 17 Cent Arbeitspreis beim
Lieferanten und 14 Cent EG-Preis*.</p>
{A.table(
    ["Position", "Normalbezug", "Lokale EEG", "Ersparnis"],
    [
        ["Netznutzung 1.000 kWh", "80 €", "34,40 €", "45,60 €"],
        ["Netzverlust 1.000 kWh", "7 €", "3,01 €", "3,99 €"],
        ["Elektrizitätsabgabe (1,5 ct, Stand 2027)", "15 €", "0 €", "15 €"],
        ["Erneuerbaren-Förderbeitrag (2027 ausgesetzt)", "0 €", "0 €", "0 €"],
        ["Energiepreis (17 ct Lieferant vs. 14 ct EG)", "170 €", "140 €", "30 €"],
        ["Summe netto", "272 €", "177,41 €", "94,59 €"],
    ],
    hl_cols=(3,),
)}
<p>Rund 9,5 Cent Ersparnis je zugeordneter Kilowattstunde, davon etwa 6,5 Cent aus Netz und Abgaben und 3 Cent aus
dem günstigeren Energiepreis. Bei einer regionalen Gemeinschaft sind es rund 7 Cent. Mit den Abgaben 2026 sieht die
Rechnung ähnlich aus: Die Elektrizitätsabgabe beträgt für Haushalte befristet nur 0,1 Cent (1 € statt 15 €), dafür
entfällt in der EEG noch der Förderbeitrag von rund 1 Cent (10 €), zusammen rund 91 € Ersparnis. Der
Abgabenvorteil ist damit deutlich kleiner als die früher oft genannten 2,5 Cent, der größte Posten bleibt das
Netzentgelt. Die Zahl, die am Ende zählt,
ist aber die zugeordnete Menge: 1.000 kWh entsprechen bei einem 4.000-kWh-Haushalt einer Zuordnungsquote von
25 Prozent, was für einen Haushalt ohne Tagesverbrauch realistisch ist. Mit Wärmepumpe, E-Auto oder Homeoffice sind
40 bis 60 Prozent erreichbar. Eine zu niedrige Zuordnungsquote ist der häufigste Grund, warum sich eine
Gemeinschaft weniger lohnt als erwartet, mehr dazu im Artikel
{a('/energiegemeinschaft-nachteile/', 'Energiegemeinschaft: Nachteile')}. Den Effekt für Ihren Haushalt zeigt der
{a('eg_rechner', 'Energiegemeinschaft-Rechner')}.</p>
<p><small>*Beispielkonditionen: EG-Bezugspreis 14 Cent, Lieferantenpreis 17 Cent netto je kWh, Netzentgelt-Richtwerte
und Abschläge 2026 (geltende SNE-VO), Abgaben Stand 2027. Mit dem E-Control-Entwurf für 2027 (49 Prozent lokal) sänke
die Netzersparnis im Beispiel von rund 50 auf rund 43 €. Jede Gemeinschaft legt ihre Preise selbst fest, die Konditionen bei EBZ nennen wir im Erstgespräch.</small></p>
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
Gebühren dafür üblich sind, steht im Artikel {a('/energiegemeinschaft-kosten/', 'Was eine Energiegemeinschaft kostet')},
konkrete Preise mehrerer Anbieter im {a('/energiegemeinschaft-vergleich/', 'Energiegemeinschaft-Vergleich')}.</p>
"""),
        ("Gilt das auch für Erzeuger?", "erzeuger", f"""
<p>Der Netzentgelt-Abschlag betrifft den Bezug, nicht die Einspeisung. Als Erzeuger profitieren Sie davon in den
Stunden, in denen Sie selbst aus der Gemeinschaft beziehen, also abends und im Winter. Auf der Einspeiseseite liegt
Ihr Vorteil im fix vereinbarten EG-Preis: Der OeMAG-Tarif schwankte 2026 zwischen 6,146 Cent (Juli) und 14,874 Cent
(Oktober), ein EG-Preis liegt je nach Monat darüber oder darunter, ist aber planbar. Den Vergleich zieht der Artikel
{a('/oemag-einspeisetarif/', 'OeMAG-Einspeisetarif oder Energiegemeinschaft')}.</p>
<p>Eine Neuerung des ElWG betrifft größere Einspeiser: Für Anlagen mit mehr als 20 kW eingespeister Leistung wird ein
Versorgungsinfrastrukturbeitrag fällig, gedeckelt mit durchschnittlich 0,5 Euro je Megawattstunde, also 0,05 Cent je
Kilowattstunde. Er gilt auch innerhalb von Energiegemeinschaften, fällt aber wirtschaftlich kaum ins Gewicht.</p>
"""),
        ("Netzentgelte heute und ab 2027: Was für welches Modell gilt", "ab-2027", f"""
<p>Seit 1. Oktober 2026 regelt das Elektrizitätswirtschaftsgesetz (ElWG) fünf Bürgerenergie-Modelle. Beim
Netzentgelt gilt eine Übergangsphase: Von Oktober bis Dezember 2026 dürfen Netzbetreiber vergünstigte
Netzentgelte nur Mitgliedern lokaler und regionaler EEGs verrechnen. Mit der novellierten
Systemnutzungsentgelte-Verordnung sollen nach heutigem Stand ab 1. Jänner 2027 auch lokale und regionale BEG,
{a('/peer-to-peer-strom/', 'Peer-to-Peer-Verträge')} und Eigenversorgungsanlagen reduzierte Netzentgelte bekommen.
Die Höhe legt die E-Control per Verordnung fest; laut E-Control-Entwurf für 2027 sind 49 Prozent lokal und 22 bzw.
58 Prozent regional vorgesehen (Entwurf).</p>
{A.table(
    ["Modell", "Oktober bis Dezember 2026", "Ab 1.1.2027 (voraussichtlich)", "Elektrizitätsabgabe, Förderbeitrag"],
    [
        ["EEG lokal / regional", "minus 57 % / minus 28 %, bis 64 % nur NE 4/5", "reduziert, Höhe legt die E-Control fest", "entfallen"],
        ["BEG im Nahbereich", "volles Netzentgelt", "reduziert, Höhe legt die E-Control fest", "bleiben"],
        ["Peer-to-Peer im Nahbereich", "volles Netzentgelt", "reduziert, Höhe legt die E-Control fest", "nicht geregelt"],
        ["Eigenversorgungsanlage im Nahbereich", "volles Netzentgelt", "reduziert, Höhe legt die E-Control fest", "nicht geregelt"],
        ["GEA an derselben Hauptleitung", "kein Netzentgelt auf den intern verteilten Strom",
         "unverändert; Standortbereich reduziert, Umsetzung voraussichtlich ab April 2027", "E-Abgabe entfällt, kein Förderbeitrag"],
        ["BEG oder Peer-to-Peer österreichweit", "volles Netzentgelt", "volles Netzentgelt", "bleiben bzw. nicht geregelt"],
    ],
    hl_cols=(1, 2),
)}
<p><small>Quellen: energiegemeinschaften.gv.at (FAQs zum ElWG, Bürgerenergie-Modelle, Stand November 2026),
E-Control SNE-VO. Netzübergreifende Zuordnungen sind laut Koordinationsstelle voraussichtlich ab April 2027
möglich, bis dahin nur mit Zählpunkten beim selben Netzbetreiber.</small></p>
<p>Neu ist außerdem die Mehrfachteilnahme: Ein Zählpunkt kann an bis zu fünf Modellen gleichzeitig teilnehmen,
der Teilnahmefaktor verteilt die Mengen (in Summe höchstens 100 Prozent). Den reduzierten Netzarbeitspreis gibt
es dabei je Modell nur für die Menge, die im jeweiligen Nahbereich zugeordnet wird. Im Mehrparteienhaus kommt
der Strom über die {a('/gemeinschaftliche-erzeugungsanlage/', 'gemeinschaftliche Erzeugungsanlage')} ganz ohne
öffentliches Netz zu den Wohnungen. Alle fünf Modelle im
Vergleich stehen im {a('eg', 'Leitartikel Energiegemeinschaft in Österreich')}.</p>
{A.box_dark("Die EEG bleibt vorerst das stärkste Modell",
    "Die Befreiung von Elektrizitätsabgabe und Erneuerbaren-Förderbeitrag gilt laut Koordinationsstelle derzeit "
    "nur für Erneuerbare-Energie-Gemeinschaften, und bis Ende 2026 ist die EEG das einzige Modell mit "
    "Netzentgelt-Rabatt. 2027 bleibt davon die Befreiung von der Elektrizitätsabgabe (1,5 Cent), weil die "
    "Bundesregierung den Förderbeitrag für alle aussetzt. Wir aktualisieren diesen Artikel, sobald die neue "
    "Verordnung vorliegt.")}
"""),
        ("Fazit: Netzkosten in der Energiegemeinschaft", "fazit", f"""
<p>Der Netzentgelt-Abschlag ist kein Rabatt auf die ganze Rechnung, sondern eine deutliche Ersparnis auf die
zugeordnete Menge: rund 6 bis 6,5 Cent je Kilowattstunde aus Netz und Abgaben (Richtwerte 2026 und 2027), plus den
Preisvorteil beim EG-Strom.
Wer seinen Verbrauch in die Erzeugungszeiten legt, macht aus einem kleinen Vorteil einen großen. Genau dafür sind
{a('batteriespeicher', 'Speicher')} und Energiemanagement da, für Letzteres gibt es 2026 sogar eine eigene
{a('/ems-foerderung/', 'EMS-Förderung')}. Wie der Einstieg abläuft, steht im Artikel
{a('/energiegemeinschaft-beitreten/', 'Energiegemeinschaft beitreten')}, wie EBZ Sie in Kärnten und der
Steiermark aufnimmt, auf der Seite {a('eg_privat', 'Energiegemeinschaft für Privatkunden')}.</p>
{A.cta("Rechnen Sie Ihre Netzersparnis nach",
       "Der Rechner berücksichtigt Netzebene, Abgaben und Ihre Zuordnungsquote.",
       primary=("kontakt", "Beratung anfragen"), secondary=("eg_rechner", "Zum Rechner"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Energiegemeinschaft: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und Wallboxen in "
                 "Kärnten und der Steiermark, mit zertifizierten Fachkräften. Dazu kommt "
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
         "In einer Erneuerbare-Energie-Gemeinschaft auf den EG-Strom 57 Prozent des Arbeitspreises von "
         "Netznutzungs- und Netzverlustentgelt im Lokalbereich, 28 Prozent im Regionalbereich (Werte der geltenden "
         "SNE-VO). Grundpauschale und Leistungspreis bleiben unverändert."),
        ("Bekommen BEG und Peer-to-Peer schon reduzierte Netzentgelte?",
         "Nein. Von Oktober bis Dezember 2026 haben laut Koordinationsstelle nur Mitglieder lokaler und regionaler "
         "EEGs Anspruch auf den reduzierten Netzarbeitspreis. Für lokale und regionale BEG, Peer-to-Peer und "
         "Eigenversorgungsanlagen ist die Reduktion nach heutigem Stand ab 1. Jänner 2027 vorgesehen, die Höhe "
         "legt die E-Control per Verordnung fest."),
        ("Entfällt die Elektrizitätsabgabe in jeder Energiegemeinschaft?",
         "Nein. Die Befreiung von Elektrizitätsabgabe (2026 für Haushalte befristet 0,1 Cent, ab 2027 wieder 1,5 Cent "
         "je kWh) und Erneuerbaren-Förderbeitrag gilt laut "
         "Koordinationsstelle derzeit nur für Erneuerbare-Energie-Gemeinschaften, nicht für "
         "Bürgerenergiegemeinschaften. Für Peer-to-Peer und Eigenversorgungsanlage ist sie nicht geregelt. Den "
         "Förderbeitrag setzt die Bundesregierung 2027 ohnehin für alle Stromkunden aus. In einer "
         "gemeinschaftlichen Erzeugungsanlage entfällt die Elektrizitätsabgabe, ein Förderbeitrag fällt nicht an, "
         "weil kein öffentliches Netz genutzt wird."),
        ("Sinkt das Netzentgelt auf meine gesamte Stromrechnung?",
         "Nein, nur auf die Menge, die Ihnen aus der Gemeinschaft zugeordnet wird. Alles, was Sie aus dem "
         "öffentlichen Netz von Ihrem Lieferanten beziehen, wird weiterhin zum vollen Tarif verrechnet."),
        ("Wie viel Cent je kWh spare ich insgesamt?",
         "Bei Richtwerten von 8 Cent Netznutzung, 0,7 Cent Netzverlust und 1,5 Cent Elektrizitätsabgabe (Stand 2027, "
         "Förderbeitrag 2027 ausgesetzt) sind es in einer lokalen EEG rund 6,5 Cent aus Netz und Abgaben, 2026 mit "
         "0,1 Cent Elektrizitätsabgabe und rund 1 Cent Förderbeitrag rund 6 Cent. Dazu kommt die Differenz "
         "zwischen Lieferantenpreis und EG-Preis, typisch 2 bis 4 Cent."),
        ("Gilt der Abschlag auch beim Stromteilen über Bundesländer hinweg?",
         "Nein. Der Abschlag ist an den Nahbereich gebunden. Eine Bürgerenergiegemeinschaft, die österreichweit "
         "funktioniert, zahlt außerhalb des Nahbereichs das volle Netzentgelt. Der Vorteil liegt dann nur im "
         "vereinbarten Strompreis. Über mehrere Netzbetreiber hinweg ist das laut Koordinationsstelle "
         "voraussichtlich erst ab April 2027 umsetzbar."),
        ("Ändert das ElWG die Netzentgelt-Abschläge?",
         "Das ElWG ermächtigt die E-Control, die Abschläge per Verordnung neu festzulegen. Die novellierte "
         "Systemnutzungsentgelte-Verordnung soll nach heutigem Stand ab 1. Jänner 2027 gelten und den Rabatt auf "
         "BEG, Peer-to-Peer und Eigenversorgungsanlage im Nahbereich ausweiten. Laut E-Control-Entwurf für 2027 "
         "sind 49 Prozent lokal und 22 bzw. 58 Prozent regional vorgesehen (Entwurf); bis Ende 2026 gelten 57 und "
         "28 Prozent."),
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
        ("Koordinationsstelle: Bürgerenergie-Modelle und Nahebereiche",
         "https://energiegemeinschaften.gv.at/gemeinsame-energienutzung/"),
        ("Koordinationsstelle: Peer-to-Peer-Verträge", "https://energiegemeinschaften.gv.at/peer-to-peer-vertraege/"),
        ("Koordinationsstelle: Eigenversorgungsanlage (EVA)", "https://energiegemeinschaften.gv.at/eigenversorgungsanlage/"),
        ("Parlament: Nationalrat beschließt Senkung der Elektrizitätsabgabe",
         "https://www.parlament.gv.at/aktuelles/news/Nationalrat-beschliesst-Senkung-der-Elektrizitaetsabgabe"),
        ("BMF: Aussetzung von Ökostrompauschale und Förderbeitrag 2027",
         "https://www.bmf.gv.at/presse/pressemeldungen/2026/november-2026/oekostrompauschale.html"),
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
