"""Ratgeber: Balkonkraftwerk-Förderung in Österreich (EAG-Ausschluss, kleinste förderfähige Anlage, Ablauf).

Migriert von ebz-photovoltaik.at/balkonkraftwerk-foerderung-in-oesterreich/ (Quelle Stand November 2025,
Förderjahr 2025). Die EAG-Konditionen 2026 wurden aus den belegten Schwesterartikeln ergänzt.
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
    "description": ("Balkonkraftwerk-Förderung in Österreich: Warum Steckeranlagen bis 800 W keinen EAG-Zuschuss "
                    "bekommen, was Länder und Gemeinden zahlen, wann 150 €/kWp fließen."),
    "eyebrow": "Förderung · Balkonkraftwerk",
    "crumb_label": "Balkonkraftwerk-Förderung",
    "h1": "Balkonkraftwerk-Förderung in Österreich: kein EAG-Zuschuss bis 800 Watt, aber Alternativen",
    "lead": ("Seit dem Ende des Nullsteuersatzes am 1. April 2025 ist der EAG-Investitionszuschuss die zentrale "
             "Bundesförderung für Photovoltaik. Ein klassisches Balkonkraftwerk geht dabei leer aus, weil ihm der "
             "Einspeisezählpunkt fehlt. Dieser Ratgeber erklärt den Grund, die Förderungen der Länder und "
             "Gemeinden und die kleinste förderfähige Alternative."),
    "chips": [
        "Balkonkraftwerk bis <b>800 W</b>: kein EAG",
        "Nullsteuersatz: <b>Ende 1. April 2025</b>",
        "EAG Kat. A: <b>150 €/kWp</b> (2026)",
        "Speicher: <b>150 €/kWh</b> mit neuer PV",
    ],
    "date_published": "2025-08-20",
    "date_modified": "2026-09-24",
    "hero_img": "balkon",
    "hero_alt": "Balkonkraftwerk mit zwei Solarmodulen am Balkongeländer eines Wohnhauses",

    "tldr": [
        "Ein Standard-Balkonkraftwerk bis 800 Watt bekommt keinen EAG-Investitionszuschuss. Grund: Es läuft im "
        "vereinfachten Meldeverfahren beim Netzbetreiber und erhält keinen eigenen Einspeisezählpunkt, den die "
        "EAG-Abwicklungsstelle zwingend verlangt.",
        "Der Nullsteuersatz (0 Prozent Umsatzsteuer) für PV-Anlagen endete am 31. März 2025. Seit 1. April 2025 "
        "gilt wieder der reguläre Steuersatz; die Bundesförderung läuft über den EAG-Zuschuss.",
        "Kleinste förderfähige Alternative: jede PV-Anlage, die formell beim Netzbetreiber angemeldet wird und "
        "einen Einspeisezählpunkt erhält. Praktisch ist das eine kleine, fest installierte Dach-, Terrassen- oder "
        "Gartenanlage in Kategorie A (bis 10 kWp) mit 150 Euro je kWp (2026).",
        "Fördercalls 2026: 23. April bis 11. Mai, 16. bis 30. Juni, ab 8. Oktober. In Kategorie A gilt "
        "First-Come-First-Served mit Ticketziehung; der Antrag muss vor Inbetriebnahme gestellt werden.",
        "Länder und Gemeinden haben teils eigene Programme, die auch Balkonkraftwerke einschließen können. Ein "
        "Blick auf Landes- und Gemeindeebene lohnt sich, bevor Sie kaufen.",
    ],
    "kpis": [
        ("800 W", "Grenze für Balkonkraftwerke im vereinfachten Meldeverfahren"),
        ("0 €", "EAG-Bundeszuschuss für ein Standard-Balkonkraftwerk"),
        ("150 €/kWp", "EAG-Zuschuss 2026 für angemeldete PV-Anlagen bis 10 kWp"),
        ("3 Calls", "EAG-Fördercalls 2026, Antrag vor Inbetriebnahme"),
    ],

    "sections": [
        ("Warum ein Balkonkraftwerk keinen EAG-Zuschuss bekommt", "eag-ausschluss", f"""
<p>Der EAG-Investitionszuschuss ist eine direkte, nicht rückzahlbare Beihilfe für die Neuerrichtung oder
Erweiterung von Photovoltaikanlagen. Er deckt Module, Wechselrichter und optional einen Stromspeicher ab, wenn
dieser gemeinsam mit der Anlage installiert wird. Die entscheidende Voraussetzung: Die Anlage muss über einen
eigenen, vom Netzbetreiber vergebenen Einspeisezählpunkt verfügen.</p>
<p>Genau daran scheitert das Balkonkraftwerk. Eine Steckeranlage bis 800 Watt gilt als Kleinsterzeugungsanlage
und durchläuft ein vereinfachtes Meldeverfahren beim Netzbetreiber, bei dem typischerweise kein
Einspeisezählpunkt vergeben wird. Die EAG-Abwicklungsstelle bestätigt das unmissverständlich: Anlagen ohne
eigenen Einspeisezählpunkt sind nicht förderfähig. Die Bundesförderung zielt auf formell registrierte
PV-Anlagen, nicht auf Plug-and-Play-Lösungen.</p>
{A.box("Der Nullsteuersatz für PV-Anlagen war eine befristete Maßnahme und endete vorzeitig mit 31. März "
       "2025. Seit 1. April 2025 gilt wieder der reguläre Umsatzsteuersatz, auch für Balkonkraftwerke.",
       label="Hinweis:")}
"""),
        ("So funktioniert der EAG-Investitionszuschuss", "eag-zuschuss", f"""
<p>Das EAG teilt PV-Anlagen nach Leistung in vier Kategorien. Für private Anlagen ist Kategorie A relevant:
alle Anlagen bis 10 kWp. Die Fördersätze wurden mit der EAG-Novelle 2026 neu fixiert:</p>
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
ab 8. Oktober. In Kategorie A gilt First-Come-First-Served: Anträge werden streng nach Eingang bearbeitet,
bis das Budget des Calls erschöpft ist.</p>
<p>Der <b>Made-in-Europe-Bonus</b> ist seit dem zweiten Call 2025 (23. Juni 2025) verfügbar: Für Module und
Wechselrichter mit nachgewiesener europäischer Wertschöpfung steigt der Zuschuss um bis zu 20 Prozent, für den
Speicher um weitere 10 Prozent. Alle Details im Ratgeber
{a('/foerderung-fuer-pv-speicher/', 'Förderung für PV-Speicher in Österreich')}.</p>
<p><small>Stand: Juni 2026 (EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026). Werte 2025 laut Quelle vom
November 2025.</small></p>
"""),
        ("Die Alternative: die kleinste förderfähige PV-Anlage", "alternative", f"""
<p>Da ein typisches Balkonkraftwerk nicht für den EAG-Zuschuss qualifiziert, stellt sich die Frage nach der
Alternative. Die Antwort: Jede Photovoltaikanlage, unabhängig von ihrer Größe, die den formellen
Anmeldeprozess durchläuft und einen eigenen Einspeisezählpunkt erhält, ist grundsätzlich förderfähig.</p>
<p>Statt des vereinfachten Meldeverfahrens stellen Sie einen regulären Netzzugangsantrag beim Netzbetreiber.
Das ist aufwendiger und erfordert einen konzessionierten Elektrofachbetrieb, der die Anlage installiert und
abnimmt. Theoretisch ginge das auch für eine Anlage knapp über 0,8 kWp. In der Praxis machen die Kosten für
Planung und Installation den formellen Weg erst bei einer kleinen, fest installierten Dachanlage oder einer
professionell angebundenen Anlage auf Terrasse oder im Garten sinnvoll. Diese fällt in Kategorie A und erhält
den vollen Zuschuss.</p>
{A.table(
    ["Kriterium", "Balkonkraftwerk (bis 800 W)", "Kleine angemeldete PV-Anlage"],
    [
        ["Anmeldung", "vereinfachtes Meldeverfahren", "regulärer Netzzugangsantrag, Elektrofachbetrieb"],
        ["Einspeisezählpunkt", "in der Regel nein", "ja, 33-stellige Bezeichnung beginnend mit AT"],
        ["EAG-Zuschuss", "nein", "150 €/kWp (2026), Speicher 150 €/kWh"],
        ["Speicher förderfähig", "nein", "ja, gemeinsam mit der neuen Anlage"],
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
<p>Wichtig bei Kombinationen: Der EAG-Zuschuss kann nicht mit anderen Bundesförderungen kombiniert werden. Eine
Kumulierung mit Landes- oder Gemeindeförderungen ist dagegen oft ausdrücklich erlaubt, je nach Richtlinie des
Landes.</p>
"""),
        ("Schritt für Schritt zum EAG-Zuschuss für eine kleine PV-Anlage", "ablauf", f"""
{A.steps([
    ("Einspeisezählpunkt beantragen",
     "Die 33-stellige Zählpunktbezeichnung beginnend mit „AT“ ist die Eintrittskarte. Sie wird beim lokalen "
     "Netzbetreiber beantragt und kann einige Zeit dauern. Ohne sie ist kein Antrag möglich."),
    ("Unterlagen vorbereiten",
     "Datenblätter der Module (kWp) und des Wechselrichters, Angebot des Fachbetriebs, gegebenenfalls "
     "Speicherdaten (kWh) bereitlegen."),
    ("Ticket ziehen",
     "Zum Call-Start (typischerweise 17:00 Uhr) im Portal der EAG-Abwicklungsstelle ein digitales Ticket "
     "ziehen. In Kategorie A entscheidet der Zeitstempel über die Reihung."),
    ("Antrag vervollständigen",
     "Nach der Ticketziehung bleibt bis zum Ende des Calls Zeit, den Online-Antrag auszufüllen und alle "
     "Dokumente hochzuladen."),
    ("Installation nach der Zusage",
     "Fachgerechte Installation durch einen befugten Fachbetrieb, dann Inbetriebnahme und Endabrechnung."),
])}
{A.box_dark("Voraussetzungen im Überblick",
    "Antrag vor Inbetriebnahme, eigener Einspeisezählpunkt, Installation durch einen befugten Fachbetrieb, keine "
    "zweite Bundesförderung für dieselbe Anlage. Ein Speicher wird nur gefördert, wenn er gemeinsam mit der "
    "neuen oder erweiterten PV-Anlage installiert wird.")}
"""),
        ("Fazit: Förderung als Chance für den größeren Schritt", "fazit", f"""
<p>Die Enttäuschung ist verständlich: Das unkomplizierte Balkonkraftwerk bleibt beim Bund außen vor. Das
EAG-System bietet dafür eine klare, planbare Förderung für alle, die in eine formell angemeldete PV-Anlage
investieren, auch in eine kleine. Für Balkonkraftwerk-Besitzer lohnt sich der Blick auf Land und Gemeinde.
Wer ohnehin über mehr als 800 Watt nachdenkt, fährt mit einer kleinen Dachanlage inklusive Zuschuss und
optionalem Speicher oft besser.</p>
{A.cta("Kleine PV-Anlage mit Förderung planen",
       "Kostenlose Erstberatung, Zählpunkt und EAG-Antrag aus einer Hand, Montage durch zertifizierte "
       "Fachkräfte in Kärnten und der Steiermark.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("photovoltaik", "Zur Photovoltaik"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Förderung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher und Balkonkraftwerke in "
                 "Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften und "
                 "über 300 dokumentierten Projekten. Wir prüfen die Förderfähigkeit Ihres Projekts, beantragen den "
                 "Zählpunkt beim Netzbetreiber und reichen den EAG-Antrag pünktlich im Fördercall ein."),
        "grid": [
            ("Ehrliche Empfehlung", "Balkonkraftwerk oder kleine Dachanlage: Wir rechnen beides durch."),
            ("Zählpunkt und Antrag", "Netzzugangsantrag, Ticketziehung und Antrag im Call übernehmen wir."),
            ("Normgerechte Montage", "Installation und Abnahme durch befugte Fachkräfte."),
            ("Speicher mitplanen", "150 € je kWh vom Bund, nur bei gemeinsamer Errichtung mit der Anlage."),
        ],
    },

    "faq": [
        ("Kann ich die Bundesförderung für ein Balkonkraftwerk beantragen?",
         "Nein. Ein Standard-Balkonkraftwerk bis 800 Watt ist vom EAG-Investitionszuschuss ausgeschlossen, weil "
         "für den Antrag ein eigener Einspeisezählpunkt nötig ist, den ein Balkonkraftwerk im vereinfachten "
         "Meldeverfahren in der Regel nicht erhält."),
        ("Was ist die kleinste PV-Anlage, die gefördert werden kann?",
         "Jede Anlage, die formell beim Netzbetreiber angemeldet wird und einen Einspeisezählpunkt erhält, "
         "theoretisch schon ab knapp über 0,8 kWp. Praktisch lohnt der Aufwand erst bei einer kleinen, fest "
         "installierten Dachanlage in Kategorie A mit 150 Euro je kWp (2026)."),
        ("Gibt es Landes- oder Gemeindeförderungen für Balkonkraftwerke?",
         "Teilweise. Mehrere Länder und Gemeinden haben eigene Programme, die auch Steckeranlagen einschließen "
         "können. Sie ändern sich häufig und sind budgetiert. Prüfen Sie vor dem Kauf die Website Ihres Landes und "
         "Ihrer Gemeinde."),
        ("Was passiert, wenn der Fördertopf bei einem Fördercall leer ist?",
         "Sie können den Antrag im nächsten Call erneut stellen. Abgelehnte Anträge von Privatpersonen kann die "
         "EAG-Abwicklungsstelle mit Zustimmung an den Klima- und Energiefonds weiterleiten, was eine zusätzliche "
         "Chance auf einen Zuschuss bietet."),
        ("Endet die Photovoltaik-Förderung bald?",
         "Nein. Das Erneuerbaren-Ausbau-Gesetz ist langfristig angelegt und soll den Ausbau bis 2030 und darüber "
         "hinaus steuern. Die Konditionen werden jährlich angepasst, 2026 etwa auf 150 Euro je kWp in "
         "Kategorie A."),
        ("Brauche ich für die Förderung einen Stromspeicher?",
         "Nein, der Speicher ist keine Voraussetzung. Sie können den Zuschuss auch nur für die PV-Anlage "
         "beantragen. Ein Speicher wird mit 150 Euro je kWh gefördert, wenn er gemeinsam mit der neuen Anlage "
         "installiert wird."),
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
