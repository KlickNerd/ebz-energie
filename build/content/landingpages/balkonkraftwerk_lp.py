"""Ads-Landingpage Balkonkraftwerk (alte WP-Seite /balkonkraftwerk-lp/, Stand 2025).

Aufbau wie die alte LP (Oktober 2026 abgeglichen): Vollbild-Hero "Balkonkraftwerk komplett", "Kleinkraftwerk
fuer Ihr Zuhause" mit Paketliste neben der Modul-Nahaufnahme, Pakete (ohne Preis), "Ihr Photovoltaik-Fachbetrieb
garantiert Ihnen" 01/02/03, Tipp "Vereinfachte Bewilligung" von Mario mit Telefon, Galerie 2024, Bewertungen
(wie das "Ausgezeichnet"-Widget der alten LP direkt vor dem Formular), Formular, dazu FAQ.

Korrigiert: Fixpreise 995 € / 1.995 € und "Sparen Sie 500 € / 740 €" weggelassen (nicht freigegeben), Pakete
"Preis auf Anfrage"; Speicherfoto und Speichermarke der alten LP nicht uebernommen; "800 Wp Wechselrichter" ->
800 Watt; "30 Jahre Garantie" -> bis zu 30 Jahre Leistungsgarantie auf die Module; Tipp "Seit 1. September ...
Nachbarn" -> Zustimmungsfiktion im Wohnungseigentum seit 1. September 2024; Widmanngasse -> NAP.
Keine Foerderbetraege.
"""

LP = {
    "path": "/balkonkraftwerk-lp/",
    "title": "Balkonkraftwerk komplett mit Montage und Anmeldung | EBZ",
    "description": ("Balkonkraftwerk komplett vom Fachbetrieb: 800 Watt, auf Wunsch mit Speicher, Montage und Meldung "
                    "beim Netzbetreiber in Kärnten und der Steiermark."),
    "eyebrow": "Beste Qualität vom Photovoltaik-Fachbetrieb",
    "h1": "Balkonkraftwerk komplett",
    "lead": ("Inklusive Anmeldung beim Netzbetreiber und bis zu 30 Jahre Leistungsgarantie auf die Module. Ein "
             "Balkonkraftwerk mit 800 Watt liefert bei guter Ausrichtung 600 bis 800 kWh im Jahr.* Wir stellen das "
             "passende Komplettset zusammen, auf Wunsch mit Speicher, und montieren es sturmsicher."),
    "badges": [("800 Watt", "normgerecht"), ("bis 30 J.", "Leistungsgarantie"), ("4,9", "Sterne auf Google")],
    "hero_img": "balkon",
    "hero_alt": "Solarmodule eines Balkonkraftwerks am Balkongeländer eines Wohnhauses",
    "media": {
        "hero_bg": "/assets/img/balkonkraftwerk.jpg",
        "problem_img": ("/assets/img/lp-hero-module-sonne.jpg",
                        "Nahaufnahme von Solarmodulen im Licht der untergehenden Sonne"),
        "mario_cta": True,
        "gallery": "GALLERY_2024",
    },
    "order": ["hero", "problem", "benefits", "why", "quote", "gallery", "reviews", "contact", "faq", "footnote"],
    # alte LP: "Kleinkraftwerk fuer Ihr Zuhause" / "Holen Sie sich die Kraft der Sonne!" mit Paketliste
    "problem": {
        "eyebrow": "Holen Sie sich die Kraft der Sonne!",
        "h2": "Kleinkraftwerk für Ihr Zuhause",
        "paragraphs": [
            ("Ein Balkonkraftwerk ist eine steckerfertige Mini-PV-Anlage mit bis zu 800 Watt Wechselrichterleistung. "
             "Die Modulleistung ist frei wählbar, auch 1.200 bis 2.000 Wp sind möglich und bringen auch morgens, abends und im "
             "Winter mehr Ertrag. Geräte, die gerade laufen, nutzen den Sonnenstrom zuerst."),
        ],
        "bullets_intro": "Das ist im Komplettset enthalten:",
        "bullets": [
            "Solarmodule, zum Beispiel vier Flexmodule mit je 220 Wp, mit bis zu 30 Jahren Leistungsgarantie",
            "Halterungen: flexibel und stabil",
            "Wechselrichter mit 800 Watt",
            "Einrichtung der App",
            "Inklusive Anmeldung beim Netzbetreiber",
        ],
    },
    # alte LP: Preisabschnitt "Balkonkraftwerk" / "+ Speicher" (ohne Preise, nicht freigegeben)
    "benefits": {
        "eyebrow": "Ihre Pakete",
        "h2": "Balkonkraftwerk mit oder ohne Speicher",
        "intro": ("Zwei Pakete, ein Ablauf: Sie erhalten ein persönliches Festpreisangebot, in dem Set, Speicher und "
                  "Montage als eigene Positionen stehen."),
        "cards": [
            ("☀", "Balkonkraftwerk",
             "Module, Halterung, Wechselrichter mit 800 Watt, Einrichtung der App und Anmeldung beim Netzbetreiber. "
             "<b>Preis auf Anfrage.</b>"),
            ("▮", "Balkonkraftwerk mit Speicher",
             "Das Komplettset plus Speicher mit rund 2,5 kWh. Er hebt den Mittagsüberschuss für den Abend auf und den "
             "Eigenverbrauch auf 70 bis 80 %.* <b>Preis auf Anfrage.</b>"),
            ("✓", "Bei beiden Paketen inklusive",
             "Lieferung, Montage, Prüfung von Steckdose und Stromkreis und die Meldung bei Kärnten Netz, Energienetze "
             "Steiermark oder Stromnetz Graz."),
        ],
    },
    # alte LP: "Ihr Photovoltaik-Fachbetrieb garantiert Ihnen" 01./02./03.
    "why": {
        "eyebrow": "Darauf können Sie sich verlassen",
        "h2": "Ihr Photovoltaik-Fachbetrieb garantiert Ihnen",
        "items": [
            ("◇", "01. Top-Qualität",
             "Alle Komponenten aus dem Fachhandel, hagel- und sturmfest, die wir auch bei Dachanlagen einsetzen."),
            ("✓", "02. Bis zu 30 Jahre Garantie",
             "Extrem lange Lebensdauer: bis zu 30 Jahre Leistungsgarantie auf die Module."),
            ("⌂", "03. Komplettservice",
             "Lieferung, Montage, Anschluss und Anmeldung beim Netzbetreiber aus einer Hand."),
        ],
    },
    # alte LP: "Tipp: Vereinfachte Bewilligung" mit Mario und Telefon
    "quote": ("Tipp zur vereinfachten Bewilligung: Seit 1. September 2024 reicht es im Wohnungseigentum, die anderen "
              "Eigentümer schriftlich über Ihr geplantes Balkonkraftwerk zu verständigen. Widerspricht innerhalb von "
              "zwei Monaten niemand, gilt die Zustimmung als erteilt."),
    "gallery_h2": "Ihr Photovoltaik-Fachbetrieb: PV-Anlagen, Batteriespeicher, Solarmodule",
    "contact": {
        "h2": "Jetzt unverbindlich anfragen",
        "sub": ("Schreiben Sie uns, wo die Module hin sollen und wie Ihr Haushalt Strom verbraucht. Wir empfehlen das "
                "passende Set, mit oder ohne Speicher, und übernehmen die Meldung. Kostenlos und unverbindlich."),
    },
    "faq": [
        ("Muss ich mein Balkonkraftwerk anmelden?",
         "Ja, beim Netzbetreiber, nicht beim Stromlieferanten: in Kärnten bei der Kärnten Netz, in der Steiermark bei den "
         "Energienetzen Steiermark, in Graz bei der Stromnetz Graz. Die Meldung ist kostenlos und muss mindestens 14 Tage "
         "vor der Inbetriebnahme erfolgen. Das übernehmen wir für Sie."),
        ("Darf ich mehr als 800 Watt Module anschließen?",
         "Ja. Begrenzt ist nur die Einspeiseleistung des Wechselrichters mit 800 Watt. Die Modulleistung ist frei wählbar, "
         "1.200 oder 2.000 Wp sind üblich. Mit Speicher lädt der Überschuss über 800 Watt die Batterie."),
        ("Wie viel Strom liefert ein Balkonkraftwerk?",
         "Bei guter Ausrichtung 600 bis 800 kWh im Jahr, im Jahresmittel rund 2 kWh am Tag.* Bei 30 Cent je kWh sparen "
         "Sie damit rund 180 bis 240 € im Jahr.*"),
        ("Was kostet ein Balkonkraftwerk mit Montage?",
         "Ein Komplettset mit zwei Modulen, Mikro-Wechselrichter und Halterung kostet im Handel rund 800 €, die "
         "fachgerechte Montage rund 400 € (Richtwerte laut klimaaktiv).* Ein Speicher kommt dazu. Unser Angebot nennt Set, "
         "Speicher und Montage als eigene Positionen."),
        ("Wo kann ich das Balkonkraftwerk montieren?",
         "Am Balkongeländer, an der Loggia, an der Fassade, auf dem Flachdach, der Garage oder im Garten. Wir liefern die "
         "passende, statisch geprüfte Halterung."),
        ("Brauche ich die Zustimmung der anderen Wohnungseigentümer?",
         "Seit 1. September 2024 gilt im Wohnungseigentum die Zustimmungsfiktion: Sie informieren die anderen Eigentümer "
         "schriftlich, widerspricht innerhalb von zwei Monaten niemand, gilt die Zustimmung als erteilt. Mieter brauchen "
         "das Okay von Vermieter oder Hausverwaltung. Die technischen Unterlagen liefern wir."),
        ("Gibt es eine Förderung für Balkonkraftwerke?",
         "Das hängt von Bundesland und Gemeinde ab, die Programme ändern sich laufend. Wir prüfen den aktuellen Förderstand "
         "für Ihr Projekt und übernehmen die Anträge."),
    ],
    "footnote": ("*Richtwerte: Jahresertrag 600 bis 800 kWh für ein 800-Watt-Balkonkraftwerk bei guter Ausrichtung, "
                 "Ersparnis bei 30 ct/kWh, Eigenverbrauch mit Speicher 70 bis 80 %, Kostenanker 800 € Set plus 400 € "
                 "Montage laut klimaaktiv. Ertrag und Ersparnis hängen von Standort, Verschattung, Verbrauch und Strompreis "
                 "ab. Verbindlich ist Ihr persönliches Angebot."),
}
