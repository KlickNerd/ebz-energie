"""Hub-Seite Förderungen 2026 (/foerderungen/).

Buendelt alle Foerderprogramme fuer Photovoltaik, Stromspeicher, Waermepumpe, Energiemanagement
und Balkonkraftwerk auf einer Seite: Status (laeuft / beendet / geplant), Matrix Technologie x
Fördergeber, Reihenfolge der Antraege, FAQ. Zahlen ausschliesslich aus dem Faktenblatt
build/seo/_fakten_2026-10.md und den Foerder-Ratgebern in build/content/ratgeber/
(photovoltaik_foerderung_oesterreich_2026, photovoltaik_landesfoerderungen, photovoltaik_foerderung_kaernten,
foerderung_photovoltaik_steiermark, foerderung_pv_speicher_kaernten, foerderung_fuer_pv_speicher,
balkonkraftwerk_foerderung_in_oesterreich, ems_foerderung, waermepumpenfoerderung_in_oesterreich,
landesfoerderungen_fuer_die_waermepumpe, unternehmensfoerderung_von_waermepumpen,
waermepumpe_steuerlich_absetzen_die_oeko_sonderausgabenpauschale_2026).
SEO-Luecke laut build/seo/_competitors.md (Cluster 2: pv foerderung oesterreich 2026 / eag foerdercall).
Keine Gedankenstriche, keine erfundenen Zahlen; Status immer mit Stand und Quelle.
"""

from common import IMG, NAP, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page
from layout import page
import components as C

PATH = "/foerderungen/"
TITLE = "Förderungen 2026: PV, Speicher, Wärmepumpe, EMS | EBZ"
DESC = ("Förderungen 2026 im Überblick: EAG 150 €/kWp und 150 €/kWh bis 22.10., Kärnten 3.000 € "
        "bis 31.12., EMS bis 600 €, Wärmepumpe Bund beendet. Stand Oktober.")

STAND = "Stand 10. Oktober 2026"

# Ratgeber-Pfade (alle in out/ gebaut)
R_BUND = "foerderung_at"
R_LAENDER = "/photovoltaik-landesfoerderungen/"
R_KTN = "foerderung_kaernten"
R_STMK = "foerderung_steiermark"
R_SPEICHER = "/foerderung-fuer-pv-speicher/"
R_SPEICHER_KTN = "/foerderung-pv-speicher-kaernten/"
R_BALKON = "/balkonkraftwerk-foerderung-in-oesterreich/"
R_EMS = "/ems-foerderung/"
R_WP_AT = "/waermepumpenfoerderung-in-oesterreich/"
R_WP_LAENDER = "/landesfoerderungen-fuer-die-waermepumpe/"
R_WP_BETRIEBE = "/unternehmensfoerderung-von-waermepumpen/"
R_WP_STEUER = "/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/"
R_SANIERUNG = "/sanierungsoffensive-2026/"
R_SAUBER = "/sauber-heizen-fuer-alle-2026/"
# (Pfad, Bundesland, Kurzstatus PV/Speicher, Kernmarkt?)  Kurzstatus = Auszug aus der Matrix unten
LAENDER = [
    (R_KTN, "Kärnten", "3.000 € Pauschale mit Speicher", True),
    (R_STMK, "Steiermark", "Sanierungsbonus und Ökofonds", True),
    ("/photovoltaik-foerderung-tirol/", "Tirol", "bis 125 €/kWp, Speicher 100 €/kWh", False),
    ("/photovoltaik-foerderung-oberoesterreich/", "Oberösterreich", "Speicher-Nachrüstung 150 €/kWh", False),
    ("/photovoltaik-foerderung-burgenland/", "Burgenland", "Speicher 100 €/kWh", False),
    ("/photovoltaik-foerderung-vorarlberg/", "Vorarlberg", "VKW-Speicherbonus", False),
    ("/photovoltaik-foerderung-salzburg/", "Salzburg", "Bundesförderung", False),
    ("/photovoltaik-foerderung-niederoesterreich/", "Niederösterreich", "Bundesförderung", False),
    ("/photovoltaik-foerderung-wien/", "Wien", "Stadt Wien oder Bund", False),
]


def _laender_section():
    home_cls = ' class="is-home"'
    tiles = "".join(
        f'<a href="{path}"{home_cls if home else ""}><b>{name}</b><small>{status}</small>'
        f'<span class="arr" aria-hidden="true">→</span></a>'
        for path, name, status, home in LAENDER
    )
    return f"""
  <section class="section section--tight" id="bundeslaender">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Landesförderung</p>
      <h2 class="center eg-reveal">Förderung nach Bundesland</h2>
      <p class="lead center eg-reveal" style="max-width:62ch;margin-inline:auto">Die Bundesförderung gilt überall,
      die Länder legen unterschiedlich viel dazu. Kärnten und die Steiermark sind unser Montagegebiet.</p>
      <div class="landgrid eg-reveal" style="margin-top:30px">{tiles}</div>
      <p class="landgrid-more eg-reveal">{a(R_LAENDER, 'Alle 9 Bundesländer im Vergleich →', cls='btn btn--ghost')}</p>
    </div>
  </section>"""


FAQ = [
    ("Kann ich die Bundesförderung mit einer Landesförderung kombinieren?",
     "In Kärnten ja: Die 3.000 Euro Landespauschale für PV mit Speicher wird laut Land ohne Anrechnung zusätzlich "
     "zum EAG-Investitionszuschuss gezahlt, gedeckelt mit 50 Prozent der Baukosten. In der Steiermark sind "
     "Sanierungsbonus und Ökofonds mit dem Bund kombinierbar. Ausnahmen: In Oberösterreich schließen sich "
     "EAG-Speicherzuschuss und Landes-Speicherförderung aus, im Burgenland zahlt das Land nur, wenn der Bund nicht "
     "möglich ist, in Wien gilt Stadt oder Bund."),
    ("Welche Fristen gelten im Herbst 2026?",
     "EAG-Investitionszuschuss: Antragstellung im dritten Fördercall bis 22. Oktober 2026, danach gibt es im alten "
     "System keinen Call mehr. Kärnten: zweiter Landes-Call vom 12. Oktober bis 31. Dezember 2026, Antrag nach "
     "Fertigstellung über die Förderplattform des Landes. EMS-Förderung des Klimafonds: Registrierung vor der "
     "Rechnung, Programm bis 15. April 2027. Wärmepumpe Bund: keine Frist mehr, die Programme sind ausgeschöpft "
     "(Stand 9. Oktober 2026, umweltfoerderung.at)."),
    ("Wer stellt die Förderanträge, EBZ oder ich?",
     "Antragsteller ist immer der Eigentümer der Anlage, also Sie. EBZ Energie bereitet alles vor: Zählpunkt, "
     "Ticket im EAG-Call, Antragsdaten, Fertigstellungsmeldung, Rechnung und Fotos für das Land, Registrierung beim "
     "Klimafonds. Sie bestätigen die Einreichung. Das gilt auch bei Finanzierung: Die Anlage gehört ab Tag 1 Ihnen, "
     "die Förderung geht auf Ihr Konto."),
    ("Was ändert sich 2027 bei der PV-Förderung?",
     "Laut BMWET soll der EAG-Investitionszuschuss ab 2027 zur Systemförderung werden: Gefördert wird das "
     "Zusammenspiel aus Speicher und intelligenter Steuerung, der Antrag wird nach Installation und Rechnung gestellt, "
     "ohne Fördercall und ohne Ticketziehung. Auch die Nachrüstung von Speicher und EMS soll förderbar werden. "
     "Projekte ab 1. November 2026 sollen 2027 im neuen System beantragbar sein. Höhe und Technikkriterien sind "
     "offen; alles ist geplant, nicht beschlossen."),
    ("Wird die Wärmepumpe 2026 überhaupt noch gefördert?",
     "Vom Bund derzeit nicht: Sanierungsoffensive mit Kesseltausch (bis 7.500 Euro) und Sauber Heizen für Alle sind "
     "seit Herbst 2026 ausgeschöpft, neue Registrierungen sind nicht möglich; bereits Registrierte können noch "
     "beantragen. Weiter laufen die Landesförderungen (Kärnten 35 Prozent, Steiermark 35 Prozent der förderbaren "
     "Kosten, Stand beim Land prüfen). Die Öko-Sonderausgabenpauschale (fünf Jahre je 400 Euro) setzt eine ausbezahlte "
     "Bundesförderung voraus und gilt damit nur für bereits Registrierte. Ob 2027 ein neues Bundesprogramm kommt, "
     "ist offen."),
    ("Welche Förderungen gibt es für Betriebe und Gemeinden?",
     "PV: EAG-Zuschuss in den Kategorien B bis D (140 bis 120 Euro je kWp, ab 20 kWp im Bieterverfahren) plus "
     "Speicher 150 Euro je kWh; Kärnten fördert betriebliche Eigenverbrauchsanlagen mit bis zu 200 Euro je kWp, die "
     "Steiermark über den Ökofonds mit bis zu 30 Prozent ab 20 kWp. EMS: 30 Prozent bis 20.000 Euro je Standort "
     "(Großunternehmen 20 Prozent). Wärmepumpe: KPC-Programm für Betriebe bis 7.500 Euro unter 50 kW und 12.000 Euro "
     "bei 50 bis 100 kW, maximal 50 Prozent, Antrag bis sechs Monate nach Rechnung."),
]


def _table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    body = ""
    for r in rows:
        tds = "".join(f'<td class="hl">{c}</td>' if i == 0 else f"<td>{c}</td>" for i, c in enumerate(r))
        body += f"<tr>{tds}</tr>"
    return (f'<div class="art-tablewrap eg-reveal"><table class="art-table"><thead><tr>{th}</tr></thead>'
            f"<tbody>{body}</tbody></table></div>")


def _cell(text, link_key, link_text="Details"):
    return f"{text}<br>{a(link_key, link_text + ' <span aria-hidden=\"true\">→</span>')}"


def _matrix_section():
    lead = (f"Fünf Technologien, vier Fördergeber, alle Beträge für private Anlagen ({STAND}).")
    rows = [
        ("Photovoltaik",
         _cell("150 €/kWp bis 10 kWp, darüber 140 bis 120 €/kWp, 10 % Made-in-Europe-Bonus. <b>Läuft:</b> Antrag bis 22.10.2026", R_BUND),
         _cell("<b>3.000 € Pauschale</b> für Neuanlagen ab 5 kWp mit Speicher ab 5 kWh. <b>Läuft:</b> 12.10. bis 31.12.2026", R_KTN),
         _cell("Keine Pauschale. Sanierungsbonus bis 15 % (Call 1.4. bis 15.5.2026 beendet), Ökofonds bis 30 % ab 20 kWp, Gemeinden 200 bis 1.000 €", R_STMK),
         _cell("Tirol bis 125 €/kWp; Burgenland, Niederösterreich, Oberösterreich, Salzburg, Vorarlberg und Wien: nur Bund für Standard-Dachanlagen", R_LAENDER)),
        ("Stromspeicher",
         _cell("150 €/kWh bis 50 kWh, nur gemeinsam mit neuer oder erweiterter PV-Anlage. <b>Läuft</b> bis 22.10.2026", R_SPEICHER),
         _cell("In der 3.000-€-Pauschale enthalten; <b>Nachrüstung 1.000 €</b> ab 5 kWh an Bestandsanlagen. <b>Läuft</b> bis 31.12.2026", R_SPEICHER_KTN),
         _cell("Nur Bund; einzelne Gemeinden zahlen einen Speicherbonus", R_STMK),
         _cell("Oberösterreich 150 €/kWh Nachrüstung bis 2.250 €, Burgenland 100 €/kWh bis 2.000 €, Tirol 100 €/kWh bis 1.000 €, Vorarlberg VKW-Bonus bis 500 €; sonst nur Bund", R_LAENDER)),
        ("Wärmepumpe",
         _cell("<b>Beendet:</b> Kesseltausch bis 7.500 € und Sauber Heizen für Alle ausgeschöpft. Die Öko-Sonderausgabenpauschale (5 Jahre je 400 €) setzt eine ausbezahlte Bundesförderung voraus", R_WP_AT),
         _cell("35 % der förderbaren Kosten, Obergrenze 6.000 € laut Richtlinie (laut Berichten 2026: 3.000 €), plus 1.200 € Kelag-Prämie. Stand beim Land prüfen", R_WP_LAENDER),
         _cell("35 % der förderbaren Kosten für Eigenheime mit maximal zwei Wohnungen, Energieberatung kostenlos", R_WP_LAENDER),
         _cell("Wien 35 % bis 8.000 €, Tirol 25 % plus 3.000 € Bonus, Salzburg rund 5.000 €, Burgenland 2.000 €, Vorarlberg 1.000 €, Oberösterreich bis 1.700 €", R_WP_LAENDER)),
        ("Energiemanagement (EMS)",
         _cell("Klimafonds: <b>50 % bis 600 €</b> für Haushalte, 30 % bis 20.000 € für Betriebe. <b>Läuft</b> bis 15.4.2027, Registrierung vor Rechnung", R_EMS),
         _cell("Nur Bund", R_EMS),
         _cell("Nur Bund; im Ökofonds ab 20 kWp gibt es 125 €/kWp Bonus für die Einbindung in ein Energiesystem", R_STMK),
         _cell("Nur Bund", R_EMS)),
        ("Balkonkraftwerk",
         _cell("Kein EAG-Zuschuss für Steckeranlagen bis 800 W (kein Einspeisezählpunkt). Angemeldete Kleinanlagen ab rund 3 kWp: 150 €/kWp", R_BALKON),
         _cell("Keine Landesförderung; Gemeinde prüfen", R_BALKON),
         _cell("Keine Landesförderung; Gemeinde prüfen", R_BALKON),
         _cell("Einzelne Länder und Gemeinden mit budgetierten Zuschüssen, Programme ändern sich häufig", R_BALKON)),
    ]
    table = _table(["Technologie", "Bund (EAG, Klimafonds, KPC)", "Kärnten", "Steiermark", "Andere Bundesländer"], rows)
    return f"""
  <section class="section section--tight" style="background:#fff;border-block:1px solid var(--line)" id="matrix">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Für alle, die alles sehen wollen</p>
      <h2 class="center eg-reveal">Die komplette Fördermatrix 2026</h2>
      <p class="lead center eg-reveal" style="max-width:64ch;margin-inline:auto">{lead}</p>
      <details class="fall">
        <summary>Alle Förderungen in einer Tabelle</summary>
        {table}
        <p class="form-note center">Quellen: EAG-Abwicklungsstelle, Land Kärnten, Land Steiermark, Klima- und Energiefonds,
        umweltfoerderung.at, Landesförderstellen (Länderdaten Stand Mai bis Oktober 2026). Änderungen durch die Fördergeber vorbehalten.</p>
      </details>
    </div>
  </section>"""


# --- Foerder-Finder ---------------------------------------------------------
# Zwei Fragen im Hero (Vorhaben, Ort) -> EINE Ergebniskarte mit einer Rechenzeile:
# Bund + Land = Foerderung. Zahlen sind Auszuege aus der Matrix (gleiche Quellen), ohne
# Made-in-Europe-Bonus gerechnet. Fristen stehen bewusst nicht in der Karte, sondern in der
# Statusleiste darunter und in den Ratgebern. Alle 18 Karten stehen im HTML, das Skript blendet
# nur ein und aus; ohne JavaScript bleibt die Standardkarte sichtbar.
VORHABEN = [
    ("pvsp", "PV mit Speicher"),
    ("pv", "PV ohne Speicher"),
    ("sp", "Speicher nachrüsten"),
    ("wp", "Wärmepumpe"),
    ("ems", "Energiemanagement"),
    ("balkon", "Balkonkraftwerk"),
]
ORTE = [("ktn", "Kärnten", "in Kärnten", "Land Kärnten"),
        ("stmk", "Steiermark", "in der Steiermark", "Land Steiermark"),
        ("at", "Anderes Bundesland", "in anderen Bundesländern", "Bundesland")]

_BONUS = " Mit Made-in-Europe-Bonus sind bis zu 450 € mehr möglich."
_SP_BUND = ("Der Bund fördert 2026 nur Speicher zusammen mit einer neuen oder erweiterten PV-Anlage. "
            "Ab 2027 soll die Nachrüstung förderbar werden (laut BMWET geplant).")
_WP_BUND = "Die Bundesförderung für Wärmepumpen ist derzeit ausgeschöpft."
_EMS = "Erst beim Klimafonds registrieren, dann die Rechnung ausstellen lassen. Betriebe erhalten 30 % bis 20.000 €."
_BALKON = ("Steckeranlagen haben keinen Einspeisezählpunkt und bekommen deshalb keinen Zuschuss. "
           "Eine angemeldete Kleinanlage ab rund 3 kWp erhält 150 € je kWp vom Bund.")
_B_PVSP, _B_PV = "Beispiel: 10 kWp mit 10 kWh Speicher", "Beispiel: 10 kWp ohne Speicher"
_B_SP, _B_WP = "Speicher an einer bestehenden PV-Anlage", "Anteil an den förderbaren Kosten"
_B_EMS, _B_BALKON = "50 % der Kosten, für einen Haushalt", "Steckeranlage bis 800 Watt"

# (Vorhaben, Ort): (Status, Basis, Bund, Land, Summe, Hinweis, Ratgeber)
ERGEBNIS = {
    ("pvsp", "ktn"): ("ok", _B_PVSP, "3.000 €", "3.000 €", "6.000 €",
                      "Reihenfolge beachten: Bund vor der Montage beantragen, Land danach." + _BONUS, R_KTN),
    ("pvsp", "stmk"): ("ok", _B_PVSP, "3.000 €", "0 €", "3.000 €",
                       "Die Steiermark hat keine Pauschale; manche Gemeinden zahlen 200 bis 1.000 € dazu." + _BONUS, R_STMK),
    ("pvsp", "at"): ("ok", _B_PVSP, "3.000 €", "je nach Land", "ab 3.000 €",
                     "Tirol legt bis 125 € je kWp dazu, Oberösterreich, Burgenland und Vorarlberg fördern den Speicher.",
                     R_LAENDER),
    ("pv", "ktn"): ("ok", _B_PV, "1.500 €", "0 €", "1.500 €",
                    "Kärnten zahlt die Pauschale nur mit Speicher ab 5 kWh. Mit 10 kWh Speicher wären es im Beispiel 6.000 €.",
                    R_KTN),
    ("pv", "stmk"): ("ok", _B_PV, "1.500 €", "0 €", "1.500 €",
                     "Mit einem Speicher zahlt der Bund zusätzlich 150 € je kWh, im Beispiel mit 10 kWh also 3.000 €.", R_STMK),
    ("pv", "at"): ("ok", _B_PV, "1.500 €", "je nach Land", "ab 1.500 €",
                   "Tirol legt bis 125 € je kWp dazu. In den meisten anderen Ländern gilt für Dachanlagen die Bundesförderung.",
                   R_LAENDER),
    ("sp", "ktn"): ("ok", "Speicher ab 5 kWh an einer bestehenden PV-Anlage", "0 €", "1.000 €", "1.000 €",
                    _SP_BUND, R_SPEICHER_KTN),
    ("sp", "stmk"): ("end", _B_SP, "0 €", "0 €", "0 €",
                     _SP_BUND + " Einzelne Gemeinden zahlen einen Speicherbonus.", R_SPEICHER),
    ("sp", "at"): ("part", _B_SP, "0 €", "bis 2.250 €", "bis 2.250 €",
                   "Höchstwert Oberösterreich (150 € je kWh). Burgenland bis 2.000 €, Tirol bis 1.000 €, Vorarlberg bis 500 €.",
                   R_SPEICHER),
    ("wp", "ktn"): ("part", _B_WP, "0 €", "35 %", "35 %",
                    _WP_BUND + " Kärnten deckelt den Betrag; den aktuellen Stand klären wir vor dem Angebot mit dem Land.",
                    R_WP_LAENDER),
    ("wp", "stmk"): ("part", _B_WP, "0 €", "35 %", "35 %",
                     _WP_BUND + " Die Steiermark fördert Eigenheime mit maximal zwei Wohnungen; den Stand klären wir vor dem Angebot.",
                     R_WP_LAENDER),
    ("wp", "at"): ("part", "je nach Bundesland", "0 €", "bis 8.000 €", "bis 8.000 €",
                   _WP_BUND + " Höchstwert Wien (35 %), Tirol 25 % plus 3.000 €, Salzburg rund 5.000 €.", R_WP_LAENDER),
    ("ems", "ktn"): ("ok", _B_EMS, "bis 600 €", "0 €", "bis 600 €", _EMS, R_EMS),
    ("ems", "stmk"): ("ok", _B_EMS, "bis 600 €", "0 €", "bis 600 €", _EMS, R_EMS),
    ("ems", "at"): ("ok", _B_EMS, "bis 600 €", "0 €", "bis 600 €", _EMS, R_EMS),
    ("balkon", "ktn"): ("end", _B_BALKON, "0 €", "0 €", "0 €", _BALKON, R_BALKON),
    ("balkon", "stmk"): ("end", _B_BALKON, "0 €", "0 €", "0 €", _BALKON, R_BALKON),
    ("balkon", "at"): ("end", _B_BALKON, "0 €", "0 €", "0 €", _BALKON, R_BALKON),
}
BADGE = {"ok": "Läuft", "part": "Bund pausiert, Land läuft", "end": "Derzeit keine Förderung"}
DEFAULT = ("pvsp", "ktn")

FINDER_JS = """
(function(){
  var card = document.querySelector(".ff-card"); if(!card) return;
  var state = {v: card.getAttribute("data-v"), o: card.getAttribute("data-o")};
  var cards = card.querySelectorAll(".ff-result");
  var opts = document.querySelectorAll(".ff__opt");
  function show(){
    cards.forEach(function(c){ c.classList.toggle("is-active", c.getAttribute("data-v") === state.v && c.getAttribute("data-o") === state.o); });
    opts.forEach(function(b){ b.setAttribute("aria-pressed", String(state[b.getAttribute("data-group")] === b.getAttribute("data-val"))); });
  }
  function reveal(){
    var r = card.getBoundingClientRect();
    if(r.top < window.innerHeight - 220) return;
    var calm = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    window.scrollTo({top: window.pageYOffset + r.top - 96, behavior: calm ? "auto" : "smooth"});
  }
  opts.forEach(function(b){ b.addEventListener("click", function(){
    var g = b.getAttribute("data-group");
    state[g] = b.getAttribute("data-val"); show();
    if(g === "o") reveal();
  }); });
  show();
})();
"""


def _opts(group, items, active):
    return "".join(
        f'<button type="button" class="ff__opt" data-group="{group}" data-val="{val}" '
        f'aria-pressed="{"true" if val == active else "false"}">{label}</button>'
        for val, label in items
    )


def _hero_section():
    return f"""
  <section class="page-hero fhero">
    <div class="page-hero__inner">
      <p class="eyebrow">Förderungen 2026</p>
      <h1>Förderungen für Photovoltaik, Speicher und Wärmepumpe</h1>
      <p class="lead">Zwei Klicks, und Sie sehen, was Bund und Land für Ihr Vorhaben zahlen.</p>
      <div class="ffq">
        <p class="ffq__label" id="ffq-v">1 · Was planen Sie?</p>
        <div class="ffq__opts ffq__opts--6" role="group" aria-labelledby="ffq-v">{_opts("v", VORHABEN, DEFAULT[0])}</div>
      </div>
      <div class="ffq">
        <p class="ffq__label" id="ffq-o">2 · Wo steht das Gebäude?</p>
        <div class="ffq__opts" role="group" aria-labelledby="ffq-o">{_opts("o", [(k, l) for k, l, _p, _n in ORTE], DEFAULT[1])}</div>
      </div>
    </div>
  </section>"""


def _finder_section():
    from urllib.parse import quote
    results = ""
    for vk, vlabel in VORHABEN:
        for ok_, _olabel, ophrase, landname in ORTE:
            status, basis, bund, land, summe, hinweis, detail = ERGEBNIS[(vk, ok_)]
            title = f"{vlabel} {ophrase}"
            active = " is-active" if (vk, ok_) == DEFAULT else ""
            anliegen = quote(f"Förderung prüfen: {title}")
            # Ohne Foerderung keine Rechenzeile: "0 + 0 = 0" hilft niemandem.
            eq = "" if summe == "0 €" else f"""          <div class="ff-eq">
            <div class="ff-eq__cell"><span>Bund</span><b>{bund}</b></div>
            <span class="ff-eq__op" aria-hidden="true">+</span>
            <div class="ff-eq__cell"><span>{landname}</span><b>{land}</b></div>
            <span class="ff-eq__op" aria-hidden="true">=</span>
            <div class="ff-eq__cell ff-eq__cell--sum"><span>Ihre Förderung</span><b>{summe}</b></div>
          </div>"""
            results += f"""
        <article class="ff-result{active}" data-v="{vk}" data-o="{ok_}">
          <span class="ff-badge ff-badge--{status}">{BADGE[status]}</span>
          <p class="ff-title">{title}</p>
          <p class="ff-sub">{basis}</p>
{eq}
          <p class="ff-hint">{hinweis}</p>
          <div class="ff-actions">
            <a class="btn btn--primary" href="/kontakt/?anliegen={anliegen}">Förderung für mein Projekt prüfen</a>
            {a(detail, 'Details im Ratgeber <span aria-hidden="true">→</span>', cls='ff-more')}
          </div>
        </article>"""
    return f"""
  <section class="ff-wrap" id="finder">
    <div class="wrap">
      <div class="ff-card" data-v="{DEFAULT[0]}" data-o="{DEFAULT[1]}" aria-live="polite">{results}
      </div>
      <p class="ff-foot">Beträge für private Anlagen, ohne Made-in-Europe-Bonus gerechnet. {STAND}.</p>
    </div>
  </section>
  <script>{FINDER_JS}</script>"""


def _status_section():
    return f"""
  <section class="section section--tight">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Was läuft gerade</p>
      <h2 class="center eg-reveal">Förderstatus im Oktober 2026</h2>
      <div class="fstatus eg-reveal" style="margin-top:28px">
        <div><b><span class="dot dot--ok"></span>Läuft</b>
          <p>EAG-Zuschuss des Bundes für PV und Speicher (Antrag bis 22. Oktober 2026), Landespauschale Kärnten
          (12. Oktober bis 31. Dezember 2026), EMS-Förderung des Klimafonds (bis 15. April 2027).</p></div>
        <div><b><span class="dot dot--end"></span>Beendet</b>
          <p>Bundesförderung für Wärmepumpen: Kesseltausch und Sauber Heizen für Alle sind ausgeschöpft.
          Steirischer Sanierungsbonus: Call 2026 abgeschlossen.</p></div>
        <div><b><span class="dot dot--plan"></span>Geplant ab 2027</b>
          <p>Systemförderung für Speicher mit intelligenter Steuerung, Antrag nach der Installation statt im
          Fördercall (laut BMWET, noch nicht beschlossen).</p></div>
      </div>
      <p class="form-note center eg-reveal" style="margin-top:16px">Quellen: EAG-Abwicklungsstelle, Land Kärnten,
      Klima- und Energiefonds, umweltfoerderung.at, BMWET. {STAND}.</p>
    </div>
  </section>"""


def _beispiel_section():
    return f"""
  <section class="section" id="beispiel">
    <div class="wrap">
      <div class="split">
        <div class="panel eg-reveal">
          <p class="eyebrow">Ein Beispiel</p>
          <h2 style="font-size:clamp(1.4rem,2.4vw,1.8rem)">10 kWp mit 10 kWh Speicher in Kärnten</h2>
          <dl class="fcalc">
            <div><dt>Bund: Photovoltaik, 10 kWp × 150 €</dt><dd>1.500 €</dd></div>
            <div><dt>Bund: Speicher, 10 kWh × 150 €</dt><dd>1.500 €</dd></div>
            <div><dt>Land Kärnten: Pauschale</dt><dd>3.000 €</dd></div>
            <div class="is-sum"><dt>Förderung gesamt</dt><dd>6.000 €</dd></div>
          </dl>
          <p class="form-note">Mit Made-in-Europe-Bonus rund 450 € mehr*. Richtpreis der Anlage rund 15.000 bis 22.000 €
          vor Förderung; Kärnten fördert maximal 50 % der Baukosten.</p>
        </div>
        <div class="panel panel--dark eg-reveal">
          <p class="eyebrow" style="color:var(--amber)">Service inklusive</p>
          <h2 style="color:#fff;font-size:clamp(1.4rem,2.4vw,1.8rem)">Wir übernehmen die Anträge</h2>
          <p style="color:#c6dbe2">Sie bleiben Antragsteller, das Geld kommt auf Ihr Konto, auch bei Finanzierung.
          Den Papierkram machen wir.</p>
          <ul class="checklist">
            <li>Förderprüfung vor dem Angebot, Beträge im Projektbericht mit 3D-Belegplan und Statikreport</li>
            <li>Ticket, Antrag und Fertigstellungsmeldung bereiten wir vor, Sie bestätigen</li>
            <li>Reihenfolge im Blick: Bund vor der Montage, Land danach</li>
          </ul>
          <div class="hero__cta" style="margin-top:22px">{a('kontakt', 'Kostenlose Förderprüfung', cls='btn btn--primary')}</div>
        </div>
      </div>
    </div>
  </section>"""


def build():
    body = "".join([
        _hero_section(),
        _finder_section(),
        _status_section(),
        C.steps_section(
            eyebrow="So kommen Sie zur Förderung",
            h2="Vier Schritte, die Reihenfolge entscheidet",
            steps=[
                ("Förderung prüfen",
                 "Wir klären vor dem Angebot, welche Programme zu Dach, Heizung und Bundesland passen.",
                 "vor dem Angebot"),
                ("Bund: Antrag vor der Montage",
                 "Zählpunkt, Ticket, Antrag. Montiert wird erst danach, sonst verfällt der Bundeszuschuss.",
                 "vor der Montage"),
                ("Land: Antrag nach der Fertigstellung",
                 "Kärnten zahlt nach Rechnung und Fertigstellungsmeldung, ohne den Bund anzurechnen.",
                 "nach der Montage"),
                ("Energiemanagement: erst registrieren",
                 "Beim Klimafonds registrieren, dann erst die Rechnung ausstellen lassen.",
                 "vor der Rechnung"),
            ],
        ),
        _beispiel_section(),
        _matrix_section(),
        _laender_section(),
        C.faq_section(FAQ),
        C.linkgrid_section("Weiterlesen", [
            ("photovoltaik", "Photovoltaikanlage mit Speicher"),
            ("waermepumpe", "Wärmepumpe"),
            ("finanzierung", "Finanzierung: Eigentum ab Tag 1"),
            ("solarrechner", "Solarrechner: Kosten und Ertrag"),
        ]),
        C.contact_section(
            "Welche Förderung passt zu Ihrem Projekt?",
            "Sagen Sie uns Bundesland, Dach und Heizung. Wir sagen Ihnen, welche Programme laufen und wie wir einreichen.",
            page_label="Förderungen",
        ),
        C.finalcta(
            "Förderung prüfen lassen, bevor eine Frist verfällt",
            "Kostenlose Erstberatung mit Förderprüfung. Wir melden uns innerhalb eines Werktags.",
            trust=[(f"{NAP['rating']} auf Google", True), ("300+ Projekte", False),
                   ("Anträge inklusive", False), ("Antwort in einem Werktag", False)],
        ),
        f'<div class="wrap"><p class="form-note" style="padding:8px 0 40px">*Made-in-Europe-Bonus: 10 % je Komponente auf den '
        f'Bundeszuschuss, im Beispiel rund 450 €, nur wenn Module, Wechselrichter und Speicher die Kriterien erfüllen. '
        f'Fördersätze und Fristen {STAND}, Länderdaten zum Teil Stand Mai bis Juni 2026; Angaben zu 2027 laut BMWET geplant, '
        f'nicht beschlossen. Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p></div>',
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ), og_image=IMG["foerderung"])
    return write_page("foerderungen/index.html", html)


if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import theme
    theme.write_assets()
    build()
