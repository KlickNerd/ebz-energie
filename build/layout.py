"""Seiten-Geruest: <head>, Header (Navigation), Footer.

page(...) baut ein vollstaendiges HTML5-Dokument. Header und Footer sind
seitenuebergreifend identisch (eine Quelle) und werden hier gepflegt.
"""

from common import (BASE, NAP, S, IMG, a, href, tel_link, u,
                    localbusiness_jsonld)

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    'family=Sora:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&display=swap">'
)


def _nav():
    leistungen = [
        ("photovoltaik", "Photovoltaik"),
        ("batteriespeicher", "Batteriespeicher"),
        ("waermepumpe", "Wärmepumpe"),
        ("balkonkraftwerke", "Balkonkraftwerke"),
        ("ems", "Energiemanagement"),
        ("eg_privat", "Energiegemeinschaft"),
    ]
    menu = "".join(a(k, t) for k, t in leistungen)
    return f"""
    <nav class="nav" id="nav" aria-label="Hauptnavigation">
      {a('photovoltaik', 'Photovoltaik')}
      {a('waermepumpe', 'Wärmepumpe')}
      <div class="nav__has">
        <a href="{href('leistungen')}" aria-haspopup="true">Leistungen ▾</a>
        <div class="nav__menu">{menu}</div>
      </div>
      {a('referenzen', 'Referenzen')}
      {a('ratgeber', 'Ratgeber')}
      {a('finanzierung', 'Finanzierung')}
      {a('kontakt', 'Kontakt')}
    </nav>"""


def _header():
    return f"""
  <header class="site-header">
    <div class="site-header__inner">
      <a class="brand" href="{href('home')}" aria-label="EBZ Energie Startseite">
        <img class="brand__logo" src="{IMG['logo']}" alt="EBZ Energie" width="969" height="223">
      </a>
      <button class="nav-toggle" aria-label="Menü" aria-controls="nav" aria-expanded="false">
        <span></span>
      </button>
      {_nav()}
      <div class="header-cta">
        <a class="header-phone" href="{NAP['phone_href']}">{NAP['phone_display']}<span>Mo bis Fr 10 bis 20 Uhr</span></a>
        {a('kontakt', 'Beratung', cls='btn btn--primary')}
      </div>
    </div>
  </header>"""


def _footer():
    return f"""
  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-brand">
          <a class="brand" href="{href('home')}" aria-label="EBZ Energie Startseite">
            <img class="brand__logo" src="{IMG['logo']}" alt="EBZ Energie" width="969" height="223">
          </a>
          <p>Ihr Photovoltaik-Fachbetrieb aus Villach. Planung, Montage und Service
          aus einer Hand für Kärnten, die Steiermark und ganz Österreich.</p>
        </div>
        <div class="footer-col">
          <h4>Leistungen</h4>
          <ul>
            <li>{a('photovoltaik', 'Photovoltaik')}</li>
            <li>{a('batteriespeicher', 'Batteriespeicher')}</li>
            <li>{a('waermepumpe', 'Wärmepumpe')}</li>
            <li>{a('balkonkraftwerke', 'Balkonkraftwerke')}</li>
            <li>{a('eg_privat', 'Energiegemeinschaft')}</li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Unternehmen</h4>
          <ul>
            <li>{a('ueber_uns', 'Über uns')}</li>
            <li>{a('referenzen', 'Referenzen')}</li>
            <li>{a('ratgeber', 'Ratgeber')}</li>
            <li>{a('kontakt', 'Kontakt')}</li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Kontakt</h4>
          <ul>
            <li>{NAP['street']}</li>
            <li>{NAP['zip']} {NAP['city']}</li>
            <li>{tel_link()}</li>
            <li><a href="mailto:{NAP['email']}">{NAP['email']}</a></li>
            <li>{NAP['hours']}</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 EBZ Energie GmbH</span>
        <span>{a('impressum', 'Impressum')} &middot; {a('datenschutz', 'Datenschutz')}</span>
      </div>
    </div>
  </footer>"""


def _sticky_cta():
    return f"""
  <div class="sticky-cta">
    <a class="btn btn--ghost" href="{NAP['phone_href']}">Anrufen</a>
    {a('kontakt', 'Beratung anfragen', cls='btn btn--primary')}
  </div>"""


def page(title, description, path, body, faq_jsonld_str=None,
         include_business_schema=False, og_image=None):
    """Baut ein vollstaendiges HTML-Dokument.

    title/description: fuer <title> und Meta.
    path: kanonischer Pfad (z. B. "/photovoltaik/"), fuer canonical/OG.
    body: HTML der <main>-Sektionen.
    faq_jsonld_str: fertiges FAQPage-JSON (optional).
    include_business_schema: LocalBusiness einbetten (nur Startseite/Kontakt).
    """
    canonical = BASE + path
    og = BASE + (og_image or "/assets/img/hero-photovoltaik-villach.jpg")

    schemas = ""
    if include_business_schema:
        schemas += f'\n  <script type="application/ld+json">{localbusiness_jsonld()}</script>'
    if faq_jsonld_str:
        schemas += f'\n  <script type="application/ld+json">{faq_jsonld_str}</script>'

    return f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="de_AT">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og}">
  <meta name="theme-color" content="#0e4d64">
  <link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
  {FONTS}
  <link rel="stylesheet" href="/assets/css/styles.css">{schemas}
</head>
<body>
  <a class="skip-link" href="#main">Zum Inhalt springen</a>
{_header()}
  <main id="main">
{body}
  </main>
{_footer()}
{_sticky_cta()}
  <script src="/assets/js/main.js" defer></script>
</body>
</html>
"""
