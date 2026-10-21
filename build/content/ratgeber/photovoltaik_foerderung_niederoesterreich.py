"""Ratgeber: Photovoltaik-Förderung Niederösterreich 2026.

Migriert vom Live-Artikel ebz-photovoltaik.at/photovoltaik-foerderung-niederoesterreich/
(Stand der Quelle: Juni 2026), nach README optimiert. Zahlen aus der Quelle
(EAG-Novelle 2026, NÖ Wohnbauförderung, PV-Parkplatzüberdachungen, Gemeindeförderungen).
Stand ab 23.10.2026: letzter EAG-Call lief 8. bis 22.10.2026, derzeit kein Bundeszuschuss; 2027
Systemfoerderung laut BMWET geplant, nicht beschlossen.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

EAG_TABLE = A.table(
    ["Kategorie", "Anlagengröße", "Fördersatz PV", "Speicher"],
    [
        ["A", "bis 10 kWp", "150 €/kWp", "150 €/kWh (max. 50 kWh)"],
        ["B", "10 bis 20 kWp", "140 €/kWp", "150 €/kWh (max. 50 kWh)"],
        ["C", "20 bis 100 kWp", "max. 130 €/kWp", "150 €/kWh (max. 50 kWh)"],
        ["D", "100 bis 1.000 kWp", "max. 120 €/kWp", "150 €/kWh (max. 50 kWh)"],
    ],
    hl_cols=(2,),
)

ARTICLE = {
    "slug": "photovoltaik-foerderung-niederoesterreich",
    "path": "/photovoltaik-foerderung-niederoesterreich/",
    "title": "PV-Förderung NÖ 2026: Wohnbau, Gemeinde, EAG beendet | EBZ",
    "description": ("PV-Förderung Niederösterreich 2026: Wohnbauförderung mit Punktesystem, Gemeinde 200 bis "
                    "1.000 €. Der EAG-Call endete am 22. Oktober, Bund derzeit nicht offen."),
    "eyebrow": "Förderung · Niederösterreich",
    "crumb_label": "PV-Förderung Niederösterreich 2026",
    "h1": "Photovoltaik-Förderung Niederösterreich 2026: Wohnbauförderung, Gemeinde und was nach dem letzten EAG-Call gilt",
    "lead": ("Niederösterreich zahlt keine PV-Pauschale, sondern rechnet Photovoltaik über ein Punktesystem in die "
             "Wohnbauförderung ein. Zusammen mit der EAG-Bundesförderung, der Spezialschiene für "
             "PV-Parkplatzüberdachungen und einer landesweit einmaligen Dichte an Gemeindeförderungen waren im "
             "Call 2026 für 10 kWp mit Speicher rund 4.650 bis 7.450 €* erreichbar. Der letzte EAG-Call lief vom "
             "8. bis 22. Oktober 2026, derzeit ist kein Bundeszuschuss beantragbar."),
    "chips": [
        "EAG im Call 2026: <b>150 €/kWp</b> + 150 €/kWh",
        "Land NÖ: <b>Punktesystem</b> Wohnbauförderung",
        "Parkplatz-PV: <b>bis 45 %</b> der Mehrkosten",
        "Gemeinde: <b>200 bis 1.000 €</b>",
    ],
    "date_published": "2026-05-10",
    "date_modified": "2026-10-21",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit Photovoltaikanlage auf dem Dach als Beispiel für eine geförderte Eigenheimsanierung",

    "tldr": [
        "Keine direkte PV-Pauschale: Niederösterreich integriert Photovoltaik in das Punktesystem der "
        "Wohnbauförderung, bei Eigenheimsanierung und Neubau. Speicher bringen zusätzliche Punkte.",
        "Die EAG-Bundesförderung war 2026 der stärkste Hebel: 150 €/kWp bis 10 kWp, 140 €/kWp bis 20 kWp, 150 €/kWh "
        "Speicher bis 50 kWh, plus 10 % Made-in-Europe-Bonus. Der letzte Call endete am 22. Oktober 2026, derzeit "
        "ist kein Bundeszuschuss beantragbar; ab 2027 ist laut BMWET eine Systemförderung geplant, nicht beschlossen.",
        "Spezialschiene PV-Parkplatzüberdachungen: 2 Millionen Euro Budget, bis 45 % der umweltrelevanten "
        "Mehrkosten, einziger Einreichtermin 2026 war der 30. Juni.",
        "Gemeindeförderungen von 200 bis 1.000 € gibt es in Niederösterreich in einer Dichte wie in keinem "
        "anderen Bundesland.",
        "Doppelstrategie im Call 2026: Speicher über die EAG, PV über EAG und Wohnbauförderung. Beispiel 10 kWp "
        "mit 10 kWh Speicher: rund 4.650 bis 7.450 €*, also rund 21 bis 34 % der Kosten. Aktuell bleiben ohne "
        "Bund Wohnbau- und Gemeindeförderung.",
    ],
    "kpis": [
        ("150 €/kWp", "EAG-Zuschuss Kategorie A im Call 2026"),
        ("2 Mio. €", "Budget PV-Parkplatzüberdachungen 2026"),
        ("45 %", "max. Förderquote Parkplatz-Schiene"),
        ("bis 7.450 €", "Beispiel 10 kWp + 10 kWh, alle Schienen im Call 2026*"),
    ],

    "sections": [
        ("Die Photovoltaik-Förderung Niederösterreich 2026 im Überblick", "ueberblick", f"""
<p>Niederösterreich gehört zu den führenden Bundesländern beim PV-Ausbau: Bereits 2023 wurden über 43.000 neue
Anlagen fertiggestellt. Anders als Kärnten oder Tirol zahlt das größte Bundesland aber keine direkte
PV-Pauschale. Stattdessen werden Photovoltaikanlagen in die Wohnbauförderung integriert, ein Punktesystem, das
bei Sanierungs- und Neubauprojekten die Förderhöhe erhöht. Dazu kommen die EAG-Bundesförderung, eine
Spezialschiene für PV-Parkplatzüberdachungen und besonders viele Gemeindeförderungen. Der letzte EAG-Call
endete am 22. Oktober 2026, derzeit ist kein Bundeszuschuss beantragbar.</p>
{A.table(
    ["Ebene", "Förderung 2026", "Für wen"],
    [
        ["Bund (EAG)", "im Call 2026: 150 €/kWp (Kat. A) + 150 €/kWh Speicher + Made-in-Europe-Bonus; letzter Call 8. bis 22. Oktober 2026 beendet, Systemförderung 2027 geplant", "alle netzgekoppelten PV-Anlagen"],
        ["Land NÖ", "Punktesystem der Wohnbauförderung (Sanierung, Neubau)", "Eigenheime, Bestandsgebäude"],
        ["Land NÖ (Spezial)", "PV-Parkplatzüberdachungen, 2 Mio. €, bis 45 % der Mehrkosten", "Gemeinden, Unternehmen, Vereine, konfessionelle Einrichtungen"],
        ["Gemeinde", "200 bis 1.000 €, je nach Gemeinde", "Haushalte in Gemeinden mit eigenem Programm"],
    ],
    hl_cols=(1,),
)}
<p>Die niederösterreichische Wohnbauförderung gilt voraussichtlich bis Ende 2026 in der aktuellen Form, ab 2027
soll ein neues Zuschussmodell starten. Die im November 2025 novellierte Richtlinie berücksichtigt
Batteriespeicher bereits explizit auch im Einfamilienhausbereich. Den Vergleich mit den anderen Bundesländern
finden Sie im {a('/photovoltaik-landesfoerderungen/', 'Überblick aller neun Landesförderungen')}.</p>
"""),
        ("EAG-Bundesförderung: der stärkste Hebel in Niederösterreich 2026", "eag", f"""
<p>Weil Niederösterreich keine PV-Pauschale kennt, war die EAG-Bundesförderung 2026 der zentrale Zuschuss. Mit der
EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026, kundgemacht am 16. Jänner 2026, standen 60 Millionen Euro
für PV- und Speicherprojekte bereit. Speicher wurden im Call 2026 mit 150 €/kWh bis maximal 50 kWh gefördert, nur
in Kombination mit einer PV-Neuerrichtung oder -Erweiterung. Der Made-in-Europe-Bonus brachte je 10 % pro
Komponente auf der White List der OeMAG.</p>
{EAG_TABLE}
<p>Die drei Fördercalls 2026 liefen vom 23. April bis 11. Mai, vom 16. bis 30. Juni sowie vom 8. bis 22. Oktober,
online über die EAG-Abwicklungsstelle, in den Kategorien A und B mit Ticketziehung und Antrag vor
Inbetriebnahme. Im bisherigen System gibt es keinen weiteren Call, neue Anlagen bekommen derzeit keinen
Bundeszuschuss. Ab 2027 ist laut BMWET eine Systemförderung geplant, nicht beschlossen: Speicher mit
intelligenter Steuerung, Antrag nach Installation und Rechnung; Projekte, die ab 1. November 2026 in Betrieb
gehen, sollen beantragbar sein. Wer jetzt plant, baut deshalb mit Speicher und Energiemanagement, das bringt
auch in der Wohnbauförderung Zusatzpunkte. Alle Details im Ratgeber
{a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}.</p>
"""),
        ("Wohnbauförderung Niederösterreich: PV im Punktesystem", "wohnbau", f"""
<p>Das Herzstück der Landesförderung ist die Wohnbauförderung, im Neubau wie in der Eigenheimsanierung. Die
Logik: Ökologische Maßnahmen, darunter PV-Anlagen, bringen Zuschlagspunkte, und mehr Punkte bedeuten eine
höhere Förderung. Ein Stromspeicher bringt weitere Punkte.</p>
<h3>Neubau</h3>
<p>Bei Variante B (standardisierte Wärmedämmung mit optimierter Haustechnik) ist die Errichtung einer PV-Anlage
mit mindestens 2 kWp, einer Solaranlage oder einer Wohnraumlüftung verpflichtend. Ergänzungspunkte für
Photovoltaik gibt es nur für die Leistung über der Mindestanforderung. Ein zusätzlicher Speicher erhöht die
erreichbare Punktezahl und damit die Gesamtförderung.</p>
<h3>Eigenheimsanierung</h3>
<p>Für Bestandsgebäude gilt eine andere Logik: Hier ist auch die alleinige Errichtung einer PV-Anlage
förderfähig, ohne weitere Sanierungsmaßnahmen. Auch hier bringt ein Speicher Zusatzpunkte. Die tatsächliche
Förderhöhe hängt von Energiekennzahl, Dämmstandard, weiteren Nachhaltigkeitskriterien und gegebenenfalls einem
Jungfamilien-Bonus ab. Details veröffentlicht das Land Niederösterreich.</p>
{A.box("Das aktuelle Fördermodell gilt voraussichtlich bis Ende 2026, ab 2027 soll ein neues Zuschussmodell "
       "starten. Wer eine Sanierung mit PV plant, sollte jetzt prüfen, ob das aktuelle System günstiger ist als "
       "das künftige.", label="Übergang 2027:")}
"""),
        ("PV-Parkplatzüberdachungen: Spezialschiene für Unternehmen und Gemeinden", "parkplatz", f"""
<p>Für PV-Parkplatzüberdachungen hat das Land Niederösterreich 2026 zwei Millionen Euro bereitgestellt. Gefördert
wird die Errichtung netzgebundener PV-Anlagen als Überdachung bestehender, befestigter, kostenfrei und öffentlich
zugänglicher Parkplätze. Antragsberechtigt sind Gebietskörperschaften, Unternehmen, Vereine und konfessionelle
Einrichtungen.</p>
<ul>
  <li><b>Budget:</b> 2 Mio. € für 2026</li>
  <li><b>Einreichung:</b> einziger Stichtag 2026 war der 30. Juni, vollständige Anträge wurden ab Anfang März laufend entgegengenommen</li>
  <li><b>Förderzusage:</b> Juryentscheid voraussichtlich bis 30. September 2026</li>
  <li><b>Förderquote:</b> maximal 45 % der umweltrelevanten Mehrkosten, abhängig von Anlagengröße und Errichtungskosten</li>
  <li><b>Umsetzungsfrist:</b> 18 Monate nach Förderzusage</li>
</ul>
<p>Bei der Reihung werden Zusatzpunkte vergeben:</p>
{A.table(
    ["Kriterium", "Bonus bei der Reihung"],
    [
        ["NÖ-Gemeinde oder Gemeindeverband", "+10 %"],
        ["Stromverbrauch im örtlichen Zusammenhang mit der PV-Anlage", "+10 %"],
        ["Speicher mit mindestens 0,5 kWh pro kWp", "+5 %"],
        ["Gleichzeitige Errichtung von E-PKW-Ladestellen", "+5 %"],
    ],
    hl_cols=(1,),
)}
<p>Eine Kombination mit anderen Förderungen ist möglich, sofern die beihilferechtlichen Höchstgrenzen eingehalten
werden. Ob es 2027 einen neuen Einreichtermin gibt, war mit Stand Juni 2026 offen. Mehr zu Carport- und
Parkplatzanlagen im Ratgeber {a('/photovoltaik-carport/', 'Photovoltaik-Carport')}.</p>
{A.cta("Gewerbe- oder Gemeindeprojekt in Niederösterreich?",
       "EBZ Energie plant Parkplatz- und Dachanlagen mit Projektbericht, 3D-Belegplan und Statikreport und "
       "bereitet die Unterlagen für Land und Bund auf.",
       secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
        ("Gemeindeförderungen: der oft unterschätzte Hebel", "gemeinden", f"""
<p>Niederösterreich hat die größte Vielfalt an Gemeindeförderungen für Photovoltaik. Viele Gemeinden zahlen
eigene Zuschüsse zusätzlich zu Land und Bund: einmalige Pauschalen, prozentuale Beteiligungen oder Speicherboni,
typisch 200 bis 1.000 €.</p>
<p>Eine Auswahl von Gemeinden mit eigenen PV-Programmen laut Quelle: Auersthal, Ebergassing (Wienerherberg),
Ernstbrunn, Großrußbach, Groß-Schweinbarth, Harmannsdorf/Rückersdorf, Hollabrunn, Kirchberg am Wagram,
Klosterneuburg, Kreuttal, Kreuzstetten, Ladendorf sowie im Raum Mödling und Baden unter anderem Brunn am Gebirge,
Perchtoldsdorf, Maria Enzersdorf, Hinterbrühl, Guntramsdorf, Wiener Neudorf, Vösendorf, Laxenburg, Baden,
Traiskirchen und Pfaffstätten.</p>
<p>Viele Gemeinden passen ihre Mittel jährlich an, manche Programme sind früh ausgeschöpft. Fragen Sie deshalb vor
der Planung beim Gemeindeamt nach oder nutzen Sie die kostenlose Energieberatung NÖ. In den meisten Fällen sind
Gemeindezuschüsse mit Landes- und Bundesförderung kombinierbar, sofern die beihilferechtlichen Höchstgrenzen eingehalten
werden.</p>
"""),
        ("Die Doppelstrategie 2026: Speicher über EAG, PV über EAG und Wohnbauförderung", "strategie", f"""
<p>Mit der EAG-Novelle 2026 war die Kombination von Bundes- und Landesförderung für PV-Anlagen bis 100 kWp
explizit erlaubt. Für Niederösterreich ergab sich daraus im Call 2026 eine klare Strategie: den Speicher über den
EAG-Zuschuss fördern (150 €/kWh), für die PV-Anlage EAG-Zuschuss und Wohnbauförderung gemeinsam nutzen. Seit
dem Ende des letzten Calls am 22. Oktober 2026 entfallen die EAG-Posten, Wohnbau- und Gemeindeförderung
bleiben. Wie die geplante Systemförderung 2027 mit der Landesförderung zusammenspielt, ist offen.</p>
<h3>Rechenbeispiel im Call 2026: 10 kWp mit 10 kWh Speicher, rund 22.000 €* Investition</h3>
{A.table(
    ["Förderposition", "Rechnung", "Betrag"],
    [
        ["EAG-Zuschuss PV (Call 2026)", "10 kWp × 150 €/kWp", "1.500 €"],
        ["EAG-Zuschuss Speicher (Call 2026)", "10 kWh × 150 €/kWh", "1.500 €"],
        ["Made-in-Europe-Bonus (Call 2026)", "20 % auf 1.500 € + 10 % auf 1.500 €", "450 €"],
        ["Wohnbauförderung NÖ (Punktesystem)", "typisch im Sanierungskontext", "1.000 bis 3.000 €*"],
        ["Gemeindeförderung", "je nach Gemeinde", "200 bis 1.000 €*"],
        ["<b>Gesamtförderung im Call 2026</b>", "", "<b>rund 4.650 bis 7.450 €*</b>"],
        ["Aktuell ohne Bund (derzeit nicht beantragbar)", "Wohnbau- und Gemeindeförderung", "rund 1.200 bis 4.000 €*"],
    ],
    hl_cols=(2,),
)}
<p>Im Call 2026 entsprach das rund 21 bis 34 % der Investitionskosten. Wer die Wohnbauförderung in einem
Sanierungsgesamtkonzept nutzt, kann darüber liegen.</p>
<p><small>*Richtwerte auf Basis der Fördersätze im Call 2026 (EAG beendet, derzeit nicht beantragbar) und des EBZ-Richtpreises von rund 15.000 bis 22.000 € für
10 kWp mit Speicher vor Förderung. Wohnbau- und Gemeindeförderung hängen von Punktezahl, Energiekennzahl und
Gemeinde ab.</small></p>
"""),
        ("Voraussetzungen und Antragsablauf", "ablauf", f"""
<ul>
  <li><b>EAG-Bund (Call 2026, beendet):</b> netzgekoppelte Anlage, Eigentum an der Liegenschaft oder schriftliche Einwilligung des Eigentümers, Stand der Technik, Installation durch eine befugte Fachkraft, Kosten-, Zeit- und Finanzierungsplan, erforderliche Genehmigungen inklusive Zählpunkt vom Netzbetreiber. Der Antrag konnte nach Beginn der Arbeiten gestellt werden, musste aber vor Inbetriebnahme erfolgen.</li>
  <li><b>Wohnbauförderung NÖ:</b> abhängig vom Programm (Eigenheimsanierung oder Neubau). Im Sanierungsfall müssen die Maßnahmen den definierten Standards entsprechen, die Energiekennzahl eine Grenze unterschreiten, und Nachweise zur thermischen und energetischen Qualität sind zu erbringen.</li>
</ul>
{A.steps([
    ("Gemeinde und Förderprogramm klären",
     "Beim Gemeindeamt oder der Energieberatung NÖ nachfragen, ob ein Gemeindezuschuss besteht, und prüfen, ob "
     "Eigenheimsanierung oder Neubau-Wohnbauförderung greift."),
    ("Planung und Komponenten",
     "Anlagengröße, Speicher und White-List-Komponenten für den Made-in-Europe-Bonus festlegen, Kosten-, Zeit- "
     "und Finanzierungsplan erstellen."),
    ("Zählpunkt und Genehmigungen",
     "Zählpunkt beim Netzbetreiber beantragen, Anzeigen oder Genehmigungen einholen. Diese Unterlagen müssen bei "
     "EAG-Antragstellung vorliegen."),
    ("EAG-Antrag im Fördercall",
     "Im Call 2026 online über die EAG-Abwicklungsstelle, mit Ticketziehung, zwingend vor Inbetriebnahme. "
     "Calls 2026: 23. April bis 11. Mai, 16. bis 30. Juni, 8. bis 22. Oktober (alle beendet). Für die geplante "
     "Systemförderung 2027 soll der Antrag laut BMWET nach Installation kommen."),
    ("Wohnbauförderung im Sanierungs- oder Neubauantrag",
     "PV und Speicher als Punkte-Maßnahmen im Antrag beim Land Niederösterreich angeben, Nachweise zur "
     "energetischen Qualität beilegen."),
    ("Inbetriebnahme, Gemeindeantrag, Endabrechnung",
     "Nach Inbetriebnahme Gemeindeförderung nach lokaler Richtlinie beantragen und, wo ein Bundesantrag läuft, die Endabrechnung einreichen."),
])}
{A.box_dark("Der häufigste Fehler im Call 2026",
    "Die Anlage ging in Betrieb, bevor der EAG-Antrag gestellt wurde. Der Bundeszuschuss war dann verloren, "
    "und die Wohnbauförderung allein deckte nur einen Teil. Für die geplante Systemförderung 2027 soll der "
    "Antrag laut BMWET erst nach Installation und Rechnung kommen (nicht beschlossen).")}
"""),
        ("Photovoltaik und Wärmepumpe im Sanierungskonzept", "waermepumpe", f"""
<p>Wer die PV-Anlage mit einer {a('waermepumpe', 'Wärmepumpe')} kombiniert, nutzt den Sonnenstrom direkt für
Heizung und Warmwasser und kann die Energiekosten um bis zu 85 % senken. Förderseitig laufen beide Systeme
getrennt: Für die PV-Anlage gelten die hier beschriebenen Schienen, für die Wärmepumpe die Sanierungsoffensive
des Bundes oder {a('/sauber-heizen-fuer-alle-2026/', '„Sauber Heizen für Alle“')}. Weil die Wohnbauförderung in
Niederösterreich bei Sanierungs-Gesamtkonzepten besonders stark wirkt, kann die Kombination PV plus Wärmepumpe
hohe Förderbeträge auslösen.</p>
"""),
        ("Fazit: Vielschichtig, aber mit klarer Strategie lohnend", "fazit", f"""
<p>Niederösterreich bietet 2026 eine vielschichtige Förderlandschaft, die strategisch genutzt werden will. Die
Wohnbauförderung belohnt PV-Investitionen im Sanierungs- und Neubaukontext über Punkte, die EAG brachte im
Call 2026 1.500 bis 2.800 € PV-Zuschuss plus Speicherförderung und Made-in-Europe-Bonus, und die
Gemeindezuschüsse gibt es in dieser Dichte in keinem anderen Bundesland. Für 10 kWp mit 10 kWh Speicher waren im
Call 2026 rund 4.650 bis 7.450 €* realistisch; seit dem 22. Oktober 2026 ist kein Bundeszuschuss beantragbar.
Voraussetzung sind sorgfältige Planung und die richtige Reihenfolge bei der Antragstellung.</p>
<p><small>Stand: Juni 2026. Förderhöhen, Budgets und Fristen können sich ändern beziehungsweise sind budgetär
begrenzt. Maßgeblich sind die Richtlinien der EAG-Abwicklungsstelle (OeMAG), des Landes Niederösterreich und
der jeweiligen Gemeinde.</small></p>
<p><b>Stand ab 23. Oktober 2026:</b> Der dritte EAG-Call lief vom 8. bis 22. Oktober 2026 und war der letzte im
bisherigen System. Neue Anlagen bekommen derzeit keinen Bundeszuschuss. Ab 2027 ist laut Eckpunkten des BMWET
eine Systemförderung geplant, aber nicht beschlossen: Antrag nach Installation und Rechnung statt Fördercall,
gefördert werden sollen Speicher mit intelligenter Steuerung, auch als Nachrüstung; Projekte mit intelligentem
Speicher, die ab 1. November 2026 in Betrieb gehen, sollen 2027 beantragbar sein. Höhe und Technikkriterien
sind noch offen. Wer jetzt plant, baut deshalb sinnvoll mit Speicher und Energiemanagement.</p>
{A.cta("Förderkombination für Ihr Projekt in Niederösterreich",
       "Wir planen PV und Speicher förderfähig, prüfen Wohnbau- und Gemeindeförderung und bereiten Ihr "
       "Projekt auf die geplante Systemförderung 2027 vor.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("finanzierung", "Finanzierung ab 147 €/Monat"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Planung und Förderabwicklung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant Photovoltaikanlagen, Speicher und Wärmepumpen und hat über 300 Projekte "
                 "in sechs Bundesländern dokumentiert. Für Projekte in Niederösterreich übernehmen wir Beratung, Planung "
                 "mit Projektbericht (3D-Belegplan und Statikreport) und die Förderabwicklung aus einer Hand: "
                 "Wohnbauförderung im Punktesystem, Gemeindeförderung, bei Bedarf die Parkplatz-Schiene und die "
                 "Vorbereitung auf die geplante Systemförderung 2027."),
        "grid": [
            ("Förderabwicklung komplett", "Wohnbauförderung, Gemeinde und Bund in der richtigen Reihenfolge."),
            ("Europäische Komponenten", "Module, Wechselrichter und Speicher mit Blick auf den geplanten Europa-Bonus 2027."),
            ("Speicher mit System", "Speicher und Energiemanagement: Zusatzpunkte im Land, Chance auf die Systemförderung 2027."),
            ("Referenzen in 6 Bundesländern", "300+ Projekte, 4,9 Sterne auf Google."),
        ],
    },

    "faq": [
        ("Gibt es in Niederösterreich 2026 eine direkte PV-Pauschalförderung?",
         "Nein. Anders als Kärnten mit seiner 3.000-Euro-Pauschale integriert Niederösterreich Photovoltaik in das "
         "Punktesystem der Wohnbauförderung: Bei Sanierung und Neubau bringen PV-Anlagen und Speicher Zusatzpunkte "
         "und damit höhere Fördersummen. Dazu kommen zahlreiche Gemeindezuschüsse; die EAG-Bundesförderung lief "
         "2026 mit dem letzten Call bis 22. Oktober aus."),
        ("Wie hoch ist die Förderung für 10 kWp mit Speicher in Niederösterreich?",
         "Im Call 2026 gab es über die EAG 1.500 € für PV und 1.500 € für einen 10-kWh-Speicher plus 450 € "
         "Made-in-Europe-Bonus, mit Wohnbau- und Gemeindeförderung in Summe rund 4.650 bis 7.450 €. Derzeit ist kein "
         "Bundeszuschuss beantragbar: Es bleiben die Wohnbauförderung (im Sanierungskontext typisch 1.000 bis 3.000 €) "
         "und die Gemeinde (200 bis 1.000 €), alles Richtwerte."),
        ("Wann ist der Stichtag für die PV-Parkplatzüberdachungs-Förderung?",
         "Der einzige Einreichtermin 2026 war der 30. Juni 2026, vollständige Anträge wurden ab Anfang März laufend "
         "entgegengenommen. Juryentscheid und Förderzusage erfolgen voraussichtlich bis 30. September 2026. Budget: "
         "2 Millionen Euro, gefördert werden bis zu 45 % der umweltrelevanten Mehrkosten, Umsetzung innerhalb von "
         "18 Monaten."),
        ("Kann ich Bundes-, Landes- und Gemeindeförderung kombinieren?",
         "Im Call 2026 waren alle drei Ebenen kombinierbar, sofern die beihilferechtlichen Höchstgrenzen "
         "eingehalten wurden; die EAG-Novelle 2026 erlaubte die Kombination für PV-Anlagen bis 100 kWp explizit. "
         "Derzeit ist kein Bundeszuschuss beantragbar, Wohnbau- und Gemeindeförderung lassen sich weiter kombinieren. "
         "Wie die geplante Systemförderung 2027 mit Landesförderungen zusammenspielt, ist offen."),
        ("Ist eine PV-Anlage ohne weitere Sanierung in der Wohnbauförderung förderfähig?",
         "Ja, bei der Eigenheimsanierung für Bestandsgebäude ist auch die alleinige Errichtung einer PV-Anlage "
         "förderfähig, ohne weitere Sanierungsmaßnahmen. Ein Speicher bringt Zusatzpunkte. Die Höhe hängt von "
         "Energiekennzahl, Dämmstandard und weiteren Kriterien ab."),
        ("Wie finde ich heraus, ob meine Gemeinde PV fördert?",
         "Rufen Sie beim Gemeindeamt an oder prüfen Sie die Gemeinde-Website. Auch die kostenlose Energieberatung NÖ "
         "und das Amt der NÖ Landesregierung geben Auskunft. Weil Programme jährlich angepasst werden und manche "
         "früh ausgeschöpft sind, fragen Sie idealerweise vor Beginn der Planung."),
        ("Wann waren die EAG-Fördercalls 2026?",
         "Die drei Calls liefen vom 23. April bis 11. Mai, vom 16. bis 30. Juni und vom 8. bis 22. Oktober 2026, mit "
         "Ticketziehung und Antrag vor Inbetriebnahme. Im bisherigen System gibt es keinen weiteren Call. Ab 2027 ist "
         "laut BMWET eine Systemförderung mit Antrag nach Installation geplant, nicht beschlossen."),
        ("Wer hilft bei der Förderabwicklung in Niederösterreich?",
         "EBZ Energie aus Villach übernimmt für Projekte in Niederösterreich Beratung, Planung und Förderabwicklung "
         "aus einer Hand: Wohnbauförderung im Punktesystem, Gemeindeförderung, Bundesantrag sobald wieder offen und bei "
         "Gewerbeprojekten die Parkplatz-Schiene. Mit über 300 Projekten in sechs Bundesländern kennen wir die "
         "Unterschiede zwischen Bund und Ländern aus der Praxis."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant PV-Anlagen, Speicher und "
                    "Wärmepumpen und übernimmt die Förderabwicklung, Referenzen liegen in sechs Bundesländern vor. "
                    "Die Angaben werden anhand der offiziellen Unterlagen von OeMAG und Land Niederösterreich geprüft. "
                    "Keine Rechts- oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("Land Niederösterreich: Eigenheimsanierung", "https://noe.gv.at/eigenheimsanierung"),
        ("Energieberatung NÖ", "https://www.enu.at"),
    ],
    "related": [
        ("/photovoltaik-landesfoerderungen/", "Vergleich: PV-Landesförderungen aller 9 Bundesländer"),
        ("/photovoltaik-foerderung-oesterreich-2026/", "Photovoltaik-Förderung Österreich 2026 (EAG)"),
        ("/photovoltaik-foerderung-burgenland/", "Photovoltaik-Förderung Burgenland"),
        ("batteriespeicher", "Batteriespeicher: Auslegung und Technik"),
    ],
    "cta": {
        "h3": "Förderung in Niederösterreich sichern",
        "text": "EAG-Call 2026 beendet: Wir kombinieren Wohnbauförderung und Gemeindezuschuss und planen mit Speicher für die geplante Systemförderung 2027.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre PV-Förderung in Niederösterreich, vollständig genutzt",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung und "
                   "Förderabwicklung aus einer Hand übernimmt."),
}
