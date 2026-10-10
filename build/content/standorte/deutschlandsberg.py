"""Ortsseite Deutschlandsberg (/photovoltaik-deutschlandsberg/), Steiermark.

Inhalt fuer die gemeinsame Vorlage build/pages/standorte.py. Briefing: build/seo/standort_deutschlandsberg.json.
Alle lokalen Angaben stammen aus Quellen, die am 10.10.2026 abgerufen wurden (Liste in ORT["quellen"]):

- Landesstatistik Steiermark, Gemeindeprofil 60344 und Bezirksprofil 603 (aktualisiert 08.09.2026):
  11.675 Einwohner (1.1.2026), 179,1 km2, Seehoehe Gemeindeamt 370 m, 4.506 Gebaeude, davon 3.908 Wohngebaeude,
  6.999 Wohnungen, 5.509 Privathaushalte (2024), Agrarstrukturerhebung 2020: 15.390 ha Forst von 19.077 ha;
  Bezirk: 60.962 Einwohner, 863,5 km2. 15 Gemeinden laut Steuerkraft-Tabelle der Landesstatistik.
- Stadtgemeinde Deutschlandsberg (deutschlandsberg.at): Ortsteile, Bauberatung im Rathaus (Hauptplatz 35, 2. Stock),
  Foerderseite ohne Programm fuer PV, Speicher oder Heizungstausch.
- Land Steiermark, Seite "Steiermaerkisches Baurecht" (Baugesetz idF LGBl. Nr. 20/2026, ab 28.02.2026) und Auszug
  aus den Erlaeuterungen zum Stmk. Deregulierungsgesetz (LGBl. Nr. 19/2026, ab 27.02.2026): PV auf Dach und
  Fassade unabhaengig von der Groesse meldepflichtig (Paragraf 21 Abs. 1 Z 2 lit. o Stmk. BauG), Bewilligung nur ueber
  3,50 m Anlagenhoehe (Paragraf 20 Z 2 lit. l); Batterieanlagen bis 20 kWh meldepflichtig, bis 100 kWh mit Nachweis;
  Waermepumpen meldepflichtig mit Datenblatt und Schallbestaetigung (Paragraf 21 Abs. 2 Z 2b, Abs. 3 Z 5).
- Energienetze Steiermark (e-netze.at): Ablauf Erzeugungsanlagen (Einspeiserportal, Netzanschlusskonzept 12 Monate),
  Freie Einspeisekapazitaeten: Umspannwerk Deutschlandsberg 29,0 MW gebucht, 0,0 MW verfuegbar (Stand 01.07.2026).
- EVU der Marktgemeinde Eibiswald (eibiswald.gv.at): eigener Netzbetreiber, 16 Trafostationen, rund 60 km Netz.
- Energie Steiermark Waerme GmbH, Brennstoffmix 2025: Fernwaermenetz Deutschlandsberg 56,8 % erneuerbar, 43,2 % fossil.
- PVGIS (EU-Kommission, JRC), Standort 46,816 N / 15,215 O: 1.181 kWh je kWp und Jahr (39 Grad Neigung, Sued,
  14 % Systemverluste, PVGIS-SARAH2 2005 bis 2020).
- Klima- und Energiefonds (orte-von-morgen.at): Pionierstadt Deutschlandsberg, Projektstart 2023.
- OeBB-Infrastruktur: Koralmbahn (130 km neue Strecke Graz bis Klagenfurt), keine Fahrzeiten uebernommen.

Bewusst weggelassen (keine amtliche Quelle abgerufen): Schilcherland, KEM-Zugehoerigkeit, Gasnetz, Ortsbildschutz,
Sonnenstunden, Details zum Fernwaerme-Ausbau (nur Regionalpresse), Lage des Bahnhofs Weststeiermark.
"""

from common import a

_EXT = 'rel="nofollow noopener" target="_blank"'

ORT = {
    "key": "pv_deutschlandsberg",
    "name": "Deutschlandsberg",
    "kurz": "Deutschlandsberg",
    "area_name": "Bezirk Deutschlandsberg",
    "land": "stmk",

    "title": "Photovoltaik Deutschlandsberg: PV & Wärmepumpe | EBZ",
    "description": ("Photovoltaik und Wärmepumpe in Deutschlandsberg: rund 1.180 kWh Ertrag je kWp, Meldung statt "
                    "Baubewilligung, Netzanschluss bei Energienetze Steiermark."),
    "h1": "Photovoltaik in Deutschlandsberg: PV-Anlage, Speicher und Wärmepumpe aus einer Planung",
    "lead": ("EBZ Energie ist ein Fachbetrieb aus Villach und plant Photovoltaik, Speicher und Wärmepumpe vor Ort in "
             "Deutschlandsberg und in der Weststeiermark. Sie bekommen einen Projektbericht mit 3D-Belegplan und "
             "Statikreport, ein Fixangebot und einen festen Ansprechpartner von der Planung bis zur Übergabe. "
             "Meldung beim Bauamt und Antrag bei Energienetze Steiermark bereiten wir für Sie vor."),
    "badges": [
        ("1.180 kWh", "je kWp und Jahr laut PVGIS*"),
        ("Meldung", "statt Baubewilligung für PV am Dach"),
        ("ab 147 €*", "im Monat, PV mit Speicher finanziert"),
    ],
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit Photovoltaikanlage auf dem Dach, Symbolbild (kein Foto aus Deutschlandsberg)",

    "intro": {
        "h2": "PV-Anlage Deutschlandsberg: guter Ertrag, knappes Netz",
        "paragraphs": [
            ("Deutschlandsberg ist die Bezirkshauptstadt der Weststeiermark an der Koralpe. Laut Landesstatistik "
             "Steiermark leben hier 11.675 Menschen (Stand 1.1.2026) in 5.509 Privathaushalten, verteilt auf "
             "179,1 km² und sieben Ortsteile. Die Statistik zählt 3.908 Wohngebäude mit 6.999 Wohnungen: Das spricht "
             "für viele Häuser mit eigenem Dach, und genau dort rechnet sich eine PV-Anlage am schnellsten."),
            ("Der Standort liefert ordentlich Strom. Das Rechenwerkzeug PVGIS der EU-Kommission weist für "
             "Deutschlandsberg (370 m Seehöhe) rund 1.180 kWh je kWp und Jahr aus, gerechnet für ein Süddach mit "
             "39 Grad Neigung und 14 Prozent Systemverlusten. Eine Anlage mit 10 kWp kommt damit auf rund "
             "11.800 kWh im Jahr (Richtwert*). Ost-West-Dächer liegen etwas darunter, verteilen den Strom dafür "
             "besser über den Tag."),
            ("Die Besonderheit vor Ort ist das Netz: Energienetze Steiermark weist für das Umspannwerk "
             "Deutschlandsberg derzeit 0,0 MW freie Einspeisekapazität aus (Stand 1. Juli 2026, unverbindliche "
             "Momentaufnahme). Wir legen Anlagen in Deutschlandsberg deshalb auf Eigenverbrauch aus: mit "
             + a("batteriespeicher", "Batteriespeicher") + ", " + a("waermepumpe", "Wärmepumpe") + " und "
             + a("ems", "Energiemanagement") + ". Überschüsse können Sie in einer "
             + a("eg_privat", "Energiegemeinschaft") + " teilen."),
        ],
    },

    "lokal": {
        "h2": "Photovoltaik Deutschlandsberg: Stadt, Netz und Behörde auf einen Blick",
        "intro": ("Diese Angaben haben wir für Deutschlandsberg aus amtlichen und offiziellen Quellen "
                  "zusammengetragen. Sie entscheiden darüber, wie Ihre Anlage geplant, gemeldet und angeschlossen wird."),
        "rows": [
            ("Stadt und Bezirk",
             "Stadtgemeinde Deutschlandsberg, Sitz der Bezirkshauptmannschaft. Der Bezirk Deutschlandsberg hat "
             "15 Gemeinden und 60.962 Einwohner (Stand 1.1.2026)."),
            ("Zahlen zur Stadt",
             "11.675 Einwohner, 179,1 km², Seehöhe 370 m (Gemeindeamt), 3.908 Wohngebäude, 5.509 Privathaushalte "
             "(Landesstatistik Steiermark)."),
            ("Ortsteile",
             "Bad Gams, Deutschlandsberg, Freiland, Kloster, Osterwitz, Trahütten und Wildbach."),
            ("Lage",
             "Weststeiermark, an der Koralpe. Die Koralmbahn (130 Kilometer neue Strecke zwischen Graz und "
             "Klagenfurt) hat die Weststeiermark laut ÖBB-Infrastruktur deutlich besser an Südkärnten angebunden."),
            ("Stromnetz",
             "Energienetze Steiermark GmbH, Umspannwerk Deutschlandsberg. Der Antrag läuft über das Einspeiserportal "
             "des Netzbetreibers. In Eibiswald betreibt das EVU der Marktgemeinde ein eigenes Stromnetz."),
            ("Freie Einspeisekapazität",
             "Umspannwerk Deutschlandsberg: 29,0 MW gebucht, 0,0 MW verfügbar (Energienetze Steiermark, Stand "
             "1. Juli 2026). Unverbindliche Momentaufnahme, jede Anfrage wird einzeln geprüft."),
            ("Baubehörde",
             "Bauamt der Stadtgemeinde im Rathaus, Hauptplatz 35, 2. Stock. Die Stadt bietet eine Bauberatung nach "
             "Terminvereinbarung an."),
            ("Genehmigung",
             "Photovoltaik auf Dach oder Fassade ist nach dem Steiermärkischen Baugesetz meldepflichtig, unabhängig "
             "von der Größe. Auch die Wärmepumpe ist meldepflichtig, mit Schallbestätigung."),
            ("Solarpotenzial",
             f'Das <a href="https://gis.stmk.gv.at/atlas2/Solartool.html" {_EXT}>SolarTool im Digitalen Atlas '
             "Steiermark</a> (GIS Steiermark) zeigt die Eignung Ihrer Dachfläche für Photovoltaik und Solarthermie "
             "und schickt den Bericht per E-Mail."),
            ("Fernwärme",
             "Die Energie Steiermark Wärme GmbH betreibt in Deutschlandsberg ein Fernwärmenetz. Brennstoffmix 2025: "
             "56,8 % erneuerbare Energie, 43,2 % fossile Energie."),
            ("Klimaprogramm",
             "Deutschlandsberg ist Pionierstadt der Mission „Klimaneutrale Stadt“ des Klima- und Energiefonds "
             "(Projektstart 2023) und erarbeitet einen Klimaneutralitätsfahrplan mit Roadmap bis 2040."),
        ],
    },

    "netz": {
        "h2": "Genehmigung und Netzanschluss in Deutschlandsberg: Meldung an die Stadt, Antrag beim Netzbetreiber",
        "betreiber": "der Energienetze Steiermark GmbH",
        "paragraphs": [
            ("In der Steiermark regelt das Steiermärkische Baugesetz, was eine Photovoltaikanlage braucht. Seit der "
             "Novelle durch das Steiermärkische Deregulierungsgesetz (LGBl. Nr. 19/2026) sind Anlagen, die auf Dach- "
             "oder Fassadenflächen angebracht oder in sie integriert werden, unabhängig von ihrer Größe nur noch "
             "meldepflichtig. Ein Bewilligungsverfahren entfällt. Bewilligungspflichtig bleiben Anlagen mit mehr als "
             "3,50 m Anlagenhöhe, für Freiflächen gelten eigene Regeln. Die Meldung geht an die Baubehörde: in "
             "Deutschlandsberg an das Bauamt im Rathaus am Hauptplatz 35."),
            ("Für den Speicher gilt dasselbe Prinzip: Stationäre Batterieanlagen bis 20 kWh sind meldepflichtig, "
             "bis 100 kWh dann, wenn der Hersteller nachweist, dass das thermische Durchgehen einer Zelle nicht zum "
             "Brand der Anlage führt. Diese Nachweise legen wir der Meldung bei."),
            ("Beim Netzanschluss ist die Reihenfolge fix. Wir registrieren Ihre Anlage im Einspeiserportal von "
             "Energienetze Steiermark und beantragen den Einspeisezählpunkt. Danach erstellt der Netzbetreiber das "
             "Netzanschlusskonzept. Es gilt 12 Monate und lässt sich einmal um 12 Monate verlängern; ohne gültiges "
             "Konzept gibt es keinen Zugang zum Verteilnetz. Nach der Montage folgen die Fertigmeldung durch ein "
             "konzessioniertes Elektrounternehmen und die Anmeldung beim Stromabnehmer, erst dann geht die Anlage "
             "in Betrieb."),
            ("Wie viel Sie einspeisen dürfen, steht erst im Netzanschlusskonzept. Am Umspannwerk Deutschlandsberg "
             "sind laut Netzbetreiber 29,0 MW gebucht und 0,0 MW frei, in der Liste zeigen 42 von 53 steirischen "
             "Umspannwerken denselben Wert. Für PV-Anlagen von 3,68 bis 250 kW verlangt Energienetze Steiermark "
             "außerdem seit Dezember 2024 eine Wirkleistungsvorgabe: Im Notzustand des Netzes kann die Einspeisung "
             "aus der Ferne reduziert werden. Unsere Antwort darauf ist eine Planung, die möglichst viel Strom im "
             "Haus hält. Mehr dazu auf der Seite " + a("photovoltaik", "Photovoltaik") + "."),
        ],
        "bullets": [
            "PV auf Dach oder Fassade: Meldung nach § 21 Stmk. BauG, keine Baubewilligung",
            "Netzanschlusskonzept von Energienetze Steiermark: 12 Monate gültig, einmal verlängerbar",
            "Umspannwerk Deutschlandsberg: 0,0 MW freie Einspeisekapazität (Stand 1. Juli 2026)",
            "SolarTool im GIS Steiermark zeigt das Potenzial Ihrer Dachfläche",
        ],
        "img": "gen_detail",
        "alt": "Montagedetail einer Photovoltaikanlage: Modulklemmen und Unterkonstruktion auf einem Dach, Symbolbild",
    },

    "waermepumpe": {
        "h2": "Heizungstausch Deutschlandsberg: Fernwärme prüfen, Wärmepumpe richtig planen",
        "paragraphs": [
            ("Vor dem Heizungstausch steht in Deutschlandsberg eine einfache Frage: Liegt vor dem Haus eine "
             "Fernwärmeleitung? Die Energie Steiermark Wärme GmbH betreibt in der Stadt ein Fernwärmenetz, das 2025 "
             "zu 56,8 Prozent mit erneuerbarer und zu 43,2 Prozent mit fossiler Energie gespeist wurde. Wo ein "
             "Anschluss möglich ist, vergleichen wir ihn offen mit der Wärmepumpe. Wo keine Leitung liegt, etwa in "
             "vielen Lagen der Ortsteile und in den Nachbargemeinden, ist die Wärmepumpe meist der naheliegende "
             "Ersatz für Öl- oder Gaskessel."),
            ("Baurechtlich ist die Wärmepumpe seit 2026 einfacher geworden. Die ortsfeste Aufstellung ist in der "
             "Steiermark unabhängig von der Leistung nur noch meldepflichtig. Der Meldung an das Bauamt müssen das "
             "technische Datenblatt und die Bestätigung eines befugten Sachverständigen beiliegen, dass der "
             "zulässige Schallpegel (Planungsbasispegel) an der relevanten Nachbargrundgrenze eingehalten wird. "
             "Deshalb legen wir den Aufstellort der Außeneinheit schon bei der Beratung fest und nicht erst am "
             "Montagetag."),
            ("Mit einer Photovoltaikanlage passt die Wärmepumpe in Deutschlandsberg doppelt gut: Sie senkt die "
             "Heizkosten und nimmt Strom ab, den das Netz am Umspannwerk derzeit kaum zusätzlich aufnehmen kann. "
             "Ein Energiemanagement lässt die Wärmepumpe bevorzugt laufen, wenn das Dach liefert, und lädt den "
             "Warmwasserspeicher als Wärmepuffer. Ob Ihr Haus dafür zuerst eine Sanierung braucht, sagen wir "
             "Ihnen nach dem Blick in den Heizraum."),
        ],
        "bullets": [
            "Fernwärme in der Stadt: Anschluss vor dem Angebot prüfen",
            "Meldung an das Bauamt mit Datenblatt und Schallbestätigung",
            "Wärmepumpe als Abnehmer für den eigenen PV-Strom",
        ],
        "img": "waermepumpe",
        "alt": "Außeneinheit einer Luft-Wasser-Wärmepumpe neben einem Wohnhaus, Symbolbild für den Heizungstausch",
    },

    "foerderung_lokal": [
        ("Die Stadtgemeinde Deutschlandsberg weist auf ihrer Förderseite (Stand Oktober 2026) kein eigenes Programm "
         "für Photovoltaik, Stromspeicher oder Heizungstausch aus. Gelistet ist dort unter anderem ein "
         "Heizkostenzuschuss für Haushalte, der keine Investition fördert. Für Frauental, Stainz, Eibiswald und die "
         "anderen Gemeinden im Bezirk fragen wir vor dem Angebot direkt im Gemeindeamt nach, weil Gemeindezuschüsse "
         "nicht zentral veröffentlicht werden."),
    ],

    "referenzen": {
        "h2": "Referenzen in der Steiermark: zwei Projekte in Graz",
        "intro": ("Aus dem Bezirk Deutschlandsberg zeigen wir hier noch kein dokumentiertes Projekt. Die "
                  "nächstgelegenen Referenzen mit Zahlen liegen in Graz, das dritte Beispiel ist ein Einfamilienhaus "
                  "am Firmensitz in Villach."),
        "slugs": ["projekt-flachdach-in-graz", "projekt-stadthaus-in-graz", "projekt-einfamilienhaus-villach"],
    },

    "umgebung": [
        "Frauental an der Laßnitz", "Groß Sankt Florian", "Stainz", "St. Stefan ob Stainz", "Bad Schwanberg",
        "Wies", "Eibiswald", "Pölfing-Brunn", "St. Martin im Sulmtal", "St. Peter im Sulmtal", "Wettmannstätten",
        "Lannach",
    ],

    "links": [
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau"),
        ("/landesfoerderungen-fuer-die-waermepumpe/", "Landesförderungen für die Wärmepumpe"),
        ("/energiegemeinschaft-steiermark/", "Energiegemeinschaft in der Steiermark"),
        ("/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/", "10 kWp Komplettanlage mit Speicher"),
    ],

    "faq": [
        ("Photovoltaik Deutschlandsberg: Was kostet eine Anlage mit Speicher?",
         "Eine Komplettanlage mit rund 10 kWp und Speicher kostet bei EBZ Energie rund 15.000 bis 22.000 Euro vor "
         "Förderung, inklusive Montage, Meldung beim Bauamt und Netzanmeldung bei Energienetze Steiermark "
         "(Richtpreis, Stand Oktober 2026). Der genaue Preis hängt in Deutschlandsberg vor allem von Dachform, "
         "Zählerschrank und Speichergröße ab. Sie erhalten nach dem Termin vor Ort ein Fixangebot. Auf Wunsch "
         "finanzieren Sie die Anlage, sie gehört Ihnen dann trotzdem ab dem ersten Tag."),
        ("Wie viel Strom erzeugt eine Photovoltaikanlage in Deutschlandsberg?",
         "Das Rechenwerkzeug PVGIS der EU-Kommission weist für Deutschlandsberg rund 1.180 kWh je kWp und Jahr aus, "
         "gerechnet für ein Süddach mit 39 Grad Neigung und 14 Prozent Systemverlusten. Eine Anlage mit 10 kWp "
         "erzeugt damit rund 11.800 kWh im Jahr. Das ist ein Richtwert und kein zugesagter Ertrag: Ausrichtung, "
         "Neigung und Verschattung durch Bäume oder Nachbargebäude verändern das Ergebnis. Eine erste Einschätzung "
         "für Ihr Dach liefert das SolarTool im GIS Steiermark."),
        ("Brauche ich in Deutschlandsberg eine Baubewilligung für die PV-Anlage?",
         "In der Regel nicht. Seit der Novelle des Steiermärkischen Baugesetzes (LGBl. Nr. 19/2026) sind "
         "Photovoltaikanlagen auf Dach- oder Fassadenflächen unabhängig von ihrer Größe nur noch meldepflichtig. "
         "Die Meldung geht an das Bauamt der Stadtgemeinde im Rathaus am Hauptplatz 35. Eine Bewilligung brauchen "
         "weiterhin Anlagen mit mehr als 3,50 m Anlagenhöhe, für Freiflächen gelten eigene Regeln. Wir bereiten "
         "die Meldung samt Unterlagen für Sie vor."),
        ("Wer ist der Netzbetreiber in Deutschlandsberg und wie läuft der Netzanschluss?",
         "Deutschlandsberg hängt am Umspannwerk Deutschlandsberg der Energienetze Steiermark GmbH. Die Anlage wird im "
         "Einspeiserportal des Netzbetreibers registriert, danach erstellt er das Netzanschlusskonzept. Es gilt "
         "12 Monate und kann einmal um 12 Monate verlängert werden. Nach Montage und Fertigmeldung durch ein "
         "konzessioniertes Elektrounternehmen geht die Anlage in Betrieb. Im Bezirk gibt es auch lokale Netze: In "
         "Eibiswald ist das EVU der Marktgemeinde zuständig. Wir klären den Netzbetreiber vor dem Angebot."),
        ("Was bedeutet die fehlende freie Einspeisekapazität am Umspannwerk Deutschlandsberg?",
         "Energienetze Steiermark weist für das Umspannwerk Deutschlandsberg 29,0 MW gebuchte und 0,0 MW freie "
         "Einspeisekapazität aus (Stand 1. Juli 2026). Die Angabe ist eine unverbindliche Momentaufnahme, jede "
         "Anfrage wird einzeln geprüft. Wie viel Ihre Anlage einspeisen darf, steht erst im Netzanschlusskonzept. "
         "Wir planen deshalb mit hohem Eigenverbrauch: Speicher, Wärmepumpe, Wallbox und Energiemanagement halten "
         "den Strom im Haus, damit sich die Anlage auch bei begrenzter Einspeisung rechnet."),
        ("Lohnt sich eine Wärmepumpe in Deutschlandsberg, wenn es Fernwärme gibt?",
         "Das hängt von der Adresse ab. Die Energie Steiermark Wärme GmbH betreibt in Deutschlandsberg ein "
         "Fernwärmenetz, das 2025 zu 56,8 Prozent aus erneuerbarer Energie gespeist wurde. Liegt eine Leitung vor "
         "dem Haus, vergleichen wir Anschluss und Wärmepumpe mit Zahlen. Ohne Fernwärme ist die Wärmepumpe meist "
         "der sinnvolle Ersatz für Öl- oder Gaskessel, besonders zusammen mit Photovoltaik, weil sie den eigenen "
         "Strom direkt im Haus verbraucht."),
        ("Muss ich eine Wärmepumpe in Deutschlandsberg bei der Gemeinde melden?",
         "Ja. Die ortsfeste Aufstellung einer Wärmepumpe ist in der Steiermark seit 2026 unabhängig von der Leistung "
         "meldepflichtig, eine Baubewilligung ist nicht mehr nötig. Der Meldung an das Bauamt der Stadtgemeinde "
         "Deutschlandsberg liegen das technische Datenblatt und die Bestätigung eines befugten Sachverständigen "
         "bei, dass der zulässige Schallpegel an der relevanten Nachbargrundgrenze eingehalten wird. Wir planen den "
         "Aufstellort der Außeneinheit so, dass diese Bestätigung möglich ist."),
        ("Gibt es eine Förderung der Stadt Deutschlandsberg für Photovoltaik oder Wärmepumpe?",
         "Die Stadtgemeinde Deutschlandsberg weist auf ihrer Förderseite (Stand Oktober 2026) kein eigenes Programm "
         "für Photovoltaik, Stromspeicher oder Heizungstausch aus. Welche Programme von Bund und Land Steiermark "
         "gerade beantragbar sind, zeigt unser Förderrechner; für neue Wärmepumpen nimmt derzeit weder der Bund "
         "noch das Land Anträge an. Für Kundinnen und Kunden in anderen Gemeinden des Bezirks, etwa Frauental, "
         "Stainz oder Wies, fragen wir vor dem Angebot im Gemeindeamt nach und bereiten die Anträge vor."),
    ],

    "quellen": [
        ("Landesstatistik Steiermark: Gemeindeprofil Deutschlandsberg (Einwohner, Fläche, Seehöhe, Gebäude)",
         "https://www.landesentwicklung.steiermark.at/cms/dokumente/12256480_141979478/965eb940/60344.pdf"),
        ("Landesstatistik Steiermark: Bezirksprofil Deutschlandsberg",
         "https://www.landesentwicklung.steiermark.at/cms/dokumente/12256480_141979478/1d0cea17/603.pdf"),
        ("Stadtgemeinde Deutschlandsberg: Ortsteile und Bürgerservice",
         "https://www.deutschlandsberg.at/"),
        ("Stadtgemeinde Deutschlandsberg: Bauberatung im Rathaus",
         "https://www.deutschlandsberg.at/system/web/zusatzseite.aspx?detailonr=225309977&amp;menuonr=225309978"),
        ("Stadtgemeinde Deutschlandsberg: Förderungen",
         "https://www.deutschlandsberg.at/system/web/foerderung.aspx?menuonr=225283910"),
        ("Land Steiermark: Steiermärkisches Baurecht (Baugesetz in der Fassung LGBl. Nr. 20/2026)",
         "https://www.technik.steiermark.at/cms/beitrag/11549819/58813874/"),
        ("Land Steiermark: Erläuterungen zum Stmk. Deregulierungsgesetz, LGBl. Nr. 19/2026 (Baugesetz: Photovoltaik, "
         "Batterieanlagen, Wärmepumpen)",
         "https://www.technik.steiermark.at/cms/dokumente/11549819_58813874/8510f5cf/"
         "Erl%C3%A4uterungen%20zum%20Stmk%20Deregulierungsgesetz%20LGBL_19_2026.pdf"),
        ("Energienetze Steiermark: Erzeugungsanlagen (Einspeiserportal, Netzanschlusskonzept)",
         "https://www.e-netze.at/Strom/Erzeugungsanlagen/Default.aspx"),
        ("Energienetze Steiermark: Freie Einspeisekapazitäten je Umspannwerk",
         "https://www.e-netze.at/Service/FEK/Default.aspx"),
        ("Marktgemeinde Eibiswald: EVU Eibiswald (Netzbetreiber und Stromlieferant)",
         "https://www.eibiswald.gv.at/wirtschaftumweltwohnen/evu-eibiswald"),
        ("Land Steiermark: Solarpotenzial Steiermark mit SolarTool im Digitalen Atlas",
         "https://www.landesentwicklung.steiermark.at/cms/beitrag/12910759/145230171"),
        ("Europäische Kommission, Joint Research Centre: PVGIS (Ertrag je kWp am Standort)",
         "https://re.jrc.ec.europa.eu/pvg_tools/de/"),
        ("Energie Steiermark Wärme GmbH: Brennstoffmix der Fernwärmenetze 2025",
         "https://www.e-steiermark.com/fileadmin/user_upload/downloads/Uebersicht_Brennstoffmix_Regionen_2025.pdf"),
        ("Klima- und Energiefonds: Pionierstadt Deutschlandsberg",
         "https://orte-von-morgen.at/ort/pionierstadt-deutschlandsberg/?place-id=366"),
        ("ÖBB-Infrastruktur: Koralmbahn",
         "https://infrastruktur.oebb.at/de/projekte-fuer-oesterreich/bahnstrecken/suedstrecke-wien-villach/koralmbahn"),
    ],

    "notizen": (
        "Faktenfragen für den Kunden: (1) Gibt es ein EBZ-Projekt im Bezirk Deutschlandsberg, das als Referenz "
        "freigegeben werden kann? (2) Netzbetreiber je Ortsteil: Energienetze Steiermark ist über das Umspannwerk "
        "Deutschlandsberg belegt, eine amtliche Gemeindeliste des Netzgebiets war nicht abrufbar (interaktive Karte). "
        "(3) Baurecht: Quelle sind die Erläuterungen des Landes zum Deregulierungsgesetz LGBl. 19/2026; der "
        "konsolidierte Paragraf 21 im RIS war am 10.10.2026 technisch nicht abrufbar, Wortlaut vor Livegang "
        "gegenlesen. (4) Wärmepumpen-Förderung: Land Steiermark nimmt laut build/seo/_fakten_2026-10.md derzeit "
        "keine Anträge an (deckt sich mit dem Hinweis auf der Fernwärme-Seite der Energie Steiermark); die FAQ "
        "zur Stadtförderung sagt das ausdrücklich und muss angepasst werden, sobald sich die Lage ändert. "
        "(5) Fernwärme-Ausbau (neues Biomasse-Heizwerk, Regionalpresse Juni 2026) nicht übernommen, weil keine "
        "offizielle Quelle abrufbar war. (6) Schilcherland, KEM, Gasnetz, Ortsbildschutz nicht belegt, daher "
        "weggelassen."
    ),
}
