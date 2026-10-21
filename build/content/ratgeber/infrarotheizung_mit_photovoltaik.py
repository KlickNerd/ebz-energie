"""Ratgeber: Infrarotheizung mit Photovoltaik (Kosten, Stromverbrauch, Vergleich mit Wärmepumpe).

Migriert vom WordPress-Artikel ebz-photovoltaik.at/infrarotheizung-mit-photovoltaik/
(veröffentlicht 2026-09-25, geändert 2026-09-30). Struktur, Preise und Verbrauchswerte aus der Quelle.
Ausrichtung: neutral beratend. EBZ bietet Infrarotheizungen derzeit nicht prominent als eigene Leistung an:
Angebotsaussagen ("Unsere Infrarotheizsysteme", "alle Systeme im Programm") und der Link auf
/infrarotheizsysteme/ wurden entfernt, CTA auf Beratung zu PV und Wärmepumpe.
Korrigiert: Strombedarf Wärmepumpe im Vergleich (Quelle 2.000 bis 4.000 kWh widersprach dem eigenen
Faktor 3 bis 4; jetzt aus 5.000 bis 7.000 kWh Wärme und JAZ 3,5 bis 4 gerechnet), Einspeisewert
"rund 6 Cent" durch OeMAG-Marktpreis September 2026 ersetzt, EAG-Aussage auf Stand ab 23.10.2026,
Bundesförderung Wärmepumpe nicht als "2027 angekündigt/ja", EMS-Förderung: Infrarot zählt nicht als
förderfähige Komponente. Links /luftwaermepumpe-kosten/ und /batteriespeicher-und-photovoltaik/ ersetzt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "infrarotheizung-mit-photovoltaik",
    "path": "/infrarotheizung-mit-photovoltaik/",
    "cluster": "Wärmepumpe und Heizen",
    "title": "Infrarotheizung mit Photovoltaik: Lohnt sich das? | EBZ",
    "description": ("Infrarotheizung mit PV: 200 bis 700 € je Paneel, doch 1 kWh Strom ergibt nur 1 kWh Wärme. "
                    "Wann Infrarot passt und wann die Wärmepumpe 3 bis 4 Mal sparsamer ist."),
    "eyebrow": "Heizen · Infrarot und Photovoltaik",
    "crumb_label": "Infrarotheizung mit Photovoltaik",
    "h1": "Infrarotheizung mit Photovoltaik: Wann sie sich lohnt und warum sie 3 bis 4 Mal mehr Strom braucht als eine Wärmepumpe",
    "lead": ("Eine Infrarotheizung ist mit 4.000 bis 7.000 Euro für ein Einfamilienhaus günstig in der Anschaffung, "
             "macht aber aus einer Kilowattstunde Strom nur eine Kilowattstunde Wärme. Dieser Ratgeber zeigt "
             "ehrlich, wann Infrarot mit Sonnenstrom passt (Bad, Einzelräume, Passivhaus) und wann eine "
             "Wärmepumpe die bessere Wahl bleibt."),
    "chips": [
        "Paneel: <b>200 bis 700 €</b>*",
        "Haus komplett: <b>4.000 bis 7.000 €</b>*",
        "Effizienz: <b>1 kWh Strom = 1 kWh Wärme</b>",
        "Ideal: <b>Bad und Übergangszeit</b>",
    ],
    "date_published": "2026-09-25",
    "date_modified": "2026-10-21",
    "hero_img": "gen_hero",
    "hero_alt": "Photovoltaikmodule auf einem Ziegeldach mit Kamin vor blauem Himmel",

    "tldr": [
        "Eine Infrarotheizung ist günstig in der Anschaffung: 200 bis 700 Euro je Paneel, rund 4.000 bis 7.000 "
        "Euro für ein Einfamilienhaus inklusive Elektroinstallation.",
        "Als Direktstromheizung macht sie aus einer Kilowattstunde Strom eine Kilowattstunde Wärme. Eine "
        "Wärmepumpe braucht für dieselbe Wärme nur ein Drittel bis ein Viertel des Stroms.",
        "Im 100-m²-Neubau braucht Infrarot als Hauptheizung 5.000 bis 7.000 Kilowattstunden Strom, das sind "
        "1.400 bis 1.960 Euro pro Jahr. Eine Wärmepumpe kommt im selben Haus mit rund 1.300 bis 2.000 "
        "Kilowattstunden aus.",
        "Photovoltaik hilft vor allem in der Übergangszeit. Im Dezember und Jänner liefert die PV-Anlage nur "
        "wenige Prozent ihres Jahresertrags, dann kommt der Großteil des Heizstroms aus dem Netz.",
        "Sinnvoll ist Infrarot im Bad, in selten genutzten Räumen, im Passivhaus und im Ferienhaus. Eine "
        "Förderung für Infrarot als Hauptheizung gibt es weder vom Bund noch in Kärnten oder der Steiermark.",
    ],
    "kpis": [
        ("200 bis 700 €", "je Infrarot-Paneel*"),
        ("4.000 bis 7.000 €", "ganzes Einfamilienhaus*"),
        ("1 : 1", "Strom zu Wärme (Wärmepumpe 1 : 3 bis 5)"),
        ("rund 60 €", "Strom pro Jahr fürs Bad-Paneel*"),
    ],

    "sections": [
        ("So funktioniert eine Infrarotheizung", "funktion", f"""
<p><b>Eine Infrarotheizung ist eine Direktstromheizung: Aus einer Kilowattstunde Strom wird genau eine
Kilowattstunde Wärme. Eine Wärmepumpe macht aus derselben Kilowattstunde drei bis fünf.</b> Infrarot erwärmt
nicht in erster Linie die Luft, sondern die Flächen und Menschen im Raum, ähnlich wie Sonnenstrahlen. Das
fühlt sich schon bei etwas niedrigerer Raumtemperatur angenehm an, und die Wärme ist nach wenigen Minuten
spürbar. Die Paneele sind flach, wartungsfrei und lassen sich an Wand oder Decke montieren, auch als
Spiegel oder Bild.</p>
<p>Damit stellt sich bei Infrarot mit Photovoltaik eine einzige entscheidende Frage: Wie viel des
Heizstroms kann Ihre PV-Anlage liefern, wenn tatsächlich geheizt wird? Wie eine Wärmepumpe die
Umgebungswärme nutzt, erklärt der Ratgeber
{a('/funktionsweise-einer-waermepumpe/', 'Funktionsweise einer Wärmepumpe')}.</p>
"""),
        ("Photovoltaik und Infrarot: Das Winterproblem", "winter", f"""
<p>Die Idee klingt verlockend: Das Dach produziert Strom, die Paneele machen daraus Wärme. In der Praxis
passen Angebot und Bedarf zeitlich aber schlecht zusammen. In einem Einfamilienhaus in Kärnten oder der
Steiermark fällt im Dezember und Jänner rund ein Drittel des Jahresheizbedarfs an, die PV-Anlage liefert in
diesen beiden Monaten aber nur wenige Prozent ihres Jahresertrags*.</p>
<p>Heizen Sie ein ganzes Haus mit Infrarot, deckt die eigene PV-Anlage erfahrungsgemäß nur einen kleineren
Teil des Heizstroms, grob ein Fünftel bis ein Drittel, je nach Speicher und Nutzung*. Der Rest kommt aus dem
Netz, und zwar im Winter, wenn Strom oft am teuersten ist. Ein Batteriespeicher ändert daran wenig: Im tiefen
Winter bleibt er mangels Überschuss oft leer.</p>
{A.box("In der Übergangszeit von März bis Mai und September bis November gibt es an vielen Tagen "
       "Sonnenüberschuss und gleichzeitig leichten Heizbedarf. Wer dann Bad, Arbeitszimmer oder Wintergarten "
       "mit Infrarot temperiert, nutzt Strom, der sonst zum OeMAG-Marktpreis ins Netz ginge (September 2026: "
       f"10,168 ct je kWh, Juli 2026: 6,146 ct; der Wert schwankt monatlich, siehe {a('marktpreis', 'Marktpreis 2026')}).",
       label="Wo PV und Infrarot gut zusammenpassen:")}
<p><small>*Schematische Richtwerte für ein Einfamilienhaus in Kärnten oder der Steiermark. Der tatsächliche
Anteil hängt von Anlagengröße, Ausrichtung, Speicher und Heizverhalten ab.</small></p>
"""),
        ("Was kostet eine Infrarotheizung?", "kosten", f"""
<h3>Anschaffung: Leistung je Quadratmeter</h3>
{A.table(
    ["Gebäudestandard", "Leistung je m²*", "Beispiel 20-m²-Zimmer*"],
    [
        ["Passivhaus, Niedrigenergiehaus", "30 bis 40 W", "600 bis 800 W"],
        ["gut gedämmter Neubau", "40 bis 60 W", "800 bis 1.200 W"],
        ["durchschnittlicher Bestand", "60 bis 80 W", "1.200 bis 1.600 W"],
        ["unsanierter Altbau", "80 bis 100 W", "1.600 bis 2.000 W"],
    ],
    hl_cols=(1,),
)}
<p>Ein Paneel kostet je nach Leistung und Ausführung meist 200 bis 700 Euro, grob 50 bis 90 Euro je 100
Watt*. Für ein komplettes Einfamilienhaus sind 4.000 bis 7.000 Euro inklusive Elektroinstallation
realistisch. Das ist ein Bruchteil der Kosten einer {a('/luftwaermepumpe-preise/', 'Luftwärmepumpe')}
(14.000 bis 28.000 Euro).</p>
<h3>Betrieb: Stromverbrauch und Kosten pro Jahr</h3>
{A.table(
    ["Anwendung", "Stromverbrauch*", "Kosten pro Jahr bei 28 ct/kWh*"],
    [
        ["Bad als Zusatzheizung, 600 W, 2 Stunden täglich in der Heizsaison", "rund 220 kWh", "rund 60 €"],
        ["Infrarot als Hauptheizung, Neubau 100 m²", "5.000 bis 7.000 kWh", "1.400 bis 1.960 €"],
        ["Zum Vergleich: Wärmepumpe, gleiches Haus (JAZ 3,5 bis 4)", "rund 1.300 bis 2.000 kWh", "rund 350 bis 560 €"],
    ],
    hl_cols=(2,),
)}
<p>Die Rechnung zeigt das Muster: Infrarot ist günstig in der Anschaffung und teuer im Betrieb, die
Wärmepumpe umgekehrt. Je höher Ihr Wärmebedarf, desto schneller holt die Wärmepumpe ihre Mehrkosten wieder
herein.</p>
<p><small>*Richtwerte. Die genaue Auslegung hängt von Raumhöhe, Fenstern und Dämmung ab, die Kosten von
Ihrem Stromtarif.</small></p>
"""),
        ("Infrarotheizung oder Wärmepumpe: der ehrliche Vergleich", "vergleich", f"""
{A.table(
    ["", "Infrarotheizung", "Wärmepumpe (Luft-Wasser)"],
    [
        ["Anschaffung Einfamilienhaus*", "4.000 bis 7.000 €", "14.000 bis 28.000 €"],
        ["Effizienz", "1 kWh Strom = 1 kWh Wärme", "1 kWh Strom = 3 bis 5 kWh Wärme"],
        ["Strombedarf 100 m² Neubau*", "5.000 bis 7.000 kWh", "rund 1.300 bis 2.000 kWh"],
        ["Förderung Heizungstausch", "nein", "Kärnten 3.000 € Pauschale; Bund 2026 ausgeschöpft"],
        ["Warmwasser", "separat nötig", "inklusive möglich"],
        ["Wartung", "keine", "gering, regelmäßiger Service empfohlen"],
        ["Ideal für", "Zusatzheizung, Passivhaus, selten genutzte Räume", "Hauptheizung in fast allen Häusern"],
    ],
    hl_cols=(1, 2),
)}
<p>Der Kern des Vergleichs ist der <b>Faktor 3 bis 4 beim Strombedarf</b>: Für dieselbe Wärme braucht eine
Infrarotheizung drei- bis viermal so viel Strom wie eine Wärmepumpe. Das gilt auch mit PV-Anlage, denn jede
Kilowattstunde Sonnenstrom, die in Infrarot fließt, könnte in einer Wärmepumpe die drei- bis vierfache Wärme
erzeugen. Weniger geeignet ist Infrarot deshalb als alleinige Heizung in einem normal oder schlecht gedämmten
Einfamilienhaus. Dort sprechen Stromkosten und Förderlage klar für die
{a('waermepumpe', 'Wärmepumpe')}, idealerweise kombiniert mit Photovoltaik, siehe
{a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}.</p>
<p><small>*Richtwerte, Wärmepumpe mit Jahresarbeitszahl 3,5 bis 4 gerechnet.</small></p>
"""),
        ("Wann sich eine Infrarotheizung wirklich lohnt", "sinnvoll", f"""
<ul>
  <li><b>Badezimmer:</b> als Zusatzheizung, Spiegel- oder Handtuchheizung. Ein 600-Watt-Paneel, das in der
  Heizsaison zwei Stunden am Tag läuft, kostet rund 60 Euro Strom im Jahr.</li>
  <li><b>Selten genutzte Räume:</b> Gästezimmer, Hobbyraum, Atelier, die nur bei Bedarf geheizt werden.</li>
  <li><b>Übergangszeit:</b> Infrarot mit PV-Überschuss, statt die Zentralheizung früh im Herbst zu
  starten.</li>
  <li><b>Passivhaus und sehr gut gedämmter Neubau:</b> Mit 30 bis 40 Watt je Quadratmeter ist der
  Wärmebedarf so gering, dass die niedrigen Investitionskosten überwiegen können.</li>
  <li><b>Ferienhaus oder Nebenwohnsitz:</b> geringe Nutzungsdauer, kein wasserführendes Heizsystem, das
  einfrieren kann.</li>
</ul>
{A.cta("Infrarot, Wärmepumpe oder beides?",
       "Wir prüfen Ihr Haus, Ihre PV-Anlage und Ihren Verbrauch und rechnen ehrlich durch, wie Sie mit "
       "Sonnenstrom am günstigsten heizen.",
       secondary=("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"))}
"""),
        ("So holen Sie mehr Sonnenstrom in die Infrarotheizung", "steuerung", f"""
<ul>
  <li><b>Thermostat mit Zeitsteuerung:</b> Räume gezielt dann heizen, wenn sie genutzt werden, und in der
  Übergangszeit mittags vorwärmen.</li>
  <li><b>Batteriespeicher:</b> verschiebt Sonnenstrom vom Mittag in den Abend. Im tiefen Winter bleibt der
  Speicher aber oft leer, hier hilft er wenig. Mehr zum {a('batteriespeicher', 'Batteriespeicher')}.</li>
  <li><b>Energiemanagementsystem:</b> schaltet Verbraucher bei PV-Überschuss automatisch zu. Die
  {a('/ems-foerderung/', 'EMS-Förderung')} von bis zu 600 Euro gibt es nur, wenn das System mindestens zwei
  der Komponenten PV-Anlage, Speicher, Wärmepumpe beziehungsweise Warmwasserbereitung oder Ladestelle aktiv
  steuert. Infrarotpaneele allein zählen nicht dazu.</li>
  <li><b>Dynamischer Stromtarif:</b> Der Netzstrom im Winter wird günstiger, wenn Sie in Stunden mit
  niedrigen Börsenpreisen heizen, siehe {a('/dynamischer-stromtarif/', 'dynamischer Stromtarif')}.</li>
</ul>
"""),
        ("Förderung: Was es für Infrarot, PV und Wärmepumpe gibt", "foerderung", f"""
<p>Stand Oktober 2026 sieht die Förderlage für die drei Bausteine so aus:</p>
<ul>
  <li><b>Infrarotheizung:</b> Die Heizungstausch-Programme förderten 2026 den Umstieg auf Wärmepumpe,
  Nah- oder Fernwärme und Holzzentralheizung. Infrarot als Hauptheizung war nicht förderfähig, auch die
  Kärntner Pauschale für energieeffiziente Haustechnik nennt Infrarot nicht.</li>
  <li><b>Photovoltaik:</b> Der EAG-Bundeszuschuss für PV und Speicher ist für 2026 abgeschlossen, der letzte
  Call lief vom 8. bis 22. Oktober 2026. Ab 2027 ist laut BMWET eine Systemförderung für Speicher mit
  intelligenter Steuerung geplant, nicht beschlossen. Kärnten zahlt 3.000 Euro Pauschale für eine neue
  PV-Anlage ab 5 kWp mit neuem Speicher ab 5 kWh (Einreichung bis 31. Dezember 2026), siehe
  {a('foerderung_kaernten', 'Photovoltaik-Förderung Kärnten')}. Die Steiermark hat derzeit keine
  PV-Landesförderung.</li>
  <li><b>Wärmepumpe:</b> Die Bundesförderung 2026 ist ausgeschöpft, neue Registrierungen sind derzeit nicht
  möglich. Kärnten zahlt 3.000 Euro Pauschale, die Steiermark nimmt für neue Wärmepumpen derzeit keine
  Anträge an. Überblick: {a('/waermepumpenfoerderung-in-oesterreich/', 'Wärmepumpenförderung in Österreich')}.</li>
</ul>
"""),
        ("Fazit: Gute Ergänzung, selten die beste Hauptheizung", "fazit", f"""
<p>Eine Infrarotheizung ist günstig, wartungsfrei und angenehm, und mit Photovoltaik nutzt sie in der
Übergangszeit Sonnenstrom, der sonst für rund 10 Cent ins Netz ginge. Als alleinige Heizung eines normal
gedämmten Hauses ist sie aber teuer im Betrieb, weil Sonnenstrom im Winter knapp ist und jede Kilowattstunde
nur eine Kilowattstunde Wärme liefert. Unsere Empfehlung: Infrarot gezielt dort einsetzen, wo es seine
Stärken hat, und die Grundlast mit einer Wärmepumpe decken.</p>
{A.cta("Vor dem Winter richtig planen",
       "Wir beraten Sie zu Photovoltaik, Speicher und Wärmepumpe und zeigen, wie viel Sonnenstrom Ihr Haus "
       "tatsächlich zum Heizen nutzen kann.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Heizen mit Sonnenstrom: Beratung mit ehrlicher Rechnung",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie plant und installiert Photovoltaik, Batteriespeicher und Wärmepumpen in Kärnten "
                 "und der Steiermark, mit zertifizierten Fachkräften und einem festen Ansprechpartner von der "
                 "Planung bis zur Übergabe. Wir rechnen Anschaffung und Betriebskosten für Ihr Haus offen durch, "
                 "auch wenn am Ende eine kleine Lösung herauskommt."),
        "grid": [
            ("Ehrliche Rechnung", "Anschaffung und Betriebskosten im Vergleich."),
            ("PV und Wärmepumpe aus einer Hand", "Ein abgestimmtes System statt Einzelteile."),
            ("Smarte Steuerung", "PV-Überschuss automatisch in Wärme umwandeln."),
            ("Förderung im Blick", "Land, Bund und EMS-Förderung zum richtigen Zeitpunkt."),
        ],
    },

    "faq": [
        ("Lohnt sich eine Infrarotheizung mit Photovoltaik?",
         "Als Ergänzung ja, als alleinige Hauptheizung selten. Die PV-Anlage liefert im Dezember und Jänner nur "
         "wenige Prozent ihres Jahresertrags, deshalb kommt ein Großteil des Heizstroms auch mit PV aus dem "
         "Netz. Sinnvoll ist Infrarot mit PV vor allem für Bad, Übergangszeit, selten genutzte Räume und sehr "
         "gut gedämmte Häuser."),
        ("Wie viel Strom verbraucht eine Infrarotheizung?",
         "Eine Infrarotheizung wandelt eine Kilowattstunde Strom in eine Kilowattstunde Wärme um. Im gut "
         "gedämmten Neubau mit 100 Quadratmetern sind 5.000 bis 7.000 Kilowattstunden pro Jahr realistisch, im "
         "Altbau deutlich mehr. Eine Wärmepumpe braucht für dieselbe Wärme etwa ein Drittel bis ein Viertel "
         "des Stroms."),
        ("Was kostet eine Infrarotheizung?",
         "Einzelne Paneele kosten meist 200 bis 700 Euro, grob 50 bis 90 Euro je 100 Watt. Für ein ganzes "
         "Einfamilienhaus liegen die Anschaffungskosten bei rund 4.000 bis 7.000 Euro inklusive "
         "Elektroinstallation. Dafür sind die laufenden Stromkosten mit 1.400 bis 1.960 Euro pro Jahr im "
         "100-m²-Neubau deutlich höher als bei einer Wärmepumpe."),
        ("Wird eine Infrarotheizung in Österreich gefördert?",
         "Als Hauptheizung nein. Die Heizungstausch-Programme förderten 2026 nur den Umstieg auf Wärmepumpe, "
         "Nah- oder Fernwärme und Holzzentralheizung. Für die PV-Anlage zahlt Kärnten 3.000 Euro Pauschale, wenn "
         "gleichzeitig ein Speicher ab 5 kWh errichtet wird; der EAG-Bundeszuschuss ist für 2026 abgeschlossen."),
        ("Wie viel Watt Infrarotheizung brauche ich pro Quadratmeter?",
         "Als Richtwert: im Passivhaus 30 bis 40 Watt, im gut gedämmten Neubau 40 bis 60 Watt, im "
         "durchschnittlichen Bestand 60 bis 80 Watt und im unsanierten Altbau 80 bis 100 Watt je "
         "Quadratmeter. Die genaue Auslegung hängt von Raumhöhe, Fenstern und Dämmung ab."),
        ("Ist eine Infrarotheizung im Badezimmer sinnvoll?",
         "Ja, das ist einer der besten Einsatzbereiche. Ein Paneel mit 600 Watt, das in der Heizsaison zwei "
         "Stunden am Tag läuft, braucht rund 220 Kilowattstunden und kostet damit rund 60 Euro Strom im Jahr. "
         "Als Spiegel- oder Handtuchheizung ist es zusätzlich praktisch."),
        ("Kann ich statt Wärmepumpe nur Infrarot und PV nehmen?",
         "Im Passivhaus oder sehr gut gedämmten Neubau kann das funktionieren und spart hohe "
         "Investitionskosten. In normal gedämmten Häusern steigen die Stromkosten im Winter aber stark, weil die "
         "PV-Anlage dann wenig liefert und Infrarot drei- bis viermal so viel Strom braucht wie eine "
         "Wärmepumpe. Wir rechnen beide Varianten für Ihr Haus durch."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Mit zertifizierten Fachkräften plant und "
                    "installiert EBZ Energie Photovoltaik, Batteriespeicher und Wärmepumpen in Kärnten und der "
                    "Steiermark. Verbrauchs- und Kostenwerte in diesem Ratgeber sind Richtwerte und werden "
                    "anhand realer Projekte überprüft. Keine Rechts- oder Steuerberatung, maßgeblich sind die "
                    "offiziellen Förderbedingungen der jeweiligen Stelle."),
    "sources": [
        ("pieno.at: Infrarotheizung in Österreich, Stromverbrauch und Kosten 2026",
         "https://pieno.at/infrarotheizung-stromverbrauch-kosten-oesterreich/"),
        ("Sanierungsoffensive des Bundes", "https://www.sanierungsoffensive.gv.at/"),
        ("OeMAG Abwicklungsstelle für Ökostrom", "https://www.oem-ag.at/"),
    ],
    "related": [
        ("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"),
        ("waermepumpe", "Wärmepumpen-Installateur in Kärnten und Steiermark"),
        ("/luftwaermepumpe-preise/", "Luftwärmepumpe: Preise und Betriebskosten"),
        ("ems", "Energiemanagementsystem: PV-Überschuss automatisch nutzen"),
    ],
    "cta": {
        "h3": "Mit Sonnenstrom heizen, aber richtig",
        "text": "Wir rechnen PV, Speicher und Wärmepumpe für Ihr Haus ehrlich durch.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Heizen mit Sonnenstrom, ehrlich gerechnet",
    "final_text": ("Kostenlose Erstberatung zu Photovoltaik, Speicher und Wärmepumpe, mit transparenten Zahlen und "
                   "einem Ansprechpartner aus Villach."),
}
