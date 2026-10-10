"""Ortsseiten aus gemeinsamer Vorlage + Uebersicht /standorte/.

Jede Datei build/content/standorte/<ort>.py liefert ein Dict ORT (Schema: build/content/standorte/README.md).
Die Vorlage stellt Aufbau, Vertrauensbausteine (Bewertungen, Referenzen aus referenz_projekte.py, Ablauf,
Finanzierung) und die zentral gepflegte Foerder-Kurzfassung je Bundesland; alle ortsbezogenen Texte, lokalen
Fakten und Quellen kommen aus der Inhaltsdatei. So bleibt jede Seite inhaltlich eigenstaendig, und eine
Aenderung an Foerdersaetzen oder Regeln wird an EINER Stelle gemacht (LAND unten).

Aufruf einzeln (fuer die Arbeit an einer Seite): python3 build/pages/standorte.py <dateiname ohne .py>
Ohne Argument (und ueber build_all.py): alle Ortsseiten plus /standorte/.
Eigene Module haben Villach, Klagenfurt, Wolfsberg, Graz und die Region Steiermark (build/pages/standort_*.py).
"""

import importlib.util
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # build/ (fuer Direktaufruf)

from common import (IMG, NAP, AUTHOR, AUTHOR_ROLE, S, STANDORTE, BASE, faq_jsonld, breadcrumb_jsonld, u, a, href,
                    tel_link, write_page, load_reviews, standorte, standort_exists)
from layout import page
import components as C

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(os.path.dirname(HERE), "content", "standorte")
STATIC_IMG = os.path.join(os.path.dirname(HERE), "static", "img")
STAND = "Oktober 2026"

# Zentral gepflegte Kurzfassung je Bundesland (Quelle: build/seo/_fakten_2026-10.md). KEINE Fristen hier.
# Steiermark Waermepumpe: laut wohnbau.steiermark.at (abgerufen 10.10.2026) derzeit keine Antragstellung moeglich,
# "auf absehbare Zeit keine Foerderungsmoeglichkeit". Die frueher genannten 35 % gelten NICHT mehr.
LAND = {
    "ktn": {
        "name": "Kärnten", "in": "in Kärnten", "foerder_key": "foerderung_kaernten",
        "foerder_label": "PV-Förderung Kärnten im Detail",
        "foerder_p": ("Das Land Kärnten zahlt für neue private PV-Anlagen ab 5 kWp mit Speicher ab 5 kWh eine Pauschale "
                      "von 3.000 Euro, zusätzlich zum Investitionszuschuss des Bundes (2026: 150 Euro je kWp bis 10 kWp "
                      "und 150 Euro je kWh Speicher). Bei der Wärmepumpe ist die Bundesförderung derzeit ausgeschöpft, "
                      "das Land Kärnten zahlt für den Umstieg im Eigenheim eine Pauschale von 3.000 Euro."),
        "foerder_bullets": [
            "Landespauschale Kärnten: 3.000 € für PV ab 5 kWp mit Speicher ab 5 kWh",
            "Bund: 150 €/kWp bis 10 kWp und 150 €/kWh Speicher",
            "Wärmepumpe: 3.000 € Landespauschale Kärnten, Bund derzeit ausgeschöpft",
        ],
        "kpi": ("3.000 €", "Landespauschale Kärnten für PV mit Speicher"),
    },
    "stmk": {
        "name": "Steiermark", "in": "in der Steiermark", "foerder_key": "foerderung_steiermark",
        "foerder_label": "PV-Förderung Steiermark im Detail",
        "foerder_p": ("Die Steiermark zahlt keine Landespauschale für private PV-Anlagen. Es gilt der "
                      "Investitionszuschuss des Bundes (2026: 150 Euro je kWp bis 10 kWp und 150 Euro je kWh Speicher). "
                      "Für neue Wärmepumpen nimmt das Land Steiermark derzeit keine Förderanträge an, und auch die "
                      "Bundesförderung ist ausgeschöpft. Der Heizungstausch rechnet sich deshalb vor allem über den "
                      "eigenen Sonnenstrom."),
        "foerder_bullets": [
            "Bund: 150 €/kWp bis 10 kWp und 150 €/kWh Speicher",
            "Keine PV-Landespauschale, einzelne Gemeinden zahlen einen Zuschuss",
            "Wärmepumpe: Land Steiermark und Bund nehmen derzeit keine Anträge an",
        ],
        "kpi": ("4 bis 6 Jahre", "typische Amortisation einer PV-Anlage*"),
    },
}

REQUIRED = ["datei", "key", "name", "kurz", "land", "title", "description", "h1", "lead", "badges", "hero_img",
            "hero_alt", "intro", "lokal", "netz", "waermepumpe", "foerderung_lokal", "referenzen", "umgebung",
            "faq", "quellen"]


def _projekte():
    """Laedt referenz_projekte.py ueber den Dateipfad (pages/ liegt nicht im Suchpfad von build_all)."""
    if "referenz_projekte" in sys.modules:
        return sys.modules["referenz_projekte"]
    spec = importlib.util.spec_from_file_location("referenz_projekte", os.path.join(HERE, "referenz_projekte.py"))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["referenz_projekte"] = mod
    spec.loader.exec_module(mod)
    return mod


def _img(val):
    """IMG-Key oder Pfad unter /assets/img/ (muss in build/static/img existieren oder ein IMG-Wert sein)."""
    if val in IMG:
        return IMG[val]
    if val.startswith("/assets/img/") and (val in IMG.values() or os.path.exists(os.path.join(STATIC_IMG, os.path.basename(val)))):
        return val
    raise ValueError(f"Bild unbekannt: {val}")


def _plain(html_str):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html_str)).strip()


def check(o):
    """Inhaltliche Mindestanforderungen an eine Ortsdatei. Gibt Fehlerliste zurueck."""
    err = [f"Pflichtfeld fehlt: {k}" for k in REQUIRED if k not in o]
    if err:
        return err
    if o["land"] not in LAND:
        err.append("land muss 'ktn' oder 'stmk' sein")
    if o["key"] not in S:
        err.append(f"key {o['key']} fehlt in common.S")
    if len(o["title"]) > 60:
        err.append(f"title {len(o['title'])} Zeichen (max. 60)")
    if not 140 <= len(o["description"]) <= 160:
        err.append(f"description {len(o['description'])} Zeichen (140 bis 160)")
    if not 6 <= len(o["faq"]) <= 9:
        err.append("faq: 6 bis 9 Fragen")
    if sum("ärmepumpe" in q + ant for q, ant in o["faq"]) < 2:
        err.append("faq: mindestens 2 Fragen zur Wärmepumpe")
    if len(o["quellen"]) < 4 or any(not url.startswith("https://") for _l, url in o["quellen"]):
        err.append("quellen: mindestens 4 offizielle Quellen mit https-URL")
    if len(o["lokal"].get("rows", [])) < 5:
        err.append("lokal.rows: mindestens 5 Zeilen")
    for sec in ("intro", "netz", "waermepumpe"):
        if len(o[sec].get("paragraphs", [])) < 2:
            err.append(f"{sec}.paragraphs: mindestens 2 Absätze")
    words = len(_plain(" ".join(
        [o["lead"]] + o["intro"]["paragraphs"] + o["netz"]["paragraphs"] + o["waermepumpe"]["paragraphs"]
        + o["foerderung_lokal"] + [v for _k, v in o["lokal"]["rows"]] + [q + " " + ant for q, ant in o["faq"]])).split())
    if words < 650:
        err.append(f"zu wenig eigener Text: {words} Wörter (mindestens 650 ortsbezogene Wörter)")
    try:
        _img(o["hero_img"]); _img(o["netz"]["img"]); _img(o["waermepumpe"]["img"])
    except (ValueError, KeyError) as exc:
        err.append(str(exc))
    known = {p["slug"] for p in _projekte().PROJEKTE}
    for slug in o["referenzen"].get("slugs", []):
        if slug not in known:
            err.append(f"Referenz unbekannt: {slug}")
    if not 1 <= len(o["referenzen"].get("slugs", [])) <= 3:
        err.append("referenzen.slugs: 1 bis 3 Projekte aus referenz_projekte.py")
    return err


def _reference_items(slugs):
    rp = _projekte()
    path_for = rp.path_for
    by = {p["slug"]: p for p in rp.PROJEKTE}
    items = []
    for slug in slugs:
        p = by[slug]
        num, sub = p["badges"][-1]
        specs = ", ".join(f"{n} {l}" for n, l in p["kpis"][:3]) + "."
        items.append({"img": p["hero_img"], "alt": p["hero_alt"],
                      "title": f'<a href="{path_for(p)}">{p["kurz"]}</a>',
                      "specs": f'{p["ort"]}. {specs}', "result": num, "result_sub": sub})
    return items


def _quellen(o):
    lis = "".join(f'<li><a href="{url}" rel="nofollow noopener" target="_blank">{label}</a></li>'
                  for label, url in o["quellen"])
    return f"""
  <section class="section section--tight">
    <div class="wrap" style="max-width:860px">
      <div class="art-eeat">
        <img src="{IMG['mario']}" alt="{AUTHOR}, {AUTHOR_ROLE}" width="92" height="92" loading="lazy">
        <p><b>Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</b> Lokale Angaben zu {o['name']} stammen aus den
        unten verlinkten amtlichen und offiziellen Quellen, Stand {STAND}. Förderungen und Netzbedingungen ändern
        sich; verbindlich ist immer die Auskunft der zuständigen Stelle.</p>
      </div>
      <div class="art-sources"><p><b>Quellen für {o['kurz']}</b></p><ul>{lis}</ul></div>
    </div>
  </section>"""


def _service_jsonld(o, path):
    data = {
        "@context": "https://schema.org", "@type": "Service",
        "@id": u(path).rstrip("/") + "/#service",
        "serviceType": "Photovoltaik, Batteriespeicher und Wärmepumpe: Planung, Montage und Förderabwicklung",
        "name": "Photovoltaik und Wärmepumpe " + o.get("ort_in", f"in {o['name']}"),
        "areaServed": {"@type": "AdministrativeArea", "name": o.get("area_name", o["name"]),
                       "containedInPlace": {"@type": "AdministrativeArea", "name": LAND[o["land"]]["name"]}},
        "provider": {"@type": "SolarInstallation", "@id": BASE + "/#business", "name": NAP["name"],
                     "telephone": NAP["phone_display"], "url": BASE + "/",
                     "address": {"@type": "PostalAddress", "streetAddress": NAP["street"], "postalCode": NAP["zip"],
                                 "addressLocality": NAP["city"], "addressCountry": NAP["country"]}},
        "url": u(path),
    }
    return json.dumps(data, ensure_ascii=False)


def render(o):
    L = LAND[o["land"]]
    kurz, name = o["kurz"], o["name"]
    # Ortsangaben mit Praeposition (optional, z. B. "im Murtal" / "ins Murtal" statt "in Murtal" / "nach Murtal")
    ort_in = o.get("ort_in", f"in {kurz}")
    ort_nach = o.get("ort_nach", f"nach {kurz}")
    path = S[o["key"]]
    rating, count, reviews = load_reviews()
    bew = f"{count} Bewertungen" if count else "echten Bewertungen"
    netz = o["netz"].get("betreiber", "dem Netzbetreiber")
    umgebung = ", ".join(o["umgebung"])
    nachbarn = standorte(o["land"], ohne=o["key"])
    region_link = [("pv_steiermark", "Photovoltaik in der Steiermark")] if o["land"] == "stmk" and standort_exists("pv_steiermark") else []

    body = "".join([
        C.hero(
            eyebrow=o.get("eyebrow", f"Photovoltaik und Wärmepumpe {kurz}"),
            h1=o["h1"], lead=o["lead"], badges=o["badges"],
            img=_img(o["hero_img"]), img_alt=o["hero_alt"],
            float_num=rating, float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_secondary=("#vor-ort", f"Vor Ort {ort_in}"),
        ),
        C.kpis(o.get("kpis") or [
            ("bis zu 85 %", "weniger Stromkosten mit PV und Speicher*"),
            L["kpi"],
            ("300+", "dokumentierte Projekte in 6 Bundesländern"),
            (NAP["rating"], f"Sterne auf Google, {bew}"),
        ]),
        C.text_block(eyebrow="Kurz erklärt", h2=o["intro"]["h2"], paragraphs=o["intro"]["paragraphs"]),
        C.facts_panel(
            eyebrow=f"Vor Ort {ort_in}",
            h2=o["lokal"]["h2"],
            intro=o["lokal"]["intro"],
            rows=list(o["lokal"]["rows"]) + [
                ("Orte in der Umgebung", umgebung),
                ("Ihr Fachbetrieb", f"{NAP['name']}, {NAP['street']}, {NAP['zip']} {NAP['city']}. "
                                    f"Für die Erstberatung kommen wir zu Ihnen {ort_nach}."),
                ("Telefon", f"{tel_link()} ({NAP['hours']})"),
            ],
            actions=[("Beratung anfragen", href("kontakt"), ""), ("Anrufen", NAP["phone_href"], "")],
        ).replace('<section class="section"', '<section id="vor-ort" class="section"', 1),
        C.media_text(
            eyebrow="Behörde und Netzbetreiber", h2=o["netz"]["h2"], paragraphs=o["netz"]["paragraphs"],
            img=_img(o["netz"]["img"]), alt=o["netz"]["alt"], bullets=o["netz"].get("bullets"),
            cta=("photovoltaik", "So planen wir Ihre PV-Anlage"),
        ),
        C.media_text(
            eyebrow=f"Wärmepumpe {kurz}", h2=o["waermepumpe"]["h2"], paragraphs=o["waermepumpe"]["paragraphs"],
            img=_img(o["waermepumpe"]["img"]), alt=o["waermepumpe"]["alt"],
            bullets=list(o["waermepumpe"].get("bullets", [])) + [
                a("/kosten-einer-waermepumpe/", "Was eine Wärmepumpe kostet"),
                a("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"),
            ],
            reverse=True, cta=("waermepumpe", "Mehr zur Wärmepumpe"), anchor="waermepumpe",
        ),
        C.media_text(
            eyebrow=f"Förderung {L['name']}",
            h2=o.get("foerderung_h2", f"Förderung für Photovoltaik und Wärmepumpe {ort_in}"),
            paragraphs=[L["foerder_p"]] + list(o["foerderung_lokal"]) + [
                "Welche Programme heute beantragbar sind, zeigt der "
                + a("foerderrechner", "Förderrechner") + ". Wir prüfen die Förderung vor dem Angebot und bereiten die "
                "Anträge vor; Antragsteller bleiben Sie, das Geld kommt auf Ihr Konto."],
            img=IMG["foerderung"], alt=f"Beratung zur Förderung für Photovoltaik und Wärmepumpe {L['in']}",
            bullets=L["foerder_bullets"] + [a(L["foerder_key"], L["foerder_label"])],
            cta=("foerderungen", "Aktuelle Förderungen"), dark=True,
        ),
        C.finance_band(),
        C.reference_cards(
            eyebrow="Referenzen mit Zahlen", h2=o["referenzen"]["h2"], intro=o["referenzen"]["intro"],
            items=_reference_items(o["referenzen"]["slugs"]),
        ),
        C.founder_story(
            eyebrow="Persönliche Beratung vor Ort",
            h2=f"Beratung {ort_in}: erst hinschauen, dann rechnen",
            paragraphs=[
                (f"Eine Photovoltaikanlage oder eine Wärmepumpe plant man nicht am Telefon. Für die Erstberatung kommen "
                 f"wir zu Ihnen {ort_nach} und sehen uns Dach, Zählerschrank und Heizraum an. Danach wissen wir, was "
                 f"technisch passt und was der Netzanschluss hergibt."),
                ("Sie bekommen einen Projektbericht mit 3D-Belegplan und Statikreport und ein Fixangebot. Passt eine "
                 "kleinere Anlage besser oder ist die Wärmepumpe erst nach einer Sanierung sinnvoll, sagen wir Ihnen "
                 "das genauso offen. Ein fester Ansprechpartner begleitet Sie von der Planung bis zur Übergabe."),
            ],
            quote="Wir verkaufen keine Module, wir bauen Unabhängigkeit.",
            name=AUTHOR, role=AUTHOR_ROLE, badge="Fachbetrieb aus Villach",
            cta=("kontakt", f"Beratungstermin {ort_in}"),
        ),
        C.reviews_slider(reviews, rating=rating, count=count),
        C.steps_section(
            eyebrow="So läuft es ab",
            h2=f"Von der Beratung {ort_in} bis zur Übergabe",
            steps=[
                ("Beratung vor Ort", f"Wir besprechen Verbrauch, Dach und Heizung bei Ihnen {ort_in}. Kostenlos und unverbindlich.", ""),
                ("Projektbericht", "Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport sowie ein Fixangebot.", ""),
                ("Förderung, Gemeinde, Netz", f"Wir prüfen die Förderung, bereiten die Anträge vor und melden die Anlage bei {netz} an.", ""),
                ("Montage und Übergabe", "Zertifizierte Fachkräfte montieren, wir kümmern uns um Zählertausch, Inbetriebnahme und Einschulung.", ""),
            ],
        ),
        C.faq_section(o["faq"]),
        _quellen(o),
        C.linkgrid_section(
            f"Weiterlesen: Standorte {L['in']} und Ratgeber",
            [(k, f"Photovoltaik {n}") for k, n in nachbarn] + region_link + list(o.get("links", [])) + [
                ("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
                ("waermepumpe", "Wärmepumpe"),
                ("batteriespeicher", "Batteriespeicher"),
                (L["foerder_key"], L["foerder_label"]),
                ("foerderrechner", "Förderrechner"),
                ("finanzierung", "Finanzierung ab 147 € im Monat"),
                ("referenzen", "Alle Referenzen"),
                ("standorte", "Alle Standorte"),
            ],
        ),
        C.contact_section(
            headline=f"Ihr kostenloses Angebot für Photovoltaik und Wärmepumpe {ort_in}",
            sub=(f"Sie erreichen uns telefonisch oder über das Formular. Wir zeigen Ihnen ehrlich, was an Ihrem Haus "
                 f"{ort_in} möglich ist und was es kostet. Kostenlos und unverbindlich."),
            page_label=f"Standort {kurz}",
        ),
        C.finalcta(
            f"Bereit für eigenen Strom und saubere Wärme {ort_in}?",
            "Fordern Sie jetzt Ihre kostenlose Beratung an. Wir melden uns innerhalb eines Werktags und kommen zu Ihnen vor Ort.",
        ),
        f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte auf Basis typischer Projekte, vor Förderung. Preis, Ersparnis, Eigenverbrauch und
      Amortisation hängen von Verbrauch, Anlagengröße, Ausrichtung und Strompreis ab. Finanzierung: Beispielkonditionen,
      vorbehaltlich Bonitätsprüfung. Fördersätze Stand {STAND}, Änderungen durch Fördergeber und Netzbetreiber
      vorbehalten. Firmensitz von EBZ Energie ist Villach; {ort_in} beraten und montieren wir vor Ort.</p>
    </div>
  </section>""",
    ])
    crumbs = breadcrumb_jsonld([("Startseite", u("/")), ("Standorte", u("standorte")), (name, u(path))])
    html = page(o["title"], o["description"], path, body, faq_jsonld_str=faq_jsonld(u(path), o["faq"]),
                og_image=_img(o["hero_img"]), extra_jsonld=[crumbs, _service_jsonld(o, path)])
    return write_page(path.strip("/") + "/index.html", html)


def load(datei):
    spec = importlib.util.spec_from_file_location(f"standort_{datei}", os.path.join(CONTENT_DIR, datei + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    o = dict(mod.ORT)
    o.setdefault("datei", datei)
    return o


def build_one(datei):
    o = load(datei)
    errors = [f"{datei}: {e}" for e in check(o)]
    if errors:
        print(f"[{len(errors)}x!] standorte/{datei}")
        for e in errors:
            print(f"      ! {e}")
        return errors
    return render(o)


def build_hub():
    """Uebersicht /standorte/: alle gebauten Standortseiten nach Bundesland."""
    def tiles(land):
        return "".join(
            f'<a href="{href(k)}"><b>{n}</b><small>Photovoltaik und Wärmepumpe</small>'
            f'<span class="arr" aria-hidden="true">→</span></a>' for k, n in standorte(land))
    stmk_region = (f'<p class="landgrid-more eg-reveal">{a("pv_steiermark", "Überblick: Photovoltaik in der Steiermark →", cls="btn btn--ghost")}</p>'
                   if standort_exists("pv_steiermark") else "")
    faq = [
        ("Wo montiert EBZ Energie?",
         "Der Montageschwerpunkt liegt in Kärnten und der Steiermark. Firmensitz ist die Triglavstraße 15 in Villach; "
         "für die Erstberatung kommen wir zu Ihnen vor Ort. Referenzprojekte gibt es in sechs Bundesländern."),
        ("Mein Ort steht nicht in der Liste. Kommen Sie trotzdem?",
         "Ja. Die Liste zeigt Orte, für die es eine eigene Seite mit lokalen Angaben zu Netzbetreiber, Genehmigung und "
         "Förderung gibt. Wir beraten und montieren in ganz Kärnten und der Steiermark, andere Bundesländer prüfen wir "
         "auf Anfrage."),
        ("Gibt es Unterschiede zwischen Kärnten und der Steiermark?",
         "Ja, vor allem bei Förderung und Baurecht. Kärnten zahlt eine Landespauschale von 3.000 Euro für PV mit "
         "Speicher, die Steiermark hat keine PV-Pauschale und nimmt für neue Wärmepumpen derzeit keine Förderanträge "
         "an. Auch die Netzbetreiber unterscheiden sich je nach Ort. Die Details stehen auf den Ortsseiten."),
    ]
    body = "".join([
        C.page_hero(
            eyebrow="Standorte",
            h1="Photovoltaik und Wärmepumpe in Kärnten und der Steiermark: unsere Standorte",
            lead=("EBZ Energie ist ein Fachbetrieb aus Villach. Für jeden dieser Orte haben wir die lokalen Angaben "
                  "zusammengetragen: Netzbetreiber, Genehmigung, Förderung und Referenzen in der Nähe."),
            cta=("kontakt", "Kostenlose Beratung"), cta2=("foerderrechner", "Förderung berechnen"),
        ),
        f"""
  <section class="section section--tight">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Kärnten</p>
      <h2 class="center eg-reveal">Standorte in Kärnten</h2>
      <div class="landgrid eg-reveal" style="margin-top:30px">{tiles('ktn')}</div>
    </div>
  </section>
  <section class="section section--tight" style="background:#fff;border-block:1px solid var(--line)">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Steiermark</p>
      <h2 class="center eg-reveal">Standorte in der Steiermark</h2>
      <div class="landgrid eg-reveal" style="margin-top:30px">{tiles('stmk')}</div>
      {stmk_region}
    </div>
  </section>""",
        C.faq_section(faq),
        C.linkgrid_section("Weiterlesen", [
            ("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
            ("waermepumpe", "Wärmepumpe"),
            ("foerderungen", "Förderungen im Überblick"),
            ("referenzen", "Referenzen mit Zahlen"),
        ]),
        C.contact_section("Beratung bei Ihnen vor Ort",
                          "Sagen Sie uns, wo Ihr Haus steht. Wir melden uns innerhalb eines Werktags.",
                          page_label="Standorte"),
        C.finalcta("Ihr Ort, Ihr Dach, Ihre Heizung",
                   "Kostenlose Erstberatung in Kärnten und der Steiermark, mit Projektbericht und Förderprüfung."),
    ])
    path = S["standorte"]
    html = page("Standorte: Photovoltaik & Wärmepumpe | EBZ Energie",
                ("Alle Standorte von EBZ Energie in Kärnten und der Steiermark: Photovoltaik und Wärmepumpe mit lokalen "
                 "Angaben zu Netzbetreiber, Genehmigung und Förderung."),
                path, body, faq_jsonld_str=faq_jsonld(u(path), faq), og_image=IMG["hero_home"],
                extra_jsonld=[breadcrumb_jsonld([("Startseite", u("/")), ("Standorte", u(path))])])
    return write_page("standorte/index.html", html)


def build():
    errors = []
    for _key, _name, _land, src in STANDORTE:
        if src != "modul" and os.path.exists(os.path.join(CONTENT_DIR, src + ".py")):
            errors += build_one(src)
    errors += build_hub()
    return errors


if __name__ == "__main__":
    if len(sys.argv) > 1:
        sys.exit(1 if build_one(sys.argv[1]) else 0)
    import theme
    theme.write_assets()
    sys.exit(1 if build() else 0)
