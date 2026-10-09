"""Leistungsseite Energiemanagementsystem (/energiemanagementsystem/).

Quellen: bestehende EMS-Landingpage /ems-lp-2/ (Inhalte freigegeben) und der
Ratgeber /ems-foerderung/ (Klimafonds-Zahlen 2026). Roter Faden: Hook ->
Definition + Vernetzung -> Problem (Eigenverbrauch 30 vs. 80 %) -> sechs Nutzen ->
Privat/Gewerbe -> Foerderung 2026 (erst registrieren, dann Rechnung) ->
Smart Meter + dynamischer Tarif -> Energiegemeinschaft -> warum EBZ -> Beweis ->
Ablauf -> FAQ -> Cluster -> Kontakt.
"""

from common import IMG, NAP, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

PATH = "/energiemanagementsystem/"
TITLE = "Energiemanagementsystem: bis 80 % Eigenverbrauch | EBZ"
DESC = ("EMS für Eigenheim und Gewerbe: Eigenverbrauch von 30 auf bis zu 80 %, dynamische Tarife, "
        "Überschussladen, Förderung 2026 bis 600 €. Fachbetrieb aus Villach.")

FAQ = [
    ("Was genau macht ein Energiemanagementsystem?",
     "Ein EMS ist die Steuerzentrale Ihres Energiesystems. Es misst laufend Erzeugung und Verbrauch und "
     "lenkt den Strom automatisch dorthin, wo er am meisten wert ist: in den direkten Verbrauch, in den "
     "Speicher, in die Wärmepumpe oder ins E-Auto. So steigt Ihre Eigenverbrauchsquote und Sie kaufen "
     "weniger teuren Netzstrom zu."),
    ("Lohnt sich ein EMS auch für Privathaushalte?",
     "Ja, besonders in Kombination mit Wärmepumpe oder E-Auto. Dort entstehen die größten Sparpotenziale, "
     "weil sich diese flexiblen Verbraucher an die Sonnenstunden und an günstige Tarifzeiten anpassen lassen. "
     "Schon bei einer PV-Anlage mit Speicher sorgt ein EMS dafür, dass Ihr Sonnenstrom nicht ungenutzt ins "
     "Netz wandert."),
    ("Funktioniert ein EMS auch mit meiner bestehenden Anlage?",
     "In den meisten Fällen ja. Ein EMS lässt sich nachrüsten und bindet Ihre vorhandenen Komponenten ein, "
     "Sie müssen nichts neu kaufen. In der kostenlosen Analyse prüfen wir, welche Systeme mit Ihrer Technik "
     "kompatibel sind und den größten Nutzen bringen."),
    ("Wie viel kann ich mit einem EMS sparen?",
     "Das hängt von Anlage, Verbrauch und Tarif ab. Typischerweise steigt die Eigenverbrauchsquote von rund "
     "30 % auf 60 bis 80 %. Jede zusätzlich selbst genutzte Kilowattstunde spart den vollen Strompreis statt "
     "nur den Einspeisetarif. Wie viel es in Ihrem Fall ist, rechnen wir individuell."),
    ("Brauche ich einen dynamischen Stromtarif dafür?",
     "Nein. Ein EMS bringt auch ohne dynamischen Tarif klare Vorteile beim Eigenverbrauch. Mit Smart Meter und "
     "variablem Tarif kommt ein weiterer Hebel dazu: Ihr System lädt und verbraucht automatisch dann, wenn der "
     "Börsenstrom am günstigsten ist. Wir beraten Sie, ob sich das für Sie lohnt."),
    ("Wie hoch ist die EMS-Förderung 2026?",
     "Der Klima- und Energiefonds fördert Energiemanagementsysteme 2026 erstmals eigenständig: Private Haushalte "
     "erhalten 50 % der Kosten, maximal 600 €. Betriebe, Gemeinden und Vereine bekommen bis zu 30 %, maximal "
     "20.000 € pro Standort. Registrierung längstens bis 15. April 2027, solange Budget vorhanden ist."),
    ("Was ist bei der Förderung die häufigste Fehlerquelle?",
     "Die Reihenfolge. Haushalte müssen sich online registrieren, bevor die erste Rechnung gelegt wird. Betriebe "
     "stellen den Antrag vor der ersten verbindlichen Bestellung. Wer zuerst kauft und dann einreicht, verliert "
     "die Förderung vollständig. EBZ Energie übernimmt die Registrierung zum richtigen Zeitpunkt."),
    ("Welche Systeme verbaut EBZ Energie?",
     "Wir arbeiten herstellerunabhängig und wählen das EMS, das zu Ihrer Technik und Ihren Zielen passt, statt "
     "Sie an ein einzelnes Produkt zu binden. Entscheidend ist, dass alle Komponenten sauber zusammenspielen "
     "und das System den Förderkriterien entspricht."),
]


def _foerder_hinweis():
    """A-Box-artiger Hinweis zur Reihenfolge bei der Foerderung (wird in die Preis-Sektion eingesetzt)."""
    return (
        '<div class="art-box art-box--p eg-reveal" style="margin:32px auto 0;max-width:920px">'
        '<h3>Erst registrieren, dann Rechnung</h3>'
        '<p>Die Förderung gibt es nur, wenn die Reihenfolge stimmt: Private Haushalte registrieren sich online '
        'bei der Umweltförderung, <b>bevor</b> die erste Rechnung gelegt wird. Betriebe reichen den Antrag ein, '
        '<b>bevor</b> sie verbindlich bestellen. Danach bleiben sechs Monate für Installation und Abrechnung. '
        'Wer zuerst kauft, geht leer aus. Wir planen die Registrierung deshalb gemeinsam mit Ihrem Angebot. '
        f'Alle Details: {a("/ems-foerderung/", "Ratgeber EMS-Förderung 2026")}.</p>'
        '</div>'
    )


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        # 1. Hook
        C.hero(
            eyebrow="Energiemanagement für Privat und Gewerbe · Kärnten und Steiermark",
            h1="Ihre Anlage produziert Strom. Ein Energiemanagementsystem sorgt dafür, dass Sie ihn auch nutzen.",
            lead=("PV, Speicher, Wärmepumpe und Wallbox arbeiten bei den meisten Anlagen nebeneinander her, "
                  "statt zusammen. Ein EMS verbindet alles und lenkt jede Kilowattstunde automatisch dorthin, "
                  "wo sie am meisten wert ist. Das Ergebnis: weniger Netzbezug, höherer Eigenverbrauch und "
                  "volle Kontrolle per App."),
            badges=[("Hersteller", "unabhängig"),
                    ("Privat", "und Gewerbe"),
                    ("Auch zum", "Nachrüsten")],
            img=IMG["ems"],
            img_alt="Energiemanagementsystem vernetzt Photovoltaik, Speicher, Wärmepumpe und Wallbox im Eigenheim",
            float_num=rating,
            float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_primary=("kontakt", "Kostenlose EMS-Beratung"),
            cta_secondary=("#foerderung", "Förderung 2026"),
        ),
        C.kpis([
            ("bis 80 %", "Eigenverbrauch statt rund 30 %"),
            ("1 System", "für Strom, Wärme und Mobilität"),
            ("bis 600 €", "EMS-Förderung 2026 für Haushalte"),
            ("24/7", "automatische Optimierung"),
        ]),
        # 2. Definition (GEO) + Vernetzungsgrafik
        C.text_block(
            eyebrow="Was ist ein EMS?",
            h2="Das Gehirn Ihrer Energie: Es verbindet, was bisher nur nebeneinander lief",
            paragraphs=[
                ("Ein Energiemanagementsystem (EMS) ist die Steuerzentrale Ihres Zuhauses oder Betriebs. Es misst "
                 "in Echtzeit, wie viel Strom Ihre PV-Anlage produziert und wie viel jedes Gerät gerade braucht, "
                 "und entscheidet automatisch, wohin jede Kilowattstunde fließt: direkt in den Verbrauch, in den "
                 "Speicher, in die Wärmepumpe oder ins E-Auto."),
                ("Im Gewerbe kappt es zusätzlich Lastspitzen und senkt so Netzentgelte und Leistungspreis. "
                 "Das System arbeitet rund um die Uhr, Sie sehen das Ergebnis in einer App."),
            ],
        ),
        C.hub_section(
            eyebrow="Vernetzung statt Einzelteile",
            h2="Ohne EMS arbeitet jede Komponente für sich. Mit EMS arbeiten alle für Ihr Konto.",
            lead=("Das EMS sitzt in der Mitte und kennt PV-Produktion, Speicherstand, Wärmebedarf, Ladestand "
                  "des E-Autos und den aktuellen Strompreis. Daraus entsteht ein Fahrplan, der täglich neu gerechnet wird."),
            points=[
                ("☀", "Direkt verbrauchen statt teuer einspeisen und zurückkaufen."),
                ("▮", "Den Speicher laden, wenn Überschuss da ist oder der Börsenstrom günstig ist."),
                ("♨", "Die Wärmepumpe laufen lassen, wenn die Sonne scheint (SG-Ready)."),
                ("⌖", "Das E-Auto mit reinem PV-Überschuss laden."),
                ("◎", "Im Gewerbe: Lastspitzen kappen und Netzkosten senken."),
            ],
        ),
        # 3. Problem in Zahlen
        C.problem_compare(
            eyebrow="Das kostet Sie bares Geld",
            h2="Ohne Steuerung verschenken Sie jeden Tag Strom",
            intro=("Jede Kilowattstunde, die Sie mittags für ein paar Cent einspeisen und abends für 25 Cent und "
                   "mehr zurückkaufen, ist ein Verlustgeschäft. Bei den meisten Anlagen lädt der Speicher zur "
                   "falschen Zeit, die Wärmepumpe läuft nachts auf Netzstrom, das E-Auto zieht zum vollen Tarif. "
                   "Ein EMS dreht diese Logik um, automatisch, Tag für Tag."),
            bars=[
                ("Eigenverbrauch Ihrer PV-Anlage ohne EMS", 30, "bad", "rund 30 %*"),
                ("Eigenverbrauch mit EMS, Speicher und flexiblen Verbrauchern", 80, "good", "bis 80 %*"),
            ],
            aside=("Was sich mit EMS ändert", [
                ("☀", "Mittags nutzen", "Überschuss geht in Speicher, Wärmepumpe und Auto statt ins Netz."),
                ("◔", "Zur richtigen Zeit", "Laden und heizen, wenn Strom günstig oder gratis ist."),
                ("€", "Volle Ersparnis", "Jede selbst genutzte Kilowattstunde spart den vollen Strompreis."),
                ("◎", "Alles sichtbar", "Produktion, Verbrauch und Ersparnis live in einer App."),
            ]),
        ),
        # 4. Sechs Nutzen (aus der freigegebenen LP)
        C.cards_section(
            eyebrow="Ihre Sparpotenziale",
            h2="Sechs Hebel, mit denen ein EMS bares Geld herausholt",
            intro=("Welche Hebel bei Ihnen greifen, hängt von Ihren Komponenten und Ihrem Tarif ab. "
                   "Die kostenlose Analyse zeigt es ehrlich."),
            cards=[
                {"ic": "☀", "title": "Eigenverbrauch maximieren",
                 "text": "Statt einzuspeisen und teuer zurückzukaufen, nutzen Sie Ihren Sonnenstrom selbst. Die Eigenverbrauchsquote steigt oft von rund 30 % auf 60 bis 80 %."},
                {"ic": "◔", "title": "Dynamische Tarife nutzen",
                 "text": "Mit Smart Meter und variablem Stromtarif verbraucht und lädt Ihr System automatisch dann, wenn der Börsenstrom am günstigsten ist.",
                 "link_key": "/dynamischer-stromtarif/", "link_text": "Ratgeber dynamischer Tarif"},
                {"ic": "⌖", "title": "Überschussladen fürs E-Auto",
                 "text": "Die Wallbox lädt bevorzugt mit PV-Überschuss. So fahren Sie mit selbst produziertem Strom, nahezu zum Nulltarif."},
                {"ic": "♨", "title": "Wärmepumpe PV-optimiert",
                 "text": "Das EMS erzeugt Wärme und Warmwasser bevorzugt bei Sonnenschein über die SG-Ready-Schnittstelle und senkt so Ihre Heizkosten spürbar.",
                 "link_key": "waermepumpe", "link_text": "Zur Wärmepumpe"},
                {"ic": "▮", "title": "Lastspitzen kappen",
                 "text": "Besonders im Gewerbe: Das EMS glättet teure Leistungsspitzen über den Speicher und senkt Netzentgelte und Leistungspreis.",
                 "link_key": "batteriespeicher", "link_text": "Zum Batteriespeicher"},
                {"ic": "◎", "title": "Volle Transparenz",
                 "text": "Sie sehen live, was produziert, verbraucht und gespart wird, decken Stromfresser auf und behalten alles per App im Griff."},
            ],
        ),
        # 5. Privat / Gewerbe
        C.audience_split(
            eyebrow="Für Ihr Zuhause und Ihren Betrieb",
            h2="Ein EMS, zwei Welten: Wir planen es passend für Sie",
            intro="Wählen Sie, was auf Sie zutrifft. Systemwahl, Einbindung und Förderweg richten wir danach aus.",
            left={
                "img": IMG["gen_eigenheim"],
                "alt": "Einfamilienhaus mit Photovoltaik, Speicher und Wallbox in Kärnten",
                "title": "Privat: mehr Unabhängigkeit und Komfort",
                "bullets": [
                    "Sonnenstrom rund um die Uhr optimal genutzt",
                    "E-Auto günstig mit PV-Überschuss laden",
                    "Wärmepumpe und Warmwasser automatisch steuern",
                    "Dynamische Tarife ohne Aufwand ausnutzen",
                    "Alles per App, kein Fachwissen nötig",
                ],
                "cta": ("kontakt", "Für mein Zuhause anfragen"),
            },
            right={
                "img": IMG["gen_gewerbe"],
                "alt": "Gewerbebetrieb mit großer Photovoltaikanlage auf dem Dach",
                "title": "Gewerbe: kalkulierbare Energiekosten",
                "bullets": [
                    "Lastspitzenmanagement senkt Leistungspreis und Netzentgelte",
                    "Lademanagement für Fuhrpark und Ladeparks",
                    "Energiedaten für ESG-Reporting und Energieaudits",
                    "Skalierbar über mehrere Standorte und Verbraucher",
                    "Bessere Amortisation der gesamten Energieinvestition",
                ],
                "cta": ("kontakt", "Für meinen Betrieb anfragen"),
            },
        ),
        # 6. Foerderung 2026 (prominent)
        C.price_cards(
            eyebrow="EMS-Förderung 2026",
            h2="Der Klimafonds zahlt mit: bis zu 600 € für Haushalte, bis zu 20.000 € für Betriebe",
            intro=("Der Klima- und Energiefonds fördert 2026 erstmals eigenständig Energiemanagementsysteme, die "
                   "mindestens zwei Komponenten wie PV-Anlage, Speicher, Wärmepumpe oder Ladestelle aktiv steuern. "
                   "Budget: 4,9 Millionen Euro, Registrierung längstens bis 15. April 2027."),
            items=[
                {"size": "Private Haushalte", "price": "50 %", "price_sub": "der Kosten, maximal 600 €",
                 "features": ["Steuerung, Messtechnik, Installation und Konfiguration förderfähig",
                              "Plus 100 € Bonus bei Teilnahme an der Begleitforschung",
                              "Online-Registrierung vor der ersten Rechnung",
                              "Sechs Monate Zeit für Installation und Abrechnung"]},
                {"size": "Betriebe, Gemeinden, Vereine", "price": "bis 30 %", "price_sub": "der Nettokosten, maximal 20.000 € je Standort",
                 "features": ["Auch Beratung, Planung und Standortanalyse förderfähig",
                              "Großunternehmen bis zu 20 %",
                              "Antrag vor der ersten verbindlichen Bestellung",
                              "Bis zu fünf Standorte je Unternehmen"]},
                {"size": "Was EBZ Energie übernimmt", "price": "Alles", "price_sub": "aus einer Hand",
                 "features": ["Förderfähige Technik: aktive Steuerung, Preissignale, lokale Steuerung",
                              "Registrierung und Antrag zum richtigen Zeitpunkt",
                              "EMS-Kosten als eigene Position im Angebot",
                              "Nachweise und Endabrechnung mit Fachbetriebs-Bestätigung",
                              a("kontakt", "Förderung sichern →")]},
            ],
            note=("Typische EMS-Kosten im Einfamilienhaus: 800 bis 1.500 €* inklusive Installation. Nach Abzug der "
                  "Förderung bleiben oft nur wenige hundert Euro Eigenanteil. Fünf Jahre Betrieb mit einer von sechs "
                  "Optionen, zum Beispiel dynamischer Stromtarif oder Teilnahme an einer Energiegemeinschaft."),
        ).replace('<section class="section"', '<section id="foerderung" class="section"', 1)
         .replace('<p class="form-note center eg-reveal" style="margin-top:22px">',
                  _foerder_hinweis() + '<p class="form-note center eg-reveal" style="margin-top:22px">', 1),
        # 7. Smart Meter + dynamischer Tarif
        C.media_text(
            eyebrow="Smart Meter und dynamischer Stromtarif",
            h2="Der zweite Hebel: Strom kaufen, wenn er günstig ist",
            paragraphs=[
                ("Der Smart Meter erfasst Ihren Verbrauch in Viertelstundenwerten. Damit wird ein dynamischer "
                 "Stromtarif möglich, der stundengenau nach Börsenpreis abrechnet. Ein EMS macht daraus ohne Ihr "
                 "Zutun einen Vorteil: Es lädt den Speicher oder das E-Auto in günstigen Stunden und meidet die "
                 "teuren."),
                ("Das ist auch die Brücke zur Förderung: Ein dynamischer Liefervertrag ist eine der sechs Optionen, "
                 "mit denen Sie die fünfjährige Betriebsverpflichtung des Klimafonds erfüllen. Ob sich der Tarif "
                 "für Ihr Verbrauchsprofil rechnet, zeigen wir Ihnen mit Zahlen."),
            ],
            img=IMG["gen_detail"],
            alt="Fachkraft von EBZ Energie bei der Einbindung von Steuerungstechnik an einer Photovoltaikanlage",
            bullets=[
                "Smart Meter: Voraussetzung für stundengenaue Abrechnung",
                "Dynamischer Tarif: Börsenpreis statt Fixpreis, automatisch genutzt",
                "Regelbare Netztarife ab 2027: Wer Lasten steuert, spart doppelt",
            ],
            cta=("/smart-meter/", "Ratgeber Smart Meter"),
            reverse=True,
        ),
        # 8. Energiegemeinschaft
        C.media_text(
            eyebrow="Energiegemeinschaft",
            h2="Überschuss teilen statt verschenken",
            paragraphs=[
                ("Was auch ein EMS nicht im Haus unterbringt, muss nicht für wenige Cent ins Netz. In einer "
                 "Energiegemeinschaft teilen Sie Ihren Überschuss mit Nachbarn oder Verwandten, österreichweit "
                 "möglich. Im Nahbereich sparen die Bezieher zusätzlich beim Netzentgelt, bis zu 57 % lokal und "
                 "28 % regional. Österreichweites Teilen funktioniert als Bürgerenergiegemeinschaft ohne diesen Rabatt."),
                ("Das EMS legt Ihren Verbrauch in die Stunden, in denen die Gemeinschaft Überschuss hat. Die "
                 "Teilnahme an einer lokalen oder regionalen Energiegemeinschaft zählt außerdem als Option für die "
                 "EMS-Förderung."),
            ],
            img=IMG["eg_drohne"],
            alt="Wohngebiet aus der Luft: Nachbarn teilen Sonnenstrom in einer Energiegemeinschaft",
            bullets=[
                "Strom teilen mit Nachbarn oder der Familie in einem anderen Bundesland",
                "Netzentgelt-Rabatt nur im Nahbereich, bis zu 57 % lokal",
                "Abrechnung über die Plattform energyfamily",
            ],
            cta=("eg_privat", "Zur Energiegemeinschaft"),
            dark=True,
        ),
        # 9. Warum EBZ
        C.why_section(
            eyebrow="Ihr Handwerkspartner",
            h2="Ein EMS ist nur so gut wie die Hand, die es installiert und einstellt",
            items=[
                ("◇", "Herstellerunabhängig", "Wir empfehlen das System, das zu Ihnen passt, nicht umgekehrt. Neutral beraten, sauber umgesetzt."),
                ("☀", "Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EMS von einem Partner. Kein Schnittstellen-Chaos."),
                ("✓", "Zertifizierte Fachkräfte", "Festangestelltes Team aus zertifizierten Elektro-Fachkräften, volle Verantwortung bei uns."),
                ("⌂", "Auch zum Nachrüsten", "Ihr EMS funktioniert auch mit Ihrer bestehenden PV-Anlage. Sie müssen nichts neu kaufen."),
                ("€", "Förderung mitgedacht", "Förderfähige Technik, Registrierung zum richtigen Zeitpunkt, Endabrechnung inklusive."),
                ("◎", "Service über Jahre", "Monitoring, Wartung und ein direkter Draht zu unserem Team, auch nach der Inbetriebnahme."),
            ],
        ),
        C.founder_block(
            "Eine PV-Anlage ist ein guter Anfang. Erst mit einem durchdachten Energiemanagement holen Sie das "
            "Maximum heraus. Wir sorgen dafür, dass jede Kilowattstunde für Sie arbeitet."
        ),
        C.reviews_slider(reviews, rating, count),
        # 10. Ablauf
        C.steps_section(
            eyebrow="So einfach geht es",
            h2="In vier Schritten zu einem System, das für Sie mitdenkt",
            steps=[
                ("Analyse Ihrer Anlage", "Wir erfassen Komponenten, Verbraucher, Tarif und Ziele und zeigen ehrlich, welches Sparpotenzial in Ihrer Anlage steckt.", "kostenlos"),
                ("Herstellerunabhängige Auswahl", "Wir wählen das EMS, das zu Ihrer Technik passt und förderfähig ist. Inklusive transparentem Angebot mit eigener EMS-Position.", ""),
                ("Registrierung und Einbindung", "Erst die Förderregistrierung, dann binden unsere zertifizierten Fachkräfte alle Komponenten ein und konfigurieren das System.", ""),
                ("Optimierung und Service", "Nach dem Feintuning behalten Sie alles per App im Blick und haben einen direkten Ansprechpartner für die kommenden Jahre.", ""),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section("Weiterlesen zum Energiemanagement", [
            ("/ems-foerderung/", "EMS-Förderung 2026"),
            ("/smart-meter/", "Smart Meter"),
            ("/dynamischer-stromtarif/", "Dynamischer Stromtarif"),
            ("eg", "Energiegemeinschaft"),
            ("batteriespeicher", "Batteriespeicher"),
            ("waermepumpe", "Wärmepumpe"),
            ("/pv-speicher-nachruesten/", "PV-Speicher nachrüsten"),
            ("referenzen", "Referenzen"),
        ]),
        C.contact_section(
            headline="Machen Sie mehr aus dem Strom, den Sie ohnehin produzieren",
            sub=("Ob Sie schon eine PV-Anlage haben oder gerade planen: Wir zeigen Ihnen in einem kostenlosen "
                 "Gespräch, wie viel ein Energiemanagementsystem in Ihrem Fall herausholt. Ohne Verkaufsdruck, "
                 "dafür mit ehrlicher Rechnung."),
        ),
        C.finalcta(
            "Jede Kilowattstunde zählt. Lassen Sie sie für sich arbeiten.",
            "Ob Privat oder Gewerbe: Wir rechnen kostenlos nach, was ein EMS bei Ihnen bringt, und sichern die "
            "Förderung in der richtigen Reihenfolge.",
            cta=("kontakt", "Kostenlose EMS-Beratung"),
            trust=[(f"{NAP['rating']} auf Google", True), ("Herstellerunabhängig", False),
                   ("Auch zum Nachrüsten", False), ("Förderung inklusive", False)],
        ),
        _footnote(),
    ])

    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ), og_image=IMG["ems"])
    return write_page("energiemanagementsystem/index.html", html)


def _footnote():
    return (f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte, abhängig von Anlage, Verbrauch und Tarif. Eigenverbrauchsquoten auf
      Basis typischer Anlagen mit Speicher und flexiblen Verbrauchern, EMS-Kosten für marktübliche Systeme
      inklusive Installation. Förderangaben laut Leitfaden des Klima- und Energiefonds (Juni 2026), maßgeblich
      sind die offiziellen Förderbedingungen. Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import theme
    theme.write_assets()
    build()
