"""Ratgeber: Kosten einer Wärmepumpe 2026 (Anschaffung, Betrieb, Förderung).

Migriert von ebz-photovoltaik.at/kosten-einer-waermepumpe/ (Stand März 2026).
Bereinigt: Der Abschnitt "Erdwärmepumpe" war in der Quelle ein Copy-Paste des
Luftwärmepumpen-Absatzes und wurde aus den Zahlen der Kostenübersicht neu geschrieben.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "kosten-einer-waermepumpe",
    "path": "/kosten-einer-waermepumpe/",
    "title": "Kosten einer Wärmepumpe 2026: Anschaffung & Betrieb | EBZ",
    "description": ("Was kostet eine Wärmepumpe 2026? Luft-Wasser 12.000 bis 22.000 €, Erdwärme bis "
                    "40.000 €, Betrieb ab 700 €/Jahr. Förderung, Wartung und PV-Kombination erklärt."),
    "eyebrow": "Wärmepumpe · Kosten",
    "crumb_label": "Kosten einer Wärmepumpe",
    "h1": "Kosten einer Wärmepumpe 2026: Was Sie für Anschaffung und Betrieb wirklich zahlen",
    "lead": ("Eine Luft-Wasser-Wärmepumpe kostet für ein Einfamilienhaus 12.000 bis 22.000 Euro vor "
             "Förderung, im Betrieb liegt sie mit 700 bis 1.100 Euro pro Jahr deutlich unter Gas und Öl. "
             "Dieser Ratgeber schlüsselt alle Kostenblöcke auf: Gerät, Installation, Neubau und Altbau, "
             "Strom, Wartung und Förderung."),
    "chips": [
        "Luft-Wasser: <b>12.000 bis 22.000 €</b>*",
        "Erdwärme: <b>22.000 bis 40.000 €</b>*",
        "Betrieb: <b>700 bis 1.100 €/Jahr</b>*",
        "Amortisation: <b>8 bis 15 Jahre</b>",
    ],
    "date_published": "2026-02-05",
    "date_modified": "2026-09-24",
    "hero_img": "waermepumpe",
    "hero_alt": "Luft-Wasser-Wärmepumpe als Außeneinheit neben einem Einfamilienhaus",

    "tldr": [
        "Gerätekosten 2026: Luft-Wasser-Wärmepumpe 8.000 bis 18.000 Euro, Erdwärmepumpe 12.000 bis "
        "22.000 Euro, Wasser-Wasser-Wärmepumpe 15.000 bis 25.000 Euro. Dazu kommt die Installation mit "
        "3.000 bis 15.000 Euro je nach Wärmequelle.",
        "Für ein typisches Einfamilienhaus mit 130 bis 180 m² kostet eine Luft-Wasser-Wärmepumpe im "
        "Neubau 14.000 bis 22.000 Euro, im Altbau 16.000 bis 28.000 Euro, jeweils vor Förderung.",
        "Bundes- und Landesförderung reduzieren die Anschaffung je nach Programm um 4.000 bis "
        "12.000 Euro. EBZ Energie übernimmt die komplette Förderabwicklung.",
        "Betrieb: Ein gut gedämmtes Haus mit 12.000 kWh Wärmebedarf braucht bei Jahresarbeitszahl 4 rund "
        "3.000 kWh Strom, also etwa 900 Euro pro Jahr. Eine Gasheizung kostet für dieselbe Wärme 1.400 "
        "bis 1.900 Euro.",
        "Mit eigener Photovoltaikanlage sinken die Heizkosten auf 200 bis 500 Euro pro Jahr. Die "
        "Amortisation der Wärmepumpe liegt typischerweise bei 8 bis 15 Jahren.",
    ],
    "kpis": [
        ("3.000 kWh", "Strombedarf pro Jahr im Beispielhaus*"),
        ("900 €", "Stromkosten pro Jahr bei 0,30 €/kWh*"),
        ("200 bis 500 €", "Heizkosten pro Jahr mit PV-Anlage*"),
        ("150 bis 400 €", "Wartung, alle 2 bis 3 Jahre"),
    ],

    "sections": [
        ("Anschaffungskosten im Überblick: Gerät plus Installation", "anschaffung", f"""
<p>Die Anschaffungskosten einer Wärmepumpe liegen über denen einer Gasheizung. Dieser Vergleich greift
aber zu kurz, weil er laufende Kosten und Lebensdauer ausblendet. Eine Wärmepumpe ist eine Investition,
die sich über Jahre und Jahrzehnte rechnet. Die Anschaffung besteht aus zwei Blöcken: dem Gerät selbst
und der Installation inklusive aller Anpassungen an der bestehenden Haustechnik.</p>
{A.table(
    ["Wärmepumpentyp", "Gerät", "Installation", "Besonderheit"],
    [
        ["Luft-Wasser-Wärmepumpe", "8.000 bis 18.000 €", "3.000 bis 6.000 €",
         "keine Erschließung von Erdreich oder Grundwasser nötig"],
        ["Erdwärmepumpe (Sole-Wasser)", "12.000 bis 22.000 €", "8.000 bis 15.000 €",
         "inklusive Erdkollektor oder Tiefenbohrung"],
        ["Wasser-Wasser-Wärmepumpe", "15.000 bis 25.000 €", "6.000 bis 12.000 €",
         "Förder- und Schluckbrunnen, wasserrechtliche Bewilligung"],
    ],
    hl_cols=(1, 2),
)}
<p>Je nach Gebäude kommen Pufferspeicher, Warmwasserspeicher, Anpassungen am Verteilsystem oder der
Einbau einer Fußbodenheizung dazu. Diese Positionen entscheiden oft darüber, ob ein Projekt am unteren
oder oberen Ende der Spanne landet.</p>
<p><small>*Richtwerte 2026 für Österreich, vor Abzug von Förderungen. Die tatsächlichen Kosten hängen von
Gebäude, Wärmequelle, Heizsystem und Aufwand vor Ort ab.</small></p>
"""),
        ("Luftwärmepumpe, Erdwärmepumpe und Grundwasser im Vergleich", "typen", f"""
<h3>Luft-Wasser-Wärmepumpe: die günstigste und flexibelste Option</h3>
<p>Die Luft-Wasser-Wärmepumpe ist die mit Abstand häufigste Wahl. Sie entzieht der Außenluft
thermische Energie und wandelt sie in Heizwärme um. Weil weder Erdreich noch Grundwasser erschlossen
werden müssen, sind die Gesamtkosten am niedrigsten: Für ein typisches Einfamilienhaus liegen sie
inklusive Installation bei 12.000 bis 22.000 Euro vor Förderung. Der größte Vorteil: Sie lässt sich
praktisch überall aufstellen, ohne Genehmigung für Tiefenbohrungen und ohne besondere
Grundstücksvoraussetzungen.</p>
<h3>Erdwärmepumpe: höhere Investition, konstante Effizienz</h3>
<p>Die Sole-Wasser-Wärmepumpe nutzt die ganzjährig konstante Temperatur des Erdreichs, entweder über
flächige Erdkollektoren oder über eine Tiefenbohrung. Das Gerät kostet 12.000 bis 22.000 Euro, die
Installation inklusive Kollektor oder Bohrung 8.000 bis 15.000 Euro. Für ein Einfamilienhaus ergeben
sich damit Gesamtkosten von 22.000 bis 40.000 Euro vor Förderung. Dafür arbeitet die Anlage auch im
Winter mit gleichbleibend hoher Effizienz und hat entsprechend niedrige Betriebskosten. Voraussetzung
ist ausreichend Grundstücksfläche für Kollektoren oder die Möglichkeit einer Bohrung.</p>
<h3>Wasser-Wasser-Wärmepumpe: die effizienteste Variante</h3>
<p>Diese Variante nutzt Grundwasser als Wärmequelle und erreicht die höchsten Effizienzwerte. Sie
kommt nur dort infrage, wo ausreichend Grundwasser in geeigneter Qualität vorhanden ist und die
wasserrechtliche Bewilligung erteilt wird. Gesamtkosten: 22.000 bis 38.000 Euro vor Förderung.</p>
<p>Wie die drei Systeme technisch arbeiten, erklärt der Ratgeber
{a('/funktionsweise-einer-waermepumpe/', 'Funktionsweise einer Wärmepumpe')}.</p>
"""),
        ("Neubau oder Altbau: So unterscheiden sich die Kosten", "neubau-altbau", f"""
<h3>Neubau: optimale Bedingungen von Anfang an</h3>
<p>Im Neubau wird das Gebäude von Beginn an auf die Wärmepumpe ausgelegt: gute Dämmung, flächige
Wärmeabgabe über Fußbodenheizung und eine auf den tatsächlichen Wärmebedarf abgestimmte Anlagengröße.
Es fallen keine Kosten für Rückbau oder Anpassung alter Systeme an. Für einen typischen Neubau mit
150 m² Wohnfläche rechnet man mit 14.000 bis 25.000 Euro für eine Luft-Wasser-Wärmepumpe inklusive
Anbindung an die Fußbodenheizung und Installation, vor Förderung.</p>
<h3>Altbau: machbar mit Planung</h3>
<p>Beim Heizungstausch im Bestand ist die Luft-Wasser-Wärmepumpe die häufigste Variante. Moderne
Geräte sind für niedrige Vorlauftemperaturen entwickelt und funktionieren auch mit vorhandenen
Heizkörpern, eine Fußbodenheizung ist nicht zwingend nötig. Drei Punkte entscheiden über die Kosten:</p>
<ul>
  <li><b>Dämmzustand:</b> Im schlecht gedämmten Altbau muss die Wärmepumpe mit höheren
  Vorlauftemperaturen arbeiten, was die Effizienz senkt. Fassadendämmung oder neue Fenster verbessern
  die Jahresarbeitszahl erheblich.</li>
  <li><b>Heizkörper und Verteilsystem:</b> Sind die Heizkörper groß genug, um bei niedrigeren
  Vorlauftemperaturen ausreichend Wärme abzugeben? Das prüfen wir bei der Vor-Ort-Besichtigung.</li>
  <li><b>Fußbodenheizung nachrüsten:</b> Je nach System (Nassestrich oder Trockensystem) kostet die
  nachträgliche Installation 50 bis 120 Euro pro Quadratmeter. Alternativen sind großflächige oder
  spezielle Niedertemperatur-Heizkörper.</li>
</ul>
<p>Die Gesamtkosten für eine Wärmepumpe im Altbau liegen inklusive aller Anpassungen bei rund 15.000
bis 30.000 Euro vor Förderung. Details, Rechenbeispiele und Voraussetzungen finden Sie im Ratgeber
{a('/waermepumpe-im-altbau/', 'Wärmepumpe im Altbau')}.</p>
"""),
        ("Richtwerte für ein Einfamilienhaus 2026", "einfamilienhaus", f"""
<p>Das Einfamilienhaus ist der häufigste Anwendungsfall. Für ein durchschnittliches Haus mit 130 bis
180 m² Wohnfläche in Österreich gelten 2026 folgende Richtwerte, jeweils gesamt und vor Förderung:</p>
{A.table(
    ["System", "Gesamtkosten vor Förderung*"],
    [
        ["Luft-Wasser-Wärmepumpe im Neubau", "14.000 bis 22.000 €"],
        ["Luft-Wasser-Wärmepumpe im Altbau", "16.000 bis 28.000 €"],
        ["Erdwärmepumpe (Neubau oder Altbau)", "22.000 bis 40.000 €"],
    ],
    hl_cols=(1,),
)}
<p>Nach Abzug der Bundesförderung „Raus aus Öl und Gas“, der Landesförderung Kärnten beziehungsweise
Steiermark und allfälliger kommunaler Programme reduzieren sich diese Summen deutlich. Zum Vergleich:
Eine {a('photovoltaik', 'Photovoltaikanlage')} mit 10 kWp und Speicher kostet rund 15.000 bis
22.000 Euro vor Förderung, die Kombination aus beidem senkt die Energiekosten am stärksten.</p>
{A.cta("Was kostet die Wärmepumpe für Ihr Haus?",
       "Wir prüfen Gebäude, Heizsystem und Förderhöhe kostenlos vor Ort und erstellen ein "
       "transparentes Festpreisangebot.",
       secondary=("waermepumpe", "Zum Wärmepumpen-Installateur"))}
"""),
        ("Förderung: Wie viel bekommen Sie zurück?", "foerderung", f"""
<p>Die Anschaffung einer Wärmepumpe wird in Österreich aus mehreren Quellen gleichzeitig gefördert.
Zusammengenommen können die Zuschüsse die Investition je nach Bundesland und Programm um 4.000 bis
12.000 Euro senken.</p>
<ul>
  <li><b>Bundesförderung „Raus aus Öl und Gas“:</b> Wer eine fossile Heizung durch eine Wärmepumpe
  ersetzt, erhält einen Investitionszuschuss von mehreren tausend Euro, förderfähig sind Gerät und
  Installation. Aktuelle Konditionen: {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive 2026')}
  und {a('/sauber-heizen-fuer-alle-2026/', 'Sauber Heizen für Alle 2026')} für einkommensschwache
  Haushalte.</li>
  <li><b>Landesförderung Kärnten und Steiermark:</b> Beide Bundesländer haben eigene Programme, deren
  Höhe je nach Antragsjahr variiert. Überblick: {a('/landesfoerderungen-fuer-die-waermepumpe/',
  'Landesförderungen für die Wärmepumpe')}.</li>
  <li><b>Steuer:</b> Zusätzlich lässt sich der Heizungstausch über die
  {a('/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/',
  'Öko-Sonderausgabenpauschale')} steuerlich geltend machen.</li>
</ul>
{A.box("Damit die Förderung genehmigt wird, muss der Installateur bestimmte Zertifizierungen erfüllen "
       "und die Anlage mit förderfähigen Geräten umgesetzt werden. EBZ Energie erfüllt als "
       "zertifizierter Fachbetrieb alle Anforderungen und übernimmt die Förderabwicklung von der "
       "Antragstellung bis zur Auszahlung.")}
<p>Alle Programme im Detail: {a('/waermepumpenfoerderung-in-oesterreich/',
'Wärmepumpenförderung in Österreich')}.</p>
"""),
        ("Stromverbrauch und Betriebskosten: Was der Betrieb wirklich kostet", "betriebskosten", f"""
<p>Die Betriebskosten entscheiden über die langfristige Wirtschaftlichkeit, und hier liegt die Stärke
der Wärmepumpe: Aus einer Kilowattstunde Strom erzeugt sie 4 bis 5 Kilowattstunden Wärme. Der
Stromverbrauch hängt von zwei Größen ab:</p>
<ul>
  <li><b>Wärmebedarf des Gebäudes:</b> Ein gut gedämmtes Einfamilienhaus braucht rund 8.000 bis
  12.000 kWh Wärme pro Jahr, ein älteres, ungedämmtes Gebäude 20.000 kWh und mehr.</li>
  <li><b>Jahresarbeitszahl (JAZ):</b> Sie gibt an, wie viel Wärme pro eingesetzter Kilowattstunde Strom
  entsteht. JAZ 4 bedeutet: 1 kWh Strom ergibt 4 kWh Wärme. Moderne Geräte erreichen je nach Typ und
  Einsatzort eine JAZ von 3,5 bis 5.</li>
</ul>
{A.box_dark("Rechenbeispiel Einfamilienhaus*",
    "Wärmebedarf 12.000 kWh/Jahr, JAZ 4,0: Die Wärmepumpe verbraucht 3.000 kWh Strom pro Jahr. Bei "
    "0,30 €/kWh sind das rund 900 Euro Stromkosten. Eine Gasheizung kostet für denselben Wärmebedarf "
    "etwa 1.400 bis 1.900 Euro pro Jahr.")}
<h3>Heizkosten im Vergleich: Wärmepumpe, Gas, Öl</h3>
{A.table(
    ["Heizsystem", "Jahreskosten bei 12.000 kWh Wärmebedarf*"],
    [
        ["Gasheizung (Erdgas)", "1.400 bis 1.900 €"],
        ["Ölheizung", "1.500 bis 2.200 €"],
        ["Luft-Wasser-Wärmepumpe", "700 bis 1.100 €"],
        ["Wärmepumpe + PV-Anlage", "200 bis 500 €"],
    ],
    hl_cols=(1,),
)}
<h3>Wartungskosten</h3>
<p>Anders als eine Gasheizung mit jährlicher Abgasmessung und Brennereinstellung braucht eine
Wärmepumpe nur alle 2 bis 3 Jahre eine professionelle Inspektion. Je nach Anbieter und Aufwand kostet
ein Wartungstermin 150 bis 400 Euro. Größere Reparaturen sind bei Qualitätsgeräten selten,
vorausgesetzt die Installation erfolgte fachgerecht.</p>
<p><small>*Richtwerte bei einem Strompreis von 0,30 €/kWh und aktuellen Gas- und Ölpreisen. Ihre
tatsächlichen Kosten hängen von Wärmebedarf, Jahresarbeitszahl und Tarif ab.</small></p>
"""),
        ("Wärmepumpe und Photovoltaik: Heizkosten auf 200 bis 500 Euro senken", "photovoltaik", f"""
<p>Die Wärmepumpe ist der größte Stromverbraucher im Haushalt, und genau diesen Strom kann eine
PV-Anlage auf dem Dach liefern. Statt 0,30 Euro pro Kilowattstunde aus dem Netz nutzen Sie eigenen
Solarstrom zu nahezu null Grenzkosten. Die Betriebskosten der Wärmepumpe sinken damit in vielen Fällen
auf 200 bis 500 Euro im Jahr. Ein {a('batteriespeicher', 'Batteriespeicher')} stellt den Sonnenstrom
auch abends und nachts bereit, ein {a('ems', 'Energiemanagementsystem')} lässt die Wärmepumpe dann
laufen, wenn Überschuss vorhanden ist.</p>
<p>Beide Systeme werden separat gefördert, die Gesamtinvestition amortisiert sich entsprechend
schneller. EBZ Energie plant und installiert Wärmepumpe und Photovoltaik aus einer Hand, mit einer
einzigen Förderabwicklung. Mehr dazu im Ratgeber
{a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}.</p>
<h3>Vier Hebel für mehr Effizienz</h3>
<ul>
  <li><b>Richtige Dimensionierung:</b> Eine zu große Anlage taktet ständig, eine zu kleine schafft den
  Wärmebedarf nicht. Beides kostet Effizienz und Lebensdauer.</li>
  <li><b>Niedertemperatursystem:</b> Bei 35 °C Vorlauf statt 70 °C arbeitet die Wärmepumpe deutlich
  effizienter. Fußbodenheizung oder großflächige Heizkörper sind im Vorteil.</li>
  <li><b>Smarte Steuerung:</b> Eine Regelung, die die Wärmepumpe bei viel Solarstrom betreibt, senkt
  die Stromkosten spürbar.</li>
  <li><b>Regelmäßige Wartung:</b> Ohne Wartung kann sich die Jahresarbeitszahl über die Jahre
  verschlechtern.</li>
</ul>
"""),
        ("Fazit: Lohnen sich die Kosten einer Wärmepumpe?", "fazit", f"""
<p>Ja, und zwar deutlicher, als viele erwarten. Die Anschaffung liegt über einer Gasheizung, aber über
die Lebensdauer gerechnet ist die Wärmepumpe mit niedrigeren Betriebskosten, staatlicher Förderung und
der Möglichkeit, den Strom selbst zu erzeugen, die wirtschaftlichste Heizlösung für Hausbesitzer in
Österreich. Die Amortisation liegt typischerweise bei 8 bis 15 Jahren, danach heizen Sie für einen
Bruchteil der bisherigen Kosten.</p>
<ul>
  <li>Luft-Wasser-Wärmepumpe: die günstigste und flexibelste Lösung für die meisten Gebäude</li>
  <li>Förderungen von Bund und Land reduzieren die Investition um 4.000 bis 12.000 Euro</li>
  <li>Betriebskosten von 700 bis 1.100 Euro pro Jahr statt 1.400 bis 2.200 Euro bei Gas oder Öl</li>
  <li>Mit Photovoltaik sinken die Heizkosten auf 200 bis 500 Euro pro Jahr</li>
</ul>
{A.cta("Kostenlose Erstberatung für Ihre Wärmepumpe",
       "Wir analysieren Ihr Gebäude, berechnen Ihre persönliche Förderhöhe und zeigen Ihnen ehrlich, "
       "was eine Wärmepumpe für Ihr Zuhause kostet.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Wärmepumpe und Förderung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Wärmepumpen, Photovoltaik und Speicher in "
                 "Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. "
                 "Sie erhalten ein Festpreisangebot mit allen Positionen, wir übernehmen Bundes- und "
                 "Landesförderung und stimmen Wärmepumpe und PV-Anlage von Anfang an aufeinander ab."),
        "grid": [
            ("Festpreis statt Überraschungen", "Alle Kosten von Gerät bis Inbetriebnahme in einem Angebot."),
            ("Förderung komplett abgewickelt", "Bund, Land und Steuer: wir reichen ein, Sie erhalten die Zuschüsse."),
            ("Wärmepumpe plus Photovoltaik", "Ein Konzept, ein Team, eine Förderabwicklung."),
            ("Vor-Ort-Analyse kostenlos", "Dämmung, Heizkörper und Wärmebedarf prüfen wir bei Ihnen zu Hause."),
        ],
    },

    "faq": [
        ("Wie viel kostet eine Wärmepumpe für ein Einfamilienhaus in Österreich?",
         "Als Richtwert 2026 kostet eine Luft-Wasser-Wärmepumpe für ein typisches Einfamilienhaus 14.000 "
         "bis 28.000 Euro inklusive Installation, vor Förderung. Im Neubau liegt sie am unteren, im Altbau "
         "am oberen Ende. Eine Erdwärmepumpe kostet 22.000 bis 40.000 Euro."),
        ("Wie viel Strom verbraucht eine Wärmepumpe im Jahr?",
         "Für ein gut gedämmtes Einfamilienhaus rechnet man mit 3.000 bis 5.000 kWh Strom pro Jahr. Bei "
         "12.000 kWh Wärmebedarf und einer Jahresarbeitszahl von 4 sind es 3.000 kWh, also rund 900 Euro "
         "Stromkosten bei 0,30 Euro je Kilowattstunde."),
        ("Was kostet die Wärmepumpe nach Abzug der Förderung?",
         "Je nach Bundesland und Programm reduzieren Bundes- und Landesförderung die Anschaffung um 4.000 "
         "bis 12.000 Euro. Aus 20.000 Euro vor Förderung können so 8.000 bis 16.000 Euro Eigenanteil werden. "
         "EBZ Energie berechnet Ihre individuelle Förderhöhe kostenlos."),
        ("Amortisiert sich eine Wärmepumpe wirklich?",
         "Ja, in den meisten Fällen innerhalb von 8 bis 15 Jahren. Entscheidend sind die ausgeschöpfte "
         "Förderung, der Zustand des Gebäudes und die Kombination mit einer PV-Anlage, die die "
         "Betriebskosten auf 200 bis 500 Euro pro Jahr senkt."),
        ("Lohnt sich eine Wärmepumpe auch im Altbau?",
         "Ja, vor allem wenn das Gebäude ausreichend gedämmt ist oder gleichzeitig saniert wird. Eine "
         "Luft-Wasser-Wärmepumpe ist im Altbau meist problemlos möglich, die Gesamtkosten liegen bei 15.000 "
         "bis 30.000 Euro vor Förderung. Entscheidend ist eine ehrliche Vorabanalyse vor Ort."),
        ("Was kostet die Wartung einer Wärmepumpe?",
         "Empfohlen wird eine Inspektion alle 2 bis 3 Jahre, ein Termin kostet je nach Anbieter 150 bis "
         "400 Euro. Eine jährliche Abgasmessung wie bei Gas oder Öl entfällt."),
        ("Was kostet eine Fußbodenheizung im Altbau zusätzlich?",
         "Die nachträgliche Installation kostet je nach System 50 bis 120 Euro pro Quadratmeter. Oft "
         "reichen aber großflächige oder Niedertemperatur-Heizkörper, die deutlich günstiger sind."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Wärmepumpen, PV-Anlagen und Speicher in Kärnten und der Steiermark und übernimmt die "
                    "Förderabwicklung. Alle Preisangaben sind Richtwerte aus der Projektpraxis 2026. Keine "
                    "Rechts- oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "related": [
        ("waermepumpe", "Wärmepumpen-Installateur in Kärnten und Steiermark"),
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau: Lohnt sie sich?"),
        ("/waermepumpenfoerderung-in-oesterreich/", "Wärmepumpenförderung in Österreich"),
        ("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"),
    ],
    "cta": {
        "h3": "Kosten und Förderung berechnen",
        "text": "Kostenlose Vor-Ort-Analyse, Festpreisangebot und Förderabwicklung aus einer Hand.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre Wärmepumpe, ehrlich kalkuliert",
    "final_text": ("Kostenlose Erstberatung, transparente Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
