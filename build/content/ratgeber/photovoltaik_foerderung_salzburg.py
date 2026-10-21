"""Ratgeber: Photovoltaik-Förderung Salzburg 2026.

Migriert vom Live-Artikel ebz-photovoltaik.at/photovoltaik-foerderung-salzburg/
(Stand der Quelle: Mai 2026), nach README optimiert. Zahlen aus der Quelle
(EAG-Novelle 2026, Wegfall der Landes- und Stadtförderung, Heizungstausch-Förderung).
Stand ab 23.10.2026: letzter EAG-Call 2026 lief 8. bis 22.10.2026, derzeit kein Bundeszuschuss;
Ausblick 2027 Systemfoerderung laut BMWET (geplant, nicht beschlossen).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

EAG_TABLE = A.table(
    ["Kategorie", "Anlagengröße", "Fördersatz PV", "Speicher"],
    [
        ["A", "bis 10 kWp", "150 €/kWp", "150 €/kWh (max. 50 kWh)"],
        ["B", "10 bis 20 kWp", "140 €/kWp", "150 €/kWh (max. 50 kWh)"],
        ["C", "20 bis 100 kWp", "max. 130 €/kWp", "150 €/kWh (max. 50 kWh)"],
        ["D", "100 bis 1.000 kWp", "max. 120 €/kWp", "150 €/kWh (max. 50 kWh)"],
    ],
    hl_cols=(2,),
)

CALLS_TABLE = A.table(
    ["Call", "Zeitraum", "Hinweis"],
    [
        ["Call 1", "23. April bis 11. Mai 2026", "erster Call des Jahres, beendet"],
        ["Call 2", "16. bis 30. Juni 2026", "Sommer-Call, beendet"],
        ["Call 3", "8. bis 22. Oktober 2026", "Herbst-Call, letzter Call im bisherigen System, beendet"],
    ],
    hl_cols=(1,),
)

ARTICLE = {
    "slug": "photovoltaik-foerderung-salzburg",
    "path": "/photovoltaik-foerderung-salzburg/",
    "title": "PV-Förderung Salzburg 2026: Land weg, Bund beendet | EBZ",
    "description": ("PV-Förderung Salzburg 2026: Landesförderung ausgelaufen, der letzte EAG-Call endete am "
                    "22. Oktober. Was bleibt: Gemeindezuschüsse und der Ausblick auf 2027."),
    "eyebrow": "Förderung · Salzburg",
    "crumb_label": "PV-Förderung Salzburg 2026",
    "h1": "Photovoltaik-Förderung Salzburg 2026: Landesförderung weggefallen, EAG-Call beendet, was jetzt noch bleibt",
    "lead": ("Die Salzburger PV-Landesförderung mit bis zu 2.000 € für PV und Speicher ist mit 31. Dezember 2025 "
             "ersatzlos ausgelaufen, die Stadt Salzburg hat ihre Förderung mit 1. Jänner 2026 eingestellt. Der "
             "Hauptzuschuss 2026 war die EAG-Bundesförderung, deren letzter Call vom 8. bis 22. Oktober 2026 lief; "
             "derzeit bleiben Gemeindezuschüsse, ab 2027 ist laut BMWET eine Systemförderung geplant, nicht beschlossen."),
    "chips": [
        "EAG im Call 2026: <b>150 €/kWp</b> bis 10 kWp",
        "Speicher im Call 2026: <b>150 €/kWh</b>",
        "Letzter Call: <b>8. bis 22. Oktober 2026</b>, beendet",
        "Gemeinde: <b>200 bis 1.000 €</b> möglich",
    ],
    "date_published": "2026-04-20",
    "date_modified": "2026-10-21",
    "hero_img": "gen_hero",
    "hero_alt": "Photovoltaikanlage auf einem Einfamilienhausdach bei Sonnenschein",

    "tldr": [
        "Salzburg hat 2026 keine eigene Landesförderung für PV-Anlagen oder Speicher mehr. Auch die Förderung der "
        "Stadt Salzburg ist mit 1. Jänner 2026 eingestellt. Das Land verweist Antragsteller direkt an die OeMAG.",
        "Der Hauptzuschuss 2026 war die EAG-Bundesförderung: im Call 2026 150 €/kWp bis 10 kWp, 140 €/kWp bis "
        "20 kWp, Speicher 150 €/kWh bis 50 kWh, jeweils plus 10 % Made-in-Europe-Bonus pro gelisteter Komponente. "
        "Der letzte Call endete am 22. Oktober 2026, derzeit ist kein Bundeszuschuss beantragbar.",
        "Rechenbeispiel im Call 2026, 8 kWp mit 8 kWh Speicher: 1.200 € PV plus 1.200 € Speicher plus 360 € Bonus "
        "ergaben rund 2.760 € vom Bund.",
        "Gemeindeförderungen bringen je nach Wohnsitzgemeinde 200 bis 1.000 € zusätzlich. Die Wohnbauförderung "
        "des Landes ist nur im Sanierungskontext relevant.",
        "Ab 2027 ist laut BMWET eine Systemförderung geplant, nicht beschlossen: Speicher mit intelligenter "
        "Steuerung, Antrag nach Installation und Rechnung, Projekte ab 1. November 2026 sollen beantragbar sein. "
        "Wer jetzt plant, baut mit Speicher und Energiemanagement.",
    ],
    "kpis": [
        ("150 €/kWp", "EAG Kategorie A im Call 2026 (bis 10 kWp)"),
        ("2.760 €", "Beispiel 8 kWp + 8 kWh im Call 2026*"),
        ("0 €", "Landesförderung Salzburg für Privat-PV 2026"),
        ("beendet", "Bundes-Wärmepumpenförderung 2026 (ausgeschöpft)"),
    ],

    "sections": [
        ("Die Photovoltaik-Förderung Salzburg 2026 im Überblick", "ueberblick", f"""
<p>Salzburg hat zum Jahreswechsel 2025/2026 einen harten Schnitt gemacht: Die PV-Landesförderung, die in der
Vergangenheit bis zu 2.000 € für die Kombination aus PV und Speicher brachte, ist mit 31. Dezember 2025
ersatzlos ausgelaufen. Die Stadt Salzburg hat ihre eigene Photovoltaikförderung mit 1. Jänner 2026 eingestellt.
Das Land konzentriert sich 2026 auf die betriebliche PV-Förderung und verweist Privathaushalte bei
Photovoltaik-Vorhaben direkt an die OeMAG beziehungsweise die EAG-Abwicklungsstelle des Bundes.</p>
<p>Was für Salzburger Privathaushalte 2026 galt und gilt:</p>
<ul>
  <li><b>EAG-Bundesförderung:</b> im Call 2026 120 bis 150 €/kWp plus 150 €/kWh Speicher plus Made-in-Europe-Bonus, der Hauptzuschuss; der letzte Call endete am 22. Oktober 2026, derzeit nicht beantragbar</li>
  <li><b>Gemeindeförderungen:</b> uneinheitlich, je nach Wohnsitzgemeinde 200 bis 1.000 € möglich</li>
  <li><b>Wohnbauförderung Salzburg:</b> im Sanierungskontext relevant, nicht für reine Neubauten</li>
  <li><b>Landesförderung Privat:</b> weggefallen</li>
</ul>
<p>Damit hat Salzburg für Privathaushalte die schmalste Förderlandschaft aller Bundesländer. Wie groß der
Unterschied etwa zu Kärnten mit seiner 3.000-Euro-Pauschale ist, zeigt der
{a('/photovoltaik-landesfoerderungen/', 'Vergleich aller neun Landesförderungen')}.</p>
"""),
        ("EAG-Bundesförderung: 2026 nahezu der einzige Zuschuss für Salzburger Hausbesitzer", "eag", f"""
<p>Mit der EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026, kundgemacht am 16. Jänner 2026, waren die
Konditionen fixiert: 60 Millionen Euro Bundesmittel für PV- und Speicherprojekte, abgewickelt über die
EAG-Förderabwicklungsstelle der OeMAG. Die Fördersätze im Call 2026 waren nach Anlagengröße gestaffelt:</p>
{EAG_TABLE}
<h3>Die drei EAG-Fördercalls 2026</h3>
{CALLS_TABLE}
<p>Die Antragstellung erfolgte online, in den Kategorien A und B nach dem First-come-first-served-Prinzip mit
Ticketziehung, und musste vor Inbetriebnahme der Anlage liegen. Der dritte und letzte Call lief vom 8. bis
22. Oktober 2026; im bisherigen System gibt es keinen weiteren Call, neue Anlagen bekommen derzeit keinen
Bundeszuschuss. Ab 2027 ist laut BMWET eine Systemförderung geplant, nicht beschlossen: Speicher mit
intelligenter Steuerung, Antrag nach Installation und Rechnung, Projekte ab 1. November 2026 sollen
beantragbar sein, die Höhe ist offen. Alle Details im Ratgeber
{a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}.</p>
"""),
        ("Made-in-Europe-Bonus: mehr Förderung durch europäische Komponenten", "made-in-europe", f"""
<p>Der Made-in-Europe-Bonus galt seit Juni 2025 und im Call 2026. Er honorierte Komponenten mit
europäischer Wertschöpfung: je 10 % Zuschlag für PV-Module, Wechselrichter und Stromspeicher. Auf den
PV-Zuschuss waren damit bis zu 20 % möglich, auf den Speicherzuschuss weitere 10 %. Voraussetzung: Die
Komponenten standen auf der White List der OeMAG und wurden nachweislich im Europäischen Wirtschaftsraum oder
in der Schweiz produziert. Für die Systemförderung 2027 ist laut BMWET wieder ein Europa-Bonus geplant, Höhe
offen.</p>
<h3>Rechenbeispiel im Call 2026: 8-kWp-Anlage mit 8-kWh-Speicher (Kategorie A)</h3>
{A.table(
    ["Förderposition", "Rechnung", "Betrag"],
    [
        ["EAG-Zuschuss PV", "8 kWp × 150 €/kWp", "1.200 €"],
        ["EAG-Zuschuss Speicher", "8 kWh × 150 €/kWh", "1.200 €"],
        ["Made-in-Europe-Bonus PV", "20 % auf 1.200 €", "240 €"],
        ["Made-in-Europe-Bonus Speicher", "10 % auf 1.200 €", "120 €"],
        ["<b>Gesamtförderung ohne Gemeinde</b>", "", "<b>rund 2.760 €*</b>"],
    ],
    hl_cols=(2,),
)}
<p>Im Call 2026 waren das rund 2.760 € vom Bund, bei größeren Anlagen der Kategorie B mit größerem Speicher
bis rund 4.500 €*. Derzeit ist kein Bundeszuschuss beantragbar. Wer in seiner Wohnsitzgemeinde eine PV- oder
Speicherförderung findet, erhält 200 bis 1.000 €.</p>
<p><small>*Richtwerte auf Basis der EAG-Fördersätze im Call 2026 (beendet). Die tatsächliche Höhe hing von
Anlagengröße, Speicherkapazität und den verbauten Komponenten ab.</small></p>
{A.cta("Jetzt mit Speicher planen",
       "EBZ Energie plant Ihre Anlage mit Speicher und Energiemanagement, erstellt Projektbericht mit 3D-Belegplan "
       "und Statikreport und behält die geplante Systemförderung 2027 im Blick.",
       secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
        ("Wohnbauförderung Salzburg im Sanierungskontext", "wohnbaufoerderung", f"""
<p>Auch ohne direkte PV-Landesförderung kann die Salzburger Wohnbauförderung relevant werden, wenn Sie Ihr
Eigenheim ohnehin energetisch sanieren: Fassadendämmung, Fenstertausch, Heizungsmodernisierung. Dann lohnt die
Prüfung, ob die PV-Anlage als ökologische Maßnahme Teil eines förderbaren Gesamtkonzepts wird.</p>
<p>Bei reinen Neubauvorhaben wird die Wohnbauförderung für PV grundsätzlich nicht gewährt, hier verweist das
Land an die OeMAG. Im Sanierungskontext können Gesamtsanierungs-Förderungen greifen, die auch PV oder
Wärmepumpen berücksichtigen. Die Konditionen ändern sich regelmäßig, eine individuelle Auskunft beim Land
Salzburg ist unerlässlich.</p>
"""),
        ("Gemeindeförderungen: der oft übersehene Topf", "gemeinden", f"""
<p>Während die Landesförderung weggefallen ist, bieten viele Salzburger Gemeinden weiterhin eigene
PV-Programme: pauschale Fixzuschüsse, Speicherboni oder prozentuale Beteiligungen an den Investitionskosten.
Manche setzen Schwerpunkte auf Speicher, andere auf E-Mobilität und Wallboxen. Weil die Stadt Salzburg ihre
Förderung mit 1. Jänner 2026 eingestellt hat, gilt das vor allem für die ländlicheren Gemeinden.</p>
<p>Im Call 2026 ließen sich Gemeindezuschüsse in den meisten Fällen mit der EAG-Bundesförderung kombinieren,
sofern die beihilferechtlichen Höchstgrenzen eingehalten wurden. Seit dem Ende des letzten Calls am
22. Oktober 2026 ist die Gemeinde für neue Anlagen oft der einzige verfügbare Zuschuss.</p>
{A.box("Drei Fragen an Ihre Gemeinde: Gibt es eine PV- oder Speicherförderung? Wie hoch ist der Zuschuss "
       "und welche Voraussetzungen gelten? Ist die Kombination mit einer künftigen Bundesförderung möglich?", label="Tipp:")}
"""),
        ("Wärmepumpe und Heizungstausch: die zweite Förderschiene", "waermepumpe", f"""
<p>Wer im Zuge der PV-Investition die alte Öl-, Gas- oder Kohleheizung gegen eine {a('waermepumpe', 'Wärmepumpe')}
oder Biomasseanlage tauscht, profitiert von Bundesförderungen, die den Wegfall der Salzburger PV-Landesförderung
teilweise kompensieren:</p>
<ul>
  <li><b>Sanierungsoffensive (Wärmepumpe):</b> galt 2026 mit bis zu 7.500 € Pauschale, seit Herbst 2026 ausgeschöpft, keine Registrierung mehr möglich (Stand Oktober 2026)</li>
  <li><b>Sanierungsoffensive (Biomasse):</b> Pauschale bis zu 8.500 €</li>
  <li><b>„Sauber Heizen für Alle“</b> (einkommensschwache Haushalte): bis zu 100 % Förderung</li>
</ul>
<p>Technisch passt die Kombination ohnehin: Die Wärmepumpe nutzt den selbst erzeugten PV-Strom direkt, der
Eigenverbrauch steigt, und die Energiekosten sinken um bis zu 85 %. Mehr dazu im Ratgeber
{a('/sauber-heizen-fuer-alle-2026/', 'Sauber Heizen für Alle 2026')}.</p>
"""),
        ("Voraussetzungen und Antragsablauf", "ablauf", f"""
<p>Die EAG-Voraussetzungen im Call 2026 waren bundesweit einheitlich und galten auch in Salzburg. Der letzte
Call endete am 22. Oktober 2026; für die geplante Systemförderung 2027 sind die Kriterien noch offen:</p>
<ul>
  <li>Eigentum an der Liegenschaft oder schriftliche Einwilligung des Eigentümers</li>
  <li>Bestehende Elektroinstallation und Erdungsanlage nach Stand der Technik</li>
  <li>Anschluss an das öffentliche Stromnetz (Inselanlagen sind nicht förderfähig)</li>
  <li>Antragstellung vor Inbetriebnahme; anerkannt werden Kosten ab frühestens 21. April 2022</li>
  <li>Alle Genehmigungen oder Anzeigen in erster Instanz liegen vor, inklusive Zählpunkt und Netzzugang</li>
  <li>Speicher nur in Kombination mit PV-Neuanlage oder -Erweiterung, mindestens 0,5 kWh pro kWp</li>
  <li>Zahlung ausschließlich per Überweisung, keine Barzahlung</li>
</ul>
{A.steps([
    ("Gemeindeförderung prüfen",
     "Vor der Planung beim Gemeindeamt nachfragen, ob und in welcher Höhe 2026 ein PV- oder Speicherzuschuss besteht."),
    ("Planung und Komponenten",
     "Anlagengröße und Speicher (mindestens 0,5 kWh pro kWp) festlegen. Für den Made-in-Europe-Bonus müssen Module, "
     "Wechselrichter und Speicher auf der White List der OeMAG stehen."),
    ("Genehmigungen und Netzzugang",
     "Anzeigen oder Genehmigungen einholen, Zählpunkt und Netzzugang beim Netzbetreiber beantragen. Diese Unterlagen "
     "müssen bei Antragstellung vorliegen."),
    ("EAG-Antrag im Fördercall (2026)",
     "Online über die EAG-Abwicklungsstelle, in Kategorie A und B mit Ticketziehung, zwingend vor Inbetriebnahme. "
     "Calls 2026: 23. April bis 11. Mai, 16. bis 30. Juni, 8. bis 22. Oktober, alle beendet. Für 2027 soll der "
     "Antrag laut BMWET nach Installation und Rechnung kommen (geplant, nicht beschlossen)."),
    ("Inbetriebnahme und Endabrechnung",
     "Nach Inbetriebnahme Rechnungen (per Überweisung bezahlt) und Nachweise einreichen, danach wird der Zuschuss "
     "ausbezahlt. Gemeindeförderung nach lokaler Richtlinie beantragen."),
])}
{A.box_dark("Der häufigste Fehler im Call 2026",
    "Die Anlage ging in Betrieb, bevor der EAG-Antrag gestellt wurde. In Salzburg gibt es 2026 keine "
    "Landesförderung, die diesen Verlust auffangen konnte. Wer jetzt plant, baut mit Speicher und "
    "Energiemanagement, damit die Anlage für die geplante Systemförderung 2027 in Frage kommt.")}
"""),
        ("Fazit: Auch ohne Landesförderung lohnt sich der Blick auf die Zahlen", "fazit", f"""
<p>Salzburg hat 2026 die strikteste Förderlandschaft aller Bundesländer, die PV-Landesförderung ist komplett
weggefallen. Im Call 2026 brachte die EAG-Bundesförderung rund 2.760 € für 8 kWp mit 8 kWh Speicher und bis rund
4.500 €* bei größeren Anlagen; seit dem 22. Oktober 2026 ist kein Bundeszuschuss mehr beantragbar. Die Strategie
jetzt: Gemeindeförderung recherchieren, mit Speicher und Energiemanagement bauen (Chance auf die laut BMWET
geplante Systemförderung 2027) und idealerweise mit einer Wärmepumpe kombinieren.</p>
<p><small>Stand: Mai 2026. Förderhöhen, Budgets und Fristen können sich ändern, maßgeblich sind die Richtlinien
der EAG-Abwicklungsstelle (OeMAG), des Landes Salzburg und der jeweiligen Gemeinde.</small></p>
<p><b>Stand ab 23. Oktober 2026:</b> Der dritte Call lief vom 8. bis 22. Oktober 2026 und war der letzte im
bisherigen System. Neue Anlagen bekommen derzeit keinen Bundeszuschuss. Ab 2027 ist laut Eckpunkten des
BMWET eine Systemförderung geplant, aber nicht beschlossen: Antrag nach Installation und Rechnung statt
Fördercall, gefördert werden sollen Speicher mit intelligenter Steuerung, auch als Nachrüstung; Projekte mit
intelligentem Speicher, die ab 1. November 2026 in Betrieb gehen, sollen 2027 beantragbar sein. Höhe und
Technikkriterien sind noch offen.</p>
{A.cta("Förderstrategie für Ihr Projekt in Salzburg",
       "Wir planen mit Speicher und Energiemanagement, prüfen Ihre Gemeindeförderung und behalten die geplante "
       "Systemförderung 2027 im Blick.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("finanzierung", "Finanzierung ab 147 €/Monat"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Planung und Förderabwicklung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant Photovoltaikanlagen, Speicher und Wärmepumpen und hat über 300 Projekte "
                 "in sechs Bundesländern dokumentiert. Für Projekte in Salzburg übernehmen wir Beratung, Planung mit "
                 "Projektbericht (3D-Belegplan und Statikreport) und die Förderabwicklung aus einer Hand: "
                 "Komponentenwahl, Gemeindeförderung, Wärmepumpen-Förderung und Vorbereitung auf die geplante "
                 "Systemförderung 2027."),
        "grid": [
            ("Förderabwicklung komplett", "Gemeindezuschuss, Heizungstausch-Förderung und Blick auf die Kriterien 2027."),
            ("Europäische Komponenten", "Module, Wechselrichter und Speicher, für 2027 ist laut BMWET ein Europa-Bonus geplant."),
            ("PV plus Wärmepumpe", "Die Bundespauschale 2026 ist ausgeschöpft; Landesförderung Salzburg und Ausblick 2027 prüfen wir mit."),
            ("Referenzen in 6 Bundesländern", "300+ Projekte, 4,9 Sterne auf Google."),
        ],
    },

    "faq": [
        ("Gibt es 2026 in Salzburg noch eine PV-Landesförderung?",
         "Nein. Die Salzburger PV-Landesförderung ist mit 31. Dezember 2025 ersatzlos ausgelaufen, die Förderung der "
         "Stadt Salzburg wurde mit 1. Jänner 2026 eingestellt. Privathaushalte waren 2026 nahezu vollständig auf die "
         "EAG-Bundesförderung angewiesen, deren letzter Call am 22. Oktober 2026 endete. Derzeit bleiben mögliche "
         "Gemeindezuschüsse."),
        ("Wie hoch war die PV-Förderung in Salzburg 2026?",
         "Im Call 2026 waren für eine private 8-kWp-Anlage mit 8-kWh-Speicher rund 2.760 € vom Bund realistisch: "
         "2.400 € EAG-Zuschuss plus 360 € Made-in-Europe-Bonus, größere Anlagen erreichten bis rund 4.500 € "
         "(Richtwerte). Derzeit ist kein Bundeszuschuss beantragbar; Gemeindezuschüsse bringen je nach "
         "Wohnsitzgemeinde 200 bis 1.000 €."),
        ("Werden Stromspeicher in Salzburg gefördert?",
         "Derzeit nicht vom Land und nicht vom Bund. Im Call 2026 gab es über die EAG 150 €/kWh bis maximal 50 kWh, "
         "nur mit PV-Neuerrichtung oder -Erweiterung. Ab 2027 ist laut BMWET eine Systemförderung für Speicher mit "
         "intelligenter Steuerung geplant, auch als Nachrüstung (nicht beschlossen, Höhe offen)."),
        ("Was brachte der Made-in-Europe-Bonus?",
         "Im Call 2026 je 10 % Zuschlag auf den EAG-Zuschuss für PV-Module, Wechselrichter und Speicher von der White "
         "List der OeMAG. Bei 8 kWp und 8 kWh waren das 240 € auf den PV-Zuschuss und 120 € auf den "
         "Speicherzuschuss, in Summe 360 €. Für 2027 ist laut BMWET wieder ein Europa-Bonus geplant, Höhe offen."),
        ("Wann waren die EAG-Fördercalls 2026?",
         "Die drei Calls liefen vom 23. April bis 11. Mai, vom 16. bis 30. Juni und vom 8. bis 22. Oktober 2026, "
         "jeweils mit Ticketziehung und Antrag vor Inbetriebnahme. Im bisherigen System gibt es keinen weiteren Call. "
         "Projekte mit intelligentem Speicher ab 1. November 2026 sollen laut BMWET 2027 beantragbar sein."),
        ("Kann ich Gemeindeförderung und Bundesförderung kombinieren?",
         "Im Call 2026 in den meisten Fällen ja, sofern die beihilferechtlichen Höchstgrenzen eingehalten wurden. "
         "Wie die geplante Systemförderung 2027 mit Gemeindezuschüssen zusammenspielt, ist offen. Fragen Sie beim "
         "Gemeindeamt nach Höhe und Voraussetzungen; die Stadt Salzburg selbst fördert seit 1. Jänner 2026 nicht mehr."),
        ("Lohnt sich eine PV-Anlage in Salzburg 2026 trotz Wegfall der Landesförderung?",
         "Ja. Der Wegfall wird durch Gemeindezuschüsse und gestiegene Strompreise teilweise ausgeglichen. Entscheidend ist ein hoher Eigenverbrauch, idealerweise über 40 % mit Speicher, und die "
         "Kombination mit einer Wärmepumpe. Bei EBZ-Referenzprojekten liegt die Amortisation typisch bei 4 bis 6 Jahren, "
         "bei 25 bis 30 Jahren Lebensdauer der Module."),
        ("Wer hilft bei der Förderabwicklung in Salzburg?",
         "EBZ Energie aus Villach übernimmt für Projekte in Salzburg Beratung, Planung und Förderabwicklung aus einer "
         "Hand, von der Komponentenwahl über die Gemeindeförderung bis zur Vorbereitung auf die geplante "
         "Systemförderung 2027. Referenzen liegen in sechs Bundesländern vor."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant PV-Anlagen, Speicher und "
                    "Wärmepumpen und übernimmt die Förderabwicklung, Referenzen liegen in sechs Bundesländern vor. "
                    "Die Angaben werden anhand der offiziellen Unterlagen von OeMAG und Land Salzburg geprüft. Keine "
                    "Rechts- oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("EAG-Förderabwicklungsstelle der OeMAG", "https://www.eag-abwicklungsstelle.at/"),
        ("White List der OeMAG (Made-in-Europe-Komponenten)", "https://www.oem-ag.at/"),
        ("Land Salzburg: Förderungen", "https://www.salzburg.gv.at/"),
    ],
    "related": [
        ("/photovoltaik-landesfoerderungen/", "Vergleich: PV-Landesförderungen aller 9 Bundesländer"),
        ("/photovoltaik-foerderung-oesterreich-2026/", "Photovoltaik-Förderung Österreich 2026 (EAG)"),
        ("/foerderung-fuer-pv-speicher/", "Förderung für PV-Speicher"),
        ("waermepumpe", "Wärmepumpe: Planung und Förderung"),
    ],
    "cta": {
        "h3": "PV in Salzburg richtig planen",
        "text": "EAG-Call 2026 beendet: Wir planen mit Speicher und Energiemanagement, prüfen Ihre Gemeindeförderung und behalten 2027 im Blick.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre PV-Förderung in Salzburg, vollständig genutzt",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung und "
                   "Förderabwicklung aus einer Hand übernimmt."),
}
