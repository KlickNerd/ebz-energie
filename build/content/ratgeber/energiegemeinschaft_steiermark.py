"""Ratgeber: Energiegemeinschaft Steiermark.

Migriert von ebz-photovoltaik.at/energiegemeinschaft-steiermark/ (Stand August 2026),
Inhalt freigegeben, auf die Ratgeber-Vorlage umgestellt. Rechenbeispiel der Quelle war in
sich widersprüchlich (Jahresverbrauch 5.000 kWh bei 5.800 kWh Eigenverbrauch) und wurde
auf konsistente Werte gebracht (Jahresverbrauch 7.800 kWh, Netzbezug 2.000 kWh).
Korrektur 10.10.2026 (build/seo/_fakten_2026-10.md): Der 125-€/kWp-Bonus war Teil der PV-Ausschreibung des
Ökofonds; der Ökofonds hat derzeit keine PV-Ausschreibung, der Bonus steht daher nicht mehr als laufend da.
Update 20.11.2026: ElWG-Faktenfix (Übergangsphase, Netzentgelt nur EEG bis Ende 2026), neuer Abschnitt
"Angebote und Anlaufstellen" mit Preisen, die am 20.11.2026 auf den Anbieterseiten geöffnet wurden, Regionen
mit belegten Gemeinschaften statt der generischen Bezirkstabelle, Netzbetreiber ergänzt (Feistritzwerke,
Stadtwerke Voitsberg), FAQ zu Gründung, Abrechnung und ElWG.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a


def _ext(url, text):
    """Externer Quellenlink (nofollow, neuer Tab)."""
    return f'<a href="{url}" rel="nofollow noopener" target="_blank">{text}</a>'


# Werte am 20.11.2026 auf den Anbieterseiten geöffnet (siehe Abschlussbericht / sources).
_ANGEBOTE = A.table(
    ["Anbieter / Stelle", "Modell", "Reichweite", "Preise bzw. Leistung (Stand November 2026)", "Quelle"],
    [
        ["Energieinitiative Steiermark (Raiffeisen-Landesbank Steiermark)",
         "regionale Energiegemeinschaften als Genossenschaften (eGen), laut Anbieter 16 in der Steiermark",
         "je Gemeinschaft ein Umspannwerk, z. B. Weiz Nord, Gleisdorf, Deutschlandsberg, Liesingtal",
         "Q4 2026 in den sieben von uns geprüften Gemeinschaften: Bezug 10,5 bis 11,5 ct, Einspeisung 7,5 bis "
         "10,5 ct je kWh, jeweils netto (exkl. USt)",
         _ext("https://energieinitiative.at/", "energieinitiative.at")],
        ["EEG Steiermark (Landes-EEG) mit Mitgliedsvereinen wie der EEG Premstätten",
         "Erneuerbare-Energie-Gemeinschaft, Verein",
         "Regional-Tarife, daneben eigene Austria-Tarife",
         "Bezug Regional Fix 11,94 ct je kWh brutto (inkl. Servicegebühr und Steuer bzw. Mitgliederausgleich; "
         "Energie-Basispreis 8,95 ct netto); Einspeisung Regional PV 7,75 ct je kWh inkl. Servicegebühr, ohne "
         "Abschläge; Mitgliedsbeitrag 12 € pro Jahr und Zählpunkt; Preisgarantie 1.1. bis 31.12.2026",
         _ext("https://www.eeg-premstaetten.at/tarife", "eeg-premstaetten.at")],
        ["EG Aichfeld",
         "regionale Erneuerbare-Energie-Gemeinschaft",
         "Umspannwerke Knittelfeld, Zeltweg und Judenburg West (Murtal)",
         "Bezug und Einspeisung je 9,00 ct je kWh netto; Grundgebühr 2,00 € pro Zählpunkt und Monat; "
         "Abrechnung quartalsweise",
         _ext("https://www.eg-aichfeld.at/", "eg-aichfeld.at")],
        ["smartCOMMUNITY der Energie Steiermark",
         "Peer-to-Peer-Handelsplattform des Lieferanten, laut Anbieter keine EEG oder BEG",
         "laut Anbieter österreichweit; nur für Stromkunden der Energie Steiermark, PV bis 50 kWp",
         "Preis legen die Teilnehmer selbst fest (Durchschnitt September 2026: 9,26 ct je kWh inkl. 20 % USt); "
         "2,50 € pro Monat inkl. USt, in den ersten 12 Monaten frei; Einspeise-Abwicklung 2,00 ct je kWh "
         "exkl. USt; Netzgebühren, Steuern und Abgaben bleiben unverändert",
         _ext("https://www.e-steiermark.com/smartcommunity", "e-steiermark.com")],
        ["Beratungsstelle Energiegemeinschaften der Energie Agentur Steiermark",
         "unabhängige Beratung",
         "ganze Steiermark",
         "kostenlose Beratung zu Modellwahl und Gründung; Telefon +43 316 269 700 0 (Montag und Mittwoch "
         "13:00 bis 16:00 Uhr), schriftlich jederzeit an energiegemeinschaften@ea-stmk.at",
         _ext("https://www.ea-stmk.at/eag/energiegemeinschaften/", "ea-stmk.at")],
        ["Energienetze Steiermark",
         "Netzbetreiber",
         "Großteil der Steiermark (Graz-Stadt: Stromnetz Graz)",
         "Quick Check zur Nahbereichszuordnung (portal.e-netze.at/nahbereich), Teilnahmebestätigung im "
         "Serviceportal; Kontakt energiegemeinschaften@e-netze.at, Info-Hotline 0316 90555",
         _ext("https://www.e-netze.at/energiegemeinschaften", "e-netze.at")],
    ],
)

_SV_LINK = _ext("https://stromverbindet.energiegemeinschaften.gv.at/", "stromverbindet.energiegemeinschaften.gv.at")

ARTICLE = {
    "slug": "energiegemeinschaft-steiermark",
    "path": "/energiegemeinschaft-steiermark/",
    "title": "Energiegemeinschaft Steiermark: Angebote, Preise, ElWG | EBZ",
    "description": "Energiegemeinschaft Steiermark: Preise von 7,5 bis 11,5 ct je kWh (Stand November 2026), "
                   "Beratungsstelle, Regionen von Graz bis Murtal, ElWG-Regeln ab 2027.",
    "eyebrow": "Energiegemeinschaft · Steiermark",
    "crumb_label": "Energiegemeinschaft Steiermark",
    "h1": "Energiegemeinschaft Steiermark: Angebote, Preise und Regeln nach ElWG",
    "lead": ("In der Steiermark gibt es regionale Energiegemeinschaften von Deutschlandsberg bis ins Aichfeld, "
             "dazu eine kostenlose Beratungsstelle und ein Prüfwerkzeug des Netzbetreibers. Hier finden Sie "
             "Angebote mit Preisen (Stand November 2026), die Regeln nach dem ElWG und den Weg zur eigenen "
             "Gemeinschaft."),
    "chips": [
        "Beitritt: <b>4 bis 8 Wochen</b>",
        "EEG-Netzrabatt: <b>bis zu 57 %</b>",
        "OeMAG Okt. 2026: <b>14,874 ct/kWh</b>",
        "EBZ vor Ort in der <b>ganzen Steiermark</b>",
    ],
    "date_published": "2026-08-05",
    "date_modified": "2026-11-20",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus in der Steiermark mit Photovoltaikanlage auf dem Dach",

    "tldr": [
        "Seit 1. Oktober 2026 gilt das ElWG mit fünf Modellen (GEA, EEG, BEG, Peer-to-Peer, Eigenversorgung). "
        "Bis Ende 2026 bekommen nur Mitglieder lokaler und regionaler EEGs den reduzierten Netzarbeitspreis "
        "(minus 57 % lokal, minus 28 % regional). BEG, Peer-to-Peer und Eigenversorgung im Nahbereich folgen "
        "voraussichtlich ab 1.1.2027, Teilen über mehrere Netzgebiete voraussichtlich ab April 2027.",
        "Steirische Angebote, Stand November 2026: Die geprüften Genossenschaften der Energieinitiative "
        "Steiermark zahlen 7,5 bis 10,5 ct je kWh für die Einspeisung und verrechnen 10,5 bis 11,5 ct für den "
        "Bezug (netto), die EG Aichfeld 9,00 ct in beide Richtungen.",
        "Kostenlose Beratung gibt die Beratungsstelle Energiegemeinschaften der Energie Agentur Steiermark. Ob "
        "Ihr Anschluss lokal oder regional zu einer Gemeinschaft passt, zeigt der Quick Check der Energienetze "
        "Steiermark.",
        "Der OeMAG-Marktpreis schwankt monatlich: Juli 2026 6,146 ct, September 10,168 ct, Oktober 14,874 ct je "
        "kWh. Planbar ist dagegen der Bezugsvorteil in der EEG: weniger Netzentgelt im Nahbereich und keine "
        "Elektrizitätsabgabe (2026 für Haushalte befristet 0,1 ct, ab 2027 wieder 1,5 ct je kWh). Den "
        "Erneuerbaren-Förderbeitrag setzt die Bundesregierung 2027 für alle Stromkunden aus.",
        "Den früheren steirischen Bonus von 125 Euro je kWp (Ökofonds) gibt es derzeit nicht, weil der Ökofonds "
        "keine PV-Ausschreibung hat (Stand Oktober 2026).",
    ],
    "kpis": [
        ("14,874 ct/kWh", "OeMAG-Marktpreis Oktober 2026 (Juli: 6,146 ct)"),
        ("7,5 bis 10,5 ct", "EG-Einspeisepreise netto, geprüfte steirische Angebote Q4 2026"),
        ("57 % / 28 %", "Netzentgelt-Abschlag EEG lokal / regional (SNE-VO, bis Ende 2026)"),
        ("4 bis 8 Wochen", "vom Erstgespräch bis zum Start"),
    ],

    "sections": [
        ("Energiegemeinschaft in der Steiermark: die Ausgangslage", "ausgangslage", f"""
<p>Die Steiermark hat in den vergangenen Jahren mehr PV-Leistung zugebaut als fast jedes andere Bundesland, und
genau daraus entsteht das Problem, das die Energiegemeinschaft löst: Zu Mittag drückt so viel Sonnenstrom ins Netz,
dass der Börsenpreis fällt und der OeMAG-Tarif monatlich schwankt: im Juli 2026 lag er mit 6,146 Cent pro
Kilowattstunde an der gesetzlichen Untergrenze, im Oktober 2026 bei 14,874 Cent. Planbar ist er damit nicht. Ihre
Nachbarn zahlen für Strom aus dem Netz gleichzeitig den vollen Arbeitspreis plus Netzentgelt und Abgaben. Eine
Energiegemeinschaft schließt diese Lücke, indem sie Ihren Überschuss direkt an Abnehmer im selben Netzgebiet
verkauft, zu einem Preis, den die Gemeinschaft selbst bestimmt.</p>
{A.table(
    ["Wo der Überschuss landet", "Cent je kWh", "Wer bekommt / zahlt"],
    [
        ["OeMAG-Tarif (Juli 2026)", "6,1 ct", "Erzeuger bekommt"],
        ["OeMAG-Tarif (Oktober 2026)", "14,9 ct", "Erzeuger bekommt"],
        ["EG-Einspeisung*", "10,0 ct", "Erzeuger bekommt"],
        ["EG-Bezug*", "14,0 ct", "Abnehmer zahlt"],
        ["Lieferant, Arbeitspreis netto*", "17,0 ct", "Abnehmer zahlt"],
    ],
    hl_cols=(1,),
)}
<p>Zwischen OeMAG-Tarif und Arbeitspreis des Lieferanten lag 2026 je nach Monat eine Spanne von rund 2 bis 11 Cent.
Die Energiegemeinschaft teilt diese Spanne zwischen Erzeuger und Abnehmer auf. Liegt der OeMAG-Tarif wie im Oktober
über dem EG-Preis, bekommt der Erzeuger für den zugeordneten Strom weniger als bei der OeMAG, dafür einen planbaren
Preis; der Abnehmer spart in einer lokalen oder regionalen EEG zusätzlich Netzentgelt und Abgaben. Das Prinzip ist
in ganz Österreich gleich und in unserem {a('eg', 'Leitartikel zur Energiegemeinschaft')} erklärt. Was die
Steiermark besonders macht: mehrere Netzbetreiber (Energienetze Steiermark, Stromnetz Graz und regionale wie die
Feistritzwerke oder die Stadtwerke Voitsberg) und viele bestehende regionale Gemeinschaften.</p>
<p><small>*Beispielwerte, jede Gemeinschaft legt ihre Preise selbst fest. Lieferantenpreis netto ohne Netz und
Abgaben. Echte Preise steirischer Gemeinschaften stehen im Abschnitt Angebote und Anlaufstellen, Anbieter aus
ganz Österreich im {a('/energiegemeinschaft-vergleich/', 'Energiegemeinschaft-Vergleich')}.</small></p>
"""),
        ("Der steirische Bonus von 125 Euro je kWp: derzeit nicht beantragbar", "landesbonus", f"""
<p>Die PV-Ausschreibung des Ökofonds Steiermark kannte bis Ende Mai 2026 einen Zuschlag von 125 Euro pro
Kilowattpeak, wenn die Anlage in ein ganzheitliches, dezentrales Energiesystem eingebunden war: bei Kombination
mit mindestens zwei weiteren neu installierten Komponenten, etwa {a('batteriespeicher', 'Speicher')} und Wallbox,
oder eben durch die Teilnahme an einer Energiegemeinschaft. Der Bonus galt für Anlagen ab 20 kWp mit
Doppelnutzung. Stand 10. Oktober 2026 führt der Ökofonds keine PV-Ausschreibung (nur Wasserstoffprojekte und
Innovative Energiespeicher), der Bonus ist daher derzeit nicht beantragbar. Den aktuellen Förderstand finden Sie
im Artikel {a('foerderung_steiermark', 'Photovoltaik-Förderung Steiermark 2026')}.</p>
{A.box("Ob der Ökofonds wieder eine PV-Ausschreibung öffnet, ist offen. Planen Sie die Energiegemeinschaft "
       "deshalb nach ihrem laufenden Vorteil und nicht nach einem Bonus. Den Förderstand prüfen wir vor dem "
       "Angebot.", label="Praxistipp:")}
"""),
        ("Netzgebiete und ElWG: was seit Oktober 2026 gilt", "netzgebiete", f"""
<p>Den Großteil der Steiermark versorgt die Energienetze Steiermark GmbH, die Landeshauptstadt die Stromnetz Graz
GmbH. Dazu kommen regionale Netzbetreiber, etwa die Feistritzwerke rund um Gleisdorf oder die Stadtwerke Voitsberg.
Alle melden Zählpunkte nach demselben bundesweiten Verfahren über die EDA an und ordnen Ihren Anschluss einem Trafo
und einem Umspannwerk zu. Daraus ergibt sich, ob Sie mit anderen Teilnehmern lokal oder regional verbunden sind.
Im Gebiet der Energienetze Steiermark können Sie das vorab im Quick Check prüfen
(portal.e-netze.at/nahbereich), die endgültige Zuordnung erfolgt bei der Anmeldung.</p>
<p>Seit 1. Oktober 2026 gilt das Elektrizitätswirtschaftsgesetz (ElWG). Es kennt fünf Modelle zum gemeinsamen
Nutzen von Strom: {a('/gemeinschaftliche-erzeugungsanlage/', 'gemeinschaftliche Erzeugungsanlage (GEA)')},
Erneuerbare-Energie-Gemeinschaft (EEG), {a('/buergerenergiegemeinschaft/', 'Bürgerenergiegemeinschaft (BEG)')},
{a('/peer-to-peer-strom/', 'Peer-to-Peer-Vertrag (P2P)')} und Eigenversorgungsanlage (EVA). Mit einem
Zählpunkt können Sie an bis zu fünf dieser Modelle gleichzeitig teilnehmen. Für die Steiermark bedeutet die
Übergangsphase:</p>
<ul>
<li><b>Netzentgelt bis Ende 2026:</b> Von Oktober bis Dezember 2026 bekommen nur Mitglieder lokaler und
regionaler EEGs den reduzierten Netzarbeitspreis. Die Werte der geltenden SNE-VO: minus 57 Prozent lokal, minus
28 Prozent regional, minus 64 Prozent bei ausschließlich Netzebene 4/5. Für BEG, Peer-to-Peer und Eigenversorgung
verrechnen die Netzbetreiber in diesem Zeitraum noch keine Reduktion, das bestätigen auch die Energienetze
Steiermark.</li>
<li><b>Ab 1.1.2027:</b> Mit der novellierten SNE-VO sollen nach heutigem Stand auch lokale und regionale BEG,
Peer-to-Peer und Eigenversorgung reduzierte Netzentgelte bekommen. Die Höhe ab 2027 legt die E-Control per
Verordnung fest, laut E-Control-Entwurf für 2027 49 % lokal, 22 % bzw. 58 % regional (Entwurf).</li>
<li><b>Über Netzgrenzen:</b> Neue Zuordnungen lassen sich seit 5. Oktober 2026 vorübergehend nur mit Zählpunkten
beim selben Netzbetreiber umsetzen. Netzübergreifend, also etwa Graz-Stadt mit Graz-Umgebung oder die Steiermark
mit Wien, geht das laut Koordinationsstelle voraussichtlich ab April 2027.</li>
<li><b>Abgaben:</b> Der Entfall von Elektrizitätsabgabe und Erneuerbaren-Förderbeitrag gilt derzeit nur in der
EEG. Die Elektrizitätsabgabe beträgt 2026 für Haushalte befristet 0,1 Cent, ab 2027 wieder 1,5 Cent je kWh; den
Förderbeitrag setzt die Bundesregierung 2027 für alle aus. Der Abgabenvorteil der EEG liegt 2027 damit bei rund
1,5 Cent je zugeordneter Kilowattstunde.</li>
</ul>
<p>Der Abschlag wirkt auf den Arbeitspreis des Netznutzungs- und Netzverlustentgelts. Die Rechnung Position für
Position steht im Artikel {a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft und Netzkosten')}, die fünf
Modelle im Detail im {a('eg', 'Leitartikel Energiegemeinschaft')}.</p>
"""),
        ("Energiegemeinschaften in der Steiermark: Angebote und Anlaufstellen", "angebote", f"""
<p>Die folgende Übersicht enthält nur Angebote und Stellen, deren Angaben wir am 20. November 2026 auf der
jeweiligen Website selbst geprüft haben. Sie ist keine vollständige Liste: In der Steiermark gibt es weitere
Gemeinschaften, etwa Vereine einzelner Gemeinden oder Stadtteile.</p>
{_ANGEBOTE}
<p><small>Stand November 2026, Werte laut Websites der Anbieter. Netto = exklusive Umsatzsteuer, brutto =
inklusive. Preise ändern sich, meist quartalsweise oder jährlich; maßgeblich ist das aktuelle Tarifblatt der
jeweiligen Gemeinschaft.</small></p>
<p><b>Fair verglichen mit der OeMAG:</b> Der OeMAG-Marktpreis lag im Oktober 2026 bei 14,874 Cent je kWh, im
September bei 10,168 Cent und im Juli bei 6,146 Cent. Die EG-Einspeisepreise von 7,5 bis 10,5 Cent lagen damit im
Oktober darunter und im Juli darüber, dafür stehen sie für ein Quartal oder ein Jahr fest. Strom, den die
Gemeinschaft nicht abnimmt, geht weiter an die OeMAG oder Ihren Abnehmer. Für Abnehmer kommt in einer lokalen
oder regionalen EEG der Netzentgelt-Abschlag dazu, den der Netzbetreiber direkt auf der Netzrechnung
berücksichtigt. Welche Grenzen das Modell hat, steht offen im Ratgeber
{a('/energiegemeinschaft-nachteile/', 'Nachteile einer Energiegemeinschaft')}.</p>
<p><b>Wo EBZ hilft:</b> EBZ betreibt keine der genannten Gemeinschaften. Wir planen und errichten die
{a('photovoltaik', 'PV-Anlage')} mit Speicher, prüfen, welche Gemeinschaft an Ihrem Umspannwerk passt, und binden
Sie an eine Gemeinschaft an, die über unseren Abrechnungspartner energyfamily abgerechnet wird. Für
Nachbarschaften, Betriebe und Gemeinden gründen wir eine Gemeinschaft im Nahbereich, siehe
{a('eg_gewerbe', 'Energiegemeinschaft für Gewerbe und Gemeinden')}. Ob eine bestehende Gemeinschaft vor Ort oder
eine neue besser zu Ihnen passt, klären wir im Erstgespräch.</p>
"""),
        ("Energiegemeinschaft in den steirischen Regionen", "bezirke", f"""
<p>Pro Region nennen wir Gemeinschaften, die wir in öffentlichen Quellen gefunden haben (Anbieterseiten, Gemeinden,
Regionalmedien). Wo wir nichts belegen konnten, steht nichts. Eine Suche nach Gemeinschaften in Ihrer Nähe bietet
auch die Plattform Strom verbindet der Koordinationsstelle
({_SV_LINK}).</p>
<h3>Energiegemeinschaft Graz und Graz-Umgebung</h3>
<p>In Graz-Stadt ist die Stromnetz Graz Netzbetreiber, rundherum meist die Energienetze Steiermark; bis April 2027
lassen sich neue Zuordnungen nur innerhalb eines Netzgebiets umsetzen. Im Bezirk Geidorf hat der Verein EEG
Graz-Geidorf im März 2026 zu einer Informationsveranstaltung geladen, in Premstätten sitzt die EEG Premstätten als
Mitgliedsverein der EEG Steiermark. Unsere Leistungen vor Ort: {a('pv_graz', 'Photovoltaik in Graz')}.</p>
<h3>Energiegemeinschaft Murtal</h3>
<p>Die EG Aichfeld nimmt Zählpunkte an den Umspannwerken Knittelfeld, Zeltweg und Judenburg West auf und
verrechnet laut Website 9,00 Cent je kWh netto für Bezug und Einspeisung. Ob Ihr Anschluss dazugehört, zeigt die
Nahbereichsabfrage. Mehr zur Region: {a('pv_murtal', 'Photovoltaik im Murtal')}.</p>
<h3>Energiegemeinschaft Weiz und Weiz Nord</h3>
<p>Die Energiegenossenschaft Weiz Nord UM1 eGen (im Firmenbuch seit 30.10.2024, Sitz Weiz) arbeitet am
Umspannwerk Tannhausen und umfasst unter anderem Anger, Weiz, Passail und Floing. Preise im vierten Quartal 2026:
Bezug 11,5 Cent, Einspeisung 9,5 bis 10,5 Cent je kWh netto, je nach Uhrzeit. Vor Ort: {a('pv_weiz', 'Photovoltaik in Weiz')}.</p>
<h3>Energiegemeinschaft Gleisdorf</h3>
<p>Rund um Gleisdorf ist die Energiegenossenschaft Umspannwerk Gleisdorf UM2 im Netz der Feistritzwerke aktiv,
unter anderem für Pischelsdorf, Nestelbach und Sinabelkirchen (Q4 2026: Bezug 11,5 Cent, Einspeisung 9,5 bis 10,5
Cent netto). Gleisdorf liegt im Bezirk Weiz, unsere Seite dazu: {a('pv_weiz', 'Photovoltaik Bezirk Weiz')}.</p>
<h3>Energiegemeinschaft Leibnitz und Südsteiermark</h3>
<p>Die Gemeinde Großklein informiert über die regionale Erneuerbare Energiegemeinschaft Sulmtal-Sausal. Eine
vollständige Übersicht für den Bezirk Leibnitz haben wir nicht gefunden; den Nahbereich Ihres Anschlusses klärt der
Quick Check der Energienetze Steiermark. Vor Ort: {a('pv_leibnitz', 'Photovoltaik in Leibnitz')}.</p>
<h3>Energiegemeinschaft Deutschlandsberg</h3>
<p>Die Energiegenossenschaft Region Deutschlandsberg arbeitet am Umspannwerk Deutschlandsberg und umfasst
Deutschlandsberg, Frauental, Groß St. Florian, Stainz, Bad Schwanberg und Sankt Peter im Sulmtal. Q4 2026: Bezug 11
Cent, Einspeisung 8,5 Cent je kWh netto. Vor Ort: {a('pv_deutschlandsberg', 'Photovoltaik in Deutschlandsberg')}.</p>
<h3>Energiegemeinschaft Voitsberg</h3>
<p>Im Netz der Stadtwerke Voitsberg ist die Energiegenossenschaft Mittleres Kainachtal aktiv, unter anderem für
Voitsberg, Krottendorf-Gaisfeld, Ligist, Bärnbach und Rosental (Q4 2026: Bezug 11 Cent, Einspeisung 8,5 Cent netto).
Die EEG Rosental meldete im Juli 2026 108 Mitglieder mit 143 Zählpunkten und 361,62 MWh ausgetauschter Energie im
laufenden Jahr. Vor Ort: {a('pv_voitsberg', 'Photovoltaik in Voitsberg')}.</p>
<h3>Energiegemeinschaft Leoben</h3>
<p>Die Energiegenossenschaft Region Liesingtal arbeitet am Umspannwerk Hessenberg und umfasst Trofaiach, Sankt
Michael in Obersteiermark, Traboch, St. Peter-Freienstein, Kammern, Mautern, Kalwang und Wald am Schoberpaß. Q4 2026:
Bezug 11 Cent, Einspeisung 9,5 Cent je kWh netto. Vor Ort: {a('pv_leoben', 'Photovoltaik in Leoben')}.</p>
<h3>Energiegemeinschaft Südoststeiermark</h3>
<p>Am Umspannwerk Feldbach arbeitet die Energiegenossenschaft Region Fehring-Riegersburg (Fehring, Riegersburg,
Feldbach; Q4 2026: Bezug 11 Cent, Einspeisung 8,5 Cent netto), am Umspannwerk Halbenrain die Energiegenossenschaft
Region Halbenrain (Halbenrain, Tieschen, Klöch, Bad Radkersburg; Bezug 10,5 Cent, Einspeisung 7,5 Cent netto). Vor
Ort: {a('pv_suedoststeiermark', 'Photovoltaik in der Südoststeiermark')}.</p>
<p>Alle weiteren Bezirke und unser Einzugsgebiet finden Sie unter {a('pv_steiermark', 'Photovoltaik Steiermark')}.
Wie Sie eine passende Gemeinschaft auswählen, zeigt der Artikel
{a('/energiegemeinschaft-finden/', 'Energiegemeinschaft finden')}; wenn es vor Ort keine gibt, hilft der Ratgeber
{a('/energiegemeinschaft-gruenden/', 'Energiegemeinschaft gründen')}.</p>
{A.cta("Energiegemeinschaft in der Steiermark: Jetzt Eignung prüfen",
       "Wir klären Netzgebiet, passende Gemeinschaft und Ihr Einsparpotenzial.",
       secondary=("eg_rechner", "Ersparnis berechnen"))}
"""),
        ("Rechenbeispiel für ein steirisches Einfamilienhaus", "rechenbeispiel", f"""
<p>Ein Haushalt in der Weststeiermark mit 10 kWp und 5 kWh Speicher, Jahresverbrauch rund 7.800 kWh (mit
Wärmepumpe), Ertrag rund 10.500 kWh. Eigenverbrauch mit Speicher etwa 55 Prozent der Erzeugung, also 5.800 kWh, der
Rest von 4.700 kWh ist Überschuss. Der Netzbezug liegt bei 2.000 kWh. In einer lokalen EEG landen vom Überschuss
typisch 60 bis 70 Prozent bei anderen Mitgliedern.</p>
{A.table(
    ["Position", "Ohne EG", "Mit lokaler EEG*"],
    [
        ["Einspeisung 4.700 kWh", "zum OeMAG-Tarif: 289 € (Juli-Wert 6,146 ct) bis 699 € (Oktober-Wert 14,874 ct)",
         "3.000 kWh zu 10 ct + 1.700 kWh zum OeMAG-Tarif: 404 € (Juli-Wert) bis 553 € (Oktober-Wert)"],
        ["Netzbezug 2.000 kWh, davon 600 kWh aus EG", "Netzentgelt voll",
         "600 kWh mit minus 57 % Netz, ohne E-Abgabe (1,5 ct, Stand 2027): ca. 40 € gespart"],
        ["Vorteil pro Jahr", "", "ca. 150 bis 180 € beim Juli-Wert, beim Oktober-Wert rund 105 € weniger als ohne EG; "
         "sicher sind die rund 40 € beim Bezug"],
    ],
    hl_cols=(2,),
)}
<p>Die laufende Ersparnis wirkt auf den ersten Blick bescheiden, und sie hängt beim Erzeugeranteil am OeMAG-Tarif,
der jeden Monat neu festgelegt wird: Die Spalten rechnen den Juli- und den Oktober-Wert aufs ganze Jahr hoch und
zeigen damit nur die Bandbreite. Verlässlich ist der Bezugsvorteil, und dieser Hebel wächst mit jeder Tariferhöhung
beim Netzentgelt. Rechnen Sie Ihre Zahlen
im {a('eg_rechner', 'EG-Rechner')} nach.</p>
<p><small>*Beispielkonditionen: EG-Einspeisepreis 10 Cent je kWh, Netzentgelt-Richtwerte 2026 (SNE-VO, gilt bis
Ende 2026; die Höhe ab 2027 legt die E-Control neu fest), Elektrizitätsabgabe 1,5 Cent (Stand 2027; 2026 für
Haushalte befristet 0,1 Cent, dafür noch rund 1 Cent Förderbeitrag, im Ergebnis ähnlich). Jede Gemeinschaft legt ihre Preise selbst fest, die
Zuordnungsquote hängt von Erzeugern und Abnehmern im Nahbereich ab.</small></p>
"""),
        ("Fazit: Energiegemeinschaft Steiermark", "fazit", f"""
<p>In der Steiermark ist der Einstieg in eine Energiegemeinschaft gut vorbereitet: regionale Gemeinschaften in
vielen Bezirken, veröffentlichte Preise, ein Quick Check des Netzbetreibers und eine kostenlose Beratungsstelle.
Bis Ende 2026 bringt nur die lokale oder regionale EEG den Netzentgelt-Abschlag, ab 2027 kommen weitere Modelle
dazu. Wer jetzt eine {a('photovoltaik', 'PV-Anlage')} plant, sollte die Gemeinschaft von Anfang an mitdenken. Wer
schon eine hat, kann in wenigen Wochen {a('/energiegemeinschaft-beitreten/', 'beitreten')}. Was das für
Privathaushalte konkret heißt, zeigt der Ratgeber
{a('/energiegemeinschaft-privat/', 'Energiegemeinschaft für Privathaushalte')}; umgesetzte Anlagen finden Sie in
unseren {a('referenzen', 'Referenzen')}.</p>
{A.cta("Ihre Anlage, Ihre Gemeinschaft, ein Ansprechpartner",
       "EBZ Energie plant die Anlage, beantragt die Förderung und bringt Sie in die passende "
       "Energiegemeinschaft.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("eg_privat", "Zur Leistungsseite"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Energiegemeinschaft in der Steiermark: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und Wallboxen in "
                 "Kärnten und der Steiermark, mit zertifizierten Fachkräften. Dazu kommt "
                 "die Energiegemeinschaft: Wir nehmen Sie in eine bestehende Gemeinschaft auf oder bauen mit Ihnen eine "
                 "eigene auf, abgerechnet über die Plattform unseres Partners energyfamily. Einzugsgebiet Steiermark: "
                 "Graz und Graz-Umgebung, Leibnitz, Deutschlandsberg, Voitsberg, Weiz, Murtal, Leoben, "
                 "Bruck-Mürzzuschlag, Südoststeiermark und Umgebung."),
        "grid": [
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EG-Anbindung vom selben Team."),
            ("Förderstand geprüft", "Stand von Bund und steirischen Landesprogrammen vor dem Angebot geklärt, Blick auf 2027."),
            ("Abrechnung inklusive", "Zählpunktfreigabe, Aufnahme und monatliche Abrechnung über energyfamily."),
            ("Kostenlose Erstberatung", "Wir prüfen Netzgebiet, Eignung und Ihr Einsparpotenzial."),
        ],
    },

    "faq": [
        ("Gibt es in der Steiermark eine Förderung für die Energiegemeinschaft?",
         "Derzeit nicht. Der frühere Bonus von 125 Euro je kWp für PV-Anlagen in einem dezentralen Energiesystem "
         "war Teil der PV-Ausschreibung des Ökofonds (Anlagen ab 20 kWp mit Doppelnutzung). Der Ökofonds hat derzeit "
         "keine PV-Ausschreibung (Stand 10. Oktober 2026). Für die Teilnahme allein gibt es keine eigene Prämie."),
        ("Welcher Netzbetreiber ist für mich zuständig?",
         "In Graz-Stadt die Stromnetz Graz GmbH, im Großteil des Landes die Energienetze Steiermark GmbH, regional "
         "auch andere Betreiber wie die Feistritzwerke rund um Gleisdorf oder die Stadtwerke Voitsberg. Die "
         "Zuordnung steht auf Ihrer Netzrechnung. Im Gebiet der Energienetze Steiermark zeigt der Quick Check "
         "unter portal.e-netze.at/nahbereich vorab, mit wem Sie lokal oder regional verbunden sein können."),
        ("Was ändert das ElWG für Energiegemeinschaften in der Steiermark?",
         "Seit 1. Oktober 2026 gibt es fünf Modelle: GEA, EEG, BEG, Peer-to-Peer und Eigenversorgung, mit einem "
         "Zählpunkt an bis zu fünf Modellen gleichzeitig. Bis Ende 2026 bekommen nur Mitglieder lokaler und "
         "regionaler EEGs den reduzierten Netzarbeitspreis (minus 57 % lokal, minus 28 % regional). BEG, "
         "Peer-to-Peer und Eigenversorgung im Nahbereich sollen nach heutigem Stand ab 1.1.2027 folgen, die Höhe "
         "legt die E-Control fest. Neue Zuordnungen über mehrere Netzbetreiber sind voraussichtlich ab April 2027 "
         "möglich."),
        ("Wie gründe ich eine Energiegemeinschaft in der Steiermark?",
         "Eine EEG braucht eine Rechtsform, in der Steiermark meist Verein oder Genossenschaft. Registriert wird "
         "über ebUtilities.at bei der EDA, Marktpartner- und Gemeinschafts-ID werden zentral vergeben; danach meldet "
         "der Netzbetreiber die Zählpunkte an und die Teilnehmer bestätigen im Serviceportal. Kostenlose "
         "Gründungsberatung gibt die Beratungsstelle der Energie Agentur Steiermark (+43 316 269 700 0, Montag und "
         "Mittwoch 13 bis 16 Uhr). EBZ übernimmt auf Wunsch Planung der Erzeugungsanlage, Gründung im Nahbereich "
         "und Abrechnung über energyfamily."),
        ("Wie funktioniert die Abrechnung in einer Energiegemeinschaft?",
         "Der Smart Meter misst in Viertelstunden, welcher Teil Ihres Verbrauchs zeitgleich aus der Gemeinschaft "
         "kommt, der Netzbetreiber übermittelt die Werte über die EDA an die Gemeinschaft. Diese verrechnet die "
         "zugeordneten kWh zu ihrem eigenen Preis, je nach Gemeinschaft monatlich oder quartalsweise; den Rest "
         "liefert weiter Ihr Lieferant. Den Netzentgelt-Abschlag der EEG zieht der Netzbetreiber direkt auf der "
         "Netzrechnung ab. Bei EBZ läuft die Abrechnung über die Plattform energyfamily."),
        ("Was passiert mit meinem Strom, wenn in der Gemeinschaft niemand Bedarf hat?",
         "Er wird wie bisher an die OeMAG oder Ihren Einspeisevertragspartner geliefert und zum dortigen Tarif "
         "vergütet, im Juli 2026 waren das 6,146 Cent je kWh, im Oktober 2026 14,874 Cent. Sie verlieren also "
         "nichts gegenüber heute."),
        ("Wie lange dauert der Beitritt?",
         "Vom Erstgespräch bis zur ersten zugeordneten Kilowattstunde vergehen in der Regel vier bis acht Wochen. "
         "Der größte Zeitfaktor ist die Zählpunktanmeldung beim Netzbetreiber."),
        ("Muss ich meinen Stromlieferanten wechseln?",
         "Für eine EEG nicht: Ihr Vertrag mit Energie Steiermark oder einem anderen Lieferanten bleibt unverändert, "
         "die Gemeinschaft deckt nur den Anteil, der zeitgleich in der Gemeinschaft erzeugt wird. Anders bei "
         "Lieferantenplattformen: smartCOMMUNITY setzt laut Energie Steiermark einen Strombezugstarif der Energie "
         "Steiermark voraus."),
        ("Kann ich Strom auch mit Verwandten außerhalb der Steiermark teilen?",
         "Grundsätzlich ja, etwa über eine Bürgerenergiegemeinschaft, die sich über ganz Österreich erstrecken darf, "
         "zum Beispiel mit Familie in Wien. In der Übergangsphase seit Oktober 2026 lassen sich neue Zuordnungen "
         "laut Koordinationsstelle aber nur mit Zählpunkten beim selben Netzbetreiber umsetzen, netzübergreifend "
         "voraussichtlich ab April 2027. Einen Netzentgelt-Abschlag gibt es außerhalb des Nahbereichs nicht. EBZ "
         "bietet beide Varianten an."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und errichtet Photovoltaik-, "
                    "Speicher- und Wärmepumpensysteme in Kärnten und der Steiermark und begleitet Kunden beim Einstieg "
                    "in Energiegemeinschaften. Inhalte werden regelmäßig anhand der Vorgaben von E-Control, OeMAG und "
                    "energiegemeinschaften.gv.at aktualisiert. Keine Rechts- oder Steuerberatung, maßgeblich sind die "
                    "Förderrichtlinien des Landes Steiermark und die Tarifblätter der jeweiligen Gemeinschaft."),
    "sources": [
        ("Koordinationsstelle: FAQs zum ElWG", "https://energiegemeinschaften.gv.at/faqs-zum-elwg/"),
        ("Koordinationsstelle: Bürgerenergiegemeinschaft",
         "https://energiegemeinschaften.gv.at/buergerenergiegemeinschaft/"),
        ("Koordinationsstelle: Peer-to-Peer", "https://energiegemeinschaften.gv.at/peer-to-peer/"),
        ("Koordinationsstelle: Mehrfachteilnahme", "https://energiegemeinschaften.gv.at/mehrfachteilnahme/"),
        ("Parlament: Nationalrat beschließt Senkung der Elektrizitätsabgabe",
         "https://www.parlament.gv.at/aktuelles/news/Nationalrat-beschliesst-Senkung-der-Elektrizitaetsabgabe"),
        ("BMF: Aussetzung von Ökostrompauschale und Förderbeitrag 2027",
         "https://www.bmf.gv.at/presse/pressemeldungen/2026/november-2026/oekostrompauschale.html"),
        ("Koordinationsstelle: Änderungen für bestehende EGs",
         "https://energiegemeinschaften.gv.at/aenderungen-fuer-bestehende-energiegemeinschaften/"),
        ("Koordinationsstelle: Strom verbindet (Suche nach Gemeinschaften)",
         "https://stromverbindet.energiegemeinschaften.gv.at/"),
        ("Energienetze Steiermark: Energiegemeinschaften und Bürgerenergiemodelle",
         "https://www.e-netze.at/energiegemeinschaften"),
        ("Energie Agentur Steiermark: Beratungsstelle Energiegemeinschaften",
         "https://www.ea-stmk.at/eag/energiegemeinschaften/"),
        ("Energieinitiative Steiermark: Energiegemeinschaften und Preise", "https://energieinitiative.at/"),
        ("EEG Premstätten (Mitgliedsverein der EEG Steiermark): Tarife", "https://www.eeg-premstaetten.at/tarife"),
        ("EG Aichfeld", "https://www.eg-aichfeld.at/"),
        ("Energie Steiermark: smartCOMMUNITY", "https://www.e-steiermark.com/smartcommunity"),
        ("MeinBezirk Voitsberg: EEG Rosental, Juli 2026",
         "https://www.meinbezirk.at/voitsberg/c-wirtschaft/regionalstrom-fuer-zwei-millionen-e-auto-kilometer_a8791305"),
        ("E-Control: Energiegemeinschaften", "https://www.e-control.at/energiegemeinschaften"),
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/marktpreis"),
    ],
    "related": [
        ("/energiegemeinschaft-kaernten/", "Energiegemeinschaft Kärnten"),
        ("/energiegemeinschaft-finden/", "Energiegemeinschaft finden"),
        ("/oemag-einspeisetarif/", "OeMAG-Einspeisetarif und die Alternative"),
        ("foerderung_steiermark", "Photovoltaik-Förderung Steiermark 2026"),
    ],
    "cta": {
        "h3": "Eignung prüfen lassen",
        "text": "Wir planen Anlage, Förderung und Energiegemeinschaft aus einer Hand und prüfen Netzgebiet und Einsparpotenzial.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Mehr aus jeder steirischen Kilowattstunde",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team, das PV-Anlage, Förderung und "
                   "Energiegemeinschaft in der Steiermark aus einer Hand übernimmt."),
}
