# Standortseiten: Arbeitsanweisung (Stand 10.10.2026)

Gilt zusaetzlich zu `build/pages/README.md` (harte Regeln, Imports, Pruefung) und `build/seo/README.md`
(Briefing-Format, DataForSEO nur Oesterreich/Deutsch). ZUERST beide lesen, dann die Referenz
`build/pages/standort_villach.py` (Aufbau, Tonfall, Komponenten) und `build/components.py`.

## Ziel
Jede Standortseite ist fuer ZWEI Themen am Ort optimiert: Photovoltaik (Primaer) UND Waermepumpe (Sekundaer).
Eine Seite je Ort, keine getrennten PV-/Waermepumpen-Seiten (Suchvolumen je Ort zu klein, zwei duenne Seiten
wuerden sich gegenseitig schwaechen). Die Waermepumpe bekommt eine eigene H2-Sektion mit lokalem Bezug,
mindestens zwei FAQ und Links auf `waermepumpe` und die Waermepumpen-Ratgeber.

## Ablauf
1. Briefing nach `build/seo/README.md` erstellen (`build/seo/standort_<ort>.json` und `.md`): Seeds
   "photovoltaik <ort>", "pv anlage <ort>", "waermepumpe <ort>", "solaranlage <ort>", "photovoltaik firmen <ort>",
   dazu Bezirks-/Umlandbegriffe. SERP fuer PV und Waermepumpe getrennt abrufen (location passend zum Ort),
   People-also-ask mitnehmen. Budget max. 1,50 $ je Seite. Volumen NUR aus Oesterreich.
2. Lokale Fakten recherchieren (WebSearch/WebFetch) und im Modul-Docstring mit Quelle notieren.
3. Modul `build/pages/standort_<ort>.py` schreiben (Funktion `build()`, `__main__`-Block wie in
   `build/pages/foerderungen.py`), pruefen mit `python3 build/pages/standort_<ort>.py` (muss "[OK ]" melden).
   NICHT `build_all.py` starten (andere Agenten arbeiten parallel), NICHT committen.
4. Bericht: Primaer-/Sekundaer-Keywords mit Volumen, Title/H1/Description, lokale Fakten mit Quelle,
   offene Faktenfragen fuer den Kunden, Kosten der API-Aufrufe.

## Harte Regeln (zusaetzlich zu README.md)
- Firmensitz ist NUR Triglavstrasse 15, 9500 Villach. Nie einen Standort, ein Buero oder eine Niederlassung am
  Zielort behaupten. Formulierung: "Fachbetrieb aus Villach, vor Ort in <Ort>".
- NIE "eigenes Montageteam", "festangestellt", "eigene Monteure", "Subunternehmer". Nur: "zertifizierte
  Fachkraefte", "ein fester Ansprechpartner von der Planung bis zur Uebergabe". Kein "Leasing", keine
  "Ertragsprognose" (stattdessen "Projektbericht mit 3D-Belegplan und Statikreport"), kein Schauraum, kein Marstek.
- KEINE Foerderfristen, Call-Termine oder Datumsangaben zu Foerderungen auf Standortseiten (Skript
  `build/seo/check_fristen.py` prueft das). Foerderung nur als Kurzfassung mit Betraegen aus
  `build/seo/_fakten_2026-10.md`, fuer Fristen auf `foerderungen` (Hub) und `foerderrechner` verlinken.
  Bundesfoerderung fuer Waermepumpen ist ausgeschoepft: nie als verfuegbar darstellen.
- Keine erfundenen Zahlen. Jede lokale Angabe (Netzbetreiber, Genehmigung/Baurecht, Solarkataster,
  Gemeinde- oder Stadtfoerderung, Sonnenstunden, Ertrag je kWp) braucht eine amtliche oder offizielle Quelle,
  die du in dieser Sitzung selbst abgerufen hast. Ohne Quelle weglassen. Keine Entfernungs- oder
  Fahrzeitangaben. Richtwerte mit Sternchen und Fussnote.
- Referenzen nur mit den freigegebenen Zahlen aus `build/pages/referenz_projekte.py` und CLAUDE.md; Bild und
  Zahlen muessen zum selben Projekt gehoeren. Bilder nur ueber vorhandene IMG-Keys aus `build/common.py`.
- Keine Textbloecke aus `standort_villach.py` oder `standort_wolfsberg.py` woertlich uebernehmen: jede Seite
  braucht eigene, ortsbezogene Inhalte (sonst Doorway-Page). Kaernten-/Steiermark-weite Standardabsaetze kurz
  halten und auf die zustaendige Seite verlinken.
- Interne Links ueber Slug-Keys aus `common.S`: pv_villach, pv_wolfsberg, pv_klagenfurt, pv_graz, pv_steiermark,
  photovoltaik, waermepumpe, batteriespeicher, ems, foerderungen, foerderrechner, foerderung_kaernten,
  foerderung_steiermark, solarrechner, finanzierung, referenzen, kontakt, eg_privat. Ratgeber als Pfad "/slug/"
  nur, wenn `out/<slug>/index.html` existiert.
- Nur die eigene Datei und das eigene Briefing schreiben. Keine Aenderungen an common.py, theme.py,
  components.py, layout.py, home.py oder anderen Seiten.
