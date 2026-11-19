"""Ratgeber: Wärmepumpe Stromverbrauch (Rechenweg, Tabelle nach Wohnfläche, JAZ, Winter pro Tag, Kosten, Tarif, PV, Tipps).

Neuer Artikel (kein WordPress-Vorgänger), erstellt 2026-11-19.
Ziel-Keywords (Google Ads, Österreich, 19.11.2026): wärmepumpe stromverbrauch / stromverbrauch wärmepumpe /
stromverbrauch einer wärmepumpe je 590 (Jänner 1.000), luft wärmepumpe stromverbrauch 210, wärmepumpe stromverbrauch
pro tag winter 140, jahresarbeitszahl wärmepumpe 140, stromverbrauch einfamilienhaus mit wärmepumpe 70 bis 90,
wärmepumpe stromverbrauch pro jahr 50 bis 90, wie viel strom braucht eine wärmepumpe 50, wärmepumpe stromtarif 50.

Faktenbasis (alle Quellen am 19.11.2026 geöffnet): Fraunhofer ISE Presseinformation 03.11.2025 (Feldtest 77 Anlagen,
Deutschland), Energieinstitut Vorarlberg (Vorlauftemperatur, 2,5 % je Grad, Zähler, PV-Anteil 10 bis 15 %),
Statistik Austria Energieverwendung 2025 bis 2026 (Warmwasser, Wohnfläche, Nutzungsgrade), E-Control Preismonitor
November 2026 und OeMAG Oktober 2026 (aus warmwasser_fakten.md), PVGIS-SARAH2 (JRC) für 10 kWp in Villach,
VERBUND-Tariffolder Wärmepumpe 01/2026, HTW Berlin 2023 (SG Ready), Energie Agentur Steiermark (Grundwasser),
Verbraucherzentrale (Deutschland), Klimafonds-Leitfaden EMS 2026.
Eigene Rechnungen (mit *): Tabelle nach Wohnfläche (Heizwärmebedarf je m² als Annahme, JAZ als Annahme innerhalb der
Fraunhofer-Spanne), Tagesverbrauch im Winter (Heizlast 6 kW, COP-Annahmen), Kosten mit 28 bis 35 ct.
Nicht behauptet: Netztarif "unterbrechbar" in Kärnten/Steiermark (nicht belegt), konkrete Preise von
Wärmepumpentarifen (Folder nicht lesbar), Energieausweis-Klassengrenzen (Skala wird umgestellt), JAZ-Zahl für
Grundwasser-Wärmepumpen (keine geöffnete Quelle mit Zahl).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "waermepumpe-stromverbrauch",
    "path": "/waermepumpe-stromverbrauch/",
    "cluster": "Wärmepumpe und Heizen",
    "title": "Wärmepumpe Stromverbrauch: kWh pro Jahr und Tag | EBZ",
    "description": ("Wärmepumpe Stromverbrauch: 12.000 kWh Wärme brauchen bei JAZ 3,4 rund 3.500 kWh Strom. "
                    "Tabelle nach Wohnfläche, Tag im Winter, Kosten 2026, Tarif, PV-Anteil."),
    "eyebrow": "Wärmepumpe · Stromverbrauch",
    "crumb_label": "Wärmepumpe Stromverbrauch",
    "h1": "Wärmepumpe Stromverbrauch: Wie viel Strom eine Wärmepumpe im Jahr und pro Tag braucht",
    "lead": ("Ein Einfamilienhaus mit 12.000 kWh Heizwärmebedarf braucht mit einer Luft-Wasser-Wärmepumpe rund "
             "3.000 bis 3.500 kWh Strom im Jahr, ein unsanierter Altbau leicht das Doppelte. Dieser Ratgeber zeigt "
             "den Rechenweg, eine Tabelle nach Wohnfläche, den Verbrauch an kalten Wintertagen, die Kosten mit "
             "österreichischen Strompreisen 2026 und was eine PV-Anlage davon realistisch deckt."),
    "chips": [
        "Formel: <b>Wärmebedarf ÷ JAZ</b>",
        "JAZ Luft im Feldtest: <b>3,4</b>",
        "150 m² saniert: <b>rund 3.400 kWh*</b>",
        "Strompreis: <b>28 bis 35 ct/kWh</b>",
    ],
    "date_published": "2026-11-19",
    "date_modified": "2026-11-19",
    "hero_img": "waermepumpe",
    "hero_alt": "Außeneinheit einer Luft-Wasser-Wärmepumpe mit zwei Ventilatoren auf einem Betonsockel vor einer Holzwand im Garten",

    "tldr": [
        "Stromverbrauch = Heizwärmebedarf geteilt durch die Jahresarbeitszahl (JAZ). 12.000 kWh Wärme brauchen "
        "bei JAZ 3,4 rund 3.500 kWh Strom, bei JAZ 4 rund 3.000 kWh.*",
        "Im Feldtest des Fraunhofer ISE (77 Anlagen in Bestandsgebäuden, Deutschland) erreichten "
        "Luft-Wasser-Wärmepumpen im Mittel JAZ 3,4, Erdwärmepumpen 4,3.",
        "An einem Wintertag mit 0 °C braucht ein Haus mit 6 kW Heizlast rund 29 kWh Strom, bei -10 °C rund "
        "54 kWh.*",
        "Bei 28 bis 35 Cent je kWh (E-Control, November 2026) kosten 3.400 kWh rund 950 bis 1.200 Euro im Jahr.*",
        "Eine 10-kWp-Anlage in Villach liefert im Dezember nur rund 615 kWh, weniger als die Hälfte des Juli. "
        "PV senkt die Kosten deutlich, deckt den Winterbedarf aber nicht.",
    ],
    "kpis": [
        ("3,4", "mittlere JAZ Luft-Wasser im Feldtest"),
        ("rund 3.400 kWh", "150 m², saniert, pro Jahr*"),
        ("2,5 %", "Effizienz je Grad Vorlauftemperatur"),
        ("28 bis 35 ct", "Haushaltsstrom Kärnten und Steiermark*"),
    ],

    "sections": [
        ("Wie viel Strom braucht eine Wärmepumpe? Die Formel", "formel", f"""
<p><b>Der Stromverbrauch einer Wärmepumpe ergibt sich aus zwei Zahlen: dem Heizwärmebedarf des Hauses und der
Jahresarbeitszahl (JAZ) der Anlage.</b> Die JAZ sagt, wie viele Kilowattstunden Wärme die Wärmepumpe über ein
ganzes Jahr aus einer Kilowattstunde Strom macht. Den Rest holt sie aus Luft, Erdreich oder Grundwasser.</p>
{A.box_dark("Stromverbrauch (kWh) = Heizwärmebedarf (kWh) ÷ Jahresarbeitszahl",
            "Beispiel: 12.000 kWh Wärme ÷ JAZ 3,4 = rund 3.530 kWh Strom im Jahr. Mit JAZ 4 sind es "
            "3.000 kWh, mit JAZ 4,3 rund 2.790 kWh.*")}
<p>Ihren Heizwärmebedarf finden Sie im Energieausweis (kWh pro m² und Jahr, mal Wohnfläche) oder Sie
rechnen ihn aus dem bisherigen Verbrauch zurück: Gas- oder Ölmenge mal Nutzungsgrad des alten Kessels.
Statistik Austria rechnet für Gas mit 91,5 % und für Heizöl mit 86,9 % Nutzungsgrad. Wer bisher 1.500 Liter
Heizöl im Jahr verbraucht hat (rund 10 kWh je Liter), kam also auf rund 13.000 kWh Wärme.*</p>
<p>Dazu kommt das <b>Warmwasser</b>. Statistik Austria rechnet mit rund 15.600 Litern warmem Wasser pro
Person und Jahr, erwärmt von 10 auf 60 °C sind das rund 900 kWh Wärme pro Person. Weil die Wärmepumpe dafür
höhere Temperaturen braucht, ist sie beim Warmwasser weniger effizient. Mit JAZ 3 sind es rund 300 kWh Strom
pro Person und Jahr.* Wie die Kennzahlen COP und JAZ entstehen, erklärt der Ratgeber
{a('/funktionsweise-einer-waermepumpe/', 'Funktionsweise einer Wärmepumpe')}.</p>
"""),
        ("Stromverbrauch nach Wohnfläche und Gebäudestandard", "tabelle", f"""
<p><b>Die Wohnfläche allein sagt wenig: Ein unsanierter Altbau braucht bei gleicher Fläche etwa das
Vierfache an Strom wie ein Neubau.</b> Die Tabelle rechnet drei typische Gebäudestandards durch, nur für die
Heizung, ohne Warmwasser.</p>
{A.table(
    ["Wohnfläche", "Neubau, Fußbodenheizung (40 kWh/m², JAZ 4)*", "saniert (80 kWh/m², JAZ 3,5)*",
     "unsanierter Altbau (140 kWh/m², JAZ 3)*"],
    [
        ["100 m²", "rund 1.000 kWh", "rund 2.300 kWh", "rund 4.700 kWh"],
        ["150 m²", "rund 1.500 kWh", "rund 3.400 kWh", "rund 7.000 kWh"],
        ["200 m²", "rund 2.000 kWh", "rund 4.600 kWh", "rund 9.300 kWh"],
        ["Kosten 150 m² bei 30 ct*", "rund 450 €", "rund 1.030 €", "rund 2.100 €"],
    ],
    hl_cols=(2,),
)}
<p>So ist die Tabelle gerechnet: Heizwärmebedarf je m² mal Wohnfläche, geteilt durch die JAZ. Die Werte je
m² sind gerundete Beispielannahmen für die drei Standards, die JAZ-Werte liegen innerhalb der im Feldtest
gemessenen Spanne von 2,6 bis 4,9 für Luft-Wasser-Wärmepumpen. In der Auswertung von Statistik
Austria haben Häuser im Schnitt 154 m² Wohnfläche (Haushalte in Ein- und Zweifamilienhäusern). Für Warmwasser kommen rund 300 kWh Strom pro Person dazu, bei vier
Personen also rund 1.200 kWh.* Setzen Sie für Ihr Haus den Wert aus dem Energieausweis ein, dann wird die
Rechnung genau. Was im Altbau vor der Wärmepumpe sinnvoll ist, zeigt
{a('/waermepumpe-im-altbau/', 'Wärmepumpe im Altbau')}.</p>
"""),
        ("Luftwärmepumpe, Erdwärme, Grundwasser: Stromverbrauch nach Wärmequelle", "jaz", f"""
<p><b>Je wärmer und gleichmäßiger die Wärmequelle, desto weniger Strom braucht die Wärmepumpe.</b> Das
Fraunhofer ISE hat in Deutschland über vier Jahre 77 Wärmepumpen in Ein- bis Dreifamilienhäusern im Bestand
gemessen (Abschluss November 2025):</p>
{A.table(
    ["Wärmequelle", "Jahresarbeitszahl im Feldtest", "Strom für 12.000 kWh Wärme*", "Was zu beachten ist"],
    [
        ["Luft-Wasser (61 Anlagen)", "Mittel 3,4, Spanne 2,6 bis 4,9", "rund 3.530 kWh",
         "keine Bohrung, im Winter sinkt die Effizienz"],
        ["Erdreich, Sole-Wasser (16 Anlagen)", "Mittel 4,3, Spanne 3,6 bis 5,4", "rund 2.790 kWh",
         "Bohrung oder Kollektor, höhere Anschaffung"],
        ["Grundwasser, Wasser-Wasser", "laut Verbraucherzentrale am effizientesten", "nicht gemessen",
         "Brunnen, wasserrechtliche Genehmigung, Pumpenstrom"],
    ],
    hl_cols=(1,),
)}
<p>Bei der Grundwasser-Wärmepumpe braucht die Brunnenpumpe zusätzlich Strom, und die Nutzung des Grundwassers
braucht immer eine wasserrechtliche Genehmigung (Energie Agentur Steiermark). Das Energieinstitut Vorarlberg
nennt eine JAZ von 4 als Ziel und warnt: Mit der Warmwasserbereitung kann die Gesamteffizienz einer Anlage
auf 2,5 sinken. Eine Luft-Wasser-Wärmepumpe mit JAZ 3,4 braucht also rund 25 % mehr Strom als eine
Erdwärmepumpe mit JAZ 4,3.* Ob sich die Mehrkosten der Bohrung zurückverdienen, rechnet der Ratgeber
{a('/erdwaermepumpe-kosten/', 'Erdwärmepumpe Kosten')} vor, die Preise der Luftvariante stehen unter
{a('/luftwaermepumpe-preise/', 'Luftwärmepumpe Preise')}.</p>
"""),
        ("Stromverbrauch pro Tag im Winter", "winter", f"""
<p><b>Der Jahreswert verteilt sich nicht gleichmäßig: An einem kalten Jännertag braucht die Wärmepumpe ein
Vielfaches eines Tages im Oktober.</b> Zwei Effekte kommen zusammen. Das Haus verliert mehr Wärme, und die
Luft-Wasser-Wärmepumpe arbeitet bei kalter Außenluft weniger effizient.</p>
{A.table(
    ["Tagesmitteltemperatur außen", "Wärmebedarf am Tag*", "angenommener COP*", "Strom am Tag*"],
    [
        ["+8 °C (Übergangszeit)", "rund 48 kWh", "4", "rund 12 kWh"],
        ["0 °C (normaler Wintertag)", "rund 86 kWh", "3", "rund 29 kWh"],
        ["-10 °C (Kälteperiode)", "rund 134 kWh", "2,5", "rund 54 kWh"],
    ],
    hl_cols=(3,),
)}
<p>Beispielhaus mit 6 kW Heizlast bei -12 °C, Wärmebedarf vereinfacht proportional zur Differenz zwischen
18 °C und der Außentemperatur, nur Heizung. Die COP-Werte sind Annahmen für eine moderne Luft-Wasser-Wärmepumpe
mit Fußbodenheizung. Mit Heizkörpern und höherer Vorlauftemperatur liegt der Verbrauch höher. Ein auffällig
hoher Tageswert bei milder Witterung deutet auf ein Problem hin, etwa einen zugeschalteten Heizstab oder eine
zu hoch eingestellte Heizkurve. Ein eigener Stromzähler für die Wärmepumpe macht solche Ausreißer sichtbar.</p>
"""),
        ("Stromkosten der Wärmepumpe 2026 in Kärnten und der Steiermark", "kosten", f"""
<p><b>Haushaltsstrom kostet in Kärnten und der Steiermark laut E-Control-Preismonitor (November 2026) im
Schnitt rund 28 bis 35 Cent je kWh</b>, inklusive Netz, Steuern und Abgaben. Gerechnet ist das aus dem
Jahrespreis für 3.500 kWh: Kelag 33,2 ct, Energie Klagenfurt 34,8 ct, Energie Steiermark 31,9 ct,
Energie Graz 28,0 ct. Weil darin die Grundpauschalen stecken, ist jede zusätzliche kWh für die Wärmepumpe
etwas günstiger.</p>
{A.table(
    ["Strombedarf Wärmepumpe pro Jahr", "bei 28 ct*", "bei 30 ct*", "bei 35 ct*"],
    [
        ["1.500 kWh (Neubau, 150 m²)", "rund 420 €", "rund 450 €", "rund 525 €"],
        ["3.400 kWh (saniert, 150 m²)", "rund 950 €", "rund 1.020 €", "rund 1.190 €"],
        ["7.000 kWh (Altbau, 150 m²)", "rund 1.960 €", "rund 2.100 €", "rund 2.450 €"],
    ],
    hl_cols=(2,),
)}
<p>Zum Vergleich mit Gas: Erdgas kostet bei denselben Anbietern rund 11,3 bis 15,3 Cent je kWh, bei 91,5 %
Nutzungsgrad sind das rund 12 bis 17 Cent je kWh Wärme. Die Wärmepumpe liefert die kWh Wärme bei JAZ 3,4 und
30 Cent Strompreis um rund 9 Cent.* Was Anschaffung und Betrieb über die Jahre kosten, steht im Ratgeber
{a('/kosten-einer-waermepumpe/', 'Kosten einer Wärmepumpe')}.</p>
{A.cta("Wie viel Strom braucht Ihre Wärmepumpe?",
       "Wir rechnen mit Ihrem Energieausweis oder Ihrem bisherigen Verbrauch, prüfen Heizkörper und "
       "Vorlauftemperatur vor Ort und sagen ehrlich, mit welchem Stromverbrauch Sie rechnen müssen.",
       secondary=("waermepumpe", "Zur Wärmepumpe"))}
"""),
        ("Wärmepumpentarif und eigener Zähler: lohnt sich das?", "tarif", f"""
<p><b>Einige Stromlieferanten bieten eigene Wärmepumpentarife an.</b> Beim VERBUND-Strom-Wärmepumpentarif
etwa (Folder Jänner 2026) gilt: nur für Privatpersonen mit eigener Wärmepumpe als primärem Heizsystem, mit
Nachweis wie Rechnungskopie oder Installationsnachweis, nicht für gemeinsam genutzte Anlagen in
Mehrparteienhäusern. Der Grundpreis wird je Monat und Zählpunkt verrechnet.</p>
<ul>
  <li><b>Zweiter Zählpunkt kostet laufend:</b> Für einen separaten Wärmepumpenzähler fallen eigene
  Grundgebühren an. Ob der günstigere Arbeitspreis das übersteigt, hängt vom Verbrauch ab. Bei 1.500 kWh im
  Neubau rechnet es sich seltener als bei 7.000 kWh im Altbau.</li>
  <li><b>Messen statt schätzen:</b> Das Energieinstitut Vorarlberg empfiehlt einen eigenen Stromzähler für
  die Wärmepumpe und einen Wärmemengenzähler im Heizkreis. Erst damit kennen Sie Ihre echte JAZ. Viele
  moderne Wärmepumpen zeigen Strom und Wärme auch selbst an.</li>
  <li><b>Dynamischer Tarif als Alternative:</b> Eine Wärmepumpe kann Wärme und Warmwasser in günstige Stunden
  verschieben. Wann das besser ist als ein Wärmepumpentarif, erklärt
  {a('/dynamischer-stromtarif/', 'Dynamischer Stromtarif')}.</li>
</ul>
<p>Netzseitige Sondertarife für Wärmepumpen in Kärnten und der Steiermark prüfen wir im Einzelfall mit dem
Netzbetreiber, eine allgemeine Aussage dazu treffen wir hier bewusst nicht.</p>
"""),
        ("Wie viel Strom kann die PV-Anlage liefern? Sommer und Winter ehrlich gerechnet", "photovoltaik", f"""
<p><b>Photovoltaik senkt die Stromkosten der Wärmepumpe, deckt aber im Winter nur einen kleinen Teil.</b>
Laut PVGIS (EU-Kommission, Strahlungsdaten 2005 bis 2020) erzeugt eine 10-kWp-Anlage in Villach, Süd mit 30°
Neigung, rund 12.350 kWh im Jahr. Davon fallen nur rund 2.720 kWh (22 %) in die Monate November bis Februar,
in denen die Wärmepumpe am meisten braucht.*</p>
{A.table(
    ["Monat", "PV-Ertrag 10 kWp Villach*", "Bedarf der Wärmepumpe"],
    [
        ["Juli", "rund 1.410 kWh", "nur Warmwasser"],
        ["Oktober", "rund 910 kWh", "Heizbeginn"],
        ["Dezember", "rund 615 kWh", "am höchsten"],
        ["Jänner", "rund 710 kWh", "am höchsten"],
    ],
    hl_cols=(1,),
)}
<p>Feldmessungen bestätigen das: Im Fraunhofer-Feldtest erreichten Gebäude mit Wärmepumpe und PV ohne
Batterie 25 bis 40 % Autarkie, mit Batterie 32 bis 62 %. Das Energieinstitut Vorarlberg nennt für ein
Einfamilienhaus mit 5 kWp, dass die Wärmepumpe in der Regel nicht über 10 bis 15 % des selbst erzeugten
Stroms direkt nutzt. Der Grund: Sonnenertrag und Wärmebedarf passen über das Jahr kaum zusammen (HTW Berlin).</p>
<p>Lohnend ist es trotzdem. Jede kWh, die die Wärmepumpe aus der eigenen Anlage bezieht, ersetzt Netzstrom
um 28 bis 35 Cent, statt für den OeMAG-Marktpreis eingespeist zu werden (Oktober 2026: 14,874 Cent).*
Wie Sie Anlage und Speicher dafür dimensionieren, zeigt
{a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}.</p>
"""),
        ("Stromverbrauch senken: sieben Hebel", "tipps", f"""
<p><b>Der größte Hebel ist die Vorlauftemperatur: Jedes Grad weniger verbessert die Effizienz um rund
2,5 %</b> (Energieinstitut Vorarlberg). Ideal sind unter 35 °C, über 50 °C wird es kritisch.</p>
{A.steps([
    ("Heizkurve absenken",
     "Stellen Sie die Heizkurve so niedrig ein, dass es gerade noch warm genug wird. 5 Grad weniger Vorlauf "
     "bringen nach der Faustregel rund 12 % weniger Strom.* Ausreichend große Heizkörper kommen laut "
     "Fraunhofer-Feldtest mit ähnlich niedrigen Temperaturen aus wie eine Fußbodenheizung."),
    ("Hydraulischen Abgleich machen",
     "Erst wenn jeder Heizkreis die richtige Wassermenge bekommt, reicht eine niedrige Vorlauftemperatur. "
     "Das Energieinstitut Vorarlberg nennt den Abgleich in jedem Fall empfehlenswert."),
    ("Nach dem ersten Winter nachregeln",
     "Heizkurve, Warmwassertemperatur und Laufzeiten nach der ersten Heizsaison prüfen. Im Feldtest waren "
     "viele Wärmepumpen bezogen auf den Verbrauch überdimensioniert, einige schalteten sehr häufig."),
    ("Heizstab im Blick behalten",
     "Im Feldtest machte der Heizstab bei Luft-Wasser-Wärmepumpen im Mittel nur 1,3 % des Stroms aus. "
     "Liegt der Wert bei Ihnen deutlich höher, stimmt die Einstellung oder die Auslegung nicht."),
    ("Warmwasser getrennt denken",
     "Bei Kombispeichern ohne saubere Trennung der Temperaturen wurde im Feldtest unnötig Wärme auf "
     "Warmwasser-Niveau erzeugt. Warmwasser nur so heiß wie nötig, Hygiene beachten, siehe "
     + a('/warmwasser-mit-photovoltaik/', 'Warmwasser mit Photovoltaik') + "."),
    ("SG Ready und Energiemanagement nutzen",
     "Über die SG-Ready-Schnittstelle kann ein Energiemanagementsystem die Wärmepumpe bei PV-Überschuss "
     "früher starten und Solltemperaturen anheben, so wird Solarstrom als Wärme gespeichert (HTW Berlin)."),
    ("Förderung für die Steuerung mitnehmen",
     "Die EMS-Förderung des Klimafonds zahlt 50 % der Kosten, höchstens 600 Euro, wenn das System "
     "mindestens zwei Komponenten steuert, etwa PV und Wärmepumpe. Registrierung vor der ersten Rechnung, "
     "bis 15. April 2027: " + a('/ems-foerderung/', 'EMS-Förderung 2026') + "."),
])}
"""),
        ("Fazit: Erst rechnen, dann dimensionieren", "fazit", f"""
<p>Der Stromverbrauch einer Wärmepumpe ist kein Rätsel: Heizwärmebedarf durch Jahresarbeitszahl, plus rund
300 kWh pro Person für Warmwasser. Ein saniertes Einfamilienhaus mit 150 m² liegt damit bei rund 3.400 kWh
fürs Heizen, ein Neubau bei der Hälfte, ein unsanierter Altbau beim Doppelten. Entscheidend für einen
niedrigen Verbrauch sind eine niedrige Vorlauftemperatur, eine passend dimensionierte Anlage und eine
Einstellung, die nach dem ersten Winter nachgeschärft wird. Photovoltaik und Energiemanagement senken die
Kosten spürbar, den Winter überbrückt aber weiter das Netz. Mehr zum Gesamtsystem lesen Sie unter
{a('/heizen-mit-waermepumpe/', 'Heizen mit Wärmepumpe')}, umgesetzte Anlagen finden Sie in unseren
{a('referenzen', 'Referenzen')}.</p>
<p><small>*Richtwerte und eigene Berechnungen auf Basis der genannten Quellen. Heizwärmebedarf je m², JAZ und
COP sind Beispielannahmen, Ihre Werte hängen von Gebäude, Heizsystem, Einstellung und Nutzung ab.
Strompreise E-Control Stand November 2026 (Durchschnittspreis inklusive Grundpauschalen), OeMAG-Marktpreis
Oktober 2026, PV-Erträge PVGIS-SARAH2 ohne Verschattung, Feldtestwerte aus Deutschland.</small></p>
{A.cta("Wärmepumpe und Photovoltaik ehrlich gerechnet",
       "Wir ermitteln Ihren Wärmebedarf, wählen die passende Wärmepumpe und zeigen, wie viel des Stroms "
       "Ihre PV-Anlage im Sommer und im Winter tatsächlich liefert.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("photovoltaik", "Zur Photovoltaik"))}
"""),
    ],

    "partner": {
        "h2": "Wärmepumpe, Photovoltaik und Steuerung aus einer Hand",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie plant und installiert Wärmepumpen, Photovoltaik, Batteriespeicher und "
                 "Energiemanagement in Kärnten und der Steiermark, mit zertifizierten Fachkräften und einem "
                 "festen Ansprechpartner von der Planung bis zur Übergabe. Wir dimensionieren die Wärmepumpe "
                 "nach dem tatsächlichen Wärmebedarf und stellen sie so ein, dass sie mit möglichst niedriger "
                 "Vorlauftemperatur läuft."),
        "grid": [
            ("Bedarf statt Schätzung", "Wärmebedarf aus Energieausweis oder Verbrauch berechnet."),
            ("Effizienz eingestellt", "Heizkurve, Abgleich und Warmwasser passend zum Haus."),
            ("Solarstrom eingebunden", "SG Ready und EMS nutzen den PV-Überschuss."),
            ("Förderung im Blick", "Landes- und EMS-Förderung in der richtigen Reihenfolge."),
        ],
    },

    "faq": [
        ("Wie viel Strom verbraucht eine Wärmepumpe im Jahr?",
         "Teilen Sie den Heizwärmebedarf durch die Jahresarbeitszahl. Ein saniertes Einfamilienhaus mit "
         "12.000 kWh Wärmebedarf braucht bei JAZ 3,4 rund 3.500 kWh, bei JAZ 4 rund 3.000 kWh Strom. Für "
         "Warmwasser kommen rund 300 kWh pro Person dazu. Ein Neubau liegt oft bei 1.000 bis 2.000 kWh, ein "
         "unsanierter Altbau bei 5.000 kWh und mehr."),
        ("Wie viel Strom braucht eine Wärmepumpe pro Tag im Winter?",
         "Das hängt von Heizlast und Außentemperatur ab. Ein Haus mit 6 kW Heizlast braucht an einem Tag mit "
         "0 °C rund 29 kWh Strom, bei -10 °C rund 54 kWh und bei +8 °C rund 12 kWh (Richtwerte für eine "
         "Luft-Wasser-Wärmepumpe mit Fußbodenheizung). Mit Heizkörpern und höherer Vorlauftemperatur liegt der "
         "Wert höher."),
        ("Was kostet das Heizen mit einer Wärmepumpe im Monat?",
         "Bei 3.400 kWh im Jahr und 30 Cent je kWh sind es rund 1.020 Euro, im Schnitt also rund 85 Euro im "
         "Monat. Tatsächlich fällt der Großteil zwischen November und Februar an, im Sommer bleibt nur das "
         "Warmwasser. Viele Lieferanten verrechnen gleichmäßige Teilbeträge."),
        ("Warum ist der Stromverbrauch meiner Wärmepumpe so hoch?",
         "Häufige Ursachen sind eine zu hohe Vorlauftemperatur, ein fehlender hydraulischer Abgleich, ein oft "
         "zugeschalteter Heizstab oder sehr häufiges Takten. Jedes Grad Vorlauf kostet rund 2,5 % Effizienz. "
         "Ein eigener Stromzähler und ein Wärmemengenzähler zeigen, welche JAZ Ihre Anlage wirklich erreicht."),
        ("Ist eine Wärmepumpe günstiger als Gas?",
         "Im Betrieb meist ja. Erdgas kostet in Kärnten und der Steiermark rund 11 bis 15 Cent je kWh, mit "
         "Kesselverlusten rund 12 bis 17 Cent je kWh Wärme. Eine Wärmepumpe mit JAZ 3,4 liefert die kWh Wärme "
         "bei 30 Cent Strompreis um rund 9 Cent, mit eigenem PV-Strom noch günstiger."),
        ("Welche Jahresarbeitszahl ist gut?",
         "Im Feldtest des Fraunhofer ISE (Deutschland, 77 Anlagen im Bestand) erreichten Luft-Wasser-"
         "Wärmepumpen im Mittel 3,4, Erdwärmepumpen 4,3. Das Energieinstitut Vorarlberg nennt eine JAZ von 4 "
         "als Ziel. Mit Warmwasserbereitung kann die Gesamteffizienz auf 2,5 sinken."),
        ("Brauche ich einen eigenen Stromzähler für die Wärmepumpe?",
         "Für einen Wärmepumpentarif ja, dann wird der Zählpunkt mit eigener Grundgebühr verrechnet. Ob sich "
         "das lohnt, hängt vom Verbrauch ab. Unabhängig vom Tarif empfiehlt das Energieinstitut Vorarlberg "
         "einen eigenen Stromzähler und einen Wärmemengenzähler, um die echte JAZ zu kennen."),
        ("Wie viel Strom der Wärmepumpe deckt eine PV-Anlage?",
         "Über das Jahr einen spürbaren Teil, im Winter wenig. Eine 10-kWp-Anlage in Villach erzeugt im "
         "Dezember rund 615 kWh, im Juli rund 1.410 kWh. Im Fraunhofer-Feldtest erreichten Häuser mit "
         "Wärmepumpe und PV ohne Batterie 25 bis 40 % Autarkie, mit Batterie 32 bis 62 %."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Mit zertifizierten Fachkräften plant und "
                    "installiert EBZ Energie Wärmepumpen, Photovoltaik, Speicher und Energiemanagement in "
                    "Kärnten und der Steiermark und rechnet den Strombedarf vor jedem Angebot mit den Daten des "
                    "Hauses durch. Die Zahlen in diesem Ratgeber sind Richtwerte. Keine Rechtsberatung, "
                    "maßgeblich sind die offiziellen Förder- und Tarifbedingungen."),
    "sources": [
        ("Fraunhofer ISE: Wärmepumpen heizen auch im Altbau klimafreundlich, Presseinformation 03.11.2025 (Deutschland)",
         "https://www.ise.fraunhofer.de/de/presse-und-medien/presseinformationen/2025/waermepumpen-heizen-auch-im-altbau-klimafreundlich-forschungsprojekt-des-fraunhofer-ise-abgeschlossen.html"),
        ("Energieinstitut Vorarlberg: Die Wärmepumpe, eine Glanzleistung an Effizienz",
         "https://www.energieinstitut.at/privatpersonen/heizung-und-lueftung/die-waermepumpe-eine-glanzleistung-an-effizienz"),
        ("Statistik Austria: Energieverwendung privater Haushalte 2025 bis 2026",
         "https://www.statistik.at/fileadmin/publications/Energieverwendung_2025-2026_bf.pdf"),
        ("E-Control: Strom- und Gaspreismonitor November 2026", "https://www.e-control.at/preismonitor"),
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/de/marktpreis/"),
        ("EU-Kommission JRC: PVGIS, Photovoltaik-Ertrag 10 kWp Villach (PVGIS-SARAH2)",
         "https://re.jrc.ec.europa.eu/pvg_tools/de/"),
        ("VERBUND: Strom-Wärmepumpentarif, Folder 01/2026",
         "https://a.storyblok.com/f/283344/x/574c803726/verbund_waermepumpe-tariffolder_01_2026_neu.pdf"),
        ("Energie Agentur Steiermark (ich tu's): Ratgeber Wärmepumpe",
         "https://www.ich-tus.steiermark.at/cms/dokumente/12957506_179561470/e9f2f9c9/Waermepumpe_Ratgeber.pdf"),
        ("HTW Berlin: Solarstromoptimiertes Energiemanagement von Wärmepumpen (2023, Deutschland)",
         "https://solar.htw-berlin.de/wp-content/uploads/WIDERA-2023-Solarstromoptimiertes-Energiemanagement-von-Waermepumpen.pdf"),
        ("Verbraucherzentrale: Wie umweltfreundlich und effizient ist eine Wärmepumpe? (Deutschland)",
         "https://www.verbraucherzentrale.de/wissen/energie/heizen-und-warmwasser/klimaschutz-wie-umweltfreundlich-und-effizient-ist-eine-waermepumpe-113947"),
        ("Klima- und Energiefonds: Leitfaden Energiemanagement private Haushalte 2026",
         "https://www.umweltfoerderung.at/fileadmin/user_upload/umweltfoerderung/private/Energiemanagement/ems_private_leitfaden.pdf"),
    ],
    "related": [
        ("waermepumpe", "Wärmepumpe für Kärnten und die Steiermark"),
        ("/kosten-einer-waermepumpe/", "Kosten einer Wärmepumpe"),
        ("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"),
        ("/waermepumpe-mit-heizkoerpern/", "Wärmepumpe mit Heizkörpern"),
    ],
    "cta": {
        "h3": "Stromverbrauch vorab berechnen",
        "text": "Wir rechnen Wärmebedarf, Jahresarbeitszahl und PV-Anteil für Ihr Haus ehrlich durch.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Wärmepumpe mit kalkulierbarem Stromverbrauch",
    "final_text": ("Kostenlose Erstberatung zu Wärmepumpe, Photovoltaik, Speicher und Energiemanagement, mit "
                   "transparenten Zahlen und einem Ansprechpartner aus Villach."),
}
