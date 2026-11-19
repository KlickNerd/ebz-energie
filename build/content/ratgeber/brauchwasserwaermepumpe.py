"""Ratgeber: Brauchwasserwärmepumpe (Warmwasser-Wärmepumpe, Wärmepumpenboiler).

Neuer Artikel (kein WordPress-Vorgänger), erstellt 2026-11-19.
Ziel-Keywords (Google Ads, Österreich/Deutsch, 19.11.2026): brauchwasserwärmepumpe 1.600,
warmwasser wärmepumpe 1.300, wärmepumpe für warmwasser 1.300, wärmepumpenboiler 390,
warmwasserwärmepumpe 140, brauchwasserwärmepumpe 200 liter 110, brauchwasserwärmepumpe förderung
(österreich) 40 bis 50, brauchwasserwärmepumpe kosten / stromverbrauch / lautstärke je 10.
People also ask: Wie viel kW braucht eine Brauchwasserwärmepumpe? Kombination mit Wärmepumpe?
Ist Brauchwasser gleich Warmwasser? Wie schnell heizt eine Brauchwasserwärmepumpe?

Faktenbasis (alle am 19.11.2026 selbst geöffnet): Energieinstitut Vorarlberg (Preis 3.000 bis 4.000 €,
Tausch an einem Tag, bis zu 75 %), Stiftung Warentest 06/2026 (DE: 2.400 bis 3.400 € Gerät, Raum ab 20 m³,
R290), Verbraucherzentrale 01/2026 (DE: JAZ 2,5 bis 4, Aufstellraum), Bosch Home Comfort Österreich
(4 Personen 2.400 bis 3.200 kWh Wärme, 260 l), Stiebel Eltron Datenblatt WWK 222/302 (COP A20, Schall),
Austria Email Prospekt Explorer Evo 3 V03/26 (COP A7/A14/A20, 600 W, Aufheizzeit, AEC, Einsatzgrenzen,
Legionellenfunktion) und Produktseite AE Revolution Evo 3, BFE Schweiz 2014 (COP je Zapfprofil),
Förderung: BMLUK Kesseltausch (Start 2.11.2026), Biomasse-Verband Übersicht Landesförderung Kärnten
2026 bis 2028, Steiermark Richtlinie Heizungstausch 2026, Klimafonds EMS-Leitfaden 2026.
Energiepreise, OeMAG, Heizöl, Nutzungsgrade und Legionellen aus der Recherche zu /warmwasser-mit-photovoltaik/
(E-Control Nov 2026, OeMAG Okt 2026, WKO, Statistik Austria, NÖ Landesregierung).
Eigene Rechnungen: Betriebskosten = 2.400 kWh Wärme / Nutzungsgrad bzw. JAZ x Energiepreis.
Nicht belegt und daher nicht behauptet: österreichische Einbaukosten-Spanne, eigene Förderung für
Brauchwasserwärmepumpen (Bund, Kärnten, Steiermark), Kelag-Prämie für Warmwasser-Wärmepumpen, Lebensdauer.
ktn.gv.at war nicht erreichbar (Verbindung abgelehnt).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "brauchwasserwaermepumpe",
    "path": "/brauchwasserwaermepumpe/",
    "cluster": "Wärmepumpe und Heizen",
    "title": "Brauchwasserwärmepumpe: Kosten, Verbrauch, Förderung | EBZ",
    "description": ("Brauchwasserwärmepumpe: rund 3.000 bis 4.000 €, braucht rund ein Drittel des Stroms eines "
                    "Elektroboilers. Betriebskosten, Aufstellraum, PV und Förderung 2026."),
    "eyebrow": "Warmwasser · Brauchwasserwärmepumpe",
    "crumb_label": "Brauchwasserwärmepumpe",
    "h1": "Brauchwasserwärmepumpe: Warmwasser mit rund einem Drittel des Stroms eines Elektroboilers",
    "lead": ("Eine Brauchwasserwärmepumpe, auch Warmwasser-Wärmepumpe oder Wärmepumpenboiler genannt, holt "
             "Wärme aus der Raumluft und macht aus 1 kWh Strom rund 2,5 bis 4 kWh Wärme. Dieser Ratgeber zeigt "
             "mit österreichischen Energiepreisen, was das Gerät kostet, was es im Jahr spart, welcher Raum "
             "passt und wie es mit Photovoltaik zusammenarbeitet."),
    "chips": [
        "Anschaffung: <b>rund 3.000 bis 4.000 €</b>",
        "Effizienz: <b>JAZ 2,5 bis 4</b>",
        "4-Personen-Haushalt: <b>rund 800 kWh Strom</b>*",
        "Aufstellraum: <b>ab 20 m³</b>",
    ],
    "date_published": "2026-11-19",
    "date_modified": "2026-11-19",
    "hero_img": "waermepumpe",
    "hero_alt": "Außeneinheit einer Luft-Wasser-Wärmepumpe vor einer Holzwand im Garten eines Wohnhauses",

    "tldr": [
        "Eine Brauchwasserwärmepumpe erwärmt nur das Trinkwarmwasser, nicht die Heizung. Sie kostet laut "
        "Energieinstitut Vorarlberg rund 3.000 bis 4.000 Euro, der Tausch ist bei guten Voraussetzungen an "
        "einem Tag erledigt.",
        "Für einen 4-Personen-Haushalt mit rund 2.400 kWh Wärmebedarf fürs Warmwasser braucht sie bei einer "
        "Jahresarbeitszahl von 3 rund 800 kWh Strom, also rund 260 Euro im Jahr statt rund 780 Euro mit dem "
        "Elektroboiler.*",
        "Gegenüber Heizöl spart sie rund 240 Euro im Jahr, gegenüber Gas kaum etwas.* Am meisten lohnt sie "
        "sich als Ersatz für einen Elektroboiler.",
        "Der Aufstellraum sollte frostfrei sein und mindestens 20 m³ haben. Das Gerät kühlt und entfeuchtet "
        "ihn. Die Datenblätter nennen rund 45 bis 47 dB(A).",
        "Mit PV-Funktion nutzt sie Sonnenstrom gezielt: Die Wärmepumpe braucht nur rund 600 W. Eine eigene "
        "Förderung für Brauchwasserwärmepumpen ist uns für 2026 weder vom Bund noch von Kärnten oder der "
        "Steiermark bekannt.",
    ],
    "kpis": [
        ("2,5 bis 4", "Jahresarbeitszahl (kWh Wärme je kWh Strom)"),
        ("3.000 bis 4.000 €", "Anschaffung laut Energieinstitut Vorarlberg"),
        ("rund 520 €", "Ersparnis pro Jahr gegenüber Elektroboiler*"),
        ("ab 20 m³", "Aufstellraum, frostfrei"),
    ],

    "sections": [
        ("Was ist eine Brauchwasserwärmepumpe?", "funktion", f"""
<p><b>Eine Brauchwasserwärmepumpe ist ein Warmwasserspeicher mit eingebauter Luft-Wärmepumpe. Sie entzieht
der Luft im Aufstellraum Wärme und hebt sie mit einem Kältekreis auf Warmwassertemperatur.</b> Brauchwasser
meint das Trinkwarmwasser für Dusche, Bad und Küche. Die Heizung unterstützt das Gerät nicht, es ist ein
reiner Ersatz für Elektroboiler oder die Warmwasserbereitung über den Heizkessel.</p>
<p>Im Gerät stecken Ventilator, Verdampfer, Kompressor und Kondensator, darunter ein Speicher mit meist 200
bis 300 Litern. Bosch nennt 260 Liter als typische Größe für einen 4-Personen-Haushalt, die Geräte im Test
der Stiftung Warentest (Juni 2026) haben 260 bis 300 Liter für drei bis fünf Personen und arbeiten alle mit
dem Kältemittel R290 (Propan). Ein eingebauter Heizstab dient als Zusatz- und Notheizung.</p>
{A.table(
    ["", "Elektroboiler", "Brauchwasserwärmepumpe"],
    [
        ["Wärmequelle", "nur Strom", "Raum- oder Außenluft plus Strom"],
        ["Aus 1 kWh Strom", "knapp 1 kWh Wärme", "rund 2,5 bis 4 kWh Wärme"],
        ["Platz", "Wandboiler", "Standgerät, etwa wie ein großer Kühlschrank"],
        ["Anschaffung", "gering", "rund 3.000 bis 4.000 €"],
    ],
    hl_cols=(2,),
)}
<p>Wie eine Wärmepumpe grundsätzlich arbeitet, erklärt {a('/funktionsweise-einer-waermepumpe/', 'Funktionsweise einer Wärmepumpe')}.
Für Heizung und Warmwasser gemeinsam ist eine {a('waermepumpe', 'Heizungswärmepumpe')}
die passende Lösung.</p>
"""),
        ("Effizienz: COP nach EN 16147 und Jahresarbeitszahl", "effizienz", f"""
<p><b>Der COP im Datenblatt wird nach der Norm EN 16147 im Labor gemessen, und zwar bei einer festgelegten
Lufttemperatur und einem festgelegten Zapfprofil. Die Jahresarbeitszahl (JAZ) beschreibt, was im Alltag
übers Jahr herauskommt: laut Verbraucherzentrale typischerweise 2,5 bis 4.</b> Eine JAZ von 3 heißt: Aus 1 kWh
Strom werden 3 kWh Wärme.</p>
<p>Wie stark die Lufttemperatur den COP verändert, zeigt das Datenblatt der Austria Email Explorer Evo 3
(Hersteller aus Knittelfeld):</p>
{A.table(
    ["Modell", "COP bei 7 °C Luft", "bei 14 °C", "bei 20 °C"],
    [
        ["Explorer Evo 3, 200 Liter", "3,18", "3,54", "3,63"],
        ["Explorer Evo 3, 270 Liter", "3,46", "3,78", "3,99"],
    ],
    hl_cols=(1,),
)}
<p>Angaben laut Herstellerprospekt (Stand 03/2026), gemessen nach EN 16147. Stiebel Eltron gibt für die WWK 302
einen COP von 2,91 bei 20 °C Luft und Zapfprofil XL an. <b>Vergleichen Sie deshalb nur Werte mit gleicher
Lufttemperatur</b> (A7, A14, A20 im Datenblatt).</p>
{A.box("Wenig Warmwasser bedeutet weniger Effizienz. In Labormessungen des Schweizer Bundesamts für Energie "
       "(2014) kam eine 270-Liter-Brauchwasserwärmepumpe bei kleinem Zapfprofil (2,1 kWh am Tag) nur auf einen "
       "COP von 1,50, beim großen Profil (19,1 kWh) auf 2,98. Auch ein 300-Liter-Elektroboiler schaffte wegen "
       "der Speicherverluste nur 0,68 bis 0,94. Der Speicher sollte also zum Verbrauch passen.",
       label="Gut zu wissen:")}
"""),
        ("Was kostet eine Brauchwasserwärmepumpe?", "kosten", f"""
<p><b>Das Energieinstitut Vorarlberg nennt für einen Wärmepumpenboiler rund 3.000 bis 4.000 Euro.</b> Die
Stiftung Warentest (Deutschland, Juni 2026) hat Gerätepreise von rund 2.400 bis 3.400 Euro ermittelt,
zuzüglich Einbau. Eine neutrale österreichische Preisübersicht für den Einbau gibt es nicht. Bei guten
Voraussetzungen ist der Tausch laut Energieinstitut an einem Tag erledigt.</p>
<p>Was den Einbaupreis bestimmt:</p>
<ul>
  <li><b>Einbringung:</b> Die Geräte sind rund 1,5 bis 1,9 Meter hoch und wiegen leer rund 85 bis 135 kg
  (Austria Email, Stiebel Eltron). Enge Kellerstiegen kosten Zeit.</li>
  <li><b>Luftführung:</b> Im Umluftbetrieb reicht der Raum, für Abluft oder Außenluft kommen Luftkanäle dazu
  (Anschluss zum Beispiel 160 mm bei Austria Email).</li>
  <li><b>Anschlüsse:</b> Kalt- und Warmwasser, gegebenenfalls Zirkulation, ein Kondensatablauf und ein
  230-V-Anschluss.</li>
  <li><b>Alter Boiler:</b> Demontage und Entsorgung des Elektroboilers oder Anpassung am Heizkessel.</li>
</ul>
<p>Was eine komplette {a('/kosten-einer-waermepumpe/', 'Heizungswärmepumpe kostet')}, lesen Sie im eigenen
Ratgeber. Den genauen Preis für Ihre Brauchwasserwärmepumpe nennen wir nach der Besichtigung.</p>
"""),
        ("Stromverbrauch und Betriebskosten im Vergleich", "betriebskosten", f"""
<p><b>Ein 4-Personen-Haushalt braucht laut Bosch rund 2.400 bis 3.200 kWh Wärme im Jahr fürs Warmwasser.
Bei einer Jahresarbeitszahl von 3 sind das rund 800 bis 1.100 kWh Strom.</b> Die Herstellerangabe für den
jährlichen Stromverbrauch nach EU-Energielabel liegt bei der Explorer Evo 3 zwischen 682 kWh (200 Liter,
Zapfprofil L) und 1.058 kWh (270 Liter, Zapfprofil XL).</p>
<p>Was das in Euro bedeutet, zeigt ein Beispiel mit 2.400 kWh Wärme pro Jahr und österreichischen Preisen
vom November 2026:</p>
{A.table(
    ["Warmwasser mit", "Energie pro Jahr*", "Kosten pro Jahr*"],
    [
        ["Elektroboiler (Strom 32 ct)", "rund 2.450 kWh Strom", "rund 780 €"],
        ["Heizöl (1,788 € je Liter)", "rund 2.760 kWh Heizöl", "rund 490 €"],
        ["Erdgas (13,1 ct, Kelag)", "rund 2.620 kWh Gas", "rund 340 €"],
        ["Brauchwasserwärmepumpe, JAZ 3", "rund 800 kWh Strom", "rund 260 €"],
        ["Brauchwasserwärmepumpe, JAZ 2,5", "rund 960 kWh Strom", "rund 310 €"],
        ["Brauchwasserwärmepumpe, JAZ 3, Hälfte aus PV-Überschuss", "rund 800 kWh Strom", "rund 190 €"],
    ],
    hl_cols=(2,),
)}
<p>Rechenweg: Strom 32 ct je kWh (Durchschnittspreis inkl. Netz und Abgaben laut E-Control-Preismonitor
November 2026: Energie Steiermark rund 31,9 ct, Kelag rund 33,2 ct), Nutzungsgrade laut Statistik Austria
(Strom 98 %, Gas 91,5 %, Heizöl 86,9 %), Heizöl mit 10 kWh je Liter. PV-Strom ist mit der entgangenen
Einspeisung bewertet (OeMAG-Marktpreis Oktober 2026: 14,874 ct).</p>
{A.box("Gegenüber dem Elektroboiler spart die Brauchwasserwärmepumpe im Beispiel rund 520 Euro im Jahr. Bei "
       "3.000 bis 4.000 Euro Anschaffung sind das rechnerisch rund 6 bis 8 Jahre.* Gegenüber Heizöl sind es "
       "rund 240 Euro im Jahr, gegenüber Gas nur rund 90 Euro. Ein Kessel, der im Sommer nur fürs Warmwasser "
       "anspringt, arbeitet allerdings oft schlechter als im Modell angenommen.",
       label="Das Ergebnis:")}
"""),
        ("Aufstellraum: Umluft, Abluft oder Außenluft", "aufstellung", f"""
<p><b>Ideal ist ein unbeheizter, aber frostfreier Raum wie der Heizraum oder ein Kellerraum mit mindestens
20 m³ Volumen</b> (Verbraucherzentrale, Stiftung Warentest). Das Gerät kühlt und entfeuchtet den Raum, im
Winter kann es laut Energieinstitut Vorarlberg die Abwärme im Heizraum nutzen. Im beheizten Wohnraum
würde es dagegen Wärme entziehen, die vorher die Heizung erzeugt hat.</p>
{A.table(
    ["Betriebsart", "Luft kommt aus", "Worauf achten"],
    [
        ["Umluft", "dem Aufstellraum", "Raum ab 20 m³, Lufttemperatur laut Datenblatt (Austria Email: ab +5 °C)"],
        ["Abluft", "einer Lüftungsanlage, Bad oder Küche", "Luftkanäle, nutzt Abwärme des Hauses"],
        ["Außenluft (Kanalbetrieb)", "draußen, über zwei Luftkanäle", "läuft bis -5 °C, im Winter niedrigerer COP"],
    ],
    hl_cols=(0,),
)}
<p>Einsatzgrenzen laut Herstellern: Austria Email Explorer Evo 3 im Umluftbetrieb +5 bis +43 °C, im
Kanalbetrieb -5 bis +43 °C; Stiebel Eltron WWK -5 bis +42 °C. Für die Umluft-Variante nennt Austria Email
eine Mindestraumhöhe von rund 1,82 bis 2,01 Metern. Weil das Gerät Feuchtigkeit aus der Luft holt, braucht
es einen Kondensatablauf.</p>
<h3>Wie laut ist eine Brauchwasserwärmepumpe?</h3>
<p>Stiebel Eltron gibt für die WWK 222 und 302 einen mittleren Schalldruck von 45 dB(A) in einem Meter
Abstand an, die Schallleistung nach EN 12102 beträgt 56 dB(A). Austria Email nennt für die Explorer Evo 3
eine Schallleistung von 47 dB(A) im Kanalbetrieb. Vergleichen Sie nur gleiche Größen: Schalldruck in einem
Meter Abstand und Schallleistung sind unterschiedliche Werte. Den Aufstellort neben einem Schlafzimmer
planen wir deshalb mit Abstand oder Luftkanal.</p>
"""),
        ("Brauchwasserwärmepumpe mit Photovoltaik: PV-Eingang und SG Ready", "photovoltaik", f"""
<p><b>Mit einer PV-Anlage läuft die Brauchwasserwärmepumpe bevorzugt dann, wenn Sonnenstrom übrig ist.</b>
Viele Modelle sind laut Stiftung Warentest PV-kompatibel. Bei der Explorer Evo 3 hebt die integrierte
PV-Funktion die Solltemperatur an, wenn Überschuss da ist, auf Wunsch auch mit dem eingebauten Heizstab.
Stiebel Eltron liefert die WWK serienmäßig mit PV-Anschlussmöglichkeit.</p>
<ul>
  <li><b>Kleine Leistung, früher Start:</b> Die Wärmepumpe der Explorer Evo 3 nimmt maximal 600 W auf, der
  Zusatzheizstab 1.200 W. Für den Wärmepumpenbetrieb reicht also schon ein kleiner Überschuss.</li>
  <li><b>Wärme speichern statt einspeisen:</b> Der Speicher wird mittags auf eine höhere Temperatur geladen,
  am Abend ist das Wasser warm. Im Beispiel oben sinken die Kosten so von rund 260 auf rund 190 Euro im
  Jahr.*</li>
  <li><b>Ansteuerung:</b> Je nach Modell über einen PV-Eingang oder SG Ready. Fronius beschreibt zum Beispiel,
  wie der Ohmpilot eine Wärmepumpe mit SG-Ready-Eingang bei Überschuss in den verstärkten Betrieb schaltet.
  Ein {a('ems', 'Energiemanagementsystem')} verteilt den Überschuss auf Speicher, Wallbox und Warmwasser.</li>
</ul>
<p>Die günstigere Alternative im bestehenden Boiler ist ein Heizstab mit PV-Regler. Er macht aus 1 kWh Strom
aber nur 1 kWh Wärme. Den Vergleich mit Rechnung finden Sie unter
{a('/warmwasser-mit-photovoltaik/', 'Warmwasser mit Photovoltaik')}. Heizen Sie mit einer Wärmepumpe, lesen
Sie {a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}.</p>
{A.cta("Passt eine Brauchwasserwärmepumpe zu Ihrem Haus?",
       "Wir sehen uns Aufstellraum, Warmwasserbedarf und Ihre Photovoltaik an und rechnen ehrlich durch, ob "
       "Wärmepumpenboiler, Heizstab oder Energiemanagement mehr bringt.",
       secondary=("photovoltaik", "Photovoltaik von EBZ"))}
"""),
        ("Legionellen und Warmwassertemperatur", "hygiene", f"""
<p><b>Legionellen vermehren sich bevorzugt zwischen 25 und 45 °C, erst über 60 °C sterben sie ab</b>
(Infoblatt der NÖ Landesregierung mit Verweis auf ÖNORM B 5019). Das Energieinstitut Vorarlberg nennt 60 °C
im Speicher, im Einfamilienhaus mit regelmäßigem Verbrauch seien Legionellen in der Regel kein Problem.
Ansteckend ist nur eingeatmeter Wassernebel, etwa beim Duschen, nicht das Trinken.</p>
<ul>
  <li><b>Wärmepumpe allein:</b> Die Explorer Evo 3 erreicht im Wärmepumpenbetrieb 45 bis 62 °C, die Stiebel
  Eltron WWK bis 65 °C.</li>
  <li><b>Legionellenprogramm:</b> Austria Email bietet wahlweise 62, 65 oder 70 °C, dafür hilft der Heizstab
  mit. Die Stiftung Warentest empfiehlt den Hygienemodus etwa einmal pro Woche.</li>
  <li><b>Effizienz:</b> Je höher die Temperatur, desto niedriger der COP und desto höher die
  Speicherverluste. Mit PV-Überschuss ist die Aufheizung auf 60 °C und mehr günstig.</li>
</ul>
"""),
        ("Förderung 2026: was es gibt und was nicht", "foerderung", f"""
<p><b>Eine eigene Förderung für Brauchwasserwärmepumpen ist uns für 2026 weder vom Bund noch vom Land Kärnten
oder der Steiermark bekannt</b> (Stand 19. November 2026).</p>
<ul>
  <li><b>Bund, Kesseltausch:</b> Seit 2. November 2026 läuft die Aktion wieder (Wärmepumpe 5.000 Euro). Sie
  fördert den Austausch einer fossilen Heizung. Eine Wärmepumpe nur fürs Warmwasser ersetzt die Heizung
  nicht und wird nicht genannt. Mehr dazu: {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive')}.</li>
  <li><b>Kärnten:</b> Die Landesförderung für energieeffiziente Haustechnikanlagen (gültig 2026 bis 2028)
  zahlt 3.000 Euro für den Heizungstausch und 1.500 Euro für eine thermische Solaranlage ab 6 m².
  Warmwasser-Wärmepumpen kommen in der Übersicht nicht vor.</li>
  <li><b>Steiermark:</b> Die Richtlinie zum Tausch erneuerbar betriebener Heizungssysteme 2026 nennt
  Brauchwasser-Wärmepumpen nicht, für neue Wärmepumpen nimmt das Land derzeit keine Anträge an.</li>
  <li><b>EMS-Förderung des Klimafonds:</b> 50 % der Kosten, höchstens 600 Euro, für ein
  Energiemanagementsystem, das mindestens zwei Komponenten steuert. "Wärmepumpe/elektrische
  Warmwasseraufbereitung in Verbindung mit Warmwasserspeicher" zählt dazu, aber nur in bestimmten
  Kombinationen, etwa mit Batteriespeicher oder Ladestelle. Gefördert wird das EMS, nicht das Gerät.
  Details: {a('/ems-foerderung/', 'EMS-Förderung 2026')}.</li>
</ul>
<p>Fragen Sie zusätzlich bei Ihrer Gemeinde nach. Alle aktuellen Programme für Photovoltaik, Speicher und
Wärmepumpe finden Sie unter {a('foerderungen', 'Förderungen 2026')} und
{a('/landesfoerderungen-fuer-die-waermepumpe/', 'Landesförderungen für die Wärmepumpe')}.</p>
"""),
        ("Wann sich der Tausch lohnt: Fazit", "fazit", f"""
<p><b>Am deutlichsten lohnt sich eine Brauchwasserwärmepumpe als Ersatz für einen Elektroboiler:</b> Im
Beispiel sinken die Warmwasserkosten um rund zwei Drittel, die Anschaffung ist rechnerisch nach rund 6 bis 8
Jahren wieder drin.* Mit Photovoltaik wird es noch günstiger, weil die Wärmepumpe mit wenigen hundert Watt
Überschuss läuft.</p>
<ul>
  <li><b>Lohnt sich meist:</b> alter Elektroboiler, PV-Anlage vorhanden, frostfreier Keller- oder Heizraum
  ab 20 m³.</li>
  <li><b>Lohnt sich teilweise:</b> Ölkessel, der im Sommer nur fürs Warmwasser läuft. Der Kessel kann dann
  ruhen, die reine Energieersparnis beträgt im Beispiel rund 240 Euro im Jahr.</li>
  <li><b>Lohnt sich kaum:</b> Gaskessel mit niedrigem Gaspreis oder ein Haus, das ohnehin bald eine
  Heizungswärmepumpe bekommt. Dann übernimmt diese meist auch das Warmwasser.</li>
</ul>
<p><small>*Richtwerte und eigene Berechnungen auf Basis der genannten Quellen: 2.400 kWh Wärme pro Jahr,
Energiepreise Stand November 2026, OeMAG-Marktpreis Oktober 2026, Nutzungsgrade laut Statistik Austria,
ohne Einbaukosten, Wartung, Grundgebühren und Förderung. Preise aus Deutschland sind als solche gekennzeichnet.
Die tatsächlichen Werte hängen von Verbrauch, Gerät und Aufstellraum ab.</small></p>
{A.cta("Warmwasser effizient und mit Sonnenstrom",
       "Kostenlose Beratung zu Brauchwasserwärmepumpe, Photovoltaik und Energiemanagement, mit Ihren "
       "Verbrauchswerten gerechnet.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("waermepumpe", "Wärmepumpe von EBZ"))}
"""),
    ],

    "partner": {
        "h2": "Warmwasser, Photovoltaik und Wärmepumpe aus einer Hand",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie plant und installiert Photovoltaik, Batteriespeicher, Wärmepumpen und "
                 "Energiemanagement in Kärnten und der Steiermark, mit zertifizierten Fachkräften und einem "
                 "festen Ansprechpartner von der Planung bis zur Übergabe. Wir rechnen vorher durch, ob der "
                 "Sonnenstrom im Warmwasser, im Speicher oder im Netz am meisten wert ist."),
        "grid": [
            ("Ehrliche Rechnung", "Betriebskosten mit Ihren Energiepreisen."),
            ("Aufstellraum geprüft", "Raumgröße, Luftführung und Kondensat vor Ort."),
            ("PV mitgedacht", "Wärmepumpenboiler oder Heizstab, passend zum Überschuss."),
            ("Förderung im Blick", "EMS-Förderung in der richtigen Reihenfolge."),
        ],
    },

    "faq": [
        ("Was kostet eine Brauchwasserwärmepumpe?",
         "Das Energieinstitut Vorarlberg nennt rund 3.000 bis 4.000 Euro. Die Stiftung Warentest ermittelte in "
         "Deutschland Gerätepreise von 2.400 bis 3.400 Euro, zuzüglich Einbau. Der Einbaupreis hängt von "
         "Einbringung, Luftkanälen und Anschlüssen ab."),
        ("Wie viel Strom verbraucht eine Brauchwasserwärmepumpe?",
         "Für einen 4-Personen-Haushalt mit 2.400 bis 3.200 kWh Wärmebedarf rund 800 bis 1.100 kWh im Jahr bei "
         "einer Jahresarbeitszahl von 3. Die Herstellerangaben nach EU-Energielabel liegen zum Beispiel zwischen "
         "682 und 1.058 kWh im Jahr. Bei 32 Cent je kWh sind das rund 260 Euro für 800 kWh."),
        ("Wie viel kW braucht eine Brauchwasserwärmepumpe?",
         "Wenig: Die Wärmepumpe der Austria Email Explorer Evo 3 nimmt maximal 600 W auf, der Zusatzheizstab "
         "1.200 W, zusammen höchstens 1.800 W. Angeschlossen wird sie mit 230 V einphasig."),
        ("Wie schnell heizt eine Brauchwasserwärmepumpe?",
         "Langsamer als ein Heizstab: Austria Email gibt für die Explorer Evo 3 Aufheizzeiten von rund 6 bis "
         "8 Stunden an (200 bis 270 Liter, 20 °C Luft). Im Alltag wird meist nur ein Teil des Speichers "
         "nachgeheizt, bei Bedarf hilft der eingebaute Heizstab."),
        ("Ist Brauchwasser gleich Warmwasser?",
         "Im Haushalt ja: Brauchwasser meint das Trinkwarmwasser für Dusche, Bad und Küche. Brauchwasserwärmepumpe, "
         "Warmwasser-Wärmepumpe und Wärmepumpenboiler bezeichnen dasselbe Gerät. Die Heizung unterstützt es nicht."),
        ("Kann ich eine Brauchwasserwärmepumpe mit einer Wärmepumpe kombinieren?",
         "Ja, laut Verbraucherzentrale ist die Kombination mit einer Heizungswärmepumpe beliebt, weil beide "
         "effizient arbeiten. Oft übernimmt die Heizungswärmepumpe das Warmwasser aber selbst. Was in Ihrem "
         "Haus sinnvoller ist, prüfen wir vor Ort."),
        ("Wie laut ist eine Brauchwasserwärmepumpe?",
         "Stiebel Eltron nennt für die WWK 302 einen Schalldruck von 45 dB(A) in einem Meter Abstand, Austria "
         "Email für die Explorer Evo 3 eine Schallleistung von 47 dB(A) im Kanalbetrieb. Ein Keller- oder "
         "Heizraum ist deshalb der übliche Aufstellort."),
        ("Gibt es 2026 eine Förderung für die Brauchwasserwärmepumpe?",
         "Eine eigene Förderung von Bund, Kärnten oder Steiermark ist uns für 2026 nicht bekannt. Der "
         "Kesseltausch des Bundes fördert nur den Ersatz einer fossilen Heizung. Über die EMS-Förderung (50 %, "
         "maximal 600 Euro) kann die Steuerung gefördert werden, wenn das EMS mindestens zwei passende "
         "Komponenten steuert."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Mit zertifizierten Fachkräften plant und "
                    "installiert EBZ Energie Photovoltaik, Batteriespeicher, Wärmepumpen und Energiemanagement in "
                    "Kärnten und der Steiermark. Preise und Rechnungen in diesem Ratgeber sind Richtwerte. Keine "
                    "Rechtsberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("Energieinstitut Vorarlberg: Warmwasser effizient und umweltfreundlich aufbereiten",
         "https://www.energieinstitut.at/privatpersonen/haustechnik-energieversorgung/warmwasser-effizient-und-umweltfreundlich-aufbereiten"),
        ("Stiftung Warentest (Deutschland): Brauchwasserwärmepumpen im Test, Juni 2026",
         "https://www.test.de/brauchwasserwaermepumpe-test-6300548-6300553/"),
        ("Verbraucherzentrale (Deutschland): Warmwasser mit der Wärmepumpe",
         "https://www.verbraucherzentrale.de/wissen/energie/heizen-und-warmwasser/wie-erzeuge-ich-warmwasser-wenn-ich-mit-einer-waermepumpe-heize-114880"),
        ("Bosch Home Comfort Österreich: Brauchwasserwärmepumpe",
         "https://www.bosch-homecomfort.com/at/de/wohngebaeude/wissen/heizungsratgeber/waermepumpe/brauchwasserwaermepumpe/"),
        ("Austria Email: Prospekt Explorer Evo 3 (V03/26)",
         "https://www.heizungsdiscount24.de/pdf/Austria-Email-Explorer-Evo-3-Prospekt.pdf"),
        ("Austria Email: Warmwasser-Wärmepumpe AE Revolution Evo 3",
         "https://www.austria-email.at/privatkunden/produkte/warmwasser-waermepumpen/warmwasser-waermepumpe-ae-revolution-evo-3/"),
        ("Stiebel Eltron: Datenblatt WWK 222 / WWK 302",
         "https://www.stiebel-eltron.com/en/home/products-solutions/dhw/dhw_heat_pumps/wwk-222-302--h-/wwk-302/technical-data.product.pdf"),
        ("Bundesamt für Energie (Schweiz): Effizienzuntersuchung Brauchwarmwasser an Wärmepumpen, 2014",
         "https://pubdb.bfe.admin.ch/de/publication/download/7606"),
        ("E-Control: Strom- und Gaspreismonitor November 2026", "https://www.e-control.at/preismonitor"),
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/de/marktpreis/"),
        ("WKO: Heizölpreise", "https://www.wko.at/oe/industrie/energierohstoff-kraftstoff/kraftstoffpreise"),
        ("Statistik Austria: Energieverwendung privater Haushalte 2025 bis 2026",
         "https://www.statistik.at/fileadmin/publications/Energieverwendung_2025-2026_bf.pdf"),
        ("Verbraucherzentrale Rheinland-Pfalz (Deutschland): Warmwasser", "https://verbraucherzentrale-rlp.de/node/77008"),
        ("Amt der NÖ Landesregierung: Infoblatt Legionellen",
         "https://www.noe.gv.at/noe/Gesundheitsvorsorge-Forschung/Infoblatt_Legionellen_oeffentliche_Einrichtungen_20260909.pdf"),
        ("BMLUK: Sanierung und Kesseltausch",
         "https://www.bmluk.gv.at/themen/klima-und-umwelt/klima/klima-initiativen-und-foerderungen/ufg/sanierung-kesselaustausch-2027.html"),
        ("Österreichischer Biomasse-Verband: Landesförderung Kärnten 2026 (Übersicht)",
         "https://www.biomasseverband.at/wp-content/uploads/Landesfoerderung-Holzheizsysteme-Kaernten-2026.pdf"),
        ("Land Steiermark: Richtlinie Tausch erneuerbar betriebener Heizungssysteme 2026",
         "https://www.wohnbau.steiermark.at/cms/dokumente/13000784_183599709/c26463e2/2026_F%C3%B6rderungsrichtlinie%20Tausch%20erneuerbar%20betriebener%20Heizungssysteme.pdf"),
        ("Klima- und Energiefonds: Leitfaden Energiemanagement private Haushalte 2026",
         "https://www.umweltfoerderung.at/fileadmin/user_upload/umweltfoerderung/private/Energiemanagement/ems_private_leitfaden.pdf"),
        ("Fronius: Ohmpilot Bedienungsanleitung", "https://manuals.fronius.com/html/4204260538/de.html"),
    ],
    "related": [
        ("/warmwasser-mit-photovoltaik/", "Warmwasser mit Photovoltaik: Heizstab und PV-Regler"),
        ("waermepumpe", "Wärmepumpe: Planung und Installation"),
        ("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"),
        ("ems", "Energiemanagementsystem: PV-Überschuss automatisch nutzen"),
    ],
    "cta": {
        "h3": "Warmwasser günstiger machen",
        "text": "Wir rechnen Brauchwasserwärmepumpe, Heizstab und Photovoltaik für Ihr Haus ehrlich durch.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Warmwasser effizient bereiten, ehrlich gerechnet",
    "final_text": ("Kostenlose Erstberatung zu Warmwasser, Photovoltaik, Wärmepumpe und Energiemanagement, mit "
                   "transparenten Zahlen und einem Ansprechpartner aus Villach."),
}
