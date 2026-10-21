"""Ratgeber: Photovoltaik-Förderung Kärnten 2026.

Migriert von ebz-photovoltaik.at/photovoltaik-foerderung-kaernten/ (Stand Juni 2026),
inhaltlich bereinigt und auf die Ratgeber-Vorlage umgestellt.
Stand Oktober 2026: 2. Landes-Call 12.10. bis 31.12.2026 (Budget rund 10 Mio. EUR), 1. Call (15.4. bis 30.6.)
als Historie; EAG 3. und letzter Call lief 8. bis 22.10.2026 (beendet, derzeit kein Bundeszuschuss),
Ausblick 2027 Systemfoerderung (laut BMWET geplant, nicht beschlossen). Stand ab 23.10.2026.
Zahlen: Landesrichtlinie Kärnten 2026 und EAG-Investitionszuschüsseverordnung 2026 (Quellen unten).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "photovoltaik-foerderung-kaernten",
    "path": "/photovoltaik-foerderung-kaernten/",
    "title": "PV-Förderung Kärnten 2026: 3.000 € bis 31.12. | EBZ Energie",
    "description": ("PV-Förderung Kärnten 2026: 3.000 € Landespauschale für PV ab 5 kWp mit Speicher, 2. Call "
                    "bis 31.12.2026. Bundescall beendet, Ausblick 2027, Rechenbeispiel."),
    "eyebrow": "Förderung · Kärnten",
    "crumb_label": "PV-Förderung Kärnten 2026",
    "h1": "Photovoltaik-Förderung Kärnten 2026: 3.000 Euro Landespauschale, 2. Call bis 31. Dezember 2026",
    "lead": ("Kärnten fördert 2026 neue private PV-Anlagen mit Speicher pauschal mit 3.000 Euro, ohne "
             "Anrechnung der EAG-Bundesförderung. Der zweite Landes-Call läuft vom 12. Oktober bis 31. Dezember 2026. "
             "Der letzte EAG-Call des Bundes lief vom 8. bis 22. Oktober 2026, derzeit ist kein Bundeszuschuss "
             "beantragbar; im Call 2026 waren für 8 kWp mit 8 kWh rund 5.760 Euro Gesamtförderung möglich, aktuell "
             "sind es 3.000 Euro vom Land."),
    "chips": [
        "Land Kärnten: <b>3.000 €</b> Pauschale",
        "Speicher-Nachrüstung: <b>1.000 €</b>",
        "EAG-Bund: <b>Call 2026 beendet</b>",
        "2. Landes-Call: <b>12. Oktober bis 31. Dezember 2026</b>",
    ],
    "date_published": "2026-05-25",
    "date_modified": "2026-10-21",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus in Kärnten mit Photovoltaikanlage auf dem Dach",

    "tldr": [
        "Das Land Kärnten zahlt 2026 eine Pauschale von 3.000 Euro für neue private PV-Anlagen ab 5 kWp "
        "mit Stromspeicher ab 5 kWh nutzbarer Kapazität. Die Speicher-Nachrüstung an Bestandsanlagen "
        "bringt 1.000 Euro.",
        "Die Landespauschale war im Call 2026 voll mit dem EAG-Investitionszuschuss des Bundes kombinierbar, "
        "die frühere Anrechnung der Bundesförderung entfällt 2026. Der letzte EAG-Call endete am 22. Oktober 2026, "
        "derzeit gibt es keinen Bundeszuschuss für neue Anlagen.",
        "Speicherpflicht: Reine PV-Anlagen ohne Speicher fördert das Land Kärnten 2026 nicht mehr. Wer jetzt "
        "plant, baut daher mit Speicher und Energiemanagement: Das sichert die 3.000 Euro und wahrt die Chance auf "
        "die Systemförderung 2027, die laut BMWET geplant, aber nicht beschlossen ist.",
        "Termine (Stand Oktober 2026): 2. Landes-Call vom 12. Oktober bis 31. Dezember 2026, Budget rund "
        "10 Millionen Euro, Antrag erst nach Fertigstellung über die Förderplattform des Landes; der 1. Call lief "
        "vom 15. April bis 30. Juni 2026. EAG-Bund: Der 3. und letzte Call lief vom 8. bis 22. Oktober 2026, ab "
        "2027 ist laut BMWET eine Systemförderung mit Antrag nach Installation geplant (nicht beschlossen).",
        "Rechenbeispiel 8 kWp mit 8 kWh Speicher: Im Call 2026 gab es 3.000 Euro Land plus 2.400 Euro Bund plus "
        "Made-in-Europe-Bonus, in Summe rund 5.760 Euro oder etwa 32 Prozent der Kosten. Aktuell: 3.000 Euro Land, "
        "der Bund ist derzeit nicht beantragbar.",
    ],
    "kpis": [
        ("3.000 €", "Landespauschale für PV ab 5 kWp mit Speicher"),
        ("150 €/kWp", "EAG-Bundesförderung bis 10 kWp im Call 2026"),
        ("31.12.2026", "Ende des 2. Kärntner Landes-Calls (Start 12.10.)"),
        ("~32 %", "Förderquote im Rechenbeispiel*"),
    ],

    "sections": [
        ("Die Photovoltaik-Förderung Kärnten 2026 im Überblick", "ueberblick", f"""
<p><b>Das Land Kärnten fördert 2026 private PV-Anlagen ab 5 kWp mit mindestens 5 kWh Speicher pauschal mit
3.000 Euro, die Speicher-Nachrüstung mit 1.000 Euro.</b> Antrag online vom 12. Oktober bis 31. Dezember 2026
(zweiter Call, Start 9 Uhr), maximal 50 Prozent der Baukosten, Budget rund 10 Millionen Euro, Anlagen ab
1. Jänner 2026 errichtet (Quelle: Land Kärnten, Stand Oktober 2026). Der EAG-Zuschuss des Bundes kam im
Call 2026 ohne Anrechnung dazu; der letzte Call endete am 22. Oktober 2026, derzeit ist der Bund nicht
beantragbar.</p>
<p>Kärnten zählt mit über 1.900 Sonnenstunden im Jahr zu den einstrahlungsreichsten Regionen Österreichs
und hat 2026 zusätzlich seine PV-Landesförderung grundlegend vereinfacht. Statt der degressiven Sätze
pro Kilowattpeak aus den Vorjahren gibt es jetzt eine Pauschale: Wer eine neue private PV-Anlage mit
mindestens 5 kWp errichtet und gleichzeitig einen Stromspeicher mit mindestens 5 kWh nutzbarer
Kapazität installiert, erhält 3.000 Euro vom Land. Der Betrag gilt unabhängig von der Anlagengröße,
eine 12-kWp-Anlage bekommt dieselbe Pauschale wie eine 5-kWp-Anlage.</p>
<p>Wer bereits eine PV-Anlage besitzt und nur einen Speicher ab 5 kWh nachrüstet, erhält 1.000 Euro.
Für betriebliche Eigenverbrauchsanlagen gibt es eine eigene Schiene mit bis zu 200 Euro pro kWp.</p>
{A.table(
    ["Förderschiene Land Kärnten", "Voraussetzung", "Förderhöhe 2026"],
    [
        ["Neue private PV-Anlage mit Speicher", "ab 5 kWp PV und ab 5 kWh nutzbarer Speicherkapazität", "3.000 € Pauschale"],
        ["Speicher-Nachrüstung an Bestandsanlage", "Speicher ab 5 kWh", "1.000 € Pauschale"],
        ["Reine PV-Anlage ohne Speicher", "keine Landesförderung mehr", "0 € (EAG-Bund nur im Call 2026)"],
        ["Betriebliche Eigenverbrauchsanlage", "eigenverbrauchsoptimierte Auslegung", "bis 200 €/kWp, max. 45 % der Kosten, max. 500.000 € je Standort"],
    ],
    hl_cols=(2,),
)}
<p>Insgesamt stellt das Land Kärnten 2026 rund 40 Millionen Euro für die Energieförderung bereit, ein
ähnlich hohes Budget wie im Vorjahr, in dem rund 13.000 Förderfälle abgewickelt wurden. Der erste
Landes-Call lief vom 15. April bis 30. Juni 2026, der zweite Call mit rund 10 Millionen Euro Budget vom
12. Oktober bis 31. Dezember 2026. Zwei Grenzen gelten: maximal 50 Prozent der Baukosten, und
Landesförderungen der letzten zehn Jahre werden berücksichtigt. Die wichtigste Neuerung für die Kalkulation:
Die bisher nötige Anrechnung von Bundesförderungen auf die Landespauschale entfällt komplett.</p>
<p><small>Stand: Oktober 2026. Maßgeblich sind die jeweils gültigen Richtlinien des Landes Kärnten.</small></p>
"""),
        ("EAG-Bundesförderung 2026: die zweite Säule", "eag", f"""
<p>Im Call 2026 entfaltete die Kärntner Landesförderung ihre volle Wirkung erst in Kombination mit dem
EAG-Investitionszuschuss des Bundes. Mit der EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026,
kundgemacht am 16. Jänner 2026, waren die Konditionen für das Förderjahr fixiert. Die Fördersätze waren
nach Anlagengröße in vier Kategorien gestaffelt und sind derzeit nicht beantragbar:</p>
{A.table(
    ["Kategorie", "Anlagengröße", "Fördersatz PV", "Vergabe"],
    [
        ["A", "bis 10 kWp", "150 €/kWp", "First-Come-First-Served"],
        ["B", "über 10 bis 20 kWp", "140 €/kWp", "First-Come-First-Served"],
        ["C", "über 20 bis 100 kWp", "max. 130 €/kWp", "Bieterverfahren"],
        ["D", "über 100 bis 1.000 kWp", "max. 120 €/kWp", "Bieterverfahren"],
    ],
    hl_cols=(2,),
)}
<p>Stromspeicher förderte der Bund 2026 mit 150 Euro je kWh bis maximal 50 kWh, allerdings nur in
Kombination mit einer PV-Neuerrichtung oder -Erweiterung. Dazu kam der Made-in-Europe-Bonus von jeweils
10 Prozent pro Komponente für PV-Module, Wechselrichter und Speicher, sofern die Produkte auf der
White List der EAG-Abwicklungsstelle standen.</p>
<p>Die drei EAG-Fördercalls 2026 liefen vom 23. April bis 11. Mai, vom 16. bis 30. Juni sowie vom 8. bis
22. Oktober. Die Antragstellung erfolgte online über die EAG-Abwicklungsstelle, in den Kategorien A und B
mit Ticketziehung nach Eingang, und musste vor Inbetriebnahme der Anlage gestellt werden. Die Kärntner
Landesförderung wird dagegen erst nach Fertigstellung beantragt. Mehr zu den Bundeskonditionen im Ratgeber
{a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}.</p>
<p><b>Stand ab 23. Oktober 2026:</b> Der dritte Call lief vom 8. bis 22. Oktober 2026 und war der letzte im
bisherigen System. Neue Anlagen bekommen derzeit keinen Bundeszuschuss. Ab 2027 ist laut Eckpunkten des
BMWET eine Systemförderung geplant, aber nicht beschlossen: Antrag nach Installation und Rechnung statt
Fördercall, gefördert werden sollen Speicher mit intelligenter Steuerung, auch als Nachrüstung; Projekte mit
intelligentem Speicher, die ab 1. November 2026 in Betrieb gehen, sollen 2027 beantragbar sein. Höhe und
Technikkriterien sind noch offen.</p>
<p>Wer jetzt in Kärnten plant, baut deshalb sinnvoll mit Speicher und Energiemanagement: Das Land zahlt die
3.000 Euro nur mit Speicher, und die Anlage wahrt die Chance auf die Systemförderung 2027.</p>
"""),
        ("Voraussetzungen für die Landesförderung Kärnten", "voraussetzungen", f"""
<p>Die Kärntner Bedingungen sind im Vergleich zu anderen Bundesländern klar formuliert, jede Abweichung
führt aber zur Ablehnung. Diese Punkte müssen erfüllt sein:</p>
<ul>
  <li><b>Speicherpflicht:</b> mindestens 5 kWp PV-Leistung und 5 kWh nutzbare Speicherkapazität.
  Reine PV-Anlagen ohne Speicher fördert das Land 2026 nicht.</li>
  <li><b>Netzkopplung:</b> Inselanlagen ohne Verbindung zum öffentlichen Netz sind nicht förderfähig.
  Anlagen, die ausschließlich als Volleinspeiser laufen, ebenfalls nicht.</li>
  <li><b>Rechnungsdatum:</b> Module, Wechselrichter und Speicher müssen nach dem 1. Jänner 2026 in
  Rechnung gestellt worden sein.</li>
  <li><b>Eigentum:</b> Sie sind Eigentümer der Liegenschaft oder legen eine schriftliche Einwilligung
  des Eigentümers vor.</li>
  <li><b>Zahlung:</b> Barzahlungen werden nicht akzeptiert, alle Rechnungen müssen per Überweisung
  beglichen sein.</li>
  <li><b>Keine Doppelförderung:</b> Für denselben Förderzweck darf in den letzten zehn Jahren kein
  Antrag gestellt worden sein.</li>
  <li><b>Fachbetrieb:</b> Montage und Inbetriebnahme durch ein gewerblich befugtes Unternehmen,
  inklusive Abnahme- beziehungsweise Prüfprotokoll.</li>
</ul>
{A.box("Wer keinen Speicher installieren möchte, verliert die 3.000-Euro-Pauschale; ein Bundeszuschuss für "
       "die PV-Anlage ist seit Ende des Calls 2026 derzeit nicht beantragbar. Bei einem 5-kWh-Speicher ab rund "
       "3.000 Euro Mehrkosten* rechnet sich die Pauschale in der Regel bereits über die Förderung selbst.")}
<p><small>*Richtwert für marktübliche Heimspeicher inklusive Installation. Der tatsächliche Preis hängt von
Hersteller, Kapazität und Aufwand vor Ort ab.</small></p>
"""),
        ("Antragstellung in Kärnten: Schritt für Schritt", "antrag", f"""
<p>Der zentrale Unterschied zwischen Land und Bund war 2026 der Zeitpunkt: Der Kärntner Landesantrag wird
erst nach vollständiger Fertigstellung gestellt, der EAG-Antrag musste im Call 2026 zwingend vor
Inbetriebnahme liegen. So lief die Kombination 2026; seit dem Ende des letzten Calls am 22. Oktober 2026
entfällt Schritt 1 derzeit:</p>
{A.steps([
    ("EAG-Antrag vor der Errichtung",
     "Im Call 2026 wurde am ersten Tag des EAG-Calls (23. April, 16. Juni oder 8. Oktober 2026; der letzte "
     "Call endete am 22. Oktober) das Ticket gezogen und der Bundesantrag online eingereicht, mit "
     "Zählpunktnummer, Netzzugangsvertrag und allen Genehmigungen oder Anzeigen. Ab 2027 soll der Antrag laut "
     "BMWET nach der Installation gestellt werden (geplant, nicht beschlossen)."),
    ("Montage und Inbetriebnahme",
     "Errichtung durch ein gewerblich befugtes Unternehmen. Alle Hauptkomponenten müssen nach dem "
     "1. Jänner 2026 in Rechnung gestellt und per Überweisung bezahlt sein."),
    ("Landesantrag nach Fertigstellung",
     "Im zweiten Call zwischen 12. Oktober (ab 9 Uhr) und 31. Dezember 2026 den Antrag online über die "
     "Förderplattform des Landes Kärnten stellen: Rechnungen, Zahlungsnachweise und Abnahme- beziehungsweise "
     "Prüfprotokoll hochladen. Der erste Call lief vom 15. April bis 30. Juni 2026."),
    ("Prüfung und Auszahlung",
     "Bei vollständigen Unterlagen wird die 3.000-Euro-Pauschale auf das angegebene Konto überwiesen. "
     "Da eine Reihung nach Eingang der vollständigen Anträge erfolgen kann, lohnt sich eine zeitnahe "
     "Einreichung."),
])}
{A.box_dark("Der häufigste Fehler",
    "Wer den Landesantrag vor der Fertigstellung stellt, wird abgelehnt. Im Call 2026 verlor zudem die "
    "Bundesförderung, wer vor dem EAG-Antrag in Betrieb nahm; für die geplante Systemförderung 2027 soll der "
    "Antrag laut BMWET erst nach der Installation kommen. Planen Sie die Termine gemeinsam mit Ihrem "
    "Fachbetrieb, bevor die erste Rechnung gestellt wird.")}
{A.cta("Förderabwicklung in Kärnten aus einer Hand",
       "EBZ Energie aus Villach stellt den Landesantrag nach Fertigstellung, prüft die Gemeindeförderung an "
       "Ihrem Wohnort und plant Speicher und Energiemanagement mit Blick auf die Systemförderung 2027.",
       secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
        ("Kombination mit dem Bund: die Rechnung im Detail", "kombination", f"""
<p>Der attraktivste Aspekt der Kärntner Reform 2026 war die volle Kombinierbarkeit mit dem
EAG-Investitionszuschuss. Eine typische 8-kWp-Anlage mit 8-kWh-Speicher kostet inklusive Montage rund
18.000 Euro*. So setzte sich die Förderung im Call 2026 zusammen; die Bundesposten sind derzeit nicht
beantragbar:</p>
{A.table(
    ["Position", "Berechnung", "Betrag"],
    [
        ["EAG-Bund, PV-Anlage, im Call 2026", "8 kWp × 150 €/kWp", "1.200 €"],
        ["EAG-Bund, Speicher, im Call 2026", "8 kWh × 150 €/kWh", "1.200 €"],
        ["Made-in-Europe-Bonus, im Call 2026", "10 % je Komponente auf den EAG-Zuschuss", "rund 360 €"],
        ["Land Kärnten", "Pauschale PV mit Speicher", "3.000 €"],
        ["<b>Gesamtförderung im Call 2026</b>", "rund 32 % von 18.000 €", "<b>rund 5.760 €</b>"],
        ["<b>Aktuell (Bund derzeit nicht beantragbar)</b>", "nur Landespauschale, rund 17 % von 18.000 €", "<b>3.000 €</b>"],
    ],
    hl_cols=(2,),
)}
<p>Bei größeren Anlagen stieg der Betrag im Call 2026 weiter: Eine 12-kWp-Anlage mit 10-kWh-Speicher
(Kategorie B) brachte aus dem Bund 1.680 Euro für die PV-Anlage plus 1.500 Euro für den Speicher, also
3.180 Euro, dazu die Kärntner Pauschale von 3.000 Euro. Mit Made-in-Europe-Bonus lag die Gesamtförderung
damit bei rund 6.600 bis 6.800 Euro. Aktuell bleibt auch hier die Landespauschale von 3.000 Euro, weil die
Pauschale unabhängig von der Anlagengröße ist. Zusätzliche Gemeindeförderungen können noch dazukommen.</p>
<p>Zum Vergleich: Der Richtpreis für eine 10-kWp-Anlage mit Speicher liegt bei rund 15.000 bis 22.000 Euro
vor Förderung. Was danach bleibt, lässt sich über eine {a('finanzierung', 'Finanzierung')} ab 147 Euro
im Monat inklusive Speicher abbilden, die Anlage gehört dabei ab dem ersten Tag Ihnen.</p>
<p><small>*Beispielkonditionen für eine marktübliche Anlage inklusive Montage; Bundesposten nach den Sätzen
im Call 2026 (beendet). Der Made-in-Europe-Bonus setzte Komponenten von der White List der
EAG-Abwicklungsstelle voraus.</small></p>
"""),
        ("Gemeindeförderungen in Kärnten: der oft übersehene Zusatztopf", "gemeinde", f"""
<p>Neben Land und Bund bieten viele Kärntner Gemeinden eigene PV-Förderprogramme an. Die Bandbreite
reicht von pauschalen Fixzuschüssen über Speicherboni bis zu prozentualen Beteiligungen an den
Investitionskosten. Manche Gemeinden setzen Schwerpunkte auf Stromspeicher, andere auf Wallboxen.</p>
<p>Weil sich diese Programme jährlich ändern und nicht zentral veröffentlicht werden, lohnt sich ein
Anruf bei der Wohnsitzgemeinde oder ein Blick auf deren Website. In vielen Fällen sind
Gemeindeförderungen zusätzlich zur Landesförderung kombinierbar, sofern die
beihilferechtlichen Höchstgrenzen eingehalten werden. EBZ Energie prüft für jeden Kunden in Kärnten,
welche Zuschüsse vor Ort möglich sind.</p>
"""),
        ("Photovoltaik und Wärmepumpe: die Kombination für Kärnten", "waermepumpe", f"""
<p>Wer die Energiekosten dauerhaft senken will, kombiniert die PV-Anlage mit einer
{a('waermepumpe', 'Wärmepumpe')}. Die PV-Anlage erzeugt tagsüber Sonnenstrom, die Wärmepumpe deckt
Heizung und Warmwasser und nutzt im Idealfall direkt den selbst produzierten Strom. In dieser
Kombination sind laut Erfahrungswerten von EBZ Energie bis zu 85 Prozent Ersparnis bei den
Energiekosten möglich.</p>
<p>Förderseitig profitieren Sie doppelt: Für die PV-Anlage gelten die hier beschriebenen Förderungen,
für die Wärmepumpe gibt es eigene Schienen wie die Sanierungsoffensive des Bundes oder „Sauber Heizen
für Alle“. Ein {a('ems', 'Energiemanagementsystem')}, das beide Anlagen steuert, wird seit Juni 2026
zusätzlich vom Klima- und Energiefonds gefördert (siehe {a('/ems-foerderung/', 'EMS-Förderung 2026')}).</p>
"""),
        ("Fazit: Kärnten ist 2026 das Bundesland mit der höchsten PV-Landespauschale", "fazit", f"""
<p>Die einheitliche 3.000-Euro-Pauschale, die volle Kombinierbarkeit mit dem Bund im Call 2026 und die hohe
Sonneneinstrahlung im Süden Österreichs ergaben eine Förderkonstellation, die es 2026 in keinem anderen
Bundesland gab (Vergleich: {a('/photovoltaik-landesfoerderungen/', 'PV-Landesförderungen aller neun Bundesländer')}).
Im Call 2026 waren für eine typische Privatanlage rund 5.700 bis 6.800 Euro Gesamtförderung realistisch.</p>
<p>Der letzte EAG-Call endete am 22. Oktober 2026, derzeit ist kein Bundeszuschuss beantragbar. Beantragbar
bleibt die Landespauschale: Der zweite Landes-Call läuft vom 12. Oktober bis 31. Dezember 2026 mit rund
10 Millionen Euro Budget, der Antrag kommt nach Fertigstellung. Wer jetzt plant, baut mit Speicher und
Energiemanagement: Das sichert die 3.000 Euro und wahrt die Chance auf die Systemförderung 2027, die laut
BMWET geplant, aber nicht beschlossen ist.</p>
{A.cta("Jetzt Förderung in Kärnten sichern",
       "Wir planen Ihre Anlage förderfähig, übernehmen den Landesantrag und liefern den "
       "Projektbericht mit 3D-Belegplan und Statikreport.",
       primary=("kontakt", "Kostenlose Beratung anfragen"), secondary=("batteriespeicher", "Mehr zum Batteriespeicher"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für PV-Förderung in Kärnten: EBZ Energie aus Villach",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie GmbH plant und montiert Photovoltaikanlagen, Speicher und Wärmepumpen in ganz "
                 "Kärnten mit einem Team aus "
                 "zertifizierten Fachkräften. Wir kennen die Kärntner Landesrichtlinie, den Stand der Bundesförderung und die "
                 "Gemeindeförderungen im Detail und übernehmen die komplette Förderabwicklung. Referenz vor "
                 "Ort: ein Einfamilienhaus in Villach mit 10 kWp Ost-West-Anlage, Notstromfunktion und rund "
                 "80 Prozent weniger Stromkosten."),
        "grid": [
            ("Förderabwicklung komplett", "Landesantrag Kärnten, Gemeindeförderung, Endabrechnung und Blick auf die Systemförderung 2027."),
            ("Förderfähig geplant", "Mindestens 5 kWp und 5 kWh, Speicher mit Energiemanagement, europäische Komponenten."),
            ("Referenzen in Kärnten", "300+ Projekte, darunter Villach, Krumpendorf, Landskron und Faakersee."),
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und Energiemanagement vom selben Team."),
        ],
    },

    "faq": [
        ("Wie hoch ist die maximale Photovoltaik-Förderung in Kärnten 2026?",
         "Aktuell 3.000 Euro Landespauschale für PV ab 5 kWp mit Speicher ab 5 kWh, denn der letzte EAG-Call "
         "endete am 22. Oktober 2026 und der Bund ist derzeit nicht beantragbar. Im Call 2026 waren für 8 kWp mit "
         "8 kWh rund 5.760 Euro möglich (3.000 Euro Land plus 2.400 Euro Bund plus Made-in-Europe-Bonus). "
         "Gemeindeförderungen können den Betrag erhöhen."),
        ("Bekomme ich die Kärntner PV-Förderung auch ohne Speicher?",
         "Nein. Die Richtlinie 2026 schreibt für jede neu geförderte Anlage einen stationären Stromspeicher mit "
         "mindestens 5 kWh nutzbarer Kapazität vor, die PV-Anlage muss mindestens 5 kWp leisten. Ohne Speicher "
         "gab es nur im Call 2026 die EAG-Bundesförderung mit 150 Euro je kWp; derzeit ist der Bund nicht "
         "beantragbar."),
        ("Wann muss ich den Antrag in Kärnten 2026 stellen?",
         "Der zweite Landes-Call läuft vom 12. Oktober bis 31. Dezember 2026 (der erste lief vom 15. April bis "
         "30. Juni), der Antrag wird erst nach vollständiger Fertigstellung der Anlage über die Förderplattform des "
         "Landes gestellt. Der letzte EAG-Call des Bundes lief vom 8. bis 22. Oktober 2026 (Antrag vor "
         "Inbetriebnahme) und ist beendet; ab 2027 ist laut BMWET ein Antrag nach Installation geplant, nicht "
         "beschlossen."),
        ("Wird die Bundesförderung auf die Kärntner Pauschale angerechnet?",
         "Nein, nicht mehr. Seit 2026 entfällt die Anrechnung von Bundesförderungen auf die Landespauschale. "
         "Im Call 2026 gab es daher den vollen EAG-Investitionszuschuss und zusätzlich die 3.000 Euro vom Land "
         "Kärnten. Derzeit ist kein Bundeszuschuss beantragbar, die Landespauschale bleibt bis 31. Dezember 2026."),
        ("Was bekomme ich für eine Speicher-Nachrüstung an einer bestehenden Anlage?",
         "Das Land Kärnten fördert die Nachrüstung eines Speichers ab 5 kWh an einer Bestandsanlage mit "
         "1.000 Euro Pauschale. Die EAG-Bundesförderung griff 2026 bei reiner Nachrüstung nicht; laut BMWET soll "
         "die Nachrüstung von Speicher und Energiemanagement ab 2027 förderbar werden (geplant, nicht beschlossen). "
         "Details im Ratgeber zur Speicherförderung in Kärnten."),
        ("Werden auch betriebliche PV-Anlagen in Kärnten gefördert?",
         "Ja. Betriebliche Eigenverbrauchsanlagen fördert das Land 2026 mit bis zu 200 Euro je kWp, maximal "
         "45 Prozent der förderfähigen Investitionskosten und höchstens 500.000 Euro je Standort. Voraussetzung "
         "ist eine eigenverbrauchsoptimierte Auslegung, das Rechnungsdatum muss nach dem 1. Jänner 2026 liegen."),
        ("Welche Unterlagen brauche ich für den Landesantrag?",
         "Rechnungen der Hauptkomponenten mit Datum nach dem 1. Jänner 2026, Zahlungsnachweise per Überweisung, "
         "das Abnahme- beziehungsweise Prüfprotokoll des Fachbetriebs sowie den Eigentumsnachweis oder die "
         "Einwilligung des Eigentümers. Die Einreichung erfolgt ausschließlich online über das Portal des "
         "Landes Kärnten."),
        ("Wer übernimmt die Förderabwicklung in Kärnten?",
         "EBZ Energie mit Sitz in Villach übernimmt die komplette Abwicklung: Auswahl der Förderungen, "
         "Landesantrag nach Fertigstellung, Prüfung der Gemeindeförderung und die Vorbereitung auf die geplante "
         "Systemförderung 2027. Sie müssen sich um nichts kümmern."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und montiert "
                    "PV-Anlagen und Speicher in ganz Kärnten und wickelt die Landes-, Bundes- und "
                    "Gemeindeförderungen für seine Kunden ab. Die Angaben werden anhand der offiziellen Richtlinien "
                    "des Landes Kärnten und der EAG-Abwicklungsstelle aktualisiert. Keine Rechts- oder "
                    "Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("EAG-Abwicklungsstelle (OeMAG)", "https://www.eag-abwicklungsstelle.at/"),
        ("Förderportal des Landes Kärnten", "https://www.ktn.gv.at/"),
    ],
    "related": [
        ("/foerderung-pv-speicher-kaernten/", "Förderung für PV-Speicher in Kärnten"),
        ("/photovoltaik-landesfoerderungen/", "PV-Landesförderungen: alle 9 Bundesländer"),
        ("foerderung_steiermark", "Photovoltaik-Förderung Steiermark 2026"),
        ("pv_villach", "Photovoltaik Villach: Ihr lokaler Partner"),
    ],
    "cta": {
        "h3": "3.000 Euro vom Land Kärnten sichern",
        "text": "2. Call bis 31. Dezember 2026: Wir planen Ihre Anlage mit Speicher so, dass die Landespauschale greift, und übernehmen den Antrag.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre PV-Anlage in Kärnten, förderoptimiert geplant",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
