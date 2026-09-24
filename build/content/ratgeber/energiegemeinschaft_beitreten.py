"""Ratgeber: Energiegemeinschaft beitreten.

Migriert von ebz-photovoltaik.at/energiegemeinschaft-beitreten/ (Stand August 2026),
Inhalt freigegeben, auf die Ratgeber-Vorlage umgestellt. EG-Preise als Beispielwerte
gekennzeichnet, Hinweis auf österreichweite Bürgerenergiegemeinschaft ergänzt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "energiegemeinschaft-beitreten",
    "path": "/energiegemeinschaft-beitreten/",
    "title": "Energiegemeinschaft beitreten: 4 Schritte, 4 bis 8 Wochen | EBZ",
    "description": ("Energiegemeinschaft beitreten: Voraussetzungen (Zählpunkt, Smart Meter, Nahbereich), Ablauf in "
                    "4 Schritten, Kosten 2 bis 8 € im Monat, Start in 4 bis 8 Wochen. Auch ohne PV-Anlage möglich."),
    "eyebrow": "Energiegemeinschaft · Beitritt",
    "crumb_label": "Energiegemeinschaft beitreten",
    "h1": "Energiegemeinschaft beitreten: In vier Schritten und 4 bis 8 Wochen Mitglied",
    "lead": ("Mit oder ohne eigene PV-Anlage: Der Beitritt zu einer bestehenden Energiegemeinschaft ist der "
             "schnellste Weg zu günstigem Regionalstrom. Was Sie brauchen, wie lange es dauert, was es kostet."),
    "chips": [
        "<b>Ohne PV-Anlage</b> möglich",
        "Smart Meter mit <b>15-min-Werten</b>",
        "<b>4 bis 8 Wochen</b> bis zum Start",
        "Kündbar <b>monatlich bis quartalsweise</b>",
    ],
    "date_published": "2026-08-10",
    "date_modified": "2026-09-24",
    "hero_img": "team_quer",
    "hero_alt": "Team von EBZ Energie berät zum Beitritt in eine Energiegemeinschaft",

    "tldr": [
        "Beitreten kann jeder mit eigenem Zählpunkt und Smart Meter: Hausbesitzer, Mieter, Wohnungseigentümer, "
        "Betriebe, Vereine, Gemeinden. Eine PV-Anlage ist nicht nötig.",
        "Der Ablauf: passende Gemeinschaft im Nahbereich finden, Mitgliedsvertrag unterschreiben, Zählpunkt im "
        "Netzbetreiber-Portal freigeben, Start im Folgemonat. In Summe vier bis acht Wochen.",
        "Abnehmer sparen beim EG-Strom Netzentgelt (28 bis 57 Prozent) und Abgaben, Erzeuger bekommen mehr als den "
        "OeMAG-Tarif von 6,146 Cent (Juli 2026). Der Lieferantenvertrag bleibt bestehen.",
        "Kosten: meist 2 bis 8 Euro Mitgliedsbeitrag im Monat, keine Einrichtungsgebühr, Kündigungsfrist ein bis "
        "drei Monate.",
        "EBZ Energie nimmt Kunden in Kärnten und der Steiermark auf und erledigt die Schritte beim Netzbetreiber mit. "
        "Strom teilen über den Nahbereich hinaus geht österreichweit als Bürgerenergiegemeinschaft.",
    ],
    "kpis": [
        ("11.000+", "Energiegemeinschaften in Österreich"),
        ("4 bis 8 Wochen", "vom Erstgespräch bis zum Start"),
        ("2 bis 8 €", "Mitgliedsbeitrag im Monat, typisch"),
        ("1 bis 3 Monate", "übliche Kündigungsfrist"),
    ],

    "sections": [
        ("Beitreten oder gründen? Die schnelle Entscheidung", "beitreten-oder-gruenden", f"""
<p>Wer zum ersten Mal über eine Energiegemeinschaft nachdenkt, landet meist bei der Frage, ob er eine gründen muss.
In den allermeisten Fällen lautet die Antwort nein. In Österreich gibt es mittlerweile über 11.000
Energiegemeinschaften, davon mehr als 5.500 Erneuerbare-Energie-Gemeinschaften. In Kärnten und der Steiermark
findet sich in fast jedem Umspannwerksbereich eine aktive Gemeinschaft oder eine, die gerade entsteht. Der Beitritt
erspart Ihnen Rechtsform, Vereinsregister, Netzbetreibervertrag und Abrechnungssoftware. Das alles steht schon.</p>
<p>Gründen lohnt sich dann, wenn Sie mehrere Erzeuger und Abnehmer kennen, die an einem Trafo hängen, oder wenn eine
Gemeinde oder ein Betrieb die Gemeinschaft als eigenes Projekt aufsetzen will. Dafür haben wir den Artikel
{a('/energiegemeinschaft-gruenden/', 'Energiegemeinschaft gründen')} geschrieben. Hier geht es um den Beitritt.
Wie eine Gemeinschaft grundsätzlich funktioniert, erklärt der {a('eg', 'Leitartikel zur Energiegemeinschaft')}.</p>
"""),
        ("Voraussetzungen für den Beitritt", "voraussetzungen", f"""
{A.table(
    ["Voraussetzung", "Was das heißt", "So prüfen Sie es"],
    [
        ["Eigener Zählpunkt", "Eine 33-stellige Zählpunktnummer, beginnend mit AT",
         "steht auf der Netzrechnung und im Kundenportal"],
        ["Smart Meter mit Viertelstundenwerten", "Der Zähler muss 15-min-Werte liefern (Opt-in beim Netzbetreiber)",
         "im Kundenportal aktivieren, dauert wenige Tage"],
        ["Nahbereich passt", "Ihr Anschluss liegt am selben Trafo (lokal) oder Umspannwerk (regional) wie die Gemeinschaft",
         "Netzbetreiber ordnet bei Anmeldung zu, EBZ fragt vorab ab"],
        ["Keine Großunternehmen in EEG", "Große Unternehmen dürfen nur in BEG oder P2P, nicht in EEG",
         "gilt für Betriebe ab 250 Mitarbeitern"],
        ["Lieferantenvertrag bleibt", "Sie brauchen weiterhin einen Stromlieferanten für den Rest", "nichts zu tun"],
    ],
)}
{A.box("Der häufigste Stolperstein ist der Smart Meter. Zwar sind in Kärnten und der Steiermark fast alle Haushalte "
       "umgerüstet, aber standardmäßig übermittelt der Zähler nur Tageswerte. Für die Energiegemeinschaft braucht der "
       "Netzbetreiber Viertelstundenwerte, das sogenannte Opt-in. Wer früher ein Opt-out gewählt hat, muss das im "
       "Kundenportal rückgängig machen.")}
<p>Passt der Nahbereich nicht, etwa weil Sie Strom mit Verwandten in einem anderen Bundesland teilen wollen, bleibt
die Bürgerenergiegemeinschaft: Sie funktioniert österreichweit, allerdings ohne den Netzentgelt-Abschlag, der an
den Nahbereich gebunden ist. EBZ bietet beide Varianten an.</p>
"""),
        ("Der Ablauf in vier Schritten", "ablauf", f"""
{A.steps([
    ("Gemeinschaft im Nahbereich finden",
     "Über die Gemeinde, über Plattformen wie energyfamily oder über einen Fachbetrieb, der Gemeinschaften betreut. "
     "Entscheidend ist der Nahbereich, nicht die Entfernung in Kilometern. Wie Sie suchen, steht im Artikel "
     + a('/energiegemeinschaft-finden/', 'Energiegemeinschaft finden') + "."),
    ("Mitgliedsvertrag und Preise",
     "Sie erhalten die Teilnahmebedingungen: Einspeisepreis (falls Sie Erzeuger sind), Bezugspreis, Mitgliedsbeitrag, "
     "Kündigungsfrist, Aufteilungsschlüssel (statisch oder dynamisch). Lesen Sie besonders den Aufteilungsschlüssel, "
     "er bestimmt, wie viel EG-Strom Ihnen zugeordnet wird."),
    ("Zählpunkt freigeben",
     "Im Kundenportal Ihres Netzbetreibers (Kärnten Netz, Energienetze Steiermark, Stromnetz Graz) bestätigen Sie "
     "die Teilnahmeanfrage der Gemeinschaft und die Datenfreigabe. Das ist ein gesetzlich vorgeschriebener Schritt, "
     "die Gemeinschaft kann ihn nicht für Sie erledigen."),
    ("Start und Abrechnung",
     "Nach Bestätigung ordnet der Netzbetreiber ab dem Folgemonat die Energiemengen zu. Die Gemeinschaft rechnet "
     "monatlich oder quartalsweise ab. Der Netzbetreiber stellt die reduzierten Netzentgelte automatisch auf der "
     "Netzrechnung dar."),
])}
{A.net([
    ("☀", "PV-Erzeuger", "speist den Überschuss tagsüber ins Ortsnetz ein"),
    ("◎", "Smart Meter", "misst Viertelstundenwerte, der Netzbetreiber ordnet zu"),
    ("⌂", "Abnehmer in der Nähe", "Haushalte, Betriebe, Gemeinde beziehen mit reduziertem Netzentgelt"),
    ("€", "Rest wie gewohnt", "nicht zugeordnete Mengen laufen über OeMAG und Lieferant"),
], "Abrechnung über die Plattform",
   "Der EG-Strom wird zum vereinbarten Preis abgerechnet (bei EBZ über energyfamily). Physisch fließt der Strom "
   "wie bisher durchs Netz, neu ist nur die Zuordnung per Smart Meter.")}
{A.cta("Beitritt in Kärnten oder der Steiermark: Wir übernehmen die Schritte",
       "EBZ prüft den Nahbereich, aktiviert mit Ihnen die Viertelstundenwerte und meldet den Zählpunkt an. Sie "
       "unterschreiben, wir erledigen den Rest.",
       secondary=("eg_rechner", "Ersparnis berechnen"))}
"""),
        ("Was der Beitritt für Abnehmer bringt", "abnehmer", f"""
<p>Als reiner Stromkunde ohne PV-Anlage profitieren Sie dreifach. Erstens zahlen Sie für den EG-Anteil den
Gemeinschaftspreis, der meist unter dem Arbeitspreis Ihres Lieferanten liegt (im Beispiel unseres Rechners
14 Cent*). Zweitens sparen Sie auf diesen Anteil 28 bis 57 Prozent des Netznutzungs- und Netzverlustentgelts.
Drittens entfallen bei einer Erneuerbaren-Energie-Gemeinschaft die Elektrizitätsabgabe von 1,5 Cent und der
Erneuerbaren-Förderbeitrag. Wie viel EG-Strom Ihnen zugeordnet wird, hängt von Ihrem Verbrauchsprofil ab: Wer
tagsüber verbraucht (Homeoffice, Wärmepumpe, E-Auto am Wochenende) bekommt mehr als ein Haushalt, der nur abends
zuhause ist. Die Rechnung je Position steht im Artikel
{a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft und Netzkosten')}.</p>
"""),
        ("Was der Beitritt für Erzeuger bringt", "erzeuger", f"""
<p>Als PV-Besitzer verkaufen Sie den Überschuss zum EG-Einspeisepreis, typisch zwischen 8 und 12 Cent*, statt zum
OeMAG-Tarif von aktuell 6,146 Cent (Juli 2026). Nur der Anteil, der zeitgleich in der Gemeinschaft verbraucht wird,
bekommt diesen Preis. Der Rest geht weiter an die OeMAG oder Ihren Einspeisevertragspartner. Sie verlieren also nie,
Sie gewinnen nur auf dem zugeordneten Anteil. Gleichzeitig sind Sie abends und im Winter selbst Abnehmer und
profitieren von den Ersparnissen oben. Den Vergleich mit allen Zahlen ziehen wir im Artikel
{a('/oemag-einspeisetarif/', 'OeMAG-Einspeisetarif oder Energiegemeinschaft')}. Ein
{a('batteriespeicher', 'Batteriespeicher')} verschiebt Überschuss zusätzlich in die Abendstunden, in denen die
Gemeinschaft mehr braucht.</p>
<p><small>*Beispielkonditionen aus dem Markt (EG-Einspeisung 10 Cent, EG-Bezug 14 Cent je kWh). Jede Gemeinschaft
legt ihre Preise selbst fest, die Konditionen bei EBZ nennen wir im Erstgespräch.</small></p>
"""),
        ("Kosten, Kündigung und Risiko", "kosten", f"""
<p>Die meisten Gemeinschaften verlangen einen Mitgliedsbeitrag zwischen zwei und acht Euro im Monat oder einen
kleinen Aufschlag je abgerechneter Kilowattstunde. Damit werden Plattform, Abrechnung und Verwaltung finanziert.
Einrichtungsgebühren sind unüblich. Die Kündigungsfristen liegen bei einem bis drei Monaten.</p>
{A.box("Ein wirtschaftliches Risiko besteht nicht, weil der Lieferantenvertrag bestehen bleibt und nicht zugeordnete "
       "Mengen wie bisher abgerechnet werden.", label="Gut zu wissen:")}
<p>Die ehrliche Liste der Einschränkungen finden Sie im Artikel
{a('/energiegemeinschaft-nachteile/', 'Energiegemeinschaft: Nachteile')}. Eine Übersicht der Gebührenmodelle gibt
der Artikel {a('/energiegemeinschaft-kosten/', 'Was eine Energiegemeinschaft kostet')}.</p>
"""),
        ("Fazit: Energiegemeinschaft beitreten", "fazit", f"""
<p>Der Beitritt ist unkompliziert, in wenigen Wochen erledigt und ohne Wechsel des Lieferanten möglich. Entscheidend
sind drei Dinge: der richtige Nahbereich, aktivierte Viertelstundenwerte und ein fairer Aufteilungsschlüssel. Wer das
im Blick hat, spart ab dem ersten Monat. Regionale Details finden Sie in den Artikeln
{a('/energiegemeinschaft-kaernten/', 'Energiegemeinschaft Kärnten')} und
{a('/energiegemeinschaft-steiermark/', 'Energiegemeinschaft Steiermark')}.</p>
{A.cta("In vier Schritten zur Energiegemeinschaft",
       "Erstgespräch, Gemeinschaft wählen, Zählpunkt freigeben, starten. EBZ begleitet Sie in Kärnten und der "
       "Steiermark durch jeden Schritt.",
       primary=("kontakt", "Beitritt anfragen"), secondary=("eg_privat", "Zur Energiegemeinschaft mit EBZ"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für den Beitritt: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und Wallboxen in "
                 "Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. Dazu kommt "
                 "die Energiegemeinschaft: Wir nehmen Sie in eine bestehende Gemeinschaft auf oder bauen mit Ihnen eine "
                 "eigene auf, abgerechnet über die Plattform unseres Partners energyfamily mit rund 330 Gemeinschaften "
                 "und rund 15.000 Nutzern."),
        "grid": [
            ("Nahbereich vorab geprüft", "Wir fragen Trafo und Umspannwerk ab, bevor Sie unterschreiben."),
            ("Viertelstundenwerte aktiviert", "Wir zeigen Ihnen das Opt-in im Kundenportal Ihres Netzbetreibers."),
            ("Abrechnung inklusive", "Zählpunktfreigabe, Aufnahme und monatliche Abrechnung über energyfamily."),
            ("Auch ohne PV-Anlage", "Als Abnehmer beziehen Sie Solarstrom aus der Nachbarschaft."),
        ],
    },

    "faq": [
        ("Kann ich einer Energiegemeinschaft ohne PV-Anlage beitreten?",
         "Ja. Abnehmer sind für jede Gemeinschaft wichtig, weil Überschuss nur dann zum EG-Preis abgerechnet werden "
         "kann, wenn ihn jemand zeitgleich verbraucht. Sie brauchen nur einen eigenen Zählpunkt und einen Smart Meter "
         "mit Viertelstundenwerten."),
        ("Was ist der Unterschied zwischen statischer und dynamischer Aufteilung?",
         "Bei der statischen Aufteilung bekommt jeder Abnehmer einen festen Prozentsatz der Erzeugung zugeordnet, "
         "egal wie viel er gerade verbraucht. Bei der dynamischen Aufteilung wird der Strom nach dem tatsächlichen "
         "Verbrauch in der Viertelstunde verteilt. Dynamisch ist für die meisten Gemeinschaften effizienter."),
        ("Muss ich meinen Stromlieferanten wechseln, wenn ich beitrete?",
         "Nein. Ihr Lieferantenvertrag bleibt unverändert. Die Gemeinschaft liefert nur den zeitgleich erzeugten "
         "Anteil, alles andere kommt weiterhin vom bisherigen Anbieter."),
        ("Wie lange dauert es vom Antrag bis zum Start?",
         "In der Regel vier bis acht Wochen. Der Großteil entfällt auf die Aktivierung der Viertelstundenwerte und "
         "die Zählpunktanmeldung beim Netzbetreiber, die nur zum Monatsersten wirksam wird."),
        ("Was kostet der Beitritt?",
         "Typisch sind zwei bis acht Euro Mitgliedsbeitrag im Monat oder ein kleiner Aufschlag je Kilowattstunde. "
         "Einrichtungsgebühren sind unüblich. Die Kündigungsfrist liegt meist bei einem bis drei Monaten."),
        ("Kann ich in mehreren Energiegemeinschaften gleichzeitig sein?",
         "Ja, die Mehrfachteilnahme erlaubt bis zu fünf Gemeinschaften je Zählpunkt, mit Teilnahmefaktoren, die "
         "festlegen, welcher Anteil in welche Gemeinschaft geht. Für Privathaushalte reicht üblicherweise eine."),
        ("Was passiert, wenn ich umziehe?",
         "Der Zählpunkt gehört zur Adresse. Beim Umzug wird der alte Zählpunkt abgemeldet. Am neuen Wohnort prüfen "
         "Sie, ob die Gemeinschaft dort noch im Nahbereich liegt, sonst treten Sie einer anderen bei."),
        ("Kann ich auch beitreten, wenn die Gemeinschaft nicht in meinem Nahbereich liegt?",
         "Ja, als Bürgerenergiegemeinschaft funktioniert das Stromteilen österreichweit, zum Beispiel mit Verwandten "
         "in einem anderen Bundesland. Der Netzentgelt-Abschlag von 28 bis 57 Prozent gilt dann aber nicht."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und errichtet Photovoltaik-, "
                    "Speicher- und Wärmepumpensysteme in Kärnten und der Steiermark und begleitet Kunden beim Einstieg "
                    "in Energiegemeinschaften. Inhalte werden regelmäßig anhand der Vorgaben von E-Control, OeMAG und "
                    "energiegemeinschaften.gv.at aktualisiert. Keine Rechts- oder Steuerberatung."),
    "sources": [
        ("Koordinationsstelle: Schritte zur Teilnahme", "https://energiegemeinschaften.gv.at/online-guide/"),
        ("E-Control: Energiegemeinschaften", "https://www.e-control.at/energiegemeinschaften"),
        ("energyfamily: Schritte zur Teilnahme", "https://www.energyfamily.at/schritte-zur-teilnahme"),
        ("Koordinationsstelle: FAQs", "https://energiegemeinschaften.gv.at/faqs/"),
    ],
    "related": [
        ("/energiegemeinschaft-finden/", "Energiegemeinschaft finden"),
        ("/energiegemeinschaft-kosten/", "Energiegemeinschaft: Kosten und Abrechnung"),
        ("/energiegemeinschaft-kaernten/", "Energiegemeinschaft Kärnten"),
        ("eg_privat", "Energiegemeinschaft für Private mit Rechner"),
    ],
    "cta": {
        "h3": "Beitritt anfragen",
        "text": "Wir prüfen Nahbereich und Smart Meter und melden Ihren Zählpunkt an. Start ab dem Folgemonat.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "In wenigen Wochen Mitglied einer Energiegemeinschaft",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das die Schritte beim "
                   "Netzbetreiber mit Ihnen erledigt."),
}
