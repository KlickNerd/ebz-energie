"""Leistungsseite Energiegemeinschaft fuer Privathaushalte (/leistungen/energiegemeinschaft/).

Quellen: Live-LPs /leistungen/energiegemeinschaft/ und /energiegemeinschaften/ (freigegebene
Inhalte), der Pillar-Ratgeber /energiegemeinschaft/ (ElWG-Aenderungen ab 1.10.2026), die Ratgeber
/energiegemeinschaft-beitreten/ (Mehrfachteilnahme, Teilnahmefaktor) und /energiegemeinschaft-finden/
(Nahbereichsabfrage), build/seo/_fakten_2026-10.md (OeMAG Oktober 2026: 14,874 ct, Verlauf Juli 6,146 ct) und das
SEO/GEO-Briefing build/seo/eg_privat.{json,md}. Seit 20.11.2026 kommerziell ausgerichtet ("Energiegemeinschaft mit
PV-Anlage", PV-Anlage plus Anbindung); "Energiegemeinschaft beitreten" gehoert dem Ratgeber /energiegemeinschaft-beitreten/
(Kannibalisierung), der hier im Fliesstext verlinkt ist.

Rechenbeispiel mit Beispielwerten 10 ct / 14 ct / 4 EUR je Monat (alle mit Sternchen). Ehrlich
dargestellt: Bei 10 ct* EG-Preis liegt der Erzeugererloes derzeit unter dem OeMAG-Marktpreis von
14,874 ct (Oktober 2026). Das Rechenbeispiel zeigt die Einspeise-Differenz deshalb als Spanne Juli- bis
Oktober-Wert (Monatswert aufs Jahr hochgerechnet, gekennzeichnet); der sichere Vorteil kommt aus Netzentgelt
und Bezug, der EG-Preis ist planbar.

Pflicht (README): Netzentgelt-Rabatt 57 % lokal / 28 % regional NUR im Nahbereich,
oesterreichweit = Buergerenergiegemeinschaft ohne Rabatt. energyfamily nur als Text-Badge.
ElWG (Faktenliste, Abschnitt "VERBINDLICH AB 20.11.2026"): Rabatt Oktober bis Dezember 2026 nur fuer EEG-Mitglieder,
BEG/P2P/EVA im Nahbereich voraussichtlich ab 1.1.2027 (Hoehe legt die E-Control fest); netzuebergreifend bzw.
oesterreichweit voraussichtlich ab April 2027, bis dahin nur Zaehlpunkte beim selben Netzbetreiber. Abgabenbefreiung nur EEG.
"""

from common import IMG, NAP, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

PATH = "/leistungen/energiegemeinschaft/"
TITLE = "Energiegemeinschaft mit PV-Anlage | EBZ Kärnten, Steiermark"
DESC = ("Energiegemeinschaft mit EBZ: PV-Anlage planen, montieren und an eine Gemeinschaft anbinden. In der "
        "lokalen EEG bis zu 57 % weniger Netzentgelt.")

OEMAG_OKT = "14,874"   # aktueller Wert, Stand November 2026
OEMAG_SEPT = "10,168"
OEMAG_JULI = "6,146"

FAQ = [
    ("Wie trete ich einer Energiegemeinschaft bei?",
     "In vier Schritten: Eignung prüfen (Postleitzahl, Zählpunktnummer, PV-Leistung, Verbrauch), Konditionen und "
     "Vertrag, Zählpunkt im Kundenportal freigeben und Viertelstundenwerte aktivieren, Start ab dem Folgemonat. "
     "EBZ übernimmt Nahbereichsabfrage und EDA-Anmeldung. Dauer 4 bis 8 Wochen, weil die Zählpunktanmeldung nur "
     "zum Monatsersten wirksam wird."),
    ("Wie hoch ist der Strompreis in einer Energiegemeinschaft?",
     "Den Energiepreis legt jede Gemeinschaft selbst fest, üblich sind 8 bis 14 ct/kWh.* Dazu kommen für Abnehmer "
     "einer Erneuerbare-Energie-Gemeinschaft (EEG) im Nahbereich das um 57 Prozent (lokal) oder 28 Prozent (regional) reduzierte Netznutzungsentgelt "
     "und keine Elektrizitätsabgabe (ab 2027 wieder 1,5 ct je kWh, 2026 für Haushalte befristet 0,1 ct). Gegenüber einem Haushaltstarif mit rund 17 ct* "
     "Energiepreis plus vollem Netzentgelt sparen Abnehmer auf die zugeordnete Menge rund 9,5 ct je kWh (Abgaben Stand 2027).*"),
    ("Lohnt sich das Einspeisen in die Gemeinschaft noch, wenn der OeMAG-Marktpreis bei 14,874 ct liegt?",
     "Ehrliche Antwort: Bei einem EG-Preis von 10 ct* nicht über den Preis, denn der liegt unter dem "
     "OeMAG-Marktpreis von 14,874 ct (Oktober 2026). Im Juli waren es 6,146 ct, im September 10,168 ct: Der Marktpreis "
     "schwankt monatlich stark, der EG-Preis ist fix vereinbart und planbar. Dazu kommt Ihr eigener Vorteil als Abnehmer "
     "(im Nahbereich mit Netzentgelt-Rabatt), und Ihr Strom bleibt im Ort."),
    ("Kann ich mehreren Energiegemeinschaften beitreten (Mehrfachteilnahme, Teilnahmefaktor)?",
     "Ja. Seit dem ElWG darf jeder Zählpunkt an bis zu fünf Bürgerenergie-Modellen teilnehmen, ein Teilnahmefaktor "
     "(in Summe höchstens 100 Prozent) legt fest, welcher Anteil wohin geht. Für Privathaushalte reicht meist eine "
     "Gemeinschaft, sinnvoll wird es etwa bei einer lokalen EEG plus einer Bürgerenergiegemeinschaft mit Verwandten. "
     "Liegen die Zählpunkte bei verschiedenen Netzbetreibern, ist das laut Koordinationsstelle voraussichtlich erst "
     "ab April 2027 umsetzbar."),
    ("Welche Änderungen gelten für Energiegemeinschaften ab Oktober 2026?",
     "Seit 1. Oktober 2026 gilt das neue Elektrizitätswirtschaftsgesetz (ElWG) mit fünf Modellen: Gemeinschaftliche "
     "Erzeugungsanlage (GEA), Erneuerbare-Energie-Gemeinschaft (EEG), Bürgerenergiegemeinschaft (BEG), "
     "Peer-to-Peer-Vertrag (Verkauf oder Schenkung direkt an eine Person, ohne Verein) und Eigenversorgungsanlage "
     "(EVA). Den reduzierten Netzarbeitspreis bekommen von Oktober bis Dezember 2026 nur Mitglieder lokaler und "
     "regionaler EEGs; für BEG, Peer-to-Peer und EVA im Nahbereich ist er mit der neuen Netzentgelt-Verordnung "
     "voraussichtlich ab 1. Jänner 2027 vorgesehen, die Höhe legt die E-Control fest. In der Übergangsphase lassen "
     "sich neue Zuordnungen nur mit Zählpunkten beim selben Netzbetreiber umsetzen, netzübergreifend voraussichtlich "
     "ab April 2027. Für Einspeiser über 20 kW kommt ein Versorgungsinfrastrukturbeitrag von durchschnittlich "
     "0,05 ct je kWh. Bestehende Gemeinschaften werden ins neue System übergeführt."),
    ("Wie finde ich eine Energiegemeinschaft in meiner Nähe?",
     "Über die Nahbereichsabfrage beim Netzbetreiber (Kärnten Netz, Energie Klagenfurt, Energienetze Steiermark, "
     "Stromnetz Graz) mit Ihrer Zählpunktnummer, über die energiegemeinschaften.gv.at Landkarte, über Plattformen wie "
     "energyfamily oder Ihre Gemeinde. EBZ erledigt die Abfrage in einem Werktag."),
    ("Ist Strom teilen mit Nachbarn in Österreich erlaubt?",
     "Ja. PV Strom mit Nachbarn teilen ist seit 2021 über Erneuerbare-Energie-Gemeinschaften erlaubt und seit "
     "Oktober 2026 auch per Peer-to-Peer-Vertrag ohne Verein. Der Strom fließt über das öffentliche Netz, der "
     "Netzbetreiber ordnet ihn viertelstundengenau zu. Auch Verwandte in einem anderen Bundesland sollen Strom "
     "beziehen können, dann über eine Bürgerenergiegemeinschaft ohne Netzentgelt-Rabatt. In der Übergangsphase "
     "seit Oktober 2026 geht das laut Koordinationsstelle aber nur mit Zählpunkten beim selben Netzbetreiber, "
     "netzübergreifend (etwa Kärnten und Wien) voraussichtlich ab April 2027."),
    ("Woran erkenne ich eine gute Energiegemeinschaft im Vergleich?",
     "Ob Energiegemeinschaft Anbieter wie Kelag oder Energie Steiermark, Verein im Ort oder Plattform (Preise und Gebühren im "
     + a("/energiegemeinschaft-vergleich/", "Vergleich der Energiegemeinschaften") + "): Achten Sie auf "
     "einen fixen EG-Preis, der nicht an den OeMAG-Marktpreis gekoppelt ist, null Einrichtungs- und Austrittsgebühr, "
     "eine Kündigungsfrist von höchstens drei Monaten, monatliche Abrechnung mit App und eine Nahbereichsprüfung vor "
     "der Unterschrift. Ein Rabatt für österreichweites Teilen ist ein Versprechen, das niemand halten kann."),
    ("Welche Voraussetzungen brauche ich?",
     "Einen eigenen Zählpunkt (33-stellig, beginnt mit AT), einen Smart Meter mit aktivierten Viertelstundenwerten "
     "(Smart Meter Opt-in im Kundenportal, ein früheres Opt-out muss zurück) und für den Rabatt derzeit die "
     "Mitgliedschaft in einer EEG mit Anschluss im Nahbereich. Eine eigene PV-Anlage brauchen Sie nicht, Abnehmer sind willkommen."),
]


def _rechenbeispiel():
    """Statischer Ersatz fuer den eingebetteten Rechner: zwei Beispielhaushalte, lokale EEG, OeMAG-Spanne Juli bis Oktober 2026."""
    rows = [
        ("Ausgangslage",
         "7.000 kWh Überschuss, 60 % zugeordnet (4.200 kWh), dazu 1.000 kWh EG-Bezug",
         "1.000 kWh EG-Strom zugeordnet"),
        (f"Einspeisung: EG-Preis statt OeMAG-Marktpreis ({OEMAG_JULI} ct im Juli bis {OEMAG_OKT} ct im Oktober 2026)",
         "bei 10 ct*: <b>plus 162 €</b> (Juli-Wert) bis <b>minus 205 €</b> (Oktober-Wert), "
         "bei 12 ct*: <b>plus 246 €</b> bis <b>minus 121 €</b>",
         "entfällt"),
        ("Netznutzungsentgelt minus 57 % (lokal) auf 1.000 kWh Bezug",
         "<b>rund 50 €</b>",
         "<b>rund 50 €</b>"),
        ("Elektrizitätsabgabe 1,5 ct entfällt (Stand 2027)",
         "<b>rund 15 €</b>",
         "<b>rund 15 €</b>"),
        ("Energiepreis 14 ct* statt 17 ct* beim Lieferanten",
         "<b>rund 30 €</b>",
         "<b>rund 30 €</b>"),
        ("Mitgliedsbeitrag 4 € je Monat*",
         "minus 48 €",
         "minus 48 €"),
        ("Netto im Jahr",
         "<b>rund 47 €</b> sicher aus dem Bezug, dazu die Einspeise-Differenz je nach Marktpreis (siehe oben)*",
         "<b>rund 47 €</b>, bei 2.000 kWh Zuordnung rund 140 €"),
    ]
    trs = "".join(
        f"<tr><td>{p}</td><td class=\"hl\">{m}</td><td class=\"hl\">{o}</td></tr>" for p, m, o in rows
    )
    return f"""
  <section class="section" id="rechenbeispiel" style="background:#fff;border-block:1px solid var(--line)">
    <div class="wrap">
      <p class="eyebrow center eg-reveal">Energiegemeinschaft Strompreis: was Sie zahlen und bekommen</p>
      <h2 class="center eg-reveal">Rechenbeispiel: ein Jahr in einer lokalen Energiegemeinschaft</h2>
      <p class="lead center eg-reveal" style="max-width:72ch;margin-inline:auto">Vergünstigt wird nur Strom,
      der in derselben Viertelstunde erzeugt und verbraucht wird (Zuordnungsquote: etwa 25 % ohne Tagesverbrauch,
      40 bis 60 % mit Wärmepumpe, E-Auto oder Homeoffice*). Zuteilung statisch oder dynamisch nach dem Schlüssel
      der Gemeinschaft. Wo die Grenzen liegen, bewertet der Ratgeber
      {a('/energiegemeinschaft-nachteile/', 'Nachteile einer Energiegemeinschaft')}.</p>
      <div class="art-tablewrap eg-reveal" style="margin-top:32px">
        <table class="art-table">
          <thead><tr><th>Position</th><th>Haushalt mit 10-kWp-Anlage</th><th>Haushalt ohne PV-Anlage</th></tr></thead>
          <tbody>{trs}</tbody>
        </table>
      </div>
      <p class="form-note center eg-reveal" style="margin-top:18px">*Beispielkonditionen: Einspeisung 10 bzw. 12 ct,
      Bezug 14 ct, Beitrag 4 € je Monat, Lieferantenpreis 17 ct, Netznutzung 8 ct, Netzverlust 0,7 ct (Richtwerte 2026).
      Abgaben mit Stand 2027: Elektrizitätsabgabe 1,5 ct (2026 für Haushalte befristet 0,1 ct, dann rund 1 € statt 15 €),
      den Erneuerbaren-Förderbeitrag setzt die Bundesregierung 2027 für alle Stromkunden aus, er ist daher nicht eingerechnet.
      OeMAG-Marktpreis 2026: {OEMAG_JULI} ct im Juli, {OEMAG_SEPT} ct im September, {OEMAG_OKT} ct im Oktober. Die Spanne
      rechnet den Juli- und den Oktober-Wert aufs ganze Jahr hoch und zeigt nur die Bandbreite; die OeMAG vergütet
      jeden Monat zum jeweiligen Marktpreis.
      Die Konditionen von EBZ nennen wir im Erstgespräch.</p>
      <div class="center eg-reveal" style="margin-top:26px">
        {a('eg_rechner', 'Mit eigenen Zahlen rechnen: Energiegemeinschaft-Rechner', cls='btn btn--primary btn--lg')}
        {a('/energiegemeinschaft-netzkosten/', 'Rechnung Position für Position', cls='btn btn--ghost btn--lg')}
      </div>
    </div>
  </section>"""


def body():
    """Inhalt der Seite (auch fuer die Ads-Landingpage unter der alten Adresse, siehe pages/landingpages.py)."""
    rating, count, reviews = load_reviews()
    body = "".join([
        C.hero(
            eyebrow="Energiegemeinschaft für Privathaushalte · PV-Anlage und Anbindung · Kärnten, Steiermark",
            h1="Energiegemeinschaft mit eigener PV-Anlage: Solarstrom im Ort teilen und in der lokalen EEG bis zu 57 % Netzentgelt sparen",
            lead=(f"Der OeMAG-Marktpreis schwankt monatlich: {OEMAG_JULI} Cent im Juli, {OEMAG_OKT} Cent im "
                  "Oktober 2026. In einer Energiegemeinschaft verkaufen Sie Ihren Überschuss zu einem fix vereinbarten "
                  "Preis an Haushalte in der Nähe, und wer in einer lokalen Erneuerbare-Energie-Gemeinschaft bezieht, zahlt "
                  "bis zu 57 % weniger Netzentgelt. EBZ plant und montiert Ihre PV-Anlage, prüft den Nahbereich und "
                  "erledigt die Anmeldung beim Netzbetreiber."),
            badges=[("bis zu 57 %", "weniger Netzentgelt lokal"),
                    ("Fixer EG-Preis*", "statt schwankendem OeMAG-Marktpreis"),
                    ("Kein Wechsel", "Lieferant bleibt")],
            img=IMG["eg_drohne"],
            img_alt="Ortschaft mit Photovoltaik auf mehreren Dächern, typisches Netzgebiet einer lokalen Energiegemeinschaft",
            float_num=rating,
            float_label=f"aus {count} Google Bewertungen" if count else "auf Google",
            cta_primary=("kontakt", "Energiegemeinschaft anfragen"),
            cta_secondary=("#rechenbeispiel", "Was bringt mir das?"),
        ),
        C.kpis([
            ("57 %", "weniger Netzentgelt in der lokalen EEG"),
            (f"{OEMAG_OKT} ct", f"OeMAG-Marktpreis Okt. 2026 (Juli: {OEMAG_JULI} ct)"),
            ("4 bis 8 Wochen", "vom Erstgespräch bis zum Start"),
            ("rund 330", "Gemeinschaften auf der Partnerplattform energyfamily"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Was ist eine Energiegemeinschaft und wer kann teilnehmen?",
            paragraphs=[
                ("Eine Energiegemeinschaft ist ein Zusammenschluss von mindestens zwei Teilnehmern, die Solarstrom "
                 "über das öffentliche Netz teilen. In einer Erneuerbare-Energie-Gemeinschaft (EEG) sinken die "
                 "Netzentgelte im Nahbereich um 57 Prozent (lokal) oder 28 Prozent (regional). "
                 "Bürgerenergiegemeinschaften dürfen sich über ganz Österreich erstrecken, bekommen dafür aber keinen "
                 "Rabatt; netzübergreifend sind neue Zuordnungen laut Koordinationsstelle voraussichtlich ab April 2027 "
                 "möglich. Voraussetzung ist ein Smart Meter mit Viertelstundenwerten (Quellen: E-Control SNE-VO, "
                 "energiegemeinschaften.gv.at, Stand November 2026)."),
                ("Beitreten können Haushalte, Mieter mit eigenem Zählpunkt, Gemeinden, Vereine und kleine und "
                 "mittlere Unternehmen. Die Modelle: Erneuerbare-Energie-Gemeinschaft (EEG) im Nahbereich, "
                 "Bürgerenergiegemeinschaft (BEG) österreichweit, "
                 + a("/gemeinschaftliche-erzeugungsanlage/", "Gemeinschaftliche Erzeugungsanlage (GEA)") + " im "
                 "Mehrparteienhaus, seit 1. Oktober 2026 der "
                 + a("/peer-to-peer-strom/", "Peer-to-Peer-Vertrag (P2P)") + " zwischen zwei Personen und "
                 "die Eigenversorgungsanlage (EVA) für mehrere eigene Standorte. Ein Zählpunkt darf per "
                 "Mehrfachteilnahme an bis zu 5 Modellen teilnehmen, mit Teilnahmefaktor in Summe höchstens 100 %. "
                 "Wie der Beitritt abläuft, welche Unterlagen Sie brauchen und wie lange es dauert, erklärt der Ratgeber "
                 + a("/energiegemeinschaft-beitreten/", "Energiegemeinschaft beitreten: Ablauf und Dauer") + "."),
            ],
        ),
        C.split_section(
            left={
                "title": "Ich habe eine PV-Anlage: Überschuss planbar statt zum Börsenpreis verkaufen",
                "dark": True,
                "items": [
                    "EG-Preis fix vereinbart, typisch 8 bis 12 ct*, unabhängig vom monatlich schwankenden OeMAG-Marktpreis",
                    f"Ehrlich: Beim Oktober-Marktpreis von {OEMAG_OKT} ct bringen 10 ct* rund 4,9 ct je kWh weniger als die OeMAG, im Juli ({OEMAG_JULI} ct) waren es rund 4 ct je kWh mehr",
                    "OeMAG-Vertrag bleibt als Auffangnetz bestehen, nicht zugeordneter Strom geht wie bisher dorthin",
                    "Abends und im Winter sind Sie selbst günstiger Abnehmer mit Netzentgelt-Rabatt",
                    "Speicher und Energiemanagement auf die Gemeinschaft abgestimmt",
                ],
            },
            right={
                "title": "Ich habe keine PV-Anlage: Solarstrom aus der Nachbarschaft beziehen",
                "items": [
                    "EG-Preis unter dem üblichen Arbeitspreis Ihres Lieferanten, typisch 14 ct*",
                    "Bis zu 57 % weniger Netznutzungsentgelt auf den EG-Strom (lokale EEG)",
                    "Elektrizitätsabgabe entfällt in der EEG (ab 2027 wieder 1,5 ct je kWh, 2026 für Haushalte befristet 0,1 ct)",
                    "Keine Investition, kurze Kündigungsfrist, auch für Mieter mit eigenem Zählpunkt",
                    "Richtwert: plus 60 bis 220 € im Jahr, je nach Tagesverbrauch**",
                ],
                "note": "**Richtwerte aus unserem Rechner mit Beispielkonditionen, lokale EEG, Zuordnung 60 %, 1- bis 4-Personen-Haushalt (1.927 bis 4.725 kWh), Abgaben Stand 2027. Ihr Wert hängt von Verbrauchsprofil, Netzebene und Gemeinschaft ab.",
            },
        ),
        C.problem_compare(
            eyebrow="Wo der Vorteil entsteht",
            h2="Der sichere Vorteil liegt beim Bezug: Netzentgelt und Abgaben je Kilowattstunde",
            intro=("Je bezogener Kilowattstunde zahlen Sie neben dem Energiepreis rund 8 ct Netznutzungsentgelt, 0,7 ct "
                   "Netzverlustentgelt und ab 2027 wieder 1,5 ct Elektrizitätsabgabe (2026 für Haushalte befristet 0,1 ct; "
                   "Netzebene 7, Richtwerte). Den Erneuerbaren-Förderbeitrag setzt die Bundesregierung 2027 für alle "
                   "Stromkunden aus, er ist deshalb kein EEG-Vorteil mehr. In der lokalen EEG sinken die Netzentgelte um "
                   "57 Prozent (geltende SNE-VO), die Elektrizitätsabgabe entfällt."),
            bars=[
                ("Netzentgelt und Abgaben je kWh beim Lieferanten (Stand 2027)", 100, "bad", "rund 10,2 ct"),
                ("Netzentgelt und Abgaben je kWh in der lokalen EEG", 36, "good", "rund 3,7 ct"),
            ],
            aside=("Ihre Vorteile auf einen Blick", [
                ("◇", "Bis zu 57 % weniger Netzentgelt", "Netznutzungs- und Netzverlustentgelt sinken um 57 % (lokal) oder 28 % (regional)."),
                ("✓", "Elektrizitätsabgabe entfällt", "In der EEG fällt die Elektrizitätsabgabe weg: ab 2027 wieder 1,5 ct je kWh, 2026 für Haushalte befristet 0,1 ct."),
                ("€", "Planbarer Erzeugerpreis", f"EG-Preis fix statt Marktpreis, der 2026 zwischen {OEMAG_JULI} ct (Juli) und {OEMAG_OKT} ct (Oktober) schwankte."),
                ("⌂", "Kein Wechsel, kein Risiko", "Lieferant und OeMAG-Vertrag bleiben, Kündigungsfrist 1 bis 3 Monate, keine Einrichtungsgebühr."),
            ]),
        ),
        _rechenbeispiel(),
        C.media_text(
            eyebrow="Nahbereich (lokal/regional) oder österreichweit",
            h2="Nahbereich oder ganz Österreich: wo der Netzentgelt-Rabatt gilt",
            paragraphs=[
                ("Ob Ihre Gemeinschaft lokal oder regional ist, bestimmt nicht die Gemeindegrenze, sondern der "
                 "Netzanschluss auf Netzebene 7 / 6 / 4-5: Hängen Erzeuger und Abnehmer an derselben Trafostation, "
                 "gilt in der EEG der lokale Abschlag von 57 %. Teilen sie sich nur das Umspannwerk, sind es 28 %. Der "
                 "Netzbetreiber entscheidet das anhand der Zählpunktnummer, diese Nahbereichsabfrage übernehmen wir."),
                ("Sie möchten Ihren Sonnenstrom lieber der Tante in Wien zukommen lassen? Das sieht das ElWG über eine "
                 + a("/buergerenergiegemeinschaft/", "Bürgerenergiegemeinschaft") + " oder einen Peer-to-Peer-Vertrag vor. In der Übergangsphase seit Oktober 2026 "
                 "lassen sich neue Zuordnungen laut Koordinationsstelle aber vorübergehend nur mit Zählpunkten beim "
                 "selben Netzbetreiber umsetzen, netzübergreifend (etwa Kärnten und Wien) voraussichtlich ab April 2027. "
                 "Einen Netzentgelt-Rabatt gibt es dafür auch dann nicht, weil der Strom die übergeordneten Netzebenen "
                 "nutzt, und die Abgabenbefreiung gilt nur in der EEG."),
            ],
            img=IMG["gen_eigenheim"],
            alt="Einfamilienhaus mit Photovoltaikanlage, Erzeuger in einer lokalen Energiegemeinschaft",
            bullets=[
                "Lokal (selber Trafo): in der EEG minus 57 % Netzentgelt, Abgaben entfallen",
                "Regional (selbes Umspannwerk): in der EEG minus 28 % Netzentgelt, Abgaben entfallen",
                "Österreichweit (Bürgerenergiegemeinschaft): Teilen ja, netzübergreifend voraussichtlich ab April 2027, Rabatt nein",
            ],
            reverse=True,
            cta=("/energiegemeinschaft-privat/", "Ratgeber: Energiegemeinschaft privat"),
        ),
        C.cards_section(
            eyebrow="Energiegemeinschaft in der Nähe finden",
            h2="Energiegemeinschaft in Kärnten, der Steiermark oder in Ihrer Nähe finden",
            intro=("Eine Energiegemeinschaft mit Nachbarn findet man selten über Google, weil Nähe den Netzanschluss meint, "
                   "nicht die Landkarte. Drei Wege führen zur passenden Gemeinschaft in "
                   + a("/energiegemeinschaft-villach-klagenfurt/", "Villach und Klagenfurt") + ", im Lavanttal "
                   "oder in Graz. Netzbetreiber und Besonderheiten der Länder stehen in den Ratgebern "
                   + a("/energiegemeinschaft-kaernten/", "Energiegemeinschaft Kärnten") + " und "
                   + a("/energiegemeinschaft-steiermark/", "Energiegemeinschaft Steiermark") + "."),
            cards=[
                {"ic": "◎", "title": "Nahbereichsabfrage Kärnten Netz / Energie Klagenfurt",
                 "text": "Mit Ihrer Zählpunktnummer liefert der Netzbetreiber die Kennung Ihres Lokal- und Regionalbereichs, in der Steiermark die Energienetze Steiermark und Stromnetz Graz. Das sagt verbindlich, welche Gemeinschaften passen.",
                 "link_key": "/energiegemeinschaft-finden/", "link_text": "Ratgeber: Energiegemeinschaft finden"},
                {"ic": "⌖", "title": "Plattform energyfamily",
                 "text": "Rund 330 Gemeinschaften mit rund 15.000 Nutzern, darunter viele in Kärnten und der Steiermark. Die Plattform prüft anhand des Zählpunkts, ob eine davon in Ihrem Nahbereich liegt, und liefert die Abrechnung gleich mit."},
                {"ic": "⌂", "title": "energiegemeinschaften.gv.at Landkarte und Gemeinde",
                 "text": "Die Koordinationsstelle führt eine Landkarte bestehender Gemeinschaften, Gemeinden kennen ihre Vereinsgemeinschaften. Passt keine, gründen wir mit Ihnen und Ihren Nachbarn eine neue.",
                 "link_key": "/energiegemeinschaft-kaernten/", "link_text": "Energiegemeinschaft Kärnten"},
            ],
        ),
        C.facts_panel(
            eyebrow="Rechtsrahmen seit 1. Oktober 2026",
            h2="Was sich durch das ElWG ändert und was gleich bleibt",
            intro=("Mit 1. Oktober 2026 gelten die Bestimmungen des neuen Elektrizitätswirtschaftsgesetzes zur "
                   "gemeinsamen Energienutzung. Bestehende Gemeinschaften laufen weiter und werden ins neue System "
                   "übergeführt (Quelle: Koordinationsstelle, "
                   '<a href="https://energiegemeinschaften.gv.at/faqs-zum-elwg/" target="_blank" rel="noopener">FAQ zum ElWG</a>'
                   ", Stand November 2026)."),
            rows=[
                ("Fünf Modelle", "GEA im Mehrparteienhaus, EEG, Bürgerenergiegemeinschaft (BEG), Peer-to-Peer-Vertrag (P2P) und Eigenversorgungsanlage (EVA); je Zählpunkt bis zu 5 Modelle, Teilnahmefaktor in Summe höchstens 100 %"),
                ("Peer-to-Peer-Verträge", "Strom direkt an eine Person verkaufen oder verschenken, ohne Verein; Betreiber bis 30 kW werden nicht zum Lieferanten; in der Übergangsphase nur beim selben Netzbetreiber"),
                ("Netzentgelt-Rabatt 2026", "Von Oktober bis Dezember 2026 nur für Mitglieder lokaler und regionaler EEGs; für BEG, P2P und EVA im Nahbereich voraussichtlich ab 1. Jänner 2027"),
                ("Übergangsphase", "Neue Zuordnungen vorübergehend nur mit Zählpunkten beim selben Netzbetreiber, netzübergreifend und österreichweit voraussichtlich ab April 2027"),
                ("Abgaben", "Elektrizitätsabgabe und Erneuerbaren-Förderbeitrag entfallen nur in der EEG, für P2P und EVA ist das nicht geregelt. 2027 setzt die Bundesregierung den Förderbeitrag für alle aus, die Elektrizitätsabgabe steigt wieder auf 1,5 ct (2026 Haushalte 0,1 ct): Der Abgabenvorteil der EEG liegt dann bei rund 1,5 ct je kWh"),
                ("Versorgungsinfrastrukturbeitrag", "Nur für Einspeiser über 20 kW, durchschnittlich 0,05 ct je kWh; für Einfamilienhäuser nicht relevant"),
                ("Netzentgelte ab 1. Jänner 2027", "Die Abschläge legt die E-Control per Verordnung (SNE-VO) neu fest; laut E-Control-Entwurf für 2027 49 % lokal, 22 % bzw. 58 % regional (Entwurf)"),
                ("Registrierung", "Gemeinschaft als Marktpartner bei ebUtilities, Zählpunkte über das EDA-Portal mit Gemeinschafts-ID; erledigt EBZ"),
                ("Rechtsform und Kosten", "Verein oder Genossenschaft, für Peer-to-Peer keine; Mitgliedsbeitrag typisch 2 bis 8 € je Monat, keine Einrichtungsgebühr"),
                ("Ihre Voraussetzungen", "Eigener Zählpunkt, Smart Meter Opt-in für Viertelstundenwerte, für den Rabatt ein Anschluss im Nahbereich"),
            ],
            actions=[("ElWG-Änderungen im Leitartikel", "/energiegemeinschaft/#elwg", "")],
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
                ("Eine eigene Förderung für die Teilnahme gibt es nicht. Gefördert wird Ihre Photovoltaikanlage: In "
                 "Kärnten mit 3.000 € Pauschale für Neuanlagen ab 5 kWp mit 5 kWh Speicher, die Steiermark zahlt derzeit "
                 "keine PV-Landesförderung. Der Investitionszuschuss des Bundes für PV und Speicher ist für 2026 "
                 "abgeschlossen; ab 2027 plant der Bund laut BMWET eine Systemförderung für Speicher mit intelligenter "
                 "Steuerung. Für ein Energiemanagementsystem gibt es "
                 "zusätzlich die EMS-Förderung des Klimafonds, die Teilnahme an einer Energiegemeinschaft ist dort eine "
                 "zulässige Betriebsoption."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Förderung von Photovoltaik und Energiegemeinschaft",
            bullets=[
                a("foerderung_kaernten", "Kärnten: 3.000 € Landespauschale") + " für PV mit Speicher",
                a("foerderung_steiermark", "Steiermark") + ": derzeit keine PV-Landespauschale",
                a("/ems-foerderung/", "EMS-Förderung des Klimafonds") + " bis 600 € für Haushalte",
                a("finanzierung", "Finanzierung") + " ab 147 € im Monat inkl. Speicher, Eigentum ab Tag 1",
                "Welche Fristen gerade laufen, steht tagesaktuell auf unserer Förderseite; wir prüfen sie für Ihr Projekt",
            ],
            cta=("foerderungen", "Aktuelle Förderungen 2026"),
        ),
        C.why_section(
            eyebrow="Ihr Partner vor Ort",
            h2="Warum Sie mit EBZ in die Energiegemeinschaft gehen",
            items=[
                ("⌂", "Regional verankert", "Sitz in Villach, Montage und Betreuung in ganz Kärnten und der Steiermark. Ansprechpartner statt Hotline."),
                ("☀", "Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und Energiegemeinschaft vom selben Team aus zertifizierten Fachkräften."),
                ("▮", "Anlage auf die EG abgestimmt", "Auslegung, Speicher und Energiemanagement sorgen dafür, dass Ihr Überschuss dann anfällt, wenn die Gemeinschaft ihn braucht."),
                ("◎", "Netzbetreiber-Prozesse inklusive", "Nahbereichsabfrage, Zählpunktfreigabe und Anmeldung über das EDA-Portal erledigen wir mit Ihnen."),
                ("✓", "Abrechnung über energyfamily", "Monatliche Abrechnung, App, DSGVO-konform, Datenverarbeitung in Österreich."),
                ("€", "Ehrliche Zahlen", "Wir rechnen mit der ganzen Spanne des OeMAG-Marktpreises, nicht nur mit dem Tief vom Juli. Was sich nicht rechnet, empfehlen wir nicht."),
            ],
        ),
        C.founder_block(
            "Der Marktpreis sprang heuer zwischen sechs und fast fünfzehn Cent. In der Energiegemeinschaft bleibt der Strom im Ort, "
            "der Preis ist planbar, und der Mehrwert bleibt bei Ihnen und Ihren Nachbarn."
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
            h2="Mit EBZ in die Energiegemeinschaft: 4 Schritte, 4 bis 8 Wochen",
            steps=[
                ("Eignung prüfen",
                 "Sie nennen uns PLZ, Zählpunktnummer, PV-Leistung und Verbrauch. Wir fragen den Nahbereich beim Netzbetreiber ab und sagen, ob eine lokale oder regionale Gemeinschaft passt.",
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
            ("eg_rechner", "Energiegemeinschaft-Rechner"),
            ("/energiegemeinschaft-beitreten/", "Beitreten: Ablauf, Dauer, Unterlagen"),
            ("/energiegemeinschaft-finden/", "Energiegemeinschaft finden"),
            ("/energiegemeinschaft-kosten/", "Kosten und Abrechnung"),
            ("/energiegemeinschaft-netzkosten/", "Netzkosten im Detail"),
            ("/energiegemeinschaft-kaernten/", "Energiegemeinschaft Kärnten"),
            ("/energiegemeinschaft-steiermark/", "Energiegemeinschaft Steiermark"),
            ("/energiegemeinschaft-villach-klagenfurt/", "Energiegemeinschaft Villach und Klagenfurt"),
            ("/energiegemeinschaft-privat/", "Energiegemeinschaft privat: Familie und Nachbarn"),
            ("eg_gewerbe", "Für Betriebe und Gemeinden"),
            ("referenzen", "Referenzen"),
        ]),
        C.contact_section(
            "Eignung in 10 Minuten prüfen lassen",
            ("Nennen Sie uns Postleitzahl, PV-Leistung und Jahresverbrauch. Wir sagen Ihnen, welche Gemeinschaft "
             "infrage kommt, was sie bringt und welche Konditionen gelten. Kostenlos und unverbindlich."),
            page_label="Leistungsseite Energiegemeinschaft Privat",
        ),
        C.finalcta(
            "Mit eigener PV zum starken Teil der Gemeinschaft",
            ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, Montage und "
             "EG-Anbindung aus einer Hand übernimmt."),
            cta=("kontakt", "Energiegemeinschaft anfragen"),
            trust=[(f"{NAP['rating']} auf Google", True), ("Lieferant bleibt", False),
                   ("Start in 4 bis 8 Wochen", False), ("Kündigungsfrist 1 bis 3 Monate", False)],
        ),
        f"""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*EG-Preise sind Beispielwerte (Einspeisung 10 bzw. 12 ct, Bezug 14 ct, Beitrag 4 € je Monat),
      jede Gemeinschaft legt ihre Konditionen selbst fest. OeMAG-Marktpreis Oktober 2026: {OEMAG_OKT} ct je kWh
      (Stand November 2026, Quelle oem-ag.at); im September lag er bei {OEMAG_SEPT} ct, im Juli 2026 bei {OEMAG_JULI} ct,
      der Wert schwankt monatlich.
      Netzentgelt-Abschlag und Abgabenbefreiung gelten derzeit nur für Mitglieder einer Erneuerbare-Energie-Gemeinschaft,
      nur für die zugeordnete Menge und nur im Nahbereich (lokal 57 %, regional 28 %, Werte der geltenden SNE-VO der
      E-Control); die Höhe ab 2027 legt die E-Control neu fest. Abgaben: Elektrizitätsabgabe 2026 befristet 0,1 ct für Haushalte, ab 2027 wieder 1,5 ct; Erneuerbaren-Förderbeitrag 2027 laut Bundesregierung ausgesetzt (Quellen: <a href="https://www.parlament.gv.at/aktuelles/news/Nationalrat-beschliesst-Senkung-der-Elektrizitaetsabgabe" target="_blank" rel="noopener">Parlament</a>, <a href="https://www.bmf.gv.at/presse/pressemeldungen/2026/november-2026/oekostrompauschale.html" target="_blank" rel="noopener">BMF</a>). ElWG-Übergangsphase laut Koordinationsstelle
      energiegemeinschaften.gv.at (FAQ zum ElWG), Stand November 2026. Keine Garantie, keine Steuerberatung.
      Fachlich geprüft von {AUTHOR}, {AUTHOR_ROLE}.</p>
    </div>
  </section>""",
    ])
    return body


def build():
    html = page(TITLE, DESC, PATH, body(), faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=IMG["eg_drohne"])
    return write_page("leistungen/energiegemeinschaft/index.html", html)


if __name__ == "__main__":
    build()
