"""Ratgeber: Funktionsweise einer Wärmepumpe (Kreislauf, COP, JAZ, Arten, PV).

Migriert von ebz-photovoltaik.at/funktionsweise-einer-waermepumpe/ (Stand April 2026).
Bereinigt: Montage-Formulierung auf "zertifizierte Fachkräfte" umgestellt, Einsatzgebiet auf Kärnten und Steiermark
präzisiert, Minuszeichen als Gedankenstrich ersetzt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "funktionsweise-einer-waermepumpe",
    "path": "/funktionsweise-einer-waermepumpe/",
    "title": "Funktionsweise Wärmepumpe: Kreislauf, COP, JAZ | EBZ",
    "description": ("Funktionsweise einer Wärmepumpe: Kältemittelkreislauf in 4 Schritten, 75 % "
                    "Umgebungswärme plus 25 % Strom, COP und JAZ, JAZ 3,0 bis 5,5 je nach Wärmequelle."),
    "eyebrow": "Wärmepumpe · Technik",
    "crumb_label": "Funktionsweise einer Wärmepumpe",
    "h1": "Die Funktionsweise einer Wärmepumpe einfach erklärt: 4 Schritte, 75 Prozent Umweltwärme",
    "lead": ("Eine Wärmepumpe holt Wärme aus Luft, Erdreich oder Grundwasser und hebt sie mit wenig Strom "
             "auf Heiztemperatur: Aus 1 kWh Strom werden 4 bis 5 kWh Wärme. Dieser Ratgeber erklärt den "
             "Kältemittelkreislauf, die Kennzahlen COP und Jahresarbeitszahl, die drei Wärmepumpenarten und "
             "die Bedingungen, unter denen die Anlage am effizientesten läuft."),
    "chips": [
        "Umweltwärme: <b>75 %</b>",
        "Strom: <b>25 %</b>",
        "JAZ: <b>3,0 bis 5,5</b> je nach Quelle",
        "Betrieb bis <b>-20 °C</b> und darunter",
    ],
    "date_published": "2026-03-30",
    "date_modified": "2026-09-24",
    "hero_img": "waermepumpe",
    "hero_alt": "Außeneinheit einer Luft-Wasser-Wärmepumpe: Wärmequelle Außenluft für den Kältemittelkreislauf",

    "tldr": [
        "Eine Wärmepumpe arbeitet wie ein Kühlschrank in umgekehrter Richtung: Sie entzieht der Umgebung "
        "Wärme und gibt sie an das Heizsystem ab. Es gibt keine Verbrennung, keinen CO₂-Ausstoß im Betrieb "
        "und keine fossilen Brennstoffe.",
        "Der Kältemittelkreislauf hat vier Schritte: Verdampfen, Verdichten, Verflüssigen, Entspannen. "
        "Nur der Verdichter braucht Strom. Das Kältemittel R290 (Propan) siedet schon bei rund -42 °C.",
        "3 bis 4 kWh kostenlose Umgebungswärme plus 1 kWh Strom ergeben 4 bis 5 kWh Heizwärme. Der COP "
        "beschreibt einen Betriebspunkt, die Jahresarbeitszahl (JAZ) das ganze Heizjahr.",
        "Typische JAZ: Luft-Wasser 3,0 bis 3,5, Sole-Wasser 4,0 bis 4,5, Wasser-Wasser 4,5 bis 5,5. Ein "
        "Gas-Brennwertkessel liegt bei 0,85 bis 0,95, eine Ölheizung bei 0,80 bis 0,90.",
        "Am effizientesten läuft die Wärmepumpe bei niedriger Vorlauftemperatur (30 bis 40 °C, maximal "
        "55 °C), guter Dämmung, richtiger Dimensionierung und mit eigenem Solarstrom.",
    ],
    "kpis": [
        ("4 Schritte", "im Kältemittelkreislauf"),
        ("4 bis 5 kWh", "Wärme aus 1 kWh Strom"),
        ("-42 °C", "Siedepunkt des Kältemittels R290"),
        ("55 °C", "maximale Vorlauftemperatur für Heizkörper"),
    ],

    "sections": [
        ("Das Grundprinzip: wie ein Kühlschrank, nur umgekehrt", "grundprinzip", f"""
<p>Eine Wärmepumpe nutzt dasselbe physikalische Prinzip wie ein Kühlschrank, nur in die andere Richtung.
Der Kühlschrank entzieht seinem Inneren Wärme und gibt sie nach außen ab. Die Wärmepumpe entzieht der
Umgebung Wärme und gibt sie an Ihr Heizsystem ab.</p>
<p>Das klingt zunächst paradox: Wie soll aus Außenluft mit -5 °C Heizwärme von 35 °C werden? Der
Schlüssel ist der Kältemittelkreislauf. Ein Kältemittel wie R290 (Propan) hat einen extrem niedrigen
Siedepunkt und verdampft schon bei sehr niedrigen Temperaturen. Durch Verdampfung, Kompression und
Kondensation wird die Umgebungswärme auf ein höheres Temperaturniveau „gepumpt“.</p>
<p>Das Ergebnis: Aus einer Kilowattstunde Strom und rund drei bis fünf Kilowattstunden kostenloser
Umgebungswärme erzeugt die Wärmepumpe vier bis sechs Kilowattstunden Heizwärme. Sie vervielfacht die
eingesetzte Energie, ohne Verbrennung, ohne CO₂-Ausstoß im Betrieb und ohne fossile Brennstoffe.</p>
"""),
        ("Der Kältemittelkreislauf in 4 Schritten", "kreislauf", f"""
<p>Herzstück jeder Wärmepumpe ist ein geschlossener Kreislauf, in dem ein Kältemittel zirkuliert. In
vier aufeinanderfolgenden Schritten wird Umgebungswärme aufgenommen und auf Heiztemperatur gebracht:</p>
{A.steps([
    ("Verdampfen",
     "Das flüssige Kältemittel fließt durch den Verdampfer, einen Wärmetauscher mit Kontakt zur "
     "Wärmequelle (Luft, Erde oder Grundwasser). Weil sein Siedepunkt extrem niedrig liegt (bei R290 rund "
     "-42 °C), reicht selbst Außenluft weit unter null Grad, um es zum Verdampfen zu bringen. Es wird "
     "gasförmig und speichert dabei die Umgebungswärme."),
    ("Verdichten",
     "Der Kompressor verdichtet das gasförmige Kältemittel unter hohem Druck. Dabei steigen Druck und "
     "Temperatur stark an, das Kältemittel erreicht 50 bis 70 °C. Dieser Schritt ist der einzige im "
     "Kreislauf, der elektrische Energie braucht. Genau hier liegt der Schlüssel zur Effizienz: Mit "
     "relativ wenig Strom wird viel gespeicherte Umgebungswärme auf Heiztemperatur gebracht."),
    ("Verflüssigen",
     "Das heiße Gas strömt durch den Kondensator, einen zweiten Wärmetauscher, der mit dem Heizungswasser "
     "verbunden ist. Hier gibt das Kältemittel seine Wärme an Heizkörper, Fußbodenheizung oder "
     "Warmwasserspeicher ab, kühlt ab und wird wieder flüssig."),
    ("Entspannen",
     "Das flüssige, noch unter Druck stehende Kältemittel passiert das Expansionsventil. Der Druck fällt "
     "schlagartig, das Kältemittel kühlt stark ab und ist wieder bereit, im Verdampfer Umgebungswärme "
     "aufzunehmen. Der Kreislauf beginnt von vorn, solange Heizwärme benötigt wird."),
])}
"""),
        ("75 Prozent Umgebungswärme, 25 Prozent Strom: COP und Jahresarbeitszahl", "cop-jaz", f"""
<p>Das Verhältnis von eingesetztem Strom zu gewonnener Heizwärme macht die Wärmepumpe so effizient. Im
Durchschnitt stammen rund drei Viertel der Heizenergie aus der Umgebung und nur ein Viertel aus dem
Stromnetz.</p>
{A.box_dark("Die Rechnung im Überblick",
    "3 bis 4 kWh Umgebungswärme (kostenlos) + 1 kWh Strom = 4 bis 5 kWh Heizwärme.")}
<p>Dieses Verhältnis heißt <b>COP-Wert</b> (Coefficient of Performance). Der COP gibt an, wie viel
Heizwärme die Wärmepumpe in einem bestimmten Betriebspunkt aus einer Kilowattstunde Strom erzeugt. COP 4
bedeutet: Aus 1 kWh Strom entstehen 4 kWh Wärme.</p>
<p>Für die Praxis wichtiger ist die <b>Jahresarbeitszahl (JAZ)</b>. Sie misst die durchschnittliche
Effizienz über ein gesamtes Heizjahr, inklusive kalter Wintertage, Warmwasserbereitung und
Abtauzyklen. Die JAZ ist deshalb realistischer als der COP und liegt typischerweise etwas niedriger.
Je höher die JAZ, desto günstiger arbeitet Ihre Wärmepumpe: Bei JAZ 4 erhalten Sie für jede
Kilowattstunde Strom vier Kilowattstunden Heizwärme.</p>
"""),
        ("Effizienz im Vergleich: Wärmepumpe gegen fossile Heizung", "effizienz-vergleich", f"""
<p>Ein moderner Gas-Brennwertkessel erzeugt aus einer Einheit Energie maximal 0,9 Einheiten Wärme. Eine
Wärmepumpe schafft das Drei- bis Fünffache. Typische Jahresarbeitszahlen im Vergleich:</p>
{A.table(
    ["Heizsystem", "Typische Jahresarbeitszahl"],
    [
        ["Luft-Wasser-Wärmepumpe", "3,0 bis 3,5"],
        ["Sole-Wasser-Wärmepumpe (Erdwärme)", "4,0 bis 4,5"],
        ["Wasser-Wasser-Wärmepumpe (Grundwasser)", "4,5 bis 5,5"],
        ["Gas-Brennwertkessel", "0,85 bis 0,95"],
        ["Ölheizung", "0,80 bis 0,90"],
    ],
    hl_cols=(1,),
)}
<p>Der Unterschied ist drastisch: Eine Sole-Wasser-Wärmepumpe mit JAZ 4,5 erzeugt aus derselben Menge
Energie fast fünfmal so viel Heizwärme wie ein Gaskessel. Das bedeutet deutlich niedrigere Heizkosten,
deutlich weniger CO₂ und eine schnellere Amortisation. Was das in Euro heißt, rechnet der Ratgeber
{a('/kosten-einer-waermepumpe/', 'Kosten einer Wärmepumpe 2026')} vor.</p>
"""),
        ("Die drei Wärmepumpenarten im Überblick", "arten", f"""
<p>Je nachdem, welche Umgebungswärme genutzt wird, unterscheidet man drei Haupttypen. Jeder hat seine
Stärken und eignet sich für unterschiedliche Gebäude, Grundstücke und Budgets.</p>
<h3>Luft-Wasser-Wärmepumpe</h3>
<p>Sie nutzt die Außenluft als Wärmequelle und ist am einfachsten zu installieren: keine Bohrung, keine
Erdarbeiten, nur eine Außeneinheit im Garten oder an der Hauswand. Moderne Geräte arbeiten zuverlässig
bis -20 °C und darunter. Die Effizienz ist bei milden Temperaturen am höchsten und sinkt bei extremer
Kälte leicht ab, was sich in der JAZ von typischerweise 3,0 bis 3,5 zeigt. Sie ist die meistverkaufte
Variante in Österreich und bietet das beste Verhältnis aus Investition, Installationsaufwand und
Leistung, besonders für Bestandsgebäude ohne Möglichkeit für Erdarbeiten.</p>
<h3>Sole-Wasser-Wärmepumpe (Erdwärme)</h3>
<p>Sie nutzt die konstante Temperatur des Erdreichs: In wenigen Metern Tiefe herrschen ganzjährig
etwa 8 bis 12 °C, unabhängig von der Außentemperatur. Die Wärme wird über Erdsonden (Tiefenbohrung)
oder Flächenkollektoren erschlossen. Diese Konstanz macht sie sehr effizient, JAZ-Werte von 4,0 bis
4,5 sind Standard, auch im Winter. Der Nachteil sind die höheren Investitionskosten für die Bohrung.
Dafür sieht die Bundesförderung laut Quelle einen zusätzlichen Bohrbonus von 5.000 Euro vor, der die
Mehrkosten deutlich reduziert.</p>
<h3>Wasser-Wasser-Wärmepumpe (Grundwasser)</h3>
<p>Sie nutzt Grundwasser mit ganzjährig 8 bis 12 °C und erreicht die höchsten JAZ-Werte aller Typen,
typischerweise 4,5 bis 5,5. Nötig sind ein Förderbrunnen zur Entnahme und ein Schluckbrunnen zur
Rückführung. Das System ist genehmigungspflichtig und setzt ausreichend Grundwasser in geeigneter
Qualität voraus. Wo diese Bedingungen erfüllt sind, ist es die effizienteste Heizlösung.</p>
{A.cta("Welche Wärmepumpe passt zu Ihrem Gebäude?",
       "Wir prüfen Wärmequelle, Heizsystem und Dämmung kostenlos vor Ort und dimensionieren die Anlage "
       "auf Ihren tatsächlichen Wärmebedarf.",
       secondary=("waermepumpe", "Zum Wärmepumpen-Installateur"))}
"""),
        ("Wann arbeitet eine Wärmepumpe am effizientesten?", "effizienz-faktoren", f"""
<p>Eine Wärmepumpe funktioniert grundsätzlich in jedem Gebäude. Ihre maximale Effizienz erreicht sie
aber unter bestimmten Bedingungen. Die wichtigste Faustregel: Je kleiner die Temperaturdifferenz
zwischen Wärmequelle und Heizsystem, desto weniger Strom wird benötigt.</p>
<ul>
  <li><b>Niedrige Vorlauftemperatur:</b> Fußbodenheizungen und Wandheizungen arbeiten mit 30 bis 40 °C,
  der Idealfall. Auch mit konventionellen Heizkörpern funktioniert eine moderne Wärmepumpe, solange
  die maximale Vorlauftemperatur von 55 °C nicht überschritten wird. In vielen Bestandsgebäuden reicht
  ein hydraulischer Abgleich, um die Vorlauftemperatur zu senken (siehe
  {a('/waermepumpe-im-altbau/', 'Wärmepumpe im Altbau')}).</li>
  <li><b>Gute Gebäudedämmung:</b> Je besser gedämmt, desto weniger Heizleistung ist nötig und desto
  kleiner und effizienter kann die Wärmepumpe ausgelegt werden. Auch bei mittlerem Dämmstandard ist ein
  wirtschaftlicher Betrieb möglich, entscheidend ist die richtige Auslegung.</li>
  <li><b>Richtige Dimensionierung:</b> Eine zu große Wärmepumpe taktet häufig ein und aus, das senkt die
  Effizienz und erhöht den Verschleiß. Eine zu kleine schafft an kalten Tagen die Heizlast nicht. Basis
  der Auslegung sind Heizlastberechnung, Gebäudedaten und Nutzungsverhalten.</li>
  <li><b>Eigener Solarstrom:</b> Wer den Strom mit einer PV-Anlage selbst erzeugt, senkt die
  Betriebskosten nochmals drastisch. EBZ Energie plant Wärmepumpe und Photovoltaik als abgestimmtes
  Gesamtpaket.</li>
</ul>
"""),
        ("Wärmepumpe und Photovoltaik: die Kombination, die unabhängig macht", "photovoltaik", f"""
<p>Die Wärmepumpe senkt Ihre Heizkosten um bis zu 75 Prozent, die PV-Anlage produziert den Strom dafür
vom eigenen Dach. Zusammen machen sie Ihr Haus nahezu energieautark:</p>
{A.net([
    ("☀", "PV-Anlage", "produziert tagsüber Strom, auch im Winter bei flacher Sonne"),
    ("♨", "Wärmepumpe", "vervielfacht den Solarstrom zu Heizwärme und Warmwasser"),
    ("▮", "Batteriespeicher", "hält Überschuss für Abend und Nacht bereit"),
    ("⌂", "Haushalt", "nutzt den Rest, Überschuss geht ins Netz"),
], "Energiemanagement als Schaltzentrale",
   "Ein Energiemanagementsystem lässt die Wärmepumpe dann laufen, wenn die PV-Anlage Überschuss hat.")}
<p>Eine durchschnittliche Wärmepumpe verbraucht 3.000 bis 5.000 kWh Strom pro Jahr. Mit einer passend
dimensionierten {a('photovoltaik', 'PV-Anlage')} decken Sie einen Großteil dieses Bedarfs selbst, den
Rest speisen Sie ein oder speichern ihn im {a('batteriespeicher', 'Batteriespeicher')}. Beide Systeme
werden separat gefördert: die Wärmepumpe über die
{a('/sanierungsoffensive-2026/', 'Sanierungsoffensive 2026')} (Kesseltausch), die PV-Anlage über den
EAG-Investitionszuschuss. Wer beides gemeinsam plant, maximiert Förderung und Ersparnis. Details zur
Dimensionierung: {a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}.</p>
"""),
        ("Fazit: Wissen ist der erste Schritt, die Auslegung der zweite", "fazit", f"""
<p>Die Funktionsweise einer Wärmepumpe ist einfach: Umgebungswärme aufnehmen, verdichten, an das
Heizsystem abgeben, entspannen. Aus 1 kWh Strom werden so 4 bis 5 kWh Wärme, ein Verhältnis, das keine
fossile Heizung erreicht. Ob die Anlage dieses Potenzial im Alltag ausschöpft, entscheidet sich bei
der Planung: Wärmequelle, Vorlauftemperatur, Dämmung und Dimensionierung müssen zum Gebäude passen.</p>
{A.cta("Jetzt unverbindlich beraten lassen",
       "Wir berechnen Ihr Sparpotenzial, wählen die passende Wärmequelle und planen auf Wunsch die "
       "PV-Anlage gleich mit.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Ihr regionaler Partner für Wärmepumpe und Photovoltaik: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("Sie wissen jetzt, wie eine Wärmepumpe funktioniert. Zwischen dem Wissen und der warmen "
                 "Stube liegt die Umsetzung. EBZ Energie aus Villach plant und installiert Wärmepumpen und "
                 "Photovoltaik in Kärnten und der Steiermark, mit einem festangestellten Team aus "
                 "zertifizierten Fachkräften, 300+ dokumentierten Projekten in 6 Bundesländern und bis zu "
                 "30 Jahren Leistungsgarantie."),
        "grid": [
            ("Regionale Expertise", "Wir kennen Bauvorschriften, Netzbetreiber und Förderstellen vor Ort."),
            ("Zertifizierte Fachkräfte", "Montage durch unser festangestelltes Team, keine Qualitätskompromisse."),
            ("Alles aus einer Hand", "Beratung, Planung, Montage und Förderabwicklung mit einem Ansprechpartner."),
            ("Langfristiger Partner", "Auch nach der Installation für Fragen, Überwachung und Service-Checks da."),
        ],
    },

    "faq": [
        ("Funktioniert eine Wärmepumpe auch bei Minusgraden?",
         "Ja. Moderne Luft-Wasser-Wärmepumpen arbeiten zuverlässig bis -20 °C und darunter. Die Effizienz "
         "sinkt bei extremer Kälte leicht, die Wärmepumpe liefert aber auch an den kältesten Tagen genug "
         "Heizwärme. Erdwärme- und Grundwassersysteme sind von der Außentemperatur praktisch unabhängig, "
         "weil ihre Quelle ganzjährig 8 bis 12 °C hat."),
        ("Kann ich meine bestehenden Heizkörper weiternutzen?",
         "In den meisten Fällen ja. Moderne Wärmepumpen liefern Vorlauftemperaturen bis 55 °C, was für "
         "viele konventionelle Heizkörper reicht. Ideal sind Fußbodenheizungen oder großflächige Radiatoren. "
         "Ob Ihre Heizkörper geeignet sind, prüft EBZ Energie bei der kostenlosen Erstberatung vor Ort, "
         "oft reicht ein hydraulischer Abgleich."),
        ("Wie laut ist eine Wärmepumpe?",
         "Die Außeneinheit einer modernen Luft-Wasser-Wärmepumpe erzeugt im Betrieb etwa 35 bis 50 Dezibel, "
         "vergleichbar mit einem leisen Gespräch. Durch geschickte Platzierung, schallgedämmte Gehäuse und "
         "Inverter-Technik lässt sich die Geräuschbelastung für Sie und Ihre Nachbarn minimieren."),
        ("Wie hoch sind die jährlichen Betriebskosten einer Wärmepumpe?",
         "Für ein durchschnittliches Einfamilienhaus liegen die Stromkosten bei etwa 600 bis 1.200 Euro pro "
         "Jahr, abhängig von Gebäudegröße, Dämmung und Wärmepumpentyp. Eine Ölheizung verursacht "
         "typischerweise 2.000 bis 3.000 Euro Brennstoffkosten. Mit Photovoltaik sinken die Kosten nochmals "
         "deutlich."),
        ("Erzeugt eine Wärmepumpe auch Warmwasser?",
         "Ja. Die Wärmepumpe übernimmt Raumheizung und Warmwasserbereitung, dazu wird ein passend "
         "dimensionierter Warmwasserspeicher eingebunden. Moderne Geräte erreichen 55 bis 60 °C "
         "Wassertemperatur, das reicht für den gesamten Haushaltsbedarf."),
        ("Was ist der Unterschied zwischen COP und Jahresarbeitszahl?",
         "Der COP beschreibt die Effizienz in einem einzelnen Betriebspunkt unter Laborbedingungen. Die "
         "Jahresarbeitszahl (JAZ) misst die reale Effizienz über ein ganzes Heizjahr inklusive Wintertagen, "
         "Warmwasser und Abtauzyklen. Sie liegt deshalb etwas niedriger und ist die aussagekräftigere Zahl."),
        ("Welches Kältemittel verwenden moderne Wärmepumpen?",
         "Viele aktuelle Geräte arbeiten mit R290 (Propan), einem natürlichen Kältemittel mit einem "
         "Siedepunkt von rund -42 °C. Deshalb kann es selbst bei Außenluft weit unter null Grad verdampfen "
         "und Umgebungswärme aufnehmen."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Wärmepumpen, PV-Anlagen und Speicher in Kärnten und der Steiermark. Dieser Artikel "
                    "dient der allgemeinen Information über die Funktionsweise von Wärmepumpen, für Ihr "
                    "Gebäude zählt die individuelle Auslegung vor Ort."),
    "related": [
        ("waermepumpe", "Wärmepumpen-Installateur in Kärnten und Steiermark"),
        ("/heizen-mit-waermepumpe/", "Heizen mit Wärmepumpe: Grundlagen"),
        ("/kosten-einer-waermepumpe/", "Kosten einer Wärmepumpe 2026"),
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau: Lohnt sie sich?"),
    ],
    "cta": {
        "h3": "Sparpotenzial berechnen lassen",
        "text": "Kostenlose Vor-Ort-Analyse, passende Wärmequelle und Festpreisangebot aus einer Hand.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Von der Umgebungswärme zur warmen Stube",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
