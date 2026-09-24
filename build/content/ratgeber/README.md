# Ratgeber-Migration: Arbeitsanweisung

Jeder Ratgeber ist eine Python-Datei `build/content/ratgeber/<slug_mit_unterstrichen>.py`
mit einem Dict `ARTICLE`. Vorlage und Referenz: `ems_foerderung.py` (zuerst komplett lesen).
Bausteine kommen aus `build/article.py` (`A.tldr`, `A.kpis`, `A.box`, `A.box_dark`, `A.table`,
`A.steps`, `A.net`, `A.cta`, `A.figure`); Links über `a(key_oder_pfad, text)` aus `common`.

Quelle je Artikel: `<scratchpad>/wp/<slug>.txt` (bereinigter Text des Live-Artikels mit
Überschriften, Listen, Tabellen, FAQ, Links, Bildern). Bei Bedarf `<slug>.html` daneben.

## Harte Regeln (werden validiert, Build bricht sonst ab)
- KEINE Gedankenstriche (– — ‐ ‒ − ―). Ersatz: Doppelpunkt, Komma, Klammer, neuer Satz. Bindestrich - ist ok.
- NIE: "Subunternehmer" (auch nicht "ohne Subunternehmer"), "Leasing", "Ertragsprognose", "Widmanngasse", "Ackerweg", "90 %", "5,0".
- Google-Bewertung immer "4,9". Ersparnis "bis zu 85 %". Statt Leasing/Mieten-Angebot von EBZ: "Finanzierung" (Anlage gehört ab Tag 1 dem Kunden, ab 147 €/Monat inkl. Speicher).
- Planungsunterlagen heißen "Projektbericht mit 3D-Belegplan und Statikreport".
- Adresse nur: Triglavstraße 15, 9500 Villach. Tel. +43 650 220 26 26. office@ebz-energie.com.
- Keine Emojis, keine Icon-Fonts. Unicode-Zeichen erlaubt: ☀ ▮ ♨ ⌖ ◎ ✓ € ⌂ ☎ ✉ ◷.
- Sie-Form, Deutsch (Österreich: Jänner, Euro), direkt, keine Marketing-Floskeln, keine Superlative ohne Zahl.

## Fakten
- Alle Zahlen, Fristen, Beträge aus der Quelle übernehmen. NICHTS erfinden. Keine Zahl "aktualisieren", die nicht belegt ist.
- Richtwerte/Beispiele mit Sternchen kennzeichnen und Fußnote (`<p><small>*Richtwerte …</small></p>`).
- Zeitbezug: Wo die Quelle ein Jahr nennt, bleibt es ("Stand: <Monat Jahr>" aus dem Änderungsdatum der Quelle).
- Offensichtliche Fehler der Quelle (doppelte Absätze, widersprüchliche Zahlen, Copy-Paste-Reste) bereinigen und im Bericht nennen.
- Quellen-URLs nur aus der Quelle ("Links im Original") übernehmen, nie ausdenken.
- EBZ-Fakten: 300+ Projekte, 6 Bundesländer, Amortisation typisch 4 bis 6 Jahre, bis zu 30 Jahre Leistungsgarantie, mind. 10 Jahre Produktgarantie, Richtpreis 10 kWp mit Speicher rund 15.000 bis 22.000 € vor Förderung, festangestelltes Team aus zertifizierten Fachkräften, Montage Kärnten + Steiermark, Geschäftsführer Mario Zintl.

## Struktur je Artikel (Optimierung gegenüber der Quelle)
- `title` ≤ 60 Zeichen mit " | EBZ Energie" oder " | EBZ", `description` 140 bis 160 Zeichen, konkret mit Zahl.
- `h1` mit Nutzen + Zahl, `lead` 2 Sätze, `chips` 3 bis 4 harte Fakten.
- `tldr` 3 bis 5 Punkte mit Zahlen. `kpis` 4 Kennzahlen.
- 6 bis 9 H2-Sektionen mit sprechenden `id`s. Vergleiche als `A.table`, Abläufe als `A.steps`, Warnungen als `A.box`/`A.box_dark`.
- Ein `A.cta` in der Mitte und einer vor dem Fazit (auf `kontakt` + passende Leistungsseite).
- `partner`: auf das Thema zugeschnitten (Wärmepumpe, Förderabwicklung, Speicher …).
- `faq`: 6 bis 8 Fragen (Quelle + typische Suchfragen), Antworten 2 bis 4 Sätze mit Zahl.
- `author_note`: 2 bis 3 Sätze zu Mario Zintl / EBZ im Themenkontext + Hinweis "keine Rechts-/Steuerberatung" bei Förder-/Steuerthemen.
- `related`: 4 Links, Mix aus Ratgebern des Clusters (Pfad "/slug/") und Leistungsseiten (Keys: photovoltaik, batteriespeicher, waermepumpe, balkonkraftwerke, finanzierung, eg, ems, referenzen, kontakt, foerderung_kaernten, foerderung_steiermark, foerderung_at, marktpreis).
- `hero_img`: nur vorhandene IMG-Keys aus `common.py` (waermepumpe, foerderung, pv_card, speicher, gen_hero, gen_eigenheim, gen_gewerbe, gen_detail, team_quer, eg_drohne, gewerbe_dach, balkon, ems). Keine neuen Bilder laden.
- `date_published` aus der Quelle, `date_modified` = "2026-09-24".
- Interne Links im Text: `{a('waermepumpe', 'Wärmepumpen-Installateur')}` (Key) oder `{a('/kosten-einer-waermepumpe/', 'Kosten einer Wärmepumpe')}` (Pfad).

## Prüfen
Vom Repo-Root: `python3 build/ratgeber.py` muss für jede Datei `[OK ]` melden. Fehler beheben.
Andere Dateien nicht ändern, nicht committen.
