"""Ratgeber: Gemeinschaftliche Erzeugungsanlage (GEA), PV im Mehrparteienhaus.

Neuer Artikel (kein WordPress-Vorgänger), erstellt 2026-11-20 (Cluster Energiegemeinschaft, Runde 2).
Ziel-Keywords (Google Ads, Österreich, 20.11.2026): gemeinschaftliche erzeugungsanlage 170,
gea gemeinschaftliche erzeugungsanlage 20, gea strom 20, je 10: photovoltaik mehrparteienhaus,
pv anlage mehrparteienhaus, pv anlage mehrfamilienhaus, photovoltaik mehrfamilienhaus, photovoltaik
wohnungseigentum, pv anlage eigentümergemeinschaft, photovoltaik eigentümergemeinschaft, photovoltaik
mietshaus, mieterstrom; ohne Volumen: gea photovoltaik, energiegemeinschaft mehrfamilienhaus.
SERP-Frage "Nutzer fragen auch": "Was ist eine gemeinschaftliche Erzeugungsanlage?", "Welche Änderungen
bringt das neue PV-Gesetz 2026 in Österreich?".

Faktenbasis (alle am 20.11.2026 selbst geöffnet): energiegemeinschaften.gv.at (Seiten
gemeinschaftliche-erzeugungsanlagen, was-sind-geas, betriebsmodelle-gruendungsschritte,
messung-und-aufteilung, wirtschaftliche-ueberlegungen, mehrfachteilnahme, faqs-zum-elwg FAQ 1.3/1.5/4.1/4.2/
4.4/4.6, faqs Abschnitt 9 zur GEA nach bisherigem Recht), WEG 2002 §§ 24 und 29 (Volltext über jusline.at,
RIS war am 20.11.2026 per Sicherheitsprüfung gesperrt), Fachbeitrag forum-media.at (Reßler, 05.04.2023,
OGH 5 Ob 161/17p und 5 Ob 137/21i), IEA PVPS National Survey Report Austria 2024 (Systempreise),
OeMAG-Marktpreis laut zentraler Faktenliste, EAG-Status laut Faktenliste.
Nicht behauptet: Höhe der Netzentgelt-Reduktion im Standortbereich (E-Control-Verordnung offen),
Abgabenbefreiung im Standortbereich (offen), konkrete GEA-Kosten je Wohnung (keine neutrale Quelle),
Landesförderung speziell für GEA in Kärnten/Steiermark (nicht belegt), dass die Referenz Krumpendorf eine
GEA ist (unbekannt).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "gemeinschaftliche-erzeugungsanlage",
    "path": "/gemeinschaftliche-erzeugungsanlage/",
    "cluster": "Energiegemeinschaft",
    "title": "Gemeinschaftliche Erzeugungsanlage: PV fürs Wohnhaus | EBZ",
    "description": ("Gemeinschaftliche Erzeugungsanlage (GEA): PV-Strom im Mehrparteienhaus auf die Wohnungen "
                    "verteilen. Ab 2 Parteien, kein Netzentgelt im Haus, WEG-Beschluss."),
    "eyebrow": "Energiegemeinschaft · Mehrparteienhaus",
    "crumb_label": "Gemeinschaftliche Erzeugungsanlage",
    "h1": "Gemeinschaftliche Erzeugungsanlage (GEA): PV-Strom im Mehrparteienhaus teilen, ab 2 Parteien",
    "lead": ("Ein Dach, viele Wohnungen, aber jede hat ihren eigenen Zähler: Genau dafür gibt es die "
             "gemeinschaftliche Erzeugungsanlage. Dieser Ratgeber erklärt, wer sie betreiben darf, wie der "
             "Strom aufgeteilt wird, was das neue ElWG ändert und welche Beschlüsse im Wohnungseigentum nötig "
             "sind."),
    "chips": [
        "Teilnehmer: <b>ab 2 Parteien</b>",
        "Strom im Haus: <b>kein öffentliches Netz</b>",
        "Teilnahme: <b>freiwillig</b>",
        "Standortbereich: <b>voraussichtlich ab April 2027</b>",
    ],
    "date_published": "2026-11-20",
    "date_modified": "2026-11-20",
    "hero_img": "ref_krumpendorf",
    "hero_alt": ("Drohnenaufnahme einer 25-kWp-Photovoltaikanlage von EBZ auf dem roten Dach eines "
                 "Mehrparteienhauses in Krumpendorf am Wörthersee"),

    "tldr": [
        "Eine gemeinschaftliche Erzeugungsanlage (GEA) ist meist eine PV-Anlage auf einem Mehrparteienhaus, "
        "deren Strom mehrere Wohnungen oder Betriebe an derselben Hauptleitung nutzen. Seit 2017 sind laut "
        "Koordinationsstelle über 3.500 GEA in Österreich in Betrieb.",
        "Die Teilnahme ist freiwillig. Reststrom kommt weiter vom frei wählbaren Lieferanten, jede Partei "
        "behält ihren Zähler und ihren Vertrag.",
        "Der Strom aus der GEA nutzt das öffentliche Netz nicht: Dafür fallen laut Koordinationsstelle keine "
        "Netzentgelte und kein Erneuerbaren-Förderbeitrag an, die Elektrizitätsabgabe entfällt.",
        "Neu mit dem ElWG ist der Standortbereich (mehrere Steigleitungen am selben Hausanschlusskasten). "
        "Dort legt die E-Control die Netzentgelte per Verordnung fest, umsetzbar voraussichtlich ab April 2027.",
        "Im Wohnungseigentum reicht für eine Anlage, die allen offensteht, in der Regel ein Mehrheitsbeschluss "
        "nach § 29 WEG 2002. Überstimmte können binnen 3 Monaten ab Anschlag anfechten.",
    ],
    "kpis": [
        ("über 3.500", "GEA in Österreich seit 2017"),
        ("ab 2", "Parteien an einer Hauptleitung"),
        ("bis zu 5", "Bürgerenergie-Modelle je Zählpunkt"),
        ("April 2027", "Standortbereich voraussichtlich"),
    ],

    "sections": [
        ("Was ist eine gemeinschaftliche Erzeugungsanlage?", "definition", f"""
<p><b>Eine gemeinschaftliche Erzeugungsanlage (GEA) ist eine Stromerzeugungsanlage, meist Photovoltaik am
Dach, deren Strom mehrere Parteien im selben Gebäude direkt nutzen.</b> Die Teilnehmenden hängen an
derselben Hauptleitung (Steigleitung) bzw. derselben Sammelschiene. Der Strom fließt vom Dach über die
Hausleitung in die Wohnungen, das öffentliche Verteilernetz wird dafür nicht genutzt.</p>
<p>Das Modell gibt es seit 2017, damals im ElWOG 2010 (§ 16a) geregelt. Seit 1. Oktober 2026 gilt das neue
Elektrizitätswirtschaftsgesetz (ElWG): Die GEA ist dort in § 6 Abs. 1 Z 58 definiert und gehört zu den
Nahebereichen nach § 70 Abs. 6 ElWG. Bestehende GEA wurden laut Koordinationsstelle für
Energiegemeinschaften mit 1. Oktober 2026 ins neue System übergeführt, eine Neugründung ist nicht nötig.
Weil sich mit diesem Datum aber Rechte und Pflichten ändern, sollten bestehende Verträge geprüft werden.</p>
{A.table(
    ["Merkmal", "Gemeinschaftliche Erzeugungsanlage"],
    [
        ["Typischer Ort", "Mehrparteienhaus, Wohnhausanlage, Gebäude mit mehreren Betrieben"],
        ["Technik", "meist Photovoltaik, möglich auch Wind, Kleinwasserkraft, Kraft-Wärme-Kopplung"],
        ["Verbindung", "dieselbe Hauptleitung bzw. Sammelschiene, kein öffentliches Netz"],
        ["Teilnehmer", "Zählpunktinhaber: natürliche oder juristische Personen, eingetragene Personengesellschaften"],
        ["Mindestgröße", "kein Mindestwert im Gesetz, in der Regel ab 2 Parteien"],
        ["Rechtsform", "nicht zwingend, ein Vertrag zwischen Betreiber und Teilnehmern reicht"],
    ],
    hl_cols=(1,),
)}
<p>Alle Bürgerenergie-Modelle (GEA, Erneuerbare-Energie-Gemeinschaft, Bürgerenergiegemeinschaft,
Peer-to-Peer, Eigenversorgungsanlage) im Überblick erklärt der {a('eg', 'Leitartikel Energiegemeinschaft')}.</p>
"""),
        ("Wer betreibt die GEA und wer macht mit?", "betreiber", f"""
<p><b>Betreiben kann die Anlage, wer das Dach nutzen darf und die Verantwortung übernimmt: die
Eigentümergemeinschaft, einzelne Eigentümer, die Hausverwaltung, ein Bewohnerverein oder ein externer
Dienstleister.</b> Die Koordinationsstelle beschreibt vier typische Betriebsmodelle:</p>
{A.table(
    ["Betriebsmodell", "So funktioniert es", "Passt für"],
    [
        ["Gebäudeeigentümer oder Hausverwaltung", "betreibt die Anlage und stellt den Strom den Bewohnern zur Verfügung",
         "Mietshaus, gemeinnütziger Wohnbau, Neubau"],
        ["Bewohnerverein", "pachtet das Dach, errichtet und betreibt die Anlage, Tarif und Aufteilung stehen in den Statuten",
         "Häuser, in denen nicht alle mitmachen"],
        ["Wohnungseigentümergemeinschaft", "die Gemeinschaft oder einzelne Eigentümer betreiben die Anlage",
         "Eigentumswohnhaus"],
        ["Externer Dienstleister oder Energieversorger", "pachtet das Dach, haftet für den Betrieb, Bewohner zahlen einen festen Preis",
         "wer selbst nicht investieren will"],
    ],
    hl_cols=(0,),
)}
<ul>
  <li><b>Freiwillig:</b> Jede Partei an der Hauptleitung kann mitmachen oder verzichten. Wer nicht teilnimmt,
  bleibt wie bisher beim eigenen Lieferanten.</li>
  <li><b>Reststrom frei wählbar:</b> Was die Anlage nicht liefert, kommt vom Stromlieferanten, den jede
  Partei selbst wählt. Der bestehende Liefervertrag bleibt.</li>
  <li><b>Kein Stromhändler:</b> Wer eine GEA betreibt, wird dadurch laut Koordinationsstelle nicht zum
  Lieferanten und braucht keine Konzession.</li>
  <li><b>Mieter:</b> können Strom beziehen und auch investieren. Das Modell sollte so gebaut sein, dass mit
  dem Ende des Mietvertrags ein einfacher Ausstieg möglich ist.</li>
</ul>
"""),
        ("Wie wird der Strom auf die Wohnungen aufgeteilt?", "aufteilung", f"""
<p><b>Grundlage sind Viertelstundenwerte aus den Smart Metern aller Teilnehmer. Im Regelfall teilt der
Netzbetreiber den Strom dynamisch auf: In jeder Viertelstunde bekommt jede Wohnung Strom nach ihrem
tatsächlichen Verbrauch, höchstens so viel, wie sie gerade braucht.</b> Eine feste Quote (statische
Aufteilung) können ältere Gemeinschaften noch verwenden, für neue ist sie laut Koordinationsstelle nicht
mehr vorgesehen.</p>
{A.table(
    ["Beispiel einer Viertelstunde*", "Verbrauch", "Strom aus der GEA", "Bezug vom Lieferanten"],
    [
        ["Wohnung A (Homeoffice, Wärmepumpe)", "1,0 kWh", "0,5 kWh", "0,5 kWh"],
        ["Wohnung B", "0,6 kWh", "0,3 kWh", "0,3 kWh"],
        ["Wohnung C (niemand zu Hause)", "0,4 kWh", "0,2 kWh", "0,2 kWh"],
        ["Summe, PV erzeugt 1,0 kWh", "2,0 kWh", "1,0 kWh", "1,0 kWh"],
    ],
    hl_cols=(2,),
)}
<p>Erzeugt die Anlage mehr, als alle zusammen verbrauchen, wird der Rest ins Netz eingespeist und an einen
frei wählbaren Abnehmer verkauft, etwa zum {a('/oemag-einspeisetarif/', 'OeMAG-Marktpreis')} (Oktober 2026:
14,874 Cent je kWh, September 10,168 Cent, Juli 6,146 Cent; der Wert schwankt monatlich). Die Anlage kann als
Überschusseinspeiser laufen (zuerst der eigene Verbrauch, etwa Allgemeinstrom, dann die Wohnungen) oder als
Volleinspeiser in die Gemeinschaft.</p>
{A.box("Jeder Zählpunkt darf an bis zu fünf Bürgerenergie-Modellen teilnehmen, etwa an der GEA im Haus und "
       "zusätzlich an einer Energiegemeinschaft. Wie viel Verbrauch jedem Modell zusteht, regelt der "
       "Teilnahmefaktor: in Summe höchstens 100 %, einmal täglich änderbar (ab 2028 voraussichtlich öfter).",
       label="Mehrfachteilnahme:")}
<p>Fehlt ein Smart Meter, baut ihn der Netzbetreiber kostenlos ein, auf Verlangen binnen zwei Monaten
(§ 49 ElWG). Die Viertelstundenwerte müssen freigegeben sein, mehr dazu im Ratgeber
{a('/smart-meter/', 'Smart Meter')}.</p>
"""),
        ("Netzentgelt und Abgaben: Was die GEA spart und was offen ist", "netzentgelt", f"""
<p><b>Der Strom, der über die gemeinsame Hauptleitung verteilt wird, nutzt das öffentliche Netz nicht.
Dafür fallen laut Koordinationsstelle keine Netzentgelte an, auch der Erneuerbaren-Förderbeitrag entfällt.
Die Elektrizitätsabgabe entfällt nach § 2 Abs. 1 Z 4 Elektrizitätsabgabegesetz.</b> Für den Reststrom aus
dem Netz zahlen alle Teilnehmer wie bisher Netzentgelt, Abgaben und Energiepreis.</p>
{A.table(
    ["", "GEA an derselben Hauptleitung", "Neu: GEA im Standortbereich"],
    [
        ["Verbindung", "eine Haupt- bzw. Steigleitung",
         "mehrere Steigleitungen an derselben Sammelschiene im Hausanschlusskasten bzw. Kabelverteilschrank"],
        ["Netzentgelt auf GEA-Strom", "keines, kein öffentliches Netz",
         "reduziert, Höhe legt die E-Control per Verordnung fest"],
        ["Elektrizitätsabgabe, Förderbeitrag", "entfallen", "offen, muss gesetzlich geregelt werden"],
        ["Umsetzbar", "ja, wie bisher", "voraussichtlich ab April 2027"],
    ],
    hl_cols=(1,),
)}
<p>Der Standortbereich (§ 70 Abs. 6 Z 2 ElWG) hilft vor allem großen Wohnhausanlagen: Statt drei getrennter
GEA für drei Stiegen kann künftig eine Anlage alle versorgen. Ob Ihr Haus diese Voraussetzung erfüllt,
bestätigt der Verteilnetzbetreiber. Wie sich die Netzentgelte in Erneuerbare-Energie-Gemeinschaften
entwickeln, steht im Ratgeber {a('/energiegemeinschaft-netzkosten/', 'Netzkosten der Energiegemeinschaft')}.</p>
{A.box("Die GEA spart Netzentgelt und Abgaben nur auf den Strom, der zeitgleich im Haus verbraucht wird. Ein "
       "Haus mit wenig Tagesverbrauch speist viel ein und verdient daran nur den Marktpreis. Mehr Verbrauch "
       "am Tag, etwa durch Wärmepumpe, Wallbox oder einen Speicher, erhöht den Anteil.",
       label="Ehrlich gerechnet:")}
"""),
        ("PV-Anlage im Wohnungseigentum: welcher Beschluss nötig ist", "wohnungseigentum", f"""
<p><b>Dient die PV-Anlage am gemeinsamen Dach allen Eigentümern, ist sie eine Maßnahme der
außerordentlichen Verwaltung nach § 29 WEG 2002. Darüber entscheidet die Mehrheit der
Wohnungseigentümer.</b> Steht die Teilnahme und Investition allen offen, kann laut Koordinationsstelle ein
Mehrheitsbeschluss reichen. Nutzen nur einzelne Eigentümer das Dach für sich, liegt eine Änderung vor, für die laut
Koordinationsstelle die Zustimmung aller Wohnungseigentümer nötig ist.</p>
{A.table(
    ["Regel im WEG 2002", "Was sie bedeutet"],
    [
        ["Mehrheit (§ 24 Abs. 4)", "Mehrheit aller Miteigentumsanteile, oder zwei Drittel der abgegebenen Stimmen, "
         "wenn diese zugleich mindestens ein Drittel aller Anteile ausmachen"],
        ["Anschlag (§ 24 Abs. 5)", "Beschluss wird im Haus sichtbar angeschlagen und jedem Eigentümer schriftlich übermittelt"],
        ["Anfechtung (§ 29 Abs. 1)", "Überstimmte können binnen 3 Monaten ab Anschlag die Aufhebung beantragen, "
         "6 Monate, wenn sie vorher nicht verständigt wurden"],
        ["Aufhebungsgründe (§ 29 Abs. 2 und 3)", "übermäßige Beeinträchtigung oder Kosten nicht aus der Rücklage gedeckt; "
         "Letzteres nicht, wenn die Mehrheit den Rest trägt oder die Verbesserung allen eindeutig nützt"],
        ["Privilegierte Änderung (§ 16 Abs. 5)", "gilt für die Solaranlage eines einzelnen Eigentümers nur bei "
         "Reihen- oder Einzelhäusern, Zustimmungsfiktion nach 2 Monaten"],
    ],
    hl_cols=(0,),
)}
<p>Die Finanzierung aus der Rücklage ist möglich, wenn die Anlage allen nutzt. Machen nicht alle mit,
empfiehlt die Koordinationsstelle einen eigenen Betreiberverein, der das Dach per Mehrheitsbeschluss pachtet.
Wer den Beschluss vorschlägt, muss laut § 24 Abs. 4 über die Mehrheitsregeln informieren. Ein Fachbeitrag auf forum-media.at verweist dazu auf die OGH-Entscheidungen 5 Ob 161/17p
(gemeinschaftliche Anlage) und 5 Ob 137/21i (eigennützige Anlage eines Einzelnen).</p>
{A.box("Diese Übersicht ersetzt keine Rechtsberatung. Bei strittigen Häusern, ungewöhnlichen Wohnungseigentumsverträgen "
       "oder Dachgeschoßausbauten klären Hausverwaltung oder Rechtsanwalt vor dem Beschluss, welcher Weg gilt.",
       label="Wichtig:")}
"""),
        ("In 8 Schritten zur gemeinschaftlichen Erzeugungsanlage", "ablauf", f"""
<p><b>Von der ersten Hausversammlung bis zum ersten geteilten Sonnenstrom kommen Beschluss, Verträge,
Montage und Netzbetreiber nacheinander dran.</b> Die Reihenfolge laut Koordinationsstelle:</p>
{A.steps([
    ("Teilnehmer klären: ", "Wer macht mit, wer investiert, wer nutzt nur den Strom? Mindestens zwei Parteien, "
     "abgestimmt mit Eigentümern und Hausverwaltung."),
    ("Betriebsmodell wählen: ", "Eigentümergemeinschaft, Hausverwaltung, Verein oder Dienstleister, dazu im "
     "Wohnungseigentum der Beschluss nach § 29 WEG."),
    ("Errichter auswählen: ", "Dach, Statik, Hauptleitung und Zählerplätze prüfen lassen, idealerweise von "
     "einem Betrieb mit Erfahrung im Mehrparteienhaus."),
    ("Errichtungs- und Betriebsvertrag: ", "zwischen Betreiber und Teilnehmern, mit Aufteilungsschlüssel, "
     "Strompreis, Wartung, Haftung und Ausstieg."),
    ("Netzbetreiber: ", "Registrierung als Marktpartner (GC-Nummer), Netzzugangsvertrag und Vereinbarung über "
     "den Betrieb der GEA."),
    ("Anlage errichten: ", "Smart Meter mit Zustimmung zur Datenübermittlung, Stromabnahmevertrag für den "
     "Überschuss."),
    ("EDA-Registrierung und Zusatzvereinbarung: ", "Datenaustausch über das EDA-Portal (bis 50 Zählpunkte "
     "kostenlos), jede Partei stimmt im Kundenportal des Netzbetreibers zu."),
    ("Betrieb und Abrechnung: ", "in Eigenregie oder über einen Dienstleister, auf Basis der täglichen "
     "Viertelstundenwerte."),
])}
<p>In der Übergangsphase seit Oktober 2026 lassen sich neue Zuordnungen laut Koordinationsstelle nur mit
Zählpunkten beim selben Netzbetreiber umsetzen. Für eine GEA im selben Haus ist das ohnehin der Fall.</p>
{A.cta("Passt Ihr Dach für eine Gemeinschaftsanlage?",
       "Wir prüfen Dach, Statik und Hauptleitung und liefern einen Projektbericht mit 3D-Belegplan und "
       "Statikreport, den Sie in die Eigentümerversammlung mitnehmen können.",
       secondary=("photovoltaik", "Photovoltaik von EBZ"))}
"""),
        ("Kosten und Förderung 2026", "kosten", f"""
<p><b>Technisch ist eine GEA eine normale PV-Anlage mit mehreren teilnehmenden Zählpunkten. Die
Errichtungskosten liegen im Mehrparteienhaus laut Koordinationsstelle meist höher als beim
Einfamilienhaus.</b> Der Netzbetreiber
verrechnet für die Einrichtung der GEA laut Koordinationsstelle keine zusätzlichen Kosten, außergewöhnliche
Kosten wie eine neue Leitung trägt der Anlagenbetreiber.</p>
{A.table(
    ["Kostenpunkt", "Richtwert*"],
    [
        ["PV-Wohnhaus-Dachanlage, Österreich 2024", "im Schnitt rund 1.551 € je kWp (IEA PVPS)"],
        ["Kleine Gewerbe-Dachanlage, Österreich 2024", "im Schnitt rund 1.000 € je kWp (IEA PVPS)"],
        ["EBZ-Richtpreis Einfamilienhaus, 10 kWp mit Speicher", "rund 15.000 bis 22.000 € vor Förderung"],
        ["Einrichtung beim Netzbetreiber", "keine zusätzlichen Kosten, EDA bis 50 Zählpunkte kostenlos"],
        ["Abrechnung", "Eigenregie oder Dienstleister, je nach Anbieter"],
    ],
    hl_cols=(1,),
)}
<p>Den Preis für Ihr Haus nennen wir nach der Besichtigung, weil Dachform, Leitungswege und Zählerplätze
stark variieren. Zur Förderung, Stand November 2026:</p>
<ul>
  <li><b>Bund (EAG-Investitionszuschuss):</b> Der dritte und letzte Fördercall 2026 lief vom 8. bis
  22. Oktober 2026. Derzeit gibt es keinen Bundeszuschuss für neue PV-Anlagen. Für 2027 ist laut BMWET eine
  Systemförderung für Speicher mit intelligenter Steuerung geplant, Höhe und Kriterien sind offen.</li>
  <li><b>Land:</b> Kärnten fördert Private mit 3.000 € Pauschale für PV ab 5 kWp mit neuem Speicher ab 5 kWh
  (2. Call bis 31. Dezember 2026). Ob das bei einer Gemeinschaftsanlage greift, hängt davon ab, wer
  Antragsteller ist; das klären wir vor dem Angebot. Die Steiermark hat derzeit keine PV-Landesförderung.
  Überblick: {a('foerderungen', 'Förderungen 2026')}.</li>
</ul>
<h3>Beispiel aus unserer Praxis: 25 kWp auf einem Mehrparteienhaus</h3>
<p>In Krumpendorf am Wörthersee haben wir auf einem Mehrparteienhaus eine
{a('/referenzen/projekt-mehrparteienhaus-krumpendorf/', '25-kWp-Anlage in Ost-West-Lage mit 25-kWh-Speicher')}
und Notstrom für die wichtigsten Verbraucher montiert, Montage und Inbetriebnahme dauerten vier Tage. Die
Ost-West-Ausrichtung verteilt die Erzeugung über den Tag, was zu einem Haus mit mehreren Haushalten passt.
Wie der Strom dort organisatorisch verteilt wird, ist nicht Teil der Projektdaten. Weitere Projekte finden
Sie unter {a('referenzen', 'Referenzen')}.</p>
"""),
        ("GEA, EEG oder BEG: der kurze Vergleich", "vergleich", f"""
<p><b>Die GEA bleibt im Gebäude, die Energiegemeinschaften reichen über das Haus hinaus.</b> Die wichtigsten
Unterschiede, Stand November 2026:</p>
{A.table(
    ["", "GEA", "Erneuerbare-Energie-Gemeinschaft (EEG)", "Bürgerenergiegemeinschaft (BEG)"],
    [
        ["Reichweite", "dieselbe Hauptleitung, künftig Standortbereich",
         "Lokalbereich (Trafo) oder Regionalbereich (Umspannwerk)", "auch über mehrere Netzbetreiber, österreichweit"],
        ["Rechtsform", "nicht nötig, Vertrag reicht", "ja, z. B. Verein oder Genossenschaft", "ja"],
        ["Netzentgelt auf geteilten Strom", "keines an der Hauptleitung",
         "Okt. bis Dez. 2026 reduziert (bisher minus 57 % lokal, minus 28 % regional)",
         "reduziert nur im Nahbereich, nach heutigem Stand ab 1.1.2027"],
        ["Abgaben", "Elektrizitätsabgabe und Förderbeitrag entfallen", "entfallen", "bleiben"],
    ],
    hl_cols=(1,),
)}
<p>Die Modelle lassen sich kombinieren: Die GEA versorgt das Haus, der Überschuss geht an eine EEG im Ort.
Den ausführlichen Vergleich aller Modelle lesen Sie unter
{a('/energiegemeinschaft-vergleich/', 'Energiegemeinschaft im Vergleich')}, dazu
{a('/buergerenergiegemeinschaft/', 'Bürgerenergiegemeinschaft')} und
{a('/peer-to-peer-strom/', 'Peer-to-Peer-Strom')}. Wer selbst eine Gemeinschaft im Ort aufbauen will, findet
die Schritte unter {a('/energiegemeinschaft-gruenden/', 'Energiegemeinschaft gründen')}.</p>
"""),
        ("Fazit: Lohnt sich die GEA im Mehrparteienhaus?", "fazit", f"""
<p>Die gemeinschaftliche Erzeugungsanlage ist der direkteste Weg, Sonnenstrom vom eigenen Dach in die
Wohnungen zu bringen: kein öffentliches Netz, kein Netzentgelt auf den geteilten Strom, kein Verein nötig.
Wirtschaftlich entscheidet, wie viel Strom das Haus tagsüber selbst verbraucht und wie fair Kosten und Nutzen
verteilt sind. Die Koordinationsstelle nennt als typische Hürden höhere Errichtungskosten im
Mehrparteienhaus, eher geringen Verbrauch und den Aufwand für Gründung und Betrieb. Wer früh einen klaren
Vertrag, einen sauberen Beschluss und eine passende Anlagengröße hat, räumt die meisten davon aus. Voraussichtlich
ab April 2027 macht der Standortbereich das Modell auch für große Wohnhausanlagen mit mehreren Stiegen
einfacher.</p>
<p><small>*Richtwerte und Beispiel ohne Gewähr: Das Viertelstunden-Beispiel ist vereinfacht, Systempreise
laut IEA PVPS (Österreich 2024, Durchschnittswerte), EBZ-Richtpreis für Einfamilienhäuser vor Förderung.
Rechtslage, Förderungen und OeMAG-Marktpreis Stand November 2026; die Werte ändern sich laufend.</small></p>
{A.cta("Photovoltaik fürs Mehrparteienhaus, ehrlich geplant",
       "Wir sehen uns Dach und Hauptleitung an, rechnen die Anlagengröße passend zum Verbrauch im Haus und "
       "liefern die Unterlagen für Eigentümerversammlung und Netzbetreiber.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("eg_privat", "Energiegemeinschaft mit EBZ"))}
"""),
    ],

    "partner": {
        "h2": "Photovoltaik fürs Mehrparteienhaus: EBZ Energie als Partner",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und montiert Photovoltaik, Speicher, Wärmepumpen und Wallboxen in "
                 "Kärnten und der Steiermark, mit zertifizierten Fachkräften und einem festen Ansprechpartner von "
                 "der Planung bis zur Übergabe. Für Eigentümergemeinschaften und Hausverwaltungen liefern wir die "
                 "technische Grundlage für den Beschluss. Wer zusätzlich Strom über das Haus hinaus teilen will, "
                 "den binden wir an eine Energiegemeinschaft an, abgerechnet über die Plattform unseres Partners "
                 "energyfamily."),
        "grid": [
            ("Projektbericht", "3D-Belegplan und Statikreport für die Eigentümerversammlung."),
            ("Hauptleitung im Blick", "Zählerplätze und Leitungswege vor dem Angebot geprüft."),
            ("Ehrliche Größe", "Anlage passend zum Tagesverbrauch im Haus, nicht zur Dachfläche."),
            ("Mehr als das Haus", "Anbindung an eine Energiegemeinschaft im Nahbereich."),
        ],
    },

    "faq": [
        ("Was ist eine gemeinschaftliche Erzeugungsanlage?",
         "Eine gemeinschaftliche Erzeugungsanlage (GEA) ist meist eine PV-Anlage auf einem Mehrparteienhaus, deren "
         "Strom mehrere Parteien an derselben Hauptleitung direkt nutzen. Der Strom fließt über die Hausleitung, "
         "nicht über das öffentliche Netz. Seit 2017 sind laut Koordinationsstelle über 3.500 GEA in Österreich "
         "aktiv."),
        ("Muss jede Wohnung bei der GEA mitmachen?",
         "Nein, die Teilnahme ist freiwillig. Jede Partei an der Hauptleitung kann mitmachen oder verzichten und "
         "behält ihren eigenen Stromlieferanten für den Reststrom. Es reichen zwei teilnehmende Parteien."),
        ("Fallen für GEA-Strom Netzentgelte an?",
         "Für den Strom, der über die gemeinsame Hauptleitung verteilt wird, fallen laut Koordinationsstelle keine "
         "Netzentgelte und kein Erneuerbaren-Förderbeitrag an, die Elektrizitätsabgabe entfällt. Für den neuen "
         "Standortbereich legt die E-Control reduzierte Netzentgelte per Verordnung fest, ob die Abgaben dort "
         "entfallen, ist noch offen."),
        ("Was ändert das ElWG für gemeinschaftliche Erzeugungsanlagen?",
         "Seit 1. Oktober 2026 ist die GEA im ElWG geregelt, bestehende Anlagen wurden ohne Neugründung "
         "übergeführt. Neu ist der Standortbereich: Mehrere Steigleitungen am selben Hausanschlusskasten können "
         "eine Anlage teilen, umsetzbar voraussichtlich ab April 2027. Außerdem darf jeder Zählpunkt an bis zu "
         "fünf Modellen teilnehmen."),
        ("Braucht eine GEA einen Verein?",
         "Nein, eine Rechtsform ist nicht zwingend, ein Errichtungs- und Betriebsvertrag zwischen Betreiber und "
         "Teilnehmern reicht. Machen nicht alle Eigentümer mit, empfiehlt die Koordinationsstelle einen eigenen "
         "Betreiberverein, der das Dach pachtet."),
        ("Wie viele Eigentümer müssen einer PV-Anlage am Dach zustimmen?",
         "Dient die Anlage allen, ist sie außerordentliche Verwaltung nach § 29 WEG 2002 und braucht die Mehrheit: "
         "mehr als die Hälfte aller Anteile oder zwei Drittel der abgegebenen Stimmen mit mindestens einem Drittel "
         "aller Anteile. Überstimmte können binnen 3 Monaten ab Anschlag anfechten. Nutzen nur Einzelne das Dach, "
         "braucht es die Zustimmung aller Wohnungseigentümer."),
        ("Können Mieter an einer GEA teilnehmen?",
         "Ja, Mieter können Strom aus der GEA beziehen und auch investieren. Betreiber ist dann meist der "
         "Gebäudeeigentümer, die Hausverwaltung oder ein Dienstleister. Der Vertrag sollte einen einfachen Ausstieg "
         "beim Auszug vorsehen."),
        ("Kann ich mit der GEA zusätzlich in einer Energiegemeinschaft sein?",
         "Ja, ein Zählpunkt darf an bis zu fünf Bürgerenergie-Modellen teilnehmen. Über den Teilnahmefaktor (in "
         "Summe höchstens 100 %, einmal täglich änderbar) legen Sie fest, welcher Anteil auf welches Modell "
         "entfällt. So kann der Überschuss der Hausanlage zum Beispiel an eine EEG im Ort gehen."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Mit zertifizierten Fachkräften plant und "
                    "montiert EBZ Energie Photovoltaikanlagen in Kärnten und der Steiermark, auch auf "
                    "Mehrparteienhäusern wie in Krumpendorf. Die Angaben zu ElWG und WEG 2002 sind eine "
                    "Orientierung, keine Rechtsberatung; maßgeblich sind Gesetzestext, Netzbetreiber und Ihre "
                    "Hausverwaltung."),
    "sources": [
        ("Koordinationsstelle für Energiegemeinschaften: Gemeinschaftliche Erzeugungsanlagen",
         "https://energiegemeinschaften.gv.at/gemeinschaftliche-erzeugungsanlagen/"),
        ("Koordinationsstelle: Was sind GEAs?", "https://energiegemeinschaften.gv.at/was-sind-geas/"),
        ("Koordinationsstelle: Betriebsmodelle und Gründungsschritte",
         "https://energiegemeinschaften.gv.at/betriebsmodelle-gruendungsschritte/"),
        ("Koordinationsstelle: Messung und Aufteilung", "https://energiegemeinschaften.gv.at/messung-und-aufteilung/"),
        ("Koordinationsstelle: Wirtschaftliche Überlegungen",
         "https://energiegemeinschaften.gv.at/wirtschaftliche-ueberlegungen/"),
        ("Koordinationsstelle: Mehrfachteilnahme", "https://energiegemeinschaften.gv.at/mehrfachteilnahme/"),
        ("Koordinationsstelle: FAQs zum ElWG", "https://energiegemeinschaften.gv.at/faqs-zum-elwg/"),
        ("Koordinationsstelle: FAQs (Abschnitt Gemeinschaftliche Erzeugungsanlagen)",
         "https://energiegemeinschaften.gv.at/faqs/"),
        ("WEG 2002, § 24 (Beschlussfassung)", "https://www.jusline.at/gesetz/weg/paragraf/24"),
        ("WEG 2002, § 29 (Außerordentliche Verwaltung)", "https://www.jusline.at/gesetz/weg/paragraf/29"),
        ("forum-media.at: Errichtung einer PV-Solaranlage am Dach im Wohnungseigentum (2023)",
         "https://www.forum-media.at/news/Bau-Immobilien/Errichtung-einer-PV-Solaranlage-am-Dach-im-Wohnungseigentum"),
        ("IEA PVPS: National Survey Report Austria 2024", "https://iea-pvps.org/national_survey/nsr-austria-2024/"),
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/de/marktpreis/"),
    ],
    "related": [
        ("eg", "Energiegemeinschaft: alle Modelle nach ElWG"),
        ("/energiegemeinschaft-vergleich/", "Energiegemeinschaft im Vergleich: GEA, EEG, BEG, P2P"),
        ("/energiegemeinschaft-privat/", "Energiegemeinschaft privat: mit Nachbarn und Familie"),
        ("eg_privat", "Energiegemeinschaft mit EBZ: PV und Anbindung"),
    ],
    "cta": {
        "h3": "Sonnenstrom für alle Wohnungen",
        "text": "Wir prüfen Dach, Hauptleitung und Verbrauch und sagen Ihnen, welche Anlage zu Ihrem Haus passt.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Photovoltaik fürs Mehrparteienhaus, ehrlich geplant",
    "final_text": ("Kostenlose Erstberatung für Eigentümergemeinschaften, Hausverwaltungen und Vermieter in Kärnten "
                   "und der Steiermark, mit Projektbericht, transparenten Zahlen und einem Ansprechpartner aus Villach."),
}
