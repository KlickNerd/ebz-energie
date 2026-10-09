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
LAENDER = [
    (R_KTN, "Kärnten: 3.000 € Pauschale"),
    (R_STMK, "Steiermark: Sanierungsbonus und Ökofonds"),
    ("/photovoltaik-foerderung-wien/", "Wien"),
    ("/photovoltaik-foerderung-niederoesterreich/", "Niederösterreich"),
    ("/photovoltaik-foerderung-oberoesterreich/", "Oberösterreich"),
    ("/photovoltaik-foerderung-salzburg/", "Salzburg"),
    ("/photovoltaik-foerderung-tirol/", "Tirol"),
    ("/photovoltaik-foerderung-vorarlberg/", "Vorarlberg"),
    ("/photovoltaik-foerderung-burgenland/", "Burgenland"),
    (R_LAENDER, "Alle 9 Bundesländer im Vergleich"),
]

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
     "Kosten, Stand beim Land prüfen) und die Öko-Sonderausgabenpauschale mit fünf Jahren je 400 Euro. Ob 2027 ein "
     "neues Bundesprogramm kommt, ist offen."),
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
    lead = (f"Eine Zeile je Technologie, eine Spalte je Fördergeber; Beträge für private Anlagen ({STAND}), "
            "Programme für Betriebe stehen in den FAQ.")
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
         _cell("<b>Beendet:</b> Kesseltausch bis 7.500 € und Sauber Heizen für Alle ausgeschöpft. Weiter gültig: Öko-Sonderausgabenpauschale 5 Jahre je 400 €", R_WP_AT),
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
  <section class="section" style="background:#fff;border-block:1px solid var(--line)" id="matrix">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Fördermatrix 2026</p>
      <h2 class="center eg-reveal">Förderungen nach Technologie und Bundesland: die Matrix</h2>
      <p class="lead center eg-reveal" style="max-width:72ch;margin-inline:auto">{lead}</p>
      {table}
      <p class="form-note center eg-reveal">Quellen: EAG-Abwicklungsstelle, Land Kärnten, Land Steiermark, Klima- und Energiefonds,
      umweltfoerderung.at, Landesförderstellen (Länderdaten Stand Mai bis Oktober 2026). Änderungen durch die Fördergeber vorbehalten.</p>
    </div>
  </section>"""


def build():
    body = "".join([
        C.page_hero(
            eyebrow="Förderungen 2026 · Bund, Kärnten, Steiermark, alle Bundesländer",
            h1="Förderungen 2026 für Photovoltaik, Speicher, Wärmepumpe und Energiemanagement",
            lead=("Stand Oktober 2026: Welche Förderung für Photovoltaik, Speicher, Wärmepumpe, Energiemanagement und "
                  "Balkonkraftwerk läuft, was beendet ist und was 2027 kommt. Bund, Kärnten, Steiermark und alle "
                  "Bundesländer auf einer Seite, mit Fristen, Beträgen und Links zu den Detail-Ratgebern."),
            cta=("kontakt", "Förderung für mein Projekt prüfen"),
            cta2=("#matrix", "Zur Fördermatrix"),
        ),
        C.kpis([
            ("150 €/kWp", "EAG-Bund für PV bis 10 kWp, plus 150 €/kWh Speicher"),
            ("3.000 €", "Landespauschale Kärnten, 12.10. bis 31.12.2026"),
            ("bis 600 €", "EMS-Förderung Klimafonds, bis 15.4.2027"),
            ("beendet", "Wärmepumpe Bund 2026: Mittel ausgeschöpft"),
        ]),
        C.cards_section(
            eyebrow="Was läuft gerade",
            h2="Förderstatus Oktober 2026: läuft, beendet, geplant",
            intro=(f"{STAND} laufen drei Förderprogramme: der EAG-Zuschuss des "
                   "Bundes (150 € je kWp, 150 € je kWh, bis 22. Oktober 2026), der Landes-Call Kärnten "
                   "(3.000 € Pauschale, 12. Oktober bis 31. Dezember 2026) und die EMS-Förderung des Klimafonds "
                   "(50 % bis 600 €, bis 15. April 2027). Die Bundesförderung für Wärmepumpen ist ausgeschöpft "
                   "(Quellen: EAG-Abwicklungsstelle, Land Kärnten, Klimafonds)."),
            cards=[
                {"ic": "✓", "title": "Läuft: jetzt einreichen",
                 "text": ("EAG-Fördercall 3/2026: Antragstellung bis 22. Oktober 2026, letzter Call im bisherigen System. "
                          "Kärnten: 2. Landes-Call 12. Oktober bis 31. Dezember 2026, Budget rund 10 Mio. €, Antrag nach "
                          "Fertigstellung. EMS: Klimafonds bis 15. April 2027."),
                 "link_key": R_BUND, "link_text": "EAG-Fördercall im Detail"},
                {"ic": "◇", "title": "Beendet: keine neuen Anträge",
                 "text": ("Sanierungsoffensive 2026 mit Kesseltausch (bis 7.500 €): Mittel ausgeschöpft. Sauber Heizen für "
                          "Alle 2026: neue Registrierungen nicht mehr möglich, bereits Registrierte können noch beantragen. "
                          "Steirischer Sanierungsbonus: Call 1. April bis 15. Mai 2026 abgeschlossen."),
                 "link_key": R_WP_AT, "link_text": "Was für die Wärmepumpe noch gilt"},
                {"ic": "◔", "title": "Geplant: Systemförderung 2027",
                 "text": ("Laut BMWET-Eckpunkten vom Oktober 2026 wird der EAG-Zuschuss ab 2027 zur Systemförderung für "
                          "Speicher plus intelligente Steuerung: Antrag nach Installation, kein Fördercall, Nachrüstung "
                          "soll förderbar werden. Projekte ab 1. November 2026 sollen 2027 beantragbar sein."),
                 "link_key": R_EMS, "link_text": "Speicher und EMS 2027"},
            ],
        ),
        _matrix_section(),
        C.cards_section(
            eyebrow="Fünf Technologien, fünf Fördertöpfe",
            h2="Förderung je Technologie: das Wichtigste in drei Sätzen",
            intro="Je Karte der aktuelle Betrag, die Frist und der Ratgeber mit Rechenbeispiel und Antragsweg.",
            cards=[
                {"ic": "☀", "title": "Photovoltaik",
                 "text": ("Der Bund zahlt 150 € je kWp bis 10 kWp, darüber 140 bis 120 €, plus 10 % Made-in-Europe-Bonus. "
                          "Kärnten legt 3.000 € Pauschale drauf, wenn ein Speicher ab 5 kWh dabei ist; die Steiermark arbeitet "
                          "mit Sanierungsbonus, Ökofonds und Gemeinden. Beispiel 10 kWp mit 10 kWh in Kärnten: rund 6.450 €."),
                 "link_key": R_BUND, "link_text": "PV-Förderung Österreich 2026"},
                {"ic": "▮", "title": "Stromspeicher",
                 "text": ("150 € je kWh vom Bund bis 50 kWh, nur gemeinsam mit einer neuen oder erweiterten PV-Anlage. "
                          "Kärnten fördert die Nachrüstung mit 1.000 € pauschal, Oberösterreich mit 150 € je kWh bis 2.250 €. "
                          "Ab 2027 soll die Nachrüstung laut BMWET auch im Bund förderbar werden."),
                 "link_key": R_SPEICHER, "link_text": "Speicherförderung 2026"},
                {"ic": "♨", "title": "Wärmepumpe",
                 "text": ("Die Bundesprogramme 2026 (Kesseltausch bis 7.500 €, Sauber Heizen für Alle) sind ausgeschöpft. "
                          "Weiter laufen die Länder: Kärnten und Steiermark je 35 % der förderbaren Kosten, Wien bis 8.000 €, "
                          "Tirol bis 18.000 € gesamt. Dazu die Öko-Sonderausgabenpauschale: fünf Jahre je 400 €."),
                 "link_key": R_WP_LAENDER, "link_text": "Landesförderungen Wärmepumpe"},
                {"ic": "◎", "title": "Energiemanagement (EMS)",
                 "text": ("Der Klima- und Energiefonds übernimmt 50 % der Kosten, maximal 600 € je Haushalt; Betriebe erhalten "
                          "30 % bis 20.000 € je Standort. Bei 800 bis 1.500 € Systemkosten* bleiben oft nur wenige hundert Euro "
                          "Eigenanteil. Registrierung vor der Rechnung, Programm bis 15. April 2027."),
                 "link_key": R_EMS, "link_text": "EMS-Förderung 2026"},
                {"ic": "⌂", "title": "Balkonkraftwerk",
                 "text": ("Steckeranlagen bis 800 W bekommen keinen EAG-Zuschuss, weil der Einspeisezählpunkt fehlt. "
                          "Wer Förderung will, plant eine angemeldete Kleinanlage ab rund 3 kWp: 150 € je kWp plus 150 € je kWh Speicher."),
                 "link_key": R_BALKON, "link_text": "Balkonkraftwerk-Förderung"},
                {"ic": "€", "title": "Finanzierung und Förderung",
                 "text": ("Wer finanziert, bekommt die Förderung in voller Höhe, weil die Anlage ab Tag 1 dem Kunden gehört. "
                          "Der EAG-Zuschuss wird vom Finanzierungsbetrag abgezogen, Landespauschalen kommen auf Ihr Konto."),
                 "link_key": "finanzierung", "link_text": "PV-Anlage finanzieren"},
            ],
        ),
        C.linkgrid_section("Förderung nach Bundesland", LAENDER),
        C.steps_section(
            eyebrow="Reihenfolge der Anträge",
            h2="Erst Bund, dann Land: die richtige Reihenfolge im Herbst 2026",
            steps=[
                ("EAG-Antrag vor Inbetriebnahme",
                 "Zählpunkt beim Netzbetreiber, Ticket im Fördercall (bis 22. Oktober 2026), Antrag vervollständigen. "
                 "Montiert wird erst nach der Zusage, sonst verfällt der Bundeszuschuss.",
                 "vor der Montage"),
                ("Landesförderung nach Fertigstellung",
                 "Kärnten: Antrag über die Förderplattform des Landes zwischen 12. Oktober und 31. Dezember 2026 mit "
                 "Rechnung und Fertigstellungsmeldung. Bund wird nicht angerechnet.",
                 "nach der Montage"),
                ("EMS: Registrierung vor der Rechnung",
                 "Beim Klima- und Energiefonds registrieren, erst dann die Rechnung für das EMS ausstellen lassen. "
                 "Wer die Rechnung zuerst hat, verliert die 600 €. Frist 15. April 2027.",
                 "vor der Rechnung"),
                ("Wärmepumpe: Landesstelle klären",
                 "Ohne Bundesprogramm zählt das Land: Kärnten über das Förderportal des Landes, Steiermark über die "
                 "Abteilung 15. Deckel, Fristen und Kombinationen klären wir vor dem Angebot.",
                 "vor dem Heizungstausch"),
            ],
        ),
        C.media_text(
            eyebrow="Service inklusive",
            h2="Wir übernehmen die Anträge: Bund, Land, Klimafonds",
            paragraphs=[
                ("Wir prüfen vor dem Angebot, welche Programme zu Dach, Heizung und Bundesland passen, rechnen die Beträge "
                 "in den Projektbericht mit 3D-Belegplan und Statikreport ein und terminieren Montage und Antrag so, "
                 "dass keine Frist verfällt."),
                ("Sie bleiben Antragsteller und bekommen die Auszahlung auf Ihr Konto, auch bei Finanzierung. Wir liefern "
                 "Zählpunkt, Ticket, Rechnung, Fertigstellungsmeldung und Fotos."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zu Förderanträgen für Photovoltaik und Wärmepumpe mit Unterlagen am Tisch",
            bullets=["Förderprüfung vor dem Angebot, Beträge im Projektbericht ausgewiesen",
                     "Ticket, Antrag und Fertigstellungsmeldung bereiten wir vor, Sie bestätigen",
                     "Reihenfolge im Blick: Bund vor der Montage, Land danach",
                     "Volle Förderung auch bei Finanzierung: die Anlage gehört ab Tag 1 Ihnen"],
            cta=("kontakt", "Kostenlose Förderprüfung anfragen"),
            dark=True,
        ),
        C.faq_section(FAQ),
        C.linkgrid_section("Weiterlesen: Leistungen und Ratgeber", [
            ("photovoltaik", "Photovoltaikanlage mit Speicher"),
            ("batteriespeicher", "Batteriespeicher"),
            ("waermepumpe", "Wärmepumpe"),
            ("ems", "Energiemanagementsystem"),
            ("balkonkraftwerke", "Balkonkraftwerke"),
            ("finanzierung", "Finanzierung: Eigentum ab Tag 1"),
            (R_SANIERUNG, "Sanierungsoffensive 2026: was galt"),
            (R_SAUBER, "Sauber Heizen für Alle 2026"),
            (R_WP_BETRIEBE, "Wärmepumpen-Förderung für Betriebe"),
            (R_WP_STEUER, "Öko-Sonderausgabenpauschale"),
            ("solarrechner", "Solarrechner: Kosten und Ertrag"),
            ("referenzen", "Referenzen"),
        ]),
        C.contact_section(
            "Welche Förderung passt zu Ihrem Projekt?",
            "Sagen Sie uns Bundesland, Dach und Heizung. Wir sagen Ihnen, welche Programme laufen und wie wir einreichen.",
            page_label="Förderungen",
        ),
        C.finalcta(
            "Fristen laufen: EAG bis 22. Oktober, Kärnten bis 31. Dezember",
            "Kostenlose Erstberatung mit Förderprüfung. Wir melden uns innerhalb eines Werktags.",
            trust=[(f"{NAP['rating']} auf Google", True), ("300+ Projekte", False),
                   ("Anträge inklusive", False), ("Antwort in einem Werktag", False)],
        ),
        f'<div class="wrap"><p class="form-note" style="padding:8px 0 40px">*Richtwerte: EMS-Systemkosten marktüblich. '
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
