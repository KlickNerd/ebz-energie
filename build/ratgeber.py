"""Baut alle Ratgeber aus build/content/ratgeber/*.py.

Jede Content-Datei stellt ein Dict ``ARTICLE`` bereit (Struktur: siehe article.py).
Aufruf einzeln:  python3 build/ratgeber.py
"""

import os
import sys
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import article

CONTENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content", "ratgeber")


def load_articles():
    arts = []
    for name in sorted(os.listdir(CONTENT_DIR)):
        if not name.endswith(".py") or name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(name[:-3], os.path.join(CONTENT_DIR, name))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        arts.append(mod.ARTICLE)
    return arts


def build():
    errors = []
    for art in load_articles():
        errors += article.render(art)
    return errors


if __name__ == "__main__":
    import theme
    theme.write_assets()
    errs = build()
    if errs:
        sys.exit(1)
