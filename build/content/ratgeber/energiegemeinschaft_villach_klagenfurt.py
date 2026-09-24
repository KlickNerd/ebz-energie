"""Ratgeber: Energiegemeinschaft Villach und Klagenfurt.

Migriert von ebz-photovoltaik.at/energiegemeinschaft-villach-klagenfurt/ (Stand August 2026),
Inhalt freigegeben, auf die Ratgeber-Vorlage umgestellt. Veraltete Adresse der Quelle durch
die einzig gültige NAP (Triglavstraße 15) ersetzt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "energiegemeinschaft-villach-klagenfurt",
    "path": "/energiegemeinschaft-villach-klagenfurt/",
    "title": "Energiegemeinschaft Villach & Klagenfurt: Strom teilen | EBZ",
    "description": "Energiegemeinschaft in Villach und Klagenfurt: lokal bis 57 % weniger Netzentgelt, Beitritt ohne Lieferantenwechsel, auch ohne eigene PV. EBZ berät vor Ort.",
    "eyebrow": "Energiegemeinschaft · Villach und Klagenfurt",
    "crumb_label": "Energiegemeinschaft Villach und Klagenfurt",
    "h1": "Energiegemeinschaft in Villach und Klagenfurt: bis zu 57 Prozent weniger Netzentgelt, Ihr Strom bleibt in der Stadt",
    "lead": ("EBZ Energie sitzt in der Villacher Triglavstraße und baut mit dem Partner energyfamily die "
             "Energiegemeinschaft für Zentralkärnten auf. So machen Sie mit, als Erzeuger oder als Abnehmer."),
    "chips": [
        "<b>Villach, Klagenfurt</b> und Umland",
        "Lokal: <b>minus 57 %</b> Netzentgelt",
        "Beitritt <b>ohne Lieferantenwechsel</b>",
        "Beratung <b>vor Ort</b>",
    ],
    "date_published": "2026-08-10",
    "date_modified": "2026-09-24",
    "hero_img": "gen_hero",
    "hero_alt": "Photovoltaikanlage auf einem Wohnhausdach in Villach mit Blick über die Stadt",

    "tldr": [
        "In Villach und Klagenfurt ist die Dichte an PV-Anlagen und Abnehmern hoch. Das ist ideal für lokale "
        "Energiegemeinschaften am selben Trafo mit dem vollen Netzentgelt-Abschlag von 57 Prozent.",
        "Sie brauchen keine eigene Anlage: Mieter, Wohnungseigentümer und Betriebe können als Abnehmer beitreten und "
        "günstigen Solarstrom aus der Nachbarschaft beziehen, typisch 120 bis 150 Euro Ersparnis im Jahr*.",
        "Erzeuger mit 10 kWp holen im Beispiel 150 bis 250 Euro Mehrerlös* gegenüber dem OeMAG-Tarif heraus.",
        "EBZ Energie nimmt Sie direkt vor Ort auf, übernimmt die Zählpunktfreigabe bei der Kärnten Netz und rechnet "
        "über energyfamily ab. Start ab dem Folgemonat nach der Anmeldung.",
    ],
    "kpis": [
        ("~4 bis 5 ct", "Netzentgelt-Ersparnis je EG-kWh, lokal*"),
        ("1,5 ct", "Elektrizitätsabgabe entfällt je kWh"),
        ("+4 ct", "Mehrerlös Erzeuger gegenüber OeMAG*"),
        ("0 €", "Wechselkosten, Lieferant bleibt"),
    ],

    "sections": [
        ("Warum Villach und Klagenfurt für Energiegemeinschaften prädestiniert sind", "warum", f"""
<p>Beide Städte haben, was eine Energiegemeinschaft braucht: viele Dächer mit PV, viele Haushalte ohne PV und eine
Netzstruktur, in der ganze Siedlungen an einem Trafo hängen. Im Villacher Stadtgebiet und in den Umlandgemeinden
Wernberg, Finkenstein oder Velden sind in den letzten Jahren hunderte Anlagen entstanden, viele davon von uns gebaut
(siehe {a('pv_villach', 'Photovoltaik in Villach')}). Sie alle speisen mittags Überschuss ein, der im selben Moment
von den Nachbarn aus dem Netz bezogen wird. Die Energiegemeinschaft macht aus dieser zufälligen Gleichzeitigkeit ein
Geschäft zwischen Nachbarn.</p>
<p>Schon im Juni 2024 hat EBZ-Gründer Mario Zintl in einem Interview mit Villach im Fokus angekündigt, eine
Energiegemeinschaft mit einem attraktiven Cent-Preis für Einspeiser und Abnehmer anzubieten. Seit 2026 ist diese
Leistung mit unserem Abrechnungspartner energyfamily verfügbar.</p>
{A.net([
    ("☀", "PV-Erzeuger", "speist den Überschuss tagsüber ins Ortsnetz ein"),
    ("◎", "Smart Meter", "misst Viertelstundenwerte, die Kärnten Netz ordnet zu"),
    ("⌂", "Abnehmer in der Nähe", "Haushalte, Betriebe, Gemeinde beziehen mit reduziertem Netzentgelt"),
    ("€", "Rest wie gewohnt", "nicht zugeordnete Mengen laufen über OeMAG und Lieferant"),
], "Abrechnung über die Plattform",
   "Der EG-Strom wird zum vereinbarten Preis abgerechnet (bei EBZ über energyfamily). Physisch fließt der Strom "
   "wie bisher durchs Netz, neu ist nur die Zuordnung per Smart Meter.")}
"""),
        ("Was Sie in Villach und Klagenfurt konkret sparen", "ersparnis", f"""
<p>Der Hebel liegt in der Netzebene. Wer mit den anderen Teilnehmern am selben Trafo hängt, zahlt für den EG-Strom
57 Prozent weniger Netznutzungs- und Netzverlustentgelt und keine Elektrizitätsabgabe. In dicht bebauten Stadtteilen
wie Villach-Lind, Völkendorf, Landskron oder in Klagenfurt-Waidmannsdorf, Viktring und St. Peter ist diese
Konstellation häufig. In den Umlandgemeinden geht es meist auf die regionale Ebene (selbes Umspannwerk, minus
28 Prozent), was immer noch deutlich besser ist als der Normaltarif. Die Details je Position stehen im Artikel
{a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft und Netzkosten')}.</p>
{A.table(
    ["Rolle", "Annahmen*", "Vorteil im Jahr*"],
    [
        ["Abnehmer ohne PV", "3.500 kWh Verbrauch, 40 % aus der Gemeinschaft, 14 ct EG-Preis statt 17 ct Lieferant, "
         "plus Netz- und Abgabenersparnis", "rund 120 bis 150 €"],
        ["Erzeuger mit 10 kWp", "Überschuss zum EG-Preis statt zum OeMAG-Tarif von 6,146 ct (Juli 2026)",
         "150 bis 250 € Mehrerlös"],
    ],
    hl_cols=(2,),
)}
<p>Die genauen Werte hängen von den Tarifen der jeweiligen Gemeinschaft ab, rechnen Sie es im
{a('eg_rechner', 'EG-Rechner')} mit Ihren Daten durch.</p>
<p><small>*Beispielkonditionen: EG-Einspeisung 10 Cent, EG-Bezug 14 Cent je kWh, Netzentgelt-Richtwerte 2026. Jede
Gemeinschaft legt ihre Preise selbst fest, die Konditionen nennen wir im Erstgespräch.</small></p>
"""),
        ("Mitmachen ohne eigene PV-Anlage", "ohne-pv", f"""
<p>Das wird oft übersehen: Eine Energiegemeinschaft braucht Abnehmer, sonst bleibt der Überschuss im Netz. Wenn Sie in
Villach oder Klagenfurt zur Miete wohnen, eine Eigentumswohnung ohne Dachzugang haben oder einen Betrieb mit
Tagesverbrauch führen, sind Sie für jede Gemeinschaft ein wertvolles Mitglied. Sie bekommen günstigeren Strom aus
der Nachbarschaft, der Erzeuger bekommt mehr als von der OeMAG, und beide sparen Netzentgelt. Den Ablauf für
Abnehmer beschreibt unser Artikel {a('/energiegemeinschaft-beitreten/', 'Energiegemeinschaft beitreten')}.</p>
{A.box("Sie brauchen nur einen eigenen Zählpunkt und einen Smart Meter mit Viertelstundenwerten. Ihr "
       "Lieferantenvertrag, egal ob Kelag oder ein anderer Anbieter, bleibt unverändert.", label="Voraussetzung:")}
"""),
        ("Der Ablauf mit EBZ vor Ort", "ablauf", f"""
{A.steps([
    ("Anfrage mit Postleitzahl",
     "Per Telefon, Formular oder Chat. Wir prüfen anhand Ihrer Zählpunktnummer, welchem Trafo und Umspannwerk Ihr "
     "Anschluss zugeordnet ist."),
    ("Gespräch in Villach oder bei Ihnen",
     "Wir besprechen Ihre Rolle (Erzeuger, Abnehmer oder beides), die Preise der Gemeinschaft und die "
     "Kündigungsbedingungen."),
    ("Zählpunktfreigabe",
     "Im Kundenportal der Kärnten Netz geben Sie die Viertelstundenwerte für die Gemeinschaft frei. Wir zeigen Ihnen "
     "die Klicks."),
    ("Start im Folgemonat",
     "Nach der Anmeldung im EDA-Portal wird Ihr Strom ab dem nächsten Monatsersten zugeordnet. Die Abrechnung sehen "
     "Sie in der energyfamily-App."),
])}
{A.cta("Energiegemeinschaft Villach und Klagenfurt: Platz sichern",
       "Lokale Gemeinschaften sind durch den Trafo begrenzt. Je früher Sie Ihren Zählpunkt anmelden, desto sicherer "
       "ist Ihr Platz in der passenden Gemeinschaft.",
       secondary=("eg_rechner", "Ersparnis berechnen"))}
"""),
        ("Für Betriebe, Hausverwaltungen und Gemeinden rund um Villach", "gewerbe", f"""
<p>Gewerbebetriebe mit großen Dächern in den Gewerbegebieten von Villach-Süd, St. Magdalen, Klagenfurt-Ost oder
entlang der Südautobahn sind die idealen Erzeuger für eine Energiegemeinschaft: hoher Ertrag, tagsüber selbst
Verbrauch, am Wochenende Überschuss für die Nachbarschaft. Hausverwaltungen können Mehrparteienhäuser als
gemeinschaftliche Erzeugungsanlage organisieren und zusätzlich an einer EEG teilnehmen. Gemeinden im Bezirk
Villach-Land und Klagenfurt-Land nutzen Gemeinschaften, um Schulen, Kläranlagen und Bauhöfe mit Bürgerstrom zu
versorgen. Für diese Fälle haben wir eine eigene Seite:
{a('eg_gewerbe', 'Energiegemeinschaft für Gewerbe und Gemeinden')}.</p>
"""),
        ("Fazit: Energiegemeinschaft Villach und Klagenfurt", "fazit", f"""
<p>In Zentralkärnten stimmen alle Voraussetzungen: Sonne, Dichte, Netzstruktur und ein Fachbetrieb vor Ort, der
Anlage und Gemeinschaft aus einer Hand liefert. Ob Sie einspeisen oder beziehen wollen, der Einstieg dauert wenige
Wochen und kostet nichts außer zehn Minuten für die Zählpunktfreigabe. Den Überblick für das ganze Bundesland gibt
der Artikel {a('/energiegemeinschaft-kaernten/', 'Energiegemeinschaft Kärnten')}.</p>
{A.cta("Wir sind in der Triglavstraße 15, 9500 Villach",
       "Rufen Sie an oder kommen Sie vorbei. Wir zeigen Ihnen an Ihrem Zählpunkt, welche Gemeinschaft für Sie passt.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("eg_privat", "Zur Energiegemeinschaft mit EBZ"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner vor Ort in Villach: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und Wallboxen in "
                 "Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. Dazu kommt "
                 "die Energiegemeinschaft: Wir nehmen Sie in eine bestehende Gemeinschaft auf oder bauen mit Ihnen eine "
                 "eigene auf, abgerechnet über die Plattform unseres Partners energyfamily. Direkt betreut: Villach, "
                 "Klagenfurt, Velden, Wernberg, Finkenstein, Arnoldstein, Feldkirchen, Moosburg, Maria Saal, "
                 "Grafenstein und das gesamte Umland."),
        "grid": [
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EG-Anbindung vom selben Team."),
            ("Vor Ort in Villach", "Gespräch im Büro oder bei Ihnen zu Hause, Montage in ganz Kärnten."),
            ("Abrechnung inklusive", "Zählpunktfreigabe, Aufnahme und monatliche Abrechnung über energyfamily."),
            ("Kostenlose Erstberatung", "Wir prüfen Netzebene, Eignung und Ihr Einsparpotenzial."),
        ],
    },

    "faq": [
        ("Gibt es in Villach bereits eine Energiegemeinschaft von EBZ?",
         "EBZ Energie baut seit 2026 gemeinsam mit energyfamily Energiegemeinschaften in Villach, Klagenfurt und dem "
         "Umland auf. Ob an Ihrem Trafo bereits eine Gemeinschaft aktiv ist oder gerade entsteht, prüfen wir anhand "
         "Ihrer Zählpunktnummer."),
        ("Kann ich als Mieter in Klagenfurt mitmachen?",
         "Ja. Sie brauchen nur einen eigenen Zählpunkt mit Smart Meter. Als Abnehmer beziehen Sie den Anteil Ihres "
         "Stroms, der zeitgleich in der Gemeinschaft erzeugt wird, zum EG-Preis und sparen Netzentgelt und Abgaben, "
         "im Beispiel rund 120 bis 150 Euro im Jahr."),
        ("Welche Stadtteile von Villach liegen im selben Nahbereich?",
         "Das lässt sich nicht pauschal sagen, weil der Nahbereich am Trafo und am Umspannwerk hängt, nicht an der "
         "Stadtteilgrenze. Die Kärnten Netz ordnet jeden Zählpunkt bei der Anmeldung zu. Wir übernehmen diese Abfrage "
         "für Sie."),
        ("Was kostet die Teilnahme bei EBZ?",
         "Die Konditionen nennen wir im Erstgespräch transparent, bevor Sie unterschreiben. Üblich sind ein kleiner "
         "monatlicher Beitrag für Abrechnung und Plattform (im Rechner-Beispiel 4 Euro*), keine Einrichtungsgebühr."),
        ("Muss ich meinen Stromlieferanten in Kärnten wechseln?",
         "Nein. Ihr bestehender Vertrag, egal ob Kelag oder ein anderer Anbieter, bleibt unverändert. Die Gemeinschaft "
         "deckt nur den zeitgleich erzeugten Anteil."),
        ("Wie lange dauert es bis zum Start?",
         "Nach der Zählpunktfreigabe und der Anmeldung im EDA-Portal wird Ihr Strom ab dem nächsten Monatsersten "
         "zugeordnet. Vom Erstgespräch bis zur ersten zugeordneten Kilowattstunde vergehen in der Regel vier bis acht "
         "Wochen."),
        ("Kann ich Strom mit Verwandten außerhalb von Villach teilen?",
         "Ja, über eine Bürgerenergiegemeinschaft funktioniert das österreichweit, zum Beispiel mit der Familie in "
         "Wien. Der Netzentgelt-Abschlag von 57 oder 28 Prozent gilt dann nicht, weil er an den Nahbereich gebunden "
         "ist. EBZ bietet beide Varianten an."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und errichtet Photovoltaik-, "
                    "Speicher- und Wärmepumpensysteme in Kärnten und der Steiermark und begleitet Kunden beim Einstieg "
                    "in Energiegemeinschaften. Inhalte werden regelmäßig anhand der Vorgaben von E-Control, OeMAG und "
                    "energiegemeinschaften.gv.at aktualisiert. Keine Rechts- oder Steuerberatung."),
    "sources": [
        ("Villach im Fokus: Interview mit Mario Zintl (2024)",
         "https://www.villachimfokus.at/photovoltaik-immer-mehr-werden-zum-selbstversorger/"),
        ("E-Control: Energiegemeinschaften", "https://www.e-control.at/energiegemeinschaften"),
        ("energiegemeinschaften.gv.at: FAQs", "https://energiegemeinschaften.gv.at/faqs/"),
    ],
    "related": [
        ("/energiegemeinschaft-kaernten/", "Energiegemeinschaft Kärnten: Überblick"),
        ("/energiegemeinschaft-beitreten/", "Energiegemeinschaft beitreten"),
        ("pv_villach", "Photovoltaik in Villach"),
        ("eg_gewerbe", "Energiegemeinschaft für Gewerbe und Gemeinden"),
    ],
    "cta": {
        "h3": "Platz an Ihrem Trafo sichern",
        "text": "Zählpunktnummer schicken, Nahbereich prüfen lassen, ab dem Folgemonat mitmachen.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihr Strom bleibt in Villach und Klagenfurt",
    "final_text": ("Kostenlose Erstberatung in der Triglavstraße 15 oder bei Ihnen zu Hause. Wir zeigen Ihnen an "
                   "Ihrem Zählpunkt, welche Gemeinschaft passt."),
}
