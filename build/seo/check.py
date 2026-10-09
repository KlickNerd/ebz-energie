"""Prueft nach dem Build, ob die Briefing-Keywords im sichtbaren Text der Seite vorkommen.

Aufruf: python3 build/seo/check.py   (nach python3 build/build_all.py)
"""
import glob, json, os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEO = os.path.join(ROOT, "build", "seo")


def norm(s):
    s = s.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    s = re.sub(r"[-\u2011/]", " ", s)  # Bindestrich-Varianten (Photovoltaik-Beratung) gelten als Treffer
    return re.sub(r"\s+", " ", s)


def page_text(path):
    f = os.path.join(ROOT, "out", path.strip("/"), "index.html")
    if not os.path.exists(f):
        return None, None
    h = open(f, encoding="utf-8").read()
    head = h.split("</head>")[0]
    body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", h.split("</head>")[1], flags=re.S)
    body = re.sub(r"<footer.*", " ", body, flags=re.S)  # Footer nicht zaehlen
    return norm(head), norm(html.unescape(re.sub(r"<[^>]+>", " ", body)))


def main():
    total_missing = 0
    for f in sorted(glob.glob(os.path.join(SEO, "*.json"))):
        name = os.path.basename(f)
        if name.startswith("_"):
            continue
        b = json.load(open(f, encoding="utf-8"))
        paths = b.get("path") if isinstance(b.get("path"), list) else ([b.get("path")] if b.get("path") else [])
        for p in paths:
            head, body = page_text(p)
            if body is None:
                print(f"[--] {p}: nicht gebaut"); continue
            prim = b.get("primary", {}).get("keyword", "")
            secs = [s.get("keyword", "") for s in b.get("secondary", [])]
            sem = b.get("semantic", [])
            miss_sec = [k for k in secs if k and norm(k) not in body]
            miss_sem = [k for k in sem if k and norm(k) not in body]
            prim_ok = bool(prim) and norm(prim) in body
            prim_title = bool(prim) and norm(prim) in head
            flag = "OK " if prim_ok and not miss_sec and len(miss_sem) <= len(sem) * 0.3 else "!! "
            total_missing += len(miss_sec) + (0 if prim_ok else 1)
            print(f"[{flag}] {p}  primaer={'ja' if prim_ok else 'NEIN'}({'Title ja' if prim_title else 'Title nein'})  "
                  f"sekundaer fehlt={len(miss_sec)}/{len(secs)}  semantisch fehlt={len(miss_sem)}/{len(sem)}")
            for k in miss_sec: print(f"       sek: {k}")
            for k in miss_sem[:8]: print(f"       sem: {k}")
    print("fehlend gesamt (primaer+sekundaer):", total_missing)


if __name__ == "__main__":
    main()
