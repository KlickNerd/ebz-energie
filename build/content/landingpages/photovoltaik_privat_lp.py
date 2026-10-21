"""Ads-Landingpage Photovoltaik privat (alte WP-Seite /photovoltaik-privat-lp/, Stand Mai 2026).

Botschaft der alten LP uebernommen (Unabhaengigkeit vom Stromanbieter, PV + Speicher + Wallbox, alles aus
einer Hand, Foerderabwicklung, Finanzierung). Korrigiert: 90 % -> bis zu 85 %, Leasing/ab 49 €/keine
Bonitaetspruefung -> Finanzierung ab 147 €*, eigene Montageteams -> zertifizierte Fachkraefte,
Ertragsprognose -> Projektbericht, Widmanngasse -> Triglavstrasse 15 (kommt aus NAP).
"""

LP = {
    "path": "/photovoltaik-privat-lp/",
    "title": "Photovoltaik mit Speicher: schlüsselfertig | EBZ Energie",
    "description": ("Photovoltaik mit Speicher und Wallbox vom Fachbetrieb aus Villach: Beratung, Förderabwicklung und "
                    "Montage aus einer Hand. 4,9 Sterne, 300+ Projekte. Jetzt anfragen."),
    "eyebrow": "Photovoltaik für Ihr Zuhause",
    "h1": "Machen Sie sich unabhängig vom Stromanbieter: Ihre PV-Anlage mit Speicher, schlüsselfertig aus einer Hand",
    "lead": ("Sie produzieren Ihren eigenen Sonnenstrom und senken Ihre Energiekosten um bis zu 85 %. EBZ Energie "
             "übernimmt alles: Beratung vor Ort, Planung, Förderabwicklung, Montage und Netzanmeldung."),
    "badges": [("4,9", "Sterne auf Google"), ("300+", "Projekte"), ("bis 30 J.", "Leistungsgarantie")],
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit Photovoltaikanlage auf dem Dach",
    "problem": {
        "eyebrow": "Das Problem",
        "h2": "Ihr Stromanbieter erhöht die Preise, und Sie zahlen",
        "paragraphs": [
            ("Grundgebühr, Netzentgelt, Arbeitspreis: Die Stromkosten in Österreich sind in den letzten Jahren deutlich "
             "gestiegen, und jede Jahresabrechnung bringt die nächste Überraschung."),
            ("Diese Abhängigkeit kostet nicht nur Geld, sondern auch Planungssicherheit. Dabei scheint die Energie, "
             "die Sie brauchen, jeden Tag kostenlos auf Ihr Dach."),
        ],
        "bullets_intro": "Es gibt einen besseren Weg, erprobt und zuverlässig: Ihre eigene Photovoltaikanlage.",
        "bullets": [
            "<b>Das perfekte Trio:</b> PV-Anlage, Stromspeicher und Wallbox. Sie produzieren, speichern und nutzen Ihren Sonnenstrom.",
            "<b>Alles aus einer Hand:</b> ein Ansprechpartner für Planung, Montage und Inbetriebnahme aller Komponenten.",
            "<b>Förderabwicklung inklusive:</b> Wir übernehmen Anträge, Papierkram und die Anmeldung beim Netzbetreiber.",
            "<b>Sicher entscheiden:</b> kostenlose, persönliche Beratung und technische Prüfung direkt bei Ihnen vor Ort.",
        ],
    },
    "benefits": {
        "eyebrow": "Ihre Vorteile",
        "h2": "Photovoltaik, Speicher und Wallbox: ein Energiesystem für Ihr Zuhause",
        "intro": "Sie produzieren, speichern und nutzen Ihren eigenen Strom. Wir planen das System passend zu Ihrem Verbrauch.",
        "cards": [
            ("€", "Stromkosten dauerhaft senken",
             "Mit Speicher steigt Ihr Eigenverbrauch auf bis zu 80 %. Sie senken Ihre Energiekosten um bis zu 85 %."),
            ("☀", "Unabhängig vom Strompreis",
             "Ihren Sonnenstrom produzieren Sie selbst. Preiserhöhungen Ihres Anbieters treffen nur noch den Reststrom."),
            ("⌖", "E-Auto mit Sonnenstrom laden",
             "Eine Wallbox mit Überschussladen tankt Ihr Auto bevorzugt dann, wenn das Dach mehr liefert als das Haus braucht."),
            ("✓", "Förderabwicklung inklusive",
             "Wir prüfen, welche Förderungen für Ihr Projekt gelten, und übernehmen Anträge und Netzanmeldung für Sie."),
        ],
    },
    "quote": ("Von der kostenlosen Besichtigung vor Ort über die Förderabwicklung bis zur fertigen Installation von "
              "PV-Anlage, Speicher und Wallbox: Wir setzen Ihr Projekt schlüsselfertig für Sie um."),
    "steps": {
        "eyebrow": "So einfach geht es",
        "h2": "In 4 Schritten zu Ihrer eigenen PV-Anlage",
        "steps": [
            ("Kostenlose Beratung", "Wir besprechen Ihren Stromverbrauch, Ihr Dach und Ihre Pläne, ehrlich und ohne Verkaufsdruck.", "Tag 1"),
            ("Planung vor Ort", "Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport und ein transparentes Festpreisangebot.", "ca. 1 Woche"),
            ("Förderung und Anmeldung", "Wir stellen die Förderanträge und melden die Anlage beim Netzbetreiber an.", "parallel"),
            ("Montage und Übergabe", "Zertifizierte Fachkräfte montieren Ihre Anlage. Bei der Übergabe erklären wir Ihnen alles.", "1 bis 3 Tage"),
        ],
    },
    "finance": True,
    "refs": ["villach", "krumpendorf", "gewerbe"],
    "contact": {
        "h2": "Jetzt unverbindlich anfragen",
        "sub": "Sagen Sie uns kurz, worum es geht. Wir melden uns innerhalb eines Werktags und vereinbaren einen Termin vor Ort.",
    },
    "faq": [
        ("Ist mein Dach für eine Photovoltaikanlage geeignet?",
         "In den meisten Fällen ja. Moderne Module arbeiten auch auf Ost- und Westdächern wirtschaftlich. Wir prüfen Ihr Dach kostenlos vor Ort."),
        ("Brauche ich einen Stromspeicher?",
         "Ein Speicher hebt den Eigenverbrauch von rund 30 % auf bis zu 80 %. Sie nutzen Ihren Sonnenstrom dann auch am Abend und in der Nacht."),
        ("Lohnt sich eine Wallbox mit Photovoltaik?",
         "Ja, wenn Sie ein E-Auto fahren oder eines planen. Mit Überschussladen laden Sie bevorzugt mit eigenem Sonnenstrom statt mit Netzstrom."),
        ("Welche Förderung bekomme ich?",
         "Das hängt von Bundesland, Anlagengröße und Speicher ab. Wir prüfen den aktuellen Förderstand für Ihr Projekt und übernehmen die Anträge."),
        ("Was kostet eine PV-Anlage mit Speicher?",
         "Als Richtwert kostet eine Anlage mit 10 kWp und Speicher rund 15.000 bis 22.000 € vor Förderung.* Sie erhalten ein Festpreisangebot ohne versteckte Kosten."),
        ("Kann ich die Anlage finanzieren?",
         "Ja. Mit unserer Finanzierung gehört die Anlage ab dem ersten Tag Ihnen, ab 147 € im Monat inklusive Speicher.*"),
        ("Was passiert nach der Installation?",
         "Wir bleiben Ihr Ansprechpartner für Service und Fragen. Sie haben einen festen Ansprechpartner von der Planung bis zur Übergabe und darüber hinaus."),
    ],
    "finalcta": {
        "eyebrow": "Machen Sie sich jetzt unabhängig",
        "h2": "Wie viele Sonnenstunden wollen Sie noch ungenutzt lassen?",
        "text": ("Jeder Tag ohne eigene PV-Anlage ist ein Tag, an dem Sie Strom teuer zukaufen. Wir verbinden "
                 "sorgfältiges Handwerk mit moderner Technik und bleiben auch nach der Montage Ihr Ansprechpartner."),
        "more": ["Der erste Schritt ist ein kostenloses Gespräch. Das Team von EBZ Energie freut sich auf Sie."],
    },
    "footnote": "*Richtwerte und Beispielkonditionen, abhängig von Anlagengröße, Dach und Laufzeit. Verbindlich ist Ihr persönliches Angebot.",
}
