# CLAUDE.md · Übergabe: EBZ Energie Website-Rebuild

Dieses Dokument ist die vollständige Übergabe für den Neubau der Website
**ebz-photovoltaik.at** im bestehenden EBZ-LP-Design. Es enthält alles, was ohne
Rückfragen gebraucht wird: Fakten, Design-System, Konventionen, Deployment,
Integrationen und Verbote. Bei Widerspruch zwischen diesem Dokument und
Live-Website gilt: **dieses Dokument** (die Live-Site enthält veraltete Inhalte).

---

## 1. Projekt & Rollen

- **Kunde:** EBZ Energie GmbH, Photovoltaik-Fachbetrieb
- **Agentur:** KlickNerds (Dominik), beauftragt mit SEO, Content, Web
- **Domain:** https://ebz-photovoltaik.at (WordPress + Elementor, wird sukzessive durch Custom-HTML-Blöcke ersetzt)
- **Ziel:** Komplette Website im Design der bereits gebauten Leistungsseiten (Energiegemeinschaft Privat/Gewerbe, EMS) und der neuen Startseite. SEO + GEO (LLM-Zitierbarkeit) sind Leitplanken jeder Seite.

## 2. Verbindliche Fakten (vom Kunden freigegeben, NICHT ändern)

| Fakt | Wert |
|---|---|
| Firmierung | EBZ Energie GmbH |
| Adresse (einzige gültige!) | **Triglavstraße 15, 9500 Villach** |
| Telefon | +43 650 220 26 26 (`tel:+436502202626`) |
| E-Mail | office@ebz-energie.com |
| Öffnungszeiten | Mo bis Fr: 10:00 bis 20:00 Uhr |
| Google-Bewertung | **4,9** Sterne (nie 5,0 schreiben) |
| Energiekosten-Claim | **bis zu 85 %** Ersparnis (nie 90 %) |
| Referenzen | 300+ dokumentierte Projekte, 6 Bundesländer, typ. Amortisation 4 bis 6 Jahre |
| Garantie | bis zu 30 Jahre Leistungsgarantie, mind. 10 Jahre Produktgarantie |
| Geschäftsführer / Autor | Mario Zintl ("Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH") |
| Planungsunterlagen | **"Projektbericht mit 3D-Belegplan und Statikreport"** (das Wort "Ertragsprognose" nicht verwenden, EBZ berechnet keine) |
| Finanzierung | **Finanzierung, KEIN Leasing.** Anlage gehört ab Tag 1 dem Kunden, volle Förderung privat, keine strengen Bonitätsprüfungen, kein Datenbankeintrag. Ab 147 €/Monat inkl. Speicher. Formulierungen wie "am Ende der Laufzeit gehört sie Ihnen" sind FALSCH. |
| Energiegemeinschaft | Wird **österreichweit** angeboten (Strom teilen mit Nachbarn ODER z. B. der Tante in Wien). Netzentgelt-Rabatt (bis 57 % lokal / 28 % regional, NE 4/5 bis 64 %) gilt nur im Nahbereich; österreichweit = Bürgerenergiegemeinschaft ohne Rabatt. Beides korrekt darstellen, den Rabatt nie fürs österreichweite Teilen versprechen. |
| Partner EG-Abrechnung | energyfamily (Plattform, ~330 Gemeinschaften, ~15.000 Nutzer). Logo-Freigabe steht aus → Text-Badge verwenden. |
| Einzugsgebiet Montage | Kärnten + Steiermark (Fokus), Referenzen österreichweit |

### Sprach-Verbote (hart)
- **KEINE Gedankenstriche** (– oder —). Ersatz: Doppelpunkt, Komma, Klammer, neuer Satz. Jede Datei wird darauf validiert.
- **NIE "Subunternehmer"** erwähnen, auch nicht positiv ("keine Subunternehmer"). Stattdessen: "zertifizierte Fachkräfte", "meisterhaftes Handwerk". (EBZ arbeitet mit Subs, will das nicht thematisieren.)
- Sie-Form, deutsch, direkt, ohne Marketing-Floskeln. Zahlen konkret statt Superlative.
- Keine erfundenen Zahlen. Beispielwerte immer mit Sternchen + Fußnote kennzeichnen ("*Beispielkonditionen…", "*Richtwerte…").

## 3. Design-System (Source of Truth: `build/pages.py` → Konstante `CSS`)

Alle Seiten sind **self-contained Custom-HTML-Blöcke**: ein `<div class="ebz-eg">…</div>`,
darunter `<style>` (komplettes CSS inline) und `<script>` (Vanilla JS). Kein externes
Stylesheet, keine Build-Abhängigkeit im WordPress.

### Tokens
```css
--petrol:#0e4d64; --petrol-2:#0a3a4d; --petrol-3:#082e3d;
--amber:#f5a623;  --amber-2:#e0951a;
--ink:#152730; --muted:#5c6f77; --line:#e4ebed;
--bg:#f5f8f9; --card:#fff; --radius:18px;
--shadow:0 18px 40px -22px rgba(14,77,100,.35); --wrap:1180px;
```
- **Fonts:** Sora (Headlines, 700/800) + Source Sans 3 (Copy), via Google Fonts `<link>` mit preconnect.
- **Full-bleed:** `.ebz-eg{margin-inline:calc(50% - 50vw)}`, Inhalt in `.eg-wrap` (max 1180px).
- **Scoping:** ALLE Selektoren beginnen mit `.ebz-eg` bzw. Prefix `eg-`. Theme-Override-Schutz für Headings am CSS-Ende (Farben explizit setzen, Elementor/Theme funkt sonst rein).

### Komponentenbibliothek (fertig in pages.py/home.py, wiederverwenden!)
- `eg-hero` (dunkler Gradient + Grid-Pattern, Copy links, Bild rechts mit `eg-hero__badge`)
- `kpis([...])` → weißer KPI-Strip, 4 Kennzahlen
- `eg-what` (dunkle Sektion) + `eg-hub` (animiertes SVG-Hub-Diagramm, Kreis r=64, Schrift 18/16px)
- `eg-problem` + `eg-compare` (animierte Vergleichsbalken, `--w`-Variable, IntersectionObserver)
- `eg-cards` / `eg-card` (Hover: Amber-Top-Bar via ::before; Variante `eg-card--media` mit Bild 190px)
- `eg-split` / `eg-panel` + `eg-panel--dark` (Zielgruppen-Panels mit `eg-checklist`)
- `eg-steps` / `eg-steplist` (nummerierte Schritte mit `eg-step__t` Zeitangabe)
- `eg-why` (3x2 Icon-Grid)
- `reviews_block()` (Google 4,9, drei Zitate)
- `eg-founder` (Mario-Zitat, Foto: `…/2023/12/Zintl_cut.png`)
- `contact_block(headline, sub, form_id, form_note)` (dunkle Sektion, weiße Formular-Karte, WPForms-Styling komplett enthalten)
- `eg-faq` / `eg-acc` (Akkordeons, `<details>`)
- `eg-linkgrid` (interne Link-Kacheln), `eg-mosaic` (Bildband mit Captions), `eg-leasing` (dunkles Band, jetzt = Finanzierung), `eg-finalcta` (Amber), `sticky()` (Mobile-Bottom-CTA)
- A11y: `:focus-visible` Amber-Outline, `prefers-reduced-motion` deaktiviert Animationen.
- **Keine Akzent-Streifen** (border-left/top in Amber) an Boxen: wurde explizit entfernt, "wirkt zu KI".
- Icons: Unicode-Zeichen (☀ ▮ ♨ ⬡ ⌂ ◫ ✓ ◇ € ⌖ ◔), keine Icon-Fonts, keine Emojis.

### JS-Muster
Ein IIFE pro Seite: IntersectionObserver für `.eg-reveal` → `.eg-inview` (Reveal + Balken/Hub-Animation), Smooth-Scroll für `#`-Anker. Kein jQuery, keine Dependencies.

## 4. SEO/GEO-Regeln (jede Seite)

1. **Genau ein H1**, saubere H2/H3-Hierarchie (Elementor-Altlast: Schritt-Nummern waren H1s, nie wiederholen).
2. Meta-Title + Description als Kommentar am Dateianfang (`<!-- META: … -->`), Einpflege in Rank Math/Yoast.
3. **JSON-LD: NUR FAQPage** mit `"@id": url + "#ebz-faq"`. KEIN Organization/LocalBusiness/Article/@graph-Schema in den Blöcken (kollidiert mit SEO-Plugin, war ein GSC-Problem). LocalBusiness kommt zentral vom Plugin.
4. GEO: konkrete zitierbare Zahlen (Preisspannen, kWp, €/Jahr, Fristen), Definitionsabsätze, konsistente NAP (nur Triglavstraße 15!), FAQ pro Seite, Autorenbox Mario bei Ratgebern.
5. Richtpreis-Anker (freigegeben): 10 kWp mit Speicher rund 15.000 bis 22.000 € vor Förderung.
6. Interne Verlinkung: jede Seite verlinkt in ihr Cluster (Ratgeber ↔ Leistungsseite ↔ Rechner) und auf /referenzen/.
7. Bilder: nur Mediathek-URLs (nie Base64 in Produktionsdateien), beschreibende deutsche Alt-Texte, `loading="lazy"` außer Hero, width/height-Attribute.
8. OeMAG-Zahlen aktuell halten: Marktpreis Juli 2026 = 6,146 ct (Untergrenze), Q3-Marktpreis 10,923 ct. Monatlich prüfen (Artikel 18).

## 5. Build-Pipeline (liegt in `build/`)

Python 3, keine externen Dependencies (nur Playwright optional für Screenshots).

| Datei | Zweck |
|---|---|
| `common.py` | BASE-URL, Slug-Dict `S` + Helper `u()`/`a()`, TEL, `cta_block`, `faq_jsonld` |
| `shared_css.css` | Artikel-CSS (Scope `.ebz-artikel`) |
| `figs.py` | SVG-Infografiken (Netzebenen, Stromfluss, Preisvergleich), Schriften min. 12px, mobil lesbar |
| `content_a/b/c.py` | Artikel-Inhalte als Dicts |
| `build.py` | rendert die 10 EG-Artikel + Validierung + Mario-Autorenbox |
| `pages.py` | **Design-System (CSS/JS/Komponenten)** + EG-Leistungsseiten Privat & Gewerbe |
| `rechner.py` | EG-Rechner (Scope `.ebz-rechner`), standalone + einbettbar |
| `home.py` | Startseite |

Konventionen: `python3 <datei>.py` baut nach `out/…`. Jede Datei validiert:
JSON-LD parsebar, Tag-Balance, **0 Gedankenstriche**. VORSCHAU-Dateien = Produktion
+ `<meta charset>` + viewport (nur zum lokalen Ansehen, nie deployen).
Neue Seiten: Komponenten aus `pages.py` importieren, gleiche Struktur wie `home.py`.

## 6. Seiteninventar & Slugs

### Bereits im neuen Design gebaut (fertig, liegen in den Ordnern)
- `/` Startseite (`startseite/startseite.html`)
- `/leistungen/energiegemeinschaft/` (Privat-LP, mit eingebettetem Rechner)
- `/leistungen/energiegemeinschaft-gewerbe/` (Gewerbe/Gemeinden-LP)
- `/energiegemeinschaft-rechner/` (Standalone-Rechner, optional)
- 10 EG-Ratgeber (Dateien 11 bis 20): energiegemeinschaft-kaernten, -steiermark, -villach, -beitreten, -erfahrungen, -finden, -netzkosten, oemag-einspeisetarif-energiegemeinschaft, -privat, -kosten
- EMS-LP existiert bereits live unter `/ems-lp-2/` (gleiches Design, separater Build)

### Bestehende Seiten (Elementor, sukzessive neu bauen)
`/photovoltaik/`, `/batteriespeicher/`, `/waermepumpen-installateur/`, `/balkonkraftwerke/`,
`/pv-anlage-leasen/` (→ **inhaltlich auf Finanzierung umstellen!**), `/referenzen/` (+ Projekt-Unterseiten),
`/photovoltaik-villach/`, `/photovoltaik-wolfsberg/`, `/foerderung-photovoltaik-kaernten/`,
`/foerderung-photovoltaik-steiermark/`, `/photovoltaik-foerderung-oesterreich/`, `/energiegemeinschaft/` (Pillar-Artikel),
`/energiemanagementsystem/`, `/marktpreis-2026/`, `/smart-meter-opt-out/`, `/kontakt/`, `/aktuelles/`, `/ebz-solarrechner/`.
Slug-Änderungen vermeiden; falls nötig: 301 + `S` in `common.py` anpassen und alles neu bauen.

## 7. WordPress-Deployment (immer gleich)

1. Seite bearbeiten → Elementor-Inhalt komplett durch **einen Custom-HTML-Block** (Gutenberg) oder WPCode-Snippet ersetzen. Ganzen Dateiinhalt einfügen.
2. Meta-Title/Description aus dem Dateikopf-Kommentar in Rank Math/Yoast eintragen.
3. **WP Fastest Cache → "Delete Cache and Minified CSS/JS"** (Pflicht nach jedem Update).
4. FAQPage im Rich Results Test prüfen.
5. Shortcodes ([wpforms …]) laufen in Custom-HTML nur, weil ein WPCode-PHP-Snippet `do_shortcode` auf den Content anwendet. Snippet ist seitenweit aktiv, nicht löschen.

## 8. Integrationen

- **WPForms ID 6891** (Lite!): aktuell auf beiden EG-LPs UND der Startseite. Lite speichert NICHTS in der DB, Mail-Zustellung via WP Mail SMTP muss stehen (offener Punkt). Für die Startseite ist ein eigenes allgemeines Formular sauberer (Quelle unterscheiden: Hidden Field `{page_url}`).
- **EG-Rechner → n8n:** POST-Webhook `https://klicknerds.app.n8n.cloud/webhook/ebz-eg-rechner` (im Attribut `data-webhook` der `.ebz-rechner`-Section, 3 Instanzen). Workflow: Webhook (CORS auf https://ebz-photovoltaik.at) → Gmail an office@ebz-energie.com → 200 {"ok":true}. Fallback ohne/bei Fehler: Redirect `/kontakt/` mit Query-Params. Import-JSON: `n8n-workflow-eg-rechner-leads.json`. Live-Test steht noch aus.
- **Rechner-Defaults sind Beispielwerte** (EG-Einspeisung 10 ct, Bezug 14 ct, Beitrag 4 €/Monat): echte EBZ-Konditionen ausstehend → `DEFAULTS` in `rechner.py` + Hero-Badges der LPs aktualisieren.
- **Chatbot** (Cloudflare Worker) existiert separat; bei NAP/Fakten-Änderungen dessen System-Prompt mitziehen.

## 9. Mediathek-Bilder (verifizierte URLs)

```
Hero Startseite:  /wp-content/uploads/2023/10/EBZ-Energie-Photovoltaik-Villach.jpg
Team quer:        /wp-content/uploads/2026/09/2.jpeg   ("all in one Fachbetrieb", Warum-EBZ)
Team Beratung:    /wp-content/uploads/2026/09/1.jpeg   (Kontakt-Sektion)
Mario Zintl:      /wp-content/uploads/2023/12/Zintl_cut.png
EG/Drohne Ort:    /wp-content/uploads/2026/09/pexels-stepan-vrany-591647707-28169966-1.jpg  (Hero EG-Privat + EG-Card)
Gewerbe-Dach:     /wp-content/uploads/2026/07/gewerbe-ooe-1.jpg  (Hero EG-Gewerbe + Referenz 40 kWp)
PV-Card:          /wp-content/uploads/2023/10/PHOTO-2023-06-23-09-48-56.jpg
Speicher:         /wp-content/uploads/2025/11/Speicher-768x1364.png
Wärmepumpe:       /wp-content/uploads/2026/03/2149250264-1.jpg
EMS:              /wp-content/uploads/2025/11/Gemini_Generated_Image_dndoxkdndoxkdndo.png
Balkon:           /wp-content/uploads/2024/09/AdobeStock_712663492-web-768x512.jpg
Förderung:        /wp-content/uploads/2025/12/pexels-mikhail-nilov-6963888-1024x754.jpg
Referenzen:       …/2023/09/EBZ-Photovoltaik-Module1.jpg (EFH Villach 10 kWp),
                  …/2023/10/Stranegger-ref.jpg (Krumpendorf 25 kWp),
                  …/2024/09/Misic-fertig-2-768x576.jpg (Faakersee),
                  …/2024/09/Leiter-fertig-768x576.jpg (Landskron 20 kWp),
                  …/2024/09/Kudler-fertig-2-768x576.jpg (Blechfalz 16 kWp)
```
Weitere Projektbilder: /referenzen/ crawlen. Referenz-Bild und Referenz-Zahlen müssen immer zum selben Projekt gehören.

### Freigegebene Referenz-Zahlen
- Gewerbe OÖ: 40 kWp Ost-West Trapezblech, 40-kWh-Speicher, ~40.000 kWh/Jahr, **13.500 €/Jahr Ersparnis** (Projektseite: /referenzen/projekt-gewerbe-oberoesterreich/)
- EFH Villach: 10 kWp Ost-West, Notstrom, ~11.000 kWh/Jahr, **~80 % weniger Stromkosten**
- MFH Krumpendorf: 25 kWp + 25 kWh, Notstrom, 4 Tage Bauzeit
- Hotel Villach/Warmbad: 13 kWp bifazial, 27 kWh, ~15.000 kWh, **4.200 €/Jahr**, ~6 Jahre Amortisation

## 10. Offene Punkte (Stand: Anfang September 2026)

1. Echte EG-Konditionen vom Kunden → `rechner.py` DEFAULTS + LP-Hero-Badges
2. Live-Test Rechner → n8n → Gmail (inkl. CORS mit www-Variante prüfen)
3. WP Mail SMTP vor Livegang der Formulare
4. energyfamily-Logo-Freigabe (dann Text-Badge → `<img>`)
5. OeMAG-August-Marktpreis in Artikel 18 nachtragen (Anfang September verfügbar)
6. NAP-Vereinheitlichung website-weit (Impressum, Kontaktseite, Footer, LocalBusiness-Schema, GBP, Chatbot-Prompt): nur noch Triglavstraße 15
7. `/pv-anlage-leasen/` auf Finanzierung umschreiben
8. "ohne Subunternehmer" steht noch auf der Live-/referenzen/-Seite und in der Hotel-Referenz → entfernen
9. Allgemeine Kontaktformular-ID für Startseite (statt 6891)
10. Alt-Text des Privat-LP-Heros ans Drohnen-Motiv angepasst? (war zwischenzeitlich generisch)

## 11. Arbeitsweise mit diesem Repo

- Bestehende Deliverables NIE manuell im HTML editieren: immer die Python-Quelle ändern und neu bauen, sonst divergieren Quelle und Output.
- Vor Abgabe jeder Seite: Validierung grün (JSON-LD, Tags, 0 Dashes), Desktop- und Mobil-Screenshot (Playwright, 1280px + 390px), Grep auf verbotene Begriffe: `Subunternehmer|Leasing|Ertragsprognose|Widmanngasse|Ackerweg|90 %|5,0` (Leasing nur im Slug /pv-anlage-leasen/ erlaubt).
- Neue Seite = neue Generator-Datei nach Muster `home.py` (Komponenten aus `pages.py` importieren), Ausgabe nach `out/<bereich>/`, plus VORSCHAU-Datei.
