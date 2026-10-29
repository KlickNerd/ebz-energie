"""Seiten-Geruest: <head>, Header (Navigation), Footer.

page(...) baut ein vollstaendiges HTML5-Dokument. Header und Footer sind
seitenuebergreifend identisch (eine Quelle) und werden hier gepflegt.
"""

from chatbot import CHATBOT_HTML
from common import (BASE, NAP, S, IMG, a, href, tel_link, u,
                    localbusiness_jsonld, GSC_VERIFICATION, ADS_ID)

# Schriften liegen selbst gehostet unter /assets/fonts/ (kein Aufruf von Google-Servern, DSGVO).
# Die @font-face-Regeln stehen am Anfang von styles.css (theme.write_assets), hier nur Preload der Latin-Dateien.
# Version der CSS/JS-Dateien: bei Aenderungen an Formular-JS oder CSS erhoehen, damit Browser neu laden
ASSET_V = "20261029b"

FONTS = (
    '<link rel="preload" href="/assets/fonts/sora-latin.woff2" as="font" type="font/woff2" crossorigin>'
    '<link rel="preload" href="/assets/fonts/source-sans-3-latin.woff2" as="font" type="font/woff2" crossorigin>'
)


def _nav():
    leistungen = [
        ("photovoltaik", "Photovoltaik"),
        ("batteriespeicher", "Batteriespeicher"),
        ("waermepumpe", "Wärmepumpe"),
        ("balkonkraftwerke", "Balkonkraftwerke"),
        ("ems", "Energiemanagement"),
        ("eg_privat", "Energiegemeinschaft"),
        ("foerderungen", "Förderungen"),
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
            <li>{a('foerderungen', 'Förderungen')}</li>
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
          <h4>Standorte</h4>
          <ul>
            <li>{a('pv_villach', 'Photovoltaik Villach')}</li>
            <li>{a('pv_klagenfurt', 'Photovoltaik Klagenfurt')}</li>
            <li>{a('pv_wolfsberg', 'Photovoltaik Wolfsberg')}</li>
            <li>{a('pv_graz', 'Photovoltaik Graz')}</li>
            <li>{a('pv_steiermark', 'Photovoltaik Steiermark')}</li>
            <li>{a('standorte', 'Alle Standorte')}</li>
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
        <span>{a('impressum', 'Impressum')} &middot; {a('datenschutz', 'Datenschutz')} &middot; <a href="#" class="js-cookie-settings">Cookie-Einstellungen</a></span>
      </div>
    </div>
  </footer>"""


def _sticky_cta(target="kontakt"):
    return f"""
  <div class="sticky-cta">
    <a class="btn btn--ghost" href="{NAP['phone_href']}">Anrufen</a>
    {a(target, 'Beratung anfragen', cls='btn btn--primary')}
  </div>"""


def _cookie_banner():
    return f"""
  <div class="cookie" id="cookie" role="dialog" aria-live="polite" aria-label="Cookie-Einstellungen" hidden>
    <p><b>Cookies für Werbemessung</b> Wir möchten Google Ads nutzen, um zu messen, ob unsere Anzeigen zu Anfragen führen.
    Dafür setzt Google Cookies. Das passiert nur mit Ihrer Zustimmung, die Sie jederzeit über „Cookie-Einstellungen“
    im Fußbereich widerrufen können. Mehr in der {a('datenschutz', 'Datenschutzerklärung')}.</p>
    <div class="cookie__btns">
      <button type="button" class="btn btn--ghost js-cookie" data-choice="denied">Nur notwendige</button>
      <button type="button" class="btn btn--primary js-cookie" data-choice="granted">Alle akzeptieren</button>
    </div>
  </div>"""


def _header_lp():
    """Header fuer Ads-Landingpages: Logo, Telefon, Sprung zum Formular. Kein Menue (keine Ablenkung)."""
    return f"""
  <header class="site-header site-header--lp">
    <div class="site-header__inner">
      <a class="brand" href="{href('home')}" aria-label="EBZ Energie Startseite">
        <img class="brand__logo" src="{IMG['logo']}" alt="EBZ Energie" width="969" height="223">
      </a>
      <div class="header-cta">
        <a class="header-phone" href="{NAP['phone_href']}">{NAP['phone_display']}<span>Mo bis Fr 10 bis 20 Uhr</span></a>
        <a class="btn btn--primary" href="#beratung">Angebot anfordern</a>
      </div>
    </div>
  </header>"""


def _footer_lp():
    return f"""
  <footer class="site-footer site-footer--lp">
    <div class="wrap">
      <div class="footer-bottom">
        <span>&copy; 2026 EBZ Energie GmbH &middot; {NAP['street']}, {NAP['zip']} {NAP['city']} &middot; {tel_link()}</span>
        <span>{a('home', 'Website')} &middot; {a('impressum', 'Impressum')} &middot; {a('datenschutz', 'Datenschutz')} &middot; <a href="#" class="js-cookie-settings">Cookie-Einstellungen</a></span>
      </div>
    </div>
  </footer>"""


def page(title, description, path, body, faq_jsonld_str=None,
         include_business_schema=False, og_image=None, extra_jsonld=None,
         og_type="website", landing=False):
    """Baut ein vollstaendiges HTML-Dokument.

    title/description: fuer <title> und Meta.
    path: kanonischer Pfad (z. B. "/photovoltaik/"), fuer canonical/OG.
    body: HTML der <main>-Sektionen.
    faq_jsonld_str: fertiges FAQPage-JSON (optional).
    include_business_schema: LocalBusiness einbetten (nur Startseite/Kontakt).
    extra_jsonld: weitere fertige JSON-LD-Strings (z. B. Article, BreadcrumbList).
    og_type: "website" oder "article" (Ratgeber).
    landing: Ads-Landingpage: noindex, Header ohne Menue, schlanker Footer, CTA springt zum Formular.
    """
    canonical = BASE + path
    og = BASE + (og_image or "/assets/img/hero-photovoltaik-villach.jpg")

    schemas = ""
    if include_business_schema:
        schemas += f'\n  <script type="application/ld+json">{localbusiness_jsonld()}</script>'
    if faq_jsonld_str:
        schemas += f'\n  <script type="application/ld+json">{faq_jsonld_str}</script>'
    for s in (extra_jsonld or []):
        schemas += f'\n  <script type="application/ld+json">{s}</script>'

    return f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="{'noindex,follow' if landing else 'index,follow,max-image-preview:large'}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:locale" content="de_AT">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og}">
  <meta name="theme-color" content="#0e4d64">
  <meta name="google-site-verification" content="{GSC_VERIFICATION}">
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("consent","default",{{ad_storage:"denied",ad_user_data:"denied",ad_personalization:"denied",analytics_storage:"denied"}});window.EBZ_ADS_ID="{ADS_ID}";</script>
  <link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
  {FONTS}
  <link rel="stylesheet" href="/assets/css/styles.css?v={ASSET_V}">{schemas}
</head>
<body>
  <a class="skip-link" href="#main">Zum Inhalt springen</a>
{_header_lp() if landing else _header()}
  <main id="main">
{body}
  </main>
{_footer_lp() if landing else _footer()}
{_sticky_cta("#beratung" if landing else "kontakt")}
{CHATBOT_HTML}
{_cookie_banner()}
  <script src="/assets/js/main.js?v={ASSET_V}" defer></script>
  <script src="/assets/js/chatbot.js" defer></script>
</body>
</html>
"""
