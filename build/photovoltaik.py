"""Leistungsseite Photovoltaik (/photovoltaik/).

Roter Faden (Conversion): Hook -> abholen (Eigenheim/Gewerbe) -> warum jetzt ->
verstehen -> Geld-Fragen offen -> warum EBZ -> Beweis -> Reibung/Einwaende raus
-> eine klare Handlung (kostenlose Beratung).

Zielgruppen: Eigenheim UND Gewerbe gleichwertig. Rolle der Seite: lokaler
Conversion-Pillar + Cluster-Zentrum (nicht Ranking fuer das Kopf-Keyword).
Verbote beachtet (85 %, 4,9, Finanzierung, Projektbericht, keine Dashes).
"""

from common import CLAIMS, NAP, IMG, faq_jsonld, u, write_page, load_reviews
from layout import page
import components as C

PATH = "/photovoltaik/"
TITLE = "Photovoltaik Kärnten & Steiermark | Eigenheim & Gewerbe | EBZ"
DESC = ("Photovoltaik vom Fachbetrieb EBZ Energie für Eigenheim und Gewerbe in Kärnten und der "
        "Steiermark. Bis zu 85 % weniger Stromkosten, Förderung und Finanzierung inklusive, "
        "4,9 Sterne, 300+ Projekte. Jetzt kostenlose Beratung.")


def build():
    _rating, _count, _reviews = load_reviews()
    body = "".join([
        # 1. Hook
        C.hero(
            eyebrow="Photovoltaik für Eigenheim und Gewerbe in Kärnten und der Steiermark",
            h1="Photovoltaik vom Fachbetrieb: Ihr eigener Strom vom Dach",
            lead=("Steigende Strompreise treffen jeden. Mit Ihrer eigenen Photovoltaikanlage drehen "
                  "Sie das um und senken Ihre Stromkosten um bis zu 85 %. Wir planen, montieren und "
                  "betreuen alles aus einer Hand, mit einem festangestellten Team aus der Region."),
            badges=[("Alles", "aus einer Hand"),
                    ("Faire", "Finanzierung"),
                    ("Regional", "aus Villach")],
            img=IMG["gen_hero"],
            img_alt="Photovoltaikanlage auf einem Wohnhaus in Kärnten",
            float_num="4,9",
            float_label="aus 111 Google Bewertungen",
        ),
        # Quick Trust
        C.kpis([
            ("300+", "umgesetzte Projekte"),
            (NAP["rating"], "Sterne auf Google"),
            ("bis zu 85 %", "weniger Stromkosten"),
            ("4 bis 6 Jahre", "typische Amortisation"),
        ]),
        # 2. Abholen: Eigenheim oder Gewerbe
        C.audience_split(
            eyebrow="Für wen planen wir?",
            h2="Ob Eigenheim oder Betrieb: Ihre Anlage passt zu Ihnen",
            intro="Wählen Sie, was auf Sie zutrifft. Wir richten Planung, Größe und Wirtschaftlichkeit genau danach aus.",
            left={
                "img": IMG["gen_eigenheim"],
                "alt": "Einfamilienhaus mit Photovoltaikanlage in Kärnten",
                "title": "Für Ihr Eigenheim",
                "bullets": [
                    "Bis zu 85 % weniger Stromkosten",
                    "Speicher und Notstrom für den Abend",
                    "Volle Förderung und Finanzierung ab 147 € im Monat",
                ],
                "cta": ("kontakt", "Beratung für mein Zuhause"),
            },
            right={
                "img": IMG["gen_gewerbe"],
                "alt": "Gewerbebetrieb mit großer Photovoltaikanlage am Dach",
                "title": "Für Ihren Betrieb",
                "bullets": [
                    "Hoher Eigenverbrauch tagsüber senkt die Betriebskosten",
                    "Große Dächer, Planung nach Lastprofil",
                    "Spürbare Ersparnis pro Jahr, planbare Rendite",
                ],
                "cta": ("#gewerbe", "Photovoltaik für Gewerbe"),
            },
        ),
        # 3. Warum jetzt
        C.problem_compare(
            eyebrow="Warum sich der Umstieg jetzt lohnt",
            h2="Weniger zukaufen, mehr Unabhängigkeit",
            intro=("Strompreise steigen, Förderungen gibt es jetzt und die Anlagenpreise sind "
                   "gefallen. Was Sie selbst erzeugen und verbrauchen, müssen Sie nicht teuer aus "
                   "dem Netz kaufen."),
            bars=[
                ("Stromkosten ohne eigene Anlage", 100, "bad", "voller Netzbezug"),
                ("Stromkosten mit Photovoltaik und Speicher", 15, "good", "bis zu 85 % weniger*"),
            ],
            aside=("Ihre Vorteile auf einen Blick", [
                ("☀", "Eigener Strom", "Sie produzieren Ihren Strom selbst, viele Jahre lang."),
                ("€", "Planbare Kosten", "Unabhängiger von steigenden Strompreisen."),
                ("▮", "Auch am Abend", "Mit Speicher nutzen Sie Sonnenstrom rund um die Uhr."),
                ("✓", "Ohne Aufwand", "Wir kümmern uns um Förderung, Anmeldung und Montage."),
            ]),
        ),
        # 4. Verstehen
        C.media_text(
            eyebrow="So funktioniert Photovoltaik",
            h2="So wird aus Sonne Ihr eigener Strom",
            paragraphs=[
                ("Die Module auf Ihrem Dach wandeln Sonnenlicht in Strom um. Der Wechselrichter macht "
                 "daraus nutzbaren Haushaltsstrom, den Sie sofort verbrauchen."),
                ("Was Sie gerade nicht brauchen, speichert ein Batteriespeicher für den Abend. Ein "
                 "Energiemanagement sorgt dafür, dass möglichst viel Ihres Sonnenstroms im eigenen "
                 "Haus bleibt, statt günstig ins Netz zu fließen."),
            ],
            img=IMG["gen_detail"],
            alt="Montage von Photovoltaikmodulen auf einem Dach",
            bullets=[
                "<b>Module:</b> erzeugen Strom aus Sonnenlicht, auch bei bewölktem Himmel",
                "<b>Wechselrichter:</b> macht nutzbaren Haushaltsstrom daraus",
                "<b>Speicher:</b> macht Sonnenstrom am Abend nutzbar",
                "<b>Energiemanagement:</b> steuert Verbrauch, Speicher und Wärmepumpe",
            ],
        ),
        C.cards_section(
            eyebrow="Alles aus einer Hand",
            h2="Ihre Anlage, komplett gedacht",
            intro=("Von den Modulen bis zur Ladestation: EBZ Energie plant Ihr System als Ganzes "
                   "und montiert es mit zertifizierten Fachkräften."),
            cards=[
                {"ic": "☀", "title": "Photovoltaikmodule", "text": "Hochwertige Module mit starker Leistung, passend zu Dachform und Ausrichtung."},
                {"ic": "▮", "title": "Batteriespeicher", "text": "Sonnenstrom am Abend nutzen und mit Notstrom vorbereitet sein.",
                 "link_key": "batteriespeicher", "link_text": "Zum Speicher"},
                {"ic": "⌂", "title": "Wallbox", "text": "Laden Sie Ihr E-Auto direkt mit dem eigenen Sonnenstrom.",
                 "link_key": "balkonkraftwerke", "link_text": "Mehr erfahren"},
                {"ic": "⚙", "title": "Energiemanagement", "text": "Ein System steuert Anlage, Speicher, Wärmepumpe und Wallbox.",
                 "link_key": "ems", "link_text": "Zum Energiemanagement"},
                {"ic": "♨", "title": "Wärmepumpe", "text": "Heizen Sie mit Ihrem eigenen Strom statt mit teurem Gas oder Öl.",
                 "link_key": "waermepumpe", "link_text": "Zur Wärmepumpe"},
                {"ic": "◷", "title": "Service und Monitoring", "text": "Wir bleiben Ihr Ansprechpartner, auch nach der Inbetriebnahme."},
            ],
        ),
        C.media_text(
            eyebrow="Photovoltaik mit Speicher",
            h2="Mehr vom eigenen Strom mit Batteriespeicher",
            paragraphs=[
                ("Ohne Speicher nutzen Sie tagsüber nur einen Teil Ihres Sonnenstroms selbst. Ein "
                 "Batteriespeicher hebt Ihren Eigenverbrauch deutlich an: Sie laden am Tag und nutzen "
                 "den Strom am Abend, wenn die Sonne nicht mehr scheint."),
                ("In Kombination mit einer Notstromfunktion bleibt Ihr Haus auch bei einem Stromausfall "
                 "versorgt. So holen Sie das Maximum aus Ihrer Anlage."),
            ],
            img=IMG["speicher"],
            alt="Batteriespeicher einer Photovoltaikanlage im Technikraum",
            bullets=[
                "Höherer Eigenverbrauch statt günstiger Einspeisung",
                "Sonnenstrom auch am Abend und in der Nacht",
                "Optional mit Notstrom bei Stromausfall",
            ],
            reverse=True,
            cta=("batteriespeicher", "Mehr zum Batteriespeicher"),
        ),
        # 5. Geld-Fragen offen beantworten
        C.price_cards(
            eyebrow="Photovoltaik Kosten",
            h2="Was kostet eine Photovoltaikanlage?",
            intro=("Der Preis hängt von Anlagengröße, Dach und Speicher ab. Diese Richtwerte "
                   "geben Ihnen eine erste Orientierung vor Förderung."),
            items=[
                {"size": "Kleine Anlage", "price": "ab ca. 9.000 €", "price_sub": "rund 5 kWp, ohne Speicher*",
                 "features": ["Ideal für kleinere Haushalte", "Hoher Eigenverbrauch am Tag", "Später um Speicher erweiterbar"]},
                {"size": "Beliebte Größe", "price": "15.000 bis 22.000 €", "price_sub": "rund 10 kWp mit Speicher*",
                 "features": ["Für das typische Einfamilienhaus", "Inklusive Batteriespeicher", "Optional mit Notstrom"]},
                {"size": "Gewerbe und große Dächer", "price": "individuell", "price_sub": "ab rund 20 kWp*",
                 "features": ["Für Betriebe und große Haushalte", "Hohe Ersparnis pro Jahr", "Planung nach Lastprofil"]},
            ],
            note="*Richtwerte auf Basis typischer Projekte, vor Förderung. Ihren genauen Preis erhalten Sie in der kostenlosen Beratung.",
        ),
        C.finance_band(),
        C.media_text(
            eyebrow="Förderungen",
            h2="Förderungen sichern, Kosten senken",
            paragraphs=[
                ("Photovoltaik wird in Österreich gefördert: über Bundesmittel und über "
                 "Landesförderungen in Kärnten und der Steiermark. Wir kennen die aktuellen Programme "
                 "und kümmern uns um die Anträge."),
                ("So sichern Sie sich die Förderungen, die Ihnen zustehen, und verkürzen die Zeit, "
                 "bis sich Ihre Anlage rechnet."),
            ],
            img=IMG["foerderung"],
            alt="Beratung zur Photovoltaik Förderung am Tisch",
            bullets=[
                "Bundesförderung für Photovoltaik und Speicher",
                "Landesförderungen in Kärnten und der Steiermark",
                "Komplette Abwicklung durch EBZ Energie",
            ],
            cta=("foerderung_at", "Förderungen im Überblick"),
        ),
        # Gewerbe-Abschnitt (Sprungziel der Zielgruppen-Weiche)
        C.media_text(
            eyebrow="Photovoltaik für Gewerbe",
            h2="Für Ihren Betrieb: Strom produzieren, wenn Sie ihn brauchen",
            paragraphs=[
                ("Betriebe verbrauchen den meisten Strom tagsüber, genau dann, wenn die Sonne "
                 "scheint. Dadurch ist der Eigenverbrauch besonders hoch und Ihre Anlage rechnet sich "
                 "oft noch schneller als im Privathaushalt."),
                ("Wir planen Ihre Anlage nach Ihrem Lastprofil, von der Dachprüfung bis zum "
                 "Netzanschluss, und begleiten Sie durch Förderung und Anmeldung."),
            ],
            img=IMG["gen_gewerbe"],
            alt="Große Photovoltaikanlage auf einem Gewerbedach",
            bullets=[
                "Hoher Eigenverbrauch tagsüber, niedrigere Betriebskosten",
                "Planung nach Lastprofil, auch für große Dächer",
                "Beispiel Gewerbe OÖ: 40 kWp, rund 13.500 € Ersparnis pro Jahr",
            ],
            reverse=True,
            anchor="gewerbe",
            cta=("kontakt", "Gewerbe-Beratung anfragen"),
        ),
        # 6. Warum EBZ
        C.why_section(
            eyebrow="Warum EBZ Energie",
            h2="Ihr Photovoltaik-Partner in der Region",
            items=[
                ("☀", "Alles aus einer Hand", "Planung, Montage, Förderung und Service. Ein Ansprechpartner für alles."),
                ("✓", "Zertifizierte Fachkräfte", "Festangestelltes Team, meisterhaftes Handwerk und sorgfältige Ausführung."),
                ("★", "4,9 Sterne auf Google", "Bewertungen von echten Kundinnen und Kunden aus der Region."),
                ("◉", "300+ Anlagen", "Erfahrung aus über 300 dokumentierten Projekten in 6 Bundesländern."),
                ("€", "Faire Finanzierung", "Ihre Anlage gehört Ihnen ab Tag 1. Ab 147 € im Monat inklusive Speicher."),
                ("⌂", "Regional verwurzelt", "Zuhause in Villach, im Einsatz für Kärnten und die Steiermark."),
            ],
        ),
        # 7. Beweis
        C.reference_cards(
            eyebrow="Aus der Praxis",
            h2="Anlagen, die sich rechnen. Mit Zahlen belegt.",
            intro=("Ein paar unserer Projekte aus Eigenheim und Gewerbe. Jede Anlage planen wir "
                   "individuell, damit sie zu Dach, Verbrauch und Budget passt."),
            items=[
                {"img": IMG["ref_villach"], "alt": "Photovoltaikanlage auf einem Einfamilienhaus in Villach",
                 "title": "Einfamilienhaus, Villach", "specs": "10 kWp Ost-West mit Notstrom, rund 11.000 kWh im Jahr.",
                 "result": "rund 80 %", "result_sub": "weniger Stromkosten"},
                {"img": IMG["ref_krumpendorf"], "alt": "Photovoltaikanlage auf einem Mehrparteienhaus in Krumpendorf",
                 "title": "Mehrparteienhaus, Krumpendorf", "specs": "25 kWp mit 25 kWh Speicher und Notstrom.",
                 "result": "4 Tage", "result_sub": "Bauzeit"},
                {"img": IMG["gewerbe_dach"], "alt": "Große Photovoltaikanlage auf einem Gewerbedach in Oberösterreich",
                 "title": "Gewerbe, Oberösterreich", "specs": "40 kWp Ost-West, 40 kWh Speicher, rund 40.000 kWh im Jahr.",
                 "result": "13.500 €", "result_sub": "Ersparnis pro Jahr"},
            ],
        ),
        C.reviews_slider(_reviews, rating=_rating, count=_count),
        # 8. Reibung und Einwaende raus
        C.steps_section(
            eyebrow="So einfach läuft es ab",
            h2="Von der Beratung bis zum eigenen Sonnenstrom",
            steps=[
                ("Beratung", "Wir besprechen Verbrauch, Dach und Ziele. Kostenlos und unverbindlich.", ""),
                ("Projektbericht", "Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport.", ""),
                ("Montage", "Zertifizierte Fachkräfte montieren Ihre Anlage sauber und termintreu.", ""),
                ("Inbetriebnahme", "Wir kümmern uns um Anmeldung, Zählertausch und Übergabe.", ""),
            ],
        ),
        C.faq_section([
            ("Lohnt sich Photovoltaik in Österreich?",
             "Ja. Durch gestiegene Strompreise, staatliche Förderungen und einen hohen Eigenverbrauch rechnet sich eine Anlage heute schneller als früher, in der Praxis meist innerhalb von 4 bis 6 Jahren. Danach produzieren Sie viele Jahre günstigen eigenen Strom."),
            ("Was kostet eine Photovoltaikanlage mit Speicher?",
             "Eine Komplettanlage mit rund 10 kWp und Speicher liegt typischerweise bei rund 15.000 bis 22.000 € vor Förderung. Der genaue Preis hängt von Dach, Speichergröße und Ausstattung ab."),
            ("Lohnt sich Photovoltaik auch für Betriebe?",
             "Besonders. Betriebe verbrauchen viel Strom tagsüber, wenn die Anlage produziert. Der hohe Eigenverbrauch senkt die Betriebskosten deutlich und die Anlage rechnet sich oft noch schneller."),
            ("Ist eine Photovoltaikanlage mit oder ohne Speicher besser?",
             "Mit Speicher nutzen Sie deutlich mehr Ihres Sonnenstroms selbst, weil Sie den Strom auch am Abend verwenden. Ein Speicher lohnt sich besonders, wenn Sie tagsüber wenig zu Hause sind oder Notstrom möchten."),
            ("Wie hoch ist die Förderung für Photovoltaik?",
             "Photovoltaik wird über Bundesmittel und über Landesförderungen in Kärnten und der Steiermark gefördert. Die Höhe hängt vom Programm und der Anlage ab. EBZ Energie übernimmt die Anträge für Sie."),
            ("Brauche ich eine Genehmigung für eine PV-Anlage?",
             "In Kärnten sind Anlagen auf Dächern und Fassaden meist nicht bewilligungspflichtig. Es gilt nur eine Meldepflicht. EBZ Energie klärt das für Ihr Projekt und kümmert sich um die Anmeldung."),
            ("Wie lange dauert die Amortisation?",
             "In der Praxis rechnen sich Anlagen von EBZ Energie meist innerhalb von 4 bis 6 Jahren, je nach Eigenverbrauch, Anlagengröße und Strompreis."),
        ]),
        C.linkgrid_section(
            "Photovoltaik in Ihrer Region",
            [("pv_villach", "Photovoltaik Villach"),
             ("pv_wolfsberg", "Photovoltaik Wolfsberg"),
             ("foerderung_kaernten", "Förderung Kärnten"),
             ("foerderung_steiermark", "Förderung Steiermark"),
             ("batteriespeicher", "Batteriespeicher"),
             ("waermepumpe", "Wärmepumpe"),
             ("eg_privat", "Energiegemeinschaft"),
             ("referenzen", "Referenzen")],
        ),
        C.contact_section(
            headline="Ihr kostenloses Angebot für Ihre Photovoltaikanlage",
            sub=("Sie erreichen uns telefonisch oder über das Formular. Wir zeigen Ihnen ehrlich, "
                 "was auf Ihrem Dach möglich ist und was es kostet. Kostenlos und unverbindlich."),
        ),
        # 9. Die einzige logische Handlung
        C.finalcta(
            "Bereit für Ihren eigenen Sonnenstrom?",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags "
            "und nehmen uns Zeit für Ihre Fragen.",
        ),
        _footnote(),
    ])

    faq = faq_jsonld(u(PATH), [
        ("Lohnt sich Photovoltaik in Oesterreich?",
         "Ja. Durch gestiegene Strompreise, Foerderungen und hohen Eigenverbrauch rechnet sich eine Anlage meist innerhalb von 4 bis 6 Jahren."),
        ("Was kostet eine Photovoltaikanlage mit Speicher?",
         "Eine Komplettanlage mit rund 10 kWp und Speicher liegt typischerweise bei rund 15.000 bis 22.000 Euro vor Foerderung."),
        ("Lohnt sich Photovoltaik auch fuer Betriebe?",
         "Ja, besonders. Betriebe verbrauchen viel Strom tagsueber, der hohe Eigenverbrauch senkt die Betriebskosten und die Anlage rechnet sich oft schneller."),
        ("Ist eine Photovoltaikanlage mit oder ohne Speicher besser?",
         "Mit Speicher nutzen Sie deutlich mehr Ihres Sonnenstroms selbst, weil Sie den Strom auch am Abend verwenden."),
        ("Wie lange dauert die Amortisation?",
         "Meist innerhalb von 4 bis 6 Jahren, je nach Eigenverbrauch, Anlagengroesse und Strompreis."),
    ])

    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq, include_business_schema=True,
                og_image="/assets/img/pv-hero-roof.jpg")
    return write_page("photovoltaik/index.html", html)


def _footnote():
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte auf Basis typischer Projekte, vor Förderung. Der tatsächliche
      Preis, die Ersparnis und die Amortisation hängen von Verbrauch, Anlagengröße, Ausrichtung
      und Strompreis ab. Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    build()
