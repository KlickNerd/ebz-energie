"""Leistungsseite Photovoltaik-Carport (/photovoltaik-carport/).

Kompakte Seite aus dem alten Ratgeber-Beitrag, SEO/GEO-Ueberarbeitung Oktober 2026
nach build/seo/carport.{json,md}: Tabelle Einzel-/Doppelcarport, Kosten mit und ohne
Speicher (Marktrichtwerte Salzburg AG aus dem Briefing*), Bausatz vs. Komplettsystem,
Beispielrechnung mit Amortisation*, bifaziale Glas-Glas-Module, wasserdichtes Dach,
Bauanzeige (qualitativ, keine erfundenen Masse), Betriebe. Es gibt kein eigenes
Carport-Foto, Alt-Texte bleiben deshalb ehrlich (PV-Motive als Symbolbild).
Zahlen: Ertrag 950 bis 1.100 kWh je kWp, 2 Stellplaetze 30 bis 35 m2 = 5 bis 7 kWp
(Quellbeitrag), Strompreis 28 ct und OeMAG 10,168 ct (Faktenblatt) fuer die Beispielrechnung.
"""

from common import IMG, NAP, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, href, write_page, load_reviews
from layout import page
import components as C

PATH = "/photovoltaik-carport/"
TITLE = "Photovoltaik Carport: Kosten, Statik, Wallbox | EBZ Energie"
DESC = ("Photovoltaik-Carport für 1 oder 2 Stellplätze: 3 bis 7 kWp, bifaziale Glas-Glas-Module, Wallbox, "
        "Speicher, Statik für Schneelast. Komplettsystem mit Montage.")

STAND = "Stand Oktober 2026"

FAQ = [
    ("Wie viel kostet ein Photovoltaik-Carport für zwei Stellplätze?",
     "Ein Doppelcarport mit 5 bis 7 kWp kostet als Komplettsystem mit Konstruktion, Modulen und Montage laut "
     "Marktrichtwerten rund 9.000 bis 17.000 Euro*, mit 5 bis 10 kWh Speicher rund 21.500 bis 27.500 Euro*. Der "
     "PV-Teil allein (Module, Hybridwechselrichter, Elektroanschluss, Netzanmeldung) liegt bei EBZ Energie ab etwa "
     "9.000 Euro* für rund 5 kWp; die Konstruktion kalkulieren wir nach Material, Stellplätzen und Lastzone im Festpreis."),
    ("Bausatz oder Komplettsystem mit Montage: was ist sinnvoller?",
     "Ein Bausatz (2.400 bis 9.000 Euro*) enthält Konstruktion und Module, aber keine Statik für Ihren Standort, keine "
     "Elektroinstallation und keine Netzanmeldung; Anschluss und Inbetriebnahme muss ohnehin ein Elektrofachbetrieb "
     "machen. Das Komplettsystem liefert Statik, Fundament, Elektrik, Wallbox, Speicher, Anmeldung und Garantie aus "
     "einer Hand. Wer selbst baut, spart beim Aufbau und trägt Statik- und Dichtheitsrisiko selbst."),
    ("Wie viel Strom erzeugt ein Solarcarport pro Jahr?",
     "Ein Einzelcarport mit rund 3 kWp liefert etwa 2.900 bis 3.300 kWh im Jahr, ein Doppelcarport mit 5 bis 7 kWp "
     "rund 5.000 bis 7.500 kWh (950 bis 1.100 kWh je kWp in Österreich). Das Doppelcarport reicht für ein E-Auto mit "
     "rund 15.000 Kilometern im Jahr und einen guten Teil des Haushaltsstroms."),
    ("Lohnt sich ein Solar-Carport ohne E-Auto?",
     "Ja, wenn Sie ohnehin ein Carport bauen: Das Solardach ersetzt die normale Dacheindeckung. Der Strom fließt ins "
     "Haus, in den Speicher und zur Wärmepumpe; der Eigenverbrauch liegt ohne Speicher bei rund 30 Prozent, mit "
     "Speicher bei 60 bis 80 Prozent*. Die Wallbox lässt sich jederzeit nachrüsten, wenn der Hybridwechselrichter "
     "vorbereitet ist."),
    ("Welche Vorschriften gelten für Carports in Kärnten und der Steiermark (Grundgrenze, Höhe, Bauanzeige)?",
     "Carports sind nach Kärntner Bauordnung und Steiermärkischem Baugesetz in der Regel anzeige- oder "
     "bewilligungspflichtig. Entscheidend sind Abstand zur Grundgrenze, Gesamthöhe, Bebauungsplan und Ortsbild; direkt "
     "an der Grundgrenze ist oft die Zustimmung des Nachbarn nötig. Die Maße legt Ihre Gemeinde fest. Ohne Bauanzeige "
     "riskieren Sie ein nachträgliches Verfahren bis zum Rückbau. Wir klären die Vorgaben mit und liefern den Statiknachweis."),
    ("Kann ich meinen bestehenden Carport mit Photovoltaik nachrüsten?",
     "Ja, wenn die Statik rund 15 bis 25 Kilogramm je Quadratmeter* zusätzlich für Module und Unterkonstruktion sowie "
     "die höhere Windlast trägt. Ältere Carports sind dafür oft nicht ausgelegt; dann ist Verstärkung oder Neubau "
     "wirtschaftlicher. Die statische Prüfung übernehmen wir vor dem Angebot."),
    ("Ist das Dach eines PV-Carports wasserdicht?",
     "Ja, wenn es dafür gebaut ist: Beim echten Solardach bilden Glas-Glas-Module die Dachhaut, liegen in Profilschienen "
     "mit Dichtlippen, und das Wasser läuft über eine Regenrinne gezielt ab. Günstige Bausätze mit Modulen auf offenem "
     "Rahmen sind nur regenabweisend. Wir verbauen ausschließlich für die Überkopfmontage zugelassene Module."),
    ("Muss ich den Solarcarport versichern?",
     "Pflicht ist es nicht, sinnvoll schon. Meist lässt sich die Anlage in die bestehende Wohngebäudeversicherung "
     "aufnehmen (Sturm, Hagel, Schnee, Blitz, Überspannung); melden Sie Carport und Anlage nach der Inbetriebnahme. "
     "Garantien decken die Technik: bis zu 30 Jahre Leistungsgarantie und mindestens 10 Jahre Produktgarantie."),
    ("Funktioniert ein Photovoltaik-Carport im Winter?",
     "Ja, mit geringerer Leistung; auch bei diffusem Licht produzieren die Module Strom. Entscheidend ist eine "
     "Konstruktion, die für die Schneelastzone Ihres Standorts ausgelegt ist. Die glatte Moduloberfläche begünstigt "
     "das Abrutschen des Schnees."),
    ("Wie lange hält ein Photovoltaik-Carport?",
     "Konstruktionen aus Aluminium oder verzinktem Stahl halten 30 bis 40 Jahre und länger. Für die Module gilt bis zu "
     "30 Jahre Leistungsgarantie und mindestens 10 Jahre Produktgarantie, der Wechselrichter wird meist nach 15 bis "
     "20 Jahren getauscht."),
]


def _table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    body = ""
    for r in rows:
        tds = "".join(f'<td class="hl">{c}</td>' if i == 0 else f"<td>{c}</td>" for i, c in enumerate(r))
        body += f"<tr>{tds}</tr>"
    return f'<div class="art-tablewrap eg-reveal"><table class="art-table"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def _size_section():
    rows = [
        ("Einzelcarport", "1 Stellplatz", "rund 15 m²", "rund 7 Module", "rund 3 kWp", "2.900 bis 3.300 kWh"),
        ("Doppelcarport", "2 Stellplätze", "30 bis 35 m²", "14 bis 16 Module", "5 bis 7 kWp", "5.000 bis 7.500 kWh"),
        ("Reihencarport (Betrieb)", "4 und mehr Stellplätze", "ab 60 m²", "ab 28 Module", "ab 12 kWp", "ab 11.000 kWh"),
    ]
    table = _table(["Variante", "Stellplätze", "Dachfläche", "Module*", "Leistung", "Ertrag pro Jahr*"], rows)
    return f"""
  <section class="section" style="background:#fff;border-block:1px solid var(--line)">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Carport mit Photovoltaik: Einzel- oder Doppelcarport</p>
      <h2 class="center eg-reveal">Einzel- oder Doppelcarport: Stellplätze, Module, kWp und Ertrag</h2>
      <p class="lead center eg-reveal" style="max-width:72ch;margin-inline:auto">Suchende denken in Stellplätzen, die Anlage
      rechnet in Kilowatt: Je Stellplatz stehen rund 15 m² Dachfläche zur Verfügung, es braucht etwa 5 m² Dachfläche je kWp. Ein
      Doppelcarport trägt damit rund 5 bis 7 kWp und liefert 5.000 bis 7.500 kWh im Jahr, genug für ein E-Auto mit
      15.000 Kilometern und einen guten Teil des Haushaltsstroms (EBZ Energie, {STAND}).</p>
      {table}
      <p class="form-note center eg-reveal">*Richtwerte: Module mit rund 430 bis 450 Wp, Ertrag 950 bis 1.100 kWh je kWp und Jahr
      (österreichweiter Durchschnitt). Neigung, Ausrichtung und Verschattung bestimmen den tatsächlichen Ertrag.</p>
    </div>
  </section>"""


def _cost_section():
    rows = [
        ("Bausatz zum Selbstaufbau", "Konstruktion und Module, ohne Statiknachweis, Elektrik, Netzanmeldung",
         "Bausatz 2.400 bis 9.000 €*", "Aufbau, Elektrofachbetrieb, Bauanzeige und Risiko liegen bei Ihnen"),
        ("PV-Anlage auf dem Carport (EBZ)", "Module, Hybridwechselrichter, Elektroanschluss, Netzanmeldung, rund 5 kWp",
         "ab ca. 9.000 €*", "Konstruktion vorhanden oder separat; später um Speicher und Wallbox erweiterbar"),
        ("Speicher 5 bis 10 kWh", "Batteriespeicher, optional mit Notstrom", "plus 5.000 bis 9.000 €*",
         "Eigenverbrauch von rund 30 auf 60 bis 80 Prozent, 150 € je kWh gefördert"),
        ("Komplettsystem mit Montage", "Konstruktion, bifaziale Glas-Glas-Module, Statik, Elektrik, Anmeldung, 3 bis 8 kWp",
         "rund 9.000 bis 17.000 €*", "mit Speicher rund 21.500 bis 27.500 €*; Wallbox nach Angebot"),
    ]
    table = _table(["Variante", "Umfang", "Richtpreis", "Hinweis"], rows)
    return f"""
  <section class="section" id="kosten">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Photovoltaik Carport Preise</p>
      <h2 class="center eg-reveal">Was kostet ein Photovoltaik-Carport? Preise mit und ohne Speicher, Bausatz oder Komplettsystem*</h2>
      <p class="lead center eg-reveal" style="max-width:72ch;margin-inline:auto">Ein Photovoltaik-Carport kostet in Österreich als
      Komplettsystem mit Montage rund 9.000 bis 17.000 Euro* für 3 bis 8 kWp, mit Speicher rund 21.500 bis 27.500 Euro*;
      reine Bausätze liegen bei 2.400 bis 9.000 Euro* ohne Elektrik und Statik. Der PV-Teil wird mit 150 Euro je kWp und
      150 Euro je kWh Speicher gefördert (Marktrichtwerte und EAG-Sätze, {STAND}).</p>
      {table}
      <div class="eg-reveal" style="max-width:72ch;margin-inline:auto;margin-top:22px">
        <h3>Bausatz oder Komplettsystem: der Unterschied liegt im Risiko, nicht im Preis</h3>
        <p>Beim Bausatz bleiben Statik für Ihre Lastzone, Fundament, Elektroinstallation, Netzanmeldung und Bauanzeige bei Ihnen.
        Beim Komplettsystem von EBZ Energie stecken diese Leistungen im Festpreis, mit Projektbericht, 3D-Belegplan und
        Statikreport vor dem Auftrag und einem Ansprechpartner danach.</p>
      </div>
      <p class="form-note center eg-reveal">*Richtwerte vor Förderung: PV-Teil und Speicher auf Basis typischer EBZ-Projekte,
      Komplettsystem- und Bausatzspannen aus marktüblichen österreichischen Angeboten 2026. Die Konstruktion kalkulieren wir nach
      Vor-Ort-Termin im Festpreisangebot. Weitere Preise im Ratgeber {a("/kosten-einer-solaranlage/", "Kosten einer Solaranlage")}.</p>
    </div>
  </section>"""


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        C.hero(
            eyebrow="Photovoltaik Carport für Eigenheim und Betrieb",
            h1="Photovoltaik-Carport (Solarcarport): Ihr Stellplatz wird zum Kraftwerk",
            lead=("Ein Carport mit Photovoltaik schützt Ihre Fahrzeuge und erzeugt auf derselben Fläche Strom: "
                  "3 kWp auf dem Einzelcarport, 5 bis 7 kWp auf zwei Stellplätzen. Mit Wallbox laden Sie Ihr "
                  "E-Auto direkt mit Sonnenstrom, ein Speicher versorgt Haus und Auto am Abend. EBZ Energie plant "
                  "Konstruktion, Statik, bifaziale Glas-Glas-Module und Ladetechnik als Komplettsystem mit Montage, "
                  "mit zertifizierten Fachkräften aus Villach."),
            badges=[("3 bis 7 kWp", "für 1 oder 2 Stellplätze"),
                    ("Glas-Glas bifazial", "wasserdichtes Solardach"),
                    ("Statik", "für Schnee und Wind")],
            img=IMG["gen_hero"],
            img_alt="Photovoltaikmodule auf einem Dach, Symbolbild für ein Solardach über Stellplätzen",
            float_num=rating,
            float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_secondary=("#kosten", "Kosten ansehen"),
        ),
        C.kpis([
            ("5 bis 7 kWp", "auf 30 bis 35 m² Doppelcarport"),
            ("950 bis 1.100 kWh", "Ertrag je kWp und Jahr"),
            ("30 bis 40 Jahre", "Lebensdauer der Konstruktion"),
            (NAP["rating"], "Sterne auf Google"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Was ist ein Photovoltaik-Carport?",
            paragraphs=[
                ("Ein Photovoltaik-Carport (Solarcarport, PV Carport, Solar Carport) ist ein Carport, dessen Dach "
                 "aus Solarmodulen besteht: Die Module sind Dacheindeckung und Stromerzeuger zugleich. Ein "
                 "Doppelcarport mit 30 bis 35 m² trägt rund 5 bis 7 kWp und liefert in Österreich 5.000 bis "
                 f"7.500 kWh im Jahr, ein Einzelcarport rund 3 kWp (EBZ Energie, {STAND})."),
                ("Technisch arbeitet die Anlage wie eine Dachanlage: Ein Hybridwechselrichter wandelt den Gleichstrom "
                 "in Wechselstrom für Haus, Wallbox und Speicher. Der Unterschied liegt in der Konstruktion: Sie muss "
                 "Modulgewicht, Schnee- und Windlast tragen, wasserdicht sein und braucht meist eine Bauanzeige. Eine "
                 "versiegelte Fläche wird doppelt genutzt, ohne Grünfläche zu verbauen."),
            ],
        ),
        _size_section(),
        C.cards_section(
            eyebrow="Das Komplettsystem",
            h2="Vier Bausteine: Konstruktion, bifaziale Glas-Glas-Module, Wallbox, Speicher und Notstrom",
            intro=("Vom Fundament bis zur Ladesteuerung planen wir Ihr Carport als Ganzes und stimmen "
                   "die Bausteine aufeinander ab."),
            cards=[
                {"ic": "⌂", "title": "Konstruktion und wasserdichtes Dach",
                 "text": ("Aluminium (wartungsfrei), verzinkter und pulverbeschichteter Stahl (höchste Tragfähigkeit) "
                          "oder Leimholz (natürliche Optik, pflegeintensiver). Module in Profilschienen mit Dichtlippen, "
                          "Regenrinne und Wasserableitung, statischer Nachweis für Ihre Schnee- und Windlastzone.")},
                {"ic": "☀", "title": "Bifaziale Glas-Glas-Module",
                 "text": ("Für die Überkopfmontage zugelassen, beidseitig aktiv: Die Rückseite nutzt das Streulicht vom "
                          "hellen Boden. 3 bis 7 kWp je nach Stellplätzen, bis zu 30 Jahre Leistungsgarantie. Der "
                          "Hybridwechselrichter bereitet Speicher und Notstrom vor."),
                 "link_key": "photovoltaik", "link_text": "Zur Photovoltaik"},
                {"ic": "⌖", "title": "Wallbox mit Überschussladen",
                 "text": ("Die Wallbox lädt bevorzugt dann, wenn das Dach mehr liefert als das Haus braucht. So fahren "
                          "Sie mit Strom für 10 bis 14 ct/kWh statt zu Tarifen öffentlicher Ladesäulen.* Gesteuert vom "
                          "Energiemanagementsystem."),
                 "link_key": "ems", "link_text": "Energiemanagement fürs Überschussladen"},
                {"ic": "▮", "title": "Speicher und Notstrom",
                 "text": ("5 bis 10 kWh Speicher laden das E-Auto auch nach Sonnenuntergang und halten bei "
                          "Stromausfall Kühlschrank, Router und Heizungspumpe am Netz."),
                 "link_key": "batteriespeicher", "link_text": "Zum Stromspeicher"},
            ],
        ),
        C.media_text(
            eyebrow="PV Carport Österreich: Statik zuerst",
            h2="Statik zuerst: Schneelast und Windlast in Österreich, Nachrüsten bestehender Carports",
            paragraphs=[
                ("Solarmodule bieten Wind eine große Angriffsfläche, und nasser Schnee wiegt viel. Die "
                 "Lastzonen unterscheiden sich in Österreich je nach Region erheblich: Ein Carport in einer "
                 "schneereichen Lage Oberkärntens braucht eine deutlich stärkere Auslegung als eines im "
                 "flachen Süden der Steiermark. Wir dimensionieren die Konstruktion nach der Lastzone Ihres "
                 "Standorts und liefern den Nachweis für die Bauanzeige."),
                ("Bestehende Carports lassen sich nachrüsten, wenn die Statik rund 15 bis 25 Kilogramm je "
                 "Quadratmeter* zusätzlich und die höhere Windlast trägt; die Prüfung übernehmen wir vor dem Angebot."),
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
        _cost_section(),
        C.facts_panel(
            eyebrow="Beispielrechnung",
            h2="Wann sich ein Solarcarport rechnet: Beispielrechnung und Amortisation*",
            intro=("Doppelcarport mit 6 kWp, E-Auto, 7-kWh-Speicher und Haushalt in Kärnten. Alle Werte sind "
                   "Richtwerte, die konkrete Rechnung steht im Projektbericht."),
            rows=[
                ("Ertrag", "rund 6.000 kWh im Jahr (6 kWp mal rund 1.000 kWh)*"),
                ("Eigenverbrauch", "rund 65 Prozent mit E-Auto und Speicher, also etwa 3.900 kWh*"),
                ("Ersparnis Netzstrom", "3.900 kWh mal 28 ct = rund 1.090 € im Jahr*"),
                ("Einspeisung", "2.100 kWh mal 10,168 ct (OeMAG-Marktpreis September 2026) = rund 215 € im Jahr*"),
                ("Nutzen gesamt", "rund 1.300 € im Jahr*, plus Treibstoffersparnis fürs E-Auto"),
                ("Förderung", "EAG 2026: 900 € für 6 kWp plus 150 € je kWh Speicher, Kärnten 3.000 € Pauschale mit Speicher ab 5 kWh"),
                ("Amortisation PV-Teil", "rund 7 bis 9 Jahre* ohne Konstruktion"),
                ("Amortisation Komplettsystem", "rund 10 bis 15 Jahre* (Marktrichtwert), bei 30 bis 40 Jahren Lebensdauer"),
            ],
            actions=[("Rechnung für meinen Stellplatz anfragen", href("kontakt"), ""),
                     ("Zum Solarrechner", href("solarrechner"), "")],
        ),
        C.text_block(
            eyebrow="Bauanzeige und Vorschriften",
            h2="Bauanzeige und Vorschriften in Kärnten und der Steiermark",
            paragraphs=[
                ("Ein Carport ist ein Bauwerk: Die Kärntner Bauordnung und das Steiermärkische Baugesetz regeln, ob "
                 "eine Bauanzeige oder Baubewilligung nötig ist. Entscheidend sind Abstand zur Grundgrenze, Gesamthöhe, "
                 "Bebauungsplan und Ortsbild; die konkreten Maße legt Ihre Gemeinde fest. Wir fragen sie vor der Planung "
                 "ab, legen den Statikreport der Einreichung bei und melden die Anlage beim Netzbetreiber an."),
            ],
        ),
        C.media_text(
            eyebrow="Förderung und Finanzierung",
            h2="Förderung: der PV-Teil wird gefördert wie jede Dachanlage",
            paragraphs=[
                ("Für die Photovoltaikanlage auf dem Carport gilt 2026 der EAG-Investitionszuschuss des Bundes: 150 € "
                 "je kWp bis 10 kWp, 150 € je kWh Speicher und 10 Prozent Made-in-Europe-Bonus je Komponente. Der "
                 "dritte Fördercall läuft bis 22. Oktober 2026, ab 2027 plant der Bund laut BMWET eine Systemförderung "
                 f"mit Antrag nach der Installation ({STAND}). In Kärnten kommen 3.000 € Landespauschale für "
                 "Neuanlagen ab 5 kWp mit Speicher ab 5 kWh dazu, Einreichung 12. Oktober bis 31. Dezember 2026."),
                ("Die Carport-Konstruktion selbst ist nicht Teil der PV-Förderung, und der Umsatzsteuer-Nullsatz für "
                 "PV-Anlagen ist seit April 2025 ausgelaufen; an seine Stelle tritt der Zuschuss. Wer die Investition nicht auf "
                 "einmal binden will, finanziert mit 0 € Anzahlung und fixer Rate. Die Anlage gehört Ihnen dabei ab "
                 "dem ersten Tag, die Förderung bleibt bei Ihnen."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Photovoltaik-Förderung am Tisch",
            bullets=[
                "Bund: 150 €/kWp und 150 €/kWh Speicher, plus Made-in-Europe-Bonus",
                "Kärnten: 3.000 € Pauschale für Neuanlagen mit Speicher",
                a("finanzierung", "Finanzierung: 0 € Anzahlung, Eigentum ab Tag 1"),
            ],
            cta=("foerderung_at", "PV-Förderung Österreich 2026 im Detail"),
            dark=True,
        ),
        C.media_text(
            eyebrow="Für Betriebe",
            h2="Für Betriebe: Mitarbeiter- und Kundenparkplätze mit Ladepunkten",
            paragraphs=[
                ("Ein Reihencarport über dem Firmenparkplatz liefert ab 12 kWp Strom, wenn der Betrieb ihn braucht, und "
                 "lädt Fuhrpark und Kundenfahrzeuge mit eigenem Sonnenstrom; das Energiemanagement verhindert Lastspitzen. "
                 "In der Steiermark fördert der Ökofonds Parkplatzüberdachungen ab 20 kWp mit bis zu 30 Prozent, maximal "
                 "250.000 € je Antrag, kombinierbar mit dem EAG-Zuschuss."),
            ],
            img=IMG["gen_gewerbe"],
            alt="Gewerbebetrieb mit Photovoltaikanlage, Symbolbild für Firmenparkplatz mit Solarcarport",
            bullets=[
                "Ladepunkte für Fuhrpark und Kunden, gesteuert vom EMS",
                "Kombinierbar mit Dachanlage und Gewerbespeicher",
            ],
            reverse=True,
            cta=("pv_gewerbe", "Photovoltaik für Betriebe"),
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
            h2="Ablauf: vom Stellplatz zum eigenen Kraftwerk",
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
             ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage"),
             ("foerderung_at", "PV-Förderung Österreich 2026"),
             ("batteriespeicher", "Stromspeicher"),
             ("/notstrom/", "Notstrom mit Photovoltaik"),
             ("ems", "Energiemanagementsystem fürs Überschussladen"),
             ("pv_gewerbe", "Photovoltaik für Betriebe"),
             ("finanzierung", "Finanzierung"),
             ("referenzen", "Referenzen")],
        ),
        C.contact_section(
            headline="Angebot mit Festpreis: Statik, Anlage und Konstruktion in einem",
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
    return (f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte vor Förderung: PV-Teil und Speicher auf Basis typischer EBZ-Projekte, Komplettsystem-
      und Bausatzpreise sowie Amortisation 10 bis 15 Jahre aus marktüblichen österreichischen Angeboten 2026. Ertrag 950 bis 1.100 kWh
      je kWp und Jahr ist ein österreichweiter Durchschnitt, Beispielrechnung mit 28 ct/kWh Haushaltsstrompreis, 65 Prozent
      Eigenverbrauch und OeMAG-Marktpreis September 2026 (10,168 ct). Gestehungskosten für Solarstrom 10 bis 14 ct/kWh je nach
      Anlage, Zusatzgewicht 15 bis 25 kg/m² je nach Modul und Unterkonstruktion. Fördersätze {STAND}, Änderungen durch
      Fördergeber vorbehalten. Konstruktion, Ertrag und Kosten hängen von Standort, Lastzone, Ausrichtung und Komponentenwahl ab.
      Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    import theme
    theme.write_assets()
    build()
