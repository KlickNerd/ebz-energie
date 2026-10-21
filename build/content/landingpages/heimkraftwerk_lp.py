"""Ads-Landingpage Heimkraftwerk (alte WP-Seite /heimkraftwerk-lp/, Stand 2025).

Botschaft der alten LP uebernommen (vollwertiges Heimkraftwerk: PV-Anlage mit Speicher als Komplettpaket
zum Festpreis, lange Garantie, Komplettservice, Projektbericht vor Baubeginn, drei Schritte). Korrigiert:
"30 Jahre Vollgarantie" / "15 Jahre auf Wechselrichter und Speicher" -> bis zu 30 Jahre Leistungsgarantie,
mind. 10 Jahre Produktgarantie; Paketdaten (10,68 kWp, 24 x 445 Wp) -> rund 10 kWp, 22 bis 25 Glas-Glas-Module
(build/pages/leistungen.py); "Landesfoerderung 2025 schnell sichern" -> allgemeiner Foerderhinweis;
"Made in Germany", Drohnenaufnahmen und "keine Vorauszahlungen" weggelassen (nicht freigegeben);
Statik- und Ertragsberechnungen -> Projektbericht mit 3D-Belegplan und Statikreport; Widmanngasse -> NAP.
"""

LP = {
    "path": "/heimkraftwerk-lp/",
    "title": "Heimkraftwerk: PV-Anlage mit Speicher zum Festpreis | EBZ",
    "description": ("Heimkraftwerk: PV-Anlage mit rund 10 kWp und Speicher, komplett mit Montage, Anmeldung und "
                    "Förderabwicklung zum Festpreis. Bis zu 30 Jahre Leistungsgarantie."),
    "eyebrow": "Photovoltaik mit Speicher für Ihr Zuhause",
    "h1": "Ihr Heimkraftwerk: Photovoltaikanlage mit Speicher, komplett zum Festpreis",
    "lead": ("Ein vollwertiges Heimkraftwerk mit rund 10 kWp, Batteriespeicher und auf Wunsch Notstrom, geplant, "
             "montiert und angemeldet vom Photovoltaik-Fachbetrieb aus Villach. Sie erhalten ein Festpreisangebot ohne "
             "versteckte Kosten und bis zu 30 Jahre Leistungsgarantie auf die Module."),
    "badges": [("bis 30 J.", "Leistungsgarantie"), ("Festpreis", "ohne versteckte Kosten"), ("4,9", "Sterne auf Google")],
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit dunklen Photovoltaikmodulen auf dem Satteldach vor Bergkulisse",
    "problem": {
        "eyebrow": "Komplett statt Stückwerk",
        "h2": "Ein Heimkraftwerk, ein Festpreis, ein Ansprechpartner",
        "paragraphs": [
            ("Ihr Heimkraftwerk besteht aus 22 bis 25 Glas-Glas-Modulen für rund 10 kWp, einem Hybridwechselrichter, "
             "der den Speicher gleich mitsteuert, und einem erweiterbaren Batteriespeicher aus Lithium-Eisenphosphat. "
             "Montiert wird dachschonend auf Ersatzziegeln statt auf geflexten Originalziegeln."),
            ("Im Festpreis enthalten: Unterkonstruktion, Komplettmontage mit Verkabelung, elektrischer Netzanschluss mit "
             "Dokumentation, Zählpunktansuchen und Fertigstellungsmeldung beim Netzbetreiber, die Förderabwicklung und "
             "ein Projektbericht mit 3D-Belegplan und Statikreport."),
        ],
    },
    "benefits": {
        "eyebrow": "Ihre Vorteile",
        "h2": "Ihre Vorteile beim Photovoltaik-Fachbetrieb aus Kärnten",
        "intro": "Hochwertige Komponenten, sauberes Handwerk und ein Ablauf, um den Sie sich nicht kümmern müssen.",
        "cards": [
            ("☀", "Glas-Glas-Module mit langer Garantie",
             "Bifaziale Glas-Glas-Module nutzen auch Licht von der Rückseite. Bis zu 30 Jahre Leistungsgarantie, "
             "mindestens 10 Jahre Produktgarantie."),
            ("▮", "Speicher für Abend und Nacht",
             "Mit Speicher steigt Ihr Eigenverbrauch auf bis zu 80 %, Sie senken Ihre Energiekosten um bis zu 85 %. "
             "Auf Wunsch versorgt die Anlage Ihr Haus auch bei Stromausfall."),
            ("✓", "Komplettservice",
             "Lieferung, Montage, Netzanschluss, Förderabwicklung und Anmeldung beim Netzbetreiber: alles aus einer Hand."),
            ("◎", "Projektbericht vor Baubeginn",
             "Belegplan mit realer Ausrichtung in 3D, Berechnung der Unterkonstruktion, Verschattung, Wind- und Schneelast: "
             "Sie sehen vorab genau, was auf Ihr Dach kommt."),
        ],
    },
    "steps": {
        "eyebrow": "So einfach geht es",
        "h2": "In vier Schritten zu Ihrem Heimkraftwerk",
        "steps": [
            ("Kontaktaufnahme",
             "Wir informieren Sie über Möglichkeiten, Kosten und Förderungen Ihres Projekts. Die Beratung ist kostenlos "
             "und unverbindlich.", "Tag 1"),
            ("Planung und Kalkulation",
             "Wir besichtigen Ihr Dach vor Ort. Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport und "
             "ein transparentes Festpreisangebot.", "ca. 1 Woche"),
            ("Förderung und Anmeldung",
             "Wir stellen die Förderanträge und melden die Anlage beim Netzbetreiber an.", "parallel"),
            ("Montage und Übergabe",
             "Zertifizierte Fachkräfte montieren Ihr Heimkraftwerk inklusive Speicher. Bei der Übergabe erklären wir Ihnen alles und bleiben "
             "danach Ihr Ansprechpartner.", "1 bis 3 Tage"),
        ],
    },
    "finance": True,
    "refs": ["villach", "krumpendorf", "gewerbe"],
    "contact": {
        "h2": "Jetzt unverbindlich anfragen",
        "sub": ("Sagen Sie uns kurz, wo Ihr Heimkraftwerk entstehen soll. Wir melden uns innerhalb eines Werktags und "
                "vereinbaren einen Termin vor Ort."),
    },
    "faq": [
        ("Was ist im Heimkraftwerk enthalten?",
         "Glas-Glas-Module für rund 10 kWp, Hybridwechselrichter, Batteriespeicher, Unterkonstruktion mit Ersatzziegeln, "
         "Komplettmontage, Netzanschluss mit Dokumentation, Anmeldung beim Netzbetreiber, Förderabwicklung und ein "
         "Projektbericht mit 3D-Belegplan und Statikreport. Notstrom planen wir auf Wunsch mit ein."),
        ("Was kostet ein Heimkraftwerk mit Speicher?",
         "Als Richtwert kostet eine Anlage mit 10 kWp und Speicher rund 15.000 bis 22.000 € vor Förderung.* Sie erhalten "
         "ein Festpreisangebot ohne versteckte Kosten, abgestimmt auf Ihr Dach und Ihren Verbrauch."),
        ("Welche Garantie bekomme ich?",
         "Bis zu 30 Jahre Leistungsgarantie auf die Module und mindestens 10 Jahre Produktgarantie. Bei Speichern geben "
         "die Hersteller üblicherweise 10 Jahre Garantie darauf, dass die Kapazität nicht unter 80 % fällt."),
        ("Funktioniert das Heimkraftwerk bei einem Stromausfall?",
         "Nur, wenn es notstromfähig geplant ist: Dafür braucht es einen notstromfähigen Hybridwechselrichter, einen "
         "freigegebenen Speicher und eine Umschalteinrichtung. Auf Wunsch planen wir das von Anfang an mit ein."),
        ("Kann ich den Speicher später erweitern?",
         "Ja, wir planen Speicher, die sich modular erweitern lassen. Wenn später Wärmepumpe oder E-Auto dazukommen, "
         "wächst Ihr Heimkraftwerk mit."),
        ("Welche Förderung bekomme ich?",
         "Das hängt von Bundesland, Anlagengröße und Speicher ab. Wir prüfen den aktuellen Förderstand für Ihr Projekt "
         "und übernehmen die Anträge."),
        ("Kann ich das Heimkraftwerk finanzieren?",
         "Ja. Mit unserer Finanzierung gehört die Anlage ab dem ersten Tag Ihnen, ab 147 € im Monat inklusive Speicher.*"),
    ],
    "finalcta": {
        "h2": "Holen Sie sich die Kraft der Sonne aufs eigene Dach",
        "text": "Der erste Schritt ist ein kostenloses Gespräch. Wir melden uns innerhalb eines Werktags.",
    },
    "footnote": ("*Richtwerte und Beispielkonditionen, abhängig von Anlagengröße, Dach und Laufzeit. Verbindlich ist Ihr "
                 "persönliches Angebot."),
}
