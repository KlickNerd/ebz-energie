"""Ratgeber: Balkonkraftwerk mit Speicher in Österreich (Wirtschaftlichkeit, 800-Watt-Regel, AC/DC, Kosten, Sicherheit).

Neuer Artikel auf der alten WordPress-URL /balkonkraftwerk-mit-speicher/ (bisher 301 auf /balkonkraftwerke/),
erstellt 2026-11-19. Die Leistungsseite /balkonkraftwerke/ bleibt die Angebotsseite (Montage, Meldung, Ablauf);
dieser Ratgeber beantwortet die Informationsfragen rund um den Speicher und verlinkt dorthin.
Ziel-Keywords (Google Ads, Österreich, 19.11.2026): balkonkraftwerk mit speicher 8.100,
balkonkraftwerk mit speicher österreich 1.600, balkonkraftwerk speicher 880, speicher für balkonkraftwerk 720,
balkonkraftwerk 2000 watt mit speicher österreich 260, speicher für balkonkraftwerk nachrüsten 140,
balkonkraftwerk 2000 watt mit speicher 140, balkonkraftwerk speicher nachrüsten 110.

Faktenbasis (alle Quellen am 19.11.2026 geöffnet): ElWG-Definition und Speicher-Auslegung laut Leitfaden Energie
Klagenfurt (15.07.2026), AC-Summenregel laut Meldeformular Bad Gleichenberger Energie (05/2026), Meldung zwei Wochen
und Wohnungseigentum laut oesterreich.gv.at (Stand 01.10.2026) und WKO, keine Vergütung und Schutzkontaktstecker laut
Wiener Netze, E-Control-FAQ Kleinsterzeugungsanlagen, klimaaktiv (Balkon-PV, Speicher-Beispiel 0,8 kWp + 2,2 kWh,
Praxisbeispiel Wien 800 € + 400 €), Verbraucherzentrale Niedersachsen und Stiftung Warentest (deutsche Quellen),
RWTH Aachen via pv magazine (Heimspeicher), E-Control-Preismonitor November 2026 und OeMAG Oktober 2026 (aus
der Warmwasser-Recherche), Kärnten-Pauschale laut 5min.at (03.10.2026).
Eigene Rechnung: Mehr-Eigenverbrauch = Jahresertrag x (70 % minus 50 %), bewertet mit 25 bis 30 ct je kWh.
Nicht behauptet: konkrete Speicherpreise von EBZ, Wirkungsgrade in Prozent, Brandstatistik für Balkonspeicher,
Förderung für Balkonspeicher in Kärnten oder Steiermark.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "balkonkraftwerk-mit-speicher",
    "path": "/balkonkraftwerk-mit-speicher/",
    "cluster": "Speicher und Notstrom",
    "title": "Balkonkraftwerk mit Speicher Österreich: Rechnung 2026 | EBZ",
    "description": ("Balkonkraftwerk mit Speicher in Österreich: Ein 2-kWh-Akku bringt rund 120 bis 160 kWh mehr "
                    "Eigenverbrauch im Jahr. Rechnung, 800-Watt-Regel, AC/DC, Kosten."),
    "eyebrow": "Balkonkraftwerk · Speicher",
    "crumb_label": "Balkonkraftwerk mit Speicher",
    "h1": "Balkonkraftwerk mit Speicher in Österreich: Rechnung, 800-Watt-Regel und Alternativen 2026",
    "lead": ("Ein Speicher hebt den Sonnenstrom vom Balkon für den Abend auf, denn was ein Balkonkraftwerk ins Netz "
             "schickt, wird in Österreich nicht vergütet. Ob sich der Akku rechnet und welche Speicher unter die "
             "800-Watt-Grenze fallen, rechnen wir hier mit offiziellen Quellen durch."),
    "chips": [
        "Grenze laut ElWG: <b>höchstens 800 W</b>",
        "Meldung: <b>2 Wochen</b> vor Inbetriebnahme",
        "Eigenverbrauch mit Speicher: <b>rund 70 %</b>",
        "Überschuss ins Netz: <b>keine Vergütung</b>",
    ],
    "date_published": "2026-11-19",
    "date_modified": "2026-11-19",
    "hero_img": "balkon",
    "hero_alt": "Vier Solarmodule eines Balkonkraftwerks am Balkongeländer eines Wohnhauses",

    "tldr": [
        "Ein Speicher am Balkonkraftwerk hebt den Eigenverbrauch laut klimaaktiv von etwa der Hälfte auf rund 70 %. "
        "Bei 600 bis 800 kWh Jahresertrag sind das rund 120 bis 160 kWh mehr selbst genutzter Strom.*",
        "Das spart rund 30 bis 48 Euro im Jahr.* Ein Speicher um 500 bis 1.000 Euro braucht damit 10 bis 33 Jahre, "
        "bis er sich allein bezahlt hat. Er lohnt sich eher mit mehr Modulleistung und hohem Abendverbrauch.",
        "In Österreich zählt die Bemessungsleistung an der Steckdose: höchstens 800 Watt laut ElWG. Ein AC-Speicher "
        "mit eigenem Wechselrichter wird bei manchen Netzbetreibern zur Leistung des Balkonkraftwerks addiert.",
        "Speicher mit mehr als 800 Watt, die nur per Software begrenzt sind, akzeptiert etwa Energie Klagenfurt nicht "
        "als Kleinsterzeugungsanlage. Vor dem Kauf das Datenblatt prüfen.",
        "Wer mehr will: Eine kleine Dachanlage ab 5 kWp mit Speicher ab 5 kWh fördert Kärnten mit 3.000 Euro, "
        "Überschuss wird dort vergütet.",
    ],
    "kpis": [
        ("800 W", "höchstens, Bemessungsleistung laut ElWG"),
        ("rund 70 %", "Eigenverbrauch mit 2,2-kWh-Speicher (klimaaktiv)"),
        ("700 bis 1.000 €", "Balkonspeicher im Test (Deutschland)"),
        ("0 ct", "Vergütung für Überschuss ohne Zählpunkt"),
    ],

    "sections": [
        ("Balkonkraftwerk mit Speicher: so funktioniert es", "funktion", f"""
<p><b>Ein Balkonkraftwerk mit Speicher ist eine steckerfertige Mini-PV-Anlage, deren Batterie den Strom aufnimmt,
den die Wohnung gerade nicht braucht, und ihn später abgibt.</b> In Österreich gilt sie als
Kleinsterzeugungsanlage, wenn die Bemessungsleistung an der Übergabestelle höchstens 800 Watt beträgt
(§ 6 Abs. 1 Z 78 ElWG). Die Modulleistung und die Speicherkapazität in kWh sind dafür nicht entscheidend.</p>
<p>Ohne Speicher läuft der Strom vom Balkon sofort in die Geräte, die gerade eingeschaltet sind: Kühlschrank,
Router, Waschmaschine. Was übrig bleibt, fließt ins öffentliche Netz. Für Anlagen bis 800 Watt gibt es keinen
Abnahmevertrag, eingespeiste Energie wird nicht vergütet (Wiener Netze, klimaaktiv). Der Speicher fängt diesen
Überschuss ab und gibt ihn am Abend wieder ins Hausnetz, wenn Herd, Licht und Fernseher laufen.</p>
<p>Wie Montage, Anmeldung und Ablauf bei uns funktionieren, steht auf der Seite
{a('balkonkraftwerke', 'Balkonkraftwerk mit Speicher: Montage in Kärnten und der Steiermark')}. Dieser Ratgeber
klärt die Frage davor: Bringt der Speicher genug, und welcher ist in Österreich zulässig?</p>
"""),
        ("Lohnt sich ein Speicher am Balkonkraftwerk? Die Rechnung", "rechnung", f"""
<p><b>Ein Speicher bringt so viel, wie er an Strom vom Mittag in den Abend verschiebt.</b> Klimaaktiv nennt ein
Beispiel aus 2025: Ein Balkonkraftwerk mit 0,8 kWp und einem DC-gekoppelten 2,2-kWh-Speicher hob den
Eigenverbrauch von etwa der Hälfte auf rund 70 %. Der Speicher kostete rund 500 Euro, die erwartete
Amortisation lag bei etwa zehn Jahren. Daraus ergibt sich diese Rechnung:</p>
{A.table(
    ["", "600 kWh Jahresertrag*", "800 kWh Jahresertrag*"],
    [
        ["Selbst genutzt ohne Speicher (rund 50 %)", "300 kWh", "400 kWh"],
        ["Selbst genutzt mit Speicher (rund 70 %)", "420 kWh", "560 kWh"],
        ["Mehr Eigenverbrauch durch den Speicher", "120 kWh", "160 kWh"],
        ["Mehr Ersparnis bei 25 bis 30 ct je kWh", "30 bis 36 € im Jahr", "40 bis 48 € im Jahr"],
        ["Speicher um 500 bis 1.000 € bezahlt sich ab nach", "14 bis 33 Jahren", "10 bis 25 Jahren"],
    ],
    hl_cols=(1, 2),
)}
<p>Zum Vergleich: Lithium-Speicher halten laut klimaaktiv 5.000 bis 7.000 Vollzyklen, das entspricht 15 bis
20 Jahren Betrieb. Die Garantie bei Balkonspeichern beträgt meist 10 Jahre (Verbraucherzentrale Niedersachsen,
Deutschland). Für die Rechnung nehmen wir 25 bis 30 Cent je eingesparter Kilowattstunde an: Der Durchschnittspreis
für Haushaltsstrom liegt in Kärnten und der Steiermark laut E-Control-Preismonitor (November 2026) bei rund 28 bis
35 Cent, darin stecken aber Grundpauschalen, die trotz Balkonkraftwerk bleiben.</p>
{A.box("Ein Speicher rechnet sich eher, wenn (1) mehr Modulleistung am Balkon hängt, etwa 1.600 bis 2.000 Wp, "
       "und damit mittags mehr übrig bleibt, (2) tagsüber niemand zu Hause ist und (3) der Speicher günstig ist. "
       "Wer tagsüber schon einen Großteil selbst verbraucht, hat für den Speicher kaum Überschuss. Die "
       "Verbraucherzentrale Niedersachsen hält die Wirtschaftlichkeit bei kleinen Anlagen mit zwei Modulen für "
       "\"nicht so attraktiv\", bei größeren Stecker-PV-Anlagen eher für gegeben.",
       label="Faustregel:")}
<p>Wie stark der Eigenverbrauch schon ohne Speicher sein kann, zeigen zwei klimaaktiv-Beispiele: Bei 2.800 bzw.
4.000 kWh Haushaltsverbrauch ersetzten 475 bzw. 467 kWh Balkonstrom 340 bzw. 400 kWh Netzbezug, also rund 72 bzw.
86 % (simuliert mit dem Stecker-Solar-Simulator der HTW Berlin). In solchen Haushalten bleibt für einen Speicher
wenig übrig. Wie die Rechnung bei einer großen Dachanlage aussieht, zeigt
{a('/ab-wann-lohnt-sich-photovoltaik-mit-speicher/', 'Ab wann lohnt sich Photovoltaik mit Speicher?')}.</p>
"""),
        ("Österreich 2026: 800 Watt, Meldung und was für Speicher gilt", "regeln", f"""
<p><b>Entscheidend ist in Österreich die Bemessungsleistung, die an der Übergabestelle ins Hausnetz gehen kann:
höchstens 800 Watt in Summe pro Anlage.</b> So steht es in § 6 Abs. 1 Z 78 ElWG, die Technischen und
Organisatorischen Regeln (TOR) übernehmen die Definition. Energie Klagenfurt, Netzbetreiber in Klagenfurt, hat im
Juli 2026 einen Leitfaden zu Kleinsterzeugungsanlagen mit Batteriespeicher veröffentlicht:</p>
{A.table(
    ["Ausführung", "Einstufung laut Leitfaden Energie Klagenfurt"],
    [
        ["800-W-Wechselrichter mit großer Modulleistung", "Kleinsterzeugungsanlage"],
        ["800-W-Wechselrichter mit Batteriespeicher", "Kleinsterzeugungsanlage"],
        ["800-W-Wechselrichter, große Modulleistung und Speicher", "Kleinsterzeugungsanlage"],
        ["Wechselrichter mit 5 kW, per Software auf 800 W begrenzt", "rechtlich kritisch, wird nicht akzeptiert"],
        ["5-kW-Hybridwechselrichter mit Speicher und 800-W-Limit", "keine Kleinsterzeugungsanlage, wird nicht akzeptiert"],
    ],
    hl_cols=(1,),
)}
<p>Der Grund: Eine Softwarebegrenzung kann geändert oder falsch eingestellt werden, die technische
Bemessungsleistung bleibt. Laut Leitfaden vertreten viele österreichische Netzbetreiber diese enge Auslegung.
Die Bad Gleichenberger Energie (Steiermark) schreibt in ihrem Meldeformular zudem ausdrücklich: Bei einem
Speicher im AC-Kreis umfasst die maximale Leistung von 0,8 kW die Ausgangsleistung des Speichers
<b>und</b> die Leistung der Wechselrichter.</p>
<ul>
  <li><b>Meldung statt Genehmigung:</b> Eine Genehmigung des Netzbetreibers braucht es nicht, aber eine Meldung zwei
  Wochen vor Inbetriebnahme (oesterreich.gv.at, Stand Oktober 2026). In Kärnten ist das meist die Kärnten Netz, in
  der Steiermark meist die Energienetze Steiermark, in Graz die Stromnetz Graz. Viele Formulare fragen Speicher,
  Kopplungsart und Ausgangsleistung ab.</li>
  <li><b>Kein Zählpunkt, keine Vergütung:</b> Kleinsterzeugungsanlagen brauchen keinen eigenen Zählpunkt und keinen
  Abnahmevertrag (E-Control). Der Netzbetreiber prüft den Zähler und tauscht ihn bei Bedarf.</li>
  <li><b>Steckdose:</b> Keine Verlängerungskabel, keine Steckdosenleisten (E-Control). Ob ein
  Schutzkontaktstecker reicht, sehen Netzbetreiber unterschiedlich streng: Wiener Netze verbietet ihn unter
  Verweis auf ÖVE E 8101. Wir prüfen Stromkreis und Steckdose vor der Montage.</li>
  <li><b>Wohnungseigentum:</b> Seit 1. September 2024 gilt die Zustimmung der anderen Eigentümer als erteilt, wenn
  sie nach schriftlicher Verständigung zwei Monate lang nicht widersprechen. Ein einziger Widerspruch, auch ohne
  Begründung, genügt, damit diese Zustimmungsfiktion entfällt. Mieterinnen und Mieter brauchen die Zustimmung des
  Vermieters.</li>
</ul>
<p>Ob es für den Speicher Geld gibt, steht im Ratgeber
{a('/balkonkraftwerk-foerderung-in-oesterreich/', 'Balkonkraftwerk-Förderung in Österreich')}.
Kurz: Vom Bund nicht, weil Anlagen ohne eigenen Einspeisezählpunkt vom EAG-Investitionszuschuss ausgeschlossen
waren.</p>
"""),
        ("AC- oder DC-gekoppelt: welcher Speicher für das Balkonkraftwerk?", "ac-dc", f"""
<p><b>Ein DC-Speicher sitzt zwischen Modulen und Wechselrichter, ein AC-Speicher hängt hinter dem Wechselrichter
am 230-Volt-Hausnetz.</b> Für die 800-Watt-Grenze in Österreich ist das der wichtigste Unterschied, weil ein
AC-Speicher einen eigenen Wechselrichter mitbringt.</p>
{A.table(
    ["", "DC-gekoppelt", "AC-gekoppelt", "All-in-one (Hybrid)"],
    [
        ["Anschluss", "zwischen Modulen und Mikro-Wechselrichter", "an der Steckdose, hinter dem Wechselrichter",
         "Module direkt am Speicher, Wechselrichter eingebaut"],
        ["800-W-Grenze", "bleibt beim vorhandenen 800-W-Wechselrichter",
         "Ausgang des Speichers zählt bei manchen Netzbetreibern zur Anlagenleistung dazu",
         "Bemessungsleistung des eingebauten Wechselrichters muss höchstens 800 W sein"],
        ["Nachrüsten", "Wechselrichter muss zum Speicher passen", "technisch einfach, rechtlich heikel",
         "meist Neukauf statt Nachrüstung"],
        ["Worauf achten", "Spannungsbereich und MPP-Tracker", "Summe der Ausgangsleistungen", "Datenblatt: Nennleistung, nicht nur Einspeiselimit"],
    ],
    hl_cols=(1,),
)}
<p>Manche Speicher haben Ausgänge mit mehr als 800 Watt und werden per App begrenzt. Nach dem Leitfaden
von Energie Klagenfurt reicht das nicht. Wer einen Speicher nachrüsten will, sollte deshalb vor dem Kauf das
Datenblatt mit dem zuständigen Netzbetreiber abgleichen. Für eine große Dachanlage gelten andere Regeln, siehe
{a('/pv-speicher-nachruesten/', 'PV-Speicher nachrüsten')}.</p>
"""),
        ("Speichergröße und Kosten", "kosten", f"""
<p><b>Für ein 800-Watt-Balkonkraftwerk reichen meist 1,5 bis 2 kWh Speicher.</b> Mehr kann ein Balkonkraftwerk an
einem Tag kaum füllen: Im klimaaktiv-Praxisbeispiel aus Wien lieferte eine 800-Wp-Anlage an sonnigen Frühlings-
und Herbsttagen 3,5 bis 4 kWh, ein Teil davon wird tagsüber direkt verbraucht. Die Verbraucherzentrale
Niedersachsen nennt als Faustregel rund 1 kWh Speicher je 1.000 kWh Jahresverbrauch, ein zu großer Speicher wird
oft nicht voll.</p>
{A.table(
    ["Posten", "Richtwert*", "Quelle"],
    [
        ["Balkonkraftwerk-Set", "500 bis 3.000 €", "klimaaktiv"],
        ["Praxisbeispiel Wien: Anlage plus Montage", "800 € plus 400 €", "klimaaktiv"],
        ["Balkonspeicher mit rund 2 kWh", "rund 700 bis 1.000 €", "Stiftung Warentest, März 2026 (Deutschland)"],
        ["Speicher je kWh Kapazität", "häufig 200 bis 400 €", "Verbraucherzentrale Niedersachsen (Deutschland)"],
        ["Beispiel 2,2-kWh-Speicher (DC)", "rund 500 €", "klimaaktiv"],
    ],
    hl_cols=(1,),
)}
<p>Montage, Prüfung des Stromkreises und Meldung kommen dazu. Einen Festpreis für Set, Speicher und Montage nennen
wir nach der Besichtigung, weil Halterung, Stromkreis und Aufstellort den Aufwand bestimmen. In unserem Angebot
stehen Set, Speicher und Montage als eigene Positionen.</p>
{A.cta("Speicher ja oder nein? Wir rechnen es für Ihren Balkon",
       "Wir sehen uns Ausrichtung, Stromkreis und Ihren Verbrauch an und sagen ehrlich, ob sich der Speicher lohnt "
       "und welcher in Ihrem Netzgebiet zulässig ist.",
       secondary=("balkonkraftwerke", "Balkonkraftwerk mit Montage"))}
"""),
        ("Sicherheit, Aufstellort und Notstrom", "sicherheit", f"""
<p><b>Ein Balkonspeicher gehört an einen geschützten, gut belüfteten Ort ohne starke Temperaturschwankungen:</b>
überdachter Balkon, Abstellraum oder Garage. Frost und Hitze lassen die Zellen schneller altern (Verbraucherzentrale
Niedersachsen). Die Geräte wiegen rund 20 bis 60 Kilogramm.</p>
<ul>
  <li><b>Qualität prüfen:</b> Stiftung Warentest (Deutschland, März 2026) bewertete drei von fünf Balkonspeichern mit
  "Mangelhaft", weil sie zu viele elektromagnetische Störsignale aussenden. Beim Starkregentest drang bei vier
  Geräten Wasser in die eingebauten Steckdosen, obwohl sie für draußen zugelassen sind.</li>
  <li><b>Konformität:</b> Laut E-Control braucht die Anlage einen Konformitätsnachweis einer zertifizierten
  Prüfstelle nach TOR Stromerzeugungsanlagen Typ A, vor allem für die selbsttätige Abschaltung bei Netzausfall.</li>
  <li><b>Brandrisiko einordnen:</b> Für fest installierte Heimspeicher in Deutschland ermittelte die RWTH Aachen
  eine Brandwahrscheinlichkeit von 0,0049 % pro Jahr. Für Balkonspeicher gibt es keine eigene Auswertung.</li>
</ul>
<p><b>Notstrom liefert ein Balkonkraftwerk mit Speicher meist nicht.</b> Fällt das Netz aus, muss sich die Anlage
selbsttätig vom Netz trennen. Manche Speicher haben eine eigene Steckdose für den Inselbetrieb, an der zum
Beispiel ein Router weiterläuft. Das klimaaktiv-Beispiel mit 2,2 kWh hatte keine Notstromfunktion. Wer das Haus
bei Stromausfall versorgen will, braucht eine Dachanlage mit Notstrom- oder Ersatzstromlösung, siehe
{a('/notstrom/', 'Notstrom mit Photovoltaik')}.</p>
"""),
        ("Die Alternative: kleine Dachanlage mit Speicher", "alternative", f"""
<p><b>Wer mehr als 800 Watt will, fährt mit einer angemeldeten PV-Anlage mit Speicher oft besser.</b> Sie bekommt
einen Einspeisezählpunkt, Überschuss wird vergütet (OeMAG-Marktpreis Oktober 2026: 14,874 Cent je kWh, der Wert
schwankt monatlich, siehe {a('marktpreis', 'Marktpreis 2026')}), und sie kann gefördert werden.</p>
{A.table(
    ["", "Balkonkraftwerk mit Speicher", "Dachanlage mit Speicher"],
    [
        ["Leistung", "höchstens 800 W", "nach Dach und Bedarf, oft 5 bis 10 kWp"],
        ["Speicher", "meist 1,5 bis 2 kWh", "ab 5 kWh, je nach Verbrauch"],
        ["Überschuss ins Netz", "keine Vergütung", "OeMAG-Marktpreis oder Stromlieferant"],
        ["Förderung", "vom Bund keine", "Kärnten: 3.000 € ab 5 kWp mit Speicher ab 5 kWh"],
        ["Notstrom", "meist nicht", "mit Notstrom- oder Ersatzstromlösung möglich"],
        ["Für wen", "Mieter, Wohnungen, kleiner Einstieg", "Eigenheim, Mehrparteienhaus, Betrieb"],
    ],
    hl_cols=(2,),
)}
<p>Das Land Kärnten zahlt im zweiten Call 2026 (Einreichung bis 31. Dezember 2026) 3.000 Euro Pauschale für neue
private PV-Anlagen ab 5 kWp mit neuem Speicher ab 5 kWh, errichtet ab 1. Jänner 2026, und 1.000 Euro für einen
nachgerüsteten Speicher ab 5 kWh. Ein Balkonspeicher mit 2 kWh erreicht diese Größe nicht. Details:
{a('/foerderung-pv-speicher-kaernten/', 'Förderung für PV-Speicher in Kärnten')}. Zur Einordnung: 10 kWp mit
Speicher kosten bei uns rund 15.000 bis 22.000 Euro vor Förderung,* mit
{a('finanzierung', 'Finanzierung')} ab 147 Euro im Monat inklusive Speicher, die Anlage gehört Ihnen ab Tag 1.
Welche Größe passt, zeigt {a('/pv-anlage-kwp-groessen/', 'PV-Anlage: welche kWp-Größe passt')}.</p>
<p>Für Wohnungen im Mehrparteienhaus kann eine gemeinsame Anlage am Dach mehr bringen als viele einzelne
Balkonkraftwerke. Beim {a('/referenzen/projekt-mehrparteienhaus-krumpendorf/', 'Mehrparteienhaus in Krumpendorf')}
haben wir 25 kWp mit 25 kWh Speicher und Notstrom in vier Tagen montiert. Strom teilen lässt sich auch über eine
{a('eg', 'Energiegemeinschaft')}.</p>
"""),
        ("Fazit: Speicher nur, wenn genug übrig bleibt", "fazit", f"""
<p>Ein Speicher macht das Balkonkraftwerk nicht automatisch wirtschaftlicher. Bei 600 bis 800 kWh Jahresertrag
verschiebt ein 2-kWh-Akku rund 120 bis 160 kWh in den Abend, das sind 30 bis 48 Euro im Jahr. Sinnvoll wird er
mit mehr Modulleistung, hohem Abendverbrauch und einem günstigen Gerät. In Österreich muss die gesamte
Bemessungsleistung höchstens 800 Watt betragen: Datenblatt prüfen, AC-Speicher nicht einfach dazustecken und die
Anlage zwei Wochen vor dem Start melden. Wer mehr Strom und Förderung will, plant eine kleine Dachanlage mit
Speicher.</p>
<p><small>*Richtwerte und eigene Berechnungen auf Basis der genannten Quellen: Eigenverbrauch rund 50 % ohne und
rund 70 % mit Speicher laut klimaaktiv-Beispiel, Jahresertrag 600 bis 800 kWh, 25 bis 30 Cent je eingesparter
kWh, Speicherpreis 500 bis 1.000 Euro, ohne Lade- und Umwandlungsverluste. Preise aus Deutschland sind als solche
gekennzeichnet. Richtpreis Dachanlage 10 kWp mit Speicher vor Förderung, Rate abhängig von Angebot und Laufzeit.
Stand November 2026.</small></p>
{A.cta("Balkonkraftwerk oder Dachanlage: ehrlich gerechnet",
       "Wir prüfen Balkon, Dach und Verbrauch und sagen Ihnen, ob Balkonkraftwerk, Speicher oder eine kleine "
       "Dachanlage mit Förderung für Sie mehr bringt.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("batteriespeicher", "Speicher für die Dachanlage"))}
"""),
    ],

    "partner": {
        "h2": "Balkonkraftwerk, Speicher und Dachanlage aus einer Hand",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie montiert Balkonkraftwerke mit und ohne Speicher sowie Photovoltaikanlagen mit "
                 "Batteriespeicher in Kärnten und der Steiermark, mit zertifizierten Fachkräften und einem festen "
                 "Ansprechpartner von der Planung bis zur Übergabe. Wir prüfen Stromkreis und Steckdose, wählen "
                 "einen Speicher, der in Ihrem Netzgebiet zulässig ist, und melden die Anlage beim Netzbetreiber."),
        "grid": [
            ("Ehrliche Rechnung", "Speicher nur, wenn er sich für Sie rechnet."),
            ("800 Watt sicher eingehalten", "Datenblatt und Kopplung vor dem Kauf geprüft."),
            ("Montage und Meldung", "Halterung, Stromkreis und Netzbetreiber erledigt."),
            ("Mitwachsend", "Vom Balkon zur Dachanlage mit Förderung."),
        ],
    },

    "faq": [
        ("Lohnt sich ein Balkonkraftwerk mit Speicher?",
         "Finanziell selten schnell. Ein 2-kWh-Speicher hebt den Eigenverbrauch laut klimaaktiv von etwa der Hälfte "
         "auf rund 70 %, bei 600 bis 800 kWh Jahresertrag sind das 30 bis 48 Euro mehr Ersparnis im Jahr.* Bei 500 "
         "bis 1.000 Euro Speicherpreis dauert die Amortisation 10 Jahre und länger."),
        ("Wie hoch ist die maximale Leistung eines Balkonkraftwerks in Österreich?",
         "Höchstens 800 Watt Bemessungsleistung in Summe an der Übergabestelle, so definiert § 6 Abs. 1 Z 78 ElWG "
         "die Kleinsterzeugungsanlage. Die Modulleistung und die Speicherkapazität zählen dafür nicht. Darüber "
         "braucht es einen Netzzugangsantrag über einen Elektrobetrieb."),
        ("Darf ich ein Balkonkraftwerk mit 2.000 Watt Modulen und Speicher betreiben?",
         "Ja, wenn der Wechselrichter höchstens 800 Watt Bemessungsleistung hat. Laut Leitfaden von Energie "
         "Klagenfurt sind große Modulleistung und Speicher mit einem 800-W-Wechselrichter zulässig. Ein größerer "
         "Wechselrichter, der nur per Software auf 800 Watt begrenzt ist, wird nicht als Kleinsterzeugungsanlage "
         "akzeptiert."),
        ("Kann ich einen Speicher für mein Balkonkraftwerk nachrüsten?",
         "Ja, aber prüfen Sie die Kopplung. Ein DC-Speicher zwischen Modulen und Wechselrichter lässt die 800-Watt-"
         "Grenze unverändert. Bei einem AC-Speicher an der Steckdose zählt etwa die Bad Gleichenberger Energie die "
         "Ausgangsleistung des Speichers zur Leistung des Wechselrichters dazu, die Summe darf 0,8 kW nicht "
         "überschreiten."),
        ("Wie groß sollte der Speicher für ein Balkonkraftwerk sein?",
         "Für ein 800-Watt-Balkonkraftwerk meist 1,5 bis 2 kWh. An sonnigen Tagen liefert eine 800-Wp-Anlage rund "
         "3,5 bis 4 kWh, einen Teil davon verbrauchen Sie direkt. Ein größerer Speicher wird oft nicht voll."),
        ("Muss ich das Balkonkraftwerk mit Speicher anmelden?",
         "Ja, beim Netzbetreiber zwei Wochen vor Inbetriebnahme, nicht beim Stromlieferanten. Eine Genehmigung "
         "braucht es nicht. Viele Meldeformulare fragen Speicher, Kopplungsart und Ausgangsleistung ab, geben Sie "
         "den Speicher daher immer mit an."),
        ("Liefert ein Balkonkraftwerk mit Speicher Notstrom?",
         "Meist nicht. Bei Netzausfall muss sich die Anlage selbsttätig abschalten. Manche Speicher haben eine "
         "eigene Steckdose für einzelne Geräte wie den Router. Für das ganze Haus braucht es eine Dachanlage mit "
         "Notstrom- oder Ersatzstromlösung."),
        ("Gibt es eine Förderung für den Speicher am Balkonkraftwerk?",
         "Vom Bund nicht, Balkonkraftwerke ohne eigenen Einspeisezählpunkt waren vom EAG-Zuschuss ausgeschlossen. "
         "Die Kärntner Speicherförderung (1.000 Euro für Nachrüstung, 3.000 Euro mit neuer PV ab 5 kWp) setzt "
         "mindestens 5 kWh Speicher voraus, das erreicht ein Balkonspeicher nicht."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Mit zertifizierten Fachkräften montiert EBZ "
                    "Energie Balkonkraftwerke, Photovoltaikanlagen und Batteriespeicher in Kärnten und der "
                    "Steiermark. Rechnungen und Preise in diesem Ratgeber sind Richtwerte. Keine Rechtsberatung: "
                    "Maßgeblich sind ElWG, Wohnungseigentumsgesetz und die Vorgaben Ihres Netzbetreibers."),
    "sources": [
        ("Energie Klagenfurt: Kleinsterzeugungsanlagen (0,8 kW) mit Batteriespeicher nach dem ElWG, Leitfaden 15.07.2026",
         "https://www.stw.at/wp-content/uploads/2026/08/kleintsterzteugungsanlagen_mit_batteriespeicher_leitfaden_15072026.pdf"),
        ("Bad Gleichenberger Energie: Meldung Kleinsterzeugungsanlage (Mai 2026)",
         "https://www.bg-energie.at/media/pages/downloads/d3e411e699-1779194075/meldung-kleinsterzeugungsanlagen-balkonkraftwerk_v202605.pdf"),
        ("oesterreich.gv.at: Selbsterzeugung von Strom mit erneuerbaren Energieträgern",
         "https://www.oesterreich.gv.at/de/themen/umwelt_und_klima/energie_und_ressourcen_sparen/selbsterzeugung-von-strom-mit-erneuerbaren-energietraegern"),
        ("E-Control: Anschluss von Kleinsterzeugungsanlagen (FAQ)",
         "https://www.e-control.at/documents/1785851/1811582/faq-mini-pv-anlagen.pdf/4ae8d201-921c-70f5-86e8-99bc4c68c240?t=1662024790027"),
        ("Wiener Netze: Balkonkraftwerk", "https://www.wienernetze.at/balkonkraftwerk"),
        ("WKO: WEG-Novelle, Installation von Balkonkraftwerken",
         "https://www.wko.at/information-consulting/immobilien-vermoegenstreuhaender/weg-novelle-installation-von-balkonkraftwerken"),
        ("klimaaktiv: Strom speichern, Kosten reduzieren",
         "https://www.klimaaktiv.at/private/zukunftsfittes-haus/photovoltaik/strom-speichern-kosten-senken"),
        ("klimaaktiv: Photovoltaik-Balkonkraftwerk (Fachpersonen)",
         "https://www.klimaaktiv.at/fachpersonen/energie-bau/photovoltaik/balkonkraftwerk"),
        ("klimaaktiv: Balkonkraftwerk mit Speicher, Praxisbeispiel Wien", "https://www.klimaaktiv.at/balkonkraftwerk-mit-speicher"),
        ("Verbraucherzentrale Niedersachsen: Batteriespeicher für Balkonkraftwerke (Deutschland)",
         "https://www.verbraucherzentrale-niedersachsen.de/wissen/energie/erneuerbare-energien/batteriespeicher-fuer-balkonkraftwerke-lohnt-sich-das-123659"),
        ("Stiftung Warentest: Speicher für Balkonkraftwerke im Test, März 2026 (Deutschland)",
         "https://www.test.de/Speicher-fuer-Balkonkraftwerke-im-Test-6278221-0/"),
        ("pv magazine: Brandwahrscheinlichkeit von Heimspeichern, Studie RWTH Aachen (Deutschland)",
         "https://www.pv-magazine.de/2024/12/09/brandwahrscheinlichkeit-von-photovoltaik-heimspeichern-bei-00049-prozent/"),
        ("E-Control: Strom- und Gaspreismonitor November 2026", "https://www.e-control.at/preismonitor"),
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/de/marktpreis/"),
        ("5min.at: Kärntner PV-Förderung ab 12. Oktober 2026",
         "https://www.5min.at/kaernten/5202610030852/ab-12-oktober-diese-3-000-foerderung-gibt-es-wieder-fuer-kaerntner/"),
    ],
    "related": [
        ("balkonkraftwerke", "Balkonkraftwerk mit Speicher: Montage und Anmeldung"),
        ("/balkonkraftwerk-foerderung-in-oesterreich/", "Balkonkraftwerk-Förderung in Österreich"),
        ("batteriespeicher", "Batteriespeicher für die PV-Anlage"),
        ("/foerderung-pv-speicher-kaernten/", "Förderung für PV-Speicher in Kärnten"),
    ],
    "cta": {
        "h3": "Balkonkraftwerk mit Speicher?",
        "text": "Wir prüfen, ob sich der Speicher lohnt und welcher in Ihrem Netzgebiet zulässig ist.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Balkonkraftwerk mit Speicher, ehrlich gerechnet",
    "final_text": ("Kostenlose Erstberatung zu Balkonkraftwerk, Speicher und kleiner Dachanlage, mit transparenten "
                   "Zahlen, Montage und Meldung durch einen Ansprechpartner aus Villach."),
}
