"""Ratgeber: Wechselrichter für die PV-Anlage (Aufgabe, Arten, Dimensionierung, Wirkungsgrad, Notstrom,
TOR Erzeuger, Lebensdauer, Tausch, Kosten).

Neuer Artikel (kein WordPress-Vorgänger), erstellt 2026-11-19.
Ziel-Keywords (Google Ads, Österreich, 19.11.2026): wechselrichter pv anlage 260, wechselrichter für pv-anlage 260,
wechselrichter photovoltaik 260, pv wechselrichter 320, wechselrichter mit speicher 320, mikrowechselrichter 210,
hybridwechselrichter 50 (Labs: hybrid wechselrichter 480), wechselrichter kosten 30, wechselrichter lebensdauer 30,
wechselrichter tauschen 10.

Faktenbasis (alle Quellen am 19.11.2026 geöffnet): TOR Stromerzeugungsanlagen Typ A Version 1.4 (E-Control, in Kraft
seit 1.6.2026: Anwendungsbereich, 3,68 kVA, AC-/DC-Kopplung, Ersatzstrom, Konformitätsnachweis, wesentliche Änderung,
Ansteuerbarkeit § 76 ElWG), wechselrichterliste.at, Klimafonds-Handlungsanleitung Netzanschluss (August 2023),
Fraunhofer ISE "Aktuelle Fakten zur Photovoltaik" (Fassung 11.11.2026), Uni Paderborn Krauter/Bendfeld 2024
(europäischer Wirkungsgrad), BFH/pv magazine (Lebensdauer), ADAC Juli 2026 (Kosten, Lebensdauer, Faustregel),
Verbraucherzentrale (Garantie), Sigenergy-Datenblätter (siehe Scratchpad sigenergy_fakten.md).
Nicht behauptet: österreichische Preisspanne für Wechselrichter (nur ADAC Deutschland), SigenStor-Preis,
Sigenergy-Eintrag in der Wechselrichterliste (nicht geprüft), Restkapazität der Sigenergy-Garantie, "offizieller Partner".
EBZ-Beleg: 8 von 10 Referenzprojekten mit Sigenergy (build/pages/referenz_projekte.py).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "wechselrichter-pv-anlage",
    "path": "/wechselrichter-pv-anlage/",
    "cluster": "Photovoltaik",
    "title": "Wechselrichter für die PV-Anlage: Arten, Größe, Kosten | EBZ",
    "description": ("Wechselrichter für die PV-Anlage: String, Hybrid oder Mikro, richtige Größe, rund 98 % "
                    "Wirkungsgrad, Lebensdauer, Tausch, Kosten und TOR-Regeln in Österreich."),
    "eyebrow": "Photovoltaik · Wechselrichter",
    "crumb_label": "Wechselrichter für die PV-Anlage",
    "h1": "Wechselrichter für die PV-Anlage: 4 Arten, die richtige Größe und was ein Tausch kostet",
    "lead": ("Der Wechselrichter macht aus dem Gleichstrom der Module Strom für Haus und Netz und entscheidet "
             "mit, ob Speicher, Notstrom und Netzanmeldung reibungslos funktionieren. Dieser Ratgeber erklärt die "
             "Gerätearten, die Auslegung, die österreichischen Netzregeln und was zu Lebensdauer und Kosten "
             "tatsächlich belegt ist."),
    "chips": [
        "Wirkungsgrad neuer Geräte: <b>um 98 %</b>",
        "einphasig höchstens <b>3,68 kVA</b> Schieflast",
        "Lebensdauer laut ADAC: <b>10 bis 15 Jahre</b>",
        "<b>8 von 10</b> EBZ-Referenzen mit Hybridsystem",
    ],
    "date_published": "2026-11-19",
    "date_modified": "2026-11-19",
    "hero_img": "speicher",
    "hero_alt": ("Weißes Sigenergy-System in einem Technikraum: Wechselrichter und Batteriemodule übereinander "
                 "gestapelt, darüber ein Kabelrohr"),

    "tldr": [
        "Der Wechselrichter wandelt Gleichstrom in netzkonformen Wechselstrom, sucht laufend den besten "
        "Arbeitspunkt der Module und trennt die Anlage bei Netzstörungen. Neue Geräte erreichen laut Fraunhofer "
        "ISE einen Wirkungsgrad um 98 %.",
        "Vier Bauarten: Stringwechselrichter, Hybridwechselrichter (mit Batterieanschluss), Mikrowechselrichter "
        "am Modul und Batteriewechselrichter für AC-gekoppelte Speicher. Wer heute mit Speicher plant, nimmt "
        "meist einen Hybridwechselrichter.",
        "Wechselrichter werden häufig etwas kleiner als die Modulleistung gewählt. In Österreich dürfen "
        "einphasige Geräte höchstens 3,68 kVA Schieflast verursachen, größere Anlagen laufen dreiphasig.",
        "Netzanschluss nur mit Geräten, die die TOR Stromerzeugungsanlagen erfüllen. Steht das Gerät in der "
        "Wechselrichterliste der Netzbetreiber, gilt der Konformitätsnachweis als erbracht.",
        "Rechnen Sie mit einem Tausch im Anlagenleben: Der ADAC nennt 10 bis 15 Jahre Lebensdauer, in einer "
        "Schweizer Auswertung liefen mehr als 65 % der Geräte 15 Jahre ohne ertragsrelevanten Fehler.",
    ],
    "kpis": [
        ("um 98 %", "Wirkungsgrad neuer PV-Wechselrichter"),
        ("3,68 kVA", "max. Schieflast einphasig (TOR)"),
        ("über 65 %", "ohne ertragsrelevanten Fehler bis Jahr 15"),
        ("8 von 10", "EBZ-Referenzen mit Sigenergy-Hybridsystem"),
    ],

    "sections": [
        ("Was macht der Wechselrichter in der PV-Anlage?", "aufgabe", f"""
<p><b>PV-Module erzeugen Gleichstrom. Haushalt und Stromnetz arbeiten mit 50-Hertz-Wechselstrom. Der
Wechselrichter wandelt den einen in den anderen um</b> (Fraunhofer ISE). Damit ist er das Bauteil, über das
jede Kilowattstunde Ihrer {a('photovoltaik', 'Photovoltaikanlage')} läuft. Dazu kommen drei weitere Aufgaben:</p>
<ul>
  <li><b>Bestmöglicher Arbeitspunkt:</b> Ein MPP-Tracker sucht laufend die Kombination aus Spannung und Strom,
  bei der die Module am meisten liefern. Jeder Tracker regelt seinen Modulstrang für sich, das ist wichtig,
  wenn Dachflächen unterschiedlich ausgerichtet sind, etwa Ost und West.</li>
  <li><b>Netzschutz:</b> Der Wechselrichter überwacht Spannung und Frequenz und trennt die Anlage bei
  Störungen vom Netz. Welche Werte er einhalten muss, regeln in Österreich die TOR Stromerzeugungsanlagen
  (siehe unten).</li>
  <li><b>Steuerung und Daten:</b> Moderne Geräte zeigen Ertrag und Verbrauch in einer App, steuern einen
  {a('batteriespeicher', 'Batteriespeicher')} und arbeiten mit einem
  {a('ems', 'Energiemanagementsystem')} zusammen.</li>
</ul>
<p>Laut Fraunhofer ISE bieten viele Hersteller in Europa inzwischen Wechselrichter mit integrierter
Lichtbogenerkennung an, die im Fehlerfall den Gleichstrom unterbrechen. Montiert werden sollen Wechselrichter
außerhalb von Wohn- und Schlafräumen, weil sie im Betrieb hörbare Geräusche machen können.</p>
"""),
        ("Wechselrichter-Arten: String, Hybrid, Mikro und Batteriewechselrichter", "arten", f"""
<p><b>Welche Bauart passt, hängt vor allem von zwei Fragen ab: Kommt ein Speicher dazu, und ist das Dach
verschattet?</b> Die vier Bauarten im Überblick:</p>
{A.table(
    ["Bauart", "So arbeitet sie", "Passt gut zu"],
    [
        ["Stringwechselrichter", "ein zentrales Gerät für einen oder mehrere Modulstränge",
         "unverschattete Dächer ohne Speicher"],
        ["Hybridwechselrichter", "Stringwechselrichter mit zusätzlichem Batterieanschluss, Speicher "
         "gleichstromseitig gekoppelt", "Neuanlagen mit Speicher, Notstrom, E-Auto"],
        ["Mikrowechselrichter", "ein kleines Gerät je Modul (oder je zwei bis vier Module)",
         "verschattete oder zerklüftete Flächen, Balkonkraftwerke"],
        ["Batteriewechselrichter (AC-gekoppelt)", "eigenes Gerät nur für den Speicher, an der "
         "Wechselstromseite angeschlossen", "Speicher-Nachrüstung, wenn der alte Wechselrichter bleiben soll"],
    ],
    hl_cols=(0,),
)}
<h3>Hybridwechselrichter: der Standard bei Anlagen mit Speicher</h3>
<p>Beim Hybridwechselrichter hängen Module und Speicher am selben Gerät. Die TOR nennt das ein
gleichstromgekoppeltes System. Der Sonnenstrom lädt den Speicher, ohne vorher in Wechselstrom umgewandelt zu
werden. Viele Hybridgeräte können zusätzlich eine Not- oder Ersatzstromversorgung aufbauen. Ein Beispiel ist
der {a('/sigenergy/', 'Sigenergy SigenStor')}: Wechselrichter, Batteriesteuerung, Energiemanagement und
optional ein Gleichstrom-Ladegerät fürs E-Auto stecken in einem stapelbaren Turm.</p>
<h3>AC-Kopplung: wenn schon ein Wechselrichter da ist</h3>
<p>Beim wechselstromgekoppelten System bekommt der Speicher einen eigenen Batteriewechselrichter, der
bestehende PV-Wechselrichter bleibt. Das ist bei der Nachrüstung oft der einfachere Weg. Ist der alte
Wechselrichter ohnehin in die Jahre gekommen, kann der Tausch auf ein Hybridgerät sinnvoller sein. Beide Wege
erklärt {a('/pv-speicher-nachruesten/', 'PV-Speicher nachrüsten')}.</p>
<h3>Mikrowechselrichter und Optimierer</h3>
<p>Mikrowechselrichter sitzen direkt am Modul, ein verschattetes Modul bremst dann nicht den ganzen Strang.
Eine Auswertung der Berner Fachhochschule über 15 Jahre fand allerdings, dass Wechselrichter mit
Leistungsoptimierern im Schnitt früher ausfallen.</p>
"""),
        ("Wie groß muss der Wechselrichter sein? DC/AC-Verhältnis", "dimensionierung", f"""
<p><b>Ein Wechselrichter muss nicht so groß sein wie die Modulleistung.</b> Module erreichen ihre
Nennleistung nur unter idealen Bedingungen und kurzzeitig. Deshalb werden Wechselrichter laut Fraunhofer ISE
häufig unterdimensioniert: In Deutschland liegt die Modulleistung (DC) im Mittel knapp 10 % über der
Wechselrichterleistung (AC). Das Verhältnis der beiden heißt DC/AC-Verhältnis.</p>
{A.table(
    ["Anhaltspunkt", "Wert", "Quelle"],
    [
        ["Faustregel Wechselrichterleistung", "rund 80 bis 100 % der Modulleistung, z. B. 5 kWp mit 4 bis 5 kW",
         "ADAC (Deutschland)"],
        ["Mittelwert Bestand", "Modulleistung knapp 10 % über Wechselrichterleistung", "Fraunhofer ISE"],
        ["Technische Obergrenze eines Hybridgeräts", "DC/AC-Verhältnis bis 2,0 (einphasige Modelle)",
         "Sigenergy, Herstellerangabe"],
    ],
    hl_cols=(1,),
)}
<p>Die Obergrenze des Herstellers ist keine Empfehlung: Je kleiner der Wechselrichter, desto öfter kappt er
an sonnigen Mittagen. Mit Speicher sieht das anders aus, weil der Überschuss gleichstromseitig in die Batterie
fließen kann. Die passende Größe hängt deshalb von Ausrichtung, Speicher und Verbrauch ab. Welche kWp-Größe zu
Ihrem Haus passt, zeigt {a('/pv-anlage-kwp-groessen/', 'PV-Anlage: welche kWp-Größe passt')}.</p>
<h3>Einphasig oder dreiphasig: die 3,68-kVA-Grenze in Österreich</h3>
<p>Die TOR Stromerzeugungsanlagen verlangen grundsätzlich eine symmetrische dreiphasige Einspeisung.
Einphasig dürfen Anlagen nur bis zu einer resultierenden Schieflast (Unsymmetrie) von 3,68 kVA angeschlossen
werden, das gilt auch für einphasige Speicher. Für ein übliches Einfamilienhaus mit 8 bis 15 kWp heißt das in
der Praxis: dreiphasiger Wechselrichter. Manche Netzbetreiber setzen wegen bereits vorhandener Anlagen
strengere Grenzen.</p>
"""),
        ("Wirkungsgrad: maximal oder europäisch?", "wirkungsgrad", f"""
<p><b>Im Datenblatt stehen meist zwei Werte. Der maximale Wirkungsgrad gilt nur im besten Betriebspunkt. Der
europäische Wirkungsgrad bildet ab, wie oft ein Wechselrichter in Mitteleuropa in Teillast läuft, und ist
deshalb der aussagekräftigere Vergleichswert.</b></p>
<p>Er gewichtet sechs Lastpunkte: 5 % Last mit 3 %, 10 % mit 6 %, 20 % mit 13 %, 30 % mit 10 %, 50 % mit
48 % und Volllast mit 20 % (Universität Paderborn, 2024). Am stärksten zählt also der Betrieb bei halber Last.</p>
{A.table(
    ["Gerät", "Max. Wirkungsgrad", "Europ. Wirkungsgrad"],
    [
        ["Neue PV-Wechselrichter allgemein (Fraunhofer ISE)", "um 98 %", ""],
        ["Sigenergy Energy Controller, einphasig 3 bis 12 kW", "97,6 bis 98,0 %", "97,0 bis 97,4 %"],
        ["Sigenergy Energy Controller, dreiphasig 5 bis 30 kW", "98,1 bis 98,4 %", "96,1 bis 98,0 %"],
        ["Mikrowechselrichter im Labortest (Uni Paderborn 2024)", "", "Spitzenwerte rund 95 %"],
    ],
    hl_cols=(2,),
)}
<p>Ein Prozentpunkt Wirkungsgrad macht bei 10.000 kWh Jahresertrag rund 100 kWh aus.* Wichtiger als die
Kommastelle sind daher die richtige Auslegung, passende MPP-Tracker für Ihre Dachflächen und ein Gerät, das
Speicher und Verbraucher gut steuert. Bei den Mikrowechselrichtern zeigte der Paderborner Test große
Unterschiede: Einige Geräte lagen deutlich unter den Spitzenwerten.</p>
{A.cta("Welcher Wechselrichter passt zu Ihrem Dach?",
       "Wir planen Module, Wechselrichter und Speicher als ein System, mit Projektbericht mit 3D-Belegplan "
       "und Statikreport, und übernehmen die Anmeldung beim Netzbetreiber.",
       secondary=("/sigenergy/", "Sigenergy-System ansehen"))}
"""),
        ("Notstrom und Ersatzstrom: was der Wechselrichter dafür können muss", "notstrom", f"""
<p><b>Ein normaler Netzwechselrichter schaltet bei einem Stromausfall ab, auch wenn die Sonne scheint.</b> Für
Strom bei Netzausfall braucht es einen notstromfähigen Wechselrichter, einen Speicher und eine
Umschalteinrichtung, die das Haus vom Netz trennt. Den Unterschied zwischen Notstrom (einzelne Steckdose) und
Ersatzstrom (ganzes Haus) erklärt {a('/notstrom/', 'Notstrom mit Photovoltaik')} ausführlich.</p>
<p>Die TOR geben dafür den Rahmen vor:</p>
<ul>
  <li>Ersatzstromanlagen, die in die Hausinstallation einspeisen und nicht für den Netzparallelbetrieb
  ausgerüstet sind, brauchen eine <b>verriegelte Umschalteinrichtung</b> (Umschaltung mit Unterbrechung).</li>
  <li>Bei inselbetriebsfähigen Anlagen im Niederspannungsnetz kann der Netzbetreiber eine <b>vierpolige
  Abschaltung</b> verlangen.</li>
  <li>Die Netzbetreiber listen ihre Anschlussbedingungen für Netzumschalteinrichtungen gemeinsam auf
  wechselrichterliste.at.</li>
</ul>
<p>Beim Sigenergy-System übernimmt das Sigen Gateway die Umschaltung. Laut Datenblatt beträgt die
Unterbrechung auf der Lastseite 0 Millisekunden, wenn Gateway, Energy Controller und Batterie zusammen
eingesetzt werden und die Nennleistung des Controllers über der gesamten Hauslast liegt. Im Inselbetrieb
liefert der Ausgang für 10 Sekunden die doppelte Nennleistung, etwa zum Anlaufen von Pumpen.</p>
"""),
        ("Netzanschluss in Österreich: TOR Erzeuger und Wechselrichterliste", "netzanschluss", f"""
<p><b>Für jede Hausdachanlage gelten in Österreich die TOR Stromerzeugungsanlagen Typ A der E-Control</b>,
anzuwenden auf alle Anlagen unter 250 kW, seit 1. Juni 2026 in Version 1.4. Der Netzbetreiber genehmigt
keinen Anschluss, wenn die Anforderungen nicht erfüllt sind. So läuft es ab:</p>
{A.steps([
    ("Netzanschlussantrag stellen", "Beim zuständigen Netzbetreiber, in Kärnten meist die Kärnten Netz, in der "
     "Steiermark die Energienetze Steiermark oder in Graz die Stromnetz Graz. Er beurteilt den Anschluss und "
     "schickt ein Angebot für den Netzzugangsvertrag samt Zählpunktnummer."),
    ("TOR-konformen Wechselrichter wählen", "Ist das Gerät in der Wechselrichterliste von Oesterreichs Energie "
     "als zulässig gelistet, gilt der Konformitätsnachweis als gegeben. Auf die Liste greifen alle 122 "
     "Verteilernetzbetreiber in Österreich zu."),
    ("Ländereinstellung Österreich setzen", "Der Errichter stellt den Wechselrichter auf die österreichischen "
     "Parameter ein, berücksichtigt abweichende Vorgaben des Netzbetreibers und dokumentiert das."),
    ("Fertigstellung melden", "Der Errichter bestätigt die vertragskonforme Errichtung und übermittelt die "
     "Unterlagen. Erst danach erteilt der Netzbetreiber die Betriebserlaubnis."),
])}
<p>Neu ist die <b>Ansteuerbarkeit</b>: Für Anlagen, bei denen der Netzbetreiber die Einspeisung dynamisch
vorgibt, etwa bei der Spitzenkappung nach dem ElWG, verlangt die TOR eine digitale Schnittstelle mit
Internetanbindung und eine Rückfallfunktion. Fällt die Kommunikation aus, darf eine PV-Anlage dann höchstens
70 % der Modulspitzenleistung einspeisen. Das Kommunikationsprotokoll (OpenADR) soll bis 31. Dezember 2026
veröffentlicht werden. Was das ElWG sonst ändert, steht unter
{a('/elwg-beschluss-oesterreich/', 'ElWG: was sich für PV-Besitzer ändert')}.</p>
"""),
        ("Lebensdauer, Tausch und Kosten: was belegt ist", "lebensdauer", f"""
<p><b>Der Wechselrichter ist meist das erste Bauteil einer PV-Anlage, das getauscht werden muss.</b> Der ADAC
nennt für hochwertige Geräte bei fachgerechter Montage rund 10 bis 15 Jahre, häufigste Ursachen für Ausfälle
sind Überhitzung, Feuchtigkeit und Überspannung. Module halten deutlich länger: Die Berner Fachhochschule
nennt 25 bis 30 Jahre für die übrigen Komponenten.</p>
<p>Die Berner Fachhochschule hat 2.121 Wechselrichter aus 1.195 Anlagen ausgewertet: Mehr als 65 % liefen bis
zum 15. Betriebsjahr ohne ertragsrelevanten Fehler. Die Lebensdauer hing vor allem vom Hersteller und vom
Montageort ab, im Freien montierte Geräte hielten kürzer. Faustregel der Forscher: Ein Wechselrichter wird im
Leben einer Anlage einmal ersetzt.</p>
<h3>Garantie</h3>
<p>Herstellergarantien sind freiwillig und sehr unterschiedlich. Die Verbraucherzentrale (Deutschland) nennt
als Beispiel fünf Jahre auf den Wechselrichter und rät, die Bedingungen schriftlich geben zu lassen, weil
manche Hersteller Abbau- und Transportkosten auf Kunden abwälzen. Sigenergy gibt 10 Jahre Produktgarantie auf
Energy Controller und Batterie, gegen Aufpreis verlängerbar auf bis zu 15 Jahre. Bedingung ist unter anderem
eine Internetverbindung für Updates.</p>
<h3>Wechselrichter tauschen</h3>
<p>Der Tausch gehört in die Hand einer Elektrofachkraft. Laut TOR sind Änderungen, die die elektrischen
Eigenschaften der Anlage betreffen, dem Netzbetreiber mitzuteilen. Als wesentliche Änderung nennt die TOR
ausdrücklich den Ersatz eines Wechselrichters durch ein Gerät mit erweiterten elektrischen Eigenschaften,
etwa beim Umstieg auf einen Hybridwechselrichter mit Speicher. Steht ein Tausch an, lohnt die Frage, ob nicht
gleich ein Speicher mitkommt.</p>
<h3>Was kostet ein Wechselrichter?</h3>
{A.table(
    ["Wechselrichter-Leistung", "Typischer Einsatz", "Preisspanne*"],
    [
        ["bis 800 W", "Balkonkraftwerk", "ca. 100 bis 250 €"],
        ["ca. 2.000 W", "kleine PV-Anlage", "ca. 300 bis 700 €"],
        ["3.000 bis 5.000 W", "Einfamilienhaus", "ca. 900 bis 1.800 €"],
        ["ca. 10 kW", "großes Dach, Hybridbetrieb", "ca. 1.800 bis 3.500 €"],
    ],
    hl_cols=(2,),
)}
<p>Preisspannen laut ADAC (Deutschland, Juli 2026). Ob Montage enthalten ist, sagt der ADAC nicht. Für
Österreich gibt es keine neutrale Preisübersicht. Beim Tausch kommen Montage, Inbetriebnahme und die Meldung
an den Netzbetreiber dazu. Hybridgeräte sind teurer als reine Stringwechselrichter. In einer neuen
Komplettanlage ist der Wechselrichter im Preis enthalten: Eine 10-kWp-Anlage mit Speicher kostet bei uns
rund 15.000 bis 22.000 € vor Förderung.</p>
"""),
        ("Aus der Praxis: 8 von 10 EBZ-Referenzen mit Sigenergy", "praxis", f"""
<p><b>Bei 8 der 10 Referenzprojekte auf unserer Website arbeitet ein Sigenergy-System, also ein
Hybridwechselrichter mit Speicher und Energiemanagement aus einer Hand.</b> Bei zwei Anlagen schaltet ein
Gateway bei Netzausfall automatisch auf Notstrom, bei vier weiteren ist eine manuelle Notstromumschaltung
eingebaut.</p>
{A.table(
    ["Projekt", "Leistung", "Speicher", "Besonderheit"],
    [
        [a('/referenzen/projekt-pv-anlage-hotel-villach/', 'Hotel Villach/Warmbad'), "13 kWp", "27 kWh",
         "Gateway, Notstrom automatisch"],
        [a('/referenzen/projekt-landwirtschaft-im-burgenland/', 'Landwirtschaft Burgenland'), "13 kWp", "27 kWh",
         "Gateway, Notstrom automatisch"],
        [a('/referenzen/projekt-gewerbe-oberoesterreich/', 'Gewerbe Oberösterreich'), "40 kWp", "40 kWh",
         "Ost-West auf Trapezblech"],
        [a('/referenzen/projekt-stadthaus-in-graz/', 'Stadthaus Graz'), "18 kWp", "18 kWh",
         "Wallbox 11 kW, Notstrom manuell"],
        [a('/referenzen/projekt-bitumendach-in-niederoesterreich/', 'Einfamilienhaus Niederösterreich'), "18 kWp",
         "16 kWh", "drei Ausrichtungen, Notstrom manuell"],
        [a('/referenzen/projekt-pv-wien/', 'Wohnhaus Wien'), "10,92 kWp", "20 kWh",
         "Wallbox, Warmwasser aus Überschuss"],
        [a('/referenzen/projekt-pv-am-ossiachersee/', 'Einfamilienhaus Ossiachersee'), "10 kWp", "9 kWh",
         "Ost-West, Wallbox 11 kW"],
        [a('/referenzen/projekt-flachdach-in-graz/', 'Flachdach Graz'), "11,83 kWp", "20 kWh",
         "ballastiert, Notstrom manuell"],
    ],
    hl_cols=(1,),
)}
<p>Wir setzen Sigenergy oft ein, weil ein System Wechselrichter, Speicher, Wallbox und Notstrom steuert und in
einer App zeigt. Das ist keine Festlegung: Passt bei Ihnen eine andere Lösung besser, etwa ein
Batteriewechselrichter zur bestehenden Anlage, planen wir diese. Alle Projekte finden Sie unter
{a('referenzen', 'Referenzen')}.</p>
"""),
        ("Fazit: Wechselrichter und Speicher zusammen planen", "fazit", f"""
<p>Der Wechselrichter ist das Herz der Anlage und gleichzeitig das Bauteil mit der kürzesten Lebensdauer. Wer
neu baut, plant ihn am besten gleich als Hybridwechselrichter mit Speicher und Energiemanagement, dreiphasig
und mit passenden MPP-Trackern für jede Dachfläche. Wer eine Bestandsanlage hat, prüft beim nächsten Defekt,
ob ein Hybridgerät mit Speicher sinnvoller ist als ein reiner Ersatz. In beiden Fällen gilt: nur Geräte mit
TOR-Nachweis, sauber gemeldet beim Netzbetreiber.</p>
<p><small>*Preisspannen laut ADAC (Deutschland, Stand Juli 2026), keine österreichischen Marktpreise.
Wirkungsgrad-Rechenbeispiel ist eine eigene Überschlagsrechnung. Herstellerangaben laut Datenblatt Sigenergy
Energy Controller (Version 20260330). Stand aller Angaben: November 2026.</small></p>
{A.cta("Wechselrichter, Speicher und Notstrom aus einer Hand",
       "Wir prüfen Dach, Zählerschrank und Verbrauch, legen den Wechselrichter passend aus und melden die "
       "Anlage beim Netzbetreiber an.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("batteriespeicher", "Mehr zum Batteriespeicher"))}
"""),
    ],

    "partner": {
        "h2": "Wechselrichter und Speicher richtig ausgelegt: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie plant und installiert Photovoltaik, Batteriespeicher und Energiemanagement in Kärnten "
                 "und der Steiermark, mit zertifizierten Fachkräften und einem festen Ansprechpartner von der "
                 "Planung bis zur Übergabe. Wir wählen den Wechselrichter passend zu Dach, Speicher und "
                 "Netzanschluss und übernehmen die Anmeldung beim Netzbetreiber."),
        "grid": [
            ("Saubere Auslegung", "DC/AC-Verhältnis und MPP-Tracker passend zum Dach."),
            ("TOR-konform", "Geräte mit Nachweis, Ländereinstellung Österreich."),
            ("Notstrom mitgedacht", "Gateway oder manuelle Umschaltung nach Bedarf."),
            ("Ehrliche Beratung", "Tausch, Nachrüstung oder Neuanlage im Vergleich."),
        ],
    },

    "faq": [
        ("Wie groß muss der Wechselrichter bei einer PV-Anlage sein?",
         "Meist etwas kleiner als die Modulleistung: Der ADAC nennt als Faustregel 80 bis 100 %, in Deutschland "
         "liegt die Modulleistung laut Fraunhofer ISE im Mittel knapp 10 % über der Wechselrichterleistung. In "
         "Österreich dürfen einphasige Geräte höchstens 3,68 kVA Schieflast verursachen, größere Anlagen laufen "
         "dreiphasig."),
        ("Was macht der Wechselrichter bei der PV-Anlage?",
         "Er wandelt den Gleichstrom der Module in 50-Hertz-Wechselstrom für Haus und Netz um, sucht mit dem "
         "MPP-Tracker den besten Arbeitspunkt und trennt die Anlage bei Netzstörungen. Neue Geräte erreichen "
         "dabei einen Wirkungsgrad um 98 %."),
        ("Wie viel kostet ein Wechselrichter für eine Photovoltaikanlage?",
         "Der ADAC nennt für Einfamilienhäuser (3 bis 5 kW) rund 900 bis 1.800 Euro, für rund 10 kW im "
         "Hybridbetrieb 1.800 bis 3.500 Euro, das sind deutsche Preise. Beim Tausch kommen Montage, "
         "Inbetriebnahme und die Meldung an den Netzbetreiber dazu."),
        ("Wie lange hält ein Wechselrichter?",
         "Der ADAC nennt 10 bis 15 Jahre. In einer Auswertung der Berner Fachhochschule mit 2.121 Geräten liefen "
         "mehr als 65 % bis zum 15. Betriebsjahr ohne ertragsrelevanten Fehler. Rechnen Sie mit einem Tausch im "
         "Leben einer PV-Anlage."),
        ("Was ist ein Hybridwechselrichter?",
         "Ein PV-Wechselrichter mit zusätzlichem Batterieanschluss. Module und Speicher hängen am selben Gerät, "
         "der Sonnenstrom lädt den Speicher ohne Umweg über Wechselstrom. Viele Hybridgeräte können außerdem "
         "Notstrom oder Ersatzstrom liefern."),
        ("Brauche ich für Notstrom einen speziellen Wechselrichter?",
         "Ja. Ein normaler Netzwechselrichter schaltet bei Stromausfall ab. Nötig sind ein notstromfähiger "
         "Wechselrichter, ein Speicher und eine Umschalteinrichtung, die das Haus vom Netz trennt. Beim "
         "Sigenergy-Gateway beträgt die Umschaltzeit laut Datenblatt 0 Millisekunden."),
        ("Muss ich den Tausch des Wechselrichters melden?",
         "Änderungen, die die elektrischen Eigenschaften der Anlage betreffen, sind laut TOR dem Netzbetreiber "
         "mitzuteilen. Ersetzt ein Gerät mit erweiterten Eigenschaften den alten Wechselrichter, etwa ein "
         "Hybridgerät mit Speicher, gilt das ausdrücklich als wesentliche Änderung. Die Meldung übernimmt der "
         "Fachbetrieb."),
        ("Wie sehe ich, ob der Wechselrichter funktioniert?",
         "Am einfachsten in der App oder am Display: An einem sonnigen Tag muss die Anlage Leistung zeigen. "
         "Bleibt der Ertrag bei Sonne aus oder meldet das Gerät einen Fehler, lassen Sie ihn von einer "
         "Elektrofachkraft prüfen, im Gerät liegen gefährliche Gleichspannungen an."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Mit zertifizierten Fachkräften plant und "
                    "installiert EBZ Energie Photovoltaik, Batteriespeicher und Notstromlösungen in Kärnten und der "
                    "Steiermark, bei 8 von 10 Referenzprojekten mit Hybridwechselrichtern von Sigenergy. "
                    "Herstellerangaben und Preise in diesem Ratgeber sind Richtwerte, maßgeblich sind die "
                    "aktuellen Datenblätter und die Vorgaben Ihres Netzbetreibers."),
    "sources": [
        ("E-Control: TOR Stromerzeugungsanlagen (Typ A, Version 1.4)",
         "https://www.e-control.at/marktteilnehmer/strom/marktregeln/tor"),
        ("Wechselrichterliste.at (Projektgruppe der österreichischen Verteilernetzbetreiber)",
         "https://www.wechselrichterliste.at/"),
        ("Klima- und Energiefonds: Handlungsanleitung für die Errichtung von PV-Anlagen, Schwerpunkt Netzanschluss",
         "https://klimafonds.gv.at/wp-content/uploads/2024/09/Handlungsanleitung-fuer-die-Errichtung-von-PV-Anlagen.pdf"),
        ("Fraunhofer ISE: Aktuelle Fakten zur Photovoltaik in Deutschland (Fassung 11.11.2026)",
         "https://www.ise.fraunhofer.de/content/dam/ise/de/documents/publications/studies/aktuelle-fakten-zur-photovoltaik-in-deutschland.pdf"),
        ("Universität Paderborn: Effizienz-Ranking von Mikrowechselrichtern (Krauter, Bendfeld, 2024)",
         "https://ei.uni-paderborn.de/fileadmin-eim/elektrotechnik/fg/nek/PDF/Wirkungsgrade_Mikrowechselrichter_2024_Krauter-Bendfeld_DEUTSCH.pdf"),
        ("Berner Fachhochschule: Lebenserwartung Photovoltaik-Wechselrichter",
         "https://www.bfh.ch/de/forschung/referenzprojekte/lebenserwartung-photovoltaik-wechselrichter/"),
        ("pv magazine: Studie der BFH zur Ausfallrate von Wechselrichtern (10.02.2023)",
         "https://www.pv-magazine.de/2023/02/10/studie-343-prozent-der-wechselrichter-fuer-haushalte-fallen-nach-15-jahren-erstmals-aus/"),
        ("ADAC (Deutschland): Wechselrichter, Funktion, Kosten und Unterschiede",
         "https://www.adac.de/rund-ums-haus/energie/wechselrichter/"),
        ("Verbraucherzentrale (Deutschland): Photovoltaik, Garantie- und Versicherungsbedingungen",
         "https://www.verbraucherzentrale.de/wissen/energie/erneuerbare-energien/photovoltaik-garantie-und-versicherungsbedingungen-genau-lesen-6700"),
        ("Sigenergy: Datenblatt Sigen Energy Controller",
         "https://wwwstatic.sigenergy.com/content/assets/uploads/en_download/1774951281792375.pdf"),
        ("Sigenergy: SigenStor Produktseite", "https://www.sigenergy.com/de/products/sigenstor"),
        ("Sigenergy: Garantie", "https://www.sigenergy.com/de/support/warranty"),
    ],
    "related": [
        ("/sigenergy/", "Sigenergy: Hybridwechselrichter, Speicher und Notstrom"),
        ("batteriespeicher", "Batteriespeicher: Größe, Technik und Kosten"),
        ("/pv-speicher-nachruesten/", "PV-Speicher nachrüsten: AC- oder DC-Kopplung"),
        ("/notstrom/", "Notstrom mit Photovoltaik: Ersatzstrom erklärt"),
    ],
    "cta": {
        "h3": "Wechselrichter richtig auslegen",
        "text": "Wir planen Module, Wechselrichter und Speicher als ein System und melden die Anlage an.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihr Wechselrichter, passend geplant",
    "final_text": ("Kostenlose Erstberatung zu Photovoltaik, Hybridwechselrichter, Speicher und Notstrom, mit "
                   "transparenten Zahlen und einem Ansprechpartner aus Villach."),
}
