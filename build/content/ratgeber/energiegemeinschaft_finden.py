"""Ratgeber: Energiegemeinschaft finden.

Migriert von ebz-photovoltaik.at/energiegemeinschaft-finden/ (Stand August 2026),
Inhalt freigegeben, auf die Ratgeber-Vorlage umgestellt. Hinweis auf die österreichweite
Bürgerenergiegemeinschaft (ohne Netzentgelt-Abschlag) als vierte Option ergänzt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "energiegemeinschaft-finden",
    "path": "/energiegemeinschaft-finden/",
    "title": "Energiegemeinschaft finden: 3 Wege, 11.000+ Gemeinschaften | EBZ",
    "description": ("Energiegemeinschaft in der Nähe finden: Nahbereich statt Postleitzahl, 3 Suchwege "
                    "(Netzbetreiber, Plattform, Gemeinde), 5 Prüfpunkte vor dem Beitritt. In Kärnten und der "
                    "Steiermark übernimmt EBZ die Suche."),
    "eyebrow": "Energiegemeinschaft · Suche",
    "crumb_label": "Energiegemeinschaft finden",
    "h1": "Energiegemeinschaft finden: Der Nahbereich zählt, nicht die Postleitzahl",
    "lead": ("Die Suche nach einer Energiegemeinschaft in der Nähe ist die am schnellsten wachsende Anfrage zum "
             "Thema. Das Problem: Nähe bedeutet hier etwas anderes als auf der Landkarte."),
    "chips": [
        "Nähe = <b>selber Trafo oder Umspannwerk</b>",
        "<b>11.000+</b> Gemeinschaften in Österreich",
        "<b>3 Wege</b> zur passenden EG",
        "EBZ übernimmt die Suche in <b>1 Werktag</b>",
    ],
    "date_published": "2026-08-15",
    "date_modified": "2026-09-24",
    "hero_img": "gen_detail",
    "hero_alt": "Monteur prüft Photovoltaikmodule auf einem Dach, im Hintergrund weitere Häuser der Siedlung",

    "tldr": [
        "Eine Energiegemeinschaft muss mit Ihrem Zählpunkt im selben Nahbereich liegen: lokal (gleicher Trafo, "
        "minus 57 Prozent Netzentgelt) oder regional (gleiches Umspannwerk, minus 28 Prozent). Die Entfernung in "
        "Kilometern ist zweitrangig.",
        "Österreich zählt über 11.000 Energiegemeinschaften, davon mehr als 5.500 Erneuerbare-Energie-Gemeinschaften. "
        "In fast jedem Umspannwerksbereich Kärntens und der Steiermark gibt es mindestens eine.",
        "Drei Wege führen zur passenden Gemeinschaft: Nahbereichsabfrage beim Netzbetreiber, Plattformen wie "
        "energyfamily (rund 330 Gemeinschaften, rund 15.000 Nutzer), Gemeinde und regionale Energieberatung.",
        "Gibt es keine im Nahbereich: regional ausweichen, selbst gründen oder österreichweit als "
        "Bürgerenergiegemeinschaft teilen (dann ohne Netzentgelt-Abschlag).",
        "In Kärnten und der Steiermark übernimmt EBZ Energie die Suche: Wir prüfen Ihren Zählpunkt innerhalb eines "
        "Werktags und nennen Ihnen die Gemeinschaften, die infrage kommen.",
    ],
    "kpis": [
        ("11.000+", "Energiegemeinschaften in Österreich"),
        ("5.500+", "davon Erneuerbare-Energie-Gemeinschaften"),
        ("57 % / 28 %", "Netzentgelt-Abschlag lokal / regional"),
        ("1 Werktag", "Nahbereichsabfrage bei EBZ"),
    ],

    "sections": [
        ("Warum Sie keine Energiegemeinschaft auf der Landkarte finden", "nahbereich", f"""
<p>Wer nach einer Energiegemeinschaft in der Nähe sucht, erwartet eine Karte mit Pins. Die gibt es nicht, und sie
wäre auch irreführend. Ob Sie an einer Gemeinschaft teilnehmen können, hängt nicht davon ab, wie weit sie entfernt
ist, sondern ob Ihr Stromanschluss am selben Trafo (Lokalbereich) oder am selben Umspannwerk (Regionalbereich)
hängt wie die anderen Mitglieder. Eine Gemeinschaft am anderen Ende der Straße kann außerhalb Ihres Nahbereichs
liegen, eine im Nachbarort innerhalb. Die Zuordnung kennt nur der Netzbetreiber.</p>
{A.table(
    ["Nahbereich", "Verbindung über", "Netzentgelt-Abschlag*", "Typische Ausdehnung"],
    [
        ["Lokal", "selber Trafo (Niederspannung)", "minus 57 %", "Ortschaft, Siedlung, Gewerbegebiet"],
        ["Regional", "selbes Umspannwerk (Mittelspannung)", "minus 28 %", "Gemeinde, Tal, Bezirksteil"],
        ["Österreichweit (BEG)", "keine Netzbindung", "kein Abschlag", "Verwandte oder Freunde in anderen Bundesländern"],
    ],
    hl_cols=(2,),
)}
<p><small>*Abschlag auf den Arbeitspreis des Netznutzungs- und Netzverlustentgelts, Stand 2026 (E-Control).
Details im Artikel {a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft und Netzkosten')}.</small></p>
<p>Österreich zählt inzwischen mehr als 11.000 Energiegemeinschaften, davon über 5.500
Erneuerbare-Energie-Gemeinschaften. Statistisch liegt damit in fast jedem Umspannwerksbereich Kärntens und der
Steiermark mindestens eine aktive Gemeinschaft. Die Frage ist nur, wie Sie sie finden.</p>
"""),
        ("Weg 1: Nahbereichsabfrage beim Netzbetreiber", "weg-netzbetreiber", f"""
<p>Jeder Netzbetreiber bietet eine Auskunft, zu welchem Trafo und Umspannwerk ein Zählpunkt gehört. Bei der Kärnten
Netz, den Energienetzen Steiermark und der Stromnetz Graz läuft das über das Kundenportal oder auf Anfrage mit der
Zählpunktnummer. Das Ergebnis ist eine Kennung des Lokal- und Regionalbereichs. Mit dieser Kennung können Sie bei
Gemeinschaften und Plattformen gezielt fragen, ob Sie passen. Manche Netzbetreiber, etwa die Netz NÖ, bieten einen
Quick-Check, bei dem Sie zwei Zählpunkte eingeben und sofort sehen, ob sie im selben Nahbereich liegen. Für Kärnten
und die Steiermark erledigt EBZ diese Abfrage im Erstgespräch.</p>
{A.box("Die Zählpunktnummer ist eine 33-stellige Kennung, die mit AT beginnt. Sie steht auf der Netzrechnung, auf "
       "der Jahresabrechnung und im Kundenportal des Netzbetreibers.", label="Zählpunktnummer:")}
"""),
        ("Weg 2: Plattformen und Anbieter", "weg-plattform", f"""
<p>Die großen Abrechnungsplattformen kennen alle Gemeinschaften, die sie betreuen, und können anhand Ihres
Zählpunkts prüfen, ob eine davon im Nahbereich liegt. energyfamily betreut rund 330 Gemeinschaften mit rund
15.000 registrierten Nutzern und ist der Abrechnungspartner von EBZ. Weitere Anlaufstellen sind die Angebote der
Landesenergieversorger (Kelag, Energie Steiermark) und regionale Genossenschaften. Der Vorteil der Plattformsuche:
Sie bekommen nicht nur die Gemeinschaft, sondern auch die Abrechnung. Der Nachteil: Jede Plattform zeigt nur ihre
eigenen Gemeinschaften.</p>
{A.table(
    ["Suchweg", "Vorteil", "Grenze"],
    [
        ["Netzbetreiber-Abfrage", "verbindliche Nahbereichskennung", "nennt keine Gemeinschaften"],
        ["Plattform (z. B. energyfamily)", "Gemeinschaft plus Abrechnung in einem", "zeigt nur eigene Gemeinschaften"],
        ["Gemeinde, Energieberatung", "kennt lokale Vereinsgemeinschaften", "oft nur eine Gemeinschaft im Ort"],
        ["Fachbetrieb (EBZ)", "prüft Zählpunkt, Anlage und Gemeinschaft zusammen",
         "Montage auf Kärnten und Steiermark begrenzt, EG-Anbindung österreichweit"],
    ],
)}
"""),
        ("Weg 3: Gemeinde und regionale Energieberatung", "weg-gemeinde", f"""
<p>Viele Energiegemeinschaften in Kärnten und der Steiermark sind von Gemeinden, Klimabündnis-Gemeinden oder
engagierten Bürgerinnen und Bürgern als Verein gegründet worden. Diese Gemeinschaften haben selten eine Website, die
bei Google auftaucht, aber die Gemeinde kennt sie. Fragen Sie am Gemeindeamt nach, lesen Sie die Gemeindezeitung
oder kontaktieren Sie die Koordinationsstelle für Energiegemeinschaften (energiegemeinschaften.gv.at), die regionale
Ansprechpartner vermittelt. In der Steiermark sind zusätzlich die Energieagentur und die Klima- und
Energiemodellregionen gute Anlaufstellen. Regionale Details finden Sie in den Artikeln
{a('/energiegemeinschaft-kaernten/', 'Energiegemeinschaft Kärnten')} und
{a('/energiegemeinschaft-steiermark/', 'Energiegemeinschaft Steiermark')}.</p>
{A.cta("Wir finden Ihre Energiegemeinschaft in Kärnten und der Steiermark",
       "Schicken Sie uns Ihre Zählpunktnummer. Wir prüfen den Nahbereich und sagen Ihnen, welche Gemeinschaft passt "
       "oder ob sich eine Neugründung anbietet.",
       secondary=("eg_rechner", "Ersparnis berechnen"))}
"""),
        ("Woran Sie eine gute Energiegemeinschaft erkennen", "pruefpunkte", f"""
<p>Gefunden heißt noch nicht passend. Bevor Sie beitreten, prüfen Sie fünf Punkte:</p>
<ol>
  <li><b>Verhältnis von Erzeugern und Abnehmern:</b> Es sollte ausgewogen sein, sonst bleibt die Zuordnungsquote
  niedrig.</li>
  <li><b>Aufteilungsschlüssel:</b> Dynamisch ist in fast allen Fällen besser als statisch.</li>
  <li><b>Preise:</b> Ein fester Einspeise- und Bezugspreis ist transparenter als einer, der am OeMAG-Tarif hängt.</li>
  <li><b>Abrechnung:</b> Monatlich per App statt jährlich per Hand.</li>
  <li><b>Kündigungsfrist:</b> Ein bis drei Monate sind fair, Jahresbindungen sind es nicht.</li>
</ol>
<p>Welche Gebührenmodelle üblich sind, steht im Artikel
{a('/energiegemeinschaft-kosten/', 'Was eine Energiegemeinschaft kostet')}, die Einschränkungen im Artikel
{a('/energiegemeinschaft-nachteile/', 'Energiegemeinschaft: Nachteile')}.</p>
"""),
        ("Wenn es keine passende Gemeinschaft gibt", "keine-gemeinschaft", f"""
<p>In ländlichen Lagen, an kleinen Trafos oder in neuen Siedlungen kann es sein, dass noch keine Gemeinschaft im
Nahbereich aktiv ist. Dann gibt es drei Optionen. Die regionale Ebene erweitert den Suchradius auf das Umspannwerk,
mit kleinerem Netzentgelt-Abschlag (28 statt 57 Prozent), aber deutlich mehr potenziellen Mitgliedern. Oder Sie
gründen selbst, zusammen mit Nachbarn, dem Betrieb nebenan oder der Gemeinde. Der Aufwand ist überschaubar, wenn
eine Plattform die Abrechnung übernimmt, die Schritte stehen im Artikel
{a('/energiegemeinschaft-gruenden/', 'Energiegemeinschaft gründen')}.</p>
<p>Die dritte Option ist die Bürgerenergiegemeinschaft: Sie funktioniert österreichweit, also auch mit der Tante in
Wien oder dem Bruder in Linz, allerdings ohne den Netzentgelt-Abschlag, der an den Nahbereich gebunden ist. EBZ
bündelt Interessenten aus demselben Nahbereich, startet neue Gemeinschaften, sobald genug Erzeuger und Abnehmer
zusammenkommen, und bietet das österreichweite Teilen über energyfamily an.</p>
"""),
        ("Fazit: Energiegemeinschaft finden", "fazit", f"""
<p>Die Suche beginnt nicht bei Google, sondern bei Ihrer Zählpunktnummer. Wer den Nahbereich kennt, findet über
Plattform, Gemeinde oder Fachbetrieb schnell die passende Gemeinschaft. Und wo keine ist, lässt sich eine gründen
oder österreichweit teilen, in Kärnten und der Steiermark mit EBZ als Partner. Wie der
{a('/energiegemeinschaft-beitreten/', 'Beitritt')} danach abläuft, steht im nächsten Artikel.</p>
{A.cta("Zählpunkt schicken, Gemeinschaft finden",
       "Die Nahbereichsabfrage dauert bei uns einen Werktag. Danach wissen Sie, wo Sie mitmachen können.",
       primary=("kontakt", "Anfrage senden"), secondary=("eg_privat", "Zur Leistungsseite"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für die Suche: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und Wallboxen in "
                 "Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. Dazu kommt "
                 "die Energiegemeinschaft: Wir nehmen Sie in eine bestehende Gemeinschaft auf oder bauen mit Ihnen eine "
                 "eigene auf, abgerechnet über die Plattform unseres Partners energyfamily."),
        "grid": [
            ("Nahbereich in 1 Werktag", "Wir fragen Trafo und Umspannwerk zu Ihrem Zählpunkt ab."),
            ("Passende Gemeinschaft", "Bestehende EG im Nahbereich oder Neugründung mit Nachbarn und Gemeinde."),
            ("Österreichweit teilen", "Bürgerenergiegemeinschaft für Abnehmer außerhalb des Nahbereichs."),
            ("Abrechnung inklusive", "Zählpunktfreigabe, Aufnahme und monatliche Abrechnung über energyfamily."),
        ],
    },

    "faq": [
        ("Wie finde ich eine Energiegemeinschaft in meiner Nähe?",
         "Über drei Wege: Nahbereichsabfrage mit Ihrer Zählpunktnummer beim Netzbetreiber, Anfrage bei "
         "Abrechnungsplattformen wie energyfamily (rund 330 Gemeinschaften) oder beim Gemeindeamt und der regionalen "
         "Energieberatung. In Kärnten und der Steiermark übernimmt EBZ Energie die Suche."),
        ("Gibt es eine Karte aller Energiegemeinschaften in Österreich?",
         "Keine vollständige. Einige Plattformen zeigen ihre eigenen Gemeinschaften, die Koordinationsstelle listet "
         "Beispielprojekte. Eine Karte wäre ohnehin nur bedingt hilfreich, weil die Teilnahme vom Nahbereich des "
         "Zählpunkts abhängt, nicht von der Entfernung."),
        ("Was ist die Zählpunktnummer und wo finde ich sie?",
         "Eine 33-stellige Kennung, die mit AT beginnt und jeden Stromanschluss eindeutig identifiziert. Sie steht "
         "auf der Netzrechnung, auf der Jahresabrechnung und im Kundenportal des Netzbetreibers."),
        ("Kann ich an einer Energiegemeinschaft im Nachbarort teilnehmen?",
         "Ja, wenn der Nachbarort am selben Umspannwerk hängt (Regionalbereich). Dann gilt der Netzentgelt-Abschlag "
         "von 28 Prozent. Für den Abschlag von 57 Prozent müssen Sie am selben Trafo hängen, was über Ortsgrenzen "
         "hinweg selten ist."),
        ("Kann ich Strom mit Verwandten in einem anderen Bundesland teilen?",
         "Ja, über eine Bürgerenergiegemeinschaft, die österreichweit funktioniert. Den Netzentgelt-Abschlag gibt es "
         "dann nicht, weil er an den Nahbereich gebunden ist. EBZ bietet diese Variante über energyfamily an."),
        ("Was mache ich, wenn es in meinem Nahbereich keine Gemeinschaft gibt?",
         "Entweder auf den Regionalbereich ausweichen, selbst gründen oder österreichweit als "
         "Bürgerenergiegemeinschaft teilen. EBZ sammelt Interessenten je Nahbereich und startet neue Gemeinschaften, "
         "sobald Erzeuger und Abnehmer zusammenkommen."),
        ("Wie viele Energiegemeinschaften gibt es in Österreich?",
         "Mehr als 11.000, davon über 5.500 Erneuerbare-Energie-Gemeinschaften (Stand August 2026). Statistisch "
         "liegt damit in fast jedem Umspannwerksbereich Kärntens und der Steiermark mindestens eine aktive "
         "Gemeinschaft."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und errichtet Photovoltaik-, "
                    "Speicher- und Wärmepumpensysteme in Kärnten und der Steiermark und begleitet Kunden beim Einstieg "
                    "in Energiegemeinschaften. Inhalte werden regelmäßig anhand der Vorgaben von E-Control, OeMAG und "
                    "energiegemeinschaften.gv.at aktualisiert. Keine Rechts- oder Steuerberatung."),
    "sources": [
        ("Koordinationsstelle für Energiegemeinschaften", "https://energiegemeinschaften.gv.at/"),
        ("EVN / Netz NÖ: Schritte und Quick-Check (Beispiel)",
         "https://www.evn.at/home/energiegemeinschaften/schritte-zur-energiegemeinschaft"),
        ("energyfamily: Plattform", "https://www.energyfamily.at/"),
    ],
    "related": [
        ("/energiegemeinschaft-beitreten/", "Energiegemeinschaft beitreten"),
        ("/energiegemeinschaft-kaernten/", "Energiegemeinschaft Kärnten"),
        ("/energiegemeinschaft-steiermark/", "Energiegemeinschaft Steiermark"),
        ("eg_privat", "Energiegemeinschaft für Private mit Rechner"),
    ],
    "cta": {
        "h3": "Zählpunkt prüfen lassen",
        "text": "Nahbereichsabfrage in einem Werktag. Danach wissen Sie, welche Gemeinschaft für Sie infrage kommt.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Die passende Gemeinschaft für Ihren Zählpunkt",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Nahbereich, Anlage und "
                   "Gemeinschaft zusammen prüft."),
}
