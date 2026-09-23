"""Leistungsseite Photovoltaik (/photovoltaik/).

Primaerkeyword: photovoltaik / pv anlage. Sekundaer: photovoltaik mit speicher,
photovoltaikanlage kosten, photovoltaik foerderung, photovoltaik module.
Lokal: Kaernten, Steiermark, Villach (verlinkt auf Detailseiten).
FAQ aus echten People-also-ask (Stand DataForSEO 2026-09).
"""

from common import CLAIMS, NAP, IMG, faq_jsonld, u, write_page
from layout import page
import components as C

PATH = "/photovoltaik/"
TITLE = "Photovoltaik Kärnten & Steiermark | PV-Anlage vom Fachbetrieb"
DESC = ("Photovoltaikanlage vom Fachbetrieb EBZ Energie: Planung, Montage und Service "
        "aus einer Hand in Kärnten und der Steiermark. Bis zu 85 % weniger Stromkosten, "
        "4,9 Sterne. Jetzt kostenlose Beratung.")


def build():
    body = "".join([
        C.hero(
            eyebrow="Photovoltaik in Kärnten und der Steiermark",
            h1="Photovoltaik vom Fachbetrieb: Ihr eigener Strom vom Dach",
            lead=("EBZ Energie plant und montiert Ihre Photovoltaikanlage passgenau für Dach, "
                  "Verbrauch und Budget. So senken Sie Ihre Stromkosten um bis zu 85 % und werden "
                  "unabhängiger von steigenden Preisen."),
            badges=[("4,9", "Sterne auf Google"),
                    ("300+", "Anlagen montiert"),
                    ("bis zu 30 Jahre", "Leistungsgarantie")],
            img=IMG["hero_home"],
            img_alt="Photovoltaikanlage von EBZ Energie auf einem Einfamilienhaus in Kärnten",
            float_num="4,9",
            float_label="aus 111 Google Bewertungen",
        ),
        C.kpis([
            ("300+", "dokumentierte Projekte"),
            (NAP["rating"], "Google Bewertung"),
            ("bis zu 85 %", "weniger Stromkosten"),
            ("4 bis 6 Jahre", "typische Amortisation"),
        ]),
        C.media_text(
            eyebrow="So funktioniert Photovoltaik",
            h2="Wie eine Photovoltaikanlage Ihren Strom erzeugt",
            paragraphs=[
                ("Eine Photovoltaikanlage wandelt Sonnenlicht direkt in elektrischen Strom um. "
                 "Die Module auf Ihrem Dach erzeugen Gleichstrom, der Wechselrichter macht daraus "
                 "nutzbaren Wechselstrom für Ihren Haushalt."),
                ("Was Sie nicht sofort verbrauchen, speichert ein Batteriespeicher für den Abend "
                 "oder wird ins Netz eingespeist. Ein Energiemanagementsystem sorgt dafür, dass "
                 "möglichst viel Ihres Sonnenstroms im eigenen Haus bleibt."),
            ],
            img=IMG["pv_card"],
            alt="Photovoltaikmodule auf einem Hausdach in Detailansicht",
            bullets=[
                "<b>Module:</b> erzeugen Strom aus Sonnenlicht, auch bei bewölktem Himmel",
                "<b>Wechselrichter:</b> wandelt den Strom für Ihren Haushalt um",
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
                 "link_key": "waermepumpe", "link_text": "Mehr erfahren"},
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
                ("Ohne Speicher nutzen Sie tagsüber nur einen Teil Ihres Sonnenstroms selbst. "
                 "Ein Batteriespeicher hebt Ihren Eigenverbrauch deutlich an: Sie laden den Speicher "
                 "am Tag und nutzen den Strom am Abend, wenn die Sonne nicht mehr scheint."),
                ("In Kombination mit einer Notstromfunktion bleibt Ihr Haus auch bei einem "
                 "Stromausfall versorgt. So holen Sie das Maximum aus Ihrer Anlage."),
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
        C.price_cards(
            eyebrow="Photovoltaik Kosten",
            h2="Was kostet eine Photovoltaikanlage?",
            intro=("Der Preis hängt von Anlagengröße, Dach und Speicher ab. Die folgenden "
                   "Richtwerte geben Ihnen eine erste Orientierung vor Förderung."),
            items=[
                {"size": "Kleine Anlage", "price": "ab ca. 9.000 €", "price_sub": "rund 5 kWp, ohne Speicher*",
                 "features": ["Ideal für kleinere Haushalte", "Hoher Eigenverbrauch am Tag", "Später um Speicher erweiterbar"]},
                {"size": "Beliebte Größe", "price": "15.000 bis 22.000 €", "price_sub": "rund 10 kWp mit Speicher*",
                 "features": ["Für das typische Einfamilienhaus", "Inklusive Batteriespeicher", "Optional mit Notstrom"]},
                {"size": "Gewerbe und große Dächer", "price": "individuell", "price_sub": "ab rund 20 kWp*",
                 "features": ["Für Betriebe und große Haushalte", "Hohe Ersparnis pro Jahr", "Planung nach Lastprofil"]},
            ],
            note="*Richtwerte auf Basis typischer Projekte, vor Förderung. Ihr genauer Preis kommt aus der kostenlosen Beratung.",
        ),
        C.finance_band(),
        C.media_text(
            eyebrow="Förderungen",
            h2="Förderungen sichern, Kosten senken",
            paragraphs=[
                ("Photovoltaik wird in Österreich gefördert: über Bundesmittel und über "
                 "Landesförderungen in Kärnten und der Steiermark. EBZ Energie kennt die aktuellen "
                 "Programme und unterstützt Sie bei den Anträgen."),
                ("So sichern Sie sich die Förderungen, die Ihnen zustehen, und verkürzen die Zeit "
                 "bis sich Ihre Anlage rechnet."),
            ],
            img=IMG["foerderung"],
            alt="Beratung zur Photovoltaik Förderung am Tisch",
            bullets=[
                "Bundesförderung für Photovoltaik und Speicher",
                "Landesförderungen in Kärnten und der Steiermark",
                "Unterstützung bei der Antragstellung",
            ],
            cta=("foerderung_at", "Förderungen im Überblick"),
        ),
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
            h2="Ihr Photovoltaik-Partner in der Region",
            items=[
                ("☀", "Alles aus einer Hand", "Planung, Montage, Anmeldung und Service. Ein Ansprechpartner für alles."),
                ("✓", "Zertifizierte Fachkräfte", "Meisterhaftes Handwerk und sorgfältige Ausführung bei jedem Projekt."),
                ("★", "4,9 Sterne auf Google", "Bewertungen von echten Kundinnen und Kunden aus der Region."),
                ("◉", "300+ Anlagen", "Erfahrung aus über 300 dokumentierten Projekten in 6 Bundesländern."),
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
            headline="Kostenlose Beratung für Ihre Photovoltaikanlage",
            sub=("Sie erreichen uns telefonisch oder über das Formular. Wir zeigen Ihnen ehrlich, "
                 "was auf Ihrem Dach möglich ist und was es kostet."),
        ),
        C.faq_section([
            ("Was kostet eine Photovoltaikanlage mit Speicher?",
             "Eine Komplettanlage mit rund 10 kWp und Speicher liegt typischerweise bei rund 15.000 bis 22.000 € vor Förderung. Der genaue Preis hängt von Dach, Speichergröße und Ausstattung ab."),
            ("Was kostet eine 10 kWp Anlage mit Speicher und Montage?",
             "Inklusive Montage bewegt sich eine 10 kWp Anlage mit Speicher meist im Bereich von rund 15.000 bis 22.000 € vor Förderung. In der kostenlosen Beratung erhalten Sie einen konkreten Preis für Ihr Dach."),
            ("Ist eine Photovoltaikanlage mit oder ohne Speicher besser?",
             "Mit Speicher nutzen Sie deutlich mehr Ihres Sonnenstroms selbst, weil Sie den Strom auch am Abend verwenden. Ein Speicher lohnt sich besonders, wenn Sie tagsüber wenig zu Hause sind oder Notstrom möchten."),
            ("Wie hoch ist die Förderung für Photovoltaik?",
             "Photovoltaik wird über Bundesmittel und über Landesförderungen in Kärnten und der Steiermark gefördert. Die Höhe hängt vom Programm und der Anlage ab. EBZ Energie unterstützt Sie bei den Anträgen."),
            ("Brauche ich eine Genehmigung für eine PV-Anlage?",
             "In Kärnten sind Anlagen auf Dächern und Fassaden meist nicht bewilligungspflichtig. Es gilt nur eine Meldepflicht. EBZ Energie klärt das für Ihr Projekt und kümmert sich um die Anmeldung."),
            ("Wie lange dauert die Amortisation?",
             "In der Praxis rechnen sich Anlagen von EBZ Energie meist innerhalb von 4 bis 6 Jahren, je nach Eigenverbrauch, Anlagengröße und Strompreis."),
        ]),
        C.finalcta(
            "Bereit für Ihre eigene Photovoltaikanlage?",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags.",
        ),
        _footnote(),
    ])

    faq = faq_jsonld(u(PATH), [
        ("Was kostet eine Photovoltaikanlage mit Speicher?",
         "Eine Komplettanlage mit rund 10 kWp und Speicher liegt typischerweise bei rund 15.000 bis 22.000 Euro vor Foerderung."),
        ("Ist eine Photovoltaikanlage mit oder ohne Speicher besser?",
         "Mit Speicher nutzen Sie deutlich mehr Ihres Sonnenstroms selbst, weil Sie den Strom auch am Abend verwenden."),
        ("Wie hoch ist die Foerderung fuer Photovoltaik?",
         "Photovoltaik wird ueber Bundesmittel und Landesfoerderungen in Kaernten und der Steiermark gefoerdert. EBZ Energie unterstuetzt bei den Antraegen."),
        ("Brauche ich eine Genehmigung fuer eine PV-Anlage?",
         "In Kaernten sind Anlagen auf Daechern meist nicht bewilligungspflichtig, es gilt nur eine Meldepflicht."),
        ("Wie lange dauert die Amortisation?",
         "Meist innerhalb von 4 bis 6 Jahren, je nach Eigenverbrauch, Anlagengroesse und Strompreis."),
    ])

    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq, include_business_schema=True,
                og_image="/assets/img/photovoltaik-anlage.jpg")
    return write_page("photovoltaik/index.html", html)


def _footnote():
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte auf Basis typischer Projekte. Der tatsächliche Preis, die
      Ersparnis und die Amortisation hängen von Verbrauch, Anlagengröße, Ausrichtung und
      Strompreis ab. Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    build()
