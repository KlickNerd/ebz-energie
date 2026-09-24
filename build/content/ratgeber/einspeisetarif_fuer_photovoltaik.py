"""Ratgeber: Einspeisetarif für Photovoltaik in Österreich (umfassender Leitfaden).

Zusammengeführt aus drei Live-Artikeln:
  /einspeisetarif-fuer-photovoltaik/ (Nov. 2025),
  /einspeisetarif-photovoltaik-oesterreich-vergleich/ (Juli 2025),
  /einspeiseverguetung/ (Nov. 2025).
OeMAG-Marktpreis auf Stand September 2026 (Juli 2026: 6,146 ct, Q3 2026: 10,923 ct),
ältere Werte als Verlauf. Widersprüche der Quellen (quartalsweise vs. monatliche
Berechnung, Steuerpflicht vs. Freibetrag) zugunsten der aktuelleren Rechtslage aufgelöst.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "einspeisetarif-fuer-photovoltaik",
    "path": "/einspeisetarif-fuer-photovoltaik/",
    "title": "Einspeisetarif Photovoltaik 2026: OeMAG, Anbieter, EG | EBZ",
    "description": ("Einspeisetarif Photovoltaik 2026: OeMAG-Marktpreis 6,146 ct (Juli 2026), Anbieter "
                    "4 bis 11 ct, Fixpreis oder variabel, Energiegemeinschaft, Steuerfreibetrag."),
    "eyebrow": "Stromtarife · Einspeisung",
    "crumb_label": "Einspeisetarif Photovoltaik",
    "h1": "Einspeisetarif für Photovoltaik 2026: OeMAG-Marktpreis, Anbietervergleich und Alternativen",
    "lead": ("Für eingespeisten Sonnenstrom gibt es in Österreich keinen garantierten Tarif mehr, sondern den "
             "monatlich schwankenden OeMAG-Marktpreis, Angebote privater Versorger und Energiegemeinschaften. "
             "Dieser Ratgeber zeigt, was die Modelle bringen, wo die Fallen liegen und warum Eigenverbrauch "
             "wichtiger bleibt als jeder Tarif."),
    "chips": [
        "OeMAG Juli 2026: <b>6,146 ct/kWh</b>",
        "Anbietertarife: <b>4 bis 11 ct/kWh</b>",
        "Netzbezug: <b>rund 32 ct/kWh</b>",
        "Steuerfrei: <b>bis 12.500 kWh</b> pro Jahr",
    ],
    "date_published": "2025-06-20",
    "date_modified": "2026-09-24",
    "hero_img": "gen_hero",
    "hero_alt": "Photovoltaikanlage auf einem Hausdach bei Sonnenschein: Einspeisetarif für überschüssigen Solarstrom",

    "tldr": [
        "Der OeMAG-Marktpreis ist die gesetzliche Basisvergütung für Anlagen bis 500 kWp. Er wird seit 2024 "
        "monatlich rückwirkend aus den Börsenpreisen berechnet und lag im Juli 2026 bei 6,146 Cent je "
        "Kilowattstunde, der Referenzmarktpreis für das dritte Quartal 2026 bei 10,923 Cent.",
        "Private Energieversorger zahlen je nach Modell 4 bis 11 Cent je kWh (Stand November 2025), koppeln "
        "den Einspeisetarif aber fast immer an einen Strombezugsvertrag mit Bindung und teils Grundgebühr.",
        "Eigenverbrauch schlägt jeden Tarif: Eine selbst genutzte Kilowattstunde spart rund 32 Cent Netzbezug, "
        "eine eingespeiste bringt 5 bis 10 Cent. Speicher, Wärmepumpe und E-Auto sind der größere Hebel.",
        "Energiegemeinschaften sind die Alternative: Der Preis wird in der Gemeinschaft vereinbart, im Nahbereich "
        "sinken zusätzlich die Netzentgelte um bis zu 57 Prozent.",
        "Einnahmen aus der Einspeisung sind für Privatpersonen bis 12.500 kWh pro Jahr einkommensteuerfrei "
        "(Anlagen bis 35 kWp). Der Nullsteuersatz bei der Anschaffung ist seit 1. April 2025 ausgelaufen.",
    ],
    "kpis": [
        ("6,146 ct", "OeMAG-Marktpreis Juli 2026"),
        ("10,923 ct", "Referenzmarktpreis Q3 2026"),
        ("4 bis 11 ct", "Spanne privater Anbieter (Nov. 2025)"),
        ("12.500 kWh", "steuerfreie Einspeisung pro Jahr"),
    ],

    "sections": [
        ("Was ist der Einspeisetarif und wer legt ihn fest?", "grundlagen", f"""
<p>Der Einspeisetarif (auch Einspeisevergütung) ist der Betrag, den Sie je Kilowattstunde (kWh) Solarstrom
erhalten, den Ihre Photovoltaikanlage erzeugt, Sie aber nicht selbst verbrauchen und daher ins öffentliche
Netz einspeisen. Unter dem alten Ökostromgesetz war das ein über Jahre staatlich garantierter Fixpreis, der
die Volleinspeisung attraktiv machte. Mit dem Erneuerbaren-Ausbau-Gesetz (EAG) hat sich das grundlegend
geändert: Solarstrom ist in den freien Markt integriert, es gibt marktpreisbasierte Vergütungen und
wettbewerbliche Angebote statt eines einheitlichen Tarifs.</p>
<p>Drei Akteure prägen das System. Die Abwicklungsstelle für Ökostrom (OeMAG) ist gesetzlich verpflichtet,
Strom aus PV-Anlagen bis 500 Kilowatt-Peak zum monatlich berechneten Marktpreis abzunehmen. Sie ist das
Sicherheitsnetz und der Referenzwert. Private Energieversorger werben mit eigenen Fix- und variablen Tarifen
um Ihren Überschuss. Und die E-Control als Regulierungsbehörde sorgt mit dem Tarifkalkulator für
Transparenz. Als vierte Option etablieren sich {a('eg', 'Energiegemeinschaften')}, in denen der Strom
direkt an Nachbarn, Betriebe oder Verwandte verkauft wird.</p>
<p>Die wichtigste Regel vorweg: Bei der Überschusseinspeisung, dem Standard für Privathaushalte, wird nur
eingespeist, was nach dem Eigenverbrauch übrig bleibt. Die Volleinspeisung, bei der der gesamte Strom
verkauft wird, ist bei Vergütungen unter 10 Cent und Bezugspreisen um 32 Cent wirtschaftlich kaum noch
sinnvoll.</p>
"""),
        ("Eigenverbrauch schlägt jeden Einspeisetarif", "eigenverbrauch", f"""
<p>Für eine selbst verbrauchte Kilowattstunde sparen Sie den vollen Bezugspreis, der inklusive Netzentgelte,
Abgaben und Steuern bei rund 32 Cent liegt. Für eine eingespeiste erhalten Sie im Schnitt 5 bis 10 Cent.
Jede selbst genutzte Kilowattstunde ist damit drei- bis sechsmal so viel wert wie eine verkaufte. Der
Einspeisetarif ist deshalb nur die Optimierung für den unvermeidbaren Überschuss, nicht der Treiber der
Wirtschaftlichkeit.</p>
{A.table(
    ["Verwendung der Kilowattstunde", "Wert für Sie", "Hebel"],
    [
        ["Selbst verbraucht (direkt)", "rund 32 ct gespart", "Verbrauch in die Sonnenstunden legen"],
        ["Selbst verbraucht (aus dem Speicher)", "rund 32 ct gespart, abzüglich Speicherverluste", "Batteriespeicher, Eigenverbrauch 60 bis 80 %"],
        ["In der Energiegemeinschaft verkauft", "vereinbarter Preis, plus Netzentgelt-Rabatt im Nahbereich", "lokale oder regionale EG"],
        ["Ins Netz eingespeist", "5 bis 10 ct Vergütung", "OeMAG oder Versorger, Tarifvergleich"],
    ],
    hl_cols=(1,),
)}
<p>Praktisch heißt das: Dimensionieren Sie die Anlage passend zum Verbrauch, setzen Sie auf einen
{a('batteriespeicher', 'Batteriespeicher')}, laden Sie das E-Auto zu Mittag und lassen Sie ein
{a('ems', 'Energiemanagementsystem')} Wärmepumpe und Wallbox steuern. Erst dann lohnt sich der Blick auf
den besten Abnehmer für den Rest.</p>
"""),
        ("Der OeMAG-Marktpreis: Basisvergütung mit Schwankung", "oemag-marktpreis", f"""
<p>Die OeMAG nimmt den Überschuss von PV-Anlagen bis 500 kWp zum sogenannten Marktpreis ab. Dieser wird
nicht mehr quartalsweise im Voraus festgelegt, sondern seit Anfang 2024 monatlich und rückwirkend aus dem
durchschnittlichen stündlichen Börsenpreis berechnet. Das bindet die Vergütung direkt ans Marktgeschehen,
überträgt aber auch das Preisrisiko auf Sie: Die Vergütung kann von Monat zu Monat erheblich schwanken.</p>
<p>Um Ausschläge zu dämpfen, gibt es einen Preiskorridor: Der Monatspreis darf den von der E-Control
festgelegten Quartals-Referenzmarktpreis nicht überschreiten und nicht unter 60 Prozent dieses Wertes
fallen. Das begrenzt das Risiko bei einem Preisverfall an der Börse, kappt aber auch Gewinnspitzen.</p>
{A.table(
    ["Zeitraum", "OeMAG-Marktpreis je kWh", "Einordnung"],
    [
        ["Jahresbeginn 2025", "über 9 ct", "Hochphase nach dem Winter"],
        ["Mitte 2025", "unter 6 ct", "Untergrenze des Korridors erreicht"],
        ["12-Monats-Schnitt bis November 2025", "rund 7 ct", "Verlauf laut Quelle, Stand November 2025"],
        ["Juli 2026", "6,146 ct", "an der Untergrenze des Korridors"],
        ["Referenzmarktpreis Q3 2026", "10,923 ct", "Obergrenze für die Monatspreise im Quartal"],
    ],
    hl_cols=(1,),
)}
<p><small>Stand: September 2026. Der aktuelle Monatswert wird von der OeMAG veröffentlicht, die
laufende Entwicklung kommentieren wir im Ratgeber {a('marktpreis', 'Marktpreis 2026')}.</small></p>
<p>Der große Vorteil des OeMAG-Modells: Sie brauchen keinen gekoppelten Stromliefervertrag, zahlen keine
Grundgebühr und bleiben beim Stromlieferanten frei. Es eignet sich für Betreiber, deren Rechnung auf hohem
Eigenverbrauch beruht und für die die Einspeisung eine Nebenrolle spielt.</p>
"""),
        ("Die Modelle im Vergleich: OeMAG, Fixpreis, variabel, Direktvermarktung, Energiegemeinschaft", "modelle", f"""
<p>Welcher Weg der richtige ist, hängt von Risikobereitschaft, Planungssicherheit und dem Aufwand ab, den
Sie betreiben möchten. Die Übersicht zeigt die fünf Modelle mit ihren Konditionen:</p>
{A.table(
    ["Modell", "Vergütung", "Vorteile", "Nachteile"],
    [
        ["OeMAG-Marktpreis", "monatlicher Marktpreis, Juli 2026: 6,146 ct",
         "keine Bindung, keine Grundgebühr, freier Stromlieferant", "Preisrisiko, schwankende Einnahmen"],
        ["Fixpreis beim Versorger", "fester Satz für meist 12 Monate, Spanne 4 bis 11 ct (Nov. 2025)",
         "Planungssicherheit, Schutz vor fallenden Preisen", "kein Gewinn bei steigenden Preisen, Koppelvertrag"],
        ["Variabler Versorgertarif", "OeMAG-Preis plus Bonus oder minus Abschlag",
         "Chance bei steigenden Börsenpreisen, transparent", "Risiko bei fallenden Preisen, oft Koppelvertrag"],
        ["Direktvermarktung", "Erlös an der Börse abzüglich Dienstleisterentgelt",
         "Zugang zum Großhandelsmarkt", "vor allem für größere Anlagen und Betriebe sinnvoll"],
        ["Energiegemeinschaft", "in der Gemeinschaft vereinbarter Preis",
         "Preis zwischen Marktpreis und Bezugspreis, Netzentgelt-Rabatt im Nahbereich", "Gründung oder Beitritt nötig, Abrechnung über Plattform"],
    ],
    hl_cols=(1,),
)}
<h3>Fixpreis oder variabel?</h3>
<p>Ein Fixpreis-Tarif garantiert einen festen Satz je kWh für eine Laufzeit von meist 12 Monaten. Sie
wissen zu Beginn des Vertragsjahres genau, was Sie bekommen, profitieren aber nicht von steigenden
Börsenpreisen. Variable Tarife koppeln die Vergütung an den OeMAG-Marktpreis, manche Anbieter zahlen einen
Bonus obendrauf, andere ziehen eine Bearbeitungsgebühr ab. Liegt ein Fixpreis-Angebot deutlich unter dem
aktuellen Marktpreis, ist Vorsicht geboten. Liegt es darüber, kann es eine gute Absicherung sein.</p>
<h3>Direktvermarktung</h3>
<p>Bei der Direktvermarktung übernimmt ein Energiehändler die Vermarktung Ihres Stroms an der Börse und
behält dafür ein Entgelt ein. Für Anlagen über 500 kWp, für die die OeMAG-Abnahmepflicht nicht gilt, ist
das der Standardweg; für Gewerbeanlagen im Bereich von 50 bis 500 kWp kann es sich rechnen, wenn der
Erlös nach Abzug des Entgelts über dem Marktpreis liegt. Für private Dachanlagen bis 20 kWp spielt die
Direktvermarktung in der Praxis kaum eine Rolle.</p>
"""),
        ("Anbieter vergleichen: Checkliste und Werkzeuge", "anbietervergleich", f"""
<p>Die Bandbreite der Angebote ist groß: Einige Anbieter locken mit Tarifen über 10 Cent je kWh, andere
liegen deutlich darunter (Spanne 4 bis 11 Cent, Stand November 2025). Der höchste Cent-Betrag ist aber
nicht automatisch das beste Angebot. Ein Tarif mit hoher monatlicher Grundgebühr wird für eine kleine Anlage
mit geringer Einspeisung schnell unrentabel, und ein gekoppelter Strombezugsvertrag mit teurem Bezugstarif
frisst den Vorteil auf. Prüfen Sie bei jedem Angebot:</p>
<ul>
  <li><b>Tarifart:</b> Fixpreis oder an den OeMAG-Marktpreis gekoppelt? Bei variablen Tarifen: Bonus oder
  Abschlag auf den Marktpreis?</li>
  <li><b>Vergütungshöhe:</b> Cent je kWh, gestaffelt (höherer Satz für die ersten Kilowattstunden) oder
  einheitlich?</li>
  <li><b>Laufzeit und Kündigung:</b> Mindestlaufzeit, meist 12 Monate, und Kündigungsfrist.</li>
  <li><b>Kopplung an den Strombezug:</b> Müssen Sie den Reststrom vom selben Anbieter beziehen? Dann zählt
  das Gesamtpaket aus Einspeise- und Bezugstarif.</li>
  <li><b>Gebühren:</b> Grundgebühr, Verwaltungspauschale, Zählergebühren.</li>
  <li><b>Boni:</b> Sonderboni gelten oft nur für Bestandskunden und setzen den Koppelvertrag voraus.</li>
  <li><b>Abrechnung:</b> Monatlich, quartalsweise oder jährlich?</li>
</ul>
<p>Das wichtigste Werkzeug ist der Tarifkalkulator der E-Control, der Strombezug und Einspeisung
gemeinsam vergleicht. Ergänzend lohnt der Blick auf die Websites der Versorger, weil nicht alle Tarife auf
Portalen gelistet sind. Der Wechsel selbst ist standardisiert: Der neue Anbieter kündigt beim alten und
meldet beim Netzbetreiber um. Vergleichen Sie mindestens einmal im Jahr, spätestens vor Ablauf der
Bindung.</p>
{A.box("Rechnen Sie mit Ihrer tatsächlichen Einspeisemenge. Bei 10 kWp und 70 Prozent Autarkie mit "
       "Speicher bleiben oft nur 5.000 bis 6.500 kWh Einspeisung pro Jahr. Ein Cent Unterschied je kWh "
       "macht dann 50 bis 65 Euro im Jahr aus, eine Grundgebühr von 5 Euro im Monat kostet 60 Euro.",
       label="Rechenhilfe:")}
{A.cta("Anlage, Speicher und Tarif aus einer Hand planen",
       "Wir dimensionieren Ihre PV-Anlage auf hohen Eigenverbrauch und zeigen Ihnen, welches Modell für "
       "den Überschuss zu Ihrem Verbrauch passt.",
       secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
        ("Energiegemeinschaft: Strom teilen statt einspeisen", "energiegemeinschaft", f"""
<p>Die {a('eg', 'Energiegemeinschaft')} ist die Alternative zum Verkauf an OeMAG oder Versorger: Sie
teilen Ihren Überschuss mit Nachbarn, dem Betrieb ums Eck oder auch Verwandten in einem anderen
Bundesland. Der Preis wird innerhalb der Gemeinschaft vereinbart und liegt typischerweise zwischen dem
Marktpreis und dem Netzbezugspreis: Der Erzeuger bekommt mehr als bei der Einspeisung, der Abnehmer zahlt
weniger als beim Versorger.</p>
<p>Im Nahbereich kommt ein zweiter Vorteil dazu: Für Strom, der in einer lokalen Erneuerbare-Energie-
Gemeinschaft im selben Netzabschnitt verbraucht wird, sinken die Netzentgelte um bis zu 57 Prozent,
regional um 28 Prozent, auf Netzebene 4 und 5 um bis zu 64 Prozent. Beim österreichweiten Teilen in einer
Bürgerenergiegemeinschaft gibt es diesen Rabatt nicht, der vereinbarte Preis gilt aber trotzdem. Die
Abrechnung übernimmt eine Plattform wie energyfamily. Was Sie konkret sparen, rechnet der
{a('eg_rechner', 'EG-Rechner')} aus. Details zur OeMAG in der Energiegemeinschaft finden Sie im Ratgeber
{a('/oemag-einspeisetarif/', 'OeMAG-Einspeisetarif und Energiegemeinschaft')}.</p>
"""),
        ("Steuern: Was vom Einspeiseerlös bleibt", "steuern", f"""
<p>Einnahmen aus der Stromeinspeisung gelten grundsätzlich als Einkünfte aus Gewerbebetrieb. Für
Privatpersonen gibt es aber eine großzügige Befreiung: Einnahmen aus der Einspeisung von bis zu 12.500 kWh
pro Jahr sind einkommensteuerfrei, sofern die Anlage eine Engpassleistung von höchstens 35 kWp hat. Da
private Dachanlagen diese Grenzen praktisch nie überschreiten, bleiben die Erlöse in der Regel komplett
steuerfrei. Wer mehr einspeist, versteuert nur die Menge über 12.500 kWh, der Wert wirkt als Freibetrag.</p>
<p>Bei der Umsatzsteuer hat sich die Lage geändert: Der Nullsteuersatz auf Anschaffung und Installation von
PV-Anlagen bis 35 kWp ist mit 1. April 2025 ausgelaufen, seitdem gilt wieder der reguläre Satz von 20 Prozent.
Als Ausgleich ist die EAG-Investitionsförderung 2026 wieder voll aktiv (150 Euro je kWp bis 10 kWp, 150 Euro
je kWh Speicher), siehe {a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}.
Unternehmerisch tätige Betreiber können weiterhin die Vorsteuer abziehen.</p>
{A.box("Dieser Abschnitt ersetzt keine Steuerberatung. Bei Anlagen über 35 kWp, bei gewerblicher Nutzung "
       "oder bei mehreren Zählpunkten klären Sie die Details mit Ihrer Steuerberatung.", label="Hinweis:")}
"""),
        ("Von der Planung zur ersten Gutschrift", "ablauf", f"""
{A.steps([
    ("Anlage auf Eigenverbrauch dimensionieren",
     "Der Fachbetrieb analysiert Verbrauch und Dach und plant Leistung und Speicher so, dass möglichst wenig "
     "Überschuss entsteht. Bei EBZ Energie mit Projektbericht, 3D-Belegplan und Statikreport."),
    ("Netzzugang sichern",
     "Der Netzzutrittsantrag beim Netzbetreiber liefert nach der technischen Prüfung die Zählpunktnummer, "
     "die für Förderung und Einspeisevertrag nötig ist."),
    ("Förderung vor Inbetriebnahme beantragen",
     "Mit der Zählpunktnummer stellen Sie den EAG-Antrag im Fördercall (2026: 23. April bis 11. Mai, "
     "16. bis 30. Juni, ab 8. Oktober), zwingend vor der Inbetriebnahme."),
    ("Abnehmer wählen",
     "Anmeldung bei der OeMAG zum Marktpreis, Vertrag mit einem Versorger oder Beitritt zu einer "
     "Energiegemeinschaft. Ein Wechsel ist nach Ablauf der Bindung jederzeit möglich."),
    ("Inbetriebnahme und Abrechnung",
     "Der Fachbetrieb meldet die Anlage fertig, der Netzbetreiber installiert den Smart Meter und gibt die "
     "Einspeisung frei. Ab dann wird der Überschuss gutgeschrieben."),
])}
{A.cta("Wir kümmern uns um Netzzutritt, Förderung und Einspeisevertrag",
       "Von der Dimensionierung über den Netzzutrittsantrag bis zur Wahl des Abnehmers: EBZ Energie "
       "begleitet Sie durch jeden Schritt.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("eg", "Zur Energiegemeinschaft"))}
"""),
        ("Fazit: Erst Eigenverbrauch, dann Tarif", "fazit", f"""
<p>Der Einspeisetarif für Photovoltaik hat sich vom Subventionsmodell zum Marktinstrument gewandelt. Der
OeMAG-Marktpreis liegt 2026 mit 6,146 Cent (Juli) nahe der Untergrenze, private Anbieter zahlen 4 bis 11
Cent mit Bindung, Energiegemeinschaften erzielen Preise dazwischen und sparen im Nahbereich Netzentgelte.
Der größte Hebel bleibt aber der Eigenverbrauch: Jede selbst genutzte Kilowattstunde ist mit rund 32 Cent
drei- bis sechsmal so viel wert wie eine verkaufte. Planen Sie die Anlage darauf, holen Sie sich für den
Rest den passenden Abnehmer und vergleichen Sie einmal im Jahr.</p>
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Einspeisung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und montiert Photovoltaikanlagen mit Speicher in Kärnten und der "
                 "Steiermark und betreut Energiegemeinschaften österreichweit. Wir dimensionieren auf hohen "
                 "Eigenverbrauch, erledigen Netzzutritt und Förderantrag und zeigen Ihnen, welches "
                 "Vergütungsmodell zu Ihrem Verbrauch passt."),
        "grid": [
            ("Eigenverbrauch zuerst", "Speicher, Wärmepumpe und Wallbox so geplant, dass wenig Überschuss bleibt."),
            ("Netzzutritt und Förderung", "Zählpunkt, EAG-Antrag im Call und Fertigstellungsmeldung aus einer Hand."),
            ("Energiegemeinschaft", "Beitritt oder Gründung, Abrechnung über Plattform, österreichweit möglich."),
            ("Ehrliche Zahlen", "Tarifvergleich mit Ihrer tatsächlichen Einspeisemenge, keine Lockangebote."),
        ],
    },

    "faq": [
        ("Wie hoch ist der aktuelle Einspeisetarif für Photovoltaik in Österreich?",
         "Es gibt keinen einheitlichen Tarif mehr. Der OeMAG-Marktpreis als Referenz lag im Juli 2026 bei "
         "6,146 Cent je kWh, der Referenzmarktpreis für das dritte Quartal 2026 bei 10,923 Cent. Private "
         "Versorger zahlen je nach Modell 4 bis 11 Cent (Stand November 2025), meist gekoppelt an einen "
         "Strombezugsvertrag."),
        ("Lohnt es sich mehr, Solarstrom selbst zu verbrauchen oder einzuspeisen?",
         "Selbst verbrauchen. Eine eigene Kilowattstunde spart rund 32 Cent Netzbezug, eine eingespeiste bringt "
         "5 bis 10 Cent. Speicher, Wärmepumpe, E-Auto und ein Energiemanagementsystem, das Verbraucher in die "
         "Sonnenstunden legt, sind deshalb der größere Hebel als jeder Tarifwechsel."),
        ("Wie wird der OeMAG-Marktpreis berechnet?",
         "Seit Anfang 2024 monatlich und rückwirkend aus dem durchschnittlichen stündlichen Börsenpreis. Ein "
         "Preiskorridor begrenzt den Wert: nicht über dem Quartals-Referenzmarktpreis der E-Control und nicht "
         "unter 60 Prozent davon. Die OeMAG nimmt Strom aus Anlagen bis 500 kWp zu diesem Preis ab."),
        ("Fixpreis oder variabler Einspeisetarif: Was ist besser?",
         "Ein Fixpreis für meist 12 Monate schützt vor fallenden Preisen, bringt aber nichts bei steigenden. "
         "Ein variabler Tarif folgt dem OeMAG-Marktpreis, teils mit Bonus oder Abschlag. Vergleichen Sie das "
         "Fixangebot mit dem aktuellen Marktpreis und prüfen Sie Grundgebühr, Bindung und den gekoppelten "
         "Bezugstarif."),
        ("Kann ich den Abnehmer für meinen Solarstrom frei wählen und wechseln?",
         "Ja. Sie entscheiden zwischen OeMAG, privatem Versorger und Energiegemeinschaft. Attraktive Versorgertarife "
         "setzen meist voraus, dass Sie auch Ihren Reststrom dort beziehen. Ein Wechsel ist nach Ablauf der "
         "Mindestlaufzeit, meist 12 Monate, unkompliziert: Der neue Anbieter kündigt beim alten und meldet beim "
         "Netzbetreiber um."),
        ("Was bringt eine Energiegemeinschaft im Vergleich zur Einspeisung?",
         "In der Energiegemeinschaft wird der Preis intern vereinbart und liegt typischerweise zwischen "
         "Marktpreis und Netzbezugspreis, also über der Einspeisevergütung. Im Nahbereich sinken zusätzlich die "
         "Netzentgelte um bis zu 57 Prozent (regional 28 Prozent). Österreichweites Teilen ist als "
         "Bürgerenergiegemeinschaft möglich, dann ohne Netzentgelt-Rabatt."),
        ("Muss ich Einnahmen aus der Einspeisung versteuern?",
         "Für Privatpersonen sind Einnahmen aus bis zu 12.500 kWh Einspeisung pro Jahr einkommensteuerfrei, "
         "wenn die Anlage höchstens 35 kWp Engpassleistung hat. Nur die Menge darüber ist steuerpflichtig. Die "
         "Umsatzsteuer auf die Anschaffung beträgt seit 1. April 2025 wieder 20 Prozent."),
        ("Was ist der Unterschied zwischen Überschuss- und Volleinspeisung?",
         "Bei der Überschusseinspeisung verbrauchen Sie zuerst selbst und speisen nur den Rest ein, das ist der "
         "Standard für Haushalte. Bei der Volleinspeisung wird der gesamte Strom verkauft. Bei Vergütungen unter "
         "10 Cent und Bezugspreisen um 32 Cent ist die Volleinspeisung für neue Privatanlagen wirtschaftlich "
         "nicht mehr sinnvoll."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant PV-Anlagen mit Speicher in "
                    "Kärnten und der Steiermark und begleitet Energiegemeinschaften österreichweit. Die "
                    "OeMAG-Werte in diesem Ratgeber werden monatlich geprüft, Stand September 2026. Keine "
                    "Rechts- oder Steuerberatung, maßgeblich sind die Veröffentlichungen von OeMAG und E-Control."),
    "sources": [
        ("OeMAG: Abwicklungsstelle für Ökostrom, Marktpreis", "https://www.oemag.at/"),
        ("E-Control: Tarifkalkulator und Regulierung", "https://www.e-control.at/"),
    ],
    "related": [
        ("marktpreis", "OeMAG-Marktpreis 2026: aktuelle Entwicklung"),
        ("eg", "Energiegemeinschaft: Strom teilen statt einspeisen"),
        ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage 2026"),
        ("batteriespeicher", "Batteriespeicher: Eigenverbrauch erhöhen"),
    ],
    "cta": {
        "h3": "Mehr aus jeder Kilowattstunde",
        "text": "Wir planen Ihre Anlage auf hohen Eigenverbrauch und finden den passenden Abnehmer für den Rest.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre Anlage, Ihr Strom, Ihr Tarif",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
