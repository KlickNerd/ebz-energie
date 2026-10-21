"""Ratgeber: PV-Anlage kaufen (Kaufentscheidung und Anbieterwahl).

Migriert von ebz-photovoltaik.at/pv-anlage-kaufen/ (veröffentlicht 15.09.2026).
Fokus: Ablauf, Anbieterwahl, Angebotsvergleich. Kosten nur kurz (Verweis auf /kosten-einer-solaranlage/),
Größenwahl in /pv-anlage-kwp-groessen/, Kauf vs. Miete in /solaranlage-mieten-oder-kaufen/.
Geändert gegenüber der Quelle:
  - Förderung auf Stand ab 23.10.2026: letzter EAG-Call (8. bis 22.10.2026) beendet, Bund derzeit nicht
    beantragbar, Systemförderung 2027 laut BMWET geplant (nicht beschlossen); Kärnten 3.000 EUR mit Speicher.
    Abschnitte "Tipp für den Oktober-Call" und "Angebot vor dem Fördercall sichern" entfernt.
  - Preise auf den freigegebenen EBZ-Richtpreis gesetzt (Quelle: 10 kWp 12.000 bis 18.000 EUR ohne Speicher
    plus Speicher 4.000 bis 10.000 EUR widersprach dem Anker 15.000 bis 22.000 EUR mit Speicher).
  - Eigenteam-Aussagen der Quelle ("eigenes Montageteam", "eigene Monteure", "unser eigenes Team") entfernt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "pv-anlage-kaufen",
    "path": "/pv-anlage-kaufen/",
    "title": "PV-Anlage kaufen: 10 Kriterien für den Anbieter | EBZ",
    "description": ("PV-Anlage kaufen: 10 Kriterien für den richtigen Anbieter, 8 Pflichtpositionen im Angebot, "
                    "Ablauf in 4 bis 10 Wochen und aktueller Förderstand ab Oktober 2026."),
    "eyebrow": "Photovoltaik · Kaufberatung",
    "crumb_label": "PV-Anlage kaufen",
    "h1": "PV-Anlage kaufen: An diesen 10 Kriterien erkennen Sie den richtigen Anbieter",
    "lead": ("Beim Kauf einer Photovoltaikanlage entscheidet der Anbieter mehr über Ertrag, Sicherheit und Ärger in "
             "den nächsten 25 Jahren als die Modulmarke. Dieser Ratgeber zeigt, woran Sie einen seriösen "
             "Fachbetrieb erkennen, wie Sie Angebote fair vergleichen und wie der Kauf abläuft."),
    "chips": [
        "<b>10 Kriterien</b> für die Anbieterwahl",
        "<b>8 Positionen</b> in jedem Angebot",
        "10 kWp mit Speicher: <b>15.000 bis 22.000 €</b>",
        "Kärnten: <b>3.000 €</b> mit Speicher",
    ],
    "date_published": "2026-09-15",
    "date_modified": "2026-10-21",
    "hero_img": "gen_hero",
    "hero_alt": "Photovoltaikanlage auf einem Hausdach: worauf Sie beim Kauf und bei der Anbieterwahl achten",

    "tldr": [
        "Beim Kauf entscheidet der Anbieter mehr als die Modulmarke. Achten Sie auf Besichtigung vor Ort, "
        "Belegplan und Statiknachweis, zertifizierte Fachkräfte, einen festen Ansprechpartner und regionale Referenzen.",
        "Ein vollständiges Angebot enthält acht Positionen: Module, Wechselrichter, Unterkonstruktion, Montage und "
        "Gerüst, Elektrik, Netzanmeldung, Förderabwicklung und Planungsunterlagen. Fehlt eine, kommt sie meist als Nachtrag.",
        "Richtpreis: 10 kWp mit Speicher rund 15.000 bis 22.000 Euro vor Förderung, inklusive Montage und "
        "20 Prozent Umsatzsteuer.",
        "Förderung ab 23. Oktober 2026: Der EAG-Bundeszuschuss ist für 2026 abgeschlossen, ab 2027 ist laut BMWET eine "
        "Systemförderung geplant (nicht beschlossen). Kärnten zahlt 3.000 Euro für PV ab 5 kWp mit Speicher.",
        "Vom Angebot bis zur fertigen Anlage vergehen meist 4 bis 10 Wochen, die Montage dauert ein bis zwei Tage. "
        "Finanzierung ab 147 Euro im Monat, die Anlage gehört ab Tag 1 Ihnen.",
    ],
    "kpis": [
        ("10", "Kriterien für die Anbieterwahl"),
        ("8", "Pflichtpositionen im Angebot"),
        ("15.000 bis 22.000 €", "10 kWp mit Speicher vor Förderung"),
        ("4 bis 10 Wochen", "vom Angebot bis zur fertigen Anlage"),
    ],

    "sections": [
        ("Warum der Anbieter wichtiger ist als die Modulmarke", "anbieter", f"""
<p><b>Wer eine PV-Anlage kauft, sollte zuerst den Anbieter prüfen und dann den Preis: Besichtigung vor Ort,
ein Angebot mit allen Positionen, Planungsunterlagen mit Statik und ein fester Ansprechpartner entscheiden über
25 Jahre Betrieb.</b> Eine 10-kWp-Anlage mit Speicher kostet bei EBZ Energie rund 15.000 bis 22.000 Euro vor
Förderung (Richtpreis, Stand Oktober 2026).</p>
<p>Die meisten Käufer vergleichen zuerst Module und Preise. Über Ertrag, Sicherheit und Ärger in den nächsten
Jahrzehnten entscheidet aber vor allem, <b>wer die Anlage plant und montiert</b>. Eine falsch dimensionierte
Anlage, eine undichte Dachdurchführung oder ein Förderantrag zur falschen Zeit kosten schnell mehr als jeder
Preisvorteil beim Modul. Gute Module halten 25 Jahre und länger, und genauso lange brauchen Sie einen Betrieb,
der Wartung, Garantiefälle und Erweiterungen wie {a('batteriespeicher', 'Speicher')}, Wallbox oder
{a('waermepumpe', 'Wärmepumpe')} übernimmt.</p>
"""),
        ("10 Kriterien für die Wahl des richtigen PV-Anbieters", "kriterien", f"""
{A.table(
    ["Kriterium", "Darauf achten", "Warnsignal"],
    [
        ["Besichtigung", "Termin vor Ort mit Blick auf Dach, Zählerkasten und Verschattung",
         "Angebot nur nach Satellitenbild oder Telefonat"],
        ["Planungsunterlagen", "Belegplan und Statiknachweis für Ihr Dach", "keine Aussage zur Statik"],
        ["Ausführung", "zertifizierte Fachkräfte, Termin und Ablauf vorab schriftlich",
         "niemand kann sagen, wer wann auf Ihr Dach kommt"],
        ["Angebot", "alle Positionen mit Hersteller, Typ und Menge", "Pauschalpaket ohne Details"],
        ["Dimensionierung", "nach Verbrauch, Dachfläche und Plänen wie Wärmepumpe oder E-Auto",
         "so groß wie möglich, ohne Begründung"],
        ["Förderung", "komplette Abwicklung inklusive Fristen und Reihenfolge", "Förderung wird garantiert"],
        ["Referenzen", "Projekte in der Region, echte Google-Bewertungen", "nur Stockfotos, keine Adresse in Österreich"],
        ["Zahlung", "Teilbeträge nach Baufortschritt", "hohe Vorauszahlung vor Lieferung"],
        ["Service", "fester Ansprechpartner, Wartung und Monitoring", "Hotline im Ausland oder gar keine"],
        ["Verkaufsstil", "Bedenkzeit, ehrliche Beratung", "Zeitdruck, Rabatt nur heute, Haustürgeschäft"],
    ],
)}
<p>Ein Anbieter muss nicht in allen zehn Punkten glänzen. Zwei oder mehr Warnsignale sollten Sie aber stutzig
machen, vor allem bei Besichtigung, Statik und Vorauszahlung. Echte Projekte mit Ort, Leistung und Ersparnis
finden Sie bei uns unter {a('referenzen', 'Referenzen')}.</p>
"""),
        ("So läuft der Kauf ab: von der Anfrage bis zur Inbetriebnahme", "ablauf", f"""
<p>Vom ersten Gespräch bis zur fertigen Anlage vergehen in der Regel vier bis zehn Wochen. Die Montage selbst
dauert beim Einfamilienhaus ein bis zwei Tage, die meiste Zeit entfällt auf Netzanmeldung und Lieferzeiten.
Bei EBZ Energie sieht der Ablauf so aus:</p>
{A.steps([
    ("Erstgespräch", "Wir klären Verbrauch, Pläne wie Wärmepumpe oder E-Auto und Ihr Budget."),
    ("Besichtigung vor Ort", "Wir prüfen Dach, Statik, Zählerkasten und Leitungswege."),
    ("Projektbericht und Angebot", "Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport sowie ein "
     "Festpreisangebot mit allen Positionen."),
    ("Förderung und Netzanmeldung", "Wir stellen Netzzugangsantrag und Förderanträge in der richtigen Reihenfolge, "
     "etwa die EMS-Registrierung vor der ersten Rechnung."),
    ("Montage und Inbetriebnahme", "Zertifizierte Fachkräfte montieren in ein bis zwei Tagen, danach richten wir "
     "Monitoring und App ein und übergeben die Unterlagen."),
])}
"""),
        ("Angebote richtig vergleichen", "angebote-vergleichen", f"""
<p>Zwei Angebote über 10 kWp können 4.000 Euro auseinanderliegen und trotzdem beide fair sein, oder eines davon
ist nur scheinbar günstig. Vergleichbar werden Angebote erst, wenn dieselben Leistungen enthalten sind. Diese
acht Positionen gehören in jedes vollständige PV-Angebot:</p>
{A.table(
    ["Position", "Was im Angebot stehen sollte"],
    [
        ["1. Module", "Hersteller, Typ, Leistung, Garantie"],
        ["2. Wechselrichter", "Hybrid oder Standard, speicherfähig ja oder nein"],
        ["3. Unterkonstruktion", "passend zu Dacheindeckung und Statik"],
        ["4. Montage und Gerüst", "inklusive, nicht als späterer Nachtrag"],
        ["5. Elektrik", "Zählerplatz, Überspannungsschutz, Leitungswege"],
        ["6. Netzanmeldung", "Netzzugangsantrag beim Netzbetreiber"],
        ["7. Förderabwicklung", "Landesförderung, EMS-Förderung und alle Fristen"],
        ["8. Planungsunterlagen", "Belegplan und Statiknachweis"],
    ],
    hl_cols=(0,),
)}
{A.box("Ein häufiger Trick bei Billigangeboten: Gerüst, Überspannungsschutz, Zählerplatz-Umbau oder die "
       "Netzanmeldung fehlen im Angebot und werden später nachverrechnet. Fragen Sie im Zweifel schriftlich nach, "
       "ob der Preis wirklich schlüsselfertig ist.", label="Vorsicht:")}
<p>Achten Sie außerdem darauf, dass beide Angebote dieselbe Anlagengröße und Speicherkapazität annehmen. Welche
Größe zu Ihrem Verbrauch passt, erklärt der Ratgeber
{a('/pv-anlage-kwp-groessen/', 'PV-Anlage mit 5, 10, 15 oder 20 kWp')}.</p>
{A.cta("Vollständiges Angebot statt Pauschalpaket",
       "EBZ Energie besichtigt Ihr Dach und erstellt ein Festpreisangebot mit allen acht Positionen, inklusive "
       "Projektbericht mit 3D-Belegplan und Statikreport.",
       primary=("kontakt", "Angebot anfragen"), secondary=("solarrechner", "Solarrechner starten"))}
"""),
        ("Was darf eine PV-Anlage 2026 kosten?", "preis", f"""
<p>Der Richtpreis für die häufigste Anlage im Einfamilienhaus, 10 kWp mit Speicher, liegt bei rund
<b>15.000 bis 22.000 Euro vor Förderung</b>, ohne Speicher bei rund 10.000 bis 15.000 Euro*. Seit dem Auslaufen
des Nullsteuersatzes am 1. April 2025 gelten für Photovoltaik wieder 20 Prozent Umsatzsteuer, sie ist in diesen
Werten enthalten.</p>
<p>Wo Ihre Anlage in der Spanne liegt, bestimmen Dachform, Eindeckung, Leitungswege, der Zustand des Zählerkastens
und die Wahl der Komponenten. Größere Anlagen sind pro kWp günstiger, weil Gerüst, Wechselrichter und
Anmeldung ohnehin anfallen. Die vollständige Preisübersicht mit Rechenbeispiel steht im Ratgeber
{a('/kosten-einer-solaranlage/', 'Kosten einer Solaranlage')}, was in einer Komplettanlage steckt, zeigt
{a('/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/', 'Komplettanlage 10 kWp mit Speicher')}.</p>
<p><small>*EBZ-Richtwerte, Stand Oktober 2026, inklusive Montage und 20 Prozent Umsatzsteuer, vor Förderung.
Der verbindliche Preis steht nach der Besichtigung im Festpreisangebot.</small></p>
"""),
        ("Förderung beim Kauf: Stand ab 23. Oktober 2026", "foerderung", f"""
<p>Für den Kauf einer neuen Anlage gilt derzeit diese Förderlage:</p>
{A.table(
    ["Förderung", "Höhe", "Status"],
    [
        ["Bund: EAG-Investitionszuschuss", "im Call 2026: 150 € je kWp bis 10 kWp, 140 € bis 20 kWp, 150 € je kWh Speicher",
         "für 2026 abgeschlossen, letzter Call endete am 22. Oktober 2026"],
        ["Bund: Systemförderung 2027", "Höhe und Kriterien offen", "laut BMWET geplant, nicht beschlossen"],
        ["Land Kärnten", "3.000 € Pauschale für PV ab 5 kWp mit Speicher ab 5 kWh",
         "2. Landes-Call bis 31. Dezember 2026, Antrag nach Fertigstellung"],
        ["Land Steiermark", "keine PV-Landesförderung offen", "manche Gemeinden zahlen einen Zuschuss"],
        ["Klimafonds: EMS-Förderung", "50 % der EMS-Kosten, max. 600 €", "Registrierung vor der Rechnung, bis 15. April 2027"],
    ],
    hl_cols=(1,),
)}
<p>Für 2027 plant der Bund laut Eckpunkten des BMWET eine Systemförderung für Speicher mit intelligenter Steuerung,
beantragt nach Installation und Rechnung statt im Fördercall. Projekte mit intelligentem Speicher, die ab
1. November 2026 in Betrieb gehen, sollen dann beantragbar sein. Beschlossen ist das nicht, Höhe und
Technikkriterien sind offen. Für Ihre Kaufentscheidung heißt das: Planen Sie gleich mit Speicher und
{a('ems', 'Energiemanagement')}. Das sichert in Kärnten die 3.000 Euro und wahrt die Chance auf die
Systemförderung, ohne dass Sie auf einen Stichtag warten müssen.</p>
{A.box("Seriöse Anbieter garantieren keine Förderung. Sie kennen Fristen und Reihenfolge, stellen die Anträge "
       "rechtzeitig und sagen Ihnen offen, was noch nicht beschlossen ist.")}
<p>Alle Details finden Sie in den Ratgebern
{a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')},
{a('foerderung_kaernten', 'Photovoltaik-Förderung Kärnten')} und
{a('foerderung_steiermark', 'Photovoltaik-Förderung Steiermark')}.</p>
"""),
        ("Kaufen oder finanzieren?", "finanzieren", f"""
<p>Nicht jeder möchte 15.000 Euro oder mehr auf einmal investieren. Bei EBZ Energie können Sie Ihre Anlage
deshalb auch <b>finanzieren</b>, ab 147 Euro im Monat inklusive Speicher, ohne auf Vorteile zu verzichten:</p>
<ul>
  <li>Die Anlage gehört <b>ab dem ersten Tag Ihnen</b>.</li>
  <li>Sie erhalten als Privatperson die <b>volle Förderung</b> wie beim Barkauf.</li>
  <li>Die Bonitätsprüfung läuft <b>digital in Minuten</b>, es gibt <b>keinen Grundbucheintrag</b>.</li>
</ul>
<p>Weil die Stromersparnis ab dem ersten Monat wirkt, deckt sie bei vielen Haushalten einen großen Teil der Rate.
Konditionen und Rechenbeispiele stehen auf der Seite {a('finanzierung', 'Finanzierung')}. Warum eine Mietanlage
etwas anderes ist (die Anlage gehört dort dem Anbieter, die Förderung auch), erklärt der Ratgeber
{a('/solaranlage-mieten-oder-kaufen/', 'Solaranlage mieten oder kaufen')}.</p>
"""),
        ("Online-Anbieter oder regionaler Fachbetrieb?", "online-oder-regional", f"""
{A.table(
    ["", "Online-Anbieter", "Regionaler Fachbetrieb"],
    [
        ["Preis", "oft günstige Pakete, Nachträge möglich", "Festpreis nach Besichtigung"],
        ["Planung", "häufig per Satellitenbild", "vor Ort, mit Statik und Zählerkasten"],
        ["Ansprechpartner", "Ticket-System, wechselnde Kontakte", "ein fester Ansprechpartner von der Planung bis zur Übergabe"],
        ["Service", "lange Wege bei Garantiefällen", "Betrieb in der Nähe"],
        ["Erweiterung", "oft schwierig", "Speicher, Wallbox, Wärmepumpe aus einer Hand"],
    ],
    hl_cols=(2,),
)}
<p>Online-Pakete können für einfache Dächer passen. Je mehr Sonderfälle Ihr Haus hat, etwa ein alter
Zählerkasten, ein Blechdach oder eine geplante Wärmepumpe, desto mehr zahlt sich die Besichtigung vor Ort aus.</p>
{A.cta("Ihre PV-Anlage vom Fachbetrieb aus Villach",
       "Besichtigung, Projektbericht, Festpreis, Förderabwicklung und Montage durch zertifizierte Fachkräfte. "
       "Auf Wunsch mit Finanzierung.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
        ("Fazit: Erst den Anbieter prüfen, dann den Preis", "fazit", f"""
<p>Eine PV-Anlage ist eine Investition für mehrere Jahrzehnte. Wer den Anbieter nach Besichtigung,
Planungsunterlagen, Angebotsumfang, Referenzen und Service auswählt, vermeidet teure Überraschungen. Seit dem
Ende des letzten Bundescalls am 22. Oktober 2026 gilt zusätzlich: Mit Speicher und Energiemanagement planen,
in Kärnten die 3.000 Euro Landespauschale nutzen und die geplante Systemförderung 2027 im Blick behalten.</p>
"""),
    ],

    "partner": {
        "h2": "Warum Kundinnen und Kunden EBZ Energie wählen",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und Wallboxen in "
                 "Kärnten und der Steiermark, mit über 300 dokumentierten Projekten. Vom ersten Gespräch bis zur "
                 "Förderabwicklung haben Sie einen festen Ansprechpartner."),
        "grid": [
            ("Zertifizierte Fachkräfte", "Planung und Montage aus einer Hand, koordiniert von Ihrem Ansprechpartner."),
            ("Projektbericht", "3D-Belegplan und Statikreport vor der Entscheidung."),
            ("4,9 Sterne bei Google", "Echte Bewertungen aus der Region."),
            ("Finanzierung möglich", "Ab 147 Euro im Monat, Anlage gehört ab Tag 1 Ihnen."),
        ],
    },

    "faq": [
        ("Wie erkenne ich einen seriösen PV-Anbieter?",
         "An einer Besichtigung vor dem Angebot, einem Angebot mit allen Positionen und Herstellerangaben, "
         "Belegplan und Statiknachweis, regionalen Referenzen mit echten Bewertungen und einem festen "
         "Ansprechpartner nach der Montage. Vorsicht bei Zeitdruck, Haustürgeschäften, hohen Vorauszahlungen und "
         "Förderversprechen mit Garantie."),
        ("Was kostet eine PV-Anlage 2026 in Österreich?",
         "Eine 10-kWp-Anlage kostet ohne Speicher rund 10.000 bis 15.000 Euro, mit Speicher rund 15.000 bis "
         "22.000 Euro vor Förderung, inklusive Montage und 20 Prozent Umsatzsteuer (EBZ-Richtpreis). Größere "
         "Anlagen sind pro kWp günstiger. Details im Ratgeber Kosten einer Solaranlage."),
        ("Welche Förderung gibt es aktuell beim Kauf einer PV-Anlage?",
         "Der EAG-Bundeszuschuss ist für 2026 abgeschlossen, der letzte Call endete am 22. Oktober 2026. In Kärnten "
         "gibt es 3.000 Euro Landespauschale für PV ab 5 kWp mit Speicher ab 5 kWh (2. Landes-Call bis "
         "31. Dezember 2026), in der Steiermark derzeit keine PV-Landesförderung. Für das Energiemanagement sind "
         "bis zu 600 Euro vom Klimafonds möglich."),
        ("Soll ich mit dem Kauf auf die Systemförderung 2027 warten?",
         "Meist nicht. Laut BMWET sollen Projekte mit intelligentem Speicher, die ab 1. November 2026 in Betrieb "
         "gehen, 2027 im neuen System beantragbar sein, beantragt nach Installation und Rechnung. Beschlossen ist das "
         "noch nicht, die Höhe ist offen. Wer mit Speicher und Energiemanagement plant, wahrt die Chance, ohne "
         "auf einen Stichtag zu warten."),
        ("Muss ich den Förderantrag vor dem Kauf stellen?",
         "Das hängt von der Förderung ab. Die Kärntner Landespauschale wird nach der Fertigstellung beantragt, die "
         "EMS-Förderung muss dagegen vor der ersten Rechnung registriert sein. Wir stimmen die Reihenfolge so ab, "
         "dass keine Förderung verloren geht."),
        ("Kann ich eine PV-Anlage finanzieren?",
         "Ja. Bei EBZ Energie finanzieren Sie ab 147 Euro im Monat inklusive Speicher. Die Anlage gehört ab dem "
         "ersten Tag Ihnen, Sie erhalten die volle Förderung, die Bonitätsprüfung läuft digital in Minuten und es "
         "gibt keinen Grundbucheintrag."),
        ("Lohnt sich ein Online-Anbieter statt eines regionalen Fachbetriebs?",
         "Online-Anbieter locken oft mit niedrigen Paketpreisen, planen aber häufig per Satellitenbild und ohne "
         "Ansprechpartner vor Ort. Bei Statik, Zählerkasten, Garantiefällen und späteren Erweiterungen zahlt sich ein "
         "regionaler Fachbetrieb mit festem Ansprechpartner meist aus."),
        ("Wie lange dauert es vom Angebot bis zur fertigen Anlage?",
         "In der Regel vier bis zehn Wochen. Die Montage selbst dauert beim Einfamilienhaus ein bis zwei Tage, die "
         "meiste Zeit entfällt auf Netzanmeldung und Lieferzeiten."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. EBZ Energie plant und installiert "
                    "Photovoltaik, Batteriespeicher, Wärmepumpen und Wallboxen in Kärnten und der Steiermark und "
                    "übernimmt die komplette Förderabwicklung. Preise und Förderstand werden anhand realer Angebote "
                    "und der offiziellen Förderstellen aktualisiert. Keine Rechts- oder Steuerberatung, maßgeblich "
                    "sind die offiziellen Förderbedingungen der jeweiligen Stelle."),
    "sources": [
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("LK Kärnten: EAG-Investitionszuschuss, letzter Fördercall 2026",
         "https://ktn.lko.at/eag-investitionszuschuss-letzter-f%C3%B6rdercall-2026+2400+4457200"),
    ],
    "related": [
        ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage 2026"),
        ("/pv-anlage-kwp-groessen/", "PV-Anlage mit 5, 10, 15 oder 20 kWp"),
        ("/solaranlage-mieten-oder-kaufen/", "Solaranlage mieten oder kaufen?"),
        ("finanzierung", "Finanzierung ab 147 € im Monat"),
    ],
    "cta": {
        "h3": "Angebot mit allen Positionen",
        "text": "Besichtigung, Projektbericht mit 3D-Belegplan und Statikreport, Festpreis. Kostenlos und unverbindlich.",
        "primary": ("kontakt", "Angebot anfordern"),
    },
    "final_h2": "Sprechen wir über Ihre Anlage",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein fester Ansprechpartner aus Villach, der "
                   "Planung, Montage und Förderabwicklung aus einer Hand übernimmt."),
}
