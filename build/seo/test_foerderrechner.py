"""Testet die Rechenlogik des Foerderrechners (out/foerderrechner/index.html) mit festen Faellen.

Aufruf nach dem Build: python3 build/seo/test_foerderrechner.py   (braucht node). Exit 1 bei Abweichung.
Bei neuen Saetzen oder Fristen in build/pages/foerderrechner.py die Erwartungswerte hier mitziehen.
"""
import json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
html = open(os.path.join(ROOT, "out", "foerderrechner", "index.html"), encoding="utf-8").read()
core = re.search(r"/\*CALC\*/(.*?)/\*END\*/", html, re.S).group(1)

def inp(land="ktn", kwp=10, kwh=10, **sel):
    d = {"land": land, "kwp": kwp, "kwh": kwh, "pv": False, "sp": False, "wp": False, "ems": False, "balkon": False}
    d.update(sel)
    return d

# (Name, Eingabe, Datum, erwartet min, erwartet max, erwartet open)
CASES = [
    ("Kaernten 10 kWp + 10 kWh, Call laeuft", inp(pv=True, sp=True), "2026-10-10", 6000, 6000, False),
    ("Kaernten 10 kWp + 10 kWh, nach Bundes-Call", inp(pv=True, sp=True), "2026-10-23", 3000, 3000, False),
    ("Kaernten 10 kWp + 10 kWh, 2027", inp(pv=True, sp=True), "2027-01-02", 0, 0, False),
    ("Kaernten nur PV 10 kWp", inp(pv=True), "2026-10-10", 1500, 1500, False),
    ("Kaernten 15 kWp + 15 kWh (Kategorie B)", inp(kwp=15, kwh=15, pv=True, sp=True), "2026-10-10", 15 * 140 + 15 * 150 + 3000, 7350, False),
    ("Kaernten 4 kWp + 10 kWh (Pauschale nicht erfuellt)", inp(kwp=4, kwh=10, pv=True, sp=True), "2026-10-10", 600 + 1500, 2100, False),
    ("Kaernten 10 kWp + 4 kWh (Speicher zu klein fuer Bund und Land)", inp(kwh=4, pv=True, sp=True), "2026-10-10", 1500, 1500, False),
    ("Kaernten Speicher nachruesten 10 kWh", inp(sp=True), "2026-10-15", 1000, 1000, False),
    ("Kaernten Speicher nachruesten 4 kWh", inp(kwh=4, sp=True), "2026-10-15", 0, 0, False),
    ("Steiermark 10 kWp + 10 kWh", inp(land="stmk", pv=True, sp=True), "2026-10-10", 3000, 3000, False),
    ("Steiermark Waermepumpe (offen)", inp(land="stmk", wp=True), "2026-10-10", 0, 0, True),
    ("Kaernten Waermepumpe (bis 6.000)", inp(wp=True), "2026-10-10", 0, 6000, False),
    ("EMS", inp(ems=True), "2026-10-10", 0, 600, False),
    ("EMS nach Programmende", inp(ems=True), "2027-04-16", 0, 0, False),
    ("Balkonkraftwerk", inp(balkon=True), "2026-10-10", 0, 0, False),
    ("Tirol 10 kWp + 10 kWh", inp(land="tirol", pv=True, sp=True), "2026-10-10", 3000 + 1000, 3000 + 1250 + 1000, False),
    ("Oberoesterreich neu: kein Land beim Speicher", inp(land="ooe", pv=True, sp=True), "2026-10-10", 3000, 3000, False),
    ("Oberoesterreich Nachruestung 20 kWh (Deckel 2.250)", inp(land="ooe", kwh=20, sp=True), "2026-10-10", 2250, 2250, False),
    ("Burgenland neu, Call laeuft: Land zahlt nicht", inp(land="bgld", pv=True, sp=True), "2026-10-10", 3000, 3000, False),
    ("Burgenland neu, nach Call: Land 1.000", inp(land="bgld", pv=True, sp=True), "2026-10-23", 1000, 1000, False),
    ("Vorarlberg 10 kWp + 10 kWh (VKW 500)", inp(land="vbg", pv=True, sp=True), "2026-10-10", 3500, 3500, False),
    ("Ohne Bundesland: nur Bund", inp(land="", pv=True, sp=True), "2026-10-10", 3000, 3000, False),
    ("Alles in Kaernten", inp(pv=True, sp=True, wp=True, ems=True), "2026-10-10", 6000, 6000 + 6000 + 600, False),
    ("Speicher 60 kWh bei 20 kWp (Deckel 50 kWh)", inp(land="stmk", kwp=20, kwh=60, pv=True, sp=True), "2026-10-10", 2800 + 7500, 10300, False),
]
js = core + "\nvar out=[];" + json.dumps([[c[1], c[2]] for c in CASES]) + \
    ".forEach(function(c){var r=compute(c[0],c[1]);out.push([r.min,r.max,r.open,r.bonus,r.lines.length]);});console.log(JSON.stringify(out));"
res = json.loads(subprocess.run(["node", "-e", js], capture_output=True, text=True, check=True).stdout)
bad = 0
for (name, _i, datum, mn, mx, op), (rmn, rmx, rop, bonus, n) in zip(CASES, res):
    ok = (rmn, rmx, rop) == (mn, mx, op)
    bad += not ok
    print(f"[{'OK ' if ok else '!! '}] {name} ({datum}): {rmn} bis {rmx}, offen={rop}, Bonus {bonus:g}, {n} Zeilen"
          + ("" if ok else f"  ERWARTET {mn} bis {mx}, offen={op}"))
print("Abweichungen:", bad)
sys.exit(1 if bad else 0)
