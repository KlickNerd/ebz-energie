"""Ortsseite Spittal an der Drau (/photovoltaik-spittal/), Inhalt fuer build/pages/standorte.py.

Briefing: build/seo/standort_spittal.json (DataForSEO, Oesterreich/Deutsch, 10.10.2026). Kein Keyword mit Ort
hat messbares Volumen ("photovoltaik spittal an der drau", "pv anlage spittal", "waermepumpe spittal" usw. = 0);
"fernwaerme spittal" 10, "installateur spittal an der drau" 30, "elektriker spittal an der drau" 30. Die Seite
ist deshalb auf Longtail, lokale Fakten und die Fernwaerme-Frage ausgelegt, nicht auf ein Volumen-Keyword.

Lokale Fakten, alle am 10.10.2026 selbst abgerufen:
- Stadt: 560 m Seehoehe, 48,57 km2, 7 Katastralgemeinden, 27 Ortschaften, groesste Gemeinde im Bezirk, "Zentrum des
  zweitgroessten Bezirks in Oesterreich" (spittal-drau.at/buergerservice/zahlen-und-fakten).
- Einwohner 2026: Stadt 15.263, Bezirk 75.119 (Statistik Austria, Ein Blick auf die Gemeinde, G2.1).
- Baurecht: Stadtgemeinde listet "mitteilungspflichtige Bauvorhaben (§ 7 K-BO)", schriftliche Bekanntgabe vor der
  Ausfuehrung; Abteilung Stadtplanung im Rathaus, Burgplatz 5. Wortlaut § 7 Abs. 1 lit. a Z 20 K-BO 1996 (bauliche
  Anlagen, die erneuerbare Energie erzeugen oder elektrische Energie speichern) aus dem Mitteilungsformular der
  Stadt Villach (Stand 09/2024). ACHTUNG: Die Spittaler Seite nennt noch die alte Grenze "PV bis zu 40 m2";
  RIS war am 10.10.2026 nicht erreichbar (HTTP 503). Deshalb im Text "in der Regel" und keine Flaechengrenze.
  Konsistent mit build/pages/standort_klagenfurt.py (gleiche Bestimmung, Fassung LGBl. Nr. 11/2026 laut
  Gesetzestext-Wiedergabe forum-media.at; Vollendungsmeldung binnen zwei Wochen laut Villacher Formular).
- Netz: Kaernten Netz fuehrt einen eigenen "Stoerbezirk Spittal an der Drau" (kaerntennetz.at/stoerungsdienst.htm);
  Ablauf PV-Anschluss und Rechenbeispiel 10 kWp / 3,5 kW Strombezugsrecht / 6 kW Einspeisung von
  kaerntennetz.at/pv.htm. Ein lokaler Netzbetreiber im Bezirk Spittal war nicht belegbar (weder bestaetigt noch
  ausgeschlossen), daher der Hinweis auf die Stromrechnung.
- Fernwaerme: Kelag Energie & Waerme, rund 33 Mio. kWh pro Jahr, rund 98 % Biomasse, Abwaerme der Klaeranlage rund
  2 Mio. kWh (Bedarf von rund 400 Wohnungen), Pressemitteilung 30.01.2024 (presse.kelag.at); Netzverdichtung
  Spittal 2023 bis 2024 (kew.at/forderungen.htm).
- Stadt und Energie: Pionier-Kleinstadt "Klimaneutrale Stadt", Ziel 2040, e5-Gemeinde, KEM Millstaetter See
  (Spittal, Seeboden, Millstatt, Lendorf, Baldramsdorf); fuenf staedtische PV-Anlagen mit 761,79 kWp, ueber
  1,4 Mio. kWh Eigenstrom und rund 220.000 Euro Ersparnis im Jahr 2025, zwei eigene Energiegemeinschaften
  (spittal-drau.at, Meldung vom 14.05.2026); Photovoltaik-Potenzialkataster (solare-stadt.de/nockregion).
- Foerderung: Die Foerderseite der Stadt nennt kein Programm fuer PV, Speicher oder Heizung; "Oelkesselfreie
  Gemeinde" laut KEM abgeschlossen; KEM-Beratung kostenlos; Kelag-Waermepumpen-Praemie 1.200 Euro (kelag.at).
- Gemeindenamen des Bezirks gegen die Gemeindeliste geprueft (Ferndorf gehoert NICHT zum Bezirk Spittal).

Waermepumpen-Zahlen nur aus build/pages/waermepumpe.py. Referenzen: keine im Bezirk Spittal, daher Ossiacher See
und Villach, ohne Ortsbehauptung.
"""

from common import a

_EXT = 'rel="nofollow noopener" target="_blank"'

ORT = {
    "key": "pv_spittal",
    "name": "Spittal an der Drau",
    "kurz": "Spittal",
    "area_name": "Bezirk Spittal an der Drau",
    "land": "ktn",
    "title": "Photovoltaik & Wärmepumpe Spittal an der Drau | EBZ",
    "description": ("Photovoltaik und Wärmepumpe in Spittal an der Drau: Fachbetrieb aus Villach, Beratung vor Ort, "
                    "Netzanmeldung bei Kärnten Netz, 3.000 € Landespauschale."),
    "h1": "Photovoltaik in Spittal an der Drau: PV-Anlage, Speicher und Wärmepumpe vom Fachbetrieb aus Villach",
    "lead": ("EBZ Energie ist ein Fachbetrieb aus Villach und plant Photovoltaik, Speicher und Wärmepumpe für Häuser in "
             "Spittal an der Drau und im Umland. Für die Erstberatung kommen wir zu Ihnen, sehen uns Dach, "
             "Zählerschrank und Heizraum an und klären auch, ob an Ihrer Adresse die Spittaler Fernwärme eine "
             "Alternative ist. Die Mitteilung an die Stadtgemeinde und den Anschlussantrag bei Kärnten Netz "
             "bereiten wir vor."),
    "badges": [("Vor Ort", "Beratung bei Ihnen in Spittal"),
               ("Kärnten Netz", "Anschlussantrag inklusive"),
               ("ab 147 €*", "im Monat, inklusive Speicher")],
    "hero_img": "gen_eigenheim",
    "hero_alt": ("Einfamilienhaus mit Photovoltaikanlage auf dem Satteldach vor einer Bergkulisse, Symbolbild für "
                 "Eigenheime im Raum Spittal an der Drau"),
    "intro": {
        "h2": "Warum Photovoltaik und Wärmepumpe in Spittal an der Drau zusammengehören",
        "paragraphs": [
            ("Spittal an der Drau liegt auf 560 Metern Seehöhe im Kärntner Oberland und ist mit 15.263 Einwohnern "
             "die größte Gemeinde des Bezirks. Zur Stadt gehören 27 Ortschaften, vom dicht bebauten Zentrum bis "
             "nach Molzbichl, Rothenthurn, Olsach und Großegg. Entsprechend unterschiedlich sind die Dächer: "
             "Stadthaus, Siedlungshaus, Bauernhof. In Kärnten liefert eine PV-Anlage als Richtwert rund 1.000 bis "
             "1.100 kWh je kWp und Jahr*, eine Anlage mit 10 kWp also rund 10.000 bis 11.000 kWh. Was Ihr Dach "
             "tatsächlich bringt, hängt von Ausrichtung, Neigung und Verschattung ab. Genau das rechnen wir im "
             "Projektbericht mit 3D-Belegplan und Statikreport."),
            ("Die Stadt geht selbst voran. Spittal ist Pionier-Kleinstadt der Mission „Klimaneutrale Stadt“ und will "
             "bis 2040 klimaneutral sein. Fünf städtische PV-Anlagen mit zusammen 761,79 kWp laufen bereits, unter "
             "anderem auf der Drautal Perle, der Eissportarena und dem Bildungszentrum Ost. Zusammen mit dem "
             "Trinkwasserkraftwerk am Gmeineck hat die Stadt 2025 über 1,4 Millionen kWh Strom selbst erzeugt und "
             "nach eigenen Angaben rund 220.000 Euro eingespart. Zwei eigene Energiegemeinschaften verteilen den "
             "Strom auf die städtischen Betriebe. Dasselbe Prinzip funktioniert im Kleinen: Strom vom eigenen Dach "
             "selbst nutzen, speichern und den Rest in einer "
             + a("eg_privat", "Energiegemeinschaft") + " teilen."),
            ("Bei der Wärme ist Spittal ein Sonderfall, den man kennen muss. Im Stadtgebiet betreibt die Kelag "
             "Energie &amp; Wärme ein Fernwärmenetz, das laut Kelag zu rund 98 Prozent mit Biomasse gespeist wird. "
             "Wo eine Leitung vor dem Haus liegt, ist der Anschluss oft die einfachste Lösung. Wo keine liegt, also "
             "in vielen Ortschaften und in den Nachbargemeinden, ist die "
             + a("waermepumpe", "Wärmepumpe") + " der naheliegende Ersatz für Öl- und Stromheizung. "
             "Mit Photovoltaik am Dach erzeugen Sie einen Teil ihres Stroms selbst."),
        ],
    },
    "lokal": {
        "h2": "Spittal an der Drau im Überblick: Behörde, Stromnetz, Fernwärme, Solarkataster",
        "intro": ("Die Angaben stammen von der Stadtgemeinde, Statistik Austria, Kärnten Netz, der Kelag Energie &amp; "
                  "Wärme und der Klima- und Energie-Modellregion Millstätter See. Die Links stehen am Ende der Seite."),
        "rows": [
            ("Stadt und Bezirk",
             "Stadtgemeinde Spittal an der Drau, Bezirkshauptstadt im Kärntner Oberland. 15.263 Einwohner in der "
             "Stadt, 75.119 im Bezirk Spittal an der Drau (Statistik Austria, 2026)."),
            ("Lage",
             "560 m Seehöhe, 48,57 km² Gemeindefläche, 7 Katastralgemeinden und 27 Ortschaften, darunter Molzbichl, "
             "Rothenthurn, Olsach, Edling und Sankt Peter."),
            ("Baubehörde",
             "Stadtgemeinde Spittal an der Drau, Rathaus, Burgplatz 5. Photovoltaik fällt in Kärnten in der Regel "
             "unter die mitteilungspflichtigen Vorhaben nach § 7 der Kärntner Bauordnung: schriftliche Mitteilung "
             "vor Beginn der Ausführung, kein Bauverfahren."),
            ("Stromnetz",
             "Kärnten Netz GmbH mit eigenem Störbezirk Spittal an der Drau. Der Anschlussantrag für die PV-Anlage "
             "läuft über das Kundenportal von Kärnten Netz."),
            ("Fernwärme",
             "Netz der Kelag Energie &amp; Wärme: rund 33 Millionen kWh Wärme im Jahr, rund 98 % aus Biomasse, dazu "
             "Abwärme aus der Kläranlage des Wasserverbands Millstätter See (Kelag, Jänner 2024)."),
            ("Solarkataster",
             "Photovoltaik-Potenzialkataster der Stadtgemeinde: Adresse eingeben, Gebäude anklicken, Eignung des "
             "Dachs ablesen. Abrufbar über das "
             f'<a href="https://solare-stadt.de/nockregion/index" {_EXT}>Solarpotenzial der Nockregion</a>. '
             "Eine erste Orientierung, kein Ersatz für die Planung am Dach."),
            ("Klima und Energie",
             "e5-Gemeinde und Teil der Klima- und Energie-Modellregion Millstätter See, gemeinsam mit Seeboden am "
             "Millstätter See, Millstatt am See, Lendorf und Baldramsdorf. Ziel der Stadt: klimaneutral bis 2040."),
            ("Städtische Anlagen",
             "Fünf PV-Anlagen der Stadt mit zusammen 761,79 kWp und das Trinkwasserkraftwerk am Gmeineck mit 215 kW "
             "(Stadtgemeinde, Mai 2026)."),
        ],
    },
    "netz": {
        "h2": "Genehmigung und Netzanschluss in Spittal: Mitteilung an die Stadtgemeinde, Antrag bei Kärnten Netz",
        "betreiber": "der Kärnten Netz GmbH",
        "paragraphs": [
            ("Für eine Photovoltaikanlage am Dach brauchen Sie in Spittal in der Regel keine Baubewilligung. Die "
             "Kärntner Bauordnung führt bauliche Anlagen, die erneuerbare Energie erzeugen oder Strom speichern, "
             "unter den mitteilungspflichtigen Vorhaben (§ 7 K-BO 1996). Das Vorhaben wird der Baubehörde vor "
             "Beginn der Ausführung schriftlich bekannt gegeben, in Spittal ist das die Stadtgemeinde im Rathaus am "
             "Burgplatz 5. Nach der Montage ist die Vollendung binnen zwei Wochen zu melden, bei einem Speicher samt "
             "Lage und technischen Daten. Flächenwidmungsplan und Bebauungsplan gelten trotzdem; Auskunft dazu gibt "
             "die Abteilung Stadtplanung. Wir bereiten die Mitteilung mit Beschreibung und Lageskizze vor und klären Sonderfälle "
             "vorab mit der Behörde."),
            ("Netzbetreiber in Spittal ist die Kärnten Netz GmbH. Der Anschlussantrag wird im Kundenportal gestellt, "
             "die Netzberechnung läuft dabei automatisch, das Ergebnis kommt als Netzzutrittsangebot. Kärnten Netz "
             "sichert mindestens eine Einspeiseleistung in Höhe Ihres Strombezugsrechts zu. Ein Beispiel des "
             "Netzbetreibers: Bei 3,5 kW Bezugsrecht und 6 kW möglicher Einspeisung dürfen Sie trotzdem 10 kWp "
             "bauen, am Anschlusspunkt wird die Einspeisung auf 6 kW begrenzt. Mit "
             + a("batteriespeicher", "Speicher") + " und " + a("ems", "Energiemanagement")
             + " bleibt der Überschuss im Haus, statt abgeregelt zu werden."),
            ("Nach der Montage meldet eine konzessionierte Elektrofachkraft die Anlage im Portal fertig, für den "
             "eingespeisten Strom schließen Sie einen Abnahmevertrag mit einem Lieferanten Ihrer Wahl. Liegt Ihr "
             "Haus in einer anderen Gemeinde des Bezirks, sehen wir zuerst auf Ihre Stromrechnung: Dort steht, "
             "welcher Netzbetreiber für Ihren Zählpunkt zuständig ist."),
        ],
        "bullets": [
            "Schriftliche Mitteilung an die Stadtgemeinde Spittal vor Baubeginn (§ 7 K-BO)",
            "Anschlussantrag im Kundenportal von Kärnten Netz, Antwort als Netzzutrittsangebot",
            "Fertigstellungsmeldung durch eine konzessionierte Elektrofachkraft",
            "Bei begrenzter Einspeisung: Speicher und Steuerung statt kleinerer Anlage",
        ],
        "img": "gen_detail",
        "alt": ("Montage einer Photovoltaikanlage: Ein Modul wird mit dem Akkuschrauber auf der Aluminium-Unterkonstruktion "
                "befestigt, Symbolbild"),
    },
    "waermepumpe": {
        "h2": "Wärmepumpe in Spittal: zuerst die Fernwärme prüfen, dann mit Sonnenstrom heizen",
        "paragraphs": [
            ("Ehrliche Beratung beginnt in Spittal mit einer Frage: Liegt Fernwärme vor dem Haus? Die Kelag Energie "
             "&amp; Wärme betreibt das Netz seit 2013/2014 und bezeichnet das Spittaler Biomassesystem als eines der "
             "größten in Kärnten. Rund 33 Millionen kWh Wärme gehen pro Jahr an die Kunden, dazu kommt Abwärme aus der "
             "Kläranlage: rund 2 Millionen kWh und damit der Bedarf von etwa 400 Wohnungen. Das Netz wurde 2023 und "
             "2024 verdichtet. Ist ein Anschluss an Ihrer Adresse möglich, sagen wir Ihnen das offen."),
            ("Außerhalb des Netzes ist die Luft-Wasser-Wärmepumpe meist die naheliegende Lösung. Sie kostet im "
             "Einfamilienhaus rund 12.000 bis 22.000 Euro vor Förderung*, im Altbau mit Anpassungen 15.000 bis "
             "28.000 Euro*, die Montage dauert 2 bis 4 Tage. Bis 55 Grad Vorlauftemperatur arbeitet sie effizient, "
             "große alte Heizkörper reichen oft aus. Die Klima- und Energie-Modellregion Millstätter See empfiehlt "
             "in ihrem Programm, zuerst die Gebäudehülle zu verbessern und die Heizung danach auf den geringeren "
             "Bedarf auszulegen. So planen wir auch: erst Heizlast, dann Gerät."),
            ("Mit Photovoltaik wird die Rechnung besser. Ein gut gedämmtes Haus mit 12.000 kWh Wärmebedarf braucht "
             "bei Jahresarbeitszahl 4 rund 3.000 kWh Strom im Jahr*. Einen Teil davon liefert das eigene Dach, vor "
             "allem im Frühjahr und Herbst und für das Warmwasser im Sommer. Im Hochwinter kommt der Großteil aus "
             "dem Netz, das verschweigen wir nicht. Wer bei der Kelag Strom bezieht, bekommt für eine neue "
             "Wärmepumpe mit Internetanbindung zusätzlich eine Prämie von 1.200 Euro, verteilt über zwei Jahre als "
             "Gutschrift auf der Stromrechnung."),
        ],
        "bullets": [
            "Fernwärme-Anschluss an Ihrer Adresse möglich? Das klären wir zuerst",
            "Luft-Wasser-Wärmepumpe: 12.000 bis 22.000 € vor Förderung*, Montage in 2 bis 4 Tagen",
            "Kelag-Prämie: 1.200 € für Kelag-Stromkunden in Kärnten, Gutschrift über zwei Jahre",
            a("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau: was vorher zu prüfen ist"),
        ],
        "img": "waermepumpe",
        "alt": ("Außeneinheit einer Luft-Wasser-Wärmepumpe im Garten eines Wohnhauses, Symbolbild für den "
                "Heizungstausch in Spittal an der Drau"),
    },
    "foerderung_h2": "Förderung für Photovoltaik und Wärmepumpe in Spittal an der Drau",
    "foerderung_lokal": [
        ("Die Stadtgemeinde Spittal an der Drau weist auf ihrer Förderseite derzeit kein eigenes Programm für "
         "Photovoltaik, Stromspeicher oder Heizungstausch aus (Stand Oktober 2026). Die Aktion „Ölkesselfreie "
         "Gemeinde“, bei der Gemeinden der Region den Umstieg zusätzlich unterstützt haben, ist laut KEM Millstätter "
         "See abgeschlossen. Ob sich daran etwas geändert hat, prüfen wir vor jedem Angebot."),
        ("Beratung gibt es am Ort trotzdem: Die KEM Millstätter See berät Private, Betriebe und Vereine kostenlos "
         "und verweist auf die vom Land Kärnten geförderte Energieberatung mit einem Termin im Haus von bis zu zwei "
         "Stunden. Für Kelag-Stromkunden kommt bei der Wärmepumpe die Prämie des Energieversorgers dazu."),
    ],
    "referenzen": {
        "h2": "Referenzen aus Kärnten: Ossiacher See und Villach",
        "intro": ("Aus dem Bezirk Spittal zeigen wir hier noch kein dokumentiertes Projekt, deshalb nennen wir auch "
                  "keines. Diese drei Anlagen stehen am Ossiacher See und in Villach und zeigen, was 10 bis 13 kWp "
                  "mit Speicher in Kärnten leisten."),
        "slugs": ["projekt-pv-am-ossiachersee", "projekt-einfamilienhaus-villach", "projekt-pv-anlage-hotel-villach"],
    },
    "umgebung": ["Seeboden am Millstätter See", "Millstatt am See", "Lendorf", "Baldramsdorf", "Lurnfeld",
                 "Mühldorf", "Sachsenburg", "Radenthein", "Gmünd in Kärnten", "Trebesing", "Obervellach",
                 "Greifenburg"],
    "links": [
        ("/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/", "PV-Komplettanlage 10 kWp mit Speicher: Kosten"),
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau"),
        ("/energiegemeinschaft-kaernten/", "Energiegemeinschaft in Kärnten"),
    ],
    "faq": [
        ("Was kostet eine PV-Anlage mit Speicher in Spittal an der Drau?",
         "Eine Komplettanlage mit rund 10 kWp und Speicher kostet typischerweise rund 15.000 bis 22.000 Euro vor "
         "Förderung, inklusive Montage, Mitteilung an die Stadtgemeinde Spittal und Anschlussantrag bei Kärnten "
         "Netz. Davon gehen die Landespauschale Kärnten von 3.000 Euro und der Investitionszuschuss des Bundes ab. "
         "Wer nicht alles auf einmal zahlen will, finanziert ab 147 Euro im Monat*. Den genauen Preis nennen wir "
         "nach dem Termin bei Ihnen als Fixangebot."),
        ("Brauche ich in Spittal eine Baubewilligung für die Photovoltaikanlage?",
         "In der Regel nein. Anlagen, die erneuerbare Energie erzeugen oder Strom speichern, zählen in Kärnten zu "
         "den mitteilungspflichtigen Vorhaben nach § 7 der Kärntner Bauordnung. Die Mitteilung geht vor Beginn der "
         "Ausführung schriftlich an die Stadtgemeinde Spittal an der Drau, Burgplatz 5. Flächenwidmungs- und "
         "Bebauungsplan müssen trotzdem eingehalten werden. Wir bereiten die Mitteilung vor und klären Sonderfälle "
         "vorab mit der Baubehörde."),
        ("Wer ist in Spittal der Netzbetreiber und wie läuft die Anmeldung der PV-Anlage?",
         "Zuständig ist die Kärnten Netz GmbH, die für die Region einen eigenen Störbezirk Spittal an der Drau führt. "
         "Der Anschlussantrag wird im Kundenportal gestellt, die Netzberechnung erfolgt automatisch, das Ergebnis "
         "kommt als Netzzutrittsangebot. Nach der Montage meldet eine konzessionierte Elektrofachkraft die Anlage "
         "fertig. Wir stellen den Antrag in Ihrem Namen und planen Speicher und Steuerung passend zur zugesagten "
         "Einspeiseleistung."),
        ("Wie viel Strom erzeugt eine Photovoltaikanlage in Spittal an der Drau?",
         "Als Richtwert gelten in Kärnten rund 1.000 bis 1.100 kWh je kWp und Jahr, bei 10 kWp also rund 10.000 bis "
         "11.000 kWh. Eine erste Einschätzung für Ihr Gebäude gibt der Photovoltaik-Potenzialkataster der "
         "Stadtgemeinde Spittal: Adresse eingeben, Dach anklicken. Verbindlich wird es mit unserem Projektbericht "
         "mit 3D-Belegplan und Statikreport, der Ausrichtung, Neigung und Verschattung Ihres Dachs berücksichtigt."),
        ("Fernwärme oder Wärmepumpe: Was passt in Spittal besser?",
         "Das hängt von der Adresse ab. Im Stadtgebiet betreibt die Kelag Energie & Wärme ein Fernwärmenetz mit rund "
         "98 Prozent Biomasse; liegt eine Leitung vor dem Haus, ist der Anschluss oft die einfachste Lösung. In "
         "Ortschaften ohne Fernwärme und in den Nachbargemeinden ist die Wärmepumpe meist die bessere Wahl, vor "
         "allem zusammen mit Photovoltaik. Wir prüfen beides und sagen Ihnen offen, was sich für Ihr Haus rechnet."),
        ("Was kostet eine Wärmepumpe in Spittal und welche Förderung gibt es?",
         "Eine Luft-Wasser-Wärmepumpe kostet im Einfamilienhaus rund 12.000 bis 22.000 Euro vor Förderung, im Altbau "
         "mit Anpassungen 15.000 bis 28.000 Euro. Die Bundesförderung ist derzeit ausgeschöpft; den aktuellen Stand "
         "der Landesförderung Kärnten prüfen wir vor dem Angebot. Die Stadtgemeinde Spittal weist kein eigenes "
         "Programm aus. "
         "Kelag-Stromkunden erhalten für eine Wärmepumpe mit Internetanbindung eine Prämie von 1.200 Euro. Was "
         "aktuell beantragbar ist, zeigt unser Förderrechner."),
        ("Gibt es in Spittal an der Drau eine Gemeindeförderung für Photovoltaik?",
         "Derzeit nicht: Auf der Förderseite der Stadtgemeinde Spittal an der Drau ist kein Programm für "
         "Photovoltaik oder Stromspeicher angeführt (Stand Oktober 2026). Es gelten die Landespauschale Kärnten von "
         "3.000 Euro für PV ab 5 kWp mit Speicher ab 5 kWh und der Zuschuss des Bundes. Die Klima- und "
         "Energie-Modellregion Millstätter See berät Private kostenlos. Wir prüfen die Förderlage vor jedem Angebot."),
        ("Kommt EBZ Energie auch nach Seeboden, Millstatt oder ins Lieser- und Mölltal?",
         "Ja. Unser Firmensitz ist die Triglavstraße 15 in Villach, ein Büro in Spittal haben wir nicht. Für die "
         "Erstberatung kommen wir zu Ihnen, ob in Spittal, Seeboden am Millstätter See, Millstatt am See, Lendorf, "
         "Gmünd in Kärnten oder Obervellach. Photovoltaik und Wärmepumpe planen wir aus einer Hand, die Montage "
         "übernehmen zertifizierte Fachkräfte, und Sie haben einen festen Ansprechpartner von der Planung bis zur "
         "Übergabe."),
    ],
    "quellen": [
        ("Stadtgemeinde Spittal an der Drau: Zahlen und Fakten",
         "https://www.spittal-drau.at/buergerservice/zahlen-und-fakten"),
        ("Statistik Austria: Ein Blick auf die Gemeinde Spittal an der Drau, Bevölkerungsentwicklung",
         "https://www.statistik.at/blickgem/G0201/g20635.pdf"),
        ("Stadtgemeinde Spittal an der Drau: mitteilungspflichtige Bauvorhaben (§ 7 K-BO)",
         "https://www.spittal-drau.at/buergerservice/bauen/bauverfahren/bewilligungsfreien-aber-mitteilungspflichtigen-7k-bo"),
        ("Stadt Villach: Mitteilungsformular nach § 7 Abs. 1 lit. a Z 20 K-BO 1996 (Wortlaut der Kärntner Regelung)",
         "https://villach.at/getmedia/fe3178f4-230a-4056-871d-d9412d2329ff/Mitteilung_P7_KBO1996.pdf.aspx"),
        ("Kärnten Netz: PV-Anlage anschließen", "https://kaerntennetz.at/pv.htm"),
        ("Kärnten Netz: Störungsdienst mit Störbezirk Spittal an der Drau", "https://kaerntennetz.at/stoerungsdienst.htm"),
        ("Kelag: Abwärme der Kläranlage für die Fernwärme Spittal an der Drau (30.01.2024)",
         "https://presse.kelag.at/news-wasserverband-millstaetter-see-und-kelag-energie-waerme-abwaerme-der-klaeranlage-"
         "wird-fuer-die-fernwaerme-spittal-an-der-drau-nutzbar-gemacht?id=192828&amp;menueid=27567&amp;l=deutsch"),
        ("Kelag Energie &amp; Wärme: Projekte, Netzverdichtung Spittal an der Drau", "https://www.kew.at/forderungen.htm"),
        ("Stadtgemeinde Spittal an der Drau: Photovoltaik-Potenzialkataster",
         "https://www.spittal-drau.at/buergerservice/klima-energie/photovoltaik-potenzialkataster"),
        ("Stadtgemeinde Spittal an der Drau: Klimaneutrale Stadt",
         "https://www.spittal-drau.at/buergerservice/klima-energie/klimaneutrale-stadt"),
        ("Stadtgemeinde Spittal an der Drau: Energiegeladen in die Zukunft (14.05.2026)",
         "https://www.spittal-drau.at/buergerservice/aktuelles/detailansicht/energiegeladen-in-die-zukunft"),
        ("Stadtgemeinde Spittal an der Drau: Förderungen", "https://www.spittal-drau.at/foerderungen"),
        ("KEM Millstätter See: Region und Gemeinden",
         "https://www.kem-millstaettersee.at/kem-millst%C3%A4tter-see/"),
        ("KEM Millstätter See: Förderungen und Beratung", "https://www.kem-millstaettersee.at/f%C3%B6rderungen/"),
        ("KEM Millstätter See: Ölkesselfreie Gemeinde",
         "https://www.kem-millstaettersee.at/%C3%B6lkesselfreie-gemeinde/"),
        ("Kelag: Wärmepumpen-Prämie", "https://www.kelag.at/privatkunden/ubersicht-zur-warmepumpe.htm"),
    ],
    "notizen": ("Faktenfragen: (1) Hat EBZ ein Projekt im Bezirk Spittal, das als Referenz freigegeben werden kann? "
                "(2) Bauamt Spittal: Die Stadtseite nennt noch 'PV bis zu 40 m2'; gilt Z 20 (alle EE-Anlagen "
                "mitteilungspflichtig) auch dort ohne Flächengrenze? (3) Gibt es im Bezirk Adressen ausserhalb des "
                "Netzes von Kärnten Netz? (4) Land Kärnten Heizungstausch: laut _fakten_2026-10.md widersprüchlich, daher kein Satz genannt. "
                "(5) Kelag-Prämie 1.200 Euro: Laufzeit nicht befristet angegeben, monatlich prüfen. "
                "(6) Bietet EBZ Fernwärme-Beratung wirklich neutral an (Text sagt: wir weisen auf Fernwärme hin)?"),
}
