# SEO/GEO-Briefings fuer die Leistungs- und Standortseiten

Ziel: pro Seite ein datenbasiertes Keyword-Briefing (NUR Oesterreich), aus dem danach Title, H1,
Description, H2-Struktur, semantische Begriffe, FAQ und interne Links ueberarbeitet werden.
Die Ratgeber sind bereits optimiert und NICHT Teil dieses Durchlaufs.

## Datenquellen und Parameter (immer Oesterreich, Deutsch)
DataForSEO-MCP-Tools (Namen beginnen mit `mcp__12b9456e-...__`; Schema per ToolSearch "select:<name>" laden):
- `dataforseo_labs_google_keyword_overview` (Seed-Keywords, Volumen/KD/CPC/Trend), `..._keyword_suggestions` (limit 300, filter search_volume > 10),
  `..._related_keywords` (depth 2, limit 100), `..._search_intent` (Kandidatenliste), `..._keyword_ideas` (optional, limit 100)
  -> location_name="Austria", language_code="de". Keine deutschen (.de) Volumen verwenden.
- `serp_organic_live_advanced` -> location_name "Austria" (bzw. "Villach,Carinthia,Austria" / "Wolfsberg,Carinthia,Austria" /
  "Graz,Styria,Austria" fuer Standortseiten), language_code "de", depth 10, people_also_ask_click_depth 2.
- `on_page_content_parsing` fuer die Top-5-URLs der Haupt-SERP (H1/H2/H3, Tabellen, Begriffe).
- `ai_optimization_keyword_data_search_volume` (AI-Suchvolumen der Top-Keywords, location Austria).
- Search-Console-Daten (3 Monate) liegen, sofern vorhanden, in build/seo/gsc/<slug>.json (vom Koordinator; wenn nicht da, ignorieren).

Kosten: Jede API-Antwort enthaelt ein Feld `cost`. Summe pro Seite mitfuehren und im Bericht nennen.
Budget je Seite: max. 1,50 $. Keine LLM-Response-Calls in den Seiten-Agenten (macht der GEO-Agent).

## Output je Seite: build/seo/<slug>.json
{
  "slug": "...", "path": "/.../", "seitentyp": "leistung|standort|rechner|unternehmen",
  "stand": "2026-10-09",
  "primary": {"keyword": "...", "volume_at": 0, "kd": 0, "cpc": 0.0, "intent": "..."},
  "secondary": [{"keyword": "...", "volume_at": 0, "kd": 0, "intent": "..."}],   // 3 bis 6
  "semantic": ["..."],          // 15 bis 30 Begriffe/Entitaeten aus Suggestions + Top-5-Inhalten (Fachbegriffe, Marken, Masseinheiten, Orte)
  "long_tail": [{"keyword": "...", "volume_at": 0}],   // 10 bis 20 mit Volumen
  "questions": ["..."],         // People-also-ask + Fragen-Keywords (W-Fragen), 8 bis 15
  "serp": {"features": ["local_pack","ai_overview","people_also_ask","video",...], "top10": [{"pos":1,"domain":"...","title":"...","type":"ratgeber|anbieter|portal|..."}]},
  "competitor_outline": ["H2 ...", "H2 ..."],   // gemeinsame Struktur der Top-5 (dedupliziert, in Reihenfolge)
  "gaps": ["..."],              // Themen/Begriffe, die Top-5 haben und unsere Seite (out/<path>/index.html lesen!) nicht
  "cannibalization": ["/slug/"],// eigene Ratgeber, die auf dieselben Keywords zielen (gegen out/ pruefen: grep im Hub oder Dateinamen)
  "ai_search_volume": [{"keyword": "...", "ai_volume": 0}],
  "recommendation": {
    "title": "<= 60 Zeichen", "h1": "...", "description": "140 bis 160 Zeichen",
    "h2_outline": ["..."],      // empfohlene H2-Folge fuer die Seite (vorhandene Sektionen beruecksichtigen)
    "faq_add": ["..."],         // Fragen, die in die FAQ sollen
    "internal_links": ["/slug/ -> Ankertext"],
    "notes": "2 bis 5 Saetze: was die Seite aktuell verfehlt und was zuerst zu tun ist"
  },
  "cost_usd": 0.0
}
Dazu build/seo/<slug>.md: lesbare Kurzfassung (10 bis 20 Zeilen) fuer den Menschen.

## Regeln
- Nichts erfinden: jede Zahl aus einer API-Antwort. Keywords ohne AT-Volumen als "0" eintragen, nicht weglassen.
- Kommerzielle Leistungsseiten: Primaer-Keyword mit commercial/transactional Intent bevorzugen; informationale Begriffe
  nur als semantische Begriffe oder FAQ, nicht als Primaer-Keyword (die Ratgeber decken Info-Intent ab).
- Unsere Seite vorher lesen (out/<path>/index.html), damit "gaps" und "recommendation" konkret sind.
- Harte Site-Regeln gelten auch fuer Empfehlungstexte: keine Gedankenstriche, nie "Subunternehmer", "Leasing",
  "Ertragsprognose", "90 %", "5,0". Bewertung 4,9, Ersparnis bis zu 85 %.
- Keine Aenderungen an Seiten, nur Briefings schreiben. Nicht committen.
