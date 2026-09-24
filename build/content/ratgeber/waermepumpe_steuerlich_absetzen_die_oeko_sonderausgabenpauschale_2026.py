"""Ratgeber: Wärmepumpe steuerlich absetzen, Öko-Sonderausgabenpauschale 2026.

Migriert vom WordPress-Artikel
ebz-photovoltaik.at/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/
(veröffentlicht 2026-03-20, zuletzt geändert 2026-04-12). Zahlen: Stand April 2026.
Bereinigt: Gedankenstriche, falsche FAQ-Überschrift ("Sauber Heizen für Alle", Copy-Paste-Rest),
Widerspruch "2.000 € Steuerersparnis" vs. "2.000 € Sonderausgaben, real ca. 840 €" aufgelöst
(einheitlich: 2.000 € Sonderausgaben, Steuerersparnis abhängig vom Steuersatz).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026",
    "path": "/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/",
    "title": "Wärmepumpe steuerlich absetzen: Öko-Pauschale 2026 | EBZ",
    "description": ("Öko-Sonderausgabenpauschale 2026: 5 Jahre je 400 € Sonderausgaben für den Heizungstausch, "
                    "automatisch über die KPC. Voraussetzungen und Rechenbeispiel."),
    "eyebrow": "Steuer · Wärmepumpe",
    "crumb_label": "Öko-Sonderausgabenpauschale 2026",
    "h1": "Wärmepumpe steuerlich absetzen: Die Öko-Sonderausgabenpauschale 2026 bringt 5 Jahre lang 400 €",
    "lead": ("Wer seine fossile Heizung mit Bundesförderung durch eine Wärmepumpe ersetzt, kann zusätzlich fünf "
             "Jahre lang je 400 € als Sonderausgaben absetzen, ohne eigenen Antrag beim Finanzamt. Dieser "
             "Ratgeber erklärt Voraussetzungen, Höhe, Ablauf und was die Pauschale unter dem Strich bringt."),
    "chips": [
        "Heizungstausch: <b>5 x 400 €</b>",
        "Sanierung: <b>5 x 800 €</b>",
        "Restkosten über <b>2.000 €</b>",
        "Berücksichtigung <b>automatisch</b>",
    ],
    "date_published": "2026-03-20",
    "date_modified": "2026-09-24",
    "hero_img": "foerderung",
    "hero_alt": "Unterlagen und Taschenrechner für die Steuerveranlagung nach dem Heizungstausch",

    "tldr": [
        "Die Öko-Sonderausgabenpauschale (§ 18 Abs. 1 Z 10 EStG) gilt seit der Ökosozialen Steuerreform 2022 "
        "für den Heizungstausch und die thermische Sanierung privat genutzter Wohngebäude.",
        "Höhe: 400 € pro Jahr über 5 Jahre (2.000 €) beim Heizungstausch, 800 € pro Jahr über 5 Jahre "
        "(4.000 €) bei thermischer Sanierung. Bei zwei Maßnahmen verlängert sich der Zeitraum auf 10 Jahre.",
        "Die Beträge werden vom steuerpflichtigen Einkommen abgezogen. Bei 42 % Grenzsteuersatz sind das rund "
        "168 € pro Jahr, also etwa 840 € Steuerersparnis über fünf Jahre.",
        "Voraussetzungen: ausbezahlte Bundesförderung nach dem Umweltförderungsgesetz (Sanierungsoffensive oder "
        "Sauber Heizen für Alle), Restkosten nach Förderabzug über 2.000 € (Sanierung: über 4.000 €), privat "
        "genutztes Gebäude, natürliche Person.",
        "Ablauf: Zustimmung zur Datenübermittlung im KPC-Förderantrag, dann übermittelt die KPC die Daten ans "
        "Finanzamt. Sie müssen nur jährlich die Arbeitnehmerveranlagung durchführen. Vergessene Zustimmung "
        "lässt sich per KPC-Formular nachholen.",
    ],
    "kpis": [
        ("400 €", "Sonderausgaben pro Jahr"),
        ("5 Jahre", "Berücksichtigungszeitraum"),
        ("2.000 €", "Mindest-Restkosten nach Förderung"),
        ("ca. 840 €", "Steuerersparnis bei 42 % Steuersatz"),
    ],

    "sections": [
        ("Was ist die Öko-Sonderausgabenpauschale?", "was-ist", f"""
<p>Mit der Ökosozialen Steuerreform 2022 hat der Gesetzgeber eine steuerliche Begünstigung für
klimafreundliche Investitionen in privat genutzten Wohngebäuden eingeführt. Die Öko-Sonderausgabenpauschale
(§ 18 Abs. 1 Z 10 EStG 1988) erlaubt Privatpersonen, die Kosten für den Heizungstausch oder eine
thermische Gebäudesanierung als Sonderausgaben in der Einkommensteuererklärung bzw.
Arbeitnehmerveranlagung geltend zu machen. Das geschieht nicht über den Nachweis der tatsächlichen
Kosten, sondern über einen festen Pauschalbetrag, daher der Name.</p>
<p>Das Besondere: Sind die Voraussetzungen erfüllt, wird die Pauschale automatisch in der
Steuerveranlagung berücksichtigt, ohne zusätzlichen Antrag beim Finanzamt. Sie ergänzt die direkten
Zuschüsse aus der {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive 2026')} und den
{a('/landesfoerderungen-fuer-die-waermepumpe/', 'Landesförderungen')}. Stand: April 2026.</p>
"""),
        ("Wie hoch ist die Pauschale?", "hoehe", f"""
{A.table(
    ["Maßnahme", "Pauschale pro Jahr", "Zeitraum", "Summe Sonderausgaben"],
    [
        ["Heizungstausch (Kesseltausch), z. B. Wärmepumpe", "400 €", "5 Jahre", "2.000 €"],
        ["Thermisch-energetische Sanierung (Dämmung, Fenster)", "800 €", "5 Jahre", "4.000 €"],
        ["Beide Maßnahmen innerhalb von 5 Jahren", "400 € bzw. 800 €", "10 Jahre", "6.000 €"],
    ],
    hl_cols=(1, 3),
)}
<p>Wichtig ist der Unterschied zwischen Sonderausgaben und Steuerersparnis: Die 400 € werden vom
steuerpflichtigen Einkommen abgezogen. Was Sie tatsächlich sparen, hängt vom persönlichen
Grenzsteuersatz ab. Bei 42 % sind das rund 168 € pro Jahr bzw. rund 840 € über fünf Jahre.</p>
<h3>Verlängerung auf 10 Jahre bei Kombination</h3>
<p>Tätigen Sie innerhalb des fünfjährigen Zeitraums eine zweite begünstigte Investition, verlängert
sich der Zeitraum auf 10 Jahre. Beispiel: Sie tauschen 2026 die Heizung (400 €/Jahr) und dämmen 2028
zusätzlich (800 €/Jahr). Dann werden 2026 bis 2030 je 400 € berücksichtigt und 2031 bis 2035 je 800 €,
in Summe 6.000 € Sonderausgaben über 10 Jahre. Erfolgen beide Maßnahmen im selben Jahr, werden zuerst
5 Jahre lang 800 € und anschließend 5 Jahre lang 400 € berücksichtigt.</p>
"""),
        ("Welche Voraussetzungen müssen erfüllt sein?", "voraussetzungen", f"""
<ul>
  <li><b>Bundesförderung als Grundvoraussetzung:</b> Für den Heizungstausch muss eine Bundesförderung
  nach dem Umweltförderungsgesetz gewährt und ausbezahlt worden sein, also über die Sanierungsoffensive
  2026 (Kesseltausch) oder {a('/sauber-heizen-fuer-alle-2026/', '„Sauber Heizen für Alle“')}. Reine
  Landes- oder Gemeindeförderungen reichen nicht.</li>
  <li><b>Mindest-Restkosten:</b> Nach Abzug aller ausbezahlten öffentlichen Förderungen (Bund, Land,
  Gemeinde) müssen beim Heizungstausch mehr als 2.000 € Restkosten bleiben, bei thermischer Sanierung
  mehr als 4.000 €. Beim Heizungstausch ist diese Schwelle in der Praxis fast immer überschritten.</li>
  <li><b>Privat genutztes Gebäude:</b> Ein- und Zweifamilienhäuser, Reihenhäuser und private Wohnungen.
  Betrieblich genutzte oder vermietete Gebäude sind ausgeschlossen; bei gemischter Nutzung gilt die
  Pauschale nur für den privaten Anteil.</li>
  <li><b>Natürliche Personen:</b> Anspruchsberechtigt ist, wer die Förderung empfangen hat. Bei
  Wohnungseigentumsgemeinschaften ist jede Eigentümerin und jeder Eigentümer anteilig berechtigt.</li>
  <li><b>Zeitliche Geltung:</b> erstmals für das Veranlagungsjahr 2022, sofern das Förderansuchen nach dem
  31. März 2022 eingebracht und die Förderung nach dem 30. Juni 2022 ausbezahlt wurde. Für den
  Kesseltausch 2026 ist das erfüllt.</li>
</ul>
"""),
        ("So machen Sie die Pauschale geltend", "ablauf", f"""
{A.steps([
    ("Zustimmung im Förderantrag erteilen",
     "Im Online-Antrag bei der Kommunalkredit Public Consulting (KPC) werden Sie gefragt, ob Sie die "
     "Öko-Sonderausgabenpauschale nutzen möchten, und erklären Ihr Einverständnis zur Datenübermittlung an "
     "das Finanzamt. Ohne dieses Häkchen entfällt die automatische Berücksichtigung."),
    ("Automatische Übermittlung abwarten",
     "Nach Auszahlung der Bundesförderung übermittelt die KPC die Daten an das Finanzamt. Ab dem "
     "Veranlagungsjahr der Auszahlung wird die Pauschale 5 Jahre lang automatisch berücksichtigt."),
    ("Arbeitnehmerveranlagung durchführen",
     "Damit die Pauschale wirkt, führen Sie jährlich Ihre Arbeitnehmerveranlagung (Lohnsteuerausgleich) über "
     "FinanzOnline durch. Die Pauschale fließt automatisch in die Berechnung ein."),
])}
<p><b>Beispiel:</b> Die Bundesförderung wird im September 2026 ausbezahlt. Dann wird die Pauschale
erstmals bei der Veranlagung für 2026 berücksichtigt, die Sie Anfang 2027 durchführen. Es folgen die
Jahre 2027, 2028, 2029 und 2030, insgesamt 5 Jahre zu je 400 €.</p>
{A.box_dark("Zustimmung vergessen? Nachholen ist möglich",
    "Wurde die Zustimmung zur Datenübermittlung im Antrag nicht erteilt, stellt die KPC Bestätigungsformulare "
    "bereit. Ausgefüllt per E-Mail an klimaschutz@publicconsulting.at senden; nach Prüfung werden die Daten "
    "nachträglich übermittelt und die Pauschale ab dem nächsten Veranlagungsjahr berücksichtigt. Formulare: "
    "umweltfoerderung.at/oeko-sonderausgabenpauschale.")}
{A.cta("Förderung und Steuerbonus in einem Zug",
       "Wenn EBZ Energie die Förderabwicklung übernimmt, setzen wir die Zustimmung zur Datenübermittlung "
       "standardmäßig. So geht der Steuerbonus nicht verloren.",
       secondary=("waermepumpe", "Zur Wärmepumpen-Leistungsseite"))}
"""),
        ("Rechenbeispiel: Was bringt die Pauschale konkret?", "rechenbeispiel", f"""
<p>Sie tauschen Ihre Ölheizung gegen eine Luft-Wasser-Wärmepumpe. Die Gesamtkosten betragen 22.000 €.*</p>
{A.table(
    ["Position", "Betrag"],
    [
        ["Gesamtkosten Heizungstausch", "22.000 €"],
        ["Bundesförderung Kesseltausch (30 % der förderfähigen Kosten)", "6.600 €"],
        ["Landesförderung (z. B. Kärnten)", "3.000 €"],
        ["Verbleibende Restkosten (22.000 minus 6.600 minus 3.000)", "12.400 €"],
        ["Öko-Sonderausgabenpauschale: 5 x 400 € Sonderausgaben", "2.000 €"],
        ["Steuerersparnis bei 42 % Grenzsteuersatz (5 x ca. 168 €)", "ca. 840 €"],
        ["Gesamtvorteil aus Förderung und Steuer", "ca. 10.440 €"],
    ],
    hl_cols=(1,),
)}
<p>Die Restkosten von 12.400 € übersteigen die Mindestgrenze von 2.000 € deutlich, die Bundesförderung
wurde ausbezahlt, das Gebäude wird privat genutzt: Alle Voraussetzungen sind erfüllt. Die Pauschale ist
damit kein großer Hebel, aber ein Bonus, den Sie ohne Aufwand mitnehmen. Was eine Wärmepumpe insgesamt
kostet, zeigt der Ratgeber {a('/kosten-einer-waermepumpe/', 'Kosten einer Wärmepumpe')}.</p>
<p><small>*Beispielrechnung mit Richtwerten, Stand April 2026. Bundesförderung gedeckelt bei 30 % der
förderfähigen Kosten, Landesförderung je nach Bundesland unterschiedlich, Steuerersparnis abhängig vom
persönlichen Grenzsteuersatz.</small></p>
"""),
        ("Was die Pauschale nicht abdeckt", "grenzen", f"""
<ul>
  <li><b>Kein Ersatz für die Förderung:</b> Die Pauschale ergänzt Bundes- und Landesförderung. Ohne
  ausbezahlte Bundesförderung gibt es keine steuerliche Begünstigung.</li>
  <li><b>Keine Absetzung für vermietete Objekte:</b> Vermieter können die Pauschale nicht nutzen. Für
  betrieblich genutzte Gebäude gibt es andere Wege, etwa die Abschreibung als Betriebsausgabe.</li>
  <li><b>Kein Wahlrecht bei der Höhe:</b> 400 € bzw. 800 € pro Jahr sind fix. Die tatsächlichen Kosten
  spielen keine Rolle, solange die Mindestgrenze überschritten ist.</li>
  <li><b>Keine Photovoltaik:</b> Die Pauschale gilt nur für Heizungstausch und thermische Sanierung. Die
  {a('photovoltaik', 'PV-Anlage')} wird über den EAG-Investitionszuschuss gefördert.</li>
  <li><b>Kein Anspruch ohne Zustimmung:</b> Ohne Datenübermittlung an das Finanzamt keine automatische
  Berücksichtigung; nachholen über das KPC-Bestätigungsformular.</li>
</ul>
"""),
        ("Wärmepumpe und Photovoltaik: dreifach profitieren", "photovoltaik", f"""
<p>Wer die Wärmepumpe mit einer PV-Anlage kombiniert, nutzt drei Vorteile: die Bundesförderung für den
Heizungstausch, die Öko-Sonderausgabenpauschale für die Steuer und den EAG-Investitionszuschuss für die
Photovoltaik. Dazu senkt der selbst erzeugte Strom die laufenden Betriebskosten der Wärmepumpe. Wie das
zusammenspielt, lesen Sie im Ratgeber
{a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}; einen Überblick über alle
Zuschüsse gibt {a('/waermepumpenfoerderung-in-oesterreich/', 'Wärmepumpenförderung in Österreich 2026')}.
Für das Gesamtpaket bietet EBZ Energie eine {a('finanzierung', 'Finanzierung')} an, die Anlage gehört
dabei ab Tag 1 Ihnen und die Förderungen bleiben voll erhalten.</p>
{A.cta("Gesamtersparnis vorrechnen lassen",
       "Wir berechnen Ihren Vorteil aus Bundesförderung, Landesförderung und Steuerpauschale und erledigen "
       "Registrierung, Antrag und Abrechnung mit den richtigen Einstellungen.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Förderung und Steuerbonus: EBZ Energie denkt an alles",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("Viele Hausbesitzer wissen nicht, dass ihnen die Öko-Sonderausgabenpauschale zusteht, oder "
                 "vergessen das Häkchen im Förderantrag. Wenn EBZ Energie aus Villach Ihre Wärmepumpe installiert "
                 "und die Förderabwicklung übernimmt, achten wir darauf, dass die Zustimmung zur "
                 "Datenübermittlung erteilt wird. Unser festangestelltes Team aus zertifizierten Fachkräften "
                 "montiert in Kärnten und der Steiermark."),
        "grid": [
            ("Persönliche Förderberatung", "Gesamtersparnis aus Bund, Land und Steuervorteil in einer Rechnung."),
            ("Komplette Abwicklung", "Registrierung, Antrag, Installation, Abrechnung, inklusive Pauschale."),
            ("Wärmepumpe + PV als Paket", "Zwei Fördertöpfe, ein Steuerbonus, minimale Energiekosten."),
            ("Erfahrung aus 300+ Projekten", "Wir kennen die Abläufe bei KPC und Landesstellen."),
        ],
    },

    "faq": [
        ("Muss ich die Pauschale jedes Jahr neu beantragen?",
         "Nein. Haben Sie im Förderantrag der Datenübermittlung zugestimmt, wird die Pauschale fünf Jahre lang "
         "automatisch in der Arbeitnehmerveranlagung berücksichtigt. Sie müssen nur jährlich die Veranlagung "
         "durchführen, was sich für die meisten Arbeitnehmer ohnehin lohnt."),
        ("Gilt die Pauschale auch für Wärmepumpen in Neubauten?",
         "In den meisten Fällen nicht. Die Pauschale setzt eine Bundesförderung nach dem Umweltförderungsgesetz "
         "voraus, und die Sanierungsoffensive 2026 fördert den Austausch fossiler Heizungen im Bestand. "
         "Ausnahmen sind denkbar, wenn eine andere Bundesförderung greift."),
        ("Kann ich die Pauschale nutzen, wenn ich „Sauber Heizen für Alle“ erhalten habe?",
         "Grundsätzlich ja, sofern nach Abzug aller Förderungen mehr als 2.000 € Restkosten bleiben. Da "
         "„Sauber Heizen für Alle“ bis zu 100 % der Kosten abdecken kann, bleibt oft kein ausreichender "
         "Eigenanteil; dann entfällt der Anspruch."),
        ("Was passiert, wenn ich die Zustimmung bei der Antragstellung vergessen habe?",
         "Sie können sie nachträglich erteilen. Die KPC stellt Bestätigungsformulare bereit, die Sie ausgefüllt "
         "per E-Mail an klimaschutz@publicconsulting.at senden. Die Daten werden dann nachgereicht und die "
         "Pauschale ab der nächsten Veranlagung berücksichtigt."),
        ("Kann ich die Öko-Sonderausgabenpauschale mit anderen Steuerbegünstigungen kombinieren?",
         "Ja. Die Pauschale wird unabhängig von anderen Sonderausgaben wie Kirchenbeitrag oder Spenden "
         "berücksichtigt und senkt die Bemessungsgrundlage zusätzlich. Auch die Kombination mit Bundes-, "
         "Landes- und Gemeindeförderung ist zulässig, die Pauschale ist als Ergänzung dazu konzipiert."),
        ("Wie viel Steuer spare ich wirklich?",
         "Die 400 € pro Jahr sind Sonderausgaben, keine Steuergutschrift. Bei 42 % Grenzsteuersatz sparen Sie "
         "rund 168 € pro Jahr, über fünf Jahre etwa 840 €. Bei einem niedrigeren Steuersatz entsprechend "
         "weniger, bei einem höheren mehr."),
        ("Reicht eine Landesförderung allein für die Pauschale?",
         "Nein. Auslöser ist ausschließlich eine gewährte und ausbezahlte Bundesförderung nach dem "
         "Umweltförderungsgesetz. Landes- oder Gemeindeförderungen allein begründen keinen Anspruch, werden "
         "aber bei der Berechnung der Restkosten (über 2.000 €) abgezogen."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team installiert Wärmepumpen und "
                    "Photovoltaik in Kärnten und der Steiermark und übernimmt die Förderabwicklung inklusive der "
                    "Zustimmung zur Öko-Sonderausgabenpauschale. Alle Angaben entsprechen dem Stand April 2026 und "
                    "dem Einkommensteuergesetz. Keine Rechts- oder Steuerberatung, maßgeblich sind die offiziellen "
                    "Förderbedingungen und die Bestimmungen des Bundesministeriums für Finanzen; bei individuellen "
                    "Fragen wenden Sie sich an Ihre Steuerberatung."),
    "sources": [
        ("Umweltförderung (KPC): Öko-Sonderausgabenpauschale und Bestätigungsformulare",
         "https://www.umweltfoerderung.at/oeko-sonderausgabenpauschale"),
        ("Bundesministerium für Finanzen: Öko-Sonderausgabenpauschale",
         "https://www.bmf.gv.at/oeko-sonderausgabenpauschale"),
    ],
    "related": [
        ("/waermepumpenfoerderung-in-oesterreich/", "Wärmepumpenförderung Österreich 2026: Überblick"),
        ("/sanierungsoffensive-2026/", "Sanierungsoffensive 2026: Bundesförderung"),
        ("/kosten-einer-waermepumpe/", "Kosten einer Wärmepumpe"),
        ("waermepumpe", "Wärmepumpen-Installateur EBZ Energie"),
    ],
    "cta": {
        "h3": "Steuerbonus mitnehmen",
        "text": "Wir setzen im Förderantrag die richtigen Einstellungen, damit die Pauschale automatisch läuft.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Förderung, Steuerbonus und Wärmepumpe aus einer Hand",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
