"""Leistungsseite Energiegemeinschaft fuer Gewerbe, Gemeinden und Mehrparteienhaeuser
(/leistungen/energiegemeinschaft-gewerbe/).

Quelle: Live-LP /energiegemeinschaften-gewerbe/ (freigegebene Inhalte), der Pillar-Ratgeber
/energiegemeinschaft/, die Cluster-Artikel /energiegemeinschaft-gruenden/ und /energiegemeinschaft-kosten/
(Gruendungskosten, Mindestgroesse, Rechtsform), build/seo/_fakten_2026-10.md (OeMAG Oktober 2026:
14,874 ct, Verlauf Juli 6,146 ct) und das SEO/GEO-Briefing build/seo/eg_gewerbe.{json,md}. Seit 20.11.2026 kommerziell auf "Energiegemeinschaft fuer
Betriebe und Gemeinden" ausgerichtet; "Energiegemeinschaft gruenden" gehoert dem Ratgeber /energiegemeinschaft-gruenden/
(320 Suchen, Kannibalisierung), der hier fuer den Ablauf verlinkt ist.

Abgrenzung: Diese LP = Energiegemeinschaft gruenden LASSEN (Leistungsumfang, Kosten, Dauer fuer Betriebe
und Gemeinden). Der Ratgeber /energiegemeinschaft-gruenden/ = selbst gruenden, Schritt fuer Schritt (verlinkt).
Beispielrechnung "Metallbetrieb, 100 kWp" ehrlich mit der OeMAG-Spanne 2026 (Juli 6,146 ct bis Oktober 14,874 ct,
Monatswerte aufs Jahr hochgerechnet und so gekennzeichnet): Beim Oktober-Wert bei 10 ct* und 12 ct* EG-Preis
Mindererloes, Vorteil kommt aus Netzentgelt, Planbarkeit und Abnehmer-Ersparnis.

Pflicht (README): Netzentgelt-Rabatt 57 % lokal / 28 % regional, Netzebene 4/5 bis 64 %, NUR im
Nahbereich; oesterreichweit = Buergerenergiegemeinschaft ohne Rabatt. energyfamily nur als Text-Badge.
Gemeinde-Beispiel ohne erfundene Zahlen.
ElWG (Faktenliste, Abschnitt "VERBINDLICH AB 20.11.2026"): Rabatt Oktober bis Dezember 2026 nur fuer EEG-Mitglieder,
BEG/P2P/EVA im Nahbereich voraussichtlich ab 1.1.2027 (Hoehe legt die E-Control fest); netzuebergreifend voraussichtlich
ab April 2027, bis dahin nur Zaehlpunkte beim selben Netzbetreiber. Abgabenbefreiung nur EEG.
"""

from common import IMG, NAP, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

PATH = "/leistungen/energiegemeinschaft-gewerbe/"
TITLE = "Energiegemeinschaft für Betriebe und Gemeinden | EBZ Energie"
DESC = ("Energiegemeinschaft für Betriebe, Landwirtschaft und Gemeinden: EBZ plant PV-Anlage, Rechtsform, "
        "Netzanmeldung und Abrechnung. Verein ab 50 €.")

OEMAG_OKT = "14,874"   # aktueller Wert, Stand November 2026
OEMAG_SEPT = "10,168"
OEMAG_JULI = "6,146"

FAQ = [
    ("Was kostet die Gründung einer Energiegemeinschaft?",
     "Als Verein etwa 50 bis 150 € für Vereinsregister, Statuten und Konto, als Genossenschaft mehrere hundert Euro "
     "plus jährlich den Revisionsverband. Registrierung bei ebUtilities und der Betreibervertrag mit dem Netzbetreiber "
     "sind kostenlos. Laufend fallen 2 bis 8 € je Zählpunkt und Monat für Plattform und Abrechnung an, umgelegt 25 bis "
     "100 € je Mitglied und Jahr. Planung und Potenzialanalyse durch EBZ bieten wir nach dem Erstgespräch an."),
    ("Wie viele Zählpunkte und Mitglieder braucht eine Energiegemeinschaft mindestens?",
     "Gesetzlich reichen zwei Teilnehmer mit je einem Zählpunkt. In der Praxis planen wir mit mindestens fünf "
     "Zählpunkten, damit Verwaltung, Abrechnung und Zuordnungsquote im Verhältnis stehen. Nach oben ist die Zahl "
     "offen, energyfamily rechnet von 2 bis über 1.000 Zählpunkte automatisiert ab."),
    ("Dürfen Großunternehmen an einer EEG teilnehmen oder nur KMU?",
     "An einer Erneuerbaren-Energie-Gemeinschaft dürfen nur kleine und mittlere Unternehmen nach KMU-Definition (WKO) "
     "teilnehmen, also bis 250 Mitarbeiter, und nur, wenn die Teilnahme nicht ihre gewerbliche Haupttätigkeit ist. "
     "Große Unternehmen nutzen die Bürgerenergiegemeinschaft (BEG, auch Großunternehmen) oder seit Oktober 2026 "
     "Peer-to-Peer-Verträge, beides ohne Abgabenbefreiung. Einen Netzentgelt-Rabatt im Nahbereich sieht die neue "
     "Netzentgelt-Verordnung für diese Modelle voraussichtlich ab 1. Jänner 2027 vor, die Höhe legt die E-Control fest; "
     "bis dahin bekommen ihn nur EEG-Mitglieder."),
    ("Welche Förderung gibt es für die Gründung (Klima- und Energiefonds)?",
     "Der Klima- und Energiefonds hat Konzept- und Aufbauphase von Energiegemeinschaften über eigene Förder-Calls "
     "unterstützt; ob aktuell ein Call offen ist, prüfen wir für Ihr Projekt (Stand Oktober 2026). Verlässlich "
     "beantragbar ist die EMS-Förderung des Klimafonds für das Energiemanagementsystem mit bis zu 30 Prozent, "
     "maximal 20.000 € je Standort. Der Investitionszuschuss des Bundes für PV und Speicher ist für 2026 "
     "abgeschlossen; ab 2027 plant der Bund laut BMWET eine Systemförderung für Speicher mit intelligenter Steuerung."),
    ("Verein oder Genossenschaft: welche Rechtsform passt für Gemeinde und Betrieb?",
     "Die Gemeinschaft braucht eine eigene Rechtspersönlichkeit. Für kleinere Gemeinschaften ohne Kapitalbedarf der "
     "Verein (Statuten, ZVR-Zahl, Vorstand, etwa 50 bis 150 €), für größere mit Investitionen und vielen Mitgliedern "
     "die Genossenschaft, für Projekte, die ein Betrieb als Unternehmen führt, die GmbH. Eine EEG darf nicht auf "
     "Gewinn ausgerichtet sein, der Nutzen muss bei den Mitgliedern bleiben (Gemeinnützigkeit im weiteren Sinn)."),
    ("Kann ein Betrieb Strom zwischen mehreren eigenen Standorten teilen (Eigenversorgungsanlage, BEG)?",
     "Ja. Seit dem ElWG gibt es die Eigenversorgungsanlage (EVA, mehrere eigene Standorte): Ein Unternehmen "
     "versorgt seine Filialen oder Hallen im Nahbereich mit dem Strom einer eigenen Anlage über das öffentliche "
     "Netz, ohne eigene Rechtsform. Einen Netzentgelt-Rabatt für die EVA sieht die neue Netzentgelt-Verordnung "
     "voraussichtlich ab 1. Jänner 2027 vor, die Abgabenbefreiung ist derzeit nur für die EEG geregelt. Liegen die "
     "Standorte weit auseinander, ist die Bürgerenergiegemeinschaft der Weg, dann ohne Netzentgelt-Rabatt; über "
     "mehrere Netzbetreiber hinweg laut Koordinationsstelle voraussichtlich ab April 2027."),
    ("Wie lange dauert es von der Idee bis zum Betrieb?",
     "Die Potenzialanalyse dauert 2 bis 3 Wochen, Modell und Rechtsform 2 bis 4 Wochen, Anlage und Anmeldung "
     "beim Netzbetreiber 4 bis 12 Wochen. Registrierung als Marktpartner und Betreibervertrag sind kostenlos, die "
     "Zählpunktanmeldung wird jeweils zum Monatsersten wirksam."),
    ("Was bringt die Gemeinschaft einem Betrieb mit eigener PV-Anlage?",
     f"Planbarkeit und einen zweiten Abnehmerkreis: Der Wochenendüberschuss bekommt einen fix vereinbarten EG-Preis "
     f"statt des monatlich schwankenden OeMAG-Marktpreises ({OEMAG_JULI} ct im Juli, {OEMAG_OKT} ct im Oktober "
     "2026). Ein EG-Preis von 10 oder 12 ct* liegt damit je nach Monat über oder unter dem Marktpreis, im Oktober 2026 "
     "klar darunter; dafür ist er planbar. Werktags bezieht "
     "der Betrieb bei Bedarf EG-Strom, in der EEG mit reduziertem Netzentgelt, auf Netzebene 4/5 bis zu 64 Prozent weniger."),
    ("Können Mehrparteienhäuser teilnehmen?",
     "Ja. Im Gebäude teilt eine "
     + a("/gemeinschaftliche-erzeugungsanlage/", "Gemeinschaftliche Erzeugungsanlage (GEA)")
     + " den Strom ohne Netzentgelt auf die "
     "Wohnungen auf, zusätzlich kann das Haus an einer EEG teilnehmen, um Überschuss an die Nachbarschaft zu "
     "verkaufen. Für Hausverwaltungen übernehmen wir Planung und Betreibermodell."),
]


def _table_section(eyebrow, h2, intro, headers, rows, note="", anchor=""):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join(
        "<tr>" + "".join(f'<td class="{"hl" if i == 0 else ""}">{c}</td>' for i, c in enumerate(r)) + "</tr>"
        for r in rows
    )
    anchor_attr = f' id="{anchor}"' if anchor else ""
    note_html = f'<p class="form-note center eg-reveal" style="margin-top:18px">{note}</p>' if note else ""
    return f"""
  <section class="section"{anchor_attr} style="background:#fff;border-block:1px solid var(--line)">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">{eyebrow}</p>
      <h2 class="center eg-reveal">{h2}</h2>
      <p class="lead center eg-reveal" style="max-width:72ch;margin-inline:auto">{intro}</p>
      <div class="art-tablewrap eg-reveal" style="margin-top:32px">
        <table class="art-table"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>
      </div>
      {note_html}
    </div>
  </section>"""


def body():
    """Inhalt der Seite (auch fuer die Ads-Landingpage unter der alten Adresse, siehe pages/landingpages.py)."""
    rating, count, reviews = load_reviews()
    body = "".join([
        C.hero(
            eyebrow="Energiegemeinschaft für Gewerbe, Gemeinden, Hausverwaltungen · Kärnten und Steiermark",
            h1="Energiegemeinschaft für Betriebe und Gemeinden: Ihr Dach kann mehr als Eigenverbrauch",
            lead=("Werktags verbraucht Ihr Betrieb den Sonnenstrom selbst, am Wochenende geht er zum monatlich "
                  "schwankenden OeMAG-Marktpreis ins Netz. In einer Energiegemeinschaft versorgt dieser Überschuss die "
                  "Gemeinde, die Siedlung oder den Betrieb nebenan, zu einem Preis, den Sie mitbestimmen. EBZ Energie "
                  "gründet die Gemeinschaft mit Ihnen: Potenzialanalyse, Rechtsform, Netzanmeldung, Anlage und "
                  "monatliche Abrechnung aus einer Hand."),
            badges=[("50 bis 500 kWp", "typische Dachanlagen"),
                    ("bis zu 64 %", "weniger Netzentgelt auf NE 4/5"),
                    ("ab 2", "Teilnehmern, Verein ab 50 €")],
            img=IMG["gewerbe_dach"],
            img_alt="Große Photovoltaikanlage auf einem Gewerbedach in Oberösterreich, Erzeuger einer Energiegemeinschaft",
            float_num=rating,
            float_label=f"aus {count} Google Bewertungen" if count else "auf Google",
            cta_primary=("kontakt", "Potenzialanalyse anfragen"),
            cta_secondary=("#schritte", "Gründung in 6 Schritten"),
        ),
        C.kpis([
            ("bis zu 64 %", "Netzentgelt-Abschlag auf Netzebene 4/5"),
            ("50 bis 150 €", "Gründungskosten als Verein"),
            ("2 bis 8 €", "je Zählpunkt und Monat für die Abrechnung"),
            ("2 bis 1.000+", "Zählpunkte, die energyfamily automatisiert abrechnet"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Was ist eine Energiegemeinschaft für Betriebe und Gemeinden?",
            paragraphs=[
                ("Eine Energiegemeinschaft ist ein Zusammenschluss von mindestens zwei Teilnehmern, die Strom aus "
                 "erneuerbaren Quellen über das öffentliche Netz teilen. In einer Erneuerbare-Energie-Gemeinschaft (EEG) "
                 "sinkt das Netzentgelt im Nahbereich um 57 Prozent (lokal), 28 Prozent (regional) oder 64 Prozent bei "
                 "ausschließlicher Teilnahme auf Netzebene 4/5. Die Gründung als Verein "
                 "kostet 50 bis 150 Euro, die Abrechnung 2 bis 8 Euro je Zählpunkt und Monat (Quellen: E-Control "
                 "SNE-VO, energiegemeinschaften.gv.at, Stand November 2026)."),
                ("Seit dem ElWG (1. Oktober 2026) gibt es fünf Modelle: die Erneuerbare-Energie-Gemeinschaft (EEG) im "
                 "Nahbereich für Gemeinden, Vereine, Haushalte und KMU bis 250 Mitarbeiter; die "
                 + a("/buergerenergiegemeinschaft/", "Bürgerenergiegemeinschaft (BEG, auch Großunternehmen)")
                 + ", die sich über mehrere Netzgebiete erstrecken "
                 "darf; die Gemeinschaftliche Erzeugungsanlage (GEA) im Mehrparteienhaus; den "
                 + a("/peer-to-peer-strom/", "Peer-to-Peer-Vertrag")
                 + " zwischen zwei Zählpunkten ohne Verein; und die Eigenversorgungsanlage (EVA, mehrere eigene Standorte) "
                 "für Betriebe mit Filialen. Je Zählpunkt sind bis zu fünf Modelle möglich. Den Netzentgelt-Rabatt "
                 "bekommen von Oktober bis Dezember 2026 nur EEG-Mitglieder, für BEG, Peer-to-Peer und EVA im "
                 "Nahbereich ist er voraussichtlich ab 1. Jänner 2027 vorgesehen (Höhe legt die E-Control fest). In der "
                 "Übergangsphase gehen neue Zuordnungen nur mit Zählpunkten beim selben Netzbetreiber, netzübergreifend "
                 "laut Koordinationsstelle voraussichtlich ab April 2027. Der Netzbetreiber ordnet je Viertelstunde zu, "
                 "nur die zugeordnete Menge bekommt EG-Preis und Rabatt. Für Betriebe und Gemeinden zählt deshalb vor "
                 "allem der Lastgang. Mehr zu den Modellen im Leitartikel "
                 + a("eg", "Energiegemeinschaft: Modelle und ElWG") + "."),
            ],
        ),
        C.audience_split(
            eyebrow="Für wen gründen wir?",
            h2="Zwei Ausgangslagen, ein Ziel: Strom bleibt in der Region",
            intro=("Ob Betriebsdach oder Gemeindegebäude, wir rechnen mit Ihren Viertelstundenwerten und zeigen vorab, "
                   "welche Mengen und Erlöse realistisch sind. Wer selbst gründen will, findet den Ablauf im "
                   + a("/energiegemeinschaft-gruenden/", "Ratgeber Energiegemeinschaft gründen") + "."),
            left={
                "img": IMG["gen_gewerbe"],
                "alt": "Gewerbebetrieb mit großer Photovoltaikanlage auf dem Hallendach",
                "title": "Energiegemeinschaft Unternehmen und Landwirtschaft: Wochenendüberschuss wird zum zweiten Standbein",
                "bullets": [
                    "50 bis 500 kWp typische Dachanlagen auf Hallen, Ställen und Scheunen",
                    "Werktags Eigenverbrauch, am Wochenende liefert das Dach an die Gemeinschaft",
                    "Fixer EG-Preis statt monatlich schwankendem OeMAG-Marktpreis",
                    "Voraussetzung EEG: KMU bis 250 Mitarbeiter, sonst Bürgerenergiegemeinschaft oder EVA",
                ],
                "cta": ("kontakt", "Für meinen Betrieb anfragen"),
            },
            right={
                "img": IMG["eg_drohne"],
                "alt": "Ortschaft mit Photovoltaik auf mehreren Dächern, Gemeinde als Energiegemeinschaft",
                "title": "Energiegemeinschaft Gemeinde und Hausverwaltung: Bürgerstrom für Schule, Bauhof und Wohnanlage",
                "bullets": [
                    "Gemeindedächer als Erzeuger, kommunale Gebäude und Straßenbeleuchtung als Abnehmer",
                    "Bürgerinnen und Bürger als Mitglieder, Wertschöpfung bleibt im Ort",
                    "Mehrparteienhaus: GEA im Gebäude plus EEG nach außen",
                    "Reporting für Gemeinderat und Eigentümerversammlung",
                ],
                "cta": ("kontakt", "Für meine Gemeinde anfragen"),
            },
        ),
        C.cards_section(
            eyebrow="Netzebene 7 / 6 / 4-5 und Nahbereich",
            h2="Der Netzanschluss entscheidet über Abschlag und Mitgliederkreis",
            intro=("Ob Ihre Gemeinschaft lokal oder regional ist, bestimmt nicht die Gemeindegrenze, sondern "
                   "Trafostation und Umspannwerk. Bei Betrieben mit Mittelspannung ist die regionale Ebene der Normalfall. "
                   "Die Nahbereichsabfrage je Zählpunkt übernehmen wir bei Kärnten Netz und Energienetze Steiermark."),
            cards=[
                {"ic": "⌂", "title": "Netzebene 7: Niederspannung",
                 "text": "Haushalte und kleine Betriebe. Am selben Trafo (lokal) minus 57 % Netzentgelt, am selben Umspannwerk (regional) minus 28 %. In der EEG entfällt zusätzlich die Elektrizitätsabgabe (2026 befristet 0,82 ct je kWh für Betriebe und 0,1 ct für Haushalte, ab 2027 wieder 1,5 ct); den Erneuerbaren-Förderbeitrag setzt die Bundesregierung 2027 für alle Stromkunden aus."},
                {"ic": "◎", "title": "Netzebene 6: Trafostation",
                 "text": "Betriebe mit eigener Trafo-Anbindung. Die Zuordnung zu lokal oder regional trifft der Netzbetreiber anhand der Zählpunktnummer, nicht anhand der Adresse."},
                {"ic": "◇", "title": "Netzebene 4/5: Mittelspannung",
                 "text": "Bei ausschließlicher Teilnahme auf diesen Ebenen in der EEG bis zu 64 % Abschlag auf den Arbeitspreis des Netzentgelts. Relevant für größere Betriebe und Industrieareale.",
                 "link_key": "/energiegemeinschaft-netzkosten/", "link_text": "Netzkosten im Detail"},
            ],
        ),
        C.problem_compare(
            eyebrow="Beispielrechnung",
            h2="Metallbetrieb, 100 kWp: Was das Wochenende wert ist",
            intro=("Jahresertrag rund 105.000 kWh, Eigenverbrauch werktags 65 Prozent. Bleiben rund 37.000 kWh "
                   "Überschuss an Wochenenden und Feiertagen, davon werden in der Gemeinschaft konservativ 70 Prozent "
                   f"(rund 26.000 kWh) zugeordnet.* Ehrlich gerechnet, den jeweiligen OeMAG-Monatswert aufs Jahr hochgerechnet: "
                   f"Beim Juli-Wert von {OEMAG_JULI} ct bringen 10 ct* EG-Preis rund 1.000 € mehr als die OeMAG, beim "
                   f"Oktober-Wert von {OEMAG_OKT} ct rund 1.270 € weniger, bei 12 ct* rund 750 € weniger. Der EG-Preis ist "
                   "dafür planbar, der sichere Vorteil liegt beim Netzentgelt des Bezugs."),
            bars=[
                ("Netzentgelt-Arbeitspreis je kWh Bezug beim Lieferanten", 100, "bad", "100 %"),
                ("Netzentgelt-Arbeitspreis je kWh EG-Bezug auf Netzebene 4/5", 36, "good", "minus 64 %"),
            ],
            aside=("Das Ergebnis im Beispiel", [
                ("€", "Planbarer Erzeugerpreis", "Fix vereinbart statt Marktpreis, der 2026 zwischen rund 6 und knapp 15 ct schwankte. Mehrerlös nur, wenn der EG-Preis über dem Marktpreis liegt.*"),
                ("◇", "Netzersparnis beim eigenen Bezug", "Werktags in der Früh und im Winter bezieht der Betrieb EG-Strom mit 28 bis 64 % weniger Netzentgelt, je nach Netzebene."),
                ("⌂", "Auftritt in der Gemeindezeitung", "Statt einer Zeile auf der OeMAG-Abrechnung: Ihr Strom versorgt den Ort."),
                ("◷", "Belastbare Zahl aus der Potenzialanalyse", "Betriebe mit Wochenendverbrauch (Kühlung, Hotellerie, Landwirtschaft) profitieren eher als Abnehmer: Lastgang / Lastprofil entscheiden."),
            ]),
        ).replace('<section class="section">', '<section class="section" id="beispiel">', 1),
        C.steps_section(
            eyebrow="Gründen lassen",
            h2="Gründung mit EBZ in 6 Schritten: Verein, ebUtilities, Betreibervertrag, EDA, Teilnehmer, Start",
            steps=[
                ("Potenzialanalyse und Mitglieder",
                 "Dachflächen, Lastgänge und Nahbereich aller Zählpunkte. Gesetzlich mindestens 2 Mitglieder, 5 Zählpunkte (Praxiswert) planen wir als Untergrenze.",
                 "2 bis 3 Wochen"),
                ("Rechtsform und Statuten",
                 "Verein oder Genossenschaft, Statuten mit Aufnahme, Austritt, Preis und Aufteilungsschlüssel (statische und dynamische Zuteilung), ZVR-Zahl, Konto. Mit Partnern für Recht und Steuer.",
                 "2 bis 4 Wochen"),
                ("Registrierung bei ebUtilities (Marktpartner-ID)",
                 "Die Gemeinschaft wird Marktpartner und erhält ihre Gemeinschafts-ID. Kostenlos, in wenigen Tagen erledigt.",
                 "wenige Tage"),
                ("Betreibervertrag mit dem Netzbetreiber und EDA-Portal",
                 "Vertrag mit Kärnten Netz oder Energienetze Steiermark, danach Anmeldung aller Zählpunkte über das EDA-Portal. Parallel Bau von PV-Anlage, Speicher und Lastmanagement, falls nötig.",
                 "4 bis 12 Wochen"),
                ("Teilnehmer freigeben",
                 "Jedes Mitglied bestätigt die Teilnahme im Kundenportal seines Netzbetreibers und aktiviert die Viertelstundenwerte. Wirksam zum Monatsersten.",
                 "ab Monatserstem"),
                ("Start und Abrechnung",
                 "Monatliche Abrechnung über energyfamily, Reporting für Gemeinderat oder Geschäftsführung, laufende Aufnahme neuer Mitglieder.",
                 "laufend"),
            ],
        ).replace('<section class="section', '<section id="schritte" class="section', 1),
        _table_section(
            eyebrow="Energiegemeinschaft gründen Kosten: einmalig und laufend",
            h2="Was die Gründung kostet: Vereinsgründung, Servicekosten je Zählpunkt, Mitgliedsbeitrag",
            intro=("Die Behördenseite ist günstig, die laufende Abrechnung der eigentliche Posten. Alle Zahlen sind "
                   "marktübliche Spannen aus unseren Ratgebern, die belastbare Kalkulation für Ihr Projekt liefert die "
                   "Potenzialanalyse."),
            headers=["Posten", "Wer zahlt", "Kosten", "Hinweis"],
            rows=[
                ("Vereinsgründung", "Gründer", "ca. 50 bis 150 €", "Vereinsregister (ZVR-Zahl), Statuten, Konto"),
                ("Genossenschaftsgründung", "Gründer", "mehrere hundert €", "plus Revisionsverband jährlich; für größere Gemeinschaften mit Kapitalbedarf"),
                ("Registrierung ebUtilities, Betreibervertrag", "Gemeinschaft", "0 €", "Marktpartner-Registrierung und Netzbetreibervertrag sind kostenlos"),
                ("Set-up-Kosten Plattform", "Gemeinschaft", "meist 0 €", "Einrichtungsgebühren sind bei seriösen Plattformen unüblich"),
                ("Servicekosten je Zählpunkt", "Mitglied", "2 bis 8 € je Monat", "oder 0,5 bis 2 ct je abgerechneter kWh; Plattform und Abrechnung"),
                ("Mitgliedsbeitrag gesamt", "Mitglied", "25 bis 100 € je Jahr", "typischer Jahresvorteil laut Erfahrungsberichten 100 bis 300 €"),
                ("Steuerberatung, Buchhaltung", "Gemeinschaft", "0 bis einige hundert € je Jahr", "bei Vereinen oft ehrenamtlich gelöst"),
                ("Versorgungsinfrastrukturbeitrag", "Einspeiser über 20 kW", "0,05 ct je kWh", "ElWG, gedeckelt mit 0,5 € je MWh, wirtschaftlich vernachlässigbar"),
            ],
            note=("Quellen: Ratgeber " + a("/energiegemeinschaft-kosten/", "Kosten und Abrechnung") + " und "
                  + a("/energiegemeinschaft-gruenden/", "Energiegemeinschaft gründen") + ", Stand Oktober 2026."),
            anchor="kosten",
        ),
        C.media_text(
            eyebrow="Gemeinde-Beispiel",
            h2="Wie eine Gemeinde-Energiegemeinschaft aufgebaut ist",
            paragraphs=[
                ("Das typische Gemeindeprojekt: Volksschule, Bauhof und Kläranlage tragen die PV-Anlagen, denn sie "
                 "haben die Dächer und werktags den Verbrauch. Gemeindeamt, Feuerwehrhaus und Straßenbeleuchtung sind "
                 "Abnehmer, die Straßenbeleuchtung nachts, wenn ein Speicher den Tagesüberschuss hält. Bürgerinnen und "
                 "Bürger treten als Mitglieder bei und beziehen am Wochenende den Überschuss der Schule."),
                ("Was die Potenzialanalyse liefert: die Zuordnungsquote je Gebäude aus den Viertelstundenwerten, den "
                 "Nahbereich aller Zählpunkte, die passende Rechtsform und einen Aufteilungsschlüssel, der die Gemeinde "
                 "nicht benachteiligt. Zahlen nennen wir erst, wenn Ihre Lastgänge auf dem Tisch liegen. Vergleichbare "
                 "Modelle dokumentiert die Koordinationsstelle energiegemeinschaften.gv.at."),
            ],
            img=IMG["gen_gewerbe"],
            alt="Photovoltaikanlage auf einem Betriebsdach, geplant nach Lastprofil",
            bullets=[
                "Viertelstundenwerte aller Zählpunkte als Rechengrundlage",
                "Aufteilungsschlüssel statisch oder dynamisch, passend zum Mitgliederkreis",
                "Speicher und " + a("ems", "Energiemanagement") + " verschieben Verbrauch in die richtige Viertelstunde",
            ],
            reverse=True,
            cta=("pv_gewerbe", "Photovoltaik für Gewerbe"),
        ),
        C.facts_panel(
            eyebrow="Energiegemeinschaft Abrechnung und Reporting",
            h2="Skalierbare Abrechnung über unseren Partner energyfamily",
            intro=('<span class="hero__badge" style="background:var(--petrol);color:#fff"><b>Partner</b> energyfamily</span><br>'
                   "Die Verwaltung übernimmt die österreichische Plattform energyfamily: monatliche Abrechnung aller "
                   "Zählpunkte, App für die Mitglieder und Reporting für Gemeinderat oder Geschäftsführung."),
            rows=[
                ("Plattform", "energyfamily, Datenverarbeitung in Österreich, DSGVO-konform"),
                ("Größe", "von 2 bis über 1.000 Zählpunkte automatisiert"),
                ("Erfahrung", "rund 330 aktive Gemeinschaften, rund 15.000 Nutzer"),
                ("Abrechnung", "monatlich, mit App und Reporting; neue Mitglieder laufend"),
                ("Laufende Kosten", "typisch 2 bis 8 € je Zählpunkt und Monat"),
                ("Registrierung", "Marktpartner-Registrierung und Netzbetreibervertrag kostenlos"),
            ],
            actions=[("Kosten und Abrechnung im Detail", "/energiegemeinschaft-kosten/", "")],
        ),
        C.media_text(
            eyebrow="Förderungen: Klima- und Energiefonds, Landesförderung, Ausblick Bund",
            h2="Förderungen im Blick, Finanzierung nach Bedarf",
            paragraphs=[
                ("Der Investitionszuschuss des Bundes für PV und Speicher ist für 2026 ausgeschöpft beziehungsweise "
                 "abgeschlossen; ab 2027 plant der Bund laut BMWET eine Systemförderung für Speicher mit intelligenter "
                 "Steuerung, Höhe und Kriterien offen. Für Betriebe und Gemeinden gelten bei den Ländern eigene "
                 "Richtlinien, der steirische Ökofonds hat derzeit keine PV-Ausschreibung. Das Energiemanagementsystem fördert der "
                 "Klima- und Energiefonds mit bis zu 30 Prozent, maximal 20.000 € je Standort, die Teilnahme an einer "
                 "Energiegemeinschaft ist dort eine zulässige Betriebsoption."),
                ("Für Konzept und Aufbau von Energiegemeinschaften gab es beim Klima- und Energiefonds Förder-Calls; ob "
                 "aktuell einer offen ist, prüfen wir für Ihr Projekt. Wer die Liquidität im Betrieb halten will, "
                 "finanziert die Anlage zur fixen Rate und bleibt ab Tag 1 Eigentümer."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zu Förderung und Finanzierung einer Gewerbe-Photovoltaikanlage",
            bullets=[
                "Bund: Investitionszuschuss für 2026 abgeschlossen, ab 2027 Systemförderung geplant",
                a("/ems-foerderung/", "EMS-Förderung des Klimafonds") + ": 30 % bis 20.000 € je Standort",
                a("finanzierung", "Finanzierung") + ": 0 € Anzahlung, fixe Rate, Eigentum ab Tag 1",
            ],
            cta=("foerderung_at", "Förderungen 2026 im Überblick"),
            dark=True,
        ),
        C.why_section(
            eyebrow="Ihr Partner",
            h2="Warum Betriebe und Gemeinden mit EBZ gründen",
            items=[
                ("☀", "Anlage und EG aus einer Hand", "Dachanlage, Speicher, Lastmanagement und Gemeinschaft vom selben Team aus zertifizierten Fachkräften."),
                ("◷", "Lastgang statt Bauchgefühl", "Wir rechnen mit Ihren Viertelstundenwerten, nicht mit Prospektzahlen, und mit der ganzen Spanne des OeMAG-Marktpreises statt nur mit dem Tief vom Juli."),
                ("◎", "Prozesse mit dem Netzbetreiber", "ebUtilities, Betreibervertrag, EDA-Anmeldungen: Wir kennen die Abläufe bei Kärnten Netz und Energienetze Steiermark."),
                ("✓", "Skalierbare Abrechnung", "energyfamily rechnet von 2 bis über 1.000 Zählpunkte automatisiert ab, monatlich, mit App und Reporting."),
                ("€", "Förderungen im Blick", "Landesförderungen, die EMS-Förderung des Klimafonds und die geplante Systemförderung des Bundes: Wir prüfen, was gerade beantragbar ist."),
                ("⌂", "Regional präsent", "Sitz in Villach, Projekte in ganz Kärnten und der Steiermark. Ein Ansprechpartner, vom Erstgespräch bis zum Reporting."),
            ],
        ),
        C.reference_cards(
            eyebrow="Aus der Praxis",
            h2="Erzeuger-Dächer, die sich rechnen",
            intro=("Drei Anlagen aus über 300 dokumentierten Projekten in 6 Bundesländern: Betriebsdach, Wohnanlage "
                   "und Einfamilienhaus, jede mit echten Zahlen."),
            items=[
                {"img": IMG["gewerbe_dach"], "alt": "Große Photovoltaikanlage auf einem Gewerbedach in Oberösterreich",
                 "title": "Gewerbe, Oberösterreich", "specs": "40 kWp Ost-West auf Trapezblech, 40 kWh Speicher, rund 40.000 kWh im Jahr.",
                 "result": "13.500 €", "result_sub": "Ersparnis pro Jahr"},
                {"img": IMG["ref_krumpendorf"], "alt": "Photovoltaikanlage auf einem Mehrparteienhaus in Krumpendorf",
                 "title": "Mehrparteienhaus, Krumpendorf", "specs": "25 kWp mit 25 kWh Speicher und Notstrom.",
                 "result": "4 Tage", "result_sub": "Bauzeit"},
                {"img": IMG["ref_villach"], "alt": "Photovoltaikanlage auf einem Einfamilienhaus in Villach",
                 "title": "Einfamilienhaus, Villach", "specs": "10 kWp Ost-West mit Notstrom, rund 11.000 kWh im Jahr.",
                 "result": "rund 80 %", "result_sub": "weniger Stromkosten"},
            ],
        ),
        C.reviews_slider(reviews, rating, count),
        C.faq_section(FAQ),
        C.linkgrid_section("Weiterlesen", [
            ("/energiegemeinschaft-gruenden/", "Selbst gründen: Schritt-für-Schritt-Anleitung"),
            ("/energiegemeinschaft-kosten/", "Kosten und Abrechnung"),
            ("/energiegemeinschaft-netzkosten/", "Netzentgelt-Rabatt nach Netzebene"),
            ("/energiegemeinschaft-steiermark/", "Energiegemeinschaft gründen Steiermark: Netzgebiete und Partner"),
            ("/energiegemeinschaft-kaernten/", "Energiegemeinschaft gründen Kärnten: Netzgebiete und Partner"),
            ("eg_privat", "Energiegemeinschaft für Privathaushalte"),
            ("pv_gewerbe", "Photovoltaik für Betriebe"),
            ("ems", "Lastmanagement mit EMS"),
            ("/referenzen/#gewerbe-oberoesterreich", "40 kWp Gewerbe-Referenz mit 13.500 €/Jahr"),
            ("referenzen", "Alle Referenzen"),
        ]),
        C.contact_section(
            "Kalkulierbare Energiekosten. Sichtbarer Beitrag für die Region.",
            ("Nennen Sie uns Standort, Dachflächen oder Anlagenleistung und die wichtigsten Verbraucher. Wir melden "
             "uns innerhalb eines Werktags mit dem Vorschlag für ein Erstgespräch vor Ort. Unverbindlich und ohne "
             "Verkaufsdruck."),
            page_label="Leistungsseite Energiegemeinschaft Gewerbe",
        ),
        C.finalcta(
            "Ihr Dach kann mehr als Eigenverbrauch",
            ("Potenzialanalyse anfragen und in wenigen Wochen wissen, was Ihre Flächen in einer Energiegemeinschaft "
             "wert sind."),
            cta=("kontakt", "Potenzialanalyse anfragen"),
            trust=[(f"{NAP['rating']} auf Google", True), ("300+ Projekte", False),
                   ("Potenzialanalyse in 2 bis 3 Wochen", False), ("Ein Ansprechpartner bis zum Reporting", False)],
        ),
        f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Beispielkonditionen (EG-Preis 10 bzw. 12 ct je kWh), jede Gemeinschaft legt ihre Preise selbst
      fest. OeMAG-Marktpreis Oktober 2026: {OEMAG_OKT} ct je kWh (Stand November 2026, Quelle oem-ag.at); im September
      lag er bei {OEMAG_SEPT} ct, im Juli 2026 bei {OEMAG_JULI} ct, der Wert schwankt monatlich. Netzentgelt-Abschlag (lokal 57 %, regional 28 %, Netzebene 4/5
      bis 64 %, Werte der geltenden SNE-VO) und Abgabenbefreiung gelten derzeit nur für Mitglieder einer
      Erneuerbare-Energie-Gemeinschaft, nur für die zugeordnete Menge und nur im Nahbereich; die Höhe ab 2027 legt die
      E-Control neu fest (laut E-Control-Entwurf für 2027 49 % lokal, 22 % bzw. 58 % regional, Entwurf). Elektrizitätsabgabe
      2026 befristet 0,82 ct je kWh für Unternehmen und 0,1 ct für Haushalte, ab 2027 wieder 1,5 ct; Erneuerbaren-Förderbeitrag
      und -pauschale 2027 laut Bundesregierung ausgesetzt (Quellen:
      <a href="https://www.parlament.gv.at/aktuelles/news/Nationalrat-beschliesst-Senkung-der-Elektrizitaetsabgabe" target="_blank" rel="noopener">Parlament</a>,
      <a href="https://www.bmf.gv.at/presse/pressemeldungen/2026/november-2026/oekostrompauschale.html" target="_blank" rel="noopener">BMF</a>).
      ElWG-Übergangsphase laut Koordinationsstelle energiegemeinschaften.gv.at (FAQ zum ElWG),
      Stand November 2026. Gründungs- und
      Abrechnungskosten sind marktübliche Spannen. Die belastbare Zahl für Ihren Standort liefert die Potenzialanalyse.
      Keine Garantie, keine Rechts- oder Steuerberatung. Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>""",
    ])
    return body


def build():
    html = page(TITLE, DESC, PATH, body(), faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=IMG["gewerbe_dach"])
    return write_page("leistungen/energiegemeinschaft-gewerbe/index.html", html)


if __name__ == "__main__":
    build()
