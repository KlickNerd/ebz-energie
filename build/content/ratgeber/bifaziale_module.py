"""Ratgeber: Bifaziale Glas-Glas-Module (Mehrertrag, Einsatz, Haltbarkeit, Statik, Brandschutz, Hagel, Kosten).

Neuer Artikel (kein WordPress-Vorgänger), erstellt 2026-11-19.
Ziel-Keywords (Google Ads, Österreich, 19.11.2026): bifaziale module 320, glas glas pv module 210,
bifaziale pv module 140, bifaziale solarmodule 90, bifaziale module nachteile 70, glas glas module 70,
pv modul bifazial 70, glas glas module nachteile 30, glas-glas module vorteile 10, bifaziale module mehrertrag 10
("bifazial mehrertrag" ohne Suchvolumen).

Faktenbasis: Recherche vom 19.11.2026 mit selbst geöffneten Quellen: IEA PVPS Task 13 (Executive Summary 2021),
Megasol (Schweizer Hersteller, Albedo und Mehrertrag), Datenblätter JA Solar JAM54D41 LB (Glas-Glas bifazial),
Trina Vertex S+ NEG9R.28 (Doppelglas, DE 2026) und Trina Vertex S DE09R.08 (Glas-Folie, FR 2023), Stadt Wien MA 39
(Brandverhalten Glas-Glas-PV-Module, Dezember 2023), EPZ Linz / Hans Starl in Schadenprisma 2/2023 (Hagel),
Hagelregister, PV Tech / sun.store PV Index Oktober 2026 (Großhandelspreise Europa), OeMAG Oktober 2026,
E-Control Preismonitor November 2026.
Eigene Rechnungen: Mehrleistung = Rückseitenanteil x Bifazialität (Datenblatt JA Solar: 455 W -> 491 W bei 10 %),
kg je m² aus Gewicht / Modulfläche (1,762 x 1,134 m), Großhandelspreis 10 kWp = 10.000 Wp x €/Wp.
Nicht behauptet: pauschaler Mehrertrag auf dem Ziegeldach in Prozent, Brandklasse A für Glas-Glas,
höhere Hagelfestigkeit von Glas-Glas, Endkunden-Aufpreis in Österreich, gemessener Mehrertrag der EBZ-Referenzen.
EBZ-Belege: Referenzen Flachdach Graz (helles Flachdach, ballastiert), Stadthaus Graz (drei Flachdächer,
aufgeständert), Hotel Villach/Warmbad (Bitumen-Flachdach, aufgeständert), alle mit Glas-Glas-Modulen, bifazial.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "bifaziale-module",
    "path": "/bifaziale-module/",
    "cluster": "Photovoltaik",
    "title": "Bifaziale Module: Mehrertrag, Glas-Glas, Nachteile | EBZ",
    "description": ("Bifaziale Glas-Glas-Module nutzen 60 bis über 90 Prozent der Leistung auch auf der Rückseite. "
                    "Wann sich das lohnt, Albedo, Nachteile, Hagel, Gewicht und Kosten."),
    "eyebrow": "Photovoltaik · Bifaziale Glas-Glas-Module",
    "crumb_label": "Bifaziale Module",
    "h1": "Bifaziale Glas-Glas-Module: Wann die Rückseite Mehrertrag bringt und was 30 Jahre Leistungsgarantie bedeuten",
    "lead": ("Bifaziale Module erzeugen Strom auf beiden Seiten. Bei 10 % Rückseitenlicht leistet ein "
             "455-Watt-Modul laut Datenblatt 491 Watt, auf einem Ziegeldach kommt dagegen kaum Licht unter das Modul. "
             "Dieser Ratgeber zeigt, wo sich bifaziale Glas-Glas-Module lohnen, was Glas-Glas an Haltbarkeit bringt "
             "und wo die Grenzen liegen."),
    "chips": [
        "Rückseite: <b>60 bis über 90 Prozent</b> der Vorderseite",
        "Neuschnee reflektiert <b>80 bis 90 Prozent</b>",
        "Glas-Glas 2 × 1,6 mm: <b>rund 21 kg</b>",
        "Leistungsgarantie: <b>bis zu 30 Jahre</b>",
    ],
    "date_published": "2026-11-19",
    "date_modified": "2026-11-19",
    "hero_img": "pv_card",
    "hero_alt": ("Aufgeständerte Photovoltaikmodule auf einem Flachdach mit hellem Dachbelag, im Hintergrund "
                 "Wohnhäuser und Berge"),

    "tldr": [
        "Bifaziale Module haben Solarzellen, die auch von hinten Licht aufnehmen. Die Rückseite erreicht je nach "
        "Zelltechnik mehr als 60 bis über 90 Prozent der Vorderseite (IEA PVPS).",
        "Wie viel das bringt, entscheidet vor allem der Untergrund: Naturboden reflektiert rund 20 bis 30 Prozent, "
        "Neuschnee 80 bis 90 Prozent. Über Naturboden liegt der Mehrertrag in Studien meist unter 10 %.",
        "Lohnend: aufgeständert auf hellem Flachdach, Carport, Zaun und senkrechte Ost-West-Anlagen. Kaum Nutzen: "
        "Module flach auf dem Ziegeldach, weil die Rückseite dort im Schatten liegt.",
        "Glas-Glas heißt: Glas vorne und hinten. Im Datenblattvergleich desselben Herstellers gibt es 30 statt 25 "
        "Jahre Leistungsgarantie und 0,4 statt 0,55 % Degradation pro Jahr, bei fast gleichem Gewicht (21,0 statt 21,8 kg).",
        "Hagel und Brandschutz: Glas-Glas-Module erreichen laut Stadt Wien meist Brandverhaltensklasse B, "
        "Glas-Folie D oder schlechter. Beim Hagel zählt die Dicke des Deckglases, nicht die Bauweise.",
    ],
    "kpis": [
        ("+7,9 %", "Mehrleistung bei 10 % Rückseitenlicht (Datenblatt)*"),
        ("0,2 bis 0,3", "Albedo von Naturboden (IEA PVPS)"),
        ("0,4 %", "max. Degradation pro Jahr, Glas-Glas (Datenblatt)"),
        ("bis zu 30 Jahre", "Leistungsgarantie auf EBZ-Module"),
    ],

    "sections": [
        ("Was sind bifaziale Module und was heißt Glas-Glas?", "grundlagen", f"""
<p><b>Ein bifaziales Modul ist ein Solarmodul, dessen Zellen Licht von beiden Seiten in Strom umwandeln: direkt
von vorne und reflektiert oder gestreut von hinten.</b> Die Vorderseite liefert weiterhin den Großteil des
Ertrags, die Rückseite kommt dazu, wenn Licht vom Boden, vom Dach oder aus der Umgebung unter das Modul fällt.
Bifaziale Zellen erreichen laut IEA PVPS auf der Rückseite mehr als 60 bis über 90 Prozent des
Wirkungsgrads der Vorderseite. Laut IEA-Bericht von 2024 nutzen heute über 90 Prozent der verkauften Module
bifaziale Zellen.</p>
<p><b>Glas-Glas beschreibt den Aufbau:</b> Die Zellen liegen zwischen zwei Glasscheiben statt zwischen Glas
vorne und einer Kunststofffolie hinten (Glas-Folie). Bifaziale Zellen stecken laut IEA meist in Glas-Glas-Modulen
oder in Modulen mit transparenter Rückseitenfolie. Umgekehrt gilt: <b>Nicht jedes Glas-Glas-Modul ist bifazial.</b>
Das Datenblatt des Trina Vertex S+ beschreibt zum Beispiel ein Doppelglas-Modul, weist aber keine Bifazialität
aus. Achten Sie im Angebot deshalb auf beide Angaben: Glas-Glas und bifazial mit Bifazialitätsfaktor.</p>
{A.table(
    ["", "Glas-Folie", "Glas-Glas", "Glas-Glas bifazial"],
    [
        ["Rückseite", "Kunststofffolie, lichtundurchlässig", "Glas", "Glas, Zellen von hinten aktiv"],
        ["Strom von hinten", "nein", "nein", "ja, je nach Bifazialität"],
        ["Typische Garantie (Beispiele*)", "15 Jahre Produkt, 25 Jahre Leistung", "25 Jahre Produkt, 30 Jahre Leistung",
         "25 Jahre Produkt, 30 Jahre Leistung"],
    ],
    hl_cols=(3,),
)}
<p>Beispiele aus den Datenblättern Trina Vertex S (Glas-Folie), Trina Vertex S+ (Doppelglas) und JA Solar
JAM54D41 LB (Glas-Glas bifazial), Stand der jeweiligen Version. Bei {a('photovoltaik', 'Photovoltaikanlagen von EBZ')}
gilt: bis zu 30 Jahre Leistungsgarantie und mindestens 10 Jahre Produktgarantie, je nach Modul.</p>
"""),
        ("Mehrertrag: So viel bringt die Rückseite", "mehrertrag", f"""
<p><b>Der Mehrertrag hängt von zwei Zahlen ab: wie viel Licht die Rückseite erreicht und wie gut sie es
nutzt.</b> Die zweite Zahl heißt Bifazialitätsfaktor und steht im Datenblatt. Beim JA Solar JAM54D41 LB sind es
80 % (± 10 %). Erreicht die Rückseite 10 % der Einstrahlung der Vorderseite, steigt die Leistung laut Datenblatt
von 455 auf 491 Watt, das sind rund 7,9 % mehr.* Als Faustformel: Rückseitenanteil mal Bifazialität, also
10 % × 80 % = 8 %.</p>
<p>Wie viel Licht unten ankommt, bestimmt vor allem die <b>Albedo</b>, das Rückstrahlvermögen des Untergrunds.
Laut IEA PVPS sind Albedo und Bifazialität in der Regel die wichtigsten Faktoren. Der Mehrertrag steigt außerdem
mit dem Anteil an diffusem Licht, der Montagehöhe, dem Reihenabstand und dem Abstand zwischen den Modulen.</p>
{A.table(
    ["Untergrund", "Albedo", "Quelle"],
    [
        ["Neuschnee", "0,80 bis 0,90", "Megasol"],
        ["Sauberer Beton", "rund 0,30", "Megasol"],
        ["Natürlicher Boden, Wiese", "0,2 bis 0,3", "IEA PVPS"],
        ["Asphalt", "rund 0,15", "Megasol"],
    ],
    hl_cols=(1,),
)}
<p>Albedo 0,3 heißt: 30 % des Lichts werden zurückgeworfen. In Feldern mit nachgeführten Modulen über
natürlichem Boden (Albedo 0,2 bis 0,3) liegt der Mehrertrag laut IEA meist <b>unter 10 %</b>, bei Schnee deutlich
höher; der IEA-Bericht von 2024 nennt für solche Anlagen typisch 2 bis 10 %. Der Schweizer Hersteller Megasol nennt je nach Standort und Untergrund 5 bis 35 % Mehrertrag, bei Carports
und Überdachungen bis zu 25 %. Am meisten bringt die Rückseite im Sommer, wenn die Sonne hoch steht; im Winter
liegt mehr Boden im Schatten (IEA).</p>
{A.box("Seriöse Mehrertrag-Prognosen sind schwierig: In einem Vergleich der IEA wichen die Ergebnisse "
       "verschiedener Rechenmodelle für dieselbe Anlage um bis zum Faktor zwei voneinander ab. Rechnen Sie bei "
       "der Wirtschaftlichkeit deshalb zuerst mit der Vorderseite und sehen Sie die Rückseite als Bonus.",
       label="Ehrlich gesagt:")}
"""),
        ("Wann lohnen sich bifaziale Module, wann kaum?", "einsatz", f"""
<p><b>Bifaziale Module lohnen sich dort, wo viel Licht hinter das Modul kommt: aufgeständert, mit Abstand zum
Untergrund und über hellen Flächen.</b> Wo die Rückseite dauerhaft im Schatten liegt, bleibt sie fast wirkungslos.
Megasol nennt als Beispiel ausdrücklich Module, die direkt auf Ziegeln montiert sind.</p>
{A.table(
    ["Montage", "Licht auf der Rückseite", "Einschätzung"],
    [
        ["Flachdach, aufgeständert, heller Belag", "viel, besonders am Rand der Modulfelder",
         "lohnt sich, die IEA nennt flache weiße Dächer ausdrücklich"],
        [f"{a('carport', 'Carport')} oder Überdachung", "viel, Boden und Umgebung reflektieren",
         "lohnt sich, Megasol nennt bis zu 25 %"],
        [f"{a('/photovoltaik-zaun/', 'Solarzaun')}, senkrecht Ost-West", "beide Seiten bekommen direkte Sonne",
         "laut IEA besonders geeignet, Strom über einen längeren Teil des Tages"],
        ["Freifläche mit Schnee im Winter", "sehr viel bei Schnee", "deutlicher Wintervorteil (IEA)"],
        ["Flachdach mit dunkler Bitumenbahn", "wenig, dunkle Flächen reflektieren schwach", "kleiner Bonus"],
        ["Schrägdach, Module dicht über Ziegeln", "fast keines, Rückseite im Schatten", "kaum Mehrertrag"],
    ],
    hl_cols=(2,),
)}
<p>Auf dem Schrägdach wählen wir Glas-Glas-Module deshalb nicht wegen der Rückseite, sondern wegen Haltbarkeit
und Garantie. Ein bifaziales Modul schadet dort nicht, ein Mehrpreis für die Rückseite wäre aber schlecht
investiert. Wie groß die Anlage für Ihren Verbrauch sein sollte, lesen Sie unter
{a('/pv-anlage-kwp-groessen/', 'PV-Anlage: welche kWp-Größe passt')}.</p>
{A.cta("Lohnt sich bifazial auf Ihrem Dach?",
       "Wir sehen uns Dachform, Belag und Verschattung an und sagen ehrlich, ob die Rückseite bei Ihnen etwas "
       "bringt. Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport.",
       secondary=("photovoltaik", "Photovoltaik von EBZ"))}
"""),
        ("Nachteile bifazialer Module", "nachteile", f"""
<p><b>Bifaziale Module haben keine großen Schwächen, aber einige Punkte, die Planung und Kosten betreffen.</b>
Die meisten ergeben sich daraus, dass die Rückseite Licht braucht.</p>
<ul>
  <li><b>Mehr Abstand, weniger Module pro Fläche:</b> Höhere Aufständerung und größere Reihenabstände steigern den
  Rückseitenertrag (IEA). Auf einem Flachdach heißt das: Fläche und Rückseitengewinn gegeneinander abwägen.</li>
  <li><b>Höhere Ströme:</b> Bifaziale Anlagen arbeiten mit höheren Gleichströmen. Leitungen, Sicherungen und
  Wechselrichter müssen laut IEA darauf ausgelegt werden. Beim JA-Solar-Modul steigt der Kurzschlussstrom bei
  10 % Rückseitenlicht von 14,42 auf 15,57 Ampere.</li>
  <li><b>Ungleichmäßiges Licht hinten:</b> Die Rückseite wird viel ungleichmäßiger beleuchtet als die Vorderseite.
  Das führt laut IEA zu kleinen elektrischen Fehlanpassungen im Modul und im Strang.</li>
  <li><b>Schwer vorherzusagen:</b> Der tatsächliche Mehrertrag lässt sich nur grob abschätzen, siehe oben.</li>
  <li><b>Dünneres Glas:</b> Viele aktuelle Glas-Glas-Module haben 2 × 1,6 mm Glas statt 3,2 mm Frontglas. Was das
  für Hagel bedeutet, steht weiter unten.</li>
</ul>
<p>Die Nachteile von Glas-Glas gegenüber Glas-Folie fasst die Stadt Wien knapp zusammen: Glas-Folie-Module sind
im Allgemeinen günstiger und leichter. Beim Gewicht ist der Unterschied mit dünnem Glas heute klein.</p>
"""),
        ("Glas-Glas-Module: Vorteile bei Haltbarkeit, Degradation und Brandschutz", "haltbarkeit", f"""
<p><b>Glas-Glas-Module zeichnen sich laut Stadt Wien (MA 39) durch hohe Tragfähigkeit, guten Widerstand gegen
Witterung, gute Wärmeabfuhr und höhere Langlebigkeit als Glas-Folie-Module aus.</b> Die Hersteller geben das in
der Garantie weiter. Der Vergleich zweier gleich großer Module desselben Herstellers zeigt es:</p>
{A.table(
    ["", "Trina Vertex S (Glas-Folie)", "Trina Vertex S+ (Glas-Glas)", "JA Solar JAM54D41 LB (Glas-Glas bifazial)"],
    [
        ["Glas", "3,2 mm vorne, Folie hinten", "1,6 mm vorne und hinten", "1,6 mm vorne und hinten"],
        ["Gewicht", "21,8 kg", "21,0 kg", "22 kg"],
        ["Produktgarantie", "15 Jahre", "25 Jahre", "25 Jahre"],
        ["Leistungsgarantie", "25 Jahre", "30 Jahre", "30 Jahre"],
        ["Degradation 1. Jahr / danach", "2 % / 0,55 % pro Jahr", "1 % / 0,4 % pro Jahr", "1 % / 0,4 % pro Jahr"],
        ["Garantierte Leistung am Ende", "84,8 % nach 25 Jahren", "87,4 % nach 30 Jahren", "87,4 % nach 30 Jahren"],
    ],
    hl_cols=(2, 3),
)}
<p>Angaben laut Herstellerdatenblättern (Trina Vertex S: Version 2023, Trina Vertex S+: Version 2026, JA Solar:
Version März 2025), alle Module 1.762 × 1.134 mm. Garantiebedingungen unterscheiden sich je nach Markt und
Version, maßgeblich ist das Datenblatt im Angebot.</p>
<p><b>Brandschutz:</b> Die Stadt Wien hat das Brandverhalten von Glas-Glas-Modulen für Fassaden untersucht.
Marktübliche Glas-Glas-Module erreichen danach im Normalfall die Brandverhaltensklasse B nach EN 13501-1,
Glas-Kunststoff-Module D oder schlechter. Die Klasse A2 erreicht kein Modul, weil die Einbettungsfolien zwischen
den Gläsern brennbar sind. In den Versuchen der MA 39 mit Glas-Glas-Modulen an einer hinterlüfteten Fassade gab
es keine Brandweiterleitung und kein Abfallen großer Teile. Für Ihr Dach gilt: Die Klasse hängt am geprüften
Modul, nicht an der Bauweise allein.</p>
"""),
        ("Gewicht, Statik und Hagel", "statik-hagel", f"""
<p><b>Ein Glas-Glas-Modul mit 2 × 1,6 mm Glas wiegt rund 10,5 bis 11 kg pro Quadratmeter, ein vergleichbares
Glas-Folie-Modul rund 10,9 kg.*</b> Der Gewichtsunterschied ist also kaum noch ein Argument. Auf dem Flachdach
wiegt meist der Ballast mehr als die Module: Aufgeständerte Systeme ohne Bohrung werden mit Gewichten gegen Wind
gesichert. Deshalb rechnen wir jede Anlage mit einem Statikreport. Die Datenblätter nennen für die Vorderseite
5.400 Pa Prüflast (Schnee), JA Solar für die Rückseite 2.400 Pa.</p>
<p><b>Hagel:</b> Entscheidend ist die Dicke des Deckglases, nicht ob hinten Glas oder Folie ist. Das
Elementarschaden Präventionszentrum (EPZ) in Linz nennt als Faustregel: 1 Millimeter Deckglas entspricht etwa
1 Zentimeter Hagelkorn. 3 mm Deckglas bedeuten im Regelfall Hagelwiderstandsklasse HW 3 (Hagelkorn 30 mm). Die
im Hagelregister gelisteten Module haben meist rund 3 mm Deckglas. Viele Glas-Glas-Module haben vorne nur
1,6 mm.</p>
{A.box("Prüfen Sie, ob das Modul im Hagelregister (hagelregister.at) mit einer Hagelwiderstandsklasse "
       "eingetragen ist. Für Oberösterreich empfiehlt das EPZ Module ab HW 4 (40 mm), weil diese Hagelkorngröße "
       "dort auf rund 70 % der Landesfläche einmal in der Nutzungszeit zu erwarten ist. Für Ihren Standort in "
       "Kärnten oder der Steiermark klären wir das bei der Planung.",
       label="Hagel-Check:")}
"""),
        ("Kosten: Was kosten bifaziale Module?", "kosten", f"""
<p><b>Beim Modulpreis kosten bifaziale Module heute nicht mehr als andere.</b> Laut PV Index von sun.store lag
der europäische Großhandelspreis im Oktober 2026 für TOPCon-Module bifazial bei durchschnittlich 0,116 € je Watt,
für TOPCon monofazial bei 0,131 € und für Full-Black-Module bei 0,144 €. Für die Module einer 10-kWp-Anlage sind
das rund 1.160 € gegenüber 1.310 € im Großhandel.* Endkundenpreise mit Montage liegen deutlich höher, eine
neutrale Preisübersicht für Österreich gibt es nicht.</p>
<p>Zur Einordnung: Eine 10-kWp-Anlage mit Speicher kostet bei uns rund 15.000 bis 22.000 € vor Förderung. Mehr
als der Modulpreis zählen bei bifazialen Anlagen die Unterkonstruktion, die Aufständerung und der Platz zwischen
den Reihen. Details: {a('/kosten-einer-solaranlage/', 'Kosten einer Solaranlage')}.</p>
{A.table(
    ["Angenommener Mehrertrag", "bei 10.000 kWh Jahresertrag*", "Wert bei Einspeisung (14,874 ct)*",
     "Wert bei Eigenverbrauch (28 bis 35 ct)*"],
    [
        ["3 %", "300 kWh", "rund 45 €", "rund 84 bis 105 €"],
        ["5 %", "500 kWh", "rund 74 €", "rund 140 bis 175 €"],
        ["10 %", "1.000 kWh", "rund 149 €", "rund 280 bis 350 €"],
    ],
    hl_cols=(1,),
)}
<p>Rechenbeispiel pro Jahr mit dem OeMAG-Marktpreis Oktober 2026 und Haushaltsstrompreisen in Kärnten und der
Steiermark laut E-Control (November 2026). Der Marktpreis schwankt jeden Monat, aktuelle Werte unter
{a('marktpreis', 'Marktpreis 2026')}.</p>
"""),
        ("Aus der Praxis: bifaziale Module in EBZ-Projekten", "praxis", f"""
<p>In unseren Referenzprojekten verbauen wir durchwegs Glas-Glas-Module, bifazial. Drei Beispiele zeigen, wie
unterschiedlich die Rückseite dabei zum Zug kommt:</p>
<ul>
  <li><b>{a('/referenzen/projekt-flachdach-in-graz/', 'Flachdach in Graz')}:</b> 11,83 kWp in Südausrichtung auf
  einem hellen Sarnafil-Flachdach, ballastiert ohne eine einzige Bohrung, mit 20-kWh-Speicher und 11-kW-Wallbox.
  Rund 13.000 kWh im Jahr, rund 3.500 € Ersparnis pro Jahr*. Das helle Dach reflektiert Licht auf die Rückseite.</li>
  <li><b>{a('/referenzen/projekt-stadthaus-in-graz/', 'Stadthaus in Graz')}:</b> 18 kWp auf drei Flachdächern
  in Süd- und Ostausrichtung, aufgeständert und mit Betongewichten ballastiert, ohne Dachdurchdringung. Dazu
  18 kWh Speicher, Wallbox und Notstrom. Rund 20.000 kWh im Jahr, Amortisation in etwa 4 Jahren*.</li>
  <li><b>{a('/referenzen/projekt-pv-anlage-hotel-villach/', 'Hotel in Villach/Warmbad')}:</b> 13 kWp in
  Südausrichtung mit zwei Neigungswinkeln, aufgeständert auf einem Bitumen-Flachdach, 27-kWh-Speicher und
  automatischer Notstrom. Rund 15.000 kWh im Jahr, rund 4.200 € Ersparnis pro Jahr*. Die dunkle Bitumenbahn
  reflektiert weniger als ein heller Belag, hier zählen vor allem Haltbarkeit und Garantie.</li>
</ul>
<p>Einen eigenen Mehrertrag der Rückseite haben wir bei diesen Anlagen nicht getrennt gemessen. Alle Projekte
finden Sie unter {a('referenzen', 'Referenzen')}.</p>
"""),
        ("Fazit: Glas-Glas immer, bifazial dort, wo Licht hinkommt", "fazit", f"""
<p>Glas-Glas-Module sind heute kaum schwerer als Glas-Folie-Module, haben längere Garantien und laut Datenblatt
eine geringere jährliche Degradation. Die Bifazialität ist ein Bonus, der auf dem Ziegeldach wenig, auf einem
hellen Flachdach, am Carport, am Zaun oder bei Schnee aber spürbar bringt. Wer das Modul auswählt, sollte
zusätzlich auf Bifazialitätsfaktor, Deckglasdicke und Eintrag im Hagelregister achten.</p>
<p><small>*Richtwerte und eigene Berechnungen auf Basis der genannten Quellen: Mehrleistung laut Datenblatt bei
10 % Rückseitenlicht, Gewicht je m² aus Modulgewicht und Modulfläche, Großhandelspreise Europa (sun.store PV Index
Oktober 2026) ohne Montage und Steuern, Mehrertrag-Beispiele angenommen. Energiepreise Stand November 2026,
OeMAG-Marktpreis Oktober 2026; die Werte ändern sich laufend. Referenzwerte laut Projektdaten, Stand Oktober
2026.</small></p>
{A.cta("Module, die zu Ihrem Dach passen",
       "Wir wählen Module nach Dach, Untergrund und Hagelzone aus und rechnen ehrlich, was die Rückseite bei "
       "Ihnen bringt.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("referenzen", "Referenzen ansehen"))}
"""),
    ],

    "partner": {
        "h2": "Photovoltaik mit Glas-Glas-Modulen aus einer Hand",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie plant und installiert Photovoltaik, Batteriespeicher und Energiemanagement in Kärnten "
                 "und der Steiermark, mit zertifizierten Fachkräften und einem festen Ansprechpartner von der "
                 "Planung bis zur Übergabe. Wir setzen Glas-Glas-Module ein und planen Aufständerung, Ballast und "
                 "Statik so, dass die Anlage zu Ihrem Dach passt."),
        "grid": [
            ("Ehrliche Einschätzung", "Bifazial nur dort, wo die Rückseite Licht bekommt."),
            ("Statik geprüft", "Projektbericht mit 3D-Belegplan und Statikreport."),
            ("Lange Garantie", "Bis zu 30 Jahre Leistungsgarantie auf die Module."),
            ("300+ Projekte", "Dokumentierte Referenzen in 6 Bundesländern."),
        ],
    },

    "faq": [
        ("Was sind bifaziale Module?",
         "Bifaziale Module wandeln Licht auf beiden Seiten in Strom um, vorne direktes Sonnenlicht, hinten "
         "reflektiertes und gestreutes Licht. Die Rückseite erreicht je nach Zelltechnik mehr als 60 bis über 90 "
         "Prozent des Wirkungsgrads der Vorderseite. Meist stecken die Zellen in Glas-Glas-Modulen."),
        ("Wie viel Mehrertrag bringen bifaziale Module?",
         "Das hängt vor allem vom Untergrund und von der Montage ab. Über natürlichem Boden liegt der Mehrertrag "
         "laut IEA meist unter 10 %, bei Schnee deutlich darüber. Der Hersteller Megasol nennt je nach Standort 5 "
         "bis 35 %, bei Carports bis zu 25 %. Ein Modul mit 80 % Bifazialität leistet bei 10 % Rückseitenlicht "
         "rund 8 % mehr."),
        ("Lohnen sich bifaziale Module auf dem Ziegeldach?",
         "Kaum: Liegen die Module dicht über den Ziegeln, bleibt die Rückseite im Schatten und erzeugt fast keinen "
         "zusätzlichen Strom. Glas-Glas-Module lohnen sich dort trotzdem wegen längerer Garantie und geringerer "
         "Degradation. Für die Rückseite allein sollten Sie auf dem Schrägdach keinen Aufpreis zahlen."),
        ("Welche Nachteile haben bifaziale Module?",
         "Sie brauchen Abstand zum Untergrund und Platz zwischen den Reihen, damit Licht nach hinten kommt. Die "
         "Anlage arbeitet mit höheren Strömen, das muss bei Leitungen und Wechselrichter berücksichtigt werden. "
         "Der tatsächliche Mehrertrag ist schwer vorherzusagen: Rechenmodelle weichen laut IEA bis zum Faktor zwei "
         "voneinander ab."),
        ("Sind Glas-Glas-Module schwerer als Glas-Folie-Module?",
         "Kaum noch. Mit 2 × 1,6 mm Glas wiegt etwa der Trina Vertex S+ 21,0 kg, das gleich große Glas-Folie-Modul "
         "Vertex S mit 3,2 mm Frontglas 21,8 kg. Das sind rund 10,5 bis 11 kg pro Quadratmeter. Auf dem Flachdach "
         "wiegt meist der Ballast mehr als die Module."),
        ("Sind Glas-Glas-Module hagelsicherer?",
         "Nicht automatisch. Laut EPZ Linz entscheidet die Dicke des Deckglases: 1 mm entspricht etwa 1 cm "
         "Hagelkorn, 3 mm bedeuten meist Klasse HW 3. Viele Glas-Glas-Module haben vorne nur 1,6 mm Glas. Prüfen Sie "
         "deshalb den Eintrag im Hagelregister."),
        ("Kosten bifaziale Module mehr?",
         "Beim Modul kaum: Im Oktober 2026 kosteten bifaziale TOPCon-Module im europäischen Großhandel "
         "durchschnittlich 0,116 € je Watt, monofaziale 0,131 € (sun.store PV Index). Mehrkosten entstehen eher "
         "durch Aufständerung und größere Reihenabstände auf dem Flachdach."),
        ("Bringen bifaziale Module im Winter bei Schnee mehr?",
         "Ja, Neuschnee reflektiert 80 bis 90 Prozent des Lichts, die Rückseite bekommt dann deutlich mehr ab. "
         "Über das Jahr bringt die Rückseite laut IEA aber im Sommer am meisten, weil im Winter durch den tiefen "
         "Sonnenstand mehr Boden im Schatten liegt."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Mit zertifizierten Fachkräften plant und "
                    "installiert EBZ Energie Photovoltaikanlagen mit Glas-Glas-Modulen in Kärnten und der "
                    "Steiermark, auf Ziegel-, Blech- und Flachdächern. Herstellerangaben stammen aus den genannten "
                    "Datenblättern, Rechnungen in diesem Ratgeber sind Richtwerte."),
    "sources": [
        ("IEA PVPS Task 13: Bifacial Photovoltaic Modules and Systems, Executive Summary (2021)",
         "https://iea-pvps.org/wp-content/uploads/2021/04/IEA-PVPS-T13-14_2021-Bifacial-Photovoltaic-Modules-and-Systems-executive-summary.pdf"),
        ("IEA PVPS Task 13: Bifacial Tracking Systems, Executive Summary (2024)",
         "https://iea-pvps.org/wp-content/uploads/2024/08/IEA-PVPS-T13-26_2024-EXEC-SUMM-Bifacial-Tracking-Systems.pdf"),
        ("Megasol (Schweiz): Bifaziale Module, das zweite Gesicht",
         "https://megasol.ch/bifacial-module-das-zweite-gesicht/"),
        ("JA Solar: Datenblatt JAM54D41 LB (Global EN, März 2025)",
         "https://portal.segen.co.uk/reseller/docs/JAM54D41%20430-455%20LB%20Global_EN_20250303A.pdf"),
        ("Trina Solar: Datenblatt Vertex S+ NEG9R.28 (DE 2026)",
         "https://www-cdn.trinasolar.com/wwwstorage/sites/8/260227_Datasheet_Vertex-S_NEG9R.28_DE_2026_A_web.pdf"),
        ("Trina Solar: Datenblatt Vertex S DE09R.08 (FR 2023)",
         "https://res.cloudinary.com/sonepar-fr/raw/upload/s--ovdcmkeS--/v1/documents/8163/Datasheet_VertexS_DE09R.08_EU_FR_2023_A.pdf"),
        ("Stadt Wien, MA 39: Brandverhalten von Glas-Glas-PV-Modulen (2023)",
         "https://www.wien.gv.at/pdf/ma39/brandverhalten-glas-glas-pv-module.pdf"),
        ("Hans Starl, EPZ Linz: PV-Anlagen vor Hagel schützen (Schadenprisma 2/2023, Deutschland)",
         "https://www.schadenprisma.de/wp-content/uploads/pdf/2/sp_2_2023_art4.pdf"),
        ("Hagelregister Österreich", "https://www.hagelregister.at/"),
        ("PV Tech: European solar module and inverter prices rose in October (November 2026)",
         "https://www.pv-tech.org/european-solar-module-and-inverter-prices-rose-in-october/"),
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/de/marktpreis/"),
        ("E-Control: Strom- und Gaspreismonitor November 2026", "https://www.e-control.at/preismonitor"),
    ],
    "related": [
        ("photovoltaik", "Photovoltaik von EBZ: Planung und Montage"),
        ("carport", "Photovoltaik-Carport mit bifazialen Modulen"),
        ("/photovoltaik-zaun/", "Photovoltaik-Zaun: Strom vom Gartenzaun"),
        ("referenzen", "Referenzen: über 300 Projekte"),
    ],
    "cta": {
        "h3": "Welche Module passen zu Ihrem Dach?",
        "text": "Wir prüfen Dach, Untergrund und Statik und sagen ehrlich, ob sich bifaziale Module lohnen.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Glas-Glas-Module, ehrlich geplant",
    "final_text": ("Kostenlose Erstberatung zu Photovoltaik, Modulwahl, Speicher und Statik, mit transparenten "
                   "Zahlen und einem Ansprechpartner aus Villach."),
}
