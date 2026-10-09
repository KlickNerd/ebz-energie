"""Leistungsseite Waermepumpe (/waermepumpen-installateur/).

Kernbotschaft: Die Waermepumpe ist bei EBZ Teil des Energiesystems aus
Photovoltaik, Speicher und Energiemanagement. Eigenheim UND Gewerbe.
Zahlen stammen aus den Ratgebern des Clusters (Kosten, Foerderung, Altbau,
Funktionsweise, PV fuer Waermepumpe), Stand September 2026.
Quelle der Live-Seite bereinigt: "90 %"-Claim, Gedankenstriche, Emojis,
unbelegte Superlative, "ganz Oesterreich" als Montagegebiet.
"""

from common import IMG, NAP, S, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, write_page, load_reviews
from layout import page
import components as C

# Slug kommt aus common.S (Stand Oktober 2026: /waermepumpe/, alte URL
# /waermepumpen-installateur/ per 301 in redirects.txt). Ausgabepfad folgt dem Slug,
# damit Navigation, Sitemap und Seite immer dieselbe URL verwenden.
PATH = S["waermepumpe"]
OUT_FILE = PATH.strip("/") + "/index.html"
TITLE = "Wärmepumpen-Installateur Kärnten & Steiermark | EBZ Energie"
DESC = ("Wärmepumpe vom Fachbetrieb EBZ Energie: Planung, Montage und Förderung in Kärnten und der "
        "Steiermark. Luft-Wasser ab 12.000 €, bis 7.500 € Bundesförderung.")

FAQ = [
    ("Was kostet eine Wärmepumpe für ein Einfamilienhaus?",
     "Eine Luft-Wasser-Wärmepumpe kostet für ein typisches Einfamilienhaus 12.000 bis 22.000 Euro vor "
     "Förderung, im Altbau mit Anpassungen 15.000 bis 28.000 Euro. Erdwärmepumpen liegen bei 22.000 bis "
     "40.000 Euro. Bund und Land senken die Summe je nach Programm um 4.000 bis 12.000 Euro."),
    ("Wie hoch ist die Förderung für eine Wärmepumpe 2026?",
     "Die Sanierungsoffensive des Bundes zahlt für den Tausch einer Öl-, Gas-, Kohle- oder Elektroheizung "
     "bis zu 7.500 Euro, bei Erdwärme mit Bohrbonus bis zu 12.500 Euro, gedeckelt bei 30 Prozent der "
     "Kosten. Kärnten und die Steiermark fördern zusätzlich mit 35 Prozent der förderbaren Kosten. "
     "Haushalte im unteren Einkommensdrittel erhalten über Sauber Heizen für Alle bis zu 100 Prozent."),
    ("Funktioniert eine Wärmepumpe auch im Altbau?",
     "Ja, in den meisten Fällen. Entscheidend ist nicht das Baujahr, sondern die Vorlauftemperatur: "
     "Moderne Geräte arbeiten bis 55 Grad effizient und damit auch mit vorhandenen Heizkörpern. Große alte "
     "Heizkörper sind oft überdimensioniert und deshalb gut geeignet. Eine Fußbodenheizung ist nicht zwingend."),
    ("Wie viel Strom braucht eine Wärmepumpe?",
     "Aus einer Kilowattstunde Strom macht eine Wärmepumpe 4 bis 5 Kilowattstunden Wärme. Ein gut gedämmtes "
     "Haus mit 12.000 kWh Wärmebedarf braucht bei Jahresarbeitszahl 4 rund 3.000 kWh Strom im Jahr, also "
     "etwa 900 Euro. Eine Gasheizung kostet für dieselbe Wärme 1.400 bis 1.900 Euro."),
    ("Lohnt sich die Kombination mit Photovoltaik?",
     "Ja. Eigener Solarstrom kostet 10 bis 14 Cent je Kilowattstunde, Netzstrom das Zwei- bis Dreifache. "
     "Mit PV-Anlage und Speicher sinken die Heizkosten auf 200 bis 500 Euro im Jahr. Beide Systeme werden "
     "getrennt gefördert: die Wärmepumpe über die Sanierungsoffensive, die PV-Anlage über den EAG-Zuschuss."),
    ("Heizt eine Wärmepumpe auch bei minus 15 Grad in Kärnten?",
     "Ja. Luft-Wasser-Wärmepumpen arbeiten bis minus 20 Grad und darunter. Das Kältemittel R290 verdampft "
     "schon bei rund minus 42 Grad. Für sehr kalte Lagen planen wir die Leistung entsprechend und prüfen "
     "die Heizflächen vor Ort."),
    ("Wie lange dauert der Einbau?",
     "Die Montage vor Ort dauert in der Regel 2 bis 4 Tage inklusive Demontage der alten Heizung. Davor "
     "liegen Beratung, Vor-Ort-Prüfung, Angebot und die Registrierung der Förderung, die vor dem Auftrag "
     "erfolgen muss. Nach der Registrierung bleiben 9 Monate für Umsetzung und Endabrechnung."),
]


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        C.hero(
            eyebrow="Wärmepumpen-Installateur für Kärnten und die Steiermark",
            h1="Wärmepumpe vom Fachbetrieb: heizen mit Strom statt mit Öl und Gas",
            lead=("Eine Wärmepumpe holt 75 Prozent der Heizwärme kostenlos aus Luft, Erdreich oder "
                  "Grundwasser. Mit Strom vom eigenen Dach wird sie zur günstigsten Heizung im Haus. "
                  "EBZ Energie plant, montiert und betreut Wärmepumpe, Photovoltaik, Speicher und "
                  "Energiemanagement als ein System, mit zertifizierten Fachkräften aus Villach."),
            badges=[("Bis 7.500 €", "Bundesförderung 2026"),
                    ("Luft, Erde", "oder Grundwasser"),
                    ("Mit PV + Speicher", "aus einer Hand")],
            img=IMG["waermepumpe"],
            img_alt="Luft-Wasser-Wärmepumpe im Garten eines Einfamilienhauses",
            float_num=rating,
            float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_secondary=("#kosten", "Kosten und Förderung"),
        ),
        C.kpis([
            ("4 bis 5 kWh", "Wärme aus 1 kWh Strom"),
            ("bis 7.500 €", "Bundesförderung Wärmepumpe"),
            ("12.000 bis 22.000 €", "Luft-Wasser vor Förderung*"),
            (NAP["rating"], "Sterne auf Google"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Was ist eine Wärmepumpe?",
            paragraphs=[
                ("Eine Wärmepumpe ist eine Heizung, die Umgebungswärme aus Luft, Erdreich oder Grundwasser "
                 "aufnimmt und mit einem Kältemittelkreislauf auf Heiztemperatur hebt, wie ein Kühlschrank in "
                 "umgekehrter Richtung. Nur der Verdichter braucht Strom: Aus 1 kWh Strom und 3 bis 4 kWh "
                 "Umweltwärme entstehen 4 bis 5 kWh Heizwärme (Jahresarbeitszahl, JAZ). Ein Gas-Brennwertkessel "
                 "holt aus 1 kWh Gas höchstens 0,95 kWh Wärme."),
            ],
        ),
        C.hub_section(
            eyebrow="Die Wärmepumpe im Energiesystem",
            h2="Ein Gerät heizt. Ein System spart.",
            lead=("Die Wärmepumpe ist der größte Stromverbraucher im Haus. Deshalb planen wir sie zusammen "
                  "mit Photovoltaik, Speicher und Energiemanagement: Der Heizstrom kommt vom eigenen Dach."),
            points=[
                ("☀", "Photovoltaik mit 10 bis 15 kWp liefert den Strom für Wärmepumpe und Haushalt"),
                ("▮", "Batteriespeicher mit 10 bis 12 kWh hebt den Eigenverbrauch auf 70 bis 80 Prozent"),
                ("♨", "Wärmepumpe heizt, bereitet Warmwasser und kühlt im Sommer"),
                ("⚙", "Energiemanagement mit SG-Ready-Schnittstelle lädt bei Sonne den Wärmespeicher vor"),
                ("€", "Solarstrom kostet 10 bis 14 ct/kWh, Netzstrom das Zwei- bis Dreifache*"),
            ],
        ),
        C.audience_split(
            eyebrow="Für wen planen wir?",
            h2="Eigenheim oder Betrieb: die Wärmepumpe passt zu Ihrem Gebäude",
            intro="Vom Heizungstausch im Einfamilienhaus bis zur Halle mit 80 kW Heizlast: Planung, Gerät und Förderweg richten wir danach aus.",
            left={
                "img": IMG["gen_eigenheim"],
                "alt": "Einfamilienhaus in Kärnten mit Photovoltaikanlage für die Wärmepumpe",
                "title": "Für Ihr Eigenheim",
                "bullets": [
                    "Heizungstausch Öl, Gas oder Elektro: bis 7.500 € vom Bund plus Landesförderung",
                    "Neubau und Altbau, auch mit vorhandenen Heizkörpern",
                    "Heizkosten mit Photovoltaik: 200 bis 500 € im Jahr*",
                ],
                "cta": ("kontakt", "Beratung für mein Zuhause"),
            },
            right={
                "img": IMG["gen_gewerbe"],
                "alt": "Gewerbegebäude mit großer Photovoltaikanlage am Dach",
                "title": "Für Ihren Betrieb",
                "bullets": [
                    "Betriebsförderung der KPC: bis 7.500 € unter 50 kW, bis 12.000 € bei 50 bis 100 kW",
                    "Planung nach Heizlast und Lastprofil, auch für Hallen und Bürogebäude",
                    "Kombination mit PV-Anlage senkt Heiz- und Stromkosten gleichzeitig",
                ],
                "cta": ("#gewerbe", "Wärmepumpe für Gewerbe"),
            },
        ),
        C.cards_section(
            eyebrow="Drei Wärmequellen",
            h2="Welche Wärmepumpe passt zu Ihrem Grundstück?",
            intro=("Luft, Erdreich oder Grundwasser: Die Wärmequelle entscheidet über Kosten, Effizienz "
                   "und Genehmigung. Wir prüfen vor Ort, welche Variante sich für Sie rechnet."),
            cards=[
                {"ic": "☀", "title": "Luft-Wasser-Wärmepumpe",
                 "text": ("Die häufigste Wahl: 12.000 bis 22.000 € vor Förderung, JAZ 3,0 bis 3,5, keine "
                          "Bohrung, läuft bis minus 20 Grad und darunter.*")},
                {"ic": "⬡", "title": "Erdwärmepumpe (Sole-Wasser)",
                 "text": ("Erdkollektor oder Tiefenbohrung: 22.000 bis 40.000 € vor Förderung, JAZ 4,0 bis 4,5, "
                          "dafür 5.000 € Bohrbonus vom Bund.*")},
                {"ic": "◎", "title": "Wasser-Wasser-Wärmepumpe",
                 "text": ("Die effizienteste Variante, JAZ 4,5 bis 5,5: 22.000 bis 38.000 € vor Förderung, "
                          "braucht Grundwasser und eine wasserrechtliche Bewilligung.*"),
                 "link_key": "/funktionsweise-einer-waermepumpe/", "link_text": "So funktioniert die Wärmepumpe"},
            ],
        ),
        C.problem_compare(
            eyebrow="Heizkosten im Vergleich",
            h2="Was Sie im Jahr fürs Heizen zahlen",
            intro=("Beispiel: gut gedämmtes Einfamilienhaus mit 12.000 kWh Wärmebedarf, die Wärmepumpe "
                   "braucht bei JAZ 4 rund 3.000 kWh Strom.*"),
            bars=[
                ("Gasheizung", 100, "bad", "1.400 bis 1.900 € im Jahr*"),
                ("Wärmepumpe mit Netzstrom", 50, "good", "rund 900 € im Jahr*"),
                ("Wärmepumpe mit Photovoltaik und Speicher", 20, "good", "200 bis 500 € im Jahr*"),
            ],
            aside=("Was Sie mit der Wärmepumpe gewinnen", [
                ("♨", "Heizung und Warmwasser", "Ein Gerät für beides, im Sommer auf Wunsch auch Kühlung."),
                ("€", "Planbare Kosten", "Kein Heizöl bestellen, kein Gaspreis, keine CO₂-Abgabe."),
                ("☀", "Strom vom Dach", "Mit PV-Anlage heizen Sie zu 10 bis 14 ct/kWh.*"),
                ("✓", "Wartungsarm", "Inspektion alle 2 bis 3 Jahre, 15 bis 20 Jahre Lebensdauer und mehr."),
            ]),
        ),
        C.price_cards(
            eyebrow="Wärmepumpe Kosten",
            h2="Was kostet eine Wärmepumpe?",
            intro=("Gerät plus Installation, jeweils vor Förderung. Je nach Gebäude kommen Pufferspeicher, "
                   "Warmwasserspeicher oder Anpassungen am Heizsystem dazu."),
            items=[
                {"size": "Luft-Wasser im Einfamilienhaus", "price": "12.000 bis 22.000 €", "price_sub": "vor Förderung*",
                 "features": ["Gerät 8.000 bis 18.000 €, Installation 3.000 bis 6.000 €",
                              "Keine Bohrung, keine Erschließung nötig",
                              "Bund und Land: 4.000 bis 12.000 € weniger"]},
                {"size": "Luft-Wasser im Altbau", "price": "15.000 bis 28.000 €", "price_sub": "vor Förderung*",
                 "features": ["Inklusive Anpassung von Heizkörpern und Verteilsystem",
                              "Fußbodenheizung nicht zwingend, Nachrüstung 50 bis 120 € je m²",
                              "Nach Förderung typisch 10.000 bis 20.000 €"]},
                {"size": "Erdwärme oder Grundwasser", "price": "22.000 bis 40.000 €", "price_sub": "vor Förderung*",
                 "features": ["Inklusive Kollektor, Tiefenbohrung oder Brunnen",
                              "Höchste Effizienz, niedrigste Betriebskosten",
                              "Bohrbonus des Bundes: 5.000 € zusätzlich"]},
            ],
            note=("*Richtwerte 2026 für Österreich auf Basis unseres Ratgebers Kosten einer Wärmepumpe, "
                  "vor Abzug von Förderungen. Ihren Festpreis erhalten Sie nach der Vor-Ort-Prüfung."),
        ).replace('<section class="section"', '<section id="kosten" class="section"', 1),
        C.media_text(
            eyebrow="Förderung 2026",
            h2="Bis zu 7.500 € vom Bund, dazu Land und Steuerbonus",
            paragraphs=[
                ("Die Sanierungsoffensive 2026 zahlt für den Tausch einer Öl-, Gas-, Kohle- oder "
                 "Elektroheizung gegen eine Wärmepumpe bis zu 7.500 €, bei Erdwärme mit Bohrbonus bis zu "
                 "12.500 €, gedeckelt bei 30 Prozent der Kosten. Kärnten und die Steiermark legen 35 Prozent "
                 "der förderbaren Kosten dazu, Haushalte im unteren Einkommensdrittel erhalten über Sauber "
                 "Heizen für Alle bis zu 100 Prozent."),
                ("Wichtig ist die Reihenfolge: erst Energieberatung, dann Registrierung auf "
                 "sanierungsoffensive.gv.at, dann Auftrag. Danach bleiben 9 Monate für Umsetzung und "
                 "Endabrechnung, registrieren können Sie bis 31. Dezember 2026, solange Budget vorhanden ist. "
                 "Wir organisieren Beratung und Registrierung und planen das Gerät nach den Förderkriterien: "
                 "EHPA-Gütesiegel, Kältemittel mit GWP bis 750, Vorlauf höchstens 55 Grad."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Wärmepumpenförderung am Tisch",
            bullets=[
                "Bund: bis 7.500 €, Erdwärme bis 12.500 €, Deckel 30 Prozent der Kosten",
                "Land Kärnten und Steiermark: 35 Prozent der förderbaren Kosten, mit Bund kombinierbar",
                "Betriebe: bis 7.500 € unter 50 kW, bis 12.000 € bei 50 bis 100 kW (KPC)",
                "Öko-Sonderausgabenpauschale: fünf Jahre je 400 € bei über 2.000 € Restkosten",
                "Finanzierung möglich: 0 € Anzahlung, fixe Rate, Eigentum ab Tag 1",
            ],
            cta=("/waermepumpenfoerderung-in-oesterreich/", "Alle Fördertöpfe 2026 im Überblick"),
            dark=True,
        ),
        C.media_text(
            eyebrow="Wärmepumpe im Altbau",
            h2="Auch mit Heizkörpern: Der Heizungstausch im Bestand",
            paragraphs=[
                ("Dass eine Wärmepumpe nur im Neubau funktioniert, ist überholt. Entscheidend ist die "
                 "Vorlauftemperatur: Fußbodenheizung braucht 30 bis 35 Grad, klassische Altbau-Heizkörper "
                 "oft 60 bis 70 Grad. Bis 55 Grad arbeitet eine moderne Wärmepumpe effizient, und große alte "
                 "Heizkörper sind oft überdimensioniert, was ihr entgegenkommt."),
                ("Beispiel Altbau aus 1985 mit 160 m², teilweise gedämmt: Jahresarbeitszahl 2,8 bis 3,2, "
                 "Stromkosten 1.680 bis 1.920 € statt 2.400 bis 3.000 € mit Gas. Nach Dämmung oder "
                 "Fenstertausch sinken die Kosten auf rund 900 bis 1.020 € im Jahr.*"),
            ],
            img=IMG["gen_detail"],
            alt="Fachkraft von EBZ Energie bei der Montage einer Anlage am Haus",
            bullets=[
                "Heizflächen-Check: Reichen die Heizkörper bei 50 bis 55 Grad Vorlauf?",
                "Keine Fußbodenheizung nötig, Nachrüstung möglich für 50 bis 120 € je m²",
                "Demontage und Entsorgung von Kessel und Tank sind förderfähig",
            ],
            reverse=True,
            cta=("/waermepumpe-im-altbau/", "Ratgeber: Wärmepumpe im Altbau"),
        ),
        C.media_text(
            eyebrow="Photovoltaik, Speicher und Energiemanagement",
            h2="Heizen mit Solarstrom für 10 bis 14 Cent je Kilowattstunde",
            paragraphs=[
                ("Die Betriebskosten einer Wärmepumpe sind fast nur Stromkosten. Eigener Solarstrom kostet "
                 "10 bis 14 ct/kWh, Netzstrom das Zwei- bis Dreifache. Jede Kilowattstunde vom Dach spart "
                 "diese Differenz. Für ein Haus mit Wärmepumpe empfehlen wir 10 bis 15 kWp Photovoltaik und "
                 "einen Speicher mit 10 bis 12 kWh, der den Eigenverbrauch von rund 30 auf 70 bis 80 Prozent hebt."),
                ("Das Energiemanagementsystem verbindet beides: Über die SG-Ready-Schnittstelle lädt es bei "
                 "Sonnenüberschuss Puffer- und Warmwasserspeicher vor und speichert Sonnenenergie als Wärme. "
                 "Beide Systeme werden getrennt gefördert: die Wärmepumpe über die Sanierungsoffensive, die "
                 "PV-Anlage über den EAG-Zuschuss mit 150 € je kWp und 150 € je kWh Speicher."),
            ],
            img=IMG["ems"],
            alt="Energiemanagementsystem steuert Photovoltaik, Speicher und Wärmepumpe",
            bullets=[
                "PV-Anlage 10 kWp mit Speicher: rund 15.000 bis 22.000 € vor Förderung*",
                "Energiekosten für Heizung, Warmwasser und Haushalt: 50 bis 70 Prozent weniger*",
                "Im Sommer kühlt die Wärmepumpe mit dem eigenen Überschussstrom",
            ],
            cta=("/photovoltaik-fuer-waermepumpe/", "Ratgeber: Photovoltaik für die Wärmepumpe"),
        ),
        C.media_text(
            eyebrow="Wärmepumpe für Gewerbe",
            h2="Für Ihren Betrieb: Heizkosten senken, Förderung nach Umsetzung",
            paragraphs=[
                ("Werkstatt, Bürogebäude, Vereinslokal oder Gemeindeamt: Im Betrieb laufen Heizsysteme länger "
                 "und für größere Flächen. Wir planen nach Heizlast und Lastprofil und stimmen die Wärmepumpe "
                 "auf eine PV-Anlage am Betriebsdach ab, die tagsüber genau dann liefert, wenn der Betrieb "
                 "Strom braucht. Die Betriebsförderung der KPC zahlt für den Tausch eines fossilen Heizsystems "
                 "bis zu 7.500 € unter 50 kW und bis zu 12.000 € bei 50 bis 100 kW, maximal 50 Prozent der "
                 "Kosten. Der Antrag wird erst nach Umsetzung gestellt, spätestens 6 Monate nach der Schlussrechnung."),
            ],
            img=IMG["gen_gewerbe"],
            alt="Große Photovoltaikanlage auf einem Gewerbedach, Stromquelle für die Wärmepumpe",
            bullets=[
                "Planung nach Heizlast, Lastprofil und Betriebszeiten",
                "Kombination mit PV-Anlage: Beispiel Gewerbe OÖ, 40 kWp, rund 13.500 € Ersparnis im Jahr",
                "Landesförderungen in vielen Fällen zusätzlich kombinierbar",
            ],
            reverse=True,
            anchor="gewerbe",
            cta=("kontakt", "Gewerbe-Beratung anfragen"),
        ),
        C.founder_story(
            eyebrow="Persönliche Beratung vor Ort",
            h2="Mario Zintl schaut sich Ihren Heizraum selbst an",
            paragraphs=[
                ("Eine Wärmepumpe kann man nicht aus dem Katalog verkaufen. Ob sie bei Ihnen gut läuft, "
                 "entscheidet sich im Heizraum, an den Heizkörpern und an der Dämmung. Deshalb kommen wir "
                 "zu Ihnen nach Kärnten oder in die Steiermark, bevor wir irgendetwas anbieten."),
                ("Dort rechnen wir gemeinsam: Was heizen Sie heute, was kostet das, welche Vorlauftemperatur "
                 "brauchen Ihre Heizflächen und was bringt die Kombination mit Photovoltaik. Manchmal ist die "
                 "ehrliche Antwort, dass erst die Fenster dran sind oder dass eine kleinere Anlage reicht. "
                 "Sie bekommen ein Festpreisangebot und den Förderweg dazu."),
            ],
            quote="Ich will, dass Ihre Wärmepumpe in zehn Jahren noch so läuft, wie wir es Ihnen heute sagen.",
            name=AUTHOR, role=AUTHOR_ROLE,
            badge="Villach, Kärnten",
            cta=("kontakt", "Vor-Ort-Termin vereinbaren"),
        ),
        C.why_section(
            eyebrow="Warum EBZ Energie",
            h2="Ihr Wärmepumpen-Fachbetrieb aus Villach",
            items=[
                ("♨", "Heizung, PV und Speicher aus einer Hand", "Ein Ansprechpartner für Wärmepumpe, Photovoltaik, Speicher, Energiemanagement und Förderung."),
                ("✓", "Zertifizierte Fachkräfte", "Meisterhaftes Handwerk, Sanitär und Elektro fachgerecht in einem Projekt."),
                ("★", "4,9 Sterne auf Google", "Bewertungen von Kundinnen und Kunden aus Kärnten und der Steiermark."),
                ("◎", "300+ Projekte", "Erfahrung aus über 300 dokumentierten Anlagen in 6 Bundesländern."),
                ("€", "Förderung komplett abgewickelt", "Energieberatung, Registrierung, Endabrechnung: Wir halten Fristen und Kriterien im Blick."),
                ("⌂", "Regional vor Ort", "Zuhause in Villach, Montage in Kärnten und der Steiermark, erreichbar auch nach der Übergabe."),
            ],
        ),
        C.reviews_slider(reviews, rating, count),
        C.steps_section(
            eyebrow="So läuft es ab",
            h2="Von der Beratung zur warmen Stube",
            steps=[
                ("Beratung", "Heizbedarf, Gebäude und Ziele. Kostenlos und ohne Verkaufsdruck.", ""),
                ("Vor-Ort-Prüfung", "Heizraum, Heizflächen, Dämmung und Elektrik als Grundlage für Heizlast und Festpreisangebot.", ""),
                ("Förderung sichern", "Energieberatung und Registrierung vor dem Auftrag, danach 9 Monate Frist.", ""),
                ("Montage", "Demontage der alten Heizung, Einbau, Sanitär und Elektro aus einer Hand.", "2 bis 4 Tage"),
                ("Inbetriebnahme", "Einregulierung, Übergabe, Endabrechnung der Förderung. Wir bleiben erreichbar.", ""),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section(
            "Mehr zur Wärmepumpe",
            [("/kosten-einer-waermepumpe/", "Kosten einer Wärmepumpe"),
             ("/heizen-mit-waermepumpe/", "Heizen mit Wärmepumpe"),
             ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau"),
             ("/funktionsweise-einer-waermepumpe/", "Funktionsweise einer Wärmepumpe"),
             ("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"),
             ("/waermepumpenfoerderung-in-oesterreich/", "Wärmepumpenförderung 2026"),
             ("/sanierungsoffensive-2026/", "Sanierungsoffensive 2026"),
             ("/sauber-heizen-fuer-alle-2026/", "Sauber Heizen für Alle"),
             ("photovoltaik", "Photovoltaik"),
             ("ems", "Energiemanagement"),
             ("finanzierung", "Finanzierung"),
             ("referenzen", "Referenzen")],
        ),
        C.contact_section(
            headline="Ihre Wärmepumpe: kostenlos geprüft, zum Festpreis angeboten",
            sub=("Sagen Sie uns, wie Sie heute heizen. Wir prüfen Gebäude, Heizflächen und Förderhöhe vor "
                 "Ort und sagen Ihnen ehrlich, was die Wärmepumpe bei Ihnen bringt. Kostenlos und unverbindlich."),
            page_label="Wärmepumpe",
        ),
        C.finalcta(
            "Noch eine Heizsaison mit Öl oder Gas?",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags und "
            "rechnen Heizkosten, Förderung und Photovoltaik für Ihr Haus durch.",
            trust=[(f"{NAP['rating']} auf Google", True), ("bis 7.500 € Bundesförderung", False),
                   ("Montage 2 bis 4 Tage", False), ("Kostenlos und unverbindlich", False)],
        ),
        _footnote(),
    ])

    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=IMG["waermepumpe"])
    return write_page(OUT_FILE, html)


def _footnote():
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte 2026 für Österreich aus unseren Ratgebern, vor Förderung. Beispielhaus mit
      12.000 kWh Wärmebedarf, Jahresarbeitszahl 4, Strompreis 0,30 €/kWh. Förderzahlen nach Stand der Programme
      (Sanierungsoffensive 2026, Landesförderungen Kärnten und Steiermark, KPC-Betriebsförderung), Stand April 2026,
      laufend aktualisiert im Ratgeber. Tatsächliche Kosten, Ersparnis und Förderhöhe hängen von Gebäude,
      Heizsystem, Wärmequelle und Programmbudget ab. Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    import theme
    theme.write_assets()
    build()
