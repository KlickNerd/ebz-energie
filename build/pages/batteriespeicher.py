"""Leistungsseite Batteriespeicher (/batteriespeicher/).

Quellen: Live-Seite /batteriespeicher/ sowie die beiden alten Beitraege
/photovoltaik-mit-speicher/ und /batteriespeicher-und-photovoltaik/ (gehen per 301
in diese Seite auf). Roter Faden: Hook -> Definition -> fuer wen (Neuanlage oder
Nachruestung) -> Nutzen/Zahlen -> Speichergroesse -> Technik -> Kosten (Preis je kWh)
-> Foerderung + Finanzierung -> Sicherheit/Aufstellort/EMS -> Mario -> warum EBZ
-> Referenzen -> Ablauf -> FAQ -> Cluster-Links -> Kontakt.

SEO/GEO-Briefing build/seo/batteriespeicher.json (Stand 2026-10-09): Primaer
"batteriespeicher" (4.400), "pv speicher" als Synonym; Preis pro kWh, Faustformel,
Marken (BYD, Fronius, Huawei nur als Beispiele), Entladetiefe/Wirkungsgrad,
Brandschutz/Aufstellort. Foerderzahlen aus build/seo/_fakten_2026-10.md (nur Betraege;
Fristen und Call-Termine stehen ausschliesslich im Hub /foerderungen/).
Bereinigt gegenueber der Quelle: Gedankenstriche, "Kaernten, Salzburg und der
Steiermark" (Montage nur Kaernten + Steiermark), "ueber 100 Anlagen pro Jahr" (300+
Projekte), "Stromkosten fast auf Null" / "100 % Eigenverbrauch" (bis zu 85 %),
"nicht brennbar" (LFP gilt als besonders sicher), "verlustfrei" (Wirkungsgrad ueber
95 %), Kosten 15.000 bis 25.000 (Richtpreis 15.000 bis 22.000).
"""

from common import IMG, NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

PATH = "/batteriespeicher/"
TITLE = "Batteriespeicher für PV: Größe, Kosten, Förderung | EBZ"
DESC = ("PV-Speicher vom Fachbetrieb in Kärnten und der Steiermark: Eigenverbrauch von 30 auf bis zu 80 %, Notstrom, "
        "Nachrüstung, 150 € je kWh Förderung, Preis pro kWh.")

FAQ = [
    ("Wie groß sollte mein Batteriespeicher sein, und was passiert, wenn er zu groß ist?",
     "Faustformel 1 kWh je kWp Modulleistung oder 1 bis 1,5 kWh je 1.000 kWh Jahresverbrauch: 4.500 kWh mit 5 kWp "
     "brauchen 4 bis 5 kWh, 10 kWp mit Wärmepumpe oder E-Auto eher 10 kWh. Ein zu großer Speicher wird im "
     "Winterbetrieb nie voll und verlängert die Amortisation; für die Bundesförderung reichen 0,5 kWh je kWp."),
    ("Wie hoch sind die Kosten pro kWh für einen Batteriespeicher?",
     "800 bis 1.200 € je kWh inklusive Installation (Richtwert Österreich, Stand Oktober 2026)*: 5 kWh kosten 4.000 "
     "bis 6.000 €, 10 kWh 8.000 bis 12.000 €. Nach dem EAG-Zuschuss von 150 € je kWh bleiben 650 bis 1.050 € je kWh. "
     "Eine komplette 10-kWp-Anlage mit Speicher liegt bei 15.000 bis 22.000 € vor Förderung."),
    ("Werden Batteriespeicher 2026 billiger?",
     "Die Preise je kWh sind in den vergangenen Jahren gesunken, 2026 liegt der Richtwert bei 800 bis 1.200 €*. "
     "Warten lohnt selten: Jede nicht gespeicherte kWh kostet rund 32 Cent, und die laufenden Förderungen (EAG-Zuschuss "
     "des Bundes, Kärntner Pauschale) sind budgetiert und befristet. Die Systemförderung ab 2027 ist geplant, die "
     "Höhe offen. Welche Fristen gerade laufen, steht tagesaktuell auf unserer Förderseite."),
    ("Kann ich einen Speicher bei meiner bestehenden PV-Anlage nachrüsten?",
     "Ja, fast immer. Am flexibelsten ist die AC-Kopplung mit eigenem Batteriewechselrichter, der vorhandene "
     "PV-Wechselrichter bleibt. Alternativ tauschen wir ihn gegen einen Hybridwechselrichter (DC-Kopplung), sinnvoll "
     "bei älteren Anlagen oder Notstromwunsch. Kärnten fördert die Nachrüstung ab 5 kWh 2026 mit 1.000 €."),
    ("Funktioniert der Speicher bei einem Stromausfall?",
     "Nur, wenn das System notstromfähig geplant ist: Eine normale PV-Anlage schaltet bei Netzausfall ab. Es braucht "
     "einen notstromfähigen Hybridwechselrichter, einen freigegebenen Speicher und eine Umschalteinrichtung, die das "
     "Haus vom Netz trennt. Ein 10-kWh-Speicher deckt 500 Watt Dauerlast rund 20 Stunden."),
    ("Was passiert mit dem Strom, wenn der Speicher voll ist?",
     "Der Überschuss fließt ins Netz und wird vergütet, im OeMAG-Marktpreismodell mit 10,168 Cent je kWh (September "
     "2026). Besser: Ein Energiemanagement lenkt ihn in Wärmepumpe, Warmwasser oder Wallbox, oder Sie teilen ihn in "
     "einer Energiegemeinschaft. Der Speicher nimmt keinen Schaden, das Batteriemanagement beendet die Ladung."),
    ("Wie hoch ist die Förderung für einen Batteriespeicher 2026?",
     "Bund: 150 € je kWh (maximal 50 kWh), nur mit neuer oder erweiterter PV-Anlage. Kärnten: 3.000 € Pauschale für "
     "Neuanlagen ab 5 kWp mit Speicher ab 5 kWh, 1.000 € für die Nachrüstung (Stand Oktober 2026). Für 10 kWp mit "
     "10 kWh sind in Kärnten 6.000 € erreichbar. Welche Fristen gerade laufen, steht tagesaktuell auf unserer Förderseite."),
    ("Wo wird der Speicher aufgestellt und wie steht es um den Brandschutz?",
     "Im Keller, in der Garage oder im Technikraum: frostfrei, trocken, nicht im Fluchtweg oder Schlafzimmer, nahe am "
     "Zählerkasten. LFP-Zellen ohne Kobalt gelten als besonders sicher, das Batteriemanagement trennt bei Fehlern ab, "
     "ein Rauchmelder im Raum ist Standard. Die Montage dokumentieren wir im Projektbericht."),
    ("Welche Marken verbaut EBZ (BYD, Fronius, Huawei)?",
     "Wir planen herstellerunabhängig: je nach Anlage zum Beispiel Hochvolt-Speicher von BYD oder Huawei mit "
     "Hybridwechselrichtern von Fronius oder Huawei, bei Nachrüstungen auch AC-gekoppelte Systeme. Entscheidend sind "
     "Garantie 10 Jahre auf 80 % Restkapazität, Notstromfähigkeit und modulare Erweiterbarkeit."),
    ("Wie lange hält ein Stromspeicher?",
     "LFP-Speicher sind für 6.000 bis 10.000 Ladezyklen ausgelegt, bei einem Zyklus pro Tag also 15 bis 20 Jahre. "
     "Die Hersteller geben üblicherweise 10 Jahre Garantie darauf, dass die Kapazität nicht unter 80 % fällt."),
]


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        # 1. Hook
        C.hero(
            eyebrow="Batteriespeicher und PV-Speicher für Kärnten und die Steiermark",
            h1="Batteriespeicher für Ihre PV-Anlage: Sonnenstrom auch am Abend und in der Nacht",
            lead=("Ein Batteriespeicher hebt den Eigenverbrauch Ihrer Photovoltaikanlage von rund 30 auf 60 bis 80 %*. "
                  "Richtwert: 800 bis 1.200 € je kWh inklusive Installation, der Bund fördert 150 € je kWh. Wir planen, "
                  "montieren und betreuen Ihr Speichersystem mit zertifizierten Fachkräften aus Villach, Notstrom und "
                  "Nachrüstung inklusive."),
            badges=[("bis zu 80 %", "Eigenverbrauch"),
                    ("Notstrom", "auf Wunsch"),
                    ("Nachrüstung", "für Bestandsanlagen")],
            img=IMG["gen_detail"],
            img_alt="Fachkraft montiert Photovoltaikmodule auf einem Dach in Kärnten, Grundlage für die Anlage mit Batteriespeicher",
            float_num=rating,
            float_label=f"aus {count} Google Bewertungen" if count else "auf Google",
            cta_secondary=("#kosten", "Was kostet ein Speicher?"),
        ),
        # Quick Trust
        C.kpis([
            ("bis zu 80 %", "Eigenverbrauch mit Speicher"),
            ("800 bis 1.200 €", "Preis pro kWh inkl. Installation*"),
            ("150 € je kWh", "EAG-Speicherförderung 2026"),
            (NAP["rating"], "Sterne auf Google"),
        ]),
        # Kurze Definition (GEO)
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Was ist ein Batteriespeicher?",
            paragraphs=[
                ("Ein Batteriespeicher ist eine wiederaufladbare Batterie auf Basis von Lithium-Eisenphosphat (LFP), "
                 "die den Solarstrom Ihrer Photovoltaikanlage zwischenspeichert: Mittags lädt er den Überschuss, am "
                 "Abend und in der Nacht gibt er ihn ab, bevor Strom aus dem Netz bezogen wird. Typische Heimspeicher "
                 "haben 5 bis 15 kWh nutzbare Kapazität (EBZ Energie, Stand Oktober 2026)."),
                ("Ob Sie Stromspeicher, Solarspeicher, PV Speicher oder Photovoltaik Speicher sagen: gemeint ist "
                 "dieselbe Technik. Gesteuert wird sie vom Hybridwechselrichter, der PV-Wechselrichter und "
                 "Batteriemanagement in einem Gerät vereint; bei der Nachrüstung übernimmt das ein eigener "
                 "Batteriewechselrichter."),
            ],
        ),
        # 2. Fuer wen: Neuanlage oder Nachruestung
        C.audience_split(
            eyebrow="Für wen planen wir?",
            h2="Neue Anlage mit Speicher oder Speicher nachrüsten: beides geht",
            intro=("Wer bei bestehender Photovoltaik Speicher nachrüsten möchte, braucht andere Technik als beim Neubau. "
                   "Das Ziel ist dasselbe: mehr eigener Strom, weniger Netzbezug."),
            left={
                "img": IMG["gen_eigenheim"],
                "alt": "Einfamilienhaus mit neuer Photovoltaikanlage und Batteriespeicher in Kärnten",
                "title": "Sie planen eine neue Photovoltaikanlage",
                "bullets": [
                    "DC-gekoppeltes System mit Hybridwechselrichter: höchster Wirkungsgrad",
                    "Speicher und Notstrom von Anfang an mitgeplant",
                    "EAG-Zuschuss 150 € je kWh plus Land Kärnten 3.000 €, 10 kWp mit Speicher rund 15.000 bis 22.000 €*",
                ],
                "cta": ("kontakt", "Beratung für die neue Anlage"),
            },
            right={
                "img": IMG["gen_detail"],
                "alt": "Montagearbeiten an einer bestehenden Photovoltaikanlage auf dem Dach, Vorbereitung für die Speicher-Nachrüstung",
                "title": "Sie haben bereits eine Solaranlage",
                "bullets": [
                    "AC-gekoppelt: Ihr Wechselrichter bleibt, der Speicher kommt mit eigenem Batteriewechselrichter dazu",
                    "Richtwert 800 bis 1.200 € je kWh inklusive Installation*",
                    "Kärnten fördert die Nachrüstung ab 5 kWh mit 1.000 € (Stand Oktober 2026)",
                ],
                "cta": ("/pv-speicher-nachruesten/", "PV-Speicher nachrüsten: Ablauf und Kosten"),
            },
        ),
        # 3. Das Problem und die Zahl dahinter (GEO-Passage)
        C.problem_compare(
            eyebrow="Das Problem jeder PV-Anlage ohne Speicher",
            h2="Von 30 auf bis zu 80 % Eigenverbrauch: was der Speicher ändert",
            intro=("Ein Batteriespeicher hebt den Eigenverbrauch einer PV-Anlage von rund 30 auf 60 bis 80 %*. Bei "
                   "Netzstrompreisen von rund 30 bis 35 Cent je kWh und einer Einspeisevergütung von 10,168 Cent "
                   "(OeMAG-Marktpreis September 2026) lohnt sich ein Speicher ab etwa 5 kWp PV-Leistung und 3.500 kWh "
                   "Jahresverbrauch (Stand Oktober 2026). *Richtwerte, abhängig vom Lastprofil."),
            bars=[
                ("Eigenverbrauch ohne Speicher", 30, "bad", "rund 30 %*"),
                ("Eigenverbrauch mit passendem Speicher", 80, "good", "bis zu 80 %*"),
            ],
            aside=("Was der Speicher für Sie ändert", [
                ("▮", "Strom am Abend", "Kochen, Waschen, Fernsehen mit eigenem Sonnenstrom; bei 10 kWp rund 70 % Autarkie.*"),
                ("€", "Bis zu 85 % weniger Stromkosten", "Jede gespeicherte kWh ersetzt eine teuer gekaufte."),
                ("✓", "Notstrom bei Blackout", "Notstromfähige Systeme versorgen Kühlschrank, Heizung und Router weiter."),
                ("⚙", "Ein System für alles", "Der Hybridwechselrichter steuert auch Wallbox und Wärmepumpe mit."),
            ]),
        ),
        # 4. Speichergroesse (Faustformel)
        C.cards_section(
            eyebrow="Speichergröße je Jahresverbrauch und Anlage",
            h2="Welche Speichergröße passt? Faustformel und drei Haushalte",
            intro=("Faustformel 1 kWh je kWp Modulleistung oder 1 bis 1,5 kWh je 1.000 kWh Jahresverbrauch (EBZ Energie, "
                   "Stand Oktober 2026). Ein zu kleiner Speicher ist abends früh leer, ein zu großer wird im Winterbetrieb "
                   "nie voll; die Auslegung machen wir anhand Ihres Lastprofils.*"),
            cards=[
                {"ic": "⌂", "title": "Kleiner Haushalt: 3.000 bis 4.500 kWh",
                 "text": "Empfohlen: 4 bis 7 kWp PV-Leistung und 4 bis 8 kWh Speicher. Deckt den Nachtbedarf im Sommer und in der Übergangszeit."},
                {"ic": "☀", "title": "Familie: 6.000 kWh",
                 "text": "Empfohlen: 8 bis 10 kWp und 8 bis 10 kWh Speicher. Die typische Kombination für das Einfamilienhaus, auf Wunsch mit Notstrom.",
                 "link_key": "/ab-wann-lohnt-sich-photovoltaik-mit-speicher/", "link_text": "Ab wann lohnt sich PV mit Speicher?"},
                {"ic": "♨", "title": "Mit Wärmepumpe oder E-Auto: 8.000 kWh und mehr",
                 "text": "Empfohlen: 10 kWp und mehr, 10 bis 15 kWh Speicher. Hier lohnt ein Energiemanagement, das Speicher, Wallbox und Wärmepumpe steuert.",
                 "link_key": "ems", "link_text": "Energiemanagement für Speicher und Wärmepumpe"},
            ],
        ),
        # 5. Technik und Notstrom (Bild: Speicher, Hochformat)
        C.media_text(
            eyebrow="Technik, die 20 Jahre hält",
            h2="Technik: LFP, Hybridwechselrichter, Entladetiefe, Zyklen, Garantie",
            paragraphs=[
                ("Wir setzen auf Lithium-Eisenphosphat (LFP): Wirkungsgrad über 95 %, 6.000 bis 10.000 Ladezyklen, "
                 "Herstellergarantie 10 Jahre auf mindestens 80 % Restkapazität. Die Entladetiefe aktueller Systeme "
                 "liegt bei 90 bis 100 % der Nennkapazität, ein Batteriemanagementsystem überwacht jede Zelle und "
                 "schützt vor Überladung und Tiefentladung (Stand Oktober 2026)."),
                ("Hochvolt-Speicher von Herstellern wie BYD oder Huawei arbeiten mit Hybridwechselrichtern zum "
                 "Beispiel von Fronius oder Huawei, Niedervolt-Systeme eignen sich für kleinere Nachrüstungen. Wir "
                 "wählen herstellerunabhängig nach Anlage. Notstrom ist Planungssache: Mit notstromfähigem "
                 "Hybridwechselrichter, freigegebenem Speicher und Umschalteinrichtung läuft Ihr Haus im Inselbetrieb "
                 "weiter, bei Ersatzstrom lädt die Anlage den Speicher bei Sonne sogar nach."),
            ],
            img=IMG["speicher"],
            alt="Batteriespeicher einer Photovoltaikanlage an der Wand eines Technikraums",
            bullets=[
                "Modular erweiterbar: heute 5 kWh, morgen 10 kWh, wenn E-Auto oder Wärmepumpe dazukommen",
                "Notstrom oder Ersatzstrom: 10 kWh decken 500 Watt Dauerlast rund 20 Stunden",
                "Lebensdauer 15 Jahre und mehr bei einem Ladezyklus pro Tag",
            ],
            reverse=True,
            cta=("/notstrom/", "Notstrom mit Batteriespeicher"),
        ),
        # 6. Geld-Fragen: Kosten (Preis pro kWh)
        C.price_cards(
            eyebrow="Batteriespeicher Kosten: Preis pro kWh",
            h2="Was kostet ein Batteriespeicher?",
            intro=("Ein Batteriespeicher kostet in Österreich rund 800 bis 1.200 € je kWh inklusive Installation*, die "
                   "häufige Suchanfrage „Stromspeicher 10 kWh Preis“ beantwortet sich also mit 8.000 bis 12.000 € vor "
                   "Förderung (Richtwert EBZ Energie, Stand Oktober 2026). Preisentwicklung 2026: gesunken, aber jede nicht "
                   "gespeicherte kWh kostet weiter rund 32 Cent."),
            items=[
                {"size": "Nachrüstung klein", "price": "4.000 bis 6.000 €", "price_sub": "5 kWh, AC-gekoppelt*",
                 "features": ["Passend für 3.500 bis 5.000 kWh Jahresverbrauch", "Inklusive Batteriewechselrichter und Installation",
                              "Kärnten: 1.000 € Landespauschale für die Nachrüstung"]},
                {"size": "Nachrüstung groß", "price": "8.000 bis 12.000 €", "price_sub": "10 kWh, AC-gekoppelt*",
                 "features": ["Passend für 7.000 bis 10.000 kWh Jahresverbrauch", "Optional Tausch auf Hybridwechselrichter für Notstrom",
                              "Amortisation des Speichers allein 8 bis 12 Jahre*"]},
                {"size": "Neue Komplettanlage", "price": "15.000 bis 22.000 €", "price_sub": "10 kWp mit Speicher*",
                 "features": ["Module, Hybridwechselrichter, Speicher, Montage und Anmeldung", "Förderung 2026 in Kärnten bis 6.000 € (Bund und Land)",
                              "Typische Amortisation 4 bis 6 Jahre", a("photovoltaik", "Zur Photovoltaikanlage komplett →")]},
            ],
            note=("*Richtwerte für Österreich inklusive Installation, vor Förderung. Ihren genauen Preis erhalten Sie im "
                  "Projektbericht mit 3D-Belegplan und Statikreport."),
        ).replace('<section class="section"', '<section id="kosten" class="section"', 1),
        # 7. Foerderung + Finanzierung (Betraege Stand Oktober 2026, keine Fristen: die stehen im Hub)
        C.media_text(
            eyebrow="Stromspeicher Förderung Österreich 2026",
            h2="Förderung für Ihren Speicher: 150 € je kWh vom Bund, Land Kärnten bis 3.000 €",
            paragraphs=[
                ("Der EAG-Investitionszuschuss fördert Speicher mit 150 € je kWh (mindestens 0,5 kWh je kWp, "
                 "maximal 50 kWh), nur gemeinsam mit einer neuen oder erweiterten PV-Anlage und nur bei Antrag vor der "
                 "Inbetriebnahme (Quelle: EAG-Abwicklungsstelle, Stand Oktober 2026)."),
                ("Das Land Kärnten zahlt pauschal 3.000 € für neue PV-Anlagen ab 5 kWp mit Speicher ab 5 kWh und "
                 "1.000 € für die Speicher-Nachrüstung ab 5 kWh, maximal 50 % der Kosten, ohne Anrechnung der "
                 "Bundesförderung (Quelle: Land Kärnten). Die Steiermark hat keine eigene Speicherprämie. Ab 2027 plant "
                 "der Bund laut BMWET eine Systemförderung für Speicher mit intelligenter Steuerung, Höhe offen. "
                 "Welche Fristen gerade laufen, steht tagesaktuell auf unserer Förderseite; wir prüfen sie für Ihr Projekt "
                 "und stellen die Anträge."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Speicherförderung bei EBZ Energie",
            bullets=[
                "Beispiel Kärnten: 10 kWp mit 10 kWh, 3.000 € Bund (150 € je kWp und je kWh) plus 3.000 € Land = 6.000 €",
                "EAG-Speicherförderung 150 €/kWh plus Made-in-Europe-Bonus 10 % je Komponente von der White List",
                a("/foerderung-pv-speicher-kaernten/", "Speicherförderung Land Kärnten") + " und " + a("/foerderung-fuer-pv-speicher/", "Speicherförderung 2026 im Detail"),
            ],
            cta=("foerderungen", "Aktuelle Förderungen 2026"),
        ),
        C.finance_band(),
        # 8. Sicherheit, Aufstellort, EMS
        C.cards_section(
            eyebrow="Sicherheit, Aufstellort, Steuerung",
            h2="Sicherheit und Aufstellort: Keller, Garage oder Technikraum",
            intro=("LFP-Speicher gelten als besonders sicher, weil ihre Zellchemie thermisch stabil ist. Der Brandschutz "
                   "hängt trotzdem vom Aufstellort (Keller, Garage, Technikraum) ab: frostfrei, trocken, außerhalb von "
                   "Fluchtwegen, montiert nach Herstellervorgabe (EBZ Energie, Stand Oktober 2026)."),
            cards=[
                {"ic": "⌂", "title": "Aufstellort",
                 "text": "Keller, Garage oder Technikraum, frostfrei und trocken, Temperatur im vom Hersteller freigegebenen Bereich, Wandmontage oder Standgerät, kurzer Weg zum Zählerkasten."},
                {"ic": "✓", "title": "Brandschutz",
                 "text": "LFP ohne Kobalt, das Batteriemanagement trennt bei Fehlern ab, Rauchmelder im Raum, kein Aufstellort im Fluchtweg oder Schlafzimmer. Die Installation dokumentieren wir im Projektbericht."},
                {"ic": "⚙", "title": "Energiemanagement (EMS) und dynamischer Stromtarif",
                 "text": "Mit EMS lädt der Speicher aus PV-Überschuss oder per Netzladen, wenn der Börsenstrom günstig ist, und entlädt in teuren Stunden; Wallbox und Wärmepumpe steuert es mit.",
                 "link_key": "/dynamischer-stromtarif/", "link_text": "Speicher mit dynamischem Stromtarif laden"},
            ],
        ),
        # Menschlicher Anker
        C.founder_story(
            eyebrow="Ein Wort von Mario Zintl",
            h2="Warum ich bei der Speichergröße nicht verhandle",
            paragraphs=[
                ("Der Markt ist voll von Speichern, die online in zwei Minuten bestellt sind. Was fehlt, ist die Frage, "
                 "ob die Größe zu Ihrem Haus passt. Ich habe zu viele 15-kWh-Speicher an 3.500-kWh-Haushalten gesehen, "
                 "die im November halb leer bleiben."),
                ("Deshalb schauen wir uns Jahresverbrauch, Lastprofil und Ihre Pläne für E-Auto oder Wärmepumpe an, "
                 "bevor wir Kapazität, Kopplung und Notstrom festlegen. Wenn ein kleinerer Speicher die bessere Wahl "
                 "ist, sage ich Ihnen das auch."),
            ],
            quote="Ein Speicher muss zu Ihrem Verbrauch passen, nicht zu einem Katalog.",
            name=AUTHOR, role=AUTHOR_ROLE,
            badge="Villach, Kärnten",
        ),
        # 9. Warum EBZ
        C.why_section(
            eyebrow="Warum EBZ Energie",
            h2="Ihr Speicher-Partner in Kärnten und der Steiermark",
            items=[
                ("☀", "Ein System aus einer Hand", "PV, Speicher, Wechselrichter, Wallbox und Wärmepumpe aufeinander abgestimmt, ein Ansprechpartner."),
                ("✓", "Zertifizierte Fachkräfte", "Meisterhaftes Handwerk, sauber abgestimmte Komponenten."),
                ("★", "4,9 Sterne auf Google", "Bewertungen von echten Kundinnen und Kunden aus der Region."),
                ("◉", "300+ Projekte", "Über 300 dokumentierte Anlagen in 6 Bundesländern, viele mit Speicher und Notstrom."),
                ("€", "Förderung und Finanzierung inklusive", "Wir stellen die Anträge bei Bund und Land und bieten Finanzierung ab 147 € im Monat.*"),
                ("⌂", "Auch in 10 Jahren erreichbar", "Regionaler Fachbetrieb in Villach: Service, Monitoring und Erweiterung aus der Nähe."),
            ],
        ),
        # 10. Beweis
        C.reference_cards(
            eyebrow="Aus der Praxis",
            h2="Referenzen mit Zahlen: Speicher und Notstrom",
            intro=("Drei Projekte mit Batteriespeicher aus Eigenheim, Mehrparteienhaus und Gewerbe. Bild und Zahlen "
                   "gehören jeweils zum selben Projekt."),
            items=[
                {"img": IMG["ref_krumpendorf"], "alt": "Photovoltaikanlage mit 25 kWh Speicher auf einem Mehrparteienhaus in Krumpendorf",
                 "title": "Mehrparteienhaus, Krumpendorf", "specs": "25 kWp mit 25 kWh Speicher und Notstrom, Versorgung mehrerer Wohneinheiten bei Netzausfall.",
                 "result": "4 Tage", "result_sub": "Bauzeit"},
                {"img": IMG["ref_villach"], "alt": "Photovoltaikanlage mit Speicher und Notstrom auf einem Einfamilienhaus in Villach",
                 "title": "Einfamilienhaus, Villach", "specs": "10 kWp Ost-West mit Speicher und Notstromfunktion, rund 11.000 kWh im Jahr.",
                 "result": "rund 80 %", "result_sub": "weniger Stromkosten"},
                {"img": IMG["gewerbe_dach"], "alt": "Photovoltaikanlage mit 40 kWh Speicher auf einem Gewerbedach in Oberösterreich",
                 "title": "Gewerbe, Oberösterreich", "specs": "40 kWp Ost-West auf Trapezblech, 40 kWh Speicher, rund 40.000 kWh im Jahr.",
                 "result": "13.500 €", "result_sub": "Ersparnis pro Jahr"},
            ],
        ),
        C.reviews_slider(reviews, rating=rating, count=count),
        # 11. Ablauf
        C.steps_section(
            eyebrow="So läuft es ab",
            h2="Von der Verbrauchsanalyse zum eigenen Speicher",
            steps=[
                ("Beratung und Analyse", "Jahresverbrauch, Lastprofil, bestehende Anlage und Ihre Pläne für E-Auto oder Wärmepumpe. Kostenlos.", "Tag 1"),
                ("Projektbericht", "Projektbericht mit 3D-Belegplan und Statikreport, inklusive Speichergröße, Kopplung, Aufstellort und Förderübersicht.", "wenige Tage"),
                ("Förderanträge", "EAG-Antrag vor der Inbetriebnahme, Landesantrag Kärnten; die laufenden Fristen prüfen wir für Ihr Projekt.", "vor der Montage"),
                ("Montage und Inbetriebnahme", "Zertifizierte Fachkräfte montieren Speicher und Wechselrichter, bei der Nachrüstung meist in 1 bis 3 Tagen. Anmeldung und Übergabe inklusive.", "1 bis 3 Tage vor Ort"),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section(
            "Weiterlesen: Speicher, Notstrom und Förderung",
            [("/pv-speicher-nachruesten/", "PV-Speicher nachrüsten"),
             ("/notstrom/", "Notstrom mit Batteriespeicher"),
             ("/ab-wann-lohnt-sich-photovoltaik-mit-speicher/", "Ab wann lohnt sich PV mit Speicher?"),
             ("/foerderung-fuer-pv-speicher/", "Speicherförderung 2026"),
             ("/foerderung-pv-speicher-kaernten/", "Speicherförderung Land Kärnten"),
             ("foerderungen", "Alle Förderungen 2026"),
             ("/dynamischer-stromtarif/", "Speicher mit dynamischem Tarif laden"),
             ("ems", "Energiemanagement"),
             ("photovoltaik", "Photovoltaikanlage komplett"),
             ("finanzierung", "Speicher mitfinanzieren"),
             ("referenzen", "Referenzen")],
        ),
        C.contact_section(
            headline="Ihr Speicher, passend berechnet",
            sub=("Sagen Sie uns Ihren Jahresverbrauch und ob Sie eine Anlage haben oder planen. Wir zeigen Ihnen, "
                 "welche Speichergröße sich rechnet, was sie kostet und welche Förderung Sie bekommen. Kostenlos und "
                 "unverbindlich."),
            page_label="Leistungsseite Batteriespeicher",
        ),
        C.finalcta(
            "Schluss mit Sonnenstrom für ein paar Cent",
            "Fordern Sie jetzt Ihre kostenlose Speicherberatung an. Wir melden uns innerhalb eines Werktags "
            "und rechnen Ihr Haus durch.",
            trust=[(f"{NAP['rating']} auf Google", True), ("bis zu 80 % Eigenverbrauch", False),
                   ("Notstrom auf Wunsch", False), ("Förderung inklusive", False)],
        ),
        _footnote(),
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=IMG["gen_detail"])
    return write_page("batteriespeicher/index.html", html)


def _footnote():
    return ("""
  <section class="section--tight section" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte für Österreich auf Basis typischer Projekte, inklusive Installation und vor
      Förderung, Stand Oktober 2026. Eigenverbrauchsanteil, Autarkie, Ersparnis, Preis und Amortisation hängen von
      Verbrauch, Lastprofil, Anlagengröße, Strompreis (gerechnet mit rund 30 bis 35 ct/kWh Bezug und 10,168 ct/kWh
      OeMAG-Marktpreis September 2026) und Förderung ab. Finanzierungsrate: Beispielkonditionen. Fördersätze laut
      EAG-Abwicklungsstelle und Land Kärnten, Programme sind budgetiert und ändern sich. Fachlich geprüft von
      Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import theme
    theme.write_assets()
    build()
