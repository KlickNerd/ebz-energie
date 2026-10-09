"""Leistungsuebersicht (/leistungen/).

Uebersicht des EBZ-Systems: ein System, sechs Bausteine (wie auf der Startseite),
dazu Gewerbe, Carport und Finanzierung als weitere Einstiege. SEO/GEO-Ueberarbeitung
Oktober 2026 nach build/seo/leistungen.{json,md}: Primaer-Keyword "pv komplettanlage
mit speicher und montage", Komponentenliste (Hybrid-Wechselrichter, Speicher kWh),
Faustregeln (1 kWp je 1.000 kWh, 5 bis 6 m2 je kWp, 1 kWh je kWp), Foerderzahlen aus
dem Faktenblatt, Abgrenzung Selbstmontage-Set vs. Fachbetrieb. Die 10-kWp-Varianten
gehoeren dem Ratgeber /photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/
und werden nur verlinkt. Kompakt: 1.500 bis 2.000 Woerter.
"""

from common import IMG, NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, href, write_page, load_reviews
from layout import page
import components as C

PATH = "/leistungen/"
TITLE = "PV-Komplettanlage mit Speicher und Montage | EBZ Energie"
DESC = ("PV-Komplettanlage mit Speicher und Montage aus einer Hand: Photovoltaik, Speicher, Wärmepumpe, EMS, "
        "Energiegemeinschaft. 10 kWp mit Speicher ab rund 15.000 €.")

STAND = "Stand Oktober 2026"
KOMPLETT_10 = "/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/"

FAQ = [
    ("Welche Leistungen bietet EBZ Energie an?",
     "EBZ Energie plant und montiert komplette Energiesysteme: Photovoltaik, Batteriespeicher, Wärmepumpe, "
     "Energiemanagement, Energiegemeinschaft sowie Balkonkraftwerk und Wallbox. Dazu kommen Photovoltaik für "
     "Gewerbe, PV-Carports und eine Finanzierung mit Eigentum ab Tag 1."),
    ("Was kostet eine PV-Komplettanlage mit Speicher und Montage in Österreich?",
     "Bei EBZ Energie liegt der Richtpreis für 10 kWp mit Speicher bei rund 15.000 bis 22.000 Euro vor Förderung, "
     "schlüsselfertig inklusive Module, Hybrid-Wechselrichter, Speicher, Montagesystem, Elektroinstallation und "
     "Netzanmeldung; ohne Speicher sind es rund 10.000 bis 15.000 Euro. Das entspricht rund 1.500 bis 2.200 Euro je "
     "kWp inklusive Speicher*. Bund und Land Kärnten übernehmen 2026 bis zu rund 6.450 Euro davon."),
    ("Wie groß muss der Stromspeicher für ein Einfamilienhaus sein?",
     "Als Faustregel rund 1 kWh Speicherkapazität je kWp Modulleistung oder je 1.000 kWh Jahresverbrauch. Für ein "
     "Einfamilienhaus mit 4.000 bis 7.000 kWh sind das 5 bis 10 kWh; mit Wärmepumpe oder E-Auto eher 10 kWh. Ein "
     "Speicher hebt den Eigenverbrauch von rund 30 auf 60 bis 80 Prozent*. Die Auslegung machen wir anhand Ihres "
     "Lastprofils."),
    ("Wie viel kWp brauche ich für 4.000 oder 10.000 kWh Jahresverbrauch?",
     "Faustregel: rund 1 kWp je 1.000 kWh Jahresverbrauch, mindestens 5 kWp. Für 4.000 kWh passen 4 bis 5 kWp auf "
     "rund 25 bis 30 m² Dachfläche, für 10.000 kWh rund 10 kWp auf 50 bis 60 m² (5 bis 6 m² je kWp). Je kWp liefert "
     "eine Anlage in Kärnten und der Steiermark rund 1.000 kWh im Jahr (950 bis 1.100)*. Wer Wärmepumpe oder E-Auto "
     "plant, legt 2 bis 4 kWp drauf."),
    ("Wie lange dauert die Montage einer Komplettanlage?",
     "Die Montage einer 10-kWp-Komplettanlage mit Speicher dauert vor Ort 2 bis 3 Tage, ein Mehrfamilienhaus in "
     "Krumpendorf mit 25 kWp und 25 kWh war in 4 Tagen fertig. Von der Beratung bis zur Inbetriebnahme rechnen Sie "
     "mit 4 bis 8 Wochen, abhängig von Projektbericht, Förderantrag und Zählertausch durch den Netzbetreiber."),
    ("Gibt es 2026 noch Förderung für PV mit Speicher (EAG, Landespauschale)?",
     "Ja. Der EAG-Investitionszuschuss zahlt 150 Euro je kWp bis 10 kWp und 150 Euro je kWh Speicher, dazu 10 Prozent "
     "Made-in-Europe-Bonus; der dritte Fördercall läuft bis 22. Oktober 2026, ab 2027 plant der Bund laut BMWET eine "
     "Systemförderung mit Antrag nach der Installation. Kärnten zahlt 3.000 Euro Pauschale für Neuanlagen ab 5 kWp mit "
     "Speicher ab 5 kWh (Einreichung 12. Oktober bis 31. Dezember 2026). Wir bereiten die Anträge vor und behalten "
     "Fristen und Reihenfolge im Blick."),
    ("Komplettset zur Selbstmontage oder Fachbetrieb: was ist der Unterschied?",
     "Komplettsets aus dem Online-Shop (rund 1.300 bis 9.000 Euro*) enthalten Module, Wechselrichter und oft "
     "Speicher, aber keine Montage, keine Statik, keine Elektroinstallation und keine Netzanmeldung. Der Anschluss "
     "muss ohnehin ein Elektrofachbetrieb machen. Die Komplettanlage vom Fachbetrieb ist schlüsselfertig: "
     "Projektbericht mit 3D-Belegplan und Statikreport, dachschonende Montage, Anmeldung, Förderabwicklung und ein "
     "Ansprechpartner für Garantie und Service."),
    ("Muss ich alle sechs Bausteine auf einmal umsetzen?",
     "Nein. Die meisten Kundinnen und Kunden starten mit Photovoltaik und Speicher. Wärmepumpe, Wallbox oder "
     "Energiemanagement lassen sich später ergänzen. Wir planen von Anfang an so, dass spätere Bausteine "
     "sauber dazupassen, etwa mit einem Hybrid-Wechselrichter, der Speicher und Notstrom vorbereitet."),
    ("Wo montiert EBZ Energie?",
     "Der Montageschwerpunkt liegt in Kärnten und der Steiermark, von Villach über Klagenfurt bis Graz. "
     "Referenzprojekte gibt es in 6 Bundesländern, über 300 dokumentierte Anlagen."),
    ("Welche Garantien bekomme ich?",
     "Auf die Module bis zu 30 Jahre Leistungsgarantie und mindestens 10 Jahre Produktgarantie. Montiert wird "
     "von zertifizierten Fachkräften, mit dachschonender Montage auf Ersatzziegeln statt geflexten Originalziegeln."),
]


def _table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    body = ""
    for r in rows:
        tds = "".join(f'<td class="hl">{c}</td>' if i == 0 else f"<td>{c}</td>" for i, c in enumerate(r))
        body += f"<tr>{tds}</tr>"
    return f'<div class="art-tablewrap eg-reveal"><table class="art-table"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def _components_section():
    lead = ("Eine PV-Komplettanlage mit Speicher und Montage umfasst Module, Hybrid-Wechselrichter, Batteriespeicher, "
            "Montagesystem, Elektroinstallation und Netzanmeldung. Bei EBZ Energie kostet das Standardpaket mit 10 kWp "
            "und Speicher rund 15.000 bis 22.000 Euro vor Förderung, schlüsselfertig montiert in 2 bis 3 Tagen "
            f"(EBZ-Richtpreis, {STAND}).")
    rows = [
        ("PV-Module", "Glas-Glas bifazial, 22 bis 25 Module je 10 kWp", "bis zu 30 Jahre Leistungsgarantie, mind. 10 Jahre Produktgarantie"),
        ("Hybrid-Wechselrichter", "wandelt Gleichstrom in Hausstrom, lädt den Speicher, bereitet Notstrom vor", "Herzstück für spätere Bausteine"),
        ("Batteriespeicher", "5 bis 10 kWh, Faustregel 1 kWh je kWp", "Eigenverbrauch von rund 30 auf 60 bis 80 %*"),
        ("Montagesystem", "Aufdach auf Ziegel (mit Ersatzziegeln), Trapezblech, Blechfalz, Flachdach aufgeständert, Indach", "Statikreport für Wind- und Schneelast"),
        ("Elektroinstallation", "Zählerschrank, Überspannungsschutz, Inbetriebnahme", "Anmeldung beim Netzbetreiber inklusive"),
        ("Optional", "Energiemanagement, Wallbox, Wärmepumpe, Notstrom, Energiegemeinschaft", "von Anfang an mitgeplant"),
    ]
    table = _table(["Komponente", "Umfang", "Hinweis"], rows)
    return f"""
  <section class="section" style="background:#fff;border-block:1px solid var(--line)">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Photovoltaik Komplettanlage mit Speicher: die Komponenten</p>
      <h2 class="center eg-reveal">Was gehört zu einer PV-Komplettanlage mit Speicher?</h2>
      <p class="lead center eg-reveal" style="max-width:72ch;margin-inline:auto">{lead}</p>
      {table}
      <p class="form-note center eg-reveal">Alle Preise und die Förderrechnung für das 10-kWp-Paket:
      {a(KOMPLETT_10, "10 kWp Komplettanlage mit Speicher und Montage: Kosten")}.</p>
    </div>
  </section>"""


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        C.page_hero(
            eyebrow="PV Komplettanlage mit Speicher und Montage · Kärnten und Steiermark",
            h1="PV-Komplettanlage mit Speicher und Montage: ein System, sechs Bausteine von EBZ Energie",
            lead=("Photovoltaik, Speicher, Wärmepumpe, Energiemanagement, Energiegemeinschaft und Balkonkraftwerk: "
                  "Wir planen Ihr Energiesystem als Ganzes und montieren es schlüsselfertig mit zertifizierten "
                  "Fachkräften. Ein Ansprechpartner, von der Beratung über die Netzanmeldung bis zum Service."),
            cta=("kontakt", "Kostenlose Beratung"),
            cta2=("referenzen", "Referenzen ansehen"),
        ),
        C.kpis([
            ("300+", "dokumentierte Projekte"),
            (NAP["rating"], "Sterne auf Google"),
            ("bis zu 85 %", "weniger Energiekosten"),
            ("2 bis 3 Tage", "Montage für 10 kWp mit Speicher"),
        ]),
        _components_section(),
        C.text_block(
            eyebrow="Der EBZ Systemgedanke",
            h2="Wir denken in Systemen, nicht in Einzelteilen",
            paragraphs=[
                ("Module aufs Dach schrauben kann jeder. Der Unterschied liegt im Zusammenspiel: Die "
                 "Photovoltaikanlage liefert den Strom, der Speicher hebt ihn in den Abend, die Wärmepumpe heizt "
                 "damit, die Wallbox lädt das Auto, das Energiemanagement steuert alles und die Energiegemeinschaft "
                 "verwertet, was übrig bleibt."),
                ("Deshalb planen wir jedes Projekt von Anfang an als System, auch wenn Sie mit einem Baustein "
                 "starten. So passt der nächste Schritt später dazu, ohne Umbau. Das Ergebnis: bis zu 85 % weniger "
                 "Energiekosten und eine Anlage, die sich typischerweise in 4 bis 6 Jahren rechnet."),
            ],
        ),
        C.cards_section(
            eyebrow="Die sechs Bausteine",
            h2="Alle Leistungen: sechs Bausteine für Zuhause und Betrieb",
            intro=("Sie kombinieren, was zu Haus, Verbrauch und Budget passt. Jede Leistung hat eine eigene "
                   "Seite mit Zahlen, Ablauf und Förderung."),
            with_media=True,
            cards=[
                {"img": IMG["pv_card"], "alt": "Photovoltaikanlage auf einem Hausdach in Kärnten",
                 "title": "Photovoltaik",
                 "text": "Das Herzstück: Module, Hybrid-Wechselrichter und Montage, geplant für maximalen Eigenverbrauch. Richtpreis 10 kWp mit Speicher 15.000 bis 22.000 € vor Förderung.",
                 "link_key": "photovoltaik", "link_text": "Zur Photovoltaikanlage mit Speicher"},
                {"img": IMG["speicher"], "alt": "Batteriespeicher im Technikraum",
                 "title": "Batteriespeicher",
                 "text": "Sonnenstrom am Abend und in der Nacht nutzen statt mittags einspeisen und abends zurückkaufen. 5 bis 10 kWh, bis zu 80 % Eigenverbrauch, optional mit Notstrom.",
                 "link_key": "batteriespeicher", "link_text": "Zum Speicher"},
                {"img": IMG["waermepumpe"], "alt": "Wärmepumpe an einer Hauswand",
                 "title": "Wärmepumpe",
                 "text": "Heizen und Warmwasser mit dem eigenen Sonnenstrom statt mit Gas oder Öl. SG-Ready, damit das Energiemanagement sie bei Sonnenschein laufen lässt.",
                 "link_key": "waermepumpe", "link_text": "Zur Wärmepumpe"},
                {"img": IMG["ems"], "alt": "Energiemanagementsystem vernetzt Photovoltaik, Speicher, Wärmepumpe und Wallbox",
                 "title": "Energiemanagement",
                 "text": "Das Energiemanagementsystem (EMS) ist die Steuerzentrale: hebt Eigenverbrauch und Autarkie, nutzt dynamische Tarife und kappt im Gewerbe Lastspitzen. Bis 15. April 2027 mit 50 %, maximal 600 € gefördert.",
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
                 "text": "Stellplatz und Kraftwerk in einem: Das Carportdach erzeugt 3 bis 7 kWp, die Wallbox darunter lädt das Auto. Für Eigenheim und Firmenparkplatz.",
                 "link_key": "carport", "link_text": "Zum PV-Carport"},
                {"ic": "€", "title": "Finanzierung",
                 "text": "0 € Anzahlung, fixe Rate, Eigentum ab Tag 1 und volle Förderung. Komplettanlage inklusive Speicher: Finanzierung ab 147 €/Monat*.",
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
                    "Komplettanlage mit Speicher und Notstrom, meist 5 bis 10 kWp",
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
        C.facts_panel(
            eyebrow="Photovoltaikanlage mit Speicher Komplettpaket Österreich: Kosten und Förderung 2026",
            h2="Was kostet eine Komplettanlage mit Speicher und Montage?",
            intro=("Richtpreis, Preis je kWp und die Förderung 2026 auf einen Blick. Den Preis für Ihr Dach liefert "
                   "der Projektbericht mit 3D-Belegplan und Statikreport."),
            rows=[
                ("10 kWp mit Speicher", "rund 15.000 bis 22.000 € vor Förderung, schlüsselfertig"),
                ("10 kWp ohne Speicher", "rund 10.000 bis 15.000 € vor Förderung"),
                ("Preis je kWp", "rund 1.500 bis 2.200 €/kWp inklusive Speicher und Montage*"),
                ("EAG-Investitionszuschuss Bund", "150 €/kWp bis 10 kWp und 150 €/kWh Speicher, 10 % Made-in-Europe-Bonus; 3. Fördercall bis 22.10.2026"),
                ("Landesförderung Kärnten 3.000 €", "Pauschale für Neuanlagen ab 5 kWp mit Speicher ab 5 kWh, Einreichung 12.10. bis 31.12.2026; Steiermark: eigene Programme"),
                ("Summe Förderung Kärnten", "bis zu rund 6.450 € für 10 kWp + 10 kWh (Bund + Land)*"),
                ("Finanzierung", "0 € Anzahlung, fixe Rate, Eigentum ab Tag 1, ab 147 € im Monat inkl. Speicher*"),
                ("Ab 2027", "Systemförderung des Bundes geplant (laut BMWET): Antrag nach Installation, Höhe offen"),
            ],
            actions=[("10 kWp Komplettanlage: Kosten im Detail", KOMPLETT_10, ""),
                     ("Förderung 2026", href("foerderung_at"), "")],
        ),
        C.cards_section(
            eyebrow="Welche Größe passt?",
            h2="Welche Größe passt: Faustregeln für kWp, kWh und Dachfläche",
            intro=("Vier Richtwerte, mit denen Sie Ihr Projekt vorab einschätzen. Die Auslegung machen wir anhand "
                   "Ihres Lastprofils und Ihres Dachs.*"),
            cards=[
                {"ic": "☀", "title": "Faustregel 1 kWp je 1.000 kWh Jahresverbrauch",
                 "text": "4.000 kWh: 4 bis 5 kWp (mindestens 5 kWp empfohlen). 10.000 kWh: rund 10 kWp. Mit Wärmepumpe oder E-Auto 2 bis 4 kWp dazu."},
                {"ic": "⌂", "title": "5 bis 6 m² Dachfläche je kWp",
                 "text": "10 kWp brauchen 50 bis 60 m² oder 22 bis 25 Module. Ost-West-Dächer liefern etwas weniger je kWp, dafür gleichmäßiger über den Tag."},
                {"ic": "▮", "title": "1 kWh Speicher je kWp",
                 "text": "Oder 1 bis 1,5 kWh je 1.000 kWh Jahresverbrauch. Für ein Einfamilienhaus meist 5 bis 10 kWh; der Speicher hebt den Eigenverbrauch von rund 30 auf 60 bis 80 %."},
                {"ic": "◇", "title": "Rund 1.000 kWh Ertrag je kWp",
                 "text": "In Kärnten und der Steiermark 950 bis 1.100 kWh je kWp und Jahr. Referenz Villach: 10 kWp Ost-West, rund 11.000 kWh, etwa 80 % weniger Stromkosten.",
                 "link_key": "solarrechner", "link_text": "Zum PV-Rechner"},
            ],
        ),
        C.media_text(
            eyebrow="PV Anlage komplett mit Montage oder Komplettset zur Selbstmontage?",
            h2="Komplettset zur Selbstmontage oder Fachbetrieb: der Unterschied",
            paragraphs=[
                ("Online-Shops bieten PV-Komplettsets mit Speicher ab rund 1.300 bis 9.000 Euro* an. Enthalten sind "
                 "Module, Wechselrichter und Speicher, nicht enthalten sind Montage, Gerüst, Statik, "
                 "Elektroinstallation, Netzanmeldung und Förderabwicklung. Den Anschluss muss ohnehin ein "
                 "Elektrofachbetrieb machen, und Dachdichtheit sowie Garantiefälle bleiben Ihr Risiko."),
                ("Die Komplettanlage vom Fachbetrieb ist schlüsselfertig: Projektbericht mit 3D-Belegplan und "
                 "Statikreport, dachschonende Montage auf Ersatzziegeln, Inbetriebnahme, Anmeldung beim Netzbetreiber, "
                 "Förderanträge und ein Ansprechpartner für Garantie und Service. Für Betriebe mit eigenem Zählerschrank "
                 "und Statikfragen ist das der einzige praktikable Weg."),
            ],
            img=IMG["team_quer"],
            alt="Team von EBZ Energie, Fachbetrieb für Photovoltaik, Speicher und Wärmepumpe aus Villach",
            bullets=[
                "Schlüsselfertig: Planung, Montage, Elektrik, Anmeldung, Förderung",
                "Garantie und Service aus einer Hand, zertifizierte Fachkräfte",
                "Alle Komponenten aufeinander abgestimmt, auch für spätere Bausteine",
            ],
            cta=("kontakt", "Komplettanlage anfragen"),
        ),
        C.why_section(
            eyebrow="Darum EBZ",
            h2="Ihr Photovoltaik Anbieter aus der Region, nicht irgendein Shop",
            items=[
                ("☀", "Ein Ansprechpartner für alles", "Beratung, Planung, Montage, Förderung und Anmeldung beim Netzbetreiber aus einer Hand."),
                ("⌂", "Regionale Nähe", "Zuhause in Villach, im Einsatz in Kärnten und der Steiermark. Wir kennen Netzbetreiber und Landesförderungen."),
                ("✓", "Zertifizierte Fachkräfte", "Festangestelltes Team, meisterhaftes Handwerk und dachschonende Montage mit Ersatzziegeln statt geflexten Originalziegeln."),
                ("◇", "Komponenten mit Garantie", "Führende Hersteller, Leistungsgarantie bis 30 Jahre auf die Module, Produktgarantie 10 Jahre und mehr."),
                ("★", "4,9 Sterne auf Google", "Bewertungen von echten Kundinnen und Kunden aus der Region."),
                ("◎", "300+ Projekte", "Erfahrung aus über 300 dokumentierten Anlagen in 6 Bundesländern."),
            ],
        ),
        C.reviews_slider(reviews, rating, count),
        C.steps_section(
            eyebrow="Ablauf und Dauer",
            h2="Ablauf und Dauer: von der Beratung bis zur Netzanmeldung",
            steps=[
                ("Beratung und Besichtigung", "Wir beantworten Ihre Fragen, kommen vor Ort und erfassen Dach, Verbrauch und Ziele. Kostenlos und unverbindlich.", "Woche 1"),
                ("Projektbericht", "Sie erhalten ein Fixangebot samt Projektbericht mit 3D-Belegplan und Statikreport, inklusive Wind- und Schneelasten.", "1 bis 2 Wochen"),
                ("Förderung und Netzanmeldung", "Wir reichen die Förderungen ein, melden die Anlage beim Netzbetreiber an und behalten alle Fristen im Blick.", "parallel"),
                ("Montage und Inbetriebnahme", "Zertifizierte Fachkräfte montieren in 2 bis 3 Tagen und nehmen in Betrieb. Danach bleiben wir Ihr Ansprechpartner.", "4 bis 8 Wochen gesamt"),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section(
            "Weiterlesen",
            [(KOMPLETT_10, "10 kWp Komplettanlage mit Speicher und Montage: Kosten"),
             ("photovoltaik", "Photovoltaikanlage mit Speicher"),
             ("batteriespeicher", "Batteriespeicher"),
             ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage 2026"),
             ("/ab-wann-lohnt-sich-photovoltaik-mit-speicher/", "Ab wann lohnt sich PV mit Speicher?"),
             ("foerderung_at", "Förderung 2026"),
             ("solarrechner", "PV-Rechner"),
             ("pv_gewerbe", "Photovoltaik für Gewerbe"),
             ("finanzierung", "Finanzierung"),
             ("referenzen", "Referenzen")],
        ),
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
      <p class="form-note">*Richtwerte auf Basis typischer Projekte, vor Förderung: Preis je kWp aus dem EBZ-Richtpreis
      für 10 kWp mit Speicher, Faustregeln (1 kWp je 1.000 kWh, 5 bis 6 m² je kWp, 1 kWh Speicher je kWp, 950 bis 1.100 kWh
      Ertrag je kWp) aus unseren Ratgebern, Komplettset-Preise aus marktüblichen Online-Angeboten 2026. Finanzierungsrate als
      Beispielkondition, abhängig von Anlagengröße und Laufzeit. Fördersätze {STAND}, Änderungen durch Fördergeber vorbehalten.
      Ersparnis und Amortisation hängen von Verbrauch, Anlagengröße, Ausrichtung und Strompreis ab.
      Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import theme
    theme.write_assets()
    build()
