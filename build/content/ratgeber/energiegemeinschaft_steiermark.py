"""Ratgeber: Energiegemeinschaft Steiermark.

Migriert von ebz-photovoltaik.at/energiegemeinschaft-steiermark/ (Stand August 2026),
Inhalt freigegeben, auf die Ratgeber-Vorlage umgestellt. Rechenbeispiel der Quelle war in
sich widersprüchlich (Jahresverbrauch 5.000 kWh bei 5.800 kWh Eigenverbrauch) und wurde
auf konsistente Werte gebracht (Jahresverbrauch 7.800 kWh, Netzbezug 2.000 kWh).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "energiegemeinschaft-steiermark",
    "path": "/energiegemeinschaft-steiermark/",
    "title": "Energiegemeinschaft Steiermark: 125 €/kWp Bonus | EBZ Energie",
    "description": ("Energiegemeinschaft in der Steiermark: Landesbonus 125 € je kWp bei EG-Teilnahme, Netzentgelt "
                    "bis 57 % weniger, Rechenbeispiel mit 10 kWp. Beitritt in 4 bis 8 Wochen mit EBZ Energie."),
    "eyebrow": "Energiegemeinschaft · Steiermark",
    "crumb_label": "Energiegemeinschaft Steiermark",
    "h1": "Energiegemeinschaft Steiermark: 125 Euro je kWp Bonus und mehr aus jeder Kilowattstunde",
    "lead": ("Die Steiermark ist das Bundesland mit den meisten Suchanfragen zur Energiegemeinschaft. Kein Wunder: "
             "Hier gibt es als einziges Land einen eigenen Förderbonus für Teilnehmer."),
    "chips": [
        "Landesbonus: <b>125 €/kWp</b> bei EG-Teilnahme",
        "Netzentgelt: <b>bis zu 57 %</b> weniger",
        "OeMAG Juli 2026: <b>6,146 ct/kWh</b>",
        "EBZ vor Ort in der <b>ganzen Steiermark</b>",
    ],
    "date_published": "2026-08-05",
    "date_modified": "2026-09-24",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus in der Steiermark mit Photovoltaikanlage auf dem Dach",

    "tldr": [
        "In der Steiermark gibt es neben den bundesweiten Vorteilen einen eigenen Anreiz: Die Landesförderung zahlt "
        "125 Euro je kWp zusätzlich, wenn die PV-Anlage Teil eines dezentralen Energiesystems ist, etwa durch "
        "Teilnahme an einer Energiegemeinschaft. Bei 10 kWp sind das 1.250 Euro.",
        "Netzbetreiber sind vor allem die Energienetze Steiermark und in Graz die Stromnetz Graz. Der Nahbereich "
        "(Trafo oder Umspannwerk) bestimmt den Netzentgelt-Abschlag von 57 oder 28 Prozent.",
        "Der OeMAG-Marktpreis lag im Juli 2026 bei 6,146 Cent je kWh. Zwischen diesem Tarif und dem "
        "Haushaltsstrompreis liegt eine Spanne von rund 10 Cent, die die Gemeinschaft aufteilt.",
        "Aktive Gemeinschaften gibt es in fast allen Bezirken, von Leibnitz über Weiz bis ins Murtal. EBZ Energie "
        "nimmt Kunden in der Steiermark auf und rechnet über energyfamily ab.",
    ],
    "kpis": [
        ("125 €/kWp", "Landesbonus bei Einbindung ins dezentrale Energiesystem"),
        ("1.250 €", "Bonus bei einer 10-kWp-Anlage"),
        ("57 % / 28 %", "Netzentgelt-Abschlag lokal / regional"),
        ("4 bis 8 Wochen", "vom Erstgespräch bis zum Start"),
    ],

    "sections": [
        ("Energiegemeinschaft in der Steiermark: die Ausgangslage", "ausgangslage", f"""
<p>Die Steiermark hat in den vergangenen Jahren mehr PV-Leistung zugebaut als fast jedes andere Bundesland, und
genau daraus entsteht das Problem, das die Energiegemeinschaft löst: Zu Mittag drückt so viel Sonnenstrom ins Netz,
dass der Börsenpreis fällt und der OeMAG-Tarif seit Frühjahr 2026 an der gesetzlichen Untergrenze klebt, im Juli
waren es 6,146 Cent pro Kilowattstunde. Gleichzeitig zahlen Ihre Nachbarn für Strom aus dem Netz das Dreifache. Eine
Energiegemeinschaft schließt diese Lücke, indem sie Ihren Überschuss direkt an Abnehmer im selben Netzgebiet
verkauft, zu einem Preis, den die Gemeinschaft selbst bestimmt.</p>
{A.table(
    ["Wo der Überschuss landet", "Cent je kWh", "Wer bekommt / zahlt"],
    [
        ["OeMAG-Tarif (Juli 2026)", "6,1 ct", "Erzeuger bekommt"],
        ["EG-Einspeisung*", "10,0 ct", "Erzeuger bekommt"],
        ["EG-Bezug*", "14,0 ct", "Abnehmer zahlt"],
        ["Lieferant, Arbeitspreis netto*", "17,0 ct", "Abnehmer zahlt"],
    ],
    hl_cols=(1,),
)}
<p>Zwischen OeMAG-Tarif und Haushaltsstrompreis liegt eine Spanne von rund 10 Cent. Die Energiegemeinschaft teilt
diese Spanne zwischen Erzeuger und Abnehmer auf. Das Prinzip ist in ganz Österreich gleich und in unserem
{a('eg', 'Leitartikel zur Energiegemeinschaft')} erklärt. Was die Steiermark besonders macht, sind drei Dinge: der
Landesbonus, die Netzstruktur mit zwei großen Betreibern und die Dichte an bestehenden Gemeinschaften.</p>
<p><small>*Beispielwerte aus dem Markt, jede Gemeinschaft legt ihre Preise selbst fest. Lieferantenpreis netto ohne
Netz und Abgaben.</small></p>
"""),
        ("Der steirische Bonus: 125 Euro je kWp für Teilnehmer", "landesbonus", f"""
<p>Die Photovoltaik-Förderung des Landes Steiermark kennt einen Zuschlag von 125 Euro pro Kilowattpeak, wenn die
Anlage in ein ganzheitliches, dezentrales Energiesystem eingebunden ist. Das gilt bei Kombination mit mindestens
zwei weiteren neu installierten Komponenten, etwa {a('batteriespeicher', 'Speicher')} und Wallbox, oder eben durch
die Teilnahme an einer Energiegemeinschaft. Bei einer 10-kWp-Anlage sind das 1.250 Euro, die es ohne Gemeinschaft
nicht gäbe. Alle Details, Fristen und den Made-in-Europe-Bonus finden Sie im Artikel
{a('foerderung_steiermark', 'Photovoltaik-Förderung Steiermark 2026')}.</p>
{A.box("Der Nachweis für den Bonus ist die Teilnahmebestätigung der Energiegemeinschaft. Wer die Anlage über EBZ "
       "errichten lässt, bekommt die Aufnahme in die Gemeinschaft zeitlich so gelegt, dass der Nachweis bei der "
       "Förderabrechnung vorliegt.", label="Praxistipp:")}
"""),
        ("Netzgebiete: Energienetze Steiermark und Stromnetz Graz", "netzgebiete", f"""
<p>Den Großteil der Steiermark versorgt die Energienetze Steiermark GmbH, die Landeshauptstadt die Stromnetz Graz
GmbH. Beide melden Zählpunkte nach demselben bundesweiten Verfahren über das EDA-Portal an, und beide ordnen Ihren
Anschluss bei der Anmeldung einem Trafo und einem Umspannwerk zu. Daraus ergibt sich, ob Sie mit anderen Teilnehmern
lokal oder regional verbunden sind: Lokal (Niederspannung, derselbe Trafo) bringt den größten Netzentgelt-Abschlag
von 57 Prozent, regional (dasselbe Umspannwerk) den kleineren von 28 Prozent. Der Abschlag gilt auf den Arbeitspreis
des Netznutzungs- und Netzverlustentgelts, Stand 2026 laut E-Control. Die Rechnung Position für Position steht im
Artikel {a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft und Netzkosten')}.</p>
<p>Ein Punkt, der in der Steiermark häufiger vorkommt als anderswo: Gemeinschaften, die über die Grenze zweier
Netzgebiete hinweg wachsen wollen, etwa Graz-Stadt und Graz-Umgebung. Das ist als Erneuerbare-Energie-Gemeinschaft
nicht möglich, weil der Nahbereich an den Netzbetreiber gebunden ist. In solchen Fällen werden zwei getrennte
Gemeinschaften gegründet oder eine Bürgerenergiegemeinschaft, die österreichweit funktioniert und ab Oktober 2026
im Nahbereich ebenfalls reduzierte Netzentgelte bekommt, aber nicht die Abgabenbefreiung. Außerhalb des Nahbereichs,
etwa beim Stromteilen mit Verwandten in einem anderen Bundesland, gibt es in der Bürgerenergiegemeinschaft keinen
Netzentgelt-Abschlag.</p>
"""),
        ("Aktive Energiegemeinschaften in den steirischen Bezirken", "bezirke", f"""
<p>Die Steiermark zählt zu den aktivsten Regionen Österreichs. Suchanfragen nach Gemeinschaften in Leibnitz, Weiz,
Murtal, Deutschlandsberg, Leoben, Gleisdorf, Feistritztal, Premstätten, Frohnleiten oder Hausmannstätten zeigen, wie
verteilt die Nachfrage ist. Viele dieser Gemeinschaften sind als Verein organisiert und von Gemeinden oder engagierten
Privatpersonen gegründet worden. Die Energie Steiermark bietet ebenfalls eine eigene Plattform an.</p>
{A.table(
    ["Region", "Typische Struktur", "Was für Sie zählt"],
    [
        ["Graz und Graz-Umgebung", "viele Mehrparteienhäuser, GEA und lokale EEG",
         "Netzgebiet prüfen (Stadt oder Umgebung), hohe Abnehmerdichte"],
        ["Leibnitz, Deutschlandsberg, Südoststeiermark", "Gemeinde-EEG, landwirtschaftliche Dächer",
         "viele Erzeuger, Abnehmer sind gefragt"],
        ["Weiz, Gleisdorf, Feistritztal", "Vereins-EEG mit Gemeindebeteiligung",
         "oft regional, Umspannwerk als Grenze"],
        ["Murtal, Leoben, Obersteiermark", "Tal-Strukturen, regionale EEG",
         "größerer Nahbereich, Winterertrag beachten"],
    ],
)}
<p>Ob in Ihrer Gemeinde schon eine passende Gemeinschaft besteht oder ob es sinnvoller ist, eine neue zu starten,
zeigt unser Artikel {a('/energiegemeinschaft-finden/', 'Energiegemeinschaft finden')}. EBZ prüft das für Sie im
Erstgespräch.</p>
{A.cta("Energiegemeinschaft in der Steiermark: Jetzt Eignung prüfen",
       "Wir klären Netzgebiet, passende Gemeinschaft und ob Ihre Anlage für den 125-Euro-Bonus infrage kommt.",
       secondary=("eg_rechner", "Ersparnis berechnen"))}
"""),
        ("Rechenbeispiel für ein steirisches Einfamilienhaus", "rechenbeispiel", f"""
<p>Ein Haushalt in der Weststeiermark mit 10 kWp und 5 kWh Speicher, Jahresverbrauch rund 7.800 kWh (mit
Wärmepumpe), Ertrag rund 10.500 kWh. Eigenverbrauch mit Speicher etwa 55 Prozent der Erzeugung, also 5.800 kWh, der
Rest von 4.700 kWh ist Überschuss. Der Netzbezug liegt bei 2.000 kWh. In einer lokalen EEG landen vom Überschuss
typisch 60 bis 70 Prozent bei anderen Mitgliedern.</p>
{A.table(
    ["Position", "Ohne EG", "Mit lokaler EEG*"],
    [
        ["Einspeisung 4.700 kWh", "zu 6,1 ct: 287 €", "3.000 kWh zu 10 ct + 1.700 kWh zu 6,1 ct: 404 €"],
        ["Netzbezug 2.000 kWh, davon 600 kWh aus EG", "Netzentgelt voll",
         "600 kWh mit minus 57 % Netz, ohne E-Abgabe: ca. 40 € gespart"],
        ["Landesbonus (einmalig)", "0 €", "1.250 €"],
        ["Vorteil im ersten Jahr", "", "ca. 1.400 €, danach ca. 150 bis 180 € jährlich"],
    ],
    hl_cols=(2,),
)}
<p>Die laufende Ersparnis wirkt auf den ersten Blick bescheiden. Über 20 Jahre Anlagenlaufzeit summiert sie sich
aber auf mehr als 3.000 Euro, und der Hebel wächst mit jeder Tariferhöhung beim Netzentgelt. Rechnen Sie Ihre Zahlen
im {a('eg_rechner', 'EG-Rechner')} nach.</p>
<p><small>*Beispielkonditionen: EG-Einspeisepreis 10 Cent je kWh, Netzentgelt-Richtwerte 2026. Jede Gemeinschaft
legt ihre Preise selbst fest, die Zuordnungsquote hängt von Erzeugern und Abnehmern im Nahbereich ab.</small></p>
"""),
        ("Fazit: Energiegemeinschaft Steiermark", "fazit", f"""
<p>Nirgendwo in Österreich ist der Einstieg in eine Energiegemeinschaft so gut angeschoben wie in der Steiermark:
Landesbonus, viele bestehende Gemeinschaften und zwei Netzbetreiber mit eingespielten Prozessen. Wer jetzt eine
{a('photovoltaik', 'PV-Anlage')} plant, sollte die Gemeinschaft von Anfang an mitdenken. Wer schon eine hat, kann in
wenigen Wochen {a('/energiegemeinschaft-beitreten/', 'beitreten')}.</p>
{A.cta("Ihre Anlage, Ihre Gemeinschaft, ein Ansprechpartner",
       "EBZ Energie plant die Anlage, beantragt die Förderung inklusive Bonus und bringt Sie in die passende "
       "Energiegemeinschaft.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("eg_privat", "Zur Leistungsseite"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Energiegemeinschaft in der Steiermark: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und Wallboxen in "
                 "Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. Dazu kommt "
                 "die Energiegemeinschaft: Wir nehmen Sie in eine bestehende Gemeinschaft auf oder bauen mit Ihnen eine "
                 "eigene auf, abgerechnet über die Plattform unseres Partners energyfamily. Einzugsgebiet Steiermark: "
                 "Graz und Graz-Umgebung, Leibnitz, Deutschlandsberg, Voitsberg, Weiz, Murtal, Leoben, "
                 "Bruck-Mürzzuschlag, Südoststeiermark und Umgebung."),
        "grid": [
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EG-Anbindung vom selben Team."),
            ("Bonus mitgeplant", "Aufnahme in die Gemeinschaft so terminiert, dass der 125-Euro-Nachweis vorliegt."),
            ("Abrechnung inklusive", "Zählpunktfreigabe, Aufnahme und monatliche Abrechnung über energyfamily."),
            ("Kostenlose Erstberatung", "Wir prüfen Netzgebiet, Eignung und Ihr Einsparpotenzial."),
        ],
    },

    "faq": [
        ("Gibt es in der Steiermark eine Förderung für die Energiegemeinschaft?",
         "Indirekt ja. Die PV-Landesförderung zahlt 125 Euro je kWp zusätzlich, wenn die Anlage in ein dezentrales "
         "Energiesystem eingebunden ist, unter anderem durch Teilnahme an einer Energiegemeinschaft. Bei 10 kWp sind "
         "das 1.250 Euro. Für die Teilnahme allein gibt es keine eigene Prämie."),
        ("Welcher Netzbetreiber ist für mich zuständig?",
         "In Graz-Stadt die Stromnetz Graz GmbH, fast überall sonst die Energienetze Steiermark GmbH. Die Zuordnung "
         "steht auf Ihrer Netzrechnung. Sie bestimmt, mit wem Sie lokal oder regional verbunden sein können."),
        ("Kann ich an mehreren Energiegemeinschaften teilnehmen?",
         "Ja, die Mehrfachteilnahme ist seit 2024 möglich, mit bis zu fünf Gemeinschaften je Zählpunkt. In der "
         "Praxis reicht für Privathaushalte eine gut passende Gemeinschaft."),
        ("Was passiert mit meinem Strom, wenn in der Gemeinschaft niemand Bedarf hat?",
         "Er wird wie bisher an die OeMAG oder Ihren Einspeisevertragspartner geliefert und zum dortigen Tarif "
         "vergütet, im Juli 2026 waren das 6,146 Cent je kWh. Sie verlieren also nichts gegenüber heute."),
        ("Wie lange dauert der Beitritt?",
         "Vom Erstgespräch bis zur ersten zugeordneten Kilowattstunde vergehen in der Regel vier bis acht Wochen. "
         "Der größte Zeitfaktor ist die Zählpunktanmeldung beim Netzbetreiber."),
        ("Muss ich meinen Stromlieferanten wechseln?",
         "Nein. Ihr Vertrag mit Energie Steiermark oder einem anderen Lieferanten bleibt unverändert. Die "
         "Gemeinschaft deckt nur den Anteil, der zeitgleich in der Gemeinschaft erzeugt wird."),
        ("Kann ich Strom auch mit Verwandten außerhalb der Steiermark teilen?",
         "Ja, über eine Bürgerenergiegemeinschaft, die österreichweit funktioniert. Den Netzentgelt-Abschlag von "
         "57 oder 28 Prozent gibt es dann nicht, weil er an den Nahbereich gebunden ist. EBZ bietet beide "
         "Varianten an."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und errichtet Photovoltaik-, "
                    "Speicher- und Wärmepumpensysteme in Kärnten und der Steiermark und begleitet Kunden beim Einstieg "
                    "in Energiegemeinschaften. Inhalte werden regelmäßig anhand der Vorgaben von E-Control, OeMAG und "
                    "energiegemeinschaften.gv.at aktualisiert. Keine Rechts- oder Steuerberatung, maßgeblich sind die "
                    "Förderrichtlinien des Landes Steiermark."),
    "sources": [
        ("E-Control: Energiegemeinschaften", "https://www.e-control.at/energiegemeinschaften"),
        ("Koordinationsstelle: Änderungen für bestehende EGs",
         "https://energiegemeinschaften.gv.at/aenderungen-fuer-bestehende-energiegemeinschaften/"),
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/marktpreis"),
    ],
    "related": [
        ("/energiegemeinschaft-kaernten/", "Energiegemeinschaft Kärnten"),
        ("/energiegemeinschaft-finden/", "Energiegemeinschaft finden"),
        ("/oemag-einspeisetarif/", "OeMAG-Einspeisetarif und die Alternative"),
        ("foerderung_steiermark", "Photovoltaik-Förderung Steiermark 2026"),
    ],
    "cta": {
        "h3": "125-Euro-Bonus mitnehmen",
        "text": "Wir planen Anlage, Förderung und Energiegemeinschaft so, dass der Nachweis rechtzeitig vorliegt.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Mehr aus jeder steirischen Kilowattstunde",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team, das PV-Anlage, Förderung und "
                   "Energiegemeinschaft in der Steiermark aus einer Hand übernimmt."),
}
