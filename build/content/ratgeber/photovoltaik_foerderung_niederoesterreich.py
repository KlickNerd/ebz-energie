"""Ratgeber: Photovoltaik-Förderung Niederösterreich 2026.

Migriert vom Live-Artikel ebz-photovoltaik.at/photovoltaik-foerderung-niederoesterreich/
(Stand der Quelle: Juni 2026), nach README optimiert. Zahlen aus der Quelle
(EAG-Novelle 2026, NÖ Wohnbauförderung, PV-Parkplatzüberdachungen, Gemeindeförderungen).
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
    "title": "PV-Förderung Niederösterreich 2026: bis 7.450 € | EBZ",
    "description": ("PV-Förderung Niederösterreich 2026: EAG 150 €/kWp + 150 €/kWh, Wohnbauförderung mit "
                    "Punktesystem, Gemeindezuschüsse 200 bis 1.000 €. Beispiel: bis 7.450 €."),
    "eyebrow": "Förderung · Niederösterreich",
    "crumb_label": "PV-Förderung Niederösterreich 2026",
    "h1": "Photovoltaik-Förderung Niederösterreich 2026: EAG, Wohnbauförderung und Gemeinde kombiniert bis zu 7.450 €",
    "lead": ("Niederösterreich zahlt keine PV-Pauschale, sondern rechnet Photovoltaik über ein Punktesystem in die "
             "Wohnbauförderung ein. Zusammen mit der EAG-Bundesförderung, der Spezialschiene für "
             "PV-Parkplatzüberdachungen und einer landesweit einmaligen Dichte an Gemeindeförderungen sind für "
             "10 kWp mit Speicher rund 4.650 bis 7.450 €* erreichbar."),
    "chips": [
        "EAG: <b>150 €/kWp</b> + 150 €/kWh Speicher",
        "Land NÖ: <b>Punktesystem</b> Wohnbauförderung",
        "Parkplatz-PV: <b>bis 45 %</b> der Mehrkosten",
        "Gemeinde: <b>200 bis 1.000 €</b>",
    ],
    "date_published": "2026-05-10",
    "date_modified": "2026-09-24",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit Photovoltaikanlage auf dem Dach als Beispiel für eine geförderte Eigenheimsanierung",

    "tldr": [
        "Keine direkte PV-Pauschale: Niederösterreich integriert Photovoltaik in das Punktesystem der "
        "Wohnbauförderung, bei Eigenheimsanierung und Neubau. Speicher bringen zusätzliche Punkte.",
        "Die EAG-Bundesförderung ist der stärkste Hebel: 150 €/kWp bis 10 kWp, 140 €/kWp bis 20 kWp, 150 €/kWh "
        "Speicher bis 50 kWh, plus 10 % Made-in-Europe-Bonus pro gelisteter Komponente.",
        "Spezialschiene PV-Parkplatzüberdachungen: 2 Millionen Euro Budget, bis 45 % der umweltrelevanten "
        "Mehrkosten, einziger Einreichtermin 2026 war der 30. Juni.",
        "Gemeindeförderungen von 200 bis 1.000 € gibt es in Niederösterreich in einer Dichte wie in keinem "
        "anderen Bundesland.",
        "Doppelstrategie seit der EAG-Novelle 2026: Speicher über die EAG, PV über EAG und Wohnbauförderung. "
        "Beispiel 10 kWp mit 10 kWh Speicher: rund 4.650 bis 7.450 €*, also rund 21 bis 34 % der Kosten.",
    ],
    "kpis": [
        ("150 €/kWp", "EAG-Zuschuss Kategorie A (bis 10 kWp)"),
        ("2 Mio. €", "Budget PV-Parkplatzüberdachungen 2026"),
        ("45 %", "max. Förderquote Parkplatz-Schiene"),
        ("bis 7.450 €", "Beispiel 10 kWp + 10 kWh mit allen Schienen*"),
    ],

    "sections": [
        ("Die Photovoltaik-Förderung Niederösterreich 2026 im Überblick", "ueberblick", f"""
<p>Niederösterreich gehört zu den führenden Bundesländern beim PV-Ausbau: Bereits 2023 wurden über 43.000 neue
Anlagen fertiggestellt. Anders als Kärnten oder Tirol zahlt das größte Bundesland aber keine direkte
PV-Pauschale. Stattdessen werden Photovoltaikanlagen in die Wohnbauförderung integriert, ein Punktesystem, das
bei Sanierungs- und Neubauprojekten die Förderhöhe erhöht. Dazu kommen die EAG-Bundesförderung, eine
Spezialschiene für PV-Parkplatzüberdachungen und besonders viele Gemeindeförderungen.</p>
{A.table(
    ["Ebene", "Förderung 2026", "Für wen"],
    [
        ["Bund (EAG)", "150 €/kWp (Kat. A) + 150 €/kWh Speicher + Made-in-Europe-Bonus", "alle netzgekoppelten PV-Anlagen"],
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
        ("EAG-Bundesförderung: der stärkste Hebel in Niederösterreich", "eag", f"""
<p>Weil Niederösterreich keine PV-Pauschale kennt, ist die EAG-Bundesförderung der zentrale Zuschuss. Mit der
EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026, kundgemacht am 16. Jänner 2026, stehen 60 Millionen Euro
für PV- und Speicherprojekte bereit. Speicher werden mit 150 €/kWh bis maximal 50 kWh gefördert, nur in
Kombination mit einer PV-Neuerrichtung oder -Erweiterung. Der Made-in-Europe-Bonus bringt je 10 % pro
Komponente auf der White List der OeMAG.</p>
{EAG_TABLE}
<p>Die drei Fördercalls 2026 laufen vom 23. April bis 11. Mai, vom 16. bis 30. Juni sowie ab 8. Oktober. Die
Antragstellung erfolgt online über die EAG-Abwicklungsstelle, in den Kategorien A und B nach dem
First-come-first-served-Prinzip mit Ticketziehung. Der Antrag muss vor Inbetriebnahme gestellt werden, wer im
ersten Call kein Ticket zieht, fällt in der Reihung zurück. Alle Details im Ratgeber
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
       "bereitet die Unterlagen für Land und EAG auf.",
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
Gemeindezuschüsse mit Bund und Land kombinierbar, sofern die beihilferechtlichen Höchstgrenzen eingehalten
werden.</p>
"""),
        ("Die Doppelstrategie: Speicher über EAG, PV über EAG und Wohnbauförderung", "strategie", f"""
<p>Seit der EAG-Novelle 2026 ist die Kombination von Bundes- und Landesförderung für PV-Anlagen bis 100 kWp
explizit erlaubt. Für Niederösterreich ergibt sich daraus eine klare Strategie: Den Speicher lassen Sie
komplett über den EAG-Zuschuss fördern (150 €/kWh), für die PV-Anlage nutzen Sie EAG-Zuschuss und
Wohnbauförderung gemeinsam. Beide Beträge neutralisieren sich nicht.</p>
<h3>Rechenbeispiel: 10 kWp mit 10 kWh Speicher, rund 22.000 €* Investition</h3>
{A.table(
    ["Förderposition", "Rechnung", "Betrag"],
    [
        ["EAG-Zuschuss PV", "10 kWp × 150 €/kWp", "1.500 €"],
        ["EAG-Zuschuss Speicher", "10 kWh × 150 €/kWh", "1.500 €"],
        ["Made-in-Europe-Bonus", "20 % auf 1.500 € + 10 % auf 1.500 €", "450 €"],
        ["Wohnbauförderung NÖ (Punktesystem)", "typisch im Sanierungskontext", "1.000 bis 3.000 €*"],
        ["Gemeindeförderung", "je nach Gemeinde", "200 bis 1.000 €*"],
        ["<b>Gesamtförderung</b>", "", "<b>rund 4.650 bis 7.450 €*</b>"],
    ],
    hl_cols=(2,),
)}
<p>Das entspricht rund 21 bis 34 % der Investitionskosten. Wer die Wohnbauförderung in einem
Sanierungsgesamtkonzept nutzt, kann darüber liegen.</p>
<p><small>*Richtwerte auf Basis der Fördersätze 2026 und des EBZ-Richtpreises von rund 15.000 bis 22.000 € für
10 kWp mit Speicher vor Förderung. Wohnbau- und Gemeindeförderung hängen von Punktezahl, Energiekennzahl und
Gemeinde ab.</small></p>
"""),
        ("Voraussetzungen und Antragsablauf", "ablauf", f"""
<ul>
  <li><b>EAG-Bund:</b> netzgekoppelte Anlage, Eigentum an der Liegenschaft oder schriftliche Einwilligung des Eigentümers, Stand der Technik, Installation durch eine befugte Fachkraft, Kosten-, Zeit- und Finanzierungsplan, erforderliche Genehmigungen inklusive Zählpunkt vom Netzbetreiber. Der Antrag kann nach Beginn der Arbeiten gestellt werden, muss aber vor Inbetriebnahme erfolgen.</li>
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
     "Online über die EAG-Abwicklungsstelle, in Kategorie A und B mit Ticketziehung, zwingend vor Inbetriebnahme. "
     "Calls 2026: 23. April bis 11. Mai, 16. bis 30. Juni, ab 8. Oktober."),
    ("Wohnbauförderung im Sanierungs- oder Neubauantrag",
     "PV und Speicher als Punkte-Maßnahmen im Antrag beim Land Niederösterreich angeben, Nachweise zur "
     "energetischen Qualität beilegen."),
    ("Inbetriebnahme, Gemeindeantrag, Endabrechnung",
     "Nach Inbetriebnahme Gemeindeförderung nach lokaler Richtlinie beantragen und die EAG-Endabrechnung einreichen."),
])}
{A.box_dark("Der häufigste Fehler",
    "Die Anlage geht in Betrieb, bevor der EAG-Antrag gestellt wurde. Der Bundeszuschuss ist dann verloren, "
    "und die Wohnbauförderung allein deckt nur einen Teil.")}
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
Wohnbauförderung belohnt PV-Investitionen im Sanierungs- und Neubaukontext über Punkte, die EAG bringt 1.500 bis
2.800 € PV-Zuschuss plus Speicherförderung und Made-in-Europe-Bonus, und die Gemeindezuschüsse gibt es in dieser
Dichte in keinem anderen Bundesland. Für 10 kWp mit 10 kWh Speicher sind rund 4.650 bis 7.450 €* realistisch.
Voraussetzung sind sorgfältige Planung und die richtige Reihenfolge bei der Antragstellung.</p>
<p><small>Stand: Juni 2026. Förderhöhen, Budgets und Fristen können sich ändern beziehungsweise sind budgetär
begrenzt. Maßgeblich sind die Richtlinien der EAG-Abwicklungsstelle (OeMAG), des Landes Niederösterreich und
der jeweiligen Gemeinde.</small></p>
{A.cta("Förderkombination für Ihr Projekt in Niederösterreich",
       "Wir planen PV und Speicher förderfähig, prüfen Wohnbau- und Gemeindeförderung und übernehmen den "
       "EAG-Antrag im richtigen Call.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("finanzierung", "Finanzierung ab 147 €/Monat"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Planung und Förderabwicklung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant Photovoltaikanlagen, Speicher und Wärmepumpen und hat über 300 Projekte "
                 "in sechs Bundesländern dokumentiert. Für Projekte in Niederösterreich übernehmen wir Beratung, Planung "
                 "mit Projektbericht (3D-Belegplan und Statikreport) und die Förderabwicklung aus einer Hand: EAG-Call, "
                 "Wohnbauförderung im Punktesystem, Gemeindeförderung und bei Bedarf die Parkplatz-Schiene."),
        "grid": [
            ("Förderabwicklung komplett", "EAG, Wohnbauförderung und Gemeinde in der richtigen Reihenfolge."),
            ("White-List-Komponenten", "Module, Wechselrichter und Speicher mit Made-in-Europe-Bonus."),
            ("Doppelstrategie", "Speicher über EAG, PV über EAG und Wohnbauförderung."),
            ("Referenzen in 6 Bundesländern", "300+ Projekte, 4,9 Sterne auf Google."),
        ],
    },

    "faq": [
        ("Gibt es in Niederösterreich 2026 eine direkte PV-Pauschalförderung?",
         "Nein. Anders als Kärnten mit seiner 3.000-Euro-Pauschale integriert Niederösterreich Photovoltaik in das "
         "Punktesystem der Wohnbauförderung: Bei Sanierung und Neubau bringen PV-Anlagen und Speicher Zusatzpunkte "
         "und damit höhere Fördersummen. Dazu kommen die EAG-Bundesförderung und zahlreiche Gemeindezuschüsse."),
        ("Wie hoch ist die Förderung für 10 kWp mit Speicher in Niederösterreich?",
         "Über die EAG 1.500 € für PV und 1.500 € für einen 10-kWh-Speicher plus 450 € Made-in-Europe-Bonus. Die "
         "Wohnbauförderung bringt im Sanierungskontext typisch 1.000 bis 3.000 €, die Gemeinde 200 bis 1.000 €. In "
         "Summe rund 4.650 bis 7.450 €, also rund 21 bis 34 % der Kosten (Richtwerte)."),
        ("Wann ist der Stichtag für die PV-Parkplatzüberdachungs-Förderung?",
         "Der einzige Einreichtermin 2026 war der 30. Juni 2026, vollständige Anträge wurden ab Anfang März laufend "
         "entgegengenommen. Juryentscheid und Förderzusage erfolgen voraussichtlich bis 30. September 2026. Budget: "
         "2 Millionen Euro, gefördert werden bis zu 45 % der umweltrelevanten Mehrkosten, Umsetzung innerhalb von "
         "18 Monaten."),
        ("Kann ich Bundes-, Landes- und Gemeindeförderung kombinieren?",
         "Ja, grundsätzlich sind alle drei Ebenen kombinierbar, sofern die beihilferechtlichen Höchstgrenzen "
         "eingehalten werden. Seit der EAG-Novelle 2026 ist die Kombination für PV-Anlagen bis 100 kWp explizit "
         "erlaubt. Reihenfolge: EAG vor Inbetriebnahme, Wohnbauförderung im Sanierungs- oder Neubauantrag, "
         "Gemeindeförderung nach lokaler Richtlinie."),
        ("Ist eine PV-Anlage ohne weitere Sanierung in der Wohnbauförderung förderfähig?",
         "Ja, bei der Eigenheimsanierung für Bestandsgebäude ist auch die alleinige Errichtung einer PV-Anlage "
         "förderfähig, ohne weitere Sanierungsmaßnahmen. Ein Speicher bringt Zusatzpunkte. Die Höhe hängt von "
         "Energiekennzahl, Dämmstandard und weiteren Kriterien ab."),
        ("Wie finde ich heraus, ob meine Gemeinde PV fördert?",
         "Rufen Sie beim Gemeindeamt an oder prüfen Sie die Gemeinde-Website. Auch die kostenlose Energieberatung NÖ "
         "und das Amt der NÖ Landesregierung geben Auskunft. Weil Programme jährlich angepasst werden und manche "
         "früh ausgeschöpft sind, fragen Sie idealerweise vor Beginn der Planung."),
        ("Wann sind die EAG-Fördercalls 2026?",
         "Die drei Calls laufen vom 23. April bis 11. Mai, vom 16. bis 30. Juni und ab 8. Oktober 2026. In den "
         "Kategorien A und B gilt First come, first served mit Ticketziehung. Der Antrag muss vor Inbetriebnahme "
         "gestellt werden."),
        ("Wer hilft bei der Förderabwicklung in Niederösterreich?",
         "EBZ Energie aus Villach übernimmt für Projekte in Niederösterreich Beratung, Planung und Förderabwicklung "
         "aus einer Hand: EAG-Antrag im Call, Wohnbauförderung im Punktesystem, Gemeindeförderung und bei "
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
        "text": "Wir kombinieren EAG, Wohnbauförderung und Gemeindezuschuss für Ihr Projekt und stellen die Anträge rechtzeitig.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre PV-Förderung in Niederösterreich, vollständig genutzt",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung und "
                   "Förderabwicklung aus einer Hand übernimmt."),
}
