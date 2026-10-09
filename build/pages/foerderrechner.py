"""Foerderrechner (/foerderrechner/): rechnet aus Vorhaben, Bundesland und Anlagengroesse die Foerderung.

Verlinkt vom Foerder-Finder der Hub-Seite /foerderungen/ (Button "Foerderung fuer mein Projekt pruefen",
Vorbelegung ueber ?v=pvsp|pv|sp|wp|ems|balkon und ?o=ktn|stmk|at). Reiner Browser-Rechner, keine
Datenuebertragung, Ergebnis fuehrt in die Beratung (Kontakt mit Vorbelegung).

PFLEGE (monatlich, zusammen mit /foerderungen/): Alle Saetze und Fristen stehen in CFG unten und sonst
nirgends. Der Rechner vergleicht bei jedem Aufruf das Tagesdatum mit den Fristen (ISO-Datum "bis"/"von")
und zeigt abgelaufene Programme von selbst als beendet. Bei einem neuen Call nur Datum und Text in CFG
aendern. Quellen: build/seo/_fakten_2026-10.md und die Foerder-Ratgeber (photovoltaik_landesfoerderungen,
foerderung_fuer_pv_speicher, landesfoerderungen_fuer_die_waermepumpe).

Rechenregeln:
- EAG-Investitionszuschuss: Satz der Kategorie mal kWp der ganzen Anlage (bis 10 kWp 150, bis 20 kWp 140).
- Speicher Bund: 150 EUR je kWh bis 50 kWh, nur mit neuer PV und ab 0,5 kWh je kWp.
- Made-in-Europe-Bonus (je 10 % auf Modul-, Wechselrichter- und Speicherzuschuss) nur als Hinweis, nie in der Summe.
- Waermepumpe: Laender nur als Spanne oder Prozentsatz, weil der Betrag von den Kosten abhaengt.
Test der Rechenlogik: python3 build/seo/test_foerderrechner.py (nach dem Build, braucht node).
"""

import json

from common import IMG, NAP, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page
from layout import page
import components as C

PATH = "/foerderrechner/"
TITLE = "Förderrechner 2026: PV, Speicher, Wärmepumpe | EBZ"
DESC = ("Kostenloser Förderrechner für Österreich: Vorhaben, Bundesland und Größe eingeben, Förderung von Bund "
        "und Land sofort sehen. Kärnten bis 6.000 € bei 10 kWp mit Speicher.")
STAND = "Stand 10. Oktober 2026"
LAENDER_STAND = "Stand Juni 2026"

R_WP_LAENDER = "/landesfoerderungen-fuer-die-waermepumpe/"
R_LAENDER = "/photovoltaik-landesfoerderungen/"

_KEINE = "Keine Landesförderung"

CFG = {
    "eag": {"a": 150, "b": 140, "sp": 150, "spMax": 50, "ratio": 0.5,
            "bis": "2026-10-22", "bisText": "22. Oktober 2026"},
    "ktn": {"pauschale": 3000, "nachruest": 1000, "minKwp": 5, "minKwh": 5,
            "von": "2026-10-12", "vonText": "12. Oktober 2026",
            "bis": "2026-12-31", "bisText": "31. Dezember 2026"},
    "ems": {"max": 600, "bis": "2027-04-15", "bisText": "15. April 2027"},
    "stand": LAENDER_STAND,
    "txt": {
        "eagEnd": ("Im bisherigen System gibt es keinen Call mehr. Laut BMWET soll 2027 eine Systemförderung für "
                   "Anlagen mit Speicher und intelligenter Steuerung starten. Die Höhe ist noch offen."),
        "spNach": ("Der Bund fördert Speicher 2026 nur zusammen mit einer neuen oder erweiterten PV-Anlage. "
                   "Ab 2027 soll die Nachrüstung laut BMWET förderbar werden."),
        "ktnPv": ("Pauschale für neue Anlagen ab 5 kWp mit neuem Speicher ab 5 kWh, zusätzlich zum Bund. "
                  "Höchstens 50 % der Baukosten."),
        "ktnNach": "Pauschale für die Nachrüstung ab 5 kWh an einer bestehenden PV-Anlage.",
        "ktnEnd": "Der Landes-Call 2026 ist beendet. Ob 2027 ein neuer Call kommt, steht noch nicht fest.",
        "wpBund": ("Kesseltausch und Sauber Heizen für Alle sind ausgeschöpft, neue Registrierungen sind nicht "
                   "möglich. Ob 2027 ein neues Programm kommt, ist offen."),
        "ems": "50 % der Kosten, höchstens 600 € je Haushalt.",
        "emsEnd": "Das Programm des Klima- und Energiefonds ist ausgelaufen.",
        "balkon": "Steckeranlagen bis 800 Watt haben keinen Einspeisezählpunkt und bekommen keinen Zuschuss.",
        "balkonEag": " Eine angemeldete Kleinanlage ab rund 3 kWp erhält 150 € je kWp vom Bund.",
        "stepBund": "Bund: Antrag vor der Montage stellen. Wer zuerst montiert, verliert den Zuschuss.",
        "stepKtn": "Land Kärnten: Antrag nach der Fertigstellung über die Förderplattform des Landes.",
        "stepEms": "Klimafonds: erst registrieren, dann die Rechnung ausstellen lassen.",
        "stepWp": "Wärmepumpe: Landesförderung vor der Bestellung klären, das übernehmen wir.",
        "stepEbz": "Wir bereiten alle Anträge vor, Sie bestätigen nur.",
    },
    # Landesregeln PV und Speicher. flat = ein Hinweis fuer alles; pv/spNeu/spNach = Regeln je Fall.
    # Regel: per (EUR je Einheit), maxKwh, cap (EUR), upTo (nur Hoechstwert), note, topf (abweichender Geber).
    "land": {
        "ktn": {"name": "Kärnten", "topf": "Land Kärnten"},
        "stmk": {"name": "Steiermark", "topf": "Land Steiermark",
                 "flat": ("Keine Landespauschale für PV oder Speicher. Manche Gemeinden zahlen 200 bis 1.000 €, "
                          "das prüfen wir für Ihre Adresse.")},
        "bgld": {"name": "Burgenland", "topf": "Land Burgenland",
                 "pv": {"note": "Keine PV-Direktförderung für private Anlagen."},
                 "spNeu": {"note": "Das Land fördert den Speicher nur, wenn der Bundeszuschuss nicht möglich ist.",
                           "fallback": {"per": 100, "maxKwh": 20, "cap": 2000,
                                        "note": "100 € je kWh nutzbarer Kapazität, höchstens 30 % der Kosten."}},
                 "spNach": {"per": 100, "maxKwh": 20, "cap": 2000,
                            "note": ("100 € je kWh nutzbarer Kapazität, höchstens 30 % der Kosten. Antrag bis "
                                     "sechs Monate nach der Rechnung.")}},
        "noe": {"name": "Niederösterreich", "topf": "Land Niederösterreich",
                "flat": ("Keine Direktförderung für PV oder Speicher. Beides bringt Punkte in der "
                         "Wohnbauförderung bei der Eigenheimsanierung.")},
        "ooe": {"name": "Oberösterreich", "topf": "Land Oberösterreich",
                "pv": {"note": "Keine Landesförderung für neue PV-Anlagen auf privaten Dächern."},
                "spNeu": {"note": ("Die Landesförderung gilt nur für die Nachrüstung und lässt sich nicht mit dem "
                                   "Speicherzuschuss des Bundes kombinieren.")},
                "spNach": {"per": 150, "maxKwh": 15, "cap": 2250,
                           "note": ("150 € je kWh, nur für PV-Anlagen, die vor dem 1. Jänner 2026 in Betrieb "
                                    "waren. Höchstens 40 % der Kosten.")}},
        "sbg": {"name": "Salzburg", "topf": "Land Salzburg",
                "flat": "Die Landesförderung für private PV-Anlagen und Speicher ist Ende 2025 ausgelaufen."},
        "tirol": {"name": "Tirol", "topf": "Land Tirol",
                  "pv": {"per": 125, "upTo": True,
                         "note": "Über die Wohnhaussanierung: 50 % der Kosten, höchstens 125 € je kWp."},
                  "spNeu": {"per": 100, "maxKwh": 10, "cap": 1000,
                            "note": "Netzdienliche Speicher: 100 € je kWh, höchstens 1.000 €."},
                  "spNach": {"per": 100, "maxKwh": 10, "cap": 1000,
                             "note": "Netzdienliche Speicher: 100 € je kWh, höchstens 1.000 €."}},
        "vbg": {"name": "Vorarlberg", "topf": "Land Vorarlberg",
                "pv": {"note": ("Anlagen auf Gebäuden fördert das Land nicht, nur Überdachungen versiegelter "
                                "Flächen ab 20 kWp.")},
                "spNeu": {"per": 50, "maxKwh": 10, "cap": 500, "topf": "VKW (Energieversorger)",
                          "note": "Speicherbonus der Vorarlberger Kraftwerke: 50 € je kWh, höchstens 500 €."},
                "spNach": {"per": 50, "maxKwh": 10, "cap": 500, "topf": "VKW (Energieversorger)",
                           "note": "Speicherbonus der Vorarlberger Kraftwerke: 50 € je kWh, höchstens 500 €."}},
        "wien": {"name": "Wien", "topf": "Stadt Wien",
                 "flat": ("Standard-Dachanlagen auf Einfamilienhäusern fördert die Stadt nicht mehr, die "
                          "Speicherförderung ist Ende 2025 ausgelaufen.")},
    },
    # Waermepumpe je Bundesland: min/max in EUR; open = Betrag haengt von den Kosten ab (nicht in der Summe).
    "wp": {
        "ktn": {"min": 0, "max": 6000, "st": "check", "badge": "In Klärung",
                "note": ("35 % der förderbaren Kosten, Obergrenze 6.000 € laut Richtlinie (laut Berichten 2026: "
                         "3.000 €). Kärnten fördert im Anschluss an den Bund. Wie neue Projekte ohne "
                         "Bundesförderung behandelt werden, klären wir vor dem Angebot mit dem Land.")},
        "stmk": {"open": True, "label": "35 %", "st": "check", "badge": "Betrag je nach Angebot",
                 "note": ("35 % der förderbaren Kosten für Eigenheime mit höchstens zwei Wohnungen. Den Betrag "
                          "rechnen wir mit Ihrem Angebot aus.")},
        "wien": {"min": 0, "max": 8000, "st": "check", "badge": LAENDER_STAND,
                 "note": "35 % der förderbaren Kosten, höchstens 8.000 €."},
        "tirol": {"open": True, "label": "25 % + 3.000 €", "st": "check", "badge": LAENDER_STAND,
                  "note": "25 % der förderfähigen Kosten plus 3.000 € Bonus."},
        "noe": {"open": True, "label": "Zinszuschuss", "st": "check", "badge": LAENDER_STAND,
                "note": "Annuitätenzuschuss von 4 % für ein Bankdarlehen statt einer Einmalzahlung."},
        "ooe": {"min": 0, "max": 1700, "st": "check", "badge": LAENDER_STAND,
                "note": ("100 € je kW Nennwärmeleistung, höchstens 1.700 €. Voraussetzung: PV ab 3 kWp oder "
                         "Ökostrom.")},
        "sbg": {"min": 5000, "max": 5000, "label": "rund 5.000 €", "st": "check", "badge": LAENDER_STAND,
                "note": "Rund 5.000 € für den Umstieg auf ein erneuerbares Heizsystem."},
        "vbg": {"min": 1000, "max": 1500, "st": "check", "badge": LAENDER_STAND,
                "note": ("1.000 € Basisförderung, plus 500 € beim Ersatz einer fossilen Heizung. Höchstens 25 % "
                         "der Kosten.")},
        "bgld": {"min": 2000, "max": 2500, "st": "check", "badge": LAENDER_STAND,
                 "note": ("2.000 € beim Tausch einer fossilen Heizung, plus 500 € Sozialzuschlag bis 43.000 € "
                          "Jahreseinkommen.")},
    },
}

LAND_ORDER = ["ktn", "stmk", "bgld", "noe", "ooe", "sbg", "tirol", "vbg", "wien"]

FORM = """
  <fieldset class="fr-set"><legend>Was planen Sie? Mehrfachauswahl möglich</legend>
    <div class="fr-chips">
      <label class="fr-chip"><input type="checkbox" id="fr-pv" checked><span>Photovoltaik</span></label>
      <label class="fr-chip"><input type="checkbox" id="fr-sp" checked><span>Stromspeicher</span></label>
      <label class="fr-chip"><input type="checkbox" id="fr-wp"><span>Wärmepumpe</span></label>
      <label class="fr-chip"><input type="checkbox" id="fr-ems"><span>Energiemanagement</span></label>
      <label class="fr-chip"><input type="checkbox" id="fr-balkon"><span>Balkonkraftwerk</span></label>
    </div>
  </fieldset>
  <div class="field"><label for="fr-land">Wo steht das Gebäude?</label>
    <select id="fr-land"><option value="">Bundesland wählen</option>__LAND_OPTIONS__</select></div>
  <div class="field" id="fr-kwp-wrap"><label for="fr-kwp">Leistung der neuen PV-Anlage (kWp)</label>
    <input id="fr-kwp" type="number" min="1" max="20" step="0.5" value="10" inputmode="decimal">
    <p class="calc__hint">Faustregel: 1 kWp je 1.000 kWh Jahresverbrauch. Ein Eigenheim liegt meist bei 5 bis 12 kWp.</p></div>
  <div class="field" id="fr-kwh-wrap"><label for="fr-kwh">Größe des Speichers (kWh)</label>
    <input id="fr-kwh" type="number" min="1" max="50" step="0.5" value="10" inputmode="decimal">
    <p class="calc__hint" id="fr-kwh-hint">Richtwert: 1 kWh Speicher je kWp Anlagenleistung.</p></div>
  <p class="form-note">Für private Anlagen bis 20 kWp. Für Betriebe, Gemeinden und größere Anlagen gelten eigene
  Sätze, die rechnen wir im Angebot. Der Rechner läuft nur in Ihrem Browser, es werden keine Daten übertragen.</p>
"""

RESULT = """
  <h3>Ihre Förderung</h3>
  <p class="calc__big" id="fr-big" aria-live="polite"><span id="fr-sum">0 €</span><small id="fr-sumnote">Richtwert für Ihr Vorhaben*</small></p>
  <div class="fr-lines" id="fr-lines"></div>
  <p class="fr-bonus" id="fr-bonus"></p>
  <p class="fr-sub" id="fr-steps-h">So beantragen Sie</p>
  <ol class="fr-steps" id="fr-steps"></ol>
  <a class="btn btn--primary btn--lg" id="fr-cta" href="/kontakt/">Dieses Ergebnis kostenlos prüfen lassen</a>
  <a class="btn btn--light" href="/foerderungen/">Alle Förderungen im Überblick</a>
  <p class="calc__note">*Richtwert, kein Bescheid. Über die Förderung entscheidet der Fördergeber, die Töpfe sind
  begrenzt. Wir prüfen Ihr Projekt vor dem Angebot und stellen die Anträge.</p>
"""

JS = r"""
(function(){
/*CALC*/
var CFG = __CFG__;
function eur(v){ return Math.round(v).toLocaleString("de-DE") + " €"; }
function num(v){ return (Math.round(v * 10) / 10).toLocaleString("de-DE"); }
function span(min, max){
  if(max === 0) return "0 €";
  if(min === max) return eur(max);
  if(min === 0) return "bis " + eur(max);
  return Math.round(min).toLocaleString("de-DE") + " bis " + eur(max);
}
function compute(inp, t){
  var E = CFG.eag, K = CFG.ktn, M = CFG.ems, T = CFG.txt, L = CFG.land[inp.land] || null;
  var lines = [], steps = [], bonus = 0;
  var eagOn = t <= E.bis;
  var nach = inp.sp && !inp.pv;
  function add(topf, min, max, st, badge, note, label){
    lines.push({topf: topf, min: min, max: max, st: st, badge: badge, note: note, label: label || span(min, max)});
  }
  function rule(r, units){
    return Math.min(Math.min(units, r.maxKwh || units) * r.per, r.cap || Infinity);
  }
  if(inp.pv){
    if(eagOn){
      var rate = inp.kwp <= 10 ? E.a : E.b, pvAmt = inp.kwp * rate;
      add("Bund · Photovoltaik", pvAmt, pvAmt, "ok", "Antrag bis " + E.bisText,
          num(inp.kwp) + " kWp × " + rate + " € aus dem EAG-Investitionszuschuss.");
      bonus += pvAmt * 0.2;
      if(inp.sp){
        var need = inp.kwp * E.ratio;
        if(inp.kwh < need){
          add("Bund · Stromspeicher", 0, 0, "none", "Speicher zu klein",
              "Der Bund fördert Speicher ab 0,5 kWh je kWp. Bei " + num(inp.kwp) + " kWp sind das mindestens " + num(need) + " kWh.");
        } else {
          var spAmt = Math.min(inp.kwh, E.spMax) * E.sp;
          add("Bund · Stromspeicher", spAmt, spAmt, "ok", "Antrag bis " + E.bisText,
              num(Math.min(inp.kwh, E.spMax)) + " kWh × " + E.sp + " €, nur zusammen mit der neuen PV-Anlage.");
          bonus += spAmt * 0.1;
        }
      }
      steps.push(T.stepBund);
    } else {
      add(inp.sp ? "Bund · Photovoltaik und Speicher" : "Bund · Photovoltaik", 0, 0, "end", "Call beendet", T.eagEnd, "offen");
    }
  }
  if(nach) add("Bund · Stromspeicher", 0, 0, "none", "Keine Förderung", T.spNach);

  if(L && (inp.pv || inp.sp)){
    if(inp.land === "ktn"){
      var kSt = t < K.von ? "soon" : (t <= K.bis ? "ok" : "end");
      var kBadge = kSt === "soon" ? "Startet am " + K.vonText : "Antrag bis " + K.bisText;
      if(inp.pv && inp.sp){
        if(inp.kwp < K.minKwp || inp.kwh < K.minKwh){
          add("Land Kärnten · PV mit Speicher", 0, 0, "none", "Nicht erfüllt", "Die Pauschale von " + eur(K.pauschale) + " gilt ab 5 kWp mit neuem Speicher ab 5 kWh.");
        } else if(kSt === "end"){
          add("Land Kärnten · PV mit Speicher", 0, 0, "end", "Call beendet", T.ktnEnd);
        } else {
          add("Land Kärnten · PV mit Speicher", K.pauschale, K.pauschale, kSt, kBadge, T.ktnPv);
          steps.push(T.stepKtn);
        }
      } else if(inp.pv){
        add("Land Kärnten · Photovoltaik", 0, 0, "none", "Nur mit Speicher", "Mit einem neuen Speicher ab 5 kWh zahlt Kärnten " + eur(K.pauschale) + " Pauschale.");
      } else {
        if(inp.kwh < K.minKwh){
          add("Land Kärnten · Speicher nachrüsten", 0, 0, "none", "Nicht erfüllt", "Die Pauschale für die Nachrüstung gilt ab 5 kWh.");
        } else if(kSt === "end"){
          add("Land Kärnten · Speicher nachrüsten", 0, 0, "end", "Call beendet", T.ktnEnd);
        } else {
          add("Land Kärnten · Speicher nachrüsten", K.nachruest, K.nachruest, kSt, kBadge, T.ktnNach);
          steps.push(T.stepKtn);
        }
      }
    } else if(L.flat){
      add(L.topf, 0, 0, "none", "Keine Landesförderung", L.flat);
    } else {
      if(inp.pv && L.pv){
        if(L.pv.per){
          add(L.topf + " · Photovoltaik", 0, inp.kwp * L.pv.per, "check", CFG.stand, L.pv.note);
        } else {
          add(L.topf + " · Photovoltaik", 0, 0, "none", "Keine Landesförderung", L.pv.note);
        }
      }
      if(inp.sp){
        var r = nach ? L.spNach : L.spNeu;
        if(r && !r.per && r.fallback && !eagOn) r = r.fallback;
        if(r){
          var rTopf = (r.topf || L.topf) + " · Stromspeicher";
          if(r.per){
            var rAmt = rule(r, inp.kwh);
            add(rTopf, rAmt, rAmt, "check", CFG.stand, r.note);
          } else {
            add(rTopf, 0, 0, "none", "Keine Landesförderung", r.note);
          }
        }
      }
    }
  }

  if(inp.wp){
    add("Bund · Wärmepumpe", 0, 0, "end", "Ausgeschöpft", T.wpBund);
    var W = L ? CFG.wp[inp.land] : null;
    if(W){
      lines.push({topf: L.topf + " · Wärmepumpe", min: W.min || 0, max: W.max || 0, open: !!W.open, st: W.st,
                  badge: W.badge, note: W.note, label: W.label || span(W.min || 0, W.max || 0)});
      steps.push(T.stepWp);
    }
  }
  if(inp.ems){
    if(t <= M.bis){
      add("Klimafonds · Energiemanagement", 0, M.max, "ok", "Programm bis " + M.bisText, T.ems);
      steps.push(T.stepEms);
    } else {
      add("Klimafonds · Energiemanagement", 0, 0, "end", "Beendet", T.emsEnd);
    }
  }
  if(inp.balkon) add("Bund und Land · Balkonkraftwerk", 0, 0, "none", "Keine Förderung", T.balkon + (eagOn ? T.balkonEag : ""));

  var min = 0, max = 0, open = false;
  lines.forEach(function(l){ min += l.min; max += l.max; if(l.open) open = true; });
  if(steps.length) steps.push(T.stepEbz);
  return {lines: lines, min: min, max: max, open: open, steps: steps, bonus: bonus,
          needLand: !L && (inp.pv || inp.sp || inp.wp), any: inp.pv || inp.sp || inp.wp || inp.ems || inp.balkon};
}
/*END*/
  var $ = function(id){ return document.getElementById(id); };
  if(!$("fr-land")) return;
  var boxes = ["pv", "sp", "wp", "ems", "balkon"];
  function today(){ var d = new Date(); return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); }
  function val(id, lo, hi, def){ var v = parseFloat(String($(id).value).replace(",", ".")); if(isNaN(v)) v = def; return Math.max(lo, Math.min(hi, v)); }
  function read(){
    var inp = {land: $("fr-land").value, kwp: val("fr-kwp", 1, 20, 10), kwh: val("fr-kwh", 1, 50, 10)};
    boxes.forEach(function(b){ inp[b] = $("fr-" + b).checked; });
    return inp;
  }
  function render(){
    var inp = read(), res = compute(inp, today());
    $("fr-kwp-wrap").classList.toggle("fr-hide", !inp.pv);
    $("fr-kwh-wrap").classList.toggle("fr-hide", !inp.sp);
    $("fr-kwh-hint").textContent = inp.pv
      ? "Richtwert: 1 kWh Speicher je kWp. Der Bund verlangt mindestens 0,5 kWh je kWp."
      : "Ohne neue PV-Anlage rechnen wir mit einer Nachrüstung an Ihrer bestehenden Anlage.";
    var sum = span(res.min, res.max), note = "Richtwert für Ihr Vorhaben*";
    if(!res.any){ sum = "0 €"; note = "Bitte wählen Sie mindestens ein Vorhaben."; }
    else if(res.max === 0 && res.open){ sum = "Nach Angebot"; note = "Der Landesanteil hängt von Ihren Kosten ab*"; }
    else if(res.max === 0){ note = "Für diese Auswahl läuft derzeit keine Förderung*"; }
    else if(res.open){ note = "Richtwert*, dazu der Landesanteil für die Wärmepumpe"; }
    $("fr-sum").textContent = sum;
    $("fr-sumnote").textContent = note;
    $("fr-big").classList.toggle("calc__big--range", sum.length > 9);
    var html = "";
    res.lines.forEach(function(l){
      html += '<div class="fr-line' + (l.max === 0 && !l.open ? " is-zero" : "") + '"><div class="fr-line__top"><span>' + l.topf +
              "</span><b>" + l.label + '</b></div><span class="fr-st fr-st--' + l.st + '">' + l.badge + "</span><p>" + l.note + "</p></div>";
    });
    if(res.needLand) html += '<div class="fr-line is-zero"><div class="fr-line__top"><span>Landesförderung</span><b>offen</b></div><p>Bundesland wählen, um den Landesanteil zu sehen.</p></div>';
    $("fr-lines").innerHTML = html;
    var extra = [];
    if(res.bonus > 0) extra.push("Mit Made-in-Europe-Bonus (europäische Module, Wechselrichter und Speicher) bis zu " + eur(res.bonus) + " mehr vom Bund.");
    if(inp.land && inp.land !== "ktn" && inp.land !== "stmk") extra.push("EBZ montiert in Kärnten und der Steiermark. Andere Bundesländer prüfen wir auf Anfrage.");
    $("fr-bonus").textContent = extra.join(" ");
    $("fr-bonus").classList.toggle("fr-hide", !extra.length);
    $("fr-steps").innerHTML = res.steps.map(function(s){ return "<li>" + s + "</li>"; }).join("");
    $("fr-steps-h").classList.toggle("fr-hide", !res.steps.length);
    $("fr-steps").classList.toggle("fr-hide", !res.steps.length);
    var parts = [];
    if(inp.pv) parts.push("PV " + num(inp.kwp) + " kWp");
    if(inp.sp) parts.push((inp.pv ? "Speicher " : "Speicher nachrüsten ") + num(inp.kwh) + " kWh");
    if(inp.wp) parts.push("Wärmepumpe");
    if(inp.ems) parts.push("Energiemanagement");
    if(inp.balkon) parts.push("Balkonkraftwerk");
    var cta = $("fr-cta"), base = cta.getAttribute("href").split("?")[0];
    var where = CFG.land[inp.land] ? ", " + CFG.land[inp.land].name : "";
    cta.setAttribute("href", base + "?anliegen=" + encodeURIComponent("Förderrechner: " + (parts.join(", ") || "noch offen") + where + ", Richtwert " + sum));
  }
  var q = new URLSearchParams(window.location.search), v = q.get("v"), o = q.get("o");
  var pre = {pvsp: ["pv", "sp"], pv: ["pv"], sp: ["sp"], wp: ["wp"], ems: ["ems"], balkon: ["balkon"]}[v];
  if(pre) boxes.forEach(function(b){ $("fr-" + b).checked = pre.indexOf(b) > -1; });
  $("fr-land").value = (o === "ktn" || o === "stmk") ? o : (o === "at" ? "" : "ktn");
  boxes.forEach(function(b){ $("fr-" + b).addEventListener("change", render); });
  ["fr-land", "fr-kwp", "fr-kwh"].forEach(function(id){ $(id).addEventListener("input", render); $(id).addEventListener("change", render); });
  render();
})();
"""

FAQ = [
    ("Wie genau ist der Förderrechner?",
     "Für den Bundeszuschuss für Photovoltaik und Speicher, die Kärntner Landespauschale und die EMS-Förderung "
     "rechnet er mit den veröffentlichten Sätzen und ist damit auf den Euro nachvollziehbar. Für die Wärmepumpe "
     "und für Bundesländer außerhalb unseres Montagegebiets zeigt er Spannen, weil der Betrag von den Kosten und "
     "vom Budget des Landes abhängt. Das Ergebnis ist ein Richtwert, kein Bescheid."),
    ("Welche Förderungen rechnet der Rechner ein?",
     "Den EAG-Investitionszuschuss des Bundes (150 Euro je kWp bis 10 kWp, 140 Euro bis 20 kWp, 150 Euro je kWh "
     "Speicher), die Landespauschale Kärnten (3.000 Euro für PV mit Speicher, 1.000 Euro für die Nachrüstung), die "
     "Speicherprogramme in Oberösterreich, Tirol, Burgenland und Vorarlberg, die EMS-Förderung des Klimafonds "
     "(bis 600 Euro) und die Landesförderungen für Wärmepumpen. Gemeindeförderungen und der "
     "Made-in-Europe-Bonus stehen als Hinweis dabei, nicht in der Summe."),
    ("Zeigt der Rechner auch abgelaufene Programme an?",
     "Ja, aber nicht in der Summe. Der Rechner vergleicht bei jedem Aufruf das Datum mit den Fristen der Programme. "
     "Ist eine Frist vorbei, steht der Topf als beendet in der Liste und zählt nicht mehr mit. So sehen Sie auf "
     "einen Blick, was heute beantragbar ist und was nicht."),
    ("Warum steht bei der Wärmepumpe kein fixer Betrag?",
     "Die Bundesförderung für den Heizungstausch ist derzeit ausgeschöpft, und die Länder fördern meist einen "
     "Prozentsatz der Kosten mit einer Obergrenze. Kärnten und die Steiermark zahlen 35 Prozent der förderbaren "
     "Kosten. Den Betrag für Ihr Haus rechnen wir mit dem Angebot aus und klären vorab mit dem Land, ob das Budget "
     "reicht."),
    ("Kann ich Bundes- und Landesförderung kombinieren?",
     "In Kärnten ja: Die Landespauschale wird ohne Anrechnung zusätzlich zum Bundeszuschuss gezahlt, höchstens "
     "50 Prozent der Baukosten. In Oberösterreich schließen sich der Speicherzuschuss des Bundes und die "
     "Landesförderung aus, im Burgenland zahlt das Land den Speicher nur, wenn der Bund nicht möglich ist. Der "
     "Rechner berücksichtigt diese Regeln."),
    ("Gilt der Rechner auch für Betriebe und Gemeinden?",
     "Nein, er rechnet für private Anlagen bis 20 kWp. Für Betriebe gelten eigene Sätze: beim Bund 140 bis 120 Euro "
     "je kWp, bei der EMS-Förderung 30 Prozent bis 20.000 Euro, dazu Landesprogramme für Gewerbe. Das rechnen wir "
     "im Angebot für Ihr Projekt."),
]


def _table(headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join(
        "<tr>" + "".join(f'<td class="{"hl" if i == 0 else ""}">{c}</td>' for i, c in enumerate(r)) + "</tr>"
        for r in rows
    )
    return (f'<div class="art-tablewrap eg-reveal" style="margin-top:32px">'
            f'<table class="art-table"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')


def _calc_section():
    options = "".join(f'<option value="{k}">{CFG["land"][k]["name"]}</option>' for k in LAND_ORDER)
    form = FORM.replace("__LAND_OPTIONS__", options)
    script = JS.replace("__CFG__", json.dumps(CFG, ensure_ascii=False))
    return f"""
  <section class="section" id="rechner">
    <div class="wrap">
      <div class="calc">
        <form class="form-card eg-reveal js-calc" id="fr-form" onsubmit="return false">{form}</form>
        <div>
          <div class="calc__res eg-reveal">{RESULT}</div>
        </div>
      </div>
      <p class="form-note center eg-reveal" style="margin-top:22px">Fördersätze und Fristen {STAND}, Daten der
      anderen Bundesländer {LAENDER_STAND}. Quellen: EAG-Abwicklungsstelle, Land Kärnten, Klima- und Energiefonds,
      umweltfoerderung.at, Landesförderstellen.</p>
    </div>
  </section>
  <script>{script}</script>"""


def _methodik_section():
    rows = [
        ("Bund: Photovoltaik",
         "150 € je kWp bis 10 kWp, 140 € je kWp über 10 bis 20 kWp, jeweils für die ganze Anlage",
         "Antrag vor der Montage, im laufenden Call"),
        ("Bund: Stromspeicher",
         "150 € je kWh, höchstens 50 kWh",
         "Nur mit neuer oder erweiterter PV-Anlage, ab 0,5 kWh je kWp"),
        ("Made-in-Europe-Bonus",
         "Je 10 % Zuschlag auf den Zuschuss für Module, Wechselrichter und Speicher",
         "Nur als Hinweis, nicht in der Summe"),
        ("Land Kärnten",
         "3.000 € Pauschale für PV mit Speicher, 1.000 € für die Speicher-Nachrüstung",
         "Ab 5 kWp und 5 kWh, höchstens 50 % der Baukosten, Antrag nach der Fertigstellung"),
        ("Land Steiermark",
         "Keine Pauschale für private Anlagen",
         "Gemeinden zahlen teils 200 bis 1.000 €, Ökofonds erst ab 20 kWp"),
        ("Andere Bundesländer",
         "Tirol bis 125 € je kWp und 100 € je kWh bis 1.000 €, Oberösterreich 150 € je kWh bis 2.250 € "
         "(Nachrüstung), Burgenland 100 € je kWh bis 2.000 €, Vorarlberg 50 € je kWh bis 500 € (VKW)",
         f"Länderdaten {LAENDER_STAND}, Details im " + a(R_LAENDER, "Ländervergleich")),
        ("Wärmepumpe",
         "Bund derzeit ausgeschöpft. Länder: Kärnten und Steiermark 35 % der förderbaren Kosten, Wien 35 % bis "
         "8.000 €, weitere als Pauschale",
         "Als Spanne oder Prozentsatz, Details im " + a(R_WP_LAENDER, "Wärmepumpen-Ländervergleich")),
        ("Energiemanagement",
         "50 % der Kosten, höchstens 600 € je Haushalt",
         "Klima- und Energiefonds, Registrierung vor der Rechnung"),
        ("Balkonkraftwerk",
         "Keine Förderung für Steckeranlagen bis 800 Watt",
         "Kein Einspeisezählpunkt, daher kein Zuschuss"),
    ]
    return f"""
  <section class="section section--tight" style="background:#fff;border-block:1px solid var(--line)" id="methodik">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Zum Nachrechnen</p>
      <h2 class="center eg-reveal">So rechnet der Förderrechner</h2>
      <p class="lead center eg-reveal" style="max-width:64ch;margin-inline:auto">Jeder Betrag folgt einem
      veröffentlichten Satz. Ob ein Programm gerade beantragbar ist, prüft der Rechner bei jedem Aufruf anhand der
      Fristen.</p>
      {_table(["Topf", "Satz", "Bedingung"], rows)}
    </div>
  </section>"""


def build():
    body = "".join([
        C.page_hero(
            eyebrow="Förderrechner 2026 · kostenlos, ohne Anmeldung",
            h1="Förderrechner: Wie viel Förderung bekommen Sie für PV, Speicher und Wärmepumpe?",
            lead=("Vorhaben wählen, Bundesland und Größe eintragen. Der Rechner zeigt, was Bund und Land heute "
                  "zahlen und in welcher Reihenfolge Sie beantragen."),
            cta=("#rechner", "Jetzt rechnen"), cta2=("foerderungen", "Alle Förderungen im Überblick"),
        ),
        _calc_section(),
        _methodik_section(),
        C.faq_section(FAQ),
        C.linkgrid_section("Weiterlesen", [
            ("foerderungen", "Förderungen 2026 im Überblick"),
            ("foerderung_kaernten", "Förderung Kärnten: 3.000 € Pauschale"),
            ("foerderung_steiermark", "Förderung Steiermark"),
            ("solarrechner", "Solarrechner: Kosten und Ertrag"),
            ("finanzierung", "Finanzierung: Eigentum ab Tag 1"),
            ("photovoltaik", "Photovoltaikanlage mit Speicher"),
            ("batteriespeicher", "Batteriespeicher"),
            ("waermepumpe", "Wärmepumpe"),
        ]),
        C.contact_section(
            "Ergebnis prüfen lassen, kostenlos",
            "Schicken Sie uns Ihr Ergebnis. Wir prüfen die Förderung für Ihr Projekt und bereiten die Anträge vor.",
            page_label="Förderrechner",
        ),
        C.finalcta(
            "Vom Richtwert zum Antrag",
            "Kostenlose Erstberatung mit Förderprüfung. Wir melden uns innerhalb eines Werktags.",
            trust=[(f"{NAP['rating']} auf Google", True), ("300+ Projekte", False),
                   ("Anträge inklusive", False), ("Antwort in einem Werktag", False)],
        ),
        f'<div class="wrap"><p class="form-note" style="padding:8px 0 40px">*Richtwerte für private Anlagen, kein '
        f'Bescheid. Fördersätze und Fristen {STAND}, Daten der anderen Bundesländer {LAENDER_STAND}; Angaben zu 2027 '
        f'laut BMWET geplant, nicht beschlossen. Änderungen durch die Fördergeber vorbehalten. Fachlich geprüft von '
        f'{AUTHOR}, {AUTHOR_ROLE}.</p></div>',
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ), og_image=IMG["foerderung"])
    return write_page("foerderrechner/index.html", html)


if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import theme
    theme.write_assets()
    build()
