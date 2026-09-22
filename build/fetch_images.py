"""Laedt die Original-Bilder aus der Live-Mediathek nach out/assets/img/.

Einmalig ausfuehren (Schritt weg von wp-content). Danach liegen die Bilder
self-hosted im Repo und die Seiten sind unabhaengig von WordPress.

Aufruf: python3 build/fetch_images.py
"""

import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import IMG_SOURCES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "out")


def main():
    ok, fail = 0, 0
    for dest, src in IMG_SOURCES.items():
        target = os.path.join(OUT, dest.lstrip("/"))
        os.makedirs(os.path.dirname(target), exist_ok=True)
        # curl nutzt die System-Zertifikate (Python-urllib scheitert auf macOS an SSL)
        res = subprocess.run(
            ["curl", "-sSL", "--fail", "--max-time", "40", "-A", "Mozilla/5.0",
             "-o", target, src],
            capture_output=True, text=True,
        )
        if res.returncode == 0 and os.path.exists(target) and os.path.getsize(target) > 0:
            print(f"[OK ] {dest}  ({os.path.getsize(target)//1024} KB)")
            ok += 1
        else:
            print(f"[ERR] {dest}  <- {src}\n      {res.stderr.strip()}")
            fail += 1
    print(f"=== {ok} geladen, {fail} Fehler ===")


if __name__ == "__main__":
    main()
