"""Startseite der EBZ-Website."""

from common import CLAIMS, NAP, IMG, faq_jsonld, u, write_page
from layout import page
import components as C

PATH = "/"
TITLE = "Photovoltaik aus Villach | EBZ Energie GmbH"
DESC = ("Photovoltaik, Speicher und Wärmepumpe vom Fachbetrieb aus Villach. "
        "Planung, Montage und Service aus einer Hand für Kärnten und die Steiermark. "
        "4,9 Sterne, 300+ Projekte, bis zu 85 % weniger Stromkosten.")


def build():
    body = "".join([
        C.hero(
            eyebrow="Ihr Photovoltaik-Fachbetrieb in Kärnten und der Steiermark",
            h1="Eigener Sonnenstrom vom Dach. Geplant, montiert und betreut aus einer Hand.",
            lead=("EBZ Energie plant und installiert Photovoltaikanlagen, Batteriespeicher und "
                  "Wärmepumpen. So senken Sie Ihre Stromkosten um bis zu 85 % und machen sich "
                  "unabhängig von steigenden Preisen."),
            badges=[("4,9", "Sterne auf Google"),
                    ("300+", "Projekte"),
                    ("bis zu 30 Jahre", "Leistungsgarantie")],
            img=IMG["hero_home"],
            img_alt="Photovoltaikanlage von EBZ Energie auf einem Wohnhaus in Villach",
            float_num="300+",
            float_label="Anlagen in 6 Bundesländern",
        ),
        C.kpis([
            ("300+", "dokumentierte Projekte"),
            (NAP["rating"], "Google Bewertung"),
            ("bis zu 85 %", "weniger Stromkosten"),
            ("4 bis 6 Jahre", "typische Amortisation"),
        ]),
        C.cards_section(
            eyebrow="Leistungen",
            h2="Alles für Ihre Energiewende, aus einer Hand",
            intro=("Von der Photovoltaikanlage über den Speicher bis zur Wärmepumpe: "
                   "EBZ Energie begleitet Sie von der ersten Beratung bis zum laufenden Service."),
            with_media=True,
            cards=[
                {"img": IMG["pv_card"], "alt": "Photovoltaikanlage auf einem Hausdach",
                 "title": "Photovoltaik", "text": "Passgenaue Anlagen für Eigenheim und Gewerbe, geplant für maximalen Eigenverbrauch.",
                 "link_key": "photovoltaik", "link_text": "Photovoltaik"},
                {"img": IMG["speicher"], "alt": "Batteriespeicher im Technikraum",
                 "title": "Batteriespeicher", "text": "Sonnenstrom auch abends nutzen und mit Notstrom auf Stromausfälle vorbereitet sein.",
                 "link_key": "batteriespeicher", "link_text": "Speicher"},
                {"img": IMG["waermepumpe"], "alt": "Wärmepumpe an einer Hauswand",
                 "title": "Wärmepumpe", "text": "Effizient heizen mit dem eigenen Sonnenstrom. Ideal in Kombination mit Ihrer Anlage.",
                 "link_key": "waermepumpe", "link_text": "Wärmepumpe"},
                {"img": IMG["balkon"], "alt": "Balkonkraftwerk an einem Geländer",
                 "title": "Balkonkraftwerke", "text": "Der einfache Einstieg in die eigene Stromerzeugung, auch für Mietwohnungen.",
                 "link_key": "balkonkraftwerke", "link_text": "Balkonkraftwerk"},
                {"img": IMG["ems"], "alt": "Energiemanagementsystem Visualisierung",
                 "title": "Energiemanagement", "text": "Ein System steuert Anlage, Speicher, Wärmepumpe und Wallbox für maximalen Eigenverbrauch.",
                 "link_key": "ems", "link_text": "Energiemanagement"},
                {"img": IMG["eg_drohne"], "alt": "Wohngebiet aus der Luft",
                 "title": "Energiegemeinschaft", "text": "Strom mit Nachbarn oder Verwandten teilen und beim Netzentgelt sparen. Österreichweit möglich.",
                 "link_key": "eg_privat", "link_text": "Energiegemeinschaft"},
            ],
        ),
        C.hub_section(
            eyebrow="Alles aus einer Hand",
            h2="Ein Ansprechpartner für Ihre gesamte Energieversorgung",
            lead=("Sie brauchen keine fünf verschiedenen Firmen. EBZ Energie plant Ihr System als "
                  "Ganzes: Erzeugung, Speicherung, Wärme und Mobilität greifen sauber ineinander."),
            points=[
                ("☀", "Photovoltaik, die zu Dach, Verbrauch und Budget passt."),
                ("▮", "Speicher für Abendstunden und Notstrom bei Ausfall."),
                ("♨", "Wärmepumpe, die mit Ihrem Sonnenstrom heizt."),
                ("⚙", "Energiemanagement, das alle Komponenten steuert."),
                ("✓", "Montage durch zertifizierte Fachkräfte, meisterhaftes Handwerk."),
            ],
        ),
        C.problem_compare(
            eyebrow="Warum sich der Umstieg lohnt",
            h2="Weniger Netzbezug, mehr Unabhängigkeit",
            intro=("Der größte Teil Ihres Sonnenstroms wird direkt im Haus verbraucht. "
                   "Was Sie selbst nutzen, müssen Sie nicht teuer aus dem Netz kaufen."),
            bars=[
                ("Stromkosten ohne eigene Anlage", 100, "bad", "voller Netzbezug"),
                ("Stromkosten mit Photovoltaik und Speicher", 20, "good", "bis zu 85 % weniger*"),
            ],
        ),
        C.finance_band(),
        C.steps_section(
            eyebrow="So einfach läuft es ab",
            h2="Von der Beratung bis zum eigenen Sonnenstrom",
            steps=[
                ("Beratung", "Wir besprechen Ihren Verbrauch, Ihr Dach und Ihre Ziele. Kostenlos und unverbindlich.", "Tag 1"),
                ("Projektbericht", "Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport.", "wenige Tage"),
                ("Montage", "Zertifizierte Fachkräfte montieren Ihre Anlage sauber und termintreu.", "1 bis 4 Tage"),
                ("Inbetriebnahme", "Wir kümmern uns um Anmeldung, Zählertausch und Übergabe.", "danach"),
            ],
        ),
        C.why_section(
            eyebrow="Warum EBZ Energie",
            h2="Ein Fachbetrieb, auf den Sie sich verlassen können",
            items=[
                ("☀", "Alles aus einer Hand", "Planung, Montage, Anmeldung und Service. Ein Ansprechpartner für alles."),
                ("✓", "Zertifizierte Fachkräfte", "Meisterhaftes Handwerk und sorgfältige Ausführung bei jedem Projekt."),
                ("★", "4,9 Sterne auf Google", "Bewertungen von echten Kundinnen und Kunden aus der Region."),
                ("◉", "300+ Projekte", "Erfahrung aus über 300 dokumentierten Anlagen in 6 Bundesländern."),
                ("€", "Faire Finanzierung", "Ihre Anlage gehört Ihnen ab Tag 1. Ab 147 € im Monat inklusive Speicher."),
                ("⌂", "Regional verwurzelt", "Zuhause in Villach, im Einsatz für Kärnten und die Steiermark."),
            ],
        ),
        C.reviews_block([
            ("Von der Beratung bis zur Inbetriebnahme alles reibungslos. Das Team war pünktlich, sauber und kompetent.", "Familie aus Villach"),
            ("Ehrliche Beratung ohne Verkaufsdruck. Die Anlage läuft seit Monaten einwandfrei und die Ersparnis ist deutlich spürbar.", "Kunde aus Klagenfurt"),
            ("Top Handwerk und ein echter Ansprechpartner bei Fragen. Jederzeit wieder.", "Kundin aus der Steiermark"),
        ]),
        C.founder_block(
            "Wir liefern keine Anlage von der Stange. Wir planen jedes System so, dass es zu Ihrem "
            "Dach, Ihrem Verbrauch und Ihrem Budget passt. Das ist unser Anspruch bei jedem Projekt."
        ),
        C.contact_section(
            headline="Lassen Sie uns Ihr Projekt besprechen",
            sub=("Sie erreichen uns telefonisch oder über das Formular. Wir beraten Sie ehrlich "
                 "und zeigen Ihnen, was auf Ihrem Dach möglich ist."),
        ),
        C.faq_section([
            ("Was kostet eine Photovoltaikanlage mit Speicher?",
             "Eine Komplettanlage mit rund 10 kWp und Speicher liegt typischerweise bei rund 15.000 bis 22.000 € vor Förderung. Der genaue Preis hängt von Dach, Speichergröße und Ausstattung ab."),
            ("Wie lange dauert die Amortisation?",
             "In der Praxis rechnen sich Anlagen von EBZ Energie meist innerhalb von 4 bis 6 Jahren, je nach Eigenverbrauch, Anlagengröße und Strompreis."),
            ("In welchen Regionen ist EBZ Energie tätig?",
             "Der Montageschwerpunkt liegt in Kärnten und der Steiermark. Referenzprojekte gibt es in 6 Bundesländern."),
            ("Bekomme ich alles aus einer Hand?",
             "Ja. EBZ Energie übernimmt Beratung, Planung, Montage durch zertifizierte Fachkräfte, Anmeldung und Service."),
            ("Kann ich die Anlage finanzieren?",
             "Ja, mit einer fairen Finanzierung ab 147 € im Monat inklusive Speicher. Die Anlage gehört Ihnen ab dem ersten Tag, mit voller Förderung für Privatpersonen."),
        ]),
        C.linkgrid_section(
            "Beliebte Seiten",
            [("pv_villach", "Photovoltaik Villach"),
             ("pv_wolfsberg", "Photovoltaik Wolfsberg"),
             ("foerderung_kaernten", "Förderung Kärnten"),
             ("foerderung_steiermark", "Förderung Steiermark"),
             ("batteriespeicher", "Batteriespeicher"),
             ("waermepumpe", "Wärmepumpe"),
             ("eg_privat", "Energiegemeinschaft"),
             ("referenzen", "Referenzen")],
        ),
        C.finalcta(
            "Bereit für Ihren eigenen Sonnenstrom?",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags.",
        ),
        _footnote(),
    ])

    faq = faq_jsonld(u(PATH), [
        ("Was kostet eine Photovoltaikanlage mit Speicher?",
         "Eine Komplettanlage mit rund 10 kWp und Speicher liegt typischerweise bei rund 15.000 bis 22.000 Euro vor Foerderung."),
        ("Wie lange dauert die Amortisation?",
         "Meist innerhalb von 4 bis 6 Jahren, je nach Eigenverbrauch, Anlagengroesse und Strompreis."),
        ("In welchen Regionen ist EBZ Energie taetig?",
         "Montageschwerpunkt in Kaernten und der Steiermark, Referenzprojekte in 6 Bundeslaendern."),
        ("Kann ich die Anlage finanzieren?",
         "Ja, ab 147 Euro im Monat inklusive Speicher. Die Anlage gehoert Ihnen ab dem ersten Tag."),
    ])

    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq, include_business_schema=True)
    return write_page("index.html", html)


def _footnote():
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte auf Basis typischer Projekte. Die tatsächliche Ersparnis
      und Amortisation hängen von Verbrauch, Anlagengröße, Ausrichtung und Strompreis ab.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    build()
