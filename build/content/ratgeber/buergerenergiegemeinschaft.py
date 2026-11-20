"""Ratgeber: Bürgerenergiegemeinschaft (BEG) in Österreich, österreichweit Strom teilen, Unterschied zur EEG.

Neuer Artikel (kein WordPress-Vorgänger), erstellt 2026-11-20 (Cluster Energiegemeinschaft, Runde 2).
Ziel-Keywords (Google Ads, Österreich, 20.11.2026): bürgerenergiegemeinschaft 170, beg kärnten 140
(navigational, meint die BEG Kärnten), beg energiegemeinschaft 90, bürgerenergiegemeinschaft österreich 50,
bürgerenergiegemeinschaft kärnten 20, bürgerenergiegemeinschaft gründen 10. Ohne messbares Volumen:
unterschied eeg beg, energiegemeinschaft österreichweit, strom teilen österreichweit, bürgerenergiegemeinschaft beitreten.

Faktenbasis (am 20.11.2026 selbst geöffnet): energiegemeinschaften.gv.at (Seiten /buergerenergiegemeinschaft/,
/energiegemeinschaften-eeg-beg/, /faqs-zum-elwg/, /mehrfachteilnahme/, /schritte-zur-gruendung/), BMWET-Factsheet
"Bürgerenergie" (ElWG), Website BEG Kärnten (Konditionen abgerufen 20.11.2026), OeMAG-Marktpreis laut Faktenliste.
Verbindlich: Faktenliste build/seo/_fakten_2026-10.md, Abschnitt "VERBINDLICH AB 20.11.2026".
Eigene Rechnung: Rechenbeispiel 2.000 kWh x Marktpreis bzw. x 10 ct (Beispielwert aus dem EG-Rechner).
Nicht behauptet: Höhe der Netzentgelt-Reduktion für BEG ab 2027, Abgabenbefreiung für BEG, Energiepreise einzelner
Lieferanten, BEG-Angebot über energyfamily, Zahl der BEGs in Österreich.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "buergerenergiegemeinschaft",
    "path": "/buergerenergiegemeinschaft/",
    "cluster": "Energiegemeinschaft",
    "title": "Bürgerenergiegemeinschaft (BEG): Unterschied zur EEG | EBZ",
    "description": ("Bürgerenergiegemeinschaft (BEG): Strom österreichweit teilen, volle Netzentgelte, "
                    "netzübergreifend voraussichtlich ab April 2027. Der Unterschied zur EEG."),
    "eyebrow": "Energiegemeinschaft · Bürgerenergiegemeinschaft",
    "crumb_label": "Bürgerenergiegemeinschaft",
    "h1": "Bürgerenergiegemeinschaft (BEG): Strom österreichweit teilen und der Unterschied zur EEG",
    "lead": ("Eine Bürgerenergiegemeinschaft darf Strom über ganz Österreich verteilen, etwa von der PV-Anlage in "
             "Villach zur Tochter in Wien. Was dabei wegfällt, ist der Netzentgelt-Rabatt der lokalen "
             "Energiegemeinschaft, und genau das entscheidet, ob sich die BEG für Sie rechnet."),
    "chips": [
        "Ab <b>2 Mitgliedern</b>, Rechtsform nötig",
        "Österreichweit: <b>volle Netzentgelte</b>",
        "Abgabenbefreiung: <b>nur EEG</b>",
        "Netzübergreifend: <b>voraussichtlich ab April 2027</b>",
    ],
    "date_published": "2026-11-20",
    "date_modified": "2026-11-20",
    "hero_img": "eg_drohne",
    "hero_alt": "Luftaufnahme eines kleinen Dorfes zwischen Feldern und Waldrand im Abendlicht",

    "tldr": [
        "Die Bürgerenergiegemeinschaft (BEG) ist ein Verein oder eine Genossenschaft aus mindestens zwei "
        "Mitgliedern, die Strom erzeugen, speichern, verbrauchen und verkaufen. Anders als die EEG darf sie "
        "sich über mehrere Netzgebiete und ganz Österreich erstrecken, auch große Unternehmen dürfen mitmachen.",
        "In der Übergangsphase seit 5. Oktober 2026 lassen sich neue Zuordnungen laut Koordinationsstelle nur "
        "mit Zählpunkten beim selben Netzbetreiber umsetzen. Netzübergreifend, etwa Kärnten und Wien, geht das "
        "voraussichtlich ab April 2027.",
        "Wer österreichweit teilt, zahlt volle Netzentgelte. Einen reduzierten Netzarbeitspreis bekommt eine BEG "
        "nur im Lokal- oder Regionalbereich und erst mit der neuen Netzentgelt-Verordnung, voraussichtlich ab "
        "1. Jänner 2027. Die Befreiung von Elektrizitätsabgabe und Erneuerbaren-Förderbeitrag gilt nur für die EEG.",
        "Der Vorteil einer BEG ist ein frei vereinbarter, fixer Preis. Der OeMAG-Marktpreis schwankte 2026 "
        "zwischen 6,146 Cent (Juli) und 14,874 Cent (Oktober). Ob das Teilen mehr bringt als die Einspeisung, "
        "hängt vom Monat und vom vereinbarten Preis ab.",
        "Jeder Zählpunkt darf an bis zu 5 Modellen gleichzeitig teilnehmen, also etwa an einer lokalen EEG und "
        "an einer BEG mit der Familie.",
    ],
    "kpis": [
        ("2", "Mitglieder reichen für eine BEG"),
        ("5", "Modelle je Zählpunkt gleichzeitig"),
        ("April 2027", "netzübergreifend voraussichtlich möglich"),
        ("14,874 ct", "OeMAG-Marktpreis Oktober 2026"),
    ],

    "sections": [
        ("Was ist eine Bürgerenergiegemeinschaft?", "definition", f"""
<p><b>Eine Bürgerenergiegemeinschaft (BEG) ist ein Zusammenschluss von mindestens zwei Teilnehmenden in einer
eigenen Rechtsform, meist Verein oder Genossenschaft, der elektrische Energie erzeugt, speichert, verbraucht
und verkauft.</b> Gewinn darf dabei nicht im Vordergrund stehen, der Zweck sind ökologische, wirtschaftliche
oder soziale Vorteile für die Mitglieder. Grundlage ist seit 1. Oktober 2026 das
{a('/elwg-beschluss-oesterreich/', 'Elektrizitätswirtschaftsgesetz (ElWG)')}, das die BEG als eines von fünf
Bürgerenergie-Modellen regelt.</p>
<p>Drei Merkmale unterscheiden die BEG von der Erneuerbare-Energie-Gemeinschaft (EEG):</p>
<ul>
  <li><b>Wer mitmachen darf:</b> Privatpersonen, Gemeinden, öffentliche Stellen, kleine und mittlere
  Unternehmen und zusätzlich große Unternehmen. Große Unternehmen und Elektrizitätsunternehmen dürfen
  teilnehmen, aber die Gemeinschaft nicht kontrollieren. Die Kontrolle liegt bei natürlichen Personen,
  Gebietskörperschaften und Kleinunternehmen. Große Unternehmen dürfen laut Koordinationsstelle weiterhin
  nur an einer BEG teilnehmen, nicht an einer EEG; ihre Erzeugungsanlagen dürfen sie bis 6 MW je Zählpunkt
  teilen.</li>
  <li><b>Welche Energie:</b> Die BEG darf nur elektrische Energie erzeugen, speichern, verbrauchen und
  verkaufen. Laut Koordinationsstelle ist sie dabei nicht auf erneuerbare Quellen beschränkt.</li>
  <li><b>Wie weit:</b> Die BEG darf sich über die Gebiete mehrerer Netzbetreiber und über ganz Österreich
  erstrecken. Die EEG bleibt auf den Lokal- oder Regionalbereich begrenzt.</li>
</ul>
<p>Wie sich alle fünf Modelle (GEA, EEG, BEG, Peer-to-Peer, Eigenversorgungsanlage) unterscheiden, zeigt der
{a('/energiegemeinschaft-vergleich/', 'Vergleich der Energiegemeinschaften')}. Die Grundlagen stehen im
{a('eg', 'Leitartikel zur Energiegemeinschaft')}.</p>
"""),
        ("Österreichweit Strom teilen: Reichweite und Übergangsphase", "reichweite", f"""
<p><b>Eine Bürgerenergiegemeinschaft darf sich über ganz Österreich erstrecken. In der Übergangsphase seit
Oktober 2026 lassen sich neue Zuordnungen laut Koordinationsstelle aber vorübergehend nur mit Zählpunkten beim
selben Netzbetreiber umsetzen, netzübergreifend (zum Beispiel Kärnten und Wien) voraussichtlich ab April
2027.</b></p>
{A.table(
    ["Datum", "Was gilt"],
    [
        ["1. Oktober 2026", "Neue ElWG-Regeln zur gemeinsamen Energienutzung treten in Kraft"],
        ["ab 5. Oktober 2026", "Neue Möglichkeiten vorübergehend nur mit Zählpunkten beim selben Netzbetreiber"],
        ["Oktober bis Dezember 2026", "Reduzierter Netzarbeitspreis nur für Mitglieder lokaler oder regionaler EEGs"],
        ["voraussichtlich 1. Jänner 2027", "Neue Netzentgelt-Verordnung (SNE-VO): Reduktion auch für lokale und regionale BEG"],
        ["voraussichtlich ab April 2027", "Umsetzung über mehrere Netzgebiete bzw. österreichweit"],
    ],
    hl_cols=(0,),
)}
<p>Erstreckt sich eine BEG über mehrere Netzgebiete, schließt sie mit jedem Netzbetreiber einen eigenen
Vertrag "Betrieb einer Energiegemeinschaft" ab. Bei Mitgliedern in drei Netzgebieten sind das drei Verträge.
Bestehende Gemeinschaften wurden mit 1. Oktober 2026 ins neue System überführt, eine Neugründung ist nicht
nötig. Ob die Übergangsphase auch neue Mitglieder bestehender, netzübergreifender BEGs betrifft, sagt die
Koordinationsstelle nicht. Fragen Sie vor dem Beitritt bei der Gemeinschaft nach, ab wann Ihr Zählpunkt
zugeordnet werden kann.</p>
{A.box("Eltern in Villach und Kinder in Wien hängen an zwei verschiedenen Netzbetreibern. Eine Zuordnung "
       "über diese Grenze hinweg ist laut Koordinationsstelle voraussichtlich ab April 2027 möglich. Bis dahin "
       "geht eine neue BEG-Zuordnung nur innerhalb desselben Netzgebiets.",
       label="Beispiel:")}
"""),
        ("Netzentgelt und Abgaben in der BEG", "netzentgelt", f"""
<p><b>Wer in einer Bürgerenergiegemeinschaft österreichweit teilt, zahlt für den bezogenen Gemeinschaftsstrom
volle Netzentgelte, Elektrizitätsabgabe und Erneuerbaren-Förderbeitrag.</b> Ein Nahbereich, der einen Rabatt
auslöst, besteht nur, wenn Erzeugung und Verbrauch am selben Trafo (Lokalbereich, Netzebene 6 und 7, meist rund
1 km) oder am selben Umspannwerk (Regionalbereich, Netzebene 4 bis 7, rund 30 km) hängen.</p>
<ul>
  <li><b>Netzentgelt bis Ende 2026:</b> Den reduzierten Netzarbeitspreis (bisher minus 57 % lokal, minus 28 %
  regional, minus 64 % bei ausschließlich Netzebene 4 und 5) bekommen nur Mitglieder lokaler oder regionaler
  EEGs. Eine BEG bekommt 2026 keine Reduktion.</li>
  <li><b>Netzentgelt ab 2027:</b> Mit der novellierten SNE-VO, nach heutigem Stand ab 1. Jänner 2027, kann auch
  eine BEG den reduzierten Netzarbeitspreis erhalten, wenn sie nur im Lokal- oder Regionalbereich teilt. Die
  Höhe legt die E-Control per Verordnung fest. Die Reduktion gilt nur für den Verbrauch, nicht für die
  Einspeisung.</li>
  <li><b>Österreichweit:</b> keine Reduktion, auch nicht ab 2027.</li>
  <li><b>Abgaben:</b> Der Entfall des Erneuerbaren-Förderbeitrags und die Befreiung von der
  Elektrizitätsabgabe gelten derzeit nur für die EEG, nicht für die BEG. 2027 setzt die Bundesregierung den
  Förderbeitrag für alle Stromkunden aus; der Abgabenunterschied zur EEG ist dann die Elektrizitätsabgabe von
  1,5 Cent je kWh (2026 für Haushalte befristet 0,1 Cent).</li>
</ul>
<p>Wie sich Netzentgelt, Abgaben und Energiepreis auf der Stromrechnung zusammensetzen, erklärt
{a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft: Netzkosten und Abschläge')}.</p>
"""),
        ("Unterschied EEG und BEG im Überblick", "unterschied", f"""
<p><b>Die EEG ist auf den Nahbereich begrenzt und bekommt dafür Netzrabatt und Abgabenbefreiung. Die BEG darf
österreichweit teilen und große Unternehmen aufnehmen, verzichtet dafür aber auf die Abgabenbefreiung und
außerhalb des Nahbereichs auf den Netzrabatt.</b></p>
{A.table(
    ["", "Erneuerbare-Energie-Gemeinschaft (EEG)", "Bürgerenergiegemeinschaft (BEG)"],
    [
        ["Mitglieder", "Privatpersonen, Gemeinden, öffentliche Stellen, KMU",
         "dieselben, zusätzlich große Unternehmen (ohne Kontrolle)"],
        ["Rechtsform", "ja, z. B. Verein oder Genossenschaft", "ja, z. B. Verein oder Genossenschaft"],
        ["Energie", "erneuerbare Energie", "nur Strom, laut Koordinationsstelle nicht auf erneuerbare Quellen beschränkt"],
        ["Reichweite", "lokal oder regional", "lokal, regional oder österreichweit"],
        ["Netzentgelt 2026", "reduziert im Nahbereich", "voll"],
        ["Netzentgelt ab 2027 (voraussichtlich)", "reduziert im Nahbereich",
         "reduziert nur im Nahbereich, österreichweit voll"],
        ["Elektrizitätsabgabe, Förderbeitrag", "entfallen", "fallen an"],
        ["Registrierung bei ebUtilities", "als EEG", "als BEG, Gemeinschafts-ID selbst anlegen"],
    ],
    hl_cols=(2,),
)}
<p>Die Entscheidung zwischen EEG und BEG fällt vor der Registrierung bei ebUtilities, weil beide Modelle
unterschiedliche Marktpartner-IDs bekommen. Wer im Nahbereich teilt und nur Haushalte, Gemeinden und KMU an Bord hat,
fährt mit der EEG wirtschaftlich besser. Welche Gemeinschaften es in Ihrer Region gibt, zeigt
{a('/energiegemeinschaft-kaernten/', 'Energiegemeinschaft Kärnten')} bzw.
{a('/energiegemeinschaft-steiermark/', 'Energiegemeinschaft Steiermark')}.</p>
"""),
        ("Für wen sich eine Bürgerenergiegemeinschaft lohnt", "fuer-wen", f"""
<p><b>Eine BEG lohnt sich, wenn Erzeugung und Verbrauch weit auseinanderliegen und ein fester Preis wichtiger
ist als der Netzrabatt.</b> Typische Fälle:</p>
<ul>
  <li><b>Familie in einem anderen Bundesland:</b> Die Eltern haben eine PV-Anlage in Kärnten, die Tochter wohnt
  in Wien. Teilen ist mit einer BEG erlaubt, netzübergreifend voraussichtlich ab April 2027. Die Tochter zahlt
  für den Gemeinschaftsstrom volle Netzentgelte und Abgaben. Sparen kann sie nur beim Energiepreis, und nur dann,
  wenn der vereinbarte Preis unter dem ihres Lieferanten liegt. Den Preis legt die Gemeinschaft selbst fest,
  laut BMWET ist auch ein Nulltarif möglich.</li>
  <li><b>PV-Besitzer, die einen festen Preis wollen:</b> Der OeMAG-Marktpreis schwankt jeden Monat. Im Juli
  2026 lag er bei 6,146 Cent, im September bei 10,168 Cent, im Oktober bei 14,874 Cent je kWh (Stand November
  2026). Ein in der BEG vereinbarter Preis bleibt gleich, ist aber nicht in jedem Monat höher. Mehr dazu:
  {a('/oemag-einspeisetarif/', 'OeMAG-Einspeisetarif')} und {a('marktpreis', 'Marktpreis 2026')}.</li>
  <li><b>Große Unternehmen und Betriebe mit mehreren Standorten:</b> Sie können an keiner EEG teilnehmen, an
  einer BEG schon. Mehr für Betriebe und Gemeinden auf der Seite
  {a('eg_gewerbe', 'Energiegemeinschaft für Gewerbe und Gemeinden')}.</li>
</ul>
<p><b>Weniger geeignet</b> ist die BEG, wenn alle Beteiligten im selben Ort wohnen. Dann bringt eine lokale EEG
mehr, weil Netzrabatt und Abgabenbefreiung dazukommen. Für zwei Personen ohne Verein gibt es außerdem den
{a('/peer-to-peer-strom/', 'Peer-to-Peer-Vertrag')}; die Abgabenbefreiung der EEG gilt dort derzeit nicht.</p>
{A.cta("BEG, EEG oder beides?",
       "Wir prüfen, ob Ihr Zählpunkt lokal oder regional verbunden ist, und rechnen ehrlich durch, welches Modell "
       "bei Ihren Preisen mehr bringt.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("eg_privat", "Energiegemeinschaft mit EBZ"))}
"""),
        ("Rechenbeispiel: Überschuss an die Tochter in Wien statt an die OeMAG", "rechenbeispiel", f"""
<p><b>Ein fixer Preis in der BEG schlägt die Einspeisung nur in Monaten mit niedrigem Marktpreis.</b> Das zeigt
ein einfaches Beispiel: Eltern in Villach haben eine PV-Anlage. 2.000 kWh* ihres Überschusses verbraucht die
Tochter in Wien zeitgleich, diese Menge ordnet die BEG ihr zu. Die Familie vereinbart 10 Cent je kWh*.</p>
{A.table(
    ["Variante für 2.000 kWh*", "Preis je kWh", "Erlös der Eltern im Jahr*"],
    [
        ["BEG mit Familienpreis", "10 ct* (fix)", "200 €"],
        ["OeMAG, Marktpreis wie im Juli 2026", "6,146 ct", "rund 123 €"],
        ["OeMAG, Marktpreis wie im September 2026", "10,168 ct", "rund 203 €"],
        ["OeMAG, Marktpreis wie im Oktober 2026", "14,874 ct", "rund 297 €"],
    ],
    hl_cols=(2,),
)}
<p>Für die Eltern ist die BEG also kein sicheres Plus: Bei einem Marktpreis wie im Oktober bringt die
Einspeisung mehr, bei einem wie im Juli weniger. Für die Tochter zählt nur der Vergleich mit dem Energiepreis
ihres Lieferanten, denn Netzentgelte und Abgaben zahlt sie für die 2.000 kWh in voller Höhe wie bisher. Liegt
ihr Energiepreis 2 Cent über den 10 Cent der Familie, spart sie rund 40 Euro im Jahr*, liegt er darunter, zahlt
sie drauf. Davon gehen noch die Kosten für Verein und Abrechnung ab, siehe
{a('/energiegemeinschaft-kosten/', 'Energiegemeinschaft: Kosten')}.</p>
<p>Was dafür spricht: Das Geld bleibt in der Familie, und der Preis schwankt nicht. Wie viel Strom tatsächlich
zeitgleich verbraucht wird, hängt vom Lastprofil ab. Eine eigene Schätzung für die lokale EEG liefert der
{a('eg_rechner', 'Energiegemeinschaft-Rechner')}.</p>
<p><small>*Beispielwerte und eigene Rechnung: 2.000 kWh zugeordnete Menge und 10 Cent Familienpreis sind
angenommen (10 Cent ist auch der Beispielwert für die Einspeisung im EBZ-Rechner, keine EBZ-Kondition).
OeMAG-Marktpreise laut OeMAG, Stand November 2026; die Rechnung setzt einen Monatswert vereinfacht für das ganze
Jahr an. Ohne Umsatzsteuer und ohne Kosten der Gemeinschaft.</small></p>
"""),
        ("BEG beitreten oder gründen: so läuft es ab", "beitreten-gruenden", f"""
<p><b>Beitreten ist der einfachere Weg: Sie brauchen einen Smart Meter, werden Mitglied und legen mit der
Gemeinschaft fest, welcher Anteil Ihres Verbrauchs aus der BEG kommt.</b> Ihren bisherigen Stromlieferanten
behalten Sie für den Rest. Wie der Beitritt im Detail abläuft, steht im Artikel
{a('/energiegemeinschaft-beitreten/', 'Energiegemeinschaft beitreten')}, wie Sie eine Gemeinschaft suchen, unter
{a('/energiegemeinschaft-finden/', 'Energiegemeinschaft finden')}.</p>
<p>Ein Beispiel aus Kärnten: Die <b>BEG Kärnten</b> (Bürger Energie Gemeinschaft Kärnten) nennt auf ihrer
Website (abgerufen am 20. November 2026) einen fixen Bezugspreis von 12,00 Cent je kWh inklusive 20 % USt,
8,0 Cent je kWh für die Einspeisung, keine Anmelde- und keine Grundgebühr sowie Mitglieder bei 13
Netzbetreibern in 9 Bundesländern. Wir nennen sie als Beispiel, nicht als Empfehlung; Konditionen ändern
sich, prüfen Sie den aktuellen Stand direkt bei der Gemeinschaft.</p>
<p>Wer selbst gründen will, geht laut Koordinationsstelle so vor:</p>
{A.steps([
    ("Modell und Rahmen klären", "Wo stehen Erzeugung und Verbrauch, lohnt der Nahbereich (dann eher EEG)? Ab "
     "30 kW Erzeugungs- und Speicherleistung bei Haushalten bzw. 100 kW bei anderen Kunden gelten zusätzliche "
     "Lieferantenpflichten. Prüfen Sie auch, ob Ihr Stromvertrag die Teilnahme erlaubt."),
    ("Rechtsform gründen", "Für kleine und mittlere Gemeinschaften eignet sich meist ein Verein, für größere "
     "Projekte mit gemeinsamer Finanzierung eine Genossenschaft. Die Statuten müssen sicherstellen, dass die "
     "Kontrolle bei natürlichen Personen, Gemeinden oder Kleinunternehmen liegt."),
    ("Bei ebUtilities als BEG registrieren", "Die Gemeinschaft bekommt eine Marktpartner-ID und legt die "
     "Gemeinschafts-ID anders als eine EEG selbst im Dashboard an. Eine eigene Bilanzgruppe ist nicht nötig."),
    ("Verträge mit den Netzbetreibern", "Je Netzgebiet ein Vertrag \"Betrieb einer Energiegemeinschaft\". "
     "Netzübergreifend ist das voraussichtlich ab April 2027 umsetzbar."),
    ("Mitglieder aufnehmen", "Jedes Mitglied braucht einen Smart Meter; die Zählpunkte werden der Gemeinschaft "
     "mit einem Teilnahmefaktor zugeordnet."),
    ("Abrechnen", "Die Energiedaten kommen über das EDA-Portal, kostenlos bis 50 Zählpunkte je Marktpartner, "
     "darüber kostenpflichtig. Alternativ übernehmen Software oder ein Dienstleister die Abrechnung."),
])}
<p>Den Ablauf für eine Gemeinschaft im Nahbereich beschreibt
{a('/energiegemeinschaft-gruenden/', 'Energiegemeinschaft gründen')}.</p>
"""),
        ("BEG und lokale EEG gleichzeitig: Mehrfachteilnahme", "mehrfachteilnahme", f"""
<p><b>Seit dem ElWG darf jede Erzeugungs- oder Verbrauchsanlage an bis zu 5 Bürgerenergie-Modellen gleichzeitig
teilnehmen.</b> Sie können also Mitglied einer lokalen EEG mit Netzrabatt sein und zusätzlich einer BEG mit
der Familie in einem anderen Bundesland angehören.</p>
<ul>
  <li><b>Teilnahmefaktor:</b> Er legt fest, welcher Anteil des Verbrauchs je Gemeinschaft höchstens gedeckt
  wird. Bei 70 % deckt die Gemeinschaft von 1 kWh höchstens 0,7 kWh, den Rest liefert der Energieversorger. Alle
  Faktoren eines Zählpunkts zusammen dürfen 100 % nicht überschreiten.</li>
  <li><b>Änderungen:</b> einmal täglich, ab 2028 voraussichtlich mehrmals täglich, abgestimmt mit der
  Gemeinschaft, die Änderung läuft über das EDA-Portal.</li>
  <li><b>Übergangsphase:</b> Auch die Mehrfachteilnahme ist bis voraussichtlich April 2027 nur mit Zählpunkten
  beim selben Netzbetreiber umsetzbar.</li>
</ul>
{A.box("Für Haushalte in Kärnten oder der Steiermark ist oft die Kombination sinnvoll: den größeren Teil in "
       "die lokale EEG (Netzrabatt, Abgabenbefreiung), einen kleineren Teil in eine BEG mit Familie oder "
       "Freunden außerhalb des Nahbereichs.", label="Unsere Einschätzung:")}
"""),
        ("Fazit: Die BEG ist das Modell für weite Wege, nicht für Rabatte", "fazit", f"""
<p>Die Bürgerenergiegemeinschaft macht möglich, was die EEG nicht kann: Strom über Netzgrenzen und
Bundesländer hinweg zu teilen und große Unternehmen einzubinden. Netzübergreifend geht das voraussichtlich ab
April 2027, österreichweit immer mit vollen Netzentgelten und Abgaben. Wer im Nahbereich teilen kann, fährt mit
der EEG besser; wer Familie oder Betriebsstandorte weit weg hat, nutzt die BEG zusätzlich. Die Grundlage ist
in jedem Fall eine PV-Anlage, die mehr erzeugt, als im Haus gebraucht wird. Wie das in der Praxis aussieht,
zeigen unsere {a('referenzen', 'Referenzen')}.</p>
<p><small>*Beispielwerte und eigene Berechnungen, siehe Fußnote im Rechenbeispiel. Rechtsstand November
2026 laut Koordinationsstelle für Energiegemeinschaften; Termine zur Übergangsphase und zur SNE-VO sind
Voraussichtswerte und können sich ändern. Keine Rechts- oder Steuerberatung.</small></p>
{A.cta("Photovoltaik planen, Teilen gleich mitdenken",
       "EBZ plant und montiert PV-Anlagen in Kärnten und der Steiermark, prüft Ihren Nahbereich und bindet Sie "
       "an eine passende Gemeinschaft an.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("eg_privat", "Zur Leistungsseite"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Energiegemeinschaft: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und Wallboxen "
                 "in Kärnten und der Steiermark, mit zertifizierten Fachkräften und einem festen Ansprechpartner "
                 "von der Planung bis zur Übergabe. Wir verkaufen keinen Strom, sondern sorgen dafür, dass Ihre "
                 "Anlage zum Teilen passt: Wir binden Sie an eine Gemeinschaft an, abgerechnet über die Plattform "
                 "unseres Partners energyfamily, und helfen bei der Gründung im Nahbereich."),
        "grid": [
            ("Nahbereich geprüft", "Wir klären, ob Ihr Zählpunkt lokal oder regional verbunden ist."),
            ("Ehrlicher Vergleich", "EEG, BEG oder Einspeisung, gerechnet mit Ihren Preisen."),
            ("Anlage zum Teilen", "PV, Speicher und Energiemanagement passend zum Überschuss."),
            ("Kostenlose Erstberatung", "Telefonisch oder vor Ort in Kärnten und der Steiermark."),
        ],
    },

    "faq": [
        ("Was ist eine Bürgerenergiegemeinschaft?",
         "Eine Bürgerenergiegemeinschaft (BEG) ist ein Verein oder eine Genossenschaft aus mindestens zwei "
         "Mitgliedern, die Strom erzeugen, speichern, verbrauchen und verkaufen. Sie darf sich über mehrere "
         "Netzgebiete und ganz Österreich erstrecken, auch große Unternehmen dürfen teilnehmen, aber nicht die "
         "Kontrolle übernehmen. Gewinn darf nicht im Vordergrund stehen."),
        ("Was ist der Unterschied zwischen EEG und BEG?",
         "Die EEG ist auf den Lokal- oder Regionalbereich begrenzt und bekommt dafür reduzierte Netzentgelte und "
         "die Befreiung von Elektrizitätsabgabe und Erneuerbaren-Förderbeitrag. Die BEG darf österreichweit teilen "
         "und große Unternehmen aufnehmen, zahlt aber die Abgaben und österreichweit volle Netzentgelte."),
        ("Kann ich mit einer BEG Strom österreichweit teilen?",
         "Rechtlich ja, die BEG darf sich über ganz Österreich erstrecken. In der Übergangsphase seit 5. Oktober "
         "2026 lassen sich neue Zuordnungen laut Koordinationsstelle aber nur mit Zählpunkten beim selben "
         "Netzbetreiber umsetzen. Netzübergreifend, etwa zwischen Kärnten und Wien, geht das voraussichtlich ab "
         "April 2027."),
        ("Bekommt eine Bürgerenergiegemeinschaft reduzierte Netzentgelte?",
         "2026 nicht, bis Jahresende bekommen nur Mitglieder lokaler oder regionaler EEGs den reduzierten "
         "Netzarbeitspreis. Mit der neuen SNE-VO, voraussichtlich ab 1. Jänner 2027, kann auch eine BEG ihn "
         "erhalten, wenn sie nur im Lokal- oder Regionalbereich teilt. Österreichweit bleibt es bei vollen "
         "Netzentgelten; die Höhe der Reduktion legt die E-Control fest."),
        ("Muss ich in einer BEG Elektrizitätsabgabe zahlen?",
         "Ja. Der Entfall des Erneuerbaren-Förderbeitrags und die Befreiung von der Elektrizitätsabgabe gelten "
         "derzeit nur für Erneuerbare-Energie-Gemeinschaften. In einer BEG fallen beide Abgaben auf den bezogenen "
         "Gemeinschaftsstrom an, wie beim normalen Lieferanten. Den Förderbeitrag setzt die Bundesregierung 2027 "
         "für alle aus, die Elektrizitätsabgabe beträgt dann wieder 1,5 Cent je kWh (2026 für Haushalte 0,1 Cent)."),
        ("Kann ich gleichzeitig in einer EEG und einer BEG sein?",
         "Ja, jeder Zählpunkt darf an bis zu 5 Bürgerenergie-Modellen teilnehmen. Ein Teilnahmefaktor legt fest, "
         "welchen Anteil jede Gemeinschaft höchstens deckt, zusammen höchstens 100 %. Bis voraussichtlich April "
         "2027 geht das nur mit Zählpunkten beim selben Netzbetreiber."),
        ("Kann ich als Privatperson eine Bürgerenergiegemeinschaft gründen?",
         "Ja, schon zwei Privatpersonen können eine BEG gründen, sie brauchen aber eine Rechtsform wie einen "
         "Verein, eine Registrierung bei ebUtilities und je Netzgebiet einen Vertrag mit dem Netzbetreiber. Für "
         "kleine Gruppen ist der Beitritt zu einer bestehenden Gemeinschaft meist einfacher."),
        ("Was ist die BEG Kärnten?",
         "Die BEG Kärnten (Bürger Energie Gemeinschaft Kärnten) ist eine bestehende Bürgerenergiegemeinschaft. "
         "Laut ihrer Website (abgerufen am 20. November 2026) hat sie Mitglieder bei 13 Netzbetreibern in 9 "
         "Bundesländern und nennt 12,00 Cent je kWh inklusive USt für den Bezug und 8,0 Cent für die Einspeisung. "
         "Aktuelle Konditionen erfragen Sie direkt bei der Gemeinschaft."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Mit zertifizierten Fachkräften plant und "
                    "installiert EBZ Energie PV-Anlagen, Speicher und Wärmepumpen in Kärnten und der Steiermark und "
                    "begleitet Haushalte und Betriebe beim Einstieg in Energiegemeinschaften. Die Inhalte folgen den "
                    "Angaben der Koordinationsstelle für Energiegemeinschaften (Stand November 2026). Keine Rechts- "
                    "oder Steuerberatung."),
    "sources": [
        ("Koordinationsstelle für Energiegemeinschaften: Bürgerenergiegemeinschaften",
         "https://energiegemeinschaften.gv.at/buergerenergiegemeinschaft/"),
        ("Koordinationsstelle: Energiegemeinschaften (EEG und BEG)",
         "https://energiegemeinschaften.gv.at/energiegemeinschaften-eeg-beg/"),
        ("Koordinationsstelle: FAQs zum ElWG", "https://energiegemeinschaften.gv.at/faqs-zum-elwg/"),
        ("Koordinationsstelle: Mehrfachteilnahme", "https://energiegemeinschaften.gv.at/mehrfachteilnahme/"),
        ("Koordinationsstelle: Schritte zur Gründung", "https://energiegemeinschaften.gv.at/schritte-zur-gruendung/"),
        ("BMWET: Factsheet Bürgerenergie (ElWG)",
         "https://www.bmwet.gv.at/dam/jcr:ecd60188-efdc-459d-b248-d0dd5ae1b9e0/ElWG-Factsheets_Buergerenergie.pdf"),
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/de/marktpreis/"),
        ("BEG Kärnten: Konditionen (abgerufen 20.11.2026)", "https://www.beg-kaernten.at/"),
        ("Parlament: Nationalrat beschließt Senkung der Elektrizitätsabgabe",
         "https://www.parlament.gv.at/aktuelles/news/Nationalrat-beschliesst-Senkung-der-Elektrizitaetsabgabe"),
        ("BMF: Aussetzung von Ökostrompauschale und Förderbeitrag 2027",
         "https://www.bmf.gv.at/presse/pressemeldungen/2026/november-2026/oekostrompauschale.html"),
    ],
    "related": [
        ("/energiegemeinschaft-vergleich/", "Energiegemeinschaften im Vergleich: GEA, EEG, BEG, P2P"),
        ("/peer-to-peer-strom/", "Peer-to-Peer-Strom: direkt verkaufen oder verschenken"),
        ("/energiegemeinschaft-netzkosten/", "Energiegemeinschaft: Netzkosten und Abschläge"),
        ("eg_privat", "Energiegemeinschaft mit EBZ: Leistungsseite für Privatkunden"),
    ],
    "cta": {
        "h3": "BEG, EEG oder beides?",
        "text": "Wir prüfen Ihren Nahbereich und rechnen ehrlich durch, welches Modell sich für Sie lohnt.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Strom teilen, ehrlich gerechnet",
    "final_text": ("Kostenlose Erstberatung zu Photovoltaik, Speicher und Energiegemeinschaft, mit transparenten "
                   "Zahlen und einem Ansprechpartner aus Villach."),
}
