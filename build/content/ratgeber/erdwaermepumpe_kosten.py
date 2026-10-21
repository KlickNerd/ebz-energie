"""Ratgeber: Erdwärmepumpe Kosten 2026 (Sole-Wasser, Tiefenbohrung, Flächenkollektor).

Migriert vom WordPress-Artikel ebz-photovoltaik.at/erdwaermepumpe-kosten/
(veröffentlicht 2026-09-20, geändert 2026-09-30). Struktur, Preise und Vergleichsrechnung aus der Quelle.
Abgrenzung: nur Sole/Erdwärme (Bohrung vs. Kollektor, Bohrkosten je Meter, Genehmigung, Betrieb,
Amortisation gegenüber Luft). Gesamtvergleich: /kosten-einer-waermepumpe/, Luft: /luftwaermepumpe-preise/.
Bereinigt: Quelle verlinkte /luftwaermepumpe-kosten/ (existiert nicht, Slug ist /luftwaermepumpe-preise/).
Förderung nach build/seo/_fakten_2026-10.md (Bund nicht verfügbar, Kärnten 3.000 €, Steiermark keine Anträge).
Bohrmeter-Tabelle und Amortisationsjahre sind aus den Quellwerten gerechnet (50 bis 100 €/m, JAZ 3,5/4,5, 28 ct).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "erdwaermepumpe-kosten",
    "path": "/erdwaermepumpe-kosten/",
    "title": "Erdwärmepumpe Kosten 2026: Bohrung und Betrieb | EBZ Energie",
    "description": ("Erdwärmepumpe 2026: 22.000 bis 40.000 € gesamt, Tiefenbohrung 50 bis 100 € je Meter, JAZ 4 "
                    "bis 5. Bohrung oder Kollektor, Genehmigung und Vergleich mit Luft."),
    "eyebrow": "Wärmepumpe · Erdwärme",
    "crumb_label": "Erdwärmepumpe Kosten",
    "h1": "Erdwärmepumpe Kosten 2026: 22.000 bis 40.000 Euro mit Bohrung, und wann sich das rechnet",
    "lead": ("Eine Sole-Wasser-Wärmepumpe kostet im Einfamilienhaus inklusive Tiefenbohrung oder Flächenkollektor "
             "meist 22.000 bis 40.000 Euro, die Bohrung allein 50 bis 100 Euro je Meter. Dieser Ratgeber zeigt, "
             "wie sich der Preis zusammensetzt, welche Genehmigung Sie brauchen und wie lange es dauert, bis sich "
             "die Mehrkosten gegenüber einer Luftwärmepumpe zurückverdienen."),
    "chips": [
        "Gesamt: <b>22.000 bis 40.000 €</b>*",
        "Bohrung: <b>50 bis 100 € je Meter</b>*",
        "JAZ: <b>4 bis 5</b>",
        "Plus: <b>passive Kühlung</b>",
    ],
    "date_published": "2026-09-20",
    "date_modified": "2026-10-21",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit großem Rasengrundstück in den Bergen, Platz für Erdsonde oder Flächenkollektor",

    "tldr": [
        "Eine Erdwärmepumpe kostet im Einfamilienhaus inklusive Bohrung und Montage meist 22.000 bis 40.000 "
        "Euro. Die Tiefenbohrung allein kostet 50 bis 100 Euro je Meter, bei 120 bis 160 Metern rund 6.000 bis "
        "16.000 Euro.",
        "Faustregel: Ein Meter Erdsonde liefert 40 bis 60 Watt Heizleistung. Ein Haus mit 8 kW Heizlast braucht "
        "damit etwa 130 bis 200 Bohrmeter.",
        "Mit Jahresarbeitszahlen von 4 bis 5 spart sie gegenüber einer Luftwärmepumpe im Einfamilienhaus grob "
        "150 bis 300 Euro Strom pro Jahr. Bei rund 12.000 Euro Mehrkosten rechnet sich das allein über den "
        "Strom erst nach Jahrzehnten.",
        "Tiefenbohrungen fallen unter das Wasserrecht: Anzeige mit drei Monaten Entscheidungsfrist oder "
        "Bewilligung durch die Bezirkshauptmannschaft.",
        "Förderung Stand Oktober 2026: Die Bundesförderung 2026 samt 5.000 Euro Bohrbonus ist ausgeschöpft. "
        "Kärnten zahlt 3.000 Euro Pauschale, die Steiermark nimmt für neue Wärmepumpen derzeit keine Anträge an.",
    ],
    "kpis": [
        ("22.000 bis 40.000 €", "gesamt im Einfamilienhaus*"),
        ("50 bis 100 €", "je Bohrmeter*"),
        ("4 bis 5", "Jahresarbeitszahl"),
        ("3 Monate", "Entscheidungsfrist im Anzeigeverfahren"),
    ],

    "sections": [
        ("Was kostet eine Erdwärmepumpe 2026?", "kosten", f"""
<p><b>Eine Erdwärmepumpe (Sole-Wasser-Wärmepumpe) kostet in Österreich 2026 für ein Einfamilienhaus
inklusive Tiefenbohrung, Gerät und Montage meist 22.000 bis 40.000 Euro vor Förderung*; die Bohrung kostet
50 bis 100 Euro je Meter.</b> Sie nutzt die Wärme des Erdreichs, das im Jänner fast dieselbe Temperatur hat
wie im Juli, und arbeitet deshalb besonders effizient. Der Preis dafür ist die Erschließung der
Wärmequelle: Tiefenbohrung oder Flächenkollektor machen sie deutlich teurer als eine
{a('/luftwaermepumpe-preise/', 'Luftwärmepumpe')}. Alle Wärmepumpenarten im Gesamtvergleich zeigt der
Ratgeber {a('/kosten-einer-waermepumpe/', 'Kosten einer Wärmepumpe')}.</p>
{A.table(
    ["Position", "Richtwert*", "Bemerkung"],
    [
        ["Wärmepumpe (Sole-Wasser)", "12.000 bis 22.000 €", "Gerät inkl. Regelung, oft mit integriertem Warmwasserspeicher"],
        ["Tiefenbohrung", "50 bis 100 € je Meter", "bei 120 bis 160 Metern rund 6.000 bis 16.000 €"],
        ["Flächenkollektor (Alternative)", "deutlich günstiger bei ohnehin geplanten Erdarbeiten", "große unversiegelte Gartenfläche nötig"],
        ["Montage, Hydraulik, Elektrik", "4.000 bis 8.000 €", "Anbindung, Pufferspeicher, Solekreis"],
        ["Behörde und Gutachten", "einige hundert Euro", "Anzeige oder wasserrechtliche Bewilligung"],
        ["<b>Gesamt</b>", "<b>22.000 bis 40.000 €</b>", "Neubau und Sanierung ähnlich, die Bohrung entscheidet"],
    ],
    hl_cols=(1,),
)}
<p>Die größte Unbekannte ist die Bohrung. Geologie, Zufahrt für das Bohrgerät und die Anzahl der Sonden
bestimmen, ob Sie eher bei 25.000 oder bei 40.000 Euro landen.</p>
<p><small>*Richtwerte 2026 inklusive USt, vor Förderung. Der tatsächliche Preis hängt von Heizlast,
Untergrund und Aufwand vor Ort ab.</small></p>
"""),
        ("Bohrkosten pro Meter: So rechnen Sie die Tiefenbohrung", "bohrung", f"""
<p>Wie tief gebohrt wird, hängt von der Heizlast und vom Untergrund ab. Als Faustregel liefert ein Meter
Erdsonde 40 bis 60 Watt Heizleistung. Ein Haus mit 8 kW Heizlast braucht damit etwa 130 bis 200
Bohrmeter, meist aufgeteilt auf zwei Sonden, die jeweils 80 bis 150 Meter tief reichen. Die genaue
Auslegung übernimmt das Bohrunternehmen nach geologischer Prüfung.</p>
{A.table(
    ["Bohrmeter gesamt", "bei 50 € je Meter*", "bei 100 € je Meter*"],
    [
        ["100 m", "5.000 €", "10.000 €"],
        ["130 m", "6.500 €", "13.000 €"],
        ["160 m", "8.000 €", "16.000 €"],
        ["200 m", "10.000 €", "20.000 €"],
    ],
    hl_cols=(1, 2),
)}
<p>Klären Sie im Angebot, was der Meterpreis enthält: Sonde und Verpressung, Baustelleneinrichtung,
Anfahrt des Bohrgeräts, Entsorgung des Bohrguts und die Anbindung bis ins Haus. Die Bohrung selbst dauert meist ein bis drei Tage.</p>
<p><small>*Rechenbeispiel aus der Spanne von 50 bis 100 Euro je Meter. Den verbindlichen Preis nennt das
Bohrunternehmen nach Prüfung des Untergrunds.</small></p>
"""),
        ("Tiefenbohrung, Flächenkollektor oder Grundwasser?", "waermequelle", f"""
{A.table(
    ["Wärmequelle", "Platzbedarf", "Vorteil", "Nachteil"],
    [
        ["Erdsonde (Tiefenbohrung)", "gering, wenige Quadratmeter", "sehr konstante Quellentemperatur, passive Kühlung möglich", "Bohrkosten, Genehmigung nach Wasserrecht"],
        ["Flächenkollektor", "meist ein Mehrfaches der beheizten Wohnfläche", "ohne Bohrgerät, im Neubau oft günstiger", "Fläche darf nicht bebaut oder versiegelt werden"],
        ["Grundwasser (Wasser-Wasser)", "zwei Brunnen", "höchste Effizienz", "nur bei geeignetem Grundwasser, Bewilligung nötig"],
    ],
)}
<h3>Erdsonde mit Tiefenbohrung</h3>
<p>Die häufigste Lösung. Eine oder mehrere Sonden reichen meist 80 bis 150 Meter tief. Vorteil: wenig
Platzbedarf, sehr konstante Quellentemperatur und die Möglichkeit zur passiven Kühlung im Sommer.</p>
<h3>Flächenkollektor</h3>
<p>Rohrschlangen werden in 1,2 bis 1,5 Metern Tiefe flächig im Garten verlegt. Das geht ohne Bohrgerät und
ist beim Neubau oft günstiger, weil ohnehin gegraben wird. Der Nachteil: Die Fläche ist meist ein
Mehrfaches der beheizten Wohnfläche und darf danach nicht bebaut, versiegelt oder mit tief wurzelnden
Pflanzen bepflanzt werden.</p>
<h3>Grundwasser (Wasser-Wasser-Wärmepumpe)</h3>
<p>Wo ausreichend Grundwasser in geringer Tiefe vorhanden ist, erreicht die Wasser-Wasser-Wärmepumpe die
höchste Effizienz. Voraussetzung sind ein Förder- und ein Schluckbrunnen, eine gute Wasserqualität und eine
wasserrechtliche Bewilligung. In vielen Lagen Kärntens und der Steiermark ist das eher die Ausnahme. Wie
die drei Wärmequellen technisch arbeiten, erklärt der Ratgeber
{a('/funktionsweise-einer-waermepumpe/', 'Funktionsweise einer Wärmepumpe')}.</p>
"""),
        ("Genehmigung: Wasserrecht nicht unterschätzen", "genehmigung", f"""
<p>Erdwärmesonden und Grundwassernutzung unterliegen dem Wasserrechtsgesetz. Zuständig ist in der Regel die
Bezirkshauptmannschaft beziehungsweise der Magistrat. Je nach Standort genügt eine Anzeige nach § 114 WRG
mit einer <b>Entscheidungsfrist von drei Monaten</b>, oder es ist ein Bewilligungsverfahren nötig. In
Schutz- und Schongebieten kann eine Bohrung auch untersagt werden. Bewilligungen werden häufig auf 25 Jahre
befristet.</p>
{A.box("Starten Sie mit der Klärung beim Bohrunternehmen und bei der Behörde, bevor Sie Geräte bestellen. "
       "Bei Erdwärme bestimmt die Genehmigung den Zeitplan, nicht die Montage.", label="Planungstipp:")}
"""),
        ("Erdwärme gegen Luftwärme: Betriebskosten und Amortisation", "vergleich", f"""
<p>Die Erdwärmepumpe erreicht Jahresarbeitszahlen von 4 bis 5, eine gute Luftwärmepumpe 3,5 bis 4. Im
Beispiel eines Einfamilienhauses mit 12.000 Kilowattstunden Wärmebedarf:</p>
{A.table(
    ["Kennzahl*", "Luftwärmepumpe (JAZ 3,5)", "Erdwärmepumpe (JAZ 4,5)"],
    [
        ["Anschaffung (Mitte der Spanne)", "rund 19.000 €", "rund 31.000 €"],
        ["Strombedarf pro Jahr", "rund 3.430 kWh", "rund 2.670 kWh"],
        ["Stromkosten pro Jahr bei 28 ct/kWh", "rund 960 €", "rund 750 €"],
        ["Differenz", "", "rund 12.000 € mehr, gut 200 € weniger Strom pro Jahr"],
    ],
    hl_cols=(2,),
)}
<p>Die Ersparnis im Betrieb ist real, aber begrenzt. Rein rechnerisch braucht es bei rund 12.000 Euro
Mehrkosten und gut 200 Euro Ersparnis pro Jahr über 50 Jahre, bis sich die Erdwärmepumpe allein über die
Stromkosten bezahlt macht. Bei einem Haus mit 20.000 Kilowattstunden Wärmebedarf liegt die Ersparnis bei
rund 350 Euro pro Jahr*, die Rechnung bleibt trotzdem lang. Wirtschaftlich interessant wird Erdwärme vor
allem in diesen Fällen:</p>
<ul>
  <li><b>Hohe Heizlast</b>, etwa bei großen oder wenig gedämmten Gebäuden, weil die Ersparnis mit dem
  Verbrauch wächst.</li>
  <li><b>Passive Kühlung</b> im Sommer ist gewünscht: Das kühle Erdreich nimmt Wärme aus Fußboden- oder
  Deckenheizung auf, ohne dass der Verdichter läuft.</li>
  <li><b>Schall oder Platz</b> sprechen gegen ein Außengerät, etwa bei dichter Bebauung.</li>
  <li><b>Ein Bohrbonus</b> in der Förderung verringert die Mehrkosten deutlich; 2026 waren es 5.000 Euro
  vom Bund.</li>
</ul>
<p>Für die meisten Einfamilienhäuser ist die Luftwärmepumpe die wirtschaftlichere Wahl. Wir rechnen beide
Varianten für Ihr Haus durch und empfehlen ehrlich, was sich lohnt.</p>
<p><small>*Richtwerte aus der Mitte der Preisspannen, Strompreis 28 Cent je Kilowattstunde, ohne Förderung
und ohne Strompreissteigerung. Mit eigener PV-Anlage sinken die Stromkosten beider Varianten.</small></p>
"""),
        ("Förderung für Erdwärmepumpen: Stand Oktober 2026", "foerderung", f"""
<ul>
  <li><b>Bund:</b> In der Sanierungsoffensive 2026 gab es bis zu 7.500 Euro für die Wärmepumpe und
  zusätzlich 5.000 Euro Bohrbonus für Erdsonden. Die Mittel sind laut Ministerium seit Juli 2026 vergeben,
  neue Registrierungen sind derzeit nicht möglich. Bereits registrierte Anträge werden normal abgewickelt.
  Details im Ratgeber {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive 2026')}.</li>
  <li><b>Ausblick:</b> Für 2027 hat das Ministerium einen Förderrahmen von 360 Millionen Euro vorgesehen,
  davon 179 Millionen Euro für den Kesseltausch (BMLUK, Juli 2026). Ob es wieder einen Bohrbonus gibt und
  ab wann registriert werden kann, prüfen wir vor jedem Angebot.</li>
  <li><b>Kärnten:</b> 3.000 Euro Pauschale für die Wärmepumpe, plus 1.500 Euro bei Errichtung einer
  Solaranlage und 200 Euro für den hydraulischen Abgleich. Ob das Budget reicht, klären wir vor dem
  Angebot.</li>
  <li><b>Steiermark:</b> Für neue Wärmepumpen nimmt das Land derzeit keine Förderanträge an. Gefördert
  wird nur der Tausch mindestens 15 Jahre alter Wärmepumpen oder Biomassekessel, mit höchstens 1.500 Euro.</li>
</ul>
<p>Alle Länder im Vergleich: {a('/landesfoerderungen-fuer-die-waermepumpe/', 'Landesförderungen für die Wärmepumpe')}.
Weil Genehmigung und Bohrplanung ohnehin einige Monate brauchen, ist jetzt ein guter Zeitpunkt, ein
Erdwärme-Projekt vorzubereiten. Aufträge, die eine spätere Förderung gefährden könnten, sollten erst
vergeben werden, wenn die Förderbedingungen feststehen.</p>
{A.cta("Luft oder Erde? Wir rechnen beides für Sie durch",
       "EBZ Energie prüft Heizlast, Grundstück und Förderung und empfiehlt die Lösung, die sich für Ihr Haus "
       "wirklich rechnet.",
       secondary=("waermepumpe", "Zum Wärmepumpen-Installateur"))}
"""),
        ("Ablauf eines Erdwärme-Projekts", "ablauf", f"""
{A.steps([
    ("Beratung und Heizlast",
     "Wir berechnen die Heizlast und prüfen, ob Luft oder Erde für Ihr Haus sinnvoller ist."),
    ("Geologie und Genehmigung",
     "Das Bohrunternehmen prüft den Untergrund, die Anzeige oder Bewilligung wird bei der Behörde "
     "eingereicht. Im Anzeigeverfahren gilt eine Frist von drei Monaten."),
    ("Förderung",
     "Wir prüfen Landes- und Bundesförderung und registrieren, sobald das möglich ist und bevor Kosten "
     "entstehen."),
    ("Bohrung",
     "Die Sonden werden gebohrt und verpresst, meist an ein bis drei Tagen."),
    ("Einbau und Inbetriebnahme",
     "Wärmepumpe, Solekreis und Hydraulik werden angeschlossen, auf Wunsch mit PV-Anlage und "
     "Energiemanagement."),
])}
"""),
        ("Fazit: Effizienter Komfort mit höherer Anfangsinvestition", "fazit", f"""
<p>Die Erdwärmepumpe ist die effizienteste und leiseste Wärmepumpe und kann im Sommer fast ohne Strom
kühlen. Mit 22.000 bis 40.000 Euro kostet sie aber deutlich mehr als eine Luftwärmepumpe, und die Ersparnis
im Betrieb gleicht das im Einfamilienhaus nur langsam aus. Wer Komfort, Kühlung und Unabhängigkeit vom
Außengerät schätzt oder eine hohe Heizlast hat, ist mit Erdwärme gut beraten. Mit eigenem Sonnenstrom
sinken die Betriebskosten weiter, siehe {a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}.</p>
{A.cta("Erdwärme-Projekt jetzt vorbereiten",
       "Genehmigung, Bohrung, Wärmepumpe und Förderung koordinieren wir mit einem Ansprechpartner.",
       primary=("kontakt", "Kostenlose Erstberatung"),
       secondary=("/luftwaermepumpe-preise/", "Luftwärmepumpe im Vergleich"))}
"""),
    ],

    "partner": {
        "h2": "Erdwärme und Luftwärme aus einer Hand",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie plant Wärmepumpen in Kärnten und der Steiermark und empfiehlt die Lösung, die zu "
                 "Ihrem Haus passt, nicht die teuerste. Bohrung, Genehmigung, Einbau und Förderung koordinieren "
                 "wir mit einem festen Ansprechpartner von der Planung bis zur Übergabe."),
        "grid": [
            ("Ehrlicher Vergleich", "Luft und Erde durchgerechnet für Ihr Haus."),
            ("Koordination", "Bohrunternehmen, Behörde und Montage abgestimmt."),
            ("Mit Photovoltaik", "Wärmepumpe und Sonnenstrom als System."),
            ("Förderabwicklung", "Land und Bund zum richtigen Zeitpunkt."),
        ],
    },

    "faq": [
        ("Was kostet eine Erdwärmepumpe mit Tiefenbohrung?",
         "Für ein Einfamilienhaus liegen die Gesamtkosten inklusive Bohrung, Wärmepumpe und Montage meist bei "
         "22.000 bis 40.000 Euro vor Förderung. Allein die Bohrung kostet in Österreich typischerweise 50 bis "
         "100 Euro je Bohrmeter, bei 120 bis 160 Metern also rund 6.000 bis 16.000 Euro."),
        ("Wie tief muss für eine Erdwärmepumpe gebohrt werden?",
         "Das hängt von Heizlast und Untergrund ab. Als Faustregel liefert ein Meter Erdsonde rund 40 bis 60 "
         "Watt Heizleistung. Ein Haus mit 8 kW Heizlast braucht damit oft 130 bis 200 Bohrmeter, meist "
         "aufgeteilt auf zwei Sonden."),
        ("Braucht man für eine Erdwärmepumpe eine Genehmigung?",
         "Ja. Tiefenbohrungen und Grundwassernutzung fallen unter das Wasserrecht. Je nach Standort reicht eine "
         "Anzeige oder es ist eine wasserrechtliche Bewilligung der Bezirkshauptmannschaft nötig. Im "
         "Anzeigeverfahren gilt eine Entscheidungsfrist von drei Monaten."),
        ("Ist ein Flächenkollektor günstiger als eine Tiefenbohrung?",
         "Oft ja, wenn genug Gartenfläche vorhanden ist und ohnehin gegraben wird, etwa beim Neubau. Der "
         "Kollektor liegt in 1,2 bis 1,5 Metern Tiefe und braucht meist ein Mehrfaches der beheizten "
         "Wohnfläche. Die Fläche darüber darf nicht bebaut, versiegelt oder mit tief wurzelnden Pflanzen "
         "bepflanzt werden."),
        ("Lohnt sich eine Erdwärmepumpe gegenüber einer Luftwärmepumpe?",
         "Rein rechnerisch spart die Erdwärmepumpe im Einfamilienhaus meist 150 bis 300 Euro Strom pro Jahr, "
         "kostet in der Anschaffung aber oft 10.000 Euro und mehr zusätzlich. Sie lohnt sich vor allem bei "
         "hoher Heizlast, für passive Kühlung, wenn ein Außengerät stören würde oder wenn eine Bohrförderung "
         "verfügbar ist."),
        ("Gibt es eine Förderung für Erdwärmepumpen?",
         "In der Sanierungsoffensive 2026 gab es zusätzlich zur Wärmepumpenförderung von bis zu 7.500 Euro einen "
         "Bohrbonus von 5.000 Euro. Diese Mittel sind vergeben, neue Registrierungen sind derzeit nicht "
         "möglich. Kärnten zahlt 3.000 Euro Pauschale für die Wärmepumpe, die Steiermark nimmt für neue "
         "Wärmepumpen derzeit keine Anträge an."),
        ("Kann eine Erdwärmepumpe im Sommer kühlen?",
         "Ja. Mit einer Erdsonde ist passive Kühlung möglich: Das kühle Erdreich nimmt Wärme aus der Fußboden- "
         "oder Deckenheizung auf, ohne dass der Verdichter läuft. Der Stromverbrauch dafür ist sehr gering, "
         "das ist ein echter Komfortvorteil gegenüber der Luftwärmepumpe."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Mit zertifizierten Fachkräften plant "
                    "und installiert EBZ Energie Wärmepumpen, Photovoltaik und Speicher in Kärnten und der "
                    "Steiermark und koordiniert bei Erdwärme Bohrunternehmen, Behörde und Förderung. Kosten und "
                    "Förderstand werden anhand realer Projekte und der offiziellen Förderstellen aktualisiert. "
                    "Keine Rechts- oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("BMLUK: Sanierungsoffensive 2026, alle Fördermittel abgeholt (13. Juli 2026)",
         "https://www.bmluk.gv.at/service/presse/klima-umwelt/2026/sanierungsoffensive-2026-alle-foerdermittel-abgeholt.html"),
        ("Sanierungsoffensive: Budget-Information",
         "https://www.sanierungsoffensive.gv.at/budget-information"),
        ("Land Steiermark: Förderung für Heizungen (Wohnbau)",
         "https://www.wohnbau.steiermark.at/cms/ziel/164947118/DE/"),
        ("pieno.at: Erdwärmepumpe in Österreich, Tiefenbohrung und Bewilligung",
         "https://pieno.at/erdwaermepumpe-oesterreich-tiefenbohrung-flaechenkollektor-bewilligung/"),
    ],
    "related": [
        ("/luftwaermepumpe-preise/", "Luftwärmepumpe: Preise und Betriebskosten"),
        ("/kosten-einer-waermepumpe/", "Kosten einer Wärmepumpe: alle Arten im Vergleich"),
        ("/funktionsweise-einer-waermepumpe/", "Funktionsweise einer Wärmepumpe"),
        ("waermepumpe", "Wärmepumpen-Installateur in Kärnten und Steiermark"),
    ],
    "cta": {
        "h3": "Luft oder Erde für Ihr Haus?",
        "text": "Wir rechnen beide Varianten mit Ihrer Heizlast durch und koordinieren Bohrung, Genehmigung und Förderung.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre Wärmepumpe, ehrlich verglichen",
    "final_text": ("Kostenlose Erstberatung, transparente Zahlen und ein Ansprechpartner aus Villach, der Planung, "
                   "Montage und Förderabwicklung aus einer Hand koordiniert."),
}
