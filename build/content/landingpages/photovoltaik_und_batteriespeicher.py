"""Ads-Landingpage Photovoltaik und Batteriespeicher (alte WP-Seite /photovoltaik-und-batteriespeicher/, Stand 2024).

Botschaft der alten LP uebernommen (PV komplett mit Speicher und Notstrom: Projektierung, Bau und
Foerderabwicklung aus einer Hand, fuer Private und Gewerbe, Glas-Glas-Module, Ersatzziegel, Wallbox,
lange Garantie, drei Schritte). Korrigiert/weggelassen: "Kaernten, Salzburg und die Steiermark" -> Kaernten
und Steiermark (Montagegebiet), "20 % MwSt-Bundesfoerderung" / "MwSt-Befreiung bis 35 kWp" (ausgelaufen) und
Herbst-Aktion Gratis-Wallbox (abgelaufen), "schluesselfertig in rund 3 Monaten" (nicht freigegeben),
"6 bis 7 % Rendite durch Einspeisen" und CO2-Zahlen (nicht belegt), Infrarotheizungen (keine eigene Leistung),
Wertsteigerung der Immobilie (nicht belegt), Statik- und Energieertragsberechnungen -> Projektbericht mit
3D-Belegplan und Statikreport, Widmanngasse -> NAP.
"""

LP = {
    "path": "/photovoltaik-und-batteriespeicher/",
    "title": "Photovoltaik und Batteriespeicher komplett | EBZ Energie",
    "description": ("Photovoltaik und Batteriespeicher vom Fachbetrieb in Kärnten und der Steiermark: Planung, Montage, "
                    "Notstrom und Förderabwicklung aus einer Hand. Jetzt anfragen."),
    "eyebrow": "Photovoltaik und Batteriespeicher für Kärnten und die Steiermark",
    "h1": "Photovoltaik und Batteriespeicher komplett: Projektierung, Bau und Förderabwicklung aus einer Hand",
    "lead": ("Ihr Photovoltaik-Fachbetrieb aus Villach plant Ihre PV-Anlage mit Speicher und auf Wunsch Notstrom, "
             "montiert sie schlüsselfertig und übernimmt Förderabwicklung und Netzanmeldung. Sie senken Ihre "
             "Energiekosten um bis zu 85 %, ob im Eigenheim oder im Betrieb."),
    "badges": [("bis zu 80 %", "Eigenverbrauch mit Speicher"), ("300+", "Projekte"), ("4,9", "Sterne auf Google")],
    "hero_img": "pv_card",
    "hero_alt": "Photovoltaikmodule auf dem Dach eines Wohnhauses in ländlicher Umgebung",
    "problem": {
        "eyebrow": "Holen Sie sich die Kraft der Sonne",
        "h2": "Eigener Sonnenstrom statt monatlicher Überweisung an den Stromkonzern",
        "paragraphs": [
            ("Immer mehr Hausbesitzer investieren lieber in eine eigene Photovoltaikanlage, statt Monat für Monat viel "
             "Geld an einen Stromkonzern zu überweisen. Jede Kilowattstunde, die Sie selbst verbrauchen, müssen Sie "
             "nicht teuer aus dem Netz kaufen."),
            ("Ohne Speicher nutzen Sie rund 30 % Ihres Sonnenstroms selbst, mit passend geplantem Batteriespeicher "
             "60 bis 80 %.* Der Strom vom Mittag versorgt Ihr Haus dann auch am Abend und in der Nacht, mit "
             "Notstromfunktion auch bei Stromausfall."),
        ],
    },
    "benefits": {
        "eyebrow": "Mehr als nur saubere Energie",
        "h2": "Funktionell, schön und ganz schön clever",
        "intro": ("Von Glas-Glas-Modulen bis zur Wallbox für Ihr E-Auto: Wir planen das System passend zu Ihrem Dach "
                  "und Ihrem Verbrauch."),
        "cards": [
            ("☀", "Glas-Glas-Module",
             "Bifaziale Glas-Glas-Module nutzen auch Licht von der Rückseite, sind langlebig und auf Wunsch in "
             "Full-Black-Optik für dunkle Dächer erhältlich."),
            ("⌂", "Dachschonende Montage",
             "Wir montieren auf Ersatzziegeln statt auf geflexten Originalziegeln: kein Flexen, kein Klopfen, keine "
             "Beschädigung Ihrer Dachstruktur."),
            ("▮", "Batteriespeicher mit Notstrom",
             "Der Hybridwechselrichter steuert den Speicher gleich mit. Auf Wunsch bleibt Ihr Haus auch bei Stromausfall "
             "versorgt."),
            ("⌖", "Wallbox fürs E-Auto",
             "Mit Überschussladen tanken Sie Ihr Auto bevorzugt dann, wenn das Dach mehr liefert als das Haus braucht."),
        ],
    },
    "quote": ("Von der kostenlosen Besichtigung vor Ort bis zur Abwicklung Ihrer Förderung: Wir setzen Ihr PV-Projekt "
              "schlüsselfertig für Sie um, für Private und für Betriebe."),
    "steps": {
        "eyebrow": "So einfach geht es",
        "h2": "In vier Schritten zu Ihrer Photovoltaikanlage",
        "steps": [
            ("Kontaktaufnahme",
             "Wir informieren Sie über Möglichkeiten, Kosten und Förderungen Ihres Projekts. Die Beratung ist kostenlos "
             "und unverbindlich.", "Tag 1"),
            ("Planung und Kalkulation",
             "Wir besichtigen vor Ort. Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport und ein "
             "transparentes Festpreisangebot.", "ca. 1 Woche"),
            ("Förderung und Anmeldung",
             "Wir stellen die Förderanträge und melden die Anlage beim Netzbetreiber an.", "parallel"),
            ("Montage und Übergabe",
             "Zertifizierte Fachkräfte montieren Ihre Anlage inklusive Batteriespeicher. Bei der Übergabe erklären wir Ihnen alles und bleiben "
             "danach Ihr Ansprechpartner.", "1 bis 3 Tage"),
        ],
    },
    "finance": True,
    "refs": ["villach", "krumpendorf", "gewerbe"],
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
    "finalcta": {
        "h2": "Wie viele Sonnenstunden wollen Sie noch ungenutzt lassen?",
        "text": "Der erste Schritt ist ein kostenloses Gespräch. Wir melden uns innerhalb eines Werktags.",
    },
    "footnote": ("*Richtwerte und Beispielkonditionen, abhängig von Anlagengröße, Dach, Verbrauch und Laufzeit. "
                 "Verbindlich ist Ihr persönliches Angebot."),
}
