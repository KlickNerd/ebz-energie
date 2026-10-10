"""Ortsseite Voelkermarkt (/photovoltaik-voelkermarkt/): Photovoltaik (Primaer) und Waermepumpe (Sekundaer).

Briefing: build/seo/standort_voelkermarkt.json / .md (DataForSEO, nur Oesterreich/Deutsch, 10.10.2026).
"photovoltaik voelkermarkt", "waermepumpe voelkermarkt" und alle Umland-Varianten (Bleiburg, Klopeiner See,
Jauntal, Unterkaernten, Suedkaernten, Eberndorf, Griffen) haben kein messbares Suchvolumen. Die Seite zielt
deshalb auf den Local-/Long-Tail-Intent und auf zitierbare lokale Fakten (GEO).

Lokale Fakten, alle am 10.10.2026 selbst abgerufen:
- Stadtgemeinde Voelkermarkt, Energie & Umwelt (voelkermarkt.gv.at/buergerservice/energie-umwelt): e5-Gemeinde,
  3e, Verweis auf KEM Suedkaernten, Foerderung von Solaranlagen und Elektrofahrzeugen.
- e5-Auditbericht 2021 (Amt der Kaerntner Landesregierung, Abt. 8; PDF auf voelkermarkt.gv.at): 137,44 km2,
  10.866 Einwohner (Statistik Austria 2021), 461 m, Schotterterrasse ueber dem Voelkermarkter Stausee,
  ehem. Gemeinden Haimburg, St. Peter am Wallersberg, Tainach, Waisenberg; Elektrizitaetsversorgung Kelag,
  Waermeversorgung Kelag Waerme; Stadtzentrum mit Fernwaerme versorgt, Biomasse-Nahwaerme Tainach;
  PV 2020: 230,9 kWp je 1.000 EW (Kaernten 268,1; Quelle KNG GmbH, Statistik Austria); 24 % erneuerbar
  beheizte Bruttogeschossflaeche (AGWR, Erfassung laut Bericht verbesserungsbeduerftig); Umsetzungsgrad 61,3 %;
  Rathaus unter Denkmalschutz; Energiegemeinschaften als Potenzial fuer kommunale PV.
- Stadtgemeinde Voelkermarkt, Bauen & Planen: Baupolizei, Abteilung Bauwesen und Raumordnung, Formular
  "Mitteilung ... bewilligungsfreies Bauvorhaben nach § 7 Abs. 1 K-BO 1996", Hinweis auf Teilbebauungsplaene.
- Stadtgemeinde Voelkermarkt, Foerderungen + Richtlinie "Foerderung von Solaranlagen im Eigenheimbau"
  (Fassung 1991, Betraege in Euro): 200 Euro Baukostenzuschuss, NUR thermische Solaranlagen
  (Brauchwasser, auch mit Niedertemperaturheizung). Kein Programm fuer PV, Speicher, Waermepumpe.
- RIS (Open-Data-Dokument LKT40020954): § 7 K-BO 1996, Fassung in Kraft seit 21.02.2026. Abs. 1 lit. a Z 20:
  mitteilungspflichtig sind bauliche Anlagen, die erneuerbare Energie erzeugen oder elektrische Energie
  speichern (keine Flaechengrenze mehr im Text); Abs. 4: schriftliche Mitteilung vor Beginn der Ausfuehrung.
- Kaernten Netz (kaerntennetz.at/pv.htm, /unsere-projekte.htm): Anschlussantrag im Kundenportal,
  Netzberechnung, Netzzutrittsangebot, Einspeiseleistung mindestens in Hoehe des Strombezugsrechts;
  Umspannwerk Bleiburg: 110-kV-Schaltanlage, rund 5 Mio. Euro, 2025 bis 2027.
- Kelag/Kaernten Netz, Unternehmensmeldung 17.06.2025 (news.at, Corporate News): 2,7 Mio. Euro fuer das
  Ortsnetz Voelkermarkt, 36 Trafostationen, 8,9 km Mittelspannungs- und 33,7 km Niederspannungskabel.
- Klima- und Energiefonds (orte-von-morgen.at, KEM Suedkaernten): 13 Gemeinden = Bezirk Voelkermarkt,
  41.981 Einwohner, Buero Klagenfurter Strasse 10 in Voelkermarkt, PV 0,17 (2017) -> 1,30 kWp je EW (2024),
  Thema "Oelkesselfreies Suedkaernten".
- Kelag (kelag.at): Waermepumpen-Praemie 1.200 Euro, Kelag-Stromliefervertrag in Kaernten, Internetanbindung,
  Gutschrift ueber zwei Jahre.
Nicht erreichbar in dieser Sitzung: ktn.gv.at und kagis.ktn.gv.at (Verbindung abgelehnt). Deshalb KEIN
Hinweis auf den Solarpotenzialkataster (KAGIS) und keine Angaben der BH Voelkermarkt.
"""

from common import a

ORT = {
    "key": "pv_voelkermarkt",
    "name": "Völkermarkt",
    "kurz": "Völkermarkt",
    "area_name": "Bezirk Völkermarkt",
    "land": "ktn",
    "title": "Photovoltaik Völkermarkt & Wärmepumpe vor Ort | EBZ Energie",
    "description": ("Photovoltaik und Wärmepumpe in Völkermarkt, Bleiburg und im Jauntal: Fachbetrieb aus Villach, "
                    "Netzanmeldung bei Kärnten Netz, 3.000 € Landespauschale."),
    "eyebrow": "Photovoltaik und Wärmepumpe Völkermarkt · Jauntal",
    "h1": "Photovoltaik und Wärmepumpe in Völkermarkt: für Stadt, Jauntal und Klopeiner See",
    "lead": ("Völkermarkt ist Bezirkshauptstadt, e5-Gemeinde und Sitz der Klima- und Energie-Modellregion "
             "Südkärnten. EBZ Energie ist ein Fachbetrieb aus Villach und plant Photovoltaik, Speicher und "
             "Wärmepumpe bei Ihnen vor Ort in Völkermarkt, vom Stadtkern über Tainach bis Haimburg. Die Mitteilung "
             "an die Baupolizei, die Netzanmeldung bei Kärnten Netz und die Förderanträge bereiten wir vor."),
    "badges": [("13 Gemeinden", "im Bezirk, Beratung vor Ort"),
               ("Kärnten Netz", "Netzanmeldung inklusive"),
               ("3.000 €", "Landespauschale für PV mit Speicher")],
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit Photovoltaikanlage auf dem Dach, Symbolbild (kein Foto aus Völkermarkt)",
    "intro": {
        "h2": "Sonnenstrom in Völkermarkt: Die Region holt auf, viele Dächer sind noch frei",
        "paragraphs": [
            ("Die Stadt liegt auf 461 Metern Seehöhe auf einer Schotterterrasse über dem Völkermarkter Stausee, "
             "die Karawanken im Süden und die Saualpe im Nordosten sind in Sichtweite, die Stadt selbst liegt im "
             "Flach- und Hügelland (e5-Auditbericht 2021 des Landes Kärnten). In Kärnten liefert eine "
             "Photovoltaikanlage als Richtwert rund 1.000 bis 1.100 kWh je kWp und Jahr*, eine Anlage mit 10 kWp "
             "also etwa 10.000 bis 11.000 kWh. Was Ihr Dach in Völkermarkt tatsächlich hergibt, rechnen wir im "
             "Projektbericht mit 3D-Belegplan und Statikreport, samt Verschattung durch Nachbarhäuser und Bäume."),
            ("Beim Ausbau hatte die Stadtgemeinde lange Nachholbedarf: 2020 waren 230,9 kWp Photovoltaik je "
             "1.000 Einwohner installiert, der Kärnten-Schnitt lag bei 268,1 kWp. Der Auditbericht hält dazu fest, "
             "dass hier Potenzial für PV-Angebote besteht. Seither geht es schnell: In der Klima- und "
             "Energie-Modellregion Südkärnten, zu der alle 13 Gemeinden des Bezirks gehören, stieg die "
             "installierte Leistung von 0,17 kWp je Einwohner (2017) auf 1,30 kWp je Einwohner (2024)."),
            ("Die Großgemeinde reicht mit den früheren Gemeinden Haimburg, St. Peter am Wallersberg, Tainach und "
             "Waisenberg weit über den Stadtkern hinaus: 137 Quadratkilometer, rund 10.900 Einwohner. Für das "
             "Stadthaus am Hauptplatz gelten andere Fragen als für das Einfamilienhaus in Tainach oder den Hof "
             "in Haimburg. Deshalb planen wir nach Ihrem Verbrauch, nach Dach und Zählerschrank und nicht nach "
             "einer Standardgröße. Für das Lavanttal östlich des Bezirks gibt es eine eigene Seite: "
             + a("pv_wolfsberg", "Photovoltaik Wolfsberg") + "."),
        ],
    },
    "lokal": {
        "h2": "Völkermarkt auf einen Blick: Netz, Behörde, Wärme und Förderung",
        "intro": ("Diese Angaben stammen von der Stadtgemeinde, vom Land Kärnten, vom Netzbetreiber und vom Klima- "
                  "und Energiefonds. Sie entscheiden darüber, wie Ihre Anlage in Völkermarkt geplant, gemeldet und "
                  "angeschlossen wird."),
        "rows": [
            ("Bezirk", "Völkermarkt ist Bezirkshauptstadt. Zum Bezirk gehören 13 Gemeinden mit zusammen rund "
                       "42.000 Einwohnern, vom Jauntal über den Klopeiner See bis Eisenkappel-Vellach."),
            ("Stadtgemeinde", "137,44 km², 461 m Seehöhe, 10.866 Einwohner (Statistik Austria 2021). Dazu gehören "
                              "die früheren Gemeinden Haimburg, St. Peter am Wallersberg, Tainach und Waisenberg."),
            ("Netzbetreiber", "Kärnten Netz GmbH, die Netztochter der Kelag. Der Anschlussantrag für die "
                              "PV-Anlage läuft über das Kundenportal, die mögliche Einspeiseleistung ergibt eine "
                              "Netzberechnung."),
            ("Baubehörde", "Stadtgemeinde Völkermarkt, Baupolizei (Abteilung Bauwesen und Raumordnung), "
                           "Hauptplatz 1. Für mitteilungspflichtige Vorhaben nach § 7 der Kärntner Bauordnung "
                           "gibt es ein eigenes Formular der Stadtgemeinde."),
            ("Wärmenetze", "Das Stadtzentrum ist mit Fernwärme versorgt (Kelag Wärme), in Tainach gibt es eine "
                           "Biomasse-Nahwärme. Vor dem Heizungstausch prüfen wir, ob Ihre Adresse im "
                           "Versorgungsgebiet liegt."),
            ("Klima und Energie", "e5-Gemeinde seit 2013, zuletzt mit drei von fünf e ausgezeichnet "
                                  "(Umsetzungsgrad 61,3 Prozent im Audit 2021). Das Büro der Klima- und "
                                  "Energie-Modellregion Südkärnten sitzt in der Klagenfurter Straße 10."),
            ("Gemeindeförderung", "Kein eigenes Programm für Photovoltaik, Speicher oder Wärmepumpe. Die "
                                  "Stadtgemeinde fördert thermische Solaranlagen im Eigenheim mit 200 Euro und "
                                  "den Ankauf von Elektrofahrzeugen."),
            ("Energieberatung", "Die Stadtgemeinde verweist auf den geförderten Vor-Ort-Energiecheck des Landes "
                                "Kärnten: rund zwei Stunden unabhängige, produktneutrale Beratung im Haus durch "
                                "das Netzwerk Energieberatung Kärnten."),
        ],
    },
    "netz": {
        "h2": "Genehmigung und Netzanschluss in Völkermarkt: Mitteilung an die Baupolizei, Antrag bei Kärnten Netz",
        "betreiber": "der Kärnten Netz GmbH",
        "paragraphs": [
            ("Nach § 7 der Kärntner Bauordnung (Fassung 2026) sind bauliche Anlagen, die erneuerbare Energie "
             "erzeugen oder elektrische Energie speichern, mitteilungspflichtig: Für die PV-Anlage mit Speicher auf "
             "dem Hausdach braucht es in der Regel kein Bauverfahren. "
             "Die Mitteilung geht vor Beginn der Arbeiten schriftlich an die Behörde und nennt den Ausführungsort "
             "mit Katastralgemeinde und Grundstücksnummer sowie eine kurze Beschreibung. In Völkermarkt nimmt sie "
             "die Baupolizei der Stadtgemeinde entgegen. Die Stadtgemeinde weist darauf hin, dass es neben dem "
             "textlichen Bebauungsplan viele Teilbebauungspläne gibt: Wir klären deshalb vorab, was für Ihr "
             "Grundstück gilt, und ebenso, was bei denkmalgeschützten Häusern im Stadtkern zulässig ist."),
            ("Den Netzanschluss beantragen wir für Sie im Kundenportal von Kärnten Netz. Der Netzbetreiber "
             "ermittelt mit einer Netzberechnung, wie viel Leistung an Ihrem Anschlusspunkt eingespeist werden "
             "darf, und schickt ein Netzzutrittsangebot. Geht die gewünschte Leistung nicht, sichert Kärnten Netz "
             "zumindest eine Einspeisung in Höhe Ihres Strombezugsrechts zu; als Alternativen nennt der "
             "Netzbetreiber einen anderen Anschlusspunkt oder eine dynamische Leistungsregelung. Vor der "
             "Inbetriebnahme folgt die Fertigstellungsmeldung durch den konzessionierten Elektriker."),
            ("In Völkermarkt wird das Netz gerade erneuert: Kärnten Netz investiert nach eigenen Angaben rund "
             "2,7 Millionen Euro in das Ortsnetz der Stadt, mit 36 erneuerten Trafostationen, 8,9 Kilometern "
             "Mittelspannungskabel und 33,7 Kilometern Niederspannungskabel (Unternehmensmeldung Juni 2025). Im "
             "Umspannwerk Bleiburg, das für die Stromversorgung im Bezirk wichtig ist, wird bis 2027 die "
             "110-kV-Schaltanlage erneuert, ausdrücklich auch für zusätzliche Kapazitäten zur Einbindung "
             "erneuerbarer Energien."),
        ],
        "bullets": [
            "Schriftliche Mitteilung an die Baupolizei Völkermarkt vor Baubeginn",
            "Anschlussantrag im Kundenportal von Kärnten Netz mit Netzberechnung",
            "Fertigstellungsmeldung, Zählertausch und Inbetriebnahme aus einer Hand",
        ],
        "img": "gen_detail",
        "alt": "Fachkraft montiert Photovoltaikmodule auf einer Unterkonstruktion, Symbolbild für die Montage in Völkermarkt",
    },
    "waermepumpe": {
        "h2": "Wärmepumpe in Völkermarkt: erst das Wärmenetz prüfen, dann mit Sonnenstrom heizen",
        "paragraphs": [
            ("Beim Heizungstausch in Völkermarkt steht eine Frage am Anfang: Liegt Ihr Haus an einem Wärmenetz? "
             "Das Stadtzentrum ist laut e5-Auditbericht gut mit Fernwärme versorgt, in Tainach wurde eine "
             "Biomasse-Nahwärme errichtet, und die Stadtgemeinde hat ihre in Frage kommenden Gebäude "
             "angeschlossen. Ist der Anschluss an Ihrer Adresse möglich, sagen wir Ihnen das offen. Überall "
             "sonst, in den Siedlungen am Stadtrand, in Haimburg, St. Peter am Wallersberg oder Waisenberg und "
             "in den Gemeinden des Jauntals, ist die Wärmepumpe meist der direkte Weg weg von Öl und Gas."),
            ("Der Bedarf ist da: Im Gebäuderegister waren zum Audit 2021 nur 24 Prozent der Bruttogeschoßfläche "
             "in der Stadtgemeinde als erneuerbar beheizt erfasst (die Erfassung gilt laut Bericht als "
             "lückenhaft), und die Modellregion arbeitet am Thema „Ölkesselfreies Südkärnten“. Eine "
             "Luft-Wasser-Wärmepumpe kostet im Einfamilienhaus rund 12.000 bis 22.000 Euro vor Förderung*, im "
             "Altbau mit Anpassungen rund 15.000 bis 28.000 Euro*. Bis 55 Grad Vorlauftemperatur arbeitet sie "
             "effizient, die Montage dauert 2 bis 4 Tage."),
            ("Richtig günstig wird das Heizen mit eigenem Strom. Ein gut gedämmtes Haus mit 12.000 kWh "
             "Wärmebedarf braucht bei Jahresarbeitszahl 4 rund 3.000 kWh Strom im Jahr*. Kärnten Netz empfiehlt "
             "selbst, große Verbraucher wie Wärmepumpe und E-Auto schon bei der Auslegung der PV-Anlage "
             "einzurechnen. Wir planen deshalb beides gemeinsam: Dach, Speicher, Wärmepumpe und ein "
             "Energiemanagement, das die Wärmepumpe bevorzugt dann laufen lässt, wenn die Sonne scheint."),
        ],
        "bullets": [
            "Prüfung, ob Fernwärme oder Nahwärme an Ihrer Adresse in Völkermarkt möglich ist",
            "Heizflächen-Check im Bestand: Reichen die Heizkörper bei 50 bis 55 Grad Vorlauf?",
            a("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau: wann sie passt und wann nicht"),
        ],
        "img": "waermepumpe",
        "alt": "Außengerät einer Luft-Wasser-Wärmepumpe an einem Wohnhaus, Symbolbild",
    },
    "foerderung_h2": "Förderung für Photovoltaik und Wärmepumpe in Völkermarkt",
    "foerderung_lokal": [
        ("Die Stadtgemeinde Völkermarkt weist derzeit kein eigenes Förderprogramm für Photovoltaik, Stromspeicher "
         "oder Wärmepumpen aus. Auf ihrer Website nennt sie zwei Gemeindeförderungen: einen Baukostenzuschuss von "
         "200 Euro für thermische Solaranlagen im Eigenheim (Warmwasser, auch mit Niedertemperaturheizung; kein "
         "Rechtsanspruch, nach Maßgabe der Mittel) und eine Förderung für den Ankauf von Elektrofahrzeugen. Ob "
         "sich daran etwas geändert hat, fragen wir vor dem Angebot bei der Stadtgemeinde nach."),
        ("Unabhängig von Land und Bund zahlt die Kelag eine Wärmepumpen-Prämie von 1.200 Euro: Voraussetzung sind "
         "ein aktiver Kelag-Stromliefervertrag in Kärnten und eine Wärmepumpe mit Internetanbindung, die Prämie "
         "kommt als Gutschrift über zwei Jahre auf die Stromrechnung."),
    ],
    "referenzen": {
        "h2": "Referenzen aus Kärnten: die nächstgelegenen dokumentierten Projekte",
        "intro": ("Aus dem Bezirk Völkermarkt ist auf unserer Website noch kein Projekt dokumentiert, deshalb zeigen "
                  "wir hier keines. Die nächstgelegenen Anlagen mit Zahlen stehen in Krumpendorf am Wörthersee, am "
                  "Ossiachersee und in Villach."),
        "slugs": ["projekt-mehrparteienhaus-krumpendorf", "projekt-pv-am-ossiachersee",
                  "projekt-einfamilienhaus-villach"],
    },
    "umgebung": ["Bleiburg", "Eberndorf", "St. Kanzian am Klopeiner See", "Griffen", "Eisenkappel-Vellach",
                 "Feistritz ob Bleiburg", "Sittersdorf", "Globasnitz", "Gallizien", "Ruden", "Neuhaus", "Diex"],
    "links": [
        ("/energiegemeinschaft-kaernten/", "Energiegemeinschaft in Kärnten"),
        ("/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/", "PV-Komplettanlage 10 kWp mit Speicher"),
        ("/notstrom/", "Notstrom mit Photovoltaik und Speicher"),
    ],
    "faq": [
        ("Welcher Netzbetreiber ist in Völkermarkt für meine PV-Anlage zuständig?",
         "Die Kärnten Netz GmbH, die Netztochter der Kelag. Der Anschlussantrag wird im Kundenportal gestellt, das "
         "übernehmen wir als bevollmächtigter Planer. Kärnten Netz berechnet, wie viel Leistung an Ihrem "
         "Anschlusspunkt eingespeist werden darf, und schickt ein Netzzutrittsangebot. Ist die gewünschte Leistung "
         "nicht möglich, sichert der Netzbetreiber zumindest eine Einspeisung in Höhe Ihres Strombezugsrechts zu. "
         "In Völkermarkt erneuert Kärnten Netz derzeit das Ortsnetz mit 36 Trafostationen."),
        ("Brauche ich in Völkermarkt eine Baubewilligung für eine Photovoltaikanlage?",
         "In der Regel nicht. Nach § 7 der Kärntner Bauordnung sind Anlagen, die erneuerbare Energie erzeugen oder "
         "Strom speichern, mitteilungspflichtig: Vor Beginn der Arbeiten geht eine schriftliche Mitteilung mit "
         "Grundstücksnummer, Katastralgemeinde und kurzer Beschreibung an die Baupolizei der Stadtgemeinde "
         "Völkermarkt. Wir bereiten sie vor und klären vorab, ob für Ihr Grundstück ein Teilbebauungsplan gilt "
         "oder das Haus unter Denkmalschutz steht."),
        ("Was kostet eine PV-Anlage mit Speicher in Völkermarkt und wie viel Strom liefert sie?",
         "Eine Komplettanlage mit rund 10 kWp und Speicher kostet typischerweise rund 15.000 bis 22.000 Euro vor "
         "Förderung, inklusive Montage, Netzanmeldung bei Kärnten Netz und Inbetriebnahme (Richtpreis, Stand "
         "Oktober 2026). In Kärnten liefert sie als Richtwert rund 10.000 bis 11.000 kWh im Jahr. Typisch sind "
         "eine Amortisation von 4 bis 6 Jahren und bis zu 85 Prozent weniger Stromkosten. Den Wert für Ihr Dach in "
         "Völkermarkt rechnen wir im Projektbericht mit 3D-Belegplan und Statikreport."),
        ("Fördert die Stadtgemeinde Völkermarkt Photovoltaik oder Stromspeicher?",
         "Nein, ein eigenes Programm für Photovoltaik, Stromspeicher oder Wärmepumpen weist die Stadtgemeinde "
         "Völkermarkt derzeit nicht aus. Sie fördert thermische Solaranlagen im Eigenheim mit 200 Euro und den "
         "Ankauf von Elektrofahrzeugen. Für Ihre PV-Anlage zählen deshalb die Landespauschale Kärnten von 3.000 "
         "Euro für PV ab 5 kWp mit Speicher ab 5 kWh und der Investitionszuschuss des Bundes. Was heute "
         "beantragbar ist, zeigt unser Förderrechner."),
        ("Wärmepumpe oder Fernwärme: Was passt in Völkermarkt?",
         "Das hängt von der Adresse ab. Das Stadtzentrum von Völkermarkt ist mit Fernwärme versorgt, in Tainach "
         "gibt es eine Biomasse-Nahwärme. Liegt Ihr Haus im Versorgungsgebiet, ist der Anschluss oft die "
         "einfachste Lösung, und wir sagen Ihnen das offen. Außerhalb der Wärmenetze ist die Luft-Wasser-Wärmepumpe "
         "meist die passende Wahl, besonders zusammen mit einer Photovoltaikanlage, die einen Teil des Stroms "
         "selbst liefert."),
        ("Funktioniert eine Wärmepumpe im Jauntal auch im älteren Haus mit Heizkörpern?",
         "Meistens ja. Entscheidend ist die Vorlauftemperatur: Bis 55 Grad arbeitet eine moderne "
         "Luft-Wasser-Wärmepumpe effizient, und alte Heizkörper sind oft groß genug ausgelegt. Beim Termin in "
         "Völkermarkt, Bleiburg oder Eberndorf prüfen wir Heizflächen, Dämmung und Platz für das Außengerät. Im "
         "Altbau kostet der Umstieg mit Anpassungen rund 15.000 bis 28.000 Euro vor Förderung. Ist das Haus "
         "ungedämmt, sagen wir Ihnen, wenn zuerst Fenster oder Dämmung an der Reihe sind."),
        ("Kommt EBZ Energie auch nach Bleiburg, Eberndorf, Griffen oder an den Klopeiner See?",
         "Ja. Wir beraten und montieren im ganzen Bezirk Völkermarkt: in der Stadt Völkermarkt mit Tainach und "
         "Haimburg, in Bleiburg, Eberndorf, St. Kanzian am Klopeiner See, Griffen, Eisenkappel-Vellach und den "
         "weiteren Gemeinden des Jauntals. Unser Firmensitz ist die Triglavstraße 15 in Villach, einen Standort in "
         "Völkermarkt haben wir nicht. Für die Erstberatung kommen wir zu Ihnen, sie ist kostenlos und "
         "unverbindlich."),
        ("Kann ich in Völkermarkt Sonnenstrom in einer Energiegemeinschaft teilen?",
         "Ja. Energiegemeinschaften sind österreichweit möglich. Teilen Sie den Strom im Nahbereich, sinken die "
         "Netzentgelte um bis zu 57 Prozent (lokal) oder 28 Prozent (regional); beim österreichweiten Teilen in "
         "einer Bürgerenergiegemeinschaft gibt es diesen Rabatt nicht. Der e5-Auditbericht der Stadtgemeinde "
         "Völkermarkt nennt Energiegemeinschaften ausdrücklich als Weg, Strom aus Photovoltaik stärker vor Ort zu "
         "nutzen. Die Zuordnung der Zählpunkte läuft über Kärnten Netz."),
    ],
    "quellen": [
        ("Stadtgemeinde Völkermarkt: Energie und Umwelt (e5-Gemeinde, Gemeindeförderungen)",
         "https://voelkermarkt.gv.at/buergerservice/energie-umwelt"),
        ("Amt der Kärntner Landesregierung, Abt. 8: e5-Auditbericht 2021 der Stadtgemeinde Völkermarkt (PDF)",
         "https://voelkermarkt.gv.at/fileadmin/voelkermarkt/03-Buergerservice/Energie_und_Umwelt/e5_Auditbericht_Voelkermarkt.pdf"),
        ("Stadtgemeinde Völkermarkt: Bauen und Planen (Baupolizei, Mitteilung nach § 7 K-BO)",
         "https://voelkermarkt.gv.at/buergerservice/bauen-planen"),
        ("Stadtgemeinde Völkermarkt: Richtlinien für die Förderung von Solaranlagen im Eigenheimbau (PDF)",
         "https://voelkermarkt.gv.at/fileadmin/voelkermarkt/02-Amtstafel/Foerderungen/Foerderung-Solaranlagen.pdf"),
        ("Rechtsinformationssystem des Bundes: Kärntner Bauordnung 1996, § 7 (mitteilungspflichtige Vorhaben)",
         "https://ogd.ris.bka.gv.at/Dokumente/Landesnormen/LKT40020954/LKT40020954.html"),
        ("Kärnten Netz: PV-Anlage anschließen (Antrag, Netzberechnung, Einspeiseleistung)",
         "https://www.kaerntennetz.at/pv.htm"),
        ("Kärnten Netz: Unsere Projekte (Erneuerung Umspannwerk Bleiburg)",
         "https://www.kaerntennetz.at/unsere-projekte.htm"),
        ("Kelag und Kärnten Netz: Stromnetzausbau in Völkermarkt (Unternehmensmeldung, Juni 2025)",
         "https://www.news.at/pm/kelag-voelkermarkt-glasfaserleitung"),
        ("Klima- und Energiefonds: Klima- und Energie-Modellregion Südkärnten",
         "https://orte-von-morgen.at/ort/kem-suedkaernten/?place-id=49"),
        ("Land Kärnten, Netzwerk Energieberatung: Vor-Ort-Energiecheck (Folder, PDF)",
         "https://voelkermarkt.gv.at/fileadmin/voelkermarkt/03-Buergerservice/Energie_und_Umwelt/e5/e5_Download-Vor-Ort-Energiecheck.pdf"),
        ("Kelag: Wärmepumpen-Prämie", "https://www.kelag.at/privatkunden/ubersicht-zur-warmepumpe.htm"),
    ],
    "notizen": (
        "Faktenfragen fuer den Kunden / offene Punkte: "
        "(1) Hat EBZ im Bezirk Voelkermarkt schon Anlagen gebaut? Dann eine Referenz in referenz_projekte.py "
        "aufnehmen und hier an erste Stelle setzen. "
        "(2) Die Solar-Richtlinie der Stadtgemeinde traegt 'Fassung 1991' und nennt eine Befristung auf fuenf "
        "Jahre, steht aber mit Euro-Betraegen aktuell auf der Website: bei der Stadtgemeinde nachfragen, ob sie "
        "noch ausbezahlt wird und ob es 2026/2027 eine PV- oder Heizungsfoerderung gibt. "
        "(3) e5: Website und Auditbericht 2021 nennen 3e; das naechste Audit (Turnus vier Jahre) koennte 4e "
        "gebracht haben, Ergebnis nicht auffindbar. "
        "(4) Ortsnetz-Erneuerung (36 Trafostationen, 2,7 Mio. Euro) stammt aus einer Unternehmensmeldung von Kelag "
        "und Kaernten Netz auf news.at (Corporate News, 17.06.2025), nicht von der Website des Netzbetreibers. "
        "(5) KAGIS-Solarpotenzialkataster und BH Voelkermarkt nicht verlinkt: ktn.gv.at war in der Sitzung nicht "
        "erreichbar. "
        "(6) Kelag-Praemie 1.200 Euro steht auch auf der Villach-Seite; Aktualitaet vor Livegang pruefen. "
        "(7) Waermepumpe und § 7 K-BO: Ob das Aussengeraet als mitteilungspflichtige Anlage gilt, ist im Text "
        "bewusst nicht behauptet."
    ),
}
