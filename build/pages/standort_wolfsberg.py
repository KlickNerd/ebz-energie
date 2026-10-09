"""Standortseite Photovoltaik Wolfsberg (/photovoltaik-wolfsberg/).

Kommerzieller Suchintent "photovoltaik wolfsberg". Quelle: Live-Seite
/photovoltaik-wolfsberg/ (WP-Beitrag, rund 3.000 Woerter), stark gekuerzt.
Bereinigt: "verbindliche Ertragsprognose" (jetzt Projektbericht mit 3D-Belegplan
und Statikreport), Gedankenstriche, Superlative, "historische Chance"-Rhetorik.
Kein Wolfsberg-Bild im Repo: generische Szenen mit ehrlichen Alt-Texten.
Die Quelle nennt keinen Lavanttal-Bezug und keinen Netzbetreiber, daher hier auch nicht.
"""

from common import IMG, NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, S, faq_jsonld, u, a, href, tel_link, write_page, load_reviews
from layout import page
import components as C

PATH = "/photovoltaik-wolfsberg/"
TITLE = "Photovoltaik Wolfsberg: PV mit Speicher | EBZ Energie"
DESC = ("Photovoltaik in Wolfsberg vom Kärntner Fachbetrieb: Planung vor Ort, Speicher, Notstrom, "
        "Förderung. Montage in 2 bis 4 Tagen, bis zu 80 % Eigenverbrauch.")

MAPS_URL = "https://www.google.com/maps/search/?api=1&query=Triglavstra%C3%9Fe+15%2C+9500+Villach"

FAQ = [
    ("Wie lange dauert die Installation einer PV-Anlage in Wolfsberg?",
     "Von der ersten Beratung bis zur Inbetriebnahme dauert es in der Regel wenige Wochen. Die Montage vor Ort "
     "ist meist in 2 bis 4 Tagen abgeschlossen. Die restliche Zeit braucht Planung, Materialbestellung und die "
     "Abstimmung mit dem Netzbetreiber."),
    ("Lohnt sich eine Photovoltaikanlage in Wolfsberg auch im Winter?",
     "Ja. Module arbeiten bei kalten Temperaturen sogar effizienter als bei großer Hitze. Über das Winterhalbjahr "
     "liefern Anlagen typischerweise 25 bis 30 Prozent des Jahresertrags."),
    ("Muss ich für meine PV-Anlage in Wolfsberg eine Baugenehmigung einholen?",
     "Für Anlagen auf bestehenden Gebäuden ist in Kärnten meist keine Baugenehmigung nötig, solange die Module "
     "parallel zur Dachfläche montiert werden. Es gilt eine Anzeigepflicht. Wir klären das für Ihr Projekt und "
     "stimmen uns bei Bedarf mit der Baubehörde der Gemeinde Wolfsberg ab."),
    ("Was kostet eine Photovoltaikanlage mit Speicher in Wolfsberg?",
     "Eine Komplettanlage mit rund 10 kWp und Speicher liegt typischerweise bei rund 15.000 bis 22.000 Euro vor "
     "Förderung. Das Land Kärnten zahlt 3.000 Euro Pauschale für private PV ab 5 kWp mit Speicher, der Bund "
     "150 Euro je kWp bis 10 kWp und 150 Euro je kWh Speicher."),
    ("Was ist der Unterschied zwischen Notstrom und Ersatzstrom?",
     "Notstrom versorgt bei Netzausfall einzelne Stromkreise, meist einphasig. Ersatzstrom trennt das ganze Haus "
     "vom Netz und baut ein Inselnetz auf, in dem auch dreiphasige Geräte laufen und die PV-Anlage den Speicher "
     "nachladen darf."),
    ("Welche Lebensdauer hat ein moderner Stromspeicher?",
     "Lithium-Eisenphosphat-Speicher (LFP) sind heute Standard. Hersteller garantieren meist 6.000 bis 10.000 "
     "Ladezyklen und mindestens 80 Prozent Restkapazität nach 10 bis 15 Jahren, im Einfamilienhaus also über "
     "20 Jahre Lebensdauer."),
    ("Was ist eine Energiegemeinschaft und wie profitiere ich in Wolfsberg davon?",
     "In einer Energiegemeinschaft teilen Nachbarn im Ort ihren erneuerbaren Strom. Überschüsse gehen an "
     "Mitglieder statt zum Marktpreis ins Netz. Im Nahbereich sinken die Netzentgelte für den Bezug um bis zu "
     "57 Prozent lokal und 28 Prozent regional."),
]

KAERNTEN = ["Wolfsberg", "Völkermarkt", "St. Veit an der Glan", "Klagenfurt",
            "Villach", "Feldkirchen", "Spittal an der Drau", "Hermagor"]
STEIERMARK = ["Deutschlandsberg", "Voitsberg", "Leibnitz", "Graz",
              "Weiz", "Murtal", "Leoben", "Südoststeiermark"]


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        C.hero(
            eyebrow="Photovoltaik Wolfsberg",
            h1="Photovoltaik in Wolfsberg: Planung vor Ort, Montage in wenigen Tagen",
            lead=("Gesunkene Anlagenpreise, der EAG-Investitionszuschuss und ausgereifte Speicher machen "
                  "den Einstieg in Wolfsberg so günstig wie lange nicht. EBZ Energie aus Villach plant Ihre "
                  "Anlage bei Ihnen vor Ort, montiert mit zertifizierten Fachkräften und übernimmt Förderung "
                  "und Netzanmeldung."),
            badges=[("2 bis 4 Tage", "Montage vor Ort"),
                    ("bis zu 80 %", "Eigenverbrauch mit Speicher"),
                    ("Förderung", "Kärnten und Bund inklusive")],
            img=IMG["gen_hero"],
            img_alt="Photovoltaikanlage auf einem Einfamilienhaus in Kärnten, Symbolbild für Anlagen in Wolfsberg",
            float_num=rating,
            float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_secondary=("#standort", "Standort und Kontakt"),
        ),
        C.kpis([
            ("2 bis 4 Tage", "Montage vor Ort"),
            ("bis zu 80 %", "Eigenverbrauch mit Speicher"),
            ("3.000 €", "Landespauschale Kärnten für PV mit Speicher"),
            (NAP["rating"], "Sterne auf Google"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Warum jetzt ein guter Zeitpunkt für Photovoltaik in Wolfsberg ist",
            paragraphs=[
                ("Drei Dinge kommen zusammen: Die Preise für Module und Wechselrichter sind in den letzten Jahren "
                 "deutlich gesunken, bei höherer Effizienz und Lebensdauer. Der Bund fördert über den "
                 "EAG-Investitionszuschuss direkt je kWp und je kWh Speicher. Und Speicher sind so ausgereift, "
                 "dass Sie Ihren Sonnenstrom rund um die Uhr nutzen."),
                ("Für Hausbesitzer in Wolfsberg und Umgebung heißt das: kürzere Amortisation, planbare "
                 "Stromkosten und ein Haus, das bei Netzausfall weiterläuft."),
            ],
        ),
        C.problem_compare(
            eyebrow="Eigenverbrauch ist der Hebel",
            h2="Ohne Speicher rund 30 %, mit Speicher bis zu 80 % Eigenverbrauch",
            intro=("Ohne Speicher nutzen Sie typischerweise nur etwa 30 Prozent Ihres Solarstroms selbst, weil "
                   "die meiste Energie mittags entsteht, wenn der Verbrauch im Haushalt gering ist. Der Rest geht "
                   "für wenige Cent ins Netz. Ein Speicher hebt den Eigenverbrauch auf bis zu 80 Prozent."),
            bars=[
                ("Eigenverbrauch ohne Speicher", 30, "bad", "rund 30 %*"),
                ("Eigenverbrauch mit Speicher", 80, "good", "bis zu 80 %*"),
            ],
            aside=("So planen wir Ihren Speicher", [
                ("▮", "LFP-Technologie", "Sicher, zyklenfest und langlebig: über 15 Jahre und tausende Ladezyklen."),
                ("◇", "Richtige Größe", "Zu klein puffert die Nacht nicht, zu groß kostet unnötig. Wir dimensionieren nach Verbrauch."),
                ("⚙", "Energiemanagement", "E-Auto und Wärmepumpe laufen bevorzugt mit Sonnenstrom."),
                ("✓", "Notstrom oder Ersatzstrom", "Einzelne Stromkreise oder das ganze Haus bei Netzausfall."),
            ]),
        ),
        C.media_text(
            eyebrow="Notstrom und Ersatzstrom",
            h2="Bei Stromausfall weiterlaufen: zwei Stufen der Absicherung",
            paragraphs=[
                ("Notstrom ist die Basisvariante: Bei Netzausfall versorgt der Speicher einzelne, vorher definierte "
                 "Steckdosen, etwa für Kühlschrank, Heizungssteuerung und Licht. Die Leistung ist meist auf eine "
                 "Phase beschränkt und die PV-Anlage schaltet aus Sicherheitsgründen ab."),
                ("Ersatzstrom trennt das ganze Haus vom Netz und baut ein eigenes Inselnetz auf. Alle Steckdosen "
                 "und auch dreiphasige Geräte laufen weiter, und die Anlage darf den Speicher nachladen. So "
                 "erzeugen Sie auch bei einem längeren Ausfall tagsüber Strom und füllen den Speicher für die Nacht."),
            ],
            img=IMG["speicher"],
            alt="Batteriespeicher mit Notstromfunktion im Technikraum eines Wohnhauses",
            bullets=[
                "Notstrom: einzelne Stromkreise, einphasig",
                "Ersatzstrom: ganzes Haus, dreiphasig, PV lädt den Speicher nach",
                "Wir klären in der Planung, welche Stufe zu Ihrem Haus passt",
            ],
            reverse=True,
            cta=("/notstrom/", "Ratgeber: Notstrom mit Photovoltaik"),
        ),
        C.media_text(
            eyebrow="Förderung in Wolfsberg",
            h2="EAG-Investitionszuschuss, Made-in-Europe-Bonus und Landespauschale Kärnten",
            paragraphs=[
                ("Der Bund fördert 2026 Photovoltaik bis 10 kWp mit 150 Euro je kWp und Speicher mit 150 Euro je "
                 "kWh. Wer europäische Module, Wechselrichter oder Speicher einsetzt, erhält je Komponente "
                 "10 Prozent Made-in-Europe-Bonus. Das Land Kärnten legt für private Anlagen ab 5 kWp mit Speicher "
                 "eine Pauschale von 3.000 Euro dazu."),
                ("Wir prüfen die passenden Programme für Ihr Projekt in Wolfsberg, halten die Fristen ein und "
                 "bereiten die Anträge vor."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Photovoltaik-Förderung für ein Eigenheim",
            bullets=[
                "150 €/kWp und 150 €/kWh vom Bund, 10 % Made-in-Europe-Bonus",
                "3.000 € Landespauschale Kärnten für PV mit Speicher",
                "Anträge und Netzanmeldung durch EBZ Energie",
            ],
            cta=("foerderung_kaernten", "PV-Förderung Kärnten 2026 im Detail"),
            dark=True,
        ),
        C.finance_band(),
        C.media_text(
            eyebrow="Planung und Montage",
            h2="Planung und Montage: das Fundament Ihrer Anlage in Wolfsberg",
            paragraphs=[
                ("Die Planung beginnt vor Ort in Wolfsberg: Wir prüfen Statik, Ausrichtung und Neigung des Dachs "
                 "und mögliche Verschattung durch Bäume, Kamine oder Nachbargebäude. Daraus entsteht Ihr "
                 "Projektbericht mit 3D-Belegplan und Statikreport, die Grundlage für ein ehrliches Angebot."),
                ("Zertifizierte Fachkräfte montieren mit einer Unterkonstruktion passend zur Dacheindeckung, "
                 "sturmsicher und dachschonend, und integrieren Wechselrichter und Speicher normgerecht in den "
                 "Zählerschrank. Nach der Inbetriebnahme schulen wir Sie in Anlage und Monitoring-App ein. "
                 "Fertigstellungsmeldung und Registrierung beim Netzbetreiber übernehmen wir."),
            ],
            img=IMG["gen_eigenheim"],
            alt="Einfamilienhaus mit Photovoltaikanlage in Kärnten, Symbolbild für Anlagen in Wolfsberg",
            bullets=[
                "Projektbericht mit 3D-Belegplan und Statikreport vor der Entscheidung",
                "Montage in 2 bis 4 Tagen, dachschonend und sturmsicher",
                "Anmeldung, Fertigstellungsmeldung und Förderung aus einer Hand",
            ],
            cta=("kontakt", "Planung für mein Haus anfragen"),
        ),
        C.why_section(
            eyebrow="Warum EBZ Energie",
            h2="Ihr Partner für Photovoltaik in Wolfsberg",
            items=[
                ("☀", "Alles aus einer Hand", "Beratung, Projektbericht, Montage, Förderung, Netzanmeldung und Service."),
                ("✓", "Zertifizierte Fachkräfte", "Elektrotechnik und Dachmontage aus einem Team, meisterhaftes Handwerk."),
                ("★", "4,9 Sterne auf Google", "Bewertungen von Kundinnen und Kunden aus Kärnten und der Steiermark."),
                ("◉", "300+ Projekte", "Erfahrung aus Projekten in Kärnten, der Steiermark und vier weiteren Bundesländern."),
                ("€", "Faire Finanzierung", "Eigentum ab Tag 1, 0 € Anzahlung, fixe Rate. Ab 147 € im Monat inklusive Speicher."),
                ("⌂", "Aus Kärnten", "Firmensitz in Villach, Beratung bei Ihnen vor Ort in Wolfsberg."),
            ],
        ),
        C.reference_cards(
            eyebrow="Aus der Praxis in Kärnten",
            h2="Anlagen, die sich rechnen. Mit Zahlen belegt.",
            intro="Bild und Zahlen gehören jeweils zum selben Projekt.",
            items=[
                {"img": IMG["ref_villach"],
                 "alt": "Photovoltaikanlage mit 10 kWp auf einem Einfamilienhaus in Villach",
                 "title": "Einfamilienhaus, Villach",
                 "specs": "10 kWp in Ost-West-Ausrichtung mit Notstrom, rund 11.000 kWh im Jahr.",
                 "result": "rund 80 %", "result_sub": "weniger Stromkosten"},
                {"img": IMG["ref_krumpendorf"],
                 "alt": "Photovoltaikanlage auf einem Mehrparteienhaus in Krumpendorf",
                 "title": "Mehrparteienhaus, Krumpendorf",
                 "specs": "25 kWp mit 25 kWh Speicher und Notstrom.",
                 "result": "4 Tage", "result_sub": "Bauzeit"},
                {"img": IMG["gewerbe_dach"],
                 "alt": "Gewerbe-Photovoltaikanlage 40 kWp auf Trapezblechdach in Oberösterreich",
                 "title": "Gewerbebetrieb, Oberösterreich",
                 "specs": "40 kWp Ost-West, 40 kWh Speicher, rund 40.000 kWh im Jahr.",
                 "result": "13.500 €", "result_sub": "Ersparnis pro Jahr"},
            ],
        ),
        C.founder_story(
            eyebrow="Persönliche Beratung vor Ort",
            h2="Mario Zintl kommt nach Wolfsberg, nicht nur sein Angebot",
            paragraphs=[
                ("Eine Anlage, die 25 Jahre und länger laufen soll, plant man nicht am Telefon. Deshalb kommen wir "
                 "zu Ihnen nach Wolfsberg, schauen uns Dach, Zählerschrank und Verbrauch an und hören zu, was Sie "
                 "vorhaben: E-Auto, Wärmepumpe, Notstrom oder einfach eine kleinere Stromrechnung."),
                ("Sie bekommen danach ein Angebot, das Sie verstehen. Wenn eine kleinere Anlage besser passt, sage "
                 "ich Ihnen das. Und nach der Montage bleiben wir erreichbar."),
            ],
            quote="Sie sollen nach dem Gespräch nicht überredet sein, sondern wissen, was Sie tun.",
            name=AUTHOR, role=AUTHOR_ROLE,
            badge="Villach, Kärnten",
            cta=("kontakt", "Beratungstermin in Wolfsberg"),
        ),
        C.facts_panel(
            eyebrow="Standort und Kontakt",
            h2="EBZ Energie: Firmensitz in Villach, Beratung bei Ihnen in Wolfsberg",
            intro=("Unser Firmensitz liegt in Villach. Für die Erstberatung kommen wir zu Ihnen nach Wolfsberg "
                   "und in die Umgebung, Besuche in Villach nach Terminvereinbarung."),
            rows=[
                ("Adresse", f"{NAP['name']}<br>{NAP['street']}, {NAP['zip']} {NAP['city']}"),
                ("Telefon", tel_link()),
                ("E-Mail", f'<a href="mailto:{NAP["email"]}">{NAP["email"]}</a>'),
                ("Öffnungszeiten", NAP["hours"]),
                ("Anfahrt", "Beratung und Besichtigung bei Ihnen vor Ort in Wolfsberg, kostenlos. Termine im Büro in Villach nach Vereinbarung."),
                ("Einzugsgebiet", "Wolfsberg und Umgebung, ganz Kärnten, Steiermark. Referenzen in 6 Bundesländern."),
            ],
            actions=[("Route zum Firmensitz", MAPS_URL, ' target="_blank" rel="noopener"'),
                     ("Anrufen", NAP["phone_href"], "")],
        ).replace('<section class="section"', '<section id="standort" class="section"', 1),
        C.regions_section(
            eyebrow="Einzugsgebiet",
            h2="Wolfsberg, Kärnten und die Steiermark",
            intro="Der Montageschwerpunkt liegt in Kärnten und der Steiermark, Referenzen gibt es österreichweit.",
            kaernten=KAERNTEN,
            steiermark=STEIERMARK,
            note="Referenzprojekte auch im Burgenland, in Niederösterreich, Oberösterreich und Wien.",
        ),
        C.reviews_slider(reviews, rating=rating, count=count),
        C.steps_section(
            eyebrow="So läuft es ab",
            h2="Von der Beratung in Wolfsberg bis zur Übergabe",
            steps=[
                ("Beratung vor Ort", "Wir analysieren Verbrauch, Dach und Ziele bei Ihnen in Wolfsberg. Kostenlos und unverbindlich.", ""),
                ("Projektbericht", "Projektbericht mit 3D-Belegplan und Statikreport sowie ein transparentes Angebot.", ""),
                ("Förderung und Anmeldung", "EAG-Zuschuss, Landespauschale Kärnten, Anzeige und Netzanmeldung: Wir bereiten alles vor.", ""),
                ("Montage und Übergabe", "Montage in 2 bis 4 Tagen, Inbetriebnahme, Einschulung in die Monitoring-App.", ""),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section(
            "Photovoltaik in Kärnten",
            [("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
             ("foerderung_kaernten", "PV-Förderung Kärnten 2026"),
             ("foerderung_at", "PV-Förderung Österreich 2026"),
             ("batteriespeicher", "Batteriespeicher"),
             ("/notstrom/", "Notstrom mit Photovoltaik"),
             ("eg_privat", "Energiegemeinschaft"),
             ("pv_villach", "Photovoltaik Villach"),
             ("referenzen", "Referenzen")],
        ),
        C.contact_section(
            headline="Ihr kostenloses Angebot für Photovoltaik in Wolfsberg",
            sub=("Sie erreichen uns telefonisch oder über das Formular. Wir kommen zu Ihnen nach Wolfsberg und "
                 "zeigen Ihnen ehrlich, was auf Ihrem Dach möglich ist. Kostenlos und unverbindlich."),
            page_label="Photovoltaik Wolfsberg",
        ),
        C.finalcta(
            "Bereit für Ihre eigene Energiezukunft in Wolfsberg?",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags und "
            "vereinbaren einen Termin bei Ihnen vor Ort.",
        ),
        _footnote(),
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=IMG["gen_hero"])
    return write_page("photovoltaik-wolfsberg/index.html", html)


def _footnote():
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte: Eigenverbrauchsquoten und Preise auf Basis typischer Einfamilienhäuser,
      vor Förderung. Ersparnis und Amortisation hängen von Verbrauch, Anlagengröße, Ausrichtung und Strompreis ab.
      Fördersätze Stand 2026, Änderungen durch die Fördergeber vorbehalten. Fachlich geprüft von Mario Zintl,
      Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    build()
