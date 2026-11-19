"""Ratgeber: Landesförderungen für die Wärmepumpe 2026 (alle neun Bundesländer).

Migriert vom WordPress-Artikel ebz-photovoltaik.at/landesfoerderungen-fuer-die-waermepumpe/
(veröffentlicht 2026-03-15, zuletzt geändert 2026-04-12). Zahlen: Stand April 2026.
Bereinigt: Gedankenstriche, "ohne Subunternehmer" entfernt, "in ganz Österreich" auf Kärnten +
Steiermark korrigiert, Länder-Vergleich als Tabelle.
Korrektur 10.10.2026 (build/seo/_fakten_2026-10.md): Kärnten 2026 = 3.000 € Pauschale (35 %/6.000 € galt nur
bis 31.12.2025); Steiermark nimmt für neue Wärmepumpen keine Anträge an (wohnbau.steiermark.at).
Update 19.11.2026: Bund-Kesseltausch seit 2.11.2026 neu aufgelegt (5.000 € Wärmepumpe); Rechenbeispiele
Bund plus Land mit 5.000 € neu gerechnet, 7.500 € nur noch als Historie.
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
    "description": ("Landesförderung Wärmepumpe 2026: Kärnten 3.000 € Pauschale, Steiermark derzeit keine "
                    "Anträge, Wien 35 % bis 8.000 €. Plus 5.000 € vom Bund. Alle 9 Länder."),
    "eyebrow": "Förderung · Bundesländer",
    "crumb_label": "Landesförderungen Wärmepumpe",
    "h1": "Landesförderungen für die Wärmepumpe 2026: Alle neun Bundesländer im Vergleich, kombinierbar mit 5.000 € vom Bund",
    "lead": ("Fast jedes Bundesland hat einen eigenen Zuschuss für den Heizungstausch: von 1.500 € in Vorarlberg bis "
             "8.000 € in Wien. Kärnten zahlt 2026 eine Pauschale von 3.000 €, die Steiermark nimmt für neue "
             "Wärmepumpen derzeit keine Förderanträge an. Dazu kommt seit 2. November 2026 wieder der Kesseltausch "
             "des Bundes mit 5.000 € für die Wärmepumpe (in der ersten Aktion 2026 bis zu 7.500 €). Dieser Ratgeber "
             "zeigt Förderhöhen, Voraussetzungen und Antragswege aller neun Länder und wie Sie Bund und Land "
             "kombinieren."),
    "chips": [
        "Wien: <b>35 %</b>, bis 8.000 €",
        "Bund: <b>5.000 €</b> seit 2.11.2026",
        "Kärnten: <b>3.000 €</b> Pauschale",
        "Bund + Land <b>kombinierbar</b>",
    ],
    "date_published": "2026-03-15",
    "date_modified": "2026-11-19",
    "hero_img": "foerderung",
    "hero_alt": "Beratung zur Landesförderung für Wärmepumpen mit Unterlagen am Tisch",

    "tldr": [
        "Stand November 2026: Der Kesseltausch des Bundes läuft seit 2. November 2026 wieder (5.000 € für die "
        "Wärmepumpe, Registrierung bis 31. Dezember 2026 oder bis das Budget aufgebraucht ist). Die meisten "
        "Bundesländer stocken mit eigenen Zuschüssen auf; mehrere vergeben sie als Anschlussförderung an den Bund.",
        "Die höchsten Gesamtförderungen erreichen Tirol (25 % plus 3.000 € Bonus; mit 5.000 € Bund bei 30.000 € "
        "Kosten 15.500 €*, rund 52 %) und Wien (35 % bis 8.000 €, mit Bund 13.000 €*). Kärnten zahlt 2026 eine "
        "Pauschale von 3.000 € (plus 1.500 € bei Errichtung einer Solaranlage, plus 200 € für den hydraulischen "
        "Abgleich), mit dem Bund zusammen bis 8.000 €*. Die Steiermark nimmt für neue Wärmepumpen derzeit keine "
        "Förderanträge an (Stand 10. Oktober 2026).",
        "Niederösterreich gewährt statt einer Einmalzahlung einen Annuitätenzuschuss von 4 %. Oberösterreich, "
        "Vorarlberg und das Burgenland zahlen Pauschalen zwischen 1.500 € und 2.500 €, teils erst nach Umsetzung.",
        "Zusätzlich gibt es Gemeindeförderungen und Prämien der Energieversorger, etwa 1.200 € "
        "Kelag-Wärmepumpenprämie in Kärnten.",
        "Obergrenze: Die Summe aller Förderungen darf die Investitionskosten nicht übersteigen. Alles wird in "
        "der Transparenzdatenbank erfasst.",
    ],
    "kpis": [
        ("5.000 €", "Bundespauschale Wärmepumpe seit 2. November 2026"),
        ("8.000 €", "höchster Landeszuschuss (Wien)"),
        ("15.500 €", "Tirol mit Bund bei 30.000 € Kosten*"),
        ("3.000 €", "Landespauschale Kärnten 2026"),
    ],

    "sections": [
        ("Warum die Landesförderung den Unterschied macht", "warum", f"""
{A.box("Stand November 2026: Der Kesseltausch der Sanierungsoffensive ist seit 2. November 2026 neu "
       "aufgelegt: 5.000 € Pauschale für die Wärmepumpe, Registrierung bis 31. Dezember 2026 oder bis das Budget "
       "aufgebraucht ist (Informationsblatt der KPC, Version 10/2026). Damit ist die Kombination Bund plus Land "
       "auch für neue Projekte wieder möglich, etwa in Kärnten, das seine Förderung bisher als "
       "Anschlussförderung an den Bund vergab. Die Steiermark nimmt für neue Wärmepumpen derzeit keine "
       "Förderanträge an.", label="Wichtig:")}
<p>Die {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive 2026')} des Bundes ist das Fundament jedes
Heizungstausches: Seit der Neuauflage zahlt der Kesseltausch 5.000 € für eine
{a('waermepumpe', 'Wärmepumpe')} (in der ersten Aktion 2026 bis zu 7.500 €, gedeckelt bei 30 % der
förderfähigen Kosten). Für viele Haushalte reicht das allein nicht, um den Eigenanteil auf ein tragbares
Maß zu senken. Die Bundesländer stocken deshalb mit eigenen Programmen auf, und die Unterschiede sind
erheblich: Manche Länder zahlen Pauschalen von wenigen Tausend Euro, andere prozentuale Zuschüsse, die
zusammen mit dem Bund in Tirol rund die Hälfte der Kosten abdecken können.</p>
<p>Die Kombination von Bund und Land ist in den meisten Fällen ausdrücklich erlaubt. Es gilt aber eine
Obergrenze: Die Summe aller Förderungen darf die tatsächlichen Investitionskosten nicht übersteigen.
Alle Förderungen werden in der Transparenzdatenbank erfasst, unzulässige Mehrfachförderungen werden
zurückgefordert. Stand der Angaben: Kärnten und Steiermark Oktober 2026, übrige Länder April 2026.</p>
"""),
        ("Alle neun Bundesländer im Überblick", "vergleich", f"""
{A.table(
    ["Bundesland", "Landesförderung Wärmepumpe", "Besonderheit", "Antrag"],
    [
        ["Kärnten", "3.000 € Pauschale (2026)", "+1.500 € bei Errichtung einer Solaranlage, +200 € hydraulischer Abgleich, +1.200 € Kelag-Prämie", "Förderportal Land Kärnten"],
        ["Steiermark", "derzeit keine Anträge für neue Wärmepumpen", "nur Tausch mind. 15 Jahre alter Biomassekessel oder Wärmepumpen: höchstens 30 %, höchstens 1.500 €, nur ohne Fernwärme-Anschlussmöglichkeit", "Land Steiermark, A15"],
        ["Wien", "35 %, max. 8.000 €", "auch für Mieter, mit Bund 13.000 €*", "Stadt Wien, MA 50"],
        ["Niederösterreich", "Annuitätenzuschuss 4 %", "für Bankdarlehen; Sauber Heizen 2026 (geschlossen) bis 25.383 € / 37.252 €", "Abteilung Wohnungsförderung"],
        ["Oberösterreich", "100 € je kW, max. 1.700 €", "max. 50 % der Nettokosten, PV ab 3 kWp oder Ökostrom Pflicht", "online nach Umsetzung"],
        ["Salzburg", "rund 5.000 €", "Bestand und Neubau, mit Bund ca. 10.000 €", "Abteilung 4, Referat 4/04"],
        ["Tirol", "25 % + 3.000 € Bonus", "mit Bund 15.500 € bei 30.000 € Kosten*, rund 52 %", "Landesförderstellen oder online"],
        ["Vorarlberg", "1.000 € + 500 € Fossil-Bonus", "max. 25 % der Kosten, Hauptwohnsitz", "Energieinstitut, bis 6 Monate nach Inbetriebnahme"],
        ["Burgenland", "2.000 € + 500 € Sozialzuschlag", "Sozialzuschlag bis 43.000 € Jahreseinkommen, max. 30 %", "per E-Mail oder Post nach Inbetriebnahme"],
    ],
    hl_cols=(1,),
)}
<p><small>Kärnten und Steiermark Stand Oktober 2026, übrige Länder Stand April 2026, Änderungen im Jahresverlauf möglich. Maßgeblich sind die
Landesförderungsstellen; eine laufend aktualisierte Übersicht führt der Verband Wärmepumpe Austria.</small></p>
"""),
        ("Kärnten: 3.000 € Pauschale vom Land", "kaernten", f"""
<p>Kärnten ist eine der Kernregionen von EBZ Energie. 2026 fördert das Land den Heizungstausch über die
„Landesförderung energieeffiziente Haustechnikanlagen“ mit einer Pauschale. Sie gilt für Wärmepumpe,
Nah- oder Fernwärme und Holzzentralheizung in Eigenheimen und Wohnungen:</p>
<ul>
  <li><b>Landesförderung Wärmepumpe:</b> 3.000 € Pauschale. Die frühere Regel (35 % der förderfähigen
  Kosten, höchstens 6.000 €) galt nur bis 31. Dezember 2025.</li>
  <li><b>Solaranlage:</b> zusätzlich 1.500 € bei Errichtung einer Solaranlage.</li>
  <li><b>Hydraulischer Abgleich:</b> zusätzlich 200 €.</li>
  <li><b>Kelag-Wärmepumpenprämie:</b> Kelag-Stromkunden erhalten zusätzlich 1.200 € als Gutschrift über
  zwei Jahre.</li>
</ul>
<p>Voraussetzung ist ein erneuerbares Heizsystem, das die technischen Förderkriterien des Landes erfüllt.
Ob das Budget reicht, klären wir vor dem Angebot.</p>
<p><b>Rechenbeispiel:</b>* Bei Projektkosten von 30.000 € für eine Luft-Wasser-Wärmepumpe zahlt das Land
3.000 € Pauschale (10 %), mit Solaranlage und hydraulischem Abgleich bis zu 4.700 €. Kelag-Stromkunden
erhalten zusätzlich 1.200 € Prämie. Mit dem Kesseltausch des Bundes (Neuauflage seit 2. November 2026)
kommen 5.000 € dazu: zusammen 8.000 € (rund 27 %), mit Solaranlage und hydraulischem Abgleich bis zu
9.700 €. In der ersten Aktion 2026 waren es 7.500 € Bund plus 3.000 € Land.</p>
<p>Antrag: über das Förderportal des Landes Kärnten; die Bundesförderung wird separat auf
sanierungsoffensive.gv.at registriert (Neuauflage seit 2. November 2026, längstens bis 31. Dezember 2026).
Kärnten vergab die Landesförderung bisher als Anschlussförderung an den Bund; mit der Neuauflage ist diese
Kombination wieder möglich, den aktuellen Stand klären wir vor dem Angebot mit dem Land. Kontakt: Land Kärnten, Abteilung für Umwelt und Energie. Für Photovoltaik
gilt ein eigenes Programm, siehe {a('foerderung_kaernten', 'Photovoltaik-Förderung Kärnten')}.</p>
"""),
        ("Steiermark: derzeit keine Förderung für neue Wärmepumpen", "steiermark", f"""
<p>Die Steiermark, zweite Kernregion von EBZ Energie, nimmt für neue Wärmepumpen derzeit keine
Förderanträge an. Laut Land ist eine Antragstellung oder Registrierung für geförderte Biomasse-Heizungen,
Wärmepumpen und solarthermische Anlagen nicht möglich, es besteht „auf absehbare Zeit keine
Förderungsmöglichkeit“ (wohnbau.steiermark.at, Stand 10. Oktober 2026). Bereits eingereichte Anträge werden
weiter bearbeitet.</p>
<p>Die einzige Richtlinie 2026 betrifft den Tausch erneuerbar betriebener Heizungssysteme: Gefördert wird
der Ersatz mindestens 15 Jahre alter Biomassekessel oder Wärmepumpen mit höchstens 30 %, höchstens
1.500 €, und nur, wenn kein Fernwärme-Anschluss möglich ist. Für den Umstieg von Öl oder Gas auf eine
Wärmepumpe gibt es vom Land Steiermark damit derzeit keinen Zuschuss; manche Gemeinden zahlen einen eigenen
Zuschuss. Vom Bund gibt es über den Kesseltausch seit 2. November 2026 wieder 5.000 € für die Wärmepumpe.</p>
<p>Kontakt: Amt der Steiermärkischen Landesregierung, A15 Energie, Wohnbau, Technik, Referat
Energietechnik und Umweltförderungen, Tel. 0316/877-3955. Für PV siehe
{a('foerderung_steiermark', 'Photovoltaik-Förderung Steiermark')}.</p>
{A.cta("Förderung in Kärnten oder der Steiermark durchrechnen lassen",
       "EBZ Energie kennt die Landesprogramme, die Gemeindezuschüsse und die Kelag-Prämie im Detail und "
       "prüft für Ihr Projekt, welche Förderung aktuell offen ist.",
       secondary=("waermepumpe", "Zur Wärmepumpen-Leistungsseite"))}
"""),
        ("Wien, Niederösterreich, Oberösterreich, Salzburg", "ost-mitte", f"""
<h3>Wien: 8.000 € vom Land, mit dem Bund 13.000 €</h3>
<p>Die Stadt Wien fördert 35 % der förderbaren Gesamtkosten, maximal 8.000 €, für Errichtung,
Umstellung oder Nachrüstung von Heizsystemen. Antragsberechtigt sind Eigentümer ebenso wie Mieter von
Wohnungen und Eigenheimen. Das alte System muss vollständig demontiert werden, das neue als alleinige
Heizung dienen. Rechenbeispiel:* 28.000 € Projektkosten, 5.000 € Bund plus 8.000 € Land ergeben 13.000 €
(rund 46 %). Antrag bei der MA 50, Tel. 01/4000 74 860.</p>
<h3>Niederösterreich: Annuitätenzuschuss statt Einmalzahlung</h3>
<p>Niederösterreich unterstützt den Heizungstausch über die „Förderung Eigenheimsanierung“ mit einem
Annuitätenzuschuss von 4 %, gedacht für Hausbesitzer, die ein Bankdarlehen aufnehmen. Voraussetzung:
natürliche Personen mit Hauptwohnsitz, die Eigentümer des Gebäudes sind. Für einkommensschwache
Haushalte reichten die Fördersummen über
{a('/sauber-heizen-fuer-alle-2026/', '„Sauber Heizen für Alle“')} in Niederösterreich 2026 bis 25.383 €
(Luft-Wasser) bzw. 37.252 € (Sole-Wasser); das Programm ist seit Herbst 2026 geschlossen. Kontakt: Abteilung Wohnungsförderung, Tel. 02742/22 133.</p>
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
Neubau. Mit dem Bund (5.000 € seit der Neuauflage) ergibt das rund 10.000 €. Ergänzende Gemeindeförderungen sind in manchen Salzburger
Gemeinden möglich. Kontakt: Abteilung 4 Lebensgrundlagen und Energie, Referat 4/04, Tel. 0662 8042 3791.</p>
"""),
        ("Tirol, Vorarlberg, Burgenland", "west-sued", f"""
<h3>Tirol: Spitzenreiter mit rund der Hälfte der Kosten</h3>
<p>Tirol gewährt neben der Bundesförderung einen Einmalzuschuss von 25 % der förderfähigen Kosten plus
einen Bonus von 3.000 € für den Tausch einer fossilen Heizung. Rechenbeispiel:* Bei 30.000 € Projektkosten
ergeben 7.500 € Landeszuschuss, 3.000 € Bonus und 5.000 € Bund zusammen 15.500 €, rund 52 % (mit der
früheren Bundesförderung von 7.500 € waren bis zu 18.000 € möglich). Gefördert werden alle gängigen Wärmepumpenarten für
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
     "Nach der Energieberatung auf sanierungsoffensive.gv.at registrieren, das reserviert das Bundesbudget für "
     "9 Monate. Möglich seit 2. November 2026, längstens bis 31. Dezember 2026 oder bis das Budget aufgebraucht "
     "ist. Gefördert werden Leistungen ab 7. Oktober 2026."),
    ("Landesförderung beantragen",
     "In der Regel separat beim Land. In Oberösterreich, Vorarlberg und dem Burgenland erst nach dem "
     "Heizungstausch, in anderen Ländern vor Beginn der Maßnahme. Fristen beachten."),
    ("Gemeinde und Energieversorger anfragen",
     "Zuschüsse der Gemeinde und Prämien wie die Kelag-Wärmepumpenprämie ergänzen die öffentlichen Mittel."),
    ("Obergrenze prüfen",
     "Die Summe aus Bund, Land, Gemeinde und Prämien darf die Investitionskosten nicht übersteigen."),
])}
{A.box("Nach Abzug aller Förderungen bringt die Öko-Sonderausgabenpauschale zusätzlich fünf Jahre lang "
       "je 400 € Sonderausgaben, sofern mehr als 2.000 € Restkosten bleiben. Details im Ratgeber "
       + a('/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/', 'Wärmepumpe steuerlich absetzen')
       + ".", label="Steuerbonus:")}
<p><small>*Rechenbeispiele mit den Beträgen laut Landesrichtlinien, Kärnten Stand Oktober 2026, übrige
Länder Stand April 2026; Bund: 5.000 € Pauschale für die Wärmepumpe laut Informationsblatt der KPC (Version
10/2026). Die tatsächliche
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
                 "der Steiermark, mit zertifizierten Fachkräften. Wir kennen "
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
         "In den meisten Bundesländern setzte die Landesförderung bisher den gleichzeitigen Bezug der "
         "Bundesförderung voraus, sie wird als Anschlussförderung vergeben. Seit 2. November 2026 läuft der "
         "Kesseltausch des Bundes wieder, die Kombination ist damit erneut möglich. Wer die Bundesförderung nicht "
         "nutzt, klärt mit der Landesstelle, ob die Landesförderung allein gewährt wird. Ausnahmen gab es bisher bei Landesförderungen für Neubauten oder "
         "den Tausch nicht-fossiler Heizsysteme, etwa in Salzburg."),
        ("Welches Bundesland bietet die höchste Förderung?",
         "Tirol: 25 % Landeszuschuss plus 3.000 € Bonus, mit den 5.000 € des Bundes bei 30.000 € Kosten "
         "15.500 € (rund 52 %). Wien folgt mit bis zu 8.000 € Landesförderung, mit dem Bund 13.000 €. "
         "Kärnten (3.000 € Pauschale) und Salzburg liegen im Mittelfeld, die Steiermark nimmt für neue "
         "Wärmepumpen derzeit keine Anträge an."),
        ("Muss ich die Landesförderung vor oder nach dem Heizungstausch beantragen?",
         "Das hängt vom Bundesland ab. In Oberösterreich, Vorarlberg (spätestens 6 Monate nach Inbetriebnahme) "
         "und dem Burgenland wird nach dem Heizungstausch beantragt, in anderen Ländern ist eine Registrierung "
         "vor Beginn nötig. Beim Bund registrieren Sie nach der Energieberatung, das reserviert das Budget; "
         "gefördert werden in der Neuauflage Leistungen ab 7. Oktober 2026."),
        ("Gibt es Landesförderungen auch für Neubauten?",
         "In einigen Bundesländern wie Salzburg werden auch Neubauten mit erneuerbaren Heizsystemen gefördert. "
         "In den meisten Ländern und bei der Bundesförderung liegt der Fokus auf dem Austausch fossiler "
         "Heizungen im Bestand."),
        ("Werden auch Erdwärme-Wärmepumpen von den Ländern unterstützt?",
         "Ja, die Landesprogramme fördern grundsätzlich Luft-Wasser, Sole-Wasser und Wasser-Wasser. Auf "
         "Bundesebene kommt beim Kesseltausch bei Erdwärme mit neuer Bohrung ein Bohrbonus von 5.000 € dazu "
         "(seit 2. November 2026 wieder beantragbar), in "
         "Kärnten gibt es zusätzlich 1.500 € bei Errichtung einer Solaranlage."),
        ("Wie hoch ist die Landesförderung in Kärnten 2026?",
         "2026 zahlt das Land Kärnten eine Pauschale von 3.000 € für die Wärmepumpe, plus 1.500 € bei Errichtung "
         "einer Solaranlage und 200 € für den hydraulischen Abgleich. Kelag-Stromkunden erhalten zusätzlich "
         "1.200 € Prämie als Gutschrift über zwei Jahre. Die frühere Regel (35 %, höchstens 6.000 €) galt nur bis "
         "Ende 2025. Zusammen mit dem Kesseltausch des Bundes (5.000 €) sind das bis 8.000 €. Ob das Budget "
         "reicht, klären wir vor dem Angebot."),
        ("Gibt es 2026 eine Landesförderung für Wärmepumpen in der Steiermark?",
         "Für neue Wärmepumpen derzeit nicht: Das Land Steiermark nimmt keine Anträge an und nennt auf absehbare "
         "Zeit keine Förderungsmöglichkeit (Stand 10. Oktober 2026). Gefördert wird nur der Tausch mindestens "
         "15 Jahre alter Biomassekessel oder Wärmepumpen mit höchstens 30 %, höchstens 1.500 €, und nur ohne "
         "Fernwärme-Anschlussmöglichkeit. Bereits eingereichte Anträge werden weiter bearbeitet."),
        ("Darf die Gesamtförderung die Kosten übersteigen?",
         "Nein. Die Summe aus Bund, Land, Gemeinde und Energieversorger-Prämien darf die tatsächlichen "
         "Investitionskosten nicht übersteigen. Alle Förderungen werden in der Transparenzdatenbank erfasst, "
         "unzulässige Mehrfachförderungen werden zurückgefordert."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Wärmepumpen in Kärnten und der Steiermark und übernimmt Bundes-, Landes- und "
                    "Gemeindeanträge. Bund: Stand 19. November 2026; Kärnten und Steiermark: Stand Oktober 2026, übrige Länder: Stand April 2026; Förderhöhen können sich "
                    "im Jahresverlauf ändern. Keine Rechts- oder Steuerberatung, maßgeblich sind die "
                    "offiziellen Förderbedingungen der Landesförderungsstellen."),
    "sources": [
        ("Sanierungsoffensive 2026 (Bundesportal)", "https://www.sanierungsoffensive.gv.at/"),
        ("KPC: Informationsblatt Kesseltausch 2026 Ein-/Zweifamilienhaus/Reihenhaus, Neuauflage ab 2.11.2026 (Version 10/2026)",
         "https://www.sanierungsoffensive.gv.at/fileadmin/user_upload/2026/Infoblatt_Neuauflage_Kesseltausch_2026_EFH.pdf"),
        ("Sanierungsoffensive: Aktionsseite Kesseltausch Neuauflage Ein-/Zweifamilienhaus oder Reihenhaus",
         "https://www.sanierungsoffensive.gv.at/kesseltausch/neuauflage-ein-/zweifamilienhaus-oder-reihenhaus"),
        ("Verband Wärmepumpe Austria: Förderübersicht aller Bundesländer",
         "https://www.waermepumpe-austria.at/foerderungen"),
        ("Land Steiermark: Förderung für Heizungen (Wohnbau, Stand 10. Oktober 2026)",
         "https://www.wohnbau.steiermark.at/cms/ziel/164947118/DE/"),
    ],
    "related": [
        ("/waermepumpenfoerderung-in-oesterreich/", "Wärmepumpenförderung Österreich 2026: Überblick"),
        ("/sanierungsoffensive-2026/", "Sanierungsoffensive 2026: Kesseltausch neu, 5.000 €"),
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
