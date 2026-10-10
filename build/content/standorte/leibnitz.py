"""Ortsseite Leibnitz (Steiermark): /photovoltaik-leibnitz/ aus der Vorlage build/pages/standorte.py.

Briefing: build/seo/standort_leibnitz.json und .md (DataForSEO, Oesterreich/Deutsch, 10.10.2026).
Alle lokalen Angaben stammen aus Quellen, die am 10.10.2026 selbst abgerufen wurden:

- Landesstatistik Steiermark, Gemeindedatenblatt 61053 Leibnitz (aktualisiert 08.09.2026) und Bezirksdatenblatt
  610 Leibnitz (aktualisiert 24.09.2026): Einwohner, Flaeche, Seehoehe, Wohngebaeude, Wohnungen.
- E-Control, Tarifkalkulator (Netzbetreiberabfrage je Postleitzahl, Strom und Gas): 8430 Leibnitz, 8435 Wagna,
  8431 Gralla, 8434 Tillmitsch = Energienetze Steiermark GmbH UND E-Werk Ebner GesmbH (Strom), Gas Energienetze
  Steiermark. 8403 Lebring = Energienetze Steiermark und P.K. Energieversorgungs-GmbH. 8443 Gleinstaetten =
  E-Werk Gleinstaetten GmbH und Energienetze Steiermark. 8410 Wildon, 8462 Gamlitz = nur Energienetze Steiermark.
  Kein Gasnetzbetreiber gelistet fuer 8462 Gamlitz, 8463 Leutschach, 8442 Kitzeck, 8454 Arnfels.
- Energienetze Steiermark, Seite "Erzeugungsanlagen": Einspeiserportal, Zaehlpunkt, Netzanschlusskonzept
  (12 Monate, einmal 12 Monate verlaengerbar), Installationsdokument, Freigabe; Wirkleistungsbegrenzung seit
  1.12.2024 fuer PV von 3,68 bis 250 kW (Netzwerkkabel Wechselrichter zu Smart Meter).
- Steiermaerkisches Baugesetz § 21 in der Fassung LGBl. Nr. 20/2026 (Stmk. Deregulierungsgesetz 2025), gelesen
  ueber die Zusammenfassung der Kammer der Ziviltechniker:innen fuer Steiermark und Kaernten und die Textausgabe
  bei Forum Media; RIS selbst war nicht abrufbar (Sicherheitsabfrage). Dach-/Fassaden-PV meldepflichtig
  (Abs. 1 Z 2 lit. o, Hoehe hoechstens 3,50 m), Batterieanlagen bis 20 kWh meldepflichtig (Abs. 2 Z 2a),
  Waermepumpen meldepflichtig mit Datenblatt und Sachverstaendigen-Bestaetigung zum Planungsbasispegel (Abs. 2 Z 2b,
  Abs. 3 Z 5). Deckt sich mit den Angaben im Briefing build/seo/standort_graz.json (Merkblaetter Stadt Graz).
- Stadtgemeinde Leibnitz (newsroom.leibnitz.at, www.leibnitz.at war am 10.10.2026 wegen Wartung nicht erreichbar):
  Formular "Mitteilung meldepflichtiges Bauvorhaben", Antraege "Direktfoerderung von Solaranlagen" (nur thermische
  Solaranlage ankreuzbar) und "Direktfoerderung von Balkonkraftwerken" (beide ohne Rechtsanspruch, nach Budget),
  Abteilung Baurecht & Umwelt, Hauptplatz 24; Klima- und Standortstrategie 2040 (Beschluss April 2026, rund 65 %
  fossiler Energiebedarf, Pionierstadt "Klimaneutrale Stadt").
- Klima- und Energiefonds, Endbericht "Solare Fernwaerme Leibnitz-Tillmitsch" (Mai 2024): Fernwaermeverbund
  Tillmitsch-Leibnitz-Wagna, Betreiberin Nahwaerme Tillmitsch GmbH & Co KG, Heizzentrale Kaindorf mit zwei
  Biomassekesseln zu je 3 MW.
- Land Steiermark, "Solarpotenzial Steiermark mit neuem Solartool" (April 2023): Digitaler Atlas, SolarTool.
- PVGIS 5.3 (EU-Kommission, Joint Research Centre), Standort 46,781 N / 15,545 O, 1 kWp, 14 % Verluste:
  Sued 30 Grad 1.207 kWh/kWp (Dezember 48,5, Juli 142,8), Ost bzw. West 15 Grad 994 bzw. 997 kWh/kWp.

Foerderung Waermepumpe: laut build/seo/_fakten_2026-10.md (wohnbau.steiermark.at, 10.10.2026) nimmt das Land
Steiermark derzeit keine Antraege fuer neue Waermepumpen an, Bund ausgeschoepft. Kein Prozentsatz auf der Seite.

Bewusst weggelassen (nicht selbst belegt): Betraege der Stadtfoerderung, Zahl der Gemeinden im Bezirk,
Klima- und Energie-Modellregion, Ortsbildschutz, Sonnenstunden, Netzgebietsgrenzen innerhalb der Stadt.
Kein Bild aus Leibnitz im Repo: Hero zeigt das Grazer Referenzprojekt (ehrlicher Alt-Text).
"""

from common import a

SOLARTOOL = ('<a href="https://gis.stmk.gv.at/atlas2/Solartool.html" rel="nofollow noopener" target="_blank">'
             'SolarTool des Landes</a>')

ORT = {
    "key": "pv_leibnitz",
    "name": "Leibnitz",
    "kurz": "Leibnitz",
    "area_name": "Bezirk Leibnitz",
    "land": "stmk",
    "title": "Photovoltaik Leibnitz: PV-Anlage & Wärmepumpe | EBZ Energie",
    "description": ("Photovoltaik und Wärmepumpe in Leibnitz, Wagna und im Bezirk: rund 1.200 kWh je kWp laut PVGIS, "
                    "Meldung statt Baubewilligung. Fachbetrieb aus Villach."),
    "eyebrow": "Photovoltaik und Wärmepumpe Leibnitz",
    "h1": "Photovoltaik in Leibnitz: PV-Anlage, Speicher und Wärmepumpe für die Südsteiermark",
    "lead": ("EBZ Energie plant und montiert Photovoltaik, Batteriespeicher und Wärmepumpen in Leibnitz und im Bezirk. "
             "Wir sind ein Fachbetrieb aus Villach in Kärnten und kommen für Beratung und Montage zu Ihnen in die "
             "Südsteiermark. Sie bekommen einen Projektbericht mit 3D-Belegplan und Statikreport, ein Fixangebot und "
             "einen festen Ansprechpartner von der Planung bis zur Übergabe."),
    "badges": [
        ("rund 1.200 kWh", "je kWp und Jahr am Süddach*"),
        ("Meldung genügt", "für PV am Dach, keine Baubewilligung"),
        ("2 Netzbetreiber", "im Raum Leibnitz laut E-Control"),
    ],
    "hero_img": "/assets/img/ref-flachdach-graz-1.jpg",
    "hero_alt": ("Drohnenaufnahme einer Photovoltaikanlage von EBZ Energie auf dem Flachdach eines Einfamilienhauses "
                 "in Graz, Referenzprojekt aus der Steiermark"),

    "intro": {
        "h2": "Photovoltaik und Wärmepumpe in Leibnitz: was das Dach hier liefert",
        "paragraphs": [
            ("Leibnitz ist Sitz der Bezirkshauptmannschaft und mit 13.441 Einwohnern (Stand 1.1.2026) das Zentrum "
             "der Südsteiermark, das Gemeindeamt liegt auf 273 Metern Seehöhe. Für diesen Standort rechnet das "
             "Solarwerkzeug PVGIS der EU-Kommission mit rund 1.200 kWh Strom je kWp und Jahr auf einem Süddach mit "
             "30 Grad Neigung und mit rund 1.000 kWh je kWp bei einer flachen Ost-West-Belegung.* Eine Anlage mit "
             "10 kWp auf einem Süddach kommt damit auf rund 12.000 kWh im Jahr."),
            ("Stadt und Umland unterscheiden sich deutlich. In der Stadtgemeinde, zu der auch Kaindorf an der Sulm "
             "und Seggauberg gehören, zählt die Landesstatistik 3.328 Wohngebäude mit 7.750 Wohnungen: Hier steht "
             "also viel Geschoßwohnbau. Im ganzen Bezirk sind es 29.568 Wohngebäude mit 44.836 Wohnungen, das Umland "
             "von Wagna bis ins Weinland besteht überwiegend aus Ein- und Zweifamilienhäusern mit eigenem Dach. Für "
             "das Eigenheim planen wir die klassische Dachanlage mit Speicher, im Mehrparteienhaus prüfen wir eine "
             "gemeinschaftliche Anlage oder eine " + a("eg_privat", "Energiegemeinschaft") + "."),
            ("Eine Anlage mit rund 10 kWp und Speicher kostet typischerweise rund 15.000 bis 22.000 Euro vor "
             "Förderung*, die Amortisation liegt typisch bei 4 bis 6 Jahren*. Wie viel davon in Leibnitz bei Ihnen "
             "ankommt, hängt vom Verbrauch ab: Mit Wärmepumpe oder E-Auto nutzen Sie mehr Strom selbst, ohne große "
             "Verbraucher planen wir bewusst kleiner."),
        ],
    },

    "lokal": {
        "h2": "Leibnitz auf einen Blick: Netz, Behörde, Fernwärme, Solarpotenzial",
        "intro": ("Diese Angaben brauchen wir für jede Planung in Leibnitz. Sie stammen aus amtlichen und offiziellen "
                  "Quellen, die Links stehen am Ende der Seite."),
        "rows": [
            ("Stadt und Bezirk",
             "Stadtgemeinde Leibnitz: 13.441 Einwohner, 23,5 km², Seehöhe 273 m (Gemeindeamt). Bezirk Leibnitz: "
             "88.164 Einwohner, 750,1 km² (Landesstatistik Steiermark, Stand 1.1.2026)."),
            ("Stromnetz",
             "Für die Postleitzahl 8430 führt die E-Control zwei Verteilernetzbetreiber: Energienetze Steiermark GmbH "
             "und E-Werk Ebner GesmbH. Dasselbe gilt für Wagna, Gralla und Tillmitsch. In Lebring ist neben "
             "Energienetze Steiermark die P.K. Energieversorgungs-GmbH gelistet, in Gleinstätten die E-Werk "
             "Gleinstätten GmbH."),
            ("Baubehörde",
             "Stadtgemeinde Leibnitz, Abteilung Baurecht &amp; Umwelt, Hauptplatz 24. PV auf Dach oder Fassade, "
             "Batteriespeicher bis 20 kWh und Wärmepumpen sind nach § 21 Steiermärkisches Baugesetz meldepflichtig."),
            ("Solarpotenzial",
             "Der Digitale Atlas Steiermark zeigt Eignung und technisches Potenzial der Dachflächen für Photovoltaik "
             "und Solarthermie. Das " + SOLARTOOL + " schickt den Bericht für ausgewählte Flächen per E-Mail."),
            ("Ertrag je kWp",
             "Rund 1.200 kWh pro Jahr am Süddach mit 30 Grad Neigung, rund 1.000 kWh bei flacher Ost-West-Belegung "
             "(PVGIS 5.3, Standort Leibnitz, 14 % Systemverluste).*"),
            ("Fernwärme",
             "Fernwärmeverbund Tillmitsch, Leibnitz, Wagna der Nahwärme Tillmitsch. Die Heizzentrale in Kaindorf "
             "arbeitet mit zwei Biomassekesseln zu je 3 MW (Klima- und Energiefonds, 2024)."),
            ("Gasnetz",
             "Energienetze Steiermark GmbH in Leibnitz, Wagna, Gralla, Tillmitsch, Lebring und Wildon. Für Gamlitz, "
             "Leutschach, Kitzeck und Arnfels weist die E-Control keinen Gasnetzbetreiber aus."),
            ("Klimastrategie der Stadt",
             "Klima- und Standortstrategie Leibnitz 2040, im April 2026 einstimmig vom Gemeinderat beschlossen. Laut "
             "Stadt stammen rund 65 % des Energiebedarfs noch aus fossilen Quellen."),
        ],
    },

    "netz": {
        "h2": "Genehmigung und Netzanschluss in Leibnitz: Meldung an die Stadt, Antrag beim Netzbetreiber",
        "betreiber": "Ihrem Netzbetreiber (in Leibnitz Energienetze Steiermark oder E-Werk Ebner)",
        "paragraphs": [
            ("Eine Photovoltaikanlage auf Dach oder Fassade braucht in der Steiermark keine Baubewilligung. Sie ist "
             "nach § 21 des Steiermärkischen Baugesetzes meldepflichtig: Das Vorhaben wird der Gemeinde vor der "
             "Ausführung schriftlich mitgeteilt, mit Grundstücksnummer, Lage am Grundstück und einer kurzen "
             "Beschreibung. Die Anlage und ihre Teile dürfen 3,50 Meter Höhe nicht überschreiten. In Leibnitz geht "
             "die Mitteilung an die Abteilung Baurecht &amp; Umwelt der Stadtgemeinde, die dafür ein eigenes "
             "Formular für meldepflichtige Bauvorhaben bereitstellt."),
            ("Seit der Novelle des Baugesetzes 2026 sind auch Batteriespeicher ausdrücklich geregelt: Bis 20 kWh "
             "genügt die Meldung mit einem Nachweis des Energieinhalts, bis 100 kWh ist zusätzlich ein "
             "Nachweis zum Brandverhalten der Zellen nötig. Auch meldepflichtige Vorhaben müssen Bebauungsplan, "
             "Baufluchtlinien und Abstände einhalten. Wir bereiten die Mitteilung mit allen Beilagen vor, "
             "unterschrieben wird sie von Ihnen als Eigentümer."),
            ("Beim Stromnetz ist Leibnitz ein Sonderfall. Für die Postleitzahl 8430 führt der Tarifkalkulator der "
             "E-Control zwei Verteilernetzbetreiber: die Energienetze Steiermark GmbH und die E-Werk Ebner GesmbH. "
             "Welcher für Ihre Adresse zuständig ist, steht auf Ihrer Stromrechnung beim Zählpunkt. Bei Energienetze "
             "Steiermark läuft der Antrag über das Einspeiserportal: Zuerst wird der Einspeisezählpunkt vergeben, "
             "danach erstellt der Netzbetreiber von sich aus das Netzanschlusskonzept mit dem technisch geeigneten "
             "Anschlusspunkt. Es gilt zwölf Monate und lässt sich einmal um zwölf Monate verlängern."),
            ("Für PV-Anlagen von 3,68 bis 250 kW verlangt Energienetze Steiermark seit 1. Dezember 2024 eine "
             "Wirkleistungsbegrenzung: Bei Neuanlagen wird ein Netzwerkkabel vom Wechselrichter zum Smart Meter "
             "verlegt, damit der Netzbetreiber die Anlage im Notfall für wenige Stunden abschalten kann. Eingeschaltet "
             "wird erst nach der Freigabe. Liegt Ihr Haus im Netz des E-Werks Ebner, klären wir Ablauf und technische "
             "Vorgaben direkt mit dem Betreiber, bevor Sie ein Angebot unterschreiben."),
        ],
        "bullets": [
            "PV auf Dach oder Fassade: Meldung an die Gemeinde vor Baubeginn, keine Baubewilligung",
            "Batteriespeicher bis 20 kWh: meldepflichtig mit Nachweis des Energieinhalts",
            "Netzanschlusskonzept von Energienetze Steiermark: 12 Monate gültig, einmal verlängerbar",
            "Netzwerkkabel vom Wechselrichter zum Smart Meter bei Neuanlagen ab 3,68 kW",
        ],
        "img": "gen_detail",
        "alt": "Montagedetail einer Photovoltaikanlage: ein Monteur verschraubt eine Modulklemme auf der Unterkonstruktion",
    },

    "waermepumpe": {
        "h2": "Wärmepumpe in Leibnitz: erst Fernwärme prüfen, dann Heizung tauschen und mit PV koppeln",
        "paragraphs": [
            ("Vor jeder Wärmepumpe steht in Leibnitz eine Frage, die sich in vielen Orten nicht stellt: Liegt "
             "Fernwärme vor der Tür? Laut Klima- und Energiefonds deckt der Fernwärmeverbund Tillmitsch, Leibnitz, "
             "Wagna einen Großteil der Wärmeversorgung im Raum Leibnitz, Tillmitsch, Kaindorf und Gralla. "
             "Das Netz betreibt laut Bericht die Nahwärme Tillmitsch, die Heizzentrale in Kaindorf arbeitet mit zwei "
             "Biomassekesseln zu je 3 MW. Ist an Ihrer Adresse ein Anschluss möglich, sagen wir Ihnen das offen: "
             "Dann ist Fernwärme oft der einfachere Weg, und die Photovoltaik senkt Ihre Stromrechnung."),
            ("Außerhalb des Fernwärmenetzes ist die Luft-Wasser-Wärmepumpe meist die naheliegende Lösung. In "
             "Leibnitz, Wagna, Gralla, Tillmitsch, Lebring und Wildon betreibt Energienetze Steiermark ein Gasnetz: "
             "Wer dort eine Gastherme ersetzt, wird mit der Wärmepumpe unabhängig vom Gaspreis. Für Gamlitz, "
             "Leutschach, Kitzeck oder Arnfels weist die E-Control keinen Gasnetzbetreiber aus, dort steht ein "
             "Gasanschluss beim Heizungstausch gar nicht zur Wahl. Eine Luft-Wasser-Wärmepumpe kostet im "
             "Einfamilienhaus 12.000 bis 22.000 Euro inklusive Installation, im Altbau mit Anpassungen 15.000 bis "
             "28.000 Euro.* Bis 55 Grad Vorlauftemperatur arbeitet sie effizient, die Montage dauert 2 bis 4 Tage. "
             "Gerechnet wird derzeit ohne Zuschuss: Land Steiermark und Bund nehmen für neue Wärmepumpen keine "
             "Förderanträge an (Stand Oktober 2026)."),
            ("Auch die Wärmepumpe ist in der Steiermark seit der Baugesetz-Novelle 2026 meldepflichtig. Der "
             "Mitteilung an die Gemeinde liegen das technische Datenblatt und die Bestätigung eines befugten "
             "Sachverständigen bei, dass der zulässige Planungsbasispegel an der relevanten Grundgrenze eingehalten "
             "wird. Den Aufstellort der Außeneinheit planen wir deshalb von Anfang an mit Blick auf das "
             "Nachbargrundstück."),
            ("Mit Photovoltaik rechnen wir in Leibnitz nach dem Jahresverlauf, nicht nach dem Jahresmittel. Laut "
             "PVGIS liefert eine 10-kWp-Anlage am Süddach im Juli rund 1.430 kWh, im Dezember rund 490 kWh.* Die "
             "Wärmepumpe braucht den meisten Strom genau dann, wenn das Dach am wenigsten liefert. Im Winter deckt "
             "die PV-Anlage also einen Teil des Heizstroms, in der Übergangszeit und im Sommer läuft das Warmwasser "
             "großteils mit eigenem Strom. Ein " + a("ems", "Energiemanagementsystem") + " legt die Laufzeiten in "
             "die Sonnenstunden."),
        ],
        "bullets": [
            "Zuerst prüfen: Ist an Ihrer Adresse ein Fernwärmeanschluss möglich?",
            "Luft-Wasser-Wärmepumpe: 12.000 bis 22.000 € inklusive Installation, im Altbau 15.000 bis 28.000 €*",
            "Meldung an die Gemeinde mit Datenblatt und Schallbestätigung",
            a("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau: was vorher zu klären ist"),
        ],
        "img": "waermepumpe",
        "alt": "Außeneinheit einer Luft-Wasser-Wärmepumpe neben einem Wohnhaus, Symbolbild für den Heizungstausch im Raum Leibnitz",
    },

    "foerderung_h2": "Förderung für Photovoltaik und Wärmepumpe in Leibnitz",
    "foerderung_lokal": [
        ("Die Stadtgemeinde Leibnitz führt Antragsformulare für eine Direktförderung von Solaranlagen (im Formular "
         "als thermische Solaranlage) und von Balkonkraftwerken. Beide werden ohne Rechtsanspruch und nach Maßgabe "
         "der verfügbaren Budgetmittel vergeben, zuständig ist die Abteilung Baurecht &amp; Umwelt. Eine eigene "
         "Förderung der Stadt für Photovoltaik-Dachanlagen, Stromspeicher oder den Heizungstausch haben wir in den "
         "Unterlagen der Stadt nicht gefunden (Stand Oktober 2026). Wir fragen vor dem Angebot bei Ihrer Gemeinde "
         "nach, auch in Wagna, Gralla oder Gamlitz: Jede Gemeinde im Bezirk regelt das selbst."),
    ],

    "referenzen": {
        "h2": "Referenzen aus der Steiermark: zwei Projekte in Graz",
        "intro": ("Aus Leibnitz selbst können wir Ihnen noch kein dokumentiertes Referenzprojekt zeigen. Die "
                  "nächstgelegenen Anlagen mit vollständigen Zahlen stehen in Graz: ein Einfamilienhaus und ein "
                  "Stadthaus, beide mit Flachdach, Speicher und Wallbox. Dazu kommt ein Einfamilienhaus in Villach "
                  "als Beispiel für das klassische Satteldach."),
        "slugs": ["projekt-flachdach-in-graz", "projekt-stadthaus-in-graz", "projekt-einfamilienhaus-villach"],
    },

    "umgebung": ["Wagna", "Gralla", "Tillmitsch", "Lebring-Sankt Margarethen", "Wildon", "Gamlitz",
                 "Ehrenhausen an der Weinstraße", "Straß in Steiermark", "Heimschuh", "Kitzeck im Sausal",
                 "Gleinstätten", "Leutschach an der Weinstraße"],

    "links": [
        ("/energiegemeinschaft-steiermark/", "Energiegemeinschaft in der Steiermark"),
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau"),
        ("/pv-speicher-nachruesten/", "PV-Speicher nachrüsten"),
        ("/kosten-einer-solaranlage/", "Was eine Solaranlage kostet"),
    ],

    "faq": [
        ("Was kostet eine Photovoltaikanlage in Leibnitz mit Speicher?",
         "Eine Anlage mit rund 10 kWp und Speicher kostet typischerweise rund 15.000 bis 22.000 Euro vor Förderung, "
         "inklusive Montage, Netzanmeldung und Inbetriebnahme (EBZ-Richtpreis, Stand Oktober 2026). Der Bund zahlt 2026 "
         "einen Investitionszuschuss von 150 Euro je kWp bis 10 kWp und 150 Euro je kWh Speicher, eine Landespauschale "
         "für private PV gibt es in der Steiermark nicht. Den Fixpreis für Ihr Haus in Leibnitz nennen wir nach dem "
         "Termin vor Ort, zusammen mit dem Projektbericht mit 3D-Belegplan und Statikreport."),
        ("Wie viel Strom liefert eine PV-Anlage in Leibnitz pro kWp?",
         "Das Solarwerkzeug PVGIS der EU-Kommission rechnet für Leibnitz mit rund 1.200 kWh je kWp und Jahr auf einem "
         "Süddach mit 30 Grad Neigung und mit rund 1.000 kWh je kWp bei flacher Ost-West-Belegung (14 Prozent "
         "Systemverluste). Eine 10-kWp-Anlage am Süddach kommt damit auf rund 12.000 kWh im Jahr. Das ist ein "
         "Richtwert: Verschattung, Dachneigung und Ausrichtung Ihres Hauses prüfen wir vor Ort."),
        ("Brauche ich in Leibnitz eine Baubewilligung für die PV-Anlage?",
         "Nein. Photovoltaik auf Dach oder Fassade ist nach § 21 des Steiermärkischen Baugesetzes meldepflichtig. Die "
         "Mitteilung geht vor Baubeginn schriftlich an die Stadtgemeinde Leibnitz, Abteilung Baurecht und Umwelt, mit "
         "Grundstücksnummer, Lage und kurzer Beschreibung. Die Anlage darf 3,50 Meter Höhe nicht überschreiten und muss "
         "Bebauungsplan und Abstände einhalten. Ein Batteriespeicher bis 20 kWh ist ebenfalls meldepflichtig. Wir "
         "bereiten die Mitteilung für Sie vor."),
        ("Welcher Netzbetreiber ist in Leibnitz für meine PV-Anlage zuständig?",
         "Das hängt von der Adresse ab. Für die Postleitzahl 8430 Leibnitz führt die E-Control zwei "
         "Verteilernetzbetreiber: die Energienetze Steiermark GmbH und die E-Werk Ebner GesmbH. Dasselbe gilt für "
         "Wagna, Gralla und Tillmitsch. Ihr Netzbetreiber steht auf der Stromrechnung beim Zählpunkt. Wir stellen den "
         "Antrag beim richtigen Betreiber und planen die Anlage nach dessen Vorgaben, bei Energienetze Steiermark über "
         "das Einspeiserportal."),
        ("Fernwärme oder Wärmepumpe: Was passt in Leibnitz besser?",
         "Das entscheidet die Adresse. In Leibnitz, Tillmitsch, Wagna und Gralla gibt es den Fernwärmeverbund der "
         "Nahwärme Tillmitsch mit Biomasse-Heizzentrale in Kaindorf. Wo ein Anschluss möglich ist, ist Fernwärme oft "
         "der einfachere Weg. Außerhalb des Netzes, etwa in vielen Einfamilienhäusern im Umland und im Weinland, ist "
         "die Luft-Wasser-Wärmepumpe meist die naheliegende Lösung, am besten zusammen mit einer Photovoltaikanlage. "
         "Wir prüfen beides, bevor wir ein Angebot schreiben."),
        ("Muss ich eine Wärmepumpe in Leibnitz bei der Gemeinde melden?",
         "Ja. Seit der Novelle des Steiermärkischen Baugesetzes 2026 ist die ortsfeste Aufstellung einer Wärmepumpe "
         "meldepflichtig. Der Mitteilung an die Stadtgemeinde Leibnitz liegen das technische Datenblatt und die "
         "Bestätigung eines befugten Sachverständigen bei, dass der zulässige Planungsbasispegel an der relevanten "
         "Grundgrenze eingehalten wird. Deshalb planen wir den Aufstellort der Außeneinheit von Anfang an mit Blick "
         "auf die Nachbarn."),
        ("Zahlt die Stadt Leibnitz eine Förderung für Photovoltaik oder Wärmepumpe?",
         "Die Stadtgemeinde Leibnitz führt Antragsformulare für eine Direktförderung von thermischen Solaranlagen und "
         "von Balkonkraftwerken, ohne Rechtsanspruch und nach Maßgabe des Budgets. Eine eigene Stadtförderung für "
         "Photovoltaik-Dachanlagen, Speicher oder Wärmepumpe haben wir in den Unterlagen der Stadt nicht gefunden "
         "(Stand Oktober 2026). Für PV und Speicher gilt der Investitionszuschuss des Bundes. Für neue Wärmepumpen "
         "nehmen Land Steiermark und Bund derzeit keine Förderanträge an. Wir fragen vor dem Angebot bei Ihrer "
         "Gemeinde nach."),
        ("Kommt EBZ Energie aus Villach wirklich bis nach Leibnitz?",
         "Ja. Unser Firmensitz ist die Triglavstraße 15 in Villach, montiert wird in Kärnten und der Steiermark. Einen "
         "eigenen Standort in der Südsteiermark haben wir nicht. Für die Erstberatung kommen wir zu Ihnen nach "
         "Leibnitz, Wagna, Gralla oder ins Weinland, sehen uns Dach, Zählerschrank und Heizraum an und erstellen "
         "danach das Fixangebot. Zwei dokumentierte Referenzprojekte aus der Steiermark stehen in Graz."),
    ],

    "quellen": [
        ("Landesstatistik Steiermark: Gemeindedatenblatt Leibnitz (61053), Stand September 2026",
         "https://www.landesentwicklung.steiermark.at/cms/dokumente/12256481_141979478/0a48dff2/61053.pdf"),
        ("Landesstatistik Steiermark: Bezirksdatenblatt Leibnitz (610), Stand September 2026",
         "https://www.landesentwicklung.steiermark.at/cms/dokumente/12658731_141979478/b8d8a2ef/610.pdf"),
        ("E-Control: Tarifkalkulator, Netzbetreiber für Strom und Gas je Postleitzahl",
         "https://www.e-control.at/tarifkalkulator"),
        ("Energienetze Steiermark: Erzeugungsanlagen, Einspeiserportal und Netzanschlusskonzept",
         "https://www.e-netze.at/Strom/Erzeugungsanlagen/Default.aspx"),
        ("Kammer der Ziviltechniker:innen für Steiermark und Kärnten: Änderungen im Steiermärkischen Baugesetz "
         "(Deregulierungsgesetz 2025), § 21 Meldepflichtige Vorhaben",
         "https://sued.zt.at/fileadmin/user_upload/redakteure_stk/02_Mitglieder/Gesetze/2026/Stmk._Deregulierungsgesetz_2025.pdf"),
        ("Stadtgemeinde Leibnitz: Formulare und Anträge, Mitteilung meldepflichtiges Bauvorhaben",
         "https://newsroom.leibnitz.at/formulareundantraege/"),
        ("Stadtgemeinde Leibnitz: Klima- und Standortstrategie 2040",
         "https://newsroom.leibnitz.at/weichenstellung-fuer-die-zukunftleibnitz-praesentiert-klima-und-standortstrategie-2040/"),
        ("Klima- und Energiefonds: Endbericht Solare Fernwärme Leibnitz-Tillmitsch",
         "https://klimafonds.gv.at/wp-content/uploads/2025/02/KC398825_Publizierbarer-Endbericht_SolareGA.pdf"),
        ("Land Steiermark: Solarpotenzial im Digitalen Atlas und SolarTool",
         "https://landesentwicklung.steiermark.at/cms/beitrag/12910759/145230171"),
        ("Europäische Kommission, Joint Research Centre: PVGIS (Ertragsberechnung für den Standort Leibnitz)",
         "https://re.jrc.ec.europa.eu/pvg_tools/de/"),
    ],

    "notizen": (
        "Faktenfragen für den Kunden: (1) Gibt es EBZ-Projekte im Bezirk Leibnitz, die als Referenz freigegeben "
        "werden können? (2) Erfahrungen mit dem Netz des E-Werks Ebner (Ablauf, Vorgaben)? "
        "Unsicherheiten: www.leibnitz.at war am 10.10.2026 in Wartung; laut Suchmaschinen-Vorschau nennt die Stadtseite "
        "Pauschalen von 150 Euro (Solaranlagen) und 50 Euro (Balkonkraftwerke) und den Hinweis, dass es seit 2024 keine "
        "PV-Förderung mehr gibt. Nicht selbst abgerufen, deshalb keine Beträge auf der Seite. Nach Ende der Wartung "
        "prüfen: leibnitz.at/buergerservice/bauen/foerderung-von-solaranlagen-und-balkonkraftwerken. "
        "P.K. Energieversorgungs-GmbH (Lebring, Ragnitz) vermutlich Netzgesellschaft des E-Werks Kiendler: nicht belegt, "
        "daher nur der Name laut E-Control. E-Control ordnet nach Postleitzahl zu, die Grenze zwischen den Netzen "
        "innerhalb der Stadt ist nicht belegt. Baugesetz: RIS nicht abrufbar, Quelle ist die Zusammenfassung der "
        "ZT-Kammer (Inkrafttreten laut Kammer 27.2.2026, laut Forum Media Fassung LGBl. 20/2026 ab 1.3.2026)."
    ),
}
