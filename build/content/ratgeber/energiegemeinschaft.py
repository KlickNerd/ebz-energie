"""Ratgeber (Pillar): Energiegemeinschaft in Österreich.

Migriert von ebz-photovoltaik.at/energiegemeinschaft/ und als Leitartikel des
EG-Clusters ausgebaut: Inhalte aus den Cluster-Artikeln (Netzkosten, Beitreten,
Kosten, Kärnten, OeMAG) sind hier zusammengefasst und verlinkt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "energiegemeinschaft",
    "path": "/energiegemeinschaft/",
    "title": "Energiegemeinschaft: Strom teilen und sparen | EBZ Energie",
    "description": ("Energiegemeinschaft erklärt: EEG, BEG, GEA und Peer-to-Peer, bis zu 57 % weniger Netzentgelt, "
                    "8 bis 12 ct statt 6,146 ct OeMAG. Ablauf, Kosten, Nachteile."),
    "eyebrow": "Energiegemeinschaft · Leitartikel",
    "crumb_label": "Energiegemeinschaft",
    "h1": "Energiegemeinschaft in Österreich: Solarstrom teilen und bis zu 57 % Netzentgelt sparen",
    "lead": ("In einer Energiegemeinschaft verkaufen PV-Besitzer ihren Überschuss zu einem selbst vereinbarten "
             "Preis an Haushalte und Betriebe in der Nähe, statt ihn zum OeMAG-Marktpreis abzugeben. Dieser "
             "Leitartikel erklärt die Modelle, die Ersparnis, den Ablauf und die Grenzen, mit Links zu allen "
             "Detailartikeln."),
    "chips": [
        "Netzentgelt: bis zu <b>57 %</b> weniger",
        "EG-Einspeisepreis: <b>8 bis 12 ct</b>",
        "OeMAG Juli 2026: <b>6,146 ct</b>",
        "Über <b>11.000</b> Gemeinschaften in Österreich",
    ],
    "date_published": "2026-07-22",
    "date_modified": "2026-09-24",
    "hero_img": "eg_drohne",
    "hero_alt": "Ortschaft mit Photovoltaik auf mehreren Dächern, typisches Netzgebiet einer lokalen Energiegemeinschaft",

    "tldr": [
        "Eine Energiegemeinschaft ist ein Zusammenschluss von mindestens zwei Teilnehmern, die Strom aus "
        "erneuerbaren Quellen gemeinsam erzeugen, teilen und verbrauchen. Der Strom fließt physisch wie bisher "
        "durchs Netz, neu ist nur die Zuordnung per Smart Meter und die Abrechnung zum EG-Preis.",
        "Abnehmer sparen auf den zugeordneten Strom 57 Prozent (lokal) oder 28 Prozent (regional) des "
        "Arbeitspreises von Netznutzungs- und Netzverlustentgelt. In einer Erneuerbaren-Energie-Gemeinschaft "
        "entfallen zusätzlich Elektrizitätsabgabe (1,5 ct/kWh) und Erneuerbaren-Förderbeitrag.",
        "Erzeuger bekommen für den zugeordneten Überschuss typisch 8 bis 12 Cent statt 6,146 Cent OeMAG-Tarif "
        "(Juli 2026). Was nicht zugeordnet wird, geht weiterhin an die OeMAG oder den Einspeisevertrag.",
        "Strom teilen geht österreichweit, etwa mit der Tante in Wien. Den Netzentgelt-Abschlag gibt es aber "
        "nur im Nahbereich (selber Trafo oder selbes Umspannwerk). Überregional bleibt die "
        "Bürgerenergiegemeinschaft ohne Rabatt.",
        "Beitritt statt Gründung: Über 11.000 Gemeinschaften gibt es bereits, der Beitritt dauert 4 bis 8 "
        "Wochen und kostet laufend 2 bis 8 Euro je Zählpunkt und Monat. Der Lieferantenvertrag bleibt bestehen.",
    ],
    "kpis": [
        ("57 %", "weniger Netzentgelt (Arbeitspreis) in der lokalen EEG"),
        ("6,146 ct", "OeMAG-Marktpreis PV im Juli 2026"),
        ("2 Teilnehmer", "gesetzliche Mindestgröße einer Energiegemeinschaft"),
        ("1.10.2026", "ElWG: neue Regeln, Peer-to-Peer-Verträge"),
    ],

    "sections": [
        ("Was ist eine Energiegemeinschaft?", "was-ist", f"""
<p>Eine Energiegemeinschaft ist ein Zusammenschluss von mindestens zwei Teilnehmern, die Strom aus
erneuerbaren Quellen, in der Praxis fast immer Photovoltaik, gemeinsam erzeugen, teilen und verbrauchen.
Rechtsgrundlage ist seit 2021 das Erneuerbaren-Ausbau-Gesetz (EAG), ab 1. Oktober 2026 übernimmt das
neue Elektrizitätswirtschaftsgesetz (ElWG) die Regeln. Für einen Hausbesitzer mit PV-Anlage heißt das:
Der Strom, den die Anlage mittags zu viel produziert, geht nicht mehr nur an die OeMAG oder den
Lieferanten, sondern an Nachbarn, Betriebe oder die Gemeinde, zu einem Preis, den die Gemeinschaft
selbst festlegt.</p>
<p>Die physikalische Seite ändert sich dabei nicht. Der Strom fließt weiter über das Ortsnetz, der Smart
Meter misst viertelstundengenau, und der Netzbetreiber rechnet aus, welcher Anteil des Überschusses
innerhalb der Gemeinschaft verbraucht wurde. Nur dieser Anteil wird zum EG-Preis abgerechnet. Was übrig
bleibt, geht wie bisher an die OeMAG oder den Einspeisevertrag.</p>
{A.net([
    ("☀", "PV-Erzeuger", "speist Überschuss tagsüber ins Ortsnetz"),
    ("⌂", "Abnehmer", "Haushalte, Betriebe, Gemeinde im Nahbereich"),
    ("◷", "Smart Meter", "misst Einspeisung und Bezug in Viertelstundenwerten"),
    ("€", "Abrechnung", "Plattform verrechnet monatlich zum EG-Preis"),
], "Der Netzbetreiber ordnet zu",
   "Für jede Viertelstunde rechnet der Netzbetreiber aus, wie viel Erzeugung in der Gemeinschaft auf wie "
   "viel Verbrauch trifft. Nur diese Menge bekommt den EG-Preis und das reduzierte Netzentgelt.")}
<p>Wer teilnehmen darf: Privathaushalte, Mieter und Wohnungseigentümer mit eigenem Zählpunkt, Gemeinden,
Vereine sowie kleine und mittlere Unternehmen. Große Unternehmen ab 250 Mitarbeitern dürfen nicht an
einer Erneuerbaren-Energie-Gemeinschaft teilnehmen, wohl aber an einer Bürgerenergiegemeinschaft.
Eine eigene PV-Anlage ist keine Voraussetzung, reine Abnehmer sind ausdrücklich erwünscht, weil
Überschuss nur dann zum EG-Preis abgerechnet werden kann, wenn ihn jemand zeitgleich verbraucht.</p>
"""),
        ("Welche Modelle gibt es in Österreich?", "modelle", f"""
<p>Ab Oktober 2026 gibt es vier Wege, Strom gemeinsam zu nutzen. Welcher passt, hängt davon ab, ob die
Beteiligten im selben Gebäude wohnen, am selben Trafo hängen, nur im selben Bundesland leben oder weit
auseinander, und wie viel Verwaltung sie sich antun wollen.</p>
{A.table(
    ["Modell", "Reichweite", "Rechtsform", "Netzentgelt", "Abgaben"],
    [
        ["Erneuerbare-Energie-Gemeinschaft (EEG)", "Nahbereich: selber Trafo (lokal) oder selbes Umspannwerk (regional)",
         "ja, z. B. Verein", "minus 57 % lokal, minus 28 % regional", "E-Abgabe und Förderbeitrag entfallen"],
        ["Bürgerenergiegemeinschaft (BEG)", "österreichweit, technologieoffen",
         "ja", "voll; ab Okt. 2026 im Nahbereich reduziert", "bleiben"],
        ["Gemeinschaftliche Erzeugungsanlage (GEA)", "Wohnungen im selben Gebäude oder Anschlussobjekt",
         "nein, Vereinbarung reicht", "kein Netzentgelt auf den intern verteilten Strom", "E-Abgabe entfällt"],
        ["Peer-to-Peer-Vertrag (ab 1.10.2026)", "zwei oder mehr Vertragspartner, österreichweit",
         "nein", "reduziert nur im Nahbereich", "bleiben"],
    ],
    hl_cols=(3, 4),
)}
<p>Für Haushalte und Betriebe mit Photovoltaik ist die Erneuerbare-Energie-Gemeinschaft das wirtschaftlich
stärkste Modell, weil nur sie den vollen Netzentgelt-Abschlag mit der Abgabenbefreiung kombiniert.
Strom teilen ist trotzdem österreichweit möglich: Wer den Überschuss etwa der Tante in Wien zukommen
lassen will, kann das über eine Bürgerenergiegemeinschaft oder ab Oktober 2026 per Peer-to-Peer-Vertrag
tun. Den Netzentgelt-Rabatt gibt es dafür allerdings nicht, weil der Strom die übergeordneten
Netzebenen nutzt. Die privaten Konstellationen (Familie, Nachbarn, Mehrparteienhaus) beschreibt der
Artikel {a('/energiegemeinschaft-privat/', 'Energiegemeinschaft privat')}.</p>
"""),
        ("Was Abnehmer sparen: Netzentgelt und Abgaben", "ersparnis", f"""
<p>Der Netzentgelt-Abschlag ist das stärkste Argument für die Energiegemeinschaft und gleichzeitig das am
häufigsten missverstandene. Er gilt nicht für die ganze Stromrechnung, sondern nur für die Menge, die
Ihnen aus der Gemeinschaft zugeordnet wird, und nur für die Positionen, die je Kilowattstunde verrechnet
werden. Grundpauschale und Leistungspreis bleiben unverändert.</p>
{A.table(
    ["Position je kWh", "Richtwert Haushalt 2026*", "Lokale EEG", "Regionale EEG", "BEG im Nahbereich"],
    [
        ["Netznutzungsentgelt (Arbeit)", "7 bis 10 ct", "minus 57 %", "minus 28 %", "minus 57 / 28 % ab Okt. 2026"],
        ["Netzverlustentgelt", "0,5 bis 1 ct", "minus 57 %", "minus 28 %", "minus 57 / 28 % ab Okt. 2026"],
        ["Elektrizitätsabgabe", "1,5 ct", "entfällt", "entfällt", "bleibt"],
        ["Erneuerbaren-Förderbeitrag", "ca. 1 ct", "entfällt", "entfällt", "bleibt"],
        ["Grundpauschale, Leistungspreis", "fix pro Jahr", "unverändert", "unverändert", "unverändert"],
    ],
    hl_cols=(2,),
)}
<p>Lokal bedeutet: Erzeuger und Verbraucher hängen an derselben Trafostation auf der Niederspannungsebene.
Regional bedeutet: Beide sind am selben Umspannwerk auf der Mittelspannungsebene angeschlossen. Wer
ausschließlich auf den Netzebenen 4 und 5 teilnimmt, was nur für größere Betriebe relevant ist, erreicht
bis zu 64 Prozent. Ob Ihr Anschluss lokal oder regional liegt, entscheidet nicht die Postleitzahl, sondern
der Netzbetreiber anhand der Zählpunktnummer.</p>
<p>Rechenbeispiel: Ein Haushalt bekommt 1.000 kWh im Jahr aus einer lokalen EEG zugeordnet. Mit
Richtwerten von 8 Cent Netznutzung, 0,7 Cent Netzverlust, 1,5 Cent Elektrizitätsabgabe und 1 Cent
Förderbeitrag spart er rund 75 Euro aus Netz und Abgaben. Kommt ein EG-Preis von 14 Cent* statt 17 Cent*
Lieferantenpreis dazu, sind es rund 105 Euro, also etwa 10,5 Cent je zugeordneter Kilowattstunde. Die
Rechnung Position für Position steht im Artikel
{a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft und Netzkosten')}.</p>
<p><small>*Richtwerte 2026, die exakten Sätze Ihres Netzgebiets stehen auf der Netzrechnung. EG-Preise sind
Beispielwerte, jede Gemeinschaft legt sie selbst fest.</small></p>
"""),
        ("Was Erzeuger gewinnen: mehr als der OeMAG-Tarif", "erzeuger", f"""
<p>Die OeMAG nimmt PV-Strom zum sogenannten Marktpreis ab, der seit Jänner 2024 monatlich im Nachhinein
festgelegt wird. Für Juli 2026 lag er bei 6,146 Cent je Kilowattstunde, das ist die gesetzliche
Untergrenze von 60 Prozent des Quartalsmarktpreises der E-Control (10,923 Cent im dritten Quartal 2026)
abzüglich Ausgleichsenergiekosten. Solange die Börsenpreise zur Mittagszeit wegen des vielen
Solarstroms niedrig sind, klebt der Tarif an dieser Untergrenze.</p>
<p>In einer Energiegemeinschaft verkaufen Sie den zugeordneten Überschuss zu einem selbst vereinbarten
Preis, typisch 8 bis 12 Cent. Rechnerisch bei 7.000 kWh Überschuss und 60 Prozent Zuordnung: 4.200 kWh
zu 10 Cent* statt 6,146 Cent ergeben rund 160 Euro Mehrerlös im Jahr. Dazu kommt der Abnehmervorteil in
den Abend- und Winterstunden, in denen Sie selbst aus der Gemeinschaft beziehen.</p>
{A.box("Sie müssen den OeMAG-Vertrag nicht kündigen. Die Gemeinschaft ordnet nur die Menge zu, die in "
       "derselben Viertelstunde von einem Mitglied verbraucht wird. Alles andere bleibt Überschuss im Netz "
       "und wird von Ihrem bestehenden Abnahmevertrag zum dortigen Tarif vergütet. Sie können also nur "
       "gewinnen.", label="Wichtig:")}
<p>Die Berechnung des OeMAG-Tarifs, den Verlauf 2026 und den Vergleich aller Optionen für den Überschuss
finden Sie im Artikel {a('/oemag-einspeisetarif/', 'OeMAG-Einspeisetarif 2026')}, die Einordnung für
Kärnten und die Steiermark im {a('/marktpreis-2026/', 'Marktpreis-Überblick 2026')}.</p>
{A.cta("Rechnen Sie Ihre Ersparnis mit eigenen Zahlen",
       "Der Energiegemeinschaft-Rechner vergleicht OeMAG-Einspeisung mit der Gemeinschaft, auf Basis Ihrer "
       "kWp, Ihres Verbrauchs und Ihrer Netzebene. Die Konditionen von EBZ nennen wir im Erstgespräch.",
       primary=("eg_rechner", "Zum Energiegemeinschaft-Rechner"), secondary=("kontakt", "Beratung anfragen"))}
"""),
        ("Beitreten oder gründen: Voraussetzungen und Ablauf", "beitreten", f"""
<p>In Österreich gibt es mittlerweile über 11.000 Energiegemeinschaften, davon mehr als 5.500
Erneuerbare-Energie-Gemeinschaften. In Kärnten und der Steiermark findet sich in fast jedem
Umspannwerksbereich eine aktive Gemeinschaft oder eine, die gerade entsteht. Für die meisten Haushalte
ist der Beitritt deshalb der schnellere Weg: Rechtsform, Vereinsregister, Netzbetreibervertrag und
Abrechnung stehen schon. Die Gründung lohnt sich für Gemeinden, Betriebe oder Nachbarschaften mit
mehreren Erzeugern an einem Trafo.</p>
<h3>Vier Voraussetzungen für den Beitritt</h3>
<ul>
  <li><b>Eigener Zählpunkt:</b> die 33-stellige Nummer, beginnend mit AT, steht auf der Netzrechnung.</li>
  <li><b>Smart Meter mit Viertelstundenwerten:</b> Standardmäßig übermittelt der Zähler nur Tageswerte. Das
  Opt-in aktivieren Sie im Kundenportal des Netzbetreibers, es dauert wenige Tage. Ein früheres Opt-out
  muss rückgängig gemacht werden.</li>
  <li><b>Passender Nahbereich:</b> Ihr Anschluss liegt am selben Trafo (lokal) oder Umspannwerk (regional)
  wie die Gemeinschaft. Der Netzbetreiber ordnet das bei der Anmeldung zu.</li>
  <li><b>Lieferantenvertrag bleibt:</b> Sie brauchen weiterhin einen Stromlieferanten für den Rest. Ein
  Wechsel ist nicht nötig.</li>
</ul>
<h3>Der Beitritt in vier Schritten</h3>
{A.steps([
    ("Gemeinschaft im Nahbereich finden",
     "Über die Gemeinde, über Plattformen wie energyfamily oder über einen Fachbetrieb, der Gemeinschaften "
     "betreut. Entscheidend ist der Nahbereich, nicht die Entfernung in Kilometern."),
    ("Mitgliedsvertrag und Preise prüfen",
     "Einspeisepreis, Bezugspreis, Mitgliedsbeitrag, Kündigungsfrist und Aufteilungsschlüssel (statisch "
     "oder dynamisch). Der Schlüssel bestimmt, wie viel EG-Strom Ihnen zugeordnet wird."),
    ("Zählpunkt freigeben",
     "Im Kundenportal des Netzbetreibers (Kärnten Netz, Energienetze Steiermark, Stromnetz Graz) bestätigen "
     "Sie die Teilnahmeanfrage und die Datenfreigabe. Diesen Schritt kann nur der Zählpunktinhaber setzen."),
    ("Start im Folgemonat",
     "Der Netzbetreiber ordnet ab dem Folgemonat die Energiemengen zu, die Gemeinschaft rechnet monatlich "
     "oder quartalsweise ab. Vom Erstgespräch bis zum Start vergehen in der Regel 4 bis 8 Wochen."),
])}
<p>Die Details zu Ablauf, Aufteilungsschlüssel und Kündigung stehen im Artikel
{a('/energiegemeinschaft-beitreten/', 'Energiegemeinschaft beitreten')}, die Suche nach einer passenden
Gemeinschaft im Artikel {a('/energiegemeinschaft-finden/', 'Energiegemeinschaft finden')}. Wer selbst
eine aufbauen will, findet Rechtsform, Registrierung und Zeitplan im Artikel
{a('/energiegemeinschaft-gruenden/', 'Energiegemeinschaft gründen')}.</p>
"""),
        ("Kosten und Nachteile ehrlich betrachtet", "kosten-nachteile", f"""
<p>Die Energiegemeinschaft ist günstig, aber nicht gratis. Für den Beitritt fallen üblicherweise keine
Einrichtungskosten an. Laufend zahlen Mitglieder 2 bis 8 Euro je Zählpunkt und Monat für Plattform und
Abrechnung, manche Gemeinschaften verrechnen stattdessen 0,5 bis 2 Cent je abgerechneter
Kilowattstunde. Im Jahr sind das 25 bis 100 Euro. Dem stehen laut Erfahrungsberichten typische Vorteile
von 100 bis 300 Euro gegenüber. Die Rechnung geht auf, solange die Zuordnungsquote stimmt. Alle
Kostenarten und die drei Rechnungen nach dem Beitritt erklärt der Artikel
{a('/energiegemeinschaft-kosten/', 'Energiegemeinschaft: Kosten und Abrechnung')}.</p>
<p>Der wichtigste Nachteil, den viele unterschätzen: Vergünstigt wird nur Strom, der zeitgleich erzeugt und
verbraucht wird. Ein Haushalt ohne Tagesverbrauch erreicht bei 4.000 kWh Jahresverbrauch eine
Zuordnungsquote von etwa 25 Prozent. Mit Wärmepumpe, E-Auto oder Homeoffice sind 40 bis 60 Prozent
erreichbar. Ein {a('batteriespeicher', 'Speicher')} und ein Energiemanagementsystem verschieben Verbrauch
und Speicherung so, dass mehr Strom zur richtigen Zeit genutzt wird.</p>
{A.box_dark("Faustregel vor dem Beitritt",
    "Liegt die jährliche Gebühr über 30 Prozent Ihres erwarteten Vorteils, passt die Gemeinschaft nicht "
    "zu Ihrem Verbrauchsprofil. Prüfen Sie außerdem Jahresbindungen, Preisklauseln, die den Einspeisepreis "
    "an den OeMAG-Tarif koppeln, und Gebühren für den Austritt, die es bei seriösen Gemeinschaften nicht "
    "gibt. Die vollständige Liste steht im Artikel " +
    a('/energiegemeinschaft-nachteile/', 'Energiegemeinschaft: Nachteile') + ".")}
"""),
        ("Was sich ab Oktober 2026 durch das ElWG ändert", "elwg", f"""
<p>Mit 1. Oktober 2026 treten die Bestimmungen des neuen Elektrizitätswirtschaftsgesetzes zur gemeinsamen
Energienutzung in Kraft. Bestehende Energiegemeinschaften laufen weiter und werden ins neue System
übergeführt. Drei Neuerungen sind für Haushalte relevant:</p>
<ul>
  <li><b>Peer-to-Peer-Verträge:</b> Strom kann ohne Verein direkt an eine Person verkauft oder verschenkt
  werden, ohne Rechtsform, geografische Grenze oder Mindestteilnehmerzahl. Betreiber bis 30 kW werden
  durch den Verkauf nicht zum Energielieferanten. Die Abgabenbefreiung bleibt aber der EEG vorbehalten.</li>
  <li><b>Reduzierte Netzentgelte für BEG und Peer-to-Peer im Nahbereich:</b> Wer sich auf einen Nahbereich
  beschränkt, bekommt auch in diesen Modellen den Netzentgelt-Abschlag.</li>
  <li><b>Versorgungsinfrastrukturbeitrag:</b> Für Einspeiser mit mehr als 20 kW, gedeckelt mit
  durchschnittlich 0,5 Euro je Megawattstunde (0,05 Cent je Kilowattstunde). Für eine typische
  Einfamilienhaus-Anlage nicht relevant.</li>
</ul>
<p>Offen ist die Netzentgeltstruktur ab 1. Jänner 2027: Das ElWG ermächtigt die E-Control, die Abschläge
per Verordnung neu festzulegen. Ob sich die 57 und 28 Prozent ändern, ist derzeit nicht bekannt. Welche
Marktprozesse die Netzbetreiber zum Stichtag bereitstellen, ist laut Koordinationsstelle ebenfalls noch
offen. Wir aktualisieren diesen Artikel, sobald die Verordnung vorliegt.</p>
"""),
        ("Energiegemeinschaft in Kärnten und der Steiermark", "regional", f"""
<p>Kärnten liefert mit rund 1.050 bis 1.150 Kilowattstunden je installiertem Kilowattpeak die höchsten
PV-Erträge Österreichs und ist kleinteilig besiedelt: Viele Ortschaften hängen an einem gemeinsamen
Trafo, was lokale Gemeinschaften mit dem vollen Abschlag erleichtert. Netzbetreiber ist überwiegend die
Kärnten Netz GmbH, in der Steiermark sind es die Energienetze Steiermark und in Graz die Stromnetz Graz.
Die regionalen Besonderheiten, Anbieter und Förderungen beschreiben die Artikel
{a('/energiegemeinschaft-kaernten/', 'Energiegemeinschaft Kärnten')},
{a('/energiegemeinschaft-steiermark/', 'Energiegemeinschaft Steiermark')} und
{a('/energiegemeinschaft-villach-klagenfurt/', 'Energiegemeinschaft in Villach und Klagenfurt')}.</p>
<p>EBZ Energie geht dabei den umgekehrten Weg vieler Abrechnungsanbieter: Wir kommen von der
{a('photovoltaik', 'PV-Anlage')} und ergänzen sie um die Energiegemeinschaft. Auslegung, Speicher,
Wallbox und Energiemanagement werden von Anfang an darauf abgestimmt, dass der Überschuss dann anfällt,
wenn die Gemeinschaft ihn braucht. Für Abrechnung und Verwaltung arbeiten wir mit energyfamily, einer
österreichischen Plattform mit rund 330 aktiven Gemeinschaften und rund 15.000 Nutzern. Für
Privathaushalte gibt es die {a('eg_privat', 'Energiegemeinschaft für Privatkunden')}, für Betriebe und
Gemeinden die {a('eg_gewerbe', 'Energiegemeinschaft für Gewerbe und Gemeinden')}.</p>
<p>Eine eigene Förderung für die Teilnahme gibt es nicht. Gefördert wird die PV-Anlage über den
EAG-Investitionszuschuss und die Landesförderungen. Wer ein Energiemanagementsystem einsetzt, kann seit
Juni 2026 die {a('/ems-foerderung/', 'EMS-Förderung des Klimafonds')} nutzen: Die Teilnahme an einer
Energiegemeinschaft ist dort eine der sechs zulässigen Betriebsoptionen.</p>
"""),
        ("Fazit: Energiegemeinschaft", "fazit", f"""
<p>Die Energiegemeinschaft macht lokal erzeugten Strom für mehrere Teilnehmer nutzbar und wirkt an zwei
Stellen: Erzeuger bekommen 8 bis 12 Cent statt 6,146 Cent für den zugeordneten Überschuss, Abnehmer
sparen bis zu 57 Prozent Netzentgelt plus Abgaben. Beides gilt nur für die zugeordnete Menge, deshalb
entscheiden Verbrauchsprofil, Speicher und Energiemanagement über den tatsächlichen Nutzen. Der Einstieg
dauert wenige Wochen, das Risiko ist gering: Lieferant und OeMAG-Vertrag bleiben, der Austritt ist mit
ein bis drei Monaten Frist möglich.</p>
{A.cta("Anlage planen, Teilen gleich mitdenken",
       "EBZ prüft Netzebene, Eignung und Einsparpotenzial, nimmt Sie in Kärnten und der Steiermark in eine "
       "Gemeinschaft auf und übernimmt Zählpunktfreigabe und Abrechnung.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("eg_privat", "Zur Energiegemeinschaft mit EBZ"))}
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
        ("Was ist eine Energiegemeinschaft?",
         "Ein Zusammenschluss von mindestens zwei Teilnehmern, die Strom aus erneuerbaren Quellen gemeinsam "
         "erzeugen, teilen und verbrauchen. Der Strom fließt über das öffentliche Netz, der Netzbetreiber ordnet "
         "ihn viertelstundengenau zu, und die Mitglieder zahlen dafür einen selbst vereinbarten Preis und im "
         "Nahbereich bis zu 57 Prozent weniger Netzentgelt."),
        ("Welche Arten von Energiegemeinschaften gibt es?",
         "Die Erneuerbare-Energie-Gemeinschaft (EEG) im Nahbereich mit vollem Netzentgelt-Abschlag und "
         "Abgabenbefreiung, die Bürgerenergiegemeinschaft (BEG) österreichweit und technologieoffen ohne "
         "Abgabenbefreiung, die gemeinschaftliche Erzeugungsanlage (GEA) innerhalb eines Gebäudes und ab "
         "1. Oktober 2026 der Peer-to-Peer-Vertrag zwischen einzelnen Personen."),
        ("Kann ich Strom auch mit Verwandten in einem anderen Bundesland teilen?",
         "Ja. Strom teilen ist österreichweit möglich, über eine Bürgerenergiegemeinschaft oder ab Oktober 2026 "
         "per Peer-to-Peer-Vertrag. Den Netzentgelt-Abschlag von 57 oder 28 Prozent und die Abgabenbefreiung "
         "gibt es aber nur im Nahbereich, also am selben Trafo oder Umspannwerk."),
        ("Wie viel kann ich sparen?",
         "Abnehmer sparen auf die zugeordnete Menge rund 7 bis 8 Cent je Kilowattstunde aus Netz und Abgaben "
         "(lokale EEG, Richtwerte 2026) plus die Differenz zwischen Lieferantenpreis und EG-Preis. Erzeuger "
         "bekommen typisch 8 bis 12 Cent statt 6,146 Cent OeMAG-Tarif. Laut Erfahrungsberichten liegt der "
         "Jahresvorteil eines Haushalts typisch bei 100 bis 300 Euro, abhängig von der Zuordnungsquote."),
        ("Brauche ich eine eigene PV-Anlage?",
         "Nein. Sie können als reiner Abnehmer teilnehmen und sparen Netzentgelt und Abgaben auf den EG-Strom. "
         "Mit eigener PV-Anlage profitieren Sie doppelt: Sie nutzen den Eigenverbrauch und verkaufen den "
         "Überschuss zum EG-Preis statt zum OeMAG-Tarif."),
        ("Muss ich meinen Stromlieferanten oder den OeMAG-Vertrag kündigen?",
         "Nein, beides bleibt bestehen. Die Gemeinschaft deckt nur den Anteil, der zeitgleich erzeugt und "
         "verbraucht wird. Den Rest liefert weiterhin Ihr Lieferant, nicht zugeordneter Überschuss geht wie "
         "bisher an die OeMAG oder Ihren Einspeisevertrag."),
        ("Welche Voraussetzungen brauche ich?",
         "Einen eigenen Zählpunkt, einen Smart Meter mit aktivierten Viertelstundenwerten (Opt-in beim "
         "Netzbetreiber) und einen Anschluss im Nahbereich der Gemeinschaft. Große Unternehmen ab 250 "
         "Mitarbeitern dürfen nur in Bürgerenergiegemeinschaften, nicht in EEGs."),
        ("Wie lange dauert der Beitritt und was kostet er?",
         "In der Regel 4 bis 8 Wochen, weil die Zählpunktanmeldung nur zum Monatsersten wirksam wird. "
         "Einrichtungsgebühren sind unüblich, laufend fallen 2 bis 8 Euro je Zählpunkt und Monat oder 0,5 bis "
         "2 Cent je abgerechneter Kilowattstunde an. Kündigungsfristen liegen bei ein bis drei Monaten."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert PV-Anlagen, "
                    "Speicher, Wärmepumpen und Energiemanagementsysteme in Kärnten und der Steiermark und begleitet "
                    "Kunden beim Einstieg in Energiegemeinschaften. Die Inhalte werden anhand der Vorgaben von "
                    "E-Control, OeMAG und energiegemeinschaften.gv.at aktualisiert. Keine Rechts- oder Steuerberatung."),
    "sources": [
        ("E-Control: Energiegemeinschaften", "https://www.e-control.at/energiegemeinschaften"),
        ("Koordinationsstelle für Energiegemeinschaften: Neue rechtliche Grundlagen (ElWG)",
         "https://energiegemeinschaften.gv.at/rechtliche-grundlagen-elwg/"),
        ("Koordinationsstelle: Peer-to-Peer-Verträge", "https://energiegemeinschaften.gv.at/peer-to-peer-vertraege/"),
        ("Koordinationsstelle: Gemeinsame Energienutzung", "https://energiegemeinschaften.gv.at/gemeinsame-energienutzung/"),
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/marktpreis"),
        ("oesterreich.gv.at", "https://www.oesterreich.gv.at/"),
    ],
    "related": [
        ("eg_privat", "Energiegemeinschaft mit EBZ: Leistungsseite für Privatkunden"),
        ("/energiegemeinschaft-beitreten/", "Energiegemeinschaft beitreten: Ablauf in vier Schritten"),
        ("/energiegemeinschaft-netzkosten/", "Netzkosten: Was in der Energiegemeinschaft günstiger wird"),
        ("/oemag-einspeisetarif/", "OeMAG-Einspeisetarif 2026 und die Alternative"),
    ],
    "cta": {
        "h3": "Eignung in 10 Minuten prüfen",
        "text": "Nennen Sie uns Postleitzahl, PV-Leistung und Jahresverbrauch. Wir sagen Ihnen, welche Gemeinschaft infrage kommt und was sie bringt.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Mit eigener PV zum starken Teil der Gemeinschaft",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, Montage "
                   "und EG-Anbindung aus einer Hand übernimmt."),
}
