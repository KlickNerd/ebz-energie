"""Kontaktseite (/kontakt/): Formular, direkte Wege, Ablauf nach der Anfrage, NAP, Einzugsgebiet.

LocalBusiness-Schema wird hier (neben der Startseite) eingebettet.
"""

from common import IMG, NAP, EMAIL, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, href, tel_link, write_page, load_reviews
from layout import page
import components as C

PATH = "/kontakt/"
TITLE = "Kontakt: kostenlose PV-Beratung in Villach | EBZ Energie"
DESC = ("Kostenlose Erstberatung zu Photovoltaik, Speicher, Wärmepumpe und Energiegemeinschaft in Kärnten und Steiermark. Antwort in einem Werktag, Mo bis Fr 10 bis 20 Uhr.")

FAQ = [
    ("Was kostet die Erstberatung?",
     "Nichts. Das erste Gespräch und der Vor-Ort-Termin in Kärnten und der Steiermark sind kostenlos und "
     "unverbindlich. Sie erhalten anschließend einen Projektbericht mit 3D-Belegplan und Statikreport."),
    ("Wie schnell meldet sich EBZ Energie?",
     "In der Regel innerhalb eines Werktags, telefonisch oder per E-Mail. Wer es eilig hat, erreicht uns "
     "Montag bis Freitag von 10 bis 20 Uhr direkt unter +43 650 220 26 26."),
    ("Welche Angaben helfen bei der Anfrage?",
     "Je mehr wir wissen, desto konkreter die Antwort: Ort, Gebäudetyp (Eigenheim oder Betrieb), ungefährer "
     "Stromverbrauch pro Jahr, Interesse an Speicher, Wärmepumpe, Wallbox oder Energiegemeinschaft. Ein Foto "
     "vom Dach oder die letzte Stromrechnung beschleunigt die Planung."),
    ("Beraten Sie auch außerhalb von Kärnten und der Steiermark?",
     "Montiert wird in Kärnten und der Steiermark. Für Energiegemeinschaften beraten wir österreichweit, und "
     "für Projekte in anderen Bundesländern prüfen wir die Machbarkeit auf Anfrage; Referenzen gibt es in "
     "sechs Bundesländern."),
]


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        C.page_hero(
            eyebrow="Kontakt",
            h1="Ihr direkter Draht nach Villach",
            lead=("Kein Callcenter, keine Warteschleife: Sie sprechen mit Menschen aus der Region, die Ihre "
                  "Anlage später auch planen und montieren. Schreiben Sie uns oder rufen Sie an."),
            cta=("#beratung", "Anfrage schreiben"),
            cta2=(NAP["phone_href"], "☎ " + NAP["phone_display"]),
        ),
        C.kpis([
            ("1 Werktag", "bis zur Rückmeldung"),
            ("Mo bis Fr", "10:00 bis 20:00 Uhr erreichbar"),
            (NAP["rating"], f"Sterne auf Google ({count} Bewertungen)" if count else "Sterne auf Google"),
            ("300+", "Projekte in 6 Bundesländern"),
        ]),
        C.contact_section(
            "Kostenlose Erstberatung anfragen",
            ("Ob Photovoltaik, Speicher, Wärmepumpe, Energiemanagement oder Energiegemeinschaft: Schildern Sie "
             "kurz Ihr Vorhaben, wir melden uns mit einer ehrlichen Einschätzung."),
            form_note="Wir melden uns innerhalb eines Werktags. Ihre Daten verwenden wir nur zur Bearbeitung der Anfrage.",
            page_label="Kontaktseite",
        ),
        C.steps_section(
            eyebrow="Was passiert nach Ihrer Anfrage?",
            h2="Klar und ohne Druck",
            steps=[
                ("Ihre Anfrage kommt an", "Wir lesen Ihre Nachricht hier in Villach und ordnen sie dem passenden Ansprechpartner für Kärnten oder die Steiermark zu.", "sofort"),
                ("Persönliche Rückmeldung", "Ein kurzes Telefonat, um Ihr Projekt zu verstehen und offene Fragen zu klären.", "innerhalb eines Werktags"),
                ("Kostenlose Beratung vor Ort", "Wir schauen uns Dach, Zählerkasten und Verbrauch an und zeigen erste Lösungen, unverbindlich.", "nach Terminvereinbarung"),
                ("Projektbericht", "Sie erhalten Ihren Projektbericht mit 3D-Belegplan und Statikreport sowie die Zahlen für Kauf und Finanzierung.", "wenige Tage später"),
            ],
        ),
        C.founder_block(
            "Bei uns landet Ihre Anfrage nicht in einem Postfach, das niemand liest. Ich schaue mir jedes "
            "Projekt selbst an, und wenn eine kleinere Anlage besser passt, sage ich das auch."
        ),
        C.facts_panel(
            eyebrow="So erreichen Sie uns",
            h2="Adresse, Zeiten und Anfahrt",
            intro="Unser Standort liegt in Villach. Termine vor Ort vereinbaren wir telefonisch oder über das Formular.",
            rows=[
                ("Firmierung", NAP["name"]),
                ("Geschäftsführung", AUTHOR),
                ("Adresse", f"{NAP['street']}, {NAP['zip']} {NAP['city']}, Kärnten"),
                ("Telefon", tel_link()),
                ("E-Mail", f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
                ("Öffnungszeiten", NAP["hours"]),
                ("Montagegebiet", "Kärnten und Steiermark"),
                ("Energiegemeinschaft", "Beratung österreichweit"),
            ],
            actions=[
                ("Route auf Google Maps", "https://www.google.com/maps?cid=15592511037270601677",
                 ' target="_blank" rel="noopener"'),
                ("Zum Impressum", href("impressum"), ""),
            ],
        ),
        C.reviews_slider(reviews, rating, count),
        C.faq_section(FAQ),
        C.linkgrid_section("Das könnte Sie interessieren", [
            ("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
            ("finanzierung", "Finanzierung ohne Anzahlung"),
            ("foerderung_at", "Förderungen 2026"),
            ("ratgeber", "Alle Ratgeber"),
        ]),
        C.finalcta(
            "Lieber gleich anrufen?",
            "Montag bis Freitag von 10 bis 20 Uhr erreichen Sie uns direkt. Alles andere klären wir beim kostenlosen Termin vor Ort.",
            cta=("#beratung", "Anfrage schreiben"),
        ),
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                include_business_schema=True, og_image=IMG["team_beratung"])
    return write_page("kontakt/index.html", html)
