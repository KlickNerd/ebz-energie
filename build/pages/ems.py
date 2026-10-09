"""Leistungsseite Energiemanagementsystem (/energiemanagementsystem/).

Quellen: bestehende EMS-Landingpage /ems-lp-2/ (Inhalte freigegeben), der Ratgeber
/ems-foerderung/ (Klimafonds-Zahlen 2026), build/seo/_fakten_2026-10.md (Systemfoerderung
2027 laut BMWET) und das SEO/GEO-Briefing build/seo/ems.{json,md} (Stand 9.10.2026).

Roter Faden: Hook -> Definition mit Synonymen (EMS, HEMS, Energiemanager) -> Funktionsweise
-> Problem (Eigenverbrauch 30 vs. 80 %) -> sechs Hebel als Tabelle (inkl. Warmwasser/Heizstab)
-> wann es sich lohnt -> Kompatibilitaet (Fronius, Huawei, SMA, Kostal, SMARTFOX, Solar Manager,
neoom; EBZ herstellerunabhaengig) -> Kosten + Foerderung 2026 + Ausblick 2027 -> Privat vs.
Gewerbe (ISO 50001) -> Ausblick dynamische Tarife, EG, V2H -> warum EBZ -> Beweis -> Ablauf
-> FAQ -> Cluster -> Kontakt. Sichtbarer Text ohne Bewertungs-Slider unter 2.300 Woertern.
"""

from common import IMG, NAP, AUTHOR, AUTHOR_ROLE, faq_jsonld, u, a, write_page, load_reviews
from layout import page
import components as C

PATH = "/energiemanagementsystem/"
TITLE = "Energiemanagementsystem (EMS) für Photovoltaik | EBZ Energie"
DESC = ("Energiemanagementsystem (EMS, Energiemanager) für Eigenheim und Betrieb: steuert PV, Speicher, "
        "Wallbox, Wärmepumpe und Warmwasser. Förderung 2026 bis 600 €.")

FAQ = [
    ("Was ist ein Energiemanagementsystem und wofür steht EMS?",
     "EMS steht für Energiemanagementsystem, im Haushalt auch Energiemanager oder Home Energy Management System "
     "(HEMS). Es misst laufend, wie viel Strom die Photovoltaikanlage liefert und wie viel jedes Gerät braucht, "
     "und steuert Speicher, Heizstab, Wärmepumpe und Wallbox so, dass möglichst viel Sonnenstrom im Haus bleibt: "
     "Eigenverbrauch rund 30 statt 60 bis 80 Prozent.* Nachrüsten geht bei fast jeder bestehenden Anlage."),
    ("Wann braucht man ein Energiemanagementsystem?",
     "Sobald mehr als eine steuerbare Komponente im Haus ist: PV plus Speicher, Wärmepumpe, Heizstab oder E-Auto. "
     "Bei 3 bis 5 kWp ohne Speicher reicht meist das Monitoring des Wechselrichters. Mit Speicher, Wallbox oder "
     "Wärmepumpe holt ein EMS täglich Kilowattstunden heraus, die sonst zum OeMAG-Marktpreis ins Netz gehen."),
    ("Wie viel kostet ein Energiemanagementsystem fürs Einfamilienhaus?",
     "Marktübliche Systeme kosten inklusive Installation und Konfiguration rund 800 bis 1.500 €.* Der Klima- und "
     "Energiefonds übernimmt 2026 davon 50 Prozent, maximal 600 €, es bleiben oft nur wenige hundert Euro "
     "Eigenanteil. Steckt der Energiemanager schon im Wechselrichter (etwa Fronius GEN24), zahlen Sie vor allem "
     "Einbindung und Zubehör."),
    ("Welche Wechselrichter und Wärmepumpen sind kompatibel?",
     "Alle gängigen Systeme: Fronius (Solar.web, Energiekostenassistent), Huawei FusionSolar, SMA Energy und Kostal "
     "bringen eigene Energiemanager mit, SMARTFOX, Solar Manager oder neoom binden auch Fremdgeräte ein. "
     "Wärmepumpen brauchen SG Ready oder Modbus, Wallboxen Modbus oder OCPP. Die Schnittstellen Ihrer Geräte "
     "prüfen wir in der kostenlosen Analyse."),
    ("Funktioniert ein EMS auch ohne Speicher oder ohne PV-Anlage?",
     "Ohne Speicher ja: Das EMS legt dann Heizstab, Wärmepumpe und Wallbox in die Sonnenstunden. Ohne PV-Anlage "
     "lohnt es sich nur mit einem dynamischen Stromtarif, bei dem es Verbraucher in günstige Börsenstunden "
     "verschiebt. Die Klimafonds-Förderung verlangt mindestens zwei aktiv gesteuerte Komponenten."),
    ("Brauche ich einen Smart Meter für das EMS?",
     "Für die Steuerung im Haus nicht, das EMS misst mit eigenen Zählern am Hausanschluss. Für einen dynamischen "
     "Stromtarif oder eine Energiegemeinschaft braucht es den Smart Meter mit Viertelstundenwerten; in Kärnten "
     "und der Steiermark ist er in den meisten Haushalten bereits eingebaut."),
    ("Wie hoch ist die EMS-Förderung 2026 und was ändert sich 2027?",
     "Private Haushalte erhalten 50 Prozent der Kosten, maximal 600 €, Betriebe und Gemeinden bis zu 30 Prozent, "
     "maximal 20.000 € je Standort. Die Registrierung erfolgt vor der ersten Rechnung; welche Fristen gerade laufen, "
     "steht tagesaktuell auf unserer Förderseite. Ab 2027 plant der Bund laut BMWET eine Systemförderung für Speicher "
     "mit intelligenter Steuerung: Ein EMS soll dann Förderkriterium werden."),
    ("Was ist der Unterschied zwischen EMS fürs Haus und ISO 50001?",
     "Ein EMS fürs Haus schaltet Geräte in Echtzeit. ISO 50001 (Abgrenzung Industrie) ist dagegen ein "
     "Managementprozess für Unternehmen: Energiedaten erfassen, Ziele setzen, Maßnahmen dokumentieren. Die "
     "Messdaten eines technischen EMS können einfließen, ersetzen den Prozess aber nicht."),
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


def _ausblick_2027():
    """Hinweis-Box: Reihenfolge bei der Foerderung + geplante Systemfoerderung 2027 (BMWET)."""
    return (
        '<div class="art-box art-box--p eg-reveal" style="margin:32px auto 0;max-width:920px">'
        '<h3>Erst registrieren, dann Rechnung. Und ab 2027 soll das EMS zum Förderkriterium werden.</h3>'
        '<p>Haushalte registrieren sich online, <b>bevor</b> die erste Rechnung gelegt wird, Betriebe stellen den '
        'Antrag vor der verbindlichen Bestellung. Wer zuerst kauft, geht leer aus. Ab 2027 plant der Bund laut BMWET '
        'eine <b>Systemförderung</b> für Speicher und intelligente Steuerung, bei der ein Energiemanagementsystem '
        'voraussichtlich zum Förderkriterium wird; Höhe und Technikkriterien sind noch offen. Welche Fristen gerade '
        f'laufen, steht tagesaktuell auf unserer Förderseite: {a("foerderungen", "Aktuelle Förderungen 2026")}. '
        f'Alle Details: {a("/ems-foerderung/", "Ratgeber EMS-Förderung 2026")}.</p>'
        '</div>'
    )


def build():
    rating, count, reviews = load_reviews()
    body = "".join([
        # 1. Hook
        C.hero(
            eyebrow="Energiemanagementsystem für Privat und Gewerbe · Kärnten und Steiermark",
            h1="Energiemanagementsystem für Ihre Photovoltaik: bis zu 80 % Eigenverbrauch statt 30 %",
            lead=("PV, Speicher, Wärmepumpe, Heizstab und Wallbox arbeiten bei den meisten Anlagen nebeneinander "
                  "her. Ein Energiemanagementsystem (EMS, auch Energiemanager oder HEMS) verbindet alles und lenkt "
                  "jede Kilowattstunde automatisch dorthin, wo sie am meisten wert ist. Herstellerunabhängig "
                  "geplant, von den freundlichen Energie-Handwerkern aus Villach eingebaut, 2026 mit bis zu "
                  "600 € gefördert."),
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
            ("bis 80 %", "Eigenverbrauch statt rund 30 %*"),
            ("1 System", "für Strom, Wärme, Warmwasser und Mobilität"),
            ("bis 600 €", "EMS-Förderung 2026 für Haushalte"),
            ("800 bis 1.500 €*", "Kosten inkl. Installation vor Förderung"),
        ]),
        # 2. Definition (GEO) mit Synonymen
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Was ist ein Energiemanagementsystem?",
            paragraphs=[
                ("Ein Energiemanagementsystem (EMS) ist die Steuerzentrale einer Photovoltaikanlage: Es misst "
                 "Erzeugung und Verbrauch in Echtzeit und schaltet Speicher, Wärmepumpe, Heizstab und Wallbox so, "
                 "dass möglichst viel Sonnenstrom im Haus bleibt. Der Eigenverbrauch steigt damit von rund 30 auf "
                 "60 bis 80 Prozent.* Der Klima- und Energiefonds fördert ein EMS 2026 mit 50 Prozent, maximal "
                 "600 Euro (Stand Oktober 2026, Quelle: klimafonds.gv.at)."),
                ("Ob Sie es Energiemanagementsystem Photovoltaik, Energiemanager Photovoltaik, Energiemanagement "
                 "Photovoltaik oder Home Energy Management System (HEMS) nennen: Gemeint ist immer dieselbe Technik. "
                 "Sie steckt entweder im Wechselrichter (etwa bei Fronius, Huawei, SMA oder Kostal) oder sitzt als "
                 "eigenes Gerät im Zählerkasten (SMARTFOX, Solar Manager, neoom). Im Gewerbe kappt sie zusätzlich "
                 "Lastspitzen und senkt Netzentgelte und Leistungspreis."),
            ],
        ),
        # 3. Funktionsweise
        C.hub_section(
            eyebrow="Wie ein EMS arbeitet",
            h2="Messen, entscheiden, steuern: Das EMS sitzt in der Mitte",
            lead=("Das EMS kennt PV-Produktion, Speicherstand, Wärmebedarf, Ladestand des E-Autos, Wetterprognose und "
                  "Strompreis und rechnet daraus täglich einen neuen Fahrplan."),
            points=[
                ("☀", "Direkt verbrauchen statt zum OeMAG-Marktpreis einspeisen und abends teuer zurückkaufen."),
                ("♨", "Warmwasser über den Heizstab erhitzen, solange Überschuss da ist."),
                ("▮", "Den Speicher laden, wenn Überschuss da ist oder der Börsenstrom günstig ist."),
                ("⌖", "Das E-Auto per Überschussladen mit reinem PV-Strom laden, die Wärmepumpe per SG Ready."),
                ("◎", "Im Gewerbe: Lastspitzen kappen und Netzkosten senken."),
            ],
        ),
        # 4. Problem in Zahlen
        C.problem_compare(
            eyebrow="Das kostet Sie bares Geld",
            h2="Ohne EMS arbeitet jede Komponente für sich",
            intro=("Jede Kilowattstunde, die Sie mittags für 10,168 Cent (OeMAG-Marktpreis September 2026) einspeisen "
                   "und abends für 28 Cent zurückkaufen, ist ein Verlustgeschäft. Ohne Steuerung lädt der Speicher zur "
                   "falschen Zeit, die Wärmepumpe läuft nachts, das E-Auto zieht zum vollen Tarif."),
            bars=[
                ("Eigenverbrauch Ihrer PV-Anlage ohne EMS", 30, "bad", "rund 30 %*"),
                ("Eigenverbrauch mit EMS, Speicher und flexiblen Verbrauchern", 80, "good", "bis 80 %*"),
            ],
            aside=("Was sich mit EMS ändert", [
                ("☀", "Mittags nutzen", "Überschuss geht in Warmwasser, Speicher, Wärmepumpe und Auto statt ins Netz."),
                ("◔", "Zur richtigen Zeit", "Laden und heizen, wenn Strom günstig oder gratis ist."),
                ("€", "Volle Ersparnis", "Jede selbst genutzte Kilowattstunde spart den vollen Strompreis."),
                ("◎", "Alles sichtbar", "Produktion, Verbrauch und Ersparnis live in der App und im Monitoring."),
            ]),
        ),
        # 5. Sechs Hebel als Tabelle (inkl. Warmwasser/Heizstab als guenstigster Hebel)
        _table_section(
            eyebrow="Ihre Sparpotenziale",
            h2="Sechs Hebel, mit denen ein EMS bares Geld herausholt",
            intro=("Welche Hebel bei Ihnen greifen, hängt von Ihren Komponenten und Ihrem Tarif ab. Der günstigste "
                   "Einstieg ist fast immer das Warmwasser: Ein Heizstab im bestehenden Boiler macht aus Überschuss "
                   "Wärme, ohne dass Sie ein neues Gerät kaufen."),
            headers=["Hebel", "Was das EMS tut", "Für wen"],
            rows=[
                ("Eigenverbrauch maximieren",
                 "Lenkt Überschuss in Speicher und Verbraucher statt ins Netz. Eigenverbrauch von rund 30 auf 70 bis 80 %.*",
                 "jede PV-Anlage mit Speicher"),
                ("Heizstab / Boiler / Warmwasser",
                 "Regelt den Heizstab stufenlos nach Überschuss, der Boiler wird tagsüber mit Sonnenstrom warm.",
                 "jeder Haushalt mit Warmwasserspeicher"),
                ("Wallbox: Überschussladen / PV-geführtes Laden",
                 "Lädt das E-Auto bevorzugt mit PV-Überschuss, auf Wunsch mit Mindestladung bis zur Abfahrtszeit.",
                 "E-Auto-Fahrer, " + a("carport", "PV-Carport mit Wallbox")),
                ("Wärmepumpe SG Ready",
                 "Hebt die Solltemperatur bei Überschuss an, die Wärmepumpe heizt und speichert Wärme tagsüber.",
                 a("waermepumpe", "Wärmepumpe") + " mit SG-Ready-Kontakt"),
                ("Dynamischer Stromtarif / Börsenstrompreis",
                 "Lädt Speicher und Auto in günstigen Börsenstunden, meidet die teuren. Braucht Smart Meter.",
                 a("/dynamischer-stromtarif/", "Haushalte mit dynamischem Tarif")),
                ("Lastspitzen / Lastmanagement",
                 "Glättet Leistungsspitzen über den Speicher und senkt Netzentgelte und Leistungspreis.",
                 "Gewerbe, Ladeparks, Mehrparteienhäuser"),
            ],
            note="*Richtwerte für typische Anlagen mit Speicher und flexiblen Verbrauchern. Ihre Analyse zeigt die Zahlen für Ihr Haus.",
        ),
        # 6. Wann lohnt sich ein EMS
        C.cards_section(
            eyebrow="Wann sich ein EMS lohnt",
            h2="Kleine Anlage ohne Speicher: Monitoring reicht. Ab Speicher, E-Auto oder Wärmepumpe: EMS.",
            intro=("Entscheidend ist, wie viele flexible Verbraucher es gibt und wie viel Überschuss heute ungenutzt "
                   "ins Netz geht. Wir sagen ehrlich, wann ein Energiemanager Sinn hat."),
            cards=[
                {"ic": "◎", "title": "3 bis 5 kWp, kein Speicher",
                 "text": "Die Grundlast frisst den Sonnenstrom ohnehin tagsüber. Hier reicht das Monitoring des Wechselrichters, ein EMS bringt wenig. Ausnahme: ein Heizstab im Boiler, der den Überschuss aufnimmt."},
                {"ic": "▮", "title": "PV mit Speicher",
                 "text": "Das EMS lädt den Speicher prognosebasiert, hält Reserve für den Abend und lässt am Vormittag bewusst Platz. Der Autarkiegrad steigt, die Speicherzyklen sinken.",
                 "link_key": "batteriespeicher", "link_text": "Zum Batteriespeicher"},
                {"ic": "⌖", "title": "E-Auto, Wärmepumpe oder Gewerbe",
                 "text": "Hier liegt das größte Potenzial: 2.000 bis 4.000 kWh pro Jahr lassen sich mit Überschussladen und SG Ready in die Sonnenstunden verschieben.* Im Gewerbe kommt das Lastspitzenmanagement dazu.",
                 "link_key": "kontakt", "link_text": "Potenzial prüfen lassen"},
            ],
        ),
        # 7. Kompatibilitaet
        _table_section(
            eyebrow="Herstellerunabhängige Auswahl",
            h2="Kompatibel mit Fronius, Huawei, SMA und weiteren Systemen",
            intro=("Ob Energiemanagementsystem Fronius, Huawei oder SMA: Fast jeder Wechselrichter bringt einen eigenen "
                   "Energiemanager mit, der die eigenen Geräte gut steuert, Fremdgeräte oft nicht. Herstellerübergreifende "
                   "Systeme schließen die Lücke. EBZ Energie ist herstellerunabhängig und wählt, was zu Ihrer Technik passt."),
            headers=["System", "Typ", "Modbus / Schnittstellen", "Stärke"],
            rows=[
                ("Fronius Solar.web / Energiekostenassistent (GEN24)", "im Wechselrichter integriert",
                 "Modbus, eigener Heizstab- und Wallbox-Regler", "alles aus einem Haus, sehr verbreitet in Kärnten und der Steiermark"),
                ("Huawei FusionSolar", "im Wechselrichter integriert",
                 "Modbus, eigene Wallbox und Speicher", "einfache App, gute Speichersteuerung"),
                ("SMA Energy", "im Wechselrichter integriert",
                 "Modbus, SunSpec", "offene Schnittstellen, viele Wallboxen anbindbar"),
                ("Kostal", "im Wechselrichter integriert",
                 "Modbus", "solide Basis für Speicher und Wallbox"),
                ("SMARTFOX", "eigenes Gerät, herstellerübergreifend",
                 "Modbus, SG Ready, Relais", "stufenlose Heizstab-Regelung, österreichischer Hersteller"),
                ("Solar Manager", "eigenes Gerät, herstellerübergreifend",
                 "Modbus, EEBus, OCPP", "bindet Fremd-Wechselrichter, Wärmepumpen und Wallboxen ein"),
                ("neoom", "eigenes Gerät, herstellerübergreifend",
                 "Modbus, SG Ready", "Prognose (Wetter, Verbrauch, KI), Energiegemeinschaft, Gewerbe"),
            ],
            note=("Auswahl marktüblicher Systeme ohne Anspruch auf Vollständigkeit, Stand Oktober 2026. "
                  "Welche Schnittstelle Ihre Wärmepumpe oder Wallbox bietet, prüfen wir in der Analyse."),
        ),
        # 8. Kosten + Foerderung 2026 + Ausblick 2027
        C.price_cards(
            eyebrow="Kosten und EMS-Förderung 2026",
            h2="Was ein EMS kostet und was der Klimafonds dazuzahlt",
            intro=("Marktübliche Systeme kosten im Einfamilienhaus 800 bis 1.500 €* inklusive Installation. Der "
                   "Klima- und Energiefonds fördert 2026 Systeme, die mindestens zwei Komponenten aktiv steuern. "
                   "Budget 4,9 Millionen Euro, Registrierung vor der ersten Rechnung (Stand Oktober 2026)."),
            items=[
                {"size": "Private Haushalte", "price": "50 %", "price_sub": "der Kosten, maximal 600 €",
                 "features": ["Steuerung, Messtechnik, Installation und Konfiguration förderfähig",
                              "Plus 100 € Bonus bei Teilnahme an der Begleitforschung",
                              "Online-Registrierung vor der ersten Rechnung",
                              "Eigenanteil nach Förderung oft nur wenige hundert Euro*"]},
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
            note=("Fünf Jahre Betrieb mit einer von sechs Optionen, etwa dynamischer Stromtarif oder Energiegemeinschaft. "
                  "Amortisation: 2.000 kWh verschobener Verbrauch sparen bei 28 ct rund 350 € im Jahr*, der Eigenanteil "
                  "ist nach ein bis drei Jahren zurück."),
        ).replace('<section class="section"', '<section id="foerderung" class="section"', 1)
         .replace('<p class="form-note center eg-reveal" style="margin-top:22px">',
                  _ausblick_2027() + '<p class="form-note center eg-reveal" style="margin-top:22px">', 1),
        # 9. Privat / Gewerbe (inkl. Abgrenzung ISO 50001)
        C.audience_split(
            eyebrow="Für Ihr Zuhause und Ihren Betrieb",
            h2="Privat oder Gewerbe: EMS fürs Eigenheim und Energiemanagement im Betrieb",
            intro=("Ein Energiemanagementsystem Privathaushalt steuert Geräte, ISO 50001 ist ein Managementprozess für "
                   "Unternehmen. Wir liefern die Steuerung im Haus und die Messdaten für Audit und Reporting im Betrieb."),
            left={
                "img": IMG["gen_eigenheim"],
                "alt": "Einfamilienhaus mit Photovoltaik, Speicher und Wallbox in Kärnten",
                "title": "Privat: mehr Unabhängigkeit und Komfort",
                "bullets": [
                    "Sonnenstrom rund um die Uhr optimal genutzt, Autarkiegrad steigt",
                    "E-Auto günstig per Überschussladen, Warmwasser über den Heizstab",
                    "Wärmepumpe über SG Ready automatisch in die Sonnenstunden gelegt",
                    "Dynamische Tarife ohne Aufwand ausnutzen",
                    "Alles per App und Monitoring, kein Fachwissen nötig",
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
                    "Energiedaten für ESG-Reporting, Energieaudit und ISO 50001",
                    "Skalierbar über mehrere Standorte und Verbraucher",
                    "Bis zu 20.000 € Förderung je Standort (2026)",
                ],
                "cta": ("kontakt", "Für meinen Betrieb anfragen"),
            },
        ),
        # 10. Ausblick: dynamische Tarife, Energiegemeinschaft, V2H
        C.media_text(
            eyebrow="Was als Nächstes kommt",
            h2="Dynamische Tarife, Energiegemeinschaft, V2H: Ein EMS ist dafür gebaut",
            paragraphs=[
                ("Der Smart Meter liefert Viertelstundenwerte, damit wird ein dynamischer Stromtarif nach "
                 "Börsenstrompreis möglich. Das EMS lädt Speicher und E-Auto in günstigen Stunden und meidet die "
                 "teuren, ab 2027 kommen regelbare Netztarife dazu. Beides zählt als Option für die fünfjährige "
                 "Betriebsverpflichtung der Klimafonds-Förderung."),
                ("Was auch ein EMS nicht im Haus unterbringt, muss nicht für wenige Cent ins Netz: In einer "
                 "Energiegemeinschaft teilen Sie den Überschuss mit Nachbarn, im Nahbereich mit bis zu 57 % weniger "
                 "Netzentgelt für die Bezieher. Und mit Vehicle-to-Home (V2H) / bidirektionalem Laden wird das "
                 "E-Auto selbst zum Speicher. Ein gut gewähltes EMS steuert das alles aus einer Oberfläche."),
            ],
            img=IMG["gen_detail"],
            alt="Fachkraft von EBZ Energie bei der Einbindung von Steuerungstechnik an einer Photovoltaikanlage",
            bullets=[
                a("/smart-meter/", "Smart Meter") + ": Voraussetzung für stundengenaue Abrechnung",
                a("/dynamischer-stromtarif/", "Dynamischer Tarif") + ": Börsenpreis statt Fixpreis, automatisch genutzt",
                a("eg_privat", "Energiegemeinschaft") + ": Überschuss teilen, Rabatt nur im Nahbereich",
            ],
            cta=("eg_privat", "Zur Energiegemeinschaft"),
            reverse=True,
            dark=True,
        ),
        # 11. Warum EBZ
        C.why_section(
            eyebrow="Ihr Handwerkspartner",
            h2="Ein EMS ist nur so gut wie die Hand, die es installiert und einstellt",
            items=[
                ("◇", "Herstellerunabhängig", "Wir empfehlen das System, das zu Ihnen passt, nicht umgekehrt. Neutral beraten, sauber umgesetzt."),
                ("☀", "Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EMS von einem Partner. Kein Schnittstellen-Chaos."),
                ("✓", "Zertifizierte Fachkräfte", "Zertifizierte Elektro-Fachkräfte, volle Verantwortung bei uns, Montage in Kärnten und der Steiermark."),
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
        # 12. Ablauf
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
            ("/ems-foerderung/", "EMS-Förderung 2026 im Detail"),
            ("foerderungen", "Alle Förderungen 2026"),
            ("/smart-meter/", "Smart Meter erklärt"),
            ("/dynamischer-stromtarif/", "Dynamischer Stromtarif"),
            ("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"),
            ("batteriespeicher", "Stromspeicher"),
            ("/pv-speicher-nachruesten/", "Speicher nachrüsten"),
            ("carport", "Photovoltaik-Carport mit Wallbox"),
            ("eg_privat", "Energiegemeinschaft"),
            ("referenzen", "Referenzen"),
        ]),
        C.contact_section(
            headline="Machen Sie mehr aus dem Strom, den Sie ohnehin produzieren",
            sub=("Ob Sie schon eine PV-Anlage haben oder gerade planen: Wir zeigen Ihnen in einem kostenlosen "
                 "Gespräch, wie viel ein Energiemanagementsystem in Ihrem Fall herausholt. Ohne Verkaufsdruck, "
                 "dafür mit ehrlicher Rechnung."),
            page_label="Leistungsseite Energiemanagementsystem",
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
      inklusive Installation, Ersparnis-Beispiel mit 2.000 kWh verschobenem Verbrauch und 28 ct je kWh.
      OeMAG-Marktpreis September 2026: 10,168 ct je kWh (Juli 2026: 6,146 ct; der Wert schwankt monatlich).
      Förderangaben laut Leitfaden des Klima- und Energiefonds (Juni 2026), Ausblick 2027 laut BMWET,
      maßgeblich sind die offiziellen Förderbedingungen. Fachlich geprüft von {AUTHOR},
      {AUTHOR_ROLE}.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import theme
    theme.write_assets()
    build()
