"""Ratgeber: Förderung für PV-Speicher in Kärnten (Landesförderung 2025 und 2026, EAG-Bund, Kombination, Ablauf).

Migriert von ebz-photovoltaik.at/foerderung-pv-speicher-kaernten/ (Quelle Stand November 2025, Förderjahr
2025 mit 275 Euro je kWh). Die Kärntner Reform 2026 (3.000 Euro Pauschale, 1.000 Euro Nachrüstung) wurde
aus dem belegten Schwesterartikel photovoltaik_foerderung_kaernten.py ergänzt.
Stand ab 23.10.2026: EAG 3. und letzter Call lief 8. bis 22.10.2026, derzeit kein Bundeszuschuss; Ausblick 2027
Systemfoerderung laut BMWET (geplant, nicht beschlossen).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "foerderung-pv-speicher-kaernten",
    "path": "/foerderung-pv-speicher-kaernten/",
    "title": "PV-Speicher-Förderung Kärnten 2026: 3.000 € bis 31.12. | EBZ",
    "description": ("PV-Speicher-Förderung Kärnten 2026: 3.000 € Pauschale für PV mit Speicher, 1.000 € für die "
                    "Nachrüstung, 2. Call bis 31.12. Bundescall beendet, Ausblick 2027."),
    "eyebrow": "Förderung · Kärnten",
    "crumb_label": "PV-Speicher-Förderung Kärnten",
    "h1": "Förderung für PV-Speicher in Kärnten: 3.000 Euro Landespauschale, Bundescall 2026 beendet",
    "lead": ("Kärnten fördert Stromspeicher so stark wie kaum ein anderes Bundesland: bis 2025 mit 275 Euro je "
             "Kilowattstunde, seit 2026 mit einer Pauschale von 3.000 Euro für neue PV-Anlagen mit Speicher, "
             "im Call 2026 voll kombinierbar mit dem EAG-Zuschuss des Bundes. Der letzte Bundescall lief vom 8. bis "
             "22. Oktober 2026, derzeit ist der Bund nicht beantragbar. Dieser Ratgeber zeigt die Stände, die "
             "Voraussetzungen und den Ablauf."),
    "chips": [
        "2026: <b>3.000 €</b> Pauschale (PV + Speicher)",
        "Nachrüstung: <b>1.000 €</b> ab 5 kWh",
        "Bund: <b>150 €/kWh</b> im Call 2026, beendet",
        "2. Landes-Call: <b>12. Oktober bis 31. Dezember 2026</b>",
    ],
    "date_published": "2025-07-25",
    "date_modified": "2026-10-21",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus in Kärnten mit Photovoltaikanlage und Batteriespeicher",

    "tldr": [
        "Kärnten 2026: 3.000 Euro Pauschale für neue private PV-Anlagen ab 5 kWp mit Speicher ab 5 kWh nutzbarer "
        "Kapazität, 1.000 Euro für die Speicher-Nachrüstung an Bestandsanlagen. Reine PV-Anlagen ohne Speicher "
        "fördert das Land nicht mehr.",
        "Im Call 2026 war die Landesförderung voll mit dem EAG-Bundeszuschuss kombinierbar (150 Euro je kWp bis "
        "10 kWp, 150 Euro je kWh Speicher), ohne Anrechnung; für 10 kWp mit 10 kWh ergab das 6.000 Euro. Der letzte "
        "Call endete am 22. Oktober 2026, aktuell bleiben 3.000 Euro vom Land, der Bund ist derzeit nicht beantragbar.",
        "Bis 2025 zahlte das Land 275 Euro je kWh Speicherkapazität (bis 10 kWh), eine der höchsten "
        "Speicherförderungen Österreichs; die Kombination mit dem Bund war für gewerbliche und kommunale Anlagen "
        "vorgesehen.",
        "Termine: Die EAG-Calls 2026 (ab 23. April, 16. Juni, 8. Oktober) sind beendet, der letzte lief vom 8. bis "
        "22. Oktober 2026. Der Landesantrag kommt nach Fertigstellung im 2. Call zwischen 12. Oktober und "
        "31. Dezember 2026 (1. Call: 15. April bis 30. Juni), Rechnungen datiert nach dem 1. Jänner 2026. Ab 2027 "
        "ist laut BMWET eine Systemförderung für Speicher mit intelligenter Steuerung geplant, nicht beschlossen.",
        "Der Andrang ist groß, Budgets sind begrenzt. Vollständige Unterlagen (Angebot, Datenblätter, "
        "Zählpunkt, Nachweise) und eine frühzeitige Einreichung entscheiden.",
    ],
    "kpis": [
        ("3.000 €", "Landespauschale 2026 für PV ab 5 kWp mit Speicher ab 5 kWh"),
        ("1.000 €", "Landespauschale 2026 für die Speicher-Nachrüstung"),
        ("275 €/kWh", "Speicherförderung des Landes im Förderjahr 2025"),
        ("6.000 €", "Bund plus Land im Call 2026 für 10 kWp mit 10 kWh"),
    ],

    "sections": [
        ("Das Kärntner Modell: Speicherförderung im Wandel", "landesfoerderung", f"""
<p>Kärnten hat sich ambitionierte Ziele für die Energiewende gesetzt und untermauert sie mit einem der
stärksten Landesprogramme Österreichs. Im Gegensatz zu Bundesländern, die sich auf den Bund verlassen, setzt
das Land einen eigenen Anreiz für netzdienliche Anlagen mit Speicher. Das Programm wurde für 2026 grundlegend
vereinfacht: Statt eines Zuschusses je Kilowattstunde gibt es Pauschalen.</p>
{A.table(
    ["Förderschiene Land Kärnten", "Förderjahr 2025", "Förderjahr 2026"],
    [
        ["Neue PV-Anlage mit Speicher", "PV-Zuschuss plus 275 €/kWh Speicher (bis 10 kWh)", "3.000 € Pauschale (ab 5 kWp PV, ab 5 kWh nutzbar)"],
        ["Speicher-Nachrüstung an Bestandsanlage", "275 €/kWh (bis 10 kWh)", "1.000 € Pauschale (ab 5 kWh)"],
        ["Reine PV-Anlage ohne Speicher", "PV-Zuschuss des Landes", "keine Landesförderung, EAG-Bund nur im Call 2026"],
        ["Kombination mit EAG-Bund", "für gewerbliche und kommunale Anlagen vorgesehen", "im Call 2026 ja, ohne Anrechnung; Bund derzeit nicht beantragbar"],
        ["Antragszeitpunkt", "vor Projektbeginn, digital", "nach Fertigstellung, 2. Landes-Call 12. Oktober bis 31. Dezember 2026 (1. Call: 15. April bis 30. Juni)"],
    ],
    hl_cols=(2,),
)}
<p>Für einen typischen 10-kWh-Speicher bedeutete der Satz 2025 einen Zuschuss von 2.750 Euro. Die Pauschale
2026 von 3.000 Euro gilt unabhängig von der Anlagengröße: Eine 12-kWp-Anlage bekommt denselben Betrag wie eine
5-kWp-Anlage. Für betriebliche Eigenverbrauchsanlagen gibt es eine eigene Schiene mit bis zu 200 Euro je kWp.
Insgesamt stellt das Land 2026 rund 40 Millionen Euro für die Energieförderung bereit; der zweite Call vom
12. Oktober bis 31. Dezember 2026 ist mit rund 10 Millionen Euro dotiert, gedeckelt mit 50 Prozent der
Baukosten (Quelle: Land Kärnten, Stand Oktober 2026).</p>
<p><small>Stand: Förderjahr 2025 laut Quelle vom November 2025, Förderjahr 2026 laut Landesrichtlinie Kärnten
2026 und Ankündigung des 2. Calls (Stand Oktober 2026). Maßgeblich sind die jeweils gültigen Richtlinien des
Landes Kärnten.</small></p>
"""),
        ("Der EAG-Bundeszuschuss als zweite Säule", "eag-bund", f"""
<p>Neben dem Landesprogramm gab es 2026 den EAG-Investitionszuschuss des Bundes, abgewickelt über die
EAG-Abwicklungsstelle (OeMAG) in Fördercalls mit festem Budget. Er förderte die PV-Anlage je kWp und den
Speicher mit 150 Euro je kWh (maximal 50 kWh, nur gemeinsam mit einer neuen oder erweiterten PV-Anlage). Der
Zuschuss war ein direkter, nicht rückzahlbarer Betrag, ausbezahlt nach Inbetriebnahme und Endabrechnung; der
Antrag musste vor der Inbetriebnahme gestellt werden. Die Sätze sind derzeit nicht beantragbar.</p>
{A.table(
    ["EAG-Kategorie", "Anlagengröße", "Fördersatz PV 2026", "Speicher"],
    [
        ["A", "bis 10 kWp", "150 €/kWp", "150 €/kWh"],
        ["B", "über 10 bis 20 kWp", "140 €/kWp", "150 €/kWh"],
        ["C", "über 20 bis 100 kWp", "max. 130 €/kWp", "150 €/kWh"],
    ],
    hl_cols=(2, 3),
)}
<p>Die EAG-Calls 2026 liefen vom 23. April bis 11. Mai, vom 16. bis 30. Juni und vom 8. bis 22. Oktober. In den
Kategorien A und B galt First-Come-First-Served mit Ticketziehung. Der Made-in-Europe-Bonus brachte 10 Prozent
Zuschlag je Komponente von der White List der Abwicklungsstelle.</p>
<p><b>Stand ab 23. Oktober 2026:</b> Der dritte Call lief vom 8. bis 22. Oktober 2026 und war der letzte im
bisherigen System, neue Anlagen bekommen derzeit keinen Bundeszuschuss. Ab 2027 ist laut BMWET eine
Systemförderung geplant, aber nicht beschlossen: Antrag nach Installation und Rechnung, Speicher mit
intelligenter Steuerung im Mittelpunkt, auch die Nachrüstung soll förderbar werden. Projekte mit intelligentem
Speicher, die ab 1. November 2026 in Betrieb gehen, sollen 2027 beantragbar sein. Höhe und Kriterien sind offen.</p>
<p>Wer jetzt in Kärnten plant, baut deshalb sinnvoll mit Speicher und Energiemanagement: Das Land zahlt die
3.000 Euro nur mit Speicher, und die Anlage wahrt die Chance auf die Systemförderung 2027.</p>
<p>Zur Einordnung: Bis 31. März 2025 galt für kleine PV-Anlagen der Nullsteuersatz bei der Umsatzsteuer. Er
wurde 2026 durch den Investitionszuschuss abgelöst: ein fester Betrag, der die Anfangsinvestition unmittelbar
senkte, statt eines Steuervorteils. Alle Bundeskonditionen im Ratgeber
{a('/foerderung-fuer-pv-speicher/', 'Förderung für PV-Speicher in Österreich')}.</p>
"""),
        ("Doppelt profitieren: Rechenbeispiel Land plus Bund", "kombination", f"""
<p>Der attraktivste Aspekt der Kärntner Reform 2026 war die volle Kombinierbarkeit mit dem Bund. Die frühere
Anrechnung der Bundesförderung auf die Landesförderung entfällt. Für eine 10-kWp-Anlage mit 10-kWh-Speicher
(Richtpreis 15.000 bis 22.000 Euro vor Förderung) ergab sich im Call 2026 folgende Rechnung; die Bundesposten
sind derzeit nicht beantragbar:</p>
{A.table(
    ["Förderposition", "Rechnung", "Betrag 2026"],
    [
        ["EAG-Bund, PV-Anlage, im Call 2026", "10 kWp × 150 €/kWp", "1.500 €"],
        ["EAG-Bund, Speicher, im Call 2026", "10 kWh × 150 €/kWh", "1.500 €"],
        ["Land Kärnten, Pauschale", "PV ab 5 kWp mit Speicher ab 5 kWh", "3.000 €"],
        ["Summe im Call 2026", "ohne Made-in-Europe-Bonus", "6.000 €"],
        ["Aktuell (Bund derzeit nicht beantragbar)", "nur Landespauschale", "3.000 €"],
    ],
    hl_cols=(2,),
)}
<p>Zum Vergleich: Mit den Sätzen 2025 (EAG 160 Euro je kWp, Land 275 Euro je kWh Speicher plus
PV-Landeszuschuss) kamen für dieselbe Anlage rund 8.500 Euro zusammen. Wie sich beide Varianten auf die
Amortisation auswirken, rechnet der Ratgeber
{a('/ab-wann-lohnt-sich-photovoltaik-mit-speicher/', 'Ab wann lohnt sich Photovoltaik mit Speicher?')} vor:
4,6 beziehungsweise 5,6 Jahre bei 2.500 Euro Ersparnis pro Jahr, beides im EBZ-typischen Korridor von 4 bis
6 Jahren.</p>
{A.box("Wer nur einen Speicher nachrüstet, bekommt vom Land 1.000 Euro Pauschale, vom Bund derzeit nichts: Der "
       "EAG-Speicherzuschuss 2026 war an eine neue oder erweiterte PV-Anlage gebunden, für 2027 ist laut BMWET die "
       "Förderung der Nachrüstung geplant (nicht beschlossen). Bei einem 5-kWh-Speicher "
       "ab rund 4.000 Euro deckt die Pauschale dennoch ein Viertel der Kosten. Details: "
       + a('/pv-speicher-nachruesten/', 'PV-Speicher nachrüsten') + ".", label="Nachrüstung:")}
{A.cta("Landesförderung für Ihr Projekt sichern",
       "EBZ Energie stellt den Landesantrag nach Fertigstellung, achtet auf Rechnungsdaten und Fristen und "
       "plant Speicher mit Energiemanagement für die geplante Systemförderung 2027.",
       secondary=("batteriespeicher", "Zum Batteriespeicher"))}
"""),
        ("Voraussetzungen für die Landesförderung 2026", "voraussetzungen", f"""
<ul>
  <li><b>Speicherpflicht:</b> mindestens 5 kWp PV-Leistung und 5 kWh nutzbare Speicherkapazität. Reine
  PV-Anlagen ohne Speicher fördert das Land 2026 nicht.</li>
  <li><b>Förderwerber:</b> Privatpersonen; für Betriebe gibt es die eigene Schiene mit bis zu 200 Euro je kWp.</li>
  <li><b>Rechnungsdatum:</b> Module, Wechselrichter und Speicher müssen nach dem 1. Jänner 2026 in Rechnung
  gestellt und per Überweisung bezahlt sein.</li>
  <li><b>Antrag nach Fertigstellung:</b> Der Landesantrag wird digital über das Portal des Landes Kärnten
  gestellt, im 2. Call zwischen 12. Oktober und 31. Dezember 2026 (1. Call: 15. April bis 30. Juni), mit
  Rechnungen, Zahlungsnachweisen, Datenblättern und Zählpunkt.</li>
  <li><b>Fachgerechte Errichtung:</b> Installation durch einen befugten Fachbetrieb nach den geltenden Normen.</li>
</ul>
<p>Im Förderjahr 2025 galt die umgekehrte Reihenfolge: Der Landesantrag musste vor Projektbeginn eingereicht
sein, eine rückwirkende Förderung war ausgeschlossen. Wer 2026 nach altem Muster vorgeht, riskiert nichts.
Im Call 2026 verlor die Bundesförderung, wer den EAG-Antrag erst nach der Inbetriebnahme stellte.</p>
{A.box_dark("Der häufigste Fehler 2026",
    "Für das Land gilt: erst fertigstellen, dann einreichen. Im EAG-Call 2026 war es umgekehrt, dort entfiel der "
    "Bundeszuschuss, wenn die Anlage vor dem Ticket in Betrieb ging; für die geplante Systemförderung 2027 soll "
    "der Antrag laut BMWET nach der Installation kommen. EBZ Energie legt die Reihenfolge in der Projektplanung fest.")}
"""),
        ("Ablauf: von der Beratung bis zur Auszahlung", "ablauf", f"""
{A.steps([
    ("Erstberatung und Auslegung",
     "Analyse von Standort, Dach und Verbrauch; Auslegung von PV-Anlage und Speicher nach Lastprofil und "
     "Förderkriterien (ab 5 kWp, ab 5 kWh)."),
    ("Angebot mit Fördercheck",
     "Detailliertes Angebot, das die technischen Voraussetzungen des Landes erfüllt und Speicher mit "
     "Energiemanagement vorsieht, inklusive Projektbericht mit 3D-Belegplan und Statikreport."),
    ("Bundesförderung prüfen",
     "Im Call 2026 wurde hier am ersten Tag des EAG-Calls das Ticket gezogen; der letzte Call endete am "
     "22. Oktober 2026. Derzeit ist kein Bundesantrag möglich, für die geplante Systemförderung 2027 soll laut "
     "BMWET nach der Installation beantragt werden. Zählpunktnummer vorab beim Netzbetreiber besorgen."),
    ("Installation und Inbetriebnahme",
     "Montage durch zertifizierte Fachkräfte, Anmeldung beim Netzbetreiber. Rechnungen nach dem 1. Jänner "
     "2026 datiert und per Überweisung bezahlt."),
    ("Landesantrag nach Fertigstellung",
     "Im 2. Call zwischen 12. Oktober (ab 9 Uhr) und 31. Dezember 2026 den Antrag online über die Förderplattform "
     "des Landes Kärnten stellen, mit allen Nachweisen (1. Call: 15. April bis 30. Juni 2026)."),
    ("Endabrechnung und Auszahlung",
     "Prüfung durch das Land und Auszahlung der Pauschale; im Call 2026 kam die Endabrechnung beim Bund dazu."),
])}
"""),
        ("Strategie: warum sich in Kärnten die größere Anlage lohnt", "strategie", f"""
<p>Die Landespauschale, im Call 2026 kombiniert mit dem Bundeszuschuss, verkürzt die Amortisation erheblich
und macht Kärnten im Vergleich zu anderen Regionen besonders attraktiv. Das spricht dafür, von Anfang an
zukunftssicher zu dimensionieren: Wer ein E-Auto oder eine Wärmepumpe plant, legt Anlage und Speicher gleich
größer aus, statt später nachzurüsten; eine Bundesförderung für die Nachrüstung ist laut BMWET erst ab 2027
geplant und nicht beschlossen. Ein passend dimensionierter Speicher hebt
den Eigenverbrauch auf bis zu 80 Prozent, siehe {a('batteriespeicher', 'Batteriespeicher')}.</p>
<p>Ist ein Fördertopf für das laufende Jahr ausgeschöpft, ist die Wahrscheinlichkeit hoch, dass neue Mittel
folgen; das Land hat 2026 rund 40 Millionen Euro bereitgestellt. Wer die Unterlagen vorbereitet hat, ist beim
nächsten Call sofort startklar. Ergänzend zum Land gibt es 2026 die
{a('/ems-foerderung/', 'Energiemanagement-Förderung des Klimafonds')} mit bis zu 600 Euro für die
intelligente Steuerung von Speicher, Wärmepumpe und Wallbox.</p>
"""),
        ("Fazit: Kärnten bleibt erste Wahl für PV mit Speicher", "fazit", f"""
<p>Ob 275 Euro je kWh wie 2025 oder 3.000 Euro Pauschale wie 2026: Kärnten fördert den Speicher konsequent und
ließ im Call 2026 die Kombination mit dem Bund zu. Für 10 kWp mit 10 kWh waren im Call 2026 6.000 Euro
Förderung erreichbar, mit Made-in-Europe-Komponenten mehr. Seit dem Ende des letzten Calls am 22. Oktober 2026
bleiben aktuell 3.000 Euro vom Land. Wer jetzt plant, baut mit Speicher und Energiemanagement und wahrt die
Chance auf die Systemförderung 2027 (laut BMWET geplant, nicht beschlossen). Der Erfolg hängt an der
Reihenfolge und an vollständigen Unterlagen. Beides übernimmt EBZ Energie aus Villach für Sie.</p>
{A.cta("Förderung in Kärnten sichern",
       "Kostenlose Erstberatung, förderfähige Planung und komplette Antragsabwicklung beim Land Kärnten.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("pv_villach", "Photovoltaik in Villach"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner in Kärnten: EBZ Energie aus Villach",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie plant und installiert Photovoltaik mit Speicher in ganz Kärnten und der Steiermark, "
                 "mit zertifizierten Fachkräften und über 300 dokumentierten "
                 "Projekten. Wir kennen die Kärntner Landesrichtlinie und den Stand der Bundesförderung im Detail "
                 "und koordinieren die Anträge in der richtigen Reihenfolge."),
        "grid": [
            ("Landesantrag und Ausblick", "Landesantrag nach Fertigstellung, Planung mit Blick auf die Systemförderung 2027."),
            ("Förderfähige Auslegung", "Ab 5 kWp und 5 kWh, Rechnungsdaten und Zahlungsnachweise im Blick."),
            ("Regional vor Ort", "Villach, Klagenfurt, Wolfsberg, Spittal und ganz Kärnten."),
            ("Garantien", "Bis zu 30 Jahre Leistungsgarantie, mindestens 10 Jahre Produktgarantie."),
        ],
    },

    "faq": [
        ("Wie hoch ist die Förderung für PV-Speicher in Kärnten 2026?",
         "Das Land zahlt 3.000 Euro Pauschale für neue private PV-Anlagen ab 5 kWp mit Speicher ab 5 kWh nutzbarer "
         "Kapazität und 1.000 Euro für die Speicher-Nachrüstung an Bestandsanlagen. Der Bund förderte im Call 2026 "
         "zusätzlich mit 150 Euro je kWp und 150 Euro je kWh (für 10 kWp mit 10 kWh in Summe 6.000 Euro); der "
         "letzte Call endete am 22. Oktober 2026, derzeit ist der Bund nicht beantragbar."),
        ("Was galt im Förderjahr 2025?",
         "2025 zahlte das Land 275 Euro je Kilowattstunde Speicherkapazität für Speicher bis 10 kWh, eine der "
         "höchsten Speicherförderungen Österreichs. Die Kombination mit dem EAG-Bund war für gewerbliche und "
         "kommunale Anlagen vorgesehen, der Antrag musste vor Projektbeginn gestellt werden."),
        ("Kann ich Landes- und Bundesförderung kombinieren?",
         "Im Call 2026 ja, ohne Anrechnung: EAG-Antrag vor Inbetriebnahme bei der EAG-Abwicklungsstelle und "
         "Landesantrag nach Fertigstellung über das Portal des Landes Kärnten. Der letzte EAG-Call endete am "
         "22. Oktober 2026, derzeit ist nur der Landesantrag möglich (2. Call bis 31. Dezember 2026)."),
        ("Kann ich die Förderung für eine bereits gekaufte Anlage beantragen?",
         "Für den Bund derzeit nein: Im Call 2026 musste der EAG-Antrag vor der Inbetriebnahme gestellt sein, "
         "und der letzte Call endete am 22. Oktober 2026. Das Land Kärnten verlangt 2026 den Antrag nach Fertigstellung, aber nur für Anlagen mit "
         "Rechnungsdatum nach dem 1. Jänner 2026 und innerhalb des Landes-Calls."),
        ("Wird die Speicher-Nachrüstung in Kärnten gefördert?",
         "Ja, mit 1.000 Euro Pauschale für Speicher ab 5 kWh an einer bestehenden PV-Anlage. Der Bund förderte die "
         "reine Nachrüstung 2026 nicht; laut BMWET soll sie ab 2027 in der Systemförderung förderbar werden "
         "(geplant, nicht beschlossen)."),
        ("Wie funktionierte der EAG-Investitionszuschuss 2026?",
         "Er wurde in Fördercalls der EAG-Abwicklungsstelle beantragt, 2026 ab 23. April, 16. Juni und 8. Oktober; "
         "der letzte Call lief bis 22. Oktober 2026. Gefördert wurden die PV-Anlage je kWp (150 Euro bis 10 kWp) und "
         "der Speicher je kWh (150 Euro, max. 50 kWh). Ab 2027 ist laut BMWET ein Antrag nach Installation geplant, "
         "nicht beschlossen."),
        ("Was passiert, wenn der Fördertopf leer ist?",
         "Beim Bund gibt es nach dem 22. Oktober 2026 keinen weiteren Call im alten System; Projekte mit "
         "intelligentem Speicher ab 1. November 2026 sollen 2027 in der geplanten Systemförderung beantragbar sein. "
         "Beim Land läuft der 2. Call bis 31. Dezember 2026 mit rund 10 Millionen Euro. Wer vorbereitet ist, reicht "
         "früh ein."),
        ("Warum lohnt sich professionelle Hilfe beim Antrag?",
         "Weil zwei Stellen mit gegensätzlicher Reihenfolge, eigene Fristen und formale Anforderungen "
         "koordiniert werden müssen. Ein Fehler beim Rechnungsdatum oder ein verspäteter Antrag kostet "
         "schnell tausende Euro. EBZ Energie übernimmt die Anträge und die Endabrechnung."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team hat über 300 PV-Projekte in sechs "
                    "Bundesländern umgesetzt, den Schwerpunkt bilden Kärnten und die Steiermark. Die Inhalte werden "
                    "anhand der Landesrichtlinie Kärnten und der Richtlinien der EAG-Abwicklungsstelle aktualisiert. "
                    "Keine Rechts- oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("Förderportal des Landes Kärnten", "https://www.ktn.gv.at/"),
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("EAG-Abwicklungsstelle (OeMAG)", "https://www.eag-abwicklungsstelle.at/"),
    ],
    "related": [
        ("/photovoltaik-foerderung-kaernten/", "Photovoltaik-Förderung Kärnten 2026"),
        ("/foerderung-fuer-pv-speicher/", "Förderung für PV-Speicher in Österreich"),
        ("/pv-speicher-nachruesten/", "PV-Speicher nachrüsten"),
        ("pv_villach", "Photovoltaik Villach: Ihr lokaler Partner"),
    ],
    "cta": {
        "h3": "Kärntner Förderung sichern",
        "text": "Wir stellen den Landesantrag bis 31. Dezember 2026 und planen mit Speicher für die Systemförderung 2027.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "PV mit Speicher in Kärnten: jetzt planen",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
