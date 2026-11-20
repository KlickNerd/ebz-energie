"""Ratgeber: ElWG 2026 (Elektrizitätswirtschaftsgesetz): Was für PV-Betreiber und Haushalte gilt.

Ursprung: migriert von ebz-photovoltaik.at/elwg-beschluss-oesterreich/ (Stand der Quelle Dezember 2025),
am 2026-11-20 komplett auf den Stand nach Inkrafttreten überarbeitet. Slug bleibt unverändert.
Ziel-Keywords (Google Ads, Österreich, 20.11.2026): elwg 1.900, elwg ris 590, elektrizitätswirtschaftsgesetz 480,
elwg 2026 110, elwg österreich 110, elwg neu 90, elwg gesetz 70, elwg beschluss 70, elwg peer to peer 30.

Faktenbasis (am 20.11.2026 selbst geöffnet): ElWG-Text konsolidiert (Stand 20.11.2026) über jusline.at
(§§ 22, 36, 54, 65, 75a, 76, 96, 101, 127, 189; ris.bka.gv.at war wegen einer Sicherheitsprüfung nicht abrufbar),
BMWET-Factsheet Spitzenkappung (Februar 2026), E-Control Presseunterlage SNE-G-V (12.10.2026),
E-Control Begutachtungsentwurf SNT-V 2027 und Pressemeldung (29.10.2026), energiegemeinschaften.gv.at
(FAQs zum ElWG, Gemeinsame Energienutzung), ORF (Beschluss 11.12.2025), WKO (Kundmachung 23.12.2025).
Korrigiert gegenüber der Fassung vom September 2026: "Bestandsschutz" beim Infrastrukturbeitrag (laut § 75a
nicht vorgesehen), "Speicher 20 Jahre vom Infrastrukturbeitrag befreit" (falsch: § 127 Abs. 3 betrifft
Netzentgelte beim Netzbezug von Speichern), "3 bis 5 % Verlust durch Spitzenkappung" (nicht belegt; BMWET:
unter 1 %), "Investitionszuschüsse des Bundes laufen weiter" (EAG-Call 2026 beendet), "monatelanges Warten
auf den Zählertausch" (nicht belegt).
EBZ-Belege: Referenzen Ossiachersee (10 kWp Ost-West, 9 kWh, Wallbox) und Gewerbe Oberösterreich (40 kWp).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "elwg-beschluss-oesterreich",
    "path": "/elwg-beschluss-oesterreich/",
    "title": "ElWG 2026: Was sich für PV-Betreiber ändert | EBZ",
    "description": ("ElWG in Kraft: was für PV-Betreiber und Haushalte gilt, was 2027 kommt. Spitzenkappung "
                    "70 %, Beitrag über 20 kW (max. 0,05 ct/kWh), Smart Meter, Bürgerenergie."),
    "eyebrow": "Recht · Elektrizitätswirtschaftsgesetz",
    "crumb_label": "ElWG 2026",
    "h1": "ElWG 2026: Was das Elektrizitätswirtschaftsgesetz für PV-Betreiber und Haushalte ändert",
    "lead": ("Das Elektrizitätswirtschaftsgesetz (ElWG) gilt seit 24. Dezember 2025 und hat das ElWOG 2010 "
             "abgelöst, die neuen Regeln für Energiegemeinschaften und Peer-to-Peer-Strom gelten seit "
             "1. Oktober 2026. Hier lesen Sie, was für PV-Betreiber und Haushalte schon gilt, was ab 2027 kommt "
             "und was noch offen ist (Stand: 20. November 2026)."),
    "chips": [
        "In Kraft seit <b>24.12.2025</b>",
        "Bis <b>20 kW</b>: kein Infrastrukturbeitrag",
        "Über 20 kW ab 2027: <b>max. 0,05 ct/kWh</b>",
        "Spitzenkappung: nie unter <b>70 %</b>",
    ],
    "date_published": "2025-12-10",
    "date_modified": "2026-11-20",
    "hero_img": "gen_hero",
    "hero_alt": "Photovoltaikmodule auf einem dunklen Ziegeldach mit Kamin vor blauem Himmel",

    "tldr": [
        "Das ElWG wurde am 11. Dezember 2025 im Nationalrat beschlossen, am 23. Dezember 2025 als BGBl. I "
        "Nr. 91/2025 kundgemacht und gilt seit 24. Dezember 2025. Einzelne Teile starten später: Bürgerenergie "
        "seit 1. Oktober 2026, der Versorgungsinfrastrukturbeitrag ab 1. Jänner 2027.",
        "Einspeiser bis inklusive 20 kW netzwirksamer Leistung zahlen keinen Versorgungsinfrastrukturbeitrag. "
        "Darüber gilt ab 2027 ein Beitrag von höchstens 0,05 Cent je eingespeister kWh, für neue und "
        "bestehende Anlagen. Die genaue Höhe legt der Wirtschaftsminister per Verordnung fest.",
        "Bei neuen oder geänderten PV-Anschlüssen darf der Netzbetreiber die Einspeisung begrenzen, aber nie "
        "unter 70 % der Modulleistung. Laut Wirtschaftsministerium geht bei üblichen Hausanlagen dadurch "
        "praktisch kein Strom verloren. Bei einer vereinbarten Einspeiseleistung bis 7 kW entfällt die Kappung.",
        "Neue Anlagen ab 3,68 kW brauchen seit 1. Juni 2026 eine Einrichtung zur Steuerbarkeit. Wer eine "
        "PV-Anlage, einen Speicher oder eine Wärmepumpe hat, kann der Viertelstundenmessung am Smart Meter "
        "nicht widersprechen.",
        "Seit Oktober 2026 gibt es fünf Bürgerenergie-Modelle. In der Übergangsphase klappt das nur beim selben "
        "Netzbetreiber, österreichweit voraussichtlich ab April 2027. Den Netzentgelt-Rabatt bekommen bis Ende "
        "2026 nur Mitglieder lokaler oder regionaler Erneuerbare-Energie-Gemeinschaften.",
    ],
    "kpis": [
        ("20 kW", "Grenze für den Versorgungsinfrastrukturbeitrag"),
        ("max. 0,05 ct", "je eingespeister kWh über 20 kW, ab 2027"),
        ("70 %", "Untergrenze der Spitzenkappung neuer PV-Anlagen"),
        ("5 Modelle", "Bürgerenergie seit 1. Oktober 2026"),
    ],

    "sections": [
        ("Was ist das ElWG und seit wann gilt es?", "was-ist", f"""
<p>Das Elektrizitätswirtschaftsgesetz (ElWG) ist das zentrale Strommarktgesetz Österreichs. Es regelt, wer
für das Netz zahlt, wie viel eine Anlage einspeisen darf, welche Rechte Stromkundinnen und Stromkunden haben
und wie Strom zwischen Haushalten geteilt werden kann. Der Nationalrat hat es am 11. Dezember 2025 mit
Zweidrittelmehrheit beschlossen (116 zu 47 Stimmen). Kundgemacht wurde es am 23. Dezember 2025 als Teil des
„Günstiger-Strom-Gesetzes“ (BGBl. I Nr. 91/2025), in Kraft ist es seit 24. Dezember 2025. Das ElWOG 2010 ist
damit abgelöst.</p>
<p>Wichtig für die Praxis: Nicht alles gilt ab demselben Tag. Viele Regeln brauchen Verordnungen der E-Control
oder des Wirtschaftsministeriums (BMWET), die teils erst 2027 wirken. Die folgende Übersicht zeigt die Termine,
die für Betreiber einer {a('photovoltaik', 'Photovoltaikanlage')} und für Haushalte zählen.</p>
{A.table(
    ["Datum", "Was gilt", "Status"],
    [
        ["24.12.2025", "ElWG in Kraft, u. a. Spitzenkappung und vereinfachter Netzanschluss bis 20 kW", "gilt"],
        ["1.4.2026", "Recht auf dynamische und feste Stromtarife, gestützter Preis (Sozialtarif)", "gilt"],
        ["1.6.2026", "neue Anlagen ab 3,68 kW nur mit Einrichtung zur Steuerbarkeit", "gilt"],
        ["1.10.2026", "Bürgerenergie: GEA, EEG, BEG, Peer-to-Peer, Eigenversorgungsanlage", "gilt, Übergangsphase"],
        ["1.1.2027", "Versorgungsinfrastrukturbeitrag über 20 kW, neue Netzentgelt-Verordnungen", "kommt, Höhe teils offen"],
        ["1.1.2027 bis 1.7.2028", "Leistungspreis für Haushalte, Start je Netzbereich", "kommt"],
        ["April 2027", "Bürgerenergie über mehrere Netzgebiete und österreichweit", "voraussichtlich"],
    ],
    hl_cols=(2,),
)}
<p><small>Quellen: ElWG (§§ 22, 36, 65, 75a, 76, 101), E-Control (SNE-G-V, Oktober 2026),
energiegemeinschaften.gv.at; Stand 20. November 2026.</small></p>
"""),
        ("Regel 1: Versorgungsinfrastrukturbeitrag ab 2027", "infrastrukturbeitrag", f"""
<p>Der größte Streitpunkt war die Frage, ob Einspeiser künftig für das Netz zahlen. Das Ergebnis steht in
§ 75a ElWG: Einspeiser zahlen ab 1. Jänner 2027 jährlich einen Versorgungsinfrastrukturbeitrag. Wer eine
netzwirksame Leistung bis inklusive 20 kW hat, ist davon befreit.</p>
<h3>Privathaushalte bis 20 kW: befreit</h3>
<p>Maßgeblich ist die netzwirksame Leistung, also das, was am Netzanschluss tatsächlich ins Netz fließen kann.
Eine typische Aufdachanlage auf einem Einfamilienhaus liegt darunter. Für Sie fällt beim Einspeisen des
Überschusses damit kein Versorgungsinfrastrukturbeitrag an.</p>
<h3>Gewerbe und Landwirtschaft über 20 kW: gedeckelt</h3>
<p>Über 20 kW legt der Wirtschaftsminister den Beitrag für jedes Kalenderjahr per Verordnung fest. Das Gesetz
deckelt ihn: Die Belastung je Einspeiser darf 0,05 Cent je kWh der eingespeisten Jahresstrommenge nicht
übersteigen. Eine Bestandsschutz-Regel für ältere Anlagen enthält § 75a nicht. Der Netzbetreiber verrechnet den
Beitrag gesondert auf der Netzrechnung. Eine Verordnung mit der konkreten Höhe für 2027 haben wir bis
20. November 2026 nicht gefunden.</p>
{A.table(
    ["Netzwirksame Leistung", "Versorgungsinfrastrukturbeitrag", "Ab wann"],
    [
        ["bis inklusive 20 kW", "befreit", "nicht betroffen"],
        ["über 20 kW, neu oder bestehend", "höchstens 0,05 ct je eingespeister kWh, Höhe per Verordnung", "1. Jänner 2027"],
    ],
    hl_cols=(1,),
)}
<p>Zur Größenordnung: Unsere {a('/referenzen/projekt-gewerbe-oberoesterreich/', 'Gewerbeanlage in Oberösterreich')}
hat 40 kWp und erzeugt rund 40.000 kWh im Jahr. Selbst wenn diese Menge vollständig eingespeist würde, wären es
beim Höchstsatz 20 Euro im Jahr*. Tatsächlich verbraucht der Betrieb einen großen Teil selbst.</p>
<p><small>*Rechenbeispiel mit dem gesetzlichen Höchstwert (40.000 kWh x 0,05 ct). Maßgeblich sind die Verordnung
des BMWET und die Abrechnung Ihres Netzbetreibers.</small></p>
"""),
        ("Regel 2: Spitzenkappung auf 70 Prozent", "spitzenkappung", f"""
<p>Bei einem neuen oder geänderten Netzzugang einer PV-Anlage darf der Netzbetreiber die netzwirksame Leistung
dauerhaft begrenzen, statisch oder dynamisch. Die Grenze darf aber nie unter 70 % der Modulspitzenleistung liegen
(§ 101 Abs. 2 ElWG). Bei einer 10-kWp-Anlage dürfen also mindestens 7 kW ins Netz. Bestehende Anlagen sind nur
betroffen, wenn ihr Netzzugang geändert wird, etwa bei einer Erweiterung.</p>
<h3>Wann die Kappung nicht gilt</h3>
<ul>
  <li><b>Kleine Einspeiseleistung:</b> Wer eine netzwirksame Leistung von höchstens 7 kW vereinbart hat,
  unterliegt der Spitzenkappung nicht.</li>
  <li><b>Unbeschränkter Anschluss:</b> Wer die Kosten für einen unbeschränkten Netzanschluss trägt, ist
  ebenfalls ausgenommen.</li>
  <li><b>Eigenverbrauch:</b> Die Grenze gilt am Netzanschlusspunkt. Waschmaschine, Wärmepumpe, Wallbox und
  Speicher hinter dem Zähler nutzen weiter die volle Leistung.</li>
</ul>
<h3>Wie viel Strom geht verloren?</h3>
<p>Laut Factsheet des Wirtschaftsministeriums würde selbst bei einer nach Süden ausgerichteten Anlage, die ihren
gesamten Strom einspeist, weniger als 1 von 100 kWh abgeregelt. Eine Ost-West-Anlage überschreitet die
70-Prozent-Marke nur in einer einzigen Stunde im Jahr. Im Beispiel der Österreichischen Energieagentur (10 kWp
Ost-West, 3.500 kWh Haushaltsverbrauch) geht gar kein Strom verloren. Sobald der Netzbetreiber Anlagen
ansteuern kann, muss er die Grenze dynamisch nach der tatsächlichen Netzlage vorgeben; das BMWET nennt dafür
2028.</p>
{A.box("Eine Ost-West-Belegung, ein Speicher und gezielter Verbrauch zu Mittag machen die Spitzenkappung zum "
       "Planungsdetail. Ein Beispiel ist unsere "
       + a('/referenzen/projekt-pv-am-ossiachersee/', 'Anlage am Ossiachersee')
       + " mit 10 kWp Ost-West, 9-kWh-Speicher und Wallbox.", label="Planungstipp:")}
"""),
        ("Regel 3: Steuerbarkeit, Netzanschluss und Smart Meter", "pflichten", f"""
<p>Das ElWG ändert auch die Technik am Netzanschluss. Für neue Anlagen sind drei Punkte entscheidend.</p>
<h3>Steuerbarkeit ab 3,68 kW</h3>
<p>Neue und wesentlich geänderte Erzeugungsanlagen ab 3,68 kW netzwirksamer Leistung müssen seit
1. Juni 2026 eine technische Einrichtung zur Steuerbarkeit mit standardisierter Schnittstelle haben, die Kosten
trägt der Betreiber (§ 76 ElWG). Der Netzbetreiber muss die Ansteuerung bis 1. Juni 2028 (über 25 kW) bzw.
1. Juni 2029 (3,68 bis 25 kW) herstellen. Er gibt nur die Leistung am Anschlusspunkt vor: Eigenverbrauch,
Speicher und Regelung hinter dem Zähler bleiben Ihre Sache.</p>
<h3>Vereinfachter Netzanschluss bis 20 kW</h3>
<p>Anlagen bis 20 kW netzwirksamer Leistung werden auf Anzeige angeschlossen. Der Netzbetreiber muss binnen
vier Wochen ab vollständiger Anzeige reagieren, sonst ist die Anlage anzuschließen; verweigern darf er nur
wegen begründeter Sicherheitsbedenken oder technischer Inkompatibilität (§ 96 ElWG). PV-Anlagen bis 15 kW
über einen bestehenden Bezugsanschluss zahlen dafür kein zusätzliches Netzanschlussentgelt und dürfen bis zur
vereinbarten Bezugsleistung einspeisen, höchstens 15 kW.</p>
<h3>Smart Meter: kein Opt-out bei PV</h3>
<p>Wer eine Stromerzeugungsanlage, einen Speicher, eine Wärmepumpe oder einen Ladepunkt hat, an einem
Bürgerenergie-Modell teilnimmt oder einen dynamischen Tarif nutzt, kann der Speicherung von Viertelstundenwerten
nicht widersprechen (§ 54 Abs. 2 ElWG). Mehr dazu im Ratgeber {a('/smart-meter-opt-out/', 'Smart Meter Opt-out')}.</p>
{A.table(
    ["Bereich", "Vor dem ElWG", "Mit dem ElWG"],
    [
        ["Anschluss bis 20 kW", "je nach Netzbetreiber", "Anzeige, Reaktion binnen 4 Wochen"],
        ["Steuerbarkeit", "keine einheitliche Pflicht", "ab 3,68 kW seit 1.6.2026"],
        ["Einspeiseleistung neuer PV", "nach Netzzusage", "Kappung möglich, nie unter 70 %"],
        ["Smart-Meter-Opt-out", "möglich", "nicht bei PV, Speicher, Wärmepumpe, Ladepunkt"],
    ],
    hl_cols=(2,),
)}
{A.cta("Anlage nach den neuen Regeln planen lassen",
       "Wir planen PV-Anlage, Speicher und Steuerung so, dass Spitzenkappung und Steuerbarkeit für Sie kein "
       "Thema sind, und übernehmen die Anzeige beim Netzbetreiber.",
       secondary=("photovoltaik", "Zur Photovoltaik"))}
"""),
        ("Regel 4: Batteriespeicher und neue Netzentgelte ab 2027", "speicher", f"""
<p>Das ElWG kennt keine Befreiung des Heimspeichers vom Versorgungsinfrastrukturbeitrag, wie sie früher oft
beschrieben wurde. Für Speicher, die Strom aus dem Netz laden, stellt § 127 Abs. 3 ElWG (Fassung Stand
November 2026) den Netzbezug zum Einspeichern für 20 Jahre ab Inbetriebnahme von Netznutzungs- und
Netzverlustentgelt frei, unter Berücksichtigung des systemdienlichen Betriebs. Laut E-Control ist für
systemdienliche Speicher auch nach der neuen Grundsatzverordnung eine langfristige Befreiung oder Reduktion
möglich. Ein Heimspeicher, der nur PV-Überschuss lädt, bezieht dafür ohnehin keinen Netzstrom.</p>
<p>Der eigentliche Vorteil eines {a('batteriespeicher', 'Batteriespeichers')} kommt aus den neuen Netzentgelten,
die die E-Control auf Basis des ElWG festlegt:</p>
<ul>
  <li><b>Leistungspreis:</b> Künftig zählt auch der höchste 15-Minuten-Wert eines Monats. Jeder Netzbereich
  führt das für Haushalte zwischen 1. Jänner 2027 und spätestens 1. Juli 2028 ein, schrittweise bis zu einem
  Verhältnis von 50:50 zwischen Arbeits- und Leistungspreis. Speicher und Energiemanagement glätten
  Lastspitzen von Wallbox und Wärmepumpe.</li>
  <li><b>Zeitvariable Arbeitspreise:</b> Der Sommer-Nieder-Arbeitspreis gilt von 1. April bis 30. September
  zwischen 10 und 16 Uhr, bisher mit 20 % Reduktion. Ab Oktober 2027 kommt ein Winter-Nieder-Arbeitspreis von
  23 bis 5 Uhr. Voraussetzung ist die viertelstündliche Smart-Meter-Auslesung.</li>
  <li><b>Kärnten:</b> Laut Begutachtungsentwurf der E-Control vom Oktober 2026 sinken die Netzentgelte 2027 in
  den meisten Netzbereichen, steigen aber vor allem in Kärnten. Die Begutachtung lief bis 20. November 2026.</li>
</ul>
<p>Wie Sie Überschuss sinnvoll im Haus halten, zeigen die Ratgeber {a('/pv-speicher-nachruesten/', 'PV-Speicher nachrüsten')}
und {a('/dynamischer-stromtarif/', 'dynamischer Stromtarif')}. Ein {a('ems', 'Energiemanagementsystem')} fördert der
Klimafonds für Haushalte mit 50 %, höchstens 600 Euro (siehe {a('/ems-foerderung/', 'EMS-Förderung')}).</p>
"""),
        ("Bürgerenergie: 5 Modelle seit Oktober 2026", "buergerenergie", f"""
<p>Seit 1. Oktober 2026 gelten die Bürgerenergie-Regeln des ElWG (§§ 65 ff.). Strom teilen geht damit in fünf
Modellen: {a('/gemeinschaftliche-erzeugungsanlage/', 'gemeinschaftliche Erzeugungsanlage')} (GEA),
Erneuerbare-Energie-Gemeinschaft (EEG), {a('/buergerenergiegemeinschaft/', 'Bürgerenergiegemeinschaft')} (BEG),
{a('/peer-to-peer-strom/', 'Peer-to-Peer-Vertrag')} (P2P) und Eigenversorgungsanlage (EVA). Bestehende GEA,
EEG und BEG wurden ohne Neugründung ins neue System übergeführt. Einen Vergleich aller Modelle finden Sie im
Leitartikel {a('/energiegemeinschaft/', 'Energiegemeinschaft')}.</p>
<ul>
  <li><b>Übergangsphase:</b> Seit 5. Oktober 2026 lassen sich die neuen Möglichkeiten laut Koordinationsstelle
  vorübergehend nur mit Zählpunkten beim selben Netzbetreiber umsetzen. Netzübergreifend, etwa Kärnten und Wien,
  ist das voraussichtlich ab April 2027 möglich.</li>
  <li><b>Netzentgelt-Rabatt:</b> Von Oktober bis Dezember 2026 bekommen nur Mitglieder lokaler oder regionaler
  EEGs den reduzierten Netzarbeitspreis. Mit der neuen Verordnung, nach heutigem Stand ab 1. Jänner 2027, soll
  er auch für BEG, P2P und EVA im Nahebereich gelten. Im Entwurf der E-Control sind 49 % im Lokalbereich und
  22 % bzw. 58 % (Netzebenen 4 und 5) im Regionalbereich vorgesehen; endgültig ist erst die Verordnung.</li>
  <li><b>Österreichweit ohne Rabatt:</b> Außerhalb des Nahebereichs fallen die Netzentgelte in voller Höhe
  an. Von den Energiegemeinschaften sind derzeit nur EEGs von Erneuerbaren-Förderbeitrag und
  Elektrizitätsabgabe befreit; für P2P und EVA ist eine solche Befreiung nicht geregelt. Den Förderbeitrag setzt
  die Bundesregierung 2027 laut BMF für alle Stromkunden aus, die Elektrizitätsabgabe steigt 2027 vom befristeten
  Satz 2026 (0,1 Cent für Haushalte, 0,82 Cent für Unternehmen) wieder auf 1,5 Cent je kWh.</li>
</ul>
<p>Was das in Euro bedeutet, rechnet der Ratgeber {a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft: Netzkosten')}
vor. Ob Teilen mehr bringt als Einspeisen, hängt vom OeMAG-Marktpreis ab, der monatlich schwankt (Details im
Ratgeber {a('/oemag-einspeisetarif/', 'OeMAG-Einspeisetarif')}).</p>
"""),
        ("Was ändert sich für Haushalte als Stromkunden?", "haushalte", f"""
<p>Auch ohne eigene PV-Anlage bringt das ElWG neue Rechte, die seit 1. April 2026 gelten:</p>
<ul>
  <li><b>Dynamische und feste Tarife:</b> Wer einen Smart Meter hat, hat ein Recht auf einen Vertrag mit
  dynamischen Preisen. Lieferanten mit mehr als 25.000 Zählpunkten müssen dynamische und feste Preise anbieten.
  Feste Preise dürfen frühestens ein Jahr nach Vertragsabschluss einseitig zu Lasten der Kundin oder des Kunden
  geändert werden (§ 22 ElWG).</li>
  <li><b>Gestützter Preis (Sozialtarif):</b> Haushalte, die vom ORF-Beitrag befreit sind, bekommen für
  2.900 kWh im Jahr einen Energiepreis von 6 Cent je kWh (§ 36 ElWG).</li>
</ul>
<p>Ob sich ein dynamischer Tarif mit PV-Anlage lohnt, lesen Sie im Ratgeber
{a('/dynamischer-stromtarif/', 'dynamischer Stromtarif')}.</p>
"""),
        ("Was bedeutet das für Ihre Entscheidung?", "entscheidung", f"""
<p>Vor dem Beschluss hörten wir in Beratungen oft: „Ich warte, bis das Gesetz da ist.“ Der Rahmen steht seit
Dezember 2025, die meisten Regeln gelten. Offen sind vor allem Beträge in Verordnungen: die Höhe des
Versorgungsinfrastrukturbeitrags über 20 kW und die endgültigen Netzentgelte 2027. Für eine Hausanlage bis
20 kW ändert das nichts Grundsätzliches.</p>
<p>Bei der Förderung hat sich dagegen viel bewegt: Den EAG-Investitionszuschuss des Bundes gibt es für neue
Anlagen derzeit nicht, für 2027 plant das BMWET eine Systemförderung für Speicher mit intelligenter Steuerung.
Den aktuellen Stand finden Sie unter {a('foerderung_at', 'Photovoltaik-Förderung Österreich')}.</p>
<p>Zur Einordnung: Bei EBZ Energie liegen 10 kWp mit Speicher je nach Dach und Komponenten bei rund 15.000 bis
22.000 Euro vor Förderung, die Amortisation typischerweise bei 4 bis 6 Jahren. Dazu kommen bis zu 30 Jahre
Leistungsgarantie und mindestens 10 Jahre Produktgarantie.</p>
"""),
        ("Fazit: Klare Regeln, wenig Mehrkosten für Hausanlagen", "fazit", f"""
<p>Das ElWG ist seit Dezember 2025 in Kraft und bringt für private PV-Betreiber vor allem Klarheit: kein
Infrastrukturbeitrag bis 20 kW, eine Spitzenkappung, die bei Hausanlagen kaum Strom kostet, und neue Rechte beim
Teilen von Strom. Mehr Aufwand entsteht bei der Technik: Steuerbarkeit ab 3,68 kW und Viertelstundenmessung. Mit
Speicher und Energiemanagement nutzen Sie die neuen Netzentgelte zu Ihrem Vorteil.</p>
{A.cta("Ihr nächster Schritt",
       "Wir erstellen für Ihr Dach einen Projektbericht mit 3D-Belegplan und Statikreport, abgestimmt auf die "
       "neuen Regeln, Ihr Lastprofil und die passende Speichergröße.",
       primary=("kontakt", "Unverbindliches Angebot anfordern"), secondary=("referenzen", "Referenzen ansehen"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Anmeldung und Umsetzung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("Mit dem ElWG ist die Anmeldung technischer geworden. EBZ Energie aus Villach plant und montiert "
                 "Photovoltaik, Speicher und Energiemanagement in Kärnten und der Steiermark, mit zertifizierten "
                 "Fachkräften und einem festen Ansprechpartner von der Planung bis zur Übergabe. Aus über 300 "
                 "dokumentierten Projekten kennen wir die Abläufe bei den Netzbetreibern."),
        "grid": [
            ("Netzanzeige", "Wir übernehmen die Anzeige beim Netzbetreiber."),
            ("Steuerbar ab 3,68 kW", "Komponenten mit der geforderten Schnittstelle."),
            ("Spitzenkappung geplant", "Ausrichtung, Speicher und Verbrauch abgestimmt."),
            ("Energiegemeinschaft", "Anbindung an eine Gemeinschaft, Abrechnung über energyfamily."),
        ],
    },

    "faq": [
        ("Ab wann gilt das ElWG?",
         "Das ElWG ist seit 24. Dezember 2025 in Kraft. Der Nationalrat hat es am 11. Dezember 2025 beschlossen, "
         "kundgemacht wurde es am 23. Dezember 2025. Einzelne Teile gelten später: die Bürgerenergie-Regeln seit "
         "1. Oktober 2026, der Versorgungsinfrastrukturbeitrag für Einspeiser über 20 kW ab 1. Jänner 2027."),
        ("Muss ich als privater Hausbesitzer für die Einspeisung zahlen?",
         "Nicht, wenn Ihre netzwirksame Leistung höchstens 20 kW beträgt: Dann sind Sie vom "
         "Versorgungsinfrastrukturbeitrag befreit. Über 20 kW gilt ab 2027 ein Beitrag von höchstens 0,05 Cent je "
         "eingespeister kWh, dessen genaue Höhe eine Verordnung festlegt. Bei 40.000 kWh Einspeisung wären das "
         "höchstens 20 Euro im Jahr."),
        ("Was bedeutet die 70-Prozent-Regel und verliere ich dadurch Strom?",
         "Bei neuen oder geänderten PV-Anschlüssen darf der Netzbetreiber die Einspeisung begrenzen, aber nie unter "
         "70 % der Modulleistung. Laut Wirtschaftsministerium wird selbst bei voller Einspeisung einer Südanlage "
         "weniger als 1 von 100 kWh abgeregelt, bei üblichen Hausanlagen mit Eigenverbrauch praktisch nichts. "
         "Bei einer vereinbarten Einspeiseleistung bis 7 kW gilt die Kappung nicht."),
        ("Gilt die Spitzenkappung auch für bestehende PV-Anlagen?",
         "Nur, wenn der Netzzugang neu ist oder geändert wird, etwa bei einer Erweiterung. Anlagen mit "
         "unverändertem Netzzugang sind nicht betroffen. Ob Ihr Netzbetreiber bei einer Neuanlage begrenzt, klären "
         "wir bei der Anzeige."),
        ("Was ändert das ElWG beim Smart Meter?",
         "Smart Meter messen Viertelstundenwerte, getrennt nach Einspeisung und Bezug. Wer eine PV-Anlage, einen "
         "Speicher, eine Wärmepumpe oder einen Ladepunkt hat, kann dieser Messung nicht widersprechen. Die Daten "
         "sind auch Grundlage für den Leistungspreis, den die Netzbetreiber zwischen 2027 und Juli 2028 einführen."),
        ("Kann ich Strom mit Nachbarn oder Verwandten in Wien teilen?",
         "Ja, seit 1. Oktober 2026 etwa über eine Bürgerenergiegemeinschaft oder einen Peer-to-Peer-Vertrag. In "
         "der Übergangsphase geht das laut Koordinationsstelle aber nur beim selben Netzbetreiber, netzübergreifend "
         "voraussichtlich ab April 2027. Österreichweit fallen die vollen Netzentgelte an, den Rabatt gibt es nur im "
         "Nahebereich."),
        ("Lohnt sich ein Batteriespeicher durch das ElWG mehr?",
         "Ein Speicher fängt Mittagsspitzen auf, die sonst gekappt würden, und senkt Lastspitzen, wenn der "
         "Leistungspreis kommt. Eine Befreiung des Heimspeichers vom Versorgungsinfrastrukturbeitrag gibt es "
         "nicht, sie ist bis 20 kW aber ohnehin kein Thema. Ob sich der Speicher rechnet, hängt von Verbrauch, "
         "Wallbox und Wärmepumpe ab."),
        ("Wo finde ich den Gesetzestext des ElWG?",
         "Im Rechtsinformationssystem des Bundes (RIS) unter BGBl. I Nr. 91/2025, dort auch in der konsolidierten, "
         "tagesaktuellen Fassung. Für PV-Betreiber sind vor allem § 75a (Versorgungsinfrastrukturbeitrag), § 76 "
         "(Steuerbarkeit), § 96 (vereinfachter Netzanschluss) und § 101 (Spitzenkappung) relevant."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Mit zertifizierten Fachkräften plant und "
                    "installiert EBZ Energie Photovoltaik, Speicher, Wärmepumpen und Energiemanagement in Kärnten "
                    "und der Steiermark und übernimmt die Anzeige beim Netzbetreiber. Die Angaben beruhen auf dem "
                    "ElWG in der Fassung vom 20. November 2026 und den bis dahin veröffentlichten Unterlagen von "
                    "BMWET und E-Control. Keine Rechtsberatung, maßgeblich sind Gesetz, Verordnungen und "
                    "Netzbetreiber."),
    "sources": [
        ("ElWG § 75a Versorgungsinfrastrukturbeitrag (konsolidiert, Stand 20.11.2026)",
         "https://www.jusline.at/gesetz/elwg/paragraf/75a"),
        ("ElWG § 101 Spitzenkappung", "https://www.jusline.at/gesetz/elwg/paragraf/101"),
        ("ElWG § 76 Ansteuerbarkeit neuer Stromerzeugungsanlagen", "https://www.jusline.at/gesetz/elwg/paragraf/76"),
        ("ElWG § 96 Vereinfachter Netzanschluss", "https://www.jusline.at/gesetz/elwg/paragraf/96"),
        ("ElWG § 54 Auslesung von intelligenten Messgeräten", "https://www.jusline.at/gesetz/elwg/paragraf/54"),
        ("ElWG § 127 Systemnutzungsentgelte", "https://www.jusline.at/gesetz/elwg/paragraf/127"),
        ("ElWG § 22 Dynamische und feste Energiepreise", "https://www.jusline.at/gesetz/elwg/paragraf/22"),
        ("ElWG § 36 Gestützter Preis für begünstigte Haushalte", "https://www.jusline.at/gesetz/elwg/paragraf/36"),
        ("RIS: BGBl. I Nr. 91/2025 (Günstiger-Strom-Gesetz)", "https://www.ris.bka.gv.at/eli/bgbl/I/2025/91"),
        ("BMWET: ElWG-Factsheet Spitzenkappung",
         "https://www.bmwet.gv.at/dam/jcr:260fda60-c745-4861-bdcb-1c1223a4af58/ElWG-Factsheets_Spitzenkappung_final%20final.pdf"),
        ("E-Control: Presseunterlage Systemnutzungsentgelte-Grundsatzverordnung, 12.10.2026",
         "https://www.e-control.at/documents/d/guest/2026-10-12-presseunterlage_sne-g-v-pdf"),
        ("E-Control: Begutachtungsentwurf Systemnutzungsentgelte-Tarife-Verordnung 2027",
         "https://www.e-control.at/documents/d/guest/snt-v-2027-begutachtungsentwurf-pdf"),
        ("Koordinationsstelle Energiegemeinschaften: FAQs zum ElWG",
         "https://energiegemeinschaften.gv.at/faqs-zum-elwg/"),
        ("Koordinationsstelle Energiegemeinschaften: Bürgerenergie-Modelle",
         "https://energiegemeinschaften.gv.at/gemeinsame-energienutzung/"),
        ("ORF: Nationalrat beschließt Strommarktgesetz, 11.12.2025", "https://orf.at/stories/3414143/"),
        ("WKO: Elektrizitätswirtschaftsgesetz (ElWG)", "https://www.wko.at/energie/elektrizitaetswirtschaftsgesetz-elwg"),
        ("Parlament: Nationalrat beschließt Senkung der Elektrizitätsabgabe",
         "https://www.parlament.gv.at/aktuelles/news/Nationalrat-beschliesst-Senkung-der-Elektrizitaetsabgabe"),
        ("BMF: Aussetzung von Ökostrompauschale und Förderbeitrag 2027",
         "https://www.bmf.gv.at/presse/pressemeldungen/2026/november-2026/oekostrompauschale.html"),
    ],
    "related": [
        ("/energiegemeinschaft/", "Energiegemeinschaft: 5 Modelle nach ElWG"),
        ("/peer-to-peer-strom/", "Peer-to-Peer-Strom: Strom direkt teilen"),
        ("batteriespeicher", "Batteriespeicher: Mittagsstrom für den Abend"),
        ("/smart-meter-opt-out/", "Smart Meter Opt-out: Rechte und Folgen"),
    ],
    "cta": {
        "h3": "Anlage nach ElWG planen",
        "text": "Wir planen mit Spitzenkappung, Steuerbarkeit, Ihrem Lastprofil und der passenden Speichergröße.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihr Dach wird zum Kraftwerk",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Ansprechpartner aus Villach, der Netzanzeige, "
                   "Montage und Inbetriebnahme koordiniert."),
}
