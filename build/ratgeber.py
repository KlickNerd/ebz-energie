"""Baut alle Ratgeber aus build/content/ratgeber/*.py plus die Uebersicht /ratgeber/.

Jede Content-Datei stellt ein Dict ``ARTICLE`` bereit (Struktur: siehe article.py).
Aufruf einzeln:  python3 build/ratgeber.py
"""

import os
import sys
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import article
from common import IMG, faq_jsonld, u, write_page
from layout import page
import components as C

CONTENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content", "ratgeber")

# Cluster-Zuordnung ueber Slug-Muster (Reihenfolge = Reihenfolge auf der Hub-Seite)
CLUSTERS = [
    ("Förderungen", ("foerderung", "sanierungsoffensive", "sauber-heizen", "steuerlich", "landesfoerderungen")),
    ("Wärmepumpe und Heizen", ("waermepumpe", "heizen")),
    ("Speicher und Notstrom", ("speicher", "notstrom", "marstek")),
    ("Energiegemeinschaft", ("energiegemeinschaft", "oemag")),
    ("Smart Meter und Stromtarife", ("smart-meter", "stromtarif", "elwg", "marktpreis", "einspeise")),
    ("Photovoltaik", ()),  # Rest
]


def cluster_of(slug):
    for name, keys in CLUSTERS:
        if any(k in slug for k in keys):
            return name
    return CLUSTERS[-1][0]


def load_articles():
    arts = []
    for name in sorted(os.listdir(CONTENT_DIR)):
        if not name.endswith(".py") or name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(name[:-3], os.path.join(CONTENT_DIR, name))
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
            arts.append(mod.ARTICLE)
        except Exception as exc:  # halbfertige Datei blockiert nicht den ganzen Build
            print(f"[ERR] content/ratgeber/{name}: {type(exc).__name__}: {exc}")
    return arts


CLUSTER_INTRO = {
    "Förderungen": "Bund, alle neun Bundesländer, Speicher, Wärmepumpe und Energiemanagement: Beträge, Fristen und die richtige Reihenfolge der Anträge.",
    "Wärmepumpe und Heizen": "Kosten, Funktionsweise, Altbau-Eignung und die Kombination mit Photovoltaik.",
    "Speicher und Notstrom": "Nachrüsten, Wirtschaftlichkeit, Notstrom bei Stromausfall und Balkonkraftwerke.",
    "Energiegemeinschaft": "Strom mit Nachbarn teilen: Beitritt, Kosten, Netzentgelt-Rabatt und die Lage in Kärnten und der Steiermark.",
    "Smart Meter und Stromtarife": "Digitaler Zähler, dynamische Tarife, ElWG und der aktuelle OeMAG-Marktpreis.",
    "Photovoltaik": "Grundlagen, Kosten, Komplettanlagen und Finanzierungsmodelle.",
}
CLUSTER_ANCHOR = {
    "Förderungen": "foerderungen", "Wärmepumpe und Heizen": "waermepumpe",
    "Speicher und Notstrom": "speicher", "Energiegemeinschaft": "energiegemeinschaft",
    "Smart Meter und Stromtarife": "smart-meter", "Photovoltaik": "photovoltaik",
}
# Einstieg: die vier meistgesuchten Themen (handverlesen)
FEATURED = ["kosten-einer-solaranlage", "photovoltaik-foerderung-oesterreich-2026",
            "energiegemeinschaft", "kosten-einer-waermepumpe"]


def _card(art, cluster, big=False):
    img = IMG.get(art.get("hero_img"), art.get("hero_img")) if art.get("hero_img") else IMG["pv_card"]
    title = art["h1"] if len(art["h1"]) <= 72 else art["title"].split("|")[0].strip()
    prose = "".join(h for _h2, _id, h in art["sections"])
    minutes = article.reading_minutes(art["lead"] + prose)
    y, m, _d = art["date_modified"].split("-")
    return f"""
        <a class="rg-card" href="{art['path']}">
          <div class="rg-card__media"><img src="{img}" alt="{art.get('hero_alt', title)}" loading="lazy" width="480" height="270"></div>
          <div class="rg-card__body">
            <span class="rg-card__tag">{cluster}</span>
            <h3>{title}</h3>
            <p>{art['description']}</p>
            <div class="rg-card__meta"><span><b>{minutes} Min.</b> Lesezeit</span><span>Stand {m}/{y}</span></div>
          </div>
        </a>"""


def build_hub(arts):
    """Uebersichtsseite /ratgeber/: Suche, Cluster-Navigation, Einstiegs-Themen, Cluster-Sektionen."""
    groups = {}
    by_slug = {}
    for art in arts:
        cl = art.get("cluster") or cluster_of(art["slug"])
        groups.setdefault(cl, []).append(art)
        by_slug[art["slug"]] = (art, cl)

    nav = "".join(
        f'<li><a href="#{CLUSTER_ANCHOR[name]}">{name} <b>{len(groups[name])}</b></a></li>'
        for name, _k in CLUSTERS if groups.get(name)
    )
    featured = "".join(_card(*by_slug[s], big=True) for s in FEATURED if s in by_slug)

    sections = ""
    for name, _keys in CLUSTERS:
        items = groups.get(name)
        if not items:
            continue
        items = sorted(items, key=lambda x: (x["date_modified"], x["h1"]), reverse=True)
        cards = "".join(_card(art, name) for art in items)
        sections += f"""
  <section class="rg-section" id="{CLUSTER_ANCHOR[name]}">
    <div class="wrap">
      <div class="rg-head eg-reveal">
        <div><h2>{name}</h2><p>{CLUSTER_INTRO.get(name, "")}</p></div>
        <span class="rg-count">{len(items)} Ratgeber</span>
      </div>
      <div class="rg-grid">{cards}</div>
    </div>
  </section>"""

    total = len(arts)
    body = f"""
  <section class="rg-hero">
    <div class="wrap">
      <p class="eyebrow">Wissen aus der Praxis</p>
      <h1>Ratgeber: Photovoltaik, Speicher, Wärmepumpe und Förderungen</h1>
      <p class="lead">{total} Ratgeber mit konkreten Zahlen, Fristen und Rechenbeispielen aus über 300 Projekten.
      Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
      <div class="rg-search"><span class="ic" aria-hidden="true">⌕</span>
        <label for="rg-q" class="visually-hidden" style="position:absolute;left:-9999px">Ratgeber durchsuchen</label>
        <input id="rg-q" type="search" placeholder="Thema suchen, z. B. Förderung Kärnten, Notstrom, Smart Meter" autocomplete="off"></div>
      <ul class="rg-nav">{nav}</ul>
    </div>
  </section>
  <div class="rg-root">
  <section class="rg-featured">
    <div class="wrap"><div class="rg-grid">{featured}</div></div>
  </section>
  {sections}
  <p class="rg-empty wrap">Kein Ratgeber zu diesem Begriff. Rufen Sie uns an, wir beantworten die Frage direkt.</p>
  </div>
""" + C.finalcta(
        "Lieber direkt fragen?",
        "Ein Anruf klärt oft mehr als zehn Artikel. Wir beraten kostenlos und sagen ehrlich, was sich bei Ihnen rechnet.",
    )
    html = page(
        "Ratgeber: Photovoltaik, Speicher, Wärmepumpe, Förderung | EBZ Energie",
        f"{total} Ratgeber von EBZ Energie aus Villach: Photovoltaik-Kosten, Speicher, Wärmepumpe, "
        "Förderungen in allen Bundesländern, Energiegemeinschaft und Smart Meter. Mit Zahlen, Fristen und Beispielen.",
        "/ratgeber/", body,
    )
    return write_page("ratgeber/index.html", html)


def build():
    errors = []
    arts = load_articles()
    for art in arts:
        try:
            errors += article.render(art)
        except Exception as exc:
            print(f"[ERR] {art.get('slug')}: {type(exc).__name__}: {exc}")
            errors.append(str(exc))
    errors += build_hub(arts)
    return errors


if __name__ == "__main__":
    import theme
    theme.write_assets()
    errs = build()
    if errs:
        sys.exit(1)
