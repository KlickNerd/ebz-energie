"""Kontaktseite (/kontakt/): kostenlose Photovoltaik-Beratung, Formular, Ablauf, NAP, Einzugsgebiet.

SEO-Rolle (build/seo/kontakt.json, Oktober 2026): Primaer "photovoltaik beratung" (+ Kaernten/Villach).
Neu: "Was die Beratung beinhaltet" (Checkliste), Vorbereitungs-Checkliste, Terminwege, belegbare
Fristen nur aus Kundenbewertungen (Rueckruf am naechsten Tag, Besichtigung innerhalb einer Woche,
Angebot am Folgetag) und CLAUDE.md (Antwort in einem Werktag).
LocalBusiness-Schema wird hier (neben der Startseite) eingebettet.
"""

from common import IMG, NAP, EMAIL, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, href, tel_link, write_page, load_reviews
from layout import page
import components as C

PATH = "/kontakt/"
TITLE = "Photovoltaik-Beratung in Villach: kostenlos anfragen | EBZ"
DESC = ("Kostenlose Photovoltaik-Beratung von EBZ Energie, Villach: Vor-Ort-Termin in Kärnten und Steiermark, "
        "Projektbericht mit 3D-Belegplan, Antwort in einem Werktag.")

FAQ = [
    ("Was beinhaltet die kostenlose Photovoltaik-Beratung von EBZ Energie?",
     "Beim Vor-Ort-Termin prüfen wir Dach (Fläche, Ausrichtung, Verschattung, Eindeckung), Zählerkasten und "
     "Netzanschluss, Ihren Stromverbrauch in kWh pro Jahr und Ihre Pläne für Speicher, Wärmepumpe, Wallbox oder "
     "Energiegemeinschaft. Daraus leiten wir Anlagengröße in kWp und Speichergröße ab, prüfen die Förderung in "
     "Kärnten oder der Steiermark und erstellen ein Festpreis-Angebot mit Projektbericht, 3D-Belegplan und Statikreport."),
    ("Was kostet die Erstberatung?",
     "Nichts. Das erste Gespräch und der Vor-Ort-Termin in Kärnten und der Steiermark sind kostenlos und "
     "unverbindlich. Sie erhalten anschließend einen Projektbericht mit 3D-Belegplan und Statikreport."),
    ("Wie lange dauert es von der Anfrage bis zum Angebot?",
     "Wir melden uns innerhalb eines Werktags. Laut Kundenbewertungen auf Google folgt die Besichtigung vor Ort "
     "meist innerhalb einer Woche, das schriftliche Angebot kam bei mehreren Projekten schon am Tag nach dem Termin. "
     "Ein Kunde berichtet von fünf Wochen von der Beratung bis zur fertigen Anlage. Verbindlich ist das Datum, das "
     "wir mit Ihnen vereinbaren."),
    ("Was sollte ich zum Beratungstermin vorbereiten?",
     "Die letzte Jahresstromrechnung (Verbrauch in kWh), ein Foto vom Dach und vom Zählerkasten, wenn vorhanden "
     "einen Grundriss oder Dachmaße, und Ihre Pläne: E-Auto, Wärmepumpe, Pool, Anbau. Je mehr wir wissen, desto "
     "genauer wird das Angebot. Fehlt etwas, nehmen wir es beim Termin auf."),
    ("Ist die Beratung unabhängig oder an einen Kauf gebunden?",
     "Wir sind ein Fachbetrieb, der auch montiert, keine unabhängige Energieberatung Villach oder Kärnten, wie sie "
     "das Land anbietet. Die Beratung ist "
     "trotzdem unverbindlich: Sie entscheiden nach dem Angebot in Ruhe, es gibt keine Verpflichtung. Und wenn eine "
     "kleinere Anlage besser passt oder sich ein Speicher bei Ihnen nicht rechnet, sagen wir das."),
    ("Beraten Sie auch zu Förderung und Finanzierung?",
     "Ja, das ist Teil jeder Beratung. Wir prüfen Landespauschale Kärnten (3.000 € für PV ab 5 kWp mit Speicher, "
     "Einreichung 12. Oktober bis 31. Dezember 2026), Förderung Steiermark und den EAG-Zuschuss des Bundes und "
     "stellen die Anträge. Auf Wunsch rechnen wir eine Finanzierung ab 147 € im Monat* durch: Eigentum ab Tag 1, "
     "0 € Anzahlung, fixe Rate."),
    ("Kann ich auch telefonisch, per Video oder bei Ihnen in Villach beraten werden?",
     "Ja. Ein erstes Gespräch führen wir gern am Telefon oder per Video, damit Sie Ihre Fragen schnell klären. Für "
     "ein belastbares Angebot kommen wir dann zu Ihnen, weil wir Dach und Zählerkasten sehen müssen. Ein Besuch bei "
     "uns in der Triglavstraße 15 in Villach ist nach Terminvereinbarung möglich, Montag bis Freitag von 10 bis 20 Uhr."),
    ("Beraten Sie auch außerhalb von Kärnten und der Steiermark?",
     "Montiert wird in Kärnten und der Steiermark. Für Energiegemeinschaften beraten wir österreichweit, und "
     "für Projekte in anderen Bundesländern prüfen wir die Machbarkeit auf Anfrage; Referenzen gibt es in "
     "sechs Bundesländern."),
]


def build():
    rating, count, reviews = load_reviews()
    bew = f"{count} Bewertungen" if count else "echten Bewertungen"
    body = "".join([
        C.page_hero(
            eyebrow="Photovoltaik Beratung Kärnten und Steiermark",
            h1="Kostenlose Photovoltaik-Beratung in Villach für Kärnten und die Steiermark",
            lead=("Kein Callcenter, keine Warteschleife: Ihre PV Beratung kommt von Menschen aus der Region, die "
                  "Ihre Anlage später auch planen und montieren. Schreiben Sie uns oder rufen Sie an, wir melden "
                  "uns innerhalb eines Werktags."),
            cta=("#beratung", "Angebot anfordern"),
            cta2=(NAP["phone_href"], "☎ " + NAP["phone_display"]),
        ),
        C.kpis([
            ("1 Werktag", "bis zur Rückmeldung"),
            ("1 Woche", "bis zum Vor-Ort-Termin, laut Kundenbewertungen"),
            (NAP["rating"], f"Sterne auf Google ({bew})"),
            ("Mo bis Fr", "10:00 bis 20:00 Uhr erreichbar"),
        ]),
        C.contact_section(
            "Kostenlose Erstberatung anfragen",
            ("Ob Photovoltaik, Speicher, Wärmepumpe, Energiemanagement oder Energiegemeinschaft: Schildern Sie "
             "kurz Ihr Vorhaben, wir melden uns mit einer ehrlichen Einschätzung. Nennen Sie am besten PLZ und "
             "Ort, damit wir Förderung und Netzbetreiber für Kärnten oder die Steiermark gleich mitdenken."),
            form_note="Wir melden uns innerhalb eines Werktags. Ihre Daten verwenden wir nur zur Bearbeitung der Anfrage.",
            page_label="Kontaktseite",
        ),
        C.text_block(
            eyebrow="Inhalt der Beratung",
            h2="Was die Photovoltaik-Beratung beinhaltet",
            paragraphs=[
                ("Die kostenlose Photovoltaik-Beratung von EBZ Energie findet bei Ihnen vor Ort in Kärnten oder der "
                 "Steiermark statt: Dach, Zählerkasten und Verbrauch werden aufgenommen, Anlagengröße, Speicher und Förderung geklärt. Das Ergebnis ist ein "
                 "Festpreis-Angebot mit Projektbericht, 3D-Belegplan und Statikreport (Stand Oktober 2026)."),
            ],
            max_w="78ch",
        ),
        C.split_section(
            left={"title": "Das klären wir beim Termin", "items": [
                "Dachbesichtigung: Fläche, Ausrichtung, Neigung, Verschattung, Eindeckung und Statik",
                "Zählerkasten und Netzanschluss: Platz für Wechselrichter und Speicher, Netzbetreiber (Kärnten Netz, Energienetze Steiermark)",
                "Stromverbrauch in kWh pro Jahr und Ihr Tagesprofil",
                "Anlagengröße in kWp und Speichergröße in kWh, passend zu Verbrauch und Budget",
                "Wärmepumpe, Wallbox, Notstrom, Energiegemeinschaft: was sich kombinieren lässt",
                "Förder-Check: Landespauschale Kärnten, Förderung Steiermark, EAG-Zuschuss des Bundes",
                "Kostenvoranschlag als Festpreis-Angebot, auf Wunsch mit Finanzierung ab 147 € im Monat*",
            ]},
            right={"title": "Was Sie vorbereiten können", "dark": True, "items": [
                "Letzte Jahresstromrechnung (Verbrauch in kWh)",
                "Foto vom Dach und vom Zählerkasten",
                "Grundriss, Dachmaße oder Einreichplan, falls vorhanden",
                "Ihre Pläne: E-Auto, Wärmepumpe, Pool, Anbau, Energiegemeinschaft",
                "Offene Fragen: Wir beantworten sie beim Termin oder vorab am Telefon",
            ], "note": "Nichts davon ist Pflicht. Was fehlt, nehmen wir beim Termin gemeinsam auf."},
        ),
        C.steps_section(
            eyebrow="Was passiert nach Ihrer Anfrage?",
            h2="So geht es nach Ihrer Anfrage weiter",
            steps=[
                ("Ihre Anfrage kommt an", "Wir lesen Ihre Nachricht hier in Villach und ordnen sie dem passenden Ansprechpartner für Kärnten oder die Steiermark zu.", "sofort"),
                ("Persönliche Rückmeldung", "Ein kurzes Telefonat, um Ihr Projekt zu verstehen und offene Fragen zu klären.", "innerhalb eines Werktags"),
                ("Kostenlose Beratung vor Ort", "Wir schauen uns Dach, Zählerkasten und Verbrauch an und zeigen erste Lösungen, unverbindlich.", "meist innerhalb einer Woche*"),
                ("Angebot mit Projektbericht", "Festpreis-Angebot mit Projektbericht, 3D-Belegplan und Statikreport sowie die Zahlen für Kauf und Finanzierung.", "wenige Tage, oft am Folgetag*"),
            ],
        ),
        C.why_section(
            eyebrow="Terminwege",
            h2="So erreichen Sie uns: Telefon, Formular, Vor-Ort-Termin",
            items=[
                ("☎", "Anrufen", f"Montag bis Freitag von 10 bis 20 Uhr unter {tel_link()}. Für ein erstes Gespräch oder gleich einen Termin."),
                ("✉", "Schreiben", f'Formular oben oder E-Mail an <a href="mailto:{EMAIL}">{EMAIL}</a>. Antwort innerhalb eines Werktags.'),
                ("⌂", "Vor-Ort-Termin", "Kostenlose Besichtigung bei Ihnen in Kärnten oder der Steiermark, meist innerhalb einer Woche*."),
                ("◫", "Telefon- oder Videoberatung", "Für Fragen zu Förderung, Speicher oder Energiegemeinschaft, bevor wir Ihr Dach anschauen."),
                ("◎", "Besuch in Villach", f"Nach Terminvereinbarung in der {NAP['street']}, {NAP['zip']} {NAP['city']}."),
                ("◇", "Rückruf", "Nennen Sie im Formular Ihre Nummer und Wunschzeit, wir rufen zurück."),
            ],
        ),
        C.founder_block(
            "Bei uns landet Ihre Anfrage nicht in einem Postfach, das niemand liest. Ich schaue mir jedes "
            "Projekt selbst an, und wenn eine kleinere Anlage besser passt, sage ich das auch."
        ),
        C.facts_panel(
            eyebrow="So erreichen Sie uns",
            h2="Adresse, Öffnungszeiten und Anfahrt",
            intro=("Sie suchen eine Photovoltaik Firma in der Nähe? Unser Standort liegt in Villach, Termine vor Ort "
                   "vereinbaren wir telefonisch oder über das Formular."),
            rows=[
                ("Firmierung", NAP["name"]),
                ("Geschäftsführung", AUTHOR),
                ("Adresse", f"{NAP['street']}, {NAP['zip']} {NAP['city']}, Kärnten"),
                ("Telefon", tel_link()),
                ("E-Mail", f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
                ("Öffnungszeiten", NAP["hours"]),
                ("Anfahrt", "Besuch nach Terminvereinbarung. Für die Erstberatung kommen wir in der Regel zu Ihnen."),
                ("Montagegebiet", "Kärnten und Steiermark"),
                ("Energiegemeinschaft", "Beratung österreichweit"),
                ("Google-Bewertung", f"{NAP['rating']} von 5 aus {bew}"),
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
            ("pv_villach", "Photovoltaik in Villach"),
            ("referenzen", "300+ Projekte: Referenzen mit echten Zahlen"),
            ("ueber_uns", "Wer Sie berät: EBZ Energie GmbH"),
            ("solarrechner", "Vorab selbst rechnen: Solarrechner"),
            ("foerderung_kaernten", "Förderung Kärnten 2026"),
            ("foerderung_steiermark", "Förderung Steiermark 2026"),
            ("finanzierung", "Finanzierung ab 147 € pro Monat"),
            ("/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/", "Was kostet eine 10-kWp-Anlage mit Speicher?"),
        ]),
        C.finalcta(
            "Lieber gleich anrufen?",
            "Montag bis Freitag von 10 bis 20 Uhr erreichen Sie uns direkt. Alles andere klären wir beim kostenlosen Termin vor Ort.",
            cta=("#beratung", "Angebot anfordern"),
        ),
        _footnote(),
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                include_business_schema=True, og_image=IMG["team_beratung"])
    return write_page("kontakt/index.html", html)


def _footnote():
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Zeitangaben zu Vor-Ort-Termin und Angebot stammen aus Kundenbewertungen auf Google
      (Stand Oktober 2026) und sind Erfahrungswerte, keine Zusage; verbindlich ist der mit Ihnen vereinbarte Termin.
      Suchanfragen wie „PV Anlage Angebot“ oder „Photovoltaik Angebot“ landen oft bei Vergleichsportalen; bei uns kommt
      das Angebot direkt vom Betrieb, der auch montiert. Finanzierung: Beispielkonditionen, vorbehaltlich Bonitätsprüfung.
      Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    build()
