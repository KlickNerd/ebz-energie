"""Startseite der EBZ-Website.

EBZ ist ein System-Anbieter, nicht nur Photovoltaik: die Startseite zeigt das
komplette 6-Bausteine-System (PV, Speicher, Waermepumpe, Energiemanagement,
Energiegemeinschaft, Balkonkraftwerk und Wallbox), den Systemgedanken,
Foerderung, Referenzen mit Zahlen und das Einzugsgebiet.

Struktur orientiert sich an der freigegebenen Playground-Startseite, haelt sich
aber an die verbindlichen Fakten (85 % statt 90 %, 4,9 statt 5,0, Finanzierung
statt Leasing, Projektbericht statt Ertragsprognose).
"""

from common import CLAIMS, NAP, IMG, faq_jsonld, u, write_page, load_reviews
from layout import page
import components as C

PATH = "/"
TITLE = "Photovoltaik, Speicher & Wärmepumpe | EBZ Energie Kärnten"
DESC = ("EBZ Energie macht Ihr Zuhause zum Kraftwerk: Photovoltaik, Speicher, Wärmepumpe, "
        "Energiemanagement und Energiegemeinschaft aus einer Hand in Kärnten und der Steiermark. "
        "Bis zu 85 % weniger Stromkosten, 4,9 Sterne, 300+ Projekte.")


def build():
    _rating, _count, _reviews = load_reviews()
    body = "".join([
        C.hero(
            eyebrow="Photovoltaik · Speicher · Wärmepumpe · Kärnten und Steiermark",
            h1="Machen Sie Ihr Zuhause zum Kraftwerk. Aus einer Hand, aus der Region.",
            lead=("EBZ Energie plant und installiert Ihr komplettes Energiesystem: Photovoltaik, "
                  "Speicher, Wärmepumpe, Energiemanagement und Energiegemeinschaft. So senken Sie "
                  "Ihre Energiekosten um bis zu 85 % und werden unabhängiger von steigenden Preisen."),
            badges=[("4,9", "Sterne auf Google"),
                    ("300+", "Projekte"),
                    ("6", "Bausteine aus einer Hand")],
            img=IMG["hero_home"],
            img_alt="Photovoltaikanlage von EBZ Energie auf einem Wohnhaus in Villach",
            float_num="300+",
            float_label="Anlagen in 6 Bundesländern",
        ),
        C.kpis([
            ("300+", "dokumentierte Projekte"),
            (NAP["rating"], "Google Bewertung"),
            ("bis zu 85 %", "weniger Energiekosten"),
            ("4 bis 6 Jahre", "typische Amortisation"),
        ]),
        C.cards_section(
            eyebrow="Unsere Leistungen",
            h2="Alles, was Ihr Zuhause zum Kraftwerk macht",
            intro=("Sechs Bausteine, ein System, ein Ansprechpartner. Sie kombinieren genau das, "
                   "was zu Ihrem Haus und Ihrem Verbrauch passt."),
            with_media=True,
            cards=[
                {"img": IMG["pv_card"], "alt": "Photovoltaikanlage auf einem Hausdach",
                 "title": "Photovoltaik", "text": "Hochleistungsmodule mit bis zu 30 Jahren Leistungsgarantie, geplant für maximalen Eigenverbrauch.",
                 "link_key": "photovoltaik", "link_text": "Photovoltaik"},
                {"img": IMG["speicher"], "alt": "Batteriespeicher im Technikraum",
                 "title": "Batteriespeicher", "text": "Bis zu 80 % Eigenverbrauch: Sonnenstrom am Abend nutzen und mit Notstrom vorbereitet sein.",
                 "link_key": "batteriespeicher", "link_text": "Speicher"},
                {"img": IMG["waermepumpe"], "alt": "Wärmepumpe an einer Hauswand",
                 "title": "Wärmepumpe", "text": "Effizient heizen mit dem eigenen Sonnenstrom statt mit teurem Gas oder Öl.",
                 "link_key": "waermepumpe", "link_text": "Wärmepumpe"},
                {"img": IMG["ems"], "alt": "Energiemanagementsystem Visualisierung",
                 "title": "Energiemanagement", "text": "Ein System steuert Anlage, Speicher, Wärmepumpe und Wallbox automatisch.",
                 "link_key": "ems", "link_text": "Energiemanagement"},
                {"img": IMG["eg_drohne"], "alt": "Wohngebiet aus der Luft",
                 "title": "Energiegemeinschaft", "text": "Strom mit Nachbarn oder Verwandten teilen und beim Netzentgelt sparen. Österreichweit möglich.",
                 "link_key": "eg_privat", "link_text": "Energiegemeinschaft"},
                {"img": IMG["balkon"], "alt": "Balkonkraftwerk an einem Geländer",
                 "title": "Balkonkraftwerk und Wallbox", "text": "Der einfache Einstieg für Mieter und die Ladelösung für Ihr E-Auto.",
                 "link_key": "balkonkraftwerke", "link_text": "Balkonkraftwerk"},
            ],
        ),
        C.hub_section(
            eyebrow="Der EBZ Systemgedanke",
            h2="Wir denken in Systemen, nicht in Einzelteilen",
            lead=("Module aufs Dach schrauben kann jeder. Wir planen Ihre Erzeugung, Speicherung, "
                  "Wärme und Mobilität als ein System, das sauber ineinandergreift. So holen Sie "
                  "das Maximum aus jedem Baustein."),
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
            h2="Weniger zukaufen, mehr Unabhängigkeit",
            intro=("Je mehr Strom und Wärme Sie selbst erzeugen, speichern und nutzen, desto weniger "
                   "müssen Sie teuer dazukaufen. Genau dafür sorgt das EBZ System."),
            bars=[
                ("Energiekosten ohne eigenes System", 100, "bad", "voller Zukauf"),
                ("Energiekosten mit dem EBZ System", 15, "good", "bis zu 85 % weniger*"),
            ],
            aside=("So entsteht Ihre Unabhängigkeit", [
                ("☀", "Selbst erzeugen", "Photovoltaik liefert Ihren Strom direkt vom Dach."),
                ("▮", "Selbst speichern", "Der Speicher macht Sonnenstrom auch am Abend nutzbar."),
                ("♨", "Selbst heizen", "Die Wärmepumpe heizt mit Ihrem eigenen Strom."),
                ("⚙", "Automatisch steuern", "Das Energiemanagement holt das Maximum heraus."),
            ]),
        ),
        C.steps_section(
            eyebrow="So einfach geht es",
            h2="In vier Schritten zur eigenen Energieversorgung",
            steps=[
                ("Beratung", "Wir analysieren Verbrauch, Dach und Ziele. Kostenlos und unverbindlich.", ""),
                ("Planung mit 3D", "Sie erhalten ein Fixangebot samt Projektbericht mit 3D-Belegplan und Statikreport.", ""),
                ("Förderung und Behörden", "EBZ Energie übernimmt Förderanträge, Anmeldung und Behördenwege.", ""),
                ("Montage", "Zertifizierte Fachkräfte montieren und nehmen Ihre Anlage in Betrieb.", ""),
            ],
        ),
        C.media_text(
            eyebrow="Förderung 2026",
            h2="Wir holen jede Förderung heraus, die Ihnen zusteht",
            paragraphs=[
                ("Photovoltaik, Speicher und Wärmepumpe werden in Österreich gefördert: über "
                 "Bundesmittel und über Landesförderungen in Kärnten und der Steiermark. EBZ Energie "
                 "kennt die aktuellen Programme und kümmert sich um die Anträge."),
                ("So sichern Sie sich alle Förderungen, die Ihnen zustehen, und verkürzen die Zeit, "
                 "bis sich Ihr System rechnet."),
            ],
            img=IMG["foerderung"],
            alt="Beratung zur Photovoltaik Förderung am Tisch",
            bullets=[
                "Bundesförderung für Photovoltaik, Speicher und Wärmepumpe",
                "Landesförderungen in Kärnten und der Steiermark",
                "Komplette Abwicklung durch EBZ Energie",
            ],
            cta=("foerderung_at", "Förderungen im Überblick"),
            reverse=True,
        ),
        C.reference_cards(
            eyebrow="Aus der Praxis",
            h2="Anlagen, die sich rechnen. Mit Zahlen belegt.",
            intro=("Über 300 dokumentierte Projekte in 6 Bundesländern. Ein paar Beispiele, bei denen "
                   "sich der Umstieg deutlich bezahlt macht."),
            items=[
                {"img": IMG["gewerbe_dach"], "alt": "Gewerbe-Photovoltaikanlage auf einem Trapezblechdach in Oberösterreich",
                 "title": "Gewerbe, Oberösterreich", "specs": "40 kWp Ost-West, 40 kWh Speicher, rund 40.000 kWh im Jahr.",
                 "result": "13.500 €", "result_sub": "Ersparnis pro Jahr"},
                {"img": IMG["ref_villach"], "alt": "Photovoltaikanlage auf einem Einfamilienhaus in Villach",
                 "title": "Einfamilienhaus, Villach", "specs": "10 kWp Ost-West mit Notstrom, rund 11.000 kWh im Jahr.",
                 "result": "rund 80 %", "result_sub": "weniger Stromkosten"},
                {"img": IMG["ref_krumpendorf"], "alt": "Photovoltaikanlage auf einem Mehrparteienhaus in Krumpendorf",
                 "title": "Mehrparteienhaus, Krumpendorf", "specs": "25 kWp mit 25 kWh Speicher und Notstrom.",
                 "result": "4 Tage", "result_sub": "Bauzeit"},
            ],
        ),
        C.finance_band(),
        C.why_section(
            eyebrow="Warum EBZ Energie",
            h2="Ihr Nachbar, nicht irgendein Anbieter",
            items=[
                ("☀", "Alles aus einer Hand", "Planung, Montage, Förderung und Service. Ein Ansprechpartner für Ihr ganzes System."),
                ("✓", "Zertifizierte Fachkräfte", "Meisterhaftes Handwerk und sorgfältige Ausführung bei jedem Projekt."),
                ("★", "4,9 Sterne auf Google", "Bewertungen von echten Kundinnen und Kunden aus der Region."),
                ("◉", "300+ Projekte", "Erfahrung aus über 300 dokumentierten Anlagen in 6 Bundesländern."),
                ("€", "Faire Finanzierung", "Ihre Anlage gehört Ihnen ab Tag 1. Ab 147 € im Monat inklusive Speicher."),
                ("⌂", "Regional verwurzelt", "Zuhause in Villach, im Einsatz für Kärnten und die Steiermark."),
            ],
        ),
        C.reviews_slider(_reviews, rating=_rating, count=_count),
        C.founder_block(
            "Wir verkaufen keine Module, wir bauen Unabhängigkeit. Jedes System planen wir so, dass "
            "es zu Ihrem Dach, Ihrem Verbrauch und Ihrem Budget passt. Das ist unser Anspruch bei jedem Projekt."
        ),
        C.regions_section(
            eyebrow="Unser Einzugsgebiet",
            h2="Vor Ort in Kärnten und der Steiermark",
            intro=("Der Montageschwerpunkt liegt in Kärnten und der Steiermark. Referenzprojekte "
                   "gibt es darüber hinaus in ganz Österreich."),
            kaernten=["Villach", "Klagenfurt", "Spittal an der Drau", "Feldkirchen",
                      "St. Veit an der Glan", "Wolfsberg", "Völkermarkt", "Hermagor"],
            steiermark=["Graz", "Leibnitz", "Deutschlandsberg", "Voitsberg",
                        "Weiz", "Murtal", "Leoben", "Südoststeiermark"],
            note="Referenzprojekte auch im Burgenland, in Niederösterreich, Oberösterreich und Wien.",
        ),
        C.linkgrid_section(
            "Beliebte Seiten",
            [("photovoltaik", "Photovoltaik"),
             ("waermepumpe", "Wärmepumpe"),
             ("batteriespeicher", "Batteriespeicher"),
             ("eg_privat", "Energiegemeinschaft"),
             ("pv_villach", "Photovoltaik Villach"),
             ("foerderung_kaernten", "Förderung Kärnten"),
             ("foerderung_steiermark", "Förderung Steiermark"),
             ("referenzen", "Referenzen")],
        ),
        C.contact_section(
            headline="Sind Sie bereit, Ihre Stromrechnung selbst zu schreiben?",
            sub=("Sie erreichen uns telefonisch oder über das Formular. Wir beraten Sie ehrlich "
                 "und zeigen Ihnen, was auf Ihrem Dach möglich ist."),
        ),
        C.faq_section([
            ("In welchen Regionen ist EBZ Energie tätig?",
             "Der Montageschwerpunkt liegt in Kärnten und der Steiermark, von Villach über Klagenfurt bis Graz. Referenzprojekte gibt es in 6 Bundesländern."),
            ("Was kostet eine Photovoltaikanlage mit Speicher?",
             "Eine Komplettanlage mit rund 10 kWp und Speicher liegt typischerweise bei rund 15.000 bis 22.000 € vor Förderung. Der genaue Preis hängt von Dach, Speichergröße und Ausstattung ab."),
            ("Lohnt sich die Kombination aus Photovoltaik und Wärmepumpe?",
             "Ja. Die Wärmepumpe heizt mit Ihrem eigenen Sonnenstrom, statt teures Gas oder Öl zu kaufen. In Kombination mit Speicher und Energiemanagement steigt Ihr Eigenverbrauch deutlich."),
            ("Was bringt mir eine Energiegemeinschaft?",
             "Sie teilen Ihren Strom mit Nachbarn oder Verwandten, statt ihn günstig einzuspeisen. Im Nahbereich sparen Sie zusätzlich beim Netzentgelt. Österreichweites Teilen ist ebenfalls möglich."),
            ("Übernimmt EBZ die Förderabwicklung komplett?",
             "Ja. EBZ Energie kümmert sich um die passenden Bundes- und Landesförderungen sowie um Anmeldung und Behördenwege."),
            ("Welche Garantien bekomme ich?",
             "Auf die Module gibt es bis zu 30 Jahre Leistungsgarantie und mindestens 10 Jahre Produktgarantie."),
            ("Kann ich die Anlage finanzieren?",
             "Ja, mit einer fairen Finanzierung ab 147 € im Monat inklusive Speicher. Die Anlage gehört Ihnen ab dem ersten Tag, mit voller Förderung für Privatpersonen."),
        ]),
        C.finalcta(
            "Jetzt starten: Ihr eigenes Energiesystem",
            "Fordern Sie Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags.",
        ),
        _footnote(),
    ])

    faq = faq_jsonld(u(PATH), [
        ("In welchen Regionen ist EBZ Energie taetig?",
         "Montageschwerpunkt in Kaernten und der Steiermark, Referenzprojekte in 6 Bundeslaendern."),
        ("Was kostet eine Photovoltaikanlage mit Speicher?",
         "Eine Komplettanlage mit rund 10 kWp und Speicher liegt typischerweise bei rund 15.000 bis 22.000 Euro vor Foerderung."),
        ("Lohnt sich die Kombination aus Photovoltaik und Waermepumpe?",
         "Ja, die Waermepumpe heizt mit dem eigenen Sonnenstrom. Mit Speicher und Energiemanagement steigt der Eigenverbrauch deutlich."),
        ("Was bringt mir eine Energiegemeinschaft?",
         "Sie teilen Strom mit Nachbarn oder Verwandten statt guenstig einzuspeisen und sparen im Nahbereich beim Netzentgelt."),
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
      und Amortisation hängen von Verbrauch, Anlagengröße, Ausrichtung und Strompreis ab.
      Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    build()
