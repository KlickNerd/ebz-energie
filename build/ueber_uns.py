"""Ueber-uns-Seite (/ueber-uns/), auf EEAT ausgelegt.

Experience: 300+ Projekte, 6 Bundeslaender, regionale Wurzeln.
Expertise: eigene Planung, festangestellte zertifizierte Fachkraefte, All-in-One.
Authoritativeness: benannter Geschaeftsfuehrer Mario Zintl, 4,9 Google, Netzbetreiber-Kontakte.
Trustworthiness: Festpreisgarantie, NAP (Triglavstrasse 15), Garantien, echte Rezensionen.

Verbote beachtet: kein "Subunternehmer" (positiv: festangestellte Fachkraefte),
Adresse nur Triglavstrasse 15, keine Gedankenstriche, keine erfundenen Zahlen.
"""

from common import NAP, IMG, faq_jsonld, u, write_page, load_reviews
from layout import page
import components as C

PATH = "/ueber-uns/"
TITLE = "Über uns | EBZ Energie GmbH aus Villach"
DESC = ("Lernen Sie EBZ Energie kennen: Photovoltaik-Fachbetrieb aus Villach, geführt von "
        "Mario Zintl. Festangestellte, zertifizierte Fachkräfte, 300+ Projekte, 4,9 Sterne. "
        "Alles aus einer Hand für Kärnten und die Steiermark.")


def build():
    _rating, _count, _reviews = load_reviews()
    body = "".join([
        C.page_hero(
            eyebrow="Über uns",
            h1="Über EBZ Energie",
            lead=("Ihr Photovoltaik-Fachbetrieb aus Villach. Wir planen, montieren und betreuen "
                  "Ihr Energiesystem selbst, mit einem festangestellten Team und der Erfahrung "
                  "aus über 300 Projekten."),
            cta=("kontakt", "Kostenlose Beratung"),
            cta2=("referenzen", "Referenzen ansehen"),
        ),
        C.kpis([
            ("300+", "dokumentierte Projekte"),
            (NAP["rating"], "Google Bewertung"),
            ("6 Bundesländer", "mit Referenzen"),
            ("bis zu 30 Jahre", "Leistungsgarantie"),
        ]),
        C.media_text(
            eyebrow="Wer wir sind",
            h2="Ein regionaler Fachbetrieb für die ganze Energiewende",
            paragraphs=[
                ("EBZ Energie ist Ihr Photovoltaik-Fachbetrieb aus Villach. Aus dem regionalen "
                 "Betrieb ist ein Partner für die komplette Energiewende geworden: Photovoltaik, "
                 "Speicher, Wärmepumpe, Energiemanagement und Energiegemeinschaften, alles aus einer Hand."),
                ("Hinter jeder Anlage steht ein festangestelltes Team aus zertifizierten Fachkräften "
                 "und die Erfahrung aus über 300 dokumentierten Projekten in 6 Bundesländern. "
                 "Wir planen selbst, montieren selbst und bleiben Ihr Ansprechpartner, auch nach der Inbetriebnahme."),
            ],
            img=IMG["team_mission"],
            alt="Das Team von EBZ Energie, Photovoltaik-Fachbetrieb aus Villach",
            bullets=[
                "Standort Villach, im Einsatz für Kärnten und die Steiermark",
                "Direkte Kontakte zu Netzbetreibern und Behörden der Region",
                "Komplette Förderabwicklung inklusive",
            ],
        ),
        C.founder_block(
            "Ich bin in Villach geboren und aufgewachsen. Photovoltaik ist für mich mehr als ein "
            "Geschäft: Ich möchte, dass Menschen in der Region unabhängiger und günstiger mit "
            "Energie leben. Deshalb planen wir jede Anlage selbst, montieren mit unserem festangestellten "
            "Team und begleiten unsere Kundinnen und Kunden von der ersten Beratung bis zum laufenden Service."
        ),
        C.why_section(
            eyebrow="Wofür wir stehen",
            h2="Warum Kundinnen und Kunden uns vertrauen",
            items=[
                ("◇", "Echte Expertise", "Wir planen jede Anlage selbst. Statik, Belegung und Auslegung passen zu Ihrem Dach und Verbrauch."),
                ("★", "Jahrelange Erfahrung", "Über 300 dokumentierte Projekte in 6 Bundesländern. Wir wissen, worauf es ankommt."),
                ("✓", "Festangestellte Fachkräfte", "Montage durch zertifizierte, festangestellte Fachkräfte. Meisterhaftes Handwerk aus einer Hand."),
                ("€", "Festpreisgarantie", "Transparente Fixpreise ohne versteckte Kosten. Sie wissen von Anfang an, woran Sie sind."),
                ("⌂", "Regional verwurzelt", "Zuhause in Villach, mit direkten Kontakten zu Netzbetreibern und Behörden in Kärnten und der Steiermark."),
                ("⚙", "Alles aus einer Hand", "Beratung, Planung, Montage, Anmeldung und Förderabwicklung: ein Ansprechpartner für Ihr ganzes Projekt."),
            ],
        ),
        C.steps_section(
            eyebrow="So arbeiten wir",
            h2="Von der Beratung bis zum laufenden Service",
            steps=[
                ("Beratung", "Wir analysieren Verbrauch, Dach und Ziele. Kostenlos und unverbindlich.", ""),
                ("Planung mit 3D", "Sie erhalten ein Fixangebot samt Projektbericht mit 3D-Belegplan und Statikreport.", ""),
                ("Förderung und Behörden", "Wir übernehmen Förderanträge, Anmeldung und Behördenwege.", ""),
                ("Montage und Service", "Unser Team montiert, nimmt in Betrieb und bleibt Ihr Ansprechpartner.", ""),
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
            headline="Lernen Sie uns persönlich kennen",
            sub=("Sie erreichen uns telefonisch oder über das Formular. Wir beraten Sie ehrlich "
                 "und zeigen Ihnen, was auf Ihrem Dach möglich ist."),
        ),
        C.faq_section([
            ("Wer steht hinter EBZ Energie?",
             "EBZ Energie wird von Mario Zintl geführt, einem gebürtigen Villacher. Hinter dem Betrieb steht ein festangestelltes Team aus zertifizierten Fachkräften."),
            ("Arbeitet EBZ mit festangestellten Fachkräften?",
             "Ja. Planung und Montage übernehmen zertifizierte, festangestellte Fachkräfte. So bleibt die Qualität bei jedem Projekt in unserer Hand."),
            ("In welchen Regionen ist EBZ Energie tätig?",
             "Der Montageschwerpunkt liegt in Kärnten und der Steiermark. Referenzprojekte gibt es in 6 Bundesländern."),
            ("Übernimmt EBZ die Förderabwicklung?",
             "Ja. Wir kümmern uns um die passenden Bundes- und Landesförderungen sowie um Anmeldung und Behördenwege."),
            ("Gibt es feste Preise?",
             "Ja. Sie erhalten ein transparentes Fixangebot mit Festpreisgarantie, ohne versteckte Kosten."),
        ]),
        C.finalcta(
            "Bereit, EBZ Energie kennenzulernen?",
            "Fordern Sie Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags.",
        ),
        _footnote(),
    ])

    faq = faq_jsonld(u(PATH), [
        ("Wer steht hinter EBZ Energie?",
         "EBZ Energie wird von Mario Zintl gefuehrt. Hinter dem Betrieb steht ein festangestelltes Team aus zertifizierten Fachkraeften."),
        ("In welchen Regionen ist EBZ Energie taetig?",
         "Montageschwerpunkt in Kaernten und der Steiermark, Referenzprojekte in 6 Bundeslaendern."),
        ("Uebernimmt EBZ die Foerderabwicklung?",
         "Ja, inklusive passender Bundes- und Landesfoerderungen sowie Anmeldung und Behoerdenwege."),
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
