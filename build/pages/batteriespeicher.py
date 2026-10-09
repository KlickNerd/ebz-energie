"""Leistungsseite Batteriespeicher (/batteriespeicher/).

Quellen: Live-Seite /batteriespeicher/ sowie die beiden alten Beitraege
/photovoltaik-mit-speicher/ und /batteriespeicher-und-photovoltaik/ (gehen per 301
in diese Seite auf). Roter Faden: Hook -> Problem (Eigenverbrauch 30 %) -> fuer wen
(Neuanlage oder Nachruestung) -> Nutzen/Zahlen -> Speichergroesse -> Kosten ->
Foerderung + Finanzierung -> Notstrom/Technik -> warum EBZ -> Referenzen -> Ablauf
-> FAQ -> Cluster-Links -> Kontakt.

Bereinigt gegenueber der Quelle: Gedankenstriche, "Kaernten, Salzburg und der
Steiermark" (Montage nur Kaernten + Steiermark), "ueber 100 Anlagen pro Jahr" (300+
Projekte), "Stromkosten fast auf Null" / "100 % Eigenverbrauch" (bis zu 85 %),
"nicht brennbar" (LFP gilt als besonders sicher), "verlustfrei" (Wirkungsgrad ueber
95 %), Kosten 15.000 bis 25.000 (Richtpreis 15.000 bis 22.000), Carport-Absatz im
Fazit des alten Beitrags (Copy-Paste-Rest) verworfen.
"""

from common import IMG, NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

PATH = "/batteriespeicher/"
TITLE = "Batteriespeicher: bis 80 % Eigenverbrauch, Notstrom | EBZ"
DESC = ("Batteriespeicher in Kärnten und der Steiermark: Eigenverbrauch von 30 auf bis zu 80 %, Notstrom, "
        "Nachrüstung, Förderung 150 € je kWh. Fachbetrieb, 4,9 Sterne.")

FAQ = [
    ("Wie groß sollte mein Batteriespeicher sein?",
     "Als Faustregel gilt rund 1 kWh Speicherkapazität je kWp Modulleistung beziehungsweise je 1.000 kWh "
     "Jahresstromverbrauch. Ein Haushalt mit 4.500 kWh und einer 5-kWp-Anlage ist mit 4 bis 5 kWh gut "
     "versorgt, bei 10 kWp und Wärmepumpe oder E-Auto sind eher 10 kWh sinnvoll. Für die Bundesförderung "
     "muss der Speicher mindestens 0,5 kWh je kWp haben. Wir legen die Größe anhand Ihres Verbrauchs aus."),
    ("Wie lange hält ein Stromspeicher?",
     "Moderne Lithium-Eisenphosphat-Speicher (LFP) sind für 6.000 bis 10.000 Ladezyklen ausgelegt. Bei "
     "einem Zyklus pro Tag entspricht das 15 bis 20 Jahren Betrieb. Die Hersteller geben üblicherweise 10 "
     "Jahre Garantie und sichern zu, dass die Kapazität in dieser Zeit nicht unter 80 % fällt."),
    ("Was kostet ein Batteriespeicher?",
     "Als Richtwert gelten in Österreich 800 bis 1.200 € je Kilowattstunde Speicherkapazität inklusive "
     "Installation. Ein 10-kWh-Speicher liegt damit bei rund 8.000 bis 12.000 € vor Förderung. Eine "
     "komplette 10-kWp-Anlage mit Speicher kostet bei EBZ Energie rund 15.000 bis 22.000 € vor Förderung."),
    ("Kann ich einen Speicher bei meiner bestehenden PV-Anlage nachrüsten?",
     "Ja, fast immer. Am flexibelsten ist die AC-Kopplung: Der Speicher bekommt einen eigenen "
     "Batteriewechselrichter und arbeitet unabhängig vom vorhandenen PV-Wechselrichter. Alternativ tauschen "
     "wir den alten Wechselrichter gegen einen Hybridwechselrichter (DC-Kopplung), was sich bei älteren "
     "Anlagen oder bei Notstromwunsch oft anbietet."),
    ("Funktioniert der Speicher bei einem Stromausfall?",
     "Nur, wenn das System notstromfähig geplant ist. Eine normale PV-Anlage schaltet bei Netzausfall aus "
     "Sicherheitsgründen ab. Für Notstrom braucht es einen notstromfähigen Hybridwechselrichter, einen dafür "
     "freigegebenen Speicher und eine Umschalteinrichtung, die das Haus vom Netz trennt. Ein 10-kWh-Speicher "
     "deckt 500 Watt Dauerlast rund 20 Stunden."),
    ("Wie hoch ist die Förderung für einen Batteriespeicher 2026?",
     "Der Bund fördert Speicher mit 150 € je kWh (maximal 50 kWh), allerdings nur gemeinsam mit einer "
     "neuen oder erweiterten PV-Anlage. Kärnten zahlt 2026 zusätzlich 3.000 € Pauschale für neue PV-Anlagen "
     "ab 5 kWp mit Speicher ab 5 kWh und 1.000 € für die Speicher-Nachrüstung an Bestandsanlagen. Für "
     "10 kWp mit 10 kWh sind in Kärnten in Summe 6.000 € erreichbar."),
    ("Was passiert mit dem Speicher im Winter?",
     "Im Winter produziert die PV-Anlage weniger, der Speicher wird nicht jeden Tag voll. Das regelt das "
     "System automatisch: Jede überschüssige Kilowattstunde wird gespeichert und deckt die teuren "
     "Verbrauchsspitzen am Abend ab, bevor Strom aus dem Netz bezogen wird. Deshalb planen wir die Kapazität "
     "nicht zu groß, ein überdimensionierter Speicher ist unwirtschaftlich."),
    ("Was ist der Unterschied zwischen kWp, kW und kWh?",
     "kWp (Kilowatt-Peak) ist die Spitzenleistung Ihrer Solaranlage. kW (Kilowatt) ist die Leistung, die "
     "gerade erzeugt oder verbraucht wird, ein Herd hat zum Beispiel 2 kW. kWh (Kilowattstunde) ist die "
     "Energiemenge: wie viel in Ihren Speicher passt oder wie viel Strom Sie im Jahr verbrauchen."),
]


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        # 1. Hook
        C.hero(
            eyebrow="Batteriespeicher für Photovoltaik in Kärnten und der Steiermark",
            h1="Batteriespeicher: Ihr Sonnenstrom, auch wenn die Sonne weg ist",
            lead=("Ohne Speicher nutzen Sie nur rund 30 % Ihres eigenen Solarstroms, der Rest geht für wenige "
                  "Cent ins Netz. Mit einem passend geplanten Batteriespeicher heben Sie den Eigenverbrauch auf "
                  "bis zu 80 %, haben Strom am Abend und auf Wunsch auch bei Stromausfall. Wir planen, montieren "
                  "und betreuen Ihr Speichersystem mit zertifizierten Fachkräften aus Villach."),
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
            ("15 bis 20 Jahre", "Lebensdauer moderner LFP-Speicher"),
            ("150 € je kWh", "Bundesförderung 2026 mit neuer PV-Anlage"),
            (NAP["rating"], "Sterne auf Google"),
        ]),
        # Kurze Definition (GEO)
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Was ist ein Batteriespeicher?",
            paragraphs=[
                ("Ein Batteriespeicher (auch Stromspeicher oder Solarspeicher) ist eine wiederaufladbare Batterie, "
                 "die den Solarstrom Ihrer Photovoltaikanlage zwischenspeichert. Mittags, wenn die Anlage mehr "
                 "produziert als das Haus verbraucht, lädt er auf. Am Abend und in der Nacht gibt er den Strom "
                 "wieder ab, bevor etwas aus dem Netz bezogen wird."),
                ("Gesteuert wird das vom Hybridwechselrichter, der PV-Wechselrichter und Batteriemanager in einem "
                 "Gerät vereint. Die Kapazität wird in Kilowattstunden (kWh) angegeben, typische Heimspeicher haben "
                 "5 bis 15 kWh."),
            ],
        ),
        # 2. Fuer wen: Neuanlage oder Nachruestung
        C.audience_split(
            eyebrow="Für wen planen wir?",
            h2="Neue Anlage mit Speicher oder Speicher nachrüsten: beides geht",
            intro=("Wählen Sie, was auf Sie zutrifft. Die Technik unterscheidet sich, das Ziel ist dasselbe: mehr "
                   "eigener Strom, weniger Netzbezug."),
            left={
                "img": IMG["gen_eigenheim"],
                "alt": "Einfamilienhaus mit neuer Photovoltaikanlage und Batteriespeicher in Kärnten",
                "title": "Sie planen eine neue Photovoltaikanlage",
                "bullets": [
                    "DC-gekoppeltes System mit Hybridwechselrichter: höchster Wirkungsgrad",
                    "Speicher und Notstrom von Anfang an mitgeplant",
                    "Bundesförderung 150 € je kWh plus Landesförderung, 10 kWp mit Speicher rund 15.000 bis 22.000 €*",
                ],
                "cta": ("kontakt", "Beratung für die neue Anlage"),
            },
            right={
                "img": IMG["gen_detail"],
                "alt": "Montagearbeiten an einer bestehenden Photovoltaikanlage auf dem Dach, Vorbereitung für die Speicher-Nachrüstung",
                "title": "Sie haben bereits eine Solaranlage",
                "bullets": [
                    "AC-Kopplung: Ihr Wechselrichter bleibt, der Speicher kommt mit eigenem Batteriewechselrichter dazu",
                    "Richtwert 800 bis 1.200 € je kWh inklusive Installation*",
                    "Kärnten fördert die Nachrüstung ab 5 kWh mit 1.000 € Pauschale",
                ],
                "cta": ("/pv-speicher-nachruesten/", "Ratgeber: Speicher nachrüsten"),
            },
        ),
        # 3. Das Problem und die Zahl dahinter
        C.problem_compare(
            eyebrow="Das Problem jeder Photovoltaikanlage ohne Speicher",
            h2="Von 30 auf bis zu 80 % Eigenverbrauch",
            intro=("Eine PV-Anlage produziert den meisten Strom zur Mittagszeit, wenn oft niemand zu Hause ist. "
                   "Der Überschuss fließt für 5 bis 10 Cent ins Netz, am Abend kaufen Sie denselben Strom für rund "
                   "32 Cent zurück. Ein Speicher verschiebt den Mittagsstrom in den Abend.*"),
            bars=[
                ("Eigenverbrauch ohne Speicher", 30, "bad", "rund 30 %*"),
                ("Eigenverbrauch mit passendem Speicher", 80, "good", "bis zu 80 %*"),
            ],
            aside=("Was der Speicher für Sie ändert", [
                ("▮", "Strom am Abend", "Kochen, Waschen, Fernsehen mit eigenem Sonnenstrom statt Netzbezug."),
                ("€", "Bis zu 85 % weniger Stromkosten", "Jede gespeicherte kWh ersetzt eine teuer gekaufte."),
                ("✓", "Notstrom bei Blackout", "Notstromfähige Systeme versorgen Kühlschrank, Heizung und Router weiter."),
                ("⚙", "Ein System für alles", "Der Hybridwechselrichter steuert auch Wallbox und Wärmepumpe mit."),
            ]),
        ),
        # 4. Speichergroesse
        C.cards_section(
            eyebrow="Die richtige Speichergröße",
            h2="Wir schätzen nicht, wir berechnen",
            intro=("Ein zu kleiner Speicher ist abends zu früh leer, ein zu großer wird im Winter nie voll und kostet "
                   "unnötig. Faustregel: rund 1 kWh Kapazität je kWp Modulleistung oder je 1.000 kWh Jahresverbrauch. "
                   "Diese Richtwerte zeigen die Richtung, die Auslegung machen wir anhand Ihres Lastprofils.*"),
            cards=[
                {"ic": "⌂", "title": "Kleiner Haushalt: 3.000 bis 4.500 kWh",
                 "text": "Empfohlen: 4 bis 7 kWp PV-Leistung und 4 bis 8 kWh Speicher. Deckt den Nachtbedarf im Sommer und in der Übergangszeit."},
                {"ic": "☀", "title": "Familie: 6.000 kWh",
                 "text": "Empfohlen: 8 bis 10 kWp und 8 bis 10 kWh Speicher. Die typische Kombination für das Einfamilienhaus, auf Wunsch mit Notstrom."},
                {"ic": "♨", "title": "Mit Wärmepumpe oder E-Auto: 8.000 kWh und mehr",
                 "text": "Empfohlen: 10 kWp und mehr, 10 bis 15 kWh Speicher. Hier lohnt auch ein Energiemanagement, das Speicher, Wallbox und Wärmepumpe steuert.",
                 "link_key": "ems", "link_text": "Zum Energiemanagement"},
            ],
        ),
        # 5. Technik und Notstrom (Bild: Speicher, Hochformat)
        C.media_text(
            eyebrow="Technik, die 20 Jahre hält",
            h2="Lithium-Eisenphosphat, Hybridwechselrichter und Notstrom",
            paragraphs=[
                ("Wir setzen auf Lithium-Eisenphosphat-Speicher (LFP). Sie gelten als besonders sicher und "
                 "langlebig, erreichen einen Wirkungsgrad von über 95 % und sind für 6.000 bis 10.000 Ladezyklen "
                 "ausgelegt. Ein Batteriemanagementsystem überwacht jede Zelle und schützt vor Überladung und "
                 "Tiefentladung. Die nutzbare Kapazität liegt bei aktuellen Systemen bei 90 bis 100 Prozent der "
                 "Nennkapazität."),
                ("Notstrom ist Planungssache, kein Zubehör: Eine normale PV-Anlage schaltet bei Stromausfall ab. "
                 "Mit notstromfähigem Hybridwechselrichter, freigegebenem Speicher und Umschalteinrichtung trennt "
                 "sich Ihr Haus vom Netz und läuft im Inselbetrieb weiter. Bei einer Ersatzstromlösung lädt die "
                 "Anlage den Speicher bei Sonne sogar nach."),
            ],
            img=IMG["speicher"],
            alt="Batteriespeicher einer Photovoltaikanlage an der Wand eines Technikraums",
            bullets=[
                "Wirkungsgrad über 95 %, 10 Jahre Herstellergarantie mit mindestens 80 % Restkapazität",
                "Notstrom oder Ersatzstrom: 10 kWh decken 500 Watt Dauerlast rund 20 Stunden",
                "Erweiterbar: heute 5 kWh, morgen 10 kWh, wenn E-Auto oder Wärmepumpe dazukommen",
            ],
            reverse=True,
            cta=("/notstrom/", "Ratgeber: Notstrom mit Photovoltaik"),
        ),
        # 6. Geld-Fragen: Kosten
        C.price_cards(
            eyebrow="Batteriespeicher Kosten",
            h2="Was kostet ein Batteriespeicher?",
            intro=("Der Preis hängt von Kapazität, Kopplung und Notstromwunsch ab. Diese Richtwerte geben Ihnen eine "
                   "erste Orientierung vor Förderung."),
            items=[
                {"size": "Nachrüstung klein", "price": "4.000 bis 6.000 €", "price_sub": "5 kWh, AC-gekoppelt*",
                 "features": ["Passend für 3.500 bis 5.000 kWh Jahresverbrauch", "Inklusive Batteriewechselrichter und Installation",
                              "Kärnten: 1.000 € Landespauschale für die Nachrüstung"]},
                {"size": "Nachrüstung groß", "price": "8.000 bis 12.000 €", "price_sub": "10 kWh, AC-gekoppelt*",
                 "features": ["Passend für 7.000 bis 10.000 kWh Jahresverbrauch", "Optional Tausch auf Hybridwechselrichter für Notstrom",
                              "Amortisation des Speichers allein 8 bis 12 Jahre*"]},
                {"size": "Neue Komplettanlage", "price": "15.000 bis 22.000 €", "price_sub": "10 kWp mit Speicher*",
                 "features": ["Module, Hybridwechselrichter, Speicher, Montage und Anmeldung", "Förderung 2026 in Kärnten bis 6.000 € (Bund und Land)",
                              "Typische Amortisation 4 bis 6 Jahre", a("kontakt", "Kostenlose Beratung anfragen →")]},
            ],
            note="*Richtwerte für Österreich inklusive Installation, vor Förderung. Ihren genauen Preis erhalten Sie im Projektbericht mit 3D-Belegplan und Statikreport.",
        ).replace('<section class="section"', '<section id="kosten" class="section"', 1),
        # 7. Foerderung + Finanzierung
        C.media_text(
            eyebrow="Förderung 2026",
            h2="150 € je kWh vom Bund, bis zu 3.000 € vom Land Kärnten",
            paragraphs=[
                ("Der EAG-Investitionszuschuss des Bundes fördert Speicher mit 150 € je Kilowattstunde (maximal 50 kWh), "
                 "allerdings nur gemeinsam mit einer neuen oder erweiterten PV-Anlage und nur bei Antrag vor der "
                 "Inbetriebnahme. Der Speicher muss mindestens 0,5 kWh je kWp haben."),
                ("Kärnten legt 2026 eine Pauschale von 3.000 € für neue PV-Anlagen ab 5 kWp mit Speicher ab 5 kWh "
                 "drauf, ohne Anrechnung der Bundesförderung, und fördert die reine Speicher-Nachrüstung mit 1.000 €. "
                 "Die Steiermark hat keine eigene Speicherprämie, dafür gilt der Bundeszuschuss. Zwei Stellen, zwei "
                 "Fristen, gegensätzliche Reihenfolge: Wir übernehmen beide Anträge und die Endabrechnung."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Speicherförderung bei EBZ Energie",
            bullets=[
                "Beispiel Kärnten: 10 kWp mit 10 kWh, 3.000 € Bund plus 3.000 € Land = 6.000 €",
                "Made-in-Europe-Bonus: bis zu 10 % mehr für Speicher von der White List",
                "Fördercalls 2026 sind zeitlich begrenzt, wir reichen für Sie rechtzeitig ein",
            ],
            cta=("/foerderung-fuer-pv-speicher/", "Ratgeber: Förderung für PV-Speicher"),
        ),
        C.finance_band(),
        # Menschlicher Anker
        C.founder_story(
            eyebrow="Ein Wort von Mario Zintl",
            h2="Warum ich bei der Speichergröße nicht verhandle",
            paragraphs=[
                ("Der Markt ist voll von Speichern, die online in zwei Minuten bestellt sind. Was fehlt, ist die "
                 "Frage, ob die Größe zu Ihrem Haus passt. Ich habe zu viele Anlagen gesehen, bei denen ein 15-kWh-Speicher "
                 "an einem 3.500-kWh-Haushalt hängt und im November halb leer bleibt. Das kostet Geld und bringt nichts."),
                ("Deshalb schauen wir uns Jahresverbrauch, Lastprofil und Ihre Pläne für E-Auto oder Wärmepumpe an, "
                 "bevor wir Kapazität, Kopplung und Notstrom festlegen. Wenn ein kleinerer Speicher die bessere Wahl "
                 "ist, sage ich Ihnen das auch."),
            ],
            quote="Ein Speicher muss zu Ihrem Verbrauch passen, nicht zu einem Katalog.",
            name=AUTHOR, role=AUTHOR_ROLE,
            badge="Villach, Kärnten",
        ),
        # 8. Warum EBZ
        C.why_section(
            eyebrow="Warum EBZ Energie",
            h2="Ihr Speicher-Partner in Kärnten und der Steiermark",
            items=[
                ("☀", "Ein System aus einer Hand", "PV, Speicher, Wechselrichter, Wallbox und Wärmepumpe aufeinander abgestimmt, ein Ansprechpartner."),
                ("✓", "Zertifizierte Fachkräfte", "Festangestelltes Team, meisterhaftes Handwerk, sauber abgestimmte Komponenten."),
                ("★", "4,9 Sterne auf Google", "Bewertungen von echten Kundinnen und Kunden aus der Region."),
                ("◉", "300+ Projekte", "Erfahrung aus über 300 dokumentierten Anlagen in 6 Bundesländern, viele mit Speicher und Notstrom."),
                ("€", "Förderung und Finanzierung inklusive", "Wir stellen die Anträge bei Bund und Land und bieten Finanzierung ab 147 € im Monat."),
                ("⌂", "Auch in 10 Jahren erreichbar", "Regionaler Fachbetrieb in Villach: Service, Monitoring und Erweiterung aus der Nähe."),
            ],
        ),
        # 9. Beweis
        C.reference_cards(
            eyebrow="Aus der Praxis",
            h2="Speicher und Notstrom, mit Zahlen belegt",
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
        # 10. Ablauf
        C.steps_section(
            eyebrow="So läuft es ab",
            h2="Von der Verbrauchsanalyse zum eigenen Speicher",
            steps=[
                ("Beratung und Analyse", "Wir prüfen Jahresverbrauch, Lastprofil, bestehende Anlage und Ihre Pläne für E-Auto oder Wärmepumpe. Kostenlos.", "Tag 1"),
                ("Projektbericht", "Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport, inklusive Speichergröße, Kopplung und Förderübersicht.", "wenige Tage"),
                ("Förderanträge", "Wir reichen den EAG-Antrag vor Inbetriebnahme ein und bereiten den Landesantrag vor.", "vor der Montage"),
                ("Montage und Inbetriebnahme", "Zertifizierte Fachkräfte montieren Speicher und Wechselrichter, bei der Nachrüstung meist in 1 bis 3 Tagen. Anmeldung und Übergabe inklusive.", "1 bis 3 Tage vor Ort"),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section(
            "Weiterlesen: Speicher, Notstrom und Förderung",
            [("/pv-speicher-nachruesten/", "PV-Speicher nachrüsten"),
             ("/notstrom/", "Notstrom mit Photovoltaik"),
             ("/ab-wann-lohnt-sich-photovoltaik-mit-speicher/", "Ab wann lohnt sich PV mit Speicher?"),
             ("/foerderung-fuer-pv-speicher/", "Förderung für PV-Speicher"),
             ("/foerderung-pv-speicher-kaernten/", "Speicherförderung Kärnten"),
             ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage"),
             ("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
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
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte für Österreich auf Basis typischer Projekte, inklusive Installation und vor
      Förderung. Eigenverbrauchsanteil, Ersparnis, Preis und Amortisation hängen von Verbrauch, Lastprofil,
      Anlagengröße, Strompreis (gerechnet mit rund 32 ct/kWh Bezug und 5 bis 10 ct/kWh Einspeisung) und Förderung ab.
      Fördersätze Stand 2026, Förderprogramme sind budgetiert und ändern sich. Fachlich geprüft von Mario Zintl,
      Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import theme
    theme.write_assets()
    build()
