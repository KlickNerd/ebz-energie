"""Leistungsseite Energiegemeinschaft fuer Gewerbe, Gemeinden und Mehrparteienhaeuser
(/leistungen/energiegemeinschaft-gewerbe/).

Quelle: Live-LP /energiegemeinschaften-gewerbe/ (freigegebene Inhalte) sowie der Pillar-Ratgeber
/energiegemeinschaft/ und die Cluster-Artikel (gruenden, netzkosten, nachteile). Der eingebettete
Rechner der Live-Seite ist hier durch die Beispielrechnung "Metallbetrieb, 100 kWp" ersetzt.

Pflicht (README): Netzentgelt-Rabatt 57 % lokal / 28 % regional, Netzebene 4/5 bis 64 %, NUR im
Nahbereich; oesterreichweit = Buergerenergiegemeinschaft ohne Rabatt. energyfamily nur als Text-Badge.
"""

from common import IMG, NAP, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

PATH = "/leistungen/energiegemeinschaft-gewerbe/"
TITLE = "Energiegemeinschaft für Betriebe und Gemeinden | EBZ Energie"
DESC = ("Energiegemeinschaft für Betriebe und Gemeinden: 8 bis 12 ct statt 6,146 ct OeMAG für den Überschuss, "
        "bis zu 64 % weniger Netzentgelt. Potenzialanalyse anfragen.")

FAQ = [
    ("Darf mein Unternehmen an einer Erneuerbaren-Energie-Gemeinschaft teilnehmen?",
     "Kleine und mittlere Unternehmen bis 250 Mitarbeiter ja, solange die Teilnahme nicht ihre gewerbliche "
     "Haupttätigkeit ist. Große Unternehmen können über eine Bürgerenergiegemeinschaft oder ab Oktober 2026 "
     "über Peer-to-Peer-Verträge teilnehmen, allerdings ohne Abgabenbefreiung."),
    ("Was bringt die Gemeinschaft einem Betrieb mit eigener PV-Anlage?",
     "An Wochenenden und Feiertagen fällt der Überschuss an, den der Betrieb nicht selbst nutzt. In der "
     "Gemeinschaft erzielt er dafür den vereinbarten EG-Preis, typisch 8 bis 12 Cent, statt des OeMAG-Marktpreises "
     "von 6,146 Cent (Juli 2026). Werktags bezieht der Betrieb bei Bedarf EG-Strom von anderen Mitgliedern mit "
     "reduziertem Netzentgelt."),
    ("Wie kann eine Gemeinde eine Energiegemeinschaft nutzen?",
     "Gemeinden sind ideale Gründer und Mitglieder: Dächer von Schulen, Bauhöfen und Kläranlagen als Erzeuger, "
     "kommunale Gebäude und Straßenbeleuchtung als Abnehmer, Bürgerinnen und Bürger als Mitglieder. EBZ "
     "begleitet Gemeinden von der Potenzialanalyse bis zur Abrechnung und liefert das Reporting für den Gemeinderat."),
    ("Welche Rechtsform ist für eine Gewerbe- oder Gemeinde-EG sinnvoll?",
     "Für kleinere Gemeinschaften der Verein (Gründung etwa 50 bis 150 Euro), für größere mit Investitionen die "
     "Genossenschaft. Entscheidend sind Haftung, Gewinnverteilung und Verwaltungsaufwand. Wir arbeiten mit "
     "Partnern für Rechts- und Steuerberatung zusammen."),
    ("Wie lange dauert es von der Idee bis zum Betrieb?",
     "Die Potenzialanalyse dauert 2 bis 3 Wochen, Modell und Rechtsform 2 bis 4 Wochen, Anlage und Anmeldung "
     "beim Netzbetreiber 4 bis 12 Wochen. Registrierung als Marktteilnehmer und Netzbetreibervertrag sind "
     "kostenlos, die Zählpunktanmeldung wird jeweils zum Monatsersten wirksam."),
    ("Was ist mit dem Versorgungsinfrastrukturbeitrag?",
     "Das ElWG führt für Einspeiser über 20 kW einen Beitrag ein, gedeckelt mit durchschnittlich 0,5 Euro je "
     "MWh, also 0,05 Cent je kWh. Er gilt auch in Energiegemeinschaften und ist wirtschaftlich vernachlässigbar."),
    ("Können Mehrparteienhäuser teilnehmen?",
     "Ja. Im Gebäude teilt eine gemeinschaftliche Erzeugungsanlage (GEA) den Strom ohne Netzentgelt auf die "
     "Wohnungen auf, zusätzlich kann das Haus an einer EEG teilnehmen, um Überschuss an die Nachbarschaft zu "
     "verkaufen. Für Hausverwaltungen übernehmen wir Planung und Betreibermodell."),
]


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        C.hero(
            eyebrow="Energiegemeinschaft für Gewerbe, Gemeinden und Hausverwaltungen",
            h1="Energiegemeinschaft für Betriebe und Gemeinden: Ihr Dach kann mehr als Eigenverbrauch",
            lead=("Werktags verbraucht Ihr Betrieb den Sonnenstrom selbst, am Wochenende geht er zum OeMAG-Marktpreis "
                  "ins Netz. In einer Energiegemeinschaft versorgt dieser Überschuss die Gemeinde, die Siedlung oder "
                  "den Betrieb nebenan, zu einem Preis, den Sie mitbestimmen. EBZ Energie plant Anlage und "
                  "Gemeinschaft aus einer Hand, vom Lastgang bis zur monatlichen Abrechnung."),
            badges=[("50 bis 500 kWp", "typische Dachanlagen"),
                    ("bis zu 64 %", "weniger Netzentgelt auf NE 4/5"),
                    ("8 bis 12 ct*", "statt 6,146 ct OeMAG")],
            img=IMG["gewerbe_dach"],
            img_alt="Große Photovoltaikanlage auf einem Gewerbedach in Oberösterreich, Erzeuger einer Energiegemeinschaft",
            float_num=rating,
            float_label=f"aus {count} Google Bewertungen" if count else "auf Google",
            cta_primary=("kontakt", "Potenzialanalyse anfragen"),
            cta_secondary=("#beispiel", "Beispielrechnung ansehen"),
        ),
        C.kpis([
            ("8 bis 12 ct*", "EG-Preis für den Überschuss statt 6,146 ct OeMAG"),
            ("bis zu 64 %", "Netzentgelt-Abschlag auf Netzebene 4/5"),
            ("125 €/kWp", "Steiermark-Bonus bei Einbindung in ein dezentrales Energiesystem"),
            ("2 bis 1.000+", "Zählpunkte, die energyfamily automatisiert abrechnet"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Was ist eine Energiegemeinschaft für Betriebe und Gemeinden?",
            paragraphs=[
                ("Eine Energiegemeinschaft ist ein Zusammenschluss von mindestens zwei Teilnehmern, die Strom aus "
                 "erneuerbaren Quellen gemeinsam erzeugen, teilen und verbrauchen. Teilnehmen dürfen Gemeinden, "
                 "Vereine, Privathaushalte und kleine und mittlere Unternehmen bis 250 Mitarbeiter, solange die "
                 "Teilnahme nicht ihre gewerbliche Haupttätigkeit ist. Große Unternehmen nutzen die "
                 "Bürgerenergiegemeinschaft, allerdings ohne Abgabenbefreiung."),
                ("Der Strom fließt physikalisch wie bisher über das Netz. Der Netzbetreiber ordnet je Viertelstunde "
                 "zu, wie viel Erzeugung der Gemeinschaft auf wie viel Verbrauch trifft. Nur diese Menge wird zum "
                 "EG-Preis abgerechnet und bekommt im Nahbereich das reduzierte Netzentgelt. Für Betriebe und "
                 "Gemeinden zählt deshalb vor allem eines: der Lastgang."),
            ],
        ),
        C.audience_split(
            eyebrow="Für wen planen wir?",
            h2="Zwei Ausgangslagen, ein Ziel: Strom bleibt in der Region",
            intro=("Ob Betriebsdach oder Gemeindegebäude, wir rechnen mit Ihren Viertelstundenwerten und zeigen vorab, "
                   "welche Mengen und Erlöse realistisch sind."),
            left={
                "img": IMG["gen_gewerbe"],
                "alt": "Gewerbebetrieb mit großer Photovoltaikanlage auf dem Hallendach",
                "title": "Gewerbe und Landwirtschaft: Wochenendüberschuss wird zum zweiten Standbein",
                "bullets": [
                    "50 bis 500 kWp typische Dachanlagen auf Hallen, Ställen und Scheunen",
                    "Werktags Eigenverbrauch, am Wochenende liefert das Dach an die Gemeinschaft",
                    "EG-Preis statt OeMAG-Marktpreis für den Überschuss",
                    "Lastprofil-Analyse zeigt vorab Mengen und Erlöse",
                    "Voraussetzung EEG: KMU bis 250 Mitarbeiter, sonst Bürgerenergiegemeinschaft",
                ],
                "cta": ("kontakt", "Für meinen Betrieb anfragen"),
            },
            right={
                "img": IMG["eg_drohne"],
                "alt": "Ortschaft mit Photovoltaik auf mehreren Dächern, Gemeinde als Energiegemeinschaft",
                "title": "Gemeinden und Hausverwaltungen: Bürgerstrom für Schule, Bauhof und Wohnanlage",
                "bullets": [
                    "Gemeindedächer als Erzeuger, kommunale Gebäude und Straßenbeleuchtung als Abnehmer",
                    "Bürgerinnen und Bürger als Mitglieder einbinden",
                    "Mehrparteienhaus: GEA im Gebäude plus EEG nach außen",
                    "Wertschöpfung und Strompreisvorteil bleiben im Ort",
                    "Reporting für Gemeinderat und Eigentümerversammlung",
                ],
                "cta": ("kontakt", "Für meine Gemeinde anfragen"),
            },
        ),
        C.cards_section(
            eyebrow="Netzebene und Nahbereich",
            h2="Der Netzanschluss entscheidet über Abschlag und Mitgliederkreis",
            intro=("Ob Ihre Gemeinschaft lokal oder regional ist, bestimmt nicht die Gemeindegrenze, sondern Trafo "
                   "und Umspannwerk. Bei Betrieben mit Mittelspannungsanschluss ist die regionale Ebene der Normalfall. "
                   "Die Nahbereichsabfrage je Zählpunkt übernehmen wir beim Netzbetreiber."),
            cards=[
                {"ic": "⌂", "title": "Netzebene 7: Niederspannung",
                 "text": "Haushalte und kleine Betriebe. Am selben Trafo (lokal) minus 57 % Netzentgelt, am selben Umspannwerk (regional) minus 28 %. Dazu entfallen in der EEG Elektrizitätsabgabe und Erneuerbaren-Förderbeitrag."},
                {"ic": "◎", "title": "Netzebene 6: Trafostation",
                 "text": "Betriebe mit eigener Trafo-Anbindung. Die Zuordnung zu lokal oder regional trifft der Netzbetreiber anhand der Zählpunktnummer, nicht anhand der Adresse."},
                {"ic": "◇", "title": "Netzebene 4/5: Mittelspannung",
                 "text": "Bei ausschließlicher Teilnahme auf diesen Ebenen bis zu 64 % Abschlag auf den Arbeitspreis des Netzentgelts. Relevant für größere Betriebe und Industrieareale.",
                 "link_key": "/energiegemeinschaft-netzkosten/", "link_text": "Netzkosten im Detail"},
            ],
        ),
        C.problem_compare(
            eyebrow="Beispielrechnung",
            h2="Metallbetrieb, 100 kWp: Was das Wochenende wert ist",
            intro=("Jahresertrag rund 105.000 kWh, Eigenverbrauch werktags 65 Prozent. Bleiben rund 37.000 kWh "
                   "Überschuss an Wochenenden, Feiertagen und in der Urlaubszeit, die bisher zum OeMAG-Marktpreis ins "
                   "Netz gehen. In der Gemeinschaft mit Gemeinde und Siedlung nebenan werden davon konservativ "
                   "70 Prozent zugeordnet.*"),
            bars=[
                ("Erlös je kWh Wochenendüberschuss bei der OeMAG", 51, "bad", "6,1 ct"),
                ("Erlös je kWh in der Energiegemeinschaft", 83, "good", "8 bis 12 ct*"),
            ],
            aside=("Das Ergebnis im Beispiel", [
                ("€", "Rund 1.000 € Mehrerlös im Jahr", "Für den zugeordneten Anteil (70 % von rund 37.000 kWh) zu 10 statt 6,146 Cent.*"),
                ("◇", "Rund 150 € Netzersparnis", "Beim eigenen EG-Bezug mit reduziertem Netztarif, etwa in der Früh oder im Winter."),
                ("⌂", "Auftritt in der Gemeindezeitung", "Statt einer Zeile auf der OeMAG-Abrechnung: Ihr Strom versorgt den Ort."),
                ("◷", "Belastbare Zahl aus der Potenzialanalyse", "Bei Betrieben mit Wochenendverbrauch (Kühlung, Hotellerie, Landwirtschaft) verschiebt sich das Bild Richtung Abnehmer-Ersparnis."),
            ]),
        ).replace('<section class="section">', '<section class="section" id="beispiel">', 1),
        C.media_text(
            eyebrow="Lastprofile",
            h2="Lastgang statt Bauchgefühl",
            paragraphs=[
                ("Wir rechnen mit Ihren Viertelstundenwerten, nicht mit Prospektzahlen. Die Potenzialanalyse legt "
                 "Dachflächen, Lastgänge, Netzanschluss und Nahbereich aller beteiligten Zählpunkte übereinander. "
                 "Das Ergebnis sind Mengen, Preise und Wirtschaftlichkeit, bevor Sie eine Entscheidung treffen."),
                ("Ein Produktionsbetrieb mit Wochenendstillstand ist der klassische Erzeuger. Kühlhäuser, Hotels oder "
                 "landwirtschaftliche Betriebe mit Verbrauch an sieben Tagen profitieren eher als Abnehmer. Falls nötig, "
                 "legen wir PV-Anlage, Speicher und Lastmanagement so aus, dass der Überschuss dann anfällt, wenn die "
                 "Gemeinschaft ihn braucht."),
            ],
            img=IMG["gen_gewerbe"],
            alt="Photovoltaikanlage auf einem Betriebsdach, geplant nach Lastprofil",
            bullets=[
                "Viertelstundenwerte aller Zählpunkte als Rechengrundlage",
                "Aufteilungsschlüssel statisch oder dynamisch, passend zum Mitgliederkreis",
                "Speicher und " + a("ems", "Energiemanagement") + " verschieben Verbrauch in die richtige Viertelstunde",
            ],
            reverse=True,
            cta=("pv_gewerbe", "Photovoltaik für Gewerbe"),
        ),
        C.facts_panel(
            eyebrow="Abrechnung und Reporting",
            h2="Skalierbare Abrechnung über unseren Partner energyfamily",
            intro=('<span class="hero__badge" style="background:var(--petrol);color:#fff"><b>Partner</b> energyfamily</span><br>'
                   "Die Verwaltung übernimmt die österreichische Plattform energyfamily: monatliche Abrechnung aller "
                   "Zählpunkte, App für die Mitglieder und Reporting für Gemeinderat oder Geschäftsführung. Neue "
                   "Mitglieder werden laufend aufgenommen."),
            rows=[
                ("Plattform", "energyfamily, Datenverarbeitung in Österreich, DSGVO-konform"),
                ("Größe", "von 2 bis über 1.000 Zählpunkte automatisiert"),
                ("Erfahrung", "rund 330 aktive Gemeinschaften, rund 15.000 Nutzer"),
                ("Abrechnung", "monatlich, mit App und Reporting"),
                ("Laufende Kosten", "typisch 2 bis 8 € je Zählpunkt und Monat"),
                ("Registrierung", "Marktteilnehmer-Registrierung und Netzbetreibervertrag kostenlos"),
            ],
            actions=[("Kosten und Abrechnung im Detail", "/energiegemeinschaft-kosten/", "")],
        ),
        C.media_text(
            eyebrow="Förderung und Finanzierung",
            h2="Förderungen im Blick, Finanzierung nach Bedarf",
            paragraphs=[
                ("Gefördert wird die Anlage: über den EAG-Investitionszuschuss und die Landesförderungen. In der "
                 "Steiermark kommt bei Einbindung in ein dezentrales Energiesystem ein Bonus von 125 € je kWp dazu. "
                 "Für das Energiemanagement steht seit Juni 2026 die EMS-Förderung des Klimafonds bereit, die "
                 "Teilnahme an einer Energiegemeinschaft ist dort eine zulässige Betriebsoption."),
                ("Der Versorgungsinfrastrukturbeitrag des ElWG für Einspeiser über 20 kW ist mit durchschnittlich "
                 "0,5 € je MWh gedeckelt und wirtschaftlich vernachlässigbar. Wer die Liquidität im Betrieb halten "
                 "will, finanziert die Anlage zur fixen Rate und bleibt ab Tag 1 Eigentümer."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zu Förderung und Finanzierung einer Gewerbe-Photovoltaikanlage",
            bullets=[
                "EAG-Investitionszuschuss und Landesförderungen für PV und Speicher",
                "125 €/kWp Steiermark-Bonus bei EG-Einbindung, " + a("/ems-foerderung/", "EMS-Förderung des Klimafonds"),
                a("finanzierung", "Finanzierung") + ": 0 € Anzahlung, fixe Rate, Eigentum ab Tag 1",
            ],
            cta=("foerderung_at", "Förderungen 2026 im Überblick"),
            dark=True,
        ),
        C.why_section(
            eyebrow="Ihr Partner",
            h2="Warum Betriebe und Gemeinden mit EBZ planen",
            items=[
                ("☀", "Anlage und EG aus einer Hand", "Dachanlage, Speicher, Lastmanagement und Gemeinschaft vom selben Team aus zertifizierten Fachkräften."),
                ("◷", "Lastgang statt Bauchgefühl", "Wir rechnen mit Ihren Viertelstundenwerten, nicht mit Prospektzahlen. Die Potenzialanalyse zeigt, was realistisch ist."),
                ("◎", "Prozesse mit dem Netzbetreiber", "Marktteilnehmer-Registrierung, Netzbetreibervertrag, EDA-Anmeldungen: Wir kennen die Abläufe bei Kärnten Netz und Energienetze Steiermark."),
                ("✓", "Skalierbare Abrechnung", "energyfamily rechnet von 2 bis über 1.000 Zählpunkte automatisiert ab, monatlich, mit App und Reporting."),
                ("€", "Förderungen im Blick", "EAG-Investitionszuschuss, Landesförderungen und der Steiermark-Bonus von 125 € je kWp bei EG-Einbindung."),
                ("⌂", "Regional präsent", "Sitz in Villach, Projekte in ganz Kärnten und der Steiermark. Ein Ansprechpartner, vom Erstgespräch bis zum Reporting."),
            ],
        ),
        C.reference_cards(
            eyebrow="Aus der Praxis",
            h2="Erzeuger-Dächer, die sich rechnen",
            intro=("Drei Anlagen aus über 300 dokumentierten Projekten in 6 Bundesländern: Betriebsdach, Wohnanlage "
                   "und Einfamilienhaus, jede mit echten Zahlen."),
            items=[
                {"img": IMG["gewerbe_dach"], "alt": "Große Photovoltaikanlage auf einem Gewerbedach in Oberösterreich",
                 "title": "Gewerbe, Oberösterreich", "specs": "40 kWp Ost-West auf Trapezblech, 40 kWh Speicher, rund 40.000 kWh im Jahr.",
                 "result": "13.500 €", "result_sub": "Ersparnis pro Jahr"},
                {"img": IMG["ref_krumpendorf"], "alt": "Photovoltaikanlage auf einem Mehrparteienhaus in Krumpendorf",
                 "title": "Mehrparteienhaus, Krumpendorf", "specs": "25 kWp mit 25 kWh Speicher und Notstrom.",
                 "result": "4 Tage", "result_sub": "Bauzeit"},
                {"img": IMG["ref_villach"], "alt": "Photovoltaikanlage auf einem Einfamilienhaus in Villach",
                 "title": "Einfamilienhaus, Villach", "specs": "10 kWp Ost-West mit Notstrom, rund 11.000 kWh im Jahr.",
                 "result": "rund 80 %", "result_sub": "weniger Stromkosten"},
            ],
        ),
        C.reviews_slider(reviews, rating, count),
        C.steps_section(
            eyebrow="Unser Vorgehen",
            h2="Von der Potenzialanalyse zum laufenden Betrieb",
            steps=[
                ("Potenzialanalyse",
                 "Dachflächen, Lastgänge, Netzanschluss und Nahbereich aller beteiligten Zählpunkte. Ergebnis: Mengen, Preise, Wirtschaftlichkeit.",
                 "2 bis 3 Wochen"),
                ("Modell und Rechtsform",
                 "Verein oder Genossenschaft, Preisgestaltung, Aufteilungsschlüssel, Mitgliederkreis. Mit Partnern für Rechts- und Steuerfragen. "
                 + a("/energiegemeinschaft-gruenden/", "Ratgeber: Energiegemeinschaft gründen"),
                 "2 bis 4 Wochen"),
                ("Anlage und Anmeldung",
                 "Falls nötig PV-Anlage, Speicher und Lastmanagement. Parallel Registrierung, Netzbetreibervertrag und Zählpunktanmeldungen.",
                 "4 bis 12 Wochen"),
                ("Betrieb und Abrechnung",
                 "Monatliche Abrechnung über energyfamily, Reporting für Gemeinderat oder Geschäftsführung, laufende Aufnahme neuer Mitglieder.",
                 "laufend"),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section("Weiterlesen", [
            ("eg_privat", "Energiegemeinschaft für Privathaushalte"),
            ("/energiegemeinschaft-gruenden/", "Energiegemeinschaft gründen: Schritte"),
            ("/energiegemeinschaft-nachteile/", "Nachteile und worauf Sie achten sollten"),
            ("/oemag-einspeisetarif/", "OeMAG-Einspeisetarif 2026"),
            ("/energiegemeinschaft-kosten/", "Kosten und Abrechnung"),
            ("/energiegemeinschaft-netzkosten/", "Netzkosten im Detail"),
            ("/energiegemeinschaft-steiermark/", "Energiegemeinschaft Steiermark"),
            ("pv_gewerbe", "Photovoltaik für Gewerbe"),
            ("ems", "Energiemanagementsystem"),
            ("referenzen", "Referenzen"),
        ]),
        C.contact_section(
            "Kalkulierbare Energiekosten. Sichtbarer Beitrag für die Region.",
            ("Nennen Sie uns Standort, Dachflächen oder Anlagenleistung und die wichtigsten Verbraucher. Wir melden "
             "uns innerhalb eines Werktags mit dem Vorschlag für ein Erstgespräch vor Ort. Unverbindlich und ohne "
             "Verkaufsdruck."),
        ),
        C.finalcta(
            "Ihr Dach kann mehr als Eigenverbrauch",
            ("Potenzialanalyse anfragen und in wenigen Wochen wissen, was Ihre Flächen in einer Energiegemeinschaft "
             "wert sind."),
            cta=("kontakt", "Potenzialanalyse anfragen"),
            trust=[(f"{NAP['rating']} auf Google", True), ("300+ Projekte", False),
                   ("Potenzialanalyse in 2 bis 3 Wochen", False), ("Ein Ansprechpartner bis zum Reporting", False)],
        ),
        f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Beispielkonditionen (10 statt 6,146 ct je kWh), jede Gemeinschaft legt ihre Preise selbst
      fest. OeMAG-Marktpreis Juli 2026: 6,146 ct je kWh. Netzentgelt-Abschlag (lokal 57 %, regional 28 %, Netzebene 4/5
      bis 64 %) und Abgabenbefreiung gelten nur für die zugeordnete Menge und nur im Nahbereich. Die belastbare Zahl
      für Ihren Standort liefert die Potenzialanalyse. Keine Garantie, keine Rechts- oder Steuerberatung. Fachlich
      geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>""",
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=IMG["gewerbe_dach"])
    return write_page("leistungen/energiegemeinschaft-gewerbe/index.html", html)


if __name__ == "__main__":
    build()
