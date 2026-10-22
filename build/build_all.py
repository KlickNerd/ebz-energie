"""Baut die komplette Website nach out/.

Aufruf:  python3 build/build_all.py
Ergebnis: out/ enthaelt deploybare statische Seiten + assets/.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import theme
import home
import photovoltaik
import ueber_uns
import ratgeber
import finanzierung

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "out")

FAVICON = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
    '<rect width="64" height="64" rx="14" fill="#0e4d64"/>'
    '<circle cx="32" cy="32" r="12" fill="#f5a623"/>'
    '<g stroke="#f5a623" stroke-width="4" stroke-linecap="round">'
    '<line x1="32" y1="6" x2="32" y2="16"/><line x1="32" y1="48" x2="32" y2="58"/>'
    '<line x1="6" y1="32" x2="16" y2="32"/><line x1="48" y1="32" x2="58" y2="32"/>'
    '<line x1="13" y1="13" x2="20" y2="20"/><line x1="44" y1="44" x2="51" y2="51"/>'
    '<line x1="51" y1="13" x2="44" y2="20"/><line x1="20" y1="44" x2="13" y2="51"/>'
    '</g></svg>'
)


def write_favicon():
    path = os.path.join(OUT, "assets", "img", "favicon.svg")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(FAVICON)
    print("[OK ] assets/img/favicon.svg")


def copy_static():
    """Kopiert projekteigene Bilder aus build/static/img/ nach out/assets/img/."""
    import shutil
    src = os.path.join(ROOT, "build", "static", "img")
    dst = os.path.join(OUT, "assets", "img")
    if not os.path.isdir(src):
        return
    os.makedirs(dst, exist_ok=True)
    for name in os.listdir(src):
        if name.startswith("."):
            continue
        shutil.copy2(os.path.join(src, name), os.path.join(dst, name))
        print(f"[OK ] assets/img/{name} (static)")
    # Selbst gehostete Schriften
    fsrc = os.path.join(ROOT, "build", "static", "fonts")
    fdst = os.path.join(OUT, "assets", "fonts")
    if os.path.isdir(fsrc):
        os.makedirs(fdst, exist_ok=True)
        for name in os.listdir(fsrc):
            if name.endswith(".woff2"):
                shutil.copy2(os.path.join(fsrc, name), os.path.join(fdst, name))
                print(f"[OK ] assets/fonts/{name} (static)")


def write_meta_files():
    """robots.txt + Basis-Dateien fuer den Static-Deploy.

    Im Unterverzeichnis-Deploy (EBZ_BASE gesetzt, z. B. GitHub Pages Preview)
    wird die gesamte Seite auf noindex gestellt, damit die Preview-URL nicht
    mit der spaeteren Live-Domain konkurriert (Duplicate Content).
    """
    if os.environ.get("EBZ_BASE"):
        robots = "User-agent: *\nDisallow: /\n"
    else:
        robots = "User-agent: *\nAllow: /\nSitemap: https://ebz-photovoltaik.at/sitemap.xml\n"
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)
    # .nojekyll: verhindert Jekyll-Verarbeitung auf GitHub Pages
    with open(os.path.join(OUT, ".nojekyll"), "w", encoding="utf-8") as f:
        f.write("")
    print("[OK ] robots.txt + .nojekyll")
    write_htaccess()


# Erst auf True setzen, wenn das IONOS-Zertifikat fuer die Domain aktiv ist (sonst SSL-Warnung beim Umzug).
HTTPS_READY = True


def write_htaccess():
    """.htaccess fuer den Apache-Webspace bei IONOS: https, ohne www, 301 aus build/redirects.txt, 404, Caching.

    GitHub Pages ignoriert die Datei; fuer die Vorschau ist sie wirkungslos.
    """
    rules = []
    with open(os.path.join(ROOT, "build", "redirects.txt"), encoding="utf-8") as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 2 and parts[0].startswith("/") and parts[1].startswith("/"):
                old = parts[0].strip("/")
                if old.endswith("*"):
                    # Platzhalter: /author/* trifft /author/ und alles darunter
                    base = re.escape(old.rstrip("*").strip("/")).replace("\\-", "-")
                    pattern = "^" + base + "(/.*)?$"
                else:
                    pattern = "^$" if not old else "^" + re.escape(old).replace("\\-", "-") + "/?$"
                rules.append(f"RewriteRule {pattern} {parts[1]} [R=301,L]")
    if HTTPS_READY:
        canon = ("# https und Hauptdomain ohne www\n"
                 "RewriteCond %{HTTPS} off [OR]\n"
                 "RewriteCond %{HTTP_HOST} ^www\\. [NC]\n"
                 "RewriteRule ^ https://ebz-photovoltaik.at%{REQUEST_URI} [R=301,L]")
    else:
        canon = ("# Uebergang bis das SSL-Zertifikat aktiv ist: nur www -> ohne www, noch kein Zwang auf https\n"
                 "RewriteCond %{HTTP_HOST} ^www\\. [NC]\n"
                 "RewriteRule ^ %{REQUEST_SCHEME}://ebz-photovoltaik.at%{REQUEST_URI} [R=301,L]")
    body = f"""# Automatisch erzeugt von build/build_all.py aus build/redirects.txt. Nicht von Hand aendern.
Options -Indexes
DirectoryIndex index.html
ErrorDocument 404 /404.html

RewriteEngine On
{canon}

# 301-Weiterleitungen alter WordPress-Adressen ({len(rules)})
{chr(10).join(rules)}

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json image/svg+xml text/xml text/plain
</IfModule>
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/html "access plus 0 seconds"
  ExpiresByType text/css "access plus 7 days"
  ExpiresByType application/javascript "access plus 7 days"
  ExpiresByType image/jpeg "access plus 30 days"
  ExpiresByType image/png "access plus 30 days"
  ExpiresByType image/svg+xml "access plus 30 days"
  ExpiresByType font/woff2 "access plus 365 days"
</IfModule>
<IfModule mod_headers.c>
  Header always set X-Content-Type-Options "nosniff"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
"""
    with open(os.path.join(OUT, ".htaccess"), "w", encoding="utf-8") as f:
        f.write(body)
    print(f"[OK ] .htaccess ({len(rules)} Weiterleitungen)")


def write_sitemap():
    """sitemap.xml aus allen gebauten Seiten; lastmod der Ratgeber aus date_modified."""
    import datetime
    from common import BASE
    today = datetime.date.today().isoformat()
    lastmod = {art["path"]: art["date_modified"] for art in ratgeber.load_articles()}
    urls = []
    for dirpath, _dirs, files in os.walk(OUT):
        if "index.html" not in files:
            continue
        with open(os.path.join(dirpath, "index.html"), encoding="utf-8") as f:
            if 'content="noindex' in f.read(4000):
                continue  # Ads-Landingpages und andere noindex-Seiten gehoeren nicht in die Sitemap
        rel = os.path.relpath(dirpath, OUT).replace(os.sep, "/")
        path = "/" if rel == "." else f"/{rel}/"
        prio = "1.0" if path == "/" else ("0.6" if path in lastmod else "0.8")
        urls.append((path, lastmod.get(path, today), prio))
    urls.sort()
    body = "".join(
        f"  <url><loc>{BASE}{p}</loc><lastmod>{m}</lastmod><priority>{pr}</priority></url>\n"
        for p, m, pr in urls
    )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + "</urlset>\n")
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"[OK ] sitemap.xml ({len(urls)} URLs)")


def build_pages():
    """Baut alle Seitenmodule aus build/pages/*.py (jedes Modul stellt build() bereit)."""
    import importlib.util
    pages_dir = os.path.join(ROOT, "build", "pages")
    errors = []
    for name in sorted(os.listdir(pages_dir)):
        if not name.endswith(".py") or name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location("pages_" + name[:-3], os.path.join(pages_dir, name))
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
            errors += mod.build() or []
        except Exception as exc:  # halbfertige Seite blockiert nicht den Build
            print(f"[ERR] pages/{name}: {type(exc).__name__}: {exc}")
            errors.append(str(exc))
    return errors


def write_llms():
    """llms.txt (GEO): kompakte Uebersicht fuer KI-Suchsysteme (ChatGPT, Perplexity, Gemini) nach llmstxt.org.
    Unternehmensfakten aus common/NAP, dazu alle indexierbaren Seiten aus der Sitemap mit Titel und Beschreibung."""
    import html as _html
    from common import BASE, NAP
    sm = open(os.path.join(OUT, "sitemap.xml"), encoding="utf-8").read()
    paths = [u.replace(BASE, "") for u in re.findall(r"<loc>([^<]+)</loc>", sm)]
    arts = {a["path"] for a in ratgeber.load_articles()}
    groups = {"Leistungen und Angebot": [], "Standorte": [], "Förderung und Rechner": [], "Ratgeber": [], "Unternehmen": []}
    for p in paths:
        f = os.path.join(OUT, p.strip("/"), "index.html") if p != "/" else os.path.join(OUT, "index.html")
        h = open(f, encoding="utf-8").read(6000)
        title = _html.unescape(re.search(r"<title>(.*?)</title>", h).group(1)).split(" | ")[0]
        desc = _html.unescape(re.search(r'<meta name="description" content="([^"]*)"', h).group(1))
        line = f"- [{title}]({BASE}{p}): {desc}"
        if p in arts:
            groups["Ratgeber"].append(line)
        elif p.startswith("/photovoltaik-") and p.count("-") <= 2 and "foerderung" not in p and p not in ("/photovoltaik-carport/", "/photovoltaik-gewerbe/") or p == "/standorte/":
            groups["Standorte"].append(line)
        elif "foerder" in p or "rechner" in p:
            groups["Förderung und Rechner"].append(line)
        elif p in ("/ueber-uns/", "/referenzen/", "/kontakt/", "/impressum/", "/datenschutz/") or p.startswith("/referenzen/"):
            groups["Unternehmen"].append(line)
        else:
            groups["Leistungen und Angebot"].append(line)
    out = [
        f"# {NAP['name']}",
        "",
        (f"> Photovoltaik-Fachbetrieb aus Villach für Kärnten und die Steiermark: Photovoltaik mit Speicher, "
         f"Wärmepumpe, Energiemanagement, Balkonkraftwerke und Energiegemeinschaften aus einer Hand."),
        "",
        f"- Adresse: {NAP['street']}, {NAP['zip']} {NAP['city']}, Österreich",
        f"- Telefon: {NAP['phone_display']}, E-Mail: {NAP['email']}, {NAP['hours']}",
        "- Montagegebiet: Kärnten und Steiermark, Referenzen in 6 Bundesländern (300+ dokumentierte Projekte)",
        f"- Google-Bewertung: {NAP['rating']} Sterne",
        "- Garantie: bis zu 30 Jahre Leistungsgarantie auf Module, mindestens 10 Jahre Produktgarantie",
        "- Richtpreis: 10 kWp mit Speicher rund 15.000 bis 22.000 € vor Förderung",
        "- Finanzierung: Anlage gehört ab dem ersten Tag dem Kunden, ab 147 € im Monat inklusive Speicher (Beispielkondition)",
        "- Planung: Projektbericht mit 3D-Belegplan und Statikreport, Ausführung durch zertifizierte Fachkräfte",
        "- Geschäftsführung: Mario Zintl",
        "",
    ]
    for g, lines in groups.items():
        if lines:
            out += [f"## {g}", ""] + lines + [""]
    with open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"[OK ] llms.txt ({len(paths)} Seiten)")


def main():
    print("=== EBZ Website Build ===")
    theme.write_assets()
    write_favicon()
    copy_static()
    write_meta_files()
    errors = 0
    errors += len(home.build())
    errors += len(photovoltaik.build())
    errors += len(ueber_uns.build())
    errors += len(ratgeber.build())
    errors += len(finanzierung.build())
    errors += len(build_pages())
    write_sitemap()
    write_llms()
    print("=== Fertig ===")
    if errors:
        print(f"ACHTUNG: {errors} Validierungsfehler. Bitte beheben.")
        sys.exit(1)


if __name__ == "__main__":
    main()
