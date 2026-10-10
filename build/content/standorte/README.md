# Ortsseiten aus der gemeinsamen Vorlage: Arbeitsanweisung

Jede Datei `build/content/standorte/<datei>.py` enthaelt genau ein Dict `ORT`. Die Vorlage
`build/pages/standorte.py` rendert daraus die Seite (Aufbau, Bewertungen, Finanzierung, Ablauf, zentrale
Foerder-Kurzfassung je Bundesland, Referenzkarten aus `referenz_projekte.py`, Quellenblock, Schema).
DU lieferst nur, was den Ort ausmacht: Texte, lokale Fakten, Quellen. Lies zuerst
`build/pages/README_standort.md` (harte Regeln) und `build/pages/README.md`, dann `build/pages/standorte.py`
(Funktionen `check` und `render`: dort siehst du, wie jedes Feld verwendet und geprueft wird).

Die Seiten sind fuer Photovoltaik (Primaer) UND Waermepumpe (Sekundaer) am Ort optimiert.

## Ablauf
1. Daten (DataForSEO-MCP, nur Oesterreich/Deutsch, Budget hoechstens 0,60 $ je Ort): Suchvolumen fuer
   "photovoltaik <ort>", "pv anlage <ort>", "pv <ort>", "solaranlage <ort>", "photovoltaik firmen <ort>",
   "waermepumpe <ort>", "waermepumpe installateur <ort>", "heizungstausch <ort>" und 2 bis 3 Umland-Varianten
   (das Google-Ads-Volumen-Tool liefert hoechstens 10 Keywords je Aufruf). Dazu je eine SERP fuer
   "photovoltaik <ort>" und "waermepumpe <ort>" (location Oesterreich oder der Ort), People-also-ask mitnehmen.
   Ergebnis als `build/seo/standort_<datei>.json` und `.md` (Kurzform des Formats in build/seo/README.md:
   primary, secondary, long_tail, questions, serp.top10, recommendation, cost_usd).
2. Lokale Fakten recherchieren (WebSearch/WebFetch). Nur amtliche oder offizielle Quellen, die du in dieser
   Sitzung selbst abgerufen hast: Gemeinde/Stadt, Bezirkshauptmannschaft, Land, Netzbetreiber, Statistik
   Austria, GeoSphere Austria, Klima- und Energie-Modellregionen (klimaundenergiemodellregionen.at),
   e5-Programm, Energieberatung des Landes. Ohne Quelle: weglassen.
3. Datei schreiben, pruefen mit `python3 build/pages/standorte.py <datei>` (muss "[OK ]" ohne Fehlerzeilen
   melden). NICHT build_all.py starten, keine anderen Dateien aendern, nicht committen.
4. Bericht: Title/H1/Description, Keywords mit Volumen, lokale Fakten mit Quelle, Weggelassenes,
   Faktenfragen fuer den Kunden, API-Kosten.

## Schema (alle Felder Pflicht, ausser wo "optional" steht)
```python
from common import a   # fuer interne Links in Texten: a("waermepumpe", "Wärmepumpe"), a("/slug/", "Text")

ORT = {
    "key": "pv_spittal",                 # Slug-Key aus common.S (vorgegeben)
    "name": "Spittal an der Drau",       # voller Name
    "kurz": "Spittal",                   # Kurzform fuer Ueberschriften
    "ort_in": "im Murtal",               # optional: Ortsangabe mit Praeposition, Standard "in <kurz>"
    "ort_nach": "ins Murtal",            # optional: Richtungsangabe, Standard "nach <kurz>"
    "area_name": "Bezirk Spittal an der Drau",   # optional, fuer das Service-Schema (areaServed)
    "land": "ktn",                       # "ktn" oder "stmk"
    "title": "...",                      # hoechstens 60 Zeichen, mit Ort, Photovoltaik und moeglichst Waermepumpe
    "description": "...",                # 140 bis 160 Zeichen, mit Ort und einer konkreten Angabe
    "eyebrow": "...",                    # optional
    "h1": "...",                         # genau ein H1: Photovoltaik + Ort, Waermepumpe wenn es natuerlich passt
    "lead": "...",                       # 2 bis 3 Saetze, ehrlich: Fachbetrieb aus Villach, vor Ort in <Ort>
    "badges": [("...", "..."), ("...", "..."), ("...", "...")],   # 3 Hero-Badges (fett, klein)
    "hero_img": "gen_eigenheim",         # IMG-Key aus common.IMG oder Pfad /assets/img/<datei> aus build/static/img
    "hero_alt": "...",                   # ehrlicher Alt-Text (was wirklich zu sehen ist, KEIN Ortsbild behaupten)
    "kpis": [("...", "..."), ...],       # optional, 4 Stueck; nur freigegebene oder belegte Zahlen. Sonst weglassen.
    "intro": {"h2": "...", "paragraphs": ["...", "..."]},        # warum PV/Waermepumpe HIER: Lage, Klima, Gebaeudebestand
    "lokal": {"h2": "...", "intro": "...",
              "rows": [("Bezirk", "..."), ("Netzbetreiber", "..."), ...]},   # mind. 5 Zeilen lokaler Fakten (HTML erlaubt)
    "netz": {"h2": "...", "betreiber": "der Kärnten Netz GmbH",  # betreiber im Dativ, fuer "melden die Anlage bei ... an"
             "paragraphs": ["...", "..."], "bullets": ["...", "...", "..."],
             "img": "gen_detail", "alt": "..."},                 # Genehmigung (Landesbaurecht) + Netzanschluss am Ort
    "waermepumpe": {"h2": "...", "paragraphs": ["...", "..."], "bullets": ["...", "..."],
                    "img": "waermepumpe", "alt": "..."},         # Heizungstausch am Ort: Bestand, Fernwaerme/Gas, Kombination mit PV
    "foerderung_h2": "...",              # optional
    "foerderung_lokal": ["..."],         # 1 bis 2 Absaetze NUR zu Gemeinde-/Stadtfoerderung oder regionalen Programmen
                                         # (belegt). Gibt es keine: ein ehrlicher Satz, dass die Gemeinde derzeit kein
                                         # eigenes Programm ausweist und wir das vor dem Angebot pruefen. Landes- und
                                         # Bundesfoerderung NICHT wiederholen (kommt aus der Vorlage). Keine Fristen.
    "referenzen": {"h2": "...", "intro": "...",
                   "slugs": ["projekt-pv-am-ossiachersee"]},     # 1 bis 3 Slugs aus referenz_projekte.py, naechstgelegene
                                                                 # zuerst. Zahlen kommen automatisch. Nie behaupten, das
                                                                 # Projekt liege im Ort, wenn es das nicht tut.
    "umgebung": ["...", "..."],          # 6 bis 12 Gemeinden im Bezirk/Umland (amtliche Namen), nur Nennung
    "links": [("/slug/", "Text")],       # optional, 2 bis 4 passende Ratgeber (nur wenn out/<slug>/index.html existiert)
    "faq": [("Frage?", "Antwort ..."), ...],   # 6 bis 8, jede mit Ortsbezug, mind. 2 zur Waermepumpe, Antworten als
                                               # reiner Text ohne HTML (gehen ins FAQ-Schema), 40 bis 90 Woerter
    "quellen": [("Bezeichnung der Quelle", "https://..."), ...],   # mind. 4 offizielle Quellen, die du abgerufen hast
    "notizen": "...",                    # optional, wird nicht gerendert: Faktenfragen, Unsicherheiten
}
```

## Inhaltliche Leitlinien
- Mindestens 650 Woerter eigener, ortsbezogener Text (die Vorlage prueft das). Nicht mit Fuelltext strecken:
  lieber mehr belegte lokale Fakten.
- Lokale Signale, die fast immer belegbar sind: Bezirk und Gemeinden, zustaendiger Stromnetzbetreiber (in der
  Steiermark und in Kaernten gibt es neben dem Landesnetz staedtische und private Netze: genau pruefen, das ist
  ein echtes Unterscheidungsmerkmal), zustaendige Baubehoerde, Solardach-/Solarpotenzialkataster des Landes
  (Kaernten: KAGIS; Steiermark: GIS Steiermark), Klima- und Energie-Modellregion oder e5-Gemeinde,
  Gemeindefoerderung fuer PV, Speicher oder Heizungstausch, Fernwaerme- oder Gasnetz am Ort (wichtig fuer die
  Waermepumpen-Entscheidung), Hoehenlage und Klimadaten nur mit Quelle.
- Freigegebene Zahlen, die du ohne weitere Quelle nennen darfst: Richtpreis 10 kWp mit Speicher rund 15.000 bis
  22.000 Euro vor Foerderung; bis zu 85 % weniger Stromkosten; Amortisation typisch 4 bis 6 Jahre; bis zu
  30 Jahre Leistungsgarantie, mindestens 10 Jahre Produktgarantie; 300+ Projekte in 6 Bundeslaendern; 4,9 Sterne
  auf Google; Finanzierung ab 147 Euro im Monat (mit Sternchen); Jahresertrag in Kaernten rund 1.000 bis
  1.100 kWh je kWp (Richtwert). Fuer die Steiermark den Ertrag nur mit eigener Quelle nennen.
- Keine Mario-Zitate und keine Ich-Texte schreiben (der Beratungsblock kommt aus der Vorlage).
- Keine Aussagen, EBZ habe im Ort schon Anlagen gebaut, ausser eine Referenz aus referenz_projekte.py liegt dort.
- Faelle wie Ortsbildschutz, Altstadt, Denkmalschutz oder Seeuferzonen nur erwaehnen, wenn belegt.
- Die Seite muss sich von den anderen Ortsseiten unterscheiden: keine austauschbaren Saetze, in denen nur der
  Ortsname wechselt.
