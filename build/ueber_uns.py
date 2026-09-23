"""Ueber-uns-Seite (/ueber-uns/): warm, menschlich, einladend.

Botschaft: EBZ sind die freundlichen Energie-Handwerker aus Oesterreich, die das
GANZE System machen (PV, Speicher, Waermepumpe, Energiemanagement, Energie-
gemeinschaft). Mehr Geschichte, mehr Bilder, Vertrauen durch Waerme + Kompetenz.
EEAT bleibt gewahrt (benannter GF, echte Zahlen/Reviews, NAP, Garantien).

Verbote: kein "Subunternehmer" (positiv: festangestellte Fachkraefte), nur
Triglavstrasse 15, keine Gedankenstriche, keine erfundenen Zahlen.
"""

from common import NAP, IMG, faq_jsonld, u, write_page, load_reviews
from layout import page
import components as C

PATH = "/ueber-uns/"
TITLE = "Über uns | Die Energie-Handwerker aus Villach | EBZ Energie"
DESC = ("Lernen Sie EBZ Energie kennen: die freundlichen Energie-Handwerker aus Villach. "
        "Photovoltaik, Speicher, Wärmepumpe und Energiegemeinschaft aus einer Hand, "
        "geführt von Mario Zintl. Festangestelltes Team, 300+ Projekte, 4,9 Sterne.")


def build():
    _rating, _count, _reviews = load_reviews()
    body = "".join([
        C.page_hero(
            eyebrow="Servus, wir sind EBZ Energie",
            h1="Die freundlichen Energie-Handwerker aus Villach",
            lead=("Menschen aus der Region, die Ihr Zuhause unabhängig machen: mit Photovoltaik, "
                  "Speicher, Wärmepumpe und Energiegemeinschaft. Ehrlich beraten, sauber montiert "
                  "und persönlich betreut."),
            cta=("kontakt", "Lernen Sie uns kennen"),
            cta2=("referenzen", "Unsere Projekte"),
        ),
        C.kpis([
            ("300+", "umgesetzte Projekte"),
            (NAP["rating"], "Sterne auf Google"),
            ("6 Bundesländer", "mit Referenzen"),
            ("bis zu 30 Jahre", "Leistungsgarantie"),
        ]),
        C.media_text(
            eyebrow="Unsere Geschichte",
            h2="Aus der Region, für die Region",
            paragraphs=[
                ("Angefangen hat alles mit einer einfachen Überzeugung: Gute Energie soll leistbar "
                 "sein und in der Region bleiben. Aus dieser Idee ist EBZ Energie gewachsen, ein "
                 "Fachbetrieb aus Villach, der heute die ganze Energiewende aus einer Hand begleitet."),
                ("Wir sind keine anonyme Kette, sondern Ihre Nachbarn. Ein festangestelltes Team aus "
                 "zertifizierten Fachkräften, das selbst plant, selbst montiert und auch nach der "
                 "Inbetriebnahme für Sie da ist. Mit einem Handschlag, auf den Sie sich verlassen können."),
            ],
            img=IMG["team_quer"],
            alt="Das Team von EBZ Energie, Ihr Photovoltaik-Fachbetrieb aus Villach",
            bullets=[
                "Photovoltaik, Speicher, Wärmepumpe, Energiemanagement und Energiegemeinschaft",
                "Ehrliche Beratung, ohne Verkaufsdruck",
                "Ein Ansprechpartner, von der ersten Idee bis zum laufenden Service",
            ],
        ),
        C.gallery(
            eyebrow="Einblicke",
            h2="So sieht unsere Arbeit aus",
            intro=("Vom ersten Gespräch am Küchentisch bis zur fertigen Anlage auf dem Dach: "
                   "ein paar Eindrücke aus dem EBZ Alltag."),
            items=[
                (IMG["ref_villach"], "Photovoltaikanlage auf einem Einfamilienhaus in Villach", "Photovoltaik fürs Eigenheim"),
                (IMG["gewerbe_dach"], "Große Photovoltaikanlage auf einem Gewerbedach", "Große Dächer für Betriebe"),
                (IMG["speicher"], "Batteriespeicher im Technikraum", "Speicher für Strom rund um die Uhr"),
                (IMG["waermepumpe"], "Wärmepumpe an einer Hauswand", "Wärmepumpe statt Öl und Gas"),
                (IMG["balkon"], "Balkonkraftwerk an einem Geländer", "Balkonkraftwerk für Mieter"),
                (IMG["eg_drohne"], "Wohngebiet aus der Luft", "Energie teilen in der Nachbarschaft"),
            ],
        ),
        C.cards_section(
            eyebrow="Alles aus einer Hand",
            h2="Nicht nur Photovoltaik",
            intro=("Wir denken Ihre Energie als Ganzes. Sie kombinieren genau die Bausteine, "
                   "die zu Ihrem Zuhause passen, und haben dafür nur einen Ansprechpartner."),
            cards=[
                {"ic": "☀", "title": "Photovoltaik", "text": "Ihr eigener Strom vom Dach, geplant für maximalen Eigenverbrauch.",
                 "link_key": "photovoltaik", "link_text": "Mehr erfahren"},
                {"ic": "▮", "title": "Batteriespeicher", "text": "Sonnenstrom am Abend nutzen und bei Stromausfall vorbereitet sein.",
                 "link_key": "batteriespeicher", "link_text": "Mehr erfahren"},
                {"ic": "♨", "title": "Wärmepumpe", "text": "Heizen mit dem eigenen Strom statt mit teurem Öl oder Gas.",
                 "link_key": "waermepumpe", "link_text": "Mehr erfahren"},
                {"ic": "⚙", "title": "Energiemanagement", "text": "Ein System steuert Anlage, Speicher, Wärmepumpe und Wallbox automatisch.",
                 "link_key": "ems", "link_text": "Mehr erfahren"},
                {"ic": "⬡", "title": "Energiegemeinschaft", "text": "Strom mit Nachbarn oder Verwandten teilen. Österreichweit möglich.",
                 "link_key": "eg_privat", "link_text": "Mehr erfahren"},
                {"ic": "⌂", "title": "Balkonkraftwerk und Wallbox", "text": "Der einfache Einstieg und die Ladelösung für Ihr E-Auto.",
                 "link_key": "balkonkraftwerke", "link_text": "Mehr erfahren"},
            ],
        ),
        C.founder_block(
            "Mir ist wichtig, dass Sie sich bei uns gut aufgehoben fühlen. Wir nehmen uns Zeit, "
            "erklären alles verständlich und versprechen nichts, was wir nicht halten können. "
            "Am Ende soll nicht nur die Anlage passen, sondern auch das Gefühl, den richtigen "
            "Partner gewählt zu haben."
        ),
        C.why_section(
            eyebrow="Was Sie bei uns erwartet",
            h2="Handwerk mit Handschlagqualität",
            items=[
                ("◇", "Beratung auf Augenhöhe", "Wir hören zu, erklären verständlich und lassen Ihnen Zeit. Ganz ohne Verkaufsdruck."),
                ("★", "Erfahrung aus 300+ Projekten", "Was wir empfehlen, haben wir hundertfach gebaut. Sie profitieren von echter Praxis."),
                ("✓", "Festangestelltes Team", "Dieselben Gesichter von der Planung bis zur Montage. Zertifizierte Fachkräfte, meisterhaftes Handwerk."),
                ("€", "Faire Festpreise", "Transparente Fixangebote ohne Kleingedrucktes. Sie wissen immer, woran Sie sind."),
                ("⌂", "Aus Ihrer Nähe", "Zuhause in Villach, mit kurzen Wegen zu Netzbetreibern und Behörden in Kärnten und der Steiermark."),
                ("☀", "Da, auch nach der Montage", "Fragen nach der Inbetriebnahme? Wir bleiben Ihr Ansprechpartner. Versprochen."),
            ],
        ),
        C.reviews_slider(_reviews, rating=_rating, count=_count),
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
        C.contact_section(
            headline="Auf einen Kaffee und ein ehrliches Gespräch",
            sub=("Rufen Sie uns an oder schreiben Sie uns. Wir beraten Sie ehrlich und zeigen Ihnen "
                 "in Ruhe, was auf Ihrem Dach möglich ist. Kostenlos und unverbindlich."),
        ),
        C.faq_section([
            ("Wer steht hinter EBZ Energie?",
             "EBZ Energie wird von Mario Zintl geführt, einem gebürtigen Villacher. Hinter dem Betrieb steht ein festangestelltes Team aus zertifizierten Fachkräften."),
            ("Macht EBZ nur Photovoltaik?",
             "Nein. Wir begleiten die ganze Energiewende: Photovoltaik, Batteriespeicher, Wärmepumpe, Energiemanagement und Energiegemeinschaft, alles aus einer Hand."),
            ("Arbeitet EBZ mit festangestellten Fachkräften?",
             "Ja. Planung und Montage übernehmen zertifizierte, festangestellte Fachkräfte. So bleibt die Qualität bei jedem Projekt in unserer Hand."),
            ("In welchen Regionen ist EBZ Energie tätig?",
             "Der Montageschwerpunkt liegt in Kärnten und der Steiermark. Referenzprojekte gibt es in 6 Bundesländern."),
            ("Gibt es feste Preise?",
             "Ja. Sie erhalten ein transparentes Fixangebot mit Festpreisgarantie, ohne versteckte Kosten."),
        ]),
        C.finalcta(
            "Lernen wir uns kennen?",
            "Fordern Sie Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags und "
            "nehmen uns Zeit für Ihre Fragen.",
        ),
        _footnote(),
    ])

    faq = faq_jsonld(u(PATH), [
        ("Wer steht hinter EBZ Energie?",
         "EBZ Energie wird von Mario Zintl gefuehrt. Hinter dem Betrieb steht ein festangestelltes Team aus zertifizierten Fachkraeften."),
        ("Macht EBZ nur Photovoltaik?",
         "Nein, EBZ begleitet die ganze Energiewende: Photovoltaik, Speicher, Waermepumpe, Energiemanagement und Energiegemeinschaft."),
        ("In welchen Regionen ist EBZ Energie taetig?",
         "Montageschwerpunkt in Kaernten und der Steiermark, Referenzprojekte in 6 Bundeslaendern."),
        ("Gibt es feste Preise?",
         "Ja, ein transparentes Fixangebot mit Festpreisgarantie ohne versteckte Kosten."),
    ])

    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq, include_business_schema=True,
                og_image="/assets/img/team-ebz-mission.jpg")
    return write_page("ueber-uns/index.html", html)


def _footnote():
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.
      EBZ Energie GmbH, Triglavstraße 15, 9500 Villach.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    build()
