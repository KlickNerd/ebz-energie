"""Ratgeber: Photovoltaik-Zaun (Solarzaun) in Österreich.

Neuer Artikel (kein WordPress-Vorgänger), erstellt 2026-11-19.
Ziel-Keywords (Google Ads, Österreich, 19.11.2026): photovoltaik zaun 480 (April 880), solarzaun 720,
pv zaun / photovoltaik zaunanlage / photovoltaik zaunelemente 1.300 (Google fasst sie zusammen),
photovoltaik als zaun 480, solar zaun 140, photovoltaik zaun preis 140, solarzaun kosten 70,
photovoltaik zaun erfahrungen 70, photovoltaik zaun österreich 50, pv zaun kosten 30, pv sichtschutz 40,
photovoltaik zaun genehmigung 20.

Faktenbasis: eigene Berechnung mit PVGIS 5.3 (EU-Kommission, JRC; Standort Villach 46,61 N / 13,85 O,
SARAH3, 14 % Systemverluste, ohne Nahverschattung und Schnee): Süd 35° 1.296 kWh/kWp, senkrecht Ost 617,
West 606, Süd 937, Nord 203; Stundenreihen 2019 bis 2023. Bifazialer Zaun = Vorderseite + Rückseite x
Bifazialität 70 bis 85 % (Spanne laut Next2Sun). Recht: § 7 und § 13 K-BO 1996 und § 21 Stmk. BauG
(JUSLINE, Stand 19.11.2026). Netzanschluss: Handlungsanleitung Klima- und Energiefonds / PV Austria.
Preise: Herstellerangaben Next2Sun (DE) und Sunbooster (Graz, laut VOL.AT März 2026).
Nicht behauptet: österreichischer Komplettpreis je Meter inkl. Fundament und Montage (nicht neutral belegt),
Ballwurf-Festigkeit (keine Norm), eigene PV-Zaun-Referenz von EBZ (gibt es nicht),
Förderfähigkeit eines Zauns in der Kärntner Landesförderung (Richtlinie nennt die Anlagenart nicht).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "photovoltaik-zaun",
    "path": "/photovoltaik-zaun/",
    "cluster": "Photovoltaik",
    "title": "Photovoltaik-Zaun: Ertrag, Kosten, Genehmigung | EBZ",
    "description": ("Photovoltaik-Zaun in Österreich: rund 80 bis 87 % des Dachertrags, die Hälfte davon "
                    "morgens und abends. Kosten, Genehmigung, Statik und Förderung 2026."),
    "eyebrow": "Photovoltaik · Solarzaun",
    "crumb_label": "Photovoltaik-Zaun",
    "h1": "Photovoltaik-Zaun: 80 bis 87 % des Dachertrags, die Hälfte davon morgens und abends",
    "lead": ("Ein Solarzaun aus senkrechten, beidseitig aktiven Glas-Glas-Modulen grenzt das Grundstück ab und "
             "erzeugt Strom, wenn eine Dachanlage wenig liefert: am Morgen und am Abend. Dieser Ratgeber rechnet "
             "für Villach ehrlich vor, was ein PV-Zaun bringt, was er kostet und was Kärnten und die Steiermark "
             "baurechtlich verlangen."),
    "chips": [
        "Ertrag Ost-West: <b>80 bis 87 %</b> eines Süddachs*",
        "Vor 10 und ab 16 Uhr: <b>rund 49 %</b> des Stroms*",
        "Kärnten: Einfriedung bis <b>2 m</b> mitteilungspflichtig",
        "Steiermark: Einfriedung bis <b>1,5 m</b> meldepflichtig",
    ],
    "date_published": "2026-11-19",
    "date_modified": "2026-11-19",
    "hero_img": "gen_detail",
    "hero_alt": "Fachkraft verschraubt ein Photovoltaikmodul mit der Aluminium-Montageschiene der Unterkonstruktion",

    "tldr": [
        "Ein Photovoltaik-Zaun besteht aus senkrecht montierten, meist bifazialen Glas-Glas-Modulen. Beide "
        "Seiten erzeugen Strom, die Rückseite je nach Modul rund 70 bis 85 % der Vorderseite.",
        "Ein unverschatteter Ost-West-Zaun in Villach liefert rechnerisch rund 1.040 bis 1.130 kWh je kWp und "
        "Jahr. Das sind 80 bis 87 % einer Süd-Dachanlage mit 35° Neigung (rund 1.300 kWh je kWp).*",
        "Rund 49 % seines Stroms erzeugt der Ost-West-Zaun vor 10 Uhr und ab 16 Uhr, die Dachanlage nur rund "
        "25 %. Selbst genutzt ist jede Kilowattstunde rund doppelt so viel wert wie eingespeist.*",
        "Baurecht: In Kärnten sind Einfriedungen in Leichtbauweise bis 2 m Höhe mitteilungspflichtig, in der "
        "Steiermark Einfriedungen bis 1,5 m meldepflichtig. Ob der Zaun als Einfriedung oder als PV-Anlage "
        "gilt, klären wir vorab mit der Gemeinde.",
        "Je kWp kostet ein Zaun mehr als eine Dachanlage, weil Pfosten, Fundamente und ein windfestes Gestell "
        "dazukommen. Eine eigene Zaun-Förderung gibt es nicht, Kärnten zahlt 3.000 Euro nur für PV mit Speicher.",
    ],
    "kpis": [
        ("1.040 bis 1.130", "kWh je kWp, Ost-West-Zaun Villach*"),
        ("rund 1.300", "kWh je kWp, Süddach 35° Villach*"),
        ("rund 49 %", "des Zaunstroms vor 10 und ab 16 Uhr*"),
        ("2 m / 1,5 m", "Einfriedung Kärnten / Steiermark ohne Bewilligung"),
    ],

    "sections": [
        ("Was ist ein Photovoltaik-Zaun?", "was-ist", f"""
<p><b>Ein Photovoltaik-Zaun (Solarzaun) ist eine Einfriedung, deren Zaunfelder aus senkrecht montierten
Solarmodulen bestehen.</b> Meist sind das bifaziale Glas-Glas-Module: Die Solarzellen liegen zwischen zwei
Glasscheiben, und auch die Rückseite wandelt Licht in Strom um. Steht der Zaun in Nord-Süd-Richtung, zeigt
eine Modulseite nach Osten und die andere nach Westen. Der Zaun erntet dann die Morgensonne mit der einen und
die Abendsonne mit der anderen Seite.</p>
<p>Wie stark die Rückseite mitarbeitet, beschreibt die <b>Bifazialität</b>. Laut dem Hersteller Next2Sun, der
seit Jahren senkrechte Anlagen baut, erreichen ältere PERC-Module rund 65 %, für senkrechte Anlagen empfiehlt
er n-Typ-Module ab rund 85 %, Heterojunction-Module schaffen noch mehr. Am Markt gibt es drei Bauformen:</p>
{A.table(
    ["Bauform", "Aufbau", "Typisch für"],
    [
        ["Zaunfelder aus Glas-Glas-Modulen", "Module als Füllung zwischen Pfosten, auf Punktfundamenten oder Mauer",
         "Neuer Zaun, Sichtschutz, größere Leistung"],
        ["Module am bestehenden Zaun", "Glas-Glas-Module mit Haltern an einem Doppelstabmattenzaun",
         "Vorhandener stabiler Zaun"],
        ["Solarstreifen", "Schmale Modulstreifen werden in den Zaun eingefädelt",
         "Kleine Anlagen, oft steckerfertig"],
    ],
    hl_cols=(0,),
)}
<p>Kleine steckerfertige Zaunmodule fallen unter die Regeln für {a('balkonkraftwerke', 'Balkonkraftwerke')}.
Dieser Ratgeber behandelt fest angeschlossene Zaunanlagen, die ein Elektrofachbetrieb plant und beim
Netzbetreiber anmeldet. EBZ Energie verbaut auf Dächern ebenfalls bifaziale Glas-Glas-Module, etwa beim
{a('/referenzen/projekt-gewerbe-oberoesterreich/', 'Gewerbebetrieb in Oberösterreich')} mit 40 kWp in
Ost-West-Ausrichtung.</p>
"""),
        ("Ertrag: PV-Zaun im Vergleich zur Dachanlage", "ertrag", f"""
<p><b>Ein unverschatteter Photovoltaik-Zaun in Ost-West-Ausrichtung erreicht in Villach rechnerisch 80 bis
87 % des Jahresertrags einer Süd-Dachanlage.</b> Wir haben das mit PVGIS gerechnet, dem frei zugänglichen
Solarrechner der Europäischen Kommission (Gemeinsame Forschungsstelle JRC). Ein senkrechtes Modul mit Blick
nach Osten liefert dort 617 kWh je kWp und Jahr, nach Westen 606 kWh. Beim bifazialen Zaun kommt die
Rückseite mit 70 bis 85 % dazu.</p>
{A.table(
    ["Anlage in Villach", "Ertrag je kWp und Jahr*", "Anteil am Süddach*", "Dezember*", "Juni*"],
    [
        ["Dachanlage Süd, 35° Neigung", "rund 1.300 kWh", "100 %", "rund 63 kWh", "rund 135 kWh"],
        ["Zaun bifazial, Seiten Ost und West", "rund 1.040 bis 1.130 kWh", "80 bis 87 %", "rund 36 bis 39 kWh",
         "rund 126 bis 137 kWh"],
        ["Zaun bifazial, Seiten Süd und Nord", "rund 1.080 bis 1.110 kWh", "83 bis 86 %", "rund 75 bis 76 kWh",
         "rund 86 bis 91 kWh"],
    ],
    hl_cols=(1,),
)}
<p>Zwei Dinge fallen auf. Ein Zaun in <b>Ost-West-Richtung</b> (Modulseiten nach Süden und Norden) liefert
im Winter sogar mehr als die Dachanlage, weil die tief stehende Sonne fast senkrecht auf die Südseite trifft.
Im Sommer liegt er dafür deutlich darunter. Ein Zaun in <b>Nord-Süd-Richtung</b> (Seiten nach Osten und
Westen) folgt dagegen dem Sommerhalbjahr und kommt im Juni an das Dach heran.</p>
{A.box("Die Rechnung gilt ohne Verschattung. Ein Gartenzaun steht aber nahe am Boden, oft neben Haus, Hecke "
       "oder Nachbargebäude. Jeder Schatten auf einer Modulseite kostet Ertrag, die Rückseite bekommt bei "
       "Bewuchs und dunklem Boden weniger Licht. Realistisch planen wir deshalb mit Abschlägen und rechnen "
       "Ihren Standort einzeln.",
       label="Wichtig:")}
<p>Zum Vergleich mit Studien: Die Hochschule für Technik, Wirtschaft und Kultur Leipzig hat für Deutschland
mit 999 Wh je W für senkrechte bifaziale Ost-West-Anlagen gegenüber 1.020 Wh je W für 20° geneigte
Freiflächenanlagen gerechnet, allerdings mit 8 bis 12 Meter Reihenabstand auf freiem Feld (pv magazine, Juli
2022). Hersteller nennen für ihre Solarzäune bis zu 1.200 kWh je kWp. Für einen typischen Gartenzaun sind das
Bestwerte. Wie viele kWp Sie insgesamt brauchen, zeigt
{a("/bifaziale-module/", "Bifaziale Glas-Glas-Module")}.</p>
"""),
        ("Tageskurve: Solarstrom am Morgen und am Abend", "tageskurve", f"""
<p><b>Ein Ost-West-Zaun erzeugt rund 49 % seines Jahresstroms vor 10 Uhr und ab 16 Uhr, eine Süd-Dachanlage nur
rund 25 %.</b> Zur Mittagszeit (11 bis 15 Uhr) ist es umgekehrt: Dort liefert die Dachanlage 53 % ihres
Stroms, der Zaun 30 %. Das zeigt die stündliche PVGIS-Auswertung für Villach über die Jahre 2019 bis 2023.</p>
{A.table(
    ["Uhrzeit (Juni, Mittel)", "Dachanlage Süd 35°*", "Zaun Ost-West, bifazial*"],
    [
        ["gegen 7 Uhr", "rund 65 Wh je kWp", "rund 330 Wh je kWp"],
        ["gegen 9 Uhr", "rund 340 Wh je kWp", "rund 490 Wh je kWp"],
        ["gegen 13 Uhr", "rund 580 Wh je kWp", "rund 190 Wh je kWp"],
        ["gegen 17 Uhr", "rund 270 Wh je kWp", "rund 360 Wh je kWp"],
        ["gegen 19 Uhr", "rund 45 Wh je kWp", "rund 235 Wh je kWp"],
    ],
    hl_cols=(2,),
)}
<p>Genau zu diesen Randzeiten kochen, duschen und waschen viele Haushalte. Was der Zaun dann direkt im Haus
verbraucht, ersetzt Netzstrom um rund 28 bis 35 Cent je kWh (Haushaltsstrom in Kärnten und der Steiermark
laut E-Control, November 2026). Eingespeist bringt dieselbe Kilowattstunde den OeMAG-Marktpreis, im Oktober
2026 waren das 14,874 Cent ({a('marktpreis', 'aktueller Marktpreis')}). Am meisten bringt ein Zaun als
Ergänzung zu einer Dachanlage: Das Dach deckt den Mittag ab, der Zaun Morgen und Abend, ein
{a('batteriespeicher', 'Batteriespeicher')} die Nacht.</p>
"""),
        ("Was kostet ein Photovoltaik-Zaun?", "kosten", f"""
<p><b>Einen neutralen Preisvergleich für PV-Zäune in Österreich gibt es nicht. Hersteller nennen für das
reine Material Preise ab rund 250 Euro je Meter, Montage und Elektrik kommen dazu.</b> Je kWp ist ein Zaun
teurer als eine Dachanlage, weil Pfosten, Fundamente und ein windfestes Gestell anfallen, die das Dach nicht
braucht.</p>
{A.table(
    ["Preisangabe (Herstellerangaben)", "Was enthalten ist"],
    [
        ["Next2Sun (Deutschland): ab rund 250 € je Meter",
         "Zaunanlage mit PV-Modulen, ohne Montage, Elektromaterial und Arbeitszeit"],
        ["Sunbooster (Graz): rund 515 € je 2-m-Modul",
         "Solarstreifen für bestehende Doppelstabmattenzäune (VOL.AT, März 2026)"],
        ["Dachanlage zum Vergleich: 10 kWp mit Speicher rund 15.000 bis 22.000 €",
         "EBZ-Richtpreis vor Förderung, inklusive Montage"],
    ],
    hl_cols=(0,),
)}
<p>Für den Gesamtpreis eines Zauns zählen außerdem:</p>
<ul>
  <li><b>Fundament und Gestell:</b> Punktfundamente, gerammte Stahlprofile oder Montage auf einer Mauer, je
  nach Boden und Hang.</li>
  <li><b>Leitungsweg:</b> Vom Zaun bis zum Wechselrichter im Haus braucht es meist eine Erdleitung. Je weiter
  der Zaun vom Haus entfernt ist, desto mehr Grabarbeit.</li>
  <li><b>Wechselrichter:</b> Zwei Modulseiten mit unterschiedlicher Tageskurve passen gut zu Wechselrichtern
  mit mehreren Eingängen. Ist schon eine Anlage am Dach, prüfen wir, ob der bestehende Wechselrichter
  reicht.</li>
  <li><b>Was ohnehin anfällt:</b> Brauchen Sie sowieso einen neuen Zaun oder Sichtschutz, rechnen Sie nur den
  Mehrpreis gegenüber einem normalen Zaun gegen den Stromertrag.</li>
</ul>
{A.cta("Zaun, Dach oder beides?",
       "Wir sehen uns Grundstück, Verschattung und Verbrauch an und rechnen ehrlich, ob ein PV-Zaun bei Ihnen "
       "mehr bringt als zusätzliche Module am Dach oder ein Carport.",
       secondary=("photovoltaik", "Photovoltaik bei EBZ"))}
"""),
        ("Genehmigung in Kärnten und der Steiermark", "genehmigung", f"""
<p><b>Ein PV-Zaun ist zugleich Einfriedung und Photovoltaikanlage. In Kärnten und der Steiermark brauchen
niedrige Einfriedungen und kleinere PV-Anlagen keine Baubewilligung, müssen aber vor Baubeginn der Gemeinde
gemeldet werden.</b> Die Grenzen laut Landesgesetz (Stand November 2026):</p>
{A.table(
    ["", "Kärnten (§ 7 K-BO 1996)", "Steiermark (§ 21 Stmk. BauG)"],
    [
        ["Einfriedung", "in Leichtbauweise bis 2 m Höhe mitteilungspflichtig, mit Stützmauer bis 2,50 m "
         "Gesamthöhe", "bis 1,5 m über dem natürlichen Gelände meldepflichtig"],
        ["Photovoltaik", "Anlagen zur Erzeugung erneuerbarer Energie mitteilungspflichtig, im Gesetz ohne "
         "Größengrenze", "auf Freiflächen bis 100 kWp meldepflichtig, Anlagenteile höchstens 3,50 m hoch"],
        ["Was zu tun ist", "vor Baubeginn schriftliche Mitteilung an die Baubehörde mit Katastralgemeinde, "
         "Grundstücksnummer und Beschreibung", "vor der Ausführung schriftliche Meldung an die Gemeinde"],
        ["Was trotzdem gilt", "Flächenwidmungs- und Bebauungsplan dürfen nicht entgegenstehen",
         "Bau- und Raumordnungsvorschriften, Baufluchtlinien und Abstände sind einzuhalten"],
    ],
)}
{A.box("Ob ein Solarzaun rechtlich als Einfriedung, als Photovoltaikanlage oder als beides gilt, sagen die "
       "Gesetze nicht ausdrücklich. Wird der Zaun höher als 2 m (Kärnten) oder 1,5 m (Steiermark), steht er "
       "an einer Straße oder gibt es einen Bebauungsplan mit Vorgaben zu Einfriedungen, klären wir das vor der "
       "Bestellung mit dem Bauamt Ihrer Gemeinde.",
       label="Gemeinde fragen:")}
<p>Bei einer Grundgrenze zum Nachbarn lohnt außerdem ein Gespräch vorab: Die Rückseite des Zauns zeigt zum
Nachbargrundstück, und Sie brauchen Zugang für Montage und Reinigung.</p>
"""),
        ("Statik, Wind und Sicherheit", "statik", f"""
<p><b>Ein Solarzaun ist eine geschlossene Fläche und fängt den vollen Wind ab.</b> Die Windlast wird in
Österreich nach dem Eurocode bemessen (ÖNORM EN 1991-1-4 mit den nationalen Festlegungen der ÖNORM
B 1991-1-4), abhängig von Standort, Seehöhe und Geländeform. Daraus ergeben sich Pfostenabstand, Profilstärke
und Fundament.</p>
<ul>
  <li><b>Fundament:</b> Hersteller arbeiten mit Beton-Punktfundamenten, gerammten Stahlprofilen oder Montage
  auf einer Mauer. Bei großen Freiflächenanlagen rammt Next2Sun die ersten Pfosten einer Reihe 2 bis 2,5 m
  tief, weil am Reihenende die höchste Windlast auftritt.</li>
  <li><b>Hang:</b> Bei Gefälle wird der Zaun gestuft, die Modulunterkante sollte Abstand zu Boden und Bewuchs
  halten, damit die Rückseite Licht bekommt.</li>
  <li><b>Statiknachweis:</b> Für jede Anlage erstellt EBZ einen Projektbericht mit 3D-Belegplan und
  Statikreport.</li>
</ul>
<p><b>Ballwurf, Hagel und Vandalismus:</b> Glas-Glas-Module sind robust, aber Glas. Der Standardtest für
Solarmodule (IEC 61215) schießt 25-mm-Eiskugeln mit 23 m/s auf das Modul. Eine Norm für Ballwurf oder
Steinwurf gibt es nicht. Wo regelmäßig Fußball gespielt wird oder der Zaun direkt am Gehweg steht, sollte die
Position gut überlegt sein, etwa mit Abstand zur Spielfläche. Leitungen gehören geschützt verlegt, damit an
öffentlich zugänglichen Stellen keine Kabel offen liegen.</p>
"""),
        ("Netzanmeldung und Anschluss", "netz", f"""
<p><b>Ein fest angeschlossener PV-Zaun ist eine Erzeugungsanlage und wird vor der Errichtung beim
Netzbetreiber angemeldet,</b> in Kärnten und der Steiermark meist beim regionalen Verteilnetzbetreiber. Den
Ablauf beschreibt die Handlungsanleitung des Klima- und Energiefonds und von Photovoltaic Austria:</p>
{A.steps([
    ("Netzanschlussantrag", "Der Antrag mit Leistung, Wechselrichter und Speicher geht vor dem Bau an den "
     "Netzbetreiber, meist stellt ihn der Elektrofachbetrieb."),
    ("Anschlusskonzept und Zählpunkt", "Der Netzbetreiber prüft den Anschluss und teilt die Zählpunktnummer "
     "mit, die Sie auch für Förderung und Einspeisevertrag brauchen."),
    ("Errichtung", "Fundamente, Zaun, Module, Erdleitung und Wechselrichter durch zertifizierte Fachkräfte."),
    ("Fertigstellungsmeldung", "Nach der Montage wird die Anlage mit dem Installationsdokument fertig "
     "gemeldet."),
    ("Inbetriebsetzung", "Der Netzbetreiber prüft die Unterlagen, tauscht bei Bedarf den Zähler und gibt "
     "die Anlage frei."),
])}
<p>Gibt es schon eine Dachanlage, wird der Zaun als Erweiterung angemeldet. Welche Vergütung Sie für
eingespeisten Strom bekommen, erklärt der Ratgeber
{a('/einspeisetarif-fuer-photovoltaik/', 'Einspeisetarif für Photovoltaik')}.</p>
"""),
        ("Förderung 2026 für den PV-Zaun", "foerderung", f"""
<p><b>Eine eigene Förderung für Photovoltaik-Zäune gibt es in Kärnten und der Steiermark nicht.</b> Für den
Zaun gelten dieselben Programme wie für jede PV-Anlage, mit denselben Bedingungen (Stand November 2026):</p>
<ul>
  <li><b>Kärnten:</b> 3.000 Euro Pauschale für neue private PV-Anlagen ab 5 kWp mit gleichzeitig neuem
  Speicher ab 5 kWh, 1.000 Euro für die Speicher-Nachrüstung. Der zweite Landes-Call läuft bis
  31. Dezember 2026. Ob eine Zaunanlage alle Bedingungen erfüllt, prüfen wir vor dem Antrag. Details:
  {a('foerderung_kaernten', 'PV-Förderung Kärnten')}.</li>
  <li><b>Bund:</b> Der letzte EAG-Fördercall 2026 endete am 22. Oktober 2026, derzeit gibt es keinen
  Bundeszuschuss für neue Anlagen. Für 2027 ist laut BMWET eine Systemförderung für Speicher mit
  intelligenter Steuerung geplant, aber nicht beschlossen.</li>
  <li><b>Steiermark:</b> Derzeit keine Landesförderung für Photovoltaik, siehe
  {a('foerderung_steiermark', 'PV-Förderung Steiermark')}.</li>
  <li><b>Energiemanagement:</b> Die EMS-Förderung des Klimafonds (50 %, maximal 600 Euro) gilt unabhängig von
  der Bauform, Registrierung vor der ersten Rechnung.</li>
</ul>
<p>Alle Programme im Überblick: {a('foerderungen', 'Förderungen 2026')}.</p>
"""),
        ("Fazit: Für wen sich ein Solarzaun lohnt", "fazit", f"""
<p>Ein Photovoltaik-Zaun lohnt sich vor allem, wenn ohnehin ein neuer Zaun oder Sichtschutz geplant ist, das
Dach schon belegt oder ungeeignet ist und der Zaunverlauf frei von Schatten liegt. Er liefert in Villach
rechnerisch 80 bis 87 % des Dachertrags je kWp, und zwar zu Zeiten, in denen Haushalte Strom brauchen. Je kWp
ist er teurer als eine Dachanlage. Wer noch freie Dachfläche hat, nutzt sie zuerst; als Alternative mit
ähnlichem Nutzen kommt auch ein {a('carport', 'Solar-Carport')} infrage.</p>
<p><small>*Eigene Berechnung mit PVGIS 5.3 (Europäische Kommission, JRC) für Villach, 14 % Systemverluste,
Wetterdaten 2005 bis 2023 (Stundenwerte 2019 bis 2023), ohne Nahverschattung und Schnee. Bifazialer Zaun:
Vorderseite plus Rückseite mal 70 bis 85 % Bifazialität, Stundentabelle mit 85 %. Uhrzeiten in Sommerzeit. Richtwerte, kein Ersatz für
die Planung am Standort. Energiepreise Stand November 2026, OeMAG-Marktpreis Oktober 2026. Preise sind
Herstellerangaben und als solche gekennzeichnet.</small></p>
{A.cta("Passt ein PV-Zaun zu Ihrem Grundstück?",
       "Wir prüfen Zaunverlauf, Schatten, Untergrund und Baurecht und rechnen Ertrag und Kosten ehrlich gegen "
       "eine Dachanlage.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("referenzen", "Unsere Referenzen"))}
"""),
    ],

    "partner": {
        "h2": "Photovoltaik und Speicher aus einer Hand",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie plant und installiert Photovoltaik, Batteriespeicher, Wärmepumpen und "
                 "Energiemanagement in Kärnten und der Steiermark, mit zertifizierten Fachkräften und einem "
                 "festen Ansprechpartner von der Planung bis zur Übergabe. Wir verbauen bifaziale "
                 "Glas-Glas-Module und rechnen für jede Fläche vorab, was sie wirklich bringt."),
        "grid": [
            ("Ehrliche Rechnung", "Zaun, Dach oder Carport, mit Ertrag je Standort."),
            ("Baurecht geklärt", "Mitteilung oder Meldung bei der Gemeinde vor dem Bau."),
            ("Statik inklusive", "Projektbericht mit 3D-Belegplan und Statikreport."),
            ("Netz und Förderung", "Anmeldung und Anträge in der richtigen Reihenfolge."),
        ],
    },

    "faq": [
        ("Wie viel Strom bringt ein Photovoltaik-Zaun?",
         "Ein unverschatteter bifazialer Zaun mit Modulseiten nach Osten und Westen liefert in Villach rechnerisch "
         "rund 1.040 bis 1.130 kWh je kWp und Jahr. Das sind 80 bis 87 % einer Süd-Dachanlage mit 35° Neigung "
         "(rund 1.300 kWh je kWp). Schatten von Haus, Hecke oder Nachbargebäude senken den Wert."),
        ("Was kostet ein Meter Solarzaun?",
         "Hersteller nennen für das Material ab rund 250 Euro je Meter (Next2Sun, ohne Montage und Elektrik). "
         "Dazu kommen Fundament, Montage, Erdleitung und Wechselrichter. Einen neutralen Komplettpreis je Meter "
         "für Österreich gibt es nicht, wir nennen ihn nach der Besichtigung."),
        ("Brauche ich für einen PV-Zaun eine Genehmigung?",
         "In Kärnten sind Einfriedungen in Leichtbauweise bis 2 m Höhe und Anlagen für erneuerbare Energie "
         "mitteilungspflichtig, in der Steiermark Einfriedungen bis 1,5 m und PV-Freiflächenanlagen bis 100 kWp "
         "meldepflichtig. Beides heißt: keine Baubewilligung, aber schriftliche Meldung an die Gemeinde vor "
         "Baubeginn. Höhere Zäune oder Vorgaben im Bebauungsplan klären wir vorab mit dem Bauamt."),
        ("Ost-West oder Süd: Wie sollte ein Solarzaun ausgerichtet sein?",
         "Mit Modulseiten nach Osten und Westen erzeugt der Zaun rund 49 % seines Stroms vor 10 und ab 16 Uhr "
         "und kommt im Juni fast an eine Dachanlage heran. Mit Seiten nach Süden und Norden liefert er im "
         "Dezember mehr als ein 35°-Süddach, im Sommer aber deutlich weniger. Über das Jahr liegen beide bei "
         "rund 80 bis 87 % des Dachertrags."),
        ("Lohnt sich ein PV-Zaun mehr als eine Dachanlage?",
         "Je kWp meist nicht: Der Zaun bringt etwas weniger Ertrag und braucht zusätzlich Pfosten und "
         "Fundamente. Er lohnt sich, wenn ohnehin ein Zaun geplant ist, das Dach belegt ist oder Sie mehr "
         "Strom am Morgen und Abend selbst nutzen wollen."),
        ("Hält ein Solarzaun Ballwurf und Hagel aus?",
         "Glas-Glas-Module bestehen den Hageltest nach IEC 61215 mit 25-mm-Eiskugeln bei 23 m/s. Eine Norm für "
         "Ballwurf oder Steinwurf gibt es nicht. An Spielflächen oder direkt am Gehweg planen wir die Position "
         "deshalb gemeinsam mit Ihnen."),
        ("Gibt es eine Förderung für einen Photovoltaik-Zaun?",
         "Eine eigene Zaun-Förderung gibt es nicht. In Kärnten zahlt das Land 3.000 Euro für neue PV-Anlagen ab "
         "5 kWp mit Speicher ab 5 kWh, der zweite Call läuft bis 31. Dezember 2026. Der Bundeszuschuss ist für "
         "2026 abgeschlossen, die Steiermark fördert PV derzeit nicht."),
        ("Kann ich einen PV-Zaun mit einem Speicher kombinieren?",
         "Ja. Der Zaun wird wie jede PV-Anlage an einen Wechselrichter angeschlossen, ein Batteriespeicher "
         "nimmt den Überschuss auf. In Kärnten ist der Speicher ab 5 kWh sogar Voraussetzung für die "
         "Landesförderung von 3.000 Euro."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Mit zertifizierten Fachkräften plant und "
                    "installiert EBZ Energie Photovoltaik mit bifazialen Glas-Glas-Modulen, Batteriespeicher und "
                    "Energiemanagement in Kärnten und der Steiermark. Ertragswerte in diesem Ratgeber sind "
                    "Richtwerte aus PVGIS. Keine Rechtsberatung: Maßgeblich sind die Auskunft Ihrer Gemeinde und "
                    "die offiziellen Förderbedingungen."),
    "sources": [
        ("Europäische Kommission, JRC: PVGIS Photovoltaic Geographical Information System",
         "https://re.jrc.ec.europa.eu/pvg_tools/de/"),
        ("JUSLINE: § 7 Kärntner Bauordnung 1996 (mitteilungspflichtige Vorhaben)",
         "https://www.jusline.at/gesetz/k-bo_1996/paragraf/7"),
        ("JUSLINE: § 13 Kärntner Bauordnung 1996 (Vorprüfung)",
         "https://www.jusline.at/gesetz/k-bo_1996/paragraf/13"),
        ("JUSLINE: § 21 Steiermärkisches Baugesetz (meldepflichtige Vorhaben)",
         "https://www.jusline.at/gesetz/stmk_baug/paragraf/21"),
        ("Klima- und Energiefonds, Photovoltaic Austria: Handlungsanleitung für die Errichtung von PV-Anlagen",
         "https://klimafonds.gv.at/wp-content/uploads/2024/09/Handlungsanleitung-fuer-die-Errichtung-von-PV-Anlagen.pdf"),
        ("Next2Sun: Solarzaun (Hersteller, Deutschland)", "https://next2sun.com/solarzaun/"),
        ("Next2Sun: Agri-PV FAQ (Hersteller, englisch)", "https://next2sun.com/en/agripv/agripv-faqs/"),
        ("pv magazine: Studie der HTWK Leipzig zu senkrechten Ost-West-Anlagen (englisch, Juli 2022)",
         "https://www.pv-magazine.com/2022/07/11/the-stabilizing-effect-of-vertical-east-west-oriented-pv-systems/"),
        ("VOL.AT: Neue PV-Idee aus Österreich (Sunbooster, März 2026)",
         "https://www.vol.at/mehr-ertrag-als-am-dach-neue-pv-idee-aus-oesterreich/10027958"),
        ("Sinovoltaics: Hageltest nach IEC 61215 (englisch)",
         "https://sinovoltaics.com/learning-center/testing/what-is-iec-61215-mqt-17-solar-panel-hail-test-standard-explained/"),
        ("Austrian Standards: ÖNORM B 1991-1-4 Windeinwirkungen",
         "https://austrian-standards.at/en/shop/onorm-b-1991-1-4-2013-05-01~p2000677"),
        ("5min.at: Kärntner PV-Förderung, zweiter Call ab 12. Oktober 2026",
         "https://www.5min.at/kaernten/5202610030852/ab-12-oktober-diese-3-000-foerderung-gibt-es-wieder-fuer-kaerntner/"),
        ("E-Control: Strom- und Gaspreismonitor", "https://www.e-control.at/preismonitor"),
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/de/marktpreis/"),
    ],
    "related": [
        ("photovoltaik", "Photovoltaik vom Fachbetrieb in Kärnten und der Steiermark"),
        ("/pv-anlage-kwp-groessen/", "PV-Anlage: welche kWp-Größe passt"),
        ("foerderungen", "Förderungen 2026 im Überblick"),
        ("referenzen", "Referenzen: Anlagen mit Glas-Glas-Modulen"),
    ],
    "cta": {
        "h3": "PV-Zaun ehrlich durchgerechnet",
        "text": "Wir prüfen Zaunverlauf, Schatten und Baurecht und vergleichen mit Ihrer Dachfläche.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Strom vom Zaun, ehrlich gerechnet",
    "final_text": ("Kostenlose Erstberatung zu Photovoltaik am Dach, am Zaun und mit Speicher, mit transparenten "
                   "Zahlen und einem Ansprechpartner aus Villach."),
}
