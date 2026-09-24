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


def build_hub(arts):
    """Uebersichtsseite /ratgeber/: Cluster-Sektionen mit Karten (neueste zuerst)."""
    groups = {}
    for art in arts:
        groups.setdefault(art.get("cluster") or cluster_of(art["slug"]), []).append(art)
    sections = ""
    for name, _keys in CLUSTERS:
        items = sorted(groups.get(name, []), key=lambda x: x["date_modified"], reverse=True)
        if not items:
            continue
        cards = []
        for art in items:
            img = IMG.get(art.get("hero_img"), art.get("hero_img")) if art.get("hero_img") else IMG["pv_card"]
            cards.append({
                "img": img, "alt": art.get("hero_alt", art["h1"]),
                "title": art["h1"] if len(art["h1"]) <= 70 else art["title"].split("|")[0].strip(),
                "text": art["description"],
                "link_key": art["path"], "link_text": "Ratgeber lesen",
            })
        sections += C.cards_section("Ratgeber", name, "", cards, with_media=True)

    total = len(arts)
    body = C.page_hero(
        eyebrow="Wissen aus der Praxis",
        h1="Ratgeber: Photovoltaik, Speicher, Wärmepumpe und Förderungen",
        lead=(f"{total} Ratgeber mit konkreten Zahlen, Fristen und Beispielen aus über 300 Projekten. "
              "Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH."),
        cta=("kontakt", "Kostenlose Beratung"),
    ) + sections + C.finalcta(
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
