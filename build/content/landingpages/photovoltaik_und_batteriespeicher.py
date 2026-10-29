"""Ads-Landingpage Photovoltaik und Batteriespeicher (alte WP-Seite /photovoltaik-und-batteriespeicher/, Stand 2024).

Aufbau wie die alte LP (Oktober 2026 abgeglichen): Vollbild-Hero "Photovoltaik und Batteriespeicher",
"PV komplett: Projektierung, Bau und Foerderabwicklung" mit Modulfoto, "Holen Sie sich die Kraft der Sonne" mit
Ziegeldach-Foto, "All-in-One: Fuer Private und Gewerbe" (Mario mit Telefon), "Mehr als nur saubere Energie"
(Komponenten), drei Schritte auf Foto (hier vier), Galerie, Bewertungen (wie das "Ausgezeichnet"-Widget der
alten LP direkt vor dem Formular), Formular, dazu FAQ.

Korrigiert/weggelassen: "Kaernten, Salzburg und die Steiermark" -> Kaernten und Steiermark (Montagegebiet);
"20 % MwSt-Bundesfoerderung" / "MwSt-Befreiung bis 35 kWp" (ausgelaufen) und Herbst-Aktion Gratis-Wallbox
(abgelaufen); "schluesselfertig in rund 3 Monaten" (nicht freigegeben); "6 bis 7 % Rendite durch Einspeisen"
und CO2-Zahlen inkl. Abschnitt "Ihr gruener Fingerabdruck" (nicht belegt); Infrarotheizungen (keine
EBZ-Leistung); "Wertsteigerung der Immobilie" -> zukunftssicher; Statik- und Energieertragsberechnungen ->
Projektbericht mit 3D-Belegplan und Statikreport; Widmanngasse -> NAP.
"""

LP = {
    "path": "/photovoltaik-und-batteriespeicher/",
    "title": "Photovoltaik und Batteriespeicher komplett | EBZ Energie",
    "description": ("Photovoltaik und Batteriespeicher vom Fachbetrieb in Kärnten und der Steiermark: Planung, Montage, "
                    "Notstrom und Förderabwicklung aus einer Hand. Jetzt anfragen."),
    "eyebrow": "Ihr Photovoltaik-Fachbetrieb für Kärnten und die Steiermark",
    "h1": "Photovoltaik und Batteriespeicher",
    "lead": ("Wir planen Ihre PV-Anlage mit Speicher und Notstromlösung, montieren sie schlüsselfertig und übernehmen "
             "Förderabwicklung und Netzanmeldung. Sie senken Ihre Energiekosten um bis zu 85 %, ob im Eigenheim oder "
             "im Betrieb."),
    "badges": [("bis zu 80 %", "Eigenverbrauch mit Speicher*"), ("300+", "Projekte"), ("4,9", "Sterne auf Google")],
    "hero_img": "pv_efh",
    "hero_alt": "Photovoltaikmodule auf dem Dach eines Wohnhauses in ländlicher Umgebung",
    "media": {
        "hero_bg": "/assets/img/lp-hero-module-sonne.jpg",
        "problem_img": ("/assets/img/lp-ref-module-ziegeldach.jpg",
                        "Nahaufnahme von Photovoltaikmodulen auf einem Ziegeldach mit Dachhaken"),
        "grafik": ("/assets/img/lp-ref-ziegeldach-bergblick.jpg",
                   "Photovoltaikanlage auf einem Ziegeldach mit Bergen und Wald im Hintergrund", 960, 539),
        "mario_cta": True,
        "steps_bg": "/assets/img/lp-bg-module-abendsonne.jpg",
        "gallery": "GALLERY_PV_SPEICHER",
    },
    "order": ["hero", "problem", "system", "quote", "benefits", "steps", "gallery", "reviews", "contact", "faq",
              "footnote"],
    # alte LP: "PV komplett: Projektierung, Bau und Foerderabwicklung" mit Liste neben dem Modulfoto
    "problem": {
        "eyebrow": "Alles aus einer Hand",
        "h2": "PV komplett: Projektierung, Bau und Förderabwicklung",
        "paragraphs": [
            ("Ohne Speicher nutzen Sie rund 30 % Ihres Sonnenstroms selbst, mit passend geplantem Batteriespeicher "
             "60 bis 80 %.* Der Strom vom Mittag versorgt Ihr Haus dann auch am Abend und in der Nacht, mit "
             "Notstromfunktion auch bei Stromausfall."),
        ],
        "bullets_intro": "Ihr Komplettpaket:",
        "bullets": [
            "Photovoltaikanlage inklusive Speicher und Notstromlösung",
            "Beratung, Projektierung und komplette Bauabwicklung",
            "Förderberatung und Förderabwicklung inklusive",
            "Projektbericht mit 3D-Belegplan und Statikreport",
            "Anmeldung beim Netzbetreiber",
        ],
    },
    # alte LP: "Holen Sie sich die Kraft der Sonne" neben dem Ziegeldach-Foto
    "system": {
        "eyebrow": "Eigener Sonnenstrom",
        "h2": "Holen Sie sich die Kraft der Sonne",
        "paragraphs": [
            ("Immer mehr Hausbesitzer investieren lieber in eine Photovoltaik-Anlage, anstatt monatlich viel Geld an "
             "einen Stromkonzern zu überweisen."),
            ("<b>Sparen Sie sich monatlich hohe Stromkosten:</b> Mit eigenem Sonnenstrom und Speicher senken Sie Ihre "
             "Energiekosten um bis zu 85 %."),
            ("<b>Entlasten Sie die Umwelt:</b> Jede Kilowattstunde vom eigenen Dach ersetzt Strom aus dem Netz und "
             "entsteht im Betrieb ohne CO₂."),
            ("<b>Nutzen Sie Ihren Überschuss:</b> Was Sie nicht selbst verbrauchen, speisen Sie ins Netz ein und "
             "bekommen es vergütet, zum Beispiel über die OeMAG oder eine Energiegemeinschaft."),
            ("<b>Machen Sie Ihre Immobilie zukunftssicher:</b> Mit Speicher, Wallbox und später einer Wärmepumpe wächst "
             "Ihr Energiesystem mit."),
        ],
    },
    # alte LP: "All-in-One: Fuer Private und Gewerbe" mit Mario und Telefon
    "quote": ("All-in-One für Private und Gewerbe: Von der kostenlosen Besichtigung vor Ort bis zur Abwicklung Ihrer "
              "Förderung. Wir wickeln Ihr PV-Projekt schlüsselfertig für Sie ab."),
    # alte LP: "Mehr als nur saubere Energie" (Komponenten)
    "benefits": {
        "eyebrow": "Funktionell, schön und ganz schön clever",
        "h2": "Mehr als nur saubere Energie",
        "intro": ("Von eleganten Glas-Glas- und Black-Black-Modulen über den Batteriespeicher bis zur Wallbox für Ihre "
                  "Elektromobilität: Wir planen das System passend zu Ihrem Dach und Ihrem Verbrauch."),
        "cards": [
            ("☀", "Glas-Glas-Module",
             "Bifaziale Hochleistungs-Glas-Glas-Module der neuesten Generation sorgen für mehr Effizienz, eine höhere "
             "Lebensdauer und mehr Ästhetik auf Ihrem Dach."),
            ("⌂", "Ersatzziegel",
             "Ersatzziegel in der Farbe Ihrer Wahl halten Ihr Dach dicht, ohne Gefahr von Wassereintritt durch "
             "Ziegelbruch. Kein Flexen, kein Klopfen, keine Beschädigung Ihrer Dachstruktur."),
            ("◫", "Black-Black-Module",
             "Modulrahmen und Rückseitenfolie zwischen den Solarzellen sind schwarz. Black-Black-Module eignen sich "
             "daher vor allem für ein dunkles Hausdach."),
            ("▮", "Batteriespeicher mit Notstrom",
             "Der Hybridwechselrichter steuert den Speicher gleich mit. Auf Wunsch bleibt Ihr Haus auch bei Stromausfall "
             "versorgt."),
            ("⌖", "Wallboxen",
             "Laden Sie Ihr E-Auto bequem zu Hause: Die Wallbox nutzt den Strom, den Ihr Haus gerade nicht braucht, und "
             "macht das Laden günstig und weitgehend unabhängig vom Netz."),
            ("✓", "Garantierte Zufriedenheit",
             "Mindestens 10 Jahre Produktgarantie auf die Komponenten und bis zu 30 Jahre Leistungsgarantie auf die "
             "Module."),
        ],
    },
    # alte LP: "In drei Schritten zu Ihrer Photovoltaik-Anlage" auf Foto (Raster mit vier Spalten: Uebergabe als 4. Schritt)
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
    "gallery_h2": "Ihr Photovoltaik-Fachbetrieb für Kärnten und die Steiermark",
    "contact": {
        "h2": "Jetzt unverbindlich anfragen",
        "sub": ("Sagen Sie uns kurz, worum es geht: Eigenheim oder Betrieb, neue Anlage oder Speicher zum Nachrüsten. "
                "Wir melden uns innerhalb eines Werktags und vereinbaren einen Termin vor Ort."),
    },
    "faq": [
        ("Was kostet eine Photovoltaikanlage mit Batteriespeicher?",
         "Als Richtwert kostet eine Anlage mit 10 kWp und Speicher rund 15.000 bis 22.000 € vor Förderung.* Sie erhalten "
         "ein Festpreisangebot ohne versteckte Kosten."),
        ("Brauche ich einen Batteriespeicher?",
         "Ein Speicher hebt den Eigenverbrauch von rund 30 % auf bis zu 80 %. Sie nutzen Ihren Sonnenstrom dann auch am "
         "Abend und in der Nacht."),
        ("Funktioniert die Anlage bei einem Stromausfall?",
         "Nur, wenn sie notstromfähig geplant ist: Dafür braucht es einen notstromfähigen Hybridwechselrichter, einen "
         "freigegebenen Speicher und eine Umschalteinrichtung. Auf Wunsch planen wir das von Anfang an mit ein."),
        ("Kann ich einen Speicher bei meiner bestehenden Anlage nachrüsten?",
         "Ja, fast immer. Am flexibelsten ist die AC-Kopplung mit eigenem Batteriewechselrichter, der vorhandene "
         "Wechselrichter bleibt. Alternativ tauschen wir ihn gegen einen Hybridwechselrichter."),
        ("Welche Förderung bekomme ich?",
         "Das hängt von Bundesland, Anlagengröße und Speicher ab. Wir prüfen den aktuellen Förderstand für Ihr Projekt "
         "und übernehmen die Anträge."),
        ("Planen Sie auch Anlagen für Betriebe?",
         "Ja. Für Betriebe planen wir nach dem Lastprofil, mit Gewerbespeicher und Ladeinfrastruktur. Referenz: 40 kWp mit "
         "40 kWh Speicher in Oberösterreich sparen rund 13.500 € Stromkosten im Jahr."),
        ("Kann ich die Anlage finanzieren?",
         "Ja. Mit unserer Finanzierung gehört die Anlage ab dem ersten Tag Ihnen, ab 147 € im Monat inklusive Speicher.*"),
    ],
    "footnote": ("*Richtwerte und Beispielkonditionen, abhängig von Anlagengröße, Dach, Verbrauch und Laufzeit. "
                 "Verbindlich ist Ihr persönliches Angebot."),
}
