"""Ratgeber: Warmwasser mit Photovoltaik (Heizstab, Heizstab-Regler, Wärmepumpenboiler, EMS).

Neuer Artikel (kein WordPress-Vorgänger), erstellt 2026-11-19.
Ziel-Keywords (Google Ads, Österreich, 19.11.2026): heizstab pv überschuss 170, warmwasser mit photovoltaik 90,
warmwasser photovoltaik heizstab 70.

Faktenbasis: Recherche vom 19.11.2026 mit Quellen (Statistik Austria, Energieinstitut Vorarlberg, E-Control
Preismonitor November 2026, OeMAG, WKO Heizöl, NÖ Landesregierung Legionellen-Infoblatt, Klimafonds-Leitfaden
EMS 2026, Herstellerdatenblätter my-PV, Fronius, SMARTFOX, Stiebel Eltron, dazu deutsche Quellen
Verbraucherzentrale, co2online, Stiftung Warentest, HTW Berlin, jeweils als deutsch gekennzeichnet).
Eigene Rechnungen: Energie = Liter x K x 0,001163 kWh (Statistik Austria); ct-Werte je kWh aus Jahrespreis/3.500 kWh
bzw. 15.000 kWh (E-Control), Wärmepreis = Brennstoffpreis / Nutzungsgrad (Statistik Austria).
Nicht behauptet: österreichische Preisspanne für Heizstab-Regler (nur co2online DE), Förderung für
Wärmepumpenboiler 2026 (nicht belegt), Heizstab-Regler als EMS-Förderkomponente (nur Auslegung).
EBZ-Beleg: Referenz Wohnhaus Wien (my-PV-Regler, Heizstab aus PV-Überschuss, Sigenergy, 20 kWh, Wallbox).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "warmwasser-mit-photovoltaik",
    "path": "/warmwasser-mit-photovoltaik/",
    "cluster": "Wärmepumpe und Heizen",
    "title": "Heizstab PV-Überschuss: Warmwasser mit Photovoltaik | EBZ",
    "description": ("Warmwasser mit Photovoltaik: Ein 3-kW-Heizstab erhitzt 200 Liter in rund 3,5 Stunden mit "
                    "PV-Überschuss. Kosten, Regler, Wärmepumpenboiler, Legionellen und EMS-Förderung 2026."),
    "eyebrow": "Warmwasser · Photovoltaik und Heizstab",
    "crumb_label": "Warmwasser mit Photovoltaik",
    "h1": "Warmwasser mit Photovoltaik: So machen Heizstab und Regler aus PV-Überschuss heißes Wasser",
    "lead": ("Für jede Kilowattstunde, die Sie mittags einspeisen, bekommen Sie den OeMAG-Marktpreis, im Oktober "
             "2026 waren das 14,874 Cent. Erhitzt derselbe Strom Ihr Warmwasser, sparen Sie den Preis der "
             "Energie, die Sie sonst dafür kaufen. Dieser Ratgeber rechnet ehrlich vor, wann sich das lohnt, "
             "welche Technik es gibt und worauf Sie bei Hygiene und Förderung achten müssen."),
    "chips": [
        "200 l von 15 auf 60 °C: <b>rund 10,5 kWh</b>",
        "Regler stufenlos: <b>0 bis 3 kW</b> (bis 9 kW)",
        "Speicher: <b>60 °C</b> gegen Legionellen",
        "EMS-Förderung: <b>bis 600 €</b>",
    ],
    "date_published": "2026-11-19",
    "date_modified": "2026-11-19",
    "hero_img": "ems",
    "hero_alt": "Technikraum mit Energiemanagement-Display, Batteriespeicher und Wechselrichter einer Photovoltaikanlage",

    "tldr": [
        "Ein Heizstab mit PV-Regler im bestehenden Boiler macht aus Sonnenstrom Wärme. 200 Liter von 15 auf "
        "60 °C brauchen rund 10,5 kWh, ein 3-kW-Heizstab schafft das in rund 3,5 Sonnenstunden.*",
        "Ersetzt der Heizstab Netzstrom, ist jede Kilowattstunde rund doppelt so viel wert wie die Einspeisung "
        "(Haushaltsstrom in Kärnten und der Steiermark rund 28 bis 35 Cent, OeMAG Oktober 2026: 14,874 Cent).*",
        "Wird das Wasser sonst mit Gas bereitet, ist der Vorteil beim aktuellen Marktpreis klein, bei Heizöl "
        "deutlich. Ein stufenloser Regler nutzt nur den echten Überschuss, ohne Strom aus dem Netz zu ziehen.",
        "Im Sommerhalbjahr kann PV-Überschuss das Warmwasser fast allein bereiten, im Winter kaum. Ein "
        "Wärmepumpenboiler macht aus 1 kWh Strom rund 2,5 bis 4 kWh Wärme, kostet aber 3.000 bis 4.000 Euro.",
        "Gegen Legionellen gehört der Speicher regelmäßig auf 60 °C. Die EMS-Förderung (bis 600 Euro) zählt "
        "elektrische Warmwasserbereitung als steuerbare Komponente, aber nur in bestimmten Kombinationen.",
    ],
    "kpis": [
        ("rund 10,5 kWh", "200 l von 15 auf 60 °C*"),
        ("0 bis 3 kW", "stufenlos geregelter Heizstab"),
        ("14,874 ct", "OeMAG-Marktpreis Oktober 2026"),
        ("28 bis 35 ct", "Haushaltsstrom Kärnten und Steiermark*"),
    ],

    "sections": [
        ("So wird PV-Überschuss zu warmem Wasser", "funktion", f"""
<p><b>Ein Heizstab im Warmwasserspeicher wandelt Strom fast vollständig in Wärme um. Ein PV-Regler gibt ihm
genau so viel Leistung, wie die Photovoltaikanlage gerade übrig hat.</b> Was Haushalt und
{a('batteriespeicher', 'Batteriespeicher')} nicht brauchen, landet so im Boiler statt im Netz. Der Speicher
wird zur Wärmebatterie: Das Wasser, das mittags warm wird, steht am Abend und am nächsten Morgen zur
Verfügung.</p>
<p>Die Energie lässt sich einfach berechnen: Ein Liter Wasser braucht pro Grad Erwärmung 1,163 Wattstunden
(so rechnet auch Statistik Austria). Daraus ergibt sich:</p>
{A.table(
    ["Speicher", "Erwärmung", "Energie*", "Dauer mit 3-kW-Heizstab*"],
    [
        ["200 Liter", "15 auf 60 °C", "rund 10,5 kWh", "rund 3,5 Stunden"],
        ["300 Liter", "15 auf 60 °C", "rund 15,7 kWh", "rund 5,2 Stunden"],
        ["1 Person, 43 Liter am Tag", "10 auf 60 °C", "rund 910 kWh im Jahr", ""],
    ],
    hl_cols=(2,),
)}
<p>Drei Wege führen zum Ziel: ein <b>Heizstab mit eigenem PV-Regler</b>, ein Heizstab, den das
{a('ems', 'Energiemanagementsystem')} ansteuert, oder ein <b>Wärmepumpenboiler</b>, der über einen
PV-Eingang Überschuss bevorzugt nutzt. Die ersten beiden sind meist im bestehenden Boiler nachrüstbar.</p>
"""),
        ("Lohnt sich das? Einspeisen oder Wasser heizen", "rechnung", f"""
<p><b>Entscheidend ist, womit Sie Ihr Warmwasser heute bereiten.</b> Jede Kilowattstunde im Heizstab fehlt bei
der Einspeisung. Dafür sparen Sie den Brennstoff, den Sie sonst kaufen. Die Verbraucherzentrale
Rheinland-Pfalz bringt es auf eine Faustregel: Liegt der Preis des Brennstoffs je Kilowattstunde über der
Einspeisevergütung, kann sich ein Heizstab lohnen.</p>
{A.table(
    ["Warmwasser heute mit", "Wert von 1 kWh Wärme*", "Vergleich mit Einspeisung (14,874 ct)"],
    [
        ["Strom aus dem Netz (Elektroboiler)", "rund 28 bis 35 ct", "rund doppelt so viel wert"],
        ["Heizöl (1,788 € je Liter)", "rund 20,6 ct", "lohnt sich meist"],
        ["Erdgas", "rund 12 bis 17 ct", "etwa gleich, Grundgebühr bleibt"],
        ["Fernwärme", "je nach Anbieter", "individuell rechnen"],
    ],
    hl_cols=(1,),
)}
{A.box("Der OeMAG-Marktpreis schwankt jeden Monat: Juli 2026 waren es 6,146 Cent, September 10,168 Cent, "
       "Oktober 14,874 Cent. In Monaten mit niedrigem Marktpreis lohnt der Heizstab auch gegenüber Gas. "
       f"Aktuelle Werte: {a('marktpreis', 'Marktpreis 2026')}.",
       label="Gut zu wissen:")}
<p>Stromwerte: Jahrespreis für 3.500 kWh laut E-Control-Preismonitor November 2026 (Kelag, Energie
Klagenfurt, Energie Steiermark, Energie Graz), geteilt durch die Menge. Gas: Jahrespreis für 15.000 kWh
derselben Anbieter, umgerechnet mit 91,5 % Nutzungsgrad, Heizöl mit 10 kWh je Liter und 86,9 % Nutzungsgrad
(Werte von Statistik Austria und Verbraucherzentrale).</p>
"""),
        ("Wie viel Warmwasser braucht ein Haushalt?", "bedarf", f"""
<p><b>Rund 30 bis 50 Liter warmes Wasser verbraucht eine Person am Tag, dafür sind bis zu 1.000 kWh Energie
im Jahr nötig</b> (Energieinstitut Vorarlberg). Laut Statistik Austria entfallen im Ein- und
Zweifamilienhaus durchschnittlich 3.319 kWh im Jahr auf Warmwasser, das sind 11,4 % der gesamten
Energieverwendung des Haushalts.</p>
{A.table(
    ["Haushalt", "Strombedarf fürs Warmwasser pro Jahr*"],
    [
        ["1 Person", "300 bis 700 kWh"],
        ["2 Personen", "600 bis 1.400 kWh"],
        ["3 Personen", "900 bis 2.100 kWh"],
        ["4 Personen", "1.200 bis 2.800 kWh"],
    ],
    hl_cols=(1,),
)}
<p>Spanne von niedrigem bis sehr hohem Verbrauch laut Verbraucherzentrale Rheinland-Pfalz (elektrische
Warmwasserbereitung). Zum Vergleich: Eine Photovoltaikanlage mit 10 kWp erzeugt in Kärnten und der
Steiermark ein Vielfaches davon, ein großer Teil fällt aber im Sommer an. Wie viel davon übrig ist, zeigt
{a('/pv-anlage-kwp-groessen/', 'PV-Anlage: welche kWp-Größe passt')}.</p>
"""),
        ("Heizstab-Regler im Vergleich: stufenlos oder gestuft", "regler", f"""
<p><b>Ein stufenloser Regler folgt dem Überschuss Watt für Watt. Ein einfaches Relais schaltet die volle
Heizstab-Leistung ein, auch wenn nur ein Teil davon übrig ist.</b> Den Rest liefert dann das Netz. Für
Anlagen mit wechselndem Überschuss ist deshalb ein stufenloser oder fein gestufter Regler die bessere
Wahl.</p>
{A.table(
    ["Gerät (Hersteller)", "Leistung", "Regelung", "Ansteuerung"],
    [
        ["AC ELWA 2 (my-PV, Oberösterreich)", "0 bis 3.500 W", "stufenlos, Heizstab und Regler in einem",
         "Modbus TCP, http, RS485, PWM"],
        ["AC THOR / AC THOR 9s (my-PV)", "0 bis 3 kW / 0 bis 9 kW", "stufenlos, für vorhandene Heizstäbe",
         "Modbus, my-PV WiFi Meter, EMS"],
        ["Ohmpilot (Fronius)", "3 kW / 9 kW", "stufenlos (Pulsweitenmodulation)",
         "Modbus RTU, LAN, WLAN, SG Ready für Wärmepumpe"],
        ["Booster 3K (SMARTFOX)", "3 kW, mit Extension 9 kW", "stufenlos", "LAN, WLAN, Modbus"],
        ["Pro Heater 6K (SMARTFOX)", "220 W bis 6 kW", "15 Stufen", "SMARTFOX"],
    ],
    hl_cols=(1,),
)}
<p>Auswahl verbreiteter Geräte, Angaben laut Herstellern (Stand November 2026), ohne Anspruch auf
Vollständigkeit. Die Regler von my-PV und Fronius sowie der SMARTFOX Booster haben ein Legionellenprogramm. Welcher passt, hängt vom
Wechselrichter, vom vorhandenen Boiler und davon ab, ob ein {a('ems', 'Energiemanagementsystem')} den Heizstab
mitsteuern soll. Bei einem {a('/sigenergy/', 'Sigenergy-System')} lassen sich Verbraucher zum Beispiel über
die App und Schaltausgänge einbinden.</p>
{A.cta("Passt ein Heizstab in Ihren Boiler?",
       "Wir prüfen Boiler, Wechselrichter und Überschuss bei Ihnen vor Ort und sagen ehrlich, ob sich der "
       "Heizstab rechnet oder ob ein Wärmepumpenboiler besser passt.",
       secondary=("ems", "Energiemanagementsystem"))}
"""),
        ("Wärmepumpenboiler oder Solarthermie: die Alternativen", "alternativen", f"""
<p><b>Ein Wärmepumpenboiler holt Wärme aus der Raumluft und macht aus 1 kWh Strom rund 2,5 bis 4 kWh
Wärme</b> (Jahresarbeitszahl laut Verbraucherzentrale). Ein Heizstab schafft genau 1 zu 1. Dafür ist der
Heizstab im bestehenden Boiler deutlich günstiger.</p>
{A.table(
    ["", "Heizstab mit PV-Regler", "Wärmepumpenboiler", "Solarthermie"],
    [
        ["Aus 1 kWh Strom", "rund 1 kWh Wärme", "rund 2,5 bis 4 kWh Wärme", "keine Stromumwandlung"],
        ["Anschaffung*", "rund 1.000 bis 1.500 € bei vorhandener PV (Deutschland)",
         "rund 3.000 bis 4.000 €", "rund 6.000 bis 10.000 € (Deutschland)"],
        ["Platz", "im bestehenden Boiler", "Raum ab 20 m³, kühlt und entfeuchtet ihn", "Kollektoren am Dach, Leitungen"],
        ["Winter", "kaum Überschuss", "läuft ganzjährig effizient", "geringer Ertrag"],
        ["Ideal für", "vorhandene PV mit Überschuss", "Austausch eines Elektroboilers", "Neubau ohne PV-Fläche"],
    ],
    hl_cols=(1,),
)}
<p>Preise: Energieinstitut Vorarlberg (Wärmepumpenboiler), co2online und Verbraucherzentrale (Heizstab und
Solarthermie, deutsche Marktpreise). Ein Wärmepumpenboiler wie der Stiebel Eltron WWK 302 erreicht laut
Datenblatt einen COP von 2,91 und 45 dB(A) in einem Meter Abstand. Viele Modelle haben einen PV-Eingang und
nutzen bevorzugt Überschuss. Heizen Sie bereits mit einer {a('waermepumpe', 'Wärmepumpe')}, übernimmt diese
meist auch das Warmwasser, siehe {a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}.</p>
"""),
        ("Sommer und Winter: Was realistisch ist", "jahreszeit", f"""
<p><b>Im Sommerhalbjahr kann PV-Überschuss das Warmwasser weitgehend allein bereiten, im Winter reicht er
selten.</b> Eine Simulation der HTW Berlin (Deutschland, 2013) kam für ein Einfamilienhaus mit 5 kW
Photovoltaik und 200-Liter-Speicher auf mehr als 80 % solaren Anteil am Warmwasser über das Jahr. Für
Kärnten und die Steiermark gibt es keine vergleichbare aktuelle Auswertung. Die Größenordnung spricht aber
dafür, dass eine übliche Anlage ab 10 kWp im Sommer genug Überschuss fürs Warmwasser liefert.</p>
{A.box("Ein Gas- oder Ölkessel, der im Sommer nur für Warmwasser anspringt, läuft oft taktend mit "
       "schlechtem Wirkungsgrad. Übernimmt der Heizstab im Sommer, kann der Kessel ruhen. Im Winter heizt "
       "wieder die Hauptheizung, der Heizstab hilft an sonnigen Tagen mit.",
       label="Praxis-Tipp:")}
"""),
        ("Legionellen: 60 °C gehören dazu", "hygiene", f"""
<p><b>Legionellen vermehren sich bevorzugt zwischen 25 und 45 °C, erst über 60 °C sterben sie ab.</b> Das
Infoblatt der NÖ Landesregierung empfiehlt nach ÖNORM B 5019 Warmwasser von mindestens 55 °C im ganzen
Leitungsnetz, das Energieinstitut Vorarlberg 60 °C im Speicher. Ansteckend ist nur das Einatmen von
Wassernebel, etwa beim Duschen, nicht das Trinken.</p>
<ul>
  <li><b>Legionellenprogramm nutzen:</b> Regler wie my-PV, Fronius Ohmpilot oder SMARTFOX Booster heizen in einstellbaren Abständen auf 60 °C, bei
  my-PV ab Werk alle 7 Tage (muss aktiviert werden).</li>
  <li><b>Mindesttemperatur einstellen:</b> Reicht der Überschuss nicht, heizt der Regler aus dem Netz nach,
  damit das Wasser nie zu kalt wird.</li>
  <li><b>Höher speichern, wenn Sonne da ist:</b> Bei Überschuss darf der Speicher heißer werden, dann wird
  mehr Sonnenenergie gespeichert. Ein Mischventil schützt vor Verbrühung.</li>
</ul>
"""),
        ("Kosten und Förderung 2026", "foerderung", f"""
<p><b>Ein Heizstab mit PV-Regler kostet bei vorhandener Photovoltaik in Deutschland rund 1.000 bis 1.500 Euro
inklusive Einbau</b> (co2online, April 2025). Für Österreich gibt es keine neutrale Preisübersicht, die
Größenordnung ist ähnlich. Den genauen Preis nennen wir nach der Besichtigung.</p>
<ul>
  <li><b>EMS-Förderung des Klimafonds:</b> 50 % der Kosten, maximal 600 Euro (plus 100 Euro bei Teilnahme an
  der Begleitforschung), Registrierung vor der ersten Rechnung, bis 15. April 2027 oder solange Budget da
  ist. Elektrische Warmwasserbereitung mit Warmwasserspeicher zählt als steuerbare Komponente, gefördert
  werden aber nur bestimmte Kombinationen: zum Beispiel Batteriespeicher und Warmwasser, Ladestelle und
  Warmwasser oder PV, Batteriespeicher und Warmwasser. <b>PV und Warmwasser allein stehen nicht in der
  Liste.</b> Reine Eigenverbrauchsoptimierung ist nicht förderfähig, Sie verpflichten sich für fünf Jahre
  auf eine Option wie einen dynamischen Tarif oder eine Energiegemeinschaft. Details:
  {a('/ems-foerderung/', 'EMS-Förderung 2026')}.</li>
  <li><b>Wärmepumpenboiler:</b> Eine eigene Förderung von Bund, Kärnten oder Steiermark ist uns für 2026
  nicht bekannt. Die steirische Richtlinie zum Heizungstausch nennt Brauchwasser-Wärmepumpen nicht.</li>
  <li><b>Photovoltaik und Speicher:</b> Aktuelle Landesförderungen für Kärnten und die Steiermark finden Sie
  unter {a('foerderungen', 'Förderungen 2026')}.</li>
</ul>
"""),
        ("Aus der Praxis: Wohnhaus in Wien", "praxis", f"""
<p>Beim {a('/referenzen/projekt-pv-wien/', 'Wohnhaus in Wien')} haben wir eine 10,92-kWp-Anlage mit
20-kWh-Speicher, 11-kW-Wallbox und einem my-PV-Regler kombiniert. Der Regler leitet PV-Überschuss stufenlos
in den Heizstab des Warmwasserspeichers, statt ihn zum Marktpreis einzuspeisen. Die Anlage liefert rund
12.000 kWh im Jahr.* Wechselrichter, Speicher und Wallbox stammen aus einem
{a('/sigenergy/', 'Sigenergy-System')}, der my-PV-Regler nimmt den Überschuss fürs Warmwasser.</p>
"""),
        ("Fazit: Günstiger Einstieg, wenn Überschuss da ist", "fazit", f"""
<p>Ein Heizstab mit stufenlosem PV-Regler ist der günstigste Weg, Sonnenstrom in Wärme zu verwandeln. Am
meisten bringt er, wenn das Warmwasser heute elektrisch oder mit Öl bereitet wird und die PV-Anlage im
Sommer viel einspeist. Wer einen alten Elektroboiler ohnehin tauschen muss, fährt mit einem Wärmepumpenboiler
langfristig effizienter. Und wer ein Energiemanagementsystem plant, bindet das Warmwasser gleich mit ein und
kann die EMS-Förderung nutzen.</p>
<p><small>*Richtwerte und eigene Berechnungen auf Basis der genannten Quellen, ohne Speicher- und
Leitungsverluste. Energiepreise Stand November 2026, OeMAG-Marktpreis Oktober 2026; die Werte ändern sich
laufend. Preise aus Deutschland sind als solche gekennzeichnet.</small></p>
{A.cta("Warmwasser mit Sonnenstrom, ehrlich gerechnet",
       "Wir sehen uns Boiler, Photovoltaik und Verbrauch an und rechnen durch, ob Heizstab, "
       "Wärmepumpenboiler oder Energiemanagement bei Ihnen am meisten bringt.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("ems", "Mehr zum EMS"))}
"""),
    ],

    "partner": {
        "h2": "Warmwasser, Speicher und Photovoltaik aus einer Hand",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie plant und installiert Photovoltaik, Batteriespeicher, Wärmepumpen und "
                 "Energiemanagement in Kärnten und der Steiermark, mit zertifizierten Fachkräften und einem "
                 "festen Ansprechpartner von der Planung bis zur Übergabe. Wir binden Heizstab, Boiler und "
                 "Wallbox so ein, dass der Überschuss dort landet, wo er am meisten wert ist."),
        "grid": [
            ("Ehrliche Rechnung", "Einspeisen oder selbst nutzen, mit Ihren Preisen."),
            ("Herstellerunabhängig", "Regler und Boiler passend zu Ihrer Technik."),
            ("Hygiene mitgedacht", "Legionellenprogramm und Mindesttemperatur eingestellt."),
            ("Förderung im Blick", "EMS-Förderung in der richtigen Reihenfolge."),
        ],
    },

    "faq": [
        ("Lohnt sich ein Heizstab für PV-Überschuss?",
         "Ja, wenn Sie das Warmwasser heute mit Strom oder Heizöl bereiten und die PV-Anlage im Sommer viel "
         "einspeist. Eine Kilowattstunde Haushaltsstrom kostet in Kärnten und der Steiermark rund 28 bis 35 Cent, "
         "die Einspeisung brachte im Oktober 2026 14,874 Cent. Bei Gas ist der Vorteil beim aktuellen Marktpreis "
         "gering."),
        ("Wie lange braucht ein Heizstab, um 200 Liter zu erhitzen?",
         "200 Liter von 15 auf 60 °C brauchen rund 10,5 kWh. Ein 3-kW-Heizstab schafft das bei vollem Überschuss "
         "in rund 3,5 Stunden, ein 300-Liter-Speicher braucht rund 5,2 Stunden. Bei weniger Überschuss regelt ein "
         "stufenloser Regler die Leistung herunter und heizt entsprechend länger."),
        ("Welche Leistung sollte der Heizstab haben?",
         "Für Einfamilienhäuser sind 3 kW einphasig üblich, stufenlos geregelt ab wenigen Watt. Bei großen "
         "Anlagen und Speichern gibt es dreiphasige Regler bis 9 kW, etwa AC THOR 9s von my-PV oder den Fronius "
         "Ohmpilot. Entscheidend ist, dass der Regler nur echten Überschuss nutzt."),
        ("Heizstab oder Wärmepumpenboiler: was ist besser?",
         "Der Heizstab ist günstiger und im bestehenden Boiler nachrüstbar, macht aber aus 1 kWh Strom nur 1 kWh "
         "Wärme. Ein Wärmepumpenboiler schafft rund 2,5 bis 4 kWh und läuft auch im Winter effizient, kostet aber "
         "rund 3.000 bis 4.000 Euro und braucht einen Raum ab 20 m³."),
        ("Brauche ich dafür ein Energiemanagementsystem?",
         "Nicht zwingend: Regler wie my-PV, Fronius Ohmpilot oder SMARTFOX messen den Überschuss selbst. Ein EMS "
         "lohnt sich, wenn mehrere Verbraucher um den Überschuss konkurrieren, etwa Speicher, Wallbox und "
         "Warmwasser, oder wenn Sie die EMS-Förderung nutzen wollen."),
        ("Gibt es eine Förderung für den Heizstab?",
         "Eine eigene Heizstab-Förderung gibt es nicht. Die EMS-Förderung des Klimafonds (50 %, maximal 600 Euro) "
         "zählt elektrische Warmwasserbereitung mit Speicher als steuerbare Komponente, aber nur in bestimmten "
         "Kombinationen, etwa mit Batteriespeicher oder Ladestelle. PV und Warmwasser allein reichen nicht."),
        ("Wie verhindere ich Legionellen im Boiler?",
         "Den Speicher regelmäßig auf 60 °C bringen, die Regler haben dafür ein Legionellenprogramm (bei my-PV ab "
         "Werk alle 7 Tage, muss aktiviert werden). Im ganzen Leitungsnetz sollten mindestens 55 °C erreicht "
         "werden. Ansteckend ist nur eingeatmeter Wassernebel, nicht das Trinken."),
        ("Kann ich den Heizstab in meinen bestehenden Boiler einbauen?",
         "Oft ja, wenn der Boiler eine passende freie Öffnung für einen Heizstab hat oder ein vorhandener "
         "Heizstab ersetzt werden kann. Manche Regler wie der my-PV AC THOR steuern auch einen bereits "
         "eingebauten Heizstab. Ob Ihr Boiler passt, sehen wir bei der Besichtigung."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Mit zertifizierten Fachkräften plant und "
                    "installiert EBZ Energie Photovoltaik, Batteriespeicher, Wärmepumpen und Energiemanagement in "
                    "Kärnten und der Steiermark, darunter Anlagen, die PV-Überschuss in Warmwasser lenken. Preise "
                    "und Rechnungen in diesem Ratgeber sind Richtwerte. Keine Rechtsberatung, maßgeblich sind die "
                    "offiziellen Förderbedingungen."),
    "sources": [
        ("Statistik Austria: Energieverwendung privater Haushalte 2025 bis 2026",
         "https://www.statistik.at/fileadmin/publications/Energieverwendung_2025-2026_bf.pdf"),
        ("Energieinstitut Vorarlberg: Warmwasser effizient und umweltfreundlich aufbereiten",
         "https://www.energieinstitut.at/privatpersonen/haustechnik-energieversorgung/warmwasser-effizient-und-umweltfreundlich-aufbereiten"),
        ("E-Control: Strom- und Gaspreismonitor November 2026",
         "https://www.e-control.at/preismonitor"),
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/de/marktpreis/"),
        ("WKO: Heizölpreise", "https://www.wko.at/oe/industrie/energierohstoff-kraftstoff/kraftstoffpreise"),
        ("Amt der NÖ Landesregierung: Infoblatt Legionellen",
         "https://www.noe.gv.at/noe/Gesundheitsvorsorge-Forschung/Infoblatt_Legionellen_oeffentliche_Einrichtungen_20260909.pdf"),
        ("Klima- und Energiefonds: Leitfaden Energiemanagement private Haushalte 2026",
         "https://www.umweltfoerderung.at/fileadmin/user_upload/umweltfoerderung/private/Energiemanagement/ems_private_leitfaden.pdf"),
        ("my-PV: AC ELWA 2", "https://www.my-pv.com/de/produkte/ac-elwa-2"),
        ("Fronius: Ohmpilot, technische Daten",
         "https://www.fronius.com/de-de/germany/solarenergie/installateure-partner/technische-daten/alle-produkte/l%C3%B6sungen/fronius-w%C3%A4rmel%C3%B6sung/fronius-ohmpilot/fronius-ohmpilot"),
        ("SMARTFOX: Datenblatt Booster", "https://smartfox.at/wp-content/uploads/2026/07/Datenblatt-Booster.pdf"),
        ("Verbraucherzentrale Rheinland-Pfalz: Warmwasser", "https://verbraucherzentrale-rlp.de/node/77008"),
        ("Verbraucherzentrale: Warmwasser mit der Wärmepumpe",
         "https://www.verbraucherzentrale.de/wissen/energie/heizen-und-warmwasser/wie-erzeuge-ich-warmwasser-wenn-ich-mit-einer-waermepumpe-heize-114880"),
        ("co2online: PV-Heizstab", "https://www.co2online.de/modernisieren-und-bauen/photovoltaik/pv-heizstab/"),
        ("HTW Berlin: Chancen für den Wärmemarkt (2013)",
         "https://solar.htw-berlin.de/wp-content/uploads/TJADEN-2013-Chancen-fuer-den-Waermemarkt.pdf"),
    ],
    "related": [
        ("ems", "Energiemanagementsystem: PV-Überschuss automatisch nutzen"),
        ("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"),
        ("/brauchwasserwaermepumpe/", "Brauchwasserwärmepumpe: Kosten und Effizienz"),
        ("/sigenergy/", "Sigenergy: Speicher, Wallbox und Notstrom"),
    ],
    "cta": {
        "h3": "Mehr Sonnenstrom selbst nutzen",
        "text": "Wir rechnen Heizstab, Wärmepumpenboiler und Speicher für Ihr Haus ehrlich durch.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Warmwasser mit Sonnenstrom, ehrlich gerechnet",
    "final_text": ("Kostenlose Erstberatung zu Photovoltaik, Speicher, Warmwasser und Energiemanagement, mit "
                   "transparenten Zahlen und einem Ansprechpartner aus Villach."),
}
