"""Ratgeber: Ab wann lohnt sich Photovoltaik mit Speicher? (Rechenbeispiel Kärnten, Amortisation, Auslegung).

Migriert von ebz-photovoltaik.at/ab-wann-lohnt-sich-photovoltaik-mit-speicher/ (Quelle Stand Dezember 2025).
Das Rechenbeispiel der Quelle nutzt die Fördersätze 2025; eine zweite Rechnung mit den belegten Sätzen 2026
(EAG-Novelle 2026, Kärntner Landespauschale) wurde ergänzt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "ab-wann-lohnt-sich-photovoltaik-mit-speicher",
    "path": "/ab-wann-lohnt-sich-photovoltaik-mit-speicher/",
    "title": "Ab wann lohnt sich Photovoltaik mit Speicher? | EBZ",
    "description": ("Ab wann lohnt sich Photovoltaik mit Speicher? Rechenbeispiel Kärnten: 10 kWp, 10 kWh, 19.995 € "
                    "brutto, 2.500 € Ersparnis pro Jahr, Amortisation in 4,6 Jahren."),
    "eyebrow": "Speicher · Wirtschaftlichkeit",
    "crumb_label": "Lohnt sich PV mit Speicher?",
    "h1": "Ab wann lohnt sich Photovoltaik mit Speicher? Rechenbeispiel mit 4,6 Jahren Amortisation",
    "lead": ("Eine PV-Anlage mit Speicher ist im Einfamilienhaus zum Standard geworden. Ob sie sich rechnet, "
             "entscheiden Eigenverbrauch, Strompreis und Förderung. Wir rechnen ein konkretes Beispiel aus Kärnten "
             "durch: 10 kWp, 10 kWh, Ost-West."),
    "chips": [
        "Beispiel: <b>10 kWp + 10 kWh</b>, 19.995 €*",
        "Ersparnis: <b>rund 2.500 €</b> pro Jahr*",
        "Amortisation: <b>4,6 Jahre</b>*",
        "Eigenverbrauch: <b>30 auf 70 %+</b>",
    ],
    "date_published": "2025-12-05",
    "date_modified": "2026-09-24",
    "hero_img": "gen_hero",
    "hero_alt": "Photovoltaikanlage mit Ost-West-Ausrichtung auf einem Einfamilienhaus in Kärnten",

    "tldr": [
        "Die Einspeisevergütung liegt oft nur bei 4 bis 8 Cent je kWh, der Bezugspreis inklusive Netzentgelten "
        "und Abgaben bei 33 bis 36 Cent*. Diese Schere macht den Eigenverbrauch zum entscheidenden Hebel.",
        "Ohne Speicher nutzt ein Haushalt rund 30 Prozent seines Solarstroms selbst, mit Speicher 70 Prozent "
        "und mehr. Faustformel für die Auslegung: 1 kWp Modulleistung zu 1 kWh Speicherkapazität.",
        "Rechenbeispiel Kärnten: 10 kWp und 10 kWh für 19.995 Euro brutto, rund 8.500 Euro Förderung von Bund und "
        "Land (Fördersätze 2025), Restkosten 11.495 Euro, 2.500 Euro Ersparnis pro Jahr, Amortisation in "
        "4,6 Jahren.",
        "Mit den Fördersätzen 2026 (EAG 150 Euro je kWp und je kWh, Kärntner Pauschale 3.000 Euro) ergeben sich "
        "6.000 Euro Förderung und 5,6 Jahre Amortisation. Beides liegt im EBZ-typischen Korridor von 4 bis 6 Jahren.",
        "Über 20 Jahre summiert sich die Ersparnis im Beispiel auf 50.000 Euro, abzüglich Restkosten bleiben rund "
        "38.500 Euro Gewinn, eine Rendite von rund 335 Prozent auf die Restinvestition.",
    ],
    "kpis": [
        ("4,6 Jahre", "Amortisation im Beispiel (Fördersätze 2025)*"),
        ("2.500 €", "Stromkostenersparnis pro Jahr im Beispiel*"),
        ("rund 335 %", "Rendite auf die Restinvestition über 20 Jahre*"),
        ("1 kWp : 1 kWh", "Faustformel für Modulleistung zu Speicherkapazität"),
    ],

    "sections": [
        ("Vom Einspeiser zum Selbstversorger: warum sich die Rechnung geändert hat", "paradigmenwechsel", f"""
<p>In den Jahren hoher geförderter Tarife wurde eine PV-Anlage so ausgelegt, dass möglichst viel eingespeist
werden konnte. Die Einspeisevergütung war der Renditetreiber. Das hat sich grundlegend gedreht: Langfristig
pendelt sich die Vergütung für Überschussstrom auf einem moderaten Niveau ein, oft nur wenige Cent je
Kilowattstunde, besonders zur Mittagszeit, wenn alle Anlagen gleichzeitig liefern. Aktuelle Werte finden Sie
im Ratgeber {a('/einspeisetarif-fuer-photovoltaik/', 'Einspeisetarif für Photovoltaik')} und beim
{a('marktpreis', 'OeMAG-Marktpreis 2026')}.</p>
<p>Gleichzeitig bleiben die Bezugskosten hoch. In Österreich besteht der Strompreis nicht nur aus dem
Energiepreis, sondern zu einem erheblichen Teil aus Netzentgelten, Steuern und Abgaben. Jede selbst erzeugte
und direkt verbrauchte Kilowattstunde spart also nicht nur den Energiepreis, sondern auch Netzentgelt und
Abgaben auf diese Menge. Genau deshalb ist der Eigenverbrauch heute der wichtigste Hebel der Wirtschaftlichkeit.</p>
"""),
        ("Die Rolle des Speichers: das Zeitproblem lösen", "speicher-rolle", f"""
<p>Eine PV-Anlage ohne Speicher hat ein strukturelles Problem: Die Erzeugungskurve deckt sich selten mit der
Verbrauchskurve. Mittags liefert das Dach im Überfluss, während niemand zu Hause ist. Abends, wenn gekocht
wird, die Wärmepumpe läuft oder das E-Auto laden soll, liefert die Anlage nichts mehr.</p>
<p>Der Speicher puffert die Energie vom Tag für Abend und Nacht. Mit einer reinen PV-Anlage erreichen
Haushalte oft nur rund 30 Prozent Eigenverbrauch, mit Speicher 70 Prozent und mehr. In Österreich, wo die
Wintermonate durch Inversionswetterlagen häufig neblig sind, entscheidet die Übergangszeit im Frühjahr und
Herbst über den Autarkiegrad. Genau dort spielt der Speicher seine Stärke aus. Wer bereits eine Anlage hat,
findet im Ratgeber {a('/pv-speicher-nachruesten/', 'PV-Speicher nachrüsten')} die Optionen für den Bestand.</p>
"""),
        ("Technische Auslegung: kWp und kWh im richtigen Verhältnis", "auslegung", f"""
<p>Damit die Rechnung aufgeht, müssen die Komponenten zueinander passen. Zwei Einheiten sind entscheidend:
<b>kWp</b> (Kilowatt-Peak) ist die Spitzenleistung der Module, <b>kWh</b> (Kilowattstunde) die Kapazität des
Speichers.</p>
<p>Für ein durchschnittliches österreichisches Einfamilienhaus hat sich eine Anlagengröße von rund 10 kWp
etabliert, dazu ein Speicher mit rund 10 kWh. Diese 1:1-Auslegung gilt als Faustformel für hohe
Wirtschaftlichkeit. Ist der Speicher zu klein, verschenken Sie im Sommer Potenzial. Ist er zu groß, wird er
im Winter nie voll und die Kapazität steht ungenutzt herum. Bei 4.000 bis 5.000 kWh Jahresverbrauch sind
7 bis 11 kWh meist ideal.</p>
<p>Auch die Qualität zählt. Die HTW Berlin prüft in ihrer jährlichen Stromspeicher-Inspektion die Effizienz
marktüblicher Systeme. Die Ergebnisse gelten auch für Österreich, weil hier dieselben Hersteller dominieren.
Geringe Umwandlungsverluste beim Laden und Entladen sind bares Geld, denn jede verlorene Kilowattstunde
mindert die Ersparnis. Details zur Technik auf der Leistungsseite {a('batteriespeicher', 'Batteriespeicher')}.</p>
"""),
        ("Rechenbeispiel: 10 kWp mit 10 kWh Speicher in Kärnten", "rechenbeispiel", f"""
<p>Wir bleiben nicht bei der Theorie. Die folgende Rechnung zeigt eine Anlage, die in Kärnten errichtet wird.
Kärnten steht hier beispielhaft für ein Bundesland mit Landesförderung zusätzlich zum Bund; die Logik gilt
überall, nur die Förderhöhen variieren. Angenommen wird ein Haushalt, der seinen Verbrauch mit
Energiemanagement auf die Erzeugung abstimmt.</p>
{A.table(
    ["Anlagendaten", "Wert"],
    [
        ["PV-Leistung", "10 kWp, Ost-West-Ausrichtung"],
        ["Speicher", "10 kWh"],
        ["Gesamtpreis brutto*", "19.995 €"],
        ["Stromkostenersparnis pro Jahr*", "rund 2.500 €"],
        ["Angenommener Bezugspreis*", "0,33 bis 0,36 € je kWh"],
        ["Einspeisevergütung", "nicht eingerechnet, Fokus Eigenverbrauch"],
    ],
    hl_cols=(1,),
)}
<h3>Förderung: zwei Stände, zwei Ergebnisse</h3>
<p>Die Quelle des Beispiels rechnet mit den Fördersätzen des Jahres 2025 (EAG 160 Euro je kWp, Kärnten
275 Euro je kWh Speicher). Seit 2026 gelten neue Konditionen: Der EAG-Bundeszuschuss beträgt 150 Euro je kWp
in Kategorie A und 150 Euro je kWh Speicher, das Land Kärnten zahlt für neue PV-Anlagen ab 5 kWp mit
Speicher ab 5 kWh eine Pauschale von 3.000 Euro, voll mit dem Bund kombinierbar. Beide Varianten:</p>
{A.table(
    ["Förderposition", "Fördersätze 2025*", "Fördersätze 2026*"],
    [
        ["EAG-Bund, PV-Anlage", "1.600 €", "1.500 €"],
        ["EAG-Bund, Speicher", "1.500 €", "1.500 €"],
        ["Land Kärnten, PV", "2.680 €", "3.000 € Pauschale (PV mit Speicher)"],
        ["Land Kärnten, Speicher", "2.750 €", "in der Pauschale enthalten"],
        ["Gesamtförderung (ohne Made-in-Europe-Bonus)", "rund 8.500 €", "6.000 €"],
        ["Restkosten nach Förderung", "11.495 €", "13.995 €"],
        ["Amortisation bei 2.500 € Ersparnis pro Jahr", "4,6 Jahre", "5,6 Jahre"],
    ],
    hl_cols=(1, 2),
)}
<p>Mit dem Made-in-Europe-Bonus (europäische Module, Wechselrichter oder Speicher von der White List der
EAG-Abwicklungsstelle) steigt die Bundesförderung um 10 Prozent je Komponente. Die genaue Höhe hängt von
Einreichung, Call und Staffelung ab. Alle Kärntner Details im Ratgeber
{a('/photovoltaik-foerderung-kaernten/', 'Photovoltaik-Förderung Kärnten 2026')}.</p>
<h3>Rendite über 20 Jahre</h3>
<p>Photovoltaikmodule haben eine Leistungsgarantie von bis zu 30 Jahren, für die Rechnung genügen konservative
20 Jahre: 20 mal 2.500 Euro ergeben 50.000 Euro eingesparte Stromkosten. Abzüglich der Restkosten von
11.495 Euro bleiben rund 38.500 Euro Gewinn, das entspricht einer Rendite von rund 335 Prozent auf die
Restinvestition. Mit den Fördersätzen 2026 sind es rund 36.000 Euro Gewinn. Strompreissteigerungen und
Inflation sind dabei nicht eingerechnet; sie würden das Ergebnis verbessern.</p>
<p><small>*Beispielkonditionen und Richtwerte, Stand Dezember 2025 (Fördersätze 2025) beziehungsweise Juni 2026
(Fördersätze 2026). Die tatsächliche Förderhöhe hängt von Call, Einreichzeitpunkt und Bonus ab, die Ersparnis
von Verbrauchsprofil und Strompreis. EBZ-Richtpreis für 10 kWp mit Speicher: rund 15.000 bis 22.000 Euro
vor Förderung.</small></p>
{A.cta("Ihre persönliche Wirtschaftlichkeitsrechnung",
       "Wir rechnen mit Ihrem Verbrauch, Ihrem Dach und den aktuellen Förderungen von Bund und Land, ehrlich "
       "und ohne Schönfärberei.",
       secondary=("photovoltaik", "Zur Photovoltaik"))}
"""),
        ("Was die Rendite bestimmt", "einflussfaktoren", f"""
<p>Eine Amortisation unter 6 Jahren ist im Bereich der Haustechnik ungewöhnlich; bei Heizungen oder Dämmungen
rechnen Eigentümer mit 15 bis 20 Jahren. Dass PV mit Speicher so schnell rentabel ist, liegt an der Schere
zwischen hohen Bezugspreisen und den Förderungen. Der Speicher für sich allein, ohne PV, wäre unwirtschaftlich.
Im Systemverbund ist er der Hebel, der die teuren Netzbezugskosten eliminiert. Diese Faktoren entscheiden:</p>
<ul>
  <li><b>Eigenverbrauchsanteil:</b> Je höher, desto besser. Ziel sind über 60 Prozent, mit Speicher und
  Energiemanagement 70 Prozent und mehr.</li>
  <li><b>Strompreisentwicklung:</b> Viele Bestandskunden zahlen inklusive Netzgebühren, Steuern und Abgaben
  33 bis 36 Cent je kWh*. Für den Netzausbau erwarten Fachleute mittelfristig steigende Netzentgelte. Jede
  vermiedene Kilowattstunde wirkt dann doppelt.</li>
  <li><b>Einspeisung:</b> Je niedriger die Vergütung, desto mehr lohnt der Eigenverbrauch. Bei 4 bis 8 Cent
  Einspeisung und über 30 Cent Bezug ist der Speicher der entscheidende Faktor.</li>
  <li><b>Garantien und Lebensdauer:</b> Speicher auf LFP-Basis (Lithium-Eisenphosphat) gelten als sicher und
  langlebig, mit 10 Jahren Herstellergarantie und 15 bis 20 Jahren technischer Lebensdauer.</li>
  <li><b>Fördercall und Timing:</b> Die Förderhöhe kann je Call variieren, der EAG-Antrag muss vor
  Inbetriebnahme gestellt werden.</li>
</ul>
<h3>Blackout-Schutz als Bonus</h3>
<p>Ein Aspekt, der in der reinen Renditerechnung fehlt: Mit notstromfähigem Wechselrichter und
Umschalteinrichtung versorgt der Speicher das Haus bei Netzausfall weiter. Dieser Sicherheitsgewinn lässt sich
schwer in Euro beziffern, ist aber für viele der Hauptgrund für die Anschaffung. Nicht jeder Speicher kann das
ab Werk; Wechselrichter und Netzumschaltbox müssen bei der Planung berücksichtigt werden. Mehr dazu im Ratgeber
{a('/notstrom/', 'Notstrom mit Photovoltaik')}.</p>
<p><small>*Richtwerte, Stand Dezember 2025.</small></p>
"""),
        ("Fazit: Jetzt handeln oder warten?", "fazit", f"""
<p>Eine Photovoltaikanlage mit Speicher ist ein wirksamer Schutz vor steigenden Strompreisen: Sie legen den
Preis eines Großteils Ihres Stroms für zwei Jahrzehnte fest. Die Kombination ist technisch ausgereift und
finanziell attraktiv, mit Amortisationszeiten von typischerweise 4 bis 6 Jahren. Die Anfangsinvestition ist mit
15.000 bis 22.000 Euro für 10 kWp mit Speicher spürbar, lässt sich aber über eine
{a('finanzierung', 'Finanzierung ab 147 Euro pro Monat inklusive Speicher')} abbilden, bei der die Anlage
ab Tag 1 Ihnen gehört.</p>
<p>Damit die Rechnung aufgeht, muss die Planung stimmen: die Dimensionierung der kWp-Leistung, die Auswahl des
Speichers und die fristgerechte Beantragung aller Förderungen bei Bund und Land. Ein Fehler in der Planung
kann die Amortisation um Jahre verlängern.</p>
{A.cta("Rentiert sich PV mit Speicher auf Ihrem Dach in unter 6 Jahren?",
       "Lassen Sie uns gemeinsam rechnen: kostenlose Erstberatung mit individueller Wirtschaftlichkeitsanalyse "
       "und Projektbericht mit 3D-Belegplan und Statikreport.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("referenzen", "Referenzen mit Zahlen"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für die Wirtschaftlichkeitsrechnung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik mit Speicher in Kärnten und der "
                 "Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften und über 300 "
                 "dokumentierten Projekten mit typischer Amortisation von 4 bis 6 Jahren. Wir rechnen jedes Projekt "
                 "mit Ihrem Verbrauch durch und schöpfen die Förderungen von Bund und Land aus."),
        "grid": [
            ("Ehrliche Rechnung", "Wirtschaftlichkeit auf Basis Ihres Lastprofils, nicht auf Basis von Prospektwerten."),
            ("Förderung aus einer Hand", "EAG-Ticket, Landesantrag Kärnten oder Steiermark, Endabrechnung."),
            ("Auslegung nach Faustformel und Praxis", "1 kWp zu 1 kWh als Start, Feinabstimmung nach Verbrauch."),
            ("Garantien", "Bis zu 30 Jahre Leistungsgarantie, mindestens 10 Jahre Produktgarantie."),
        ],
    },

    "faq": [
        ("Ab wann lohnt sich Photovoltaik mit Speicher?",
         "Sobald der Eigenverbrauch hoch und der Bezugspreis deutlich über der Einspeisevergütung liegt. Im "
         "Rechenbeispiel aus Kärnten amortisiert sich eine 10-kWp-Anlage mit 10 kWh Speicher nach Förderung in "
         "4,6 Jahren (Fördersätze 2025) beziehungsweise 5,6 Jahren (Fördersätze 2026). EBZ-Projekte liegen "
         "typischerweise bei 4 bis 6 Jahren."),
        ("Wie lange hält ein Stromspeicher tatsächlich?",
         "Moderne Speicher setzen meist auf Lithium-Eisenphosphat (LFP). Hersteller geben oft 10 Jahre Garantie, "
         "die technische Lebensdauer liegt bei 15 bis 20 Jahren. Die Stromspeicher-Inspektion der HTW Berlin "
         "bescheinigt diesen Systemen eine hohe Zyklenfestigkeit."),
        ("Kann ich für meine bestehende Anlage einen Speicher nachrüsten?",
         "Ja, ein AC-gekoppelter Speicher lässt sich fast immer integrieren. Die Förderung ist für die reine "
         "Nachrüstung aber anders geregelt: Der EAG-Bund fördert Speicher nur mit neuer oder erweiterter PV-Anlage, "
         "Kärnten zahlt für die Nachrüstung 1.000 Euro Pauschale. Wirtschaftlich ist das Gesamtpaket aus PV und "
         "Speicher meist günstiger als die spätere Nachrüstung."),
        ("Wie groß sollte der Speicher dimensioniert sein?",
         "Richtwert: 1 kWp Modulleistung zu 1 kWh Speicherkapazität. Bei 4.000 bis 5.000 kWh Jahresverbrauch "
         "sind 7 bis 11 kWh meist ideal. Ziel ist, den Nachtverbrauch im Sommer und in der Übergangszeit "
         "abzudecken, ohne überdimensionierte Kapazität zu bezahlen."),
        ("Lohnt sich ein Speicher, wenn die Einspeisevergütung sinkt?",
         "Ja, dann erst recht. Je niedriger die Einspeisevergütung und je höher der Bezugspreis inklusive "
         "Netzkosten, desto mehr rechnet sich der Speicher. Bei 4 bis 8 Cent Einspeisung und über 30 Cent Bezug "
         "ist der Eigenverbrauch der entscheidende wirtschaftliche Faktor."),
        ("Was kostet eine 10-kWp-Anlage mit Speicher?",
         "Bei EBZ Energie liegt der Richtpreis für 10 kWp mit Speicher bei rund 15.000 bis 22.000 Euro vor "
         "Förderung. Das Rechenbeispiel arbeitet mit 19.995 Euro brutto. Nach Förderung von Bund und Land "
         "verbleiben je nach Jahr rund 11.500 bis 14.000 Euro."),
        ("Was bringt der Speicher bei einem Stromausfall?",
         "Standardmäßig schalten PV-Anlagen bei Netzausfall ab. Ein Speicher mit Notstromfunktion kann das Haus "
         "weiterversorgen, wenn Wechselrichter und Netzumschaltbox dafür ausgelegt sind. Nicht jeder Speicher kann "
         "das ab Werk, es muss bei der Planung berücksichtigt werden."),
        ("Wie hoch ist die Förderung 2026 für PV mit Speicher in Kärnten?",
         "Der EAG-Bund zahlt 150 Euro je kWp (bis 10 kWp) und 150 Euro je kWh Speicher, das Land Kärnten "
         "3.000 Euro Pauschale für neue PV-Anlagen ab 5 kWp mit Speicher ab 5 kWh, ohne Anrechnung der "
         "Bundesförderung. Für 10 kWp mit 10 kWh sind das 6.000 Euro. Stand Juni 2026."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team hat über 300 PV-Projekte in sechs "
                    "Bundesländern umgesetzt; die typische Amortisation liegt bei 4 bis 6 Jahren. Alle Rechenbeispiele "
                    "sind Richtwerte, keine Zusage: Maßgeblich sind Ihr Verbrauchsprofil, das individuelle Angebot "
                    "und die offiziellen Förderbedingungen. Keine Rechts- oder Steuerberatung."),
    "sources": [
        ("HTW Berlin: Stromspeicher-Inspektion 2025",
         "https://solar.htw-berlin.de/studien/stromspeicher-inspektion-2025/"),
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("Förderportal des Landes Kärnten", "https://www.ktn.gv.at/"),
    ],
    "related": [
        ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage"),
        ("/photovoltaik-foerderung-kaernten/", "Photovoltaik-Förderung Kärnten 2026"),
        ("/pv-speicher-nachruesten/", "PV-Speicher nachrüsten"),
        ("finanzierung", "Finanzierung ab 147 € pro Monat"),
    ],
    "cta": {
        "h3": "Rechnen wir Ihr Dach durch",
        "text": "Kostenlose Wirtschaftlichkeitsanalyse mit Ihrem Verbrauch und den aktuellen Förderungen.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre Anlage, Ihre Zahlen",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
