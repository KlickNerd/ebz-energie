"""Leistungsseite Photovoltaik fuer Gewerbe (/photovoltaik-gewerbe/).

Quelle: Live-Seite /photovoltaik-gewerbe/ (Elementor, 2023) plus Gewerbe-Sektion
aus build/photovoltaik.py. Bereinigt: "ohne Subunternehmer", Widmanngasse,
"Energieertrag-Berechnungen" (jetzt Projektbericht mit 3D-Belegplan und
Statikreport), "mehr als 100 Projekte" (jetzt 300+), Gedankenstriche.
SEO/GEO-Ueberarbeitung Oktober 2026 nach build/seo/pv_gewerbe.{json,md}:
EAG-Kategorien C/D (Faktenblatt _fakten_2026-10.md), Kosten je kWp 700 bis 1.300 EUR*
(Marktrichtwert aus _geo.md), Stromgestehungskosten rechnerisch*, Elektrizitaetsabgabe
1,5 ct (aus EG-Seiten), Steuer nur allgemein mit Hinweis Steuerberatung, Flachdach-Abschnitt,
Agri-PV nur als FAQ. Contracting nur als Abgrenzung, nicht als Angebot.
"""

from common import IMG, NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, S, faq_jsonld, u, a, href, tel_link, write_page, load_reviews
from layout import page
import components as C

PATH = "/photovoltaik-gewerbe/"
TITLE = "Photovoltaik für Gewerbe & Landwirtschaft | EBZ Energie"
DESC = ("Photovoltaik für Betriebe in Kärnten und Steiermark: Auslegung nach Lastprofil, Gewerbespeicher, "
        "EAG-Förderung Kategorie C und D. Referenz: 13.500 € im Jahr.")

STAND = "Stand Oktober 2026"

FAQ = [
    ("Lohnt sich Photovoltaik für meinen Betrieb und ab welcher Eigenverbrauchsquote?",
     "In den meisten Fällen ja. Betriebe verbrauchen den Großteil ihres Stroms tagsüber und erreichen ohne Speicher "
     "Eigenverbrauchsquoten von 70 Prozent und mehr*. Ab etwa 50 Prozent rechnet sich die Anlage deutlich schneller "
     "als im Eigenheim. Referenz: 40 kWp in Oberösterreich sparen rund 13.500 Euro im Jahr."),
    ("Welche Förderung gibt es 2026 für Gewerbeanlagen (EAG Kategorie C und D) und wann ist der nächste Fördercall?",
     "Der EAG-Investitionszuschuss 2026 zahlt in Kategorie C (über 20 bis 100 kWp) 130 Euro je kWp, in Kategorie D "
     "(über 100 bis 1.000 kWp) 120 Euro je kWp, Speicher 150 Euro je kWh (mindestens 0,5 kWh je kWp, maximal 50 kWh), "
     "dazu 10 Prozent Made-in-Europe-Bonus. Der letzte Fördercall 2026 läuft bis 22. Oktober 2026; ab 2027 ist laut "
     "BMWET eine Systemförderung mit Antrag nach der Installation geplant (Stand Oktober 2026)."),
    ("PV Anlage 30 kWp, 50 kWp oder 100 kWp: Was kostet sie für einen Betrieb?",
     "Marktrichtwert 2026: rund 700 bis 1.300 Euro je kWp netto*. 30 kWp liegen damit bei etwa 21.000 bis 39.000 Euro, "
     "50 kWp bei 45.000 bis 65.000 Euro, 100 kWp bei 85.000 bis 130.000 Euro, jeweils vor Förderung und ohne Speicher. "
     "Je größer die Anlage, desto günstiger je kWp. Den Preis für Ihr Dach liefert der Projektbericht mit 3D-Belegplan "
     "und Statikreport."),
    ("Sind gewerbliche PV-Anlagen steuerfrei und wie werden sie abgeschrieben?",
     "Steuerfrei nicht, aber steuerlich günstig: Die Anlage ist Betriebsvermögen und wird über die Nutzungsdauer "
     "abgeschrieben, laufende Kosten sind Betriebsausgaben, die Vorsteuer ist abziehbar. Selbst erzeugter und "
     "verbrauchter Strom ist von der Elektrizitätsabgabe (1,5 Cent je kWh) befreit, Einspeiseerlöse sind "
     "Betriebseinnahmen. Bei gemischter Nutzung (Hof und Wohnhaus) wird aufgeteilt. Details mit Ihrer Steuerberatung."),
    ("Brauche ich als PV-Betreiber eine Gewerbeanmeldung?",
     "Für die Anlage auf dem eigenen Betriebsgebäude nicht, sie ist Teil Ihres Betriebs. Private Betreiber mit "
     "Überschusseinspeisung gelten nicht als Gewerbetreibende; ihre Einspeiseerlöse sind bis 12.500 kWh im Jahr "
     "einkommensteuerfrei (Anlagen bis 35 kWp). Bei Volleinspeisung oder sehr großen Anlagen fragen Sie Ihre Steuerberatung."),
    ("Wie hoch ist die Einspeisevergütung für gewerbliche Anlagen?",
     "Einen eigenen Gewerbetarif gibt es nicht. Der OeMAG-Marktpreis lag im September 2026 bei 10,168 Cent je kWh "
     "(Stand Oktober 2026), im Juli bei 6,146 Cent; er schwankt monatlich. Weil der Bezugspreis ein Mehrfaches beträgt, "
     "zählt der Eigenverbrauch. Wochenendüberschüsse verwerten Sie besser in einer Energiegemeinschaft oder bei großen "
     "Anlagen über Direktvermarktung."),
    ("Was ist Lastspitzenkappung und wann lohnt sich ein Gewerbespeicher?",
     "Betriebe zahlen über den Leistungspreis für ihre höchste Viertelstunden-Leistungsspitze. Bei der "
     "Lastspitzenkappung (Peak Shaving) liefert der Speicher den Mehrbedarf, wenn mehrere Maschinen gleichzeitig "
     "anlaufen. Ein Gewerbespeicher lohnt sich bei teuren Lastspitzen, Verbrauch am Abend oder Wochenende und wenn "
     "Kühlung oder Server bei Netzausfall weiterlaufen müssen. Förderung: 150 Euro je kWh bis 50 kWh."),
    ("Agri-PV oder Dachanlage: was passt zu meinem landwirtschaftlichen Betrieb?",
     "Agri-PV ist eine Freiflächenanlage mit aufgeständerten oder senkrechten Modulen, unter der weiter bewirtschaftet "
     "wird: ein eigenes Projektfeld mit Flächenwidmung, Netzanschluss und meist Pachtmodellen. Für die meisten Höfe ist "
     "das Stall-, Hallen- oder Lagerdach die einfachere Fläche: keine Widmung, kurzer Weg zum Zählpunkt. In der "
     "Steiermark fördert der Ökofonds Doppelnutzungsanlagen ab 20 kWp mit bis zu 30 Prozent, maximal 250.000 Euro."),
    ("Wie groß sollte eine Gewerbe-PV-Anlage sein?",
     "Die Größe richtet sich nach Ihrem Lastprofil, nicht nur nach der Dachfläche. Typische Gewerbeanlagen liegen "
     "zwischen 20 und 100 kWp, Hallen und Ställe auch darüber. Ab rund 100 kWp stimmen wir Anschlussleistung, Netzebene "
     "und gegebenenfalls Trafo mit dem Netzbetreiber ab."),
    ("Wie lange dauert die Montage einer Gewerbeanlage?",
     "Nach Projektbericht mit 3D-Belegplan und Statikreport je nach Größe wenige Tage bis zwei Wochen, abgestimmt auf "
     "Ihre Betriebszeiten. Netzanmeldung, Zählertausch und Förderabwicklung übernehmen wir."),
]


def _table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    body = ""
    for r in rows:
        tds = "".join(f'<td class="hl">{c}</td>' if i == 0 else f"<td>{c}</td>" for i, c in enumerate(r))
        body += f"<tr>{tds}</tr>"
    return f'<div class="art-tablewrap eg-reveal"><table class="art-table"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def _cost_section():
    lead = ("Eine gewerbliche PV-Anlage kostet in Österreich 2026 rund 700 bis 1.300 Euro je kWp netto*, eine "
            "50-kWp-Dachanlage also etwa 45.000 bis 65.000 Euro vor Förderung. EBZ-Referenz: 40 kWp Ost-West auf "
            "Trapezblech mit 40-kWh-Speicher in Oberösterreich, rund 40.000 kWh pro Jahr und 13.500 Euro "
            f"Stromkostenersparnis jährlich (Projektbericht EBZ Energie, {STAND}).")
    rows = [
        ("30 kWp", "rund 21.000 bis 39.000 €*", "27.000 bis 33.000 kWh", "rund 150 bis 180 m²", "Kat. C: 130 €/kWp = 3.900 €"),
        ("50 kWp", "rund 45.000 bis 65.000 €*", "45.000 bis 55.000 kWh", "rund 250 bis 300 m²", "Kat. C: 130 €/kWp = 6.500 €"),
        ("100 kWp", "rund 85.000 bis 130.000 €*", "90.000 bis 110.000 kWh", "rund 500 bis 600 m²", "Kat. C: 130 €/kWp = 13.000 €"),
        ("Gewerbespeicher", "20 bis 100 kWh, nach Lastprofil", "Eigenverbrauch und Lastspitzenkappung", "Technikraum oder Außenschrank",
         "150 €/kWh bis 50 kWh, mind. 0,5 kWh je kWp"),
    ]
    table = _table(["Anlagengröße", "Investition netto*", "Ertrag pro Jahr*", "Dachfläche*", "EAG-Zuschuss 2026"], rows)
    return f"""
  <section class="section" style="background:#fff;border-block:1px solid var(--line)" id="kosten">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Photovoltaik Gewerbe: Kosten je kWp</p>
      <h2 class="center eg-reveal">Was kostet eine Gewerbeanlage? Richtwerte für 30, 50 und 100 kWp*</h2>
      <p class="lead center eg-reveal" style="max-width:72ch;margin-inline:auto">{lead}</p>
      {table}
      <p class="center eg-reveal" style="max-width:72ch;margin-inline:auto">Rechnerisch ergeben 700 bis 1.300 € je kWp und
      900 bis 1.100 kWh Ertrag über 25 Jahre Stromgestehungskosten von rund 4 bis 7 Cent je kWh inklusive Betrieb*, ein
      Bruchteil des Netzbezugs. Amortisation laut Marktquellen 6 bis 12 Jahre*, im Hotel Warmbad rund 6 Jahre.</p>
      <p class="form-note center eg-reveal">*Marktrichtwerte 2026 netto, vor Förderung, ohne Speicher. Ihr Preis steht im
      Projektbericht. Referenzprojekt: {a("/referenzen/#gewerbe-oberoesterreich", "Gewerbe Oberösterreich, 40 kWp")}.</p>
    </div>
  </section>"""


def _tax_section():
    return C.facts_panel(
        eyebrow="Steuer und Bilanz",
        h2="Steuer und Bilanz: Betriebsausgabe, Abschreibung, Elektrizitätsabgabe",
        intro=("Allgemeine Einordnung, keine Steuerberatung: So behandeln Betriebe eine Photovoltaikanlage in der "
               "Regel. Die Details klären Sie mit Ihrer Steuerberatung, wir liefern die Zahlen."),
        rows=[
            ("Anschaffung", "Betriebsvermögen, Abschreibung über die Nutzungsdauer, Vorsteuer abziehbar"),
            ("Laufende Kosten", "Wartung, Versicherung, Monitoring sind Betriebsausgaben"),
            ("Eigenstrom", "selbst erzeugt und verbraucht: befreit von der Elektrizitätsabgabe (1,5 ct je kWh)"),
            ("Einspeiseerlöse", "Betriebseinnahmen zum OeMAG-Marktpreis oder Lieferantentarif"),
            ("Gemischte Nutzung", "Hof und Wohnhaus, Betrieb und Privat: Aufteilung nach Verbrauchsanteil"),
            ("Förderung", "EAG-Zuschuss und EMS-Förderung mindern die Anschaffungskosten"),
        ],
        actions=[("Zahlen für die Steuerberatung anfragen", href("kontakt"), "")],
    )


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        C.hero(
            eyebrow="Photovoltaik Gewerbe: für Betriebe, Höfe und Hotels",
            h1="Photovoltaik für Gewerbe, Landwirtschaft und Hotellerie: Strom produzieren, wenn Ihr Betrieb ihn braucht",
            lead=("Betriebe verbrauchen den meisten Strom tagsüber, wenn die Sonne scheint. Wir planen nach Ihrem "
                  "Lastprofil, montieren mit zertifizierten Fachkräften und übernehmen Förderung und Netzanmeldung. "
                  "Für Hallen, Höfe, Hotels und Werkstätten in Kärnten und der Steiermark."),
            badges=[("Planung", "nach Lastprofil"),
                    ("EAG Kat. C und D", "130 bzw. 120 €/kWp"),
                    ("Gewerbespeicher + EMS", "gegen Lastspitzen")],
            img=IMG["gewerbe_dach"],
            img_alt="Gewerbe-Photovoltaikanlage mit 40 kWp in Ost-West-Ausrichtung auf einem Trapezblechdach in Oberösterreich",
            float_num=rating,
            float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_secondary=("#kosten", "Kosten je kWp ansehen"),
        ),
        C.kpis([
            ("13.500 €", "Ersparnis pro Jahr, Gewerbe OÖ (40 kWp)"),
            ("4.200 €", "Ersparnis pro Jahr, Hotel Villach (13 kWp)"),
            ("700 bis 1.300 €", "je kWp netto, Marktrichtwert 2026*"),
            (NAP["rating"], "Sterne auf Google"),
        ]),
        C.text_block(
            eyebrow="Photovoltaik für Unternehmen",
            h2="Photovoltaik für Betriebe: was wir meinen und für wen",
            paragraphs=[
                ("Auf dieser Seite geht es um Photovoltaik für Unternehmen: Gewerbe, Produktion, Logistik, "
                 "Landwirtschaft, Hotellerie und Gemeinden mit Anlagen von rund 20 bis 1.000 kWp auf Flachdach, "
                 "Trapezblech oder Stalldach. Nicht gemeint ist die Gewerbeanmeldung von Anlagenbetreibern, dazu "
                 "finden Sie eine Antwort in den häufigen Fragen. Jede Planung bei EBZ Energie beginnt mit Ihrem "
                 "Lastprofil, nicht mit der Dachfläche."),
            ],
        ),
        C.problem_compare(
            eyebrow="Warum Gewerbe anders rechnet",
            h2="Warum Photovoltaik im Gewerbe anders rechnet als im Eigenheim",
            intro=("Betriebe erreichen mit Photovoltaik Eigenverbrauchsquoten von 70 Prozent und mehr ohne Speicher*, "
                   "weil der Verbrauch in die Produktionszeit fällt; Haushalte liegen ohne Speicher bei rund 30 Prozent. "
                   "Jede selbst genutzte Kilowattstunde ersetzt Netzbezug zu Stromgestehungskosten von rund 4 bis 7 Cent "
                   f"je kWh*, fix für 25 Jahre ({STAND})."),
            bars=[
                ("Stromkosten ohne eigene Anlage", 100, "bad", "voller Netzbezug"),
                ("Stromkosten mit Photovoltaik und Speicher", 15, "good", "bis zu 85 % weniger*"),
            ],
            aside=("So holen wir den Eigenverbrauch hoch", [
                ("☀", "Lastprofil-Analyse", "Wann braucht Ihr Betrieb wie viel Strom? Darauf legen wir die Anlage aus."),
                ("◇", "Ost-West statt Mittagsspitze", "Zwei Dachseiten liefern vom Morgen bis in den Abend."),
                ("▮", "Speicher für Abend und Spitzen", "Mittagsüberschuss deckt Nachmittag, Abend und Leistungsspitzen."),
                ("⚙", "Energiemanagement", "Das EMS steuert Speicher, Wallboxen und Wärmepumpe nach Produktion und Tarif."),
            ]),
        ),
        _cost_section(),
        C.audience_split(
            eyebrow="Photovoltaik Landwirtschaft, Gewerbe und Hotellerie",
            h2="Gewerbe, Landwirtschaft oder Hotellerie: Ihr Betrieb gibt die Auslegung vor",
            intro=("Jeder Betrieb hat ein anderes Verbrauchsmuster. Wir richten Modulbelegung, Speichergröße "
                   "und Steuerung genau danach aus."),
            left={
                "img": IMG["gen_gewerbe"],
                "alt": "Gewerbehalle mit großflächiger Photovoltaikanlage am Dach",
                "title": "Gewerbe, Produktion und Logistik",
                "bullets": [
                    "Hoher Verbrauch Montag bis Freitag, tagsüber",
                    "Gewerbespeicher und EMS kappen teure Lastspitzen",
                    "Lagerhalle, Kühlhaus, Werkstatt: Flachdach oder Trapezblech",
                ],
                "cta": ("kontakt", "Beratung für meinen Betrieb"),
            },
            right={
                "img": IMG["gewerbe_dach"],
                "alt": "Trapezblechdach eines Betriebsgebäudes mit Photovoltaikmodulen",
                "title": "Landwirtschaft und Hotellerie",
                "bullets": [
                    "Stalldach, Lagerhalle und Scheune statt Freifläche: keine Widmung, kurzer Weg zum Zählpunkt",
                    "Verbrauch auch am Wochenende: Kühlung, Melktechnik, Gastronomie",
                    "Überschüsse in der Energiegemeinschaft teilen, Agri-PV siehe häufige Fragen",
                ],
                "cta": ("kontakt", "Beratung für Hof oder Hotel"),
            },
        ),
        C.media_text(
            eyebrow="Überschuss verwerten: Energiegemeinschaft Gewerbe",
            h2="Überschuss: Überschusseinspeisung, Direktvermarktung oder Energiegemeinschaft",
            paragraphs=[
                ("Standard ist die Überschusseinspeisung: zuerst Eigenverbrauch, der Rest geht zum OeMAG-Marktpreis "
                 "ins Netz. Dieser lag im September 2026 bei 10,168 Cent je kWh, im Juli bei 6,146 Cent und schwankt "
                 f"monatlich ({STAND}). Volleinspeisung lohnt sich bei diesen Preisen nicht, Direktvermarktung erst "
                 "für große Anlagen."),
                ("Am Wochenende und in der Urlaubszeit liefert das Dach weiter. Diesen Überschuss teilen Sie in einer "
                 "Energiegemeinschaft mit Gemeinde, Siedlung oder anderen Betrieben: Im Nahbereich sinken die Netzentgelte "
                 "um bis zu 57 Prozent lokal und 28 Prozent regional, bei Mittelspannungsanschluss bis zu 64 Prozent. "
                 "Österreichweit geht es als Bürgerenergiegemeinschaft ohne Rabatt. Abrechnung über unseren "
                 "Plattformpartner energyfamily."),
            ],
            img=IMG["eg_drohne"],
            alt="Luftaufnahme eines Ortes mit Photovoltaikdächern, Beispiel für eine lokale Energiegemeinschaft",
            bullets=[
                "Voraussetzung EEG: KMU bis 250 Mitarbeiter, sonst Bürgerenergiegemeinschaft",
                "Lastprofil-Analyse zeigt vorab Mengen und Erlöse",
            ],
            reverse=True,
            cta=("eg_gewerbe", "Energiegemeinschaft für Betriebe und Gemeinden"),
        ),
        C.media_text(
            eyebrow="Gewerbespeicher und EMS",
            h2="Gewerbespeicher und EMS: Eigenverbrauch und Lastspitzenkappung",
            paragraphs=[
                ("Betriebe zahlen nicht nur für Kilowattstunden, sondern über den Leistungspreis auch für ihre "
                 "höchste Leistungsspitze. Ein Gewerbespeicher mit Energiemanagementsystem glättet diese Spitzen "
                 "(Lastspitzenkappung, Peak Shaving): Wenn mehrere Maschinen gleichzeitig anlaufen, liefert der "
                 "Speicher den Mehrbedarf, statt dass er aus dem Netz kommt."),
                ("Das EMS steuert zusätzlich Wallboxen, Wärmepumpe und große Verbraucher nach Sonnenstrom und liefert "
                 "die Energiedaten für Energieaudits und ESG-Reporting. Förderung für Betriebe: 30 Prozent, maximal "
                 "20.000 Euro je Standort (Klima- und Energiefonds, bis 15. April 2027)."),
            ],
            img=IMG["ems"],
            alt="Energiemanagementsystem mit Visualisierung von Produktion, Speicher und Verbrauch",
            bullets=[
                "Lastspitzenkappung senkt Leistungspreis und Netzentgelte",
                "Lademanagement für Fuhrpark und Ladepark",
                "Notstrom für Kühlung, Server, Rezeption oder Melktechnik",
            ],
            cta=("ems", "Mehr zum Energiemanagementsystem"),
        ),
        C.media_text(
            eyebrow="Photovoltaik Flachdach",
            h2="Photovoltaik auf dem Flachdach: aufgeständert, Ost-West, ohne Dachdurchdringung",
            paragraphs=[
                ("Flachdächer auf Hallen, Hotels und Bürogebäuden sind ideale PV-Flächen: Die Module werden flach "
                 "aufgeständert, meist in Ost-West-Belegung, und mit Ballast statt Dachdurchdringung befestigt, auf "
                 "Bitumen und Folie mit Bautenschutzmatten. Ballast, Modulgewicht und Schneelast muss das Dach tragen, "
                 "deshalb gehört zu jedem Angebot ein Statikreport. Referenz: das Hotel in Villach/Warmbad, 13 kWp "
                 "bifazial auf Bitumen-Flachdach mit 27 kWh Speicher und Notstrom."),
            ],
            img=IMG["gen_gewerbe"],
            alt="Aufgeständerte Photovoltaikmodule auf dem Flachdach eines Betriebsgebäudes",
            bullets=[
                "Aufständerung mit Ballast, keine Dachdurchdringung",
                "Ost-West-Belegung für gleichmäßige Produktion über den Tag",
                "Wartungsgänge und Blitzschutz eingeplant",
            ],
            reverse=True,
        ),
        C.cards_section(
            eyebrow="Technik, die zu Betriebsdächern passt",
            h2="Komponenten für große Dächer, Netzanschluss und lange Laufzeiten",
            intro=("Betriebsdächer sind oft Trapezblech, Flachdach oder Bitumen. Wir wählen Module und "
                   "Unterkonstruktion passend zur Dachhaut und zur Statik."),
            cards=[
                {"ic": "☀", "title": "Glas-Glas-Module, bifazial",
                 "text": "Beidseitig aktiv, bis zu 30 Jahre Leistungsgarantie, mindestens 10 Jahre Produktgarantie."},
                {"ic": "⌂", "title": "Trapezblech, Flachdach, Bitumen",
                 "text": "Auf Trapezblech auf die Sicken geklemmt, auf Flachdach aufgeständert, immer mit Statikreport belegt."},
                {"ic": "▮", "title": "Gewerbespeicher",
                 "text": "20 bis 100 kWh und mehr, mit Notstromumschaltung über Gatewaybox und Lastspitzenkappung.",
                 "link_key": "batteriespeicher", "link_text": "Zum Batteriespeicher"},
                {"ic": "⚡", "title": "Wallbox und Ladepark",
                 "text": "Fuhrpark und Kundenparkplatz laden mit Sonnenstrom, gesteuert vom EMS, auch als PV-Carport.",
                 "link_key": "carport", "link_text": "Zum PV-Carport"},
                {"ic": "◎", "title": "Netzanschluss und Netzebene",
                 "text": "Ab rund 100 kWp stimmen wir Anschlussleistung, Netzebene und gegebenenfalls Trafo mit dem Netzbetreiber ab."},
                {"ic": "♨", "title": "Wärmepumpe im Betrieb",
                 "text": "Hallen, Büros und Warmwasser mit eigenem Strom heizen.",
                 "link_key": "waermepumpe", "link_text": "Wärmepumpe im Betrieb"},
            ],
        ),
        C.media_text(
            eyebrow="EAG Investitionszuschuss 2026 für Betriebe",
            h2="Förderungen 2026: EAG Kategorie C und D, Fördercall Oktober, Speicher, EMS, Elektrizitätsabgabe",
            paragraphs=[
                ("Der EAG-Investitionszuschuss 2026 fördert Gewerbeanlagen in Kategorie C (über 20 bis 100 kWp) mit "
                 "130 Euro je kWp und in Kategorie D (über 100 bis 1.000 kWp) mit 120 Euro je kWp, dazu kommt die "
                 "Speicherförderung 150 €/kWh bis 50 kWh und 10 Prozent Made-in-Europe-Bonus je Komponente. Der dritte "
                 f"Fördercall 2026 läuft bis 22. Oktober 2026 (Quelle: EAG-Abwicklungsstelle, {STAND})."),
                ("Ab 2027 plant der Bund laut BMWET eine Systemförderung mit Antrag nach der Installation statt "
                 "Fördercall. Für das EMS erhalten Betriebe 30 Prozent, maximal 20.000 Euro je Standort, Registrierung "
                 "vor der Rechnung. Auf selbst erzeugten und verbrauchten Strom entfällt die Elektrizitätsabgabe von "
                 "1,5 Cent je kWh. Reihenfolge und Fristen halten wir ein."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Photovoltaik-Förderung für einen Betrieb",
            bullets=[
                a("foerderung_at", "EAG-Fördercall Oktober 2026: Sätze und Fristen"),
                a("/ems-foerderung/", "EMS-Förderung für Betriebe: 30 % bis 20.000 €"),
                a("/unternehmensfoerderung-von-waermepumpen/", "Wärmepumpenförderung für Unternehmen"),
            ],
            cta=("kontakt", "Förderung für meinen Betrieb prüfen"),
            dark=True,
        ),
        _tax_section(),
        C.media_text(
            eyebrow="Kauf oder Finanzierung statt Contracting",
            h2="Finanzierung statt Contracting: Liquidität bleibt, die Anlage gehört Ihnen",
            paragraphs=[
                ("Beim Contracting bleibt ein Dritter Eigentümer der Anlage und verkauft Ihnen den Strom über 15 bis "
                 "20 Jahre. Bei EBZ Energie gehört die Anlage ab Tag 1 Ihrem Unternehmen: Viele Betriebe kaufen direkt "
                 "und sind typischerweise nach 4 bis 6 Jahren amortisiert. Wer die Liquidität im Betrieb behält, "
                 "finanziert zur fixen Rate: 0 Euro Anzahlung, bis 25 Jahre, Sondertilgung kostenlos, Förderung bleibt "
                 "beim Betrieb."),
            ],
            img=IMG["gen_detail"],
            alt="Montage von Photovoltaikmodulen durch Fachkräfte von EBZ Energie",
            bullets=[
                "Eigentum ab Tag 1, Abschreibung und Vorsteuerabzug wie beim Kauf",
            ],
            cta=("finanzierung", "Finanzierung für Betriebe ansehen"),
        ),
        C.reference_cards(
            eyebrow="Aus der Praxis",
            h2="Referenzen mit Zahlen: 40 kWp in Oberösterreich, Hotel in Villach",
            intro=("Projekte, die zeigen, was Planung nach Lastprofil bringt. Bild und Zahlen gehören "
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
            eyebrow="Zweite Referenz: Hotellerie 24-Stunden-Betrieb",
            h2="Hotel in Villach/Warmbad: Sonnenstrom für den 24-Stunden-Betrieb",
            intro="Ein Hotel läuft rund um die Uhr; bei Netzausfall schaltet die Anlage automatisch auf Notstrom um.",
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
            h2="Ablauf von der Besichtigung bis zum laufenden Betrieb",
            steps=[
                ("Beratung und Besichtigung", "Lastprofil, Dach, Statik und Netzanschluss vor Ort, kostenlos und unverbindlich.", "Woche 1"),
                ("Projektbericht", "Projektbericht mit 3D-Belegplan und Statikreport sowie transparentes Angebot.", "1 bis 2 Wochen"),
                ("Förderung und Anmeldung", "Förderantrag vor der Bestellung, Netzanmeldung, Zählpunkte, Fristen im Blick.", "parallel"),
                ("Montage und Übergabe", "Montage nach Ihren Betriebszeiten, Inbetriebnahme, Einschulung, Monitoring.", "wenige Tage"),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section(
            "Weiterlesen für Betriebe",
            [("photovoltaik", "Photovoltaikanlage für Eigenheim und Gewerbe"),
             ("eg_gewerbe", "Energiegemeinschaft für Betriebe und Gemeinden"),
             ("ems", "Energiemanagementsystem"),
             ("batteriespeicher", "Batteriespeicher"),
             ("foerderung_at", "EAG-Fördercall Oktober 2026"),
             ("/ems-foerderung/", "EMS-Förderung für Betriebe"),
             ("/unternehmensfoerderung-von-waermepumpen/", "Wärmepumpenförderung für Unternehmen"),
             ("waermepumpe", "Wärmepumpe im Betrieb"),
             ("finanzierung", "Finanzierung für Betriebe"),
             ("/referenzen/#gewerbe-oberoesterreich", "Referenz 40 kWp Gewerbe Oberösterreich"),
             ("referenzen", "Alle Referenzen")],
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
    return (f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Marktrichtwerte 2026 vor Förderung: 700 bis 1.300 € je kWp netto, Amortisation 6 bis 12 Jahre,
      Ertrag 900 bis 1.100 kWh je kWp, 5 bis 6 m² je kWp; Stromgestehungskosten rechnerisch (Investition durch Ertrag über
      25 Jahre plus Betrieb). Alles abhängig von Lastprofil, Größe, Ausrichtung und Strompreis. Referenzzahlen aus den
      Projekten Gewerbe Oberösterreich und Hotel Villach/Warmbad. Fördersätze und OeMAG-Marktpreis {STAND}. Steuerliche
      Angaben ersetzen keine Steuerberatung. Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    build()
