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

# Bilder der alten WordPress-LPs (Oktober 2026 gesichert nach build/static/img/lp-*).
# Projektfotos ohne Zahlen und ohne Kundennamen; Grafiken mit nicht freigegebenen Aussagen
# (90 %, 70 % Heizkosten, 70 bis 90 % Eigenverbrauch) wurden beschnitten oder nicht uebernommen.
_I = "/assets/img/"
PHOTOS = {
    "ziegeldach-bergblick": ("Photovoltaikanlage auf einem Ziegeldach mit Bergen und Wald im Hintergrund", "Ziegeldach mit Bergblick"),
    "einfamilienhaus-walmdach": ("Einfamilienhaus mit Walmdach und Photovoltaikmodulen auf mehreren Dachseiten", "Walmdach, mehrere Dachseiten"),
    "montage-unterkonstruktion": ("Montage der Unterkonstruktion für eine Photovoltaikanlage auf einem Einfamilienhaus", "Montage der Unterkonstruktion"),
    "landwirtschaft": ("Landwirtschaftlicher Betrieb mit Photovoltaikanlage auf den Stalldächern", "Landwirtschaft, Stalldach"),
    "flachdach-aufgestaendert": ("Aufgeständerte Photovoltaikmodule auf einem Flachdach im Winter", "Flachdach, aufgeständert"),
    "blechdach-montage": ("Zertifizierte Fachkräfte montieren Photovoltaikmodule auf einem Blechdach", "Montage auf Blechdach"),
    "ziegeldach-tal": ("Photovoltaikanlage auf einem Ziegeldach eines Wohnhauses im Tal", "Wohnhaus, Ziegeldach"),
    "mehrparteienhaus": ("Photovoltaikanlage auf dem Dach eines Mehrparteienhauses aus der Vogelperspektive", "Mehrparteienhaus"),
    "schieferdach": ("Photovoltaikmodule auf einem dunklen Schieferdach", "Dunkles Schieferdach"),
    "satteldach-ziegel": ("Photovoltaikanlage auf einem Satteldach mit roten Ziegeln", "Satteldach mit Ziegeln"),
    "ziegeldach-dachfenster": ("Schwarze Photovoltaikmodule auf einem dunklen Ziegeldach mit Dachfenstern", "Dunkles Ziegeldach"),
    "module-ziegeldach": ("Nahaufnahme von Photovoltaikmodulen auf einem Ziegeldach mit Dachhaken", "Saubere Montage im Detail"),
    "holzfassade": ("Photovoltaikanlage auf einem Haus mit Holzfassade unter blauem Himmel", "Haus mit Holzfassade"),
    "ziegeldach-garten": ("Photovoltaikanlage auf einem Ziegeldach mit Blick in den Garten", "Ziegeldach mit Garten"),
    "flachdach-drei-ausrichtungen": ("Photovoltaikmodule in drei Ausrichtungen auf einem Flachdach", "Flachdach, drei Ausrichtungen"),
    "blechdach-bergblick": ("Photovoltaikanlage auf einem Blechdach mit Bergpanorama", "Blechdach mit Bergpanorama"),
    "zeltdach-fassade": ("Wohnhaus mit Photovoltaik auf dem Zeltdach und Fassadenmodulen am Balkon, Luftaufnahme", "Dach und Fassade"),
    "fassadenmodule": ("Photovoltaikmodule als Balkonverkleidung an der Fassade eines Wohnhauses", "Fassadenmodule am Balkon"),
    "ziegeldach-luftbild": ("Luftaufnahme einer Photovoltaikanlage auf einem Ziegeldach in zwei Ausrichtungen", "Ziegeldach, zwei Ausrichtungen"),
    "blechdach-luftbild": ("Luftaufnahme einer Photovoltaikanlage auf einem grauen Blechdach eines Wohnhauses", "Blechdach von oben"),
    "pultdach": ("Photovoltaikanlage auf einem dunklen Pultdach neben einer Dachterrasse", "Pultdach mit Terrasse"),
    "landwirtschaft-luftbild": ("Luftaufnahme eines Hofes mit Photovoltaikanlagen auf mehreren Dächern", "Hof mit mehreren Dächern"),
}
GALLERY_2023 = ["schieferdach", "ziegeldach-bergblick", "landwirtschaft", "flachdach-aufgestaendert", "blechdach-montage", "mehrparteienhaus"]
GALLERY_2024 = ["zeltdach-fassade", "flachdach-drei-ausrichtungen", "blechdach-bergblick", "ziegeldach-garten",
                "ziegeldach-luftbild", "blechdach-luftbild", "holzfassade", "module-ziegeldach",
                "fassadenmodule", "pultdach", "satteldach-ziegel", "ziegeldach-dachfenster"]
GALLERY_PV_SPEICHER = ["ziegeldach-bergblick", "einfamilienhaus-walmdach", "montage-unterkonstruktion", "landwirtschaft",
                       "flachdach-aufgestaendert", "blechdach-montage", "ziegeldach-tal", "mehrparteienhaus", "schieferdach"]
GRAFIK_PV = (_I + "lp-grafik-pv-speicher-wallbox.jpg",
             "Grafik: Photovoltaikanlage auf dem Dach, Stromspeicher im Haus und Wallbox für das Elektroauto", 1408, 560)
GRAFIK_WP_PV = (_I + "lp-grafik-waermepumpe-pv.jpg",
                "Grafik: Photovoltaik erzeugt Strom, der Speicher puffert ihn, die Wärmepumpe heizt Haus und Warmwasser", 1600, 893)
MARIO_FOTO = _I + "lp-mario-zintl.jpg"

# Welche LP welche Bilder bekommt (wie auf der alten Seite)
MEDIA = {
    "/photovoltaik-privat-lp/": {
        "hero_bg": _I + "lp-hero-alpenhaus.jpg",
        "problem_img": (_I + "lp-haus-pv-waermepumpe.jpg", "Modernes Einfamilienhaus mit Photovoltaik auf dem Dach und Wärmepumpe vor dem Haus"),
        "grafik": GRAFIK_PV,
        "mario_cta": True,
        "steps_bg": _I + "lp-bg-module-abendsonne.jpg",
        "finance_img": (_I + "lp-finanzierung-haus.jpg", "Geldscheine vor einem Einfamilienhaus mit Photovoltaikanlage"),
        "gallery": GALLERY_2023,
        "final_mario": True,
    },
    "/photovoltaik-gewerbe-lp/": {"gallery": GALLERY_2023[:5] + ["landwirtschaft-luftbild"], "mario": True},
    "/waermepumpeninstallation-oesterreich/": {"gallery": GALLERY_2023, "mario": True},
    "/waermepumpe-photovoltaik-oesterreich/": {"grafik": GRAFIK_WP_PV, "gallery": GALLERY_2023, "mario": True},
    "/heimkraftwerk-lp/": {"hero": (_I + "lp-heimkraftwerk.jpg", "Einfamilienhaus mit Photovoltaikanlage auf dem roten Ziegeldach"),
                           "gallery": GALLERY_2024},
    "/balkonkraftwerk-lp/": {"gallery": GALLERY_2024},
    "/photovoltaik-und-batteriespeicher/": {"gallery": GALLERY_PV_SPEICHER},
    "/ems-lp-2/": {"hero": (_I + "lp-ems-smartphone.jpg", "Frau steuert die Energie im Haus über eine App am Smartphone"), "mario": True},
}


def _grafik_section(grafik, h2):
    src, alt, w, h = grafik
    return f"""
  <section class="section--tight section">
    <div class="wrap">
      <h2 class="center eg-reveal" style="margin-bottom:24px">{h2}</h2>
      <figure class="eg-reveal" style="margin:0;border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow);background:#fff">
        <img src="{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy" style="display:block;width:100%;height:auto">
      </figure>
    </div>
  </section>"""


def _lp_hero(lp, bg, cta_label, rating):
    badges = "".join(f'<span class="hero__badge"><b>{b0}</b> {b1}</span>' for b0, b1 in lp["badges"])
    return f"""
  <section class="lp-hero" style="--bg:url('{bg}')">
    <div class="lp-hero__inner">
      <div class="lp-hero__copy">
        <p class="eyebrow">{lp['eyebrow']}</p>
        <h1>{lp['h1']}</h1>
        <p class="lead">{lp['lead']}</p>
        <div class="hero__badges">{badges}</div>
        <div class="hero__cta">
          <a class="btn btn--primary btn--lg" href="#beratung">{cta_label}</a>
          <a class="btn btn--light btn--lg" href="tel:+436502202626">☎ +43 650 220 26 26</a>
        </div>
        <div class="lp-hero__rating"><span class="stars" aria-hidden="true">★★★★★</span><b>{rating}</b><span>Sterne auf Google</span></div>
      </div>
    </div>
  </section>"""


def _finance_media(img, alt):
    return C.media_text(
        "Faire Finanzierung", "Ihre Anlage gehört Ihnen ab dem ersten Tag",
        ["Sie finanzieren Ihre Photovoltaikanlage in monatlichen Raten und sind trotzdem von Beginn an Eigentümer. "
         "Komplettanlage inklusive Speicher <b>ab 147 € im Monat</b>.*"],
        img, alt,
        bullets=["0 € Anzahlung", "Fixe Rate über die gesamte Laufzeit", "Volle Förderung für Privatpersonen",
                 "Kein Grundbucheintrag"],
        cta=("#beratung", "Finanzierung anfragen"))


def _final_mario(fc, cta_label):
    """Schluss-Aufruf vor dem Formular: dunkles Band, Text links, Mario im Hochformat rechts."""
    paras = "".join(f"<p>{x}</p>" for x in [fc["text"]] + fc.get("more", []))
    return f"""
  <section class="section lp-final">
    <div class="wrap">
      <div class="lp-final__grid">
        <div class="lp-final__copy eg-reveal">
          <p class="eyebrow">{fc.get('eyebrow', 'Jetzt starten')}</p>
          <h2>{fc['h2']}</h2>
          {paras}
          <div class="hero__cta">
            <a class="btn btn--primary btn--lg" href="#beratung">{cta_label}</a>
            <a class="btn btn--ghost btn--lg" href="tel:+436502202626">☎ +43 650 220 26 26</a>
          </div>
        </div>
        <figure class="lp-final__photo eg-reveal">
          <img src="{MARIO_FOTO}" alt="Mario Zintl, Geschäftsführung EBZ Energie GmbH" width="600" height="900" loading="lazy">
          <figcaption><b>Mario Zintl</b><span>Geschäftsführung EBZ Energie GmbH</span></figcaption>
        </figure>
      </div>
    </div>
  </section>"""


def _mario_cta(cta_label):
    return (f'<div class="lp-cta-row eg-reveal"><a class="btn btn--primary btn--lg" href="#beratung">{cta_label}</a>'
            f'<a class="btn btn--ghost btn--lg" href="tel:+436502202626">☎ +43 650 220 26 26</a></div>')


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
    media = MEDIA.get(lp["path"], {})
    hero_src, hero_alt = media.get("hero", (IMG[lp["hero_img"]], lp["hero_alt"]))
    parts = [
        _lp_hero(lp, media["hero_bg"], cta_label, rating) if media.get("hero_bg") else C.hero(
            eyebrow=lp["eyebrow"], h1=lp["h1"], lead=lp["lead"], badges=lp["badges"],
            img=hero_src, img_alt=hero_alt,
            float_num=lp.get("float", ("4,9", "Sterne auf Google"))[0],
            float_label=lp.get("float", ("4,9", "Sterne auf Google"))[1],
            cta_primary=("#beratung", cta_label),
            cta_secondary=("tel:+436502202626", "☎ +43 650 220 26 26"),
        ),
        C.reviews_slider(reviews, rating=rating, count=count),
    ]
    if lp.get("problem"):
        pr = lp["problem"]
        if media.get("problem_img"):
            paras = list(pr["paragraphs"]) + ([f"<b>{pr['bullets_intro']}</b>"] if pr.get("bullets_intro") else [])
            parts.append(C.media_text(pr["eyebrow"], pr["h2"], paras, media["problem_img"][0], media["problem_img"][1],
                                      bullets=pr.get("bullets")))
        else:
            parts.append(C.text_block(pr["eyebrow"], pr["h2"], pr["paragraphs"]))
    sysblock = lp.get("system")
    if sysblock and media.get("grafik"):
        src, alt, w, h = media["grafik"]
        parts.append(C.media_text(sysblock["eyebrow"], sysblock["h2"], sysblock["paragraphs"], src, alt,
                                  reverse=True).replace('<img src="' + src, '<img class="is-grafik" src="' + src, 1))
    b = lp["benefits"]
    parts.append(C.cards_section(b["eyebrow"], b["h2"], b["intro"],
                                 [{"ic": ic, "title": t, "text": x} for ic, t, x in b["cards"]]))
    if media.get("grafik") and not sysblock:
        parts.append(_grafik_section(media["grafik"], lp.get("grafik_h2", "So arbeitet Ihr Energiesystem zusammen")))
    if lp.get("quote"):
        parts.append(C.founder_block(lp["quote"], img=MARIO_FOTO if media.get("mario") else None))
        if media.get("mario_cta"):
            parts.append(_mario_cta(cta_label))
    st = lp["steps"]
    steps_html = C.steps_section(st["eyebrow"], st["h2"], st["steps"])
    if media.get("steps_bg"):
        steps_html = steps_html.replace('<section class="section" style="background:#fff;border-block:1px solid var(--line)">',
                                        f'<section class="section lp-photo-bg" style="--bg:url(\'{media["steps_bg"]}\')">', 1)
    parts.append(steps_html)
    w = lp.get("why", {})
    parts.append(C.why_section(w.get("eyebrow", "Warum EBZ Energie"),
                               w.get("h2", "Warum Kundinnen und Kunden sich für EBZ entscheiden"),
                               w.get("items", WHY_DEFAULT)))
    if lp.get("finance"):
        parts.append(_finance_media(*media["finance_img"]) if media.get("finance_img") else C.finance_band())
    if lp.get("refs"):
        parts.append(C.reference_cards(
            "Aus der Praxis", lp.get("refs_h2", "Echte Projekte, echte Zahlen"),
            "Bild und Zahlen gehören jeweils zum selben Projekt.",
            [REFS[k] for k in lp["refs"]]))
    if media.get("gallery"):
        parts.append(C.gallery(
            "Unsere Anlagen", lp.get("gallery_h2", "Echte Projekte aus der Region"),
            "Fotos von Anlagen, die EBZ Energie geplant und umgesetzt hat.",
            [(_I + "lp-ref-" + k + ".jpg", PHOTOS[k][0], PHOTOS[k][1]) for k in media["gallery"]]))
    fc = lp.get("finalcta")
    if fc and media.get("final_mario"):
        # wie auf der alten LP: Schluss-Aufruf mit Mario-Foto direkt vor dem Formular
        parts.append(_final_mario(fc, cta_label))
    c = lp["contact"]
    parts.append(C.contact_section(c["h2"], c["sub"], page_label=f"LP {lp['_name']}"))
    if lp.get("faq"):
        parts.append(C.faq_section(lp["faq"]))
    if fc and not media.get("final_mario"):
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
