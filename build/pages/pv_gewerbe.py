"""Leistungsseite Photovoltaik fuer Gewerbe (/photovoltaik-gewerbe/).

Quelle: Live-Seite /photovoltaik-gewerbe/ (Elementor, 2023) plus Gewerbe-Sektion
aus build/photovoltaik.py. Bereinigt: "ohne Subunternehmer", Widmanngasse,
"Energieertrag-Berechnungen" (jetzt Projektbericht mit 3D-Belegplan und
Statikreport), "mehr als 100 Projekte" (jetzt 300+), Gedankenstriche.
Contracting-Modell der Live-Seite bewusst nicht uebernommen (Freigabe offen).
"""

from common import IMG, NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, S, faq_jsonld, u, a, href, tel_link, write_page, load_reviews
from layout import page
import components as C

PATH = "/photovoltaik-gewerbe/"
TITLE = "Photovoltaik Gewerbe: PV für Betriebe | EBZ Energie"
DESC = ("Photovoltaik für Gewerbe und Landwirtschaft in Kärnten und Steiermark: Planung nach "
        "Lastprofil, Speicher, EMS, Förderung. Referenz 40 kWp: 13.500 € im Jahr.")

FAQ = [
    ("Lohnt sich Photovoltaik für meinen Betrieb?",
     "In den meisten Fällen ja. Betriebe verbrauchen den Großteil ihres Stroms tagsüber, wenn die Anlage "
     "produziert. Dadurch liegt der Eigenverbrauch deutlich höher als im Privathaushalt und die Anlage "
     "rechnet sich oft schneller. Unsere Gewerbeanlage in Oberösterreich mit 40 kWp spart rund 13.500 Euro "
     "Stromkosten im Jahr, das Hotel in Villach/Warmbad mit 13 kWp rund 4.200 Euro bei etwa 6 Jahren Amortisation."),
    ("Wie groß sollte eine Gewerbe-PV-Anlage sein?",
     "Die Größe richtet sich nach Ihrem Lastprofil, nicht nur nach der Dachfläche. Wir analysieren, wann "
     "Ihr Betrieb wie viel Strom braucht, und legen die Anlage so aus, dass möglichst viel davon direkt "
     "verbraucht wird. Typische Gewerbeanlagen liegen zwischen 20 und 100 kWp, Hallen und Ställe auch darüber."),
    ("Was bringt ein Speicher im Gewerbe?",
     "Ein Speicher verschiebt Mittagsüberschüsse in den Nachmittag und Abend und fängt Lastspitzen ab. In "
     "Kombination mit einem Energiemanagementsystem senkt er den Leistungspreis und die Netzentgelte. Mit "
     "Notstromfunktion laufen Kühlung, Server oder Rezeption auch bei einem Netzausfall weiter."),
    ("Welche Förderung gibt es für Photovoltaik im Gewerbe?",
     "Der Bund fördert 2026 über den EAG-Investitionszuschuss: bis 20 kWp mit 140 Euro je kWp, über 20 bis "
     "100 kWp mit bis zu 130 Euro je kWp im Bieterverfahren, Speicher mit 150 Euro je kWh bis 50 kWh. "
     "Dazu kommen 10 Prozent Made-in-Europe-Bonus je Komponente. Für Energiemanagementsysteme gibt es für "
     "Betriebe 30 Prozent bis 20.000 Euro. Wir prüfen die passenden Programme und bereiten die Anträge vor."),
    ("Können Betriebe die Anlage auch finanzieren?",
     "Ja. Kauf oder Finanzierung stehen auch Betrieben offen. Bei der Finanzierung gehört die Anlage ab Tag 1 "
     "dem Unternehmen, mit fixer Rate, 0 Euro Anzahlung und kostenlosen Sondertilgungen. So bleibt die "
     "Liquidität im Betrieb und die Stromersparnis trägt die Rate mit."),
    ("Was passiert mit dem Überschuss am Wochenende?",
     "Überschüsse gehen entweder zum Marktpreis an die OeMAG oder Sie teilen sie in einer Energiegemeinschaft "
     "mit Gemeinde, Nachbarn oder anderen Betrieben. Im Nahbereich sinken dabei die Netzentgelte für den "
     "Bezug um bis zu 57 Prozent lokal und 28 Prozent regional, bei Mittelspannungsanschluss bis zu 64 Prozent."),
    ("Wie lange dauert die Montage einer Gewerbeanlage?",
     "Nach Beratung und Projektbericht mit 3D-Belegplan und Statikreport dauert die Montage je nach Größe wenige "
     "Tage bis zwei Wochen, abgestimmt auf Ihre Betriebszeiten. Netzanmeldung, Zählertausch und Förderabwicklung "
     "übernehmen wir."),
]


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        C.hero(
            eyebrow="Photovoltaik für Gewerbe und Landwirtschaft",
            h1="Photovoltaik für Ihren Betrieb: Strom produzieren, wenn Sie ihn brauchen",
            lead=("Betriebe verbrauchen den meisten Strom tagsüber, genau dann, wenn die Sonne scheint. "
                  "Wir planen Ihre Anlage nach Ihrem Lastprofil, montieren mit zertifizierten Fachkräften und "
                  "übernehmen Förderung und Netzanmeldung. Für Hallen, Höfe, Hotels und Werkstätten in Kärnten "
                  "und der Steiermark."),
            badges=[("Planung", "nach Lastprofil"),
                    ("Förderung", "inklusive Antrag"),
                    ("Speicher + EMS", "gegen Lastspitzen")],
            img=IMG["gewerbe_dach"],
            img_alt="Gewerbe-Photovoltaikanlage mit 40 kWp in Ost-West-Ausrichtung auf einem Trapezblechdach in Oberösterreich",
            float_num=rating,
            float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_secondary=("#referenzen", "Referenzen mit Zahlen"),
        ),
        C.kpis([
            ("13.500 €", "Ersparnis pro Jahr, Gewerbe OÖ (40 kWp)"),
            ("4.200 €", "Ersparnis pro Jahr, Hotel Villach (13 kWp)"),
            ("300+", "Projekte in 6 Bundesländern"),
            (NAP["rating"], "Sterne auf Google"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Warum Photovoltaik im Gewerbe anders rechnet als im Eigenheim",
            paragraphs=[
                ("Eine Gewerbe-Photovoltaikanlage erzeugt Strom in den Betriebszeiten: Maschinen, Kühlung, "
                 "Beleuchtung und Büro laufen dann, wenn die Module liefern. Dadurch wird ein großer Teil des "
                 "Sonnenstroms direkt verbraucht, statt für wenige Cent eingespeist zu werden."),
                ("Der Eigenverbrauch ist der entscheidende Hebel: Jede selbst genutzte Kilowattstunde ersetzt "
                 "teuren Netzbezug. Deshalb beginnt jede Planung bei EBZ Energie mit Ihrem Lastprofil, nicht mit "
                 "der Dachfläche."),
            ],
        ),
        C.audience_split(
            eyebrow="Für wen planen wir?",
            h2="Gewerbe, Landwirtschaft oder Hotellerie: Ihr Betrieb gibt die Auslegung vor",
            intro=("Jeder Betrieb hat ein anderes Verbrauchsmuster. Wir richten Modulbelegung, Speichergröße "
                   "und Steuerung genau danach aus."),
            left={
                "img": IMG["gen_gewerbe"],
                "alt": "Gewerbehalle mit großflächiger Photovoltaikanlage am Dach",
                "title": "Gewerbe und Produktion",
                "bullets": [
                    "Hoher Verbrauch Montag bis Freitag, tagsüber",
                    "Ost-West-Belegung streckt die Produktion über den Arbeitstag",
                    "Speicher und EMS kappen teure Lastspitzen",
                ],
                "cta": ("kontakt", "Beratung für meinen Betrieb"),
            },
            right={
                "img": IMG["gewerbe_dach"],
                "alt": "Trapezblechdach eines Betriebsgebäudes mit Photovoltaikmodulen",
                "title": "Landwirtschaft und Hotellerie",
                "bullets": [
                    "Große Dächer auf Hallen, Ställen und Scheunen",
                    "Verbrauch auch am Wochenende: Kühlung, Melktechnik, Gastronomie",
                    "Überschüsse in der Energiegemeinschaft teilen",
                ],
                "cta": ("kontakt", "Beratung für Hof oder Hotel"),
            },
        ),
        C.problem_compare(
            eyebrow="Zahlen statt Versprechen",
            h2="Weniger Netzbezug, planbare Betriebskosten",
            intro=("Strompreise sind ein Fixkostenblock, den Sie nicht verhandeln können. Mit eigener Anlage "
                   "produzieren Sie einen großen Teil selbst, zu Kosten, die über 25 Jahre feststehen."),
            bars=[
                ("Stromkosten ohne eigene Anlage", 100, "bad", "voller Netzbezug"),
                ("Stromkosten mit Photovoltaik und Speicher", 15, "good", "bis zu 85 % weniger*"),
            ],
            aside=("So holen wir den Eigenverbrauch hoch", [
                ("☀", "Lastprofil-Analyse", "Wir erfassen, wann Ihr Betrieb wie viel Strom braucht, und legen die Anlage darauf aus."),
                ("◇", "Ost-West statt Mittagsspitze", "Zwei Dachseiten liefern vom Morgen bis in den Abend, passend zu den Betriebszeiten."),
                ("▮", "Speicher für Abend und Spitzen", "Überschüsse vom Mittag decken Nachmittag, Abend und kurze Leistungsspitzen."),
                ("⚙", "Energiemanagement", "Das EMS steuert Speicher, Wallboxen und Wärmepumpe nach Produktion und Tarif."),
            ]),
        ),
        C.media_text(
            eyebrow="Lastspitzen und Leistungspreis",
            h2="Speicher und EMS: der zweite Hebel neben dem Eigenverbrauch",
            paragraphs=[
                ("Betriebe zahlen nicht nur für Kilowattstunden, sondern über den Leistungspreis auch für ihre "
                 "höchste Leistungsspitze. Ein Speicher mit Energiemanagementsystem glättet diese Spitzen: Wenn "
                 "mehrere Maschinen gleichzeitig anlaufen, liefert der Speicher den Mehrbedarf, statt dass er aus "
                 "dem Netz kommt."),
                ("Das EMS steuert zusätzlich Wallboxen für den Fuhrpark, die Wärmepumpe und große Verbraucher so, "
                 "dass sie bevorzugt mit Sonnenstrom laufen. Es liefert außerdem die Energiedaten, die Sie für "
                 "Energieaudits und ESG-Reporting brauchen."),
            ],
            img=IMG["ems"],
            alt="Energiemanagementsystem mit Visualisierung von Produktion, Speicher und Verbrauch",
            bullets=[
                "Lastspitzenmanagement senkt Leistungspreis und Netzentgelte",
                "Lademanagement für Fuhrpark und Ladeparks",
                "Notstrom für Kühlung, Server, Rezeption oder Melktechnik",
            ],
            reverse=True,
            cta=("ems", "Mehr zum Energiemanagement"),
        ),
        C.cards_section(
            eyebrow="Technik, die zu Betriebsdächern passt",
            h2="Komponenten für große Dächer und lange Laufzeiten",
            intro=("Betriebsdächer sind oft Trapezblech, Flachdach oder Bitumen. Wir wählen Module und "
                   "Unterkonstruktion passend zur Dachhaut und zur Statik."),
            cards=[
                {"ic": "☀", "title": "Glas-Glas-Module, bifazial",
                 "text": "Beidseitig aktive Module mit höherer Lebensdauer. Bis zu 30 Jahre Leistungsgarantie, mindestens 10 Jahre Produktgarantie."},
                {"ic": "◇", "title": "Ost-West-Belegung",
                 "text": "Verteilt die Produktion über den Arbeitstag statt einer Mittagsspitze. Mehr Eigenverbrauch bei gleicher Dachfläche."},
                {"ic": "⌂", "title": "Trapezblech, Flachdach, Bitumen",
                 "text": "Geklemmt oder aufgeständert, immer dachschonend und mit Statikreport belegt."},
                {"ic": "▮", "title": "Gewerbespeicher",
                 "text": "Von 20 bis 100 kWh und mehr, mit Notstromumschaltung über Gatewaybox.",
                 "link_key": "batteriespeicher", "link_text": "Zum Speicher"},
                {"ic": "⚡", "title": "Wallboxen und Ladeparks",
                 "text": "Firmenwagen und Kundenparkplatz laden mit eigenem Sonnenstrom, gesteuert vom EMS."},
                {"ic": "♨", "title": "Wärmepumpe im Betrieb",
                 "text": "Hallen, Büros und Warmwasser mit eigenem Strom heizen statt mit Gas oder Öl.",
                 "link_key": "waermepumpe", "link_text": "Zur Wärmepumpe"},
            ],
        ),
        C.media_text(
            eyebrow="Förderung für Betriebe",
            h2="Förderungen 2026: EAG-Zuschuss, EMS-Förderung und Wärmepumpe",
            paragraphs=[
                ("Der Bund fördert Photovoltaik über den EAG-Investitionszuschuss: Anlagen über 10 bis 20 kWp mit "
                 "140 Euro je kWp, über 20 bis 100 kWp mit bis zu 130 Euro je kWp im Bieterverfahren. Speicher "
                 "werden mit 150 Euro je kWh bis 50 kWh gefördert, europäische Komponenten bringen je 10 Prozent "
                 "Bonus."),
                ("Für Energiemanagementsysteme erhalten Betriebe 30 Prozent der Kosten, maximal 20.000 Euro je "
                 "Standort. Wichtig: Der Antrag muss vor der ersten verbindlichen Bestellung gestellt werden. Wir "
                 "halten die Reihenfolge ein und bereiten die Unterlagen vor."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Photovoltaik-Förderung für einen Betrieb",
            bullets=[
                a("foerderung_at", "PV-Förderung Österreich 2026: Sätze und Fördercalls"),
                a("/ems-foerderung/", "EMS-Förderung für Betriebe: 30 % bis 20.000 €"),
                a("/unternehmensfoerderung-von-waermepumpen/", "Wärmepumpen-Förderung für Betriebe"),
            ],
            cta=("kontakt", "Förderung für meinen Betrieb prüfen"),
            dark=True,
        ),
        C.media_text(
            eyebrow="Energiegemeinschaft für Betriebe",
            h2="Wochenendüberschuss wird zum zweiten Standbein",
            paragraphs=[
                ("Werktags verbraucht Ihr Betrieb den Sonnenstrom selbst. Am Wochenende, an Feiertagen und in der "
                 "Urlaubszeit liefert das Dach weiter. Statt diesen Überschuss zum OeMAG-Marktpreis einzuspeisen, "
                 "teilen Sie ihn in einer Energiegemeinschaft mit Gemeinde, Siedlung oder anderen Betrieben."),
                ("Im Nahbereich sinken die Netzentgelte für den Bezug aus der Gemeinschaft um bis zu 57 Prozent "
                 "lokal und 28 Prozent regional, bei Mittelspannungsanschluss bis zu 64 Prozent. Österreichweites "
                 "Teilen ist als Bürgerenergiegemeinschaft ebenfalls möglich, dann ohne Netzentgelt-Rabatt. Die "
                 "Abrechnung läuft über unseren Plattformpartner energyfamily."),
            ],
            img=IMG["eg_drohne"],
            alt="Luftaufnahme eines Ortes mit Photovoltaikdächern, Beispiel für eine lokale Energiegemeinschaft",
            bullets=[
                "Voraussetzung EEG: KMU bis 250 Mitarbeiter, sonst Bürgerenergiegemeinschaft",
                "Lastprofil-Analyse zeigt vorab Mengen und Erlöse",
                "Ihr Strom versorgt den Ort: regionales Marketing inklusive",
            ],
            reverse=True,
            cta=("eg_gewerbe", "Energiegemeinschaft für Betriebe"),
        ),
        C.media_text(
            eyebrow="Kauf oder Finanzierung",
            h2="Finanzierung auch für Betriebe: Liquidität bleibt im Unternehmen",
            paragraphs=[
                ("Viele Betriebe kaufen ihre Anlage direkt und sind typischerweise nach 4 bis 6 Jahren amortisiert. "
                 "Wer die Liquidität lieber im Betrieb behält, finanziert zur fixen Rate: 0 Euro Anzahlung, "
                 "Laufzeit bis 25 Jahre, Sondertilgungen jederzeit kostenlos."),
                ("In beiden Fällen gehört die Anlage ab Tag 1 Ihrem Unternehmen. Kein Mietmodell, kein "
                 "Eigentumsvorbehalt bis zur letzten Rate. Die Stromersparnis trägt die Rate in der Regel mit."),
            ],
            img=IMG["gen_detail"],
            alt="Montage von Photovoltaikmodulen durch Fachkräfte von EBZ Energie",
            bullets=[
                "Eigentum ab Tag 1, fixe Rate über die gesamte Laufzeit",
                "Digitale Finanzierungszusage in wenigen Minuten",
                "Förderung bleibt beim Betrieb",
            ],
            cta=("finanzierung", "Finanzierung ansehen"),
        ),
        C.why_section(
            eyebrow="Warum EBZ Energie",
            h2="Ihr Fachbetrieb für Gewerbeanlagen in Kärnten und der Steiermark",
            items=[
                ("☀", "Alles aus einer Hand", "Lastprofil-Analyse, Projektbericht, Montage, Netzanmeldung, Förderung und Service."),
                ("✓", "Zertifizierte Fachkräfte", "Elektrotechnik und Dachmontage aus einem Team, meisterhaftes Handwerk."),
                ("◎", "Kostenlose Besichtigung vor Ort", "Wir prüfen Dach, Statik und Zählerschrank bei Ihnen im Betrieb."),
                ("◉", "300+ Projekte", "Referenzen in 6 Bundesländern, vom Hof bis zur Produktionshalle."),
                ("★", "4,9 Sterne auf Google", "Bewertungen von Betrieben und Privatkunden aus der Region."),
                ("◷", "Service nach der Übergabe", "Monitoring, Wartung und Erweiterung: Wir bleiben Ihr Ansprechpartner."),
            ],
        ),
        C.reference_cards(
            eyebrow="Aus der Praxis",
            h2="Gewerbeanlage mit Zahlen: 40 kWp in Oberösterreich",
            intro=("Ein Projekt, das zeigt, was Planung nach Lastprofil bringt. Bild und Zahlen gehören "
                   "zum selben Projekt."),
            items=[
                {"img": IMG["gewerbe_dach"],
                 "alt": "Gewerbe-Photovoltaikanlage 40 kWp Ost-West auf Trapezblechdach in Oberösterreich",
                 "title": "Gewerbebetrieb, Oberösterreich",
                 "specs": "40 kWp Glas-Glas bifazial in Ost-West-Ausrichtung auf Trapezblech, 40 kWh Speicher, rund 40.000 kWh im Jahr.",
                 "result": "13.500 €", "result_sub": "Ersparnis pro Jahr"},
            ],
        ).replace('<section class="section">', '<section class="section" id="referenzen">', 1),
        C.facts_panel(
            eyebrow="Zweite Referenz: Hotellerie",
            h2="Hotel in Villach/Warmbad: Sonnenstrom für den 24-Stunden-Betrieb",
            intro=("Ein Hotel läuft rund um die Uhr. Die Anlage schaltet bei Netzausfall über eine Gatewaybox "
                   "automatisch auf Notstrom um."),
            rows=[
                ("Leistung", "13 kWp Glas-Glas bifazial, Südausrichtung auf Bitumen-Flachdach"),
                ("Speicher", "27 kWh mit automatischer Notstromumschaltung"),
                ("Eigenstrom", "rund 15.000 kWh im Jahr"),
                ("Ersparnis", "rund 4.200 € Stromkosten pro Jahr"),
                ("Amortisation", "rund 6 Jahre"),
                ("Garantie", "30 Jahre auf die Module, 15 Jahre auf Wechselrichter und Speicher"),
            ],
            actions=[("Alle Referenzen ansehen", href("referenzen"), "")],
        ),
        C.reviews_slider(reviews, rating=rating, count=count),
        C.steps_section(
            eyebrow="In vier Schritten zur Gewerbeanlage",
            h2="Von der Besichtigung bis zum laufenden Betrieb",
            steps=[
                ("Beratung und Besichtigung", "Wir erfassen Lastprofil, Dach, Statik und Netzanschluss vor Ort. Kostenlos und unverbindlich.", "Woche 1"),
                ("Projektbericht", "Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport sowie ein transparentes Angebot.", "1 bis 2 Wochen"),
                ("Förderung und Anmeldung", "Förderantrag vor der Bestellung, Netzanmeldung, Zählpunkte. Wir halten Fristen und Reihenfolge ein.", "parallel"),
                ("Montage und Übergabe", "Montage abgestimmt auf Ihre Betriebszeiten, Inbetriebnahme, Einschulung und Monitoring.", "wenige Tage"),
            ],
        ),
        C.founder_story(
            eyebrow="Ein Wort von Mario Zintl",
            h2="Gewerbeanlagen plane ich mit Ihnen am Tisch, nicht aus der Ferne",
            paragraphs=[
                ("Bei einem Betrieb geht es um mehr als um Module auf dem Dach. Es geht um Betriebszeiten, "
                 "Leistungsspitzen, Kühlung, die nicht ausfallen darf, und um eine Investition, die sich im "
                 "Jahresabschluss rechnen muss. Deshalb schaue ich mir jeden Betrieb selbst an."),
                ("Von der kostenlosen Besichtigung vor Ort bis zur Abwicklung aller Förderungen wickeln wir Ihr "
                 "PV-Projekt schlüsselfertig ab. Und wenn eine kleinere Anlage besser zu Ihrem Lastprofil passt, "
                 "sage ich Ihnen das genauso offen."),
            ],
            quote="Von der kostenlosen Besichtigung vor Ort bis zur Abwicklung aller Förderungen: Wir wickeln Ihr PV-Projekt schlüsselfertig ab.",
            name=AUTHOR, role=AUTHOR_ROLE,
            badge="Villach, Kärnten",
            cta=("kontakt", "Gewerbe-Beratung mit Mario Zintl"),
        ),
        C.faq_section(FAQ),
        C.linkgrid_section(
            "Weiterlesen für Betriebe",
            [("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
             ("eg_gewerbe", "Energiegemeinschaft für Betriebe"),
             ("ems", "Energiemanagementsystem"),
             ("batteriespeicher", "Batteriespeicher"),
             ("foerderung_at", "PV-Förderung Österreich 2026"),
             ("/ems-foerderung/", "EMS-Förderung"),
             ("/unternehmensfoerderung-von-waermepumpen/", "Wärmepumpen-Förderung für Betriebe"),
             ("finanzierung", "Finanzierung"),
             ("referenzen", "Referenzen")],
        ),
        C.contact_section(
            headline="Kostenlose Besichtigung für Ihren Betrieb",
            sub=("Wir kommen zu Ihnen, erfassen Lastprofil und Dach und sagen Ihnen ehrlich, was sich rechnet. "
                 "Für Gewerbe, Landwirtschaft und Hotellerie in Kärnten und der Steiermark."),
            page_label="Photovoltaik Gewerbe",
        ),
        C.finalcta(
            "Bereit für planbare Energiekosten in Ihrem Betrieb?",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags.",
            trust=[(f"{NAP['rating']} auf Google", True), ("300+ Projekte", False),
                   ("Besichtigung kostenlos", False), ("Förderung inklusive", False)],
        ),
        _footnote(),
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=IMG["gewerbe_dach"])
    return write_page("photovoltaik-gewerbe/index.html", html)


def _footnote():
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte auf Basis typischer Projekte, vor Förderung. Ersparnis und Amortisation
      hängen von Lastprofil, Anlagengröße, Ausrichtung und Strompreis ab. Referenzzahlen aus den dokumentierten
      Projekten Gewerbe Oberösterreich und Hotel Villach/Warmbad. Fördersätze Stand 2026, Änderungen durch
      Fördergeber vorbehalten. Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    build()
