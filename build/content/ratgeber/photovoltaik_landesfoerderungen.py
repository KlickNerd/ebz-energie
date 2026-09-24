"""Ratgeber: Photovoltaik-Landesförderungen 2026, Vergleich aller neun Bundesländer.

Zusammengeführt aus zwei Duplikaten der alten Website:
ebz-photovoltaik.at/photovoltaik-landesfoerderungen/ (Stand Mai 2026) und
ebz-photovoltaik.at/photovoltaik-landesfoerderungen-in-oesterreich/ (Stand Juni 2026).
Je Bundesland wurde die jeweils aktuellere und vollständigere Angabe übernommen.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

KTN = "/photovoltaik-foerderung-kaernten/"
STMK = "foerderung_steiermark"
OOE = "/photovoltaik-foerderung-oberoesterreich/"
BGLD = "/photovoltaik-foerderung-burgenland/"
NOE = "/photovoltaik-foerderung-niederoesterreich/"
SBG = "/photovoltaik-foerderung-salzburg/"
TIR = "/photovoltaik-foerderung-tirol/"
VBG = "/photovoltaik-foerderung-vorarlberg/"
WIEN = "/photovoltaik-foerderung-wien/"

ARTICLE = {
    "slug": "photovoltaik-landesfoerderungen",
    "path": "/photovoltaik-landesfoerderungen/",
    "title": "PV-Landesförderungen 2026: 9 Bundesländer im Vergleich | EBZ",
    "description": ("PV-Landesförderungen 2026 im Vergleich: Kärnten 3.000 € Pauschale, Speicher 100 bis 150 €/kWh "
                    "in 3 Ländern, Sanierungsbonus Steiermark. Tabelle und Fristen."),
    "eyebrow": "Förderung · Österreich",
    "crumb_label": "PV-Landesförderungen 2026",
    "h1": "Photovoltaik-Landesförderungen 2026: Alle 9 Bundesländer im Vergleich, von 0 bis 3.000 Euro",
    "lead": ("Der EAG-Investitionszuschuss des Bundes ist in ganz Österreich gleich, die Landesförderung nicht: "
             "Kärnten zahlt 3.000 Euro Pauschale, Salzburg gar nichts mehr, Wien schließt die Kombination mit dem "
             "Bund aus. Diese Übersicht zeigt, was 2026 wo gilt und was sich kombinieren lässt."),
    "chips": [
        "Bund: <b>150 €/kWp</b> + 150 €/kWh, überall gleich",
        "Höchste Pauschale: <b>Kärnten 3.000 €</b>",
        "Speicher: <b>100 bis 150 €/kWh</b> in 3 Ländern",
        "Gemeinde: zusätzlich <b>200 bis 1.000 €</b>",
    ],
    "date_published": "2026-04-01",
    "date_modified": "2026-09-24",
    "hero_img": "foerderung",
    "hero_alt": "Förderunterlagen und Taschenrechner auf dem Tisch: Vergleich der Photovoltaik-Landesförderungen in Österreich",

    "tldr": [
        "Drei Säulen: Der EAG-Bundeszuschuss (150 Euro je kWp bis 10 kWp, 150 Euro je kWh Speicher, 60 Millionen "
        "Euro Budget) gilt überall gleich, die Landesförderung unterscheidet sich stark, die Gemeinde bringt "
        "je nach Wohnort 200 bis 1.000 Euro zusätzlich.",
        "Höchste Landespauschale: Kärnten mit 3.000 Euro für PV ab 5 kWp mit Speicher ab 5 kWh, voll mit dem Bund "
        "kombinierbar. Tirol fördert im Sanierungskontext bis 125 Euro je kWp.",
        "Speicher-Schienen: Burgenland 100 Euro je kWh (bis 2.000 Euro), Oberösterreich 150 Euro je kWh (bis "
        "2.250 Euro, nur Bestandsanlagen), Tirol 100 Euro je kWh (bis 1.000 Euro).",
        "Sanierungs- und Punktesysteme: Steiermark (Sanierungsbonus bis 15 Prozent, Ökofonds bis 30 Prozent) und "
        "Niederösterreich (Wohnbauförderung).",
        "Vorsicht bei der Kombination: Wien schließt sie aus, Oberösterreich beim Speicher, im Burgenland gilt "
        "Bund vor Land. Salzburg hat die private PV-Landesförderung mit Jahresende 2025 eingestellt.",
    ],
    "kpis": [
        ("3.000 €", "Landespauschale Kärnten, die höchste in Österreich"),
        ("150 €/kWp", "EAG-Bund bis 10 kWp, in allen Bundesländern"),
        ("9", "Bundesländer, 9 verschiedene Regelwerke"),
        ("2 von 9", "Ländern ohne Landesförderung für private Dachanlagen"),
    ],

    "sections": [
        ("Das Drei-Säulen-Modell der PV-Förderung in Österreich", "saeulen", f"""
<p>PV-Förderungen funktionieren in Österreich auf drei Ebenen, die eigene Programme, Töpfe und Regeln
haben und sich in vielen Fällen kombinieren lassen:</p>
{A.table(
    ["Säule", "Wer fördert", "Was 2026 gilt"],
    [
        ["1. Bund (EAG)", "EAG-Abwicklungsstelle (OeMAG)", "einheitlicher Investitionszuschuss in ganz Österreich, 60 Mio. € Budget, 1.500 bis 2.800 € je Privatanlage für die PV-Anlage"],
        ["2. Bundesland", "neun Landesregierungen", "von 3.000 € Pauschale (Kärnten) über Speicher- und Sanierungsprogramme bis zur kompletten Einstellung (Salzburg)"],
        ["3. Gemeinde", "Wohnsitzgemeinde", "oft übersehen, je nach Ort 200 bis 1.000 € zusätzlich, meist mit dem Bund kombinierbar"],
    ],
    hl_cols=(2,),
)}
<p>Seit der EAG-Novelle 2026 ist die Kombination von Bundes- und Landesförderung für Anlagen bis 100 kWp
(Kategorien A, B und C) ausdrücklich erlaubt, sofern die beihilferechtlichen Höchstgrenzen eingehalten
werden. Ob eine Landesförderung zusätzlich zum Bund fließt, entscheidet aber die jeweilige
Landesrichtlinie. Genau deshalb lohnt sich der Blick auf jedes einzelne Bundesland.</p>
<p><small>Stand: Juni 2026. Maßgeblich sind die jeweils gültigen Richtlinien der EAG-Abwicklungsstelle sowie der
Länder und Gemeinden.</small></p>
"""),
        ("EAG-Bundesförderung 2026: die Basis für ganz Österreich", "eag", f"""
<p>Der EAG-Investitionszuschuss gilt in allen neun Bundesländern gleich. Die Konditionen wurden mit der
EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026 am 16. Jänner 2026 fixiert.</p>
{A.table(
    ["Kategorie", "Anlagengröße", "Fördersatz PV", "Speicher"],
    [
        ["A", "bis 10 kWp", "150 €/kWp", "150 €/kWh, max. 50 kWh"],
        ["B", "über 10 bis 20 kWp", "140 €/kWp", "150 €/kWh, max. 50 kWh"],
        ["C", "über 20 bis 100 kWp", "max. 130 €/kWp", "150 €/kWh, max. 50 kWh"],
        ["D", "über 100 bis 1.000 kWp", "max. 120 €/kWp", "150 €/kWh, max. 50 kWh"],
    ],
    hl_cols=(2,),
)}
<p>Speicher werden nur in Kombination mit einer PV-Neuerrichtung oder -Erweiterung gefördert. Der
Made-in-Europe-Bonus bringt jeweils 10 Prozent pro Komponente (PV-Module, Wechselrichter, Speicher), also
bis zu 20 Prozent Zuschlag für die PV-Anlage und weitere 10 Prozent für den Speicher, sofern die
Komponenten auf der White List der EAG-Abwicklungsstelle stehen.</p>
<p>Die drei Fördercalls 2026: 23. April bis 11. Mai, 16. bis 30. Juni, ab 8. Oktober. In den Kategorien A und
B gilt First-Come-First-Served mit Ticketziehung, der Antrag muss vor Inbetriebnahme gestellt werden.
Alle Details im Ratgeber {a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}.</p>
"""),
        ("Übersichtstabelle: Alle 9 Bundesländer im Schnellvergleich", "vergleich", f"""
<p>Die Tabelle zeigt je Bundesland die wichtigste Landesförderung für Photovoltaik und Speicher 2026, ob
sie mit dem EAG-Bundeszuschuss kombinierbar ist und den Stand der Angaben.</p>
{A.table(
    ["Bundesland", "Förderart 2026", "Höhe und Eckdaten", "Mit EAG kombinierbar?", "Stand"],
    [
        ["Burgenland", "Speicherförderung des Landes, keine PV-Direktförderung für Private", "100 €/kWh nutzbar, max. 20 kWh, max. 30 % der Kosten, bis 2.000 €; Antrag bis 6 Monate nach Rechnung", "teilweise: Bund vor Land, Landesgeld nur wenn EAG nicht möglich", "Juni 2026"],
        ["Kärnten", "Pauschale für PV mit Speicher, Speicher-Nachrüstung, Gewerbeprogramm", "3.000 € (ab 5 kWp + 5 kWh), Nachrüstung 1.000 €, Gewerbe bis 200 €/kWp; Landes-Call 15. April bis 30. Juni 2026, Antrag nach Fertigstellung", "ja, ohne Anrechnung", "Juni 2026"],
        ["Niederösterreich", "Wohnbauförderung (Punktesystem), keine Direktförderung", "PV und Speicher bringen Punkte in der Eigenheimsanierung; Parkplatzüberdachungen: 2 Mio. €, max. 45 % der Mehrkosten, Stichtag 30. Juni 2026", "ja", "Juni 2026"],
        ["Oberösterreich", "Speicher-Nachrüstung für Bestandsanlagen, Dächer-Förderung", "150 €/kWh Nennkapazität, max. 15 kWh, max. 40 % der Kosten, bis 2.250 €; nur PV in Betrieb vor 1. Jänner 2026", "nein beim Speicher (EAG-Speicher und OÖ-Speicher schließen sich aus)", "Juni 2026"],
        ["Salzburg", "keine PV-Landesförderung für Private mehr", "Landesförderung mit 31. Dezember 2025 ausgelaufen, Stadt Salzburg mit 1. Jänner 2026 eingestellt; nur betriebliche PV (max. 40 %)", "entfällt, nur EAG", "Juni 2026"],
        ["Steiermark", "Steirischer Sanierungsbonus, Ökofonds ab 20 kWp", "Sanierungsbonus max. 15 % (1. April bis 15. Mai 2026, 9,8 Mio. €); Ökofonds bis 30 %, max. 250.000 €", "ja", "Mai 2026"],
        ["Tirol", "Wohnhaussanierung, Speicher-Nachrüstung", "PV 50 % der Kosten, max. 125 €/kWp (Kostenobergrenze 250 €/kWp); Speicher 100 €/kWh, max. 10 kWh, bis 1.000 €", "ja", "Juni 2026"],
        ["Vorarlberg", "nur PV-Überdachungen versiegelter Flächen ab 20 kWp; VKW-Speicherbonus", "Überdachungen max. 50.000 € je Anlage, Gebäude nicht förderfähig; VKW-Speicher 50 €/kWh, max. 500 €", "ja", "Juni 2026"],
        ["Wien", "neues Paket ab 1. Mai 2026 für Fassaden- und Verschattungs-PV", "7 Mio. € Budget; Standard-Dachanlagen auf Einfamilienhäusern nicht mehr gefördert; Sonnenstrom-Offensive (bis 500 €/kWp) und Speicherförderung (max. 2.000 €) mit 31. Dezember 2025 ausgelaufen", "nein, Stadt oder Bund", "Juni 2026"],
    ],
    hl_cols=(2,),
)}
<p>Von neun Bundesländern zahlen 2026 nur zwei eine Landesförderung für private Standard-Dachanlagen ohne
Sanierungsbezug: Kärnten mit der Pauschale und Tirol im Rahmen der Wohnhaussanierung. Drei Länder
(Burgenland, Oberösterreich, Tirol) fördern Speicher direkt, zwei (Salzburg, Wien) fördern private
Dachanlagen gar nicht mehr.</p>
"""),
        ("Alle Bundesländer im Detail", "details", f"""
<h3>Burgenland: Speicherförderung als zentraler Hebel</h3>
<p>Das Burgenland zahlt keine PV-Pauschale für Private, fördert aber Stromspeicher mit 100 Euro je kWh
nutzbarer Kapazität, maximal 20 kWh und 30 Prozent der Kosten, also bis 2.000 Euro. Antragsberechtigt sind
Eigentümer privater Wohngebäude mit mehr als 50 Prozent Wohnfläche, der Antrag ist bis sechs Monate nach
Rechnungsdatum möglich. Es gilt Bund vor Land: Wer den möglichen EAG-Antrag auslässt, verliert auch die
Landesförderung. Alle Details im Ratgeber {a(BGLD, 'Photovoltaik-Förderung Burgenland 2026')}.</p>

<h3>Kärnten: die 3.000-Euro-Pauschale</h3>
<p>Kärnten hat 2026 die höchste Landespauschale Österreichs: 3.000 Euro für neue private PV-Anlagen ab
5 kWp mit Speicher ab 5 kWh, unabhängig von der Anlagengröße, plus 1.000 Euro für die Speicher-Nachrüstung.
Reine PV-Anlagen ohne Speicher werden nicht mehr gefördert. Das Budget liegt bei rund 40 Millionen Euro,
der Landes-Call läuft vom 15. April bis 30. Juni 2026, der Antrag wird nach Fertigstellung gestellt. Die
Anrechnung der Bundesförderung entfällt: Für 8 kWp mit 8 kWh Speicher ergibt das 5.400 Euro aus Land und
Bund, mit Made-in-Europe-Bonus rund 5.700 bis 5.900 Euro. Betriebe erhalten bis 200 Euro je kWp. Alle Details
im Ratgeber {a(KTN, 'Photovoltaik-Förderung Kärnten 2026')}.</p>

<h3>Niederösterreich: Wohnbauförderung als Hebel</h3>
<p>Niederösterreich hat keine PV-Pauschale, fördert Photovoltaik aber über die Wohnbauförderung: In der
Eigenheimsanierung bringen PV-Anlage und Speicher Punkte, die die Förderhöhe erhöhen, auch die alleinige
Errichtung einer PV-Anlage ist förderfähig. Seit der Richtlinien-Novelle vom November 2025 zählen Speicher
auch im Einfamilienhaus. Das Modell gilt als Übergangslösung bis Ende 2026, ab 2027 soll ein neues
Zuschussmodell starten. Dazu kommt eine Schiene für PV-Parkplatzüberdachungen (2 Millionen Euro, max.
45 Prozent der Mehrkosten, Stichtag 30. Juni 2026) und eine ungewöhnlich hohe Zahl an Gemeindeförderungen,
von Auersthal über Hollabrunn und Klosterneuburg bis Mödling und Baden. Alle Details im Ratgeber
{a(NOE, 'Photovoltaik-Förderung Niederösterreich 2026')}.</p>

<h3>Oberösterreich: Speicher-Nachrüstung im Fokus</h3>
<p>Oberösterreich fördert keine PV-Anlagen pro kWp für Private, dafür seit 1. März 2026 die Nachrüstung
systemdienlicher Speicher an Bestandsanlagen: 150 Euro je kWh Nennkapazität, maximal 15 kWh und 40 Prozent
der Bruttokosten, bis 2.250 Euro. Die PV-Anlage muss vor dem 1. Jänner 2026 mit Netzzugangsvertrag in
Betrieb gegangen sein, Richtwert 1,5 kWh je kWp. Die OÖ-Speicherförderung ist nicht mit der
EAG-Speicherförderung kombinierbar. Zusätzlich fördert das Land Dächer-Prüfung und -Ertüchtigung. Alle
Details im Ratgeber {a(OOE, 'Photovoltaik-Förderung Oberösterreich 2026')}.</p>

<h3>Salzburg: der harte Schnitt zum Jahreswechsel</h3>
<p>Die Salzburger PV-Landesförderung, zuletzt bis 2.000 Euro für PV mit Speicher, ist mit 31. Dezember 2025
ersatzlos ausgelaufen, die Stadt Salzburg hat ihre Förderung mit 1. Jänner 2026 eingestellt. Das Land
fördert nur noch betriebliche PV-Anlagen mit maximal 40 Prozent der Kosten und verweist Private an die
EAG-Abwicklungsstelle. Private stützen sich damit auf den Bund (1.500 bis 2.800 Euro plus
Made-in-Europe-Bonus), im Sanierungskontext kann die Wohnbauförderung relevant sein. Alle Details im
Ratgeber {a(SBG, 'Photovoltaik-Förderung Salzburg 2026')}.</p>

<h3>Steiermark: Sanierungsbonus und Ökofonds</h3>
<p>Die Steiermark zahlt keine PV-Pauschale, hat aber mit dem Steirischen Sanierungsbonus 2026 einen
befristeten Call vom 1. April bis 15. Mai 2026 mit 9,8 Millionen Euro Budget: maximal 15 Prozent der Kosten
nach Ökopunkten, rückwirkend für umgesetzte Maßnahmen inklusive PV und Speicher, kombinierbar mit der
EAG. Für Anlagen ab 20 kWp mit Doppelnutzung gibt es den Ökofonds mit bis zu 30 Prozent (max.
250.000 Euro) und Boni von 50 beziehungsweise 125 Euro je kWp. Die Wohnbauförderung wird zum
„Sanierungspass“ reformiert, voraussichtlich ab Sommer 2026. Alle Details im Ratgeber
{a(STMK, 'Photovoltaik-Förderung Steiermark 2026')}.</p>

<h3>Tirol: Wohnhaussanierung und Speicher-Nachrüstung</h3>
<p>Tirol fördert PV im Rahmen der Wohnhaussanierung mit 50 Prozent der förderbaren Kosten, gedeckelt bei
125 Euro je kWp (Kostenobergrenze 250 Euro je kWp). Die Halbierung von 250 auf 125 Euro je kWp seit
1. Jänner 2026 begründet das Land mit gesunkenen Modulpreisen. Voraussetzung ist ein genehmigtes
Sanierungsvorhaben an einem bestehenden Wohngebäude. Dazu kommt eine Speicher-Nachrüstung mit 100 Euro je
kWh bis 10 kWh (max. 1.000 Euro, Inbetriebnahme ab 1. Jänner 2026, netzdienliche Steuerung) sowie regionale
Programme in Landeck, Lechtal-Reutte und Pitztal mit oft 20 bis 40 Prozent der Kosten. Land und Bund sind
kombinierbar. Alle Details im Ratgeber {a(TIR, 'Photovoltaik-Förderung Tirol 2026')}.</p>

<h3>Vorarlberg: Fokus auf versiegelte Flächen</h3>
<p>Vorarlberg fördert keine Dach-PV für Private, sondern PV-Überdachungen versiegelter Flächen (Carports,
Parkplätze) ab 20 kWp mit bis zu 50.000 Euro je Anlage. Anlagen auf bestehenden Gebäuden sind ausdrücklich
nicht förderfähig. Für Private bleibt der Speicherbonus der VKW (Vorarlberger Kraftwerke) mit 50 Euro je
kWh, maximal 500 Euro, bei bestehendem VKW-Einspeisevertrag, dazu Gemeindeprogramme. Die Dachanlage
selbst läuft über die EAG mit 150 Euro je kWp in Kategorie A. Alle Details im Ratgeber
{a(VBG, 'Photovoltaik-Förderung Vorarlberg 2026')}.</p>

<h3>Wien: Komplettumbau mit Fokus auf urbane Lösungen</h3>
<p>Die Wiener Sonnenstrom-Offensive (bis 500 Euro je kWp) und die Speicherförderung (max. 2.000 Euro) sind
mit 31. Dezember 2025 ausgelaufen. Standard-Dachanlagen auf Einfamilienhäusern fördert die Stadt nicht mehr.
Seit 1. Mai 2026 gibt es ein neues Paket mit 7 Millionen Euro für PV-Fassadenanlagen und
PV-Verschattungsanlagen auf begehbaren Dächern, weitergeführt werden Mehrgeschosswohnbau, Flugdächer und
Gründächer. Eine Kombination mit der EAG oder dem Klima- und Energiefonds ist nicht möglich, Antragsteller
entscheiden sich für Stadt oder Bund. Alle Details im Ratgeber {a(WIEN, 'Photovoltaik-Förderung Wien 2026')}.</p>
{A.cta("In Kärnten oder der Steiermark? Wir holen das Maximum heraus",
       "EBZ Energie kennt Landesrichtlinien, EAG-Termine und Gemeindeförderungen in beiden Bundesländern und "
       "übernimmt die komplette Abwicklung.",
       secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
        ("In welchen Bundesländern lohnt sich PV 2026 am meisten?", "lohnt", f"""
<p>Die Förderhöhe ist nicht das einzige Kriterium, auch Sonneneinstrahlung, Strompreis und
Verbrauchsprofil entscheiden über die Wirtschaftlichkeit. Aus den Förderlandschaften lassen sich aber klare
Tendenzen ableiten:</p>
<ul>
  <li><b>Kärnten</b> ist 2026 das attraktivste Bundesland für private PV-Investitionen: 3.000 Euro Pauschale,
  volle Kombinierbarkeit mit dem Bund und hohe Einstrahlung im Süden.</li>
  <li><b>Steiermark</b> punktet ohne Pauschale mit Sanierungsbonus, Ökofonds und vielen Gemeindeförderungen.</li>
  <li><b>Niederösterreich</b> lohnt sich vor allem für alle, die ohnehin sanieren oder neu bauen, weil PV in
  die Wohnbauförderung integriert wird.</li>
  <li><b>Tirol</b> hat die Sätze halbiert, bleibt im Sanierungskontext aber gut planbar.</li>
  <li><b>Burgenland und Oberösterreich</b> punkten mit der Speicher-Nachrüstung, ideal für Bestandsanlagen.</li>
  <li><b>Salzburg und Wien</b> sind die Bundesländer, in denen Privathaushalte 2026 fast ausschließlich auf
  die EAG-Bundesförderung angewiesen sind.</li>
</ul>
<p>Unabhängig vom Bundesland gilt: Der Richtpreis für eine 10-kWp-Anlage mit Speicher liegt bei rund 15.000
bis 22.000 Euro vor Förderung, die typische Amortisation bei 4 bis 6 Jahren. Was nach der Förderung bleibt,
lässt sich über eine {a('finanzierung', 'Finanzierung')} ab 147 Euro im Monat inklusive Speicher abbilden.</p>
"""),
        ("Strategie: die richtige Reihenfolge bei der Antragstellung", "strategie", f"""
<p>Egal in welchem Bundesland: Mit der richtigen Reihenfolge lässt sich die Gesamtförderung deutlich
erhöhen, mit der falschen verliert man eine Förderung komplett.</p>
{A.steps([
    ("Mit dem EAG-Bundeszuschuss beginnen",
     "Der EAG-Antrag muss vor Inbetriebnahme gestellt werden. Wer in den Kategorien A und B den besten "
     "Reihungsplatz will, zieht am Starttag des Calls (23. April, 16. Juni oder 8. Oktober 2026) punktgenau ein "
     "Ticket. Im Burgenland ist der Bundesantrag sogar Pflicht, sonst verfällt die Landesförderung."),
    ("Made-in-Europe-Bonus einplanen",
     "10 Prozent Zuschlag pro Komponente summieren sich auf über 20 Prozent Mehrförderung. Die Komponenten "
     "müssen auf der White List der EAG-Abwicklungsstelle stehen, das gehört in die Angebotsphase, nicht in die "
     "Endabrechnung."),
    ("Landesförderung nach Fertigstellung",
     "Die meisten Landesanträge werden nach Fertigstellung gestellt: Kärnten im Landes-Call bis 30. Juni 2026, "
     "Steiermark im Sanierungsbonus-Fenster, Burgenland bis sechs Monate nach Rechnung, Oberösterreich nach "
     "Umsetzung. Ausnahme Wien: Hier muss vorab entschieden werden, ob Stadt oder Bund."),
    ("Gemeindeförderung nicht vergessen",
     "Viele Gemeinden, besonders in Niederösterreich, der Steiermark und Kärnten, zahlen 200 bis 1.000 Euro "
     "zusätzlich. Ein Anruf beim Gemeindeamt oder ein Blick auf die Gemeinde-Website lohnt sich fast immer."),
    ("Ganzheitlich denken",
     "Wer ohnehin saniert, plant PV im Gesamtkonzept und öffnet damit Wohnbauförderung, Sanierungsbonus oder "
     "Öko-Sonderausgabenpauschale. Wer eine Wärmepumpe plant, erhält in vielen Bundesländern zusätzliche "
     "Förderungen für die Kombination. Für die Steuerung fördert der Klima- und Energiefonds seit Juni 2026 "
     "Energiemanagementsysteme."),
])}
{A.box_dark("Was passiert, wenn der Topf leer ist?",
    "Bei Ausschöpfung der Mittel werden auch fristgerechte Anträge abgelehnt, in den meisten Programmen gilt "
    "First-Come-First-Served. In Wien waren die Töpfe 2024 bereits im Juni leer, in Kärnten standen 2025 rund "
    "40 Millionen Euro für 13.000 Förderanträge bereit. Eine Antragstellung am ersten Tag des Calls erhöht "
    "die Chancen erheblich.")}
"""),
        ("Fazit: Die richtige Strategie ist alles", "fazit", f"""
<p>Die österreichische PV-Förderlandschaft 2026 ist so uneinheitlich wie nie: Wer in Kärnten wohnt und Land
und Bund kombiniert, bekommt mehrere tausend Euro, die es anderswo nicht gibt. Wer in Wien lebt, muss
zwischen Stadt und Bund wählen. Wer in Salzburg plant, ist fast vollständig auf die Bundesförderung
angewiesen.</p>
<p>Was alle Bundesländer eint: begrenzte Töpfe, kurze Fristen und formale Hürden. Die richtige Reihenfolge
bei der Antragstellung, die Komponentenauswahl für den Made-in-Europe-Bonus und die rechtzeitige
Vorbereitung der Unterlagen entscheiden über mehrere tausend Euro. Was der Bund bei Speichern zusätzlich
zahlt, steht im Ratgeber {a('/foerderung-fuer-pv-speicher/', 'Förderung für PV-Speicher')}.</p>
{A.cta("Förderung in Kärnten und der Steiermark aus einer Hand",
       "Wir planen Ihre Anlage förderfähig, ziehen das EAG-Ticket, stellen den Landesantrag und prüfen die "
       "Gemeindeförderung an Ihrem Wohnort.",
       primary=("kontakt", "Kostenlose Beratung anfragen"), secondary=("referenzen", "Referenzen ansehen"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Förderabwicklung in Kärnten und der Steiermark: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie GmbH aus Villach plant und montiert Photovoltaikanlagen, Speicher und Wärmepumpen in "
                 "Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften und "
                 "über 300 dokumentierten Projekten in sechs Bundesländern. Wir kennen die Kärntner "
                 "3.000-Euro-Pauschale, den Steirischen Sanierungsbonus, die EAG-Termine und die Gemeindeförderungen "
                 "beider Länder im Detail und übernehmen die komplette Abwicklung: von der strategischen "
                 "Förderkombination über die fristgerechte Ticketziehung beim EAG-Call bis zur Endabrechnung bei "
                 "Land und Gemeinde. Für Projekte außerhalb unseres Montagegebiets prüfen wir die Machbarkeit im "
                 "Einzelfall."),
        "grid": [
            ("Förderabwicklung komplett", "EAG-Ticket, Landesantrag, Gemeindeförderung und Endabrechnung."),
            ("Kärnten: 3.000 € Pauschale", "Wir planen ab 5 kWp mit 5 kWh Speicher, damit Land und Bund voll greifen."),
            ("Steiermark: Sanierungsbonus", "Antrag im Fenster 1. April bis 15. Mai, kombiniert mit EAG und Gemeinde."),
            ("300+ Projekte", "Referenzen in sechs Bundesländern, typische Amortisation 4 bis 6 Jahre."),
        ],
    },

    "faq": [
        ("Welches Bundesland hat 2026 die höchste PV-Landesförderung?",
         "Kärnten mit 3.000 Euro Pauschale für PV ab 5 kWp mit Speicher ab 5 kWh, voll mit dem Bund kombinierbar. "
         "Die Steiermark punktet mit dem Sanierungsbonus (bis 15 Prozent rückwirkend) und dem Ökofonds (bis "
         "30 Prozent ab 20 kWp). Tirol fördert über die Wohnhaussanierung bis 125 Euro je kWp. Salzburg und Wien "
         "haben keine vergleichbare Direktförderung für Standardanlagen."),
        ("Kann ich Bundes- und Landesförderung in jedem Bundesland kombinieren?",
         "Nein. In Kärnten, Niederösterreich, der Steiermark, Tirol und Vorarlberg ist die Kombination "
         "grundsätzlich möglich. Wien schließt die Kombination der Stadtförderung mit der EAG aus. In "
         "Oberösterreich sind Landes- und EAG-Speicherförderung nicht kombinierbar. Im Burgenland gilt Bund vor "
         "Land, die Landesförderung greift nur, wenn die EAG nicht möglich ist."),
        ("Bis wann muss ich meinen Antrag 2026 stellen?",
         "Der EAG-Bundeszuschuss läuft in drei Calls: 23. April bis 11. Mai, 16. bis 30. Juni und ab 8. Oktober "
         "2026, jeweils vor Inbetriebnahme. Die Kärntner Landesförderung ist bis 30. Juni 2026 möglich, der "
         "Steirische Sanierungsbonus vom 1. April bis 15. Mai 2026, die Wiener Stadtförderung startet am 1. Mai "
         "2026. Im Burgenland gilt für den Speicher eine Frist von sechs Monaten nach Rechnung."),
        ("Welche Bundesländer fördern Stromspeicher direkt?",
         "Burgenland mit 100 Euro je kWh (max. 20 kWh, bis 2.000 Euro), Oberösterreich mit 150 Euro je kWh (max. "
         "15 kWh, bis 2.250 Euro, nur Bestandsanlagen vor 1. Jänner 2026) und Tirol mit 100 Euro je kWh (max. "
         "10 kWh, bis 1.000 Euro). Kärnten zahlt 1.000 Euro Pauschale für die Nachrüstung. Der Bund fördert "
         "Speicher überall mit 150 Euro je kWh, aber nur mit PV-Neuerrichtung oder -Erweiterung."),
        ("Wie viel bringt die EAG-Bundesförderung für eine Privatanlage?",
         "Für die PV-Anlage 150 Euro je kWp bis 10 kWp und 140 Euro je kWp bis 20 kWp, also 1.500 bis 2.800 Euro. "
         "Dazu 150 Euro je kWh Speicher und der Made-in-Europe-Bonus von 10 Prozent je Komponente. Für 8 kWp mit "
         "8 kWh Speicher ergibt das 2.400 Euro plus Bonus."),
        ("Was passiert, wenn die Fördertöpfe ausgeschöpft sind?",
         "Dann werden auch fristgerechte Anträge abgelehnt, in den meisten Programmen gilt First-Come-First-Served. "
         "In Wien waren die Töpfe 2024 bereits im Juni leer, in Kärnten standen 2025 rund 40 Millionen Euro für "
         "13.000 Anträge bereit. Eine Antragstellung am ersten Tag des Calls erhöht die Chancen erheblich."),
        ("Gibt es zusätzlich Gemeindeförderungen?",
         "Ja, viele Gemeinden zahlen 200 bis 1.000 Euro zusätzlich, besonders in Niederösterreich, der Steiermark "
         "und Kärnten. Die Programme ändern sich jährlich und werden nicht zentral veröffentlicht, ein Anruf beim "
         "Gemeindeamt lohnt sich fast immer. In den meisten Fällen sind sie mit Bund und Land kombinierbar."),
        ("Übernimmt EBZ Energie die Förderabwicklung auch in anderen Bundesländern?",
         "EBZ Energie montiert in Kärnten und der Steiermark und übernimmt dort die komplette Förderabwicklung "
         "von der Erstberatung über die Ticketziehung bis zur Endabrechnung. Referenzprojekte gibt es in sechs "
         "Bundesländern. Für Projekte außerhalb des Montagegebiets prüfen wir die Machbarkeit auf Anfrage."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und montiert PV-Anlagen, "
                    "Speicher und Wärmepumpen in Kärnten und der Steiermark und wickelt die Förderungen von Bund, Land "
                    "und Gemeinde für seine Kunden ab. Die Angaben zu allen neun Bundesländern werden anhand der "
                    "offiziellen Richtlinien der EAG-Abwicklungsstelle sowie der Länder aktualisiert. Keine Rechts- "
                    "oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("EAG-Abwicklungsstelle (OeMAG): Investitionszuschuss", "https://www.eag-abwicklungsstelle.at/"),
        ("Land Burgenland", "https://www.burgenland.at/"),
        ("Förderportal des Landes Kärnten", "https://www.ktn.gv.at/"),
        ("Land Niederösterreich", "https://www.noe.gv.at/"),
        ("Land Oberösterreich", "https://www.land-oberoesterreich.gv.at/"),
        ("Land Salzburg", "https://www.salzburg.gv.at/"),
        ("Förderportal des Landes Steiermark", "https://www.steiermark.at/"),
        ("Land Tirol", "https://www.tirol.gv.at/"),
        ("Land Vorarlberg", "https://www.vorarlberg.at/"),
        ("Stadt Wien", "https://www.wien.gv.at/"),
        ("Klima- und Energiefonds", "https://www.klimafonds.gv.at/"),
    ],
    "related": [
        (KTN, "Photovoltaik-Förderung Kärnten 2026"),
        (STMK, "Photovoltaik-Förderung Steiermark 2026"),
        ("/photovoltaik-foerderung-oesterreich-2026/", "Photovoltaik-Förderung Österreich 2026 (EAG)"),
        ("/foerderung-fuer-pv-speicher/", "Förderung für PV-Speicher"),
    ],
    "cta": {
        "h3": "Welche Förderung gilt bei Ihnen?",
        "text": "Wir prüfen Bund, Land und Gemeinde für Ihren Standort und stellen die Anträge in der richtigen Reihenfolge.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre PV-Anlage, förderoptimiert geplant",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
