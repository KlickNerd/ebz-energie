"""Ratgeber: Energiegemeinschaft Kärnten.

Migriert von ebz-photovoltaik.at/energiegemeinschaft-kaernten/ (Stand August 2026),
Inhalt freigegeben, auf die Ratgeber-Vorlage umgestellt. Rechner-/EG-Preise sind
Beispielwerte (Sternchen), Netzentgelt-Abschläge laut E-Control 2026.
20.11.2026: ElWG-Übergangsphase korrigiert, Tariftabelle Kärntner Anbieter (nur selbst
geprüfte Anbieterseiten, Stand November 2026), Regionen-Abschnitt mit Firmenbuch-/
Gemeindebelegen, Elektrizitätsabgabe 2026 (0,1 ct Haushalt, 0,82 ct Betrieb) korrigiert.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a


def _ext(url, text):
    """Externer Link (Quellenangabe in Tabellen)."""
    return f'<a href="{url}" rel="nofollow noopener" target="_blank">{text}</a>'


ARTICLE = {
    "slug": "energiegemeinschaft-kaernten",
    "path": "/energiegemeinschaft-kaernten/",
    "title": "Energiegemeinschaft Kärnten: Anbieter, Tarife 2026 | EBZ",
    "description": "Energiegemeinschaft Kärnten: Tarife von BEG Kärnten, Raiffeisen und regionalen EEGs im Vergleich, bis 57 % Netzrabatt, Gemeinschaften je Region, Einstieg mit EBZ.",
    "eyebrow": "Energiegemeinschaft · Kärnten",
    "crumb_label": "Energiegemeinschaft Kärnten",
    "h1": "Energiegemeinschaft in Kärnten: Anbieter, Tarife und Netzrabatt im Überblick",
    "lead": ("Welche Energiegemeinschaften es in Kärnten gibt, was sie für Bezug und Einspeisung verrechnen und wie viel "
             "Netzentgelt Sie sparen: Hier stehen die veröffentlichten Tarife (Stand November 2026), die Gemeinschaften "
             "in den Regionen und der Einstieg mit EBZ Energie."),
    "chips": [
        "Netzentgelt in der EEG: <b>bis zu 57 %</b> weniger",
        "EG-Einspeisung Kärnten: <b>8,0 bis 10,0 ct</b>",
        "OeMAG Okt. 2026: <b>14,874 ct/kWh</b>",
        "Start in <b>4 bis 8 Wochen</b>",
    ],
    "date_published": "2026-08-05",
    "date_modified": "2026-11-20",
    "hero_img": "eg_drohne",
    "hero_alt": "Ortschaft in Kärnten aus der Luft mit Photovoltaikanlagen auf mehreren Dächern",

    "tldr": [
        "Eine Energiegemeinschaft (EG) lässt Sie PV-Überschuss zu einem vereinbarten Preis an Haushalte "
        "und Betriebe verkaufen, statt ihn zum monatlich schwankenden OeMAG-Marktpreis abzugeben "
        "(Juli 2026: 6,146 Cent, Oktober 2026: 14,874 Cent). Je nach Monat liegt der EG-Preis darüber oder darunter, "
        "dafür ist er planbar.",
        "Veröffentlichte Tarife in Kärnten (Stand November 2026): Bezug 10,0 bis 12,5 Cent netto, Einspeisung "
        "8,0 bis 10,0 Cent je kWh, Anbieter sind unter anderem BEG Kärnten, die Raiffeisen Energie-Genossenschaften "
        "und regionale EEGs.",
        "Der Netzbetreiber bestimmt den Nahbereich: in den meisten Gemeinden die Kärnten Netz, im Stadtgebiet "
        "Klagenfurt die Energie Klagenfurt. Derselbe Trafo bedeutet lokal (minus 57 Prozent Netzentgelt in der EEG), "
        "dasselbe Umspannwerk regional (minus 28 Prozent).",
        "Erneuerbare-Energie-Gemeinschaften sind zusätzlich von Elektrizitätsabgabe (2026: 0,1 Cent je kWh für "
        "Haushalte, 0,82 Cent für Betriebe, ab 2027 wieder 1,5 Cent) und Erneuerbaren-Förderbeitrag befreit. Für BEG "
        "und Peer-to-Peer gilt das nicht. Den Förderbeitrag setzt die Bundesregierung 2027 ohnehin für alle aus.",
        "EBZ Energie aus Villach plant und montiert die PV-Anlage, bindet Sie an eine Gemeinschaft an und wickelt "
        "Zählpunktfreigabe und Abrechnung über die Plattform energyfamily ab.",
    ],
    "kpis": [
        ("~1.100 kWh", "Jahresertrag je kWp in Kärnten"),
        ("14,874 ct", "OeMAG-Marktpreis Oktober 2026 (Juli: 6,146 ct)"),
        ("57 %", "Netzentgelt-Abschlag lokale EEG (Arbeitspreis)"),
        ("8 bis 10 ct", "EG-Einspeisepreise Kärntner Anbieter, Stand Nov. 2026"),
    ],

    "sections": [
        ("Was eine Energiegemeinschaft in Kärnten konkret ist", "was-ist", f"""
<p>Eine Energiegemeinschaft ist ein Zusammenschluss von mindestens zwei Teilnehmern, die Strom aus erneuerbaren
Quellen gemeinsam erzeugen, teilen und verbrauchen. Rechtsgrundlage war seit 2021 das Erneuerbaren-Ausbau-Gesetz,
seit 1. Oktober 2026 regelt das neue Elektrizitätswirtschaftsgesetz (ElWG) die gemeinsame Energienutzung. Für Sie als
Hausbesitzer in Kärnten bedeutet das: Der Strom, den Ihre {a('photovoltaik', 'PV-Anlage')} mittags zu viel produziert,
geht nicht mehr nur an die OeMAG oder Ihren Lieferanten, sondern an Nachbarn, Betriebe oder die Gemeinde im selben
Netzgebiet. Zu einem Preis, den die Gemeinschaft selbst festlegt.</p>
<p>Die physikalische Seite ändert sich dabei nicht. Der Strom fließt weiter über das Ortsnetz, der Smart Meter misst
viertelstundengenau, und der Netzbetreiber rechnet aus, welcher Anteil Ihres Überschusses innerhalb der Gemeinschaft
verbraucht wurde. Nur dieser Anteil wird zum EG-Preis abgerechnet. Was übrig bleibt, geht wie bisher an die OeMAG
oder den Einspeisevertrag.</p>
{A.net([
    ("☀", "PV-Erzeuger", "speist den Überschuss tagsüber ins Ortsnetz ein"),
    ("◎", "Smart Meter", "misst Viertelstundenwerte, der Netzbetreiber ordnet zu"),
    ("⌂", "Abnehmer in der Nähe", "Haushalte, Betriebe, Gemeinde beziehen mit reduziertem Netzentgelt"),
    ("€", "Rest wie gewohnt", "nicht zugeordnete Mengen laufen über OeMAG und Lieferant"),
], "Abrechnung über die Plattform",
   "Der EG-Strom wird zum vereinbarten Preis abgerechnet (bei EBZ über energyfamily). Physisch fließt der Strom "
   "wie bisher, neu ist nur die Zuordnung per Smart Meter.")}
<p>Wenn Sie das Grundprinzip genauer nachlesen wollen, erklärt unser {a('eg', 'Leitartikel zur Energiegemeinschaft')}
die fünf Modelle nach dem ElWG im Detail. Hier konzentrieren wir uns auf das, was in Kärnten speziell ist.</p>
"""),
        ("Warum sich das Thema gerade in Kärnten rechnet", "warum-kaernten", f"""
<p>Drei Faktoren kommen in Kärnten zusammen. Erstens die Sonne: Mit rund 1.050 bis 1.150 Kilowattstunden Ertrag pro
installiertem Kilowattpeak liegt Kärnten österreichweit an der Spitze, das Klagenfurter Becken und das Lavanttal noch
etwas darüber. Eine 10-kWp-Anlage liefert also gut 11.000 kWh im Jahr, von denen ein Einfamilienhaus ohne Speicher
nur etwa 30 Prozent selbst verbraucht.</p>
<p>Zweitens der Einspeisetarif: Der OeMAG-Marktpreis schwankt monatlich, im Juli 2026 lag er mit 6,146 Cent pro
Kilowattstunde an der gesetzlichen Untergrenze, im September bei 10,168 Cent, im Oktober 2026 bei 14,874 Cent (Stand November 2026, aktuelle
Werte in unserem {a('marktpreis', 'Marktpreis-Überblick')}). Planbar ist er damit nicht. Drittens die Netzstruktur: Kärnten ist kleinteilig besiedelt, viele
Ortschaften hängen an einem gemeinsamen Trafo. Das erleichtert lokale Energiegemeinschaften mit dem vollen
Netzentgelt-Abschlag.</p>
{A.box("7.000 kWh Überschuss, davon landen 60 Prozent in der Gemeinschaft, zu 10 Cent*: Gegenüber dem Juli-Wert "
       "der OeMAG (rund 6 Cent) sind das 168 Euro mehr im Jahr, gegenüber dem Oktober-Wert (14,874 Cent) rund 205 Euro "
       "weniger. Auf der Einspeiseseite ist der EG-Preis damit vor allem planbar. Dazu kommt die Bezugsseite, denn in den "
       "Abend- und Winterstunden sind Sie selbst Abnehmer und sparen in einer EEG im Nahbereich beim EG-Strom Netzentgelt und Abgaben.", label="Grob durchgerechnet:")}
<p>Unser {a('eg_rechner', 'Energiegemeinschaft-Rechner')} rechnet das mit Ihren Werten durch. Wo die Grenzen liegen,
etwa bei kleinen Überschüssen oder fehlendem Smart Meter, steht ehrlich im Artikel
{a('/energiegemeinschaft-nachteile/', 'Nachteile einer Energiegemeinschaft')}.</p>
<p><small>*Beispielkonditionen: EG-Einspeisepreis 10 Cent, EG-Bezugspreis 14 Cent je kWh. Jede Gemeinschaft legt
ihre Preise selbst fest, die tatsächlichen Konditionen nennen wir im Erstgespräch.</small></p>
"""),
        ("Netzgebiet, Nahbereich und Netzbetreiber in Kärnten", "nahbereich", f"""
<p>Ob eine Energiegemeinschaft in Ihrer Gemeinde lokal oder regional ist, entscheidet nicht die Postleitzahl, sondern
der Netzanschluss. In Kärnten betreibt die Kärnten Netz GmbH, eine Tochter der Kelag, den Großteil des Verteilnetzes,
im Stadtgebiet Klagenfurt ist die Energie Klagenfurt GmbH (Stadtwerke Klagenfurt) Netzbetreiber.
Wer an derselben Trafostation hängt, bildet den Lokalbereich, wer am selben Umspannwerk hängt, den Regionalbereich.
Der Unterschied ist bares Geld: Der Abschlag gilt auf den Arbeitspreis des Netznutzungs- und Netzverlustentgelts,
Stand 2026 laut E-Control.</p>
{A.table(
    ["Merkmal", "Lokale EEG", "Regionale EEG", "Bürgerenergiegemeinschaft (BEG)"],
    [
        ["Verbindung über", "selber Trafo (Niederspannung)", "selbes Umspannwerk (Mittelspannung)",
         "auch über mehrere Netzgebiete, netzübergreifend voraussichtlich ab April 2027"],
        ["Netznutzungsentgelt (Arbeit), Okt. bis Dez. 2026", "minus 57 %", "minus 28 %",
         "voll; Reduktion im Nahbereich voraussichtlich ab 1.1.2027, Höhe legt die E-Control fest"],
        ["Netzverlustentgelt", "minus 57 %", "minus 28 %", "voll"],
        ["Elektrizitätsabgabe (2026: 0,1 ct/kWh Haushalt, 0,82 ct Betrieb; ab 2027: 1,5 ct)", "entfällt", "entfällt", "bleibt"],
        ["Erneuerbaren-Förderbeitrag (2027 laut Bundesregierung für alle ausgesetzt)", "entfällt", "entfällt", "bleibt 2026"],
        ["Typisch in Kärnten", "Ortschaft, Siedlung, Gewerbegebiet", "Gemeinde, Tal, Bezirksteil",
         "Strom teilen über Netzgebiete und Bundesländer hinweg"],
    ],
    hl_cols=(1, 2),
)}
<p>Hängen alle Teilnehmer ausschließlich an den Netzebenen 4 und 5, beträgt der Abschlag in der EEG 64 Prozent. Die
Elektrizitätsabgabe ist für 2026 befristet gesenkt, im Vergleich dazu wiegt der Netzentgelt-Abschlag schwerer. Ab
2027 gilt wieder der Normalsatz von 1,5 Cent, während die Bundesregierung den Erneuerbaren-Förderbeitrag für alle
Stromkunden aussetzt: Der Abgabenvorteil der EEG beträgt 2027 damit rund 1,5 Cent je zugeordneter Kilowattstunde.
Die Netzabschläge ab 2027 legt die E-Control fest, laut E-Control-Entwurf 49 % lokal, 22 % bzw. 58 % regional
(Entwurf).</p>
<p>Die {a('/buergerenergiegemeinschaft/', 'Bürgerenergiegemeinschaft')} ist der Weg, wenn die Abnehmer nicht im Nahbereich sitzen, etwa die Tante in Wien.
Eine BEG darf sich über ganz Österreich erstrecken. In der Übergangsphase seit Oktober 2026 lassen sich neue
Zuordnungen laut Koordinationsstelle aber vorübergehend nur mit Zählpunkten beim selben Netzbetreiber umsetzen,
netzübergreifend (z. B. Kärnten und Wien) voraussichtlich ab April 2027. Das betrifft auch Kärnten selbst: Eine
Gemeinschaft aus Villach (Kärnten Netz) und dem Klagenfurter Stadtgebiet (Energie Klagenfurt) läuft über zwei
Netzbetreiber, neue Zuordnungen sind dort also voraussichtlich erst ab April 2027 möglich. EBZ bietet beide Varianten an,
die BEG ohne Netzentgelt-Abschlag.</p>
<p>Die gute Nachricht für alle anderen: Sie müssen die Netzebene nicht selbst herausfinden. Bei der Anmeldung prüft
der Netzbetreiber über die Zählpunktnummer, welchem Trafo und welchem Umspannwerk Ihr Anschluss zugeordnet ist, im
Netz der Kärnten Netz sehen Sie Lokal- und Regional-ID auch selbst im „Mein Portal“. EBZ übernimmt diese Abfrage im
Rahmen der Erstberatung. Was der Abschlag Position für Position bringt, steht im Artikel
{a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft und Netzkosten')}.</p>
"""),
        ("Energiegemeinschaften in Kärnten: Angebote und Tarife im Überblick", "anbieter", f"""
<p>In Kärnten gibt es mehrere Wege in eine Energiegemeinschaft: die Bürgerenergiegemeinschaft BEG Kärnten, die
Raiffeisen Energie-Genossenschaften (laut Raiffeisen 51 Genossenschaften in Kärnten), regionale EEGs einzelner
Gemeinden oder Stadtteile und Gemeinschaften, die EBZ mit Ihnen aufbaut. Die folgende Tabelle zeigt nur Werte, die
die Anbieter selbst veröffentlichen. Angaben zur Netz- und Abgabenersparnis stammen von den Anbietern und beziehen
sich auf die Abgaben 2026. Anbieter über Kärnten hinaus stellt der
{a('/energiegemeinschaft-vergleich/', 'Energiegemeinschaft-Vergleich')} gegenüber.</p>
{A.table(
    ["Anbieter / Gemeinschaft", "Modell", "Reichweite", "Bezugspreis je kWh", "Einspeisepreis je kWh",
     "Beitrag / Gebühren", "Quelle"],
    [
        ["BEG Kärnten (Energieverein Kärnten, Klagenfurt)", "BEG (Verein)",
         "ganz Österreich, laut Anbieter 13 Netzbetreiber in 9 Bundesländern",
         "12,00 ct inkl. 20 % USt (10,0 ct netto), Fixpreis", "8,0 ct",
         "keine Anmelde- oder Grundgebühr", _ext("https://www.beg-kaernten.at/", "beg-kaernten.at")],
        ["Raiffeisen Energie-Genossenschaften Kärnten", "EEG als Genossenschaft",
         "lokal/regional, Zuordnung nach Netzanschlusspunkt",
         "12,50 ct netto; nach Netz- und Abgabenersparnis für Private 9,07 ct (Netz Kärnten Netz) bzw. "
         "9,85 ct (Netz Energie Klagenfurt), Preisperiode 1.10. bis 31.12.2026",
         "9,50 ct (ohne Angabe netto/brutto)",
         "10 € Geschäftsanteil (bei Austritt zurück), einmalige Gebühr je Einspeisezählpunkt (Höhe nicht angegeben)",
         _ext("https://www.raiffeisen.at/ktn/de/privatkunden/energiegenossenschaft.html", "raiffeisen.at")],
        ["EEG 2R2 Völkermarkt (über BEG-Kärnten-Plattform)", "regionale EEG",
         "Völkermarkt, Klopeiner See, Griffen",
         "14,40 ct inkl. 20 % USt (12,0 ct netto)", "10,0 ct",
         "keine Anmelde- oder Grundgebühr", _ext("https://www.beg-kaernten.at/regionen/2r2.html", "beg-kaernten.at")],
        ["EEG KLU Mitte (über BEG-Kärnten-Plattform, im Aufbau)", "regionale EEG",
         "Klagenfurt Zentrum, St. Martin, Kreuzbergl (Netz Stadtwerke Klagenfurt)",
         "12,0 ct Endpreis (Kleinunternehmer, keine USt)",
         "10,0 ct für Private; Betriebe mit UID 8,33 ct netto",
         "keine Anmelde- oder Grundgebühr", _ext("https://www.beg-kaernten.at/regionen/klu-mitte.html", "beg-kaernten.at")],
        ["EEG Oisternig (Feistritz an der Gail)", "regionale EEG (rund 28 % Netzrabatt laut Preisblatt)",
         "Feistritz an der Gail und Umgebung",
         "12,5 ct netto, nach Netz- und Abgabenersparnis 9,07 ct netto (Preisblatt ab 1.4.2026)", "10 ct netto",
         "im Preisblatt nicht angegeben",
         _ext("https://feistritz-gail.gv.at/fileadmin/feistritz_an_der_gail/user_upload/Preisblattinfo_EEG_Oisternig-ab_01.04.2026.pdf",
              "Preisblatt (PDF)")],
        ["Kelag", "kein eigenes EG-Angebot für Privatkunden",
         "für Gemeinden: Projektierung, Betriebsführung, Software für Verwaltung und Abrechnung",
         "keine Angabe", "keine Angabe", "keine Angabe",
         _ext("https://www.kelag.at/gemeinden/uebersicht-energiegemeinschaft.htm", "kelag.at")],
    ],
)}
<p><small>Stand November 2026 (Anbieterseiten abgerufen am 20.11.2026, EEG Oisternig: Preisblatt gültig ab
1.4.2026). Preise ändern sich, bitte beim Anbieter prüfen. „Netto“ heißt ohne Umsatzsteuer; ob auf die
Einspeisevergütung Umsatzsteuer anfällt, hängt davon ab, ob Sie als Privatperson, Kleinunternehmer oder Betrieb
einspeisen.</small></p>
<h3>Wie die EG-Preise im Vergleich zur OeMAG abschneiden</h3>
<p>Für Einspeiser liegen die veröffentlichten EG-Preise in Kärnten zwischen 8,0 und 10,0 Cent je kWh. Der
OeMAG-Marktpreis lag im Juli 2026 bei 6,146 Cent, im September bei 10,168 Cent und im Oktober bei 14,874 Cent
(Stand November 2026). In einem Sommermonat wie Juli bringt die Gemeinschaft also mehr, im Oktober 2026 lag die OeMAG
über allen Tarifen in der Tabelle. Der Vorteil der Gemeinschaft ist der feste Preis für eine ganze Preisperiode. Für
Abnehmer ist die Rechnung klarer: In einer EEG im Netz der Kärnten Netz kostet EG-Strom nach Netz- und
Abgabenersparnis laut Raiffeisen und EEG Oisternig effektiv rund 9 Cent netto je kWh. Wer selbst Strom bezieht und
einspeist, profitiert auf beiden Seiten.</p>
<h3>Wo EBZ Energie hilft</h3>
<p>Die genannten Gemeinschaften rechnen Strom ab, die PV-Anlage selbst, den {a('batteriespeicher', 'Speicher')} und
die Optimierung des Eigenverbrauchs organisieren Sie dort separat. EBZ Energie kommt von der Anlage: Wir planen und
montieren PV-Anlage, Speicher, Wallbox und {a('ems', 'Energiemanagementsystem')} so, dass Ihr Überschuss dann anfällt,
wenn die Gemeinschaft ihn braucht. Danach binden wir Sie an eine Gemeinschaft an, abgerechnet über energyfamily,
eine österreichische Plattform mit rund 330 aktiven Gemeinschaften und rund 15.000 Nutzern. Gibt es in Ihrem Trafo-
oder Umspannwerksbereich keine passende Gemeinschaft, gründen wir mit Ihnen und Ihren Nachbarn eine neue im
Nahbereich; für Gemeinden und Betriebe beschreibt das die Seite
{a('eg_gewerbe', 'Energiegemeinschaft für Gewerbe und Gemeinden')}. Einer der oben genannten Gemeinschaften können Sie
trotzdem beitreten: Seit dem ElWG darf ein Zählpunkt an bis zu fünf Modellen gleichzeitig teilnehmen. Alle Details zur
Leistung für Haushalte: {a('eg_privat', 'Energiegemeinschaft für Private')}, ausgeführte Anlagen sehen Sie unter
{a('referenzen', 'unseren Referenzen')}.</p>
"""),
        ("Energiegemeinschaften in den Kärntner Regionen", "regionen", f"""
<p>Viele Kärntner suchen nicht nach „Kärnten“, sondern nach ihrem Tal oder Bezirk. Hier steht je Region, welche
Gemeinschaften öffentlich belegt sind (Firmenbuch, Gemeinde- oder Anbieterseiten), und wo EBZ vor Ort ist. Ob Sie
einer bestimmten Gemeinschaft beitreten können, hängt immer von Ihrem Netzanschluss ab. Gemeinschaften in Ihrer Nähe finden Sie
auch über die Plattform Strom verbindet unter
{_ext("https://stromverbindet.energiegemeinschaften.gv.at/", "stromverbindet.energiegemeinschaften.gv.at")}.</p>
<h3>Energiegemeinschaft Rosental</h3>
<p>Im Kärntner Rosental sind seit April 2024 die Energiegenossenschaft Rosental eG und die Energiegenossenschaft
Ferlach eG (beide mit Sitz in Feistritz im Rosental) sowie die Energiegenossenschaft Wernberg-Rosental eG im
Firmenbuch eingetragen. Nicht verwechseln: Die „EEG Rosental“ mit 108 Mitgliedern und 143 Zählpunkten (MeinBezirk,
Juli 2026) liegt im steirischen Rosental an der Kainach, Bezirk Voitsberg; dazu passt unser
{a('/energiegemeinschaft-steiermark/', 'Ratgeber Energiegemeinschaft Steiermark')} und die Seite
{a('pv_voitsberg', 'Photovoltaik Voitsberg')}. Für das Kärntner Rosental passt unsere Seite
{a('pv_klagenfurt', 'Photovoltaik Klagenfurt')}.</p>
<h3>Energiegemeinschaft Lavanttal und Wolfsberg</h3>
<p>Im Lavanttal sind die Energiegenossenschaft Wolfsberg eG und die Energiegenossenschaft St. Andrä-St. Paul eG
(Sitz jeweils St. Andrä) seit April 2024 im Firmenbuch eingetragen. Mit rund 1.100 kWh je kWp zählt das Lavanttal zu
den ertragsstärksten Lagen Kärntens. Planung und Montage vor Ort: {a('pv_wolfsberg', 'Photovoltaik Wolfsberg')}.</p>
<h3>Energiegemeinschaft Villach</h3>
<p>In Villach ist seit April 2025 die Energiegenossenschaft Villach-Dobratsch eG im Firmenbuch eingetragen. Im
benachbarten Gailtal veröffentlicht die EEG Oisternig in Feistritz an der Gail ihr Preisblatt (10 ct netto
Einspeisung, siehe Tabelle). EBZ hat seinen Sitz in Villach: {a('pv_villach', 'Photovoltaik Villach')} und
{a('/energiegemeinschaft-villach-klagenfurt/', 'Energiegemeinschaft Villach und Klagenfurt')}.</p>
<h3>Energiegemeinschaft Klagenfurt</h3>
<p>Im Netz der Stadtwerke Klagenfurt listet BEG Kärnten fünf regionale EEGs: KLU Nord, Ost, Süd, West und Mitte, die
EEG KLU Mitte (Zentrum, St. Martin, Kreuzbergl) ist laut Anbieter im Aufbau. Rund um den Wörthersee kommen die EEGs
24R1 Pörtschach, 24R1 Augsdorf und 17R1 Pritschitz (Moosburg, Reifnitz, Keutschach) im Netz der Kärnten Netz dazu.
Mehr dazu unter {a('pv_klagenfurt', 'Photovoltaik Klagenfurt')} und im Artikel
{a('/energiegemeinschaft-villach-klagenfurt/', 'Energiegemeinschaft Villach und Klagenfurt')}.</p>
<h3>Energiegemeinschaft Spittal und Mölltal</h3>
<p>Im Bezirk Spittal ist die Energie4Mölltal eGen mit Sitz in Außerfragant (Gemeinde Flattach) seit Februar 2022 im
Firmenbuch eingetragen. Für weitere Gemeinden in Oberkärnten lohnt die Suche über die Koordinationsstelle oder eine
eigene Gründung im Nahbereich. EBZ vor Ort: {a('pv_spittal', 'Photovoltaik Spittal')}.</p>
<h3>Energiegemeinschaft Feldkirchen</h3>
<p>Laut Wirtschaftskammer Kärnten (Mai 2026) bestehen sechs der von Raiffeisen initiierten Energiegemeinschaften im
Raum Feldkirchen. Planung und Montage: {a('pv_feldkirchen', 'Photovoltaik Feldkirchen')}.</p>
<h3>Energiegemeinschaft St. Veit</h3>
<p>Im Bezirk St. Veit listet BEG Kärnten die EEG 7R1 Straßburg (Gurk, Weitensfeld, Straßburg, mit Wasserkraft und
PV) und die EEG 18R1 Mölbling (Mölbling, Guttaring, Friesach, Metnitz). EBZ vor Ort:
{a('pv_st_veit', 'Photovoltaik St. Veit')}.</p>
<h3>Energiegemeinschaft Völkermarkt</h3>
<p>Im Bezirk Völkermarkt wurden laut Raiffeisen im Jänner 2024 die ersten vier Kärntner Energie-Genossenschaften
gegründet. Dazu kommt die EEG 2R2 Völkermarkt (Völkermarkt, Klopeiner See, Griffen) mit veröffentlichtem Tarif, siehe
Tabelle. EBZ vor Ort: {a('pv_voelkermarkt', 'Photovoltaik Völkermarkt')}.</p>
<h3>Energiegemeinschaft Hermagor</h3>
<p>Die Stadtgemeinde Hermagor-Pressegger See hat mit sechs heimischen Betrieben die Erneuerbare Energiegemeinschaft
Wulfenia gegründet, die laut Präsentation der Gemeinde weitere Mitglieder aufnehmen will, insbesondere Haushalte und Betriebe. EBZ vor
Ort: {a('pv_hermagor', 'Photovoltaik Hermagor')}.</p>
"""),
        ("So kommen Sie in Kärnten in eine Energiegemeinschaft", "ablauf", f"""
<p>Es gibt zwei Wege: einer bestehenden Gemeinschaft beitreten oder eine neue gründen. Für die meisten Privathaushalte
ist der {a('/energiegemeinschaft-beitreten/', 'Beitritt')} der schnellere Weg, weil die Rechtsform, der Vertrag mit
dem Netzbetreiber und die Abrechnung schon stehen. Was das für Haushalte konkret bedeutet, fasst der Artikel
{a('/energiegemeinschaft-privat/', 'Energiegemeinschaft für Privatpersonen')} zusammen. Die Gründung lohnt sich vor
allem für Gemeinden, Betriebe oder Nachbarschaften mit mehreren Erzeugern, Details dazu im Artikel
{a('/energiegemeinschaft-gruenden/', 'Energiegemeinschaft gründen')}.</p>
{A.steps([
    ("Erstgespräch und Eignungscheck",
     "Wir klären Ihre PV-Leistung, den Verbrauch, ob ein Smart Meter mit Viertelstundenwerten aktiv ist und in "
     "welchem Netzbereich Ihr Anschluss liegt."),
    ("Passende Gemeinschaft wählen",
     "Je nach Standort nehmen wir Sie in eine bestehende Energiegemeinschaft im Nahbereich auf oder bündeln mehrere "
     "Interessenten zu einer neuen."),
    ("Zustimmung beim Netzbetreiber",
     "Im „Mein Portal“ der Kärnten Netz bestätigen Sie die Teilnahme und schließen die Zusatzvereinbarung zum "
     "Netzzugangsvertrag ab, im Stadtgebiet Klagenfurt läuft das über die Energie Klagenfurt. Das dauert wenige "
     "Minuten, wir leiten Sie an."),
    ("Aufnahme und Start",
     "Die Gemeinschaft meldet Ihren Zählpunkt über die Marktprozesse (EDA) an. Ab dem Folgemonat wird Ihr Strom zugeordnet."),
    ("Monatliche Abrechnung",
     "Über die energyfamily-Plattform sehen Sie, wie viel Strom Sie in die Gemeinschaft geliefert oder von ihr "
     "bezogen haben. Die Abrechnung läuft automatisch."),
])}
{A.cta("Energiegemeinschaft in Kärnten: Eignung in 10 Minuten prüfen",
       "Nennen Sie uns Postleitzahl, PV-Leistung und Jahresverbrauch. Wir sagen Ihnen, welche Gemeinschaft für Sie "
       "infrage kommt und was sie bringt.",
       secondary=("eg_rechner", "Ersparnis berechnen"))}
"""),
        ("Was sich seit Oktober 2026 durch das ElWG ändert", "elwg", f"""
<p>Seit 1. Oktober 2026 gilt das Elektrizitätswirtschaftsgesetz (ElWG). Es kennt fünf Bürgerenergie-Modelle:
{a('/gemeinschaftliche-erzeugungsanlage/', 'gemeinschaftliche Erzeugungsanlage (GEA)')}, Erneuerbare-Energie-Gemeinschaft
(EEG), Bürgerenergiegemeinschaft (BEG), {a('/peer-to-peer-strom/', 'Peer-to-Peer-Vertrag (P2P)')} und
Eigenversorgungsanlage (EVA). Bestehende Gemeinschaften wurden ins neue System
übergeführt, für deren Mitglieder besteht laut Kärnten Netz kein Handlungsbedarf. Neu ist die Mehrfachteilnahme: Mit
jedem Zählpunkt können Sie an bis zu fünf Modellen gleichzeitig teilnehmen, etwa an einer regionalen EEG und an einer
BEG.</p>
<p>Für die Übergangsphase gilt: Von Oktober bis Dezember 2026 bekommen nur Mitglieder lokaler und regionaler EEGs den
reduzierten Netzarbeitspreis (minus 57 Prozent lokal, minus 28 Prozent regional, minus 64 Prozent bei ausschließlich
Netzebene 4 und 5). Für BEG, Peer-to-Peer und Eigenversorgung im Nahbereich soll die Reduktion nach heutigem Stand ab
1. Jänner 2027 mit der novellierten Systemnutzungsentgelte-Verordnung kommen, die Höhe legt die E-Control fest. Die
Befreiung von Elektrizitätsabgabe und Erneuerbaren-Förderbeitrag gilt derzeit nur für die EEG. Neue Zuordnungen lassen
sich vorübergehend nur mit Zählpunkten beim selben Netzbetreiber umsetzen, netzübergreifend voraussichtlich ab April
2027.</p>
{A.box("Die EEG bleibt bis auf Weiteres das wirtschaftlich stärkste Modell, weil nur sie Netzentgelt-Abschlag und "
       "Abgabenbefreiung schon heute kombiniert. Peer-to-Peer und BEG werden Ergänzungen, sobald die neue Verordnung "
       "gilt und netzübergreifende Zuordnungen möglich sind. Die Details zu allen fünf Modellen stehen im "
       f"{a('/energiegemeinschaft/#elwg', 'Leitartikel im Abschnitt ElWG')}.", label="Für Kärnten heißt das:")}
"""),
        ("Förderung in Kärnten: Gibt es Geld für die Energiegemeinschaft?", "foerderung", f"""
<p>Für die Teilnahme selbst gibt es in Kärnten keine eigene Prämie. Gefördert wird die PV-Anlage, und zwar über die
Kärntner Landesförderung mit der 3.000-Euro-Pauschale (nur mit Speicher, 2. Landes-Call bis 31. Dezember 2026),
die wir im
Artikel {a('foerderung_kaernten', 'Photovoltaik-Förderung Kärnten')} aufgeschlüsselt haben. Der EAG-Investitionszuschuss des Bundes ist derzeit nicht beantragbar: Der letzte Call
lief vom 8. bis 22. Oktober 2026, ab 2027 ist laut BMWET eine Systemförderung für Speicher mit intelligenter
Steuerung geplant (nicht beschlossen). Wer zusätzlich ein
Energiemanagementsystem einbaut, kann die {a('/ems-foerderung/', 'EMS-Förderung des Klimafonds')} nutzen: Die
Teilnahme an einer Energiegemeinschaft zählt dort als eine der zulässigen Betriebsoptionen. Wer die Anlage über EBZ
errichten lässt, bekommt Förderabwicklung und EG-Anbindung aus einer Hand.</p>
"""),
        ("Fazit: Energiegemeinschaft Kärnten", "fazit", f"""
<p>Kärnten hat viel Sonne, einen stark schwankenden OeMAG-Marktpreis und ein kleinteiliges Netz. Das ist eine gute
Kombination für lokale und regionale Energiegemeinschaften. Die Auswahl ist groß: von der BEG Kärnten über die
Raiffeisen Energie-Genossenschaften bis zu regionalen EEGs mit Einspeisepreisen von 8,0 bis 10,0 Cent. Der Einstieg
dauert wenige Wochen, die Abrechnung läuft automatisch, und das Risiko ist gering, weil Sie austreten können und Ihr
Lieferant bleibt. Für Villach, Klagenfurt und das Umland haben
wir die Details im Artikel {a('/energiegemeinschaft-villach-klagenfurt/', 'Energiegemeinschaft Villach und Klagenfurt')}
zusammengefasst.</p>
{A.cta("Jetzt Ersparnis für Ihren Standort berechnen",
       "Unser Rechner vergleicht OeMAG-Einspeisung mit der Energiegemeinschaft, auf Basis Ihrer kWp, Ihres "
       "Verbrauchs und Ihrer Netzebene.",
       primary=("kontakt", "Beratung anfragen"), secondary=("eg_rechner", "Zum Energiegemeinschaft-Rechner"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Energiegemeinschaft in Kärnten: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und Wallboxen in "
                 "Kärnten und der Steiermark, mit zertifizierten Fachkräften. Dazu kommt "
                 "die Energiegemeinschaft: Wir nehmen Sie in eine bestehende Gemeinschaft auf oder bauen mit Ihnen eine "
                 "eigene auf, abgerechnet über die Plattform unseres Partners energyfamily. Einzugsgebiet: Villach, "
                 "Klagenfurt, Spittal, Feldkirchen, St. Veit, Völkermarkt, Wolfsberg, Hermagor und Umgebung."),
        "grid": [
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EG-Anbindung vom selben Team."),
            ("Regional verankert", "Sitz in Villach, Montage in ganz Kärnten und der Steiermark."),
            ("Abrechnung inklusive", "Zählpunktfreigabe, Aufnahme und monatliche Abrechnung über energyfamily."),
            ("Kostenlose Erstberatung", "Wir prüfen Netzebene, Eignung und Ihr Einsparpotenzial."),
        ],
    },

    "faq": [
        ("Welche Energiegemeinschaften gibt es in Kärnten?",
         "Unter anderem die Bürgerenergiegemeinschaft BEG Kärnten (österreichweit offen), die Raiffeisen "
         "Energie-Genossenschaften (laut Raiffeisen 51 in Kärnten) und regionale EEGs wie EEG 2R2 Völkermarkt, die "
         "Klagenfurter EEGs KLU Nord bis Mitte oder die EEG Wulfenia in Hermagor. Die veröffentlichten Tarife liegen "
         "bei 10,0 bis 12,5 Cent netto für den Bezug und 8,0 bis 10,0 Cent für die Einspeisung (Stand November 2026)."),
        ("Gibt es eine Energiegemeinschaft der Kelag?",
         "Laut Kelag-Website betreibt die Kelag keine eigene Energiegemeinschaft, der Privatkunden beitreten können; "
         "sie verweist an die Betreiber der jeweiligen Modelle. Für Gemeinden bietet die Kelag Projektierung, "
         "Betriebsführung und Software für Verwaltung und Abrechnung an. Die Kelag-Tochter Kärnten Netz ist als "
         "Netzbetreiber für Zählpunktanmeldung und Energiedaten zuständig."),
        ("Wer darf in Kärnten an einer Energiegemeinschaft teilnehmen?",
         "Privathaushalte, Gemeinden, Vereine und kleine sowie mittlere Unternehmen. Eine eigene PV-Anlage ist nicht "
         "Voraussetzung, reine Abnehmer sind ausdrücklich erwünscht. Voraussetzung für die EEG ist ein Zählpunkt im "
         "selben Netzbereich und ein Smart Meter mit Viertelstundenwerten."),
        ("Muss ich meinen Stromlieferanten wechseln?",
         "Nein. Der Lieferantenvertrag bleibt bestehen. Die Energiegemeinschaft deckt nur den Anteil, der zeitgleich "
         "in der Gemeinschaft erzeugt wird. Den Rest liefert weiterhin Ihr bisheriger Anbieter."),
        ("Wie viel Netzentgelt spare ich in Kärnten?",
         "Bei einer lokalen EEG (selber Trafo) 57 Prozent des Arbeitspreises von Netznutzungs- und Netzverlustentgelt, "
         "bei einer regionalen EEG (selbes Umspannwerk) 28 Prozent. Dazu entfallen in der EEG Elektrizitätsabgabe "
         "(2026: 0,1 Cent je kWh für Haushalte, ab 2027 wieder 1,5 Cent) und Erneuerbaren-Förderbeitrag (2027 laut "
         "Bundesregierung für alle ausgesetzt) auf den EG-Strom. Für BEG und "
         "Peer-to-Peer im Nahbereich soll eine Reduktion voraussichtlich ab 1. Jänner 2027 gelten."),
        ("Kann ich Strom auch mit Verwandten außerhalb Kärntens teilen?",
         "Ja, über eine Bürgerenergiegemeinschaft, die sich über ganz Österreich erstrecken darf. In der "
         "Übergangsphase seit Oktober 2026 lassen sich neue Zuordnungen laut Koordinationsstelle vorübergehend nur "
         "mit Zählpunkten beim selben Netzbetreiber umsetzen, netzübergreifend (z. B. Kärnten und Wien) "
         "voraussichtlich ab April 2027. Der Netzentgelt-Abschlag gilt dabei nicht, weil er an den Nahbereich "
         "gebunden ist. EBZ bietet beide Varianten an und rechnet über energyfamily ab."),
        ("Brauche ich einen Speicher für die Energiegemeinschaft?",
         "Nein, aber er hilft. Ein Speicher erhöht den Eigenverbrauch und verschiebt Überschuss in die Abendstunden, "
         "in denen Abnehmer in der Gemeinschaft mehr brauchen. Die Kombination aus Speicher, EMS und "
         "Energiegemeinschaft holt am meisten heraus."),
        ("Kann ich die Energiegemeinschaft wieder verlassen?",
         "Ja. Die Kündigungsfristen regelt die jeweilige Gemeinschaft, üblich sind ein bis drei Monate zum Monatsende. "
         "Der Zählpunkt wird dann beim Netzbetreiber abgemeldet, Ihr Lieferantenvertrag läuft unverändert weiter."),
        ("Was kostet die Teilnahme?",
         "Das legt jede Gemeinschaft selbst fest. BEG Kärnten und die regionalen EEGs auf deren Plattform verlangen "
         "laut eigener Angabe keine Anmelde- oder Grundgebühr, bei den Raiffeisen Energie-Genossenschaften zeichnen "
         "Sie einen Geschäftsanteil von 10 Euro. Bei EBZ erfahren Sie die genauen Konditionen im Erstgespräch, "
         "bevor Sie sich entscheiden."),
        ("Wie lange dauert der Einstieg in Kärnten?",
         "Vom Erstgespräch bis zur ersten zugeordneten Kilowattstunde vergehen in der Regel vier bis acht Wochen. "
         "Der größte Zeitfaktor ist die Zählpunktanmeldung beim Netzbetreiber (Kärnten Netz oder im Stadtgebiet "
         "Klagenfurt die Energie Klagenfurt), die zum Monatsersten wirksam wird."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und errichtet Photovoltaik-, "
                    "Speicher- und Wärmepumpensysteme in Kärnten und der Steiermark und begleitet Kunden beim Einstieg "
                    "in Energiegemeinschaften. Inhalte werden regelmäßig anhand der Vorgaben von E-Control, OeMAG und "
                    "energiegemeinschaften.gv.at aktualisiert. Keine Rechts- oder Steuerberatung."),
    "sources": [
        ("E-Control: Energiegemeinschaften", "https://www.e-control.at/energiegemeinschaften"),
        ("Koordinationsstelle: Neue rechtliche Grundlagen (ElWG)",
         "https://energiegemeinschaften.gv.at/rechtliche-grundlagen-elwg/"),
        ("Koordinationsstelle: FAQs zum ElWG", "https://energiegemeinschaften.gv.at/faqs-zum-elwg/"),
        ("Koordinationsstelle: Bürgerenergiegemeinschaft", "https://energiegemeinschaften.gv.at/buergerenergiegemeinschaft/"),
        ("Koordinationsstelle: Peer-to-Peer", "https://energiegemeinschaften.gv.at/peer-to-peer/"),
        ("Koordinationsstelle: Mehrfachteilnahme", "https://energiegemeinschaften.gv.at/mehrfachteilnahme/"),
        ("Strom verbindet: Energiegemeinschaften in der Nähe finden", "https://stromverbindet.energiegemeinschaften.gv.at/"),
        ("OeMAG: Aktueller Marktpreis", "https://www.oem-ag.at/marktpreis"),
        ("Parlament: Senkung der Elektrizitätsabgabe 2026",
         "https://www.parlament.gv.at/aktuelles/news/Nationalrat-beschliesst-Senkung-der-Elektrizitaetsabgabe"),
        ("BMF: Aussetzung von Ökostrompauschale und Förderbeitrag 2027",
         "https://www.bmf.gv.at/presse/pressemeldungen/2026/november-2026/oekostrompauschale.html"),
        ("Kärnten Netz: Bürgerenergiemodelle", "https://www.kaerntennetz.at/buergerenergiemodelle.htm"),
        ("Kelag: Bürgerenergiemodelle (Privatkunden)", "https://www.kelag.at/privatkunden/buergerenergiemodelle.htm"),
        ("Kelag: Energiegemeinschaften für Gemeinden", "https://www.kelag.at/gemeinden/uebersicht-energiegemeinschaft.htm"),
        ("BEG Kärnten: Tarife", "https://www.beg-kaernten.at/"),
        ("BEG Kärnten: Regionale EEGs", "https://www.beg-kaernten.at/regionen/"),
        ("BEG Kärnten: EEG 2R2 Völkermarkt", "https://www.beg-kaernten.at/regionen/2r2.html"),
        ("BEG Kärnten: EEG KLU Mitte", "https://www.beg-kaernten.at/regionen/klu-mitte.html"),
        ("Raiffeisen Kärnten: Energie-Genossenschaften", "https://www.raiffeisen.at/ktn/de/privatkunden/energiegenossenschaft.html"),
        ("Gemeinde Feistritz an der Gail: Preisblatt EEG Oisternig ab 1.4.2026",
         "https://feistritz-gail.gv.at/fileadmin/feistritz_an_der_gail/user_upload/Preisblattinfo_EEG_Oisternig-ab_01.04.2026.pdf"),
        ("Stadtgemeinde Hermagor: EEG Wulfenia", "https://hermagor.at/fileadmin/user_upload/direct-uploads/EEG-050923.pdf"),
        ("WKO Kärnten: Energiegemeinschaften als Wettbewerbsvorteil (Feldkirchen)",
         "https://www.wko.at/ktn/bezirksstellen/early-bird-energiegemeinschaften-als-wettbewerbsvorteil"),
        ("Firmenbuch (EVI): Energiegenossenschaft Rosental eG", "https://www.evi.gv.at/b/fb/bl2-kxl"),
        ("Firmenbuch (EVI): Energiegenossenschaft Wolfsberg eG", "https://www.evi.gv.at/b/fb/bl2-kxn"),
        ("Firmenbuch (EVI): Energiegenossenschaft Villach-Dobratsch eG", "https://www.evi.gv.at/f/651928v"),
        ("Firmenbuch (EVI): Energie4Mölltal eGen", "https://www.evi.gv.at/f/573300p"),
        ("MeinBezirk: EEG Rosental (Steiermark)",
         "https://www.meinbezirk.at/voitsberg/c-wirtschaft/regionalstrom-fuer-zwei-millionen-e-auto-kilometer_a8791305"),
    ],
    "related": [
        ("/energiegemeinschaft-villach-klagenfurt/", "Energiegemeinschaft in Villach und Klagenfurt"),
        ("/energiegemeinschaft-beitreten/", "Energiegemeinschaft beitreten: Ablauf"),
        ("/energiegemeinschaft-netzkosten/", "Netzkosten sparen mit der EG"),
        ("eg_privat", "Energiegemeinschaft für Private mit Rechner"),
    ],
    "cta": {
        "h3": "Eignung für Ihren Zählpunkt prüfen",
        "text": ("Wir fragen den Nahbereich beim Netzbetreiber ab (Kärnten Netz oder Energie Klagenfurt) und sagen "
                 "Ihnen, welche Gemeinschaft für Sie passt."),
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihr Solarstrom bleibt in Kärnten",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das PV-Anlage, Speicher und "
                   "Energiegemeinschaft aus einer Hand liefert."),
}
