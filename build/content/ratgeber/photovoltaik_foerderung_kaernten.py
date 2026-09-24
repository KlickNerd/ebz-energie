"""Ratgeber: Photovoltaik-Förderung Kärnten 2026.

Migriert von ebz-photovoltaik.at/photovoltaik-foerderung-kaernten/ (Stand Juni 2026),
inhaltlich bereinigt und auf die Ratgeber-Vorlage umgestellt.
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
    "title": "PV-Förderung Kärnten 2026: 3.000 € plus Bund | EBZ Energie",
    "description": ("PV-Förderung Kärnten 2026: 3.000 € Landespauschale für PV ab 5 kWp mit Speicher, voll mit "
                    "der EAG-Bundesförderung kombinierbar. Fristen, Ablauf, Rechenbeispiel."),
    "eyebrow": "Förderung · Kärnten",
    "crumb_label": "PV-Förderung Kärnten 2026",
    "h1": "Photovoltaik-Förderung Kärnten 2026: 3.000 Euro Landespauschale plus Bundesförderung",
    "lead": ("Kärnten fördert 2026 neue private PV-Anlagen mit Speicher pauschal mit 3.000 Euro, ohne "
             "Anrechnung der EAG-Bundesförderung. Für eine typische 8-kWp-Anlage mit 8-kWh-Speicher sind "
             "damit rund 5.700 bis 5.900 Euro Gesamtförderung realistisch."),
    "chips": [
        "Land Kärnten: <b>3.000 €</b> Pauschale",
        "Speicher-Nachrüstung: <b>1.000 €</b>",
        "EAG-Bund: <b>150 €/kWp</b> + 150 €/kWh",
        "Landes-Call: <b>15. April bis 30. Juni 2026</b>",
    ],
    "date_published": "2026-05-25",
    "date_modified": "2026-09-24",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus in Kärnten mit Photovoltaikanlage auf dem Dach",

    "tldr": [
        "Das Land Kärnten zahlt 2026 eine Pauschale von 3.000 Euro für neue private PV-Anlagen ab 5 kWp "
        "mit Stromspeicher ab 5 kWh nutzbarer Kapazität. Die Speicher-Nachrüstung an Bestandsanlagen "
        "bringt 1.000 Euro.",
        "Die Landespauschale ist voll mit dem EAG-Investitionszuschuss des Bundes kombinierbar. Die "
        "frühere Anrechnung der Bundesförderung auf die Landesförderung entfällt 2026.",
        "Speicherpflicht: Reine PV-Anlagen ohne Speicher fördert das Land Kärnten 2026 nicht mehr. Die "
        "EAG-Bundesförderung bleibt davon unberührt.",
        "Termine: Landes-Call vom 15. April bis 30. Juni 2026 (Antrag erst nach Fertigstellung), "
        "EAG-Calls ab 23. April, 16. Juni und 8. Oktober 2026 (Antrag vor Inbetriebnahme). "
        "Landesbudget: rund 40 Millionen Euro.",
        "Rechenbeispiel 8 kWp mit 8 kWh Speicher: 3.000 Euro Land plus 2.400 Euro Bund plus "
        "Made-in-Europe-Bonus, in Summe rund 5.700 bis 5.900 Euro oder etwa 32 Prozent der Kosten.",
    ],
    "kpis": [
        ("3.000 €", "Landespauschale für PV ab 5 kWp mit Speicher"),
        ("150 €/kWp", "EAG-Bundesförderung bis 10 kWp"),
        ("30.06.2026", "Ende des Kärntner Landes-Calls"),
        ("~32 %", "Förderquote im Rechenbeispiel*"),
    ],

    "sections": [
        ("Die Photovoltaik-Förderung Kärnten 2026 im Überblick", "ueberblick", f"""
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
        ["Reine PV-Anlage ohne Speicher", "keine Landesförderung mehr", "0 € (nur EAG-Bund)"],
        ["Betriebliche Eigenverbrauchsanlage", "eigenverbrauchsoptimierte Auslegung", "bis 200 €/kWp, max. 45 % der Kosten, max. 500.000 € je Standort"],
    ],
    hl_cols=(2,),
)}
<p>Insgesamt stellt das Land Kärnten 2026 rund 40 Millionen Euro für die Energieförderung bereit, ein
ähnlich hohes Budget wie im Vorjahr, in dem rund 13.000 Förderfälle abgewickelt wurden. Der erste
Landes-Call läuft vom 15. April bis 30. Juni 2026. Die wichtigste Neuerung für die Kalkulation: Die
bisher nötige Anrechnung von Bundesförderungen auf die Landespauschale entfällt komplett.</p>
<p><small>Stand: Juni 2026. Maßgeblich sind die jeweils gültigen Richtlinien des Landes Kärnten.</small></p>
"""),
        ("EAG-Bundesförderung 2026: die zweite Säule", "eag", f"""
<p>Die volle Wirkung entfaltet die Kärntner Landesförderung erst in Kombination mit dem
EAG-Investitionszuschuss des Bundes. Mit der EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026,
kundgemacht am 16. Jänner 2026, sind die Konditionen für das Förderjahr fixiert. Die Fördersätze sind
nach Anlagengröße in vier Kategorien gestaffelt:</p>
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
<p>Stromspeicher fördert der Bund mit 150 Euro je kWh bis maximal 50 kWh, allerdings nur in Kombination
mit einer PV-Neuerrichtung oder -Erweiterung. Dazu kommt der Made-in-Europe-Bonus von jeweils
10 Prozent pro Komponente für PV-Module, Wechselrichter und Speicher, sofern die Produkte auf der
White List der EAG-Abwicklungsstelle stehen.</p>
<p>Die drei EAG-Fördercalls 2026 laufen vom 23. April bis 11. Mai, vom 16. bis 30. Juni sowie ab
8. Oktober. Die Antragstellung erfolgt online über die EAG-Abwicklungsstelle, in den Kategorien A und B
mit Ticketziehung nach Eingang. Entscheidend: Der EAG-Antrag muss vor Inbetriebnahme der Anlage gestellt
werden. Die Kärntner Landesförderung wird dagegen erst nach Fertigstellung beantragt. Mehr zu den
Bundeskonditionen im Ratgeber {a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}.</p>
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
{A.box("Wer keinen Speicher installieren möchte, verliert die 3.000-Euro-Pauschale, kann aber weiterhin "
       "die EAG-Bundesförderung für die PV-Anlage nutzen. Bei einem 5-kWh-Speicher ab rund 3.000 Euro "
       "Mehrkosten* rechnet sich die Pauschale in der Regel bereits über die Förderung selbst.")}
<p><small>*Richtwert für marktübliche Heimspeicher inklusive Installation. Der tatsächliche Preis hängt von
Hersteller, Kapazität und Aufwand vor Ort ab.</small></p>
"""),
        ("Antragstellung in Kärnten: Schritt für Schritt", "antrag", f"""
<p>Der zentrale Unterschied zwischen Land und Bund ist der Zeitpunkt: Der Kärntner Landesantrag wird
erst nach vollständiger Fertigstellung gestellt, der EAG-Antrag zwingend vor Inbetriebnahme. Wer beide
Förderungen kombinieren will, hält diese Reihenfolge ein:</p>
{A.steps([
    ("EAG-Antrag vor der Errichtung",
     "Am ersten Tag des EAG-Calls (23. April, 16. Juni oder 8. Oktober 2026) Ticket ziehen und den "
     "Bundesantrag online einreichen. Dafür brauchen Sie Zählpunktnummer, Netzzugangsvertrag und alle "
     "erforderlichen Genehmigungen oder Anzeigen."),
    ("Montage und Inbetriebnahme",
     "Errichtung durch ein gewerblich befugtes Unternehmen. Alle Hauptkomponenten müssen nach dem "
     "1. Jänner 2026 in Rechnung gestellt und per Überweisung bezahlt sein."),
    ("Landesantrag nach Fertigstellung",
     "Zwischen 15. April und 30. Juni 2026 den Antrag online über das Portal des Landes Kärnten "
     "stellen: Rechnungen, Zahlungsnachweise und Abnahme- beziehungsweise Prüfprotokoll hochladen."),
    ("Prüfung und Auszahlung",
     "Bei vollständigen Unterlagen wird die 3.000-Euro-Pauschale auf das angegebene Konto überwiesen. "
     "Da eine Reihung nach Eingang der vollständigen Anträge erfolgen kann, lohnt sich eine zeitnahe "
     "Einreichung."),
])}
{A.box_dark("Der häufigste Fehler",
    "Wer die Anlage in Betrieb nimmt, bevor der EAG-Antrag gestellt ist, verliert die Bundesförderung. "
    "Wer den Landesantrag vor der Fertigstellung stellt, wird abgelehnt. Planen Sie beide Termine "
    "gemeinsam mit Ihrem Fachbetrieb, bevor die erste Rechnung gestellt wird.")}
{A.cta("Förderabwicklung in Kärnten aus einer Hand",
       "EBZ Energie aus Villach zieht das EAG-Ticket, stellt den Landesantrag nach Fertigstellung und "
       "prüft die Gemeindeförderung an Ihrem Wohnort.",
       secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
        ("Kombination mit dem Bund: die Rechnung im Detail", "kombination", f"""
<p>Der attraktivste Aspekt der Kärntner Reform 2026 ist die volle Kombinierbarkeit mit dem
EAG-Investitionszuschuss. Eine typische 8-kWp-Anlage mit 8-kWh-Speicher kostet inklusive Montage rund
18.000 Euro*. So setzt sich die Förderung zusammen:</p>
{A.table(
    ["Position", "Berechnung", "Betrag"],
    [
        ["EAG-Bund, PV-Anlage", "8 kWp × 150 €/kWp", "1.200 €"],
        ["EAG-Bund, Speicher", "8 kWh × 150 €/kWh", "1.200 €"],
        ["Made-in-Europe-Bonus", "10 % je Komponente auf den EAG-Zuschuss", "rund 360 bis 480 €"],
        ["Land Kärnten", "Pauschale PV mit Speicher", "3.000 €"],
        ["<b>Gesamtförderung</b>", "rund 32 % von 18.000 €", "<b>rund 5.700 bis 5.900 €</b>"],
    ],
    hl_cols=(2,),
)}
<p>Bei größeren Anlagen steigt der Betrag weiter: Eine 12-kWp-Anlage mit 10-kWh-Speicher (Kategorie B)
bringt aus dem Bund 1.680 Euro für die PV-Anlage plus 1.500 Euro für den Speicher, also 3.180 Euro,
dazu die Kärntner Pauschale von 3.000 Euro. Mit Made-in-Europe-Bonus liegt die Gesamtförderung damit bei
rund 6.600 bis 6.800 Euro. Zusätzliche Gemeindeförderungen können noch dazukommen.</p>
<p>Zum Vergleich: Der Richtpreis für eine 10-kWp-Anlage mit Speicher liegt bei rund 15.000 bis 22.000 Euro
vor Förderung. Was danach bleibt, lässt sich über eine {a('finanzierung', 'Finanzierung')} ab 147 Euro
im Monat inklusive Speicher abbilden, die Anlage gehört dabei ab dem ersten Tag Ihnen.</p>
<p><small>*Beispielkonditionen für eine marktübliche Anlage inklusive Montage. Der Made-in-Europe-Bonus
setzt Komponenten von der White List der EAG-Abwicklungsstelle voraus.</small></p>
"""),
        ("Gemeindeförderungen in Kärnten: der oft übersehene Zusatztopf", "gemeinde", f"""
<p>Neben Land und Bund bieten viele Kärntner Gemeinden eigene PV-Förderprogramme an. Die Bandbreite
reicht von pauschalen Fixzuschüssen über Speicherboni bis zu prozentualen Beteiligungen an den
Investitionskosten. Manche Gemeinden setzen Schwerpunkte auf Stromspeicher, andere auf Wallboxen.</p>
<p>Weil sich diese Programme jährlich ändern und nicht zentral veröffentlicht werden, lohnt sich ein
Anruf bei der Wohnsitzgemeinde oder ein Blick auf deren Website. In vielen Fällen sind
Gemeindeförderungen zusätzlich zu Bundes- und Landesförderung kombinierbar, sofern die
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
<p>Die einheitliche 3.000-Euro-Pauschale, die volle Kombinierbarkeit mit dem Bund und die hohe
Sonneneinstrahlung im Süden Österreichs ergeben eine Förderkonstellation, die es 2026 in keinem anderen
Bundesland gibt (Vergleich: {a('/photovoltaik-landesfoerderungen/', 'PV-Landesförderungen aller neun Bundesländer')}).
Für eine typische Privatanlage sind rund 5.700 bis 6.800 Euro Gesamtförderung realistisch.</p>
<p>Die Fördertöpfe sind aber begrenzt, der Landes-Call endet am 30. Juni 2026, und die Reihenfolge der
Anträge ist entscheidend: EAG vor Inbetriebnahme, Land nach Fertigstellung. Wer diese Reihenfolge
falsch macht, verliert eine der beiden Förderungen.</p>
{A.cta("Jetzt Förderung in Kärnten sichern",
       "Wir planen Ihre Anlage förderfähig, übernehmen EAG-Ticket und Landesantrag und liefern den "
       "Projektbericht mit 3D-Belegplan und Statikreport.",
       primary=("kontakt", "Kostenlose Beratung anfragen"), secondary=("batteriespeicher", "Mehr zum Batteriespeicher"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für PV-Förderung in Kärnten: EBZ Energie aus Villach",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie GmbH plant und montiert Photovoltaikanlagen, Speicher und Wärmepumpen in ganz "
                 "Kärnten mit einem festangestellten Team aus "
                 "zertifizierten Fachkräften. Wir kennen die Kärntner Landesrichtlinie, die EAG-Termine und die "
                 "Gemeindeförderungen im Detail und übernehmen die komplette Förderabwicklung. Referenz vor "
                 "Ort: ein Einfamilienhaus in Villach mit 10 kWp Ost-West-Anlage, Notstromfunktion und rund "
                 "80 Prozent weniger Stromkosten."),
        "grid": [
            ("Förderabwicklung komplett", "EAG-Ticket, Landesantrag Kärnten, Gemeindeförderung und Endabrechnung."),
            ("Förderfähig geplant", "Mindestens 5 kWp und 5 kWh, Made-in-Europe-Komponenten von der White List."),
            ("Referenzen in Kärnten", "300+ Projekte, darunter Villach, Krumpendorf, Landskron und Faakersee."),
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und Energiemanagement vom selben Team."),
        ],
    },

    "faq": [
        ("Wie hoch ist die maximale Photovoltaik-Förderung in Kärnten 2026?",
         "Für eine private 8-kWp-Anlage mit 8-kWh-Speicher sind rund 5.700 bis 5.900 Euro realistisch: 3.000 Euro "
         "Landespauschale plus 2.400 Euro EAG-Bundesförderung plus Made-in-Europe-Bonus. Bei einer 12-kWp-Anlage "
         "mit 10-kWh-Speicher steigt die Gesamtförderung auf rund 6.600 bis 6.800 Euro. Gemeindeförderungen "
         "können den Betrag weiter erhöhen."),
        ("Bekomme ich die Kärntner PV-Förderung auch ohne Speicher?",
         "Nein. Die Richtlinie 2026 schreibt für jede neu geförderte Anlage einen stationären Stromspeicher mit "
         "mindestens 5 kWh nutzbarer Kapazität vor, die PV-Anlage muss mindestens 5 kWp leisten. Ohne Speicher "
         "bleibt nur die EAG-Bundesförderung mit 150 Euro je kWp."),
        ("Wann muss ich den Antrag in Kärnten 2026 stellen?",
         "Der Landes-Call läuft vom 15. April bis 30. Juni 2026, der Antrag wird erst nach vollständiger "
         "Fertigstellung der Anlage gestellt. Der EAG-Bundesantrag muss dagegen vor Inbetriebnahme eingereicht "
         "werden, idealerweise am ersten Tag eines Fördercalls (23. April, 16. Juni oder 8. Oktober 2026)."),
        ("Wird die Bundesförderung auf die Kärntner Pauschale angerechnet?",
         "Nein, nicht mehr. Seit 2026 entfällt die Anrechnung von Bundesförderungen auf die Landespauschale. "
         "Sie erhalten den vollen EAG-Investitionszuschuss und zusätzlich die 3.000 Euro vom Land Kärnten."),
        ("Was bekomme ich für eine Speicher-Nachrüstung an einer bestehenden Anlage?",
         "Das Land Kärnten fördert die Nachrüstung eines Speichers ab 5 kWh an einer Bestandsanlage mit "
         "1.000 Euro Pauschale. Die EAG-Bundesförderung greift bei reiner Nachrüstung nicht, weil sie eine "
         "PV-Neuerrichtung oder -Erweiterung voraussetzt. Details im Ratgeber zur Speicherförderung in Kärnten."),
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
         "Ticketziehung beim EAG-Call, Landesantrag nach Fertigstellung und Prüfung der Gemeindeförderung. "
         "Sie müssen sich um nichts kümmern."),
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
        "text": "Wir planen Ihre Anlage so, dass Land und Bund voll greifen, und übernehmen beide Anträge.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre PV-Anlage in Kärnten, förderoptimiert geplant",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
