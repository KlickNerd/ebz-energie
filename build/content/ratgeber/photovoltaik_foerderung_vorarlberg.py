"""Ratgeber: Photovoltaik-Förderung Vorarlberg 2026.

Migriert vom Live-Artikel ebz-photovoltaik.at/photovoltaik-foerderung-vorarlberg/
(Stand der Quelle: Mai 2026), nach README optimiert. Zahlen aus der Quelle
(EAG-Novelle 2026, Landesförderung versiegelte Flächen, VKW-Speicherförderung).
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
    "slug": "photovoltaik-foerderung-vorarlberg",
    "path": "/photovoltaik-foerderung-vorarlberg/",
    "title": "PV-Förderung Vorarlberg 2026: EAG, VKW, Gemeinden | EBZ",
    "description": ("PV-Förderung Vorarlberg 2026: EAG 150 €/kWp, VKW-Speicherbonus 50 €/kWh, bis 50.000 € "
                    "Landesförderung für PV auf versiegelten Flächen ab 20 kWp."),
    "eyebrow": "Förderung · Vorarlberg",
    "crumb_label": "PV-Förderung Vorarlberg 2026",
    "h1": "Photovoltaik-Förderung Vorarlberg 2026: EAG-Zuschuss bis 150 €/kWp, VKW-Speicherbonus und bis zu 50.000 € für PV auf versiegelten Flächen",
    "lead": ("Vorarlberg fördert 2026 keine klassischen Dach-PV-Anlagen für Privathaushalte, sondern setzt auf "
             "PV-Überdachungen versiegelter Flächen ab 20 kWp. Für Hausbesitzer bleiben die EAG-Bundesförderung, "
             "der VKW-Speicherbonus und Gemeindezuschüsse, in Summe typisch 2.500 bis 4.500 €*."),
    "chips": [
        "EAG: <b>150 €/kWp</b> bis 10 kWp",
        "VKW-Speicher: <b>50 €/kWh</b>, max. 500 €",
        "Land: <b>bis 50.000 €</b> ab 20 kWp auf versiegelten Flächen",
        "Typisch: <b>2.500 bis 4.500 €</b> für EFH*",
    ],
    "date_published": "2026-04-15",
    "date_modified": "2026-09-24",
    "hero_img": "gen_gewerbe",
    "hero_alt": "Photovoltaikanlage auf einem Gewerbedach mit Parkplatzfläche als Beispiel für PV auf versiegelten Flächen",

    "tldr": [
        "Vorarlberg zahlt 2026 keine Pauschalförderung pro kWp für Standard-Dachanlagen. Der Hauptzuschuss für "
        "Privathaushalte ist die EAG-Bundesförderung mit 150 €/kWp (bis 10 kWp) und 150 €/kWh Speicher.",
        "Die Landesförderung konzentriert sich auf PV auf versiegelten Flächen wie Carports und Parkplätzen: "
        "ab 20 kWp, bis 50.000 € pro Anlage, nicht auf bestehenden Gebäuden, mit EAG kombinierbar.",
        "Die VKW (Vorarlberger Kraftwerke) fördert Speicher mit 50 €/kWh bis maximal 500 €, Voraussetzung ist ein "
        "VKW-Einspeisevertrag. Mit der EAG ergibt das bis zu 200 €/kWh für die ersten kWh.",
        "Gemeindeförderungen sind in Vorarlberg der wichtigste Zusatzhebel, weil eine Landesförderung für "
        "Privathaushalte fehlt. Fragen Sie vor Projektstart beim Gemeindeamt nach.",
        "Realistische Gesamtförderung für eine 8-kWp-Anlage mit Speicher: 2.500 bis 4.500 €*. Der EAG-Antrag "
        "muss vor Inbetriebnahme im Fördercall gestellt werden.",
    ],
    "kpis": [
        ("150 €/kWp", "EAG-Zuschuss Kategorie A (bis 10 kWp)"),
        ("500 €", "maximaler VKW-Speicherbonus (50 €/kWh)"),
        ("50.000 €", "Landesförderung PV auf versiegelten Flächen"),
        ("20 kWp", "Mindestleistung für die Landesförderung"),
    ],

    "sections": [
        ("Die Photovoltaik-Förderung Vorarlberg 2026 im Überblick", "ueberblick", f"""
<p>Vorarlberg geht 2026 einen eigenen Weg. Während Kärnten oder Tirol Direktförderungen für Standard-PV-Anlagen
auf Hausdächern bieten, konzentriert sich das westlichste Bundesland auf PV-Überdachungen bereits versiegelter
Flächen: Carports, Parkplätze, befestigte Betriebsflächen. Eine Pauschalförderung pro Kilowattpeak für
Privathaushalte gibt es 2026 nicht.</p>
<p>Leer gehen Vorarlberger Hausbesitzer trotzdem nicht aus. Drei Schienen sind relevant:</p>
<ul>
  <li><b>EAG-Bundesförderung:</b> 120 bis 150 €/kWp plus 150 €/kWh Speicher plus Made-in-Europe-Bonus, der Hauptzuschuss für Privathaushalte</li>
  <li><b>Landesförderung versiegelte Flächen:</b> bis 50.000 € pro Anlage, nur ab 20 kWp und nicht auf Bestandsgebäuden</li>
  <li><b>VKW-Speicherförderung:</b> 50 €/kWh bis maximal 500 €, nur für VKW-Kunden mit Einspeisevertrag</li>
</ul>
<p>Für klassische Dachanlagen macht die EAG damit den mit Abstand größten Anteil der Gesamtförderung aus.
Die systematische Suche nach einer Gemeindeförderung ist in Vorarlberg 2026 deshalb wichtiger als in den
meisten anderen Bundesländern. Wie sich Vorarlberg im Vergleich schlägt, zeigt der
{a('/photovoltaik-landesfoerderungen/', 'Vergleich aller neun Landesförderungen')}.</p>
"""),
        ("EAG-Bundesförderung: der Hauptzuschuss für Vorarlberger Hausbesitzer", "eag", f"""
<p>Mit der EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026, kundgemacht am 16. Jänner 2026, sind die
Bundeskonditionen fixiert: 60 Millionen Euro stehen für PV- und Speicherprojekte bereit, abgewickelt über die
EAG-Förderabwicklungsstelle der OeMAG. Die Fördersätze sind nach Anlagengröße gestaffelt, Speicher werden mit
150 €/kWh bis maximal 50 kWh gefördert.</p>
{EAG_TABLE}
<h3>Made-in-Europe-Bonus</h3>
<p>Für Komponenten auf der White List der OeMAG gibt es jeweils 10 % Bonus pro Komponente (PV-Module,
Wechselrichter, Speicher): bis zu 20 % auf den PV-Zuschuss und weitere 10 % auf den Speicherzuschuss.</p>
<h3>Die drei EAG-Fördercalls 2026</h3>
{CALLS_TABLE}
<p>Die Antragstellung erfolgt online, in den Kategorien A und B nach dem First-come-first-served-Prinzip mit
Ticketziehung. Der Antrag muss vor Inbetriebnahme der Anlage gestellt werden. Alle Details im Ratgeber
{a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}.</p>
"""),
        ("Landesförderung Vorarlberg: PV auf versiegelten Flächen ab 20 kWp", "landesfoerderung", f"""
<p>Das Herzstück der Vorarlberger Landesförderung 2026 richtet sich an größere Projekte ab 20 kWp auf bereits
versiegelten Flächen: Carports, Parkplatzüberdachungen, befestigte Lagerflächen und ähnliche Konstruktionen.
Wer einen größeren Carport mit PV plant oder einen Firmenparkplatz überdachen will, kann hier bis zu
50.000 € pro Anlage erhalten.</p>
{A.table(
    ["Kriterium", "Konditionen 2026"],
    [
        ["Mindestleistung", "20 kWp"],
        ["Maximalförderung", "50.000 € pro Anlage"],
        ["Förderfähige Flächen", "Carports, Parkplätze, befestigte Betriebsflächen"],
        ["Nicht förderfähig", "Anlagen auf bestehenden Gebäuden"],
        ["Antragsberechtigt", "Unternehmen, Bauträger, Vereine, öffentliche Einrichtungen, Privatbauherren"],
        ["Kombination mit EAG", "ja, innerhalb der beihilferechtlichen Höchstgrenzen"],
    ],
    hl_cols=(1,),
)}
<p>Hintergrund ist der politische Wille des Landes, vorhandene Flächen optimal zu nutzen und die Versiegelung
von Grünflächen zu vermeiden. Die aktuellen Richtlinien veröffentlicht das Land Vorarlberg. Für Gewerbebetriebe
mit Parkflächen ist diese Schiene in Kombination mit der EAG-Kategorie C oder D besonders interessant, siehe
auch unser Ratgeber {a('/photovoltaik-carport/', 'Photovoltaik-Carport')}.</p>
"""),
        ("VKW-Speicherförderung: 50 €/kWh über den Energieversorger", "vkw-speicher", f"""
<p>Eine weitere Schiene trägt nicht das Land, sondern der regionale Energieversorger: Die VKW (Vorarlberger
Kraftwerke) unterstützen Stromspeicher in Kombination mit PV-Anlagen.</p>
<ul>
  <li><b>Förderhöhe:</b> 50 €/kWh, maximal 500 € pro Anlage</li>
  <li><b>Voraussetzung:</b> bestehender VKW-Einspeisevertrag, Speicher in Kombination mit einer PV-Anlage</li>
  <li><b>Antragstellung:</b> direkt über die VKW</li>
  <li><b>Kombination mit EAG:</b> ja, in Summe bis zu 200 €/kWh für die ersten kWh (150 € Bund plus 50 € VKW)</li>
</ul>
<p>Im Vergleich zu Tirol oder Burgenland (jeweils 100 €/kWh über das Land) fällt der VKW-Bonus mit 50 €/kWh
geringer aus, ist aber in vielen Fällen die einzige zusätzliche Speicherschiene neben dem Bund. Prüfen Sie
deshalb, ob Sie als VKW-Kunde infrage kommen. Aktuelle Konditionen direkt bei der VKW. Mehr zur Bundesschiene
im Ratgeber {a('/foerderung-fuer-pv-speicher/', 'Förderung für PV-Speicher')}.</p>
{A.cta("Speicher richtig dimensionieren, Förderung mitnehmen",
       "EBZ Energie plant PV und Speicher so, dass EAG-Zuschuss, Made-in-Europe-Bonus und VKW-Förderung "
       "zusammenpassen, mit Projektbericht, 3D-Belegplan und Statikreport.",
       secondary=("batteriespeicher", "Zum Batteriespeicher"))}
"""),
        ("Gemeindeförderungen: der wichtigste Zusatzhebel in Vorarlberg", "gemeinden", f"""
<p>Weil das Land keine direkte PV-Förderung für Privathaushalte mit Standard-Dachanlagen bietet, kommt den
Gemeinden eine besondere Rolle zu. Viele Vorarlberger Gemeinden haben eigene Programme, die sich in Höhe und
Ausgestaltung stark unterscheiden: pauschale Fixzuschüsse, Speicherboni oder prozentuale Beteiligungen an den
Investitionskosten. Manche setzen auf Speicher, andere auf E-Mobilität und Wallboxen, wieder andere auf reine
PV-Anlagen.</p>
<p>Da die Programme jährlich angepasst und nicht zentral kommuniziert werden, lohnt sich ein Anruf beim
Gemeindeamt oder ein Blick auf die Gemeinde-Website. Auch das Energieinstitut Vorarlberg berät. In den meisten
Fällen lassen sich Gemeindezuschüsse zusätzlich zur EAG-Bundesförderung und zur VKW-Speicherförderung
kombinieren, sofern die beihilferechtlichen Höchstgrenzen eingehalten werden.</p>
{A.box("Drei Fragen an Ihre Gemeinde: Gibt es 2026 eine PV- oder Speicherförderung? Wie hoch ist der Zuschuss "
       "und welche Voraussetzungen gelten? Ist die Kombination mit EAG und VKW möglich?", label="Tipp:")}
"""),
        ("Drei Szenarien: welche Förderkombination passt zu Ihrem Projekt?", "szenarien", f"""
{A.table(
    ["Szenario", "Zielgruppe", "Förderkombination", "Gesamtförderung*"],
    [
        ["Standard-Dach-PV (z. B. Einfamilienhaus)", "Privathaushalte", "EAG + Made-in-Europe-Bonus + VKW-Speicher + Gemeinde", "2.500 bis 4.500 €"],
        ["PV-Carport oder Parkplatz ab 20 kWp", "Unternehmen, Bauträger, Vereine, Private", "Landesförderung + EAG", "bis 50.000 € plus EAG"],
        ["Gewerbliche PV auf Bestandsgebäude", "KMU, Industrie", "EAG Kategorie C/D + Made-in-Europe-Bonus", "projektabhängig"],
    ],
    hl_cols=(3,),
)}
<h3>Szenario 1: Standard-Dachanlage</h3>
<p>Sie nutzen die EAG als Hauptzuschuss (1.500 € bei 10 kWp bis 2.800 € bei 20 kWp), holen mit gelisteten
Komponenten den Made-in-Europe-Bonus (10 % je Komponente), beantragen die VKW-Speicherförderung (50 €/kWh,
max. 500 €) und prüfen die Gemeindeförderung. Rechenbeispiel 8 kWp mit 8 kWh Speicher: 1.200 € PV plus 1.200 €
Speicher plus 360 € Bonus plus 400 € VKW ergeben rund 3.160 €*, mit Gemeindezuschuss entsprechend mehr.</p>
<h3>Szenario 2: PV-Carport oder Parkplatzüberdachung ab 20 kWp</h3>
<p>Landesförderung (max. 50.000 €) plus EAG-Bundesförderung. Je nach Projektgröße fällt die Gesamtförderung
deutlich höher aus, für gewerbliche Bauherren ist diese Schiene besonders attraktiv.</p>
<h3>Szenario 3: Gewerbliche Anlage auf bestehendem Gebäude</h3>
<p>Hier greifen EAG Kategorie C oder D (max. 130 bzw. 120 €/kWp im Bieterverfahren) plus Made-in-Europe-Bonus.
Eine Landesförderung ist nicht verfügbar, weil Anlagen auf bestehenden Gebäuden ausgeschlossen sind.</p>
<p><small>*Richtwerte auf Basis der Fördersätze 2026. Die tatsächliche Höhe hängt von Anlagengröße,
Speicherkapazität, Komponenten und der Wohnsitzgemeinde ab.</small></p>
"""),
        ("Voraussetzungen und Antragsablauf", "ablauf", f"""
<p>Für die drei Schienen gelten unterschiedliche Voraussetzungen:</p>
<ul>
  <li><b>EAG-Bundesförderung:</b> netzgekoppelte Anlage, Antrag vor Inbetriebnahme, alle Genehmigungen oder Anzeigen liegen bei Antragstellung vor, Anlage nach Stand der Technik</li>
  <li><b>Landesförderung versiegelte Flächen:</b> mindestens 20 kWp, Errichtung auf bereits versiegelter Fläche, keine Bestandsgebäude, max. 50.000 € pro Anlage</li>
  <li><b>VKW-Speicherförderung:</b> VKW-Einspeisevertrag, Speicher in Kombination mit PV, max. 500 €, Antrag direkt bei der VKW</li>
</ul>
{A.steps([
    ("Gemeinde und VKW-Status klären",
     "Vor der Planung: Gibt es eine Gemeindeförderung? Besteht ein VKW-Einspeisevertrag oder wird er abgeschlossen?"),
    ("Planung und Komponenten",
     "Anlagengröße, Speicher und Komponenten festlegen. Für den Made-in-Europe-Bonus müssen Module, Wechselrichter "
     "und Speicher auf der White List der OeMAG stehen."),
    ("Genehmigungen und Netzzugang",
     "Anzeigen oder Genehmigungen einholen, Zählpunkt und Netzzugang mit dem Netzbetreiber klären. Die Unterlagen "
     "müssen bei EAG-Antragstellung vorliegen."),
    ("EAG-Antrag im Fördercall",
     "Online über die EAG-Abwicklungsstelle, in Kategorie A und B mit Ticketziehung, zwingend vor Inbetriebnahme. "
     "Calls 2026: 23. April bis 11. Mai, 16. bis 30. Juni, ab 8. Oktober."),
    ("Landes- und VKW-Antrag",
     "Projekte ab 20 kWp auf versiegelten Flächen beim Land Vorarlberg einreichen, Speicherbonus direkt bei der VKW "
     "beantragen. Gemeindeförderung nach lokaler Richtlinie."),
    ("Inbetriebnahme und Endabrechnung",
     "Nach Inbetriebnahme Rechnungen und Nachweise einreichen, danach werden die Zuschüsse ausbezahlt."),
])}
{A.box_dark("Der häufigste Fehler",
    "Die Anlage geht in Betrieb, bevor der EAG-Antrag gestellt wurde. Dann ist der Bundeszuschuss weg, und "
    "in Vorarlberg gibt es für Standard-Dachanlagen keine Landesförderung als Ersatz.")}
"""),
        ("Photovoltaik und Wärmepumpe: die zweite Förderschiene", "waermepumpe", f"""
<p>Wer die PV-Anlage mit einer {a('waermepumpe', 'Wärmepumpe')} kombiniert, deckt Heizung und Warmwasser mit
eigenem Sonnenstrom und kann die Energiekosten um bis zu 85 % senken. Förderseitig laufen beide Systeme getrennt:
Für die PV-Anlage greift die EAG, für die Wärmepumpe die Sanierungsoffensive des Bundes. Gerade in Vorarlberg,
wo eine PV-Landesförderung für Privathaushalte fehlt, bringt die Wärmepumpen-Förderung zusätzliche Mittel ins
Gesamtprojekt.</p>
"""),
        ("Fazit: EAG als Basis, VKW und Gemeinde als Zusatz", "fazit", f"""
<p>Die Photovoltaik-Förderung in Vorarlberg 2026 ist anders strukturiert als in den meisten Bundesländern, bei
richtiger Strategie aber attraktiv: EAG-Bundesförderung als Hauptzuschuss, Made-in-Europe-Komponenten für den
Bonus, VKW-Speicherförderung und Gemeindezuschuss dazu. Für eine typische Privatanlage mit Speicher sind
2.500 bis 4.500 €* realistisch. Bauherren von Carports oder Parkplatzüberdachungen ab 20 kWp erreichen mit der
Landesförderung von bis zu 50.000 € plus EAG deutlich höhere Gesamtquoten.</p>
<p><small>Stand: Mai 2026. Förderhöhen, Budgets und Fristen können sich ändern, maßgeblich sind die Richtlinien
der EAG-Abwicklungsstelle (OeMAG), des Landes Vorarlberg und der VKW.</small></p>
{A.cta("Förderkombination für Ihr Projekt in Vorarlberg",
       "Wir prüfen EAG, VKW-Bonus, Gemeindeförderung und bei Flächenprojekten die Landesförderung und übernehmen "
       "die Antragstellung in der richtigen Reihenfolge.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("finanzierung", "Finanzierung ab 147 €/Monat"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Planung und Förderabwicklung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant Photovoltaikanlagen, Speicher und Wärmepumpen und hat über 300 Projekte "
                 "in sechs Bundesländern dokumentiert. Für Projekte in Vorarlberg übernehmen wir Beratung, Planung mit "
                 "Projektbericht (3D-Belegplan und Statikreport) und die Förderabwicklung aus einer Hand: EAG-Call, "
                 "VKW-Speicherbonus, Gemeindeförderung und bei Flächenprojekten die Landesförderung."),
        "grid": [
            ("Förderabwicklung komplett", "EAG, VKW, Gemeinde und Land in der richtigen Reihenfolge."),
            ("White-List-Komponenten", "Module, Wechselrichter und Speicher mit Made-in-Europe-Bonus."),
            ("Flächenprojekte ab 20 kWp", "Carport und Parkplatz mit Landesförderung bis 50.000 € planen."),
            ("Referenzen in 6 Bundesländern", "300+ Projekte, 4,9 Sterne auf Google."),
        ],
    },

    "faq": [
        ("Gibt es in Vorarlberg 2026 eine direkte PV-Förderung für Privathaushalte?",
         "Nein. Vorarlberg bietet 2026 keine Pauschalförderung pro Kilowattpeak für Standard-Dachanlagen. Der "
         "Schwerpunkt des Landes liegt auf PV auf versiegelten Flächen ab 20 kWp mit bis zu 50.000 € pro Anlage. "
         "Privathaushalte mit Dachanlagen nutzen die EAG-Bundesförderung mit 150 €/kWp bis 10 kWp."),
        ("Wie hoch ist die Vorarlberger Förderung für PV-Carports?",
         "Für PV-Anlagen auf versiegelten Flächen wie Carports oder Parkplätzen ab 20 kWp zahlt das Land bis zu "
         "50.000 € pro Anlage. Anlagen auf bestehenden Gebäuden sind ausgeschlossen. Die Förderung ist mit der EAG "
         "kombinierbar, sofern die beihilferechtlichen Höchstgrenzen eingehalten werden."),
        ("Was bietet die VKW-Speicherförderung?",
         "Die VKW fördern 2026 Speicher mit 50 €/kWh, gedeckelt bei 500 € pro Anlage. Voraussetzung sind ein "
         "VKW-Einspeisevertrag und der Betrieb in Kombination mit einer PV-Anlage. Zusammen mit der EAG-Speicherförderung "
         "von 150 €/kWh ergibt das bis zu 200 €/kWh für die ersten kWh."),
        ("Wie viel Förderung bekomme ich für eine 8-kWp-Anlage mit Speicher in Vorarlberg?",
         "8 kWp bringen 1.200 € EAG-Zuschuss, ein 8-kWh-Speicher 1.200 €, der Made-in-Europe-Bonus 360 € und der "
         "VKW-Bonus 400 €, in Summe rund 3.160 € (Richtwert). Mit Gemeindeförderung sind 2.500 bis 4.500 € typisch, "
         "je nach Anlagengröße und Wohnsitzgemeinde."),
        ("Kann ich EAG, VKW und Gemeindeförderung kombinieren?",
         "Ja. EAG-Bundesförderung, VKW-Speicherbonus und Gemeindezuschüsse lassen sich in den meisten Fällen "
         "kombinieren, sofern die beihilferechtlichen Höchstgrenzen eingehalten werden. Auch die Landesförderung für "
         "versiegelte Flächen ist mit der EAG kombinierbar."),
        ("Wann sind die EAG-Fördercalls 2026?",
         "Die drei Calls laufen vom 23. April bis 11. Mai, vom 16. bis 30. Juni und ab 8. Oktober 2026. In den "
         "Kategorien A und B gilt First come, first served mit Ticketziehung. Der Antrag muss vor Inbetriebnahme "
         "gestellt werden."),
        ("Lohnt sich eine PV-Anlage in Vorarlberg trotz fehlender Landesförderung?",
         "Ja. EAG-Zuschuss mit 150 €/kWp, Made-in-Europe-Bonus, VKW-Speicherbonus und mögliche Gemeindezuschüsse "
         "ergeben in Summe 2.500 bis 4.500 € für eine typische Privatanlage. Entscheidend für die Wirtschaftlichkeit "
         "ist ein hoher Eigenverbrauch, zum Beispiel mit Speicher und Wärmepumpe. Bei EBZ-Referenzprojekten liegt die "
         "Amortisation typisch bei 4 bis 6 Jahren."),
        ("Wer hilft bei der Förderabwicklung in Vorarlberg?",
         "EBZ Energie aus Villach übernimmt für Projekte in Vorarlberg Beratung, Planung und Förderabwicklung aus "
         "einer Hand, von der Komponentenwahl für den Made-in-Europe-Bonus über den EAG-Call bis zu VKW- und "
         "Gemeindeantrag. Referenzen liegen in sechs Bundesländern vor."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant PV-Anlagen, Speicher und "
                    "Wärmepumpen und übernimmt die Förderabwicklung, Referenzen liegen in sechs Bundesländern vor. "
                    "Die Angaben werden anhand der offiziellen Unterlagen von OeMAG, Land Vorarlberg und VKW geprüft. "
                    "Keine Rechts- oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("EAG-Förderabwicklungsstelle der OeMAG", "https://www.eag-abwicklungsstelle.at/"),
        ("White List der OeMAG (Made-in-Europe-Komponenten)", "https://www.oem-ag.at/"),
        ("Land Vorarlberg: Förderungen", "https://www.vorarlberg.at/"),
        ("VKW: Speicherförderung", "https://www.vkw.at/"),
        ("Energieinstitut Vorarlberg", "https://www.energieinstitut.at/"),
    ],
    "related": [
        ("/photovoltaik-landesfoerderungen/", "Vergleich: PV-Landesförderungen aller 9 Bundesländer"),
        ("/photovoltaik-foerderung-oesterreich-2026/", "Photovoltaik-Förderung Österreich 2026 (EAG)"),
        ("/foerderung-fuer-pv-speicher/", "Förderung für PV-Speicher"),
        ("batteriespeicher", "Batteriespeicher: Auslegung und Technik"),
    ],
    "cta": {
        "h3": "Förderung in Vorarlberg sichern",
        "text": "Wir kombinieren EAG, VKW-Bonus und Gemeindeförderung für Ihr Projekt und stellen die Anträge rechtzeitig.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre PV-Förderung in Vorarlberg, vollständig genutzt",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung und "
                   "Förderabwicklung aus einer Hand übernimmt."),
}
