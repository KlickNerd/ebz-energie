"""Ratgeber-Vorlage: Komponenten + Renderer fuer Artikel.

Ein Artikel ist ein Dict ``ARTICLE`` in build/content/ratgeber/<slug>.py mit:
  slug, path, title, description, eyebrow, h1, lead, chips, date_published,
  date_modified, hero_img, hero_alt, tldr, kpis, sections [(h2, id, html)],
  faq [(frage, antwort_html)], sources [(label, url)], related [(key, text)],
  cta (dict h3/text/primary/secondary), partner (dict h2/text/grid), crumbs [(name, key)]

Die Bausteine (tldr, kpis, box, table, steps, net, cta, partner, faq ...)
werden in den Content-Dateien als Helfer genutzt, damit der Inhalt sauber
und ohne handgeschriebenes Layout-HTML bleibt.
"""

import re
import html as _html

from common import (NAP, IMG, AUTHOR, AUTHOR_ROLE, S, u, href, a, tel_link,
                    faq_jsonld, article_jsonld, breadcrumb_jsonld, write_page)
from layout import page
import components as C


# --- Bausteine (im Fliesstext) ---------------------------------------------

def tldr(items, title="Auf den Punkt"):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<aside class="art-tldr"><h2>{title}</h2><ul>{lis}</ul></aside>'


def kpis(items):
    """items: Liste aus (wert, label)."""
    cells = "".join(f'<div class="art-kpi"><b>{v}</b><span>{l}</span></div>' for v, l in items)
    return f'<div class="art-kpis">{cells}</div>'


def box(text, label="Wichtig:"):
    return f'<div class="art-box"><b>{label}</b> {text}</div>'


def box_dark(h3, text):
    return f'<div class="art-box art-box--p"><h3>{h3}</h3><p>{text}</p></div>'


def table(head, rows, hl_cols=()):
    """head: Liste Spaltentitel. rows: Liste aus Zeilen (Liste Zellen). hl_cols: Indizes hervorheben."""
    th = "".join(f"<th>{h}</th>" for h in head)
    trs = "".join(
        "<tr>" + "".join(
            f'<td class="hl">{c}</td>' if i in hl_cols else f"<td>{c}</td>"
            for i, c in enumerate(r)
        ) + "</tr>"
        for r in rows
    )
    return (f'<div class="art-tablewrap"><table class="art-table"><thead><tr>{th}</tr></thead>'
            f'<tbody>{trs}</tbody></table></div>')


def steps(items):
    """items: Liste aus (titel, text)."""
    lis = "".join(f"<li><b>{t}</b>{x}</li>" for t, x in items)
    return f'<ol class="art-steps">{lis}</ol>'


def net(items, hub_title, hub_text, hub_icon="◎"):
    """Vernetzungs-Infografik: 4 Komponenten + zentrale Schaltzentrale.
    items: Liste aus (icon, titel, text)."""
    tiles = "".join(
        f'<div><span class="ic" aria-hidden="true">{ic}</span><div><b>{t}</b><span>{x}</span></div></div>'
        for ic, t, x in items
    )
    hub = (f'<div class="art-net__hub"><span class="ic" aria-hidden="true">{hub_icon}</span>'
           f'<div><b>{hub_title}</b><span>{hub_text}</span></div></div>')
    return f'<div class="art-net" role="group" aria-label="{_html.escape(hub_title)}">{tiles}{hub}</div>'


def cta(h3, text, primary=("kontakt", "Kostenlose Beratung anfragen"), secondary=None):
    btns = a(primary[0], primary[1], cls="btn btn--primary")
    if secondary:
        btns += a(secondary[0], secondary[1], cls="btn btn--light")
    return f'<div class="art-cta"><h3>{h3}</h3><p>{text}</p><div class="art-btns">{btns}</div></div>'


def figure(img_key_or_path, alt, caption=None, width=1024, height=768):
    src = IMG.get(img_key_or_path, img_key_or_path)
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    return (f'<figure><img src="{src}" alt="{alt}" width="{width}" height="{height}" loading="lazy">'
            f'{cap}</figure>')


def partner(h2, text, grid, anchor="ebz"):
    """Abschnitt 'Ihr Partner': Text, 4 Vorteile, NAP, Buttons. grid: Liste (titel, text)."""
    cells = "".join(f"<div><b>{t}</b>{x}</div>" for t, x in grid)
    return f"""
<section class="art-partner" id="{anchor}">
  <h2>{h2}</h2>
  <p>{text}</p>
  <div class="art-grid">{cells}</div>
  <ul class="art-partner__nap">
    <li><span class="ic" aria-hidden="true">⌂</span>{NAP['name']}, {NAP['street']}, {NAP['zip']} {NAP['city']}</li>
    <li><span class="ic" aria-hidden="true">☎</span>{tel_link()}</li>
    <li><span class="ic" aria-hidden="true">✉</span><a href="mailto:{NAP['email']}">{NAP['email']}</a></li>
    <li><span class="ic" aria-hidden="true">◷</span>{NAP['hours']}</li>
  </ul>
  <div class="art-btns">{a('kontakt', 'Kostenlose Erstberatung', cls='btn btn--primary')}
    {tel_link(cls='btn btn--dark', label='☎ ' + NAP['phone_display'])}</div>
</section>"""


def faq(items):
    accs = "".join(
        f'<details class="acc"><summary>{q}</summary><div class="acc__body">{x}</div></details>'
        for q, x in items
    )
    return f'<div class="art-faq">{accs}</div>'


def author_box(note):
    return f"""
<div class="art-eeat">
  <img src="{IMG['mario']}" alt="{AUTHOR}, {AUTHOR_ROLE}" width="92" height="92" loading="lazy">
  <p><b>Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</b> {note}</p>
</div>"""


def sources(items):
    lis = "".join(
        f'<li><a href="{url}" rel="nofollow noopener" target="_blank">{label}</a></li>'
        for label, url in items
    )
    return f'<div class="art-sources"><p><b>Quellen</b></p><ul>{lis}</ul></div>'


# --- Helfer -------------------------------------------------------------------

def _text(html_str):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html_str)).strip()


def reading_minutes(html_str):
    words = len(_text(html_str).split())
    return max(1, round(words / 200))


def _date_de(iso):
    y, m, _d = iso.split("-")
    months = ["Jänner", "Februar", "März", "April", "Mai", "Juni", "Juli", "August",
              "September", "Oktober", "November", "Dezember"]
    return f"{months[int(m) - 1]} {y}"


# --- Renderer -----------------------------------------------------------------

def render(art):
    """Rendert ein ARTICLE-Dict zur fertigen Seite und schreibt out/<path>index.html."""
    path = art["path"]
    url = u(path)
    crumbs = [("Startseite", "home"), ("Ratgeber", "ratgeber")] + art.get("crumbs", [])

    # Hauptinhalt (Prose)
    body_parts = []
    if art.get("tldr"):
        body_parts.append(tldr(art["tldr"]))
    if art.get("kpis"):
        body_parts.append(kpis(art["kpis"]))
    toc = []
    for h2, sid, html_ in art["sections"]:
        toc.append((sid, h2))
        body_parts.append(f'<h2 id="{sid}">{h2}</h2>{html_}')
    if art.get("partner"):
        p = art["partner"]
        toc.append(("ebz", p.get("toc", "Ihr Partner: EBZ Energie")))
        body_parts.append(partner(p["h2"], p["text"], p["grid"]))
    if art.get("faq"):
        toc.append(("faq", "Häufige Fragen"))
        body_parts.append(f'<h2 id="faq">Häufige Fragen</h2>{faq(art["faq"])}')
    if art.get("author_note"):
        body_parts.append(author_box(art["author_note"]))
    if art.get("sources"):
        body_parts.append(sources(art["sources"]))
    prose = "".join(body_parts)

    minutes = reading_minutes(art["lead"] + prose)
    chips = "".join(f"<li>{c}</li>" for c in art.get("chips", []))
    crumb_html = "".join(
        f'<li><a href="{href(k)}">{n}</a></li>' for n, k in crumbs
    ) + f'<li aria-current="page">{art.get("crumb_label", art["eyebrow"])}</li>'
    hero_img = ""
    if art.get("hero_img"):
        src = IMG.get(art["hero_img"], art["hero_img"])
        hero_img = (f'<div class="article-hero__img"><img src="{src}" alt="{art["hero_alt"]}" '
                    f'width="760" height="570" fetchpriority="high"></div>')
    toc_html = "".join(f'<li><a href="#{sid}">{t}</a></li>' for sid, t in toc)

    body = f"""
  <section class="article-hero">
    <div class="wrap">
      <nav aria-label="Brotkrumen"><ol class="crumbs">{crumb_html}</ol></nav>
      <div class="article-hero__inner">
        <div>
          <p class="eyebrow">{art['eyebrow']}</p>
          <h1>{art['h1']}</h1>
          <p class="lead">{art['lead']}</p>
          <ul class="art-chips">{chips}</ul>
          <ul class="art-meta">
            <li>Aktualisiert: <b>{_date_de(art['date_modified'])}</b></li>
            <li>Lesezeit: <b>{minutes} Minuten</b></li>
            <li>Fachlich geprüft von <b>{AUTHOR}</b></li>
          </ul>
        </div>
        {hero_img}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="article-grid">
        <article class="prose">{prose}</article>
        <aside class="article-aside">
          <div class="aside-card aside-card--toc"><h2>Inhalt</h2><ul class="toc">{toc_html}</ul></div>
          <div class="aside-card aside-card--dark">
            <h3>{art['cta']['h3']}</h3>
            <p>{art['cta']['text']}</p>
            {a(art['cta'].get('primary', ('kontakt', 'Kostenlose Beratung'))[0], art['cta'].get('primary', ('kontakt', 'Kostenlose Beratung'))[1], cls='btn btn--primary')}
            {tel_link(cls='btn btn--light', label='☎ ' + NAP['phone_display'])}
            <small>{NAP['hours']}<br>{NAP['rating']} Sterne auf Google · 300+ Projekte</small>
          </div>
        </aside>
      </div>
    </div>
  </section>
""" + C.linkgrid_section("Weiterlesen", art["related"]) + C.finalcta(
        art.get("final_h2", "Sprechen wir über Ihr Energiesystem"),
        art.get("final_text", "Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, "
                              "das Planung, Montage und Förderabwicklung aus einer Hand übernimmt."),
    )

    faq_ld = faq_jsonld(url, [(q, _text(x)) for q, x in art.get("faq", [])]) if art.get("faq") else None
    extra = [
        article_jsonld(url, art["h1"], art["description"], art["date_published"],
                       art["date_modified"], IMG.get(art.get("hero_img"), art.get("hero_img"))),
        breadcrumb_jsonld([(n, u(k)) for n, k in crumbs] + [(art.get("crumb_label", art["eyebrow"]), url)]),
    ]
    html_doc = page(art["title"], art["description"], path, body, faq_jsonld_str=faq_ld,
                    og_image=IMG.get(art.get("hero_img"), art.get("hero_img")),
                    extra_jsonld=extra, og_type="article")
    rel = path.strip("/") + "/index.html"
    return write_page(rel, html_doc)
