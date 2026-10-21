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
    "/ems-lp-2/": {"hero": (_I + "lp-ems-smartphone.jpg", "Frau steuert die Energie im Haus über eine App am Smartphone"),
                   "mario_cta": True},
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


def _finance_media(img, alt, fin=None):
    """fin (optional, dict): eigener Text ohne Privat-Rate, z. B. fuer Gewerbe-LPs (eyebrow, h2, paragraphs, bullets, cta)."""
    if isinstance(fin, dict):
        return C.media_text(fin.get("eyebrow", "Faire Finanzierung"), fin["h2"], fin["paragraphs"], img, alt,
                            bullets=fin.get("bullets"), cta=("#beratung", fin.get("cta", "Finanzierung anfragen")))
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


DEFAULT_ORDER = ["hero", "kpis", "reviews", "hub", "problem", "system", "benefits", "grafik", "split", "quote",
                 "steps", "why", "finance", "refs", "gallery", "final", "contact", "faq", "finalcta", "footnote"]


_PAGES_DIR = os.path.dirname(os.path.abspath(__file__))


def _page_module(name):
    spec = importlib.util.spec_from_file_location(f"lp_src_{name}", os.path.join(_PAGES_DIR, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def render_from_page(lp):
    """LP mit dem Inhalt einer bestehenden Leistungsseite (die alte LP war dieselbe Seite), im LP-Modus:
    Ratgeber-Linkliste raus, Kontakt-Buttons springen zum Formular, Rechner nach dem Ablauf wie auf der alten LP."""
    import re
    body = _page_module(lp["source"]).body()
    # Link-Kacheln (Weiterlesen/Ratgeber) fuehren von der LP weg
    body = re.sub(r'\n  <section class="section--tight section">\s*<div class="wrap">\s*<h2[^>]*>[^<]*</h2>\s*<div class="linkgrid">.*?</section>',
                  "", body, count=1, flags=re.S)
    body = body.replace('href="/kontakt/"', 'href="#beratung"')
    body = re.sub(r'(<input type="hidden" name="quelle" value=")[^"]*(")', r"\g<1>Ads-LP " + lp["path"] + r"\g<2>", body)
    if lp.get("rechner"):
        rech = _page_module("rechner")
        calc = rech._calc_section(lp["rechner"], lp.get("rechner_intro", ""), rech.EG_FORM, rech.EG_RESULT,
                                  rech.EG_ASSUMPTIONS, rech.EG_JS)
        i = body.find('<div class="steps"')
        j = body.find("</section>", i) + len("</section>")
        body = body[:j] + calc + body[j:]
        # Rechner-Button bleibt auf der LP: Ergebnis ins Anliegen-Feld, dann zum Formular scrollen
        body += """
  <script>
  document.addEventListener("click", function(e){
    var c = e.target.closest("#e-cta, #s-cta"), f = document.getElementById("beratung");
    if(!c || !f) return;
    e.preventDefault();
    var v = new URLSearchParams((c.getAttribute("href").split("?")[1] || "")).get("anliegen");
    var m = f.querySelector("[name=msg]");
    if(v && m) m.value = v + "\\n\\n";
    f.scrollIntoView({behavior: "smooth"});
  });
  </script>"""
    return page(lp["title"], lp["description"], lp["path"], body, landing=True)


def render(lp):
    if lp.get("source"):
        return render_from_page(lp)
    rating, count, reviews = load_reviews()
    cta_label = lp.get("cta", "Kostenloses Angebot anfordern")
    media = dict(MEDIA.get(lp["path"], {}))
    for k, v in lp.get("media", {}).items():  # Bilder koennen auch direkt in der Content-Datei stehen
        media[k] = globals()[v] if isinstance(v, str) and v.isupper() and v in globals() else v
    hero_src, hero_alt = media.get("hero", (IMG[lp["hero_img"]], lp["hero_alt"]))
    fc = lp.get("finalcta")
    sysblock = lp.get("system")

    def s_hero():
        if media.get("hero_bg"):
            return _lp_hero(lp, media["hero_bg"], cta_label, rating)
        return C.hero(
            eyebrow=lp["eyebrow"], h1=lp["h1"], lead=lp["lead"], badges=lp["badges"],
            img=hero_src, img_alt=hero_alt,
            float_num=lp.get("float", ("4,9", "Sterne auf Google"))[0],
            float_label=lp.get("float", ("4,9", "Sterne auf Google"))[1],
            cta_primary=("#beratung", cta_label),
            cta_secondary=("tel:+436502202626", "☎ +43 650 220 26 26"))

    def s_kpis():
        return C.kpis(lp["kpis"]) if lp.get("kpis") else ""

    def s_reviews():
        return C.reviews_slider(reviews, rating=rating, count=count)

    def s_hub():
        h = lp.get("hub")
        return C.hub_section(h["eyebrow"], h["h2"], h["lead"], h["points"]) if h else ""

    def s_problem():
        pr = lp.get("problem")
        if not pr:
            return ""
        if pr.get("bars"):
            return C.problem_compare(pr["eyebrow"], pr["h2"], pr["intro"], pr["bars"], pr.get("aside"))
        if media.get("problem_img"):
            paras = list(pr["paragraphs"]) + ([f"<b>{pr['bullets_intro']}</b>"] if pr.get("bullets_intro") else [])
            return C.media_text(pr["eyebrow"], pr["h2"], paras, media["problem_img"][0], media["problem_img"][1],
                                bullets=pr.get("bullets"))
        return C.text_block(pr["eyebrow"], pr["h2"], pr["paragraphs"])

    def s_system():
        if not (sysblock and media.get("grafik")):
            return ""
        src, alt, w, h = media["grafik"]
        return C.media_text(sysblock["eyebrow"], sysblock["h2"], sysblock["paragraphs"], src, alt,
                            reverse=True).replace('<img src="' + src, '<img class="is-grafik" src="' + src, 1)

    def s_benefits():
        b = lp["benefits"]
        return C.cards_section(b["eyebrow"], b["h2"], b["intro"],
                               [{"ic": ic, "title": t, "text": x} for ic, t, x in b["cards"]])

    def s_grafik():
        if media.get("grafik") and not sysblock:
            return _grafik_section(media["grafik"], lp.get("grafik_h2", "So arbeitet Ihr Energiesystem zusammen"))
        return ""

    def s_split():
        sp = lp.get("split")
        if not sp:
            return ""
        left, right = dict(sp["left"]), dict(sp["right"])
        for side in (left, right):
            side["img"] = IMG[side.pop("img_key")]
        return C.audience_split(sp["eyebrow"], sp["h2"], sp["intro"], left, right)

    def s_quote():
        if not lp.get("quote"):
            return ""
        html = C.founder_block(lp["quote"], img=MARIO_FOTO if media.get("mario") else None)
        return html + (_mario_cta(cta_label) if media.get("mario_cta") else "")

    def s_steps():
        st = lp["steps"]
        html = C.steps_section(st["eyebrow"], st["h2"], st["steps"])
        if media.get("steps_bg"):
            html = html.replace('<section class="section" style="background:#fff;border-block:1px solid var(--line)">',
                                f'<section class="section lp-photo-bg" style="--bg:url(\'{media["steps_bg"]}\')">', 1)
        return html

    def s_why():
        w = lp.get("why", {})
        return C.why_section(w.get("eyebrow", "Warum EBZ Energie"),
                             w.get("h2", "Warum Kundinnen und Kunden sich für EBZ entscheiden"),
                             w.get("items", WHY_DEFAULT))

    def s_finance():
        if not lp.get("finance"):
            return ""
        return _finance_media(*media["finance_img"], fin=lp["finance"]) if media.get("finance_img") else C.finance_band()

    def s_refs():
        if not lp.get("refs"):
            return ""
        return C.reference_cards("Aus der Praxis", lp.get("refs_h2", "Echte Projekte, echte Zahlen"),
                                 "Bild und Zahlen gehören jeweils zum selben Projekt.", [REFS[k] for k in lp["refs"]])

    def s_gallery():
        if not media.get("gallery"):
            return ""
        return C.gallery("Unsere Anlagen", lp.get("gallery_h2", "Echte Projekte aus der Region"),
                         "Fotos von Anlagen, die EBZ Energie geplant und umgesetzt hat.",
                         [(_I + "lp-ref-" + k + ".jpg", PHOTOS[k][0], PHOTOS[k][1]) for k in media["gallery"]])

    def s_final():
        # wie auf der alten LP: Schluss-Aufruf mit Mario-Foto direkt vor dem Formular
        return _final_mario(fc, cta_label) if (fc and media.get("final_mario")) else ""

    def s_contact():
        c = lp["contact"]
        return C.contact_section(c["h2"], c["sub"], page_label="Ads-LP " + lp["path"])

    def s_faq():
        return C.faq_section(lp["faq"]) if lp.get("faq") else ""

    def s_finalcta():
        if fc and not media.get("final_mario"):
            return C.finalcta(fc["h2"], fc["text"], cta=("#beratung", cta_label))
        return ""

    def s_footnote():
        if not lp.get("footnote"):
            return ""
        return f'\n  <section class="section--tight section"><div class="wrap"><p class="form-note">{lp["footnote"]}</p></div></section>'

    sections = {name[2:]: fn for name, fn in locals().items() if name.startswith("s_")}
    parts = [sections[key]() for key in lp.get("order", DEFAULT_ORDER)]
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
