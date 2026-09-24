"""Ratgeber: Photovoltaik-Förderung Burgenland 2026.

Migriert von ebz-photovoltaik.at/photovoltaik-foerderung-burgenland/ (Stand Juni 2026),
inhaltlich bereinigt und auf die Ratgeber-Vorlage umgestellt.
Zahlen: EAG-Investitionszuschüsseverordnung 2026, Stromspeicher-Förderung Land Burgenland, Heizungstausch Burgenland.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "photovoltaik-foerderung-burgenland",
    "path": "/photovoltaik-foerderung-burgenland/",
    "title": "PV-Förderung Burgenland 2026: EAG + Speicherzuschuss | EBZ",
    "description": ("PV-Förderung Burgenland 2026: EAG-Bund 150 €/kWp, Speicher 100 €/kWh bis 2.000 €, Prinzip "
                    "Bund vor Land, Heizungstausch 3.500 €. Fristen und Ablauf."),
    "eyebrow": "Förderung · Burgenland",
    "crumb_label": "PV-Förderung Burgenland 2026",
    "h1": "Photovoltaik-Förderung Burgenland 2026: EAG-Zuschuss, bis zu 2.000 Euro Speicherförderung und das Prinzip Bund vor Land",
    "lead": ("Das Burgenland zahlt 2026 keine PV-Pauschale, fördert aber Stromspeicher mit 100 Euro je kWh bis "
             "2.000 Euro. Wichtigste Regel: Die EAG-Bundesförderung ist immer vorrangig zu beantragen, sonst "
             "verfällt der Anspruch auf die Landesförderung."),
    "chips": [
        "EAG-Bund: <b>150 €/kWp</b> bis 10 kWp",
        "Land-Speicher: <b>100 €/kWh</b>, max. 2.000 €",
        "Prinzip: <b>Bund vor Land</b>",
        "Landesantrag bis <b>6 Monate</b> nach Rechnung",
    ],
    "date_published": "2026-05-20",
    "date_modified": "2026-09-24",
    "hero_img": "gen_hero",
    "hero_alt": "Photovoltaikanlage auf einem Hausdach unter klarem Himmel, wie im sonnenreichen Burgenland",

    "tldr": [
        "Für die PV-Anlage selbst gibt es im Burgenland 2026 keine Landespauschale. Neue Anlagen laufen über die "
        "EAG-Bundesförderung: 150 Euro je kWp bis 10 kWp, 150 Euro je kWh Speicher, plus Made-in-Europe-Bonus.",
        "Das Land Burgenland fördert Stromspeicher mit 100 Euro je kWh nutzbarer Kapazität, maximal 20 kWh und "
        "30 Prozent der anrechenbaren Kosten, also bis zu 2.000 Euro. Antragsberechtigt sind Eigentümer privater "
        "Wohngebäude mit mehr als 50 Prozent Wohnfläche.",
        "Prinzip Bund vor Land: Die EAG-Förderung ist vorrangig zu beantragen. Wer keinen Bundesantrag stellt, "
        "obwohl er möglich wäre, verliert auch die Landesförderung.",
        "Stärkster Hebel der Landesförderung ist die Speicher-Nachrüstung an Bestandsanlagen, weil die "
        "EAG-Speicherförderung dort nicht greift. Der Landesantrag ist bis sechs Monate nach Rechnungsdatum "
        "möglich, der EAG-Antrag muss vor Inbetriebnahme gestellt werden.",
        "Heizungstausch: 30 Prozent bis 3.500 Euro vom Land plus 7.500 Euro (Wärmepumpe) bis 8.500 Euro (Biomasse) "
        "aus der Sanierungsoffensive des Bundes.",
    ],
    "kpis": [
        ("150 €/kWp", "EAG-Bundesförderung bis 10 kWp"),
        ("100 €/kWh", "Landes-Speicherförderung, max. 20 kWh"),
        ("2.000 €", "maximaler Landeszuschuss Speicher"),
        ("3.500 €", "Landesförderung Heizungstausch"),
    ],

    "sections": [
        ("Die Photovoltaik-Förderung Burgenland 2026 im Überblick", "ueberblick", f"""
<p>Das Burgenland zählt mit über 1.900 Sonnenstunden im Jahr zu den sonnenreichsten Regionen Österreichs.
Bei der Förderung geht das Land aber einen anderen Weg als Kärnten oder Tirol: Es gibt keine eigene
PV-Pauschale für Privathaushalte. Der Schwerpunkt der Landesförderung liegt auf Stromspeichern, ergänzt
um Gemeindeförderungen und eine Landesförderung für den Heizungstausch.</p>
{A.table(
    ["Förderschiene", "Für wen", "Förderhöhe 2026", "Hinweis"],
    [
        ["EAG-Investitionszuschuss (Bund)", "Neue PV-Anlage, mit oder ohne Speicher", "150 €/kWp (Kat. A) + 150 €/kWh Speicher + Made-in-Europe-Bonus", "vorrangig zu beantragen, Antrag vor Inbetriebnahme"],
        ["Stromspeicher-Förderung (Land)", "Eigentümer privater Wohngebäude (Wohnfläche über 50 %)", "100 €/kWh nutzbarer Kapazität, max. 20 kWh, max. 30 % der Kosten, bis 2.000 €", "greift, wenn die Bundesförderung nicht möglich ist; Antrag bis 6 Monate nach Rechnung"],
        ["Heizungstausch (Land)", "Tausch fossiler Heizungen gegen Wärmepumpe oder Biomasse", "30 % der förderfähigen Kosten, max. 3.500 €", "kombinierbar mit Sanierungsoffensive des Bundes"],
        ["Gemeindeförderung", "je nach Wohnsitzgemeinde", "Fixzuschuss, Speicherbonus oder Prozentanteil", "laufend, gemeindeabhängig"],
    ],
    hl_cols=(2,),
)}
<p>Wer im Burgenland reines PV-Geld will, stützt sich auf den Bund. Wer eine Bestandsanlage um einen
Speicher ergänzt, profitiert von der Landesförderung. Wer beide Ebenen und die Gemeinde geschickt
kombiniert, senkt die Investitionskosten deutlich.</p>
<p><small>Stand: Juni 2026. Maßgeblich sind die jeweils gültigen Richtlinien der EAG-Abwicklungsstelle und des
Landes Burgenland.</small></p>
"""),
        ("EAG-Bundesförderung 2026: der Hauptzuschuss im Burgenland", "eag", f"""
<p>Ohne Landespauschale ist der EAG-Investitionszuschuss der zentrale Förderhebel für burgenländische
Hausbesitzer. Die Konditionen wurden mit der EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026 am
16. Jänner 2026 fixiert. Insgesamt stehen rund 60 Millionen Euro Bundesmittel bereit.</p>
{A.table(
    ["Kategorie", "Anlagengröße", "Fördersatz PV", "Vergabe"],
    [
        ["A", "bis 10 kWp", "150 €/kWp", "First-Come-First-Served mit Ticket"],
        ["B", "über 10 bis 20 kWp", "140 €/kWp", "First-Come-First-Served mit Ticket"],
        ["C", "über 20 bis 100 kWp", "max. 130 €/kWp", "Bieterverfahren"],
        ["D", "über 100 bis 1.000 kWp", "max. 120 €/kWp", "Bieterverfahren"],
    ],
    hl_cols=(2,),
)}
<p>Stromspeicher fördert der Bund mit 150 Euro je kWh bis maximal 50 kWh, nur in Kombination mit einer
PV-Neuerrichtung oder -Erweiterung. Der Made-in-Europe-Bonus bringt jeweils 10 Prozent pro Komponente
(PV-Module, Wechselrichter, Speicher) von der White List der EAG-Abwicklungsstelle.</p>
<p>Die drei EAG-Fördercalls 2026 laufen vom 23. April bis 11. Mai, vom 16. bis 30. Juni sowie ab
8. Oktober. Der Antrag muss vor Inbetriebnahme online gestellt werden. Mehr dazu im Ratgeber
{a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}.</p>
"""),
        ("Burgenländische Stromspeicher-Förderung 2026 im Detail", "speicher", f"""
<p>Die Speicherförderung des Landes gilt sowohl für die Nachrüstung an bestehenden PV-Anlagen als auch
für die gleichzeitige Errichtung mit einer neuen Anlage. Wegen des Prinzips Bund vor Land (siehe unten)
kommt sie in der Praxis vor allem bei der Nachrüstung zum Tragen.</p>
{A.table(
    ["Kriterium", "Regelung Burgenland 2026"],
    [
        ["Förderhöhe", "100 € je kWh nutzbarer Speicherkapazität"],
        ["Obergrenzen", "max. 20 kWh (Bestand plus Erweiterung), max. 30 % der anrechenbaren Kosten, bis 2.000 €"],
        ["Antragsberechtigt", "Eigentümer privater Wohngebäude im Burgenland, Wohnfläche über 50 % des Gebäudes"],
        ["Nutzung", "überwiegend privat, Speicher dient überwiegend dem Eigenverbrauch, Betriebserlaubnis liegt vor"],
        ["Frist", "Antrag bis sechs Monate nach Rechnungsdatum, online über das Förderportal des Landes"],
        ["Ausschlüsse", "keine Förderung bei Umsatzsteuer-Befreiung nach § 28 Abs. 62 UStG; keine Barzahlung"],
        ["Vorrang", "Bundesförderungen und andere Landesförderungen sind vorrangig zu nutzen"],
    ],
    hl_cols=(1,),
)}
<p>Die Frist ist entspannter als beim Bund: Der Landesantrag kann bis zu sechs Monate nach dem
Rechnungsdatum gestellt werden, der EAG-Antrag dagegen zwingend vor Inbetriebnahme. Welche
Speichergröße zu Ihrer Anlage passt, erklärt die Leistungsseite {a('batteriespeicher', 'Batteriespeicher')}.</p>
"""),
        ("Bund vor Land: das wichtigste Prinzip im Burgenland", "bund-vor-land", f"""
<p>Die EAG-Bundesförderung ist im Burgenland immer vorrangig zu beanspruchen. Landesgeld fließt nur, wenn
die Bundesförderung für Ihr Projekt nicht möglich ist oder offiziell abgelehnt wurde. Auch andere
Bundesförderungen wie der Klima- und Energiefonds oder Investitionsprämien sind vorrangig zu nutzen.</p>
{A.box_dark("Anspruch verfällt",
    "Wer gar keinen Bundesantrag stellt, obwohl dieser möglich wäre, verliert auch die Landesförderung. "
    "Die burgenländische Speicherförderung ist als Sicherheitsnetz für Fälle gedacht, in denen der Bund "
    "nicht greift.")}
{A.table(
    ["Ihre Situation", "Richtige Förderschiene"],
    [
        ["Neue PV-Anlage 2026 mit Speicher", "EAG-Bundesförderung für PV und Speicher; Landesförderung in der Regel nicht zusätzlich"],
        ["Bestandsanlage, Speicher nachrüsten", "Burgenland-Speicherförderung (100 €/kWh, bis 2.000 €), weil die EAG bei reiner Nachrüstung nicht greift"],
        ["Bundesantrag möglich, aber nicht gestellt", "keine Landesförderung, Anspruch verfällt"],
    ],
    hl_cols=(1,),
)}
<p>Der wirtschaftliche Hebel der Landesförderung liegt damit in der Speicher-Nachrüstung von
Bestandsanlagen. Wer neu baut, beantragt die EAG für PV und Speicher und ergänzt um die Gemeinde.</p>
{A.cta("Neuanlage oder Nachrüstung? Wir rechnen beide Varianten",
       "EBZ Energie prüft, welche Schiene für Ihre Anlage greift, und plant die Anträge in der richtigen "
       "Reihenfolge.",
       secondary=("batteriespeicher", "Mehr zum Batteriespeicher"))}
"""),
        ("Antragstellung: Reihenfolge und Voraussetzungen", "antrag", f"""
<p>Die beiden Schienen haben unterschiedliche Zeitpunkte: EAG vor Inbetriebnahme, Landes-Speicherförderung
bis sechs Monate nach Rechnung. So läuft es ab:</p>
{A.steps([
    ("EAG-Antrag prüfen und stellen",
     "Für jede Neuanlage und jede Erweiterung am ersten Tag eines EAG-Calls (23. April, 16. Juni oder "
     "8. Oktober 2026) Ticket ziehen und den Antrag einreichen. Nur wenn die EAG nicht möglich ist, etwa bei "
     "reiner Speicher-Nachrüstung, kommt der Landesantrag ins Spiel."),
    ("Errichtung durch den Fachbetrieb",
     "Montage und Inbetriebnahme durch ein gewerblich befugtes Unternehmen. Alle Rechnungen per Überweisung "
     "bezahlen, Betriebserlaubnis dokumentieren."),
    ("Landesantrag innerhalb von sechs Monaten",
     "Speicher-Nachrüstung online über das Förderportal des Landes Burgenland beantragen: Rechnung, "
     "Zahlungsnachweis, Eigentumsnachweis, Nachweis der Wohnnutzung über 50 Prozent und gegebenenfalls "
     "Ablehnung des Bundes."),
    ("Gemeindeförderung einreichen",
     "Bei der Wohnsitzgemeinde nachfragen und den Gemeindeantrag stellen. Viele burgenländische Gemeinden "
     "zahlen zusätzlich zu Bund und Land."),
    ("Endabrechnung beim Bund",
     "Nach Inbetriebnahme Rechnungen, Zahlungsbelege und Fotos innerhalb der Frist bei der "
     "EAG-Abwicklungsstelle einreichen, dann wird der Zuschuss ausbezahlt."),
])}
<h3>Voraussetzungen im Überblick</h3>
<ul>
  <li><b>EAG-Bundesförderung:</b> netzgekoppelte Anlage, Eigentümer oder schriftliche Einwilligung,
  Elektroinstallation und Erdung am Stand der Technik, kein Baubeginn vor Antragstellung, Speicher nur mit
  Neuanlage oder Erweiterung.</li>
  <li><b>Landes-Speicherförderung:</b> Eigentümer eines privaten Wohngebäudes im Burgenland, Wohnfläche über
  50 Prozent, Speicher überwiegend für den Eigenverbrauch, Betriebserlaubnis, keine Umsatzsteuer-Befreiung nach
  § 28 Abs. 62 UStG, Bundes- und andere Landesförderungen vorrangig genutzt, keine Barzahlung.</li>
</ul>
"""),
        ("Heizungstausch-Förderung Burgenland: 3.500 Euro plus Bund", "heizung", f"""
<p>Wer neben der PV-Anlage auch die Heizung tauscht, profitiert im Burgenland doppelt. Das Land fördert
den Tausch fossiler Altanlagen (Öl, Gas, Kohle, Allesbrenner) gegen Wärmepumpe oder Biomasseanlage mit
30 Prozent der förderfähigen Kosten, gedeckelt bei 3.500 Euro. Diese Förderung ist mit der
Sanierungsoffensive des Bundes kombinierbar, die je nach System 7.500 Euro (Wärmepumpe) bis 8.500 Euro
(Biomasse) als Pauschale gewährt.</p>
{A.table(
    ["Beispiel: Öl auf Wärmepumpe, 30.000 € Projektkosten*", "Betrag"],
    [
        ["Sanierungsoffensive des Bundes (Pauschale Wärmepumpe)", "7.500 €"],
        ["Land Burgenland (30 %, gedeckelt)", "3.500 €"],
        ["<b>Gesamtförderung</b>", "<b>11.000 € (rund 37 %)</b>"],
    ],
    hl_cols=(1,),
)}
<p>Wer parallel eine PV-Anlage zur Versorgung der {a('waermepumpe', 'Wärmepumpe')} errichtet, kann
zusätzlich die EAG-Bundesförderung und gegebenenfalls die Speicherförderung des Landes nutzen. Nach
Erfahrungswerten von EBZ Energie sind in der Kombination aus PV und Wärmepumpe bis zu 85 Prozent
Ersparnis bei den Energiekosten möglich. Für die Steuerung beider Anlagen fördert der Klima- und
Energiefonds seit Juni 2026 Energiemanagementsysteme (siehe {a('/ems-foerderung/', 'EMS-Förderung 2026')}).</p>
<p><small>*Beispielkonditionen. Die tatsächliche Förderhöhe hängt von System, Kosten und den jeweils gültigen
Richtlinien ab.</small></p>
"""),
        ("Gemeindeförderungen im Burgenland", "gemeinde", f"""
<p>Viele burgenländische Gemeinden bieten eigene PV-Programme: pauschale Fixzuschüsse, Speicherboni oder
prozentuale Beteiligungen an den Investitionskosten. Weil sich diese Programme jährlich ändern und nicht
zentral veröffentlicht werden, lohnt sich ein Anruf bei der Wohnsitzgemeinde oder ein Blick auf deren
Website.</p>
<p>In vielen Fällen sind Gemeindeförderungen zusätzlich zu Bundes- und Landesförderung kombinierbar, sofern
die beihilferechtlichen Höchstgrenzen eingehalten werden. Gerade weil burgenländische Hausbesitzer wegen
des Prinzips Bund vor Land primär auf die EAG angewiesen sind, kann der Gemeindezuschuss den Unterschied
machen.</p>
"""),
        ("Fazit: Reihenfolge entscheidet", "fazit", f"""
<p>Die Photovoltaik-Förderung im Burgenland 2026 ist anders aufgebaut als in den meisten Bundesländern
(Vergleich: {a('/photovoltaik-landesfoerderungen/', 'PV-Landesförderungen aller neun Bundesländer')}).
Der Schlüssel ist die richtige Kombination: EAG-Bundesförderung für die Neuanlage, Landesförderung für die
Speicher-Nachrüstung, dazu die Gemeinde. Wer den Bundesantrag auslässt, verliert auch das Landesgeld.</p>
<p>Für eine typische Privatanlage mit PV und Speicher sind im Burgenland 2026 zwischen 2.500 und 4.500 Euro
Gesamtförderung realistisch, primär aus der EAG, ergänzt um Made-in-Europe-Bonus und Gemeindezuschuss.
Wer eine Bestandsanlage um einen Speicher ergänzt, erhält vom Land bis zu 2.000 Euro. Zum Vergleich: Der
Richtpreis für eine 10-kWp-Anlage mit Speicher liegt bei rund 15.000 bis 22.000 Euro vor Förderung.</p>
{A.cta("Jetzt Förderung und Technik aus einer Hand",
       "Wir prüfen Ihre Förderschiene, planen Speicher und Anlage förderfähig und stellen die Anträge in der "
       "richtigen Reihenfolge.",
       primary=("kontakt", "Kostenlose Beratung anfragen"), secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Förderung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie GmbH aus Villach plant und montiert Photovoltaikanlagen, Speicher und Wärmepumpen in "
                 "Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften und "
                 "über 300 dokumentierten Projekten in sechs Bundesländern. Wir übernehmen die komplette "
                 "Förderabwicklung von der Ticketziehung beim EAG-Call bis zur Endabrechnung bei Land und Gemeinde. "
                 "Für Projekte außerhalb unseres Montagegebiets sprechen Sie uns an, wir prüfen die Machbarkeit im "
                 "Einzelfall. Burgenländische Hausbesitzer finden die Landesförderung auch direkt über das "
                 "Förderportal des Landes Burgenland."),
        "grid": [
            ("Förderabwicklung komplett", "EAG-Ticket, Landesantrag, Gemeindeförderung und Endabrechnung."),
            ("PV und Wärmepumpe", "Beide Systeme geplant, montiert und gefördert aus einer Hand."),
            ("300+ Projekte", "Referenzen in sechs Bundesländern, typische Amortisation 4 bis 6 Jahre."),
            ("Finanzierung statt Warten", "Ab 147 € im Monat inklusive Speicher, die Anlage gehört ab Tag 1 Ihnen."),
        ],
    },

    "faq": [
        ("Gibt es im Burgenland 2026 eine direkte PV-Pauschalförderung?",
         "Nein. Das Burgenland zahlt 2026 keine eigene PV-Pauschale für Privathaushalte. Die Landesförderung "
         "konzentriert sich auf Stromspeicher mit 100 Euro je kWh bis maximal 20 kWh, also bis 2.000 Euro. Für die "
         "PV-Anlage selbst gilt die EAG-Bundesförderung mit 1.500 bis 2.800 Euro Direktzuschuss für Privatanlagen "
         "plus Made-in-Europe-Bonus."),
        ("Wie hoch ist die maximale Speicherförderung im Burgenland?",
         "100 Euro je Kilowattstunde nutzbarer Speicherkapazität, maximal 20 kWh und 30 Prozent der anrechenbaren "
         "Kosten, also bis zu 2.000 Euro. Voraussetzung ist, dass für denselben Speicher keine Bundesförderung in "
         "Anspruch genommen werden kann, weil die Bundesförderung vorrangig ist."),
        ("Was bedeutet das Prinzip Bund vor Land?",
         "Die EAG-Bundesförderung muss im Burgenland immer vorrangig beantragt werden. Wer keinen Bundesantrag "
         "stellt, obwohl dieser möglich wäre, verliert auch den Anspruch auf die Landesförderung. Die "
         "Speicherförderung des Landes greift als Sicherheitsnetz, etwa bei reiner Nachrüstung an Bestandsanlagen, "
         "wo die EAG nicht möglich ist."),
        ("Wann muss ich den Antrag im Burgenland 2026 stellen?",
         "Die EAG-Bundesförderung wird vor Inbetriebnahme beantragt, die drei Fördercalls 2026 starten am "
         "23. April, 16. Juni und 8. Oktober. Die Speicherförderung des Landes kann bis zu sechs Monate nach "
         "Rechnungsdatum eingereicht werden."),
        ("Kann ich für eine neue PV-Anlage mit Speicher beide Speicherförderungen bekommen?",
         "In der Regel nicht. Bei einer Neuanlage greift die EAG-Speicherförderung mit 150 Euro je kWh, und weil "
         "der Bund vorrangig ist, kommt die Landesförderung nicht zusätzlich zum Tragen. Die Landesförderung ist "
         "vor allem für die Speicher-Nachrüstung an Bestandsanlagen gedacht."),
        ("Wie hoch ist die Heizungstausch-Förderung im Burgenland?",
         "Das Land fördert den Tausch fossiler Heizungen gegen Wärmepumpe oder Biomasse mit 30 Prozent der "
         "förderfähigen Kosten, maximal 3.500 Euro. Zusammen mit der Sanierungsoffensive des Bundes (7.500 Euro "
         "Wärmepumpe, 8.500 Euro Biomasse) ergibt das bei 30.000 Euro Projektkosten 11.000 Euro oder rund "
         "37 Prozent."),
        ("Welche Voraussetzungen gelten für die Landes-Speicherförderung?",
         "Sie müssen Eigentümer eines privaten Wohngebäudes im Burgenland sein, die Wohnfläche muss über 50 Prozent "
         "ausmachen, der Speicher überwiegend dem Eigenverbrauch dienen und eine Betriebserlaubnis vorliegen. "
         "Ausgeschlossen sind Projekte mit Umsatzsteuer-Befreiung nach § 28 Abs. 62 UStG und Barzahlungen."),
        ("Wer hilft bei der Förderabwicklung im Burgenland?",
         "Burgenländische Hausbesitzer finden die Landesförderung über das Förderportal des Landes Burgenland. "
         "EBZ Energie mit Sitz in Villach montiert in Kärnten und der Steiermark und hat Referenzprojekte in sechs "
         "Bundesländern. Für Projekte außerhalb des Montagegebiets prüfen wir die Machbarkeit auf Anfrage."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und montiert PV-Anlagen, "
                    "Speicher und Wärmepumpen in Kärnten und der Steiermark und wickelt die Förderungen von Bund, "
                    "Land und Gemeinde für seine Kunden ab. Die Angaben werden anhand der offiziellen Richtlinien der "
                    "EAG-Abwicklungsstelle und des Landes Burgenland aktualisiert. Keine Rechts- oder Steuerberatung, "
                    "maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("Förderportal des Landes Burgenland: Energie",
         "https://www.burgenland.at/themen/bauen/wohnen/energie-neu/"),
    ],
    "related": [
        ("/photovoltaik-landesfoerderungen/", "PV-Landesförderungen: alle 9 Bundesländer"),
        ("/foerderung-fuer-pv-speicher/", "Förderung für PV-Speicher"),
        ("/photovoltaik-foerderung-niederoesterreich/", "Photovoltaik-Förderung Niederösterreich 2026"),
        ("waermepumpe", "Wärmepumpe mit Photovoltaik kombinieren"),
    ],
    "cta": {
        "h3": "Bund vor Land richtig nutzen",
        "text": "Wir prüfen EAG, Landes-Speicherförderung und Gemeinde und stellen die Anträge in der richtigen Reihenfolge.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre PV-Anlage, förderoptimiert geplant",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
