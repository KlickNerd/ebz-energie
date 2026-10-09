"""Leistungsseite Energiegemeinschaft fuer Privathaushalte (/leistungen/energiegemeinschaft/).

Quellen: Live-LPs /leistungen/energiegemeinschaft/ und /energiegemeinschaften/ (freigegebene
Inhalte) sowie der Pillar-Ratgeber /energiegemeinschaft/. Der auf der Live-Seite eingebettete
Rechner ist hier durch ein statisches Rechenbeispiel ersetzt (Beispielwerte 10 ct / 14 ct /
4 EUR je Monat, alle mit Sternchen).

Pflicht (README): Netzentgelt-Rabatt 57 % lokal / 28 % regional NUR im Nahbereich,
oesterreichweit = Buergerenergiegemeinschaft ohne Rabatt. energyfamily nur als Text-Badge.
"""

from common import IMG, NAP, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

PATH = "/leistungen/energiegemeinschaft/"
TITLE = "Energiegemeinschaft: bis zu 57 % Netzentgelt sparen | EBZ"
DESC = ("Energiegemeinschaft mit EBZ: Überschuss zu 8 bis 12 ct statt 6,146 ct OeMAG, bis zu 57 % weniger "
        "Netzentgelt im Nahbereich. Beitritt in 4 Schritten.")

FAQ = [
    ("Was ist eine Energiegemeinschaft?",
     "Ein Zusammenschluss von mindestens zwei Teilnehmern, die Strom aus erneuerbaren Quellen, meist "
     "Photovoltaik, gemeinsam erzeugen, teilen und verbrauchen. Der Strom fließt wie bisher über das Netz, "
     "der Netzbetreiber ordnet ihn viertelstundengenau zu, und die Mitglieder zahlen einen selbst "
     "vereinbarten Preis und im Nahbereich bis zu 57 Prozent weniger Netzentgelt."),
    ("Kann ich Strom auch mit Verwandten in einem anderen Bundesland teilen?",
     "Ja. Strom teilen ist österreichweit möglich, zum Beispiel mit der Tante in Wien, über eine "
     "Bürgerenergiegemeinschaft oder ab Oktober 2026 per Peer-to-Peer-Vertrag. Den Netzentgelt-Abschlag "
     "von 57 oder 28 Prozent und die Abgabenbefreiung gibt es aber nur im Nahbereich, also am selben Trafo "
     "oder Umspannwerk."),
    ("Wie viel kann ich sparen?",
     "Abnehmer sparen auf die zugeordnete Menge rund 7 bis 8 Cent je Kilowattstunde aus Netzentgelt und "
     "Abgaben (lokale EEG, Richtwerte 2026) plus die Differenz zwischen Lieferantenpreis und EG-Preis. "
     "Erzeuger bekommen typisch 8 bis 12 Cent statt 6,146 Cent OeMAG-Tarif. Laut Erfahrungsberichten liegt "
     "der Jahresvorteil eines Haushalts bei 100 bis 300 Euro, abhängig von der Zuordnungsquote."),
    ("Brauche ich eine eigene PV-Anlage?",
     "Nein. Sie können als reiner Abnehmer teilnehmen und sparen Netzentgelt und Abgaben auf den EG-Strom. "
     "Mit eigener Photovoltaikanlage profitieren Sie doppelt: Eigenverbrauch plus Überschuss zum EG-Preis "
     "statt zum OeMAG-Tarif."),
    ("Muss ich meinen Stromlieferanten oder den OeMAG-Vertrag kündigen?",
     "Nein, beides bleibt bestehen. Die Gemeinschaft deckt nur den Anteil, der zeitgleich erzeugt und "
     "verbraucht wird. Den Rest liefert weiterhin Ihr Lieferant, nicht zugeordneter Überschuss geht wie "
     "bisher an die OeMAG oder Ihren Einspeisevertrag."),
    ("Welche Voraussetzungen brauche ich?",
     "Einen eigenen Zählpunkt, einen Smart Meter mit aktivierten Viertelstundenwerten (Opt-in im Kundenportal "
     "Ihres Netzbetreibers) und für den Netzentgelt-Rabatt einen Anschluss im Nahbereich der Gemeinschaft. "
     "Ein früheres Smart-Meter-Opt-out muss rückgängig gemacht werden."),
    ("Wie lange dauert der Beitritt und was kostet er?",
     "In der Regel 4 bis 8 Wochen, weil die Zählpunktanmeldung nur zum Monatsersten wirksam wird. "
     "Einrichtungsgebühren sind unüblich, laufend fallen typisch 2 bis 8 Euro je Zählpunkt und Monat an. "
     "Kündigungsfristen liegen bei ein bis drei Monaten."),
]


def _rechenbeispiel():
    """Statischer Ersatz fuer den eingebetteten Rechner: zwei Beispielhaushalte, lokale EEG."""
    rows = [
        ("Ausgangslage",
         "7.000 kWh Überschuss, 60 % zugeordnet (4.200 kWh)",
         "1.000 kWh EG-Strom zugeordnet"),
        ("Mehrerlös Einspeisung",
         "4.200 kWh zu 10 ct* statt 6,146 ct: <b>rund 160 €</b>",
         "entfällt"),
        ("Netzentgelt minus 57 % (lokal)",
         "zusätzlich beim eigenen EG-Bezug",
         "<b>rund 50 €</b>"),
        ("Abgaben entfallen (1,5 ct E-Abgabe, rund 1 ct Förderbeitrag)",
         "zusätzlich beim eigenen EG-Bezug",
         "<b>rund 25 €</b>"),
        ("Energiepreis 14 ct* statt 17 ct* Lieferant",
         "zusätzlich beim eigenen EG-Bezug",
         "<b>rund 30 €</b>"),
        ("Mitgliedsbeitrag 4 € je Monat*",
         "minus 48 €",
         "minus 48 €"),
        ("Netto im Jahr",
         "<b>rund 110 €</b> plus Bezugsvorteil",
         "<b>rund 57 €</b>, bei höherer Zuordnung mehr"),
    ]
    trs = "".join(
        f"<tr><td>{p}</td><td class=\"hl\">{m}</td><td class=\"hl\">{o}</td></tr>" for p, m, o in rows
    )
    return f"""
  <section class="section" id="rechenbeispiel" style="background:#fff;border-block:1px solid var(--line)">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Was bringt mir das?</p>
      <h2 class="center eg-reveal">Rechenbeispiel: ein Jahr in einer lokalen Energiegemeinschaft</h2>
      <p class="lead center eg-reveal" style="max-width:72ch;margin-inline:auto">Vergünstigt wird nur Strom,
      der in derselben Viertelstunde erzeugt und verbraucht wird. Die Zuordnungsquote entscheidet deshalb über
      Ihren Vorteil: etwa 25 % ohne Tagesverbrauch, 40 bis 60 % mit Wärmepumpe, E-Auto oder Homeoffice.*</p>
      <div class="art-tablewrap eg-reveal" style="margin-top:32px">
        <table class="art-table">
          <thead><tr><th>Position</th><th>Haushalt mit 10-kWp-Anlage</th><th>Haushalt ohne PV-Anlage</th></tr></thead>
          <tbody>{trs}</tbody>
        </table>
      </div>
      <p class="form-note center eg-reveal" style="margin-top:18px">*Beispielkonditionen: EG-Einspeisepreis 10 ct,
      EG-Bezugspreis 14 ct, Mitgliedsbeitrag 4 € je Monat, Lieferantenpreis 17 ct, Netznutzung 8 ct, Netzverlust 0,7 ct
      (Richtwerte 2026). OeMAG-Marktpreis Juli 2026: 6,146 ct. Die Konditionen von EBZ nennen wir im Erstgespräch.</p>
      <div class="center eg-reveal" style="margin-top:26px">
        {a('kontakt', 'Ersparnis berechnen lassen', cls='btn btn--primary btn--lg')}
        {a('/energiegemeinschaft-netzkosten/', 'Rechnung Position für Position', cls='btn btn--ghost btn--lg')}
      </div>
    </div>
  </section>"""


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        C.hero(
            eyebrow="Energiegemeinschaft für Privathaushalte",
            h1="Energiegemeinschaft: Solarstrom mit Nachbarn teilen und gemeinsam sparen",
            lead=("Sechs Cent von der OeMAG sind für Ihren Sonnenstrom zu wenig. In einer Energiegemeinschaft "
                  "verkaufen Sie den Überschuss zu einem selbst vereinbarten Preis an Haushalte und Betriebe in der "
                  "Nähe, und wer bezieht, zahlt im Nahbereich bis zu 57 % weniger Netzentgelt. EBZ Energie nimmt Sie "
                  "in eine Gemeinschaft auf und erledigt die Schritte beim Netzbetreiber mit."),
            badges=[("8 bis 12 ct*", "statt 6,146 ct OeMAG"),
                    ("bis zu 57 %", "weniger Netzentgelt lokal"),
                    ("Kein Wechsel", "Lieferant bleibt")],
            img=IMG["eg_drohne"],
            img_alt="Ortschaft mit Photovoltaik auf mehreren Dächern, typisches Netzgebiet einer lokalen Energiegemeinschaft",
            float_num=rating,
            float_label=f"aus {count} Google Bewertungen" if count else "auf Google",
            cta_secondary=("#rechenbeispiel", "Was bringt mir das?"),
        ),
        C.kpis([
            ("57 %", "weniger Netzentgelt in der lokalen EEG"),
            ("8 bis 12 ct*", "EG-Preis statt 6,146 ct OeMAG"),
            ("4 bis 8 Wochen", "vom Erstgespräch bis zum Start"),
            ("rund 330", "Gemeinschaften auf der Partnerplattform energyfamily"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Was ist eine Energiegemeinschaft?",
            paragraphs=[
                ("Eine Energiegemeinschaft ist ein Zusammenschluss von mindestens zwei Teilnehmern, die Strom aus "
                 "erneuerbaren Quellen, in der Praxis fast immer Photovoltaik, gemeinsam erzeugen, teilen und "
                 "verbrauchen. Ein Haushalt speist seinen Überschuss ins Ortsnetz, ein Nachbar, eine Schule oder ein "
                 "Betrieb bezieht ihn, und die Gemeinschaft legt den Preis selbst fest."),
                ("Physikalisch ändert sich nichts, neu ist nur die Zuordnung: Der Smart Meter misst viertelstundengenau, "
                 "der Netzbetreiber rechnet aus, welcher Anteil innerhalb der Gemeinschaft verbraucht wurde, und nur "
                 "dieser Anteil wird zum EG-Preis und mit reduziertem Netzentgelt abgerechnet. Der Rest läuft wie "
                 "bisher über Lieferant und OeMAG."),
            ],
        ),
        C.split_section(
            left={
                "title": "Ich habe eine PV-Anlage: Überschuss zum besseren Preis verkaufen",
                "dark": True,
                "items": [
                    "Einspeisepreis deutlich über dem OeMAG-Tarif, typisch 8 bis 12 ct*",
                    "OeMAG-Vertrag bleibt als Auffangnetz bestehen",
                    "Abends und im Winter sind Sie selbst günstiger Abnehmer",
                    "Speicher und Energiemanagement auf die Gemeinschaft abgestimmt",
                    "Richtwert: plus 150 bis 300 € im Jahr bei 10 kWp**",
                ],
            },
            right={
                "title": "Ich habe keine PV-Anlage: Solarstrom aus der Nachbarschaft beziehen",
                "items": [
                    "EG-Preis unter dem üblichen Arbeitspreis Ihres Lieferanten",
                    "Bis zu 57 % weniger Netzentgelt auf den EG-Strom (lokal)",
                    "Elektrizitätsabgabe von 1,5 ct je kWh entfällt in der EEG",
                    "Keine Investition, kurze Kündigungsfrist, auch für Mieter mit eigenem Zählpunkt",
                    "Richtwert: plus 80 bis 200 € im Jahr, je nach Tagesverbrauch**",
                ],
                "note": "**Richtwerte aus unserem Rechner mit Beispielkonditionen, lokale EEG, Zuordnung 60 %. Ihr Wert hängt von Verbrauchsprofil, Netzebene und Gemeinschaft ab.",
            },
        ),
        C.problem_compare(
            eyebrow="Warum sich das Teilen lohnt",
            h2="Mehr für Ihren Überschuss, weniger für Ihren Bezug",
            intro=("Die OeMAG zahlt für PV-Strom den monatlich festgelegten Marktpreis, im Juli 2026 waren das "
                   "6,146 Cent je Kilowattstunde. In der Energiegemeinschaft bekommt der zugeordnete Überschuss den "
                   "vereinbarten EG-Preis, und der Abnehmer spart auf dieselbe Kilowattstunde Netzentgelt und Abgaben."),
            bars=[
                ("Erlös je kWh Überschuss bei der OeMAG (Juli 2026)", 51, "bad", "6,146 ct"),
                ("Erlös je kWh in der Energiegemeinschaft", 83, "good", "8 bis 12 ct*"),
            ],
            aside=("Ihre Vorteile auf einen Blick", [
                ("€", "Mehrerlös für Überschuss", "EG-Preis statt OeMAG-Marktpreis. Was nicht zugeordnet wird, läuft wie bisher."),
                ("◇", "Bis zu 57 % weniger Netzentgelt", "Netznutzungs- und Netzverlustentgelt sinken um 57 % (lokal) oder 28 % (regional)."),
                ("✓", "Abgaben entfallen", "Elektrizitätsabgabe (1,5 ct je kWh) und Erneuerbaren-Förderbeitrag fallen in der EEG weg."),
                ("⌂", "Kein Wechsel, kein Risiko", "Lieferant und OeMAG-Vertrag bleiben, kurze Kündigungsfrist, keine Einrichtungsgebühr."),
            ]),
        ),
        _rechenbeispiel(),
        C.media_text(
            eyebrow="Nahbereich oder österreichweit",
            h2="Strom teilen geht in ganz Österreich, der Netzentgelt-Rabatt nur im Nahbereich",
            paragraphs=[
                ("Ob Ihre Gemeinschaft lokal oder regional ist, bestimmt nicht die Gemeindegrenze, sondern der "
                 "Netzanschluss: Hängen Erzeuger und Abnehmer an derselben Trafostation, gilt der lokale Abschlag "
                 "von 57 %. Teilen sie sich nur das Umspannwerk, sind es 28 %. Der Netzbetreiber entscheidet das "
                 "anhand der Zählpunktnummer, diese Nahbereichsabfrage übernehmen wir."),
                ("Sie möchten Ihren Sonnenstrom lieber der Tante in Wien zukommen lassen? Auch das geht, über eine "
                 "Bürgerenergiegemeinschaft oder ab 1. Oktober 2026 per Peer-to-Peer-Vertrag. Den Netzentgelt-Rabatt "
                 "und die Abgabenbefreiung gibt es dafür nicht, weil der Strom die übergeordneten Netzebenen nutzt."),
            ],
            img=IMG["gen_eigenheim"],
            alt="Einfamilienhaus mit Photovoltaikanlage, Erzeuger in einer lokalen Energiegemeinschaft",
            bullets=[
                "Lokal (selber Trafo): minus 57 % Netzentgelt, Abgaben entfallen",
                "Regional (selbes Umspannwerk): minus 28 % Netzentgelt, Abgaben entfallen",
                "Österreichweit (Bürgerenergiegemeinschaft): Teilen ja, Rabatt nein",
            ],
            reverse=True,
            cta=("/energiegemeinschaft-privat/", "Ratgeber: Energiegemeinschaft privat"),
        ),
        C.cards_section(
            eyebrow="Voraussetzungen",
            h2="Was Sie für die Teilnahme brauchen",
            intro=("Der Einstieg ist überschaubar. Die meisten Haushalte in Kärnten und der Steiermark erfüllen die "
                   "Voraussetzungen bereits oder mit wenigen Klicks im Kundenportal des Netzbetreibers."),
            cards=[
                {"ic": "◎", "title": "Eigener Zählpunkt",
                 "text": "Die 33-stellige Nummer, beginnend mit AT, steht auf Ihrer Netzrechnung. Hausbesitzer, Mieter und Wohnungseigentümer haben in der Regel einen eigenen."},
                {"ic": "◷", "title": "Smart Meter mit Opt-in",
                 "text": "Standardmäßig übermittelt der Zähler nur Tageswerte. Die Viertelstundenwerte aktivieren Sie per Opt-in im Kundenportal, ein früheres Opt-out muss zurück.",
                 "link_key": "/smart-meter-opt-out/", "link_text": "Smart Meter Opt-out erklärt"},
                {"ic": "⌖", "title": "Nahbereich, sonst nichts Neues",
                 "text": "Für den Netzentgelt-Rabatt liegt Ihr Anschluss am selben Trafo oder Umspannwerk wie die Gemeinschaft. Lieferant und OeMAG-Vertrag bleiben."},
            ],
        ),
        C.facts_panel(
            eyebrow="Abrechnung und Verwaltung",
            h2="Abrechnung über unseren Partner energyfamily",
            intro=('<span class="hero__badge" style="background:var(--petrol);color:#fff"><b>Partner</b> energyfamily</span><br>'
                   "Verwaltung und Abrechnung laufen über die österreichische Plattform energyfamily. Sie sehen "
                   "monatlich in der App, was Sie geliefert oder bezogen haben, Gutschrift und Rechnung laufen automatisch."),
            rows=[
                ("Plattform", "energyfamily, Datenverarbeitung in Österreich, DSGVO-konform"),
                ("Erfahrung", "rund 330 Gemeinschaften, rund 15.000 Nutzer"),
                ("Laufende Kosten", "typisch 2 bis 8 € je Zählpunkt und Monat, keine Einrichtungsgebühr"),
                ("Kündigung", "ein bis drei Monate Frist, keine Austrittsgebühr"),
            ],
            actions=[("Kosten und Abrechnung im Detail", "/energiegemeinschaft-kosten/", "")],
        ),
        C.media_text(
            eyebrow="Förderung und Finanzierung",
            h2="Gefördert wird die Anlage, die Gemeinschaft kommt dazu",
            paragraphs=[
                ("Eine eigene Förderung für die Teilnahme gibt es nicht. Gefördert wird Ihre Photovoltaikanlage über "
                 "den EAG-Investitionszuschuss und die Landesförderungen in Kärnten und der Steiermark, dort mit einem "
                 "Bonus von 125 € je kWp bei Einbindung in ein dezentrales Energiesystem. Wer ein Energiemanagementsystem "
                 "einsetzt, kann seit Juni 2026 zusätzlich die EMS-Förderung des Klimafonds nutzen. Die Anträge bereiten "
                 "wir mit Ihnen vor."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Förderung von Photovoltaik und Energiegemeinschaft",
            bullets=[
                "EAG-Investitionszuschuss für PV-Anlage und Speicher",
                "Landesförderungen Kärnten und Steiermark, 125 €/kWp Steiermark-Bonus bei EG-Einbindung",
                a("/ems-foerderung/", "EMS-Förderung des Klimafonds") + " für das Energiemanagement",
                a("finanzierung", "Finanzierung") + " ab 147 € im Monat inkl. Speicher, Eigentum ab Tag 1",
            ],
            cta=("foerderung_at", "Förderungen 2026 im Überblick"),
        ),
        C.why_section(
            eyebrow="Ihr Partner vor Ort",
            h2="Warum EBZ der richtige Partner für Ihre Energiegemeinschaft ist",
            items=[
                ("⌂", "Regional verankert", "Sitz in Villach, Montage und Betreuung in ganz Kärnten und der Steiermark. Ansprechpartner statt Hotline."),
                ("☀", "Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und Energiegemeinschaft vom selben Team aus zertifizierten Fachkräften."),
                ("▮", "Anlage auf die EG abgestimmt", "Auslegung, Speicher und Energiemanagement sorgen dafür, dass Ihr Überschuss dann anfällt, wenn die Gemeinschaft ihn braucht."),
                ("◎", "Netzbetreiber-Prozesse inklusive", "Nahbereichsabfrage, Zählpunktfreigabe und Anmeldung über das EDA-Portal erledigen wir mit Ihnen."),
                ("✓", "Abrechnung über energyfamily", "Monatliche Abrechnung, App, DSGVO-konform, Datenverarbeitung in Österreich."),
                ("€", "Förderungen geprüft", "EAG-Zuschuss, Kärntner Landesförderung und der Steiermark-Bonus bei EG-Einbindung."),
            ],
        ),
        C.founder_block(
            "Sechs Cent für Ihren Sonnenstrom sind zu wenig. In der Energiegemeinschaft bleibt der Strom im Ort, "
            "und der Mehrwert bei Ihnen und Ihren Nachbarn."
        ),
        C.reference_cards(
            eyebrow="Aus der Praxis",
            h2="Anlagen, die Gemeinschaften tragen",
            intro="Der stärkste Teilnehmer einer Energiegemeinschaft ist ein guter Erzeuger. Drei Anlagen aus über 300 Projekten.",
            items=[
                {"img": IMG["ref_villach"], "alt": "Photovoltaikanlage auf einem Einfamilienhaus in Villach",
                 "title": "Einfamilienhaus, Villach", "specs": "10 kWp Ost-West mit Notstrom, rund 11.000 kWh im Jahr.",
                 "result": "rund 80 %", "result_sub": "weniger Stromkosten"},
                {"img": IMG["ref_krumpendorf"], "alt": "Photovoltaikanlage auf einem Mehrparteienhaus in Krumpendorf",
                 "title": "Mehrparteienhaus, Krumpendorf", "specs": "25 kWp mit 25 kWh Speicher und Notstrom.",
                 "result": "4 Tage", "result_sub": "Bauzeit"},
                {"img": IMG["gewerbe_dach"], "alt": "Große Photovoltaikanlage auf einem Gewerbedach in Oberösterreich",
                 "title": "Gewerbe, Oberösterreich", "specs": "40 kWp Ost-West, 40 kWh Speicher, rund 40.000 kWh im Jahr.",
                 "result": "13.500 €", "result_sub": "Ersparnis pro Jahr"},
            ],
        ),
        C.reviews_slider(reviews, rating, count),
        C.steps_section(
            eyebrow="So einfach geht es",
            h2="In 4 Schritten zur ersten EG-Kilowattstunde",
            steps=[
                ("Eignung prüfen",
                 "Sie nennen uns PLZ, Zählpunktnummer, PV-Leistung und Verbrauch. Wir prüfen beim Netzbetreiber, ob eine lokale oder regionale Gemeinschaft passt.",
                 "1 Werktag"),
                ("Konditionen und Vertrag",
                 "Einspeise- und Bezugspreis, Beitrag und Kündigungsfrist schwarz auf weiß. Erst dann unterschreiben Sie.",
                 "Ihr Tempo"),
                ("Zählpunkt freigeben",
                 "Im Kundenportal Ihres Netzbetreibers bestätigen Sie die Teilnahme und aktivieren die Viertelstundenwerte. Wir zeigen Ihnen die Klicks.",
                 "10 Minuten"),
                ("Start und Abrechnung",
                 "Ab dem Folgemonat wird Ihr Strom zugeordnet. In der energyfamily-App sehen Sie monatlich, was Sie geliefert oder bezogen haben.",
                 "ab Monatserstem"),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section("Ratgeber rund um die Energiegemeinschaft", [
            ("eg", "Energiegemeinschaft: der Leitartikel"),
            ("/energiegemeinschaft-beitreten/", "Beitreten in vier Schritten"),
            ("/energiegemeinschaft-kosten/", "Kosten und Abrechnung"),
            ("/energiegemeinschaft-netzkosten/", "Netzkosten im Detail"),
            ("/energiegemeinschaft-kaernten/", "Energiegemeinschaft Kärnten"),
            ("/energiegemeinschaft-steiermark/", "Energiegemeinschaft Steiermark"),
            ("/energiegemeinschaft-privat/", "Energiegemeinschaft privat: Familie und Nachbarn"),
            ("/ems-foerderung/", "EMS-Förderung des Klimafonds"),
            ("eg_gewerbe", "Für Betriebe und Gemeinden"),
            ("referenzen", "Referenzen"),
        ]),
        C.contact_section(
            "Eignung in 10 Minuten prüfen lassen",
            ("Nennen Sie uns Postleitzahl, PV-Leistung und Jahresverbrauch. Wir sagen Ihnen, welche Gemeinschaft "
             "infrage kommt, was sie bringt und welche Konditionen gelten. Kostenlos und unverbindlich."),
        ),
        C.finalcta(
            "Mit eigener PV zum starken Teil der Gemeinschaft",
            ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, Montage und "
             "EG-Anbindung aus einer Hand übernimmt."),
            trust=[(f"{NAP['rating']} auf Google", True), ("Lieferant bleibt", False),
                   ("Start in 4 bis 8 Wochen", False), ("Kündigungsfrist 1 bis 3 Monate", False)],
        ),
        f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*EG-Preise sind Beispielwerte (Einspeisung 10 ct, Bezug 14 ct, Beitrag 4 € je Monat),
      jede Gemeinschaft legt ihre Konditionen selbst fest. Netzentgelt-Abschlag und Abgabenbefreiung gelten nur für
      die zugeordnete Menge und nur im Nahbereich (lokal 57 %, regional 28 %). Keine Garantie, keine Steuerberatung.
      Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>""",
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=IMG["eg_drohne"])
    return write_page("leistungen/energiegemeinschaft/index.html", html)


if __name__ == "__main__":
    build()
