"""Ads-Landingpage Waermepumpe (alte WP-Seite /waermepumpeninstallation-oesterreich/, Stand Mai 2026).

Aufbau wie das Muster /photovoltaik-privat-lp/ und wie die alte LP: Hero auf Foto (Alpenhaus), Bewertungen,
Problem mit Bild (Haus mit Waermepumpe) und 4 Punkten, Heizsystem-Text mit den 4 Karten (die alte
WP-Funktionsgrafik mit "Heizkosten um bis zu 70 %" ist nicht freigegeben, deshalb Text in den Karten),
Mario-Zitat mit Button, 4 Schritte auf Foto, Warum EBZ, Finanzierung mit Bild, Galerie 2023, Schluss-Aufruf mit
Mario, Formular, FAQ.

Korrigiert: Foerderversprechen ("gefoerdert", "Maximale Foerderung gesichert", "massiv gefoerdert", "so hoch wie
nie", "tausende Euro an Zuschuessen", "Bund und Land", "Foerderungen sind begrenzt") -> Foerderstand wird geprueft,
keine Betraege; Techniker/Montageteams -> zertifizierte Fachkraefte; PV-Finanzierung ab 49 €/keine
Bonitaetspruefung/24 Stunden/KSV/Servicevertrag/Leasing -> Standard-Finanzierungsblock (PV-Komplettanlage mit
Speicher ab 147 €*, Eigentum ab Tag 1), fuer die Waermepumpe keine eigene Rate; "tausende Euro", "drastisch",
"100 % zukunftssicher", "massiv" -> sachlich; "100 Anlagen pro Jahr" -> 300+ Projekte; "ganz Oesterreich" als
Einsatzgebiet -> Kaernten und Steiermark; Garantie nur fuer PV-Module; Widmanngasse -> Triglavstrasse 15 (NAP).
Zahlen aus build/pages/waermepumpe.py.
"""

from common import a

_I = "/assets/img/"

LP = {
    "path": "/waermepumpeninstallation-oesterreich/",
    "title": "Wärmepumpe installieren lassen: schlüsselfertig | EBZ",
    "description": ("Wärmepumpe schlüsselfertig vom Fachbetrieb aus Villach: Beratung vor Ort, Heizlastberechnung, "
                    "Förderabwicklung und Montage aus einer Hand. 4,9 Sterne."),
    "eyebrow": "Sagen Sie Ihren Heizkosten den Kampf an",
    "h1": "Ihre neue Wärmepumpe von EBZ: schlüsselfertig, mit Förderabwicklung und aus einer Hand",
    "lead": ("Heizen Sie ab sofort moderner, günstiger und unabhängiger. EBZ Energie begleitet Sie auf diesem Weg und "
             "übernimmt alle wichtigen Schritte für Sie: von der Erstberatung über die Förderabwicklung bis zur sauberen "
             "Montage durch zertifizierte Fachkräfte."),
    "badges": [("1 kWh Strom", "wird zu 4 bis 5 kWh Wärme"), ("2 bis 4 Tage", "Montage vor Ort"), ("300+", "Projekte")],
    "hero_img": "waermepumpe",
    "hero_alt": "Luft-Wasser-Wärmepumpe im Garten neben einem Wohnhaus",
    "media": {
        "hero_bg": _I + "lp-hero-alpenhaus.jpg",
        "problem_img": (_I + "lp-haus-pv-waermepumpe.jpg",
                        "Modernes Einfamilienhaus mit Wärmepumpe vor dem Haus und Photovoltaik auf dem Dach"),
        "mario": False,
        "mario_cta": True,
        "steps_bg": _I + "lp-bg-module-abendsonne.jpg",
        "finance_img": (_I + "lp-finanzierung-haus.jpg", "Geldscheine vor einem Einfamilienhaus mit Photovoltaikanlage"),
        "gallery": "GALLERY_2023",
        "final_mario": True,
    },
    "problem": {
        "eyebrow": "Das Problem",
        "h2": "Ihre Heizung kostet Sie jeden Winter mehr, ohne dass Sie etwas dagegen tun können",
        "paragraphs": [
            ("Egal ob Öl, Gas oder Fernwärme: Die Preise steigen seit Jahren. Und jedes Mal, wenn Sie die "
             "Heizkostenabrechnung öffnen, wissen Sie schon vorher: Nächstes Jahr wird es wieder teurer."),
            ("Diese Abhängigkeit von fossilen Energieträgern kostet Sie nicht nur Geld. Sie kostet Sie Nerven, "
             "Planungssicherheit und Jahr für Jahr Geld, das Sie nie wiedersehen."),
        ],
        "bullets_intro": "Es gibt einen besseren Weg, erprobt und zuverlässig: die Wärmepumpe.",
        "bullets": [
            ("<b>Das perfekte Duo:</b> Auf Wunsch liefert Ihre PV-Anlage den eigenen Sonnenstrom, und die Wärmepumpe "
             "heizt damit Ihr Haus."),
            ("<b>Alles aus einer Hand:</b> ein Ansprechpartner für Planung, Montage und Inbetriebnahme. Kein "
             "Handwerker-Chaos."),
            ("<b>Förderabwicklung inklusive:</b> Wir prüfen den aktuellen Förderstand und übernehmen den lästigen "
             "Papierkram und die Anträge für Sie."),
            ("<b>Sicher entscheiden:</b> kostenlose, persönliche Beratung und technische Machbarkeitsprüfung direkt "
             "bei Ihnen vor Ort."),
        ],
    },
    "benefits": {
        "eyebrow": "Das Heizsystem",
        "h2": "Die Wärmepumpe: das modernste und im Betrieb günstigste Heizsystem, das es heute gibt",
        "intro": ("Statt fossile Brennstoffe teuer einzukaufen und zu verbrennen, nutzt eine Wärmepumpe eine Ressource, "
                  "die ohnehin da ist: kostenlose Umweltwärme aus der Luft, der Erde oder dem Grundwasser. Ein "
                  "hocheffizienter Prozess hebt diese Energie so weit an, dass sie Ihr gesamtes Gebäude heizt und mit "
                  "Warmwasser versorgt. Aus 1 kWh Strom und 3 bis 4 kWh Umweltwärme entstehen 4 bis 5 kWh Heizwärme."
                  "<br><br>"
                  "Für Sie bedeutet das: Sie koppeln sich vom unsicheren Markt für fossile Brennstoffe ab, und Ihre "
                  "Heizkosten sinken deutlich und dauerhaft. Gleichzeitig heizen Sie zukunftssicher und klimafreundlich "
                  "und steigern den Wert Ihrer Immobilie."
                  "<br><br>"
                  "<b>Ihre Umgebung ist voller ungenutzter Energie, und wir machen sie für Sie nutzbar.</b>"),
        "cards": [
            ("€", "Heizkosten dauerhaft senken",
             "Eine moderne Wärmepumpe erzeugt aus 1 kWh Strom 4 bis 5 kWh Wärme. Ihre Heizkosten sinken deutlich und "
             "bleiben dauerhaft niedrig. Mit Strom vom eigenen Dach wird sie zur günstigsten Heizung im Haus."),
            ("♨", "Weg von Gas und Öl, für immer",
             "Kein Heizöl mehr bestellen, keine Gaspreise mehr beobachten, keine bösen Überraschungen bei der "
             "Jahresabrechnung. Sie heizen mit Energie aus Ihrer Umgebung, die kostenlos und unbegrenzt verfügbar ist."),
            ("☀", "Angenehme Kühlung im Sommer",
             "Viele moderne Wärmepumpen können an heißen Tagen auch kühlen, über die Fußbodenheizung oder "
             "Gebläsekonvektoren. Sie erhalten ein System für Heizung, Warmwasser und Kühlung in einem, ganz ohne "
             "teure Klimaanlage."),
            ("✓", "Förderabwicklung inklusive",
             "Wir prüfen den aktuellen Förderstand für Ihr Projekt, stellen jeden Antrag korrekt und rechtzeitig und "
             "übernehmen den gesamten Papierkram."),
        ],
    },
    "quote": ("Von der kostenlosen Besichtigung vor Ort über die Förderabwicklung bis zur fertigen Installation: "
              "Wir setzen Ihre Wärmepumpe schlüsselfertig für Sie um."),
    "steps": {
        "eyebrow": "So einfach geht es",
        "h2": "Ihr Weg zur Energieunabhängigkeit mit EBZ: in 4 einfachen Schritten",
        "steps": [
            ("Kostenlose und ehrliche Beratung",
             "Kein Druck, kein Verkaufsgespräch. Wir analysieren Ihren Heizbedarf, Ihr Gebäude und Ihre Situation und "
             "zeigen Ihnen ehrlich, welche Wärmepumpe für Sie die meiste Ersparnis bringt.", "Tag 1"),
            ("Maßgeschneiderte Planung",
             "Wir kommen zu Ihnen vor Ort. Sie erhalten eine detaillierte Heizlastberechnung, eine Systemempfehlung und "
             "ein transparentes Festpreisangebot ohne versteckte Kosten.", "ca. 1 Woche"),
            ("Wir erledigen die Bürokratie",
             "Förderanträge, Behördenkommunikation und Genehmigungen: Wir übernehmen alles. Sie müssen sich um nichts "
             "kümmern.", "parallel"),
            ("Installation und Inbetriebnahme",
             "Zertifizierte Fachkräfte installieren Ihre Wärmepumpe sauber, zügig und nach österreichischen Normen, "
             "inklusive Demontage der alten Heizung. Danach erklären wir Ihnen alles und bleiben Ihr Ansprechpartner.",
             "2 bis 4 Tage"),
        ],
    },
    "why": {
        "eyebrow": "Warum EBZ Energie",
        "h2": "Darum sollten Sie sich für EBZ entscheiden: Ihr Energie-Partner für Kärnten und die Steiermark",
        "items": [
            ("♨", "Wärmepumpe aus einer Hand",
             "Ein Ansprechpartner, ein Vertrag, auch in Kombination mit Photovoltaik und Speicher."),
            ("✓", "Zertifizierte Fachkräfte", "Meisterhaftes Handwerk und sorgfältige Ausführung nach österreichischen Normen."),
            ("€", "Komplette Förderabwicklung",
             "Wir prüfen vor jedem Angebot den aktuellen Förderstand und übernehmen die Anträge."),
            ("◇", "Lange Garantien",
             "Für Photovoltaikmodule bis zu 30 Jahre Leistungsgarantie und mindestens 10 Jahre Produktgarantie. Die "
             "Garantie Ihrer Wärmepumpe nennen wir Ihnen im Angebot."),
            ("◎", "Volle Transparenz",
             "Kein Angebot ohne klare Kostenaufstellung: Sie erhalten einen Festpreis ohne versteckte Kosten."),
            ("⌂", "Regionale Expertise", "Zuhause in Villach, im Einsatz in Kärnten und der Steiermark."),
        ],
    },
    "finance": True,
    "gallery_h2": "Echte Projekte, echte Ergebnisse, aus Ihrer Region",
    "contact": {
        "h2": "Jetzt unverbindlich anfragen",
        "sub": "Sagen Sie uns kurz, wie Sie heute heizen. Wir melden uns innerhalb eines Werktags und vereinbaren einen Termin vor Ort.",
    },
    "faq": [
        ("Ist mein Haus für eine Wärmepumpe geeignet?",
         "Moderne Wärmepumpen funktionieren in den meisten Gebäuden, auch in älteren Häusern ohne Fußbodenheizung. "
         "Bis 55 Grad Vorlauf arbeitet eine moderne Wärmepumpe effizient, große alte Heizkörper sind oft "
         "überdimensioniert und deshalb geeignet. Wir prüfen Ihr Gebäude kostenlos vor Ort und sagen Ihnen ehrlich, "
         "was für Ihre Situation Sinn ergibt."),
        ("Funktioniert die Wärmepumpe auch im Winter zuverlässig?",
         "Ja. Moderne Luft-Wasser-Wärmepumpen arbeiten bis minus 20 Grad Außentemperatur, auch im Klima von Kärnten "
         "und der Steiermark. Entscheidend ist die richtige Auslegung nach der Heizlast Ihres Hauses, dann ist Ihre "
         "Wärmeversorgung auch an den kältesten Tagen gesichert."),
        ("Welche Förderung bekomme ich?",
         "Das hängt von Bundesland, Gebäude und System ab, und die Förderlage ändert sich derzeit laufend. Wir prüfen "
         "den aktuellen Förderstand für Ihr Projekt und übernehmen die Anträge."),
        ("Was kostet mich das wirklich?",
         "Als Richtwert kostet eine Luft-Wasser-Wärmepumpe im Einfamilienhaus inklusive Montage rund 12.000 bis "
         "22.000 € vor Förderung.* Sie erhalten nach der Vor-Ort-Prüfung ein detailliertes Festpreisangebot ohne "
         "Überraschungen."),
        ("Wie lange dauert der Einbau?",
         "Die Montage vor Ort dauert 2 bis 4 Tage inklusive Demontage der alten Heizung. Davor liegen Beratung, "
         "Vor-Ort-Prüfung, Festpreisangebot und die Förderanträge."),
        ("Kann ich die Wärmepumpe finanzieren?",
         "Ja. Mit unserer " + a("finanzierung", "Finanzierung") + " gehört die Anlage ab dem ersten Tag Ihnen, mit "
         "0 € Anzahlung und fixer Rate. Die Konditionen für Ihr Projekt nennen wir Ihnen mit dem Angebot."),
        ("Was passiert nach der Installation?",
         "Wir bleiben Ihr Ansprechpartner für Wartungsfragen, Service-Checks oder wenn einmal etwas nicht stimmt. Eine "
         "Wärmepumpe braucht nur alle 2 bis 3 Jahre eine Inspektion und hält 15 bis 20 Jahre und mehr. Bei uns endet "
         "die Betreuung nicht mit der Inbetriebnahme."),
    ],
    "finalcta": {
        "eyebrow": "Machen Sie sich jetzt mit EBZ unabhängig",
        "h2": "Wie viel Geld wollen Sie weiterhin sinnlos verheizen?",
        "text": ("Jeder Tag ohne Wärmepumpe ist ein Tag, an dem Sie Geld verschenken. Der beste Zeitpunkt zum Handeln "
                 "war gestern, der zweitbeste ist jetzt."),
        "more": [
            ("Wir kombinieren handwerkliche Präzision mit moderner Technik und einem Serviceversprechen, das über die "
             "Montage hinausgeht. Die Erfahrung aus über 300 dokumentierten Projekten fließt in jedes neue Projekt ein."),
            ("Der erste Schritt in eine unabhängige Zukunft ist ein Gespräch. Kontaktieren Sie uns noch heute für Ihr "
             "kostenloses und unverbindliches Angebot."),
            "Das Team von EBZ Energie freut sich auf Sie.",
        ],
    },
    "footnote": ("*Richtwert für eine Luft-Wasser-Wärmepumpe im Einfamilienhaus inklusive Montage, vor Förderung, Stand "
                 "Oktober 2026. Finanzierung: Beispielkonditionen für eine Photovoltaik-Komplettanlage mit Speicher, "
                 "abhängig von Anlagengröße und Laufzeit. Verbindlich ist Ihr persönliches Angebot."),
}
