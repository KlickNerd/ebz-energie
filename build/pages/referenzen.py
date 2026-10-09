"""Referenzseite (/referenzen/): alle Projekte auf EINER Seite, keine Unterseiten.

Quellen der Projektzahlen: die alten WP-Projektseiten (/referenzen-alt/projekt-*) und
die alte Referenz-Uebersicht. Freigegebene Kernzahlen (CLAUDE.md, Abschnitt 9) bleiben
exakt so: Gewerbe OOe 40 kWp / 40 kWh / ~40.000 kWh / 13.500 EUR; EFH Villach 10 kWp
Ost-West, Notstrom, ~11.000 kWh, ~80 % weniger Stromkosten; MFH Krumpendorf 25 kWp +
25 kWh, Notstrom, 4 Tage Bauzeit; Hotel Warmbad 13 kWp bifazial, 27 kWh, ~15.000 kWh,
4.200 EUR/Jahr, ~6 Jahre.

SEO/GEO Oktober 2026 (build/seo/referenzen.json): Kennzahl-Tabelle ueber alle zehn Projekte am
Anfang (zitierbar), Abschnitt "Woran Sie eine serioese Photovoltaik-Firma erkennen" (SERP-Intent
"photovoltaik erfahrungen"), FAQ zu Montagedauer, Besichtigung und vermeidbaren Fehlern, Links zu
/batteriespeicher/, /notstrom/, /pv-speicher-nachruesten/, /ueber-uns/. Kein Baujahr: liegt in den
Projektdaten nicht vor.

Bereinigt gegenueber den Quelltexten: Formulierungen zur Ausfuehrung durch Dritte entfernt, keine Kundennamen
von Privatpersonen (nur Ort und Gebaeudetyp), keine Gedankenstriche.
Bilder liegen in build/static/img/ (ref-<slug>-<n>.jpg) und werden per copy_static kopiert.
"""

from common import IMG, NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

PATH = "/referenzen/"
TITLE = "Photovoltaik-Referenzen: 10 Anlagen mit echten Zahlen | EBZ"
DESC = ("Photovoltaik-Erfahrungen: 10 Referenzanlagen von EBZ Energie in Kärnten, Steiermark und "
        "4 weiteren Bundesländern, mit kWp, Speicher, Ertrag und Ersparnis.")

# Projektbilder (build/static/img/), Schluessel ref_villach/ref_krumpendorf/gewerbe_dach aus common.IMG
R = {
    "gewerbe_ooe_2": "/assets/img/ref-gewerbe-ooe-2.jpg",
    "hotel_1": "/assets/img/ref-hotel-villach-1.jpg",
    "hotel_2": "/assets/img/ref-hotel-villach-2.jpg",
    "bgld_1": "/assets/img/ref-landwirtschaft-bgld-1.jpg",
    "graz_stadthaus_1": "/assets/img/ref-stadthaus-graz-1.jpg",
    "graz_stadthaus_2": "/assets/img/ref-stadthaus-graz-2.jpg",
    "noe_1": "/assets/img/ref-bitumendach-noe-1.jpg",
    "wien_1": "/assets/img/ref-wien-1.jpg",
    "ossiach_1": "/assets/img/ref-ossiachersee-1.jpg",
    "graz_flach_1": "/assets/img/ref-flachdach-graz-1.jpg",
    # Galerie (aeltere Projekte aus der alten Referenz-Uebersicht)
    "g_faakersee_gh": "/assets/img/ref-faakersee-gaestehaus-1.jpg",
    "g_gaestehaus_see": "/assets/img/ref-gaestehaus-see-1.jpg",
    "g_keutschach": "/assets/img/ref-keutschach-1.jpg",
    "g_landskron": "/assets/img/ref-landskron-1.jpg",
    "g_blechfalz": "/assets/img/ref-blechfalz-garage-1.jpg",
    "g_faakersee_ow": "/assets/img/ref-faakersee-ostwest-1.jpg",
    "g_flach3": "/assets/img/ref-flachdach-3ausrichtungen-1.jpg",
    "g_axitec36": "/assets/img/ref-axitec-36-1.jpg",
    "g_ostwest_lfp": "/assets/img/ref-ostwest-eisenphosphat-1.jpg",
}

# Kennzahlen der zehn Projekte (identisch mit den Projektabschnitten unten).
# (anchor, Projekt, Dach/Ausrichtung, kWp, Speicher kWh, Ertrag kWh/Jahr, Ersparnis/Jahr*, Amortisation*, Extras)
TABLE = [
    ("gewerbe-oberoesterreich", "Gewerbebetrieb, Oberösterreich", "Trapezblech, Ost-West", "40", "40", "rund 40.000", "rund 13.500 €", "ca. 5 Jahre", "Sigenergy-Speicher"),
    ("hotel-villach-warmbad", "Hotel, Villach/Warmbad", "Bitumen-Flachdach, Süd", "13", "27", "rund 15.000", "rund 4.200 €", "ca. 6 Jahre", "Notstrom automatisch"),
    ("landwirtschaft-burgenland", "Landwirtschaft, Burgenland", "Bitumendach, Süd", "13", "27", "rund 15.000", "rund 4.200 €", "k. A.", "Notstrom automatisch"),
    ("einfamilienhaus-villach", "Einfamilienhaus, Villach", "Satteldach Bitumen, Ost-West", "10", "k. A.", "rund 11.000", "rund 80 % weniger Stromkosten", "k. A.", "Notstrom automatisch"),
    ("mehrparteienhaus-krumpendorf", "Mehrparteienhaus, Krumpendorf", "Ost-West", "25", "25", "k. A.", "k. A.", "k. A.", "Notstrom, Bauzeit 4 Tage"),
    ("stadthaus-graz", "Stadthaus, Graz", "3 Flachdächer ballastiert, Süd/Ost", "18", "18", "rund 20.000", "rund 5.000 €", "ca. 4 Jahre", "Wallbox 11 kW, Notstrom"),
    ("bitumendach-niederoesterreich", "Einfamilienhaus, Niederösterreich", "Bitumendach, Süd/West/Ost", "18", "16", "rund 18.000", "rund 4.400 €", "ca. 5,2 Jahre", "Notstrom"),
    ("wohnhaus-wien", "Wohnhaus, Wien", "Schindeldach, Süd/Ost", "10,92", "20", "rund 12.000", "rund 3.360 €", "ca. 6 Jahre", "Wallbox, my-PV Warmwasser, Notstrom"),
    ("einfamilienhaus-ossiachersee", "Einfamilienhaus, Ossiachersee", "Ziegeldach, Ost-West", "10", "9", "rund 11.000", "rund 3.200 €", "ca. 5,4 Jahre", "Wallbox 11 kW"),
    ("flachdach-graz", "Einfamilienhaus, Graz", "Flachdach ballastiert, Süd", "11,83", "20", "rund 13.000", "rund 3.500 €", "ca. 5 Jahre", "Wallbox 11 kW, Notstrom"),
]

FAQ = [
    ("Lohnt sich eine 10-kWp-Anlage mit Speicher für ein Einfamilienhaus?",
     "Die gezeigten Eigenheime sagen ja: Villach 10 kWp Ost-West mit rund 11.000 kWh und rund 80 % weniger "
     "Stromkosten*, Ossiachersee 10 kWp mit 9 kWh Speicher und rund 3.200 € Ersparnis* bei rund 5,4 Jahren "
     "Amortisation. Eine 10-kWp-Komplettanlage mit Speicher kostet rund 15.000 bis 22.000 € vor Förderung "
     "(Stand Oktober 2026)."),
    ("Wie lange hat die Montage bei den gezeigten Anlagen gedauert?",
     "Das Mehrparteienhaus in Krumpendorf (25 kWp, 25 kWh) war in vier Tagen montiert und in Betrieb. Bei "
     "Einfamilienhäusern dauert die Montage typischerweise 2 bis 4 Tage; eine Kundenbewertung auf Google nennt "
     "zwei Tage für die Module und zwei Tage für die Elektroinstallation. Dazu kommen Planung, Materialbestellung "
     "und die Abstimmung mit dem Netzbetreiber."),
    ("Woran erkenne ich einen seriösen Photovoltaik-Anbieter?",
     "An prüfbaren Firmendaten (EBZ Energie GmbH, FN 597101 s, Triglavstraße 15, Villach), an zertifizierten "
     "Fachkräften für die Montage, an einem Projektbericht mit 3D-Belegplan und Statikreport statt einem Pauschalangebot, an "
     "schriftlichen Garantien (bis zu 30 Jahre Leistungs-, mindestens 10 Jahre Produktgarantie), an Referenzen mit "
     "Zahlen wie auf dieser Seite und an echten Google-Bewertungen (4,9 Sterne)."),
    ("Kann ich eine Referenzanlage besichtigen oder mit einem Kunden sprechen?",
     "Fragen Sie uns. Wo Kundinnen und Kunden zustimmen, vermitteln wir gern ein Gespräch oder einen Blick auf eine "
     "Anlage in Ihrer Nähe, vor allem rund um Villach, am Wörthersee und am Ossiachersee. Aus Datenschutzgründen "
     "nennen wir auf dieser Seite nur Ort und Gebäudetyp."),
    ("Welche negativen Erfahrungen mit Photovoltaik lassen sich durch gute Planung vermeiden?",
     "Die drei häufigsten: eine falsch dimensionierte Anlage (Lösung: Planung nach gemessenem Verbrauch), ein "
     "undichtes Dach nach der Montage (Lösung: Ersatzziegel, Klemmen oder Ballast statt Bohrung, wie in Graz, Wien "
     "und am Ossiachersee) und verpasste Förderfristen (Lösung: Förderantrag und Netzanmeldung durch den Fachbetrieb)."),
    ("Wie schnell amortisieren sich die gezeigten Anlagen?",
     "Je nach Größe, Eigenverbrauch und Strompreis in der Regel innerhalb von 4 bis 6 Jahren. Das Stadthaus in "
     "Graz liegt bei rund 4 Jahren, das Hotel in Villach/Warmbad bei rund 6 Jahren. Bei bis zu 30 Jahren "
     "Leistungsgarantie auf die Module folgen danach viele Jahre günstiger Eigenstrom."),
    ("Woher stammen die Zahlen zu Ertrag und Ersparnis?",
     "Aus den Projektunterlagen der jeweiligen Anlage: Anlagenleistung, Speichergröße, Ausrichtung und der "
     "rechnerische Jahresertrag am Standort. Die Ersparnis ist ein Richtwert, der von Verbrauch, Strompreis "
     "und Wetter abhängt."),
]


# Anker der Uebersicht -> Slug der Detailseite (build/pages/referenz_projekte.py)
DETAIL = {
    "gewerbe-oberoesterreich": "projekt-gewerbe-oberoesterreich",
    "hotel-villach-warmbad": "projekt-pv-anlage-hotel-villach",
    "landwirtschaft-burgenland": "projekt-landwirtschaft-im-burgenland",
    "einfamilienhaus-villach": "projekt-einfamilienhaus-villach",
    "mehrparteienhaus-krumpendorf": "projekt-mehrparteienhaus-krumpendorf",
    "stadthaus-graz": "projekt-stadthaus-in-graz",
    "bitumendach-niederoesterreich": "projekt-bitumendach-in-niederoesterreich",
    "wohnhaus-wien": "projekt-pv-wien",
    "einfamilienhaus-ossiachersee": "projekt-pv-am-ossiachersee",
    "flachdach-graz": "projekt-flachdach-in-graz",
}


def _project(eyebrow, h2, paragraphs, img, alt, specs, reverse, anchor):
    cta = (f"/referenzen/{DETAIL[anchor]}/", 'Zum Projekt <span aria-hidden="true">→</span>') if anchor in DETAIL else None
    return C.media_text(eyebrow=eyebrow, h2=h2, paragraphs=paragraphs, img=img, alt=alt,
                        bullets=specs, reverse=reverse, anchor=anchor, cta=cta)


def _section_label(eyebrow, h2, text):
    return C.text_block(eyebrow, h2, [text], max_w="68ch")


def _table_section():
    rows = ""
    for anchor, name, dach, kwp, kwh, ertrag, ersparnis, amort, extras in TABLE:
        rows += (f'<tr><td class="hl"><a href="#{anchor}">{name}</a></td><td>{dach}</td><td>{kwp}</td>'
                 f'<td>{kwh}</td><td>{ertrag}</td><td>{ersparnis}</td><td>{amort}</td><td>{extras}</td></tr>')
    return f"""
  <section class="section" id="projekte" style="background:#fff;border-block:1px solid var(--line)">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Photovoltaik Referenzen mit Zahlen</p>
      <h2 class="center eg-reveal">Zehn Projekte, eine Tabelle: alle Kennzahlen auf einen Blick</h2>
      <p class="lead center eg-reveal" style="max-width:76ch;margin-inline:auto">Zehn dokumentierte
      Photovoltaik-Referenzen von EBZ Energie (Stand Oktober 2026): 10 bis 40 kWp, Speicher von 9 bis 40 kWh,
      Jahreserträge von rund 11.000 bis 40.000 kWh, Ersparnis rund 3.200 bis 13.500 € pro Jahr*, Amortisation
      rund 4 bis 6 Jahre. Alle Werte stammen aus den Projektunterlagen der jeweiligen Anlage, keine Hochrechnung.</p>
      <div class="art-tablewrap eg-reveal" style="margin-top:32px">
        <table class="art-table">
          <thead><tr><th>Projekt</th><th>Dach, Ausrichtung</th><th>kWp</th><th>Speicher kWh</th>
          <th>Ertrag kWh/Jahr</th><th>Ersparnis/Jahr*</th><th>Amortisation*</th><th>Extras</th></tr></thead>
          <tbody>{rows}</tbody>
        </table>
      </div>
      <p class="form-note center eg-reveal" style="margin-top:18px">*Richtwerte aus den Projektunterlagen,
      abhängig von Verbrauch, Strompreis und Wetter. k. A.: in den Projektdaten nicht erfasst. Bei Privatkunden
      nennen wir nur Ort und Gebäudetyp. Was „Photovoltaik Erfahrungsberichte“ und „PV Anlage Erfahrungen“ in
      Foren selten bieten: Zahlen je Anlage.</p>
    </div>
  </section>"""


def build():
    rating, count, reviews = load_reviews()
    bew = f"{count} Bewertungen" if count else "echten Bewertungen"
    body = "".join([
        C.page_hero(
            eyebrow="Photovoltaik Projekte und Referenzen",
            h1="Photovoltaik-Referenzen und Erfahrungen: 10 Anlagen von EBZ Energie mit Ertrag, Ersparnis und Amortisation",
            lead=("Von der 10-kWp-Dachanlage am Eigenheim bis zur 40-kWp-Gewerbeanlage: Hier sehen Sie, was "
                  "wir gebaut haben, mit Leistung, Speicher, Jahresertrag und Ersparnis. Geplant und montiert "
                  "von den freundlichen Energie-Handwerkern aus Villach, Montage in Kärnten und der Steiermark."),
            cta=("kontakt", "Kostenlose Beratung"),
            cta2=("#projekte", "Projekte ansehen"),
        ),
        C.kpis([
            (CLAIMS["projekte"], "dokumentierte Projekte"),
            ("6", "Bundesländer"),
            (NAP["rating"], f"Sterne auf Google, {bew}"),
            (CLAIMS["amortisation"], "typische Amortisation"),
        ]),
        _table_section(),

        # ---------------- Gewerbe, Hotel, Landwirtschaft ----------------
        _section_label(
            "Gewerbe und Betriebe",
            "Gewerbe und Landwirtschaft: wenn Erzeugung und Verbrauch zusammenfallen",
            ("Betriebe verbrauchen Strom, wenn die Sonne scheint. Deshalb rechnen sich Gewerbeanlagen oft am "
             "schnellsten: hoher Eigenverbrauch tagsüber, Speicher für Lastspitzen, Notstrom für alles, was nicht "
             "ausfallen darf."),
        ),
        _project(
            eyebrow="Gewerbe · Oberösterreich",
            h2="Gewerbebetrieb in Oberösterreich: 40 kWp auf Trapezblech",
            paragraphs=[
                ("Die größte Anlage in dieser Auswahl: 40 kWp bifaziale Glas-Glas-Module in Ost-West-Ausrichtung, "
                 "mit Klemmen direkt auf den Sicken des Trapezblechdachs befestigt. Die Ostfläche liefert am "
                 "Morgen, die Westfläche am Nachmittag und Abend, also über die gesamten Betriebszeiten."),
                ("Ein 40-kWh-Speicher fängt Überschüsse und Lastspitzen ab. Das Ergebnis: rund 40.000 kWh "
                 "Eigenstrom pro Jahr und etwa 13.500 € weniger Stromkosten jährlich*, über zehn Jahre rund "
                 "135.000 €. Mehr dazu: " + a("pv_gewerbe", "Photovoltaik für Betriebe") + "."),
            ],
            img=IMG["gewerbe_dach"],
            alt="Drohnenaufnahme der 40-kWp-Photovoltaikanlage in Ost-West-Ausrichtung auf dem roten Trapezblechdach eines Gewerbebetriebs in Oberösterreich",
            specs=[
                "Leistung: 40 kWp, Glas-Glas bifazial, Ost-West",
                "Speicher: 40 kWh, Sigenergy All-in-One-System",
                "Dach: Trapezblech, Klemmbefestigung ohne Bohrung",
                "Jahresertrag: rund 40.000 kWh",
                "Ersparnis: rund 13.500 € pro Jahr*, Amortisation ca. 5 Jahre (geschätzt)",
            ],
            reverse=False,
            anchor="gewerbe-oberoesterreich",
        ),
        _project(
            eyebrow="Hotel · Villach/Warmbad",
            h2="Hotel in Villach/Warmbad: 13 kWp mit 27 kWh und automatischem Notstrom",
            paragraphs=[
                ("Ein Hotel läuft rund um die Uhr: Rezeption, Aufzug, Kühlung, WLAN. Deshalb hat diese Anlage "
                 "einen besonders großen 27-kWh-Speicher und eine Gatewaybox, die bei Netzausfall in Sekunden "
                 "vollautomatisch auf " + a("/notstrom/", "Notstrom") + " umschaltet, ohne dass jemand eingreifen muss."),
                ("Die 13 kWp bifazialen Glas-Glas-Module sind auf dem Bitumen-Flachdach mit einer "
                 "K2-Unterkonstruktion in Südausrichtung aufgeständert, über zwei Neigungswinkel für die beste "
                 "Flächennutzung. Rund 15.000 kWh im Jahr, Amortisation in rund 6 Jahren."),
            ],
            img=R["hotel_1"],
            alt="Drohnenaufnahme des Hotels in Villach/Warmbad mit aufgeständerten Glas-Glas-Modulen in Südausrichtung auf dem Bitumen-Flachdach",
            specs=[
                "Leistung: 13 kWp, Glas-Glas bifazial, Süd mit 2 Neigungswinkeln",
                "Speicher: 27 kWh, Notstrom automatisch über Gatewaybox",
                "Dach: Bitumen-Flachdach, K2-Aufständerung",
                "Jahresertrag: rund 15.000 kWh",
                "Ersparnis: rund 4.200 € pro Jahr*, Amortisation ca. 6 Jahre",
            ],
            reverse=True,
            anchor="hotel-villach-warmbad",
        ),
        _project(
            eyebrow="Landwirtschaft · Burgenland",
            h2="Landwirtschaftlicher Betrieb im Burgenland: Versorgung, die nicht ausfallen darf",
            paragraphs=[
                ("Kühlung, Lüftung, Pumpen und Steuerungen müssen in der Landwirtschaft durchlaufen. Diese "
                 "Anlage kombiniert 13 kWp Glas-Glas-Module in Südausrichtung mit einem 27-kWh-Speicher und "
                 "einer Gatewaybox für die automatische Notstromversorgung."),
                ("Montiert wurde auf dem Bitumendach mit K2-Unterkonstruktion, in zwei Modulreihen und zwei "
                 "Neigungswinkeln. Rund 15.000 kWh Eigenstrom pro Jahr machen den Betrieb weitgehend unabhängig vom Netz."),
            ],
            img=R["bgld_1"],
            alt="Photovoltaikanlage in zwei Modulreihen auf dem Bitumenschindel-Dach eines landwirtschaftlichen Betriebs im Burgenland",
            specs=[
                "Leistung: 13 kWp, Glas-Glas bifazial, Süd mit 2 Neigungswinkeln",
                "Speicher: 27 kWh, Notstrom automatisch über Gatewaybox",
                "Dach: Bitumendach, K2-Unterkonstruktion",
                "Jahresertrag: rund 15.000 kWh, Ersparnis rund 4.200 € pro Jahr*",
            ],
            reverse=False,
            anchor="landwirtschaft-burgenland",
        ),

        # ---------------- Eigenheim und Wohnbau ----------------
        _section_label(
            "Eigenheim und Wohnbau",
            "Eigenheime und Mehrparteienhäuser: vom Satteldach bis zum Flachdach",
            ("Sieben Wohnprojekte aus Kärnten, der Steiermark, Niederösterreich und Wien, alle mit "
             + a("batteriespeicher", "Batteriespeicher") + " oder Notstrom, viele mit Wallbox: was ein Eigenheim "
             "mit 10 bis 25 kWp realistisch erreicht."),
        ),
        _project(
            eyebrow="Einfamilienhaus · Villach",
            h2="Einfamilienhaus in Villach: 10 kWp Ost-West mit Notstrom",
            paragraphs=[
                ("Ein klassisches Eigenheim-Projekt vor unserer Haustür: 10 kWp in Ost-West-Ausrichtung auf einem "
                 "Satteldach mit Bitumeneindeckung. Zwei Dachseiten liefern Strom von der Morgen- bis zur "
                 "Abendsonne, passend zum Tagesablauf einer Familie."),
                ("Mit automatischer Notstromumschaltung bleibt das Haus auch bei Netzausfall versorgt. Rund "
                 "11.000 kWh Jahresertrag decken im Sommer die komplette Pooltechnik, die Stromkosten sanken "
                 "um rund 80 %*."),
            ],
            img=IMG["ref_villach"],
            alt="Nahaufnahme der Photovoltaik-Module auf dem Ost-West-Satteldach eines Einfamilienhauses in Villach mit Bergen im Hintergrund",
            specs=[
                "Leistung: 10 kWp, Ost-West auf Satteldach (Bitumen)",
                "Notstrom: automatische Umschaltung",
                "Jahresertrag: rund 11.000 kWh",
                "Ergebnis: rund 80 % weniger Stromkosten*, Pool im Sommer zu 100 % versorgt",
            ],
            reverse=True,
            anchor="einfamilienhaus-villach",
        ),
        _project(
            eyebrow="Mehrparteienhaus · Krumpendorf am Wörthersee",
            h2="Mehrparteienhaus in Krumpendorf: 25 kWp und 25 kWh in vier Tagen",
            paragraphs=[
                ("Mehrere Wohneinheiten, ein gemeinsames Dach: Diese 25-kWp-Anlage in Ost-West-Lage versorgt das "
                 "Haus zusammen mit einem 25-kWh-Speicher auch nach Sonnenuntergang."),
                ("Die Notstromversorgung sichert die wichtigsten Verbraucher bei Netzausfall. Montage und "
                 "Inbetriebnahme dauerten vier Tage."),
            ],
            img=IMG["ref_krumpendorf"],
            alt="Drohnenaufnahme der 25-kWp-Photovoltaikanlage auf dem roten Dach eines Mehrparteienhauses in Krumpendorf",
            specs=[
                "Leistung: 25 kWp, Ost-West",
                "Speicher: 25 kWh mit Notstromversorgung",
                "Bauzeit: 4 Tage",
            ],
            reverse=False,
            anchor="mehrparteienhaus-krumpendorf",
        ),
        _project(
            eyebrow="Stadthaus · Graz",
            h2="Stadthaus in Graz: 18 kWp auf drei Flachdächern, amortisiert in rund 4 Jahren",
            paragraphs=[
                ("Drei getrennte Flachdächer, ein System: 18 kWp bifaziale Glas-Glas-Module in Süd- und "
                 "Ostausrichtung, aufgeständert und mit Betongewichten ballastiert, ganz ohne Dachdurchdringung. "
                 "Die Dachabdichtung bleibt unversehrt."),
                ("Dazu kommen ein 18-kWh-Speicher, eine 11-kW-Wallbox für das E-Auto und manuelle "
                 "Notstromumschaltung. Rund 20.000 kWh im Jahr bringen die Anlage in rund 4 Jahren ins Plus, "
                 "der schnellste Wert in dieser Auswahl."),
            ],
            img=R["graz_stadthaus_1"],
            alt="Aufgeständerte Glas-Glas-Module auf den begrünten Flachdächern eines Stadthauses in Graz, mit Betongewichten ballastiert",
            specs=[
                "Leistung: 18 kWp, Glas-Glas bifazial, Süd und Ost auf 3 Flachdächern",
                "Speicher: 18 kWh, Wallbox 11 kW, Notstrom manuell",
                "Montage: aufgeständert und ballastiert, keine Dachdurchdringung",
                "Jahresertrag: rund 20.000 kWh",
                "Ersparnis: rund 5.000 € pro Jahr*, Amortisation ca. 4 Jahre",
            ],
            reverse=True,
            anchor="stadthaus-graz",
        ),
        _project(
            eyebrow="Einfamilienhaus · Niederösterreich",
            h2="Neues Bitumendach in Niederösterreich: 18 kWp auf drei Dachflächen",
            paragraphs=[
                ("Süd, West und Ost: Die Module verteilen sich auf drei Dachflächen eines frisch eingedeckten "
                 "Bitumendachs. Die Produktion beginnt im Osten, läuft über den Süden und endet im Westen, ein "
                 "gleichmäßiger Verlauf statt einer Mittagsspitze."),
                ("Ein 16-kWh-Speicher und die manuelle Notstromumschaltung sorgen für Strom am Abend und bei "
                 "Netzausfall. Rund 18.000 kWh Jahresertrag, Amortisation in rund 5,2 Jahren."),
            ],
            img=R["noe_1"],
            alt="Drohnenaufnahme eines Einfamilienhauses in Niederösterreich mit Photovoltaik-Modulen in Süd-, West- und Ostausrichtung auf dem neuen Bitumendach",
            specs=[
                "Leistung: 18 kWp, Glas-Glas bifazial, Süd, West und Ost",
                "Speicher: 16 kWh, Notstrom manuell",
                "Dach: neues Bitumendach",
                "Jahresertrag: rund 18.000 kWh",
                "Ersparnis: rund 4.400 € pro Jahr*, Amortisation ca. 5,2 Jahre",
            ],
            reverse=False,
            anchor="bitumendach-niederoesterreich",
        ),
        _project(
            eyebrow="Wohnhaus · Wien",
            h2="Wohnhaus in Wien: 10,92 kWp mit 20 kWh, Wallbox und Warmwasser aus Überschuss",
            paragraphs=[
                ("Die vollständigste Ausstattung in dieser Auswahl: 10,92 kWp Glas-Glas-Module in Süd- und "
                 "Ostausrichtung auf einem Schindeldach, befestigt über Ersatzziegel mit integrierter Halterung."),
                ("Ein 20-kWh-Speicher, eine 11-kW-Wallbox, ein my-PV-Regler, der Überschuss stufenlos in warmes "
                 "Wasser verwandelt, und manuelle Notstromumschaltung greifen ineinander. Rund 12.000 kWh im Jahr, "
                 "Amortisation in rund 6 Jahren."),
            ],
            img=R["wien_1"],
            alt="Drohnenaufnahme eines Wohnhauses in Wien mit Photovoltaik-Modulen in Süd- und Ostausrichtung auf dem Schindeldach",
            specs=[
                "Leistung: 10,92 kWp, Glas-Glas bifazial, Süd und Ost",
                "Speicher: 20 kWh, Wallbox 11 kW, Notstrom manuell",
                "Warmwasser: my-PV aus PV-Überschuss",
                "Jahresertrag: rund 12.000 kWh",
                "Ersparnis: rund 3.360 € pro Jahr*, Amortisation ca. 6 Jahre",
            ],
            reverse=True,
            anchor="wohnhaus-wien",
        ),
        _project(
            eyebrow="Einfamilienhaus · Ossiachersee",
            h2="Einfamilienhaus am Ossiachersee: 10 kWp Ost-West mit Wallbox",
            paragraphs=[
                ("Sonnenstrom mit Seeblick: 10 kWp bifaziale Glas-Glas-Module in Ost-West-Ausrichtung auf einem "
                 "Bramac-Ziegeldach. Für die Befestigung wurden einzelne Ziegel durch Marzari-Ersatzziegel mit "
                 "Halterung getauscht, regensicher und unauffällig."),
                ("Ein 9-kWh-Speicher und eine 11-kW-Wallbox laden Haus und E-Auto mit eigenem Strom. Rund "
                 "11.000 kWh im Jahr, Amortisation in rund 5,4 Jahren."),
            ],
            img=R["ossiach_1"],
            alt="Einfamilienhaus am Ossiachersee mit Photovoltaik-Modulen auf dem Ziegeldach, umgeben von Bäumen",
            specs=[
                "Leistung: 10 kWp, Glas-Glas bifazial, Ost-West",
                "Speicher: 9 kWh, Wallbox 11 kW",
                "Dach: Bramac-Ziegel mit Marzari-Ersatzziegeln",
                "Jahresertrag: rund 11.000 kWh",
                "Ersparnis: rund 3.200 € pro Jahr*, Amortisation ca. 5,4 Jahre",
            ],
            reverse=False,
            anchor="einfamilienhaus-ossiachersee",
        ),
        _project(
            eyebrow="Einfamilienhaus · Graz",
            h2="Flachdach in Graz: 11,83 kWp ballastiert, ohne eine einzige Bohrung",
            paragraphs=[
                ("Auf dem Sarnafil-Flachdach dieses Einfamilienhauses stehen zwei Modulfelder mit zusammen "
                 "11,83 kWp in Südausrichtung. Das Montagesystem ist komplett ballastiert, die Folie bleibt "
                 "unversehrt und zu 100 % dicht."),
                ("Mit 20-kWh-Speicher, 11-kW-Wallbox und manueller Notstromumschaltung ist das Haus weitgehend "
                 "unabhängig. Rund 13.000 kWh im Jahr, Amortisation in rund 5 Jahren."),
            ],
            img=R["graz_flach_1"],
            alt="Drohnen-Draufsicht auf zwei Modulfelder der 11,83-kWp-Photovoltaikanlage auf dem Flachdach eines Einfamilienhauses in Graz mit Pool im Garten",
            specs=[
                "Leistung: 11,83 kWp, Glas-Glas bifazial, Süd",
                "Speicher: 20 kWh, Wallbox 11 kW, Notstrom manuell",
                "Montage: Sarnafil-Flachdach, ballastiert, keine Dachdurchdringung",
                "Jahresertrag: rund 13.000 kWh",
                "Ersparnis: rund 3.500 € pro Jahr*, Amortisation ca. 5 Jahre",
            ],
            reverse=True,
            anchor="flachdach-graz",
        ),

        # ---------------- Galerie ----------------
        C.gallery(
            eyebrow="Weitere Projekte",
            h2="Noch mehr umgesetzte Anlagen",
            intro=("Ein Auszug weiterer Photovoltaikanlagen aus Kärnten, privat wie gewerblich, vom Ziegeldach bis "
                   "zum Blechdach. Die Bildunterschrift nennt die wichtigsten Daten."),
            items=[
                (R["g_faakersee_gh"], "Orangefarbenes Gästehaus am Faakersee mit Glas-Glas-Modulen auf dem roten Dach",
                 "Gästehaus am Faakersee: 14,62 kWp Glas-Glas, Speicher, Warmwasser aus Überschuss"),
                (R["g_gaestehaus_see"], "Glas-Glas-Module auf dem Ziegeldach eines Gästehauses an einem Kärntner See, Kirchturm im Hintergrund",
                 "Gästehaus an einem Kärntner See: 15 kWp Ost-West, 13,8 kWh Speicher, Wallbox"),
                (R["g_keutschach"], "Drohnen-Draufsicht auf Photovoltaik-Module auf dem Ziegeldach eines Hauses am Keutschacher See",
                 "Keutschacher See: 11 kWp Ost-West, 20 kWh Speicher, Wallbox"),
                (R["g_landskron"], "Einfamilienhaus in Landskron mit Photovoltaik-Modulen um die Dachfenster auf dem Ziegeldach",
                 "Landskron: 20 kWp Süd, 28 kWh Speicher"),
                (R["g_blechfalz"], "Photovoltaik-Module auf dem Blechfalzdach einer Garage mit Bergblick",
                 "Garage mit Blechfalzdach in Kärnten: 16 kWp, 16 kWh Speicher, Notstrom"),
                (R["g_faakersee_ow"], "Drohnen-Draufsicht auf drei Modulfelder auf einem Ziegeldach beim Faakersee",
                 "Beim Faakersee: Ost-West-Anlage mit Ersatzstrom und Ersatzziegeln"),
                (R["g_flach3"], "Aufgeständerte Module auf einem Flachdach mit Pool und Bergpanorama in Kärnten",
                 "Flachdach mit 3 Ausrichtungen: 15 kWp, 10 kWh Speicher, Warmwasser aus Überschuss"),
                (R["g_axitec36"], "Photovoltaik-Module auf einem Stehfalz-Blechdach mit Blick auf die Karawanken",
                 "Stehfalz-Blechdach: 36 Glas-Glas-Module mit Optimierern, 16,4 kWh Speicher, Autoladestation"),
                (R["g_ostwest_lfp"], "Einfamilienhaus mit Holzbalkon und Photovoltaik-Modulen auf beiden Dachseiten im Abendlicht",
                 "Ost-West optimiert: 12,04 kWp, 14,2 kWh Eisenphosphat-Speicher"),
            ],
        ),
        C.gallery(
            eyebrow="Blick aufs Dach",
            h2="Drei Projekte aus der Luft",
            intro="Modulfelder, Aufständerung und Kabelführung aus der Vogelperspektive.",
            items=[
                (R["gewerbe_ooe_2"], "Drohnen-Draufsicht auf die zwei Modulfelder in Ost-West-Ausrichtung auf dem Trapezblechdach des Gewerbebetriebs in Oberösterreich",
                 "Oberösterreich: 40 kWp Ost-West auf Trapezblech"),
                (R["hotel_2"], "Drohnen-Draufsicht auf die Modulreihen auf dem Flachdach des Hotels in Villach/Warmbad",
                 "Villach/Warmbad: 13 kWp mit zwei Neigungswinkeln"),
                (R["graz_stadthaus_2"], "Aufgeständerte Module auf dem begrünten Flachdach des Stadthauses in Graz, ohne Dachdurchdringung montiert",
                 "Graz: 18 kWp ballastiert auf Gründach"),
            ],
        ),
        C.cards_section(
            eyebrow="Anbieter-Check",
            h2="Woran Sie eine seriöse Photovoltaik-Firma erkennen",
            intro=("Wer nach Photovoltaik-Erfahrungen und seriösen Anbietern sucht, landet oft bei Foren und Betrugswarnungen. "
                   "Sechs Punkte, die Sie bei jedem Angebot "
                   "prüfen können, mit den Antworten von EBZ Energie (Stand Oktober 2026)."),
            cards=[
                {"ic": "◫", "title": "Prüfbare Firmendaten", "text": "EBZ Energie GmbH, FN 597101 s, Triglavstraße 15, 9500 Villach, Mitglied der Wirtschaftskammer Kärnten.",
                 "link_key": "ueber_uns", "link_text": "Wer hinter den Anlagen steht"},
                {"ic": "✓", "title": "Zertifizierte Montage", "text": "Zertifizierte Fachkräfte für Dach und Elektrotechnik, von der Planung bis zur Übergabe."},
                {"ic": "◇", "title": "Projektbericht statt Pauschale", "text": "Projektbericht mit 3D-Belegplan und Statikreport für Ihr Dach, dazu ein Fixangebot mit Festpreisgarantie."},
                {"ic": "☀", "title": "Garantien schriftlich", "text": "Glas-Glas-Module mit bis zu 30 Jahren Leistungs- und mindestens 10 Jahren Produktgarantie, im Angebot festgehalten."},
                {"ic": "◉", "title": "Referenzen mit Zahlen", "text": "Zehn Anlagen mit kWp, Speicher, Ertrag und Ersparnis auf dieser Seite, 300+ Projekte insgesamt."},
                {"ic": "★", "title": "Echte Bewertungen", "text": f"{NAP['rating']} Sterne aus {bew} auf Google, von Kundinnen und Kunden aus Kärnten und der Steiermark."},
            ],
        ),
        C.reviews_slider(reviews, rating=rating, count=count),
        C.faq_section([(q, f"<p>{ans}</p>") for q, ans in FAQ]),
        C.linkgrid_section(
            "Passend zu diesen Projekten",
            [("ueber_uns", "Wer hinter den Anlagen steht: EBZ Energie GmbH"),
             ("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
             ("pv_gewerbe", "Photovoltaik für Betriebe"),
             ("batteriespeicher", "Batteriespeicher und Notstrom"),
             ("/notstrom/", "Notstrom bei Netzausfall"),
             ("/pv-speicher-nachruesten/", "Speicher nachrüsten"),
             ("/ab-wann-lohnt-sich-photovoltaik-mit-speicher/", "Ab wann lohnt sich Photovoltaik mit Speicher?"),
             ("solarrechner", "Ihre Zahlen im Solarrechner berechnen"),
             ("pv_villach", "Photovoltaik Villach"),
             ("kontakt", "Kostenlose Erstberatung anfragen")],
        ),
        C.contact_section(
            headline="Ihr Dach ist das nächste Projekt",
            sub=("Erzählen Sie uns kurz von Ihrem Dach und Ihrem Verbrauch. Wir sagen Ihnen ehrlich, welche "
                 "Anlage passt, was sie kostet und wie schnell sie sich rechnet. Kostenlos und unverbindlich."),
        ),
        C.finalcta(
            "Bereit für Ihre eigene Referenz?",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags und nehmen "
            "uns Zeit für Ihr Projekt.",
        ),
        _footnote(),
    ])

    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=IMG["gewerbe_dach"])
    return write_page("referenzen/index.html", html)


def _footnote():
    return f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte aus den jeweiligen Projektunterlagen. Jahresertrag, Ersparnis und
      Amortisation hängen von Verbrauch, Strompreis, Ausrichtung und Wetter ab und können bei Ihrer Anlage
      abweichen. Montagedauer laut Projektunterlagen und Kundenbewertungen auf Google (Stand Oktober 2026).
      Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>"""


if __name__ == "__main__":
    build()
