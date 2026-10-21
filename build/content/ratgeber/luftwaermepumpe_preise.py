"""Ratgeber: Luftwärmepumpe Preise 2026 (Luft-Wasser, kurz Luft-Luft).

Migriert vom WordPress-Artikel ebz-photovoltaik.at/luftwaermepumpe-preise/
(veröffentlicht 2026-09-05, geändert 2026-09-30). Struktur, Preise und Betriebskosten aus der Quelle.
Abgrenzung: nur Luft-Wasser- und kurz Luft-Luft-Wärmepumpe (Preise, Installation, Betrieb, JAZ, Schall,
Aufstellung). Gesamtvergleich aller Wärmepumpenarten: /kosten-einer-waermepumpe/.
Korrigiert nach build/seo/_fakten_2026-10.md: Steiermark "bis zu 35 %" entfernt (keine Anträge für neue
Wärmepumpen), Kärnten 3.000 € Pauschale, Bund nicht als verfügbar, Öko-Sonderausgabenpauschale nur mit
ausbezahlter Bundesförderung, "eigene zertifizierte Fachkräfte" entfernt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "luftwaermepumpe-preise",
    "path": "/luftwaermepumpe-preise/",
    "title": "Luftwärmepumpe Preise 2026: Kosten und Betrieb | EBZ Energie",
    "description": ("Luftwärmepumpe 2026: 14.000 bis 22.000 € im Neubau, 16.000 bis 28.000 € in der Sanierung, "
                    "Strom 700 bis 1.100 € im Jahr. Preise, JAZ, Schall und Förderstand."),
    "eyebrow": "Wärmepumpe · Luftwärmepumpe",
    "crumb_label": "Luftwärmepumpe Preise",
    "h1": "Luftwärmepumpe Preise 2026: Was eine Luft-Wasser-Wärmepumpe ab 14.000 Euro wirklich kostet",
    "lead": ("Eine Luft-Wasser-Wärmepumpe kostet im Einfamilienhaus inklusive Montage 14.000 bis 22.000 Euro im "
             "Neubau und 16.000 bis 28.000 Euro in der Sanierung, im Betrieb rund 700 bis 1.100 Euro Strom pro "
             "Jahr. Hier finden Sie alle Preispositionen, die Rechnung zur Jahresarbeitszahl, die Regeln für "
             "Aufstellung und Schall und den Förderstand Oktober 2026."),
    "chips": [
        "Neubau: <b>14.000 bis 22.000 €</b>*",
        "Sanierung: <b>16.000 bis 28.000 €</b>*",
        "Betrieb: <b>700 bis 1.100 €/Jahr</b>*",
        "Mit PV: <b>200 bis 500 €/Jahr</b>*",
    ],
    "date_published": "2026-09-05",
    "date_modified": "2026-10-21",
    "hero_img": "waermepumpe",
    "hero_alt": "Außeneinheit einer Luft-Wasser-Wärmepumpe auf einem Betonsockel vor einer Holzwand im Garten",

    "tldr": [
        "Eine Luft-Wasser-Wärmepumpe kostet 2026 inklusive Montage meist 14.000 bis 22.000 Euro im Neubau und "
        "16.000 bis 28.000 Euro in der Sanierung, jeweils vor Förderung. Das Gerät allein liegt bei 8.000 bis "
        "18.000 Euro, eine Luft-Luft-Wärmepumpe startet bei rund 5.000 Euro.",
        "Bei 12.000 Kilowattstunden Wärmebedarf und einer Jahresarbeitszahl von 3,5 bis 4 braucht sie rund "
        "3.000 bis 3.500 Kilowattstunden Strom, das sind etwa 700 bis 1.100 Euro pro Jahr. Mit Photovoltaik "
        "sinkt der Wert auf grob 200 bis 500 Euro.",
        "Förderung Stand Oktober 2026: Die Bundesförderung 2026 (Kesseltausch bis 7.500 Euro) ist ausgeschöpft, "
        "neue Registrierungen sind derzeit nicht möglich. Kärnten zahlt 3.000 Euro Pauschale, die Steiermark "
        "nimmt für neue Wärmepumpen derzeit keine Anträge an.",
        "Für den Altbau entscheidet die Vorlauftemperatur: Reichen 55 Grad Celsius, arbeitet eine "
        "Luftwärmepumpe wirtschaftlich.",
        "Beim Aufstellort zählen Abstand zu Schlafzimmerfenstern (auch beim Nachbarn), keine Ecken oder Nischen "
        "und ein leiser Nachtmodus.",
    ],
    "kpis": [
        ("14.000 €", "Einstieg Neubau inkl. Montage*"),
        ("16.000 bis 28.000 €", "typisch in der Sanierung*"),
        ("3,5 bis 4", "Jahresarbeitszahl moderner Geräte"),
        ("700 bis 1.100 €", "Stromkosten pro Jahr ohne PV*"),
    ],

    "sections": [
        ("Was kostet eine Luftwärmepumpe 2026?", "preise", f"""
<p><b>Eine Luft-Wasser-Wärmepumpe kostet in Österreich 2026 für ein Einfamilienhaus inklusive Gerät,
Montage, Pufferspeicher und Inbetriebnahme meist 14.000 bis 22.000 Euro im Neubau und 16.000 bis 28.000
Euro in der Sanierung, jeweils vor Förderung*.</b> Sie ist die günstigste Wärmepumpe in der Anschaffung,
weil sie ihre Energie aus der Außenluft holt und weder Tiefenbohrung noch Erdkollektor braucht. Wie sie im
Vergleich zu Erdwärme und Grundwasser abschneidet, zeigt der Gesamtvergleich
{a('/kosten-einer-waermepumpe/', 'Kosten einer Wärmepumpe')}.</p>
{A.table(
    ["Variante", "Gesamtkosten inkl. Montage*", "Typischer Einsatz"],
    [
        ["Luft-Wasser-Wärmepumpe, Neubau", "14.000 bis 22.000 €", "Fußbodenheizung, niedrige Vorlauftemperatur"],
        ["Luft-Wasser-Wärmepumpe, Sanierung", "16.000 bis 28.000 €", "Heizungstausch, Heizkörper, mehr Hydraulik"],
        ["Luft-Luft-Wärmepumpe", "5.000 bis 15.000 €", "einzelne Räume oder Wohnungen, kein Wasser-Heizsystem"],
    ],
    hl_cols=(1,),
)}
<p>In der Sanierung kosten Hydraulik, Speicher und eventuell neue Heizkörper mehr als im Neubau. Ob Sie am
unteren oder oberen Ende landen, entscheiden die Heizlast Ihres Hauses, die vorhandenen Heizflächen und der
Aufwand für Hydraulik und Elektrik. Der Gerätepreis allein sagt wenig.</p>
<h3>Kurz zur Luft-Luft-Wärmepumpe</h3>
<p>Eine Luft-Luft-Wärmepumpe erwärmt direkt die Raumluft und versorgt kein Wasser-Heizsystem. Sie startet
bei rund 5.000 Euro und eignet sich für einzelne Räume, kleine Wohnungen oder als Ergänzung. Warmwasser
bereitet sie nicht, dafür braucht es ein separates System. Für ein ganzes Einfamilienhaus mit Heizkörpern
oder Fußbodenheizung ist die Luft-Wasser-Wärmepumpe die passende Bauart, um die es in diesem Ratgeber
geht.</p>
<p><small>*Richtwerte 2026 für ein Einfamilienhaus inklusive Montage und USt, vor Förderung. Der
tatsächliche Preis hängt von Heizlast, Heizsystem und Aufwand vor Ort ab.</small></p>
"""),
        ("Woraus sich der Preis zusammensetzt", "positionen", f"""
<p>Ein Angebot für eine Luft-Wasser-Wärmepumpe besteht aus mehreren Positionen. Die Spannen zeigen, wo
die Unterschiede zwischen zwei Angeboten meist herkommen:</p>
{A.table(
    ["Position", "Richtwert*", "Worauf es ankommt"],
    [
        ["Außen- und Inneneinheit (Luft-Wasser)", "8.000 bis 18.000 €", "Leistung nach Heizlast, Kältemittel, Schallwerte, Effizienz"],
        ["Montage und Hydraulik", "3.000 bis 6.000 €", "Rohrführung, Pufferspeicher, Anbindung an das Heizsystem"],
        ["Warmwasserspeicher", "oft im Paket, sonst 1.500 bis 3.000 €", "Speichergröße nach Personen im Haushalt"],
        ["Elektroinstallation", "500 bis 1.500 €", "eigener Stromkreis, Zählerplatz, Anmeldung beim Netzbetreiber"],
        ["Fundament und Aufstellung", "300 bis 1.000 €", "Sockel oder Wandkonsole, Kondensatablauf, Schallentkopplung"],
        ["Demontage der Altanlage", "500 bis 2.000 €", "Öltank entsorgen, Kessel ausbauen, Kamin"],
        ["Heizflächen (nur Sanierung)", "0 bis 5.000 €", "einzelne größere Heizkörper statt kompletter Fußbodenheizung"],
    ],
    hl_cols=(1,),
)}
<h3>Gerätepreis nach Leistung: Heizlast statt Quadratmeter</h3>
<p>Der größte Einzelposten ist das Gerät, und sein Preis steigt mit der Heizleistung. Welche Leistung Ihr
Haus braucht, ergibt sich aus der <b>Heizlastberechnung</b>, nicht aus einer Schätzung nach Wohnfläche.
Eine zu große Wärmepumpe taktet häufig und kostet unnötig mehr, eine zu kleine schafft kalte Tage nicht
und lässt den Heizstab einspringen. Beides verschlechtert die Jahresarbeitszahl.</p>
{A.box("Ein scheinbar günstiges Gerät wird teuer, wenn Pufferspeicher, Elektrik oder die Entsorgung der "
       "Ölheizung als Nachtrag kommen. Vergleichen Sie Angebote immer nach Gesamtpreis mit allen Positionen.",
       label="Beim Angebotsvergleich:")}
<p><small>*Richtwerte 2026 inklusive USt, vor Förderung.</small></p>
"""),
        ("Betriebskosten und Jahresarbeitszahl", "betrieb", f"""
<p>Eine Luftwärmepumpe macht aus einer Kilowattstunde Strom je nach Außentemperatur drei bis fünf
Kilowattstunden Wärme. Über das Jahr gemittelt erreichen moderne Geräte in gut geplanten Anlagen eine
<b>Jahresarbeitszahl (JAZ) von 3,5 bis 4</b>. Im Altbau mit höherer Vorlauftemperatur liegt sie meist
niedriger, typischerweise bei 3,0 bis 3,5. Wie COP und JAZ zustande kommen, erklärt der Ratgeber
{a('/funktionsweise-einer-waermepumpe/', 'Funktionsweise einer Wärmepumpe')}.</p>
{A.box_dark("Rechenbeispiel Einfamilienhaus*",
    "Wärmebedarf 12.000 kWh pro Jahr, JAZ 3,5 bis 4: Die Wärmepumpe braucht rund 3.000 bis 3.500 kWh Strom. "
    "Bei rund 30 Cent je Kilowattstunde (je nach Tarif) sind das etwa 700 bis 1.100 Euro pro Jahr.")}
{A.table(
    ["Heizsystem", "Heizkosten pro Jahr bei 12.000 kWh Wärmebedarf*"],
    [
        ["Ölheizung", "1.500 bis 2.200 €"],
        ["Gasheizung", "1.400 bis 1.900 €"],
        ["Luft-Wasser-Wärmepumpe", "700 bis 1.100 €"],
        ["Luftwärmepumpe + Photovoltaik", "200 bis 500 €"],
    ],
    hl_cols=(1,),
)}
<p>Im Vergleich zur Öl- oder Gasheizung sparen Sie damit jedes Jahr mehrere hundert Euro. Richtig günstig
wird es mit eigenem Sonnenstrom: Warmwasser läuft von April bis Oktober fast vollständig über die
PV-Anlage, in der Übergangszeit auch ein guter Teil der Heizung. Wie Sie beides kombinieren, zeigt der
Ratgeber {a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}.</p>
{A.box("Im Dezember und Jänner liefert eine PV-Anlage in Kärnten und der Steiermark nur einen kleinen Teil "
       "ihres Jahresertrags. Genau dann braucht die Wärmepumpe am meisten Strom. Die großen Einsparungen durch "
       "PV entstehen deshalb in den Übergangsmonaten und beim Warmwasser, nicht im tiefen Winter.",
       label="Ehrlich gerechnet:")}
<p><small>*Richtwerte für ein Einfamilienhaus. Ihre Kosten hängen von Wärmebedarf, Jahresarbeitszahl und
Stromtarif ab.</small></p>
"""),
        ("Förderung für die Luftwärmepumpe: Stand Oktober 2026", "foerderung", f"""
<p>Bei der Förderung hat sich 2026 viel bewegt. Der aktuelle Stand für neue Projekte:</p>
<ul>
  <li><b>Bund:</b> Die Fördermittel für den Kesseltausch 2026 (Sanierungsoffensive, bis 7.500 Euro für eine
  Wärmepumpe) sind laut Ministerium seit Juli 2026 vollständig vergeben, „Sauber Heizen für Alle 2026“ ist
  ebenfalls beendet. Neue Registrierungen sind derzeit nicht möglich, bereits Registrierte werden nach den
  geltenden Bedingungen abgewickelt. Details: {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive 2026')}.</li>
  <li><b>Ausblick:</b> Für 2027 hat das Ministerium einen Förderrahmen von 360 Millionen Euro vorgesehen,
  davon 179 Millionen Euro für den Kesseltausch (BMLUK, Juli 2026). Ab wann und zu welchen Bedingungen
  wieder registriert werden kann, prüfen wir vor jedem Angebot.</li>
  <li><b>Kärnten:</b> Das Land zahlt 2026 eine Pauschale von 3.000 Euro für die Wärmepumpe, plus 1.500 Euro
  bei Errichtung einer Solaranlage und 200 Euro für den hydraulischen Abgleich. Ob das Budget reicht und
  wie das Land Projekte ohne Bundesförderung behandelt, klären wir vor dem Angebot. Kelag-Stromkunden
  erhalten zusätzlich eine Wärmepumpen-Prämie von 1.200 Euro als Gutschrift über zwei Jahre.</li>
  <li><b>Steiermark:</b> Für neue Wärmepumpen nimmt das Land derzeit keine Förderanträge an. Gefördert wird
  nur der Tausch mindestens 15 Jahre alter Wärmepumpen oder Biomassekessel, mit höchstens 30 Prozent und
  höchstens 1.500 Euro. Der Umstieg von Öl oder Gas ist damit nicht gefördert.</li>
  <li><b>Steuer:</b> Die {a('/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/',
  'Öko-Sonderausgabenpauschale')} setzt eine ausbezahlte Bundesförderung voraus und betrifft damit derzeit
  vor allem bereits registrierte Projekte.</li>
</ul>
<p>Alle Länder im Vergleich: {a('/landesfoerderungen-fuer-die-waermepumpe/', 'Landesförderungen für die Wärmepumpe')}.</p>
{A.box_dark("Unser Rat für die Planung",
    "Bereiten Sie das Projekt jetzt vor (Heizlast, Aufstellort, Angebot), aber unterschreiben Sie keinen "
    "Auftrag, bevor geklärt ist, ab wann Leistungen förderfähig sind. Bei Bundesprogrammen muss die "
    "Registrierung in der Regel vor der Umsetzung erfolgen. Wir behalten die Förderstellen im Blick und "
    "melden uns, sobald eine Registrierung wieder möglich ist.")}
{A.cta("Kosten für Ihr Haus konkret berechnen lassen",
       "EBZ Energie erstellt eine Heizlastberechnung vor Ort und ein Festpreisangebot mit allen Positionen. "
       "Die Förderabwicklung übernehmen wir für Sie.",
       secondary=("waermepumpe", "Zum Wärmepumpen-Installateur"))}
"""),
        ("Für welches Haus eignet sich eine Luftwärmepumpe?", "eignung", f"""
<p>Die Luftwärmepumpe ist heute die Standardlösung für Neubauten und für die meisten sanierten
Bestandsgebäude. Entscheidend ist nicht das Baujahr, sondern die benötigte Vorlauftemperatur:</p>
{A.table(
    ["Gebäude", "Vorlauftemperatur", "Eignung"],
    [
        ["Neubau mit Fußbodenheizung", "um 35 °C", "ideal, sehr hohe Effizienz"],
        ["Teilsanierter Altbau mit Heizkörpern", "50 bis 55 °C", "meist gut geeignet, oft reicht der Tausch einzelner zu kleiner Heizkörper"],
        ["Unsanierter Altbau mit hohem Wärmebedarf", "über 55 °C", "möglich, aber die Effizienz sinkt; Dämmung prüfen"],
    ],
    hl_cols=(2,),
)}
<p>Mehr zu Heizkörpern, Dämmung und Vorlauftemperatur im Bestand: {a('/waermepumpe-im-altbau/',
'Wärmepumpe im Altbau')}. Bei hoher Heizlast oder wenn ein Außengerät nicht möglich ist, lohnt der
Vergleich mit einer {a('/erdwaermepumpe-kosten/', 'Erdwärmepumpe')}.</p>
"""),
        ("Aufstellung und Schall: Was Sie beachten sollten", "aufstellung", f"""
<p>Die Außeneinheit einer Luft-Wasser-Wärmepumpe saugt Umgebungsluft an und bläst abgekühlte Luft aus.
Moderne Geräte sind im Normalbetrieb leise, trotzdem entscheidet der Aufstellort, ob Sie und Ihre
Nachbarn etwas hören. Vier Punkte zählen bei der Planung:</p>
<ul>
  <li><b>Abstand zu Schlafzimmerfenstern</b>, auch zu denen der Nachbarn.</li>
  <li><b>Keine Aufstellung in Ecken oder Nischen</b>, weil Wände den Schall reflektieren und verstärken.</li>
  <li><b>Nachtabsenkung und Flüstermodus</b>, die viele Geräte heute serienmäßig haben.</li>
  <li><b>Kondensatablauf und Frostschutz</b>, damit im Winter keine Eisplatte vor dem Gerät entsteht.</li>
</ul>
<p>Gemeinden und Länder haben eigene Vorgaben zu Schall und Abständen. Je nach Gemeinde kann für das
Außengerät eine Bauanzeige oder eine Mitteilung an die Baubehörde nötig sein. Wir planen den Standort
immer mit einer Schallabschätzung und klären die Meldepflicht im Rahmen der Planung.</p>
"""),
        ("So läuft Ihr Projekt mit EBZ Energie ab", "ablauf", f"""
{A.steps([
    ("Beratung vor Ort",
     "Wir sehen uns Heizraum, Heizflächen, Stromanschluss und den möglichen Aufstellort an und besprechen "
     "Ihre Ziele."),
    ("Heizlastberechnung und Angebot",
     "Sie erhalten ein Festpreisangebot mit allen Positionen, abgestimmt auf die tatsächliche Heizlast."),
    ("Förderung klären",
     "Wir prüfen Landes- und Bundesförderung und registrieren zum richtigen Zeitpunkt, bevor Kosten entstehen."),
    ("Montage",
     "Zertifizierte Fachkräfte bauen die Altanlage aus und die Wärmepumpe ein, meist in zwei bis vier Tagen."),
    ("Inbetriebnahme und Einweisung",
     "Wir stellen Heizkurve und Warmwasser ein, erklären die App und reichen die Förderunterlagen ein."),
])}
"""),
        ("Fazit: Luftwärmepumpe, die wirtschaftliche Standardlösung", "fazit", f"""
<p>Mit 14.000 bis 28.000 Euro ist die Luftwärmepumpe die günstigste Art, eine fossile Heizung dauerhaft zu
ersetzen. Im Betrieb kostet sie rund halb so viel wie eine Gasheizung und mit eigener PV-Anlage noch
deutlich weniger. Weil die Bundesförderung 2026 ausgeschöpft ist und neue Registrierungen derzeit nicht
möglich sind, lohnt jetzt die saubere Vorbereitung: Heizlast berechnen, Aufstellort klären, Angebot
einholen und die Förderlage vor der Auftragsvergabe prüfen.</p>
{A.cta("Jetzt Luftwärmepumpe planen",
       "Wir rechnen Ihr Haus durch, kombinieren auf Wunsch mit Photovoltaik und Speicher und übernehmen die "
       "Förderanträge.",
       primary=("kontakt", "Beratungstermin vereinbaren"),
       secondary=("/photovoltaik-fuer-waermepumpe/", "Wärmepumpe mit Photovoltaik"))}
"""),
    ],

    "partner": {
        "h2": "Ihre Luftwärmepumpe vom Fachbetrieb aus Villach",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie plant und installiert Luftwärmepumpen in Kärnten und der Steiermark, auf Wunsch "
                 "kombiniert mit Photovoltaik, Speicher und Energiemanagement. Mit zertifizierten Fachkräften, "
                 "Festpreisangebot und kompletter Förderabwicklung."),
        "grid": [
            ("Heizlast statt Schätzung", "Dimensionierung nach Berechnung, nicht nach Quadratmetern."),
            ("PV und Wärmepumpe aus einer Hand", "Ein Ansprechpartner, ein abgestimmtes System."),
            ("Förderung im Blick", "Wir registrieren bei Land und Bund zum richtigen Zeitpunkt."),
            ("4,9 Sterne bei Google", "Bewertet von Kundinnen und Kunden aus der Region."),
        ],
    },

    "faq": [
        ("Was kostet eine Luftwärmepumpe für ein Einfamilienhaus?",
         "Eine Luft-Wasser-Wärmepumpe kostet 2026 im Neubau inklusive Montage meist 14.000 bis 22.000 Euro, "
         "in der Sanierung 16.000 bis 28.000 Euro, jeweils vor Förderung. Die Spanne hängt vor allem von der "
         "Heizlast, dem Pufferspeicher, der Warmwasserbereitung und davon ab, ob Heizkörper getauscht werden "
         "müssen."),
        ("Wie viel Strom verbraucht eine Luftwärmepumpe im Jahr?",
         "Bei einem Wärmebedarf von 12.000 Kilowattstunden und einer Jahresarbeitszahl von 3,5 bis 4 braucht "
         "eine Luftwärmepumpe rund 3.000 bis 3.500 Kilowattstunden Strom. Das entspricht bei rund 30 Cent je "
         "Kilowattstunde etwa 700 bis 1.100 Euro pro Jahr, je nach Tarif."),
        ("Was kostet eine Luft-Luft-Wärmepumpe?",
         "Eine Luft-Luft-Wärmepumpe startet bei rund 5.000 Euro, typisch sind 5.000 bis 15.000 Euro. Sie "
         "erwärmt direkt die Raumluft, versorgt kein Wasser-Heizsystem und bereitet kein Warmwasser. Für "
         "einzelne Räume oder kleine Wohnungen ist sie eine günstige Lösung."),
        ("Gibt es 2026 noch eine Bundesförderung für die Luftwärmepumpe?",
         "Für neue Projekte derzeit nicht: Die Mittel für den Kesseltausch 2026 (bis 7.500 Euro) sind "
         "vollständig vergeben, neue Registrierungen sind nicht möglich. Bereits registrierte Anträge werden "
         "normal abgewickelt. In Kärnten zahlt das Land 3.000 Euro Pauschale, in der Steiermark gibt es für "
         "neue Wärmepumpen derzeit keine Landesförderung."),
        ("Funktioniert eine Luftwärmepumpe auch im Altbau?",
         "Ja, wenn das Haus mit einer Vorlauftemperatur von höchstens 55 Grad Celsius warm wird. Das ist in "
         "vielen teilsanierten Häusern bereits der Fall. Wir prüfen das vor Ort mit einer Heizlastberechnung "
         "und sagen Ihnen ehrlich, ob einzelne Heizkörper getauscht werden sollten."),
        ("Wie laut ist eine Luftwärmepumpe?",
         "Moderne Außengeräte sind im Normalbetrieb leise, trotzdem zählt der Aufstellort. Entscheidend sind "
         "der Abstand zu Schlafzimmerfenstern der Nachbarn, keine reflektierenden Ecken oder Nischen und ein "
         "leiser Nachtmodus. Gemeinden und Länder haben eigene Vorgaben, daher planen wir den Standort mit "
         "einer Schallabschätzung."),
        ("Lohnt sich eine Luftwärmepumpe mit Photovoltaik?",
         "Ja. Im Frühling, Sommer und Herbst deckt die PV-Anlage einen großen Teil des Stroms für Warmwasser "
         "und Heizung. Mit Speicher und Energiemanagement sinken die Betriebskosten auf grob 200 bis 500 Euro "
         "pro Jahr. Im tiefen Winter kommt der Großteil des Stroms weiterhin aus dem Netz."),
        ("Luftwärmepumpe oder Erdwärmepumpe, was ist günstiger?",
         "In der Anschaffung ist die Luftwärmepumpe klar günstiger, weil keine Bohrung oder Kollektorfläche "
         "nötig ist: 14.000 bis 28.000 Euro gegenüber 22.000 bis 40.000 Euro. Die Erdwärmepumpe spart im "
         "Einfamilienhaus grob 150 bis 300 Euro Strom pro Jahr, das gleicht die Mehrkosten nur langsam aus."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Mit zertifizierten Fachkräften plant "
                    "und installiert EBZ Energie Wärmepumpen, Photovoltaik und Speicher in Kärnten und der "
                    "Steiermark und übernimmt die Förderabwicklung. Kosten und Förderstand werden anhand realer "
                    "Angebote und der offiziellen Förderstellen aktualisiert. Keine Rechts- oder "
                    "Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen der jeweiligen Stelle."),
    "sources": [
        ("BMLUK: Sanierungsoffensive 2026, alle Fördermittel abgeholt (13. Juli 2026)",
         "https://www.bmluk.gv.at/service/presse/klima-umwelt/2026/sanierungsoffensive-2026-alle-foerdermittel-abgeholt.html"),
        ("Sanierungsoffensive: Budget-Information",
         "https://www.sanierungsoffensive.gv.at/budget-information"),
        ("Umweltförderung: Kesseltausch Ein-/Zweifamilienhaus 2026",
         "https://www.umweltfoerderung.at/privatpersonen/kesseltausch-ein-zweifamilienhaus-und-reihenhaus-2026"),
        ("Land Steiermark: Förderung für Heizungen (Wohnbau)",
         "https://www.wohnbau.steiermark.at/cms/ziel/164947118/DE/"),
        ("gecheckt.at: Preise Luftwärmepumpe 2026",
         "https://www.gecheckt.at/preise/waermepumpen/kosten-luftwaermepumpe"),
    ],
    "related": [
        ("/kosten-einer-waermepumpe/", "Kosten einer Wärmepumpe: alle Arten im Vergleich"),
        ("/erdwaermepumpe-kosten/", "Erdwärmepumpe: Kosten, Bohrung und Förderung"),
        ("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"),
        ("waermepumpe", "Wärmepumpen-Installateur in Kärnten und Steiermark"),
    ],
    "cta": {
        "h3": "Luftwärmepumpe berechnen lassen",
        "text": "Heizlastberechnung vor Ort, Festpreisangebot mit allen Positionen und Förderabwicklung aus einer Hand.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre Luftwärmepumpe, ehrlich kalkuliert",
    "final_text": ("Kostenlose Erstberatung, transparente Zahlen und ein Ansprechpartner aus Villach, der Planung, "
                   "Montage und Förderabwicklung aus einer Hand koordiniert."),
}
