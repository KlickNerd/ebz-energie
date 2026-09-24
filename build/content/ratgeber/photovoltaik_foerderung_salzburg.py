"""Ratgeber: Photovoltaik-Förderung Salzburg 2026.

Migriert vom Live-Artikel ebz-photovoltaik.at/photovoltaik-foerderung-salzburg/
(Stand der Quelle: Mai 2026), nach README optimiert. Zahlen aus der Quelle
(EAG-Novelle 2026, Wegfall der Landes- und Stadtförderung, Heizungstausch-Förderung).
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
        ["Call 1", "23. April bis 11. Mai 2026", "erster Call des Jahres, meist hohe Nachfrage"],
        ["Call 2", "16. bis 30. Juni 2026", "Sommer-Call"],
        ["Call 3", "ab 8. Oktober 2026", "Herbst-Call"],
    ],
    hl_cols=(1,),
)

ARTICLE = {
    "slug": "photovoltaik-foerderung-salzburg",
    "path": "/photovoltaik-foerderung-salzburg/",
    "title": "PV-Förderung Salzburg 2026: bis 2.760 € vom Bund | EBZ",
    "description": ("PV-Förderung Salzburg 2026: Landesförderung ausgelaufen. Was bleibt: EAG 150 €/kWp, "
                    "150 €/kWh Speicher, Made-in-Europe-Bonus und Gemeindezuschüsse."),
    "eyebrow": "Förderung · Salzburg",
    "crumb_label": "PV-Förderung Salzburg 2026",
    "h1": "Photovoltaik-Förderung Salzburg 2026: Landesförderung weggefallen, so holen Sie rund 2.760 € und mehr über EAG und Gemeinde",
    "lead": ("Die Salzburger PV-Landesförderung mit bis zu 2.000 € für PV und Speicher ist mit 31. Dezember 2025 "
             "ersatzlos ausgelaufen, die Stadt Salzburg hat ihre Förderung mit 1. Jänner 2026 eingestellt. Privathaushalte "
             "setzen 2026 auf die EAG-Bundesförderung, den Made-in-Europe-Bonus und Gemeindezuschüsse."),
    "chips": [
        "EAG: <b>150 €/kWp</b> bis 10 kWp",
        "Speicher: <b>150 €/kWh</b> über EAG",
        "Bonus: <b>10 %</b> je Made-in-Europe-Komponente",
        "Gemeinde: <b>200 bis 1.000 €</b> möglich",
    ],
    "date_published": "2026-04-20",
    "date_modified": "2026-09-24",
    "hero_img": "gen_hero",
    "hero_alt": "Photovoltaikanlage auf einem Einfamilienhausdach bei Sonnenschein",

    "tldr": [
        "Salzburg hat 2026 keine eigene Landesförderung für PV-Anlagen oder Speicher mehr. Auch die Förderung der "
        "Stadt Salzburg ist mit 1. Jänner 2026 eingestellt. Das Land verweist Antragsteller direkt an die OeMAG.",
        "Der Hauptzuschuss ist die EAG-Bundesförderung: 150 €/kWp bis 10 kWp, 140 €/kWp bis 20 kWp, Speicher "
        "150 €/kWh bis 50 kWh, jeweils plus 10 % Made-in-Europe-Bonus pro gelisteter Komponente.",
        "Rechenbeispiel 8 kWp mit 8 kWh Speicher: 1.200 € PV plus 1.200 € Speicher plus 360 € Bonus ergeben rund "
        "2.760 € allein vom Bund.",
        "Gemeindeförderungen bringen je nach Wohnsitzgemeinde 200 bis 1.000 € zusätzlich. Die Wohnbauförderung "
        "des Landes ist nur im Sanierungskontext relevant.",
        "Der EAG-Antrag muss vor Inbetriebnahme im Fördercall gestellt werden: 23. April bis 11. Mai, 16. bis "
        "30. Juni, ab 8. Oktober 2026.",
    ],
    "kpis": [
        ("150 €/kWp", "EAG-Zuschuss Kategorie A (bis 10 kWp)"),
        ("2.760 €", "Beispiel 8 kWp + 8 kWh inkl. Bonus*"),
        ("0 €", "Landesförderung Salzburg für Privat-PV 2026"),
        ("7.500 €", "Bundespauschale Wärmepumpe (Sanierungsoffensive)"),
    ],

    "sections": [
        ("Die Photovoltaik-Förderung Salzburg 2026 im Überblick", "ueberblick", f"""
<p>Salzburg hat zum Jahreswechsel 2025/2026 einen harten Schnitt gemacht: Die PV-Landesförderung, die in der
Vergangenheit bis zu 2.000 € für die Kombination aus PV und Speicher brachte, ist mit 31. Dezember 2025
ersatzlos ausgelaufen. Die Stadt Salzburg hat ihre eigene Photovoltaikförderung mit 1. Jänner 2026 eingestellt.
Das Land konzentriert sich 2026 auf die betriebliche PV-Förderung und verweist Privathaushalte bei
Photovoltaik-Vorhaben direkt an die OeMAG beziehungsweise die EAG-Abwicklungsstelle des Bundes.</p>
<p>Was für Salzburger Privathaushalte 2026 bleibt:</p>
<ul>
  <li><b>EAG-Bundesförderung:</b> 120 bis 150 €/kWp plus 150 €/kWh Speicher plus Made-in-Europe-Bonus, der Hauptzuschuss</li>
  <li><b>Gemeindeförderungen:</b> uneinheitlich, je nach Wohnsitzgemeinde 200 bis 1.000 € möglich</li>
  <li><b>Wohnbauförderung Salzburg:</b> im Sanierungskontext relevant, nicht für reine Neubauten</li>
  <li><b>Landesförderung Privat:</b> weggefallen</li>
</ul>
<p>Damit hat Salzburg für Privathaushalte die schmalste Förderlandschaft aller Bundesländer. Wie groß der
Unterschied etwa zu Kärnten mit seiner 3.000-Euro-Pauschale ist, zeigt der
{a('/photovoltaik-landesfoerderungen/', 'Vergleich aller neun Landesförderungen')}.</p>
"""),
        ("EAG-Bundesförderung: nahezu der einzige Zuschuss für Salzburger Hausbesitzer", "eag", f"""
<p>Mit der EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026, kundgemacht am 16. Jänner 2026, sind die
Konditionen fixiert: 60 Millionen Euro Bundesmittel für PV- und Speicherprojekte, abgewickelt über die
EAG-Förderabwicklungsstelle der OeMAG. Die Fördersätze sind nach Anlagengröße gestaffelt:</p>
{EAG_TABLE}
<h3>Die drei EAG-Fördercalls 2026</h3>
{CALLS_TABLE}
<p>Die Antragstellung erfolgt online, in den Kategorien A und B nach dem First-come-first-served-Prinzip mit
Ticketziehung. Der Antrag muss vor Inbetriebnahme der Anlage gestellt werden. Wer im ersten Call kein Ticket
zieht, fällt in der Reihung deutlich zurück. Alle Details im Ratgeber
{a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}.</p>
"""),
        ("Made-in-Europe-Bonus: mehr Förderung durch europäische Komponenten", "made-in-europe", f"""
<p>Der Made-in-Europe-Bonus gilt seit Juni 2025 und auch 2026 weiter. Er honoriert Komponenten mit
europäischer Wertschöpfung: je 10 % Zuschlag für PV-Module, Wechselrichter und Stromspeicher. Auf den
PV-Zuschuss sind damit bis zu 20 % möglich, auf den Speicherzuschuss weitere 10 %. Voraussetzung: Die
Komponenten stehen auf der White List der OeMAG und wurden nachweislich im Europäischen Wirtschaftsraum oder
in der Schweiz produziert. Für Salzburger Hausbesitzer, die stark auf die EAG angewiesen sind, gleicht der
Bonus den Wegfall der Landesförderung teilweise aus.</p>
<h3>Rechenbeispiel: 8-kWp-Anlage mit 8-kWh-Speicher (Kategorie A)</h3>
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
<p>Rund 2.760 € allein vom Bund. Wer in seiner Wohnsitzgemeinde noch eine PV- oder Speicherförderung findet,
erhöht den Betrag um 200 bis 1.000 €. Bei größeren Anlagen der Kategorie B mit größerem Speicher sind bis rund
4.500 €* erreichbar.</p>
<p><small>*Richtwerte auf Basis der EAG-Fördersätze 2026. Die tatsächliche Höhe hängt von Anlagengröße,
Speicherkapazität und den verbauten Komponenten ab.</small></p>
{A.cta("Komponenten mit Bonus, Antrag im richtigen Call",
       "EBZ Energie plant Ihre Anlage mit gelisteten Komponenten, erstellt Projektbericht mit 3D-Belegplan und "
       "Statikreport und stellt den EAG-Antrag vor Inbetriebnahme.",
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
<p>In den meisten Fällen lassen sich Gemeindezuschüsse mit der EAG-Bundesförderung kombinieren, sofern die
beihilferechtlichen Höchstgrenzen eingehalten werden.</p>
{A.box("Drei Fragen an Ihre Gemeinde: Gibt es 2026 eine PV- oder Speicherförderung? Wie hoch ist der Zuschuss "
       "und welche Voraussetzungen gelten? Ist die Kombination mit der EAG-Bundesförderung möglich?", label="Tipp:")}
"""),
        ("Wärmepumpe und Heizungstausch: die zweite Förderschiene", "waermepumpe", f"""
<p>Wer im Zuge der PV-Investition die alte Öl-, Gas- oder Kohleheizung gegen eine {a('waermepumpe', 'Wärmepumpe')}
oder Biomasseanlage tauscht, profitiert von Bundesförderungen, die den Wegfall der Salzburger PV-Landesförderung
teilweise kompensieren:</p>
<ul>
  <li><b>Sanierungsoffensive (Wärmepumpe):</b> Pauschale bis zu 7.500 €</li>
  <li><b>Sanierungsoffensive (Biomasse):</b> Pauschale bis zu 8.500 €</li>
  <li><b>„Sauber Heizen für Alle“</b> (einkommensschwache Haushalte): bis zu 100 % Förderung</li>
</ul>
<p>Technisch passt die Kombination ohnehin: Die Wärmepumpe nutzt den selbst erzeugten PV-Strom direkt, der
Eigenverbrauch steigt, und die Energiekosten sinken um bis zu 85 %. Mehr dazu im Ratgeber
{a('/sauber-heizen-fuer-alle-2026/', 'Sauber Heizen für Alle 2026')}.</p>
"""),
        ("Voraussetzungen und Antragsablauf", "ablauf", f"""
<p>Die EAG-Voraussetzungen sind bundesweit einheitlich und gelten auch in Salzburg:</p>
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
    ("EAG-Antrag im Fördercall",
     "Online über die EAG-Abwicklungsstelle, in Kategorie A und B mit Ticketziehung, zwingend vor Inbetriebnahme. "
     "Calls 2026: 23. April bis 11. Mai, 16. bis 30. Juni, ab 8. Oktober."),
    ("Inbetriebnahme und Endabrechnung",
     "Nach Inbetriebnahme Rechnungen (per Überweisung bezahlt) und Nachweise einreichen, danach wird der Zuschuss "
     "ausbezahlt. Gemeindeförderung nach lokaler Richtlinie beantragen."),
])}
{A.box_dark("Der häufigste Fehler",
    "Die Anlage geht in Betrieb, bevor der EAG-Antrag gestellt wurde. In Salzburg gibt es 2026 keine "
    "Landesförderung, die diesen Verlust auffangen könnte.")}
"""),
        ("Fazit: Auch ohne Landesförderung lohnt sich der Blick auf die Zahlen", "fazit", f"""
<p>Salzburg hat 2026 die strikteste Förderlandschaft aller Bundesländer, die PV-Landesförderung ist komplett
weggefallen. Trotzdem sind über die EAG-Bundesförderung rund 2.760 € für 8 kWp mit 8 kWh Speicher und bis rund
4.500 €* bei größeren Anlagen möglich, mit Gemeindezuschuss entsprechend mehr. Die Strategie: Komponenten mit
Made-in-Europe-Zertifizierung wählen, Gemeindeförderung recherchieren, idealerweise mit einer Wärmepumpe
kombinieren und den Antrag vor Inbetriebnahme stellen.</p>
<p><small>Stand: Mai 2026. Förderhöhen, Budgets und Fristen können sich ändern, maßgeblich sind die Richtlinien
der EAG-Abwicklungsstelle (OeMAG), des Landes Salzburg und der jeweiligen Gemeinde.</small></p>
{A.cta("Förderstrategie für Ihr Projekt in Salzburg",
       "Wir planen mit gelisteten Komponenten, prüfen Ihre Gemeindeförderung und übernehmen den EAG-Antrag "
       "im richtigen Call.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("finanzierung", "Finanzierung ab 147 €/Monat"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Planung und Förderabwicklung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant Photovoltaikanlagen, Speicher und Wärmepumpen und hat über 300 Projekte "
                 "in sechs Bundesländern dokumentiert. Für Projekte in Salzburg übernehmen wir Beratung, Planung mit "
                 "Projektbericht (3D-Belegplan und Statikreport) und die Förderabwicklung aus einer Hand: "
                 "Made-in-Europe-Komponentenwahl, EAG-Call, Gemeindeförderung und Wärmepumpen-Förderung."),
        "grid": [
            ("Förderabwicklung komplett", "EAG-Antrag, Gemeindezuschuss und Heizungstausch-Förderung."),
            ("White-List-Komponenten", "Module, Wechselrichter und Speicher mit Made-in-Europe-Bonus."),
            ("PV plus Wärmepumpe", "Bis zu 7.500 € Bundespauschale für die Wärmepumpe mitplanen."),
            ("Referenzen in 6 Bundesländern", "300+ Projekte, 4,9 Sterne auf Google."),
        ],
    },

    "faq": [
        ("Gibt es 2026 in Salzburg noch eine PV-Landesförderung?",
         "Nein. Die Salzburger PV-Landesförderung ist mit 31. Dezember 2025 ersatzlos ausgelaufen, die Förderung der "
         "Stadt Salzburg wurde mit 1. Jänner 2026 eingestellt. Privathaushalte sind 2026 nahezu vollständig auf die "
         "EAG-Bundesförderung angewiesen, ergänzt durch mögliche Gemeindezuschüsse."),
        ("Wie hoch ist die maximale PV-Förderung in Salzburg 2026?",
         "Für eine private 8-kWp-Anlage mit 8-kWh-Speicher sind rund 2.760 € vom Bund realistisch: 2.400 € "
         "EAG-Zuschuss plus 360 € Made-in-Europe-Bonus. Gemeindezuschüsse bringen je nach Wohnsitzgemeinde 200 bis "
         "1.000 € zusätzlich, größere Anlagen erreichen bis rund 4.500 € (Richtwerte)."),
        ("Werden Stromspeicher 2026 in Salzburg gefördert?",
         "Nur über die EAG-Bundesförderung: 150 €/kWh bis maximal 50 kWh, ausschließlich in Kombination mit einer "
         "PV-Neuerrichtung oder -Erweiterung und mit mindestens 0,5 kWh pro kWp. Eine reine Speicher-Nachrüstung ohne "
         "PV ist über die EAG nicht förderfähig, eine separate Salzburger Speicherförderung gibt es 2026 nicht mehr."),
        ("Was bringt der Made-in-Europe-Bonus?",
         "Je 10 % Zuschlag auf den EAG-Zuschuss für PV-Module, Wechselrichter und Speicher, die auf der White List der "
         "OeMAG stehen. Bei 8 kWp und 8 kWh sind das 240 € auf den PV-Zuschuss und 120 € auf den Speicherzuschuss, "
         "in Summe 360 €."),
        ("Wann sind die EAG-Fördercalls 2026?",
         "Die drei Calls laufen vom 23. April bis 11. Mai, vom 16. bis 30. Juni und ab 8. Oktober 2026. In den "
         "Kategorien A und B gilt First come, first served mit Ticketziehung. Der Antrag muss vor Inbetriebnahme "
         "gestellt werden."),
        ("Kann ich Gemeindeförderung und EAG kombinieren?",
         "In den meisten Fällen ja, sofern die beihilferechtlichen Höchstgrenzen eingehalten werden. Fragen Sie beim "
         "Gemeindeamt nach Höhe, Voraussetzungen und Kombinierbarkeit. Die Stadt Salzburg selbst fördert seit "
         "1. Jänner 2026 nicht mehr."),
        ("Lohnt sich eine PV-Anlage in Salzburg 2026 trotz Wegfall der Landesförderung?",
         "Ja. Der Wegfall wird durch Made-in-Europe-Bonus, Gemeindezuschüsse und gestiegene Strompreise teilweise "
         "ausgeglichen. Entscheidend ist ein hoher Eigenverbrauch, idealerweise über 40 % mit Speicher, und die "
         "Kombination mit einer Wärmepumpe. Bei EBZ-Referenzprojekten liegt die Amortisation typisch bei 4 bis 6 Jahren, "
         "bei 25 bis 30 Jahren Lebensdauer der Module."),
        ("Wer hilft bei der Förderabwicklung in Salzburg?",
         "EBZ Energie aus Villach übernimmt für Projekte in Salzburg Beratung, Planung und Förderabwicklung aus einer "
         "Hand, von der Komponentenwahl für den Made-in-Europe-Bonus über den EAG-Call bis zur Endabrechnung. "
         "Referenzen liegen in sechs Bundesländern vor."),
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
        "h3": "EAG-Förderung in Salzburg sichern",
        "text": "Wir wählen Komponenten mit Bonus, prüfen Ihre Gemeindeförderung und stellen den Antrag vor Inbetriebnahme.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre PV-Förderung in Salzburg, vollständig genutzt",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung und "
                   "Förderabwicklung aus einer Hand übernimmt."),
}
