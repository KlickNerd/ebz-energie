"""Referenz-Projektseiten (/referenzen/projekt-<slug>/): zehn Detailseiten zu den Projekten
der Referenzuebersicht (build/pages/referenzen.py).

Quellen: die acht alten WP-Projektseiten (/referenzen-alt/projekt-*) und die Zahlen aus
referenzen.py (dort identisch mit TABLE). Fuer EFH Villach und MFH Krumpendorf gibt es keine
alte Unterseite: nur die freigegebenen Daten aus CLAUDE.md, deshalb kuerzer.

Bereinigt gegenueber den Quelltexten: "ohne Subunternehmer" und "alles aus einer Hand" als
Ausfuehrungs-Claim entfernt, "30 Jahre Produktgarantie" durch die freigegebenen Garantie-Claims
ersetzt (bis zu 30 Jahre Leistungsgarantie, mindestens 10 Jahre Produktgarantie), die
"15 Jahre Garantie auf Wechselrichter und Speicher" nicht uebernommen (nicht freigegeben),
keine Kundennamen (nur Ort und Gebaeudetyp), keine Gedankenstriche. Kundenstimmen gibt es in
den Quellen nicht, daher auf keiner Seite. Amortisation Landwirtschaft Burgenland wie in
referenzen.py "k. A." (die alte Seite nennt ~6 Jahre, Zahlen identisch mit dem Hotel).

Bilder: build/static/img/ref-*.jpg (nur die zum Projekt gehoerenden), Hero-Bilder der
Uebersicht aus common.IMG. Schema: nur FAQPage.
"""

from common import IMG, NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

STAND = "Stand Oktober 2026"
GARANTIE = f"{CLAIMS['garantie_leistung']} auf die Module, {CLAIMS['garantie_produkt']}"
RICHTPREIS = f"Eine 10-kWp-Komplettanlage mit Speicher kostet {CLAIMS['richtpreis_10kwp']}"

R = {
    "gewerbe_ooe_2": "/assets/img/ref-gewerbe-ooe-2.jpg",
    "hotel_1": "/assets/img/ref-hotel-villach-1.jpg",
    "hotel_2": "/assets/img/ref-hotel-villach-2.jpg",
    "bgld_1": "/assets/img/ref-landwirtschaft-bgld-1.jpg",
    "graz_stadthaus_1": "/assets/img/ref-stadthaus-graz-1.jpg",
    "graz_stadthaus_2": "/assets/img/ref-stadthaus-graz-2.jpg",
    "noe_1": "/assets/img/ref-bitumendach-noe-1.jpg",
    "wien_1": "/assets/img/ref-wien-1.jpg",
    "ossiach_1": "/assets/img/ref-ossiachersee-1.jpg",
    "graz_flach_1": "/assets/img/ref-flachdach-graz-1.jpg",
}

# Wiederkehrende Komponenten-Bullets (Quelle: alte Projektseiten, Technikabschnitt)
B_GLASGLAS = "Glas-Glas-Module, bifazial: beidseitig mit Glas laminiert, Mehrertrag durch Rückseitenlicht"
B_SIGENERGY = "Sigenergy All-in-One-System: Wechselrichter und Speichermanagement aus einem System, Monitoring per App, modular erweiterbar"
B_WALLBOX = "Wallbox 11 kW, dreiphasig: lädt das E-Auto bevorzugt mit eigenem PV-Strom, über Nacht voll"
B_NOTSTROM_MAN = "Manuelle Notstromumschaltung: Licht, Kühlschrank und andere wichtige Verbraucher laufen bei Netzausfall aus dem Speicher weiter"
B_NOTSTROM_AUTO = "Gatewaybox: erkennt den Netzausfall in Sekunden, trennt normgerecht vom Netz und schaltet vollautomatisch auf den Speicher um"


def _ratgeber_links(*items):
    return list(items)


PROJEKTE = [
    # ------------------------------------------------------------------ 1
    {
        "slug": "projekt-gewerbe-oberoesterreich",
        "anchor": "gewerbe-oberoesterreich",
        "titel": "Gewerbebetrieb in Oberösterreich: 40 kWp Ost-West auf Trapezblech mit 40-kWh-Speicher",
        "kurz": "Gewerbe Oberösterreich, 40 kWp",
        "ort": "Oberösterreich",
        "typ": "Gewerbebetrieb",
        "eyebrow": "Referenzprojekt · Gewerbe · Oberösterreich",
        "title": "Referenz: 40 kWp Gewerbe-PV in Oberösterreich | EBZ",
        "desc": ("Referenzprojekt Gewerbe Oberösterreich: 40 kWp Glas-Glas-Module in Ost-West auf Trapezblech, "
                 "40-kWh-Speicher, rund 40.000 kWh und 13.500 € Ersparnis pro Jahr*."),
        "lead": ("Die größte Anlage unserer Referenzauswahl: 40 kWp bifaziale Glas-Glas-Module in Ost-West-Ausrichtung, "
                 "auf die Sicken des Trapezblechdachs geklemmt, dazu ein 40-kWh-Speicher. Rund 40.000 kWh Eigenstrom pro "
                 "Jahr und etwa 13.500 € weniger Stromkosten*, jedes Jahr."),
        "badges": [("40 kWp", "Glas-Glas bifazial"), ("40 kWh", "Sigenergy-Speicher"), ("13.500 €", "Ersparnis pro Jahr*")],
        "hero_img": IMG["gewerbe_dach"],
        "hero_alt": "Drohnenaufnahme der 40-kWp-Photovoltaikanlage in Ost-West-Ausrichtung auf dem roten Trapezblechdach eines Gewerbebetriebs in Oberösterreich",
        "kpis": [("40 kWp", "Leistung, Ost-West"), ("40 kWh", "Batteriespeicher"), ("~40.000 kWh", "Jahresertrag"), ("~13.500 €", "Ersparnis pro Jahr*")],
        "eckdaten": [
            ("Standort", "Oberösterreich"), ("Gebäudetyp", "Gewerbebetrieb"),
            ("Leistung", "40 kWp"), ("Module", "Glas-Glas, bifazial"),
            ("Speicher", "40 kWh"), ("System", "Sigenergy All-in-One"),
            ("Ausrichtung", "Ost und West, zwei Modulfelder"), ("Dach und Montage", "Trapezblechdach, Klemmbefestigung auf den Sicken"),
            ("Jahresertrag", "rund 40.000 kWh"), ("Ersparnis", "rund 13.500 € pro Jahr*"),
            ("Amortisation", "ca. 5 Jahre (geschätzt)*"), ("Garantie", GARANTIE),
        ],
        "ausgangslage": [
            ("Ein Gewerbebetrieb verbraucht Strom genau dann, wenn die Sonne scheint: Maschinen, Beleuchtung, Kühlung "
             "und Technik laufen über den Arbeitstag. Diese Deckung von Erzeugung und Verbrauch ist der entscheidende "
             "Hebel, denn selbst genutzter Strom spart am meisten. Ziel war deshalb eine Anlage, die nicht eine "
             "Mittagsspitze liefert, sondern von Betriebsbeginn bis Betriebsschluss produziert."),
            ("Das Trapezblechdach bot eine große, zusammenhängende Fläche. Es sollte ohne Bohrungen in die Dachhaut "
             "belegt werden, mit einer Befestigung, die schnell montiert ist und Wind- und Schneelasten sicher aufnimmt. "
             "Zusätzlich sollte ein Speicher Lastspitzen glätten und den Bedarf nach Betriebsschluss abdecken."),
            ("Ein Betrieb braucht außerdem planbare Energiekosten. Je mehr Strom vom eigenen Dach direkt in Maschinen und Kühlung "
             "fließt, desto unabhängiger wird die Kalkulation von Strompreisschwankungen."),
        ],
        "loesung_h2": "Die Lösung: Ost-West-Belegung, Klemmen statt Bohren, 40 kWh Puffer",
        "loesung": [
            ("Die 40 kWp verteilen sich auf zwei Modulfelder: Die Ostfläche liefert am Morgen, die Westfläche am Nachmittag "
             "und Abend. Statt einer Spitze um die Mittagszeit entsteht ein breiter Ertragsverlauf über die gesamten "
             "Betriebszeiten, und der Eigenverbrauch steigt."),
            ("Auf dem Trapezblech sitzen die Module mit speziellen Klemmen direkt auf den erhöhten Blechsicken. Das geht "
             "schnell, hält sicher und schont das Dach. Das Sigenergy-System bündelt Wechselrichter und 40-kWh-Speicher: "
             "Überschüsse aus dem Tag stehen am Abend, in Pausen und bei Lastspitzen zur Verfügung."),
        ],
        "loesung_img": R["gewerbe_ooe_2"],
        "loesung_alt": "Drohnen-Draufsicht auf die zwei Modulfelder in Ost-West-Ausrichtung auf dem Trapezblechdach des Gewerbebetriebs in Oberösterreich",
        "komponenten": [
            "40 kWp Glas-Glas-Module, bifazial, Ost-West auf zwei Modulfeldern",
            B_SIGENERGY,
            "40 kWh Batteriespeicher: puffert Überschüsse, Lastspitzen und den Bedarf nach Betriebsschluss",
            "Klemmbefestigung auf Trapezblech: keine Bohrung, schnelle und dachschonende Montage",
            "Überschuss-Einspeisung ins Netz, wenn Betrieb und Speicher versorgt sind",
        ],
        "ergebnis": [
            ("Die 40-kWp-Photovoltaikanlage auf dem Trapezblechdach eines Gewerbebetriebs in Oberösterreich liefert rund "
             "40.000 kWh Strom pro Jahr. Zusammen mit dem 40-kWh-Speicher spart der Betrieb rund 13.500 € Stromkosten "
             f"jährlich*, die Amortisation liegt bei etwa 5 Jahren. Geplant und montiert von EBZ Energie aus Villach ({STAND})."),
            ("Über zehn Jahre summiert sich die Ersparnis auf rund 135.000 €*. Weil die Module bis zu 30 Jahre "
             "Leistungsgarantie haben, folgen danach viele weitere Jahre günstiger Eigenstrom. Für den Betrieb heißt das: "
             "planbare Energiekosten, weniger Netzbezug und ein sichtbares Zeichen für Nachhaltigkeit."),
        ],
        "faq": [
            ("Was bringt die Ost-West-Ausrichtung für einen Gewerbebetrieb?",
             "Eine Ost-West-Belegung verteilt die Produktion über den ganzen Tag statt auf eine Mittagsspitze. Die Ostfläche "
             "liefert am Morgen, die Westfläche am Nachmittag und Abend, also über die typischen Betriebszeiten. Genau dann "
             "verbraucht der Betrieb Strom, was den Eigenverbrauch und damit die Wirtschaftlichkeit erhöht."),
            ("Warum lohnt sich ein 40-kWh-Speicher im Gewerbe?",
             "Der Speicher legt Überschüsse aus dem Tag zurück und stellt sie am Abend, in Pausen oder bei Lastspitzen wieder "
             "bereit. Dadurch bleibt mehr selbst erzeugter Strom im Betrieb, der teure Netzbezug sinkt und die Energiekosten "
             "werden planbarer. Bei dieser Anlage trägt er zu rund 13.500 € Ersparnis pro Jahr* bei."),
            ("Wie werden Module auf einem Trapezblechdach montiert?",
             "Auf Trapezblech werden die Module mit speziellen Klemmen direkt auf den erhöhten Blechsicken befestigt. Diese "
             "Montage ist schnell, sehr belastbar und kommt ohne Bohrung in die Dachhaut aus, ideal für große, "
             "zusammenhängende Gewerbedächer."),
            ("Wie schnell rechnet sich eine 40-kWp-Gewerbeanlage?",
             "Das hängt vor allem vom Eigenverbrauch ab. Bei rund 40.000 kWh Jahresertrag und rund 13.500 € Ersparnis pro "
             "Jahr* liegt dieses Projekt bei etwa 5 Jahren (geschätzt). Typisch sind bei EBZ-Anlagen 4 bis 6 Jahre. Die "
             "genaue Rechnung für Ihren Betrieb liefert der Projektbericht mit 3D-Belegplan und Statikreport."),
        ],
        "related": [
            ("pv_gewerbe", "Photovoltaik für Gewerbe und Landwirtschaft"),
            ("/photovoltaik-foerderung-oberoesterreich/", "PV-Förderung Oberösterreich 2026"),
            ("/ab-wann-lohnt-sich-photovoltaik-mit-speicher/", "Ab wann lohnt sich Photovoltaik mit Speicher?"),
            ("batteriespeicher", "Batteriespeicher für Betriebe"),
        ],
        "contact_h": "Ihr Betrieb hat ein ähnliches Dach?",
        "contact_sub": ("Schicken Sie uns Dachfläche, Jahresverbrauch und Betriebszeiten. Wir sagen Ihnen, welche Anlage "
                        "passt, was sie kostet und wie schnell sie sich rechnet. Kostenlos und unverbindlich."),
        "final_h": "Planbare Energiekosten für Ihren Betrieb",
        "final_t": "Von der Machbarkeitsprüfung bis zur Förderabwicklung: Wir begleiten Gewerbeprojekte in Kärnten, der Steiermark und darüber hinaus.",
    },
    # ------------------------------------------------------------------ 2
    {
        "slug": "projekt-pv-anlage-hotel-villach",
        "anchor": "hotel-villach-warmbad",
        "titel": "Hotel in Villach/Warmbad: 13 kWp auf dem Flachdach, 27-kWh-Speicher und automatischer Notstrom",
        "kurz": "Hotel Villach/Warmbad, 13 kWp",
        "ort": "Villach/Warmbad, Kärnten",
        "typ": "Hotelbetrieb",
        "eyebrow": "Referenzprojekt · Hotel · Villach/Warmbad",
        "title": "Referenz: Hotel Villach/Warmbad, 13 kWp + 27 kWh | EBZ",
        "desc": ("Referenzprojekt Hotel Villach/Warmbad: 13 kWp auf dem Bitumen-Flachdach, 27-kWh-Speicher, "
                 "automatischer Notstrom, rund 4.200 € Ersparnis pro Jahr*."),
        "lead": ("Ein Hotel läuft rund um die Uhr. Deshalb kombiniert diese Anlage 13 kWp bifaziale Glas-Glas-Module in "
                 "Südausrichtung mit einem besonders großen 27-kWh-Speicher und einer Gatewaybox, die bei Netzausfall "
                 "vollautomatisch auf Notstrom umschaltet. Rund 15.000 kWh im Jahr, Amortisation in etwa 6 Jahren*."),
        "badges": [("13 kWp", "Glas-Glas bifazial, Süd"), ("27 kWh", "Speicher mit Notstrom"), ("4.200 €", "Ersparnis pro Jahr*")],
        "hero_img": R["hotel_1"],
        "hero_alt": "Drohnenaufnahme des Hotels in Villach/Warmbad mit aufgeständerten Glas-Glas-Modulen in Südausrichtung auf dem Bitumen-Flachdach",
        "kpis": [("13 kWp", "Leistung, Süd"), ("27 kWh", "Speicher, Notstrom automatisch"), ("~15.000 kWh", "Jahresertrag"), ("~6 Jahre", "Amortisation*")],
        "eckdaten": [
            ("Standort", "Villach/Warmbad, Kärnten"), ("Gebäudetyp", "Hotel"),
            ("Leistung", "13 kWp"), ("Module", "Glas-Glas, bifazial"),
            ("Speicher", "27 kWh"), ("System", "Sigenergy All-in-One mit Gatewaybox"),
            ("Notstrom", "automatische Umschaltung in Sekunden"), ("Ausrichtung", "Süd, zwei Neigungswinkel"),
            ("Dach und Montage", "Bitumen-Flachdach, K2-Unterkonstruktion aufgeständert"),
            ("Jahresertrag", "rund 15.000 kWh"), ("Ersparnis", "rund 4.200 € pro Jahr*"),
            ("Amortisation", "ca. 6 Jahre*"), ("Garantie", GARANTIE),
        ],
        "ausgangslage": [
            ("Rezeption, Zimmerkarten, Aufzug, Kühlung, Beleuchtung und WLAN: In einem Beherbergungsbetrieb darf nichts "
             "davon ausfallen, auch nicht nachts. Ein Stromausfall ist hier kein Komfortproblem, sondern ein Sicherheits- "
             "und Imagerisiko. Die Anlage musste deshalb zwei Aufgaben lösen: Stromkosten senken und den Betrieb bei "
             "Netzausfall weiterlaufen lassen, ohne dass jemand im Technikraum eingreifen muss."),
            ("Das Bitumen-Flachdach des Hotels bot viel Fläche, aber keine Neigung. Die Module mussten aufgeständert "
             "werden, dachschonend und windlastsicher, und die vorhandene Fläche sollte möglichst vollständig genutzt werden."),
            ("Dazu kam die Wirtschaftlichkeit: Ein Hotel hat hohe Grundlasten am Tag und in der Nacht. Ein großer Speicher "
             "sollte den Sonnenstrom vom Nachmittag in die Nachtstunden verschieben, damit möglichst wenig Netzstrom zugekauft wird."),
        ],
        "loesung_h2": "Die Lösung: Südaufständerung mit zwei Winkeln, 27 kWh Reserve, Gatewaybox",
        "loesung": [
            ("Auf dem Flachdach steht eine K2-Unterkonstruktion, die die 13 kWp Glas-Glas-Module in reiner Südausrichtung "
             "aufnimmt, über zwei unterschiedliche Neigungswinkel. So wird die Dachfläche optimal belegt und der Ertragsverlauf "
             "über den Tag geglättet. Die Dachhaut bleibt fachgerecht dicht."),
            ("Das Herz der Anlage ist der 27-kWh-Speicher im Sigenergy-System. Er versorgt Abend, Nacht und Netzausfall. Eine "
             "Gatewaybox überwacht das Netz permanent: Fällt es aus, trennt sie die Anlage sauber vom Netz und schaltet in "
             "Sekunden auf den Speicher um. Licht, Aufzug, Kühlung und WLAN laufen weiter, die Gäste merken im Idealfall nichts."),
        ],
        "loesung_img": R["hotel_2"],
        "loesung_alt": "Drohnen-Draufsicht auf die Modulreihen in Südausrichtung auf dem Flachdach des Hotels in Villach/Warmbad",
        "komponenten": [
            "13 kWp Glas-Glas-Module, bifazial, Süd mit zwei Neigungswinkeln",
            B_SIGENERGY,
            "27 kWh Batteriespeicher: große Reserve für Nachtbetrieb und Notstrom",
            B_NOTSTROM_AUTO,
            "K2-Unterkonstruktion auf Bitumen-Flachdach: aufgeständert, dachschonend, windlastsicher",
        ],
        "ergebnis": [
            ("Das Hotel in Villach/Warmbad erzeugt mit 13 kWp bifazialen Glas-Glas-Modulen rund 15.000 kWh Strom pro Jahr "
             "und spart damit rund 4.200 € Stromkosten jährlich*. Der 27-kWh-Speicher mit Gatewaybox sichert den Betrieb "
             f"bei Netzausfall automatisch ab, die Amortisation liegt bei etwa 6 Jahren* ({STAND})."),
            ("Nach der Amortisation produziert die Anlage weiter, bei bis zu 30 Jahren Leistungsgarantie auf die Module über "
             "Jahrzehnte. Dazu kommt ein Wert, der sich nicht in Euro ausdrücken lässt: Versorgungssicherheit für Gäste und "
             "Personal, ohne Handgriff."),
        ],
        "faq": [
            ("Wie funktioniert die automatische Notstromumschaltung mit Gatewaybox?",
             "Die Gatewaybox überwacht permanent das Stromnetz. Fällt das Netz aus, trennt sie die Anlage sicher und "
             "normgerecht vom Netz und schaltet vollautomatisch auf den Speicher um, ohne dass jemand eingreifen muss. "
             "Wichtige Verbraucher des Hotels laufen praktisch unterbrechungsfrei aus dem 27-kWh-Speicher weiter."),
            ("Warum ist Notstrom für ein Hotel so wichtig?",
             "In einem Beherbergungsbetrieb läuft Technik rund um die Uhr: Rezeption, Zimmerkarten, Aufzug, Kühlung, "
             "Beleuchtung und WLAN. Ein Stromausfall wäre ein spürbarer Komfort- und Sicherheitsverlust für die Gäste. Die "
             "automatische Notstromversorgung überbrückt solche Ausfälle aus dem Speicher."),
            ("Was bringt die Südausrichtung mit zwei Neigungswinkeln?",
             "Eine reine Südausrichtung liefert die höchste Tagesleistung. Durch zwei unterschiedliche Neigungswinkel wird "
             "die vorhandene Dachfläche optimal belegt und der Ertragsverlauf über den Tag geglättet. Das erhöht den Anteil "
             "des selbst genutzten Stroms."),
            ("Lohnt sich Photovoltaik für ein Hotel in Villach?",
             "Ja. Diese Anlage spart rund 4.200 € Stromkosten pro Jahr* und hat sich nach etwa 6 Jahren amortisiert. Danach "
             "folgen viele Jahre günstiger Eigenstrom, dazu die Versorgungssicherheit durch den automatischen Notstrom und "
             "die Unabhängigkeit von steigenden Strompreisen."),
        ],
        "related": [
            ("pv_gewerbe", "Photovoltaik für Gewerbe und Hotellerie"),
            ("/notstrom/", "Notstrom mit Photovoltaik: Ersatzstrom erklärt"),
            ("/photovoltaik-foerderung-kaernten/", "PV-Förderung Kärnten 2026"),
            ("pv_villach", "Photovoltaik in Villach"),
        ],
        "contact_h": "Ihr Betrieb darf nicht stillstehen?",
        "contact_sub": ("Hotel, Gastronomie, Praxis oder Produktion: Wir planen Photovoltaik mit Speicher und automatischem "
                        "Notstrom passend zu Ihrem Lastprofil. Kostenlos und unverbindlich."),
        "final_h": "Sonnenstrom und Versorgungssicherheit aus einer Anlage",
        "final_t": "Erzählen Sie uns von Ihrem Dach und Ihrem Verbrauch. Wir melden uns innerhalb eines Werktags.",
    },
    # ------------------------------------------------------------------ 3
    {
        "slug": "projekt-landwirtschaft-im-burgenland",
        "anchor": "landwirtschaft-burgenland",
        "titel": "Landwirtschaftlicher Betrieb im Burgenland: 13 kWp mit 27-kWh-Speicher und automatischem Notstrom",
        "kurz": "Landwirtschaft Burgenland, 13 kWp",
        "ort": "Burgenland",
        "typ": "Landwirtschaftlicher Betrieb",
        "eyebrow": "Referenzprojekt · Landwirtschaft · Burgenland",
        "title": "Referenz: Landwirtschaft Burgenland, 13 kWp + Notstrom | EBZ",
        "desc": ("Referenzprojekt Landwirtschaft Burgenland: 13 kWp in Süd auf Bitumendach, 27-kWh-Speicher, "
                 "automatischer Notstrom per Gatewaybox, rund 15.000 kWh pro Jahr."),
        "lead": ("Kühlung, Lüftung, Pumpen und Steuerungen dürfen in der Landwirtschaft nicht ausfallen. Diese Anlage "
                 "kombiniert 13 kWp bifaziale Glas-Glas-Module in Südausrichtung mit einem 27-kWh-Speicher und einer "
                 "Gatewaybox, die bei Netzausfall vollautomatisch auf Notstrom umschaltet. Rund 15.000 kWh Eigenstrom pro Jahr."),
        "badges": [("13 kWp", "Glas-Glas bifazial, Süd"), ("27 kWh", "Speicher mit Notstrom"), ("4.200 €", "Ersparnis pro Jahr*")],
        "hero_img": R["bgld_1"],
        "hero_alt": "Photovoltaikanlage in zwei Modulreihen auf dem Bitumenschindel-Dach eines landwirtschaftlichen Betriebs im Burgenland",
        "kpis": [("13 kWp", "Leistung, Süd"), ("27 kWh", "Speicher, Notstrom automatisch"), ("~15.000 kWh", "Jahresertrag"), ("~4.200 €", "Ersparnis pro Jahr*")],
        "eckdaten": [
            ("Standort", "Burgenland"), ("Gebäudetyp", "Landwirtschaftlicher Betrieb mit Wohnhaus"),
            ("Leistung", "13 kWp"), ("Module", "Glas-Glas, bifazial"),
            ("Speicher", "27 kWh"), ("System", "Sigenergy All-in-One mit Gatewaybox"),
            ("Notstrom", "automatische Umschaltung in Sekunden"), ("Ausrichtung", "Süd, zwei Modulreihen, zwei Neigungswinkel"),
            ("Dach und Montage", "Bitumendach, K2-Unterkonstruktion"),
            ("Jahresertrag", "rund 15.000 kWh"), ("Ersparnis", "rund 4.200 € pro Jahr*"),
            ("Amortisation", "in den Projektdaten nicht erfasst"), ("Garantie", GARANTIE),
        ],
        "ausgangslage": [
            ("In einem landwirtschaftlichen Betrieb kann ein Stromausfall teuer werden: Kühlketten reißen, Lüftung und "
             "Pumpen stehen, Steuerungen fallen aus. Gleichzeitig läuft ein großer Teil des Verbrauchs tagsüber, wenn die "
             "Sonne scheint. Die Anlage sollte deshalb den Eigenverbrauch hoch halten und den Betrieb bei Netzausfall "
             "automatisch weiterversorgen, ohne dass jemand vor Ort einen Schalter umlegen muss."),
            ("Das Bitumendach des Betriebsgebäudes sollte in zwei Modulreihen belegt werden, fachgerecht abgedichtet und "
             "so ausgerichtet, dass die Südsonne den höchsten Tagesertrag liefert."),
            ("Weil Betrieb und Wohnhaus am selben Anschluss hängen, sollte eine Anlage beides versorgen: tagsüber die Technik "
             "des Betriebs, abends den Haushalt. Der Speicher musste entsprechend groß ausfallen."),
        ],
        "loesung_h2": "Die Lösung: Südanlage in zwei Reihen, 27 kWh Reserve, Gatewaybox",
        "loesung": [
            ("Die 13 kWp Glas-Glas-Module sitzen in zwei Reihen auf einer K2-Unterkonstruktion, in reiner Südausrichtung und "
             "über zwei Neigungswinkel, damit die Dachfläche vollständig genutzt wird. Die Dachhaut bleibt fachgerecht dicht, "
             "die Konstruktion hält der Windlast stand."),
            ("Der 27-kWh-Speicher im Sigenergy-System legt den Sonnenstrom für Abend und Nacht zurück und dient als Reserve für "
             "den Notstrombetrieb. Die Gatewaybox überwacht das Netz, erkennt einen Ausfall in Sekunden und schaltet "
             "vollautomatisch auf den Speicher um. Kühlung, Tierhaltung und Technik bleiben versorgt, auch bei längeren Ausfällen."),
        ],
        "loesung_img": R["bgld_1"],
        "loesung_alt": "Glas-Glas-Module in zwei Reihen auf dem Bitumendach des Betriebs im Burgenland, montiert mit K2-Unterkonstruktion",
        "komponenten": [
            "13 kWp Glas-Glas-Module, bifazial, Süd mit zwei Neigungswinkeln",
            B_SIGENERGY,
            "27 kWh Batteriespeicher: Sonnenstrom rund um die Uhr, Reserve für Notstrom",
            B_NOTSTROM_AUTO,
            "K2-Unterkonstruktion auf Bitumendach: fachgerecht dicht, windlastsicher",
        ],
        "ergebnis": [
            ("Der landwirtschaftliche Betrieb im Burgenland erzeugt mit 13 kWp bifazialen Glas-Glas-Modulen in Südausrichtung "
             "rund 15.000 kWh Strom pro Jahr und spart rund 4.200 € Stromkosten jährlich*. Der 27-kWh-Speicher mit Gatewaybox "
             f"übernimmt bei Netzausfall automatisch die Versorgung von Kühlung, Pumpen und Technik ({STAND})."),
            ("Der Betrieb ist damit weitgehend unabhängig vom Netz: tagsüber direkt von den Modulen, abends und nachts aus dem "
             "Speicher, bei Ausfall ebenfalls aus dem Speicher. Die Module haben bis zu 30 Jahre Leistungsgarantie."),
        ],
        "faq": [
            ("Wozu ein so großer 27-kWh-Speicher in der Landwirtschaft?",
             "Der große Speicher erhöht den Eigenverbrauch deutlich und macht den Betrieb weitgehend unabhängig vom Netz. "
             "Zusätzlich dient er als Reserve für den automatischen Notstrombetrieb. Gerade in der Landwirtschaft, wo Kühlung "
             "und Technik nicht ausfallen dürfen, hält er wichtige Verbraucher auch bei längeren Ausfällen am Laufen."),
            ("Wie funktioniert die automatische Notstromumschaltung mit Gatewaybox?",
             "Die Gatewaybox überwacht permanent das Stromnetz. Fällt das Netz aus, trennt sie die Anlage sicher vom Netz und "
             "schaltet vollautomatisch auf den Speicher um, ohne dass jemand eingreifen muss. Wichtige Verbraucher laufen so "
             "praktisch unterbrechungsfrei aus dem 27-kWh-Speicher weiter."),
            ("Wie werden die Module auf dem Bitumendach befestigt?",
             "Auf dem Bitumendach kommt eine K2-Unterkonstruktion zum Einsatz, ein bewährtes, dachschonendes Montagesystem. "
             "Es nimmt die Module sicher auf, hält der Windlast stand und lässt die Dachabdichtung fachgerecht dicht."),
            ("Lohnt sich Photovoltaik für einen landwirtschaftlichen Betrieb?",
             "Ja, vor allem wegen des hohen Tagesverbrauchs. Diese Anlage spart rund 4.200 € Stromkosten pro Jahr*. Dazu kommen "
             "Versorgungssicherheit durch den automatischen Notstrom und Unabhängigkeit von steigenden Strompreisen. Für "
             "Betriebe gelten eigene Förderkategorien, die wir im Angebot prüfen."),
        ],
        "related": [
            ("pv_gewerbe", "Photovoltaik für Gewerbe und Landwirtschaft"),
            ("/notstrom/", "Notstrom mit Photovoltaik: Ersatzstrom erklärt"),
            ("/photovoltaik-foerderung-burgenland/", "PV-Förderung Burgenland 2026"),
            ("batteriespeicher", "Batteriespeicher und Notstrom"),
        ],
        "contact_h": "Ihr Betrieb braucht Strom, der nicht ausfällt?",
        "contact_sub": ("Landwirtschaft, Kühlung, Tierhaltung: Wir planen Photovoltaik mit Speicher und automatischem Notstrom "
                        "nach Ihrem Lastprofil. Kostenlos und unverbindlich."),
        "final_h": "Versorgungssicherheit vom eigenen Dach",
        "final_t": "Erzählen Sie uns von Ihrem Betrieb. Wir melden uns innerhalb eines Werktags mit einer ehrlichen Einschätzung.",
    },
    # ------------------------------------------------------------------ 4
    {
        "slug": "projekt-stadthaus-in-graz",
        "anchor": "stadthaus-graz",
        "titel": "Stadthaus in Graz: 18 kWp auf drei Flachdächern, ballastiert ohne Bohrung, amortisiert in rund 4 Jahren",
        "kurz": "Stadthaus Graz, 18 kWp",
        "ort": "Graz, Steiermark",
        "typ": "Stadthaus",
        "eyebrow": "Referenzprojekt · Stadthaus · Graz",
        "title": "Referenz: Stadthaus Graz, 18 kWp auf 3 Flachdächern | EBZ",
        "desc": ("Referenzprojekt Stadthaus Graz: 18 kWp auf drei Flachdächern, ballastiert ohne Bohrung, "
                 "18-kWh-Speicher, Wallbox 11 kW, rund 5.000 € Ersparnis pro Jahr*."),
        "lead": ("Drei getrennte Flachdächer, ein System: 18 kWp bifaziale Glas-Glas-Module in Süd- und Ostausrichtung, "
                 "aufgeständert und mit Betongewichten ballastiert, ganz ohne Dachdurchdringung. Dazu 18 kWh Speicher, eine "
                 "11-kW-Wallbox und Notstrom. Rund 20.000 kWh im Jahr, Amortisation in etwa 4 Jahren*."),
        "badges": [("18 kWp", "auf 3 Flachdächern"), ("18 kWh", "Speicher + Wallbox 11 kW"), ("5.000 €", "Ersparnis pro Jahr*")],
        "hero_img": R["graz_stadthaus_1"],
        "hero_alt": "Aufgeständerte Glas-Glas-Module auf den begrünten Flachdächern eines Stadthauses in Graz, mit Betongewichten ballastiert",
        "kpis": [("18 kWp", "Leistung, Süd und Ost"), ("18 kWh", "Speicher, Notstrom manuell"), ("~20.000 kWh", "Jahresertrag"), ("~4 Jahre", "Amortisation*")],
        "eckdaten": [
            ("Standort", "Graz, Steiermark"), ("Gebäudetyp", "Stadthaus mit drei Flachdächern"),
            ("Leistung", "18 kWp"), ("Module", "Glas-Glas, bifazial"),
            ("Speicher", "18 kWh"), ("System", "Sigenergy All-in-One"),
            ("Wallbox", "11 kW, dreiphasig"), ("Notstrom", "manuelle Umschaltung"),
            ("Ausrichtung", "Süd und Ost"), ("Dach und Montage", "3 Flachdächer, aufgeständert und mit Betongewichten ballastiert, keine Dachdurchdringung"),
            ("Jahresertrag", "rund 20.000 kWh"), ("Ersparnis", "rund 5.000 € pro Jahr*"),
            ("Amortisation", "ca. 4 Jahre*"), ("Garantie", GARANTIE),
        ],
        "ausgangslage": [
            ("Das Stadthaus hat keine zusammenhängende Dachfläche, sondern drei getrennte Flachdächer, teils begrünt, teils "
             "mit Kies. Die Dachabdichtung sollte unversehrt bleiben: keine Bohrung, keine Durchdringung. Gleichzeitig wollte "
             "die Familie möglichst viel Strom selbst nutzen, ein E-Auto laden und bei Netzausfall nicht im Dunkeln sitzen."),
            ("Eine reine Südanlage hätte eine Mittagsspitze geliefert, die zu einem Haushalt nur bedingt passt. Gesucht war ein "
             "Konzept, das die drei Flächen jeweils optimal ausrichtet und als eine Einheit betreibt."),
        ],
        "loesung_h2": "Die Lösung: drei Dächer, Süd und Ost, Betongewichte statt Bohrung",
        "loesung": [
            ("Auf allen drei Flachdächern stehen die 18 kWp Glas-Glas-Module auf einer aufgeständerten Unterkonstruktion, "
             "gehalten von Betongewichten. Es wurde nicht ins Dach gebohrt, die Abdichtung ist vollständig unversehrt. Die leichte "
             "Neigung sorgt für guten Lichteinfall und dafür, dass Regen die Module selbst reinigt."),
            ("Die Flächen sind in Süd- und Ostausrichtung belegt, so läuft die Produktion vom Vormittag bis in den Nachmittag "
             "gleichmäßig. Das Sigenergy-System bündelt Wechselrichter, 18-kWh-Speicher und die 11-kW-Wallbox: Das E-Auto lädt "
             "bevorzugt mit eigenem Sonnenstrom, bei Netzausfall lässt sich die Anlage manuell in den Notstrombetrieb schalten."),
        ],
        "loesung_img": R["graz_stadthaus_2"],
        "loesung_alt": "Aufgeständerte Module auf dem begrünten Flachdach des Stadthauses in Graz, ohne Dachdurchdringung montiert",
        "komponenten": [
            "18 kWp Glas-Glas-Module, bifazial, Süd und Ost auf drei Flachdächern",
            B_SIGENERGY,
            "18 kWh Batteriespeicher: Sonnenstrom für Abend und Nacht, Reserve für Notstrom",
            B_WALLBOX,
            B_NOTSTROM_MAN,
            "Aufständerung mit Betongewichten ballastiert: keine Dachdurchdringung, Abdichtung bleibt unversehrt",
        ],
        "ergebnis": [
            ("Das Stadthaus in Graz erzeugt mit 18 kWp bifazialen Glas-Glas-Modulen auf drei ballastierten Flachdächern rund "
             "20.000 kWh Strom pro Jahr. Mit 18-kWh-Speicher und 11-kW-Wallbox spart die Familie rund 5.000 € Stromkosten "
             f"jährlich*, die Amortisation liegt bei etwa 4 Jahren*, der schnellste Wert unserer Referenzauswahl ({STAND})."),
            ("Dazu kommen ein E-Auto, das mit eigenem Strom fährt, und Sicherheit bei Netzausfall. Nach der Amortisation "
             "produziert die Anlage weiter, bei bis zu 30 Jahren Leistungsgarantie auf die Module über Jahrzehnte."),
        ],
        "faq": [
            ("Wie werden die Module auf dem Flachdach befestigt, ohne zu bohren?",
             "Auf den drei Flachdächern werden die Module auf einer Unterkonstruktion aufgeständert und mit Betongewichten "
             "ballastiert. Es wird nicht ins Dach gebohrt, die Abdichtung bleibt vollständig unversehrt. Die leichte Aufständerung "
             "sorgt zugleich für guten Lichteinfall und dafür, dass Regen die Module selbst reinigt."),
            ("Was bringt die kombinierte Süd-Ost-Ausrichtung auf drei Flachdächern?",
             "Die Süd-Ost-Belegung erntet vom Vormittag bis in den Nachmittag Sonne und verteilt den Ertrag gleichmäßiger über "
             "den Tag als eine reine Südanlage. Weil sich die Anlage über drei Flachdächer verteilt, lässt sich jede Fläche "
             "optimal ausrichten. Das passt zum typischen Tagesverbrauch und erhöht den Eigenverbrauch."),
            ("Kann ich das E-Auto mit Sonnenstrom laden?",
             "Ja. Die 11-kW-Wallbox lädt dreiphasig und damit rund fünfmal schneller als eine Haushaltssteckdose. Weil Wallbox, "
             "Speicher und Wechselrichter aus dem Sigenergy-System stammen, lädt das Auto bevorzugt mit selbst erzeugtem PV-Strom."),
            ("Warum amortisiert sich diese Anlage schon in rund 4 Jahren?",
             "Weil viel Strom direkt im Haus bleibt: 20.000 kWh Jahresertrag, ein 18-kWh-Speicher für den Abend und ein E-Auto, "
             "das statt teurem Netz- oder Ladesäulenstrom Sonnenstrom tankt. Rund 5.000 € Ersparnis pro Jahr* bringen die Anlage "
             "in etwa 4 Jahren ins Plus. Typisch sind bei EBZ-Anlagen 4 bis 6 Jahre."),
        ],
        "related": [
            ("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
            ("/foerderung-photovoltaik-steiermark/", "PV-Förderung Steiermark 2026"),
            ("/notstrom/", "Notstrom mit Photovoltaik: Ersatzstrom erklärt"),
            ("batteriespeicher", "Batteriespeicher mit Wallbox"),
        ],
        "contact_h": "Flachdach, Gründach oder mehrere Dachflächen?",
        "contact_sub": ("Wir planen Anlagen auch für Dächer, die nicht nach Lehrbuch aussehen. Schicken Sie uns ein Foto oder "
                        "die Adresse, wir prüfen die Machbarkeit. Kostenlos und unverbindlich."),
        "final_h": "Ihr Dach kann das auch",
        "final_t": "Steiermark und Kärnten sind unser Montagegebiet. Wir melden uns innerhalb eines Werktags.",
    },
    # ------------------------------------------------------------------ 5
    {
        "slug": "projekt-bitumendach-in-niederoesterreich",
        "anchor": "bitumendach-niederoesterreich",
        "titel": "Einfamilienhaus in Niederösterreich: 18 kWp auf drei Dachflächen eines neuen Bitumendachs",
        "kurz": "Bitumendach Niederösterreich, 18 kWp",
        "ort": "Niederösterreich",
        "typ": "Einfamilienhaus",
        "eyebrow": "Referenzprojekt · Einfamilienhaus · Niederösterreich",
        "title": "Referenz: 18 kWp auf Bitumendach in Niederösterreich | EBZ",
        "desc": ("Referenzprojekt Niederösterreich: 18 kWp in Süd, West und Ost auf einem neuen Bitumendach, "
                 "16-kWh-Speicher, Notstrom, rund 4.400 € Ersparnis pro Jahr*."),
        "lead": ("Süd, West und Ost: Die 18 kWp verteilen sich auf drei Flächen eines frisch eingedeckten Bitumendachs. Die "
                 "Produktion beginnt im Osten, läuft über den Süden und endet im Westen. Ein 16-kWh-Speicher und manueller "
                 "Notstrom sichern Abend und Netzausfall ab. Rund 18.000 kWh im Jahr, Amortisation in etwa 5,2 Jahren*."),
        "badges": [("18 kWp", "Süd, West und Ost"), ("16 kWh", "Speicher mit Notstrom"), ("4.400 €", "Ersparnis pro Jahr*")],
        "hero_img": R["noe_1"],
        "hero_alt": "Drohnenaufnahme eines Einfamilienhauses in Niederösterreich mit Photovoltaik-Modulen in Süd-, West- und Ostausrichtung auf dem neuen Bitumendach",
        "kpis": [("18 kWp", "Leistung, 3 Ausrichtungen"), ("16 kWh", "Speicher, Notstrom manuell"), ("~18.000 kWh", "Jahresertrag"), ("~5,2 Jahre", "Amortisation*")],
        "eckdaten": [
            ("Standort", "Niederösterreich"), ("Gebäudetyp", "Einfamilienhaus"),
            ("Leistung", "18 kWp"), ("Module", "Glas-Glas, bifazial"),
            ("Speicher", "16 kWh"), ("System", "Sigenergy All-in-One"),
            ("Notstrom", "manuelle Umschaltung"), ("Ausrichtung", "Süd, West und Ost auf drei Dachflächen"),
            ("Dach und Montage", "neues, frisch eingedecktes Bitumendach"),
            ("Jahresertrag", "rund 18.000 kWh"), ("Ersparnis", "rund 4.400 € pro Jahr*"),
            ("Amortisation", "ca. 5,2 Jahre*"), ("Garantie", GARANTIE),
        ],
        "ausgangslage": [
            ("Das Haus bekam ein neues Bitumendach. Das war der richtige Moment für Photovoltaik: Ein frisch eingedecktes Dach "
             "ist dicht, sauber und für Jahrzehnte gemacht, passend zur langen Lebensdauer der Module. Wer die Anlage erst "
             "später montiert, muss sie für eine Dachsanierung wieder abnehmen."),
            ("Die Familie ist tagsüber oft außer Haus, der Verbrauch steigt morgens und abends. Eine reine Südanlage mit "
             "Mittagsspitze hätte viel Strom zu Zeiten geliefert, in denen niemand zu Hause ist. Gesucht war ein Ertragsverlauf, "
             "der zum Alltag passt."),
        ],
        "loesung_h2": "Die Lösung: drei Himmelsrichtungen, 16 kWh für den Abend, Notstrom",
        "loesung": [
            ("Die 18 kWp Glas-Glas-Module verteilen sich auf die Süd-, West- und Ostfläche des neuen Dachs. Die Ostfläche liefert "
             "am Morgen für Frühstück und Start in den Tag, die Südfläche zur Mittagszeit und lädt den Speicher, die Westfläche "
             "am Abend, wenn die Familie nach Hause kommt. Zusammen ergibt das einen bemerkenswert gleichmäßigen Ertragsverlauf."),
            ("Das Sigenergy-System bündelt Wechselrichter und 16-kWh-Speicher. Was tagsüber nicht gebraucht wird, steht am Abend "
             "und in der Nacht zur Verfügung. Bei einem Stromausfall lässt sich die Anlage manuell in den Notstrombetrieb schalten; "
             "Licht und Kühlschrank laufen dann aus dem Speicher weiter."),
        ],
        "loesung_img": R["noe_1"],
        "loesung_alt": "Glas-Glas-Module auf den Süd-, West- und Ostflächen des neuen Bitumendachs in Niederösterreich",
        "komponenten": [
            "18 kWp Glas-Glas-Module, bifazial, Süd, West und Ost",
            B_SIGENERGY,
            "16 kWh Batteriespeicher: Sonnenstrom für Abend und Nacht, Reserve für Notstrom",
            B_NOTSTROM_MAN,
            "Montage auf neuem Bitumendach: Dach und Module mit langer Lebensdauer, kein späterer Umbau",
        ],
        "ergebnis": [
            ("Das Einfamilienhaus in Niederösterreich erzeugt mit 18 kWp bifazialen Glas-Glas-Modulen auf drei Dachflächen "
             "rund 18.000 kWh Strom pro Jahr. Mit dem 16-kWh-Speicher spart die Familie rund 4.400 € Stromkosten jährlich*, die "
             f"Amortisation liegt bei etwa 5,2 Jahren*. Geplant und montiert von EBZ Energie ({STAND})."),
            ("Der geglättete Tagesverlauf trifft den realen Bedarf besser als eine Mittagsspitze, so bleibt mehr Strom im eigenen "
             "Haus. Nach der Amortisation produziert die Anlage weiter, bei bis zu 30 Jahren Leistungsgarantie auf die Module."),
        ],
        "faq": [
            ("Was bringt die Verteilung auf Süd, West und Ost?",
             "Statt einer einzigen Mittagsspitze wie bei einer reinen Südanlage verteilt sich die Produktion über den ganzen Tag: "
             "Die Ostfläche liefert am Morgen, die Südfläche zu Mittag und die Westfläche am Abend. Dieser geglättete Ertragsverlauf "
             "passt besser zum typischen Tagesverbrauch und erhöht den Anteil des selbst genutzten Stroms."),
            ("Welchen Vorteil hat ein neues Bitumendach für die Photovoltaik?",
             "Ein frisch eingedecktes Bitumendach ist dicht, sauber und für Jahrzehnte gemacht. So passt die Lebensdauer des Dachs "
             "zur langen Garantie der Glas-Glas-Module, und man spart sich den späteren Umbau, bei dem die Module für eine "
             "Dachsanierung wieder abgenommen werden müssten."),
            ("Was bedeutet die manuelle Notstromumschaltung?",
             "Bei einem Stromausfall lässt sich die Anlage manuell auf Notstrombetrieb umschalten. Wichtige Verbraucher wie Licht "
             "und Kühlschrank werden dann aus dem 16-kWh-Speicher versorgt, sodass das Haus auch ohne Netz für eine gewisse Zeit "
             "funktionsfähig bleibt. Eine automatische Umschaltung über Gatewaybox ist optional möglich."),
            ("Lohnt sich Photovoltaik in Niederösterreich?",
             "Ja. Diese Anlage spart rund 4.400 € Stromkosten pro Jahr* und hat sich nach etwa 5,2 Jahren amortisiert. Danach folgen "
             "viele Jahre günstiger Eigenstrom, dazu die Unabhängigkeit von steigenden Strompreisen. EBZ montiert in Kärnten und der "
             "Steiermark, Referenzen wie diese gibt es in sechs Bundesländern."),
        ],
        "related": [
            ("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
            ("/photovoltaik-foerderung-niederoesterreich/", "PV-Förderung Niederösterreich 2026"),
            ("/notstrom/", "Notstrom mit Photovoltaik: Ersatzstrom erklärt"),
            ("batteriespeicher", "Batteriespeicher: Größe und Nutzen"),
        ],
        "contact_h": "Neues Dach geplant? Jetzt ist der richtige Moment",
        "contact_sub": ("Dachsanierung und Photovoltaik in einem Zug sparen den späteren Umbau. Wir prüfen Ausrichtung, Flächen "
                        "und Speichergröße für Ihr Haus. Kostenlos und unverbindlich."),
        "final_h": "Strom von früh bis spät, passend zu Ihrem Alltag",
        "final_t": "Erzählen Sie uns, wann bei Ihnen Strom gebraucht wird. Wir planen die Ausrichtung danach.",
    },
    # ------------------------------------------------------------------ 6
    {
        "slug": "projekt-pv-wien",
        "anchor": "wohnhaus-wien",
        "titel": "Wohnhaus in Wien: 10,92 kWp mit 20-kWh-Speicher, Wallbox und Warmwasser aus PV-Überschuss",
        "kurz": "Wohnhaus Wien, 10,92 kWp",
        "ort": "Wien",
        "typ": "Wohnhaus",
        "eyebrow": "Referenzprojekt · Wohnhaus · Wien",
        "title": "Referenz: Wohnhaus Wien, 10,92 kWp mit 20 kWh Speicher | EBZ",
        "desc": ("Referenzprojekt Wien: 10,92 kWp in Süd und Ost auf Schindeldach, 20-kWh-Speicher, Wallbox 11 kW, "
                 "my-PV-Warmwasser, Notstrom, rund 3.360 € Ersparnis pro Jahr*."),
        "lead": ("Die vollständigste Ausstattung unserer Referenzauswahl: 10,92 kWp bifaziale Glas-Glas-Module in Süd- und "
                 "Ostausrichtung auf einem Schindeldach, 20-kWh-Speicher, 11-kW-Wallbox, ein my-PV-Regler, der Überschuss in "
                 "warmes Wasser verwandelt, und manueller Notstrom. Rund 12.000 kWh im Jahr, Amortisation in etwa 6 Jahren*."),
        "badges": [("10,92 kWp", "Süd und Ost"), ("20 kWh", "Speicher + Wallbox 11 kW"), ("3.360 €", "Ersparnis pro Jahr*")],
        "hero_img": R["wien_1"],
        "hero_alt": "Drohnenaufnahme eines Wohnhauses in Wien mit Photovoltaik-Modulen in Süd- und Ostausrichtung auf dem Schindeldach",
        "kpis": [("10,92 kWp", "Leistung, Süd und Ost"), ("20 kWh", "Speicher, Notstrom manuell"), ("~12.000 kWh", "Jahresertrag"), ("~6 Jahre", "Amortisation*")],
        "eckdaten": [
            ("Standort", "Wien"), ("Gebäudetyp", "Wohnhaus"),
            ("Leistung", "10,92 kWp"), ("Module", "Glas-Glas, bifazial"),
            ("Speicher", "20 kWh"), ("System", "Sigenergy All-in-One"),
            ("Wallbox", "11 kW, dreiphasig"), ("Warmwasser", "my-PV-Regler, Heizstab aus PV-Überschuss"),
            ("Notstrom", "manuelle Umschaltung"), ("Ausrichtung", "Süd und Ost"),
            ("Dach und Montage", "Schindeldach, Ersatzziegel mit integrierter Halterung"),
            ("Jahresertrag", "rund 12.000 kWh"), ("Ersparnis", "rund 3.360 € pro Jahr*"),
            ("Amortisation", "ca. 6 Jahre*"), ("Garantie", GARANTIE),
        ],
        "ausgangslage": [
            ("Ein anspruchsvolles Dach in Wien: Schindeleindeckung, zwei nutzbare Flächen nach Süden und Osten, und der Wunsch, "
             "möglichst wenig Strom zu niedrigen Tarifen ins Netz zu geben. Die Familie wollte nicht nur Strom erzeugen, sondern "
             "das E-Auto laden, Warmwasser bereiten und bei Netzausfall versorgt bleiben."),
            ("Die Befestigung auf dem Schindeldach musste regensicher sein, ohne die Dichtheit der Dachhaut zu beeinträchtigen. "
             "Und alle Bausteine sollten als ein System zusammenarbeiten, nicht als Sammlung einzelner Geräte."),
            ("Besonders wichtig war der Umgang mit dem Überschuss: An sonnigen Tagen erzeugt eine 10,92-kWp-Anlage mehr, als ein "
             "Haushalt gleichzeitig verbraucht. Dieser Strom sollte im Haus bleiben statt ins Netz zu gehen."),
        ],
        "loesung_h2": "Die Lösung: Süd-Ost-Belegung, 20 kWh, Wallbox und Warmwasser aus Überschuss",
        "loesung": [
            ("Für die Montage wurden einzelne Schindeln durch passende Ersatzziegel mit integrierter Halterung ersetzt. So sitzt "
             "die Unterkonstruktion sicher und das Dach bleibt vollständig dicht. Die 10,92 kWp Glas-Glas-Module liefern in Süd- "
             "und Ostausrichtung vom Vormittag bis in den Nachmittag gleichmäßig Strom."),
            ("Das Sigenergy-System verbindet Wechselrichter, 20-kWh-Speicher und 11-kW-Wallbox. Erzeugt die Anlage mehr, als Haus, "
             "Auto und Speicher aufnehmen, leitet der my-PV-Regler den Überschuss stufenlos in den Heizstab des Warmwasserspeichers. "
             "Die Sonne heizt das Brauchwasser, statt dass der Strom günstig eingespeist wird. Bei Netzausfall lässt sich die Anlage "
             "manuell in den Notstrombetrieb schalten."),
        ],
        "loesung_img": R["wien_1"],
        "loesung_alt": "Photovoltaik-Module in Süd- und Ostausrichtung auf dem Schindeldach des Wohnhauses in Wien, befestigt über Ersatzziegel",
        "komponenten": [
            "10,92 kWp Glas-Glas-Module, bifazial, Süd und Ost",
            B_SIGENERGY,
            "20 kWh Batteriespeicher: Sonnenstrom rund um die Uhr, Reserve für Notstrom",
            B_WALLBOX,
            "my-PV-Warmwasser: PV-Überschuss wird stufenlos zu warmem Wasser statt zu Niedrigtarif-Einspeisung",
            B_NOTSTROM_MAN,
            "Schindeldach mit Ersatzziegeln und integrierter Halterung: regensicher, sauberes Erscheinungsbild",
        ],
        "ergebnis": [
            ("Das Wohnhaus in Wien erzeugt mit 10,92 kWp bifazialen Glas-Glas-Modulen in Süd- und Ostausrichtung rund 12.000 kWh "
             "Strom pro Jahr. Mit 20-kWh-Speicher, 11-kW-Wallbox und my-PV-Warmwasser spart die Familie rund 3.360 € Stromkosten "
             f"jährlich*, die Amortisation liegt bei etwa 6 Jahren*. Geplant und montiert von EBZ Energie ({STAND})."),
            ("Der Überschuss landet im E-Auto und im Warmwasser statt zu niedrigen Tarifen im Netz. Nach der Amortisation "
             "produziert die Anlage weiter, bei bis zu 30 Jahren Leistungsgarantie auf die Module über Jahrzehnte."),
        ],
        "faq": [
            ("Wie funktioniert die my-PV-Warmwasserbereitung?",
             "Sobald die Anlage mehr Strom erzeugt, als gerade verbraucht oder gespeichert wird, leitet der my-PV-Regler diesen "
             "Überschuss stufenlos in einen Heizstab im Warmwasserspeicher. So wird günstiger Sonnenstrom in warmes Wasser "
             "umgewandelt, statt ihn zu niedrigen Tarifen ins Netz einzuspeisen."),
            ("Wie wird eine PV-Anlage auf einem Schindeldach befestigt?",
             "Für die Befestigung werden einzelne Schindeln durch passende Ersatzziegel mit integrierter Halterung ersetzt. So "
             "sitzt die Unterkonstruktion sicher und das Dach bleibt vollständig dicht, fachgerecht und regensicher eingedeckt."),
            ("Kann ich das E-Auto mit dem eigenen Sonnenstrom laden?",
             "Ja. Die 11-kW-Wallbox lädt dreiphasig rund fünfmal schneller als eine Haushaltssteckdose, ein E-Auto ist über Nacht "
             "voll. Weil Wallbox, Speicher und Wechselrichter aus dem Sigenergy-System stammen, lädt das Auto bevorzugt mit "
             "selbst erzeugtem PV-Strom."),
            ("Lohnt sich Photovoltaik in Wien?",
             "Ja. Diese Anlage spart rund 3.360 € Stromkosten pro Jahr* und hat sich nach etwa 6 Jahren amortisiert. Danach folgen "
             "viele Jahre günstiger Eigenstrom für Haus, Auto und Warmwasser. EBZ montiert in Kärnten und der Steiermark, "
             "Referenzen wie diese gibt es in sechs Bundesländern."),
        ],
        "related": [
            ("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
            ("/photovoltaik-foerderung-wien/", "PV-Förderung Wien 2026"),
            ("/ab-wann-lohnt-sich-photovoltaik-mit-speicher/", "Ab wann lohnt sich Photovoltaik mit Speicher?"),
            ("batteriespeicher", "Batteriespeicher mit Wallbox"),
        ],
        "contact_h": "Mehr als Module: Speicher, Wallbox, Warmwasser",
        "contact_sub": ("Wir planen das ganze Energiesystem, nicht nur das Dach. Sagen Sie uns, was Sie mit Ihrem Sonnenstrom "
                        "versorgen wollen. Kostenlos und unverbindlich."),
        "final_h": "Ihr Überschuss gehört ins Auto und ins Warmwasser",
        "final_t": "Wir zeigen Ihnen, wie viel Sonnenstrom Sie selbst nutzen können. Antwort innerhalb eines Werktags.",
    },
    # ------------------------------------------------------------------ 7
    {
        "slug": "projekt-pv-am-ossiachersee",
        "anchor": "einfamilienhaus-ossiachersee",
        "titel": "Einfamilienhaus am Ossiachersee: 10 kWp Ost-West auf Ziegeldach mit 9-kWh-Speicher und Wallbox",
        "kurz": "Einfamilienhaus Ossiachersee, 10 kWp",
        "ort": "Ossiachersee, Kärnten",
        "typ": "Einfamilienhaus",
        "eyebrow": "Referenzprojekt · Einfamilienhaus · Ossiachersee",
        "title": "Referenz: 10 kWp Ost-West am Ossiachersee mit Wallbox | EBZ",
        "desc": ("Referenzprojekt Ossiachersee: 10 kWp Ost-West auf Bramac-Ziegeldach, 9-kWh-Speicher, Wallbox 11 kW, "
                 "rund 11.000 kWh und 3.200 € Ersparnis pro Jahr*."),
        "lead": ("Sonnenstrom mit Seeblick: 10 kWp bifaziale Glas-Glas-Module in Ost-West-Ausrichtung auf einem Bramac-Ziegeldach, "
                 "befestigt über Marzari-Ersatzziegel, regensicher und unauffällig. Ein 9-kWh-Speicher und eine 11-kW-Wallbox "
                 "versorgen Haus und E-Auto. Rund 11.000 kWh im Jahr, Amortisation in etwa 5,4 Jahren*."),
        "badges": [("10 kWp", "Ost-West, Glas-Glas"), ("9 kWh", "Speicher + Wallbox 11 kW"), ("3.200 €", "Ersparnis pro Jahr*")],
        "hero_img": R["ossiach_1"],
        "hero_alt": "Einfamilienhaus am Ossiachersee mit Photovoltaik-Modulen auf dem Ziegeldach, umgeben von Bäumen",
        "kpis": [("10 kWp", "Leistung, Ost-West"), ("9 kWh", "Speicher + Wallbox"), ("~11.000 kWh", "Jahresertrag"), ("~5,4 Jahre", "Amortisation*")],
        "eckdaten": [
            ("Standort", "Ossiachersee, Kärnten"), ("Gebäudetyp", "Einfamilienhaus"),
            ("Leistung", "10 kWp"), ("Module", "Glas-Glas, bifazial"),
            ("Speicher", "9 kWh"), ("System", "Sigenergy All-in-One"),
            ("Wallbox", "11 kW, dreiphasig"), ("Ausrichtung", "Ost und West"),
            ("Dach und Montage", "Bramac-Ziegeldach, Marzari-Ersatzziegel mit Halterung"),
            ("Jahresertrag", "rund 11.000 kWh"), ("Ersparnis", "rund 3.200 € pro Jahr*"),
            ("Amortisation", "ca. 5,4 Jahre*"), ("Garantie", GARANTIE),
        ],
        "ausgangslage": [
            ("Ein Einfamilienhaus am Ossiachersee mit Bramac-Ziegeldach und zwei Dachseiten nach Osten und Westen. Die Familie "
             "fährt elektrisch und wollte das Auto mit eigenem Strom laden, ohne dass tagsüber die Mittagsspitze ungenutzt ins "
             "Netz fließt."),
            ("Beim Ziegeldach zählt die Dichtheit: Die Befestigung sollte regensicher sein und optisch nicht auffallen. Dazu "
             "sollte die Anlage im Budget eines typischen Eigenheims bleiben und sich innerhalb weniger Jahre rechnen."),
            ("Der Speicher sollte bewusst kompakt bleiben: groß genug für den Abend, aber nicht überdimensioniert, weil ein Teil "
             "des Überschusses ohnehin direkt ins E-Auto fließt."),
        ],
        "loesung_h2": "Die Lösung: Ost-West auf Ersatzziegeln, 9 kWh Speicher, 11-kW-Wallbox",
        "loesung": [
            ("Für die Befestigung wurden einzelne Bramac-Ziegel durch Marzari-Ersatzziegel mit integrierter Halterung getauscht. "
             "Die Unterkonstruktion sitzt sicher, das Dach bleibt vollständig dicht, und die Anlage wirkt wie Teil des Dachs. Die "
             "10 kWp Glas-Glas-Module liefern morgens von der Ostseite und abends von der Westseite."),
            ("Das Sigenergy-System bündelt Wechselrichter, 9-kWh-Speicher und 11-kW-Wallbox. Der Speicher legt Sonnenstrom für "
             "Abend und Nacht zurück, die Wallbox lädt das E-Auto dreiphasig und bevorzugt mit eigenem PV-Strom. Was übrig bleibt, "
             "geht ins Netz. Mit 9 kWh ist der Speicher bewusst kompakt dimensioniert: Er deckt den Abend ab, ohne dass Kapazität ungenutzt bleibt."),
        ],
        "loesung_img": R["ossiach_1"],
        "loesung_alt": "Glas-Glas-Module auf dem Bramac-Ziegeldach des Einfamilienhauses am Ossiachersee, befestigt über Marzari-Ersatzziegel",
        "komponenten": [
            "10 kWp Glas-Glas-Module, bifazial, Ost-West",
            B_SIGENERGY,
            "9 kWh Batteriespeicher: Sonnenstrom für Abend und Nacht, weniger Netzbezug",
            B_WALLBOX,
            "Bramac-Ziegeldach mit Marzari-Ersatzziegeln: regensicher, passgenau, unauffällig",
        ],
        "ergebnis": [
            ("Das Einfamilienhaus am Ossiachersee erzeugt mit 10 kWp bifazialen Glas-Glas-Modulen in Ost-West-Ausrichtung rund "
             "11.000 kWh Strom pro Jahr. Mit 9-kWh-Speicher und 11-kW-Wallbox spart die Familie rund 3.200 € Stromkosten jährlich*, "
             f"die Amortisation liegt bei etwa 5,4 Jahren*. Geplant und montiert von EBZ Energie aus Villach ({STAND})."),
            (f"{RICHTPREIS}. Diese Anlage zeigt, was ein typisches Eigenheim damit erreicht: Haus und Auto fahren mit Sonnenstrom, "
             "nach der Amortisation bei bis zu 30 Jahren Leistungsgarantie auf die Module noch viele Jahre lang."),
        ],
        "faq": [
            ("Was bedeutet Bramac-Ziegeldach mit Marzari-Ersatzziegeln?",
             "Bramac ist der Hersteller der vorhandenen Dachziegel. Für die Montage werden einzelne Ziegel durch Marzari-Ersatzziegel "
             "mit integrierter Halterung ersetzt. So wird die Unterkonstruktion sauber und regensicher am Dach befestigt, ohne die "
             "Dichtheit der Dachhaut zu beeinträchtigen."),
            ("Was bringt die Ost-West-Ausrichtung beim Eigenheim?",
             "Statt einer einzelnen Ertragsspitze zur Mittagszeit liefert eine Ost-West-Anlage über den ganzen Tag verteilt Strom: "
             "morgens von der Ostseite, abends von der Westseite. Das passt zum Tagesverbrauch eines Haushalts und erhöht den "
             "Eigenverbrauch, weil weniger Strom ungenutzt ins Netz fließt."),
            ("Wie schnell lädt die 11-kW-Wallbox?",
             "Mit 11 kW dreiphasig lädt die Wallbox rund fünfmal schneller als eine normale Haushaltssteckdose. Ein durchschnittliches "
             "E-Auto ist damit über Nacht vollständig geladen, bevorzugt mit eigenem PV-Strom, weil Wallbox, Speicher und "
             "Wechselrichter aus dem Sigenergy-System stammen."),
            ("Was kostet eine 10-kWp-Anlage mit Speicher wie diese?",
             f"{RICHTPREIS}, abhängig von Dach, Speichergröße und Zubehör wie Wallbox. Der EAG-Investitionszuschuss und die "
             "Kärntner Landesförderung senken den Preis zusätzlich. Diese Anlage amortisiert sich in rund 5,4 Jahren*."),
        ],
        "related": [
            ("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
            ("/photovoltaik-foerderung-kaernten/", "PV-Förderung Kärnten 2026"),
            ("/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/", "PV-Komplettanlage 10 kWp mit Speicher: Kosten"),
            ("pv_villach", "Photovoltaik in Villach und Umgebung"),
        ],
        "contact_h": "Ziegeldach am See oder in der Stadt?",
        "contact_sub": ("Ost-West, Süd oder beides: Wir planen die Belegung nach Ihrem Dach und Ihrem Verbrauch. Kostenlos und "
                        "unverbindlich, Montage in Kärnten und der Steiermark."),
        "final_h": "Ihr Eigenheim kann das auch",
        "final_t": "10 kWp mit Speicher und Wallbox sind unser häufigstes Projekt. Wir melden uns innerhalb eines Werktags.",
    },
    # ------------------------------------------------------------------ 8
    {
        "slug": "projekt-flachdach-in-graz",
        "anchor": "flachdach-graz",
        "titel": "Flachdach in Graz: 11,83 kWp ballastiert auf Sarnafil-Folie, ohne eine einzige Bohrung",
        "kurz": "Flachdach Graz, 11,83 kWp",
        "ort": "Graz, Steiermark",
        "typ": "Einfamilienhaus",
        "eyebrow": "Referenzprojekt · Einfamilienhaus · Graz",
        "title": "Referenz: Flachdach Graz, 11,83 kWp ballastiert | EBZ",
        "desc": ("Referenzprojekt Flachdach Graz: 11,83 kWp in Süd auf Sarnafil-Folie, ballastiert ohne Bohrung, "
                 "20-kWh-Speicher, Wallbox 11 kW, rund 3.500 € Ersparnis pro Jahr*."),
        "lead": ("Zwei Modulfelder mit zusammen 11,83 kWp in Südausrichtung auf dem Sarnafil-Flachdach eines Einfamilienhauses. "
                 "Das Montagesystem ist komplett ballastiert, die Folie bleibt unversehrt und zu 100 % dicht. Mit 20-kWh-Speicher, "
                 "11-kW-Wallbox und Notstrom ist das Haus weitgehend unabhängig. Rund 13.000 kWh im Jahr, Amortisation in etwa 5 Jahren*."),
        "badges": [("11,83 kWp", "Süd, ballastiert"), ("20 kWh", "Speicher + Wallbox 11 kW"), ("3.500 €", "Ersparnis pro Jahr*")],
        "hero_img": R["graz_flach_1"],
        "hero_alt": "Drohnen-Draufsicht auf zwei Modulfelder der 11,83-kWp-Photovoltaikanlage auf dem Flachdach eines Einfamilienhauses in Graz mit Pool im Garten",
        "kpis": [("11,83 kWp", "Leistung, Süd"), ("20 kWh", "Speicher, Notstrom manuell"), ("~13.000 kWh", "Jahresertrag"), ("~5 Jahre", "Amortisation*")],
        "eckdaten": [
            ("Standort", "Graz, Steiermark"), ("Gebäudetyp", "Einfamilienhaus mit Flachdach"),
            ("Leistung", "11,83 kWp"), ("Module", "Glas-Glas, bifazial"),
            ("Speicher", "20 kWh"), ("System", "Sigenergy All-in-One"),
            ("Wallbox", "11 kW, dreiphasig"), ("Notstrom", "manuelle Umschaltung"),
            ("Ausrichtung", "Süd, zwei Modulfelder"), ("Dach und Montage", "Sarnafil-Flachdach, ballastiertes Montagesystem, keine Dachdurchdringung"),
            ("Jahresertrag", "rund 13.000 kWh"), ("Ersparnis", "rund 3.500 € pro Jahr*"),
            ("Amortisation", "ca. 5 Jahre*"), ("Garantie", GARANTIE),
        ],
        "ausgangslage": [
            ("Ein modernes Einfamilienhaus in Graz mit Flachdach, Pool und E-Auto. Die Dachhaut ist eine Sarnafil-Kunststoffbahn, "
             "und die hat eine klare Bedingung: keine Bohrung, keine Durchdringung. Jede Verletzung der Folie wäre ein Risiko für "
             "die Dichtheit des ganzen Hauses."),
            ("Die Familie wollte möglichst unabhängig werden: Strom für Haus, Pooltechnik und Auto, Reserve für den Abend und "
             "Sicherheit bei Netzausfall. Das helle Flachdach bot dafür eine Besonderheit, die bifaziale Module ausnutzen können."),
            ("Ein Flachdach erlaubt außerdem die freie Wahl der Ausrichtung und des Neigungswinkels. Die Aufgabe war, die Fläche "
             "in Südausrichtung optimal zu belegen und zugleich die Statik mit dem Ballast im Blick zu behalten."),
        ],
        "loesung_h2": "Die Lösung: Südaufständerung mit Ballast, 20 kWh, Wallbox und Notstrom",
        "loesung": [
            ("Die 11,83 kWp Glas-Glas-Module stehen in zwei Feldern auf einem ballastierten Montagesystem, gehalten von Gewichten, "
             "nicht von Schrauben. Die Sarnafil-Folie bleibt zu 100 % dicht, die Anlage sitzt sturmsicher. Weil die Module "
             "bifazial sind, nutzen sie auch das vom hellen Dach reflektierte Licht, das steigert den Ertrag."),
            ("Das Sigenergy-System bündelt Wechselrichter, 20-kWh-Speicher und 11-kW-Wallbox. Der große Speicher versorgt Abend und "
             "Nacht, die Wallbox lädt das E-Auto bevorzugt mit Sonnenstrom. Bei Netzausfall lässt sich die Anlage manuell in den "
             "Notstrombetrieb schalten; Licht und Kühlschrank laufen aus dem Speicher weiter."),
        ],
        "loesung_img": R["graz_flach_1"],
        "loesung_alt": "Zwei ballastierte Modulfelder in Südausrichtung auf dem Sarnafil-Flachdach des Einfamilienhauses in Graz",
        "komponenten": [
            "11,83 kWp Glas-Glas-Module, bifazial, Süd auf zwei Modulfeldern",
            B_SIGENERGY,
            "20 kWh Batteriespeicher: Sonnenstrom rund um die Uhr, Reserve für Notstrom",
            B_WALLBOX,
            B_NOTSTROM_MAN,
            "Ballastiertes Montagesystem auf Sarnafil: keine Dachdurchdringung, 100 % dicht, sturmsicher",
        ],
        "ergebnis": [
            ("Das Einfamilienhaus mit Flachdach in Graz erzeugt mit 11,83 kWp bifazialen Glas-Glas-Modulen in Südausrichtung rund "
             "13.000 kWh Strom pro Jahr. Mit 20-kWh-Speicher und 11-kW-Wallbox spart die Familie rund 3.500 € Stromkosten jährlich*, "
             f"die Amortisation liegt bei etwa 5 Jahren*. Montiert ohne eine einzige Dachdurchdringung ({STAND})."),
            ("Haus, Pool und Auto laufen weitgehend mit eigenem Strom, bei Netzausfall übernimmt der Speicher. Nach der Amortisation "
             "produziert die Anlage weiter, bei bis zu 30 Jahren Leistungsgarantie auf die Module über Jahrzehnte."),
        ],
        "faq": [
            ("Wie wird die Anlage auf dem Flachdach befestigt?",
             "Die Module werden auf einem ballastierten Montagesystem verankert und mit Gewichten (Ballaststeinen) auf dem "
             "Sarnafil-Flachdach gehalten. Es sind keine Dachdurchdringungen nötig, die Dachhaut bleibt vollständig dicht und die "
             "Anlage sicher fixiert."),
            ("Was bringt der 20-kWh-Speicher bei einer 11,83-kWp-Anlage?",
             "Der große Speicher legt tagsüber erzeugten Sonnenstrom für Abend und Nacht zurück. Dadurch wird ein sehr hoher Anteil "
             "des selbst produzierten Stroms auch selbst verbraucht, der Zukauf von teurem Netzstrom sinkt deutlich. Zusätzlich dient "
             "er als Reserve für den Notstrombetrieb und für das Laden des E-Autos."),
            ("Was bedeutet die manuelle Notstromumschaltung?",
             "Bei einem Stromausfall lässt sich die Anlage manuell auf Notstrombetrieb umschalten. Wichtige Verbraucher wie Licht und "
             "Kühlschrank werden dann aus dem Speicher versorgt, sodass das Haus auch ohne Netz für eine gewisse Zeit funktionsfähig "
             "bleibt."),
            ("Lohnt sich Photovoltaik auf einem Flachdach in Graz?",
             "Ja. Diese Anlage spart rund 3.500 € Stromkosten pro Jahr* und hat sich nach etwa 5 Jahren amortisiert. Flachdächer "
             "erlauben die freie Wahl der Ausrichtung und eine Montage ohne Bohrung. Danach folgen viele Jahre günstiger Eigenstrom "
             "für Haus, Pool und Auto."),
        ],
        "related": [
            ("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
            ("/foerderung-photovoltaik-steiermark/", "PV-Förderung Steiermark 2026"),
            ("/notstrom/", "Notstrom mit Photovoltaik: Ersatzstrom erklärt"),
            ("batteriespeicher", "Batteriespeicher: Größe und Nutzen"),
        ],
        "contact_h": "Flachdach mit Folie? Wir bohren nicht",
        "contact_sub": ("Ballastierte Montage schützt Ihre Dachhaut. Schicken Sie uns ein Foto oder die Adresse, wir prüfen "
                        "Statik, Belegung und Speichergröße. Kostenlos und unverbindlich."),
        "final_h": "Ihr Flachdach wird zum Kraftwerk",
        "final_t": "Graz und die Steiermark gehören zu unserem Montagegebiet. Wir melden uns innerhalb eines Werktags.",
    },
    # ------------------------------------------------------------------ 9 (kurz, keine alte Unterseite)
    {
        "slug": "projekt-einfamilienhaus-villach",
        "anchor": "einfamilienhaus-villach",
        "titel": "Einfamilienhaus in Villach: 10 kWp Ost-West mit automatischem Notstrom, rund 80 % weniger Stromkosten",
        "kurz": "Einfamilienhaus Villach, 10 kWp",
        "ort": "Villach, Kärnten",
        "typ": "Einfamilienhaus",
        "eyebrow": "Referenzprojekt · Einfamilienhaus · Villach",
        "title": "Referenz: Einfamilienhaus Villach, 10 kWp mit Notstrom | EBZ",
        "desc": ("Referenzprojekt Villach: 10 kWp Ost-West auf Satteldach mit Bitumeneindeckung, automatischer Notstrom, "
                 "rund 11.000 kWh pro Jahr und 80 % weniger Stromkosten*."),
        "lead": ("Ein klassisches Eigenheim-Projekt vor unserer Haustür: 10 kWp in Ost-West-Ausrichtung auf einem Satteldach mit "
                 "Bitumeneindeckung, dazu automatische Notstromumschaltung. Rund 11.000 kWh Jahresertrag decken im Sommer die "
                 "komplette Pooltechnik, die Stromkosten sanken um rund 80 %*."),
        "badges": [("10 kWp", "Ost-West auf Satteldach"), ("Notstrom", "automatische Umschaltung"), ("~80 %", "weniger Stromkosten*")],
        "hero_img": IMG["ref_villach"],
        "hero_alt": "Nahaufnahme der Photovoltaik-Module auf dem Ost-West-Satteldach eines Einfamilienhauses in Villach mit Bergen im Hintergrund",
        "kpis": [("10 kWp", "Leistung, Ost-West"), ("~11.000 kWh", "Jahresertrag"), ("~80 %", "weniger Stromkosten*"), ("Notstrom", "automatisch")],
        "eckdaten": [
            ("Standort", "Villach, Kärnten"), ("Gebäudetyp", "Einfamilienhaus mit Pool"),
            ("Leistung", "10 kWp"), ("Ausrichtung", "Ost und West"),
            ("Dach und Montage", "Satteldach mit Bitumeneindeckung"), ("Notstrom", "automatische Umschaltung"),
            ("Speicher", "in den Projektdaten nicht erfasst"),
            ("Jahresertrag", "rund 11.000 kWh"), ("Ergebnis", "rund 80 % weniger Stromkosten*, Pool im Sommer zu 100 % versorgt"),
            ("Garantie", GARANTIE),
        ],
        "ausgangslage": [
            ("Ein Einfamilienhaus in Villach mit Satteldach in Ost-West-Lage und einem Pool, dessen Technik im Sommer zu den größten "
             "Stromverbrauchern gehört. Die Familie wollte ihre Stromrechnung deutlich senken und bei Netzausfall nicht ohne Strom "
             "dastehen."),
            ("Zwei Dachseiten nach Osten und Westen sind für ein Eigenheim kein Nachteil: Sie liefern von der Morgen- bis zur "
             "Abendsonne und passen damit zum Tagesablauf einer Familie besser als eine reine Mittagsspitze."),
        ],
        "loesung_h2": "Die Lösung: 10 kWp auf beiden Dachseiten, Notstrom automatisch",
        "loesung": [
            ("Die 10 kWp verteilen sich auf die Ost- und die Westseite des Satteldachs mit Bitumeneindeckung. So beginnt die "
             "Produktion am Morgen und reicht bis in den Abend. Im Sommer versorgt die Anlage die komplette Pooltechnik aus eigenem Strom."),
            ("Mit automatischer Notstromumschaltung bleibt das Haus auch bei Netzausfall versorgt, ohne dass jemand eingreifen muss."),
        ],
        "loesung_img": IMG["ref_villach"],
        "loesung_alt": "Photovoltaik-Module auf dem Satteldach des Einfamilienhauses in Villach, Ost-West-Ausrichtung",
        "komponenten": [
            "10 kWp Photovoltaik, Ost-West auf Satteldach (Bitumen)",
            "Automatische Notstromumschaltung: Versorgung bei Netzausfall ohne Handgriff",
            "Rund 11.000 kWh Jahresertrag, Pooltechnik im Sommer zu 100 % aus Sonnenstrom",
        ],
        "ergebnis": [
            ("Das Einfamilienhaus in Villach erzeugt mit 10 kWp Photovoltaik in Ost-West-Ausrichtung rund 11.000 kWh Strom pro Jahr. "
             "Die Stromkosten der Familie sanken um rund 80 %*, die Pooltechnik läuft im Sommer vollständig mit Sonnenstrom, und die "
             f"automatische Notstromumschaltung sichert das Haus bei Netzausfall ab. Geplant und montiert von EBZ Energie aus Villach ({STAND})."),
            (f"{RICHTPREIS}. Typische EBZ-Anlagen amortisieren sich in 4 bis 6 Jahren, danach produzieren sie bei bis zu 30 Jahren "
             "Leistungsgarantie auf die Module noch viele Jahre lang günstigen Eigenstrom."),
        ],
        "faq": [
            ("Was bringt die Ost-West-Ausrichtung beim Einfamilienhaus?",
             "Zwei Dachseiten nach Osten und Westen liefern Strom von der Morgen- bis zur Abendsonne statt einer Mittagsspitze. Das "
             "passt zum Tagesablauf einer Familie und erhöht den Anteil des selbst genutzten Stroms. Bei diesem Haus reichen rund "
             "11.000 kWh im Jahr für rund 80 % weniger Stromkosten*."),
            ("Was heißt automatische Notstromumschaltung?",
             "Bei einem Netzausfall schaltet die Anlage selbstständig in den Notstrombetrieb um, ohne dass jemand einen Schalter "
             "umlegen muss. Wichtige Verbraucher im Haus bleiben versorgt. Mehr dazu im Ratgeber Notstrom mit Photovoltaik."),
            ("Was kostet eine 10-kWp-Anlage wie diese?",
             f"{RICHTPREIS}, abhängig von Dach, Speichergröße und Notstromlösung. Der EAG-Investitionszuschuss und die Kärntner "
             "Landesförderung senken den Preis zusätzlich. Den Preis für Ihr Dach liefert der Projektbericht mit 3D-Belegplan und Statikreport."),
        ],
        "related": [
            ("pv_villach", "Photovoltaik in Villach"),
            ("/notstrom/", "Notstrom mit Photovoltaik: Ersatzstrom erklärt"),
            ("/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/", "PV-Komplettanlage 10 kWp mit Speicher: Kosten"),
            ("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
        ],
        "contact_h": "Ein Eigenheim in Villach oder Umgebung?",
        "contact_sub": ("Wir sind die freundlichen Energie-Handwerker aus Villach, Triglavstraße 15. Erzählen Sie uns von Ihrem Dach, "
                        "wir sagen Ihnen ehrlich, was passt. Kostenlos und unverbindlich."),
        "final_h": "Ihr Haus in Villach kann das auch",
        "final_t": "Kurzer Weg, schnelle Besichtigung: Wir melden uns innerhalb eines Werktags.",
    },
    # ------------------------------------------------------------------ 10 (kurz, keine alte Unterseite)
    {
        "slug": "projekt-mehrparteienhaus-krumpendorf",
        "anchor": "mehrparteienhaus-krumpendorf",
        "titel": "Mehrparteienhaus in Krumpendorf: 25 kWp und 25 kWh Speicher mit Notstrom, montiert in vier Tagen",
        "kurz": "Mehrparteienhaus Krumpendorf, 25 kWp",
        "ort": "Krumpendorf am Wörthersee, Kärnten",
        "typ": "Mehrparteienhaus",
        "eyebrow": "Referenzprojekt · Mehrparteienhaus · Krumpendorf",
        "title": "Referenz: Mehrparteienhaus Krumpendorf, 25 kWp | EBZ",
        "desc": ("Referenzprojekt Krumpendorf am Wörthersee: 25 kWp Ost-West auf einem Mehrparteienhaus, 25-kWh-Speicher "
                 "mit Notstrom, Montage und Inbetriebnahme in 4 Tagen."),
        "lead": ("Mehrere Wohneinheiten, ein gemeinsames Dach: Diese 25-kWp-Anlage in Ost-West-Lage versorgt das Haus zusammen mit einem "
                 "25-kWh-Speicher auch nach Sonnenuntergang. Die Notstromversorgung sichert die wichtigsten Verbraucher bei Netzausfall. "
                 "Montage und Inbetriebnahme dauerten vier Tage."),
        "badges": [("25 kWp", "Ost-West"), ("25 kWh", "Speicher mit Notstrom"), ("4 Tage", "Montage und Inbetriebnahme")],
        "hero_img": IMG["ref_krumpendorf"],
        "hero_alt": "Drohnenaufnahme der 25-kWp-Photovoltaikanlage auf dem roten Dach eines Mehrparteienhauses in Krumpendorf",
        "kpis": [("25 kWp", "Leistung, Ost-West"), ("25 kWh", "Batteriespeicher"), ("Notstrom", "für wichtige Verbraucher"), ("4 Tage", "Bauzeit")],
        "eckdaten": [
            ("Standort", "Krumpendorf am Wörthersee, Kärnten"), ("Gebäudetyp", "Mehrparteienhaus"),
            ("Leistung", "25 kWp"), ("Ausrichtung", "Ost und West"),
            ("Speicher", "25 kWh"), ("Notstrom", "Versorgung der wichtigsten Verbraucher bei Netzausfall"),
            ("Bauzeit", "4 Tage für Montage und Inbetriebnahme"),
            ("Jahresertrag", "in den Projektdaten nicht erfasst"), ("Ersparnis", "in den Projektdaten nicht erfasst"),
            ("Garantie", GARANTIE),
        ],
        "ausgangslage": [
            ("Ein Mehrparteienhaus in Krumpendorf am Wörthersee: mehrere Wohneinheiten, ein gemeinsames Dach in Ost-West-Lage. Der "
             "Strombedarf verteilt sich über den ganzen Tag, weil in mehreren Haushalten zu unterschiedlichen Zeiten gekocht, gewaschen "
             "und gearbeitet wird."),
            ("Die Anlage sollte groß genug sein, um das Haus auch nach Sonnenuntergang zu versorgen, wichtige Verbraucher bei Netzausfall "
             "absichern und mit möglichst kurzer Bauzeit montiert werden, damit die Bewohner wenig beeinträchtigt werden."),
        ],
        "loesung_h2": "Die Lösung: 25 kWp Ost-West, 25 kWh Speicher, vier Tage Bauzeit",
        "loesung": [
            ("Die 25 kWp nutzen beide Dachseiten: Die Ostseite liefert am Morgen, die Westseite am Nachmittag und Abend. Der Ertragsverlauf "
             "passt damit zum verteilten Verbrauch mehrerer Haushalte besser als eine Mittagsspitze."),
            ("Ein 25-kWh-Speicher legt den Sonnenstrom für Abend und Nacht zurück. Die Notstromversorgung hält die wichtigsten Verbraucher "
             "bei Netzausfall am Laufen. Montage und Inbetriebnahme waren nach vier Tagen abgeschlossen."),
        ],
        "loesung_img": IMG["ref_krumpendorf"],
        "loesung_alt": "Photovoltaik-Module in Ost-West-Ausrichtung auf dem Dach des Mehrparteienhauses in Krumpendorf am Wörthersee",
        "komponenten": [
            "25 kWp Photovoltaik, Ost-West auf dem gemeinsamen Dach",
            "25 kWh Batteriespeicher: Versorgung auch nach Sonnenuntergang",
            "Notstromversorgung für die wichtigsten Verbraucher bei Netzausfall",
            "Montage und Inbetriebnahme in 4 Tagen",
        ],
        "ergebnis": [
            ("Das Mehrparteienhaus in Krumpendorf am Wörthersee wird von einer 25-kWp-Photovoltaikanlage in Ost-West-Ausrichtung und einem "
             "25-kWh-Speicher versorgt, auch nach Sonnenuntergang. Die Notstromversorgung sichert die wichtigsten Verbraucher bei Netzausfall. "
             f"Montage und Inbetriebnahme durch EBZ Energie aus Villach dauerten vier Tage ({STAND})."),
            ("Für Eigentümergemeinschaften und Vermieter zeigt das Projekt: Eine große Dachanlage mit Speicher lässt sich in wenigen Tagen "
             "umsetzen. Die Module haben bis zu 30 Jahre Leistungsgarantie."),
        ],
        "faq": [
            ("Wie lange dauert die Montage einer 25-kWp-Anlage mit Speicher?",
             "Bei diesem Mehrparteienhaus waren Montage und Inbetriebnahme nach vier Tagen abgeschlossen. Bei Einfamilienhäusern dauert "
             "die Montage typischerweise 2 bis 4 Tage. Dazu kommen vorab Planung, Materialbestellung und die Abstimmung mit dem Netzbetreiber."),
            ("Eignet sich Photovoltaik für ein Mehrparteienhaus?",
             "Ja. Mehrere Haushalte verteilen den Verbrauch über den Tag, das passt gut zu einer Ost-West-Anlage. Ein gemeinsamer Speicher "
             "versorgt das Haus auch am Abend. Wie der Strom auf die Wohneinheiten aufgeteilt wird, klären wir in der Planung, zum Beispiel "
             "über eine gemeinschaftliche Erzeugungsanlage oder eine Energiegemeinschaft."),
            ("Was bringt der 25-kWh-Speicher?",
             "Der Speicher legt den tagsüber erzeugten Sonnenstrom für Abend und Nacht zurück und erhöht so den Anteil des selbst genutzten "
             "Stroms. Zusätzlich dient er als Reserve für die Notstromversorgung der wichtigsten Verbraucher bei Netzausfall."),
        ],
        "related": [
            ("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
            ("/notstrom/", "Notstrom mit Photovoltaik: Ersatzstrom erklärt"),
            ("/photovoltaik-foerderung-kaernten/", "PV-Förderung Kärnten 2026"),
            ("eg_privat", "Energiegemeinschaft: Strom im Haus teilen"),
        ],
        "contact_h": "Mehrparteienhaus, Eigentümergemeinschaft oder Vermietung?",
        "contact_sub": ("Wir planen Dachanlagen mit Speicher für mehrere Wohneinheiten und klären die Stromaufteilung mit. Kostenlos "
                        "und unverbindlich, Montage in Kärnten und der Steiermark."),
        "final_h": "Ein Dach, viele Haushalte, ein Kraftwerk",
        "final_t": "Erzählen Sie uns von Ihrem Haus. Wir melden uns innerhalb eines Werktags.",
    },
]


def path_for(p):
    return f"/referenzen/{p['slug']}/"


def _ergebnis(p):
    ps = "".join(f'<p class="lead">{t}</p>' for t in p["ergebnis"])
    return f"""
  <section class="section" style="background:#fff;border-block:1px solid var(--line)">
    <div class="wrap" style="max-width:820px">
      <p class="eyebrow eg-reveal">Das Ergebnis</p>
      <h2 class="eg-reveal">Ergebnis in Zahlen</h2>
      <div class="eg-reveal" style="max-width:72ch">{ps}</div>
    </div>
  </section>"""


def _footnote():
    return f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte aus den Projektunterlagen dieser Anlage. Jahresertrag, Ersparnis und
      Amortisation hängen von Verbrauch, Strompreis, Ausrichtung und Wetter ab und können bei Ihrer Anlage
      abweichen. Aus Datenschutzgründen nennen wir nur Ort und Gebäudetyp ({STAND}).
      Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>"""


def render(p, rating, count):
    path = path_for(p)
    body = "".join([
        C.hero(
            eyebrow=p["eyebrow"],
            h1=p["titel"],
            lead=p["lead"],
            badges=p["badges"],
            img=p["hero_img"],
            img_alt=p["hero_alt"],
            float_num=rating,
            float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_primary=("kontakt", "Ähnliches Projekt anfragen"),
            cta_secondary=("referenzen", "Alle Referenzen"),
        ),
        C.kpis(p["kpis"]),
        C.facts_panel(
            eyebrow="Eckdaten",
            h2=f"{p['typ']} in {p['ort']}: alle Anlagendaten auf einen Blick",
            intro=("Alle Werte stammen aus den Projektunterlagen dieser Anlage. Richtwerte sind mit Sternchen "
                   "gekennzeichnet und hängen von Verbrauch, Strompreis und Wetter ab."),
            rows=p["eckdaten"],
            actions=[("Ähnliches Projekt anfragen", "/kontakt/", ""), ("Alle Referenzen", "/referenzen/", "")],
        ),
        C.text_block("Ausgangslage", "Die Ausgangslage", p["ausgangslage"], max_w="72ch"),
        C.media_text(
            eyebrow="Die Lösung",
            h2=p["loesung_h2"],
            paragraphs=p["loesung"],
            img=p["loesung_img"],
            alt=p["loesung_alt"],
            bullets=p["komponenten"],
            reverse=True,
        ),
        _ergebnis(p),
    ])
    gal = p.get("galerie") or []
    if len(gal) >= 2:
        body += C.gallery("Bilder", "Das Projekt in Bildern", "Modulfelder, Unterkonstruktion und Kabelführung im Detail.", gal)
    if p.get("kundenstimme"):
        body += C.reviews_block([p["kundenstimme"]])
    body += "".join([
        C.faq_section([(q, f"<p>{ans}</p>") for q, ans in p["faq"]]),
        C.linkgrid_section("Passend zu diesem Projekt", p["related"] + [("referenzen", "Alle 10 Referenzen mit Zahlen")]),
        C.contact_section(headline=p["contact_h"], sub=p["contact_sub"], page_label=f"Referenz: {p['kurz']}"),
        C.finalcta(p["final_h"], p["final_t"], cta=("kontakt", "Ähnliches Projekt anfragen")),
        _footnote(),
    ])
    return page(p["title"], p["desc"], path, body,
                faq_jsonld_str=faq_jsonld(u(path), p["faq"]), og_image=p["hero_img"])


def build():
    rating, count, _reviews = load_reviews()
    errors = []
    for p in PROJEKTE:
        html = render(p, rating, count)
        errors += write_page(f"referenzen/{p['slug']}/index.html", html)
    return errors


if __name__ == "__main__":
    build()
