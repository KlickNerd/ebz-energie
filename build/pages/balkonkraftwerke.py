"""Leistungsseite Balkonkraftwerke (/balkonkraftwerke/).

Quellen: Live-Seite /balkonkraftwerke/ und der alte Beitrag /balkonkraftwerk-mit-speicher/
(geht per 301 in diese Seite auf). Roter Faden: Hook -> Definition -> fuer wen (Mieter /
Hausbesitzer) -> Vorteile vom Fachbetrieb -> 800-Watt-Regel und Anmeldung -> Speicher-Option
-> Rechnet sich das? -> Foerderung -> Wallbox und groessere Anlage (Zusatzthema) -> warum EBZ
-> Bewertungen -> Ablauf -> FAQ -> Cluster-Links -> Kontakt.

Bereinigt gegenueber der Quelle: "Marktstammdatenregister" (deutsches Register; in
Oesterreich gilt die Meldung beim Netzbetreiber), Gedankenstriche, "Kaernten, Salzburg und
der Steiermark" (Montage nur Kaernten + Steiermark), "ueber 100 Anlagen pro Jahr" (300+
Projekte), Zeitbezuege "2024 und 2025" entfernt, doppelte Nummerierung "04.", "finanziert
sich quasi von selbst" und aehnliche Floskeln. Steuer: Nullsteuersatz seit 1. April 2025
ausgelaufen. Keine Set-Preise in der Quelle, daher keine Preisangabe, nur Ersparnis mit Stand.
"""

from common import IMG, NAP, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

PATH = "/balkonkraftwerke/"
TITLE = "Balkonkraftwerk 800 W: Montage, Anmeldung, Speicher | EBZ"
DESC = ("Balkonkraftwerk bis 800 Watt in Kärnten und der Steiermark: Montage, Meldung beim Netzbetreiber, "
        "optional mit Speicher. 600 bis 800 kWh im Jahr, 4,9 Sterne.")

FAQ = [
    ("Wie viel Strom darf ein Balkonkraftwerk einspeisen?",
     "In Österreich gilt eine Anlage bis 800 Watt Wechselrichterleistung als Kleinsterzeugungsanlage und läuft im "
     "vereinfachten Meldeverfahren beim Netzbetreiber. Die Module dürfen mehr Leistung haben, der Wechselrichter "
     "begrenzt die Abgabe ins Hausnetz auf maximal 800 Watt."),
    ("Muss ich mein Balkonkraftwerk anmelden?",
     "Ja. Jede Stromerzeugungsanlage muss vor der Inbetriebnahme beim zuständigen Netzbetreiber gemeldet werden. "
     "Für Balkonkraftwerke bis 800 Watt ist das Verfahren stark vereinfacht, in der Regel kostenlos und läuft über "
     "ein Online-Formular. Der Netzbetreiber prüft dabei, ob Ihr Zähler getauscht werden muss. Wir unterstützen "
     "Sie bei der Meldung."),
    ("Funktioniert das Balkonkraftwerk bei Stromausfall?",
     "Ein Standard-Balkonkraftwerk schaltet bei Stromausfall aus Sicherheitsgründen ab (Netz- und Anlagenschutz). "
     "Es ist keine Notstromlösung. Wer Strom bei Netzausfall möchte, braucht eine Photovoltaikanlage mit "
     "notstromfähigem Speicher."),
    ("Was ist der Unterschied zwischen Balkonkraftwerk und Photovoltaikanlage?",
     "Ein Balkonkraftwerk besteht aus 1 bis 4 Modulen und einem Wechselrichter bis 800 Watt, der in eine Steckdose "
     "eingespeist wird. Eine Photovoltaikanlage wird fest am Dach installiert, hat typischerweise 5 bis 10 kWp und "
     "mehr und braucht einen Elektrofachbetrieb für den Netzanschluss. Dafür bekommt sie Förderung und kann Speicher "
     "und Notstrom integrieren."),
    ("Lohnt sich ein Speicher für das Balkonkraftwerk?",
     "Wenn Sie tagsüber wenig zu Hause sind, ja. Ein Speicher mit 1 bis 3 kWh fängt den Mittagsüberschuss auf und "
     "gibt ihn abends ab, statt ihn unvergütet ins Netz zu geben. So steigt der Eigenverbrauchsanteil auf 70 bis "
     "80 %. Der Speicher kostet allerdings zusätzlich, die Rechnung machen wir mit Ihnen gemeinsam."),
    ("Wie viel spare ich mit einem Balkonkraftwerk?",
     "Ein 800-Watt-Balkonkraftwerk erzeugt in Österreich bei guter Ausrichtung etwa 600 bis 800 kWh im Jahr. "
     "Bei 30 Cent je kWh und hohem Eigenverbrauch sind das rund 180 bis 240 € Ersparnis pro Jahr. Entscheidend ist, "
     "dass Sie den Strom selbst verbrauchen, eingespeister Strom wird bei Balkonkraftwerken meist nicht vergütet."),
    ("Gibt es eine Förderung für Balkonkraftwerke?",
     "Vom Bund nicht: Der EAG-Investitionszuschuss setzt einen eigenen Einspeisezählpunkt voraus, den ein "
     "Balkonkraftwerk im vereinfachten Meldeverfahren nicht bekommt. Einzelne Länder und Gemeinden haben eigene, "
     "budgetierte Programme. Eine kleine, fest installierte PV-Anlage wird dagegen 2026 mit 150 € je kWp gefördert."),
    ("Brauche ich einen Elektriker?",
     "Für Montage und Anschluss an eine geeignete Steckdose in der Regel nicht. Wir prüfen auf Wunsch den Stromkreis "
     "und die Steckdose und montieren Halterung, Module und Wechselrichter normgerecht. Bei einer Einspeisesteckdose "
     "(Wieland) oder Anpassungen in der Hausinstallation übernehmen unsere Fachkräfte den Anschluss."),
]


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        # 1. Hook
        C.hero(
            eyebrow="Balkonkraftwerke in Kärnten und der Steiermark",
            h1="Balkonkraftwerk: Ihr einfacher Einstieg in den eigenen Sonnenstrom",
            lead=("Kühlschrank, Router und Standby-Geräte laufen tagsüber mit Strom vom eigenen Balkon statt vom "
                  "Versorger. Ein Balkonkraftwerk bis 800 Watt ist für Mieter wie Eigentümer die günstigste Art, mit "
                  "Photovoltaik zu starten. Wir beraten, montieren sturmsicher und helfen bei der Meldung an den "
                  "Netzbetreiber."),
            badges=[("800 Watt", "vereinfachtes Verfahren"),
                    ("Für Mieter", "und Eigentümer"),
                    ("Speicher", "optional")],
            img=IMG["balkon"],
            img_alt="Balkonkraftwerk mit zwei Solarmodulen am Geländer eines Wohnungsbalkons",
            float_num=rating,
            float_label=f"aus {count} Google Bewertungen" if count else "auf Google",
            cta_secondary=("#anmeldung", "800-Watt-Regel und Anmeldung"),
        ),
        C.kpis([
            ("800 W", "maximale Wechselrichterleistung"),
            ("600 bis 800 kWh", "Jahresertrag bei guter Ausrichtung*"),
            ("180 bis 240 €", "Ersparnis pro Jahr bei 30 ct/kWh*"),
            (NAP["rating"], "Sterne auf Google"),
        ]),
        # Definition (GEO)
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Was ist ein Balkonkraftwerk?",
            paragraphs=[
                ("Ein Balkonkraftwerk (auch Mini-PV-Anlage oder Steckeranlage) ist eine kleine Solaranlage aus 1 bis 4 "
                 "Modulen, einem Wechselrichter und Halterung. Die Module erzeugen Gleichstrom, der Wechselrichter macht "
                 "daraus 230-Volt-Wechselstrom und speist ihn über eine Steckdose direkt in Ihr Hausnetz ein. Geräte, "
                 "die gerade laufen, nutzen diesen Strom zuerst."),
                ("In Österreich gilt eine Anlage bis 800 Watt Wechselrichterleistung als Kleinsterzeugungsanlage. Sie "
                 "wird im vereinfachten Verfahren beim Netzbetreiber gemeldet und braucht keine Baugenehmigung, wenn sie "
                 "den technischen Normen entspricht. Montiert wird am Balkongeländer, an der Fassade, im Garten, auf "
                 "dem Carport oder auf dem Flachdach."),
            ],
        ),
        # 2. Fuer wen
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
                    "Grundlast des Haushalts decken: Kühlschrank, Router, Standby, Homeoffice",
                    "Halterung für Geländer oder Fassade, statisch geprüft und sturmsicher",
                    "Zustimmung von Hausverwaltung oder Eigentümergemeinschaft klären wir mit",
                ],
                "cta": ("kontakt", "Beratung für meine Wohnung"),
            },
            right={
                "img": IMG["gen_eigenheim"],
                "alt": "Einfamilienhaus mit kleiner Photovoltaikanlage auf dem Dach",
                "title": "Für Hausbesitzer",
                "bullets": [
                    "Aufständerung für Garten, Carport oder Flachdach, oft mit Speicher kombiniert",
                    "Mehr als 800 Watt gewünscht? Eine kleine Dachanlage bekommt 2026 150 € je kWp Förderung",
                    "Später erweiterbar zu Photovoltaikanlage mit Speicher, Wallbox und Notstrom",
                ],
                "cta": ("photovoltaik", "Photovoltaik fürs Eigenheim"),
            },
        ),
        # 3. Vorteile vom Fachbetrieb
        C.cards_section(
            eyebrow="Fachbetrieb statt Versandkarton",
            h2="Fünf Gründe für ein Balkonkraftwerk von EBZ",
            intro=("Ein Set im Online-Shop ist schnell bestellt. Ob es beim nächsten Sturm hält, normgerecht angeschlossen "
                   "ist und nach zwei Jahren noch Strom liefert, entscheidet die Qualität der Komponenten und der Montage."),
            cards=[
                {"ic": "✓", "title": "Sicherheit statt Bastellösung",
                 "text": "Wir prüfen Steckdose und Stromkreis, montieren normgerecht und mit statisch geprüfter Befestigung. Kein Suchen nach einem Elektriker, falls Anpassungen nötig sind."},
                {"ic": "☀", "title": "800 Watt voll ausgenutzt",
                 "text": "Der Wechselrichter regelt die Einspeisung zuverlässig auf 800 Watt. Viele Geräte sind per Software upgradefähig, falls sich der gesetzliche Rahmen ändert."},
                {"ic": "▮", "title": "Speicher-Option für den Abend",
                 "text": "Mit einem Speicher von 1 bis 3 kWh nutzen Sie den Mittagsstrom auch abends. Wir integrieren Systeme etablierter Hersteller wie Anker Solix oder Zendure."},
                {"ic": "◇", "title": "Module, die 20 Jahre halten",
                 "text": "Glas-Glas- oder Glas-Folien-Module aus dem Fachhandel, widerstandsfähig gegen Hagel und Sturm, mit gutem Ertrag auch bei Schwachlicht am Morgen und Abend."},
                {"ic": "⌂", "title": "Montage, wo Sie wollen",
                 "text": "Balkon, Fassade, Garten, Carport oder Flachdach: Wir liefern das passende Befestigungsmaterial und montieren auf Wunsch. Der Wechselrichter sitzt platzsparend hinter den Modulen.",
                 "link_key": "kontakt", "link_text": "Beratung anfragen"},
            ],
        ),
        # 4. 800-Watt-Regel und Anmeldung
        C.media_text(
            eyebrow="Regeln in Österreich",
            h2="800-Watt-Grenze und Meldung beim Netzbetreiber",
            paragraphs=[
                ("Die wichtigste Zahl: 800 Watt. Bis zu dieser Wechselrichterleistung gilt Ihre Anlage als "
                 "Kleinsterzeugungsanlage und durchläuft ein vereinfachtes Meldeverfahren beim Netzbetreiber, meist "
                 "kostenlos über ein Online-Formular. Die Module selbst dürfen mehr Leistung haben, der Wechselrichter "
                 "begrenzt die Abgabe ins Hausnetz."),
                ("Gemeldet wird vor der Inbetriebnahme. Der Netzbetreiber prüft dabei, ob Ihr Zähler rückwärts laufen "
                 "könnte und tauscht ihn gegebenenfalls gegen einen Smart Meter. Für Mieter kommt die Zustimmung von "
                 "Vermieter oder Hausverwaltung dazu, bei Eigentumswohnungen die der Eigentümergemeinschaft. Wir "
                 "bereiten die Meldung mit Ihnen vor und wissen, was die Netzbetreiber in Kärnten und der Steiermark "
                 "verlangen."),
            ],
            img=IMG["gen_eigenheim"],
            alt="Wohnhaus mit Solarmodulen, Beispiel für eine gemeldete Kleinsterzeugungsanlage",
            bullets=[
                "Bis 800 Watt: vereinfachte Meldung, keine Baugenehmigung bei normgerechter Anlage",
                "Anschluss über geeignete Schutzkontaktsteckdose oder Einspeisesteckdose (Wieland)",
                "Smart Meter: Der digitale Zähler zeigt Ihnen, wie viel Sie wirklich selbst verbrauchen",
            ],
            anchor="anmeldung",
            cta=("/smart-meter/", "Ratgeber: Smart Meter in Österreich"),
        ),
        # 5. Speicher-Option
        C.media_text(
            eyebrow="Balkonkraftwerk mit Speicher",
            h2="Tagsüber laden, abends verbrauchen",
            paragraphs=[
                ("Ohne Speicher nutzen Sie den Strom nur, während die Sonne scheint. Wer tagsüber arbeitet, verschenkt "
                 "den Mittagsüberschuss ins Netz, bei Balkonkraftwerken meist ohne Vergütung. Ein Speicher mit 1 bis 3 kWh "
                 "fängt diesen Strom auf und gibt ihn abends ab, wenn Herd, Fernseher und Licht laufen. Der "
                 "Eigenverbrauchsanteil steigt so auf 70 bis 80 %.*"),
                ("Die Speicher basieren auf Lithium-Eisenphosphat-Zellen (LFP), sind für 6.000 bis 10.000 Ladezyklen "
                 "ausgelegt und lassen sich per App überwachen: Erzeugung, Verbrauch, Ladestand in Echtzeit. Modulare "
                 "Systeme wachsen mit, wenn Sie später mehr Kapazität wollen. Notstrom liefert ein Standard-System "
                 "allerdings nicht, dafür braucht es eine Photovoltaikanlage mit notstromfähigem Speicher."),
            ],
            img=IMG["balkon"],
            alt="Balkonkraftwerk mit Solarmodulen und Speicher auf einem Balkon",
            bullets=[
                "1 bis 3 kWh decken die Grundlast eines Haushalts über Abend und Nacht",
                "LFP-Zellen mit Batteriemanagement, 6.000 bis 10.000 Ladezyklen",
                "Erweiterbar, per App steuerbar, Montage und Einbindung durch EBZ",
            ],
            reverse=True,
            cta=("batteriespeicher", "Großer Speicher für die Dachanlage"),
        ),
        # 6. Rechnet sich das?
        C.problem_compare(
            eyebrow="Rechnet sich das?",
            h2="Jede selbst verbrauchte Kilowattstunde spart den vollen Strompreis",
            intro=("Ein Balkonkraftwerk speist nicht für ein paar Cent ein, es ersetzt Strom, den Sie sonst für rund "
                   "30 bis 40 Cent je kWh kaufen. Bei 800 Watt und guter Ausrichtung sind das 600 bis 800 kWh im Jahr.*"),
            bars=[
                ("Ersparnis ohne Speicher (nur direkter Verbrauch am Tag)", 55, "bad", "Teil des Ertrags geht unvergütet ins Netz"),
                ("Ersparnis mit Speicher (70 bis 80 % Eigenverbrauch)", 100, "good", "rund 180 bis 240 € pro Jahr*"),
            ],
            aside=("Was Ihre Ersparnis bestimmt", [
                ("☀", "Ausrichtung und Neigung", "Süden ist ideal, Ost oder West deckt Morgen und Abend. 30 bis 35 Grad Neigung sind in Österreich optimal."),
                ("◷", "Verbrauch am Tag", "Homeoffice, Kühlgeräte und Router nutzen den Strom direkt. Wer tagsüber weg ist, profitiert vom Speicher."),
                ("€", "Ihr Strompreis", "Je höher der Bezugspreis, desto schneller rechnet sich die Anlage."),
                ("✓", "Qualität der Komponenten", "Module mit 25 bis 30 Jahren Leistungsgarantie und ein Wechselrichter, der 10 bis 15 Jahre hält."),
            ]),
        ),
        # 7. Foerderung
        C.media_text(
            eyebrow="Förderung und Steuer",
            h2="Was der Bund fördert und was nicht",
            paragraphs=[
                ("Der EAG-Investitionszuschuss des Bundes gilt nicht für Standard-Balkonkraftwerke bis 800 Watt: Für den "
                 "Antrag ist ein eigener Einspeisezählpunkt nötig, den eine Anlage im vereinfachten Meldeverfahren nicht "
                 "erhält. Einzelne Länder und Gemeinden haben eigene Programme für Steckeranlagen, sie sind budgetiert "
                 "und ändern sich häufig. Wir prüfen die aktuelle Lage für Ihren Wohnort."),
                ("Der Nullsteuersatz auf PV-Anlagen ist am 31. März 2025 ausgelaufen, seit 1. April 2025 gilt wieder der "
                 "reguläre Umsatzsteuersatz von 20 Prozent. Wer mehr als 800 Watt möchte, fährt oft besser mit einer kleinen, "
                 "fest installierten Dachanlage: Sie wird 2026 mit 150 € je kWp gefördert, ein Speicher dazu mit 150 € je kWh."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zu Förderung und Anmeldung eines Balkonkraftwerks",
            bullets=[
                "Bund: kein EAG-Zuschuss für Balkonkraftwerke bis 800 Watt",
                "Länder und Gemeinden: teilweise eigene Programme, vor dem Kauf prüfen",
                "Alternative: kleine Dachanlage mit 150 € je kWp Förderung (2026)",
            ],
            cta=("/balkonkraftwerk-foerderung-in-oesterreich/", "Ratgeber: Balkonkraftwerk-Förderung"),
        ),
        # 8. Zusatzthema: Wallbox und der Schritt zur Dachanlage
        C.media_text(
            eyebrow="Wenn der Balkon nicht reicht",
            h2="Vom Balkonkraftwerk zur Anlage mit Speicher und Wallbox",
            paragraphs=[
                ("Wer mit 800 Watt startet, will oft mehr. Der nächste Schritt ist eine Photovoltaikanlage am Dach: "
                 "10 kWp mit Speicher kosten rund 15.000 bis 22.000 € vor Förderung, senken die Stromkosten um bis zu "
                 "85 % und lassen sich ab 147 € im Monat finanzieren, die Anlage gehört Ihnen ab Tag 1.*"),
                ("Dazu planen wir auf Wunsch eine Wallbox, die Ihr E-Auto mit eigenem Sonnenstrom lädt, und ein "
                 "Energiemanagement, das Speicher, Wallbox und Wärmepumpe abstimmt. Alles aus einer Hand, von den "
                 "freundlichen Energie-Handwerkern aus Villach."),
            ],
            img=IMG["gen_detail"],
            alt="Montage einer Photovoltaikanlage auf einem Dach durch Fachkräfte von EBZ Energie",
            bullets=[
                "Photovoltaikanlage mit Speicher und Notstrom für Eigenheim und Gewerbe",
                "Wallbox fürs E-Auto, gesteuert nach Sonnenstrom",
                "Finanzierung ab 147 € im Monat, Eigentum ab Tag 1, volle Förderung",
            ],
            reverse=True,
            anchor="wallbox",
            cta=("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
        ),
        # 9. Warum EBZ
        C.why_section(
            eyebrow="Warum EBZ Energie",
            h2="Ihr Fachbetrieb für Balkonkraftwerke in Kärnten und der Steiermark",
            items=[
                ("✓", "Zertifizierte Fachkräfte", "Festangestelltes Team, normgerechte Montage, statisch geprüfte Befestigung."),
                ("☀", "Komponenten aus großen Projekten", "Wir verbauen nur Module und Wechselrichter, denen wir auch bei Dachanlagen vertrauen."),
                ("★", "4,9 Sterne auf Google", "Bewertungen von echten Kundinnen und Kunden aus der Region."),
                ("◉", "300+ Projekte", "Erfahrung aus über 300 dokumentierten Anlagen in 6 Bundesländern, vom Balkon bis zum Gewerbedach."),
                ("⌂", "Regional aus Villach", "Beratung, Montage und Service vor Ort in Kärnten und der Steiermark."),
                ("◇", "Mitwachsende Lösung", "Vom Balkonkraftwerk über Speicher bis zur Dachanlage mit Wallbox: ein Ansprechpartner."),
            ],
        ),
        C.reviews_slider(reviews, rating=rating, count=count),
        # 10. Ablauf
        C.steps_section(
            eyebrow="So einfach geht es",
            h2="Vom Gespräch zum eigenen Sonnenstrom",
            steps=[
                ("Beratung", "Wir klären Standort, Ausrichtung, Verschattung, Verbrauch und ob 1, 2 oder 4 Module und ein Speicher sinnvoll sind. Kostenlos.", "Tag 1"),
                ("Set und Angebot", "Sie erhalten ein abgestimmtes Set aus Modulen, Wechselrichter, Halterung und optional Speicher, mit Preis und Ertragsrichtwert.", "wenige Tage"),
                ("Meldung beim Netzbetreiber", "Wir bereiten die vereinfachte Meldung vor und klären Zustimmung von Hausverwaltung oder Vermieter.", "vor der Inbetriebnahme"),
                ("Montage und Start", "Unsere Fachkräfte montieren sturmsicher, prüfen den Anschluss und richten die App ein. Danach produziert Ihr Balkon Strom.", "wenige Stunden"),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section(
            "Weiterlesen: Balkonkraftwerk, Zähler und Einspeisung",
            [("/balkonkraftwerk-foerderung-in-oesterreich/", "Balkonkraftwerk-Förderung in Österreich"),
             ("/smart-meter/", "Smart Meter in Österreich"),
             ("/einspeisetarif-fuer-photovoltaik/", "Einspeisetarif für Photovoltaik"),
             ("batteriespeicher", "Batteriespeicher"),
             ("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
             ("finanzierung", "Finanzierung ohne Anzahlung"),
             ("referenzen", "Referenzen")],
        ),
        C.contact_section(
            headline="Welches Balkonkraftwerk passt zu Ihnen?",
            sub=("Schreiben Sie uns, wo die Module hin sollen (Balkon, Fassade, Garten, Flachdach) und wie Ihr Haushalt "
                 "Strom verbraucht. Wir empfehlen das passende Set, mit oder ohne Speicher. Kostenlos und unverbindlich."),
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
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte: Jahresertrag 600 bis 800 kWh für ein 800-Watt-Balkonkraftwerk bei guter
      Ausrichtung in Österreich, Ersparnis bei 30 ct/kWh und hohem Eigenverbrauch (Angaben der Quelle, Stand 2025).
      Ertrag, Eigenverbrauchsanteil und Ersparnis hängen von Standort, Verschattung, Verbrauchsverhalten und Strompreis
      ab. Richtpreis und Finanzierung für die Dachanlage: 10 kWp mit Speicher, vor Förderung, Rate abhängig von Angebot
      und Laufzeit. Fördersätze Stand 2026. Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import theme
    theme.write_assets()
    build()
