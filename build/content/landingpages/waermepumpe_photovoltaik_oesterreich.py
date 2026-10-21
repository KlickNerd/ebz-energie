"""Ads-Landingpage Waermepumpe + Photovoltaik (alte WP-Seite /waermepumpe-photovoltaik-oesterreich/, Stand Mai 2026).

Aufbau wie das Muster /photovoltaik-privat-lp/ und wie die alte LP: Hero auf Foto (Alpenhaus), Bewertungen,
Problem mit Bild (Haus mit Waermepumpe) und 4 Punkten, "So funktioniert die Kombination" mit der freigegebenen
Grafik GRAFIK_WP_PV, Vorteils-Karten, Mario-Zitat mit Button, 4 Schritte auf Foto, Warum EBZ, Finanzierung mit
Bild, Galerie 2023, Schluss-Aufruf mit Mario, Formular, FAQ.

Korrigiert: "bis zu 90 %" -> bis zu 85 %; "echter Selbstversorger", "fast zum Nulltarif", "vom ersten Tag an
bezahlt" -> sachlich; Autarkie -> Eigenverbrauch bis zu 80 % mit Speicher; "doppelte Foerderung von Bund und
Laendern", "Maximum aus beiden Foerdertoepfen", "Foerderungen sind begrenzt" -> Foerderstand wird geprueft, keine
Betraege; Ertragsprognose -> Projektbericht mit 3D-Belegplan und Statikreport; Techniker/Montageteams ->
zertifizierte Fachkraefte; Leasing/ab 49 €/keine Bonitaetspruefung/24 Stunden/KSV/Servicevertrag -> Finanzierung
ab 147 €* inkl. Speicher fuer die PV-Anlage, Eigentum ab Tag 1; "tausende Euro" -> sachlich; "100 Anlagen pro
Jahr" -> 300+ Projekte; "ganz Oesterreich" als Einsatzgebiet -> Kaernten und Steiermark; Widmanngasse -> NAP.
Zahlen aus build/pages/waermepumpe.py und dem Muster.
"""

_I = "/assets/img/"

LP = {
    "path": "/waermepumpe-photovoltaik-oesterreich/",
    "title": "Wärmepumpe und Photovoltaik kombinieren | EBZ Energie",
    "description": ("Wärmepumpe und PV-Anlage aus einer Hand: Heizen mit eigenem Sonnenstrom, bis zu 85 % weniger "
                    "Energiekosten, Förderabwicklung inklusive. 4,9 Sterne."),
    "eyebrow": "Bis zu 85 % Energiekosten sparen",
    "h1": "Wärmepumpe und Photovoltaik kombinieren: heizen mit eigenem Sonnenstrom",
    "lead": ("Die Kombination aus Photovoltaik und Wärmepumpe macht Sie weitgehend zum Selbstversorger: Ihre PV-Anlage "
             "produziert den Strom, und Ihre Wärmepumpe nutzt ihn zum Heizen. EBZ Energie übernimmt alles: Planung, "
             "Montage und den kompletten Papierkram. Schlüsselfertig aus einer Hand, inklusive Förderabwicklung."),
    "badges": [("bis zu 85 %", "weniger Energiekosten"), ("1 Ansprechpartner", "für PV und Wärmepumpe"), ("300+", "Projekte")],
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit Photovoltaikanlage auf dem Dach vor einer Bergkulisse",
    "media": {
        "hero_bg": _I + "lp-hero-alpenhaus.jpg",
        "problem_img": (_I + "lp-haus-pv-waermepumpe.jpg",
                        "Modernes Einfamilienhaus mit Photovoltaik auf dem Dach und Wärmepumpe vor dem Haus"),
        "grafik": "GRAFIK_WP_PV",
        "mario": False,
        "mario_cta": True,
        "steps_bg": _I + "lp-bg-module-abendsonne.jpg",
        "finance_img": (_I + "lp-finanzierung-haus.jpg", "Geldscheine vor einem Einfamilienhaus mit Photovoltaikanlage"),
        "gallery": "GALLERY_2023",
        "final_mario": True,
    },
    "problem": {
        "eyebrow": "Das Problem",
        "h2": "Strom und Heizung: zwei Rechnungen, die jeden Monat mehr werden",
        "paragraphs": [
            ("Die Strompreise steigen. Die Heizkosten steigen. Und Sie stehen jeden Monat vor der gleichen Frage: Wie "
             "viel wird es diesmal sein?"),
            ("Diese doppelte Abhängigkeit vom Strommarkt und vom Heizungsmarkt kostet Sie Jahr für Jahr viel Geld."),
        ],
        "bullets_intro": "Dabei könnten Sie beides gleichzeitig lösen, mit nur einer einzigen Entscheidung.",
        "bullets": [
            "<b>Das perfekte Duo:</b> Ihre PV-Anlage liefert den eigenen Sonnenstrom, die Wärmepumpe heizt Ihr Haus.",
            ("<b>Alles aus einer Hand:</b> ein Ansprechpartner für Planung, Montage und Inbetriebnahme beider Systeme. "
             "Kein Handwerker-Chaos."),
            ("<b>Förderabwicklung inklusive:</b> Wir prüfen den aktuellen Förderstand und übernehmen den lästigen "
             "Papierkram und die Anträge für Sie."),
            ("<b>Sicher entscheiden:</b> kostenlose, persönliche Beratung und technische Machbarkeitsprüfung direkt "
             "bei Ihnen vor Ort."),
        ],
    },
    "system": {
        "eyebrow": "So funktioniert es",
        "h2": "So funktioniert die Kombination aus PV und Wärmepumpe: zwei Technologien, die füreinander gemacht sind",
        "paragraphs": [
            ("Machen Sie Ihr Zuhause zum Selbstversorger und verabschieden Sie sich von steigenden Energiekosten. Das "
             "Prinzip ist einfach: Ihre Photovoltaikanlage auf dem Dach fängt kostenlose Sonnenenergie ein und liefert "
             "sauberen Strom."),
            ("Genau diesen Strom nutzt Ihre Wärmepumpe als Antrieb und erzeugt daraus mit hoher Effizienz Heizung und "
             "Warmwasser für Ihr gesamtes Haus: Aus 1 kWh Strom und 3 bis 4 kWh Umweltwärme entstehen 4 bis 5 kWh "
             "Heizwärme."),
            ("Sie heizen damit sehr günstig, machen sich unabhängig von den Launen des Strommarktes und investieren in "
             "ein nachhaltiges System, das sich Monat für Monat auf Ihrem Konto bemerkbar macht. Eigener Solarstrom "
             "kostet 10 bis 14 Cent je kWh, Netzstrom das Zwei- bis Dreifache.*"),
        ],
    },
    "benefits": {
        "eyebrow": "Ihre Vorteile",
        "h2": "Außerdem profitieren Sie von diesen Vorteilen",
        "intro": "Wir planen PV-Anlage, Speicher und Wärmepumpe als ein System, passend zu Ihrem Haus und Ihrem Verbrauch.",
        "cards": [
            ("€", "Strom- und Heizkosten sinken gleichzeitig",
             "Nicht nur eine Rechnung reduzieren, sondern beide. Die Kombination aus PV und Wärmepumpe ist der "
             "effektivste Weg, Ihre gesamten Energiekosten dauerhaft zu senken. Mit PV-Anlage und Speicher sinken die "
             "Heizkosten im Beispielhaus auf 200 bis 500 € im Jahr.*"),
            ("▮", "Mehr Unabhängigkeit mit Speicher",
             "Mit einem Batteriespeicher versorgen Sie sich auch abends, nachts und an bewölkten Tagen weitgehend selbst, "
             "Ihr Eigenverbrauch steigt auf bis zu 80 %. Steigende Strom- und Gaspreise treffen Sie nur noch beim Reststrom."),
            ("✓", "Zwei Systeme, eine Förderabwicklung",
             "Wir prüfen für PV-Anlage und Wärmepumpe jeweils den aktuellen Förderstand, stellen jeden Antrag korrekt "
             "und rechtzeitig, und Sie müssen sich um nichts kümmern."),
            ("⌂", "Mehr Wert für Ihre Immobilie",
             "Ein Gebäude, das sich weitgehend selbst mit Strom und Wärme versorgt, ist am Markt deutlich attraktiver. "
             "Ihre Investition zahlt sich doppelt aus."),
        ],
    },
    "quote": ("Von der kostenlosen Besichtigung vor Ort über die Förderabwicklung bis zur fertigen Installation von "
              "Photovoltaik und Wärmepumpe: Wir setzen Ihr Projekt schlüsselfertig für Sie um."),
    "steps": {
        "eyebrow": "So einfach geht es",
        "h2": "Ihr Weg zur Energieunabhängigkeit mit EBZ: in 4 einfachen Schritten",
        "steps": [
            ("Kostenlose und ehrliche Beratung",
             "Kein Druck, kein Verkaufsgespräch. Wir analysieren Ihren Strom- und Wärmebedarf und zeigen Ihnen ehrlich, "
             "wie Sie effektiv Kosten sparen.", "Tag 1"),
            ("Maßgeschneiderte Planung",
             "Wir kommen zu Ihnen vor Ort. Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport, die "
             "Heizlastberechnung und ein transparentes Gesamtangebot für das kombinierte System, ohne versteckte Kosten.",
             "ca. 1 Woche"),
            ("Wir erledigen die Bürokratie",
             "Förderanträge, Behördenkommunikation und Anmeldung beim Netzbetreiber: Sie lehnen sich zurück, wir "
             "übernehmen den Rest.", "parallel"),
            ("Installation und Inbetriebnahme",
             "Zertifizierte Fachkräfte installieren PV-Anlage und Wärmepumpe sauber und zügig. Anschließend erklären wir "
             "Ihnen alles und bleiben auch nach der Installation Ihr Ansprechpartner.", "wenige Tage"),
        ],
    },
    "why": {
        "eyebrow": "Warum EBZ Energie",
        "h2": "Darum sollten Sie sich für EBZ entscheiden: Ihr Energie-Partner für Kärnten und die Steiermark",
        "items": [
            ("☀", "PV und Wärmepumpe aus einer Hand",
             "Ein Ansprechpartner, ein Vertrag: Planung, Montage, Förderabwicklung und Netzanmeldung für beide Systeme."),
            ("✓", "Zertifizierte Fachkräfte", "Meisterhaftes Handwerk und sorgfältige Ausführung nach österreichischen Normen."),
            ("€", "Förderabwicklung für beide Systeme",
             "Wir prüfen für PV-Anlage und Wärmepumpe den aktuellen Förderstand und übernehmen die Anträge."),
            ("◇", "Bis zu 30 Jahre Leistungsgarantie",
             "Bis zu 30 Jahre Leistungsgarantie auf die Module, mindestens 10 Jahre Produktgarantie."),
            ("◎", "Volle Transparenz", "Kein Angebot ohne klare Kostenaufstellung, ohne versteckte Kosten."),
            ("⌂", "Regionale Expertise", "Zuhause in Villach, im Einsatz in Kärnten und der Steiermark."),
        ],
    },
    "finance": True,
    "refs": ["villach", "krumpendorf"],
    "gallery_h2": "Echte Projekte, echte Ergebnisse, aus Ihrer Region",
    "contact": {
        "h2": "Jetzt unverbindlich anfragen",
        "sub": "Sagen Sie uns kurz, wie Sie heute heizen und wie viel Strom Sie brauchen. Wir melden uns innerhalb eines Werktags.",
    },
    "faq": [
        ("Ist mein Haus für eine Wärmepumpe geeignet?",
         "Moderne Wärmepumpen funktionieren in den meisten Gebäuden, auch in älteren Häusern ohne Fußbodenheizung. Bis "
         "55 Grad Vorlauf arbeitet eine moderne Wärmepumpe effizient. Wir prüfen Ihr Gebäude kostenlos vor Ort und "
         "sagen Ihnen ehrlich, was für Ihre Situation Sinn ergibt."),
        ("Funktioniert die Wärmepumpe auch im Winter zuverlässig?",
         "Ja. Moderne Luft-Wasser-Wärmepumpen arbeiten bis minus 20 Grad Außentemperatur, auch im Klima von Kärnten und "
         "der Steiermark. Im Winter liefert die PV-Anlage weniger, dann kommt der Reststrom aus dem Netz. Ihre "
         "Wärmeversorgung ist auch an den kältesten Tagen gesichert."),
        ("Lohnt sich die Kombination aus PV und Wärmepumpe wirklich?",
         "Ja. Eine Wärmepumpe, die mit selbst erzeugtem Sonnenstrom läuft, hat sehr niedrige Betriebskosten: Eigener "
         "Solarstrom kostet 10 bis 14 Cent je kWh, Netzstrom das Zwei- bis Dreifache. Mit PV-Anlage und Speicher sinken "
         "die Heizkosten im Beispielhaus auf 200 bis 500 € im Jahr.*"),
        ("Wie groß muss die PV-Anlage für eine Wärmepumpe sein?",
         "Für Haushalt und Wärmepumpe planen wir meist 10 bis 15 kWp mit einem Speicher von 10 bis 12 kWh. Die genaue "
         "Größe richtet sich nach Ihrem Verbrauch und Ihrem Dach."),
        ("Was kostet mich das wirklich?",
         "Als Richtwert kostet eine PV-Anlage mit 10 kWp und Speicher rund 15.000 bis 22.000 €, eine Luft-Wasser-Wärmepumpe "
         "inklusive Montage rund 12.000 bis 22.000 €, jeweils vor Förderung.* Sie erhalten ein detailliertes "
         "Festpreisangebot ohne Überraschungen. Mit unserer Finanzierung gehört die PV-Anlage ab dem ersten Tag Ihnen, "
         "ab 147 € im Monat inklusive Speicher.*"),
        ("Welche Förderung bekomme ich?",
         "Ob und wie PV-Anlage und Wärmepumpe gefördert werden, hängt von Bundesland und Projekt ab, und die Förderlage "
         "ändert sich derzeit laufend. Wir prüfen den aktuellen Förderstand für Ihr Projekt und übernehmen die Anträge."),
        ("Was passiert nach der Installation?",
         "Wir bleiben Ihr Ansprechpartner für Service-Checks, Fragen zur Überwachung oder wenn einmal etwas nicht stimmt, "
         "erreichbar Montag bis Freitag von 10 bis 20 Uhr. Bei uns endet die Betreuung nicht mit der Inbetriebnahme."),
    ],
    "finalcta": {
        "eyebrow": "Machen Sie sich jetzt mit EBZ unabhängig",
        "h2": "Verschenken Sie kein Geld mehr an die Energiekonzerne",
        "text": ("Jeder Tag ohne Photovoltaik und Wärmepumpe ist ein Tag, an dem Sie Geld verschenken. Der beste "
                 "Zeitpunkt zum Handeln war gestern, der zweitbeste ist jetzt."),
        "more": [
            ("Wir kombinieren handwerkliche Präzision mit moderner Technik und einem Serviceversprechen, das über die "
             "Montage hinausgeht. Die Erfahrung aus über 300 dokumentierten Projekten fließt in jedes neue Projekt ein."),
            ("Der erste Schritt in eine unabhängige Zukunft ist ein Gespräch. Kontaktieren Sie uns noch heute für Ihr "
             "kostenloses und unverbindliches Angebot."),
            "Das Team von EBZ Energie freut sich auf Sie.",
        ],
    },
    "footnote": ("*Richtwerte und Beispielkonditionen, Stand Oktober 2026, abhängig von Gebäude, Verbrauch, Anlagengröße, "
                 "Dach und Laufzeit. Alle Preise vor Förderung. Verbindlich ist Ihr persönliches Angebot."),
}
