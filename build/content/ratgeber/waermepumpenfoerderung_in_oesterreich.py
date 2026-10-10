"""Ratgeber: Wärmepumpenförderung Österreich 2026 (Überblick über alle Fördertöpfe).

Stand Oktober 2026: Bundesprogramme (Sanierungsoffensive/Kesseltausch, Sauber Heizen fuer Alle) BEENDET,
Mittel ausgeschoepft (umweltfoerderung.at, 9.10.2026). Konditionen als "galt 2026", Status-Box oben.

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
    "title": "Wärmepumpenförderung 2026: Bund beendet, Länder laufen | EBZ",
    "description": ("Wärmepumpenförderung 2026: Bundesprogramme (bis 7.500 €, Sauber Heizen) seit Herbst 2026 "
                    "ausgeschöpft. Was 2026 galt, welche Länder zahlen, Ausblick 2027."),
    "eyebrow": "Förderung · Wärmepumpe",
    "crumb_label": "Wärmepumpenförderung 2026",
    "h1": "Wärmepumpenförderung in Österreich 2026: Bund ausgeschöpft, was jetzt noch gilt. Alle Fördertöpfe im Überblick",
    "lead": ("Stand Oktober 2026: Die Bundesförderung für den Heizungstausch (bis 7.500 €, Sauber Heizen für Alle "
             "bis 100 %) ist ausgeschöpft, neue Registrierungen sind nicht möglich. Weiter laufen die "
             "Landesprogramme und, für bereits Registrierte, der Steuerbonus. Dieser Überblick zeigt, was 2026 "
             "galt, was jetzt noch offen ist und wie es 2027 weitergehen könnte."),
    "chips": [
        "Bund 2026: <b>beendet</b> (Stand Oktober 2026)",
        "Galt 2026: <b>bis 7.500 €</b> (Erdwärme 12.500 €)",
        "Land: <b>bis 8.000 €</b> (Wien)",
        "Ausblick 2027: <b>offen</b>",
    ],
    "date_published": "2026-03-05",
    "date_modified": "2026-10-10",
    "hero_img": "foerderung",
    "hero_alt": "Beratungsgespräch zur Wärmepumpenförderung mit Unterlagen und Taschenrechner",

    "tldr": [
        "Stand Oktober 2026: Die Sanierungsoffensive 2026 (Kesseltausch bis 7.500 €, Erdwärme 12.500 €) und "
        "„Sauber Heizen für Alle 2026“ sind beendet, die Mittel ausgeschöpft. Neue Registrierungen sind nicht "
        "möglich (umweltfoerderung.at). Wer registriert ist, setzt innerhalb der Fristen um.",
        "Die meisten Bundesländer haben eigene Zuschüsse, zum Beispiel Wien 35 % bis 8.000 €, Salzburg "
        "rund 5.000 €, Kärnten 3.000 € Pauschale, Oberösterreich 100 € je kW bis 1.700 €. Die Steiermark nimmt "
        "für neue Wärmepumpen derzeit keine Förderanträge an. Bund und Land waren in der Regel kombinierbar.",
        "„Sauber Heizen für Alle“ übernahm 2026 für Haushalte im unteren Einkommensdrittel bis zu 100 % der "
        "Kosten (Obergrenze 25.586 € Luft-Wasser, 37.550 € Sole-Wasser); Registrierte können noch beantragen.",
        "Die Öko-Sonderausgabenpauschale bringt zusätzlich fünf Jahre lang 400 € Sonderausgaben, wenn nach "
        "Förderabzug mehr als 2.000 € Restkosten bleiben.",
        "Betriebe, Vereine und Gemeinden erhalten bis zu 7.500 € (unter 50 kW) oder 12.000 € (50 bis 100 kW), "
        "maximal 50 % der Kosten (eigene KPC-Schiene, Stand prüfen). Ob 2027 ein neues Bundesprogramm für "
        "Private kommt, ist offen.",
    ],
    "kpis": [
        ("beendet", "Bundesförderung 2026, Stand Oktober 2026"),
        ("7.500 €", "Bundesförderung Wärmepumpe (galt 2026)"),
        ("8.000 €", "höchster Landeszuschuss (Wien)"),
        ("2.000 €", "Öko-Sonderausgabenpauschale (mit Bundesförderung)"),
    ],

    "sections": [
        ("Stand Oktober 2026: Bund ausgeschöpft, was noch läuft", "status", f"""
<p><b>Die Bundesförderung 2026 für den Heizungstausch (Kesseltausch bis 7.500 Euro, Sauber Heizen für
Alle bis 100 Prozent) ist seit Herbst 2026 ausgeschöpft, neue Registrierungen sind nicht möglich</b>
(Quelle: umweltfoerderung.at, Stand 9. Oktober 2026). Weiter laufen Landesförderungen: Kärnten zahlt
2026 eine Pauschale von 3.000 Euro (plus 1.500 Euro bei Errichtung einer Solaranlage, plus 200 Euro für den
hydraulischen Abgleich); ob das Budget reicht, klären wir vor dem Angebot. Die Steiermark nimmt für neue
Wärmepumpen derzeit keine Förderanträge an (wohnbau.steiermark.at, Stand 10. Oktober 2026). Ob ein Land
ohne Bundesförderung zahlt, klärt die Landesstelle. Ob 2027 ein neues
Bundesprogramm kommt, ist offen.</p>
{A.box_dark("Was das für Ihr Projekt heißt",
    "Bereits registrierte Haushalte setzen innerhalb ihrer Frist um (Sanierungsoffensive: 9 Monate ab "
    "Registrierung, Sauber Heizen für Alle: 12 Monate ab Zusage) und erhalten danach auch die "
    "Öko-Sonderausgabenpauschale. Wer neu plant, klärt die Landesförderung mit der Landesstelle und baut die "
    "Wärmepumpe so, dass sie die bekannten Bundeskriterien erfüllt, falls 2027 ein Folgeprogramm startet.")}
"""),
        ("Wer 2026 wie viel bekam: die vier Fördertöpfe", "ueberblick", f"""
<p>Der Umstieg von Öl, Gas, Kohle oder Strom auf eine {a('waermepumpe', 'Wärmepumpe')} wurde 2026 aus
vier Richtungen unterstützt: vom Bund (Sanierungsoffensive), vom jeweiligen Bundesland, für
einkommensschwache Haushalte durch das Sonderprogramm „Sauber Heizen für Alle“ und über die Steuer
(Öko-Sonderausgabenpauschale). Betriebe haben eine eigene Schiene. Die Tabelle zeigt die Eckwerte,
die Details folgen in den Abschnitten darunter. Konditionen: Stand April 2026; Programmstatus: Stand
Oktober 2026.</p>
{A.table(
    ["Fördertopf", "Für wen", "Höhe", "Frist / Ablauf"],
    [
        ["Sanierungsoffensive 2026 (Bund)", "Eigentümer von Ein-, Zweifamilien- und Reihenhäusern",
         "bis 7.500 €, mit Bohrbonus Erdwärme bis 12.500 €, max. 30 % der Kosten (galt 2026)",
         "beendet seit Herbst 2026, Mittel ausgeschöpft; Registrierte: 9 Monate Umsetzungsfrist"],
        ["Landesförderungen", "je nach Bundesland Eigentümer, teils auch Mieter",
         "z. B. Wien 35 % bis 8.000 €, Salzburg rund 5.000 €, OÖ 100 €/kW bis 1.700 €",
         "eigene Portale, teils vor, teils nach Umsetzung"],
        ["Sauber Heizen für Alle", "Haushalte im unteren Einkommensdrittel mit Hauptwohnsitz",
         "bis 100 % der Kosten, Obergrenze 25.586 € (Luft-Wasser) bzw. 37.550 € (Sole-Wasser) (galt 2026)",
         "beendet, keine neuen Registrierungen; Registrierte können noch beantragen"],
        ["Öko-Sonderausgabenpauschale", "Private mit ausbezahlter Bundesförderung (damit nur für Registrierte)",
         "5 Jahre je 400 € Sonderausgaben (2.000 €)", "automatisch über die Steuerveranlagung"],
        ["Betriebsförderung (KPC)", "Unternehmen, Vereine, konfessionelle Einrichtungen",
         "bis 7.500 € (unter 50 kW), bis 12.000 € (50 bis 100 kW), max. 50 %",
         "Antrag bis 6 Monate nach Schlussrechnung"],
    ],
    hl_cols=(2,),
)}
"""),
        ("Bundesförderung Sanierungsoffensive 2026: das Fundament (seit Herbst 2026 ausgeschöpft)", "bund", f"""
<p>Die {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive 2026')} war das zentrale Programm der
Bundesregierung für den Heizungstausch. Sie richtete sich an Eigentümerinnen und Eigentümer von Ein- und
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
{A.box("Stand 9. Oktober 2026: Die Mittel sind ausgeschöpft, Registrierung und Antragstellung sind laut "
       "umweltfoerderung.at nicht mehr möglich. Im April 2026 waren bereits über 60 % der Mittel gebunden. "
       "Wer registriert ist, hält die 9-Monats-Frist für Umsetzung und Endabrechnung ein.", label="Status:")}
"""),
        ("Sauber Heizen für Alle: bis zu 100 % für einkommensschwache Haushalte (beendet)", "sauber-heizen", f"""
<p>Das Programm {a('/sauber-heizen-fuer-alle-2026/', '„Sauber Heizen für Alle“')} richtete sich an
Haushalte im unteren Einkommensdrittel und konnte bis zu 100 % der förderfähigen Kosten abdecken. Seit
Herbst 2026 werden keine neuen Registrierungen angenommen, Registrierte können noch beantragen.
Antragsberechtigt waren Eigentümerinnen und Eigentümer von Ein- oder Zweifamilienhäusern mit
Hauptwohnsitz am Standort des Heizungstausches.</p>
<ul>
  <li><b>Einkommensgrenze:</b> 1.867 € netto pro Monat für einen Einpersonenhaushalt. Für jeden
  weiteren Erwachsenen kommen 50 % dazu, für jedes Kind 30 %.</li>
  <li><b>Kostenobergrenze:</b> 25.586 € für Luft-Wasser-Wärmepumpen, 37.550 € für Sole-Wasser-Systeme.
  Bis zu dieser Grenze wird die Kombination aus Bundes-, Landes- und Sonderförderung ausbezahlt, im
  Idealfall ohne Eigenanteil.</li>
  <li><b>Ablauf:</b> Registrierung auf sauber-heizen.at, möglich seit 1. Jänner 2026, seit Herbst 2026
  geschlossen. Für Registrierte prüft die Landesförderungsstelle die Unterlagen, organisiert eine kostenlose
  Energieberatung und begleitet den gesamten Prozess.</li>
</ul>
"""),
        ("Landesförderungen: So stocken die Bundesländer auf", "laender", f"""
<p>Die meisten Bundesländer bieten eigene Programme für den Wärmepumpen-Einbau, die in der Regel mit der
Bundesförderung kombiniert werden konnten. Die Beträge unterscheiden sich deutlich, die Steiermark nimmt
für neue Wärmepumpen derzeit keine Förderanträge an:</p>
{A.table(
    ["Bundesland", "Landesförderung", "Besonderheit"],
    [
        ["Wien", "35 % der förderbaren Kosten, max. 8.000 €", "auch für Mieterinnen und Mieter"],
        ["Salzburg", "rund 5.000 €", "Bestand und Neubau"],
        ["Oberösterreich", "100 € je kW Nennwärmeleistung, max. 1.700 €", "begrenzt auf 50 % der Kosten"],
        ["Kärnten", "3.000 € Pauschale (2026)", "plus 1.500 € bei Errichtung einer Solaranlage, plus 200 € hydraulischer Abgleich"],
        ["Steiermark", "derzeit keine Anträge für neue Wärmepumpen",
         "nur Tausch mind. 15 Jahre alter Biomassekessel oder Wärmepumpen: höchstens 30 %, höchstens 1.500 €"],
        ["NÖ, Tirol, Vorarlberg, Burgenland", "eigene Programme, unterschiedliche Beträge",
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
senkt die Betriebskosten dauerhaft. 2026 gab es dafür zwei getrennte Fördertöpfe: die Sanierungsoffensive
für den Heizungstausch (seit Herbst 2026 ausgeschöpft) und den EAG-Investitionszuschuss für die PV-Anlage
(letzter Call bis 22. Oktober 2026, ab 2027 laut BMWET Systemförderung mit Antrag nach Installation). Wie
beide Systeme technisch
zusammenspielen, lesen Sie im Ratgeber
{a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}. Wer die Investition
nicht auf einmal stemmen will, kann sie über eine {a('finanzierung', 'Finanzierung')} verteilen; die
Anlage gehört dabei ab dem ersten Tag Ihnen, die Förderungen bleiben voll erhalten.</p>
"""),
        ("Fazit: Was nach dem Förderstopp des Bundes gilt", "fazit", f"""
<p>2026 ließen sich Bundesförderung, Landesförderung und Steuerbonus zu einer Gesamtförderung
kombinieren, die je nach Bundesland und Projekt 12.500 bis 18.000 € erreichen konnte. Das Bundesbudget
wurde nach „First Come, First Served“ vergeben und war im Herbst 2026 ausgeschöpft. Wer registriert ist,
hält seine Fristen ein. Wer neu plant, klärt die Landesförderung mit der Landesstelle, baut förderkonform
und behält den Ausblick auf ein mögliches Bundesprogramm 2027 im Blick. Was eine Wärmepumpe kostet, zeigt
der Ratgeber {a('/kosten-einer-waermepumpe/', 'Kosten einer Wärmepumpe')}.</p>
{A.cta("Offene Förderwege prüfen lassen",
       "Wir prüfen, welche Landesförderung für Ihr Projekt möglich ist, begleiten Registrierte bis zur "
       "Endabrechnung und informieren Sie, sobald ein neues Bundesprogramm startet.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Wärmepumpe und Förderung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Wärmepumpen und Photovoltaik in Kärnten und "
                 "der Steiermark, mit zertifizierten Fachkräften. Wir "
                 "analysieren Ihre Situation, prüfen Landes- und Gemeindeförderung und "
                 "übernehmen Unterlagen und fristgerechte Einreichung, bei Registrierten bis zur Endabrechnung."),
        "grid": [
            ("Persönliche Förderberatung", "Wir berechnen, welche Töpfe Sie kombinieren können."),
            ("Komplette Förderabwicklung", "Landesantrag, Unterlagen, Endabrechnung für Registrierte: alles aus einer Hand."),
            ("Förderkonforme Installation", "EHPA-Gütesiegel, GWP unter 750, Vorlauf 55 °C: wir planen passend."),
            ("Energieberatung organisiert", "Das verpflichtende Beratungsprotokoll kümmern wir uns mit."),
        ],
    },

    "faq": [
        ("Gibt es 2026 noch eine Bundesförderung für die Wärmepumpe?",
         "Nein. Stand Oktober 2026 sind die Sanierungsoffensive (Kesseltausch bis 7.500 €) und „Sauber Heizen für "
         "Alle 2026“ laut umweltfoerderung.at beendet, die Mittel sind ausgeschöpft und neue Registrierungen nicht "
         "möglich. Bereits Registrierte können innerhalb ihrer Fristen umsetzen. Ob 2027 ein neues Programm "
         "kommt, ist offen."),
        ("Wer konnte die Wärmepumpenförderung 2026 beantragen?",
         "In erster Linie private Eigentümerinnen und Eigentümer von Ein- und Zweifamilienhäusern sowie "
         "Reihenhäusern in Österreich, die eine fossile Heizung vollständig durch eine Wärmepumpe ersetzen. "
         "Die Installation muss ein zertifizierter Fachbetrieb durchführen. Auch Eigentümergemeinschaften "
         "und Hausverwaltungen im mehrgeschossigen Wohnbau sowie Betriebe und Vereine haben eigene "
         "Förderschienen."),
        ("Kann ich Bundes- und Landesförderung kombinieren?",
         "Ja, in den meisten Fällen war die Kombination ausdrücklich erlaubt. So kamen zu den bis zu 7.500 € "
         "des Bundes je nach Bundesland mehrere Tausend Euro dazu, in Wien zum Beispiel bis zu 8.000 €. Seit dem "
         "Förderstopp des Bundes klären Sie mit der Landesstelle, ob die Landesförderung auch ohne Bundesförderung "
         "gewährt wird. Die "
         "Summe aller Förderungen darf die tatsächlichen Investitionskosten aber nie übersteigen."),
        ("Was kostet eine Wärmepumpe in Österreich insgesamt?",
         "Für eine Luft-Wasser-Wärmepumpe inklusive Installation sollten Sie mit rund 10.000 bis 18.000 € "
         "rechnen, für Erdwärmepumpen mit Bohrung eher mit 18.000 bis 25.000 € (Richtwerte, abhängig von "
         "Gebäude und System). Nach Abzug aller Förderungen sinkt der Eigenanteil oft um mehr als die Hälfte."),
        ("Muss ich die Förderung vor oder nach der Installation beantragen?",
         "Für Privatpersonen galt: Erst registrieren, dann umsetzen (seit Herbst 2026 ist keine Registrierung "
         "mehr möglich). Bei der Sanierungsoffensive waren zwar "
         "Leistungen ab 3. Oktober 2025 rückwirkend förderfähig, ohne Registrierung ist das Budget aber nicht "
         "reserviert. Bei „Sauber Heizen für Alle“ sind Leistungen vor der Antragstellung nicht förderfähig. "
         "Betriebe stellen den Antrag nach Umsetzung, bis sechs Monate nach der Schlussrechnung."),
        ("Was passiert, wenn das Förderbudget aufgebraucht ist?",
         "Genau das ist 2026 eingetreten: Seit Herbst 2026 werden keine neuen Registrierungen mehr angenommen, "
         "obwohl der 31. Dezember 2026 noch nicht erreicht ist. Im April 2026 waren bereits über 60 % der Mittel "
         "gebunden. Den aktuellen Stand zeigt umweltfoerderung.at."),
        ("Wie hoch ist die Förderung für eine Erdwärme-Wärmepumpe?",
         "2026 galt: Zur Grundpauschale von 7.500 € kam bei Sole-Wasser- oder Wasser-Wasser-Wärmepumpen mit "
         "Tiefen- oder Brunnenbohrung ein Bohrbonus von 5.000 €, in Summe bis zu 12.500 € vom Bund, gedeckelt "
         "mit 30 % der förderfähigen Kosten. Das Programm ist seit Herbst 2026 ausgeschöpft."),
        ("Gibt es zusätzlich einen Steuervorteil?",
         "Ja. Bleiben nach Abzug aller Förderungen mehr als 2.000 € Restkosten, werden fünf Jahre lang je "
         "400 € automatisch als Sonderausgaben berücksichtigt (Öko-Sonderausgabenpauschale). Bei 42 % "
         "Grenzsteuersatz entspricht das rund 840 € Steuerersparnis über fünf Jahre."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Wärmepumpen und Photovoltaik in Kärnten und der Steiermark und übernimmt die komplette "
                    "Förderabwicklung. Beträge: Stand April 2026 (Kärnten und Steiermark: Stand 10. Oktober 2026); Programmstatus: Stand 9. Oktober 2026 laut "
                    "umweltfoerderung.at. Keine Rechts- "
                    "oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("Sanierungsoffensive 2026 (Bundesportal)", "https://www.sanierungsoffensive.gv.at/"),
        ("Sauber Heizen für Alle (Bundesportal)", "https://www.sauber-heizen.at/"),
        ("Verband Wärmepumpe Austria: Förderübersicht", "https://www.waermepumpe-austria.at/foerderungen"),
        ("Land Steiermark: Förderung für Heizungen (Wohnbau, Stand 10. Oktober 2026)",
         "https://www.wohnbau.steiermark.at/cms/ziel/164947118/DE/"),
    ],
    "related": [
        ("/sanierungsoffensive-2026/", "Sanierungsoffensive 2026: beendet, das gilt jetzt"),
        ("/landesfoerderungen-fuer-die-waermepumpe/", "Landesförderungen: alle 9 Bundesländer"),
        ("/sauber-heizen-fuer-alle-2026/", "Sauber Heizen für Alle 2026: beendet, was für Registrierte gilt"),
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
