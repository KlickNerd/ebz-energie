"""Ratgeber: Wärmepumpe mit Heizkörpern (Vorlauftemperatur, 55-Grad-Test, Heizkörpertypen, Tausch, Abgleich, JAZ).

Neuer Artikel (kein WordPress-Vorgänger), erstellt 2026-11-19.
Ziel-Keywords (Google Ads, Österreich, 19.11.2026): wärmepumpe mit heizkörper / wärmepumpe heizkörper /
heizkörper für wärmepumpe 720 (Oktober 1.000), niedertemperatur heizkörper 720, vorlauftemperatur
wärmepumpe 170, luft wärmepumpe heizkörper 170, niedertemperatur-heizkörper für wärmepumpe 110,
gebläsekonvektor wärmepumpe 70, wärmepumpe mit heizkörper erfahrung 50, wärmepumpe ohne fußbodenheizung 30.

Faktenbasis: Recherche vom 19.11.2026 (Energieinstitut Vorarlberg, Herstellerseiten Vaillant, Bosch, Viessmann
und Kermi für Österreich, Zehnder-Datenblatt nach EN 442, Fraunhofer ISE Projektseiten, Solarserver und
Cleanthinking als deutsche Fachmedien zum Abschlussbericht WP-QS im Bestand, Verbraucherzentrale als deutsche
Quelle, Förderblatt Kärnten 2026 der KEM Mittelkärnten, BMLUK und sanierungsoffensive.gv.at zum Kesseltausch,
Land Steiermark, E-Control Preismonitor November 2026).
Zahlen konsistent mit /waermepumpe-im-altbau/ und der Vorlauf-Infografik (30 bis 35 °C Fußboden, 50 bis 55 °C
effizient, 60 bis 70 °C klassische Heizkörper). Infografik bewusst nicht eingebaut (Komponente der Leistungsseiten).
Eigene Rechnungen: Stromverbrauch = Wärmebedarf / JAZ, Kosten mit 28 bis 35 ct/kWh; 10 K x 2,5 % je Grad.
Nicht behauptet: österreichische Preise für Montage beim Heizkörpertausch, JAZ-Unterschied in Prozent
zwischen Heizkörper und Fußbodenheizung aus einer Studie, technische Kriterien der Bundesförderung (Infoblatt
nicht lesbar), Förderfähigkeit neuer Heizkörper.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "waermepumpe-mit-heizkoerpern",
    "path": "/waermepumpe-mit-heizkoerpern/",
    "cluster": "Wärmepumpe und Heizen",
    "title": "Wärmepumpe mit Heizkörper: Vorlauf, Test, Kosten | EBZ",
    "description": ("Wärmepumpe mit Heizkörper: Bis 55 °C Vorlauf läuft sie effizient. So testen Sie Ihre "
                    "Heizkörper, was ein Tausch kostet (rund 500 € je Stück), JAZ und Förderung."),
    "eyebrow": "Wärmepumpe · Heizkörper",
    "crumb_label": "Wärmepumpe mit Heizkörpern",
    "h1": "Wärmepumpe mit Heizkörpern: Bis 55 °C Vorlauf funktioniert es meist ohne Fußbodenheizung",
    "lead": ("Eine Wärmepumpe braucht keine Fußbodenheizung. Entscheidend ist, ob Ihre Heizkörper das Haus "
             "an kalten Tagen mit höchstens 55 °C Vorlauftemperatur warm bekommen. Dieser Ratgeber zeigt, wie "
             "Sie das selbst testen, welche Heizkörper passen, was ein Tausch einzelner Heizkörper kostet und "
             "wie viel Effizienz die Vorlauftemperatur ausmacht."),
    "chips": [
        "Grenze: <b>55 °C</b> Vorlauf an kalten Tagen",
        "Je Grad weniger: <b>rund 2,5 %</b> Effizienz",
        "Heizkörpertausch: <b>rund 500 €</b> je Stück",
        "JAZ nur mit Heizkörpern: <b>3,0 bis 4,0</b>",
    ],
    "date_published": "2026-11-19",
    "date_modified": "2026-11-19",
    "hero_img": "waermepumpe",
    "hero_alt": "Außeneinheit einer Luft-Wasser-Wärmepumpe mit zwei Ventilatoren auf einem Betonsockel im Garten vor einer Holzwand",

    "tldr": [
        "Eine Wärmepumpe funktioniert mit Heizkörpern, wenn das Haus an kalten Tagen mit höchstens 55 °C "
        "Vorlauftemperatur warm wird. Darüber steigt der Stromverbrauch deutlich.",
        "Jedes Grad Vorlauftemperatur verändert die Effizienz um rund 2,5 % (Energieinstitut Vorarlberg). "
        "10 Grad weniger Vorlauf sparen damit grob ein Viertel des Heizstroms.*",
        "Ob Ihre Heizkörper reichen, zeigt ein einfacher Test an einem kalten Tag: Thermostate voll auf, "
        "Vorlauf am bestehenden Kessel schrittweise senken. Bleibt es bei 55 °C oder darunter warm, passen sie.",
        "Meist reicht es, einzelne zu kleine Heizkörper zu tauschen, im Schnitt rund 500 Euro je Stück plus "
        "Montage. Eine neue Fußbodenheizung ist selten nötig.",
        "Im Fraunhofer-Feldtest erreichten Häuser nur mit Heizkörpern eine Jahresarbeitszahl von 3,0 bis 4,0. "
        "Ausreichend große Heizkörper liefen ähnlich niedrig temperiert wie Fußbodenheizungen.",
    ],
    "kpis": [
        ("55 °C", "Faustregel: max. Vorlauf an kalten Tagen"),
        ("rund 2,5 %", "Effizienz je Grad Vorlauf"),
        ("rund 50 %", "Heizkörperleistung bei 55/45 °C statt 75/65 °C"),
        ("3,0 bis 4,0", "JAZ in Häusern nur mit Heizkörpern (Feldtest)"),
    ],

    "sections": [
        ("Wärmepumpe mit Heizkörper: Geht das?", "geht-das", f"""
<p><b>Ja. Eine Wärmepumpe kann ein Haus mit normalen Heizkörpern beheizen, wenn diese groß genug sind, um
den Raum mit niedriger Vorlauftemperatur warm zu bekommen.</b> Als Faustregel gilt: Reichen an kalten Tagen
höchstens 55 °C, ist das Haus für eine Wärmepumpe geeignet. Diese Grenze nennen die Verbraucherzentrale
(Deutschland) und Hersteller wie Vaillant Österreich übereinstimmend.</p>
<p>Wie gut das in der Praxis klappt, zeigen Messungen des Fraunhofer ISE in Deutschland. Im Projekt
„WP-QS im Bestand“ wurden 77 Wärmepumpen in bestehenden Ein- bis Dreifamilienhäusern über vier Jahre
vermessen, gebaut zwischen 1826 und 2001. Die Luft-Wasser-Wärmepumpen kamen im Mittel auf eine
Jahresarbeitszahl (JAZ) von 3,4, die Erdwärmepumpen auf 4,3. Ausreichend dimensionierte Heizkörper liefen
dabei im Mittel mit ähnlich niedrigen Temperaturen wie Fußbodenheizungen. Einen Zusammenhang zwischen
Baujahr und Effizienz fanden die Forschenden nicht.</p>
<p>Wichtig ist deshalb nicht, ob Ihr Haus ein Altbau ist, sondern welche Vorlauftemperatur es braucht.
Was Dämmung, Rechenbeispiele und die Wahl der Wärmepumpe im Bestand betrifft, finden Sie im Ratgeber
{a('/waermepumpe-im-altbau/', 'Wärmepumpe im Altbau')}. Hier geht es um die Heizkörper selbst.</p>
"""),
        ("Vorlauftemperatur der Wärmepumpe: warum 55 °C die Grenze ist", "vorlauftemperatur", f"""
<p><b>Die Vorlauftemperatur ist die Temperatur des Heizwassers, das zu den Heizkörpern fließt. Je
niedriger sie ist, desto weniger Strom braucht die Wärmepumpe für dieselbe Wärme.</b> Das Energieinstitut
Vorarlberg beziffert den Einfluss mit rund 2,5 % je Grad. Ideal sind laut Energieinstitut unter 35 °C, wie
sie Fußboden- und Wandheizungen schaffen. Ab etwa 50 °C wird es kritisch: Die Stromkosten steigen, die
Ökobilanz kann schlechter ausfallen als beim alten Ölkessel.</p>
{A.table(
    ["Heizfläche", "Typische Vorlauftemperatur", "Eignung für die Wärmepumpe"],
    [
        ["Fußboden-, Wand- oder Deckenheizung", "25 bis 40 °C", "sehr gut"],
        ["Niedertemperatur-Heizkörper", "30 bis 50 °C", "sehr gut"],
        ["Plattenheizkörper", "50 bis 70 °C", "gut bis eingeschränkt, je nach Größe"],
        ["Glieder- und Röhrenheizkörper", "55 bis 80 °C", "nur bedingt"],
    ],
    hl_cols=(1,),
)}
<p>Richtwerte laut Bosch Home Comfort Österreich. Entscheidend ist aber nicht der Typ allein, sondern die
Größe im Verhältnis zum Wärmebedarf des Raums: Ein großer alter Gussheizkörper in einem kleinen Zimmer
kann mit weniger Vorlauf auskommen als ein knapp bemessener Plattenheizkörper in einem großen Raum.</p>
<h3>Warum Heizkörper bei niedriger Temperatur weniger leisten</h3>
<p>Heizkörper werden nach EN 442 mit 75 °C Vorlauf, 65 °C Rücklauf und 20 °C Raumtemperatur gemessen.
Bei 55/45/20 °C gibt derselbe Heizkörper nur rund die Hälfte dieser Normleistung ab. Im Datenblatt des
Zehnder Nova etwa sinkt ein Element von 71 auf 36,6 Watt.* Viele Heizkörper aus der Zeit der Öl- und
Gaskessel sind aber großzügig bemessen. Genau das macht sie oft wärmepumpentauglich.</p>
"""),
        ("Der 55-Grad-Test: Reichen Ihre Heizkörper?", "test", f"""
<p><b>Ob Ihre Heizkörper für eine Wärmepumpe reichen, können Sie mit dem bestehenden Öl- oder Gaskessel
selbst testen.</b> Vaillant Österreich beschreibt dafür vier Schritte:</p>
{A.steps([
    ("Kalten Tag abwarten",
     "Der Test sagt nur etwas aus, wenn es draußen richtig kalt ist. Bosch empfiehlt, die Heizkurve nur bei "
     "Außentemperaturen bis höchstens 5 °C zu verändern."),
    ("Thermostate voll aufdrehen",
     "An allen Heizkörpern, die Sie prüfen wollen, die Thermostatventile auf die höchste Stufe stellen."),
    ("Vorlauftemperatur senken",
     "Über die Heizkurve des Kessels die Vorlauftemperatur schrittweise so weit absenken, dass die "
     "Raumtemperatur gerade noch stabil bleibt. Die Einstellung kann einige Tage dauern."),
    ("Ergebnis ablesen",
     "Liegt dieser Wert bei 55 °C oder darunter, eignen sich die vorhandenen Heizkörper für eine "
     "Wärmepumpe."),
])}
<h3>So lesen Sie das Ergebnis</h3>
<ul>
  <li><b>Alle Räume bleiben bei 55 °C oder weniger warm:</b> Die Heizkörper können bleiben.</li>
  <li><b>Ein oder zwei Räume werden nicht warm</b> (oft Bad, Wohnzimmer mit großer Fensterfläche oder ein
  ausgebauter Dachraum): Hier reicht es meist, genau diese Heizkörper gegen größere oder
  Wärmepumpenheizkörper zu tauschen. Das empfiehlt auch die Verbraucherzentrale (Deutschland).</li>
  <li><b>Das ganze Haus braucht deutlich über 55 °C:</b> Dann sind meist die Wärmeverluste der Gebäudehülle
  der größere Hebel. Welche Dämmmaßnahmen sich zuerst lohnen, steht im Ratgeber
  {a('/waermepumpe-im-altbau/', 'Wärmepumpe im Altbau')}.</li>
</ul>
{A.box("Der Selbsttest ersetzt keine Heizlastberechnung. Bei der Besichtigung prüfen wir Raum für Raum, "
       "welche Heizkörper reichen, und legen die Wärmepumpe auf den tatsächlichen Wärmebedarf aus.",
       label="Gut zu wissen:")}
"""),
        ("Heizkörper für die Wärmepumpe: welche Typen passen", "heizkoerper-typen", f"""
<p><b>Für die Wärmepumpe zählt die Wärme abgebende Fläche. Je mehr Fläche ein Heizkörper hat, desto
niedriger darf die Vorlauftemperatur sein.</b> Wie stark das wirkt, zeigt eine Beispielrechnung aus dem
Fraunhofer-Projekt WPsmart im Bestand: Bei gleicher Baulänge sinkt die mittlere Heizkreistemperatur von
63,0 °C (Plattenheizkörper Typ 21) auf 54,1 °C (Typ 22) und 47,1 °C (Typ 33).</p>
{A.table(
    ["Heizkörper", "Wie er arbeitet", "Für die Wärmepumpe"],
    [
        ["Glieder- und Röhrenheizkörper", "wenig Fläche, träge", "nur wenn groß bemessen"],
        ["Plattenheizkörper Typ 22 oder 33", "zwei bzw. drei Platten mit Lamellen", "gut, wenn groß genug"],
        ["Niedertemperatur-Heizkörper", "großflächig und flach, für niedrige Vorlauftemperatur ausgelegt",
         "sehr gut"],
        ["Wärmepumpenheizkörper mit Ventilatoren", "kleine Lüfter erhöhen den Luftstrom",
         "sehr gut, wo wenig Platz ist"],
        ["Fußboden- oder Wandheizung", "sehr große Fläche", "ideal, im Bestand aber aufwendig"],
    ],
    hl_cols=(2,),
)}
<h3>Niedertemperatur-Heizkörper</h3>
<p>Niedertemperatur-Heizkörper sind auf Vorlauftemperaturen deutlich unter 55 °C ausgelegt. Bosch nennt
für sie 30 bis 50 °C, meist unter 40 °C. Sie passen dort, wo an der Wand genug Platz für einen
größeren Heizkörper ist.</p>
<h3>Wärmepumpenheizkörper und Gebläsekonvektoren</h3>
<p>Wärmepumpenheizkörper sind Plattenheizkörper mit eingebauten kleinen Ventilatoren (Viessmann
Österreich). Die Lüfter blasen mehr Luft durch die Lamellen, so gibt derselbe Heizkörper bei niedriger
Vorlauftemperatur mehr Wärme ab. Kermi nennt für seinen x-flair einen Einsatzbereich von 35 bis 65 °C
Vorlauf und einen Tausch 1:1 gegen alte Heizkörper ohne aufwendige Umbauarbeiten. Mit einer passenden Wärmepumpe können manche Modelle im
Sommer auch kühlen. Die Ventilatoren brauchen einen Stromanschluss am Heizkörper, das klären wir bei der
Planung.</p>
<p>Röhrenheizkörper durch neue Röhrenheizkörper zu ersetzen, bringt laut Vaillant nur optisch etwas,
keine höhere Effizienz. Infrarotheizungen machen aus Strom direkt Wärme und eignen sich laut Vaillant
nur für selten genutzte Räume, siehe {a('/infrarotheizung-mit-photovoltaik/', 'Infrarotheizung mit Photovoltaik')}.</p>
"""),
        ("Einzelne Heizkörper tauschen statt Fußbodenheizung: Kosten und Förderung", "tauschen", f"""
<p><b>Meist reicht es, die zwei oder drei Heizkörper zu tauschen, die beim Test nicht mitkommen.</b> Laut
Abschlussbericht des Fraunhofer-Projekts (zitiert von Cleanthinking) ist ein teurer und aufwendiger Umbau
auf Flächenheizungen nicht nötig, wenn zu klein dimensionierte Heizkörper raumweise ersetzt werden. Eine nachträgliche Fußbodenheizung bedeutet neue Estrich- oder
Trockenbausysteme und Bodenbeläge, die Kosten dafür stehen im Ratgeber
{a('/waermepumpe-im-altbau/', 'Wärmepumpe im Altbau')}.</p>
{A.table(
    ["Posten", "Richtwert", "Quelle"],
    [
        ["Neuer Heizkörper", "im Schnitt rund 500 € je Stück", "Vaillant und Bosch Österreich"],
        ["Spanne je Heizkörper", "rund 50 € (klein) bis 1.000 € (groß)", "Bosch Österreich"],
        ["Beispiel: drei Heizkörper", "rund 1.500 € Material*", "eigene Rechnung"],
        ["Dazu", "Montage und hydraulischer Abgleich", "nach Aufwand, Angebot vor Ort"],
    ],
    hl_cols=(1,),
)}
<p>Zum Vergleich: Eine Wärmepumpe mit Installation kostet laut Vaillant 10.000 bis 20.000 Euro, die
Spannen für den Altbau stehen im Ratgeber {a('/kosten-einer-waermepumpe/', 'Kosten einer Wärmepumpe')}.
Der Heizkörpertausch ist also ein kleiner Posten, der die Betriebskosten über viele Jahre senkt.</p>
<h3>Förderung 2026</h3>
<ul>
  <li><b>Bund:</b> Der Kesseltausch für Ein- und Zweifamilienhäuser ist seit 2. November 2026 neu aufgelegt.
  Für den Umstieg von einer fossilen Heizung auf eine Wärmepumpe nennt das BMLUK eine Pauschale
  von 5.000 Euro. Registrieren können Sie sich bis 31. Dezember 2026 oder bis das Budget aufgebraucht ist,
  anerkannt werden Leistungen ab 7. Oktober 2026.</li>
  <li><b>Kärnten:</b> Die Landesförderung für energieeffiziente Haustechnik zahlt 2026 für die Wärmepumpe im
  Eigenheim 3.000 Euro, dazu 200 Euro für den hydraulischen Abgleich. Ob das Budget reicht, klären wir vor
  dem Angebot.</li>
  <li><b>Steiermark:</b> Für neue Wärmepumpen nimmt das Land derzeit keine Förderanträge an.</li>
</ul>
<p>Welche Kosten im Detail förderfähig sind, regeln die Informationsblätter der Programme. Alle Programme
im Überblick: {a('/waermepumpenfoerderung-in-oesterreich/', 'Wärmepumpenförderung in Österreich')} und
{a('/landesfoerderungen-fuer-die-waermepumpe/', 'Landesförderungen für die Wärmepumpe')}.</p>
{A.cta("Reichen Ihre Heizkörper für eine Wärmepumpe?",
       "Wir prüfen Heizkörper, Wärmebedarf und Vorlauftemperatur bei Ihnen vor Ort und sagen ehrlich, "
       "welche bleiben können und welche getauscht werden sollten.",
       secondary=("waermepumpe", "Zum Wärmepumpen-Installateur"))}
"""),
        ("Hydraulischer Abgleich und Heizkurve: die günstigsten Stellschrauben", "abgleich", f"""
<p><b>Ein hydraulischer Abgleich sorgt dafür, dass jeder Heizkörper genau die Wassermenge bekommt, die er
braucht.</b> Ohne Abgleich nimmt das Heizwasser den Weg des geringsten Widerstands: Heizkörper nahe der
Wärmepumpe werden überversorgt, entfernte Räume bleiben kühl (Viessmann Österreich). Die übliche, aber
teure Reaktion darauf ist eine höhere Vorlauftemperatur für das ganze Haus.</p>
<ul>
  <li><b>Abgleich:</b> Senkt laut Vaillant die durchschnittliche Vorlauftemperatur und damit die
  Stromkosten. Das Energieinstitut Vorarlberg hält ihn „in jedem Fall“ für empfehlenswert. Kärnten fördert
  ihn 2026 mit 200 Euro.</li>
  <li><b>Heizkurve:</b> Sie legt fest, welche Vorlauftemperatur bei welcher Außentemperatur gefahren wird.
  Nach dem ersten Winter lohnt es sich, sie nachzustellen. Das Energieinstitut empfiehlt, die Anlage nach
  dem ersten Betriebswinter zu prüfen.</li>
</ul>
{A.box("Werden Räume trotz Wärmepumpe nicht warm, liegt es meist an fehlendem Abgleich, einer zu flach "
       "eingestellten Heizkurve oder einzelnen zu kleinen Heizkörpern. Alle drei lassen sich beheben, ohne "
       "die Vorlauftemperatur für das ganze Haus anzuheben.",
       label="Praxis-Tipp:")}
"""),
        ("Effizienz: Heizkörper gegenüber Fußbodenheizung (JAZ)", "jaz", f"""
<p><b>Die Jahresarbeitszahl (JAZ) gibt an, wie viele Kilowattstunden Wärme die Wärmepumpe im Jahr aus einer
Kilowattstunde Strom macht.</b> Sie hängt vor allem von der Heizkreistemperatur ab, nicht davon, ob die
Wärme über Heizkörper oder Fußboden in den Raum kommt. Das zeigen die Fraunhofer-Messungen:</p>
{A.table(
    ["Messung (Deutschland)", "Heizkreis", "Ergebnis"],
    [
        ["WP-QS im Bestand, 2024: nur Fußbodenheizung", "im Jahresmittel 32,0 °C", ""],
        ["WP-QS im Bestand, 2024: nur Heizkörper", "im Jahresmittel 38,5 °C", "JAZ 3,0 bis 4,0"],
        ["WP-QS im Bestand: alle Luft-Wasser-Wärmepumpen", "", "JAZ im Mittel 3,4 (2,6 bis 4,9)"],
        ["WP im Bestand, 2008 bis 2009: 72 % nur Radiatoren", "im Winter meist 50 bis 65 °C",
         "Luft-Wasser JAZ im Mittel 2,6"],
    ],
    hl_cols=(2,),
)}
<p>Der Vergleich der beiden Feldtests zeigt, was niedrigere Vorlauftemperaturen und bessere Geräte
gemeinsam bringen. Das Energieinstitut Vorarlberg nennt als Ziel eine JAZ über 4 und rechnet vor: Bei einer
JAZ von 3 braucht die Wärmepumpe ein Drittel mehr Strom als bei JAZ 4.</p>
{A.table(
    ["Beispiel: 12.000 kWh Wärme im Jahr*", "JAZ 3,0", "JAZ 4,0"],
    [
        ["Strombedarf der Wärmepumpe", "4.000 kWh", "3.000 kWh"],
        ["Stromkosten bei 28 bis 35 ct/kWh", "1.120 bis 1.400 €", "840 bis 1.050 €"],
        ["Unterschied pro Jahr", "", "rund 280 bis 350 € weniger"],
    ],
    hl_cols=(2,),
)}
<p>Strompreis: Durchschnitt für Kärnten und die Steiermark laut E-Control-Preismonitor November 2026. Wie
viel Strom eine Wärmepumpe insgesamt braucht, erklärt der Ratgeber
{a('/funktionsweise-einer-waermepumpe/', 'Funktionsweise einer Wärmepumpe')}.</p>
"""),
        ("Hochtemperatur-Wärmepumpe: die Lösung für alte Heizkörper?", "hochtemperatur", f"""
<p><b>Wärmepumpen können heute bis zu 75 °C Vorlauftemperatur erzeugen</b> (Vaillant Österreich), Bosch
nennt diesen Wert für seine Luft-Wasser-Wärmepumpen mit dem Kältemittel R290 (Propan). Technisch kann eine Wärmepumpe damit auch Heizkörper
versorgen, die 65 oder 70 °C brauchen. Bosch weist aber darauf hin, dass Hochtemperatur-Wärmepumpen weniger
effizient arbeiten und in der Anschaffung teurer sind.</p>
<p>Unsere Reihenfolge ist deshalb: zuerst testen, dann Abgleich und einzelne Heizkörper, erst danach eine
höhere Vorlauftemperatur. Vaillant formuliert es ähnlich: Die Wärmepumpe kann bis 75 °C, angestrebt werden
aber höchstens 55 °C. Eine Hochtemperatur-Lösung ist sinnvoll, wenn Heizkörper aus Platz- oder
Denkmalgründen nicht getauscht werden können und eine Dämmung nicht möglich ist.</p>
"""),
        ("Wärmepumpe mit Heizkörpern und Photovoltaik", "photovoltaik", f"""
<p><b>Eine Photovoltaikanlage senkt die Stromkosten der Wärmepumpe, deckt im Winter aber nur einen kleinen
Teil.</b> Im Fraunhofer-Projekt wurden sechs Kombinationen aus Wärmepumpe und Photovoltaik ausgewertet: Ohne
Batteriespeicher kamen 25 bis 40 % des Wärmepumpenstroms vom eigenen Dach, mit Speicher 32 bis 62 %. Das
Energieinstitut Vorarlberg betont, dass der Winterstrom meist aus dem Netz kommt, auch wenn die
Jahresbilanz ausgeglichen sein kann.</p>
<p>Gerade bei Heizkörpern hilft die Kombination: An sonnigen Tagen in der Übergangszeit kann die Wärmepumpe
mit Solarstrom den Puffer- oder Warmwasserspeicher aufladen, ein
{a('ems', 'Energiemanagementsystem')} steuert das über die SG-Ready-Schnittstelle. Ein
{a('batteriespeicher', 'Batteriespeicher')} verschiebt Solarstrom in den Abend. Wie Sie PV-Anlage und
Wärmepumpe aufeinander abstimmen, erklärt der Ratgeber
{a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}. Warmwasser mit Solarstrom:
{a('/warmwasser-mit-photovoltaik/', 'Warmwasser mit Photovoltaik')}.</p>
"""),
        ("Fazit: Erst testen, dann gezielt tauschen", "fazit", f"""
<p>Eine Wärmepumpe mit Heizkörpern ist im Bestand der Normalfall, nicht die Ausnahme. Die Grenze liegt bei
etwa 55 °C Vorlauf an kalten Tagen. Ob Ihr Haus darunter bleibt, zeigt der Test mit dem alten Kessel. Wo
einzelne Räume nicht mitkommen, reichen meist größere oder Wärmepumpenheizkörper für rund 500 Euro je
Stück, dazu ein hydraulischer Abgleich und eine sauber eingestellte Heizkurve. Jedes Grad weniger
Vorlauf spart rund 2,5 % Strom, über die Lebensdauer der Wärmepumpe summiert sich das.</p>
<p><small>*Richtwerte und eigene Berechnungen auf Basis der genannten Quellen. Heizkörperleistung laut
Herstellerdatenblatt (Zehnder Nova, Element 600 mm, EN 442). Das Viertel Strom ergibt sich aus 10 Grad mal
rund 2,5 %. Kostenbeispiel mit 12.000 kWh Wärmebedarf und Strompreisen laut E-Control, Stand November 2026.
Deutsche Studien und Quellen sind als solche gekennzeichnet. Ihre Werte hängen von Gebäude, Heizflächen und
Tarif ab.</small></p>
{A.cta("Wärmepumpe mit Ihren Heizkörpern, ehrlich geprüft",
       "Wir sehen uns Heizkörper, Vorlauftemperatur und Wärmebedarf an und sagen Ihnen, was bleiben kann, "
       "was getauscht werden sollte und welche Förderung Sie bekommen.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Wärmepumpe im Bestand: EBZ Energie plant mit Ihren Heizkörpern",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Wärmepumpen, Photovoltaik, Speicher und "
                 "Energiemanagement in Kärnten und der Steiermark, mit zertifizierten Fachkräften und einem "
                 "festen Ansprechpartner von der Planung bis zur Übergabe. Wir prüfen Ihre Heizkörper Raum für "
                 f"Raum und tauschen nur, was nötig ist. Umgesetzte Anlagen finden Sie unter "
                 f"{a('referenzen', 'Referenzen')}."),
        "grid": [
            ("Heizkörper-Check vor Ort", "Raum für Raum, mit Blick auf die Vorlauftemperatur."),
            ("Gezielt statt pauschal", "Nur zu kleine Heizkörper tauschen, keine unnötige Fußbodenheizung."),
            ("Abgleich und Heizkurve", "Sauber eingestellt, damit die Wärmepumpe effizient läuft."),
            ("Förderung im Blick", "Bund und Land in der richtigen Reihenfolge beantragt."),
        ],
    },

    "faq": [
        ("Kann man eine Wärmepumpe mit normalen Heizkörpern betreiben?",
         "Ja, wenn die Heizkörper das Haus an kalten Tagen mit höchstens 55 °C Vorlauftemperatur warm "
         "bekommen. Im Fraunhofer-Feldtest erreichten Häuser nur mit Heizkörpern eine Jahresarbeitszahl von "
         "3,0 bis 4,0. Eine Fußbodenheizung ist nicht nötig."),
        ("Wie heiß werden Heizkörper bei einer Wärmepumpe?",
         "Deutlich weniger heiß als mit Öl oder Gas. Die Vorlauftemperatur sollte höchstens 55 °C betragen, "
         "im Fraunhofer-Feldtest lag die mittlere Heizkreistemperatur in Häusern nur mit Heizkörpern bei "
         "38,5 °C. Die Heizkörper fühlen sich daher eher lauwarm an, geben aber über längere Zeit genug "
         "Wärme ab."),
        ("Welche Vorlauftemperatur ist für eine Wärmepumpe ideal?",
         "So niedrig wie möglich: Ideal sind laut Energieinstitut Vorarlberg unter 35 °C, wie sie "
         "Fußbodenheizungen schaffen. Mit Heizkörpern sind 50 bis 55 °C an kalten Tagen ein effizienter "
         "Bereich. Jedes Grad weniger verbessert die Effizienz um rund 2,5 %."),
        ("Welche Heizkörper sind für eine Wärmepumpe am besten?",
         "Großflächige Plattenheizkörper vom Typ 22 oder 33, Niedertemperatur-Heizkörper und "
         "Wärmepumpenheizkörper mit kleinen Ventilatoren. Glieder- und Röhrenheizkörper eignen sich nur, wenn "
         "sie für den Raum großzügig bemessen sind."),
        ("Was kostet es, Heizkörper für die Wärmepumpe zu tauschen?",
         "Ein neuer Heizkörper kostet laut Vaillant und Bosch Österreich im Schnitt rund 500 Euro, je nach "
         "Größe von rund 50 bis 1.000 Euro. Dazu kommen Montage und hydraulischer Abgleich. Meist müssen nur "
         "zwei oder drei Heizkörper getauscht werden."),
        ("Warum werden die Räume trotz Wärmepumpe nicht warm?",
         "Häufige Ursachen sind ein fehlender hydraulischer Abgleich, eine zu niedrig eingestellte Heizkurve "
         "oder einzelne zu kleine Heizkörper. Statt die Vorlauftemperatur für das ganze Haus zu erhöhen, "
         "sollten diese Punkte zuerst geprüft werden."),
        ("Brauche ich für alte Heizkörper eine Hochtemperatur-Wärmepumpe?",
         "Meist nicht. Wärmepumpen mit R290 erreichen zwar bis zu 75 °C, arbeiten bei hohen Temperaturen aber "
         "weniger effizient. Zuerst testen, abgleichen und einzelne Heizkörper tauschen ist in der Regel "
         "günstiger."),
        ("Wie viel effizienter ist eine Fußbodenheizung als Heizkörper?",
         "Den Unterschied macht die Vorlauftemperatur, nicht das System an sich. Im Fraunhofer-Feldtest lag "
         "der Heizkreis bei Fußbodenheizungen im Mittel bei 32,0 °C, bei Heizkörpern bei 38,5 °C. Mit der Faustregel "
         "von rund 2,5 % je Grad entspricht das grob 16 % mehr Strom für dieselbe Wärme.*"),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Mit zertifizierten Fachkräften plant und "
                    "installiert EBZ Energie Wärmepumpen, Photovoltaik und Speicher in Kärnten und der "
                    "Steiermark, im Bestand meist mit den vorhandenen Heizkörpern. Preise und Rechnungen in "
                    "diesem Ratgeber sind Richtwerte. Keine Rechtsberatung, maßgeblich sind die offiziellen "
                    "Förderbedingungen."),
    "sources": [
        ("Energieinstitut Vorarlberg: Die Wärmepumpe, eine Glanzleistung an Effizienz",
         "https://www.energieinstitut.at/privatpersonen/heizung-und-lueftung/die-waermepumpe-eine-glanzleistung-an-effizienz"),
        ("Vaillant Österreich: Wärmepumpe mit Heizkörpern kombinieren",
         "https://www.vaillant.at/ratgeber/technologie-verstehen/waermepumpen/waermepumpe-mit-heizkoerpern/"),
        ("Bosch Home Comfort Österreich: Wärmepumpe mit Heizkörper betreiben",
         "https://www.bosch-homecomfort.com/at/de/wohngebaeude/wissen/heizungsratgeber/waermepumpe/waermepumpe-heizkoerper-kombinieren/"),
        ("Viessmann Österreich: Wärmepumpe ohne Fußbodenheizung",
         "https://www.viessmann.at/de/wissen/info-und-tipps-zum-kauf/heat-pump-without-underfloor-heating.html"),
        ("Kermi: Wärmepumpe und Heizkörper (x-flair)",
         "https://www.kermi.com/en/de/guide/knowledge/heat-pumps/heat-pump-and-radiator/"),
        ("Zehnder: Technische Daten Nova nach EN 442 (Datenblatt)",
         "https://baddepot.de/media/products/zehnder/Massblaetter-2019/Massblatt-Nova-v.pdf"),
        ("Fraunhofer ISE (Deutschland): WP-QS im Bestand, Projektseite und Abschlussbericht",
         "https://www.ise.fraunhofer.de/de/forschungsprojekte/wp-qs-im-bestand.html"),
        ("Fraunhofer ISE (Deutschland): WP im Bestand, Feldtest 2006 bis 2009",
         "https://www.ise.fraunhofer.de/de/forschungsprojekte/wp-im-bestand.html"),
        ("Solarserver (Deutschland): Wärmepumpen heizen im Altbau klimafreundlich, 3. November 2025",
         "https://www.solarserver.de/2025/11/03/forschungsprojekt-waermepumpen-heizen-im-altbau-klimafreundlich/"),
        ("Cleanthinking (Deutschland): Hausbesitzer behalten beim Wechsel zur Wärmepumpe oft ihre Heizkörper",
         "https://www.cleanthinking.de/?p=1074119"),
        ("Verbraucherzentrale (Deutschland): Wärmepumpe im Eigenheim, Voraussetzungen",
         "https://www.verbraucherzentrale.de/node/113948"),
        ("KEM Mittelkärnten: Förderungen 2026, Thermische Sanierung und Kesseltausch (Kärnten)",
         "https://www.maria-saal.gv.at/fileadmin/maria_saal/user_upload/Foerderungen_2026.pdf"),
        ("BMLUK: Sanierung und Kesseltausch",
         "https://www.bmluk.gv.at/themen/klima-und-umwelt/klima/klima-initiativen-und-foerderungen/ufg/sanierung-kesselaustausch-2027.html"),
        ("Sanierungsoffensive: Neuauflage Kesseltausch Ein-/Zweifamilienhaus 2026",
         "https://www.sanierungsoffensive.gv.at/kesseltausch/neuauflage-ein-/zweifamilienhaus-oder-reihenhaus"),
        ("Land Steiermark: Förderung für Heizungen",
         "https://www.wohnbau.steiermark.at/cms/ziel/164947118/DE/"),
        ("E-Control: Strom- und Gaspreismonitor November 2026", "https://www.e-control.at/preismonitor"),
    ],
    "related": [
        ("waermepumpe", "Wärmepumpen-Installateur in Kärnten und Steiermark"),
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau: Voraussetzungen und Beispiele"),
        ("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"),
        ("/waermepumpe-stromverbrauch/", "Stromverbrauch einer Wärmepumpe"),
    ],
    "cta": {
        "h3": "Reichen Ihre Heizkörper?",
        "text": "Wir prüfen Heizkörper und Vorlauftemperatur vor Ort und planen die Wärmepumpe passend dazu.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Wärmepumpe mit Ihren Heizkörpern, ehrlich geprüft",
    "final_text": ("Kostenlose Erstberatung zu Wärmepumpe, Heizkörpern, Photovoltaik und Förderung, mit "
                   "transparenten Zahlen und einem Ansprechpartner aus Villach."),
}
