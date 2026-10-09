"""Ratgeber: Sanierungsoffensive 2026 (Bundesförderung Kesseltausch, bis 7.500 € für Wärmepumpen).

Stand Oktober 2026: Programm BEENDET, Mittel ausgeschöpft, keine Registrierung mehr (umweltfoerderung.at,
9.10.2026). Konditionen bleiben als "galt 2026" dokumentiert, Status-Box oben, Alternativen genannt.

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
    "title": "Sanierungsoffensive 2026: beendet, das gilt jetzt | EBZ",
    "description": ("Sanierungsoffensive 2026: Kesseltausch-Förderung bis 7.500 € seit Herbst 2026 ausgeschöpft, "
                    "keine Registrierung mehr. Was 2026 galt, Alternativen, Ausblick."),
    "eyebrow": "Förderung · Bund",
    "crumb_label": "Sanierungsoffensive 2026",
    "h1": "Sanierungsoffensive 2026: Programm beendet, Mittel ausgeschöpft. Was jetzt für Ihre Wärmepumpe gilt",
    "lead": ("Stand Oktober 2026: Die Bundesförderung für den Kesseltausch (bis zu 7.500 €, mit Bohrbonus 12.500 €) "
             "ist ausgeschöpft, neue Registrierungen sind nicht mehr möglich. Hier finden Sie den aktuellen Status, "
             "die Konditionen, die 2026 galten, und die Alternativen, die jetzt noch offen sind."),
    "chips": [
        "Status: <b>beendet</b> (Stand Oktober 2026)",
        "Galt 2026: <b>bis 7.500 €</b> Wärmepumpe",
        "Bohrbonus Erdwärme: <b>+5.000 €</b> (galt 2026)",
        "Alternative: <b>Landesförderung</b> + Steuer",
    ],
    "date_published": "2026-03-10",
    "date_modified": "2026-10-09",
    "hero_img": "waermepumpe",
    "hero_alt": "Luft-Wasser-Wärmepumpe an der Hauswand eines Einfamilienhauses",

    "tldr": [
        "Stand Oktober 2026: Die Sanierungsoffensive 2026 (Sanierungsbonus und Kesseltausch) ist beendet. Die "
        "Mittel sind ausgeschöpft, eine Registrierung oder Antragstellung ist nicht mehr möglich (Quelle: "
        "umweltfoerderung.at).",
        "Was 2026 galt: Tausch einer fossilen Heizung im Ein-, Zweifamilien- oder Reihenhaus mit bis zu 7.500 € "
        "für Wärmepumpen, 8.500 € für Holzzentralheizungen und 6.500 € für Fernwärmeanschluss. Deckel: 30 % der "
        "förderfähigen Kosten.",
        "Boni: 5.000 € Bohrbonus für Sole-Wasser- oder Wasser-Wasser-Wärmepumpen, 2.500 € für eine thermische "
        "Solaranlage ab 6 m². Bei Kältemitteln mit GWP 150 bis 750 (z. B. R32) sinkt die Förderung um 20 %.",
        "Voraussetzungen: EHPA-Gütesiegel, GWP höchstens 750, Vorlauftemperatur maximal 55 °C, Leistung unter "
        "100 kW, Installation durch einen befugten Fachbetrieb, Energieberatungsprotokoll bei der Registrierung.",
        "Bereits Registrierte: Die Reservierung lief 9 Monate ab Registrierung für Umsetzung und Endabrechnung. "
        "Den Stand der eigenen Reservierung zeigt das KPC-Kundenportal.",
        "Alternativen jetzt: Landesförderungen in Kärnten und der Steiermark (ob ohne Bundesförderung möglich, "
        "klärt die Landesstelle). Die Öko-Sonderausgabenpauschale gilt nur mit ausbezahlter Bundesförderung. Ob "
        "2027 ein neues Bundesprogramm kommt, ist offen.",
    ],
    "kpis": [
        ("beendet", "Stand Oktober 2026: Mittel ausgeschöpft"),
        ("7.500 €", "Grundpauschale Wärmepumpe (galt 2026)"),
        ("9 Monate", "Frist für bereits Registrierte"),
        ("35 %", "Landesförderung Kärnten/Steiermark laut Richtlinie, Stand prüfen"),
    ],

    "sections": [
        ("Stand Oktober 2026: Programm beendet, Mittel ausgeschöpft", "status", f"""
{A.box_dark("Sanierungsoffensive 2026: keine Registrierung mehr möglich",
    "Die Sanierungsoffensive mit Sanierungsbonus und Kesseltausch (Ein- und Zweifamilienhaus 2026) ist laut "
    "umweltfoerderung.at beendet: Die Mittel sind ausgeschöpft, eine Registrierung oder Antragstellung ist nicht "
    "mehr möglich (Stand 9. Oktober 2026). Auch „Sauber Heizen für Alle 2026“ nimmt keine neuen Registrierungen "
    "an; wer dort bereits registriert ist, kann noch beantragen. Ob 2027 ein neues Bundesprogramm kommt, ist offen.")}
<p>Was jetzt weiterhin gilt: Die Landesförderungen für den Heizungstausch laufen weiter; mehrere Länder, darunter
Kärnten, vergeben sie bisher als Anschlussförderung an den Bund, den aktuellen Stand klären Sie vor der
Antragstellung mit der Landesstelle (Kärnten, Steiermark). Die steuerliche
{a('/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/', 'Öko-Sonderausgabenpauschale')}
(fünf Jahre je 400 € Sonderausgaben) setzt eine ausbezahlte Bundesförderung voraus und bleibt damit für
registrierte Projekte relevant. Wer sein Projekt vor dem Förderstopp registriert hat, prüft den
Status seiner Reservierung im KPC-Kundenportal; maßgeblich sind die Informationen auf umweltfoerderung.at.
Alle Angaben weiter unten beschreiben die Konditionen, die 2026 galten, und bleiben für bereits registrierte
Projekte sowie als Referenz für ein mögliches Folgeprogramm relevant. Den Überblick über alle Töpfe gibt der
Ratgeber {a('/waermepumpenfoerderung-in-oesterreich/', 'Wärmepumpenförderung in Österreich')}.</p>
"""),
        ("Warum der Bund 2026 auf den Kesseltausch gesetzt hat", "hintergrund", f"""
<p>Jede fünfte Heizung in Österreich läuft noch mit Öl oder Gas. Das bedeutet hohe Energiekosten,
steigende CO₂-Abgaben und Abhängigkeit von internationalen Energiemärkten. Die Bundesregierung hat
deshalb für die Sanierungsoffensive im Zeitraum 2026 bis 2030 jährlich 360 Millionen Euro angekündigt,
insgesamt 1,8 Milliarden Euro. Innerhalb eines Jahres kann das Budget aber ausgeschöpft sein, weil
Registrierungen nach Reihenfolge des Eingangs angenommen werden. Genau das ist 2026 passiert: Im Herbst
waren die Mittel aufgebraucht, die Registrierung wurde geschlossen.</p>
<p>Der Kesseltausch steht im Mittelpunkt, weil der Austausch einer fossilen Heizung durch eine
{a('waermepumpe', 'Wärmepumpe')} die höchste CO₂-Einsparung pro Fördereuro erzielt. Seit 2. Februar 2026
konzentriert der Bund die Mittel auf den Kesseltausch. Neue Registrierungen für den Sanierungsbonus
(thermische Gebäudesanierung wie Dämmung oder Fenstertausch) werden seither nicht mehr angenommen.</p>
"""),
        ("Wie hoch war die Förderung beim Kesseltausch 2026?", "foerderhoehe", f"""
<p>Der Zuschuss war ein nicht rückzahlbarer Einmalbetrag, der nach Prüfung direkt auf das Konto
ausbezahlt wird. Er ist mit maximal 30 % der förderfähigen Investitionskosten gedeckelt. Für Ein- oder
Zweifamilienhäuser und Reihenhäuser galten 2026 diese Grundpauschalen und Boni (für neue Projekte seit
Herbst 2026 nicht mehr verfügbar):</p>
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
       "EAG-Investitionszuschuss gefördert; der letzte Fördercall 2026 läuft bis 22. Oktober 2026, ab 2027 ist "
       "laut BMWET eine Systemförderung mit Antrag nach der Installation geplant.")}
"""),
        ("Wer konnte den Kesseltausch 2026 beantragen?", "antragsberechtigt", f"""
<p>Die Förderung richtete sich an Privatpersonen:</p>
<ul>
  <li><b>(Mit-)Eigentümerinnen und Eigentümer</b> von Ein- oder Zweifamilienhäusern und Reihenhäusern
  im Inland, unabhängig davon, ob dort der Hauptwohnsitz liegt.</li>
  <li><b>Bauberechtigte</b> an einem Grundstück mit bestehendem Wohngebäude.</li>
  <li><b>Mieterinnen und Mieter</b>, wenn sie die Zustimmung des Eigentümers zum Heizungstausch nachweisen.</li>
</ul>
<p>Es gibt keine Einkommensgrenze und kein Mindestalter für die alte Heizanlage. Entscheidend ist, dass
ein fossiles Heizsystem vollständig durch ein klimafreundliches ersetzt wird. Pro Standort ist nur ein
Antrag möglich: In einem Zweifamilienhaus mit gemeinsamer Zentralheizung gibt es einen gemeinsamen Antrag.
Für Haushalte mit geringem Einkommen gab es parallel
{a('/sauber-heizen-fuer-alle-2026/', '„Sauber Heizen für Alle“')} mit bis zu 100 % der Kosten; auch dieses
Programm nimmt seit Herbst 2026 keine neuen Registrierungen mehr an.</p>
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
        ("So lief die Antragstellung ab (für bereits Registrierte weiterhin relevant)", "ablauf", f"""
<p>Der Förderprozess bestand aus zwei Schritten: Registrierung und Endabrechnung. Neue Registrierungen
sind seit Herbst 2026 nicht mehr möglich; wer registriert ist, durchläuft die Schritte 3 und 4.</p>
{A.steps([
    ("Energieberatung durchführen lassen",
     "Bereits bei der Registrierung muss ein gültiges Energieberatungsprotokoll Ihres Bundeslandes vorliegen. "
     "Die Beratung kann vor Ort, telefonisch oder per Videokonferenz stattfinden und muss den konkreten "
     "Standort betreffen. Ein Energieausweis ist nicht erforderlich."),
    ("Online registrieren",
     "Auf sanierungsoffensive.gv.at mit ID Austria oder Lichtbildausweis, mit Angaben zur Maßnahme und den "
     "voraussichtlichen Kosten. Möglich war das seit 24. November 2025, solange Budget vorhanden war; seit Herbst "
     "2026 ist die Registrierung geschlossen. Registrierte haben eine Bestätigung per E-Mail und Zugangsdaten zur "
     "Plattform erhalten, das Budget ist ab der Registrierung 9 Monate reserviert."),
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
{A.cta("Alternativen prüfen, Technik förderkonform planen",
       "EBZ Energie prüft, welche Landesförderung für Ihr Projekt aktuell "
       "möglich ist, und plant die Wärmepumpe so, dass sie auch die Kriterien eines möglichen Folgeprogramms erfüllt.",
       secondary=("waermepumpe", "Zur Wärmepumpen-Leistungsseite"))}
"""),
        ("Zeitplan und Fristen der Sanierungsoffensive 2026", "fristen", f"""
{A.table(
    ["Datum", "Was gilt"],
    [
        ["3. Oktober 2025", "Stichtag: Leistungen ab diesem Rechnungsdatum sind rückwirkend förderfähig"],
        ["24. November 2025", "Start der Online-Registrierung auf sanierungsoffensive.gv.at"],
        ["2. Februar 2026", "Fokus auf den Kesseltausch; keine neuen Registrierungen mehr für den Sanierungsbonus"],
        ["Herbst 2026", "Mittel ausgeschöpft, Registrierung geschlossen (Stand 9. Oktober 2026, umweltfoerderung.at)"],
        ["31. Dezember 2026", "ursprünglich letztmöglicher Tag für die Registrierung, durch das Budgetende hinfällig"],
        ["9 Monate ab Registrierung", "Frist für Installation und Hochladen der Endabrechnung (für Registrierte)"],
    ],
    hl_cols=(0,),
)}
<p><b>Budgetstand (Oktober 2026):</b> Die Mittel sind ausgeschöpft. Im April 2026 waren laut Berichten
bereits über 60 % gebunden, seit der Konzentration auf den Kesseltausch im Februar war die Nachfrage stark
gestiegen. Ob und in welcher Form 2027 ein neues Bundesprogramm folgt, ist offen.</p>
<h3>Landesförderungen: jetzt der wichtigste Topf</h3>
<p>Für bereits registrierte Projekte kann die Bundesförderung mit den Programmen der Bundesländer
kombiniert werden. Für neue Projekte sind die Landesförderungen derzeit die wichtigste Unterstützung: In
Kärnten und der Steiermark, den Kernregionen von EBZ Energie, geht es um mehrere Tausend Euro. Ob ein Land
ohne Bundesförderung zahlt, regelt seine Richtlinie (Kärnten vergab die Förderung bisher als Anschlussförderung
an den Bund); klären Sie den Stand vor der Antragstellung mit der Landesstelle. Alle Beträge
und Bedingungen stehen im Ratgeber
{a('/landesfoerderungen-fuer-die-waermepumpe/', 'Landesförderungen für die Wärmepumpe')}. Wichtig:
Die Summe aus Bund, Land und Gemeinde darf die tatsächlichen Investitionskosten nicht übersteigen.
Alle Förderungen werden in der Transparenzdatenbank erfasst, unzulässige Mehrfachförderungen werden
zurückgefordert. Zusätzlich bringt die
{a('/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/', 'Öko-Sonderausgabenpauschale')}
fünf Jahre lang je 400 € Sonderausgaben, Voraussetzung ist eine ausbezahlte Bundesförderung.</p>
"""),
        ("Wärmepumpe und Photovoltaik: die Kombination, die unabhängig macht", "photovoltaik", f"""
<p>Eine Wärmepumpe verbraucht rund 3.000 bis 5.000 kWh Strom pro Jahr. Mit einer passend
dimensionierten {a('photovoltaik', 'PV-Anlage')} decken Sie einen Großteil dieses Bedarfs selbst und
speisen den Überschuss ein oder speichern ihn. Photovoltaik wird über den EAG-Investitionszuschuss
gefördert: Der letzte Call 2026 läuft bis 22. Oktober 2026, ab 2027 plant das BMWET eine Systemförderung
für Speicher mit intelligenter Steuerung, beantragt nach der Installation. Wer beides gemeinsam plant,
nutzt die laufenden Töpfe und spart dauerhaft. Wie das technisch zusammenspielt, zeigt der Ratgeber
{a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}; die Kosten des Gesamtpakets
lassen sich über eine {a('finanzierung', 'Finanzierung')} verteilen, die Anlage gehört ab Tag 1 Ihnen.</p>
"""),
        ("Fazit: Was nach dem Förderstopp gilt", "fazit", f"""
<p>Die Sanierungsoffensive 2026 war mit bis zu 7.500 € (Erdwärme 12.500 €) das Fundament jedes
Heizungstausches, ist aber seit Herbst 2026 ausgeschöpft. Wer registriert ist, hält die 9-Monats-Frist für
Umsetzung und Endabrechnung ein. Wer neu plant, klärt die Landesförderung mit der Landesstelle
und baut die Wärmepumpe so, dass sie die bekannten Kriterien (EHPA-Gütesiegel, GWP unter 750, Vorlauf
55 °C, Fachbetrieb) erfüllt, falls 2027 ein neues Bundesprogramm kommt. Einen Überblick über alle Töpfe gibt
der Ratgeber {a('/waermepumpenfoerderung-in-oesterreich/', 'Wärmepumpenförderung in Österreich 2026')}.</p>
{A.cta("Jetzt die offenen Förderwege nutzen",
       "Wir prüfen die Landesförderung für Ihr Projekt, planen die Wärmepumpe förderkonform und "
       "informieren Sie, sobald ein neues Bundesprogramm startet.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Ihr regionaler Partner für Wärmepumpe und Photovoltaik: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach ist Ihr Fachbetrieb für Wärmepumpen und Photovoltaik in Kärnten und "
                 "der Steiermark, mit zertifizierten Fachkräften. Wir kommen zu "
                 "Ihnen, analysieren das Gebäude, planen Wärmepumpe und PV als Gesamtlösung und übernehmen den "
                 "gesamten Förderprozess, aktuell für die Landesförderung, bei Registrierten bis zur Endabrechnung."),
        "grid": [
            ("Beratung vor Ort", "Wir berechnen, welches System zu Ihrem Haus passt."),
            ("Komplette Förderabwicklung", "Landesförderung, Endabrechnung für Registrierte, neue Programme sobald verfügbar."),
            ("Installation aus einer Hand", "Wärmepumpe und PV vom selben Team, klare Verantwortlichkeiten."),
            ("Regionale Expertise", "Wir kennen die Landesförderungen in Kärnten und der Steiermark."),
        ],
    },

    "faq": [
        ("Kann ich mich noch für die Sanierungsoffensive 2026 registrieren?",
         "Nein. Stand Oktober 2026 ist die Sanierungsoffensive mit Sanierungsbonus und Kesseltausch beendet, die "
         "Mittel sind ausgeschöpft und eine Registrierung oder Antragstellung ist laut umweltfoerderung.at nicht "
         "mehr möglich. Offen bleiben die Landesförderungen (Bedingungen beim Land prüfen); die "
         "Öko-Sonderausgabenpauschale setzt eine ausbezahlte Bundesförderung voraus."),
        ("Kommt 2027 eine neue Bundesförderung für den Heizungstausch?",
         "Das ist offen. Der Bund hatte für 2026 bis 2030 jährlich 360 Millionen Euro angekündigt, ein konkretes "
         "Programm für 2027 ist aber noch nicht veröffentlicht. Wir aktualisieren diesen Ratgeber, sobald es "
         "offizielle Informationen gibt."),
        ("Konnte ich die Förderung beantragen, wenn ich keinen Hauptwohnsitz am Standort habe?",
         "Ja. Ein Hauptwohnsitz am Standort war keine Voraussetzung, die Förderung galt für Wohngebäude im "
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
        ("Ich habe vor dem Förderstopp registriert. Was gilt für mich?",
         "Für registrierte Projekte galt die Reservierung 9 Monate ab Registrierung für Umsetzung und Hochladen "
         "der Endabrechnung. Prüfen Sie den Stand Ihrer Reservierung im KPC-Kundenportal und halten Sie die Frist "
         "ein; maßgeblich sind die Informationen auf umweltfoerderung.at."),
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
                    "und Endabrechnung bei der Sanierungsoffensive. Status des Programms: Stand 9. Oktober 2026 laut "
                    "umweltfoerderung.at; Konditionen: Stand April 2026. Keine Rechts- oder Steuerberatung, "
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
        "h3": "Offene Förderwege prüfen",
        "text": "Bundesprogramm ausgeschöpft: Wir prüfen, welche Landesförderung für Ihren Heizungstausch offen ist, und planen förderkonform.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre neue Wärmepumpe: offene Förderwege nutzen",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
