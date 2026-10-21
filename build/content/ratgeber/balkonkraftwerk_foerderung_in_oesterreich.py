"""Ratgeber: Balkonkraftwerk-Förderung in Österreich (EAG-Ausschluss, kleinste förderfähige Anlage, Ablauf).

Migriert von ebz-photovoltaik.at/balkonkraftwerk-foerderung-in-oesterreich/ (Quelle Stand November 2025,
Förderjahr 2025). Die EAG-Konditionen 2026 wurden aus den belegten Schwesterartikeln ergänzt.
Stand ab 23.10.2026: letzter EAG-Call lief 8. bis 22.10.2026, derzeit kein Bundeszuschuss; Ausblick 2027
Systemfoerderung laut BMWET (geplant, nicht beschlossen).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "balkonkraftwerk-foerderung-in-oesterreich",
    "path": "/balkonkraftwerk-foerderung-in-oesterreich/",
    "title": "Balkonkraftwerk-Förderung Österreich: Bund und Länder | EBZ",
    "description": ("Balkonkraftwerk-Förderung Österreich: Warum Anlagen bis 800 W keinen EAG-Zuschuss bekamen, "
                    "was Länder und Gemeinden zahlen und was ab 2027 geplant ist."),
    "eyebrow": "Förderung · Balkonkraftwerk",
    "crumb_label": "Balkonkraftwerk-Förderung",
    "h1": "Balkonkraftwerk-Förderung in Österreich: kein EAG-Zuschuss bis 800 Watt, aber Alternativen",
    "lead": ("Nach dem Ende des Nullsteuersatzes am 1. April 2025 war der EAG-Investitionszuschuss die zentrale "
             "Bundesförderung für Photovoltaik, der letzte Call lief vom 8. bis 22. Oktober 2026. Ein klassisches "
             "Balkonkraftwerk ging dabei leer aus, weil ihm der Einspeisezählpunkt fehlt. Dieser Ratgeber erklärt "
             "den Grund, die Förderungen der Länder und Gemeinden und die kleinste förderfähige Alternative."),
    "chips": [
        "Balkonkraftwerk bis <b>800 W</b>: kein EAG",
        "Nullsteuersatz: <b>Ende 1. April 2025</b>",
        "EAG Kat. A im Call 2026: <b>150 €/kWp</b>",
        "Letzter Call: <b>8. bis 22. Oktober 2026</b>, beendet",
    ],
    "date_published": "2025-08-20",
    "date_modified": "2026-10-21",
    "hero_img": "balkon",
    "hero_alt": "Balkonkraftwerk mit zwei Solarmodulen am Balkongeländer eines Wohnhauses",

    "tldr": [
        "Ein Standard-Balkonkraftwerk bis 800 Watt bekommt keinen EAG-Investitionszuschuss. Grund: Es läuft im "
        "vereinfachten Meldeverfahren beim Netzbetreiber und erhält keinen eigenen Einspeisezählpunkt, den die "
        "EAG-Abwicklungsstelle zwingend verlangt.",
        "Der Nullsteuersatz (0 Prozent Umsatzsteuer) für PV-Anlagen endete am 31. März 2025. Seit 1. April 2025 "
        "gilt wieder der reguläre Steuersatz; die Bundesförderung lief 2026 über den EAG-Zuschuss.",
        "Kleinste förderfähige Alternative im Call 2026: jede PV-Anlage, die formell beim Netzbetreiber angemeldet "
        "wird und einen Einspeisezählpunkt erhält, praktisch eine kleine, fest installierte Dach-, Terrassen- oder "
        "Gartenanlage in Kategorie A (bis 10 kWp) mit 150 Euro je kWp.",
        "Fördercalls 2026: 23. April bis 11. Mai, 16. bis 30. Juni, 8. bis 22. Oktober. Der letzte endete am "
        "22. Oktober 2026, derzeit ist kein Bundeszuschuss beantragbar. Ab 2027 ist laut BMWET eine "
        "Systemförderung für Speicher mit intelligenter Steuerung geplant, nicht beschlossen.",
        "Länder und Gemeinden haben teils eigene Programme, die auch Balkonkraftwerke einschließen können. Ein "
        "Blick auf Landes- und Gemeindeebene lohnt sich, bevor Sie kaufen.",
    ],
    "kpis": [
        ("800 W", "Grenze für Balkonkraftwerke im vereinfachten Meldeverfahren"),
        ("0 €", "EAG-Bundeszuschuss für ein Standard-Balkonkraftwerk"),
        ("150 €/kWp", "EAG-Zuschuss im Call 2026 für angemeldete PV-Anlagen bis 10 kWp"),
        ("22.10.2026", "Ende des letzten EAG-Fördercalls 2026"),
    ],

    "sections": [
        ("Warum ein Balkonkraftwerk keinen EAG-Zuschuss bekommt", "eag-ausschluss", f"""
<p><b>Ein Balkonkraftwerk darf in Österreich bis 800 Watt Wechselrichterleistung ohne Genehmigung betrieben
werden.</b> Es muss mindestens 14 Tage vor Inbetriebnahme beim örtlichen Netzbetreiber gemeldet werden
(Kleinsterzeugungsanlage laut E-Control). Eine eigene Bundesförderung gibt es nicht, der EAG-Zuschuss griff
2026 erst bei Anlagen mit Einspeisezählpunkt; seit dem Ende des letzten Calls am 22. Oktober 2026 ist er
derzeit gar nicht beantragbar. Welche Geräte EBZ Energie anbietet, zeigt die
Leistungsseite {a('balkonkraftwerke', 'Balkonkraftwerk')}.</p>
<p>Der EAG-Investitionszuschuss war 2026 eine direkte, nicht rückzahlbare Beihilfe für die Neuerrichtung oder
Erweiterung von Photovoltaikanlagen. Er deckte Module, Wechselrichter und optional einen Stromspeicher ab, wenn
dieser gemeinsam mit der Anlage installiert wurde. Die entscheidende Voraussetzung: Die Anlage musste über einen
eigenen, vom Netzbetreiber vergebenen Einspeisezählpunkt verfügen.</p>
<p>Genau daran scheitert das Balkonkraftwerk. Eine Steckeranlage bis 800 Watt gilt als Kleinsterzeugungsanlage
und durchläuft ein vereinfachtes Meldeverfahren beim Netzbetreiber, bei dem typischerweise kein
Einspeisezählpunkt vergeben wird. Die EAG-Abwicklungsstelle bestätigt das unmissverständlich: Anlagen ohne
eigenen Einspeisezählpunkt sind nicht förderfähig. Die Bundesförderung zielte auf formell registrierte
PV-Anlagen, nicht auf Plug-and-Play-Lösungen.</p>
{A.box("Der Nullsteuersatz für PV-Anlagen war eine befristete Maßnahme und endete vorzeitig mit 31. März "
       "2025. Seit 1. April 2025 gilt wieder der reguläre Umsatzsteuersatz, auch für Balkonkraftwerke.",
       label="Hinweis:")}
"""),
        ("So funktionierte der EAG-Investitionszuschuss 2026", "eag-zuschuss", f"""
<p>Das EAG teilt PV-Anlagen nach Leistung in vier Kategorien. Für private Anlagen war Kategorie A relevant:
alle Anlagen bis 10 kWp. Die Fördersätze wurden mit der EAG-Novelle 2026 neu fixiert und galten im Call 2026;
derzeit sind sie nicht beantragbar:</p>
{A.table(
    ["Kategorie", "Anlagengröße", "Fördersatz 2026", "Fördersatz 2025"],
    [
        ["A", "bis 10 kWp", "150 €/kWp", "160 €/kWp"],
        ["B", "über 10 bis 20 kWp", "140 €/kWp", "je Call festgelegt"],
        ["Speicher (nur mit neuer PV)", "bis 50 kWh", "150 €/kWh", "150 €/kWh"],
    ],
    hl_cols=(2,),
)}
<p>Die Vergabe erfolgt in zeitlich begrenzten Fördercalls. 2025 waren es drei Calls (23. April bis 8. Mai,
23. Juni bis 7. Juli, 8. bis 22. Oktober), 2026 ebenfalls drei: 23. April bis 11. Mai, 16. bis 30. Juni und
8. bis 22. Oktober. In Kategorie A galt First-Come-First-Served: Anträge wurden streng nach Eingang bearbeitet,
bis das Budget des Calls erschöpft war.</p>
<p><b>Stand ab 23. Oktober 2026:</b> Der dritte Call lief vom 8. bis 22. Oktober 2026 und war der letzte im
bisherigen System. Neue Anlagen bekommen derzeit keinen Bundeszuschuss. Ab 2027 ist laut Eckpunkten des
BMWET eine Systemförderung geplant, aber nicht beschlossen: Antrag nach Installation und Rechnung statt
Fördercall, gefördert werden sollen Speicher mit intelligenter Steuerung, auch als Nachrüstung; Projekte mit
intelligentem Speicher, die ab 1. November 2026 in Betrieb gehen, sollen 2027 beantragbar sein. Höhe und
Technikkriterien sind noch offen.</p>
<p>Der <b>Made-in-Europe-Bonus</b> war seit dem zweiten Call 2025 (23. Juni 2025) verfügbar: Für Module und
Wechselrichter mit nachgewiesener europäischer Wertschöpfung stieg der Zuschuss um bis zu 20 Prozent, für den
Speicher um weitere 10 Prozent. Alle Details im Ratgeber
{a('/foerderung-fuer-pv-speicher/', 'Förderung für PV-Speicher in Österreich')}.</p>
<p><small>Sätze 2026: EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026, gültig für die Calls 2026 (beendet).
Werte 2025 laut Quelle vom November 2025.</small></p>
"""),
        ("Die Alternative: die kleinste förderfähige PV-Anlage", "alternative", f"""
<p>Da ein typisches Balkonkraftwerk nicht für den EAG-Zuschuss qualifizierte, stellt sich die Frage nach der
Alternative. Die Antwort im Call 2026: Jede Photovoltaikanlage, unabhängig von ihrer Größe, die den formellen
Anmeldeprozess durchlief und einen eigenen Einspeisezählpunkt erhielt, war grundsätzlich förderfähig.</p>
<p>Statt des vereinfachten Meldeverfahrens stellen Sie einen regulären Netzzugangsantrag beim Netzbetreiber.
Das ist aufwendiger und erfordert einen konzessionierten Elektrofachbetrieb, der die Anlage installiert und
abnimmt. Theoretisch ginge das auch für eine Anlage knapp über 0,8 kWp. In der Praxis machen die Kosten für
Planung und Installation den formellen Weg erst bei einer kleinen, fest installierten Dachanlage oder einer
professionell angebundenen Anlage auf Terrasse oder im Garten sinnvoll. Diese fiel in Kategorie A und erhielt
im Call 2026 den vollen Zuschuss. Derzeit ist kein Bundeszuschuss beantragbar; die für 2027 laut BMWET geplante
Systemförderung soll auf Speicher mit intelligenter Steuerung ausgerichtet sein (nicht beschlossen, Kriterien
offen). Wer jetzt eine kleine Dachanlage plant, baut daher sinnvoll mit Speicher und Energiemanagement.</p>
{A.table(
    ["Kriterium", "Balkonkraftwerk (bis 800 W)", "Kleine angemeldete PV-Anlage"],
    [
        ["Anmeldung", "vereinfachtes Meldeverfahren", "regulärer Netzzugangsantrag, Elektrofachbetrieb"],
        ["Einspeisezählpunkt", "in der Regel nein", "ja, 33-stellige Bezeichnung beginnend mit AT"],
        ["EAG-Zuschuss im Call 2026", "nein", "150 €/kWp, Speicher 150 €/kWh (derzeit nicht beantragbar)"],
        ["Speicher förderfähig (Call 2026)", "nein", "ja, gemeinsam mit der neuen Anlage"],
        ["Typische Größe", "0,8 kWp", "3 bis 10 kWp"],
    ],
    hl_cols=(2,),
)}
<p>Was eine solche Anlage kostet und bringt, zeigt der Ratgeber {a('/kosten-einer-solaranlage/', 'Kosten einer Solaranlage')};
zur Einordnung: 10 kWp mit Speicher liegen bei EBZ Energie bei rund 15.000 bis 22.000 Euro vor Förderung. Wer
beim Balkonkraftwerk bleibt, findet auf der Leistungsseite {a('balkonkraftwerke', 'Balkonkraftwerke')} die
Modelle und Voraussetzungen.</p>
{A.cta("Balkonkraftwerk oder kleine Dachanlage?",
       "Wir rechnen beide Varianten für Ihren Haushalt durch, inklusive Förderung, und sagen ehrlich, was sich "
       "bei Ihnen lohnt.",
       secondary=("balkonkraftwerke", "Zu den Balkonkraftwerken"))}
"""),
        ("Förderungen der Länder und Gemeinden für Balkonkraftwerke", "laender", f"""
<p>Unabhängig vom Bund bieten mehrere Länder und Gemeinden eigene Zuschüsse an, die unter Umständen auch
Balkonkraftwerke einschließen. Die Programme ändern sich häufig und sind oft budgetiert; prüfen Sie daher vor
dem Kauf die Website Ihres Bundeslandes und Ihrer Gemeinde. Für größere PV-Anlagen mit Speicher haben die
Länder 2026 eigene Schienen, etwa Kärnten mit 3.000 Euro Pauschale für PV ab 5 kWp mit Speicher ab 5 kWh.
Den Überblick gibt der Ratgeber {a('/photovoltaik-landesfoerderungen/', 'PV-Landesförderungen aller Bundesländer')},
für Kärnten im Detail {a('/photovoltaik-foerderung-kaernten/', 'Photovoltaik-Förderung Kärnten 2026')}.</p>
<p>Wichtig bei Kombinationen: Der EAG-Zuschuss konnte im Call 2026 nicht mit anderen Bundesförderungen
kombiniert werden. Eine Kumulierung mit Landes- oder Gemeindeförderungen war dagegen oft ausdrücklich erlaubt,
je nach Richtlinie des Landes.</p>
"""),
        ("Schritt für Schritt zum EAG-Zuschuss für eine kleine PV-Anlage", "ablauf", f"""
<p>So lief der Antrag im Call 2026. Derzeit ist kein Bundesantrag möglich; für die geplante Systemförderung
2027 soll der Antrag laut BMWET erst nach Installation und Rechnung kommen (nicht beschlossen).</p>
{A.steps([
    ("Einspeisezählpunkt beantragen",
     "Die 33-stellige Zählpunktbezeichnung beginnend mit „AT“ ist die Eintrittskarte. Sie wird beim lokalen "
     "Netzbetreiber beantragt und kann einige Zeit dauern. Ohne sie ist kein Antrag möglich."),
    ("Unterlagen vorbereiten",
     "Datenblätter der Module (kWp) und des Wechselrichters, Angebot des Fachbetriebs, gegebenenfalls "
     "Speicherdaten (kWh) bereitlegen."),
    ("Ticket ziehen",
     "Zum Call-Start (typischerweise 17:00 Uhr) im Portal der EAG-Abwicklungsstelle ein digitales Ticket "
     "ziehen. In Kategorie A entschied der Zeitstempel über die Reihung."),
    ("Antrag vervollständigen",
     "Nach der Ticketziehung blieb bis zum Ende des Calls Zeit, den Online-Antrag auszufüllen und alle "
     "Dokumente hochzuladen."),
    ("Installation nach der Zusage",
     "Fachgerechte Installation durch einen befugten Fachbetrieb, dann Inbetriebnahme und Endabrechnung."),
])}
{A.box_dark("Voraussetzungen im Call 2026",
    "Antrag vor Inbetriebnahme, eigener Einspeisezählpunkt, Installation durch einen befugten Fachbetrieb, keine "
    "zweite Bundesförderung für dieselbe Anlage. Ein Speicher wurde nur gefördert, wenn er gemeinsam mit der "
    "neuen oder erweiterten PV-Anlage installiert wurde.")}
"""),
        ("Fazit: Förderung als Chance für den größeren Schritt", "fazit", f"""
<p>Die Enttäuschung ist verständlich: Das unkomplizierte Balkonkraftwerk blieb beim Bund außen vor. Das
EAG-System bot 2026 dafür eine klare Förderung für alle, die in eine formell angemeldete PV-Anlage
investierten, auch in eine kleine; der letzte Call endete am 22. Oktober 2026. Für Balkonkraftwerk-Besitzer
lohnt sich der Blick auf Land und Gemeinde. Wer ohnehin über mehr als 800 Watt nachdenkt, fährt mit einer
kleinen Dachanlage mit Speicher und Energiemanagement oft besser: In Kärnten gibt es dafür 3.000 Euro
Landespauschale, und laut BMWET ist ab 2027 eine Systemförderung für solche Speicher geplant (nicht beschlossen).</p>
{A.cta("Kleine PV-Anlage mit Förderung planen",
       "Kostenlose Erstberatung, Zählpunkt und Förderanträge aus einer Hand, Montage durch zertifizierte "
       "Fachkräfte in Kärnten und der Steiermark.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("photovoltaik", "Zur Photovoltaik"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Förderung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher und Balkonkraftwerke in "
                 "Kärnten und der Steiermark, mit zertifizierten Fachkräften und "
                 "über 300 dokumentierten Projekten. Wir prüfen die Förderfähigkeit Ihres Projekts, beantragen den "
                 "Zählpunkt beim Netzbetreiber und reichen die Landesförderung fristgerecht ein."),
        "grid": [
            ("Ehrliche Empfehlung", "Balkonkraftwerk oder kleine Dachanlage: Wir rechnen beides durch."),
            ("Zählpunkt und Antrag", "Netzzugangsantrag und Förderanträge übernehmen wir."),
            ("Normgerechte Montage", "Installation und Abnahme durch befugte Fachkräfte."),
            ("Speicher mitplanen", "Kärnten zahlt 3.000 € nur mit Speicher, 2027 Systemförderung geplant."),
        ],
    },

    "faq": [
        ("Kann ich die Bundesförderung für ein Balkonkraftwerk beantragen?",
         "Nein. Ein Standard-Balkonkraftwerk bis 800 Watt war vom EAG-Investitionszuschuss ausgeschlossen, weil "
         "für den Antrag ein eigener Einspeisezählpunkt nötig war, den ein Balkonkraftwerk im vereinfachten "
         "Meldeverfahren in der Regel nicht erhält. Seit dem Ende des letzten Calls am 22. Oktober 2026 ist "
         "derzeit ohnehin kein Bundeszuschuss beantragbar."),
        ("Was ist die kleinste PV-Anlage, die gefördert werden kann?",
         "Im Call 2026 jede Anlage, die formell beim Netzbetreiber angemeldet wurde und einen Einspeisezählpunkt "
         "erhielt, theoretisch schon ab knapp über 0,8 kWp. Praktisch lohnte der Aufwand erst bei einer kleinen, "
         "fest installierten Dachanlage in Kategorie A mit 150 Euro je kWp. Derzeit ist kein Bundeszuschuss "
         "beantragbar."),
        ("Gibt es Landes- oder Gemeindeförderungen für Balkonkraftwerke?",
         "Teilweise. Mehrere Länder und Gemeinden haben eigene Programme, die auch Steckeranlagen einschließen "
         "können. Sie ändern sich häufig und sind budgetiert. Prüfen Sie vor dem Kauf die Website Ihres Landes und "
         "Ihrer Gemeinde."),
        ("Gibt es nach dem Call im Oktober 2026 einen weiteren Fördercall?",
         "Nein. Der dritte und letzte Call 2026 lief vom 8. bis 22. Oktober 2026, im bisherigen System gibt es "
         "keinen weiteren Call. Projekte mit intelligentem Speicher, die ab 1. November 2026 in Betrieb gehen, "
         "sollen laut BMWET 2027 in der geplanten Systemförderung beantragbar sein (nicht beschlossen)."),
        ("Endet die Photovoltaik-Förderung?",
         "Die Investitionsförderung im bisherigen System ist mit dem Call bis 22. Oktober 2026 abgeschlossen, 2026 "
         "galten 150 Euro je kWp in Kategorie A. Ab 2027 ist laut BMWET eine Systemförderung für Speicher mit "
         "intelligenter Steuerung geplant, Antrag nach Installation; beschlossen ist sie nicht, die Höhe ist offen."),
        ("Brauche ich für die Förderung einen Stromspeicher?",
         "Im Call 2026 nicht, der Zuschuss ließ sich auch nur für die PV-Anlage beantragen, ein Speicher brachte "
         "150 Euro je kWh. Aktuell schon: Die Kärntner Landespauschale von 3.000 Euro gibt es nur mit Speicher ab "
         "5 kWh, und die für 2027 geplante Systemförderung soll laut BMWET Speicher mit intelligenter Steuerung "
         "fördern."),
        ("Wie bekomme ich den Einspeisezählpunkt?",
         "Sie beantragen ihn beim lokalen Netzbetreiber im Rahmen eines regulären Netzzugangsantrags. Die "
         "33-stellige Bezeichnung beginnt mit „AT“. Da der Prozess einige Zeit dauert, sollte er der erste "
         "Schritt in der Planung sein."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team hat über 300 PV-Projekte in sechs "
                    "Bundesländern umgesetzt, von der kleinen Dachanlage bis zur Gewerbeanlage. Die Inhalte werden "
                    "anhand der Richtlinien der EAG-Abwicklungsstelle aktualisiert. Keine Rechts- oder Steuerberatung, "
                    "maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("EAG-Abwicklungsstelle (OeMAG)", "https://www.eag-abwicklungsstelle.at/"),
        ("Klima- und Energiefonds", "https://www.klimafonds.gv.at/"),
    ],
    "related": [
        ("balkonkraftwerke", "Balkonkraftwerke: Modelle und Voraussetzungen"),
        ("/foerderung-fuer-pv-speicher/", "Förderung für PV-Speicher in Österreich"),
        ("/photovoltaik-landesfoerderungen/", "PV-Landesförderungen: alle 9 Bundesländer"),
        ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage"),
    ],
    "cta": {
        "h3": "Förderung richtig nutzen",
        "text": "Wir sagen Ihnen, ob Balkonkraftwerk oder kleine Dachanlage bei Ihnen mehr bringt.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Eigener Sonnenstrom, richtig gefördert",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
