"""Ratgeber: Wärmepumpe im Altbau (Voraussetzungen, Vorlauftemperatur, Beispiele, Kosten).

Migriert von ebz-photovoltaik.at/waermepumpe-im-altbau/ (Stand März 2026).
Bereinigt: Ersparnis im sanierten Beispiel bezieht sich laut Zahlen auf die alte
Gasheizung vor Sanierung, wurde entsprechend präzisiert.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "waermepumpe-im-altbau",
    "path": "/waermepumpe-im-altbau/",
    "title": "Wärmepumpe im Altbau: Lohnt sie sich? Kosten & Tipps | EBZ",
    "description": ("Wärmepumpe im Altbau: 15.000 bis 28.000 € vor Förderung, JAZ 2,8 bis 4,0 je nach "
                    "Dämmung, 700 bis 2.000 € Ersparnis pro Jahr gegenüber Gas. Was zu beachten ist."),
    "eyebrow": "Wärmepumpe · Altbau",
    "crumb_label": "Wärmepumpe im Altbau",
    "h1": "Wärmepumpe im Altbau: Lohnt sie sich wirklich? Zahlen, Voraussetzungen und Beispiele",
    "lead": ("Dass eine Wärmepumpe nur im Neubau funktioniert, ist überholt: Moderne Geräte sind für den "
             "Bestand entwickelt und heizen auch mit vorhandenen Heizkörpern günstiger als Gas oder Öl. "
             "Dieser Ratgeber zeigt, welche Voraussetzungen zählen, was die Vorlauftemperatur damit zu tun hat "
             "und was ein Altbau von 1985 vor und nach der Sanierung an Heizkosten spart."),
    "chips": [
        "Kosten: <b>15.000 bis 28.000 €</b> vor Förderung*",
        "JAZ im Altbau: <b>2,8 bis 4,0</b>",
        "Ersparnis vs. Gas: <b>700 bis 2.000 €/Jahr</b>*",
        "Montage: <b>2 bis 4 Tage</b>",
    ],
    "date_published": "2026-02-20",
    "date_modified": "2026-09-24",
    "hero_img": "waermepumpe",
    "hero_alt": "Luft-Wasser-Wärmepumpe an der Fassade eines sanierten Altbaus",

    "tldr": [
        "Eine Wärmepumpe im Altbau ist in den meisten Fällen möglich und wirtschaftlich. Entscheidend ist "
        "nicht das Baujahr, sondern Dämmzustand, Heizflächen und die benötigte Vorlauftemperatur.",
        "Fußbodenheizung braucht 30 bis 35 °C Vorlauf, Niedertemperatur-Heizkörper 40 bis 50 °C, "
        "klassische Altbau-Heizkörper oft 60 bis 70 °C. Je niedriger, desto effizienter die Wärmepumpe.",
        "Beispiel Altbau 1985, 160 m², teilweise gedämmt: JAZ 2,8 bis 3,2, Stromkosten 1.680 bis 1.920 "
        "Euro pro Jahr statt 2.400 bis 3.000 Euro mit Gas. Nach Sanierung: JAZ 3,5 bis 4,0 und 900 bis "
        "1.020 Euro pro Jahr.",
        "Große alte Gussheizkörper sind oft überdimensioniert und deshalb gut geeignet. Eine "
        "Fußbodenheizung ist nicht zwingend, das Nachrüsten kostet 50 bis 120 Euro pro Quadratmeter.",
        "Kosten im typischen Altbau-Einfamilienhaus: 15.000 bis 28.000 Euro vor Förderung, nach Bundes- "
        "und Landesförderung 10.000 bis 20.000 Euro. Über 20 Jahre ist die Wärmepumpe meist günstiger als "
        "Gas und Öl.",
    ],
    "kpis": [
        ("30 bis 35 °C", "Vorlauf bei Fußbodenheizung"),
        ("60 bis 70 °C", "Vorlauf klassischer Altbau-Heizkörper"),
        ("50 bis 120 €/m²", "Fußbodenheizung nachrüsten"),
        ("10.000 bis 20.000 €", "Kosten nach Förderung*"),
    ],

    "sections": [
        ("Warum der schlechte Ruf der Wärmepumpe im Altbau nicht verdient ist", "mythos", f"""
<p>Der Ruf der Wärmepumpe im Altbau leidet vor allem unter einem Missverständnis: Viele glauben, sie
brauche zwingend eine Fußbodenheizung und eine Passivhausdämmung. Das war früher teilweise richtig,
heute nicht mehr. Moderne Wärmepumpen sind deutlich leistungsfähiger als noch vor zehn Jahren, arbeiten
auch bei höheren Vorlauftemperaturen effizient und wurden gezielt für den Betrieb im Bestand
optimiert.</p>
<p>Das bedeutet: Auch ein Altbau mit herkömmlichen Heizkörpern, ohne vollständige Dämmung und ohne
Fußbodenheizung lässt sich heute mit einer Wärmepumpe beheizen, vorausgesetzt die Anlage wird richtig
geplant und dimensioniert. Entscheidend ist nicht, ob das Gebäude ein Altbau ist, sondern wie der
Altbau beschaffen ist und welche Maßnahmen sich sinnvoll kombinieren lassen. Genau das analysiert
EBZ Energie kostenlos und ohne Verpflichtung bei Ihnen vor Ort.</p>
"""),
        ("Wann sich die Wärmepumpe im Altbau lohnt und wann Sanierung dazugehört", "voraussetzungen", f"""
<p>Der Betrieb einer Wärmepumpe im Altbau ist besonders wirtschaftlich, wenn folgende Punkte
zutreffen:</p>
<ul>
  <li><b>Gute Dämmung vorhanden oder geplant:</b> Je besser gedämmt, desto niedriger der Wärmebedarf
  und die Vorlauftemperatur, desto effizienter arbeitet die Wärmepumpe. Dämmung und Wärmepumpe
  gemeinsam sind oft der optimale Ansatz.</li>
  <li><b>Großflächige Heizkörper oder Fußbodenheizung:</b> Altbau-Heizkörper sind oft
  überdimensioniert, was für die Wärmepumpe ein Vorteil ist. Große Heizflächen geben auch bei niedrigen
  Vorlauftemperaturen genug Wärme ab.</li>
  <li><b>Wechsel von einer fossilen Heizung:</b> Wer heute mit Öl oder Gas heizt, hat das größte
  Einsparpotenzial. Die Betriebskosten sinken sofort, selbst wenn das Gebäude noch nicht perfekt
  gedämmt ist.</li>
  <li><b>Förderung möglich:</b> Die aktuellen Programme fördern den Kesseltausch im Bestand
  ausdrücklich, Details weiter unten.</li>
</ul>
{A.box("Im schlecht gedämmten Altbau (ungedämmte Außenwände, einfach verglaste Fenster, hohe "
       "Wärmeverluste) ist eine Wärmepumpe technisch möglich, die Effizienz leidet aber. Dann empfehlen "
       "wir, den Heizungstausch mit gezielten Maßnahmen zu kombinieren: Fassadendämmung, Dämmung der "
       "obersten Geschossdecke oder der Kellerdecke sind oft kostengünstig und wirken stark auf die "
       "Effizienz der gesamten Heizanlage.", label="Wann Sanierung dazugehört:")}
"""),
        ("Vorlauftemperatur: der entscheidende Faktor im Altbau", "vorlauftemperatur", f"""
<p>Wer die Diskussion um Wärmepumpen im Altbau verstehen will, muss einen Begriff kennen: die
Vorlauftemperatur. Sie gibt an, wie heiß das Wasser sein muss, das durch Heizkörper oder
Fußbodenheizung fließt, damit der Raum warm wird. Je niedriger die Vorlauftemperatur, desto
effizienter arbeitet die Wärmepumpe und desto geringer der Stromverbrauch.</p>
{A.table(
    ["Heizsystem", "Benötigte Vorlauftemperatur", "Eignung für die Wärmepumpe"],
    [
        ["Fußbodenheizung", "30 bis 35 °C", "ideal"],
        ["Moderne Niedertemperatur-Heizkörper", "40 bis 50 °C", "gut geeignet"],
        ["Klassische Heizkörper im Altbau", "oft 60 bis 70 °C",
         "reduziert die Effizienz, neuere Geräte kommen damit aber zurecht"],
    ],
    hl_cols=(1,),
)}
<p>Hohe Vorlauftemperaturen bedeuten mehr Stromverbrauch, nicht dass die Wärmepumpe im Altbau nicht
funktioniert. Sie arbeitet dann nicht ganz so effizient wie im Neubau mit Fußbodenheizung, ist aber in
den allermeisten Fällen trotzdem günstiger im Betrieb als eine Gas- oder Ölheizung.</p>
"""),
        ("Altbau ohne Fußbodenheizung: Wärmepumpe mit Heizkörpern", "ohne-fussbodenheizung", f"""
<p>Eine der häufigsten Fragen an EBZ: Funktioniert eine Wärmepumpe im Altbau auch ohne
Fußbodenheizung? In den meisten Fällen ja. Entscheidend ist, ob die bestehenden Heizkörper groß genug
sind, um bei niedrigen Vorlauftemperaturen ausreichend Wärme abzugeben. Große, alte Gussheizkörper sind
dabei oft überraschend gut geeignet: Sie wurden früher bewusst überdimensioniert, was ihnen heute
zugutekommt.</p>
<p>Sind die Heizkörper zu klein, gibt es zwei Wege: Entweder werden sie gegen größere
Niedertemperatur-Modelle getauscht, was deutlich günstiger ist als eine neue Fußbodenheizung, oder man
wählt eine Wärmepumpe, die auch bei etwas höheren Vorlauftemperaturen noch effizient arbeitet.</p>
<h3>Fußbodenheizung nachrüsten: Wann lohnt es sich?</h3>
<p>Wer im Altbau auf eine Fußbodenheizung setzen möchte, kann sie nachträglich einbauen lassen. Es gibt
heute schlanke Trockensysteme, die ohne dicken Estrichaufbau auskommen und damit auch in
Bestandsgebäuden realisierbar sind. Die Kosten liegen je nach System bei 50 bis 120 Euro pro
Quadratmeter. Ob sich das lohnt, klären wir gemeinsam bei der Vor-Ort-Begehung.</p>
"""),
        ("Welche Wärmepumpe ist die richtige für den Altbau?", "waermepumpenart", f"""
<h3>Luft-Wasser-Wärmepumpe: die erste Wahl im Altbau</h3>
<p>Für den Altbau ist die Luft-Wasser-Wärmepumpe in den meisten Fällen die beste Wahl. Sie entzieht der
Außenluft Energie, braucht weder Tiefenbohrung noch Erdkollektor und lässt sich in nahezu jedem Altbau
nachrüsten, ohne große Eingriffe in die Bausubstanz. Die kompakte Außeneinheit steht außerhalb des
Gebäudes, was die Installation im Bestand erheblich vereinfacht.</p>
<h3>Sole-Wasser-Wärmepumpe: für Grundstücke mit Platz</h3>
<p>Wer ausreichend Grundstücksfläche für Erdkollektoren oder die Möglichkeit einer Bohrung hat, kann
auch im Altbau auf Erdwärme setzen. Die höheren Installationskosten zahlen sich langfristig durch
niedrigere Betriebskosten aus, weil das Erdreich ganzjährig konstante Temperaturen liefert und die
Effizienz auch im Winter hoch bleibt. Die Unterschiede der Systeme erklärt der Ratgeber
{a('/funktionsweise-einer-waermepumpe/', 'Funktionsweise einer Wärmepumpe')}.</p>
{A.cta("Ist Ihr Altbau bereit für die Wärmepumpe?",
       "Wir prüfen Dämmung, Heizkörper und Vorlauftemperatur kostenlos vor Ort und sagen Ihnen "
       "ehrlich, was in Ihrem Gebäude möglich ist.",
       secondary=("waermepumpe", "Zum Wärmepumpen-Installateur"))}
"""),
        ("Drei Maßnahmen für eine niedrige Vorlauftemperatur", "massnahmen", f"""
<p>Damit die Wärmepumpe effizient läuft, sollte die Vorlauftemperatur so niedrig wie möglich sein.
Das lässt sich im Altbau mit drei Maßnahmen erreichen, die nicht immer teuer sein müssen:</p>
{A.steps([
    ("Dämmung gezielt verbessern",
     "Weniger Wärmeverlust bedeutet weniger Wärmebedarf und damit niedrigere Vorlauftemperaturen. Die "
     "wirksamsten und oft günstigsten Maßnahmen sind die Dämmung der obersten Geschossdecke und der "
     "Kellerdecke sowie der Tausch alter Fenster und Türen."),
    ("Heizflächen vergrößern",
     "Je größer die Heizfläche, desto niedriger kann die Vorlauftemperatur sein. Größere Heizkörper oder "
     "Fußbodenheizung: Beides funktioniert im Altbau, wenn die Dimensionierung stimmt."),
    ("Hydraulischen Abgleich durchführen",
     "Der Abgleich verteilt die Wärme gleichmäßig im Gebäude, kein Raum wird überheizt, keiner bleibt "
     "kalt. Das senkt den Stromverbrauch spürbar und amortisiert sich schnell."),
])}
"""),
        ("Rechenbeispiel: Altbau von 1985 vor und nach der Sanierung", "rechenbeispiel", f"""
<p>Wie effizient arbeitet eine Wärmepumpe im Altbau wirklich? Ein Einfamilienhaus, Baujahr 1985,
160 m², in zwei Zuständen:</p>
{A.table(
    ["Kennzahl", "Teilweise gedämmt, Heizkörper", "Saniert, Niedertemperatur-Heizkörper"],
    [
        ["Benötigte Vorlauftemperatur", "50 bis 55 °C", "40 bis 45 °C"],
        ["Jahresarbeitszahl", "ca. 2,8 bis 3,2", "ca. 3,5 bis 4,0"],
        ["Wärmebedarf", "ca. 18.000 kWh/Jahr", "ca. 12.000 kWh/Jahr"],
        ["Stromverbrauch Wärmepumpe", "ca. 5.600 bis 6.400 kWh/Jahr", "ca. 3.000 bis 3.400 kWh/Jahr"],
        ["Stromkosten bei 0,30 €/kWh", "ca. 1.680 bis 1.920 €/Jahr", "ca. 900 bis 1.020 €/Jahr"],
        ["Bisherige Gasheizung (unsaniert)", "ca. 2.400 bis 3.000 €/Jahr", "ca. 2.400 bis 3.000 €/Jahr"],
        ["Ersparnis gegenüber Gas", "700 bis 1.300 €/Jahr", "1.400 bis 2.000 €/Jahr"],
    ],
    hl_cols=(1, 2),
)}
<p>Die Zahlen zeigen: Auch im teilweise gedämmten Altbau lohnt sich die Wärmepumpe, und mit gezielten
Sanierungsmaßnahmen verdoppelt sich die Ersparnis. Wer den Strom mit einer eigenen
{a('photovoltaik', 'Photovoltaikanlage')} erzeugt, senkt die Heizkosten noch weiter.</p>
<h3>Heizkosten über 20 Jahre: Wärmepumpe, Gas, Öl</h3>
<p>Viele Hausbesitzer vergleichen nur die Anschaffung. Über 20 Jahre betrachtet ergibt sich ein anderes
Bild:</p>
{A.table(
    ["", "Gasheizung", "Ölheizung", "Wärmepumpe im Altbau"],
    [
        ["Anschaffung", "6.000 bis 10.000 €", "8.000 bis 12.000 €", "15.000 bis 25.000 € (vor Förderung)"],
        ["Betriebskosten pro Jahr", "1.800 bis 2.500 €", "2.000 bis 2.800 €", "900 bis 1.900 €"],
        ["Gesamtkosten 20 Jahre", "42.000 bis 60.000 €", "48.000 bis 68.000 €", "33.000 bis 63.000 €"],
    ],
    hl_cols=(3,),
)}
<p>Die Wärmepumpe ist im Altbau langfristig in den meisten Fällen günstiger, besonders wenn die
Förderung abgezogen wird, die in der Tabelle noch nicht berücksichtigt ist. Alle Kostenblöcke im
Detail: {a('/kosten-einer-waermepumpe/', 'Kosten einer Wärmepumpe 2026')}.</p>
<p><small>*Beispielrechnungen mit Richtwerten bei 0,30 €/kWh Strom. Ihre Zahlen hängen von Gebäude,
Dämmung, Heizflächen und Tarif ab.</small></p>
"""),
        ("Photovoltaik und Förderung: So holen Sie im Altbau das Maximum heraus", "foerderung", f"""
<h3>Stromverbrauch mit Photovoltaik senken</h3>
<p>Wer den Strom für die Wärmepumpe selbst erzeugt, senkt die Heizkosten auf ein Minimum. Die
PV-Anlage liefert tagsüber Solarstrom, die Wärmepumpe heizt damit, bereitet Warmwasser und lädt den
Pufferspeicher vor. Mit einem {a('batteriespeicher', 'Batteriespeicher')} steht der Strom auch abends
und nachts bereit. Wie die Kombination geplant wird:
{a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}.</p>
<h3>Förderung: im Bestand oft höher als im Neubau</h3>
<p>Die aktuellen Förderungen machen den Einbau einer Wärmepumpe im Altbau besonders attraktiv, weil der
Wechsel von einer fossilen Heizung ausdrücklich unterstützt wird:</p>
<ul>
  <li><b>Bundesförderung „Raus aus Öl und Gas“:</b> Wer im Altbau eine Gas- oder Ölheizung durch eine
  Wärmepumpe ersetzt, erhält einen Investitionszuschuss von mehreren tausend Euro, abhängig von
  Gebäudetyp und Wärmepumpe. Details: {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive 2026')}
  und {a('/sauber-heizen-fuer-alle-2026/', 'Sauber Heizen für Alle 2026')}.</li>
  <li><b>Landesförderung Kärnten und Steiermark:</b> Beide Bundesländer fördern zusätzlich, auch
  Sanierungsmaßnahmen, die gemeinsam mit der Wärmepumpe umgesetzt werden. Die Kombination aus
  Wärmepumpen- und Sanierungsförderung senkt die Investition erheblich. Überblick:
  {a('/landesfoerderungen-fuer-die-waermepumpe/', 'Landesförderungen für die Wärmepumpe')}.</li>
  <li><b>Steuerlich absetzen:</b> {a('/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/',
  'Öko-Sonderausgabenpauschale 2026')}.</li>
</ul>
<p>Als zertifizierter Fachbetrieb übernimmt EBZ Energie die gesamte Förderabwicklung, korrekt,
vollständig und fristgerecht. Alle Programme:
{a('/waermepumpenfoerderung-in-oesterreich/', 'Wärmepumpenförderung in Österreich')}.</p>
"""),
        ("Fazit: Lohnt sich eine Wärmepumpe im Altbau?", "fazit", f"""
<p>In den meisten Fällen ja, mit den richtigen Begleitmaßnahmen sogar sehr deutlich. Gerade im Altbau,
wo die Heizkosten durch veraltete fossile Systeme besonders hoch sind, ist das Einsparpotenzial am
größten: 700 bis 2.000 Euro pro Jahr gegenüber Gas im Rechenbeispiel. Was es dafür braucht:</p>
<ul>
  <li>eine ehrliche Analyse des Gebäudes durch einen erfahrenen Fachbetrieb</li>
  <li>die richtige Wärmepumpe, präzise auf den Wärmebedarf dimensioniert</li>
  <li>gegebenenfalls gezielte Dämmmaßnahmen</li>
  <li>Heizflächen, die niedrige Vorlauftemperaturen erlauben</li>
  <li>die vollständige Ausschöpfung aller Förderungen</li>
</ul>
<p>Wer diese Punkte umsetzt, muss auch im Altbau keine Abstriche bei Komfort oder Wirtschaftlichkeit
machen. Und wer die Wärmepumpe mit einer PV-Anlage kombiniert, heizt für einen Bruchteil der bisherigen
Kosten.</p>
{A.cta("Kostenlose Vor-Ort-Analyse für Ihren Altbau",
       "Wir prüfen Dämmung, Heizkörper und Wärmebedarf, berechnen Ihre Förderung und erstellen ein "
       "Festpreisangebot.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für die Wärmepumpe im Bestand: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Wärmepumpen, Photovoltaik und Speicher in "
                 "Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. "
                 "Der Heizungstausch im Altbau ist unser Alltag: Wir prüfen Heizkörper und Dämmung vor Ort, "
                 "dimensionieren die Anlage auf den tatsächlichen Wärmebedarf und wickeln Bundes- und "
                 "Landesförderung ab."),
        "grid": [
            ("Vor-Ort-Analyse kostenlos", "Heizkörper, Vorlauftemperatur und Dämmung realistisch bewertet."),
            ("Passende Dimensionierung", "Wärmepumpe auf den Wärmebedarf Ihres Altbaus ausgelegt."),
            ("Förderung komplett abgewickelt", "Kesseltausch, Sanierung und Landesförderung aus einer Hand."),
            ("Montage in 2 bis 4 Tagen", "Zertifizierte Fachkräfte, Inbetriebnahme und Einschulung inklusive."),
        ],
    },

    "faq": [
        ("Ist eine Wärmepumpe im Altbau auch ohne Sanierung geeignet?",
         "Ja, in vielen Fällen. Eine Luft-Wasser-Wärmepumpe läuft auch im unsanierten Altbau, im "
         "Rechenbeispiel mit Jahresarbeitszahl 2,8 bis 3,2. Die Effizienz ist niedriger als im gedämmten "
         "Gebäude, die Betriebskosten liegen aber mit 1.680 bis 1.920 Euro pro Jahr deutlich unter den "
         "2.400 bis 3.000 Euro einer Gasheizung."),
        ("Funktioniert eine Wärmepumpe im Altbau ohne Fußbodenheizung?",
         "Ja. Mit großflächigen oder Niedertemperatur-Heizkörpern bei 40 bis 50 °C Vorlauf funktioniert die "
         "Wärmepumpe im Altbau gut. Bei höheren Vorlauftemperaturen sinkt die Effizienz etwas, sie bleibt "
         "aber wirtschaftlicher als Gas oder Öl."),
        ("Was kostet eine Wärmepumpe im Altbau nach Förderung?",
         "Für ein typisches Altbau-Einfamilienhaus liegen die Kosten inklusive Installation bei 15.000 bis "
         "28.000 Euro vor Förderung. Nach Abzug der Bundes- und Landesförderung bleiben je nach Gebäude und "
         "Bundesland 10.000 bis 20.000 Euro. Wir berechnen Ihre individuelle Förderhöhe kostenlos."),
        ("Wie lange dauert der Einbau einer Wärmepumpe im Altbau?",
         "Die eigentliche Montage dauert in der Regel 2 bis 4 Tage. Der gesamte Prozess von der Beratung bis "
         "zur Inbetriebnahme dauert einige Wochen, weil Förderanträge und Genehmigungen Zeit brauchen."),
        ("Brauche ich für die Wärmepumpe im Altbau eine Baugenehmigung?",
         "Für Luft-Wasser-Wärmepumpen ist in der Regel keine Baugenehmigung erforderlich, in manchen "
         "Gemeinden aber eine Anzeige. EBZ Energie kümmert sich um alle behördlichen Erfordernisse."),
        ("Welche Vorlauftemperatur braucht mein Altbau?",
         "Fußbodenheizung kommt mit 30 bis 35 °C aus, Niedertemperatur-Heizkörper mit 40 bis 50 °C, "
         "klassische Altbau-Heizkörper brauchen oft 60 bis 70 °C. Ein hydraulischer Abgleich und größere "
         "Heizflächen senken die benötigte Temperatur und damit den Stromverbrauch."),
        ("Lohnt sich im Altbau eine Erdwärmepumpe?",
         "Wenn genug Grundstücksfläche für Erdkollektoren oder eine Bohrung vorhanden ist, ja. Die höhere "
         "Investition zahlt sich durch die ganzjährig konstante Quellentemperatur und niedrigere "
         "Betriebskosten aus. In den meisten Altbauten ist aber die Luft-Wasser-Wärmepumpe die erste Wahl."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team tauscht in Kärnten und "
                    "der Steiermark regelmäßig Öl- und Gasheizungen in Bestandsgebäuden gegen Wärmepumpen und "
                    "übernimmt die Förderabwicklung. Alle Rechenbeispiele sind Richtwerte aus der "
                    "Projektpraxis. Keine Rechts- oder Steuerberatung, maßgeblich sind die offiziellen "
                    "Förderbedingungen."),
    "related": [
        ("waermepumpe", "Wärmepumpen-Installateur in Kärnten und Steiermark"),
        ("/kosten-einer-waermepumpe/", "Kosten einer Wärmepumpe 2026"),
        ("/sanierungsoffensive-2026/", "Sanierungsoffensive 2026: Kesseltausch fördern lassen"),
        ("/heizen-mit-waermepumpe/", "Heizen mit Wärmepumpe: Grundlagen"),
    ],
    "cta": {
        "h3": "Altbau auf Wärmepumpe umstellen?",
        "text": "Kostenlose Vor-Ort-Analyse, Festpreisangebot und Förderabwicklung aus einer Hand.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihr Altbau, effizient beheizt",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
