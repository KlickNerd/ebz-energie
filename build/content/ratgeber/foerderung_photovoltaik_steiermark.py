"""Ratgeber: Photovoltaik-Förderung Steiermark 2026.

Migriert von ebz-photovoltaik.at/foerderung-photovoltaik-steiermark/ (Stand Mai 2026),
inhaltlich bereinigt und auf die Ratgeber-Vorlage umgestellt.
Zahlen: EAG-Investitionszuschüsseverordnung 2026, Steirischer Sanierungsbonus 2026, Ökofonds Steiermark.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "foerderung-photovoltaik-steiermark",
    "path": "/foerderung-photovoltaik-steiermark/",
    "title": "PV-Förderung Steiermark 2026: EAG + Sanierungsbonus | EBZ",
    "description": ("PV-Förderung Steiermark 2026: 150 €/kWp EAG-Bund, 150 €/kWh Speicher, Sanierungsbonus bis "
                    "15 %, Ökofonds bis 30 %. Fristen, Voraussetzungen und Antragsablauf."),
    "eyebrow": "Förderung · Steiermark",
    "crumb_label": "PV-Förderung Steiermark 2026",
    "h1": "Photovoltaik-Förderung Steiermark 2026: EAG-Zuschuss, Sanierungsbonus und Ökofonds richtig kombinieren",
    "lead": ("In der Steiermark gibt es 2026 keine PV-Pauschale des Landes, dafür drei kombinierbare Töpfe: "
             "den EAG-Investitionszuschuss des Bundes, den Steirischen Sanierungsbonus und die Gemeindeförderung. "
             "Für eine private Anlage mit Speicher sind so 4.000 bis 6.000 Euro realistisch."),
    "chips": [
        "EAG-Bund: <b>150 €/kWp</b> bis 10 kWp",
        "Speicher: <b>150 €/kWh</b> bis 50 kWh",
        "Sanierungsbonus: <b>bis 15 %</b> der Kosten",
        "Ökofonds ab 20 kWp: <b>bis 30 %</b>",
    ],
    "date_published": "2026-04-05",
    "date_modified": "2026-09-24",
    "hero_img": "foerderung",
    "hero_alt": "Beratungsgespräch zur Photovoltaik-Förderung in der Steiermark mit Förderunterlagen am Tisch",

    "tldr": [
        "Die wichtigste PV-Förderung in der Steiermark ist der EAG-Investitionszuschuss des Bundes: 150 Euro je kWp "
        "bis 10 kWp, 140 Euro je kWp bis 20 kWp, Speicher 150 Euro je kWh bis 50 kWh, plus 10 Prozent "
        "Made-in-Europe-Bonus je Komponente.",
        "Das Land Steiermark fördert 2026 über den Steirischen Sanierungsbonus: maximal 15 Prozent der "
        "förderbaren Kosten, Antragsfenster 1. April bis 15. Mai 2026, rückwirkend für umgesetzte Maßnahmen, "
        "9,8 Millionen Euro Budget, kombinierbar mit der EAG-Förderung.",
        "Für Anlagen ab 20 kWp mit Doppelnutzung (Parkplatzüberdachung, Agri-PV, Fassade) gibt es den Ökofonds "
        "mit bis zu 30 Prozent der Kosten, maximal 250.000 Euro je Antrag.",
        "EAG-Fördercalls 2026: 23. April bis 11. Mai, 16. bis 30. Juni, ab 8. Oktober. Der Antrag muss vor "
        "Baubeginn und Inbetriebnahme gestellt werden, in den Kategorien A und B gilt First-Come-First-Served.",
        "Viele steirische Gemeinden zahlen zusätzlich 200 bis 1.000 Euro. Bund, Land und Gemeinde sind in der "
        "Steiermark grundsätzlich kombinierbar.",
    ],
    "kpis": [
        ("150 €/kWp", "EAG-Bundesförderung bis 10 kWp"),
        ("15 %", "Steirischer Sanierungsbonus maximal"),
        ("9,8 Mio. €", "Budget Sanierungsbonus 2026"),
        ("4.000 bis 6.000 €", "realistische Gesamtförderung Privatanlage*"),
    ],

    "sections": [
        ("Die PV-Förderung Steiermark 2026 im Überblick: drei Säulen", "ueberblick", f"""
<p>Die steirische Förderlandschaft funktioniert 2026 nach einem Drei-Säulen-Prinzip: Bundesförderung über
das Erneuerbaren-Ausbau-Gesetz (EAG), Landesförderungen des Landes Steiermark und Gemeindeförderungen.
Diese drei Ebenen sind in vielen Fällen kombinierbar und reduzieren die Investitionskosten deutlich.</p>
{A.table(
    ["Förderschiene", "Für wen", "Förderhöhe 2026", "Zeitfenster"],
    [
        ["EAG-Investitionszuschuss (Bund)", "Private, Betriebe, Landwirte, Gemeinden", "150 €/kWp (bis 10 kWp) + 150 €/kWh Speicher + Made-in-Europe-Bonus", "3 Calls: ab 23. April, 16. Juni, 8. Oktober"],
        ["Steirischer Sanierungsbonus (Land)", "Private, rückwirkend für umgesetzte Maßnahmen", "max. 15 % der förderbaren Kosten, nach Ökopunkten", "1. April bis 15. Mai 2026"],
        ["Ökofonds Steiermark (Land)", "Anlagen ab 20 kWp mit Doppelnutzung", "bis 30 %, max. 250.000 € je Antrag, Boni bis 175 €/kWp", "Call bis Ende Mai 2026"],
        ["Gemeindeförderung", "je nach Wohnsitzgemeinde", "meist 200 bis 1.000 € oder Speicherbonus", "laufend, gemeindeabhängig"],
    ],
    hl_cols=(2,),
)}
<p>Eine direkte PV-Pauschale des Landes wie die 3.000 Euro in Kärnten gibt es in der Steiermark nicht.
Die finanziell stärkste Schiene ist deshalb der EAG-Investitionszuschuss, der Sanierungsbonus und die
Gemeindeförderung kommen als Ergänzung dazu.</p>
<p><small>Stand: Mai 2026. Maßgeblich sind die jeweils gültigen Richtlinien der EAG-Abwicklungsstelle und des
Landes Steiermark. *Richtwert für eine private Anlage bis 10 kWp mit Speicher inklusive Sanierungsbonus und
Gemeindeförderung.</small></p>
"""),
        ("EAG-Investitionszuschuss 2026: die wichtigste PV-Förderung", "eag", f"""
<p>Der EAG-Investitionszuschuss ist die zentrale Bundesförderung für Photovoltaik und Stromspeicher in
Österreich. Mit der EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026, kundgemacht am 16. Jänner 2026,
wurden die Konditionen im Wesentlichen auf dem Niveau des Vorjahres fortgeschrieben. Insgesamt stehen 2026
rund 60 Millionen Euro Bundesmittel bereit, vergeben über drei Fördercalls.</p>
<h3>Fördersätze nach Anlagengröße</h3>
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
<p>Die Förderung ist generell auf 30 Prozent der förderfähigen Netto-Investitionskosten begrenzt. Für die
meisten privaten Anlagen ist diese Obergrenze nicht relevant, hier entscheiden die kWp-Sätze.</p>
<h3>Die Fördercall-Termine 2026</h3>
<ul>
  <li><b>Erster Call:</b> 23. April 2026 (17:00 Uhr) bis 11. Mai 2026 (23:59 Uhr)</li>
  <li><b>Zweiter Call:</b> 16. bis 30. Juni 2026</li>
  <li><b>Dritter Call:</b> ab 8. Oktober 2026</li>
</ul>
<p>Die Antragstellung ist nur in diesen Zeitfenstern möglich. In den Kategorien A und B zählt der
Eingang: Wer am ersten Tag ein Ticket zieht, sichert sich die beste Reihung. Wer den Call verpasst,
wartet auf den nächsten und riskiert, dass die Mittel bereits ausgeschöpft sind.</p>
<h3>Made-in-Europe-Bonus: bis zu 20 Prozent extra</h3>
<p>Der Made-in-Europe-Bonus gilt seit Juni 2025 und auch 2026: Für jede förderbare Komponente mit
europäischer Wertschöpfung gibt es 10 Prozent Zuschlag auf den Investitionszuschuss, also je 10 Prozent für
PV-Module, Wechselrichter und Speicher. Für die PV-Anlage sind damit bis zu 20 Prozent Zuschlag möglich,
für den Speicher weitere 10 Prozent. Voraussetzung: Die Komponenten stehen auf der White List der
EAG-Abwicklungsstelle und wurden nachweislich im Europäischen Wirtschaftsraum oder in der Schweiz
produziert. EBZ Energie plant die Anlage von Anfang an mit gelisteten Komponenten.</p>
"""),
        ("Steirischer Sanierungsbonus 2026: die Landesförderung für PV", "sanierungsbonus", f"""
<p>Das Land Steiermark hat für 2026 den „Steirischen Sanierungsbonus 2026“ als befristeten
Sonderförderungs-Call aufgelegt. Das Budget beträgt 9,8 Millionen Euro. Gefördert werden rückwirkend
bereits umgesetzte Sanierungsmaßnahmen, ausdrücklich auch die Errichtung einer PV-Anlage beziehungsweise
einer PV-Anlage mit Stromspeicher.</p>
<ul>
  <li><b>Antragsfenster:</b> 1. April bis 15. Mai 2026, ausschließlich online</li>
  <li><b>Förderhöhe:</b> maximal 15 Prozent der förderbaren Kosten, die genaue Höhe hängt vom erreichten
  Ökopunkte-Wert ab</li>
  <li><b>Kombinierbar:</b> ja, mit der EAG-Bundesförderung und mit Gemeindeförderungen</li>
  <li><b>Sperrfrist:</b> Wer bereits eine „Kleine Sanierung“ oder „Umfassende energetische Sanierung“ erhalten
  hat, muss seit der Förderzusage mindestens vier Jahre warten</li>
</ul>
{A.box("Der Sanierungsbonus wird rückwirkend für fertige Maßnahmen beantragt, der EAG-Zuschuss dagegen vor "
       "Inbetriebnahme. Wer beide nutzen will, stellt zuerst den EAG-Antrag, errichtet die Anlage und reicht "
       "dann im Antragsfenster des Landes ein.")}
<p>Parallel wird die steirische Wohnbauförderung reformiert: „Kleine Sanierung“ und „Umfassende
energetische Sanierung“ sollen zu einer einheitlichen Sanierungsförderung („Sanierungspass“)
zusammengelegt werden, voraussichtlich ab Sommer 2026. PV-Anlagen werden dort als ökologische Maßnahme
im Gesamtkonzept berücksichtigt.</p>
"""),
        ("Ökofonds Steiermark: bis zu 30 Prozent für Anlagen mit Doppelnutzung", "oekofonds", f"""
<p>Der Ökofonds des Landes Steiermark fördert PV-Projekte ab 20 kWp, die eine Doppelnutzung erfüllen:
bauwerksintegrierte Anlagen, Hybridkollektoren (PVT), PV auf befestigten Betriebsflächen,
Parkplatzüberdachungen, Floating-PV und Agri-PV. Zielgruppe sind vor allem Unternehmen, Landwirte,
Gemeinden und Bauträger, Privatpersonen können ebenfalls einreichen. Der aktuelle Call läuft bis Ende
Mai 2026.</p>
{A.table(
    ["Ökofonds Steiermark", "Konditionen 2026"],
    [
        ["Grundförderung", "bis zu 30 % der förderungsfähigen Investitionskosten, max. 250.000 € je Antrag und Anlage"],
        ["Bonus Made in Europe", "+ 50 €/kWp bei europäischen Komponenten"],
        ["Bonus Energiesystem", "+ 125 €/kWp bei Integration in ein dezentrales Energiesystem, z. B. mit zwei weiteren neuen Komponenten oder Teilnahme an einer Energiegemeinschaft"],
        ["Mindestgröße", "20 kWp installierte Leistung mit Doppelnutzen"],
    ],
    hl_cols=(1,),
)}
<p>Für Betriebe, die eine {a('eg', 'Energiegemeinschaft')} gründen oder ihr beitreten, ist der
Energiesystem-Bonus besonders interessant, weil die Teilnahme als Integrationskriterium zählt.</p>
{A.cta("Gewerbliche PV in der Steiermark: Ökofonds und EAG kombinieren",
       "EBZ Energie plant Anlagen ab 20 kWp mit Parkplatzüberdachung oder Betriebsfläche förderfähig und "
       "reicht Ökofonds und EAG in der richtigen Reihenfolge ein.",
       secondary=("referenzen", "Referenzen ansehen"))}
"""),
        ("Gemeindeförderungen und Öko-Sonderausgabenpauschale", "gemeinde", f"""
<p>Viele steirische Gemeinden bieten eigene PV-Förderprogramme an: pauschale Fixzuschüsse, Speicherboni
oder prozentuale Beteiligungen an den Investitionskosten, typischerweise im Bereich von 200 bis
1.000 Euro. Manche Gemeinden setzen Schwerpunkte auf Speicher, andere auf Wallboxen. Da sich diese
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
<p>Der EAG-Antrag läuft vollständig digital über das Portal der EAG-Abwicklungsstelle. Fehler oder
fehlende Unterlagen kosten Reihungsplätze oder führen zur Ablehnung. So gehen Sie vor:</p>
{A.steps([
    ("Vorbereitung vor dem Call",
     "Anlagengröße in kWp, Komponenten (idealerweise von der Made-in-Europe-White-List), Speichergröße, "
     "Errichtungstermin und ein verbindliches Angebot des Fachbetriebs festlegen. Der Einspeisezählpunkt "
     "muss registriert sein."),
    ("Ticket ziehen am ersten Call-Tag",
     "Am 23. April, 16. Juni oder 8. Oktober 2026 öffnet das Ticketsystem. Wer schnell ist, sichert sich in "
     "den Kategorien A und B die beste Reihung. Danach den vollständigen Antrag mit allen Nachweisen im "
     "EAG-Portal einreichen."),
    ("Errichtung und Inbetriebnahme",
     "Nach der Förderzusage gilt eine Frist zur Inbetriebnahme. Montage durch einen befugten Fachbetrieb, "
     "Rechnungen ausschließlich per Überweisung bezahlen."),
    ("Sanierungsbonus und Gemeinde",
     "Nach Fertigstellung den Steirischen Sanierungsbonus im Antragsfenster (1. April bis 15. Mai 2026) "
     "online beantragen und die Gemeindeförderung einreichen."),
    ("Endabrechnung beim Bund",
     "Innerhalb von sechs Monaten nach Ende der Inbetriebnahmefrist Endabrechnung mit Rechnungen, "
     "Zahlungsbelegen und Fotos der Anlage einreichen. Erst dann wird der EAG-Zuschuss ausbezahlt."),
])}
<h3>Voraussetzungen für die Förderung</h3>
<ul>
  <li><b>Eigentumsnachweis:</b> Eigentümer der Liegenschaft oder schriftliche Einwilligung des Eigentümers.</li>
  <li><b>Stand der Technik:</b> Elektroinstallation und Erdungsanlage müssen dem Stand der Technik entsprechen.</li>
  <li><b>Netzanschluss:</b> Die Anlage muss an das öffentliche Stromnetz angeschlossen sein.</li>
  <li><b>Kein vorzeitiger Baubeginn:</b> Zum Zeitpunkt der EAG-Antragstellung darf noch nicht mit der
  Errichtung begonnen worden sein.</li>
  <li><b>Speicher nur in Kombination:</b> Die EAG fördert Speicher ausschließlich mit einer Neuanlage
  oder Erweiterung, eine reine Speichernachrüstung nicht.</li>
  <li><b>Keine Barzahlung:</b> Alle Rechnungen per Überweisung.</li>
</ul>
{A.box_dark("Der häufigste Fehler",
    "Wer die Anlage bestellt und errichtet, bevor der EAG-Antrag im Call eingereicht ist, verliert den "
    "Bundeszuschuss. Der Sanierungsbonus des Landes funktioniert genau umgekehrt und wird erst nach "
    "Fertigstellung beantragt. Beide Termine gehören in einen gemeinsamen Zeitplan.")}
"""),
        ("Photovoltaik und Wärmepumpe: alle Förderpotenziale ausschöpfen", "waermepumpe", f"""
<p>Wer die Energiekosten dauerhaft senken will, kombiniert die PV-Anlage mit einer
{a('waermepumpe', 'Wärmepumpe')}. Die PV-Anlage liefert tagsüber Sonnenstrom, die Wärmepumpe deckt
Heizung und Warmwasser und nutzt im Idealfall direkt den eigenen Strom. Nach Erfahrungswerten von EBZ
Energie sind in dieser Kombination bis zu 85 Prozent Ersparnis bei den Energiekosten möglich.</p>
<p>Förderseitig gibt es für die Wärmepumpe eigene Schienen: die Sanierungsoffensive des Bundes und die
steirische Landesförderung für den Tausch von Heizungssystemen, die seit 1. Februar 2026 verfügbar ist.
Ein {a('ems', 'Energiemanagementsystem')}, das PV, Speicher und Wärmepumpe steuert, fördert der Klima-
und Energiefonds seit Juni 2026 zusätzlich (siehe {a('/ems-foerderung/', 'EMS-Förderung 2026')}).</p>
"""),
        ("Fazit: Drei Töpfe, eine Reihenfolge", "fazit", f"""
<p>Die Photovoltaik-Förderung in der Steiermark 2026 kommt ohne Landespauschale aus, bringt aber mit
EAG-Investitionszuschuss, Steirischem Sanierungsbonus, Made-in-Europe-Bonus und Gemeindeförderung für
eine private Anlage mit Speicher 4.000 bis 6.000 Euro zusammen. Für Betriebe mit Doppelnutzung kommt der
Ökofonds mit bis zu 30 Prozent dazu. Einen Vergleich mit den anderen Bundesländern finden Sie im Ratgeber
{a('/photovoltaik-landesfoerderungen/', 'PV-Landesförderungen in Österreich')}.</p>
<p>Entscheidend ist die Reihenfolge: EAG-Antrag im Call vor Baubeginn, Sanierungsbonus und Gemeinde nach
Fertigstellung, Endabrechnung innerhalb der Frist. Wer das sauber plant, verschenkt kein Geld.</p>
{A.cta("Jetzt Förderung in der Steiermark sichern",
       "Wir planen Ihre Anlage förderfähig, ziehen das EAG-Ticket und übernehmen Sanierungsbonus, "
       "Gemeindeantrag und Endabrechnung.",
       primary=("kontakt", "Kostenlose Beratung anfragen"), secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für PV-Förderung in der Steiermark: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie GmbH aus Villach plant und montiert Photovoltaikanlagen, Speicher und Wärmepumpen in "
                 "Kärnten und der Steiermark mit einem festangestellten Team aus zertifizierten Fachkräften. Wir "
                 "kennen die EAG-Termine, den Steirischen Sanierungsbonus, den Ökofonds und die "
                 "Gemeindeförderungen im Detail und übernehmen die komplette Förderabwicklung von der "
                 "Ticketziehung bis zur Endabrechnung. Die Anlage gehört dabei ab dem ersten Tag Ihnen, auf "
                 "Wunsch mit Finanzierung ab 147 Euro im Monat inklusive Speicher."),
        "grid": [
            ("Förderabwicklung komplett", "EAG-Ticket, Sanierungsbonus, Gemeindeförderung und Endabrechnung."),
            ("Made-in-Europe geplant", "Komponenten von der White List für bis zu 20 % Bonus auf den Zuschuss."),
            ("300+ Projekte", "Referenzen in Kärnten und der Steiermark, typische Amortisation 4 bis 6 Jahre."),
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und Energiemanagement vom selben Team."),
        ],
    },

    "faq": [
        ("Wie hoch ist die Photovoltaik-Förderung in der Steiermark 2026 maximal?",
         "Für eine private Anlage bis 10 kWp gibt es 150 Euro je kWp aus der EAG-Bundesförderung, also bis zu "
         "1.500 Euro für die PV-Anlage, plus 150 Euro je kWh Speicher. Der Made-in-Europe-Bonus bringt bis zu "
         "20 Prozent Zuschlag auf die PV-Anlage und 10 Prozent auf den Speicher. Mit Sanierungsbonus und "
         "Gemeindeförderung sind insgesamt 4.000 bis 6.000 Euro realistisch."),
        ("Wann sind die EAG-Fördercalls 2026?",
         "Der erste Call läuft vom 23. April (17:00 Uhr) bis 11. Mai 2026, der zweite vom 16. bis 30. Juni 2026, "
         "der dritte startet am 8. Oktober 2026. Der Steirische Sanierungsbonus hat ein eigenes Antragsfenster vom "
         "1. April bis 15. Mai 2026."),
        ("Gibt es in der Steiermark eine PV-Pauschale des Landes?",
         "Nein. Anders als Kärnten mit 3.000 Euro zahlt das Land Steiermark 2026 keine direkte PV-Pauschale. Die "
         "Landesförderung läuft über den Steirischen Sanierungsbonus mit maximal 15 Prozent der förderbaren Kosten "
         "und für Anlagen ab 20 kWp mit Doppelnutzung über den Ökofonds mit bis zu 30 Prozent."),
        ("Kann ich Bundes-, Landes- und Gemeindeförderung kombinieren?",
         "Ja, in der Steiermark ist die Kombination von EAG-Investitionszuschuss, Steirischem Sanierungsbonus und "
         "Gemeindeförderung grundsätzlich zulässig, sofern die beihilferechtlichen Höchstgrenzen eingehalten "
         "werden. Wichtig ist die Reihenfolge: EAG vor Baubeginn, Sanierungsbonus nach Fertigstellung."),
        ("Werden Stromspeicher 2026 in der Steiermark gefördert?",
         "Ja, über die EAG mit 150 Euro je kWh bis maximal 50 kWh, allerdings nur in Kombination mit der "
         "Neuerrichtung oder Erweiterung einer PV-Anlage. Eine reine Speichernachrüstung ist über die EAG nicht "
         "förderfähig. Mit Made-in-Europe-Bonus kommen 10 Prozent Zuschlag auf den Speicher dazu."),
        ("Was ist der Ökofonds Steiermark?",
         "Der Ökofonds fördert PV-Anlagen ab 20 kWp mit Doppelnutzung, etwa Parkplatzüberdachungen, "
         "bauwerksintegrierte PV, Floating- oder Agri-PV, mit bis zu 30 Prozent der Investitionskosten und maximal "
         "250.000 Euro je Antrag. Boni: 50 Euro je kWp für Made-in-Europe-Komponenten und 125 Euro je kWp bei "
         "Integration in ein dezentrales Energiesystem. Der aktuelle Call läuft bis Ende Mai 2026."),
        ("Muss der EAG-Antrag vor Baubeginn gestellt werden?",
         "Ja. Zum Zeitpunkt der Antragstellung darf mit der Errichtung noch nicht begonnen worden sein, und der "
         "Antrag muss vor Inbetriebnahme im Call eingereicht sein. Wer vorher baut, verliert den Bundeszuschuss."),
        ("Wer hilft mir bei der Förderabwicklung in der Steiermark?",
         "EBZ Energie mit Sitz in Villach betreut Kunden in ganz Kärnten und der Steiermark und übernimmt die "
         "komplette Förderabwicklung: Auswahl der Förderungen, Ticketziehung beim EAG-Call, Sanierungsbonus, "
         "Gemeindeförderung und Endabrechnung."),
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
    ],
    "related": [
        ("/photovoltaik-foerderung-kaernten/", "Photovoltaik-Förderung Kärnten 2026"),
        ("/photovoltaik-landesfoerderungen/", "PV-Landesförderungen: alle 9 Bundesländer"),
        ("/foerderung-fuer-pv-speicher/", "Förderung für PV-Speicher"),
        ("batteriespeicher", "Batteriespeicher: Planung und Auswahl"),
    ],
    "cta": {
        "h3": "Förderung in der Steiermark sichern",
        "text": "Wir planen Ihre Anlage förderfähig und übernehmen EAG-Ticket, Sanierungsbonus und Gemeindeantrag.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre PV-Anlage in der Steiermark, förderoptimiert geplant",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
