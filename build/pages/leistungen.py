"""Leistungsuebersicht (/leistungen/).

Uebersicht des EBZ-Systems: ein System, sechs Bausteine (wie auf der Startseite),
dazu Gewerbe, Carport und Finanzierung als weitere Einstiege. Quelle zur
Orientierung: Live-Seite /leistungen/ (bereinigt: keine alte Adresse, keine
Superlative, Projektbericht statt Ertragsberechnung). Kompakt: 900 bis 1.300 Woerter.
"""

from common import IMG, NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, write_page, load_reviews
from layout import page
import components as C

PATH = "/leistungen/"
TITLE = "Leistungen: Photovoltaik, Speicher, Wärmepumpe, EMS | EBZ"
DESC = ("Photovoltaik, Speicher, Wärmepumpe, Energiemanagement, Energiegemeinschaft und Balkonkraftwerk: "
        "das EBZ-System aus einer Hand, bis zu 85 % weniger Stromkosten.")

FAQ = [
    ("Welche Leistungen bietet EBZ Energie an?",
     "EBZ Energie plant und montiert komplette Energiesysteme: Photovoltaik, Batteriespeicher, Wärmepumpe, "
     "Energiemanagement, Energiegemeinschaft sowie Balkonkraftwerk und Wallbox. Dazu kommen Photovoltaik für "
     "Gewerbe, PV-Carports und eine Finanzierung mit Eigentum ab Tag 1."),
    ("Muss ich alle sechs Bausteine auf einmal umsetzen?",
     "Nein. Die meisten Kundinnen und Kunden starten mit Photovoltaik und Speicher. Wärmepumpe, Wallbox oder "
     "Energiemanagement lassen sich später ergänzen. Wir planen von Anfang an so, dass spätere Bausteine "
     "sauber dazupassen."),
    ("Was kostet eine Photovoltaikanlage mit Speicher?",
     "Eine Komplettanlage mit rund 10 kWp und Speicher liegt typischerweise bei rund 15.000 bis 22.000 € vor "
     "Förderung. Der genaue Preis hängt von Dach, Speichergröße und Ausstattung ab und steht im Projektbericht "
     "mit 3D-Belegplan und Statikreport."),
    ("Übernimmt EBZ die Förderabwicklung?",
     "Ja. Wir kennen die Programme von Bund und Ländern in Kärnten und der Steiermark, bereiten die Anträge vor "
     "und behalten Fristen und Reihenfolge im Blick, zum Beispiel die Registrierung vor der Rechnung bei der "
     "EMS-Förderung."),
    ("Wo montiert EBZ Energie?",
     "Der Montageschwerpunkt liegt in Kärnten und der Steiermark, von Villach über Klagenfurt bis Graz. "
     "Referenzprojekte gibt es in 6 Bundesländern, über 300 dokumentierte Anlagen."),
    ("Kann ich die Anlage finanzieren?",
     "Ja. Mit 0 € Anzahlung, fixer Rate und Eigentum ab dem ersten Tag, ab 147 € im Monat inklusive Speicher. "
     "Die Förderung bleibt in voller Höhe bei Ihnen. Mietmodelle bieten wir bewusst nicht an."),
    ("Welche Garantien bekomme ich?",
     "Auf die Module bis zu 30 Jahre Leistungsgarantie und mindestens 10 Jahre Produktgarantie. Montiert wird "
     "von zertifizierten Fachkräften, mit dachschonender Montage auf Ersatzziegeln statt geflexten Originalziegeln."),
]


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        C.page_hero(
            eyebrow="Unsere Leistungen · Kärnten und Steiermark",
            h1="Ein System, sechs Bausteine: alle Leistungen von EBZ Energie",
            lead=("Photovoltaik, Speicher, Wärmepumpe, Energiemanagement, Energiegemeinschaft und Balkonkraftwerk: "
                  "Wir planen Ihr Energiesystem als Ganzes und montieren es mit zertifizierten Fachkräften. "
                  "Ein Ansprechpartner, von der Beratung bis zum Service."),
            cta=("kontakt", "Kostenlose Beratung"),
            cta2=("referenzen", "Referenzen ansehen"),
        ),
        C.kpis([
            ("300+", "dokumentierte Projekte"),
            (NAP["rating"], "Sterne auf Google"),
            ("bis zu 85 %", "weniger Energiekosten"),
            ("6", "Bausteine aus einer Hand"),
        ]),
        C.text_block(
            eyebrow="Der EBZ Systemgedanke",
            h2="Wir denken in Systemen, nicht in Einzelteilen",
            paragraphs=[
                ("Module aufs Dach schrauben kann jeder. Der Unterschied liegt im Zusammenspiel: Eine "
                 "Photovoltaikanlage liefert den Strom, der Speicher hebt ihn in den Abend, die Wärmepumpe heizt "
                 "damit, die Wallbox lädt das Auto, das Energiemanagement steuert alles und die Energiegemeinschaft "
                 "verwertet, was übrig bleibt."),
                ("Deshalb planen wir jedes Projekt von Anfang an als System, auch wenn Sie mit einem Baustein "
                 "starten. So passt der nächste Schritt später dazu, ohne Umbau und ohne Schnittstellen-Chaos. "
                 "Das Ergebnis: bis zu 85 % weniger Energiekosten und eine Anlage, die sich typischerweise in "
                 "4 bis 6 Jahren rechnet."),
            ],
        ),
        C.cards_section(
            eyebrow="Die sechs Bausteine",
            h2="Alles, was Ihr Zuhause oder Ihren Betrieb zum Kraftwerk macht",
            intro=("Sie kombinieren, was zu Haus, Verbrauch und Budget passt. Jede Leistung hat eine eigene "
                   "Seite mit Zahlen, Ablauf und Förderung."),
            with_media=True,
            cards=[
                {"img": IMG["pv_card"], "alt": "Photovoltaikanlage auf einem Hausdach in Kärnten",
                 "title": "Photovoltaik",
                 "text": "Das Herzstück: Module, Wechselrichter und Montage, geplant für maximalen Eigenverbrauch. Bis zu 30 Jahre Leistungsgarantie, Richtpreis 10 kWp mit Speicher rund 15.000 bis 22.000 € vor Förderung.",
                 "link_key": "photovoltaik", "link_text": "Zur Photovoltaik"},
                {"img": IMG["speicher"], "alt": "Batteriespeicher im Technikraum",
                 "title": "Batteriespeicher",
                 "text": "Sonnenstrom am Abend und in der Nacht nutzen statt mittags einspeisen und abends zurückkaufen. Bis zu 80 % Eigenverbrauch, optional mit Notstrom bei Ausfall.",
                 "link_key": "batteriespeicher", "link_text": "Zum Speicher"},
                {"img": IMG["waermepumpe"], "alt": "Wärmepumpe an einer Hauswand",
                 "title": "Wärmepumpe",
                 "text": "Heizen und Warmwasser mit dem eigenen Sonnenstrom statt mit Gas oder Öl. SG-Ready, damit das Energiemanagement sie bei Sonnenschein laufen lässt.",
                 "link_key": "waermepumpe", "link_text": "Zur Wärmepumpe"},
                {"img": IMG["ems"], "alt": "Energiemanagementsystem vernetzt Photovoltaik, Speicher, Wärmepumpe und Wallbox",
                 "title": "Energiemanagement",
                 "text": "Die Steuerzentrale: hebt den Eigenverbrauch von rund 30 auf bis zu 80 %, nutzt dynamische Tarife und kappt im Gewerbe Lastspitzen. 2026 mit bis zu 600 € gefördert.",
                 "link_key": "ems", "link_text": "Zum Energiemanagement"},
                {"img": IMG["eg_drohne"], "alt": "Wohngebiet aus der Luft, Nachbarn teilen Sonnenstrom",
                 "title": "Energiegemeinschaft",
                 "text": "Überschuss mit Nachbarn oder Verwandten teilen statt verschenken. Österreichweit möglich, im Nahbereich mit bis zu 57 % Netzentgelt-Rabatt.",
                 "link_key": "eg_privat", "link_text": "Zur Energiegemeinschaft"},
                {"img": IMG["balkon"], "alt": "Balkonkraftwerk an einem Geländer",
                 "title": "Balkonkraftwerk und Wallbox",
                 "text": "Der Einstieg für Mieter und kleine Flächen, sturmsicher montiert. Dazu die Wallbox, die Ihr E-Auto bevorzugt mit PV-Überschuss lädt.",
                 "link_key": "balkonkraftwerke", "link_text": "Zum Balkonkraftwerk"},
                {"ic": "◎", "title": "Photovoltaik für Gewerbe",
                 "text": "Große Dächer, Planung nach Lastprofil, hoher Eigenverbrauch tagsüber. Beispiel Oberösterreich: 40 kWp, rund 13.500 € Ersparnis pro Jahr.",
                 "link_key": "pv_gewerbe", "link_text": "Photovoltaik für Gewerbe"},
                {"ic": "⌂", "title": "PV-Carport",
                 "text": "Stellplatz und Kraftwerk in einem: Das Carportdach erzeugt Strom, die Wallbox darunter lädt das Auto. Für Eigenheim und Firmenparkplatz.",
                 "link_key": "carport", "link_text": "Zum PV-Carport"},
                {"ic": "€", "title": "Finanzierung",
                 "text": "0 € Anzahlung, fixe Rate, Eigentum ab Tag 1 und volle Förderung. Komplettanlage inklusive Speicher ab 147 € im Monat*.",
                 "link_key": "finanzierung", "link_text": "Zur Finanzierung"},
            ],
        ),
        C.audience_split(
            eyebrow="Für wen planen wir?",
            h2="Eigenheim oder Betrieb: Das System passt sich an, nicht Sie",
            intro="Wählen Sie, was auf Sie zutrifft. Wir richten Planung, Größe und Wirtschaftlichkeit danach aus.",
            left={
                "img": IMG["gen_eigenheim"],
                "alt": "Einfamilienhaus mit Photovoltaikanlage in Kärnten",
                "title": "Für Ihr Eigenheim",
                "bullets": [
                    "Photovoltaik mit Speicher und Notstrom",
                    "Wärmepumpe und Wallbox mit Sonnenstrom betreiben",
                    "Energiemanagement und Energiegemeinschaft für den Rest",
                    "Volle Förderung, Finanzierung ab 147 € im Monat*",
                ],
                "cta": ("kontakt", "Beratung für mein Zuhause"),
            },
            right={
                "img": IMG["gen_gewerbe"],
                "alt": "Gewerbebetrieb mit großer Photovoltaikanlage am Dach",
                "title": "Für Ihren Betrieb",
                "bullets": [
                    "Große Dächer und Carports, Planung nach Lastprofil",
                    "Lastspitzen kappen, Netzentgelte und Leistungspreis senken",
                    "Energiedaten für ESG-Reporting und Energieaudits",
                    "Beispiel Gewerbe OÖ: 40 kWp, 13.500 € Ersparnis pro Jahr",
                ],
                "cta": ("pv_gewerbe", "Photovoltaik für Gewerbe"),
            },
        ),
        C.why_section(
            eyebrow="Darum EBZ",
            h2="Ihr Partner aus der Region, nicht irgendein Anbieter",
            items=[
                ("☀", "Ein Ansprechpartner für alles", "Beratung, Planung, Montage, Förderung und Anmeldung beim Netzbetreiber aus einer Hand."),
                ("⌂", "Regionale Nähe", "Zuhause in Villach, im Einsatz in Kärnten und der Steiermark. Wir kennen Netzbetreiber und Landesförderungen."),
                ("✓", "Zertifizierte Fachkräfte", "Festangestelltes Team, meisterhaftes Handwerk und dachschonende Montage mit Ersatzziegeln statt geflexten Originalziegeln."),
                ("◇", "Komponenten mit Garantie", "Führende Hersteller, bis zu 30 Jahre Leistungsgarantie und mindestens 10 Jahre Produktgarantie."),
                ("★", "4,9 Sterne auf Google", "Bewertungen von echten Kundinnen und Kunden aus der Region."),
                ("◎", "300+ Projekte", "Erfahrung aus über 300 dokumentierten Anlagen in 6 Bundesländern."),
            ],
        ),
        C.reviews_slider(reviews, rating, count),
        C.steps_section(
            eyebrow="Beratung. Planung. Umsetzung.",
            h2="Ihr Weg zur eigenen Energieversorgung in vier Schritten",
            steps=[
                ("Beratung und Besichtigung", "Wir beantworten Ihre Fragen, kommen vor Ort und erfassen Dach, Verbrauch und Ziele. Kostenlos und unverbindlich.", ""),
                ("Projektbericht", "Sie erhalten ein Fixangebot samt Projektbericht mit 3D-Belegplan und Statikreport, inklusive Wind- und Schneelasten.", ""),
                ("Förderung und Behörden", "Wir reichen die Förderungen ein, melden die Anlage beim Netzbetreiber an und behalten alle Fristen im Blick.", ""),
                ("Montage und Service", "Zertifizierte Fachkräfte montieren und nehmen in Betrieb. Danach bleiben wir Ihr Ansprechpartner, mit Monitoring auf Wunsch.", ""),
            ],
        ),
        C.faq_section(FAQ),
        C.contact_section(
            headline="Reden wir über Ihr Projekt",
            sub=("Beim Reden kommen die Leute zusammen. Wir besichtigen Ihr Projekt gerne unverbindlich vor Ort "
                 "und zeigen Ihnen, welche Bausteine sich für Sie rechnen."),
        ),
        C.finalcta(
            "Ihr Weg in die Unabhängigkeit beginnt jetzt",
            "Hören Sie auf, Ihren Strom teuer einzukaufen, wenn Sie ihn selbst produzieren können. "
            "Fordern Sie Ihre kostenlose Beratung an, wir melden uns innerhalb eines Werktags.",
        ),
        _footnote(),
    ])

    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ), og_image=IMG["hero_home"])
    return write_page("leistungen/index.html", html)


def _footnote():
    return (f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte auf Basis typischer Projekte, vor Förderung. Finanzierungsrate als
      Beispielkondition, abhängig von Anlagengröße und Laufzeit. Ersparnis und Amortisation hängen von
      Verbrauch, Anlagengröße, Ausrichtung und Strompreis ab. Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import theme
    theme.write_assets()
    build()
