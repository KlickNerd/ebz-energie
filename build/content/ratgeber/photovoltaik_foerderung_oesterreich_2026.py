"""Ratgeber: Photovoltaik-Förderung Österreich 2026 (Bundesförderung EAG + Überblick Länder).

Migriert von /photovoltaik-foerderung-oesterreich-2026/ (Dez. 2025). Die Fördersätze der
Quelle (160 €/kWp, Bonus bis 20 %) stammen aus der Zeit vor der EAG-Novelle; sie wurden
auf die mit 16. Jänner 2026 kundgemachten Werte (150/140/130/120 €/kWp, 10 % je Komponente)
angeglichen, damit der Artikel zu den Bundesland-Ratgebern und zum Landesförderungs-Überblick
passt. Details im Migrationsbericht.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "photovoltaik-foerderung-oesterreich-2026",
    "path": "/photovoltaik-foerderung-oesterreich-2026/",
    "title": "PV-Förderung Österreich 2026: EAG-Sätze und Calls | EBZ",
    "description": ("PV-Förderung Österreich 2026: 150 €/kWp und 150 €/kWh Speicher vom Bund, 10 % "
                    "Made-in-Europe-Bonus, Calls ab 23. April, 16. Juni, 8. Oktober. Alle 9 Länder."),
    "eyebrow": "Förderung · Österreich",
    "crumb_label": "PV-Förderung Österreich 2026",
    "h1": "Photovoltaik-Förderung Österreich 2026: 150 Euro je kWp, 150 Euro je kWh und drei Fördercalls",
    "lead": ("Der Nullsteuersatz ist Geschichte, dafür zahlt der Bund 2026 wieder Investitionszuschüsse: 150 Euro "
             "je kWp für Anlagen bis 10 kWp, 150 Euro je kWh Speicher und 10 Prozent Made-in-Europe-Bonus. "
             "Dieser Ratgeber erklärt Sätze, Termine, Ablauf und die Kombination mit den Landesförderungen."),
    "chips": [
        "PV bis 10 kWp: <b>150 €/kWp</b>",
        "Speicher: <b>150 €/kWh</b>, max. 50 kWh",
        "Made-in-Europe: <b>+10 %</b> je Komponente",
        "Calls: <b>23. April, 16. Juni, 8. Oktober</b>",
    ],
    "date_published": "2025-12-15",
    "date_modified": "2026-09-24",
    "hero_img": "foerderung",
    "hero_alt": "Euro-Scheine und Taschenrechner: Photovoltaik-Förderung in Österreich 2026 berechnen",

    "tldr": [
        "Seit 1. April 2025 gilt für PV-Anlagen wieder 20 Prozent Umsatzsteuer. Als Ausgleich läuft 2026 die "
        "EAG-Investitionsförderung mit 60 Millionen Euro Budget, fixiert durch die Verordnungsnovelle vom "
        "16. Jänner 2026.",
        "Fördersätze: 150 Euro je kWp bis 10 kWp (Kategorie A), 140 Euro je kWp bis 20 kWp (B), bis 130 Euro (C) "
        "und bis 120 Euro (D). Speicher: 150 Euro je kWh bis 50 kWh, nur mit PV-Neuerrichtung oder -Erweiterung "
        "und mindestens 0,5 kWh je kWp.",
        "Made-in-Europe-Bonus: je 10 Prozent Zuschlag auf den Zuschuss für Module, Wechselrichter und Speicher "
        "von der White List, also bis zu 20 Prozent für die PV-Anlage und 10 Prozent für den Speicher.",
        "Drei Fördercalls 2026: 23. April bis 11. Mai, 16. bis 30. Juni und ab 8. Oktober. In den Kategorien A "
        "und B gilt First-Come-First-Served mit Ticketziehung, der Antrag muss vor Inbetriebnahme gestellt werden.",
        "Rechenbeispiel 10 kWp mit 10 kWh: 3.000 Euro vom Bund plus rund 450 Euro Bonus. In Kärnten kommen 3.000 "
        "Euro Landespauschale dazu, in Summe rund 6.450 Euro.",
    ],
    "kpis": [
        ("150 €/kWp", "EAG-Bund bis 10 kWp"),
        ("150 €/kWh", "Speicher, bis 50 kWh"),
        ("60 Mio. €", "Bundesbudget 2026"),
        ("23.04.2026", "Start des ersten Fördercalls"),
    ],

    "sections": [
        ("Was sich 2026 ändert: Zuschuss statt Steuerbefreiung", "aenderungen", f"""
<p>2024 und bis Ende März 2025 war die Anschaffung einer PV-Anlage bis 35 kWp für Private umsatzsteuerfrei.
Dieser Nullsteuersatz ist mit 1. April 2025 ausgelaufen, seither gilt wieder der reguläre Satz von 20 Prozent
auf Komponenten und Montage. Die Photovoltaik-Förderung in Österreich funktioniert 2026 daher wieder über
den klassischen Weg: Sie zahlen den Angebotspreis, der Bund zahlt nach Inbetriebnahme einen
Investitionszuschuss zurück.</p>
<p>Das Rückgrat ist das Erneuerbaren-Ausbau-Gesetz (EAG). Die Konditionen für das Förderjahr wurden mit
der EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026 am 16. Jänner 2026 kundgemacht, das Budget
beträgt 60 Millionen Euro. Abgewickelt wird die Förderung von der EAG-Abwicklungsstelle bei der OeMAG,
online und mit Ticketsystem. Das Verfahren wirkt bürokratischer als der Nullsteuersatz, bietet aber
Planungssicherheit: Die Termine stehen fest, die Sätze sind fixiert, und die Förderung ist auf
systemdienliche Anlagen mit Speicher ausgerichtet.</p>
<p>Die wirtschaftliche Betrachtung verschiebt sich damit: Entscheidend ist 2026 die Gesamtrechnung aus
Investitionszuschuss, Eigenverbrauchsquote und Strompreis. Wer den eigenen Strom nutzt, statt ihn für rund
6 Cent einzuspeisen, spart 25 bis 35 Cent je Kilowattstunde Netzbezug und erhält obendrein den Zuschuss.</p>
"""),
        ("EAG-Bundesförderung 2026: Sätze und Kategorien", "eag-saetze", f"""
<p>Die Fördersätze sind nach Anlagengröße in vier Kategorien gestaffelt. Für private Dachanlagen sind die
Kategorien A und B relevant, Gewerbeanlagen fallen in C und D:</p>
{A.table(
    ["Kategorie", "Anlagengröße", "Fördersatz PV", "Speicher", "Vergabe"],
    [
        ["A", "bis 10 kWp", "150 €/kWp", "150 €/kWh, max. 50 kWh", "First-Come-First-Served, Ticket"],
        ["B", "über 10 bis 20 kWp", "140 €/kWp", "150 €/kWh, max. 50 kWh", "First-Come-First-Served, Ticket"],
        ["C", "über 20 bis 100 kWp", "max. 130 €/kWp", "150 €/kWh, max. 50 kWh", "Bieterverfahren"],
        ["D", "über 100 bis 1.000 kWp", "max. 120 €/kWp", "150 €/kWh, max. 50 kWh", "Bieterverfahren"],
    ],
    hl_cols=(2, 3),
)}
<p>Für den Speicher gelten zwei Bedingungen: Er wird nur gemeinsam mit einer PV-Neuerrichtung oder
-Erweiterung gefördert, und die Kapazität muss mindestens 0,5 kWh je kWp installierter PV-Leistung
betragen. Ein Speicher, der Jahre später nachgerüstet wird, erhält keinen EAG-Zuschuss, dafür gibt es in
einigen Bundesländern eigene Programme (siehe {a('/foerderung-fuer-pv-speicher/', 'Förderung für PV-Speicher')}).</p>
<p>Seit der EAG-Novelle 2026 ist die Kombination mit Landesförderungen für Anlagen bis 100 kWp
ausdrücklich erlaubt, sofern die beihilferechtlichen Höchstgrenzen eingehalten werden. Ob das jeweilige
Land zusätzlich zahlt, regelt aber dessen Richtlinie.</p>
"""),
        ("Made-in-Europe-Bonus: 10 Prozent je Komponente", "made-in-europe", f"""
<p>Der Bund honoriert europäische Wertschöpfung: Für PV-Module, Wechselrichter und Speicher, die auf der
White List der EAG-Abwicklungsstelle stehen, erhöht sich der jeweilige Zuschuss um 10 Prozent je
Komponente. Für die PV-Anlage sind damit bis zu 20 Prozent Bonus möglich (Module plus Wechselrichter),
für den Speicher weitere 10 Prozent.</p>
<p>Für Sie lohnt sich der Blick auf die Herkunft der Komponenten doppelt: Europäische Produkte bringen oft
längere Garantien, und die Entscheidung wird mit barem Geld honoriert. EBZ Energie berücksichtigt die
White List bereits bei der Angebotslegung, damit der Bonus im Antrag nicht verloren geht.</p>
"""),
        ("Die drei Fördercalls 2026: Termine und Ablauf", "foerdercalls", f"""
<p>Die Fördermittel werden nicht durchgehend, sondern in drei Antragsfenstern vergeben. Der erste Call ist
der volumenstärkste:</p>
{A.table(
    ["Fördercall", "Zeitraum", "Hinweis"],
    [
        ["1. Call", "23. April bis 11. Mai 2026", "größtes Budgetvolumen, Ticket am ersten Tag empfohlen"],
        ["2. Call", "16. bis 30. Juni 2026", "für Projekte, die im April noch nicht antragsreif waren"],
        ["3. Call", "ab 8. Oktober 2026", "Restbudget, Abschluss des Förderjahres"],
    ],
    hl_cols=(1,),
)}
<p>In den Kategorien A und B gilt First-Come-First-Served: Beim Start des Calls ziehen Sie online ein Ticket,
die Reihung erfolgt nach Eingang. Wer die Unterlagen und die Zählpunktnummer vorbereitet hat und am ersten
Tag einreicht, hat die besten Chancen. Ist das Budget eines Calls ausgeschöpft, werden auch fristgerechte
Anträge abgelehnt.</p>
{A.steps([
    ("Angebot und Zählpunkt vorbereiten",
     "Sie brauchen ein Angebot des Fachbetriebs und die Zählpunktnummer aus dem Netzzutrittsantrag beim "
     "Netzbetreiber. Beides sollte vor dem Call-Start vorliegen."),
    ("Ticket ziehen und Antrag stellen",
     "Am Starttag des Calls (23. April, 16. Juni oder 8. Oktober 2026) online bei der EAG-Abwicklungsstelle "
     "registrieren und den Antrag mit Anlagendaten, Speicherkapazität und Komponentenliste einreichen."),
    ("Anlage errichten",
     "Erst nach der Antragstellung darf die Anlage in Betrieb gehen. Die Montage kann vorbereitet werden, "
     "die Inbetriebnahme muss nach dem Antrag liegen."),
    ("Endabrechnung einreichen",
     "Nach Inbetriebnahme reichen Sie Rechnungen, Fertigstellungsmeldung des Netzbetreibers und die "
     "Nachweise für den Made-in-Europe-Bonus ein. Danach wird der Zuschuss ausbezahlt."),
])}
{A.box_dark("Der häufigste Fehler",
    "Der EAG-Antrag muss <b>vor der Inbetriebnahme</b> gestellt werden. Wer die Anlage zuerst in Betrieb nimmt "
    "und danach einreicht, geht beim Bund leer aus. Bei den Landesförderungen ist es oft umgekehrt: Kärnten "
    "zum Beispiel fördert erst nach Fertigstellung. EBZ Energie stimmt Montagetermin und Anträge so ab, dass "
    "beide Fristen passen.")}
"""),
        ("Rechenbeispiel: 10 kWp mit 10 kWh Speicher", "rechenbeispiel", f"""
<p>Für eine typische Einfamilienhaus-Anlage mit 10 kWp und 10 kWh Speicher, Richtpreis rund 15.000 bis
22.000 Euro vor Förderung, ergibt sich 2026 folgende Förderung:</p>
{A.table(
    ["Förderung", "Rechnung", "Betrag*"],
    [
        ["EAG-Bund, PV-Anlage (Kategorie A)", "10 kWp × 150 €", "1.500 €"],
        ["EAG-Bund, Speicher", "10 kWh × 150 €", "1.500 €"],
        ["Made-in-Europe-Bonus", "10 % auf Modul-, Wechselrichter- und Speicherzuschuss", "rund 450 €"],
        ["Zwischensumme Bund", "", "rund 3.450 €"],
        ["Landespauschale Kärnten", "PV ab 5 kWp mit Speicher ab 5 kWh, Landes-Call bis 30. Juni 2026", "3.000 €"],
        ["Summe in Kärnten", "", "rund 6.450 €"],
    ],
    hl_cols=(2,),
)}
<p>Dazu kommen je nach Wohnort 200 bis 1.000 Euro Gemeindeförderung. Bei 18.500 Euro Anlagenpreis bleiben in
Kärnten damit rund 12.000 Euro Investition. Mit hohem Eigenverbrauch amortisiert sich die Anlage in
EBZ-Projekten typischerweise in 4 bis 6 Jahren, die vollständige Rechnung finden Sie im Ratgeber
{a('/kosten-einer-solaranlage/', 'Kosten einer Solaranlage')}.</p>
<p><small>*Beispielkonditionen nach EAG-Investitionszuschüsseverordnung 2026 und Kärntner Landesrichtlinie,
Stand Juni 2026. Der Bonus setzt Komponenten von der White List voraus.</small></p>
{A.cta("Förderung sichern, bevor der Call-Topf leer ist",
       "Wir bereiten Angebot und Zählpunkt vor, ziehen am Starttag das Ticket und reichen die Endabrechnung "
       "ein. Sie müssen sich um nichts kümmern.",
       secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
        ("Föderalismus: So unterschiedlich fördern die Bundesländer", "bundeslaender", f"""
<p>Während der Bund überall gleich fördert, setzen die neun Länder 2026 eigene Akzente, von einer
Pauschale mit Speicherpflicht über Sanierungsprogramme bis zur kompletten Einstellung. Der Überblick mit
Link zum jeweiligen Detail-Ratgeber:</p>
{A.table(
    ["Bundesland", "Landesförderung 2026 (Kurzfassung)", "Mit Bund kombinierbar"],
    [
        [a('/photovoltaik-foerderung-kaernten/', 'Kärnten'), "3.000 € Pauschale für PV ab 5 kWp mit Speicher ab 5 kWh, Landes-Call 15. April bis 30. Juni 2026, Antrag nach Fertigstellung; Nachrüstung 1.000 €", "ja"],
        [a('/foerderung-photovoltaik-steiermark/', 'Steiermark'), "Sanierungsbonus bis 15 % im Sanierungskontext (1. April bis 15. Mai 2026), Ökofonds bis 30 % ab 20 kWp", "ja"],
        [a('/photovoltaik-foerderung-wien/', 'Wien'), "Stadtförderung ab 1. Mai 2026, Fokus auf Gründächer, Fassaden und Mehrparteienhäuser", "nein"],
        [a('/photovoltaik-foerderung-niederoesterreich/', 'Niederösterreich'), "über die Wohnbauförderung, Punktesystem", "ja"],
        [a('/photovoltaik-foerderung-oberoesterreich/', 'Oberösterreich'), "Speicher-Nachrüstung 150 €/kWh bis 2.250 € für Bestandsanlagen vor 1. Jänner 2026", "nein beim Speicher"],
        [a('/photovoltaik-foerderung-salzburg/', 'Salzburg'), "private PV-Landesförderung mit Jahresende 2025 eingestellt, nur EAG", "entfällt"],
        [a('/photovoltaik-foerderung-tirol/', 'Tirol'), "bis 125 €/kWp über die Wohnhaussanierung, Speicher 100 €/kWh bis 1.000 €", "ja"],
        [a('/photovoltaik-foerderung-vorarlberg/', 'Vorarlberg'), "Landesprogramm für PV und Speicher", "ja"],
        [a('/photovoltaik-foerderung-burgenland/', 'Burgenland'), "Speicher 100 €/kWh bis 2.000 €, Bund vor Land", "nur wenn EAG nicht möglich"],
    ],
)}
<p>Die Kombination ist also nicht überall erlaubt: Wien schließt sie aus, Oberösterreich beim Speicher, im
Burgenland gilt Bund vor Land. Den vollständigen Vergleich aller neun Regelwerke finden Sie im Ratgeber
{a('/photovoltaik-landesfoerderungen/', 'Photovoltaik-Landesförderungen: alle 9 Bundesländer')}.</p>
<p><small>Stand: Juni 2026. Maßgeblich sind die jeweils gültigen Landesrichtlinien.</small></p>
"""),
        ("Wirtschaftlichkeit 2026: Förderung plus Eigenverbrauch", "wirtschaftlichkeit", f"""
<p>Lohnt sich Photovoltaik, wenn die Einspeisevergütung sinkt und die Umsatzsteuer wieder gilt? Ja, aber
die Rechnung hat sich verschoben. Der Zuschuss dämpft die Anfangskosten, der eigentliche Hebel ist der
Eigenverbrauch: Netzstrom kostet 25 bis 35 Cent je Kilowattstunde inklusive Netzgebühren und Steuern, die
Gestehungskosten des eigenen Solarstroms liegen dank Förderung oft nur bei 6 bis 8 Cent. Der OeMAG-Marktpreis
für eingespeisten Strom lag im Juli 2026 bei 6,146 Cent, mehr dazu im Ratgeber
{a('/einspeisetarif-fuer-photovoltaik/', 'Einspeisetarif für Photovoltaik')}.</p>
<p>Genau deshalb fördert der Bund den Speicher mit 150 Euro je kWh: Er hebt den Eigenverbrauch von rund 30
auf 60 bis 80 Prozent und senkt die Stromrechnung um bis zu 85 Prozent. Dazu kommt die
Einkommensteuerbefreiung für Einspeiseerlöse bis 12.500 kWh pro Jahr bei Anlagen bis 35 kWp. Wer heute
investiert, friert seine Stromkosten für die nächsten 25 Jahre auf einem niedrigen Niveau ein und steigert
den Wert der Immobilie.</p>
{A.cta("Förderung und Anlage aus einer Hand",
       "Wir prüfen Bundes-, Landes- und Gemeindeförderung für Ihren Standort, wählen förderfähige Komponenten "
       "und halten alle Fristen ein.",
       primary=("kontakt", "Kostenlose Förderberatung"), secondary=("finanzierung", "Finanzierung ab 147 €/Monat"))}
"""),
        ("Fazit: Fristen kennen, Reihenfolge einhalten", "fazit", f"""
<p>Die Photovoltaik-Förderung in Österreich 2026 ist mit 150 Euro je kWp, 150 Euro je kWh Speicher und dem
Made-in-Europe-Bonus solide ausgestattet, in Kärnten kommt die höchste Landespauschale Österreichs dazu.
Entscheidend ist die Reihenfolge: Zählpunkt sichern, am Starttag des Calls (23. April, 16. Juni, 8. Oktober)
das Ticket ziehen, erst dann in Betrieb nehmen. Wer das einhält und die Anlage auf hohen Eigenverbrauch
plant, holt 3.000 bis 6.500 Euro Förderung und senkt seine Stromkosten dauerhaft.</p>
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Förderung und Photovoltaik: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und montiert Photovoltaikanlagen mit Speicher in Kärnten und der "
                 "Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften und über 300 "
                 "dokumentierten Projekten. Die Förderabwicklung ist Teil des Pakets: Netzzutritt, Ticketziehung "
                 "im EAG-Call, Landes- und Gemeindeanträge und die Endabrechnung."),
        "grid": [
            ("Fristen im Griff", "Zählpunkt und Angebot vor dem Call, Ticket am Starttag, Inbetriebnahme danach."),
            ("Förderfähige Technik", "Komponenten von der White List für den Made-in-Europe-Bonus, Speicher ab 0,5 kWh je kWp."),
            ("Land und Gemeinde", "Kärntner Pauschale, steirischer Sanierungsbonus und Gemeindeförderung geprüft."),
            ("Endabrechnung inklusive", "Rechnungen, Fertigstellungsmeldung und Nachweise reichen wir für Sie ein."),
        ],
    },

    "faq": [
        ("Wann startet der erste Fördercall 2026?",
         "Der erste und volumenstärkste EAG-Call läuft vom 23. April bis 11. Mai 2026, der zweite vom 16. bis "
         "30. Juni, der dritte ab 8. Oktober. Bereiten Sie Angebot und Zählpunktnummer vor, um am Starttag das "
         "Ticket zu ziehen. Wer den April verpasst, kann im Juni nachreichen, dann mit kleinerem Budget."),
        ("Gilt die 0 Prozent Umsatzsteuer für Photovoltaik noch?",
         "Nein. Der Nullsteuersatz für PV-Anlagen bis 35 kWp ist mit 1. April 2025 ausgelaufen, seither gilt "
         "wieder 20 Prozent auf Komponenten und Montage. Als Ausgleich wurde die EAG-Investitionsförderung 2026 "
         "wieder voll aktiviert: ein Zuschuss nach Inbetriebnahme statt einer Steuerbefreiung auf der Rechnung."),
        ("Wie hoch ist die Förderung für eine private PV-Anlage 2026?",
         "150 Euro je kWp bis 10 kWp (Kategorie A) und 140 Euro je kWp bis 20 kWp (Kategorie B), also 1.500 bis "
         "2.800 Euro. Dazu 150 Euro je kWh Speicher bis 50 kWh und 10 Prozent Made-in-Europe-Bonus je Komponente. "
         "Für 10 kWp mit 10 kWh ergibt das rund 3.450 Euro vom Bund."),
        ("Wie hoch ist die Förderung für einen Stromspeicher 2026?",
         "150 Euro je kWh nutzbarer Kapazität, maximal 50 kWh, plus 10 Prozent Made-in-Europe-Bonus. Voraussetzung: "
         "Der Speicher wird gemeinsam mit einer neuen oder erweiterten PV-Anlage errichtet und hat mindestens "
         "0,5 kWh je kWp PV-Leistung. In Kärnten gibt es zusätzlich 3.000 Euro Landespauschale, die einen Speicher "
         "ab 5 kWh voraussetzt."),
        ("Kann ich die Bundesförderung mit der Landesförderung kombinieren?",
         "In den meisten Bundesländern ja, etwa in Kärnten, der Steiermark, Niederösterreich, Tirol und "
         "Vorarlberg. Wien schließt die Kombination aus, Oberösterreich beim Speicher, im Burgenland gilt Bund vor "
         "Land. Seit der EAG-Novelle 2026 ist die Kombination bis 100 kWp bundesseitig erlaubt, maßgeblich ist die "
         "Landesrichtlinie."),
        ("Was bedeutet der Made-in-Europe-Bonus?",
         "Für Module, Wechselrichter und Speicher, die auf der White List der EAG-Abwicklungsstelle stehen, erhöht "
         "sich der jeweilige Zuschuss um 10 Prozent. Für die PV-Anlage sind so bis zu 20 Prozent Bonus möglich, "
         "für den Speicher weitere 10 Prozent. Bei 10 kWp mit 10 kWh sind das rund 450 Euro zusätzlich."),
        ("Was passiert, wenn das Budget eines Calls ausgeschöpft ist?",
         "Dann werden auch fristgerechte Anträge abgelehnt, in den Kategorien A und B entscheidet die Reihenfolge "
         "der Ticketziehung. Eine Antragstellung am ersten Tag des Calls erhöht die Chancen erheblich. Nicht "
         "berücksichtigte Projekte können im nächsten Call erneut einreichen."),
        ("Muss der Antrag wirklich vor der Inbetriebnahme gestellt werden?",
         "Ja. Der EAG-Antrag muss vor der Inbetriebnahme der Anlage im Fördercall eingereicht werden, sonst entfällt "
         "die Bundesförderung. Die Montage darf vorbereitet werden, die Inbetriebnahme muss nach dem Antrag liegen. "
         "Bei Landesförderungen wie in Kärnten ist es umgekehrt, dort wird nach Fertigstellung beantragt."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team hat über 300 PV-Projekte in "
                    "6 Bundesländern umgesetzt und wickelt Bundes-, Landes- und Gemeindeförderungen für Kunden in "
                    "Kärnten und der Steiermark ab. Die Werte in diesem Ratgeber werden nach den Veröffentlichungen "
                    "der EAG-Abwicklungsstelle aktualisiert. Keine Rechts- oder Steuerberatung, maßgeblich sind die "
                    "offiziellen Förderrichtlinien."),
    "sources": [
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("EAG-Abwicklungsstelle (OeMAG)", "https://www.eag-abwicklungsstelle.at/"),
        ("Förderportal des Landes Kärnten", "https://www.ktn.gv.at/"),
        ("Förderportal des Landes Steiermark", "https://www.steiermark.at/"),
    ],
    "related": [
        ("/photovoltaik-landesfoerderungen/", "PV-Landesförderungen: alle 9 Bundesländer"),
        ("/photovoltaik-foerderung-kaernten/", "Photovoltaik-Förderung Kärnten 2026"),
        ("/foerderung-photovoltaik-steiermark/", "Photovoltaik-Förderung Steiermark 2026"),
        ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage 2026"),
    ],
    "cta": {
        "h3": "Förderung nicht verschenken",
        "text": "Wir ziehen das Ticket am Starttag, wählen förderfähige Komponenten und reichen die Endabrechnung ein.",
        "primary": ("kontakt", "Kostenlose Förderberatung"),
    },
    "final_h2": "Ihre Förderung, richtig beantragt",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
