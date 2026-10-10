"""Ortsseite St. Veit an der Glan (/photovoltaik-st-veit/): Inhalte fuer die Vorlage build/pages/standorte.py.

Briefing: build/seo/standort_st_veit.json (DataForSEO, Oesterreich/Deutsch, 10.10.2026).
Primaer "photovoltaik st veit" (20/Monat), dazu "photovoltaik st. veit an der glan" (10) und
"photovoltaik st veit glan" (10). Alle Waermepumpen-Varianten ohne messbares Volumen, daher Waermepumpe
als Sekundaerthema ueber Sektion und FAQ. Abgrenzung zu St. Veit im Pongau ueber vollen Namen, Bezirk,
Postleitzahl 9300 und eine FAQ.

Lokale Fakten, alle am 10.10.2026 selbst abgerufen:
- Stadtgemeinde, Seite "Sonne & Energie" (stveit.com): knapp 4 MWp PV im Stadtgebiet, 2 MW auf ehemaliger
  Muelldeponie (2014), 1 MW Sonnenpark, rund 700 kW auf Tennishallen/Schulen/Sportstaetten, ueber 1.300
  Haushalte mit St. Veiter Solarstrom; Fernwaermenetz seit Anfang der 1990er, Biomasse, ueber 70 % der
  Haushalte; "vor ueber 30 Jahren" erneuerbarer Weg; eine von 13 Kleinstaedten "Leuchttuerme fuer resiliente
  Staedte". Der Begriff "Sonnenstadt" steht dort NICHT, daher nicht als Titel der Stadt verwendet.
- Stadtgemeinde, Klimaneutralitaetsfahrplan Version 1.0 vom 31.10.2024 (PDF): Fernwaermenetz 50 km,
  52 GWh/a, etwa 800 Gebaeude, Betreiber KELAG Energie & Waerme, Abwaermenutzung Industrie, Verdichtung und
  Ausbau geplant; Ziel 80 % der PV-geeigneten Daecher bis 2040 auf Basis Solarkataster (Abbildung
  "Solarpotenzialkataster St. Veit/Glan, Quelle KAGIS Energie"); Ausstieg aus Kohle, Oel und Gas bei Wohn-
  und Dienstleistungsgebaeuden bis 2040; Energiesprechtage der KEM Sonnenland Mittelkaernten, Netzwerk
  Energieberatung Kaernten (alle 5 Jahre kostenlos); Ziel Foerderung lokaler und regionaler
  Energiegemeinschaften; e5-Programm, Klimabuendnis.
- Stadtgemeinde, /klimaschutz: Teil der KEM Sonnenland Mittelkaernten, einzige Kaerntner Stadt im
  Leuchtturm-Programm. News 13.05.2026: European Energy Award in Silber (e5).
- Stadtgemeinde, Bauamt: Bau- und Feuerpolizei (Bewilligungen § 6, mitteilungspflichtige Vorhaben § 7 K-BO),
  Stadtplanung und Ortsbildpflege, Denkmalschutz; Rathaus, Hauptplatz 1.
- Stadtgemeinde, Foerderseite: Familienzuschuss, Kultur-, Sportsubvention, Wirtschaftsfoerderung,
  Wohnbeihilfe. Kein PV-/Speicher-/Heizungsprogramm gelistet. (Eine Presseinfo von 2022 zu "bis 1.500 Euro"
  fuer den Ausbau fossiler Heizungen ist online nicht mehr abrufbar, HTTP 404: nicht verwendet.)
- Land Kaernten, EAP-Verfahrensportal "Mitteilungspflichtige Bauvorhaben": § 7 K-BO, u. a. "bauliche Anlagen,
  die erneuerbare Energie [...] erzeugen oder elektrische Energie speichern"; schriftlich vor Beginn an die
  Baubehoerde, kein Bewilligungsverfahren, keine Kosten, Flaechenwidmungs- und Bebauungsplan gelten.
  (RIS und ktn.gv.at waren am 10.10.2026 nicht abrufbar, daher kein Paragrafenzitat aus dem Gesetzestext.)
- Kaernten Netz, /pv.htm: Ablauf Anschlussantrag (Kundenportal, Netzberechnung, Netzzutrittsangebot,
  Netzzugangsvertrag, Fertigstellungsmeldung durch konzessionierten Elektriker), Optionen bei begrenzter
  Einspeisung. /mittelkaernten.htm: Erneuerung 110-kV-Netz zwischen den Umspannwerken St. Veit, Treibach,
  Wietersdorf, Brueckl, rund 38 km, rund 90 Mio. Euro, UVP-Verfahren.
- Kelag, Unternehmensgeschichte: 1947 Eingliederung der Elektrizitaetswerke u. a. der Stadt St. Veit.
- Statistik Austria, "Ein Blick auf die Gemeinde" 20527: 12.178 Einwohner (1.1.2026), Bezirk 53.749;
  GWZ 2021: 2.999 Gebaeude, 2.469 Wohngebaeude, 1.440 mit einer und 417 mit zwei Wohnungen; Bauperioden
  (vor 1981: 372+310+442+307+323 = 1.754 = 58,5 %). Die 20 Bezirksgemeinden ueber die Blaetter 20501 bis
  20534 geprueft.
- oesterreich.gv.at: Bezirkshauptmannschaft Sankt Veit an der Glan, Hauptplatz 28.

Waermepumpen-Zahlen (12.000 bis 22.000 EUR, Altbau 15.000 bis 28.000 EUR, 55 Grad Vorlauf, 1 kWh Strom ->
4 bis 5 kWh Waerme, Montage 2 bis 4 Tage) aus build/pages/waermepumpe.py. Keine Foerderbetraege oder
Prozentsaetze zur Kaerntner Waermepumpen-Foerderung (laut _fakten_2026-10.md in Klaerung).
"""

from common import a

ORT = {
    "key": "pv_st_veit",
    "name": "St. Veit an der Glan",
    "kurz": "St. Veit",
    "area_name": "Bezirk Sankt Veit an der Glan",
    "land": "ktn",
    "title": "Photovoltaik St. Veit an der Glan & Wärmepumpe | EBZ",
    "description": ("Photovoltaik und Wärmepumpe in St. Veit an der Glan: Fachbetrieb aus Villach berät vor Ort. "
                    "Netzanmeldung bei Kärnten Netz, 3.000 € Landespauschale."),
    "h1": "Photovoltaik und Wärmepumpe in St. Veit an der Glan: Sonnenstrom vom eigenen Dach",
    "lead": ("St. Veit an der Glan erzeugt laut Stadtgemeinde bereits knapp 4 Megawatt Peak Sonnenstrom im "
             "Stadtgebiet. Wir bringen die Photovoltaik auf Ihr eigenes Dach und prüfen ehrlich, ob bei Ihnen eine "
             "Wärmepumpe oder der Anschluss an die Fernwärme die bessere Heizung ist. EBZ Energie ist ein "
             "Fachbetrieb aus Villach, vor Ort in St. Veit und im ganzen Bezirk."),
    "badges": [("PV + Wärmepumpe", "aus einer Planung"),
               ("Kärnten Netz", "Netzanmeldung inklusive"),
               ("ab 147 €*", "im Monat finanzieren")],
    "hero_img": "gen_eigenheim",
    "hero_alt": ("Einfamilienhaus mit Photovoltaik-Modulen auf dem Satteldach vor einer Bergkulisse, Symbolbild "
                 "(keine Aufnahme aus St. Veit an der Glan)"),

    "intro": {
        "h2": "Photovoltaik in St. Veit an der Glan: Die Stadt hat vorgelegt, jetzt sind die Hausdächer dran",
        "paragraphs": [
            ("St. Veit an der Glan in Mittelkärnten setzt nach eigenen Angaben seit über 30 Jahren auf erneuerbare "
             "Energie. Laut Stadtgemeinde sind im Stadtgebiet knapp 4 Megawatt Peak Photovoltaik installiert: "
             "2 Megawatt auf einer ehemaligen Mülldeponie (seit 2014 in Betrieb), 1 Megawatt im Sonnenpark "
             "südöstlich des Zentrums und rund 700 Kilowatt auf Tennishallen, Schulen und Sportstätten. Der "
             "Klimaneutralitätsfahrplan der Stadt vom Oktober 2024 geht einen Schritt weiter: Bis 2040 sollen "
             "80 Prozent der dafür geeigneten Dächer eine Photovoltaikanlage tragen."),
            ("Die meisten dieser Dächer gehören Privatleuten. Die Gebäude- und Wohnungszählung 2021 der Statistik "
             "Austria weist für die Stadtgemeinde 2.999 Gebäude aus, davon 2.469 Wohngebäude; 1.857 davon haben "
             "eine oder zwei Wohnungen. Rund 58 Prozent aller Gebäude wurden vor 1981 errichtet. Das sind Häuser "
             "mit eigenem Dach, eigenem Zählerkasten und oft einer Heizung, die in den nächsten Jahren ohnehin "
             "erneuert wird. Genau dort planen wir Photovoltaik, Speicher und "
             + a("waermepumpe", "Wärmepumpe") + " als ein System."),
            ("Als Richtwert für Kärnten rechnen wir mit rund 1.000 bis 1.100 kWh Jahresertrag je kWp*. Eine Anlage "
             "mit 10 kWp liefert damit etwa 10.000 bis 11.000 kWh im Jahr und kostet mit Speicher rund 15.000 bis "
             "22.000 Euro vor Förderung*. Was auf Ihrem Dach in St. Veit tatsächlich Platz hat, zeigt zuerst der "
             "Solarpotenzialkataster des Landes (KAGIS), auf den auch die Stadt ihre Dachplanung stützt, und "
             "danach unser Projektbericht mit 3D-Belegplan und Statikreport."),
        ],
    },

    "lokal": {
        "h2": "St. Veit an der Glan auf einen Blick: Zahlen, Behörden, Netze",
        "intro": ("Diese Angaben brauchen wir für jede Planung in St. Veit. Sie stammen von der Stadtgemeinde, vom "
                  "Land Kärnten, von Kärnten Netz und der Statistik Austria; die Quellen stehen weiter unten."),
        "rows": [
            ("Stadt und Bezirk",
             "Stadtgemeinde St. Veit an der Glan (Postleitzahl 9300), Sitz der Bezirkshauptmannschaft Sankt Veit "
             "an der Glan in Kärnten. 12.178 Einwohnerinnen und Einwohner in der Stadt, 53.749 im Bezirk mit seinen "
             "20 Gemeinden (Statistik Austria, 1.1.2026). Nicht zu verwechseln mit St. Veit im Pongau."),
            ("Gebäudebestand",
             "2.999 Gebäude, davon 2.469 Wohngebäude. 1.440 Wohngebäude haben eine Wohnung, 417 zwei Wohnungen. "
             "1.754 Gebäude (rund 58 %) stammen aus der Zeit vor 1981 (Statistik Austria, Gebäude- und "
             "Wohnungszählung 2021)."),
            ("Stromnetz",
             "Kärnten Netz GmbH. Ein städtisches Elektrizitätswerk gibt es seit Langem nicht mehr: Es wurde laut "
             "Kelag 1947 in die Kelag eingegliedert. Der Netzzutritt für Ihre PV-Anlage läuft über das "
             "Kundenportal von Kärnten Netz."),
            ("Baubehörde",
             "Bauamt der Stadtgemeinde im Rathaus, Hauptplatz 1. Die Bau- und Feuerpolizei ist dort für "
             "mitteilungspflichtige Vorhaben nach § 7 der Kärntner Bauordnung zuständig; Ortsbildpflege und "
             "Denkmalschutz liegen in derselben Abteilung."),
            ("Fernwärme",
             "Netz der Kelag Energie &amp; Wärme: rund 50 km Leitungen, etwa 800 angeschlossene Gebäude, 52 GWh "
             "Wärmeabsatz im Jahr (Klimaneutralitätsfahrplan der Stadt, 2024). Laut Stadt werden über 70 % der "
             "Haushalte mit Fernwärme versorgt."),
            ("Sonnenstrom der Stadt",
             "Knapp 4 Megawatt Peak im Stadtgebiet, darunter 2 MW auf einer ehemaligen Mülldeponie und 1 MW im "
             "Sonnenpark. Über 1.300 Haushalte werden laut Stadt mit St. Veiter Solarstrom versorgt."),
            ("Klima und Energie",
             "e5-Gemeinde mit European Energy Award in Silber (Meldung der Stadt vom Mai 2026), Teil der Klima- und "
             "Energie-Modellregion Sonnenland Mittelkärnten, Klimaneutralitätsfahrplan 2040. Laut Stadt eine von "
             "13 Kleinstädten im Programm „Leuchttürme für resiliente Städte“ des Klima- und Energiefonds und "
             "die einzige in Kärnten."),
            ("Energieberatung",
             "Energiesprechtage der Modellregion Sonnenland Mittelkärnten zu Förderungen für Heizungstausch, "
             "Sanierung, Photovoltaik und Stromsparen; dazu die Energieberatung des Landes (Netzwerk "
             "Energieberatung Kärnten)."),
            ("Energiegemeinschaft",
             "Die Stadt nennt die Förderung lokaler und regionaler Energiegemeinschaften als Ziel bis 2040. Wie Sie "
             "Überschussstrom mit Nachbarn teilen, steht auf unserer Seite zur "
             + a("eg_privat", "Energiegemeinschaft") + "."),
        ],
    },

    "netz": {
        "h2": "Genehmigung und Netzanschluss in St. Veit an der Glan: Bauamt im Rathaus, Kärnten Netz am Zähler",
        "betreiber": "der Kärnten Netz GmbH",
        "paragraphs": [
            ("Für eine Photovoltaikanlage auf dem Dach brauchen Sie in St. Veit in aller Regel keine "
             "Baubewilligung. Bauliche Anlagen, die erneuerbare Energie erzeugen oder elektrische Energie "
             "speichern, zählt das Land Kärnten zu den mitteilungspflichtigen Vorhaben nach § 7 der Kärntner "
             "Bauordnung: Sie werden der Baubehörde vor Beginn der Ausführung schriftlich bekannt gegeben, ein "
             "Bewilligungsverfahren findet nicht statt, Kosten entstehen laut Land keine. Zuständig ist das Bauamt "
             "der Stadtgemeinde (Bau- und Feuerpolizei) im Rathaus am Hauptplatz 1. Die Anlage muss trotzdem zum "
             "Flächenwidmungs- und Bebauungsplan passen. Spielen bei Ihrem Haus Ortsbildpflege oder Denkmalschutz "
             "eine Rolle, fragen wir im Bauamt nach, bevor wir planen."),
            ("Stromnetzbetreiber in St. Veit an der Glan ist die Kärnten Netz GmbH. Den Anschlussantrag stellen wir "
             "als bevollmächtigter Anlagenplaner über das Kundenportal. Eine Netzberechnung ermittelt, wie viel "
             "Leistung an Ihrem Anschlusspunkt eingespeist werden darf; das Ergebnis steht im "
             "Netzzutrittsangebot, danach folgt der Netzzugangsvertrag. Nach der Montage meldet ein "
             "konzessionierter Elektriker die Fertigstellung im Portal. Erlaubt das Netz weniger Einspeisung als "
             "gewünscht, nennt Kärnten Netz drei Wege: einen anderen Anschlusspunkt, eine dynamische "
             "Leistungsregelung oder den Netzausbau. Meist lösen wir das mit Speicher und Regelung, weil dabei "
             "laut Kärnten Netz nur ein kleiner Teil der Jahresenergie verloren geht."),
            ("Gut zu wissen für Mittelkärnten: Kärnten Netz erneuert die 110-kV-Leitung zwischen den "
             "Umspannwerken St. Veit, Treibach, Wietersdorf und Brückl auf rund 38 km Länge und nennt dafür "
             "eine Investition von etwa 90 Millionen Euro. Begründet wird das Projekt mit der Integration "
             "erneuerbarer Energien und mit neuen Anwendungen wie Wärmepumpen und E-Mobilität. Das Vorhaben "
             "befindet sich im Verfahren zur Umweltverträglichkeitsprüfung. Für Ihre Anlage zählt bis dahin, was "
             "die Netzberechnung an Ihrem Hausanschluss ergibt."),
        ],
        "bullets": [
            "Mitteilung nach § 7 Kärntner Bauordnung an das Bauamt im Rathaus, vor Montagebeginn",
            "Anschlussantrag im Kundenportal von Kärnten Netz, Netzzutrittsangebot und Netzzugangsvertrag",
            "Fertigstellungsmeldung durch den konzessionierten Elektriker, danach Inbetriebnahme",
            a("batteriespeicher", "Speicher richtig auslegen, wenn die Einspeisung begrenzt ist"),
        ],
        "img": "gen_detail",
        "alt": ("Monteur verschraubt ein Photovoltaik-Modul auf der Aluminium-Unterkonstruktion eines Daches, "
                "Nahaufnahme (Symbolbild)"),
    },

    "waermepumpe": {
        "h2": "Wärmepumpe in St. Veit an der Glan: erst die Fernwärme prüfen, dann die Wärmepumpe planen",
        "paragraphs": [
            ("In St. Veit beginnt jede ehrliche Heizungsberatung mit der Fernwärme. Das Netz wurde laut Stadt "
             "Anfang der 1990er Jahre errichtet und wird mit Biomasse betrieben; der Klimaneutralitätsfahrplan "
             "nennt zusätzlich die Nutzung industrieller Abwärme. Es ist rund 50 km lang, etwa 800 Gebäude sind "
             "angeschlossen, und laut Stadt werden über 70 Prozent der Haushalte so versorgt. Der Betreiber, die "
             "Kelag Energie &amp; Wärme, will das Netz weiter verdichten und ausbauen. Liegt Ihr Haus an einer "
             "Leitung, ist der Anschluss oft die naheliegende Lösung, und das sagen wir Ihnen auch."),
            ("Die Zahlen zeigen aber auch die andere Seite: Etwa 800 angeschlossene Gebäude stehen 2.999 Gebäuden "
             "in der Stadtgemeinde gegenüber. Das legt nahe, dass vor allem Gebäude mit vielen Wohnungen am Netz "
             "hängen, während viele Ein- und Zweifamilienhäuser eine eigene Heizung haben. Die Stadt will bis "
             "2040 bei Wohn- und Dienstleistungsgebäuden ganz aus Kohle, Öl und Gas aussteigen. Für Häuser ohne "
             "Fernwärmeanschluss ist die Wärmepumpe dafür der direkte Weg: Sie macht aus 1 kWh Strom 4 bis 5 kWh "
             "Wärme, und einen Teil dieses Stroms liefert die eigene Photovoltaikanlage."),
            ("Eine Luft-Wasser-Wärmepumpe kostet im Einfamilienhaus rund 12.000 bis 22.000 Euro vor Förderung*, "
             "im Altbau mit Anpassungen 15.000 bis 28.000 Euro*. Weil in St. Veit mehr als die Hälfte der Gebäude "
             "vor 1981 gebaut wurde, prüfen wir bei jedem Termin zuerst die Heizflächen: Bis etwa 55 Grad "
             "Vorlauftemperatur arbeitet eine moderne Wärmepumpe effizient, oft genügt der Tausch einzelner "
             "Heizkörper. Die Montage dauert in der Regel 2 bis 4 Tage."),
        ],
        "bullets": [
            "Vorab klären: Liegt Ihr Haus im Fernwärmegebiet der Kelag Energie &amp; Wärme?",
            "Heizflächen-Check: Reichen Ihre Heizkörper bei 50 bis 55 Grad Vorlauf?",
            "Photovoltaik, Speicher und Wärmepumpe als ein System planen",
            a("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau: was vor dem Tausch zu prüfen ist"),
        ],
        "img": "waermepumpe",
        "alt": ("Außeneinheit einer Luft-Wasser-Wärmepumpe vor einer Holzfassade im Garten, Symbolbild für den "
                "Heizungstausch in St. Veit an der Glan"),
    },

    "foerderung_lokal": [
        ("Eine eigene Förderung der Stadtgemeinde St. Veit an der Glan für Photovoltaik, Stromspeicher oder "
         "Heizungstausch haben wir auf der Förderseite der Stadt nicht gefunden: Dort stehen derzeit "
         "Familienzuschuss, Kultur- und Sportsubvention, Wirtschaftsförderung und Wohnbeihilfe. Ob die Stadt "
         "darüber hinaus einen Zuschuss vergibt, fragen wir vor dem Angebot im Rathaus nach."),
        ("Beratung gibt es in St. Veit dafür direkt vor Ort: Die Klima- und Energie-Modellregion Sonnenland "
         "Mittelkärnten, zu der die Stadt gehört, bietet laut Klimaneutralitätsfahrplan Energiesprechtage zu "
         "Förderungen für Heizungstausch, Sanierung, Photovoltaik und Stromsparen an. Die Energieberatung des "
         "Landes über das Netzwerk Energieberatung Kärnten ist laut Fahrplan alle fünf Jahre kostenlos."),
    ],

    "referenzen": {
        "h2": "Referenzen in der Nähe von St. Veit an der Glan",
        "intro": ("Aus dem Bezirk St. Veit zeigen wir hier noch kein dokumentiertes Projekt. Die nächstgelegenen "
                  "Referenzen aus Kärnten stehen in Krumpendorf am Wörthersee, am Ossiachersee und in Villach, "
                  "jeweils mit Leistung, Speicher und Ergebnis."),
        "slugs": ["projekt-mehrparteienhaus-krumpendorf", "projekt-pv-am-ossiachersee",
                  "projekt-einfamilienhaus-villach"],
    },

    "umgebung": ["Althofen", "Friesach", "St. Georgen am Längsee", "Liebenfels", "Frauenstein", "Mölbling",
                 "Kappel am Krappfeld", "Brückl", "Eberstein", "Guttaring", "Klein St. Paul", "Straßburg"],

    "links": [
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau"),
        ("/energiegemeinschaft-kaernten/", "Energiegemeinschaft in Kärnten"),
        ("/pv-speicher-nachruesten/", "PV-Speicher nachrüsten"),
        ("/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/", "10 kWp mit Speicher und Montage"),
    ],

    "faq": [
        ("Was kostet eine Photovoltaikanlage in St. Veit an der Glan?",
         "Eine Komplettanlage mit rund 10 kWp und Speicher kostet typischerweise rund 15.000 bis 22.000 Euro vor "
         "Förderung, inklusive Montage, Mitteilung an das Bauamt und Netzanmeldung bei Kärnten Netz (Richtpreis, "
         "Stand Oktober 2026). Als Richtwert für Kärnten rechnen wir mit 1.000 bis 1.100 kWh Jahresertrag je kWp, "
         "bei 10 kWp also mit rund 10.000 bis 11.000 kWh. Den genauen Preis für Ihr Haus in St. Veit nennt das "
         "Fixangebot nach dem Termin vor Ort."),
        ("Brauche ich in St. Veit an der Glan eine Baubewilligung für Photovoltaik und Speicher?",
         "In aller Regel nicht. Anlagen, die erneuerbare Energie erzeugen oder Strom speichern, sind laut Land "
         "Kärnten nach Paragraf 7 der Kärntner Bauordnung mitteilungspflichtig: Das Vorhaben wird vor Beginn "
         "schriftlich der Baubehörde bekannt gegeben, ein Bewilligungsverfahren gibt es nicht, Kosten fallen dafür "
         "keine an. In St. Veit geht die Mitteilung an das Bauamt im Rathaus. Flächenwidmungs- und Bebauungsplan "
         "müssen eingehalten werden; die Mitteilung bereiten wir für Sie vor."),
        ("Wer ist der Stromnetzbetreiber in St. Veit an der Glan und wie läuft die Netzanmeldung?",
         "Netzbetreiber ist die Kärnten Netz GmbH. Den Anschlussantrag stellen wir über das Kundenportal. Eine "
         "Netzberechnung zeigt, wie viel Leistung an Ihrem Anschlusspunkt eingespeist werden darf; das Ergebnis "
         "steht im Netzzutrittsangebot, danach kommt der Netzzugangsvertrag. Nach der Montage meldet ein "
         "konzessionierter Elektriker die Fertigstellung. Ist die Einspeisung begrenzt, planen wir Speicher und "
         "Leistungsregelung so, dass möglichst viel Strom im Haus bleibt."),
        ("Lohnt sich eine Wärmepumpe in St. Veit an der Glan, obwohl es Fernwärme gibt?",
         "Das hängt von Ihrer Adresse ab. Laut Stadt werden über 70 Prozent der Haushalte mit Fernwärme versorgt, "
         "angeschlossen sind aber nur etwa 800 der rund 3.000 Gebäude. Liegt Ihr Haus an einer Leitung, ist der "
         "Anschluss oft naheliegend, und das sagen wir Ihnen offen. Ohne Anschlussmöglichkeit ist die Wärmepumpe "
         "meist die passende Lösung, vor allem zusammen mit Photovoltaik: Aus 1 kWh Strom werden 4 bis 5 kWh "
         "Wärme."),
        ("Funktioniert eine Wärmepumpe in einem älteren Haus in St. Veit an der Glan?",
         "In vielen Fällen ja. Rund 58 Prozent der Gebäude in der Stadtgemeinde wurden laut Statistik Austria vor "
         "1981 gebaut, deshalb prüfen wir zuerst die Heizflächen. Bis etwa 55 Grad Vorlauftemperatur arbeitet eine "
         "moderne Wärmepumpe effizient; oft reicht der Tausch einzelner Heizkörper. Im Altbau mit Anpassungen "
         "liegt der Richtpreis bei 15.000 bis 28.000 Euro vor Förderung. Sind zuerst Fenster oder Dämmung an der "
         "Reihe, sagen wir das."),
        ("Gibt es in St. Veit an der Glan eine Förderung der Stadt für Photovoltaik oder Heizungstausch?",
         "Auf der Förderseite der Stadtgemeinde ist derzeit kein eigenes Programm für Photovoltaik, Stromspeicher "
         "oder Heizungstausch angeführt. Wir fragen vor dem Angebot im Rathaus nach, ob es einen Zuschuss gibt. Es "
         "bleiben die Landespauschale Kärnten für Photovoltaik mit Speicher und der Investitionszuschuss des "
         "Bundes; bei der Wärmepumpe ist die Bundesförderung derzeit ausgeschöpft. Beratung zu Förderungen bieten "
         "die Energiesprechtage der Klima- und Energie-Modellregion Sonnenland Mittelkärnten."),
        ("In welchen Orten rund um St. Veit an der Glan berät und montiert EBZ Energie?",
         "Im ganzen Bezirk Sankt Veit an der Glan mit seinen 20 Gemeinden, zum Beispiel in Althofen, Friesach, "
         "St. Georgen am Längsee, Liebenfels, Frauenstein, Mölbling, Kappel am Krappfeld und Brückl. Gemeint ist "
         "St. Veit an der Glan in Kärnten mit der Postleitzahl 9300, nicht St. Veit im Pongau. Unser Firmensitz "
         "ist die Triglavstraße 15 in Villach; zur Erstberatung kommen wir zu Ihnen, die Montage übernehmen "
         "zertifizierte Fachkräfte."),
        ("Kann ich Sonnenstrom in St. Veit an der Glan mit Nachbarn teilen?",
         "Ja, über eine Energiegemeinschaft. Die Stadt St. Veit nennt die Förderung lokaler und regionaler "
         "Energiegemeinschaften als Ziel in ihrem Klimaneutralitätsfahrplan. Im Nahbereich sinken die Netzentgelte "
         "für den geteilten Strom um bis zu 57 Prozent (lokal) oder 28 Prozent (regional). Österreichweit ist das "
         "Teilen als Bürgerenergiegemeinschaft möglich, dann ohne diesen Rabatt. Wir planen Ihre Anlage so, dass "
         "Überschüsse sinnvoll geteilt werden können."),
    ],

    "quellen": [
        ("Stadtgemeinde St. Veit an der Glan: Sonne &amp; Energie (Photovoltaik im Stadtgebiet, Fernwärme)",
         "https://stveit.com/unser-st-veit/projekte-in-st-veit/sonne-energie"),
        ("Stadtgemeinde St. Veit an der Glan: Klimaneutralitätsfahrplan, Version 1.0 vom 31.10.2024 (PDF)",
         "https://stveit.com/fileadmin/sankt_veit/_Laufwerk_Stadt_SanktVeit/Sonstige_Dokumente/"
         "St._VeitGlan_Klimaneutralitaetsfahrplan__Vers._1.0_.pdf"),
        ("Stadtgemeinde St. Veit an der Glan: Klimapionier St. Veit (Modellregion, Leuchtturm-Programm)",
         "https://www.stveit.com/klimaschutz"),
        ("Stadtgemeinde St. Veit an der Glan: European Energy Award in Silber (Meldung vom 13.05.2026)",
         "https://stveit.com/unser-st-veit/neuigkeiten/news-detail/st-veit-an-der-glan-ist-energie-champion"),
        ("Stadtgemeinde St. Veit an der Glan: Bauamt (Bau- und Feuerpolizei, Ortsbildpflege)",
         "https://stveit.com/unser-rathaus/stadtverwaltung/bauamt"),
        ("Stadtgemeinde St. Veit an der Glan: Förderung, Beihilfe und Subventionen",
         "https://stveit.com/service/foerderung-beihilfe-subventionen"),
        ("Land Kärnten, Verfahrensportal EAP: Mitteilungspflichtige Bauvorhaben nach § 7 Kärntner Bauordnung",
         "https://eap.ktn.gv.at/Verfahren.aspx?id=331c5659-97a7-4994-8e00-cba24cf92d78&amp;lang=de&amp;p=az"),
        ("Kärnten Netz: PV-Anlage ans Netz anschließen (Ablauf und Einspeiseleistung)",
         "https://www.kaerntennetz.at/pv.htm"),
        ("Kärnten Netz: Ausbau des Stromnetzes Mittelkärnten (110-kV-Leitung St. Veit, Treibach, Brückl)",
         "https://kaerntennetz.at/mittelkaernten.htm"),
        ("Kelag: Unternehmensgeschichte (Eingliederung des Elektrizitätswerks St. Veit 1947)",
         "https://www.kelag.at/ueber-kelag/geschichte.htm"),
        ("Statistik Austria: Ein Blick auf die Gemeinde St. Veit an der Glan, Bevölkerung (PDF)",
         "https://www.statistik.at/blickgem/G0201/g20527.pdf"),
        ("Statistik Austria: Gebäude nach Nutzung und Wohnungszahl, Gebäude- und Wohnungszählung 2021 (PDF)",
         "https://www.statistik.at/blickgem/G0402/g20527.pdf"),
        ("Statistik Austria: Gebäude nach Bauperiode, Gebäude- und Wohnungszählung 2021 (PDF)",
         "https://www.statistik.at/blickgem/G0403/g20527.pdf"),
    ],

    "notizen": (
        "Faktenfragen an den Kunden: (1) Gibt es EBZ-Projekte im Bezirk St. Veit, die als Referenz freigegeben "
        "werden koennen? Derzeit steht auf der Seite, dass wir aus dem Bezirk noch kein dokumentiertes Projekt "
        "zeigen. (2) Stadtfoerderung: 2022 gab es laut Presseinfo der Stadt bis 1.500 Euro fuer den Ausbau "
        "fossiler Heizungen; die Presseinfo ist nicht mehr online, die Foerderseite der Stadt listet nichts. "
        "Im Rathaus (Umwelt-, Klima- und Energiekoordination) nachfragen, ob das Programm noch laeuft. "
        "(3) Plant EBZ die Waermepumpe selbst auch dann, wenn ein Fernwaermeanschluss moeglich waere? Die Seite "
        "empfiehlt in diesem Fall offen den Anschluss. (4) Kaerntner Baurecht: Text stuetzt sich auf das "
        "EAP-Portal des Landes (alle Anlagen zur Erzeugung erneuerbarer Energie und Stromspeicher sind "
        "mitteilungspflichtig). Villach und Wolfsberg schreiben 'in der Regel Mitteilungspflicht': konsistent. "
        "RIS war nicht abrufbar, Gesetzestext nicht gegengelesen. (5) Netzbetreiber Kaernten Netz ist ueber das "
        "Umspannwerk St. Veit und die Kelag-Geschichte belegt, nicht ueber eine Gemeindeliste des Netzgebiets: "
        "am ersten Zaehlpunkt gegenpruefen. (6) Nicht verwendet mangels Quelle: Sonnenstunden, Seehoehe, "
        "Gasnetz am Ort, Kelag-Waermepumpen-Praemie, Begriff 'Sonnenstadt' (steht nicht auf der Seite der Stadt)."
    ),
}
