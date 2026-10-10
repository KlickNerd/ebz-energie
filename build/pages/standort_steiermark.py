"""Regionsseite Photovoltaik Steiermark (/photovoltaik-steiermark/), Slug-Key pv_steiermark.

Regionaler Ueberblick fuer Photovoltaik (Primaer) UND Waermepumpe (Sekundaer) in der Steiermark, kein
Stadtportraet: Bezirke im Montagegebiet, Baurecht, Netzbetreiber, Solarpotenzial, Foerderlage,
Energiegemeinschaft, zwei Grazer Referenzen. Briefing: build/seo/standort_steiermark.json / .md.
Die alte WordPress-Seite gleichen Pfads wurde nur als Themenliste angesehen (allgemeiner PV-Ratgeber mit
"sieben Vorteilen"), es wurden keine Texte und keine Zahlen uebernommen.

Ehrlichkeit: EBZ sitzt in Villach (Kaernten). Die Seite behauptet keinen steirischen Standort und keine
Referenzen ausserhalb von Graz. Keine Foerderfristen (Verweis auf foerderungen, foerderrechner, foerderung_steiermark).

LOKALE FAKTEN, alle am 10.10.2026 selbst abgerufen:
- Baurecht PV: Steiermaerkisches Baugesetz idF LGBl. Nr. 20/2026 (gueltig ab 28.02.2026), § 21 Abs. 1 Z 2 lit. o:
  PV und Solarthermie auf Dach-/Fassadenflaechen meldepflichtig (ohne Groessengrenze), Freiflaeche bis 100 kWp,
  Hoehe hoechstens 3,50 m; ueber 3,50 m § 20 Z 2 lit. l (vereinfachtes Verfahren). § 21 Abs. 3: schriftliche
  Mitteilung an die Gemeinde vor Ausfuehrung (Grundstuecknummer, Lage, kurze Beschreibung).
  Batterie § 21 Abs. 2 Z 2a: bis 20 kWh, bis 100 kWh mit Nachweis "thermal runaway". § 80b Abs. 2: Solarpflicht Neubau.
  Quelle: https://www.technik.steiermark.at/cms/beitrag/11549819/58813874/ (PDF Baugesetz_idF_LGBl_20_2026.pdf)
  und Erlaeuterungen zum Stmk. Deregulierungsgesetz LGBl. Nr. 19/2026 (gleiche Seite). Behoerde: Gemeinde, in Graz
  der Magistrat (Verfahrenshandbuch PV/Solarthermie, Abt. 13, Stand August 2025,
  https://www.verwaltung.steiermark.at/cms/dokumente/12898224_173036325/f51050a9/Verfahrenshandbuch%20Erneuerbare%20Energie%20PV%20und%20Solaranlagen.pdf).
  RIS war nicht abrufbar (Bot-Sperre), deshalb die konsolidierte Fassung des Landes.
- Baurecht Waermepumpe: § 21 Abs. 2 Z 2b (ortsfeste Aufstellung meldepflichtig) und Abs. 3 Z 5 (technisches
  Datenblatt, Bestaetigung eines befugten Sachverstaendigen zum Planungsbasispegel an der relevanten Grundgrenze).
- Netz: Energienetze Steiermark GmbH, Einspeiserportal, fuenf Schritte, Netzanschlusskonzept 12 Monate gueltig und
  einmal um 12 Monate verlaengerbar, netzwirksame Leistung: https://www.e-netze.at/Strom/Erzeugungsanlagen/Default.aspx
  Stromnetz Graz GmbH & Co KG als Verteilernetzbetreiber: von der E-Control genehmigte Allgemeine Bedingungen
  (e-control.at, Dokument stromnetz-graz-allgemeine-verteilernetzbedingungen-270614.pdf). Weitere Stadtnetze im
  "Netzbereich Steiermark" (Stadtwerke Voitsberg, Koeflach, Judenburg, Kapfenberg, Hartberg, Muerzzuschlag,
  Feistritzwerke-STEWEAG): Entwurf SNE-V 2018, 2. Novelle 2023 der E-Control (Kopie wko.at). ACHTUNG: Stand 2023,
  vor Livegang gegen die aktuelle SNE-V pruefen. stromnetz-graz.at selbst war nicht erreichbar (Timeout).
- Solarpotenzial Steiermark im Digitalen Atlas (Klassen, Jahresertrag, kWp, SolarTool-Bericht per E-Mail, GIS Graz
  hoeher aufgeloest): https://www.technik.steiermark.at/cms/ziel/99241573/DE/
- Foerderung PV: Umweltfoerderungen des Landes kennen kein Programm fuer private PV-Dachanlagen
  (https://www.wohnbau.steiermark.at/cms/ziel/165238232/DE/, Navigation). Steirischer Sanierungsbonus: 15 % der
  foerderbaren Kosten, PV bis 15 kWp je Wohneinheit, befristeter Sonder-Call (Richtlinie 01.04.2026,
  wohnbau.steiermark.at). Oekofonds: aktuell Ausschreibungen "Wasserstoffprojekte" und "Innovative Energiespeicher"
  (nur juristische Personen), KEINE offene PV-Ausschreibung: https://www.technik.steiermark.at/oekofonds
  Bund: build/seo/_fakten_2026-10.md.
- Foerderung Waermepumpe: ABWEICHUNG vom Auftrag ("35 % vom Land"). Die Landesseite sagt woertlich: "Eine
  Antragstellung/Registrierung ist fuer gefoerderte Biomasse-Heizungen, Waermepumpen und solarthermische Anlagen
  derzeit nicht moeglich. [...] auf absehbare Zeit keine Foerderungsmoeglichkeit seitens des Landes Steiermark"
  (https://www.wohnbau.steiermark.at/cms/ziel/165238232/DE/). Offen ist nur "Tausch erneuerbar betriebener
  Heizungssysteme" (mind. 15 Jahre alte Biomassekessel und Waermepumpen, max. 30 % der foerderungsfaehigen
  Investitionskosten, Budget 2026 700.000 Euro, 27 % verfuegbar am 06.10.2026):
  https://www.wohnbau.steiermark.at/cms/ziel/183599709/DE/ . Die 35 % stehen deshalb NICHT auf der Seite.
- Energiegemeinschaft: fuenf Buergerenergiemodelle, Quick Check im Serviceportal, Nahebereich (Trafostation lokal,
  Umspannwerk regional), neue Modelle Peer-to-Peer und Eigenversorgung seit Oktober 2026:
  https://www.e-netze.at/Strom/Energiegemeinschaften/ ; Anlaufstelle Energieagentur Steiermark:
  https://www.technik.steiermark.at/cms/ziel/165889217/DE/ . Rabattsaetze 57/28 % laut build/pages/README.md.
- Energieberatung Land Steiermark (produktunabhaengig): https://www.technik.steiermark.at/cms/ziel/82233481/DE/

BEWUSST WEGGELASSEN (keine selbst abgerufene offizielle Quelle): Sonnenstunden und Ertrag je kWp fuer die
Steiermark, Betraege von Gemeindefoerderungen, Oekofonds-Saetze fuer PV-Doppelnutzung (Ausschreibung nicht mehr
online), 125 Euro je kWp Energiesystem-Bonus, Fristen jeder Art, Entfernungen und Fahrzeiten.

Referenzen: nur die zwei Grazer Projekte aus referenz_projekte.py mit genau den dortigen Zahlen und Bildern.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # build/ (fuer Direktaufruf)

import common as _common
from common import IMG, NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, S, BASE, faq_jsonld, breadcrumb_jsonld, u, a, href, tel_link, write_page, load_reviews
from layout import page
import components as C

PATH = "/photovoltaik-steiermark/"
TITLE = "Photovoltaik Steiermark: PV & Wärmepumpe | EBZ Energie"
DESC = ("Photovoltaik und Wärmepumpe in der Steiermark: Planung, Montage, Meldung an die Gemeinde und "
        "Netzansuchen aus einer Hand. 2 Referenzen in Graz, 4,9 Sterne.")

STAND = "Stand Oktober 2026"

# Projekteigene Referenzbilder (build/static/img/, identisch mit referenz_projekte.R)
IMG_FLACHDACH_GRAZ = "/assets/img/ref-flachdach-graz-1.jpg"
IMG_STADTHAUS_GRAZ = "/assets/img/ref-stadthaus-graz-2.jpg"
REF_STADTHAUS = "/referenzen/projekt-stadthaus-in-graz/"
REF_FLACHDACH = "/referenzen/projekt-flachdach-in-graz/"

# Helfer aus common.py fuer die Ortsseiten der gemeinsamen Vorlage (verlinkt wird nur, was es schon gibt)
_standort_exists = getattr(_common, "standort_exists", lambda key: False)
_standorte = getattr(_common, "standorte", lambda land=None, ohne=None: [])

URL_SOLARPOTENZIAL = "https://www.technik.steiermark.at/cms/ziel/99241573/DE/"

QUELLEN = [
    ("Land Steiermark: Steiermärkisches Baugesetz, Fassung LGBl. Nr. 20/2026 (§ 21 Meldepflichtige Vorhaben, § 80b)",
     "https://www.technik.steiermark.at/cms/beitrag/11549819/58813874/"),
    ("Land Steiermark, Abteilung 13: Verfahrenshandbuch Photovoltaik- und Solarthermieanlagen",
     "https://www.verwaltung.steiermark.at/cms/dokumente/12898224_173036325/f51050a9/Verfahrenshandbuch%20Erneuerbare%20Energie%20PV%20und%20Solaranlagen.pdf"),
    ("Energienetze Steiermark: Erzeugungsanlagen und Einspeiserportal",
     "https://www.e-netze.at/Strom/Erzeugungsanlagen/Default.aspx"),
    ("Energienetze Steiermark: Energiegemeinschaften und Bürgerenergiemodelle",
     "https://www.e-netze.at/Strom/Energiegemeinschaften/"),
    ("E-Control: Allgemeine Bedingungen für den Zugang zum Verteilernetz der Stromnetz Graz GmbH & Co KG",
     "https://www.e-control.at/documents/1785851/1811363/stromnetz-graz-allgemeine-verteilernetzbedingungen-270614.pdf/b9e191a8-e26e-41b4-b916-4642ba567491"),
    ("Land Steiermark: Solarpotenzial Steiermark im Digitalen Atlas", URL_SOLARPOTENZIAL),
    ("Land Steiermark: Förderung von Wärmepumpen (Status der Antragstellung)",
     "https://www.wohnbau.steiermark.at/cms/ziel/165238232/DE/"),
    ("Land Steiermark: Förderung des Tausches erneuerbar betriebener Heizungssysteme",
     "https://www.wohnbau.steiermark.at/cms/ziel/183599709/DE/"),
    ("Land Steiermark: Ökofonds Steiermark, aktuelle Ausschreibungen",
     "https://www.technik.steiermark.at/oekofonds"),
    ("Land Steiermark: Energiegemeinschaften, Anlaufstelle Energieagentur Steiermark",
     "https://www.technik.steiermark.at/cms/ziel/165889217/DE/"),
]

# Bezirke im Montagegebiet: (Slug-Key oder None, Titel, Text). Orte sind die groesseren Gemeinden des Bezirks.
BEZIRKE = [
    ("pv_graz", "Graz",
     "Landeshauptstadt mit eigenem Stromnetz (Stromnetz Graz) und dem Magistrat als Baubehörde. Hier stehen unsere "
     "zwei steirischen Referenzen: ein Stadthaus mit 18 kWp und ein Einfamilienhaus mit 11,83 kWp, beide auf "
     "Flachdächern und ohne eine einzige Bohrung montiert."),
    (None, "Graz-Umgebung",
     "Seiersberg-Pirka, Gratwein-Straßengel, Frohnleiten, Kalsdorf, Premstätten, Hart bei Graz, Hausmannstätten und "
     "Lieboch: Einfamilienhäuser und Betriebe rund um die Landeshauptstadt. Welcher Netzbetreiber an Ihrer Adresse "
     "zuständig ist, klären wir vor der Planung."),
    ("pv_leibnitz", "Leibnitz",
     "Leibnitz, Wagna, Wildon, Gamlitz, Ehrenhausen und Straß in der Südsteiermark. Wohnhäuser, Weinbaubetriebe und "
     "landwirtschaftliche Dächer mit viel Fläche: Wir planen von der Hausanlage mit Speicher bis zum Betriebsdach."),
    ("pv_deutschlandsberg", "Deutschlandsberg",
     "Deutschlandsberg, Stainz, Frauental, Wies, Eibiswald und Bad Schwanberg in der Weststeiermark. Der Bezirk "
     "grenzt über Koralpe und Soboth an Kärnten, von unserem Montagegebiet im Lavanttal ist es der Nachbarbezirk."),
    ("pv_voitsberg", "Voitsberg",
     "Voitsberg, Köflach, Bärnbach, Ligist und Söding-Sankt Johann. In Voitsberg und Köflach betreiben die Stadtwerke "
     "eigene Stromnetze; dort läuft das Netzansuchen über das jeweilige Stadtwerk statt über das Landesnetz."),
    ("pv_weiz", "Weiz",
     "Weiz, Gleisdorf, Birkfeld, Passail und St. Ruprecht an der Raab in der Oststeiermark. Bestehende Anlagen "
     "ergänzen wir um Speicher, Wallbox oder Wärmepumpe, neue planen wir gleich als System."),
    ("pv_murtal", "Murtal",
     "Judenburg, Knittelfeld, Zeltweg, Fohnsdorf und Spielberg. In Judenburg betreiben die Stadtwerke ein eigenes "
     "Stromnetz. In Tallagen rechnen wir die Verschattung durch die Berge im 3D-Belegplan mit, statt mit "
     "Pauschalwerten zu arbeiten."),
    ("pv_leoben", "Leoben",
     "Leoben, Trofaiach, St. Michael in Obersteiermark, Niklasdorf und Eisenerz. Für Wohnhäuser und Betriebe legen "
     "wir die Anlage nach dem Verbrauch aus, nicht nach der größtmöglichen Dachbelegung."),
    ("pv_suedoststeiermark", "Südoststeiermark",
     "Feldbach, Fehring, Bad Gleichenberg, Mureck und Bad Radkersburg. Einfamilienhäuser und landwirtschaftliche "
     "Betriebe: Mit Speicher bleibt der Sonnenstrom im Haus, statt mittags ins Netz zu gehen."),
]

FAQ = [
    ("Brauche ich in der Steiermark eine Baubewilligung für eine Photovoltaikanlage?",
     "Für Anlagen auf Dach- oder Fassadenflächen nein: Sie sind nach § 21 des Steiermärkischen Baugesetzes "
     "meldepflichtig, seit der Novelle 2026 unabhängig von der Größe. Die Gemeinde (in Graz der Magistrat) wird vor "
     "der Ausführung schriftlich informiert, mit Grundstücksnummer, Lage am Grundstück und kurzer Beschreibung. Eine "
     "Bewilligung im vereinfachten Verfahren braucht die Anlage erst, wenn sie höher als 3,50 Meter ist. Zusätzlich "
     "ist das Ansuchen beim Netzbetreiber nötig (Stand Oktober 2026)."),
    ("Welche Netzbetreiber gibt es in der Steiermark?",
     "Das Landesnetz betreibt die Energienetze Steiermark GmbH, die Stadt Graz versorgt die Stromnetz Graz GmbH & Co "
     "KG. Dazu kommen Stadtnetze, unter anderem der Stadtwerke Voitsberg, Köflach, Judenburg, Kapfenberg, Hartberg "
     "und Mürzzuschlag sowie der Feistritzwerke-STEWEAG. Der Netzbetreiber hängt an der Adresse und lässt sich nicht "
     "wählen. Im Landesnetz läuft das Ansuchen über das Einspeiserportal, das Netzanschlusskonzept gilt 12 Monate "
     "und kann einmal um 12 Monate verlängert werden."),
    ("Gibt es in der Steiermark eine Landesförderung für Photovoltaik?",
     "Eine Pauschale für private Dachanlagen wie in Kärnten gibt es nicht. Der Bund fördert 2026 mit 150 Euro je kWp "
     "bis 10 kWp und 150 Euro je kWh Speicher. Das Land vergibt den Steirischen Sanierungsbonus (15 Prozent der "
     "förderbaren Kosten) nur in befristeten Sonderausschreibungen, der Ökofonds richtet sich mit einzelnen "
     "Ausschreibungen an Betriebe, Gemeinden und Energiegemeinschaften. Manche Gemeinden zahlen einen eigenen "
     "Zuschuss. Was gerade offen ist, zeigt unsere Förderseite."),
    ("Was kostet eine PV-Anlage mit Speicher in der Steiermark?",
     "Eine Komplettanlage mit rund 10 kWp und Speicher kostet rund 15.000 bis 22.000 Euro vor Förderung, inklusive "
     "Montage, Netzansuchen und Inbetriebnahme (EBZ-Richtpreis, Stand Oktober 2026). Zum Vergleich unsere Referenzen "
     "in Graz: Das Einfamilienhaus mit 11,83 kWp und 20 kWh Speicher spart rund 3.500 Euro Stromkosten im Jahr*, das "
     "Stadthaus mit 18 kWp und 18 kWh Speicher rund 5.000 Euro*. Finanzierung ab 147 Euro im Monat* ist möglich."),
    ("Ist Photovoltaik in der Steiermark verpflichtend?",
     "Für bestehende Häuser nicht. Bei Neubauten schreibt § 80b des Steiermärkischen Baugesetzes eine Solaranlage "
     "vor: Wohngebäude mit mehr als 100 Quadratmetern konditionierter Brutto-Grundfläche brauchen je angefangene 100 "
     "Quadratmeter mindestens 3 Quadratmeter Photovoltaik oder 1 Quadratmeter Solarthermie. Für andere Gebäude mit "
     "mehr als 250 Quadratmetern oberirdischer Bruttogeschoßfläche gelten 6 Quadratmeter Photovoltaik oder 2 "
     "Quadratmeter Solarthermie je angefangene 100 Quadratmeter. Wirtschaftlich sinnvoll ist meist deutlich mehr als "
     "dieses Minimum."),
    ("Brauche ich in der Steiermark eine Genehmigung für eine Wärmepumpe?",
     "Die ortsfeste Aufstellung einer Wärmepumpe ist seit der Baugesetz-Novelle 2026 meldepflichtig, ein "
     "Bewilligungsverfahren entfällt. Der Meldung an die Gemeinde liegen das technische Datenblatt und die "
     "Bestätigung eines befugten Sachverständigen bei, dass der zulässige Planungsbasispegel an der Grundgrenze zum "
     "nächstgelegenen Nachbargrundstück eingehalten wird. Für die Meldung zählt also der Schall an der Grenze; "
     "deshalb planen wir Aufstellort und Gerät gemeinsam."),
    ("Welche Förderung gibt es 2026 für eine Wärmepumpe in der Steiermark?",
     "Stand Oktober 2026 wenig: Die Bundesförderung für den Heizungstausch ist ausgeschöpft, und das Land Steiermark "
     "nimmt für den Umstieg von einer fossilen Heizung auf eine Wärmepumpe derzeit keine Anträge an. Offen ist das "
     "Landesprogramm für den Tausch mindestens 15 Jahre alter Wärmepumpen und Biomassekessel in Ein- und "
     "Zweifamilienhäusern, mit höchstens 30 Prozent der förderungsfähigen Investitionskosten und begrenztem Budget. "
     "Wir prüfen den Stand vor jedem Angebot; die Energieberatung des Landes Steiermark berät produktunabhängig."),
    ("Kann ich meinen Sonnenstrom in der Steiermark in einer Energiegemeinschaft teilen?",
     "Ja. Im Nahbereich sinkt das Netzentgelt in einer Erneuerbare-Energie-Gemeinschaft um bis zu 57 Prozent (lokal) "
     "oder 28 Prozent (regional). Österreichweit funktioniert es über die Bürgerenergiegemeinschaft, dann ohne diesen "
     "Rabatt. Ob zwei Zählpunkte im selben Nahbereich liegen, zeigt im Landesnetz der Quick Check im Serviceportal "
     "der Energienetze Steiermark."),
    ("EBZ Energie sitzt in Villach: In welchen steirischen Bezirken montieren Sie?",
     "In Graz, Graz-Umgebung, Leibnitz, Deutschlandsberg, Voitsberg, Weiz, im Murtal, in Leoben und in der "
     "Südoststeiermark. Unser einziger Firmensitz ist die Triglavstraße 15 in Villach, ein Büro in der Steiermark "
     "haben wir nicht. Die Beratung findet bei Ihnen vor Ort statt, montiert wird mit zertifizierten Fachkräften, und "
     "Sie haben einen festen Ansprechpartner von der Planung bis zur Übergabe. Andere Bezirke fragen Sie bitte an."),
]


def _bezirk_cards():
    cards = []
    for key, name, text in BEZIRKE:
        card = {"ic": "⌖", "title": name, "text": text}
        if key == "pv_graz" or (key and _standort_exists(key)):
            card["link_key"] = key
            card["link_text"] = f"Photovoltaik {name}"
        cards.append(card)
    return cards


def _ext(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'


def _quellen():
    lis = "".join(f'<li><a href="{url}" rel="nofollow noopener" target="_blank">{label}</a></li>'
                  for label, url in QUELLEN)
    return f"""
  <section class="section section--tight">
    <div class="wrap" style="max-width:860px">
      <div class="art-eeat">
        <img src="{IMG['mario']}" alt="{AUTHOR}, {AUTHOR_ROLE}" width="92" height="92" loading="lazy">
        <p><b>Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</b> Die Angaben zu Baurecht, Netzbetreibern,
        Solarpotenzial und Förderlage in der Steiermark stammen aus den unten verlinkten amtlichen und offiziellen
        Quellen, {STAND}. Förderungen und Netzbedingungen ändern sich; verbindlich ist immer die Auskunft der
        zuständigen Stelle.</p>
      </div>
      <div class="art-sources"><p><b>Quellen für die Steiermark</b></p><ul>{lis}</ul></div>
    </div>
  </section>"""


def _service_jsonld():
    data = {
        "@context": "https://schema.org", "@type": "Service",
        "@id": u(PATH).rstrip("/") + "/#service",
        "serviceType": "Photovoltaik, Batteriespeicher und Wärmepumpe: Planung, Montage und Förderabwicklung",
        "name": "Photovoltaik und Wärmepumpe in der Steiermark",
        "areaServed": {"@type": "AdministrativeArea", "name": "Steiermark",
                       "containedInPlace": {"@type": "Country", "name": "Österreich"}},
        "provider": {"@type": "SolarInstallation", "@id": BASE + "/#business", "name": NAP["name"],
                     "telephone": NAP["phone_display"], "url": BASE + "/",
                     "address": {"@type": "PostalAddress", "streetAddress": NAP["street"], "postalCode": NAP["zip"],
                                 "addressLocality": NAP["city"], "addressCountry": NAP["country"]}},
        "url": u(PATH),
    }
    return json.dumps(data, ensure_ascii=False)


def build():
    rating, count, reviews = load_reviews()
    bew = f"{count} Bewertungen" if count else "echten Bewertungen"
    orte = [(k, f"Photovoltaik {n}") for k, n in _standorte("stmk", ohne="pv_graz")]
    hub = [("standorte", "Alle Standorte")] if "standorte" in S else []
    body = "".join([
        C.hero(
            eyebrow="Photovoltaik Steiermark · Wärmepumpe · Speicher",
            h1="Photovoltaik in der Steiermark: PV-Anlage, Speicher und Wärmepumpe vom Fachbetrieb aus Villach",
            lead=("EBZ Energie plant und montiert PV-Anlagen, Speicher und Wärmepumpen von Graz über Leibnitz und "
                  "Deutschlandsberg bis ins Murtal. Unser Firmensitz ist Villach in Kärnten, zur Beratung kommen wir "
                  "zu Ihnen. Wir übernehmen die Meldung an Ihre Gemeinde, das Ansuchen beim Netzbetreiber und die "
                  "Förderanträge."),
            badges=[("Graz bis Murtal", "Montagegebiet Steiermark"),
                    ("Meldung genügt", "für PV am Dach seit 2026"),
                    ("bis zu 85 %", "weniger Stromkosten")],
            img=IMG_FLACHDACH_GRAZ,
            img_alt=("Drohnenaufnahme: Photovoltaikanlage mit 11,83 kWp auf dem Flachdach eines Einfamilienhauses in "
                     "Graz, Referenzprojekt von EBZ Energie"),
            float_num=rating,
            float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_secondary=("#bezirke", "Bezirke und Orte"),
        ),
        C.kpis([
            ("2 Referenzen", "in Graz, mit Ertrag und Ersparnis belegt"),
            ("rund 20.000 kWh", "Jahresertrag Stadthaus Graz mit 18 kWp"),
            ("150 €/kWp", "Bundeszuschuss 2026 bis 10 kWp, dazu 150 €/kWh Speicher"),
            (NAP["rating"], f"Sterne auf Google, {bew}"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Photovoltaik und Wärmepumpe in der Steiermark: was hier anders läuft als in Kärnten",
            paragraphs=[
                ("Photovoltaik Steiermark heißt bei EBZ Energie: ein Fachbetrieb mit Sitz in Villach "
                 "(Triglavstraße 15), der in Kärnten und der Steiermark plant und mit zertifizierten Fachkräften "
                 f"montiert. Dahinter stehen 300+ dokumentierte Projekte und {NAP['rating']} Sterne aus {bew} auf "
                 f"Google ({STAND})."),
                ("Drei Dinge unterscheiden die Steiermark von Kärnten. Das Land zahlt keine Pauschale für private "
                 "PV-Anlagen, es bleibt der Zuschuss des Bundes. Für Anlagen auf Dach und Fassade genügt seit der "
                 "Baugesetz-Novelle 2026 eine schriftliche Meldung an die Gemeinde, unabhängig von der Größe. Und "
                 "neben dem Landesnetz der Energienetze Steiermark gibt es eigene Stadtnetze, etwa in Graz. Alle "
                 "drei Punkte klären wir für Ihre Adresse, bevor Sie etwas unterschreiben."),
            ],
            max_w="76ch",
        ),
        C.cards_section(
            eyebrow="Montagegebiet Steiermark",
            h2="PV-Anlage in der Steiermark: Bezirke und Orte, in denen wir planen und montieren",
            intro=("Wer eine PV-Anlage in der Steiermark sucht, sucht meist im eigenen Bezirk. In diesen neun "
                   "Regionen beraten wir bei Ihnen zu Hause oder im Betrieb und montieren Photovoltaik, Speicher und "
                   "Wärmepumpe. Hartberg-Fürstenfeld, Bruck-Mürzzuschlag, Liezen oder Murau: Fragen Sie an, wir "
                   "sagen Ihnen ehrlich, ob wir Ihr Projekt übernehmen können."),
            cards=_bezirk_cards(),
        ).replace('<section class="section"', '<section id="bezirke" class="section"', 1),
        C.media_text(
            eyebrow="Baurecht Steiermark",
            h2="PV-Anlage genehmigen in der Steiermark: Meldung an die Gemeinde statt Baubewilligung",
            paragraphs=[
                ("Photovoltaikanlagen auf Dach- oder Fassadenflächen sind nach § 21 des Steiermärkischen "
                 "Baugesetzes meldepflichtig, seit der Novelle 2026 unabhängig von ihrer Größe. Das Vorhaben wird der "
                 "Gemeinde vor der Ausführung schriftlich mitgeteilt, in Graz dem Magistrat: Grundstücksnummer, Lage "
                 "am Grundstück und eine kurze Beschreibung genügen. Erst eine Anlage, die höher als 3,50 Meter "
                 f"aufbaut, braucht eine Bewilligung im vereinfachten Verfahren ({STAND})."),
                ("Auch der Speicher ist geregelt: Batterieanlagen bis 20 kWh sind meldepflichtig, bis 100 kWh "
                 "ebenfalls, wenn der Hersteller nachweist, dass das thermische Durchgehen einer Zelle keinen Brand "
                 "der Anlage auslöst. Anlagen auf der Freifläche bleiben bis 100 kWp meldepflichtig. Die Bau- und "
                 "Raumordnungsvorschriften gelten auch für gemeldete Vorhaben; Sonderfälle wie Schutzzonen klären wir "
                 "mit der Baubehörde."),
            ],
            img=IMG["gen_detail"],
            alt="Montagedetail einer Photovoltaikanlage: Modulklemmen und Unterkonstruktion auf einem Dach (Symbolbild)",
            bullets=[
                "Dach und Fassade: schriftliche Meldung an die Gemeinde, unabhängig von der Anlagengröße",
                "Speicher bis 20 kWh meldepflichtig, bis 100 kWh mit Nachweis des Herstellers",
                "Neubau: Wohngebäude über 100 m² brauchen ohnehin eine Solaranlage (§ 80b Baugesetz)",
                "Wir bereiten die Meldung mit den Daten aus dem Projektbericht vor",
            ],
        ),
        C.facts_panel(
            eyebrow="Netzanschluss",
            h2="Netzbetreiber in der Steiermark: Energienetze Steiermark, Stromnetz Graz und Stadtwerke",
            intro=("Den Netzbetreiber können Sie nicht wählen, er hängt an der Adresse. Er beurteilt, wie viel "
                   "Leistung Ihre Anlage einspeisen darf. Wir stellen das Ansuchen, bevor wir Module bestellen."),
            rows=[
                ("Landesnetz", "Energienetze Steiermark GmbH. Erzeugungsanlagen werden über das Einspeiserportal angesucht."),
                ("Stadt Graz", "Stromnetz Graz GmbH & Co KG, eigener Netzbereich. Mehr dazu auf der Seite "
                 + a("pv_graz", "Photovoltaik in Graz") + "."),
                ("Weitere Stadtnetze", "Unter anderem Stadtwerke Voitsberg, Köflach, Judenburg, Kapfenberg, Hartberg "
                 "und Mürzzuschlag sowie die Feistritzwerke-STEWEAG."),
                ("Ablauf im Landesnetz", "Einspeisezählpunkt ansuchen, Netzanschlusskonzept erhalten, Anlage errichten, "
                 "Installationsdokument übermitteln, Inbetriebnahme in Abstimmung mit dem Netzbetreiber."),
                ("Gültigkeit", "Das Netzanschlusskonzept gilt 12 Monate und kann einmal um 12 Monate verlängert werden. "
                 "Läuft es ab, wird die reservierte Netzkapazität wieder frei."),
                ("Einspeiseleistung", "Der Netzbetreiber legt die netzwirksame Leistung fest. Die Modulleistung darf "
                 "höher sein, wenn die Anlage die Einspeisung technisch begrenzt."),
                ("Wer ansucht", "EBZ Energie, mit den Daten aus dem Projektbericht. Für die Inbetriebnahme braucht es "
                 "außerdem einen Abnehmer für den Überschussstrom; auch das bereiten wir mit Ihnen vor."),
            ],
        ),
        C.text_block(
            eyebrow="Solardachkataster",
            h2="Solarpotenzial Steiermark: Ihr Dach im Digitalen Atlas prüfen",
            paragraphs=[
                ("Das Land Steiermark zeigt im Digitalen Atlas die Karte "
                 + _ext(URL_SOLARPOTENZIAL, "Solarpotenzial Steiermark")
                 + ". Sie stuft Dachflächen nach der Globalstrahlung als sehr gut geeignet, gut geeignet oder geeignet "
                 "ein und nennt den zu erwartenden Jahresertrag und die mögliche Leistung in kWp. Das SolarTool "
                 "schickt für selbst gewählte Flächen einen Bericht per E-Mail, für Graz gibt es im GIS der Stadt "
                 "eine höher aufgelöste Darstellung einzelner Dachteilflächen."),
                ("Die Karte ist ein guter erster Blick, eine Planung ersetzt sie nicht: Statik, Zählerschrank, "
                 "Leitungswege und die Verschattung durch Kamine oder Nachbargebäude nehmen wir vor Ort auf. Das "
                 "Ergebnis ist unser Projektbericht mit 3D-Belegplan und Statikreport."),
            ],
            max_w="76ch",
        ),
        C.media_text(
            eyebrow="Förderung Steiermark",
            h2="Förderung für Photovoltaik in der Steiermark: Bundeszuschuss statt Landespauschale",
            paragraphs=[
                ("Das Land Steiermark zahlt keine Pauschale für private PV-Anlagen auf dem Dach. Die verlässliche "
                 "Förderung kommt vom Bund: 2026 gibt es über den EAG-Investitionszuschuss 150 Euro je kWp bis 10 kWp "
                 "und 150 Euro je kWh Speicher, europäische Komponenten bringen je 10 Prozent Bonus. Ab 2027 plant "
                 f"der Bund laut BMWET eine Systemförderung für Speicher mit intelligenter Steuerung ({STAND})."),
                ("Vom Land kommen zwei Bausteine, die nicht dauernd offen sind: der Steirische Sanierungsbonus "
                 "(15 Prozent der förderbaren Kosten, auch für PV bis 15 kWp je Wohneinheit, als befristete "
                 "Sonderausschreibung) und der Ökofonds, der einzelne Ausschreibungen für Betriebe, Gemeinden und "
                 "Energiegemeinschaften auflegt, derzeit für innovative Energiespeicher. Manche Gemeinden zahlen einen "
                 "eigenen Zuschuss; das fragen wir für Ihre Adresse ab. Welche Programme gerade laufen, steht auf "
                 "unserer Förderseite."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Förderung einer Photovoltaikanlage am Tisch",
            bullets=[
                "Bund: 150 €/kWp bis 10 kWp und 150 €/kWh Speicher, 10 % Bonus je europäischer Komponente",
                "Land: keine PV-Pauschale, Sanierungsbonus und Ökofonds nur in befristeten Ausschreibungen",
                "Gemeinde: Zuschuss je nach Wohnort, wir fragen nach",
                a("foerderung_steiermark", "PV-Förderung Steiermark im Detail") + " und "
                + a("foerderrechner", "Förderrechner"),
            ],
            cta=("foerderungen", "Aktuelle Förderungen ansehen"),
            dark=True,
        ),
        C.finance_band(),
        C.media_text(
            eyebrow="Wärmepumpe Steiermark",
            h2="Wärmepumpe in der Steiermark: Meldepflicht, Schallnachweis und Förderlage",
            paragraphs=[
                ("Wir planen und installieren Wärmepumpen für Ein- und Zweifamilienhäuser in der Steiermark, auf "
                 "Wunsch gemeinsam mit der PV-Anlage. Baurechtlich ist die ortsfeste Aufstellung einer Wärmepumpe "
                 "seit der Baugesetz-Novelle 2026 nur noch meldepflichtig, unabhängig von der Leistung. Der Meldung "
                 "an die Gemeinde liegen das technische Datenblatt und die Bestätigung eines befugten "
                 "Sachverständigen bei, dass der zulässige Planungsbasispegel an der Grundgrenze zum nächsten "
                 "Nachbarn eingehalten wird."),
                ("Deshalb beginnt unsere Planung beim Aufstellort und bei der Schallleistung des Geräts. Bei der "
                 "Förderung sind wir offen: Die Bundesförderung für den Heizungstausch ist ausgeschöpft, und das Land "
                 "Steiermark nimmt für den Umstieg von Öl oder Gas auf eine Wärmepumpe derzeit keine Anträge an. "
                 "Offen ist ein Landesprogramm für den Tausch mindestens 15 Jahre alter Wärmepumpen und "
                 "Biomassekessel mit höchstens 30 Prozent der förderungsfähigen Investitionskosten, solange das "
                 f"Budget reicht ({STAND})."),
                ("Eine Luft-Wasser-Wärmepumpe kostet im Einfamilienhaus 12.000 bis 22.000 Euro vor Förderung "
                 "inklusive Installation*. Mit Sonnenstrom vom eigenen Dach sinken die Betriebskosten: Das "
                 "Energiemanagement lässt die Wärmepumpe bevorzugt laufen, wenn die PV-Anlage Überschuss liefert."),
            ],
            img=IMG["waermepumpe"],
            alt="Außeneinheit einer Luft-Wasser-Wärmepumpe an einem Wohnhaus (Symbolbild)",
            bullets=[
                "Meldung an die Gemeinde mit Datenblatt und Schallbestätigung, kein Bewilligungsverfahren",
                "Bund ausgeschöpft, Land: Umstieg von Öl und Gas derzeit ohne Antragsmöglichkeit",
                "Tausch alter Wärmepumpen und Biomassekessel: höchstens 30 % vom Land, Budget begrenzt",
                a("/landesfoerderungen-fuer-die-waermepumpe/", "Landesförderungen für die Wärmepumpe") + ", "
                + a("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau") + ", "
                + a("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"),
            ],
            reverse=True,
            cta=("waermepumpe", "Wärmepumpe vom Fachbetrieb"),
            anchor="waermepumpe",
        ),
        C.media_text(
            eyebrow="Energiegemeinschaft Steiermark",
            h2="Energiegemeinschaft in der Steiermark: Strom teilen im Nahbereich oder österreichweit",
            paragraphs=[
                ("Überschuss, den Sie nicht selbst verbrauchen, können Sie in einer Energiegemeinschaft an Nachbarn, "
                 "Familie oder Betriebe weitergeben. In der Erneuerbare-Energie-Gemeinschaft sinkt das Netzentgelt im "
                 "Nahbereich um bis zu 57 Prozent (lokal, dieselbe Trafostation) oder 28 Prozent (regional, dasselbe "
                 "Umspannwerk). Österreichweit, etwa mit der Tochter in Wien, geht es über die "
                 "Bürgerenergiegemeinschaft, dann ohne diesen Rabatt."),
                ("Der Nahbereich wird innerhalb eines Netzgebiets bestimmt. Im Serviceportal der Energienetze "
                 "Steiermark zeigt ein Quick Check, ob zwei Zählpunkte lokal oder regional verbunden sind. Seit "
                 "Oktober 2026 lassen sich auch Peer-to-Peer-Verträge (Strom direkt an einen anderen Haushalt, ohne "
                 "Verein) und die Eigenversorgung mehrerer eigener Standorte registrieren. Das Land hat bei der "
                 "Energieagentur Steiermark eine Anlaufstelle für Energiegemeinschaften eingerichtet; EBZ Energie "
                 "rechnet über die Plattform energyfamily ab."),
            ],
            img=IMG["eg_drohne"],
            alt="Wohngebiet aus der Luft, Symbolbild für das Netzgebiet einer lokalen Energiegemeinschaft",
            bullets=[
                "Bis zu 57 % (lokal) oder 28 % (regional) weniger Netzentgelt, nur im Nahbereich",
                "Österreichweit über die Bürgerenergiegemeinschaft, ohne Netzentgelt-Rabatt",
                "Quick Check im Serviceportal der Energienetze Steiermark zeigt den Nahbereich",
                a("/energiegemeinschaft-steiermark/", "Ratgeber: Energiegemeinschaft Steiermark"),
            ],
            cta=("eg_privat", "Energiegemeinschaft für Privathaushalte"),
        ),
        C.reference_cards(
            eyebrow="Referenzen in der Steiermark",
            h2="Was Photovoltaik in der Steiermark kostet und bringt: zwei Anlagen aus Graz",
            intro=("Eine Komplettanlage mit rund 10 kWp und Speicher kostet rund 15.000 bis 22.000 € vor Förderung "
                   f"(EBZ-Richtpreis, {STAND}). Was dabei herauskommt, zeigen unsere zwei veröffentlichten Projekte in "
                   "der Steiermark. Bild und Zahlen gehören jeweils zum selben Projekt; aus den anderen Bezirken gibt "
                   "es noch keine veröffentlichte Referenz."),
            items=[
                {"img": IMG_STADTHAUS_GRAZ,
                 "alt": "Aufgeständerte Module auf dem begrünten Flachdach des Stadthauses in Graz, ohne Dachdurchdringung montiert",
                 "title": a(REF_STADTHAUS, "Stadthaus, Graz"),
                 "specs": ("18 kWp auf drei Flachdächern in Süd und Ost, ballastiert ohne Bohrung, 18 kWh Speicher, "
                           "Wallbox 11 kW und Notstrom. Rund 20.000 kWh im Jahr, Amortisation ca. 4 Jahre*."),
                 "result": "rund 5.000 €", "result_sub": "Ersparnis pro Jahr*"},
                {"img": IMG_FLACHDACH_GRAZ,
                 "alt": "Zwei ballastierte Modulfelder in Südausrichtung auf dem Flachdach eines Einfamilienhauses in Graz",
                 "title": a(REF_FLACHDACH, "Einfamilienhaus mit Flachdach, Graz"),
                 "specs": ("11,83 kWp in Südausrichtung auf Sarnafil-Folie, ballastiert ohne Bohrung, 20 kWh Speicher, "
                           "Wallbox 11 kW und Notstrom. Rund 13.000 kWh im Jahr, Amortisation ca. 5 Jahre*."),
                 "result": "rund 3.500 €", "result_sub": "Ersparnis pro Jahr*"},
            ],
        ),
        C.why_section(
            eyebrow="Photovoltaik-Anbieter Steiermark",
            h2="Photovoltaik-Firmen in der Steiermark vergleichen: sechs Fragen an jeden Anbieter",
            items=[
                ("⌂", "Wo sitzt der Betrieb?",
                 "Fragen Sie nach Firmensitz und Ansprechpartner. EBZ Energie sitzt in Villach, Triglavstraße 15, und "
                 "sagt das dazu. Beraten und montiert wird bei Ihnen in der Steiermark."),
                ("◷", "Wann kommt das Netzansuchen?",
                 "Vor der Bestellung. Erst das Netzanschlusskonzept zeigt, welche Einspeiseleistung an Ihrem Anschluss "
                 "möglich ist und ob Kosten für den Netzanschluss entstehen."),
                ("◇", "Was steht im Angebot?",
                 "Ein Projektbericht mit 3D-Belegplan und Statikreport, Datenblätter und ein Fixpreis. Dazu die "
                 "Garantien schriftlich: bis zu 30 Jahre Leistungsgarantie, mindestens 10 Jahre Produktgarantie."),
                ("✓", "Wer übernimmt die Behördenwege?",
                 "Meldung an die Gemeinde, Einspeiserportal, Förderantrag und Fertigmeldung gehören in eine Hand. Bei "
                 "der Wärmepumpe kommt die Schallbestätigung dazu."),
                ("☀", "Gibt es Referenzen mit Zahlen?",
                 "kWp, Jahresertrag und Ersparnis statt Fotos ohne Daten. Unsere steirischen Beispiele stehen in Graz, "
                 "weitere Projekte aus sechs Bundesländern auf der " + a("referenzen", "Referenzseite") + "."),
                ("€", "Wem gehört die Anlage?",
                 "Bei uns Ihnen, ab dem ersten Tag, auch mit " + a("finanzierung", "Finanzierung")
                 + ": 0 € Anzahlung, fixe Rate, kein Grundbucheintrag."),
            ],
        ),
        C.facts_panel(
            eyebrow="Firmensitz und Kontakt",
            h2="EBZ Energie: Sitz in Villach, Beratung und Montage in der Steiermark",
            intro=("Wir haben kein Büro in der Steiermark und behaupten auch keines. Die Erstberatung findet bei Ihnen "
                   "zu Hause oder im Betrieb statt, weil wir Dach, Zählerschrank und Heizraum ohnehin sehen müssen."),
            rows=[
                ("Firmensitz", f"{NAP['name']}<br>{NAP['street']}, {NAP['zip']} {NAP['city']}, Kärnten"),
                ("Telefon", tel_link()),
                ("E-Mail", f'<a href="mailto:{NAP["email"]}">{NAP["email"]}</a>'),
                ("Erreichbar", NAP["hours"]),
                ("Google-Bewertung", f"{NAP['rating']} von 5 aus {bew}"),
                ("Montagegebiet Steiermark", "Graz, Graz-Umgebung, Leibnitz, Deutschlandsberg, Voitsberg, Weiz, "
                 "Murtal, Leoben und Südoststeiermark; weitere Bezirke auf Anfrage."),
                ("Leistungen", "Photovoltaik, Batteriespeicher, Wärmepumpe, Energiemanagement, Wallbox und "
                 "Energiegemeinschaft, für Eigenheim und Betrieb."),
                ("Referenzen", "300+ dokumentierte Projekte in 6 Bundesländern, in der Steiermark zwei veröffentlichte "
                 "Projekte in Graz."),
            ],
            actions=[("Anrufen", NAP["phone_href"], ""),
                     ("Beratung anfragen", "#beratung", "")],
        ).replace('<section class="section"', '<section id="standort" class="section"', 1),
        C.reviews_slider(reviews, rating=rating, count=count),
        C.steps_section(
            eyebrow="So läuft es ab",
            h2="Von der Anfrage bis zur Inbetriebnahme in der Steiermark",
            steps=[
                ("Beratung bei Ihnen", "Wir kommen zu Ihnen in die Steiermark und nehmen Dach, Zählerschrank, "
                 "Verbrauch und Heizung auf. Kostenlos und unverbindlich.", ""),
                ("Projektbericht und Netzansuchen", "Sie erhalten den Projektbericht mit 3D-Belegplan und "
                 "Statikreport und ein Fixangebot. Parallel suchen wir beim Netzbetreiber um den Einspeisezählpunkt an.", ""),
                ("Meldung und Förderung", "Schriftliche Meldung an die Gemeinde, Förderantrag beim Bund und, wo "
                 "vorhanden, bei der Gemeinde. Die richtige Reihenfolge halten wir für Sie ein.", ""),
                ("Montage und Inbetriebnahme", "Zertifizierte Fachkräfte montieren. Danach übermitteln wir das "
                 "Installationsdokument, die Inbetriebnahme erfolgt in Abstimmung mit dem Netzbetreiber.", ""),
            ],
        ),
        C.faq_section(FAQ),
        _quellen(),
        C.linkgrid_section(
            "Weiterlesen: Photovoltaik und Wärmepumpe in der Steiermark",
            [("pv_graz", "Photovoltaik in Graz")] + orte + [
                ("foerderung_steiermark", "PV-Förderung Steiermark im Detail"),
                ("foerderungen", "Alle Förderungen im Überblick"),
                ("foerderrechner", "Förderrechner"),
                ("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
                ("waermepumpe", "Wärmepumpe"),
                ("batteriespeicher", "Batteriespeicher"),
                ("ems", "Energiemanagementsystem"),
                ("/energiegemeinschaft-steiermark/", "Energiegemeinschaft Steiermark"),
                ("/kosten-einer-waermepumpe/", "Kosten einer Wärmepumpe"),
                ("solarrechner", "Solarrechner"),
                ("finanzierung", "Finanzierung ab 147 € im Monat"),
                ("referenzen", "Alle Referenzen"),
            ] + hub,
        ),
        C.contact_section(
            headline="Ihr kostenloses Angebot für Photovoltaik und Wärmepumpe in der Steiermark",
            sub=("Sie erreichen uns telefonisch oder über das Formular. Nennen Sie uns Ort, Dach und Heizung, wir "
                 "sagen Ihnen ehrlich, was möglich ist, was es kostet und welche Förderung gerade offen ist. "
                 "Kostenlos und unverbindlich."),
            page_label="Photovoltaik Steiermark",
        ),
        C.finalcta(
            "Bereit für eigenen Strom und saubere Wärme in der Steiermark?",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags und kommen "
            "zu Ihnen vor Ort.",
        ),
        _footnote(),
    ])
    crumbs = [("Startseite", u("/"))]
    if "standorte" in S:
        crumbs.append(("Standorte", u("standorte")))
    crumbs.append(("Photovoltaik Steiermark", u(PATH)))
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ), og_image=IMG_FLACHDACH_GRAZ,
                extra_jsonld=[breadcrumb_jsonld(crumbs), _service_jsonld()])
    return write_page("photovoltaik-steiermark/index.html", html)


def _footnote():
    return f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte auf Basis typischer Projekte, vor Förderung. Ersparnis, Jahresertrag und
      Amortisation der Referenzen sind Projektwerte und hängen von Verbrauch, Anlagengröße, Ausrichtung und Strompreis
      ab. Preisspanne Wärmepumpe: Richtwert für ein Einfamilienhaus, der Festpreis folgt nach der Prüfung vor Ort.
      Finanzierung: Beispielkonditionen, vorbehaltlich Bonitätsprüfung. Fördersätze, Baurecht und Netzbedingungen
      {STAND}, Änderungen durch Gesetzgeber, Fördergeber und Netzbetreiber vorbehalten. Firmensitz von EBZ Energie ist
      Villach; in der Steiermark beraten und montieren wir vor Ort. Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>"""


if __name__ == "__main__":
    import theme
    theme.write_assets()
    sys.exit(1 if build() else 0)
