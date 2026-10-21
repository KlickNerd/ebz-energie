"""Ads-Landingpage Energiegemeinschaft fuer Betriebe und Gemeinden (alte WP-Seite /energiegemeinschaften-gewerbe/,
Stand September 2026).

Botschaft der alten LP uebernommen (Anlage und Gemeinschaft aus einer Hand fuer Gewerbe, Landwirtschaft, Gemeinden
und Hausverwaltungen, Wochenendueberschuss, Netzebene und Nahbereich, Potenzialanalyse, 4 Schritte, Abrechnung ueber
energyfamily). Korrigiert: "+3 bis 6 ct je kWh Wochenendueberschuss" und Beispielrechnung mit OeMAG Juli 2026
(6,146 ct, "rund 1.000 Euro Mehrerloes") -> ehrlich mit dem Marktpreis September 2026 (10,168 ct) wie in
eg_gewerbe.py; Foerderbetraege (125 € je kWp Steiermark, EAG-Zuschuss) gestrichen; "eigene zertifizierte
Fachkraefte" -> zertifizierte Fachkraefte; Bewertung 5,0 -> 4,9 (kommt aus den Reviews); Netzentgelt-Rabatt nur im
Nahbereich, oesterreichweit Buergerenergiegemeinschaft ohne Rabatt; eingebetteter Rechner -> Link auf den
EG-Rechner. Leere H1 der alten Seite durch das Anzeigenversprechen ersetzt.
"""

from common import a

LP = {
    "path": "/energiegemeinschaften-gewerbe/",
    "title": "Energiegemeinschaft für Betriebe und Gemeinden | EBZ",
    "description": ("Energiegemeinschaft für Gewerbe, Landwirtschaft, Gemeinden und Hausverwaltungen: EBZ plant Anlage "
                    "und Gemeinschaft aus einer Hand, Netzanmeldung inklusive."),
    "eyebrow": "Energiegemeinschaft für Gewerbe, Landwirtschaft und Gemeinden",
    "h1": "Energiegemeinschaft für Betriebe und Gemeinden: Anlage und Gemeinschaft aus einer Hand",
    "lead": ("Werktags verbraucht Ihr Betrieb den Sonnenstrom selbst, am Wochenende geht der Überschuss zum monatlich "
             "schwankenden OeMAG-Marktpreis ins Netz. In einer Energiegemeinschaft versorgt er die Gemeinde, die "
             "Siedlung oder den Betrieb nebenan, zu einem Preis, den Sie mitbestimmen. EBZ Energie übernimmt "
             "Potenzialanalyse, Rechtsform, Netzanmeldung, Anlage und Abrechnung."),
    "badges": [("50 bis 500 kWp", "typische Dachanlagen"), ("bis zu 64 %", "weniger Netzentgelt im Nahbereich"), ("2 bis 1.000+", "Zählpunkte je Gemeinschaft")],
    "hero_img": "gewerbe_dach",
    "hero_alt": "Photovoltaikanlage auf einem Gewerbedach in Oberösterreich, Erzeuger für eine Energiegemeinschaft",
    "cta": "Potenzialanalyse anfragen",
    "problem": {
        "eyebrow": "Für wen sich das rechnet",
        "h2": "Erzeuger mit großen Dächern, Abnehmer mit Tagesverbrauch",
        "paragraphs": [
            ("Betriebe, Landwirtschaften und Gemeinden haben große Dächer auf Hallen, Ställen, Scheunen, Schulen und "
             "Bauhöfen. Werktags wird der Strom vor Ort gebraucht, an Wochenenden, Feiertagen und in der Urlaubszeit "
             "bleibt Überschuss. Ein Beispiel: Ein Metallbetrieb mit 100 kWp erzeugt rund 105.000 kWh im Jahr, verbraucht "
             "werktags 65 % selbst und hat rund 37.000 kWh Überschuss.*"),
            ("Bisher geht dieser Überschuss zum OeMAG-Marktpreis ins Netz, der monatlich schwankt: 6,146 Cent im Juli, "
             "10,168 Cent im September 2026. In der Energiegemeinschaft gilt ein fix vereinbarter Preis, und beim eigenen "
             "Bezug aus der Gemeinschaft sinkt das Netzentgelt. Ehrlich gerechnet: Bei einem EG-Preis von 10 ct* liegt "
             "der Erlös derzeit knapp unter dem Marktpreis, der sichere Vorteil kommt aus Netzentgelt und Planbarkeit."),
        ],
    },
    "benefits": {
        "eyebrow": "Ihre Vorteile",
        "h2": "Was die Energiegemeinschaft Betrieben und Gemeinden bringt",
        "intro": ("Der Netzanschluss entscheidet über Abschlag und Mitgliederkreis: nicht die Gemeindegrenze, sondern "
                  "Trafostation und Umspannwerk. Die Nahbereichsabfrage je Zählpunkt übernehmen wir."),
        "cards": [
            ("☀", "Fixer Preis für den Wochenendüberschuss",
             "Werktags Eigenverbrauch, am Wochenende liefert das Dach an die Gemeinschaft, zum vereinbarten EG-Preis statt zum schwankenden Marktpreis."),
            ("◇", "Bis zu 64 % weniger Netzentgelt",
             "Im Nahbereich: Netzebene 7 lokal minus 57 %, regional minus 28 %, Netzebene 4/5 bei ausschließlicher Teilnahme bis zu 64 %. Österreichweites Teilen (Bürgerenergiegemeinschaft) ohne Rabatt."),
            ("€", "Abgaben entfallen in der EEG",
             "Elektrizitätsabgabe (1,5 ct je kWh) und Erneuerbaren-Förderbeitrag fallen auf EG-Strom in der Erneuerbaren-Energie-Gemeinschaft weg."),
            ("⌂", "Gemeinden als Gründer",
             "Gemeindedächer als Erzeuger, kommunale Gebäude und Straßenbeleuchtung als Abnehmer, Bürgerinnen und Bürger als Mitglieder. Die Wertschöpfung bleibt im Ort."),
            ("▮", "Mehrparteienhaus: GEA plus EEG",
             "Im Gebäude teilt eine Gemeinschaftliche Erzeugungsanlage den Strom auf die Wohnungen auf, über eine EEG geht der Überschuss an die Nachbarschaft."),
            ("◉", "Skalierbare Abrechnung",
             "Unser Partner energyfamily rechnet von 2 bis über 1.000 Zählpunkte automatisiert ab, monatlich, mit App und Reporting für Gemeinderat oder Geschäftsführung."),
        ],
    },
    "steps": {
        "eyebrow": "Unser Vorgehen",
        "h2": "Von der Potenzialanalyse zum laufenden Betrieb",
        "steps": [
            ("Potenzialanalyse", "Dachflächen, Lastgänge, Netzanschluss und Nahbereich aller beteiligten Zählpunkte. Ergebnis: Mengen, Preise, Wirtschaftlichkeit.", "2 bis 3 Wochen"),
            ("Modell und Rechtsform", "Verein oder Genossenschaft, Preisgestaltung, Aufteilungsschlüssel, Mitgliederkreis. Mit Partnern für Rechts- und Steuerfragen.", "2 bis 4 Wochen"),
            ("Anlage und Anmeldung", "Falls nötig PV-Anlage, Speicher und Lastmanagement. Parallel Registrierung, Netzbetreibervertrag und Zählpunktanmeldungen.", "4 bis 12 Wochen"),
            ("Betrieb und Abrechnung", "Monatliche Abrechnung über energyfamily, Reporting für Gemeinderat oder Geschäftsführung, laufende Aufnahme neuer Mitglieder.", "laufend"),
        ],
    },
    "why": {
        "eyebrow": "Ihr Partner",
        "h2": "Warum Betriebe und Gemeinden mit EBZ planen",
        "items": [
            ("☀", "Anlage und EG aus einer Hand", "Dachanlage, Speicher, Lastmanagement und Gemeinschaft mit zertifizierten Fachkräften und einem festen Ansprechpartner."),
            ("◇", "Lastgang statt Bauchgefühl", "Wir rechnen mit Ihren Viertelstundenwerten, nicht mit Prospektzahlen, und mit dem aktuellen OeMAG-Marktpreis."),
            ("◎", "Prozesse mit dem Netzbetreiber", "Marktpartner-Registrierung, Netzbetreibervertrag, EDA-Anmeldungen: Wir kennen die Abläufe bei Kärnten Netz und Energienetze Steiermark."),
            ("✓", "Skalierbare Abrechnung", "energyfamily: rund 330 Gemeinschaften, rund 15.000 Nutzer, monatliche Abrechnung mit App und Reporting."),
            ("€", "Förderung geprüft", "Wir prüfen den aktuellen Förderstand für Ihr Projekt und übernehmen die Anträge."),
            ("⌂", "Regional präsent", "Sitz in Villach, Projekte in Kärnten und der Steiermark. Ein Ansprechpartner vom Erstgespräch bis zum Reporting."),
        ],
    },
    "refs": ["gewerbe"],
    "refs_h2": "Eine Gewerbeanlage aus der Praxis",
    "contact": {
        "h2": "Potenzialanalyse anfragen",
        "sub": ("Nennen Sie uns Standort, Dachflächen oder Anlagenleistung und die wichtigsten Verbraucher. Wir melden "
                "uns innerhalb eines Werktags mit dem Vorschlag für ein Erstgespräch vor Ort."),
    },
    "faq": [
        ("Darf mein Unternehmen an einer Erneuerbaren-Energie-Gemeinschaft teilnehmen?",
         "Kleine und mittlere Unternehmen bis 250 Mitarbeiter ja, solange die Teilnahme nicht ihre gewerbliche "
         "Haupttätigkeit ist. Große Unternehmen nutzen die Bürgerenergiegemeinschaft oder seit Oktober 2026 "
         "Peer-to-Peer-Verträge, beides ohne Abgabenbefreiung."),
        ("Was bringt die Gemeinschaft einem Betrieb mit eigener PV-Anlage?",
         "Planbarkeit und einen zweiten Abnehmerkreis: Der Wochenendüberschuss bekommt einen fix vereinbarten EG-Preis "
         "statt des monatlich schwankenden OeMAG-Marktpreises. Werktags bezieht der Betrieb bei Bedarf EG-Strom mit "
         "reduziertem Netzentgelt. Eine erste Schätzung liefert unser " + a("eg_rechner", "Energiegemeinschaft-Rechner")
         + ", die belastbare Zahl die Potenzialanalyse mit Ihren Lastgängen."),
        ("Wie kann eine Gemeinde eine Energiegemeinschaft nutzen?",
         "Gemeinden sind ideale Gründer und Mitglieder: Dächer von Schulen, Bauhöfen und Kläranlagen als Erzeuger, "
         "kommunale Gebäude und Straßenbeleuchtung als Abnehmer, Bürgerinnen und Bürger als Mitglieder. EBZ begleitet "
         "Gemeinden von der Potenzialanalyse bis zur Abrechnung."),
        ("Welche Rechtsform ist sinnvoll und was kostet die Gründung?",
         "Für kleinere Gemeinschaften der Verein (etwa 50 bis 150 € Gründungskosten), für größere mit Investitionen die "
         "Genossenschaft. Laufend fallen 2 bis 8 € je Zählpunkt und Monat für Plattform und Abrechnung an. Für Rechts- "
         "und Steuerfragen arbeiten wir mit Partnern zusammen."),
        ("Gilt der Netzentgelt-Rabatt auch bei Standorten in anderen Bundesländern?",
         "Nein. Der Rabatt gilt nur im Nahbereich, also am selben Trafo oder Umspannwerk. Liegen die Standorte weit "
         "auseinander, ist die Bürgerenergiegemeinschaft der Weg, dann ohne Netzentgelt-Rabatt. Für mehrere eigene "
         "Standorte gibt es seit dem ElWG zusätzlich die Eigenversorgungsanlage."),
        ("Was ist mit dem Versorgungsinfrastrukturbeitrag?",
         "Das ElWG führt für Einspeiser über 20 kW einen Beitrag von durchschnittlich 0,05 Cent je kWh ein. Er gilt auch "
         "in Energiegemeinschaften und ist wirtschaftlich vernachlässigbar."),
        ("Können Mehrparteienhäuser teilnehmen?",
         "Ja. Im Gebäude teilt eine Gemeinschaftliche Erzeugungsanlage (GEA) den Strom ohne Netzentgelt auf die "
         "Wohnungen auf, zusätzlich kann das Haus an einer EEG teilnehmen. Für Hausverwaltungen übernehmen wir Planung "
         "und Betreibermodell."),
    ],
    "finalcta": {
        "h2": "Ihr Dach kann mehr als Eigenverbrauch",
        "text": "Potenzialanalyse anfragen und in wenigen Wochen wissen, was Ihre Flächen in einer Energiegemeinschaft wert sind.",
    },
    "footnote": ("*Beispielwerte und Beispielkonditionen: Jede Gemeinschaft legt ihre Preise selbst fest, die belastbare "
                 "Zahl liefert die Potenzialanalyse. OeMAG-Marktpreis laut oem-ag.at, Stand Oktober 2026. "
                 "Netzentgelt-Rabatt und Abgabenbefreiung gelten nur für die zugeordnete Menge und nur im Nahbereich. "
                 "Keine Garantie, keine Rechts- oder Steuerberatung."),
}
