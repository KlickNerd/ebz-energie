"""Ratgeber: Photovoltaik-Förderung Tirol 2026.

Migriert vom Live-Artikel ebz-photovoltaik.at/photovoltaik-foerderung-tirol/
(Stand der Quelle: Juni 2026), nach README optimiert. Zahlen aus der Quelle
(EAG-Novelle 2026, Wohnhaussanierungsförderung Tirol, Speicher-Nachrüstung, Regionalprogramme).
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
    "slug": "photovoltaik-foerderung-tirol",
    "path": "/photovoltaik-foerderung-tirol/",
    "title": "PV-Förderung Tirol 2026: 125 €/kWp + EAG 150 €/kWp | EBZ",
    "description": ("PV-Förderung Tirol 2026: Wohnhaussanierung 50 %, max. 125 €/kWp, Speicher-Nachrüstung "
                    "100 €/kWh bis 1.000 €, EAG 150 €/kWp. Speicher gesamt bis 250 €/kWh."),
    "eyebrow": "Förderung · Tirol",
    "crumb_label": "PV-Förderung Tirol 2026",
    "h1": "Photovoltaik-Förderung Tirol 2026: 125 €/kWp vom Land, 150 €/kWp vom Bund und 250 €/kWh für den Speicher",
    "lead": ("Tirol hat die Wohnhaussanierungsförderung für PV mit 1. Jänner 2026 von 250 auf 125 €/kWp halbiert, "
             "gleichzeitig ist die neue Speicher-Nachrüstungsförderung mit 100 €/kWh gestartet. Beide Schienen "
             "sind mit der EAG-Bundesförderung kombinierbar, im Sanierungskontext sind rund 4.500 €* für eine "
             "8-kWp-Anlage mit Speicher realistisch."),
    "chips": [
        "Land: <b>125 €/kWp</b> (50 % im Sanierungspaket)",
        "Speicher Land: <b>100 €/kWh</b>, max. 1.000 €",
        "Bund: <b>150 €/kWp</b> + 150 €/kWh",
        "Speicher gesamt: <b>bis 250 €/kWh</b>",
    ],
    "date_published": "2026-05-05",
    "date_modified": "2026-09-24",
    "hero_img": "gen_detail",
    "hero_alt": "Montage von Photovoltaikmodulen auf einem sanierten Wohnhausdach",

    "tldr": [
        "EAG-Bundesförderung als Basis: 120 bis 150 €/kWp je nach Anlagengröße, 150 €/kWh Speicher und "
        "Made-in-Europe-Bonus von je 10 % pro Komponente.",
        "Tiroler Wohnhaussanierung: 50 % Einmalzuschuss auf förderbare Kosten von 250 €/kWp, also maximal "
        "125 €/kWp, nur im Rahmen eines genehmigten Sanierungsvorhabens auf einem bestehenden Wohngebäude.",
        "Neue Speicher-Nachrüstungsförderung seit 1. Jänner 2026: 100 €/kWh für die ersten 10 kWh, maximal "
        "1.000 €, Voraussetzung ist eine netzdienliche Steuerung. Mit der EAG ergibt das bis zu 250 €/kWh.",
        "Regionale Sonderprogramme in Landeck, Lechtal-Reutte und Pitztal bringen zusätzlich 20 bis 40 % "
        "Förderquote, in Pitztal auch für Privatpersonen.",
        "Reihenfolge beachten: EAG-Antrag vor Inbetriebnahme, Tiroler Landesförderung erst nach Inbetriebnahme.",
    ],
    "kpis": [
        ("125 €/kWp", "Wohnhaussanierung Tirol (50 %, max.)"),
        ("1.000 €", "Speicher-Nachrüstung Tirol (100 €/kWh)"),
        ("250 €/kWh", "Speicher Bund + Land für die ersten 10 kWh"),
        ("4.560 €", "Beispiel 8 kWp + 8 kWh im Sanierungskontext*"),
    ],

    "sections": [
        ("Die Photovoltaik-Förderung Tirol 2026 im Überblick", "ueberblick", f"""
<p>Die Tiroler Förderlandschaft 2026 ist übersichtlich strukturiert, allerdings mit halbierter Landesförderung.
Die EAG-Bundesförderung bildet die Basis mit 120 bis 150 €/kWp plus Speicherförderung und Made-in-Europe-Bonus.
Das Land Tirol fördert PV-Anlagen im Rahmen der Wohnhaussanierung mit einem Einmalzuschuss von 50 % der
förderbaren Kosten, gedeckelt bei 125 €/kWp. Neu seit 1. Jänner 2026 ist die Speicher-Nachrüstungsförderung:
100 €/kWh für bis zu 10 kWh, also maximal 1.000 € pro Anlage.</p>
{A.table(
    ["Schiene", "Förderhöhe", "Bedingung"],
    [
        ["EAG-Bund", "150 €/kWp (Kat. A) + 150 €/kWh Speicher + Bonus", "Antrag vor Inbetriebnahme im Fördercall"],
        ["Wohnhaussanierung Tirol", "50 %, max. 125 €/kWp", "nur im genehmigten Sanierungspaket"],
        ["Speicher-Nachrüstung Tirol", "100 €/kWh, max. 10 kWh / 1.000 €", "netzdienliche Steuerung, seit 1. Jänner 2026"],
        ["Regionalprogramme", "+20 bis 40 % Förderquote", "Landeck, Lechtal-Reutte, Pitztal"],
    ],
    hl_cols=(1,),
)}
<p>Die Halbierung der Wohnhaussanierungsförderung von 250 auf 125 €/kWp ab 1. Jänner 2026 begründet das Land
mit den gesunkenen Marktpreisen für PV-Module. Trotzdem bleibt Tirol eines der Bundesländer, in denen sich Land
und Bund besonders sinnvoll kombinieren lassen. Den Vergleich mit den anderen Bundesländern finden Sie im
{a('/photovoltaik-landesfoerderungen/', 'Überblick aller neun Landesförderungen')}.</p>
"""),
        ("EAG-Bundesförderung: die Basis auch in Tirol", "eag", f"""
<p>Die EAG-Bundesförderung ist der zentrale Hebel, vor allem für Hausbesitzer, die nicht im Sanierungskontext
investieren. Mit der EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026, kundgemacht am 16. Jänner 2026,
stehen 60 Millionen Euro für PV- und Speicherprojekte bereit. Stromspeicher werden mit 150 €/kWh bis maximal
50 kWh gefördert, allerdings nur in Kombination mit einer PV-Neuerrichtung oder -Erweiterung. Hinzu kommt der
Made-in-Europe-Bonus mit je 10 % pro Komponente auf der White List der OeMAG.</p>
{EAG_TABLE}
<p>Die drei Fördercalls 2026 laufen vom 23. April bis 11. Mai, vom 16. bis 30. Juni sowie ab 8. Oktober. Die
Antragstellung erfolgt online über die EAG-Abwicklungsstelle, in den Kategorien A und B nach dem
First-come-first-served-Prinzip mit Ticketziehung. Alle Details im Ratgeber
{a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}.</p>
{A.box("Der EAG-Antrag muss vor Inbetriebnahme der Anlage gestellt werden. Die Tiroler Landesförderung wird "
       "dagegen erst nach Inbetriebnahme beantragt. Wer die Reihenfolge vertauscht, verliert den Bundeszuschuss.",
       label="Reihenfolge:")}
"""),
        ("Wohnhaussanierungsförderung Tirol: PV im Sanierungspaket", "sanierung", f"""
<p>Das Herzstück der Tiroler Landesförderung für Photovoltaik ist die Wohnhaussanierungsförderung. PV-Anlagen
werden als Bestandteil eines genehmigten Sanierungsvorhabens gefördert, nicht als Einzelmaßnahme. Die Förderhöhe
beträgt 50 % der förderbaren Kosten, maximal 125 €/kWp. Die Kostenobergrenze für die Förderberechnung liegt bei
250 €/kWp installierter Leistung.</p>
<p>Rechenbeispiel: Eine 8-kWp-Anlage hat förderbare Kosten von 8 × 250 € = 2.000 €. 50 % davon ergeben einen
Einmalzuschuss von 1.000 €. Bei 10 kWp sind es maximal 10 × 125 € = 1.250 €.</p>
<ul>
  <li>Errichtung auf einem bestehenden Wohngebäude (Ein- oder Mehrfamilienhaus)</li>
  <li>PV-Errichtung ist Teil eines genehmigten Sanierungsvorhabens</li>
  <li>Technische Mindestanforderungen erfüllt, sinnvolle Auslegung der Anlage</li>
  <li>Fachgerechte Installation durch ein gewerblich befugtes Unternehmen</li>
</ul>
<p>Alternativ zum Einmalzuschuss bietet Tirol einen Annuitätenzuschuss (zum Beispiel 55 % der Anfangsbelastung),
der für längerfristig finanzierte Sanierungen interessant sein kann. Welche Variante besser passt, hängt vom
Sanierungskonzept ab. Die Wohnhaussanierungsförderung ist mit der EAG kombinierbar, sofern die
beihilferechtlichen Höchstgrenzen eingehalten werden.</p>
"""),
        ("Speicher-Nachrüstungsförderung Tirol: 100 €/kWh seit 1. Jänner 2026", "speicher", f"""
<p>Das Land Tirol fördert seit 1. Jänner 2026 netzdienliche Stromspeichersysteme, um den Eigenverbrauch von
Solarstrom zu erhöhen und das Netz zu entlasten. Gefördert werden neu installierte Speicher und Erweiterungen
bestehender Speicher, sofern sie über eine steuerbare Schnittstelle verfügen und netzdienlich betrieben werden
können.</p>
<ul>
  <li><b>Förderhöhe:</b> 100 €/kWh, in der Regel für die ersten 10 kWh, maximal 1.000 € pro Anlage</li>
  <li><b>Antragsberechtigt:</b> Privatpersonen, Betriebe und juristische Personen mit Anlagenstandort in Tirol</li>
  <li><b>Voraussetzung:</b> Installation und Inbetriebnahme ab 1. Jänner 2026, kompatible netzdienliche Steuerung</li>
  <li><b>Antrag:</b> online über das Landesportal Tirol, nach Inbetriebnahme, alle Rechnungen auf den Antragsteller</li>
</ul>
{A.table(
    ["Speicherförderung", "€/kWh"],
    [
        ["EAG-Bund", "150 €/kWh"],
        ["Land Tirol (Nachrüstung)", "100 €/kWh"],
        ["<b>Gesamt für die ersten 10 kWh</b>", "<b>bis 250 €/kWh</b>"],
    ],
    hl_cols=(1,),
)}
<p>Ein 10-kWh-Speicher bringt damit bis zu 2.500 € Förderung aus Bund und Land. Welche Systeme netzdienlich
steuerbar sind, klären wir in der Planung, siehe {a('batteriespeicher', 'Batteriespeicher')} und
{a('/foerderung-fuer-pv-speicher/', 'Förderung für PV-Speicher')}.</p>
{A.cta("Speicher netzdienlich planen, 250 €/kWh mitnehmen",
       "EBZ Energie legt Speicher und Steuerung so aus, dass EAG und Tiroler Nachrüstungsförderung zusammen "
       "greifen, mit Projektbericht, 3D-Belegplan und Statikreport.",
       secondary=("batteriespeicher", "Zum Batteriespeicher"))}
"""),
        ("Regionale Sonderprogramme: Landeck, Lechtal-Reutte, Pitztal", "regional", f"""
<p>Eine Tiroler Besonderheit sind regionale Sonderförderprogramme, die den PV-Ausbau lokal beschleunigen sollen
und je nach Region zusätzlich 20 bis 40 % Förderquote ermöglichen:</p>
{A.table(
    ["Region", "Förderberechtigt", "Besonderheit"],
    [
        ["Landeck", "Betriebe, Gemeinden, Energiegemeinschaften, Vereine", "+20 bis 40 % möglich"],
        ["Lechtal-Reutte", "Betriebe, Gemeinden, Energiegemeinschaften, Vereine", "+20 bis 40 % möglich"],
        ["Pitztal", "auch Privatpersonen, Betriebe und Gemeinden", "breiteste Zielgruppe"],
    ],
    hl_cols=(2,),
)}
<p>Förderhöhen und Voraussetzungen variieren stark, die Programme sind zeitlich und budgetär begrenzt.
Informieren Sie sich vor Projektstart direkt bei der Regionalstelle oder beim Land Tirol. In Kombination mit
Bund und Land sind hier außergewöhnlich hohe Gesamtquoten möglich.</p>
"""),
        ("Rechenbeispiel: 8 kWp mit 8 kWh Speicher im Sanierungskontext", "rechenbeispiel", f"""
{A.table(
    ["Förderposition", "Rechnung", "Betrag"],
    [
        ["EAG-Zuschuss PV", "8 kWp × 150 €/kWp", "1.200 €"],
        ["EAG-Zuschuss Speicher", "8 kWh × 150 €/kWh", "1.200 €"],
        ["Wohnhaussanierung Tirol", "8 kWp × 125 €/kWp", "1.000 €"],
        ["Speicher-Nachrüstung Tirol", "8 kWh × 100 €/kWh", "800 €"],
        ["Made-in-Europe-Bonus", "20 % auf 1.200 € + 10 % auf 1.200 €", "360 €"],
        ["<b>Gesamtförderung</b>", "", "<b>rund 4.560 €*</b>"],
    ],
    hl_cols=(2,),
)}
<p>Mit einem 10-kWh-Speicher steigt die Summe auf rund 5.100 €* (1.500 € EAG-Speicher, 1.000 € Land, 390 € Bonus).
Außerhalb des Sanierungskontexts, also ohne Wohnhaussanierungsförderung, bleiben rund 3.000 bis 3.500 €*.
Bezogen auf Investitionskosten von rund 22.000 €* für 10 kWp mit Speicher entspricht die Förderung im
Sanierungskontext rund einem Fünftel der Kosten. In Pitztal, Landeck oder Lechtal-Reutte kommen die
Regionalprogramme dazu.</p>
<p><small>*Richtwerte auf Basis der Fördersätze 2026 und des EBZ-Richtpreises von rund 15.000 bis 22.000 € für
10 kWp mit Speicher vor Förderung. Die tatsächliche Höhe hängt von Anlagengröße, Speicher, Komponenten und
dem Sanierungsvorhaben ab.</small></p>
"""),
        ("Voraussetzungen und Antragsablauf in der richtigen Reihenfolge", "ablauf", f"""
<ul>
  <li><b>EAG-Bund:</b> netzgekoppelte Anlage, Antrag vor Inbetriebnahme, Genehmigungen oder Anzeigen liegen bei Antragstellung vor, Stand der Technik und Sicherheitsanforderungen</li>
  <li><b>Wohnhaussanierung Tirol:</b> PV ist Teil eines genehmigten Sanierungsvorhabens auf einem bestehenden Wohngebäude, technische Mindestanforderungen, Installation durch ein gewerblich befugtes Unternehmen</li>
  <li><b>Speicher-Nachrüstung Tirol:</b> Installation und Inbetriebnahme ab 1. Jänner 2026, netzdienliche Steuerung, Antrag nach Inbetriebnahme, Rechnungen auf den Antragsteller</li>
</ul>
{A.steps([
    ("Sanierungsvorhaben und Regionalprogramm klären",
     "Wird die PV-Anlage Teil einer Wohnhaussanierung? Dann das Sanierungsvorhaben beim Land genehmigen lassen. "
     "Liegt der Standort in Landeck, Lechtal-Reutte oder Pitztal, Regionalstelle kontaktieren."),
    ("Planung mit netzdienlichem Speicher",
     "Anlagengröße, Speicher mit steuerbarer Schnittstelle und White-List-Komponenten für den Made-in-Europe-Bonus "
     "festlegen."),
    ("EAG-Antrag im Fördercall",
     "Online über die EAG-Abwicklungsstelle, in Kategorie A und B mit Ticketziehung, zwingend vor Inbetriebnahme. "
     "Calls 2026: 23. April bis 11. Mai, 16. bis 30. Juni, ab 8. Oktober."),
    ("Errichtung und Inbetriebnahme",
     "Installation durch ein gewerblich befugtes Unternehmen, Rechnungen auf den Antragsteller ausstellen lassen."),
    ("Tiroler Landesförderung beantragen",
     "Nach Inbetriebnahme: Speicher-Nachrüstung online über das Landesportal Tirol, PV-Zuschuss im Rahmen der "
     "Wohnhaussanierung. Danach EAG-Endabrechnung einreichen."),
])}
{A.box_dark("Der häufigste Fehler",
    "Erst die Anlage in Betrieb nehmen und dann den EAG-Antrag stellen. Der Bundeszuschuss ist damit verloren, "
    "und die Tiroler Landesförderung allein deckt nur einen Bruchteil.")}
"""),
        ("Photovoltaik und Wärmepumpe im Sanierungspaket", "waermepumpe", f"""
<p>Wer die PV-Anlage mit einer {a('waermepumpe', 'Wärmepumpe')} kombiniert, nutzt den Sonnenstrom direkt für
Heizung und Warmwasser und kann die Energiekosten um bis zu 85 % senken. Förderseitig laufen beide Systeme
getrennt: Für die PV-Anlage gelten die hier beschriebenen Schienen, für die Wärmepumpe die Sanierungsoffensive
des Bundes und {a('/sauber-heizen-fuer-alle-2026/', '„Sauber Heizen für Alle“')}. In Tirol kann zusätzlich die
Wohnhaussanierungsförderung greifen, wenn beide Maßnahmen Teil eines Sanierungsgesamtkonzepts sind.</p>
"""),
        ("Fazit: Halbiert, aber in der Kombination weiterhin attraktiv", "fazit", f"""
<p>Die Photovoltaik-Förderung in Tirol 2026 ist nach der Halbierung der Wohnhaussanierungsförderung weniger üppig
als in den Vorjahren, im Vergleich zu vielen anderen Bundesländern aber weiterhin gut strukturiert. Der Schlüssel
liegt in der Kombination: EAG-Bundesförderung für PV und Speicher, Wohnhaussanierungsförderung im
Sanierungskontext, Speicher-Nachrüstungsförderung für die ersten 10 kWh und gegebenenfalls Regionalprogramme.
Für eine 8-kWp-Anlage mit 8-kWh-Speicher im Sanierungskontext sind rund 4.560 €* realistisch. Voraussetzung ist
die richtige Reihenfolge: EAG vor Inbetriebnahme, Land danach.</p>
<p><small>Stand: Juni 2026. Förderhöhen, Budgets und Fristen können sich ändern beziehungsweise sind budgetär
begrenzt. Maßgeblich sind die Richtlinien der EAG-Abwicklungsstelle (OeMAG) und des Landes Tirol.</small></p>
{A.cta("Förderkombination für Ihr Projekt in Tirol",
       "Wir planen PV, Speicher und Steuerung förderfähig und übernehmen EAG-Antrag und Landesförderung in der "
       "richtigen Reihenfolge.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("finanzierung", "Finanzierung ab 147 €/Monat"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Planung und Förderabwicklung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant Photovoltaikanlagen, Speicher und Wärmepumpen und hat über 300 Projekte "
                 "in sechs Bundesländern dokumentiert. Für Projekte in Tirol übernehmen wir Beratung, Planung mit "
                 "Projektbericht (3D-Belegplan und Statikreport) und die Förderabwicklung aus einer Hand: EAG-Call, "
                 "Wohnhaussanierung, Speicher-Nachrüstung und Regionalprogramme in der richtigen Reihenfolge."),
        "grid": [
            ("Förderabwicklung komplett", "EAG vor Inbetriebnahme, Landesförderung danach."),
            ("Netzdienliche Speicher", "Steuerbare Systeme, die die Tiroler Nachrüstungsförderung erfüllen."),
            ("White-List-Komponenten", "Module, Wechselrichter und Speicher mit Made-in-Europe-Bonus."),
            ("Referenzen in 6 Bundesländern", "300+ Projekte, 4,9 Sterne auf Google."),
        ],
    },

    "faq": [
        ("Wie hoch ist die maximale PV-Förderung in Tirol 2026?",
         "Für eine private 8-kWp-Anlage mit 8-kWh-Speicher im Sanierungskontext sind rund 4.560 € realistisch: "
         "2.400 € EAG-Bund, 1.000 € Wohnhaussanierung Tirol (8 × 125 €/kWp), 800 € Speicher-Nachrüstung "
         "(8 × 100 €/kWh) und 360 € Made-in-Europe-Bonus. Außerhalb des Sanierungskontexts sind es rund 3.000 bis "
         "3.500 € (Richtwerte)."),
        ("Warum wurden die Tiroler Fördersätze 2026 halbiert?",
         "Die Halbierung der Wohnhaussanierungsförderung von 250 auf 125 €/kWp ab 1. Jänner 2026 begründet das Land "
         "Tirol mit den gesunkenen Marktpreisen für PV-Module. Weil Anlagen heute deutlich günstiger sind, wurden die "
         "Fördersätze angepasst. In der Kombination mit dem Bund bleibt Tirol trotzdem attraktiv."),
        ("Kann ich Bundes- und Landesförderung in Tirol kombinieren?",
         "Ja. Die Wohnhaussanierungsförderung lässt sich mit der EAG kombinieren, sofern die beihilferechtlichen "
         "Höchstgrenzen eingehalten werden. Auch die Speicher-Nachrüstungsförderung ist mit dem EAG-Speicherzuschuss "
         "kombinierbar, das ergibt bis zu 250 €/kWh für die ersten 10 kWh. Wichtig ist die Reihenfolge: EAG vor, "
         "Land nach Inbetriebnahme."),
        ("Wird eine PV-Anlage in Tirol auch ohne Sanierung vom Land gefördert?",
         "Nein. Der PV-Zuschuss des Landes gibt es nur als Bestandteil eines genehmigten Sanierungsvorhabens auf einem "
         "bestehenden Wohngebäude. Ohne Sanierung bleiben die EAG-Bundesförderung und, bei netzdienlicher Steuerung, "
         "die Tiroler Speicher-Nachrüstungsförderung mit bis zu 1.000 €."),
        ("Welche Speicher fördert das Land Tirol?",
         "Neu installierte Speicher und Erweiterungen mit steuerbarer Schnittstelle, die netzdienlich betrieben werden "
         "können, bei Installation und Inbetriebnahme ab 1. Jänner 2026. Gefördert werden 100 €/kWh für in der Regel "
         "die ersten 10 kWh, maximal 1.000 €. Der Antrag läuft online über das Landesportal Tirol nach Inbetriebnahme."),
        ("Was sind die Sonderprogramme in Landeck, Lechtal-Reutte und Pitztal?",
         "Drei Tiroler Regionen bieten 2026 zusätzliche Förderprogramme: Landeck und Lechtal-Reutte für Betriebe, "
         "Gemeinden, Energiegemeinschaften und Vereine, Pitztal auch für Privatpersonen. Die Quoten liegen häufig "
         "zwischen 20 und 40 % der förderfähigen Kosten. Die Programme sind zeitlich und budgetär begrenzt, fragen "
         "Sie vor Projektstart bei der Regionalstelle nach."),
        ("Wann sind die EAG-Fördercalls 2026?",
         "Die drei Calls laufen vom 23. April bis 11. Mai, vom 16. bis 30. Juni und ab 8. Oktober 2026. In den "
         "Kategorien A und B gilt First come, first served mit Ticketziehung. Der Antrag muss vor Inbetriebnahme "
         "gestellt werden."),
        ("Wer hilft bei der Förderabwicklung in Tirol?",
         "EBZ Energie aus Villach übernimmt für Projekte in Tirol Beratung, Planung und Förderabwicklung aus einer "
         "Hand: EAG-Antrag im Call, Wohnhaussanierungs- und Speicherförderung des Landes sowie Regionalprogramme. "
         "Mit über 300 Projekten in sechs Bundesländern kennen wir die Unterschiede zwischen Bund und Ländern aus "
         "der Praxis."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant PV-Anlagen, Speicher und "
                    "Wärmepumpen und übernimmt die Förderabwicklung, Referenzen liegen in sechs Bundesländern vor. "
                    "Die Angaben werden anhand der offiziellen Unterlagen von OeMAG und Land Tirol geprüft. Keine "
                    "Rechts- oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("Land Tirol: Wohnhaussanierung, Photovoltaik-Anlagen",
         "https://www.tirol.gv.at/bauen-wohnen/wohnbaufoerderung/sanierung/photovoltaik-anlagen/"),
        ("Land Tirol: Ansuchen zur Förderung von netzdienlichen Stromspeichersystemen",
         "https://www.tirol.gv.at/buergerservice/e-government/formulare/ansuchen-zur-foerderung-von-netzdienlichen-stromspeichersystemen/"),
        ("Land Tirol: Energieförderungen",
         "https://www.tirol.gv.at/umwelt/wasser-forst-und-energierecht/energiefoerderungen/"),
    ],
    "related": [
        ("/photovoltaik-landesfoerderungen/", "Vergleich: PV-Landesförderungen aller 9 Bundesländer"),
        ("/photovoltaik-foerderung-oesterreich-2026/", "Photovoltaik-Förderung Österreich 2026 (EAG)"),
        ("/foerderung-fuer-pv-speicher/", "Förderung für PV-Speicher"),
        ("referenzen", "Referenzanlagen von EBZ Energie"),
    ],
    "cta": {
        "h3": "Förderung in Tirol sichern",
        "text": "Wir kombinieren EAG, Wohnhaussanierung und Speicher-Nachrüstung für Ihr Projekt und halten die Reihenfolge ein.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre PV-Förderung in Tirol, vollständig genutzt",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung und "
                   "Förderabwicklung aus einer Hand übernimmt."),
}
