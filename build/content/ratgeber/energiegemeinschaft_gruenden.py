"""Ratgeber: Energiegemeinschaft gründen, Schritt für Schritt.

Migriert von ebz-photovoltaik.at/energiegemeinschaft-gruenden/ (Juli 2026) und mit
Fakten aus den Cluster-Artikeln (Kosten, Beitreten, Netzkosten, Kärnten) vertieft:
Rechtsformen und Kosten, Nahbereich, Registrierung, Preisregeln, ElWG-Ausblick.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "energiegemeinschaft-gruenden",
    "path": "/energiegemeinschaft-gruenden/",
    "title": "Energiegemeinschaft gründen: 6 Schritte, Kosten | EBZ",
    "description": ("Energiegemeinschaft gründen: ab 2 Teilnehmern, Verein ab ca. 50 €, Registrierung kostenlos. "
                    "Sechs Schritte von den Mitgliedern bis zur Abrechnung, mit Zeitplan."),
    "eyebrow": "Energiegemeinschaft · Gründung",
    "crumb_label": "Energiegemeinschaft gründen",
    "h1": "Energiegemeinschaft gründen: In sechs Schritten von der Idee zur ersten Abrechnung",
    "lead": ("Sie möchten mit Nachbarn, im Betrieb oder in der Gemeinde Strom teilen? Eine Energiegemeinschaft zu "
             "gründen ist gut machbar, wenn man Ablauf, Rechtsform und Kosten kennt. Dieser Ratgeber führt Sie "
             "durch die sechs Etappen in Österreich."),
    "chips": [
        "Ab <b>2 Teilnehmern</b> möglich",
        "Verein: <b>ca. 50 bis 150 €</b>",
        "Registrierung: <b>kostenlos</b>",
        "Dauer: <b>Wochen bis Monate</b>",
    ],
    "date_published": "2026-07-03",
    "date_modified": "2026-09-24",
    "hero_img": "gewerbe_dach",
    "hero_alt": "Großes Dach mit Photovoltaikanlage als Erzeuger einer neu gegründeten Energiegemeinschaft",

    "tldr": [
        "Eine Energiegemeinschaft braucht eine eigene Rechtsform, meist einen Verein (Gründung etwa 50 bis 150 "
        "Euro), bei größeren Projekten eine Genossenschaft oder GmbH. Mindestgröße: zwei Teilnehmer.",
        "Der Ablauf hat sechs Schritte: Mitglieder im Nahbereich finden, Rechtsform gründen, Smart Meter mit "
        "Viertelstundenwerten sicherstellen, bei ebutilities und beim Netzbetreiber registrieren, Preise und "
        "Aufteilungsschlüssel festlegen, Betrieb starten.",
        "Registrierung als Marktteilnehmer und Netzbetreibervertrag sind kostenlos. Der echte Aufwand steckt in "
        "Verwaltung und Abrechnung, die eine Plattform für 2 bis 8 Euro je Zählpunkt und Monat übernimmt.",
        "Gründen lohnt sich für Gemeinden, Betriebe und Nachbarschaften mit mehreren Erzeugern an einem Trafo. "
        "Für zwei Haushalte ist der Beitritt zu einer der über 11.000 bestehenden Gemeinschaften meist einfacher.",
        "Die technische Basis (PV, Speicher, Energiemanagement) entscheidet über den tatsächlichen Nutzen: "
        "Nur zeitgleich erzeugter und verbrauchter Strom wird zum EG-Preis abgerechnet.",
    ],
    "kpis": [
        ("2", "Teilnehmer als gesetzliche Mindestgröße"),
        ("50 bis 150 €", "Gründungskosten als Verein (Register, Statuten, Konto)"),
        ("0 €", "Registrierung bei ebutilities und Netzbetreibervertrag"),
        ("57 %", "Netzentgelt-Abschlag am selben Trafo (lokale EEG)"),
    ],

    "sections": [
        ("Gründen oder beitreten? Die Entscheidung vorab", "gruenden-oder-beitreten", f"""
<p>Eine Energiegemeinschaft zu gründen bedeutet: Sie schließen sich mit anderen Erzeugern und Verbrauchern
zusammen, geben der Gemeinschaft eine Rechtsform und melden sie beim Netzbetreiber an, damit Strom geteilt
und vergünstigt abgerechnet werden kann. Bevor Sie damit anfangen, lohnt ein Blick auf die Alternative:
In Österreich gibt es mittlerweile über 11.000 Energiegemeinschaften, davon mehr als 5.500
Erneuerbare-Energie-Gemeinschaften. In Kärnten und der Steiermark findet sich in fast jedem
Umspannwerksbereich eine aktive Gemeinschaft oder eine, die gerade entsteht.</p>
<p>Gründen lohnt sich dann, wenn Sie mehrere Erzeuger und Abnehmer kennen, die an einem Trafo hängen, oder
wenn eine Gemeinde oder ein Betrieb die Gemeinschaft als eigenes Projekt aufsetzen will. Zwei Personen
können zwar eine Gemeinschaft gründen, der Aufwand mit Verein und Netzbetreibervertrag ist aber derselbe
wie für zwanzig. Für kleine Gruppen ist der Beitritt der schnellere Weg, beschrieben im Artikel
{a('/energiegemeinschaft-beitreten/', 'Energiegemeinschaft beitreten')}.</p>
"""),
        ("Rechtsform wählen: Verein, Genossenschaft oder GmbH", "rechtsform", f"""
<p>Die Gemeinschaft braucht eine eigene Rechtsperson. Der Verein ist für kleinere Gemeinschaften die
einfachste und günstigste Variante, die Genossenschaft eignet sich für größere Gemeinschaften mit vielen
Mitgliedern und Kapitalbedarf, die GmbH für Projekte, die ein Betrieb oder eine Gemeinde als Unternehmen
führt.</p>
{A.table(
    ["Rechtsform", "Gründungskosten", "Laufender Aufwand", "Geeignet für"],
    [
        ["Verein", "ca. 50 bis 150 € (Vereinsregister, Statuten, Konto)",
         "Vorstand, Mitgliederversammlung, Buchhaltung oft ehrenamtlich; unter der Kleinunternehmergrenze ohne Umsatzsteuer",
         "Nachbarschaften, Siedlungen, kleine Gemeinden"],
        ["Genossenschaft", "mehrere hundert € plus Revisionsverband jährlich",
         "Revisionsverband, Buchhaltung, Generalversammlung", "größere Gemeinschaften, Bürgerbeteiligung"],
        ["GmbH", "Notariat, Stammkapital, Firmenbuch",
         "Buchhaltung, Jahresabschluss, Steuerberatung", "Betriebe, Gemeinden mit eigenem Projekt"],
    ],
    hl_cols=(1,),
)}
<p>Für Erneuerbare-Energie-Gemeinschaften gilt zusätzlich: Große Unternehmen ab 250 Mitarbeitern dürfen nicht
teilnehmen, landwirtschaftliche Betriebe und Gewerbebetriebe darunter schon. Die Gemeinschaft darf nicht
auf Gewinn ausgerichtet sein, der Nutzen muss bei den Mitgliedern bleiben. Den Ratgeber zu den
Rechtsformen stellt die Koordinationsstelle für Energiegemeinschaften kostenlos bereit (siehe Quellen).</p>
"""),
        ("In sechs Schritten zur eigenen Energiegemeinschaft", "sechs-schritte", f"""
{A.steps([
    ("Mitglieder im Nahbereich finden",
     "Sprechen Sie Nachbarn, Betriebe oder die Gemeinde an. Ideal ist eine Mischung aus Erzeugern mit PV und "
     "Abnehmern mit Tagesverbrauch (Wärmepumpe, Gewerbe, Homeoffice). Entscheidend ist, dass alle am selben "
     "Trafo (lokal) oder zumindest am selben Umspannwerk (regional) hängen. Der Netzbetreiber prüft das über "
     "die Zählpunktnummer."),
    ("Rechtsform gründen",
     "Statuten beschließen, Vorstand wählen, Verein beim Vereinsregister anmelden und ein Konto eröffnen. "
     "Die Statuten sollten Aufnahme, Austritt, Preisfestlegung und Aufteilungsschlüssel regeln."),
    ("Smart Meter sicherstellen",
     "Alle Beteiligten brauchen einen Smart Meter mit aktivierten Viertelstundenwerten (Opt-in im "
     "Kundenportal des Netzbetreibers, dauert wenige Tage). Wer früher ein Opt-out gewählt hat, muss das "
     "rückgängig machen."),
    ("Bei ebutilities und beim Netzbetreiber registrieren",
     "Die Gemeinschaft registriert sich kostenlos als Marktteilnehmer bei ebutilities und schließt den "
     "ebenfalls kostenlosen Vertrag mit dem Netzbetreiber (Kärnten Netz, Energienetze Steiermark, Stromnetz "
     "Graz). Danach werden die Zählpunkte über das EDA-Portal angemeldet, jedes Mitglied bestätigt die "
     "Datenfreigabe im eigenen Kundenportal."),
    ("Preise und Aufteilungsschlüssel festlegen",
     "Einspeisepreis deutlich über dem OeMAG-Marktpreis (Juli 2026: 6,146 Cent), Bezugspreis unter dem "
     "Arbeitspreis der Lieferanten, typisch 8 bis 12 Cent Einspeisung und 12 bis 16 Cent Bezug. Die "
     "Differenz deckt die Gemeinschaftskosten. Dynamische Aufteilung nach tatsächlichem Verbrauch ist für "
     "die meisten Gemeinschaften effizienter als feste Prozentsätze."),
    ("Betrieb starten und optimieren",
     "Die Zuordnung beginnt im Folgemonat nach der Anmeldung. Die Abrechnung läuft händisch oder über eine "
     "Plattform wie energyfamily, die Gutschriften und Rechnungen monatlich erstellt. Danach optimieren Sie "
     "die zeitliche Deckung, etwa mit Speicher und Energiemanagement."),
])}
{A.box("In Österreich unterstützt die Koordinationsstelle für Energiegemeinschaften mit einem Online-Guide, "
       "Musterstatuten und Beratung bei den rechtlichen und organisatorischen Schritten. Die technische "
       "Seite, also PV-Anlage, Speicher und Energiemanagement, übernimmt EBZ.", label="Tipp:")}
"""),
        ("Nahbereich: Lokal, regional oder österreichweit", "nahbereich", f"""
<p>Bei der Mitgliedersuche entscheidet nicht die Postleitzahl, sondern der Netzanschluss. Wer an derselben
Trafostation hängt, bildet den Lokalbereich, wer am selben Umspannwerk hängt, den Regionalbereich. Der
Unterschied ist bares Geld, weil der Netzentgelt-Abschlag davon abhängt.</p>
{A.table(
    ["Reichweite", "Verbindung über", "Netznutzungs- und Netzverlustentgelt (Arbeit)", "Elektrizitätsabgabe, Förderbeitrag"],
    [
        ["Lokale EEG", "selber Trafo (Niederspannung)", "minus 57 %", "entfallen"],
        ["Regionale EEG", "selbes Umspannwerk (Mittelspannung)", "minus 28 %", "entfallen"],
        ["Netzebene 4 und 5 (Betriebe)", "ausschließlich Mittelspannung", "bis zu 64 %", "entfallen"],
        ["Bürgerenergiegemeinschaft", "österreichweit", "voll, im Nahbereich ab Okt. 2026 reduziert", "bleiben"],
    ],
    hl_cols=(2,),
)}
<p>Strom teilen geht also auch österreichweit, etwa mit Verwandten in einem anderen Bundesland, dann aber
als Bürgerenergiegemeinschaft ohne Netzentgelt-Rabatt und ohne Abgabenbefreiung. Für eine Gründung mit
wirtschaftlichem Anspruch ist die lokale EEG das Ziel. Die Rechnung Position für Position steht im Artikel
{a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft und Netzkosten')}, die regionalen
Besonderheiten im Artikel {a('/energiegemeinschaft-kaernten/', 'Energiegemeinschaft Kärnten')}.</p>
"""),
        ("Was die Gründung kostet", "kosten", f"""
<p>Die Gründungskosten sind überschaubar, der laufende Aufwand ist der eigentliche Posten. Als Verein
zahlen Sie etwa 50 bis 150 Euro für Vereinsregister, Statuten und Konto. Die Registrierung bei ebutilities,
der Vertrag mit dem Netzbetreiber und das Smart-Meter-Opt-in sind kostenlos. Steuerberatung und
Buchhaltung kosten null bis einige hundert Euro im Jahr, bei Vereinen oft ehrenamtlich gelöst.</p>
<p>Die Abrechnung ist der Punkt, an dem viele Gründer unterschätzen, was auf sie zukommt: Für jede
Viertelstunde liefert der Netzbetreiber zugeordnete Mengen je Zählpunkt, die mit den vereinbarten Preisen
multipliziert, Erzeugern gutgeschrieben und Abnehmern verrechnet werden müssen. Wer das händisch macht,
zahlt mit Zeit. Wer eine Plattform nutzt, zahlt 2 bis 8 Euro je Zählpunkt und Monat oder 0,5 bis 2 Cent
je abgerechneter Kilowattstunde. Umgelegt auf die Mitglieder sind das 25 bis 100 Euro im Jahr, denen
typische Vorteile von 100 bis 300 Euro gegenüberstehen. Die vollständige Kostentabelle finden Sie im
Artikel {a('/energiegemeinschaft-kosten/', 'Energiegemeinschaft: Kosten und Abrechnung')}.</p>
{A.box_dark("Faustregel für die Kalkulation",
    "Liegt die jährliche Gebühr eines Mitglieds über 30 Prozent seines erwarteten Vorteils, ist die "
    "Gemeinschaft zu klein oder das Gebührenmodell falsch gewählt. Rechnen Sie vor der Gründung mit der "
    "voraussichtlichen Zuordnungsmenge durch: Ein Haushalt ohne Tagesverbrauch erreicht etwa 25 Prozent "
    "Zuordnungsquote, mit Wärmepumpe, E-Auto oder Homeoffice 40 bis 60 Prozent.")}
"""),
        ("Wie lange die Gründung dauert", "dauer", f"""
<p>Rechnen Sie realistisch mit einigen Wochen bis Monaten, je nach Größe und Organisation. Der zeitliche
Ablauf hängt weniger von den Behörden als von der Abstimmung unter den Mitgliedern ab: Statuten,
Preisfindung und Aufteilungsschlüssel brauchen Einigkeit. Die Vereinsregistrierung und die
Marktteilnehmer-Registrierung sind in wenigen Tagen erledigt, die Aktivierung der Viertelstundenwerte
dauert ebenfalls wenige Tage je Zählpunkt.</p>
<p>Zum Vergleich: Der Beitritt zu einer bestehenden Gemeinschaft dauert in der Regel 4 bis 8 Wochen, weil
die Zählpunktanmeldung beim Netzbetreiber nur zum Monatsersten wirksam wird. Diese Frist gilt auch für
neu gegründete Gemeinschaften: Ab dem Folgemonat nach der Anmeldung wird der Strom zugeordnet.</p>
{A.cta("Technische Basis für Ihre Gemeinschaft",
       "Wir zeigen Ihnen kostenlos, wie Sie mit PV, Speicher und Energiemanagement zum starken Erzeuger "
       "Ihrer Gemeinschaft werden, und bündeln auf Wunsch mehrere Interessenten im Nahbereich.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("eg_gewerbe", "Für Gemeinden und Betriebe"))}
"""),
        ("Die technische Basis entscheidet über den Erfolg", "technische-basis", f"""
<p>Eine Energiegemeinschaft ist nur so gut wie die Erzeugung und die zeitliche Deckung ihrer Mitglieder.
Vergünstigt wird nur Strom, der in derselben Viertelstunde erzeugt und verbraucht wird. Passt der
Verbrauch der Mitglieder zeitlich nicht zur Erzeugung, bleibt der Vorteil klein, egal wie sauber die
Gründung gelaufen ist.</p>
<p>Als Erzeuger mit einer gut geplanten {a('photovoltaik', 'Photovoltaikanlage')}, einem
{a('batteriespeicher', 'Speicher')} und einem Energiemanagementsystem steigern Sie den Anteil des sinnvoll
geteilten Stroms erheblich. Der Speicher verschiebt Überschuss in die Abendstunden, in denen Abnehmer
mehr brauchen, das Energiemanagement legt steuerbare Lasten wie Wärmepumpe oder Wallbox in die
Erzeugungszeiten. Wer ein Energiemanagementsystem einsetzt, kann seit Juni 2026 die
{a('/ems-foerderung/', 'EMS-Förderung des Klimafonds')} nutzen: Die Teilnahme an einer
Energiegemeinschaft ist dort eine der sechs zulässigen Betriebsoptionen.</p>
"""),
        ("Ausblick: Was das ElWG ab Oktober 2026 ändert", "elwg", f"""
<p>Mit 1. Oktober 2026 treten die Bestimmungen des neuen Elektrizitätswirtschaftsgesetzes zur gemeinsamen
Energienutzung in Kraft. Bestehende Gemeinschaften laufen weiter und werden ins neue System übergeführt.
Neu sind Peer-to-Peer-Verträge: Strom kann ohne Verein direkt an eine Person verkauft oder verschenkt
werden. Für Einzelfälle wie Eltern und Kinder ersetzt das die Gründung, für Nachbarschaften nicht, denn
die Befreiung von Elektrizitätsabgabe und Förderbeitrag bleibt der Erneuerbaren-Energie-Gemeinschaft
vorbehalten. Ab 1. Jänner 2027 gilt zudem eine neue Netzentgeltstruktur. Ob sich die Abschläge von 57 und
28 Prozent ändern, ist offen. Wir aktualisieren diesen Artikel, sobald die Verordnung vorliegt.</p>
"""),
        ("Fazit: Energiegemeinschaft gründen", "fazit", f"""
<p>Eine Energiegemeinschaft zu gründen ist gut machbar, wenn man den Ablauf kennt: Mitglieder im
Nahbereich, Rechtsform, Smart Meter, Registrierung, Preise und Aufteilung, Betrieb. Die Kosten sind mit
50 bis 150 Euro für den Verein und 2 bis 8 Euro je Zählpunkt und Monat für die Abrechnung überschaubar.
Über den tatsächlichen Nutzen entscheidet die technische Basis. Mit einer starken PV-Anlage, einem Speicher
und einem Energiemanagementsystem legen Sie dafür das Fundament, und dabei unterstützt Sie EBZ von der
Planung bis zur Installation.</p>
{A.cta("Starker Erzeuger werden",
       "Wir liefern die technische Basis, damit Ihre Energiegemeinschaft von Anfang an gut funktioniert, "
       "und übernehmen auf Wunsch die Anbindung an die Abrechnungsplattform.",
       primary=("kontakt", "Kostenlose Beratung sichern"), secondary=("eg_privat", "Zur Energiegemeinschaft mit EBZ"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Energiegemeinschaft: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("Wir übernehmen zwar nicht die Vereinsgründung, aber das Entscheidende für den Erfolg: eine "
                 "leistungsfähige PV-Anlage, den passenden Speicher und ein Energiemanagementsystem, das Erzeugung "
                 "und Verbrauch abstimmt. EBZ Energie aus Villach installiert alles aus einer Hand, mit einem "
                 "festangestellten Team aus zertifizierten Fachkräften in Kärnten und der Steiermark, und bindet "
                 "Ihre Gemeinschaft auf Wunsch an die Abrechnungsplattform unseres Partners energyfamily an."),
        "grid": [
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EG-Anbindung vom selben Team."),
            ("Für Gründer", "Wir bündeln Interessenten im Nahbereich und prüfen die Netzebene vorab."),
            ("Abrechnung inklusive", "Zählpunktfreigabe, Aufnahme und monatliche Abrechnung über energyfamily."),
            ("Kostenlose Erstberatung", "Wir prüfen Netzebene, Eignung und das Einsparpotenzial der Gemeinschaft."),
        ],
    },

    "faq": [
        ("Wie gründe ich eine Energiegemeinschaft?",
         "In sechs Schritten: Mitglieder im Nahbereich finden, eine Rechtsform gründen (meist Verein), bei allen "
         "Beteiligten Smart Meter mit Viertelstundenwerten sicherstellen, die Gemeinschaft bei ebutilities und "
         "beim Netzbetreiber registrieren, Preise und Aufteilungsschlüssel festlegen und den Betrieb starten. "
         "Die Zuordnung beginnt im Folgemonat nach der Anmeldung."),
        ("Welche Rechtsform braucht eine Energiegemeinschaft?",
         "Sie muss als eigene Rechtsperson organisiert sein, häufig als Verein, teils als Genossenschaft oder "
         "GmbH. Der Verein ist für kleinere Gemeinschaften mit etwa 50 bis 150 Euro Gründungskosten die "
         "einfachste Variante. Eine Genossenschaft kostet mehrere hundert Euro und verlangt einen Revisionsverband."),
        ("Wie viele Teilnehmer braucht eine Energiegemeinschaft?",
         "Die gesetzliche Mindestgröße sind zwei Teilnehmer. Wirtschaftlich sinnvoll wird eine Nachbarschafts-EEG "
         "ab etwa drei bis fünf Abnehmern je Erzeuger, weil der Gründungsaufwand für zwei derselbe ist wie für "
         "zwanzig. Für zwei Haushalte ist der Beitritt zu einer bestehenden Gemeinschaft meist einfacher."),
        ("Was kostet die Gründung?",
         "Als Verein etwa 50 bis 150 Euro für Vereinsregister, Statuten und Konto. Registrierung bei ebutilities, "
         "Netzbetreibervertrag und Smart-Meter-Opt-in sind kostenlos. Laufend kostet die Abrechnung über eine "
         "Plattform 2 bis 8 Euro je Zählpunkt und Monat, umgelegt 25 bis 100 Euro je Mitglied und Jahr."),
        ("Wie lange dauert die Gründung?",
         "Rechnen Sie mit einigen Wochen bis Monaten, je nach Abstimmung unter den Mitgliedern. Vereinsregister "
         "und Marktteilnehmer-Registrierung sind in Tagen erledigt, die Zählpunktanmeldung beim Netzbetreiber "
         "wird zum Monatsersten wirksam. Danach wird ab dem Folgemonat zugeordnet."),
        ("Müssen alle Mitglieder am selben Trafo hängen?",
         "Für den vollen Netzentgelt-Abschlag von 57 Prozent ja (lokale EEG). Am selben Umspannwerk sind es "
         "28 Prozent (regionale EEG). Österreichweites Teilen ist als Bürgerenergiegemeinschaft möglich, dann aber "
         "ohne Netzentgelt-Rabatt und ohne Abgabenbefreiung."),
        ("Welche Preise soll die Gemeinschaft festlegen?",
         "Der Einspeisepreis sollte deutlich über dem OeMAG-Marktpreis liegen (Juli 2026: 6,146 Cent), der "
         "Bezugspreis unter dem Arbeitspreis der Lieferanten. Typisch sind 8 bis 12 Cent Einspeisung und 12 bis "
         "16 Cent Bezug. Die Differenz deckt Plattform und Verwaltung."),
        ("Welche technische Basis brauche ich?",
         "Alle Beteiligten benötigen einen Smart Meter mit Viertelstundenwerten. Erzeuger bringen idealerweise "
         "eine PV-Anlage ein. Ein Energiemanagementsystem und ein Speicher erhöhen den Anteil des zeitgleich "
         "genutzten Stroms und damit den Nutzen der Gemeinschaft."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert PV-Anlagen, "
                    "Speicher und Energiemanagementsysteme in Kärnten und der Steiermark und liefert die technische "
                    "Basis für Energiegemeinschaften. Die Inhalte werden anhand der Vorgaben von E-Control und der "
                    "Koordinationsstelle für Energiegemeinschaften aktualisiert. Keine Rechts- oder Steuerberatung."),
    "sources": [
        ("Koordinationsstelle: Gründungs-Guide", "https://energiegemeinschaften.gv.at/online-guide/"),
        ("Koordinationsstelle: Ratgeber Rechtsformen (PDF)",
         "https://energiegemeinschaften.gv.at/wp-content/uploads/sites/19/2023/01/Ratgeber-Rechtsformen-Erneuerbare-Energie-Gemeinschaften.pdf"),
        ("Koordinationsstelle: Neue rechtliche Grundlagen (ElWG)",
         "https://energiegemeinschaften.gv.at/rechtliche-grundlagen-elwg/"),
        ("E-Control: Energiegemeinschaften", "https://www.e-control.at/energiegemeinschaften"),
        ("oesterreich.gv.at", "https://www.oesterreich.gv.at/"),
    ],
    "related": [
        ("eg", "Energiegemeinschaft: Der Leitartikel"),
        ("/energiegemeinschaft-beitreten/", "Energiegemeinschaft beitreten: die schnellere Alternative"),
        ("/energiegemeinschaft-kosten/", "Energiegemeinschaft: Kosten und Abrechnung"),
        ("eg_gewerbe", "Energiegemeinschaft für Gewerbe und Gemeinden"),
    ],
    "cta": {
        "h3": "Gründung geplant?",
        "text": "Wir prüfen die Netzebene Ihrer Interessenten, planen die Erzeugung und binden die Gemeinschaft an die Abrechnung an.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Die technische Basis für Ihre Gemeinschaft",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, Montage "
                   "und EG-Anbindung aus einer Hand übernimmt."),
}
