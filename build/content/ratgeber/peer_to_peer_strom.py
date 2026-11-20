"""Ratgeber: Peer-to-Peer-Strom (P2P-Vertrag nach ElWG): PV-Strom an Nachbarn, Familie oder Betrieb
verkaufen oder verschenken.

Neuer Artikel (kein WordPress-Vorgänger), erstellt 2026-11-20.
Ziel-Keywords (Google Ads, Österreich, 20.11.2026): peer to peer strom 480 (Oktober 2026: 2.900),
peer-to-peer strom österreich 390 (Oktober 1.600), pv strom verkaufen 170, peer to peer verträge österreich 110
(Oktober 480), strom teilen 40 (Oktober 170), strom verschenken 40 (Oktober 170), strom an nachbarn
verkaufen 20 (Oktober 90), peer-to-peer strom ab wann 30 (Oktober 110).

Faktenbasis (am 20.11.2026 selbst geöffnet): Koordinationsstelle energiegemeinschaften.gv.at (Seiten
/peer-to-peer-vertraege/, /faqs-zum-elwg/, /lieferantenverpflichtungen/, /mehrfachteilnahme/,
/gemeinsame-energienutzung/), BMWET-Pressemeldung 2.10.2026, Energie Steiermark (P2P-Infoseite),
Netz Niederösterreich (P2P-Anmeldung), E-Control Presseunterlage SNE-G-V 12.10.2026, OeMAG-Marktpreis,
BMF Überschusseinspeisung (Stand 7.8.2025). Faktenliste build/seo/_fakten_2026-10.md (Abschnitt ab 20.11.2026).
Nicht behauptet: Höhe des Netzentgelt-Rabatts für P2P ab 2027 (legt die E-Control fest), steuerliche
Behandlung von P2P-Verkäufen (nicht geregelt bzw. nicht veröffentlicht), P2P-Handelsplattformen
(smartCOMMUNITY der Energie Steiermark ist laut deren Seite ein EG-Produkt, keine P2P-Plattform),
konkrete Anmeldeschritte bei Kärnten Netz (keine Quelle gefunden).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "peer-to-peer-strom",
    "path": "/peer-to-peer-strom/",
    "cluster": "Energiegemeinschaft",
    "title": "Peer-to-Peer-Strom: PV-Strom an Nachbarn verkaufen | EBZ",
    "description": ("Peer-to-Peer-Strom nach ElWG: PV-Strom seit Oktober 2026 an Nachbarn, Familie oder Betrieb "
                    "verkaufen oder verschenken. Ablauf, Netzentgelt, Rechenbeispiel."),
    "eyebrow": "Energiegemeinschaft · Peer-to-Peer",
    "crumb_label": "Peer-to-Peer-Strom",
    "h1": "Peer-to-Peer-Strom: Seit Oktober 2026 PV-Strom direkt an Nachbarn verkaufen oder verschenken",
    "lead": ("Mit einem Peer-to-Peer-Vertrag geben Sie Strom aus Ihrer Photovoltaikanlage direkt an eine andere "
             "Person oder einen Betrieb weiter, ohne Verein und ohne Energiegemeinschaft. Den Preis legen Sie selbst "
             "fest, auch null Cent sind erlaubt. Dieser Ratgeber zeigt, was dafür nötig ist, was es heute schon bringt "
             "und wo die Grenzen in der Startphase liegen."),
    "chips": [
        "Rechtsgrundlage: <b>§ 6 Abs. 1 Z 124 ElWG</b>",
        "Umsetzbar seit <b>5. Oktober 2026</b>",
        "Netzübergreifend: voraussichtlich <b>ab April 2027</b>",
        "Preis: <b>frei vereinbar</b>, auch 0 Cent",
    ],
    "date_published": "2026-11-20",
    "date_modified": "2026-11-20",
    "hero_img": "eg_drohne",
    "hero_alt": "Kleine Ortschaft mit Einfamilienhäusern zwischen Wiesen und Feldern aus der Luft im Abendlicht",

    "tldr": [
        "Ein Peer-to-Peer-Vertrag (P2P) ist laut § 6 Abs. 1 Z 124 ElWG der Verkauf oder die Schenkung von "
        "erneuerbarem Strom zwischen zwei oder mehr Parteien. Privatpersonen, Unternehmen und Gemeinden dürfen "
        "teilnehmen, eine Rechtsform braucht es nicht, Gewinnabsicht ist erlaubt.",
        "Voraussetzungen: funktionierender Smart Meter bei allen Beteiligten, Registrierung über ebUtilities und "
        "das EDA-Portal, Zustimmung jedes Teilnehmers im Webportal des Netzbetreibers. Geteilt wird viertelstündlich.",
        "Seit 5. Oktober 2026 geht P2P vorerst nur zwischen Zählpunkten beim selben Netzbetreiber. Über mehrere "
        "Netzgebiete, etwa von Kärnten in die Steiermark, voraussichtlich erst ab April 2027.",
        "Bis Ende 2026 gibt es für P2P keinen Netzentgelt-Rabatt, die Abgabenbefreiung gilt derzeit nur in der "
        "Erneuerbare-Energie-Gemeinschaft. Reduzierte Netzentgelte im Nahbereich sollen voraussichtlich ab 1. Jänner "
        "2027 kommen, die Höhe legt die E-Control fest.",
        "Ob sich der Verkauf rechnet, hängt vom OeMAG-Marktpreis ab: Oktober 2026 14,874 Cent, September 10,168 "
        "Cent, Juli 6,146 Cent. Ein P2P-Preis bringt nicht automatisch mehr als die Einspeisung.",
    ],
    "kpis": [
        ("2", "Parteien reichen für einen P2P-Vertrag"),
        ("15 Min.", "Takt, in dem der Strom zugeteilt wird"),
        ("5", "Bürgerenergie-Modelle je Zählpunkt möglich"),
        ("14,874 ct", "OeMAG-Marktpreis Oktober 2026 zum Vergleich"),
    ],

    "sections": [
        ("Was ist Peer-to-Peer-Strom? Die Definition im ElWG", "definition", f"""
<p><b>Peer-to-Peer-Strom bedeutet: Sie verkaufen oder verschenken Strom aus Ihrer eigenen Erzeugungsanlage
direkt an einen anderen Stromkunden, auf Basis eines Vertrags mit vorab festgelegten Bedingungen.</b> So
definiert das Elektrizitätswirtschaftsgesetz (ElWG) den Peer-to-Peer-Vertrag in § 6 Abs. 1 Z 124. Geregelt
ist das Modell in den Bestimmungen zur gemeinsamen Energienutzung (§§ 65 bis 72 ElWG), die seit
1. Oktober 2026 gelten. Laut Koordinationsstelle für Energiegemeinschaften ist die Umsetzung seit
5. Oktober 2026 möglich.</p>
<p>Teilnehmen dürfen natürliche und juristische Personen: Privathaushalte, Unternehmen und Gemeinden. Das
Wirtschaftsministerium nennt in seiner Pressemeldung vom 2. Oktober 2026 als typische Fälle die Familie,
die Nachbarn und andere Betriebe. Unternehmen können zudem Strom mit Kunden oder Mitarbeitern teilen oder
eigene Standorte versorgen. Große Unternehmen dürfen bis zu 6 MW Erzeugungsleistung je Zählpunkt
einbringen.</p>
<ul>
  <li><b>Kein Verein, keine Genossenschaft:</b> Ein Vertrag zwischen den Beteiligten genügt.</li>
  <li><b>Verkaufen oder schenken:</b> Der Preis wird in Cent je kWh vereinbart, ein Nulltarif ist erlaubt.</li>
  <li><b>Gewinnabsicht erlaubt:</b> Sie dürfen am Verkauf verdienen.</li>
  <li><b>Ihr Stromliefervertrag bleibt:</b> P2P deckt nur den geteilten Überschuss. Den Rest liefert weiter Ihr
  frei gewählter Lieferant.</li>
</ul>
<p>Den rechtlichen Hintergrund zum neuen Gesetz finden Sie im Ratgeber
{a('/elwg-beschluss-oesterreich/', 'ElWG: Was das neue Strommarktgesetz ändert')}.</p>
"""),
        ("P2P-Vertrag oder Energiegemeinschaft: die Unterschiede", "vergleich", f"""
<p><b>Der P2P-Vertrag braucht keine Rechtsform und erlaubt Gewinnabsicht, bringt 2026 aber weniger
Kostenvorteile als eine Energiegemeinschaft.</b> Den Netzentgelt-Rabatt und die Abgabenbefreiung bekommt derzeit nur die
Erneuerbare-Energie-Gemeinschaft (EEG) im Nahbereich.</p>
{A.table(
    ["", "Peer-to-Peer-Vertrag", "Energiegemeinschaft (EEG)", "Bürgerenergiegemeinschaft (BEG)", "Gemeinschaftliche Erzeugungsanlage (GEA)"],
    [
        ["Rechtsform", "keine, nur Vertrag", "nötig (z. B. Verein, Genossenschaft)", "nötig", "keine nötig"],
        ["Gebiet", "Nahbereich oder österreichweit*", "lokal oder regional", "Nahbereich oder österreichweit*",
         "gemeinsame Hauptleitung im Gebäude"],
        ["Netzentgelt-Rabatt", "keiner bis Ende 2026, danach im Nahbereich voraussichtlich", "ja, lokal und regional",
         "keiner bis Ende 2026, danach im Nahbereich voraussichtlich", "kein öffentliches Netz genutzt"],
        ["Abgabenbefreiung", "nicht geregelt", "ja", "nein", "Elektrizitätsabgabe entfällt"],
    ],
    hl_cols=(1,),
)}
<p><small>*Netzübergreifend erst, wenn die Übergangsphase endet (voraussichtlich April 2027). Quelle: FAQ
und Modellseiten der Koordinationsstelle für Energiegemeinschaften, Stand 20. November 2026.</small></p>
<p>Welches Modell zu Ihnen passt, vergleicht der Ratgeber
{a('/energiegemeinschaft-vergleich/', 'Energiegemeinschaft: alle Modelle im Vergleich')}. Details zu den
anderen Modellen: {a('/buergerenergiegemeinschaft/', 'Bürgerenergiegemeinschaft')},
{a('/gemeinschaftliche-erzeugungsanlage/', 'Gemeinschaftliche Erzeugungsanlage')} und der Überblick
{a('/energiegemeinschaft/', 'Energiegemeinschaft in Österreich')}.</p>
{A.box("Sie müssen sich nicht entscheiden: Jeder Zählpunkt darf an bis zu fünf Bürgerenergie-Modellen "
       "gleichzeitig teilnehmen, etwa an einer EEG und einem P2P-Vertrag. Ein Teilnahmefaktor legt fest, welcher "
       "Anteil je Viertelstunde in welches Modell geht, in Summe höchstens 100 %. Der Faktor lässt sich einmal "
       "täglich ändern, ab 2028 voraussichtlich mehrmals täglich. Eine Rangfolge der Modelle gibt es nicht.",
       label="Kombinieren geht:")}
"""),
        ("Voraussetzungen und Ablauf: Strom an Nachbarn verkaufen in 6 Schritten", "ablauf", f"""
<p><b>Alle Beteiligten brauchen einen funktionierenden Smart Meter, der Viertelstundenwerte liefert, einen
bestehenden Stromliefervertrag und einen Netzzugang.</b> Wer den Smart Meter abgelehnt hat
({a('/smart-meter-opt-out/', 'Opt-out')}), kann so nicht teilnehmen. Was der Zähler misst, erklärt der
Ratgeber {a('/smart-meter/', 'Smart Meter')}. Den P2P-Vertrag selbst müssen Sie dem Netzbetreiber nicht
vorlegen.</p>
{A.steps([
    ("Partner und Bedingungen festlegen", "Wer liefert an wen, zu welchem Preis je kWh, wie wird abgerechnet? Die "
     "Koordinationsstelle bietet zwei Mustervorlagen: eine für 1:1 und 1:n, eine für n:n."),
    ("Zählpunkte klären", "Beide Zählpunktnummern stehen auf der Netzrechnung. In der Startphase müssen alle "
     "Zählpunkte beim selben Netzbetreiber liegen."),
    ("Registrieren bei ebUtilities", "Benutzerkonto anlegen, als Modell P2P wählen, Stammdaten und Nachweise "
     "hochladen. Nach der Prüfung gibt es eine Marktpartnerkennung und eine Gemeinschafts-ID."),
    ("Anmeldung beim Netzbetreiber", "Über das EDA-Portal werden die Zählpunkte angemeldet. Dabei wird der "
     "Nahbereich festgelegt (Standort-, Lokal- oder Regionalbereich), der später über reduzierte Netzentgelte entscheidet."),
    ("Zustimmung im Netzportal", "Jeder Teilnehmer stimmt im Webportal seines Netzbetreibers der Teilnahme seines "
     "Zählpunkts zu. Erst dann ist der Austausch aktiv."),
    ("Abrechnen", "Der Netzbetreiber stellt die Viertelstundenwerte über das EDA-Portal bereit, rechnet aber nicht ab. "
     "Der Erzeuger stellt dem Abnehmer selbst eine Rechnung, oder ein beauftragter Dienstleister übernimmt das."),
])}
<p>Wie die Schritte in der Praxis aussehen, beschreiben etwa Netz Niederösterreich und Energie Steiermark
auf ihren P2P-Seiten. Welcher Netzbetreiber für Sie zuständig ist, steht auf Ihrer Netzrechnung.</p>
{A.cta("Genug Überschuss zum Teilen?",
       "Wir planen Ihre Photovoltaikanlage so, dass sie zu Ihrem Verbrauch passt, und zeigen Ihnen, ob sich "
       "Teilen, Speichern oder Einspeisen mehr lohnt.",
       secondary=("eg_privat", "Energiegemeinschaft mit EBZ"))}
"""),
        ("Preis, Rechnung, Pflichten: was der Verkäufer wissen muss", "pflichten", f"""
<p><b>Den Preis je Kilowattstunde vereinbaren Sie frei, vom Geschenk bis zum Verkauf mit Gewinn.</b> Eine
Liefergarantie gibt es nicht: Weder müssen Sie eine Mindestmenge liefern, noch muss Ihr Nachbar eine
Mindestmenge abnehmen. Zugeteilt wird je Viertelstunde, was Sie tatsächlich übrig haben und Ihr Partner
tatsächlich verbraucht. Was er nicht braucht, vermarkten Sie wie bisher selbst, etwa über die
{a('/oemag-einspeisetarif/', 'OeMAG')} oder Ihren Einspeisevertrag.</p>
<ul>
  <li><b>Rechnung:</b> Der Erzeuger stellt dem Abnehmer eine Rechnung auf Basis der EDA-Daten. Bei mehreren
  Teilnehmern im n:n-Modell stellt jeder Erzeuger jedem Abnehmer eine eigene Rechnung, das wird schnell aufwendig.</li>
  <li><b>Laufzeit und Kündigung:</b> Der Mustervertrag läuft unbefristet. Für Haushalte und Kleinunternehmen gilt
  grundsätzlich eine Kündigungsfrist von zwei Wochen.</li>
  <li><b>Lieferantenpflichten:</b> Bringt ein Haushalt Erzeugungs- und Speicheranlagen mit mehr als 30 kW ein,
  gelten Pflichten wie für einen Stromlieferanten (Lieferbedingungen, Informationsblatt, Rechnung mit
  Mindestinhalten). Für Unternehmen liegt die Grenze bei 100 kW. Die Mustervorlagen enthalten die allgemeinen
  Lieferbedingungen bereits.</li>
  <li><b>Dienstleister möglich:</b> Abrechnung, Kommunikation mit dem Netzbetreiber und Lieferantenpflichten kann
  ein beauftragter Organisator oder Aggregator übernehmen.</li>
  <li><b>Haftung:</b> Für Mess- oder Zuteilungsfehler des Netzbetreibers haften die Vertragsparteien nicht.</li>
</ul>
<p>Für den Abnehmer wichtig: Sein Lieferant darf ihn laut ElWG nicht benachteiligen, weil er zusätzlich
P2P-Strom bezieht, und keine Mindestabnahme verlangen (§ 72 ElWG laut FAQ der Koordinationsstelle).</p>
"""),
        ("Netzentgelt, Abgaben und Übergangsphase: der Stand im November 2026", "netzentgelt", f"""
<p><b>Peer-to-Peer spart dem Abnehmer derzeit nur den Energiepreis seines Lieferanten, nicht die Netzkosten.</b>
Netzentgelte, Abgaben und Steuern fallen auf den geteilten Strom weiter an.</p>
{A.table(
    ["Thema", "Oktober bis Dezember 2026", "Ab 2027"],
    [
        ["Netzentgelt im Nahbereich", "kein Rabatt für P2P (nur Mitglieder lokaler und regionaler EEG)",
         "reduzierte Netzentgelte voraussichtlich ab 1. Jänner 2027, Höhe per Verordnung der E-Control"],
        ["Netzentgelt österreichweit", "volle Netzentgelte", "volle Netzentgelte (kein Nahbereich)"],
        ["Elektrizitätsabgabe, Erneuerbaren-Förderbeitrag", "Entfall nur in der EEG", "für P2P nicht geregelt"],
        ["Teilnehmer", "nur Zählpunkte beim selben Netzbetreiber",
         "über mehrere Netzgebiete voraussichtlich ab April 2027"],
    ],
    hl_cols=(2,),
)}
<p>Die Rabatte gelten nur, wenn alle Zählpunkte im selben Nahbereich liegen: im Lokalbereich am selben
Niederspannungs-Trafo (laut Koordinationsstelle rund 1 km), im Regionalbereich am selben Umspannwerk
(rund 30 km). Teilen Sie österreichweit, zum Beispiel mit der Tochter in Wien (voraussichtlich ab April
2027), bleiben die Netzentgelte in voller Höhe. Wie viel der bisherige EEG-Rabatt ausmacht, rechnet der Ratgeber
{a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft: Netzkosten')} vor.</p>
{A.box("Für Haushalte ändert sich ab 2027 auch die Netzentgeltstruktur: Laut E-Control kommt schrittweise ein "
       "Leistungspreis dazu, der sich am höchsten 15-Minuten-Wert eines Monats orientiert. Die Einführung kann je "
       "Netzbereich zwischen 1. Jänner 2027 und spätestens 1. Juli 2028 erfolgen.",
       label="Gut zu wissen:")}
"""),
        ("Rechenbeispiel: PV-Strom verkaufen oder einspeisen?", "rechnung", f"""
<p><b>Ein P2P-Verkauf lohnt sich für Sie nur, wenn der vereinbarte Preis über dem liegt, was Sie für die
Einspeisung bekommen.</b> Der OeMAG-Marktpreis schwankt jeden Monat stark. Beispiel: Sie geben im Jahr
2.000 kWh Überschuss an Ihren Nachbarn weiter.*</p>
{A.table(
    ["Weg", "Preis je kWh", "Erlös für 2.000 kWh*"],
    [
        ["Einspeisung zum OeMAG-Marktpreis Oktober 2026", "14,874 ct", "rund 297 €"],
        ["Einspeisung zum OeMAG-Marktpreis September 2026", "10,168 ct", "rund 203 €"],
        ["Einspeisung zum OeMAG-Marktpreis Juli 2026", "6,146 ct", "rund 123 €"],
        ["P2P-Verkauf an den Nachbarn (Beispielpreis*)", "12 ct", "240 €"],
        ["P2P-Schenkung an die Tochter", "0 ct", "0 €"],
    ],
    hl_cols=(2,),
)}
<p>Mit 12 Cent liegen Sie in diesem Beispiel unter dem Oktober-Marktpreis, aber deutlich über dem Juli-Wert.
Weil eine PV-Anlage den meisten Überschuss im Sommerhalbjahr erzeugt, zählen vor allem die Sommermonate.
Aktuelle Werte: {a('marktpreis', 'Marktpreis 2026')}.</p>
<p><b>Für den Nachbarn</b> ersetzt jede geteilte Kilowattstunde nur den Energiepreis seines Lieferanten.
Haushaltsstrom kostet in Kärnten und der Steiermark zwar rund 28 bis 35 Cent je kWh (E-Control, November
2026), darin stecken aber Netzentgelte, Abgaben und Steuern, die er 2026 weiter voll zahlt. Ob 12 Cent für
ihn günstig sind, zeigt der Vergleich mit dem Energiepreis je kWh auf seiner Stromrechnung.</p>
{A.box("Peer-to-Peer ist kein Weg zu garantiert höheren Erlösen. Es lohnt sich vor allem, wenn Sie Strom gezielt "
       "Familie oder Nachbarn zukommen lassen wollen, wenn der Marktpreis niedrig ist oder wenn ab 2027 der "
       "Netzentgelt-Rabatt im Nahbereich dazukommt.",
       label="Ehrlich gerechnet:")}
"""),
        ("Steuern und Gewerbe: was Sie vorher klären sollten", "steuern", f"""
<p><b>Wie Einnahmen aus einem P2P-Vertrag steuerlich behandelt werden, ist offiziell noch nicht
beschrieben.</b> Für die Einspeisung von PV-Strom gilt laut Finanzministerium: Einkünfte aus bis zu
12.500 kWh im Jahr sind einkommensteuerfrei, wenn die Anlage höchstens 35 kWp Engpassleistung und 25 kW
Anschlussleistung hat (§ 3 Abs. 1 Z 39 EStG). Umsatzsteuerlich gilt der Betreiber bei Überschusseinspeisung
als Unternehmer, bis 55.000 Euro Jahresumsatz greift die Kleinunternehmerregelung. Peer-to-Peer erwähnt
das BMF dabei nicht.</p>
<ul>
  <li><b>Gewerbeordnung:</b> Laut Koordinationsstelle ist sie beim P2P-Vertrag, anders als bei EEG und BEG,
  nicht ausgenommen. Ob regelmäßiger Verkauf mit Gewinn eine Gewerbeberechtigung braucht, klären Sie mit der
  Wirtschaftskammer oder Ihrer Steuerberatung.</li>
  <li><b>Schenkung:</b> Strom zum Nulltarif ist ausdrücklich erlaubt. Eine offizielle Aussage zu steuerlichen Folgen haben wir nicht gefunden.</li>
</ul>
<p>Unser Rat: Bevor Sie Strom gegen Geld abgeben, kurz mit der Steuerberatung sprechen, besonders wenn Sie
schon einspeisen oder mehrere Abnehmer beliefern wollen.</p>
"""),
        ("Fazit: Für wen sich Peer-to-Peer lohnt", "fazit", f"""
<p>Peer-to-Peer ist der einfachste Weg, eigenen Sonnenstrom an einen bestimmten Menschen oder Betrieb
weiterzugeben: ohne Verein, mit frei gewähltem Preis. Passend ist es für Eltern und Kinder im selben
Netzgebiet, für zwei Nachbarn oder für einen Betrieb, der Mitarbeiter mit Strom versorgen will. Finanziell
ist der Vorteil 2026 begrenzt, weil Netzentgelt-Rabatt und Abgabenbefreiung fehlen. Wer
mehrere Teilnehmer am selben Trafo hat, fährt mit einer {a('/energiegemeinschaft-gruenden/', 'eigenen EEG')}
oder dem {a('/energiegemeinschaft-beitreten/', 'Beitritt zu einer bestehenden Gemeinschaft')} derzeit
besser. Was wir bisher gebaut haben, zeigen unsere {a('referenzen', 'Referenzen')}.</p>
<p><small>*Beispielwerte und eigene Berechnungen: 2.000 kWh geteilter Überschuss im Jahr und 12 Cent je kWh
sind angenommene Werte, keine Konditionen von EBZ (EBZ verkauft keinen Strom). OeMAG-Marktpreise laut
oem-ag.at, Haushaltsstrom laut E-Control-Preismonitor November 2026. Rechtsstand 20. November 2026; Netzentgelte
ab 2027 und netzübergreifende Umsetzung stehen noch nicht endgültig fest.</small></p>
{A.cta("Sonnenstrom selbst nutzen, teilen oder einspeisen?",
       "Wir planen Photovoltaik, Speicher und Energiemanagement für Ihr Haus und rechnen ehrlich durch, welcher "
       "Weg für Ihren Überschuss am meisten bringt.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("photovoltaik", "Photovoltaik von EBZ"))}
"""),
    ],

    "partner": {
        "h2": "Photovoltaik zum Teilen: Was EBZ Energie übernimmt",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und montiert Photovoltaik, Batteriespeicher und Energiemanagement in "
                 "Kärnten und der Steiermark, mit zertifizierten Fachkräften und einem festen Ansprechpartner von der "
                 "Planung bis zur Übergabe. Für Energiegemeinschaften binden wir Ihre Anlage an eine Gemeinschaft an, "
                 "abgerechnet über die Plattform unseres Partners energyfamily. Beim P2P-Vertrag zeigen wir Ihnen die "
                 "Schritte und prüfen, ob eine Energiegemeinschaft für Sie mehr bringt. EBZ ist kein Energieversorger "
                 "und verkauft keinen Strom."),
        "grid": [
            ("Anlage mit Überschuss", "Projektbericht mit 3D-Belegplan und Statikreport für Ihr Dach."),
            ("Speicher und EMS", "Überschuss dorthin lenken, wo er am meisten wert ist."),
            ("Modell-Check", "P2P, EEG oder BEG: ehrlich verglichen für Ihren Fall."),
            ("Anbindung", "Aufnahme in eine Energiegemeinschaft, Abrechnung über energyfamily."),
        ],
    },

    "faq": [
        ("Was ist ein Peer-to-Peer-Vertrag für Strom?",
         "Ein Vertrag, mit dem Sie erneuerbaren Strom aus Ihrer eigenen Anlage direkt an andere Stromkunden verkaufen "
         "oder verschenken (§ 6 Abs. 1 Z 124 ElWG). Es braucht keinen Verein und keine Energiegemeinschaft, "
         "Gewinnabsicht ist erlaubt. Zugeteilt wird viertelstündlich nach tatsächlicher Erzeugung und tatsächlichem Verbrauch."),
        ("Kann ich in Österreich Strom an meinen Nachbarn verkaufen?",
         "Ja, seit Oktober 2026 per Peer-to-Peer-Vertrag. Beide brauchen einen funktionierenden Smart Meter, die "
         "Zählpunkte werden über ebUtilities und das EDA-Portal angemeldet, und jeder stimmt im Netzportal zu. In der "
         "Startphase müssen beide Zählpunkte beim selben Netzbetreiber liegen."),
        ("Kann ich Strom an Familie oder Freunde verschenken?",
         "Ja, der Preis darf null Cent je kWh betragen. Verschenken lässt sich so zum Beispiel Strom an die Eltern oder "
         "an Kinder in einem anderen Haus. Netzübergreifend, etwa von Kärnten nach Wien, geht das voraussichtlich erst "
         "ab April 2027, und österreichweit fallen die Netzentgelte voll an."),
        ("Ab wann ist Peer-to-Peer-Strom möglich?",
         "Die Bestimmungen gelten seit 1. Oktober 2026, umgesetzt werden können P2P-Verträge seit 5. Oktober 2026, "
         "vorerst nur zwischen Zählpunkten beim selben Netzbetreiber. Über mehrere Netzgebiete und österreichweit soll "
         "das voraussichtlich ab April 2027 möglich sein."),
        ("Spart der Abnehmer beim P2P-Strom Netzentgelte?",
         "Bis Ende 2026 nicht: Reduzierte Netzentgelte bekommen derzeit nur Mitglieder lokaler und regionaler "
         "Erneuerbare-Energie-Gemeinschaften. Für P2P im Nahbereich sollen sie voraussichtlich ab 1. Jänner 2027 "
         "kommen, die Höhe legt die E-Control per Verordnung fest. Österreichweit bleibt es bei vollen Netzentgelten."),
        ("Lohnt sich Peer-to-Peer mehr als die Einspeisung?",
         "Nicht automatisch. Der OeMAG-Marktpreis lag im Oktober 2026 bei 14,874 Cent, im Juli bei 6,146 Cent. Ein "
         "P2P-Preis von 12 Cent bringt mehr als der Juli-Marktpreis, aber weniger als der Oktober-Marktpreis. Der Abnehmer spart nur den Energiepreis "
         "seines Lieferanten, Netzentgelte und Abgaben zahlt er 2026 weiter."),
        ("Muss ich P2P-Einnahmen versteuern?",
         "Das ist für P2P noch nicht offiziell beschrieben. Für eingespeisten PV-Strom gilt laut BMF eine "
         "Einkommensteuerbefreiung bis 12.500 kWh im Jahr bei Anlagen bis 35 kWp und 25 kW Anschlussleistung. Die "
         "Gewerbeordnung ist beim P2P-Vertrag nicht ausgenommen. Klären Sie den Verkauf vorab mit Ihrer Steuerberatung."),
        ("Kann ich P2P und Energiegemeinschaft kombinieren?",
         "Ja. Jeder Zählpunkt darf an bis zu fünf Bürgerenergie-Modellen teilnehmen. Ein Teilnahmefaktor regelt, "
         "welcher Anteil in welches Modell geht, in Summe höchstens 100 %, änderbar einmal täglich."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Mit zertifizierten Fachkräften plant und "
                    "installiert EBZ Energie Photovoltaik, Speicher und Energiemanagement in Kärnten und der Steiermark "
                    "und bindet Anlagen an Energiegemeinschaften an. Rechenwerte in diesem Ratgeber sind Beispiele. "
                    "Keine Rechts- oder Steuerberatung, maßgeblich sind ElWG, Verordnungen und die Angaben Ihres "
                    "Netzbetreibers."),
    "sources": [
        ("Koordinationsstelle für Energiegemeinschaften: Peer-to-Peer-Verträge",
         "https://energiegemeinschaften.gv.at/peer-to-peer-vertraege/"),
        ("Koordinationsstelle für Energiegemeinschaften: FAQs zum ElWG",
         "https://energiegemeinschaften.gv.at/faqs-zum-elwg/"),
        ("Koordinationsstelle für Energiegemeinschaften: Lieferantenverpflichtungen",
         "https://energiegemeinschaften.gv.at/lieferantenverpflichtungen/"),
        ("Koordinationsstelle für Energiegemeinschaften: Mehrfachteilnahme",
         "https://energiegemeinschaften.gv.at/mehrfachteilnahme/"),
        ("Koordinationsstelle für Energiegemeinschaften: Gemeinsame Energienutzung und Nahebereiche",
         "https://energiegemeinschaften.gv.at/gemeinsame-energienutzung/"),
        ("BMWET: Peer-to-Peer-Verträge, Pressemeldung vom 2. Oktober 2026",
         "https://www.bmwet.gv.at/Presse/AktuellePressemeldungen/peer-to-peer.html"),
        ("Netz Niederösterreich: Peer-to-Peer (P2P) gründen",
         "https://netz-noe.at/strom/buergerenergiemodelle/p2p-peer-to-peer"),
        ("Energie Steiermark: Peer-to-Peer-Stromverträge",
         "https://www.e-steiermark.com/privat/entdecken/smarter-strom/peer-to-peer-stromvertraege"),
        ("E-Control: Presseunterlage zur Systemnutzungsentgelte-Grundsatzverordnung, 12. Oktober 2026",
         "https://www.e-control.at/documents/d/guest/2026-10-12-presseunterlage_sne-g-v-pdf"),
        ("E-Control: Preismonitor", "https://www.e-control.at/preismonitor"),
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/de/marktpreis/"),
        ("BMF: Photovoltaik bei Privatpersonen, Überschusseinspeisung",
         "https://www.bmf.gv.at/themen/klimapolitik/steuerliche-aspekte-bei-photovoltaikanlagen-von-privatpersonen/ueberschusseinspeisung.html"),
    ],
    "related": [
        ("/energiegemeinschaft/", "Energiegemeinschaft in Österreich: alle Modelle"),
        ("/energiegemeinschaft-privat/", "Energiegemeinschaft privat: mit Familie und Nachbarn"),
        ("eg_privat", "Energiegemeinschaft mit EBZ: Anlage und Anbindung"),
        ("/oemag-einspeisetarif/", "OeMAG-Einspeisetarif: was Einspeisen bringt"),
    ],
    "cta": {
        "h3": "Strom teilen oder selbst nutzen?",
        "text": "Wir rechnen Photovoltaik, Speicher und Energiegemeinschaft für Ihren Fall ehrlich durch.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihr Sonnenstrom, sinnvoll verteilt",
    "final_text": ("Kostenlose Erstberatung zu Photovoltaik, Speicher, Energiemanagement und Energiegemeinschaft, "
                   "mit transparenten Zahlen und einem Ansprechpartner aus Villach."),
}
