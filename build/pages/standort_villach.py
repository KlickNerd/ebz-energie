"""Standortseite Photovoltaik Villach (/photovoltaik-villach/).

Kommerzieller Suchintent "photovoltaik villach". Quelle: Live-Seite
/photovoltaik-villach/ (WP-Beitrag). Bereinigt: falsche Notstrom-Absaetze unter
"Finanzielle Entlastung" entfernt, "25 Jahre Leistungsgarantie" -> bis zu 30 Jahre,
Gedankenstriche, Superlative. Lokale Fakten nur aus Quelle bzw. Repo-Ratgeber
(Kaernten ueber 1.900 Sonnenstunden, Landespauschale 3.000 Euro).
"""

from common import IMG, NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, S, faq_jsonld, u, a, href, tel_link, write_page, load_reviews
from layout import page
import components as C

PATH = "/photovoltaik-villach/"
TITLE = "Photovoltaik Villach: Fachbetrieb vor Ort | EBZ Energie"
DESC = ("Photovoltaik in Villach vom Fachbetrieb vor Ort: Planung, Montage, Speicher und Förderung "
        "Kärnten aus einer Hand. Referenz 10 kWp: rund 80 % weniger Strom.")

HERO_IMG = "/assets/img/pv-villach-stadt.jpg"

MAPS_URL = "https://www.google.com/maps/search/?api=1&query=Triglavstra%C3%9Fe+15%2C+9500+Villach"

FAQ = [
    ("Was kostet eine Photovoltaikanlage in Villach?",
     "Eine Komplettanlage mit rund 10 kWp und Speicher liegt typischerweise bei rund 15.000 bis 22.000 Euro vor "
     "Förderung. Der genaue Preis hängt von Dach, Speichergröße und Ausstattung ab. Das Land Kärnten zahlt für "
     "neue private Anlagen ab 5 kWp mit Speicher eine Pauschale von 3.000 Euro, dazu kommt die Bundesförderung."),
    ("Wie bestimme ich die richtige Größe für meine Anlage in Villach?",
     "Die Größe in kWp richtet sich nach Ihrem Stromverbrauch, der geeigneten Dachfläche und Ihren Plänen, etwa "
     "E-Auto oder Wärmepumpe. Wir kommen zu Ihnen nach Villach oder in die Umgebung, analysieren Dach und "
     "Verbrauch und legen die Anlage im Projektbericht mit 3D-Belegplan und Statikreport aus."),
    ("Lohnt sich Photovoltaik in Villach überhaupt?",
     "Ja. Kärnten zählt mit über 1.900 Sonnenstunden im Jahr zu den einstrahlungsreichsten Regionen Österreichs. "
     "Unsere Referenz in Villach, ein Einfamilienhaus mit 10 kWp in Ost-West-Ausrichtung, erzeugt rund 11.000 kWh "
     "im Jahr und senkt die Stromkosten um rund 80 Prozent. Typisch rechnet sich eine Anlage in 4 bis 6 Jahren."),
    ("Wie lange hält eine Photovoltaikanlage?",
     "Moderne Anlagen sind auf 25 bis 30 Jahre und mehr ausgelegt. Auf die Module gibt es bis zu 30 Jahre "
     "Leistungsgarantie und mindestens 10 Jahre Produktgarantie. Wir setzen auf hochwertige Komponenten, damit "
     "Ihre Anlage in Villach viele Jahre zuverlässig produziert."),
    ("Brauche ich einen Stromspeicher zu meiner PV-Anlage?",
     "Nicht zwingend, aber ein Speicher ist die wichtigste Ergänzung. Ohne Speicher nutzen Sie Ihren Sonnenstrom "
     "nur, während die Sonne scheint. Mit Speicher steht er auch abends und nachts zur Verfügung, der "
     "Eigenverbrauch steigt deutlich und Notstrom wird möglich."),
    ("Übernimmt EBZ Energie die Förderanträge und die Anmeldung beim Netzbetreiber?",
     "Ja. Wir kennen die Programme von Land Kärnten und Bund, bereiten die Anträge vor und kümmern uns um die "
     "Anmeldung beim Netzbetreiber, den Zählertausch und die Inbetriebnahme. Sie bekommen eine schlüsselfertige Anlage."),
    ("Kann ich bei EBZ Energie in Villach persönlich vorbeikommen?",
     "Ja, nach Terminvereinbarung in der Triglavstraße 15, 9500 Villach, Montag bis Freitag von 10:00 bis 20:00 Uhr. "
     "Die Beratung findet meist direkt bei Ihnen vor Ort statt, weil wir Dach, Zählerschrank und Verbrauch "
     "gleich mit aufnehmen."),
]

KAERNTEN = ["Villach", "Klagenfurt", "Spittal an der Drau", "Feldkirchen",
            "St. Veit an der Glan", "Wolfsberg", "Völkermarkt", "Hermagor"]
STEIERMARK = ["Graz", "Leibnitz", "Deutschlandsberg", "Voitsberg",
              "Weiz", "Murtal", "Leoben", "Südoststeiermark"]


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        C.hero(
            eyebrow="Photovoltaik Villach",
            h1="Photovoltaik in Villach: Ihr Fachbetrieb aus der Triglavstraße",
            lead=("Sonnenstrom vom eigenen Dach, geplant und montiert von einem Betrieb, der selbst in Villach "
                  "zuhause ist. Wir kommen zu Ihnen, prüfen Dach und Verbrauch und übernehmen Förderung, "
                  "Netzanmeldung und Montage. Für Eigenheim und Betrieb in Villach, Klagenfurt und Umgebung."),
            badges=[("Aus Villach", "für Villach"),
                    ("Förderung Kärnten", "inklusive Antrag"),
                    ("bis zu 85 %", "weniger Stromkosten")],
            img=HERO_IMG,
            img_alt="Stadtansicht von Villach in Kärnten, Standort von EBZ Energie",
            float_num=rating,
            float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_secondary=("#standort", "Standort und Kontakt"),
        ),
        C.kpis([
            ("rund 80 %", "weniger Stromkosten, EFH Villach (10 kWp)"),
            ("1.900+", "Sonnenstunden im Jahr in Kärnten"),
            ("3.000 €", "Landespauschale Kärnten für PV mit Speicher"),
            (NAP["rating"], "Sterne auf Google"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Warum sich Photovoltaik in Villach lohnt",
            paragraphs=[
                ("Kärnten gehört mit über 1.900 Sonnenstunden im Jahr zu den sonnenreichsten Regionen "
                 "Österreichs. Eine Photovoltaikanlage in Villach wandelt dieses Licht in Strom um, den Sie "
                 "direkt im Haus oder Betrieb verbrauchen. Was Sie selbst erzeugen, kaufen Sie nicht mehr teuer "
                 "aus dem Netz."),
                ("Das Land Kärnten und der Bund fördern den Einstieg. Mit Speicher nutzen Sie den Sonnenstrom "
                 "auch am Abend, mit Notstrom bleibt Ihr Haus bei einem Netzausfall versorgt. Typisch rechnet "
                 "sich eine Anlage in 4 bis 6 Jahren."),
            ],
        ),
        C.audience_split(
            eyebrow="Für wen planen wir in Villach?",
            h2="Eigenheim oder Betrieb: Ihre Anlage passt zu Ihrem Verbrauch",
            intro="Jedes Dach und jeder Strombedarf ist anders. Wir legen Größe, Speicher und Wirtschaftlichkeit genau darauf aus.",
            left={
                "img": IMG["gen_eigenheim"],
                "alt": "Einfamilienhaus mit Photovoltaikanlage in Kärnten",
                "title": "Für Ihr Zuhause in Villach",
                "bullets": [
                    "Bis zu 85 % weniger Stromkosten",
                    "Speicher und Notstrom für Abend und Netzausfall",
                    "Landespauschale Kärnten plus Bundesförderung, Finanzierung ab 147 € im Monat",
                ],
                "cta": ("kontakt", "Beratung für mein Zuhause"),
            },
            right={
                "img": IMG["gen_gewerbe"],
                "alt": "Betriebsgebäude mit großer Photovoltaikanlage am Dach",
                "title": "Für Ihren Betrieb in Villach oder Klagenfurt",
                "bullets": [
                    "Hoher Eigenverbrauch tagsüber senkt die Betriebskosten",
                    "Anlagen auch mit hoher kWp-Leistung, Planung nach Lastprofil",
                    "Beispiel Hotel Villach/Warmbad: 13 kWp, rund 4.200 € Ersparnis pro Jahr",
                ],
                "cta": ("pv_gewerbe", "Photovoltaik für Gewerbe"),
            },
        ),
        C.problem_compare(
            eyebrow="Finanzielle Entlastung",
            h2="Schutz vor Preiserhöhungen, Wertsteigerung für Ihr Haus",
            intro=("Mit eigener Anlage werden Sie vom Konsumenten zum Erzeuger. Ein großer Teil Ihres "
                   "Stroms kommt vom Dach, zu Kosten, die über Jahrzehnte feststehen. Ein Gebäude mit "
                   "niedrigen Betriebskosten ist zudem auf dem Markt in Villach deutlich attraktiver."),
            bars=[
                ("Stromkosten ohne eigene Anlage", 100, "bad", "voller Netzbezug"),
                ("Stromkosten mit Photovoltaik und Speicher", 15, "good", "bis zu 85 % weniger*"),
            ],
            aside=("Ihre Vorteile in Villach", [
                ("☀", "Eigener Strom", "Sie erzeugen Ihren Strom selbst und werden unabhängiger von Preissteigerungen."),
                ("€", "Förderung Kärnten", "3.000 € Landespauschale für private PV ab 5 kWp mit Speicher, dazu der Bund."),
                ("▮", "Speicher und Notstrom", "Sonnenstrom auch abends, Versorgung auch bei Netzausfall."),
                ("⌂", "Wertsteigerung", "Ein Haus mit eigener Energieversorgung gilt als zukunftssicher."),
            ]),
        ),
        C.media_text(
            eyebrow="Mehr Unabhängigkeit mit Speicher",
            h2="Eigenverbrauch und Stromspeicher: der Schlüssel zur Unabhängigkeit",
            paragraphs=[
                ("Ohne Speicher nutzen Sie Ihren Sonnenstrom nur, während die Sonne scheint, und speisen den "
                 "Überschuss für wenige Cent ein. Ein Stromspeicher hält den Strom vom Tag für Abend und Nacht "
                 "bereit, wenn der Bedarf im Haushalt am höchsten ist."),
                ("Deshalb planen wir den Speicher als zentrales Element im System mit, nicht als Zubehör. Mit "
                 "Notstromfunktion bleibt Ihr Zuhause in Villach auch bei einem Stromausfall versorgt."),
            ],
            img=IMG["speicher"],
            alt="Batteriespeicher einer Photovoltaikanlage im Technikraum",
            bullets=[
                "Deutlich höherer Eigenverbrauch statt günstiger Einspeisung",
                "Sonnenstrom auch am Abend und in der Nacht",
                "Optional mit Notstrom bei Netzausfall",
            ],
            reverse=True,
            cta=("batteriespeicher", "Mehr zum Batteriespeicher"),
        ),
        C.media_text(
            eyebrow="Förderung Kärnten",
            h2="Förderung für Photovoltaik in Villach: Land Kärnten und Bund",
            paragraphs=[
                ("Das Land Kärnten zahlt 2026 eine Pauschale von 3.000 Euro für neue private PV-Anlagen ab 5 kWp "
                 "mit Speicher. Der Bund fördert über den EAG-Investitionszuschuss mit 150 Euro je kWp bis 10 kWp "
                 "und 150 Euro je kWh Speicher, europäische Komponenten bringen 10 Prozent Bonus."),
                ("Sich hier zurechtzufinden kostet Zeit. Als Ihr Partner aus Villach übernehmen wir die Abwicklung: "
                 "Wir prüfen, welche Programme zu Ihrem Projekt passen, halten Fristen und Reihenfolge ein und "
                 "bereiten die Anträge vor."),
            ],
            img=IMG["foerderung"],
            alt="Beratung zur Photovoltaik-Förderung in Kärnten am Tisch",
            bullets=[
                "3.000 € Landespauschale Kärnten für PV mit Speicher",
                "150 €/kWp und 150 €/kWh vom Bund, 10 % Made-in-Europe-Bonus",
                "Antrag und Abwicklung durch EBZ Energie",
            ],
            cta=("foerderung_kaernten", "PV-Förderung Kärnten 2026 im Detail"),
            dark=True,
        ),
        C.media_text(
            eyebrow="Unser Service für Villach",
            h2="Planung, Installation und Service aus einer Hand",
            paragraphs=[
                ("Wir nehmen uns Zeit für Ihr Projekt. Die Analyse findet bei Ihnen vor Ort in Villach, Klagenfurt "
                 "oder in der Umgebung statt: Dach, Zählerschrank, Verbrauch und Ihre Pläne für E-Auto oder "
                 "Wärmepumpe. Daraus entsteht Ihr Projektbericht mit 3D-Belegplan und Statikreport."),
                ("Zertifizierte Fachkräfte montieren Ihre Anlage sauber und termintreu, Elektrik und Dach aus einem "
                 "Team. Wir planen Ihr Energiesystem als Ganzes, vom Speicher bis zur Wallbox, und bleiben nach "
                 "der Inbetriebnahme Ihr Ansprechpartner in Villach für Monitoring, Wartung und Erweiterung."),
            ],
            img=IMG["team_beratung"],
            alt="Beratungsgespräch mit dem Team von EBZ Energie in Villach",
            bullets=[
                "Analyse und Beratung bei Ihnen vor Ort",
                "Förderung, Netzanmeldung und Zählertausch inklusive",
                "Service und Monitoring nach der Übergabe",
            ],
            cta=("ems", "Speicher, Wallbox und Wärmepumpe im System"),
        ),
        C.finance_band(),
        C.reference_cards(
            eyebrow="Referenz aus Villach",
            h2="Anlagen in Villach und am Wörthersee, mit Zahlen belegt",
            intro=("So sehen typische Anlagen aus unserer Region aus. Bild und Zahlen gehören jeweils zum selben "
                   "Projekt. Das Hotel in Villach/Warmbad (13 kWp, 27 kWh Speicher, rund 4.200 € Ersparnis im "
                   "Jahr) finden Sie auf der Referenzseite."),
            items=[
                {"img": IMG["ref_villach"],
                 "alt": "Photovoltaikanlage mit 10 kWp auf einem Einfamilienhaus in Villach",
                 "title": "Einfamilienhaus, Villach",
                 "specs": "10 kWp in Ost-West-Ausrichtung mit Notstrom, rund 11.000 kWh im Jahr.",
                 "result": "rund 80 %", "result_sub": "weniger Stromkosten"},
                {"img": IMG["ref_krumpendorf"],
                 "alt": "Photovoltaikanlage auf einem Mehrparteienhaus in Krumpendorf am Wörthersee",
                 "title": "Mehrparteienhaus, Krumpendorf",
                 "specs": "25 kWp mit 25 kWh Speicher und Notstrom.",
                 "result": "4 Tage", "result_sub": "Bauzeit"},
            ],
        ),
        C.founder_story(
            eyebrow="Persönliche Beratung vor Ort",
            h2="Mario Zintl: in Villach aufgewachsen, in Villach im Einsatz",
            paragraphs=[
                ("Ich bin in Villach aufgewachsen und kenne die Dächer hier: Ost-West-Giebel in den Siedlungen, "
                 "Flachdächer in Warmbad, Mehrparteienhäuser am See. Wenn Sie anfragen, komme ich oder jemand "
                 "aus meinem Team persönlich vorbei und schaut sich Dach, Zählerschrank und Verbrauch an."),
                ("Sie bekommen keine Standardanlage aus dem Katalog, sondern einen Projektbericht mit 3D-Belegplan "
                 "und Statikreport für Ihr Haus. Und wenn eine kleinere Anlage besser passt, sage ich Ihnen das "
                 "genauso offen. Wir sind danach erreichbar, weil wir hier wohnen."),
            ],
            quote="Wir verkaufen keine Module, wir bauen Unabhängigkeit. In Villach seit dem ersten Tag.",
            name=AUTHOR, role=AUTHOR_ROLE,
            badge="Gebürtiger Villacher",
            cta=("kontakt", "Beratungstermin in Villach"),
        ),
        C.facts_panel(
            eyebrow="Standort Villach",
            h2="So erreichen Sie EBZ Energie in Villach",
            intro=("Unser Firmensitz liegt in der Triglavstraße in Villach. Besuche nach Terminvereinbarung, "
                   "die Beratung findet meist direkt bei Ihnen vor Ort statt."),
            rows=[
                ("Adresse", f"{NAP['name']}<br>{NAP['street']}, {NAP['zip']} {NAP['city']}"),
                ("Telefon", tel_link()),
                ("E-Mail", f'<a href="mailto:{NAP["email"]}">{NAP["email"]}</a>'),
                ("Öffnungszeiten", NAP["hours"]),
                ("Anfahrt", "Nach Terminvereinbarung. Für die Erstberatung kommen wir in der Regel zu Ihnen nach Villach, Klagenfurt oder in die Umgebung."),
                ("Einzugsgebiet", "Villach und Umgebung, ganz Kärnten, Steiermark. Referenzen in 6 Bundesländern."),
            ],
            actions=[("Route planen", MAPS_URL, ' target="_blank" rel="noopener"'),
                     ("Anrufen", NAP["phone_href"], "")],
        ).replace('<section class="section"', '<section id="standort" class="section"', 1),
        C.regions_section(
            eyebrow="Einzugsgebiet",
            h2="Von Villach aus in ganz Kärnten und der Steiermark",
            intro=("Villach ist unser Zuhause, der Montageschwerpunkt liegt in Kärnten und der Steiermark. "
                   "Referenzprojekte gibt es darüber hinaus in ganz Österreich."),
            kaernten=KAERNTEN,
            steiermark=STEIERMARK,
            note="Referenzprojekte auch im Burgenland, in Niederösterreich, Oberösterreich und Wien.",
        ),
        C.reviews_slider(reviews, rating=rating, count=count),
        C.steps_section(
            eyebrow="So läuft es ab",
            h2="Von der Beratung in Villach bis zum eigenen Sonnenstrom",
            steps=[
                ("Beratung vor Ort", "Wir besprechen Verbrauch, Dach und Ziele bei Ihnen in Villach. Kostenlos und unverbindlich.", ""),
                ("Projektbericht", "Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport sowie ein transparentes Angebot.", ""),
                ("Förderung und Anmeldung", "Landespauschale Kärnten, Bundesförderung und Netzanmeldung: Wir bereiten alles vor.", ""),
                ("Montage und Übergabe", "Zertifizierte Fachkräfte montieren, wir kümmern uns um Zählertausch, Inbetriebnahme und Einschulung.", ""),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section(
            "Photovoltaik in Kärnten",
            [("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
             ("foerderung_kaernten", "PV-Förderung Kärnten 2026"),
             ("batteriespeicher", "Batteriespeicher"),
             ("/notstrom/", "Notstrom mit Photovoltaik"),
             ("/energiegemeinschaft-villach-klagenfurt/", "Energiegemeinschaft Villach und Klagenfurt"),
             ("pv_wolfsberg", "Photovoltaik Wolfsberg"),
             ("finanzierung", "Finanzierung"),
             ("referenzen", "Referenzen")],
        ),
        C.contact_section(
            headline="Ihr kostenloses Angebot für Photovoltaik in Villach",
            sub=("Sie erreichen uns telefonisch oder über das Formular. Wir zeigen Ihnen ehrlich, was auf Ihrem "
                 "Dach in Villach möglich ist und was es kostet. Kostenlos und unverbindlich."),
            page_label="Photovoltaik Villach",
        ),
        C.finalcta(
            "Bereit für Sonnenstrom vom eigenen Dach in Villach?",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags und "
            "kommen zu Ihnen vor Ort.",
        ),
        _footnote(),
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=HERO_IMG)
    return write_page("photovoltaik-villach/index.html", html)


def _footnote():
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte auf Basis typischer Projekte, vor Förderung. Preis, Ersparnis und
      Amortisation hängen von Verbrauch, Anlagengröße, Ausrichtung und Strompreis ab. Fördersätze Stand 2026,
      Änderungen durch die Fördergeber vorbehalten. Fachlich geprüft von Mario Zintl, Geschäftsführung
      EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    build()
