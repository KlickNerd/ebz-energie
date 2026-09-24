"""Ratgeber: Energiegemeinschaft, Kosten und Abrechnung.

Migriert von ebz-photovoltaik.at/energiegemeinschaft-kosten/ (Stand August 2026),
Struktur nach Ratgeber-Vorlage, Beispielwerte gekennzeichnet.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "energiegemeinschaft-kosten",
    "path": "/energiegemeinschaft-kosten/",
    "title": "Energiegemeinschaft: Kosten und Abrechnung | EBZ Energie",
    "description": ("Was eine Energiegemeinschaft kostet: 2 bis 8 € je Zählpunkt und Monat, Verein ab ca. 50 €, "
                    "meist keine Einrichtungsgebühr. Plus: die 3 Rechnungen nach Beitritt."),
    "eyebrow": "Energiegemeinschaft · Kosten",
    "crumb_label": "Kosten und Abrechnung",
    "h1": "Was eine Energiegemeinschaft kostet: 25 bis 100 Euro im Jahr, und wie abgerechnet wird",
    "lead": ("Mitgliedsbeitrag, Plattformgebühr, Vereinskosten: Die Energiegemeinschaft ist günstig, aber nicht "
             "gratis. Hier ist die vollständige Kostenseite und der Weg des Geldes vom Smart Meter bis zur "
             "Gutschrift."),
    "chips": [
        "Beitritt: meist <b>0 €</b> Einrichtung",
        "Laufend: <b>2 bis 8 €</b> je Monat",
        "Vereinsgründung: <b>ca. 50 bis 150 €</b>",
        "<b>3 Rechnungen:</b> Netz, Lieferant, EG",
    ],
    "date_published": "2026-08-25",
    "date_modified": "2026-09-24",
    "hero_img": "gen_detail",
    "hero_alt": "Montagedetail einer Photovoltaikanlage, deren Überschuss in einer Energiegemeinschaft abgerechnet wird",

    "tldr": [
        "Für den Beitritt fallen üblicherweise keine Einrichtungskosten an. Laufend zahlen Mitglieder 2 bis 8 Euro "
        "je Zählpunkt und Monat für Plattform und Abrechnung, manchmal stattdessen 0,5 bis 2 Cent je "
        "abgerechneter Kilowattstunde.",
        "Die Gründung kostet als Verein etwa 50 bis 150 Euro, als Genossenschaft mehrere hundert Euro plus "
        "Revisionsverband. Registrierung bei ebutilities und Netzbetreibervertrag sind kostenlos. Der echte "
        "Aufwand steckt in Verwaltung und Abrechnung.",
        "Nach dem Beitritt bekommen Sie drei Rechnungen: Netzbetreiber (mit reduziertem EG-Anteil), Lieferant "
        "(Reststrom) und Gemeinschaft (EG-Strom). Plattformen wie energyfamily fassen die Gemeinschaftsseite "
        "monatlich in einer App zusammen.",
        "Bei typisch 100 bis 300 Euro Jahresvorteil bleibt nach Abzug von 25 bis 100 Euro Kosten ein klares "
        "Plus, sofern die Zuordnungsquote stimmt.",
    ],
    "kpis": [
        ("0 €", "Einrichtungsgebühr bei den meisten Gemeinschaften"),
        ("2 bis 8 €", "je Zählpunkt und Monat für Plattform und Abrechnung"),
        ("25 bis 100 €", "Gesamtkosten eines Mitglieds im Jahr"),
        ("100 bis 300 €", "typischer Jahresvorteil laut Erfahrungsberichten"),
    ],

    "sections": [
        ("Die Kostenarten im Überblick", "kostenarten", f"""
<p>Die Kosten einer Energiegemeinschaft verteilen sich auf Mitglieder, Gründer und die Gemeinschaft selbst.
Die meisten Positionen sind klein oder kostenlos, entscheidend ist die laufende Gebühr für Abrechnung
und Plattform.</p>
{A.table(
    ["Kostenart", "Wer zahlt", "Typische Höhe", "Anmerkung"],
    [
        ["Einrichtungsgebühr Beitritt", "Mitglied", "0 bis 50 €", "bei den meisten Gemeinschaften keine"],
        ["Mitgliedsbeitrag / Plattformgebühr", "Mitglied", "2 bis 8 € je Zählpunkt und Monat",
         "alternativ 0,5 bis 2 ct je abgerechneter kWh"],
        ["Vereinsgründung", "Gründer", "ca. 50 bis 150 €", "Vereinsregister, Statuten, Konto"],
        ["Genossenschaftsgründung", "Gründer", "mehrere hundert € plus Revisionsverband jährlich",
         "nur für größere Gemeinschaften sinnvoll"],
        ["Marktteilnehmer-Registrierung (ebutilities)", "Gemeinschaft", "kostenlos", "Pflicht für jede EG"],
        ["Vertrag mit Netzbetreiber", "Gemeinschaft", "kostenlos", "Kärnten Netz, Energienetze Steiermark usw."],
        ["Smart-Meter-Opt-in", "Mitglied", "kostenlos", "Viertelstundenwerte aktivieren"],
        ["Steuerberatung, Buchhaltung", "Gemeinschaft", "0 bis einige hundert € jährlich", "bei Vereinen oft ehrenamtlich"],
    ],
    hl_cols=(2,),
)}
<p>Unterm Strich zahlt ein Mitglied für die Teilnahme 25 bis 100 Euro im Jahr. Dem stehen laut
Erfahrungsberichten typische Vorteile von 100 bis 300 Euro gegenüber. Die Rechnung geht also auf,
solange die Zuordnungsquote nicht im Keller liegt. Wovon die Quote abhängt, erklärt der Artikel
{a('/energiegemeinschaft-nachteile/', 'Energiegemeinschaft: Nachteile')}.</p>
"""),
        ("Gebührenmodelle: Pauschale oder je Kilowattstunde", "gebuehrenmodelle", f"""
<p>Zwei Modelle haben sich etabliert. Die Pauschale je Zählpunkt ist planbar und für Vielverbraucher
günstiger. Der Aufschlag je abgerechneter Kilowattstunde ist für kleine Abnehmer günstiger, weil sie nur
zahlen, wenn tatsächlich Strom zugeordnet wird. Manche Plattformen kombinieren beides oder staffeln nach
Gemeinschaftsgröße. Fragen Sie vor dem Beitritt nach dem Modell und rechnen Sie es mit Ihrer
voraussichtlichen Zuordnungsmenge durch. Bei EBZ nennen wir die Konditionen im Erstgespräch, bevor Sie
unterschreiben.</p>
{A.table(
    ["Modell", "Beispiel*", "Kosten bei 1.000 kWh Zuordnung", "Kosten bei 3.000 kWh Zuordnung", "Günstiger für"],
    [
        ["Pauschale je Zählpunkt", "4 € je Monat", "48 € im Jahr", "48 € im Jahr", "Vielverbraucher, Wärmepumpe, E-Auto"],
        ["Aufschlag je kWh", "1,5 ct je abgerechneter kWh", "15 € im Jahr", "45 € im Jahr", "kleine Abnehmer, Wohnungen"],
    ],
    hl_cols=(2, 3),
)}
{A.box("Liegt die jährliche Gebühr über 30 Prozent Ihres erwarteten Vorteils, passt die Gemeinschaft nicht "
       "zu Ihrem Verbrauchsprofil. Dann lohnt sich ein anderes Gebührenmodell oder eine andere Gemeinschaft.",
       label="Faustregel:")}
<p><small>*Beispielwerte innerhalb der marktüblichen Spannen (2 bis 8 Euro je Monat, 0,5 bis 2 Cent je kWh).
Die tatsächlichen Konditionen legt jede Gemeinschaft selbst fest.</small></p>
"""),
        ("Wie die Abrechnung technisch funktioniert", "abrechnung", f"""
<p>Die Abrechnung einer Energiegemeinschaft läuft in drei Schritten, von denen Sie nur den letzten sehen.
Der Strom fließt physisch wie bisher durchs Netz. Neu ist nur die Zuordnung per Smart Meter und die
Abrechnung zum EG-Preis.</p>
{A.steps([
    ("Messung",
     "Der Smart Meter jedes Teilnehmers erfasst Einspeisung und Bezug in Viertelstundenwerten und "
     "übermittelt sie an den Netzbetreiber. Dafür muss das Opt-in für Viertelstundenwerte aktiv sein."),
    ("Zuordnung durch den Netzbetreiber",
     "Für jede Viertelstunde rechnet der Netzbetreiber aus, wie viel Erzeugung in der Gemeinschaft auf wie "
     "viel Verbrauch trifft, und verteilt sie nach dem Aufteilungsschlüssel (statisch oder dynamisch). Das "
     "Ergebnis stellt er der Gemeinschaft über das EDA-Portal zur Verfügung."),
    ("Verrechnung durch die Gemeinschaft",
     "Die Gemeinschaft oder ihre Plattform multipliziert die zugeordneten Mengen mit den vereinbarten "
     "Preisen, schreibt Erzeugern gut und stellt Abnehmern in Rechnung. Bei energyfamily passiert das "
     "monatlich, mit Übersicht in der App."),
])}
{A.net([
    ("☀", "PV-Erzeuger", "Überschuss tagsüber ins öffentliche Netz"),
    ("◷", "Smart Meter", "misst Viertelstundenwerte, Netzbetreiber ordnet zu"),
    ("⌂", "Abnehmer in der Nähe", "Haushalte, Betriebe, Gemeinde, Netzentgelt reduziert"),
    ("€", "Abrechnung über die Plattform", "EG-Strom zum vereinbarten Preis, Rest wie gewohnt"),
], "So fließt der Strom in der Energiegemeinschaft",
   "Der Netzbetreiber liefert die zugeordneten Mengen, die Plattform (bei EBZ: energyfamily) macht daraus "
   "Gutschriften und Rechnungen. Rest wie gewohnt über Netzbetreiber und Lieferant.")}
"""),
        ("Die drei Rechnungen nach dem Beitritt", "drei-rechnungen", f"""
<p><b>Netzbetreiber:</b> Die Netzrechnung weist den EG-Bezug gesondert mit reduziertem Netznutzungs- und
Netzverlustentgelt aus, bei Erneuerbaren-Energie-Gemeinschaften zusätzlich ohne Elektrizitätsabgabe und
Förderbeitrag. Die Grundpauschale bleibt unverändert. Welche Positionen genau sinken, steht im Artikel
{a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft und Netzkosten')}.</p>
<p><b>Lieferant:</b> Ihr Stromlieferant verrechnet nur noch den Reststrom, der nicht aus der Gemeinschaft kam.
Die Energiemenge auf dieser Rechnung sinkt entsprechend. Wer einen Tarif mit Mindestabnahme oder
Grundgebühr hat, sollte prüfen, ob sich der Tarif noch rechnet.</p>
<p><b>Gemeinschaft:</b> Die dritte Rechnung kommt von der Energiegemeinschaft selbst. Abnehmer zahlen den
EG-Preis je zugeordneter Kilowattstunde plus Mitgliedsbeitrag, Erzeuger bekommen eine Gutschrift. Die
Umsatzsteuer hängt von der Rechtsform ab: Vereine unter der Kleinunternehmergrenze rechnen ohne
Umsatzsteuer ab, größere Gemeinschaften mit.</p>
{A.cta("Transparente Konditionen statt Kleingedrucktem",
       "EBZ nennt Ihnen Einspeisepreis, Bezugspreis und Gebühr vor dem Beitritt. Keine Einrichtungsgebühr, "
       "kurze Kündigungsfrist.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("eg_rechner", "Ersparnis berechnen"))}
"""),
        ("Was bei der Preisfestlegung zu beachten ist", "preise", f"""
<p>Die Gemeinschaft legt Einspeise- und Bezugspreis selbst fest. Drei Regeln haben sich bewährt. Erstens:
Der Einspeisepreis sollte deutlich über dem OeMAG-Marktpreis liegen (Juli 2026: 6,146 Cent), sonst fehlt
der Anreiz für Erzeuger. Zweitens: Der Bezugspreis sollte unter dem Arbeitspreis der gängigen Lieferanten
liegen, sonst fehlt der Anreiz für Abnehmer. Drittens: Die Differenz zwischen beiden deckt die
Gemeinschaftskosten.</p>
{A.table(
    ["Preis", "Marktübliche Spanne", "Beispielwert*", "Vergleichswert"],
    [
        ["EG-Einspeisepreis (Erzeuger bekommt)", "8 bis 12 ct", "10 ct", "OeMAG Juli 2026: 6,146 ct"],
        ["EG-Bezugspreis (Abnehmer zahlt)", "12 bis 16 ct", "14 ct", "Lieferant Arbeitspreis: 12 bis 20 ct netto"],
        ["Differenz (deckt Verwaltung)", "2 bis 4 ct", "4 ct", "plus Mitgliedsbeitrag 2 bis 8 € je Monat"],
    ],
    hl_cols=(2,),
)}
<p>Wie sich das gegen den OeMAG-Tarif rechnet, zeigt der Artikel
{a('/oemag-einspeisetarif/', 'OeMAG-Einspeisetarif 2026')}. Wer die Anlage über EBZ plant, bekommt die
Preise der Gemeinschaft im Erstgespräch genannt, nicht erst im Vertrag.</p>
<p><small>*Beispielwerte aus dem Markt. Jede Gemeinschaft legt ihre Preise selbst fest, die Konditionen von
EBZ erfahren Sie im Erstgespräch.</small></p>
"""),
        ("Versteckte Kosten und wie Sie sie vermeiden", "versteckte-kosten", f"""
<p>Vier Punkte tauchen in Verträgen auf, die Sie vorher lesen sollten:</p>
<ul>
  <li><b>Jahresbindungen</b> mit automatischer Verlängerung. Üblich und fair sind Kündigungsfristen von ein
  bis drei Monaten zum Monatsende.</li>
  <li><b>Preisklauseln,</b> die den Einspeisepreis an den OeMAG-Tarif koppeln, sodass er mitsinkt.</li>
  <li><b>Kopplungen</b> an ein bestimmtes Stromprodukt oder Konto desselben Anbieters.</li>
  <li><b>Gebühren für den Austritt</b> oder die Zählpunktabmeldung, die es bei seriösen Gemeinschaften nicht gibt.</li>
</ul>
{A.box_dark("Vor der Unterschrift prüfen",
    "Gebührenmodell, Einspeise- und Bezugspreis, Aufteilungsschlüssel und Kündigungsfrist. Diese vier "
    "Angaben müssen im Mitgliedsvertrag stehen. Fehlt eine davon, fragen Sie nach, bevor Sie den "
    "Zählpunkt freigeben. Den Ablauf des Beitritts beschreibt der Artikel " +
    a('/energiegemeinschaft-beitreten/', 'Energiegemeinschaft beitreten') + ".")}
"""),
        ("Fazit: Kosten und Abrechnung", "fazit", f"""
<p>Eine Energiegemeinschaft kostet ein Mitglied 25 bis 100 Euro im Jahr und bringt typisch das Drei- bis
Zehnfache zurück. Die Abrechnung ist komplexer als eine normale Stromrechnung, aber eine gute Plattform
macht sie unsichtbar. Entscheidend ist, dass Sie Gebührenmodell, Preise und Kündigungsfrist vor dem
Beitritt kennen.</p>
{A.cta("Kosten und Nutzen für Ihren Haushalt",
       "Der Rechner zeigt Ihren erwarteten Jahresvorteil. Die Konditionen von EBZ erfahren Sie im Erstgespräch.",
       primary=("eg_rechner", "Zum Rechner"), secondary=("kontakt", "Konditionen anfragen"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Energiegemeinschaft: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und Wallboxen "
                 "in Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. "
                 "Dazu kommt die Energiegemeinschaft: Wir nehmen Sie in eine bestehende Gemeinschaft auf oder bauen "
                 "mit Ihnen eine eigene auf, abgerechnet über die Plattform unseres Partners energyfamily mit rund "
                 "330 Gemeinschaften und rund 15.000 Nutzern."),
        "grid": [
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EG-Anbindung vom selben Team."),
            ("Regional verankert", "Sitz in Villach, Montage in ganz Kärnten und der Steiermark."),
            ("Abrechnung inklusive", "Zählpunktfreigabe, Aufnahme und monatliche Abrechnung über energyfamily."),
            ("Konditionen vorab", "Einspeisepreis, Bezugspreis und Gebühr nennen wir vor dem Beitritt."),
        ],
    },

    "faq": [
        ("Was kostet die Teilnahme an einer Energiegemeinschaft?",
         "Laufend 2 bis 8 Euro je Zählpunkt und Monat oder ein Aufschlag von 0,5 bis 2 Cent je abgerechneter "
         "Kilowattstunde. Einrichtungsgebühren sind unüblich. Im Jahr sind das 25 bis 100 Euro."),
        ("Was kostet es, eine Energiegemeinschaft zu gründen?",
         "Als Verein etwa 50 bis 150 Euro für Vereinsregister, Statuten und Konto, die Registrierung bei "
         "ebutilities und der Netzbetreibervertrag sind kostenlos. Eine Genossenschaft kostet mehrere hundert Euro "
         "und verlangt eine jährliche Revisionsverbandsmitgliedschaft. Der Hauptaufwand ist die Abrechnung."),
        ("Wie wird der Strom in der Energiegemeinschaft abgerechnet?",
         "Der Netzbetreiber ordnet jede Viertelstunde Erzeugung und Verbrauch in der Gemeinschaft zu und "
         "übermittelt die Mengen über das EDA-Portal. Die Gemeinschaft oder ihre Plattform verrechnet sie zu den "
         "vereinbarten Preisen, schreibt Erzeugern gut und stellt Abnehmern in Rechnung, meist monatlich."),
        ("Bekomme ich mehrere Stromrechnungen?",
         "Ja, drei: vom Netzbetreiber (mit reduziertem EG-Anteil), vom Lieferanten (Reststrom) und von der "
         "Gemeinschaft (EG-Strom). Plattformen wie energyfamily fassen die Gemeinschaftsrechnung in einer App "
         "zusammen."),
        ("Welche Preise sind in einer Energiegemeinschaft üblich?",
         "Typisch sind 8 bis 12 Cent Einspeisung und 12 bis 16 Cent Bezug je Kilowattstunde. Der Einspeisepreis "
         "liegt damit deutlich über dem OeMAG-Marktpreis von 6,146 Cent (Juli 2026), der Bezugspreis unter dem "
         "Arbeitspreis der meisten Lieferanten. Die Differenz deckt die Gemeinschaftskosten."),
        ("Fällt auf den EG-Strom Umsatzsteuer an?",
         "Das hängt von der Rechtsform der Gemeinschaft ab. Vereine unter der Kleinunternehmergrenze rechnen ohne "
         "Umsatzsteuer ab, größere Gemeinschaften weisen sie aus. Für Privatpersonen als Erzeuger gilt bis "
         "12.500 kWh und 35 kWp die Einkommensteuerbefreiung. Keine Steuerberatung."),
        ("Lohnt sich die Gemeinschaft trotz Gebühr?",
         "Bei 25 bis 100 Euro Kosten und typisch 100 bis 300 Euro Vorteil im Jahr ja. Kritisch wird es erst, "
         "wenn die Gebühr über 30 Prozent des erwarteten Vorteils liegt, etwa bei sehr geringer Zuordnungsquote. "
         "Dann passt ein anderes Gebührenmodell oder eine andere Gemeinschaft besser."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert PV-Anlagen, "
                    "Speicher und Wärmepumpen in Kärnten und der Steiermark und begleitet Kunden beim Einstieg in "
                    "Energiegemeinschaften. Die Inhalte werden anhand der Vorgaben von E-Control, OeMAG und "
                    "energiegemeinschaften.gv.at aktualisiert. Keine Rechts- oder Steuerberatung."),
    "sources": [
        ("Koordinationsstelle: Gründungs-Guide", "https://energiegemeinschaften.gv.at/online-guide/"),
        ("Koordinationsstelle: Ratgeber Rechtsformen (PDF)",
         "https://energiegemeinschaften.gv.at/wp-content/uploads/sites/19/2023/01/Ratgeber-Rechtsformen-Erneuerbare-Energie-Gemeinschaften.pdf"),
        ("E-Control: Energiegemeinschaften", "https://www.e-control.at/energiegemeinschaften"),
        ("energyfamily", "https://www.energyfamily.at/"),
    ],
    "related": [
        ("/energiegemeinschaft-netzkosten/", "Netzkosten: Was in der Energiegemeinschaft günstiger wird"),
        ("/energiegemeinschaft-beitreten/", "Energiegemeinschaft beitreten: Ablauf in vier Schritten"),
        ("/energiegemeinschaft-gruenden/", "Energiegemeinschaft gründen: Ablauf in sechs Schritten"),
        ("eg_rechner", "Energiegemeinschaft-Rechner: Jahresvorteil berechnen"),
    ],
    "cta": {
        "h3": "Konditionen vor dem Beitritt",
        "text": "Einspeisepreis, Bezugspreis, Gebühr und Kündigungsfrist: Wir nennen Ihnen alle Zahlen im Erstgespräch.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Klare Zahlen statt Kleingedrucktem",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, Montage "
                   "und EG-Anbindung aus einer Hand übernimmt."),
}
