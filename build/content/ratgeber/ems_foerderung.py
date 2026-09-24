"""Ratgeber: Energiemanagement-Förderung 2026 (Klima- und Energiefonds).

Migriert vom bestehenden HTML-Block auf ebz-photovoltaik.at/ems-foerderung/,
inhaltlich geprüft und optimiert (siehe Commit-Beschreibung).
Zahlen stammen aus dem Förderleitfaden des Klima- und Energiefonds (Quellen unten).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "ems-foerderung",
    "path": "/ems-foerderung/",
    "title": "EMS-Förderung 2026: bis 600 € vom Klimafonds | EBZ Energie",
    "description": "Energiemanagement-Förderung 2026: 50 % bis 600 € für Haushalte, 30 % bis 20.000 € für Betriebe. Voraussetzungen, Ablauf, Fristen und der häufigste Fehler.",
    "eyebrow": "Förderung · Energiemanagement",
    "crumb_label": "EMS-Förderung 2026",
    "h1": "Energiemanagement-Förderung 2026: Bis zu 600 Euro für die intelligente Vernetzung Ihrer Anlage",
    "lead": ("Der Klima- und Energiefonds fördert erstmals Energiemanagementsysteme für Haushalte und "
             "Betriebe. Wer PV-Anlage, Speicher, Wärmepumpe oder Wallbox vernetzt, bekommt bis zu "
             "50 Prozent der Kosten zurück."),
    "chips": [
        "Haushalte: <b>50 %</b>, max. 600 €",
        "Betriebe: <b>30 %</b>, max. 20.000 €",
        "Bonus: <b>100 €</b> Begleitforschung",
        "Frist: <b>15. April 2027</b>",
    ],
    "date_published": "2026-09-05",
    "date_modified": "2026-09-24",
    "hero_img": "ems",
    "hero_alt": "Energiemanagementsystem vernetzt Photovoltaik, Speicher, Wärmepumpe und Wallbox im Eigenheim",

    "tldr": [
        "Die Energiemanagement-Förderung 2026 des Klima- und Energiefonds unterstützt kommunikationsfähige, "
        "automatisierte Energiemanagementsysteme (EMS) mit insgesamt 4,9 Millionen Euro Budget.",
        "Private Haushalte erhalten 50 Prozent der förderfähigen Kosten, maximal 600 Euro, plus 100 Euro "
        "Bonus bei Teilnahme an der Begleitforschung. Betriebe, Gemeinden und Vereine bekommen bis zu "
        "30 Prozent, maximal 20.000 Euro pro Standort.",
        "Das EMS muss mindestens zwei Komponenten wie PV-Anlage, Speicher, Wärmepumpe oder Ladestelle aktiv "
        "steuern, Preissignale verarbeiten und lokal arbeiten. Reine Eigenverbrauchsoptimierung reicht nicht.",
        "Fünf Jahre Verpflichtung: Sie wählen eine von sechs Optionen, zum Beispiel einen dynamischen "
        "Stromtarif oder die Teilnahme an einer Energiegemeinschaft.",
        "Reihenfolge beachten: Haushalte registrieren sich online, bevor die erste Rechnung gelegt wird. "
        "Betriebe stellen den Antrag vor der ersten verbindlichen Bestellung. Frist: 15. April 2027, 12:00 Uhr.",
    ],
    "kpis": [
        ("4,9 Mio. €", "Gesamtbudget des Programms"),
        ("600 €", "maximal für private Haushalte"),
        ("20.000 €", "maximal je Betriebsstandort"),
        ("15.04.2027", "spätester Registrierungsschluss"),
    ],

    "sections": [
        ("Was ist die Energiemanagement-Förderung des Klimafonds?", "was-ist", f"""
<p>Die Energiemanagement-Förderung 2026 trägt offiziell den Titel „Energiemanagement, Flexibilisierung
im Verteilnetz“ und ist ein neues Programm des Klima- und Energiefonds der österreichischen
Bundesregierung. Gefördert werden Anschaffung, Installation und Konfiguration intelligenter
Energiemanagementsysteme in privaten Haushalten sowie in Betrieben, Gemeinden und Vereinen. Insgesamt
stehen bis zu 4,9 Millionen Euro bereit, aufgeteilt zu je 2,45 Millionen Euro auf die beiden
Zielgruppen. Die Abwicklung übernimmt die Kommunalkredit Public Consulting (KPC) auf der Plattform der
Umweltförderung. Einreichungen sind seit 23. Juni 2026 möglich, längstens bis 15. April 2027, 12:00 Uhr,
oder bis das Budget ausgeschöpft ist.</p>
<p>Der Hintergrund: Je mehr Photovoltaikanlagen, Speicher, Wärmepumpen und E-Autos ans Netz gehen,
desto wichtiger wird es, Erzeugung, Speicherung und Verbrauch aufeinander abzustimmen. Ein
{a('ems', 'Energiemanagementsystem')} nutzt Sonnenstrom dann, wenn er verfügbar ist, entlastet das
Stromnetz und senkt gleichzeitig Ihre Energiekosten. Genau diese netzdienliche Steuerung wird jetzt
finanziell belohnt.</p>
"""),
        ("Was wird gefördert?", "was-wird-gefoerdert", f"""
<p>Förderfähig sind kommunikationsfähige, automatisierte Energiemanagementsysteme, die mindestens zwei
Komponenten miteinander vernetzen und aktiv steuern. Infrage kommen laut Leitfaden PV-Anlage,
elektrischer Energiespeicher, Ladestelle für E-Autos sowie Wärmepumpe beziehungsweise elektrische
Warmwasserbereitung mit Warmwasserspeicher:</p>
{A.net([
    ("☀", "PV-Anlage", "erzeugt Sonnenstrom"),
    ("▮", "Batteriespeicher", "lädt nach Preis und Netzsituation"),
    ("♨", "Wärmepumpe", "heizt mit Sonnenstrom (auch Warmwasser mit Speicher)"),
    ("⌖", "Ladestelle", "lädt das E-Auto netzdienlich"),
], "Das Energiemanagementsystem ist die Schaltzentrale",
   "Mindestens zwei der vier Komponenten müssen vernetzt und aktiv gesteuert werden. Pflicht: aktive "
   "Steuerung, dynamische Tarife, Messung von Bezug und Einspeisung, Lastmanagement.")}
<h3>Technische Mindestanforderungen</h3>
<p>Damit ein System förderfähig ist, muss es laut Leitfaden vier Funktionen beherrschen: angeschlossene
Anlagen aktiv steuern (nicht nur visualisieren), zeitvariable oder dynamische Preissignale (Strompreise
und Netztarife) verarbeiten, Bezug und Einspeisung am Netzanschluss messen und Lastmanagement
unterstützen, also Leistungsvorgaben umsetzen. Ihr Fachbetrieb bestätigt die Erfüllung im
Abrechnungsformular.</p>
<p>Wichtig für die Systemwahl: Die Steuerungseinheit muss am Standort vorhanden sein und die Steuerung
lokal ausführen, auch ohne Internetverbindung. Cloud-Funktionen für Preisdaten, Prognosen oder
Fernwartung sind erlaubt, reine Cloud-Lösungen sind nicht förderfähig.</p>
{A.box("Eine reine Eigenverbrauchsoptimierung, wie sie viele Wechselrichter ohnehin mitbringen, reicht "
       "für diese Förderung nicht aus. Das System muss netzdienlich reagieren können, zum Beispiel den "
       "Speicher bei niedrigen Börsenpreisen laden oder die Wärmepumpe bei PV-Überschuss vorziehen.")}
<h3>Was zählt zu den förderfähigen Kosten?</h3>
<ul>
  <li><b>Förderfähig:</b> Steuerungseinheit (Software und gegebenenfalls Hardware, einmalige Anschaffung),
  Messtechnik, Kommunikations- und Steuerungstechnik (Gateways, Relais, Datenkabel) sowie Installation,
  Konfiguration und Inbetriebnahme durch den Fachbetrieb. Bei Betrieben zusätzlich Beratung, Planung und
  Standortanalyse.</li>
  <li><b>Nicht förderfähig:</b> die PV-Anlage, der Speicher oder die Wärmepumpe selbst, laufende Abo-
  und Softwarekosten, Material in Eigenleistung und alles, was vor der Registrierung verrechnet wurde.
  Bringt ein Wechselrichter oder Speicher bereits EMS-Funktionen mit, zählen nur die separat
  ausgewiesenen Mehrkosten.</li>
</ul>
"""),
        ("Fünf Jahre Verpflichtung: eine von sechs Optionen wählen", "verpflichtung", f"""
<p>Die Förderung ist an eine Bedingung geknüpft, die im Alltag wenig Aufwand bedeutet, aber bei der
Antragstellung angegeben werden muss: Für fünf Jahre ab Auszahlung betreiben Sie Ihr System auf Basis
einer der folgenden Optionen. Ein Wechsel zwischen den Optionen ist zulässig, muss aber gemeldet werden.</p>
<ol>
  <li><b>Dynamischer Einspeisevertrag</b> mit stündlicher oder viertelstündlicher Abrechnung</li>
  <li><b>Dynamischer Liefervertrag</b> (Stromtarif mit Börsenpreisen)</li>
  <li><b>Vertrag mit einem Flexibilitätsdienstleister</b> (Energielieferant, virtuelles Kraftwerk, Aggregator)</li>
  <li><b>Flexibler Netzzugang</b>, also eine Begrenzung der Einspeiseleistung nach Vorgabe des Netzbetreibers</li>
  <li><b>Regelbarer Netztarif</b> (voraussichtlich ab 1. Jänner 2027)</li>
  <li><b>Teilnahme an einer lokalen oder regionalen Energiegemeinschaft</b> mit dynamischer Einspeisung und Bezug</li>
</ol>
<p>Für viele Kunden von EBZ Energie ist Option 6 der einfachste Weg: Wer ohnehin einer
{a('eg', 'Energiegemeinschaft')} beitritt, erfüllt die Bedingung mit dem Beitritt. Option 2 ist der
zweite Klassiker, weil ein EMS mit dynamischem Tarif den größten Kostenhebel hat.</p>
"""),
        ("Förderhöhe im Überblick", "foerderhoehe", f"""
{A.table(
    ["Zielgruppe", "Förderquote", "Maximalbetrag", "Extras"],
    [
        ["Private Haushalte (Netzebene 7)", "50 % der förderfähigen Kosten inkl. USt.", "600 € pro Projekt",
         "+ 100 € Bonus, wenn das Projekt für die Begleitforschung ausgewählt wird; ein Antrag pro Person und Standort"],
        ["KMU, Gemeinden, Vereine (Netzebene 6 und 7)", "bis zu 30 % der Nettokosten", "20.000 € pro Standort",
         "Beratung, Planung und Standortanalyse förderfähig; + 1.000 € Bonus bei Begleitforschung; max. 5 Standorte je Unternehmen"],
        ["Großunternehmen", "bis zu 20 % der Nettokosten", "20.000 € pro Standort",
         "wie KMU; Erzeugung, Speicher und Ladeleistung am Standort unter 250 kW"],
    ],
    hl_cols=(1, 2),
)}
<p>Für ein typisches Einfamilienhaus mit EMS-Kosten zwischen 800 und 1.500 Euro* deckt der Zuschuss also
einen erheblichen Teil der Investition. Rechenbeispiel: Kostet das System 1.200 Euro, erhalten Sie
600 Euro zurück, mit Begleitforschung 700 Euro. Bei Betrieben mit größeren Lastmanagement-Projekten
wächst der Hebel entsprechend.</p>
<p>Nicht adressiert werden haushaltsübergreifende Systeme, etwa für Mehrparteienhäuser. Dafür plant der
Klimafonds für Herbst 2026 ein eigenes Programm. Auch Trägerorganisationen von Energiegemeinschaften
sind nicht Zielgruppe dieser Ausschreibung.</p>
<p><small>*Richtwerte für marktübliche Systeme inklusive Installation und Konfiguration. Der
tatsächliche Preis hängt von Hersteller, Anzahl der Komponenten und dem Aufwand vor Ort ab.</small></p>
"""),
        ("So läuft die Antragstellung ab", "ablauf", f"""
<p>Für private Haushalte erfolgt die Einreichung in einem zweistufigen Verfahren über die Online-Plattform
der Umweltförderung: erst registrieren, dann beantragen.</p>
{A.steps([
    ("Online registrieren",
     "Die Registrierung erfolgt ausschließlich online mit ID Austria oder Lichtbildausweis. Sie geben "
     "Standort, Zählpunktnummer und die zu steuernden Anlagen an. Damit sind die Fördermittel für Ihr "
     "Projekt reserviert. Möglich, solange Budget verfügbar ist, längstens bis 15. April 2027, 12:00 Uhr."),
    ("EMS installieren lassen",
     "Ab dem Registrierungsdatum haben Sie sechs Monate Zeit für Installation, Inbetriebnahme und "
     "Abrechnung durch den Fachbetrieb. Ist das nicht realistisch, rät der Leitfaden ausdrücklich davon "
     "ab, sich schon zu registrieren."),
    ("Antrag stellen",
     "Über den individuellen Link aus der Bestätigungs-Mail reichen Sie Rechnung, IBAN, die gewählte "
     "Option (siehe oben) und das Formular Förderungsabrechnung mit Bestätigung des Fachbetriebs ein. "
     "Das System muss zu diesem Zeitpunkt fertig installiert und abgerechnet sein."),
    ("Förderung erhalten",
     "Nach Prüfung und Freigabe durch die KPC wird der Zuschuss ausbezahlt. Die fünfjährige "
     "Verpflichtung beginnt mit der Auszahlung."),
])}
{A.box_dark("Der häufigste Fehler",
    "Die Registrierung muss <b>vor der Rechnungslegung</b> erfolgen. Werden Komponenten oder Leistungen "
    "bereits vor der Registrierung verrechnet, entfällt die Förderfähigkeit vollständig. Planen Sie die "
    "Registrierung daher gemeinsam mit Ihrem Fachbetrieb, bevor die erste Rechnung gestellt wird.")}
<h3>Anderer Ablauf für Betriebe, Gemeinden und Vereine</h3>
<p>Betriebe registrieren sich nicht, sondern stellen einen vollständigen Förderantrag mit Beschreibung der
Anlagen, Kostendarstellung und Angeboten. Entscheidend: Der Antrag muss bei der KPC einlangen, <b>bevor
die erste rechtsverbindliche Bestellung</b> erfolgt. Nur Planungsleistungen dürfen davor anfallen. Nach
Genehmigung erhalten Sie einen Förderungsvertrag, haben sechs Monate für die Umsetzung und weitere
drei Monate für die Endabrechnung (inklusive Standortanalyse und Abnahmeprotokoll des Fachbetriebs).</p>
{A.box("Wer als Betrieb zuerst bestellt und dann einreicht, geht leer aus. Holen Sie Angebote ein, "
       "reichen Sie ein, und bestellen Sie erst nach dem Einlangen des Antrags.", label="Für Betriebe:")}
{A.cta("EMS-Förderung sichern, bevor das Budget ausgeschöpft ist",
       "EBZ Energie plant Ihr komplettes Energiesystem aus einer Hand und übernimmt die Registrierung "
       "bei der Förderstelle: im richtigen Moment und in der richtigen Reihenfolge.",
       secondary=("ems", "Zum Energiemanagementsystem"))}
"""),
        ("Warum sich ein EMS gerade jetzt lohnt", "warum-jetzt", f"""
<p>Die Förderung kommt zum richtigen Zeitpunkt, denn gleich mehrere Entwicklungen machen intelligentes
Energiemanagement in den nächsten Jahren zum Standard:</p>
<ul>
  <li><b>Dynamische Stromtarife:</b> Immer mehr Anbieter rechnen stundengenau ab. Ein EMS verschiebt
  Verbrauch automatisch in günstige Stunden, etwa das Laden des Speichers oder des E-Autos.</li>
  <li><b>Regelbare Netztarife ab 2027:</b> Voraussichtlich ab 1. Jänner 2027 kommen in Österreich
  regelbare Netztarife, bei denen Lastspitzen stärker ins Gewicht fallen. Wer Lasten intelligent steuert,
  spart doppelt.</li>
  <li><b>Sinkende Einspeisetarife:</b> Der {a('marktpreis', 'OeMAG-Marktpreis')} lag im Juli 2026 bei
  6,146 Cent je Kilowattstunde. Je weniger die Einspeisung bringt, desto wertvoller wird jede selbst
  genutzte Kilowattstunde, gerade in Kombination mit Wärmepumpe und Wallbox.</li>
  <li><b>Energiegemeinschaften:</b> Ein EMS legt Ihren Verbrauch in die Stunden, in denen die
  {a('eg', 'Energiegemeinschaft')} Überschuss hat, und hebt so die Zuordnungsquote.</li>
</ul>
"""),
        ("Kombinierbarkeit mit anderen Förderungen", "kombinierbarkeit", f"""
<p>Hier ist der Leitfaden strenger, als viele annehmen: Für das Energiemanagementsystem selbst ist die
Kombination mit anderen Bundes-, Landes- oder Gemeindeförderungen <b>nicht möglich</b>. Sie können also
nicht dieselbe EMS-Rechnung bei zwei Stellen einreichen.</p>
<p>Unberührt bleiben die Förderungen für die Anlagen drumherum: PV-Anlage, Speicher oder Wärmepumpe
laufen über eigene Schienen, in Kärnten über die Landesförderung (siehe
{a('foerderung_kaernten', 'Photovoltaik-Förderung Kärnten')}), in der Steiermark über die dortige
Landesförderung (siehe {a('foerderung_steiermark', 'Photovoltaik-Förderung Steiermark')}). Wer eine neue
Anlage plant, kann das EMS förderfähig mitplanen, wenn zwei Regeln eingehalten werden: Die EMS-Kosten
stehen auf einer eigenen Rechnung oder als eigene Position, und bringt der Wechselrichter oder Speicher
bereits EMS-Komponenten mit, gelten nur die separat ausgewiesenen Mehrkosten als förderfähig. Genau
diese Trennung übernimmt EBZ Energie in der Angebotslegung.</p>
"""),
        ("Fazit: Kleine Förderung, großer Hebel", "fazit", f"""
<p>600 Euro klingen zunächst überschaubar. Der eigentliche Wert der Energiemanagement-Förderung 2026
liegt aber im Zeitpunkt: Wer sein Energiesystem jetzt intelligent vernetzt, ist für dynamische
Stromtarife und die neue Netztarifstruktur ab 2027 gerüstet und holt aus PV-Anlage, Speicher,
Wärmepumpe und Wallbox dauerhaft mehr heraus. Entscheidend ist die richtige Reihenfolge: erst
registrieren, dann installieren.</p>
{A.cta("Jetzt Förderung und Technik aus einer Hand",
       "Wir prüfen, welche Ihrer Komponenten sich förderfähig vernetzen lassen, und erledigen "
       "Registrierung, Nachweise und Endabrechnung für Sie.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("ems", "Mehr zum EMS erfahren"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für EMS und Förderung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und "
                 "Wallboxen in Kärnten und der Steiermark, mit einem festangestellten Team aus "
                 "zertifizierten Fachkräften. Das Energiemanagementsystem denken wir von Anfang an mit: "
                 "Wir setzen auf Systeme, die den Mindestfunktionsumfang des Klimafonds erfüllen, und "
                 "übernehmen die Förderabwicklung von der Registrierung bis zur Endabrechnung."),
        "grid": [
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EMS vom selben Team."),
            ("Förderfähige Technik", "Aktive Steuerung, dynamische Tarife, Messung von Bezug und Einspeisung."),
            ("Registrierung zum richtigen Zeitpunkt", "Wir melden an, bevor die erste Rechnung gestellt wird."),
            ("Auch für Bestandsanlagen", "Nachrüstung bestehender PV-Anlagen, Speicher und Wärmepumpen."),
        ],
    },

    "faq": [
        ("Wie hoch ist die EMS-Förderung für private Haushalte?",
         "Private Haushalte erhalten 50 Prozent der förderfähigen Kosten inklusive Umsatzsteuer, maximal "
         "600 Euro pro Projekt. Wird Ihr Projekt für die Begleitforschung des Klimafonds ausgewählt, kommen "
         "einmalig 100 Euro Bonus dazu, in Summe also bis zu 700 Euro."),
        ("Welche Geräte muss das Energiemanagementsystem steuern?",
         "Mindestens zwei Komponenten müssen vernetzt und aktiv gesteuert werden, zum Beispiel PV-Anlage und "
         "Batteriespeicher, PV-Anlage und Wärmepumpe oder Wärmepumpe und Wallbox. Das System muss außerdem "
         "dynamische Strompreise oder Netztarife verarbeiten, Netzbezug und Einspeisung messen und "
         "Lastmanagement unterstützen."),
        ("Reicht die Eigenverbrauchsoptimierung meines Wechselrichters?",
         "Nein. Eine reine Eigenverbrauchsoptimierung ist laut Förderleitfaden ausdrücklich nicht "
         "ausreichend. Das System muss Preissignale verarbeiten, Bezug und Einspeisung messen, Leistungsvorgaben "
         "umsetzen und lokal steuern. Reine Cloud-Lösungen sind ebenfalls nicht förderfähig."),
        ("Was bedeutet die fünfjährige Verpflichtung konkret?",
         "Für fünf Jahre ab Auszahlung betreiben Sie das System auf Basis einer von sechs Optionen: dynamischer "
         "Einspeise- oder Liefervertrag, Vertrag mit einem Flexibilitätsdienstleister, flexibler Netzzugang, "
         "regelbarer Netztarif (voraussichtlich ab 2027) oder Teilnahme an einer lokalen beziehungsweise "
         "regionalen Energiegemeinschaft. Ein Wechsel der Option ist erlaubt und muss gemeldet werden."),
        ("Kann ich die EMS-Förderung mit der PV-Förderung kombinieren?",
         "Für das Energiemanagementsystem selbst ist keine zweite Förderung möglich. PV-Anlage, Speicher oder "
         "Wärmepumpe können aber weiterhin über Bund oder Land gefördert werden. Voraussetzung: getrennte "
         "Rechnungen beziehungsweise eigene Positionen für das EMS; bei integrierten EMS-Komponenten zählen nur "
         "die ausgewiesenen Mehrkosten."),
        ("Kann ich zuerst kaufen und danach die Förderung beantragen?",
         "Nein, die Reihenfolge ist entscheidend: Die Online-Registrierung muss vor der Rechnungslegung "
         "erfolgen. Wurden Komponenten oder Leistungen bereits vorher verrechnet, entfällt die "
         "Förderfähigkeit. Nach der Registrierung bleiben sechs Monate Zeit für Installation, "
         "Inbetriebnahme und Antragstellung."),
        ("Wie lange kann ich die Förderung beantragen?",
         "Registrierungen sind laufend möglich, solange Budgetmittel verfügbar sind, längstens jedoch bis "
         "15. April 2027, 12:00 Uhr. Da das Budget mit 4,9 Millionen Euro begrenzt ist, empfiehlt sich eine "
         "frühzeitige Registrierung."),
        ("Gilt die Förderung auch für Bestandsanlagen?",
         "Ja. Gefördert wird das Energiemanagementsystem selbst, also Anschaffung, Installation und "
         "Konfiguration. Auch bestehende PV-Anlagen, Speicher oder Wärmepumpen können mit einem "
         "förderfähigen EMS nachgerüstet und vernetzt werden."),
        ("Können Betriebe und Gemeinden die Förderung auch nutzen?",
         "Ja. KMU, Gemeinden und Vereine erhalten bis zu 30 Prozent, Großunternehmen bis zu 20 Prozent der "
         "Nettokosten, jeweils maximal 20.000 Euro pro Standort und bis zu fünf Standorte je Unternehmen. "
         "Beratung, Planung und Standortanalyse sind förderfähig, bei Auswahl zur Begleitforschung gibt es "
         "1.000 Euro Bonus. Der Antrag muss vor der ersten verbindlichen Bestellung eingereicht werden."),
        ("Was kostet ein förderfähiges Energiemanagementsystem?",
         "Für ein Einfamilienhaus liegen marktübliche Systeme inklusive Installation und Konfiguration "
         "meist zwischen 800 und 1.500 Euro (Richtwert). Nach Abzug der Förderung bleiben damit oft nur "
         "wenige hundert Euro Eigenanteil. Der genaue Preis hängt von Hersteller, Komponentenzahl und "
         "Aufwand vor Ort ab."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "PV-Anlagen, Speicher, Wärmepumpen und Energiemanagementsysteme in Kärnten und der "
                    "Steiermark und übernimmt die komplette Förderabwicklung. Die Inhalte werden anhand der "
                    "offiziellen Unterlagen von Klima- und Energiefonds und Umweltförderung aktualisiert. "
                    "Keine Rechts- oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("Klima- und Energiefonds: Energiemanagement Haushalte 2026",
         "https://www.klimafonds.gv.at/foerderung/energiemanagement-haushalte-2026/"),
        ("Klima- und Energiefonds: Energiemanagement Betriebe 2026",
         "https://www.klimafonds.gv.at/foerderung/energiemanagement-betriebe-2026/"),
        ("Umweltförderung: Energiemanagement für Privatpersonen",
         "https://www.umweltfoerderung.at/privatpersonen/energiemanagement-fuer-privatpersonen"),
        ("Leitfaden für private Haushalte, Juni 2026 (PDF)",
         "https://www.klimafonds.gv.at/wp-content/uploads/2026/06/Leitfaden-Energiemanagement-Haushalte.pdf"),
        ("Leitfaden für Betriebe, Gemeinden und Vereine, Juni 2026 (PDF)",
         "https://www.klimafonds.gv.at/wp-content/uploads/2026/06/Leitfaden-Energiemanagement-Betriebe.pdf"),
    ],
    "related": [
        ("ems", "Energiemanagementsystem: Funktion und Nutzen"),
        ("foerderung_kaernten", "Photovoltaik-Förderung Kärnten"),
        ("foerderung_steiermark", "Photovoltaik-Förderung Steiermark"),
        ("eg", "Energiegemeinschaft: Überblick"),
    ],
    "cta": {
        "h3": "Förderung nicht verschenken",
        "text": "Wir registrieren Ihr EMS-Projekt zum richtigen Zeitpunkt und planen die Technik so, dass sie förderfähig ist.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihr Energiesystem, intelligent vernetzt",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
