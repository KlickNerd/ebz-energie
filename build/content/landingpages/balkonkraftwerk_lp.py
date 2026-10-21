"""Ads-Landingpage Balkonkraftwerk (alte WP-Seite /balkonkraftwerk-lp/, Stand 2025).

Botschaft der alten LP uebernommen (Balkonkraftwerk komplett, Qualitaet vom Fachbetrieb, Anmeldung inklusive,
lange Modulgarantie, optional Speicher, Tipp vereinfachte Zustimmung, Komplettservice). Korrigiert: Fixpreise
995 € / 1.995 € und "Sparen Sie 500 € / 740 €" weggelassen (keine freigegebenen EBZ-Set-Preise, stattdessen
Kostenanker laut klimaaktiv aus build/pages/balkonkraftwerke.py*), Speichermarke der alten LP nicht genannt,
"4 Flexmodule a 220 Wp" -> Modulleistung frei, 1.200 bis 2.000 Wp ueblich; "30 Jahre Garantie" -> 25 bis 30
Jahre Leistungsgarantie auf die Module; Tipp "Seit 1. September ... Nachbarn" -> Zustimmungsfiktion im
Wohnungseigentum seit 1. September 2024; Widmanngasse -> NAP. Keine Foerderbetraege.
"""

LP = {
    "path": "/balkonkraftwerk-lp/",
    "title": "Balkonkraftwerk komplett mit Montage und Anmeldung | EBZ",
    "description": ("Balkonkraftwerk komplett vom Fachbetrieb: 800 Watt, auf Wunsch mit Speicher, Montage und Meldung "
                    "beim Netzbetreiber in Kärnten und der Steiermark."),
    "eyebrow": "Balkonkraftwerk für Mieter und Eigentümer",
    "h1": "Balkonkraftwerk komplett: Qualität vom Fachbetrieb, inklusive Montage und Anmeldung",
    "lead": ("Holen Sie sich die Kraft der Sonne auf den Balkon. Ein Balkonkraftwerk mit 800 Watt liefert bei guter "
             "Ausrichtung 600 bis 800 kWh im Jahr.* Wir stellen das passende Komplettset zusammen, auf Wunsch mit "
             "Speicher, montieren sturmsicher und melden die Anlage beim Netzbetreiber."),
    "badges": [("800 Watt", "normgerecht"), ("600 bis 800 kWh", "im Jahr*"), ("4,9", "Sterne auf Google")],
    "hero_img": "balkon",
    "hero_alt": "Solarmodule eines Balkonkraftwerks am Balkongeländer eines Wohnhauses",
    "problem": {
        "eyebrow": "Balkonkraftwerk komplett",
        "h2": "Kleinkraftwerk für Ihr Zuhause: Das steckt im Komplettset",
        "paragraphs": [
            ("Ein Balkonkraftwerk ist eine steckerfertige Mini-PV-Anlage mit bis zu 800 Watt Wechselrichterleistung. "
             "Die Modulleistung ist frei wählbar, 1.200 bis 2.000 Wp sind üblich und bringen auch morgens, abends und im "
             "Winter mehr Ertrag. Geräte, die gerade laufen, nutzen den Sonnenstrom zuerst."),
            ("Im Komplettset: Module, stabile und statisch geprüfte Halterung, Mikro-Wechselrichter mit 800 Watt, "
             "Einrichtung der App und die Meldung beim Netzbetreiber. Auf Wunsch kommt ein Speicher dazu, der den "
             "Mittagsüberschuss für den Abend aufhebt."),
        ],
    },
    "benefits": {
        "eyebrow": "Ihre Vorteile",
        "h2": "Ihr Photovoltaik-Fachbetrieb garantiert Ihnen",
        "intro": ("Ein Set im Online-Shop ist schnell bestellt. Ob es beim nächsten Sturm hält und normgerecht "
                  "angeschlossen ist, entscheiden Komponenten und Montage."),
        "cards": [
            ("◇", "Top-Qualität",
             "Glas-Glas- oder bifaziale Module aus dem Fachhandel, hagel- und sturmfest, mit 25 bis 30 Jahren "
             "Leistungsgarantie."),
            ("▮", "Speicher auf Wunsch",
             "Ein Speicher mit 1 bis 2 kWh hebt den Eigenverbrauch auf 70 bis 80 %.* So nutzen Sie den Sonnenstrom "
             "auch am Abend."),
            ("✓", "Komplettservice",
             "Lieferung, Montage, Prüfung von Steckdose und Stromkreis, Einrichtung der App und Meldung beim Netzbetreiber."),
            ("⌂", "Montage, wo Sie wollen",
             "Balkongeländer, Loggia, Fassade, Flachdach, Garage oder Garten: Wir liefern das passende Material."),
        ],
    },
    "quote": ("Mein Tipp: Seit 1. September 2024 reicht es im Wohnungseigentum, die anderen Eigentümer schriftlich über "
              "Ihr geplantes Balkonkraftwerk zu informieren. Widerspricht innerhalb von zwei Monaten niemand, gilt die "
              "Zustimmung als erteilt."),
    "steps": {
        "eyebrow": "So einfach geht es",
        "h2": "Vom Gespräch zum eigenen Sonnenstrom",
        "steps": [
            ("Beratung",
             "Wir klären Standort, Ausrichtung, Verschattung und Verbrauch und ob ein Speicher sinnvoll ist. Kostenlos.",
             "Tag 1"),
            ("Set und Angebot",
             "Sie erhalten ein abgestimmtes Komplettset aus Modulen, Wechselrichter, Halterung und optional Speicher, "
             "mit Set, Speicher und Montage als eigene Positionen.", "wenige Tage"),
            ("Meldung beim Netzbetreiber",
             "Wir bereiten die Meldung bei Kärnten Netz, Energienetze Steiermark oder Stromnetz Graz vor.",
             "14 Tage vor Inbetriebnahme"),
            ("Montage und Start",
             "Unsere Fachkräfte montieren sturmsicher, prüfen den Anschluss und richten die App ein.", "wenige Stunden"),
        ],
    },
    "why": {
        "eyebrow": "Warum EBZ Energie",
        "h2": "Ihr Fachbetrieb für Balkonkraftwerke in Kärnten und der Steiermark",
        "items": [
            ("✓", "Zertifizierte Fachkräfte",
             "Normgerechte Montage, statisch geprüfte Befestigung, Prüfung von Steckdose und Stromkreis."),
            ("☀", "Komponenten aus großen Projekten",
             "Nur Module und Wechselrichter, denen wir auch bei Dachanlagen vertrauen."),
            ("★", "4,9 Sterne auf Google", "Bewertungen von echten Kundinnen und Kunden aus der Region."),
            ("◉", "300+ Projekte",
             "Erfahrung aus über 300 dokumentierten Projekten in 6 Bundesländern, vom Balkon bis zum Gewerbedach."),
            ("⌂", "Regional aus Villach",
             "Montage in Villach, Klagenfurt, Wolfsberg, Graz und Umgebung. Beratung vor Ort."),
            ("◇", "Mitwachsende Lösung",
             "Vom Balkonkraftwerk über den Speicher bis zur Dachanlage mit Wallbox: ein Ansprechpartner."),
        ],
    },
    "finance": False,
    "refs": ["villach", "krumpendorf", "gewerbe"],
    "refs_h2": "Vom Balkon bis zum Dach: Projekte vom Fachbetrieb",
    "contact": {
        "h2": "Welches Balkonkraftwerk passt zu Ihnen?",
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
        ("Brauche ich die Zustimmung der anderen Wohnungseigentümer?",
         "Seit 1. September 2024 gilt im Wohnungseigentum die Zustimmungsfiktion: Sie informieren die anderen Eigentümer "
         "schriftlich, widerspricht innerhalb von zwei Monaten niemand, gilt die Zustimmung als erteilt. Mieter brauchen "
         "das Okay von Vermieter oder Hausverwaltung. Die technischen Unterlagen liefern wir."),
        ("Gibt es eine Förderung für Balkonkraftwerke?",
         "Das hängt von Bundesland und Gemeinde ab, die Programme ändern sich laufend. Wir prüfen den aktuellen Förderstand "
         "für Ihr Projekt und übernehmen die Anträge."),
    ],
    "finalcta": {
        "h2": "Starten Sie klein, aber richtig",
        "text": ("Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags und sagen Ihnen, "
                 "ob Balkonkraftwerk oder Dachanlage für Sie die bessere Wahl ist."),
    },
    "footnote": ("*Richtwerte: Jahresertrag 600 bis 800 kWh für ein 800-Watt-Balkonkraftwerk bei guter Ausrichtung, "
                 "Ersparnis bei 30 ct/kWh, Eigenverbrauch mit Speicher 70 bis 80 %, Kostenanker 800 € Set plus 400 € "
                 "Montage laut klimaaktiv. Ertrag und Ersparnis hängen von Standort, Verschattung, Verbrauch und Strompreis "
                 "ab. Verbindlich ist Ihr persönliches Angebot."),
}
