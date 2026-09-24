"""Ratgeber: Heizen mit Wärmepumpe (Funktion, Arten, Kosten, Förderung, PV).

Migriert von ebz-photovoltaik.at/heizen-mit-waermepumpe/ (Stand März 2026).
Bereinigt: Montage-Formulierung auf "zertifizierte Fachkräfte" umgestellt; Kostenspannen an den Kostenratgeber
angeglichen (Quelle nannte für Sole- und Wasser-Wasser abweichende Werte).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "heizen-mit-waermepumpe",
    "path": "/heizen-mit-waermepumpe/",
    "title": "Heizen mit Wärmepumpe: Funktion, Kosten, Förderung | EBZ",
    "description": ("Heizen mit Wärmepumpe erklärt: JAZ 3 bis 5, rund 3.000 kWh Strom pro Jahr im "
                    "Einfamilienhaus, 840 € Ersparnis gegenüber Gas. Arten, Kosten, Förderung."),
    "eyebrow": "Wärmepumpe · Grundlagen",
    "crumb_label": "Heizen mit Wärmepumpe",
    "h1": "Heizen mit Wärmepumpe: 75 Prozent der Wärme kommen kostenlos aus der Umwelt",
    "lead": ("Eine Wärmepumpe macht aus einer Kilowattstunde Strom drei bis fünf Kilowattstunden Wärme und "
             "heizt damit günstiger als jede Gas- oder Ölheizung. Dieser Ratgeber erklärt Funktionsweise, "
             "die drei Wärmepumpenarten, geeignete Heizsysteme, Stromverbrauch, Kosten, Förderung und die "
             "Kombination mit Photovoltaik."),
    "chips": [
        "Jahresarbeitszahl: <b>3,5 bis 5</b>",
        "Strombedarf: <b>rund 3.000 kWh/Jahr</b>*",
        "Ersparnis vs. Gas: <b>ca. 840 €/Jahr</b>*",
        "Montage: <b>2 bis 4 Tage</b>",
    ],
    "date_published": "2026-02-15",
    "date_modified": "2026-09-24",
    "hero_img": "waermepumpe",
    "hero_alt": "Wärmepumpe im Garten eines Einfamilienhauses in Kärnten",

    "tldr": [
        "Eine Wärmepumpe arbeitet wie ein Kühlschrank in umgekehrter Richtung: Sie entzieht Luft, Erdreich "
        "oder Grundwasser Wärme und hebt sie über einen Kältemittelkreislauf auf Heiztemperatur. Es findet "
        "keine Verbrennung statt.",
        "Rund 75 Prozent der Heizenergie kommen aus der Umwelt, 25 Prozent aus Strom. Bei einer "
        "Jahresarbeitszahl von 4 ergibt 1 kWh Strom 4 kWh Wärme, eine Gasheizung schafft aus 1 kWh Gas "
        "höchstens 0,95 kWh.",
        "Ein gut gedämmtes Einfamilienhaus mit 12.000 kWh Wärmebedarf braucht rund 3.000 kWh Strom pro "
        "Jahr, bei 0,25 bis 0,35 €/kWh also 750 bis 1.050 Euro. Eine Gasheizung liegt bei rund 1.700 Euro.",
        "Luft-Wasser-Wärmepumpen sind mit 12.000 bis 22.000 Euro vor Förderung die günstigste und "
        "flexibelste Variante, sie arbeiten in Kärnten und der Steiermark auch bei Temperaturen weit "
        "unter null Grad.",
        "In Kombination mit Photovoltaik und Speicher sinken die Heizkosten auf 200 bis 400 Euro pro Jahr. "
        "Beide Systeme werden separat gefördert.",
    ],
    "kpis": [
        ("75 %", "der Heizwärme stammen aus der Umwelt"),
        ("4 kWh", "Wärme aus 1 kWh Strom bei JAZ 4"),
        ("858 €", "Stromkosten pro Jahr im Beispielhaus*"),
        ("200 bis 400 €", "Heizkosten pro Jahr mit PV-Anlage*"),
    ],

    "sections": [
        ("Wie funktioniert eine Wärmepumpe?", "funktionsweise", f"""
<p>Eine Wärmepumpe nutzt dasselbe physikalische Prinzip wie ein Kühlschrank, nur in umgekehrter
Richtung: Der Kühlschrank transportiert Wärme aus seinem Inneren nach außen, die Wärmepumpe holt Wärme
aus der Umgebung ins Haus. Die Energiequelle ist keine Verbrennung, sondern die kostenlose thermische
Energie aus Luft, Erdreich oder Grundwasser. Strom braucht die Wärmepumpe nur, um diese Wärme auf ein
nutzbares Temperaturniveau anzuheben, und zwar deutlich weniger, als sie an Wärme abgibt.</p>
<p>Herzstück ist ein geschlossener Kältemittelkreislauf mit vier Schritten:</p>
{A.steps([
    ("Verdampfen",
     "Das Kältemittel verdampft schon bei sehr niedrigen Temperaturen und nimmt dabei Wärme aus Luft, "
     "Erdreich oder Grundwasser auf. Auch bei Minusgraden enthält die Umwelt genug Energie dafür."),
    ("Verdichten",
     "Der Verdichter komprimiert das gasförmige Kältemittel. Durch die Kompression steigt seine "
     "Temperatur auf ein Niveau, das zum Heizen nutzbar ist."),
    ("Kondensieren",
     "Das heiße Kältemittel gibt seine Wärme an Fußbodenheizung, Heizkörper oder Warmwasserspeicher ab, "
     "kühlt dabei ab und wird wieder flüssig."),
    ("Entspannen",
     "Ein Ventil senkt den Druck, das Kältemittel kühlt weiter ab und ist bereit, erneut Umweltwärme "
     "aufzunehmen. Der Kreislauf beginnt von vorn."),
])}
<p>Den Kreislauf mit COP, Jahresarbeitszahl und Kältemittel im Detail erklärt der Ratgeber
{a('/funktionsweise-einer-waermepumpe/', 'Funktionsweise einer Wärmepumpe')}.</p>
"""),
        ("Wie effizient ist eine Wärmepumpe? JAZ, Vorlauftemperatur, Stromverbrauch", "effizienz", f"""
<p>Die Effizienz einer Wärmepumpe drückt die <b>Jahresarbeitszahl (JAZ)</b> aus: Sie gibt an, wie viel
Wärme pro eingesetzter Kilowattstunde Strom über ein ganzes Jahr entsteht. JAZ 4,0 bedeutet, aus 1 kWh
Strom werden 4 kWh Wärme, drei Viertel davon liefert die Umwelt. Zum Vergleich: Eine Gasheizung
erzeugt aus 1 kWh Gas bestenfalls 0,95 kWh Wärme. Moderne Wärmepumpen erreichen je nach Typ, Standort
und Gebäude eine JAZ von 3 bis 5.</p>
<p>Der zweite entscheidende Faktor ist die <b>Vorlauftemperatur</b>: Je niedriger das Heizsystem sie
braucht, desto effizienter arbeitet die Wärmepumpe. Fußbodenheizungen mit 30 bis 35 °C sind ideal,
Heizkörper brauchen höhere Temperaturen und senken die Effizienz etwas, bleiben aber deutlich besser
als jede fossile Heizung.</p>
<h3>Stromverbrauch: Was Sie einplanen müssen</h3>
<p>Faustregel: 25 Prozent der Heizenergie liefert der Strom, 75 Prozent kommen kostenlos aus der
Umwelt. Für ein gut gedämmtes Einfamilienhaus mit 12.000 kWh Jahreswärmebedarf und JAZ 4 bedeutet das
rund 3.000 kWh Strom pro Jahr für Heizung und Warmwasser. Bei einem Arbeitspreis von derzeit etwa 0,25
bis 0,35 €/kWh sind das 750 bis 1.050 Euro Betriebskosten im Jahr. Drei Faktoren bestimmen den
Verbrauch:</p>
<ul>
  <li><b>Typ der Wärmepumpe:</b> Wasser-Wasser hat den niedrigsten Stromverbrauch, gefolgt von
  Sole-Wasser. Luft-Wasser liegt etwas höher, ist dafür am flexibelsten und günstigsten.</li>
  <li><b>Vorlauftemperatur:</b> Fußbodenheizung schlägt Heizkörper klar.</li>
  <li><b>Dämmzustand:</b> Ein gut gedämmtes Gebäude braucht weniger Wärme und damit weniger Strom.</li>
</ul>
<p><small>*Richtwerte. Der tatsächliche Verbrauch hängt von Wärmebedarf, Jahresarbeitszahl und
Stromtarif ab.</small></p>
"""),
        ("Arten von Wärmepumpen: Welche Wärmequelle passt zu Ihrem Gebäude?", "arten", f"""
<p>Der wichtigste Unterschied zwischen Wärmepumpen liegt in der genutzten Energiequelle. Drei Systeme
sind für Wohngebäude relevant:</p>
{A.table(
    ["System", "Wärmequelle", "Stärke", "Voraussetzung"],
    [
        ["Luft-Wasser-Wärmepumpe", "Außenluft",
         "überall installierbar, keine Bohrung, geringster Aufwand, im Neubau wie im Altbau",
         "Aufstellplatz für die Außeneinheit"],
        ["Sole-Wasser-Wärmepumpe (Erdwärme)", "Erdreich über Kollektor oder Tiefenbohrung",
         "ganzjährig konstante Quellentemperatur, hohe Effizienz, niedrige Betriebskosten",
         "Grundstücksfläche für Kollektoren oder Bohrmöglichkeit"],
        ["Wasser-Wasser-Wärmepumpe", "Grundwasser mit konstant 10 bis 12 °C",
         "höchste Effizienz aller Typen",
         "ausreichend Grundwasser in geeigneter Qualität, wasserrechtliche Bewilligung"],
    ],
)}
<p>Moderne Luft-Wasser-Wärmepumpen arbeiten effizient bis weit unter 0 °C, auch in strengen Wintern in
Kärnten oder der Steiermark. Bei sehr tiefen Außentemperaturen sinkt die Effizienz etwas, weil die
Differenz zwischen Außenluft und Vorlauftemperatur wächst. Für die meisten Wohngebäude in Österreich
ist sie dennoch die beste Lösung. Bei der Wasser-Wasser-Wärmepumpe unterstützen wir Sie bei der
Bewilligung der Grundwassernutzung.</p>
"""),
        ("Heizsysteme und Gebäude: Fußbodenheizung, Heizkörper, Neubau, Altbau", "heizsysteme", f"""
<p>Die Wärmepumpe arbeitet am besten mit Niedertemperatur-Heizsystemen. Je niedriger die
Vorlauftemperatur, desto geringer der Stromverbrauch.</p>
<ul>
  <li><b>Fußbodenheizung, das ideale System:</b> Sie verteilt die Wärme großflächig und braucht nur 30
  bis 35 °C Vorlauf. Im Neubau ist sie Standard, in Kombination mit der Wärmepumpe die optimale Lösung.</li>
  <li><b>Heizkörper, mit Einschränkungen:</b> Auch mit vorhandenen Heizkörpern lässt sich eine
  Wärmepumpe betreiben, allerdings mit höheren Vorlauftemperaturen. Großflächige oder spezielle
  Niedertemperatur-Heizkörper lösen das Problem in vielen Fällen.</li>
  <li><b>Warmwasser inklusive:</b> Die Wärmepumpe übernimmt neben dem Heizen die Warmwasserbereitung
  für Duschen, Baden und Haushalt, ein einziges System für beides.</li>
</ul>
<h3>Neubau: die Standardlösung</h3>
<p>Im Neubau wird das Gebäude von Anfang an auf die Wärmepumpe ausgelegt: gute Dämmung,
Fußbodenheizung und eine auf den tatsächlichen Wärmebedarf abgestimmte Anlagengröße. Hier erreichen
Wärmepumpen die höchsten Effizienzwerte und die niedrigsten Betriebskosten.</p>
<h3>Altbau: machbar mit der richtigen Planung</h3>
<p>Eine Luft-Wasser-Wärmepumpe eignet sich grundsätzlich auch für ältere Gebäude. Entscheidend ist
der Dämmzustand: Je besser gedämmt, desto niedriger die Vorlauftemperatur und desto effizienter der
Betrieb. Im schlecht gedämmten Altbau empfehlen wir, den Heizungstausch mit Dämmmaßnahmen zu
kombinieren. Alle Voraussetzungen, Rechenbeispiele und Kosten finden Sie im Ratgeber
{a('/waermepumpe-im-altbau/', 'Wärmepumpe im Altbau')}.</p>
{A.cta("Passt eine Wärmepumpe zu Ihrem Haus?",
       "Wir prüfen Dämmung, Heizkörper und Wärmebedarf kostenlos vor Ort und sagen Ihnen ehrlich, "
       "welches System für Ihr Gebäude sinnvoll ist.",
       secondary=("waermepumpe", "Zum Wärmepumpen-Installateur"))}
"""),
        ("Kosten und Förderung: Was Sie einplanen sollten", "kosten-foerderung", f"""
<p>Die Kosten einer Wärmepumpe teilen sich in Anschaffung, Installation und laufenden Betrieb. Sie
hängen von der Wärmequelle, der Gebäudegröße und dem Zustand der bestehenden Heizungsanlage ab. Als
grobe Orientierung für ein typisches Einfamilienhaus, jeweils gesamt und vor Förderung:</p>
{A.table(
    ["System", "Gesamtkosten inkl. Installation*"],
    [
        ["Luft-Wasser-Wärmepumpe", "12.000 bis 22.000 €"],
        ["Sole-Wasser-Wärmepumpe (Erdwärme)", "22.000 bis 40.000 €"],
        ["Wasser-Wasser-Wärmepumpe", "22.000 bis 38.000 €"],
    ],
    hl_cols=(1,),
)}
<p>Alle Kostenblöcke, Rechenbeispiele und Wartungskosten im Detail:
{a('/kosten-einer-waermepumpe/', 'Kosten einer Wärmepumpe 2026')}.</p>
<h3>Förderung: Bund und Land gleichzeitig</h3>
<ul>
  <li><b>Bundesförderung „Raus aus Öl und Gas“:</b> Wer eine fossile Heizung durch eine Wärmepumpe
  ersetzt, erhält einen Investitionszuschuss von mehreren tausend Euro. Die Höhe richtet sich nach
  Gebäudetyp und Wärmepumpe. Details: {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive 2026')}.</li>
  <li><b>Landesförderung Kärnten und Steiermark:</b> Beide Bundesländer haben eigene Programme.
  Überblick: {a('/landesfoerderungen-fuer-die-waermepumpe/', 'Landesförderungen für die Wärmepumpe')}.</li>
</ul>
<p>Als zertifizierter Fachbetrieb übernimmt EBZ Energie die gesamte Förderabwicklung von der
Antragstellung bis zur Auszahlung. Alle Programme im Überblick:
{a('/waermepumpenfoerderung-in-oesterreich/', 'Wärmepumpenförderung in Österreich')}.</p>
<p><small>*Richtwerte 2026, vor Abzug von Förderungen.</small></p>
"""),
        ("Wärmepumpe und Photovoltaik: Heizen und Kühlen mit eigenem Strom", "photovoltaik", f"""
<p>Die Wärmepumpe ist der größte Stromverbraucher im Haushalt, und genau diesen Strom kann eine
PV-Anlage auf dem Dach liefern. Scheint die Sonne, heizt die Wärmepumpe mit Solarstrom, bereitet
Warmwasser oder lädt den Pufferspeicher vor. Überschuss landet im
{a('batteriespeicher', 'Batteriespeicher')}, damit die Wärmepumpe auch abends und nachts mit eigenem
Strom läuft. Die effektiven Heizkosten sinken so in vielen Fällen auf 200 bis 400 Euro pro Jahr für ein
komplettes Einfamilienhaus. Beide Systeme werden separat gefördert, die Gesamtinvestition amortisiert
sich schneller.</p>
<p>Diese Kombination empfehlen wir bei EBZ in den meisten Fällen. Wie Sie PV-Anlage, Speicher und
Wärmepumpe richtig dimensionieren, lesen Sie im Ratgeber
{a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}.</p>
<h3>Kühlen mit der Wärmepumpe: der unterschätzte Zusatznutzen</h3>
<p>Moderne Wärmepumpen können im Sommer auch kühlen. Dazu wird der Kreislauf umgekehrt: Die Wärmepumpe
entzieht dem Wohnraum Wärme und gibt sie nach außen ab. Eine separate Klimaanlage wird überflüssig, ein
System heizt, kühlt und bereitet Warmwasser.</p>
"""),
        ("Praxisbeispiel: Einfamilienhaus in Kärnten", "praxisbeispiel", f"""
<p>Wie effizient eine Wärmepumpe wirklich ist, zeigt ein konkretes Beispiel: ein Einfamilienhaus mit
150 m² in Kärnten, Baujahr 2005, gut gedämmt, mit Fußbodenheizung.</p>
{A.table(
    ["Kennzahl", "Wert*"],
    [
        ["Wärmebedarf", "12.000 kWh/Jahr"],
        ["Wärmepumpe", "Luft-Wasser, JAZ 4,2"],
        ["Stromverbrauch", "ca. 2.860 kWh/Jahr"],
        ["Stromkosten bei 0,30 €/kWh", "ca. 858 €/Jahr"],
        ["Vergleich Gasheizung", "ca. 1.700 €/Jahr"],
        ["Ersparnis", "ca. 840 €/Jahr"],
    ],
    hl_cols=(1,),
)}
<p>Über die Lebensdauer der Anlage summiert sich diese Differenz auf einen fünfstelligen Betrag, noch
ohne Photovoltaik. Mit eigener PV-Anlage fällt der größte Teil der 858 Euro Stromkosten weg.</p>
<p><small>*Beispielrechnung mit Richtwerten. Ihre Zahlen hängen von Gebäude, Tarif und Nutzung ab.</small></p>
"""),
        ("So läuft der Umstieg mit EBZ Energie ab", "ablauf", f"""
<p>Wer sich für eine Wärmepumpe entscheidet, sollte von Anfang an auf einen erfahrenen Partner setzen.
Bei EBZ Energie begleiten wir Sie von der ersten Frage bis zum ersten warmen Heiztag und darüber
hinaus:</p>
{A.steps([
    ("Kostenlose Erstberatung",
     "Wir analysieren Ihren Wärmebedarf und Ihr Gebäude und zeigen Ihnen ehrlich, welche Wärmepumpe "
     "zu Ihrer Situation passt. Ohne Druck, ohne Verpflichtung."),
    ("Vor-Ort-Besichtigung und technische Analyse",
     "Wir prüfen alle baulichen Voraussetzungen: Dämmung, bestehendes Heizsystem, Heizkörper und die "
     "Möglichkeiten für Erdkollektoren oder eine Tiefenbohrung."),
    ("Planung und Festpreisangebot",
     "Sie erhalten ein detailliertes Angebot mit einer klaren Aufstellung aller Kosten, ohne versteckte "
     "Posten."),
    ("Förderabwicklung",
     "Wir übernehmen alle Förderanträge: Bundesförderung, Landesförderung Kärnten oder Steiermark und "
     "auf Wunsch auch die Förderung für eine Photovoltaikanlage."),
    ("Montage durch zertifizierte Fachkräfte",
     "Die eigentliche Montage dauert in der Regel 2 bis 4 Tage und erfolgt durch unser festangestelltes "
     "Team aus zertifizierten Fachkräften."),
    ("Inbetriebnahme und Übergabe",
     "Wir nehmen die Anlage in Betrieb, erklären alle Funktionen und bleiben Ihr Ansprechpartner für "
     "Wartung und Service."),
])}
"""),
        ("Fazit: Lohnt sich das Heizen mit Wärmepumpe?", "fazit", f"""
<p>Für die meisten Haushalte in Österreich klar ja. Eine Wärmepumpe heizt effizienter als jedes andere
verfügbare System, nutzt Energie aus der Umwelt, erzeugt im Betrieb keine direkten Emissionen, braucht
kaum Wartung und arbeitet vollautomatisch, auch im strengen Winter. Im Beispielhaus spart sie
gegenüber Gas rund 840 Euro im Jahr, mit Photovoltaik sinken die Heizkosten auf 200 bis 400 Euro. Mit
den aktuellen Förderungen von Bund und Land ist der Einstieg so günstig wie selten.</p>
{A.cta("Jetzt kostenlose Erstberatung vereinbaren",
       "Wir analysieren Ihr Gebäude, berechnen Förderung und Betriebskosten und planen Wärmepumpe und "
       "Photovoltaik als abgestimmtes Gesamtsystem.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Wärmepumpe und Photovoltaik: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Wärmepumpen, Photovoltaik und Speicher in "
                 "Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. "
                 "Wir stimmen Wärmepumpe, PV-Anlage und Speicher aufeinander ab, übernehmen Bundes- und "
                 "Landesförderung und bleiben nach der Inbetriebnahme Ihr Ansprechpartner."),
        "grid": [
            ("Alles aus einer Hand", "Beratung, Planung, Montage und Förderabwicklung vom selben Team."),
            ("Wärmepumpe plus Photovoltaik", "Heizen mit eigenem Solarstrom, beide Systeme separat gefördert."),
            ("Festpreisangebot", "Alle Kosten transparent aufgestellt, keine versteckten Posten."),
            ("Montage in 2 bis 4 Tagen", "Zertifizierte Fachkräfte, Inbetriebnahme und Einschulung inklusive."),
        ],
    },

    "faq": [
        ("Wärmepumpe und Photovoltaik: Passt das zusammen?",
         "Ja, die Wärmepumpe ist der ideale Partner für eine PV-Anlage. Sie verbraucht den selbst "
         "erzeugten Solarstrom direkt und senkt die Heizkosten in vielen Fällen auf 200 bis 400 Euro pro "
         "Jahr. Beide Systeme werden separat gefördert, EBZ plant und installiert sie aus einer Hand."),
        ("Funktioniert eine Wärmepumpe auch bei sehr kalten Wintern?",
         "Ja. Moderne Luft-Wasser-Wärmepumpen arbeiten effizient bis weit unter minus 15 °C. Für besonders "
         "kalte Standorte empfehlen wir Modelle mit erweitertem Betriebsbereich oder eine Erdwärmepumpe, "
         "deren Quelle ganzjährig konstant bleibt."),
        ("Eignet sich eine Wärmepumpe auch ohne Fußbodenheizung?",
         "Ja. Mit modernen Luft-Wasser-Wärmepumpen und großflächigen Niedertemperatur-Heizkörpern "
         "funktioniert das Heizen auch ohne Fußbodenheizung. Die Effizienz ist etwas geringer als mit "
         "Fußbodenheizung bei 30 bis 35 °C Vorlauf, aber deutlich besser als bei jeder fossilen Heizung."),
        ("Wie viel Strom verbraucht eine Wärmepumpe?",
         "Ein gut gedämmtes Einfamilienhaus mit 12.000 kWh Wärmebedarf und Jahresarbeitszahl 4 braucht rund "
         "3.000 kWh Strom pro Jahr, also 750 bis 1.050 Euro bei 0,25 bis 0,35 Euro je Kilowattstunde. "
         "Rund 75 Prozent der Heizenergie kommen kostenlos aus der Umwelt."),
        ("Wie lange dauert die Installation einer Wärmepumpe?",
         "Die eigentliche Montage dauert in der Regel 2 bis 4 Tage. Der gesamte Prozess von der ersten "
         "Beratung bis zur Inbetriebnahme dauert inklusive Förderanträgen und Genehmigungen einige Wochen."),
        ("Was passiert mit der Wärmepumpe bei einem Stromausfall?",
         "Eine Wärmepumpe braucht Strom. Mit PV-Anlage und notstromfähigem Batteriespeicher läuft sie "
         "auch bei einem Ausfall des Netzes weiter und Ihr Zuhause bleibt warm."),
        ("Kann eine Wärmepumpe auch kühlen?",
         "Ja. Moderne Wärmepumpen kehren im Sommer den Kreislauf um, entziehen dem Wohnraum Wärme und "
         "geben sie nach außen ab. Eine separate Klimaanlage ist dann nicht nötig."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Wärmepumpen, PV-Anlagen und Speicher in Kärnten und der Steiermark und übernimmt die "
                    "komplette Förderabwicklung. Alle Verbrauchs- und Kostenangaben sind Richtwerte aus der "
                    "Projektpraxis. Keine Rechts- oder Steuerberatung, maßgeblich sind die offiziellen "
                    "Förderbedingungen."),
    "related": [
        ("waermepumpe", "Wärmepumpen-Installateur in Kärnten und Steiermark"),
        ("/kosten-einer-waermepumpe/", "Kosten einer Wärmepumpe 2026"),
        ("/funktionsweise-einer-waermepumpe/", "Funktionsweise einer Wärmepumpe"),
        ("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"),
    ],
    "cta": {
        "h3": "Wärmepumpe für Ihr Haus?",
        "text": "Kostenlose Vor-Ort-Analyse, Festpreisangebot und Förderabwicklung aus einer Hand.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Heizen mit Energie aus der Umwelt",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
