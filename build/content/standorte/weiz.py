"""Ortsseite Weiz (/photovoltaik-weiz/): Inhalte fuer die gemeinsame Vorlage build/pages/standorte.py.

Briefing: build/seo/standort_weiz.json und .md. Alle lokalen Angaben am 10.10.2026 selbst abgerufen:
- Stadt Weiz (weiz.at): 477 m Seehoehe, 17,5 km2, 12.970 Einwohner (davon 12.000 Hauptwohnsitz), 5.632 Haushalte;
  Klimabuendnis- und e5-Gemeinde; Oekofoerderungen 2026 (Heizungstausch 300 EUR fuer Waermepumpe,
  Nah-/Fernwaermeanschluss oder Biomassekessel, +100 EUR je weiterer Wohneinheit, nur ohne Bundesfoerderung;
  Solarthermie 300 EUR; KEINE PV- oder Speicherfoerderung in der Liste); Bauamt Hauptplatz 7, Formular
  "Mitteilung gem. § 21 Stmk. BauG", Ortsbildschutz als Aufgabe des Bauamts (Ortsbildschutzzone).
- Fernwaerme Weiz GmbH (weiz.at/Fernwaerme_Weiz): 50.000 MWh, ca. 80 % des Waermebedarfs in Weiz, zwei Heizanlagen,
  100 % biogene Brennstoffe, im Hauptbesitz der Stadtgemeinde.
- BH Weiz: 31 Gemeinden im Bezirk (Liste unter bh-weiz.steiermark.at).
- Stromnetz Stadt Weiz = Energienetze Steiermark: belegt ueber (a) Energieagentur W.E.I.Z. (PIN fuer die beiden
  Weizer Energiegemeinschaften kommt aus dem Serviceportal der E-Netze Steiermark), (b) Landesrechnungshof
  Steiermark 2014 (Verteilernetz der Pichlerwerke 01/2012 in die Stromnetz Steiermark integriert),
  (c) Pressemitteilung Energie Steiermark 3.7.2023 (Mittelspannungsverstaerkung "vom UW Weiz bis nach Passail",
  6,5 Mio. EUR, bis zu 12 MW neue Einspeisekapazitaet, 2022 bis 2025).
- Energienetze Steiermark, freie Einspeisekapazitaeten je Umspannwerk, Stand 01.07.2026: Weiz 24,5 MW gebucht /
  0,0 MW verfuegbar; Gleisdorf 13,3 / 0,0; Birkfeld 7,0 / 0,9 ("unverbindliche Information ... Momentaufnahme").
  Erzeugungsanlagen-Seite: Einspeiserportal, Netzanschlusskonzept 12 Monate + einmal 12 Monate, netzwirksame
  Leistung, Wirkleistungsvorgabe fuer PV 3,68 bis 250 kW seit 1.12.2024.
- Stromnetz Gleisdorf = Feistritzwerke (gleisdorf.at/energie-strom_118.htm: "zustaendig fuer Stromnetz und
  Netzanschluesse"). Feistritzwerke: flaechenmaessig zweitgroesster steirischer Verteilnetzbetreiber;
  Huellkurvenkonzept vom 31.08.2026 (PDF): Engpass im 110-kV-Netz der Energienetze Steiermark und im APG-Netz in
  Rueckspeiserichtung, neue Anlagen nur netzneutral (Nulleinspeisung), Einspeisung in Randzeiten per Huellkurve,
  Batteriespeicher Voraussetzung, dynamische Regelung am Netzanschlusspunkt, Einstellung am EMS, Bestandsanlagen
  behalten ihre Einspeiseleistung.
- Stadtwerke Gleisdorf: Fernwaerme rund 17 km Leitung, 720 Kunden.
- Energieregion Weiz-Gleisdorf (energieregion.at): 12 Gemeinden, rd. 48.500 Einwohner, KEM seit 2013.
- Energieagentur W.E.I.Z. (innovationszentrum-weiz.at): anerkannte Energieberatungsstelle des Landes,
  Heizungstausch-Beratung vor Ort 150 EUR Selbstkostenbeitrag; zwei EEG in der Stadt (Sued: EnErGie Werk Weiz,
  Nord: Region Umspannwerk WEIZnord).
- Baurecht: Steiermaerkisches Baugesetz idF LGBl. Nr. 20/2026, konsolidierte Fassung des Landes ("BauG April 2026",
  PDF unter technik.steiermark.at/cms/beitrag/11549819/58813874/), selbst gelesen: § 21 lit. o PV und Solarthermie
  auf Dach- oder Fassadenflaechen meldepflichtig (keine Flaechengrenze mehr), Freiflaeche bis 100 kWp, Anlage und
  Teile hoechstens 3,50 m hoch; darueber § 20 Z 2 lit. l (vereinfachtes Verfahren). § 21 Abs. 2 Z 2a Batterieanlagen
  bis 20 kWh meldepflichtig (bis 100 kWh mit Nachweis). § 21 Abs. 2 Z 2b ortsfeste Aufstellung von Waermepumpen
  meldepflichtig; Abs. 3 Z 5: technisches Datenblatt und Bestaetigung eines befugten Sachverstaendigen ueber die
  Einhaltung des Planungsbasispegels an der relevanten Grundgrenze. Deckt sich mit build/pages/standort_graz.py und
  standort_steiermark.py. Der Artikel der LK Steiermark von 2023 (400 m2) ist UEBERHOLT und wird nicht verwendet.
  RIS war nicht abrufbar (Bot-Sperre).
- Foerderung Waermepumpe Land Steiermark: laut build/seo/_fakten_2026-10.md (Nachtrag 10.10.2026) und der
  Vorlage (LAND["stmk"]) derzeit KEINE Antragstellung fuer neue Waermepumpen, Bund ausgeschoepft. Die Inhaltsdatei
  nennt deshalb keinen Landessatz; die KPI-Zeile zeigt statt der Vorlagen-Kachel die belegte Stadtfoerderung.
- Solarpotenzial: SolarTool im Digitalen Atlas Steiermark (technik.steiermark.at).
Nicht belegt und deshalb weggelassen: Ertrag je kWp, Sonnenstunden, Gasnetz, Gemeindefoerderung Gleisdorf,
Netzbetreiber der uebrigen Bezirksgemeinden, Inhalt der Weizer Energieraumplanung (Fernwaerme-Vorgaben).
"""

from common import a

ORT = {
    "key": "pv_weiz",
    "name": "Weiz",
    "kurz": "Weiz",
    "area_name": "Bezirk Weiz",
    "land": "stmk",
    "title": "Photovoltaik Weiz & Gleisdorf: PV und Wärmepumpe | EBZ",
    "description": ("Photovoltaik und Wärmepumpe in Weiz und Gleisdorf: Netzanschluss bei Energienetze Steiermark "
                    "oder Feistritzwerken, 300 € Stadtförderung für den Heizungstausch."),
    "eyebrow": "Photovoltaik und Wärmepumpe im Bezirk Weiz",
    "h1": "Photovoltaik in Weiz und Gleisdorf: PV-Anlage, Speicher und Wärmepumpe vom Fachbetrieb",
    "lead": ("EBZ Energie ist ein Fachbetrieb aus Villach und plant Photovoltaik, Speicher und Wärmepumpen im Bezirk "
             "Weiz vor Ort bei Ihnen. In der Energieregion Weiz-Gleisdorf entscheidet der Netzanschluss über die "
             "Auslegung: Am Umspannwerk Weiz ist derzeit keine freie Einspeisekapazität ausgewiesen, in Gleisdorf "
             "gilt das Hüllkurvenkonzept der Feistritzwerke. Wir planen deshalb auf Eigenverbrauch mit Speicher."),
    "badges": [
        ("Vor Ort", "Beratung in Weiz, Gleisdorf und Umgebung"),
        ("2 Netze", "Energienetze Steiermark und Feistritzwerke"),
        ("300 €", "Stadt Weiz für die Wärmepumpe"),
    ],
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit Photovoltaikanlage auf dem Dach, Symbolbild für Anlagen im Bezirk Weiz",

    "kpis": [
        ("bis zu 85 %", "weniger Stromkosten mit PV und Speicher*"),
        ("300 €", "Stadt Weiz für die Wärmepumpe beim Heizungstausch"),
        ("300+", "dokumentierte Projekte in 6 Bundesländern"),
        ("4,9", "Sterne auf Google"),
    ],

    "intro": {
        "h2": "Warum Photovoltaik und Wärmepumpe im Raum Weiz anders geplant werden",
        "paragraphs": [
            ("Weiz liegt auf 477 Metern Seehöhe in der Oststeiermark und ist Sitz der Bezirkshauptmannschaft für "
             "einen Bezirk mit 31 Gemeinden. Zusammen mit Gleisdorf und zehn weiteren Gemeinden bildet die Stadt die "
             "Energieregion Weiz-Gleisdorf: rund 48.500 Einwohnerinnen und Einwohner, seit 2013 Klima- und "
             "Energie-Modellregion. Gleisdorf nennt sich Solarstadt und führt seit vielen Jahren das Leitbild "
             "„Im Herzen die Sonne“, Weiz ist Klimabündnis- und e5-Gemeinde."),
            ("Diese Vorgeschichte hat eine praktische Folge: In der Region hängt bereits so viel Sonnenstrom am Netz, "
             "dass der Netzanschluss zur wichtigsten Planungsfrage geworden ist. Für das Umspannwerk Weiz weist die "
             "Energienetze Steiermark mit Stand 1. Juli 2026 keine freie Einspeisekapazität aus, die Feistritzwerke "
             "in Gleisdorf nehmen neue Anlagen nur mit einem Hüllkurvenkonzept ans Netz. Eine PV-Anlage rechnet sich "
             "hier über den Strom, den Sie selbst verbrauchen: im Haushalt, im "
             + a("batteriespeicher", "Batteriespeicher") + ", in der Wärmepumpe oder im E-Auto."),
            ("Deshalb planen wir im Bezirk Weiz zuerst den Verbrauch und dann das Dach. Was Ihr Dach liefern kann, "
             "zeigt das SolarTool im Digitalen Atlas des Landes Steiermark für jedes erfasste Gebäude. Wir gleichen "
             "das beim Termin vor Ort mit Dachneigung, Verschattung und Zählerschrank ab. Als Richtwert kostet eine "
             "Anlage mit 10 kWp und Speicher rund 15.000 bis 22.000 Euro vor Förderung.*"),
        ],
    },

    "lokal": {
        "h2": "Weiz und Gleisdorf auf einen Blick: Netz, Behörde, Wärme",
        "intro": ("Die Angaben stammen von Stadtgemeinde, Bezirkshauptmannschaft, Netzbetreibern und Land, Stand "
                  "Oktober 2026. Sie zeigen, mit wem wir für Ihr Projekt sprechen."),
        "rows": [
            ("Bezirk",
             "Weiz, Oststeiermark. 31 Gemeinden, Sitz der Bezirkshauptmannschaft ist die Stadt Weiz."),
            ("Stadt Weiz in Zahlen",
             "477 m Seehöhe, 17,5 km² Fläche, 12.970 Einwohner (davon 12.000 mit Hauptwohnsitz), 5.632 Haushalte "
             "(Angaben der Stadtgemeinde)."),
            ("Stromnetz in Weiz",
             "Energienetze Steiermark GmbH, Antrag über das Einspeiserportal. Umspannwerk Weiz mit Stand "
             "1. Juli 2026: 24,5 MW gebucht, 0,0 MW frei (unverbindliche Momentaufnahme des Netzbetreibers)."),
            ("Stromnetz in Gleisdorf",
             "Feistritzwerke, Gleisdorf. Neue Anlagen nur netzneutral mit Hüllkurvenkonzept: Batteriespeicher und "
             "Energiemanagement sind Voraussetzung für die Einspeisung in den Randzeiten."),
            ("Baubehörde",
             "Die Gemeinde. Stadt Weiz: Bauamt, Hauptplatz 7, 8160 Weiz. PV auf Dach oder Fassade, Speicher bis "
             "20 kWh und Wärmepumpe sind meldepflichtig (§ 21 Stmk. BauG, Fassung 2026)."),
            ("Solarpotenzial",
             "SolarTool im Digitalen Atlas Steiermark (GIS des Landes): Eignung und Ertrag der Dachflächen "
             "erfasster Gebäude, Bericht per E-Mail."),
            ("Wärmeversorgung",
             "Fernwärme Weiz GmbH (im Hauptbesitz der Stadtgemeinde): rund 50.000 MWh im Jahr, etwa 80 % des "
             "Wärmebedarfs in Weiz, biogene Brennstoffe. Gleisdorf: Fernwärme der Stadtwerke, rund 17 km Leitung, "
             "720 Kunden."),
            ("Energieregion",
             "Energieregion Weiz-Gleisdorf: 12 Gemeinden, seit 2013 Klima- und Energie-Modellregion. Weiz ist "
             "Klimabündnis- und e5-Gemeinde."),
            ("Energiegemeinschaften",
             "In der Stadt Weiz gibt es zwei regionale Gemeinschaften, getrennt nach Umspannwerk: EnErGie Werk Weiz "
             "für den Süden, Region Umspannwerk WEIZnord für den Norden. "
             + a("eg_privat", "So funktioniert die Energiegemeinschaft") + "."),
            ("Neutrale Energieberatung",
             "Energieagentur W.E.I.Z. im Innovationszentrum Weiz, anerkannte Energieberatungsstelle des Landes "
             "Steiermark."),
        ],
    },

    "netz": {
        "h2": "Genehmigung und Netzanschluss in Weiz: Bauamt, Energienetze Steiermark, Feistritzwerke",
        "betreiber": "der Energienetze Steiermark oder den Feistritzwerken",
        "paragraphs": [
            ("Baurechtlich ist eine Dachanlage im Bezirk Weiz meist schnell erledigt. Nach dem Steiermärkischen "
             "Baugesetz in der Fassung von 2026 sind Photovoltaikanlagen auf Dach- oder Fassadenflächen "
             "meldepflichtig, solange die Anlage und ihre Teile nicht höher als 3,50 Meter sind; erst darüber "
             "braucht es ein vereinfachtes Bewilligungsverfahren. Auch ein Batteriespeicher bis 20 kWh ist nur "
             "meldepflichtig. Die Mitteilung nach § 21 geht vor der Ausführung an die Gemeinde, in der Stadt Weiz an "
             "das Bauamt am Hauptplatz 7, das dafür ein eigenes Formular führt. Weiz hat eine Ortsbildschutzzone: "
             "Liegt Ihr Haus darin, stimmen wir die Anlage vorab mit dem Bauamt ab."),
            ("Den Netzanschluss beantragen wir in der Stadt Weiz bei der Energienetze Steiermark über deren "
             "Einspeiserportal. Sie erhalten zuerst einen Einspeisezählpunkt und danach ein Netzanschlusskonzept. "
             "Es legt fest, wie viel Leistung Ihre Anlage ins Netz abgeben darf (netzwirksame Leistung), gilt "
             "12 Monate und kann einmal um 12 Monate verlängert werden. Die Modulleistung darf laut Netzbetreiber "
             "größer sein, wenn die Anlage die Einspeisung technisch begrenzt. Für das Umspannwerk Weiz nennt der "
             "Netzbetreiber mit Stand 1. Juli 2026 24,5 MW gebuchte und 0,0 MW freie Einspeisekapazität. Das ist "
             "eine unverbindliche Momentaufnahme, jede Anfrage wird einzeln geprüft. Richtung Passail hat die "
             "Energie Steiermark 2023 eine Verstärkung der Mittelspannung ab dem Umspannwerk Weiz angekündigt, die "
             "bis zu 12 MW zusätzliche Einspeisekapazität bringen soll."),
            ("In Gleisdorf sind laut Stadtgemeinde die Feistritzwerke für Stromnetz und Netzanschlüsse zuständig, "
             "nach eigenen Angaben der flächenmäßig zweitgrößte Verteilnetzbetreiber der Steiermark. Dort werden "
             "neue Stromerzeugungsanlagen wegen eines Engpasses im vorgelagerten 110-kV-Netz und im Übertragungsnetz "
             "nur mehr netzneutral angeschlossen, also grundsätzlich mit Nulleinspeisung. Das Hüllkurvenkonzept der "
             "Feistritzwerke (Fassung vom 31. August 2026) erlaubt die Einspeisung in den Randzeiten, setzt aber "
             "einen Batteriespeicher, eine dynamische Regelung am Netzanschlusspunkt und ein passend eingestelltes "
             + a("ems", "Energiemanagementsystem") + " voraus. Bestehende Anlagen behalten ihre Einspeiseleistung. "
             "In den übrigen Gemeinden des Bezirks klären wir den zuständigen Netzbetreiber über Ihren Zählpunkt."),
        ],
        "bullets": [
            "PV auf Dach oder Fassade bis 3,50 m Anlagenhöhe: Mitteilung an die Gemeinde (§ 21 Stmk. BauG)",
            "Stadt Weiz: Energienetze Steiermark, Antrag über das Einspeiserportal",
            "Gleisdorf: Feistritzwerke, Hüllkurvenkonzept mit Speicher und Energiemanagement",
            "Neue PV-Anlagen von 3,68 bis 250 kW bei Energienetze Steiermark: Wirkleistungsvorgabe über den Smart Meter",
        ],
        "img": "ems",
        "alt": "Technikraum mit Energiemanagement-Display, Batteriespeicher und Wechselrichter, Symbolbild",
    },

    "waermepumpe": {
        "h2": "Wärmepumpe in Weiz: erst die Fernwärme prüfen, dann rechnen",
        "paragraphs": [
            ("Weiz ist eine Fernwärmestadt. Die Fernwärme Weiz GmbH, im Hauptbesitz der Stadtgemeinde, liefert nach "
             "eigenen Angaben rund 50.000 MWh Wärme im Jahr und deckt damit etwa 80 Prozent des Wärmebedarfs in "
             "Weiz, erzeugt in zwei Heizanlagen mit biogenen Brennstoffen aus der Region. Liegt die Leitung vor "
             "Ihrem Haus, ist der Anschluss oft die naheliegende Lösung, und das sagen wir Ihnen auch so. In "
             "Gleisdorf betreiben die Stadtwerke ein Fernwärmenetz mit rund 17 Kilometern Leitung für 720 Kunden."),
            ("Die Wärmepumpe ist die Lösung, wo kein Fernwärmeanschluss möglich ist: für Häuser abseits der Trassen "
             "und für alle, die Öl oder Gas ersetzen und den eigenen Sonnenstrom im Haus halten wollen. Eine "
             "Luft-Wasser-Wärmepumpe macht aus 1 kWh Strom 4 bis 5 kWh Wärme und kostet im Einfamilienhaus rund "
             "12.000 bis 22.000 Euro vor Förderung.* Weil die Einspeisung im Raum Weiz und Gleisdorf begrenzt sein "
             "kann, passt sie hier besonders gut zur PV-Anlage: Sie nimmt den Strom ab, den das Netz nicht aufnimmt, "
             "vor allem für Warmwasser und in der Übergangszeit."),
            ("Vor dem Angebot prüfen wir Heizlast, Vorlauftemperatur, Heizkörper und den Aufstellort der "
             "Außeneinheit. Der Aufstellort ist in der Steiermark auch baurechtlich entscheidend: Die Wärmepumpe "
             "ist meldepflichtig, und zur Meldung gehört die Bestätigung eines befugten Sachverständigen, dass der "
             "zulässige Schallpegel an der Grundgrenze zum Nachbarn eingehalten wird. Die Stadt Weiz hat außerdem "
             "eine Energieraumplanung verordnet; ob daraus für Ihr Grundstück Vorgaben zur Wärmeversorgung folgen, "
             "klären wir vorab mit dem Bauamt. Wer eine neutrale Zweitmeinung möchte, findet sie in "
             "Weiz bei der Energieagentur W.E.I.Z., einer anerkannten Energieberatungsstelle des Landes Steiermark: "
             "Die Heizungstausch-Beratung vor Ort kostet dort 150 Euro Selbstkostenbeitrag."),
        ],
        "bullets": [
            "Fernwärme Weiz: etwa 80 % des Wärmebedarfs der Stadt, biogene Brennstoffe",
            "Stadt Weiz: 300 € für Wärmepumpe, Fernwärmeanschluss oder Biomassekessel",
            "Energieagentur W.E.I.Z.: Heizungstausch-Beratung vor Ort, 150 € Selbstkostenbeitrag",
            a("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau"),
        ],
        "img": "waermepumpe",
        "alt": "Luft-Wasser-Wärmepumpe im Garten eines Wohnhauses, Symbolbild für den Heizungstausch im Bezirk Weiz",
    },

    "foerderung_h2": "Förderung in Weiz: 300 Euro von der Stadt für den Heizungstausch",
    "foerderung_lokal": [
        ("Die Stadtgemeinde Weiz fördert den Heizungstausch laut ihren Ökoförderungen für das Jahr 2026 mit "
         "300 Euro für eine Wärmepumpe, einen Nah- oder Fernwärmeanschluss oder einen Biomassekessel, dazu 100 Euro "
         "für jede zusätzliche Wohneinheit. Bedingung: Für dieselbe Anlage wird keine Bundesförderung in Anspruch "
         "genommen. Für solarthermische Anlagen gibt es ebenfalls 300 Euro. Eine eigene Förderung für Photovoltaik "
         "oder Stromspeicher führt die Stadt in ihrer Liste nicht an; sie empfiehlt vor PV, Speicher und "
         "Heizungstausch eine Energieberatung."),
        ("Für Gleisdorf und die anderen Gemeinden im Bezirk Weiz geben wir hier keine Beträge an, weil sich die "
         "Richtlinien von Gemeinde zu Gemeinde unterscheiden und häufig ändern. Wir fragen vor jedem Angebot bei "
         "Ihrer Wohnsitzgemeinde nach, ob es einen Zuschuss für PV, Speicher oder Heizungstausch gibt."),
    ],

    "referenzen": {
        "h2": "Referenzen in der Steiermark: zwei Projekte aus Graz",
        "intro": ("Aus dem Bezirk Weiz haben wir noch kein dokumentiertes Referenzprojekt. Die nächstgelegenen "
                  "Anlagen stehen in Graz: beide mit Speicher und Wallbox, also mit genau der Kombination, die bei "
                  "begrenzter Einspeisung im Raum Weiz und Gleisdorf zählt."),
        "slugs": ["projekt-flachdach-in-graz", "projekt-stadthaus-in-graz"],
    },

    "umgebung": [
        "Gleisdorf", "Birkfeld", "Passail", "St. Ruprecht an der Raab", "Anger", "Pischelsdorf am Kulm",
        "Mortantsch", "Naas", "Thannhausen", "Puch bei Weiz", "Mitterdorf an der Raab", "Sinabelkirchen",
    ],

    "links": [
        ("/energiegemeinschaft-steiermark/", "Energiegemeinschaft in der Steiermark"),
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau"),
        ("/pv-speicher-nachruesten/", "PV-Speicher nachrüsten"),
        ("ems", "Energiemanagementsystem"),
    ],

    "faq": [
        ("Wer ist in Weiz und in Gleisdorf der Stromnetzbetreiber für meine PV-Anlage?",
         "In der Stadt Weiz ist die Energienetze Steiermark GmbH zuständig, dort läuft der Antrag über das "
         "Einspeiserportal. In Gleisdorf sind laut Stadtgemeinde die Feistritzwerke für Stromnetz und "
         "Netzanschlüsse zuständig. In den anderen Gemeinden des Bezirks Weiz kommt es auf die Adresse an: Der "
         "Netzbetreiber steht auf Ihrer Stromrechnung und im Netzzugangsvertrag. Wir prüfen das vor dem Angebot "
         "anhand Ihres Zählpunkts, weil die beiden Netze derzeit unterschiedliche Vorgaben für die Einspeisung "
         "machen."),
        ("Kann ich in Weiz noch Sonnenstrom ins Netz einspeisen?",
         "Das entscheidet das Netzanschlusskonzept für Ihre Adresse. Die Energienetze Steiermark weist für das "
         "Umspannwerk Weiz mit Stand 1. Juli 2026 24,5 MW gebuchte und 0,0 MW freie Einspeisekapazität aus, nennt "
         "das aber eine unverbindliche Momentaufnahme und prüft jede Anfrage einzeln. Die Modulleistung darf größer "
         "sein als die erlaubte Einspeisung, wenn die Anlage sie technisch begrenzt. Wir legen Anlagen in Weiz "
         "deshalb auf hohen Eigenverbrauch mit Speicher aus und beantragen den Zählpunkt früh."),
        ("Was bedeutet das Hüllkurvenkonzept der Feistritzwerke für eine PV-Anlage in Gleisdorf?",
         "Die Feistritzwerke schließen neue Stromerzeugungsanlagen wegen eines Engpasses im vorgelagerten Netz nur "
         "mehr netzneutral an, also grundsätzlich mit Nulleinspeisung. Die Hüllkurve erlaubt die Einspeisung in den "
         "Randzeiten. Voraussetzung sind laut Fassung vom 31. August 2026 ein Batteriespeicher, eine dynamische "
         "Regelung am Netzanschlusspunkt und ein Energiemanagementsystem, in dem die Kurve des zuständigen "
         "Umspannwerks eingestellt wird. Bestehende Anlagen behalten ihre Einspeiseleistung. Wir planen Speicher "
         "und Steuerung von Anfang an passend dazu."),
        ("Brauche ich für eine Photovoltaikanlage in Weiz eine Baubewilligung?",
         "Für eine Anlage auf Dach oder Fassade nein. Sie ist nach Paragraf 21 des Steiermärkischen Baugesetzes "
         "in der Fassung von 2026 meldepflichtig, solange die Anlage und ihre Teile höchstens 3,50 Meter hoch "
         "sind. Die schriftliche Mitteilung geht vor der Ausführung an die Gemeinde, in Weiz an das Bauamt am "
         "Hauptplatz 7. Höhere Anlagen brauchen ein vereinfachtes Bewilligungsverfahren. Liegt Ihr Haus in der "
         "Weizer Ortsbildschutzzone, klären wir die Ausführung vorab mit dem Bauamt. Die Unterlagen bereiten wir "
         "für Sie vor."),
        ("Wärmepumpe oder Fernwärme in Weiz: Was ist sinnvoller?",
         "Das hängt von Ihrer Adresse ab. Die Fernwärme Weiz deckt nach eigenen Angaben etwa 80 Prozent des "
         "Wärmebedarfs der Stadt und arbeitet mit biogenen Brennstoffen aus der Region. Ist ein Anschluss möglich, "
         "ist er oft die einfachere Lösung. Ohne Fernwärmeleitung in der Nähe ist die Wärmepumpe die naheliegende "
         "Alternative zu Öl und Gas, besonders zusammen mit einer PV-Anlage. Wir prüfen beides und sagen offen, wenn "
         "die Fernwärme für Ihr Haus besser passt."),
        ("Fördert die Stadt Weiz die Wärmepumpe oder die Photovoltaikanlage?",
         "Für den Heizungstausch ja: Die Stadtgemeinde Weiz zahlt laut ihren Ökoförderungen für 2026 300 Euro für "
         "eine Wärmepumpe, einen Nah- oder Fernwärmeanschluss oder einen Biomassekessel, dazu 100 Euro je "
         "zusätzlicher Wohneinheit, sofern für die Anlage keine Bundesförderung bezogen wird. Für Photovoltaik und "
         "Stromspeicher führt die Stadt keine eigene Förderung an, hier gilt der Investitionszuschuss des Bundes. "
         "Land und Bund nehmen für neue Wärmepumpen derzeit keine Förderanträge an. Was am Tag Ihrer Anfrage "
         "offen ist, prüfen wir vor dem Angebot."),
        ("Brauche ich in Weiz eine Genehmigung für eine Luft-Wasser-Wärmepumpe?",
         "Eine Baubewilligung nicht, aber eine Meldung. Die ortsfeste Aufstellung einer Wärmepumpe ist nach "
         "Paragraf 21 des Steiermärkischen Baugesetzes in der Fassung von 2026 meldepflichtig. Der Mitteilung an "
         "das Bauamt der Stadtgemeinde Weiz liegen das technische Datenblatt und die Bestätigung eines befugten "
         "Sachverständigen bei, dass der zulässige Schallpegel an der Grundgrenze zum Nachbarn eingehalten wird. "
         "Wir wählen den Aufstellort der Außeneinheit deshalb schon bei der Planung nach dem Schall und bereiten "
         "die Unterlagen vor."),
        ("EBZ Energie sitzt in Villach. Montieren Sie trotzdem in Weiz und Gleisdorf?",
         "Ja. Unser Firmensitz ist die Triglavstraße 15 in Villach, einen Standort in der Steiermark haben wir "
         "nicht. Kärnten und die Steiermark sind unser Montagegebiet: Für die Erstberatung kommen wir zu Ihnen nach "
         "Weiz, Gleisdorf oder in die Gemeinden rundum und sehen uns Dach, Zählerschrank und Heizraum an. Montiert "
         "wird von zertifizierten Fachkräften, ein fester Ansprechpartner begleitet Sie von der Planung bis zur "
         "Übergabe. Unsere nächstgelegenen Referenzen stehen in Graz."),
    ],

    "quellen": [
        ("Stadtgemeinde Weiz: Zahlen zur Stadt (Seehöhe, Fläche, Einwohner, Haushalte)", "https://www.weiz.at/"),
        ("Stadtgemeinde Weiz: Ökoförderungen 2026",
         "https://www.weiz.at/Gemeinde/Umwelt-_Klimaschutz/Oekofoerderungen"),
        ("Stadtgemeinde Weiz: Bauamt und Formulare (Mitteilung nach § 21 Stmk. BauG)",
         "https://www.weiz.at/Services/Bauen_Wohnen/Bauamt"),
        ("Fernwärme Weiz GmbH", "https://www.weiz.at/Fernwaerme_Weiz"),
        ("Bezirkshauptmannschaft Weiz: Gemeinden des Bezirks",
         "https://www.bh-weiz.steiermark.at/cms/ziel/58210179/DE/"),
        ("Energienetze Steiermark: Erzeugungsanlagen und Einspeiserportal",
         "https://www.e-netze.at/Strom/Erzeugungsanlagen/Default.aspx"),
        ("Energienetze Steiermark: freie Einspeisekapazitäten je Umspannwerk (Stand 1. Juli 2026)",
         "https://www.e-netze.at/Service/FEK/Default.aspx"),
        ("Energie Steiermark: Pressemitteilung zum Netzausbau in der Ost- und Südoststeiermark (3. Juli 2023)",
         "https://www.e-steiermark.com/pressemitteilungen/energienetze-steiermark-ein-tochterunternehmen-der-"
         "energie-steiermark-schaffen-die-voraussetzung-dass-ost-und-suedoststeiermark-an-sonnigen-tagen-mehr-als-"
         "die-haelfte-des-gesamten-strombedarfs-des-landes-abdecken-kann"),
        ("Feistritzwerke: Eigenerzeugung anmelden", "https://www.feistritzwerke.at/eigenerzeugung/"),
        ("Feistritzwerke: Hüllkurvenkonzept für Stromerzeugungsanlagen, Fassung 31. August 2026 (PDF)",
         "https://www.feistritzwerke.at/files/fws_huellkurvenkonzept_20260831.pdf"),
        ("Feistritzwerke: Versorgungsgebiet", "https://www.feistritzwerke.at/versorgungsgebiet/"),
        ("Stadtgemeinde Gleisdorf: Energie und Strom", "https://www.gleisdorf.at/energie-strom_118.htm"),
        ("Stadtwerke Gleisdorf: Fernwärme", "https://www.stadtwerke-gleisdorf.at/waerme/"),
        ("Energieregion Weiz-Gleisdorf: die Region und ihre 12 Gemeinden", "https://www.energieregion.at/region/"),
        ("Energieregion Weiz-Gleisdorf: Klima- und Energie-Modellregion", "https://www.energieregion.at/kem/"),
        ("Energieagentur W.E.I.Z.: Energieberatung und Energiegemeinschaften",
         "https://www.innovationszentrum-weiz.at/energieberatung-energiegemeinschaften/"),
        ("Land Steiermark: Steiermärkisches Baugesetz, Fassung LGBl. Nr. 20/2026 (§ 21 Meldepflichtige Vorhaben)",
         "https://www.technik.steiermark.at/cms/beitrag/11549819/58813874/"),
        ("Land Steiermark: Solarpotenzial und SolarTool im Digitalen Atlas",
         "https://www.technik.steiermark.at/cms/beitrag/12756734/99241573/"),
    ],

    "notizen": (
        "Faktenfragen/Unsicherheiten: (1) Stadtfoerderung Weiz fuer die Waermepumpe (300 EUR) setzt voraus, dass "
        "keine Bundesfoerderung bezogen wird; da Bund und Land derzeit keine Antraege annehmen, ist das aktuell der "
        "einzige belegte Zuschuss. Bei neuen Bundes-/Landesprogrammen FAQ und Foerderabsatz anpassen. (2) Netzbetreiber der uebrigen Bezirksgemeinden (Birkfeld, Anger, Passail, "
        "Pischelsdorf, Sinabelkirchen usw.) nicht einzeln belegt; Feistritzwerke nennen keine Gemeindeliste. "
        "(3) Freie Einspeisekapazitaet UW Weiz ist eine Momentaufnahme (Stand 01.07.2026): bei jeder Aktualisierung "
        "der FEK-Tabelle nachziehen. (4) Huellkurvenkonzept Feistritzwerke wird laufend neu gefasst (Dateiname mit "
        "Datum). (5) Gemeindefoerderung Gleisdorf: Seite umweltfoerderungen_365.htm liefert 404, daher keine "
        "Betraege. (6) Energieraumplanung der Stadt Weiz (Verordnung STEK 1.02): Inhalt nicht gelesen; gibt es einen "
        "Fernwaerme-Anschlussbereich mit Anschlussverpflichtung? (7) Oekofoerderung Weiz gilt fuer die Foerderperiode 2026; 2027 neu "
        "pruefen. (8) Kunde: Gibt es Projekte im Bezirk Weiz/Gleisdorf, die als Referenz freigegeben werden koennen? "
        "Hat EBZ schon Anlagen mit Huellkurve/Nulleinspeisung im Feistritzwerke-Netz in Betrieb genommen?"
    ),
}
