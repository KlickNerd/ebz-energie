"""Ortsseite Feldkirchen in Kaernten (/photovoltaik-feldkirchen/), Vorlage build/pages/standorte.py.

Briefing: build/seo/standort_feldkirchen.json (DataForSEO, nur Oesterreich/Deutsch, 10.10.2026).
Primaer "photovoltaik feldkirchen" (10), dazu "pv feldkirchen" (10), "photovoltaik feldkirchen kaernten" (10).
Die SERPs mischen Feldkirchen in Kaernten mit Feldkirchen bei Graz, Feldkirchen an der Donau und
Feldkirchen bei Mattighofen: deshalb steht "in Kaernten" in Title, H1, Description, Lead und FAQ.

Lokale Fakten, alle am 10.10.2026 selbst abgerufen (URLs in ORT["quellen"]):
- Stadtgemeinde Feldkirchen, Daten und Fakten: Bezirkshauptstadt, noerdlicher Rand des Klagenfurter Beckens,
  Seehoehe 550 bis 900 m (tiefster Punkt 510 m, hoechster 1.069 m), 77,49 km2, Ortschaften, Auslaeufer der Nockberge.
- Statistik Austria, Blick auf die Gemeinde 21002: 14.558 Einwohner (2026), Bezirk 30.082; die zehn Gemeinden
  des Bezirks ueber die Blaetter 21001 bis 21010.
- Stadtgemeinde, Formulare: "Baumitteilung" (Mitteilungspflichtiges Bauvorhaben, bewilligungsfrei) und
  "Bauvollendungsmeldung (Mitteilungspflichtiges Bauvorhaben) (zB.: Photovoltaikanlagen, ...)", dazu
  "Anzeige Ortsbildschutz/Ortsbildpflege". Keine Energie-Foerderformulare, nur Wirtschafts-/Vereinsfoerderung.
- Stadtgemeinde, Bauamt: zustaendig fuer Bauordnung, Bauberatung, Ortsbildschutz, Bebauungsplaene, e5.
- Stadtgemeinde, e5: Beitritt 2016, erstes Audit 2019; Vor-Ort-Energieberatung netEB, vom Land gefoerdert.
- Stadtgemeinde, KEM: KEM Tiebeltal und Wimitzerberge (Feldkirchen, Himmelberg, St. Urban, Steuerberg), Ziel
  Ausstieg aus Oel und Gas. KEM-Seite: Gemeindeaktion "Raus aus den fossilen Energietraegern" (bis 1.500 Euro)
  ist als BEENDET gekennzeichnet.
- Kaernten Netz, pv.htm: Anschlussantrag im Kundenportal, Netzberechnung, Netzzutrittsangebot, Einspeiseleistung
  mindestens in Hoehe des Strombezugsrechts, dynamische Leistungsregelung, Fertigstellungsmeldung durch
  konzessionierten Elektriker, Abnahmevertrag.
- Kaernten Netz, Einspeisekapazitaeten je Umspannwerk (Paragraf 20 ElWOG, Stand 30.07.2026): UW Feldkirchen
  2 MVA gebucht, 10 MVA verfuegbar (unverbindliche Momentaufnahme).
- Klima- und Energiefonds, Zwischenbericht solarFELDkirchen (27.03.2025): Biomasse-Heizwerk mit 7,5 MW
  Anschlussleistung, Netzbetreiber BC Regionalwaerme, Netzverdichtung und Ausbau geplant, restlicher Waermebedarf
  ueber Gasnetz und Oelheizungen, zweites Waermenetz der Diakonie Waiern. Regionalwaerme Gruppe fuehrt Feldkirchen
  als Heizwerk.
- Baurecht wie auf /photovoltaik-klagenfurt/: Mitteilungspflicht nach Paragraf 7 Abs. 1 lit. a Z 20 K-BO 1996
  (bauliche Anlagen, die erneuerbare Energie erzeugen oder elektrische Energie speichern; Vollendung binnen zwei
  Wochen schriftlich melden, bei Speichern Lage und technische Daten). Beleg: Formular des Magistrats Villach zur
  selben landesweiten Bestimmung (selbst abgerufen). RIS (Bot-Schutz) und ktn.gv.at waren nicht abrufbar, deshalb
  kein KAGIS-Hinweis auf dieser Seite.
- Ertrag: PVGIS 5.3 (EU-Kommission, JRC), SARAH3 2005 bis 2023, 46.729 N / 14.100 O (Koordinaten laut Stadtgemeinde),
  559 m, 1 kWp, 14 % Verluste, Horizont beruecksichtigt: Sued 30 Grad 1.247 kWh/kWp, Ost 25 Grad 996, West 25 Grad 1.001.
"""

from common import a, standort_link

ORT = {
    "key": "pv_feldkirchen",
    "name": "Feldkirchen in Kärnten",
    "kurz": "Feldkirchen",
    "area_name": "Bezirk Feldkirchen",
    "land": "ktn",
    "title": "Photovoltaik & Wärmepumpe Feldkirchen in Kärnten | EBZ",
    "description": ("Photovoltaik und Wärmepumpe in Feldkirchen in Kärnten: Fachbetrieb aus Villach, Beratung vor Ort, "
                    "Baumitteilung, Kärnten Netz und 3.000 € Landespauschale."),
    "h1": "Photovoltaik in Feldkirchen in Kärnten: PV-Anlage, Speicher und Wärmepumpe aus einer Hand",
    "lead": ("EBZ Energie ist ein Fachbetrieb aus Villach und plant Photovoltaik, Speicher und Wärmepumpen für Häuser "
             "und Betriebe in Feldkirchen in Kärnten und im ganzen Bezirk, von Himmelberg bis zum Ossiacher See. Für "
             "die Erstberatung kommen wir zu Ihnen, die Baumitteilung an die Stadtgemeinde und die Netzanmeldung bei "
             "Kärnten Netz bereiten wir vor. Gemeint ist die Bezirksstadt in Mittelkärnten, nicht Feldkirchen bei "
             "Graz oder Feldkirchen an der Donau."),
    "badges": [("10 Gemeinden", "im Bezirk Feldkirchen"),
               ("Kärnten Netz", "Netzanmeldung durch uns"),
               ("3.000 €", "Landespauschale Kärnten")],
    "hero_img": "/assets/img/ref-ossiachersee-1.jpg",
    "hero_alt": ("Einfamilienhaus am Ossiachersee mit Photovoltaik-Modulen auf dem Ziegeldach, Referenzprojekt von "
                 "EBZ Energie (Aufnahme nicht aus der Stadt Feldkirchen)"),
    "intro": {
        "h2": "Photovoltaik und Wärmepumpe in Feldkirchen: Bezirksstadt zwischen Klagenfurter Becken und Nockbergen",
        "paragraphs": [
            ("Feldkirchen in Kärnten ist die Hauptstadt des Bezirks Feldkirchen in Mittelkärnten, mit rund 14.600 "
             "Einwohnern in der Stadtgemeinde und rund 30.100 im Bezirk (Statistik Austria, 2026). Eine "
             "Photovoltaikanlage mit 10 kWp und Speicher kostet hier rund 15.000 bis 22.000 Euro vor Förderung*. Für "
             "den Standort Feldkirchen rechnet das Solarmodell PVGIS der EU-Kommission mit rund 1.250 kWh je kWp und "
             "Jahr auf einem Süddach mit 30 Grad Neigung und mit rund 1.000 kWh je kWp auf Ost- oder Westdächern*."),
            ("Die Stadt liegt am nördlichen Rand des Klagenfurter Beckens, laut Stadtgemeinde auf 550 bis 900 m "
             "Seehöhe, dahinter beginnen die Ausläufer der Nockberge. Für die Planung heißt das: Schneelast und "
             "Verschattung durch Hänge und Wald gehören in jeden Entwurf. Beides steckt im Projektbericht mit "
             "3D-Belegplan und Statikreport, den Sie vor dem Angebot bekommen. Das gilt für das Haus im Zentrum "
             "genauso wie in den Ortschaften Waiern, St. Ulrich, Glanhofen, St. Nikolai, St. Martin, Sittich, "
             "Klein St. Veit und Radweg."),
            ("Beim Heizen ist Feldkirchen im Umbruch. Ein Biomasse-Heizwerk versorgt einen Teil der Stadt mit "
             "Fernwärme, der übrige Wärmebedarf wird laut einem Bericht an den Klima- und Energiefonds noch über "
             "das Gasnetz und Ölheizungen gedeckt. Die Stadt ist seit 2016 e5-Gemeinde und Teil der Klima- und "
             "Energie-Modellregion Tiebeltal und Wimitzerberge, die den Ausstieg aus Öl und Gas zum Ziel hat. Wo "
             "keine Fernwärmeleitung liegt, ist die " + a("waermepumpe", "Wärmepumpe") + " mit Strom vom eigenen "
             "Dach die naheliegende Lösung."),
        ],
    },
    "lokal": {
        "h2": "Feldkirchen in Kärnten auf einen Blick: Behörde, Netz und Wärme",
        "intro": ("Diese Angaben brauchen wir für jede Anlage in Feldkirchen. Sie stammen von der Stadtgemeinde, von "
                  "Statistik Austria, von Kärnten Netz und vom Klima- und Energiefonds (Quellen am Seitenende)."),
        "rows": [
            ("Stadt und Bezirk",
             "Feldkirchen in Kärnten, Bezirkshauptstadt. Rund 14.600 Einwohner in der Stadtgemeinde, rund 30.100 im "
             "Bezirk mit seinen zehn Gemeinden (Statistik Austria, 2026)."),
            ("Lage und Höhe",
             "Nördlicher Rand des Klagenfurter Beckens, 77,49 km² Gemeindefläche. Seehöhe laut Stadtgemeinde 550 bis "
             "900 m, tiefster Punkt 510 m, höchster Punkt 1.069 m."),
            ("Sonnenertrag",
             "Laut PVGIS (EU-Kommission) rund 1.250 kWh je kWp und Jahr bei Südausrichtung und 30 Grad Neigung, rund "
             "1.000 kWh je kWp bei Ost oder West mit 25 Grad*. Modellwert für 559 m Seehöhe mit Horizont, ohne "
             "Verschattung durch Bäume oder Nachbargebäude."),
            ("Baubehörde",
             "Stadtgemeinde Feldkirchen in Kärnten, Bauamt, Hauptplatz 5. Für Photovoltaik gibt es die "
             "Online-Formulare Baumitteilung und Bauvollendungsmeldung für mitteilungspflichtige Vorhaben."),
            ("Stromnetz",
             "KNG-Kärnten Netz GmbH. Für das Umspannwerk Feldkirchen weist sie 10 MVA verfügbare und 2 MVA gebuchte "
             "Einspeisekapazität aus (Stand Juli 2026, unverbindliche Momentaufnahme)."),
            ("Fernwärme und Gas",
             "Biomasse-Heizwerk der Regionalwärme Gruppe mit 7,5 MW Anschlussleistung, Netzausbau laut Betreiber "
             "geplant. Dazu kommt das Wärmenetz der Diakonie Waiern. Der übrige Wärmebedarf läuft über "
             "Gasnetz und Ölheizungen (Bericht an den Klima- und Energiefonds, März 2025)."),
            ("Klima und Energie",
             "e5-Gemeinde seit 2016, erstes Audit 2019. Klima- und Energie-Modellregion Tiebeltal und Wimitzerberge "
             "mit Feldkirchen, Himmelberg, St. Urban und Steuerberg, dazu die Anpassungsregion KLAR! mit Steuerberg "
             "und St. Urban."),
            ("Nicht verwechseln",
             "Diese Seite gilt für Feldkirchen in Kärnten (PLZ 9560). Für Feldkirchen bei Graz ist "
             + standort_link("pv_graz", "unsere Seite für Graz und Umgebung") + " zuständig, Feldkirchen an der "
             "Donau liegt in Oberösterreich, dort prüfen wir Projekte auf Anfrage."),
        ],
    },
    "netz": {
        "h2": "Baumitteilung in Feldkirchen und Netzanschluss bei Kärnten Netz",
        "betreiber": "der Kärnten Netz GmbH",
        "paragraphs": [
            ("Nach der Kärntner Bauordnung (§ 7 Abs. 1 lit. a Z 20 K-BO 1996) sind bauliche Anlagen, die erneuerbare "
             "Energie erzeugen oder elektrische Energie speichern, mitteilungspflichtig. Für eine Photovoltaikanlage "
             "mit Speicher auf dem Hausdach heißt das in der Regel: Mitteilung statt Bauverfahren. Die Stadtgemeinde "
             "Feldkirchen führt dafür zwei Online-Formulare, die Baumitteilung für das bewilligungsfreie Vorhaben und "
             "die Bauvollendungsmeldung, die die Stadt ausdrücklich für Photovoltaikanlagen nennt. Die Vollendung ist "
             "binnen zwei Wochen zu melden, bei Speichern mit Lage und technischen Daten."),
            ("Zuständig ist das Bauamt im Rathaus am Hauptplatz 5, das auch Bauberatung, Ortsbildschutz und "
             "Bebauungspläne betreut. Flächenwidmung und Bebauungsplan gelten auch für mitteilungspflichtige Vorhaben. "
             "Ob für Ihr Haus zusätzlich eine Anzeige zur Ortsbildpflege nötig ist, für die es in Feldkirchen ein "
             "eigenes Formular gibt, klären wir vorab mit dem Bauamt."),
            ("Netzbetreiber ist die KNG-Kärnten Netz GmbH. Der Anschlussantrag läuft über ihr Kundenportal: Kärnten "
             "Netz ermittelt per Netzberechnung die maximal mögliche Einspeiseleistung an Ihrem Anschlusspunkt und "
             "schickt ein Netzzutrittsangebot. Laut Kärnten Netz wird in jedem Fall eine Einspeiseleistung mindestens "
             "in Höhe Ihres Strombezugsrechts gewährt. Reicht das für die gewünschte Modulleistung nicht, kann die "
             "Anlage mit dynamischer Leistungsregelung trotzdem in voller Größe gebaut werden."),
            ("Für das Umspannwerk Feldkirchen weist Kärnten Netz 10 MVA verfügbare Einspeisekapazität aus, an mehreren "
             "anderen Kärntner Umspannwerken steht dieser Wert bei 0 MVA. Das ist eine gute Ausgangslage, entscheidet "
             "aber nicht über Ihren einzelnen Hausanschluss: Maßgeblich bleibt die Netzberechnung für Ihren Zählpunkt. "
             "Bei Häusern und Höfen mit langer Zuleitung planen wir deshalb "
             + a("batteriespeicher", "Speicher") + " und Leistungsregelung von Anfang an mit."),
        ],
        "bullets": [
            "Baumitteilung an die Stadtgemeinde Feldkirchen, nach der Montage die Bauvollendungsmeldung",
            "Anschlussantrag im Kundenportal von Kärnten Netz, Netzzutrittsangebot mit Einspeiseleistung",
            "Fertigstellungsmeldung durch den konzessionierten Elektriker, Abnahmevertrag für den Überschussstrom",
            "Umspannwerk Feldkirchen: 10 MVA verfügbare Einspeisekapazität (Stand Juli 2026)",
        ],
        "img": "gen_detail",
        "alt": ("Fachkraft verschraubt eine Modulklemme auf der Aluminiumschiene einer Photovoltaik-Unterkonstruktion "
                "(Symbolbild)"),
    },
    "waermepumpe": {
        "h2": "Wärmepumpe in Feldkirchen: die Alternative zu Öl und Gas abseits der Fernwärme",
        "paragraphs": [
            ("Feldkirchen hat ein Biomasse-Fernwärmenetz: Das Heizwerk der Regionalwärme Gruppe hat laut einem "
             "Bericht an den Klima- und Energiefonds 7,5 MW Anschlussleistung, der Betreiber plant Netzverdichtung "
             "und weiteren Ausbau. Dazu kommt das Wärmenetz der Diakonie Waiern. Liegt die Leitung vor "
             "Ihrem Haus, lohnt der Vergleich, und wir sagen Ihnen offen, wenn der Anschluss die bessere Wahl ist."),
            ("Für alle anderen Häuser ist die Wärmepumpe der direkte Weg weg von Öl und Gas, und genau diese beiden "
             "Energieträger decken in Feldkirchen laut demselben Bericht noch den Wärmebedarf abseits der Fernwärme. "
             "Wegen der Höhenlage von 550 bis 900 m rechnen wir nicht mit Pauschalwerten: Grundlage ist die Heizlast "
             "Ihres Hauses und die Auslegungstemperatur an Ihrem Standort. Luft-Wasser-Geräte arbeiten bis minus "
             "20 Grad, entscheidend sind Dämmstandard und Vorlauftemperatur. Ob für das Außengerät eine Mitteilung "
             "an das Bauamt genügt, klären wir für Sie. Mehr dazu im Ratgeber "
             + a("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau") + "."),
            ("Am meisten bringt die Kombination mit Photovoltaik. Kärnten Netz empfiehlt selbst, große Verbraucher "
             "wie Wärmepumpe und E-Auto bei der Größe der PV-Anlage einzurechnen. Wir planen deshalb Dach, Speicher "
             "und Heizung in einem Zug, auf Wunsch mit " + a("ems", "Energiemanagement") + ", das die Wärmepumpe "
             "bevorzugt dann laufen lässt, wenn die Sonne scheint."),
        ],
        "bullets": [
            "Heizlast für Ihr Haus in Feldkirchen statt Pauschalgröße",
            "Ehrlicher Vergleich mit dem Fernwärmeanschluss, wenn eine Leitung in der Nähe liegt",
            "Photovoltaik, Speicher und Wärmepumpe aus einer Planung",
        ],
        "img": "waermepumpe",
        "alt": "Außeneinheit einer Luft-Wasser-Wärmepumpe mit zwei Ventilatoren vor einer Holzwand im Garten (Symbolbild)",
    },
    "foerderung_h2": "Förderung für Photovoltaik und Wärmepumpe in Feldkirchen in Kärnten",
    "foerderung_lokal": [
        ("Die Stadtgemeinde Feldkirchen weist derzeit kein eigenes Förderprogramm für Photovoltaik, Speicher oder "
         "Heizungstausch aus: Bei den Formularen und Förderungen der Stadt finden sich nur Wirtschafts- und "
         "Vereinsförderungen (abgerufen im Oktober 2026). Die frühere Gemeindeaktion „Raus aus den fossilen "
         "Energieträgern“ mit bis zu 1.500 Euro für den Ausstieg aus einer fossilen Heizung ist laut der Klima- und "
         "Energie-Modellregion Tiebeltal und Wimitzerberge beendet. Ob es eine Neuauflage gibt, fragen wir vor dem "
         "Angebot beim Stadtamt nach."),
        ("Kostenlos nutzen können Sie die Beratung in der Region: Die Modellregion veranstaltet gemeinsam mit der "
         "Stadtgemeinde Energiesprechtage, und die Energieberater aus dem Netzwerk Energieberatung Kärnten (netEB) "
         "kommen für einen vom Land Kärnten geförderten Vor-Ort-Energiecheck zu Ihnen nach Hause. Das ersetzt keine "
         "Anlagenplanung, ist aber ein guter erster Schritt vor einem Heizungstausch."),
    ],
    "referenzen": {
        "h2": "Referenzen in der Nähe von Feldkirchen: Ossiachersee, Villach, Krumpendorf",
        "intro": ("Aus der Stadt Feldkirchen selbst zeigen wir hier noch kein dokumentiertes Projekt. Die "
                  "nächstgelegenen Referenzen mit Zahlen liegen am Ossiachersee, in Villach und in Krumpendorf am "
                  "Wörthersee."),
        "slugs": ["projekt-pv-am-ossiachersee", "projekt-einfamilienhaus-villach",
                  "projekt-mehrparteienhaus-krumpendorf"],
    },
    "umgebung": ["Himmelberg", "Steuerberg", "St. Urban", "Glanegg", "Steindorf am Ossiacher See", "Ossiach",
                 "Gnesau", "Albeck", "Reichenau"],
    "links": [
        ("/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/", "10 kWp mit Speicher: Kosten"),
        ("/foerderung-pv-speicher-kaernten/", "Speicherförderung Kärnten"),
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau"),
        ("/energiegemeinschaft-kaernten/", "Energiegemeinschaft in Kärnten"),
    ],
    "faq": [
        ("Was kostet eine Photovoltaikanlage mit Speicher in Feldkirchen in Kärnten?",
         "Eine Komplettanlage mit rund 10 kWp und Speicher kostet in Feldkirchen typischerweise 15.000 bis 22.000 Euro "
         "vor Förderung, inklusive Montage, Baumitteilung an die Stadtgemeinde und Netzanmeldung bei Kärnten Netz "
         "(EBZ-Richtpreis, Stand Oktober 2026). Davon gehen die Landespauschale Kärnten von 3.000 Euro und der "
         "Investitionszuschuss des Bundes ab. Eine Finanzierung ab 147 Euro im Monat* ist möglich, die Anlage gehört "
         "Ihnen ab dem ersten Tag."),
        ("Wer ist in Feldkirchen der Stromnetzbetreiber und wie läuft die Anmeldung der PV-Anlage?",
         "Netzbetreiber in Feldkirchen in Kärnten ist die KNG-Kärnten Netz GmbH, die dort ein eigenes Umspannwerk "
         "betreibt. Der Anschlussantrag wird im Kundenportal gestellt. Kärnten Netz berechnet die mögliche "
         "Einspeiseleistung an Ihrem Anschlusspunkt und schickt ein Netzzutrittsangebot. Nach der Montage meldet der "
         "konzessionierte Elektriker die Anlage fertig, für den Überschussstrom brauchen Sie einen Abnahmevertrag. "
         "Wir bereiten Antrag und Unterlagen für Sie vor."),
        ("Brauche ich in Feldkirchen eine Baubewilligung für die Photovoltaikanlage?",
         "In der Regel nicht. Nach § 7 der Kärntner Bauordnung sind Anlagen, die erneuerbare Energie erzeugen oder "
         "Strom speichern, mitteilungspflichtig. Die Stadtgemeinde Feldkirchen stellt dafür das Online-Formular "
         "Baumitteilung bereit, nach der Montage folgt binnen zwei Wochen die Bauvollendungsmeldung. Zuständig ist "
         "das Bauamt am Hauptplatz 5, das auch den Ortsbildschutz betreut. Flächenwidmung und Bebauungsplan gelten "
         "trotzdem, besondere Lagen klären wir vorab mit dem Bauamt."),
        ("Wie viel Strom erzeugt eine PV-Anlage in Feldkirchen?",
         "Das Solarmodell PVGIS der EU-Kommission rechnet für Feldkirchen in Kärnten mit rund 1.250 kWh je kWp und "
         "Jahr auf einem Süddach mit 30 Grad Neigung und mit rund 1.000 kWh je kWp auf Ost- oder Westdächern. Wir "
         "planen vorsichtiger mit 1.000 bis 1.100 kWh je kWp, weil Hänge, Wald und Schnee den Ertrag drücken können. "
         "Unser Referenzprojekt am nahen Ossiachersee erzeugt mit 10 kWp in Ost-West-Ausrichtung rund 11.000 kWh im "
         "Jahr."),
        ("Wärmepumpe oder Fernwärme: Was passt in Feldkirchen besser?",
         "Das hängt von Ihrer Adresse ab. Feldkirchen hat ein Biomasse-Fernwärmenetz der Regionalwärme Gruppe, das "
         "laut Betreiber verdichtet und ausgebaut wird, dazu das Wärmenetz der Diakonie Waiern. Liegt eine Leitung "
         "vor Ihrem Haus, ist der Anschluss oft eine gute Lösung. Abseits der Netze ersetzt die Wärmepumpe Öl oder "
         "Gas, am günstigsten zusammen mit einer Photovoltaikanlage. Wir vergleichen beide Wege mit Ihnen."),
        ("Funktioniert eine Luft-Wasser-Wärmepumpe in der Höhenlage von Feldkirchen?",
         "Ja. Luft-Wasser-Wärmepumpen arbeiten bis minus 20 Grad Außentemperatur. Entscheidend ist die richtige "
         "Auslegung: In Feldkirchen, das laut Stadtgemeinde zwischen 550 und 900 m Seehöhe liegt, berechnen wir die "
         "Heizlast für Ihr Haus und den konkreten Standort statt mit Pauschalwerten zu arbeiten. In älteren Häusern "
         "prüfen wir zuerst Dämmung und Vorlauftemperatur und sagen offen, wenn vor der Wärmepumpe eine Sanierung "
         "sinnvoll ist."),
        ("Gibt es in Feldkirchen eine Gemeindeförderung für Photovoltaik oder Wärmepumpe?",
         "Derzeit weist die Stadtgemeinde Feldkirchen kein eigenes Programm für Photovoltaik, Speicher oder "
         "Heizungstausch aus (Stand Oktober 2026). Eine frühere Gemeindeaktion für den Ausstieg aus fossilen "
         "Heizungen mit bis zu 1.500 Euro ist beendet. Für Photovoltaik gelten die Förderungen von Land Kärnten und "
         "Bund. Bei der Wärmepumpe ist die Bundesförderung derzeit ausgeschöpft; was das Land Kärnten für den "
         "Heizungstausch aktuell zahlt, prüfen wir vor jedem Angebot."),
        ("Ist hier Feldkirchen in Kärnten oder Feldkirchen bei Graz gemeint, und kommen Sie in den ganzen Bezirk?",
         "Gemeint ist Feldkirchen in Kärnten, die Bezirkshauptstadt mit der Postleitzahl 9560, nicht Feldkirchen bei "
         "Graz in der Steiermark und nicht Feldkirchen an der Donau in Oberösterreich. Wir beraten und montieren im "
         "ganzen Bezirk Feldkirchen: in Himmelberg, Steuerberg, St. Urban, Glanegg, Steindorf am Ossiacher See, "
         "Ossiach, Gnesau, Albeck und Reichenau. Firmensitz ist Villach, für die Erstberatung kommen wir zu Ihnen."),
    ],
    "quellen": [
        ("Stadtgemeinde Feldkirchen in Kärnten: Daten und Fakten (Lage, Seehöhe, Fläche, Ortschaften)",
         "https://www.feldkirchen.at/tourismus/service/daten-und-fakten"),
        ("Statistik Austria: Ein Blick auf die Gemeinde Feldkirchen in Kärnten (Bevölkerung Gemeinde und Bezirk 2026)",
         "https://www.statistik.at/blickgem/G0201/g21002.pdf"),
        ("Stadtgemeinde Feldkirchen: Formulare (Baumitteilung, Bauvollendungsmeldung, Ortsbildpflege)",
         "https://www.feldkirchen.at/sites/formulare"),
        ("Stadtgemeinde Feldkirchen: Bauamt, Tiefbau, Umweltschutz und Landwirtschaft",
         "https://www.feldkirchen.at/stadtamt-und-services/abteilungen/bauamt-tiefbau-umweltschutz-und-landwirtschaft"),
        ("Magistrat Villach: Formular Mitteilung nach § 7 Abs. 1 lit. a Z 20 K-BO 1996 (Wortlaut der landesweiten "
         "Bestimmung)",
         "https://villach.at/getmedia/fe3178f4-230a-4056-871d-d9412d2329ff/Mitteilung_P7_KBO1996.pdf.aspx"),
        ("EU-Kommission, PVGIS 5.3: Ertragsberechnung für Feldkirchen in Kärnten (1 kWp, Süd, 30 Grad)",
         "https://re.jrc.ec.europa.eu/api/v5_3/PVcalc?lat=46.729&lon=14.100&peakpower=1&loss=14&angle=30&aspect=0"),
        ("Kärnten Netz: Photovoltaik-Netzanschluss (Antrag, Einspeiseleistung, Leistungsregelung)",
         "https://kaerntennetz.at/pv.htm"),
        ("Kärnten Netz: Verfügbare Einspeisekapazitäten je Umspannwerk gemäß § 20 ElWOG (Stand Juli 2026)",
         "https://kaerntennetz.at/dokumente/Strom/Veroeffentlichung_der_verfuegbaren_Kapazitaeten_gemaess_20_ElWOG.pdf"),
        ("Klima- und Energiefonds: Zwischenbericht solarFELDkirchen (Fernwärme, Heizwerk, Gasnetz), März 2025",
         "https://klimafonds.gv.at/wp-content/uploads/2025/04/KC397616_Publizierbarer-Zwischenbericht-Solar_Feldkirchen_260325C.pdf"),
        ("Regionalwärme Gruppe: Heizwerke (Standort Feldkirchen)",
         "https://regionalwaerme.com/leistungen/heizwerke/"),
        ("Stadtgemeinde Feldkirchen: e5-Programm und Vor-Ort-Energieberatung (netEB)",
         "https://www.feldkirchen.at/stadt-und-politik/umwelt/e5-energieeffiziente-gemeinde"),
        ("Stadtgemeinde Feldkirchen: Klima- und Energie-Modellregion Tiebeltal und Wimitzerberge",
         "https://www.feldkirchen.at/stadt-und-politik/umwelt/kem-klima-und-energie-modellregion"),
        ("KEM Tiebeltal und Wimitzerberge: Gemeindeaktion „Raus aus den fossilen Energieträgern“ (beendet)",
         "https://kem.fenergiereich.at/kem/news/raus-aus-den-fossilen-energietraegern"),
    ],
    "notizen": (
        "Faktenfragen an den Kunden: (1) Gibt es ein dokumentiertes EBZ-Projekt in der Stadt oder im Bezirk "
        "Feldkirchen (Himmelberg, Steindorf, Ossiach)? Dann als Referenz aufnehmen. In welcher Gemeinde liegt das "
        "Ossiachersee-Projekt (Bezirk Feldkirchen oder Villach-Land)? (2) Montiert EBZ in Feldkirchen auch "
        "Wärmepumpen in Lagen über 800 m und in Reichenau/Turracher Höhe? (3) Fernwärme: Soll EBZ aktiv zum "
        "Fernwärmeanschluss raten, wenn eine Leitung vorhanden ist (so steht es jetzt im Text)? "
        "Unsicherheiten: Netzbetreiber über das KNG-Umspannwerk Feldkirchen belegt, kein Hinweis auf ein Kleinnetz, "
        "aber keine gemeindegenaue Netzgebietsliste gefunden. RIS (Bot-Sperre) und ktn.gv.at waren nicht "
        "erreichbar: Baurecht über das Formular des Magistrats Villach und die Formulare der Stadtgemeinde belegt, "
        "KAGIS-Solarkataster weggelassen. Landesförderung Wärmepumpe Kärnten laut Faktenliste ungeklärt, deshalb "
        "ohne Satz und Betrag. Einspeisekapazität am Umspannwerk ändert sich: bei jeder "
        "Aktualisierung der KNG-Veröffentlichung nachziehen. Gemeindeförderung: Stadtamt (umwelt@feldkirchen.at) nach "
        "Neuauflage der Heizungsaktion fragen. Vor-Ort-Energiecheck: Stadt nennt 200 Euro Landesförderung, Aktualität "
        "unklar, deshalb ohne Betrag."
    ),
}
