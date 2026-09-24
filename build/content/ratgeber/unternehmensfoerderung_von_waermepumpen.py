"""Ratgeber: Unternehmensförderung für Wärmepumpen 2026 (Betriebe, Vereine, Gemeinden).

Migriert vom WordPress-Artikel ebz-photovoltaik.at/unternehmensfoerderung-von-waermepumpen/
(veröffentlicht 2026-03-25, zuletzt geändert 2026-04-12). Zahlen: Stand April 2026.
Bereinigt: Gedankenstriche ("50–100 kW", "15–25 %"), "Ohne Subunternehmer" entfernt,
Förderhöhen als Tabelle, Hinweis auf geänderte Voraussetzungen ab 1. April 2026 beibehalten.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "unternehmensfoerderung-von-waermepumpen",
    "path": "/unternehmensfoerderung-von-waermepumpen/",
    "title": "Wärmepumpen-Förderung für Betriebe 2026: bis 12.000 € | EBZ",
    "description": ("Wärmepumpen-Förderung für Betriebe 2026: bis 7.500 € unter 50 kW, 12.000 € bei 50 bis "
                    "100 kW, max. 50 %. Antrag bis 6 Monate nach Rechnung, De-minimis-Grenze."),
    "eyebrow": "Förderung · Betriebe und Vereine",
    "crumb_label": "Unternehmensförderung Wärmepumpe",
    "h1": "Unternehmensförderung für Wärmepumpen 2026: Bis zu 12.000 € für Betriebe, Vereine und Gemeinden",
    "lead": ("Die Wärmepumpenförderung ist nicht nur für Privathaushalte gedacht. Unternehmen, Vereine, "
             "konfessionelle Einrichtungen und Gemeinden erhalten über die KPC bis zu 12.000 € für den Tausch "
             "einer fossilen Heizung, bei Anlagen ab 100 kW bis zu 30 % der Förderungsbasis. Hier lesen Sie "
             "Programme, Förderhöhen und den Ablauf, der sich von der Privatförderung unterscheidet."),
    "chips": [
        "Unter 50 kW: <b>bis 7.500 €</b>",
        "50 bis 100 kW: <b>bis 12.000 €</b>",
        "Quote: <b>max. 50 %</b>",
        "Antrag <b>nach</b> Umsetzung",
    ],
    "date_published": "2026-03-25",
    "date_modified": "2026-09-24",
    "hero_img": "gen_gewerbe",
    "hero_alt": "Gewerbegebäude mit Photovoltaik auf dem Dach und Wärmepumpe im Betrieb",

    "tldr": [
        "„Raus aus Öl und Gas“ für Betriebe (KPC) fördert den Tausch eines fossilen Heizsystems unter 100 kW "
        "mit bis zu 7.500 € (unter 50 kW) bzw. 12.000 € (50 bis 100 kW), maximal 50 % der förderfähigen Kosten. "
        "Neuerrichtung oder Ersatz nicht-fossiler Anlagen: 4.000 € bzw. 7.000 €.",
        "Ab 100 kW gibt es ein eigenes KPC-Programm: 15 bis 25 % der Förderungsbasis bei Projekten bis 150.000 €, "
        "30 % darüber, plus 5 % EMAS-Bonus.",
        "Antragsberechtigt sind alle Unternehmen, unternehmerisch tätige Organisationen, Vereine, konfessionelle "
        "Einrichtungen und (ab 100 kW) Gemeinden. Die Wärmepumpe muss überwiegend betrieblich genutzt werden.",
        "Anders als bei Privaten wird der Antrag unter 100 kW erst nach Umsetzung gestellt, spätestens 6 Monate "
        "nach Rechnungslegung. Ab 1. April 2026 gelten geänderte Voraussetzungen für Anlagen unter 100 kW.",
        "De-minimis: maximal 300.000 € Förderung je Unternehmen in drei Jahren. Landesförderungen sind in vielen "
        "Fällen kombinierbar. Land- und Forstwirtschaft: eigenes Programm mit bis zu 100.000 € bis November 2026.",
    ],
    "kpis": [
        ("12.000 €", "max. bei 50 bis 100 kW"),
        ("50 %", "maximale Förderquote"),
        ("6 Monate", "Antragsfrist nach Rechnung"),
        ("300.000 €", "De-minimis-Grenze in 3 Jahren"),
    ],

    "sections": [
        ("Warum sich der Heizungstausch auch für Unternehmen rechnet", "warum", f"""
<p>Steigende Energiepreise treffen Betriebe besonders, weil Heizsysteme dort über längere Zeiträume und für
größere Flächen laufen. Ob Bürogebäude, Werkstatt, Vereinslokal oder Gemeindeamt: Die Heizkosten sind
ein wesentlicher Betriebskostenfaktor, der sich mit einer {a('waermepumpe', 'Wärmepumpe')} deutlich senken
lässt. Gleichzeitig wächst der regulatorische Druck: Das Erneuerbaren-Wärme-Paket sieht den schrittweisen
Ausstieg aus fossilen Heizsystemen vor, und Kunden wie Auftraggeber legen zunehmend Wert auf nachhaltige
Betriebsführung.</p>
<p>Der Bund unterstützt den Umstieg für Betriebe mit eigenen Programmen, die sich von den
Privatprogrammen unterscheiden und in manchen Fällen höhere Beträge bieten. Stand: April 2026.</p>
"""),
        ("Welche Förderprogramme gibt es für Unternehmen?", "programme", f"""
<h3>„Raus aus Öl und Gas“ für Betriebe: Anlagen unter 100 kW</h3>
<p>Das Programm ist das Pendant zur {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive')} für
Privathaushalte und wird von der Kommunalkredit Public Consulting (KPC) im Auftrag des Bundesministeriums
abgewickelt. Antragsberechtigt sind alle Unternehmen und unternehmerisch tätigen Organisationen in
Österreich sowie Vereine und konfessionelle Einrichtungen. Gefördert wird der Ersatz eines fossilen
Heizsystems (Öl, Gas, Kohle, Strom, Allesbrenner) durch Wärmepumpe, Holzheizung oder Fernwärmeanschluss
mit überwiegend betrieblicher Nutzung. Die thermische Leistung der neuen Anlage muss unter 100 kW liegen.
Auch Neuerrichtungen im Neubau und der Ersatz nicht-fossiler Altanlagen werden gefördert, zu geringeren
Sätzen.</p>
{A.table(
    ["Maßnahme", "Leistung", "Maximale Förderung"],
    [
        ["Tausch eines fossilen Heizsystems", "unter 50 kW", "7.500 €"],
        ["Tausch eines fossilen Heizsystems", "50 bis 100 kW", "12.000 €"],
        ["Neuerrichtung oder Ersatz nicht-fossiler Altanlage", "unter 50 kW", "4.000 €"],
        ["Neuerrichtung oder Ersatz nicht-fossiler Altanlage", "50 bis 100 kW", "7.000 €"],
    ],
    hl_cols=(2,),
)}
<p>Die Förderung ist mit maximal 50 % der förderfähigen Kosten gedeckelt.</p>
{A.box("Ab dem 1. April 2026 gelten geänderte Voraussetzungen für die Förderung betrieblich genutzter "
       "Wärmeerzeuger unter 100 kW. Prüfen Sie vor der Beauftragung die aktuellen Bedingungen auf "
       "umweltfoerderung.at.", label="Achtung:")}
<h3>Wärmepumpen ab 100 kW: größere betriebliche Anlagen</h3>
<p>Für Anlagen ab 100 kW Nennwärmeleistung gibt es ein eigenes KPC-Programm für Unternehmen,
unternehmerisch tätige Organisationen und österreichische Gemeinden. Gefördert werden elektrisch
betriebene Wärmepumpen, die Umgebungswärme nutzen und überwiegend Heizwärme oder Warmwasser
bereitstellen. Die Fördersätze werden projektindividuell berechnet:</p>
{A.table(
    ["Projektumfang", "Fördersatz"],
    [
        ["Projekte bis 150.000 €", "15 bis 25 % der Förderungsbasis, abhängig von der Unternehmensgröße"],
        ["Projekte über 150.000 €", "30 % der Förderungsbasis"],
        ["EMAS-Bonus", "zusätzlich 5 % für Unternehmen mit EMAS-Zertifizierung"],
    ],
    hl_cols=(1,),
)}
"""),
        ("Was gefördert wird und was nicht", "foerderfaehig", f"""
<h3>Förderfähige Kosten</h3>
<ul>
  <li><b>Material:</b> Wärmepumpe, Speicher, Regelungstechnik und Zubehör.</li>
  <li><b>Montage:</b> Installation durch einen befugten Installationsbetrieb.</li>
  <li><b>Planung:</b> technische Auslegung und Projektplanung.</li>
  <li><b>Demontage und Entsorgung:</b> Abbau der alten Heizanlage, Entsorgung von Kessel und Tankanlage.</li>
</ul>
<h3>Nicht förderfähig</h3>
<ul>
  <li><b>Eigenleistungen:</b> Die Anlage muss von einem befugten Fachbetrieb installiert werden.</li>
  <li><b>Reine Kälteanlagen:</b> Wärmepumpen, die ausschließlich kühlen, sind ausgeschlossen.</li>
  <li><b>Wiederholte Förderung:</b> Pro Standort wird nur eine Zentralheizungsanlage gefördert. Wurde für den
  Standort bereits eine Förderung gewährt, ist ein neuer Antrag ausgeschlossen.</li>
</ul>
"""),
        ("Technische Voraussetzungen für Betriebe", "technik", f"""
{A.table(
    ["Kriterium", "Anforderung"],
    [
        ["EHPA-Gütesiegel", "Kriterien der European Heat Pump Association in gültiger Version, bestätigt durch ein unabhängiges Prüfinstitut"],
        ["Kältemittel", "unter 100 kW: GWP höchstens 750; über 100 kW: bei GWP ab 1.500 Abzug von 20 %"],
        ["Vorrangprüfung Fernwärme", "Anschluss an ein klimafreundliches Fernwärmenetz hat Vorrang, wenn technisch möglich und wirtschaftlich zumutbar"],
        ["Nutzung", "überwiegend Heizwärme oder Warmwasser für den Betrieb"],
        ["Altanlage", "vollständig stilllegen und entsorgen; nicht entsorgbare Tanks entleeren, reinigen, verplomben; Nachweis auf Nachfrage der KPC"],
    ],
)}
"""),
        ("Schritt für Schritt: So läuft die Antragstellung für Betriebe ab", "ablauf", f"""
<p>Der entscheidende Unterschied zur Privatförderung: Bei Anlagen unter 100 kW wird der Antrag nach der
Umsetzung gestellt.</p>
{A.steps([
    ("Projekt planen und umsetzen",
     "Sie beauftragen einen Fachbetrieb, lassen die alte Heizung entsorgen und die Wärmepumpe installieren. "
     "Sammeln Sie alle Rechnungen und Nachweise, sie sind Grundlage des Antrags."),
    ("Online-Antrag bei der KPC einreichen",
     "Nach Umsetzung stellen Sie den Antrag über die KPC-Plattform, spätestens 6 Monate nach Rechnungslegung. "
     "Abgefragt wird auch die Höhe bisher erhaltener De-minimis-Förderungen."),
    ("Prüfung und Auszahlung",
     "Die KPC prüft die Unterlagen. Nach positivem Bescheid und Genehmigung durch das Bundesministerium wird "
     "die Förderung als einmaliger, nicht rückzahlbarer Zuschuss überwiesen."),
])}
<h3>Anlagen ab 100 kW</h3>
<p>Hier ist der Prozess umfangreicher, weil die Förderung projektindividuell berechnet wird. Nehmen Sie
frühzeitig Kontakt mit der KPC auf. Nach Einreichung und Bestätigung können Sie das Bauvorhaben auf eigenes
Risiko starten; die endgültige Zusage folgt nach Projektprüfung und Genehmigung. KPC-Serviceteam „Raus aus
Öl und Gas für Betriebe“: Tel. +43 1 31631-714, E-Mail heizung@kommunalkredit.at.</p>
{A.box_dark("Frist im Blick behalten",
    "Unter 100 kW zählt das Rechnungsdatum: Der Antrag muss innerhalb von 6 Monaten nach Rechnungslegung "
    "bei der KPC einlangen. Wer die Frist versäumt, verliert den Anspruch, unabhängig von der Anlagenqualität.")}
{A.cta("Betriebliche Wärmepumpe mit Förderung planen",
       "EBZ Energie analysiert Ihren Wärmebedarf, plant Wärmepumpe und Photovoltaik als Gesamtpaket und "
       "bereitet den KPC-Antrag inklusive De-minimis-Prüfung vor.",
       secondary=("waermepumpe", "Zur Wärmepumpen-Leistungsseite"))}
"""),
        ("Kombination mit Landesförderungen und De-minimis-Regel", "kombination", f"""
<p>Die Bundesförderung kann in vielen Fällen mit Landesförderungen kombiniert werden. In manchen
Bundesländern gibt es eigene betriebliche Programme, die auf die KPC-Förderung aufstocken; in Kärnten
etwa können Betriebe Landesförderungen zusätzlich beantragen. Auch hier darf die Gesamtförderung die
tatsächlichen Investitionskosten nicht übersteigen. Dazu kommen Gemeindezuschüsse. Einen Überblick über
die Länderprogramme gibt der Ratgeber
{a('/landesfoerderungen-fuer-die-waermepumpe/', 'Landesförderungen für die Wärmepumpe')}.</p>
<h3>De-minimis: 300.000 € in drei Jahren</h3>
<p>Viele Unternehmensförderungen werden als De-minimis-Beihilfen vergeben. Ein Unternehmen einschließlich
verbundener Unternehmen darf innerhalb von drei Jahren maximal 300.000 € an De-minimis-Förderungen
erhalten. Die bisher erhaltenen Beträge werden im Online-Antrag abgefragt. Haben Sie in den letzten drei
Jahren bereits andere De-minimis-Förderungen bezogen, prüfen Sie den verbleibenden Spielraum. Für
bestimmte Kategorien, etwa Dienstleistungen von allgemeinem wirtschaftlichem Interesse wie sozialen
Wohnbau, gelten eigene beihilfenrechtliche Grundlagen mit höheren Obergrenzen.</p>
"""),
        ("Wärmepumpe und Photovoltaik: für Betriebe die ideale Kombination", "photovoltaik", f"""
<p>Betriebe mit hohem Tagesstrombedarf, etwa Bürogebäude, Werkstätten oder Gastronomie, haben ein
Verbrauchsprofil, das gut zur Erzeugung einer {a('photovoltaik', 'Photovoltaikanlage')} passt. Der
tagsüber erzeugte Solarstrom treibt die Wärmepumpe direkt an und senkt die Betriebskosten. Für
betriebliche PV-Anlagen gibt es eigene Programme über den EAG-Investitionszuschuss und die
KPC-Umweltförderung für Betriebe (siehe {a('foerderung_at', 'Photovoltaik-Förderung Österreich')}).
Wie Wärmepumpe und PV zusammenspielen, zeigt der Ratgeber
{a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}. Ein Beispiel aus der Praxis:
Bei einem Gewerbebetrieb in Oberösterreich mit 40 kWp und 40-kWh-Speicher liegt die Ersparnis bei rund
13.500 € pro Jahr (siehe {a('referenzen', 'Referenzen')}).</p>
<h3>Sonderfall Land- und Forstwirtschaft</h3>
<p>Für land- und forstwirtschaftliche Betriebe hat der Klima- und Energiefonds ein eigenes Programm
aufgelegt. Wer Wärmepumpe, Solarthermie und Energiemanagement kombiniert, kann einen Investitionszuschuss
von bis zu 100.000 € erhalten. Die Einreichfrist läuft bis November 2026. Für das Energiemanagement
selbst gibt es zudem die {a('/ems-foerderung/', 'EMS-Förderung des Klimafonds')}.</p>
"""),
        ("Fazit: Höhere Beträge, anderer Ablauf", "fazit", f"""
<p>Die Betriebsförderung bietet mit bis zu 12.000 € und einer Quote von bis zu 50 % mehr als die
Privatförderung, folgt aber eigenen Regeln: Antrag nach Umsetzung, 6-Monats-Frist ab Rechnung,
De-minimis-Grenze und ab 1. April 2026 geänderte Voraussetzungen unter 100 kW. Wer Wärmepumpe und
Photovoltaik gemeinsam plant, nutzt zwei Fördertöpfe und senkt die Betriebskosten dauerhaft. Alle
Programme im Überblick: {a('/waermepumpenfoerderung-in-oesterreich/', 'Wärmepumpenförderung in Österreich 2026')}.</p>
{A.cta("Jetzt berechnen, wie viel Ihr Betrieb sparen kann",
       "Bedarfsanalyse, Förderberatung für Betriebe und Installation von Wärmepumpe und PV aus einer Hand.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für gewerbliche Wärmepumpen und Photovoltaik: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("Ob Handwerksbetrieb, Vereinslokal oder landwirtschaftlicher Hof: EBZ Energie aus Villach "
                 "plant und installiert Wärmepumpen und Photovoltaik für Betriebe in Kärnten und der "
                 "Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften und voller "
                 "Gewährleistung. Wir kennen die betrieblichen Programme, die De-minimis-Grenzen und die "
                 "Kontakte zu den Förderstellen."),
        "grid": [
            ("Bedarfsanalyse", "Wir ermitteln den betrieblichen Wärmebedarf und das passende System."),
            ("Förderberatung für Betriebe", "KPC-Antrag, De-minimis-Prüfung, Landes- und Gemeindemittel."),
            ("Komplettinstallation", "Wärmepumpe und PV vom selben Team, mit voller Gewährleistung."),
            ("Regionale Expertise", "Betriebliche Förderlandschaft in Kärnten und der Steiermark im Detail."),
        ],
    },

    "faq": [
        ("Kann ich als Einzelunternehmer die Betriebsförderung nutzen?",
         "Ja. Alle Unternehmen und unternehmerisch tätigen Organisationen sind antragsberechtigt, unabhängig "
         "von Rechtsform oder Größe. Entscheidend ist die überwiegend betriebliche Nutzung der Wärmepumpe. "
         "Wird das Gebäude teilweise privat genutzt, kann die Privatförderung der bessere Weg sein."),
        ("Muss ich als Betrieb den Antrag vor oder nach dem Heizungstausch stellen?",
         "Bei Anlagen unter 100 kW nach der Umsetzung, spätestens 6 Monate nach Rechnungslegung. Das ist der "
         "wesentliche Unterschied zur Privatförderung, bei der vor Beginn registriert wird. Ab 100 kW empfiehlt "
         "sich eine frühzeitige Abstimmung mit der KPC, weil die Förderung projektindividuell berechnet wird."),
        ("Gibt es eine Förderung für Wärmepumpen in Gebäuden, die ich als Unternehmer vermiete?",
         "Vermietete Gebäude fallen nicht unter die Privatförderung. Die Betriebsförderung setzt eine überwiegend "
         "betriebliche Nutzung voraus. Rein vermietete Wohngebäude sind in der Regel von beiden Schienen nicht "
         "abgedeckt; lassen Sie Ihre Situation individuell prüfen."),
        ("Was ist der Unterschied zwischen Betriebs- und Privatförderung?",
         "Die Betriebsförderung erlaubt höhere Maximalbeträge (bis 12.000 € bei 50 bis 100 kW) und eine Quote "
         "von bis zu 50 % statt 30 %. Dafür gelten De-minimis-Grenzen und beihilfenrechtliche Vorschriften, und "
         "der Antrag erfolgt nach Umsetzung. Die Privatförderung ist einfacher, hat aber niedrigere Beträge."),
        ("Kann ein Verein die Förderung beantragen?",
         "Ja. Vereine und konfessionelle Einrichtungen sind ausdrücklich antragsberechtigt, mit denselben "
         "Fördersätzen und technischen Voraussetzungen wie Unternehmen. Der Antrag läuft ebenfalls online über "
         "die KPC."),
        ("Was bedeutet die De-minimis-Grenze für meinen Betrieb?",
         "Ein Unternehmen inklusive verbundener Unternehmen darf in drei Jahren maximal 300.000 € an "
         "De-minimis-Förderungen erhalten. Bereits bezogene Beträge werden im Antrag abgefragt. Bei anderen "
         "Förderungen in den letzten drei Jahren sollten Sie den verbleibenden Spielraum vorab prüfen."),
        ("Wie hoch ist die Förderung für Wärmepumpen ab 100 kW?",
         "Bei Projekten bis 150.000 € liegen die Sätze je nach Unternehmensgröße bei 15 bis 25 % der "
         "Förderungsbasis, bei Projekten über 150.000 € bei 30 %. Unternehmen mit EMAS-Zertifizierung erhalten "
         "zusätzlich 5 %. Bei einem GWP des Kältemittels ab 1.500 sinkt die Förderung um 20 %."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Wärmepumpen und Photovoltaik für Betriebe in Kärnten und der Steiermark und bereitet die "
                    "Anträge bei der KPC vor. Alle Angaben entsprechen dem Stand April 2026; ab 1. April 2026 "
                    "gelten geänderte Voraussetzungen unter 100 kW. Keine Rechts- oder Steuerberatung, "
                    "maßgeblich sind die offiziellen Förderbedingungen auf umweltfoerderung.at."),
    "sources": [
        ("Umweltförderung (KPC): Raus aus Öl und Gas für Betriebe", "https://www.umweltfoerderung.at/"),
    ],
    "related": [
        ("/waermepumpenfoerderung-in-oesterreich/", "Wärmepumpenförderung Österreich 2026: Überblick"),
        ("/landesfoerderungen-fuer-die-waermepumpe/", "Landesförderungen: alle 9 Bundesländer"),
        ("/ems-foerderung/", "EMS-Förderung 2026: bis 20.000 € für Betriebe"),
        ("waermepumpe", "Wärmepumpen-Installateur EBZ Energie"),
    ],
    "cta": {
        "h3": "Förderung für Ihren Betrieb",
        "text": "Wir prüfen Programm, De-minimis-Spielraum und Kombination mit dem Land und planen die Anlage.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Heizkosten im Betrieb dauerhaft senken",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
