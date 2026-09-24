"""Ratgeber: Photovoltaik für die Wärmepumpe (Synergie, Planung, Speicher, EMS, Kosten).

Migriert von ebz-photovoltaik.at/photovoltaik-fuer-waermepumpe/ (Stand November 2025).
Bereinigt: deutsche KfW-Kredite durch EBZ-Finanzierung ersetzt, unbelegte
"bis zu 70 % Förderung" entfernt, PV-Preis auf den freigegebenen Richtpreis
(10 kWp mit Speicher rund 15.000 bis 22.000 €) gesetzt, Marketing-Floskeln gekürzt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "photovoltaik-fuer-waermepumpe",
    "path": "/photovoltaik-fuer-waermepumpe/",
    "title": "Photovoltaik für die Wärmepumpe: Heizen mit Solarstrom | EBZ",
    "description": ("Photovoltaik für die Wärmepumpe: Solarstrom für 10 bis 14 ct/kWh statt Netzstrom, "
                    "Eigenverbrauch bis 80 % mit Speicher, 50 bis 70 % weniger Energiekosten."),
    "eyebrow": "Photovoltaik · Wärmepumpe",
    "crumb_label": "Photovoltaik für die Wärmepumpe",
    "h1": "Photovoltaik für die Wärmepumpe: Heizen mit Solarstrom für 10 bis 14 Cent je Kilowattstunde",
    "lead": ("Die Wärmepumpe ist der größte Stromverbraucher im Haus, die PV-Anlage liefert genau diesen "
             "Strom zu Gestehungskosten von 10 bis 14 Cent statt dem Zwei- bis Dreifachen aus dem Netz. "
             "Dieser Ratgeber zeigt, wie Sie PV-Anlage, Speicher, Energiemanagement und Wärmepumpe richtig "
             "dimensionieren, was das System kostet und wie es gefördert wird."),
    "chips": [
        "Solarstrom: <b>10 bis 14 ct/kWh</b>*",
        "Eigenverbrauch: <b>bis 80 %</b> mit Speicher",
        "PV-Leistung: <b>10 bis 15 kWp</b>",
        "Energiekosten: <b>50 bis 70 %</b> weniger*",
    ],
    "date_published": "2025-07-20",
    "date_modified": "2026-09-24",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit Photovoltaikanlage auf dem Dach und Wärmepumpe im Garten",

    "tldr": [
        "Selbst erzeugter Solarstrom kostet meist 10 bis 14 Cent pro Kilowattstunde, Netzstrom das Zwei- "
        "bis Dreifache. Jede Kilowattstunde, die die Wärmepumpe vom Dach bezieht, spart diese Differenz.",
        "Empfohlene PV-Leistung mit Wärmepumpe: 10 bis 15 kWp. Ein Speicher mit dem 1- bis 1,5-fachen der "
        "kWp-Zahl in kWh (10 bis 12 kWh bei 10 kWp) hebt den Eigenverbrauch von rund 30 auf 70 bis 80 %.",
        "Ein Energiemanagementsystem mit SG-Ready-Schnittstelle lädt bei PV-Überschuss Puffer- und "
        "Warmwasserspeicher auf höhere Temperaturen und speichert Sonnenenergie so als Wärme.",
        "Kosten: Wärmepumpe 15.000 bis 30.000 Euro, PV-Anlage mit 10 kWp und Speicher rund 15.000 bis "
        "22.000 Euro, jeweils vor Förderung. Beide Systeme werden separat gefördert.",
        "Die Kombination senkt die jährlichen Energiekosten für Heizung, Warmwasser und Haushalt um 50 bis "
        "70 Prozent, das Gesamtsystem amortisiert sich in rund 12 bis 16 Jahren.",
    ],
    "kpis": [
        ("10 bis 15 kWp", "empfohlene PV-Leistung mit Wärmepumpe"),
        ("10 bis 12 kWh", "Speicher für eine 10-kWp-Anlage"),
        ("12 bis 16 Jahre", "Amortisation des Gesamtsystems*"),
        ("15.000 bis 22.000 €", "10 kWp mit Speicher vor Förderung*"),
    ],

    "sections": [
        ("Warum Photovoltaik und Wärmepumpe zusammenpassen", "synergie", f"""
<p>Eine Wärmepumpe bezieht den Großteil ihrer Energie aus Luft, Erdreich oder Grundwasser. Für
Kompressor und Pumpen braucht sie aber Strom, und der ist aus dem Netz teuer. Genau hier setzt die
Photovoltaikanlage an: Sie produziert auf dem Dach sauberen Strom, den die Wärmepumpe direkt nutzt.
Die Betriebskosten der Heizung sinken auf ein Minimum.</p>
{A.net([
    ("☀", "PV-Anlage", "erzeugt tagsüber Solarstrom, 10 bis 15 kWp empfohlen"),
    ("♨", "Wärmepumpe", "heizt, bereitet Warmwasser und kühlt im Sommer"),
    ("▮", "Batteriespeicher", "hält Überschuss für Abend und Nacht bereit"),
    ("⌖", "Wallbox (optional)", "lädt das E-Auto mit dem restlichen Überschuss"),
], "Energiemanagement als Schaltzentrale",
   "Das EMS stimmt Erzeugung und Verbrauch aufeinander ab und lädt bei Überschuss den Wärmespeicher.")}
<h3>So ergänzen sich beide Systeme über das Jahr</h3>
<ul>
  <li><b>Sommer:</b> Die PV-Anlage produziert am meisten. Der Überschuss deckt den Haushalt und die
  Warmwasserbereitung der Wärmepumpe. Viele Wärmepumpen kühlen im Sommer auch, ebenfalls mit eigenem
  Solarstrom.</li>
  <li><b>Winter:</b> Der Heizbedarf ist am höchsten, die PV-Anlage liefert weniger, aber an sonnigen
  Tagen genug für die Grundlast der Wärmepumpe. Das reduziert den teuren Netzbezug.</li>
  <li><b>Übergangszeit:</b> Eine ausreichend große Anlage deckt in Frühjahr und Herbst einen
  erheblichen Teil des Wärmepumpenstroms.</li>
</ul>
<p>Wie die Wärmepumpe technisch aus Strom Wärme macht, erklärt der Ratgeber
{a('/funktionsweise-einer-waermepumpe/', 'Funktionsweise einer Wärmepumpe')}.</p>
"""),
        ("Die finanziellen Vorteile: Solarstrom statt Netzstrom", "einsparung", f"""
<p>Die Betriebskosten einer Wärmepumpe bestehen fast nur aus Stromkosten. Mit eigener PV-Anlage
ändern sich die Spielregeln: Die Gestehungskosten für selbst erzeugten Solarstrom liegen meist bei 10
bis 14 Cent pro Kilowattstunde, Netzstrom kostet oft das Zwei- bis Dreifache. Jede Kilowattstunde vom
Dach spart diese Differenz, über die Jahre summiert sich das auf erhebliche Beträge.</p>
<p>Die Amortisation des Gesamtsystems aus PV-Anlage, Speicher und Wärmepumpe stützt sich auf drei
Säulen:</p>
<ol>
  <li><b>Direkte Einsparung</b> bei Strom- und Heizkosten ab der Inbetriebnahme, in Summe 50 bis
  70 Prozent der jährlichen Energiekosten für Heizung, Warmwasser und Haushalt.</li>
  <li><b>Förderungen</b> für Heizungstausch und Photovoltaik, die die Anschaffung deutlich senken.</li>
  <li><b>Einspeisevergütung</b> für überschüssigen Strom, den Sie nicht selbst verbrauchen (siehe
  {a('marktpreis', 'OeMAG-Marktpreis 2026')}).</li>
</ol>
<p>So amortisiert sich die Investition oft nach 12 bis 16 Jahren, danach heizen Sie für viele weitere
Jahre nahezu kostenlos. Dazu kommt die Preissicherheit: Ihr Solarstrom hat für die nächsten 25 bis 30
Jahre stabile, niedrige Kosten, unabhängig von Netzstrompreisen und fossilen Energieträgern.</p>
<p><small>*Richtwerte. Gestehungskosten, Einsparung und Amortisation hängen von Anlagengröße,
Verbrauchsprofil, Stromtarif und Förderung ab.</small></p>
"""),
        ("Planung und Dimensionierung: PV-Anlage und Wärmepumpe aufeinander abstimmen", "planung", f"""
<p>Eine unterdimensionierte PV-Anlage liefert nicht genug Strom für die Wärmepumpe, eine
überdimensionierte verursacht unnötige Kosten. Ebenso muss die Wärmepumpe exakt zum Wärmebedarf des
Gebäudes passen. Deshalb gehört an den Anfang eine Analyse von Dachfläche und Ausrichtung, Dämmstandard,
Jahresstromverbrauch und Heizbedarf.</p>
<h3>PV-Anlage: 10 bis 15 kWp</h3>
<p>Für die Kombination mit Wärmepumpe gilt: eher größer planen. Eine Anlage mit 10 bis 15 kWp deckt
in einem typischen Einfamilienhaus nicht nur den Großteil des Haushaltsstroms, sondern auch einen
signifikanten Teil des Wärmepumpenstroms, selbst in den Übergangsmonaten. Weil Gerüst, Montage und
Wechselrichter ohnehin anfallen, senken zusätzliche Module die Kosten pro kWp und die größere Anlage
amortisiert sich oft schneller.</p>
<h3>Wärmepumpe: nach Heizlastberechnung</h3>
<p>Die Heizleistung wird über eine Heizlastberechnung ermittelt. Eine zu kleine Wärmepumpe muss an sehr
kalten Tagen auf den elektrischen Heizstab zurückgreifen, was die Betriebskosten in die Höhe treibt. Eine
zu große taktet zu häufig, das verkürzt die Lebensdauer und senkt die Effizienz. Nur eine passend
ausgelegte Wärmepumpe arbeitet im optimalen Bereich.</p>
{A.box("Wer eine Wärmepumpe plant, sollte die PV-Anlage gleich mitplanen. Nur so lassen sich "
       "Anlagengröße, Speicher und Energiemanagement auf den tatsächlichen Strombedarf der Heizung "
       "abstimmen. EBZ Energie liefert dafür einen Projektbericht mit 3D-Belegplan und Statikreport.")}
{A.cta("PV-Anlage und Wärmepumpe gemeinsam planen",
       "Wir analysieren Dach, Wärmebedarf und Stromverbrauch kostenlos vor Ort und dimensionieren beide "
       "Systeme als Gesamtpaket.",
       secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
        ("Der Stromspeicher: Eigenverbrauch von 30 auf bis zu 80 Prozent", "speicher", f"""
<p>Die PV-Anlage produziert mittags am meisten, der höchste Bedarf für Haushalt und Heizung fällt aber
morgens und abends an. Ohne Speicher müsste der Überschuss für eine geringe Vergütung eingespeist und
abends teuer zurückgekauft werden. Ein {a('batteriespeicher', 'Batteriespeicher')} löst das: Er
speichert den Solarstrom vom Tag und gibt ihn abends und nachts an Wärmepumpe und Haushalt ab.</p>
{A.table(
    ["Kennzahl", "Richtwert*"],
    [
        ["Eigenverbrauchsquote ohne Speicher", "ca. 30 %"],
        ["Eigenverbrauchsquote mit Speicher", "70 bis 80 %"],
        ["Faustregel Speichergröße", "1- bis 1,5-faches der PV-Leistung (kWp) in kWh"],
        ["Beispiel 10-kWp-Anlage", "10 bis 12 kWh Speicher"],
        ["Lebensdauer Lithium-Speicher", "15 bis 20 Jahre bzw. 8.000 bis 10.000 Ladezyklen"],
    ],
    hl_cols=(1,),
)}
<p>Jede selbst verbrauchte Kilowattstunde aus dem Speicher ist eine gesparte Kilowattstunde aus dem
Netz. Ein notstromfähiger Speicher hält zudem die Wärmepumpe bei einem Netzausfall in Betrieb.</p>
<p><small>*Richtwerte. Die passende Speichergröße hängt von nächtlichem Verbrauch, PV-Leistung und
Wärmepumpenbedarf ab.</small></p>
"""),
        ("Energiemanagement und SG Ready: Sonnenenergie als Wärme speichern", "energiemanagement", f"""
<p>Das beste System ist nur so gut wie seine Steuerung. Ein {a('ems', 'Energiemanagementsystem (EMS)')}
verbindet PV-Anlage, Speicher, Wärmepumpe und auf Wunsch die Wallbox. Anhand von Wetterprognosen und
Ihren Verbrauchsmustern weiß es, wann wie viel Solarstrom verfügbar ist und welcher Verbraucher wann
laufen sollte, um den Eigenverbrauch zu maximieren.</p>
<p>Zentral ist die <b>SG-Ready-Schnittstelle</b> (Smart Grid Ready) der Wärmepumpe. Über sie gibt das
EMS der Wärmepumpe gezielte Befehle: Erkennt es einen großen PV-Überschuss, lädt die Wärmepumpe den
Pufferspeicher der Heizung oder den Warmwasserspeicher auf eine höhere Temperatur als üblich.
Überschüssiger Strom wird so in Wärme umgewandelt und für später gespeichert, auch wenn die Sonne
nicht mehr scheint. Keine Kilowattstunde geht verloren.</p>
{A.box("Der Klima- und Energiefonds fördert Energiemanagementsysteme, die mindestens zwei Komponenten "
       "wie PV-Anlage und Wärmepumpe aktiv steuern, für Haushalte mit 50 Prozent bis 600 Euro. Details "
       "und Fristen: " + a('/ems-foerderung/', 'EMS-Förderung 2026') + ".", label="Förderung:")}
"""),
        ("Kosten, Förderung und Finanzierung im Überblick", "kosten", f"""
<p>Die Anfangsinvestition wirkt auf den ersten Blick hoch, muss aber im Kontext der langfristigen
Einsparungen und der Zuschüsse gesehen werden. Die Kostenblöcke für ein Einfamilienhaus:</p>
{A.table(
    ["Komponente", "Richtwert vor Förderung*", "Anmerkung"],
    [
        ["Wärmepumpe inkl. Installation", "15.000 bis 30.000 €", "je nach Wärmequelle (Luft, Erde, Wasser) und Leistung"],
        ["PV-Anlage 10 kWp inkl. Speicher", "rund 15.000 bis 22.000 €", "ideale Größe für die Kombination mit Wärmepumpe"],
        ["Energiemanagementsystem", "je nach System", "förderfähig über den Klima- und Energiefonds"],
    ],
    hl_cols=(1,),
)}
<h3>Förderung: zwei Systeme, zwei Programme</h3>
<ul>
  <li><b>Wärmepumpe:</b> Der Tausch einer fossilen Heizung wird über die Bundesförderung „Raus aus Öl
  und Gas“ und die Landesprogramme gefördert. Überblick:
  {a('/waermepumpenfoerderung-in-oesterreich/', 'Wärmepumpenförderung in Österreich')} und
  {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive 2026')}.</li>
  <li><b>Photovoltaik und Speicher:</b> Bundesweit über den EAG-Investitionszuschuss, dazu
  Landesförderungen: {a('foerderung_kaernten', 'Photovoltaik-Förderung Kärnten')},
  {a('foerderung_steiermark', 'Photovoltaik-Förderung Steiermark')},
  {a('foerderung_at', 'Photovoltaik-Förderung Österreich')}.</li>
</ul>
<h3>Finanzierung statt Eigenkapital</h3>
<p>Wer nicht die gesamte Summe auf einmal aufbringen möchte, kann die Anlage über EBZ Energie
{a('finanzierung', 'finanzieren')}: ab 147 Euro pro Monat inklusive Speicher. Die Anlage gehört ab dem
ersten Tag Ihnen, die volle Förderung bleibt bei Ihnen, ohne strenge Bonitätsprüfung und ohne
Datenbankeintrag.</p>
<p>Unterm Strich senkt die Kombination die jährlichen Energiekosten für Heizung, Warmwasser und
Haushalt um 50 bis 70 Prozent, je nach bisherigem Verbrauch mehrere tausend Euro pro Jahr. Alle
Wärmepumpen-Kostenblöcke im Detail: {a('/kosten-einer-waermepumpe/', 'Kosten einer Wärmepumpe 2026')}.</p>
<p><small>*Richtwerte vor Abzug von Förderungen. Die tatsächlichen Kosten hängen von Gebäude,
Wärmequelle, Dachfläche und Komponentenwahl ab.</small></p>
"""),
        ("Winterbetrieb und Nachrüstung: Was in der Praxis wichtig ist", "praxis", f"""
<h3>Was passiert im Winter?</h3>
<p>Im Winter produziert die PV-Anlage weniger, an sonnigen Tagen reicht es aber oft für die Grundlast
der Wärmepumpe. An trüben Tagen oder bei sehr tiefen Temperaturen kommt zusätzlicher Strom aus dem
Netz. Dafür gibt es spezielle, oft günstigere Wärmepumpen-Stromtarife. Ein gut dimensioniertes System
mit Speicher hält den Netzbezug auch im Winter so gering wie möglich.</p>
<h3>Bestehende PV-Anlage mit neuer Wärmepumpe kombinieren</h3>
<p>Das ist in den meisten Fällen problemlos möglich. Zu prüfen sind die Leistung der bestehenden Anlage
und die Kompatibilität der Komponenten, etwa des Wechselrichters. Oft lohnt es sich, im Zuge der
Nachrüstung einen Speicher und ein Energiemanagement zu ergänzen, um den Eigenverbrauch zu
maximieren.</p>
<h3>Photovoltaik für die Wärmepumpe im Altbau</h3>
<p>Gerade im sanierten Altbau mit gutem Dämmstandard spielt die Wärmepumpe ihre Effizienz aus, und die
PV-Anlage deckt den dann höheren Strombedarf der Heizung mit günstigem Eigenstrom. Voraussetzung sind
eine professionelle Gebäudeanalyse und die richtige Dimensionierung. Mehr dazu:
{a('/waermepumpe-im-altbau/', 'Wärmepumpe im Altbau')}.</p>
"""),
        ("Fazit: Zukunftssicher heizen und unabhängig werden", "fazit", f"""
<p>Die Kombination aus Photovoltaik und Wärmepumpe löst Sie von fossilen Brennstoffen und
unkalkulierbaren Energiepreisen. Sie setzen auf zwei kostenlose Quellen, die Wärme der Umwelt und die
Kraft der Sonne, und sichern sich für Jahrzehnte niedrige, planbare Energiekosten. Mit Speicher und
Energiemanagement werden Sie zu Ihrem eigenen Energieversorger für Heizung, Warmwasser, Haushalt und
auf Wunsch das E-Auto. Die Förderungen für beide Systeme machen die Investition auch wirtschaftlich
zu einer klaren Entscheidung.</p>
{A.cta("Jetzt Gesamtkonzept anfragen",
       "Kostenlose Vor-Ort-Analyse, Projektbericht mit 3D-Belegplan und Statikreport, Förderabwicklung "
       "für PV und Wärmepumpe aus einer Hand.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Wärmepumpe: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und "
                 "Energiemanagement in Kärnten und der Steiermark, mit einem festangestellten Team aus "
                 "zertifizierten Fachkräften und 300+ dokumentierten Projekten. Sie erhalten ein Gesamtkonzept "
                 "aus einer Hand: Analyse vor Ort, Projektbericht mit 3D-Belegplan und Statikreport, "
                 "Förderabwicklung für beide Systeme, Montage und Service danach."),
        "grid": [
            ("Gesamtkonzept statt Einzelteile", "PV-Anlage, Speicher, EMS und Wärmepumpe aufeinander abgestimmt."),
            ("Förderung für beide Systeme", "Heizungstausch und EAG-Zuschuss: wir reichen alles ein."),
            ("Bis zu 30 Jahre Leistungsgarantie", "Komponenten führender Hersteller, mind. 10 Jahre Produktgarantie."),
            ("Finanzierung ab 147 €/Monat", "Inklusive Speicher, Anlage gehört ab Tag 1 Ihnen."),
        ],
    },

    "faq": [
        ("Lohnt sich Photovoltaik für die Wärmepumpe auch im Altbau?",
         "Ja. Im sanierten Altbau mit gutem Dämmstandard arbeitet die Wärmepumpe effizient, und die "
         "PV-Anlage deckt den höheren Strombedarf der Heizung mit Eigenstrom für 10 bis 14 Cent je "
         "Kilowattstunde. Entscheidend sind eine Gebäudeanalyse und die richtige Dimensionierung."),
        ("Wie groß sollte der Stromspeicher sein?",
         "Als Faustregel entspricht die Speicherkapazität in kWh dem 1- bis 1,5-fachen der PV-Leistung in "
         "kWp. Für ein Einfamilienhaus mit 10-kWp-Anlage sind 10 bis 12 kWh meist eine gute Wahl, um eine "
         "Eigenverbrauchsquote von über 70 Prozent zu erreichen."),
        ("Wie groß sollte die PV-Anlage für eine Wärmepumpe sein?",
         "Für die Kombination empfehlen sich 10 bis 15 kWp. Eine Wärmepumpe verbraucht 3.000 bis 5.000 kWh "
         "Strom pro Jahr, dazu kommt der Haushalt. Eine größere Anlage senkt die Kosten pro kWp und deckt "
         "auch in den Übergangsmonaten einen relevanten Teil des Heizstroms."),
        ("Was passiert im Winter, wenn die Sonne kaum scheint?",
         "An sonnigen Wintertagen deckt die PV-Anlage oft die Grundlast der Wärmepumpe, an trüben Tagen "
         "kommt Strom aus dem Netz, idealerweise über einen günstigeren Wärmepumpen-Stromtarif. Speicher "
         "und Energiemanagement halten den Netzbezug so gering wie möglich."),
        ("Kann ich eine bestehende PV-Anlage mit einer neuen Wärmepumpe kombinieren?",
         "Ja, in den meisten Fällen problemlos. Geprüft werden Leistung der Anlage und Kompatibilität der "
         "Komponenten wie Wechselrichter. Oft ist es sinnvoll, dabei einen Speicher und ein "
         "Energiemanagement nachzurüsten."),
        ("Wie lange hält eine solche Anlage?",
         "PV-Module halten 30 Jahre und mehr, EBZ Energie gibt bis zu 30 Jahre Leistungsgarantie. "
         "Hochwertige Wärmepumpen sind für 15 bis 20 Jahre Betrieb ausgelegt, Lithium-Speicher für 15 bis "
         "20 Jahre beziehungsweise 8.000 bis 10.000 Ladezyklen."),
        ("Was ist SG Ready und warum ist es wichtig?",
         "SG Ready (Smart Grid Ready) ist eine Schnittstelle der Wärmepumpe, über die ein "
         "Energiemanagementsystem sie steuern kann. Bei PV-Überschuss lädt die Wärmepumpe dann Puffer- oder "
         "Warmwasserspeicher auf höhere Temperaturen und speichert Sonnenenergie als Wärme."),
        ("Werden PV-Anlage und Wärmepumpe getrennt gefördert?",
         "Ja. Die Wärmepumpe wird über die Bundesförderung für den Heizungstausch und die Landesprogramme "
         "gefördert, die PV-Anlage mit Speicher über den EAG-Investitionszuschuss und Landesförderungen. "
         "EBZ Energie wickelt beide Anträge ab."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "PV-Anlagen, Speicher, Wärmepumpen und Energiemanagementsysteme in Kärnten und der "
                    "Steiermark und übernimmt die Förderabwicklung für beide Systeme. Alle Kosten- und "
                    "Einsparangaben sind Richtwerte aus der Projektpraxis. Keine Rechts- oder Steuerberatung, "
                    "maßgeblich sind die offiziellen Förderbedingungen."),
    "related": [
        ("photovoltaik", "Photovoltaik-Anlagen von EBZ Energie"),
        ("waermepumpe", "Wärmepumpen-Installateur in Kärnten und Steiermark"),
        ("batteriespeicher", "Batteriespeicher: Solarstrom rund um die Uhr"),
        ("/kosten-einer-waermepumpe/", "Kosten einer Wärmepumpe 2026"),
    ],
    "cta": {
        "h3": "PV und Wärmepumpe aus einer Hand",
        "text": "Kostenlose Vor-Ort-Analyse, Gesamtkonzept und Förderabwicklung für beide Systeme.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Heizen mit der Kraft der Sonne",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Photovoltaik, "
                   "Speicher und Wärmepumpe als Gesamtsystem plant und montiert."),
}
