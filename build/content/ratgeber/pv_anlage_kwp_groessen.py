"""Ratgeber: PV-Anlage mit 5, 10, 15 oder 20 kWp (Größenwahl).

Migriert von ebz-photovoltaik.at/pv-anlage-kwp-groessen/ (veröffentlicht 30.09.2026).
Fokus: Größe nach Verbrauch, Dachfläche und Speicherverhältnis. Preise nur kurz (Verweis auf
/kosten-einer-solaranlage/), Anbieterwahl in /pv-anlage-kaufen/.
Geändert gegenüber der Quelle:
  - Förderung auf Stand ab 23.10.2026: letzter EAG-Call beendet, Bund derzeit nicht beantragbar,
    Systemförderung 2027 laut BMWET geplant (nicht beschlossen); Kärnten 3.000 EUR ab 5 kWp mit Speicher.
    Tabellenzeile "EAG-Förderung (Okt. 2026)" und die Rechnung zur 10-kWp-Kategoriegrenze nur noch als
    Rückblick auf den Call 2026.
  - Preise: 10 kWp auf den EBZ-Richtpreis gesetzt (Quelle 12.000 bis 18.000 EUR widersprach dem Anker
    15.000 bis 22.000 EUR mit Speicher). Die Quellwerte für 15 und 20 kWp (17.000 bis 24.000 bzw.
    21.000 bis 30.000 EUR) waren damit je kWp teurer als 10 kWp und sind entfallen, ebenso das daraus
    abgeleitete Preis-je-kWp-Diagramm.
  - OeMAG-Wert September 2026 (10,168 ct) ergänzt; Eigenteam-Aussagen entfernt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "pv-anlage-kwp-groessen",
    "path": "/pv-anlage-kwp-groessen/",
    "title": "PV-Anlage 5, 10, 15 oder 20 kWp: richtige Größe | EBZ",
    "description": ("Wie viel kWp brauchen Sie? Faustregel Verbrauch durch 1.000, plus Wärmepumpe und E-Auto. "
                    "Dachfläche, Ertrag und Speichergröße für 5 bis 20 kWp im Vergleich."),
    "eyebrow": "Photovoltaik · Anlagengröße",
    "crumb_label": "PV-Anlage: kWp-Größen",
    "h1": "PV-Anlage mit 5, 10, 15 oder 20 kWp: So finden Sie die richtige Größe",
    "lead": ("Wie viel kWp Sie brauchen, hängt von Ihrem Verbrauch, Ihren Plänen für Wärmepumpe oder E-Auto und "
             "der Dachfläche ab. Dieser Ratgeber zeigt die Faustregel, vergleicht 5, 10, 15 und 20 kWp und erklärt, "
             "wie groß der Speicher dazu sein sollte."),
    "chips": [
        "Faustregel: <b>kWh ÷ 1.000 = kWp</b>",
        "1 kWp: <b>rund 5 m²</b> Dachfläche",
        "1 kWp: <b>1.000 bis 1.150 kWh</b> im Jahr",
        "Speicher: <b>1 bis 1,5 kWh</b> je 1.000 kWh",
    ],
    "date_published": "2026-09-30",
    "date_modified": "2026-10-21",
    "hero_img": "pv_efh",
    "hero_alt": "Photovoltaikmodule auf einem Hausdach: Anlagengröße in Kilowatt-Peak richtig wählen",

    "tldr": [
        "Faustregel: Jahresverbrauch in kWh geteilt durch 1.000 ergibt die sinnvolle Mindestgröße in kWp. Eine "
        "Wärmepumpe (rund 3.000 bis 4.000 kWh) und ein E-Auto (rund 2.000 kWh bei 12.000 km) rechnen Sie dazu.",
        "In Kärnten und der Steiermark erzeugt 1 kWp bei guter Lage grob 1.000 bis 1.150 kWh im Jahr und braucht "
        "rund 5 Quadratmeter Dachfläche. 10 kWp belegen also rund 50 Quadratmeter.",
        "Speicher: 1 bis 1,5 kWh je 1.000 kWh Jahresverbrauch, bei 10 kWp sind 5 bis 10 kWh typisch.",
        "Förderung ab 23. Oktober 2026: Der EAG-Bundeszuschuss ist für 2026 abgeschlossen, die Kategoriegrenze bei "
        "10 kWp spielt derzeit keine Rolle. Kärnten zahlt 3.000 Euro pauschal ab 5 kWp mit mindestens 5 kWh Speicher.",
        "Eingespeister Strom bringt nur den OeMAG-Marktpreis (September 2026: 10,168 Cent), selbst genutzter spart "
        "rund 25 bis 30 Cent. Größer planen lohnt sich, wenn Wärmepumpe oder E-Auto kommen.",
    ],
    "kpis": [
        ("÷ 1.000", "Jahresverbrauch in kWh ergibt die Mindestgröße in kWp"),
        ("rund 5 m²", "Dachfläche je kWp"),
        ("1.000 bis 1.150 kWh", "Jahresertrag je kWp bei guter Lage*"),
        ("5 bis 10 kWh", "typischer Speicher zu 10 kWp"),
    ],

    "sections": [
        ("Wie viel kWp brauchen Sie? Die Faustregel", "faustregel", f"""
<p><b>Die richtige Größe einer PV-Anlage ergibt sich aus dem Jahresverbrauch: Kilowattstunden geteilt durch
1.000 ergibt die sinnvolle Mindestgröße in Kilowatt-Peak (kWp).</b> Ein Haushalt mit 4.000 kWh kommt so auf rund
4 bis 5 kWp, mit Wärmepumpe und E-Auto landen viele Familien bei 10 bis 15 kWp. 1 kWp erzeugt in Kärnten und der
Steiermark bei guter Lage grob 1.000 bis 1.150 kWh im Jahr und braucht rund 5 Quadratmeter Dach.</p>
<p>Die Größe einer PV-Anlage wird in kWp angegeben, der Spitzenleistung unter Normbedingungen. Wie viel Sie
brauchen, hängt von drei Dingen ab: Ihrem heutigen Stromverbrauch, Ihren Plänen für die nächsten Jahre und der
verfügbaren Dachfläche.</p>
{A.box_dark("Faustregel",
    "<b>Jahresverbrauch in kWh geteilt durch 1.000 ergibt die sinnvolle Mindestgröße in kWp.</b> Dazu rechnen Sie "
    "geplante Verbraucher: Eine Wärmepumpe braucht im Einfamilienhaus rund 3.000 bis 4.000 kWh im Jahr, ein E-Auto "
    "bei 12.000 Kilometern rund 2.000 kWh.")}
<p>Beispiel: Eine Familie mit 4.000 kWh Haushaltsstrom plant eine Luftwärmepumpe (3.500 kWh) und ein E-Auto
(2.200 kWh). Zusammen sind das knapp 10.000 kWh, die sinnvolle Größe liegt also bei 10 kWp oder etwas darüber.
Wie Wärmepumpe und PV zusammenspielen, zeigt der Ratgeber
{a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}.</p>
"""),
        ("5, 10, 15 und 20 kWp im direkten Vergleich", "vergleich", f"""
{A.table(
    ["", "5 kWp", "10 kWp", "15 kWp", "20 kWp"],
    [
        ["Module (ca. 430 Wp)", "rund 12", "rund 24", "rund 35", "rund 47"],
        ["Dachfläche", "rund 25 m²", "rund 50 m²", "rund 75 m²", "rund 100 m²"],
        ["Stromerzeugung pro Jahr*", "5.000 bis 5.700 kWh", "10.000 bis 11.500 kWh", "15.000 bis 17.000 kWh",
         "20.000 bis 23.000 kWh"],
        ["Passt für", "Singles, Paare, kleiner Verbrauch", "Familie, oft mit Wärmepumpe", "Wärmepumpe und E-Auto",
         "großer Verbrauch, Landwirtschaft, Betrieb"],
        ["Landespauschale Kärnten**", "3.000 €", "3.000 €", "3.000 €", "3.000 €"],
    ],
)}
<p><small>*Richtwert für Kärnten und die Steiermark bei guter Südausrichtung ohne Verschattung, 1.000 bis
1.150 kWh je kWp. **Nur mit gleichzeitig neuem Speicher ab 5 kWh, 2. Landes-Call 2026, Stand Oktober 2026.</small></p>
<h3>5 kWp: Der Einstieg</h3>
<p>Eine 5-kWp-Anlage passt zu kleinen Haushalten mit 2.500 bis 4.000 kWh Verbrauch, zu kleinen Dachflächen oder als
Zweitanlage auf Garage oder {a('carport', 'Carport')}. Sie ist in absoluten Euro die günstigste Anlage, pro kWp
aber die teuerste, weil Gerüst, Wechselrichter und Anmeldung fast gleich viel kosten wie bei einer doppelt so
großen Anlage. Wer eine Erweiterung plant, wählt gleich einen passenden Wechselrichter. 5 kWp sind zugleich die
Untergrenze für die Kärntner Landespauschale.</p>
<h3>10 kWp: Der Standard fürs Einfamilienhaus</h3>
<p>Mit rund 10.000 kWh im Jahr deckt eine 10-kWp-Anlage den Verbrauch einer Familie und einen guten Teil einer
Wärmepumpe ab. Mit 5 bis 10 kWh Speicher steigt der Eigenverbrauch deutlich. Was in einem Komplettpaket steckt,
zeigt der Ratgeber {a('/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/', 'Photovoltaik-Komplettanlage 10 kWp mit Speicher')}.</p>
<h3>15 kWp: Für Haus mit Wärmepumpe und E-Auto</h3>
<p>Wer mit Strom heizt und fährt, profitiert von jeder zusätzlichen Kilowattstunde. 15 kWp liefern auch im Frühjahr
und Herbst genug für Wärmepumpe und Auto. Der Preis je kWp liegt unter dem kleinerer Anlagen.</p>
<h3>20 kWp: Für großen Verbrauch</h3>
<p>20 kWp lohnen sich bei hohem Eigenverbrauch, etwa in der Landwirtschaft, mit Einliegerwohnung, Pool, zwei
E-Autos oder im kleinen Betrieb. Überschüsse lassen sich über eine {a('eg', 'Energiegemeinschaft')} oft besser
verwerten als über die reine Einspeisung. Ab dieser Größe kann der Netzbetreiber eine Einspeisebegrenzung
vorschreiben, das klären wir mit dem Netzzugangsantrag.</p>
"""),
        ("Dachfläche: Was passt auf Ihr Dach?", "dachflaeche", f"""
<p>Mit modernen Modulen um 430 Watt braucht 1 kWp rund 5 Quadratmeter Dachfläche. Eine 10-kWp-Anlage benötigt
also etwa 50 Quadratmeter, eine 20-kWp-Anlage rund 100 Quadratmeter, jeweils ohne Randabstände, Dachfenster,
Kamine und Gauben. Die nutzbare Fläche ist daher fast immer kleiner als die Dachfläche laut Plan.</p>
<ul>
  <li><b>Ausrichtung:</b> Süddächer liefern den höchsten Jahresertrag. Ost-West-Dächer liegen etwas darunter,
  erzeugen den Strom aber gleichmäßiger über den Tag, morgens und abends, wenn der Haushalt ihn braucht.</li>
  <li><b>Verschattung:</b> Bäume, Nachbargebäude oder Kamine kosten Ertrag. Sie entscheiden mit, welche
  Dachflächen sich überhaupt lohnen.</li>
  <li><b>Statik und Eindeckung:</b> Ziegel, Blechfalz oder Trapezblech brauchen unterschiedliche
  Unterkonstruktionen. Die Tragfähigkeit prüfen wir vor dem Angebot.</li>
</ul>
<p>Wie viele Module tatsächlich auf Ihr Dach passen, zeigt der Projektbericht mit 3D-Belegplan und Statikreport.
Eine erste Schätzung liefert der {a('solarrechner', 'EBZ-Solarrechner')}.</p>
"""),
        ("Speichergröße passend zur Anlage", "speicher", f"""
<p>In der Praxis haben sich für Einfamilienhäuser <b>1 bis 1,5 kWh Speicher je 1.000 kWh Jahresverbrauch</b>
bewährt. Bei 10 kWp PV sind 5 bis 10 kWh Speicher typisch. Ein zu großer Speicher wird im Winter nie voll, ein zu
kleiner ist im Sommer schnell am Limit.</p>
{A.table(
    ["Jahresverbrauch", "Speicher nach Faustregel*", "Passende PV-Größe*"],
    [
        ["3.000 kWh", "3 bis 4,5 kWh", "rund 3 bis 5 kWp"],
        ["4.500 kWh", "4,5 bis 7 kWh", "rund 5 kWp"],
        ["6.000 kWh", "6 bis 9 kWh", "rund 6 bis 10 kWp"],
        ["8.000 kWh (mit Wärmepumpe oder E-Auto)", "8 bis 12 kWh", "rund 8 bis 15 kWp"],
    ],
    hl_cols=(1,),
)}
<p>Zwei Förderregeln beeinflussen die Speichergröße: In Kärnten gibt es die Landespauschale von 3.000 Euro nur
für eine neue Anlage ab 5 kWp mit gleichzeitig neuem Speicher ab 5 kWh. Und für 2027 plant der Bund laut BMWET
eine Systemförderung für Speicher mit intelligenter Steuerung (nicht beschlossen, Kriterien offen). Im Call 2026
verlangte der Bund mindestens 0,5 kWh Speicher je kWp. Wann sich ein Speicher rechnet, erklärt der Ratgeber
{a('/ab-wann-lohnt-sich-photovoltaik-mit-speicher/', 'Ab wann lohnt sich Photovoltaik mit Speicher')}, die
Technik steht auf der Seite {a('batteriespeicher', 'Batteriespeicher')}.</p>
<p><small>*Richtwerte nach der Faustregel 1 bis 1,5 kWh Speicher je 1.000 kWh Verbrauch und Verbrauch durch
1.000 als Mindestgröße der PV-Anlage. Die PV-Spanne berücksichtigt Reserve für künftige Verbraucher.</small></p>
"""),
        ("Was kosten die Größen ungefähr?", "kosten", f"""
<p>Der Richtpreis für 10 kWp liegt bei rund 10.000 bis 15.000 Euro ohne Speicher und rund 15.000 bis
22.000 Euro mit Speicher vor Förderung*. Eine 5-kWp-Anlage kostet meist 7.000 bis 10.000 Euro* und ist damit pro
kWp deutlich teurer. Bei 15 und 20 kWp sinkt der Preis je kWp weiter, weil sich Gerüst, Elektrik, Wechselrichter
und Anmeldung auf mehr Leistung verteilen; wie stark, hängt bei großen Anlagen vor allem von Dach und Zählerplatz
ab. Die vollständige Preisübersicht steht im Ratgeber
{a('/kosten-einer-solaranlage/', 'Kosten einer Solaranlage')}.</p>
<p><small>*Richtwerte, Stand Oktober 2026, schlüsselfertig inklusive Montage und 20 Prozent Umsatzsteuer, vor
Förderung. Der verbindliche Preis steht nach der Besichtigung im Festpreisangebot.</small></p>
{A.cta("Welche Größe passt zu Ihrem Dach?",
       "Wir prüfen Dachfläche, Statik und Verbrauch vor Ort und erstellen einen Projektbericht mit 3D-Belegplan "
       "und Statikreport, inklusive passender Speichergröße.",
       primary=("kontakt", "Beratung anfragen"), secondary=("solarrechner", "Solarrechner starten"))}
"""),
        ("Förderung und Anlagengröße: Stand ab 23. Oktober 2026", "foerderung", f"""
<p>Im EAG-Fördercall 2026 hing die Bundesförderung direkt an der Größe: 150 Euro je kWp bis 10 kWp
(Kategorie A), 140 Euro je kWp über 10 bis 20 kWp (Kategorie B) und 150 Euro je kWh Speicher. Weil der Satz für die
ganze Anlage galt, bekam eine Anlage knapp über 10 kWp rechnerisch weniger als eine mit genau 10 kWp:</p>
{A.table(
    ["Anlagengröße", "Kategorie im Call 2026", "Bundesförderung im Call 2026"],
    [
        ["10,0 kWp", "A, 150 € je kWp", "1.500 €"],
        ["10,5 kWp", "B, 140 € je kWp", "1.470 €"],
        ["11,0 kWp", "B, 140 € je kWp", "1.540 €"],
    ],
    hl_cols=(2,),
)}
<p><b>Diese Grenze spielt derzeit keine Rolle mehr:</b> Der dritte und letzte Call 2026 endete am
22. Oktober 2026, neue Anlagen bekommen aktuell keinen Bundeszuschuss. Für 2027 ist laut BMWET eine
Systemförderung für Speicher mit intelligenter Steuerung geplant, beantragt nach Installation und Rechnung;
beschlossen ist sie nicht, Höhe und Kriterien sind offen.</p>
<p>Was heute zählt, ist größenunabhängig: Kärnten zahlt 3.000 Euro pauschal für eine neue private Anlage ab
5 kWp mit Speicher ab 5 kWh, egal ob 5 oder 20 kWp (2. Landes-Call bis 31. Dezember 2026, Antrag nach
Fertigstellung, höchstens 50 Prozent der Baukosten). In der Steiermark ist derzeit keine PV-Landesförderung
offen. Für das {a('ems', 'Energiemanagement')} sind über den Klimafonds bis zu 600 Euro möglich.</p>
{A.box("Wählen Sie die Größe nach Verbrauch und Plänen, nicht nach einer Förderkategorie. Die Kriterien der "
       "Systemförderung 2027 sind noch nicht bekannt, sicher ist nur: Speicher und intelligente Steuerung "
       "stehen im Mittelpunkt.")}
<p>Alle Details im Ratgeber {a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}
und unter {a('foerderung_kaernten', 'Photovoltaik-Förderung Kärnten')}.</p>
"""),
        ("Größer planen oder nicht? Die Rechnung mit der Einspeisung", "groesser-planen", f"""
<p>Früher galt: Anlage so groß wie das Dach. Heute ist es differenzierter, denn eingespeister Strom bringt nur den
OeMAG-Marktpreis, im September 2026 waren das 10,168 Cent je Kilowattstunde, im Juli 6,146 Cent (siehe
{a('/oemag-einspeisetarif/', 'OeMAG-Einspeisetarif')}). Selbst verbrauchter Strom spart dagegen rund 25 bis
30 Cent. Die Wirtschaftlichkeit hängt deshalb vor allem am Eigenverbrauch.</p>
<p>Trotzdem spricht einiges dafür, eher großzügig zu planen:</p>
<ul>
  <li>Zusätzliche kWp sind günstig, weil Gerüst, Elektrik und Anmeldung ohnehin anfallen.</li>
  <li>Wärmepumpe, E-Auto oder Klimagerät kommen oft erst ein paar Jahre nach der PV-Anlage.</li>
  <li>Eine spätere Erweiterung kostet pro kWp deutlich mehr als eine gleich größere Anlage.</li>
  <li>Mit Energiegemeinschaft und {a('/dynamischer-stromtarif/', 'dynamischem Stromtarif')} lässt sich
  Überschuss besser verwerten.</li>
</ul>
{A.box("Für einen Zwei-Personen-Haushalt ohne Wärmepumpe und E-Auto ist eine 20-kWp-Anlage meist "
       "überdimensioniert. Wir empfehlen die Größe, die zu Ihrem Verbrauch und Ihren Plänen passt, nicht die "
       "größte, die aufs Dach passt.", label="Ehrlich gesagt:")}
"""),
        ("So finden wir die richtige Größe für Sie", "ablauf", f"""
{A.steps([
    ("Verbrauch und Pläne", "Wir sehen uns Ihre Stromrechnung an und besprechen Wärmepumpe, E-Auto und andere "
     "geplante Verbraucher."),
    ("Dach vor Ort prüfen", "Ausrichtung, Neigung, Verschattung, Statik und Zählerkasten."),
    ("Projektbericht", "Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport mit der passenden "
     "Anlagen- und Speichergröße."),
    ("Förderung", "Wir prüfen Landes- und EMS-Förderung, stellen die Anträge in der richtigen Reihenfolge und "
     "planen mit Blick auf die Systemförderung 2027."),
    ("Montage", "Zertifizierte Fachkräfte montieren und nehmen die Anlage in Betrieb."),
])}
{A.cta("Anlagengröße festlegen, Förderung sichern",
       "Beratung, Projektbericht, Förderabwicklung und Montage aus einer Hand. Auf Wunsch mit Finanzierung, die "
       "Anlage gehört ab Tag 1 Ihnen.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("/pv-anlage-kaufen/", "PV-Anlage kaufen: Checkliste"))}
"""),
        ("Fazit: Die richtige Größe folgt dem Verbrauch von morgen", "fazit", f"""
<p>5 kWp für den kleinen Haushalt, 10 kWp als Standard für die Familie, 15 kWp mit Wärmepumpe und E-Auto, 20 kWp
für großen Verbrauch. Weil jedes zusätzliche kWp günstiger wird, lohnt es sich, künftige Verbraucher gleich
mitzudenken, und ein Speicher von 1 bis 1,5 kWh je 1.000 kWh Verbrauch rundet die Anlage ab. Die Kategoriegrenze
bei 10 kWp ist seit dem Ende des Bundescalls 2026 kein Kriterium mehr; in Kärnten zählt nur: ab 5 kWp mit
Speicher ab 5 kWh.</p>
"""),
    ],

    "partner": {
        "h2": "Die passende Anlagengröße vom Fachbetrieb",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie plant Photovoltaik in Kärnten und der Steiermark nach Ihrem Verbrauch und Ihren Plänen, "
                 "nicht nach der Dachgröße. Mit Projektbericht, zertifizierten Fachkräften, Förderabwicklung und auf "
                 "Wunsch Finanzierung ab 147 Euro im Monat."),
        "grid": [
            ("Auslegung nach Verbrauch", "Heute und mit Wärmepumpe oder E-Auto von morgen."),
            ("3D-Belegplan und Statikreport", "Vor der Entscheidung, nicht danach."),
            ("Speicher passend dimensioniert", "Nach Verbrauch und mit Blick auf die Förderbedingungen."),
            ("Finanzierung möglich", "Anlage gehört ab Tag 1 Ihnen."),
        ],
    },

    "faq": [
        ("Wie viel kWp brauche ich für mein Einfamilienhaus?",
         "Als Faustregel teilen Sie Ihren Jahresstromverbrauch in Kilowattstunden durch 1.000. Ein Haushalt mit "
         "4.000 kWh kommt so auf rund 4 bis 5 kWp. Planen Sie eine Wärmepumpe oder ein E-Auto, rechnen Sie deren "
         "Verbrauch dazu, dann landen viele Familien bei 10 bis 15 kWp."),
        ("Wie viel Strom erzeugt 1 kWp in Kärnten und der Steiermark?",
         "Bei guter Ausrichtung ohne Verschattung erzeugt ein Kilowatt-Peak in unserer Region grob 1.000 bis "
         "1.150 Kilowattstunden im Jahr. Ost-West-Dächer liegen etwas darunter, erzeugen den Strom aber "
         "gleichmäßiger über den Tag."),
        ("Wie viel Dachfläche braucht eine 10-kWp-Anlage?",
         "Mit modernen Modulen um 430 Watt braucht 1 kWp rund 5 Quadratmeter. Eine 10-kWp-Anlage benötigt also "
         "etwa 50 Quadratmeter für rund 24 Module, eine 20-kWp-Anlage rund 100 Quadratmeter, jeweils ohne "
         "Randabstände und Dachfenster."),
        ("Wie groß sollte der Speicher zur PV-Anlage sein?",
         "Für Einfamilienhäuser haben sich 1 bis 1,5 kWh Speicher je 1.000 kWh Jahresverbrauch bewährt. Bei 10 kWp "
         "PV sind 5 bis 10 kWh typisch. Für die Kärntner Landespauschale braucht es mindestens 5 kWh."),
        ("Ist eine größere PV-Anlage immer besser?",
         "Nicht automatisch. Eingespeister Strom bringt nur den OeMAG-Marktpreis, im September 2026 rund 10 Cent, im "
         "Juli rund 6 Cent je Kilowattstunde. Größer lohnt sich, wenn Wärmepumpe, E-Auto oder eine "
         "Energiegemeinschaft den Strom nutzen. Weil jedes zusätzliche kWp vergleichsweise günstig ist, raten wir zu "
         "großzügiger Planung, wenn der Verbrauch in den nächsten Jahren steigt."),
        ("Welche Förderung gibt es für 5, 10, 15 oder 20 kWp?",
         "Der EAG-Bundeszuschuss ist für 2026 abgeschlossen, der letzte Call endete am 22. Oktober 2026; ab 2027 ist "
         "laut BMWET eine Systemförderung geplant (nicht beschlossen). Kärnten zahlt größenunabhängig 3.000 Euro "
         "für neue Anlagen ab 5 kWp mit Speicher ab 5 kWh, in der Steiermark gibt es derzeit keine PV-Landesförderung."),
        ("Was kostet eine PV-Anlage mit 10 kWp?",
         "Rund 10.000 bis 15.000 Euro ohne Speicher und rund 15.000 bis 22.000 Euro mit Speicher vor Förderung, "
         "inklusive Montage und 20 Prozent Umsatzsteuer (EBZ-Richtpreis). Eine 5-kWp-Anlage kostet meist 7.000 bis "
         "10.000 Euro, größere Anlagen sind pro kWp günstiger."),
        ("Brauche ich für 20 kWp eine Genehmigung des Netzbetreibers?",
         "Jede PV-Anlage braucht einen Netzzugangsantrag beim Netzbetreiber. Ab rund 20 kWp kann der Netzbetreiber "
         "eine Einspeisebegrenzung vorschreiben. Das klären wir vor der Montage im Netzzugangsantrag."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. EBZ Energie plant und installiert "
                    "Photovoltaik, Batteriespeicher, Wärmepumpen und Wallboxen in Kärnten und der Steiermark, über "
                    "300 dokumentierte Projekte, und übernimmt die komplette Förderabwicklung. Erträge und Größen "
                    "beruhen auf realen Projekten in der Region. Keine Rechts- oder Steuerberatung, maßgeblich sind "
                    "die offiziellen Förderbedingungen der jeweiligen Stelle."),
    "sources": [
        ("EAG-Abwicklungsstelle: Investitionszuschuss Photovoltaik und Speicher",
         "https://www.eag-abwicklungsstelle.at/wissen/investitionszuschuss-photovoltaik-und-speicher/"),
        ("LK Kärnten: EAG-Investitionszuschuss, letzter Fördercall 2026",
         "https://ktn.lko.at/eag-investitionszuschuss-letzter-f%C3%B6rdercall-2026+2400+4457200"),
        ("Conversio Energie: Photovoltaik Kosten Österreich 2026",
         "https://www.conversioenergie.at/ratgeber/photovoltaik-kosten-oesterreich"),
    ],
    "related": [
        ("/pv-anlage-kaufen/", "PV-Anlage kaufen: Anbieter wählen"),
        ("/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/", "Komplettanlage 10 kWp mit Speicher"),
        ("/ab-wann-lohnt-sich-photovoltaik-mit-speicher/", "Ab wann lohnt sich Photovoltaik mit Speicher?"),
        ("solarrechner", "EBZ-Solarrechner"),
    ],
    "cta": {
        "h3": "Die richtige Größe für Ihr Dach",
        "text": "Projektbericht mit 3D-Belegplan und Statikreport, inklusive passender Speichergröße. Kostenlos.",
        "primary": ("kontakt", "Beratung anfragen"),
    },
    "final_h2": "Planen wir Ihre Anlage passend",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein fester Ansprechpartner aus Villach, der "
                   "Planung, Montage und Förderabwicklung aus einer Hand übernimmt."),
}
