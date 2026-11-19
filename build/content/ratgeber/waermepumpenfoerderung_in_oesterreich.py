"""Ratgeber: Wärmepumpenförderung Österreich 2026 (Überblick über alle Fördertöpfe).

Stand 19.11.2026: Bundesförderung Kesseltausch seit 2.11.2026 neu aufgelegt (5.000 € Wärmepumpe, +5.000 €
Bohrbonus, +2.500 € Solarthermie, Registrierung bis 31.12.2026; Infoblatt KPC 10/2026, siehe
build/seo/_fakten_2026-10.md). "Sauber Heizen fuer Alle" bleibt geschlossen. 7.500 € nur als Historie.

Migriert vom WordPress-Artikel ebz-photovoltaik.at/waermepumpenfoerderung-in-oesterreich/
(veröffentlicht 2026-03-05, zuletzt geändert 2026-04-12). Länderzahlen: Stand April 2026.
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
    "title": "Wärmepumpenförderung 2026: Bund 5.000 € plus Land | EBZ",
    "description": ("Wärmepumpenförderung 2026: Kesseltausch seit 2.11.2026 neu, 5.000 € vom Bund plus "
                    "Landesförderung (Kärnten 3.000 €). Alle Töpfe, Fristen, Ausblick 2027."),
    "eyebrow": "Förderung · Wärmepumpe",
    "crumb_label": "Wärmepumpenförderung 2026",
    "h1": "Wärmepumpenförderung in Österreich 2026: Kesseltausch neu aufgelegt. Alle Fördertöpfe im Überblick",
    "lead": ("Stand November 2026: Seit 2. November 2026 fördert der Bund den Heizungstausch wieder, mit 5.000 € "
             "Pauschale für die Wärmepumpe (plus 5.000 € Bohrbonus bei Erdwärme, plus 2.500 € bei Solarthermie). "
             "Registrieren können Sie bis 31. Dezember 2026 oder bis das Budget aufgebraucht ist. Dazu kommen die "
             "Landesprogramme und der Steuerbonus; „Sauber Heizen für Alle“ bleibt geschlossen. Dieser Überblick "
             "zeigt, was jetzt gilt und wie es 2027 weitergeht."),
    "chips": [
        "Bund: <b>5.000 €</b> Wärmepumpe (seit 2.11.2026)",
        "Erdwärme: <b>+5.000 €</b> Bohrbonus",
        "Land: <b>bis 8.000 €</b> (Wien)",
        "Registrierung <b>bis 31.12.2026</b>",
    ],
    "date_published": "2026-03-05",
    "date_modified": "2026-11-19",
    "hero_img": "foerderung",
    "hero_alt": "Beratungsgespräch zur Wärmepumpenförderung mit Unterlagen am Tisch",

    "tldr": [
        "Stand November 2026: Der Kesseltausch des Bundes (Sanierungsoffensive) ist seit 2. November 2026 neu "
        "aufgelegt. Wärmepumpe 5.000 €, Bohrbonus bei Erdwärme +5.000 €, thermische Solaranlage ab 6 m² "
        "+2.500 €. Registrierung bis 31. Dezember 2026 oder bis das Budget aufgebraucht ist. In der ersten "
        "Aktion 2026 waren es bis zu 7.500 €.",
        "Die meisten Bundesländer haben eigene Zuschüsse, zum Beispiel Wien 35 % bis 8.000 €, Salzburg "
        "rund 5.000 €, Kärnten 3.000 € Pauschale, Oberösterreich 100 € je kW bis 1.700 €. Die Steiermark nimmt "
        "für neue Wärmepumpen derzeit keine Förderanträge an. Bund und Land sind kombinierbar, in Kärnten "
        "zusammen bis 8.000 €*.",
        "„Sauber Heizen für Alle“ übernahm 2026 für Haushalte im unteren Einkommensdrittel bis zu 100 % der "
        "Kosten (Obergrenze 25.586 € Luft-Wasser, 37.550 € Sole-Wasser). Das Programm bleibt geschlossen, "
        "Registrierte können noch beantragen.",
        "Die Öko-Sonderausgabenpauschale bringt zusätzlich fünf Jahre lang 400 € Sonderausgaben, wenn eine "
        "Bundesförderung ausbezahlt wurde und nach Förderabzug mehr als 2.000 € Restkosten bleiben.",
        "Betriebe, Vereine und Gemeinden erhalten bis zu 7.500 € (unter 50 kW) oder 12.000 € (50 bis 100 kW), "
        "maximal 50 % der Kosten (eigene KPC-Schiene, Stand prüfen). Für 2027 sind laut BMLUK 179 Mio. € für "
        "den Kesseltausch vorgesehen, die Förderhöhe soll gleich bleiben.",
    ],
    "kpis": [
        ("5.000 €", "Bundespauschale Wärmepumpe seit 2. November 2026"),
        ("31.12.2026", "Registrierungsschluss Bund (oder früheres Budgetende)"),
        ("8.000 €", "höchster Landeszuschuss (Wien)"),
        ("2.000 €", "Öko-Sonderausgabenpauschale (mit Bundesförderung)"),
    ],

    "sections": [
        ("Stand November 2026: Bund wieder offen, Länder laufen", "status", f"""
<p><b>Der Bund fördert den Heizungstausch wieder: Seit 2. November 2026 ist der Kesseltausch neu
aufgelegt, mit 5.000 Euro Pauschale für die Wärmepumpe. Registrierung und Antrag sind möglich, solange
Budget vorhanden ist, längstens bis 31. Dezember 2026</b> (Quelle: Informationsblatt der KPC, Version
10/2026). Die erste Aktion 2026 (bis 7.500 Euro) war im Herbst ausgeschöpft. „Sauber Heizen für Alle“
bleibt geschlossen. Daneben laufen Landesförderungen: Kärnten zahlt 2026 eine Pauschale von 3.000 Euro (plus
1.500 Euro bei Errichtung einer Solaranlage, plus 200 Euro für den hydraulischen Abgleich); ob das Budget
reicht, klären wir vor dem Angebot. Die Steiermark nimmt für neue Wärmepumpen derzeit keine Förderanträge
an (wohnbau.steiermark.at, Stand 10. Oktober 2026). Für 2027 sind laut BMLUK 179 Millionen Euro für den
Kesseltausch vorgesehen, die Förderhöhe soll sich laut Aktionsseite nicht ändern.</p>
{A.box_dark("Was das für Ihr Projekt heißt",
    "Wer neu plant, lässt jetzt die Energieberatung machen, holt ein Angebot ein und registriert bis "
    "31. Dezember 2026, bevor das Budget aufgebraucht ist. Danach bleiben 9 Monate für Umsetzung und Antrag. "
    "Die Landesförderung beantragen Sie zusätzlich. Bereits registrierte Haushalte (erste Aktion: 9 Monate ab "
    "Registrierung, Sauber Heizen für Alle: 12 Monate ab Zusage) setzen innerhalb ihrer Frist um. Mit der "
    "ausbezahlten Bundesförderung greift auch die Öko-Sonderausgabenpauschale.")}
"""),
        ("Wer wie viel bekommt: die vier Fördertöpfe", "ueberblick", f"""
<p>Der Umstieg von Öl, Gas, Kohle oder Strom auf eine {a('waermepumpe', 'Wärmepumpe')} wird aus
vier Richtungen unterstützt: vom Bund (Kesseltausch der Sanierungsoffensive), vom jeweiligen Bundesland,
über die Steuer (Öko-Sonderausgabenpauschale) und, bis zur Schließung 2026, für einkommensschwache
Haushalte durch das Sonderprogramm „Sauber Heizen für Alle“. Betriebe haben eine eigene Schiene. Die
Tabelle zeigt die Eckwerte, die Details folgen in den Abschnitten darunter. Bund: Stand November 2026;
Länder: Stand April 2026 (Kärnten und Steiermark: Oktober 2026).</p>
{A.table(
    ["Fördertopf", "Für wen", "Höhe", "Frist / Ablauf"],
    [
        ["Kesseltausch (Bund, Sanierungsoffensive)", "Privatpersonen mit Ein-, Zweifamilien- oder Reihenhaus",
         "5.000 €, mit Bohrbonus Erdwärme 10.000 €, Solarthermie +2.500 € (erste Aktion 2026: bis 7.500 €)",
         "Neuauflage seit 2.11.2026, Registrierung bis 31.12.2026 oder Budgetende; dann 9 Monate für Umsetzung und Antrag"],
        ["Landesförderungen", "je nach Bundesland Eigentümer, teils auch Mieter",
         "z. B. Wien 35 % bis 8.000 €, Salzburg rund 5.000 €, OÖ 100 €/kW bis 1.700 €",
         "eigene Portale, teils vor, teils nach Umsetzung"],
        ["Sauber Heizen für Alle", "Haushalte im unteren Einkommensdrittel mit Hauptwohnsitz",
         "bis 100 % der Kosten, Obergrenze 25.586 € (Luft-Wasser) bzw. 37.550 € (Sole-Wasser) (galt 2026)",
         "geschlossen, keine neuen Registrierungen; Registrierte können noch beantragen"],
        ["Öko-Sonderausgabenpauschale", "Private mit ausbezahlter Bundesförderung (z. B. Kesseltausch)",
         "5 Jahre je 400 € Sonderausgaben (2.000 €)", "automatisch über die Steuerveranlagung"],
        ["Betriebsförderung (KPC)", "Unternehmen, Vereine, konfessionelle Einrichtungen",
         "bis 7.500 € (unter 50 kW), bis 12.000 € (50 bis 100 kW), max. 50 %",
         "Antrag bis 6 Monate nach Schlussrechnung"],
    ],
    hl_cols=(2,),
)}
"""),
        ("Bundesförderung Kesseltausch: seit 2. November 2026 neu aufgelegt", "bund", f"""
<p>Die {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive 2026')} ist das zentrale Programm der
Bundesregierung für den Heizungstausch. Der Kesseltausch richtet sich an Privatpersonen mit Ein- und
Zweifamilienhäusern sowie Reihenhäusern, die eine bestehende Öl-, Gas-, Kohle- oder Elektroheizung
vollständig durch eine Wärmepumpe ersetzen, ohne Einkommensprüfung. Gefördert werden Material, Montage,
Planung und die fachgerechte Entsorgung der Altanlage.</p>
<ul>
  <li><b>Förderhöhe (Neuauflage):</b> 5.000 € Pauschale für die Wärmepumpe. Für Erdwärme (Sole-Wasser
  oder Wasser-Wasser mit neuer Tiefenbohrung oder neuem Brunnen) kommt ein Bohrbonus von 5.000 € dazu,
  für eine thermische Solaranlage ab 6 m² weitere 2.500 € (Photovoltaik zählt nicht). Die frühere Grenze
  von 30 % der Kosten entfällt. Bei Luft-Wasser-Wärmepumpen mit Kältemittel-GWP 150 bis 750 sinkt die
  Förderung um 20 %. In der ersten Aktion 2026 waren es bis zu 7.500 €.</li>
  <li><b>Voraussetzungen:</b> EHPA-Gütesiegel, Kältemittel mit GWP-Wert von höchstens 750, maximale
  Vorlauftemperatur 55 °C, unter 100 kW, Installation durch eine befugte Fachkraft. Fernwärme hat Vorrang.
  Vor der Registrierung ist eine Energieberatung Pflicht, deren Protokoll bei der Registrierung vorliegen
  muss.</li>
  <li><b>Ablauf:</b> Registrierung online auf sanierungsoffensive.gv.at, ab 2. November 2026 bis längstens
  31. Dezember 2026. Danach bleiben 9 Monate für Umsetzung und Antrag. Gefördert werden Leistungen ab
  7. Oktober 2026. Prüfung und Auszahlung übernimmt die Kommunalkredit Public Consulting (KPC).</li>
</ul>
{A.box("Stand 19. November 2026: Registrierungen werden angenommen, solange Budget vorhanden ist. Die "
       "Neuauflage wird laut BMLUK aus Mitteln finanziert, die durch Stornierungen und verfallene "
       "Registrierungen der ersten Aktion frei wurden. Wer in der ersten Aktion registriert ist, hält seine "
       "9-Monats-Frist für Umsetzung und Endabrechnung ein.", label="Status:")}
"""),
        ("Sauber Heizen für Alle: bis zu 100 % für einkommensschwache Haushalte (geschlossen)", "sauber-heizen", f"""
<p>Das Programm {a('/sauber-heizen-fuer-alle-2026/', '„Sauber Heizen für Alle“')} richtete sich an
Haushalte im unteren Einkommensdrittel und konnte bis zu 100 % der förderfähigen Kosten abdecken. Seit
Herbst 2026 werden keine neuen Registrierungen angenommen, daran ändert die Neuauflage des Kesseltauschs
nichts; Registrierte können noch beantragen. Laut BMLUK soll das Angebot für einkommensschwache Haushalte
künftig in die Sanierungsoffensive integriert werden. Der Kesseltausch selbst hat keine Einkommensprüfung.
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
Bundesförderung kombiniert werden können. Die Beträge unterscheiden sich deutlich, die Steiermark nimmt
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
<p>Rechenbeispiele mit der Bundespauschale der Neuauflage:* In Kärnten ergeben 5.000 € Bund plus
3.000 € Land zusammen bis 8.000 €. In Wien ergeben 5.000 € Bund plus 8.000 € Land bei 28.000 €
Projektkosten 13.000 € Gesamtförderung (rund 46 %). In Tirol kommen bei 30.000 € Projektkosten 25 %
Landeszuschuss (7.500 €), 3.000 € Bonus und 5.000 € Bund auf 15.500 € (rund 52 %). Dabei gilt immer: Die
Summe aller Förderungen darf die tatsächlichen Investitionskosten nicht übersteigen. Eine laufend
aktualisierte Übersicht führt der Verband Wärmepumpe Austria (Quelle unten).</p>
<p><small>*Beispielrechnungen: Bund laut Informationsblatt der KPC (Version 10/2026), Kärnten Stand Oktober
2026, Wien und Tirol Stand April 2026. Die tatsächliche Förderung hängt von Anlage, Kosten, Budget und den
Bedingungen der Förderstellen ab.</small></p>
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
senkt die Betriebskosten dauerhaft. Dafür gibt es zwei getrennte Fördertöpfe: den Kesseltausch der
Sanierungsoffensive für den Heizungstausch (seit 2. November 2026 neu aufgelegt, 5.000 € für die
Wärmepumpe) und den EAG-Investitionszuschuss für die PV-Anlage
(letzter Call lief vom 8. bis 22. Oktober 2026, derzeit nicht beantragbar; ab 2027 laut BMWET Systemförderung
mit Antrag nach Installation geplant, nicht beschlossen). Wie
beide Systeme technisch
zusammenspielen, lesen Sie im Ratgeber
{a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}. Wer die Investition
nicht auf einmal stemmen will, kann sie über eine {a('finanzierung', 'Finanzierung')} verteilen; die
Anlage gehört dabei ab dem ersten Tag Ihnen, die Förderungen bleiben voll erhalten.</p>
"""),
        ("Fazit: Was jetzt gilt", "fazit", f"""
<p>Bundesförderung, Landesförderung und Steuerbonus lassen sich kombinieren. Mit der Neuauflage zahlt der
Bund 5.000 € für die Wärmepumpe (in der ersten Aktion 2026 bis zu 7.500 €), bei Erdwärme mit Bohrung
10.000 €; in Kärnten kommen 3.000 € vom Land dazu, zusammen bis 8.000 €*. Das Bundesbudget wird nach
Reihenfolge der Registrierung vergeben, die Neuauflage läuft längstens bis 31. Dezember 2026. Wer umsteigen
will, holt jetzt Energieberatung und Angebot ein und registriert früh. Was eine Wärmepumpe kostet, zeigt
der Ratgeber {a('/kosten-einer-waermepumpe/', 'Kosten einer Wärmepumpe')}.</p>
{A.cta("Förderwege prüfen lassen",
       "Wir rechnen Bund und Land für Ihr Projekt durch, unterstützen bei Energieberatung, Registrierung und "
       "Landesantrag und begleiten Sie bis zur Endabrechnung.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Wärmepumpe und Förderung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Wärmepumpen und Photovoltaik in Kärnten und "
                 "der Steiermark, mit zertifizierten Fachkräften. Wir "
                 "analysieren Ihre Situation, prüfen Landes- und Gemeindeförderung und "
                 "übernehmen Unterlagen und fristgerechte Einreichung, von der Registrierung beim Bund bis zur "
                 "Endabrechnung."),
        "grid": [
            ("Persönliche Förderberatung", "Wir berechnen, welche Töpfe Sie kombinieren können."),
            ("Komplette Förderabwicklung", "Registrierung beim Bund, Landesantrag, Endabrechnung: alles aus einer Hand."),
            ("Förderkonforme Installation", "EHPA-Gütesiegel, GWP unter 750, Vorlauf 55 °C: wir planen passend."),
            ("Energieberatung organisiert", "Das verpflichtende Beratungsprotokoll kümmern wir uns mit."),
        ],
    },

    "faq": [
        ("Gibt es 2026 noch eine Bundesförderung für die Wärmepumpe?",
         "Ja. Seit 2. November 2026 ist der Kesseltausch neu aufgelegt: 5.000 € Pauschale für die Wärmepumpe, "
         "plus 5.000 € Bohrbonus bei Sole- oder Wasser-Wasser-Wärmepumpen und 2.500 € bei einer thermischen "
         "Solaranlage ab 6 m². Registrieren können Sie bis 31. Dezember 2026 oder bis das Budget aufgebraucht "
         "ist. „Sauber Heizen für Alle“ bleibt geschlossen."),
        ("Wer kann die Wärmepumpenförderung beantragen?",
         "Beim Kesseltausch des Bundes Privatpersonen, die als Eigentümer, Bauberechtigte oder Mieter in einem "
         "Ein-, Zweifamilien- oder Reihenhaus in Österreich eine fossile Heizung vollständig durch eine "
         "Wärmepumpe ersetzen, ohne Einkommensprüfung. Die Installation muss eine befugte Fachkraft durchführen. "
         "Für Wohnungen im mehrgeschossigen Wohnbau sowie für Betriebe und Vereine gibt es eigene "
         "Förderschienen."),
        ("Kann ich Bundes- und Landesförderung kombinieren?",
         "Ja, die Kombination ist möglich, wenn das Land sie zulässt. Zu den 5.000 € des Bundes kommen je nach "
         "Bundesland mehrere Tausend Euro dazu, in Kärnten 3.000 €, in Wien bis zu 8.000 €. Die Summe aller "
         "Förderungen darf die tatsächlichen Investitionskosten aber nie übersteigen."),
        ("Was kostet eine Wärmepumpe in Österreich insgesamt?",
         "Für eine Luft-Wasser-Wärmepumpe inklusive Installation sollten Sie mit rund 10.000 bis 18.000 € "
         "rechnen, für Erdwärmepumpen mit Bohrung eher mit 18.000 bis 25.000 € (Richtwerte, abhängig von "
         "Gebäude und System). Bund und Land senken den Eigenanteil deutlich, in Kärnten zum Beispiel um bis zu "
         "8.000 € bei einer Luft-Wasser-Wärmepumpe."),
        ("Muss ich die Förderung vor oder nach der Installation beantragen?",
         "Beim Kesseltausch gilt: zuerst Energieberatung, dann Online-Registrierung, die das Budget 9 Monate "
         "reserviert, danach Antrag mit Rechnungen. Registriert werden kann ein geplantes oder bereits "
         "umgesetztes Projekt, gefördert werden Leistungen ab 7. Oktober 2026; ohne Registrierung ist das Budget "
         "aber nicht reserviert. Bei „Sauber Heizen für Alle“ (geschlossen) waren Leistungen vor der "
         "Antragstellung nicht förderfähig. Betriebe stellen den Antrag nach Umsetzung, bis sechs Monate nach "
         "der Schlussrechnung."),
        ("Was passiert, wenn das Förderbudget aufgebraucht ist?",
         "Dann werden keine neuen Registrierungen mehr angenommen, auch vor dem offiziellen Enddatum. Genau das "
         "ist 2026 in der ersten Aktion passiert, die im Herbst ausgeschöpft war. Die Neuauflage seit "
         "2. November 2026 wird laut BMLUK aus frei gewordenen Mitteln finanziert und läuft längstens bis "
         "31. Dezember 2026. Den aktuellen Stand zeigt sanierungsoffensive.gv.at."),
        ("Wie hoch ist die Förderung für eine Erdwärme-Wärmepumpe?",
         "Zur Pauschale von 5.000 € kommt bei Sole-Wasser- oder Wasser-Wasser-Wärmepumpen mit neuer "
         "Tiefenbohrung oder neuem Brunnen ein Bohrbonus von 5.000 €, in Summe bis zu 10.000 € vom Bund, ohne "
         "Prozentgrenze. In der ersten Aktion 2026 waren es bis zu 12.500 €, gedeckelt mit 30 % der Kosten."),
        ("Gibt es zusätzlich einen Steuervorteil?",
         "Ja. Wurde eine Bundesförderung ausbezahlt und bleiben nach Abzug aller Förderungen mehr als 2.000 € "
         "Restkosten, werden fünf Jahre lang je "
         "400 € automatisch als Sonderausgaben berücksichtigt (Öko-Sonderausgabenpauschale). Bei 42 % "
         "Grenzsteuersatz entspricht das rund 840 € Steuerersparnis über fünf Jahre."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert "
                    "Wärmepumpen und Photovoltaik in Kärnten und der Steiermark und übernimmt die komplette "
                    "Förderabwicklung. Bund: Neuauflage Kesseltausch laut Informationsblatt der KPC (Version "
                    "10/2026), geprüft am 19. November 2026; Länder: Stand April 2026 (Kärnten und Steiermark: "
                    "Stand 10. Oktober 2026). Keine Rechts- "
                    "oder Steuerberatung, maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("KPC: Informationsblatt Kesseltausch 2026 Ein-/Zweifamilienhaus/Reihenhaus, Neuauflage ab 2.11.2026 (Version 10/2026)",
         "https://www.sanierungsoffensive.gv.at/fileadmin/user_upload/2026/Infoblatt_Neuauflage_Kesseltausch_2026_EFH.pdf"),
        ("Sanierungsoffensive: Aktionsseite Kesseltausch Neuauflage Ein-/Zweifamilienhaus oder Reihenhaus",
         "https://www.sanierungsoffensive.gv.at/kesseltausch/neuauflage-ein-/zweifamilienhaus-oder-reihenhaus"),
        ("BMLUK: Sanierung und Kesseltausch 2027",
         "https://www.bmluk.gv.at/themen/klima-und-umwelt/klima/klima-initiativen-und-foerderungen/ufg/sanierung-kesselaustausch-2027.html"),
        ("Sauber Heizen für Alle (Bundesportal)", "https://www.sauber-heizen.at/"),
        ("Verband Wärmepumpe Austria: Förderübersicht", "https://www.waermepumpe-austria.at/foerderungen"),
        ("Land Steiermark: Förderung für Heizungen (Wohnbau, Stand 10. Oktober 2026)",
         "https://www.wohnbau.steiermark.at/cms/ziel/164947118/DE/"),
    ],
    "related": [
        ("/sanierungsoffensive-2026/", "Sanierungsoffensive 2026: Kesseltausch neu, 5.000 €"),
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
