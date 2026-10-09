"""Leistungsseite Balkonkraftwerke (/balkonkraftwerke/).

Quellen: Live-Seite /balkonkraftwerke/, der alte Beitrag /balkonkraftwerk-mit-speicher/ (301 in diese
Seite), Ratgeber /balkonkraftwerk-foerderung-in-oesterreich/, GEO-Datenbasis build/seo/_geo.md
(800 W, Meldung 14 Tage vorher, Zustimmungsfiktion zwei Monate) und das SEO/GEO-Briefing
build/seo/balkonkraftwerke.{json,md} (Stand 9.10.2026; GSC: Steiermark, Kaernten, Graz, Montageservice).

Roter Faden: Hook (mit Speicher, Montage, Anmeldung) -> Oesterreich-Definition (GEO) -> Wohnung oder Haus
(Zustimmungsfiktion) -> 800-Watt-Grenze und Modulleistung 1.200 / 2.000 Wp -> Anmeldung je Netzbetreiber
(Tabelle) -> Ertrag, Verbrauch, Ersparnis (Tabelle) -> Speicher -> Kosten und Amortisation* -> fuenf Gruende
Fachbetrieb -> Foerderung (kurz, Link Ratgeber) -> Dachanlage -> warum EBZ -> Bewertungen -> Ablauf -> FAQ
-> Cluster -> Kontakt. Keine Set-Preise von EBZ; Kostenanker 800 € Set + 400 € Montage laut klimaaktiv*.
Nullsteuersatz seit 1. April 2025 ausgelaufen. Montage nur Kaernten + Steiermark.
"""

from common import IMG, NAP, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

PATH = "/balkonkraftwerke/"
TITLE = "Balkonkraftwerk mit Speicher: Montage in Kärnten | EBZ"
DESC = ("Balkonkraftwerk mit Speicher bis 800 Watt: Montage und Meldung beim Netzbetreiber in Kärnten und "
        "Steiermark. 600 bis 800 kWh im Jahr, für Mieter und Eigentümer.")

FAQ = [
    ("Muss ich mein Balkonkraftwerk bei Kelag oder Energie Steiermark anmelden und wie lange vorher?",
     "Ja, beim Netzbetreiber, nicht beim Stromlieferanten: in Kärnten bei der Kärnten Netz (Kelag-Tochter), in der "
     "Steiermark bei den Energienetzen Steiermark, in Graz bei der Stromnetz Graz. Die Online-Meldung als "
     "Kleinsterzeugungsanlage ist kostenlos und muss mindestens 14 Tage vor der Inbetriebnahme erfolgen."),
    ("Darf ich in Österreich 2.000 Watt Module an einem 800-Watt-Wechselrichter betreiben?",
     "Ja. Begrenzt ist nur die Einspeiseleistung des Wechselrichters: 800 Watt (0,8 kVA). Die Modulleistung ist "
     "frei wählbar, 1.200 oder 2.000 Wp sind üblich und bringen bei Bewölkung, morgens, abends und im Winter mehr "
     "Ertrag. Mit Speicher lädt der Überschuss über 800 Watt die Batterie."),
    ("Wie viel Strom produziert ein 800 Watt Balkonkraftwerk am Tag und im Jahr?",
     "Bei guter Ausrichtung 600 bis 800 kWh im Jahr, im Jahresmittel rund 2 kWh am Tag.* An sonnigen Sommertagen "
     "3 bis 4 kWh, im Dezember oft unter 1 kWh; rund 70 Prozent fallen im Sommerhalbjahr an."),
    ("Was kostet ein Balkonkraftwerk mit Speicher inklusive Montage?",
     "Ein Komplettset mit zwei Modulen, Mikro-Wechselrichter und Halterung kostet im Handel rund 800 €, die "
     "fachgerechte Montage rund 400 € (Richtwerte laut klimaaktiv).* Ein Speicher mit 1 bis 2 kWh kommt dazu. Unser "
     "Angebot nennt Set, Speicher und Montage als eigene Positionen."),
    ("Wann amortisiert sich ein Balkonkraftwerk?",
     "Bei rund 1.200 € für Set und Montage und 180 bis 240 € Ersparnis im Jahr nach 5 bis 7 Jahren.* Mit Speicher "
     "dauert es länger, dafür nutzen Sie auch den Abendverbrauch. Module halten 25 Jahre und mehr."),
    ("Schuko-Stecker vs. Wieland-Stecker: welchen braucht ein Balkonkraftwerk?",
     "Schuko ist in Österreich zulässig, wenn der Stromkreis geeignet ist. Eine Wieland-Einspeisesteckdose ist "
     "berührungsgeschützt, braucht aber einen Elektriker. Wir prüfen Steckdose und Leitungsschutz bei der Montage "
     "und setzen auf Wunsch eine Wieland-Dose."),
    ("Brauche ich die Zustimmung der anderen Wohnungseigentümer?",
     "Seit 1. September 2024 gilt im Wohnungseigentum die Zustimmungsfiktion: Sie informieren die anderen "
     "Eigentümer schriftlich, widerspricht innerhalb von zwei Monaten niemand, gilt die Zustimmung als erteilt. "
     "Mieter brauchen das Okay von Vermieter oder Hausverwaltung. Die technischen Unterlagen liefern wir."),
    ("Was sind die Nachteile eines Balkonkraftwerks?",
     "Die 800-Watt-Grenze deckelt die Leistung, Mittagsüberschuss geht ohne Speicher unvergütet ins Netz, bei "
     "Stromausfall schaltet die Anlage ab, Bundesförderung gibt es keine. Wer mehr will, fährt mit einer kleinen "
     "Dachanlage mit Speicher und 150 € je kWp Förderung oft besser."),
    ("Gibt es eine Förderung für Balkonkraftwerke in Österreich?",
     "Vom Bund nicht: Der EAG-Investitionszuschuss verlangt einen eigenen Einspeisezählpunkt, den ein "
     "Balkonkraftwerk nicht bekommt. Einzelne Länder und Gemeinden haben eigene Programme. Eine kleine, fest "
     "installierte PV-Anlage wird 2026 mit 150 € je kWp gefördert."),
]


def _table_section(eyebrow, h2, intro, headers, rows, note="", anchor=""):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join(
        "<tr>" + "".join(f'<td class="{"hl" if i == 0 else ""}">{c}</td>' for i, c in enumerate(r)) + "</tr>"
        for r in rows
    )
    anchor_attr = f' id="{anchor}"' if anchor else ""
    note_html = f'<p class="form-note center eg-reveal" style="margin-top:18px">{note}</p>' if note else ""
    return f"""
  <section class="section"{anchor_attr} style="background:#fff;border-block:1px solid var(--line)">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">{eyebrow}</p>
      <h2 class="center eg-reveal">{h2}</h2>
      <p class="lead center eg-reveal" style="max-width:72ch;margin-inline:auto">{intro}</p>
      <div class="art-tablewrap eg-reveal" style="margin-top:32px">
        <table class="art-table"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>
      </div>
      {note_html}
    </div>
  </section>"""


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        # 1. Hook
        C.hero(
            eyebrow="Balkonkraftwerk Montage und Anmeldung · Kärnten, Steiermark, Graz, Klagenfurt",
            h1="Balkonkraftwerk mit Speicher: Montage und Anmeldung in Kärnten und der Steiermark",
            lead=("Kühlschrank, Router und Homeoffice laufen tagsüber mit Strom vom eigenen Balkon, der Speicher "
                  "hebt den Rest für den Abend auf. Ein Balkonkraftwerk 800 Watt ist für Mieter wie Eigentümer der "
                  "günstigste Einstieg in Photovoltaik. Wir beraten in Villach, Klagenfurt, Graz und Umgebung, "
                  "montieren sturmsicher und melden die Anlage beim Netzbetreiber."),
            badges=[("800 Watt", "Einspeisegrenze, Module frei"),
                    ("Für Mieter", "und Eigentümer"),
                    ("Speicher", "1 bis 2 kWh optional")],
            img=IMG["balkon"],
            img_alt="Balkonkraftwerk mit zwei Solarmodulen am Geländer eines Wohnungsbalkons",
            float_num=rating,
            float_label=f"aus {count} Google Bewertungen" if count else "auf Google",
            cta_secondary=("#anmeldung", "Anmeldung beim Netzbetreiber"),
        ),
        C.kpis([
            ("800 W", "Einspeisegrenze des Wechselrichters"),
            ("600 bis 800 kWh", "Jahresertrag bei guter Ausrichtung*"),
            ("14 Tage", "vor Inbetriebnahme beim Netzbetreiber melden"),
            ("5 bis 7 Jahre", "Amortisation von Set und Montage*"),
        ]),
        # 2. Definition Oesterreich (GEO)
        C.text_block(
            eyebrow="Balkonkraftwerk Österreich kurz erklärt",
            h2="Was ist ein Balkonkraftwerk?",
            paragraphs=[
                ("Ein Balkonkraftwerk ist in Österreich eine steckerfertige Mini-PV-Anlage mit bis zu 800 Watt "
                 "Wechselrichterleistung. Es gilt als Kleinsterzeugungsanlage, braucht keine Bewilligung und wird "
                 "mindestens 14 Tage vor Inbetriebnahme beim Netzbetreiber gemeldet. Die Modulleistung ist nicht "
                 "begrenzt, 600 bis 800 kWh Jahresertrag sind typisch* (Quelle: E-Control, oesterreich.gv.at, "
                 "Stand Oktober 2026)."),
                ("Ein bis vier Module erzeugen Gleichstrom, der Mikro-Wechselrichter macht daraus 230-Volt-Wechselstrom "
                 "und speist ihn über eine Steckdose in Ihr Hausnetz ein. Geräte, die gerade laufen, nutzen diesen "
                 "Strom zuerst. Montiert wird am Balkongeländer, auf der Loggia, an der Fassade oder auf Flachdach, "
                 "Garage und im Garten. Die Regeln gelten für jedes Balkonkraftwerk mit Speicher österreichweit gleich: "
                 "meldepflichtig, aber ohne zusätzliche Auflagen."),
            ],
        ),
        # 3. Fuer wen (inkl. Zustimmungsfiktion)
        C.audience_split(
            eyebrow="Für wen passt das?",
            h2="Wohnung oder Haus: der passende Einstieg",
            intro=("Ein Balkonkraftwerk ist die kleinste Stufe der Photovoltaik. Wir sagen Ihnen ehrlich, wann sie "
                   "reicht und wann eine kleine Dachanlage mit Förderung die bessere Wahl ist."),
            left={
                "img": IMG["balkon"],
                "alt": "Solarmodule eines Balkonkraftwerks an einem Mehrparteienhaus",
                "title": "Für Mieter und Wohnungseigentümer",
                "bullets": [
                    "Grundlast (Kühlschrank, Router, Standby) und Homeoffice mit Sonnenstrom decken",
                    "Halterung / Montagewinkel für Geländer, Loggia oder Fassade, statisch geprüft und sturmsicher",
                    "Zustimmungsfiktion im Wohnungseigentum seit 1.9.2024 (zwei Monate Widerspruchsfrist): Eigentümer informieren, nicht fragen",
                    "Mieter: Zustimmung von Vermieter oder Hausverwaltung, wir liefern die Unterlagen",
                ],
                "cta": ("kontakt", "Beratung für meine Wohnung"),
            },
            right={
                "img": IMG["gen_eigenheim"],
                "alt": "Einfamilienhaus mit kleiner Photovoltaikanlage auf dem Dach",
                "title": "Für Hausbesitzer",
                "bullets": [
                    "Aufständerung für Garten, Garage, Carport oder Flachdach, oft mit Speicher kombiniert",
                    "Mehr als 800 Watt gewünscht? Eine kleine Dachanlage bekommt 2026 150 € je kWp Förderung",
                    "Später erweiterbar zu Photovoltaikanlage mit Speicher, Wallbox und Notstrom",
                ],
                "cta": ("photovoltaik", "Photovoltaik fürs Eigenheim"),
            },
        ),
        # 4. 800-Watt-Grenze und Modulleistung
        C.media_text(
            eyebrow="Regeln in Österreich",
            h2="800 Watt Einspeisegrenze: warum 1.200 oder 2.000 Watt Module trotzdem erlaubt sind",
            paragraphs=[
                ("Die 800 Watt Einspeisegrenze (Wechselrichter) ist die einzige Leistungsgrenze: Bis 800 Watt, "
                 "genauer 0,8 kVA, gilt Ihre Anlage als Kleinsterzeugungsanlage im vereinfachten Meldeverfahren. Die "
                 "Modulleistung bis 2.000 Wp frei wählbar zu halten, ist ausdrücklich zulässig: Der Mikro-Wechselrichter "
                 "drosselt die Abgabe ins Hausnetz, egal wie viel die Module liefern."),
                ("Warum mehr Modulleistung trotzdem lohnt: Ein 800-Wp-Set erreicht die 800 Watt nur an klaren "
                 "Mittagsstunden. Mit 1.200 oder 2.000 Wp liefern Sie auch morgens, abends und im Winter öfter die volle "
                 "Leistung, ein Speicher dazwischen nimmt den Rest auf. Bifaziale Module nutzen am Geländer auch das "
                 "Licht von hinten."),
            ],
            img=IMG["gen_eigenheim"],
            alt="Wohnhaus mit Solarmodulen, Beispiel für eine gemeldete Kleinsterzeugungsanlage",
            bullets=[
                "Einspeisung: maximal 800 Watt (0,8 kVA) am Wechselrichter",
                "Module: Leistung frei wählbar, 1.200 bis 2.000 Wp üblich, mehr Ertrag bei Schwachlicht",
                "Speicher: nimmt den Überschuss über 800 Watt auf und gibt ihn abends ab",
            ],
            cta=("#anmeldung", "So melden Sie Ihre Anlage"),
        ),
        # 5. Anmeldung je Netzbetreiber
        _table_section(
            eyebrow="Balkonkraftwerk anmelden",
            h2="Anmeldung beim Netzbetreiber: Kärnten Netz, Energienetze Steiermark, Stromnetz Graz",
            intro=("Ein Balkonkraftwerk anmelden heißt in Österreich: Meldung an den Netzbetreiber zwei Wochen vor "
                   "Inbetriebnahme, nicht an den Stromlieferanten. Das Verfahren ist kostenlos und läuft online. Der "
                   "Netzbetreiber prüft, ob Ihr Zähler rückwärts laufen könnte, und tauscht ihn gegebenenfalls gegen "
                   "einen Smart Meter."),
            headers=["Netzgebiet", "Netzbetreiber", "So läuft die Meldung", "Frist"],
            rows=[
                ("Kärnten (Villach, Klagenfurt, Wolfsberg und der Großteil des Landes)",
                 "Kelag / Kärnten Netz GmbH", "Online-Meldung Kleinsterzeugungsanlage bis 800 W, Zählpunktnummer und Datenblatt des Wechselrichters bereithalten", "mindestens 14 Tage vorher"),
                ("Steiermark (außer Graz)",
                 "Energienetze Steiermark / Energie Steiermark", "Online-Meldung Kleinsterzeugungsanlage, Zählpunktnummer und Datenblatt bereithalten", "mindestens 14 Tage vorher"),
                ("Graz",
                 "Stromnetz Graz", "Online-Meldung Kleinsterzeugungsanlage, Zählpunktnummer und Datenblatt bereithalten", "mindestens 14 Tage vorher"),
                ("Alle Netzgebiete",
                 "E-Control (Regulator)", "Legt die 800-Watt-Grenze und das vereinfachte Verfahren fest; Beschwerdestelle bei Problemen", "Stand Oktober 2026"),
            ],
            note=("Smart Meter / Nulleinspeisung: Der digitale Zähler zeigt, wie viel Sie wirklich selbst verbrauchen. "
                  "Eine Nulleinspeisung ist nicht Pflicht, ungenutzter Überschuss wird nur nicht vergütet. "
                  + a("/smart-meter/", "Ratgeber: Smart Meter in Österreich")),
            anchor="anmeldung",
        ),
        # 6. Ertrag, Verbrauch, Ersparnis
        _table_section(
            eyebrow="Ertrag und Ersparnis",
            h2="Was ein 800-Watt-Balkonkraftwerk vom Haushaltsstrom deckt",
            intro=("Ein Haushaltsstromverbrauch 1.400 bis 5.000 kWh im Jahr ist in Österreich die Regel. Ein "
                   "Balkonkraftwerk 800 Watt liefert bei guter Ausrichtung 600 bis 800 kWh*, rund 70 Prozent davon "
                   "im Sommerhalbjahr. Jede selbst verbrauchte Kilowattstunde ersetzt Netzstrom für rund 30 Cent."),
            headers=["Haushalt", "Jahresverbrauch (E-Control)", "Anteil, den das Balkonkraftwerk deckt*", "Ersparnis bei 30 ct/kWh*"],
            rows=[
                ("1-Personen-Haushalt", "rund 1.900 kWh", "30 bis 40 % bei hohem Tagesverbrauch", "180 bis 240 €, mit Speicher am oberen Ende"),
                ("2-Personen-Haushalt", "rund 2.500 bis 3.000 kWh", "20 bis 30 %", "180 bis 240 €"),
                ("4-Personen-Haushalt", "rund 4.700 kWh", "13 bis 17 %", "180 bis 240 €, Speicher lohnt bei Abwesenheit tagsüber"),
                ("Tagesertrag", "Jahresmittel rund 2 kWh", "sonniger Sommertag 3 bis 4 kWh", "Dezember oft unter 1 kWh"),
            ],
            note=("*Richtwerte: 800 Wp Module, Süd bis Ost/West, 30 bis 35 Grad Neigung, keine Verschattung. In der Praxis "
                  "liegen Anlagen laut klimaaktiv zwischen 350 und 700 kWh, je nach Standort und Verbrauchsverhalten."),
        ),
        # 7. Speicher
        C.media_text(
            eyebrow="Balkonkraftwerk mit Speicher",
            h2="Speicher fürs Balkonkraftwerk: tagsüber laden, abends verbrauchen",
            paragraphs=[
                ("Ohne Speicher nutzen Sie den Strom nur, während die Sonne scheint. Wer tagsüber arbeitet, verschenkt "
                 "den Mittagsüberschuss ins Netz, bei Balkonkraftwerken meist ohne Vergütung. Ein Speicher mit 1 bis 2 kWh "
                 "fängt diesen Strom auf und gibt ihn abends ab, wenn Herd, Fernseher und Licht laufen. Der "
                 "Eigenverbrauchsanteil steigt so auf 70 bis 80 %.*"),
                ("Speicher von Anker Solix oder Zendure nutzen Lithium-Eisenphosphat-Zellen (LFP), halten 6.000 "
                 "Ladezyklen und mehr und sind per App überwachbar. Aufstellort: frostfrei und trocken, also überdachter "
                 "Balkon, Abstellraum oder Keller. Notstrom liefert ein Standard-System nicht."),
            ],
            img=IMG["balkon"],
            alt="Balkonkraftwerk mit Solarmodulen und Speicher auf einem Balkon",
            bullets=[
                "1 bis 2 kWh decken die Grundlast über Abend und Nacht",
                "LFP-Zellen mit Batteriemanagement, frostfreier Aufstellort",
                "Erweiterbar, per App steuerbar, Montage und Einbindung durch EBZ",
            ],
            reverse=True,
            cta=("batteriespeicher", "Großer Speicher für die Dachanlage"),
        ),
        # 8. Kosten und Amortisation
        C.problem_compare(
            eyebrow="Was Set und Montage kosten",
            h2="Wann sich ein Balkonkraftwerk rechnet*",
            intro=("Ein Komplettset mit zwei Modulen, Mikro-Wechselrichter und Halterung kostet rund 800 €, die "
                   "fachgerechte Montage rund 400 € (Richtwerte klimaaktiv).* Bei 180 bis 240 € Ersparnis im Jahr ist das "
                   "Geld nach 5 bis 7 Jahren zurück. Ein Speicher verlängert die Amortisation, erhöht aber den nutzbaren Ertrag."),
            bars=[
                ("Ersparnis ohne Speicher (nur direkter Verbrauch am Tag)", 55, "bad", "Teil des Ertrags geht unvergütet ins Netz"),
                ("Ersparnis mit Speicher (70 bis 80 % Eigenverbrauch)", 100, "good", "rund 180 bis 240 € pro Jahr*"),
            ],
            aside=("Was Ihre Ersparnis bestimmt", [
                ("☀", "Ausrichtung und Neigung", "Süden ist ideal, Ost oder West deckt Morgen und Abend, 30 bis 35 Grad Neigung sind optimal."),
                ("◷", "Verbrauch am Tag", "Homeoffice, Kühlgeräte und Router nutzen den Strom direkt, sonst hilft der Speicher."),
                ("€", "Ihr Strompreis", "Je höher der Bezugspreis, desto schneller rechnet sich die Anlage."),
                ("✓", "Qualität", "Module mit 25 bis 30 Jahren Leistungsgarantie, Wechselrichter für 10 bis 15 Jahre."),
            ]),
        ),
        # 9. Fuenf Gruende Fachbetrieb
        C.cards_section(
            eyebrow="Fachbetrieb statt Versandkarton",
            h2="Fünf Gründe für die Montage durch den Fachbetrieb",
            intro=("Ein Set im Online-Shop ist schnell bestellt. Ob es beim nächsten Sturm hält, normgerecht angeschlossen "
                   "ist und nach zwei Jahren noch Strom liefert, entscheiden Komponenten und Montage."),
            cards=[
                {"ic": "✓", "title": "Sicherheit statt Bastellösung",
                 "text": "Wir prüfen Steckdose und Stromkreis und montieren normgerecht mit statisch geprüfter Halterung / Montagewinkel."},
                {"ic": "☀", "title": "Schuko oder Wieland",
                 "text": "Schuko-Stecker vs. Wieland-Stecker: Beides ist zulässig. Wir sagen, was Ihr Stromkreis verträgt, und bauen die Einspeisesteckdose ein."},
                {"ic": "▮", "title": "Speicher richtig dimensioniert",
                 "text": "1 bis 2 kWh reichen für die Grundlast am Abend. Wir integrieren Anker Solix oder Zendure und richten die App ein."},
                {"ic": "◇", "title": "Module, die 25 Jahre halten",
                 "text": "Glas-Glas- oder bifaziale Module aus dem Fachhandel, hagel- und sturmfest, gut bei Schwachlicht."},
                {"ic": "⌂", "title": "Montage, wo Sie wollen",
                 "text": "Loggia / Balkongeländer, Flachdach, Fassade, Garten, Garage: Wir liefern das passende Material und melden die Anlage beim Netzbetreiber.",
                 "link_key": "kontakt", "link_text": "Beratung anfragen"},
            ],
        ),
        # 10. Foerderung (kurz)
        C.media_text(
            eyebrow="Förderung und Steuer",
            h2="Keine Bundesförderung bis 800 W, aber Alternativen",
            paragraphs=[
                ("Der EAG-Investitionszuschuss gilt nicht für Balkonkraftwerke: Er verlangt einen eigenen "
                 "Einspeisezählpunkt, den eine Anlage im vereinfachten Meldeverfahren nicht erhält. Einzelne Länder und "
                 "Gemeinden haben eigene, budgetierte Programme. Der Umsatzsteuer-Nullsatz ist am 31. März 2025 "
                 "ausgelaufen, seit 1. April 2025 gelten wieder 20 Prozent."),
                ("Wer mehr als 800 Watt möchte, fährt oft besser mit einer kleinen Dachanlage: 150 € je kWp und 150 € je "
                 "kWh Speicher vom Bund (2026), in Kärnten dazu 3.000 € Landespauschale ab 5 kWp mit 5 kWh Speicher "
                 "(Call bis 31. Dezember 2026)."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zu Förderung und Anmeldung eines Balkonkraftwerks",
            bullets=[
                "Bund: kein EAG-Zuschuss für Balkonkraftwerke bis 800 Watt",
                "Länder und Gemeinden: teilweise eigene Programme, vor dem Kauf prüfen",
                "Alternative: kleine Dachanlage mit 150 € je kWp Förderung (2026)",
            ],
            cta=("/balkonkraftwerk-foerderung-in-oesterreich/", "Ratgeber: Balkonkraftwerk-Förderung in Österreich"),
        ),
        # 11. Dachanlage
        C.media_text(
            eyebrow="Wenn der Balkon nicht reicht",
            h2="Vom Balkonkraftwerk zur Dachanlage mit Speicher und Wallbox",
            paragraphs=[
                ("Wer mit 800 Watt startet, will oft mehr. Der nächste Schritt ist eine Photovoltaikanlage am Dach: "
                 "10 kWp mit Speicher kosten rund 15.000 bis 22.000 € vor Förderung, senken die Stromkosten um bis zu "
                 "85 % und lassen sich ab 147 € im Monat finanzieren, die Anlage gehört Ihnen ab Tag 1.* Dazu planen "
                 "wir Wallbox und Energiemanagement, alles aus einer Hand von den freundlichen Energie-Handwerkern aus Villach."),
            ],
            img=IMG["gen_detail"],
            alt="Montage einer Photovoltaikanlage auf einem Dach durch Fachkräfte von EBZ Energie",
            bullets=[
                a("photovoltaik", "Photovoltaikanlage fürs Dach") + " mit Speicher und Notstrom",
                a("pv_villach", "Photovoltaik in Villach") + " und Umgebung",
                a("finanzierung", "Finanzierung") + " ab 147 € im Monat, Eigentum ab Tag 1",
            ],
            reverse=True,
            anchor="wallbox",
            cta=("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
        ),
        # 12. Warum EBZ
        C.why_section(
            eyebrow="Warum EBZ Energie",
            h2="Ihr Fachbetrieb für Balkonkraftwerke in Kärnten und der Steiermark",
            items=[
                ("✓", "Zertifizierte Fachkräfte", "Normgerechte Montage, statisch geprüfte Befestigung, Prüfung von Steckdose und Stromkreis."),
                ("☀", "Komponenten aus großen Projekten", "Nur Module und Wechselrichter, denen wir auch bei Dachanlagen vertrauen."),
                ("★", "4,9 Sterne auf Google", "Bewertungen von echten Kundinnen und Kunden aus der Region."),
                ("◉", "300+ Projekte", "Erfahrung aus über 300 dokumentierten Anlagen in 6 Bundesländern, vom Balkon bis zum Gewerbedach."),
                ("⌂", "Regional aus Villach", "Montageservice in Villach, Klagenfurt, Wolfsberg, Graz und im Umland. Beratung vor Ort."),
                ("◇", "Mitwachsende Lösung", "Vom Balkonkraftwerk über Speicher bis zur Dachanlage mit Wallbox: ein Ansprechpartner."),
            ],
        ),
        C.reviews_slider(reviews, rating=rating, count=count),
        # 13. Ablauf
        C.steps_section(
            eyebrow="So einfach geht es",
            h2="Vom Gespräch zum eigenen Sonnenstrom",
            steps=[
                ("Beratung", "Wir klären Standort, Ausrichtung, Verschattung, Verbrauch und ob 1, 2 oder 4 Module und ein Speicher sinnvoll sind. Kostenlos.", "Tag 1"),
                ("Set und Angebot", "Sie erhalten ein abgestimmtes Komplettset aus Modulen, Wechselrichter, Halterung und optional Speicher, mit Preis und Ertragsrichtwert.", "wenige Tage"),
                ("Meldung beim Netzbetreiber", "Wir bereiten die Meldung bei Kärnten Netz oder Energienetze Steiermark vor und klären die Zustimmung im Haus.", "14 Tage vor Inbetriebnahme"),
                ("Montage und Start", "Unsere Fachkräfte montieren sturmsicher, prüfen den Anschluss und richten die App ein. Danach produziert Ihr Balkon Strom.", "wenige Stunden"),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section(
            "Weiterlesen: Balkonkraftwerk, Zähler und Einspeisung",
            [("/balkonkraftwerk-foerderung-in-oesterreich/", "Balkonkraftwerk-Förderung in Österreich"),
             ("/smart-meter/", "Smart Meter und Zähler"),
             ("/einspeisetarif-fuer-photovoltaik/", "Einspeisetarif für Photovoltaik"),
             ("batteriespeicher", "Stromspeicher für die Dachanlage"),
             ("photovoltaik", "Photovoltaikanlage fürs Dach"),
             ("pv_villach", "Photovoltaik in Villach"),
             ("finanzierung", "Finanzierung ohne Anzahlung"),
             ("referenzen", "Referenzen")],
        ),
        C.contact_section(
            headline="Welches Balkonkraftwerk passt zu Ihnen?",
            sub=("Schreiben Sie uns, wo die Module hin sollen (Balkon, Fassade, Garten, Flachdach) und wie Ihr Haushalt "
                 "Strom verbraucht. Wir empfehlen das passende Set, mit oder ohne Speicher, und übernehmen die Meldung. "
                 "Kostenlos und unverbindlich."),
            page_label="Leistungsseite Balkonkraftwerke",
        ),
        C.finalcta(
            "Starten Sie klein, aber richtig",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags und sagen Ihnen, "
            "ob Balkonkraftwerk oder Dachanlage für Sie die bessere Wahl ist.",
            trust=[(f"{NAP['rating']} auf Google", True), ("800 Watt normgerecht", False),
                   ("Für Mieter und Eigentümer", False), ("Montage und Meldung inklusive", False)],
        ),
        _footnote(),
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=IMG["balkon"])
    return write_page("balkonkraftwerke/index.html", html)


def _footnote():
    return (f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte: Jahresertrag 600 bis 800 kWh für ein 800-Watt-Balkonkraftwerk bei guter
      Ausrichtung (Praxis laut klimaaktiv 350 bis 700 kWh), Ersparnis bei 30 ct/kWh, Deckungsanteile auf Basis der
      E-Control-Verbrauchswerte, Kostenanker 800 € Set plus 400 € Montage laut klimaaktiv. Ertrag und Ersparnis
      hängen von Standort, Verschattung, Verbrauch und Strompreis ab. Meldefrist und 800-Watt-Grenze laut E-Control,
      Zustimmungsfiktion laut Wohnungseigentumsgesetz, Fördersätze Stand Oktober 2026. Richtpreis und Finanzierung
      der Dachanlage: 10 kWp mit Speicher vor Förderung, Rate abhängig von Angebot und Laufzeit. Fachlich geprüft
      von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import theme
    theme.write_assets()
    build()
