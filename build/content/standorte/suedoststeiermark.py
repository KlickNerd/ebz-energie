"""Ortsseite Suedoststeiermark (/photovoltaik-suedoststeiermark/): Photovoltaik (Primaer) und Waermepumpe (Sekundaer).

Bezirksseite (kein Stadtportraet): Feldbach, Fehring, Bad Radkersburg, Mureck und Umland.
Briefing: build/seo/standort_suedoststeiermark.json / .md (DataForSEO, Oesterreich/Deutsch, 10.10.2026).
EBZ sitzt in Villach: kein Standort, keine Referenz im Bezirk behauptet.

LOKALE FAKTEN, alle am 10.10.2026 selbst abgerufen (Liste in ORT["quellen"]):
- Landesstatistik Steiermark, Bezirksdaten 623 (aktualisiert 08.09.2026): 983,1 km2, 83.333 Einwohner am 1.1.2026,
  85 Einwohner je km2; Gebaeude- und Wohnungszaehlung 2024: 32.916 Gebaeude, davon 29.250 Wohngebaeude, 41.756
  Wohnungen (rechnerisch 1,43 je Wohngebaeude); Agrarstrukturerhebung 2020: 4.708 land- und forstwirtschaftliche
  Betriebe (1.295 Haupterwerb, 3.200 Nebenerwerb), 292.832 Schweine, 2.524.802 Stueck Gefluegel.
- BH Suedoststeiermark, Gemeindeliste: 25 Gemeinden (4 Stadtgemeinden Feldbach, Fehring, Bad Radkersburg, Mureck;
  13 Marktgemeinden; 8 Gemeinden). Amtliche Namen fuer "umgebung" von dort.
- Stromnetz: Tarifkalkulator der E-Control (Abfrage Netzbetreiber je Postleitzahl, Strom): Energienetze Steiermark
  GmbH in allen abgefragten PLZ; zusaetzlich P.K. Energieversorgungs-GmbH (8330 Feldbach, 8332 Edelsbach, 8341
  Paldau, 8324 und 8323 Kirchberg an der Raab, 8082 Kirchbach, 8083 St. Stefan im Rosental, 8092 Mettersdorf),
  Bad Gleichenberger Energie GmbH (8344, 8343, 8353), "Stadtgemeinde Mureck, Inhaberin der nicht prot. Fa. EVU der
  Stadtgemeinde Mureck" (8480); an den Raendern Feistritzwerke-STEWEAG GmbH (8323, 8081) und Netz Burgenland GmbH
  (8350). Die PLZ-Abfrage sagt nicht, welche Strassen in welchem Netz liegen: deshalb ueberall "laut E-Control,
  je Adresse zu klaeren". ACHTUNG: Die Stadt Feldbach nannte 2016 das "regionale EVU Lugitsch" als zweiten
  Netzbetreiber im Raum Feldbach (Gemeindezeitung Juni 2016), die E-Control fuehrt fuer 8330 heute stattdessen die
  P.K. Energieversorgungs-GmbH. Ob das Lugitsch-Netz uebergegangen ist, war nicht zu belegen: Lugitsch wird nicht
  genannt, Faktenfrage an den Kunden.
- EVU der Stadtgemeinde Mureck (evu-mureck.at/stromnetz): "rund 5 km2 Flaeche mit einer 100%igen Erdverkabelung",
  "ueber 1.200 Kunden", eigene Formulare (Datenblatt Erzeugungsanlagen, Ausfuehrungs- bzw. Fertigstellungsmeldung PV).
- Bad Gleichenberger Energie GmbH (bg-energie.at): eigenes Stromnetz, Sitz Bairisch Koelldorf 12, 8344 Bad Gleichenberg.
- Energienetze Steiermark, Erzeugungsanlagen: Einspeiserportal, Einspeisezaehlpunkt, Netzanschlusskonzept,
  Installationsdokument durch konzessioniertes Elektrounternehmen. Freie Einspeisekapazitaeten je Umspannwerk,
  Stand 01.07.2026: Feldbach 16,7 MW gebucht / 0,0 MW verfuegbar, Halbenrain 20,2 / 0,0 ("unverbindliche
  Information", "Momentaufnahme", Einzelfallbetrachtung). Hohenbrugg (35,2 / 0,0), Merkendorf (11,3 / 0,0) und
  Gosdorf (29,9 / 0,0) liegen vermutlich ebenfalls im Bezirk, die Zuordnung der Umspannwerke zu Gemeinden ist aber
  nicht amtlich belegt: nur Feldbach und Halbenrain genannt.
- Gasnetz: Tarifkalkulator der E-Control (Gas): Energienetze Steiermark fuer 8330, 8322, 8324, 8341, 8343, 8344,
  8350, 8490, 8493; kein Gasnetzbetreiber fuer 8342 Gnas, 8345 Straden, 8082 Kirchbach, 8083 St. Stefan i. R.,
  8333 Riegersburg, 8480 Mureck, 8354 St. Anna am Aigen, 8353 Kapfenstein u. a.
- Baurecht: Stmk. Baugesetz idF LGBl. 20/2026 (Ausgabe Land Steiermark, April 2026) und Erlaeuterungen zum Stmk.
  Deregulierungsgesetz LGBl. 19/2026: § 21 Abs. 1 Z 2 lit. o (PV auf Dach/Fassade meldepflichtig ohne
  Groessengrenze, Hoehe bis 3,50 m), § 21 Abs. 2 Z 2a (Batterie bis 20 kWh, bis 100 kWh mit Nachweis "thermal
  runaway"), Z 2b und Abs. 3 Z 5 (Waermepumpe: Datenblatt + Bestaetigung Sachverstaendiger zum Planungsbasispegel),
  Abs. 3 (schriftliche Mitteilung an die Gemeinde vor Ausfuehrung: Grundstuecknummer, Lage, kurze Beschreibung).
  Behoerde: Standortgemeinde/Buergermeister; Hinweis Einspeisebegrenzung durch den Netzbetreiber
  (Verfahrenshandbuch PV/Solarthermie, Abt. 13, Stand August 2025). RIS war nicht abrufbar (Bot-Sperre).
- Steirisches Vulkanland, Energievision 2035: 100 % Waerme, Treibstoff und Elektrizitaet aus der Region; vier KEM.
- LEA GmbH (Lokale Energieagentur, Muehldorf 165, 8330 Feldbach), KEM-Seiten: Wirtschaftsregion mittleres Raabtal
  (Feldbach, Paldau, Kirchberg an der Raab, Eichkoegl; Stand Oktober 2024: 32 PV-Anlagen auf oeffentlichen Gebaeuden,
  1,6 MWp, rd. 1.700.000 kWh/Jahr = rechnerisch 1.062 kWh je kWp), Netzwerk Suedost (Fehring, Kapfenstein, Unterlamm,
  Riegersburg, St. Anna am Aigen), Wein- und Thermenregion Suedoststeiermark (Bad Gleichenberg, Straden, Bad
  Radkersburg; Schwerpunkt u. a. "Ausbau Nahwaermeversorgungen"), Gnas - St. Peter - Deutsch Goritz (u. a.
  "Biomassenahwaerme").
- Stadtgemeinde Feldbach, Umweltfoerderungen: 200 Euro fuer Biomasseheizungen, Fernwaermeanschluesse, Solaranlagen
  (GR 2.10.2015); 100 Euro fuer Fotovoltaikanlagen und Stromspeicheranlagen (GR 16.11.2023). Die dort verlinkten
  Antragsformulare lieferten am 10.10.2026 HTTP 404: deshalb mit Vorbehalt formuliert. Seite "Beihilfen, Foerderungen":
  Foerderansuchen fuer Bund und Land ueber LEA.
- Land Steiermark, Foerderung von Waermepumpen: derzeit keine Antragstellung (kommt zentral aus der Vorlage).

BEWUSST WEGGELASSEN (keine selbst abgerufene offizielle Quelle): Sonnenstunden und Klimawerte, Altstadt-/Ortsbild-
Richtlinie Bad Radkersburg fuer PV (PDF der Stadt war nicht mehr abrufbar), Gemeindefoerderungen ausser Feldbach
(Bad Radkersburg nannte 2023/2024 300 Euro, aktueller Stand nicht pruefbar), Fernwaerme-Ausbaustand in Feldbach,
Thermalwasser/Geothermie, Netzbetreiber "Lugitsch", Entfernungen und Fahrzeiten, Fristen jeder Art.
"""

from common import a

ORT = {
    "key": "pv_suedoststeiermark",
    "name": "Südoststeiermark",
    "kurz": "Südoststeiermark",
    "ort_in": "in der Südoststeiermark",
    "ort_nach": "in die Südoststeiermark",
    "area_name": "Bezirk Südoststeiermark",
    "land": "stmk",
    "title": "Photovoltaik Südoststeiermark, Feldbach + Wärmepumpe | EBZ",
    "description": ("Photovoltaik und Wärmepumpe in der Südoststeiermark: Feldbach, Fehring, Bad Radkersburg, Mureck. "
                    "4 Stromnetze, Meldung an die Gemeinde, Fachbetrieb aus Villach."),
    "eyebrow": "Photovoltaik und Wärmepumpe im Bezirk Südoststeiermark",
    "h1": "Photovoltaik und Wärmepumpe in der Südoststeiermark: von Feldbach bis Bad Radkersburg",
    "lead": ("EBZ Energie ist ein Fachbetrieb aus Villach und plant Photovoltaik, Speicher und Wärmepumpen vor Ort in "
             "der Südoststeiermark: in Feldbach, Fehring, Bad Radkersburg, Mureck und den Gemeinden dazwischen. Im "
             "Bezirk arbeiten neben dem Landesnetz drei lokale Stromnetzbetreiber, und für die Umspannwerke Feldbach und Halbenrain ist derzeit "
             "keine freie Einspeisekapazität ausgewiesen. Wir klären zuerst, welches Netz für Ihre Adresse gilt, und "
             "legen die Anlage auf Eigenverbrauch aus."),
    "badges": [
        ("25 Gemeinden", "von Feldbach über Fehring bis Bad Radkersburg und Mureck"),
        ("4 Stromnetze", "wir klären, welcher Netzbetreiber für Ihre Adresse gilt"),
        ("Meldepflichtig", "PV am Dach und Wärmepumpe, kein Bauverfahren"),
    ],
    "hero_img": "/assets/img/ref-landwirtschaft-bgld-1.jpg",
    "hero_alt": ("Photovoltaikanlage in zwei Modulreihen auf dem Bitumenschindel-Dach eines landwirtschaftlichen "
                 "Betriebs im Burgenland, Referenzprojekt von EBZ Energie (kein Foto aus der Südoststeiermark)"),

    "intro": {
        "h2": "Warum Photovoltaik und Wärmepumpe in der Südoststeiermark zusammengehören",
        "paragraphs": [
            ("Der Bezirk Südoststeiermark reicht vom Raabtal bei Feldbach bis an die Mur bei Mureck und Bad "
             "Radkersburg. Laut Landesstatistik Steiermark leben hier 83.333 Menschen (Stand 1. Jänner 2026) in "
             "25 Gemeinden auf 983 Quadratkilometern, das sind 85 Einwohner je Quadratkilometer. Auf 29.250 "
             "Wohngebäude kommen 41.756 Wohnungen (Gebäude- und Wohnungszählung 2024), rechnerisch also rund "
             "1,4 Wohnungen je Haus. Das Ein- und Zweifamilienhaus mit eigenem Dach, eigenem Zähler und eigener "
             "Heizung ist hier der Normalfall, und genau dafür sind Photovoltaik mit Speicher und Wärmepumpe gemacht."),
            ("Dazu kommt die Landwirtschaft. Die Agrarstrukturerhebung 2020 zählt im Bezirk 4.708 land- und "
             "forstwirtschaftliche Betriebe, 3.200 davon im Nebenerwerb, mit rund 293.000 Schweinen und 2,5 Millionen "
             "Stück Geflügel. Lüftung, Fütterung und Kühlung im Stall brauchen Strom zu jeder Tageszeit, und die "
             "Wirtschaftsgebäude bieten oft große Dachflächen. Für Höfe planen wir Photovoltaik mit Speicher und auf "
             "Wunsch mit " + a("/notstrom/", "Notstrom") + ", für Betriebe "
             + a("pv_gewerbe", "Photovoltaik für Gewerbedächer") + "."),
            ("Die Region hat sich das Ziel selbst gesetzt: Nach der Energievision des Steirischen Vulkanlandes sollen "
             "spätestens 2035 Wärme, Treibstoff und Strom zu 100 Prozent in der Region erzeugt werden. Vier Klima- und "
             "Energie-Modellregionen arbeiten daran, gemanagt von der Lokalen Energieagentur (LEA) in Feldbach. Allein "
             "in der Modellregion Wirtschaftsregion mittleres Raabtal (Feldbach, Paldau, Kirchberg an der Raab, "
             "Eichkögl) liefen mit Stand Oktober 2024 schon 32 PV-Anlagen auf öffentlichen Gebäuden mit zusammen "
             "1,6 MWp und rund 1,7 Millionen kWh Sonnenstrom im Jahr. Das sind rechnerisch rund 1.060 kWh je "
             "installiertem kWp; Ihr Dach kann je nach Ausrichtung und Verschattung darüber oder darunter liegen."),
        ],
    },

    "lokal": {
        "h2": "Die Südoststeiermark auf einen Blick: Bezirk, Stromnetze, Behörde, Solarkataster",
        "intro": ("Alle Angaben stammen aus amtlichen und offiziellen Quellen, abgerufen im Oktober 2026. Die Links "
                  "stehen im Quellenblock weiter unten."),
        "rows": [
            ("Bezirk",
             "Südoststeiermark, Bezirkshauptmannschaft in Feldbach. 25 Gemeinden: 4 Stadtgemeinden (Feldbach, Fehring, "
             "Bad Radkersburg, Mureck), 13 Marktgemeinden und 8 Gemeinden. 983 km², 83.333 Einwohner (1. Jänner 2026)."),
            ("Gebäudebestand",
             "29.250 Wohngebäude mit 41.756 Wohnungen (2024), rechnerisch rund 1,4 Wohnungen je Wohngebäude. "
             "4.708 land- und forstwirtschaftliche Betriebe (2020)."),
            ("Stromnetzbetreiber",
             "Im Großteil des Bezirks die Energienetze Steiermark GmbH. Laut Tarifkalkulator der E-Control daneben die "
             "P.K. Energieversorgungs-GmbH (Postleitzahlen von Feldbach, Edelsbach, Paldau, Kirchberg an der Raab, "
             "Kirchbach, Sankt Stefan im Rosental und Mettersdorf), die Bad Gleichenberger Energie GmbH (Bad "
             "Gleichenberg, Trautmannsdorf, Kapfenstein) und das EVU der Stadtgemeinde Mureck (Stadt Mureck, rund "
             "5 km², vollständig erdverkabelt). An den Bezirksrändern führt die E-Control für einzelne Postleitzahlen "
             "auch die Feistritzwerke-STEWEAG und die Netz Burgenland."),
            ("Freie Einspeisekapazität",
             "Umspannwerk Feldbach: 16,7 MW gebucht, 0,0 MW verfügbar. Umspannwerk Halbenrain: 20,2 MW gebucht, "
             "0,0 MW verfügbar (Energienetze Steiermark, Stand 1. Juli 2026, unverbindliche Momentaufnahme; jede "
             "Anfrage wird einzeln geprüft)."),
            ("Baubehörde und Genehmigung",
             "Grundsätzlich die Standortgemeinde (Bürgermeister). Photovoltaik auf Dach oder Fassade, Batteriespeicher bis 20 kWh "
             "und Wärmepumpen sind nach § 21 des Steiermärkischen Baugesetzes meldepflichtig: schriftliche Mitteilung "
             "an die Gemeinde vor der Ausführung."),
            ("Gasnetz",
             "Die E-Control führt einen Gasnetzbetreiber (Energienetze Steiermark) nur für einen Teil des Bezirks, "
             "etwa für die Postleitzahlen von Feldbach, Kirchberg an der Raab, Paldau, Bad Gleichenberg, Fehring, "
             "Bad Radkersburg und Klöch. Für Gnas, Straden, Kirchbach, Sankt Stefan im Rosental, Riegersburg oder "
             "Mureck ist keiner hinterlegt."),
            ("Solarpotenzial",
             "Das Land Steiermark zeigt im Digitalen Atlas (GIS Steiermark) für jedes erfasste Dach Eignung, möglichen "
             "Jahresertrag und kWp. Das SolarTool schickt den Bericht für eine ausgewählte Fläche per E-Mail."),
            ("Klima- und Energie-Modellregionen",
             "Wirtschaftsregion mittleres Raabtal (Feldbach, Paldau, Kirchberg an der Raab, Eichkögl), Netzwerk "
             "Südost (Fehring, Kapfenstein, Unterlamm, Riegersburg, Sankt Anna am Aigen), Wein- und Thermenregion "
             "Südoststeiermark (Bad Gleichenberg, Straden, Bad Radkersburg), Gnas, Sankt Peter am Ottersbach und "
             "Deutsch Goritz."),
            ("Energieberatung in der Region",
             "Lokale Energieagentur (LEA GmbH) in Feldbach: Die Stadtgemeinde Feldbach verweist für Förderansuchen "
             "bei Bund und Land auf deren Förderservice."),
        ],
    },

    "netz": {
        "h2": "Genehmigung und Netzanschluss in der Südoststeiermark: Gemeinde informieren, richtiges Netz finden",
        "betreiber": "dem für Ihre Adresse zuständigen Netzbetreiber",
        "paragraphs": [
            ("Für eine Photovoltaikanlage auf Dach oder Fassade brauchen Sie in Feldbach, Gnas oder Mureck kein "
             "Bauverfahren. Seit der Baugesetz-Novelle 2026 sind solche Anlagen in der Steiermark unabhängig von ihrer "
             "Größe meldepflichtig, solange sie nicht höher als 3,50 Meter sind. Die Mitteilung geht vor Baubeginn "
             "schriftlich an Ihre Gemeinde und nennt Grundstücksnummer, Lage am Grundstück und eine kurze Beschreibung. "
             "Batteriespeicher bis 20 kWh sind ebenfalls meldepflichtig, bis 100 kWh mit Nachweis des Herstellers zum "
             "Brandverhalten. Was landesweit gilt, steht ausführlich auf der Seite "
             + a("pv_steiermark", "Photovoltaik in der Steiermark") + "."),
            ("Der zweite Schritt ist in der Südoststeiermark weniger selbstverständlich als anderswo: Welches Netz ist "
             "zuständig? Neben dem Landesnetz der Energienetze Steiermark führt die E-Control die P.K. "
             "Energieversorgungs-GmbH rund um Feldbach, Kirchberg an der Raab, Kirchbach und Sankt Stefan im Rosental, "
             "die Bad Gleichenberger Energie GmbH und das EVU der Stadtgemeinde Mureck. Die Grenzen folgen nicht den "
             "Gemeindegrenzen, für die Postleitzahl von Feldbach sind zwei Netzbetreiber hinterlegt. Jeder hat eigene "
             "Formulare: Die Energienetze Steiermark arbeitet mit dem Einspeiserportal, Einspeisezählpunkt und "
             "Netzanschlusskonzept, das EVU Mureck mit einem Datenblatt für Erzeugungsanlagen und einer eigenen "
             "Fertigstellungsmeldung. Wir lesen den Netzbetreiber von Ihrer Stromrechnung ab und stellen das Ansuchen "
             "dort."),
            ("Der dritte Punkt ist die Einspeisung. Die Energienetze Steiermark veröffentlicht je Umspannwerk, wie viel "
             "Einspeiseleistung gebucht und wie viel frei ist. Mit Stand 1. Juli 2026 stehen dort für das Umspannwerk "
             "Feldbach 16,7 MW gebucht und 0,0 MW verfügbar, für Halbenrain 20,2 MW gebucht und 0,0 MW verfügbar. Der "
             "Netzbetreiber nennt das eine unverbindliche Momentaufnahme und prüft jede Anfrage einzeln; ein Verbot "
             "neuer Dachanlagen ist es nicht. Es bedeutet aber, dass der Netzbetreiber vorgeben kann, wie viel Leistung "
             "Sie einspeisen dürfen. Wir planen deshalb mit " + a("batteriespeicher", "Speicher") + ", Warmwasser, "
             "Wärmepumpe und " + a("ems", "Energiemanagement") + " so, dass möglichst viel Strom im Haus bleibt."),
        ],
        "bullets": [
            "PV auf Dach oder Fassade: schriftliche Mitteilung an die Gemeinde vor Baubeginn",
            "Speicher bis 20 kWh meldepflichtig, bis 100 kWh mit Nachweis des Herstellers",
            "Netz klären: Energienetze Steiermark, P.K. Energieversorgung, Bad Gleichenberger Energie oder EVU Mureck",
            "Einspeisezählpunkt und Netzzusage vor der Montage, Auslegung auf Eigenverbrauch",
        ],
        "img": "gen_detail",
        "alt": ("Symbolbild: Fachkraft mit Arbeitshandschuhen verschraubt mit dem Akkuschrauber eine Modulklemme auf "
                "der Aluminiumschiene einer Photovoltaikanlage"),
    },

    "waermepumpe": {
        "h2": "Wärmepumpe in der Südoststeiermark: Meldung, Gasnetz, Nahwärme und eigener Sonnenstrom",
        "paragraphs": [
            ("Auch die Wärmepumpe braucht in der Steiermark seit 2026 kein Bauverfahren mehr: Die ortsfeste Aufstellung "
             "ist meldepflichtig, egal wie groß das Gerät ist. Zur Mitteilung an die Gemeinde gehören das technische "
             "Datenblatt und die Bestätigung eines befugten Sachverständigen, dass der zulässige Planungsbasispegel an "
             "der Grundgrenze zum Nachbarn eingehalten wird. Auf einem freistehenden Hof ist dieser Nachweis meist "
             "schnell erbracht. In den dichter bebauten Ortskernen von Feldbach, Fehring oder Bad Radkersburg "
             "entscheidet der Aufstellort der Außeneinheit, deshalb planen wir ihn zuerst."),
            ("Was die Wärmepumpe ersetzt, hängt vom Ort ab. Einen Gasnetzbetreiber führt die E-Control nur für einen "
             "Teil des Bezirks, etwa für Feldbach, Fehring, Bad Gleichenberg und Bad Radkersburg. In Gnas, Straden, "
             "Kirchbach-Zerlach, Sankt Stefan im Rosental oder Mureck stellt sich die Frage Gas oder Wärmepumpe gar "
             "nicht. Dafür ist Biomasse-Nahwärme in der Region ein Thema: Zwei der vier Klima- und "
             "Energie-Modellregionen führen den Ausbau der Nahwärme als Schwerpunkt, und die Stadtgemeinde Feldbach "
             "nennt Fernwärmeanschlüsse in ihrer Förderliste. Führt ein Wärmenetz an Ihrem Grundstück vorbei, "
             "vergleichen wir den Anschluss offen mit der Wärmepumpe."),
            ("Am meisten bringt die Wärmepumpe zusammen mit der eigenen Photovoltaik. Wo die Einspeisung begrenzt sein "
             "kann, ist sie neben dem Warmwasser der größte Abnehmer für Ihren Sonnenstrom, und ein Speicher verschiebt "
             "den Mittagsstrom in den Abend. Ob Ihr Haus dafür bereit ist, hängt an Dämmung, Heizflächen und "
             "Vorlauftemperatur. Das sehen wir uns bei Ihnen im Heizraum an, bevor wir etwas anbieten. Mehr dazu im "
             "Ratgeber " + a("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau") + "."),
        ],
        "bullets": [
            "Aufstellung meldepflichtig: Datenblatt und Schallbestätigung gehen an die Gemeinde",
            "Gasnetz nur in einem Teil des Bezirks, Nahwärme als Alternative ehrlich geprüft",
            "Wärmepumpe und Warmwasser als Abnehmer für den eigenen Sonnenstrom",
        ],
        "img": "waermepumpe",
        "alt": "Symbolbild: Außeneinheit einer Luft-Wasser-Wärmepumpe mit zwei Ventilatoren vor einer Holzwand im Garten",
    },

    "foerderung_h2": "Förderung für Photovoltaik und Wärmepumpe in der Südoststeiermark",
    "foerderung_lokal": [
        ("Auf Gemeindeebene haben wir für die Stadtgemeinde Feldbach eine Angabe gefunden: Auf ihrer Klima- und "
         "Umweltseite nennt sie je 100 Euro für Photovoltaikanlagen und Stromspeicher (Gemeinderatsbeschluss vom "
         "November 2023) sowie je 200 Euro für Biomasseheizungen, Fernwärmeanschlüsse und Solaranlagen. Eine "
         "Wärmepumpe steht nicht in dieser Liste. Die dort verlinkten Antragsformulare waren im Oktober 2026 nicht "
         "abrufbar, deshalb klären wir vor dem Angebot mit dem Bauamt, ob die Förderung noch ausbezahlt wird."),
        ("Für Anträge bei Bund und Land verweist die Stadt Feldbach auf den Förderservice der Lokalen Energieagentur "
         "(LEA) in Feldbach. Für die anderen 24 Gemeinden des Bezirks haben wir keine aktuelle Richtlinie abgerufen: "
         "Wir fragen für Ihr Projekt direkt bei Ihrer Gemeinde nach und nehmen einen Zuschuss erst in die Rechnung, "
         "wenn er bestätigt ist."),
    ],

    "referenzen": {
        "h2": "Referenzen in der Nähe: zwei Projekte in Graz und ein landwirtschaftlicher Betrieb",
        "intro": ("Aus der Südoststeiermark selbst können wir noch kein dokumentiertes Projekt zeigen, und wir erfinden "
                  "keines. Die nächstgelegenen Referenzen stehen in Graz. Der landwirtschaftliche Betrieb im "
                  "Burgenland zeigt, wie Speicher und automatischer Notstrom auf einem Hof zusammenspielen."),
        "slugs": ["projekt-flachdach-in-graz", "projekt-stadthaus-in-graz", "projekt-landwirtschaft-im-burgenland"],
    },

    "umgebung": ["Feldbach", "Fehring", "Bad Radkersburg", "Mureck", "Bad Gleichenberg", "Gnas",
                 "Kirchbach-Zerlach", "Sankt Stefan im Rosental", "Riegersburg", "Straden",
                 "Kirchberg an der Raab", "Paldau"],

    "links": [
        ("/energiegemeinschaft-steiermark/", "Energiegemeinschaft in der Steiermark"),
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau"),
        ("/notstrom/", "Notstrom mit Photovoltaik"),
        ("pv_gewerbe", "Photovoltaik für Gewerbe und Betriebe"),
    ],

    "faq": [
        ("Welcher Netzbetreiber ist in der Südoststeiermark für meine Photovoltaikanlage zuständig?",
         "Das hängt von der Adresse ab. Im Großteil des Bezirks ist es die Energienetze Steiermark GmbH. Laut "
         "Tarifkalkulator der E-Control gibt es daneben die P.K. Energieversorgungs-GmbH (unter anderem in den "
         "Postleitzahlgebieten von Feldbach, Kirchberg an der Raab, Paldau, Kirchbach und Sankt Stefan im Rosental), "
         "die Bad Gleichenberger Energie GmbH und das EVU der Stadtgemeinde Mureck. Welches Netz für Ihr Haus gilt, "
         "steht auf Ihrer Stromrechnung. Wir klären das vor der Planung und stellen das Ansuchen beim richtigen "
         "Netzbetreiber."),
        ("Brauche ich in Feldbach, Fehring oder Bad Radkersburg eine Baubewilligung für die Photovoltaikanlage?",
         "Für Anlagen auf Dach oder Fassade nein. Sie sind nach § 21 des Steiermärkischen Baugesetzes meldepflichtig, "
         "seit der Novelle 2026 unabhängig von der Größe, solange die Anlage nicht höher als 3,50 Meter ist. Die "
         "Mitteilung geht vor Baubeginn schriftlich an Ihre Gemeinde und enthält Grundstücksnummer, Lage und eine "
         "kurze Beschreibung. Baubehörde ist grundsätzlich die Standortgemeinde. Ob in einem "
         "Ortskern zusätzliche Vorgaben zum Ortsbild gelten, fragen wir für Ihr Grundstück beim Bauamt ab."),
        ("Für das Umspannwerk Feldbach ist keine Einspeisekapazität frei. Kann ich trotzdem eine PV-Anlage bauen?",
         "Die Energienetze Steiermark weist mit Stand 1. Juli 2026 für die Umspannwerke Feldbach und Halbenrain "
         "0,0 MW verfügbare Einspeisekapazität aus, nennt das aber eine unverbindliche Momentaufnahme und prüft jede "
         "Anfrage einzeln. Für Ihr Haus zählt die Zusage, die der Netzbetreiber nach dem Ansuchen um einen "
         "Einspeisezählpunkt ausstellt. Darin kann die Einspeiseleistung begrenzt sein. Wir legen die Anlage in der "
         "Südoststeiermark deshalb auf hohen Eigenverbrauch aus: mit Speicher, Warmwasser, Wärmepumpe und "
         "Energiemanagement."),
        ("Was kostet eine Photovoltaikanlage mit Speicher in der Südoststeiermark?",
         "Eine Komplettanlage mit rund 10 kWp und Speicher kostet typischerweise rund 15.000 bis 22.000 Euro vor "
         "Förderung, inklusive Montage und Anmeldung beim Netzbetreiber (EBZ-Richtpreis, Stand Oktober 2026). Eine "
         "Landespauschale gibt es in der Steiermark nicht, es bleibt der Investitionszuschuss des Bundes. Die "
         "Stadtgemeinde Feldbach nennt auf ihrer Umweltseite zusätzlich je 100 Euro für Photovoltaik und "
         "Stromspeicher. Nach der Beratung bei Ihnen vor Ort bekommen Sie einen Projektbericht mit 3D-Belegplan und "
         "Statikreport und ein Fixangebot."),
        ("Brauche ich in der Südoststeiermark eine Genehmigung für eine Wärmepumpe?",
         "Ein Bauverfahren ist in der Regel nicht mehr nötig. Seit der Novelle des Steiermärkischen Baugesetzes 2026 "
         "ist die ortsfeste Aufstellung einer Wärmepumpe meldepflichtig, unabhängig von der Leistung. Der "
         "schriftlichen Mitteilung an die Gemeinde liegen das technische Datenblatt und die Bestätigung eines "
         "befugten Sachverständigen bei, dass der zulässige Planungsbasispegel an der Grundgrenze zum Nachbarn "
         "eingehalten wird. Wir wählen den Aufstellort der Außeneinheit so, dass dieser Nachweis gelingt, und "
         "bereiten die Unterlagen für Ihre Gemeinde vor."),
        ("In meiner Gemeinde gibt es kein Gasnetz. Ist die Wärmepumpe dann die richtige Heizung?",
         "Oft ja, aber nicht automatisch. Die E-Control führt nur für einen Teil der Südoststeiermark einen "
         "Gasnetzbetreiber, etwa für die Postleitzahlen von Feldbach, Fehring, Bad Gleichenberg und Bad Radkersburg, "
         "nicht aber für Gnas, Straden, Kirchbach oder Mureck. Zugleich führen zwei der vier Klima- und "
         "Energie-Modellregionen im Bezirk den Ausbau der Nahwärme als Schwerpunkt. Liegt ein Wärmenetz vor der Tür, vergleichen wir "
         "den Anschluss offen mit der Wärmepumpe. Entscheidend sind Dämmung, Heizflächen und Vorlauftemperatur: Das "
         "sehen wir uns im Heizraum an, bevor wir etwas anbieten."),
        ("Zahlt die Stadt Feldbach oder meine Gemeinde eine Förderung für Photovoltaik, Speicher oder Wärmepumpe?",
         "Die Stadtgemeinde Feldbach nennt auf ihrer Klima- und Umweltseite je 100 Euro für Photovoltaikanlagen und "
         "Stromspeicher sowie je 200 Euro für Biomasseheizungen, Fernwärmeanschlüsse und Solaranlagen. Eine "
         "Wärmepumpe steht nicht in dieser Liste. Die verlinkten Antragsformulare waren im Oktober 2026 nicht "
         "abrufbar, deshalb fragen wir vor dem Angebot beim Bauamt nach. Für Anträge bei Bund und Land verweist die "
         "Stadt auf die Lokale Energieagentur in Feldbach. Für alle anderen Gemeinden des Bezirks prüfen wir die "
         "Förderung einzeln."),
        ("Hat EBZ Energie einen Standort in der Südoststeiermark?",
         "Nein. Firmensitz ist die Triglavstraße 15 in Villach, einen Standort in der Steiermark gibt es nicht. Wir "
         "beraten und montieren in Kärnten und der Steiermark und kommen für die Erstberatung zu Ihnen, ob nach "
         "Feldbach, Gnas oder Bad Radkersburg. Ein dokumentiertes Referenzprojekt aus dem Bezirk können wir noch "
         "nicht zeigen, die nächstgelegenen stehen in Graz. Die Montage übernehmen zertifizierte Fachkräfte, und Sie "
         "haben einen festen Ansprechpartner von der Planung bis zur Übergabe."),
    ],

    "quellen": [
        ("Landesstatistik Steiermark: Bezirksdaten Südoststeiermark (Fläche, Einwohner, Gebäude, Agrarstruktur; "
         "aktualisiert 8. September 2026)",
         "https://www.landesentwicklung.steiermark.at/cms/dokumente/12256490_141979478/413b52d8/623.pdf"),
        ("Bezirkshauptmannschaft Südoststeiermark: Gemeinden des Bezirkes",
         "https://www.bh-suedoststeiermark.steiermark.at/cms/ziel/58158963/DE/"),
        ("E-Control: Strom- und Gasnetzbetreiber finden (Tarifkalkulator, Abfrage nach Postleitzahl)",
         "https://www.e-control.at/konsumenten/strom-und-gasnetzbetreiber-finden"),
        ("Energienetze Steiermark: Erzeugungsanlagen (Einspeiserportal, Einspeisezählpunkt, Netzanschlusskonzept)",
         "https://www.e-netze.at/Strom/Erzeugungsanlagen/Default.aspx"),
        ("Energienetze Steiermark: Freie Einspeisekapazitäten je Umspannwerk (Stand 1. Juli 2026)",
         "https://www.e-netze.at/Service/FEK/Default.aspx"),
        ("EVU der Stadtgemeinde Mureck: Stromnetz und Formulare für Erzeugungsanlagen",
         "https://evu-mureck.at/stromnetz/"),
        ("Bad Gleichenberger Energie GmbH: Stromnetz und Versorgung", "https://bg-energie.at/"),
        ("Land Steiermark: Steiermärkisches Baurecht (Baugesetz in der Fassung LGBl. Nr. 20/2026, Erläuterungen zum "
         "Deregulierungsgesetz LGBl. Nr. 19/2026)",
         "https://www.technik.steiermark.at/cms/beitrag/11549819/58813874/"),
        ("Land Steiermark, Abteilung 13: Verfahrenshandbuch Photovoltaik- und Solarthermieanlagen (Stand August 2025)",
         "https://www.verwaltung.steiermark.at/cms/dokumente/12898224_173036325/f51050a9/Verfahrenshandbuch%20Erneuerbare%20Energie%20PV%20und%20Solaranlagen.pdf"),
        ("Land Steiermark: Solarpotenzial Steiermark im Digitalen Atlas und SolarTool",
         "https://www.technik.steiermark.at/cms/beitrag/12756734/99241573/"),
        ("Steirisches Vulkanland: Energievision 2035 und Klima- und Energie-Modellregionen",
         "https://www.vulkanland.at/regionalwirtschaft/energievision-2025/"),
        ("Lokale Energieagentur (LEA): Klima- und Energie-Modellregion Wirtschaftsregion mittleres Raabtal",
         "https://www.lea.at/klima-und-energiemodellregion-wirtschaftsregion-mittleres-raabtal/"),
        ("Lokale Energieagentur (LEA): Klima- und Energie-Modellregion Wein- und Thermenregion Südoststeiermark",
         "https://www.lea.at/klima-und-energiemodellregion-wein-und-thermenregion-suedoststeiermark/"),
        ("Stadtgemeinde Feldbach: Umweltförderungen", "https://feldbach.gv.at/klima/umweltfoerderungen/"),
        ("Stadtgemeinde Feldbach: Beihilfen, Förderungen, Unterstützungen (Bauen)",
         "https://feldbach.gv.at/buerger-a-z/beihilfen-foerderungen-unterstuetzungen-bauen"),
    ],

    "notizen": ("Faktenfragen: (1) Netzbetreiber im Raum Feldbach/Gniebing: E-Control führt die P.K. "
                "Energieversorgungs-GmbH, die Stadt Feldbach nannte 2016 das EVU Lugitsch. Wer ist heute zuständig? "
                "(2) Zahlt Feldbach die 100 Euro für PV und Speicher noch aus (Formulare 404)? (3) Gibt es ein "
                "EBZ-Projekt im Bezirk, das als Referenz dokumentiert werden darf? (4) Gilt in der Altstadt von Bad "
                "Radkersburg eine Ortsbild-Richtlinie für PV (PDF der Stadt nicht mehr abrufbar)?"),
}
