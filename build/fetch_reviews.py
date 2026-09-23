"""Holt echte Google-Rezensionen von EBZ Energie via DataForSEO und cached sie.

Nutzt die DataForSEO Business Data API (Google Reviews, task-basiert). Filtert
auf 4 und 5 Sterne mit Text und schreibt build/data/reviews.json. Diese Datei
ist im Repo eingecheckt (Fallback), damit der Build auch ohne API-Zugang laeuft.

Zugangsdaten via Umgebungsvariablen (in GitHub Actions als Secrets):
  DATAFORSEO_LOGIN, DATAFORSEO_PASSWORD

Aufruf: python3 build/fetch_reviews.py
Ohne Zugangsdaten wird die vorhandene reviews.json unveraendert gelassen.
"""

import base64
import json
import os
import re
import subprocess
import sys
import time

MIN_CHARS = 40  # nur aussagekraeftige Rezensionen (wie bei Reinwald)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "build", "data", "reviews.json")

CID = "15592511037270601677"           # EBZ Energie GmbH (Google)
PLACE_ID = "ChIJN6ZIgHIEaQURzS_f_Cy6Y9g"
API = "https://api.dataforseo.com"


def _auth():
    login = os.environ.get("DATAFORSEO_LOGIN")
    pw = os.environ.get("DATAFORSEO_PASSWORD")
    if not (login and pw):
        return None
    return base64.b64encode(f"{login}:{pw}".encode()).decode()


def _call(auth, path, payload=None):
    args = ["curl", "-sS", "--max-time", "60",
            "-H", f"Authorization: Basic {auth}",
            "-H", "Content-Type: application/json", API + path]
    if payload is not None:
        args += ["-X", "POST", "-d", json.dumps(payload)]
    res = subprocess.run(args, capture_output=True, text=True)
    try:
        return json.loads(res.stdout)
    except json.JSONDecodeError:
        print("Antwort nicht lesbar:", res.stdout[:200], res.stderr[:200])
        return {}


def main():
    auth = _auth()
    if not auth:
        print("[skip] Keine DATAFORSEO_LOGIN/PASSWORD gesetzt. Cache bleibt unveraendert.")
        return 0

    payload = [{
        "cid": CID,
        "location_name": "Austria",
        "language_name": "German",
        "sort_by": "newest",
        "depth": 200,
    }]
    post = _call(auth, "/v3/business_data/google/reviews/task_post", payload)
    try:
        task_id = post["tasks"][0]["id"]
    except (KeyError, IndexError, TypeError):
        print("[err] task_post fehlgeschlagen:", json.dumps(post)[:300])
        return 1

    result = None
    for attempt in range(30):
        time.sleep(8)
        got = _call(auth, f"/v3/business_data/google/reviews/task_get/{task_id}")
        try:
            task = got["tasks"][0]
        except (KeyError, IndexError, TypeError):
            continue
        if task.get("result"):
            result = task["result"][0]
            break
        print(f"[wait] Rezensionen noch nicht bereit ({attempt + 1}/30)")

    if not result:
        print("[err] Keine Ergebnisse erhalten, Cache bleibt unveraendert.")
        return 1

    rating_value = (result.get("rating") or {}).get("value")
    total = result.get("reviews_count") or (result.get("rating") or {}).get("votes_count")
    items = result.get("items") or []

    def clean(s):
        # Gedankenstriche in echten Zitaten auf ASCII-Bindestrich normalisieren
        # (sonst schlaegt die Dash-Validierung an), Whitespace glaetten.
        s = re.sub(r"[–—]", "-", str(s))
        s = re.sub(r"[ \t]+", " ", s).strip()
        return s

    def truncate(s, n=220):
        s = s.strip()
        if len(s) <= n:
            return s
        return re.sub(r"\s+\S*$", "", s[:n]).rstrip() + "…"

    reviews = []
    for it in items:
        rv = (it.get("rating") or {}).get("value")
        text = clean(it.get("review_text") or "")
        if rv and rv >= 4 and len(text) >= MIN_CHARS:
            reviews.append({
                "author": it.get("profile_name") or "Google Nutzer",
                "rating": int(rv),
                "text": truncate(text),
                "date": (it.get("timestamp") or "")[:10],
            })

    data = {
        "rating": ("%.1f" % rating_value).replace(".", ",") if rating_value else "4,9",
        "count": total,
        "reviews": reviews,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[OK] {len(reviews)} Rezensionen (4-5 Sterne) gespeichert nach build/data/reviews.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
