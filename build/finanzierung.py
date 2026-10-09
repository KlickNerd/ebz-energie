"""Leistungsseite Finanzierung (/finanzierung/).

Quelle der Zahlen: Finanzierungsbeilage "powered by Cloover" (common.FINANZIERUNG),
Faktenblatt build/seo/_fakten_2026-10.md (EAG, Kaernten), Ratgeber
/solaranlage-mieten-oder-kaufen/ (Mietmodell-Richtwerte). SEO/GEO-Briefing:
build/seo/finanzierung.{json,md}. Primaer-Keyword "pv anlage finanzieren".
Botschaft: Kaufen oder finanzieren, in beiden Faellen gehoert die Anlage ab Tag 1
dem Kunden. Kein Mietmodell. Der Begriff "Leasing" darf nicht vorkommen (Validator),
Mietmodelle heissen "Mietmodell" oder "gemietete Anlage".
Gesamtkosten der Beispiele sind Rate x 300 Monate (transparent, mit Sternchen);
ein Zinssatz wird nicht genannt, weil er im individuellen Angebot steht.
"""

from common import IMG, NAP, AUTHOR, AUTHOR_ROLE, FINANZIERUNG as F, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

PATH = "/finanzierung/"
TITLE = "PV-Anlage finanzieren: fixe Rate, Eigentum ab Tag 1 | EBZ"
DESC = ("PV-Anlage finanzieren statt mieten: 0 € Anzahlung, fixe Rate bis 25 Jahre, volle Förderung, "
        "Eigentum ab Tag 1. Beispiel 10 kWp mit Speicher ab 164 € im Monat*.")

STAND = "Stand Oktober 2026"

FAQ = [
    ("Gehört mir die Anlage bei der Finanzierung wirklich ab dem ersten Tag?",
     "Ja. Sie kaufen die Anlage von EBZ Energie und finanzieren den Kaufpreis über unseren Partner Cloover. "
     "Die Anlage ist ab der Montage Ihr Eigentum, es gibt keinen Eigentumsvorbehalt bis zur letzten Rate, "
     "keinen Grundbucheintrag und kein Mietmodell."),
    ("Wie hoch ist der Zinssatz und was kostet die Finanzierung insgesamt?",
     "Der Zinssatz ist über die gesamte Laufzeit fix und steht als effektiver Jahreszins in Ihrem Angebot, "
     "weil er von Laufzeit, Betrag und Bonität abhängt. Die Gesamtkosten sind einfach zu rechnen: Rate mal "
     "Monate. Im repräsentativen Beispiel 10 kWp mit 10-kWh-Speicher (22.000 Euro nach Abzug der "
     "Bundesförderung) sind das ab 164 Euro über 300 Monate, also rund 49.200 Euro*. Kürzere Laufzeit oder "
     "kostenlose Sondertilgungen senken diese Summe deutlich."),
    ("Kann ich eine PV-Anlage ohne Eigenkapital finanzieren?",
     "Ja. Die EBZ-Finanzierung startet mit 0 Euro Anzahlung, Eigenkapital ist nicht erforderlich. Der komplette "
     "Kaufpreis abzüglich der Bundesförderung wird zur fixen Monatsrate. Wer Eigenkapital einsetzen möchte, "
     "verkürzt die Laufzeit oder senkt die Rate."),
    ("Finanzierung über EBZ oder Kredit bei der Hausbank: was ist der Unterschied?",
     "Ein Ratenkredit, Konsumkredit, Wohnkredit ohne Grundbucheintrag oder ein Bauspardarlehen bei der Hausbank "
     "(etwa Raiffeisen, Erste Bank und Sparkasse oder BAWAG) ist eine echte Alternative, braucht aber einen "
     "Banktermin, oft Unterlagen zu Einkommen und Sicherheiten und je nach Produkt einen Grundbucheintrag. Die EBZ-Finanzierung läuft digital in Minuten, ohne "
     "Grundbuch, mit Fixzins und kostenloser Sondertilgung. Vergleichen Sie in beiden Fällen den effektiven "
     "Jahreszins und die Summe aller Raten."),
    ("Zinsloses Darlehen Photovoltaik Österreich: Gibt es eine 0 %-Finanzierung für PV-Anlagen?",
     "Ein bundesweites zinsloses Darlehen für Photovoltaik gibt es nicht. Der Bund fördert über den "
     "EAG-Investitionszuschuss (150 Euro je kWp bis 10 kWp, 150 Euro je kWh Speicher), nicht über Kredite. "
     "Angebote mit 0 Prozent Zins sind meist Aktionen einzelner Anbieter oder Banken mit kurzer Laufzeit und "
     "hoher Rate. Entscheidend sind die Gesamtkosten über die Laufzeit, nicht der beworbene Zinssatz."),
    ("Bekomme ich die Förderung, obwohl ich finanziere?",
     "Ja, in voller Höhe. Weil Sie Eigentümer und Antragsteller sind, erhalten Sie als Privatperson die "
     "Bundesförderung und die Landesförderung auf Ihr Konto. Im Beispiel wird der Bundes-Investitionszuschuss "
     "direkt vom Finanzierungsbetrag abgezogen, Landesförderungen wie die Kärntner Pauschale von 3.000 Euro "
     "kommen zusätzlich dazu."),
    ("Kann ich Speicher und Wärmepumpe mitfinanzieren?",
     "Ja. Finanziert wird das gesamte Energiesystem aus einem Angebot: Photovoltaik, Batteriespeicher, "
     "Wärmepumpe, Wallbox und Energiemanagement. Eine Rate, ein Ansprechpartner, und alle Komponenten gehören "
     "ab Tag 1 Ihnen. Das gilt für Eigenheime genauso wie für Betriebe."),
    ("Wie läuft die Bonitätsprüfung ab?",
     "Digital und in wenigen Minuten, ohne Banktermin. Die Finanzierungszusage kommt in der Regel in unter "
     "zwei Minuten, die Annahmequote liegt bei 94 Prozent. Die Vergabe erfolgt vorbehaltlich dieser Prüfung. "
     "Auch Selbständige und Pensionisten können finanzieren."),
    ("Was passiert bei einem Hausverkauf oder wenn ich früher zurückzahlen will?",
     "Sondertilgungen sind jederzeit kostenlos möglich. Sie können die Restschuld ganz oder teilweise ablösen, "
     "die fixe Rate bleibt bis dahin gleich. Beim Hausverkauf lösen Sie die Restschuld aus dem Verkaufserlös "
     "ab; die Anlage ist Ihr Eigentum und wird mit dem Haus verkauft, ohne Vertragsübernahme durch den Käufer."),
    ("Was ist der Unterschied zwischen Finanzierung und Mietmodell beim Eigentum?",
     "Beim Mietmodell bleibt die Anlage Eigentum des Anbieters, die Förderung geht an ihn, und nach 20 Jahren "
     "gehört Ihnen die Anlage weiterhin nicht. Marktüblich sind 120 bis 180 Euro Miete im Monat, über 20 Jahre "
     "28.800 bis 43.200 Euro*. Bei der EBZ-Finanzierung sind Sie ab Tag 1 Eigentümer, die Rate endet mit der "
     "Laufzeit und die Förderung fließt an Sie."),
]


def _table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    body = ""
    for r in rows:
        tds = "".join(f'<td class="hl">{c}</td>' if i == 0 else f"<td>{c}</td>" for i, c in enumerate(r))
        body += f"<tr>{tds}</tr>"
    return f'<div class="art-tablewrap eg-reveal"><table class="art-table"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def _compare_section():
    """Kauf, Finanzierung, Mietmodell in einer Tabelle (GEO-Zitierpassage als Lead)."""
    lead = ("In Österreich lässt sich eine PV-Anlage mit Speicher ab rund 147 Euro pro Monat finanzieren*. Die "
            "Anlage gehört ab dem ersten Tag dem Kunden, die volle Förderung bleibt privat erhalten, es gibt keinen "
            "Grundbucheintrag. Der Direktkauf bleibt über 20 Jahre die günstigste Variante, die Finanzierung schont "
            f"Liquidität, das Mietmodell kostet am meisten (EBZ Energie, {STAND}).")
    rows = [
        ("Eigentum", "Ab dem ersten Tag Ihres", "Ab dem ersten Tag Ihres", "Beim Anbieter, auch nach Vertragsende"),
        ("Anschaffung", "15.000 bis 22.000 € für 10 kWp mit Speicher, vor Förderung", "0 € Anzahlung", "0 € Anzahlung"),
        ("Monatliche Kosten", "Keine Rate; 200 bis 400 € pro Jahr* für Wartung und Versicherung",
         "Fixe Rate ab 147 €* inkl. Speicher, Beispiel 10 kWp + 10 kWh: ab 164 €*", "120 bis 180 € Miete*, 15 bis 25 Jahre"),
        ("Gesamtkosten über 20 Jahre", "Kaufpreis plus 4.000 bis 8.000 € Betrieb*, abzüglich Förderung",
         "Summe der Raten (Rate mal Monate), senkbar durch Sondertilgung", "28.800 bis 43.200 €*, Anlage danach nicht Ihre"),
        ("Förderung", "Bund und Land an Sie", "Bund und Land an Sie, in voller Höhe", "Geht an den Anbieter"),
        ("Wartung und Garantie", "Bis zu 30 Jahre Leistungsgarantie, Service nach Wunsch",
         "Gleiche Technik und Garantien wie beim Kauf", "Im Vertrag enthalten, dafür höhere Rate"),
        ("Vertragsende", "Anlage läuft weiter, nur für Sie", "Rate endet, Anlage läuft weiter, nur für Sie",
         "Kaufoption zum Restwert, Verlängerung oder Rückbau"),
        ("Passt für", "Wer den Kaufpreis binden kann: Amortisation typisch 4 bis 6 Jahre",
         "Wer Liquidität behalten will, Private, Selbständige, Pensionisten, Betriebe",
         "Wer weder kaufen noch finanzieren kann oder will"),
    ]
    table = _table(["Kriterium", "Kauf", "EBZ-Finanzierung", "Mietmodell / Contracting"], rows)
    return f"""
  <section class="section" style="background:#fff;border-block:1px solid var(--line)" id="vergleich">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">PV-Anlage finanzieren, kaufen oder mieten</p>
      <h2 class="center eg-reveal">Kaufen, finanzieren oder Mietmodell? Der Vergleich in einer Tabelle</h2>
      <p class="lead center eg-reveal" style="max-width:72ch;margin-inline:auto">{lead}</p>
      <p class="center eg-reveal" style="max-width:72ch;margin-inline:auto;color:var(--muted)">Wer nach „PV Anlage mieten“ oder
      „Photovoltaik mieten“ sucht, will meist nur eines: keine große Einmalzahlung. Genau das löst die
      Finanzierung, ohne dass Sie auf Eigentum und Förderung verzichten.</p>
      {table}
      <p class="form-note center eg-reveal">*Beispielkonditionen und Richtwerte: Mietraten und Laufzeiten aus marktüblichen
      Angeboten, Finanzierungsrate abhängig von Laufzeit und Anlagenkonfiguration, Kaufpreis = EBZ-Richtpreis vor Förderung.
      Die Rechnung über 20 Jahre finden Sie im Ratgeber {a("/solaranlage-mieten-oder-kaufen/", "Solaranlage mieten oder kaufen: der Vergleich")}.</p>
    </div>
  </section>"""


def build():
    rating, count, reviews = load_reviews()
    k, g = F["beispiel_klein"], F["beispiel_gross"]
    body = "".join([
        C.hero(
            eyebrow="PV Anlage finanzieren in Kärnten und der Steiermark",
            h1="PV-Anlage finanzieren oder kaufen: fixe Rate, 0 € Anzahlung, Eigentum ab dem ersten Tag",
            lead=("Keine Anzahlung, eine fixe Monatsrate und eine Anlage, die vom ersten Tag an Ihnen gehört. "
                  "Die Finanzierungszusage kommt digital in wenigen Minuten, die Förderung bleibt bei Ihnen. "
                  "Und wer den Kaufpreis binden kann, kauft direkt: Wir rechnen beide Wege nebeneinander."),
            badges=[("0 €", "Anzahlung, kein Eigenkapital nötig"), ("Fixe Rate", "bis 25 Jahre, kein Zinsrisiko"),
                    ("Volle Förderung", "trotz Finanzierung")],
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
                   "steigend. Mit PV-Anlage und Speicher decken Sie bis zu 80 % Ihres Bedarfs selbst, übrig bleibt "
                   "ein Reststrom von rund 20 bis 30 € im Monat.* Die Photovoltaik-Finanzierung macht aus der "
                   "Stromrechnung eine planbare Rate, die endet, während die Anlage weiterläuft."),
            bars=[
                ("Stromkosten ohne PV-Anlage", 100, "bad", f"rund {F['strom_heute']} im Monat*"),
                ("Reststrom mit PV-Anlage und Speicher", 16, "good", f"rund {F['strom_mit_pv']} im Monat*"),
            ],
            aside=("Was die Finanzierung ersetzt", [
                ("€", "Keine Einmalzahlung", "0 € Anzahlung, der Kaufpreis wird zur fixen Monatsrate."),
                ("✓", "Kein Zinsrisiko", "Fixzins: Die Rate bleibt über die gesamte Laufzeit gleich."),
                ("⌂", "Kein Grundbucheintrag", "Ihr Haus bleibt vollständig unbelastet."),
                ("◷", "Rate endet", "Nach der Laufzeit produziert die Anlage weiter, nur für Sie."),
            ]),
        ),
        _compare_section(),
        C.price_cards(
            eyebrow="Zwei repräsentative Beispiele",
            h2="So sieht die Monatsrate aus: Beispiel 10 kWp mit Speicher",
            intro=("Beispiele unseres Finanzierungspartners Cloover über 25 Jahre Laufzeit. Die Förderung des "
                   "Bundes wird direkt vom Finanzierungsbetrag abgezogen, die Anlage gehört Ihnen ab Tag 1. Der "
                   "Fixzins steckt in der Rate; die Gesamtkosten sind Rate mal Monate und stehen im Angebot."),
            items=[
                {"size": f"{k['betrag']} · 25 Jahre", "price": k["rate"], "price_sub": "pro Monat*",
                 "features": [f"Beispiel {k['anlage']}", f"abzüglich {k['foerderung']} Bundesförderung",
                              f"mit Reststrom (rund 25 €) gesamt {k['gesamt']} im Monat",
                              "Summe der Raten über 300 Monate: rund 30.600 €*",
                              "Fixe Rate, 0 € Anzahlung, Sondertilgung jederzeit kostenlos"]},
                {"size": f"{g['betrag']} · 25 Jahre", "price": g["rate"], "price_sub": "pro Monat*",
                 "features": [f"Beispiel {g['anlage']}", f"abzüglich {g['foerderung']} Bundesförderung",
                              f"mit Reststrom (rund 25 €) gesamt {g['gesamt']} im Monat",
                              "Summe der Raten über 300 Monate: rund 49.200 €*",
                              "Fixe Rate, 0 € Anzahlung, Sondertilgung jederzeit kostenlos"]},
                {"size": "Ihr Dach", "price": "Ihre Rate", "price_sub": "im Angebot",
                 "features": ["Projektbericht mit 3D-Belegplan und Statikreport",
                              "Kauf und Finanzierung nebeneinander, effektiver Jahreszins ausgewiesen",
                              "Laufzeit bis 25 Jahre wählbar: kürzer heißt höhere Rate, weniger Zinsen",
                              "Förderung beantragen wir mit", a("kontakt", "Kostenlose Beratung anfragen →")]},
            ],
            note=("*Beispielkonditionen: Rate abhängig von individuellem Angebot, Laufzeit und Bonität. Gesamtsumme = "
                  "Mindestrate mal 300 Monate, ohne Sondertilgungen. Förderhöhe und Zusage variieren."),
        ).replace('<section class="section"', '<section id="beispiele" class="section"', 1),
        C.media_text(
            eyebrow="Förderung trotz Finanzierung",
            h2="Förderung trotz Finanzierung: EAG-Zuschuss, Speicherbonus, Landespauschale Kärnten",
            paragraphs=[
                ("Wer in Österreich eine PV-Anlage finanziert, erhält die Förderung in voller Höhe: Der "
                 "EAG-Investitionszuschuss 2026 zahlt 150 Euro je kWp bis 10 kWp und 150 Euro je kWh Speicher, "
                 "zusammen bis zu 3.000 Euro, dazu 10 Prozent Made-in-Europe-Bonus je Komponente (Quelle: "
                 f"EAG-Abwicklungsstelle, {STAND})."),
                ("Weil Sie bei der EBZ-Finanzierung vom ersten Tag an Eigentümer sind, stellen Sie den Antrag "
                 "selbst und die Auszahlung geht auf Ihr Konto. Bei Mietmodellen bekommt der Anbieter die "
                 "Förderung. In Kärnten kommen 3.000 Euro Landespauschale für Neuanlagen ab 5 kWp mit Speicher "
                 "ab 5 kWh dazu, die Steiermark fördert über eigene Programme. Ab 2027 plant der Bund laut BMWET "
                 "eine Systemförderung für Speicher und intelligente Steuerung. "
                 "Welche Fristen gerade laufen, steht tagesaktuell auf unserer Förderseite; wir prüfen sie für Ihr Projekt "
                 "und stellen die Anträge."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Photovoltaik-Förderung bei Finanzierung",
            bullets=["EAG-Investitionszuschuss 150 €/kWp bis 10 kWp, Speicher 150 €/kWh, 10 % Made-in-Europe-Bonus",
                     "Sie sind Eigentümer und Antragsteller, nicht die Bank",
                     "Bund und Land sind kombinierbar, wir prüfen beides für Ihr Projekt",
                     "Anträge bereiten wir vor, Fristen und Reihenfolge behalten wir im Blick"],
            cta=("foerderungen", "Aktuelle Förderungen 2026"),
            dark=True,
        ),
        C.facts_panel(
            eyebrow="Photovoltaik Finanzierung: Konditionen im Klartext",
            h2="Zins, Laufzeit, Sondertilgung, Grundbuch, Bonität: die Konditionen auf einen Blick",
            intro=("Keine versteckten Bedingungen: So funktioniert die Photovoltaik-Finanzierung über unseren "
                   "Partner Cloover."),
            rows=[
                ("Anzahlung und Eigenkapital", "0 € Anzahlung, kein Eigenkapital erforderlich"),
                ("Zinssatz", "Fixzins über die gesamte Laufzeit, effektiver Jahreszins im individuellen Angebot"),
                ("Laufzeit", "bis 25 Jahre, kürzere Laufzeiten wählbar"),
                ("Gesamtkosten", "Rate mal Monate, im Angebot ausgewiesen; Beispiel 10 kWp + 10 kWh: rund 49.200 €*"),
                ("Sondertilgung", "jederzeit kostenlos, ganz oder teilweise"),
                ("Grundbuch", "kein Eintrag, das Haus bleibt unbelastet"),
                ("Bonitätsprüfung", "digital in wenigen Minuten, Zusage in der Regel unter 2 Minuten, 94 % Annahmequote"),
                ("Für wen", "Private, Selbständige, Pensionisten und Betriebe"),
                ("Was finanziert wird", "Photovoltaik, Speicher, Wärmepumpe, Wallbox und Energiemanagement aus einem Angebot"),
                ("Alternative", "Ratenkredit, Wohnkredit ohne Grundbucheintrag oder Bauspardarlehen bei der Hausbank; vergleichen Sie Effektivzins und Summe der Raten"),
            ],
            actions=[("Kostenlose Beratung anfragen", "/kontakt/", "")],
        ),
        C.cards_section(
            eyebrow="Mehr als Module",
            h2="Auch für Speicher, Wärmepumpe und Betriebe",
            intro=("Finanziert wird das ganze Energiesystem, nicht nur das Dach. Eine Rate, ein Ansprechpartner, "
                   "alles ab Tag 1 Ihr Eigentum."),
            cards=[
                {"ic": "▮", "title": "Speicher finanzieren",
                 "text": "5 bis 10 kWh heben den Eigenverbrauch von rund 30 auf 60 bis 80 Prozent. Der Speicher wird mit 150 € je kWh gefördert und läuft in derselben Rate mit.",
                 "link_key": "batteriespeicher", "link_text": "Batteriespeicher"},
                {"ic": "♨", "title": "Wärmepumpe finanzieren",
                 "text": "Heizung und Photovoltaik in einem Angebot: Die Wärmepumpe läuft mit eigenem Sonnenstrom, die Rate ersetzt Öl- oder Gasrechnung plus Stromkosten.",
                 "link_key": "waermepumpe", "link_text": "Wärmepumpe"},
                {"ic": "◎", "title": "Finanzierung für Betriebe",
                 "text": "Liquidität bleibt im Unternehmen, die Stromersparnis trägt die Rate mit. Gewerbe, Landwirtschaft und Hotellerie finanzieren zu denselben Bedingungen.",
                 "link_key": "pv_gewerbe", "link_text": "Photovoltaik für Gewerbe"},
            ],
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
                 "dass eine kleinere Anlage besser passt."),
            ],
            quote="Sie sollen nach dem Gespräch nicht überredet sein, sondern wissen, was Sie tun.",
            name=AUTHOR, role=AUTHOR_ROLE,
            badge="Villach, Kärnten",
            cta=("kontakt", "Beratungstermin mit Mario Zintl"),
        ),
        C.why_section(
            eyebrow="Warum finanzieren?",
            h2="Sechs Gründe für die EBZ-Finanzierung",
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
            h2="Ablauf: Beratung, Online-Anfrage, Zusage in Minuten, Montage",
            steps=[
                ("Beratung und Angebot", "Wir planen Ihre Anlage und legen Kauf und Finanzierung mit konkreten Zahlen nebeneinander.", "Tag 1"),
                ("Online-Anfrage", "Sie stellen die Finanzierungsanfrage digital bei unserem Partner Cloover, ohne Banktermin.", "wenige Minuten"),
                ("Zusage", "Die Finanzierungsentscheidung kommt in der Regel in unter zwei Minuten.", "sofort"),
                ("Montage und Förderung", "Unser Team montiert, meldet an und bereitet die Förderanträge vor. Die Anlage gehört Ihnen.", "4 bis 8 Wochen"),
            ],
        ),
        C.reviews_slider(reviews, rating, count),
        C.faq_section(FAQ),
        C.linkgrid_section("Weiterlesen", [
            ("/solaranlage-mieten-oder-kaufen/", "Solaranlage mieten oder kaufen: der Vergleich"),
            ("/kosten-einer-solaranlage/", "Was kostet eine Solaranlage?"),
            ("foerderung_at", "PV-Förderung Österreich 2026"),
            ("photovoltaik", "Photovoltaikanlage für Eigenheim und Gewerbe"),
            ("batteriespeicher", "Batteriespeicher mitfinanzieren"),
            ("waermepumpe", "Wärmepumpe mitfinanzieren"),
            ("pv_gewerbe", "Finanzierung für Betriebe"),
            ("solarrechner", "Solarrechner: Kosten und Ertrag"),
            ("referenzen", "Referenzen"),
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
        f'<div class="wrap"><p class="form-note" style="padding:8px 0 40px">{F["fussnote"]} Gesamtsummen sind Mindestrate mal '
        f'300 Monate ohne Sondertilgung. Mietmodell-Werte sind marktübliche Richtwerte aus unserem Ratgeber. Fördersätze '
        f'{STAND}, Änderungen durch Fördergeber vorbehalten. Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p></div>',
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=IMG["gen_eigenheim"])
    return write_page("finanzierung/index.html", html)


if __name__ == "__main__":
    import theme
    theme.write_assets()
    build()
