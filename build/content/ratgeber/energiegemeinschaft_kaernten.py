"""Ratgeber: Energiegemeinschaft Kärnten.

Migriert von ebz-photovoltaik.at/energiegemeinschaft-kaernten/ (Stand August 2026),
Inhalt freigegeben, auf die Ratgeber-Vorlage umgestellt. Rechner-/EG-Preise sind
Beispielwerte (Sternchen), Netzentgelt-Abschläge laut E-Control 2026.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "energiegemeinschaft-kaernten",
    "path": "/energiegemeinschaft-kaernten/",
    "title": "Energiegemeinschaft Kärnten: bis 57 % weniger Netzentgelt | EBZ",
    "description": "Energiegemeinschaft in Kärnten: PV-Überschuss an Nachbarn statt für 6,146 ct an die OeMAG. Netzentgelt bis 57 % weniger, Start in 4 bis 8 Wochen. EBZ, Villach.",
    "eyebrow": "Energiegemeinschaft · Kärnten",
    "crumb_label": "Energiegemeinschaft Kärnten",
    "h1": "Energiegemeinschaft in Kärnten: Solarstrom teilen statt für 6 Cent einspeisen",
    "lead": ("Rund 390 Kärntnerinnen und Kärntner suchen jeden Monat nach einer Energiegemeinschaft. "
             "Hier steht, wie sie funktioniert, was sie in Kärnten konkret bringt und wie Sie mit EBZ Energie einsteigen."),
    "chips": [
        "Netzentgelt: <b>bis zu 57 %</b> weniger",
        "Elektrizitätsabgabe: <b>entfällt</b>",
        "OeMAG Juli 2026: <b>6,146 ct/kWh</b>",
        "Start in <b>4 bis 8 Wochen</b>",
    ],
    "date_published": "2026-08-05",
    "date_modified": "2026-09-24",
    "hero_img": "eg_drohne",
    "hero_alt": "Ortschaft in Kärnten aus der Luft mit Photovoltaikanlagen auf mehreren Dächern",

    "tldr": [
        "Eine Energiegemeinschaft (EG) lässt Sie PV-Überschuss zu einem selbst vereinbarten Preis an Haushalte "
        "und Betriebe im Nahbereich verkaufen, statt ihn zum OeMAG-Marktpreis von 6,146 Cent (Juli 2026) abzugeben.",
        "In Kärnten entscheidet das Netz der Kärnten Netz GmbH über den Nahbereich: derselbe Trafo bedeutet lokal "
        "(minus 57 Prozent Netzentgelt), dasselbe Umspannwerk regional (minus 28 Prozent).",
        "Erneuerbare-Energie-Gemeinschaften sind zusätzlich von Elektrizitätsabgabe (1,5 Cent je kWh) und "
        "Erneuerbaren-Förderbeitrag befreit.",
        "Mit rund 1.100 kWh Jahresertrag je kWp liegt Kärnten österreichweit an der Spitze. Eine 10-kWp-Anlage "
        "liefert gut 11.000 kWh, ein Haushalt ohne Speicher nutzt davon nur etwa 30 Prozent selbst.",
        "EBZ Energie aus Villach nimmt Kunden in ganz Kärnten in eine Energiegemeinschaft auf und wickelt "
        "Zählpunktfreigabe und Abrechnung über die Plattform energyfamily ab.",
    ],
    "kpis": [
        ("~1.100 kWh", "Jahresertrag je kWp in Kärnten"),
        ("6,146 ct", "OeMAG-Marktpreis Juli 2026 je kWh"),
        ("57 %", "Netzentgelt-Abschlag lokal (Arbeitspreis)"),
        ("8 bis 12 ct", "typischer EG-Einspeisepreis*"),
    ],

    "sections": [
        ("Was eine Energiegemeinschaft in Kärnten konkret ist", "was-ist", f"""
<p>Eine Energiegemeinschaft ist ein Zusammenschluss von mindestens zwei Teilnehmern, die Strom aus erneuerbaren
Quellen gemeinsam erzeugen, teilen und verbrauchen. Rechtsgrundlage ist seit 2021 das Erneuerbaren-Ausbau-Gesetz,
ab 1. Oktober 2026 übernimmt das neue Elektrizitätswirtschaftsgesetz (ElWG) die Regeln. Für Sie als Hausbesitzer in
Kärnten bedeutet das: Der Strom, den Ihre {a('photovoltaik', 'PV-Anlage')} mittags zu viel produziert, geht nicht
mehr nur an die OeMAG oder Ihren Lieferanten, sondern an Nachbarn, Betriebe oder die Gemeinde im selben Netzgebiet.
Zu einem Preis, den die Gemeinschaft selbst festlegt.</p>
<p>Die physikalische Seite ändert sich dabei nicht. Der Strom fließt weiter über das Ortsnetz, der Smart Meter misst
viertelstundengenau, und der Netzbetreiber rechnet aus, welcher Anteil Ihres Überschusses innerhalb der Gemeinschaft
verbraucht wurde. Nur dieser Anteil wird zum EG-Preis abgerechnet. Was übrig bleibt, geht wie bisher an die OeMAG
oder den Einspeisevertrag.</p>
{A.net([
    ("☀", "PV-Erzeuger", "speist den Überschuss tagsüber ins Ortsnetz ein"),
    ("◎", "Smart Meter", "misst Viertelstundenwerte, der Netzbetreiber ordnet zu"),
    ("⌂", "Abnehmer in der Nähe", "Haushalte, Betriebe, Gemeinde beziehen mit reduziertem Netzentgelt"),
    ("€", "Rest wie gewohnt", "nicht zugeordnete Mengen laufen über OeMAG und Lieferant"),
], "Abrechnung über die Plattform",
   "Der EG-Strom wird zum vereinbarten Preis abgerechnet (bei EBZ über energyfamily). Physisch fließt der Strom "
   "wie bisher, neu ist nur die Zuordnung per Smart Meter.")}
<p>Wenn Sie das Grundprinzip genauer nachlesen wollen, erklärt unser {a('eg', 'Leitartikel zur Energiegemeinschaft')}
die drei Modelle EEG, BEG und GEA im Detail. Hier konzentrieren wir uns auf das, was in Kärnten speziell ist.</p>
"""),
        ("Warum sich das Thema gerade in Kärnten rechnet", "warum-kaernten", f"""
<p>Drei Faktoren kommen in Kärnten zusammen. Erstens die Sonne: Mit rund 1.050 bis 1.150 Kilowattstunden Ertrag pro
installiertem Kilowattpeak liegt Kärnten österreichweit an der Spitze, das Klagenfurter Becken und das Lavanttal noch
etwas darüber. Eine 10-kWp-Anlage liefert also gut 11.000 kWh im Jahr, von denen ein Einfamilienhaus ohne Speicher
nur etwa 30 Prozent selbst verbraucht.</p>
<p>Zweitens der Einspeisetarif: Der OeMAG-Marktpreis lag im Juli 2026 bei 6,146 Cent pro Kilowattstunde, das ist die
gesetzliche Untergrenze, und die Tendenz zeigt seit Monaten nach unten (aktuelle Werte in unserem
{a('marktpreis', 'Marktpreis-Überblick')}). Drittens die Netzstruktur: Kärnten ist kleinteilig besiedelt, viele
Ortschaften hängen an einem gemeinsamen Trafo. Das erleichtert lokale Energiegemeinschaften mit dem vollen
Netzentgelt-Abschlag.</p>
{A.box("7.000 kWh Überschuss, davon landen 60 Prozent in der Gemeinschaft, zu 10 statt 6 Cent*: Das sind 168 Euro "
       "mehr im Jahr auf der Einspeiseseite. Dazu kommt die Bezugsseite, denn in den Abend- und Winterstunden sind "
       "Sie selbst Abnehmer und sparen beim EG-Strom Netzentgelt und Abgaben.", label="Grob durchgerechnet:")}
<p>Unser {a('eg_rechner', 'Energiegemeinschaft-Rechner')} rechnet das mit Ihren Werten durch.</p>
<p><small>*Beispielkonditionen: EG-Einspeisepreis 10 Cent, EG-Bezugspreis 14 Cent je kWh. Jede Gemeinschaft legt
ihre Preise selbst fest, die tatsächlichen Konditionen nennen wir im Erstgespräch.</small></p>
"""),
        ("Netzgebiet, Nahbereich und Kärnten Netz", "nahbereich", f"""
<p>Ob eine Energiegemeinschaft in Ihrer Gemeinde lokal oder regional ist, entscheidet nicht die Postleitzahl, sondern
der Netzanschluss. In Kärnten betreibt die Kärnten Netz GmbH, eine Tochter der Kelag, den Großteil des Verteilnetzes.
Wer an derselben Trafostation hängt, bildet den Lokalbereich, wer am selben Umspannwerk hängt, den Regionalbereich.
Der Unterschied ist bares Geld: Der Abschlag gilt auf den Arbeitspreis des Netznutzungs- und Netzverlustentgelts,
Stand 2026 laut E-Control.</p>
{A.table(
    ["Merkmal", "Lokale EEG", "Regionale EEG", "Bürgerenergiegemeinschaft"],
    [
        ["Verbindung über", "selber Trafo (Niederspannung)", "selbes Umspannwerk (Mittelspannung)",
         "österreichweit, ab Okt. 2026 auch im Nahbereich"],
        ["Netznutzungsentgelt (Arbeit)", "minus 57 %", "minus 28 %", "voll, im Nahbereich reduziert"],
        ["Netzverlustentgelt", "minus 57 %", "minus 28 %", "voll"],
        ["Elektrizitätsabgabe (1,5 ct/kWh)", "entfällt", "entfällt", "bleibt"],
        ["Erneuerbaren-Förderbeitrag", "entfällt", "entfällt", "bleibt"],
        ["Typisch in Kärnten", "Ortschaft, Siedlung, Gewerbegebiet", "Gemeinde, Tal, Bezirksteil",
         "Strom teilen über Bundesländer hinweg"],
    ],
    hl_cols=(1, 2),
)}
<p>Die Bürgerenergiegemeinschaft ist der Weg, wenn die Abnehmer nicht im Nahbereich sitzen, etwa die Tante in Wien.
Auch das bietet EBZ österreichweit an, nur ohne den Netzentgelt-Abschlag. Die gute Nachricht für alle anderen: Sie
müssen die Netzebene nicht selbst herausfinden. Bei der Anmeldung prüft der Netzbetreiber über die Zählpunktnummer,
welchem Trafo und welchem Umspannwerk Ihr Anschluss zugeordnet ist. EBZ übernimmt diese Abfrage im Rahmen der
Erstberatung. Was der Abschlag Position für Position bringt, steht im Artikel
{a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft und Netzkosten')}.</p>
"""),
        ("So kommen Sie in Kärnten in eine Energiegemeinschaft", "ablauf", f"""
<p>Es gibt zwei Wege: einer bestehenden Gemeinschaft beitreten oder eine neue gründen. Für die meisten Privathaushalte
ist der {a('/energiegemeinschaft-beitreten/', 'Beitritt')} der schnellere Weg, weil die Rechtsform, der Vertrag mit
dem Netzbetreiber und die Abrechnung schon stehen. Die Gründung lohnt sich vor allem für Gemeinden, Betriebe oder
Nachbarschaften mit mehreren Erzeugern, Details dazu im Artikel
{a('/energiegemeinschaft-gruenden/', 'Energiegemeinschaft gründen')}.</p>
{A.steps([
    ("Erstgespräch und Eignungscheck",
     "Wir klären Ihre PV-Leistung, den Verbrauch, ob ein Smart Meter mit Viertelstundenwerten aktiv ist und in "
     "welchem Netzbereich Ihr Anschluss liegt."),
    ("Passende Gemeinschaft wählen",
     "Je nach Standort nehmen wir Sie in eine bestehende Energiegemeinschaft im Nahbereich auf oder bündeln mehrere "
     "Interessenten zu einer neuen."),
    ("Zählpunktfreigabe beim Netzbetreiber",
     "Im Kundenportal der Kärnten Netz stimmen Sie der Datenweitergabe für Ihren Zählpunkt zu. Das dauert wenige "
     "Minuten, wir leiten Sie an."),
    ("Aufnahme und Start",
     "Die Gemeinschaft meldet Ihren Zählpunkt über das EDA-Portal an. Ab dem Folgemonat wird Ihr Strom zugeordnet."),
    ("Monatliche Abrechnung",
     "Über die energyfamily-Plattform sehen Sie, wie viel Strom Sie in die Gemeinschaft geliefert oder von ihr "
     "bezogen haben. Die Abrechnung läuft automatisch."),
])}
{A.cta("Energiegemeinschaft in Kärnten: Eignung in 10 Minuten prüfen",
       "Nennen Sie uns Postleitzahl, PV-Leistung und Jahresverbrauch. Wir sagen Ihnen, welche Gemeinschaft für Sie "
       "infrage kommt und was sie bringt.",
       secondary=("eg_rechner", "Ersparnis berechnen"))}
"""),
        ("Welche Anbieter es in Kärnten gibt und wo EBZ steht", "anbieter", f"""
<p>In Kärnten sind mehrere Modelle aktiv. Die Kelag bietet eigene Energiegemeinschaften an, die Raiffeisen
Energiegenossenschaft Kärnten ist in vielen Gemeinden präsent. Bei beiden müssen Sie weder Lieferanten noch
Bankverbindung wechseln, es sind aber in erster Linie Abrechnungsangebote: Die PV-Anlage selbst, den
{a('batteriespeicher', 'Speicher')} und die Optimierung des Eigenverbrauchs müssen Sie anderswo organisieren.</p>
<p>EBZ Energie geht den umgekehrten Weg. Wir kommen von der Anlage und ergänzen sie um die Energiegemeinschaft. Das
hat einen praktischen Vorteil: Die Auslegung der Anlage, der Speicher, die Wallbox und das
{a('ems', 'Energiemanagementsystem')} werden von Anfang an darauf abgestimmt, dass Ihr Überschuss dann anfällt, wenn
die Gemeinschaft ihn braucht. Für die Abrechnung arbeiten wir mit energyfamily, einer österreichischen Plattform mit
rund 330 aktiven Gemeinschaften und rund 15.000 Nutzern, damit Sie sich um Verwaltung und Buchhaltung nicht kümmern
müssen. Alle Details zur Leistung: {a('eg_privat', 'Energiegemeinschaft für Private')}.</p>
"""),
        ("Was sich ab Oktober 2026 durch das ElWG ändert", "elwg", f"""
<p>Mit 1. Oktober 2026 treten die Bestimmungen des neuen Elektrizitätswirtschaftsgesetzes zur gemeinsamen
Energienutzung in Kraft. Bestehende Energiegemeinschaften laufen weiter und werden ins neue System übergeführt. Neu
sind vor allem Peer-to-Peer-Verträge: Damit können Sie Strom auch ohne Verein direkt an einen Nachbarn verkaufen.
Die volle Befreiung von Elektrizitätsabgabe und Förderbeitrag bleibt aber der Erneuerbaren-Energie-Gemeinschaft
vorbehalten.</p>
{A.box("Die EEG bleibt das wirtschaftlich stärkste Modell, Peer-to-Peer wird eine Ergänzung für einzelne "
       "Nachbarschaftslösungen. Wir aktualisieren diesen Artikel, sobald die Marktprozesse der Netzbetreiber "
       "feststehen.", label="Für Kärnten heißt das:")}
"""),
        ("Förderung in Kärnten: Gibt es Geld für die Energiegemeinschaft?", "foerderung", f"""
<p>Für die Teilnahme selbst gibt es in Kärnten keine eigene Prämie. Gefördert wird die PV-Anlage, und zwar über den
EAG-Investitionszuschuss des Bundes plus die Kärntner Landesförderung mit der 3.000-Euro-Pauschale, die wir im
Artikel {a('foerderung_kaernten', 'Photovoltaik-Förderung Kärnten')} aufgeschlüsselt haben. Wer zusätzlich ein
Energiemanagementsystem einbaut, kann die {a('/ems-foerderung/', 'EMS-Förderung des Klimafonds')} nutzen: Die
Teilnahme an einer Energiegemeinschaft zählt dort als eine der zulässigen Betriebsoptionen. Wer die Anlage über EBZ
errichten lässt, bekommt Förderabwicklung und EG-Anbindung aus einer Hand.</p>
"""),
        ("Fazit: Energiegemeinschaft Kärnten", "fazit", f"""
<p>Kärnten hat viel Sonne, niedrige Einspeisetarife und ein kleinteiliges Netz. Das ist die ideale Kombination für
lokale Energiegemeinschaften. Wer eine PV-Anlage hat oder plant, verschenkt ohne Gemeinschaft jedes Jahr einen
dreistelligen Betrag. Der Einstieg dauert wenige Wochen, die Abrechnung läuft automatisch, und das Risiko ist
gering, weil Sie jederzeit austreten können und Ihr Lieferant bleibt. Für Villach, Klagenfurt und das Umland haben
wir die Details im Artikel {a('/energiegemeinschaft-villach-klagenfurt/', 'Energiegemeinschaft Villach und Klagenfurt')}
zusammengefasst.</p>
{A.cta("Jetzt Ersparnis für Ihren Standort berechnen",
       "Unser Rechner vergleicht OeMAG-Einspeisung mit der Energiegemeinschaft, auf Basis Ihrer kWp, Ihres "
       "Verbrauchs und Ihrer Netzebene.",
       primary=("kontakt", "Beratung anfragen"), secondary=("eg_rechner", "Zum Energiegemeinschaft-Rechner"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Energiegemeinschaft in Kärnten: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und Wallboxen in "
                 "Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. Dazu kommt "
                 "die Energiegemeinschaft: Wir nehmen Sie in eine bestehende Gemeinschaft auf oder bauen mit Ihnen eine "
                 "eigene auf, abgerechnet über die Plattform unseres Partners energyfamily. Einzugsgebiet: Villach, "
                 "Klagenfurt, Spittal, Feldkirchen, St. Veit, Völkermarkt, Wolfsberg, Hermagor und Umgebung."),
        "grid": [
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EG-Anbindung vom selben Team."),
            ("Regional verankert", "Sitz in Villach, Montage in ganz Kärnten und der Steiermark."),
            ("Abrechnung inklusive", "Zählpunktfreigabe, Aufnahme und monatliche Abrechnung über energyfamily."),
            ("Kostenlose Erstberatung", "Wir prüfen Netzebene, Eignung und Ihr Einsparpotenzial."),
        ],
    },

    "faq": [
        ("Wer darf in Kärnten an einer Energiegemeinschaft teilnehmen?",
         "Privathaushalte, Gemeinden, Vereine und kleine sowie mittlere Unternehmen. Eine eigene PV-Anlage ist nicht "
         "Voraussetzung, reine Abnehmer sind ausdrücklich erwünscht. Voraussetzung ist ein Zählpunkt im selben "
         "Netzbereich und ein Smart Meter mit Viertelstundenwerten."),
        ("Muss ich meinen Stromlieferanten wechseln?",
         "Nein. Der Lieferantenvertrag bleibt bestehen. Die Energiegemeinschaft deckt nur den Anteil, der zeitgleich "
         "in der Gemeinschaft erzeugt wird. Den Rest liefert weiterhin Ihr bisheriger Anbieter."),
        ("Wie viel Netzentgelt spare ich in Kärnten?",
         "Bei einer lokalen EEG (selber Trafo) 57 Prozent des Arbeitspreises von Netznutzungs- und Netzverlustentgelt, "
         "bei einer regionalen EEG (selbes Umspannwerk) 28 Prozent. Dazu entfallen Elektrizitätsabgabe von 1,5 Cent "
         "je kWh und Erneuerbaren-Förderbeitrag auf den EG-Strom."),
        ("Kann ich Strom auch mit Verwandten außerhalb Kärntens teilen?",
         "Ja, über eine Bürgerenergiegemeinschaft, die österreichweit funktioniert. Der Netzentgelt-Abschlag von "
         "57 oder 28 Prozent gilt dann aber nicht, weil er an den Nahbereich gebunden ist. EBZ bietet beide Varianten "
         "an und rechnet über energyfamily ab."),
        ("Brauche ich einen Speicher für die Energiegemeinschaft?",
         "Nein, aber er hilft. Ein Speicher erhöht den Eigenverbrauch und verschiebt Überschuss in die Abendstunden, "
         "in denen Abnehmer in der Gemeinschaft mehr brauchen. Die Kombination aus Speicher, EMS und "
         "Energiegemeinschaft holt am meisten heraus."),
        ("Kann ich die Energiegemeinschaft wieder verlassen?",
         "Ja. Die Kündigungsfristen regelt die jeweilige Gemeinschaft, üblich sind ein bis drei Monate zum Monatsende. "
         "Der Zählpunkt wird dann beim Netzbetreiber abgemeldet, Ihr Lieferantenvertrag läuft unverändert weiter."),
        ("Was kostet die Teilnahme?",
         "Je nach Gemeinschaft ein kleiner Mitgliedsbeitrag oder eine Plattformgebühr von wenigen Euro im Monat, "
         "im Beispiel unseres Rechners 4 Euro*. Bei EBZ erfahren Sie die genauen Konditionen im Erstgespräch, "
         "bevor Sie sich entscheiden."),
        ("Wie lange dauert der Einstieg in Kärnten?",
         "Vom Erstgespräch bis zur ersten zugeordneten Kilowattstunde vergehen in der Regel vier bis acht Wochen. "
         "Der größte Zeitfaktor ist die Zählpunktanmeldung bei der Kärnten Netz, die zum Monatsersten wirksam wird."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und errichtet Photovoltaik-, "
                    "Speicher- und Wärmepumpensysteme in Kärnten und der Steiermark und begleitet Kunden beim Einstieg "
                    "in Energiegemeinschaften. Inhalte werden regelmäßig anhand der Vorgaben von E-Control, OeMAG und "
                    "energiegemeinschaften.gv.at aktualisiert. Keine Rechts- oder Steuerberatung."),
    "sources": [
        ("E-Control: Energiegemeinschaften", "https://www.e-control.at/energiegemeinschaften"),
        ("Koordinationsstelle: Neue rechtliche Grundlagen (ElWG)",
         "https://energiegemeinschaften.gv.at/rechtliche-grundlagen-elwg/"),
        ("OeMAG: Aktueller Marktpreis", "https://www.oem-ag.at/marktpreis"),
        ("Kelag: Energiegemeinschaften", "https://www.kelag.at/privatkunden/energiegemeinschaften.htm"),
    ],
    "related": [
        ("/energiegemeinschaft-villach-klagenfurt/", "Energiegemeinschaft in Villach und Klagenfurt"),
        ("/energiegemeinschaft-beitreten/", "Energiegemeinschaft beitreten: Ablauf"),
        ("/energiegemeinschaft-netzkosten/", "Netzkosten sparen mit der EG"),
        ("eg_privat", "Energiegemeinschaft für Private mit Rechner"),
    ],
    "cta": {
        "h3": "Eignung für Ihren Zählpunkt prüfen",
        "text": "Wir fragen den Nahbereich bei der Kärnten Netz ab und sagen Ihnen, welche Gemeinschaft für Sie passt.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihr Solarstrom bleibt in Kärnten",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das PV-Anlage, Speicher und "
                   "Energiegemeinschaft aus einer Hand liefert."),
}
