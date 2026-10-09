"""Leistungs-, Standort- und Unternehmensseiten duerfen keine Foerderfristen/Call-Termine tragen.

Fristen gehoeren in den Hub /foerderungen/ und die Foerder-Ratgeber (monatlich gepflegt).
Aufruf: python3 build/seo/check_fristen.py   (nach dem Build). Exit 1 bei Treffern.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Seiten, die Fristen tragen DUERFEN
ALLOW = {"/foerderungen/", "/foerderrechner/", "/ratgeber/"}
# Nur Foerderfristen: Call-Begriffe und die bekannten Stichtage (Liste bei neuen Calls erweitern).
# Rechts-/Historiendaten (USt-Nullsatz 1.4.2025, Zustimmungsfiktion 1.9.2024, ElWG 1.10.2026) sind erlaubt.
PAT = re.compile(
    r"(F(ö|oe)rdercalls?|letzte[rn]?\s+Call|Call\s+bis|Einreichfrist|Registrierungsschluss|Einreichzeitraum|"
    r"\b(8|9|12|22)\.\s?(10\.|Oktober)\s?2026|31\.\s?(12\.|Dezember)\s?2026|15\.\s?(4\.|04\.|April)\s?2027|"
    r"bis\s+(22\.10\.|31\.12\.)2026|bis\s+15\.0?4\.2027)", re.I)


def main():
    ratgeber_slugs = {f[:-3].replace("_", "-") for f in os.listdir(os.path.join(ROOT, "build", "content", "ratgeber")) if f.endswith(".py")}
    hits = 0
    for f in sorted(glob.glob(os.path.join(ROOT, "out", "**", "index.html"), recursive=True)):
        rel = os.path.relpath(os.path.dirname(f), os.path.join(ROOT, "out")).replace(os.sep, "/")
        path = "/" if rel == "." else f"/{rel}/"
        if path in ALLOW or rel in ratgeber_slugs:
            continue
        h = open(f, encoding="utf-8").read()
        body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", h.split("</head>")[1], flags=re.S)
        text = re.sub(r"<[^>]+>", " ", body)
        found = {m.group(0).strip() for m in PAT.finditer(text)}
        if found:
            hits += 1
            print(f"[!!] {path}: {sorted(found)[:6]}")
    print("Seiten mit Fristen:", hits)
    sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
