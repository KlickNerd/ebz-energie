"""Ortsseite Hermagor (/photovoltaik-hermagor/), Slug-Key pv_hermagor, Vorlage build/pages/standorte.py.

Photovoltaik (primaer) und Waermepumpe (sekundaer) in Hermagor-Pressegger See und im Gailtal.
Briefing: build/seo/standort_hermagor.json/.md. Alle Ortsbegriffe ("photovoltaik hermagor", "pv anlage
hermagor", "waermepumpe hermagor", "photovoltaik gailtal", "photovoltaik koetschach-mauthen", "photovoltaik
nassfeld") haben in Oesterreich KEIN messbares Google-Ads-Volumen; die Seite zielt auf Long-Tail, Local
und zitierbare lokale Fakten (zwei Netzbetreiber im Bezirk, Ertrag je kWp, Fernwaerme).

EBZ hat KEINEN Standort in Hermagor: Firmensitz nur Triglavstrasse 15, 9500 Villach.

Lokale Fakten, alle am 10.10.2026 selbst abgerufen:
- Statistik Austria, "Ein Blick auf die Gemeinde" 20305: 6.930 Einwohner Gemeinde / 17.910 Bezirk (2026);
  Katasterflaeche 20.482 ha, 62,0 % Wald, Dauersiedlungsraum 22,7 %; 526 land- und forstwirtschaftliche
  Betriebe (Agrarstrukturerhebung 2020). statistik.at/blickgem/G0201|G0101|G0701/g20305.pdf
- Baubehoerde: Stadtgemeinde Hermagor-Pressegger See, Abteilung Baubehoerde/Hochbau, Wulfeniaplatz 1,
  9620 Hermagor; Aufgaben u. a. Ortsbildpflege; Formulare Bauanzeige, Bauansuchen, Ortsbildpflege (Anzeige).
  hermagor.at/verwaltung/abteilungen/baubehoerde/ und /buergerservice/downloads/formulare/
- Gebaeudebestand: textlicher Bebauungsplan Hermagor (GR 06/2012): Stadtkern mit Sattel-, Walm- und
  Flachdaechern; doerfliche Ortskerne mit ueberformten landwirtschaftlichen Hofstellengebaeuden;
  touristischer Schwerpunkt Nassfeld mit Zweitwohnsitzen und Beherbergungsbetrieben.
- Baurecht: Mitteilung nach § 7 Abs. 1 lit. a Z 20 K-BO 1996 (bauliche Anlagen, die erneuerbare Energie
  erzeugen oder elektrische Energie speichern; erneuerbar umfasst laut Formular auch Umgebungsenergie),
  Vollendungsmeldung binnen zwei Wochen, Flaechenwidmung und Bebauungsplan sind einzuhalten. Quelle:
  Formular des Magistrats Villach zur selben landesweiten Bestimmung (RIS war nicht erreichbar, HTTP 503).
  Konsistent mit build/pages/standort_klagenfurt.py.
- Netz: KNG-Kaernten Netz GmbH, 100-%-Tochter der Kelag, betreibt das Elektrizitaets- und
  Erdgasverteilernetz in Kaernten (kaerntennetz.at/impressum.htm); PV-Ablauf: Antrag im Kundenportal,
  auch durch bevollmaechtigten Elektriker/Anlagenplaner, Netzberechnung, Netzzutrittsangebot,
  Einspeiseleistung mindestens in Hoehe des Strombezugsrechts, sonst dynamische Leistungsregelung,
  Fertigstellungsmeldung durch konzessionierten Elektriker, Abnahmevertrag (kaerntennetz.at/pv.htm).
- Zweiter Netzbetreiber im Bezirk: AAE Wasserkraft GmbH, Koetschach 66, 9640 Koetschach-Mauthen:
  regionales Verteilernetz in Koetschach, ca. 700 Zaehlpunkte, ca. 550 Anschlussanlagen, 10 Trafostationen,
  vorgelagert KNG ueber UW Wuermlach (aae-wasserkraft.at/stromnetz/netze/); Netzanschluss fuer Eigenheim
  oder Erzeugungsanlage per Anfrage (aae-wasserkraft.at/stromnetz/stromanschluss/). Der e5-Auditbericht
  2020 nennt als Elektrizitaetsversorgung der Gemeinde "KNG GmbH, AAE Naturstrom GmbH".
- Ertrag: PVGIS 5.3 (EU-Kommission, JRC), SARAH3 2005 bis 2023, 46.627 N / 13.367 O, 1 kWp, 14 % Verluste,
  Horizont eingerechnet: Sued 30 Grad 1.185 kWh/kWp (Dezember 39, Juli 141), Ost 25 Grad 976, West 25 Grad
  943. Koetschach-Mauthen (46.675 N / 13.000 O): Sued 30 Grad 1.250 kWh/kWp.
- Fernwaerme Hermagor: KELAG Waerme GmbH, rund 120 Kunden, Biomasse-Heisswasserkessel 4 MW (Fachverband
  Gas Waerme, fernwaerme.at, Meldung vom 03.11.2016: Zahl ist alt, im Text mit "Stand 2016").
- Koetschach-Mauthen (e5-Audit-Bericht 2020, Amt der Kaerntner Landesregierung, Abt. 8): e5 seit 2009,
  Umsetzungsgrad 82,1 %, 21 Kleinwasserkraftwerke, zwei Windturbinen, drei Biomasseheizwerke, Fernwaerme
  in Koetschach, Mauthen und Wuermlach, PV 2019: 118 kWp je 1.000 EW (Kaernten 229), gemeindeeigene
  Foerderung fuer Solaranlagen und Heizungsanlagen (Stand 2020, aktuelle Hoehe NICHT belegt).
- KEM Karnische Energie aus dem Bezirk Hermagor, eine von 18 KEM in Kaernten (Mitteilungsblatt der
  Stadtgemeinde, Juni 2026); KEM Tourismus und Region Hermagor mit 9 Gemeinden (Regionalstrategie Region
  Hermagor, Land Kaernten).
- EEG Wulfenia: Stadtgemeinde und 6 Betriebe, Start mit 8 bestehenden PV-Anlagen und Kleinwasserkraftwerk,
  Aufnahme von Haushalten vorgesehen (hermagor.at, EEG-050923.pdf).
- Gemeindefoerderung Hermagor: auf hermagor.at (Formulare, Abteilungen) keine fuer PV, Speicher oder
  Heizungstausch gefunden.

Mangels Quelle WEGGELASSEN: Solarpotenzialkataster KAGIS (ktn.gv.at nicht erreichbar), Seehoehe und
Sonnenstunden, Schneelastzone (nur als Planungsthema ohne Zahl), Gasnetz, gemeindeweise Zuordnung der
Netzgebiete, Landesfoerderung Waermepumpe (Hoehe laut _fakten_2026-10.md ungeklaert), Kelag-Praemie,
Entfernungen und Fahrzeiten, Aussage zu eigenen EBZ-Projekten im Bezirk.

Waermepumpe: Zahlen nur aus build/pages/waermepumpe.py (12.000 bis 22.000 EUR, 1 kWh Strom -> 4 bis 5 kWh
Waerme, Vorlauf bis 55 Grad, Beispielhaus 12.000 kWh / JAZ 4).
"""

from common import a

_PVGIS = "https://re.jrc.ec.europa.eu/api/v5_3/PVcalc?lat=46.627&amp;lon=13.367&amp;peakpower=1&amp;loss=14&amp;angle=30&amp;aspect=0"

ORT = {
    "key": "pv_hermagor",
    "name": "Hermagor-Pressegger See",
    "kurz": "Hermagor",
    "area_name": "Bezirk Hermagor",
    "land": "ktn",
    "title": "Photovoltaik Hermagor & Wärmepumpe im Gailtal | EBZ Energie",
    "description": ("Photovoltaik und Wärmepumpe in Hermagor und im Gailtal: rund 1.185 kWh je kWp am Süddach, "
                    "Netzanmeldung bei Kärnten Netz oder AAE Wasserkraft inklusive."),
    "eyebrow": "Photovoltaik und Wärmepumpe Hermagor · Gailtal",
    "h1": "Photovoltaik in Hermagor: PV-Anlage, Speicher und Wärmepumpe für das Gailtal",
    "lead": ("EBZ Energie ist ein Fachbetrieb aus Villach und plant Photovoltaik, Speicher und Wärmepumpe bei Ihnen "
             "vor Ort in Hermagor-Pressegger See und im Gailtal, von St. Stefan bis Kötschach-Mauthen. Vor dem "
             "Angebot klären wir, was hier den Unterschied macht: Horizont und Schnee am Dach, der zuständige "
             "Netzbetreiber (Kärnten Netz oder AAE Wasserkraft) und die Frage Fernwärme oder Wärmepumpe. Sie "
             "erhalten einen Projektbericht mit 3D-Belegplan und Statikreport und ein Fixangebot."),
    "badges": [
        ("rund 1.185 kWh", "je kWp und Jahr am Süddach in Hermagor*"),
        ("2 Netzbetreiber", "im Bezirk: Kärnten Netz und AAE Wasserkraft"),
        ("1 Ansprechpartner", "von der Planung bis zur Übergabe"),
    ],
    "hero_img": "gen_eigenheim",
    "hero_alt": ("Einfamilienhaus mit Photovoltaikanlage auf dem Satteldach vor einer Bergkette im Abendlicht "
                 "(Symbolbild, nicht in Hermagor aufgenommen)"),
    "kpis": [
        ("bis zu 85 %", "weniger Stromkosten mit PV und Speicher*"),
        ("rund 1.185 kWh", "je kWp und Jahr, Süddach in Hermagor (PVGIS)*"),
        ("3.000 €", "Landespauschale Kärnten für PV mit Speicher"),
        ("300+", "dokumentierte Projekte in 6 Bundesländern"),
    ],
    "intro": {
        "h2": "Lohnt sich Photovoltaik in Hermagor und im Gailtal?",
        "paragraphs": [
            ("Ja, wenn die Planung den Horizont ernst nimmt. Für den Standort Hermagor rechnet das "
             "Photovoltaik-Informationssystem PVGIS der EU-Kommission mit rund 1.185 kWh je kWp und Jahr bei "
             "Südausrichtung und 30 Grad Neigung, mit rund 976 kWh für ein Ostdach und rund 943 kWh für ein Westdach "
             "mit 25 Grad*. Die Abschattung durch das Gelände ist in diesen Werten bereits eingerechnet. Hermagor "
             "liegt damit im Kärntner Richtwert von rund 1.000 bis 1.100 kWh je kWp, bei reiner Südlage darüber. "
             "Talaufwärts, am Standort Kötschach-Mauthen, kommt PVGIS für das Süddach auf rund 1.250 kWh je kWp*."),
            ("Dieselbe Rechnung zeigt, worauf es im Tal zwischen Gailtaler und Karnischen Alpen ankommt: Im Dezember "
             "liefert ein Kilowattpeak in Hermagor rund 39 kWh, im Juli rund 141 kWh*. Ob ein Dach in Presseggen, Egg "
             "oder Rattendorf im Winter früh Sonne bekommt oder lange im Schatten eines Bergrückens liegt, "
             "entscheidet über Modulbelegung und Speichergröße. Pauschalen helfen hier nicht. Im Projektbericht mit "
             "3D-Belegplan und Statikreport steht, wie Ihr Dach belegt wird und was es trägt; die Schneelast am "
             "Standort gehört im Gailtal zu jeder statischen Prüfung."),
            ("Der Gebäudebestand spricht für eher große Anlagen. Der textliche Bebauungsplan der Stadtgemeinde "
             "beschreibt neben dem dicht bebauten Stadtkern mit Sattel-, Walm- und Flachdächern vor allem dörfliche "
             "Ortskerne mit großen, umgebauten Hofgebäuden, Streusiedlungen mit Einfamilienhäusern und Hofstellen "
             "sowie den touristischen Schwerpunkt am Nassfeld mit Zweitwohnsitzen und Beherbergungsbetrieben. "
             "Statistik Austria zählt in der Gemeinde 526 land- und forstwirtschaftliche Betriebe (2020). Viel "
             "Dachfläche und ein hoher Strom- und Warmwasserbedarf im Haus: gute Voraussetzungen für Eigenverbrauch. "
             "Eine 10-kWp-Anlage mit Speicher kostet rund 15.000 bis 22.000 Euro vor Förderung*."),
        ],
    },
    "lokal": {
        "h2": "Hermagor und das Gailtal: Zahlen und Zuständigkeiten für Ihre Anlage",
        "intro": ("Diese Angaben brauchen wir für jede Planung im Bezirk Hermagor. Sie stammen aus den unten "
                  "verlinkten amtlichen und offiziellen Quellen."),
        "rows": [
            ("Gemeinde und Bezirk",
             "Stadtgemeinde Hermagor-Pressegger See, Bezirkshauptstadt des Bezirks Hermagor. 6.930 Einwohner in der "
             "Gemeinde, 17.910 im Bezirk (Statistik Austria, 2026)."),
            ("Fläche und Siedlungsraum",
             "20.482 Hektar Gemeindefläche, davon 62 Prozent Wald. Als Dauersiedlungsraum gelten 22,7 Prozent "
             "(Statistik Austria)."),
            ("Baubehörde",
             "Stadtgemeinde Hermagor-Pressegger See, Abteilung Baubehörde/Hochbau, Wulfeniaplatz 1, 9620 Hermagor. "
             "Formulare für Bauanzeige, Bauansuchen und Ortsbildpflege stehen auf hermagor.at."),
            ("Netzbetreiber Strom",
             "KNG-Kärnten Netz GmbH, eine 100-Prozent-Tochter der Kelag. In Kötschach betreibt die AAE Wasserkraft "
             "GmbH ein eigenes Verteilernetz mit rund 700 Zählpunkten, das über das Umspannwerk Würmlach an das Netz "
             "der Kärnten Netz angebunden ist."),
            ("Ertrag je kWp",
             "PVGIS für den Standort Hermagor: Süd 30 Grad rund 1.185 kWh, Ost 25 Grad rund 976 kWh, West 25 Grad "
             "rund 943 kWh je kWp und Jahr* (Daten 2005 bis 2023, 14 Prozent Systemverluste, Horizont eingerechnet)."),
            ("Fernwärme",
             "In Hermagor betreibt die KELAG Wärme GmbH ein Fernwärmenetz mit rund 120 Kunden, gespeist von einem "
             "Biomassekessel mit 4 MW (Fachverband Gas Wärme, Stand 2016). In Kötschach, Mauthen und Würmlach gibt es "
             "eigene Wärmenetze (e5-Auditbericht 2020)."),
            ("Klima- und Energie-Modellregion",
             "KEM Karnische Energie für den Bezirk Hermagor, eine von 18 Klima- und Energie-Modellregionen in Kärnten "
             "(Mitteilungsblatt der Stadtgemeinde, Juni 2026)."),
            ("Energiegemeinschaft",
             "Erneuerbare Energiegemeinschaft Wulfenia: gegründet von der Stadtgemeinde mit sechs Betrieben, zum "
             "Start mit acht bestehenden PV-Anlagen und einem Kleinwasserkraftwerk. Die Aufnahme von Haushalten ist "
             "laut Stadtgemeinde vorgesehen. Mehr zur " + a("eg_privat", "Energiegemeinschaft für Private") + "."),
            ("Energiegemeinde im Bezirk",
             "Kötschach-Mauthen ist seit 2009 e5-Gemeinde (Umsetzungsgrad 82,1 Prozent im Audit 2020) mit 21 "
             "Kleinwasserkraftwerken, zwei Windturbinen und drei Biomasseheizwerken. Bei Photovoltaik lag die "
             "Gemeinde 2019 mit 118 kWp je 1.000 Einwohner unter dem Kärntner Schnitt von 229 kWp: Auf den Dächern "
             "ist noch Platz."),
        ],
    },
    "netz": {
        "h2": "Genehmigung und Netzanschluss in Hermagor: Bauamt, Kärnten Netz und AAE Wasserkraft",
        "betreiber": "Ihrem Netzbetreiber (Kärnten Netz oder AAE Wasserkraft)",
        "paragraphs": [
            ("Nach der Kärntner Bauordnung (§ 7 Abs. 1 lit. a Z 20 K-BO 1996) sind bauliche Anlagen, die erneuerbare "
             "Energie erzeugen oder elektrische Energie speichern, mitteilungspflichtig. Für eine Photovoltaikanlage "
             "mit Speicher auf Ihrem Dach heißt das in der Regel: eine schriftliche Mitteilung an die Baubehörde vor "
             "Beginn der Arbeiten, mit Grundstücksnummer, Katastralgemeinde und kurzer Beschreibung, und eine "
             "Vollendungsmeldung binnen zwei Wochen. Zuständig ist die Baubehörde der Stadtgemeinde "
             "Hermagor-Pressegger See am Wulfeniaplatz 1. Flächenwidmung und Bebauungsplan gelten auch für "
             "mitteilungspflichtige Vorhaben. Die Stadtgemeinde führt außerdem eigene Formulare zur Ortsbildpflege; "
             "ob Ihr Vorhaben davon berührt ist, klären wir vorab mit dem Bauamt."),
            ("Den Netzanschluss beantragen wir beim Verteilernetzbetreiber. Für Kärnten ist das die KNG-Kärnten Netz "
             "GmbH: Der Antrag läuft über ihr Kundenportal und kann von einem bevollmächtigten Elektriker oder "
             "Anlagenplaner gestellt werden. Eine Netzberechnung ergibt die maximale Einspeiseleistung an Ihrem "
             "Anschlusspunkt, danach folgt das Netzzutrittsangebot. Zugesichert wird laut Kärnten Netz mindestens "
             "eine Einspeiseleistung in Höhe Ihres Strombezugsrechts. Reicht das Ortsnetz für mehr nicht aus, kann "
             "die Anlage trotzdem in voller Größe gebaut und dynamisch geregelt werden: Der Verbrauch im Haus hat "
             "Vorrang, begrenzt wird nur der Überschuss. Deshalb fragen wir die mögliche Einspeiseleistung ab, bevor "
             "wir die Anlagengröße festlegen."),
            ("Eine Besonderheit im Bezirk: In Kötschach betreibt die AAE Wasserkraft GmbH ein eigenes regionales "
             "Verteilernetz mit rund 700 Zählpunkten, 550 Anschlussanlagen und zehn Trafostationen. Wer dort "
             "angeschlossen ist, beantragt den Netzanschluss der Erzeugungsanlage nicht bei Kärnten Netz, sondern bei "
             "AAE Wasserkraft in Kötschach 66. Welcher Netzbetreiber für Ihre Adresse zuständig ist, steht auf Ihrer "
             "Stromrechnung. Wir prüfen das beim ersten Termin und reichen die Unterlagen an der richtigen Stelle "
             "ein."),
        ],
        "bullets": [
            "Mitteilung an die Baubehörde der Stadtgemeinde vor Baubeginn, Vollendungsmeldung binnen zwei Wochen",
            "Kärnten Netz: Antrag im Kundenportal, Netzberechnung der Einspeiseleistung, Netzzutrittsangebot",
            "Kötschach: Netzanschluss über die AAE Wasserkraft GmbH",
            "Fertigstellungsmeldung durch den konzessionierten Elektriker, Abnahmevertrag mit einem Stromlieferanten Ihrer Wahl",
        ],
        "img": "gen_detail",
        "alt": ("Hände in Arbeitshandschuhen verschrauben mit dem Akkuschrauber eine Modulklemme auf der "
                "Aluminiumschiene einer Photovoltaikanlage (Symbolbild)"),
    },
    "waermepumpe": {
        "h2": "Wärmepumpe in Hermagor: erst die Fernwärme prüfen, dann mit Sonnenstrom heizen",
        "paragraphs": [
            ("Vor jedem Heizungstausch in Hermagor steht eine einfache Frage: Liegt das Haus an einem Wärmenetz? In "
             "der Stadt betreibt die KELAG Wärme GmbH ein Fernwärmenetz, das laut Fachverband Gas Wärme rund 120 "
             "Kunden mit Heizung und Warmwasser versorgt und von einem Biomassekessel mit 4 MW gespeist wird (Stand "
             "2016). In Kötschach, Mauthen und Würmlach gibt es laut e5-Auditbericht des Landes eigene Wärmenetze. "
             "Wo eine Leitung vor dem Haus liegt, lohnt zuerst die Anfrage beim Betreiber. Für die Häuser außerhalb "
             "dieser Netze, in den Dörfern und Streusiedlungen der Gemeinde, ist die Luft-Wasser-Wärmepumpe meist "
             "der naheliegende Ersatz für den alten Kessel."),
            ("Eine Luft-Wasser-Wärmepumpe kostet inklusive Montage rund 12.000 bis 22.000 Euro vor Förderung* und "
             "macht aus 1 kWh Strom 4 bis 5 kWh Wärme*. Im Bestand entscheidet die Vorlauftemperatur: Bis 55 Grad "
             "arbeitet das Gerät effizient, große alte Heizkörper reichen oft aus. In den umgebauten Hofgebäuden der "
             "Ortskerne sehen wir uns deshalb Heizflächen und Dämmung genau an, bevor wir ein Gerät empfehlen. Im "
             "Gailtal gehört auch der Aufstellort der Außeneinheit zur Planung: geschützt vor Dachlawinen und "
             "Schneeverwehungen und mit ausreichend Abstand zum Nachbarn."),
            ("Ehrlich gerechnet liefert das Dach im Winter am wenigsten, wenn die Heizung am meisten braucht. Eine "
             "10-kWp-Anlage am Süddach bringt in Hermagor im Dezember rund 390 kWh, im Juli rund 1.400 kWh (PVGIS)*. "
             "Warmwasser und Übergangszeit laufen damit weitgehend mit eigenem Strom, im Hochwinter deckt die Anlage "
             "nur einen Teil des Heizstroms. Darum planen wir Photovoltaik, Speicher und Wärmepumpe gemeinsam und "
             "nehmen Dach, Zählerschrank und Heizraum in einem Termin auf. Für Gästehäuser und Pensionen rund um den "
             "Pressegger See passt das Profil gut, weil die Badesaison in die ertragreichen Monate fällt."),
        ],
        "bullets": [
            "Zuerst klären: Fernwärme in Hermagor oder Wärmenetz in Kötschach-Mauthen am Grundstück verfügbar?",
            "Heizkörper, Vorlauftemperatur und Aufstellort der Außeneinheit bei einem Termin vor Ort geprüft",
            a("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau") + ": Heizkörper, Vorlauftemperatur, Dämmung",
        ],
        "img": "waermepumpe",
        "alt": "Außeneinheit einer Luft-Wasser-Wärmepumpe vor einer Holzwand im Garten (Symbolbild, nicht in Hermagor aufgenommen)",
    },
    "foerderung_h2": "Förderung in Hermagor: Land, Bund und was die Gemeinden beitragen",
    "foerderung_lokal": [
        ("Die Stadtgemeinde Hermagor-Pressegger See weist auf ihrer Website derzeit kein eigenes Förderprogramm für "
         "Photovoltaik, Speicher oder Heizungstausch aus (Stand Oktober 2026); wir fragen das vor dem Angebot beim "
         "Stadtamt nach. Anders in Kötschach-Mauthen: Dort nennt der e5-Auditbericht des Landes eine gemeindeeigene "
         "Förderung für Solaranlagen und Heizungsanlagen (Stand 2020). Ob und in welcher Höhe sie heute gilt, klären "
         "wir für Ihr Projekt mit dem Gemeindeamt."),
        ("Regionale Anlaufstelle für Energiefragen ist die Klima- und Energie-Modellregion Karnische Energie im Bezirk "
         "Hermagor. Wer Überschussstrom im Ort weitergeben möchte, kann sich die Erneuerbare Energiegemeinschaft "
         "Wulfenia ansehen, die die Stadtgemeinde mit sechs Betrieben gegründet hat und die laut Stadtgemeinde auch "
         "Haushalte aufnehmen will. Wie das Modell funktioniert, steht auf der Seite "
         + a("eg_privat", "Energiegemeinschaft für Private") + "."),
    ],
    "referenzen": {
        "h2": "Referenzen aus Kärnten: die nächstgelegenen Projekte",
        "intro": ("Die nächstgelegenen dokumentierten Referenzprojekte von EBZ Energie stehen im Raum Villach und am "
                  "Ossiacher See, nicht in Hermagor: ein Hotel in Warmbad mit Speicher und Notstrom, ein "
                  "Einfamilienhaus in Villach und ein Einfamilienhaus mit Wallbox am See."),
        "slugs": ["projekt-pv-anlage-hotel-villach", "projekt-einfamilienhaus-villach", "projekt-pv-am-ossiachersee"],
    },
    "umgebung": ["St. Stefan im Gailtal", "Gitschtal", "Kirchbach", "Dellach", "Kötschach-Mauthen", "Lesachtal",
                 "Weißensee", "Feistritz an der Gail"],
    "links": [
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau"),
        ("/notstrom/", "Notstrom mit Photovoltaik und Speicher"),
        ("/energiegemeinschaft-kaernten/", "Energiegemeinschaft in Kärnten"),
    ],
    "faq": [
        ("Wie viel Strom erzeugt eine Photovoltaikanlage in Hermagor?",
         "Für den Standort Hermagor rechnet PVGIS, das Photovoltaik-Informationssystem der EU-Kommission, mit rund "
         "1.185 kWh je kWp und Jahr am Süddach mit 30 Grad Neigung, mit rund 976 kWh am Ostdach und rund 943 kWh am "
         "Westdach. Eine 10-kWp-Anlage kommt damit auf rund 11.800 kWh bei Südausrichtung und auf rund 9.600 kWh bei "
         "Ost-West-Belegung. Die Abschattung durch das Gelände ist eingerechnet. Was Ihr Dach hergibt, steht im "
         "Projektbericht mit 3D-Belegplan und Statikreport."),
        ("Was kostet eine PV-Anlage mit Speicher in Hermagor?",
         "Eine Komplettanlage mit rund 10 kWp und Speicher kostet in Hermagor typischerweise rund 15.000 bis 22.000 "
         "Euro vor Förderung, inklusive Montage, Netzanmeldung und Inbetriebnahme. Davon gehen die Landespauschale "
         "Kärnten von 3.000 Euro und der Investitionszuschuss des Bundes ab. Die Stadtgemeinde Hermagor-Pressegger "
         "See weist derzeit kein eigenes Förderprogramm aus. Eine Finanzierung ist ab 147 Euro im Monat* möglich, "
         "die Anlage gehört Ihnen ab dem ersten Tag."),
        ("Wer ist in Hermagor und in Kötschach-Mauthen der Netzbetreiber für meine PV-Anlage?",
         "Verteilernetzbetreiber in Kärnten ist die KNG-Kärnten Netz GmbH, eine Tochter der Kelag; der Antrag läuft "
         "über ihr Kundenportal. In Kötschach betreibt die AAE Wasserkraft GmbH ein eigenes regionales Verteilernetz "
         "mit rund 700 Zählpunkten, dort geht der Antrag an AAE Wasserkraft. Welcher Netzbetreiber für Ihre Adresse "
         "zuständig ist, steht auf Ihrer Stromrechnung. Wir prüfen das beim ersten Termin und stellen den Antrag an "
         "der richtigen Stelle."),
        ("Brauche ich in Hermagor eine Baubewilligung für eine Photovoltaikanlage?",
         "In der Regel nicht. Nach § 7 Abs. 1 lit. a Z 20 der Kärntner Bauordnung sind Anlagen, die erneuerbare "
         "Energie erzeugen oder elektrische Energie speichern, mitteilungspflichtig: Die Baubehörde der Stadtgemeinde "
         "Hermagor-Pressegger See wird vor Beginn schriftlich informiert, die Vollendung ist binnen zwei Wochen zu "
         "melden. Flächenwidmung und Bebauungsplan gelten trotzdem. Sonderfälle wie die Ortsbildpflege klären wir "
         "vorab mit dem Bauamt am Wulfeniaplatz."),
        ("Lohnt sich Photovoltaik im Gailtal trotz Bergen und Schnee?",
         "Ja, aber die Planung muss den Standort abbilden. Die PVGIS-Werte für Hermagor enthalten die Abschattung "
         "durch das Gelände und liegen am Süddach trotzdem bei rund 1.185 kWh je kWp und Jahr. Der Unterschied "
         "zwischen den Jahreszeiten ist groß: rund 39 kWh je kWp im Dezember, rund 141 kWh im Juli. Deshalb legen "
         "wir Belegung und Speicher für Ihr Dach aus, und der Statikreport prüft die Unterkonstruktion auf die "
         "Schneelast am Standort."),
        ("Fernwärme oder Wärmepumpe in Hermagor: Was passt zu meinem Haus?",
         "Liegt Ihr Haus am Fernwärmenetz der KELAG Wärme in Hermagor, das laut Fachverband Gas Wärme rund 120 Kunden "
         "versorgt (Stand 2016), lohnt zuerst die Anfrage beim Betreiber. Außerhalb des Netzes ist die "
         "Luft-Wasser-Wärmepumpe meist die naheliegende Lösung: rund 12.000 bis 22.000 Euro vor Förderung, effizient "
         "bis 55 Grad Vorlauftemperatur. Wir prüfen Heizkörper, Dämmung und Aufstellort bei Ihnen vor Ort und sagen "
         "offen, wenn zuerst saniert werden sollte."),
        ("Reicht eine PV-Anlage in Hermagor für die Wärmepumpe im Winter?",
         "Nicht allein. Eine 10-kWp-Anlage am Süddach liefert in Hermagor im Dezember rund 390 kWh, im Juli rund "
         "1.400 kWh (PVGIS-Richtwerte). Ein Beispielhaus mit 12.000 kWh Wärmebedarf braucht bei Jahresarbeitszahl 4 "
         "rund 3.000 kWh Strom im Jahr, den größten Teil davon im Winter. Die Photovoltaik deckt Warmwasser und "
         "Übergangszeit weitgehend und senkt die Heizkosten über das Jahr deutlich, im Hochwinter kommt der Rest aus "
         "dem Netz."),
        ("Hat EBZ Energie einen Standort in Hermagor?",
         "Nein. EBZ Energie ist ein Fachbetrieb aus Villach, Firmensitz ist die Triglavstraße 15, 9500 Villach. Für "
         "die Erstberatung kommen wir zu Ihnen nach Hermagor, ins Gitschtal oder nach Kötschach-Mauthen und sehen "
         "uns Dach, Zählerschrank und Heizraum an. Zertifizierte Fachkräfte montieren die Anlage, ein fester "
         "Ansprechpartner begleitet Sie von der Planung bis zur Übergabe. Erreichbar sind wir Montag bis Freitag von "
         "10 bis 20 Uhr."),
    ],
    "quellen": [
        ("Statistik Austria: Ein Blick auf die Gemeinde Hermagor-Pressegger See, Bevölkerung",
         "https://www.statistik.at/blickgem/G0201/g20305.pdf"),
        ("Statistik Austria: Hermagor-Pressegger See, Fläche und Dauersiedlungsraum",
         "https://www.statistik.at/blickgem/G0101/g20305.pdf"),
        ("Statistik Austria: Hermagor-Pressegger See, land- und forstwirtschaftliche Betriebe",
         "https://www.statistik.at/blickgem/G0701/g20305.pdf"),
        ("Stadtgemeinde Hermagor-Pressegger See: Baubehörde und Hochbau",
         "https://hermagor.at/verwaltung/abteilungen/baubehoerde/"),
        ("Stadtgemeinde Hermagor-Pressegger See: Formulare (Bauanzeige, Ortsbildpflege)",
         "https://hermagor.at/buergerservice/downloads/formulare/"),
        ("Stadtgemeinde Hermagor-Pressegger See: Textlicher Bebauungsplan",
         "https://hermagor.at/fileadmin/Redakteure/Amtstafel/Hermagor_textlicher_Bbpl_gesamt_GR_06-2012.pdf"),
        ("Stadtgemeinde Hermagor-Pressegger See: Erneuerbare Energiegemeinschaft Wulfenia",
         "https://hermagor.at/fileadmin/user_upload/direct-uploads/EEG-050923.pdf"),
        ("Stadtgemeinde Hermagor-Pressegger See: Mitteilungsblatt Juni 2026 (KEM Karnische Energie)",
         "https://hermagor.at/fileadmin/user_upload/direct-uploads/MTB_JUNI_2026_Web.pdf"),
        ("Magistrat Villach: Formular Mitteilung nach § 7 Abs. 1 lit. a Z 20 Kärntner Bauordnung 1996",
         "https://villach.at/getmedia/fe3178f4-230a-4056-871d-d9412d2329ff/Mitteilung_P7_KBO1996.pdf.aspx"),
        ("Kärnten Netz: PV-Anlage anschließen", "https://www.kaerntennetz.at/pv.htm"),
        ("Kärnten Netz: Impressum (KNG-Kärnten Netz GmbH)", "https://www.kaerntennetz.at/impressum.htm"),
        ("AAE Wasserkraft GmbH: Verteilernetz Kötschach", "https://aae-wasserkraft.at/stromnetz/netze/"),
        ("AAE Wasserkraft GmbH: Stromanschluss", "https://aae-wasserkraft.at/stromnetz/stromanschluss/"),
        ("EU-Kommission, Joint Research Centre: PVGIS 5.3, Standort Hermagor", _PVGIS),
        ("Fachverband Gas Wärme: Biomasse-Heißwasserkessel und Fernwärmenetz in Hermagor",
         "https://www.fernwaerme.at/neuer-biomasse-heiswasserkessel-in-hermagor"),
        ("Amt der Kärntner Landesregierung, Abt. 8: e5-Audit-Bericht 2020 Kötschach-Mauthen",
         "https://cdn.citiesapps.com/pages/8ec89955280b06333deb5e56/page-file-system/1741594570253_e5_Audit-Bericht_Ktschach-Mauthen2020.pdf"),
        ("Land Kärnten: Regionalstrategie Region Hermagor",
         "https://kirchbach.gv.at/fileadmin/kirchbach/PDFs_allgemein/Regionalstrategie_Region_Hermagor_Land-Kaernten_Broschuere-Hermagor_.pdf"),
    ],
    "notizen": ("Faktenfragen an den Kunden: (1) Hat EBZ im Bezirk Hermagor schon Anlagen gebaut, die als Referenz "
                "genannt werden duerfen? (2) Faehrt EBZ fuer Montage und Service bis ins Lesachtal und auf das "
                "Nassfeld, oder gibt es eine Grenze? (3) Erfahrung mit Netzanschluessen bei AAE Wasserkraft "
                "(Koetschach)? (4) Montiert EBZ Waermepumpen im Bezirk selbst, und welche Geraete? "
                "Unsicher: Fernwaerme-Zahl (120 Kunden) stammt von 2016; Gemeindefoerderung Koetschach-Mauthen nur "
                "fuer 2020 belegt; adressgenaue Netzgebiete (KNG/AAE, evtl. weitere kleine Netze im Bezirk) nicht "
                "amtlich gemeindeweise belegt; RIS und ktn.gv.at waren nicht erreichbar (K-BO ueber Formular "
                "Magistrat Villach belegt)."),
}
