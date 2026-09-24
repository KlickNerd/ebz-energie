"""Ratgeber: Kosten einer Solaranlage 2026 (Preis-Guide mit Speicher).

Zusammengeführt aus zwei Live-Artikeln (Duplikate):
  /kosten-einer-solaranlage/ (Dez. 2025) und
  /kosten-von-photovoltaikanlagen-mit-speicher/ (Dez. 2025).
Preise auf den freigegebenen EBZ-Richtpreis (10 kWp mit Speicher rund 15.000 bis
22.000 Euro vor Förderung) und die EAG-Förderung 2026 abgestimmt. Abweichungen
der Quellen (24.000 Euro, 20.000 bis 30.000 Euro, Nullsteuersatz, Amortisation
13,5 Jahre) sind im Migrationsbericht dokumentiert.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "kosten-einer-solaranlage",
    "path": "/kosten-einer-solaranlage/",
    "title": "Kosten einer Solaranlage 2026: Preise mit Speicher | EBZ",
    "description": ("Kosten einer Solaranlage: 10 kWp ohne Speicher 10.000 bis 15.000 €, mit Speicher "
                    "15.000 bis 22.000 € vor Förderung. Mit Förderabzug 2026 und Rechenbeispiel."),
    "eyebrow": "Photovoltaik · Kosten",
    "crumb_label": "Kosten einer Solaranlage",
    "h1": "Kosten einer Solaranlage 2026: 10 kWp mit Speicher ab rund 15.000 Euro",
    "lead": ("Eine 10-kWp-Anlage kostet ohne Speicher rund 10.000 bis 15.000 Euro, mit Speicher 15.000 bis "
             "22.000 Euro vor Förderung. Dieser Preis-Guide zeigt, woraus sich die Summe zusammensetzt, "
             "was Bund und Land abziehen und wann sich die Anlage bezahlt gemacht hat."),
    "chips": [
        "10 kWp ohne Speicher: <b>10.000 bis 15.000 €</b>",
        "10 kWp mit Speicher: <b>15.000 bis 22.000 €</b>",
        "Förderung 2026: <b>150 €/kWp + 150 €/kWh</b>",
        "Finanzierung: <b>ab 147 €/Monat</b>",
    ],
    "date_published": "2025-12-17",
    "date_modified": "2026-09-24",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit Photovoltaikanlage auf dem Dach: Kosten einer Solaranlage mit Speicher",

    "tldr": [
        "Richtpreis 2026: Eine 10-kWp-Anlage kostet ohne Speicher rund 10.000 bis 15.000 Euro, mit "
        "Batteriespeicher rund 15.000 bis 22.000 Euro vor Förderung, jeweils inklusive Montage und "
        "Inbetriebnahme.",
        "Der Speicher kostet je nach Kapazität 5.000 bis 9.000 Euro Aufpreis und hebt den Eigenverbrauch "
        "von etwa 30 Prozent auf 60 bis 80 Prozent.",
        "Die Bundesförderung (EAG) bringt 2026 für 10 kWp mit 10 kWh Speicher rund 3.000 Euro plus "
        "Made-in-Europe-Bonus, in Kärnten kommen 3.000 Euro Landespauschale dazu.",
        "Laufende Kosten liegen bei 1 bis 2 Prozent der Anschaffung pro Jahr, die Module halten 25 bis "
        "30 Jahre, der Wechselrichter rund 15 Jahre.",
        "Amortisation im Rechenbeispiel: rund 9 Jahre für einen Standardhaushalt, rund 6 Jahre mit "
        "Wärmepumpe und E-Auto. In EBZ-Projekten mit hohem Eigenverbrauch typisch 4 bis 6 Jahre.",
    ],
    "kpis": [
        ("15.000 bis 22.000 €", "10 kWp mit Speicher, vor Förderung"),
        ("5.000 bis 9.000 €", "Aufpreis für den Batteriespeicher"),
        ("bis 85 %", "weniger Stromkosten mit Speicher"),
        ("4 bis 6 Jahre", "typische Amortisation in EBZ-Projekten"),
    ],

    "sections": [
        ("Was kostet eine Solaranlage 2026? Die Richtpreise", "richtpreise", f"""
<p>Die Kosten einer Solaranlage hängen von der Leistung in Kilowatt-Peak (kWp), vom Speicher und vom
Montageaufwand ab. Für ein Einfamilienhaus hat sich eine Anlagengröße von rund 10 kWp als Standard
etabliert: Sie braucht 50 bis 60 Quadratmeter Dachfläche, besteht aus 22 bis 25 Modulen und liefert in
Österreich etwa 10.000 Kilowattstunden Strom pro Jahr. Die folgenden Richtwerte gelten für
Komplettanlagen inklusive Montage, Elektroinstallation und Anmeldung beim Netzbetreiber:</p>
{A.table(
    ["Anlage", "Richtpreis 2026*", "Entspricht"],
    [
        ["10 kWp ohne Speicher", "10.000 bis 15.000 €", "1.000 bis 1.500 € je kWp"],
        ["Batteriespeicher 5 bis 10 kWh (Aufpreis)", "5.000 bis 9.000 €", "je nach Kapazität und Hersteller"],
        ["10 kWp mit Speicher (Komplettanlage)", "15.000 bis 22.000 €", "EBZ-Richtpreis vor Förderung"],
        ["Zählerschrank-Erneuerung (falls nötig)", "oft über 1.000 €", "nur bei alten Verteilern"],
    ],
    hl_cols=(1,),
)}
<p>Grundsätzlich gilt: Je größer die Anlage, desto günstiger der Preis pro kWp. Gerüst, Anfahrt,
Wechselrichter und Elektroanschluss fallen bei einer 5-kWp-Anlage genauso an wie bei 10 kWp, verteilen
sich aber auf weniger Module. Deshalb lohnt es sich meist, das Dach vollständig zu belegen, statt die
Anlage künstlich klein zu halten. Die genaue Kalkulation für Ihr Dach liefert der
{a('solarrechner', 'EBZ-Solarrechner')} oder ein Angebot mit Projektbericht, 3D-Belegplan und Statikreport.</p>
<p><small>*Richtwerte für marktübliche Komponenten und Standardmontage auf Ziegeldach, vor Abzug von
Förderungen. Der tatsächliche Preis hängt von Dach, Komponentenwahl und Hauselektrik ab.</small></p>
"""),
        ("Woraus sich die Kosten zusammensetzen", "kostenbausteine", f"""
<p>Den größten Anteil an der Gesamtrechnung haben die Solarmodule mit etwa 30 bis 40 Prozent.
Hochleistungsmodule kosten pro Stück mehr, holen aus einer begrenzten oder teilverschatteten Dachfläche
aber deutlich mehr Strom heraus. Glas-Glas-Module sind robuster und langlebiger als Glas-Folie-Module,
kosten in der Anschaffung aber etwas mehr.</p>
<p>Der zweite große Posten ist der Wechselrichter, bei Anlagen mit Speicher meist ein Hybrid-Wechselrichter,
der PV-Management und Batterieladung vereint. Hier sollten Sie nicht sparen: Fällt das Gerät aus, steht die
gesamte Produktion. Dazu kommen Montagesystem, Verkabelung, Gerüst und die Arbeit der zertifizierten
Fachkräfte. Hochwertige Betriebe montieren mit Blech-Ersatzziegeln statt bearbeiteter Dachziegel, damit
das Dach über Jahrzehnte dicht bleibt.</p>
<p>Oft übersehen werden die administrativen Positionen: Anmeldung beim Netzbetreiber, Abnahme durch den
Elektriker, Zählertausch und die Förderabwicklung. Ein seriöses Komplettangebot weist diese Punkte
transparent aus. Bei EBZ Energie sind Projektbericht mit 3D-Belegplan und Statikreport, Netzzutrittsantrag
und Förderanträge Teil des Pakets.</p>
{A.net([
    ("☀", "Solarmodule", "30 bis 40 % der Kosten, 22 bis 25 Stück bei 10 kWp"),
    ("◎", "Wechselrichter", "Hybrid-Gerät für PV und Speicher, Lebensdauer rund 15 Jahre"),
    ("▮", "Batteriespeicher", "5.000 bis 9.000 € Aufpreis, 5 bis 10 kWh üblich"),
    ("⌂", "Montage und Elektro", "Gerüst, Unterkonstruktion, Verkabelung, Zählerschrank"),
], "Komplettanlage inklusive Anmeldung",
   "Dazu kommen Netzzutrittsantrag, Förderanträge und Inbetriebnahme. Bei EBZ Energie alles aus einer Hand.")}
"""),
        ("Speicher: Was der Aufpreis bringt", "speicher", f"""
<p>Ohne Speicher nutzt ein typischer Haushalt nur rund 30 Prozent des eigenen Solarstroms direkt, der
Rest fließt zu 5 bis 10 Cent je Kilowattstunde ins Netz, während der Bezug aus dem Netz rund 32 Cent
kostet. Ein {a('batteriespeicher', 'Batteriespeicher')} verschiebt den Mittagsüberschuss in den Abend
und hebt den Eigenverbrauch auf 60 bis 80 Prozent. Für 5.000 bis 9.000 Euro Aufpreis sinkt die
Stromrechnung damit um bis zu 85 Prozent.</p>
<p>Die Kapazität sollte zum Verbrauch passen: Ein Speicher mit 5 kWh deckt den Nachtbedarf im Sommer,
wer eine Wärmepumpe betreibt oder ein E-Auto lädt, greift eher zu 10 kWh. Als Faustregel gilt das
Verhältnis 1:1, also 10 kWh Speicher zu 10 kWp Leistung. Ein zu großer Speicher wird im Winter nie
voll, ein zu kleiner ist im Sommer schnell am Limit. Moderne Systeme auf Lithium-Eisenphosphat-Basis
sind modular und lassen sich später erweitern.</p>
{A.box("Der Bund fördert Speicher 2026 nur gemeinsam mit einer PV-Neuerrichtung oder -Erweiterung "
       "(150 Euro je kWh). Wer den Speicher erst später nachrüstet, verliert diese Förderung. Details im "
       "Ratgeber " + a('/pv-speicher-nachruesten/', 'PV-Speicher nachrüsten') + ".")}
"""),
        ("Förderung abziehen: Was 2026 übrig bleibt", "foerderung", f"""
<p>Seit 1. April 2025 gilt für Photovoltaik wieder der reguläre Umsatzsteuersatz von 20 Prozent, der
Nullsteuersatz ist ausgelaufen. Dafür ist die Investitionsförderung des Bundes (EAG) 2026 wieder voll
aktiv: 150 Euro je kWp bis 10 kWp, 140 Euro je kWp bis 20 kWp und 150 Euro je kWh Speicherkapazität.
Für Module, Wechselrichter und Speicher von der White List der EAG-Abwicklungsstelle gibt es zusätzlich
je 10 Prozent Made-in-Europe-Bonus auf den jeweiligen Zuschuss.</p>
{A.table(
    ["Förderung für 10 kWp + 10 kWh", "Rechnung", "Betrag*"],
    [
        ["EAG-Bund, PV-Anlage", "10 kWp × 150 €", "1.500 €"],
        ["EAG-Bund, Speicher", "10 kWh × 150 €", "1.500 €"],
        ["Made-in-Europe-Bonus", "10 % je Komponente auf den Zuschuss", "rund 450 €"],
        ["Landespauschale Kärnten", "PV ab 5 kWp mit Speicher ab 5 kWh", "3.000 €"],
        ["Summe in Kärnten", "", "rund 6.450 €"],
    ],
    hl_cols=(2,),
)}
<p>In der Steiermark läuft die Landesförderung über den Sanierungsbonus (bis 15 Prozent der Kosten im
Sanierungskontext), viele Gemeinden zahlen zusätzlich 200 bis 1.000 Euro. Die EAG-Fördercalls 2026
laufen vom 23. April bis 11. Mai, vom 16. bis 30. Juni und ab 8. Oktober, der Antrag muss vor der
Inbetriebnahme gestellt werden. Alle Details finden Sie in den Ratgebern
{a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')},
{a('/photovoltaik-foerderung-kaernten/', 'Photovoltaik-Förderung Kärnten')} und
{a('/foerderung-fuer-pv-speicher/', 'Förderung für PV-Speicher')}.</p>
<p><small>*Beispielkonditionen nach EAG-Investitionszuschüsseverordnung 2026 und Kärntner Landesrichtlinie,
Stand Juni 2026. Der Made-in-Europe-Bonus setzt Komponenten von der White List voraus.</small></p>
{A.cta("Was kostet Ihr Dach konkret?",
       "Wir berechnen Preis, Förderung und Ersparnis für Ihr Haus und liefern den Projektbericht mit "
       "3D-Belegplan und Statikreport, kostenlos und unverbindlich.",
       secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
        ("Rechenbeispiel: Wann hat sich die Anlage bezahlt gemacht?", "rechenbeispiel", f"""
<p>Nehmen wir eine 10-kWp-Anlage mit 10 kWh Speicher in Kärnten für 18.500 Euro* vor Förderung. Nach
Abzug von 6.450 Euro Bundes- und Landesförderung bleiben 12.050 Euro Investition. Die Anlage erzeugt
rund 10.000 kWh pro Jahr. Wir rechnen mit 32 Cent je bezogener Kilowattstunde, 6 Cent Einspeisevergütung
(OeMAG-Marktpreis Juli 2026: 6,146 Cent) und 100 Euro Betriebskosten pro Jahr.</p>
{A.table(
    ["Haushalt", "Verbrauch", "Selbst genutzt", "Ersparnis + Einspeisung", "Amortisation*"],
    [
        ["Standard (4 Personen)", "4.500 kWh", "3.400 kWh (75 % Autarkie)", "1.088 € + 396 € = 1.484 €", "rund 9 Jahre"],
        ["Mit Wärmepumpe und E-Auto", "8.000 kWh", "5.600 kWh (70 % Autarkie)", "1.792 € + 264 € = 2.056 €", "rund 6 Jahre"],
    ],
    hl_cols=(4,),
)}
<p>Der Unterschied zeigt den wichtigsten Hebel: Je mehr Solarstrom Sie selbst verbrauchen, desto schneller
rechnet sich die Anlage. Wärmepumpe, Wallbox und ein {a('ems', 'Energiemanagementsystem')}, das
Verbraucher in die Sonnenstunden verschiebt, verkürzen die Amortisation deutlich. Steigende Strompreise
und Gemeindeförderungen wirken in dieselbe Richtung. In EBZ-Projekten mit hohem Eigenverbrauch liegt die
Amortisation typischerweise bei 4 bis 6 Jahren, danach produziert die Anlage noch zwei Jahrzehnte
praktisch kostenlosen Strom. Ein Beispiel aus der Praxis: Ein Hotel in Villach-Warmbad spart mit 13 kWp
und 27 kWh Speicher rund 4.200 Euro pro Jahr, Amortisation etwa 6 Jahre (siehe
{a('referenzen', 'Referenzen')}).</p>
<p><small>*Beispielrechnung mit Richtwerten, ohne Strompreissteigerung und ohne Made-in-Europe-Bonus
in der Ersparnis. Ihr Ergebnis hängt von Verbrauchsprofil, Dach und Tarif ab. Wann sich Speicher
lohnen, erklärt der Ratgeber {a('/ab-wann-lohnt-sich-photovoltaik-mit-speicher/', 'Ab wann lohnt sich Photovoltaik mit Speicher')}.</small></p>
"""),
        ("Welche Faktoren den Preis nach oben oder unten treiben", "preisfaktoren", f"""
<p>Nicht jedes Dach ist gleich, deshalb können zwei Anlagen mit identischer Leistung unterschiedlich viel
kosten. Diese Punkte beeinflussen die Kalkulation am stärksten:</p>
<ul>
  <li><b>Dachneigung und Höhe:</b> Steile oder hohe Dächer brauchen aufwendigere Gerüste und Sicherung,
  das erhöht die Arbeitszeit.</li>
  <li><b>Eindeckung:</b> Ziegel sind Standard. Bei Blechfalz, Schiefer, Eternit oder Sonderziegeln steigen
  Material- und Montagekosten.</li>
  <li><b>Kabelwege:</b> Müssen neue Kabelkanäle über mehrere Stockwerke gelegt oder Wände durchbohrt werden,
  wächst der Installationsaufwand.</li>
  <li><b>Zählerschrank:</b> Entspricht der alte Verteiler nicht den aktuellen Normen, kostet die Erneuerung oft
  über 1.000 Euro.</li>
  <li><b>Komponentenwahl:</b> Glas-Glas-Module, Notstromfunktion, Wallbox oder ein größerer Speicher erhöhen
  den Preis, bringen aber Nutzen über Jahrzehnte.</li>
  <li><b>Region:</b> Hardware-Preise schwanken global, Montagekosten sind lokal geprägt. Ein regionaler
  Fachbetrieb spart Anfahrt und ist bei Service schnell vor Ort.</li>
</ul>
<p>Planen Sie einen Puffer für Anpassungen an der Hauselektrik ein. Und vergleichen Sie Angebote nicht nur
nach dem Endpreis, sondern nach Lieferumfang, Garantien und Montagequalität: Wer bei Dachhaken und
Unterkonstruktion spart, riskiert teure Folgeschäden.</p>
"""),
        ("Laufende Kosten und Lebensdauer", "laufende-kosten", f"""
<p>Nach der Installation bleiben die Kosten überschaubar. Kalkulieren Sie 1 bis 2 Prozent der
Anschaffungskosten pro Jahr für Wartung, gelegentliche Reinigung und Rücklagen, etwa für einen
Wechselrichtertausch nach rund 15 Jahren. Eine Anlagenversicherung kostet meist unter 100 Euro im Jahr,
dazu kommt eine geringe Zählergebühr beim Netzbetreiber.</p>
{A.table(
    ["Komponente", "Lebensdauer", "Garantie bei EBZ Energie"],
    [
        ["Solarmodule", "25 bis 30 Jahre, oft länger", "bis zu 30 Jahre Leistungsgarantie"],
        ["Wechselrichter", "rund 15 Jahre", "mindestens 10 Jahre Produktgarantie"],
        ["Batteriespeicher", "10 bis 15 Jahre", "mindestens 10 Jahre Produktgarantie"],
    ],
)}
<p>Moderne Module reinigen sich bei Regen weitgehend selbst. Nur in der Nähe von Landwirtschaft oder
Industrie lohnt sich alle paar Jahre eine professionelle Reinigung.</p>
"""),
        ("Finanzierung: ab 147 Euro im Monat", "finanzierung", f"""
<p>Sie müssen die Investition nicht auf einmal stemmen. EBZ Energie bietet eine
{a('finanzierung', 'Finanzierung ab 147 Euro pro Monat')} inklusive Speicher. Die Anlage gehört Ihnen
ab dem ersten Tag, Sie erhalten die volle Förderung als Privatperson, und die Bonitätsprüfung läuft digital in Minuten, ohne Grundbucheintrag. Da die monatliche Rate in vielen Fällen unter der
bisherigen Stromrechnung liegt, sparen Sie ab dem ersten Monat.</p>
{A.cta("Preis, Förderung und Rate für Ihr Haus",
       "Wir erstellen Ihnen ein transparentes Angebot mit Projektbericht, 3D-Belegplan und Statikreport "
       "und prüfen alle Förderungen für Ihren Standort.",
       primary=("kontakt", "Jetzt Angebot anfordern"), secondary=("finanzierung", "Zur Finanzierung"))}
"""),
        ("Fazit: Solide Investition mit klarer Rechnung", "fazit", f"""
<p>Die Kosten einer Solaranlage lassen sich 2026 gut eingrenzen: 10.000 bis 15.000 Euro für 10 kWp ohne
Speicher, 15.000 bis 22.000 Euro mit Speicher, abzüglich 3.000 bis 6.500 Euro Förderung je nach
Bundesland. Entscheidend für die Wirtschaftlichkeit ist nicht der niedrigste Preis, sondern hoher
Eigenverbrauch, solide Montage und Komponenten, die 25 Jahre und länger halten. Wer beides richtig
plant, senkt seine Stromkosten um bis zu 85 Prozent und hat die Anlage in wenigen Jahren wieder
eingespielt. Was genau eine Komplettanlage umfasst, lesen Sie im Ratgeber
{a('/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/', 'Photovoltaik-Komplettanlage 10 kWp mit Speicher und Montage')}.</p>
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik mit klarem Preis: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und montiert Photovoltaikanlagen mit Speicher in Kärnten und der "
                 "Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften und über 300 "
                 "dokumentierten Projekten. Sie erhalten ein Angebot mit Projektbericht, 3D-Belegplan und "
                 "Statikreport, wir übernehmen Netzzutritt, Förderanträge und Inbetriebnahme."),
        "grid": [
            ("Transparenter Komplettpreis", "Module, Wechselrichter, Speicher, Montage, Elektro und Anmeldung in einem Angebot."),
            ("Förderung inklusive", "EAG-Antrag zum richtigen Zeitpunkt, Landes- und Gemeindeförderung geprüft."),
            ("Garantie", "Bis zu 30 Jahre Leistungsgarantie, mindestens 10 Jahre Produktgarantie."),
            ("Finanzierung", "Ab 147 Euro im Monat inklusive Speicher, Anlage ab Tag 1 Ihr Eigentum."),
        ],
    },

    "faq": [
        ("Wie hoch sind die Kosten einer Solaranlage für ein Einfamilienhaus?",
         "Für eine typische 10-kWp-Anlage ohne Speicher rechnen Sie 2026 mit rund 10.000 bis 15.000 Euro. "
         "Mit Batteriespeicher liegt der Richtpreis bei 15.000 bis 22.000 Euro vor Förderung, inklusive "
         "Montage und Anmeldung. Gerüst, Dacheindeckung und Zählerschrank beeinflussen den Preis."),
        ("Was kostet ein Speicher zusätzlich und lohnt er sich?",
         "Ein Speicher mit 5 bis 10 kWh kostet 5.000 bis 9.000 Euro Aufpreis. Er hebt den Eigenverbrauch von "
         "rund 30 auf 60 bis 80 Prozent, weil der Mittagsstrom abends genutzt wird. Da Netzstrom rund 32 Cent "
         "kostet und die Einspeisung nur 5 bis 10 Cent bringt, lohnt sich der Speicher in den meisten "
         "Haushalten, besonders mit Wärmepumpe oder E-Auto."),
        ("Wie viel Förderung gibt es 2026 für eine 10-kWp-Anlage mit Speicher?",
         "Der Bund zahlt 150 Euro je kWp und 150 Euro je kWh Speicher, für 10 kWp mit 10 kWh also 3.000 Euro, "
         "plus rund 450 Euro Made-in-Europe-Bonus bei Komponenten von der White List. In Kärnten kommen 3.000 "
         "Euro Landespauschale dazu, in Summe rund 6.450 Euro. Der EAG-Antrag muss vor Inbetriebnahme gestellt "
         "werden."),
        ("Gilt der Nullsteuersatz für Photovoltaik noch?",
         "Nein. Der Umsatzsteuersatz von 0 Prozent auf PV-Anlagen bis 35 kWp ist mit 1. April 2025 ausgelaufen, "
         "seitdem gilt wieder 20 Prozent. Als Ausgleich wurde die EAG-Investitionsförderung 2026 wieder voll "
         "aktiviert. Für Privatkunden ist die Umsatzsteuer im Angebotspreis enthalten."),
        ("Wie lange dauert es, bis sich die Solaranlage amortisiert hat?",
         "Im Rechenbeispiel mit 12.050 Euro nach Förderung braucht ein Standardhaushalt rund 9 Jahre, ein "
         "Haushalt mit Wärmepumpe und E-Auto rund 6 Jahre. In EBZ-Projekten mit hohem Eigenverbrauch liegt "
         "die Amortisation typischerweise bei 4 bis 6 Jahren. Danach liefern die Module noch rund 20 Jahre "
         "nahezu kostenlosen Strom."),
        ("Welche laufenden Kosten kommen nach der Installation auf mich zu?",
         "Rechnen Sie mit 1 bis 2 Prozent der Anschaffungskosten pro Jahr für Wartung, Reinigung und "
         "Rücklagen, etwa für den Wechselrichtertausch nach rund 15 Jahren. Eine Versicherung kostet meist "
         "unter 100 Euro jährlich, dazu kommt eine geringe Zählergebühr des Netzbetreibers."),
        ("Sind die Preise für PV-Anlagen gesunken?",
         "Ja. Nach den Lieferengpässen und Preisspitzen der Jahre 2022 und 2023 haben sich Module und "
         "Wechselrichter wieder auf einem moderaten Niveau eingependelt. Die Umsatzsteuer gilt zwar seit "
         "April 2025 wieder, dafür senkt die Förderung 2026 den Preis einer 10-kWp-Anlage mit Speicher "
         "um 3.000 bis 6.500 Euro."),
        ("Kann ich die Anlage finanzieren, statt sie zu kaufen?",
         "Ja. EBZ Energie bietet eine Finanzierung ab 147 Euro im Monat inklusive Speicher. Die Anlage gehört "
         "Ihnen ab dem ersten Tag, Sie erhalten die volle private Förderung, die Bonitätsprüfung läuft digital in Minuten, ohne Grundbucheintrag. Die Rate liegt oft unter der bisherigen "
         "Stromrechnung."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team hat über 300 "
                    "Photovoltaikanlagen mit Speicher in Kärnten und der Steiermark geplant und montiert. "
                    "Die Preise in diesem Ratgeber sind Richtwerte aus der laufenden Angebotspraxis und werden "
                    "regelmäßig aktualisiert. Keine Rechts- oder Steuerberatung, maßgeblich sind die jeweils "
                    "gültigen Förderrichtlinien."),
    "sources": [
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("OeMAG: Marktpreis für Photovoltaik", "https://www.oemag.at/"),
        ("Förderportal des Landes Kärnten", "https://www.ktn.gv.at/"),
    ],
    "related": [
        ("/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/", "Komplettanlage 10 kWp mit Speicher und Montage"),
        ("/photovoltaik-foerderung-oesterreich-2026/", "Photovoltaik-Förderung Österreich 2026"),
        ("/ab-wann-lohnt-sich-photovoltaik-mit-speicher/", "Ab wann lohnt sich Photovoltaik mit Speicher?"),
        ("finanzierung", "Finanzierung ab 147 € im Monat"),
    ],
    "cta": {
        "h3": "Ihr Preis in 48 Stunden",
        "text": "Kostenloses Angebot mit Projektbericht, 3D-Belegplan und Statikreport für Ihr Dach.",
        "primary": ("kontakt", "Angebot anfordern"),
    },
    "final_h2": "Sprechen wir über Ihre Anlage",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
