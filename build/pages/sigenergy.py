"""Marken-/Leistungsseite Sigenergy (/sigenergy/).

Ziel-Keywords (Google Ads, Oesterreich, 19.11.2026): sigenergy 1.900, sigenergy wallbox 170,
sigenergy speicher preis 140, sigenergy erfahrungen 140, sigenergy oesterreich 90, sigenergy preis 70,
sigenergy app 70, sigenergy installateur 30, sigenergy notstrom 20, sigen gateway 20.

Produktfakten: ausschliesslich aus den Herstellerunterlagen, recherchiert am 19.11.2026
(Faktenblatt mit allen Quell-URLs: Sitzungsnotiz sigenergy_fakten.md, Kernquellen in QUELLEN unten).
EBZ-Fakten: die acht Referenzprojekte mit Sigenergy aus pages/referenz_projekte.py (Zahlen identisch).

Bewusst NICHT behauptet (nicht belegt bzw. nicht freigegeben):
- kein "offizieller Sigenergy-Partner" / "zertifizierter Installateur" (Kunde muss bestaetigen)
- keine Sigenergy-Endkundenpreise (keine serioese Quelle), nur der freigegebene Richtpreis-Anker
- keine Restkapazitaet in der Garantie (Europa-Fassung 60 %, Deutschland-Fassung 80 %, AT unklar)
- keine Aussage "SigenStor ist EMS-foerderfaehig" (Klimafonds hat keine Produktliste, lokale
  Steuerung ohne Internet ist Pruefkriterium, bei integriertem EMS nur separat ausgewiesene Mehrkosten)
- V2H/V2G nur als "vorbereitet, abhaengig vom Fahrzeug"
"""

from common import IMG, NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page
from layout import page
import components as C

PATH = "/sigenergy/"
TITLE = "Sigenergy Speicher Österreich: Preis, Erfahrungen | EBZ Energie"
DESC = ("SigenStor von Sigenergy: Wechselrichter, LFP-Speicher, Energiemanagement und Wallbox in einem System. "
        "Erfahrungen aus acht EBZ-Projekten, Preise und Notstrom in Kärnten und der Steiermark.")
STAND = "Stand November 2026"

QUELLEN = [
    ("Sigenergy: Produktseite SigenStor", "https://www.sigenergy.com/de/products/sigenstor"),
    ("Sigenergy: Datenblatt Sigen Energy Controller (Version 20260330)",
     "https://wwwstatic.sigenergy.com/content/assets/uploads/en_download/1774951281792375.pdf"),
    ("Sigenergy: Datenblatt Sigen Battery 6.0 / 10.0",
     "https://wwwstatic.sigenergy.com/content/assets/uploads/en_download/1758200906743690.pdf"),
    ("Sigenergy: Datenblatt Sigen Battery 5.0 / 8.0",
     "https://wwwstatic.sigenergy.com/content/assets/uploads/en_download/1745981044645769.pdf"),
    ("Sigenergy: Sigen Energy Gateway", "https://www.sigenergy.com/de/products/gateway"),
    ("Sigenergy: Datenblatt EV DC Charging Module (Version 20260609)",
     "https://wwwstatic.sigenergy.com/upload/2026-06-17/1781667822045_5fbd5d79-e80a-4a9c-bfd8-b34a5d10a1a6.pdf"),
    ("Sigenergy: AC-Wallbox", "https://www.sigenergy.com/de/products/ac-charger"),
    ("Sigenergy: mySigen App", "https://www.sigenergy.com/de/products/mysigen-app"),
    ("Sigenergy: Garantiebedingungen", "https://www.sigenergy.com/de/support/warranty"),
    ("Sigenergy: Unternehmen", "https://www.sigenergy.com/de/about"),
    ("Klima- und Energiefonds: Leitfaden Energiemanagement private Haushalte 2026",
     "https://www.umweltfoerderung.at/fileadmin/user_upload/umweltfoerderung/private/Energiemanagement/ems_private_leitfaden.pdf"),
]

FAQ = [
    ("Was ist Sigenergy und was ist SigenStor?",
     "Sigenergy ist ein Hersteller von Wechselrichtern und Batteriespeichern mit Sitz in Shanghai, Markteinführung "
     "2022, seit April 2026 an der Börse Hongkong. SigenStor ist das Heimspeichersystem: Wechselrichter, "
     "Batterie-Wechselrichter, LFP-Batteriemodule und Energiemanagement in einem Turm, optional mit DC-Lademodul fürs "
     "E-Auto. Der Hersteller nennt das eine 5-in-1-Lösung."),
    ("Was kostet ein Sigenergy Speicher?",
     "Das hängt von der Zahl der Batteriemodule, der Wechselrichtergröße und dem Zubehör ab, etwa Gateway für "
     "Notstrom oder Wallbox. Als Orientierung: Eine 10-kWp-Photovoltaikanlage mit Speicher kostet "
     f"{CLAIMS['richtpreis_10kwp']}.* Ein Fixangebot für Ihr Haus bekommen Sie nach der kostenlosen Beratung vor Ort, "
     "mit Speichergröße passend zu Ihrem Verbrauch."),
    ("Welche Erfahrungen hat EBZ Energie mit Sigenergy?",
     "Acht der zehn Referenzprojekte auf unserer Website laufen mit einem Sigenergy-System: vom Einfamilienhaus mit "
     "9 kWh Speicher bis zum Gewerbebetrieb mit 40 kWh, teils mit automatischem Notstrom, teils mit Wallbox. Alle "
     "Projekte mit Eckdaten und Ersparnis finden Sie auf unserer Referenzseite."),
    ("Kann ich einen Sigenergy Speicher später erweitern?",
     "Ja. An einen Energy Controller passen laut Hersteller 1 bis 6 Batteriemodule. Jedes Modul hat einen eigenen "
     "DC-Wandler, deshalb lassen sich neue und ältere Module gemeinsam betreiben. Kommen E-Auto oder Wärmepumpe dazu, "
     "stocken wir den Speicher auf, ohne das System zu tauschen."),
    ("Funktioniert Sigenergy bei Stromausfall (Notstrom)?",
     "Mit dem Sigen Energy Gateway ja: Es erkennt den Netzausfall und versorgt das Haus weiter, laut Hersteller ohne "
     "Unterbrechung auf der Lastseite (0 ms). Ohne Gateway planen wir je nach Anlage eine manuelle Umschaltung für "
     "wichtige Verbraucher. Welche Lösung bei Ihnen passt, klären wir in der Beratung."),
    ("Gibt es eine Sigenergy Wallbox?",
     "Ja, zwei Varianten: eine AC-Wallbox mit bis zu 22 kW und ein DC-Lademodul mit 12,5 oder 25 kW, das direkt in "
     "den SigenStor-Turm kommt. Beide können mit PV-Überschuss laden. Das DC-Modul ist laut Hersteller bidirektional "
     "vorbereitet; ob das E-Auto Strom zurückgeben kann, hängt vom Fahrzeug ab."),
    ("Welche Garantie gibt Sigenergy?",
     "Der Hersteller gibt 10 Jahre Produktgarantie auf Batteriemodule und Energy Controller, kostenpflichtig "
     "verlängerbar auf bis zu 15 Jahre. Bedingung: Das System muss für Updates mit dem Internet verbunden sein. Ist es "
     "insgesamt länger als ein Jahr offline, verkürzt sich die Garantie laut Bedingungen auf 5 Jahre."),
    ("Ist das Energiemanagement von Sigenergy förderfähig?",
     "Der Klima- und Energiefonds fördert 2026 Energiemanagementsysteme mit 50 %, maximal 600 €. Eine Produktliste gibt "
     "es nicht: Gefordert sind unter anderem aktive Steuerung, Preissignale und eine lokale Steuerung, die ohne "
     "Internet funktioniert. Bei einem im Speicher integrierten EMS sind nur separat ausgewiesene Mehrkosten "
     "förderbar. Ob das für Ihre Anlage zutrifft, prüfen wir vor dem Angebot."),
    ("Wo installiert EBZ Energie Sigenergy-Systeme?",
     "Wir planen und montieren in Kärnten und der Steiermark, Beratung vor Ort inklusive. Referenzen mit Sigenergy "
     "haben wir zusätzlich in Wien, Niederösterreich, Oberösterreich und im Burgenland."),
]


def _table(eyebrow, h2, intro, headers, rows, note=""):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join(
        "<tr>" + "".join(f'<td class="{"hl" if i == 0 else ""}">{c}</td>' for i, c in enumerate(r)) + "</tr>"
        for r in rows
    )
    note_html = f'<p class="form-note center eg-reveal" style="margin-top:18px">{note}</p>' if note else ""
    return f"""
  <section class="section" style="background:#fff;border-block:1px solid var(--line)">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">{eyebrow}</p>
      <h2 class="center eg-reveal">{h2}</h2>
      <p class="lead center eg-reveal" style="max-width:72ch;margin-inline:auto">{intro}</p>
      <div class="art-tablewrap eg-reveal" style="margin-top:32px">
        <table class="art-table"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>
      </div>
      {note_html}
    </div>
  </section>"""


REFS = [
    {"img": "/assets/img/gewerbe-dach-ooe.jpg",
     "alt": "Drohnenaufnahme der 40-kWp-Photovoltaikanlage in Ost-West-Ausrichtung auf dem Trapezblechdach eines Gewerbebetriebs in Oberösterreich",
     "title": "Gewerbebetrieb Oberösterreich",
     "specs": "40 kWp Ost-West · 40 kWh Speicher · Sigenergy All-in-One",
     "result": "~13.500 €", "result_sub": "Ersparnis pro Jahr*",
     "href": "/referenzen/projekt-gewerbe-oberoesterreich/"},
    {"img": "/assets/img/ref-hotel-villach-1.jpg",
     "alt": "Hotel in Villach/Warmbad mit aufgeständerten Glas-Glas-Modulen in Südausrichtung auf dem Flachdach",
     "title": "Hotel Villach/Warmbad",
     "specs": "13 kWp Süd · 27 kWh Speicher · Notstrom automatisch über Gatewaybox",
     "result": "~4.200 €", "result_sub": "Ersparnis pro Jahr*",
     "href": "/referenzen/projekt-pv-anlage-hotel-villach/"},
    {"img": "/assets/img/ref-stadthaus-graz-1.jpg",
     "alt": "Aufgeständerte Glas-Glas-Module auf den begrünten Flachdächern eines Stadthauses in Graz",
     "title": "Stadthaus Graz",
     "specs": "18 kWp · 18 kWh Speicher · Wallbox 11 kW · Notstrom manuell",
     "result": "~5.000 €", "result_sub": "Ersparnis pro Jahr*",
     "href": "/referenzen/projekt-stadthaus-in-graz/"},
    {"img": "/assets/img/ref-wien-1.jpg",
     "alt": "Wohnhaus in Wien mit Photovoltaik-Modulen in Süd- und Ostausrichtung auf dem Schindeldach",
     "title": "Wohnhaus Wien",
     "specs": "10,92 kWp · 20 kWh Speicher · Wallbox 11 kW · Warmwasser aus PV-Überschuss",
     "result": "~12.000 kWh", "result_sub": "Jahresertrag, Amortisation ca. 6 Jahre*",
     "href": "/referenzen/projekt-pv-wien/"},
    {"img": "/assets/img/ref-ossiachersee-1.jpg",
     "alt": "Einfamilienhaus am Ossiachersee mit Photovoltaik-Modulen auf dem Ziegeldach",
     "title": "Einfamilienhaus Ossiachersee",
     "specs": "10 kWp Ost-West · 9 kWh Speicher · Wallbox 11 kW im selben System",
     "result": "~3.200 €", "result_sub": "Ersparnis pro Jahr*",
     "href": "/referenzen/projekt-pv-am-ossiachersee/"},
    {"img": "/assets/img/ref-flachdach-graz-1.jpg",
     "alt": "Drohnen-Draufsicht auf zwei Modulfelder der Photovoltaikanlage auf dem Flachdach eines Einfamilienhauses in Graz",
     "title": "Flachdach Graz",
     "specs": "11,83 kWp Süd · 20 kWh Speicher · Wallbox 11 kW",
     "result": "~3.500 €", "result_sub": "Ersparnis pro Jahr*",
     "href": "/referenzen/projekt-flachdach-in-graz/"},
]


def _quellen():
    lis = "".join(f'<li><a href="{url}" rel="nofollow noopener" target="_blank">{label}</a></li>'
                  for label, url in QUELLEN)
    return f"""
  <section class="section section--tight">
    <div class="wrap" style="max-width:860px">
      <div class="art-eeat">
        <img src="{IMG['mario']}" alt="{AUTHOR}, {AUTHOR_ROLE}" width="92" height="92" loading="lazy">
        <p><b>Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</b> Die technischen Angaben stammen aus den unten
        verlinkten Datenblättern und Bedingungen von Sigenergy und dem Förderleitfaden des Klima- und Energiefonds,
        {STAND}. Die Projektdaten stammen aus unseren eigenen Projektunterlagen.</p>
      </div>
      <div class="art-sources"><p><b>Quellen</b></p><ul>{lis}</ul></div>
    </div>
  </section>"""


def build():
    reviews = [
        ("Von der ersten Beratung bis zur fertigen Umsetzung unserer 15-kWp-Photovoltaikanlage auf dem Flachdach "
         "inklusive Sigenergy-Speicher war alles äußerst professionell und perfekt organisiert.…",
         "Andrei Gligor, Google-Rezension, September 2026"),
        ("Mit EBZ Energie habe ich durchweg sehr positive Erfahrungen bei der Erweiterung meiner bestehenden "
         "5-kWp-PV-Anlage gemacht. Ziel war die Skalierung um weitere 20 kWp inklusive Batteriespeicher sowie…",
         "Tom Stenger, Google-Rezension, Jänner 2026"),
        ("Tolle Firma, zuverlässig, sehr bemüht...vor allem Herr Zintl Mario, super Erstberatung und bis zur "
         "Inbetriebnahme sehr bemüht...alles super geklappt.",
         "Anton Riepl, Google-Rezension, Dezember 2024"),
    ]
    body = "".join([
        C.hero(
            eyebrow="Sigenergy in Kärnten und der Steiermark · Planung und Montage vom Fachbetrieb",
            h1="Sigenergy Speicher vom Fachbetrieb: SigenStor mit Wallbox und Notstrom",
            lead=("Acht der zehn Referenzprojekte auf unserer Website laufen mit Sigenergy, vom Einfamilienhaus am "
                  "Ossiachersee bis zum Gewerbebetrieb mit 40 kWh Speicher. Wir planen das System passend zu Ihrem "
                  "Verbrauch, melden es beim Netzbetreiber an, kümmern uns um die Förderung und richten die App mit "
                  "Ihnen ein."),
            badges=[("8 von 10", "Referenzen mit Sigenergy"),
                    ("1 bis 6", "Batteriemodule je System"),
                    ("Notstrom", "mit Gateway")],
            img=IMG["speicher"],
            img_alt="Sigenergy SigenStor mit Batteriemodulen im Technikraum eines Wohnhauses, installiert von EBZ Energie",
            float_num=NAP["rating"],
            float_label="auf Google",
            cta_primary=("kontakt", "Kostenlose Sigenergy-Beratung"),
            cta_secondary=("#referenzen", "Unsere Sigenergy-Projekte"),
        ),
        C.kpis([
            ("8 von 10", "unserer Referenzprojekte mit Sigenergy"),
            ("9 bis 40 kWh", "Speichergrößen in diesen Projekten"),
            ("0 ms", "Unterbrechung bei Netzausfall mit Gateway*"),
            ("10 Jahre", "Herstellergarantie, verlängerbar auf 15*"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Was ist Sigenergy und was steckt im SigenStor?",
            paragraphs=[
                ("Sigenergy ist ein Hersteller von Wechselrichtern und Batteriespeichern mit Hauptsitz in Shanghai. "
                 "Die ersten Produkte kamen 2022 auf den Markt, seit April 2026 ist das Unternehmen an der Börse "
                 "Hongkong notiert. Laut eigenen Angaben arbeitet Sigenergy mit über 46.000 registrierten "
                 "Installateuren in mehr als 130 Ländern (Stand November 2026)."),
                ("Das Heimspeichersystem heißt SigenStor. Es vereint laut Hersteller fünf Funktionen in einem Turm: "
                 "PV-Wechselrichter, Batterie-Wechselrichter, Batteriemodule aus Lithium-Eisenphosphat (LFP), "
                 "Energiemanagement und optional ein DC-Ladegerät fürs E-Auto. Für Sie heißt das: ein System, eine App "
                 "und ein Ansprechpartner statt drei Geräten von drei Herstellern."),
                ("Die Batteriemodule werden gestapelt, 1 bis 6 je Energy Controller. Weil jedes Modul einen eigenen "
                 "DC-Wandler hat, laufen neue und ältere Module zusammen. Sie können also mit einem kleineren Speicher "
                 "starten und später aufstocken, wenn E-Auto oder " + a("waermepumpe", "Wärmepumpe") + " dazukommen."),
            ],
        ),
        _table(
            eyebrow="Technische Daten",
            h2="SigenStor im Überblick: Leistung, Speicher, Notstrom, Laden",
            intro=("Die wichtigsten Herstellerangaben auf einen Blick. Welche Kombination zu Ihrem Haus passt, rechnen "
                   "wir nach Verbrauch, Dachfläche und Plänen für E-Auto oder Wärmepumpe."),
            headers=["Baustein", "Herstellerangabe", "Was das für Sie heißt"],
            rows=[
                ("Wechselrichter (Energy Controller)",
                 "einphasig 3 bis 12 kW, dreiphasig 5 bis 30 kW, bis 98,4 % Wirkungsgrad (max.), Schutzart IP66",
                 "passt vom Einfamilienhaus bis zum kleinen Gewerbebetrieb"),
                ("Batteriemodule",
                 "nutzbar 5,2 / 5,84 / 7,8 / 8,76 kWh je Modul (Modelle BAT 5.0, 6.0, 8.0, 10.0), LFP-Zellen",
                 "Achtung: Die Modellnummer ist nicht die kWh-Zahl"),
                ("Speichergröße",
                 "1 bis 6 Module je Energy Controller, bis 54,24 kWh brutto je System",
                 "klein starten, später aufstocken"),
                ("Notstrom",
                 "mit Sigen Energy Gateway 0 ms Unterbrechung auf der Lastseite, Versorgung des ganzen Hauses",
                 "Licht, Kühlschrank und Heizung laufen beim Netzausfall weiter"),
                ("E-Auto laden",
                 "DC-Lademodul 12,5 oder 25 kW im Turm, AC-Wallbox bis 22 kW, jeweils mit PV-Überschussladen",
                 "das Auto tankt bevorzugt Sonnenstrom"),
                ("Energiemanagement",
                 "mySigen App, KI-Modus für dynamische Stromtarife, Verbraucher über Shelly oder SG-Ready-Kontakte",
                 "Wärmepumpe und Warmwasser laufen, wenn Überschuss da ist"),
                ("Garantie",
                 "10 Jahre auf Batteriemodule und Energy Controller, kostenpflichtig verlängerbar auf bis zu 15 Jahre",
                 "Bedingung: Internetverbindung für Updates"),
            ],
            note=(f"Herstellerangaben laut Sigenergy-Datenblättern, {STAND}. Einzelne Leistungsklassen sind laut "
                  "Datenblatt nur in bestimmten Regionen erhältlich. Quellen am Seitenende."),
        ),
        C.reference_cards(
            eyebrow="Erfahrungen aus unseren Projekten",
            h2="Sigenergy in der Praxis: sechs Anlagen von EBZ Energie",
            intro=("Vom Einfamilienhaus mit 9 kWh bis zum Gewerbebetrieb mit 40 kWh: Alle Zahlen stammen aus den "
                   "Projektunterlagen der jeweiligen Anlage. Klicken Sie auf ein Projekt für Bilder und alle Eckdaten."),
            items=REFS,
        ).replace('<section class="section"', '<section id="referenzen" class="section"', 1),
        C.cards_section(
            eyebrow="Was uns in den Projekten auffällt",
            h2="Warum wir Sigenergy so oft einsetzen",
            intro=("Wir planen herstellerunabhängig. Dass Sigenergy in unseren Projekten so oft vorkommt, hat vier "
                   "praktische Gründe."),
            cards=[
                {"ic": "▮", "title": "Speicher wächst mit",
                 "text": "In unseren Projekten reicht die Spanne von 9 kWh am Ossiachersee bis 40 kWh im Gewerbebetrieb. Weitere Module lassen sich später ergänzen, ohne den Wechselrichter zu tauschen."},
                {"ic": "⌂", "title": "Notstrom nach Bedarf",
                 "text": "Im Hotel in Villach und im Betrieb im Burgenland schaltet eine Gatewaybox automatisch um. In anderen Häusern reicht eine manuelle Umschaltung für die wichtigsten Verbraucher. Beides planen wir passend zum Budget."},
                {"ic": "⌖", "title": "Wallbox im selben System",
                 "text": "In vier unserer Sigenergy-Projekte lädt eine 11-kW-Wallbox das E-Auto bevorzugt mit eigenem PV-Strom. Wechselrichter, Speicher und Wallbox sprechen dieselbe Sprache.",
                 "link_key": "/wallbox-foerderung-kosten/", "link_text": "Wallbox: Förderung und Kosten"},
                {"ic": "◎", "title": "Eine App für alles",
                 "text": "Erzeugung, Speicher, Verbrauch und E-Auto sehen Sie in der mySigen App. Bei der Übergabe richten wir die App gemeinsam mit Ihnen ein.",
                 "link_key": "ems", "link_text": "Mehr zum Energiemanagement"},
            ],
        ),
        C.media_text(
            eyebrow="Notstrom mit Sigenergy",
            h2="Wenn das Netz ausfällt: Gateway oder manuelle Umschaltung",
            paragraphs=[
                ("Mit dem Sigen Energy Gateway erkennt das System einen Netzausfall selbst, trennt normgerecht vom Netz "
                 "und versorgt das Haus aus Speicher und Photovoltaik weiter. Der Hersteller gibt dafür 0 ms "
                 "Unterbrechung auf der Lastseite an, wenn die Leistung des Wechselrichters größer ist als die Hauslast. "
                 "Im Inselbetrieb liefert der Backup-Ausgang für 10 Sekunden die doppelte Nennleistung, etwa zum "
                 "Anlaufen einer Pumpe."),
                ("Nicht jedes Haus braucht die Vollversorgung. Bei kleineren Budgets planen wir eine manuelle "
                 "Umschaltung, über die Licht, Kühlschrank und andere wichtige Verbraucher bei Stromausfall aus dem "
                 "Speicher weiterlaufen. Was bei Ihnen sinnvoll ist, klären wir bei der Besichtigung."),
            ],
            img=IMG["netz_gateway"],
            alt="Sigenergy-Wandgerät im Technikraum einer von EBZ Energie installierten Photovoltaikanlage",
            bullets=[
                "Automatisch: Hotel Villach/Warmbad und Landwirtschaft Burgenland mit je 27 kWh",
                "Manuell: Stadthaus Graz, Wohnhaus Wien, Flachdach Graz, Bitumendach Niederösterreich",
                a("batteriespeicher", "Mehr zu Speicher und Notstrom"),
            ],
            reverse=True,
        ),
        C.media_text(
            eyebrow="Sigenergy Wallbox und Energiemanagement",
            h2="E-Auto, Wärmepumpe, dynamischer Tarif: Das System steuert mit",
            paragraphs=[
                ("Sigenergy bietet zwei Wege zum Laden: eine AC-Wallbox mit bis zu 22 kW und ein DC-Lademodul mit 12,5 "
                 "oder 25 kW, das direkt in den Turm kommt. Beide laden auf Wunsch nur mit PV-Überschuss oder nach "
                 "Zeitplan. Das DC-Modul ist laut Hersteller für bidirektionales Laden vorbereitet; ob Ihr E-Auto Strom "
                 "ans Haus zurückgeben kann, hängt vom Fahrzeug ab."),
                ("Das Energiemanagement steckt im Energy Controller. In der mySigen App legen Sie fest, wann Wärmepumpe "
                 "oder Heizstab mit Überschuss laufen, angebunden über Shelly-Schalter oder SG-Ready-Kontakte. Mit einem "
                 + a("/dynamischer-stromtarif/", "dynamischen Stromtarif") + " lädt der KI-Modus den Speicher, wenn "
                 "Strom günstig ist, und nutzt ihn, wenn er teuer ist."),
                ("Zur EMS-Förderung des Klimafonds: Es gibt keine Produktliste. Bei einem im Speicher integrierten "
                 "Energiemanagement sind nur separat ausgewiesene Mehrkosten förderbar, und die Steuerung muss auch ohne "
                 "Internet lokal funktionieren. Ob Ihre Anlage die Kriterien erfüllt, prüfen wir vor dem Angebot. "
                 "Details: " + a("/ems-foerderung/", "EMS-Förderung 2026") + "."),
            ],
            img=IMG["ems"],
            alt="Technikraum mit Energiemanagement-Display, Batteriespeicher und Wechselrichter einer Photovoltaikanlage",
            bullets=[
                "Überschussladen: das E-Auto tankt bevorzugt Sonnenstrom",
                "Wärmepumpe und Warmwasser in die Sonnenstunden gelegt",
                a("ems", "Energiemanagementsystem: Funktion und Nutzen"),
            ],
        ),
        C.price_cards(
            eyebrow="Preis und Förderung",
            h2="Was kostet ein Sigenergy Speicher?",
            intro=("Der Preis hängt an drei Stellschrauben: Zahl der Batteriemodule, Größe des Wechselrichters und "
                   "Zubehör wie Gateway oder Wallbox. Deshalb nennen wir keinen Pauschalpreis, sondern rechnen nach "
                   "Ihrem Verbrauch."),
            items=[
                {"size": "Orientierung", "price": "ab 15.000 €*",
                 "price_sub": "rund 15.000 bis 22.000 € für 10 kWp Photovoltaik mit Speicher, vor Förderung",
                 "features": ["Richtwert für eine typische Komplettanlage",
                              "Speichergröße nach Ihrem Jahresverbrauch",
                              "Projektbericht mit 3D-Belegplan und Statikreport",
                              "Fixangebot nach der Besichtigung"]},
                {"size": "Finanzierung", "price": "ab 147 €*", "price_sub": "im Monat inklusive Speicher",
                 "features": ["Die Anlage gehört Ihnen ab dem ersten Tag",
                              "Volle Förderung bleibt bei Ihnen",
                              "Keine strengen Bonitätsprüfungen",
                              a("finanzierung", "Zur Finanzierung →")]},
                {"size": "Förderung", "price": "Land + Klimafonds", "price_sub": "je nach Bundesland und Komponente",
                 "features": ["Landesförderung für PV und Speicher in Kärnten",
                              "EMS-Förderung bis 600 €, wenn die Kriterien erfüllt sind",
                              "Antrag in der richtigen Reihenfolge",
                              a("foerderungen", "Alle Förderungen 2026 →")]},
            ],
            note=("*Richtwerte und Beispielkonditionen. Der genaue Preis hängt von Speichergröße, Dach und Zubehör ab, "
                  "die Finanzierungsrate von Laufzeit und Anzahlung. Förderfristen ändern sich laufend."),
        ),
        C.reviews_block(reviews),
        C.steps_section(
            eyebrow="So läuft es ab",
            h2="In vier Schritten zu Ihrem Sigenergy-System",
            steps=[
                ("Beratung vor Ort", "Wir sehen uns Dach, Zählerschrank und Technikraum an und klären Verbrauch, E-Auto, Wärmepumpe und Notstromwunsch.", "kostenlos"),
                ("Projektbericht und Fixangebot", "Sie bekommen einen Projektbericht mit 3D-Belegplan und Statikreport, Speichergröße und Wechselrichter passend zu Ihrem Verbrauch.", ""),
                ("Anmeldung und Förderung", "Wir melden die Anlage beim Netzbetreiber an und stellen die Förderanträge in der richtigen Reihenfolge.", ""),
                ("Montage und App", "Zertifizierte Fachkräfte montieren das System, wir nehmen es in Betrieb und richten die mySigen App mit Ihnen ein.", ""),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section("Weiterlesen", [
            ("ems", "Energiemanagementsystem"),
            ("batteriespeicher", "Batteriespeicher"),
            ("/wechselrichter-pv-anlage/", "Wechselrichter für die PV-Anlage"),
            ("/pv-speicher-nachruesten/", "Speicher nachrüsten"),
            ("/wallbox-foerderung-kosten/", "Wallbox: Förderung und Kosten"),
            ("/ems-foerderung/", "EMS-Förderung 2026"),
            ("referenzen", "Alle Referenzen"),
            ("finanzierung", "Finanzierung"),
            ("foerderungen", "Förderungen 2026"),
        ]),
        _quellen(),
        C.contact_section(
            headline="Sigenergy für Ihr Haus: kostenlos beraten lassen",
            sub=("Sie überlegen, ob ein Sigenergy-System zu Ihrem Haus passt, oder wollen einen bestehenden Speicher "
                 "erweitern? Wir kommen zu Ihnen, rechnen ehrlich und sagen Ihnen auch, wenn eine kleinere Lösung "
                 "reicht."),
            page_label="Leistungsseite Sigenergy",
        ),
        C.finalcta(
            "Ein System für Strom, Speicher und E-Auto",
            "Beratung vor Ort in Kärnten und der Steiermark, Projektbericht mit 3D-Belegplan und Statikreport, "
            "Förderung und Netzanmeldung inklusive.",
            cta=("kontakt", "Kostenlose Sigenergy-Beratung"),
            trust=[(f"{NAP['rating']} auf Google", True), ("8 Sigenergy-Referenzen", False),
                   ("Notstrom möglich", False), ("Förderung inklusive", False)],
        ),
        _footnote(),
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ), og_image=IMG["speicher"])
    return write_page("sigenergy/index.html", html)


def _footnote():
    return (f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Projektzahlen (Ersparnis, Jahresertrag, Amortisation) sind Richtwerte aus den
      Projektunterlagen der jeweiligen Anlage und hängen von Verbrauch, Strompreis und Wetter ab. Richtpreis und
      Finanzierungsrate sind Beispielwerte. Technische Daten, Notstrom-Umschaltzeit und Garantie laut Herstellerangaben
      von Sigenergy, {STAND}; die Umschaltzeit von 0 ms gilt laut Datenblatt nur mit Sigen Energy Gateway und wenn die
      Wechselrichterleistung über der Hauslast liegt. Sigenergy und SigenStor sind Marken der Sigenergy Technology
      Co., Ltd. Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import theme
    theme.write_assets()
    build()
