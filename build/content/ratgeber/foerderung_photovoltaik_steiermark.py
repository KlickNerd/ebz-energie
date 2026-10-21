"""Ratgeber: Photovoltaik-Förderung Steiermark 2026.

Migriert von ebz-photovoltaik.at/foerderung-photovoltaik-steiermark/ (Stand Mai 2026),
inhaltlich bereinigt und auf die Ratgeber-Vorlage umgestellt.
Zahlen: EAG-Investitionszuschüsseverordnung 2026, Steirischer Sanierungsbonus 2026, Ökofonds Steiermark.
Korrektur 10.10.2026 (build/seo/_fakten_2026-10.md): Sanierungsbonus beendet, Ökofonds ohne PV-Ausschreibung,
Gemeindebeträge nicht amtlich belegt, Land nimmt für neue Wärmepumpen keine Anträge an.
Stand ab 23.10.2026: EAG 3. und letzter Call lief 8. bis 22.10.2026, derzeit kein Bundeszuschuss; Ausblick 2027
Systemfoerderung laut BMWET (geplant, nicht beschlossen).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "foerderung-photovoltaik-steiermark",
    "path": "/foerderung-photovoltaik-steiermark/",
    "title": "PV-Förderung Steiermark 2026: Bundescall beendet | EBZ",
    "description": ("PV-Förderung Steiermark: Der letzte EAG-Call endete am 22. Oktober 2026, das Land fördert PV "
                    "derzeit nicht. Was jetzt noch geht und was 2027 geplant ist."),
    "eyebrow": "Förderung · Steiermark",
    "crumb_label": "PV-Förderung Steiermark 2026",
    "h1": "Photovoltaik-Förderung Steiermark 2026: EAG-Call beendet, keine Landesförderung, Systemförderung 2027 geplant",
    "lead": ("In der Steiermark gibt es 2026 keine PV-Pauschale des Landes. Die wichtigste Förderung war der "
             "EAG-Investitionszuschuss des Bundes, dessen dritter und letzter Call vom 8. bis 22. Oktober 2026 lief; "
             "derzeit ist kein Bundeszuschuss beantragbar. Der Steirische Sanierungsbonus ist beendet, der Ökofonds "
             "hat keine PV-Ausschreibung, manche Gemeinden zahlen einen eigenen Zuschuss. Ab 2027 ist laut BMWET "
             "eine Systemförderung geplant, nicht beschlossen."),
    "chips": [
        "EAG-Bund: <b>Call 2026 beendet</b>",
        "2027: <b>Systemförderung</b> geplant",
        "Sanierungsbonus: <b>beendet</b>",
        "Ökofonds: <b>keine PV-Ausschreibung</b>",
    ],
    "date_published": "2026-04-05",
    "date_modified": "2026-10-21",
    "hero_img": "foerderung",
    "hero_alt": "Beratungsgespräch zur Photovoltaik-Förderung in der Steiermark mit Förderunterlagen am Tisch",

    "tldr": [
        "Die wichtigste PV-Förderung in der Steiermark war 2026 der EAG-Investitionszuschuss des Bundes: Im Call "
        "2026 gab es 150 Euro je kWp bis 10 kWp, 140 Euro je kWp bis 20 kWp, Speicher 150 Euro je kWh bis 50 kWh, "
        "plus 10 Prozent Made-in-Europe-Bonus je Komponente. Derzeit ist der Bund nicht beantragbar.",
        "Der Steirische Sanierungsbonus 2026 (maximal 15 Prozent der förderbaren Kosten, Antragsfenster "
        "1. April bis 15. Mai 2026, 9,8 Millionen Euro Budget) war eine befristete Sonderausschreibung und ist "
        "beendet.",
        "Der Ökofonds des Landes hat derzeit keine PV-Ausschreibung, ausgeschrieben sind nur Wasserstoffprojekte "
        "und Innovative Energiespeicher (Stand 10. Oktober 2026). Der PV-Call für Anlagen ab 20 kWp mit "
        "Doppelnutzung (bis zu 30 Prozent) lief bis Ende Mai 2026.",
        "EAG-Fördercalls 2026: 23. April bis 11. Mai, 16. bis 30. Juni, 8. bis 22. Oktober, alle beendet; im "
        "bisherigen System gibt es keinen weiteren Call. Ab 2027 ist laut BMWET eine Systemförderung für Speicher "
        "mit intelligenter Steuerung geplant, Antrag nach Installation, nicht beschlossen, Höhe offen.",
        "Manche Gemeinden zahlen einen eigenen Zuschuss, die EMS-Förderung des Klimafonds läuft bis 15. April 2027. "
        "Wer jetzt plant, baut mit Speicher und Energiemanagement, um die Chance auf die Systemförderung 2027 zu wahren.",
    ],
    "kpis": [
        ("150 €/kWp", "EAG-Bundesförderung bis 10 kWp im Call 2026"),
        ("150 €/kWh", "EAG-Speicherförderung im Call 2026"),
        ("22. Oktober", "Ende des letzten EAG-Calls 2026"),
        ("3.000 €", "EAG im Call 2026 für 10 kWp mit 10 kWh*"),
    ],

    "sections": [
        ("Die PV-Förderung Steiermark 2026 im Überblick: was noch läuft", "ueberblick", f"""
<p>Die steirische Förderlandschaft stand 2026 auf drei Säulen: Bundesförderung über das
Erneuerbaren-Ausbau-Gesetz (EAG), Landesförderungen des Landes Steiermark und Gemeindeförderungen.
Stand ab 23. Oktober 2026 ist für Photovoltaik davon keine Bundes- oder Landesschiene offen: Der dritte und
letzte EAG-Call lief vom 8. bis 22. Oktober 2026, die beiden Landesschienen sind beendet. Bleiben manche
Gemeindezuschüsse und die EMS-Förderung des Klimafonds.</p>
{A.table(
    ["Förderschiene", "Für wen", "Förderhöhe 2026", "Zeitfenster"],
    [
        ["EAG-Investitionszuschuss (Bund)", "Private, Betriebe, Landwirte, Gemeinden", "im Call 2026: 150 €/kWp (bis 10 kWp) + 150 €/kWh Speicher + Made-in-Europe-Bonus", "beendet: 3 Calls 2026, der letzte lief vom 8. bis 22. Oktober 2026; ab 2027 Systemförderung laut BMWET geplant"],
        ["Steirischer Sanierungsbonus (Land)", "Private, rückwirkend für umgesetzte Maßnahmen", "war: max. 15 % der förderbaren Kosten, nach Ökopunkten", "beendet (Antragsfenster war 1. April bis 15. Mai 2026)"],
        ["Ökofonds Steiermark (Land)", "Anlagen ab 20 kWp mit Doppelnutzung", "war: bis 30 %, max. 250.000 € je Antrag", "derzeit keine PV-Ausschreibung (PV-Call lief bis Ende Mai 2026)"],
        ["Gemeindeförderung", "je nach Wohnsitzgemeinde", "manche Gemeinden zahlen einen eigenen Zuschuss", "gemeindeabhängig"],
    ],
    hl_cols=(2,),
)}
<p>Eine direkte PV-Pauschale des Landes wie die 3.000 Euro in Kärnten gibt es in der Steiermark nicht.
Die finanziell stärkste Schiene war deshalb 2026 der EAG-Investitionszuschuss; derzeit ist er nicht
beantragbar, manche Gemeinden zahlen einen eigenen Zuschuss.</p>
<p><small>Stand: Oktober 2026. Maßgeblich sind die jeweils gültigen Richtlinien der EAG-Abwicklungsstelle und des
Landes Steiermark. *Rechenwert im Call 2026 (beendet) für eine private Anlage mit 10 kWp und 10 kWh Speicher:
1.500 Euro plus 1.500 Euro aus dem EAG, ohne Made-in-Europe-Bonus.</small></p>
"""),
        ("EAG-Investitionszuschuss 2026: die wichtigste PV-Förderung", "eag", f"""
<p>Der EAG-Investitionszuschuss war 2026 die zentrale Bundesförderung für Photovoltaik und Stromspeicher in
Österreich. Mit der EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026, kundgemacht am 16. Jänner 2026,
wurden die Konditionen im Wesentlichen auf dem Niveau des Vorjahres fortgeschrieben. Insgesamt standen 2026
rund 60 Millionen Euro Bundesmittel bereit, vergeben über drei Fördercalls. Der letzte Call endete am
22. Oktober 2026, die Sätze sind derzeit nicht beantragbar.</p>
<h3>Fördersätze nach Anlagengröße im Call 2026</h3>
{A.table(
    ["Kategorie", "Engpassleistung", "Fördersatz", "Vergabe"],
    [
        ["A", "bis 10 kWp", "150 €/kWp", "fixer Satz, First-Come-First-Served"],
        ["B", "über 10 bis 20 kWp", "140 €/kWp", "fixer Satz, First-Come-First-Served"],
        ["C", "über 20 bis 100 kWp", "max. 130 €/kWp", "Bieterverfahren"],
        ["D", "über 100 bis 1.000 kWp", "max. 120 €/kWp", "Bieterverfahren"],
        ["Stromspeicher", "bis 50 kWh", "150 €/kWh", "nur mit PV-Neuerrichtung oder -Erweiterung"],
    ],
    hl_cols=(2,),
)}
<p>Die Förderung war generell auf 30 Prozent der förderfähigen Netto-Investitionskosten begrenzt. Für die
meisten privaten Anlagen war diese Obergrenze nicht relevant, dort entschieden die kWp-Sätze.</p>
<h3>Die Fördercall-Termine 2026 (alle beendet)</h3>
<ul>
  <li><b>Erster Call:</b> 23. April 2026 (17:00 Uhr) bis 11. Mai 2026 (23:59 Uhr)</li>
  <li><b>Zweiter Call:</b> 16. bis 30. Juni 2026</li>
  <li><b>Dritter Call:</b> 8. bis 22. Oktober 2026</li>
</ul>
<p>Die Antragstellung war nur in diesen Zeitfenstern möglich, in den Kategorien A und B zählte der
Eingang nach Ticketziehung. Im bisherigen System gibt es keinen weiteren Call, neue Anlagen bekommen derzeit
keinen Bundeszuschuss.</p>
<p><b>Ausblick 2027:</b> Laut Eckpunkten des BMWET ist eine Systemförderung geplant, aber nicht beschlossen:
Antrag nach Installation und Rechnung statt Fördercall und Ticketziehung, gefördert werden sollen Speicher mit
intelligenter Steuerung, auch als Nachrüstung. Projekte mit intelligentem Speicher, die ab 1. November 2026 in
Betrieb gehen, sollen 2027 beantragbar sein. Höhe und Kriterien sind offen. Wer jetzt plant, baut deshalb
sinnvoll mit Speicher und Energiemanagement.</p>
<h3>Made-in-Europe-Bonus: bis zu 20 Prozent extra im Call 2026</h3>
<p>Der Made-in-Europe-Bonus galt seit Juni 2025 und im Call 2026: Für jede förderbare Komponente mit
europäischer Wertschöpfung gab es 10 Prozent Zuschlag auf den Investitionszuschuss, also je 10 Prozent für
PV-Module, Wechselrichter und Speicher. Für die PV-Anlage waren damit bis zu 20 Prozent Zuschlag möglich,
für den Speicher weitere 10 Prozent. Voraussetzung: Die Komponenten standen auf der White List der
EAG-Abwicklungsstelle und wurden nachweislich im Europäischen Wirtschaftsraum oder in der Schweiz
produziert. Für 2027 ist laut BMWET wieder ein Europa-Bonus geplant, Höhe offen; EBZ Energie plant die
Anlage weiterhin mit europäischen Komponenten, wo es sinnvoll ist.</p>
"""),
        ("Steirischer Sanierungsbonus 2026: Sonderausschreibung beendet", "sanierungsbonus", f"""
<p>Das Land Steiermark hatte für 2026 den „Steirischen Sanierungsbonus 2026“ als befristeten
Sonderförderungs-Call aufgelegt. Diese Sonderausschreibung ist beendet, neue Anträge sind nicht möglich
(Stand Oktober 2026). Das Budget betrug 9,8 Millionen Euro. Gefördert wurden rückwirkend bereits umgesetzte
Sanierungsmaßnahmen, ausdrücklich auch die Errichtung einer PV-Anlage beziehungsweise einer PV-Anlage mit
Stromspeicher.</p>
<ul>
  <li><b>Antragsfenster:</b> 1. April bis 15. Mai 2026, ausschließlich online (abgelaufen)</li>
  <li><b>Förderhöhe:</b> maximal 15 Prozent der förderbaren Kosten, die genaue Höhe hing vom erreichten
  Ökopunkte-Wert ab</li>
  <li><b>Kombinierbar:</b> war mit der EAG-Bundesförderung und mit Gemeindeförderungen kombinierbar</li>
  <li><b>Sperrfrist:</b> Wer bereits eine „Kleine Sanierung“ oder „Umfassende energetische Sanierung“ erhalten
  hatte, musste seit der Förderzusage mindestens vier Jahre warten</li>
</ul>
{A.box("Für neue Projekte ist der Sanierungsbonus keine Option mehr: Das Antragsfenster ist abgelaufen, die "
       "Sonderausschreibung beendet. Auch der EAG-Investitionszuschuss ist seit Ende des letzten Calls am "
       "22. Oktober 2026 derzeit nicht beantragbar; ab 2027 ist laut BMWET eine Systemförderung geplant.")}
<p>Parallel wird die steirische Wohnbauförderung reformiert: „Kleine Sanierung“ und „Umfassende
energetische Sanierung“ sollen zu einer einheitlichen Sanierungsförderung („Sanierungspass“)
zusammengelegt werden, voraussichtlich ab Sommer 2026. PV-Anlagen werden dort als ökologische Maßnahme
im Gesamtkonzept berücksichtigt.</p>
"""),
        ("Ökofonds Steiermark: derzeit keine PV-Ausschreibung", "oekofonds", f"""
<p>Der Ökofonds des Landes Steiermark führt derzeit nur die Ausschreibungen „Wasserstoffprojekte“ und
„Innovative Energiespeicher“. Eine PV-Ausschreibung gibt es nicht (technik.steiermark.at, Stand
10. Oktober 2026). Bis Ende Mai 2026 förderte der Ökofonds PV-Projekte ab 20 kWp, die eine Doppelnutzung
erfüllen: bauwerksintegrierte Anlagen, Hybridkollektoren (PVT), PV auf befestigten Betriebsflächen,
Parkplatzüberdachungen, Floating-PV und Agri-PV. Zielgruppe waren vor allem Unternehmen, Landwirte,
Gemeinden und Bauträger, Privatpersonen konnten ebenfalls einreichen.</p>
{A.table(
    ["Ökofonds Steiermark", "Konditionen im PV-Call bis Ende Mai 2026 (beendet)"],
    [
        ["Grundförderung", "bis zu 30 % der förderungsfähigen Investitionskosten, max. 250.000 € je Antrag und Anlage"],
        ["Bonus Made in Europe", "+ 50 €/kWp bei europäischen Komponenten"],
        ["Bonus Energiesystem", "+ 125 €/kWp bei Integration in ein dezentrales Energiesystem, z. B. mit zwei weiteren neuen Komponenten oder Teilnahme an einer Energiegemeinschaft"],
        ["Mindestgröße", "20 kWp installierte Leistung mit Doppelnutzen"],
    ],
    hl_cols=(1,),
)}
<p>Der Energiesystem-Bonus, bei dem die Teilnahme an einer {a('eg', 'Energiegemeinschaft')} als
Integrationskriterium zählte, ist damit derzeit ebenfalls nicht beantragbar. Ob der Ökofonds wieder eine
PV-Ausschreibung öffnet, ist offen.</p>
{A.cta("Gewerbliche PV in der Steiermark förderfähig planen",
       "EBZ Energie plant Anlagen ab 20 kWp mit Parkplatzüberdachung oder Betriebsfläche mit Speicher und "
       "Energiemanagement. Ob der Ökofonds wieder eine PV-Ausschreibung führt und was die geplante "
       "Systemförderung 2027 bringt, prüfen wir vor dem Angebot.",
       secondary=("referenzen", "Referenzen ansehen"))}
"""),
        ("Gemeindeförderungen und Öko-Sonderausgabenpauschale", "gemeinde", f"""
<p>Manche steirische Gemeinden zahlen einen eigenen Zuschuss: pauschale Fixzuschüsse, Speicherboni
oder prozentuale Beteiligungen an den Investitionskosten. Einige setzen Schwerpunkte auf Speicher, andere auf Wallboxen. Da sich diese
Programme jährlich ändern und nicht zentral veröffentlicht werden, lohnt sich ein Anruf bei der
Wohnsitzgemeinde. EBZ Energie prüft die Gemeindeförderung in Kärnten und der Steiermark für jeden Kunden
individuell.</p>
<h3>Steuerlich: die Öko-Sonderausgabenpauschale</h3>
<p>Die Öko-Sonderausgabenpauschale ermöglicht Privathaushalten, bestimmte Sanierungsmaßnahmen pauschal
über mehrere Jahre steuerlich abzusetzen, ohne Einzelnachweise. Sie ist primär für den Tausch fossiler
Heizsysteme und thermische Sanierungen gedacht, kann aber beim gleichzeitigen Einbau von Wärmepumpe und
PV-Anlage zusätzliche Vorteile bringen. Die Voraussetzungen ändern sich regelmäßig, klären Sie das vor
der Steuererklärung mit Steuerberatung oder Finanzamt.</p>
"""),
        ("Antragstellung Schritt für Schritt", "antrag", f"""
<p>Der EAG-Antrag lief 2026 vollständig digital über das Portal der EAG-Abwicklungsstelle. Fehler oder
fehlende Unterlagen kosteten Reihungsplätze oder führten zur Ablehnung. So lief der Antrag im Call 2026; seit
dem Ende des letzten Calls am 22. Oktober 2026 ist er derzeit nicht möglich:</p>
{A.steps([
    ("Vorbereitung vor dem Call",
     "Anlagengröße in kWp, Komponenten (idealerweise von der Made-in-Europe-White-List), Speichergröße, "
     "Errichtungstermin und ein verbindliches Angebot des Fachbetriebs wurden festgelegt, der "
     "Einspeisezählpunkt musste registriert sein."),
    ("Ticket ziehen am ersten Call-Tag",
     "Am 23. April, 16. Juni oder 8. Oktober 2026 öffnete das Ticketsystem. In den Kategorien A und B "
     "sicherte die schnelle Ticketziehung die beste Reihung, danach folgte der vollständige Antrag im "
     "EAG-Portal."),
    ("Errichtung und Inbetriebnahme",
     "Nach der Förderzusage galt eine Frist zur Inbetriebnahme. Montage durch einen befugten Fachbetrieb, "
     "Rechnungen ausschließlich per Überweisung bezahlen."),
    ("Gemeindeförderung",
     "Nach Fertigstellung die Gemeindeförderung einreichen, sofern Ihre Wohnsitzgemeinde einen eigenen Zuschuss "
     "zahlt. Der Steirische Sanierungsbonus ist beendet (Antragsfenster war 1. April bis 15. Mai 2026)."),
    ("Endabrechnung beim Bund",
     "Innerhalb von sechs Monaten nach Ende der Inbetriebnahmefrist Endabrechnung mit Rechnungen, "
     "Zahlungsbelegen und Fotos der Anlage einreichen. Erst dann wird der EAG-Zuschuss ausbezahlt. Das gilt "
     "weiter für Projekte mit Zusage aus den Calls 2026."),
])}
<h3>Voraussetzungen für die EAG-Förderung im Call 2026</h3>
<ul>
  <li><b>Eigentumsnachweis:</b> Eigentümer der Liegenschaft oder schriftliche Einwilligung des Eigentümers.</li>
  <li><b>Stand der Technik:</b> Elektroinstallation und Erdungsanlage müssen dem Stand der Technik entsprechen.</li>
  <li><b>Netzanschluss:</b> Die Anlage muss an das öffentliche Stromnetz angeschlossen sein.</li>
  <li><b>Kein vorzeitiger Baubeginn:</b> Zum Zeitpunkt der EAG-Antragstellung durfte noch nicht mit der
  Errichtung begonnen worden sein.</li>
  <li><b>Speicher nur in Kombination:</b> Die EAG förderte Speicher 2026 ausschließlich mit einer Neuanlage
  oder Erweiterung, eine reine Speichernachrüstung nicht (für 2027 laut BMWET geplant, nicht beschlossen).</li>
  <li><b>Keine Barzahlung:</b> Alle Rechnungen per Überweisung.</li>
</ul>
{A.box_dark("Reihenfolge: 2026 und ab 2027 verschieden",
    "Im Call 2026 verlor den Bundeszuschuss, wer die Anlage vor dem EAG-Antrag bestellte und errichtete. Für "
    "die geplante Systemförderung 2027 soll der Antrag laut BMWET erst nach Installation und Rechnung kommen "
    "(nicht beschlossen). Gemeindeanträge und Rechnungsdaten gehören trotzdem in einen gemeinsamen Zeitplan.")}
"""),
        ("Photovoltaik und Wärmepumpe: alle Förderpotenziale ausschöpfen", "waermepumpe", f"""
<p>Wer die Energiekosten dauerhaft senken will, kombiniert die PV-Anlage mit einer
{a('waermepumpe', 'Wärmepumpe')}. Die PV-Anlage liefert tagsüber Sonnenstrom, die Wärmepumpe deckt
Heizung und Warmwasser und nutzt im Idealfall direkt den eigenen Strom. Nach Erfahrungswerten von EBZ
Energie sind in dieser Kombination bis zu 85 Prozent Ersparnis bei den Energiekosten möglich.</p>
<p>Förderseitig ist die Lage für die Wärmepumpe derzeit eng: Die Sanierungsoffensive des Bundes ist seit
Herbst 2026 ausgeschöpft, und das Land Steiermark nimmt für neue Wärmepumpen keine Förderanträge an
(Stand 10. Oktober 2026). Die steirische Richtlinie für den Tausch von Heizungssystemen (seit 1. Februar
2026) fördert nur den Ersatz mindestens 15 Jahre alter Biomassekessel oder Wärmepumpen mit höchstens
30 Prozent, höchstens 1.500 Euro, und nur ohne Fernwärme-Anschlussmöglichkeit.
Ein {a('ems', 'Energiemanagementsystem')}, das PV, Speicher und Wärmepumpe steuert, fördert der Klima-
und Energiefonds seit Juni 2026 zusätzlich (siehe {a('/ems-foerderung/', 'EMS-Förderung 2026')}).</p>
"""),
        ("Fazit: Der EAG-Zuschuss zählt, die Reihenfolge entscheidet", "fazit", f"""
<p>Die Photovoltaik-Förderung in der Steiermark 2026 kam ohne Landespauschale aus. Die wichtigste Schiene
war der EAG-Investitionszuschuss: Im Call 2026 gab es für eine private Anlage mit 10 kWp und 10 kWh Speicher
3.000 Euro*, mit Made-in-Europe-Bonus entsprechend mehr. Der letzte Call endete am 22. Oktober 2026, derzeit
ist der Bund nicht beantragbar. Der Steirische Sanierungsbonus ist beendet, der Ökofonds hat derzeit
keine PV-Ausschreibung, manche Gemeinden zahlen einen eigenen Zuschuss. Einen Vergleich mit den anderen Bundesländern finden Sie im Ratgeber
{a('/photovoltaik-landesfoerderungen/', 'PV-Landesförderungen in Österreich')}.</p>
<p>Wer eine Zusage aus den Calls 2026 hat, hält die Inbetriebnahmefrist ein und reicht die Endabrechnung
fristgerecht ein. Gemeindeförderungen werden nach Fertigstellung beantragt.</p>
<p><b>Stand ab 23. Oktober 2026:</b> Der dritte Call lief vom 8. bis 22. Oktober 2026 und war der letzte im
bisherigen System. Ab 2027 ist laut Eckpunkten des BMWET eine Systemförderung geplant, aber nicht beschlossen:
Antrag nach Installation und Rechnung statt Fördercall, gefördert werden sollen Speicher mit intelligenter
Steuerung, auch als Nachrüstung; Projekte mit intelligentem Speicher, die ab 1. November 2026 in Betrieb gehen,
sollen 2027 beantragbar sein. Höhe und Technikkriterien sind noch offen. Wer jetzt plant, baut deshalb mit
Speicher und Energiemanagement.</p>
{A.cta("Jetzt in der Steiermark richtig planen",
       "Wir planen Ihre Anlage mit Speicher und Energiemanagement für die geplante Systemförderung 2027 und "
       "übernehmen Gemeindeantrag und Endabrechnung.",
       primary=("kontakt", "Kostenlose Beratung anfragen"), secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für PV-Förderung in der Steiermark: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie GmbH aus Villach plant und montiert Photovoltaikanlagen, Speicher und Wärmepumpen in "
                 "Kärnten und der Steiermark mit zertifizierten Fachkräften. Wir "
                 "kennen den Stand der Bundesförderung, der steirischen Landesprogramme und die "
                 "Gemeindeförderungen im Detail und übernehmen die komplette Förderabwicklung bis zur "
                 "Endabrechnung. Die Anlage gehört dabei ab dem ersten Tag Ihnen, auf "
                 "Wunsch mit Finanzierung ab 147 Euro im Monat inklusive Speicher."),
        "grid": [
            ("Förderabwicklung komplett", "Gemeindeförderung, EAG-Endabrechnung aus 2026 und Blick auf 2027."),
            ("Zukunftsfähig geplant", "Speicher mit Energiemanagement und europäische Komponenten für die Systemförderung 2027."),
            ("300+ Projekte", "Referenzen in Kärnten und der Steiermark, typische Amortisation 4 bis 6 Jahre."),
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und Energiemanagement vom selben Team."),
        ],
    },

    "faq": [
        ("Wie hoch ist die Photovoltaik-Förderung in der Steiermark 2026 maximal?",
         "Im Call 2026 gab es für eine private Anlage bis 10 kWp 150 Euro je kWp aus der EAG-Bundesförderung plus "
         "150 Euro je kWh Speicher, für 10 kWp mit 10 kWh 3.000 Euro ohne Made-in-Europe-Bonus. Der letzte Call "
         "endete am 22. Oktober 2026, derzeit ist kein Bundeszuschuss beantragbar. Der Steirische Sanierungsbonus "
         "ist beendet, manche Gemeinden zahlen einen eigenen Zuschuss."),
        ("Wann waren die EAG-Fördercalls 2026?",
         "Der erste Call lief vom 23. April (17:00 Uhr) bis 11. Mai 2026, der zweite vom 16. bis 30. Juni 2026, "
         "der dritte und letzte vom 8. bis 22. Oktober 2026. Im bisherigen System gibt es keinen weiteren Call, ab "
         "2027 ist laut BMWET eine Systemförderung geplant (nicht beschlossen). Das Antragsfenster des Steirischen "
         "Sanierungsbonus (1. April bis 15. Mai 2026) ist ebenfalls abgelaufen."),
        ("Gibt es in der Steiermark eine PV-Pauschale des Landes?",
         "Nein. Anders als Kärnten mit 3.000 Euro zahlt das Land Steiermark 2026 keine direkte PV-Pauschale. Der "
         "Steirische Sanierungsbonus (maximal 15 Prozent der förderbaren Kosten) war eine befristete "
         "Sonderausschreibung und ist beendet, der Ökofonds hat derzeit keine PV-Ausschreibung."),
        ("Kann ich Bundes-, Landes- und Gemeindeförderung kombinieren?",
         "Im Call 2026 waren EAG-Investitionszuschuss und Gemeindeförderung in der Steiermark grundsätzlich "
         "kombinierbar, sofern die beihilferechtlichen Höchstgrenzen eingehalten wurden. Derzeit ist weder der Bund "
         "noch eine Landesförderung für Photovoltaik offen: Der letzte EAG-Call endete am 22. Oktober 2026, der "
         "Sanierungsbonus ist beendet, der Ökofonds hat keine PV-Ausschreibung."),
        ("Werden Stromspeicher in der Steiermark gefördert?",
         "Derzeit nicht: Im Call 2026 gab es über die EAG 150 Euro je kWh bis maximal 50 kWh, nur mit "
         "Neuerrichtung oder Erweiterung einer PV-Anlage; der letzte Call endete am 22. Oktober 2026. Ab 2027 ist "
         "laut BMWET eine Systemförderung für Speicher mit intelligenter Steuerung geplant, auch als Nachrüstung "
         "(nicht beschlossen, Höhe offen)."),
        ("Was ist der Ökofonds Steiermark?",
         "Der Ökofonds ist ein Förderinstrument des Landes Steiermark. Derzeit führt er nur die Ausschreibungen "
         "Wasserstoffprojekte und Innovative Energiespeicher, eine PV-Ausschreibung gibt es nicht (Stand "
         "10. Oktober 2026). Bis Ende Mai 2026 förderte er PV-Anlagen ab 20 kWp mit Doppelnutzung mit bis zu "
         "30 Prozent der Investitionskosten, maximal 250.000 Euro je Antrag."),
        ("Musste der EAG-Antrag vor Baubeginn gestellt werden?",
         "Im Call 2026 ja: Zum Zeitpunkt der Antragstellung durfte mit der Errichtung noch nicht begonnen worden "
         "sein, der Antrag musste vor Inbetriebnahme eingereicht sein. Für die geplante Systemförderung 2027 soll "
         "der Antrag laut BMWET nach Installation und Rechnung kommen (nicht beschlossen)."),
        ("Wer hilft mir bei der Förderabwicklung in der Steiermark?",
         "EBZ Energie mit Sitz in Villach betreut Kunden in ganz Kärnten und der Steiermark und übernimmt die "
         "komplette Förderabwicklung: Auswahl der Förderungen, Gemeindeförderung, Endabrechnung und die "
         "Vorbereitung auf die geplante Systemförderung 2027."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und montiert PV-Anlagen, "
                    "Speicher und Wärmepumpen in Kärnten und der Steiermark und wickelt die Förderungen von Bund, Land "
                    "und Gemeinde für seine Kunden ab. Die Angaben werden anhand der offiziellen Richtlinien der "
                    "EAG-Abwicklungsstelle und des Landes Steiermark aktualisiert. Keine Rechts- oder Steuerberatung, "
                    "maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("EAG-Abwicklungsstelle (OeMAG): Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/"),
        ("Förderportal des Landes Steiermark", "https://www.steiermark.at/"),
        ("Land Steiermark: Förderung für Heizungen (Wohnbau, Stand 10. Oktober 2026)",
         "https://www.wohnbau.steiermark.at/cms/ziel/164947118/DE/"),
    ],
    "related": [
        ("/photovoltaik-foerderung-kaernten/", "Photovoltaik-Förderung Kärnten 2026"),
        ("/photovoltaik-landesfoerderungen/", "PV-Landesförderungen: alle 9 Bundesländer"),
        ("/foerderung-fuer-pv-speicher/", "Förderung für PV-Speicher"),
        ("batteriespeicher", "Batteriespeicher: Planung und Auswahl"),
    ],
    "cta": {
        "h3": "Förderung in der Steiermark sichern",
        "text": "Wir planen Ihre Anlage mit Speicher für die Systemförderung 2027 und übernehmen Gemeindeantrag und Endabrechnung.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre PV-Anlage in der Steiermark, förderoptimiert geplant",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
