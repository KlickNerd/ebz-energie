"""Ads-Landingpage Energiegemeinschaft privat (alte WP-Seite /energiegemeinschaften/, Stand September 2026).

Botschaft der alten LP uebernommen (Solarstrom clever teilen, von Nachbarn fuer Nachbarn, Erzeuger und Abnehmer,
Netzentgelt-Rabatt, Abgaben entfallen, Lieferant bleibt, Abrechnung ueber energyfamily, 4 Schritte).
Korrigiert: Erloesvergleich mit OeMAG Juli 2026 (6,146 ct, "Sie koennen nur gewinnen", "8 bis 12 ct statt 6,1 ct")
-> ehrlich mit dem schwankenden Marktpreis (September 2026: 10,168 ct), EG-Preis als planbarer Vorteil wie auf
eg_privat.py; Richtwerte "+150 bis 300 €" / "+80 bis 200 €" aus dem Rechner gestrichen (Beispielkonditionen);
"nur Kaernten und Steiermark" -> Energiegemeinschaft oesterreichweit, Rabatt nur im Nahbereich; Foerderbetraege
(EAG, Kaernten, 125 € je kWp Steiermark) gestrichen; Bewertung 5,0 -> 4,9 (kommt aus den Reviews); eingebetteter
Rechner -> Link auf den EG-Rechner. Leere H1 der alten Seite durch das Anzeigenversprechen ersetzt.
"""

from common import a

LP = {
    "path": "/energiegemeinschaften/",
    "title": "Energiegemeinschaft: Solarstrom clever teilen | EBZ Energie",
    "description": ("Energiegemeinschaft mit EBZ: PV-Überschuss an Nachbarn verkaufen oder Solarstrom aus der Region "
                    "beziehen, bis zu 57 % weniger Netzentgelt im Nahbereich."),
    "eyebrow": "Energiegemeinschaft für Privathaushalte",
    "h1": "Energiegemeinschaft mit EBZ: Solarstrom clever teilen, von Nachbarn für Nachbarn",
    "lead": ("Mit PV-Anlage verkaufen Sie Ihren Überschuss zu einem fix vereinbarten Preis an Haushalte in der Nähe, "
             "statt zum monatlich schwankenden OeMAG-Marktpreis. Ohne Anlage beziehen Sie Solarstrom aus der "
             "Nachbarschaft und zahlen im Nahbereich bis zu 57 % weniger Netzentgelt. EBZ prüft Ihren Anschluss und "
             "erledigt die Schritte beim Netzbetreiber."),
    "badges": [("bis zu 57 %", "weniger Netzentgelt im Nahbereich"), ("Kein Wechsel", "Lieferant bleibt"), ("4 bis 8 Wochen", "bis zum Start")],
    "hero_img": "eg_drohne",
    "hero_alt": "Luftaufnahme eines Dorfes zwischen Feldern und Wald, Nachbarschaft für eine lokale Energiegemeinschaft",
    "cta": "Eignung prüfen lassen",
    "problem": {
        "eyebrow": "Was ist eine Energiegemeinschaft?",
        "h2": "Strom von Nachbarn für Nachbarn, abgerechnet zu vereinbarten Preisen",
        "paragraphs": [
            ("In einer Energiegemeinschaft teilen Haushalte, Betriebe und Gemeinden Solarstrom über das öffentliche "
             "Netz. Der Smart Meter misst viertelstundengenau, der Netzbetreiber ordnet zu, und die Gemeinschaft rechnet "
             "zum vereinbarten Preis ab. Der Strom fließt physisch wie bisher, neu sind nur Zuordnung und Preis."),
            ("Für Ihren Überschuss bekommen Sie bisher den OeMAG-Marktpreis, der monatlich schwankt: 6,146 Cent im Juli, "
             "10,168 Cent im September 2026. In der Gemeinschaft gilt ein fix vereinbarter Preis, und wer im Nahbereich "
             "bezieht, zahlt weniger Netzentgelt und keine Elektrizitätsabgabe. Teilen geht auch österreichweit, etwa "
             "mit Verwandten in Wien, dann über eine Bürgerenergiegemeinschaft ohne Netzentgelt-Rabatt."),
        ],
    },
    "benefits": {
        "eyebrow": "Ihre Vorteile",
        "h2": "Sechs Gründe für die Energiegemeinschaft",
        "intro": ("Mit oder ohne PV-Anlage: Sie profitieren als Erzeuger und als Abnehmer. Was es in Ihrem Fall bringt, "
                  "rechnen Sie mit unserem " + a("eg_rechner", "Energiegemeinschaft-Rechner") + " mit eigenen Zahlen."),
        "cards": [
            ("☀", "Planbarer Preis für Ihren Überschuss",
             "Statt des schwankenden OeMAG-Marktpreises gilt ein fix vereinbarter EG-Preis, typisch 8 bis 12 ct.* Was die Gemeinschaft nicht abnimmt, geht weiter an die OeMAG."),
            ("◇", "Bis zu 57 % weniger Netzentgelt",
             "Auf EG-Strom sinkt das Netzentgelt um 57 % (lokal) oder 28 % (regional). Der Rabatt gilt nur im Nahbereich, nicht beim österreichweiten Teilen."),
            ("€", "Abgaben entfallen",
             "Elektrizitätsabgabe (1,5 ct je kWh) und Erneuerbaren-Förderbeitrag fallen in der lokalen oder regionalen Gemeinschaft auf EG-Strom weg."),
            ("⌂", "Kein Wechsel, kein Risiko",
             "Lieferant und OeMAG-Vertrag bleiben bestehen. Keine Einrichtungsgebühr, kurze Kündigungsfrist."),
            ("◉", "Abrechnung per App",
             "Über die Plattform unseres Partners energyfamily sehen Sie monatlich, was Sie geliefert oder bezogen haben. Gutschrift und Rechnung laufen automatisch."),
            ("⌖", "Strom bleibt in der Region",
             "Ihr Sonnenstrom versorgt Nachbarn, Schule oder den Betrieb nebenan, statt anonym an der Börse zu landen."),
        ],
    },
    "quote": ("Der Marktpreis sprang heuer zwischen sechs und zehn Cent. In der Energiegemeinschaft bleibt der Strom im "
              "Ort, der Preis ist planbar, und der Mehrwert bleibt bei Ihnen und Ihren Nachbarn."),
    "steps": {
        "eyebrow": "So einfach geht es",
        "h2": "In 4 Schritten zur ersten EG-Kilowattstunde",
        "steps": [
            ("Eignung prüfen", "Sie nennen uns PLZ, Zählpunktnummer, PV-Leistung und Verbrauch. Wir prüfen beim Netzbetreiber, ob eine lokale oder regionale Gemeinschaft passt.", "1 Werktag"),
            ("Konditionen und Vertrag", "Einspeise- und Bezugspreis, Beitrag und Kündigungsfrist erhalten Sie schwarz auf weiß. Erst dann unterschreiben Sie.", "Ihr Tempo"),
            ("Zählpunkt freigeben", "Im Kundenportal Ihres Netzbetreibers bestätigen Sie die Teilnahme und aktivieren die Viertelstundenwerte. Wir zeigen Ihnen die Klicks.", "10 Minuten"),
            ("Start und Abrechnung", "Ab dem Folgemonat wird Ihr Strom zugeordnet. In der energyfamily-App sehen Sie monatlich, was Sie geliefert oder bezogen haben.", "ab Monatserstem"),
        ],
    },
    "why": {
        "eyebrow": "Ihr Partner vor Ort",
        "h2": "Warum EBZ der richtige Partner für Ihre Energiegemeinschaft ist",
        "items": [
            ("⌂", "Regional verankert", "Sitz in Villach, Montage und Betreuung in Kärnten und der Steiermark. Ansprechpartner statt Hotline."),
            ("☀", "Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und Energiegemeinschaft mit zertifizierten Fachkräften und einem festen Ansprechpartner."),
            ("▮", "Anlage auf die EG abgestimmt", "Auslegung, Speicher und Energiemanagement sorgen dafür, dass Ihr Überschuss dann anfällt, wenn die Gemeinschaft ihn braucht."),
            ("◎", "Netzbetreiber-Prozesse inklusive", "Nahbereichsabfrage, Zählpunktfreigabe und Anmeldung über das EDA-Portal erledigen wir mit Ihnen."),
            ("✓", "Abrechnung über energyfamily", "Österreichische Plattform mit rund 330 Gemeinschaften und rund 15.000 Nutzern, monatliche Abrechnung mit App."),
            ("€", "Ehrliche Zahlen", "Wir rechnen mit dem aktuellen OeMAG-Marktpreis. Was sich nicht rechnet, empfehlen wir nicht."),
        ],
    },
    "contact": {
        "h2": "Eignung für die Energiegemeinschaft prüfen",
        "sub": ("Schicken Sie uns Ihre PLZ und, falls vorhanden, Ihre Zählpunktnummer. Wir sagen Ihnen innerhalb eines "
                "Werktags, welche Gemeinschaft infrage kommt und was sie bringt, ehrlich gerechnet und ohne Verkaufsdruck."),
    },
    "faq": [
        ("Brauche ich eine eigene PV-Anlage, um mitzumachen?",
         "Nein. Abnehmer ohne Anlage sind für jede Gemeinschaft wichtig. Sie brauchen nur einen eigenen Zählpunkt mit "
         "Smart Meter und beziehen den zeitgleich erzeugten Anteil zum EG-Preis, im Nahbereich mit reduziertem "
         "Netzentgelt und ohne Elektrizitätsabgabe."),
        ("Muss ich meinen Stromlieferanten wechseln?",
         "Nein. Ihr Lieferantenvertrag bleibt unverändert. Die Gemeinschaft deckt nur den Anteil, der zeitgleich von "
         "Mitgliedern erzeugt wird. Den Rest liefert weiterhin Ihr bisheriger Anbieter."),
        ("Was bekomme ich als Erzeuger für meinen Überschuss?",
         "Den mit der Gemeinschaft fix vereinbarten Einspeisepreis. Der OeMAG-Marktpreis schwankt monatlich (Juli 2026: "
         "6,146 Cent, September 2026: 10,168 Cent), ob der EG-Preis darüber liegt, hängt vom Monat ab. Dazu kommt Ihr "
         "Vorteil als Abnehmer am Abend und im Winter. Was nicht in der Gemeinschaft verbraucht wird, geht weiter an die "
         "OeMAG. Mit eigenen Zahlen rechnen: " + a("eg_rechner", "Energiegemeinschaft-Rechner") + "."),
        ("Kann ich Strom auch österreichweit teilen, etwa mit Verwandten?",
         "Ja. EBZ bietet Energiegemeinschaften österreichweit an. Mit den Nachbarn im Nahbereich gibt es den "
         "Netzentgelt-Rabatt von bis zu 57 % (lokal) oder 28 % (regional). Teilen Sie mit der Tante in Wien, läuft das "
         "über eine Bürgerenergiegemeinschaft ohne Netzentgelt-Rabatt."),
        ("Wie lange dauert es bis zum Start?",
         "Vom Erstgespräch bis zur ersten zugeordneten Kilowattstunde in der Regel 4 bis 8 Wochen. Der Start erfolgt "
         "immer zum Monatsersten nach Freigabe durch den Netzbetreiber."),
        ("Was kostet die Teilnahme und kann ich wieder austreten?",
         "Üblich ist ein Beitrag von 2 bis 8 € je Monat für Plattform und Abrechnung, keine Einrichtungsgebühr. Die "
         "genauen Konditionen erfahren Sie, bevor Sie unterschreiben. Austreten können Sie mit kurzer Kündigungsfrist, "
         "Ihr Lieferantenvertrag läuft unverändert weiter."),
        ("Was macht energyfamily und was macht EBZ?",
         "EBZ ist Ihr Ansprechpartner: Beratung, Prüfung des Nahbereichs, Anlage, Speicher, Energiemanagement und die "
         "Aufnahme in die Gemeinschaft. energyfamily stellt die Plattform für Verwaltung und monatliche Abrechnung "
         "bereit, inklusive App."),
    ],
    "finalcta": {
        "h2": "Ihr Überschuss hat Nachbarn verdient",
        "text": "Ob Erzeuger oder Abnehmer: Wir zeigen Ihnen kostenlos und ehrlich, was die Energiegemeinschaft in Ihrem Fall bringt.",
    },
    "footnote": ("*Beispielkonditionen: Jede Gemeinschaft legt ihre Preise selbst fest, die Konditionen von EBZ nennen "
                 "wir im Erstgespräch. OeMAG-Marktpreis laut oem-ag.at, Stand Oktober 2026. Netzentgelt-Rabatt und "
                 "Abgabenbefreiung gelten nur für die zugeordnete Menge und nur im Nahbereich (lokal 57 %, regional 28 %). "
                 "Keine Garantie, keine Steuerberatung."),
}
