"""Ads-Landingpage Energiemanagementsystem (alte WP-Seite /ems-lp-2/, Stand Juli 2026).

Botschaft der alten LP uebernommen (EMS als "Gehirn Ihrer Energie", Eigenverbrauch rund 30 % -> bis 80 %,
sechs Sparhebel, Privat und Gewerbe, herstellerunabhaengig, auch zum Nachruesten, 4 Schritte, Mario-Zitat).
Korrigiert/weggelassen: "bis 30 % mehr Ertrag aus bestehender PV" (nicht belegt) gestrichen; "eigene
zertifizierte Elektro-Fachkraefte, keine Subunternehmer" -> zertifizierte Fachkraefte; Bewertung 5,0 -> 4,9
(kommt aus den Reviews); "abends fuer 25 Cent zurueckkaufen" -> OeMAG-Marktpreis September 2026 und 28 Cent wie
auf der Leistungsseite; Foerderung ohne Betraege; Widmanngasse -> Triglavstrasse 15 (kommt aus NAP).
Leere H1 der alten Seite durch das Hauptversprechen ersetzt. Zahlen aus build/pages/ems.py.
"""

LP = {
    "path": "/ems-lp-2/",
    "title": "Energiemanagementsystem (EMS) für Ihre PV | EBZ Energie",
    "description": ("Energiemanagementsystem für Photovoltaik: steuert Speicher, Wärmepumpe und Wallbox, bis zu 80 % "
                    "Eigenverbrauch. Herstellerunabhängig, auch zum Nachrüsten."),
    "eyebrow": "Energiemanagementsystem für Zuhause und Betrieb",
    "h1": "Das Gehirn Ihrer Energie: Ein Energiemanagementsystem verbindet, was bisher nur nebeneinander lief",
    "lead": ("Ein EMS misst in Echtzeit, wie viel Strom Ihre PV-Anlage produziert und was jedes Gerät gerade braucht, "
             "und lenkt jede Kilowattstunde automatisch dorthin, wo sie am meisten wert ist. Ihr Eigenverbrauch steigt "
             "von rund 30 % auf bis zu 80 %.* Herstellerunabhängig geplant, auch für bestehende Anlagen."),
    "badges": [("bis 80 %", "Eigenverbrauch möglich*"), ("Hersteller", "unabhängig"), ("Auch zum", "Nachrüsten")],
    "hero_img": "ems",
    "hero_alt": "Energiemanagement-Display an der Wand neben Wechselrichter und Batteriespeicher im Technikraum",
    "cta": "Kostenlose EMS-Beratung anfragen",
    "problem": {
        "eyebrow": "Das kostet Sie bares Geld",
        "h2": "Ohne Steuerung verschenken Sie jeden Tag Strom und damit Ersparnis",
        "paragraphs": [
            ("Jede Kilowattstunde, die Sie mittags zum OeMAG-Marktpreis (September 2026: 10,168 Cent) einspeisen und "
             "abends für rund 28 Cent zurückkaufen, ist ein Verlustgeschäft. Genau das passiert bei den meisten Anlagen "
             "jeden Tag."),
            ("Der Speicher lädt zur falschen Zeit, die Wärmepumpe läuft nachts mit Netzstrom, und das E-Auto lädt zum "
             "vollen Tarif. Ohne EMS arbeitet jede Komponente für sich. Mit EMS arbeiten alle zusammen: Der "
             "Eigenverbrauch steigt von rund 30 % auf 60 bis 80 %.*"),
        ],
    },
    "benefits": {
        "eyebrow": "Ihre Sparpotenziale",
        "h2": "Sechs Hebel, mit denen ein EMS bares Geld herausholt",
        "intro": "Welche Hebel bei Ihnen greifen, hängt von Ihren Komponenten und Ihrem Tarif ab. Wir prüfen das kostenlos.",
        "cards": [
            ("☀", "Eigenverbrauch maximieren",
             "Statt einzuspeisen und teuer zurückzukaufen, nutzen Sie Ihren Sonnenstrom selbst: Der Eigenverbrauch steigt von rund 30 % auf 60 bis 80 %.*"),
            ("◎", "Dynamische Tarife nutzen",
             "Mit Smart Meter und variablem Stromtarif lädt und verbraucht Ihr System automatisch dann, wenn der Börsenstrom am günstigsten ist."),
            ("⌖", "Überschussladen fürs E-Auto",
             "Die Wallbox lädt bevorzugt mit PV-Überschuss. So fahren Sie mit selbst produziertem Strom."),
            ("♨", "Wärmepumpe PV-optimiert",
             "Das EMS erzeugt Wärme und Warmwasser bevorzugt bei Sonnenschein (SG Ready) und senkt so Ihre Heizkosten."),
            ("▮", "Lastspitzen kappen",
             "Im Gewerbe glättet das EMS teure Leistungsspitzen über den Speicher und senkt Netzentgelte und Leistungspreis."),
            ("◉", "Volle Transparenz",
             "Sie sehen live, was produziert, verbraucht und gespart wird, finden Stromfresser und behalten alles per App im Blick."),
        ],
    },
    "quote": ("Eine PV-Anlage ist ein guter Anfang. Erst mit einem durchdachten Energiemanagement holen Sie das Maximum "
              "heraus. Wir sorgen dafür, dass jede Kilowattstunde für Sie arbeitet."),
    "steps": {
        "eyebrow": "So einfach geht es",
        "h2": "In 4 Schritten zu einem System, das für Sie mitdenkt",
        "steps": [
            ("Analyse Ihrer Anlage", "Wir erfassen Komponenten, Verbraucher, Tarif und Ihre Ziele und zeigen ehrlich, welches Sparpotenzial in Ihrer Anlage steckt.", "kostenlos"),
            ("Herstellerunabhängige Auswahl", "Wir wählen das EMS, das zu Ihrer Technik passt, nicht das, was ein einzelner Hersteller vorgibt. Mit transparentem Angebot.", "Ihr Tempo"),
            ("Installation und Einbindung", "Zertifizierte Elektro-Fachkräfte binden alle Komponenten sauber ein und konfigurieren das System auf Ihren Bedarf.", "nach Termin"),
            ("Optimierung und Service", "Nach dem Feintuning behalten Sie alles per App im Blick und haben einen festen Ansprechpartner für die kommenden Jahre.", "laufend"),
        ],
    },
    "why": {
        "eyebrow": "Ihr Handwerkspartner",
        "h2": "Warum EBZ der richtige Partner für Ihr EMS ist",
        "items": [
            ("◇", "Herstellerunabhängig", "Wir empfehlen das System, das zu Ihnen passt, nicht umgekehrt. Neutral beraten, sauber umgesetzt."),
            ("☀", "Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EMS von einem Partner. Kein Schnittstellen-Chaos."),
            ("✓", "Zertifizierte Fachkräfte", "Meisterhaftes Handwerk und sorgfältige Ausführung nach österreichischen Normen."),
            ("▮", "Auch zum Nachrüsten", "Ihr EMS funktioniert auch mit Ihrer bestehenden PV-Anlage. Sie müssen nichts neu kaufen."),
            ("€", "Förderung geprüft", "Wir prüfen den aktuellen Förderstand für Ihr Projekt und übernehmen die Anträge."),
            ("◉", "Service über Jahre", "Monitoring und ein fester Ansprechpartner, auch nach der Inbetriebnahme."),
        ],
    },
    "contact": {
        "h2": "Kostenlose EMS-Beratung anfragen",
        "sub": ("Ob Sie schon eine PV-Anlage haben oder gerade planen: Wir zeigen Ihnen in einem kostenlosen Gespräch, "
                "wie viel ein Energiemanagementsystem in Ihrem Fall herausholt. Wir melden uns innerhalb eines Werktags."),
    },
    "faq": [
        ("Was genau macht ein Energiemanagementsystem?",
         "Ein EMS ist die Steuerzentrale Ihres Energiesystems. Es misst laufend Erzeugung und Verbrauch und lenkt den "
         "Strom automatisch dorthin, wo er am meisten wert ist: in den Eigenverbrauch, in den Speicher, in die "
         "Wärmepumpe oder ins E-Auto. So kaufen Sie deutlich weniger Netzstrom zu."),
        ("Lohnt sich ein EMS für Privathaushalte und Betriebe?",
         "Im Haushalt vor allem mit Speicher, Wärmepumpe, Heizstab oder E-Auto, weil sich diese Verbraucher an die "
         "Sonnenstunden anpassen lassen. Im Betrieb kommt das Kappen von Lastspitzen dazu, das Netzentgelte und "
         "Leistungspreis senkt."),
        ("Funktioniert ein EMS auch mit meiner bestehenden Anlage?",
         "In den allermeisten Fällen ja. Ein EMS lässt sich nachrüsten und bindet Ihre vorhandenen Komponenten ein. "
         "Welche Systeme mit Ihrer Technik kompatibel sind, prüfen wir in der kostenlosen Analyse."),
        ("Wie viel kann ich mit einem EMS sparen?",
         "Das hängt von Anlage, Verbrauch und Tarif ab. Typisch steigt der Eigenverbrauch von rund 30 % auf 60 bis "
         "80 %,* und jede zusätzlich selbst genutzte Kilowattstunde spart den vollen Strompreis. Mit Smart Meter und "
         "dynamischem Tarif kommt ein weiterer Hebel dazu. Ihre Zahl rechnen wir individuell."),
        ("Was kostet ein Energiemanagementsystem?",
         "Marktübliche Systeme für das Einfamilienhaus kosten inklusive Installation und Konfiguration rund 800 bis "
         "1.500 € vor Förderung.* Steckt der Energiemanager schon im Wechselrichter, fallen vor allem Einbindung und "
         "Zubehör an."),
        ("Welche Systeme verbaut EBZ?",
         "Wir arbeiten herstellerunabhängig. Fronius, Huawei, SMA und Kostal bringen eigene Energiemanager mit, "
         "SMARTFOX, Solar Manager oder neoom binden auch Fremdgeräte ein. Welche Lösung zu Ihrer Technik passt, klären "
         "wir in der Beratung."),
        ("Ist ein EMS förderfähig?",
         "Häufig ja, die Programme und Bedingungen ändern sich derzeit aber laufend. Wir prüfen den aktuellen "
         "Förderstand für Ihr Projekt und übernehmen die Anträge."),
    ],
    "finalcta": {
        "h2": "Jede Kilowattstunde zählt. Lassen Sie sie für sich arbeiten.",
        "text": "Ob privat oder Gewerbe: Wir zeigen Ihnen kostenlos und ehrlich, wie viel ein EMS in Ihrem Fall herausholt.",
    },
    "footnote": ("*Richtwerte, abhängig von Anlage, Verbrauch, Speicher und Tarif, Stand Oktober 2026. Ihre "
                 "individuelle Rechnung erstellen wir kostenlos. Verbindlich ist Ihr persönliches Angebot."),
}
