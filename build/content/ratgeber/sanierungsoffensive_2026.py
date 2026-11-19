"""Ratgeber: Sanierungsoffensive 2026 (Bundesförderung Kesseltausch, Neuauflage ab 2.11.2026).

Stand 19.11.2026: Kesseltausch neu aufgelegt (Infoblatt und FAQ KPC Version 10/2026, Aktionsseite,
BMLUK; build/seo/_fakten_2026-10.md, Abschnitt "VERBINDLICH AB 19.11.2026"). Wärmepumpe 5.000 €,
Bohrbonus +5.000 €, Solarthermie +2.500 €, keine 30-%-Grenze mehr, Registrierung bis 31.12.2026.
Die Werte der ersten Aktion 2026 (bis 7.500 €) bleiben nur als Historie im Text.

Migriert vom WordPress-Artikel ebz-photovoltaik.at/sanierungsoffensive-2026/
(veröffentlicht 2026-03-10, zuletzt geändert 2026-04-12).
Bereinigt: Gedankenstriche, "ohne Subunternehmer" entfernt, Link auf PV-für-Wärmepumpe auf den
Cluster-Pfad umgestellt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "sanierungsoffensive-2026",
    "path": "/sanierungsoffensive-2026/",
    "title": "Sanierungsoffensive 2026: Kesseltausch neu, 5.000 € | EBZ",
    "description": ("Sanierungsoffensive 2026: Kesseltausch seit 2. November 2026 neu aufgelegt. 5.000 € für die "
                    "Wärmepumpe, +5.000 € Bohrbonus, Registrierung bis 31.12.2026."),
    "eyebrow": "Förderung · Bund",
    "crumb_label": "Sanierungsoffensive 2026",
    "h1": "Sanierungsoffensive 2026: Kesseltausch neu aufgelegt. 5.000 € für Ihre Wärmepumpe, Registrierung bis 31. Dezember 2026",
    "lead": ("Stand November 2026: Seit 2. November 2026 läuft der Kesseltausch für Ein-, Zweifamilien- und "
             "Reihenhäuser wieder. Der Bund zahlt 5.000 € Pauschale für die Wärmepumpe, dazu 5.000 € Bohrbonus bei "
             "Erdwärme und 2.500 € bei einer thermischen Solaranlage. Registrieren können Sie bis 31. Dezember 2026 "
             "oder bis das Budget aufgebraucht ist. Hier finden Sie Beträge, Voraussetzungen, Ablauf und Fristen."),
    "chips": [
        "Status: <b>läuft wieder</b> seit 2. November 2026",
        "Wärmepumpe: <b>5.000 €</b> Pauschale",
        "Bohrbonus Erdwärme: <b>+5.000 €</b>",
        "Registrierung <b>bis 31.12.2026</b>",
    ],
    "date_published": "2026-03-10",
    "date_modified": "2026-11-19",
    "hero_img": "waermepumpe",
    "hero_alt": "Luft-Wasser-Wärmepumpe an der Hauswand eines Einfamilienhauses",

    "tldr": [
        "Stand November 2026: Der Kesseltausch der Sanierungsoffensive ist seit 2. November 2026 neu aufgelegt. "
        "Registrierung und Antrag sind möglich, solange Budget vorhanden ist, längstens bis 31. Dezember 2026 "
        "(Quelle: Informationsblatt der KPC, Version 10/2026).",
        "Pauschalen: Wärmepumpe 5.000 €, Holzzentralheizung 6.000 €, Nah- und Fernwärme 4.000 €. Die frühere "
        "Grenze von 30 % der Kosten entfällt in der Neuauflage; alle Förderungen zusammen dürfen die "
        "Investitionskosten nicht übersteigen.",
        "Zuschläge: +5.000 € für Tiefenbohrung oder Brunnen bei Sole-Wasser- oder Wasser-Wasser-Wärmepumpen, "
        "+2.500 € für eine thermische Solaranlage ab 6 m² (Photovoltaik zählt nicht). Bei Luft-Wasser-Wärmepumpen "
        "mit Kältemittel-GWP 150 bis 750 sinkt die Förderung um 20 %.",
        "Voraussetzungen: Privatperson, Ein-, Zweifamilien- oder Reihenhaus, keine Einkommensprüfung, kein "
        "Hauptwohnsitz nötig. Wärmepumpe mit EHPA-Gütesiegel, Vorlauftemperatur höchstens 55 °C, unter 100 kW, "
        "Installation durch eine Fachkraft. Fernwärme hat Vorrang.",
        "Ablauf: Energieberatung des Bundeslandes, Online-Registrierung (reserviert das Budget 9 Monate), "
        "Umsetzung, Antrag mit Rechnungen innerhalb von 9 Monaten. Gefördert werden Leistungen ab 7. Oktober 2026.",
        "Mit der Landesförderung kombinierbar: in Kärnten 5.000 € Bund plus 3.000 € Land, zusammen bis 8.000 €*. "
        "Die Steiermark fördert neue Wärmepumpen derzeit nicht, dort bleiben die 5.000 € vom Bund. In der ersten "
        "Aktion 2026 waren es bis zu 7.500 € vom Bund.",
    ],
    "kpis": [
        ("5.000 €", "Bundespauschale Wärmepumpe (Neuauflage)"),
        ("+5.000 €", "Bohrbonus Sole- oder Wasser-Wasser-Wärmepumpe"),
        ("31.12.2026", "letzter Registrierungstag (oder früheres Budgetende)"),
        ("9 Monate", "für Umsetzung und Antrag ab Registrierung"),
    ],

    "sections": [
        ("Stand November 2026: Kesseltausch neu aufgelegt", "status", f"""
{A.box_dark("Kesseltausch 2026: Registrierung seit 2. November wieder möglich",
    "Die erste Kesseltausch-Aktion 2026 war im Herbst ausgeschöpft, die Registrierung wurde geschlossen "
    "(Stand 9. Oktober 2026). Seit 2. November 2026 läuft die Aktion „Kesseltausch 2026, "
    "Ein-/Zweifamilienhaus/Reihenhaus“ als Neuauflage: Registrierung und Antrag sind möglich, solange Budget "
    "vorhanden ist, längstens bis 31. Dezember 2026. Möglich wird das laut BMLUK durch Mittel aus dem "
    "Zusagerahmen 2026, die durch Stornierungen, nicht umgesetzte Vorhaben und verfallene Registrierungen frei "
    "wurden.")}
<p>Was sich gegenüber der ersten Aktion ändert: Die Pauschalen sind niedriger (Wärmepumpe 5.000 € statt bis
zu 7.500 €), dafür entfällt die Grenze von 30 % der förderfähigen Kosten. Bohrbonus (5.000 €) und
Solarbonus (2.500 €) bleiben. Gefördert werden Lieferungen und Leistungen ab 7. Oktober 2026. Wer in der
ersten Aktion registriert ist, setzt nach deren Bedingungen um und prüft den Stand der Reservierung im
KPC-Kundenportal.</p>
<p>Zusätzlich gilt: Der Kesseltausch ist mit Landesförderungen kombinierbar. Kärnten zahlt 2026 eine
Pauschale von 3.000 € für die Wärmepumpe (ob das Budget reicht, klären wir vor dem Angebot), die Steiermark
nimmt für neue Wärmepumpen derzeit keine Förderanträge an (wohnbau.steiermark.at, Stand 10. Oktober 2026).
Mit der ausbezahlten Bundesförderung greift außerdem die
{a('/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/', 'Öko-Sonderausgabenpauschale')}
(fünf Jahre je 400 € Sonderausgaben). „Sauber Heizen für Alle“ bleibt geschlossen. Für 2027 sind laut BMLUK
179 Millionen Euro für den Kesseltausch vorgesehen, die Förderhöhe soll sich 2027 laut Aktionsseite nicht
ändern. Den Überblick über alle Töpfe gibt der Ratgeber
{a('/waermepumpenfoerderung-in-oesterreich/', 'Wärmepumpenförderung in Österreich')}.</p>
"""),
        ("Warum der Bund 2026 auf den Kesseltausch setzt", "hintergrund", f"""
<p>Jede fünfte Heizung in Österreich läuft noch mit Öl oder Gas. Das bedeutet hohe Energiekosten,
steigende CO₂-Abgaben und Abhängigkeit von internationalen Energiemärkten. Die Bundesregierung hat
deshalb für die Sanierungsoffensive im Zeitraum 2026 bis 2030 jährlich 360 Millionen Euro angekündigt,
insgesamt 1,8 Milliarden Euro. Innerhalb eines Jahres kann das Budget aber ausgeschöpft sein, weil
Registrierungen nach Reihenfolge des Eingangs angenommen werden. Genau das ist 2026 passiert: Im Herbst
waren die Mittel der ersten Aktion aufgebraucht, die Registrierung wurde geschlossen. Mit frei gewordenen
Mitteln startete am 2. November 2026 die Neuauflage.</p>
<p>Der Kesseltausch steht im Mittelpunkt, weil der Austausch einer fossilen Heizung durch eine
{a('waermepumpe', 'Wärmepumpe')} die höchste CO₂-Einsparung pro Fördereuro erzielt. Seit 2. Februar 2026
konzentriert der Bund die Mittel auf den Kesseltausch. Neue Registrierungen für den Sanierungsbonus
(thermische Gebäudesanierung wie Dämmung oder Fenstertausch) werden seither nicht mehr angenommen.</p>
"""),
        ("Wie hoch ist die Förderung beim Kesseltausch 2026?", "foerderhoehe", f"""
<p>Der Zuschuss ist ein nicht rückzahlbarer Einmalbetrag als Pauschale, der nach Prüfung direkt auf das
Konto ausbezahlt wird. Für Ein- oder Zweifamilienhäuser und Reihenhäuser gelten in der Neuauflage diese
Beträge (zum Vergleich die Werte der ersten Aktion 2026):</p>
{A.table(
    ["Maßnahme", "Neuauflage ab 2.11.2026", "Erste Aktion 2026 (Historie)"],
    [
        ["Wärmepumpe (Luft-Wasser, Sole-Wasser, Wasser-Wasser)", "5.000 €", "bis zu 7.500 €"],
        ["Holzzentralheizung (Pellets, Stückholz, Hackgut)", "6.000 €", "bis zu 8.500 €"],
        ["Anschluss an Nah-/Fernwärme", "4.000 €", "bis zu 6.500 €"],
        ["Bohrbonus für Erdwärme (Tiefenbohrung oder Brunnen)", "+ 5.000 €", "+ 5.000 €"],
        ["Bonus thermische Solaranlage (ab 6 m² Bruttokollektorfläche, nicht für Photovoltaik)", "+ 2.500 €", "+ 2.500 €"],
        ["Begrenzung", "keine Prozentgrenze; alle Förderungen zusammen höchstens die Investitionskosten", "max. 30 % der förderfähigen Kosten"],
    ],
    hl_cols=(1,),
)}
<p>Die Zuschläge sind kombinierbar: Eine Sole-Wasser-Wärmepumpe mit Tiefenbohrung und thermischer
Solaranlage kommt auf bis zu 12.500 € vom Bund. Wohnungen in Gebäuden ab drei Wohneinheiten fallen nicht
unter diese Aktion, dafür gibt es den „Kesseltausch“ für den mehrgeschossigen Wohnbau mit eigenem
Informationsblatt. Laut Aktionsseite ändert sich die Förderhöhe 2027 nicht.</p>
<h3>Abzug bei höherem GWP-Wert des Kältemittels</h3>
<p>Wärmepumpen mit natürlichen Kältemitteln wie R290 (Propan, GWP 3) erhalten die volle Förderung.
Liegt der GWP-Wert bei Luft-Wasser-Wärmepumpen zwischen 150 und 750, etwa bei R32, reduziert sich die
Förderung bei Monoblockgeräten bis 50 kW und Splitgeräten bis 12 kW um 20 %, also von 5.000 € auf
4.000 €. Geräte mit einem GWP über 750 sind ausgeschlossen. Laut Informationsblatt dürfen solche Monoblock-
und Splitgeräte mit GWP über 150 nach der F-Gase-Verordnung nur noch bis 1. Jänner 2027 in Verkehr gebracht
werden.</p>
{A.box("Photovoltaik ist nicht Teil der Kesseltausch-Förderung. PV-Anlagen werden separat über den "
       "EAG-Investitionszuschuss gefördert; der letzte Fördercall 2026 lief vom 8. bis 22. Oktober 2026, derzeit "
       "ist kein Bundeszuschuss beantragbar. Ab 2027 ist laut BMWET eine Systemförderung mit Antrag nach der "
       "Installation geplant, nicht beschlossen.")}
"""),
        ("Wer kann den Kesseltausch beantragen?", "antragsberechtigt", f"""
<p>Die Förderung richtet sich ausschließlich an Privatpersonen:</p>
<ul>
  <li><b>(Mit-)Eigentümerinnen und Eigentümer</b> von Ein- oder Zweifamilienhäusern und Reihenhäusern
  im Inland, unabhängig davon, ob dort der Hauptwohnsitz liegt.</li>
  <li><b>Bauberechtigte</b> an einem Grundstück mit bestehendem Wohngebäude.</li>
  <li><b>Mieterinnen und Mieter</b>, wenn sie die Zustimmung des Eigentümers zum Heizungstausch nachweisen.</li>
</ul>
<p>Es gibt keine Einkommensprüfung und kein Mindestalter für die alte Heizanlage; sie muss aber
mindestens eine Heizperiode in Betrieb gewesen sein. Entscheidend ist, dass ein fossiles Heizsystem
vollständig durch ein klimafreundliches ersetzt wird. Pro Standort ist nur ein Antrag möglich: In einem
Zweifamilienhaus mit gemeinsamer Zentralheizung gibt es einen gemeinsamen Antrag.
Für Haushalte mit geringem Einkommen gab es 2026
{a('/sauber-heizen-fuer-alle-2026/', '„Sauber Heizen für Alle“')} mit bis zu 100 % der Kosten; dieses
Programm bleibt geschlossen. Laut BMLUK soll das Angebot für einkommensschwache Haushalte künftig in die
Sanierungsoffensive integriert werden, Details gibt es noch nicht. Der Kesseltausch steht ohne
Einkommensgrenze auch diesen Haushalten offen.</p>
"""),
        ("Was gefördert wird und was nicht", "foerderfaehig", f"""
<h3>Förderfähige Kosten</h3>
<ul>
  <li><b>Material:</b> Wärmepumpe, Speicher, Verrohrung, Regelungstechnik und Zubehör.</li>
  <li><b>Montage:</b> Installation durch eine befugte Fachkraft.</li>
  <li><b>Planung:</b> technische Planung und Auslegung der neuen Heizanlage.</li>
  <li><b>Demontage und Entsorgung:</b> Abbau der alten Heizung, Entsorgung von Kessel und Brennstofftanks.</li>
</ul>
<p>Gefördert wird ein Zentralheizungssystem mit wassergeführter Wärmeverteilung. Ersetzt werden können
Öl- und Gasheizungen, Allesbrenner für Kohle oder Koks und fix verbaute Elektroheizungen wie
Elektrospeicheröfen. Rechnungen müssen auf die antragstellende Person lauten und von ihr bezahlt sein. In
der Neuauflage förderfähig sind Lieferungen und Leistungen ab dem 7. Oktober 2026; maßgeblich ist das
Lieferdatum des Wärmeerzeugers (in der ersten Aktion galt der 3. Oktober 2025).</p>
<h3>Nicht förderfähig</h3>
<ul>
  <li><b>Eigenleistungen:</b> In Eigenregie errichtete Anlagen sind vollständig ausgeschlossen.</li>
  <li><b>Gebrauchte Anlagen:</b> Nur Neuanschaffungen werden gefördert.</li>
  <li><b>Photovoltaik:</b> eigenes Programm (EAG-Investitionszuschuss, letzter Call 2026 beendet), siehe
  {a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}.</li>
</ul>
"""),
        ("Technische Voraussetzungen für die Wärmepumpe", "technik", f"""
{A.table(
    ["Kriterium", "Anforderung"],
    [
        ["EHPA-Gütesiegel", "Kriterien der European Heat Pump Association in gültiger Version, bestätigt durch ein unabhängiges Prüfinstitut; Gerät auf der Liste förderungsfähiger Wärmepumpen"],
        ["Kältemittel", "GWP höchstens 750; R290 (GWP 3) volle Förderung, Luft-Wasser mit GWP 150 bis 750 Abzug von 20 %"],
        ["Vorlauftemperatur", "maximal 55 °C, ideal mit Fußbodenheizung oder großflächigen Heizkörpern"],
        ["Leistung", "unter 100 kW für Ein-, Zweifamilien- und Reihenhäuser"],
        ["Fernwärme-Prüfung", "Anschluss an ein klimafreundliches Fernwärmenetz technisch nicht möglich oder wirtschaftlich nicht zumutbar (Wärmepumpe mindestens 25 % günstiger als der Anschluss)"],
        ["Altanlage", "fossile Heizung und Tanks stilllegen und entsorgen; nicht entsorgbare Tanks entleeren, reinigen, verplomben"],
    ],
)}
<p>Die Fernwärme-Prüfung ist in den meisten ländlichen und vorstädtischen Gebieten erfüllt, weil dort
kein Netz verfügbar ist. Legt der Fernwärmebetreiber binnen drei Monaten ab Anfrage kein Angebot, ist die
Wärmepumpe laut KPC ebenfalls förderbar. Ob Ihr Gebäude die 55 °C Vorlauftemperatur einhält, klärt der
Ratgeber {a('/waermepumpe-im-altbau/', 'Wärmepumpe im Altbau')}.</p>
"""),
        ("So läuft die Antragstellung ab", "ablauf", f"""
<p>Der Förderprozess besteht aus zwei Schritten: Registrierung und Antrag mit Endabrechnung. Vorher
braucht es eine Energieberatung, dazwischen setzen Sie den Heizungstausch um.</p>
{A.steps([
    ("Energieberatung durchführen lassen",
     "Bei der Registrierung muss ein Energieberatungsprotokoll Ihres Bundeslandes vorliegen. "
     "Die Beratung kann vor Ort, telefonisch oder digital stattfinden und muss den konkreten "
     "Standort betreffen. Ein Energieausweis ersetzt das Protokoll nicht."),
    ("Online registrieren",
     "Auf sanierungsoffensive.gv.at mit ID Austria oder Lichtbildausweis, mit Angaben zur Maßnahme, zu den "
     "voraussichtlichen Kosten und zum ausführenden Fachbetrieb. Möglich seit 2. November 2026, solange Budget "
     "vorhanden ist, längstens bis 31. Dezember 2026. Registriert werden kann ein geplantes oder ein bereits "
     "umgesetztes Projekt. Danach ist das Budget 9 Monate für Sie reserviert."),
    ("Heizungstausch umsetzen",
     "Eine befugte Fachkraft installiert die Wärmepumpe, die Altanlage wird abgebaut, Kessel und "
     "Tanks werden entsorgt. Sammeln Sie alle Rechnungen, sie müssen auf Ihren Namen lauten und bezahlt sein."),
    ("Antrag und Endabrechnung einreichen",
     "Innerhalb von 9 Monaten nach der Registrierung laden Sie Endabrechnungsformular und alle "
     "Schlussrechnungen im Portal hoch; die Heizung muss dann fertig installiert und abgerechnet sein. Die "
     "Kommunalkredit Public Consulting (KPC) prüft, das Ministerium genehmigt, danach wird die Förderung auf "
     "Ihr Konto überwiesen."),
])}
{A.box_dark("Früh registrieren, Frist im Blick behalten",
    "Die Registrierung ist nur bis 31. Dezember 2026 offen und endet früher, wenn das Budget aufgebraucht "
    "ist. Holen Sie Energieberatung und Angebot daher jetzt ein. Ab der Registrierung laufen 9 Monate: Wird "
    "der Antrag nicht in dieser Frist eingereicht, verfällt die Reservierung. Planen Sie Liefertermin und "
    "Montage so, dass sie hineinpassen.")}
{A.cta("Kesseltausch jetzt förderkonform planen",
       "EBZ Energie plant die Wärmepumpe nach den Kriterien der Neuauflage, unterstützt bei Energieberatung "
       "und Registrierung und prüft zusätzlich die Landesförderung.",
       secondary=("waermepumpe", "Zur Wärmepumpen-Leistungsseite"))}
"""),
        ("Zeitplan und Fristen der Sanierungsoffensive 2026", "fristen", f"""
{A.table(
    ["Datum", "Was gilt"],
    [
        ["3. Oktober 2025", "Stichtag der ersten Aktion 2026: Leistungen ab diesem Datum förderfähig"],
        ["24. November 2025", "Start der Online-Registrierung der ersten Aktion auf sanierungsoffensive.gv.at"],
        ["2. Februar 2026", "Fokus auf den Kesseltausch; keine neuen Registrierungen mehr für den Sanierungsbonus"],
        ["Herbst 2026", "erste Aktion ausgeschöpft, Registrierung geschlossen (Stand 9. Oktober 2026)"],
        ["7. Oktober 2026", "Stichtag der Neuauflage: Lieferungen und Leistungen ab diesem Datum förderfähig"],
        ["2. November 2026", "Start der Neuauflage: Registrierung und Antrag wieder möglich"],
        ["31. Dezember 2026", "letzter Tag für Registrierung und Antrag, sofern das Budget nicht früher aufgebraucht ist"],
        ["9 Monate ab Registrierung", "Frist für Umsetzung und Antrag mit Rechnungen"],
    ],
    hl_cols=(0,),
)}
<p><b>Budgetstand (November 2026):</b> Registrierungen werden angenommen, solange Mittel vorhanden sind.
Die Neuauflage speist sich aus frei gewordenen Mitteln des Zusagerahmens 2026; wie lange sie reichen, ist
nicht veröffentlicht. Für 2027 sind laut BMLUK 179 Millionen Euro für den Kesseltausch vorgesehen.</p>
<h3>Landesförderungen: zusätzlich kombinierbar</h3>
<p>Der Kesseltausch des Bundes lässt sich mit den Programmen der Bundesländer kombinieren, sofern das Land
das zulässt. In Kärnten, einer Kernregion von EBZ Energie, zahlt das Land 2026 eine Pauschale von 3.000 €
(plus 1.500 € bei Errichtung einer Solaranlage, plus 200 € für den hydraulischen Abgleich). Ersetzt eine
Luft-Wasser-Wärmepumpe einen Ölkessel, ergibt das 5.000 € Bund plus 3.000 € Land, zusammen bis 8.000 €*.
Ob das Landesbudget reicht, klären wir vor dem Angebot. Die Steiermark nimmt für neue Wärmepumpen derzeit
keine Förderanträge an; gefördert wird dort nur der Tausch mindestens 15 Jahre alter Biomassekessel oder
Wärmepumpen mit höchstens 30 %, höchstens 1.500 €. Für den Umstieg von Öl oder Gas bleibt in der
Steiermark damit der Bund mit 5.000 €. Alle Beträge und Bedingungen stehen im Ratgeber
{a('/landesfoerderungen-fuer-die-waermepumpe/', 'Landesförderungen für die Wärmepumpe')}. Wichtig:
Die Summe aus Bund, Land und Gemeinde darf die tatsächlichen Investitionskosten nicht übersteigen.
Alle Förderungen werden in der Transparenzdatenbank erfasst, unzulässige Mehrfachförderungen werden
zurückgefordert. Zusätzlich bringt die
{a('/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/', 'Öko-Sonderausgabenpauschale')}
fünf Jahre lang je 400 € Sonderausgaben, Voraussetzung ist die ausbezahlte Bundesförderung.</p>
<p><small>*Beispiel mit den Pauschalen laut Informationsblatt der KPC (Version 10/2026) und der
Landesförderung Kärnten 2026. Die tatsächliche Förderung hängt von Anlage, Kältemittel, Budget und den
Bedingungen der Förderstellen ab.</small></p>
"""),
        ("Wärmepumpe und Photovoltaik: die Kombination, die unabhängig macht", "photovoltaik", f"""
<p>Eine Wärmepumpe verbraucht rund 3.000 bis 5.000 kWh Strom pro Jahr. Mit einer passend
dimensionierten {a('photovoltaik', 'PV-Anlage')} decken Sie einen Großteil dieses Bedarfs selbst und
speisen den Überschuss ein oder speichern ihn. Photovoltaik wurde 2026 über den EAG-Investitionszuschuss
gefördert: Der letzte Call lief vom 8. bis 22. Oktober 2026, derzeit ist kein Bundeszuschuss beantragbar. Ab
2027 ist laut BMWET eine Systemförderung für Speicher mit intelligenter Steuerung geplant, beantragt nach der
Installation (nicht beschlossen). Wer jetzt plant, baut daher mit Speicher und Energiemanagement, nutzt die
laufenden Landestöpfe und spart dauerhaft. Wie das technisch zusammenspielt, zeigt der Ratgeber
{a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}; die Kosten des Gesamtpakets
lassen sich über eine {a('finanzierung', 'Finanzierung')} verteilen, die Anlage gehört ab Tag 1 Ihnen.</p>
"""),
        ("Fazit: Was jetzt gilt", "fazit", f"""
<p>Der Kesseltausch läuft seit 2. November 2026 wieder: 5.000 € für die Wärmepumpe, plus 5.000 € bei
Erdwärme mit Bohrung und 2.500 € bei einer thermischen Solaranlage, ohne Prozentgrenze. In der ersten
Aktion 2026 waren es bis zu 7.500 €. Wer umsteigen will, holt jetzt Energieberatung und Angebot ein und
registriert bis 31. Dezember 2026, bevor das Budget aufgebraucht ist; danach bleiben 9 Monate für Umsetzung
und Antrag. Wer in der ersten Aktion registriert ist, hält seine Frist ein. Die Wärmepumpe muss die
bekannten Kriterien erfüllen (EHPA-Gütesiegel, GWP höchstens 750, Vorlauf 55 °C, Fachkraft). Einen Überblick
über alle Töpfe gibt der Ratgeber
{a('/waermepumpenfoerderung-in-oesterreich/', 'Wärmepumpenförderung in Österreich 2026')}.</p>
{A.cta("Jetzt die Förderung sichern",
       "Wir planen die Wärmepumpe förderkonform, unterstützen bei Energieberatung und Registrierung und "
       "rechnen Bund und Land für Ihr Projekt durch.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Ihr regionaler Partner für Wärmepumpe und Photovoltaik: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach ist Ihr Fachbetrieb für Wärmepumpen und Photovoltaik in Kärnten und "
                 "der Steiermark, mit zertifizierten Fachkräften. Wir kommen zu "
                 "Ihnen, analysieren das Gebäude, planen Wärmepumpe und PV als Gesamtlösung und übernehmen den "
                 "gesamten Förderprozess, von der Registrierung beim Bund bis zur Landesförderung."),
        "grid": [
            ("Beratung vor Ort", "Wir berechnen, welches System zu Ihrem Haus passt."),
            ("Komplette Förderabwicklung", "Registrierung und Antrag beim Bund, Landesförderung, Endabrechnung."),
            ("Installation aus einer Hand", "Wärmepumpe und PV vom selben Team, klare Verantwortlichkeiten."),
            ("Regionale Expertise", "Wir kennen die Landesförderungen in Kärnten und der Steiermark."),
        ],
    },

    "faq": [
        ("Kann ich mich noch für die Sanierungsoffensive 2026 registrieren?",
         "Ja, seit 2. November 2026 wieder. Der Kesseltausch für Ein-, Zweifamilien- und Reihenhäuser ist neu "
         "aufgelegt, Registrierung und Antrag sind möglich, solange Budget vorhanden ist, längstens bis "
         "31. Dezember 2026. Vor der Registrierung brauchen Sie ein Energieberatungsprotokoll Ihres Bundeslandes."),
        ("Wie geht es 2027 mit der Bundesförderung weiter?",
         "Laut BMLUK sind 2027 im Rahmen der Sanierungsoffensive 179 Millionen Euro für den Kesseltausch "
         "vorgesehen. Die Förderhöhe soll sich 2027 laut Aktionsseite nicht ändern. Wir aktualisieren diesen "
         "Ratgeber, sobald die Bedingungen für 2027 veröffentlicht sind."),
        ("Kann ich die Förderung beantragen, wenn ich keinen Hauptwohnsitz am Standort habe?",
         "Ja. Ein Haupt- oder Nebenwohnsitz am Standort ist keine Voraussetzung, die Förderung gilt für Ein-, "
         "Zweifamilien- und Reihenhäuser im Inland, auch wenn Sie dort nur zeitweise wohnen. Entscheidend ist, "
         "dass die zu Wohnzwecken genutzte Fläche mehr als 50 % des Gebäudes ausmacht und die fossile Heizung "
         "vollständig ersetzt wird."),
        ("Gilt noch die Grenze von 30 % der Kosten?",
         "Nein. In der Neuauflage entfällt die prozentuelle Begrenzung, es gelten die Pauschalen laut "
         "Informationsblatt. Alle Förderungen zusammen dürfen aber die Investitionskosten nicht übersteigen. In "
         "der ersten Aktion 2026 war die Förderung mit 30 % der förderfähigen Kosten gedeckelt: Bei 15.000 € "
         "Kosten gab es dort 4.500 € statt der Pauschale von 7.500 €."),
        ("Brauche ich einen Energieausweis für den Förderantrag?",
         "Nein. Für den Kesseltausch ist kein Energieausweis nötig, er wird für die Registrierung auch nicht "
         "anerkannt. Nötig ist ein Energieberatungsprotokoll Ihres Bundeslandes. Die Beratung kann vor Ort, "
         "telefonisch oder digital erfolgen und muss bei der Registrierung vorliegen. EBZ Energie unterstützt "
         "bei der Organisation des Termins."),
        ("Wird auch der Austausch einer Elektroheizung gefördert?",
         "Ja. Der Ersatz stationärer oder fix verbauter Elektroheizungen wie Elektrospeicheröfen wird mit "
         "denselben Sätzen und Voraussetzungen gefördert wie der Tausch einer Öl- oder Gasheizung. Die alte "
         "Stromheizung muss vollständig stillgelegt werden, die neue Anlage muss eine Zentralheizung mit "
         "wassergeführter Wärmeverteilung sein."),
        ("Ich bin in der ersten Aktion 2026 registriert. Was gilt für mich?",
         "Ihre Reservierung gilt 9 Monate ab Registrierung für Umsetzung und Hochladen der Endabrechnung, nach "
         "den Bedingungen der ersten Aktion. Prüfen Sie den Stand Ihrer Reservierung im KPC-Kundenportal und "
         "halten Sie die Frist ein; maßgeblich ist Ihre Registrierungsbestätigung."),
        ("Wie hoch ist die Förderung für eine Erdwärme-Wärmepumpe?",
         "Zur Pauschale von 5.000 € kommt bei Sole-Wasser- oder Wasser-Wasser-Wärmepumpen mit neuer "
         "Tiefenbohrung oder neuem Brunnen ein Bohrbonus von 5.000 €, in Summe bis zu 10.000 € vom Bund, mit "
         "thermischer Solaranlage bis zu 12.500 €. Flächen- oder Ringgrabenkollektoren, Erdwärmekörbe und "
         "Eisspeicher erhalten keinen Bohrbonus."),
        ("Reduziert das Kältemittel R32 die Förderung?",
         "Ja. Bei Luft-Wasser-Wärmepumpen mit einem GWP-Wert zwischen 150 und 750, wie bei R32, sinkt die "
         "Förderung bei Monoblockgeräten bis 50 kW und Splitgeräten bis 12 kW um 20 %, also von 5.000 € auf "
         "4.000 €. Geräte mit dem natürlichen Kältemittel R290 (Propan, GWP 3) erhalten die volle Förderung, "
         "Geräte mit GWP über 750 gar keine."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Wärmepumpen und Photovoltaik in Kärnten und der Steiermark und übernimmt die Registrierung "
                    "und Endabrechnung bei der Sanierungsoffensive. Konditionen der Neuauflage: Informationsblatt "
                    "und FAQ der KPC (Version 10/2026) und Aktionsseite, geprüft am 19. November 2026. Keine Rechts- "
                    "oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("KPC: Informationsblatt Kesseltausch 2026 Ein-/Zweifamilienhaus/Reihenhaus, Neuauflage ab 2.11.2026 (Version 10/2026)",
         "https://www.sanierungsoffensive.gv.at/fileadmin/user_upload/2026/Infoblatt_Neuauflage_Kesseltausch_2026_EFH.pdf"),
        ("Sanierungsoffensive: Aktionsseite Kesseltausch Neuauflage Ein-/Zweifamilienhaus oder Reihenhaus",
         "https://www.sanierungsoffensive.gv.at/kesseltausch/neuauflage-ein-/zweifamilienhaus-oder-reihenhaus"),
        ("KPC: Häufig gestellte Fragen Kesseltausch 2026 und Neuauflage (Version 10/2026)",
         "https://www.sanierungsoffensive.gv.at/fileadmin/user_upload/2026/faq_Kesseltausch_2026_EFH.pdf"),
        ("BMLUK: Sanierung und Kesseltausch 2027",
         "https://www.bmluk.gv.at/themen/klima-und-umwelt/klima/klima-initiativen-und-foerderungen/ufg/sanierung-kesselaustausch-2027.html"),
        ("Land Steiermark: Förderung für Heizungen (Wohnbau, Stand 10. Oktober 2026)",
         "https://www.wohnbau.steiermark.at/cms/ziel/164947118/DE/"),
    ],
    "related": [
        ("/waermepumpenfoerderung-in-oesterreich/", "Wärmepumpenförderung Österreich 2026: Überblick"),
        ("/landesfoerderungen-fuer-die-waermepumpe/", "Landesförderungen: alle 9 Bundesländer"),
        ("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau: Voraussetzungen"),
        ("waermepumpe", "Wärmepumpen-Installateur EBZ Energie"),
    ],
    "cta": {
        "h3": "Förderung sichern",
        "text": "Kesseltausch läuft bis 31. Dezember 2026: Wir planen förderkonform und unterstützen bei Registrierung und Antrag.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre neue Wärmepumpe: Förderung jetzt nutzen",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
