"""Leistungsseite Photovoltaik-Carport (/photovoltaik-carport/).

Kompakte Seite (Ziel 1.000 bis 1.400 Woerter) aus dem alten Ratgeber-Beitrag.
Botschaft: Stellplatz wird zum Kraftwerk, Wallbox laedt mit Sonnenstrom, Statik
fuer Schnee- und Windlast in Oesterreich. Es gibt kein eigenes Carport-Foto,
Alt-Texte bleiben deshalb ehrlich (PV-Motive als Symbolbild).
Zahlen: Ertrag 950 bis 1.100 kWh je kWp, 2 Stellplaetze 30 bis 35 m2 = 5 bis 7 kWp
(aus dem Quellbeitrag), PV-Richtpreise und Foerderung aus den Ratgebern.
"""

from common import IMG, NAP, faq_jsonld, u, write_page, load_reviews
from layout import page
import components as C

PATH = "/photovoltaik-carport/"
TITLE = "Photovoltaik Carport: Solardach mit Wallbox | EBZ Energie"
DESC = ("Photovoltaik-Carport von EBZ Energie: 5 bis 7 kWp auf 2 Stellplätzen, Wallbox und Speicher, "
        "Statik für Schnee und Wind. Montage in Kärnten und der Steiermark.")

FAQ = [
    ("Brauche ich für ein Photovoltaik-Carport eine Baugenehmigung?",
     "In den meisten Gemeinden ist für einen Carport eine Bauanzeige oder Baubewilligung nötig, die Regeln "
     "unterscheiden sich je nach Bundesland und Gemeinde, etwa bei Abständen zum Nachbargrundstück. Wir klären "
     "die Vorgaben für Ihren Standort mit und liefern den statischen Nachweis für die Einreichung."),
    ("Wie viel Strom liefert ein Solarcarport?",
     "Ein Carport für zwei Stellplätze bietet 30 bis 35 Quadratmeter Dachfläche, darauf passen rund 5 bis 7 kWp. "
     "Je kWp sind in Österreich 950 bis 1.100 Kilowattstunden im Jahr üblich, also etwa 5.000 bis 7.500 kWh. "
     "Das reicht für ein E-Auto mit rund 15.000 Kilometern im Jahr und einen guten Teil des Haushaltsstroms."),
    ("Kann ich einen bestehenden Carport mit Photovoltaik nachrüsten?",
     "Grundsätzlich ja, wenn die Statik das Gewicht der Module und die höhere Windlast trägt. Ältere Carports "
     "sind dafür oft nicht ausgelegt. Eine statische Prüfung ist Pflicht, bevor Module montiert werden."),
    ("Funktioniert ein Photovoltaik-Carport im Winter?",
     "Ja, mit geringerer Leistung. Auch bei diffusem Licht produzieren die Module Strom. Entscheidend ist eine "
     "Konstruktion, die für die Schneelastzone Ihres Standorts ausgelegt ist. Die glatte Moduloberfläche "
     "begünstigt das Abrutschen des Schnees."),
    ("Was passiert mit Solarstrom, den ich nicht sofort brauche?",
     "Er lädt zuerst das E-Auto über die Wallbox oder den Batteriespeicher, der Rest fließt ins Netz und wird "
     "vergütet. Wirtschaftlich ist der Eigenverbrauch am besten, weil eine selbst genutzte Kilowattstunde 25 bis "
     "35 Cent Netzbezug ersetzt, die Einspeisung aber nur rund 6 Cent bringt."),
    ("Wie lange hält ein Photovoltaik-Carport?",
     "Konstruktionen aus Aluminium oder verzinktem Stahl halten 30 bis 40 Jahre und länger. Für die Module gilt "
     "bei EBZ Energie bis zu 30 Jahre Leistungsgarantie und mindestens 10 Jahre Produktgarantie, der "
     "Wechselrichter wird meist nach 15 bis 20 Jahren getauscht."),
]


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        C.hero(
            eyebrow="Photovoltaik-Carport für Eigenheim und Betrieb",
            h1="Photovoltaik-Carport: Ihr Stellplatz wird zum Kraftwerk",
            lead=("Ein Solarcarport schützt Ihre Fahrzeuge und erzeugt auf derselben Fläche Strom. Mit "
                  "Wallbox laden Sie Ihr E-Auto direkt mit Sonnenstrom, ein Speicher versorgt Haus und Auto "
                  "am Abend. EBZ Energie plant Konstruktion, Statik, Module und Ladetechnik aus einer Hand, "
                  "mit zertifizierten Fachkräften aus Villach."),
            badges=[("5 bis 7 kWp", "auf 2 Stellplätzen"),
                    ("Wallbox", "lädt mit Sonnenstrom"),
                    ("Statik", "für Schnee und Wind")],
            img=IMG["gen_hero"],
            img_alt="Photovoltaikmodule auf einem Dach, Symbolbild für ein Solardach über Stellplätzen",
            float_num=rating,
            float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_secondary=("#kosten", "Kosten ansehen"),
        ),
        C.kpis([
            ("5 bis 7 kWp", "auf 30 bis 35 m² Carportdach"),
            ("950 bis 1.100 kWh", "Ertrag je kWp und Jahr"),
            ("30 bis 40 Jahre", "Lebensdauer der Konstruktion"),
            (NAP["rating"], "Sterne auf Google"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Was ist ein Photovoltaik-Carport?",
            paragraphs=[
                ("Ein Photovoltaik-Carport (Solarcarport) ist ein Carport, dessen Dach aus Solarmodulen "
                 "besteht. Die Module sind Dacheindeckung und Stromerzeuger zugleich: Sie schützen die "
                 "Fahrzeuge vor Regen, Hagel und Schnee und liefern Gleichstrom, den ein Wechselrichter in "
                 "230-Volt-Wechselstrom für Haus, Wallbox und Speicher umwandelt."),
                ("Technisch arbeitet die Anlage wie eine Dachanlage. Der Unterschied liegt in der "
                 "Konstruktion: Sie muss das Modulgewicht sowie Schnee- und Windlast tragen und braucht "
                 "meist eine Bauanzeige bei der Gemeinde. Eine bereits versiegelte Fläche wird so doppelt "
                 "genutzt, ohne Garten oder Grünfläche zu verbauen."),
            ],
        ),
        C.cards_section(
            eyebrow="Das Komplettsystem",
            h2="Vier Bausteine, ein Ansprechpartner",
            intro=("Vom Fundament bis zur Ladesteuerung planen wir Ihr Carport als Ganzes und stimmen "
                   "die Bausteine aufeinander ab."),
            cards=[
                {"ic": "⌂", "title": "Konstruktion",
                 "text": ("Aluminium (wartungsfrei, witterungsbeständig), verzinkter Stahl (höchste "
                          "Tragfähigkeit) oder Leimholz (natürliche Optik, pflegeintensiver). Immer mit "
                          "statischem Nachweis für Ihre Schnee- und Windlastzone.")},
                {"ic": "☀", "title": "Module und Wechselrichter",
                 "text": ("5 bis 7 kWp auf zwei Stellplätzen. Hybridwechselrichter bereiten Speicher und "
                          "Notstrom vor, damit das System später wachsen kann."),
                 "link_key": "photovoltaik", "link_text": "Zur Photovoltaik"},
                {"ic": "⌖", "title": "Wallbox",
                 "text": ("PV-Überschussladen: Die Wallbox lädt bevorzugt dann, wenn das Dach mehr liefert als "
                          "das Haus braucht. So fahren Sie mit Strom für 10 bis 14 ct/kWh statt zu Tarifen "
                          "öffentlicher Ladesäulen.*")},
                {"ic": "▮", "title": "Speicher und Notstrom",
                 "text": ("5 bis 10 kWh Speicher laden das E-Auto auch nach Sonnenuntergang und halten bei "
                          "Stromausfall Kühlschrank, Router und Heizungspumpe am Netz."),
                 "link_key": "batteriespeicher", "link_text": "Zum Batteriespeicher"},
            ],
        ),
        C.media_text(
            eyebrow="Planung",
            h2="Statik zuerst: Schneelast und Windlast in Österreich",
            paragraphs=[
                ("Solarmodule bieten Wind eine große Angriffsfläche, und nasser Schnee wiegt viel. Die "
                 "Lastzonen unterscheiden sich in Österreich je nach Region erheblich: Ein Carport in einer "
                 "schneereichen Lage Oberkärntens braucht eine deutlich stärkere Auslegung als eines im "
                 "flachen Süden der Steiermark. Wir dimensionieren die Konstruktion nach der Lastzone Ihres "
                 "Standorts und liefern den Nachweis für die Bauanzeige."),
                ("Danach folgt die Anlagengröße: verfügbare Dachfläche, heutiger Stromverbrauch und das "
                 "geplante E-Auto. Als Faustregel liefert jedes kWp in Österreich 950 bis 1.100 kWh im Jahr. "
                 "Zwei Stellplätze mit 30 bis 35 m² tragen rund 5 bis 7 kWp, genug für ein E-Auto mit rund "
                 "15.000 Kilometern Jahresfahrleistung und einen guten Teil des Haushaltsstroms."),
            ],
            img=IMG["gen_detail"],
            alt="Fachkraft von EBZ Energie montiert Photovoltaikmodule auf einer Unterkonstruktion",
            bullets=[
                "Statischer Nachweis für Ihre Schnee- und Windlastzone",
                "Projektbericht mit 3D-Belegplan und Statikreport vor dem Auftrag",
                "Bauanzeige oder Bewilligung: Wir klären die Vorgaben Ihrer Gemeinde mit",
            ],
            reverse=True,
        ),
        C.price_cards(
            eyebrow="Photovoltaik-Carport Kosten",
            h2="Was kostet ein Photovoltaik-Carport?",
            intro=("Die Summe setzt sich aus Konstruktion, PV-Anlage und optional Speicher und Wallbox "
                   "zusammen. Für den PV-Teil gelten unsere Richtpreise, die Konstruktion hängt von "
                   "Material, Stellplätzen und Lastzone ab."),
            items=[
                {"size": "PV-Anlage auf dem Carport", "price": "ab ca. 9.000 €", "price_sub": "rund 5 kWp, ohne Speicher*",
                 "features": ["Module, Hybridwechselrichter, Elektroanschluss", "Anmeldung beim Netzbetreiber inklusive",
                              "Später um Speicher und Wallbox erweiterbar"]},
                {"size": "Speicher dazu", "price": "5.000 bis 9.000 €", "price_sub": "Aufpreis für 5 bis 10 kWh*",
                 "features": ["Eigenverbrauch von rund 30 auf 60 bis 80 Prozent", "E-Auto auch am Abend mit Sonnenstrom laden",
                              "Optional mit Notstromfunktion"]},
                {"size": "Konstruktion und Wallbox", "price": "individuell", "price_sub": "nach Material und Statik",
                 "features": ["Aluminium, Stahl oder Leimholz", "Ein oder mehrere Stellplätze, Lastzone Ihres Standorts",
                              "Wallbox mit PV-Überschussladen"]},
            ],
            note=("*Richtwerte für den Photovoltaik-Teil auf Basis typischer EBZ-Projekte, vor Förderung. Die "
                  "Carport-Konstruktion kalkulieren wir nach Vor-Ort-Termin im Festpreisangebot."),
        ).replace('<section class="section"', '<section id="kosten" class="section"', 1),
        C.media_text(
            eyebrow="Förderung und Finanzierung",
            h2="Der PV-Teil wird gefördert wie jede Dachanlage",
            paragraphs=[
                ("Für die Photovoltaikanlage auf dem Carport gilt 2026 der EAG-Investitionszuschuss des "
                 "Bundes: 150 € je kWp bis 10 kWp, 150 € je kWh Speicher und 10 Prozent Made-in-Europe-Bonus "
                 "je Komponente. Die Fördercalls 2026 starten am 23. April, 16. Juni und 8. Oktober, der Antrag "
                 "muss vor der Inbetriebnahme gestellt werden. In Kärnten kommen 3.000 € Landespauschale für "
                 "Neuanlagen mit Speicher dazu."),
                ("Die Carport-Konstruktion selbst ist nicht Teil der PV-Förderung. Wer die Investition nicht "
                 "auf einmal binden will, finanziert mit 0 € Anzahlung und fixer Rate. Die Anlage gehört Ihnen "
                 "dabei ab dem ersten Tag, die Förderung bleibt bei Ihnen."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Photovoltaik-Förderung am Tisch",
            bullets=[
                "Bund: 150 €/kWp und 150 €/kWh Speicher, plus Made-in-Europe-Bonus",
                "Kärnten: 3.000 € Pauschale für Neuanlagen mit Speicher",
                "Anträge und Fristen übernimmt EBZ Energie",
            ],
            cta=("foerderung_at", "Photovoltaik-Förderung 2026 im Detail"),
            dark=True,
        ),
        C.why_section(
            eyebrow="Warum EBZ Energie",
            h2="Ihr Partner für das Solarcarport in Kärnten und der Steiermark",
            items=[
                ("⌂", "Konstruktion und Anlage aus einer Hand", "Statik, Module, Wechselrichter, Wallbox und Speicher, abgestimmt in einem Projekt."),
                ("✓", "Zertifizierte Fachkräfte", "Meisterhaftes Handwerk, Elektroanschluss und Anmeldung beim Netzbetreiber inklusive."),
                ("★", "4,9 Sterne auf Google", "Bewertungen von Kundinnen und Kunden aus der Region."),
                ("◎", "300+ Projekte", "Erfahrung aus über 300 dokumentierten Anlagen in 6 Bundesländern."),
                ("€", "Förderung und Finanzierung", "Wir reichen ein und bieten die Finanzierung mit Eigentum ab Tag 1 an."),
                ("◷", "Ansprechbar nach der Übergabe", "Monitoring, Service und ein Team, das Sie erreichen."),
            ],
        ),
        C.reviews_slider(reviews, rating, count),
        C.steps_section(
            eyebrow="So läuft es ab",
            h2="Vom Stellplatz zum eigenen Kraftwerk",
            steps=[
                ("Beratung", "Stellplätze, Stromverbrauch, E-Auto und Standort. Kostenlos und unverbindlich.", ""),
                ("Planung", "Statik für Ihre Lastzone, Projektbericht mit 3D-Belegplan und Statikreport, Festpreis.", ""),
                ("Bauanzeige und Förderung", "Unterlagen für die Gemeinde, Förderantrag vor Inbetriebnahme.", ""),
                ("Montage", "Fundament, Konstruktion, Module, Wallbox und Speicher durch zertifizierte Fachkräfte.", ""),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section(
            "Weiterlesen",
            [("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
             ("batteriespeicher", "Batteriespeicher"),
             ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage"),
             ("foerderung_at", "Photovoltaik-Förderung Österreich 2026"),
             ("/notstrom/", "Notstrom mit Photovoltaik"),
             ("finanzierung", "Finanzierung"),
             ("referenzen", "Referenzen"),
             ("kontakt", "Kontakt")],
        ),
        C.contact_section(
            headline="Ihr Photovoltaik-Carport: Statik, Anlage und Festpreis in einem Angebot",
            sub=("Sagen Sie uns, wie viele Stellplätze Sie überdachen wollen und ob ein E-Auto geplant ist. "
                 "Wir prüfen Standort und Lastzone und sagen Ihnen ehrlich, was das Carport bringt und kostet."),
            page_label="Photovoltaik-Carport",
        ),
        C.finalcta(
            "Sonnenstrom tanken, wo das Auto ohnehin steht",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags.",
        ),
        _footnote(),
    ])

    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=IMG["gen_hero"])
    return write_page("photovoltaik-carport/index.html", html)


def _footnote():
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte auf Basis typischer EBZ-Projekte und unserer Ratgeber, vor Förderung.
      Ertrag 950 bis 1.100 kWh je kWp und Jahr ist ein österreichweiter Durchschnitt, Gestehungskosten für
      Solarstrom 10 bis 14 ct/kWh je nach Anlage. Konstruktion, Ertrag und Kosten hängen von Standort,
      Lastzone, Ausrichtung und Komponentenwahl ab. Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    import theme
    theme.write_assets()
    build()
