"""Standortseite Photovoltaik Villach (/photovoltaik-villach/).

Kommerzieller Suchintent "photovoltaik villach". Quelle: Live-Seite
/photovoltaik-villach/ (WP-Beitrag). Bereinigt: falsche Notstrom-Absaetze unter
"Finanzielle Entlastung" entfernt, "25 Jahre Leistungsgarantie" -> bis zu 30 Jahre,
Gedankenstriche, Superlative. Lokale Fakten nur aus Quelle bzw. Repo-Ratgeber
(Kaernten ueber 1.900 Sonnenstunden, rund 1.000 bis 1.100 kWh je kWp, Landespauschale 3.000 Euro).

SEO-Ueberarbeitung Oktober 2026 (build/seo/standort_villach.json): Genehmigung
(Mitteilungspflicht Kaernten) und Netzanschluss (Kaernten Netz) als eigene Sektion,
Ertrag je kWp, Local-Pack-Signale (NAP, Zeiten, 4,9 Sterne aus 111 Bewertungen) und eine
direkt zitierbare Antwortpassage fuer Konversations-Suchanfragen ("PV-Firma in Villach").
Foerderung nur als Kurzfassung, Details im Ratgeber. Kaernten-weiter Regionenblock entfernt
(stand identisch auf /photovoltaik-wolfsberg/).

Ueberarbeitung 10.10.2026 (README_standort.md, Briefing-Abschnitt "waermepumpe" in
build/seo/standort_villach.json):
- Waermepumpe als Sekundaerthema: eigene H2-Sektion (#waermepumpe), zwei FAQ, Links auf die
  Leistungsseite und die Ratgeber Kosten, Altbau, PV fuer Waermepumpe. Zahlen nur aus
  build/pages/waermepumpe.py (12.000 bis 22.000 EUR, Altbau 15.000 bis 28.000 EUR, 1 kWh Strom
  -> 4 bis 5 kWh Waerme, Beispielhaus 12.000 kWh / JAZ 4, Solarstrom 10 bis 14 ct).
- Foerderung Waermepumpe als Kurzfassung ohne Fristen und ohne Euro-Obergrenze: Bund ausgeschoepft,
  Land Kaernten 3.000 EUR Pauschale 2026 (Foerderblatt "Foerderungen 2026" auf maria-saal.gv.at, abgerufen
  10.10.2026; die 35 %/6.000 EUR galten nur bis 31.12.2025), Verweis auf foerderungen und foerderrechner.
- Lokale Quellen, abgerufen 10.10.2026: Fernwaermenetz Villach laut Stadt Villach
  (villach.at/stadt-service/energie); Kelag-Waermepumpen-Praemie 1.200 EUR, aktiver
  Kelag-Stromliefervertrag in Kaernten, Waermepumpe mit Internetanbindung, Gutschrift ueber zwei
  Jahre (kelag.at/privatkunden/ubersicht-zur-warmepumpe.htm).
- Von Klagenfurt entkoppelt (eigene Seite /photovoltaik-klagenfurt/, Key pv_klagenfurt):
  Klagenfurt aus Description, H2, Hero und Anbieter-Check genommen, ein sichtbarer Textlink plus
  Linkliste. Umland nur als Nennung: Faaker See, Velden, Finkenstein, Arnoldstein, Feldkirchen.
- Linkliste: andere Standortseiten (pv_klagenfurt, pv_wolfsberg, pv_graz, pv_steiermark) und
  foerderrechner.
"""

if __name__ == "__main__":  # Direktaufruf: build/ in den Suchpfad legen (build_all setzt ihn sonst)
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common import IMG, NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, S, faq_jsonld, u, a, href, tel_link, write_page, load_reviews, standorte, standort_schema
from layout import page
import components as C

PATH = "/photovoltaik-villach/"
TITLE = "Photovoltaik Villach: Fachbetrieb vor Ort | EBZ Energie"
DESC = ("Photovoltaik in Villach und Umgebung vom Fachbetrieb vor Ort: Planung, Montage, Speicher, "
        "Netzanmeldung und Förderung Kärnten aus einer Hand. 4,9 Sterne.")

HERO_IMG = "/assets/img/pv-villach-stadt.jpg"

MAPS_URL = "https://www.google.com/maps/search/?api=1&query=Triglavstra%C3%9Fe+15%2C+9500+Villach"

FAQ = [
    ("Was kostet eine 10 kWp PV-Anlage mit Speicher und Montage in Villach?",
     "Eine Komplettanlage mit rund 10 kWp und Speicher kostet in Villach typischerweise rund 15.000 bis 22.000 Euro "
     "vor Förderung, inklusive Montage, Netzanmeldung und Inbetriebnahme (EBZ-Richtpreis, Stand Oktober 2026). Davon "
     "gehen bis zu 3.000 Euro Landespauschale Kärnten und der EAG-Zuschuss des Bundes ab. Finanzierung ab 147 Euro "
     "im Monat* ist möglich."),
    ("Brauche ich in Kärnten eine Genehmigung für eine Photovoltaikanlage?",
     "Für Anlagen auf Dach oder Fassade gilt in Kärnten in der Regel eine Mitteilungspflicht statt einer "
     "Bewilligungspflicht: Die Gemeinde wird über das Vorhaben informiert, ein Bauverfahren entfällt meist. "
     "Sonderfälle wie Ortsbildschutz oder freistehende Anlagen klären wir für Sie mit der Baubehörde der Stadt Villach."),
    ("Wie viel Strom erzeugt eine PV-Anlage in Villach pro kWp?",
     "In Kärnten liegt der Jahresertrag bei rund 1.000 bis 1.100 kWh je kWp. Unsere Referenz in Villach, ein "
     "Einfamilienhaus mit 10 kWp in Ost-West-Ausrichtung, erzeugt rund 11.000 kWh im Jahr. Wie viel Ihr Dach "
     "hergibt, zeigt der Solarpotenzialkataster des Landes (KAGIS, Kärnten Atlas) und danach unser Projektbericht "
     "mit 3D-Belegplan, der auch die Verschattung durch die Berge berücksichtigt."),
    ("Wie lange dauert die Netzanmeldung bei Kärnten Netz?",
     "Wir melden Ihre Anlage mit den Daten aus dem Projektbericht beim Netzbetreiber an, in Villach und den meisten "
     "Gemeinden Kärntens ist das die Kärnten Netz GmbH. Der Netzbetreiber prüft die Einspeiseleistung, danach folgen "
     "Zählertausch und Fertigstellungsmeldung. Eine fixe Frist gibt es nicht; laut einer Kundenbewertung dauerte es bei "
     "einem Projekt fünf Wochen von der Beratung bis zur Fertigstellung."),
    ("Woran erkenne ich einen seriösen Photovoltaik-Anbieter in Villach?",
     "An zertifizierten Fachkräften und einem festen Ansprechpartner, an einem Projektbericht mit 3D-Belegplan und Statikreport, an "
     "schriftlichen Garantien (bis zu 30 Jahre Leistungs-, mindestens 10 Jahre Produktgarantie), an Referenzen mit "
     "Zahlen und an echten Google-Bewertungen. EBZ Energie: 300+ Projekte, 4,9 Sterne, Firmensitz Triglavstraße 15."),
    ("Lohnt sich ein Speicher in Kärnten?",
     "Ja, in den meisten Haushalten. Ohne Speicher nutzen Sie nur rund 30 Prozent Ihres Sonnenstroms selbst, mit "
     "Speicher bis zu 80 Prozent*. Dazu kommt die Förderung: 150 Euro je kWh vom Bund und die Landespauschale "
     "Kärnten, die einen Speicher ab 5 kWh voraussetzt. Mit Notstromfunktion bleibt Ihr Haus bei Netzausfall versorgt."),
    ("Was ändert sich 2026 bei Photovoltaik in Österreich?",
     "Ab 2027 plant der Bund laut BMWET eine Systemförderung für Speicher und intelligente Steuerung; die aktuellen "
     "Förderprogramme und Fristen stehen auf unserer Förderseite. Der OeMAG-Marktpreis lag im "
     "September 2026 bei 10,168 Cent je kWh (Juli: 6,146 Cent). Seit Oktober 2026 gilt das neue "
     "Elektrizitätswirtschaftsgesetz (ElWG)."),
    ("Was kostet eine Wärmepumpe in Villach inklusive Montage, und rechnet sie sich mit Photovoltaik?",
     "Eine Luft-Wasser-Wärmepumpe kostet im Einfamilienhaus rund 12.000 bis 22.000 Euro vor Förderung inklusive "
     "Montage, im Altbau mit Anpassungen an Heizkörpern und Verteilsystem 15.000 bis 28.000 Euro*. Mit Photovoltaik "
     "kommt ein Teil des Heizstroms vom eigenen Dach: Solarstrom kostet 10 bis 14 Cent je kWh, Netzstrom das Zwei- "
     "bis Dreifache*. Den Festpreis erhalten Sie, nachdem wir Heizraum, Heizkörper und Aufstellort bei Ihnen in "
     "Villach geprüft haben."),
    ("Welche Förderung gibt es für eine Wärmepumpe in Villach?",
     "Die Bundesförderung für den Heizungstausch ist ausgeschöpft, neue Registrierungen sind nicht möglich. Das Land "
     "Kärnten zahlt 2026 eine Pauschale von 3.000 Euro für den Umstieg auf eine Wärmepumpe im Eigenheim; ob das "
     "Budget reicht und welche Voraussetzungen für Ihr Haus gelten, prüfen wir vor dem Angebot. Kelag-Stromkunden mit aktivem "
     "Liefervertrag erhalten laut kelag.at zusätzlich eine Wärmepumpen-Prämie von 1.200 Euro als Gutschrift auf der "
     "Stromrechnung, verteilt über zwei Jahre, wenn die Wärmepumpe eine Internetanbindung hat. Den aktuellen Stand "
     "finden Sie auf unserer Förderseite und im Förderrechner."),
    ("Übernimmt EBZ Energie die Förderanträge und die Anmeldung beim Netzbetreiber?",
     "Ja. Wir kennen die Programme von Land Kärnten und Bund, bereiten die Anträge vor und kümmern uns um Mitteilung an "
     "die Gemeinde, Netzanmeldung, Zählertausch und Inbetriebnahme. Sie bekommen eine schlüsselfertige Anlage."),
    ("Kann ich bei EBZ Energie in Villach persönlich vorbeikommen?",
     "Ja, nach Terminvereinbarung in der Triglavstraße 15, 9500 Villach, Montag bis Freitag von 10:00 bis 20:00 Uhr. "
     "Die Beratung findet meist direkt bei Ihnen vor Ort statt, weil wir Dach, Zählerschrank und Verbrauch "
     "gleich mit aufnehmen."),
]


def build():
    rating, count, reviews = load_reviews()
    bew = f"{count} Bewertungen" if count else "echten Bewertungen"
    body = "".join([
        C.hero(
            eyebrow="Photovoltaik Villach",
            h1="Photovoltaik in Villach: PV-Anlage mit Speicher vom Fachbetrieb aus der Triglavstraße",
            lead=("Sonnenstrom vom eigenen Dach, geplant und montiert von einem Betrieb, der selbst in Villach "
                  "zuhause ist. Wir kommen zu Ihnen, prüfen Dach und Verbrauch und übernehmen Mitteilung an die "
                  "Gemeinde, Netzanmeldung bei Kärnten Netz, Förderung und Montage. Für Eigenheim und Betrieb in "
                  "Villach und Umgebung, vom Faaker See über Velden und Finkenstein bis Arnoldstein. Die "
                  "Wärmepumpe planen wir auf Wunsch gleich mit."),
            badges=[("Aus Villach", "für Villach"),
                    ("Förderung Kärnten", "inklusive Antrag"),
                    ("bis zu 85 %", "weniger Stromkosten")],
            img=HERO_IMG,
            img_alt="Stadtansicht von Villach in Kärnten, Standort von EBZ Energie",
            float_num=rating,
            float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_secondary=("#standort", "Standort und Kontakt"),
        ),
        C.kpis([
            ("rund 80 %", "weniger Stromkosten, EFH Villach (10 kWp)"),
            ("1.000 bis 1.100 kWh", "Jahresertrag je kWp in Kärnten"),
            ("3.000 €", "Landespauschale Kärnten für PV mit Speicher"),
            (NAP["rating"], f"Sterne auf Google, {bew}"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Warum sich Photovoltaik in Villach lohnt",
            paragraphs=[
                ("Villach liegt in einer der sonnenreichsten Regionen Österreichs: Kärnten kommt auf über 1.900 "
                 "Sonnenstunden und rund 1.000 bis 1.100 kWh Jahresertrag je kWp (Richtwert, Stand Oktober 2026). "
                 "Unsere Referenz in Villach liefert mit 10 kWp rund 11.000 kWh im Jahr. Wie viel Ihr Dach hergibt, "
                 "zeigt der Solarpotenzialkataster des Landes Kärnten (KAGIS)."),
                ("Was Villach besonders macht: Tallagen und Berge. Der Horizont schluckt am Morgen oder Abend ein paar "
                 "Prozent, deshalb rechnen wir die Verschattung im 3D-Belegplan für Ihr Dach mit, statt mit "
                 "Pauschalwerten zu arbeiten; der Statikreport, also der Statikbericht für Ihr Dach, gehört zu "
                 "jedem Projektbericht. Typisch rechnet sich eine Anlage in 4 bis 6 Jahren."),
            ],
        ),
        C.audience_split(
            eyebrow="Für wen planen wir in Villach?",
            h2="Eigenheim oder Betrieb in Villach und Umgebung: Ihre Anlage passt zu Ihrem Verbrauch",
            intro=("Jedes Dach und jeder Strombedarf ist anders. Wir legen Größe, Speicher und Wirtschaftlichkeit genau "
                   "darauf aus, in Villach genauso wie am Faaker See, in Velden, Finkenstein, Arnoldstein oder "
                   "Feldkirchen. Für die Landeshauptstadt gibt es eine eigene Seite: "
                   + a("pv_klagenfurt", "Photovoltaik in Klagenfurt") + "."),
            left={
                "img": IMG["gen_eigenheim"],
                "alt": "Einfamilienhaus mit Photovoltaikanlage in Kärnten",
                "title": "Für Ihr Zuhause in Villach",
                "bullets": [
                    "Bis zu 85 % weniger Stromkosten",
                    "Speicher, Notstrom und Wallbox für Abend, Netzausfall und E-Auto",
                    "Landespauschale Kärnten plus Bundesförderung, Finanzierung ab 147 € im Monat*",
                ],
                "cta": ("kontakt", "Beratung für mein Zuhause"),
            },
            right={
                "img": IMG["gen_gewerbe"],
                "alt": "Betriebsgebäude mit großer Photovoltaikanlage am Dach",
                "title": "Für Ihren Betrieb in Villach und Umgebung",
                "bullets": [
                    "Hoher Eigenverbrauch tagsüber senkt die Betriebskosten",
                    "Anlagen auch mit hoher kWp-Leistung, Planung nach Lastprofil",
                    "Beispiel Hotel Villach/Warmbad: 13 kWp, rund 4.200 € Ersparnis pro Jahr",
                ],
                "cta": ("pv_gewerbe", "Photovoltaik für Gewerbe"),
            },
        ),
        C.media_text(
            eyebrow="Behörde und Netzbetreiber",
            h2="Genehmigung und Netzanschluss in Kärnten: Mitteilungspflicht und Kärnten Netz",
            paragraphs=[
                ("Photovoltaikanlagen auf Dach und Fassade sind in Kärnten in der Regel mitteilungspflichtig, nicht "
                 "bewilligungspflichtig: Die Gemeinde wird über das Vorhaben informiert (Bauanzeige), ein Bauverfahren entfällt "
                 "meist. Den Netzanschluss beantragt der Errichter beim Netzbetreiber, in Villach und den meisten "
                 "Gemeinden Kärntens bei der Kärnten Netz GmbH, einer Tochter der Kelag "
                 "(Stand Oktober 2026)."),
                ("Der Netzbetreiber prüft die gewünschte Einspeiseleistung für Ihren Zählpunkt, danach folgen "
                 "Zählertausch auf den Smart Meter, Inbetriebnahme nach ÖNORM und Fertigstellungsmeldung. Wir reichen alle "
                 "Unterlagen mit den Daten aus dem Projektbericht ein, damit nichts nachgefordert wird, und klären "
                 "Sonderfälle wie Ortsbildschutz direkt mit der Baubehörde."),
            ],
            img=IMG["gen_detail"],
            alt="Montagedetail einer Photovoltaikanlage: Modulklemmen und Unterkonstruktion auf einem Dach in Kärnten",
            bullets=[
                "Mitteilung an die Gemeinde statt Bauverfahren (Dach- und Fassadenanlagen)",
                "Netzanmeldung bei Kärnten Netz mit Prüfung der Einspeiseleistung",
                "Zählertausch, Inbetriebnahme und Fertigstellungsmeldung durch EBZ Energie",
            ],
            cta=("foerderung_kaernten", "PV-Förderung Kärnten 2026"),
        ),
        C.problem_compare(
            eyebrow="Finanzielle Entlastung",
            h2="Was eine PV-Anlage in Villach kostet und was sie spart",
            intro=("Eine Komplettanlage mit rund 10 kWp und Speicher kostet rund 15.000 bis 22.000 € vor Förderung "
                   "(EBZ-Richtpreis, Stand Oktober 2026). Mit eigener Anlage werden Sie vom Konsumenten zum "
                   "Erzeuger: Ein großer Teil Ihres Stroms kommt vom Dach, zu Kosten, die über Jahrzehnte feststehen."),
            bars=[
                ("Stromkosten ohne eigene Anlage", 100, "bad", "voller Netzbezug"),
                ("Stromkosten mit Photovoltaik und Speicher", 15, "good", "bis zu 85 % weniger*"),
            ],
            aside=("Ihre Vorteile in Villach", [
                ("☀", "Eigener Strom", "Sie erzeugen Ihren Strom selbst und werden unabhängiger von Preissteigerungen."),
                ("€", "Förderung Kärnten", "3.000 € Landespauschale für private PV ab 5 kWp mit Speicher, dazu der EAG-Zuschuss des Bundes."),
                ("▮", "Speicher und Notstrom", "Sonnenstrom auch abends, Versorgung auch bei Netzausfall."),
                ("⌂", "Wertsteigerung", "Ein Haus mit eigener Energieversorgung gilt am Markt in Villach als zukunftssicher."),
            ]),
        ),
        C.media_text(
            eyebrow="Mehr Unabhängigkeit mit Speicher",
            h2="Eigenverbrauch, Speicher, Notstrom und Wallbox",
            paragraphs=[
                ("Ohne Speicher nutzen Sie Ihren Sonnenstrom nur, während die Sonne scheint, und speisen den "
                 "Überschuss für wenige Cent ein. Ein Stromspeicher hält den Strom vom Tag für Abend und Nacht "
                 "bereit, wenn der Bedarf im Haushalt am höchsten ist: Der Eigenverbrauch steigt von rund 30 auf "
                 "bis zu 80 Prozent*."),
                ("Deshalb planen wir Speicher, Notstrom oder Ersatzstrom und Wallbox als Teile eines Systems mit. "
                 "Die Wallbox lädt Ihr E-Auto bevorzugt mit Überschuss vom Dach, das Energiemanagement steuert "
                 "alles automatisch. Mit Notstromfunktion bleibt Ihr Zuhause in Villach auch bei einem "
                 "Stromausfall versorgt."),
            ],
            img=IMG["speicher"],
            alt="Batteriespeicher einer Photovoltaikanlage im Technikraum",
            bullets=[
                "Eigenverbrauch von rund 30 auf bis zu 80 Prozent*",
                "Notstrom oder Ersatzstrom bei Netzausfall",
                "Wallbox: E-Auto mit eigenem Sonnenstrom laden",
            ],
            reverse=True,
            cta=("batteriespeicher", "Mehr zum Batteriespeicher"),
        ),
        C.media_text(
            eyebrow="Wärmepumpe Villach",
            h2="Wärmepumpe in Villach: Heizungstausch mit Sonnenstrom vom eigenen Dach",
            paragraphs=[
                ("Wer in Villach, am Faaker See, in Finkenstein oder Arnoldstein den Öl- oder Gaskessel ersetzt, "
                 "braucht danach vor allem günstigen Strom. Eine Luft-Wasser-Wärmepumpe macht aus 1 kWh Strom 4 bis "
                 "5 kWh Wärme und kostet inklusive Montage rund 12.000 bis 22.000 € vor Förderung*. Ein Beispielhaus "
                 "mit 12.000 kWh Wärmebedarf braucht bei Jahresarbeitszahl 4 rund 3.000 kWh Strom im Jahr*, unsere "
                 "10-kWp-Referenz in Villach erzeugt rund 11.000 kWh. Deshalb nehmen wir Heizung und Photovoltaik in "
                 "einem Termin auf: Dach, Zählerschrank, Heizraum und Heizkörper."),
                ("Im Bestand entscheidet die Vorlauftemperatur: Bis 55 Grad arbeitet eine Wärmepumpe effizient, "
                 "vorhandene Heizkörper sind oft groß genug. Im Winter liefert das Dach weniger, als die Heizung "
                 "braucht; Warmwasser und Übergangszeit laufen dafür weitgehend mit eigenem Strom. Villach hat "
                 "außerdem ein Fernwärmenetz (Stadt Villach, villach.at): Liegt Ihr Haus im Versorgungsgebiet, lohnt "
                 "sich zuerst der Blick auf den Anschluss, das kann auch bei der Landesförderung eine Rolle spielen. "
                 "Wo kein Anschluss möglich ist, rechnen wir Ihnen die Wärmepumpe mit eigener Photovoltaik durch."),
                ("Zur Förderung in Kürze: Die Bundesförderung für den Heizungstausch ist ausgeschöpft. Das Land "
                 "Kärnten zahlt 2026 eine Pauschale von 3.000 € für den Umstieg auf die Wärmepumpe im Eigenheim; "
                 "Budget und Voraussetzungen prüfen wir für Ihr Haus vor dem Angebot. Den aktuellen Stand lesen Sie auf der Seite "
                 + a("foerderungen", "Förderungen im Überblick") + ", eine erste Zahl liefert der "
                 + a("foerderrechner", "Förderrechner") + "."),
            ],
            img=IMG["waermepumpe"],
            alt="Außeneinheit einer Luft-Wasser-Wärmepumpe neben einem Wohnhaus, Symbolbild für den Heizungstausch in Villach",
            bullets=[
                a("/kosten-einer-waermepumpe/", "Kosten einer Wärmepumpe") + ": alle Kostenblöcke vom Gerät bis zur Installation",
                a("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau") + ": Heizkörper, Vorlauftemperatur, Dämmung",
                a("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe") + ": Anlagengröße, Speicher, Steuerung",
            ],
            cta=("waermepumpe", "Wärmepumpe vom Fachbetrieb aus Villach"),
            anchor="waermepumpe",
        ),
        C.media_text(
            eyebrow="Förderung Kärnten",
            h2="Förderung für Photovoltaik in Villach: Landespauschale Kärnten und EAG",
            paragraphs=[
                ("Das Land Kärnten zahlt 2026 eine Pauschale von 3.000 Euro für neue private PV-Anlagen ab 5 kWp mit "
                 "Speicher ab 5 kWh. Der Bund fördert über den "
                 "EAG-Investitionszuschuss mit 150 Euro je kWp bis 10 kWp und 150 Euro je kWh Speicher, europäische "
                 "Komponenten bringen 10 Prozent Bonus (Stand Oktober 2026)."),
                ("Als Ihr Partner aus Villach übernehmen wir die Abwicklung: Wir prüfen, welche Programme zu Ihrem "
                 "Projekt passen, halten Fristen und Reihenfolge ein und bereiten die Anträge vor. Welche Fristen "
                 "gerade laufen, steht tagesaktuell auf unserer Förderseite; alle Details zur Landesförderung finden "
                 "Sie im Ratgeber."),
            ],
            img=IMG["foerderung"],
            alt="Beratung zur Photovoltaik-Förderung in Kärnten am Tisch",
            bullets=[
                "Landespauschale Kärnten 3.000 € für PV ab 5 kWp mit Speicher ab 5 kWh",
                "EAG-Investitionszuschuss 150 €/kWp bis 10 kWp und 150 €/kWh Speicher, 10 % Made-in-Europe-Bonus",
                "Antrag und Abwicklung durch EBZ Energie",
                a("foerderung_kaernten", "PV-Förderung Kärnten 2026 im Detail"),
            ],
            cta=("foerderungen", "Aktuelle Förderungen 2026"),
            dark=True,
        ),
        C.finance_band(),
        C.reference_cards(
            eyebrow="Referenz aus Villach",
            h2="Referenzen in Villach und am Wörthersee, mit Zahlen belegt",
            intro=("So sehen typische Anlagen aus unserer Region aus. Bild und Zahlen gehören jeweils zum selben "
                   "Projekt. Das Hotel in Villach/Warmbad (13 kWp bifazial, 27 kWh Speicher, rund 15.000 kWh und "
                   "4.200 € Ersparnis im Jahr) finden Sie auf der Referenzseite."),
            items=[
                {"img": IMG["ref_villach"],
                 "alt": "Photovoltaikanlage mit 10 kWp auf einem Einfamilienhaus in Villach",
                 "title": "Einfamilienhaus, Villach",
                 "specs": "10 kWp in Ost-West-Ausrichtung mit Notstrom, rund 11.000 kWh pro Jahr.",
                 "result": "rund 80 %", "result_sub": "weniger Stromkosten"},
                {"img": IMG["ref_krumpendorf"],
                 "alt": "Photovoltaikanlage auf einem Mehrparteienhaus in Krumpendorf am Wörthersee",
                 "title": "Mehrparteienhaus, Krumpendorf",
                 "specs": "25 kWp mit 25 kWh Speicher und Notstrom.",
                 "result": "4 Tage", "result_sub": "Bauzeit"},
            ],
        ),
        C.cards_section(
            eyebrow="Anbieter-Check",
            h2="Woran Sie einen seriösen Photovoltaik-Fachbetrieb in Villach erkennen",
            intro=("PV-Firma in Villach: EBZ Energie GmbH, Triglavstraße 15, 9500 Villach, zertifizierte "
                   f"Fachkräfte für die Montage, 300+ Projekte, {NAP['rating']} Sterne aus {bew} auf Google, Beratung vor Ort in "
                   "Villach, im Umland und in ganz Kärnten (Stand Oktober 2026). Bei der Suche nach Photovoltaik-Firmen "
                   "in Villach lohnt es sich, jeden Anbieter an diesen sechs Punkten zu messen."),
            cards=[
                {"ic": "✓", "title": "Zertifizierte Montage", "text": "Zertifizierte Fachkräfte für Dach und Elektrotechnik, ein fester Ansprechpartner von der Planung bis zur Übergabe."},
                {"ic": "◫", "title": "Projektbericht statt Pauschale", "text": "Projektbericht mit 3D-Belegplan und Statikreport für Ihr Dach, dazu ein Fixangebot."},
                {"ic": "◇", "title": "Garantien schriftlich", "text": "Bis zu 30 Jahre Leistungs- und mindestens 10 Jahre Produktgarantie auf die Module."},
                {"ic": "€", "title": "Behördenwege inklusive", "text": "Mitteilung an die Gemeinde, Netzanmeldung bei Kärnten Netz, Landespauschale und EAG-Antrag aus einer Hand."},
                {"ic": "★", "title": "Echte Bewertungen", "text": f"{NAP['rating']} Sterne aus {bew} auf Google, Local Pack Platz 1 für „Photovoltaik Villach“ (Oktober 2026)."},
                {"ic": "◉", "title": "Referenzen mit Zahlen", "text": "Anlagen in Villach, Warmbad, am Wörther- und Ossiachersee mit kWp, kWh und Ersparnis.",
                 "link_key": "referenzen", "link_text": "Referenzen in Kärnten"},
            ],
        ),
        C.founder_story(
            eyebrow="Persönliche Beratung vor Ort",
            h2="Mario Zintl und das Team in Villach",
            paragraphs=[
                ("Ich bin in Villach aufgewachsen und kenne die Dächer hier: Ost-West-Giebel in den Siedlungen, "
                 "Flachdächer in Warmbad, Mehrparteienhäuser am See. Wenn Sie anfragen, komme ich oder jemand "
                 "aus meinem Team persönlich vorbei und schaut sich Dach, Zählerschrank und Verbrauch an."),
                ("Sie bekommen keine Standardanlage aus dem Katalog, sondern einen Projektbericht mit 3D-Belegplan "
                 "und Statikreport für Ihr Haus. Und wenn eine kleinere Anlage besser passt, sage ich Ihnen das "
                 "genauso offen. Wir sind danach erreichbar, weil wir hier wohnen."),
            ],
            quote="Wir verkaufen keine Module, wir bauen Unabhängigkeit. In Villach seit dem ersten Tag.",
            name=AUTHOR, role=AUTHOR_ROLE,
            badge="Gebürtiger Villacher",
            cta=("kontakt", "Beratungstermin in Villach"),
        ),
        C.facts_panel(
            eyebrow="Standort Villach",
            h2="So erreichen Sie EBZ Energie in Villach",
            intro=("Unser Firmensitz liegt in der Triglavstraße in Villach. Besuche nach Terminvereinbarung, "
                   "die Beratung findet meist direkt bei Ihnen vor Ort statt."),
            rows=[
                ("Adresse", f"{NAP['name']}<br>{NAP['street']}, {NAP['zip']} {NAP['city']}"),
                ("Telefon", tel_link()),
                ("E-Mail", f'<a href="mailto:{NAP["email"]}">{NAP["email"]}</a>'),
                ("Öffnungszeiten", NAP["hours"]),
                ("Google-Bewertung", f"{NAP['rating']} von 5 aus {bew}"),
                ("Anfahrt", "Nach Terminvereinbarung. Für die Erstberatung kommen wir in der Regel zu Ihnen nach Villach oder in die Umgebung."),
                ("Einzugsgebiet", "Villach mit Faaker See, Velden am Wörthersee, Finkenstein, Arnoldstein und Feldkirchen, dazu Spittal an der Drau und Ossiachersee, ganz Kärnten und die Steiermark. Referenzen in 6 Bundesländern."),
                ("Netzbetreiber vor Ort", "Kärnten Netz GmbH (Villach und Umgebung)"),
            ],
            actions=[("Route planen", MAPS_URL, ' target="_blank" rel="noopener"'),
                     ("Anrufen", NAP["phone_href"], "")],
        ).replace('<section class="section"', '<section id="standort" class="section"', 1),
        C.reviews_slider(reviews, rating=rating, count=count),
        C.steps_section(
            eyebrow="So läuft es ab",
            h2="Von der Beratung in Villach bis zur Übergabe",
            steps=[
                ("Beratung vor Ort", "Wir besprechen Verbrauch, Dach und Ziele bei Ihnen in Villach. Kostenlos und unverbindlich.", ""),
                ("Projektbericht", "Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport sowie ein transparentes Fixangebot.", ""),
                ("Förderung, Gemeinde, Netz", "Landespauschale Kärnten, EAG-Antrag, Mitteilung an die Gemeinde und Netzanmeldung bei Kärnten Netz: Wir bereiten alles vor.", ""),
                ("Montage und Übergabe", "Zertifizierte Fachkräfte montieren, wir kümmern uns um Zählertausch, Inbetriebnahme und Einschulung.", ""),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section(
            "Photovoltaik und Wärmepumpe in Kärnten",
            [("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
             ("waermepumpe", "Wärmepumpe vom Fachbetrieb"),
             ("foerderung_kaernten", "PV-Förderung Kärnten 2026 im Detail"),
             ("foerderrechner", "Förderrechner: Ihre Förderung berechnen"),
             ("/kosten-einer-solaranlage/", "Was eine Solaranlage kostet"),
             ("/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/", "10 kWp Komplettanlage mit Speicher"),
             ("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"),
             ("batteriespeicher", "Stromspeicher"),
             ("/notstrom/", "Notstrom bei Stromausfall"),
             ("/energiegemeinschaft-villach-klagenfurt/", "Energiegemeinschaft Villach und Klagenfurt"),
             ("finanzierung", "Finanzierung ab 147 € im Monat"),
             ("referenzen", "Referenzen in Villach und Kärnten"),
             ("pv_klagenfurt", "Photovoltaik in Klagenfurt"),
             ("pv_wolfsberg", "Photovoltaik in Wolfsberg und im Lavanttal"),
             ("pv_graz", "Photovoltaik in Graz"),
             ("pv_steiermark", "Photovoltaik in der Steiermark")]
            + [(k, f"Photovoltaik {n}") for k, n in standorte("ktn", ohne="pv_villach") if k in ('pv_spittal', 'pv_feldkirchen', 'pv_hermagor')]
            + [("standorte", "Alle Standorte in Kärnten und der Steiermark")],
        ),
        C.contact_section(
            headline="Ihr kostenloses Angebot für Photovoltaik in Villach",
            sub=("Sie erreichen uns telefonisch oder über das Formular. Wir zeigen Ihnen ehrlich, was auf Ihrem "
                 "Dach in Villach möglich ist und was es kostet. Kostenlos und unverbindlich."),
            page_label="Photovoltaik Villach",
        ),
        C.finalcta(
            "Bereit für Sonnenstrom vom eigenen Dach in Villach?",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags und "
            "kommen zu Ihnen vor Ort.",
        ),
        _footnote(),
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=HERO_IMG, include_business_schema=True, extra_jsonld=standort_schema(PATH, "Villach", "Kärnten"))
    return write_page("photovoltaik-villach/index.html", html)


def _footnote():
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte auf Basis typischer Projekte, vor Förderung. Preis, Ersparnis, Eigenverbrauch und
      Amortisation hängen von Verbrauch, Anlagengröße, Ausrichtung und Strompreis ab. Finanzierung: Beispielkonditionen,
      vorbehaltlich Bonitätsprüfung. Fördersätze, Fristen und OeMAG-Marktpreis Stand Oktober 2026, Änderungen durch
      Fördergeber, Netzbetreiber und OeMAG vorbehalten. Wärmepumpe: Richtwerte aus unseren Ratgebern, vor Förderung,
      Beispielhaus mit 12.000 kWh Wärmebedarf und Jahresarbeitszahl 4; Förderhöhe abhängig von Richtlinie, Gebäude
      und Budget der Fördergeber. Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    import theme
    theme.write_assets()
    build()
