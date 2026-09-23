"""Baut die komplette Website nach out/.

Aufruf:  python3 build/build_all.py
Ergebnis: out/ enthaelt deploybare statische Seiten + assets/.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import theme
import home
import photovoltaik
import ueber_uns

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
    print("=== Fertig ===")
    if errors:
        print(f"ACHTUNG: {errors} Validierungsfehler. Bitte beheben.")
        sys.exit(1)


if __name__ == "__main__":
    main()
