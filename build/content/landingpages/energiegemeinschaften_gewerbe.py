"""Ads-Landingpage Energiegemeinschaft fuer Betriebe und Gemeinden (alte WP-Seite /energiegemeinschaften-gewerbe/).

Die alte LP war die Gewerbe-Leistungsseite Energiegemeinschaft im EBZ-Design mit eingebettetem EG-Rechner. Die neue
LP nimmt deshalb den Inhalt von pages/eg_gewerbe.py im LP-Modus (noindex, ohne Menue, ohne Linkliste, Rechner nach
dem Ablauf).
"""

LP = {
    "path": "/energiegemeinschaften-gewerbe/",
    "source": "eg_gewerbe",
    "title": "Energiegemeinschaft für Betriebe und Gemeinden | EBZ",
    "description": ("Energiegemeinschaft für Gewerbe, Landwirtschaft, Gemeinden und Hausverwaltungen: EBZ plant Anlage "
                    "und Gemeinschaft aus einer Hand, Netzanmeldung inklusive."),
    "rechner": "Energiegemeinschaft-Rechner: Was bringt die Gemeinschaft Ihrem Betrieb?",
    "rechner_intro": ("Überschuss, Netzbezug und Nahbereich eingeben, Vorteil pro Jahr ablesen. Beispielwerte sind "
                      "änderbar, die echten Konditionen legt jede Gemeinschaft fest."),
}
