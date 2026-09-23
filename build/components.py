"""Wiederverwendbare Sektions-Komponenten (Design-System der Uebergabe).

Jede Funktion gibt fertiges HTML einer Sektion zurueck. Icons sind Unicode,
keine Icon-Fonts, keine Emojis. Reveal ueber Klasse 'eg-reveal'.
"""

import html as _html

from common import NAP, CLAIMS, AUTHOR, AUTHOR_ROLE, IMG, a, href, tel_link


def hero(eyebrow, h1, lead, badges, img, img_alt, float_num=None, float_label=None,
         cta_primary=("kontakt", "Kostenlose Beratung"), cta_secondary=("solarrechner", "Solarrechner")):
    badge_html = "".join(
        f'<span class="hero__badge"><b>{b0}</b> {b1}</span>' for b0, b1 in badges
    )
    floater = ""
    if float_num:
        floater = (f'<div class="hero__float"><span aria-hidden="true">★</span>'
                   f'<span><b>{float_num}</b><small>{float_label}</small></span></div>')
    return f"""
  <section class="hero">
    <div class="hero__inner">
      <div class="hero__copy eg-reveal">
        <p class="eyebrow">{eyebrow}</p>
        <h1>{h1}</h1>
        <p class="lead">{lead}</p>
        <div class="hero__badges">{badge_html}</div>
        <div class="hero__cta">
          {a(cta_primary[0], cta_primary[1], cls='btn btn--primary btn--lg')}
          {a(cta_secondary[0], cta_secondary[1], cls='btn btn--light btn--lg')}
        </div>
      </div>
      <div class="hero__media eg-reveal">
        <img src="{img}" alt="{img_alt}" width="720" height="540" fetchpriority="high">
        {floater}
      </div>
    </div>
  </section>"""


def kpis(items):
    """items: Liste aus (zahl, label). Zahl kann '300+' o. reine Zahl mit data-count sein."""
    cells = ""
    for value, label in items:
        cells += f'<div class="kpi eg-reveal"><b>{value}</b><span>{label}</span></div>'
    return f'<section class="kpis"><div class="kpis__grid">{cells}</div></section>'


def _hub_svg():
    """Hub-Diagramm: EBZ im Zentrum, sechs Bausteine im Orbit.

    Glow um das Zentrum, feiner Orbit-Ring und fließende Energie-Linien
    (CSS-Animation ueber .hub-spoke, wird bei prefers-reduced-motion pausiert).
    """
    import math
    cx, cy, R = 220, 220, 150
    node_r, center_r = 44, 58
    # angle_deg, label, icon  (im Uhrzeigersinn ab oben)
    defs = [(-90, "Sonne", "☀"), (-30, "Speicher", "▮"),
            (30, "Wärme", "♨"), (90, "E-Auto", "⌂"),
            (150, "Netz", "⇄"), (210, "Steuerung", "⚙")]
    nodes = []
    for ang, label, ic in defs:
        rad = math.radians(ang)
        nodes.append((cx + R * math.cos(rad), cy + R * math.sin(rad), label, ic))

    spokes = "".join(
        f'<line class="hub-spoke" x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}"/>'
        for x, y, _, _ in nodes
    )
    dots = ""
    for x, y, label, ic in nodes:
        dots += (
            f'<g class="hub-node">'
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{node_r}" fill="url(#hubNode)" '
            f'stroke="rgba(245,166,35,.55)" stroke-width="1.5"/>'
            f'<text x="{x:.0f}" y="{y-6:.0f}" text-anchor="middle" font-size="24" fill="#f5a623">{ic}</text>'
            f'<text x="{x:.0f}" y="{y+18:.0f}" text-anchor="middle" font-size="13" '
            f'font-family="Sora,sans-serif" font-weight="600" fill="#dcebf0">{label}</text></g>')

    return f"""<svg viewBox="0 0 440 440" role="img" aria-label="EBZ Energie als Zentrum Ihrer Energieversorgung mit Photovoltaik, Speicher, Waerme, E-Auto, Netz und Steuerung">
      <defs>
        <radialGradient id="hubCenter" cx="50%" cy="42%" r="65%">
          <stop offset="0%" stop-color="#ffc555"/>
          <stop offset="100%" stop-color="#f5a623"/>
        </radialGradient>
        <radialGradient id="hubNode" cx="50%" cy="35%" r="75%">
          <stop offset="0%" stop-color="#12586f"/>
          <stop offset="100%" stop-color="#0a3a4d"/>
        </radialGradient>
        <filter id="hubGlow" x="-60%" y="-60%" width="220%" height="220%">
          <feGaussianBlur stdDeviation="12" result="b"/>
          <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
      </defs>
      <circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>
      {spokes}
      <circle class="hub-pulse" cx="{cx}" cy="{cy}" r="{center_r}" fill="none"
        stroke="rgba(245,166,35,.5)" stroke-width="2"/>
      {dots}
      <circle cx="{cx}" cy="{cy}" r="{center_r}" fill="url(#hubCenter)" filter="url(#hubGlow)"/>
      <text x="{cx}" y="{cy-6}" text-anchor="middle" font-size="22" font-weight="800"
        font-family="Sora,sans-serif" fill="#0a3a4d">EBZ</text>
      <text x="{cx}" y="{cy+16}" text-anchor="middle" font-size="12" font-weight="600"
        font-family="Sora,sans-serif" fill="#0a3a4d">Energie</text>
    </svg>"""


def hub_section(eyebrow, h2, lead, points):
    """points: Liste aus (icon, text)."""
    li = "".join(f'<li><span class="ic" aria-hidden="true">{ic}</span><span>{t}</span></li>'
                 for ic, t in points)
    return f"""
  <section class="section dark">
    <div class="wrap">
      <div class="hub">
        <div class="eg-reveal">{_hub_svg()}</div>
        <div class="eg-reveal">
          <p class="eyebrow">{eyebrow}</p>
          <h2>{h2}</h2>
          <p class="lead">{lead}</p>
          <ul class="hub__list">{li}</ul>
        </div>
      </div>
    </div>
  </section>"""


def problem_compare(eyebrow, h2, intro, bars, aside=None):
    """bars: Liste aus (label, prozent, 'bad'|'good', wert_text).

    aside (optional): (titel, [(icon, fett, text), ...]) rendert rechts eine
    dunkle Karte, damit die Sektion ausgewogen wirkt (Zweispalter).
    """
    rows = ""
    for label, pct, kind, val in bars:
        rows += (f'<div class="bar eg-reveal"><div class="bar__top"><span>{label}</span>'
                 f'<span>{val}</span></div>'
                 f'<div class="bar__track"><div class="bar__fill bar__fill--{kind}" '
                 f'style="--w:{pct}%"></div></div></div>')
    left = (f'<div class="eg-reveal"><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2>'
            f'<p class="lead">{intro}</p><div class="compare">{rows}</div></div>')

    if aside:
        title, items = aside
        li = "".join(
            f'<li><span class="ic" aria-hidden="true">{ic}</span>'
            f'<span><b>{b}</b><span>{t}</span></span></li>'
            for ic, b, t in items
        )
        aside_html = (f'<div class="compare-aside eg-reveal"><h3>{title}</h3>'
                      f'<ul class="flowlist">{li}</ul></div>')
        inner = f'<div class="compare-grid">{left}{aside_html}</div>'
    else:
        inner = left

    return f"""
  <section class="section">
    <div class="wrap">{inner}</div>
  </section>"""


def cards_section(eyebrow, h2, intro, cards, with_media=False):
    """cards: Liste aus dicts mit keys: ic|img, title, text, link_key, link_text, alt."""
    items = ""
    for c in cards:
        if with_media and c.get("img"):
            media = f'<img class="card__media" src="{c["img"]}" alt="{c.get("alt","")}" loading="lazy" width="400" height="250">'
            head = ""
        else:
            media = ""
            head = f'<div class="card__ic" aria-hidden="true">{c.get("ic","◇")}</div>'
        link = ""
        if c.get("link_key"):
            link = a(c["link_key"], c.get("link_text", "Mehr erfahren") + ' <span aria-hidden="true">→</span>', cls="card__link")
        items += f"""
        <article class="card eg-reveal">{media}
          <div class="card__body">{head}
            <h3>{c['title']}</h3>
            <p>{c['text']}</p>
            {link}
          </div>
        </article>"""
    return f"""
  <section class="section">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">{eyebrow}</p>
      <h2 class="center eg-reveal">{h2}</h2>
      <p class="lead center eg-reveal" style="max-width:70ch;margin-inline:auto">{intro}</p>
      <div class="cards" style="margin-top:36px">{items}</div>
    </div>
  </section>"""


def split_section(left, right):
    """left/right: dicts mit keys title, items (Liste), dark(bool), note(optional)."""
    def panel(p):
        cls = "panel panel--dark" if p.get("dark") else "panel"
        li = "".join(f"<li>{x}</li>" for x in p["items"])
        note = f'<p class="form-note" style="margin-top:16px">{p["note"]}</p>' if p.get("note") else ""
        return (f'<div class="{cls} eg-reveal"><h3>{p["title"]}</h3>'
                f'<ul class="checklist">{li}</ul>{note}</div>')
    return f"""
  <section class="section">
    <div class="wrap">
      <div class="split">{panel(left)}{panel(right)}</div>
    </div>
  </section>"""


def media_text(eyebrow, h2, paragraphs, img, alt, bullets=None, reverse=False,
               cta=None, dark=False):
    """Bild-Text-Block (alternierend). paragraphs: Liste aus HTML-Absaetzen."""
    rev = " mediatext--reverse" if reverse else ""
    ps = "".join(f"<p>{p}</p>" for p in paragraphs)
    checklist = ""
    if bullets:
        checklist = '<ul class="checklist">' + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>"
    cta_html = ""
    if cta:
        cta_html = '<div class="hero__cta" style="margin-top:22px">' + a(cta[0], cta[1], cls="btn btn--primary") + "</div>"
    sec_cls = "section dark" if dark else "section"
    return f"""
  <section class="{sec_cls}">
    <div class="wrap">
      <div class="mediatext{rev}">
        <div class="mediatext__media eg-reveal">
          <img src="{img}" alt="{alt}" loading="lazy" width="620" height="465">
        </div>
        <div class="eg-reveal">
          <p class="eyebrow">{eyebrow}</p>
          <h2>{h2}</h2>
          {ps}{checklist}{cta_html}
        </div>
      </div>
    </div>
  </section>"""


def price_cards(eyebrow, h2, intro, items, note):
    """items: Liste aus dicts mit keys size, price, price_sub, features (Liste)."""
    cards = ""
    for it in items:
        feats = "".join(f"<li>{x}</li>" for x in it["features"])
        cards += (f'<div class="price-card eg-reveal"><span class="price-card__size">{it["size"]}</span>'
                  f'<span class="price-card__price">{it["price"]}<small>{it["price_sub"]}</small></span>'
                  f'<ul>{feats}</ul></div>')
    return f"""
  <section class="section" style="background:#fff;border-block:1px solid var(--line)">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">{eyebrow}</p>
      <h2 class="center eg-reveal">{h2}</h2>
      <p class="lead center eg-reveal" style="max-width:70ch;margin-inline:auto">{intro}</p>
      <div class="cards" style="margin-top:36px">{cards}</div>
      <p class="form-note center eg-reveal" style="margin-top:22px">{note}</p>
    </div>
  </section>"""


def reference_cards(eyebrow, h2, intro, items):
    """Referenzprojekte mit Zahlen. items: dict img, alt, title, specs, result, result_sub.

    Bild und Zahlen muessen zum selben Projekt gehoeren (CLAUDE.md).
    """
    cards = ""
    for it in items:
        cards += f"""
        <article class="card eg-reveal">
          <img class="card__media" src="{it['img']}" alt="{it['alt']}" loading="lazy" width="400" height="250">
          <div class="card__body">
            <h3>{it['title']}</h3>
            <p class="card__specs">{it['specs']}</p>
            <p class="card__result">{it['result']}<small>{it['result_sub']}</small></p>
          </div>
        </article>"""
    cta = a("referenzen", 'Alle Referenzen ansehen <span aria-hidden="true">→</span>', cls="btn btn--ghost")
    return f"""
  <section class="section">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">{eyebrow}</p>
      <h2 class="center eg-reveal">{h2}</h2>
      <p class="lead center eg-reveal" style="max-width:70ch;margin-inline:auto">{intro}</p>
      <div class="cards" style="margin-top:36px">{cards}</div>
      <div class="center eg-reveal" style="margin-top:28px">{cta}</div>
    </div>
  </section>"""


def regions_section(eyebrow, h2, intro, kaernten, steiermark, note=None):
    """Einzugsgebiet: zwei Panels mit Ortslisten."""
    def col(title, orte):
        li = "".join(f"<li>{o}</li>" for o in orte)
        return f'<div class="panel eg-reveal"><h3>{title}</h3><ul class="regions">{li}</ul></div>'
    n = f'<p class="form-note center eg-reveal" style="margin-top:22px">{note}</p>' if note else ""
    return f"""
  <section class="section">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">{eyebrow}</p>
      <h2 class="center eg-reveal">{h2}</h2>
      <p class="lead center eg-reveal" style="max-width:70ch;margin-inline:auto">{intro}</p>
      <div class="split" style="margin-top:32px">{col('Kärnten', kaernten)}{col('Steiermark', steiermark)}</div>
      {n}
    </div>
  </section>"""


def steps_section(eyebrow, h2, steps):
    """steps: Liste aus (title, text, zeit)."""
    items = ""
    for title, text, zeit in steps:
        z = f'<span class="step__t">{zeit}</span>' if zeit else ""
        items += (f'<div class="step eg-reveal"><div class="step__n" aria-hidden="true"></div>'
                  f'<h3>{title}</h3><p>{text}</p>{z}</div>')
    return f"""
  <section class="section" style="background:#fff;border-block:1px solid var(--line)">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">{eyebrow}</p>
      <h2 class="center eg-reveal">{h2}</h2>
      <div class="steps" style="margin-top:36px">{items}</div>
    </div>
  </section>"""


def why_section(eyebrow, h2, items):
    """items: Liste aus (icon, title, text)."""
    cells = ""
    for ic, title, text in items:
        cells += (f'<div class="why__item eg-reveal"><div class="why__ic" aria-hidden="true">{ic}</div>'
                  f'<div><h3>{title}</h3><p>{text}</p></div></div>')
    return f"""
  <section class="section">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">{eyebrow}</p>
      <h2 class="center eg-reveal">{h2}</h2>
      <div class="why" style="margin-top:36px">{cells}</div>
    </div>
  </section>"""


def reviews_block(quotes):
    """quotes: Liste aus (text, name). Google 4,9."""
    cards = "".join(
        f'<div class="review eg-reveal"><div class="stars" aria-hidden="true">★★★★★</div>'
        f'<p>„{t}“</p><div class="review__by">{n}</div></div>'
        for t, n in quotes
    )
    return f"""
  <section class="section" style="background:#fff;border-block:1px solid var(--line)">
    <div class="wrap">
      <div class="reviews__head eg-reveal">
        <span class="stars" aria-hidden="true">★★★★★</span>
        <strong style="font-family:var(--font-head);font-size:1.2rem">{NAP['rating']} von 5</strong>
        <span style="color:var(--muted)">auf Google, aus echten Kundenbewertungen</span>
      </div>
      <h2 class="center eg-reveal">Das sagen unsere Kundinnen und Kunden</h2>
      <div class="reviews__grid">{cards}</div>
    </div>
  </section>"""


def reviews_slider(reviews, rating="4,9", count=None):
    """Slider mit echten Google-Rezensionen (4 und 5 Sterne).

    reviews: Liste aus dicts mit author, rating, text, optional date.
    Wird zur Build-Zeit aus build/data/reviews.json befuellt.
    """
    cards = ""
    for r in reviews:
        stars = "★" * int(round(r.get("rating", 5)))
        author = _html.escape(r.get("author", "Google Nutzer"))
        text = _html.escape(r.get("text", ""))
        initial = (author.strip()[:1] or "G").upper()
        date = f'<small>{_html.escape(r["date"])}</small>' if r.get("date") else ""
        cards += (
            f'<article class="rev-card">'
            f'<div class="stars" aria-hidden="true">{stars}</div>'
            f'<p>„{text}“</p>'
            f'<div class="rev-meta"><span class="rev-avatar" aria-hidden="true">{initial}</span>'
            f'<span class="rev-by">{author}{date}'
            f'<span class="rev-g">★ Google Rezension</span></span></div>'
            f'</article>'
        )
    count_txt = f"aus {count} Bewertungen" if count else "aus echten Kundenbewertungen"
    return f"""
  <section class="section" style="background:#fff;border-block:1px solid var(--line)">
    <div class="wrap">
      <div class="reviews__head eg-reveal">
        <span class="stars" aria-hidden="true">★★★★★</span>
        <strong style="font-family:var(--font-head);font-size:1.2rem">{rating} von 5</strong>
        <span class="rev-count">auf Google, {count_txt}</span>
      </div>
      <h2 class="center eg-reveal">Das sagen unsere Kundinnen und Kunden</h2>
      <div class="rev-slider eg-reveal">
        <div class="rev-track">{cards}</div>
        <div class="rev-nav">
          <button class="rev-btn rev-prev" type="button" aria-label="Vorherige Bewertungen">‹</button>
          <button class="rev-btn rev-next" type="button" aria-label="Weitere Bewertungen">›</button>
        </div>
      </div>
    </div>
  </section>"""


def about_section(eyebrow, h2, paragraphs, values, quote, badge=None,
                  img=None, img_alt="", cta=("ueber_uns", "Mehr über uns")):
    """Ausfuehrlicher Ueber-uns-Block (Teambild, Story, Werte, Gruender-Zitat, CTA).

    paragraphs: Liste HTML-Absaetze. values: Liste (icon, text). quote: (text, author, role).
    badge: (zahl, label) fuer das schwebende Badge am Bild. Verlinkt auf die Ueber-uns-Seite.
    """
    ps = "".join(f"<p>{p}</p>" for p in paragraphs)
    vals = "".join(
        f'<li><span class="ic" aria-hidden="true">{ic}</span><span>{t}</span></li>'
        for ic, t in values
    )
    badge_html = ""
    if badge:
        badge_html = (f'<div class="about-media__badge"><span aria-hidden="true">★</span>'
                      f'<span><b>{badge[0]}</b><small>{badge[1]}</small></span></div>')
    q_text, q_author, q_role = quote
    q_img = f'<img src="{IMG["mario"]}" alt="{q_author}, {q_role}" loading="lazy" width="62" height="62">'
    return f"""
  <section class="section about">
    <div class="wrap">
      <div class="about-grid">
        <div class="about-media eg-reveal">
          <img src="{img or IMG['team_quer']}" alt="{img_alt}" loading="lazy" width="620" height="465">
          {badge_html}
        </div>
        <div class="eg-reveal">
          <p class="eyebrow">{eyebrow}</p>
          <h2>{h2}</h2>
          {ps}
          <ul class="about-values">{vals}</ul>
          <div class="about-quote">
            {q_img}
            <div>
              <blockquote>„{q_text}“</blockquote>
              <cite>{q_author}<small>{q_role}</small></cite>
            </div>
          </div>
          <div class="hero__cta" style="margin-top:24px">
            {a(cta[0], cta[1], cls='btn btn--primary')}
          </div>
        </div>
      </div>
    </div>
  </section>"""


def founder_block(quote):
    return f"""
  <section class="section">
    <div class="wrap">
      <div class="founder eg-reveal">
        <img src="{IMG['mario']}" alt="{AUTHOR}, {AUTHOR_ROLE}" width="220" height="220" loading="lazy">
        <div>
          <blockquote>„{quote}“</blockquote>
          <cite>{AUTHOR}<small>{AUTHOR_ROLE}</small></cite>
        </div>
      </div>
    </div>
  </section>"""


def finance_band():
    return f"""
  <section class="section">
    <div class="wrap">
      <div class="finance eg-reveal">
        <div>
          <p class="eyebrow">Faire Finanzierung</p>
          <h2>Ihre Anlage gehört Ihnen ab dem ersten Tag</h2>
          <p class="lead">Sie finanzieren Ihre Photovoltaikanlage bequem in monatlichen Raten
          und bleiben trotzdem von Beginn an Eigentümer. Volle Förderung für Privatpersonen,
          keine strengen Bonitätsprüfungen und kein Datenbankeintrag.</p>
          <div class="hero__cta">{a('finanzierung', 'Finanzierung ansehen', cls='btn btn--primary')}</div>
        </div>
        <div class="finance__price">
          <span style="color:#c6dbe2">Komplettanlage inklusive Speicher</span>
          <b>ab 147 €</b>
          <span style="color:#c6dbe2">pro Monat*</span>
          <p class="form-note" style="color:#9fbcc6;margin-top:14px">*Beispielkonditionen,
          abhängig von Anlagengröße und Laufzeit.</p>
        </div>
      </div>
    </div>
  </section>"""


def contact_section(headline, sub, form_note="Wir melden uns innerhalb eines Werktags."):
    return f"""
  <section class="section contact" id="beratung">
    <div class="wrap">
      <div class="contact__grid">
        <div class="eg-reveal">
          <p class="eyebrow">Kostenlose Erstberatung</p>
          <h2>{headline}</h2>
          <p class="lead">{sub}</p>
          <ul class="contact__facts">
            <li><span class="ic" aria-hidden="true">☎</span> {tel_link()}</li>
            <li><span class="ic" aria-hidden="true">✉</span> <a href="mailto:{NAP['email']}">{NAP['email']}</a></li>
            <li><span class="ic" aria-hidden="true">⌂</span> {NAP['street']}, {NAP['zip']} {NAP['city']}</li>
            <li><span class="ic" aria-hidden="true">◷</span> {NAP['hours']}</li>
          </ul>
        </div>
        <form class="form-card eg-reveal" action="#" method="post" novalidate>
          <div class="field">
            <label for="name">Name</label>
            <input id="name" name="name" type="text" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="email">E-Mail</label>
            <input id="email" name="email" type="email" autocomplete="email" required>
          </div>
          <div class="field">
            <label for="tel">Telefon</label>
            <input id="tel" name="tel" type="tel" autocomplete="tel">
          </div>
          <div class="field">
            <label for="msg">Ihr Anliegen</label>
            <textarea id="msg" name="msg" rows="4"></textarea>
          </div>
          <button class="btn btn--primary btn--lg" type="submit" style="width:100%">Beratung anfragen</button>
          <p class="form-note">{form_note}</p>
        </form>
      </div>
    </div>
  </section>"""


def faq_section(items):
    """items: Liste aus (frage, antwort_html)."""
    accs = "".join(
        f'<details class="acc eg-reveal"><summary>{q}</summary>'
        f'<div class="acc__body">{a_}</div></details>'
        for q, a_ in items
    )
    return f"""
  <section class="section" style="background:#fff;border-block:1px solid var(--line)">
    <div class="wrap">
      <h2 class="center eg-reveal">Häufige Fragen</h2>
      <div class="faq" style="margin-top:32px">{accs}</div>
    </div>
  </section>"""


def linkgrid_section(h2, links):
    """links: Liste aus (key_or_path, text)."""
    cells = "".join(
        f'<a href="{href(k)}">{t} <span aria-hidden="true">→</span></a>' for k, t in links
    )
    return f"""
  <section class="section--tight section">
    <div class="wrap">
      <h2 class="center eg-reveal" style="margin-bottom:28px">{h2}</h2>
      <div class="linkgrid">{cells}</div>
    </div>
  </section>"""


def finalcta(h2, text, cta=("kontakt", "Jetzt Beratung sichern")):
    return f"""
  <section class="section">
    <div class="wrap">
      <div class="finalcta eg-reveal">
        <h2>{h2}</h2>
        <p>{text}</p>
        {a(cta[0], cta[1], cls='btn btn--dark btn--lg')}
      </div>
    </div>
  </section>"""
