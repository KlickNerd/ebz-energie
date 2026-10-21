"""Ads-Landingpage Heimkraftwerk (alte WP-Seite /heimkraftwerk-lp/, Stand 2025).

Aufbau wie die alte LP (Oktober 2026 abgeglichen): Vollbild-Hero "Photovoltaik-Anlage mit Speicher",
Paket "komplett mit Speicher" mit Modul-Nahaufnahme, "Besonders lange Garantie", Vorteile 01/02/03 neben dem
Heimkraftwerk-Foto, Projektbericht mit Telefon, Galerie 2024, Formular, drei Schritte (hier vor dem Formular,
damit das Formular der letzte grosse Abschnitt bleibt; dazu Bewertungen direkt vor dem Formular wie das
"Ausgezeichnet"-Widget der alten LP).

Korrigiert: "Landesfoerderung 2025, Foerdermittel begrenzt" weggelassen (veraltet), stattdessen
"Foerderabwicklung inklusive"; "30 Jahre Vollgarantie" / "15 Jahre auf Wechselrichter und Speicher" -> bis zu
30 Jahre Leistungsgarantie, mind. 10 Jahre Produktgarantie; "10,68 kWp, 24 x 445 Wp" -> rund 10 kWp;
"Made in Germany" und "EU-Komponenten" (nicht belegt) -> neutrale Qualitaetsaussage; "Keine Vorauszahlungen"
(nicht belegt) weggelassen; "30-seitiger Projektbericht mit Statik- und Ertragsberechnungen" und
"Ertragsauswertung Monat/Jahr" -> Projektbericht mit 3D-Belegplan und Statikreport; Widmanngasse -> NAP.
"""

LP = {
    "path": "/heimkraftwerk-lp/",
    "title": "Heimkraftwerk: PV-Anlage mit Speicher zum Festpreis | EBZ",
    "description": ("Heimkraftwerk: PV-Anlage mit rund 10 kWp und Speicher, komplett mit Montage, Anmeldung und "
                    "Förderabwicklung zum Festpreis. Bis zu 30 Jahre Leistungsgarantie."),
    "eyebrow": "Vollwertiges Heimkraftwerk mit bis zu 30 Jahren Leistungsgarantie",
    "h1": "Photovoltaik-Anlage mit Speicher",
    "lead": ("Ihr Heimkraftwerk komplett vom Kärntner PV-Fachbetrieb: rund 10 kWp, erweiterbarer Batteriespeicher und "
             "Notstromfunktion, geplant, montiert und angemeldet aus einer Hand. Sie erhalten ein Festpreisangebot ohne "
             "versteckte Kosten, die Förderabwicklung ist inklusive."),
    "badges": [("bis 30 J.", "Leistungsgarantie"), ("Förderabwicklung", "inklusive"), ("4,9", "Sterne auf Google")],
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit Photovoltaikanlage auf dem roten Ziegeldach",
    "media": {
        "hero_bg": "/assets/img/lp-heimkraftwerk.jpg",
        "problem_img": ("/assets/img/lp-hero-module-sonne.jpg",
                        "Nahaufnahme von Photovoltaikmodulen im Licht der untergehenden Sonne"),
        "grafik": ("/assets/img/lp-heimkraftwerk.jpg",
                   "Einfamilienhaus mit Photovoltaikanlage auf dem roten Ziegeldach", 1100, 825),
        "final_mario": True,
        "steps_bg": "/assets/img/lp-bg-module-abendsonne.jpg",
        "gallery": "GALLERY_2024",
    },
    "order": ["hero", "problem", "why", "system", "final", "gallery", "steps", "reviews", "contact", "faq",
              "footnote"],
    # alte LP: "Photovoltaik-Anlage komplett mit Speicher" + Paketliste neben der Modul-Nahaufnahme
    "problem": {
        "eyebrow": "Top-Qualität vom Kärntner PV-Fachbetrieb",
        "h2": "Photovoltaik-Anlage komplett mit Speicher",
        "paragraphs": [
            ("Ein vollwertiges Heimkraftwerk statt Stückwerk: Module, Wechselrichter, Speicher, Montage, Anmeldung und "
             "Förderung bekommen Sie aus einer Hand, mit einem festen Ansprechpartner von der Planung bis zur Übergabe."),
        ],
        "bullets_intro": "Das ist im Komplettpaket enthalten:",
        "bullets": [
            "PV-Anlage mit rund 10 kWp",
            "Bifaziale Glas-Glas-Module in TOPCon-Technologie, bis zu 30 Jahre Leistungsgarantie",
            "Hybridwechselrichter mit Notstromfunktion",
            "Erweiterbarer Eisenphosphat-Speicher mit rund 10 kWh",
            "Unterkonstruktion mit Blech-Ersatzziegeln",
            "Komplettmontage inklusive Verkabelung",
            "Elektrischer Netzanschluss inklusive Dokumentation",
            "Zählpunktansuchen inklusive Fertigstellungsmeldung beim Netzbetreiber",
            "Förderabwicklung",
            "Projektbericht mit 3D-Belegplan und Statikreport",
            "Professionelle Drohnenaufnahmen Ihres Grundstücks",
        ],
    },
    # alte LP: "Besonders lange Garantie" mit zwei grossen Zahlen
    "why": {
        "eyebrow": "Hochwertige Komponenten für eine lange Lebensdauer",
        "h2": "Besonders lange Garantie",
        "items": [
            ("◇", "Bis zu 30 Jahre",
             "Leistungsgarantie auf die Solarmodule. Die Module liefern über Jahrzehnte zuverlässig Strom."),
            ("✓", "Mindestens 10 Jahre",
             "Produktgarantie auf die Komponenten Ihres Heimkraftwerks."),
            ("▮", "Speicher mit Kapazitätsgarantie",
             "Bei Speichern geben die Hersteller üblicherweise 10 Jahre Garantie darauf, dass die Kapazität nicht "
             "unter 80 % fällt."),
        ],
    },
    # alte LP: "Ihre Vorteile beim Kaerntner Photovoltaik-Fachbetrieb!" 01./02./03. neben dem Heimkraftwerk-Foto
    "system": {
        "eyebrow": "Ihre Vorteile",
        "h2": "Ihre Vorteile beim Kärntner Photovoltaik-Fachbetrieb",
        "paragraphs": [
            ("<b>01. Top-Qualität</b><br>Module, Wechselrichter, Speicher, Wallbox und Dach-Unterkonstruktion in "
             "hochwertiger Qualität, sorgfältig montiert von zertifizierten Fachkräften."),
            ("<b>02. Mehr Ertrag mit bis zu 30 Jahren Garantie</b><br>Bifaziale TOPCon-Glas-Glas-Module nutzen auch "
             "das Licht, das auf ihre Rückseite fällt. Das sorgt für mehr Effizienz und mehr Ertrag, mit bis zu 30 Jahren "
             "Leistungsgarantie."),
            ("<b>03. Komplettservice</b><br>Lieferung, Montage, Anschluss, Förderabwicklung und Anmeldung beim "
             "Netzbetreiber: Sie müssen sich um nichts kümmern."),
        ],
    },
    # alte LP: "Professioneller Projektbericht" + Telefon (Schluss-Aufruf mit Mario, vor Galerie und Formular)
    "finalcta": {
        "eyebrow": "Sicherheit vor Baubeginn",
        "h2": "Professioneller Projektbericht, bevor wir bauen",
        "text": ("Bereits vor Baubeginn erhalten Sie einen vollständigen Projektbericht mit 3D-Belegplan und "
                 "Statikreport. Sie sehen vorab genau, was auf Ihr Dach kommt."),
        "more": [
            ("Der Bericht enthält den Belegplan mit realer Ausrichtung in der 3D-Ansicht, die Berechnung der "
             "Unterkonstruktion und die Berücksichtigung von Verschattung, Wind- und Schneelast."),
            "Rufen Sie uns an oder fordern Sie Ihr kostenloses Angebot an.",
        ],
    },
    "gallery_h2": "Ihr Photovoltaik-Fachbetrieb in Kärnten: PV-Anlagen, Batteriespeicher, Solarmodule",
    # alte LP: "In drei Schritten zu Ihrer Photovoltaik-Anlage" (Raster mit vier Spalten: Uebergabe als 4. Schritt)
    "steps": {
        "eyebrow": "So einfach geht es",
        "h2": "In vier Schritten zu Ihrer Photovoltaik-Anlage",
        "steps": [
            ("Kontaktaufnahme",
             "Wir informieren Sie umfassend über alle Möglichkeiten, Kosten und Förderungen Ihres geplanten PV-Projekts. "
             "Diese Beratung ist für Sie kostenlos und unverbindlich.", "Tag 1"),
            ("Planung und Kalkulation",
             "Wir besichtigen vor Ort und erstellen eine professionelle Planung mit Projektbericht, 3D-Belegplan, "
             "Statikreport und Konstruktionsberechnungen als Basis für unser Angebot.", "ca. 1 Woche"),
            ("Installation",
             "Wir kümmern uns um alle Details der Installation inklusive Batteriespeicher und Förderabwicklung. "
             "Zertifizierte Fachkräfte montieren Ihre Anlage schlüsselfertig.", "1 bis 3 Tage"),
            ("Übergabe und Service",
             "Bei der Übergabe erklären wir Ihnen alles. Danach bleiben wir Ihr fester Ansprechpartner, mit einem "
             "verlässlichen Service nach dem Kauf.", "danach"),
        ],
    },
    "contact": {
        "h2": "Jetzt unverbindlich anfragen",
        "sub": ("Sagen Sie uns kurz, wo Ihr Heimkraftwerk entstehen soll. Wir melden uns innerhalb eines Werktags und "
                "vereinbaren einen Termin vor Ort."),
    },
    "faq": [
        ("Was ist im Heimkraftwerk enthalten?",
         "Glas-Glas-Module für rund 10 kWp, Hybridwechselrichter mit Notstromfunktion, erweiterbarer Batteriespeicher, "
         "Unterkonstruktion mit Ersatzziegeln, Komplettmontage, Netzanschluss mit Dokumentation, Anmeldung beim "
         "Netzbetreiber, Förderabwicklung und ein Projektbericht mit 3D-Belegplan und Statikreport."),
        ("Was kostet ein Heimkraftwerk mit Speicher?",
         "Als Richtwert kostet eine Anlage mit 10 kWp und Speicher rund 15.000 bis 22.000 € vor Förderung.* Sie erhalten "
         "ein Festpreisangebot ohne versteckte Kosten, abgestimmt auf Ihr Dach und Ihren Verbrauch."),
        ("Welche Garantie bekomme ich?",
         "Bis zu 30 Jahre Leistungsgarantie auf die Module und mindestens 10 Jahre Produktgarantie. Bei Speichern geben "
         "die Hersteller üblicherweise 10 Jahre Garantie darauf, dass die Kapazität nicht unter 80 % fällt."),
        ("Funktioniert das Heimkraftwerk bei einem Stromausfall?",
         "Ja, wenn es notstromfähig geplant ist: Dafür braucht es einen notstromfähigen Hybridwechselrichter, einen "
         "freigegebenen Speicher und eine Umschalteinrichtung. Das planen wir von Anfang an mit ein."),
        ("Kann ich den Speicher später erweitern?",
         "Ja, wir planen Speicher, die sich modular erweitern lassen. Wenn später Wärmepumpe oder E-Auto dazukommen, "
         "wächst Ihr Heimkraftwerk mit."),
        ("Welche Förderung bekomme ich?",
         "Das hängt von Bundesland, Anlagengröße und Speicher ab. Wir prüfen den aktuellen Förderstand für Ihr Projekt "
         "und übernehmen die Anträge."),
        ("Kann ich das Heimkraftwerk finanzieren?",
         "Ja. Mit unserer Finanzierung gehört die Anlage ab dem ersten Tag Ihnen, ab 147 € im Monat inklusive Speicher.*"),
    ],
    "footnote": ("*Richtwerte und Beispielkonditionen, abhängig von Anlagengröße, Dach und Laufzeit. Verbindlich ist Ihr "
                 "persönliches Angebot."),
}
