"""Ads-Landingpage Energiegemeinschaft privat (alte WP-Seite /energiegemeinschaften/, WordPress-ID 6946).

Die alte LP war die Leistungsseite Energiegemeinschaft im EBZ-Design mit eingebettetem EG-Rechner. Die neue LP
nimmt deshalb den Inhalt von pages/eg_privat.py (eine Quelle, kein doppelter Text) im LP-Modus: noindex, ohne Menue,
Ratgeber-Linkliste entfernt, Buttons springen zum Formular, Rechner nach dem Ablauf wie auf der alten LP.
"""

LP = {
    "path": "/energiegemeinschaften/",
    "source": "eg_privat",
    "title": "Energiegemeinschaft: Solarstrom clever teilen | EBZ Energie",
    "description": ("Energiegemeinschaft mit EBZ: PV-Überschuss an Nachbarn verkaufen oder Solarstrom aus der Region "
                    "beziehen, bis zu 57 % weniger Netzentgelt im Nahbereich."),
    "rechner": "Energiegemeinschaft-Rechner: Was bringt Ihnen die Gemeinschaft?",
    "rechner_intro": ("Überschuss, Netzbezug und Nahbereich eingeben, Vorteil pro Jahr ablesen. Beispielwerte sind "
                      "änderbar, die echten Konditionen legt jede Gemeinschaft fest."),
}
