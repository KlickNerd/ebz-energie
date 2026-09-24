"""Ratgeber: Photovoltaik-Förderung Wien 2026.

Migriert vom Live-Artikel ebz-photovoltaik.at/photovoltaik-foerderung-wien/
(Stand der Quelle: Mai 2026), nach README optimiert. Zahlen stammen aus der
Quelle (EAG-Investitionszuschüsseverordnung-Novelle 2026, Wiener PV-Förderpaket).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

EAG_TABLE = A.table(
    ["Kategorie", "Anlagengröße", "Fördersatz PV", "Speicher"],
    [
        ["A", "bis 10 kWp", "150 €/kWp", "150 €/kWh (max. 50 kWh)"],
        ["B", "10 bis 20 kWp", "140 €/kWp", "150 €/kWh (max. 50 kWh)"],
        ["C", "20 bis 100 kWp", "max. 130 €/kWp", "150 €/kWh (max. 50 kWh)"],
        ["D", "100 bis 1.000 kWp", "max. 120 €/kWp", "150 €/kWh (max. 50 kWh)"],
    ],
    hl_cols=(2,),
)

CALLS_TABLE = A.table(
    ["Call", "Zeitraum", "Hinweis"],
    [
        ["Call 1", "23. April bis 11. Mai 2026", "erster Call des Jahres, meist hohe Nachfrage"],
        ["Call 2", "16. bis 30. Juni 2026", "Sommer-Call"],
        ["Call 3", "ab 8. Oktober 2026", "Herbst-Call"],
    ],
    hl_cols=(1,),
)

ARTICLE = {
    "slug": "photovoltaik-foerderung-wien",
    "path": "/photovoltaik-foerderung-wien/",
    "title": "PV-Förderung Wien 2026: EAG oder neues Stadtpaket | EBZ",
    "description": ("PV-Förderung Wien 2026: EAG-Zuschuss 150 €/kWp für Dachanlagen, 7-Mio.-Paket der Stadt "
                    "ab 1. Mai für Fassaden und Gründächer. Nicht kombinierbar."),
    "eyebrow": "Förderung · Wien",
    "crumb_label": "PV-Förderung Wien 2026",
    "h1": "Photovoltaik-Förderung Wien 2026: EAG-Zuschuss bis 150 €/kWp oder das neue 7-Millionen-Paket der Stadt",
    "lead": ("Die Wiener Sonnenstrom-Offensive 2025 mit bis zu 500 €/kWp ist mit 31. Dezember 2025 ausgelaufen. "
             "Seit 1. Mai 2026 fördert die Stadt Wien gezielt Fassaden, Verschattungsanlagen, Mehrgeschosswohnbau, "
             "Flugdächer und Gründächer, Standard-Dachanlagen laufen nur noch über die EAG-Bundesförderung."),
    "chips": [
        "EAG: <b>150 €/kWp</b> bis 10 kWp",
        "Speicher: <b>150 €/kWh</b> über EAG",
        "Stadt Wien: <b>7 Mio. €</b> ab 1. Mai 2026",
        "Wien + EAG: <b>nicht kombinierbar</b>",
    ],
    "date_published": "2026-04-10",
    "date_modified": "2026-09-24",
    "hero_img": "foerderung",
    "hero_alt": "Beratungsgespräch zur Photovoltaik-Förderung mit Unterlagen und Taschenrechner",

    "tldr": [
        "Standard-Dachanlagen auf Wiener Einfamilienhäusern werden 2026 nicht mehr von der Stadt gefördert. "
        "Der Hauptzuschuss ist die EAG-Bundesförderung mit 150 €/kWp (bis 10 kWp) und 150 €/kWh Speicher.",
        "Das neue Wiener PV-Förderpaket startet am 1. Mai 2026 mit 7 Millionen Euro Budget und fördert "
        "PV-Fassaden, PV-Verschattungsanlagen, Mehrgeschosswohnbau, Flugdächer und Gründächer.",
        "Wiener Landesförderung und EAG-Bundesförderung sind nicht kombinierbar. Sie müssen sich vor dem "
        "Antrag für eine Schiene entscheiden.",
        "Rechenbeispiel EAG: 8 kWp mit 8 kWh Speicher bringen 2.400 € Zuschuss plus 360 € Made-in-Europe-Bonus, "
        "in Summe rund 2.760 €*.",
        "Der EAG-Antrag muss vor Inbetriebnahme gestellt werden. Die Calls 2026: 23. April bis 11. Mai, "
        "16. bis 30. Juni und ab 8. Oktober.",
    ],
    "kpis": [
        ("150 €/kWp", "EAG-Zuschuss Kategorie A (bis 10 kWp)"),
        ("7 Mio. €", "Budget des Wiener PV-Förderpakets 2026"),
        ("1. Mai 2026", "Start des neuen Wiener Pakets"),
        ("18.000+", "PV-Anlagen in Wien in Betrieb"),
    ],

    "sections": [
        ("Die Photovoltaik-Förderung Wien 2026 im Überblick", "ueberblick", f"""
<p>Wien hat seine PV-Förderung 2026 neu aufgestellt. Die bisherigen Programme, die „Sonnenstrom-Offensive 2025“
mit bis zu 500 €/kWp und die Wiener Speicherförderung mit maximal 2.000 €, sind mit 31. Dezember 2025
ausgelaufen. Standard-Dachanlagen auf Einfamilienhäusern fördert die Stadt seit 2026 nicht mehr. Dafür startet
am 1. Mai 2026 ein neues Förderpaket mit 7 Millionen Euro Budget, das sich auf urbane, multifunktionale
PV-Lösungen konzentriert: also auf Anlagen, die der Bund nicht oder nur unzureichend fördert.</p>
<p>Der Hintergrund: Die Wiener Sonnenstrom-Offensive hat die installierte PV-Leistung seit 2020 von 50 auf
325 MWp gesteigert und damit das Zwischenziel von 250 MWp für 2025 zehn Monate früher als geplant
übertroffen. Über 18.000 Anlagen liefern in Wien Sonnenstrom, das Ziel für 2030 sind 800 MWp. Die
Förderfälle stiegen von 628 (2023) über 3.520 (2024, Töpfe bereits im Juni ausgeschöpft) auf 4.644 (2025).</p>
<ul>
  <li><b>Standard-Dach-PV (Einfamilienhaus):</b> nur EAG-Bundesförderung, 120 bis 150 €/kWp plus Speicher und Made-in-Europe-Bonus</li>
  <li><b>Wiener PV-Förderpaket ab 1. Mai 2026:</b> 7 Mio. € für Fassaden, Verschattungsanlagen, Mehrgeschosswohnbau, Flugdächer, Gründächer</li>
  <li><b>Kombinierbarkeit:</b> Wiener Förderung und EAG (oder Klima- und Energiefonds) schließen sich aus</li>
</ul>
{A.box("Eine Kombination der Wiener Landesförderung mit der EAG-Bundesförderung oder dem Klima- und "
       "Energiefonds ist nicht möglich. Sie müssen sich vor der Antragstellung für eine Schiene entscheiden. "
       "Diese strikte Trennung unterscheidet Wien von den meisten anderen Bundesländern, siehe "
       + a('/photovoltaik-landesfoerderungen/', 'Vergleich der Landesförderungen') + ".")}
"""),
        ("EAG-Bundesförderung: der Hauptzuschuss für Wiener Dachanlagen", "eag", f"""
<p>Für die meisten privaten Hausbesitzer in Wien ist die EAG-Bundesförderung 2026 der zentrale Hebel. Mit der
EAG-Investitionszuschüsseverordnung-Strom-Novelle 2026, kundgemacht am 16. Jänner 2026, sind die Konditionen
fixiert: Insgesamt stehen 60 Millionen Euro Bundesmittel für PV- und Speicherprojekte bereit. Die Abwicklung
läuft über die EAG-Förderabwicklungsstelle der OeMAG. Die Fördersätze sind nach Anlagengröße in vier
Kategorien gestaffelt, Speicher werden mit 150 €/kWh bis maximal 50 kWh gefördert.</p>
{EAG_TABLE}
<h3>Made-in-Europe-Bonus</h3>
<p>Hinzu kommt der Made-in-Europe-Bonus mit jeweils 10 % pro Komponente (PV-Module, Wechselrichter, Speicher):
also bis zu 20 % Zuschlag auf den PV-Zuschuss und weitere 10 % auf den Speicherzuschuss. Voraussetzung ist,
dass die verbauten Komponenten auf der offiziellen White List der OeMAG stehen.</p>
<h3>Die drei EAG-Fördercalls 2026</h3>
{CALLS_TABLE}
<p>Die Antragstellung erfolgt online, in den Kategorien A und B nach dem First-come-first-served-Prinzip mit
Ticketziehung. Der Antrag muss vor Inbetriebnahme der Anlage gestellt werden. Wer im ersten Call kein Ticket
zieht, fällt in der Reihung deutlich zurück. Alle Details zur Bundesförderung finden Sie im Ratgeber
{a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}.</p>
"""),
        ("Das neue Wiener PV-Förderpaket ab 1. Mai 2026", "wiener-paket", f"""
<p>Das neue Wiener PV-Förderpaket ist das Herzstück der Landesförderung 2026. Mit 7 Millionen Euro setzt die
Stadt Wien Schwerpunkte auf urbane, innovative und multifunktionale PV-Lösungen, die im dicht bebauten
Stadtraum großes Potenzial haben, aber teurer in der Errichtung sind. Da der Bund Standard-Dachanlagen bereits
umfassend fördert, konzentriert sich die Stadt komplementär auf Fassaden, begehbare Dächer und
Mehrgeschosswohnbauten.</p>
{A.table(
    ["Förderschiene", "Was wird gefördert", "Zielgruppe", "Status 2026"],
    [
        ["PV-Fassadenanlagen", "senkrechte PV an Gebäudefassaden", "Bauträger, Eigentümer, ambitionierte Privatprojekte", "neu"],
        ["PV-Verschattungsanlagen", "PV auf begehbaren Dächern (Strom plus Schatten)", "Wohnbauten, Hotels, Bürogebäude mit Dachterrassen", "neu"],
        ["Mehrgeschosswohnbau", "Gemeinschafts-PV-Anlagen", "Bauträger, Hausverwaltungen, Eigentümergemeinschaften", "läuft weiter"],
        ["Flugdächer", "PV auf überstehenden Dachelementen", "Gewerbe, Wohnbau", "läuft weiter"],
        ["Gründächer", "PV-Gründach-Kombinationen", "Wohnbau, Gewerbe", "läuft weiter"],
        ["Einfamilienhaus-Dach", "Standard-Dach-PV", "Privathaushalte", "entfällt"],
    ],
    hl_cols=(3,),
)}
<p>Die genauen Fördersätze und Voraussetzungen kommuniziert die Stadt Wien mit dem Start am 1. Mai 2026 auf der
Website der Wiener Sonnenstrom-Offensive. Grundsätzlich gilt: Die Anlage gehört in eine der geförderten
Kategorien, die Komponenten erfüllen die technischen Mindestanforderungen, und es wurde keine parallele EAG-
oder Klimafonds-Förderung beantragt.</p>
"""),
        ("PV-Fassaden und Verschattungsanlagen: die neuen Schwerpunkte", "fassade", f"""
<h3>PV-Fassadenanlagen</h3>
<p>Fassaden bieten im dicht bebauten Wien ein bislang wenig genutztes Potenzial. Senkrechte PV-Anlagen liefern
vor allem am Vor- und Nachmittag Strom und ergänzen damit Dachanlagen, die um die Mittagszeit am meisten
erzeugen. Das erhöht den unmittelbaren Eigenverbrauch und entlastet das Netz. Weil Fassadenanlagen technisch
anspruchsvoller und in der Regel teurer sind als Dachanlagen, soll die Förderung den Mehraufwand ausgleichen.</p>
<p>Antragsberechtigt sind laut Ankündigung Eigentümer und Bauträger von Mehrfamilienhäusern, Eigentümer von
Bürogebäuden und gewerblich genutzten Liegenschaften sowie ambitionierte Privatprojekte mit besonderer
architektonischer Qualität (je nach Detailausgestaltung der Richtlinie).</p>
<h3>PV-Verschattungsanlagen auf begehbaren Dächern</h3>
<p>Diese Anlagen erfüllen eine doppelte Funktion: Sie erzeugen Sonnenstrom und schaffen schattige
Außenbereiche, die in heißen Wiener Sommern wichtiger werden. Die Schiene richtet sich an Wohnbauten mit
großen Dachterrassen und Gemeinschaftsdächern, an Bürogebäude mit Dachterrassen, Hotels mit Rooftop-Bereichen
und gewerbliche Liegenschaften. Die Stadt sieht darin einen Beitrag gegen Hitzeinseln und für die urbane
Energiewende.</p>
{A.cta("Fassade, Dachterrasse oder Gemeinschaftsdach: Wir prüfen, welche Schiene mehr bringt",
       "EBZ Energie plant Ihr Projekt mit Projektbericht, 3D-Belegplan und Statikreport und rechnet EAG "
       "gegen das Wiener Paket. So entscheiden Sie mit Zahlen, nicht mit Bauchgefühl.",
       secondary=("photovoltaik", "Zur Photovoltaik-Leistungsseite"))}
"""),
        ("Mehrgeschosswohnbau, Flugdächer, Gründächer und der Sonnengutschein", "mehrgeschoss", f"""
<p>Auch wenn Standard-Dachanlagen auf Einfamilienhäusern 2026 nicht mehr gefördert werden, laufen die
bestehenden Schienen für Mehrgeschosswohnbauten, Flugdächer (überstehende Dachelemente) und Gründächer weiter.
Sie waren bereits in der bisherigen Sonnenstrom-Offensive verankert.</p>
<h3>„1, 2, 3 Sonnengutschein“: Beratung für Mehrgeschosswohnbau</h3>
<p>Für gemeinschaftliche PV-Anlagen auf Mehrparteienhäusern gibt es das Beratungsprogramm
„1, 2, 3 Sonnengutschein“ mit kostenlosen Leistungen in drei Modulen:</p>
<ul>
  <li><b>Modul 1, Ersteinschätzung:</b> technische und rechtliche Vorprüfung</li>
  <li><b>Modul 2, Entscheidungsbegleitung:</b> gemeinschaftliche Entscheidungsfindung in Hausversammlungen</li>
  <li><b>Modul 3, Umsetzungsberatung:</b> Begleitung der konkreten Umsetzung</li>
</ul>
<p>Das Programm galt für Dächer mit einem Mindestpotenzial von 5 kWp und lief laut Stadt Wien bis
31. März 2026. Ob und in welcher Form es im neuen Paket fortgesetzt wird, ist mit Stand Mai 2026 offen.
Der Fokus auf Mehrgeschosswohnbau ist für Wien naheliegend: Rund 80 Prozent der Wienerinnen und Wiener leben
in Mehrparteienhäusern, dort liegt das größte ungenutzte PV-Potenzial. Wer Strom mit den Nachbarn teilen will,
findet im Ratgeber {a('eg', 'Energiegemeinschaft')} die passende Ergänzung.</p>
"""),
        ("Wien oder EAG: welche Schiene passt zu welchem Projekt?", "entscheidung", f"""
<p>Weil sich beide Schienen ausschließen, ist die Wahl die wichtigste Entscheidung im Förderprozess:</p>
{A.table(
    ["Projekt", "Empfohlene Schiene", "Begründung"],
    [
        ["Standard-Dach-PV auf Einfamilienhaus", "EAG-Bundesförderung", "einzige Option, Wien fördert hier nicht mehr"],
        ["PV-Fassade, Verschattungsanlage", "Wiener Paket (Vergleich lohnt)", "Mehrkosten werden gezielt abgedeckt"],
        ["Mehrgeschosswohnbau, Flugdach, Gründach", "Wahl zwischen Wien und EAG", "je nach Fördersatz der Stadt und Anlagengröße"],
    ],
    hl_cols=(1,),
)}
<h3>Rechenbeispiel EAG: 8 kWp mit 8 kWh Speicher</h3>
{A.table(
    ["Position", "Rechnung", "Betrag"],
    [
        ["EAG-Zuschuss PV", "8 kWp × 150 €/kWp", "1.200 €"],
        ["EAG-Zuschuss Speicher", "8 kWh × 150 €/kWh", "1.200 €"],
        ["Made-in-Europe-Bonus PV", "20 % auf 1.200 €", "240 €"],
        ["Made-in-Europe-Bonus Speicher", "10 % auf 1.200 €", "120 €"],
        ["<b>Gesamtförderung</b>", "", "<b>rund 2.760 €*</b>"],
    ],
    hl_cols=(2,),
)}
<p>Bei größeren Anlagen der Kategorie B (bis 20 kWp, 140 €/kWp) und größerem Speicher sind über die EAG bis
rund 4.500 €* erreichbar. Eine PV-Fassadenanlage gleicher Größe könnte über das Wiener Programm höhere Beträge
erzielen, weil die Mehrkosten der Fassadenintegration berücksichtigt werden. Faustregel aus der Quelle: Bei
innovativen Projekten ist der Wiener Zuschuss in der Regel höher.</p>
<p><small>*Richtwerte auf Basis der EAG-Fördersätze 2026. Die tatsächliche Höhe hängt von Anlagengröße,
Speicherkapazität und den verbauten Komponenten (White List) ab.</small></p>
"""),
        ("Voraussetzungen und Antragsablauf", "ablauf", f"""
<p>Für die EAG-Bundesförderung gelten bundesweit einheitliche Voraussetzungen: netzgekoppelte PV-Anlage,
Antragstellung vor Inbetriebnahme, alle erforderlichen Genehmigungen oder Anzeigen liegen in erster Instanz
vor, Eigentum an der Liegenschaft oder schriftliche Einwilligung des Eigentümers, Anlage nach Stand der Technik
und Sicherheitsanforderungen.</p>
{A.steps([
    ("Schiene festlegen",
     "Standard-Dach: EAG. Fassade, Verschattung, Mehrgeschosswohnbau, Flugdach, Gründach: Wiener Paket und EAG "
     "gegenrechnen. Eine Kombination ist ausgeschlossen."),
    ("Planung und Komponenten",
     "Angebot mit Anlagengröße, Speicher und Komponenten einholen. Für den Made-in-Europe-Bonus müssen Module, "
     "Wechselrichter und Speicher auf der White List der OeMAG stehen."),
    ("Genehmigungen und Netzzugang",
     "Anzeigen oder Genehmigungen in erster Instanz einholen, Zählpunkt und Netzzugang beim Netzbetreiber klären. "
     "Diese Unterlagen müssen bei Antragstellung vorliegen."),
    ("EAG-Antrag im Fördercall",
     "Online über die EAG-Abwicklungsstelle, in Kategorie A und B mit Ticketziehung. Zwingend vor Inbetriebnahme. "
     "Calls 2026: 23. April bis 11. Mai, 16. bis 30. Juni, ab 8. Oktober."),
    ("Errichtung, Inbetriebnahme, Endabrechnung",
     "Nach Errichtung und Inbetriebnahme werden Rechnungen und Nachweise eingereicht, danach erfolgt die "
     "Auszahlung des Zuschusses."),
])}
{A.box_dark("Der häufigste Fehler in Wien",
    "Wer für eine Fassaden- oder Gründachanlage bereits einen EAG-Antrag gestellt hat, ist für das Wiener "
    "Paket gesperrt, und umgekehrt. Legen Sie die Schiene fest, bevor der erste Antrag rausgeht.")}
"""),
        ("Photovoltaik und Wärmepumpe in Wien", "waermepumpe", f"""
<p>Viele Wiener Haushalte heizen noch mit Gas. Wer die PV-Anlage mit einer {a('waermepumpe', 'Wärmepumpe')}
kombiniert, nutzt den Sonnenstrom direkt für Heizung und Warmwasser und kann die Energiekosten um bis zu
85 % senken. Förderseitig laufen beide Systeme getrennt: Für die PV-Anlage gelten die hier beschriebenen
Schienen, für die Wärmepumpe die Sanierungsoffensive des Bundes oder „Sauber Heizen für Alle“. Ein
{a('batteriespeicher', 'Batteriespeicher')} erhöht den Eigenverbrauch zusätzlich und wird über die EAG mit
150 €/kWh gefördert.</p>
"""),
        ("Fazit: Erst die Schiene wählen, dann den Antrag stellen", "fazit", f"""
<p>Die Photovoltaik-Förderung in Wien 2026 ist anders strukturiert als in den meisten Bundesländern: EAG für
Standard-Dachanlagen, Wiener Paket für Fassaden, Verschattungsanlagen, Mehrgeschosswohnbau, Flugdächer und
Gründächer. Für eine private Dachanlage mit Speicher sind über die EAG rund 2.760 € (8 kWp, 8 kWh) bis
4.500 €* realistisch. Wer ein innovatives urbanes Projekt plant, kann über das Wiener Paket mehr erreichen,
muss sich aber vorab entscheiden, weil beide Schienen nicht kombinierbar sind.</p>
<p><small>Stand: Mai 2026. Förderhöhen, Budgets und Fristen können sich ändern, maßgeblich sind die
Richtlinien der EAG-Abwicklungsstelle (OeMAG) und der Stadt Wien.</small></p>
{A.cta("Förderstrategie für Ihr Wiener Projekt",
       "Wir rechnen EAG und Wiener Paket für Ihr Dach oder Ihre Fassade durch und übernehmen die Antragstellung "
       "in der richtigen Reihenfolge.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("finanzierung", "Finanzierung ab 147 €/Monat"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Planung und Förderabwicklung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant Photovoltaikanlagen, Speicher und Wärmepumpen und hat über 300 Projekte "
                 "in sechs Bundesländern dokumentiert. Für Projekte in Wien übernehmen wir Beratung, Planung mit "
                 "Projektbericht (3D-Belegplan und Statikreport) und die komplette Förderabwicklung aus einer Hand: "
                 "Wir prüfen, ob EAG oder Wiener Paket mehr bringt, und stellen die Anträge fristgerecht."),
        "grid": [
            ("Schienenvergleich mit Zahlen", "EAG gegen Wiener Paket, bevor der erste Antrag rausgeht."),
            ("White-List-Komponenten", "Module, Wechselrichter und Speicher mit Made-in-Europe-Bonus."),
            ("Fristen im Blick", "EAG-Calls, Ticketziehung, Antrag vor Inbetriebnahme."),
            ("Referenzen in 6 Bundesländern", "300+ Projekte, 4,9 Sterne auf Google."),
        ],
    },

    "faq": [
        ("Werden Standard-Dach-PV-Anlagen in Wien 2026 noch gefördert?",
         "Nein. Standard-Dachanlagen auf Einfamilienhäusern fördert die Stadt Wien 2026 nicht mehr, die "
         "Sonnenstrom-Offensive 2025 mit bis zu 500 €/kWp ist mit 31. Dezember 2025 ausgelaufen. Wiener Hausbesitzer "
         "nutzen die EAG-Bundesförderung mit 150 €/kWp bis 10 kWp und 140 €/kWp bis 20 kWp, also 1.500 bis 2.800 € "
         "PV-Zuschuss, plus Speicherförderung und Made-in-Europe-Bonus."),
        ("Wann startet das neue Wiener PV-Förderpaket?",
         "Das neue Wiener PV-Förderpaket startet am 1. Mai 2026 mit 7 Millionen Euro Budget. Gefördert werden "
         "PV-Fassadenanlagen, PV-Verschattungsanlagen auf begehbaren Dächern sowie weiterhin Mehrgeschosswohnbau, "
         "Flugdächer und Gründächer. Die genauen Konditionen veröffentlicht die Stadt mit dem Start."),
        ("Kann ich Wiener Förderung und EAG-Bundesförderung kombinieren?",
         "Nein. Eine Kombination der Wiener Landesförderung mit der EAG-Bundesförderung oder dem Klima- und "
         "Energiefonds ist 2026 ausdrücklich nicht möglich. Sie müssen sich vorab für eine Schiene entscheiden. In den "
         "meisten anderen Bundesländern sind Bund und Land dagegen kombinierbar."),
        ("Wie hoch ist die EAG-Förderung für eine 8-kWp-Anlage mit Speicher in Wien?",
         "8 kWp bringen 1.200 € PV-Zuschuss, ein 8-kWh-Speicher weitere 1.200 €. Mit Made-in-Europe-Bonus "
         "(20 % auf PV, 10 % auf Speicher) kommen 360 € dazu, in Summe rund 2.760 €. Bei größeren Anlagen und "
         "Speichern sind bis rund 4.500 € möglich (Richtwerte)."),
        ("Welche PV-Anlagen fördert Wien 2026 noch?",
         "Wien fördert 2026 PV-Fassadenanlagen, PV-Verschattungsanlagen auf begehbaren Dächern, Anlagen auf "
         "Mehrgeschosswohnbauten, Flugdächern und Gründächern. Für Mehrgeschosswohnbau gab es zusätzlich das "
         "Beratungsprogramm „1, 2, 3 Sonnengutschein“ mit drei kostenlosen Modulen, das laut Stadt bis 31. März 2026 lief."),
        ("Wann sind die EAG-Fördercalls 2026?",
         "Die drei Calls laufen vom 23. April bis 11. Mai, vom 16. bis 30. Juni und ab 8. Oktober 2026. In den "
         "Kategorien A und B (bis 20 kWp) gilt First come, first served mit Ticketziehung. Der Antrag muss vor "
         "Inbetriebnahme der Anlage gestellt werden."),
        ("Gibt es in Wien 2026 eine Speicherförderung?",
         "Die Wiener Speicherförderung mit maximal 2.000 € ist mit 31. Dezember 2025 ausgelaufen. Speicher werden "
         "2026 über die EAG-Bundesförderung mit 150 €/kWh bis maximal 50 kWh gefördert, plus 10 % Made-in-Europe-Bonus "
         "bei gelisteten Speichern."),
        ("Wer hilft bei der Förderabwicklung in Wien?",
         "EBZ Energie aus Villach übernimmt für Wiener Projekte Beratung, Planung und Förderabwicklung aus einer "
         "Hand, von der Wahl der Förderschiene über die Antragstellung im EAG-Call bis zur Endabrechnung. Mit über "
         "300 Projekten in sechs Bundesländern kennen wir die Unterschiede zwischen Bund und Ländern aus der Praxis."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant PV-Anlagen, Speicher und "
                    "Wärmepumpen und übernimmt die Förderabwicklung, Referenzen liegen in sechs Bundesländern vor. "
                    "Die Angaben werden anhand der offiziellen Unterlagen von OeMAG und Stadt Wien geprüft. Keine Rechts- "
                    "oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("EAG-Förderabwicklungsstelle der OeMAG", "https://www.eag-abwicklungsstelle.at/"),
        ("White List der OeMAG (Made-in-Europe-Komponenten)", "https://www.oem-ag.at/"),
        ("Wiener Sonnenstrom-Offensive", "https://sonnenstrom.wien.gv.at/"),
        ("Stadt Wien: Energie und Klima", "https://www.wien.gv.at/"),
        ("Klima- und Energiefonds", "https://www.klimafonds.gv.at/"),
    ],
    "related": [
        ("/photovoltaik-landesfoerderungen/", "Vergleich: PV-Landesförderungen aller 9 Bundesländer"),
        ("/photovoltaik-foerderung-oesterreich-2026/", "Photovoltaik-Förderung Österreich 2026 (EAG)"),
        ("/foerderung-fuer-pv-speicher/", "Förderung für PV-Speicher"),
        ("photovoltaik", "Photovoltaik: Planung und Technik von EBZ"),
    ],
    "cta": {
        "h3": "Wien oder EAG?",
        "text": "Wir rechnen beide Schienen für Ihr Projekt durch und stellen den Antrag rechtzeitig vor Inbetriebnahme.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre PV-Förderung in Wien, richtig gewählt",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung und "
                   "Förderabwicklung aus einer Hand übernimmt."),
}
