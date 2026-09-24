"""Ratgeber: Förderung für PV-Speicher in Österreich (EAG-Bund plus Länder, Ablauf, Kombinierbarkeit).

Migriert von ebz-photovoltaik.at/foerderung-fuer-pv-speicher/ (Quelle Stand Juli 2025, Förderjahr 2025).
Die Konditionen 2026 (EAG-Novelle 2026, Landesprogramme) wurden aus den belegten Schwesterartikeln
ergänzt und als eigener Stand gekennzeichnet.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "foerderung-fuer-pv-speicher",
    "path": "/foerderung-fuer-pv-speicher/",
    "title": "Förderung für PV-Speicher: 150 €/kWh plus Land | EBZ",
    "description": ("Förderung für PV-Speicher in Österreich: EAG-Bund 150 € je kWh (nur mit neuer PV-Anlage), "
                    "Länder 100 bis 150 € je kWh oder 3.000 € Pauschale in Kärnten. Ablauf."),
    "eyebrow": "Förderung · Speicher",
    "crumb_label": "Förderung für PV-Speicher",
    "h1": "Förderung für PV-Speicher in Österreich: 150 Euro je kWh vom Bund plus Landeszuschuss",
    "lead": ("Bund und Länder fördern Stromspeicher mit mehreren tausend Euro, aber nach unterschiedlichen "
             "Regeln. Dieser Ratgeber zeigt, was der EAG-Investitionszuschuss zahlt, welche Bundesländer "
             "zusätzlich fördern, was kombinierbar ist und in welcher Reihenfolge Sie vorgehen müssen."),
    "chips": [
        "EAG-Bund: <b>150 €/kWh</b>, max. 50 kWh",
        "Nur mit <b>neuer oder erweiterter</b> PV-Anlage",
        "Kärnten: <b>3.000 €</b> Pauschale (2026)",
        "Antrag <b>vor Inbetriebnahme</b>",
    ],
    "date_published": "2025-07-05",
    "date_modified": "2026-09-24",
    "hero_img": "foerderung",
    "hero_alt": "Förderantrag für Photovoltaik und Stromspeicher wird am Schreibtisch vorbereitet",

    "tldr": [
        "Der EAG-Investitionszuschuss des Bundes fördert Stromspeicher mit 150 Euro je kWh, gedeckelt mit "
        "30 Prozent der Investitionskosten und maximal 50 kWh. Bedingung: Der Speicher wird gemeinsam mit einer "
        "neuen oder erweiterten PV-Anlage errichtet und hat mindestens 0,5 kWh je kWp.",
        "Der Antrag läuft über die EAG-Abwicklungsstelle (OeMAG) in zeitlich begrenzten Fördercalls und muss "
        "zwingend vor der Inbetriebnahme gestellt werden. 2026: 23. April bis 11. Mai, 16. bis 30. Juni, ab "
        "8. Oktober.",
        "Made-in-Europe-Bonus: 10 Prozent Zuschlag je Komponente (Module, Wechselrichter, Speicher) von der White "
        "List der Abwicklungsstelle, eingeführt mit dem zweiten Call im Juni 2025.",
        "Länder 2026: Kärnten 3.000 Euro Pauschale für PV mit Speicher und 1.000 Euro für die Nachrüstung, "
        "Oberösterreich 150 Euro je kWh Nachrüstung (bis 2.250 Euro), Burgenland und Tirol 100 Euro je kWh. "
        "Salzburg und Wien haben ihre privaten Programme mit Ende 2025 eingestellt.",
        "Kombination ist Ländersache: Kärnten und Tirol ja, Oberösterreich beim Speicher nein, Burgenland nur wenn "
        "der EAG nicht möglich ist, Wien schließt sie aus.",
    ],
    "kpis": [
        ("150 €/kWh", "EAG-Bundeszuschuss für Speicher, max. 50 kWh"),
        ("0,5 kWh je kWp", "Mindestgröße des Speichers für den EAG-Zuschuss"),
        ("3.000 €", "Landespauschale Kärnten 2026 für PV mit Speicher"),
        ("3 Calls", "EAG-Fördercalls pro Jahr, Antrag vor Inbetriebnahme"),
    ],

    "sections": [
        ("Die Bundesförderung: der EAG-Investitionszuschuss für Speicher", "eag-bund", f"""
<p>Das Herzstück der staatlichen Speicherförderung ist der Investitionszuschuss aus dem
Erneuerbaren-Ausbau-Gesetz (EAG). Die Abwicklung übernimmt die EAG-Abwicklungsstelle (OeMAG) in sogenannten
Fördercalls, also festgelegten Zeitfenstern mit eigenem Budget je Anlagenkategorie (A bis D). Der Vorteil für
Antragsteller ist die Planbarkeit: Die Termine sind vorab bekannt.</p>
<p>Für den Speicher gewährt der Bund 150 Euro je Kilowattstunde Nettospeicherkapazität, zusätzlich zum
Zuschuss für die PV-Module je kWp. Die Deckelung liegt bei 30 Prozent der gesamten Investitionskosten,
gefördert werden maximal 50 kWh. Drei Bedingungen entscheiden über die Förderfähigkeit:</p>
<ul>
  <li><b>Antrag vor Inbetriebnahme:</b> Ein bereits laufendes System kann nicht nachträglich gefördert werden.</li>
  <li><b>Kopplung an die PV-Anlage:</b> Der Speicher wird nur gemeinsam mit einer neuen oder erweiterten
  PV-Anlage gefördert. Die reine Nachrüstung an einer Bestandsanlage ist auf Bundesebene nicht förderfähig.</li>
  <li><b>Mindestgröße:</b> Die Nennkapazität muss mindestens 0,5 kWh je kWp der PV-Anlage betragen.</li>
</ul>
{A.table(
    ["Kategorie", "Anlagengröße", "Fördersatz PV 2026", "Speicher"],
    [
        ["A", "bis 10 kWp", "150 €/kWp", "150 €/kWh, max. 50 kWh"],
        ["B", "über 10 bis 20 kWp", "140 €/kWp", "150 €/kWh, max. 50 kWh"],
        ["C", "über 20 bis 100 kWp", "max. 130 €/kWp", "150 €/kWh, max. 50 kWh"],
        ["D", "über 100 bis 1.000 kWp", "max. 120 €/kWp", "150 €/kWh, max. 50 kWh"],
    ],
    hl_cols=(3,),
)}
<p>Der <b>Made-in-Europe-Bonus</b> wurde mit dem zweiten Fördercall im Juni 2025 eingeführt: Für PV-Module,
Wechselrichter und Speicher von Herstellern auf der White List der Abwicklungsstelle gibt es jeweils 10 Prozent
Zuschlag, also bis zu 20 Prozent für die PV-Anlage und weitere 10 Prozent für den Speicher.</p>
<p><small>Stand: Juni 2026 (EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026, kundgemacht am 16. Jänner
2026). Im Förderjahr 2025 betrug der Satz in Kategorie A 160 Euro je kWp.</small></p>
"""),
        ("Rechenbeispiel: 10 kWp mit 10 kWh Speicher", "rechenbeispiel", f"""
<p>Der Speicher verdoppelt die Bundesförderung annähernd. Bei einer 10-kWp-Anlage in Kategorie A erhalten Sie
1.500 Euro für die Module (10 kWp mal 150 Euro) und zusätzlich 1.500 Euro für einen 10-kWh-Speicher (10 kWh
mal 150 Euro), zusammen 3.000 Euro vom Bund. Mit Made-in-Europe-Komponenten steigt der Betrag um bis zu
20 Prozent für die PV-Anlage und 10 Prozent für den Speicher.</p>
{A.table(
    ["Position", "Bund (EAG 2026)", "plus Land Kärnten 2026", "Summe"],
    [
        ["PV-Anlage 10 kWp", "1.500 €", "3.000 € Pauschale (PV mit Speicher)", "4.500 €"],
        ["Speicher 10 kWh", "1.500 €", "in der Pauschale enthalten", "1.500 €"],
        ["Gesamt", "3.000 €", "3.000 €", "6.000 €"],
    ],
    hl_cols=(3,),
)}
<p>Bei einem Richtpreis von 15.000 bis 22.000 Euro für 10 kWp mit Speicher vor Förderung reduziert die
Kombination aus Bund und Land die Investition damit um rund ein Drittel bis ein Viertel. Wie sich das auf
die Amortisation auswirkt, rechnet der Ratgeber
{a('/ab-wann-lohnt-sich-photovoltaik-mit-speicher/', 'Ab wann lohnt sich Photovoltaik mit Speicher?')} vor.</p>
"""),
        ("Die Bundesländer: wer 2026 zusätzlich fördert", "laender", f"""
<p>Während der EAG-Zuschuss in ganz Österreich gleich ist, unterscheiden sich die Länder erheblich. Einige
legen eigene Speicherprogramme auf, andere verlassen sich auf den Bund oder koppeln die Förderung an die
Wohnbau- oder Sanierungsförderung. Entscheidend ist neben der Höhe die Frage, ob Land und Bund kombiniert
werden dürfen.</p>
{A.table(
    ["Bundesland", "Speicherförderung des Landes 2026", "Kombination mit EAG"],
    [
        ["Kärnten", "3.000 € Pauschale für neue PV ab 5 kWp mit Speicher ab 5 kWh; 1.000 € für die Speicher-Nachrüstung; Landes-Call 15. April bis 30. Juni 2026", "ja, ohne Anrechnung"],
        ["Oberösterreich", "Speicher-Nachrüstung: 150 €/kWh, max. 15 kWh, bis 2.250 €, nur für PV in Betrieb vor 1. Jänner 2026", "nein beim Speicher"],
        ["Burgenland", "100 €/kWh nutzbar, max. 20 kWh, max. 30 % der Kosten, bis 2.000 €", "nur, wenn der EAG-Zuschuss nicht möglich ist"],
        ["Tirol", "100 €/kWh, max. 10 kWh, bis 1.000 € (netzdienliche Speicher); PV über Wohnhaussanierung", "ja"],
        ["Vorarlberg", "VKW-Speicherbonus 50 €/kWh, max. 500 €; Land nur PV-Überdachungen ab 20 kWp", "ja"],
        ["Steiermark", "keine eigene Speicherprämie; Sanierungsbonus max. 15 % (1. April bis 15. Mai 2026), Ökofonds ab 20 kWp", "ja"],
        ["Niederösterreich", "keine Direktförderung; PV und Speicher bringen Punkte in der Wohnbauförderung", "ja"],
        ["Salzburg", "Landesförderung für Private mit 31. Dezember 2025 ausgelaufen", "entfällt, nur EAG"],
        ["Wien", "Speicherförderung (max. 2.000 €) mit 31. Dezember 2025 ausgelaufen; neues Paket ab Mai 2026 nur für Fassaden- und Verschattungs-PV", "nein"],
    ],
    hl_cols=(1,),
)}
<p><small>Stand: Juni 2026. Maßgeblich sind die jeweils gültigen Richtlinien der Länder. Im Förderjahr 2025 galten
teils andere Konditionen: Kärnten zahlte 275 Euro je kWh Speicher (bis 10 kWh), Salzburg pauschal 1.000 Euro
für PV ab 5 kWp plus 1.000 Euro für Speicher ab 5 kWh, beides mit dem Bund kombinierbar.</small></p>
<p>Alle neun Länder mit Details vergleicht der Ratgeber
{a('/photovoltaik-landesfoerderungen/', 'PV-Landesförderungen aller Bundesländer')}. Für das Montagegebiet von
EBZ Energie: {a('/foerderung-pv-speicher-kaernten/', 'Förderung für PV-Speicher in Kärnten')} und
{a('foerderung_steiermark', 'Photovoltaik-Förderung Steiermark')}.</p>
{A.cta("Förderung für Ihren Speicher sichern",
       "Wir prüfen, welche Bundes- und Landesförderung für Ihren Standort kombinierbar ist, und übernehmen "
       "Ticketziehung, Antrag und Endabrechnung.",
       secondary=("batteriespeicher", "Zum Batteriespeicher"))}
"""),
        ("Der Antrag Schritt für Schritt", "ablauf", f"""
<p>Der Weg zum EAG-Zuschuss ist klar strukturiert. Fristen, technische Vorgaben und Formulare sind die
Stolpersteine; mit der richtigen Reihenfolge ist der Prozess beherrschbar.</p>
{A.steps([
    ("Beratung und Planung",
     "Analyse von Dach, Stromverbrauch und Zielen. Daraus ergibt sich die Größe von PV-Anlage und Speicher "
     "(mindestens 0,5 kWh je kWp) und ein Angebot als Grundlage für den Antrag."),
    ("Vorbereitung auf den Fördercall",
     "Zählpunktnummer beim Netzbetreiber beantragen, Datenblätter und Angebot bereitlegen. Ohne Zählpunkt "
     "kein Antrag."),
    ("Ticketziehung und Antragstellung",
     "Am ersten Tag des Calls im Portal der EAG-Abwicklungsstelle Ticket ziehen; in den Kategorien A und B "
     "zählt die Reihenfolge des Eingangs. Danach den vollständigen Antrag bis Call-Ende einreichen."),
    ("Fördervertrag und Umsetzung",
     "Nach der Zusage Installation und Inbetriebnahme durch zertifizierte Fachkräfte. Parallel den "
     "Landesantrag stellen, wo eine Landesförderung besteht."),
    ("Endabrechnung und Auszahlung",
     "Rechnungen und Nachweise einreichen; der Zuschuss wird nach Prüfung ausbezahlt."),
])}
{A.box_dark("Der häufigste Fehler",
    "Die Anlage wird in Betrieb genommen, bevor der EAG-Antrag gestellt ist. Dann entfällt die "
    "Bundesförderung vollständig. Umgekehrt verlangt Kärnten den Landesantrag erst nach Fertigstellung. Wer "
    "beide Schienen nutzt, muss die Reihenfolge exakt einhalten.")}
"""),
        ("Speicher nachrüsten: was 2026 gefördert wird", "nachruestung", f"""
<p>Für Herbst 2025 war eine EAG-Novelle angekündigt, die erstmals die alleinige Nachrüstung eines Speichers an
einer bestehenden PV-Anlage fördern sollte. Nach der EAG-Novelle 2026 gilt weiterhin: Der Bundeszuschuss für
Speicher ist an eine Neuerrichtung oder Erweiterung der PV-Anlage gebunden. Die Nachrüstung fördern
stattdessen einzelne Länder: Kärnten mit 1.000 Euro Pauschale ab 5 kWh, Oberösterreich seit 1. März 2026 mit
150 Euro je kWh bis 2.250 Euro, Tirol mit 100 Euro je kWh bis 1.000 Euro und das Burgenland mit 100 Euro je
kWh bis 2.000 Euro. Technik, Kosten und Ablauf der Nachrüstung erklärt der Ratgeber
{a('/pv-speicher-nachruesten/', 'PV-Speicher nachrüsten')}.</p>
<p>Ein Nebeneffekt der Förderlogik: Weil der Bund nur beim Gesamtpaket zahlt und die Speicherförderung je kWh
gerechnet wird, ist es oft sinnvoll, den Speicher bei der Neuanlage gleich etwas größer auszulegen, wenn ein
E-Auto oder eine Wärmepumpe absehbar ist. Zur Steuerung von Speicher, Wärmepumpe und Wallbox gibt es 2026
zusätzlich die {a('/ems-foerderung/', 'Energiemanagement-Förderung des Klimafonds')} mit bis zu 600 Euro
für Haushalte.</p>
"""),
        ("Fazit: Förderung sichern, bevor die Anlage läuft", "fazit", f"""
<p>Bund und Länder machen den Speicher zur wirtschaftlich sinnvollsten Ergänzung jeder neuen PV-Anlage: 150 Euro
je kWh vom Bund, dazu je nach Bundesland bis zu 3.000 Euro Pauschale oder 100 bis 150 Euro je kWh vom Land.
Der Schlüssel liegt in der Reihenfolge: EAG-Antrag vor Inbetriebnahme, Landesantrag nach den jeweiligen
Regeln, Rechnungen sauber getrennt. Wer das einhält, senkt die Investition um mehrere tausend Euro und
verkürzt die Amortisation auf den EBZ-typischen Korridor von 4 bis 6 Jahren.</p>
{A.cta("Förderung und Technik aus einer Hand",
       "Kostenlose Erstberatung, Angebot nach den Förderrichtlinien und komplette Antragsabwicklung bei Bund "
       "und Land in Kärnten und der Steiermark.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("photovoltaik", "Zur Photovoltaik"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für die Förderabwicklung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik mit Speicher in Kärnten und der "
                 "Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften und über 300 "
                 "dokumentierten Projekten. Wir planen jede Anlage nach den technischen Förderrichtlinien, ziehen "
                 "das EAG-Ticket am ersten Call-Tag und stellen den Landesantrag in der richtigen Reihenfolge."),
        "grid": [
            ("Förderfähige Planung", "Speicher ab 0,5 kWh je kWp, Made-in-Europe-Komponenten wo sinnvoll."),
            ("Beide Schienen", "EAG-Bund und Landesförderung Kärnten oder Steiermark, sauber getrennt."),
            ("Fristen im Blick", "Call-Termine, Rechnungsdaten und Endabrechnung übernehmen wir."),
            ("Auch Nachrüstung", "Speicher für Bestandsanlagen inklusive Landesförderung, wo es sie gibt."),
        ],
    },

    "faq": [
        ("Wie hoch ist die Förderung für einen PV-Speicher vom Bund?",
         "Der EAG-Investitionszuschuss beträgt 150 Euro je Kilowattstunde Nettospeicherkapazität, maximal 50 kWh "
         "und maximal 30 Prozent der Investitionskosten. Für einen 10-kWh-Speicher sind das 1.500 Euro, mit "
         "Made-in-Europe-Bonus bis zu 1.650 Euro."),
        ("Kann ich die Förderung für eine bereits installierte Anlage beantragen?",
         "Nein. Der EAG-Antrag muss vor der ersten Inbetriebnahme bei der EAG-Abwicklungsstelle gestellt werden, "
         "eine nachträgliche Förderung ist ausgeschlossen. Auch die meisten Landesprogramme verlangen den Antrag "
         "vor Baubeginn; Kärnten bildet mit dem Antrag nach Fertigstellung eine Ausnahme, verlangt aber "
         "Rechnungsdaten nach dem 1. Jänner 2026."),
        ("Wird die alleinige Nachrüstung eines Speichers gefördert?",
         "Vom Bund nicht: Der EAG-Zuschuss gilt nur für Speicher, die mit einer neuen oder erweiterten PV-Anlage "
         "errichtet werden. Länderprogramme für die Nachrüstung gibt es 2026 in Kärnten (1.000 Euro Pauschale), "
         "Oberösterreich (150 Euro je kWh, bis 2.250 Euro), Tirol (100 Euro je kWh, bis 1.000 Euro) und im "
         "Burgenland (100 Euro je kWh, bis 2.000 Euro)."),
        ("Kann ich Bundes- und Landesförderung kombinieren?",
         "Das hängt vom Bundesland ab. Kärnten erlaubt die Kombination 2026 ohne Anrechnung, Tirol und "
         "Vorarlberg ebenfalls. Oberösterreich schließt EAG-Speicherzuschuss und Landes-Speicherförderung "
         "gegenseitig aus, das Burgenland zahlt nur, wenn der EAG nicht möglich ist, Wien schließt die "
         "Kombination aus."),
        ("Wann kann ich den EAG-Investitionszuschuss beantragen?",
         "Nur in den Fördercalls der EAG-Abwicklungsstelle. 2026 laufen sie vom 23. April bis 11. Mai, vom 16. "
         "bis 30. Juni und ab 8. Oktober. In den Kategorien A und B gilt First-Come-First-Served mit "
         "Ticketziehung, die Budgets je Call sind begrenzt."),
        ("Was ist der Made-in-Europe-Bonus?",
         "Ein Zuschlag von 10 Prozent je Komponente für PV-Module, Wechselrichter und Speicher von Herstellern auf "
         "der White List der EAG-Abwicklungsstelle, eingeführt mit dem zweiten Fördercall im Juni 2025. Für die "
         "PV-Anlage sind damit bis zu 20 Prozent, für den Speicher 10 Prozent mehr Förderung möglich."),
        ("Wie groß muss der Speicher für die Förderung mindestens sein?",
         "Die Nennkapazität muss mindestens 0,5 kWh je kWp der PV-Anlage betragen, bei 10 kWp also mindestens "
         "5 kWh. Kärnten verlangt für die Landespauschale zusätzlich mindestens 5 kWh nutzbare Kapazität und "
         "mindestens 5 kWp PV-Leistung."),
        ("Was passiert, wenn das Budget eines Fördercalls erschöpft ist?",
         "Dann können Sie den Antrag im nächsten Call erneut stellen. Abgelehnte Anträge von Privatpersonen kann "
         "die Abwicklungsstelle mit Zustimmung an den Klima- und Energiefonds weiterleiten. Wichtig: Die Anlage "
         "darf bis dahin nicht in Betrieb gehen."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team hat über 300 PV-Projekte in sechs "
                    "Bundesländern umgesetzt und wickelt EAG- und Landesförderungen für seine Kunden ab. Die Inhalte "
                    "werden anhand der Richtlinien der EAG-Abwicklungsstelle und der Länder aktualisiert. Keine "
                    "Rechts- oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("EAG-Abwicklungsstelle (OeMAG)", "https://www.eag-abwicklungsstelle.at/"),
        ("Förderportal des Landes Kärnten", "https://www.ktn.gv.at/"),
        ("Land Oberösterreich: Nachrüstung von systemdienlichen Solarstromspeichern",
         "https://www.land-oberoesterreich.gv.at/554598.htm"),
        ("Land Tirol: Förderung von netzdienlichen Stromspeichersystemen",
         "https://www.tirol.gv.at/buergerservice/e-government/formulare/ansuchen-zur-foerderung-von-netzdienlichen-stromspeichersystemen/"),
        ("Land Burgenland", "https://www.burgenland.at/"),
        ("Klima- und Energiefonds", "https://www.klimafonds.gv.at/"),
    ],
    "related": [
        ("/foerderung-pv-speicher-kaernten/", "Förderung für PV-Speicher in Kärnten"),
        ("/photovoltaik-landesfoerderungen/", "PV-Landesförderungen: alle 9 Bundesländer"),
        ("/pv-speicher-nachruesten/", "PV-Speicher nachrüsten"),
        ("batteriespeicher", "Batteriespeicher: Technik und Auslegung"),
    ],
    "cta": {
        "h3": "Förderung nicht verschenken",
        "text": "Wir stellen EAG- und Landesantrag in der richtigen Reihenfolge und planen die Technik förderfähig.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Speicher planen, Förderung sichern",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
