"""Ortsseite Leoben (/photovoltaik-leoben/): Photovoltaik (Primaer) und Waermepumpe (Sekundaer).

Briefing: build/seo/standort_leoben.json / .md (DataForSEO, Oesterreich/Deutsch, 10.10.2026).
Alle lokalen Angaben stammen aus Quellen, die am 10.10.2026 abgerufen wurden (Liste in ORT["quellen"]):

- Stadt Leoben, Gemeindestatistik (Stand 1.9.2026): 27.937 Einwohner gesamt, 24.307 Hauptwohnsitze, 13.456 Haushalte,
  107,77 km2, 78,69 % Wald, durchschnittliche Seehoehe 540 m, zehn Katastralgemeinden.
- Stadt Leoben, "Leben in Leoben": "zweitgroesste Stadt der Steiermark", "im Herzen der Obersteiermark", an der Mur.
- Stadt Leoben, Foerderungen fuer alternative Heiz- und Energiesysteme: Programm (Solar, PV, Biomasse, Waermepumpe)
  ruht, "bis auf Weiteres" keine Ausschuettung, kein Rechtsanspruch. (Antragsschluss 31.10.2025 steht auf der Seite,
  hier bewusst nicht genannt: keine Fristen auf Standortseiten.)
- Stadt Leoben, Ortsbildkonzept II (2.0) vom 11.7.1996, Aenderung "Solar" rechtskraeftig 16.7.2010: Ortsbildschutzgebiet
  laut Verordnung LGBl. 51/1989; § 2 (Bewilligungspflicht auch fuer nach BauG bewilligungsfreie Vorhaben), § 4
  (mittelalterliche Stadt), § 7 (Sonnenkollektoren: nicht auf Dachflaechen in mittelalterlicher Stadt und Schutzgebiet 2
  Goess; uebrige Schutzgebiete nur, wenn von oeffentlichen Verkehrsflaechen nicht einsehbar). Der Text nennt
  "Sonnenkollektoren", § 16 traegt "Solar- und Photovoltaikanlagen" nur in der Ueberschrift: Anwendung auf PV-Module
  deshalb als Klaerung mit der Baubehoerde formuliert, nicht als Verbot.
- Stadtwerke Leoben: Geschaeftsbereiche Haustechnik, Gas, Wasser, Stadtwaerme, Glasfaser, Verkehr (kein Strom).
  Stadtwaerme: Abwaerme voestalpine Donawitz seit 2009, 48 MW thermisch, Ausbau auf 68 MW vorgesehen, 111,4 GWh/Jahr,
  erschlossen Donawitz, Innere Stadt, Judendorf, Leitendorf, Goess; Anschluss ueblicherweise rund 150 EUR/kW,
  Wirtschaftlichkeit je Anschluss geprueft. Gasnetz der Stadtwerke im Stadtgebiet.
- Energienetze Steiermark: Ablauf Erzeugungsanlagen (Einspeiserportal, Einspeisezaehlpunkt, Netzanschlusskonzept
  12 Monate + einmal 12 Monate, Installationsdokument, Wirkleistungsvorgabe 3,68 bis 250 kW seit 1.12.2024) und
  freie Einspeisekapazitaeten je Umspannwerk (Stand 1.7.2026: Hessenberg 0,0 MW, Leoben West 8,4 MW verfuegbar).
- Stadtwerke Trofaiach: eigenes Strom-Verteilernetz (6.656 Abnehmeranlagen, 55 Trafostationen), Antrag auf Netzzutritt.
- Stmk. Baugesetz idF LGBl. 20/2026 (Ausgabe Land Steiermark, April 2026): § 21 Abs. 1 Z 2 lit. o (PV auf Dach/Fassade
  meldepflichtig, Hoehe bis 3,50 m), § 20 Z 2 lit. l (ueber 3,50 m vereinfachtes Verfahren), § 21 Abs. 2 Z 2a
  (Batterie bis 20 kWh, bis 100 kWh mit Nachweis), Z 2b (Waermepumpe, Datenblatt + Schallbestaetigung), Abs. 3
  (Mitteilung an die Gemeinde vor Ausfuehrung).
- Land Steiermark, Foerderungsrichtlinie "Tausch erneuerbar betriebener Heizungssysteme" 2026, Pkt. 4 und 8 e:
  keine Anschlussmoeglichkeit an Nah-/Fernwaerme, Ausnahme wirtschaftliche Unzumutbarkeit (mind. 25 % guenstiger),
  Bestaetigung des Fernwaermeunternehmens (Pkt. 10.1 d).
- BH Leoben: 16 Gemeinden (3 Staedte, 8 Marktgemeinden, 5 Gemeinden). KEM Murraum Leoben: Leoben, Trofaiach,
  St. Michael, St. Peter-Freienstein, Traboch (Proleb nur auf der Programmseite genannt, deshalb nicht aufgezaehlt).
- Land Steiermark: Solarpotenzial im Digitalen Atlas und SolarTool (ABT 15 und ABT 17).

Nicht belegt und deshalb weggelassen: Ertrag je kWp und Sonnenstunden fuer Leoben, Zahl der PV-Anlagen (nur PV-Atlas,
keine amtliche Quelle), Trassenlaenge und Kundenzahl der Stadtwaerme, Fernwaermeanschlussbereich per Verordnung,
Gemeindefoerderungen der Umlandgemeinden, Entfernungen und Fahrzeiten.
"""

from common import a

ORT = {
    "key": "pv_leoben",
    "name": "Leoben",
    "kurz": "Leoben",
    "area_name": "Bezirk Leoben",
    "land": "stmk",
    "title": "Photovoltaik Leoben & Wärmepumpe: PV mit Speicher | EBZ",
    "description": ("Photovoltaik und Wärmepumpe in Leoben und Trofaiach: Fachbetrieb aus Villach, Beratung vor Ort. "
                    "10 kWp mit Speicher rund 15.000 bis 22.000 € vor Förderung."),
    "eyebrow": "Photovoltaik und Wärmepumpe Leoben · Obersteiermark",
    "h1": "Photovoltaik in Leoben: PV-Anlage mit Speicher und Wärmepumpe vom Fachbetrieb",
    "lead": ("EBZ Energie ist ein Fachbetrieb aus Villach und plant Photovoltaik, Speicher und Wärmepumpe bei Ihnen vor "
             "Ort in Leoben, von Donawitz bis Göss und im Umland von Trofaiach bis St. Michael. Vor dem Angebot klären "
             "wir, was in Leoben den Unterschied macht: Stadtwärme oder Wärmepumpe, Ortsbildschutz, Netzanschluss. "
             "Sie bekommen einen Projektbericht mit 3D-Belegplan und Statikreport und ein Fixangebot."),
    "badges": [
        ("15.000 bis 22.000 €", "10 kWp mit Speicher vor Förderung*"),
        ("Meldung statt Bewilligung", "für PV am Dach laut Stmk. Baugesetz"),
        ("1 Ansprechpartner", "von der Planung bis zur Übergabe"),
    ],
    "hero_img": "gen_hero",
    "hero_alt": "Photovoltaikmodule auf einem dunklen Ziegeldach vor blauem Himmel (Symbolbild, nicht in Leoben aufgenommen)",
    "kpis": [
        ("bis zu 85 %", "weniger Stromkosten mit PV und Speicher*"),
        ("4 bis 6 Jahre", "typische Amortisation*"),
        ("300+", "dokumentierte Projekte in 6 Bundesländern"),
        ("4,9", "Sterne auf Google"),
    ],

    "intro": {
        "h2": "Photovoltaik und Wärmepumpe in Leoben: was hier anders ist als anderswo",
        "paragraphs": [
            ("Leoben liegt an der Mur im Herzen der Obersteiermark und ist nach Angaben der Stadt die zweitgrößte "
             "Stadt der Steiermark. Das Stadtgebiet umfasst 107,77 km², davon sind rund 79 % Wald, die "
             "durchschnittliche Seehöhe liegt bei 540 m. Zwischen Donawitz und Göß stehen 13.456 Haushalte "
             "(Gemeindestatistik der Stadt, Stand September 2026): Altstadthäuser im Murbogen, Wohnanlagen, "
             "Reihenhäuser und Einfamilienhäuser an den Hängen und in den Gräben."),
            ("Drei Dinge unterscheiden eine Planung in Leoben von der in anderen Orten. Erstens die Wärme: Die "
             "Stadtwerke Leoben liefern Stadtwärme aus der Abwärme der voestalpine in Donawitz, deshalb ist die "
             + a("waermepumpe", "Wärmepumpe") + " hier nicht für jedes Haus die erste Wahl. Zweitens das Ortsbild: "
             "Für die Altstadt und für Göss gilt ein Ortsbildkonzept mit eigenen Regeln für Dächer. Drittens das "
             "Netz: In der Stadt ist die Energienetze Steiermark zuständig, im benachbarten Trofaiach betreiben die "
             "Stadtwerke Trofaiach ein eigenes Stromnetz."),
            ("Eigener Strom rechnet sich unabhängig davon, womit Sie heizen. Eine " + a("photovoltaik", "Photovoltaikanlage")
             + " mit rund 10 kWp und " + a("batteriespeicher", "Speicher") + " kostet rund 15.000 bis 22.000 € vor "
             "Förderung*, senkt die Stromkosten um bis zu 85 %* und hat sich typischerweise nach 4 bis 6 Jahren "
             "bezahlt gemacht*. Was auf Ihrem Dach in Leoben möglich ist, sehen wir uns vor Ort an."),
        ],
    },

    "lokal": {
        "h2": "Leoben auf einen Blick: Behörde, Netze, Wärme und Solarpotenzial",
        "intro": ("Diese Angaben prüfen wir, bevor wir für ein Haus in Leoben planen. Sie stammen von der Stadt, den "
                  "Stadtwerken, den Netzbetreibern und dem Land Steiermark (Quellen am Seitenende)."),
        "rows": [
            ("Stadt und Bezirk",
             "Leoben ist Bezirkshauptstadt. Zum Bezirk Leoben gehören 16 Gemeinden: die Städte Eisenerz, Leoben und "
             "Trofaiach, acht Marktgemeinden und fünf weitere Gemeinden."),
            ("Stadtgebiet",
             "107,77 km², rund 79 % Wald, durchschnittliche Seehöhe 540 m. Zehn Katastralgemeinden: Donawitz, Göß, "
             "Gößgraben-Göß, Judendorf, Leitendorf, Leoben, Mühltal, Prettach, Schladnitzgraben und Waasen."),
            ("Stromnetz",
             "In Leoben die Energienetze Steiermark GmbH (Anmeldung über das Einspeiserportal). Die Stadtwerke Leoben "
             "sind für Gas, Wasser und Stadtwärme zuständig, nicht für das Stromnetz. In Trofaiach betreiben die "
             "Stadtwerke Trofaiach ein eigenes Verteilernetz."),
            ("Genehmigung",
             "Photovoltaik auf Dach oder Fassade ist nach § 21 Steiermärkisches Baugesetz meldepflichtig. Die "
             "Mitteilung geht vor Baubeginn schriftlich an die Stadtgemeinde Leoben."),
            ("Ortsbildschutz",
             "Im Ortsbildschutzgebiet gilt das Ortsbildkonzept II (2.0) der Stadt, mit besonderen Vorschriften für "
             "die mittelalterliche Stadt und das Schutzgebiet Göss. Dort klären wir jedes Dach vorab mit der Baubehörde."),
            ("Stadtwärme und Gas",
             "Stadtwärme der Stadtwerke Leoben aus Abwärme der voestalpine Donawitz: derzeit 48 MW thermische "
             "Leistung, erschlossen sind Donawitz, Innere Stadt, Judendorf, Leitendorf und Göss. Im Stadtgebiet "
             "betreiben die Stadtwerke außerdem das Gasnetz."),
            ("Solarpotenzial",
             "Der Digitale Atlas Steiermark zeigt für Dachflächen die Eignung für Photovoltaik und Solarthermie. Über "
             "das SolarTool des Landes lässt sich das Potenzial einer Fläche als Bericht anfordern."),
            ("Klima- und Energie-Modellregion",
             "Leoben bildet mit Trofaiach, St. Michael in Obersteiermark, St. Peter-Freienstein und Traboch die KEM "
             "Murraum Leoben. Zu ihren Maßnahmen gehören der PV-Ausbau und Energiegemeinschaften."),
        ],
    },

    "netz": {
        "h2": "Genehmigung und Netzanschluss in Leoben: Meldung an die Stadt, Antrag beim Netzbetreiber",
        "betreiber": "der Energienetze Steiermark GmbH (in Trofaiach bei den Stadtwerken Trofaiach)",
        "paragraphs": [
            ("Für eine PV-Anlage am Haus brauchen Sie in Leoben in der Regel keine Baubewilligung. Nach § 21 des "
             "Steiermärkischen Baugesetzes (Fassung LGBl. Nr. 20/2026) sind Photovoltaikanlagen meldepflichtig, die "
             "auf Dach- oder Fassadenflächen angebracht oder in diese integriert werden und samt ihren Teilen nicht "
             "höher als 3,50 m sind. Höhere Anlagen fallen in das vereinfachte Bewilligungsverfahren. Auch der "
             "Batteriespeicher ist bis 20 kWh Energieinhalt meldepflichtig, bis 100 kWh mit einem zusätzlichen "
             "Sicherheitsnachweis. Die Mitteilung geht vor der Ausführung schriftlich an die Gemeinde, mit "
             "Grundstücksnummer, Lage am Grundstück und einer kurzen Beschreibung. Wir bereiten sie für Sie vor."),
            ("Anders ist es im Ortsbildschutzgebiet. Das Ortsbildkonzept II (2.0) der Stadt Leoben macht dort "
             "Veränderungen, die sich auf das Ortsbild auswirken können, bewilligungspflichtig, auch wenn das "
             "Baugesetz sie nur als meldepflichtig einstuft. Für Sonnenkollektoren legt es fest: nicht auf Dachflächen "
             "in der mittelalterlichen Stadt und im Schutzgebiet Göss, in den übrigen Schutzgebieten nur dort, wo sie "
             "von öffentlichen Verkehrsflächen aus nicht einsehbar sind. Wie die Baubehörde das auf Ihre "
             "Photovoltaikmodule anwendet, fragen wir vor der Planung bei der Stadt an. So erfahren Sie früh, ob "
             "und auf welcher Dachfläche eine Anlage möglich ist."),
            ("Beim Netzanschluss in der Stadt führt der Weg über das Einspeiserportal der Energienetze Steiermark: "
             "Einspeisezählpunkt ansuchen, die Netzbeurteilung startet danach von selbst, das Netzanschlusskonzept "
             "nennt Anschlusspunkt und Betriebsvorgaben. Es gilt 12 Monate und lässt sich einmal um 12 Monate "
             "verlängern. Für PV-Anlagen von 3,68 bis 250 kW verlangt der Netzbetreiber eine Wirkleistungsvorgabe, bei "
             "Neuanlagen über ein Kabel vom Wechselrichter zum Smart Meter. Der Netzbetreiber veröffentlicht außerdem "
             "freie Einspeisekapazitäten je Umspannwerk: Mit Stand 1. Juli 2026 waren es für Leoben West 8,4 MW, für "
             "Hessenberg 0,0 MW. Das ist eine unverbindliche Momentaufnahme. Für Ihr Haus zählt das "
             "Netzanschlusskonzept, deshalb holen wir es ein, bevor Sie etwas bestellen."),
        ],
        "bullets": [
            "PV auf Dach oder Fassade bis 3,50 m Höhe: meldepflichtig, Mitteilung an die Stadtgemeinde vor Baubeginn",
            "Speicher bis 20 kWh: meldepflichtig, darüber mit zusätzlichem Nachweis",
            "Altstadt und Göss: Ortsbildkonzept beachten, Abklärung mit der Baubehörde vor der Planung",
            "Netz: Energienetze Steiermark in Leoben, Stadtwerke Trofaiach in Trofaiach",
        ],
        "img": "gen_detail",
        "alt": "Monteur verschraubt ein Photovoltaikmodul auf der Montageschiene eines Ziegeldachs (Symbolbild)",
    },

    "waermepumpe": {
        "h2": "Wärmepumpe in Leoben: zuerst die Stadtwärme prüfen, dann die Heizung planen",
        "paragraphs": [
            ("Der Heizungstausch beginnt in Leoben mit einer eigenen Frage: Liegt Ihr Haus im Gebiet der Stadtwärme? "
             "Die Stadtwerke Leoben nutzen seit 2009 die Abwärme der voestalpine in Donawitz. Das Netz hat derzeit "
             "48 MW thermische Leistung und soll laut Stadtwerken auf 68 MW wachsen, was einer Vollversorgung der "
             "Stadt entspräche. Erschlossen sind neben Donawitz die Innere Stadt, Judendorf, Leitendorf und Göss. "
             "Liegt eine Leitung vor Ihrem Haus, ist der Anschluss oft die naheliegende Lösung, und das sagen wir "
             "Ihnen auch so."),
            ("Die Wärmepumpe ist die richtige Wahl, wo die Stadtwärme nicht hinkommt: am Stadtrand, in den Gräben und "
             "in den Umlandgemeinden von Trofaiach bis Kraubath. Sie kann es auch im Netzgebiet sein, denn die "
             "Stadtwerke prüfen jeden Anschluss auf Wirtschaftlichkeit, und bei kleinen Anlagen kann er abgelehnt "
             "oder teurer werden. Im Bestand entscheidet die Vorlauftemperatur: Kommen Ihre Heizkörper mit bis zu "
             "55 Grad aus, arbeitet eine Luft-Wasser-Wärmepumpe effizient. Sie kostet im Einfamilienhaus rund "
             "12.000 bis 22.000 € vor Förderung*, im Altbau mit Anpassungen rund 15.000 bis 28.000 €*."),
            ("Zwei Punkte klären wir vor dem Angebot. Baurecht: Die ortsfeste Aufstellung einer Wärmepumpe ist in der "
             "Steiermark meldepflichtig. Der Mitteilung an die Gemeinde liegen das technische Datenblatt und die "
             "Bestätigung eines Sachverständigen bei, dass der zulässige Schallpegel an der Grundgrenze eingehalten "
             "wird. In Reihenhaussiedlungen legen wir den Platz der Außeneinheit deshalb früh fest. Förderung: Die "
             "Richtlinie des Landes für den Tausch erneuerbar betriebener Heizungssysteme setzt voraus, dass für das "
             "Haus keine Anschlussmöglichkeit an ein Nah- oder Fernwärmenetz besteht, außer der Anschluss ist "
             "wirtschaftlich nicht zumutbar. Das bestätigt das Fernwärmeunternehmen, in Leoben also die Stadtwerke."),
            ("Photovoltaik passt zu beiden Wegen. Mit Stadtwärme senkt sie Ihre Stromrechnung, mit Wärmepumpe liefert "
             "sie zusätzlich einen Teil des Heizstroms. Ein " + a("ems", "Energiemanagementsystem") + " legt "
             "Warmwasser und Pufferspeicher dann in die Stunden, in denen das Dach Strom liefert."),
        ],
        "bullets": [
            "Im Stadtwärme-Gebiet: Anschlussmöglichkeit zuerst bei den Stadtwerken Leoben klären",
            "Außerhalb des Netzes: Luft-Wasser-Wärmepumpe ab rund 12.000 € vor Förderung*",
            "Aufstellung meldepflichtig, mit Schallbestätigung an der Grundgrenze",
            a("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau") + ": wann die vorhandenen Heizkörper reichen",
        ],
        "img": "waermepumpe",
        "alt": "Außeneinheit einer Luft-Wasser-Wärmepumpe vor einer Holzwand im Garten (Symbolbild)",
    },

    "foerderung_h2": "Förderung für Photovoltaik und Wärmepumpe in Leoben: Bund, Land und der Stand bei der Stadt",
    "foerderung_lokal": [
        ("Die Stadtgemeinde Leoben hat thermische Solaranlagen, Photovoltaikanlagen, Biomasseheizungen und "
         "Wärmepumpen über ihre Umweltförderung unterstützt. Dieses Programm ruht: Laut Stadt werden in diesen "
         "Bereichen bis auf Weiteres keine Förderungen ausgeschüttet, einen Rechtsanspruch gab es nie. Wir fragen den "
         "Stand vor jedem Angebot beim Referat für Abfall-, Abwasser- und Umweltmanagement der Stadt nach, damit Sie "
         "nicht mit Geld rechnen, das es nicht gibt."),
        ("Für Häuser in Trofaiach, St. Michael, Niklasdorf und den anderen Gemeinden des Bezirks prüfen wir die "
         "Gemeindeförderung einzeln. Wer Strom mit Nachbarn teilen will: Die KEM Murraum Leoben führt den PV-Ausbau "
         "und Energiegemeinschaften als eigene Maßnahme. Wie das Teilen funktioniert, "
         "steht im Ratgeber " + a("/energiegemeinschaft-steiermark/", "Energiegemeinschaft in der Steiermark") + "."),
    ],

    "referenzen": {
        "h2": "Referenzen aus der Steiermark: zwei Projekte in Graz mit Zahlen",
        "intro": ("Aus Leoben zeigen wir hier noch kein Projekt mit Zahlen. Die nächstgelegenen dokumentierten Anlagen "
                  "stehen in Graz: ein Einfamilienhaus und ein Stadthaus, beide mit Speicher und Wallbox, beide "
                  "ballastiert ohne Bohrung im Flachdach."),
        "slugs": ["projekt-flachdach-in-graz", "projekt-stadthaus-in-graz"],
    },

    "umgebung": [
        "Trofaiach", "Sankt Michael in Obersteiermark", "Niklasdorf", "Proleb", "Sankt Peter-Freienstein",
        "Sankt Stefan ob Leoben", "Kraubath an der Mur", "Traboch", "Kammern im Liesingtal", "Mautern in Steiermark",
        "Vordernberg", "Eisenerz",
    ],
    "links": [
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau"),
        ("/energiegemeinschaft-steiermark/", "Energiegemeinschaft in der Steiermark"),
        ("/foerderung-fuer-pv-speicher/", "Förderung für PV-Speicher"),
    ],

    "faq": [
        ("Brauche ich in Leoben eine Baubewilligung für eine Photovoltaikanlage?",
         "In der Regel nicht. Nach § 21 des Steiermärkischen Baugesetzes sind Photovoltaikanlagen auf Dach- oder "
         "Fassadenflächen meldepflichtig, solange die Anlage samt ihren Teilen nicht höher als 3,50 Meter ist. Die "
         "Mitteilung geht vor Baubeginn schriftlich an die Stadtgemeinde Leoben und enthält Grundstücksnummer, Lage "
         "am Grundstück und eine kurze Beschreibung. Im Ortsbildschutzgebiet gelten zusätzliche Regeln. EBZ Energie "
         "bereitet die Mitteilung vor."),
        ("Darf ich in der Leobener Altstadt oder in Göss eine PV-Anlage aufs Dach bauen?",
         "Das muss vorab mit der Baubehörde geklärt werden. Im Ortsbildschutzgebiet gilt das Ortsbildkonzept II (2.0) "
         "der Stadt Leoben. Es untersagt Sonnenkollektoren auf Dachflächen in der mittelalterlichen Stadt und im "
         "Schutzgebiet Göss; in den übrigen Schutzgebieten sind sie nur zulässig, wenn sie von öffentlichen "
         "Verkehrsflächen aus nicht einsehbar sind. Veränderungen am Ortsbild sind dort bewilligungspflichtig. Wir "
         "fragen für Ihr Haus bei der Stadt an, bevor wir planen."),
        ("Wer ist in Leoben der Stromnetzbetreiber und wie läuft der Netzanschluss ab?",
         "In Leoben ist die Energienetze Steiermark GmbH zuständig, die Stadtwerke Leoben betreiben kein Stromnetz. "
         "Der Antrag läuft über das Einspeiserportal: Einspeisezählpunkt ansuchen, Netzbeurteilung abwarten, "
         "Netzanschlusskonzept erhalten. Dieses Konzept gilt 12 Monate und kann einmal um 12 Monate verlängert "
         "werden. In Trofaiach betreiben die Stadtwerke Trofaiach ein eigenes Verteilernetz mit eigenem Antrag auf "
         "Netzzutritt. Wir übernehmen die Anmeldung beim jeweils zuständigen Netzbetreiber."),
        ("Was kostet eine Photovoltaikanlage in Leoben?",
         "Eine Komplettanlage mit rund 10 kWp und Speicher kostet typischerweise rund 15.000 bis 22.000 Euro vor "
         "Förderung, inklusive Montage, Netzanmeldung und Inbetriebnahme (EBZ-Richtpreis, Stand Oktober 2026). Der "
         "Bund fördert mit 150 Euro je kWp bis 10 kWp und 150 Euro je kWh Speicher. Die Steiermark zahlt keine "
         "PV-Landespauschale, und die Stadt Leoben schüttet ihre Umweltförderung derzeit nicht aus. Den genauen "
         "Preis nennen wir nach dem Termin bei Ihnen in Leoben als Fixangebot."),
        ("Wärmepumpe oder Stadtwärme in Leoben: was passt besser?",
         "Das hängt von der Lage ab. Die Stadtwärme der Stadtwerke Leoben nutzt Abwärme der voestalpine in Donawitz "
         "und erschließt Donawitz, die Innere Stadt, Judendorf, Leitendorf und Göss. Liegt Ihr Haus dort, ist der "
         "Anschluss oft die naheliegende Lösung. Außerhalb des Netzes, in den Gräben und in den Umlandgemeinden ist "
         "die Wärmepumpe meist die bessere Wahl, vor allem zusammen mit Photovoltaik. Wir fragen die "
         "Anschlussmöglichkeit bei den Stadtwerken ab, bevor wir eine Wärmepumpe anbieten."),
        ("Muss ich eine Wärmepumpe in Leoben genehmigen lassen?",
         "Die ortsfeste Aufstellung einer Wärmepumpe ist nach dem Steiermärkischen Baugesetz meldepflichtig, eine "
         "Baubewilligung brauchen Sie dafür in der Regel nicht. Der Mitteilung an die Stadtgemeinde Leoben liegen das technische "
         "Datenblatt und die Bestätigung eines befugten Sachverständigen bei, dass der zulässige Schallpegel an der "
         "Grundgrenze zum nächsten Nachbargrundstück eingehalten wird. Im Ortsbildschutzgebiet klären wir zusätzlich "
         "den Standort der Außeneinheit mit der Baubehörde."),
        ("Fördert die Stadt Leoben Photovoltaik oder Wärmepumpen?",
         "Derzeit nicht. Die Stadtgemeinde Leoben hat thermische Solaranlagen, Photovoltaik, Biomasseheizungen und "
         "Wärmepumpen über ihre Umweltförderung unterstützt, schüttet in diesen Bereichen aber laut eigener Auskunft "
         "bis auf Weiteres keine Förderungen aus. Für Photovoltaik und Speicher bleibt der Investitionszuschuss des "
         "Bundes. Welche Programme heute beantragbar sind, prüfen wir vor dem Angebot und zeigen es im Förderrechner."),
        ("Kommt EBZ Energie auch nach Trofaiach, St. Michael oder Eisenerz?",
         "Ja. EBZ Energie ist ein Fachbetrieb aus Villach und montiert in Kärnten und der Steiermark. Für die "
         "Erstberatung kommen wir zu Ihnen nach Leoben und in die Gemeinden des Bezirks, etwa Trofaiach, St. Michael "
         "in Obersteiermark, Niklasdorf, Kraubath oder Eisenerz. Einen Standort in Leoben haben wir nicht. Sie haben "
         "einen festen Ansprechpartner von der Planung bis zur Übergabe, montiert wird von zertifizierten Fachkräften. "
         "Auch die Wärmepumpe planen wir im ganzen Bezirk."),
    ],

    "quellen": [
        ("Stadt Leoben: Gemeindestatistik (Einwohner, Haushalte, Fläche, Seehöhe, Katastralgemeinden)",
         "https://www.leoben.at/leoben-im-ueberblick/gemeindestatistik/"),
        ("Stadt Leoben: Leben in Leoben",
         "https://www.leoben.at/willkommen/leben-in-leoben/"),
        ("Stadt Leoben: Förderungen für alternative Heiz- und Energiesysteme",
         "https://www.leoben.at/service/foerderungen-alternative-heizsysteme/"),
        ("Stadt Leoben: Ortsbildkonzept II (2.0), Verordnung des Gemeinderats",
         "https://leoben.at/downloads/ortsbildkonzept"),
        ("Stadtwerke Leoben: Stadtwärme",
         "https://www.stadtwerke-leoben.at/stadtwaerme/"),
        ("Stadtwerke Leoben: Gasversorgung",
         "https://www.stadtwerke-leoben.at/gasversorgung/"),
        ("Land Steiermark: Steiermärkisches Baugesetz in der Fassung LGBl. Nr. 20/2026 (§§ 20 und 21)",
         "https://www.technik.steiermark.at/cms/dokumente/11549819_58813874/dadceab4/Baugesetz_idF_LGBl_20_2026.pdf"),
        ("Energienetze Steiermark: Erzeugungsanlagen und Netzzugang",
         "https://www.e-netze.at/Strom/Erzeugungsanlagen/Default.aspx"),
        ("Energienetze Steiermark: Freie Einspeisekapazitäten je Umspannwerk",
         "https://www.e-netze.at/Service/FEK/Default.aspx"),
        ("Stadtwerke Trofaiach: Strom und Verteilernetz",
         "https://stadtwerke-trofaiach.at/versorgung/strom/"),
        ("Bezirkshauptmannschaft Leoben: Gemeinden des Bezirks",
         "https://www.bh-leoben.steiermark.at/cms/ziel/58186641/DE/"),
        ("Land Steiermark: Förderungsrichtlinie Tausch erneuerbar betriebener Heizungssysteme 2026",
         "https://www.wohnbau.steiermark.at/cms/dokumente/13000784_183599709/c26463e2/2026_F%C3%B6rderungsrichtlinie%20Tausch%20erneuerbar%20betriebener%20Heizungssysteme.pdf"),
        ("Land Steiermark: Solarpotenzial und SolarTool im Digitalen Atlas",
         "https://landesentwicklung.steiermark.at/cms/beitrag/12910759/145230171"),
        ("Klima- und Energie-Modellregion Murraum Leoben",
         "https://www.murraum-leoben.at/"),
    ],

    "notizen": (
        "Faktenfragen und Unsicherheiten (Stand 10.10.2026): "
        "1) Landesfoerderung Waermepumpe Steiermark: Die Vorlage nennt 35 % der foerderbaren Kosten. Die Seite des "
        "Landes (wohnbau.steiermark.at, Oekofoerderungen) meldet fuer Waermepumpen 'Antragstellung derzeit nicht "
        "moeglich, auf absehbare Zeit keine Foerderungsmoeglichkeit'; die einzige 2026er Richtlinie (Tausch erneuerbar "
        "betriebener Heizungssysteme) deckt nur den Ersatz mind. 15 Jahre alter Biomassekessel/Waermepumpen, max. 30 %, "
        "max. 1.500 EUR, Budget 300.000 EUR. Bitte zentral pruefen (LAND['stmk'] in standorte.py). Diese Datei nennt "
        "deshalb keinen Landessatz und setzt eigene KPIs ohne die 35 %. "
        "2) Stromnetz Leoben: Energienetze Steiermark ist ueber deren Umspannwerke Leoben West und Hessenberg und das "
        "Fehlen eines Strombereichs bei den Stadtwerken Leoben belegt, nicht ueber eine Gemeindeliste. Vom Kunden "
        "bestaetigen lassen, ob es im Stadtgebiet Inselnetze gibt. "
        "3) Ortsbildkonzept II (2.0): veroeffentlichte Fassung mit Aenderung 2010. Ist das die geltende Fassung, und "
        "wie handhabt die Stadt PV-Module (Text nennt Sonnenkollektoren)? "
        "4) Stadtfoerderung: ruht laut leoben.at; Wiederaufnahme beobachten. "
        "5) Hat EBZ ein Projekt im Bezirk Leoben, das als Referenz freigegeben werden kann? "
        "6) Bietet EBZ in Leoben auch Erdwaerme-/Grundwasser-Waermepumpen an oder nur Luft-Wasser?"
    ),
}
