"""Ratgeber: PV-Speicher nachrüsten (AC- oder DC-Kopplung, Kriterien, Kosten, Förderung).

Migriert von ebz-photovoltaik.at/pv-speicher-nachruesten/ (Quelle Stand Juli 2025),
inhaltlich gestrafft und um die 2026 belegten Nachrüst-Förderungen der Länder ergänzt
(Zahlen aus den Schwesterartikeln Kärnten, Oberösterreich, Tirol, Quellen unten).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "pv-speicher-nachruesten",
    "path": "/pv-speicher-nachruesten/",
    "title": "PV-Speicher nachrüsten: Kosten, Technik, Förderung | EBZ",
    "description": ("PV-Speicher nachrüsten: AC- oder DC-Kopplung, 1 bis 1,5 kWh je 1.000 kWh Verbrauch, "
                    "800 bis 1.200 €/kWh, Eigenverbrauch bis zu 80 %. Förderung 2026 und Ablauf."),
    "eyebrow": "Speicher · Nachrüstung",
    "crumb_label": "PV-Speicher nachrüsten",
    "h1": "PV-Speicher nachrüsten: Eigenverbrauch von 30 auf bis zu 80 Prozent heben",
    "lead": ("Wer eine bestehende Photovoltaikanlage um einen Batteriespeicher ergänzt, nutzt den Solarstrom "
             "auch abends und nachts, statt ihn für wenige Cent einzuspeisen. Dieser Ratgeber zeigt, welche "
             "Technik zu Ihrer Anlage passt, was die Nachrüstung kostet und welche Förderung es 2026 dafür gibt."),
    "chips": [
        "Eigenverbrauch: <b>30 auf bis zu 80 %</b>",
        "Faustregel: <b>1 bis 1,5 kWh</b> je 1.000 kWh",
        "Richtwert: <b>800 bis 1.200 €</b> je kWh*",
        "Lebensdauer: <b>15 bis 20 Jahre</b>",
    ],
    "date_published": "2025-06-15",
    "date_modified": "2026-09-24",
    "hero_img": "speicher",
    "hero_alt": "Batteriespeicher für die Nachrüstung an einer bestehenden Photovoltaikanlage",

    "tldr": [
        "Ein nachgerüsteter Speicher hebt den Eigenverbrauch einer typischen PV-Anlage von rund 30 Prozent "
        "auf bis zu 80 Prozent. Jede selbst genutzte Kilowattstunde ersetzt teuren Netzbezug inklusive "
        "Netzentgelten und Abgaben.",
        "Zwei Wege: AC-Kopplung (bestehender Wechselrichter bleibt, eigener Batteriewechselrichter kommt dazu) "
        "oder DC-Kopplung mit Hybridwechselrichter (alter Wechselrichter wird ersetzt). Für die reine "
        "Nachrüstung ist AC meist der einfachere, für alte Wechselrichter DC oft der bessere Weg.",
        "Dimensionierung: 1 bis 1,5 kWh Speicherkapazität je 1.000 kWh Jahresstromverbrauch. Ein zu großer "
        "Speicher wird im Winter nie voll, ein zu kleiner ist im Sommer mittags schon geladen.",
        "Kosten: Richtwert 800 bis 1.200 Euro je kWh inklusive Installation und gegebenenfalls "
        "Batteriewechselrichter*. Für 10 kWh also rund 8.000 bis 12.000 Euro vor Förderung.",
        "Förderung 2026: Der EAG-Bundeszuschuss gilt nur für Speicher zusammen mit einer neuen oder erweiterten "
        "PV-Anlage. Die reine Nachrüstung fördern aktuell die Länder, etwa Kärnten mit 1.000 Euro Pauschale, "
        "Oberösterreich mit 150 Euro je kWh und Tirol mit 100 Euro je kWh.",
    ],
    "kpis": [
        ("bis zu 80 %", "Eigenverbrauch mit Speicher (statt rund 30 %)"),
        ("1 bis 1,5 kWh", "Speicherkapazität je 1.000 kWh Jahresverbrauch"),
        ("800 bis 1.200 €", "Richtwert je kWh inkl. Installation*"),
        ("8.000 bis 10.000", "Ladezyklen hochwertiger Lithium-Speicher"),
    ],

    "sections": [
        ("Warum sich die Nachrüstung eines PV-Speichers jetzt lohnt", "warum-jetzt", f"""
<p>Die wirtschaftliche Logik hat sich in den vergangenen Jahren umgekehrt: Die Vergütung für eingespeisten
Solarstrom ist stark gesunken, während der Bezugspreis für Netzstrom inklusive Netzentgelten und Abgaben hoch
geblieben ist. Wer den Mittagsüberschuss für wenige Cent je Kilowattstunde abgibt und abends zum vollen
Tarif zurückkauft, verschenkt einen großen Teil des möglichen Nutzens seiner Anlage. Den aktuellen
{a('marktpreis', 'OeMAG-Marktpreis')} und die Vergütungen der Anbieter vergleichen wir im Ratgeber
{a('/einspeisetarif-fuer-photovoltaik/', 'Einspeisetarif für Photovoltaik')}.</p>
<p>Ein Batteriespeicher löst dieses Zeitproblem. Er nimmt den Überschuss vom Tag auf und gibt ihn abends,
nachts und an trüben Tagen wieder ab. Der Eigenverbrauchsanteil steigt damit von durchschnittlich 30 Prozent
auf bis zu 80 Prozent. Drei weitere Gründe sprechen für die Nachrüstung:</p>
<ul>
  <li><b>Versorgungssicherheit:</b> Ein Speicher mit Notstromfunktion versorgt Kühlschrank, Heizungspumpe
  und Router auch bei Netzausfall. Details im Ratgeber {a('/notstrom/', 'Notstrom mit Photovoltaik')}.</li>
  <li><b>Unabhängigkeit vom Strompreis:</b> Je mehr eigene Kilowattstunden Sie nutzen, desto weniger treffen
  Sie Preiserhöhungen des Versorgers und steigende Netzentgelte.</li>
  <li><b>Wert der Immobilie:</b> Eine PV-Anlage mit Speicher gilt bei Käufern als modern und senkt die
  laufenden Betriebskosten, ein Argument beim Verkauf.</li>
</ul>
"""),
        ("AC- oder DC-Kopplung: welche Technik zu Ihrer Anlage passt", "ac-oder-dc", f"""
<p>Der Wechselrichter wandelt den Gleichstrom (DC) der Module in Wechselstrom (AC) für das Hausnetz um.
Beim Nachrüsten geht es darum, überschüssigen Strom in einer Batterie zu sichern, statt ihn einzuspeisen.
Dafür gibt es zwei etablierte Wege.</p>
<h3>AC-Kopplung: der flexible Weg für Bestandsanlagen</h3>
<p>Ihr bestehender PV-Wechselrichter bleibt unverändert. Der Speicher wird mit einem eigenen
Batteriewechselrichter auf der AC-Seite ins Hausnetz eingebunden. Er wandelt überschüssigen Wechselstrom
zurück in Gleichstrom für die Batterie und bei Bedarf wieder in Wechselstrom für Ihre Verbraucher. Der große
Vorteil: Das funktioniert unabhängig von Hersteller und Alter des vorhandenen Wechselrichters. Der Preis dafür
sind geringe Verluste durch die doppelte Umwandlung, die bei modernen Systemen in der Praxis kaum ins
Gewicht fallen.</p>
<h3>DC-Kopplung: Hybridwechselrichter statt altem Wechselrichter</h3>
<p>Hier ersetzt ein Hybridwechselrichter das bestehende Gerät. Er versorgt das Haus, lädt den Speicher
direkt mit Gleichstrom und speist erst bei vollem Speicher ins Netz ein. Das ist die effizienteste Variante,
weil der Umweg über die AC-Umwandlung entfällt. Für die reine Nachrüstung bedeutet sie aber einen größeren
Eingriff. Sinnvoll ist sie vor allem, wenn der alte Wechselrichter ohnehin am Ende seiner Lebensdauer ist
oder eine Notstromfunktion gewünscht wird.</p>
{A.table(
    ["Kriterium", "AC-gekoppelt", "DC-gekoppelt (Hybridwechselrichter)"],
    [
        ["Ideal für", "Nachrüstung bestehender Anlagen", "Neuanlagen oder Tausch eines alten Wechselrichters"],
        ["Wechselrichter", "bleibt, zusätzlicher Batteriewechselrichter", "wird durch Hybridwechselrichter ersetzt"],
        ["Flexibilität", "sehr hoch, herstellerunabhängig", "geringer, Komponenten müssen zusammenpassen"],
        ["Effizienz", "etwas geringer (doppelte Umwandlung)", "sehr hoch, Strom wird direkt als DC gespeichert"],
        ["Installationsaufwand", "geringer, wenig Eingriff ins Bestandssystem", "höher, zentraler Wechselrichter wird getauscht"],
        ["Kosten", "oft geringere Anfangsinvestition", "langfristig günstiger, wenn der Wechselrichter ohnehin fällig ist"],
    ],
    hl_cols=(1, 2),
)}
{A.box("Ob AC oder DC: Die Entscheidung hängt vom Alter Ihres Wechselrichters, vom gewünschten "
       "Notstromumfang und von der Herstellerkompatibilität ab. EBZ Energie prüft das vor Ort und legt "
       "beide Varianten mit Preis nebeneinander.", label="Praxis:")}
"""),
        ("Den richtigen Speicher wählen: fünf Kriterien", "kriterien", f"""
<p>Nicht der größte oder günstigste Speicher ist der richtige, sondern der, der zu Ihrem Lastprofil und zu
Ihrer Anlage passt. Diese Kennzahlen entscheiden:</p>
<ul>
  <li><b>Speicherkapazität (kWh):</b> Faustregel in Österreich: 1 bis 1,5 kWh je 1.000 kWh
  Jahresstromverbrauch. Bei 5.000 kWh sind das 5 bis 7,5 kWh. Wer eine Wärmepumpe oder ein E-Auto plant,
  legt etwas größer aus.</li>
  <li><b>Systemwirkungsgrad:</b> Moderne Lithium-Ionen-Speicher erreichen über 90 Prozent. Jeder Prozentpunkt
  weniger Verlust ist bares Geld über die Laufzeit.</li>
  <li><b>Zyklenfestigkeit:</b> Hochwertige Speicher sind für 8.000 bis 10.000 Ladezyklen ausgelegt, das
  entspricht 15 bis 20 Jahren Betrieb. Hersteller geben üblicherweise 10 Jahre Garantie mit mindestens
  80 Prozent Restkapazität.</li>
  <li><b>Entladetiefe (DoD):</b> Gibt an, wie viel der Nennkapazität nutzbar ist. Aktuelle Systeme liegen bei
  90 bis 100 Prozent. Vergleichen Sie immer die nutzbare, nicht die Brutto-Kapazität.</li>
  <li><b>Notstrom- oder Ersatzstromfähigkeit:</b> Nicht jeder Speicher kann das. Wer bei Netzausfall versorgt
  sein will, braucht ein passendes Modell, einen notstromfähigen Wechselrichter und eine Umschalteinrichtung.</li>
</ul>
<p>Mehr zur Technik und zu den Kennzahlen auf der Leistungsseite {a('batteriespeicher', 'Batteriespeicher')}.</p>
"""),
        ("Was die Nachrüstung kostet", "kosten", f"""
<p>Der größte Posten ist der Speicher selbst. Als Orientierung gilt in Österreich ein Preis von 800 bis
1.200 Euro je Kilowattstunde Speicherkapazität inklusive Installation und, bei AC-Systemen, inklusive
Batteriewechselrichter*. Die Preise sind in den vergangenen Jahren kontinuierlich gesunken.</p>
{A.table(
    ["Speichergröße", "Richtwert inkl. Installation*", "Passend für Jahresverbrauch"],
    [
        ["5 kWh", "4.000 bis 6.000 €", "3.500 bis 5.000 kWh"],
        ["8 kWh", "6.400 bis 9.600 €", "5.500 bis 8.000 kWh"],
        ["10 kWh", "8.000 bis 12.000 €", "7.000 bis 10.000 kWh"],
    ],
    hl_cols=(1,),
)}
<p>Beim Tausch auf einen Hybridwechselrichter (DC-Kopplung) kommt dessen Preis dazu, dafür entfällt der
Batteriewechselrichter. Zur Einordnung: Eine komplette neue 10-kWp-Anlage mit Speicher liegt bei EBZ Energie
bei rund 15.000 bis 22.000 Euro vor Förderung, siehe {a('/kosten-einer-solaranlage/', 'Kosten einer Solaranlage')}.</p>
<h3>Amortisation: Speicher allein und Gesamtsystem</h3>
<p>Für den nachgerüsteten Speicher allein rechnet man in Österreich mit einer Amortisationszeit von 8 bis
12 Jahren, abhängig von Anschaffungspreis nach Förderung, Strompreisentwicklung und Eigenverbrauchsanteil.
Bei einer Lebensdauer von 15 bis 20 Jahren bleibt damit ein deutlicher Gewinnzeitraum. Anders die Rechnung
für ein komplettes PV-System mit Speicher, das von Anfang an gemeinsam geplant und gefördert wird: Hier liegt
die Amortisation bei EBZ-Projekten typischerweise bei 4 bis 6 Jahren, wie der Ratgeber
{a('/ab-wann-lohnt-sich-photovoltaik-mit-speicher/', 'Ab wann lohnt sich Photovoltaik mit Speicher?')} vorrechnet.</p>
<p><small>*Richtwerte für marktübliche Lithium-Ionen-Systeme, Stand Juli 2025. Der tatsächliche Preis hängt von
Hersteller, Kapazität, Kopplungsart und Aufwand vor Ort ab.</small></p>
{A.cta("Angebot für Ihre Bestandsanlage",
       "Wir prüfen Ihren Wechselrichter, Ihr Lastprofil und die passende Speichergröße und legen AC- und "
       "DC-Variante mit Festpreis nebeneinander.",
       secondary=("batteriespeicher", "Zum Batteriespeicher"))}
"""),
        ("Förderung für die Speicher-Nachrüstung 2026", "foerderung", f"""
<p>Wichtig für die Kalkulation: Der EAG-Investitionszuschuss des Bundes (150 Euro je kWh, maximal 50 kWh)
wird nur gewährt, wenn der Speicher gemeinsam mit einer neuen oder erweiterten PV-Anlage errichtet wird. Die
reine Nachrüstung an einer Bestandsanlage ist auf Bundesebene nicht förderfähig. Dafür haben mehrere
Bundesländer eigene Schienen aufgelegt:</p>
{A.table(
    ["Bundesland", "Förderung für die Speicher-Nachrüstung", "Bedingungen"],
    [
        ["Kärnten", "1.000 € Pauschale", "Speicher ab 5 kWh an bestehender PV-Anlage, Landes-Call 15. April bis 30. Juni 2026, Antrag nach Fertigstellung"],
        ["Oberösterreich", "150 €/kWh, max. 15 kWh, bis 2.250 €", "max. 40 % der Kosten, nur für PV-Anlagen, die vor dem 1. Jänner 2026 in Betrieb gingen; seit 1. März 2026"],
        ["Tirol", "100 €/kWh, max. 10 kWh, bis 1.000 €", "netzdienliches Speichersystem, Ansuchen beim Land"],
        ["Burgenland", "100 €/kWh nutzbar, max. 20 kWh, bis 2.000 €", "max. 30 % der Kosten, Antrag bis 6 Monate nach Rechnung"],
    ],
    hl_cols=(1,),
)}
<p>Für Kärnten und die Steiermark, das Montagegebiet von EBZ Energie, finden Sie alle Details in den Ratgebern
{a('/foerderung-pv-speicher-kaernten/', 'Förderung für PV-Speicher in Kärnten')} und
{a('/photovoltaik-landesfoerderungen/', 'PV-Landesförderungen aller Bundesländer')}. Den Überblick über
Bund und Länder gibt {a('/foerderung-fuer-pv-speicher/', 'Förderung für PV-Speicher in Österreich')}.</p>
<p><small>Stand: Juni 2026. Maßgeblich sind die jeweils gültigen Richtlinien der Länder und der
EAG-Abwicklungsstelle.</small></p>
"""),
        ("So läuft die Nachrüstung ab", "ablauf", f"""
{A.steps([
    ("Bestandsaufnahme",
     "Wir analysieren Ihren Stromverbrauch, Ausrichtung und Leistung der PV-Anlage, Typ und Alter des "
     "Wechselrichters sowie den Platz im Technikraum."),
    ("Konzept und Dimensionierung",
     "Auf dieser Basis wird die Speicherkapazität festgelegt und entschieden, ob AC-Kopplung oder der "
     "Wechsel auf einen Hybridwechselrichter sinnvoller ist. Notstromwunsch wird hier mitgeplant."),
    ("Angebot und Förderung",
     "Sie erhalten ein Angebot mit allen Komponenten und Montage. Wo eine Landesförderung besteht, bereiten "
     "wir die Unterlagen vor und achten auf Fristen und Rechnungsdaten."),
    ("Installation und Inbetriebnahme",
     "Zertifizierte Fachkräfte installieren Speicher, Wechselrichter und Zählerkonfiguration, meist an "
     "einem Tag. Danach wird das System eingestellt und die Anmeldung beim Netzbetreiber erledigt."),
])}
{A.box_dark("Häufiger Fehler bei Bestandsanlagen",
    "Der Speicher wird nach der Nennleistung der Anlage gewählt statt nach dem tatsächlichen Verbrauch am "
    "Abend. Ein 10-kWh-Speicher an einem Haushalt mit 3.500 kWh Jahresverbrauch wird selten voll ausgenutzt. "
    "Entscheidend ist das Lastprofil, nicht die Modulleistung.")}
"""),
        ("Fazit: Nachrüsten lohnt sich mit der richtigen Auslegung", "fazit", f"""
<p>Die Nachrüstung eines PV-Speichers ist die logische Antwort auf niedrige Einspeisevergütungen und hohe
Bezugspreise. Sie hebt den Eigenverbrauch von rund 30 auf bis zu 80 Prozent, bringt auf Wunsch Notstrom und
macht Sie unabhängiger von der Preispolitik des Versorgers. Entscheidend für die Wirtschaftlichkeit sind drei
Dinge: eine Kapazität, die zum Verbrauch passt, die richtige Kopplungsart für Ihren Wechselrichter und die
Nutzung der Landesförderung, wo es sie gibt.</p>
{A.cta("Speicher nachrüsten mit EBZ Energie",
       "Kostenlose Erstberatung, Prüfung Ihrer Bestandsanlage und ein Festpreisangebot für AC- oder "
       "DC-Nachrüstung in Kärnten und der Steiermark.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("referenzen", "Referenzen ansehen"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für die Speicher-Nachrüstung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Batteriespeicher, Wärmepumpen und "
                 "Energiemanagement in Kärnten und der Steiermark, mit einem festangestellten Team aus "
                 "zertifizierten Fachkräften und über 300 dokumentierten Projekten. Bestandsanlagen jeder Marke "
                 "rüsten wir AC-gekoppelt oder mit Hybridwechselrichter nach und übernehmen Anmeldung und "
                 "Förderantrag."),
        "grid": [
            ("Herstellerunabhängig", "AC-Nachrüstung für praktisch jede Bestandsanlage, DC-Tausch wo sinnvoll."),
            ("Auslegung nach Lastprofil", "Speichergröße nach Ihrem Verbrauch, nicht nach Katalog."),
            ("Notstrom mitgedacht", "Auf Wunsch mit Umschalteinrichtung und Ersatzstrom für das ganze Haus."),
            ("Förderung inklusive", "Landesförderung Kärnten und Steiermark: Fristen, Unterlagen, Abrechnung."),
        ],
    },

    "faq": [
        ("Was kostet es, einen PV-Speicher nachzurüsten?",
         "Als Richtwert gelten in Österreich 800 bis 1.200 Euro je Kilowattstunde Speicherkapazität inklusive "
         "Installation und gegebenenfalls Batteriewechselrichter. Ein 10-kWh-Speicher liegt damit bei rund "
         "8.000 bis 12.000 Euro vor Förderung. Landesförderungen wie die 1.000-Euro-Pauschale in Kärnten "
         "senken den Betrag."),
        ("Welche Speichergröße ist für mich richtig?",
         "Faustformel: 1 bis 1,5 kWh Kapazität je 1.000 kWh Jahresstromverbrauch. Bei 4.000 bis 5.000 kWh "
         "sind das 4 bis 7,5 kWh. Wer eine Wärmepumpe oder ein E-Auto plant, dimensioniert etwas größer. "
         "Eine Analyse des Lastprofils zeigt, wie viel Abend- und Nachtverbrauch der Speicher tatsächlich "
         "abdecken kann."),
        ("Kann jede bestehende PV-Anlage mit einem Speicher nachgerüstet werden?",
         "Fast jede. Am flexibelsten ist die AC-Kopplung, bei der der Speicher mit eigenem Batteriewechselrichter "
         "unabhängig vom vorhandenen PV-Wechselrichter arbeitet. Alternativ wird der alte Wechselrichter durch "
         "einen Hybridwechselrichter ersetzt (DC-Kopplung), was bei älteren Anlagen oder Notstromwunsch oft die "
         "bessere Lösung ist."),
        ("Wie lange hält ein nachgerüsteter Batteriespeicher?",
         "Hochwertige Lithium-Ionen-Speicher sind für 8.000 bis 10.000 Ladezyklen ausgelegt, was in der Praxis "
         "15 bis 20 Jahren entspricht. Die Hersteller geben üblicherweise 10 Jahre Garantie und sichern zu, dass "
         "die Kapazität in dieser Zeit nicht unter 80 Prozent fällt."),
        ("Erhöht ein Speicher den Eigenverbrauch wirklich so stark?",
         "Ja. Ohne Speicher nutzt ein typischer Haushalt nur 20 bis 30 Prozent seines Solarstroms selbst, der "
         "Rest geht ins Netz. Mit einem passend dimensionierten Speicher steigt der Anteil auf 60 bis 80 Prozent, "
         "weil der Mittagsüberschuss abends und nachts verbraucht wird."),
        ("Gibt es 2026 eine Förderung für die reine Speicher-Nachrüstung?",
         "Vom Bund nicht: Der EAG-Zuschuss von 150 Euro je kWh gilt nur zusammen mit einer neuen oder "
         "erweiterten PV-Anlage. Landesförderungen gibt es unter anderem in Kärnten (1.000 Euro Pauschale ab "
         "5 kWh), Oberösterreich (150 Euro je kWh, bis 2.250 Euro), Tirol (100 Euro je kWh, bis 1.000 Euro) und "
         "im Burgenland (100 Euro je kWh, bis 2.000 Euro). Stand Juni 2026."),
        ("Wie lange rechnet sich ein nachgerüsteter Speicher?",
         "Für den Speicher allein rechnet man in Österreich mit 8 bis 12 Jahren Amortisation, abhängig von "
         "Preis nach Förderung, Strompreis und Eigenverbrauchsanteil. Bei 15 bis 20 Jahren Lebensdauer bleibt "
         "ein Gewinnzeitraum. Ein komplett neu geplantes PV-System mit Speicher amortisiert sich bei EBZ-Projekten "
         "typischerweise in 4 bis 6 Jahren."),
        ("Bekomme ich mit dem nachgerüsteten Speicher auch Notstrom?",
         "Nur mit den passenden Komponenten: ein notstromfähiger Hybridwechselrichter, ein dafür freigegebener "
         "Speicher und eine Umschalteinrichtung, die das Haus vom Netz trennt. Bei der AC-Nachrüstung übernimmt "
         "der Batteriewechselrichter diese Rolle, wenn er notstromfähig ist. Das wird bei der Planung geklärt."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team hat über 300 PV-Projekte in sechs "
                    "Bundesländern umgesetzt, darunter zahlreiche Speicher-Nachrüstungen an Bestandsanlagen "
                    "unterschiedlicher Hersteller. Preise und Förderdaten in diesem Ratgeber sind Richtwerte, "
                    "maßgeblich sind das individuelle Angebot und die offiziellen Förderbedingungen."),
    "sources": [
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("Förderportal des Landes Kärnten", "https://www.ktn.gv.at/"),
        ("Land Oberösterreich: Nachrüstung von systemdienlichen Solarstromspeichern",
         "https://www.land-oberoesterreich.gv.at/554598.htm"),
        ("Land Tirol: Förderung von netzdienlichen Stromspeichersystemen",
         "https://www.tirol.gv.at/buergerservice/e-government/formulare/ansuchen-zur-foerderung-von-netzdienlichen-stromspeichersystemen/"),
        ("Land Burgenland", "https://www.burgenland.at/"),
    ],
    "related": [
        ("batteriespeicher", "Batteriespeicher: Technik und Auslegung"),
        ("/notstrom/", "Notstrom mit Photovoltaik"),
        ("/foerderung-pv-speicher-kaernten/", "Förderung für PV-Speicher in Kärnten"),
        ("/ab-wann-lohnt-sich-photovoltaik-mit-speicher/", "Ab wann lohnt sich PV mit Speicher?"),
    ],
    "cta": {
        "h3": "Bestandsanlage prüfen lassen",
        "text": "Wir sagen Ihnen ehrlich, welche Speichergröße und Kopplung sich bei Ihrem Verbrauch rechnet.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Mehr aus Ihrer bestehenden PV-Anlage herausholen",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
