"""Ads-Landingpage Photovoltaik Gewerbe (alte WP-Seite /photovoltaik-gewerbe-lp/, Stand Mai 2026).

Botschaft der alten LP uebernommen (Betriebskosten senken, Kalkulationssicherheit, PV + Speicher +
Ladeinfrastruktur, alles aus einer Hand, Steuer, Image/ESG, Betrieb laeuft weiter). Korrigiert:
"bis zu 70 %" -> freigegebener Claim bis zu 85 %, Leasing ab 147 €/Zusage in 24 Stunden/ohne
Bonitaetspruefung/Servicevertrag -> Finanzierung (Eigentum ab Tag 1, nur in der FAQ, kein Privat-Band),
eigene Montageteams/Techniker -> zertifizierte Fachkraefte, Ertragsprognose und Wirtschaftlichkeitsberechnung
-> Lastprofil-Analyse und Projektbericht, Investitionspraemie/EAG/AfA 20 Jahre -> allgemeiner Foerder- und
Steuerhinweis, "100 Anlagen pro Jahr" -> 300+ Projekte, Widmanngasse -> NAP, Amortisation 6 bis 10 Jahre ->
4 bis 6 Jahre aus den Referenzen*. Zahlen aus CLAUDE.md und build/pages/pv_gewerbe.py.
"""

LP = {
    "path": "/photovoltaik-gewerbe-lp/",
    "title": "Photovoltaik für Unternehmen: schlüsselfertig | EBZ Energie",
    "description": ("Photovoltaik für Ihr Unternehmen mit Speicher und Ladeinfrastruktur: Planung nach Lastprofil, "
                    "Förderabwicklung und Montage aus einer Hand. Jetzt anfragen."),
    "eyebrow": "Photovoltaik für Gewerbe, Landwirtschaft und Hotellerie",
    "h1": "Photovoltaik für Ihr Unternehmen: schlüsselfertig, mit Förderabwicklung und aus einer Hand",
    "lead": ("Senken Sie Ihre Stromkosten um bis zu 85 %, gewinnen Sie Kalkulationssicherheit und machen Sie Ihren "
             "Betrieb zukunftssicher. EBZ Energie plant und errichtet Ihre gewerbliche PV-Anlage mit Speicher, "
             "Lastmanagement und Ladeinfrastruktur. Förderabwicklung und Netzanmeldung übernehmen wir für Sie."),
    "badges": [("13.500 €", "Ersparnis pro Jahr, Referenz 40 kWp"), ("300+", "Projekte"), ("4,9", "Sterne auf Google")],
    "hero_img": "gen_gewerbe",
    "hero_alt": "Gewerbehalle mit großflächiger Photovoltaikanlage auf dem Dach vor Bergkulisse",
    "cta": "Kostenlose Besichtigung anfragen",
    "problem": {
        "eyebrow": "Das Problem",
        "h2": "Strom ist einer Ihrer größten Kostenfaktoren, und Sie haben keine Kontrolle darüber",
        "paragraphs": [
            ("Ob Produktion, Hotel, Werkstatt, Landwirtschaft, Logistik oder Büro: Strom gehört in fast jedem "
             "Unternehmen zu den größten laufenden Ausgaben. Ihre Margen sind kalkuliert, die Strompreise nicht. "
             "Jeder neue Vertrag mit dem Energieversorger wird so zum Risiko für Ihre Kalkulation."),
            ("Dabei haben viele Betriebe etwas, das an jedem Sonnentag Geld wert ist: ungenutzte Dach- und "
             "Hallenflächen. Mit einer eigenen PV-Anlage produzieren Sie Ihren Strom genau dort, wo Sie ihn brauchen, "
             "und genau dann, wenn Ihr Betrieb läuft."),
        ],
    },
    "benefits": {
        "eyebrow": "Ihre Vorteile",
        "h2": "Ihre Hallenfläche ist ein ungenutztes Kraftwerk",
        "intro": ("Ihr Strombedarf ist tagsüber am höchsten, genau dann, wenn die Sonne scheint. Betriebe erreichen "
                  "deshalb ohne Speicher Eigenverbrauchsquoten von 70 % und mehr.* Speicher und Ladeinfrastruktur "
                  "decken Lastspitzen, Schichtbetrieb und Firmenflotte ab."),
        "cards": [
            ("€", "Stromkosten deutlich senken",
             "Bis zu 85 % weniger Stromkosten. Referenz: 40 kWp mit Speicher in Oberösterreich sparen rund 13.500 € im Jahr. "
             "In unseren Projekten amortisieren sich Anlagen typischerweise nach 4 bis 6 Jahren.*"),
            ("◎", "Kalkulationssicherheit gewinnen",
             "Selbst erzeugter Strom kostet über 25 Jahre gerechnet rund 4 bis 7 Cent je kWh inklusive Betrieb.* "
             "Diesen Teil Ihrer Energiekosten kennen Sie schon heute."),
            ("✓", "Steuerlich günstig",
             "Die Anlage ist Betriebsvermögen und wird abgeschrieben, die Vorsteuer ist abziehbar, auf Eigenstrom entfällt "
             "die Elektrizitätsabgabe. Für Ihre Steuerberatung liefern wir die Zahlen."),
            ("☀", "Nachhaltig mit greifbaren Zahlen",
             "Nachhaltigkeit zählt bei Ausschreibungen, Lieferantenbewertungen und im Recruiting. Das Monitoring liefert "
             "die Energiedaten für Ihr ESG-Reporting."),
        ],
    },
    "quote": ("Von der Lastprofil-Analyse über die Förderabwicklung bis zur Inbetriebnahme: Wir setzen Ihre gewerbliche "
              "PV-Anlage schlüsselfertig um, während Ihr Betrieb weiterläuft."),
    "steps": {
        "eyebrow": "So einfach geht es",
        "h2": "In 4 Schritten zu Ihrer gewerblichen PV-Anlage",
        "steps": [
            ("Kostenlose und ehrliche Beratung",
             "Wir sehen uns Lastprofil, Stromtarif, Dach- und Hallenflächen und Ihre Pläne an und sagen Ihnen ehrlich, "
             "welche Größe sich für Ihren Betrieb rechnet.", "Woche 1"),
            ("Planung nach Maß",
             "Wir prüfen vor Ort Statik, Elektroinfrastruktur und Netzanschluss. Sie erhalten einen Projektbericht mit "
             "3D-Belegplan und Statikreport und ein transparentes Angebot ohne versteckte Kosten.", "1 bis 2 Wochen"),
            ("Wir erledigen die Bürokratie",
             "Förderanträge, Netzanmeldung, Zählpunkte und Abstimmung mit dem Netzbetreiber übernehmen wir. Sie "
             "konzentrieren sich auf Ihr Kerngeschäft.", "parallel"),
            ("Montage und Inbetriebnahme",
             "Zertifizierte Fachkräfte montieren abgestimmt auf Ihre Betriebszeiten. Danach erhalten Sie Monitoring, "
             "Einschulung und einen festen Ansprechpartner.", "wenige Tage bis 2 Wochen"),
        ],
    },
    "why": {
        "eyebrow": "Warum EBZ Energie",
        "h2": "Darum entscheiden sich Betriebe für EBZ Energie",
        "items": [
            ("☀", "Alles aus einer Hand",
             "Ein Ansprechpartner für Planung, Statik, Elektrotechnik, Montage und Inbetriebnahme. Kein Schnittstellen-Chaos zwischen mehreren Gewerken."),
            ("✓", "Zertifizierte Fachkräfte", "Meisterhaftes Handwerk und sorgfältige Ausführung nach österreichischen Normen."),
            ("€", "Förderabwicklung inklusive",
             "Wir prüfen den aktuellen Förderstand für Ihr Projekt und übernehmen die Anträge."),
            ("◇", "Bis zu 30 Jahre Garantie",
             "Bis zu 30 Jahre Leistungsgarantie auf die Module, mindestens 10 Jahre Produktgarantie."),
            ("◎", "Volle Transparenz",
             "Projektbericht mit 3D-Belegplan und Statikreport, klare Kostenaufstellung ohne Überraschungen."),
            ("◉", "300+ Projekte",
             "Erfahrung aus über 300 dokumentierten Projekten in 6 Bundesländern, vom Eigenheim bis zum Gewerbedach."),
        ],
    },
    "finance": False,
    "refs": ["gewerbe", "krumpendorf", "villach"],
    "refs_h2": "Echte Projekte, echte Ergebnisse",
    "contact": {
        "h2": "Kostenlose Besichtigung für Ihren Betrieb",
        "sub": ("Sagen Sie uns kurz, um welchen Betrieb und welche Dachfläche es geht. Wir melden uns innerhalb eines "
                "Werktags, sehen uns Lastprofil und Dach an und sagen Ihnen ehrlich, was sich rechnet."),
    },
    "faq": [
        ("Lohnt sich Photovoltaik wirklich für mein Unternehmen?",
         "In den meisten Fällen ja. Betriebe verbrauchen den Großteil ihres Stroms tagsüber und erreichen ohne Speicher "
         "Eigenverbrauchsquoten von 70 % und mehr.* Entscheidend sind Lastprofil, Dachfläche und Stromtarif. In unseren "
         "Projekten amortisieren sich Anlagen typischerweise nach 4 bis 6 Jahren, das Hotel in Villach/Warmbad nach rund "
         "6 Jahren.* Die Module liefern danach noch viele Jahre Strom."),
        ("Welche Förderungen gibt es für Betriebe?",
         "Das hängt von Bundesland, Anlagengröße, Speicher und Energiemanagement ab, und die Programme ändern sich laufend. "
         "Wir prüfen den aktuellen Förderstand für Ihr Projekt und übernehmen die Anträge, rechtzeitig vor der Bestellung."),
        ("Wie lange dauert die Montage und stört das den laufenden Betrieb?",
         "Je nach Anlagengröße dauert die Montage wenige Tage bis zwei Wochen. Wir planen die Arbeiten in Abstimmung mit "
         "Ihren Betriebszeiten, etwa in Randzeiten oder Produktionspausen, damit Ihr Betrieb möglichst ungestört weiterläuft."),
        ("Wie wird eine Gewerbe-PV-Anlage steuerlich behandelt?",
         "Die Anlage ist Betriebsvermögen und wird über die Nutzungsdauer abgeschrieben, laufende Kosten sind "
         "Betriebsausgaben, die Vorsteuer ist abziehbar. Selbst erzeugter und verbrauchter Strom ist von der "
         "Elektrizitätsabgabe befreit. Die Details klären Sie mit Ihrer Steuerberatung, wir liefern die Zahlen."),
        ("Können wir die Anlage finanzieren statt kaufen?",
         "Ja. Bei EBZ Energie gehört die Anlage ab dem ersten Tag Ihrem Unternehmen. Wer die Liquidität im Betrieb "
         "behalten will, finanziert zur fixen Rate mit 0 € Anzahlung; Abschreibung und Vorsteuerabzug laufen wie beim Kauf."),
        ("Wie groß sollte eine Gewerbe-PV-Anlage sein?",
         "Die Größe richtet sich nach Ihrem Lastprofil, nicht nur nach der Dachfläche. Ein Gewerbespeicher lohnt sich bei "
         "teuren Lastspitzen, Verbrauch am Abend oder Wochenende und wenn Kühlung oder Server bei Netzausfall weiterlaufen müssen."),
        ("Was passiert nach der Installation?",
         "Sie erhalten ein Monitoring, das Ertrag und Verbrauch zeigt, und einen festen Ansprechpartner für Service und "
         "Fragen. Die Betreuung endet bei uns nicht mit der Inbetriebnahme."),
    ],
    "finalcta": {
        "h2": "Wie viel Marge wollen Sie weiterhin an Ihren Energieversorger verlieren?",
        "text": ("Der erste Schritt zu kalkulierbaren Energiekosten ist ein kostenloses Gespräch. Wir melden uns innerhalb "
                 "eines Werktags."),
    },
    "footnote": ("*Richtwerte aus EBZ-Projekten (Gewerbe Oberösterreich, Hotel Villach/Warmbad) und Marktrichtwerten 2026, "
                 "abhängig von Lastprofil, Anlagengröße, Ausrichtung und Strompreis. Steuerliche Angaben ersetzen keine "
                 "Steuerberatung. Verbindlich ist Ihr persönliches Angebot."),
}
