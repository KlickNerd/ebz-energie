"""Ratgeber: Landesförderungen für die Wärmepumpe 2026 (alle neun Bundesländer).

Migriert vom WordPress-Artikel ebz-photovoltaik.at/landesfoerderungen-fuer-die-waermepumpe/
(veröffentlicht 2026-03-15, zuletzt geändert 2026-04-12). Zahlen: Stand April 2026.
Bereinigt: Gedankenstriche, "ohne Subunternehmer" entfernt, "in ganz Österreich" auf Kärnten +
Steiermark korrigiert, Kärnten-Widerspruch (6.000 € laut Richtlinie vs. 3.000 € laut Berichten)
transparent dargestellt, Länder-Vergleich als Tabelle.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "landesfoerderungen-fuer-die-waermepumpe",
    "path": "/landesfoerderungen-fuer-die-waermepumpe/",
    "title": "Landesförderung Wärmepumpe 2026: alle 9 Bundesländer | EBZ",
    "description": ("Landesförderung Wärmepumpe 2026 im Vergleich: Wien 35 % bis 8.000 €, Tirol bis "
                    "18.000 € gesamt, Kärnten 35 % bis 6.000 €. Alle 9 Bundesländer und Fristen."),
    "eyebrow": "Förderung · Bundesländer",
    "crumb_label": "Landesförderungen Wärmepumpe",
    "h1": "Landesförderungen für die Wärmepumpe 2026: Alle neun Bundesländer im Vergleich, bis zu 18.000 € Gesamtförderung",
    "lead": ("Zur Bundesförderung von bis zu 7.500 € kommt in jedem Bundesland ein eigener Zuschuss: von 1.500 € "
             "in Vorarlberg bis 8.000 € in Wien. Dieser Ratgeber zeigt Förderhöhen, Voraussetzungen und "
             "Antragswege aller neun Länder und wie Sie Bund, Land und Gemeinde kombinieren."),
    "chips": [
        "Wien: <b>35 %</b>, bis 8.000 €",
        "Tirol: <b>bis 18.000 €</b> gesamt",
        "Kärnten: <b>35 %</b>, bis 6.000 €",
        "Bund + Land <b>kombinierbar</b>",
    ],
    "date_published": "2026-03-15",
    "date_modified": "2026-09-24",
    "hero_img": "foerderung",
    "hero_alt": "Beratung zur Landesförderung für Wärmepumpen mit Unterlagen am Tisch",

    "tldr": [
        "Die Bundesförderung (Sanierungsoffensive 2026) zahlt bis zu 7.500 € für eine Wärmepumpe, gedeckelt "
        "bei 30 % der Kosten. Alle neun Bundesländer legen eigene Zuschüsse dazu, die in der Regel "
        "kombinierbar sind.",
        "Die höchsten Gesamtförderungen erreichen Tirol (25 % plus 3.000 € Bonus, bis zu 18.000 €, rund 60 %) "
        "und Wien (35 % bis 8.000 €, mit Bund 15.500 €). Kärnten fördert 35 % bis 6.000 € (laut Berichten "
        "2026 auf 3.000 € angepasst), die Steiermark 35 % der förderbaren Kosten.",
        "Niederösterreich gewährt statt einer Einmalzahlung einen Annuitätenzuschuss von 4 %. Oberösterreich, "
        "Vorarlberg und das Burgenland zahlen Pauschalen zwischen 1.500 € und 2.500 €, teils erst nach Umsetzung.",
        "Zusätzlich gibt es Gemeindeförderungen und Prämien der Energieversorger, etwa 1.200 € "
        "Kelag-Wärmepumpenprämie in Kärnten.",
        "Obergrenze: Die Summe aller Förderungen darf die Investitionskosten nicht übersteigen, in Kärnten "
        "gilt zusätzlich ein Deckel von 85 % der förderfähigen Kosten. Alles wird in der Transparenzdatenbank "
        "erfasst.",
    ],
    "kpis": [
        ("7.500 €", "Bundesförderung als Basis"),
        ("8.000 €", "höchster Landeszuschuss (Wien)"),
        ("18.000 €", "Gesamtförderung Tirol (max.)"),
        ("9", "Bundesländer mit eigenem Programm"),
    ],

    "sections": [
        ("Warum die Landesförderung den Unterschied macht", "warum", f"""
<p>Die {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive 2026')} des Bundes ist das Fundament jedes
Heizungstausches: bis zu 7.500 € für eine {a('waermepumpe', 'Wärmepumpe')}, gedeckelt bei 30 % der
förderfähigen Kosten. Für viele Haushalte reicht das allein nicht, um den Eigenanteil auf ein tragbares
Maß zu senken. Die Bundesländer stocken deshalb mit eigenen Programmen auf, und die Unterschiede sind
erheblich: Manche Länder zahlen Pauschalen von wenigen Tausend Euro, andere prozentuale Zuschüsse, die in
Kombination mit dem Bund zu Gesamtförderquoten von 40 bis über 60 % führen.</p>
<p>Die Kombination von Bund und Land ist in den meisten Fällen ausdrücklich erlaubt. Es gilt aber eine
Obergrenze: Die Summe aller Förderungen darf die tatsächlichen Investitionskosten nicht übersteigen.
Alle Förderungen werden in der Transparenzdatenbank erfasst, unzulässige Mehrfachförderungen werden
zurückgefordert. Stand aller Angaben: April 2026.</p>
"""),
        ("Alle neun Bundesländer im Überblick", "vergleich", f"""
{A.table(
    ["Bundesland", "Landesförderung Wärmepumpe", "Besonderheit", "Antrag"],
    [
        ["Kärnten", "35 %, max. 6.000 € (laut Berichten 2026: 3.000 €)", "+1.500 € Solarthermie-Bonus, +1.200 € Kelag-Prämie, Deckel 85 %", "Förderportal Land Kärnten"],
        ["Steiermark", "35 % der förderbaren Kosten", "Eigenheime mit max. 2 Wohnungen, Energieberatung kostenlos", "Land Steiermark, A15"],
        ["Wien", "35 %, max. 8.000 €", "auch für Mieter, mit Bund 15.500 €", "Stadt Wien, MA 50"],
        ["Niederösterreich", "Annuitätenzuschuss 4 %", "für Bankdarlehen; Sauber Heizen bis 25.383 € / 37.252 €", "Abteilung Wohnungsförderung"],
        ["Oberösterreich", "100 € je kW, max. 1.700 €", "max. 50 % der Nettokosten, PV ab 3 kWp oder Ökostrom Pflicht", "online nach Umsetzung"],
        ["Salzburg", "rund 5.000 €", "Bestand und Neubau, mit Bund ca. 12.500 €", "Abteilung 4, Referat 4/04"],
        ["Tirol", "25 % + 3.000 € Bonus", "bis zu 18.000 € gesamt, rund 60 %", "Landesförderstellen oder online"],
        ["Vorarlberg", "1.000 € + 500 € Fossil-Bonus", "max. 25 % der Kosten, Hauptwohnsitz", "Energieinstitut, bis 6 Monate nach Inbetriebnahme"],
        ["Burgenland", "2.000 € + 500 € Sozialzuschlag", "Sozialzuschlag bis 43.000 € Jahreseinkommen, max. 30 %", "per E-Mail oder Post nach Inbetriebnahme"],
    ],
    hl_cols=(1,),
)}
<p><small>Alle Beträge Stand April 2026, Änderungen im Jahresverlauf möglich. Maßgeblich sind die
Landesförderungsstellen; eine laufend aktualisierte Übersicht führt der Verband Wärmepumpe Austria.</small></p>
"""),
        ("Kärnten: bis zu 13.500 € Gesamtförderung", "kaernten", f"""
<p>Kärnten ist eine der Kernregionen von EBZ Energie. Die Landesförderung für den Heizungstausch wird als
Einmalzuschuss in Form einer Anschlussförderung an die Bundesförderung vergeben:</p>
<ul>
  <li><b>Landesförderung Heizungstausch:</b> 35 % der förderfähigen Kosten, maximal 6.000 €. Laut
  Berichten wurde die Obergrenze 2026 auf 3.000 € angepasst; den aktuellen Stand bestätigt das Land Kärnten.</li>
  <li><b>Solarthermie-Bonus:</b> zusätzlich 1.500 € bei gleichzeitigem Einbau einer thermischen Solaranlage
  ab 6 m² Kollektorfläche.</li>
  <li><b>Kelag-Wärmepumpenprämie:</b> Kelag-Kunden erhalten zusätzlich 1.200 €.</li>
</ul>
<p>Voraussetzung ist der Austausch einer fossilen Heizung gegen ein erneuerbares System, das die
technischen Förderkriterien des Landes erfüllt. Die Gesamtförderung aus Bund, Land und weiteren
Zuschüssen ist mit 85 % der förderfähigen Kosten gedeckelt; darüber wird die Landesförderung gekürzt.</p>
<p><b>Rechenbeispiel:</b>* Bei Projektkosten von 30.000 € für eine Luft-Wasser-Wärmepumpe ergeben
7.500 € Bund plus bis zu 6.000 € Land eine Gesamtförderung von bis zu 13.500 € (rund 45 %). Mit der
berichteten Obergrenze von 3.000 € wären es 10.500 € (35 %).</p>
<p>Antrag: über das Förderportal des Landes Kärnten, die Bundesförderung separat auf
sanierungsoffensive.gv.at. Kontakt: Land Kärnten, Abteilung für Umwelt und Energie. Für Photovoltaik
gilt ein eigenes Programm, siehe {a('foerderung_kaernten', 'Photovoltaik-Förderung Kärnten')}.</p>
"""),
        ("Steiermark: 35 % Einmalzuschuss", "steiermark", f"""
<p>Die Steiermark, zweite Kernregion von EBZ Energie, gewährt einen Einmalzuschuss von 35 % der
förderbaren Kosten für Eigenheime mit maximal zwei Wohnungen (Ein- und Zweifamilienhäuser,
Reihenhäuser). Die maximale Förderhöhe kann sich im Lauf des Jahres ändern und ist beim Land zu
erfragen.</p>
<p>Gefördert wird der Austausch eines fossilen Heizsystems durch eine Wärmepumpe oder ein anderes
erneuerbares System. Die technischen Mindestanforderungen entsprechen im Wesentlichen den
Bundeskriterien: EHPA-Gütesiegel, GWP höchstens 750, maximale Vorlauftemperatur 55 °C. Die Kombination
mit der Bundesförderung ist möglich, die Energieberatung bietet das Land kostenlos an.</p>
<p>Kontakt: Amt der Steiermärkischen Landesregierung, A15 Energie, Wohnbau, Technik, Referat
Energietechnik und Umweltförderungen, Tel. 0316/877-3955. Für PV siehe
{a('foerderung_steiermark', 'Photovoltaik-Förderung Steiermark')}.</p>
{A.cta("Förderung in Kärnten oder der Steiermark durchrechnen lassen",
       "EBZ Energie kennt die Landesprogramme, die Gemeindezuschüsse und die Kelag-Prämie im Detail und "
       "berechnet für Ihr Projekt die höchste Gesamtförderung.",
       secondary=("waermepumpe", "Zur Wärmepumpen-Leistungsseite"))}
"""),
        ("Wien, Niederösterreich, Oberösterreich, Salzburg", "ost-mitte", f"""
<h3>Wien: bis zu 15.500 € Gesamtförderung</h3>
<p>Die Stadt Wien fördert 35 % der förderbaren Gesamtkosten, maximal 8.000 €, für Errichtung,
Umstellung oder Nachrüstung von Heizsystemen. Antragsberechtigt sind Eigentümer ebenso wie Mieter von
Wohnungen und Eigenheimen. Das alte System muss vollständig demontiert werden, das neue als alleinige
Heizung dienen. Rechenbeispiel:* 28.000 € Projektkosten, 7.500 € Bund plus 8.000 € Land ergeben 15.500 €
(rund 55 %). Antrag bei der MA 50, Tel. 01/4000 74 860.</p>
<h3>Niederösterreich: Annuitätenzuschuss statt Einmalzahlung</h3>
<p>Niederösterreich unterstützt den Heizungstausch über die „Förderung Eigenheimsanierung“ mit einem
Annuitätenzuschuss von 4 %, gedacht für Hausbesitzer, die ein Bankdarlehen aufnehmen. Voraussetzung:
natürliche Personen mit Hauptwohnsitz, die Eigentümer des Gebäudes sind. Für einkommensschwache
Haushalte reichen die Fördersummen über
{a('/sauber-heizen-fuer-alle-2026/', '„Sauber Heizen für Alle“')} in Niederösterreich bis 25.383 €
(Luft-Wasser) bzw. 37.252 € (Sole-Wasser). Kontakt: Abteilung Wohnungsförderung, Tel. 02742/22 133.</p>
<h3>Oberösterreich: Förderung nach Leistung</h3>
<p>Oberösterreich zahlt für Luft-Wasser-Wärmepumpen 100 € je kW Nennwärmeleistung, maximal 1.700 €,
begrenzt auf 50 % der förderfähigen Nettokosten. Das Gebäude muss ganzjährig bewohnt sein
(Hauptwohnsitz), Zweitwohnsitze sind ausgeschlossen, die Vorlauftemperatur maximal 55 °C. Zusätzlich
muss die Wärmepumpe mit einer PV-Anlage (mindestens 3 kWp) oder Solaranlage (mindestens 6 m²)
kombiniert werden, oder der Haushalt bezieht 10 Jahre lang Strom aus 100 % erneuerbaren Quellen. Der
Antrag erfolgt online nach dem Heizungstausch. Kontakt: Direktion Umwelt und Wasserwirtschaft,
Tel. 0732/7720-13483.</p>
<h3>Salzburg: rund 5.000 € Landesförderung</h3>
<p>Salzburg fördert den Umstieg auf erneuerbare Heizsysteme mit rund 5.000 €, im Bestand ebenso wie im
Neubau. Mit dem Bund ergibt das rund 12.500 €. Ergänzende Gemeindeförderungen sind in manchen Salzburger
Gemeinden möglich. Kontakt: Abteilung 4 Lebensgrundlagen und Energie, Referat 4/04, Tel. 0662 8042 3791.</p>
"""),
        ("Tirol, Vorarlberg, Burgenland", "west-sued", f"""
<h3>Tirol: Spitzenreiter mit rund 60 % Förderquote</h3>
<p>Tirol gewährt neben der Bundesförderung einen Einmalzuschuss von 25 % der förderfähigen Kosten plus
einen Bonus von 3.000 € für den Tausch einer fossilen Heizung. In Summe sind Gesamtförderungen von bis
zu 18.000 € möglich, das entspricht rund 60 %. Gefördert werden alle gängigen Wärmepumpenarten für
Bestandsgebäude, die technischen Anforderungen entsprechen den Bundeskriterien. Anträge laufen über
die Tiroler Landesförderstellen oder online.</p>
<h3>Vorarlberg: Basisförderung plus Bonus</h3>
<p>Vorarlberg zahlt 1.000 € Basisförderung für den Einbau einer Wärmepumpe plus 500 € beim Ersatz eines
fossilen Heizsystems, begrenzt auf 25 % der förderfähigen Kosten. Das Gebäude muss ganzjährig bewohnt
sein, maximal zwei Wohnungen umfassen und baurechtlich bewilligt sein. Ein wirtschaftlich zumutbarer
Nahwärmeanschluss darf nicht verfügbar sein (Prüfung über den Heizrechner des Energieinstituts
Vorarlberg). Der Antrag wird nach der Inbetriebnahme gestellt, spätestens 6 Monate danach.</p>
<h3>Burgenland: Pauschale plus Sozialzuschlag</h3>
<p>Das Burgenland zahlt 2.000 € für den Austausch eines fossilen Heizsystems plus 500 € Sozialzuschlag,
wenn das Netto-Jahreshaushaltseinkommen 43.000 € nicht überschreitet. Die Förderung ist mit 30 % der
anrechenbaren Kosten begrenzt. Antrag nach Inbetriebnahme per E-Mail (post.a9-energie@bgld.gv.at) oder
per Post an das Amt der Burgenländischen Landesregierung; Kontakt: Wohnbauförderung Burgenland bzw. BOEF,
Tel. 02682/600-2800.</p>
"""),
        ("Gemeinden und Energieversorger: die oft vergessenen Töpfe", "gemeinden", f"""
<p>Viele der über 2.100 österreichischen Gemeinden zahlen eigene Zuschüsse für den Heizungstausch, teils
auch für die Kombination mit Photovoltaik. Es gibt keine zentrale Übersicht, Höhe und Verfahren
unterscheiden sich von Gemeinde zu Gemeinde. Der sicherste Weg ist die direkte Anfrage beim Gemeindeamt,
oder Sie lassen EBZ Energie die Recherche für Kärnten und die Steiermark übernehmen.</p>
<p>Dazu kommen Prämien der Energieversorger: Kelag (Kärnten), Energie AG und andere zahlen für den
Einbau von Wärmepumpen typischerweise einige Hundert bis über Tausend Euro, ebenfalls kombinierbar mit
den öffentlichen Förderungen.</p>
"""),
        ("So kombinieren Sie Bund, Land und Gemeinde richtig", "kombination", f"""
{A.steps([
    ("Bundesförderung registrieren",
     "Auf sanierungsoffensive.gv.at, vor dem ersten Auftrag. Das reserviert das Bundesbudget für 9 Monate."),
    ("Landesförderung beantragen",
     "In der Regel separat beim Land. In Oberösterreich, Vorarlberg und dem Burgenland erst nach dem "
     "Heizungstausch, in anderen Ländern vor Beginn der Maßnahme. Fristen beachten."),
    ("Gemeinde und Energieversorger anfragen",
     "Zuschüsse der Gemeinde und Prämien wie die Kelag-Wärmepumpenprämie ergänzen die öffentlichen Mittel."),
    ("Obergrenze prüfen",
     "Die Summe aus Bund, Land, Gemeinde und Prämien darf die Investitionskosten nicht übersteigen; in "
     "Kärnten gilt zusätzlich ein Deckel von 85 % der förderfähigen Kosten."),
])}
{A.box("Nach Abzug aller Förderungen bringt die Öko-Sonderausgabenpauschale zusätzlich fünf Jahre lang "
       "je 400 € Sonderausgaben, sofern mehr als 2.000 € Restkosten bleiben. Details im Ratgeber "
       + a('/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/', 'Wärmepumpe steuerlich absetzen')
       + ".", label="Steuerbonus:")}
<p><small>*Rechenbeispiele mit den Obergrenzen laut Landesrichtlinien, Stand April 2026. Die tatsächliche
Förderung hängt von Projektkosten, Anlagentyp und den aktuellen Bedingungen der Landesstelle ab.</small></p>
{A.cta("Höchste Gesamtförderung für Ihr Projekt",
       "Wir kombinieren Bund, Land, Gemeinde und Energieversorger-Prämie und reichen alle Anträge "
       "fristgerecht ein.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Ihr regionaler Partner in Kärnten und der Steiermark: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Wärmepumpen und Photovoltaik in Kärnten und "
                 "der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. Wir kennen "
                 "die Landesprogramme, die Gemeinden mit eigenen Zuschüssen und die Prämien der Energieversorger "
                 "und berechnen für Ihr Projekt die Kombination mit der höchsten Gesamtförderung."),
        "grid": [
            ("Individuelle Förderberatung", "Bund, Land, Gemeinde, Prämie und Steuerbonus in einer Rechnung."),
            ("Komplette Förderabwicklung", "Registrierung beim Bund, Landesantrag, Einreichung bei der Gemeinde."),
            ("Installation aus einer Hand", "Wärmepumpe und auf Wunsch PV vom selben Team."),
            ("Regionale Nähe", "Wir kennen die Anforderungen der Länder Kärnten und Steiermark."),
        ],
    },

    "faq": [
        ("Kann ich die Landesförderung auch ohne Bundesförderung beantragen?",
         "In den meisten Bundesländern setzt die Landesförderung den gleichzeitigen Bezug der Bundesförderung "
         "voraus, sie wird als Anschlussförderung vergeben. Ausnahmen gibt es bei Landesförderungen für "
         "Neubauten oder den Tausch nicht-fossiler Heizsysteme, etwa in Salzburg. Prüfen Sie die Bedingungen "
         "Ihres Bundeslandes."),
        ("Welches Bundesland bietet die höchste Förderung?",
         "Tirol mit rund 60 % Förderquote bzw. Gesamtförderungen bis zu 18.000 € (25 % Landeszuschuss plus "
         "3.000 € Bonus plus Bund). Wien folgt mit bis zu 8.000 € Landesförderung, mit dem Bund 15.500 €. "
         "Kärnten und Salzburg liegen im Mittelfeld."),
        ("Muss ich die Landesförderung vor oder nach dem Heizungstausch beantragen?",
         "Das hängt vom Bundesland ab. In Oberösterreich, Vorarlberg (spätestens 6 Monate nach Inbetriebnahme) "
         "und dem Burgenland wird nach dem Heizungstausch beantragt, in anderen Ländern ist eine Registrierung "
         "vor Beginn nötig. Die Bundesförderung muss immer vor dem Auftrag registriert werden."),
        ("Gibt es Landesförderungen auch für Neubauten?",
         "In einigen Bundesländern wie Salzburg werden auch Neubauten mit erneuerbaren Heizsystemen gefördert. "
         "In den meisten Ländern und bei der Bundesförderung liegt der Fokus auf dem Austausch fossiler "
         "Heizungen im Bestand."),
        ("Werden auch Erdwärme-Wärmepumpen von den Ländern unterstützt?",
         "Ja, alle Bundesländer fördern grundsätzlich Luft-Wasser, Sole-Wasser und Wasser-Wasser. Auf "
         "Bundesebene kommt bei Erdwärme der Bohrbonus von 5.000 € dazu, in Kärnten zusätzlich 1.500 € "
         "Solarthermie-Bonus bei Kombination mit einer Solaranlage."),
        ("Wie hoch ist die Landesförderung in Kärnten 2026?",
         "Laut Landesrichtlinie 35 % der förderfähigen Kosten, maximal 6.000 €, plus 1.500 € Solarthermie-Bonus "
         "und 1.200 € Kelag-Prämie. Laut Berichten wurde die Obergrenze 2026 auf 3.000 € angepasst; den "
         "aktuellen Stand bestätigt das Land Kärnten. Die Gesamtförderung ist mit 85 % der Kosten gedeckelt."),
        ("Darf die Gesamtförderung die Kosten übersteigen?",
         "Nein. Die Summe aus Bund, Land, Gemeinde und Energieversorger-Prämien darf die tatsächlichen "
         "Investitionskosten nicht übersteigen. Alle Förderungen werden in der Transparenzdatenbank erfasst, "
         "unzulässige Mehrfachförderungen werden zurückgefordert."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Wärmepumpen in Kärnten und der Steiermark und übernimmt Bundes-, Landes- und "
                    "Gemeindeanträge. Alle Beträge entsprechen dem Stand April 2026; Förderhöhen können sich "
                    "im Jahresverlauf ändern. Keine Rechts- oder Steuerberatung, maßgeblich sind die "
                    "offiziellen Förderbedingungen der Landesförderungsstellen."),
    "sources": [
        ("Sanierungsoffensive 2026 (Bundesportal)", "https://www.sanierungsoffensive.gv.at/"),
        ("Verband Wärmepumpe Austria: Förderübersicht aller Bundesländer",
         "https://www.waermepumpe-austria.at/foerderungen"),
    ],
    "related": [
        ("/waermepumpenfoerderung-in-oesterreich/", "Wärmepumpenförderung Österreich 2026: Überblick"),
        ("/sanierungsoffensive-2026/", "Sanierungsoffensive 2026: Bundesförderung"),
        ("foerderung_kaernten", "Photovoltaik-Förderung Kärnten"),
        ("waermepumpe", "Wärmepumpen-Installateur EBZ Energie"),
    ],
    "cta": {
        "h3": "Bund + Land + Gemeinde",
        "text": "Wir berechnen die höchste Gesamtförderung für Ihr Projekt in Kärnten oder der Steiermark.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Alle Fördertöpfe für Ihre Wärmepumpe",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
