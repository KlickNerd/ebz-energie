# Leistungsseiten: Arbeitsanweisung

Jede Leistungsseite ist ein Modul `build/pages/<name>.py` mit einer Funktion `build()`, die
`write_page("<pfad>/index.html", html)` aufruft und dessen Rueckgabe (Fehlerliste) zurueckgibt.
`build_all.py` findet die Module automatisch. Vorlage und Referenz: `build/photovoltaik.py`
(komplette Leistungsseite) und `build/finanzierung.py` (kompakter). ZUERST beide lesen, dann
`build/components.py` (alle Sektionen mit Signaturen) und `build/common.py` (NAP, CLAIMS, S, IMG,
FINANZIERUNG, Helfer).

Imports im Modul (Pfad ist durch build_all gesetzt):
    from common import IMG, NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, S, faq_jsonld, u, a, href, tel_link, write_page, load_reviews
    from layout import page
    import components as C

## Harte Regeln (Validator bricht sonst ab)
- KEINE Gedankenstriche (– — ‐ ‒ − ―). Ersatz: Doppelpunkt, Komma, Klammer, neuer Satz.
- NIE: "Subunternehmer", "Leasing", "Ertragsprognose", "Widmanngasse", "Ackerweg", "90 %", Bewertung "5,0".
- Google 4,9; Ersparnis "bis zu 85 %"; 300+ Projekte; 6 Bundeslaender; Amortisation typisch 4 bis 6 Jahre;
  bis zu 30 Jahre Leistungsgarantie, mind. 10 Jahre Produktgarantie; Richtpreis 10 kWp mit Speicher
  rund 15.000 bis 22.000 EUR vor Foerderung; "Projektbericht mit 3D-Belegplan und Statikreport".
- Finanzierung: Eigentum ab Tag 1, 0 EUR Anzahlung, fixe Rate, digitale Bonitaetspruefung in Minuten,
  kein Grundbucheintrag (siehe common.FINANZIERUNG). NIE "keine strengen Bonitaetspruefungen" oder
  "kein Datenbankeintrag". Kein Mietmodell bei EBZ.
- Energiegemeinschaft: oesterreichweit moeglich; Netzentgelt-Rabatt bis 57 % lokal / 28 % regional
  (NE 4/5 bis 64 %) NUR im Nahbereich; oesterreichweit = Buergerenergiegemeinschaft ohne Rabatt.
  Partner energyfamily nur als Text-Badge (kein Logo). Rechner-Beispielwerte 10 ct / 14 ct / 4 EUR/Monat
  immer mit Sternchen.
- Adresse nur Triglavstrasse 15, 9500 Villach. Keine Emojis, keine Icon-Fonts; Unicode ☀ ▮ ♨ ⌖ ◎ ✓ € ⌂ ☎ ✉ ◷ ◇ ◔.
- Sie-Form, Deutsch (Oesterreich), direkt, warm ("die freundlichen Energie-Handwerker aus Villach"),
  keine Marketing-Floskeln, keine Superlative ohne Zahl, keine erfundenen Zahlen (Beispielwerte mit * + Fussnote).
- EBZ = ganzes Energiesystem (PV, Speicher, Waermepumpe, EMS, Energiegemeinschaft, Balkonkraftwerk/Wallbox),
  Eigenheim UND Gewerbe. Montage Kaernten + Steiermark, Referenzen in 6 Bundeslaendern.

## Roter Faden jeder Leistungsseite (wie photovoltaik.py)
hero (Bild + 3 Badges + Google-Float) -> kpis (4) -> kurze Definition/Erklaerung -> fuer wen (audience_split
oder cards) -> Nutzen/Zahlen (problem_compare, media_text, price_cards) -> Foerderung + Finanzierung (Link
foerderung_at / finanzierung) -> warum EBZ (why_section) -> Referenz(en) mit echten Zahlen (reference_cards,
nur freigegebene: EFH Villach 10 kWp ~80 % weniger Stromkosten; MFH Krumpendorf 25 kWp + 25 kWh Notstrom
4 Tage Bauzeit; Gewerbe OOe 40 kWp 13.500 EUR/Jahr; Hotel Warmbad 13 kWp bifazial 27 kWh 4.200 EUR/Jahr)
-> reviews_slider -> steps_section (Ablauf) -> faq_section (6 bis 8, mit faq_jsonld) -> linkgrid_section
(Cluster: Ratgeber + Leistungsseiten) -> contact_section -> finalcta -> Fussnote. Mario-Block
(founder_story) nur, wenn er inhaltlich passt (persoenliche Beratung), Text in seiner Stimme ohne erfundene
Fakten. Seitenlaenge: 1.200 bis 2.000 Woerter sichtbarer Text, keine Whitespace-Wuesten.

## SEO
title <= 60 Zeichen mit "| EBZ Energie" oder "| EBZ", description 140 bis 160 Zeichen mit Zahl,
genau ein H1, H2-Hierarchie, Bilder nur IMG-Keys aus common.py mit beschreibendem Alt-Text (keine neuen
Downloads), interne Links ueber Keys (S) oder Pfade "/slug/", Ratgeber des Clusters verlinken.
page(..., faq_jsonld_str=faq_jsonld(u(PATH), FAQ), og_image=IMG[...]).

## Pruefen
Vom Repo-Root: `python3 build/build_all.py` muss fuer deine Seite "[OK ] <pfad>/index.html" melden.
Andere Dateien nicht aendern, nicht committen.
