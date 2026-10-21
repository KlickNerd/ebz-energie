"""Ads-Landingpage Waermepumpe + Photovoltaik (alte WP-Seite /waermepumpe-photovoltaik-oesterreich/, Stand Mai 2026).

Botschaft der alten LP uebernommen (Heizen mit eigenem Sonnenstrom, zwei Rechnungen mit einer Entscheidung loesen,
PV + Waermepumpe + Speicher aus einer Hand, Foerderabwicklung fuer beide Systeme, Finanzierung). Korrigiert:
"bis zu 90 %" -> bis zu 85 %; "bis zu 80 % Autarkie" -> Eigenverbrauch bis zu 80 % mit Speicher; "doppelte
Foerderung von Bund und Laendern" -> Foerderstand wird geprueft, keine Betraege; Ertragsprognose -> Projektbericht
mit 3D-Belegplan und Statikreport; eigene Montageteams/Techniker -> zertifizierte Fachkraefte; Leasing/ab 49 €/
keine Bonitaetspruefung/24 Stunden/KSV/Servicevertrag -> Finanzierung ab 147 €* inkl. Speicher (finance_band);
"100 Anlagen pro Jahr" -> 300+ Projekte; "ganz Oesterreich" als Montagegebiet -> Kaernten und Steiermark;
Widmanngasse -> Triglavstrasse 15 (kommt aus NAP). Zahlen aus build/pages/waermepumpe.py und dem Muster.
"""

LP = {
    "path": "/waermepumpe-photovoltaik-oesterreich/",
    "title": "Wärmepumpe und Photovoltaik kombinieren | EBZ Energie",
    "description": ("Wärmepumpe und PV-Anlage aus einer Hand: Heizen mit eigenem Sonnenstrom, bis zu 85 % weniger "
                    "Energiekosten, Förderabwicklung inklusive. 4,9 Sterne."),
    "eyebrow": "Bis zu 85 % Energiekosten sparen",
    "h1": "Wärmepumpe und Photovoltaik kombinieren: heizen mit eigenem Sonnenstrom",
    "lead": ("Ihre PV-Anlage produziert den Strom, Ihre Wärmepumpe macht daraus Heizung und Warmwasser. So senken Sie "
             "Ihre Energiekosten um bis zu 85 %. EBZ Energie übernimmt Planung, Montage und den kompletten Papierkram: "
             "schlüsselfertig aus einer Hand, inklusive Förderabwicklung."),
    "badges": [("bis zu 85 %", "weniger Energiekosten"), ("1 Ansprechpartner", "für PV und Wärmepumpe"), ("300+", "Projekte")],
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit Photovoltaikanlage auf dem Dach vor einer Bergkulisse",
    "problem": {
        "eyebrow": "Das Problem",
        "h2": "Strom und Heizung: zwei Rechnungen, die jedes Jahr mehr werden",
        "paragraphs": [
            ("Die Strompreise steigen, die Heizkosten steigen. Diese doppelte Abhängigkeit vom Strommarkt und vom "
             "Heizungsmarkt kostet Sie Jahr für Jahr viel Geld."),
            ("Dabei lösen Sie beides mit einer Entscheidung: Die Photovoltaikanlage auf dem Dach liefert den Strom, die "
             "Wärmepumpe macht aus 1 kWh Strom 4 bis 5 kWh Wärme für Heizung und Warmwasser. Eigener Solarstrom kostet "
             "10 bis 14 Cent je kWh, Netzstrom das Zwei- bis Dreifache.*"),
        ],
    },
    "benefits": {
        "eyebrow": "Ihre Vorteile",
        "h2": "Zwei Technologien, die füreinander gemacht sind",
        "intro": "Wir planen PV-Anlage, Speicher und Wärmepumpe als ein System, passend zu Ihrem Haus und Ihrem Verbrauch.",
        "cards": [
            ("€", "Strom- und Heizkosten sinken gleichzeitig",
             "Nicht nur eine Rechnung wird kleiner, sondern beide. Mit PV-Anlage und Speicher sinken die Heizkosten im Beispielhaus auf 200 bis 500 € im Jahr.*"),
            ("▮", "Mehr Unabhängigkeit mit Speicher",
             "Mit einem Batteriespeicher steigt Ihr Eigenverbrauch auf bis zu 80 %. Sie nutzen Ihren Sonnenstrom auch abends und nachts."),
            ("✓", "Förderabwicklung für beide Systeme",
             "Wir prüfen den aktuellen Förderstand für PV-Anlage und Wärmepumpe und übernehmen die Anträge. Sie müssen sich um nichts kümmern."),
            ("⌂", "Mehr Wert für Ihre Immobilie",
             "Ein Haus, das sich weitgehend selbst mit Strom und Wärme versorgt, ist am Markt attraktiver."),
        ],
    },
    "quote": ("Von der kostenlosen Besichtigung vor Ort über die Förderabwicklung bis zur fertigen Installation von "
              "Photovoltaik und Wärmepumpe: Wir setzen Ihr Projekt schlüsselfertig für Sie um."),
    "steps": {
        "eyebrow": "So einfach geht es",
        "h2": "In 4 Schritten zu Photovoltaik und Wärmepumpe",
        "steps": [
            ("Kostenlose Beratung", "Wir analysieren Ihren Strom- und Wärmebedarf und zeigen Ihnen ehrlich, wie Sie am meisten sparen, ohne Verkaufsdruck.", "Tag 1"),
            ("Planung vor Ort", "Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport, die Heizlastberechnung und ein transparentes Gesamtangebot.", "ca. 1 Woche"),
            ("Förderung und Anmeldung", "Wir stellen die Förderanträge, übernehmen die Behördenwege und melden die PV-Anlage beim Netzbetreiber an.", "parallel"),
            ("Montage und Übergabe", "Zertifizierte Fachkräfte montieren PV-Anlage und Wärmepumpe. Bei der Übergabe erklären wir Ihnen alles.", "wenige Tage"),
        ],
    },
    "why": {
        "items": [
            ("☀", "PV und Wärmepumpe aus einer Hand", "Planung, Montage, Förderabwicklung und Netzanmeldung. Ein Ansprechpartner von der Planung bis zur Übergabe."),
            ("✓", "Zertifizierte Fachkräfte", "Meisterhaftes Handwerk und sorgfältige Ausführung nach österreichischen Normen."),
            ("★", "4,9 Sterne auf Google", "Bewertungen von echten Kundinnen und Kunden aus der Region."),
            ("◉", "300+ Projekte", "Erfahrung aus über 300 dokumentierten Projekten in 6 Bundesländern."),
            ("◇", "Bis zu 30 Jahre Garantie", "Bis zu 30 Jahre Leistungsgarantie auf die Module, mindestens 10 Jahre Produktgarantie."),
            ("⌂", "Regional verwurzelt", "Zuhause in Villach, im Einsatz in Kärnten und der Steiermark."),
        ],
    },
    "finance": True,
    "refs": ["villach", "krumpendorf"],
    "contact": {
        "h2": "Jetzt unverbindlich anfragen",
        "sub": "Sagen Sie uns kurz, wie Sie heute heizen und wie viel Strom Sie brauchen. Wir melden uns innerhalb eines Werktags.",
    },
    "faq": [
        ("Ist mein Haus für eine Wärmepumpe geeignet?",
         "Meistens ja, auch ältere Häuser ohne Fußbodenheizung. Bis 55 Grad Vorlauf arbeitet eine moderne Wärmepumpe "
         "effizient. Wir prüfen Ihr Gebäude kostenlos vor Ort und sagen Ihnen ehrlich, was Sinn ergibt."),
        ("Funktioniert die Wärmepumpe auch im Winter zuverlässig?",
         "Ja. Moderne Luft-Wasser-Wärmepumpen arbeiten bis minus 20 Grad Außentemperatur. Im Winter liefert die "
         "PV-Anlage weniger, dann kommt der Reststrom aus dem Netz."),
        ("Lohnt sich die Kombination aus PV und Wärmepumpe?",
         "Ja. Eigener Solarstrom kostet 10 bis 14 Cent je kWh, Netzstrom das Zwei- bis Dreifache. Mit PV-Anlage und "
         "Speicher sinken die Heizkosten im Beispielhaus auf 200 bis 500 € im Jahr.*"),
        ("Wie groß muss die PV-Anlage für eine Wärmepumpe sein?",
         "Für Haushalt und Wärmepumpe planen wir meist 10 bis 15 kWp mit einem Speicher von 10 bis 12 kWh. Die genaue "
         "Größe richtet sich nach Ihrem Verbrauch und Ihrem Dach."),
        ("Was kostet das kombinierte System?",
         "Als Richtwert kostet eine PV-Anlage mit 10 kWp und Speicher rund 15.000 bis 22.000 €, eine Luft-Wasser-Wärmepumpe "
         "inklusive Montage rund 12.000 bis 22.000 €, jeweils vor Förderung.* Sie erhalten ein Festpreisangebot ohne "
         "versteckte Kosten. Mit unserer Finanzierung gehört die PV-Anlage ab dem ersten Tag Ihnen, ab 147 € im Monat "
         "inklusive Speicher.*"),
        ("Welche Förderung bekomme ich?",
         "PV-Anlage und Wärmepumpe werden getrennt gefördert, abhängig von Bundesland und Projekt, und die Förderlage "
         "ändert sich derzeit laufend. Wir prüfen den aktuellen Förderstand für Ihr Projekt und übernehmen die Anträge."),
        ("Was passiert nach der Installation?",
         "Wir bleiben Ihr Ansprechpartner für Service und Fragen, erreichbar Montag bis Freitag von 10 bis 20 Uhr. Die "
         "Betreuung endet bei uns nicht mit der Inbetriebnahme."),
    ],
    "finalcta": {
        "h2": "Wie lange wollen Sie noch zwei Energierechnungen zahlen?",
        "text": "Der erste Schritt ist ein kostenloses Gespräch. Wir melden uns innerhalb eines Werktags.",
    },
    "footnote": ("*Richtwerte und Beispielkonditionen, Stand Oktober 2026, abhängig von Gebäude, Verbrauch, Anlagengröße, "
                 "Dach und Laufzeit. Alle Preise vor Förderung. Verbindlich ist Ihr persönliches Angebot."),
}
