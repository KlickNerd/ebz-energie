"""Ratgeber: Wärmepumpenförderung Österreich 2026 (Überblick über alle Fördertöpfe).

Migriert vom WordPress-Artikel ebz-photovoltaik.at/waermepumpenfoerderung-in-oesterreich/
(veröffentlicht 2026-03-05, zuletzt geändert 2026-04-12). Zahlen: Stand April 2026.
Bereinigt: Gedankenstriche, unbelegte Summe "15.825 €" durch die nachvollziehbaren
Beispiele aus dem Landesförderungs-Artikel ersetzt, Marketing-Floskeln gekürzt.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "waermepumpenfoerderung-in-oesterreich",
    "path": "/waermepumpenfoerderung-in-oesterreich/",
    "title": "Wärmepumpenförderung Österreich 2026: bis 12.500 € | EBZ",
    "description": ("Wärmepumpenförderung 2026 in Österreich: bis 7.500 € vom Bund, 5.000 € Bohrbonus, "
                    "Landeszuschüsse bis 8.000 €, Sauber Heizen bis 100 %. Alle Töpfe und Fristen."),
    "eyebrow": "Förderung · Wärmepumpe",
    "crumb_label": "Wärmepumpenförderung 2026",
    "h1": "Wärmepumpenförderung in Österreich 2026: Alle Fördertöpfe im Überblick, bis zu 12.500 € vom Bund",
    "lead": ("Bund, Länder, Gemeinden und das Finanzamt beteiligen sich 2026 am Heizungstausch: bis zu "
             "7.500 € Bundesförderung, 5.000 € Bohrbonus für Erdwärme, Landeszuschüsse bis 8.000 € und "
             "für einkommensschwache Haushalte bis zu 100 % der Kosten. Dieser Überblick zeigt, welcher "
             "Topf für wen gilt und welche Fristen laufen."),
    "chips": [
        "Bund: <b>bis 7.500 €</b> (Erdwärme 12.500 €)",
        "Land: <b>bis 8.000 €</b> (Wien)",
        "Sauber Heizen: <b>bis 100 %</b>",
        "Registrierung bis <b>31.12.2026</b>",
    ],
    "date_published": "2026-03-05",
    "date_modified": "2026-09-24",
    "hero_img": "foerderung",
    "hero_alt": "Beratungsgespräch zur Wärmepumpenförderung mit Unterlagen und Taschenrechner",

    "tldr": [
        "Die Sanierungsoffensive 2026 des Bundes zahlt für den Tausch einer Öl-, Gas-, Kohle- oder "
        "Elektroheizung gegen eine Wärmepumpe bis zu 7.500 €, bei Erdwärme mit Bohrbonus bis zu 12.500 €. "
        "Deckel: 30 % der förderfähigen Kosten.",
        "Alle neun Bundesländer legen eigene Zuschüsse dazu, zum Beispiel Wien 35 % bis 8.000 €, Salzburg "
        "rund 5.000 €, Oberösterreich 100 € je kW bis 1.700 €. Bund und Land sind in der Regel kombinierbar.",
        "„Sauber Heizen für Alle“ übernimmt für Haushalte im unteren Einkommensdrittel bis zu 100 % der "
        "Kosten (Obergrenze 25.586 € Luft-Wasser, 37.550 € Sole-Wasser).",
        "Die Öko-Sonderausgabenpauschale bringt zusätzlich fünf Jahre lang 400 € Sonderausgaben, wenn nach "
        "Förderabzug mehr als 2.000 € Restkosten bleiben.",
        "Betriebe, Vereine und Gemeinden erhalten bis zu 7.500 € (unter 50 kW) oder 12.000 € (50 bis 100 kW), "
        "maximal 50 % der Kosten. Registrierung für Private bis 31. Dezember 2026, solange Budget vorhanden.",
    ],
    "kpis": [
        ("7.500 €", "Bundesförderung Wärmepumpe"),
        ("12.500 €", "mit Bohrbonus für Erdwärme"),
        ("100 %", "Sauber Heizen für Alle (max.)"),
        ("2.000 €", "Öko-Sonderausgabenpauschale"),
    ],

    "sections": [
        ("Wer 2026 wie viel bekommt: die vier Fördertöpfe", "ueberblick", f"""
<p>Der Umstieg von Öl, Gas, Kohle oder Strom auf eine {a('waermepumpe', 'Wärmepumpe')} wird 2026 aus
vier Richtungen unterstützt: vom Bund (Sanierungsoffensive), vom jeweiligen Bundesland, für
einkommensschwache Haushalte durch das Sonderprogramm „Sauber Heizen für Alle“ und über die Steuer
(Öko-Sonderausgabenpauschale). Betriebe haben eine eigene Schiene. Die Tabelle zeigt die Eckwerte,
die Details folgen in den Abschnitten darunter. Stand: April 2026.</p>
{A.table(
    ["Fördertopf", "Für wen", "Höhe", "Frist / Ablauf"],
    [
        ["Sanierungsoffensive 2026 (Bund)", "Eigentümer von Ein-, Zweifamilien- und Reihenhäusern",
         "bis 7.500 €, mit Bohrbonus Erdwärme bis 12.500 €, max. 30 % der Kosten",
         "Registrierung bis 31.12.2026, 9 Monate Umsetzungsfrist"],
        ["Landesförderungen", "je nach Bundesland Eigentümer, teils auch Mieter",
         "z. B. Wien 35 % bis 8.000 €, Salzburg rund 5.000 €, OÖ 100 €/kW bis 1.700 €",
         "eigene Portale, teils vor, teils nach Umsetzung"],
        ["Sauber Heizen für Alle", "Haushalte im unteren Einkommensdrittel mit Hauptwohnsitz",
         "bis 100 % der Kosten, Obergrenze 25.586 € (Luft-Wasser) bzw. 37.550 € (Sole-Wasser)",
         "Registrierung seit 1.1.2026 bis 31.12.2026"],
        ["Öko-Sonderausgabenpauschale", "Private mit ausbezahlter Bundesförderung",
         "5 Jahre je 400 € Sonderausgaben (2.000 €)", "automatisch über die Steuerveranlagung"],
        ["Betriebsförderung (KPC)", "Unternehmen, Vereine, konfessionelle Einrichtungen",
         "bis 7.500 € (unter 50 kW), bis 12.000 € (50 bis 100 kW), max. 50 %",
         "Antrag bis 6 Monate nach Schlussrechnung"],
    ],
    hl_cols=(2,),
)}
"""),
        ("Bundesförderung Sanierungsoffensive 2026: das Fundament", "bund", f"""
<p>Die {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive 2026')} ist das zentrale Programm der
Bundesregierung für den Heizungstausch. Sie richtet sich an Eigentümerinnen und Eigentümer von Ein- und
Zweifamilienhäusern sowie Reihenhäusern, die eine bestehende Öl-, Gas-, Kohle- oder Elektroheizung
vollständig durch eine Wärmepumpe ersetzen. Gefördert werden Material, Montage, Planung und die
fachgerechte Entsorgung der Altanlage.</p>
<ul>
  <li><b>Förderhöhe:</b> bis zu 7.500 € für eine Luft-Wasser-Wärmepumpe. Für Erdwärme (Sole-Wasser)
  kommt ein Bohrbonus von 5.000 € dazu, in Summe bis zu 12.500 € allein vom Bund. Deckel: maximal 30 %
  der förderfähigen Investitionskosten.</li>
  <li><b>Voraussetzungen:</b> EHPA-Gütesiegel, Kältemittel mit GWP-Wert von höchstens 750, maximale
  Vorlauftemperatur 55 °C, Installation durch einen zertifizierten Fachbetrieb. Vor der Registrierung
  ist eine Energieberatung Pflicht, deren Protokoll bei der Registrierung vorliegen muss.</li>
  <li><b>Ablauf:</b> Registrierung online auf sanierungsoffensive.gv.at. Danach bleiben 9 Monate für
  Umsetzung und Endabrechnung. Prüfung und Auszahlung übernimmt die Kommunalkredit Public Consulting (KPC).</li>
</ul>
{A.box("Die Registrierung ist bis 31. Dezember 2026 möglich, aber nur solange Budget vorhanden ist. "
       "Laut Stand April 2026 waren bereits über 60 % der Mittel gebunden. Registrieren Sie sich, bevor "
       "Sie den ersten Auftrag unterschreiben.", label="Frist:")}
"""),
        ("Sauber Heizen für Alle: bis zu 100 % für einkommensschwache Haushalte", "sauber-heizen", f"""
<p>Das Programm {a('/sauber-heizen-fuer-alle-2026/', '„Sauber Heizen für Alle“')} richtet sich an
Haushalte im unteren Einkommensdrittel und kann bis zu 100 % der förderfähigen Kosten abdecken.
Antragsberechtigt sind Eigentümerinnen und Eigentümer von Ein- oder Zweifamilienhäusern mit
Hauptwohnsitz am Standort des Heizungstausches.</p>
<ul>
  <li><b>Einkommensgrenze:</b> 1.867 € netto pro Monat für einen Einpersonenhaushalt. Für jeden
  weiteren Erwachsenen kommen 50 % dazu, für jedes Kind 30 %.</li>
  <li><b>Kostenobergrenze:</b> 25.586 € für Luft-Wasser-Wärmepumpen, 37.550 € für Sole-Wasser-Systeme.
  Bis zu dieser Grenze wird die Kombination aus Bundes-, Landes- und Sonderförderung ausbezahlt, im
  Idealfall ohne Eigenanteil.</li>
  <li><b>Ablauf:</b> Registrierung auf sauber-heizen.at, möglich seit 1. Jänner 2026 bis 31. Dezember
  2026. Die Landesförderungsstelle prüft die Unterlagen, organisiert eine kostenlose Energieberatung
  und begleitet den gesamten Prozess.</li>
</ul>
"""),
        ("Landesförderungen: So stocken die Bundesländer auf", "laender", f"""
<p>Alle neun Bundesländer bieten eigene Programme für den Wärmepumpen-Einbau, die in der Regel mit der
Bundesförderung kombiniert werden können. Die Beträge unterscheiden sich deutlich:</p>
{A.table(
    ["Bundesland", "Landesförderung", "Besonderheit"],
    [
        ["Wien", "35 % der förderbaren Kosten, max. 8.000 €", "auch für Mieterinnen und Mieter"],
        ["Salzburg", "rund 5.000 €", "Bestand und Neubau"],
        ["Oberösterreich", "100 € je kW Nennwärmeleistung, max. 1.700 €", "begrenzt auf 50 % der Kosten"],
        ["Kärnten, Steiermark, NÖ, Tirol, Vorarlberg, Burgenland", "eigene Programme, unterschiedliche Beträge",
         f"Details im {a('/landesfoerderungen-fuer-die-waermepumpe/', 'Landesförderungs-Ratgeber')}"],
    ],
    hl_cols=(1,),
)}
<p>Rechenbeispiele aus den Ländern: In Wien ergeben 7.500 € Bund plus 8.000 € Land bei 28.000 €
Projektkosten 15.500 € Gesamtförderung (rund 55 %). Tirol kommt mit 25 % Landeszuschuss plus 3.000 €
Bonus auf bis zu 18.000 € (rund 60 %). Dabei gilt immer: Die Summe aller Förderungen darf die
tatsächlichen Investitionskosten nicht übersteigen. Eine laufend aktualisierte Übersicht führt der
Verband Wärmepumpe Austria (Quelle unten).</p>
{A.cta("Welche Förderung passt zu Ihrem Haus?",
       "EBZ Energie rechnet für Ihr Projekt in Kärnten oder der Steiermark durch, welche Kombination aus "
       "Bund, Land und Gemeinde die höchste Gesamtförderung ergibt, und übernimmt die Einreichung.",
       secondary=("waermepumpe", "Zur Wärmepumpen-Leistungsseite"))}
"""),
        ("Steuerbonus: die Öko-Sonderausgabenpauschale", "steuer", f"""
<p>Bleiben nach Abzug aller Förderungen Restkosten von mehr als 2.000 €, greift die
{a('/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/', 'Öko-Sonderausgabenpauschale')}:
Fünf Jahre lang werden jeweils 400 €, in Summe 2.000 €, automatisch als Sonderausgaben in der
Steuerveranlagung berücksichtigt. Ein eigener Antrag ist nicht nötig, die Daten übermittelt die KPC
an die Finanzverwaltung, sofern Sie bei der Förderantragstellung zugestimmt haben.</p>
<p>Die Begünstigung gilt seit 2022 für den Austausch fossiler Heizsysteme in privat genutzten
Gebäuden. Die tatsächliche Steuerersparnis hängt vom persönlichen Steuersatz ab: Bei 42 % Grenzsteuersatz
sind es rund 168 € pro Jahr, also etwa 840 € über fünf Jahre.</p>
"""),
        ("Förderung für Unternehmen, Vereine und Gemeinden", "betriebe", f"""
<p>Auch Betriebe, Vereine und konfessionelle Einrichtungen werden beim Tausch eines fossilen Heizsystems
unterstützt, über die {a('/unternehmensfoerderung-von-waermepumpen/', 'Betriebsförderung der KPC')}:</p>
<ul>
  <li>Anlagen unter 50 kW: maximal 7.500 €</li>
  <li>Anlagen von 50 bis 100 kW: maximal 12.000 €</li>
  <li>Förderquote: maximal 50 % der förderfähigen Kosten, kombinierbar mit Landesförderungen</li>
</ul>
<p>Der Antrag wird online gestellt, anders als bei Privathaushalten aber erst nach Umsetzung des
Projekts, innerhalb von sechs Monaten nach der Schlussrechnung.</p>
"""),
        ("Wärmepumpe und Photovoltaik: die Förderungen gemeinsam nutzen", "kombination", f"""
<p>Eine Wärmepumpe braucht Strom. Wer sie mit einer {a('photovoltaik', 'Photovoltaikanlage')} kombiniert,
senkt die Betriebskosten dauerhaft und nutzt zwei getrennte Fördertöpfe: die Sanierungsoffensive für
den Heizungstausch und den EAG-Investitionszuschuss für die PV-Anlage. Wie beide Systeme technisch
zusammenspielen, lesen Sie im Ratgeber
{a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}. Wer die Investition
nicht auf einmal stemmen will, kann sie über eine {a('finanzierung', 'Finanzierung')} verteilen; die
Anlage gehört dabei ab dem ersten Tag Ihnen, die Förderungen bleiben voll erhalten.</p>
"""),
        ("Fazit: Erst registrieren, dann beauftragen", "fazit", f"""
<p>2026 lassen sich Bundesförderung, Landesförderung und Steuerbonus zu einer Gesamtförderung
kombinieren, die je nach Bundesland und Projekt 12.500 bis 18.000 € erreichen kann. Entscheidend sind
zwei Dinge: die Reihenfolge (Energieberatung, Registrierung, dann Auftrag) und das Tempo, weil das
Bundesbudget nach dem Prinzip „First Come, First Served“ vergeben wird und Registrierungen enden, sobald
es ausgeschöpft ist. Was eine Wärmepumpe kostet, zeigt der Ratgeber
{a('/kosten-einer-waermepumpe/', 'Kosten einer Wärmepumpe')}.</p>
{A.cta("Förderung sichern, bevor das Budget aufgebraucht ist",
       "Wir prüfen Ihre Förderfähigkeit, organisieren die Energieberatung und registrieren Ihr Projekt "
       "im richtigen Moment.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Wärmepumpe und Förderung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Wärmepumpen und Photovoltaik in Kärnten und "
                 "der Steiermark, mit einem festangestellten Team aus zertifizierten Fachkräften. Wir "
                 "analysieren Ihre Situation, kombinieren Bundes-, Landes- und Gemeindeförderung und "
                 "übernehmen Registrierung, Unterlagen und fristgerechte Einreichung."),
        "grid": [
            ("Persönliche Förderberatung", "Wir berechnen, welche Töpfe Sie kombinieren können."),
            ("Komplette Förderabwicklung", "Registrierung, Unterlagen, Endabrechnung: alles aus einer Hand."),
            ("Förderkonforme Installation", "EHPA-Gütesiegel, GWP unter 750, Vorlauf 55 °C: wir planen passend."),
            ("Energieberatung organisiert", "Das verpflichtende Beratungsprotokoll kümmern wir uns mit."),
        ],
    },

    "faq": [
        ("Wer kann die Wärmepumpenförderung 2026 beantragen?",
         "In erster Linie private Eigentümerinnen und Eigentümer von Ein- und Zweifamilienhäusern sowie "
         "Reihenhäusern in Österreich, die eine fossile Heizung vollständig durch eine Wärmepumpe ersetzen. "
         "Die Installation muss ein zertifizierter Fachbetrieb durchführen. Auch Eigentümergemeinschaften "
         "und Hausverwaltungen im mehrgeschossigen Wohnbau sowie Betriebe und Vereine haben eigene "
         "Förderschienen."),
        ("Kann ich Bundes- und Landesförderung kombinieren?",
         "Ja, in den meisten Fällen ist die Kombination ausdrücklich erlaubt. So kommen zu den bis zu 7.500 € "
         "des Bundes je nach Bundesland mehrere Tausend Euro dazu, in Wien zum Beispiel bis zu 8.000 €. Die "
         "Summe aller Förderungen darf die tatsächlichen Investitionskosten aber nie übersteigen."),
        ("Was kostet eine Wärmepumpe in Österreich insgesamt?",
         "Für eine Luft-Wasser-Wärmepumpe inklusive Installation sollten Sie mit rund 10.000 bis 18.000 € "
         "rechnen, für Erdwärmepumpen mit Bohrung eher mit 18.000 bis 25.000 € (Richtwerte, abhängig von "
         "Gebäude und System). Nach Abzug aller Förderungen sinkt der Eigenanteil oft um mehr als die Hälfte."),
        ("Muss ich die Förderung vor oder nach der Installation beantragen?",
         "Für Privatpersonen gilt: Erst registrieren, dann umsetzen. Bei der Sanierungsoffensive sind zwar "
         "Leistungen ab 3. Oktober 2025 rückwirkend förderfähig, ohne Registrierung ist das Budget aber nicht "
         "reserviert. Bei „Sauber Heizen für Alle“ sind Leistungen vor der Antragstellung nicht förderfähig. "
         "Betriebe stellen den Antrag nach Umsetzung, bis sechs Monate nach der Schlussrechnung."),
        ("Was passiert, wenn das Förderbudget aufgebraucht ist?",
         "Sobald die Mittel erschöpft sind, werden keine neuen Registrierungen mehr angenommen, auch wenn der "
         "31. Dezember 2026 noch nicht erreicht ist. Im April 2026 waren bereits über 60 % der Mittel "
         "gebunden. Den aktuellen Budgetstand zeigt sanierungsoffensive.gv.at."),
        ("Wie hoch ist die Förderung für eine Erdwärme-Wärmepumpe?",
         "Zur Grundpauschale von 7.500 € kommt bei Sole-Wasser- oder Wasser-Wasser-Wärmepumpen mit Tiefen- "
         "oder Brunnenbohrung ein Bohrbonus von 5.000 €. In Summe sind bis zu 12.500 € vom Bund möglich, "
         "gedeckelt mit 30 % der förderfähigen Kosten."),
        ("Gibt es zusätzlich einen Steuervorteil?",
         "Ja. Bleiben nach Abzug aller Förderungen mehr als 2.000 € Restkosten, werden fünf Jahre lang je "
         "400 € automatisch als Sonderausgaben berücksichtigt (Öko-Sonderausgabenpauschale). Bei 42 % "
         "Grenzsteuersatz entspricht das rund 840 € Steuerersparnis über fünf Jahre."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Wärmepumpen und Photovoltaik in Kärnten und der Steiermark und übernimmt die komplette "
                    "Förderabwicklung. Alle Beträge und Fristen entsprechen dem Stand April 2026. Keine Rechts- "
                    "oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("Sanierungsoffensive 2026 (Bundesportal)", "https://www.sanierungsoffensive.gv.at/"),
        ("Sauber Heizen für Alle (Bundesportal)", "https://www.sauber-heizen.at/"),
        ("Verband Wärmepumpe Austria: Förderübersicht", "https://www.waermepumpe-austria.at/foerderungen"),
    ],
    "related": [
        ("/sanierungsoffensive-2026/", "Sanierungsoffensive 2026: bis zu 7.500 € vom Bund"),
        ("/landesfoerderungen-fuer-die-waermepumpe/", "Landesförderungen: alle 9 Bundesländer"),
        ("/sauber-heizen-fuer-alle-2026/", "Sauber Heizen für Alle: bis zu 100 %"),
        ("waermepumpe", "Wärmepumpen-Installateur EBZ Energie"),
    ],
    "cta": {
        "h3": "Förderung nicht verschenken",
        "text": "Wir prüfen, welche Fördertöpfe für Ihren Heizungstausch gelten, und übernehmen die Einreichung.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Raus aus Öl und Gas, mit voller Förderung",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
