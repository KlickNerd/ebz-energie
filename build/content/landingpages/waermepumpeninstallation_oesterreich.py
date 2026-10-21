"""Ads-Landingpage Waermepumpe (alte WP-Seite /waermepumpeninstallation-oesterreich/, Stand Mai 2026).

Botschaft der alten LP uebernommen (Heizkosten-Kampfansage, Waermepumpe schluesselfertig aus einer Hand,
Foerderabwicklung, Kuehlung im Sommer, 4 Schritte). Korrigiert: Foerderversprechen ("massiv gefoerdert",
"so hoch wie nie", "Bund und Land", "Foerderungen sind begrenzt") -> Foerderstand wird geprueft, keine Betraege;
eigene Montageteams/Techniker -> zertifizierte Fachkraefte; PV-Finanzierungsblock mit Leasing/ab 49 €/keine
Bonitaetspruefung/24 Stunden/KSV/Servicevertrag entfernt (reine Waermepumpen-LP, Finanzierung nur im FAQ);
"100 Anlagen pro Jahr" -> 300+ Projekte; "ganz Oesterreich" als Montagegebiet -> Kaernten und Steiermark;
Widmanngasse -> Triglavstrasse 15 (kommt aus NAP). Zahlen aus build/pages/waermepumpe.py.
"""

from common import a

LP = {
    "path": "/waermepumpeninstallation-oesterreich/",
    "title": "Wärmepumpe installieren lassen: schlüsselfertig | EBZ",
    "description": ("Wärmepumpe schlüsselfertig vom Fachbetrieb aus Villach: Beratung vor Ort, Heizlastberechnung, "
                    "Förderabwicklung und Montage aus einer Hand. 4,9 Sterne."),
    "eyebrow": "Sagen Sie Ihren Heizkosten den Kampf an",
    "h1": "Ihre neue Wärmepumpe von EBZ: schlüsselfertig installiert, mit Förderabwicklung, alles aus einer Hand",
    "lead": ("Heizen Sie moderner, günstiger und unabhängiger. EBZ Energie übernimmt alle wichtigen Schritte für Sie: "
             "Erstberatung vor Ort, Heizlastberechnung, Förderabwicklung und saubere Montage durch zertifizierte "
             "Fachkräfte."),
    "badges": [("1 kWh Strom", "wird zu 4 bis 5 kWh Wärme"), ("2 bis 4 Tage", "Montage vor Ort"), ("300+", "Projekte")],
    "hero_img": "waermepumpe",
    "hero_alt": "Luft-Wasser-Wärmepumpe im Garten neben einem Wohnhaus",
    "problem": {
        "eyebrow": "Das Problem",
        "h2": "Ihre Heizung kostet Sie jeden Winter mehr, ohne dass Sie etwas dagegen tun können",
        "paragraphs": [
            ("Egal ob Öl, Gas oder Fernwärme: Die Preise steigen seit Jahren. Und jedes Mal, wenn Sie die "
             "Heizkostenabrechnung öffnen, wissen Sie, dass es nächstes Jahr wieder teurer wird."),
            ("Eine Wärmepumpe nutzt eine Ressource, die ohnehin da ist: Wärme aus der Luft, der Erde oder dem "
             "Grundwasser. Aus 1 kWh Strom und 3 bis 4 kWh Umweltwärme entstehen 4 bis 5 kWh Heizwärme. Damit "
             "heizen Sie Ihr Haus und bereiten Warmwasser, ohne Heizöl zu bestellen oder Gaspreise zu beobachten."),
        ],
    },
    "benefits": {
        "eyebrow": "Ihre Vorteile",
        "h2": "Die Wärmepumpe: Heizung, Warmwasser und Kühlung in einem System",
        "intro": "Ihre Umgebung ist voller ungenutzter Energie. Wir planen die Wärmepumpe passend zu Ihrem Gebäude.",
        "cards": [
            ("€", "Heizkosten dauerhaft senken",
             "Eine moderne Wärmepumpe macht aus 1 kWh Strom 4 bis 5 kWh Wärme. Mit Strom vom eigenen Dach wird sie zur günstigsten Heizung im Haus."),
            ("♨", "Weg von Gas und Öl",
             "Kein Heizöl mehr bestellen, keine Gaspreise mehr beobachten, keine Überraschungen bei der Jahresabrechnung."),
            ("☀", "Kühlung im Sommer",
             "Viele Wärmepumpen kühlen an heißen Tagen über die Fußbodenheizung oder Gebläsekonvektoren. Ein System für Heizung, Warmwasser und Kühlung."),
            ("✓", "Förderabwicklung inklusive",
             "Wir prüfen den aktuellen Förderstand für Ihr Projekt und übernehmen die Anträge. Sie müssen sich um keinen Papierkram kümmern."),
        ],
    },
    "quote": ("Von der kostenlosen Besichtigung vor Ort über die Förderabwicklung bis zur fertigen Installation: "
              "Wir setzen Ihre Wärmepumpe schlüsselfertig für Sie um."),
    "steps": {
        "eyebrow": "So einfach geht es",
        "h2": "In 4 Schritten zu Ihrer neuen Wärmepumpe",
        "steps": [
            ("Kostenlose und ehrliche Beratung", "Wir analysieren Heizbedarf, Gebäude und Ihre Situation und zeigen Ihnen ehrlich, welche Wärmepumpe für Sie die meiste Ersparnis bringt.", "Tag 1"),
            ("Planung vor Ort", "Sie erhalten eine Heizlastberechnung, eine Systemempfehlung und ein transparentes Festpreisangebot ohne versteckte Kosten.", "ca. 1 Woche"),
            ("Förderung und Bürokratie", "Wir prüfen den aktuellen Förderstand, stellen die Anträge und übernehmen die Kommunikation mit den Behörden.", "parallel"),
            ("Montage und Inbetriebnahme", "Zertifizierte Fachkräfte installieren Ihre Wärmepumpe inklusive Demontage der alten Heizung. Danach erklären wir Ihnen alles.", "2 bis 4 Tage"),
        ],
    },
    "why": {
        "eyebrow": "Warum EBZ Energie",
        "h2": "Darum entscheiden sich Kundinnen und Kunden für EBZ",
        "items": [
            ("♨", "Wärmepumpe aus einer Hand", "Ein Ansprechpartner von der Planung bis zur Übergabe, auch in Kombination mit Photovoltaik und Speicher."),
            ("✓", "Zertifizierte Fachkräfte", "Meisterhaftes Handwerk und sorgfältige Ausführung nach österreichischen Normen."),
            ("€", "Förderabwicklung inklusive", "Wir prüfen vor jedem Angebot den aktuellen Förderstand und übernehmen die Anträge."),
            ("◇", "Volle Transparenz", "Kein Angebot ohne klare Kostenaufstellung: Sie erhalten einen Festpreis ohne versteckte Kosten."),
            ("◉", "300+ Projekte", "Erfahrung aus über 300 dokumentierten Projekten in 6 Bundesländern."),
            ("⌂", "Regional verwurzelt", "Zuhause in Villach, im Einsatz in Kärnten und der Steiermark."),
        ],
    },
    "contact": {
        "h2": "Jetzt unverbindlich anfragen",
        "sub": "Sagen Sie uns kurz, wie Sie heute heizen. Wir melden uns innerhalb eines Werktags und vereinbaren einen Termin vor Ort.",
    },
    "faq": [
        ("Ist mein Haus für eine Wärmepumpe geeignet?",
         "Meistens ja, auch ältere Häuser ohne Fußbodenheizung. Bis 55 Grad Vorlauf arbeitet eine moderne Wärmepumpe "
         "effizient, große alte Heizkörper sind oft überdimensioniert und deshalb geeignet. Wir prüfen Ihr Gebäude "
         "kostenlos vor Ort und sagen Ihnen ehrlich, was für Ihre Situation Sinn ergibt."),
        ("Funktioniert die Wärmepumpe auch im Winter zuverlässig?",
         "Ja. Moderne Luft-Wasser-Wärmepumpen arbeiten bis minus 20 Grad Außentemperatur. Kälte ist kein Hindernis, "
         "entscheidend ist die richtige Auslegung nach der Heizlast Ihres Hauses."),
        ("Welche Förderung bekomme ich?",
         "Das hängt von Bundesland, Gebäude und System ab, und die Förderlage ändert sich derzeit laufend. Wir prüfen "
         "den aktuellen Förderstand für Ihr Projekt und übernehmen die Anträge."),
        ("Was kostet eine Wärmepumpe?",
         "Als Richtwert kostet eine Luft-Wasser-Wärmepumpe im Einfamilienhaus inklusive Montage rund 12.000 bis "
         "22.000 € vor Förderung.* Sie erhalten nach der Vor-Ort-Prüfung ein Festpreisangebot ohne versteckte Kosten."),
        ("Wie lange dauert der Einbau?",
         "Die Montage vor Ort dauert 2 bis 4 Tage inklusive Demontage der alten Heizung. Davor liegen Beratung, "
         "Vor-Ort-Prüfung, Festpreisangebot und die Förderanträge."),
        ("Kann ich die Wärmepumpe finanzieren?",
         "Ja. Mit unserer " + a("finanzierung", "Finanzierung") + " gehört die Anlage ab dem ersten Tag Ihnen, mit "
         "0 € Anzahlung und fixer Rate. Die Konditionen für Ihr Projekt nennen wir Ihnen mit dem Angebot."),
        ("Was passiert nach der Installation?",
         "Wir bleiben Ihr Ansprechpartner für Service und Fragen. Eine Wärmepumpe braucht nur alle 2 bis 3 Jahre eine "
         "Inspektion und hält 15 bis 20 Jahre und mehr."),
    ],
    "finalcta": {
        "h2": "Wie viel Geld wollen Sie weiterhin verheizen?",
        "text": "Der erste Schritt ist ein kostenloses Gespräch. Wir melden uns innerhalb eines Werktags.",
    },
    "footnote": ("*Richtwert für eine Luft-Wasser-Wärmepumpe im Einfamilienhaus inklusive Montage, vor Förderung, Stand "
                 "Oktober 2026. Verbindlich ist Ihr persönliches Festpreisangebot."),
}
