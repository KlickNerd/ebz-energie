"""Ads-Landingpages unter den alten WordPress-Adressen (z. B. /photovoltaik-privat-lp/).

Jede LP ist eine Content-Datei build/content/landingpages/<name>.py mit einem Dict LP.
Gemeinsamer Aufbau: Hero mit Formular-Sprung, Bewertungen, Problem, Nutzen, Mario-Zitat, Ablauf,
Warum EBZ, optional Finanzierung, Referenzen, Anfrageformular, FAQ, Schluss-CTA.
Alle LPs sind noindex (layout.page(landing=True)) und stehen nicht in der Sitemap; SEO machen die
Leistungsseiten. Das Formular sendet die Quelle "LP <name>" mit, damit Anfragen zuordenbar sind.
"""

import glob
import importlib.util
import os

from common import IMG, write_page, load_reviews, a
from layout import page
import components as C

CONTENT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content", "landingpages")

# Freigegebene Referenzen (Bild und Zahlen gehoeren zum selben Projekt, CLAUDE.md)
REFS = {
    "villach": {"img": IMG["ref_villach"], "alt": "Photovoltaikanlage auf einem Einfamilienhaus in Villach",
                "title": "Einfamilienhaus, Villach", "specs": "10 kWp Ost-West mit Notstrom, rund 11.000 kWh im Jahr.",
                "result": "rund 80 %", "result_sub": "weniger Stromkosten"},
    "krumpendorf": {"img": IMG["ref_krumpendorf"], "alt": "Photovoltaikanlage auf einem Mehrparteienhaus in Krumpendorf",
                    "title": "Mehrparteienhaus, Krumpendorf", "specs": "25 kWp mit 25 kWh Speicher und Notstrom, Montage in 4 Tagen.",
                    "result": "4 Tage", "result_sub": "Bauzeit"},
    "gewerbe": {"img": IMG["gewerbe_dach"], "alt": "Große Photovoltaikanlage auf einem Gewerbedach in Oberösterreich",
                "title": "Gewerbe, Oberösterreich", "specs": "40 kWp Ost-West auf Trapezblech, 40 kWh Speicher, rund 40.000 kWh im Jahr.",
                "result": "13.500 €", "result_sub": "Ersparnis pro Jahr"},
}

WHY_DEFAULT = [
    ("☀", "Alles aus einer Hand", "Planung, Montage, Förderabwicklung, Netzanmeldung und Service. Ein Ansprechpartner von der Planung bis zur Übergabe."),
    ("✓", "Zertifizierte Fachkräfte", "Meisterhaftes Handwerk und sorgfältige Ausführung nach österreichischen Normen."),
    ("★", "4,9 Sterne auf Google", "Bewertungen von echten Kundinnen und Kunden aus der Region."),
    ("◉", "300+ Projekte", "Erfahrung aus über 300 dokumentierten Projekten in 6 Bundesländern."),
    ("◇", "Bis zu 30 Jahre Garantie", "Bis zu 30 Jahre Leistungsgarantie auf die Module, mindestens 10 Jahre Produktgarantie."),
    ("⌂", "Regional verwurzelt", "Zuhause in Villach, im Einsatz in Kärnten und der Steiermark."),
]


def load_lps():
    lps = []
    for path in sorted(glob.glob(os.path.join(CONTENT_DIR, "*.py"))):
        name = os.path.splitext(os.path.basename(path))[0]
        if name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f"lp_{name}", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        lp = dict(mod.LP)
        lp["_name"] = name
        lps.append(lp)
    return lps


def render(lp):
    rating, count, reviews = load_reviews()
    cta_label = lp.get("cta", "Kostenloses Angebot anfordern")
    parts = [
        C.hero(
            eyebrow=lp["eyebrow"], h1=lp["h1"], lead=lp["lead"], badges=lp["badges"],
            img=IMG[lp["hero_img"]], img_alt=lp["hero_alt"],
            float_num=lp.get("float", ("4,9", "Sterne auf Google"))[0],
            float_label=lp.get("float", ("4,9", "Sterne auf Google"))[1],
            cta_primary=("#beratung", cta_label),
            cta_secondary=("tel:+436502202626", "☎ +43 650 220 26 26"),
        ),
        C.reviews_slider(reviews, rating=rating, count=count),
    ]
    if lp.get("problem"):
        pr = lp["problem"]
        parts.append(C.text_block(pr["eyebrow"], pr["h2"], pr["paragraphs"]))
    b = lp["benefits"]
    parts.append(C.cards_section(b["eyebrow"], b["h2"], b["intro"],
                                 [{"ic": ic, "title": t, "text": x} for ic, t, x in b["cards"]]))
    if lp.get("quote"):
        parts.append(C.founder_block(lp["quote"]))
    st = lp["steps"]
    parts.append(C.steps_section(st["eyebrow"], st["h2"], st["steps"]))
    w = lp.get("why", {})
    parts.append(C.why_section(w.get("eyebrow", "Warum EBZ Energie"),
                               w.get("h2", "Warum Kundinnen und Kunden sich für EBZ entscheiden"),
                               w.get("items", WHY_DEFAULT)))
    if lp.get("finance"):
        parts.append(C.finance_band())
    if lp.get("refs"):
        parts.append(C.reference_cards(
            "Aus der Praxis", lp.get("refs_h2", "Echte Projekte, echte Zahlen"),
            "Bild und Zahlen gehören jeweils zum selben Projekt.",
            [REFS[k] for k in lp["refs"]]))
    c = lp["contact"]
    parts.append(C.contact_section(c["h2"], c["sub"], page_label=f"LP {lp['_name']}"))
    if lp.get("faq"):
        parts.append(C.faq_section(lp["faq"]))
    fc = lp.get("finalcta")
    if fc:
        parts.append(C.finalcta(fc["h2"], fc["text"], cta=("#beratung", cta_label)))
    if lp.get("footnote"):
        parts.append(f'\n  <section class="section--tight section"><div class="wrap"><p class="form-note">{lp["footnote"]}</p></div></section>')
    return page(lp["title"], lp["description"], lp["path"], "".join(parts), landing=True)


def build():
    errors = []
    for lp in load_lps():
        html = render(lp)
        errors += write_page(lp["path"].strip("/") + "/index.html", html)
    return errors


if __name__ == "__main__":
    import sys
    sys.exit(1 if build() else 0)
