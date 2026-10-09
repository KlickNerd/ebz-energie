"""Leistungsseite Waermepumpe (/waermepumpe/).

Kernbotschaft: Die Waermepumpe ist bei EBZ Teil des Energiesystems aus
Photovoltaik, Speicher und Energiemanagement. Eigenheim UND Gewerbe.
Zahlen stammen aus den Ratgebern des Clusters (Kosten, Foerderung, Altbau,
Funktionsweise, PV fuer Waermepumpe) und aus build/seo/_fakten_2026-10.md.

SEO/GEO-Briefing build/seo/waermepumpe.json (Stand 2026-10-09): Primaer
"waermepumpe" (12.100) mit Region, "Waermepumpe Installateur" als Sekundaer-
Keyword, Lautstaerke/Aufstellort, Kuehlen, Hersteller (iDM, Ochsner, Lambda als
Beispiele), Rechenbeispiel Stromverbrauch, Klagenfurt/Graz.

WICHTIG (Faktenblatt 9.10.2026): Bundesfoerderung 2026 (Sanierungsoffensive,
Sauber Heizen fuer Alle) ist ausgeschoepft, keine neuen Registrierungen. Keine
"bis zu 7.500 EUR vom Bund"-Aussage als verfuegbar. Landesfoerderungen und
Oeko-Sonderausgabenpauschale laufen, 2027 offen.
Quelle der Live-Seite bereinigt: "90 %"-Claim, Gedankenstriche, Emojis,
unbelegte Superlative, "ganz Oesterreich" als Montagegebiet.
"""

from common import IMG, NAP, S, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

# Slug kommt aus common.S (Stand Oktober 2026: /waermepumpe/, alte URL
# /waermepumpen-installateur/ per 301 in redirects.txt). Ausgabepfad folgt dem Slug,
# damit Navigation, Sitemap und Seite immer dieselbe URL verwenden.
PATH = S["waermepumpe"]
OUT_FILE = PATH.strip("/") + "/index.html"
TITLE = "Wärmepumpe Kärnten & Steiermark: Kosten, Förderung | EBZ"
DESC = ("Luft-Wasser-Wärmepumpe vom Fachbetrieb in Kärnten und der Steiermark: Kosten ab 12.000 €, Förderung "
        "komplett abgewickelt, Kombination mit Photovoltaik.")

FAQ = [
    ("Was kostet eine Wärmepumpe für ein Einfamilienhaus?",
     "Eine Luft-Wasser-Wärmepumpe kostet im Einfamilienhaus 12.000 bis 22.000 Euro vor Förderung inklusive "
     "Installation, im Altbau mit Anpassungen 15.000 bis 28.000 Euro, Erdwärme oder Grundwasser 22.000 bis 40.000 "
     "Euro (Stand Oktober 2026). Den Festpreis erhalten Sie nach der Vor-Ort-Prüfung."),
    ("Wie hoch ist die Förderung für eine Wärmepumpe 2026?",
     "Die Bundesförderung 2026 (Kesseltausch bis 7.500 Euro, Sauber Heizen für Alle bis 100 Prozent) ist seit Herbst "
     "2026 ausgeschöpft, neue Registrierungen sind nicht möglich. Aktuell laufen die Landesförderungen: Kärnten laut "
     "Berichten 2026 mit 3.000 Euro Pauschale, die Steiermark mit 35 Prozent der förderbaren Kosten. Ob 2027 ein neues "
     "Bundesprogramm kommt, ist offen (Stand Oktober 2026)."),
    ("Funktioniert eine Wärmepumpe auch im Altbau, und wann macht sie keinen Sinn?",
     "Ja, meistens. Bis 55 Grad Vorlauf arbeitet eine moderne Wärmepumpe effizient, große alte Heizkörper sind oft "
     "überdimensioniert und deshalb geeignet. Brauchen Heizkörper dauerhaft 60 bis 70 Grad, hilft eine "
     "Hochtemperatur-Wärmepumpe oder der Tausch einzelner Heizkörper. Wenig Sinn macht sie nur im ungedämmten Haus, in "
     "dem zuerst Fenster oder Dämmung dran sind; Kälte ist kein Hindernis, Luft-Wasser-Geräte arbeiten bis minus 20 Grad."),
    ("Wie viel Strom verbraucht eine Wärmepumpe im Einfamilienhaus pro Jahr?",
     "Heizwärmebedarf geteilt durch Jahresarbeitszahl: Ein gut gedämmtes Haus mit 12.000 kWh Wärmebedarf braucht bei "
     "JAZ 4 rund 3.000 kWh Strom im Jahr, bei 30 Cent je kWh etwa 900 Euro; Gas kostet für dieselbe Wärme 1.400 bis "
     "1.900 Euro. Ein ungedämmtes Gebäude mit 20.000 kWh und JAZ 3 liegt bei rund 6.700 kWh.*"),
    ("Lohnt sich die Kombination mit Photovoltaik?",
     "Ja. Eigener Solarstrom kostet 10 bis 14 Cent je Kilowattstunde, Netzstrom das Zwei- bis Dreifache. Mit "
     "PV-Anlage und Speicher sinken die Heizkosten im Beispielhaus auf 200 bis 500 Euro im Jahr. Die PV-Anlage wird "
     "getrennt gefördert: 150 Euro je kWp und 150 Euro je kWh Speicher, Fördercall bis 22. Oktober 2026."),
    ("Wie laut ist eine Luft-Wasser-Wärmepumpe und wo darf sie stehen?",
     "Die Lautstärke steht als Schallleistung in dB(A) im Datenblatt, nachts läuft die Außeneinheit mit reduzierter "
     "Drehzahl. Entscheidend ist der Aufstellort: nicht in Ecken oder zwischen zwei Wänden, Abstand zu "
     "Schlafzimmerfenstern und Nachbargrenze, freie Luftansaugung; beim Kältemittel R290 gelten Abstandsregeln zu "
     "Fenstern und Lichtschächten. Erd- und Grundwasser-Wärmepumpen stehen komplett im Haus."),
    ("Kann die Wärmepumpe im Sommer auch kühlen?",
     "Ja. Die Wärmepumpe kehrt den Kreislauf um und kühlt über die Fußbodenheizung oder Gebläsekonvektoren, nicht "
     "über klassische Heizkörper. Den Strom liefert mittags die PV-Anlage; mit 10 bis 15 kWp heizen und kühlen Sie "
     "weitgehend mit eigenem Strom."),
    ("Welche Hersteller verbaut EBZ?",
     "Wir planen herstellerunabhängig und setzen bevorzugt auf österreichische Hersteller wie iDM, Ochsner oder "
     "Lambda, je nach Gebäude, Vorlauftemperatur und Budget. Entscheidend sind Jahresarbeitszahl, Schallwerte, "
     "Kältemittel R290 und die SG-Ready-Schnittstelle; das Gerät steht im Festpreisangebot mit Datenblatt."),
    ("Wie lange hält eine Wärmepumpe und was kostet die Wartung?",
     "15 bis 20 Jahre und mehr. Statt jährlicher Abgasmessung wie bei Gas braucht sie nur alle 2 bis 3 Jahre eine "
     "Inspektion für 150 bis 400 Euro. Die Garantiebedingungen des Herstellers weisen wir im Angebot aus."),
    ("Wie lange dauert der Einbau?",
     "Die Montage vor Ort dauert 2 bis 4 Tage inklusive Demontage der alten Heizung. Davor liegen Beratung, "
     "Vor-Ort-Prüfung, Festpreisangebot und die Förderanträge beim Land."),
]


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        C.hero(
            eyebrow="Wärmepumpe für Kärnten und die Steiermark: Villach, Klagenfurt, Wolfsberg, Graz",
            h1="Wärmepumpe vom Installateur-Fachbetrieb in Kärnten und der Steiermark: heizen mit Strom statt mit Öl und Gas",
            lead=("Eine Luft-Wasser-Wärmepumpe kostet 2026 inklusive Montage rund 12.000 bis 22.000 € vor Förderung "
                  "und macht aus 1 kWh Strom 4 bis 5 kWh Wärme. Mit Strom vom eigenen Dach wird sie zur günstigsten "
                  "Heizung im Haus. EBZ Energie plant, montiert und betreut Wärmepumpe, Photovoltaik und Speicher als "
                  "ein System, mit zertifizierten Fachkräften aus Villach."),
            badges=[("ab 12.000 €", "Luft-Wasser vor Förderung*"),
                    ("Luft, Erde", "oder Grundwasser"),
                    ("Mit PV + Speicher", "aus einer Hand")],
            img=IMG["waermepumpe"],
            img_alt="Luft-Wasser-Wärmepumpe im Garten eines Einfamilienhauses",
            float_num=rating,
            float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_secondary=("#kosten", "Kosten und Förderung"),
        ),
        C.kpis([
            ("4 bis 5 kWh", "Wärme aus 1 kWh Strom"),
            ("12.000 bis 22.000 €", "Luft-Wasser vor Förderung*"),
            ("2 bis 4 Tage", "Montage vor Ort"),
            (NAP["rating"], "Sterne auf Google"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Was ist eine Wärmepumpe?",
            paragraphs=[
                ("Eine Wärmepumpe ist eine Heizung, die Umgebungswärme aus Luft, Erdreich oder Grundwasser aufnimmt "
                 "und mit einem Kältemittelkreislauf auf Heiztemperatur hebt, wie ein Kühlschrank in umgekehrter "
                 "Richtung. Aus 1 kWh Strom und 3 bis 4 kWh Umweltwärme entstehen 4 bis 5 kWh Heizwärme. Der COP "
                 "beschreibt diesen Wert an einem Betriebspunkt, die Jahresarbeitszahl (JAZ) über das ganze Heizjahr "
                 "(Ratgeber EBZ Energie, Stand Oktober 2026)."),
                ("Die häufigste Bauart ist die Luft-Wasser-Wärmepumpe, oft auch Luftwärmepumpe oder Luft Wasser "
                 "Wärmepumpe geschrieben: Als Monoblock steht die komplette Technik draußen, beim Split-Gerät sitzt "
                 "der Verdichter in der Außeneinheit und die Wärmeübergabe im Haus. Wer eine Wärmepumpe kaufen will, "
                 "vergleicht deshalb drei Zahlen: Anschaffung, Stromverbrauch und Förderung."),
            ],
        ),
        C.hub_section(
            eyebrow="Die Wärmepumpe im Energiesystem",
            h2="Ein Gerät heizt. Ein System spart.",
            lead=("Die Wärmepumpe ist der größte Stromverbraucher im Haus. Deshalb planen wir sie zusammen mit "
                  "Photovoltaik, Speicher und Energiemanagement: Der Heizstrom kommt vom eigenen Dach."),
            points=[
                ("☀", "Photovoltaik mit 10 bis 15 kWp liefert den Strom für Wärmepumpe und Haushalt"),
                ("▮", "Batteriespeicher mit 10 bis 12 kWh hebt den Eigenverbrauch auf 70 bis 80 Prozent"),
                ("♨", "Wärmepumpe heizt, bereitet Warmwasser und kühlt im Sommer"),
                ("⚙", "Energiemanagement mit SG-Ready-Schnittstelle lädt bei Sonne den Pufferspeicher vor"),
                ("€", "Solarstrom kostet 10 bis 14 ct/kWh, Netzstrom das Zwei- bis Dreifache*"),
            ],
        ),
        C.audience_split(
            eyebrow="Für wen planen wir?",
            h2="Eigenheim oder Betrieb: die Wärmepumpe passt zu Ihrem Gebäude",
            intro="Vom Heizungstausch im Einfamilienhaus bis zur Halle mit 80 kW Heizlast: Planung, Gerät und Förderweg richten wir danach aus.",
            left={
                "img": IMG["gen_eigenheim"],
                "alt": "Einfamilienhaus in Kärnten mit Photovoltaikanlage für die Wärmepumpe",
                "title": "Für Ihr Eigenheim",
                "bullets": [
                    "Raus aus Öl und Gas: Landesförderung Kärnten oder Steiermark plus Steuerbonus",
                    "Neubau und Altbau, auch mit vorhandenen Heizkörpern",
                    "Heizkosten mit Photovoltaik: 200 bis 500 € im Jahr*",
                ],
                "cta": ("kontakt", "Beratung für mein Zuhause"),
            },
            right={
                "img": IMG["gen_gewerbe"],
                "alt": "Gewerbegebäude mit großer Photovoltaikanlage am Dach",
                "title": "Für Ihren Betrieb",
                "bullets": [
                    "Betriebsförderung der KPC: eigenes Programm, Antrag nach Umsetzung",
                    "Planung nach Heizlast und Lastprofil, auch für Hallen und Bürogebäude",
                    "Kombination mit PV-Anlage senkt Heiz- und Stromkosten gleichzeitig",
                ],
                "cta": ("#gewerbe", "Wärmepumpe für Gewerbe"),
            },
        ),
        C.cards_section(
            eyebrow="Drei Wärmequellen",
            h2="Luft-Wasser, Erdwärme oder Grundwasser: welche Wärmepumpe passt zu Ihrem Grundstück?",
            intro=("Luft, Erdreich oder Grundwasser: Die Wärmequelle entscheidet über Kosten, Effizienz und Genehmigung. "
                   "Wir prüfen vor Ort, welche Variante sich für Sie rechnet."),
            cards=[
                {"ic": "☀", "title": "Luft-Wasser-Wärmepumpe (Luftwärmepumpe)",
                 "text": ("Die häufigste Wahl: 12.000 bis 22.000 € vor Förderung, JAZ 3,0 bis 3,5, keine Bohrung, als "
                          "Monoblock oder Split-Gerät, läuft bis minus 20 Grad und darunter.*")},
                {"ic": "⬡", "title": "Sole-Wasser-Wärmepumpe (Erdwärme)",
                 "text": ("Erdkollektor oder Tiefenbohrung: 22.000 bis 40.000 € vor Förderung, JAZ 4,0 bis 4,5, keine "
                          "Außeneinheit und damit kein Geräusch im Garten.*")},
                {"ic": "◎", "title": "Wasser-Wasser-Wärmepumpe (Grundwasser)",
                 "text": ("Die effizienteste Variante, JAZ 4,5 bis 5,5: 22.000 bis 38.000 € vor Förderung, braucht "
                          "Grundwasser und eine wasserrechtliche Bewilligung.*"),
                 "link_key": "/funktionsweise-einer-waermepumpe/", "link_text": "So funktioniert die Wärmepumpe"},
            ],
        ),
        C.problem_compare(
            eyebrow="Heizkosten im Vergleich",
            h2="Was Sie im Jahr fürs Heizen zahlen",
            intro=("Der Stromverbrauch einer Wärmepumpe ergibt sich aus Heizwärmebedarf geteilt durch Jahresarbeitszahl: "
                   "Ein gut gedämmtes Einfamilienhaus mit 12.000 kWh Wärmebedarf braucht bei JAZ 4 rund 3.000 kWh Strom "
                   "im Jahr, bei 30 Cent je kWh etwa 900 € (Rechenbeispiel EBZ Energie, Stand Oktober 2026). Ein "
                   "Wärmepumpenstromtarif Ihres Versorgers oder Solarstrom vom Dach senkt den Preis je kWh weiter.*"),
            bars=[
                ("Gasheizung", 100, "bad", "1.400 bis 1.900 € im Jahr*"),
                ("Wärmepumpe mit Netzstrom", 50, "good", "rund 900 € im Jahr*"),
                ("Wärmepumpe mit Photovoltaik und Speicher", 20, "good", "200 bis 500 € im Jahr*"),
            ],
            aside=("Was Sie mit der Wärmepumpe gewinnen", [
                ("♨", "Heizung und Warmwasser", "Ein Gerät für beides, im Sommer auf Wunsch auch Kühlung."),
                ("€", "Planbare Kosten", "Kein Heizöl bestellen, kein Gaspreis, keine CO₂-Abgabe."),
                ("☀", "Strom vom Dach", "Mit PV-Anlage heizen Sie zu 10 bis 14 ct/kWh.*"),
                ("✓", "Wartungsarm", "Inspektion alle 2 bis 3 Jahre für 150 bis 400 €, Lebensdauer 15 bis 20 Jahre und mehr."),
            ]),
        ),
        C.price_cards(
            eyebrow="Wärmepumpe Preis 2026: Gerät plus Installation",
            h2="Was kostet eine Wärmepumpe?",
            intro=("Eine Luft-Wasser-Wärmepumpe kostet in Österreich 2026 inklusive Montage rund 12.000 bis 22.000 € im "
                   "Einfamilienhaus, im Altbau mit Anpassungen 15.000 bis 28.000 €, Erdwärme oder Grundwasser 22.000 bis "
                   "40.000 € (Ratgeber Kosten einer Wärmepumpe, EBZ Energie, Stand Oktober 2026). Alle Werte vor "
                   "Förderung, den Festpreis erhalten Sie nach der Vor-Ort-Prüfung."),
            items=[
                {"size": "Luft-Wasser im Einfamilienhaus", "price": "12.000 bis 22.000 €", "price_sub": "vor Förderung*",
                 "features": ["Gerät 8.000 bis 18.000 €, Installation 3.000 bis 6.000 €",
                              "Keine Bohrung, keine Erschließung nötig",
                              "Landesförderung Kärnten oder Steiermark abziehbar"]},
                {"size": "Luft-Wasser im Altbau", "price": "15.000 bis 28.000 €", "price_sub": "vor Förderung*",
                 "features": ["Inklusive Anpassung von Heizkörpern und Verteilsystem",
                              "Fußbodenheizung nicht zwingend, Nachrüstung 50 bis 120 € je m²",
                              "Hochtemperatur-Wärmepumpe für Heizkörper mit 60 bis 70 Grad Vorlauf"]},
                {"size": "Erdwärme oder Grundwasser", "price": "22.000 bis 40.000 €", "price_sub": "vor Förderung*",
                 "features": ["Inklusive Kollektor, Tiefenbohrung oder Brunnen",
                              "Höchste Effizienz, niedrigste Betriebskosten",
                              "Keine Außeneinheit, kein Ventilatorgeräusch"]},
            ],
            note=("*Richtwerte 2026 für Österreich, vor Abzug von Förderungen. Alle Kostenblöcke im Detail: "
                  + a("/kosten-einer-waermepumpe/", "Was kostet eine Wärmepumpe") + "."),
        ).replace('<section class="section"', '<section id="kosten" class="section"', 1),
        C.media_text(
            eyebrow="Förderung 2026",
            h2="Förderung 2026: Bund ausgeschöpft, Land Kärnten und Steiermark, Steuerbonus",
            paragraphs=[
                ("Die Bundesförderung 2026 für den Heizungstausch (Sanierungsoffensive mit Kesseltausch bis 7.500 €, "
                 "Sauber Heizen für Alle bis 100 %) ist seit Herbst 2026 ausgeschöpft, neue Registrierungen sind nicht "
                 "möglich; ob 2027 ein neues Bundesprogramm kommt, ist offen (Quelle: umweltfoerderung.at, Stand "
                 "9. Oktober 2026). Wer bereits registriert ist, kann noch beantragen."),
                ("Aktuell laufen die Landesförderungen: Kärnten fördert den Heizungstausch weiter (2026 laut Berichten "
                 "auf 3.000 € Pauschale angepasst, zuvor 35 % bis 6.000 €), die Steiermark zahlt 35 % der förderbaren "
                 "Kosten für Ein- und Zweifamilienhäuser. Wer seine Bundesförderung noch ausbezahlt bekommt, setzt "
                 "zusätzlich fünf Jahre lang je 400 € Öko-Sonderausgabenpauschale ab. Wir prüfen vor jedem Angebot den "
                 "Budgetstand und übernehmen die Anträge."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Wärmepumpenförderung am Tisch",
            bullets=[
                "Bund 2026: Kesseltausch bis 7.500 € galt bis zur Ausschöpfung, aktuell keine neuen Registrierungen",
                a("/landesfoerderungen-fuer-die-waermepumpe/", "Landesförderungen Kärnten und Steiermark") + ": laufen, Richtlinien ändern sich, wir prüfen tagesaktuell",
                a("/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/", "Öko-Sonderausgabenpauschale") + ": 5 Jahre je 400 € bei ausbezahlter Bundesförderung und über 2.000 € Restkosten",
                "Finanzierung möglich: 0 € Anzahlung, fixe Rate, Eigentum ab Tag 1",
            ],
            cta=("/waermepumpenfoerderung-in-oesterreich/", "Wärmepumpenförderung 2026 im Detail"),
            dark=True,
        ),
        C.media_text(
            eyebrow="Wärmepumpe im Altbau",
            h2="Heizungstausch im Altbau: Heizkörper, Vorlauftemperatur, Hochtemperatur-Wärmepumpe",
            paragraphs=[
                ("Entscheidend ist die Vorlauftemperatur: Fußbodenheizung braucht 30 bis 35 Grad, klassische "
                 "Altbau-Heizkörper oft 60 bis 70 Grad. Bis 55 Grad arbeitet eine moderne Wärmepumpe effizient, große "
                 "alte Heizkörper sind oft überdimensioniert, was ihr entgegenkommt. Für Heizkörper, die dauerhaft 60 bis "
                 "70 Grad brauchen, gibt es Hochtemperatur-Wärmepumpen; meist ist der Tausch einzelner Heizkörper günstiger."),
                ("Beispiel Altbau aus 1985 mit 160 m², teilweise gedämmt: Jahresarbeitszahl 2,8 bis 3,2, Stromkosten "
                 "1.680 bis 1.920 € statt 2.400 bis 3.000 € mit Gas. Nach Dämmung oder Fenstertausch sinken die Kosten "
                 "auf rund 900 bis 1.020 € im Jahr.*"),
            ],
            img=IMG["gen_detail"],
            alt="Fachkraft von EBZ Energie bei der Montage einer Anlage am Haus",
            bullets=[
                "Heizflächen-Check: Reichen die Heizkörper bei 50 bis 55 Grad Vorlauf?",
                "Keine Fußbodenheizung nötig, Nachrüstung möglich für 50 bis 120 € je m²",
                "Raus aus Öl und Gas: Demontage von Kessel und Tank übernehmen wir mit",
            ],
            reverse=True,
            cta=("/waermepumpe-im-altbau/", "Ratgeber: Wärmepumpe im Altbau"),
        ),
        C.media_text(
            eyebrow="Photovoltaik, Speicher und Energiemanagement",
            h2="Heizen und kühlen mit Solarstrom: Wärmepumpe, PV, Speicher, EMS",
            paragraphs=[
                ("Die Betriebskosten einer Wärmepumpe sind fast nur Stromkosten. Eigener Solarstrom kostet 10 bis 14 "
                 "ct/kWh, Netzstrom das Zwei- bis Dreifache. Für ein Haus mit Wärmepumpe empfehlen wir 10 bis 15 kWp "
                 "Photovoltaik und 10 bis 12 kWh Speicher; das Energiemanagement lädt über SG-Ready bei Sonnenüberschuss "
                 "Puffer- und Warmwasserspeicher vor."),
                ("Kühlen mit Wärmepumpe: Im Sommer kehrt sie den Kreislauf um und kühlt über Fußbodenheizung oder "
                 "Gebläsekonvektoren, nicht über klassische Heizkörper. Den Strom liefert mittags die PV-Anlage, genau "
                 "dann, wenn Kühlung gebraucht wird. Die PV-Anlage wird getrennt gefördert: 150 € je kWp und 150 € je kWh "
                 "Speicher, Fördercall bis 22. Oktober 2026."),
            ],
            img=IMG["ems"],
            alt="Energiemanagementsystem steuert Photovoltaik, Speicher und Wärmepumpe",
            bullets=[
                "PV-Anlage 10 kWp mit Speicher: rund 15.000 bis 22.000 € vor Förderung*",
                "Energiekosten für Heizung, Warmwasser und Haushalt: 50 bis 70 Prozent weniger*",
                a("photovoltaik", "Photovoltaikanlage") + ", " + a("batteriespeicher", "Batteriespeicher") + " und " + a("ems", "EMS für Wärmepumpe und PV") + " aus einer Hand",
            ],
            cta=("/photovoltaik-fuer-waermepumpe/", "Ratgeber: Photovoltaik für die Wärmepumpe"),
        ),
        C.cards_section(
            eyebrow="Lautstärke, Aufstellort, Hersteller",
            h2="Lautstärke, Aufstellort und Kältemittel: was wir vor Ort planen",
            intro=("Wie laut eine Luft-Wasser-Wärmepumpe ist, steht als Schallleistung dB(A) im Datenblatt. Entscheidend "
                   "ist der Aufstellort: nicht in Ecken oder zwischen zwei Wänden, weil Schall reflektiert wird, mit "
                   "Abstand zu Schlafzimmerfenstern und Nachbargrenze, mit Nachtmodus. Beides legen wir bei der "
                   "Vor-Ort-Prüfung fest."),
            cards=[
                {"ic": "⌂", "title": "Aufstellort",
                 "text": "Luft-Wasser: Außeneinheit auf Sockel oder Konsole, freie Luftansaugung, frostfreier Kondensatablauf, kurze Leitungswege zum Heizraum. Erd- und Grundwasser-Wärmepumpen stehen komplett im Haus."},
                {"ic": "◇", "title": "Kältemittel R290 (Propan)",
                 "text": "Natürliches Kältemittel mit sehr niedrigem Treibhauspotenzial, verdampft bei rund minus 42 Grad und ermöglicht hohe Vorlauftemperaturen. Weil es brennbar ist, gelten Abstandsregeln zu Fenstern, Türen und Lichtschächten."},
                {"ic": "✓", "title": "Hersteller: iDM, Ochsner, Lambda",
                 "text": "Wir planen herstellerunabhängig und setzen bevorzugt auf österreichische Hersteller wie iDM, Ochsner oder Lambda, je nach Gebäude, Vorlauftemperatur und Budget. Das passende Gerät steht im Festpreisangebot mit Datenblatt und Schallwerten."},
            ],
        ),
        C.media_text(
            eyebrow="Wärmepumpe für Gewerbe",
            h2="Für Ihren Betrieb: Heizkosten senken, Förderung nach Umsetzung",
            paragraphs=[
                ("Werkstatt, Bürogebäude, Vereinslokal oder Gemeindeamt: Im Betrieb laufen Heizsysteme länger und für "
                 "größere Flächen. Wir planen nach Heizlast und Lastprofil und stimmen die Wärmepumpe auf eine PV-Anlage "
                 "am Betriebsdach ab. Die Betriebsförderung der KPC (Umweltförderung im Betrieb) wird erst nach Umsetzung "
                 "beantragt, spätestens 6 Monate nach der Schlussrechnung; den Budgetstand prüfen wir vor dem Angebot."),
            ],
            img=IMG["gen_gewerbe"],
            alt="Große Photovoltaikanlage auf einem Gewerbedach, Stromquelle für die Wärmepumpe",
            bullets=[
                "Planung nach Heizlast, Lastprofil und Betriebszeiten",
                "Kombination mit PV-Anlage: Beispiel Gewerbe OÖ, 40 kWp, rund 13.500 € Ersparnis im Jahr",
                "Landesförderungen in vielen Fällen zusätzlich kombinierbar",
            ],
            reverse=True,
            anchor="gewerbe",
            cta=("kontakt", "Gewerbe-Beratung anfragen"),
        ),
        C.founder_story(
            eyebrow="Persönliche Beratung vor Ort",
            h2="Mario Zintl schaut sich Ihren Heizraum selbst an",
            paragraphs=[
                ("Eine Wärmepumpe kann man nicht aus dem Katalog verkaufen. Ob sie bei Ihnen gut läuft, entscheidet "
                 "sich im Heizraum, an den Heizkörpern und an der Dämmung. Deshalb kommen wir zu Ihnen nach Kärnten "
                 "oder in die Steiermark, bevor wir irgendetwas anbieten."),
                ("Dort rechnen wir gemeinsam: Was heizen Sie heute, welche Vorlauftemperatur brauchen Ihre Heizflächen, "
                 "was bringt die Kombination mit Photovoltaik. Manchmal ist die ehrliche Antwort, dass erst die Fenster "
                 "dran sind. Sie bekommen ein Festpreisangebot und den Förderweg dazu."),
            ],
            quote="Ich will, dass Ihre Wärmepumpe in zehn Jahren noch so läuft, wie wir es Ihnen heute sagen.",
            name=AUTHOR, role=AUTHOR_ROLE,
            badge="Villach, Kärnten",
            cta=("kontakt", "Vor-Ort-Termin vereinbaren"),
        ),
        C.media_text(
            eyebrow="Ihr Fachbetrieb aus Villach",
            h2="Ihr Wärmepumpen-Fachbetrieb aus Villach: Klagenfurt, Wolfsberg, Graz",
            paragraphs=[
                ("EBZ Energie GmbH ist Fachbetrieb für Wärmepumpe, Photovoltaik und Speicher mit Sitz in Villach "
                 "(Triglavstraße 15) und montiert in Kärnten und der Steiermark: von Villach über Klagenfurt und "
                 "Wolfsberg bis Graz. Über 300 dokumentierte Projekte in sechs Bundesländern, Google-Bewertung 4,9 "
                 "Sterne (Stand Oktober 2026)."),
                ("Für Ihre Wärmepumpe Installateur, Elektriker und Planer aus einem Betrieb: Heizraum, Elektrik, "
                 "PV-Anlage und Förderantrag laufen über einen Ansprechpartner, der auch nach der Übergabe erreichbar "
                 "bleibt."),
            ],
            img=IMG["team_quer"],
            alt="Team von EBZ Energie, Fachbetrieb für Wärmepumpe und Photovoltaik aus Villach",
            bullets=[
                "Zertifizierte Fachkräfte: Sanitär und Elektro fachgerecht in einem Projekt",
                "Förderung komplett abgewickelt: Landesantrag, Fristen, Endabrechnung",
                "Finanzierung mit 0 € Anzahlung und fixer Rate, Eigentum ab Tag 1",
            ],
            cta=("kontakt", "Vor-Ort-Termin vereinbaren"),
        ),
        C.reviews_slider(reviews, rating, count),
        C.steps_section(
            eyebrow="So läuft es ab",
            h2="Von der Beratung zur warmen Stube",
            steps=[
                ("Beratung", "Heizbedarf, Gebäude und Ziele. Kostenlos und ohne Verkaufsdruck.", ""),
                ("Vor-Ort-Prüfung", "Heizraum, Heizflächen, Dämmung, Elektrik und Aufstellort als Grundlage für Heizlast und Festpreisangebot.", ""),
                ("Förderung prüfen", "Landesförderung Kärnten oder Steiermark und Steuerbonus vor dem Auftrag, Budgetstand tagesaktuell.", ""),
                ("Montage", "Demontage der alten Heizung, Einbau, Sanitär und Elektro aus einer Hand.", "2 bis 4 Tage"),
                ("Inbetriebnahme", "Einregulierung, Übergabe, Endabrechnung der Förderung. Wir bleiben erreichbar.", ""),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section(
            "Mehr zur Wärmepumpe",
            [("/kosten-einer-waermepumpe/", "Kosten einer Wärmepumpe"),
             ("/waermepumpenfoerderung-in-oesterreich/", "Wärmepumpenförderung 2026"),
             ("/landesfoerderungen-fuer-die-waermepumpe/", "Landesförderungen Kärnten und Steiermark"),
             ("/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/", "Wärmepumpe steuerlich absetzen"),
             ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau"),
             ("/funktionsweise-einer-waermepumpe/", "So funktioniert eine Wärmepumpe"),
             ("/heizen-mit-waermepumpe/", "Heizen mit Wärmepumpe"),
             ("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"),
             ("/sanierungsoffensive-2026/", "Sanierungsoffensive 2026: was galt"),
             ("ems", "EMS für Wärmepumpe und PV"),
             ("finanzierung", "Wärmepumpe finanzieren"),
             ("referenzen", "Referenzen")],
        ),
        C.contact_section(
            headline="Ihre Wärmepumpe: kostenlos geprüft, zum Festpreis angeboten",
            sub=("Sagen Sie uns, wie Sie heute heizen. Wir prüfen Gebäude, Heizflächen, Aufstellort und Förderhöhe vor "
                 "Ort und sagen Ihnen ehrlich, was die Wärmepumpe bei Ihnen bringt. Kostenlos und unverbindlich."),
            page_label="Wärmepumpe",
        ),
        C.finalcta(
            "Noch eine Heizsaison mit Öl oder Gas?",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags und "
            "rechnen Heizkosten, Förderung und Photovoltaik für Ihr Haus durch.",
            trust=[(f"{NAP['rating']} auf Google", True), ("Luft-Wasser ab 12.000 €*", False),
                   ("Montage 2 bis 4 Tage", False), ("Kostenlos und unverbindlich", False)],
        ),
        _footnote(),
    ])

    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=IMG["waermepumpe"])
    return write_page(OUT_FILE, html)


def _footnote():
    return ("""
  <section class="section--tight section" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte 2026 für Österreich aus unseren Ratgebern, vor Förderung, Stand Oktober 2026.
      Beispielhaus mit 12.000 kWh Wärmebedarf, Jahresarbeitszahl 4, Strompreis 0,30 €/kWh. Förderlage laut
      umweltfoerderung.at (Bundesprogramme 2026 ausgeschöpft), Landesförderungen Kärnten und Steiermark sowie
      KPC-Betriebsförderung nach Stand der Richtlinien, laufend aktualisiert im Ratgeber. Tatsächliche Kosten,
      Ersparnis und Förderhöhe hängen von Gebäude, Heizsystem, Wärmequelle und Programmbudget ab. Fachlich geprüft
      von Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    import theme
    theme.write_assets()
    build()
