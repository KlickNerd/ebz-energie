"""Ortsseite Murtal (/photovoltaik-murtal/): Photovoltaik (Primaer) und Waermepumpe (Sekundaer) im Bezirk Murtal.

Briefing: build/seo/standort_murtal.json / .md (DataForSEO, Oesterreich/Deutsch, 10.10.2026).
Alle lokalen Angaben stammen aus Quellen, die am 10.10.2026 abgerufen wurden (Liste in ORT["quellen"]):

- Land Steiermark, Landesstatistik, Gemeindedatenblaetter Bezirk Murtal (aktualisiert 8.9.2026): 20 Gemeinden.
  Einwohner 1.1.2026 (eigene Summe der 20 Blaetter): 71.178. Wohngebaeude 2024 (eigene Summe): 20.173.
  Knittelfeld 12.792 EW / 645 m, Judenburg 9.441 / 737 m (4.988 Privathaushalte 2024), Fohnsdorf 7.656 / 738 m,
  Zeltweg 7.055 / 656 m, Spielberg 5.309 / 663 m, Weisskirchen 4.732 / 687 m, Obdach 3.764 / 868 m,
  Poels-Oberkurzheim 2.710 / 790 m, Kobenz 2.075 / 621 m (tiefstes Gemeindeamt), Seckau 851 m, Gaal 858 m,
  Poelstal 918 m, Pusterwald 1.072 m, Hohentauern 1.272 m (hoechstes Gemeindeamt). Seehoehe = Gemeindeamt.
- BH Murtal, Informationstafel: Sitz Judenburg (Kapellenweg 11), Standort Knittelfeld (Anton-Regner-Strasse 2),
  Bezirk seit 1.1.2012 aus Judenburg und Knittelfeld, 20 Gemeinden.
- Stadtwerke Judenburg AG, Seite Strom ("Fakten Stand 2025"): Versorgungsgebiet 460 km2, 307 Trafostationen,
  1.189 km Leitungen; Formulare Antrag Netzanschluss, Antrag Einspeiseanlagen/Energiespeicher,
  Fertigstellungsmeldung PV/Speicher/Ladestationen; Einspeisekapazitaet Umspannwerk Judenburg West: gebucht
  13.000 kVA, verfuegbar 0 kVA (Stand 1.10.2026, unverbindliche Momentaufnahme, Einzelfallbetrachtung).
  Seite Energie-Informationen: "Als Ihr Netzbetreiber sind wir fuer den sicheren Betrieb des Stromnetzes
  verantwortlich". Ausfuehrungsrichtlinie Niederspannungsanschluesse 02/2026, Kap. 7.2: Wirkleistungsvorgabe fuer
  Einspeiseanlagen 3,68 kVA bis unter 250 kVA ueber Rundsteuerempfaenger (Stufen 100/60/30/0 %).
- Energienetze Steiermark: Betriebsgebiet (Netzkarte Stromnetz.json, Punktpruefung der Ortszentren am 10.10.2026:
  im Gebiet Knittelfeld, Zeltweg, Spielberg, Kobenz, Seckau, St. Margarethen bei Knittelfeld, Gaal; nicht im
  Gebiet Judenburg, Poels, St. Peter ob Judenburg, Unzmarkt, Oberzeiring; Netzgrenze nahe am Ortskern in
  Fohnsdorf, Weisskirchen, Obdach). Freie Einspeisekapazitaeten (Stand 1.7.2026): Knittelfeld Ost gebucht 11,3 MW,
  verfuegbar 0,0 MW; Judenburg West gebucht 1,6 MW, verfuegbar 0,0 MW. Erzeugungsanlagen: Einspeiserportal,
  Einspeisezaehlpunkt, Netzanschlusskonzept 12 Monate + einmal 12 Monate, Wirkleistungsvorgabe 3,68 bis 250 kW
  ueber Kabel vom Wechselrichter zum Smart Meter.
- Land Steiermark: Stmk. Baugesetz inkl. Novelle LGBl. 20/2026 (Ausgabe April 2026): § 21 Abs. 1 Z 2 lit. o
  (PV auf Dach/Fassade meldepflichtig, Hoehe bis 3,50 m), Abs. 2 Z 2a (Batterie bis 20 kWh, bis 100 kWh mit
  Nachweis), Z 2b (Waermepumpe), Abs. 3 (Mitteilung vor Ausfuehrung an die Gemeinde; Waermepumpe: Datenblatt und
  Schall-Bestaetigung). Verfahrenshandbuch PV (Abt. 13, Stand August 2025): zustaendig ist die Standortgemeinde
  (Buergermeister); der Netzbetreiber legt die zulaessige Einspeisung fest. (RIS war nicht abrufbar: 503.)
- Fernwaerme: Stadtwerke Judenburg ("Seit 2012" Abwaerme Zellstoff Poels, 11 km Leitungen, "mehr als 15.000
  Haushalte im Murtal"); Presseaussendung zur Eroeffnung auf kommunikation.steiermark.at (18 km Leitung, rund 15.000 Haushalte in
  der Region Judenburg, Zeltweg und Aichdorf, Bioenergie Aichfeld GmbH); Stadtgemeinde Zeltweg (Kooperation mit
  der Bioenergie Waermeservice GmbH). Stadt Judenburg, Seite Energie: Anschluss 2011, e5 seit 2006, fuenf "e" 2017
  und 2021.
- Land Steiermark, Foerderungsrichtlinie "Tausch erneuerbar betriebener Heizungssysteme" 2026, Pkt. 4 und 8 e:
  keine Anschlussmoeglichkeit an Nah-/Fernwaerme, Ausnahme wirtschaftliche Unzumutbarkeit.
- Stadtgemeinde Zeltweg: Photovoltaikfoerderung einmalig 150 Euro (nur Privatpersonen, Anlage mit
  Einspeisezaehlpunkt, keine Balkonkraftwerke, Meldung an die Baubehoerde vor Antrag, kein Rechtsanspruch).
  Stadtgemeinde Judenburg, Seite Foerderungen: nur Land/Bund, Verweis auf die Energieagentur Obersteiermark als
  regionale Beratungs- und Einreichstelle. Stadtgemeinde Knittelfeld, Formularliste: kein Foerderansuchen fuer PV,
  Speicher oder Heizung (nur Formular fuer meldepflichtige Bauvorhaben nach § 21).
- Klima- und Energiefonds, KEM Murtal: alle 20 Gemeinden, 71.516 Einwohner laut Programmseite, Sitz
  Energieagentur Obersteiermark, Holzinnovationszentrum 1a, Zeltweg; Massnahmenpakete u. a. "Erhoehung des
  Eigenstromverbrauchs aus PV-Anlagen" und "Fernwaermeausbaupotential".
- GeoSphere Austria, Data Hub, Klima-Jahreswerte (klima-v2-1y), Station Zeltweg (ID 115, 678 m): eigene Mittelung
  der Jahreswerte 2016 bis 2025: Lufttemperatur 8,3 Grad, 136 Frosttage, 2.016 Sonnenstunden (2023 fehlt).
  Station Villach Stadt (ID 100): 92 Frosttage im selben Zeitraum.

Nicht belegt und deshalb weggelassen: Ertrag je kWp fuer das Murtal, Fernwaerme in Knittelfeld und Spielberg
(kein offizieller Beleg abrufbar), Gasnetz, Gemeindefoerderungen ausser Zeltweg, Zuordnung jeder einzelnen Gemeinde
zu einem Netzbetreiber, "inneralpines Becken" als Klimaaussage, Entfernungen und Fahrzeiten.
"""

from common import a

ORT = {
    "key": "pv_murtal",
    "name": "Murtal",
    "kurz": "Murtal",
    "ort_in": "im Murtal",
    "ort_nach": "ins Murtal",
    "area_name": "Bezirk Murtal",
    "land": "stmk",
    "title": "Photovoltaik im Murtal: PV-Anlage & Wärmepumpe | EBZ Energie",
    "description": ("PV-Anlage und Wärmepumpe im Murtal: Beratung vor Ort in Judenburg, Knittelfeld und Zeltweg. "
                    "10 kWp mit Speicher rund 15.000 bis 22.000 € vor Förderung."),
    "eyebrow": "Photovoltaik und Wärmepumpe im Murtal · Obersteiermark",
    "h1": "Photovoltaik im Murtal: PV-Anlage mit Speicher und Wärmepumpe von Judenburg bis Knittelfeld",
    "lead": ("EBZ Energie ist ein Fachbetrieb aus Villach. Wir planen und montieren Photovoltaik, Speicher und "
             "Wärmepumpe bei Ihnen vor Ort im Murtal, von Judenburg über Fohnsdorf und Zeltweg bis Knittelfeld und in "
             "die Seitentäler. Vor dem Angebot klären wir, was im Bezirk den Unterschied macht: welcher der zwei "
             "Netzbetreiber für Ihre Adresse zuständig ist, wie viel Sie einspeisen dürfen und ob Fernwärme vor Ihrem "
             "Haus liegt. Sie bekommen einen Projektbericht mit 3D-Belegplan und Statikreport und ein Fixangebot."),
    "badges": [
        ("15.000 bis 22.000 €", "10 kWp mit Speicher vor Förderung*"),
        ("2 Stromnetze", "Stadtwerke Judenburg und Energienetze Steiermark"),
        ("1 Ansprechpartner", "von der Planung bis zur Übergabe"),
    ],
    "hero_img": "gen_eigenheim",
    "hero_alt": ("Einfamilienhaus mit Photovoltaikanlage auf dem Satteldach vor einer Bergkulisse im Abendlicht "
                 "(Symbolbild, nicht im Murtal aufgenommen)"),

    "intro": {
        "h2": "Photovoltaik und Wärmepumpe im Murtal: zwei Stromnetze, knappe Einspeisung, viel Fernwärme",
        "paragraphs": [
            ("Der Bezirk Murtal besteht aus 20 Gemeinden mit zusammen rund 71.000 Einwohnern und rund 20.000 "
             "Wohngebäuden (Landesstatistik Steiermark, Einwohner 2026, Gebäude 2024). Rund sechs von zehn Menschen "
             "leben in den fünf größten Gemeinden im Aichfeld: Knittelfeld (12.792), Judenburg (9.441), Fohnsdorf "
             "(7.656), Zeltweg (7.055) und Spielberg (5.309). Der Rest verteilt sich auf Märkte und Dörfer in den "
             "Seitentälern, von Obdach und Weißkirchen bis Pölstal und Hohentauern."),
            ("Das Murtal liegt hoch und hat lange Winter. Die Gemeindeämter im Aichfeld stehen zwischen 645 m "
             "(Knittelfeld) und 738 m (Fohnsdorf) Seehöhe, in Hohentauern sind es 1.272 m. An der Station Zeltweg "
             "von GeoSphere Austria (678 m) gab es im Mittel der Jahre 2016 bis 2025 rund 136 Frosttage pro Jahr, "
             "bei uns in Villach waren es im selben Zeitraum rund 92. Gleichzeitig zählte die Station rund 2.000 "
             "Sonnenstunden im Jahr. Für Ihr Haus heißt das: viel Sonne für die "
             + a("photovoltaik", "Photovoltaikanlage") + ", aber eine Heizung, die für kalte Monate ausgelegt sein muss."),
            ("Drei Dinge unterscheiden eine Planung im Murtal von der in anderen Bezirken. Erstens das Netz: Rund um "
             "Judenburg betreibt die Stadtwerke Judenburg AG ein eigenes Verteilernetz, in Knittelfeld, Zeltweg und "
             "Spielberg ist die Energienetze Steiermark zuständig. Zweitens die Einspeisung: Beide Netzbetreiber "
             "weisen für ihre Umspannwerke in der Region derzeit keine freie Einspeisekapazität aus. Drittens die "
             "Wärme: Aus der Abwärme der Zellstoff Pöls werden laut Stadtwerken mehr als 15.000 Haushalte mit "
             "Fernwärme versorgt, die " + a("waermepumpe", "Wärmepumpe") + " ist deshalb nicht für jedes Haus die "
             "erste Wahl."),
            ("An der Rechnung für den eigenen Strom ändert das wenig, an der Auslegung viel. Eine Anlage mit rund "
             "10 kWp und " + a("batteriespeicher", "Speicher") + " kostet rund 15.000 bis 22.000 € vor Förderung*, "
             "senkt die Stromkosten um bis zu 85 %* und hat sich typischerweise nach 4 bis 6 Jahren bezahlt "
             "gemacht*. Im Murtal planen wir sie so, dass möglichst viel Strom im Haus bleibt."),
        ],
    },

    "lokal": {
        "h2": "Das Murtal auf einen Blick: Gemeinden, Netze, Fernwärme und Solarpotenzial",
        "intro": ("Diese Angaben prüfen wir, bevor wir für ein Haus im Bezirk Murtal planen. Sie stammen vom Land "
                  "Steiermark, den Netzbetreibern, den Stadtgemeinden und GeoSphere Austria (Quellen am Seitenende)."),
        "rows": [
            ("Bezirk",
             "Der Bezirk Murtal entstand am 1. Jänner 2012 aus den Bezirken Judenburg und Knittelfeld und umfasst "
             "20 Gemeinden. Die Bezirkshauptmannschaft hat ihren Sitz in Judenburg und einen zweiten Standort in "
             "Knittelfeld."),
            ("Einwohner und Gebäude",
             "Rund 71.000 Einwohner (1. Jänner 2026) und rund 20.000 Wohngebäude (2024), Summe der "
             "Gemeindedatenblätter der Landesstatistik. Größte Gemeinde ist Knittelfeld mit 12.792 Einwohnern."),
            ("Höhenlage",
             "Gemeindeämter zwischen 621 m (Kobenz) und 1.272 m (Hohentauern). Knittelfeld 645 m, Zeltweg 656 m, "
             "Spielberg 663 m, Judenburg 737 m, Fohnsdorf 738 m, Obdach 868 m."),
            ("Stromnetz",
             "Zwei Netzbetreiber: die Stadtwerke Judenburg AG (eigenes Verteilernetz mit 460 km² Versorgungsgebiet, "
             "307 Trafostationen und 1.189 km Leitungen) und die Energienetze Steiermark GmbH (laut Netzkarte unter "
             "anderem Knittelfeld, Zeltweg, Spielberg, Kobenz und Seckau). Welcher für Ihre Adresse gilt, steht auf "
             "Ihrer Stromrechnung."),
            ("Einspeisekapazität",
             "Umspannwerk Judenburg West: laut Stadtwerken 13.000 kVA gebucht, 0 kVA verfügbar (Stand Oktober 2026). "
             "Umspannwerk Knittelfeld Ost: laut Energienetze Steiermark 11,3 MW gebucht, 0,0 MW verfügbar (Stand Juli "
             "2026). Beide Werte sind unverbindliche Momentaufnahmen, jede Anlage wird einzeln geprüft."),
            ("Genehmigung",
             "Photovoltaik auf Dach oder Fassade ist nach § 21 Steiermärkisches Baugesetz meldepflichtig. Die "
             "Mitteilung geht vor der Ausführung schriftlich an die Gemeinde, in der das Haus steht."),
            ("Fernwärme",
             "Abwärme der Zellstoff Pöls: laut Stadtwerken Judenburg mehr als 15.000 Haushalte im Murtal. Die "
             "Presseaussendung zur Eröffnung nennt die Region Judenburg, Zeltweg und Aichdorf. In Zeltweg kooperiert die "
             "Stadtgemeinde mit der Bioenergie Wärmeservice GmbH."),
            ("Solarpotenzial",
             "Der Digitale Atlas Steiermark zeigt für Dachflächen die Eignung für Photovoltaik und Solarthermie. Über "
             "das SolarTool des Landes lässt sich das Potenzial einer Fläche als Bericht anfordern."),
            ("Klima- und Energie-Modellregion",
             "Alle 20 Gemeinden bilden die KEM Murtal. Ihr Büro ist die Energieagentur Obersteiermark im "
             "Holzinnovationszentrum in Zeltweg, die auch Energieberatung für Haushalte anbietet. Judenburg hält im "
             "e5-Programm seit 2017 die Höchstwertung von fünf e."),
        ],
    },

    "netz": {
        "h2": "Genehmigung und Netzanschluss im Murtal: Meldung an die Gemeinde, Antrag beim richtigen Netzbetreiber",
        "betreiber": "der Stadtwerke Judenburg AG oder der Energienetze Steiermark GmbH (je nach Adresse)",
        "paragraphs": [
            ("Für eine PV-Anlage am Haus brauchen Sie im Murtal in der Regel keine Baubewilligung. Nach § 21 des "
             "Steiermärkischen Baugesetzes (Fassung LGBl. Nr. 20/2026) sind Photovoltaikanlagen meldepflichtig, die "
             "auf Dach- oder Fassadenflächen angebracht oder in diese integriert werden und samt ihren Teilen nicht "
             "höher als 3,50 m sind. Der Batteriespeicher ist bis 20 kWh Energieinhalt ebenfalls meldepflichtig, bis "
             "100 kWh mit einem zusätzlichen Sicherheitsnachweis. Zuständig ist die Gemeinde, in der das Haus steht: "
             "Die Mitteilung nennt Grundstücksnummer, Lage am Grundstück und eine kurze Beschreibung. Knittelfeld "
             "stellt dafür ein Online-Formular bereit, Zeltweg ein eigenes Formblatt. Wir bereiten die Mitteilung "
             "für Sie vor."),
            ("Beim Netzanschluss kommt es auf die Adresse an. Im Netz der Stadtwerke Judenburg stellen wir den "
             "Antrag für Einspeiseanlagen und Energiespeicher online, nach der Montage folgt die "
             "Fertigstellungsmeldung für PV und Speicher. Sie ist zusammen mit dem unterschriebenen "
             "Netzzugangsvertrag die Voraussetzung für Zählermontage und Inbetriebnahme. Im Netz der Energienetze "
             "Steiermark führt der Weg über das Einspeiserportal: Einspeisezählpunkt ansuchen, danach startet die "
             "Netzbeurteilung von selbst. Das Netzanschlusskonzept gilt 12 Monate und lässt sich einmal um 12 Monate "
             "verlängern."),
            ("Der wichtigste Punkt im Murtal ist die Einspeisung. Die Stadtwerke Judenburg weisen für das "
             "Umspannwerk Judenburg West 0 kVA freie Kapazität aus, die Energienetze Steiermark für Knittelfeld Ost "
             "0,0 MW. Das sind unverbindliche Momentaufnahmen und kein Bescheid für Ihr Dach: Der Netzbetreiber "
             "prüft jede Anlage einzeln und legt fest, mit welcher Leistung sie einspeisen darf. Beide verlangen für "
             "Anlagen ab 3,68 kVA beziehungsweise 3,68 kW eine Wirkleistungsvorgabe, mit der sie die Einspeisung "
             "aus der Ferne drosseln oder abschalten können: die Stadtwerke über einen Rundsteuerempfänger mit den "
             "Stufen 100, 60, 30 und 0 Prozent, die Energienetze über ein Kabel vom Wechselrichter zum Smart "
             "Meter."),
            ("Wir legen die Anlage deshalb nicht auf maximale Einspeisung aus, sondern auf Ihren Verbrauch. Die "
             "Modulleistung darf größer sein als die zugesagte Einspeiseleistung, solange der Wechselrichter "
             "begrenzt. Speicher, Warmwasser, Wärmepumpe und Wallbox nehmen den Mittagsstrom ab, ein "
             + a("ems", "Energiemanagementsystem") + " steuert die Reihenfolge."),
        ],
        "bullets": [
            "PV auf Dach oder Fassade bis 3,50 m Höhe: meldepflichtig, Mitteilung an die Gemeinde vor Baubeginn",
            "Judenburg und Umgebung: Antrag bei der Stadtwerke Judenburg AG",
            "Knittelfeld, Zeltweg, Spielberg: Einspeiserportal der Energienetze Steiermark",
            "Einspeiseleistung legt der Netzbetreiber fest: Planung auf Eigenverbrauch mit Speicher",
        ],
        "img": "gen_detail",
        "alt": ("Monteur mit Arbeitshandschuhen verschraubt mit dem Akkuschrauber eine Modulklemme auf der "
                "Montageschiene einer Photovoltaikanlage (Symbolbild)"),
    },

    "waermepumpe": {
        "h2": "Wärmepumpe im Murtal: erst die Fernwärme prüfen, dann für lange Winter auslegen",
        "paragraphs": [
            ("Der Heizungstausch beginnt im Aichfeld mit einer Frage: Liegt eine Fernwärmeleitung vor Ihrem Haus? "
             "Seit 2012 wird die Abwärme der Zellstoff Pöls zum Heizen genutzt. Die Presseaussendung zur Eröffnung "
             "nennt 18 km Leitung und rund 15.000 Haushalte in der Region Judenburg, Zeltweg und Aichdorf, die "
             "Stadtwerke Judenburg sprechen heute von mehr als 15.000 Haushalten im Murtal. Zum Vergleich: Die "
             "Stadt Judenburg selbst zählt knapp 5.000 Privathaushalte. Wo die Leitung liegt, ist der Anschluss "
             "oft die naheliegende Lösung, und das sagen wir Ihnen auch so."),
            ("Die Wärmepumpe ist die richtige Wahl, wo die Fernwärme nicht hinkommt: in den Siedlungen am Rand der "
             "Städte und in den höher gelegenen Gemeinden wie Obdach (868 m), Seckau (851 m), Gaal (858 m) oder "
             "Pölstal (918 m). Bei rund 136 Frosttagen im Jahr an der Station Zeltweg rechnen wir die Heizlast "
             "Raum für Raum und prüfen die Vorlauftemperatur: Kommen Ihre Heizkörper mit bis zu 55 Grad aus, "
             "arbeitet eine Luft-Wasser-Wärmepumpe effizient, die Geräte laufen bis minus 20 Grad. Sie kostet im "
             "Einfamilienhaus rund 12.000 bis 22.000 € vor Förderung*, im Altbau mit Anpassungen rund 15.000 bis "
             "28.000 €*."),
            ("Zwei Punkte klären wir vor dem Angebot. Baurecht: Die ortsfeste Aufstellung einer Wärmepumpe ist in "
             "der Steiermark meldepflichtig. Der Mitteilung an die Gemeinde liegen das technische Datenblatt und die "
             "Bestätigung eines Sachverständigen bei, dass der zulässige Schallpegel an der Grundgrenze eingehalten "
             "wird. Fernwärme: Die Richtlinie des Landes für den Tausch mindestens 15 Jahre alter Biomassekessel und "
             "Wärmepumpen setzt voraus, dass für das Haus kein Anschluss an ein Nah- oder Fernwärmenetz möglich ist, "
             "außer er ist wirtschaftlich nicht zumutbar. In Judenburg und Zeltweg fragen wir deshalb zuerst beim "
             "Fernwärmebetreiber nach."),
            ("Mit Photovoltaik passt die Wärmepumpe im Murtal besonders gut zusammen, gerade weil die Einspeisung "
             "begrenzt sein kann: Sie nimmt den Strom ab, den das Netz nicht aufnimmt. In der Übergangszeit und an "
             "klaren Wintertagen lädt sie Puffer und Warmwasser zu Mittag, wenn das Dach liefert."),
        ],
        "bullets": [
            "Zuerst klären: Fernwärme aus Pöls vor dem Haus, ja oder nein",
            "Auslegung auf die Heizlast Ihrer Lage: Gemeindeämter zwischen 621 und 1.272 m Seehöhe",
            "Wärmepumpe in der Steiermark meldepflichtig, mit Schallnachweis für die Grundgrenze",
        ],
        "img": "waermepumpe",
        "alt": ("Außeneinheit einer Luft-Wasser-Wärmepumpe mit zwei Ventilatoren vor einer Holzwand im Garten "
                "(Symbolbild, nicht im Murtal aufgenommen)"),
    },

    "foerderung_h2": "Förderung für Photovoltaik und Wärmepumpe im Murtal",
    "foerderung_lokal": [
        ("Im Bezirk zahlt die Stadtgemeinde Zeltweg einen eigenen Zuschuss: einmalig 150 Euro für eine "
         "Photovoltaikanlage auf dem Wohnhaus, einem Nebengebäude oder Carport. Gefördert werden Privatpersonen und "
         "nur Anlagen mit Einspeisezählpunkt, Balkonkraftwerke sind ausgenommen. Die Anlage muss vor dem Antrag der "
         "Baubehörde gemeldet sein, einen Rechtsanspruch gibt es nicht. Die Stadtgemeinde Judenburg führt auf ihrer "
         "Förderseite derzeit nur die Programme von Land und Bund, und in der Formularliste der Stadtgemeinde "
         "Knittelfeld findet sich kein Ansuchen für PV, Speicher oder Heizung. Für jede andere Gemeinde fragen wir "
         "vor dem Angebot nach."),
        ("Unabhängige Beratung gibt es vor Ort: Judenburg nennt die Energieagentur Obersteiermark in Zeltweg als "
         "regionale Beratungs- und Einreichstelle für Förderungen. Sie betreut auch die Klima- und "
         "Energie-Modellregion Murtal, die den Eigenverbrauch aus PV-Anlagen und den Fernwärmeausbau als eigene "
         "Maßnahmen führt. Wer Strom mit Nachbarn teilen will, findet die Grundlagen im Ratgeber "
         + a("/energiegemeinschaft-steiermark/", "Energiegemeinschaft in der Steiermark") + "."),
    ],

    "referenzen": {
        "h2": "Referenzen mit Zahlen: zwei Projekte in Graz, ein Einfamilienhaus in Villach",
        "intro": ("Aus dem Bezirk Murtal ist auf unserer Referenzseite noch kein Projekt mit Zahlen dokumentiert, "
                  "deshalb zeigen wir hier keines. Die beiden steirischen Anlagen stehen in Graz, das Einfamilienhaus "
                  "mit Satteldach und Notstrom steht in Villach."),
        "slugs": ["projekt-flachdach-in-graz", "projekt-stadthaus-in-graz", "projekt-einfamilienhaus-villach"],
    },

    "umgebung": ["Judenburg", "Knittelfeld", "Zeltweg", "Fohnsdorf", "Spielberg", "Weißkirchen in Steiermark",
                 "Pöls-Oberkurzheim", "Obdach", "Kobenz", "Seckau", "Sankt Margarethen bei Knittelfeld", "Lobmingtal"],

    "links": [
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau"),
        ("/einspeisetarif-fuer-photovoltaik/", "Einspeisetarif für Photovoltaik"),
        ("/energiegemeinschaft-steiermark/", "Energiegemeinschaft in der Steiermark"),
    ],

    "faq": [
        ("Wer ist im Murtal der Stromnetzbetreiber für meine Photovoltaikanlage?",
         "Das hängt von der Adresse ab. Rund um Judenburg betreibt die Stadtwerke Judenburg AG ein eigenes "
         "Verteilernetz mit 460 Quadratkilometern Versorgungsgebiet. In Knittelfeld, Zeltweg, Spielberg, Kobenz und "
         "Seckau ist laut Netzkarte die Energienetze Steiermark GmbH zuständig. In Gemeinden an der Netzgrenze, etwa "
         "Fohnsdorf, Weißkirchen oder Obdach, entscheidet die genaue Adresse. Der Netzbetreiber steht auf Ihrer "
         "Stromrechnung, wir klären ihn im ersten Gespräch und stellen den Antrag für Sie."),
        ("Kann ich im Murtal noch einspeisen, wenn die Umspannwerke ausgebucht sind?",
         "Für das Umspannwerk Judenburg West weisen die Stadtwerke Judenburg 0 kVA freie Einspeisekapazität aus "
         "(Stand Oktober 2026), die Energienetze Steiermark für Knittelfeld Ost 0,0 MW (Stand Juli 2026). Beide "
         "nennen die Werte unverbindliche Momentaufnahmen. Über Ihre Anlage entscheidet die Einzelfallprüfung nach "
         "dem Antrag: Der Netzbetreiber legt fest, mit welcher Leistung Sie einspeisen dürfen. Wir planen deshalb "
         "auf Eigenverbrauch mit Speicher, damit sich die Anlage auch bei begrenzter Einspeisung rechnet."),
        ("Brauche ich im Murtal eine Baubewilligung für eine Photovoltaikanlage?",
         "In der Regel nicht. Nach § 21 des Steiermärkischen Baugesetzes sind PV-Anlagen auf Dach- oder "
         "Fassadenflächen meldepflichtig, solange sie samt ihren Teilen nicht höher als 3,50 Meter sind. Sie teilen "
         "das Vorhaben vor der Ausführung schriftlich Ihrer Gemeinde mit, etwa Judenburg, Knittelfeld, Zeltweg oder "
         "Fohnsdorf, mit Grundstücksnummer, Lage und kurzer Beschreibung. Ein Batteriespeicher bis 20 kWh ist "
         "ebenfalls meldepflichtig. Die Mitteilung bereiten wir vor."),
        ("Was kostet eine Photovoltaikanlage im Murtal?",
         "Eine Anlage mit rund 10 kWp und Speicher kostet typischerweise rund 15.000 bis 22.000 Euro vor Förderung, "
         "inklusive Montage, Netzanmeldung und Inbetriebnahme (EBZ-Richtpreis, Stand Oktober 2026). Die Steiermark "
         "zahlt keine PV-Landespauschale, es gilt der Investitionszuschuss des Bundes. In Zeltweg kommt ein "
         "Zuschuss der Stadtgemeinde von 150 Euro dazu. Den Fixpreis für Ihr Haus in Judenburg, Knittelfeld oder "
         "einem der Seitentäler nennen wir nach der Besichtigung vor Ort."),
        ("Fernwärme oder Wärmepumpe in Judenburg und Zeltweg: was passt besser?",
         "Im Aichfeld gibt es Fernwärme aus der Abwärme der Zellstoff Pöls, laut Stadtwerken Judenburg für mehr als "
         "15.000 Haushalte im Murtal. Liegt eine Leitung vor Ihrem Haus, ist der Anschluss oft die naheliegende "
         "Lösung, und Photovoltaik senkt dann Ihre Stromrechnung. Die Wärmepumpe passt dort, wo keine Fernwärme "
         "erreichbar ist, etwa am Siedlungsrand und in den Seitentälern. Wir fragen den Anschluss vor dem Angebot "
         "beim Fernwärmebetreiber ab."),
        ("Funktioniert eine Luft-Wasser-Wärmepumpe im Murtaler Winter?",
         "Ja, wenn sie richtig ausgelegt ist. An der GeoSphere-Station Zeltweg auf 678 Metern gab es im Mittel der "
         "Jahre 2016 bis 2025 rund 136 Frosttage pro Jahr. Luft-Wasser-Wärmepumpen arbeiten bis minus 20 Grad. "
         "Entscheidend ist die Vorlauftemperatur: Kommen Ihre Heizkörper mit bis zu 55 Grad aus, läuft das Gerät "
         "effizient. In Obdach, Seckau oder Pölstal rechnen wir die Heizlast für die höhere Lage und sagen offen, "
         "wenn zuerst Fenster oder Dämmung dran sind."),
        ("Gibt es in Judenburg, Knittelfeld oder Zeltweg eine Gemeindeförderung für Photovoltaik?",
         "Zeltweg zahlt einmalig 150 Euro für eine Photovoltaikanlage von Privatpersonen, wenn die Anlage einen "
         "Einspeisezählpunkt hat und vorher der Baubehörde gemeldet wurde. Balkonkraftwerke sind ausgenommen, ein "
         "Rechtsanspruch besteht nicht. Die Stadtgemeinde Judenburg nennt auf ihrer Förderseite derzeit nur Land und "
         "Bund und verweist auf die Energieagentur Obersteiermark in Zeltweg. Für Knittelfeld und die anderen "
         "Gemeinden im Bezirk prüfen wir den Stand vor jedem Angebot."),
        ("Kommt EBZ Energie aus Villach auch ins Murtal?",
         "Ja. Unser Firmensitz ist die Triglavstraße 15 in Villach, einen Standort im Murtal haben wir nicht. "
         "Montiert wird in Kärnten und der Steiermark, zur Erstberatung kommen wir zu Ihnen nach Judenburg, "
         "Knittelfeld, Zeltweg, Fohnsdorf, Spielberg oder in die Seitentäler. Dach, Zählerschrank und Heizraum sehen "
         "wir uns vor Ort an. Zertifizierte Fachkräfte montieren, ein fester Ansprechpartner begleitet Sie von der "
         "Planung bis zur Übergabe."),
    ],

    "quellen": [
        ("Land Steiermark, Landesstatistik: Gemeindedaten Bezirk Murtal (Einwohner, Seehöhe, Gebäude)",
         "https://www.landesentwicklung.steiermark.at/cms/beitrag/12256487/141979478/"),
        ("Bezirkshauptmannschaft Murtal: Informationstafel zur Bezirksverwaltung",
         "https://www.bh-murtal.steiermark.at/cms/dokumente/12671783_58174087/64f910e3/Bezirksverwaltung%20BH%20Murtal_Informationstafel.pdf"),
        ("Stadtwerke Judenburg AG: Strom, Verteilernetz und Einspeisekapazitäten",
         "https://stadtwerke.co.at/versorgung/strom/"),
        ("Stadtwerke Judenburg AG: Ausführungsrichtlinie für Niederspannungsanschlüsse (Februar 2026)",
         "https://stadtwerke.co.at/wp-content/uploads/2026/02/Ausfuehrungsrichtlinie-fuer-Niederspannungsanschluesse_2026.02.pdf"),
        ("Stadtwerke Judenburg AG: Fernwärme aus Abwärme der Zellstoff Pöls",
         "https://stadtwerke.co.at/versorgung/fernwaerme/"),
        ("Energienetze Steiermark: Betriebsgebiet Stromnetz (Netzkarte)",
         "https://www.e-netze.at/Unternehmen/Betriebsgebiet.aspx"),
        ("Energienetze Steiermark: Erzeugungsanlagen und Netzzugang",
         "https://www.e-netze.at/Strom/Erzeugungsanlagen/Default.aspx"),
        ("Energienetze Steiermark: Freie Einspeisekapazitäten je Umspannwerk",
         "https://www.e-netze.at/Service/FEK/Default.aspx"),
        ("Land Steiermark: Steiermärkisches Baugesetz in der Fassung LGBl. Nr. 20/2026 (§ 21)",
         "https://www.technik.steiermark.at/cms/dokumente/11549819_58813874/dadceab4/Baugesetz_idF_LGBl_20_2026.pdf"),
        ("Land Steiermark: Verfahrenshandbuch Photovoltaik- und Solarthermieanlagen",
         "https://www.verwaltung.steiermark.at/cms/dokumente/12898224_173036325/f51050a9/Verfahrenshandbuch%20Erneuerbare%20Energie%20PV%20und%20Solaranlagen.pdf"),
        ("Land Steiermark, Kommunikation: Presseaussendung Aus Abwärme wird Fernwärme (Zellstoff Pöls)",
         "https://kommunikation.steiermark.at/cms/dokumente/11697623_29767960/78757df9/Ja_PresseaussendungZellstoffP%C3%B6lz.pdf"),
        ("Stadtgemeinde Zeltweg: Fernwärme in Zeltweg",
         "https://zeltweg.at/de/umwelt_und_energie/Fernwaerme_in_Zeltweg.asp"),
        ("Stadtgemeinde Zeltweg: Photovoltaikförderung",
         "https://zeltweg.at/de/verwaltung/Foerderung_Photovoltaikanlage.asp"),
        ("Stadtgemeinde Judenburg: Umweltförderungen",
         "https://www.judenburg.at/de/umwelt/Neue_Solarfoerderung.asp"),
        ("Stadtgemeinde Judenburg: e5-Programm",
         "https://www.judenburg.at/de/umwelt/e5-Programm.asp"),
        ("Stadtgemeinde Knittelfeld: Formulare (meldepflichtige Bauvorhaben nach § 21)",
         "https://knittelfeld.gv.at/leben-in-knittelfeld/formulare"),
        ("Land Steiermark: Förderungsrichtlinie Tausch erneuerbar betriebener Heizungssysteme 2026",
         "https://www.wohnbau.steiermark.at/cms/dokumente/13000784_183599709/c26463e2/2026_F%C3%B6rderungsrichtlinie%20Tausch%20erneuerbar%20betriebener%20Heizungssysteme.pdf"),
        ("Klima- und Energiefonds: Klima- und Energie-Modellregion Murtal",
         "https://orte-von-morgen.at/ort/kem-murtal/"),
        ("GeoSphere Austria, Data Hub: Klimadaten Jahreswerte, Stationen Zeltweg und Villach Stadt",
         "https://data.hub.geosphere.at/dataset/klima-v2-1y"),
        ("Land Steiermark: Solarpotenzial und SolarTool im Digitalen Atlas",
         "https://landesentwicklung.steiermark.at/cms/beitrag/12910759/145230171"),
    ],

    "notizen": (
        "Faktenfragen fuer den Kunden: (1) Gibt es EBZ-Anlagen im Bezirk Murtal, die als Referenz dokumentiert "
        "werden koennen? (2) Erfahrungen mit Netzzusagen der Stadtwerke Judenburg und der Energienetze Steiermark "
        "im Murtal: welche Einspeiseleistung wird fuer Einfamilienhaeuser derzeit zugesagt? (3) Netzbetreiber in "
        "Fohnsdorf, Poels-Oberkurzheim, St. Peter ob Judenburg, Unzmarkt-Frauenburg und Poelstal: laut Netzkarte "
        "nicht Energienetze Steiermark; Stadtwerke Judenburg oder ein weiteres Netz? (4) Fernwaerme in Knittelfeld, "
        "Spielberg und Fohnsdorf: Betreiber und Gebiet (kein offizieller Beleg abrufbar). (5) Montiert EBZ "
        "Waermepumpen im Murtal selbst oder nur in Kombination mit PV? "
        "Unsicherheiten: Klimawerte sind eigene Mittel aus GeoSphere-Jahreswerten (kein amtliches Klimamittel); "
        "Einwohner- und Gebaeudesumme sind eigene Summen der 20 Gemeindeblaetter; die Zuordnung der Orte zum Netz "
        "der Energienetze stammt aus einer Punktpruefung der Ortszentren gegen die veroeffentlichte Netzkarte."
    ),
}
