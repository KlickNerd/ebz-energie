"""Ortsseite Photovoltaik und Wärmepumpe Voitsberg (/photovoltaik-voitsberg/), Inhalt fuer die Vorlage standorte.py.

Briefing: build/seo/standort_voitsberg.json (DataForSEO, nur Oesterreich/Deutsch, 10.10.2026).
Primaer "photovoltaik voitsberg" (10/Monat, Spitzen 40 im Maerz/April), Umland "photovoltaik bärnbach" (10);
"wärmepumpe voitsberg", "photovoltaik köflach", "photovoltaik weststeiermark" ohne messbares Volumen.

Lokale Fakten, alle am 10.10.2026 selbst abgerufen:
- Stromnetz: Stadtwerke Voitsberg GmbH ist Verteilernetzbetreiber (Informationsblatt gem. § 46 ElWG). Gebiet laut
  stadtwerke-voitsberg.at/versorgung/strom/: Voitsberg, Krottendorf-Gaisfeld, Ligist, St. Johann-Köppling, Ortsteile
  von Bärnbach, Rosental, St. Martin, Stallhofen; 39 km2, 8.400 Abnehmeranlagen, 124 Trafostationen, 2 Umspannwerke.
  Buergerbeteiligungs-PV Schlossberg: 1,8 MWp, 1,8 GWh/Jahr, in Betrieb seit 15.10.2021.
  PV-Ablauf laut stadtwerke-voitsberg.at/service-fuer-mich/photovoltaik/: Ausfuehrungsmeldung (Elektroinstallateur),
  Netzpruefung, Zaehlpunktnummer, Netzzusage 12 Monate befristet, Fertigstellungsmeldung, Netzzugangsvertrag.
- Stadtwerke Koeflach GmbH (stadtwerke-koeflach.at/1/stromanbieter/netzgebiet): Netz 200 km2, Koeflach,
  Maria Lankowitz, Edelschrott, St. Martin am Woellmissberg; Ortsteile von Baernbach, Rosental a. d. Kainach
  (dazu Grosslobming, Weisskirchen im Murtal); 8.700 Kundenanlagen, 131 Trafostationen.
  NICHT belegt: wer im restlichen Bezirk (Mooskirchen, Soeding, Kainach, Geistthal-Soedingberg, Hirschegg-Pack)
  Netzbetreiber ist. Deshalb im Text kein Name dafuer.
- Baurecht: Erlaeuterungen des Landes zum Stmk. Deregulierungsgesetz (LGBl. Nr. 19/2026, technik.steiermark.at) und
  Gesetzestext § 21 Stmk. BauG im Meldeformular einer steirischen Gemeinde (08/2026): PV auf Dach/Fassade
  meldepflichtig unabhaengig von der Groesse (§ 21 Abs. 1 Z 2 lit. o), Hoehe max. 3,50 m, Freiflaeche bis 100 kWp;
  Batterie bis 20 kWh meldepflichtig, bis 100 kWh mit Thermal-Runaway-Nachweis (Abs. 2 Z 2a); Waermepumpe
  meldepflichtig unabhaengig von der Leistung (Abs. 2 Z 2b) mit Datenblatt und Sachverstaendigen-Bestaetigung zum
  Planungsbasispegel (Abs. 3 Z 5). RIS selbst war nicht abrufbar (Bot-Sperre), daher Land Steiermark als Quelle.
- Flaechenwidmungsplan 4.0 der Stadtgemeinde Voitsberg (Wortlaut, voitsberg.gv.at): § 4 Immissionsschutzzone
  (fluessige und feste Brennstoffe unzulaessig, Biomasse ausgenommen, gilt fuer Neubau und Zu-/Umbau mit
  Heizungserneuerung, Bestand unberuehrt); Stadtkern als Zone mit erhaltenswertem Orts- und Strassenbild
  ersichtlich gemacht ("kein Ortsbild-Schutzgebiet", aber Beurteilung nach § 43 BauG).
- Fernwaerme: Liste der Nah- und Fernwaermenetze des Landes, Stand Oktober 2026: Netz VO_002 der Energie Steiermark
  Waerme GmbH (ganzjaehrig) fuer Voitsberg, Baernbach, Koeflach, Rosental an der Kainach, Maria Lankowitz;
  kleinere Netze in Ligist, Krottendorf-Gaisfeld, Edelschrott, Hirschegg-Pack.
- Zahlen: Statistik Austria "Ein Blick auf die Gemeinde" 61625: Voitsberg 9.517 Einwohner, Bezirk 51.101 (2026).
  BH Voitsberg: 15 Gemeinden, 679,2 km2 (die BH nennt 52.242 Einwohner ohne Stichtag: nicht verwendet).
- Kohle: Stadtchronik voitsberg.gv.at (1762 erstmals erfolgreich nach Kohle geschuerft); Anfragebeantwortung
  1500/AB XXII. GP des Wirtschaftsministeriums (Kohleliefervertrag bis 30.6.2004, Schliessung Kraftwerk
  Voitsberg 3 mit 30.6.2006 notifiziert); Energie-Erlebnispark Zangtal auf ehemaligem Bergbaugelaende.
- Klima: Pionierstadt Voitsberg (Klimaneutralitaetsplan 2040, FFG-Projekt 5131590, abgeschlossen 30.11.2025);
  KEM WEST (Koeflach, Hirschegg-Pack, Edelschrott, Sankt Martin am Woellmissberg, Maria Lankowitz, Start 2024).
  Voitsberg selbst liegt in keiner KEM.
- Gemeindefoerderung: auf voitsberg.gv.at (Aufgaben/Formulare, Umwelt, Verordnungen) nichts zu PV, Speicher oder
  Heizungstausch gefunden.

Bewusst weggelassen (keine selbst abgerufene amtliche Quelle): Ertrag je kWp, Sonnenstunden, Seehoehe,
Gasnetz, Zahl der Fernwaermekunden (nur Pressemeldung 2015), Entfernungen und Fahrzeiten.
Kein eigener Standort in der Steiermark: Firmensitz ist Villach, Referenzen aus Graz (nicht aus dem Bezirk).
"""

from common import a

ORT = {
    "key": "pv_voitsberg",
    "name": "Voitsberg",
    "kurz": "Voitsberg",
    "area_name": "Bezirk Voitsberg",
    "land": "stmk",
    "title": "Photovoltaik Voitsberg: PV, Speicher & Wärmepumpe | EBZ",
    "description": ("Photovoltaik und Wärmepumpe in Voitsberg, Köflach und Bärnbach: Fachbetrieb aus Villach, "
                    "Netzantrag beim Stadtwerk, 10 kWp mit Speicher um 15.000 bis 22.000 €."),
    "eyebrow": "Photovoltaik und Wärmepumpe im Bezirk Voitsberg",
    "h1": "Photovoltaik und Wärmepumpe in Voitsberg: Planung vor Ort, Netzantrag bei den Stadtwerken",
    "lead": ("EBZ Energie ist ein Fachbetrieb aus Villach und plant und montiert Photovoltaik, Speicher und "
             "Wärmepumpen im Bezirk Voitsberg: in der Stadt selbst, in Köflach, Bärnbach und den Gemeinden rundum. "
             "Für die Erstberatung kommen wir zu Ihnen vor Ort. Eine Besonderheit klären wir gleich am Anfang: "
             "Je nach Adresse ist ein anderes Stadtwerk Ihr Stromnetzbetreiber."),
    "badges": [
        ("2 Stadtwerke-Netze", "Voitsberg und Köflach: wir klären, welches für Sie gilt"),
        ("Meldung statt Bauverfahren", "für PV am Dach und für die Wärmepumpe"),
        ("ab 147 €/Monat*", "Finanzierung inkl. Speicher, Eigentum ab Tag 1"),
    ],
    "hero_img": "gen_eigenheim",
    "hero_alt": ("Einfamilienhaus mit Photovoltaikanlage auf dem Satteldach vor Bergkulisse im Abendlicht "
                 "(Symbolbild, nicht in Voitsberg aufgenommen)"),

    "intro": {
        "h2": "Vom Kohlerevier zum Sonnenstrom: warum Photovoltaik und Wärmepumpe nach Voitsberg passen",
        "paragraphs": [
            ("Voitsberg ist Bezirkshauptstadt in der Weststeiermark, der Lipizzanerheimat. In der Stadt leben laut "
             "Statistik Austria 9.517 Menschen, im Bezirk mit seinen 15 Gemeinden 51.101 (Stand 2026). Über "
             "Generationen war die Gegend ein Kohlerevier: Laut Stadtchronik wurde 1762 in der Umgebung "
             "erfolgreich nach Kohle geschürft, später kamen Eisenbahn, Glasfabrik und Kraftwerk dazu."),
            ("Dieses Kapitel ist abgeschlossen. Für das Kraftwerk Voitsberg 3 wurden laut Wirtschaftsministerium das "
             "Ende des Kohleliefervertrags mit Mitte 2004 und die Schließung mit Mitte 2006 festgelegt. Heute steht "
             "am Schlossberg eine Bürgerbeteiligungsanlage der Stadtwerke Voitsberg mit "
             "1,8 MWp, die seit Oktober 2021 rund 1,8 GWh Sonnenstrom im Jahr liefert. Das frühere Bergbaugelände "
             "im Zangtal ist heute der Energie-Erlebnispark Zangtal, und die Stadtgemeinde hat in einem geförderten Projekt einen "
             "Fahrplan zur Klimaneutralität bis 2040 erarbeitet."),
            ("Was die Region im Großen hinter sich hat, lässt sich am eigenen Dach und im eigenen Heizraum "
             "wiederholen. Eine Photovoltaikanlage mit rund 10 kWp und Speicher kostet typischerweise 15.000 bis "
             "22.000 Euro vor Förderung* und senkt die Stromkosten um bis zu 85 Prozent*. Ob Ihr Dach passt, zeigt "
             "als erste Orientierung das Solarpotenzial im Digitalen Atlas Steiermark. Verbindlich wird es mit "
             "unserem Projektbericht mit 3D-Belegplan und Statikreport. Kommt eine "
             + a("waermepumpe", "Wärmepumpe") + " dazu, nutzt sie den eigenen Strom für Heizung und Warmwasser."),
        ],
    },

    "lokal": {
        "h2": "Voitsberg auf einen Blick: Bezirk, Netzbetreiber, Behörde",
        "intro": ("Die Angaben stammen von Stadtgemeinde, Stadtwerken, Bezirkshauptmannschaft, Land Steiermark und "
                  "Statistik Austria (Stand Oktober 2026). Die Quellen sind weiter unten verlinkt."),
        "rows": [
            ("Bezirk", "Voitsberg: 15 Gemeinden auf 679,2 km², 51.101 Einwohner (Statistik Austria, 2026). "
                       "Die Stadt Voitsberg hat 9.517 Einwohner und ist Sitz der Bezirkshauptmannschaft."),
            ("Stromnetz Voitsberg", "Stadtwerke Voitsberg GmbH, Hauptplatz 35. Das Verteilernetz versorgt laut "
                                    "Stadtwerken rund 8.400 Zählpunkte in Voitsberg, Krottendorf-Gaisfeld, Ligist und "
                                    "St. Johann-Köppling (Gemeinde Söding-Sankt Johann) sowie in Ortsteilen von "
                                    "Bärnbach, Rosental, St. Martin und Stallhofen."),
            ("Stromnetz Köflach", "Stadtwerke Köflach GmbH: rund 8.700 Kundenanlagen in Köflach, Maria Lankowitz, "
                                  "Edelschrott und St. Martin am Wöllmißberg sowie in Ortsteilen von Bärnbach und "
                                  "Rosental an der Kainach."),
            ("Genehmigung", "Photovoltaik auf Dach oder Fassade und die Wärmepumpe sind nach § 21 des "
                            "Steiermärkischen Baugesetzes meldepflichtig. Die schriftliche Mitteilung geht vor der "
                            "Ausführung an die Gemeinde, in Voitsberg an die Stadtgemeinde (Stadtbauamt, Hauptplatz 1)."),
            ("Solarpotenzial", "Der Digitale Atlas Steiermark zeigt die Eignung von Dachflächen für Photovoltaik und "
                               "Solarthermie. Über das SolarTool des Landes lässt sich für einzelne Flächen ein "
                               "Bericht anfordern."),
            ("Fernwärme", "Energie Steiermark Wärme GmbH: ganzjährig betriebenes Netz für Voitsberg, Bärnbach, "
                          "Köflach, Rosental an der Kainach und Maria Lankowitz (Liste des Landes, Stand Oktober 2026). "
                          "Kleinere Nahwärmenetze gibt es unter anderem in Ligist, Krottendorf-Gaisfeld und Edelschrott."),
            ("Heizen im Stadtgebiet", "Der Flächenwidmungsplan der Stadtgemeinde weist Immissionsschutzzonen aus, in "
                                      "denen flüssige und feste Brennstoffe (ausgenommen Biomasse) bei Neubau und "
                                      "Heizungserneuerung im Zuge von Zu- und Umbauten unzulässig sind."),
            ("Klimaprogramme", "Voitsberg ist Pionierstadt mit Klimaneutralitätsplan 2040. Köflach, Maria Lankowitz, "
                               "Edelschrott, Hirschegg-Pack und Sankt Martin am Wöllmißberg bilden die Klima- und "
                               "Energie-Modellregion KEM WEST."),
        ],
    },

    "netz": {
        "h2": "PV-Anlage in Voitsberg anmelden: Mitteilung an die Gemeinde, Netzzusage vom Stadtwerk",
        "betreiber": "den Stadtwerken Voitsberg oder dem für Ihre Adresse zuständigen Netzbetreiber",
        "paragraphs": [
            ("In der Steiermark brauchen Photovoltaikanlagen auf Dach- oder Fassadenflächen kein Bauverfahren mehr. "
             "Seit dem Steiermärkischen Deregulierungsgesetz (LGBl. Nr. 19/2026) sind sie nach § 21 des "
             "Steiermärkischen Baugesetzes unabhängig von ihrer Größe meldepflichtig: Das Vorhaben wird der Gemeinde "
             "vor der Ausführung schriftlich mitgeteilt, mit Grundstücksnummer, Lage am Grundstück und kurzer "
             "Beschreibung. Die Anlage darf samt ihren Teilen nicht höher als 3,50 Meter sein. Batteriespeicher sind "
             "bis 20 kWh ebenfalls nur zu melden, bis 100 kWh mit einem Sicherheitsnachweis des Herstellers. In "
             "Voitsberg geht die Mitteilung an die Stadtgemeinde, die das Formular für meldepflichtige Vorhaben "
             "online bereitstellt."),
            ("Eine Voitsberger Eigenheit betrifft den Stadtkern: Der Flächenwidmungsplan macht das Zentrum innerhalb "
             "der historischen Stadtgrenzen als Zone mit erhaltenswertem Orts- und Straßenbild ersichtlich. Das ist "
             "laut Wortlaut kein Ortsbild-Schutzgebiet, fließt aber in die Beurteilung nach dem Baugesetz ein. Bei "
             "Häusern in der Altstadt stimmen wir die Modulbelegung deshalb vorab mit dem Stadtbauamt ab."),
            ("Den Netzanschluss beantragen wir beim zuständigen Stromnetzbetreiber, und der ist im Bezirk nicht "
             "überall derselbe. In Voitsberg, Krottendorf-Gaisfeld, Ligist und St. Johann-Köppling sowie in Teilen "
             "von Bärnbach, Rosental, St. Martin und Stallhofen sind es die Stadtwerke Voitsberg, in Köflach, Maria "
             "Lankowitz, Edelschrott und St. Martin am Wöllmißberg die Stadtwerke Köflach. Bei den Stadtwerken "
             "Voitsberg läuft es so: Ausführungsmeldung durch den Elektroinstallateur, Netzprüfung, "
             "Zählpunktnummer und eine auf 12 Monate befristete Netzzusage, nach der Montage die "
             "Fertigstellungsmeldung und der Netzzugangsvertrag."),
        ],
        "bullets": [
            "Mitteilung an die Gemeinde statt Bauverfahren (PV auf Dach und Fassade)",
            "Netzzusage der Stadtwerke Voitsberg: 12 Monate gültig",
            "Stadtwerke Voitsberg oder Stadtwerke Köflach: wir klären, welches Netz für Ihre Adresse gilt",
            "Speicher bis 20 kWh: nur Meldung, kein Verfahren",
        ],
        "img": "gen_detail",
        "alt": ("Montage einer Photovoltaikanlage: Hände in Arbeitshandschuhen verschrauben ein Modul auf der "
                "Aluminiumschiene eines Daches (Symbolbild)"),
    },

    "waermepumpe": {
        "h2": "Wärmepumpe in Voitsberg: erst die Fernwärme prüfen, dann richtig auslegen",
        "paragraphs": [
            ("Vor jeder Wärmepumpe steht in Voitsberg eine Frage: Liegt Fernwärme vor dem Haus? Die Energie "
             "Steiermark Wärme GmbH betreibt hier ganzjährig ein Fernwärmenetz, das laut Liste des Landes Steiermark "
             "auch Bärnbach, Köflach, Rosental an der Kainach und Maria Lankowitz umfasst. In Ligist, "
             "Krottendorf-Gaisfeld und Edelschrott führt das Land kleinere Nahwärmenetze. Wo eine Leitung in der Nähe "
             "liegt, lohnt der Vergleich mit dem Anschluss. Für Häuser abseits der Trassen ist die "
             "Luft-Wasser-Wärmepumpe die naheliegende Lösung, um von Öl, Gas oder Kohle wegzukommen."),
            ("Dazu kommt eine lokale Regel: Der Flächenwidmungsplan der Stadtgemeinde Voitsberg weist "
             "Immissionsschutzzonen aus. Dort sind flüssige und feste Brennstoffe für die Gebäudeheizung unzulässig, "
             "ausgenommen Biomasse in genehmigten Heizungsanlagen. Die Festlegung gilt für Neubauten sowie für Zu- "
             "und Umbauten, bei denen die Heizung erneuert oder vergrößert wird. Bestehende Anlagen bleiben "
             "unberührt. Eine Wärmepumpe verbrennt vor Ort keinen Brennstoff. Ob Ihr Grundstück in einer solchen Zone "
             "liegt, sehen wir im Flächenwidmungsplan für Sie nach."),
            ("Baurechtlich ist die Wärmepumpe seit 2026 einfacher geworden: Die ortsfeste Aufstellung ist unabhängig "
             "von der Leistung nur mehr meldepflichtig (§ 21 Abs. 2 Z 2b Stmk. BauG). Der Mitteilung an die Gemeinde "
             "liegen das technische Datenblatt und die Bestätigung eines befugten Sachverständigen bei, dass der "
             "zulässige Planungsbasispegel an der relevanten Nachbargrundgrenze eingehalten wird. Den Aufstellort des "
             "Außengeräts planen wir von Anfang an danach. Mit einer " + a("photovoltaik", "Photovoltaikanlage")
             + " am Dach und einem " + a("ems", "Energiemanagement") + " läuft die Wärmepumpe bevorzugt dann, wenn "
             "eigener Strom da ist."),
        ],
        "bullets": [
            "Fernwärme-Check vor dem Angebot: Leitung in der Nähe oder nicht",
            "Meldung an die Gemeinde mit Datenblatt und Schallbestätigung",
            "Auslegung nach Heizlast, Heizkörpern und Vorlauftemperatur Ihres Hauses",
        ],
        "img": "waermepumpe",
        "alt": "Außengerät einer Wärmepumpe an einer Hauswand (Symbolbild)",
    },

    "foerderung_h2": "Förderung für Photovoltaik und Wärmepumpe in Voitsberg",
    "foerderung_lokal": [
        ("Die Stadtgemeinde Voitsberg weist auf ihrer Website derzeit kein eigenes Förderprogramm für Photovoltaik, "
         "Stromspeicher oder Heizungstausch aus (Stand Oktober 2026). Das kann sich mit einem Gemeinderatsbeschluss "
         "ändern, und die Nachbargemeinden entscheiden jeweils selbst. Wir fragen deshalb vor jedem Angebot bei Ihrer "
         "Wohnsitzgemeinde nach."),
        ("Im Bezirk laufen zwei Programme des Klima- und Energiefonds: Voitsberg ist Pionierstadt mit einem Fahrplan "
         "zur Klimaneutralität bis 2040, Köflach, Maria Lankowitz, Edelschrott, Hirschegg-Pack und Sankt Martin am "
         "Wöllmißberg bilden die Klima- und Energie-Modellregion KEM WEST mit einer Ansprechperson in der "
         "Stadtgemeinde Köflach. Beides sind keine Förderungen für Privathaushalte."),
    ],

    "referenzen": {
        "h2": "Referenzen aus der Steiermark: zwei Projekte in Graz",
        "intro": ("Auf unserer Referenzliste steht noch kein Projekt aus dem Bezirk Voitsberg. Die nächstgelegenen "
                  "dokumentierten Anlagen haben wir in Graz gebaut: ein Einfamilienhaus und ein Stadthaus, beide mit "
                  "Speicher und Wallbox."),
        "slugs": ["projekt-flachdach-in-graz", "projekt-stadthaus-in-graz"],
    },

    "umgebung": [
        "Köflach", "Bärnbach", "Rosental an der Kainach", "Maria Lankowitz", "Ligist", "Söding-Sankt Johann",
        "Krottendorf-Gaisfeld", "Mooskirchen", "Stallhofen", "Edelschrott", "Sankt Martin am Wöllmißberg",
        "Kainach bei Voitsberg",
    ],

    "links": [
        ("/energiegemeinschaft-steiermark/", "Energiegemeinschaft in der Steiermark"),
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau"),
        ("/kosten-einer-solaranlage/", "Was eine Solaranlage kostet"),
        ("/pv-speicher-nachruesten/", "PV-Speicher nachrüsten"),
    ],

    "faq": [
        ("Wer ist in Voitsberg der Stromnetzbetreiber für meine PV-Anlage?",
         "In der Stadt Voitsberg sind es die Stadtwerke Voitsberg. Ihr Verteilernetz reicht laut eigener Angabe auch "
         "nach Krottendorf-Gaisfeld, Ligist und St. Johann-Köppling sowie in Teile von Bärnbach, Rosental, St. Martin "
         "und Stallhofen. Köflach, Maria Lankowitz und Edelschrott gehören zum Netz der Stadtwerke Köflach. Welcher "
         "Betreiber für Ihre Adresse gilt, steht auf der Stromrechnung. Wir klären das vor dem Angebot und stellen "
         "den Netzantrag für Sie."),
        ("Brauche ich in Voitsberg eine Baubewilligung für eine Photovoltaikanlage?",
         "Nein, für Anlagen auf Dach oder Fassade nicht. Nach § 21 des Steiermärkischen Baugesetzes sind sie "
         "unabhängig von der Größe meldepflichtig: Die Stadtgemeinde Voitsberg erhält vor der Ausführung eine "
         "schriftliche Mitteilung mit Grundstücksnummer, Lage und Beschreibung. Die Anlage darf samt Teilen höchstens "
         "3,50 Meter hoch sein. Im Stadtkern mit erhaltenswertem Ortsbild stimmen wir die Belegung vorab mit dem "
         "Stadtbauamt ab. Die Mitteilung bereiten wir für Sie vor."),
        ("Was kostet eine Photovoltaikanlage mit Speicher in Voitsberg?",
         "Eine Anlage mit rund 10 kWp und Speicher kostet typischerweise 15.000 bis 22.000 Euro vor Förderung, "
         "inklusive Montage, Netzanmeldung bei den Stadtwerken und Inbetriebnahme. Das ist ein Richtwert aus unseren "
         "Projekten. Den Fixpreis für Ihr Haus in Voitsberg nennen wir nach dem Termin vor Ort im Angebot. Typisch "
         "ist eine Amortisation in 4 bis 6 Jahren. Auf Wunsch finanzieren Sie ab 147 Euro im Monat "
         "(Beispielkondition), die Anlage gehört Ihnen ab dem ersten Tag."),
        ("Gibt es in Voitsberg eine Gemeindeförderung für Photovoltaik oder Heizungstausch?",
         "Die Stadtgemeinde Voitsberg weist derzeit kein eigenes Förderprogramm für Photovoltaik, Speicher oder "
         "Heizungstausch aus (Stand Oktober 2026). Eine PV-Pauschale des Landes gibt es in der Steiermark nicht, es "
         "bleibt der Investitionszuschuss des Bundes. Weil Gemeinden ihre Programme jederzeit ändern können, fragen "
         "wir vor jedem Angebot bei Ihrer Wohnsitzgemeinde nach, auch in Köflach, Bärnbach oder Ligist. Welche "
         "Programme gerade offen sind, zeigt unser Förderrechner."),
        ("Wärmepumpe oder Fernwärme in Voitsberg: Was passt zu meinem Haus?",
         "Das hängt zuerst von der Lage ab. In Voitsberg, Bärnbach, Köflach, Rosental an der Kainach und Maria "
         "Lankowitz betreibt die Energie Steiermark Wärme GmbH ein Fernwärmenetz. Liegt eine Leitung in der Nähe, "
         "lohnt der Vergleich mit dem Anschluss. Ob er technisch möglich ist, klärt der Betreiber. Abseits der "
         "Trassen ist die Luft-Wasser-Wärmepumpe meist die passende Lösung, besonders zusammen mit Photovoltaik. Wir "
         "prüfen beides, bevor wir ein Angebot schreiben."),
        ("Muss ich eine Wärmepumpe in Voitsberg genehmigen lassen?",
         "Ein Bauverfahren ist nicht mehr nötig. Die ortsfeste Aufstellung einer Wärmepumpe ist in der Steiermark "
         "meldepflichtig. Die Mitteilung an die Stadtgemeinde Voitsberg enthält das technische Datenblatt und die "
         "Bestätigung eines befugten Sachverständigen, dass der zulässige Planungsbasispegel an der Grundgrenze zum "
         "nächsten Nachbarn eingehalten wird. Deshalb planen wir den Standort des Außengeräts früh und kümmern uns um "
         "die Unterlagen."),
        ("Was bedeutet die Immissionsschutzzone in Voitsberg für meine Heizung?",
         "Der Flächenwidmungsplan der Stadtgemeinde Voitsberg weist Immissionsschutzzonen aus. Dort sind flüssige und "
         "feste Brennstoffe für die Gebäudeheizung unzulässig, ausgenommen Biomasse in genehmigten Anlagen. Das gilt "
         "für Neubauten und für Zu- und Umbauten, bei denen die Heizung erneuert oder vergrößert wird. Bestehende "
         "Heizungen bleiben unberührt. Eine Wärmepumpe verbrennt vor Ort keinen Brennstoff. Ob Ihr Grundstück "
         "betroffen ist, sehen wir im Flächenwidmungsplan nach."),
        ("EBZ Energie sitzt in Villach: Montieren Sie wirklich im Bezirk Voitsberg?",
         "Ja. Unser Firmensitz ist die Triglavstraße 15 in Villach, einen Standort in Voitsberg haben wir nicht. "
         "Kärnten und die Steiermark sind unser Montagegebiet, dazu gehören alle 15 Gemeinden des Bezirks von "
         "Voitsberg, Köflach und Bärnbach bis Hirschegg-Pack und Geistthal-Södingberg. Die Erstberatung findet bei "
         "Ihnen zu Hause statt, zertifizierte Fachkräfte montieren, und ein fester Ansprechpartner begleitet Sie von "
         "der Planung bis zur Übergabe."),
    ],

    "quellen": [
        ("Stadtwerke Voitsberg: Stromversorgung, Versorgungsgebiet und PV-Anlage Schlossberg",
         "https://www.stadtwerke-voitsberg.at/versorgung/strom/"),
        ("Stadtwerke Voitsberg: Photovoltaik, Netzzusage und Ablauf der Anmeldung",
         "https://www.stadtwerke-voitsberg.at/service-fuer-mich/photovoltaik/"),
        ("Stadtwerke Köflach: Netzgebiet", "https://www.stadtwerke-koeflach.at/1/stromanbieter/netzgebiet"),
        ("Land Steiermark, Baurecht: Steiermärkisches Baugesetz und Erläuterungen zum Deregulierungsgesetz "
         "(LGBl. Nr. 19/2026)", "https://www.technik.steiermark.at/cms/beitrag/11549819/58813874/"),
        ("Stadtgemeinde Voitsberg: Flächenwidmungsplan 4.0 (Immissionsschutzzone, Ortsbild im Stadtkern)",
         "https://www.voitsberg.gv.at/de/stadtgemeinde/amtl-mitteilungen/laufend/flaechenwidmungsplaene-und-bebauungsplaene.html"),
        ("Stadtgemeinde Voitsberg: Formulare Baurecht (§ 21 meldepflichtige Vorhaben)",
         "https://www.voitsberg.gv.at/de/buergerinnenservice/aufgaben-formulare.html"),
        ("Land Steiermark: Liste der Nah- und Fernwärmenetze (Stand Oktober 2026)",
         "https://www.technik.steiermark.at/cms/beitrag/12809578/161425384/"),
        ("Land Steiermark: Solarpotenzial im Digitalen Atlas und SolarTool",
         "https://landesentwicklung.steiermark.at/cms/beitrag/12910759/145230171"),
        ("Statistik Austria: Ein Blick auf die Gemeinde Voitsberg (Bevölkerung 2026)",
         "https://www.statistik.at/blickgem/G0201/g61625.pdf"),
        ("Bezirkshauptmannschaft Voitsberg: Zahlen, Daten, Fakten",
         "https://www.bh-voitsberg.steiermark.at/cms/ziel/58206097/DE/"),
        ("Stadtgemeinde Voitsberg: Geschichte der Stadt", "https://www.voitsberg.gv.at/de/stadtgemeinde/geschichte.html"),
        ("Parlament: Anfragebeantwortung 1500/AB XXII. GP zum Kraftwerk Voitsberg",
         "https://www.parlament.gv.at/dokument/XXII/AB/1500/fname_019855.pdf"),
        ("Klima- und Energiefonds: Pionierstadt Voitsberg",
         "https://orte-von-morgen.at/ort/pionierstadt-voitsberg/?place-id=368"),
        ("Klima- und Energiefonds: Klima- und Energie-Modellregion KEM WEST",
         "https://orte-von-morgen.at/ort/kem-west/?place-id=6212"),
        ("Energie-Erlebnispark Zangtal", "https://energie-erlebnispark.at/"),
    ],

    "notizen": (
        "Faktenfragen an den Kunden: (1) Gibt es ein EBZ-Projekt im Bezirk Voitsberg, das als Referenz freigegeben "
        "werden kann? (2) Erfahrungen mit Netzzusagen der Stadtwerke Voitsberg und Köflach (Dauer, "
        "Einspeisebegrenzung)? (3) Plant EBZ auch Fernwärme-Alternativen ehrlich zu empfehlen (Text sagt: Vergleich "
        "lohnt)? (4) Wer macht bei EBZ die Schallbestätigung für die Wärmepumpe (befugter Sachverständiger)? "
        "Unsicherheiten: Netzbetreiber im restlichen Bezirk (Mooskirchen, Söding, Kainach, Geistthal-Södingberg, "
        "Hirschegg-Pack) nicht belegt und deshalb nicht benannt. Förderung Wärmepumpe Land Steiermark: laut "
        "wohnbau.steiermark.at (abgerufen 10.10.2026) derzeit keine Antragstellung für neue Wärmepumpen; deckt sich "
        "mit der zentralen Kurzfassung in standorte.py und build/seo/_fakten_2026-10.md. Im Ortstext steht deshalb "
        "kein Landes-Fördersatz. Die Einwohnerzahl 5.816 auf der Seite 'Pionierstadt Voitsberg' des Klimafonds "
        "widerspricht Statistik Austria (9.517) und wurde nicht verwendet."
    ),
}
