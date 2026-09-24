"""Ratgeber: Energiegemeinschaft privat (Familie, Nachbarn, Mehrparteienhaus).

Migriert von ebz-photovoltaik.at/energiegemeinschaft-privat/ (Stand August 2026),
Struktur nach Ratgeber-Vorlage, Beispielwerte gekennzeichnet.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "energiegemeinschaft-privat",
    "path": "/energiegemeinschaft-privat/",
    "title": "Energiegemeinschaft privat: Strom mit Nachbarn teilen | EBZ",
    "description": ("Energiegemeinschaft privat: ab 2 Teilnehmern mit Familie oder Nachbarn, GEA im Mehrparteienhaus "
                    "ohne Verein, Peer-to-Peer ab 1. Oktober 2026. Modelle, Kosten."),
    "eyebrow": "Energiegemeinschaft · Privat",
    "crumb_label": "Energiegemeinschaft privat",
    "h1": "Energiegemeinschaft privat: Strom mit Nachbarn und Familie teilen, ab 2 Teilnehmern",
    "lead": ("Die Eltern haben die PV-Anlage, die Kinder wohnen drei Häuser weiter. Der Nachbar hat ein großes "
             "Dach, Sie eine Wärmepumpe. Für genau diese Fälle gibt es kleine, private Lösungen, und ab Oktober "
             "2026 eine mehr."),
    "chips": [
        "Ab <b>2 Teilnehmern</b> möglich",
        "GEA: im selben Haus <b>ohne Verein</b>",
        "Peer-to-Peer: ab <b>1. Oktober 2026</b>",
        "EEG: lokal <b>minus 57 %</b> Netzentgelt",
    ],
    "date_published": "2026-08-20",
    "date_modified": "2026-09-24",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit Photovoltaikanlage am Dach, Ausgangspunkt einer privaten Energiegemeinschaft",

    "tldr": [
        "Eine private Energiegemeinschaft ist ab zwei Teilnehmern möglich, etwa Eltern und Kinder oder zwei "
        "Nachbarn. Voraussetzung für den Netzentgelt-Abschlag ist der gemeinsame Nahbereich (selber Trafo "
        "oder selbes Umspannwerk).",
        "Im selben Gebäude, etwa im Mehrparteienhaus, braucht es keinen Verein: Die gemeinschaftliche "
        "Erzeugungsanlage (GEA) teilt den PV-Strom direkt auf die Wohnungen auf, ohne Netzentgelt.",
        "Ab 1. Oktober 2026 erlaubt das ElWG Peer-to-Peer-Verträge: Strom direkt an eine Person verkaufen "
        "oder verschenken, österreichweit und ohne Rechtsform. Die volle Abgabenbefreiung gibt es aber nur in "
        "der Erneuerbaren-Energie-Gemeinschaft (EEG).",
        "Für kleine Gruppen lohnt sich der Beitritt zu einer bestehenden Gemeinschaft oder die Gründung über "
        "eine Plattform, die Abrechnung und Verwaltung für 2 bis 8 Euro je Zählpunkt und Monat übernimmt.",
    ],
    "kpis": [
        ("2", "Teilnehmer reichen für eine Energiegemeinschaft"),
        ("57 %", "weniger Netzentgelt am selben Trafo (EEG)"),
        ("rund 400 €*", "Jahresvorteil einer Familie bei 4.000 kWh Zuordnung"),
        ("1.10.2026", "Start der Peer-to-Peer-Verträge (ElWG)"),
    ],

    "sections": [
        ("Drei Modelle für den privaten Stromtausch", "modelle", f"""
<p>Wer Strom privat teilen will, hat ab Oktober 2026 drei Wege. Welcher passt, hängt davon ab, ob die
Beteiligten im selben Gebäude wohnen, am selben Trafo hängen oder nur im selben Ort leben, und wie viel
Verwaltung man sich antun will.</p>
{A.table(
    ["Modell", "Wer kann mitmachen", "Rechtsform nötig", "Netzentgelt", "Abgaben"],
    [
        ["Gemeinschaftliche Erzeugungsanlage (GEA)", "Wohnungen im selben Gebäude oder Anschlussobjekt",
         "nein, Vereinbarung reicht", "kein Netzentgelt auf den intern verteilten Strom", "E-Abgabe entfällt"],
        ["Erneuerbare-Energie-Gemeinschaft (EEG)", "Haushalte, Betriebe, Gemeinden im Nahbereich",
         "ja, z. B. Verein", "minus 57 % lokal, minus 28 % regional", "E-Abgabe und Förderbeitrag entfallen"],
        ["Peer-to-Peer-Vertrag (ab 1.10.2026)", "zwei oder mehr Vertragspartner, österreichweit",
         "nein", "reduziert nur im Nahbereich", "bleiben"],
    ],
    hl_cols=(3, 4),
)}
<p>Die Grundlagen zu EEG und Bürgerenergiegemeinschaft (BEG) erklärt der
{a('eg', 'Leitartikel zur Energiegemeinschaft')}. Hier geht es um die drei typischen privaten
Situationen: Familie im selben Ort, Nachbarn am selben Trafo und Wohnungen im selben Haus.</p>
"""),
        ("Fall 1: Familie, ein paar Häuser auseinander", "familie", f"""
<p>Die Eltern haben 15 kWp am Dach und verbrauchen wenig, die Tochter wohnt mit Familie, Wärmepumpe und
E-Auto 200 Meter weiter. Das ist der klassische Fall für eine kleine Erneuerbare-Energie-Gemeinschaft,
sofern beide am selben Trafo hängen, was in einer Siedlung oder einem Ortsteil häufig ist. Die Eltern
verkaufen den Überschuss zum vereinbarten Preis an die Tochter, die Tochter spart Netzentgelt und
Abgaben. Bei 4.000 kWh zugeordneter Menge und den Richtwerten aus unserem
{a('/energiegemeinschaft-netzkosten/', 'Netzkosten-Artikel')} (rund 10,5 Cent Vorteil je Kilowattstunde
bei 14 Cent* EG-Preis statt 17 Cent* Lieferantenpreis) sind das rund 400 Euro* Vorteil für die Familie im
Jahr, je nachdem, wie der EG-Preis gewählt wird.</p>
<p>Zwei Personen können eine EEG gründen, der Aufwand mit Verein und Netzbetreibervertrag ist aber
derselbe wie für zwanzig. Deshalb unser Rat: Treten Sie zu zweit einer bestehenden Gemeinschaft im
Nahbereich bei oder lassen Sie die Abrechnung über eine Plattform laufen. Ab Oktober 2026 ist für diesen
Fall auch ein Peer-to-Peer-Vertrag möglich, der ohne Verein auskommt, dafür aber die Abgabenbefreiung
nicht bietet.</p>
<p><small>*Richtwerte 2026 für Netzentgelt und Abgaben laut E-Control, EG-Preise und Lieferantenpreis sind
Beispielwerte. Jede Gemeinschaft legt ihre Preise selbst fest.</small></p>
"""),
        ("Fall 2: Nachbarn am selben Trafo", "nachbarn", f"""
<p>Der Nachbar hat ein Scheunendach mit 30 kWp, Sie haben keinen Platz für PV. Auch hier ist die lokale
EEG das Mittel der Wahl. Wichtig: Große Betriebe ab 250 Mitarbeitern dürfen an einer EEG nicht
teilnehmen, ein landwirtschaftlicher Betrieb oder ein Gewerbebetrieb mit weniger Mitarbeitern schon.
Mit drei bis fünf Nachbarn als Abnehmer ist so eine Nachbarschafts-EEG schnell wirtschaftlich. Wie Sie
herausfinden, ob Sie am selben Trafo hängen, steht im Artikel
{a('/energiegemeinschaft-finden/', 'Energiegemeinschaft finden')}.</p>
{A.table(
    ["Nahbereich", "Verbindung über", "Netznutzungs- und Netzverlustentgelt (Arbeitspreis)"],
    [
        ["Lokal", "selber Trafo (Niederspannung)", "minus 57 %"],
        ["Regional", "selbes Umspannwerk (Mittelspannung)", "minus 28 %"],
        ["Außerhalb des Nahbereichs", "z. B. Verwandte in einem anderen Bundesland", "voller Tarif (BEG oder Peer-to-Peer)"],
    ],
    hl_cols=(2,),
)}
<p>Lokal bringt den größten Abschlag, regional den kleineren, jeweils auf den Arbeitspreis von
Netznutzungs- und Netzverlustentgelt (Stand 2026, E-Control). Die Grundpauschale bleibt unverändert.
Welchem Trafo und Umspannwerk Ihr Anschluss zugeordnet ist, prüft der Netzbetreiber bei der Anmeldung
über die Zählpunktnummer. EBZ übernimmt diese Abfrage im Rahmen der Erstberatung.</p>
"""),
        ("Fall 3: Mehrparteienhaus und Wohnungseigentum", "mehrparteienhaus", f"""
<p>Für Wohnungen im selben Gebäude ist die gemeinschaftliche Erzeugungsanlage (GEA) das einfachste
Modell. Die PV-Anlage am Dach wird über eine Vereinbarung auf die teilnehmenden Wohnungen aufgeteilt,
statisch nach festen Prozentsätzen oder dynamisch nach Verbrauch. Der intern verteilte Strom läuft über
den Hausanschluss, nicht über das öffentliche Netz, deshalb fällt dafür kein Netzentgelt an. Ein Verein
ist nicht nötig, wohl aber die Zustimmung der Eigentümergemeinschaft und ein Betreiber, oft die
Hausverwaltung.</p>
<p>Zusätzlich kann dieselbe Anlage an einer EEG teilnehmen, um den Überschuss des Hauses an die
Nachbarschaft zu verkaufen. Die Anlage sollte dafür von Anfang an mit ausreichend Leistung und einem
{a('batteriespeicher', 'Speicher')} geplant werden, damit der Überschuss auch abends noch etwas wert ist.</p>
{A.cta("Private Lösung prüfen lassen",
       "Ob GEA, kleine EEG oder Peer-to-Peer: EBZ prüft Nahbereich und Gebäudesituation in Kärnten und der "
       "Steiermark und schlägt das passende Modell vor.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("eg_rechner", "Ersparnis berechnen"))}
"""),
        ("Peer-to-Peer ab Oktober 2026: Was das neue Modell kann", "peer-to-peer", f"""
<p>Mit dem Elektrizitätswirtschaftsgesetz wird ab 1. Oktober 2026 der direkte Stromverkauf zwischen
Privatpersonen möglich. Ein Peer-to-Peer-Vertrag ist eine Vereinbarung zwischen zwei oder mehr
Marktteilnehmern über Verkauf oder Schenkung von erneuerbarem Strom. Es braucht keine Rechtsform, keine
geografische Grenze und keine Mindestteilnehmerzahl. Wer sich auf einen Nahbereich beschränkt, bekommt
beim Bezug reduzierte Netzentgelte. Die Befreiung von Elektrizitätsabgabe und
Erneuerbaren-Förderbeitrag bleibt aber der EEG vorbehalten. Für Betreiber bis 30 kW gilt zudem, dass sie
durch den Verkauf nicht zum Energielieferanten werden.</p>
{A.box("Peer-to-Peer wird das Modell für Einzelfälle wie Eltern und Kinder, wenn die Abgabenbefreiung "
       "keine Rolle spielt oder kein Nahbereich besteht, etwa bei Verwandten in einem anderen Bundesland. "
       "Für Nachbarschaften bleibt die EEG wirtschaftlich überlegen.", label="Unsere Einschätzung:")}
<p>Welche Marktprozesse die Netzbetreiber zum Stichtag bereitstellen, ist laut Koordinationsstelle noch
offen. Wir aktualisieren den Artikel, sobald das feststeht.</p>
"""),
        ("Was private Energiegemeinschaften kosten", "kosten", f"""
<p>Die Gründung eines Vereins kostet wenige Euro (Vereinsregister, Statuten, Konto: etwa 50 bis 150 Euro),
die Registrierung als Marktteilnehmer bei ebutilities ist kostenlos, der Vertrag mit dem Netzbetreiber
ebenfalls. Der laufende Aufwand liegt in der Abrechnung. Wer sie händisch macht, zahlt mit Zeit, wer eine
Plattform nutzt, mit 2 bis 8 Euro je Zählpunkt und Monat. Bei einer Zwei-Personen-Gemeinschaft kann das
den Vorteil spürbar schmälern, weshalb der Beitritt zu einer größeren Gemeinschaft oft sinnvoller ist.
Die Details stehen im Artikel {a('/energiegemeinschaft-kosten/', 'Energiegemeinschaft: Kosten und Abrechnung')}.</p>
<p>Eine Frage, die in Beratungen oft kommt: Darf ich meinen PV-Strom an die Kinder verschenken?
Innerhalb einer EEG ist ein Preis von null Cent möglich, ab Oktober 2026 ist die Schenkung auch per
Peer-to-Peer-Vertrag ausdrücklich vorgesehen. Netzentgelte fallen dabei weiterhin an, im Nahbereich
reduziert.</p>
"""),
        ("Fazit: Energiegemeinschaft privat", "fazit", f"""
<p>Strom in der Familie oder mit Nachbarn zu teilen ist rechtlich einfacher, als viele denken, und ab
Oktober 2026 noch einfacher. Die Wahl des Modells folgt einer klaren Logik: selbes Gebäude, dann GEA.
Selber Trafo und mehrere Teilnehmer, dann EEG. Zwei Personen ohne Nahbereich, dann Peer-to-Peer oder
Bürgerenergiegemeinschaft, allerdings ohne Netzentgelt-Rabatt. In allen Fällen gilt: Die Anlage sollte von
Anfang an auf das Teilen ausgelegt sein.</p>
{A.cta("Anlage planen, Teilen gleich mitdenken",
       "EBZ legt PV-Anlagen so aus, dass Familie und Nachbarschaft mitversorgt werden können, und übernimmt "
       "die Anbindung an die passende Gemeinschaft.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("eg_privat", "Zur Leistungsseite"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Energiegemeinschaft: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und Wallboxen "
                 "in Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. "
                 "Dazu kommt die Energiegemeinschaft: Wir nehmen Sie in eine bestehende Gemeinschaft auf oder bauen "
                 "mit Ihnen eine eigene auf, abgerechnet über die Plattform unseres Partners energyfamily."),
        "grid": [
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EG-Anbindung vom selben Team."),
            ("Regional verankert", "Sitz in Villach, Montage in ganz Kärnten und der Steiermark."),
            ("Abrechnung inklusive", "Zählpunktfreigabe, Aufnahme und monatliche Abrechnung über energyfamily."),
            ("Kostenlose Erstberatung", "Wir prüfen Netzebene, Eignung und Ihr Einsparpotenzial."),
        ],
    },

    "faq": [
        ("Können zwei Haushalte eine Energiegemeinschaft gründen?",
         "Ja, die gesetzliche Mindestgröße sind zwei Teilnehmer. Beide müssen im selben Nahbereich liegen und "
         "eine Rechtsform, etwa einen Verein, gründen. Für so kleine Gruppen ist der Beitritt zu einer "
         "bestehenden Gemeinschaft meist einfacher und günstiger."),
        ("Kann ich meinen PV-Strom an meine Kinder verschenken?",
         "Innerhalb einer EEG ist ein Preis von null Cent möglich. Ab 1. Oktober 2026 ist mit dem "
         "Peer-to-Peer-Vertrag auch eine Schenkung ohne Verein ausdrücklich vorgesehen. Netzentgelte fallen "
         "dabei weiterhin an, im Nahbereich reduziert."),
        ("Kann ich Strom mit Verwandten in einem anderen Bundesland teilen?",
         "Ja, über eine Bürgerenergiegemeinschaft oder ab Oktober 2026 per Peer-to-Peer-Vertrag ist das "
         "österreichweit möglich. Den Netzentgelt-Abschlag von 57 oder 28 Prozent und die Abgabenbefreiung "
         "gibt es dabei nicht, weil der Strom die übergeordneten Netzebenen nutzt."),
        ("Was ist der Unterschied zwischen GEA und Energiegemeinschaft?",
         "Die gemeinschaftliche Erzeugungsanlage (GEA) teilt Strom innerhalb eines Gebäudes über den "
         "Hausanschluss auf, ohne Netzentgelt und ohne Verein. Die Energiegemeinschaft teilt Strom über das "
         "öffentliche Netz zwischen verschiedenen Gebäuden, mit reduziertem Netzentgelt und einer Rechtsform."),
        ("Brauche ich für eine private Energiegemeinschaft einen Steuerberater?",
         "Für Privatpersonen mit Anlagen bis 35 kWp und Einspeiseerlösen bis 12.500 kWh im Jahr besteht "
         "Einkommensteuerbefreiung. Ein Verein als Trägerverein ist in der Regel nicht gewinnorientiert. Bei "
         "Unsicherheit empfehlen wir eine Beratung, dieser Artikel ist keine Steuerberatung."),
        ("Kann ein Bauernhof an einer privaten Energiegemeinschaft teilnehmen?",
         "Ja, landwirtschaftliche Betriebe gelten als kleine oder mittlere Unternehmen und dürfen an "
         "Erneuerbaren-Energie-Gemeinschaften teilnehmen. Sie sind mit großen Dachflächen oft die wichtigsten "
         "Erzeuger einer Nachbarschafts-EEG."),
        ("Wie viel bringt eine private Energiegemeinschaft im Jahr?",
         "Bei 4.000 kWh zugeordneter Menge und rund 10,5 Cent Vorteil je Kilowattstunde (lokale EEG, Richtwerte "
         "2026) sind es rund 400 Euro für die Familie. Abzuziehen sind 2 bis 8 Euro je Zählpunkt und Monat für "
         "die Abrechnungsplattform. Wie viel zugeordnet wird, hängt vom Verbrauchsprofil der Abnehmer ab."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert PV-Anlagen, "
                    "Speicher und Wärmepumpen in Kärnten und der Steiermark und begleitet Familien und Nachbarschaften "
                    "beim Einstieg in Energiegemeinschaften. Die Inhalte werden anhand der Vorgaben von E-Control, "
                    "OeMAG und energiegemeinschaften.gv.at aktualisiert. Keine Rechts- oder Steuerberatung."),
    "sources": [
        ("Koordinationsstelle: Peer-to-Peer-Verträge", "https://energiegemeinschaften.gv.at/peer-to-peer-vertraege/"),
        ("Koordinationsstelle: Gemeinsame Energienutzung", "https://energiegemeinschaften.gv.at/gemeinsame-energienutzung/"),
        ("E-Control: Energiegemeinschaften", "https://www.e-control.at/energiegemeinschaften"),
        ("Koordinationsstelle: FAQs", "https://energiegemeinschaften.gv.at/faqs/"),
    ],
    "related": [
        ("/energiegemeinschaft-gruenden/", "Energiegemeinschaft gründen: Ablauf in sechs Schritten"),
        ("/energiegemeinschaft-kosten/", "Energiegemeinschaft: Kosten und Abrechnung"),
        ("/energiegemeinschaft-finden/", "Energiegemeinschaft finden: Nahbereich prüfen"),
        ("eg_privat", "Energiegemeinschaft mit EBZ: Leistungsseite für Privatkunden"),
    ],
    "cta": {
        "h3": "Welches Modell passt zu Ihnen?",
        "text": "GEA, kleine EEG oder Peer-to-Peer: Wir prüfen Nahbereich und Gebäude und sagen Ihnen, was sich rechnet.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Strom teilen in Familie und Nachbarschaft",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, Montage "
                   "und EG-Anbindung aus einer Hand übernimmt."),
}
