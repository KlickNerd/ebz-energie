"""Leistungsseite Photovoltaik (/photovoltaik/).

Roter Faden (Conversion): Hook -> abholen (Eigenheim/Gewerbe) -> verstehen
(Definition, Groesse, Speicher) -> Geld-Fragen offen (Kosten, Finanzierung,
Foerderung) -> Reibung raus (Anmeldung, laufende Kosten) -> warum EBZ -> Beweis
-> Ablauf -> FAQ -> Region -> eine klare Handlung (kostenlose Beratung).

SEO/GEO-Briefing build/seo/photovoltaik.json (Stand 2026-10-09): Primaer
"photovoltaikanlage" (8.100), Kauf-Modifier, "PV-Anlage" als Synonym. Gewerbe
wird auf /photovoltaik-gewerbe/ ausgelagert (Kannibalisierung), Info-Themen auf
die Ratgeber verlinkt. Zahlen: build/seo/_fakten_2026-10.md, freigegebene
Referenzen, bestehende Ratgeber. Verbote beachtet (85 %, 4,9, Finanzierung,
Projektbericht, keine Gedankenstriche).
"""

from common import CLAIMS, NAP, IMG, faq_jsonld, u, a, href, write_page, load_reviews
from layout import page
import components as C

PATH = "/photovoltaik/"
TITLE = "Photovoltaikanlage kaufen in Kärnten & Steiermark | EBZ"
DESC = ("Photovoltaikanlage mit Speicher vom Fachbetrieb in Kärnten und der Steiermark: 10 kWp ab rund "
        "15.000 €, bis zu 85 % weniger Stromkosten, Förderung inklusive.")

FAQ = [
    ("Was kostet eine Photovoltaikanlage mit Speicher?",
     "Eine Komplettanlage 10 kWp mit Speicher und Montage kostet rund 15.000 bis 22.000 € vor Förderung "
     "(Stand Oktober 2026). Nach EAG-Zuschuss (bis 3.000 €) und Kärntner Landespauschale (3.000 €) bleiben in "
     "Kärnten typischerweise 9.000 bis 16.000 €, je nach Dach, Speichergröße und Notstrom."),
    ("Lohnt sich eine Photovoltaikanlage in Österreich und wie schnell rechnet sie sich?",
     "Ja. Anlagen von EBZ Energie rechnen sich meist innerhalb von 4 bis 6 Jahren, je nach Eigenverbrauch und "
     "Strompreis. Danach liefern die Module bei 25 bis 30 Jahren Lebensdauer günstigen Strom, die Ersparnis liegt "
     "bei bis zu 85 % der Stromkosten."),
    ("Wie viel Strom erzeugen 10 kWp in Kärnten pro Jahr?",
     "Rund 10.000 bis 11.000 kWh. Die EBZ-Referenz in Villach erzeugt mit 10 kWp in Ost-West-Ausrichtung rund "
     "11.000 kWh im Jahr, also etwa 1.100 kWh je kWp. Richtwert für Kärnten und die Steiermark: 1.000 bis 1.100 kWh "
     "je kWp, abhängig von Ausrichtung und Verschattung.*"),
    ("Funktioniert Photovoltaik auch im Winter und bei Schnee?",
     "Ja, mit weniger Ertrag: Im Winterhalbjahr liefern Anlagen typischerweise 25 bis 30 Prozent des Jahresertrags. "
     "Schnee rutscht von geneigten Glas-Glas-Modulen meist von selbst ab, bifaziale Module nutzen zusätzlich "
     "reflektiertes Licht. Den Rest liefern Speicher oder Netz."),
    ("Ist eine Photovoltaikanlage mit oder ohne Speicher besser, und kann ich später nachrüsten?",
     "Mit Speicher steigt der Eigenverbrauch von rund 30 auf 60 bis 80 %*, Sonnenstrom gibt es auch am Abend. "
     "Nachrüsten geht fast immer, AC-gekoppelt für 800 bis 1.200 € je kWh*. Kärnten fördert die Nachrüstung 2026 "
     "mit 1.000 €, der EAG-Zuschuss von 150 € je kWh gilt nur mit neuer Anlage."),
    ("Wie hoch ist die Förderung für Photovoltaik 2026 in Kärnten und der Steiermark?",
     "Bund: EAG-Zuschuss 150 € je kWp bis 10 kWp und 150 € je kWh Speicher, letzter Fördercall 8. bis 22. Oktober "
     "2026. Land Kärnten: 3.000 € pauschal für Neuanlagen ab 5 kWp mit Speicher ab 5 kWh, Antrag 12. Oktober bis "
     "31. Dezember 2026, mit dem Bund kombinierbar. Steiermark: eigene Landesprogramme, siehe Ratgeber. Ab 2027 "
     "plant der Bund eine Systemförderung (Stand Oktober 2026)."),
    ("Brauche ich eine Genehmigung und wie lange dauert die Anmeldung beim Netzbetreiber?",
     "In Kärnten sind Dach- und Fassadenanlagen meist nicht bewilligungspflichtig, es gilt eine Mitteilungspflicht "
     "an die Gemeinde. Den Netzzutrittsantrag stellen wir direkt nach dem Auftrag, weil die Zählpunktnummer für den "
     "EAG-Antrag nötig ist; die Prüfung des Netzbetreibers dauert je nach Netzgebiet einige Wochen."),
    ("Welche laufenden Kosten hat eine Photovoltaikanlage?",
     "Rund 1 bis 2 % der Anschaffung pro Jahr, bei 15.000 bis 22.000 € also 150 bis 440 €* für Wartung, Reinigung "
     "und Rücklagen. Die Versicherung kostet meist unter 100 € im Jahr, der Wechselrichter wird nach rund 15 Jahren "
     "getauscht."),
    ("Welche Garantien gibt es auf Module, Wechselrichter und Speicher?",
     "Bis zu 30 Jahre Leistungsgarantie auf die Module und mindestens 10 Jahre Produktgarantie. Wechselrichter von "
     "Huawei oder Fronius haben meist 10 Jahre Garantie, verlängerbar; Speicher 10 Jahre auf mindestens 80 % "
     "Restkapazität. Ansprechpartner bleiben wir auch nach der Übergabe."),
    ("Lohnt sich Photovoltaik auch für Betriebe?",
     "Besonders: Betriebe verbrauchen tagsüber, wenn die Anlage produziert. Referenz Oberösterreich: 40 kWp "
     "Ost-West auf Trapezblech mit 40 kWh Speicher, rund 40.000 kWh im Jahr und 13.500 € Ersparnis jährlich. Mehr "
     "auf der Seite Photovoltaik für Gewerbe."),
]


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        # 1. Hook
        C.hero(
            eyebrow="Photovoltaikanlage kaufen in Kärnten und der Steiermark: Eigenheim und Gewerbe",
            h1="Photovoltaikanlage vom Fachbetrieb: Ihr eigener Strom vom Dach in Kärnten und der Steiermark",
            lead=("Eine Photovoltaikanlage mit 10 kWp und Speicher kostet bei EBZ Energie rund 15.000 bis 22.000 € "
                  "vor Förderung und senkt Ihre Stromkosten um bis zu 85 %. Wir planen, montieren und betreuen Ihre "
                  "PV-Anlage aus einer Hand: zertifizierte Fachkräfte aus Villach, Förderanträge und Netzanmeldung "
                  "inklusive."),
            badges=[("300+", "Anlagen gebaut"),
                    ("ab 147 €", "im Monat finanziert*"),
                    ("Regional", "aus Villach")],
            img=IMG["gen_hero"],
            img_alt="Photovoltaikanlage mit Solarmodulen auf dem Dach eines Einfamilienhauses in Kärnten",
            float_num=rating,
            float_label=f"aus {count} Google Bewertungen" if count else "auf Google",
        ),
        # Quick Trust
        C.kpis([
            ("300+", "umgesetzte Projekte"),
            (NAP["rating"], "Sterne auf Google"),
            ("bis zu 85 %", "weniger Stromkosten"),
            ("4 bis 6 Jahre", "typische Amortisation"),
        ]),
        # Definition + Infografik (GEO)
        C.pv_explainer(
            eyebrow="Kurz erklärt",
            h2="Was ist eine Photovoltaikanlage?",
            paragraphs=[
                ("Eine Photovoltaikanlage (kurz PV-Anlage) wandelt Sonnenlicht in Strom um. Sie besteht aus "
                 "Solarmodulen, einem Wechselrichter, dem Montagesystem und einem Zählpunkt beim Netzbetreiber. Die "
                 "Module erzeugen Gleichstrom, der Wechselrichter macht daraus Wechselstrom für Haushalt oder "
                 "Betrieb. Überschuss wird gespeichert oder eingespeist."),
                ("Typische Anlage von EBZ Energie: Glas-Glas-Module (auf Wunsch bifazial, sie nutzen auch Licht "
                 "von der Rückseite), ein Hybridwechselrichter, der den Batteriespeicher gleich mitsteuert, und "
                 "Komponenten von Herstellern wie Huawei, Fronius oder BYD, je nach Projekt. Ein Monitoring zeigt "
                 "Ertrag und Verbrauch am Handy."),
            ],
            note_title="Am Abend und bei wenig Sonne",
            note_text="Ein Batteriespeicher liefert den Sonnenstrom später. Sonst kommt Strom aus dem Netz.",
        ),
        # 2. Abholen: Eigenheim oder Gewerbe (Gewerbe geht auf die eigene Seite)
        C.audience_split(
            eyebrow="Für wen planen wir?",
            h2="Ob Eigenheim oder Betrieb: Ihre PV-Anlage passt zu Ihnen",
            intro="Wählen Sie, was auf Sie zutrifft. Wir richten Planung, Größe und Wirtschaftlichkeit genau danach aus.",
            left={
                "img": IMG["gen_eigenheim"],
                "alt": "Einfamilienhaus mit Photovoltaikanlage in Kärnten",
                "title": "Für Ihr Eigenheim",
                "bullets": [
                    "Bis zu 85 % weniger Stromkosten",
                    "Speicher und Notstrom für den Abend",
                    "Volle Förderung und Finanzierung ab 147 € im Monat*",
                ],
                "cta": ("kontakt", "Beratung für mein Zuhause"),
            },
            right={
                "img": IMG["gen_gewerbe"],
                "alt": "Gewerbebetrieb mit großer Photovoltaikanlage am Dach",
                "title": "Für Ihren Betrieb",
                "bullets": [
                    "Hoher Eigenverbrauch tagsüber senkt die Betriebskosten",
                    "Große Dächer: Flachdach, Trapezblech, Planung nach Lastprofil",
                    "Beispiel Gewerbe OÖ: 40 kWp, rund 13.500 € Ersparnis pro Jahr",
                ],
                "cta": ("pv_gewerbe", "Photovoltaik für Gewerbe"),
            },
        ),
        # 3. Groesse und Ertrag (GEO-Zahl kWh je kWp)
        C.cards_section(
            eyebrow="Anlagengröße und Ertrag",
            h2="Wie groß soll Ihre PV-Anlage sein?",
            intro=("In Kärnten und der Steiermark liefert eine Photovoltaikanlage rund 1.000 bis 1.100 kWh je kWp "
                   "und Jahr: Die EBZ-Referenz in Villach erzeugt mit 10 kWp in Ost-West-Ausrichtung rund 11.000 kWh, "
                   "die 40-kWp-Anlage in Oberösterreich rund 40.000 kWh (Projektberichte EBZ Energie, Stand Oktober "
                   "2026). Faustregel für die Planung: rund 1 bis 1,5 kWp je 1.000 kWh Jahresverbrauch.*"),
            cards=[
                {"ic": "⌂", "title": "Haushalt bis 4.500 kWh",
                 "text": "4 bis 7 kWp mit 4 bis 8 kWh Speicher. Deckt Grundlast, Küche und Waschmaschine, der Überschuss reicht für den Abend."},
                {"ic": "☀", "title": "Familie mit rund 6.000 kWh",
                 "text": "8 bis 10 kWp mit 8 bis 10 kWh Speicher. Die Komplettanlage 10 kWp mit Speicher ist unsere häufigste Anlage, auf Wunsch mit Notstrom.",
                 "link_key": "/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/", "link_text": "Komplettanlage 10 kWp im Detail"},
                {"ic": "♨", "title": "Mit Wärmepumpe oder E-Auto",
                 "text": "10 bis 15 kWp mit 10 bis 15 kWh Speicher. Ost-West-Ausrichtung verteilt den Ertrag über den Tag, Verschattung prüfen wir im 3D-Belegplan.",
                 "link_key": "solarrechner", "link_text": "Im Solarrechner durchrechnen"},
            ],
        ),
        # 4. Warum jetzt
        C.problem_compare(
            eyebrow="Warum sich der Umstieg jetzt lohnt",
            h2="Weniger zukaufen, mehr Unabhängigkeit",
            intro=("Netzstrom kostet rund 30 bis 35 ct je kWh, eingespeister Solarstrom bringt im OeMAG-Marktpreismodell "
                   "10,168 ct (September 2026). Was Sie selbst erzeugen und verbrauchen, müssen Sie nicht teuer aus "
                   "dem Netz kaufen.*"),
            bars=[
                ("Stromkosten ohne eigene Anlage", 100, "bad", "voller Netzbezug"),
                ("Stromkosten mit Photovoltaik und Speicher", 15, "good", "bis zu 85 % weniger*"),
            ],
            aside=("Ihre Vorteile auf einen Blick", [
                ("☀", "Eigener Strom", "Sie produzieren Ihren Strom selbst, 25 bis 30 Jahre lang."),
                ("€", "Planbare Kosten", "Unabhängiger von steigenden Strompreisen."),
                ("▮", "Auch am Abend", "Mit Speicher nutzen Sie Sonnenstrom rund um die Uhr."),
                ("✓", "Ohne Aufwand", "Wir kümmern uns um Förderung, Anmeldung und Montage."),
            ]),
        ),
        # 5. Verstehen: Speicher, Autarkie (Bausteine Wallbox/EMS/Waermepumpe ueber Links)
        C.media_text(
            eyebrow="Photovoltaik mit Speicher",
            h2="Mehr Eigenverbrauch und Autarkie mit Batteriespeicher",
            paragraphs=[
                ("Ohne Speicher nutzen Sie rund 30 % Ihres Sonnenstroms selbst, mit passend geplantem Batteriespeicher "
                 "60 bis 80 %*. Bei 10 kWp mit Speicher erreichen Haushalte typischerweise rund 70 % Autarkie, kaufen "
                 "also nur noch knapp ein Drittel ihres Stroms zu (Richtwerte EBZ Energie, Stand Oktober 2026)."),
                ("Mit Notstromfunktion bleibt Ihr Haus auch bei Stromausfall versorgt. Ein Speicher lässt sich fast "
                 "immer " + a("/pv-speicher-nachruesten/", "nachrüsten") + ", am einfachsten AC-gekoppelt mit eigenem "
                 "Batteriewechselrichter."),
            ],
            img=IMG["speicher"],
            alt="Batteriespeicher einer Photovoltaikanlage im Technikraum",
            bullets=[
                "Eigenverbrauch statt Einspeisevergütung zu 10,168 ct je kWh (OeMAG-Marktpreis September 2026)",
                "Der Hybridwechselrichter steuert auch Wallbox und Wärmepumpe mit, das Monitoring zeigt alles am Handy",
                "Nachrüstung möglich: Kärnten fördert sie 2026 mit 1.000 €",
            ],
            reverse=True,
            cta=("batteriespeicher", "Batteriespeicher für Ihre PV-Anlage"),
        ),
        # 6. Geld-Fragen offen beantworten (GEO-Passage Kosten)
        C.price_cards(
            eyebrow="PV Anlage kaufen: Preise 2026",
            h2="Was kostet eine Photovoltaikanlage?",
            intro=("Eine Photovoltaikanlage mit 10 kWp und Speicher kostet in Österreich rund 15.000 bis 22.000 € vor "
                   "Förderung (EBZ-Richtpreis, Stand Oktober 2026, inklusive 20 % Umsatzsteuer). Der EAG-Investitionszuschuss "
                   "beträgt 150 € je kWp bis 10 kWp und 150 € je kWh Speicher, zusammen bis zu 3.000 € (Quelle: "
                   "EAG-Abwicklungsstelle)."),
            items=[
                {"size": "Kleine Anlage", "price": "ab ca. 9.000 €", "price_sub": "rund 5 kWp, ohne Speicher*",
                 "features": ["Ideal für kleinere Haushalte", "Hoher Eigenverbrauch am Tag", "Später um Speicher erweiterbar"]},
                {"size": "Beliebte Größe", "price": "15.000 bis 22.000 €", "price_sub": "rund 10 kWp mit Speicher*",
                 "features": ["Komplettanlage 10 kWp mit Speicher und Montage", "Hybridwechselrichter, Speicher und Anmeldung inklusive", "Optional mit Notstrom"]},
                {"size": "Gewerbe und große Dächer", "price": "individuell", "price_sub": "ab rund 20 kWp*",
                 "features": ["Für Betriebe und große Haushalte", "Flachdach oder Trapezblech, Planung nach Lastprofil",
                              a("pv_gewerbe", "Photovoltaik für Gewerbe und Landwirtschaft →")]},
            ],
            note=("*Richtwerte auf Basis typischer Projekte, vor Förderung. Alle Kostenblöcke im Detail: "
                  + a("/kosten-einer-solaranlage/", "Was kostet eine Solaranlage") + "."),
        ),
        C.finance_band(),
        C.media_text(
            eyebrow="Förderungen 2026",
            h2="Förderungen 2026: EAG-Zuschuss, Fördercall Oktober, Land Kärnten und Steiermark",
            paragraphs=[
                ("Der Bund fördert Photovoltaik 2026 über den EAG-Investitionszuschuss: 150 € je kWp bis 10 kWp "
                 "(Kategorie A), 140 € bis 20 kWp, 130 € bis 100 kWp, dazu 150 € je kWh Speicher und 10 % "
                 "Made-in-Europe-Bonus je Komponente. Der 3. Fördercall 8. bis 22. Oktober 2026 ist der letzte im "
                 "alten System (Quelle: EAG-Abwicklungsstelle, Stand Oktober 2026)."),
                ("Das Land Kärnten fördert private PV-Anlagen ab 5 kWp mit mindestens 5 kWh Speicher pauschal mit "
                 "3.000 €, die Speicher-Nachrüstung mit 1.000 €: Antrag online vom 12. Oktober bis 31. Dezember 2026, "
                 "maximal 50 % der Investitionskosten, Budget rund 10 Mio. € (Quelle: Land Kärnten). Ab 2027 plant der "
                 "Bund laut BMWET eine Systemförderung für Speicher mit intelligenter Steuerung. Wir stellen alle "
                 "Anträge für Sie."),
            ],
            img=IMG["foerderung"],
            alt="Beratung zur Photovoltaik Förderung am Tisch",
            bullets=[
                "Land Kärnten PV-Förderung 2026: 3.000 € pauschal, Bund und Land kombinierbar",
                "Speicherförderung 150 €/kWh (mindestens 0,5 kWh je kWp, maximal 50 kWh)",
                a("foerderung_kaernten", "PV-Förderung Kärnten 2026") + " und " + a("foerderung_steiermark", "PV-Förderung Steiermark 2026") + " im Detail",
            ],
            cta=("foerderung_at", "EAG-Fördercall Oktober 2026 im Überblick"),
        ),
        # 7. Reibung raus: Anmeldung und Genehmigung
        C.media_text(
            eyebrow="Anmeldung und Genehmigung",
            h2="Anmeldung beim Netzbetreiber und Mitteilungspflicht: so läuft es in Kärnten",
            paragraphs=[
                ("In Kärnten sind Photovoltaikanlagen auf Dächern und an Fassaden meist nicht bewilligungspflichtig, "
                 "es gilt eine Mitteilungspflicht an die Gemeinde (Kärntner Bauordnung, Stand Oktober 2026). "
                 "Verpflichtend ist der Netzzutrittsantrag beim Netzbetreiber: Erst mit der technischen Freigabe und "
                 "der Zählpunktnummer sind Einspeisevertrag und EAG-Antrag möglich."),
                ("Wir übernehmen den Ablauf: Netzzutrittsantrag bei Kärnten Netz oder Energienetze Steiermark direkt "
                 "nach dem Auftrag, Mitteilung an die Gemeinde, nach der Montage Fertigstellungsmeldung, Zählertausch "
                 "und Einspeisevertrag. Weil das Netz in Kärnten und der Steiermark voller wird, reichen wir den "
                 "Netzantrag so früh wie möglich ein."),
            ],
            img=IMG["gen_detail"],
            alt="Fachkraft von EBZ Energie montiert Photovoltaikmodule auf einem Dach in Kärnten",
            bullets=[
                "Dach-PV in Kärnten: Mitteilung an die Gemeinde statt Baubewilligung, Schutzzonen ausgenommen",
                "Netzzutrittsantrag liefert die Zählpunktnummer für Förderung und Einspeisung",
                "Steiermark: Netzzutritt bei Energienetze Steiermark, Bauordnung der Gemeinde klären wir mit",
            ],
            reverse=True,
        ),
        # 8. Laufende Kosten, Wartung, Garantien (zitierbare Tabelle)
        C.facts_panel(
            eyebrow="Betrieb über 25 Jahre",
            h2="Laufende Kosten, Wartung und Garantien",
            intro=("Die laufenden Kosten einer Photovoltaikanlage liegen bei rund 1 bis 2 % der Anschaffung pro Jahr, "
                   "also 150 bis 440 € bei einer 10-kWp-Anlage mit Speicher*: Wartung, gelegentliche Reinigung, "
                   "Versicherung (meist unter 100 € im Jahr), Zählergebühr und Rücklage für den Wechselrichtertausch "
                   "nach rund 15 Jahren (EBZ Energie, Stand Oktober 2026)."),
            rows=[
                ("Solarmodule", "Lebensdauer 25 bis 30 Jahre, bis zu 30 Jahre Leistungsgarantie"),
                ("Wechselrichter", "rund 15 Jahre, mindestens 10 Jahre Produktgarantie, bei Huawei oder Fronius verlängerbar"),
                ("Batteriespeicher", "10 bis 15 Jahre, 10 Jahre Garantie auf mindestens 80 % Restkapazität"),
                ("Reinigung", "Regen reicht meist; nur nahe Landwirtschaft oder Industrie alle paar Jahre professionell"),
                ("Versicherung und Zähler", "Anlagenversicherung meist unter 100 € im Jahr, dazu eine geringe Zählergebühr"),
                ("Monitoring", "App zeigt Ertrag und Störungen; EBZ bleibt Ansprechpartner nach der Übergabe"),
            ],
            actions=[("Kosten einer Solaranlage im Detail", href("/kosten-einer-solaranlage/"), "")],
        ),
        # Menschlicher Anker
        C.founder_story(
            eyebrow="Ein Wort von Mario Zintl",
            h2="Warum Photovoltaik für mich mehr ist als Technik",
            paragraphs=[
                ("Ich bin in Villach aufgewachsen. Als ich mit Photovoltaik begonnen habe, ging es mir nie nur um "
                 "Module auf Dächern, sondern darum, dass Familien und Betriebe hier ihre Energie selbst in der Hand "
                 "haben, unabhängig von steigenden Preisen."),
                ("Wenn eine Kundin nach der Inbetriebnahme zum ersten Mal sieht, wie viel Strom ihr eigenes Dach "
                 "liefert, ist das der Moment, für den ich das mache. Deshalb plane ich jede Anlage so, als wäre es "
                 "meine eigene: ehrlich beraten, sauber gebaut, danach erreichbar."),
            ],
            quote="Wir verkaufen keine Module, wir bauen Unabhängigkeit.",
            name="Mario Zintl",
            role="Geschäftsführung EBZ Energie GmbH",
            badge="Gebürtiger Villacher",
        ),
        # 9. Warum EBZ
        C.why_section(
            eyebrow="Warum EBZ Energie",
            h2="Warum EBZ: Fachbetrieb aus Villach, 300+ Anlagen, 4,9 Sterne",
            items=[
                ("☀", "Alles aus einer Hand", "Planung, Montage, Förderung, Netzanmeldung und Service. Ein Ansprechpartner für alles."),
                ("✓", "Zertifizierte Fachkräfte", "Meisterhaftes Handwerk und sorgfältige Ausführung."),
                ("★", "4,9 Sterne auf Google", "Bewertungen von echten Kundinnen und Kunden aus der Region."),
                ("◉", "300+ Anlagen", "Erfahrung aus über 300 dokumentierten Projekten in 6 Bundesländern."),
                ("€", "Faire Finanzierung", "Ihre Anlage gehört Ihnen ab Tag 1. Ab 147 € im Monat inklusive Speicher.*"),
                ("⌂", "Regional verwurzelt", "Zuhause in Villach, im Einsatz für Kärnten und die Steiermark."),
            ],
        ),
        # 10. Beweis
        C.reference_cards(
            eyebrow="Aus der Praxis",
            h2="Referenzen mit Zahlen: Anlagen, die sich rechnen",
            intro=("Ziegeldach, Mehrparteienhaus, Trapezblech: drei Projekte aus Eigenheim und Gewerbe. Bild und "
                   "Zahlen gehören jeweils zum selben Projekt."),
            items=[
                {"img": IMG["ref_villach"], "alt": "Photovoltaikanlage auf einem Einfamilienhaus in Villach",
                 "title": "Einfamilienhaus, Villach", "specs": "10 kWp Ost-West mit Notstrom, rund 11.000 kWh im Jahr.",
                 "result": "rund 80 %", "result_sub": "weniger Stromkosten"},
                {"img": IMG["ref_krumpendorf"], "alt": "Photovoltaikanlage auf einem Mehrparteienhaus in Krumpendorf",
                 "title": "Mehrparteienhaus, Krumpendorf", "specs": "25 kWp mit 25 kWh Speicher und Notstrom, Montage in 4 Tagen.",
                 "result": "4 Tage", "result_sub": "Bauzeit"},
                {"img": IMG["gewerbe_dach"], "alt": "Große Photovoltaikanlage auf einem Gewerbedach in Oberösterreich",
                 "title": "Gewerbe, Oberösterreich", "specs": "40 kWp Ost-West auf Trapezblech, 40 kWh Speicher, rund 40.000 kWh im Jahr.",
                 "result": "13.500 €", "result_sub": "Ersparnis pro Jahr"},
            ],
        ),
        C.reviews_slider(reviews, rating=rating, count=count),
        # 11. Ablauf (inkl. Montage-Details)
        C.steps_section(
            eyebrow="So einfach läuft es ab",
            h2="Ablauf von der Beratung zum eigenen Sonnenstrom",
            steps=[
                ("Beratung", "Verbrauch, Dach und Ziele. Kostenlos, unverbindlich, auf Wunsch bei Ihnen vor Ort in Kärnten oder der Steiermark.", "Tag 1"),
                ("Projektbericht", "Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport, dazu Förderübersicht und Festpreis.", "wenige Tage"),
                ("Anträge", "Netzzutrittsantrag, Mitteilung an die Gemeinde, EAG- und Landesantrag: alles vor der Montage und fristgerecht.", "vor der Montage"),
                ("Montage", "Zertifizierte Fachkräfte montieren auf Ziegel, Trapezblech, Blechfalz oder Flachdach. Bauzeit je nach Größe 1 bis 4 Tage (25 kWp in Krumpendorf: 4 Tage).", "1 bis 4 Tage"),
                ("Inbetriebnahme", "Fertigstellungsmeldung, Zählertausch, Einspeisevertrag, Monitoring und Übergabe. Wir bleiben erreichbar.", ""),
            ],
        ),
        C.faq_section(FAQ),
        # 12. Region (Local-Pack-Signale, ohne die Standortseiten zu kannibalisieren)
        C.text_block(
            eyebrow="Photovoltaik in Ihrer Region",
            h2="Photovoltaik Kärnten und Steiermark: Villach, Klagenfurt, Wolfsberg, Graz",
            paragraphs=[
                ("EBZ Energie ist eine Photovoltaik Firma mit Sitz in Villach (Triglavstraße 15) und montiert in ganz "
                 "Kärnten und der Steiermark: von Villach, Landskron und Warmbad über Klagenfurt und Wolfsberg bis "
                 "Graz. Über 300 dokumentierte Projekte in sechs Bundesländern, Google-Bewertung 4,9 Sterne, bis zu "
                 "30 Jahre Leistungsgarantie (Stand Oktober 2026)."),
                ("Sie suchen einen Photovoltaik Anbieter in Ihrer Nähe? Wir kommen zur Beratung zu Ihnen, mit "
                 "Projektbericht, 3D-Belegplan und Statikreport für Ihr Dach."),
            ],
        ),
        C.linkgrid_section(
            "Weiterlesen: Standorte, Förderung, Kosten",
            [("pv_villach", "Photovoltaik Villach"),
             ("pv_wolfsberg", "Photovoltaik Wolfsberg"),
             ("foerderung_kaernten", "PV-Förderung Kärnten 2026"),
             ("foerderung_steiermark", "PV-Förderung Steiermark 2026"),
             ("foerderungen", "Alle Förderungen 2026"),
             ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage"),
             ("/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/", "Komplettanlage 10 kWp mit Speicher"),
             ("batteriespeicher", "Batteriespeicher"),
             ("waermepumpe", "Wärmepumpe mit Solarstrom"),
             ("ems", "Energiemanagement"),
             ("carport", "PV-Carport mit Wallbox"),
             ("pv_gewerbe", "Photovoltaik für Gewerbe"),
             ("solarrechner", "Solarrechner"),
             ("finanzierung", "PV-Anlage finanzieren"),
             ("referenzen", "Referenzen")],
        ),
        C.contact_section(
            headline="Ihr kostenloses Angebot für Ihre Photovoltaikanlage",
            sub=("Sie erreichen uns telefonisch oder über das Formular. Wir zeigen Ihnen ehrlich, "
                 "was auf Ihrem Dach möglich ist und was es kostet. Kostenlos und unverbindlich."),
            page_label="Leistungsseite Photovoltaik",
        ),
        # 13. Die einzige logische Handlung
        C.finalcta(
            "Bereit für Ihren eigenen Sonnenstrom?",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags "
            "und nehmen uns Zeit für Ihre Fragen.",
        ),
        _footnote(),
    ])

    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ), include_business_schema=True,
                og_image="/assets/img/pv-hero-roof.jpg")
    return write_page("photovoltaik/index.html", html)


def _footnote():
    return ("""
  <section class="section--tight section" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte auf Basis typischer EBZ-Projekte in Kärnten und der Steiermark, vor Förderung,
      Stand Oktober 2026. Preis, Ertrag, Eigenverbrauch, Ersparnis und Amortisation hängen von Verbrauch, Anlagengröße,
      Ausrichtung, Verschattung und Strompreis ab (gerechnet mit rund 30 bis 35 ct/kWh Netzbezug). Finanzierungsrate:
      Beispielkonditionen, abhängig von Anlagengröße und Laufzeit. Fördersätze laut EAG-Abwicklungsstelle und Land
      Kärnten, Programme sind budgetiert und ändern sich. Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    build()
