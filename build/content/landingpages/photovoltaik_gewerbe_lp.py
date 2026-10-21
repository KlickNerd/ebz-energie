"""Ads-Landingpage Photovoltaik Gewerbe (alte WP-Seite /photovoltaik-gewerbe-lp/, Stand Mai 2026).

Aufbau wie das Muster /photovoltaik-privat-lp/ und wie die alte LP: Hero auf Foto, Bewertungen, Problem mit
Hotel-Referenzbild und 4 Punkten, Energiesystem-Text mit den 4 Karten (die alte Gewerbe-Grafik mit
"70 bis 90 %" ist nicht freigegeben, deshalb Text in den Karten), Mario-Zitat mit Button, 4 Schritte auf Foto,
Warum EBZ, Finanzierung mit Bild, Galerie 2023, Schluss-Aufruf mit Mario, Formular, FAQ.

Finanzierung: Der Standard-Finanzierungsblock nennt die private Rate (ab 147 € inkl. Speicher) und die
Privatfoerderung. Fuer Gewerbe gilt beides nicht, deshalb ist "finance" ein eigener Text ohne Rate
(Bild: Geldscheine vor Haus wie auf der alten LP).

Korrigiert: Leasing ab 147 €, Eigentumsuebergang nach Laufzeit, Servicevertrag, Zusage in 24 Stunden, ohne
Bonitaetspruefung -> Finanzierung, Eigentum ab Tag 1, keine Rate; "bis zu 70 %" bzw. "50 bis 70 %" -> bis zu 85 %;
"70 bis 90 Prozent Eigenverbrauch" -> 70 % und mehr* (wie pv_gewerbe.py); Amortisation 6 bis 10 Jahre -> 4 bis 6
Jahre aus den Referenzen*; Investitionspraemie/EAG/AfA 20 Jahre/Steueroptimierung -> Foerderstand wird geprueft,
allgemeiner Steuerhinweis; Ertragsprognose, Amortisations- und Wirtschaftlichkeitsberechnung -> Projektbericht
mit 3D-Belegplan und Statikreport, Lastprofil-Analyse; Techniker/eigene Montageteams -> zertifizierte Fachkraefte;
"100 Anlagen pro Jahr in ganz Oesterreich" -> 300+ Projekte in 6 Bundeslaendern; "ganz Oesterreich" als
Einsatzgebiet -> Kaernten und Steiermark; "Foerderungen sind begrenzt" entfernt; Widmanngasse -> NAP.
Hotel-Bild nur mit den freigegebenen Hotel-Zahlen (CLAUDE.md).
"""

_I = "/assets/img/"

LP = {
    "path": "/photovoltaik-gewerbe-lp/",
    "title": "Photovoltaik für Unternehmen: schlüsselfertig | EBZ Energie",
    "description": ("Photovoltaik für Ihr Unternehmen mit Speicher und Ladeinfrastruktur: Planung nach Lastprofil, "
                    "Förderabwicklung und Montage aus einer Hand. Jetzt anfragen."),
    "eyebrow": "Sagen Sie Ihren Betriebskosten den Kampf an",
    "h1": "Photovoltaik für Ihr Unternehmen: schlüsselfertig, mit Förderabwicklung und aus einer Hand",
    "lead": ("Senken Sie Ihre Stromkosten um bis zu 85 %, gewinnen Sie Kalkulationssicherheit und machen Sie Ihr "
             "Unternehmen zukunftssicher. EBZ Energie plant, errichtet und betreut Ihre gewerbliche PV-Anlage, "
             "inklusive Speicher, Lastmanagement und Ladeinfrastruktur. Förderabwicklung, Netzanmeldung und "
             "Bürokratie übernehmen wir für Sie."),
    "badges": [("13.500 €", "Ersparnis pro Jahr, Referenz 40 kWp"), ("300+", "Projekte"), ("4,9", "Sterne auf Google")],
    "hero_img": "gen_gewerbe",
    "hero_alt": "Gewerbehalle mit großflächiger Photovoltaikanlage auf dem Dach vor Bergkulisse",
    "cta": "Kostenlose Besichtigung anfragen",
    "media": {
        "hero_bg": _I + "lp-hero-gewerbe-alpen.jpg",
        "problem_img": (_I + "lp-hotel-villach-luftbild.jpg",
                        "Luftaufnahme eines Hotels in Villach mit Photovoltaikanlage auf dem Dach"),
        "finance_img": (_I + "lp-finanzierung-haus.jpg", "Geldscheine vor einem Gebäude mit Photovoltaikanlage"),
        "mario": False,
        "mario_cta": True,
        "steps_bg": _I + "lp-bg-module-abendsonne.jpg",
        "gallery": "GALLERY_2023",
        "final_mario": True,
    },
    "order": ["hero", "reviews", "problem", "benefits", "quote", "steps", "why", "finance", "refs", "gallery",
              "final", "contact", "faq", "footnote"],
    "problem": {
        "eyebrow": "Das Problem",
        "h2": "Strom ist einer Ihrer größten Kostenfaktoren, und Sie haben keine Kontrolle darüber",
        "paragraphs": [
            ("Egal ob produzierender Betrieb, Hotel, Werkstatt, Landwirtschaft, Logistik oder Bürogebäude: Strom gehört "
             "in fast jedem Unternehmen zu den größten laufenden Ausgaben. Und während Ihre Margen kalkuliert sind, "
             "können Sie die Strompreise nicht kalkulieren."),
            ("Diese Abhängigkeit vom Energiemarkt frisst Ihre Marge, erschwert die langfristige Kalkulation und macht "
             "jeden neuen Vertrag mit Ihrem Energieversorger zum Risiko. Dabei haben viele Betriebe etwas, das an jedem "
             "Sonnentag bares Geld wert ist: ungenutzte Dach- oder Hallenflächen."),
            ("Im Bild: ein Hotel in Villach/Warmbad mit 13 kWp bifazialen Modulen und 27 kWh Speicher. Die Anlage "
             "liefert rund 15.000 kWh im Jahr, spart rund 4.200 € pro Jahr und hat sich nach rund 6 Jahren bezahlt gemacht."),
        ],
        "bullets_intro": ("Es gibt einen besseren Weg, erprobt und betriebswirtschaftlich überzeugend: "
                          "Ihre eigene gewerbliche PV-Anlage."),
        "bullets": [
            ("<b>Das perfekte Trio für Unternehmen:</b> PV-Anlage, Speicher und Ladeinfrastruktur. Sie produzieren, "
             "speichern und nutzen Ihren eigenen Sonnenstrom genau dann, wenn Ihr Betrieb läuft."),
            ("<b>Alles aus einer Hand:</b> ein Ansprechpartner für Planung, Statik, Elektrotechnik, Montage und "
             "Inbetriebnahme. Kein Schnittstellen-Chaos zwischen mehreren Gewerken."),
            ("<b>Förderabwicklung inklusive:</b> Wir prüfen den aktuellen Förderstand für Ihr Projekt und übernehmen "
             "die Anträge. Für Ihre Steuerberatung liefern wir die Zahlen."),
            ("<b>Sicher entscheiden:</b> kostenlose Lastgang-Analyse und technische Machbarkeitsprüfung direkt bei "
             "Ihnen vor Ort."),
        ],
    },
    "benefits": {
        "eyebrow": "Photovoltaik im Gewerbe",
        "h2": "Photovoltaik im Gewerbe: das moderne und wirtschaftliche Energiesystem für Ihr Unternehmen",
        "intro": ("Statt teuren Strom einzukaufen, produzieren Sie ihn dort, wo Sie ihn brauchen: auf Ihrem eigenen Dach. "
                  "Eine moderne gewerbliche PV-Anlage wandelt Sonnenlicht direkt in elektrische Energie um, sauber, leise "
                  "und über 25 Jahre und länger zuverlässig."
                  "<br><br>"
                  "Der entscheidende Vorteil im Gewerbe: Ihr Strombedarf ist tagsüber am höchsten, genau dann, wenn auch "
                  "die Sonne scheint. Betriebe erreichen deshalb Eigenverbrauchsquoten von 70 % und mehr direkt aus der "
                  "Anlage, ganz ohne Speicher.* Mit einem zusätzlichen Stromspeicher decken Sie Lastspitzen ab und nutzen "
                  "den Sonnenstrom auch im Zwei- oder Drei-Schicht-Betrieb am Abend. Mit einer gewerblichen "
                  "Ladeinfrastruktur versorgen Sie Ihre Firmenflotte, Mitarbeiterfahrzeuge oder Kundenparkplätze."
                  "<br><br>"
                  "Für Sie bedeutet das: Ihre Stromkosten sinken deutlich und werden langfristig kalkulierbar. Sie nutzen "
                  "steuerliche Abschreibungen, und wir prüfen die Förderungen für Ihr Projekt. Und Sie positionieren Ihr "
                  "Unternehmen als zukunftsorientiert und nachhaltig, ein Faktor, der bei Kunden, Mitarbeitenden und im "
                  "ESG-Reporting immer wichtiger wird."
                  "<br><br>"
                  "<b>Ihre Hallenfläche ist ein ungenutztes Kraftwerk, und wir machen sie für Sie nutzbar.</b>"),
        "cards": [
            ("€", "Stromkosten deutlich senken",
             "Eine gewerbliche PV-Anlage senkt Ihre Stromkosten um bis zu 85 %. Referenz: 40 kWp mit Speicher in "
             "Oberösterreich sparen rund 13.500 € im Jahr. In unseren Projekten amortisieren sich Anlagen typischerweise "
             "nach 4 bis 6 Jahren* und produzieren danach noch viele Jahre günstigen Strom."),
            ("◎", "Kalkulationssicherheit gewinnen",
             "Sie wissen schon heute, was Ihr selbst erzeugter Strom in 5, 10 oder 20 Jahren kostet: über 25 Jahre "
             "gerechnet rund 4 bis 7 Cent je kWh inklusive Betrieb.* Diese Planbarkeit ist im aktuellen Energieumfeld "
             "viel wert, gerade für mittel- und langfristige Angebotskalkulationen."),
            ("✓", "Steuerliche Vorteile nutzen",
             "Die Anlage ist Betriebsvermögen und wird über die Nutzungsdauer abgeschrieben, die Vorsteuer ist abziehbar, "
             "auf selbst verbrauchten Strom entfällt die Elektrizitätsabgabe. Wir stimmen uns mit Ihrer Steuerberatung ab "
             "und liefern die Zahlen, damit Sie das Potenzial ausschöpfen."),
            ("☀", "Imagegewinn als nachhaltiges Unternehmen",
             "Nachhaltigkeit ist längst kein Nice-to-have mehr, sondern ein harter Wettbewerbsfaktor bei Ausschreibungen, "
             "Lieferantenbewertungen und im Recruiting. Mit einer eigenen PV-Anlage liefern Sie greifbare Zahlen für Ihr "
             "ESG-Reporting und positionieren sich als Vorreiter in Ihrer Branche."),
        ],
    },
    "quote": ("Von der ersten Lastprofil-Analyse über die Förderabwicklung bis zur Inbetriebnahme: Wir setzen Ihre "
              "gewerbliche PV-Anlage schlüsselfertig um, während Ihr Betrieb weiterläuft."),
    "steps": {
        "eyebrow": "So einfach geht es",
        "h2": "Ihr Weg zur Energieunabhängigkeit mit EBZ: in 4 einfachen Schritten",
        "steps": [
            ("Kostenlose und ehrliche Beratung",
             "Wir analysieren Ihren Lastgang, Ihren aktuellen Stromtarif, Ihre Dach- und Hallenflächen und Ihre "
             "langfristigen Pläne. Sie erhalten eine ehrliche Einschätzung, in welcher Größe und Konfiguration sich eine "
             "PV-Anlage für Ihren Betrieb wirklich rechnet.", "Woche 1"),
            ("Maßgeschneiderte Planung",
             "Wir kommen zu Ihnen vor Ort und prüfen Statik, Elektroinfrastruktur und Anschlussmöglichkeiten. Sie "
             "erhalten einen Projektbericht mit 3D-Belegplan und Statikreport und ein transparentes Angebot ohne "
             "versteckte Kosten.", "1 bis 2 Wochen"),
            ("Wir erledigen die Bürokratie",
             "Förderanträge, Anmeldung beim Netzbetreiber, Behördenkommunikation und Genehmigungen übernehmen wir, die "
             "Zahlen für Ihre Steuerberatung liefern wir mit. Sie können sich auf Ihr Kerngeschäft konzentrieren.",
             "parallel"),
            ("Installation und Inbetriebnahme",
             "Zertifizierte Fachkräfte installieren Ihre PV-Anlage so, dass Ihr Betriebsablauf möglichst nicht gestört "
             "wird. Nach der Inbetriebnahme erhalten Sie ein Monitoring mit Fernüberwachung und einen festen "
             "Ansprechpartner für die kommenden Jahre.", "wenige Tage bis 2 Wochen"),
        ],
    },
    "why": {
        "eyebrow": "Warum EBZ Energie",
        "h2": "Darum sollten Sie sich für EBZ entscheiden: Ihr Energie-Partner für Kärnten und die Steiermark",
        "items": [
            ("☀", "Photovoltaik aus einer Hand",
             "Ein Ansprechpartner, ein Vertrag: für PV-Anlage, Speicher und Ladeinfrastruktur. Kein Schnittstellen-Chaos "
             "zwischen mehreren Gewerken."),
            ("✓", "Zertifizierte Fachkräfte", "Meisterhaftes Handwerk und sorgfältige Ausführung nach österreichischen Normen."),
            ("€", "Komplette Förderabwicklung",
             "Wir prüfen den aktuellen Förderstand für Ihr Projekt und übernehmen die Anträge."),
            ("◇", "Bis zu 30 Jahre Leistungsgarantie",
             "Mindestens 10 Jahre Produktgarantie und bis zu 30 Jahre Leistungsgarantie auf die Module."),
            ("◎", "Volle Transparenz",
             "Projektbericht mit 3D-Belegplan und Statikreport und eine klare Kostenaufstellung ohne Überraschungen."),
            ("⌂", "Regionale Expertise",
             "Zuhause in Villach, im Einsatz in Kärnten und der Steiermark, mit über 300 dokumentierten Projekten in "
             "6 Bundesländern."),
        ],
    },
    # Finanzierung fuer Gewerbe: eigener Text ohne die Privat-Rate (147 € gilt fuer die private Komplettanlage)
    "finance": {
        "eyebrow": "Finanzierung für Unternehmen",
        "h2": "Gewerbliche Photovoltaik finanzieren, ganz ohne Eigenkapital",
        "paragraphs": [
            ("Eine eigene PV-Anlage ist eine der besten Investitionen, die Sie für Ihr Unternehmen treffen können. Aber "
             "gerade in wirtschaftlich anspruchsvollen Zeiten möchten viele Betriebe ihr Eigenkapital nicht binden, "
             "sondern im Kerngeschäft arbeiten lassen. Genau dafür bietet EBZ Energie eine Finanzierung für Gewerbekunden."),
            ("Ob PV-Anlage, Speicher, Wärmepumpe oder Ladeinfrastruktur: Wir finanzieren jede Komponente, einzeln oder "
             "im Paket. Die Konditionen für Ihr Unternehmen nennen wir Ihnen mit dem Angebot."),
        ],
        "bullets": [
            "0 € Anzahlung, fixe Rate über die gesamte Laufzeit",
            "Die Anlage gehört von Beginn an Ihrem Unternehmen",
            "Einzeln oder im Paket: PV, Speicher, Wärmepumpe, Ladeinfrastruktur",
            "Förderstand geprüft, Anträge übernehmen wir",
        ],
    },
    "refs": ["gewerbe", "krumpendorf", "villach"],
    "refs_h2": "Echte Projekte, echte Zahlen",
    "gallery_h2": "Echte Projekte, echte Ergebnisse, aus Ihrer Region",
    "contact": {
        "h2": "Kostenlose Besichtigung für Ihren Betrieb",
        "sub": ("Sagen Sie uns kurz, um welchen Betrieb und welche Dachfläche es geht. Wir melden uns innerhalb eines "
                "Werktags, sehen uns Lastprofil und Dach an und sagen Ihnen ehrlich, was sich rechnet."),
    },
    "faq": [
        ("Lohnt sich Photovoltaik wirklich für mein Unternehmen?",
         "In den allermeisten Fällen ja, und oft schneller, als viele erwarten. Betriebe verbrauchen den Großteil ihres "
         "Stroms tagsüber und erreichen ohne Speicher Eigenverbrauchsquoten von 70 % und mehr.* Entscheidend sind "
         "Lastprofil, Dach- oder Freiflächen und Stromtarif. In unseren Projekten amortisieren sich Anlagen "
         "typischerweise nach 4 bis 6 Jahren, das Hotel in Villach/Warmbad nach rund 6 Jahren.* Die Module liefern "
         "danach noch viele Jahre günstigen Strom. Wir beraten Sie kostenlos und ohne Verkaufsdruck."),
        ("Welche Förderungen gibt es speziell für Betriebe?",
         "Das hängt von Bundesland, Anlagengröße, Branche, Speicher und Energiemanagement ab, und die Programme ändern "
         "sich laufend. Wir prüfen den aktuellen Förderstand für Ihr Projekt und übernehmen die Anträge, rechtzeitig "
         "vor der Bestellung."),
        ("Wie lange dauert die Installation und stört das den laufenden Betrieb?",
         "Je nach Anlagengröße dauert die Montage meist wenige Tage bis zwei Wochen. Wir planen die Arbeiten so, dass "
         "Ihr Betrieb möglichst nicht beeinträchtigt wird, etwa am Wochenende, in Randzeiten oder abgestimmt auf Ihre "
         "Produktionsfenster. Ihre Mitarbeitenden und Kunden bekommen davon in der Regel kaum etwas mit."),
        ("Wie sieht die steuerliche Behandlung einer Gewerbe-PV-Anlage aus?",
         "Die Anlage ist Betriebsvermögen und wird über die Nutzungsdauer abgeschrieben, laufende Kosten sind "
         "Betriebsausgaben, die Vorsteuer ist abziehbar. Selbst erzeugter und verbrauchter Strom ist von der "
         "Elektrizitätsabgabe befreit. Die Details klären Sie mit Ihrer Steuerberatung, wir liefern die Zahlen."),
        ("Können wir die Anlage finanzieren statt kaufen?",
         "Ja. Bei EBZ Energie gehört die Anlage ab dem ersten Tag Ihrem Unternehmen. Wer die Liquidität im Betrieb "
         "behalten will, finanziert zur fixen Rate mit 0 € Anzahlung; Abschreibung und Vorsteuerabzug laufen wie beim "
         "Kauf. Die Konditionen für Ihr Projekt nennen wir Ihnen mit dem Angebot."),
        ("Wie groß sollte eine Gewerbe-PV-Anlage sein?",
         "Die Größe richtet sich nach Ihrem Lastprofil, nicht nur nach der Dachfläche. Ein Gewerbespeicher lohnt sich bei "
         "teuren Lastspitzen, Verbrauch am Abend oder Wochenende und wenn Kühlung oder Server bei Netzausfall weiterlaufen müssen."),
        ("Was passiert nach der Installation?",
         "Wir bleiben Ihr Ansprechpartner. Sie erhalten ein Monitoring mit Fernüberwachung, das Ertrag und Verbrauch "
         "zeigt, und einen festen Ansprechpartner für Service und Fragen. Bei uns endet die Betreuung nicht mit der "
         "Inbetriebnahme, sondern begleitet Sie über die Lebensdauer Ihrer Anlage."),
    ],
    "finalcta": {
        "eyebrow": "Machen Sie jetzt Ihr Unternehmen mit EBZ unabhängig",
        "h2": "Wie viel Marge wollen Sie weiterhin an Ihren Energieversorger verlieren?",
        "text": ("Jeder Tag ohne eigene PV-Anlage ist ein Tag, an dem Ihr Betrieb unnötig hohe Stromkosten zahlt. Der "
                 "beste Zeitpunkt für Ihre Investition war gestern, der zweitbeste ist jetzt."),
        "more": [
            ("Wir verbinden handwerkliche Präzision, moderne Technik und betriebswirtschaftliches Verständnis mit einem "
             "Serviceversprechen, das über die Montage hinausgeht. Die Erfahrung aus über 300 dokumentierten Projekten "
             "in 6 Bundesländern, vom Eigenheim bis zum Gewerbedach, fließt in jedes neue Projekt ein."),
            ("Der erste Schritt zu kalkulierbaren Energiekosten ist ein Gespräch. Kontaktieren Sie uns noch heute für "
             "Ihre kostenlose Besichtigung mit Lastprofil-Analyse."),
            "Das Team von EBZ Energie freut sich auf Ihr Unternehmen.",
        ],
    },
    "footnote": ("*Richtwerte aus EBZ-Projekten (Gewerbe Oberösterreich, Hotel Villach/Warmbad) und Marktrichtwerten 2026, "
                 "abhängig von Lastprofil, Anlagengröße, Ausrichtung und Strompreis. Steuerliche Angaben ersetzen keine "
                 "Steuerberatung. Verbindlich ist Ihr persönliches Angebot."),
}
