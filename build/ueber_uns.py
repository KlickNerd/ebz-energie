"""Ueber-uns-Seite (/ueber-uns/): warm, menschlich, einladend, und als Entitaets-Seite der Marke erkennbar.

Botschaft: EBZ Energie GmbH sind die freundlichen Energie-Handwerker aus Villach, die das
GANZE System machen (PV, Speicher, Waermepumpe, Energiemanagement, Energie-
gemeinschaft). Mehr Geschichte, mehr Bilder, Vertrauen durch Waerme + Kompetenz.
EEAT: benannter GF, Firmendaten (FN 597101 s, WK Kaernten, BH Villach), echte Zahlen/Reviews, NAP, Garantien.

SEO-Rolle (build/seo/ueber_uns.json, Oktober 2026): Title/H1 mit Firmierung "EBZ Energie GmbH" und
"Photovoltaik-Fachbetrieb aus Villach", Primaer "photovoltaik kaernten firmen". Review-Slider bleibt
(gemeinsame Komponente), wird nicht erweitert.

Verbote: kein "Subunternehmer" (positiv: Fachkraefte), nur
Triglavstrasse 15, keine Gedankenstriche, keine erfundenen Zahlen (kein Gruendungsjahr ohne Beleg).
"""

from common import NAP, IMG, EMAIL, faq_jsonld, u, a, href, tel_link, write_page, load_reviews, STANDORTE, standort_link
from layout import page
import components as C

PATH = "/ueber-uns/"
TITLE = "EBZ Energie GmbH: Photovoltaik-Fachbetrieb aus Villach"
DESC = ("EBZ Energie GmbH, Photovoltaik-Fachbetrieb aus Villach: 300+ Anlagen in Kärnten und der Steiermark, "
        "4,9 Sterne auf Google, ein fester Ansprechpartner für Planung und Montage.")

FN = "FN 597101 s"

FAQ = [
    ("Wer steht hinter EBZ Energie und wo ist der Firmensitz?",
     "Die EBZ Energie GmbH ist im Firmenbuch unter FN 597101 s eingetragen, Mitglied der Wirtschaftskammer Kärnten "
     "und wird von Mario Zintl geführt, einem gebürtigen Villacher. Der Firmensitz ist die Triglavstraße 15, "
     "9500 Villach; Besuche sind nach Terminvereinbarung Montag bis Freitag von 10 bis 20 Uhr möglich."),
    ("Wer montiert die Anlagen von EBZ Energie?",
     "Planung, Dachmontage und Elektrotechnik übernehmen zertifizierte Fachkräfte, die EBZ Energie koordiniert "
     "und verantwortet. So bleibt die Qualität bei jedem Projekt in unserer Hand, und Sie haben von der Beratung bis "
     "zum Service denselben Ansprechpartner."),
    ("Welche Qualifikationen hat das Team?",
     "Zertifizierte Fachkräfte für Dachmontage und Elektrotechnik, meisterhaftes Handwerk und Erfahrung aus über "
     "300 dokumentierten Projekten in 6 Bundesländern. Jede Anlage wird mit Projektbericht, 3D-Belegplan und "
     "Statikreport geplant und normgerecht in den Zählerschrank integriert."),
    ("Woran erkenne ich einen seriösen Photovoltaik-Anbieter in Kärnten?",
     "An prüfbaren Firmendaten (Firmenbuch, Impressum, Kammer), an zertifizierten Fachkräften für die Montage, an einem Projektbericht "
     "mit 3D-Belegplan und Statikreport statt einem Pauschalangebot, an schriftlichen Garantien (bis zu 30 Jahre "
     "Leistungs-, mindestens 10 Jahre Produktgarantie), an Referenzen mit Zahlen und an echten Google-Bewertungen."),
    ("Kann ich EBZ Energie in Villach besuchen?",
     "Ja, nach Terminvereinbarung in der Triglavstraße 15 in Villach. Für die Planung kommen wir aber meist zu Ihnen, "
     "weil wir Dach, Zählerschrank und Verbrauch vor Ort aufnehmen."),
    ("Übernimmt EBZ Energie die Förderabwicklung?",
     "Ja, komplett: Landespauschale Kärnten (3.000 € für PV ab 5 kWp mit Speicher), Förderung Steiermark, "
     "EAG-Zuschuss des Bundes sowie Mitteilung an die Gemeinde und Netzanmeldung beim Netzbetreiber. Welche "
     "Fristen gerade laufen, steht tagesaktuell auf unserer Förderseite."),
    ("Macht EBZ nur Photovoltaik?",
     "Nein. Wir begleiten die ganze Energiewende: Photovoltaik, Batteriespeicher, Wärmepumpe, Energiemanagement, "
     "Wallbox und Energiegemeinschaft, alles aus einer Hand."),
    ("Gibt es feste Preise?",
     "Ja. Sie erhalten ein transparentes Fixangebot mit Festpreisgarantie, ohne versteckte Kosten."),
]


def build():
    _rating, _count, _reviews = load_reviews()
    bew = f"{_count} Bewertungen" if _count else "über 100 Bewertungen"
    body = "".join([
        C.page_hero(
            eyebrow="EBZ Energie GmbH · Villach, Kärnten",
            h1="EBZ Energie GmbH: Ihr Photovoltaik-Fachbetrieb in Villach für Kärnten und die Steiermark",
            lead=("EBZ Energie GmbH ist ein Photovoltaik-Fachbetrieb mit Sitz in Villach (Triglavstraße 15) und "
                  "montiert in Kärnten und der Steiermark. Über 300 dokumentierte Projekte in sechs Bundesländern, "
                  f"Google-Bewertung {NAP['rating']} Sterne aus {bew}, bis zu 30 Jahre Leistungsgarantie. Jedes "
                  "Angebot enthält einen Projektbericht mit 3D-Belegplan und Statikreport (Stand Oktober 2026)."),
            cta=("kontakt", "Lernen Sie uns kennen"),
            cta2=("referenzen", "Unsere Projekte"),
        ),
        C.kpis([
            ("300+", "umgesetzte Projekte"),
            (NAP["rating"], f"Sterne auf Google, {bew}"),
            ("6 Bundesländer", "mit Referenzen"),
            ("bis zu 30 Jahre", "Leistungsgarantie"),
        ]),
        C.media_text(
            eyebrow="Wer wir sind",
            h2="Photovoltaik-Fachbetrieb aus Villach: Firma, Standort, Geschäftsführung",
            paragraphs=[
                ("Angefangen hat alles mit einer einfachen Überzeugung: Gute Energie soll leistbar sein und in der "
                 "Region bleiben. Daraus ist die EBZ Energie GmbH gewachsen, ein Fachbetrieb aus Villach, geführt "
                 "von Mario Zintl, einem gebürtigen Villacher. Eingetragen im Firmenbuch " + FN + ", Mitglied "
                 "der Wirtschaftskammer Kärnten, Aufsichtsbehörde Bezirkshauptmannschaft Villach."),
                ("Ob Sie uns als Photovoltaik-Fachbetrieb in Kärnten, als Installateur oder auf der Suche nach "
                 "Photovoltaik-Firmen in Villach gefunden haben: Dahinter steht ein Team aus zertifizierten "
                 "Fachkräften, das plant, die Montage koordiniert und auch nach der Inbetriebnahme für Sie da ist. "
                 "Als Komplettanbieter liefern wir die ganze Energiewende aus einer Hand: Strom vom Dach, Speicher, "
                 "Wärmepumpe, Energiemanagement und Energiegemeinschaft."),
            ],
            img=IMG["team_quer"],
            alt="Das Team von EBZ Energie, Photovoltaik-Fachbetrieb aus Villach",
            bullets=[
                "EBZ Energie GmbH, Triglavstraße 15, 9500 Villach, " + FN,
                "Geschäftsführung Mario Zintl, Mitglied der Wirtschaftskammer Kärnten",
                "Montage in Kärnten und der Steiermark, Referenzen in 6 Bundesländern",
            ],
            cta=("impressum", "Firmendaten im Impressum"),
        ),
        C.steps_section(
            eyebrow="So arbeiten wir",
            h2="Vom Erstgespräch bis zur Förderabwicklung",
            steps=[
                ("Erstgespräch und Vor-Ort-Termin", "Rückmeldung innerhalb eines Werktags, Besichtigung von Dach, Zählerschrank und Verbrauch meist innerhalb einer Woche*.", "1 Werktag"),
                ("Projektbericht und Fixangebot", "Projektbericht mit 3D-Belegplan und Statikreport, Festpreis-Angebot mit Förder-Check und auf Wunsch Finanzierung.", "wenige Tage"),
                ("Förderung, Gemeinde, Netz", "Landespauschale Kärnten oder Förderung Steiermark, EAG-Zuschuss, Mitteilung an die Gemeinde, Netzanmeldung.", "vor der Montage"),
                ("Montage, Übergabe, Service", "Montage durch unser Team in 2 bis 4 Tagen, Inbetriebnahme, Einschulung in die Monitoring-App. Danach bleiben wir Ihr Ansprechpartner.", "2 bis 4 Tage"),
            ],
        ),
        C.prose_panels(
            eyebrow="Was uns antreibt",
            h2="Mission und Vision",
            panels=[
                ("◎", "Unsere Mission", [
                    "Wir machen saubere Energie leistbar und einfach. Jede Familie und jeder Betrieb "
                    "in der Region soll den eigenen Strom nutzen und unabhängiger von steigenden Preisen werden.",
                    "Dafür liefern wir alles aus einer Hand, beraten ehrlich und bleiben ansprechbar, "
                    "wenn es darauf ankommt.",
                ], True),
                ("☀", "Unsere Vision", [
                    "Eine Region, die ihre Energie selbst erzeugt, speichert und teilt. Wir wollen dazu "
                    "beitragen, dass Kärnten und die Steiermark ein Stück unabhängiger werden.",
                    "Haus für Haus, Dach für Dach, Nachbarschaft für Nachbarschaft.",
                ], False),
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
            h2="Photovoltaik, Speicher, Wärmepumpe, Energiemanagement, Energiegemeinschaft",
            intro=("Wir denken Ihre Energie als Ganzes. Sie kombinieren genau die Bausteine, "
                   "die zu Ihrem Zuhause passen, und haben dafür nur einen Ansprechpartner."),
            cards=[
                {"ic": "☀", "title": "Photovoltaik", "text": "Ihr eigener Strom vom Dach, geplant für maximalen Eigenverbrauch. Photovoltaik Kärnten und Steiermark aus einer Hand.",
                 "link_key": "photovoltaik", "link_text": "Mehr erfahren"},
                {"ic": "▮", "title": "Batteriespeicher", "text": "Sonnenstrom am Abend nutzen und bei Stromausfall mit Notstrom vorbereitet sein.",
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
            eyebrow="Qualität, die man prüfen kann",
            h2="Handwerk mit Handschlagqualität, Fakten zum Nachlesen",
            items=[
                ("◫", "Prüfbare Firmendaten", "EBZ Energie GmbH, " + FN + ", Mitglied der Wirtschaftskammer Kärnten, Sitz Triglavstraße 15 in Villach. Alles im Impressum."),
                ("✓", "Ein Ansprechpartner", "Ein fester Ansprechpartner von der Planung bis zur Übergabe. Zertifizierte Fachkräfte für Dach und Elektrotechnik, meisterhaftes Handwerk."),
                ("☀", "Glas-Glas-Module mit Garantie", "Bifaziale Glas-Glas-Module mit bis zu 30 Jahren Leistungs- und mindestens 10 Jahren Produktgarantie, schriftlich im Angebot."),
                ("◇", "Projektbericht statt Pauschale", "Projektbericht mit 3D-Belegplan und Statikreport für Ihr Dach, dazu ein Fixangebot mit Festpreisgarantie."),
                ("€", "Förderabwicklung inklusive", "Landespauschale Kärnten, Förderung Steiermark, EAG-Zuschuss und Netzanmeldung: wir stellen die Anträge, Sie unterschreiben."),
                ("★", "Erfahrung aus 300+ Projekten", f"Referenzen mit Zahlen in 6 Bundesländern und {NAP['rating']} Sterne aus {bew} auf Google."),
            ],
        ),
        C.facts_panel(
            eyebrow="EBZ auf einen Blick",
            h2="Fakten und Kontakt",
            intro="Alle wichtigen Angaben zur EBZ Energie GmbH auf einen Blick. Rechtliche Details finden Sie im Impressum.",
            rows=[
                ("Firmierung", "EBZ Energie GmbH"),
                ("Firmenbuchnummer", FN),
                ("Geschäftsführung", "Mario Zintl"),
                ("Kammerzugehörigkeit", "Wirtschaftskammer Kärnten"),
                ("Adresse", f"{NAP['street']}, {NAP['zip']} {NAP['city']}"),
                ("Telefon", tel_link()),
                ("E-Mail", f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
                ("Öffnungszeiten", NAP["hours"]),
                ("Einzugsgebiet", "Kärnten und Steiermark, Referenzen in 6 Bundesländern"),
                ("Google-Bewertung", f"{NAP['rating']} von 5 aus {bew}"),
                ("Erfahrung", "300+ dokumentierte Projekte"),
                ("Garantie", "bis zu 30 Jahre Leistungs-, mind. 10 Jahre Produktgarantie"),
            ],
            actions=[
                ("Auf Google Maps ansehen", "https://www.google.com/maps?cid=15592511037270601677",
                 ' target="_blank" rel="noopener"'),
                ("Zum Impressum", href("impressum"), ""),
            ],
        ),
        C.reviews_slider(_reviews, rating=_rating, count=_count),
        C.regions_section(
            eyebrow="Unser Einzugsgebiet",
            h2="Vor Ort in Kärnten und der Steiermark",
            intro=("Der Montageschwerpunkt liegt in Kärnten und der Steiermark: als Photovoltaik Anbieter Steiermark "
                   "rund um Graz, in Kärnten von Villach bis Wolfsberg. Referenzprojekte gibt es darüber hinaus in "
                   "ganz Österreich."),
            kaernten=[standort_link(k, n) for k, n, l, _s in STANDORTE if l == "ktn"],
            steiermark=[standort_link(k, n) for k, n, l, _s in STANDORTE if l == "stmk"],
            note=("Überblick für die Region: " + a("pv_steiermark", "Photovoltaik und Wärmepumpe in der Steiermark")
                  + ". Referenzprojekte auch im Burgenland, in Niederösterreich, Oberösterreich und Wien."),
        ),
        C.contact_section(
            headline="Auf einen Kaffee und ein ehrliches Gespräch",
            sub=("Rufen Sie uns an oder schreiben Sie uns. Wir beraten Sie ehrlich und zeigen Ihnen "
                 "in Ruhe, was auf Ihrem Dach möglich ist. Kostenlos und unverbindlich."),
        ),
        C.faq_section(FAQ),
        C.linkgrid_section("Weiterlesen", [
            ("photovoltaik", "Photovoltaik in Kärnten und der Steiermark"),
            ("pv_villach", "Photovoltaik in Villach"),
            ("referenzen", "300+ Projekte: Referenzen mit echten Zahlen"),
            ("kontakt", "Kostenlose Erstberatung anfragen"),
            ("foerderung_kaernten", "Photovoltaik-Förderung Kärnten 2026"),
            ("foerderung_steiermark", "Photovoltaik-Förderung Steiermark 2026"),
            ("finanzierung", "Finanzierung ab 147 € pro Monat"),
            ("impressum", "Firmendaten im Impressum"),
        ]),
        C.finalcta(
            "Lernen wir uns kennen?",
            "Fordern Sie Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags und "
            "nehmen uns Zeit für Ihre Fragen.",
        ),
        _footnote(),
    ])

    faq = faq_jsonld(u(PATH), FAQ)
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq,
                og_image="/assets/img/team-ebz-mission.jpg")
    return write_page("ueber-uns/index.html", html)


def _footnote():
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Zeitangabe laut Kundenbewertungen auf Google (Stand Oktober 2026), Erfahrungswert, keine Zusage.
      Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.
      EBZ Energie GmbH, Triglavstraße 15, 9500 Villach, FN 597101 s.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    build()
