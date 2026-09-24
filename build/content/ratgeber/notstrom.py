"""Ratgeber: Notstrom mit Photovoltaik (Notstrom vs. Ersatzstrom, Komponenten, Nachrüstung, Kosten, Ablauf).

Zusammengeführt aus zwei stark überlappenden Live-Artikeln:
ebz-photovoltaik.at/notstrom/ und ebz-photovoltaik.at/pv-anlage-mit-notstrom-nachruesten/
(beide Stand November 2025). Ein Artikel mit klarer Struktur, Referenzprojekte von EBZ ergänzt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "notstrom",
    "path": "/notstrom/",
    "title": "Notstrom mit Photovoltaik: Ersatzstrom und Nachrüstung | EBZ",
    "description": ("Notstrom mit Photovoltaik: Warum PV-Anlagen bei Stromausfall abschalten, Notstrom vs. "
                    "Ersatzstrom, 3 Pflichtkomponenten, Nachrüstung in 1 bis 3 Tagen."),
    "eyebrow": "Speicher · Notstrom",
    "crumb_label": "Notstrom mit Photovoltaik",
    "h1": "Notstrom mit Photovoltaik: So bleibt Ihr Haus bei Stromausfall versorgt",
    "lead": ("Eine normale PV-Anlage schaltet bei Netzausfall ab, auch bei Sonnenschein. Erst ein notstromfähiger "
             "Hybridwechselrichter, ein Speicher und eine Umschalteinrichtung machen aus Ihrer Anlage eine "
             "Notstromversorgung. Dieser Ratgeber erklärt die Technik, den Unterschied zwischen Notstrom und "
             "Ersatzstrom und die Nachrüstung im Bestand."),
    "chips": [
        "Standard-PV: <b>schaltet ab</b> bei Netzausfall",
        "<b>3 Komponenten</b> für Notstrom",
        "10 kWh Speicher: <b>rund 20 h</b> bei 500 W",
        "Nachrüstung: <b>1 bis 3 Tage</b> vor Ort",
    ],
    "date_published": "2025-09-15",
    "date_modified": "2026-09-24",
    "hero_img": "gen_detail",
    "hero_alt": "Montage eines notstromfähigen Hybridwechselrichters mit Batteriespeicher im Technikraum",

    "tldr": [
        "Netzgekoppelte PV-Anlagen schalten bei Stromausfall aus Sicherheitsgründen ab, weil der Wechselrichter "
        "das Netz als Taktgeber braucht und kein Strom in ein abgeschaltetes Netz fließen darf.",
        "Notstrom braucht drei Komponenten: einen notstromfähigen Hybridwechselrichter (baut ein eigenes Inselnetz "
        "mit 50 Hertz auf), einen Batteriespeicher und eine Umschalteinrichtung, die das Haus allpolig vom Netz trennt.",
        "Notstrom versorgt eine einzelne abgesicherte Steckdose aus dem Speicher. Ersatzstrom versorgt ganze "
        "Stromkreise oder das ganze Haus automatisch, und die PV-Anlage lädt den Speicher bei Sonne weiter nach.",
        "Reichweite: Ein 10-kWh-Speicher deckt eine Dauerlast von 500 Watt rund 20 Stunden. Mit Nachladung durch "
        "die PV-Anlage lassen sich auch mehrtägige Ausfälle überbrücken.",
        "Nachrüstung im Bestand ist meist möglich: Wechselrichtertausch oder AC-gekoppelter Batteriewechselrichter, "
        "Speicher und Umschalteinrichtung. Die Montage vor Ort dauert 1 bis 3 Tage, der Gesamtprozess mehrere Wochen.",
    ],
    "kpis": [
        ("3", "Pflichtkomponenten: Hybridwechselrichter, Speicher, Umschalteinrichtung"),
        ("50 Hz", "Netzfrequenz, die der Wechselrichter im Inselbetrieb selbst erzeugt"),
        ("rund 20 h", "Reichweite eines 10-kWh-Speichers bei 500 W Dauerlast"),
        ("1 bis 3 Tage", "Montagezeit für die Notstrom-Nachrüstung vor Ort"),
    ],

    "sections": [
        ("Warum eine normale PV-Anlage bei Stromausfall abschaltet", "warum-abschaltung", f"""
<p>Die Annahme, dass die eigene Photovoltaikanlage bei einem Stromausfall einfach weiterläuft, ist weit
verbreitet und leider falsch. Ein netzgekoppelter Wechselrichter braucht das öffentliche Netz als Taktgeber
für Frequenz und Spannung. Fällt dieses Signal weg, stoppt er sofort die Einspeisung. Diese Abschaltung ist
vorgeschrieben: Sie verhindert, dass Strom in ein vermeintlich spannungsfreies Netz fließt und dort
Monteure gefährdet, die die Störung beheben.</p>
<p>Ein längerer Ausfall trifft den Haushalt an mehreren Stellen gleichzeitig: Kühlschrank und Gefriertruhe,
die Heizungspumpe im Winter, Internet und Telefon, gegebenenfalls medizinische Geräte. Genau hier setzt eine
Notstromlösung an. Sie trennt das Haus sicher vom Netz und baut ein eigenes, stabiles Inselnetz auf, in dem
Speicher und PV-Anlage die wichtigsten Verbraucher weiter versorgen.</p>
{A.box("Auch ein Speicher allein hilft nicht: Ohne notstromfähigen Wechselrichter und Umschalteinrichtung "
       "bleibt der Speicher bei Netzausfall genauso stumm wie die Module auf dem Dach.")}
"""),
        ("Notstrom oder Ersatzstrom: der Unterschied entscheidet über Komfort und Kosten", "notstrom-vs-ersatzstrom", f"""
<p>Die beiden Begriffe werden oft synonym verwendet, beschreiben aber zwei verschiedene Versorgungsstufen.
Die Wahl bestimmt, welche Geräte im Ernstfall laufen, ob die PV-Anlage weiter produziert und wie viel die
Lösung kostet.</p>
{A.table(
    ["Kriterium", "Notstrom (Basis)", "Ersatzstrom (Vollversorgung)"],
    [
        ["Versorgte Verbraucher", "eine einzelne abgesicherte Steckdose beim Wechselrichter", "ganze Stromkreise oder das gesamte Haus"],
        ["Umschaltung", "manuell: Geräte werden angesteckt", "automatisch, innerhalb von Millisekunden bis wenigen Sekunden"],
        ["Phasen", "einphasig", "einphasig oder dreiphasig (Wärmepumpe, E-Herd möglich)"],
        ["PV lädt Speicher nach", "meist nein, nur Energie aus dem Speicher", "ja, bei Sonne wird der Speicher weiter geladen"],
        ["Überbrückbare Dauer", "Stunden, begrenzt durch Speicherinhalt", "mehrere Tage möglich"],
        ["Aufwand und Kosten", "geringer", "höher: Umschalteinrichtung, leistungsfähigere Komponenten"],
    ],
    hl_cols=(2,),
)}
<p><b>Notstrom</b> ist die einfache Variante: eine speziell abgesicherte Steckdose in der Nähe von Wechselrichter
oder Speicher, an die Sie bei Netzausfall Kühlschrank, Router oder eine Lampe anschließen. Der Rest des Hauses
bleibt stromlos, und die PV-Anlage kann den Speicher in dieser Betriebsart meist nicht nachladen.</p>
<p><b>Ersatzstrom</b> versorgt automatisch ganze Stromkreise oder das ganze Haus. Das System trennt sich vom
Netz, der Wechselrichter baut ein eigenes Inselnetz auf, und der Strom kommt wie gewohnt aus jeder Steckdose.
Der entscheidende Vorteil: Bei Sonnenschein produziert die Anlage weiter und lädt den Speicher nach. Damit
lassen sich auch Ausfälle über mehrere Tage überbrücken.</p>
"""),
        ("Die Technik: drei Komponenten müssen zusammenspielen", "komponenten", f"""
<p>Eine Standardanlage ist für den Netzparallelbetrieb gebaut. Eine Notstromanlage muss im Ernstfall die Rolle
des gesamten öffentlichen Netzes für Ihr Haus übernehmen. Dafür braucht es ein abgestimmtes System:</p>
{A.net([
    ("☀", "PV-Module", "liefern bei Sonne Energie ins Inselnetz und laden den Speicher nach (Ersatzstrom)"),
    ("▮", "Batteriespeicher", "Energiereservoir für Nacht und trübe Tage, oft mit reservierter Notstromkapazität"),
    ("⌖", "Umschalteinrichtung", "trennt das Haus allpolig vom Netz, bevor das Inselnetz aufgebaut wird"),
    ("⌂", "Kritische Verbraucher", "Kühlgeräte, Heizungspumpe, Router, Licht, Ladegeräte"),
], "Notstromfähiger Hybridwechselrichter",
   "Erkennt den Netzausfall, erzeugt selbst 50 Hertz und eine stabile Spannung (Schwarzstartfähigkeit) und "
   "steuert den Energiefluss zwischen Modulen, Speicher und Verbrauchern.")}
<h3>Der notstromfähige Wechselrichter</h3>
<p>Im Gegensatz zum Standardgerät kann ein notstromfähiger Hybridwechselrichter ohne externes Netzsignal
starten und ein eigenes Hausnetz aufbauen. Entscheidend bei der Auswahl: einphasig oder dreiphasig. Einphasige
Systeme versorgen ausgewählte kleinere Verbraucher auf einer Phase. Dreiphasige Systeme können auch Wärmepumpe
oder E-Herd betreiben und das ganze Haus abdecken.</p>
<h3>Der Speicher</h3>
<p>Ohne Speicher gibt es keinen Notstrom, sobald die Sonne nicht scheint. Die nutzbare Kapazität in kWh
bestimmt die Überbrückungsdauer. Viele Systeme reservieren einen Teil der Kapazität ausschließlich für den
Notfall; diese Reserve wird im Alltag nicht angetastet. Zur Auslegung von Speichern siehe
{a('batteriespeicher', 'Batteriespeicher')} und {a('/pv-speicher-nachruesten/', 'PV-Speicher nachrüsten')}.</p>
<h3>Die Umschalteinrichtung</h3>
<p>Die „Backup-Box“ oder Netztrennstelle trennt das Haus physisch und allpolig vom Netz. Das ist
vorgeschrieben, damit kein Notstrom ins öffentliche Netz zurückfließt. Erst nach dieser Trennung darf der
Wechselrichter das Inselnetz aufbauen. Bei einfachen Systemen erfolgt die Umschaltung manuell, bei
hochwertigen automatisch innerhalb von Millisekunden bis wenigen Sekunden. Sie bemerken den Ausfall dann
oft nur an einem kurzen Flackern.</p>
"""),
        ("Notstrom nachrüsten: Voraussetzungen im Bestand", "nachruesten", f"""
<p>Die meisten bestehenden PV-Anlagen lassen sich mit Notstrom nachrüsten. Es reicht aber nicht, einen
Speicher dazuzustellen. Das System muss neu gedacht werden, damit es im Ernstfall sicher vom Netz trennt und
ein stabiles Inselnetz erzeugt. Zwei technische Wege stehen zur Wahl:</p>
<ul>
  <li><b>Wechselrichtertausch (DC-Kopplung):</b> Der alte Wechselrichter wird durch einen notstromfähigen
  Hybridwechselrichter ersetzt, der die Module direkt anbindet und den Speicher mit Gleichstrom lädt. Die
  effizienteste Lösung und bei älteren Wechselrichtern meist die sinnvollste.</li>
  <li><b>AC-gekoppelter Batteriewechselrichter:</b> Der bestehende PV-Wechselrichter bleibt, ein notstromfähiger
  Batteriewechselrichter mit Speicher kommt parallel dazu und übernimmt im Inselbetrieb die Netzbildung. Weniger
  Eingriff, dafür müssen beide Geräte im Inselbetrieb zusammenarbeiten können.</li>
</ul>
<p>In beiden Fällen kommen Speicher und Umschalteinrichtung dazu. Ein Fachbetrieb prüft vorab die
Kompatibilität von Modulen, Verkabelung und Hauselektrik.</p>
{A.steps([
    ("Bestandsaufnahme und Kompatibilitätsprüfung",
     "Module, Verkabelung und Wechselrichter werden geprüft. Daraus ergibt sich, ob AC- oder DC-Kopplung passt."),
    ("Bedarfsanalyse und Dimensionierung",
     "Welche Verbraucher müssen laufen (Notstrom oder Ersatzstrom)? Daraus werden Wechselrichterleistung und "
     "Speicherkapazität berechnet."),
    ("Komponentenauswahl",
     "Hybridwechselrichter, Speicher und Umschalteinrichtung werden aufeinander abgestimmt ausgewählt."),
    ("Installation und Umbau",
     "Wechselrichtertausch, Speichermontage und Einbau der Netztrennstelle durch zertifizierte Fachkräfte, "
     "nach den geltenden Normen. Vor Ort meist in 1 bis 3 Tagen erledigt."),
    ("Inbetriebnahme mit Testlauf",
     "Ein simulierter Netzausfall prüft die Umschaltung und die Versorgung. Danach erhalten Sie eine Einweisung."),
])}
{A.cta("Notstrom für Ihre Anlage planen lassen",
       "Wir prüfen Ihre Bestandsanlage, legen Notstrom- und Ersatzstromvariante mit Preis nebeneinander und "
       "übernehmen Umbau und Anmeldung.",
       secondary=("batteriespeicher", "Zum Batteriespeicher"))}
"""),
        ("Planung: sechs Fragen vor der Entscheidung", "planung", f"""
<p>Eine Notstromversorgung ist kein Produkt von der Stange. Unzureichende Planung führt dazu, dass der
Speicher zu schnell leer ist, der Wechselrichter überlastet wird oder wichtige Geräte gar nicht versorgt
werden. Diese Punkte klären wir gemeinsam mit Ihnen:</p>
<ul>
  <li><b>Welche Verbraucher müssen laufen?</b> Kühlschrank, Gefriertruhe, Heizungspumpe, Router, Licht,
  Ladegeräte, medizinische Geräte. Große Verbraucher wie E-Herd oder Waschmaschine sind nur mit
  Ersatzstrom sinnvoll.</li>
  <li><b>Wie viel Leistung (kW) brauchen sie gleichzeitig?</b> Die Summe bestimmt die Mindestleistung des
  Wechselrichters im Inselbetrieb, damit keine Sicherung fällt.</li>
  <li><b>Wie lange soll überbrückt werden?</b> Stündlicher Verbrauch der kritischen Geräte mal gewünschte
  Stunden, plus Puffer, ergibt die nötige Speicherkapazität. Beispiel: 500 Watt Dauerlast über 20 Stunden
  entsprechen 10 kWh.</li>
  <li><b>Einphasig oder dreiphasig?</b> Einige Geräte an einer Steckdose (Notstrom) oder das ganze Haus
  inklusive Wärmepumpe (Ersatzstrom)?</li>
  <li><b>Soll die PV-Anlage nachladen?</b> Typisch für Ersatzstromsysteme; verlängert die Autarkie erheblich.</li>
  <li><b>Wo ist Platz?</b> Speicher und Backup-Box brauchen einen trockenen, belüfteten, zugänglichen Ort.</li>
</ul>
{A.box_dark("Der häufigste Planungsfehler",
    "Die Speichergröße wird nach dem Jahresverbrauch gewählt, die Wechselrichterleistung aber nicht nach der "
    "gleichzeitigen Last im Notfall. Wenn Heizungspumpe, Kühlgeräte und Wärmepumpe gleichzeitig anlaufen, "
    "entscheidet die Leistung des Wechselrichters, nicht die Kapazität des Speichers.")}
"""),
        ("Kosten und Beispiele aus der Praxis", "kosten", f"""
<p>Die größten Kostenpositionen sind der notstromfähige Hybridwechselrichter und der Speicher, dazu kommen
Umschalteinrichtung und Montage. Für den Speicher gilt als Richtwert 800 bis 1.200 Euro je Kilowattstunde
inklusive Installation*. Eine Ersatzstromlösung für das ganze Haus liegt über einer einfachen
Notstromsteckdose, weil Umschalteinrichtung und leistungsfähigere Komponenten dazukommen. Bei einer
Neuanlage ist die Notstromfunktion am günstigsten mitzuplanen: Eine komplette 10-kWp-Anlage mit Speicher liegt
bei EBZ Energie bei rund 15.000 bis 22.000 Euro vor Förderung, siehe
{a('/kosten-einer-solaranlage/', 'Kosten einer Solaranlage')}. Der Speicheranteil wird vom Bund mit
150 Euro je kWh gefördert, in Kärnten kommt die Landespauschale dazu, siehe
{a('/foerderung-fuer-pv-speicher/', 'Förderung für PV-Speicher')}.</p>
<h3>Zwei Referenzprojekte mit Notstrom</h3>
{A.table(
    ["Projekt", "Anlage", "Ergebnis"],
    [
        ["Einfamilienhaus Villach", "10 kWp Ost-West mit Speicher und Notstromfunktion", "rund 11.000 kWh Jahresertrag, rund 80 % weniger Stromkosten"],
        ["Mehrfamilienhaus Krumpendorf", "25 kWp mit 25 kWh Speicher und Notstrom", "4 Tage Bauzeit, Versorgung mehrerer Wohneinheiten bei Netzausfall"],
    ],
    hl_cols=(2,),
)}
<p>Weitere Projekte mit Zahlen finden Sie unter {a('referenzen', 'Referenzen')}.</p>
<p><small>*Richtwerte für marktübliche Lithium-Ionen-Systeme, Stand Juli 2025. Der tatsächliche Preis hängt von
Hersteller, Kapazität, Kopplungsart und Umfang der Ersatzstromlösung ab.</small></p>
"""),
        ("Fazit: Notstrom ist Planungssache, nicht Zubehör", "fazit", f"""
<p>Eine Photovoltaikanlage mit Notstromfunktion macht aus einem reinen Stromerzeuger eine Absicherung für den
Haushalt. Der Schlüssel liegt im Zusammenspiel von notstromfähigem Hybridwechselrichter, richtig
dimensioniertem Speicher und sicherer Umschalteinrichtung. Ob eine Notstromsteckdose reicht oder das ganze
Haus mit Ersatzstrom versorgt werden soll, entscheidet über Aufwand und Kosten. Beides lässt sich im Bestand
nachrüsten, am günstigsten ist die Funktion aber, wenn sie bei einer Neuanlage von Anfang an mitgeplant wird.</p>
{A.cta("Sicher versorgt, auch wenn das Netz ausfällt",
       "Kostenlose Erstberatung, Analyse Ihrer kritischen Verbraucher und ein Festpreisangebot für Notstrom "
       "oder Ersatzstrom in Kärnten und der Steiermark.",
       primary=("kontakt", "Jetzt Kontakt aufnehmen"), secondary=("photovoltaik", "Zur Photovoltaik"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik mit Notstrom: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher und Notstromlösungen in "
                 "Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften und "
                 "über 300 dokumentierten Projekten. Wir übernehmen Bedarfsanalyse, Komponentenauswahl, Umbau, "
                 "Anmeldung beim Netzbetreiber und den Testlauf mit simuliertem Netzausfall."),
        "grid": [
            ("Notstrom und Ersatzstrom", "Von der Notstromsteckdose bis zur dreiphasigen Vollversorgung."),
            ("Auch für Bestandsanlagen", "Wechselrichtertausch oder AC-Nachrüstung, herstellerübergreifend."),
            ("Abnahme mit Testlauf", "Simulierter Netzausfall vor Übergabe, Einweisung inklusive."),
            ("Förderung inklusive", "EAG-Bund und Landesförderung Kärnten oder Steiermark für den Speicheranteil."),
        ],
    },

    "faq": [
        ("Schaltet sich jede PV-Anlage bei Stromausfall ab?",
         "Ja, jede netzgekoppelte Standardanlage schaltet bei Netzausfall aus Sicherheitsgründen ab. Für Strom "
         "bei Netzausfall braucht es einen notstromfähigen Hybridwechselrichter, einen Speicher und eine "
         "Umschalteinrichtung, die das Haus vom Netz trennt und ein eigenes Inselnetz aufbaut."),
        ("Was ist der Unterschied zwischen Notstrom und Ersatzstrom?",
         "Notstrom versorgt wenige ausgewählte Geräte über eine separate Steckdose, der Strom kommt nur aus dem "
         "Speicher. Ersatzstrom versorgt automatisch ganze Stromkreise oder das gesamte Haus, und die PV-Anlage "
         "lädt den Speicher bei Sonne weiter nach, was mehrtägige Ausfälle überbrückbar macht."),
        ("Welche Geräte kann ich mit Notstrom betreiben?",
         "Typisch sind Verbraucher mit geringer Leistung: Kühlschrank, Gefriertruhe, Heizungspumpe, Licht, "
         "Router und Ladegeräte. E-Herd, Waschmaschine oder Wärmepumpe brauchen eine leistungsstarke, meist "
         "dreiphasige Ersatzstromanlage."),
        ("Wie lange reicht der Notstrom aus dem Speicher?",
         "Das hängt von nutzbarer Kapazität und Last ab. Ein 10-kWh-Speicher deckt 500 Watt Dauerlast rund "
         "20 Stunden. Bei einer Ersatzstromlösung verlängert die Nachladung durch die PV-Anlage die Dauer bei "
         "Sonnenschein deutlich."),
        ("Kann ich Notstrom bei meiner bestehenden Anlage nachrüsten?",
         "In den meisten Fällen ja. Entweder wird der Wechselrichter gegen ein notstromfähiges Hybridmodell "
         "getauscht oder ein notstromfähiger Batteriewechselrichter AC-seitig ergänzt. Dazu kommen Speicher und "
         "Umschalteinrichtung. Ein Fachbetrieb prüft vorab die Kompatibilität mit Modulen und Hauselektrik."),
        ("Kann die PV-Anlage den Speicher während des Stromausfalls nachladen?",
         "Bei einer einfachen Notstromsteckdose meist nicht. Bei einer Ersatzstromlösung baut der Wechselrichter "
         "ein eigenes Inselnetz auf, in dem die Module bei Sonnenschein weiter produzieren und den Speicher für "
         "die Nacht laden."),
        ("Wie lange dauert die Nachrüstung?",
         "Die Montage vor Ort ist meist in 1 bis 3 Tagen erledigt: Wechselrichtertausch, Speichermontage und "
         "Anpassung der Hauselektrik. Beratung, Planung, Kompatibilitätsprüfung und Lieferung der Komponenten "
         "nehmen davor mehrere Wochen in Anspruch."),
        ("Was kostet eine Notstromlösung?",
         "Die Hauptposten sind Hybridwechselrichter und Speicher (Richtwert 800 bis 1.200 Euro je kWh inklusive "
         "Installation), dazu Umschalteinrichtung und Montage. Eine Ersatzstromversorgung für das ganze Haus kostet "
         "mehr als eine Notstromsteckdose. Am günstigsten ist die Funktion, wenn sie bei einer Neuanlage von "
         "Anfang an mitgeplant wird."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team hat über 300 PV-Projekte in sechs "
                    "Bundesländern umgesetzt, darunter Notstrom- und Ersatzstromanlagen für Einfamilienhäuser, "
                    "Mehrfamilienhäuser und Betriebe. Jede Notstromanlage von EBZ wird vor Übergabe mit einem "
                    "simulierten Netzausfall getestet."),
    "sources": [],
    "related": [
        ("batteriespeicher", "Batteriespeicher: Technik und Auslegung"),
        ("/pv-speicher-nachruesten/", "PV-Speicher nachrüsten"),
        ("/ab-wann-lohnt-sich-photovoltaik-mit-speicher/", "Ab wann lohnt sich PV mit Speicher?"),
        ("referenzen", "Referenzprojekte mit Notstrom"),
    ],
    "cta": {
        "h3": "Notstrom für Ihr Haus",
        "text": "Wir sagen Ihnen, ob Notstromsteckdose oder Ersatzstrom für das ganze Haus bei Ihnen sinnvoll ist.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Versorgt, wenn es darauf ankommt",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
