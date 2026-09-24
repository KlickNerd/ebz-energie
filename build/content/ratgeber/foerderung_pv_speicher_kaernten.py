"""Ratgeber: Förderung für PV-Speicher in Kärnten (Landesförderung 2025 und 2026, EAG-Bund, Kombination, Ablauf).

Migriert von ebz-photovoltaik.at/foerderung-pv-speicher-kaernten/ (Quelle Stand November 2025, Förderjahr
2025 mit 275 Euro je kWh). Die Kärntner Reform 2026 (3.000 Euro Pauschale, 1.000 Euro Nachrüstung) wurde
aus dem belegten Schwesterartikel photovoltaik_foerderung_kaernten.py ergänzt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "foerderung-pv-speicher-kaernten",
    "path": "/foerderung-pv-speicher-kaernten/",
    "title": "Förderung PV-Speicher Kärnten: 3.000 € plus Bund | EBZ",
    "description": ("Förderung für PV-Speicher in Kärnten: 2026 zahlt das Land 3.000 € Pauschale für PV mit Speicher, "
                    "1.000 € für die Nachrüstung, der Bund 150 € je kWh. Ablauf."),
    "eyebrow": "Förderung · Kärnten",
    "crumb_label": "PV-Speicher-Förderung Kärnten",
    "h1": "Förderung für PV-Speicher in Kärnten: 3.000 Euro Landespauschale plus 150 Euro je kWh vom Bund",
    "lead": ("Kärnten fördert Stromspeicher so stark wie kaum ein anderes Bundesland: bis 2025 mit 275 Euro je "
             "Kilowattstunde, seit 2026 mit einer Pauschale von 3.000 Euro für neue PV-Anlagen mit Speicher, "
             "voll kombinierbar mit dem EAG-Zuschuss des Bundes. Dieser Ratgeber zeigt beide Stände, die "
             "Voraussetzungen und den Ablauf."),
    "chips": [
        "2026: <b>3.000 €</b> Pauschale (PV + Speicher)",
        "Nachrüstung: <b>1.000 €</b> ab 5 kWh",
        "Bund: <b>150 €/kWh</b>, voll kombinierbar",
        "Landes-Call: <b>15. April bis 30. Juni 2026</b>",
    ],
    "date_published": "2025-07-25",
    "date_modified": "2026-09-24",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus in Kärnten mit Photovoltaikanlage und Batteriespeicher",

    "tldr": [
        "Kärnten 2026: 3.000 Euro Pauschale für neue private PV-Anlagen ab 5 kWp mit Speicher ab 5 kWh nutzbarer "
        "Kapazität, 1.000 Euro für die Speicher-Nachrüstung an Bestandsanlagen. Reine PV-Anlagen ohne Speicher "
        "fördert das Land nicht mehr.",
        "Die Landesförderung ist 2026 voll mit dem EAG-Bundeszuschuss kombinierbar (150 Euro je kWp bis 10 kWp, "
        "150 Euro je kWh Speicher), ohne Anrechnung. Für 10 kWp mit 10 kWh ergibt das 6.000 Euro.",
        "Bis 2025 zahlte das Land 275 Euro je kWh Speicherkapazität (bis 10 kWh), eine der höchsten "
        "Speicherförderungen Österreichs; die Kombination mit dem Bund war für gewerbliche und kommunale Anlagen "
        "vorgesehen.",
        "Reihenfolge beachten: EAG-Antrag vor Inbetriebnahme im Fördercall (2026: ab 23. April, 16. Juni, "
        "8. Oktober), Landesantrag erst nach Fertigstellung zwischen 15. April und 30. Juni 2026, Rechnungen "
        "datiert nach dem 1. Jänner 2026.",
        "Der Andrang ist groß, Budgets sind begrenzt. Vollständige Unterlagen (Angebot, Datenblätter, "
        "Zählpunkt, Nachweise) und eine frühzeitige Einreichung entscheiden.",
    ],
    "kpis": [
        ("3.000 €", "Landespauschale 2026 für PV ab 5 kWp mit Speicher ab 5 kWh"),
        ("1.000 €", "Landespauschale 2026 für die Speicher-Nachrüstung"),
        ("275 €/kWh", "Speicherförderung des Landes im Förderjahr 2025"),
        ("6.000 €", "Bund plus Land 2026 für 10 kWp mit 10 kWh"),
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
        ["Reine PV-Anlage ohne Speicher", "PV-Zuschuss des Landes", "keine Landesförderung, nur EAG-Bund"],
        ["Kombination mit EAG-Bund", "für gewerbliche und kommunale Anlagen vorgesehen", "ja, ohne Anrechnung"],
        ["Antragszeitpunkt", "vor Projektbeginn, digital", "nach Fertigstellung, Landes-Call 15. April bis 30. Juni 2026"],
    ],
    hl_cols=(2,),
)}
<p>Für einen typischen 10-kWh-Speicher bedeutete der Satz 2025 einen Zuschuss von 2.750 Euro. Die Pauschale
2026 von 3.000 Euro gilt unabhängig von der Anlagengröße: Eine 12-kWp-Anlage bekommt denselben Betrag wie eine
5-kWp-Anlage. Für betriebliche Eigenverbrauchsanlagen gibt es eine eigene Schiene mit bis zu 200 Euro je kWp.
Insgesamt stellt das Land 2026 rund 40 Millionen Euro für die Energieförderung bereit.</p>
<p><small>Stand: Förderjahr 2025 laut Quelle vom November 2025, Förderjahr 2026 laut Landesrichtlinie Kärnten
2026 (Stand Juni 2026). Maßgeblich sind die jeweils gültigen Richtlinien des Landes Kärnten.</small></p>
"""),
        ("Der EAG-Bundeszuschuss als zweite Säule", "eag-bund", f"""
<p>Neben dem Landesprogramm gibt es den EAG-Investitionszuschuss des Bundes, abgewickelt über die
EAG-Abwicklungsstelle (OeMAG) in Fördercalls mit festem Budget. Er fördert die PV-Anlage je kWp und den
Speicher mit 150 Euro je kWh (maximal 50 kWh, nur gemeinsam mit einer neuen oder erweiterten PV-Anlage). Der
Zuschuss ist ein direkter, nicht rückzahlbarer Betrag, der nach Inbetriebnahme und Endabrechnung ausbezahlt
wird. Der Antrag muss vor der Inbetriebnahme gestellt werden.</p>
{A.table(
    ["EAG-Kategorie", "Anlagengröße", "Fördersatz PV 2026", "Speicher"],
    [
        ["A", "bis 10 kWp", "150 €/kWp", "150 €/kWh"],
        ["B", "über 10 bis 20 kWp", "140 €/kWp", "150 €/kWh"],
        ["C", "über 20 bis 100 kWp", "max. 130 €/kWp", "150 €/kWh"],
    ],
    hl_cols=(2, 3),
)}
<p>Die EAG-Calls 2026 laufen vom 23. April bis 11. Mai, vom 16. bis 30. Juni und ab 8. Oktober. In den
Kategorien A und B gilt First-Come-First-Served mit Ticketziehung. Der Made-in-Europe-Bonus bringt 10 Prozent
Zuschlag je Komponente von der White List der Abwicklungsstelle.</p>
<p>Zur Einordnung: Bis 31. März 2025 galt für kleine PV-Anlagen der Nullsteuersatz bei der Umsatzsteuer. Er
wurde durch den Investitionszuschuss abgelöst. Für Sie als Endkunde ist das transparenter: ein fester Betrag,
der die Anfangsinvestition unmittelbar senkt, statt eines Steuervorteils. Alle Bundeskonditionen im Ratgeber
{a('/foerderung-fuer-pv-speicher/', 'Förderung für PV-Speicher in Österreich')}.</p>
"""),
        ("Doppelt profitieren: Rechenbeispiel Land plus Bund", "kombination", f"""
<p>Der attraktivste Aspekt der Kärntner Reform 2026 ist die volle Kombinierbarkeit mit dem Bund. Die frühere
Anrechnung der Bundesförderung auf die Landesförderung entfällt. Für eine 10-kWp-Anlage mit 10-kWh-Speicher
(Richtpreis 15.000 bis 22.000 Euro vor Förderung) ergibt sich:</p>
{A.table(
    ["Förderposition", "Rechnung", "Betrag 2026"],
    [
        ["EAG-Bund, PV-Anlage", "10 kWp × 150 €/kWp", "1.500 €"],
        ["EAG-Bund, Speicher", "10 kWh × 150 €/kWh", "1.500 €"],
        ["Land Kärnten, Pauschale", "PV ab 5 kWp mit Speicher ab 5 kWh", "3.000 €"],
        ["Summe", "ohne Made-in-Europe-Bonus", "6.000 €"],
    ],
    hl_cols=(2,),
)}
<p>Zum Vergleich: Mit den Sätzen 2025 (EAG 160 Euro je kWp, Land 275 Euro je kWh Speicher plus
PV-Landeszuschuss) kamen für dieselbe Anlage rund 8.500 Euro zusammen. Wie sich beide Varianten auf die
Amortisation auswirken, rechnet der Ratgeber
{a('/ab-wann-lohnt-sich-photovoltaik-mit-speicher/', 'Ab wann lohnt sich Photovoltaik mit Speicher?')} vor:
4,6 beziehungsweise 5,6 Jahre bei 2.500 Euro Ersparnis pro Jahr, beides im EBZ-typischen Korridor von 4 bis
6 Jahren.</p>
{A.box("Wer nur einen Speicher nachrüstet, bekommt vom Land 1.000 Euro Pauschale, vom Bund aber nichts, weil "
       "der EAG-Speicherzuschuss an eine neue oder erweiterte PV-Anlage gebunden ist. Bei einem 5-kWh-Speicher "
       "ab rund 4.000 Euro deckt die Pauschale dennoch ein Viertel der Kosten. Details: "
       + a('/pv-speicher-nachruesten/', 'PV-Speicher nachrüsten') + ".", label="Nachrüstung:")}
{A.cta("Beide Förderungen für Ihr Projekt sichern",
       "EBZ Energie zieht das EAG-Ticket, stellt den Landesantrag nach Fertigstellung und achtet auf "
       "Rechnungsdaten und Fristen.",
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
  gestellt, zwischen 15. April und 30. Juni 2026, mit Rechnungen, Zahlungsnachweisen, Datenblättern und
  Zählpunkt.</li>
  <li><b>Fachgerechte Errichtung:</b> Installation durch einen befugten Fachbetrieb nach den geltenden Normen.</li>
</ul>
<p>Im Förderjahr 2025 galt die umgekehrte Reihenfolge: Der Landesantrag musste vor Projektbeginn eingereicht
sein, eine rückwirkende Förderung war ausgeschlossen. Wer 2026 nach altem Muster vorgeht, riskiert nichts,
wer aber den EAG-Antrag nach der Inbetriebnahme stellt, verliert die Bundesförderung.</p>
{A.box_dark("Der häufigste Fehler 2026",
    "Die Anlage geht in Betrieb, bevor das EAG-Ticket gezogen ist. Dann entfällt der Bundeszuschuss. Umgekehrt "
    "gilt für das Land: erst fertigstellen, dann einreichen. Beide Schienen brauchen eine abgestimmte "
    "Reihenfolge, die EBZ Energie in der Projektplanung festlegt.")}
"""),
        ("Ablauf: von der Beratung bis zur Auszahlung", "ablauf", f"""
{A.steps([
    ("Erstberatung und Auslegung",
     "Analyse von Standort, Dach und Verbrauch; Auslegung von PV-Anlage und Speicher nach Lastprofil und "
     "Förderkriterien (ab 5 kWp, ab 5 kWh)."),
    ("Angebot mit Fördercheck",
     "Detailliertes Angebot, das die technischen Voraussetzungen von Land und Bund erfüllt, inklusive "
     "Projektbericht mit 3D-Belegplan und Statikreport."),
    ("EAG-Antrag vor der Errichtung",
     "Am ersten Tag des EAG-Calls Ticket ziehen und den Antrag bei der EAG-Abwicklungsstelle einreichen. "
     "Zählpunktnummer vorab beim Netzbetreiber besorgen."),
    ("Installation und Inbetriebnahme",
     "Montage durch zertifizierte Fachkräfte, Anmeldung beim Netzbetreiber. Rechnungen nach dem 1. Jänner "
     "2026 datiert und per Überweisung bezahlt."),
    ("Landesantrag nach Fertigstellung",
     "Zwischen 15. April und 30. Juni 2026 den Antrag online über das Portal des Landes Kärnten stellen, mit "
     "allen Nachweisen."),
    ("Endabrechnung und Auszahlung",
     "Endabrechnung beim Bund, Prüfung durch das Land, Auszahlung beider Zuschüsse."),
])}
"""),
        ("Strategie: warum sich in Kärnten die größere Anlage lohnt", "strategie", f"""
<p>Die Kombination aus Landespauschale und Bundeszuschuss verkürzt die Amortisation erheblich und macht
Kärnten im Vergleich zu anderen Regionen besonders attraktiv. Das spricht dafür, von Anfang an zukunftssicher
zu dimensionieren: Wer ein E-Auto oder eine Wärmepumpe plant, legt Anlage und Speicher gleich größer aus,
statt später nachzurüsten, was auf Bundesebene nicht gefördert wird. Ein passend dimensionierter Speicher hebt
den Eigenverbrauch auf bis zu 80 Prozent, siehe {a('batteriespeicher', 'Batteriespeicher')}.</p>
<p>Ist ein Fördertopf für das laufende Jahr ausgeschöpft, ist die Wahrscheinlichkeit hoch, dass neue Mittel
folgen; das Land hat 2026 rund 40 Millionen Euro bereitgestellt. Wer die Unterlagen vorbereitet hat, ist beim
nächsten Call sofort startklar. Ergänzend zu Land und Bund gibt es 2026 die
{a('/ems-foerderung/', 'Energiemanagement-Förderung des Klimafonds')} mit bis zu 600 Euro für die
intelligente Steuerung von Speicher, Wärmepumpe und Wallbox.</p>
"""),
        ("Fazit: Kärnten bleibt erste Wahl für PV mit Speicher", "fazit", f"""
<p>Ob 275 Euro je kWh wie 2025 oder 3.000 Euro Pauschale wie 2026: Kärnten fördert den Speicher konsequent und
lässt die Kombination mit dem Bund zu. Für 10 kWp mit 10 kWh sind 2026 6.000 Euro Förderung erreichbar, mit
Made-in-Europe-Komponenten mehr. Der Erfolg hängt an der Reihenfolge und an vollständigen Unterlagen. Beides
übernimmt EBZ Energie aus Villach für Sie.</p>
{A.cta("Förderung in Kärnten sichern",
       "Kostenlose Erstberatung, förderfähige Planung und komplette Antragsabwicklung bei Land Kärnten und "
       "EAG-Abwicklungsstelle.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("pv_villach", "Photovoltaik in Villach"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner in Kärnten: EBZ Energie aus Villach",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie plant und installiert Photovoltaik mit Speicher in ganz Kärnten und der Steiermark, "
                 "mit einem festangestellten Team aus zertifizierten Fachkräften und über 300 dokumentierten "
                 "Projekten. Wir kennen die Kärntner Landesrichtlinie und die EAG-Calls im Detail und koordinieren "
                 "beide Anträge in der richtigen Reihenfolge."),
        "grid": [
            ("Landes- und Bundesantrag", "EAG-Ticket vor Inbetriebnahme, Landesantrag nach Fertigstellung."),
            ("Förderfähige Auslegung", "Ab 5 kWp und 5 kWh, Rechnungsdaten und Zahlungsnachweise im Blick."),
            ("Regional vor Ort", "Villach, Klagenfurt, Wolfsberg, Spittal und ganz Kärnten."),
            ("Garantien", "Bis zu 30 Jahre Leistungsgarantie, mindestens 10 Jahre Produktgarantie."),
        ],
    },

    "faq": [
        ("Wie hoch ist die Förderung für PV-Speicher in Kärnten 2026?",
         "Das Land zahlt 3.000 Euro Pauschale für neue private PV-Anlagen ab 5 kWp mit Speicher ab 5 kWh nutzbarer "
         "Kapazität und 1.000 Euro für die Speicher-Nachrüstung an Bestandsanlagen. Der Bund fördert zusätzlich mit "
         "150 Euro je kWp und 150 Euro je kWh, für 10 kWp mit 10 kWh sind das in Summe 6.000 Euro."),
        ("Was galt im Förderjahr 2025?",
         "2025 zahlte das Land 275 Euro je Kilowattstunde Speicherkapazität für Speicher bis 10 kWh, eine der "
         "höchsten Speicherförderungen Österreichs. Die Kombination mit dem EAG-Bund war für gewerbliche und "
         "kommunale Anlagen vorgesehen, der Antrag musste vor Projektbeginn gestellt werden."),
        ("Kann ich Landes- und Bundesförderung kombinieren?",
         "Ja, 2026 ohne Anrechnung. Sie stellen zwei Anträge bei zwei Stellen: den EAG-Antrag vor Inbetriebnahme "
         "bei der EAG-Abwicklungsstelle und den Landesantrag nach Fertigstellung über das Portal des Landes "
         "Kärnten, zwischen 15. April und 30. Juni 2026."),
        ("Kann ich die Förderung für eine bereits gekaufte Anlage beantragen?",
         "Für den Bund nein: Der EAG-Antrag muss vor der Inbetriebnahme gestellt sein, sonst entfällt der "
         "Zuschuss. Das Land Kärnten verlangt 2026 den Antrag nach Fertigstellung, aber nur für Anlagen mit "
         "Rechnungsdatum nach dem 1. Jänner 2026 und innerhalb des Landes-Calls."),
        ("Wird die Speicher-Nachrüstung in Kärnten gefördert?",
         "Ja, mit 1.000 Euro Pauschale für Speicher ab 5 kWh an einer bestehenden PV-Anlage. Der Bund fördert die "
         "reine Nachrüstung nicht, weil der EAG-Speicherzuschuss an eine neue oder erweiterte PV-Anlage gebunden ist."),
        ("Wie funktioniert der EAG-Investitionszuschuss?",
         "Er wird in Fördercalls der EAG-Abwicklungsstelle beantragt, 2026 ab 23. April, 16. Juni und "
         "8. Oktober. Gefördert werden die PV-Anlage je kWp (150 Euro bis 10 kWp) und der Speicher je kWh "
         "(150 Euro, max. 50 kWh). Der Zuschuss wird nach Fertigstellung und Endabrechnung ausbezahlt."),
        ("Was passiert, wenn der Fördertopf leer ist?",
         "Beim Bund können Sie im nächsten Call erneut einreichen; die Anlage darf bis dahin nicht in Betrieb "
         "gehen. Beim Land ist mit neuen Budgets im Folgejahr zu rechnen; 2026 stehen rund 40 Millionen Euro "
         "bereit. Wer vorbereitet ist, reicht am ersten Tag ein."),
        ("Warum lohnt sich professionelle Hilfe beim Antrag?",
         "Weil zwei Stellen mit gegensätzlicher Reihenfolge, eigene Fristen und formale Anforderungen "
         "koordiniert werden müssen. Ein Fehler beim Rechnungsdatum oder ein verspätetes EAG-Ticket kostet "
         "mehrere tausend Euro. EBZ Energie übernimmt beide Anträge und die Endabrechnung."),
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
        "text": "Wir koordinieren EAG- und Landesantrag in der richtigen Reihenfolge und planen förderfähig.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "PV mit Speicher in Kärnten: jetzt planen",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
