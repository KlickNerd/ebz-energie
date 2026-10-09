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
# Zwei Fragen (Vorhaben, Ort) -> eine Ergebniskarte. Alle Texte sind Auszuege aus der Matrix oben
# (gleiche Quellen), es entstehen keine neuen Zahlen. Alle 18 Karten stehen im HTML, das Skript
# blendet nur ein und aus; ohne JavaScript bleibt die Standardkarte sichtbar.
VORHABEN = [
    ("pvsp", "☀", "PV mit Speicher"),
    ("pv", "◫", "PV ohne Speicher"),
    ("sp", "▮", "Speicher nachrüsten"),
    ("wp", "♨", "Wärmepumpe"),
    ("ems", "◎", "Energiemanagement"),
    ("balkon", "⌂", "Balkonkraftwerk"),
]
ORTE = [("ktn", "Kärnten", "in Kärnten"), ("stmk", "Steiermark", "in der Steiermark"),
        ("at", "Anderes Bundesland", "in anderen Bundesländern")]

BUND = {
    "pvsp": ("150 € je kWp bis 10 kWp (darüber 140 bis 120 €) und 150 € je kWh Speicher, plus 10 % Made-in-Europe-Bonus "
             "je Komponente. Antrag vor der Inbetriebnahme, aktueller Call bis 22. Oktober 2026."),
    "pv": ("150 € je kWp bis 10 kWp, darüber 140 bis 120 €, plus 10 % Made-in-Europe-Bonus je Komponente. Antrag vor der "
           "Inbetriebnahme, aktueller Call bis 22. Oktober 2026."),
    "sp": ("2026 keine Bundesförderung für die reine Nachrüstung: Der Speicherzuschuss gilt nur zusammen mit einer neuen "
           "oder erweiterten PV-Anlage. Ab 2027 soll die Nachrüstung laut BMWET förderbar werden."),
    "wp": ("Derzeit nichts: Kesseltausch (bis 7.500 €) und Sauber Heizen für Alle sind ausgeschöpft, neue Registrierungen "
           "sind nicht möglich. Ob 2027 ein neues Programm kommt, ist offen."),
    "ems": ("Klima- und Energiefonds: 50 % der Kosten, maximal 600 € je Haushalt (Betriebe 30 % bis 20.000 €). "
            "Registrierung vor der Rechnung, Programm bis 15. April 2027."),
    "balkon": "Kein EAG-Zuschuss für Steckeranlagen bis 800 Watt, weil der Einspeisezählpunkt fehlt.",
}
_GEMEINDE = "Keine Landesförderung; manche Gemeinden zahlen einen Zuschuss."
LAND = {
    ("pvsp", "ktn"): ("3.000 € Pauschale für Neuanlagen ab 5 kWp mit Speicher ab 5 kWh, zusätzlich zum Bund. Antrag nach "
                      "Fertigstellung, 12. Oktober bis 31. Dezember 2026."),
    ("pvsp", "stmk"): ("Keine Pauschale. Ökofonds bis 30 % ab 20 kWp, Gemeinden zahlen teils 200 bis 1.000 € oder einen "
                       "Speicherbonus. Der Sanierungsbonus-Call 2026 ist beendet."),
    ("pvsp", "at"): ("Tirol bis 125 € je kWp und 100 € je kWh Speicher. Oberösterreich, Burgenland und Vorarlberg haben "
                     "Speicherprogramme, die sich teils nicht mit dem Bund kombinieren lassen. Sonst gilt der Bund."),
    ("pv", "ktn"): "Die 3.000-€-Pauschale gibt es nur mit Speicher ab 5 kWh. Ohne Speicher bleibt die Bundesförderung.",
    ("pv", "stmk"): "Keine Pauschale. Ökofonds bis 30 % ab 20 kWp, Gemeinden zahlen teils 200 bis 1.000 €.",
    ("pv", "at"): ("Tirol bis 125 € je kWp. In Burgenland, Niederösterreich, Oberösterreich, Salzburg, Vorarlberg und Wien "
                   "gilt für Standard-Dachanlagen die Bundesförderung."),
    ("sp", "ktn"): ("1.000 € pauschal für die Nachrüstung ab 5 kWh an einer bestehenden Anlage. Antrag nach Fertigstellung, "
                    "bis 31. Dezember 2026."),
    ("sp", "stmk"): "Keine Landesförderung für die Nachrüstung; einzelne Gemeinden zahlen einen Speicherbonus.",
    ("sp", "at"): ("Oberösterreich 150 € je kWh bis 2.250 €, Burgenland 100 € je kWh bis 2.000 €, Tirol 100 € je kWh bis "
                   "1.000 €, Vorarlberg VKW-Bonus bis 500 €."),
    ("wp", "ktn"): ("35 % der förderbaren Kosten. Obergrenze laut Richtlinie 6.000 €, laut Berichten 2026 auf 3.000 € "
                    "angepasst; dazu 1.200 € Kelag-Prämie. Den aktuellen Stand klären wir vor dem Angebot mit dem Land."),
    ("wp", "stmk"): ("35 % der förderbaren Kosten für Eigenheime mit maximal zwei Wohnungen, Energieberatung kostenlos. "
                     "Den aktuellen Stand klären wir vor dem Angebot mit dem Land."),
    ("wp", "at"): ("Wien 35 % bis 8.000 €, Tirol 25 % plus 3.000 € Bonus, Salzburg rund 5.000 €, Burgenland 2.000 €, "
                   "Oberösterreich bis 1.700 €, Vorarlberg 1.000 €."),
    ("ems", "ktn"): "Keine eigene Landesförderung, es gilt der Klimafonds.",
    ("ems", "stmk"): ("Keine eigene Landesförderung. Im Ökofonds gibt es ab 20 kWp einen Bonus von 125 € je kWp für die "
                      "Einbindung in ein Energiesystem."),
    ("ems", "at"): "Keine eigene Landesförderung, es gilt der Klimafonds.",
    ("balkon", "ktn"): _GEMEINDE,
    ("balkon", "stmk"): _GEMEINDE,
    ("balkon", "at"): "Einzelne Länder und Gemeinden haben budgetierte Zuschüsse, die sich häufig ändern.",
}
# (Status, Kernzahl, Erlaeuterung)
_PVSP_SUB = "Beispiel: 10 kWp mit 10 kWh Speicher, inklusive Made-in-Europe-Bonus"
_PV_SUB = "Beispiel: 10 kWp ohne Speicher, je nach Made-in-Europe-Bonus"
SUMME = {
    ("pvsp", "ktn"): ("ok", "rund 6.450 €*", _PVSP_SUB),
    ("pvsp", "stmk"): ("ok", "rund 3.450 €*", _PVSP_SUB),
    ("pvsp", "at"): ("ok", "rund 3.450 €*", _PVSP_SUB + "; Landesförderung je nach Bundesland zusätzlich"),
    ("pv", "ktn"): ("ok", "1.500 bis 1.800 €*", _PV_SUB),
    ("pv", "stmk"): ("ok", "1.500 bis 1.800 €*", _PV_SUB),
    ("pv", "at"): ("ok", "1.500 bis 1.800 €*", _PV_SUB),
    ("sp", "ktn"): ("ok", "1.000 €", "Landespauschale für die Nachrüstung ab 5 kWh"),
    ("sp", "stmk"): ("end", "Derzeit keine", "2027 soll die Nachrüstung im Bund förderbar werden"),
    ("sp", "at"): ("part", "bis 2.250 €", "je nach Bundesland, Höchstwert Oberösterreich"),
    ("wp", "ktn"): ("part", "35 %", "der förderbaren Kosten vom Land, der Bund ist derzeit ausgeschöpft"),
    ("wp", "stmk"): ("part", "35 %", "der förderbaren Kosten vom Land, der Bund ist derzeit ausgeschöpft"),
    ("wp", "at"): ("part", "bis 8.000 €", "je nach Bundesland, Höchstwert Wien; der Bund ist derzeit ausgeschöpft"),
    ("ems", "ktn"): ("ok", "bis 600 €", "50 % der Kosten für Haushalte"),
    ("ems", "stmk"): ("ok", "bis 600 €", "50 % der Kosten für Haushalte"),
    ("ems", "at"): ("ok", "bis 600 €", "50 % der Kosten für Haushalte"),
    ("balkon", "ktn"): ("end", "Keine Förderung", "für Steckeranlagen bis 800 Watt"),
    ("balkon", "stmk"): ("end", "Keine Förderung", "für Steckeranlagen bis 800 Watt"),
    ("balkon", "at"): ("end", "Keine Förderung", "für Steckeranlagen bis 800 Watt"),
}
_MACHBAR = " Montiert wird in Kärnten und der Steiermark; andere Bundesländer prüfen wir auf Anfrage."
_SP_2027 = ("Speicher, die ab 1. November 2026 in Betrieb gehen, sollen laut BMWET 2027 im neuen Bundessystem "
            "beantragbar sein (geplant, nicht beschlossen).")
_WP_TIPP = ("Mit Photovoltaik sinken die Heizkosten deutlich. Die Öko-Sonderausgabenpauschale setzt eine ausbezahlte "
            "Bundesförderung voraus.")
_EMS_TIPP = "Erst registrieren, dann die Rechnung: Wer zuerst die Rechnung hat, verliert die Förderung."
_BALKON_TIPP = "Wer Förderung will, plant eine angemeldete Kleinanlage ab rund 3 kWp: 150 € je kWp vom Bund."
TIPP = {
    ("pvsp", "ktn"): "Reihenfolge beachten: Bundesantrag vor der Montage, Landesantrag danach. Beides bereiten wir vor.",
    ("pvsp", "stmk"): "Bundesantrag vor der Montage stellen. Welche Gemeinde zusätzlich fördert, prüfen wir für Sie.",
    ("pvsp", "at"): "Bundesantrag vor der Montage stellen." + _MACHBAR,
    ("pv", "ktn"): "Mit einem Speicher ab 5 kWh kommen 3.000 € vom Land und 150 € je kWh vom Bund dazu.",
    ("pv", "stmk"): "Mit einem Speicher zahlt der Bund zusätzlich 150 € je kWh.",
    ("pv", "at"): "Mit einem Speicher zahlt der Bund zusätzlich 150 € je kWh." + _MACHBAR,
    ("sp", "ktn"): _SP_2027, ("sp", "stmk"): _SP_2027, ("sp", "at"): _SP_2027,
    ("wp", "ktn"): _WP_TIPP, ("wp", "stmk"): _WP_TIPP, ("wp", "at"): _WP_TIPP + _MACHBAR,
    ("ems", "ktn"): _EMS_TIPP, ("ems", "stmk"): _EMS_TIPP, ("ems", "at"): _EMS_TIPP,
    ("balkon", "ktn"): _BALKON_TIPP, ("balkon", "stmk"): _BALKON_TIPP, ("balkon", "at"): _BALKON_TIPP,
}
DETAIL = {
    "pvsp": {"ktn": R_KTN, "stmk": R_STMK, "at": R_LAENDER},
    "pv": {"ktn": R_KTN, "stmk": R_STMK, "at": R_LAENDER},
    "sp": {"ktn": R_SPEICHER_KTN, "stmk": R_SPEICHER, "at": R_SPEICHER},
    "wp": {"ktn": R_WP_LAENDER, "stmk": R_WP_LAENDER, "at": R_WP_LAENDER},
    "ems": {"ktn": R_EMS, "stmk": R_EMS, "at": R_EMS},
    "balkon": {"ktn": R_BALKON, "stmk": R_BALKON, "at": R_BALKON},
}
BADGE = {"ok": ("ok", "Läuft"), "part": ("part", "Teilweise"), "end": ("end", "Derzeit nichts")}
DEFAULT = ("pvsp", "ktn")

FINDER_JS = """
(function(){
  var root = document.querySelector(".ff"); if(!root) return;
  var state = {v: root.getAttribute("data-v"), o: root.getAttribute("data-o")};
  var cards = root.querySelectorAll(".ff-result");
  function show(){
    cards.forEach(function(c){ c.classList.toggle("is-active", c.getAttribute("data-v") === state.v && c.getAttribute("data-o") === state.o); });
    root.querySelectorAll(".ff__opt").forEach(function(b){
      b.setAttribute("aria-pressed", String(state[b.getAttribute("data-group")] === b.getAttribute("data-val")));
    });
  }
  root.addEventListener("click", function(ev){
    var b = ev.target.closest(".ff__opt"); if(!b) return;
    state[b.getAttribute("data-group")] = b.getAttribute("data-val"); show();
  });
  show();
})();
"""


def _finder_section():
    from urllib.parse import quote

    def opts(group, items, active):
        return "".join(
            f'<button type="button" class="ff__opt" data-group="{group}" data-val="{val}" '
            f'aria-pressed="{"true" if val == active else "false"}">{ic}{label}</button>'
            for val, ic, label in items
        )

    v_items = [(k, f'<span class="ic" aria-hidden="true">{ic}</span>', label) for k, ic, label in VORHABEN]
    o_items = [(k, "", label) for k, label, _phrase in ORTE]
    results = ""
    for vk, _ic, vlabel in VORHABEN:
        for ok_, _olabel, ophrase in ORTE:
            status, zahl, sub = SUMME[(vk, ok_)]
            bcls, btxt = BADGE[status]
            title = f"{vlabel} {ophrase}"
            active = " is-active" if (vk, ok_) == DEFAULT else ""
            anliegen = quote(f"Förderung prüfen: {title}")
            results += f"""
        <article class="ff-result{active}" data-v="{vk}" data-o="{ok_}">
          <div>
            <span class="ff-badge ff-badge--{bcls}">{btxt}</span>
            <h3>{title}</h3>
            <p class="ff-sum"><b>{zahl}</b><span>{sub}</span></p>
          </div>
          <dl class="ff-rows">
            <div><dt>Vom Bund</dt><dd>{BUND[vk]}</dd></div>
            <div><dt>Vom Land</dt><dd>{LAND[(vk, ok_)]}</dd></div>
            <div><dt>Unser Tipp</dt><dd>{TIPP[(vk, ok_)]}</dd></div>
          </dl>
          <div class="ff-btns">
            <a class="btn btn--primary" href="/kontakt/?anliegen={anliegen}">Förderung für mein Projekt prüfen</a>
            {a(DETAIL[vk][ok_], 'Alle Details im Ratgeber', cls='btn btn--light')}
          </div>
        </article>"""
    return f"""
  <section class="ff-wrap" id="finder">
    <div class="wrap">
      <div class="ff" data-v="{DEFAULT[0]}" data-o="{DEFAULT[1]}">
        <div class="ff__step"><span class="ff__n" aria-hidden="true">1</span><span class="ff__q">Was planen Sie?</span>
          <div class="ff__opts" role="group" aria-label="Was planen Sie?">{opts("v", v_items, DEFAULT[0])}</div></div>
        <div class="ff__step"><span class="ff__n" aria-hidden="true">2</span><span class="ff__q">Wo steht das Gebäude?</span>
          <div class="ff__opts" role="group" aria-label="Wo steht das Gebäude?">{opts("o", o_items, DEFAULT[1])}</div></div>
        <div aria-live="polite">{results}
        </div>
        <p class="ff-foot">*Beispielrechnung, siehe unten. {STAND}, Beträge für private Anlagen.</p>
      </div>
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
            <div><dt>Made-in-Europe-Bonus, falls erfüllt</dt><dd>rund 450 €*</dd></div>
            <div><dt>Land Kärnten: Pauschale</dt><dd>3.000 €</dd></div>
            <div class="is-sum"><dt>Förderung gesamt</dt><dd>rund 6.450 €*</dd></div>
          </dl>
          <p class="form-note">Bei einem Richtpreis von rund 15.000 bis 22.000 € vor Förderung. In Kärnten maximal 50 %
          der Baukosten.</p>
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
        f"""
  <section class="page-hero fhero">
    <div class="page-hero__inner eg-reveal">
      <p class="eyebrow">Förderungen 2026</p>
      <h1>Welche Förderung bekommen Sie für Photovoltaik, Speicher und Wärmepumpe?</h1>
      <p class="lead">Zwei Klicks, und Sie sehen, was Bund und Land für Ihr Vorhaben zahlen.</p>
    </div>
  </section>""",
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
        f'<div class="wrap"><p class="form-note" style="padding:8px 0 40px">*Beispielrechnung: 10 kWp × 150 € plus '
        f'10 kWh × 150 € ergeben 3.000 € vom Bund; der Made-in-Europe-Bonus (10 % je Komponente, rund 450 € im Beispiel, '
        f'300 € ohne Speicher) gilt nur, wenn Module, Wechselrichter und Speicher die Kriterien erfüllen; dazu 3.000 € '
        f'Landespauschale Kärnten. Fördersätze und Fristen {STAND}, Länderdaten zum Teil Stand Mai bis Juni 2026; Angaben '
        f'zu 2027 laut BMWET geplant, nicht beschlossen. Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p></div>',
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
