"""Ratgeber: Sauber Heizen für Alle 2026 (bis zu 100 % Förderung für einkommensschwache Haushalte).

Stand Oktober 2026: Programm BEENDET, keine neuen Registrierungen (umweltfoerderung.at, 9.10.2026);
bereits Registrierte koennen noch beantragen. Konditionen als "galt 2026" dokumentiert, Status-Box oben.
Update 19.11.2026: Programm bleibt geschlossen; Verweise auf den regulären Kesseltausch auf die Neuauflage
ab 2.11.2026 umgestellt (5.000 € Wärmepumpe, keine Einkommensprüfung, Registrierung bis 31.12.2026).

Migriert vom WordPress-Artikel ebz-photovoltaik.at/sauber-heizen-fuer-alle-2026/
(veröffentlicht 2026-03-15, zuletzt geändert 2026-04-12). Zahlen: Stand April 2026.
Bereinigt: Gedankenstriche, "ohne Subunternehmer" entfernt, "Fachbetrieb in ganz Österreich"
auf Kärnten + Steiermark korrigiert, Einkommensgrenzen und Programmvergleich als Tabellen.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "sauber-heizen-fuer-alle-2026",
    "path": "/sauber-heizen-fuer-alle-2026/",
    "title": "Sauber Heizen für Alle 2026: beendet, das gilt jetzt | EBZ",
    "description": ("Sauber Heizen für Alle 2026: keine neuen Registrierungen. Was für Registrierte gilt und "
                    "welche Alternativen bleiben, etwa der Kesseltausch (seit 2.11.2026, 5.000 €)."),
    "eyebrow": "Förderung · Einkommensschwache Haushalte",
    "crumb_label": "Sauber Heizen für Alle 2026",
    "h1": "Sauber Heizen für Alle 2026: Programm beendet. Was für Registrierte gilt und welche Alternativen bleiben",
    "lead": ("Stand Oktober 2026: „Sauber Heizen für Alle 2026“ nimmt keine neuen Registrierungen mehr an. Wer "
             "registriert ist, kann noch beantragen und bis zu 100 % der Kosten bis zur Obergrenze von 25.586 € "
             "(Luft-Wasser) bzw. 37.550 € (Sole-Wasser) erhalten. Seit 2. November 2026 läuft der reguläre "
             "Kesseltausch wieder (5.000 € für die Wärmepumpe, ohne Einkommensprüfung). Hier lesen Sie, was jetzt "
             "gilt, welche Konditionen 2026 galten und welche Förderwege offen bleiben."),
    "chips": [
        "Status: <b>beendet</b> (Stand Oktober 2026)",
        "Registrierte: <b>Antrag weiter möglich</b>",
        "Galt 2026: <b>bis 100 %</b> Förderung",
        "Obergrenze Luft-Wasser: <b>25.586 €</b>",
    ],
    "date_published": "2026-03-15",
    "date_modified": "2026-11-19",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit neuer Wärmepumpe und Photovoltaik nach dem Heizungstausch",

    "tldr": [
        "Stand Oktober 2026: „Sauber Heizen für Alle 2026“ ist beendet, neue Registrierungen sind nicht mehr "
        "möglich. Bereits registrierte Haushalte können noch beantragen (Quelle: umweltfoerderung.at).",
        "Was 2026 galt: Das Programm des Bundes (BMLUK) gemeinsam mit den Bundesländern ergänzte Bundes- und "
        "Landesförderung so, dass bis zu 100 % der förderfähigen Kosten abgedeckt waren.",
        "Kostenobergrenzen: 25.586 € für Luft-Wasser-Wärmepumpen, 37.550 € für Sole-Wasser- und "
        "Wasser-Wasser-Systeme. Liegen Ihre Kosten darunter, bleibt kein Eigenanteil.",
        "Voraussetzungen: Eigentum an einem Ein-, Zweifamilien- oder Reihenhaus, Hauptwohnsitz am Standort "
        "(begründet vor 31. Dezember 2024), Haushaltseinkommen im unteren Einkommensdrittel.",
        "Einkommensgrenze: 1.867 € netto pro Monat für eine Person, rund 2.801 € für zwei Erwachsene, "
        "rund 3.361 € mit einem Kind, rund 3.921 € mit zwei Kindern.",
        "Ablauf für Registrierte: kostenlose Energieberatung durch die Landesstelle, Antrag auf sauber-heizen.at, "
        "dann 12 Monate für Umsetzung und Endabrechnung. Leistungen vor der Antragstellung sind nicht förderfähig. "
        "Für alle anderen: der Kesseltausch des Bundes, seit 2. November 2026 neu aufgelegt (5.000 € für die "
        "Wärmepumpe, ohne Einkommensprüfung, Registrierung bis 31. Dezember 2026), plus Landesförderung. Laut "
        "BMLUK soll das Angebot für einkommensschwache Haushalte künftig in die Sanierungsoffensive integriert "
        "werden.",
    ],
    "kpis": [
        ("beendet", "Stand Oktober 2026: keine neuen Registrierungen"),
        ("100 %", "maximale Kostenübernahme (galt 2026)"),
        ("25.586 €", "Obergrenze Luft-Wasser-WP"),
        ("12 Monate", "Umsetzungsfrist ab Zusage für Registrierte"),
    ],

    "sections": [
        ("Stand Oktober 2026: Programm beendet, keine neuen Registrierungen", "status", f"""
{A.box_dark("Sauber Heizen für Alle 2026: Registrierung geschlossen",
    "Laut umweltfoerderung.at ist „Sauber Heizen für Alle 2026“ beendet, neue Registrierungen sind nicht mehr "
    "möglich (Stand 9. Oktober 2026). Wer bereits registriert ist, kann den Antrag noch stellen und das Projekt "
    "innerhalb der Fristen umsetzen. Die reguläre Kesseltausch-Förderung der Sanierungsoffensive läuft dagegen "
    "seit 2. November 2026 als Neuauflage wieder.")}
<p>Was offen ist: der {a('/sanierungsoffensive-2026/', 'Kesseltausch des Bundes')} mit 5.000 € Pauschale
für die Wärmepumpe (plus 5.000 € Bohrbonus bei Erdwärme, plus 2.500 € bei einer thermischen Solaranlage),
ohne Einkommensprüfung; Registrierung bis 31. Dezember 2026 oder bis das Budget aufgebraucht ist. Er deckt
nicht die gesamten Kosten, ist aber mit der Landesförderung kombinierbar: in Kärnten mit der Landespauschale
von 3.000 € für die Wärmepumpe (ob das Budget reicht, klären wir vor dem Angebot). Die Steiermark nimmt für
neue Wärmepumpen derzeit keine Förderanträge an (wohnbau.steiermark.at, Stand 10. Oktober 2026). Die
steuerliche
{a('/waermepumpe-steuerlich-absetzen-die-oeko-sonderausgabenpauschale-2026/', 'Öko-Sonderausgabenpauschale')}
setzt eine ausbezahlte Bundesförderung voraus, also auch den Kesseltausch. Laut BMLUK soll das Angebot für
einkommensschwache Haushalte künftig in die Sanierungsoffensive integriert werden; Details gibt es noch
nicht. Die folgenden Abschnitte beschreiben die Konditionen, die 2026 galten, und bleiben für bereits
registrierte Haushalte relevant.</p>
"""),
        ("Warum es „Sauber Heizen für Alle“ gibt", "hintergrund", f"""
<p>Die reguläre Bundesförderung über die {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive 2026')}
zahlte in der ersten Aktion 2026 bis zu 7.500 € für eine Wärmepumpe, in der Neuauflage seit
2. November 2026 sind es 5.000 €. Für Haushalte mit geringem
Einkommen blieb danach ein Eigenanteil, der oft nicht tragbar ist. Genau hier setzte „Sauber Heizen für
Alle“ an. Das Programm wurde
vom Bundesministerium für Land- und Forstwirtschaft, Klima- und Umweltschutz, Regionen und
Wasserwirtschaft (BMLUK) ins Leben gerufen und wird gemeinsam mit den Bundesländern umgesetzt.</p>
<p>Die Förderung wird als einmaliger Investitionszuschuss in Ergänzung zur Basisförderung des Bundes und
zur jeweiligen Landesförderung vergeben. Im Idealfall decken die drei Bausteine zusammen bis zu 100 %
der förderfähigen Kosten ab: eine neue {a('waermepumpe', 'Wärmepumpe')} ohne Eigenanteil.
Konditionen: Stand April 2026; Programmstatus: Stand Oktober 2026.</p>
"""),
        ("Was wird gefördert?", "was-wird-gefoerdert", f"""
<h3>Förderfähige Heizsysteme</h3>
<p>Vorrang hat der Anschluss an ein klimafreundliches oder hocheffizientes Nah- oder Fernwärmenetz. Ist
das technisch nicht möglich oder wirtschaftlich nicht zumutbar, wird der Umstieg auf eine dieser
Alternativen gefördert:</p>
<ul>
  <li><b>Wärmepumpe:</b> Luft-Wasser, Sole-Wasser und Wasser-Wasser mit EHPA-Gütesiegel, GWP höchstens 750,
  maximaler Vorlauftemperatur 55 °C und Leistung unter 100 kW.</li>
  <li><b>Holzzentralheizung:</b> Pellets, Stückholz und Hackgut mit Emissionsgrenzwerten gemäß Umweltzeichen UZ37.</li>
  <li><b>Nah-/Fernwärmeanschluss:</b> wenn am Standort ein klimafreundliches Netz verfügbar ist.</li>
</ul>
<h3>Förderfähige Kosten und ersetzte Altanlagen</h3>
<p>Anerkannt werden Material, Montage, Planung sowie Demontage und Entsorgung der alten Heizanlage und
der Brennstofftanks. Die Installation muss ein befugter Fachbetrieb durchführen, Eigenleistungen sind
ausgeschlossen. Ersetzt werden können Ölheizungen (zentral und Einzelöfen), Gasheizungen (Zentral- und
Etagenheizungen), Kohle- und Koksfeuerungen („Allesbrenner“, auch bei teilweiser Holznutzung) sowie
stationäre Elektroheizungen wie Nachtspeicher- und Elektrospeicheröfen.</p>
"""),
        ("Wie hoch ist die Förderung für Registrierte?", "foerderhoehe", f"""
<p>Die Förderung wird bis zu einer technologiespezifischen Kostenobergrenze gewährt. Diese Obergrenze
umfasst die gesamte Förderung aus Bund, Land und Sauber-Heizen-Zuschuss:</p>
{A.table(
    ["Technologie", "Kostenobergrenze"],
    [
        ["Luft-Wasser-Wärmepumpe", "25.586 €"],
        ["Sole-Wasser- oder Wasser-Wasser-Wärmepumpe", "37.550 €"],
        ["Holzzentralheizung", "variiert je nach Anlagentyp"],
        ["Nah-/Fernwärmeanschluss", "eigene Obergrenze gemäß Infoblatt"],
    ],
    hl_cols=(1,),
)}
<h3>Drei Bausteine bis zur Obergrenze</h3>
<ol>
  <li><b>Basisförderung des Bundes</b> (Kesseltausch-Pauschale): bis zu 7.500 € für Wärmepumpen (galt 2026).</li>
  <li><b>Landesförderung</b> des jeweiligen Bundeslandes: je nach Land mehrere Tausend Euro.</li>
  <li><b>Zusatzförderung „Sauber Heizen für Alle“:</b> schließt die Lücke bis zur Kostenobergrenze.</li>
</ol>
<p>Liegen die tatsächlichen Kosten Ihres Heizungstausches innerhalb der Obergrenze, tragen Sie keinen
Eigenanteil. Übersteigen sie die Obergrenze, zahlen Sie nur die Differenz.</p>
"""),
        ("Wer war förderberechtigt?", "voraussetzungen", f"""
<ul>
  <li><b>Gebäudeeigentum:</b> Sie sind Eigentümerin oder Eigentümer eines Ein- oder Zweifamilienhauses
  bzw. Reihenhauses. Fruchtgenussrecht allein reicht nicht.</li>
  <li><b>Hauptwohnsitz:</b> am Standort des Heizungstausches, begründet vor dem 31. Dezember 2024.</li>
  <li><b>Einkommensgrenze:</b> Der Haushalt liegt im unteren Einkommensdrittel (unterste zwei Einkommensdezile).</li>
</ul>
<h3>Einkommensgrenzen 2026</h3>
<p>Maßgeblich ist das Netto-Haushaltseinkommen nach EU-SILC-Methodik, gestaffelt nach Haushaltsgröße:
Für jeden weiteren Erwachsenen kommt der Faktor 0,5 dazu, für jedes Kind unter 14 Jahren der Faktor 0,3.</p>
{A.table(
    ["Haushalt", "Netto pro Monat (12x)", "Netto pro Jahr"],
    [
        ["Einpersonenhaushalt", "bis 1.867 €", "22.404 €"],
        ["Zwei Erwachsene, keine Kinder", "bis ca. 2.801 €", "ca. 33.612 €"],
        ["Zwei Erwachsene, ein Kind", "bis ca. 3.361 €", "ca. 40.332 €"],
        ["Zwei Erwachsene, zwei Kinder", "bis ca. 3.921 €", "ca. 47.052 €"],
    ],
    hl_cols=(1,),
)}
<h3>Wie wird das Einkommen nachgewiesen?</h3>
<p>Am einfachsten über den Bezug von Sozialhilfe, eine Befreiung vom ORF-Beitrag (frühere GIS-Befreiung)
oder den Bezug von Wohnbeihilfe. Liegt keiner dieser Nachweise vor, prüft die Landesförderungsstelle das
anrechenbare Haushaltseinkommen individuell: Lohn, Gehalt, Pensionen und Einkommen aus Selbständigkeit
werden berücksichtigt, bestimmte Beihilfen und Sozialleistungen nicht. Haushalte ohne jeden
Einkommensnachweis sind ausgeschlossen.</p>
{A.cta("Registriert? Antrag und Umsetzung begleiten lassen",
       "EBZ Energie unterstützt bereits registrierte Haushalte bei Antrag und förderkonformer Umsetzung und zeigt "
       "allen anderen, welche Förderung aktuell möglich ist: Kesseltausch des Bundes und Landesförderung.",
       secondary=("waermepumpe", "Zur Wärmepumpen-Leistungsseite"))}
"""),
        ("Schritt für Schritt: So läuft der Antrag für Registrierte ab", "ablauf", f"""
<p>Der Prozess ist in drei Phasen gegliedert. Beteiligt sind Bund, Land und die Abwicklungsstelle
Kommunalkredit Public Consulting (KPC). Schritt 1 ist seit Herbst 2026 geschlossen, Registrierte setzen
bei Schritt 2 fort.</p>
{A.steps([
    ("Registrierung auf sauber-heizen.at (geschlossen)",
     "Möglich war die Registrierung seit 1. Jänner 2026, solange Budget vorhanden war; seit Herbst 2026 werden "
     "keine neuen Registrierungen angenommen. Nötig waren ein Einkommensnachweis (Sozialhilfebescheid, ORF-Beitragsbefreiung, Wohnbeihilfebescheid "
     "oder Angaben zum Einkommen aller Haushaltsmitglieder), eine Haushaltsbestätigung und einen "
     "Grundbuchauszug. Die Unterlagen gehen an die Landesförderungsstelle, die die Einkommenssituation prüft."),
    ("Energieberatung und Antragstellung",
     "Nach positiver Prüfung organisiert die Landesstelle eine kostenlose, verpflichtende Energieberatung "
     "inklusive Unterstützung bei Angebotseinholung und Antrag. Der Antrag wird online auf sauber-heizen.at "
     "gestellt und umfasst die Angebote und das Energieberatungsprotokoll."),
    ("Umsetzung und Endabrechnung",
     "Mit der Förderzusage (Bund, Land und Sauber-Heizen-Zuschuss) haben Sie 12 Monate für Heizungstausch "
     "und Endabrechnung. Nötig sind Inbetriebnahmebestätigung, Endabrechnungsformular und alle Rechnungen. "
     "Die Bundesförderung zahlt die KPC aus, Landesförderung und Zuschuss die Landesförderungsstelle."),
])}
{A.box_dark("Erst Antrag, dann Auftrag",
    "Anders als bei der regulären Kesseltausch-Förderung sind bei „Sauber Heizen für Alle“ nur Leistungen "
    "förderfähig, die nach der Antragstellung erbracht wurden. Wer vorher beauftragt, verliert den Anspruch.")}
"""),
        ("Fristen auf einen Blick und was bei Ablehnung passiert", "fristen", f"""
{A.table(
    ["Zeitpunkt", "Was gilt"],
    [
        ["1. Jänner 2026", "Start der Online-Registrierung auf sauber-heizen.at"],
        ["Herbst 2026", "Programm beendet, keine neuen Registrierungen (Stand 9. Oktober 2026, umweltfoerderung.at)"],
        ["31. Dezember 2026", "ursprünglich letztmöglicher Registrierungstag, durch das Programmende hinfällig"],
        ["nach positiver Prüfung", "Landesstelle organisiert die Energieberatung"],
        ["nach Antragstellung", "Förderzusage, ab jetzt sind Leistungen förderfähig"],
        ["12 Monate nach Zusage", "Frist für Umsetzung und Endabrechnung"],
    ],
    hl_cols=(0,),
)}
<p>Wird der Antrag eines registrierten Haushalts abgelehnt, etwa weil die Einkommensgrenze überschritten
ist, wird das Projekt nicht automatisch in die reguläre Kesseltausch-Förderung übernommen. In diesem Fall
bleibt der reguläre Kesseltausch, der seit 2. November 2026 als Neuauflage läuft (5.000 € für die
Wärmepumpe, eigene Registrierung bis 31. Dezember 2026), plus die Landesförderung (Bedingungen beim Land
prüfen).</p>
"""),
        ("Sauber Heizen für Alle vs. regulärer Kesseltausch", "vergleich", f"""
<p>„Sauber Heizen für Alle“ ist seit Herbst 2026 für neue Registrierungen geschlossen, der reguläre
Kesseltausch läuft seit 2. November 2026 als Neuauflage wieder. Der Vergleich zeigt die Konditionen von
„Sauber Heizen für Alle“ 2026 und der Kesseltausch-Neuauflage; beide Aktionen sind laut KPC nicht
kombinierbar:</p>
{A.table(
    ["Kriterium", "Sauber Heizen für Alle", "Kesseltausch (Neuauflage seit 2.11.2026)"],
    [
        ["Status", "geschlossen, Registrierte können noch beantragen", "Registrierung bis 31.12.2026 oder Budgetende"],
        ["Förderhöhe", "bis zu 100 % innerhalb der Kostenobergrenze", "5.000 € Pauschale für die Wärmepumpe, keine Prozentgrenze (erste Aktion 2026: bis 7.500 €, max. 30 %)"],
        ["Einkommensgrenze", "unteres Einkommensdrittel", "keine"],
        ["Hauptwohnsitz", "Pflicht, begründet vor 31.12.2024", "nicht nötig"],
        ["Antragsberechtigt", "nur Eigentümer", "Eigentümer, Bauberechtigte, Mieter mit Zustimmung"],
        ["Förderfähige Leistungen", "ab Datum der Antragstellung", "ab 7. Oktober 2026"],
        ["Umsetzungsfrist", "12 Monate nach Förderzusage", "9 Monate nach Registrierung"],
        ["Landesförderung", "in der Obergrenze inkludiert, weitere Kombination teils ausgeschlossen", "zusätzlich kombinierbar"],
    ],
    hl_cols=(1,),
)}
"""),
        ("Wärmepumpe und Photovoltaik: auch mit kleinem Einkommen langfristig sparen", "photovoltaik", f"""
<p>Eine Wärmepumpe braucht Strom. Wer ihn mit einer eigenen {a('photovoltaik', 'Photovoltaikanlage')}
erzeugt, macht sich von steigenden Strompreisen weitgehend unabhängig. Die Wärmepumpe senkt die
Heizkosten, die PV-Anlage die Stromkosten. Photovoltaik wurde 2026 über den EAG-Investitionszuschuss separat
gefördert: Der letzte Call lief vom 8. bis 22. Oktober 2026, derzeit ist kein Bundeszuschuss beantragbar. Ab
2027 ist laut BMWET eine Systemförderung mit Antrag nach der Installation geplant, nicht beschlossen. Wie beide Systeme zusammenarbeiten, lesen
Sie im Ratgeber {a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}. Für die PV-Anlage
bietet EBZ Energie eine {a('finanzierung', 'Finanzierung')} ab 147 € pro Monat inklusive Speicher an, die
Anlage gehört dabei ab Tag 1 Ihnen.</p>
{A.cta("Gemeinsam den offenen Förderweg finden",
       "Registrierte begleiten wir durch Antrag und Umsetzung, alle anderen zum Kesseltausch des Bundes und "
       "zur Landesförderung. "
       "Die Wärmepumpe installieren wir förderkonform.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Sauber Heizen für Alle: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("Antrag, Umsetzungsfrist, Endabrechnung für Registrierte, Landesförderung für alle anderen: "
                 "EBZ Energie aus Villach nimmt Ihnen diesen Weg ab. Als Fachbetrieb für Wärmepumpen und "
                 "Photovoltaik in Kärnten und der Steiermark begleiten wir Sie mit einem Team "
                 "aus zertifizierten Fachkräften von der ersten Frage bis zur warmen Stube."),
        "grid": [
            ("Förder-Check", "Wir prüfen, welche Förderung aktuell offen ist: Kesseltausch des Bundes und Land."),
            ("Antrag für Registrierte", "Begleitung auf sauber-heizen.at inklusive Unterlagen und Angebote."),
            ("Förderkonforme Installation", "EHPA-Gütesiegel, GWP unter 750, Vorlauf 55 °C: passend geplant."),
            ("Photovoltaik als Ergänzung", "Auf Wunsch eine PV-Anlage, abgestimmt auf die Wärmepumpe."),
        ],
    },

    "faq": [
        ("Kann ich mich noch für „Sauber Heizen für Alle 2026“ registrieren?",
         "Nein. Stand Oktober 2026 ist das Programm laut umweltfoerderung.at beendet, neue Registrierungen sind "
         "nicht mehr möglich. Wer bereits registriert ist, kann den Antrag noch stellen und hat nach der Zusage "
         "12 Monate für Umsetzung und Endabrechnung."),
        ("Welche Förderung gibt es jetzt noch für einkommensschwache Haushalte?",
         "Auf Bundesebene der reguläre Kesseltausch, der seit 2. November 2026 als Neuauflage läuft: 5.000 € "
         "Pauschale für die Wärmepumpe, ohne Einkommensprüfung, Registrierung bis 31. Dezember 2026 oder bis das "
         "Budget aufgebraucht ist. Er deckt nicht die gesamten Kosten. Dazu kommt in Kärnten die Landespauschale "
         "von 3.000 € für die Wärmepumpe; ob das Budget reicht, klären wir vor dem Angebot. Die Steiermark nimmt "
         "für neue Wärmepumpen derzeit keine Förderanträge an. Laut BMLUK soll das Angebot für "
         "einkommensschwache Haushalte künftig in die Sanierungsoffensive integriert werden, Details gibt es "
         "noch nicht."),
        ("Kann ich „Sauber Heizen für Alle“ mit der regulären Kesseltausch-Förderung kombinieren?",
         "„Sauber Heizen für Alle“ enthält bereits die Basisförderung des Bundes und die Landesförderung. Es "
         "ist ein eigenständiges Gesamtpaket, das die reguläre Kesseltausch-Förderung nicht ergänzt, sondern "
         "durch eine deutlich höhere Fördersumme bis zur Kostenobergrenze ersetzt. Laut KPC sind beide "
         "Aktionen nicht kombinierbar."),
        ("Was passiert, wenn mein Einkommen knapp über der Grenze liegt?",
         "Dann war kein Antrag auf „Sauber Heizen für Alle“ möglich. Offen ist der reguläre Kesseltausch: Seit "
         "2. November 2026 zahlt der Bund in der Neuauflage 5.000 € für die Wärmepumpe (Erdwärme mit Bohrung "
         "10.000 €), ohne Einkommensgrenze, dazu die Landesförderung (Bedingungen beim Land prüfen). EBZ Energie "
         "rechnet die offenen Wege für Sie durch."),
        ("Muss ich die Energieberatung selbst organisieren?",
         "Nein. Nach positiver Prüfung Ihrer Registrierung organisiert die Landesförderungsstelle automatisch "
         "eine kostenlose Energieberatung. Sie umfasst Erstberatung, Unterstützung bei der Angebotseinholung "
         "und Hilfe bei der Antragstellung; die Beraterin oder der Berater meldet sich bei Ihnen."),
        ("Kann ich als Mieter die Förderung beantragen?",
         "Nein. Bei „Sauber Heizen für Alle“ waren ausschließlich Gebäudeeigentümerinnen und -eigentümer "
         "antragsberechtigt. Beim regulären Kesseltausch der Sanierungsoffensive können auch Mieter ansuchen, "
         "wenn der Eigentümer dem Heizungstausch zustimmt; er läuft seit 2. November 2026 als Neuauflage "
         "wieder, Registrierung bis 31. Dezember 2026."),
        ("Wie lange dauert es für Registrierte bis zur Auszahlung?",
         "Einkommensprüfung, Terminierung der Energieberatung, Angebotseinholung und Antragsprüfung dauern "
         "erfahrungsgemäß mehrere Wochen bis wenige Monate. Danach beginnt die Umsetzungsfrist von 12 Monaten "
         "ab Förderzusage. Halten Sie die Fristen ein, sonst verfällt die Zusage."),
        ("Welche Einkommensgrenze gilt für eine vierköpfige Familie?",
         "Für zwei Erwachsene mit zwei Kindern unter 14 Jahren liegt die Grenze bei rund 3.921 € netto pro "
         "Monat (Faktor 1 + 0,5 + 0,3 + 0,3 auf 1.867 €). Für eine Person gelten 1.867 €, für zwei Erwachsene "
         "rund 2.801 €, mit einem Kind rund 3.361 €."),
        ("Bleibt bei „Sauber Heizen für Alle“ wirklich kein Eigenanteil?",
         "Liegen die Gesamtkosten innerhalb der Kostenobergrenze von 25.586 € (Luft-Wasser) bzw. 37.550 € "
         "(Sole-Wasser), decken Bund, Land und Zuschuss zusammen bis zu 100 % ab. Kostet die Anlage mehr, "
         "zahlen Sie nur die Differenz zur Obergrenze."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team installiert Wärmepumpen und "
                    "Photovoltaik in Kärnten und der Steiermark und begleitet Haushalte durch Registrierung und "
                    "Antrag bei „Sauber Heizen für Alle“. Programmstatus: Stand 9. Oktober 2026 laut umweltfoerderung.at; "
                    "Beträge: Stand April 2026 laut sauber-heizen.at; Kesseltausch-Neuauflage: Informationsblatt "
                    "der KPC (Version 10/2026), geprüft am 19. November 2026. Keine Rechts- oder Steuerberatung, "
                    "maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("Sauber Heizen für Alle (Bundesportal, Registrierung)", "https://www.sauber-heizen.at/"),
        ("Umweltförderung (KPC): Förderbedingungen", "https://www.umweltfoerderung.at/"),
        ("KPC: Informationsblatt Kesseltausch 2026 Ein-/Zweifamilienhaus/Reihenhaus, Neuauflage ab 2.11.2026 (Version 10/2026)",
         "https://www.sanierungsoffensive.gv.at/fileadmin/user_upload/2026/Infoblatt_Neuauflage_Kesseltausch_2026_EFH.pdf"),
        ("Sanierungsoffensive: Aktionsseite Kesseltausch Neuauflage Ein-/Zweifamilienhaus oder Reihenhaus",
         "https://www.sanierungsoffensive.gv.at/kesseltausch/neuauflage-ein-/zweifamilienhaus-oder-reihenhaus"),
        ("BMLUK: Sanierung und Kesseltausch 2027",
         "https://www.bmluk.gv.at/themen/klima-und-umwelt/klima/klima-initiativen-und-foerderungen/ufg/sanierung-kesselaustausch-2027.html"),
        ("Land Steiermark: Förderung für Heizungen (Wohnbau, Stand 10. Oktober 2026)",
         "https://www.wohnbau.steiermark.at/cms/ziel/164947118/DE/"),
    ],
    "related": [
        ("/waermepumpenfoerderung-in-oesterreich/", "Wärmepumpenförderung Österreich 2026: Überblick"),
        ("/sanierungsoffensive-2026/", "Sanierungsoffensive 2026: Kesseltausch neu, 5.000 €"),
        ("/kosten-einer-waermepumpe/", "Kosten einer Wärmepumpe"),
        ("waermepumpe", "Wärmepumpen-Installateur EBZ Energie"),
    ],
    "cta": {
        "h3": "Offene Förderwege prüfen",
        "text": "Programm beendet: Wir begleiten Registrierte durch den Antrag, alle anderen zum Kesseltausch des Bundes und zur Landesförderung.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Heizungstausch: die offenen Förderwege nutzen",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
