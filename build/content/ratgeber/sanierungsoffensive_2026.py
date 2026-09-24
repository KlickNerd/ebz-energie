"""Ratgeber: Sanierungsoffensive 2026 (Bundesförderung Kesseltausch, bis 7.500 € für Wärmepumpen).

Migriert vom WordPress-Artikel ebz-photovoltaik.at/sanierungsoffensive-2026/
(veröffentlicht 2026-03-10, zuletzt geändert 2026-04-12). Zahlen: Stand April 2026.
Bereinigt: Gedankenstriche, "ohne Subunternehmer" entfernt, Widerspruch "Budget langfristig
gesichert" vs. "Budget kann vorzeitig enden" aufgelöst (Jahresbudget fix, innerhalb des Jahres
erschöpfbar), Link auf PV-für-Wärmepumpe auf den Cluster-Pfad umgestellt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "sanierungsoffensive-2026",
    "path": "/sanierungsoffensive-2026/",
    "title": "Sanierungsoffensive 2026: bis 7.500 € für Wärmepumpen | EBZ",
    "description": ("Sanierungsoffensive 2026: bis 7.500 € Bundesförderung für den Kesseltausch auf "
                    "Wärmepumpe, mit Bohrbonus 12.500 €. Voraussetzungen, 9-Monats-Frist und Ablauf."),
    "eyebrow": "Förderung · Bund",
    "crumb_label": "Sanierungsoffensive 2026",
    "h1": "Sanierungsoffensive 2026: Bis zu 7.500 € Bundesförderung für Ihre neue Wärmepumpe",
    "lead": ("Wer seine Öl-, Gas-, Kohle- oder Elektroheizung durch eine Wärmepumpe ersetzt, erhält vom Bund "
             "einen nicht rückzahlbaren Zuschuss von bis zu 7.500 €, bei Erdwärme mit Bohrbonus bis zu 12.500 €. "
             "Hier finden Sie Förderhöhen, technische Kriterien, Fristen und den genauen Ablauf der Registrierung."),
    "chips": [
        "Wärmepumpe: <b>bis 7.500 €</b>",
        "Bohrbonus Erdwärme: <b>+5.000 €</b>",
        "Deckel: <b>30 %</b> der Kosten",
        "Registrierung bis <b>31.12.2026</b>",
    ],
    "date_published": "2026-03-10",
    "date_modified": "2026-09-24",
    "hero_img": "waermepumpe",
    "hero_alt": "Luft-Wasser-Wärmepumpe an der Hauswand eines Einfamilienhauses",

    "tldr": [
        "Die Sanierungsoffensive 2026 fördert den Tausch einer fossilen Heizung im Ein-, Zweifamilien- oder "
        "Reihenhaus mit bis zu 7.500 € für Wärmepumpen, 8.500 € für Holzzentralheizungen und 6.500 € für "
        "Fernwärmeanschluss. Deckel: 30 % der förderfähigen Kosten.",
        "Boni: 5.000 € Bohrbonus für Sole-Wasser- oder Wasser-Wasser-Wärmepumpen, 2.500 € für eine thermische "
        "Solaranlage ab 6 m². Bei Kältemitteln mit GWP 150 bis 750 (z. B. R32) sinkt die Förderung um 20 %.",
        "Voraussetzungen: EHPA-Gütesiegel, GWP höchstens 750, Vorlauftemperatur maximal 55 °C, Leistung unter "
        "100 kW, Installation durch einen befugten Fachbetrieb, Energieberatungsprotokoll bei der Registrierung.",
        "Ablauf: online registrieren auf sanierungsoffensive.gv.at (seit 24. November 2025, bis 31. Dezember "
        "2026), dann 9 Monate für Umsetzung und Endabrechnung. Leistungen ab 3. Oktober 2025 sind förderfähig.",
        "Budget: 360 Millionen Euro pro Jahr von 2026 bis 2030. Innerhalb des Jahres gilt „First Come, First "
        "Served“: Im April 2026 waren bereits über 60 % der Mittel gebunden.",
    ],
    "kpis": [
        ("7.500 €", "Grundpauschale Wärmepumpe"),
        ("12.500 €", "mit Bohrbonus Erdwärme"),
        ("9 Monate", "Frist ab Registrierung"),
        ("360 Mio. €", "Bundesbudget pro Jahr"),
    ],

    "sections": [
        ("Warum der Bund 2026 auf den Kesseltausch setzt", "hintergrund", f"""
<p>Jede fünfte Heizung in Österreich läuft noch mit Öl oder Gas. Das bedeutet hohe Energiekosten,
steigende CO₂-Abgaben und Abhängigkeit von internationalen Energiemärkten. Die Bundesregierung stellt
deshalb für die Sanierungsoffensive im Zeitraum 2026 bis 2030 jährlich 360 Millionen Euro bereit,
insgesamt 1,8 Milliarden Euro. Die Finanzierung ist damit über mehrere Jahre gesichert. Innerhalb eines
Jahres kann das Budget aber ausgeschöpft sein, weil Registrierungen nach Reihenfolge des Eingangs
angenommen werden.</p>
<p>Der Kesseltausch steht im Mittelpunkt, weil der Austausch einer fossilen Heizung durch eine
{a('waermepumpe', 'Wärmepumpe')} die höchste CO₂-Einsparung pro Fördereuro erzielt. Seit 2. Februar 2026
konzentriert der Bund die Mittel auf den Kesseltausch. Neue Registrierungen für den Sanierungsbonus
(thermische Gebäudesanierung wie Dämmung oder Fenstertausch) werden seither nicht mehr angenommen.</p>
"""),
        ("Wie hoch ist die Förderung beim Kesseltausch 2026?", "foerderhoehe", f"""
<p>Der Zuschuss ist ein nicht rückzahlbarer Einmalbetrag, der nach Prüfung direkt auf Ihr Konto
ausbezahlt wird. Er ist mit maximal 30 % der förderfähigen Investitionskosten gedeckelt. Für Ein- oder
Zweifamilienhäuser und Reihenhäuser gelten diese Grundpauschalen und Boni (Stand: April 2026):</p>
{A.table(
    ["Maßnahme", "Förderung", "Hinweis"],
    [
        ["Wärmepumpe (Luft-Wasser, Sole-Wasser, Wasser-Wasser)", "bis zu 7.500 €", "Grundpauschale"],
        ["Holzzentralheizung (Pellets, Stückholz, Hackgut)", "bis zu 8.500 €", "Grundpauschale"],
        ["Anschluss an Nah-/Fernwärme", "bis zu 6.500 €", "Grundpauschale"],
        ["Bohrbonus für Erdwärme (Tiefen- oder Brunnenbohrung)", "+ 5.000 €", "in Summe bis zu 12.500 € vom Bund"],
        ["Bonus thermische Solaranlage (ab 6 m² Bruttokollektorfläche)", "+ 2.500 €", "gilt nicht für Photovoltaik"],
        ["Wohnung im Mehrgeschossbau (Zentralisierung)", "bis zu 2.000 € je Wohneinheit", "Gesamtobjekt: eigene Regeln"],
    ],
    hl_cols=(1,),
)}
<h3>Abzug bei höherem GWP-Wert des Kältemittels</h3>
<p>Wärmepumpen mit natürlichen Kältemitteln wie R290 (Propan, GWP 3) erhalten die volle Förderung.
Liegt der GWP-Wert zwischen 150 und 750, etwa bei R32, reduziert sich die Förderung bei Monoblockgeräten
bis 50 kW und Splitgeräten bis 12 kW um 20 %. Geräte mit einem GWP über 750 sind ausgeschlossen.</p>
{A.box("Photovoltaik ist nicht Teil der Kesseltausch-Förderung. PV-Anlagen werden separat über den "
       "EAG-Investitionszuschuss gefördert, die Fördercalls 2026 starten im April, Juni und Oktober.")}
"""),
        ("Wer kann den Kesseltausch 2026 beantragen?", "antragsberechtigt", f"""
<p>Die Förderung richtet sich an Privatpersonen:</p>
<ul>
  <li><b>(Mit-)Eigentümerinnen und Eigentümer</b> von Ein- oder Zweifamilienhäusern und Reihenhäusern
  im Inland, unabhängig davon, ob dort der Hauptwohnsitz liegt.</li>
  <li><b>Bauberechtigte</b> an einem Grundstück mit bestehendem Wohngebäude.</li>
  <li><b>Mieterinnen und Mieter</b>, wenn sie die Zustimmung des Eigentümers zum Heizungstausch nachweisen.</li>
</ul>
<p>Es gibt keine Einkommensgrenze und kein Mindestalter für die alte Heizanlage. Entscheidend ist, dass
ein fossiles Heizsystem vollständig durch ein klimafreundliches ersetzt wird. Pro Standort ist nur ein
Antrag möglich: In einem Zweifamilienhaus mit gemeinsamer Zentralheizung gibt es einen gemeinsamen Antrag.
Haushalte mit geringem Einkommen sollten zuerst
{a('/sauber-heizen-fuer-alle-2026/', '„Sauber Heizen für Alle“')} prüfen, dort sind bis zu 100 % der
Kosten möglich.</p>
"""),
        ("Was gefördert wird und was nicht", "foerderfaehig", f"""
<h3>Förderfähige Kosten</h3>
<ul>
  <li><b>Material:</b> Wärmepumpe, Speicher, Verrohrung, Regelungstechnik und Zubehör.</li>
  <li><b>Montage:</b> Installation durch einen befugten Installationsbetrieb.</li>
  <li><b>Planung:</b> technische Planung und Auslegung der neuen Heizanlage.</li>
  <li><b>Demontage und Entsorgung:</b> Abbau der alten Heizung, Entsorgung von Kessel und Brennstofftanks.</li>
</ul>
<p>Rechnungen müssen auf die antragstellende Person lauten und von ihr bezahlt sein. Anerkannt werden
ausschließlich Nettobeträge. Förderfähig sind Leistungen, die ab dem 3. Oktober 2025 erbracht wurden.</p>
<h3>Nicht förderfähig</h3>
<ul>
  <li><b>Eigenleistungen:</b> In Eigenregie errichtete Anlagen sind vollständig ausgeschlossen.</li>
  <li><b>Gebrauchte Anlagen:</b> Nur Neuanschaffungen werden gefördert.</li>
  <li><b>Photovoltaik:</b> eigenes Programm (EAG-Investitionszuschuss), siehe
  {a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}.</li>
</ul>
"""),
        ("Technische Voraussetzungen für die Wärmepumpe", "technik", f"""
{A.table(
    ["Kriterium", "Anforderung"],
    [
        ["EHPA-Gütesiegel", "Kriterien der European Heat Pump Association in gültiger Version, bestätigt durch ein unabhängiges Prüfinstitut"],
        ["Kältemittel", "GWP höchstens 750; R290 (GWP 3) volle Förderung, GWP 150 bis 750 Abzug von 20 %"],
        ["Vorlauftemperatur", "maximal 55 °C, ideal mit Fußbodenheizung oder großflächigen Heizkörpern"],
        ["Leistung", "unter 100 kW für Ein-, Zweifamilien- und Reihenhäuser"],
        ["Fernwärme-Prüfung", "Anschluss an ein klimafreundliches Fernwärmenetz technisch nicht möglich oder wirtschaftlich nicht zumutbar (Wärmepumpe mindestens 25 % günstiger als der Anschluss)"],
        ["Altanlage", "fossile Heizung und Tanks stilllegen und entsorgen; nicht entsorgbare Tanks entleeren, reinigen, verplomben"],
    ],
)}
<p>Die Fernwärme-Prüfung ist in den meisten ländlichen und vorstädtischen Gebieten erfüllt, weil dort
kein Netz verfügbar ist. Ob Ihr Gebäude die 55 °C Vorlauftemperatur einhält, klärt der Ratgeber
{a('/waermepumpe-im-altbau/', 'Wärmepumpe im Altbau')}.</p>
"""),
        ("Schritt für Schritt: So läuft die Antragstellung ab", "ablauf", f"""
<p>Der Förderprozess besteht aus zwei Schritten: Registrierung und Endabrechnung.</p>
{A.steps([
    ("Energieberatung durchführen lassen",
     "Bereits bei der Registrierung muss ein gültiges Energieberatungsprotokoll Ihres Bundeslandes vorliegen. "
     "Die Beratung kann vor Ort, telefonisch oder per Videokonferenz stattfinden und muss den konkreten "
     "Standort betreffen. Ein Energieausweis ist nicht erforderlich."),
    ("Online registrieren",
     "Auf sanierungsoffensive.gv.at mit ID Austria oder Lichtbildausweis, mit Angaben zur Maßnahme und den "
     "voraussichtlichen Kosten. Möglich seit 24. November 2025, längstens bis 31. Dezember 2026, solange Budget "
     "vorhanden ist. Sie erhalten eine Bestätigung per E-Mail und Zugangsdaten zur Plattform. Das Budget ist "
     "ab jetzt 9 Monate für Sie reserviert."),
    ("Heizungstausch umsetzen",
     "Ein befugter Fachbetrieb installiert die Wärmepumpe, baut die Altanlage ab und entsorgt Kessel und "
     "Tanks. Sammeln Sie alle Rechnungen, sie müssen auf Ihren Namen lauten und bezahlt sein."),
    ("Antrag und Endabrechnung einreichen",
     "Innerhalb der 9-Monats-Frist laden Sie Rechnungen, Bestätigung der fachgerechten Installation, "
     "Entsorgungsnachweise und die Kostenaufstellung im Portal hoch. Die Kommunalkredit Public Consulting "
     "(KPC) prüft und überweist die Förderung direkt auf Ihr Konto. Den Stand sehen Sie im KPC-Kundenportal."),
])}
{A.box_dark("Verpasste Frist, verlorenes Budget",
    "Wird die Endabrechnung nicht innerhalb von 9 Monaten nach der Registrierung hochgeladen, verfällt die "
    "Reservierung und die Mittel fließen zurück in den allgemeinen Topf. Registrieren Sie sich erst, wenn "
    "Beratung, Angebot und Liefertermin realistisch in diese Frist passen.")}
{A.cta("Registrierung und Technik aus einer Hand",
       "EBZ Energie organisiert die Energieberatung, registriert Ihr Projekt auf sanierungsoffensive.gv.at "
       "und plant die Wärmepumpe so, dass alle Förderkriterien erfüllt sind.",
       secondary=("waermepumpe", "Zur Wärmepumpen-Leistungsseite"))}
"""),
        ("Zeitplan und Fristen der Sanierungsoffensive 2026", "fristen", f"""
{A.table(
    ["Datum", "Was gilt"],
    [
        ["3. Oktober 2025", "Stichtag: Leistungen ab diesem Rechnungsdatum sind rückwirkend förderfähig"],
        ["24. November 2025", "Start der Online-Registrierung auf sanierungsoffensive.gv.at"],
        ["2. Februar 2026", "Fokus auf den Kesseltausch; keine neuen Registrierungen mehr für den Sanierungsbonus"],
        ["31. Dezember 2026", "letztmöglicher Tag für die Registrierung, sofern noch Budget vorhanden ist"],
        ["9 Monate ab Registrierung", "Frist für Installation und Hochladen der Endabrechnung"],
    ],
    hl_cols=(0,),
)}
<p><b>Budgetstand (April 2026):</b> Laut Berichten waren bereits über 60 % der verfügbaren Fördermittel
gebunden. Seit der Konzentration auf den Kesseltausch im Februar ist die Nachfrage stark gestiegen.
Registrieren Sie sich daher, bevor Sie den ersten Auftrag unterschreiben.</p>
<h3>Kombination mit Landesförderungen</h3>
<p>Die Bundesförderung kann mit den Programmen der Bundesländer kombiniert werden. In Kärnten und der
Steiermark, den Kernregionen von EBZ Energie, kommen dadurch mehrere Tausend Euro dazu. Alle Beträge
und Bedingungen stehen im Ratgeber
{a('/landesfoerderungen-fuer-die-waermepumpe/', 'Landesförderungen für die Wärmepumpe')}. Wichtig:
Die Summe aus Bund, Land und Gemeinde darf die tatsächlichen Investitionskosten nicht übersteigen.
Alle Förderungen werden in der Transparenzdatenbank erfasst, unzulässige Mehrfachförderungen werden
zurückgefordert. Zusätzlich bringt die
{a('/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/', 'Öko-Sonderausgabenpauschale')}
fünf Jahre lang je 400 € Sonderausgaben.</p>
"""),
        ("Wärmepumpe und Photovoltaik: die Kombination, die unabhängig macht", "photovoltaik", f"""
<p>Eine Wärmepumpe verbraucht rund 3.000 bis 5.000 kWh Strom pro Jahr. Mit einer passend
dimensionierten {a('photovoltaik', 'PV-Anlage')} decken Sie einen Großteil dieses Bedarfs selbst und
speisen den Überschuss ein oder speichern ihn. Photovoltaik wird über den EAG-Investitionszuschuss
gefördert, die Calls 2026 starten im April, Juni und Oktober. Wer beides gemeinsam plant, nutzt beide
Fördertöpfe und spart dauerhaft. Wie das technisch zusammenspielt, zeigt der Ratgeber
{a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}; die Kosten des Gesamtpakets
lassen sich über eine {a('finanzierung', 'Finanzierung')} verteilen, die Anlage gehört ab Tag 1 Ihnen.</p>
"""),
        ("Fazit: Registrieren, bevor das Jahresbudget aufgebraucht ist", "fazit", f"""
<p>Die Sanierungsoffensive 2026 ist mit bis zu 7.500 € (Erdwärme 12.500 €) das Fundament jedes
Heizungstausches. Die Bedingungen sind klar: EHPA-Gütesiegel, GWP unter 750, Vorlauf 55 °C,
Fachbetrieb, Energieberatung. Der kritische Punkt ist die Zeit: Erst Beratung, dann Registrierung, dann
Auftrag, und die Endabrechnung innerhalb von 9 Monaten. Einen Überblick über alle weiteren Töpfe gibt
der Ratgeber {a('/waermepumpenfoerderung-in-oesterreich/', 'Wärmepumpenförderung in Österreich 2026')}.</p>
{A.cta("Jetzt Förderung sichern",
       "Wir prüfen Ihre Förderfähigkeit, organisieren die Energieberatung und registrieren Ihr Projekt "
       "zum richtigen Zeitpunkt.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Ihr regionaler Partner für Wärmepumpe und Photovoltaik: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach ist Ihr Fachbetrieb für Wärmepumpen und Photovoltaik in Kärnten und "
                 "der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. Wir kommen zu "
                 "Ihnen, analysieren das Gebäude, planen Wärmepumpe und PV als Gesamtlösung und übernehmen den "
                 "gesamten Förderprozess von der Energieberatung bis zur Endabrechnung."),
        "grid": [
            ("Beratung vor Ort", "Wir berechnen, welches System zu Ihrem Haus passt."),
            ("Komplette Förderabwicklung", "Energieberatung, Registrierung, Endabrechnung auf sanierungsoffensive.gv.at."),
            ("Installation aus einer Hand", "Wärmepumpe und PV vom selben Team, klare Verantwortlichkeiten."),
            ("Regionale Expertise", "Wir kennen die Landesförderungen in Kärnten und der Steiermark."),
        ],
    },

    "faq": [
        ("Kann ich die Förderung beantragen, wenn ich keinen Hauptwohnsitz am Standort habe?",
         "Ja. Ein Hauptwohnsitz am Standort ist keine Voraussetzung, die Förderung gilt für Wohngebäude im "
         "Inland, auch wenn Sie dort nur zeitweise wohnen oder das Objekt vermieten. Entscheidend ist, dass "
         "die beheizte Wohnfläche mehr als 50 % des Gebäudes ausmacht und die fossile Heizung vollständig "
         "ersetzt wird."),
        ("Was passiert, wenn meine Kosten unter der Förderpauschale liegen?",
         "Die Förderung ist mit 30 % der tatsächlichen förderfähigen Kosten begrenzt. Bei Gesamtkosten von "
         "15.000 € beträgt die Förderung also 4.500 €, obwohl die Pauschale 7.500 € beträgt. Der 30-%-Deckel "
         "greift immer dann, wenn er einen niedrigeren Betrag ergibt als die Pauschale."),
        ("Brauche ich einen Energieausweis für den Förderantrag?",
         "Nein. Für den Kesseltausch ist kein Energieausweis nötig, sondern ein Energieberatungsprotokoll "
         "Ihres Bundeslandes. Die Beratung kann vor Ort, telefonisch oder per Video erfolgen und muss bei der "
         "Registrierung vorliegen. EBZ Energie unterstützt bei der Organisation des Termins."),
        ("Wird auch der Austausch einer Elektroheizung gefördert?",
         "Ja. Der Ersatz stationärer oder fest eingebauter Elektroheizungen wie Nachtspeicheröfen oder "
         "Elektrospeicherheizungen wird mit denselben Sätzen und Voraussetzungen gefördert wie der Tausch "
         "einer Öl- oder Gasheizung. Die alte Stromheizung muss vollständig stillgelegt werden."),
        ("Kann ich mit der Umsetzung beginnen, bevor die Registrierung abgeschlossen ist?",
         "Leistungen sind ab dem 3. Oktober 2025 förderfähig, also auch vor der Registrierung. Sie tragen dann "
         "aber das Risiko, dass die Mittel bei der späteren Registrierung bereits erschöpft sind. Wir "
         "empfehlen, zuerst zu registrieren und erst danach zu beauftragen."),
        ("Wie hoch ist die Förderung für eine Erdwärme-Wärmepumpe?",
         "Zur Grundpauschale von 7.500 € kommt bei Sole-Wasser- oder Wasser-Wasser-Wärmepumpen mit Tiefen- "
         "oder Brunnenbohrung ein Bohrbonus von 5.000 €, in Summe bis zu 12.500 € vom Bund. Auch hier gilt "
         "der Deckel von 30 % der förderfähigen Kosten."),
        ("Reduziert das Kältemittel R32 die Förderung?",
         "Ja. Bei einem GWP-Wert zwischen 150 und 750, wie bei R32, sinkt die Förderung bei Monoblockgeräten "
         "bis 50 kW und Splitgeräten bis 12 kW um 20 %. Geräte mit dem natürlichen Kältemittel R290 (Propan, "
         "GWP 3) erhalten die volle Förderung, Geräte mit GWP über 750 gar keine."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Wärmepumpen und Photovoltaik in Kärnten und der Steiermark und übernimmt die Registrierung "
                    "und Endabrechnung bei der Sanierungsoffensive. Alle Angaben entsprechen dem Stand April 2026 "
                    "und den Vorgaben auf sanierungsoffensive.gv.at. Keine Rechts- oder Steuerberatung, "
                    "maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("Sanierungsoffensive 2026 (Bundesportal, Registrierung und Förderbedingungen)",
         "https://www.sanierungsoffensive.gv.at/"),
    ],
    "related": [
        ("/waermepumpenfoerderung-in-oesterreich/", "Wärmepumpenförderung Österreich 2026: Überblick"),
        ("/landesfoerderungen-fuer-die-waermepumpe/", "Landesförderungen: alle 9 Bundesländer"),
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau: Voraussetzungen"),
        ("waermepumpe", "Wärmepumpen-Installateur EBZ Energie"),
    ],
    "cta": {
        "h3": "Budget reservieren",
        "text": "Wir registrieren Ihren Heizungstausch, bevor das Jahresbudget ausgeschöpft ist, und planen förderkonform.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre neue Wärmepumpe, mit Bundesförderung",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
