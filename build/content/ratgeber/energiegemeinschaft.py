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
    "title": "Energiegemeinschaft Österreich: 5 Modelle nach ElWG | EBZ",
    "description": ("Energiegemeinschaft in Österreich: die 5 Modelle nach ElWG (EEG, BEG, GEA, P2P, EVA), bis zu "
                    "57 % weniger Netzentgelt in der EEG, Kosten und Ablauf."),
    "eyebrow": "Energiegemeinschaft · Leitartikel",
    "crumb_label": "Energiegemeinschaft",
    "h1": "Energiegemeinschaft in Österreich: Solarstrom teilen und bis zu 57 % Netzentgelt sparen",
    "lead": ("In einer Energiegemeinschaft verkaufen PV-Besitzer ihren Überschuss zu einem selbst vereinbarten "
             "Preis an Haushalte und Betriebe in der Nähe, statt ihn zum OeMAG-Marktpreis abzugeben. Dieser "
             "Leitartikel erklärt die Modelle, die Ersparnis, den Ablauf und die Grenzen, mit Links zu allen "
             "Detailartikeln."),
    "chips": [
        "Lokale EEG: bis zu <b>57 %</b> weniger Netzentgelt",
        "EG-Einspeisepreis: <b>8 bis 12 ct</b>",
        "OeMAG Okt. 2026: <b>14,874 ct</b>",
        "Über <b>11.000</b> Gemeinschaften in Österreich",
    ],
    "date_published": "2026-07-22",
    "date_modified": "2026-11-20",
    "hero_img": "eg_drohne",
    "hero_alt": "Ortschaft mit Photovoltaik auf mehreren Dächern, typisches Netzgebiet einer lokalen Energiegemeinschaft",

    "tldr": [
        "Eine Energiegemeinschaft ist ein Zusammenschluss von mindestens zwei Teilnehmern, die Strom aus "
        "erneuerbaren Quellen gemeinsam erzeugen, teilen und verbrauchen. Der Strom fließt physisch wie bisher "
        "durchs Netz, neu ist nur die Zuordnung per Smart Meter und die Abrechnung zum EG-Preis. Seit "
        "1. Oktober 2026 kennt das ElWG fünf Bürgerenergie-Modelle: GEA, EEG, BEG, Peer-to-Peer-Vertrag und "
        "Eigenversorgungsanlage.",
        "Mitglieder einer lokalen oder regionalen Erneuerbare-Energie-Gemeinschaft (EEG) sparen auf den "
        "zugeordneten Strom 57 Prozent (lokal) oder 28 Prozent (regional) des Arbeitspreises von Netznutzungs- "
        "und Netzverlustentgelt, zusätzlich entfällt die Elektrizitätsabgabe (2026 für Haushalte befristet "
        "0,1 ct, ab 2027 wieder 1,5 ct je kWh). Den Erneuerbaren-Förderbeitrag setzt die Bundesregierung 2027 "
        "für alle Stromkunden aus. Bis Ende 2026 gilt der Netzentgelt-Rabatt nur für EEG-Mitglieder.",
        "Erzeuger bekommen für den zugeordneten Überschuss einen fix vereinbarten Preis, typisch 8 bis 12 Cent "
        "(Beispielwerte), statt des monatlich schwankenden OeMAG-Tarifs (Juli 2026: 6,146 Cent, Oktober 2026: "
        "14,874 Cent). Je nach Monat liegt der EG-Preis darüber oder darunter, dafür ist er planbar. Was nicht zugeordnet wird, geht weiterhin an die OeMAG oder den Einspeisevertrag.",
        "Eine Bürgerenergiegemeinschaft darf sich über ganz Österreich erstrecken, etwa bis zur Familie in Wien. "
        "In der Übergangsphase seit Oktober 2026 lassen sich neue Zuordnungen laut Koordinationsstelle aber nur "
        "mit Zählpunkten beim selben Netzbetreiber umsetzen, netzübergreifend voraussichtlich ab April 2027. "
        "Außerhalb des Nahbereichs gibt es keinen Netzentgelt-Rabatt.",
        "Beitritt statt Gründung: Über 11.000 Gemeinschaften gibt es bereits, der Beitritt dauert 4 bis 8 "
        "Wochen und kostet laufend 2 bis 8 Euro je Zählpunkt und Monat. Der Lieferantenvertrag bleibt bestehen.",
    ],
    "kpis": [
        ("57 %", "weniger Netzentgelt (Arbeitspreis) in der lokalen EEG"),
        ("14,874 ct", "OeMAG-Marktpreis PV im Oktober 2026 (Juli: 6,146 ct)"),
        ("2 Teilnehmer", "gesetzliche Mindestgröße einer Energiegemeinschaft"),
        ("5 Modelle", "Bürgerenergie nach ElWG seit 1.10.2026: GEA, EEG, BEG, P2P, EVA"),
    ],

    "sections": [
        ("Was ist eine Energiegemeinschaft?", "was-ist", f"""
<p><b>Eine Energiegemeinschaft ist ein Zusammenschluss von mindestens zwei Teilnehmern, die Solarstrom über
das öffentliche Netz teilen.</b> Für Mitglieder einer Erneuerbare-Energie-Gemeinschaft sinken die Netzentgelte
im Nahbereich um bis zu 57 Prozent (lokal) oder 28 Prozent (regional). Bürgerenergiegemeinschaften dürfen sich
über ganz Österreich erstrecken, außerhalb des Nahbereichs aber ohne Rabatt. Voraussetzung ist ein Smart Meter
mit Viertelstundenwerten (Quellen: E-Control SNE-VO, energiegemeinschaften.gv.at, Stand November 2026).</p>
<p>Die Teilnehmer erzeugen, teilen und verbrauchen Strom aus erneuerbaren Quellen gemeinsam, in der Praxis
fast immer Photovoltaik. Rechtsgrundlage war seit 2021 das Erneuerbaren-Ausbau-Gesetz (EAG), seit 1. Oktober 2026 regelt das
neue Elektrizitätswirtschaftsgesetz (ElWG) die gemeinsame Energienutzung. Für einen Hausbesitzer mit PV-Anlage heißt das:
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
einer Erneuerbaren-Energie-Gemeinschaft teilnehmen, wohl aber an einer Bürgerenergiegemeinschaft (ohne dort
die Kontrolle auszuüben) und an Peer-to-Peer-Verträgen.
Eine eigene PV-Anlage ist keine Voraussetzung, reine Abnehmer sind ausdrücklich erwünscht, weil
Überschuss nur dann zum EG-Preis abgerechnet werden kann, wenn ihn jemand zeitgleich verbraucht.</p>
"""),
        ("Die 5 Bürgerenergie-Modelle nach ElWG: GEA, EEG, BEG, Peer-to-Peer, EVA", "elwg", f"""
<p><b>Seit 1. Oktober 2026 regelt das Elektrizitätswirtschaftsgesetz (ElWG) fünf Bürgerenergie-Modelle:
die gemeinschaftliche Erzeugungsanlage (GEA), die Erneuerbare-Energie-Gemeinschaft (EEG), die
Bürgerenergiegemeinschaft (BEG), den Peer-to-Peer-Vertrag (P2P) und die Eigenversorgungsanlage (EVA).</b>
Sie unterscheiden sich darin, wer mitmachen darf, ob eine Rechtsform nötig ist, wie weit der Strom reisen
darf und ob es Rabatte auf Netzentgelt und Abgaben gibt. Bestehende GEA, EEG und BEG wurden mit
1. Oktober 2026 ins neue System übergeführt (Quelle: Koordinationsstelle für Energiegemeinschaften, Stand
November 2026).</p>
{A.table(
    ["Modell", "Wer darf teilnehmen", "Rechtsform", "Reichweite", "Netzentgelt Okt. bis Dez. 2026",
     "Netzentgelt ab 2027 (voraussichtlich)", "Abgabenbefreiung"],
    [
        ["Gemeinschaftliche Erzeugungsanlage (GEA)",
         "Zählpunktinhaber an derselben Hauptleitung: Mieter, Wohnungseigentümer, Betriebe im selben Gebäude",
         "nein, Vertrag reicht",
         "dieselbe Hauptleitung im Gebäude, kein öffentliches Netz",
         "kein Netzentgelt auf den intern verteilten Strom",
         "Hauptleitung weiter ohne Netzentgelt; Standortbereich reduziert per Verordnung, Umsetzung voraussichtlich ab April 2027",
         "Elektrizitätsabgabe entfällt, kein Förderbeitrag (im Standortbereich offen)"],
        ["Erneuerbare-Energie-Gemeinschaft (EEG)",
         "natürliche Personen, Gemeinden, öffentliche Stellen, KMU (keine großen Unternehmen)",
         "ja, z. B. Verein oder Genossenschaft",
         "Lokalbereich (Trafo, rund 1 km) oder Regionalbereich (Umspannwerk, rund 30 km)",
         "minus 57 % lokal, minus 28 % regional, bis 64 % nur NE 4/5 (geltende SNE-VO)",
         "reduziert im Nahbereich, Höhe legt die E-Control neu fest (Entwurf: 49 % lokal, 22 % bzw. 58 % regional)",
         "ja: Elektrizitätsabgabe entfällt (ab 2027 wieder 1,5 ct), Förderbeitrag entfällt (2027 ohnehin für alle ausgesetzt)"],
        ["Bürgerenergiegemeinschaft (BEG)",
         "alle, auch große Unternehmen (ohne Kontrolle über die BEG)",
         "ja",
         "jeder Nahbereich oder ganz Österreich über mehrere Netzbetreiber",
         "volles Netzentgelt",
         "im Nahbereich reduziert, österreichweit volles Netzentgelt",
         "nein"],
        ["Peer-to-Peer-Vertrag (P2P)",
         "mindestens zwei aktive Kunden: Privatpersonen, Unternehmen jeder Größe, Gemeinden",
         "nein, zivilrechtlicher Vertrag (Verkauf oder Schenkung)",
         "Nahbereich oder ganz Österreich",
         "volles Netzentgelt",
         "im Nahbereich reduziert, österreichweit volles Netzentgelt",
         "nicht geregelt, nicht zugesagt"],
        ["Eigenversorgungsanlage (EVA)",
         "eine Person oder ein Betrieb mit mehreren eigenen Standorten",
         "nein",
         "Standort-, Lokal- oder Regionalbereich, bei der Registrierung festgelegt",
         "volles Netzentgelt",
         "im Nahbereich reduziert",
         "nicht geregelt, nicht zugesagt"],
    ],
    hl_cols=(4, 5),
)}
<p><small>Quellen: energiegemeinschaften.gv.at (FAQs zum ElWG, Modellseiten), E-Control SNE-VO. Die Werte für
2027 hängen von der novellierten Systemnutzungsentgelte-Verordnung ab, die laut Koordinationsstelle nach
heutigem Stand mit 1. Jänner 2027 in Kraft treten soll. Laut E-Control-Entwurf für 2027 sind 49 Prozent lokal
und 22 bzw. 58 Prozent regional vorgesehen (Entwurf, Höhe legt die E-Control fest).</small></p>
<h3>Welches Modell für wen?</h3>
<ul>
  <li><b>GEA:</b> für Mehrparteienhäuser, Wohnanlagen und Bürogebäude. Die PV-Anlage am Dach versorgt die
  Wohnungen über die Hauptleitung, den Reststrom liefert weiterhin ein frei wählbarer Lieferant. Details im
  Ratgeber {a('/gemeinschaftliche-erzeugungsanlage/', 'Gemeinschaftliche Erzeugungsanlage im Mehrparteienhaus')}.</li>
  <li><b>EEG:</b> für Nachbarschaften, Siedlungen, Gemeinden und KMU am selben Trafo oder Umspannwerk. Das
  einzige Modell, das schon 2026 Netzentgelt-Rabatt und Abgabenbefreiung kombiniert. Preise und Gebühren
  bestehender Gemeinschaften zeigt der {a('/energiegemeinschaft-vergleich/', 'Energiegemeinschaft-Vergleich')}.</li>
  <li><b>BEG:</b> für Projekte mit großen Unternehmen oder über mehrere Netzgebiete hinweg. Je Netzgebiet ist
  ein eigener Vertrag mit dem Netzbetreiber nötig. Mehr im Ratgeber
  {a('/buergerenergiegemeinschaft/', 'Bürgerenergiegemeinschaft (BEG)')}.</li>
  <li><b>Peer-to-Peer:</b> für zwei oder wenige Beteiligte ohne Verein, etwa Eltern und Kinder. Gewinnabsicht
  ist erlaubt, Strom darf auch verschenkt werden. Smart Meter und Anmeldung über das EDA-Portal sind nötig,
  Ablauf im Ratgeber {a('/peer-to-peer-strom/', 'Peer-to-Peer-Strom')}.</li>
  <li><b>EVA:</b> für Sie selbst an mehreren Standorten, etwa PV am Wohnhaus und Verbrauch im Zweitwohnsitz
  oder im zweiten Betriebsgebäude. Eine zweite Person ist nicht nötig.</li>
</ul>
<h3>Mehrfachteilnahme: bis zu fünf Modelle je Zählpunkt</h3>
<p>Mit jeder Erzeugungsanlage bzw. jedem Zählpunkt können Sie an bis zu fünf Bürgerenergie-Modellen
gleichzeitig teilnehmen, etwa an einer GEA im Haus, einer lokalen EEG im Ort und einem Peer-to-Peer-Vertrag
mit der Tochter. Der Teilnahmefaktor legt je 15-Minuten-Intervall fest, welcher Anteil höchstens auf welches
Modell entfällt, in Summe maximal 100 Prozent. Geändert werden kann er derzeit einmal täglich, ab 2028
voraussichtlich mehrmals täglich.</p>
<h3>Übergangsphase: vorerst nur beim selben Netzbetreiber</h3>
<p>Eine BEG darf sich über ganz Österreich erstrecken. In der Übergangsphase seit Oktober 2026 lassen sich
neue Zuordnungen laut Koordinationsstelle vorübergehend nur mit Zählpunkten beim selben Netzbetreiber
umsetzen, netzübergreifend (z. B. Kärnten und Wien) voraussichtlich ab April 2027. Das gilt genauso für
Peer-to-Peer-Verträge und die Mehrfachteilnahme. Wer seinen Überschuss also der Familie in Wien zukommen
lassen will, plant das realistisch für 2027 und ohne Netzentgelt-Rabatt, weil der Strom die übergeordneten
Netzebenen nutzt. Für Haushalte und Betriebe mit Photovoltaik bleibt die lokale EEG das wirtschaftlich
stärkste Modell. Die privaten Konstellationen (Familie, Nachbarn, Mehrparteienhaus) beschreibt der Artikel
{a('/energiegemeinschaft-privat/', 'Energiegemeinschaft privat')}.</p>
"""),
        ("Was Abnehmer sparen: Netzentgelt und Abgaben", "ersparnis", f"""
<p>Der Netzentgelt-Abschlag ist das stärkste Argument für die Energiegemeinschaft und gleichzeitig das am
häufigsten missverstandene. Er gilt nicht für die ganze Stromrechnung, sondern nur für die Menge, die
Ihnen aus der Gemeinschaft zugeordnet wird, und nur für die Positionen, die je Kilowattstunde verrechnet
werden. Grundpauschale und Leistungspreis bleiben unverändert.</p>
{A.table(
    ["Position je kWh", "Richtwert Haushalt*", "Lokale EEG", "Regionale EEG", "BEG, P2P, EVA im Nahbereich"],
    [
        ["Netznutzungsentgelt (Arbeit)", "7 bis 10 ct", "minus 57 %", "minus 28 %", "2026 voll, ab 1.1.2027 voraussichtlich reduziert"],
        ["Netzverlustentgelt", "0,5 bis 1 ct", "minus 57 %", "minus 28 %", "2026 voll, ab 1.1.2027 voraussichtlich reduziert"],
        ["Elektrizitätsabgabe", "2026: 0,1 ct (befristet), ab 2027: 1,5 ct", "entfällt", "entfällt", "bleibt (keine Befreiung zugesagt)"],
        ["Erneuerbaren-Förderbeitrag", "2026: ca. 1 ct, 2027 laut Bundesregierung ausgesetzt", "entfällt", "entfällt", "2026 voll, 2027 für alle ausgesetzt"],
        ["Grundpauschale, Leistungspreis", "fix pro Jahr", "unverändert", "unverändert", "unverändert"],
    ],
    hl_cols=(2,),
)}
<p>Lokal bedeutet: Erzeuger und Verbraucher hängen an derselben Trafostation auf der Niederspannungsebene,
meist in einem Radius von rund 1 km. Regional bedeutet: Beide sind am selben Umspannwerk auf der
Mittelspannungsebene angeschlossen, rund 30 km. Die Abschläge von 57 und 28 Prozent stammen aus der derzeit
geltenden SNE-VO und gelten von Oktober bis Dezember 2026 nur für Mitglieder lokaler und regionaler EEGs. Wer
ausschließlich auf den Netzebenen 4 und 5 teilnimmt, was nur für größere Betriebe relevant ist, erreicht
bis zu 64 Prozent. Ob Ihr Anschluss lokal oder regional liegt, entscheidet nicht die Postleitzahl, sondern
der Netzbetreiber anhand der Zählpunktnummer.</p>
<p>Rechenbeispiel (Abgaben Stand 2027): Ein Haushalt bekommt 1.000 kWh im Jahr aus einer lokalen EEG
zugeordnet. Mit Richtwerten von 8 Cent Netznutzung, 0,7 Cent Netzverlust und 1,5 Cent Elektrizitätsabgabe
spart er rund 65 Euro aus Netz und Abgaben; den Erneuerbaren-Förderbeitrag zahlt 2027 laut Bundesregierung
ohnehin niemand. Kommt ein EG-Preis von 14 Cent* statt 17 Cent* Lieferantenpreis dazu, sind es rund
95 Euro, also etwa 9,5 Cent je zugeordneter Kilowattstunde. 2026 liegt der Abgabenteil ähnlich niedrig:
Die Elektrizitätsabgabe beträgt für Haushalte befristet nur 0,1 Cent, dafür entfällt noch rund 1 Cent
Förderbeitrag, zusammen rund 60 Euro aus Netz und Abgaben. Der Abgabenvorteil der EEG ist also kleiner
als früher, der Netzentgelt-Rabatt bleibt der größte Posten. Die
Rechnung Position für Position steht im Artikel
{a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft und Netzkosten')}.</p>
<p><small>*Richtwerte: Netzentgelte und Abschläge 2026 (geltende SNE-VO), Abgaben wie angegeben; die exakten
Sätze Ihres Netzgebiets stehen auf der Netzrechnung. EG-Preise sind Beispielwerte, jede Gemeinschaft legt sie
selbst fest. Die Höhe der Abschläge ab 2027 legt die E-Control per Verordnung neu fest; mit dem Entwurfswert
von 49 Prozent lokal sänke die Netzersparnis im Beispiel von rund 50 auf rund 43 Euro.</small></p>
"""),
        ("Was Erzeuger gewinnen: fixer Preis statt schwankendem OeMAG-Tarif", "erzeuger", f"""
<p>Die OeMAG nimmt PV-Strom zum sogenannten Marktpreis ab, der seit Jänner 2024 monatlich im Nachhinein
festgelegt wird. Für Oktober 2026 beträgt er 14,874 Cent je Kilowattstunde (Stand November 2026), im
September 2026 lag er bei 10,168 Cent, im Juli 2026 bei 6,146 Cent, der gesetzlichen Untergrenze von 60 Prozent des Quartalsmarktpreises der
E-Control (10,923 Cent im dritten Quartal 2026) abzüglich Ausgleichsenergiekosten. Der Tarif schwankte
also schon innerhalb des dritten Quartals um rund 4 Cent und bis Oktober um fast 9 Cent, je nachdem, wie die Börsenpreise zur Mittagszeit stehen.</p>
<p>In einer Energiegemeinschaft verkaufen Sie den zugeordneten Überschuss zu einem selbst vereinbarten,
fixen Preis, typisch 8 bis 12 Cent*. Rechnerisch bei 7.000 kWh Überschuss und 60 Prozent Zuordnung:
4.200 kWh zu 10 Cent* bringen 420 Euro im Jahr. Bei der OeMAG wären es, den jeweiligen Monatswert aufs Jahr
hochgerechnet, 258 Euro (Juli 2026) bis 625 Euro (Oktober 2026). Der Erzeugervorteil hängt also vom Marktpreis ab:
In Monaten mit niedrigem Tarif bringt der EG-Preis mehr, beim Oktober-Wert von 14,874 Cent zahlt die OeMAG mehr. Verlässlich sind die Planbarkeit des fixen Preises und der
Abnehmervorteil in den Abend- und Winterstunden, in denen Sie selbst aus der Gemeinschaft beziehen.</p>
{A.box("Sie müssen den OeMAG-Vertrag nicht kündigen. Die Gemeinschaft ordnet nur die Menge zu, die in "
       "derselben Viertelstunde von einem Mitglied verbraucht wird. Alles andere bleibt Überschuss im Netz "
       "und wird von Ihrem bestehenden Abnahmevertrag zum dortigen Tarif vergütet. Auf dem nicht "
       "zugeordneten Anteil ändert sich für Sie nichts.", label="Wichtig:")}
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
     "Im Kundenportal des Netzbetreibers (Kärnten Netz, Energie Klagenfurt, Energienetze Steiermark, Stromnetz Graz) bestätigen "
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
        ("Was das ElWG ändert: Zeitplan 2026 bis 2028", "elwg-zeitplan", f"""
<p>Mit 1. Oktober 2026 sind die Bestimmungen des neuen Elektrizitätswirtschaftsgesetzes zur gemeinsamen
Energienutzung in Kraft getreten. Bestehende Energiegemeinschaften laufen weiter und wurden ins neue System
übergeführt. Die Neuerungen greifen schrittweise, die Termine nennt die Koordinationsstelle für
Energiegemeinschaften als "voraussichtlich" bzw. "nach heutigem Stand":</p>
{A.steps([
    ("1. Oktober 2026: ElWG in Kraft",
     "Fünf Bürgerenergie-Modelle, neu sind Peer-to-Peer-Vertrag und Eigenversorgungsanlage. Die Beschränkung "
     "einer EEG auf einen Netzbetreiber fällt weg."),
    ("Seit 5. Oktober 2026: Umsetzung beim selben Netzbetreiber",
     "Neue Modelle und Mehrfachteilnahme lassen sich vorerst nur mit Zählpunkten umsetzen, die alle beim "
     "selben Netzbetreiber sind."),
    ("Oktober bis Dezember 2026: Rabatt nur für EEG",
     "Den reduzierten Netzarbeitspreis bekommen bis Jahresende nur Mitglieder lokaler und regionaler EEGs "
     "(minus 57 % lokal, minus 28 % regional, minus 64 % bei ausschließlich NE 4/5)."),
    ("1. Jänner 2027: neue SNE-VO",
     "Mit der novellierten Systemnutzungsentgelte-Verordnung sollen auch lokale und regionale BEG, "
     "Peer-to-Peer und EVA reduzierte Netzentgelte bekommen. Die Höhe legt die E-Control fest, laut "
     "E-Control-Entwurf für 2027 49 % lokal, 22 % bzw. 58 % regional (Entwurf). Elektrizitätsabgabe wieder "
     "1,5 Cent, Erneuerbaren-Förderbeitrag laut Bundesregierung ausgesetzt."),
    ("April 2027: netzübergreifend und österreichweit",
     "Zuordnungen über mehrere Netzgebiete (z. B. Kärnten und Wien) und der Standortbereich sollen in der "
     "Praxis umsetzbar werden."),
    ("2028: flexibler Teilnahmefaktor",
     "Der Teilnahmefaktor bei der Mehrfachteilnahme soll mehrmals täglich statt einmal täglich änderbar sein."),
])}
<p>Die Befreiung von Elektrizitätsabgabe und Erneuerbaren-Förderbeitrag gilt derzeit nur für die EEG, für
Peer-to-Peer und EVA ist sie nicht geregelt. Ihr Wert hängt am Jahr: Die Elektrizitätsabgabe beträgt 2026
befristet 0,1 Cent für Haushalte und 0,82 Cent für Unternehmen, ab 2027 wieder 1,5 Cent je Kilowattstunde.
Den Erneuerbaren-Förderbeitrag und die Erneuerbaren-Förderpauschale setzt die Bundesregierung 2027 laut BMF
für alle Stromkunden aus. Der Abgabenvorteil der EEG beträgt 2027 damit rund 1,5 Cent je zugeordneter
Kilowattstunde. Neu ist außerdem der Versorgungsinfrastrukturbeitrag für
Einspeiser mit mehr als 20 kW, gedeckelt mit durchschnittlich 0,5 Euro je Megawattstunde (0,05 Cent je
Kilowattstunde), für eine typische Einfamilienhaus-Anlage nicht relevant. Wir aktualisieren diesen Artikel,
sobald die neue Verordnung vorliegt.</p>
"""),
        ("Energiegemeinschaft in Kärnten und der Steiermark", "regional", f"""
<p>Kärnten liefert mit rund 1.050 bis 1.150 Kilowattstunden je installiertem Kilowattpeak die höchsten
PV-Erträge Österreichs und ist kleinteilig besiedelt: Viele Ortschaften hängen an einem gemeinsamen
Trafo, was lokale Gemeinschaften mit dem vollen Abschlag erleichtert. Netzbetreiber ist überwiegend die
Kärnten Netz GmbH, im Stadtgebiet Klagenfurt die Energie Klagenfurt GmbH, in der Steiermark sind es die
Energienetze Steiermark und in Graz die Stromnetz Graz.
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
Gemeinden die {a('eg_gewerbe', 'Energiegemeinschaft für Gewerbe und Gemeinden')}. Ausgeführte Anlagen vom
Einfamilienhaus bis zum Gewerbedach zeigen unsere {a('referenzen', 'Referenzprojekte in Kärnten und Österreich')}.</p>
<p>Eine eigene Förderung für die Teilnahme gibt es nicht. Gefördert wird die PV-Anlage über die
Landesförderungen, etwa 3.000 Euro Pauschale in Kärnten (nur mit Speicher); der EAG-Investitionszuschuss des
Bundes ist derzeit nicht beantragbar, der letzte Call endete am 22. Oktober 2026, für 2027 ist laut BMWET eine
Systemförderung geplant (nicht beschlossen). Wer ein Energiemanagementsystem einsetzt, kann seit
Juni 2026 die {a('/ems-foerderung/', 'EMS-Förderung des Klimafonds')} nutzen: Die Teilnahme an einer
Energiegemeinschaft ist dort eine der sechs zulässigen Betriebsoptionen.</p>
"""),
        ("Fazit: Energiegemeinschaft", "fazit", f"""
<p>Die Energiegemeinschaft macht lokal erzeugten Strom für mehrere Teilnehmer nutzbar und wirkt an zwei
Stellen: Erzeuger bekommen einen fix vereinbarten Preis, typisch 8 bis 12 Cent, für den zugeordneten
Überschuss (der OeMAG-Tarif schwankte 2026 zwischen 6,146 Cent im Juli und 14,874 Cent im Oktober), Abnehmer
sparen in einer lokalen EEG bis zu 57 Prozent Netzentgelt plus Abgaben. Welches der fünf ElWG-Modelle passt,
hängt von Gebäude, Nahbereich und Teilnehmern ab. Beides gilt nur für die zugeordnete Menge, deshalb
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
                 "in Kärnten und der Steiermark, mit zertifizierten Fachkräften. "
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
         "erzeugen, teilen und verbrauchen. Mitglieder einer lokalen Erneuerbare-Energie-Gemeinschaft zahlen "
         "für den zugeordneten Strom einen selbst vereinbarten Preis und bis zu 57 Prozent weniger Netzentgelt."),
        ("Wie funktioniert eine Energiegemeinschaft in Österreich?",
         "Erzeuger speisen ihren Überschuss wie bisher ins Netz, Smart Meter messen Einspeisung und Verbrauch "
         "in Viertelstundenwerten. Der Netzbetreiber ordnet für jede Viertelstunde zu, wie viel Erzeugung auf "
         "wie viel Verbrauch in der Gemeinschaft trifft, und die Gemeinschaft rechnet diese Menge zum EG-Preis "
         "ab. Den Reststrom liefert weiterhin Ihr Lieferant, nicht zugeordneter Überschuss geht an die OeMAG "
         "oder Ihren Einspeisevertrag."),
        ("Welche Arten von Energiegemeinschaften gibt es?",
         "Das ElWG kennt seit 1. Oktober 2026 fünf Bürgerenergie-Modelle: die gemeinschaftliche "
         "Erzeugungsanlage (GEA) im selben Gebäude, die Erneuerbare-Energie-Gemeinschaft (EEG) im Nahbereich mit "
         "Netzentgelt-Rabatt und Abgabenbefreiung, die Bürgerenergiegemeinschaft (BEG) auch über mehrere "
         "Netzgebiete, den Peer-to-Peer-Vertrag zwischen einzelnen Personen und die Eigenversorgungsanlage (EVA) "
         "für eine Person mit mehreren Standorten. Mit einem Zählpunkt sind bis zu fünf Modelle gleichzeitig möglich."),
        ("Kann ich als Privatperson eine Energiegemeinschaft gründen?",
         "Ja. Natürliche Personen dürfen eine EEG oder BEG gründen, nötig sind mindestens zwei Teilnehmer und "
         "eine Rechtsform, meist ein Verein. Ohne Verein geht es seit Oktober 2026 per Peer-to-Peer-Vertrag mit "
         "einer zweiten Person oder als Eigenversorgungsanlage mit sich selbst an mehreren Standorten. Ablauf und "
         "Kosten stehen im Artikel " + a('/energiegemeinschaft-gruenden/', 'Energiegemeinschaft gründen') +
         ", für die meisten Haushalte ist der Beitritt zu einer bestehenden Gemeinschaft schneller."),
        ("Kann ich Strom auch mit Verwandten in einem anderen Bundesland teilen?",
         "Grundsätzlich ja, über eine Bürgerenergiegemeinschaft oder einen Peer-to-Peer-Vertrag. In der "
         "Übergangsphase seit Oktober 2026 lassen sich neue Zuordnungen laut Koordinationsstelle aber nur mit "
         "Zählpunkten beim selben Netzbetreiber umsetzen, netzübergreifend (z. B. Kärnten und Wien) "
         "voraussichtlich ab April 2027. Netzentgelt-Rabatt und Abgabenbefreiung gibt es dafür nicht, weil der "
         "Strom außerhalb des Nahbereichs fließt."),
        ("Wie viel kann ich sparen?",
         "Abnehmer sparen auf die zugeordnete Menge rund 6 bis 6,5 Cent je Kilowattstunde aus Netz und Abgaben "
         "(lokale EEG, Richtwerte 2026 und 2027; die Elektrizitätsabgabe ist 2026 befristet gesenkt, der "
         "Förderbeitrag 2027 ausgesetzt) plus die Differenz zwischen Lieferantenpreis und EG-Preis. Erzeuger "
         "bekommen einen fixen EG-Preis von typisch 8 bis 12 Cent; der OeMAG-Tarif schwankte 2026 zwischen 6,146 Cent "
         "(Juli) und 14,874 Cent (Oktober), der EG-Preis liegt je nach Monat darüber oder darunter. Laut Erfahrungsberichten liegt der "
         "Jahresvorteil eines Haushalts typisch bei 100 bis 300 Euro, abhängig von der Zuordnungsquote."),
        ("Brauche ich eine eigene PV-Anlage?",
         "Nein. Sie können als reiner Abnehmer teilnehmen und sparen Netzentgelt und Abgaben auf den EG-Strom. "
         "Mit eigener PV-Anlage nutzen Sie zusätzlich den Eigenverbrauch und verkaufen den zugeordneten "
         "Überschuss zu einem planbaren EG-Preis statt zum schwankenden OeMAG-Tarif."),
        ("Muss ich meinen Stromlieferanten oder den OeMAG-Vertrag kündigen?",
         "Nein, beides bleibt bestehen. Die Gemeinschaft deckt nur den Anteil, der zeitgleich erzeugt und "
         "verbraucht wird. Den Rest liefert weiterhin Ihr Lieferant, nicht zugeordneter Überschuss geht wie "
         "bisher an die OeMAG oder Ihren Einspeisevertrag."),
        ("Welche Voraussetzungen brauche ich?",
         "Einen eigenen Zählpunkt, einen Smart Meter mit aktivierten Viertelstundenwerten (Opt-in beim "
         "Netzbetreiber) und einen Anschluss im Nahbereich der Gemeinschaft. Große Unternehmen ab 250 "
         "Mitarbeitern dürfen an Bürgerenergiegemeinschaften und Peer-to-Peer-Verträgen teilnehmen, nicht an EEGs."),
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
        ("Koordinationsstelle für Energiegemeinschaften: FAQs zum ElWG",
         "https://energiegemeinschaften.gv.at/faqs-zum-elwg/"),
        ("Koordinationsstelle: Bürgerenergie-Modelle und Nahebereiche",
         "https://energiegemeinschaften.gv.at/gemeinsame-energienutzung/"),
        ("Koordinationsstelle: Energiegemeinschaften (EEG und BEG)",
         "https://energiegemeinschaften.gv.at/energiegemeinschaften-eeg-beg/"),
        ("Koordinationsstelle: Bürgerenergiegemeinschaften (BEG)",
         "https://energiegemeinschaften.gv.at/buergerenergiegemeinschaften-beg/"),
        ("Koordinationsstelle: Gemeinschaftliche Erzeugungsanlagen (GEA)",
         "https://energiegemeinschaften.gv.at/gemeinschaftliche-erzeugungsanlagen/"),
        ("Koordinationsstelle: Peer-to-Peer-Verträge", "https://energiegemeinschaften.gv.at/peer-to-peer-vertraege/"),
        ("Koordinationsstelle: Eigenversorgungsanlage (EVA)",
         "https://energiegemeinschaften.gv.at/eigenversorgungsanlage/"),
        ("Koordinationsstelle: Mehrfachteilnahme", "https://energiegemeinschaften.gv.at/mehrfachteilnahme/"),
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/marktpreis"),
        ("Parlament: Nationalrat beschließt Senkung der Elektrizitätsabgabe",
         "https://www.parlament.gv.at/aktuelles/news/Nationalrat-beschliesst-Senkung-der-Elektrizitaetsabgabe"),
        ("BMF: Aussetzung von Ökostrompauschale und Förderbeitrag 2027",
         "https://www.bmf.gv.at/presse/pressemeldungen/2026/november-2026/oekostrompauschale.html"),
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
