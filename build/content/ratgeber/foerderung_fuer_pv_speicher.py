"""Ratgeber: Förderung für PV-Speicher in Österreich (EAG-Bund plus Länder, Ablauf, Kombinierbarkeit).

Migriert von ebz-photovoltaik.at/foerderung-fuer-pv-speicher/ (Quelle Stand Juli 2025, Förderjahr 2025).
Die Konditionen 2026 (EAG-Novelle 2026, Landesprogramme) wurden aus den belegten Schwesterartikeln
ergänzt und als eigener Stand gekennzeichnet.
Stand ab 23.10.2026: letzter EAG-Call lief 8. bis 22.10.2026, derzeit kein Bundeszuschuss; Ausblick 2027
Systemfoerderung fuer Speicher laut BMWET (geplant, nicht beschlossen).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "foerderung-fuer-pv-speicher",
    "path": "/foerderung-fuer-pv-speicher/",
    "title": "Förderung für PV-Speicher: Bund beendet, Länder, 2027 | EBZ",
    "description": ("PV-Speicher-Förderung: Der Bundescall 2026 (150 € je kWh) endete am 22. Oktober. Kärnten "
                    "zahlt 3.000 €, Länder 100 bis 150 €/kWh, Systemförderung 2027 geplant."),
    "eyebrow": "Förderung · Speicher",
    "crumb_label": "Förderung für PV-Speicher",
    "h1": "Förderung für PV-Speicher in Österreich: Bundescall 2026 beendet, was die Länder zahlen und was 2027 geplant ist",
    "lead": ("Bund und Länder förderten Stromspeicher 2026 mit mehreren tausend Euro, aber nach unterschiedlichen "
             "Regeln. Der letzte EAG-Call lief vom 8. bis 22. Oktober 2026, derzeit gibt es keinen Bundeszuschuss. "
             "Dieser Ratgeber zeigt, was der Bund im Call 2026 zahlte, welche Bundesländer jetzt fördern und was "
             "laut BMWET für 2027 geplant ist."),
    "chips": [
        "EAG-Bund im Call 2026: <b>150 €/kWh</b>, max. 50 kWh",
        "Letzter Call: <b>8. bis 22. Oktober 2026</b>, beendet",
        "Kärnten: <b>3.000 €</b> Pauschale bis 31.12.2026",
        "2027: <b>Systemförderung</b> geplant",
    ],
    "date_published": "2025-07-05",
    "date_modified": "2026-10-21",
    "hero_img": "foerderung",
    "hero_alt": "Beratungsgespräch zum Förderantrag für Photovoltaik und Stromspeicher",

    "tldr": [
        "Im Call 2026 förderte der EAG-Investitionszuschuss des Bundes Stromspeicher mit 150 Euro je kWh, "
        "gedeckelt mit 30 Prozent der Investitionskosten und maximal 50 kWh, nur gemeinsam mit einer neuen oder "
        "erweiterten PV-Anlage und mit mindestens 0,5 kWh je kWp.",
        "Die Fördercalls 2026 liefen vom 23. April bis 11. Mai, 16. bis 30. Juni und 8. bis 22. Oktober, jeweils "
        "mit Antrag vor Inbetriebnahme. Der letzte endete am 22. Oktober 2026, im bisherigen System gibt es keinen "
        "weiteren Call; neue Speicher bekommen derzeit keinen Bundeszuschuss.",
        "Ab 2027 ist laut BMWET eine Systemförderung geplant, nicht beschlossen: Speicher mit intelligenter "
        "Steuerung, Antrag nach Installation und Rechnung, auch die Nachrüstung soll förderbar werden. Projekte ab "
        "1. November 2026 sollen beantragbar sein, die Höhe ist offen.",
        "Länder 2026: Kärnten 3.000 Euro Pauschale für PV mit Speicher und 1.000 Euro für die Nachrüstung, "
        "Oberösterreich 150 Euro je kWh Nachrüstung (bis 2.250 Euro), Burgenland und Tirol 100 Euro je kWh. "
        "Salzburg und Wien haben ihre privaten Programme mit Ende 2025 eingestellt.",
        "Wer jetzt plant, baut mit Speicher und Energiemanagement: Das wahrt die Chance auf die Systemförderung "
        "2027, und Kärnten zahlt die 3.000 Euro nur mit Speicher.",
    ],
    "kpis": [
        ("150 €/kWh", "EAG-Bundeszuschuss für Speicher im Call 2026, max. 50 kWh"),
        ("0,5 kWh je kWp", "Mindestgröße des Speichers für den EAG-Zuschuss 2026"),
        ("3.000 €", "Landespauschale Kärnten 2026 für PV mit Speicher"),
        ("22.10.2026", "Ende des letzten EAG-Fördercalls 2026"),
    ],

    "sections": [
        ("Die Bundesförderung: der EAG-Investitionszuschuss für Speicher", "eag-bund", f"""
<p>Das Herzstück der staatlichen Speicherförderung war 2026 der Investitionszuschuss aus dem
Erneuerbaren-Ausbau-Gesetz (EAG). Die Abwicklung übernahm die EAG-Abwicklungsstelle (OeMAG) in sogenannten
Fördercalls, also festgelegten Zeitfenstern mit eigenem Budget je Anlagenkategorie (A bis D). Der dritte und
letzte Call lief vom 8. bis 22. Oktober 2026; im bisherigen System gibt es keinen weiteren Call, neue Anlagen
bekommen derzeit keinen Bundeszuschuss. Welcher {a('batteriespeicher', 'PV-Speicher')}
förderfähig ist und wie EBZ Energie ihn auslegt, zeigt die Leistungsseite Batteriespeicher.</p>
<p>Für den Speicher gewährte der Bund im Call 2026 150 Euro je Kilowattstunde Nettospeicherkapazität,
zusätzlich zum Zuschuss für die PV-Module je kWp. Die Deckelung lag bei 30 Prozent der gesamten
Investitionskosten, gefördert wurden maximal 50 kWh. Drei Bedingungen entschieden über die Förderfähigkeit:</p>
<ul>
  <li><b>Antrag vor Inbetriebnahme:</b> Ein bereits laufendes System konnte nicht nachträglich gefördert werden.</li>
  <li><b>Kopplung an die PV-Anlage:</b> Der Speicher wurde nur gemeinsam mit einer neuen oder erweiterten
  PV-Anlage gefördert. Die reine Nachrüstung an einer Bestandsanlage war auf Bundesebene nicht förderfähig.</li>
  <li><b>Mindestgröße:</b> Die Nennkapazität musste mindestens 0,5 kWh je kWp der PV-Anlage betragen.</li>
</ul>
{A.table(
    ["Kategorie", "Anlagengröße", "Fördersatz PV im Call 2026", "Speicher im Call 2026"],
    [
        ["A", "bis 10 kWp", "150 €/kWp", "150 €/kWh, max. 50 kWh"],
        ["B", "über 10 bis 20 kWp", "140 €/kWp", "150 €/kWh, max. 50 kWh"],
        ["C", "über 20 bis 100 kWp", "max. 130 €/kWp", "150 €/kWh, max. 50 kWh"],
        ["D", "über 100 bis 1.000 kWp", "max. 120 €/kWp", "150 €/kWh, max. 50 kWh"],
    ],
    hl_cols=(3,),
)}
<p>Der <b>Made-in-Europe-Bonus</b> wurde mit dem zweiten Fördercall im Juni 2025 eingeführt: Für PV-Module,
Wechselrichter und Speicher von Herstellern auf der White List der Abwicklungsstelle gab es jeweils 10 Prozent
Zuschlag, also bis zu 20 Prozent für die PV-Anlage und weitere 10 Prozent für den Speicher.</p>
<p><b>Ausblick 2027:</b> Laut Eckpunkten des BMWET ist ab 2027 eine Systemförderung geplant, aber nicht
beschlossen: gefördert werden sollen Speicher mit intelligenter Steuerung, der Antrag soll nach Installation
und Rechnung kommen, ohne Call und Ticketziehung, auch die Nachrüstung von Speicher und Energiemanagement soll
förderbar werden. Projekte mit intelligentem Speicher, die ab 1. November 2026 in Betrieb gehen bzw. abgerechnet
werden, sollen 2027 beantragbar sein. Höhe und Kriterien sind offen.</p>
<p><small>Sätze: EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026, kundgemacht am 16. Jänner 2026, gültig
für die Calls 2026 (beendet). Im Förderjahr 2025 betrug der Satz in Kategorie A 160 Euro je kWp.</small></p>
"""),
        ("Rechenbeispiel: 10 kWp mit 10 kWh Speicher", "rechenbeispiel", f"""
<p>Im Call 2026 verdoppelte der Speicher die Bundesförderung annähernd. Bei einer 10-kWp-Anlage in Kategorie A
gab es 1.500 Euro für die Module (10 kWp mal 150 Euro) und zusätzlich 1.500 Euro für einen 10-kWh-Speicher
(10 kWh mal 150 Euro), zusammen 3.000 Euro vom Bund. Mit Made-in-Europe-Komponenten stieg der Betrag um bis zu
20 Prozent für die PV-Anlage und 10 Prozent für den Speicher. Derzeit ist der Bund nicht beantragbar, aktuell
bleibt in Kärnten die Landespauschale:</p>
{A.table(
    ["Position", "Bund (im Call 2026)", "plus Land Kärnten 2026", "Summe"],
    [
        ["PV-Anlage 10 kWp", "1.500 €", "3.000 € Pauschale (PV mit Speicher)", "4.500 €"],
        ["Speicher 10 kWh", "1.500 €", "in der Pauschale enthalten", "1.500 €"],
        ["Gesamt im Call 2026", "3.000 €", "3.000 €", "6.000 €"],
        ["Aktuell (Bund derzeit nicht beantragbar)", "0 €", "3.000 €", "3.000 €"],
    ],
    hl_cols=(3,),
)}
<p>Bei einem Richtpreis von 15.000 bis 22.000 Euro für 10 kWp mit Speicher vor Förderung reduzierte die
Kombination aus Bund und Land im Call 2026 die Investition damit um rund ein Drittel bis ein Viertel; mit der
Kärntner Pauschale allein sind es aktuell 3.000 Euro. Wie sich das auf
die Amortisation auswirkt, rechnet der Ratgeber
{a('/ab-wann-lohnt-sich-photovoltaik-mit-speicher/', 'Ab wann lohnt sich Photovoltaik mit Speicher?')} vor.</p>
"""),
        ("Die Bundesländer: wer 2026 zusätzlich fördert", "laender", f"""
<p>Während der EAG-Zuschuss 2026 in ganz Österreich gleich war, unterscheiden sich die Länder erheblich. Einige
legen eigene Speicherprogramme auf, andere verließen sich auf den Bund oder koppeln die Förderung an die
Wohnbau- oder Sanierungsförderung. Die Spalte zur Kombination beschreibt die Regeln für den Call 2026;
derzeit ist kein Bundeszuschuss beantragbar.</p>
{A.table(
    ["Bundesland", "Speicherförderung des Landes 2026", "Kombination mit EAG (Call 2026)"],
    [
        ["Kärnten", "3.000 € Pauschale für neue PV ab 5 kWp mit Speicher ab 5 kWh; 1.000 € für die Speicher-Nachrüstung; 2. Landes-Call 12. Oktober bis 31. Dezember 2026 (1. Call: 15. April bis 30. Juni)", "ja, ohne Anrechnung"],
        ["Oberösterreich", "Speicher-Nachrüstung: 150 €/kWh, max. 15 kWh, bis 2.250 €, nur für PV in Betrieb vor 1. Jänner 2026", "nein beim Speicher"],
        ["Burgenland", "100 €/kWh nutzbar, max. 20 kWh, max. 30 % der Kosten, bis 2.000 €", "nur, wenn der EAG-Zuschuss nicht möglich ist"],
        ["Tirol", "100 €/kWh, max. 10 kWh, bis 1.000 € (netzdienliche Speicher); PV über Wohnhaussanierung", "ja"],
        ["Vorarlberg", "VKW-Speicherbonus 50 €/kWh, max. 500 €; Land nur PV-Überdachungen ab 20 kWp", "ja"],
        ["Steiermark", "keine eigene Speicherprämie; Sanierungsbonus (max. 15 %, Fenster 1. April bis 15. Mai 2026) beendet, Ökofonds derzeit ohne PV-Ausschreibung", "entfällt, nur EAG"],
        ["Niederösterreich", "keine Direktförderung; PV und Speicher bringen Punkte in der Wohnbauförderung", "ja"],
        ["Salzburg", "Landesförderung für Private mit 31. Dezember 2025 ausgelaufen", "entfällt, nur EAG"],
        ["Wien", "Speicherförderung (max. 2.000 €) mit 31. Dezember 2025 ausgelaufen; neues Paket ab Mai 2026 nur für Fassaden- und Verschattungs-PV", "nein"],
    ],
    hl_cols=(1,),
)}
<p><small>Stand: Juni 2026. Maßgeblich sind die jeweils gültigen Richtlinien der Länder. Im Förderjahr 2025 galten
teils andere Konditionen: Kärnten zahlte 275 Euro je kWh Speicher (bis 10 kWh), Salzburg pauschal 1.000 Euro
für PV ab 5 kWp plus 1.000 Euro für Speicher ab 5 kWh, beides mit dem Bund kombinierbar.</small></p>
<p>Alle neun Länder mit Details vergleicht der Ratgeber
{a('/photovoltaik-landesfoerderungen/', 'PV-Landesförderungen aller Bundesländer')}. Für das Montagegebiet von
EBZ Energie: {a('/foerderung-pv-speicher-kaernten/', 'Förderung für PV-Speicher in Kärnten')} und
{a('foerderung_steiermark', 'Photovoltaik-Förderung Steiermark')}.</p>
{A.cta("Förderung für Ihren Speicher sichern",
       "Wir prüfen, welche Landesförderung für Ihren Standort gilt, planen den Speicher für die geplante "
       "Systemförderung 2027 und übernehmen Antrag und Endabrechnung.",
       secondary=("batteriespeicher", "Zum Batteriespeicher"))}
"""),
        ("Der Antrag Schritt für Schritt", "ablauf", f"""
<p>So lief der Weg zum EAG-Zuschuss im Call 2026. Derzeit ist kein Bundesantrag möglich; für die geplante
Systemförderung 2027 soll der Antrag laut BMWET erst nach Installation und Rechnung kommen (nicht
beschlossen). Fristen, technische Vorgaben und Formulare waren die Stolpersteine:</p>
{A.steps([
    ("Beratung und Planung",
     "Analyse von Dach, Stromverbrauch und Zielen. Daraus ergibt sich die Größe von PV-Anlage und Speicher "
     "(mindestens 0,5 kWh je kWp) und ein Angebot als Grundlage für den Antrag."),
    ("Vorbereitung auf den Fördercall",
     "Zählpunktnummer beim Netzbetreiber beantragen, Datenblätter und Angebot bereitlegen. Ohne Zählpunkt "
     "kein Antrag."),
    ("Ticketziehung und Antragstellung",
     "Am ersten Tag des Calls im Portal der EAG-Abwicklungsstelle Ticket ziehen; in den Kategorien A und B "
     "zählte die Reihenfolge des Eingangs. Danach den vollständigen Antrag bis Call-Ende einreichen."),
    ("Fördervertrag und Umsetzung",
     "Nach der Zusage Installation und Inbetriebnahme durch zertifizierte Fachkräfte. Parallel den "
     "Landesantrag stellen, wo eine Landesförderung besteht."),
    ("Endabrechnung und Auszahlung",
     "Rechnungen und Nachweise einreichen; der Zuschuss wurde nach Prüfung ausbezahlt."),
])}
{A.box_dark("Reihenfolge: 2026 und ab 2027 verschieden",
    "Im Call 2026 entfiel die Bundesförderung vollständig, wenn die Anlage vor dem EAG-Antrag in Betrieb ging. "
    "Für die geplante Systemförderung 2027 soll der Antrag laut BMWET nach Installation und Rechnung kommen "
    "(nicht beschlossen). Kärnten verlangt den Landesantrag schon jetzt erst nach Fertigstellung.")}
"""),
        ("Speicher nachrüsten: was 2026 gefördert wird", "nachruestung", f"""
<p>Für Herbst 2025 war eine EAG-Novelle angekündigt, die erstmals die alleinige Nachrüstung eines Speichers an
einer bestehenden PV-Anlage fördern sollte. Nach der EAG-Novelle 2026 galt weiterhin: Der Bundeszuschuss für
Speicher war an eine Neuerrichtung oder Erweiterung der PV-Anlage gebunden, der letzte Call dafür endete am
22. Oktober 2026. Ab 2027 soll die Nachrüstung laut BMWET im Rahmen der geplanten Systemförderung förderbar
werden (nicht beschlossen, Höhe offen). Die Nachrüstung fördern
stattdessen einzelne Länder: Kärnten mit 1.000 Euro Pauschale ab 5 kWh, Oberösterreich seit 1. März 2026 mit
150 Euro je kWh bis 2.250 Euro, Tirol mit 100 Euro je kWh bis 1.000 Euro und das Burgenland mit 100 Euro je
kWh bis 2.000 Euro. Technik, Kosten und Ablauf der Nachrüstung erklärt der Ratgeber
{a('/pv-speicher-nachruesten/', 'PV-Speicher nachrüsten')}.</p>
<p>Für die Planung heißt das: Wer jetzt plant, baut sinnvoll mit Speicher und Energiemanagement. Das wahrt die
Chance auf die Systemförderung 2027, und Kärnten zahlt die 3.000 Euro nur mit Speicher. Ist ein E-Auto oder
eine Wärmepumpe absehbar, lohnt es sich oft, den Speicher bei der Neuanlage gleich etwas größer auszulegen. Zur Steuerung von Speicher, Wärmepumpe und Wallbox gibt es 2026
zusätzlich die {a('/ems-foerderung/', 'Energiemanagement-Förderung des Klimafonds')} mit bis zu 600 Euro
für Haushalte.</p>
"""),
        ("Fazit: Förderung sichern, bevor die Anlage läuft", "fazit", f"""
<p>Bund und Länder machten den Speicher 2026 zur wirtschaftlich sinnvollsten Ergänzung jeder neuen PV-Anlage:
150 Euro je kWh vom Bund im Call 2026, dazu je nach Bundesland bis zu 3.000 Euro Pauschale oder 100 bis
150 Euro je kWh vom Land. Der Bundescall endete am 22. Oktober 2026, derzeit zahlt nur das Land. Ab 2027 ist
laut BMWET eine Systemförderung für Speicher mit intelligenter Steuerung geplant, nicht beschlossen. Wer jetzt
mit Speicher und Energiemanagement baut, den Landesantrag nach den jeweiligen Regeln stellt und Rechnungen
sauber trennt, verkürzt die Amortisation auf den EBZ-typischen Korridor von 4 bis 6 Jahren.</p>
{A.cta("Förderung und Technik aus einer Hand",
       "Kostenlose Erstberatung, Angebot nach den Förderrichtlinien und komplette Antragsabwicklung beim Land "
       "in Kärnten und der Steiermark, mit Blick auf die geplante Systemförderung 2027.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("photovoltaik", "Zur Photovoltaik"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für die Förderabwicklung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik mit Speicher in Kärnten und der "
                 "Steiermark, mit zertifizierten Fachkräften und über 300 "
                 "dokumentierten Projekten. Wir planen jede Anlage nach den technischen Förderrichtlinien, stellen "
                 "den Landesantrag in der richtigen Reihenfolge und behalten die geplante Systemförderung 2027 im Blick."),
        "grid": [
            ("Förderfähige Planung", "Speicher mit Energiemanagement, europäische Komponenten wo sinnvoll."),
            ("Land und Ausblick", "Kärntner Landesförderung jetzt, Kriterien der Systemförderung 2027 im Blick."),
            ("Fristen im Blick", "Landes-Call bis 31. Dezember 2026, Rechnungsdaten und Endabrechnung übernehmen wir."),
            ("Auch Nachrüstung", "Speicher für Bestandsanlagen inklusive Landesförderung, wo es sie gibt."),
        ],
    },

    "faq": [
        ("Gibt es derzeit eine Förderung für einen PV-Speicher vom Bund?",
         "Derzeit nicht. Im Call 2026 betrug der EAG-Investitionszuschuss 150 Euro je Kilowattstunde "
         "Nettospeicherkapazität, maximal 50 kWh und 30 Prozent der Investitionskosten, für 10 kWh also 1.500 "
         "Euro. Der letzte Call endete am 22. Oktober 2026. Ab 2027 ist laut BMWET eine Systemförderung für "
         "Speicher mit intelligenter Steuerung geplant, nicht beschlossen, die Höhe ist offen."),
        ("Kann ich die Förderung für eine bereits installierte Anlage beantragen?",
         "Beim Bund im Call 2026 nicht: Der EAG-Antrag musste vor der ersten Inbetriebnahme gestellt werden. Für "
         "die geplante Systemförderung 2027 soll der Antrag laut BMWET nach Installation kommen, für Projekte ab "
         "1. November 2026 (nicht beschlossen). Die meisten Landesprogramme verlangen den Antrag "
         "vor Baubeginn; Kärnten bildet mit dem Antrag nach Fertigstellung eine Ausnahme, verlangt aber "
         "Rechnungsdaten nach dem 1. Jänner 2026."),
        ("Wird die alleinige Nachrüstung eines Speichers gefördert?",
         "Vom Bund derzeit nicht: Der EAG-Zuschuss galt 2026 nur für Speicher mit einer neuen oder erweiterten "
         "PV-Anlage; ab 2027 soll die Nachrüstung laut BMWET förderbar werden (geplant). Länderprogramme für die Nachrüstung gibt es 2026 in Kärnten (1.000 Euro Pauschale), "
         "Oberösterreich (150 Euro je kWh, bis 2.250 Euro), Tirol (100 Euro je kWh, bis 1.000 Euro) und im "
         "Burgenland (100 Euro je kWh, bis 2.000 Euro)."),
        ("Konnte man Bundes- und Landesförderung kombinieren?",
         "Im Call 2026 hing das vom Bundesland ab. Kärnten erlaubte die Kombination ohne Anrechnung, Tirol und "
         "Vorarlberg ebenfalls. Oberösterreich schloss EAG-Speicherzuschuss und Landes-Speicherförderung "
         "gegenseitig aus, das Burgenland zahlte nur, wenn der EAG nicht möglich war, Wien schloss die "
         "Kombination aus. Derzeit ist kein Bundeszuschuss beantragbar."),
        ("Wann kann ich den EAG-Investitionszuschuss beantragen?",
         "Derzeit nicht. 2026 lief er in drei Fördercalls: 23. April bis 11. Mai, 16. bis 30. Juni und 8. bis "
         "22. Oktober, mit Ticketziehung und begrenzten Budgets. Im bisherigen System gibt es keinen weiteren Call. "
         "Ab 2027 soll der Antrag laut BMWET nach der Installation gestellt werden (Systemförderung, geplant, "
         "nicht beschlossen, Details offen)."),
        ("Was war der Made-in-Europe-Bonus?",
         "Ein Zuschlag von 10 Prozent je Komponente für PV-Module, Wechselrichter und Speicher von Herstellern auf "
         "der White List der EAG-Abwicklungsstelle, eingeführt mit dem zweiten Fördercall im Juni 2025. Für die "
         "PV-Anlage waren damit im Call 2026 bis zu 20 Prozent, für den Speicher 10 Prozent mehr Förderung möglich. "
         "Für 2027 ist laut BMWET wieder ein Europa-Bonus geplant."),
        ("Wie groß muss der Speicher für die Förderung mindestens sein?",
         "Im Call 2026 musste die Nennkapazität beim Bund mindestens 0,5 kWh je kWp betragen, bei 10 kWp also "
         "mindestens 5 kWh. Kärnten verlangt für die Landespauschale zusätzlich mindestens 5 kWh nutzbare Kapazität und "
         "mindestens 5 kWp PV-Leistung."),
        ("Was passiert mit Projekten, die im Call 2026 nicht zum Zug kamen?",
         "Einen nächsten Call gibt es im bisherigen System nicht, der letzte endete am 22. Oktober 2026. Projekte "
         "mit intelligentem Speicher, die ab 1. November 2026 in Betrieb gehen bzw. abgerechnet werden, sollen "
         "laut BMWET 2027 in der geplanten Systemförderung beantragbar sein (nicht beschlossen). In Kärnten bleibt "
         "die Landespauschale bis 31. Dezember 2026 beantragbar."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team hat über 300 PV-Projekte in sechs "
                    "Bundesländern umgesetzt und wickelt EAG- und Landesförderungen für seine Kunden ab. Die Inhalte "
                    "werden anhand der Richtlinien der EAG-Abwicklungsstelle und der Länder aktualisiert. Keine "
                    "Rechts- oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("EAG-Abwicklungsstelle (OeMAG)", "https://www.eag-abwicklungsstelle.at/"),
        ("Förderportal des Landes Kärnten", "https://www.ktn.gv.at/"),
        ("Land Oberösterreich: Nachrüstung von systemdienlichen Solarstromspeichern",
         "https://www.land-oberoesterreich.gv.at/554598.htm"),
        ("Land Tirol: Förderung von netzdienlichen Stromspeichersystemen",
         "https://www.tirol.gv.at/buergerservice/e-government/formulare/ansuchen-zur-foerderung-von-netzdienlichen-stromspeichersystemen/"),
        ("Land Burgenland", "https://www.burgenland.at/"),
        ("Klima- und Energiefonds", "https://www.klimafonds.gv.at/"),
    ],
    "related": [
        ("/foerderung-pv-speicher-kaernten/", "Förderung für PV-Speicher in Kärnten"),
        ("/photovoltaik-landesfoerderungen/", "PV-Landesförderungen: alle 9 Bundesländer"),
        ("/pv-speicher-nachruesten/", "PV-Speicher nachrüsten"),
        ("batteriespeicher", "Batteriespeicher: Technik und Auslegung"),
    ],
    "cta": {
        "h3": "Förderung nicht verschenken",
        "text": "Wir stellen den Landesantrag in der richtigen Reihenfolge und planen Speicher und Energiemanagement für die geplante Systemförderung 2027.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Speicher planen, Förderung sichern",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
