"""Startseite der EBZ-Website.

EBZ ist ein System-Anbieter, nicht nur Photovoltaik: die Startseite zeigt das
komplette 6-Bausteine-System (PV, Speicher, Waermepumpe, Energiemanagement,
Energiegemeinschaft, Balkonkraftwerk und Wallbox), den Systemgedanken,
Foerderung, Referenzen mit Zahlen und das Einzugsgebiet.

SEO-Rolle (Briefing build/seo/home.json, Oktober 2026): Die Startseite traegt das
regionale Kopf-Keyword "Photovoltaik Kaernten" plus Marke; die Produktbegriffe
gehoeren auf /photovoltaik/. Foerderzahlen 2026 und Netzanmeldung (Kaernten Netz)
stehen kurz und datiert auf der Seite, Details in den Ratgebern.

Struktur orientiert sich an der freigegebenen Playground-Startseite, haelt sich
aber an die verbindlichen Fakten (85 % statt 90 %, 4,9 statt 5,0, Finanzierung
statt Leasing, Projektbericht statt Ertragsprognose).
"""

from common import CLAIMS, NAP, IMG, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

PATH = "/"
TITLE = "Photovoltaik Kärnten: EBZ Energie, Fachbetrieb Villach"
DESC = ("EBZ Energie, Villach: Photovoltaik, Speicher, Wärmepumpe und Energiegemeinschaft aus einer "
        "Hand in Kärnten und der Steiermark. 300+ Projekte, 4,9 Sterne.")

FAQ = [
    ("Was kostet eine Photovoltaikanlage für ein Einfamilienhaus in Kärnten?",
     "Eine Komplettanlage mit rund 10 kWp und Speicher liegt in Kärnten typischerweise bei rund 15.000 bis "
     "22.000 € vor Förderung (EBZ-Richtpreis, Stand Oktober 2026). Davon gehen bis zu 3.000 € Landespauschale "
     "Kärnten und der EAG-Zuschuss des Bundes ab. Der genaue Preis hängt von Dach, Speichergröße und Ausstattung ab."),
    ("Welche Förderung gibt es 2026 für Photovoltaik in Kärnten?",
     "Das Land Kärnten zahlt für neue private PV-Anlagen ab 5 kWp mit mindestens 5 kWh Speicher pauschal 3.000 €, "
     "für die Speicher-Nachrüstung 1.000 €. Einreichung vom 12. Oktober bis 31. Dezember 2026 über die "
     "Förderplattform des Landes. Der EAG-Investitionszuschuss des Bundes beträgt 150 € je kWp bis 10 kWp und "
     "150 € je kWh Speicher; der letzte Fördercall 2026 läuft bis 22. Oktober. EBZ Energie übernimmt die Anträge."),
    ("Was ändert sich 2026 bei Photovoltaik in Österreich?",
     "Drei Punkte: Der EAG-Fördercall Oktober 2026 (8. bis 22. Oktober) ist der letzte im bisherigen System; ab 2027 ist "
     "laut BMWET eine Systemförderung für Speicher und intelligente Steuerung geplant, beantragt nach der "
     "Installation. Der OeMAG-Marktpreis für eingespeisten Strom lag im September 2026 bei 10,168 ct je kWh "
     "(Juli: 6,146 ct), er schwankt monatlich. Und seit Oktober 2026 gilt das neue Elektrizitätswirtschaftsgesetz (ElWG)."),
    ("Wie läuft die Netzanmeldung bei Kärnten Netz?",
     "In den meisten Gemeinden Kärntens ist die Kärnten Netz GmbH (eine Tochter der Kelag) der Netzbetreiber, in der Stadt Klagenfurt die "
     "Energie Klagenfurt. EBZ Energie meldet Ihre Anlage mit den Daten aus dem Projektbericht an, der Netzbetreiber "
     "prüft die Einspeiseleistung, danach folgen Zählertausch, Inbetriebnahme und Fertigstellungsmeldung. Sie "
     "müssen sich um nichts kümmern."),
    ("Lohnt sich Photovoltaik in Kärnten auch im Winter?",
     "Ja. Kärnten zählt mit über 1.900 Sonnenstunden zu den sonnenreichsten Regionen Österreichs, der Jahresertrag "
     "liegt bei rund 1.000 bis 1.100 kWh je kWp. Im Winterhalbjahr liefert eine Anlage typischerweise 25 bis "
     "30 Prozent des Jahresertrags; Module arbeiten bei Kälte sogar effizienter als bei Hitze."),
    ("Woran erkenne ich den richtigen Photovoltaik-Fachbetrieb in Kärnten?",
     "An zertifizierten Fachkräften für Montage und Elektrotechnik, an einem Projektbericht mit 3D-Belegplan und Statikreport "
     "statt einem Pauschalangebot, an schriftlichen Garantien (bis zu 30 Jahre Leistungs-, mindestens 10 Jahre "
     "Produktgarantie), an dokumentierten Referenzen mit Zahlen und an echten Google-Bewertungen. EBZ Energie: "
     "300+ Projekte, 4,9 Sterne."),
    ("In welchen Regionen ist EBZ Energie tätig?",
     "Der Montageschwerpunkt liegt in Kärnten und der Steiermark, von Villach über Klagenfurt, Spittal und "
     "Wolfsberg bis Graz. Referenzprojekte gibt es in 6 Bundesländern."),
    ("Was bringt mir eine Energiegemeinschaft?",
     "Sie teilen Ihren Strom mit Nachbarn oder Verwandten, statt ihn günstig einzuspeisen. Im Nahbereich sparen Sie "
     "zusätzlich beim Netzentgelt. Österreichweites Teilen ist ebenfalls möglich, dann ohne Netzentgelt-Rabatt."),
    ("Kann ich die Anlage finanzieren?",
     "Ja, mit einer fairen Finanzierung ab 147 € im Monat inklusive Speicher*. Die Anlage gehört Ihnen ab dem "
     "ersten Tag, mit voller Förderung für Privatpersonen, 0 € Anzahlung und fixer Rate."),
]


def build():
    _rating, _count, _reviews = load_reviews()
    bewertungen = f"{_count} Bewertungen" if _count else "echten Bewertungen"
    body = "".join([
        C.hero(
            eyebrow="Photovoltaik Kärnten und Steiermark · Fachbetrieb aus Villach",
            h1="Photovoltaik in Kärnten und der Steiermark: Ihr Fachbetrieb für Anlage, Speicher und Wärmepumpe aus einer Hand",
            lead=("EBZ Energie plant und montiert Ihre PV-Anlage in Kärnten und der Steiermark als komplettes "
                  "Energiesystem: Photovoltaik, Speicher, Wärmepumpe, Energiemanagement und Energiegemeinschaft. "
                  "So senken Sie Ihre Energiekosten um bis zu 85 % und werden unabhängiger von steigenden Preisen."),
            badges=[("4,9", "Sterne auf Google"),
                    ("300+", "Projekte"),
                    ("6", "Bausteine aus einer Hand")],
            img=IMG["hero_home"],
            img_alt="Photovoltaikanlage von EBZ Energie auf einem Wohnhaus in Villach, Kärnten",
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
            intro=("Sechs Bausteine, ein Komplettanbieter, ein Ansprechpartner. Sie kombinieren genau das, "
                   "was zu Ihrem Haus und Ihrem Verbrauch passt."),
            with_media=True,
            cards=[
                {"img": IMG["pv_card"], "alt": "Photovoltaikanlage auf einem Hausdach in Kärnten",
                 "title": "Photovoltaik", "text": "Hochleistungsmodule mit bis zu 30 Jahren Leistungsgarantie, geplant für maximalen Eigenverbrauch.",
                 "link_key": "photovoltaik", "link_text": "Photovoltaikanlage mit Speicher"},
                {"img": IMG["speicher"], "alt": "Batteriespeicher im Technikraum",
                 "title": "Batteriespeicher", "text": "Bis zu 80 % Eigenverbrauch: Sonnenstrom am Abend nutzen und mit Notstrom vorbereitet sein.",
                 "link_key": "batteriespeicher", "link_text": "Speicher"},
                {"img": IMG["waermepumpe"], "alt": "Wärmepumpe an einer Hauswand",
                 "title": "Wärmepumpe", "text": "Effizient heizen mit dem eigenen Sonnenstrom statt mit teurem Gas oder Öl.",
                 "link_key": "waermepumpe", "link_text": "Wärmepumpe"},
                {"img": IMG["ems"], "alt": "Energiemanagementsystem Visualisierung",
                 "title": "Energiemanagement", "text": "Ein System steuert Anlage, Speicher, Wärmepumpe und Wallbox automatisch, mit Monitoring per App.",
                 "link_key": "ems", "link_text": "Energiemanagement"},
                {"img": IMG["eg_drohne"], "alt": "Wohngebiet aus der Luft",
                 "title": "Energiegemeinschaft", "text": "Strom mit Nachbarn oder Verwandten teilen und beim Netzentgelt sparen. Österreichweit möglich.",
                 "link_key": "eg_privat", "link_text": "Energiegemeinschaft beitreten"},
                {"img": IMG["balkon"], "alt": "Balkonkraftwerk an einem Geländer",
                 "title": "Balkonkraftwerk und Wallbox", "text": "Der einfache Einstieg für Mieter und die Ladelösung für Ihr E-Auto.",
                 "link_key": "balkonkraftwerke", "link_text": "Balkonkraftwerk"},
            ],
        ),
        C.hub_section(
            eyebrow="Der EBZ Systemgedanke",
            h2="Wir denken in Systemen, nicht in Einzelteilen",
            lead=("Module aufs Dach schrauben kann jeder. Wir planen Erzeugung, Speicherung, Wärme und "
                  "Mobilität als ein System, das sauber ineinandergreift."),
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
            intro=("Je mehr Strom und Wärme Sie selbst erzeugen, speichern und nutzen, desto höher Ihre "
                   "Autarkie und desto weniger müssen Sie teuer dazukaufen. Mit rund 1.000 bis 1.100 kWh Jahresertrag je kWp gehört "
                   "Kärnten zu den besten Standorten Österreichs."),
            bars=[
                ("Energiekosten ohne eigenes System", 100, "bad", "voller Zukauf"),
                ("Energiekosten mit dem EBZ System", 15, "good", "bis zu 85 % weniger*"),
            ],
        ),
        C.steps_section(
            eyebrow="So einfach geht es",
            h2="In vier Schritten zur eigenen Anlage",
            steps=[
                ("Beratung", "Wir analysieren Verbrauch, Dach und Ziele bei Ihnen vor Ort. Kostenlos und unverbindlich.", ""),
                ("Projektbericht mit 3D", "Sie erhalten ein Fixangebot samt Projektbericht mit 3D-Belegplan und Statikreport.", ""),
                ("Förderung und Netzanmeldung", "Landespauschale, EAG-Zuschuss und die Anmeldung beim Netzbetreiber (in Kärnten meist Kärnten Netz): Wir erledigen alles.", ""),
                ("Montage", "Zertifizierte Fachkräfte montieren, wir übernehmen Zählertausch, Inbetriebnahme und Einschulung.", ""),
            ],
        ),
        C.media_text(
            eyebrow="Förderung 2026",
            h2="Förderung 2026 in Kärnten und der Steiermark: Landespauschale und EAG-Zuschuss",
            paragraphs=[
                ("Das Land Kärnten fördert 2026 private PV-Anlagen ab 5 kWp mit mindestens 5 kWh Speicher pauschal "
                 "mit 3.000 €, die Speicher-Nachrüstung mit 1.000 €. Einreichung vom 12. Oktober bis 31. Dezember "
                 "2026. Der EAG-Investitionszuschuss des Bundes zahlt 150 € je kWp bis 10 kWp und 150 € je kWh "
                 "Speicher, letzter Fördercall bis 22. Oktober 2026 (Quelle: Land Kärnten, EAG-Abwicklungsstelle, "
                 "Stand Oktober 2026)."),
                ("Ab 2027 plant der Bund laut BMWET eine Systemförderung für Speicher und intelligente Steuerung, "
                 "beantragt nach der Installation. Welche Programme für Ihr Projekt passen, prüfen wir und "
                 "stellen die Anträge: in Kärnten ebenso wie in der " +
                 a("foerderung_steiermark", "Steiermark") + "."),
            ],
            img=IMG["foerderung"],
            alt="Beratung zur Photovoltaik-Förderung in Kärnten am Tisch",
            bullets=[
                "3.000 € Landespauschale Kärnten für PV ab 5 kWp mit Speicher ab 5 kWh",
                "150 €/kWp und 150 €/kWh vom Bund, 10 % Made-in-Europe-Bonus",
                "Komplette Abwicklung durch EBZ Energie, inklusive Netzanmeldung",
            ],
            cta=("foerderung_kaernten", "PV-Förderung Kärnten 2026 im Detail"),
            reverse=True,
        ),
        C.reference_cards(
            eyebrow="Aus der Praxis",
            h2="Anlagen, die sich rechnen. Mit Zahlen belegt.",
            intro=("Über 300 dokumentierte Projekte in 6 Bundesländern, typische Amortisation 4 bis 6 Jahre. "
                   "Drei Beispiele, bei denen sich der Umstieg deutlich bezahlt macht."),
            items=[
                {"img": IMG["gewerbe_dach"], "alt": "Gewerbe-Photovoltaikanlage auf einem Trapezblechdach in Oberösterreich",
                 "title": "Gewerbe, Oberösterreich", "specs": "40 kWp in Ost-West-Ausrichtung, 40 kWh Speicher, rund 40.000 kWh im Jahr.",
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
        C.cards_section(
            eyebrow="Anbieter-Checkliste",
            h2="Woran Sie einen guten Photovoltaik-Betrieb in Kärnten erkennen",
            intro=("Die Suche nach Photovoltaik-Firmen in Kärnten, in Klagenfurt oder in der Steiermark liefert "
                   "Dutzende Treffer. Sechs Punkte, an denen Sie "
                   "einen Fachbetrieb von einem Vermittler unterscheiden, mit den Zahlen von EBZ Energie."),
            cards=[
                {"ic": "✓", "title": "Zertifizierte Montage", "text": "Zertifizierte Fachkräfte für Dach und Elektrotechnik, ein fester Ansprechpartner von der Planung bis zur Übergabe."},
                {"ic": "◫", "title": "Projektbericht statt Pauschale", "text": "Projektbericht mit 3D-Belegplan und Statikreport für Ihr Dach, dazu ein Fixangebot. Keine Standardanlage aus dem Katalog."},
                {"ic": "◇", "title": "Garantien schriftlich", "text": "Leistungsgarantie bis 30 Jahre und Produktgarantie mindestens 10 Jahre auf die Module, im Angebot festgehalten."},
                {"ic": "€", "title": "Förderung und Netz inklusive", "text": "Landespauschale, EAG-Antrag und Netzanmeldung bei Kärnten Netz oder Energie Klagenfurt übernimmt der Betrieb."},
                {"ic": "★", "title": "Bewertungen prüfen", "text": f"{NAP['rating']} Sterne aus {bewertungen} auf Google, von Kundinnen und Kunden aus Kärnten und der Steiermark."},
                {"ic": "◉", "title": "Referenzen mit Zahlen", "text": "300+ dokumentierte Projekte mit kWp, Speicher, Jahresertrag und Ersparnis statt bloßer Fotos.",
                 "link_key": "referenzen", "link_text": "Referenzen ansehen"},
            ],
        ),
        C.reviews_slider(_reviews, rating=_rating, count=_count),
        C.about_section(
            eyebrow="Über EBZ Energie",
            h2="Ihr Energie-Fachbetrieb aus Villach: Team, Zahlen, Handschlag",
            paragraphs=[
                ("EBZ Energie GmbH ist ein Photovoltaik-Fachbetrieb mit Sitz in Villach (Triglavstraße 15) und "
                 "montiert in Kärnten und der Steiermark. Über 300 dokumentierte Projekte in sechs Bundesländern, "
                 "Google-Bewertung 4,9 Sterne, bis zu 30 Jahre Leistungsgarantie. Jedes Angebot enthält einen "
                 "Projektbericht mit 3D-Belegplan und Statikreport (Stand Oktober 2026)."),
                ("Als Komplettanbieter planen und montieren wir das ganze System aus Photovoltaik, Speicher, "
                 "Wärmepumpe und Energiemanagement, mit zertifizierten Fachkräften und einem Ansprechpartner "
                 "von der ersten Beratung bis zum laufenden Service."),
            ],
            values=[
                ("⌂", "Regional verwurzelt in Villach"),
                ("☀", "Alles aus einer Hand"),
                ("✓", "Zertifizierte Fachkräfte"),
                ("★", "4,9 Sterne auf Google"),
            ],
            quote=(
                "Wir verkaufen keine Module, wir bauen Unabhängigkeit. Jedes System planen wir so, "
                "dass es zu Ihrem Dach, Ihrem Verbrauch und Ihrem Budget passt.",
                "Mario Zintl", "Geschäftsführung EBZ Energie GmbH",
            ),
            img=IMG["team_mission"],
            img_alt="EBZ Energie: Ihre Energie, unsere Mission. Das Team des "
                    "Photovoltaik-Fachbetriebs aus Villach.",
            cta=("ueber_uns", "Über EBZ Energie"),
        ),
        C.regions_section(
            eyebrow="Unser Einzugsgebiet",
            h2="Vor Ort in Kärnten und der Steiermark: Villach, Klagenfurt, Spittal, Wolfsberg, Graz",
            intro=("Photovoltaik Kärnten und Photovoltaik Steiermark aus einer Hand: Der Montageschwerpunkt "
                   "liegt rund um Villach, Klagenfurt, Wolfsberg und Graz. Für die Erstberatung kommen wir zu "
                   "Ihnen, Referenzprojekte gibt es in ganz Österreich."),
            kaernten=[a("pv_villach", "Villach"), "Klagenfurt", "Spittal an der Drau", "Feldkirchen",
                      "St. Veit an der Glan", a("pv_wolfsberg", "Wolfsberg"), "Völkermarkt", "Hermagor"],
            steiermark=["Graz", "Leibnitz", "Deutschlandsberg", "Voitsberg",
                        "Weiz", "Murtal", "Leoben", "Südoststeiermark"],
            note="Referenzprojekte auch im Burgenland, in Niederösterreich, Oberösterreich und Wien.",
        ),
        C.linkgrid_section(
            "Beliebte Seiten",
            [("photovoltaik", "Photovoltaikanlage mit Speicher"),
             ("pv_villach", "Photovoltaik in Villach"),
             ("foerderung_kaernten", "PV-Förderung Kärnten 2026"),
             ("foerderung_steiermark", "PV-Förderung Steiermark"),
             ("solarrechner", "PV-Rechner"),
             ("eg_privat", "Energiegemeinschaft beitreten"),
             ("finanzierung", "Finanzierung ab 147 €/Monat"),
             ("referenzen", "Referenzen")],
        ),
        C.contact_section(
            headline="Sind Sie bereit, Ihre Stromrechnung selbst zu schreiben?",
            sub=("Sie erreichen uns telefonisch oder über das Formular. Wir beraten Sie ehrlich "
                 "und zeigen Ihnen, was auf Ihrem Dach in Kärnten oder der Steiermark möglich ist."),
        ),
        C.faq_section(FAQ),
        C.finalcta(
            "Jetzt starten: Ihr eigenes Energiesystem",
            "Fordern Sie Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags.",
        ),
        _footnote(),
    ])

    faq = faq_jsonld(u(PATH), FAQ)
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq, include_business_schema=True)
    return write_page("index.html", html)


def _footnote():
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte auf Basis typischer Projekte. Die tatsächliche Ersparnis
      und Amortisation hängen von Verbrauch, Anlagengröße, Ausrichtung und Strompreis ab. Finanzierung:
      Beispielkonditionen, abhängig von Anlagengröße und Laufzeit, vorbehaltlich Bonitätsprüfung. Fördersätze
      und OeMAG-Marktpreis Stand Oktober 2026, Änderungen durch Fördergeber und OeMAG vorbehalten.
      Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    build()
