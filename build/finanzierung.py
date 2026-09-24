"""Leistungsseite Finanzierung (/finanzierung/).

Quelle der Zahlen: Finanzierungsbeilage "powered by Cloover" (common.FINANZIERUNG).
Botschaft: Kaufen oder finanzieren, in beiden Faellen gehoert die Anlage ab Tag 1
dem Kunden. Kein Mietmodell. Der Begriff "Leasing" darf nicht vorkommen (Validator).
"""

from common import IMG, NAP, AUTHOR, AUTHOR_ROLE, FINANZIERUNG as F, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

PATH = "/finanzierung/"
TITLE = "PV-Anlage finanzieren: 0 € Anzahlung, fixe Rate | EBZ Energie"
DESC = ("PV-Anlage finanzieren: 0 € Anzahlung, fixe Rate bis 25 Jahre, Eigentum ab Tag 1, volle Förderung. "
        "Beispiel 10 kWp mit Speicher ab 164 € im Monat, Zusage in Minuten.")

FAQ = [
    ("Gehört mir die Anlage bei der Finanzierung wirklich ab dem ersten Tag?",
     "Ja. Sie kaufen die Anlage von EBZ Energie und finanzieren den Kaufpreis über unseren Partner Cloover. "
     "Die Anlage ist ab der Montage Ihr Eigentum, es gibt keinen Eigentumsvorbehalt bis zur letzten Rate, "
     "keinen Grundbucheintrag und kein Mietmodell."),
    ("Wie hoch ist die monatliche Rate?",
     "Das hängt von Anlagengröße und Laufzeit ab. Zwei repräsentative Beispiele über 25 Jahre: 15.000 Euro "
     "(8 kWp, abzüglich 900 Euro Förderung) ab 102 Euro im Monat, 25.000 Euro (10 kWp mit 10-kWh-Speicher, "
     "abzüglich 3.000 Euro Förderung) ab 164 Euro im Monat. Ihre konkrete Rate steht im Angebot."),
    ("Bekomme ich die Förderung, obwohl ich finanziere?",
     "Ja, in voller Höhe. Weil Sie Eigentümer und Antragsteller sind, erhalten Sie als Privatperson die "
     "Bundesförderung und die Landesförderung auf Ihr Konto. Im Beispiel wird der Bundes-Investitionszuschuss "
     "direkt vom Finanzierungsbetrag abgezogen, Landesförderungen wie die Kärntner Speicherpauschale kommen "
     "zusätzlich dazu."),
    ("Wie läuft die Bonitätsprüfung ab?",
     "Digital und in wenigen Minuten, ohne Banktermin. Die Finanzierungszusage kommt in der Regel in unter "
     "zwei Minuten, die Annahmequote liegt bei 94 Prozent. Die Vergabe erfolgt vorbehaltlich dieser Prüfung. "
     "Auch Selbständige und Pensionisten können finanzieren."),
    ("Kann ich die Finanzierung vorzeitig zurückzahlen?",
     "Ja, Sondertilgungen sind jederzeit kostenlos möglich. Sie können die Restsumme ganz oder teilweise "
     "früher ablösen, die fixe Rate bleibt bis dahin gleich."),
    ("Was ist der Unterschied zu einer gemieteten Solaranlage?",
     "Bei Mietmodellen bleibt die Anlage Eigentum des Anbieters, die Förderung geht an ihn, und nach 20 "
     "Jahren gehört Ihnen die Anlage weiterhin nicht. Bei der EBZ-Finanzierung sind Sie ab Tag 1 Eigentümer, "
     "die Rate endet mit der Laufzeit und die Förderung fließt an Sie. Der Ratgeber „Solaranlage mieten, "
     "kaufen oder finanzieren?“ rechnet beide Modelle über 20 Jahre durch."),
    ("Lohnt sich die Finanzierung gegenüber der bisherigen Stromrechnung?",
     "Im repräsentativen Beispiel zahlt ein 4-Personen-Haushalt mit 7.000 kWh heute rund 163 Euro Strom im "
     "Monat. Mit PV-Anlage und Speicher bleiben rund 20 bis 30 Euro Reststrom, dazu kommt die fixe Rate. "
     "Die Rate ist planbar und endet, die Stromrechnung ohne PV steigt tendenziell weiter."),
]


def build():
    rating, count, reviews = load_reviews()
    k, g = F["beispiel_klein"], F["beispiel_gross"]
    body = "".join([
        C.hero(
            eyebrow="Faire Finanzierung",
            h1="Ihre PV-Anlage: direkt kaufen oder finanzieren. Sie entscheiden.",
            lead=("Keine Anzahlung, eine fixe Monatsrate und eine Anlage, die vom ersten Tag an Ihnen gehört. "
                  "Die Finanzierungszusage kommt digital in wenigen Minuten, die Förderung bleibt bei Ihnen."),
            badges=[("0 €", "Anzahlung"), ("Fixe Rate", "kein Zinsrisiko"), ("Volle Förderung", "trotz Finanzierung")],
            img=IMG["gen_eigenheim"],
            img_alt="Einfamilienhaus mit finanzierter Photovoltaikanlage in Kärnten",
            float_num=rating, float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_secondary=("#beispiele", "Beispielraten ansehen"),
        ),
        C.kpis([
            (F["anzahlung"], "Anzahlung"),
            ("Fixe Rate", "über die gesamte Laufzeit"),
            ("< 2 Min.", "digitale Finanzierungszusage"),
            (F["annahmequote"], "Annahmequote"),
        ]),
        C.problem_compare(
            eyebrow="Stromkosten heute und mit eigener Anlage",
            h2="Aus der Stromrechnung wird eine Rate, die endet",
            intro=("Ein 4-Personen-Haushalt mit 7.000 kWh zahlt bei 28 ct/kWh rund 163 € im Monat, Tendenz "
                   "steigend. Mit PV-Anlage und Speicher decken Sie bis zu 80 % Ihres Bedarfs selbst, "
                   "übrig bleibt ein kleiner Reststrom.*"),
            bars=[
                ("Stromkosten ohne PV-Anlage", 100, "bad", f"rund {F['strom_heute']} im Monat*"),
                ("Reststrom mit PV-Anlage und Speicher", 16, "good", f"rund {F['strom_mit_pv']} im Monat*"),
            ],
            aside=("Was die Finanzierung ersetzt", [
                ("€", "Keine Einmalzahlung", "0 € Anzahlung, der Kaufpreis wird zur fixen Monatsrate."),
                ("✓", "Kein Preisrisiko", "Die Rate bleibt über die gesamte Laufzeit gleich."),
                ("⌂", "Kein Grundbucheintrag", "Ihr Haus bleibt vollständig unbelastet."),
                ("◷", "Rate endet", "Nach der Laufzeit produziert die Anlage weiter, nur für Sie."),
            ]),
        ),
        C.price_cards(
            eyebrow="Zwei repräsentative Beispiele",
            h2="So sieht die Monatsrate aus",
            intro=("Beispiele unseres Finanzierungspartners Cloover über 25 Jahre Laufzeit. Die Förderung "
                   "des Bundes wird direkt vom Finanzierungsbetrag abgezogen, die Anlage gehört Ihnen ab Tag 1."),
            items=[
                {"size": f"{k['betrag']} · 25 Jahre", "price": k["rate"], "price_sub": "pro Monat*",
                 "features": [f"Beispiel {k['anlage']}", f"abzüglich {k['foerderung']} Bundesförderung",
                              f"mit Reststrom (rund 25 €) gesamt {k['gesamt']} im Monat",
                              "Fixe Rate, 0 € Anzahlung", "Sondertilgung jederzeit kostenlos"]},
                {"size": f"{g['betrag']} · 25 Jahre", "price": g["rate"], "price_sub": "pro Monat*",
                 "features": [f"Beispiel {g['anlage']}", f"abzüglich {g['foerderung']} Bundesförderung",
                              f"mit Reststrom (rund 25 €) gesamt {g['gesamt']} im Monat",
                              "Fixe Rate, 0 € Anzahlung", "Sondertilgung jederzeit kostenlos"]},
                {"size": "Ihr Dach", "price": "Ihre Rate", "price_sub": "im Angebot",
                 "features": ["Projektbericht mit 3D-Belegplan und Statikreport",
                              "Kauf und Finanzierung nebeneinander", "Laufzeit bis 25 Jahre wählbar",
                              "Förderung beantragen wir mit", a("kontakt", "Kostenlose Beratung anfragen →")]},
            ],
            note="*Rate abhängig von individuellem Angebot und Laufzeit. Förderhöhe und Zusage variieren.",
        ).replace('<section class="section"', '<section id="beispiele" class="section"', 1),
        C.media_text(
            eyebrow="Die wichtigste Frage zuerst",
            h2="Förderung trotz Finanzierung? Ja, und zwar in voller Höhe.",
            paragraphs=[
                ("Viele glauben, wer finanziert, verzichtet auf die Förderung. Das Gegenteil ist der Fall: "
                 "Weil Sie bei der EBZ-Finanzierung vom ersten Tag an Eigentümer sind, stellen Sie den "
                 "Förderantrag selbst und die Auszahlung geht auf Ihr Konto. Bei Mietmodellen bekommt der "
                 "Anbieter die Förderung, bei uns Sie."),
                ("In den Beispielen oben ist der Bundes-Investitionszuschuss bereits vom Finanzierungsbetrag "
                 "abgezogen: 900 € bei 8 kWp, 3.000 € bei 10 kWp mit 10-kWh-Speicher. Dazu kommen je nach "
                 "Bundesland Landesförderungen, in Kärnten etwa 3.000 € Pauschale für Neuanlagen mit Speicher."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Photovoltaik-Förderung bei Finanzierung",
            bullets=["Sie sind Eigentümer und Antragsteller, nicht die Bank",
                     "Bund und Land sind kombinierbar, wir prüfen beides für Ihr Projekt",
                     "Anträge bereiten wir vor, Fristen und Reihenfolge behalten wir im Blick"],
            cta=("foerderung_at", "Alle Förderungen 2026 ansehen"),
            dark=True,
        ),
        C.founder_story(
            eyebrow="Persönliche Beratung vom Inhaber",
            h2="Mario Zintl rechnet mit Ihnen, nicht für Sie",
            paragraphs=[
                ("Ob Kauf oder Finanzierung ist keine Frage, die ein Formular beantwortet. Deshalb nehme ich "
                 "mir für dieses Gespräch selbst Zeit: Wir schauen uns Ihren Stromverbrauch, Ihr Dach und Ihr "
                 "Budget an und legen die Zahlen für beide Wege nebeneinander."),
                ("Manchmal ist die Antwort: kaufen, weil es sich schneller rechnet. Manchmal: finanzieren, "
                 "weil die Liquidität im Haushalt oder im Betrieb wichtiger ist. Und manchmal sage ich auch, "
                 "dass eine kleinere Anlage besser passt. Verkaufen kann jeder, ehrlich beraten ist unser "
                 "Handwerk."),
            ],
            quote="Sie sollen nach dem Gespräch nicht überredet sein, sondern wissen, was Sie tun.",
            name=AUTHOR, role=AUTHOR_ROLE,
            badge="Villach, Kärnten",
            cta=("kontakt", "Beratungstermin mit Mario Zintl"),
        ),
        C.why_section(
            eyebrow="Warum finanzieren?",
            h2="Sechs Gründe, die für die EBZ-Finanzierung sprechen",
            items=[
                ("€", "Fixe Monatsrate über die gesamte Laufzeit", "Volle Planungssicherheit ohne Zinsrisiko, bis zu 25 Jahre."),
                ("⌂", "Die Anlage gehört von Anfang an Ihnen", "Kein Mietmodell, kein Eingriff ins Eigentum, volle Förderung für Private."),
                ("✓", "Kein Grundbucheintrag notwendig", "Ihr Haus bleibt vollständig unbelastet."),
                ("◇", "Kostenlose Sondertilgungen jederzeit", "Flexibel bleiben und früher zurückzahlen, wenn Sie möchten."),
                ("◔", "Digitale Entscheidung in wenigen Minuten", "Einfach, transparent und ohne Banktermin, 94 % Annahmequote."),
                ("☀", "Auch für Selbständige und Pensionisten", "Energielösungen für reale Lebenssituationen."),
            ],
        ),
        C.steps_section(
            eyebrow="So einfach geht es",
            h2="Von der Beratung zur eigenen Anlage",
            steps=[
                ("Beratung und Angebot", "Wir planen Ihre Anlage und legen Kauf und Finanzierung mit konkreten Zahlen nebeneinander.", "Tag 1"),
                ("Online-Anfrage", "Sie stellen die Finanzierungsanfrage digital bei unserem Partner Cloover, ohne Banktermin.", "wenige Minuten"),
                ("Zusage", "Die Finanzierungsentscheidung kommt in der Regel in unter zwei Minuten.", "sofort"),
                ("Montage und Förderung", "Unser Team montiert, meldet an und bereitet die Förderanträge vor. Die Anlage gehört Ihnen.", "4 bis 8 Wochen"),
            ],
        ),
        C.media_text(
            eyebrow="Kaufen oder finanzieren?",
            h2="Beides ist Eigentum, nur der Zahlungsweg unterscheidet sich",
            paragraphs=[
                ("Wer den Kaufpreis von rund 15.000 bis 22.000 € für 10 kWp mit Speicher auf einmal binden kann, "
                 "kauft direkt und ist typischerweise nach 4 bis 6 Jahren amortisiert. Wer die Liquidität lieber "
                 "im Haushalt oder im Betrieb behält, finanziert zur fixen Rate."),
                ("Mietmodelle bieten wir bewusst nicht an: Dort bleibt die Anlage beim Anbieter, die Förderung "
                 "auch, und die Rate läuft weiter, obwohl die Anlage längst abbezahlt wäre."),
            ],
            img=IMG["gen_detail"],
            alt="Montage einer Photovoltaikanlage durch Fachkräfte von EBZ Energie",
            bullets=["Gleiche Technik, gleiche Garantien: bis zu 30 Jahre Leistungsgarantie",
                     "Förderabwicklung, Netzanmeldung und Inbetriebnahme inklusive",
                     "Für Eigenheim und Gewerbe"],
            cta=("/solaranlage-mieten-oder-kaufen/", "Ratgeber: mieten, kaufen oder finanzieren?"),
            reverse=True,
        ),
        C.reviews_slider(reviews, rating, count),
        C.faq_section(FAQ),
        C.linkgrid_section("Weiterlesen", [
            ("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
            ("batteriespeicher", "Batteriespeicher"),
            ("foerderung_at", "Photovoltaik-Förderung Österreich 2026"),
            ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage"),
        ]),
        C.contact_section(
            "Kauf oder Finanzierung? Wir rechnen beides für Ihr Dach",
            "Kostenlose Beratung, Projektbericht mit 3D-Belegplan und Statikreport und die Zahlen für beide Wege nebeneinander.",
        ),
        C.finalcta(
            "Ihre Anlage. Ihre Rate. Ihr Eigentum.",
            "Sagen Sie uns, was Sie im Monat einplanen wollen. Wir sagen Ihnen ehrlich, welche Anlage dazu passt.",
            trust=[(f"{NAP['rating']} auf Google", True), ("0 € Anzahlung", False),
                   ("Zusage in Minuten", False), ("Eigentum ab Tag 1", False)],
        ),
        f'<div class="wrap"><p class="form-note" style="padding:8px 0 40px">{F["fussnote"]}</p></div>',
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=IMG["gen_eigenheim"])
    return write_page("finanzierung/index.html", html)


if __name__ == "__main__":
    import theme
    theme.write_assets()
    build()
