"""Standortseite Photovoltaik Wolfsberg (/photovoltaik-wolfsberg/).

Kommerzieller Suchintent "photovoltaik wolfsberg" (+ "photovoltaik lavanttal"). Quelle: Live-Seite
/photovoltaik-wolfsberg/ (WP-Beitrag, rund 3.000 Woerter), stark gekuerzt.
Bereinigt: "verbindliche Ertragsprognose" (jetzt Projektbericht mit 3D-Belegplan
und Statikreport), Gedankenstriche, Superlative, "historische Chance"-Rhetorik.
Kein Wolfsberg-Bild im Repo: generische Szenen mit ehrlichen Alt-Texten.

SEO-Ueberarbeitung Oktober 2026 (build/seo/standort_wolfsberg.json): Lavanttal mit
St. Andrae, St. Paul, Bad St. Leonhard und den Wolfsberger Ortsteilen als Einzugsgebiet,
Ertragswert laut PV-Atlas (1.162 kWh je kWp Wolfsberg, Bezirksmedian 1.188), Wallbox-Abschnitt,
Eigenheim/Landwirtschaft/Betrieb. Keine erfundene Lavanttal-Referenz: Referenzen aus Kaernten
mit Link auf /referenzen/.
"""

from common import IMG, NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, S, faq_jsonld, u, a, href, tel_link, write_page, load_reviews
from layout import page
import components as C

PATH = "/photovoltaik-wolfsberg/"
TITLE = "Photovoltaik Wolfsberg & Lavanttal: PV mit Speicher | EBZ"
DESC = ("Photovoltaik in Wolfsberg, St. Andrä und im Lavanttal: Kärntner Fachbetrieb, Planung vor Ort, "
        "Speicher, Notstrom, Wallbox, Förderung. Montage in 2 bis 4 Tagen.")

MAPS_URL = "https://www.google.com/maps/search/?api=1&query=Triglavstra%C3%9Fe+15%2C+9500+Villach"

LAVANTTAL = ["Wolfsberg mit St. Stefan, St. Marein, St. Michael und Reding", "St. Andrä",
             "St. Paul im Lavanttal", "Bad St. Leonhard", "Frantschach-St. Gertraud", "Lavamünd",
             "Preitenegg", "Reichenfels"]
NACHBARN = ["Völkermarkt und Griffen", "Klagenfurt und Umgebung", "St. Veit an der Glan",
            "Deutschlandsberg (Steiermark)", "Voitsberg und Köflach (Steiermark)", "Murtal (Steiermark)"]

FAQ = [
    ("Wie viel kostet eine Photovoltaikanlage in Wolfsberg inklusive Montage?",
     "Eine Komplettanlage mit rund 10 kWp und Speicher kostet typischerweise rund 15.000 bis 22.000 Euro vor "
     "Förderung, inklusive Montage, Netzanmeldung und Inbetriebnahme (EBZ-Richtpreis, Stand Oktober 2026). Das Land "
     "Kärnten zahlt 3.000 Euro Pauschale für private PV ab 5 kWp mit Speicher, der Bund 150 Euro je kWp bis 10 kWp "
     "und 150 Euro je kWh Speicher. Der Umsatzsteuer-Nullsatz für kleine PV-Anlagen ist seit April 2025 ausgelaufen, "
     "die Richtpreise verstehen sich inklusive 20 Prozent Umsatzsteuer. Finanzierung ab 147 Euro im Monat* ist möglich."),
    ("Wie viel Strom erzeugt eine PV-Anlage im Lavanttal pro kWp?",
     "Laut PV-Atlas (pvatlas.at) liegt der Ertrag in Wolfsberg bei rund 1.162 kWh je kWp und Jahr, der Median im "
     "Bezirk Wolfsberg bei 1.188 kWh je kWp, bei 1.887 Sonnenstunden pro Jahr und einem Horizontverlust von rund "
     "6 Prozent durch Koralpe und Saualpe (Stand Oktober 2026). Eine 10-kWp-Anlage liefert damit rund 11.600 kWh im Jahr. Den Wert "
     "für Ihr Dach rechnen wir im Projektbericht mit 3D-Belegplan nach."),
    ("Ist eine Photovoltaikanlage ohne Speicher sinnvoll?",
     "Sie funktioniert, nutzt aber nur rund 30 Prozent des Sonnenstroms selbst*; der Rest geht zum OeMAG-Marktpreis "
     "ins Netz (September 2026: 10,168 Cent je kWh, der Wert schwankt monatlich). Mit Speicher steigt der "
     "Eigenverbrauch auf bis zu 80 Prozent*, und erst mit Speicher ab 5 kWh gibt es die Landespauschale Kärnten. "
     "Ohne Speicher ist eine Anlage dann sinnvoll, wenn der Verbrauch tagsüber hoch ist, etwa in Betrieben."),
    ("Wie groß sollte der Speicher für ein Einfamilienhaus sein?",
     "Als Faustregel rund 1 bis 1,5 kWh Speicher je kWp Anlagenleistung, bei einem Einfamilienhaus mit 10 kWp also "
     "etwa 10 bis 15 kWh. Zu klein puffert die Nacht nicht, zu groß kostet unnötig. Wir dimensionieren nach Ihrem Verbrauch, "
     "nach E-Auto und Wärmepumpe und nach der Förderung (Bund: mindestens 0,5 kWh je kWp, maximal 50 kWh)."),
    ("In welchen Orten im Bezirk Wolfsberg montiert EBZ Energie?",
     "Im ganzen Lavanttal: Wolfsberg mit seinen Ortsteilen St. Stefan, St. Marein, St. Michael und Reding, St. Andrä, "
     "St. Paul im Lavanttal, Bad St. Leonhard, Frantschach-St. Gertraud, Lavamünd, Preitenegg und Reichenfels. "
     "Für die Erstberatung kommen wir von Villach über die Südautobahn A2 kostenlos zu Ihnen."),
    ("Wie hoch ist die PV-Förderung in Kärnten 2026?",
     "Das Land Kärnten fördert private PV-Anlagen ab 5 kWp mit mindestens 5 kWh Speicher pauschal mit 3.000 Euro, "
     "die Speicher-Nachrüstung mit 1.000 Euro, maximal 50 Prozent der Kosten. Der EAG-Zuschuss des Bundes beträgt "
     "150 Euro je kWp bis 10 kWp und 150 Euro je kWh Speicher (Stand Oktober 2026). Beide Förderungen sind "
     "kombinierbar. Welche Fristen gerade laufen, steht tagesaktuell auf unserer Förderseite."),
    ("Brauche ich in Kärnten eine Genehmigung für die PV-Anlage?",
     "Für Anlagen auf Dach oder Fassade gilt in Kärnten in der Regel eine Mitteilungspflicht statt einer "
     "Bewilligungspflicht: Die Gemeinde wird informiert, ein Bauverfahren entfällt meist. Wir klären das für Ihr "
     "Projekt und stimmen uns bei Bedarf mit der Baubehörde Ihrer Gemeinde im Lavanttal ab."),
    ("Solaranlage Wolfsberg oder PV Anlage Wolfsberg: Was ist der Unterschied?",
     "Im Alltag meint „Solaranlage“ meist Photovoltaik, also Strom vom Dach. Fachlich steht Solaranlage auch für "
     "Solarthermie, die Warmwasser erzeugt. Wir planen Photovoltaikanlagen; Warmwasser aus PV-Überschuss lösen wir "
     "über einen Heizstab-Regler oder die Wärmepumpe, gesteuert vom Energiemanagement."),
    ("Lohnt sich eine Photovoltaikanlage in Wolfsberg auch im Winter?",
     "Ja. Module arbeiten bei kalten Temperaturen sogar effizienter als bei großer Hitze. Über das Winterhalbjahr "
     "liefern Anlagen typischerweise 25 bis 30 Prozent des Jahresertrags."),
]


def build():
    rating, count, reviews = load_reviews()
    bew = f"{count} Bewertungen" if count else "echten Bewertungen"
    body = "".join([
        C.hero(
            eyebrow="Photovoltaik Wolfsberg · Lavanttal",
            h1="Photovoltaik in Wolfsberg und im Lavanttal: Planung vor Ort, Montage in wenigen Tagen",
            lead=("Von Wolfsberg über St. Andrä und St. Paul bis Bad St. Leonhard: EBZ Energie aus Villach plant "
                  "Ihre PV-Anlage bei Ihnen vor Ort im Lavanttal, montiert mit zertifizierten Fachkräften und "
                  "übernimmt Förderung, Mitteilung an die Gemeinde und Netzanmeldung. Mit Speicher, Notstrom und "
                  "Wallbox, wenn Sie wollen."),
            badges=[("2 bis 4 Tage", "Montage vor Ort"),
                    ("1.162 kWh/kWp", "Ertrag in Wolfsberg (PV-Atlas)"),
                    ("Förderung", "Kärnten und Bund inklusive")],
            img=IMG["gen_hero"],
            img_alt="Photovoltaikanlage auf einem Einfamilienhaus in Kärnten, Symbolbild für Anlagen in Wolfsberg",
            float_num=rating,
            float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_secondary=("#standort", "Standort und Kontakt"),
        ),
        C.kpis([
            ("1.162 kWh", "Ertrag je kWp und Jahr in Wolfsberg (PV-Atlas)"),
            ("bis zu 80 %", "Eigenverbrauch mit Speicher"),
            ("3.000 €", "Landespauschale Kärnten für PV mit Speicher"),
            (NAP["rating"], f"Sterne auf Google, {bew}"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Warum jetzt ein guter Zeitpunkt für Photovoltaik in Wolfsberg ist",
            paragraphs=[
                ("Eine PV-Anlage in Wolfsberg liefert laut PV-Atlas (pvatlas.at) rund 1.162 kWh je kWp und Jahr, "
                 "der Median im Bezirk Wolfsberg liegt bei 1.188 kWh je kWp, bei 1.887 Sonnenstunden pro Jahr und "
                 "Bergen rundum (Horizontverlust 6 %, Stand Oktober 2026). Eine 10-kWp-Anlage erzeugt im "
                 "Lavanttal damit rund 11.600 kWh im Jahr."),
                ("Dazu kommen gesunkene Preise für Module und Wechselrichter, der EAG-Investitionszuschuss des Bundes, "
                 "die Landespauschale Kärnten und ausgereifte Speicher, mit denen Sie Ihren Sonnenstrom rund um die "
                 "Uhr nutzen. Für Hausbesitzer in Wolfsberg und Umgebung heißt das: kürzere Amortisation, planbare "
                 "Stromkosten und ein Haus, das bei Netzausfall weiterläuft."),
            ],
        ),
        C.text_block(
            eyebrow="Photovoltaik Lavanttal",
            h2="Wolfsberg, St. Andrä, St. Paul, Bad St. Leonhard: unser Einzugsgebiet im Lavanttal",
            paragraphs=[
                ("Der Bezirk Wolfsberg ist für uns Montagegebiet, kein Randgebiet. Für die Erstberatung kommen wir "
                 "von Villach über die Südautobahn A2 kostenlos zu Ihnen ins Lavanttal, schauen uns Dach, "
                 "Zählerschrank und Verbrauch an und planen die Anlage für Ihr Haus, Ihren Hof oder Ihren Betrieb. "
                 "Montiert wird mit denselben zertifizierten Fachkräften wie in Villach. Wer „Photovoltaik Kärnten Firmen“ "
                 "oder „PV Anlage Kärnten“ sucht, findet unseren Firmensitz in Villach; im Lavanttal sind wir "
                 "trotzdem regelmäßig auf den Dächern."),
            ],
            max_w="76ch",
        ),
        C.split_section(
            left={"title": "Bezirk Wolfsberg (Lavanttal)", "items": LAVANTTAL,
                  "note": "Photovoltaik St. Andrä, Photovoltaik St. Paul oder Photovoltaik Bad St. Leonhard: Beratung und Montage im ganzen Bezirk."},
            right={"title": "Angrenzende Regionen", "items": NACHBARN, "dark": True,
                   "note": "Über den Packsattel und die Soboth sind wir auch in der Weststeiermark im Einsatz."},
        ),
        C.problem_compare(
            eyebrow="Eigenverbrauch ist der Hebel",
            h2="Ohne Speicher rund 30 %, mit Speicher bis zu 80 % Eigenverbrauch",
            intro=("Ohne Speicher nutzen Sie typischerweise nur etwa 30 Prozent Ihres Solarstroms selbst, weil "
                   "die meiste Energie mittags entsteht, wenn der Verbrauch im Haushalt gering ist. Der Rest geht "
                   "zum OeMAG-Marktpreis ins Netz (September 2026: 10,168 Cent je kWh). Ein Speicher hebt den "
                   "Eigenverbrauch auf bis zu 80 Prozent."),
            bars=[
                ("Eigenverbrauch ohne Speicher", 30, "bad", "rund 30 %*"),
                ("Eigenverbrauch mit Speicher", 80, "good", "bis zu 80 %*"),
            ],
            aside=("So planen wir Ihren Speicher", [
                ("▮", "LFP-Technologie", "Sicher, zyklenfest und langlebig: über 15 Jahre und tausende Ladezyklen."),
                ("◇", "Richtige Größe", "Faustregel rund 1 bis 1,5 kWh je kWp. Zu klein puffert die Nacht nicht, zu groß kostet unnötig."),
                ("⚙", "Energiemanagement", "E-Auto und Wärmepumpe laufen bevorzugt mit Sonnenstrom."),
                ("✓", "Notstrom oder Ersatzstrom", "Einzelne Stromkreise oder das ganze Haus bei Netzausfall."),
            ]),
        ),
        C.media_text(
            eyebrow="Notstrom und Ersatzstrom",
            h2="Notstrom: bei Stromausfall weiterlaufen, in zwei Stufen",
            paragraphs=[
                ("Notstrom ist die Basisvariante: Bei Netzausfall versorgt der Speicher einzelne, vorher definierte "
                 "Steckdosen, etwa für Kühlschrank, Heizungssteuerung und Licht. Die Leistung ist meist auf eine "
                 "Phase beschränkt und die PV-Anlage schaltet aus Sicherheitsgründen ab."),
                ("Ersatzstrom trennt das ganze Haus vom Netz und baut ein eigenes Inselnetz auf. Alle Steckdosen "
                 "und auch dreiphasige Geräte laufen weiter, und die Anlage darf den Speicher nachladen. So "
                 "erzeugen Sie auch bei einem längeren Ausfall tagsüber Strom und füllen den Speicher für die Nacht."),
            ],
            img=IMG["speicher"],
            alt="Batteriespeicher mit Notstromfunktion im Technikraum eines Wohnhauses",
            bullets=[
                "Notstrom: einzelne Stromkreise, einphasig",
                "Ersatzstrom: ganzes Haus, dreiphasig, PV lädt den Speicher nach",
                "Wir klären in der Planung, welche Stufe zu Ihrem Haus passt",
            ],
            reverse=True,
            cta=("/notstrom/", "Ratgeber: Notstrom mit Photovoltaik"),
        ),
        C.media_text(
            eyebrow="E-Mobilität",
            h2="Wallbox und E-Auto mit Sonnenstrom laden",
            paragraphs=[
                ("Eine Wallbox mit 11 kW lädt Ihr E-Auto zu Hause in Wolfsberg über Nacht oder, besser, tagsüber "
                 "mit Überschuss vom Dach. Das Energiemanagement startet die Ladung, sobald die Anlage mehr erzeugt "
                 "als das Haus verbraucht, und bremst sie, wenn Wolken kommen. So fahren Sie mit Strom, der Sie "
                 "nichts mehr kostet, statt mit Netzstrom."),
                ("Dasselbe System steuert Wärmepumpe und Speicher. Der Klima- und Energiefonds fördert ein "
                 "Energiemanagementsystem für Haushalte mit 50 Prozent, maximal 600 Euro (Registrierung vor der "
                 "ersten Rechnung, Stand Oktober 2026). Wir planen Wallbox und Steuerung gleich mit, damit "
                 "Leitungen und Zählerschrank passen."),
            ],
            img=IMG["ems"],
            alt="Energiemanagementsystem: Visualisierung von Photovoltaik, Speicher, Wallbox und Wärmepumpe",
            bullets=[
                "Wallbox 11 kW, lädt bevorzugt mit PV-Überschuss",
                "Energiemanagement steuert Wallbox, Speicher und Wärmepumpe",
                "EMS-Förderung: 50 % bis 600 € für Haushalte",
            ],
            cta=("ems", "Energiemanagementsystem im Detail"),
        ),
        C.media_text(
            eyebrow="Förderung in Wolfsberg",
            h2="Förderung: EAG, Made-in-Europe-Bonus und Landespauschale Kärnten",
            paragraphs=[
                ("Das Land Kärnten fördert 2026 private PV-Anlagen ab 5 kWp mit mindestens 5 kWh Speicher pauschal mit "
                 "3.000 Euro, die Speicher-Nachrüstung mit 1.000 Euro. Der Bund zahlt über den "
                 "EAG-Investitionszuschuss 150 Euro je kWp bis 10 kWp und 150 Euro je "
                 "kWh Speicher, europäische Komponenten bringen je 10 Prozent Made-in-Europe-Bonus (Stand Oktober 2026)."),
                ("Wir prüfen die passenden Programme für Ihr Projekt in Wolfsberg, halten die Fristen ein und "
                 "bereiten die Anträge vor. Welche Fristen gerade laufen, steht tagesaktuell auf unserer Förderseite; "
                 "die Details zur Landesförderung finden Sie im Ratgeber."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Photovoltaik-Förderung für ein Eigenheim",
            bullets=[
                "EAG 150 €/kWp und 150 €/kWh vom Bund, 10 % Made-in-Europe-Bonus",
                "3.000 € Landespauschale Kärnten für PV mit Speicher, 1.000 € für Speicher-Nachrüstung",
                "Anträge, Mitteilung an die Gemeinde und Netzanmeldung durch EBZ Energie",
                a("foerderung_kaernten", "PV-Förderung Kärnten 2026 im Detail"),
            ],
            cta=("foerderungen", "Aktuelle Förderungen 2026"),
            dark=True,
        ),
        C.finance_band(),
        C.audience_split(
            eyebrow="Für wen wir im Lavanttal planen",
            h2="Eigenheim, Landwirtschaft und Betrieb im Lavanttal",
            intro=("Das Lavanttal ist Wohn-, Agrar- und Industrieregion zugleich. Wir planen für alle drei und für "
                   "jedes Dach: Satteldach, Flachdach, Trapezblech."),
            left={
                "img": IMG["gen_eigenheim"],
                "alt": "Einfamilienhaus mit Photovoltaikanlage in Kärnten, Symbolbild für Eigenheime im Lavanttal",
                "title": "Eigenheim in Wolfsberg und Umgebung",
                "bullets": [
                    "10 kWp mit Speicher: rund 11.600 kWh im Jahr am Standort Wolfsberg",
                    "Speicher, Notstrom und Wallbox nach Bedarf",
                    "Landespauschale Kärnten plus EAG-Zuschuss, Finanzierung ab 147 € im Monat*",
                ],
                "cta": ("kontakt", "Beratung für mein Zuhause"),
            },
            right={
                "img": IMG["gen_gewerbe"],
                "alt": "Betriebsgebäude mit großer Photovoltaikanlage auf dem Trapezblechdach",
                "title": "Landwirtschaftlicher Betrieb und Firmengebäude",
                "bullets": [
                    "Stallgebäude und Firmendächer: Trapezblech geklemmt, ohne Bohrung",
                    "Hoher Eigenverbrauch tagsüber: Kühlung, Lüftung, Pumpen, Produktion",
                    "Referenz Gewerbe: 40 kWp Ost-West mit 40 kWh Speicher, rund 13.500 € Ersparnis im Jahr",
                ],
                "cta": ("pv_gewerbe", "Photovoltaik für Betriebe"),
            },
        ),
        C.reference_cards(
            eyebrow="Referenzen in Kärnten",
            h2="Anlagen, die sich rechnen. Mit Zahlen belegt.",
            intro=("Aus dem Bezirk Wolfsberg haben wir noch kein veröffentlichtes Referenzprojekt. Diese Anlagen aus "
                   "Kärnten und Oberösterreich zeigen, wie wir planen und was dabei herauskommt. Bild und Zahlen "
                   "gehören jeweils zum selben Projekt."),
            items=[
                {"img": IMG["ref_villach"],
                 "alt": "Photovoltaikanlage mit 10 kWp auf einem Einfamilienhaus in Villach",
                 "title": "Einfamilienhaus, Villach",
                 "specs": "10 kWp in Ost-West-Ausrichtung mit Notstrom, rund 11.000 kWh im Jahr.",
                 "result": "rund 80 %", "result_sub": "weniger Stromkosten"},
                {"img": IMG["ref_krumpendorf"],
                 "alt": "Photovoltaikanlage auf einem Mehrparteienhaus in Krumpendorf",
                 "title": "Mehrparteienhaus, Krumpendorf",
                 "specs": "25 kWp mit 25 kWh Speicher und Notstrom.",
                 "result": "4 Tage", "result_sub": "Bauzeit"},
                {"img": IMG["gewerbe_dach"],
                 "alt": "Gewerbe-Photovoltaikanlage 40 kWp auf Trapezblechdach in Oberösterreich",
                 "title": "Gewerbebetrieb, Oberösterreich",
                 "specs": "40 kWp Ost-West auf Trapezblech, 40 kWh Speicher, rund 40.000 kWh im Jahr.",
                 "result": "13.500 €", "result_sub": "Ersparnis pro Jahr"},
            ],
        ),
        C.founder_story(
            eyebrow="Persönliche Beratung vor Ort",
            h2="Mario Zintl kommt nach Wolfsberg, nicht nur sein Angebot",
            paragraphs=[
                ("Eine Anlage, die 25 Jahre und länger laufen soll, plant man nicht am Telefon. Deshalb kommen wir "
                 "zu Ihnen ins Lavanttal, schauen uns Dach, Zählerschrank und Verbrauch an und hören zu, was Sie "
                 "vorhaben: E-Auto, Wärmepumpe, Notstrom oder einfach eine kleinere Stromrechnung."),
                ("Sie bekommen danach ein Angebot, das Sie verstehen. Wenn eine kleinere Anlage besser passt, sage "
                 "ich Ihnen das. Und nach der Montage bleiben wir erreichbar."),
            ],
            quote="Sie sollen nach dem Gespräch nicht überredet sein, sondern wissen, was Sie tun.",
            name=AUTHOR, role=AUTHOR_ROLE,
            badge="Villach, Kärnten",
            cta=("kontakt", "Beratungstermin in Wolfsberg"),
        ),
        C.facts_panel(
            eyebrow="Standort und Kontakt",
            h2="EBZ Energie: Firmensitz in Villach, Beratung bei Ihnen in Wolfsberg",
            intro=("Unser Firmensitz liegt in Villach. Für die Erstberatung kommen wir zu Ihnen nach Wolfsberg "
                   "und ins Lavanttal, Besuche in Villach nach Terminvereinbarung."),
            rows=[
                ("Adresse", f"{NAP['name']}<br>{NAP['street']}, {NAP['zip']} {NAP['city']}"),
                ("Telefon", tel_link()),
                ("E-Mail", f'<a href="mailto:{NAP["email"]}">{NAP["email"]}</a>'),
                ("Öffnungszeiten", NAP["hours"]),
                ("Google-Bewertung", f"{NAP['rating']} von 5 aus {bew}"),
                ("Anfahrt", "Beratung und Besichtigung bei Ihnen vor Ort im Lavanttal, kostenlos. Termine im Büro in Villach nach Vereinbarung."),
                ("Einzugsgebiet", "Bezirk Wolfsberg (Wolfsberg, St. Andrä, St. Paul, Bad St. Leonhard, Lavamünd), ganz Kärnten und die Steiermark. Referenzen in 6 Bundesländern."),
                ("Firmendaten", "EBZ Energie GmbH, FN 597101 s, Mitglied der Wirtschaftskammer Kärnten (gelistet im WKO Firmen A-Z)"),
            ],
            actions=[("Route zum Firmensitz", MAPS_URL, ' target="_blank" rel="noopener"'),
                     ("Anrufen", NAP["phone_href"], "")],
        ).replace('<section class="section"', '<section id="standort" class="section"', 1),
        C.reviews_slider(reviews, rating=rating, count=count),
        C.steps_section(
            eyebrow="So läuft es ab",
            h2="Von der Beratung in Wolfsberg bis zur Übergabe",
            steps=[
                ("Beratung vor Ort", "Wir analysieren Verbrauch, Dach und Ziele bei Ihnen in Wolfsberg. Kostenlos und unverbindlich.", ""),
                ("Projektbericht", "Projektbericht mit 3D-Belegplan und Statikreport sowie ein transparentes Fixangebot.", ""),
                ("Förderung und Anmeldung", "EAG-Zuschuss, Landespauschale Kärnten, Mitteilung an die Gemeinde und Netzanmeldung: Wir bereiten alles vor.", ""),
                ("Montage und Übergabe", "Montage in 2 bis 4 Tagen, dachschonend und sturmsicher, Inbetriebnahme, Einschulung in die Monitoring-App. Danach Wartung und Service aus Villach.", ""),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section(
            "Photovoltaik in Kärnten",
            [("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
             ("foerderung_kaernten", "PV-Förderung Kärnten 2026"),
             ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage"),
             ("batteriespeicher", "Stromspeicher"),
             ("/notstrom/", "Notstrom bei Stromausfall"),
             ("ems", "Energiemanagementsystem"),
             ("pv_gewerbe", "Photovoltaik für Betriebe"),
             ("pv_villach", "Photovoltaik in Villach"),
             ("finanzierung", "Finanzierung ab 147 € im Monat"),
             ("referenzen", "Referenzen")],
        ),
        C.contact_section(
            headline="Ihr kostenloses Angebot für Photovoltaik in Wolfsberg",
            sub=("Sie erreichen uns telefonisch oder über das Formular. Wir kommen zu Ihnen ins Lavanttal und "
                 "zeigen Ihnen ehrlich, was auf Ihrem Dach möglich ist. Kostenlos und unverbindlich."),
            page_label="Photovoltaik Wolfsberg",
        ),
        C.finalcta(
            "Bereit für Ihre eigene Energiezukunft in Wolfsberg?",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags und "
            "vereinbaren einen Termin bei Ihnen vor Ort.",
        ),
        _footnote(),
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=IMG["gen_hero"])
    return write_page("photovoltaik-wolfsberg/index.html", html)


def _footnote():
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte: Eigenverbrauchsquoten und Preise auf Basis typischer Einfamilienhäuser,
      vor Förderung. Ersparnis und Amortisation hängen von Verbrauch, Anlagengröße, Ausrichtung und Strompreis ab.
      Ertragswerte laut PV-Atlas (pvatlas.at), Fördersätze, Fristen und OeMAG-Marktpreis Stand Oktober 2026,
      Änderungen durch Fördergeber und OeMAG vorbehalten. Finanzierung: Beispielkonditionen, vorbehaltlich
      Bonitätsprüfung. Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    build()
