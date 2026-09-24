"""Ratgeber: Sauber Heizen für Alle 2026 (bis zu 100 % Förderung für einkommensschwache Haushalte).

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
    "title": "Sauber Heizen für Alle 2026: bis 100 % Förderung | EBZ",
    "description": ("Sauber Heizen für Alle 2026: bis zu 100 % Förderung für den Heizungstausch bei "
                    "Einkommen bis 1.867 € netto. Obergrenzen 25.586 € und 37.550 €, Ablauf, Fristen."),
    "eyebrow": "Förderung · Einkommensschwache Haushalte",
    "crumb_label": "Sauber Heizen für Alle 2026",
    "h1": "Sauber Heizen für Alle 2026: Bis zu 100 % Förderung für Ihren Heizungstausch",
    "lead": ("Für Haushalte im unteren Einkommensdrittel übernimmt „Sauber Heizen für Alle“ den Umstieg auf "
             "eine Wärmepumpe bis zur Kostenobergrenze von 25.586 € (Luft-Wasser) bzw. 37.550 € (Sole-Wasser) "
             "vollständig. Hier lesen Sie, wer förderberechtigt ist, welche Einkommensgrenzen gelten und wie "
             "der Ablauf von der Registrierung bis zur Auszahlung funktioniert."),
    "chips": [
        "Förderung: <b>bis 100 %</b>",
        "Obergrenze Luft-Wasser: <b>25.586 €</b>",
        "Einkommen (1 Person): <b>1.867 €</b> netto/Monat",
        "Registrierung bis <b>31.12.2026</b>",
    ],
    "date_published": "2026-03-15",
    "date_modified": "2026-09-24",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit neuer Wärmepumpe und Photovoltaik nach dem Heizungstausch",

    "tldr": [
        "„Sauber Heizen für Alle“ ist ein Programm des Bundes (BMLUK) gemeinsam mit den Bundesländern. Es "
        "ergänzt die Bundes- und Landesförderung so, dass bis zu 100 % der förderfähigen Kosten abgedeckt sind.",
        "Kostenobergrenzen: 25.586 € für Luft-Wasser-Wärmepumpen, 37.550 € für Sole-Wasser- und "
        "Wasser-Wasser-Systeme. Liegen Ihre Kosten darunter, bleibt kein Eigenanteil.",
        "Voraussetzungen: Eigentum an einem Ein-, Zweifamilien- oder Reihenhaus, Hauptwohnsitz am Standort "
        "(begründet vor 31. Dezember 2024), Haushaltseinkommen im unteren Einkommensdrittel.",
        "Einkommensgrenze: 1.867 € netto pro Monat für eine Person, rund 2.801 € für zwei Erwachsene, "
        "rund 3.361 € mit einem Kind, rund 3.921 € mit zwei Kindern.",
        "Ablauf: Registrierung auf sauber-heizen.at (seit 1. Jänner 2026 bis 31. Dezember 2026), kostenlose "
        "Energieberatung durch die Landesstelle, Antrag, dann 12 Monate für Umsetzung und Endabrechnung. "
        "Leistungen vor der Antragstellung sind nicht förderfähig.",
    ],
    "kpis": [
        ("100 %", "maximale Kostenübernahme"),
        ("25.586 €", "Obergrenze Luft-Wasser-WP"),
        ("1.867 €", "Nettoeinkommen, 1 Person/Monat"),
        ("12 Monate", "Umsetzungsfrist ab Zusage"),
    ],

    "sections": [
        ("Warum es „Sauber Heizen für Alle“ gibt", "hintergrund", f"""
<p>Die reguläre Bundesförderung über die {a('/sanierungsoffensive-2026/', 'Sanierungsoffensive 2026')}
zahlt bis zu 7.500 € für eine Wärmepumpe. Für Haushalte mit geringem Einkommen bleibt danach ein
Eigenanteil, der oft nicht tragbar ist. Genau hier setzt „Sauber Heizen für Alle“ an. Das Programm wurde
vom Bundesministerium für Land- und Forstwirtschaft, Klima- und Umweltschutz, Regionen und
Wasserwirtschaft (BMLUK) ins Leben gerufen und wird gemeinsam mit den Bundesländern umgesetzt.</p>
<p>Die Förderung wird als einmaliger Investitionszuschuss in Ergänzung zur Basisförderung des Bundes und
zur jeweiligen Landesförderung vergeben. Im Idealfall decken die drei Bausteine zusammen bis zu 100 %
der förderfähigen Kosten ab: eine neue {a('waermepumpe', 'Wärmepumpe')} ohne Eigenanteil.
Stand: April 2026.</p>
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
        ("Wie hoch ist die Förderung?", "foerderhoehe", f"""
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
  <li><b>Basisförderung des Bundes</b> (Kesseltausch-Pauschale): bis zu 7.500 € für Wärmepumpen.</li>
  <li><b>Landesförderung</b> des jeweiligen Bundeslandes: je nach Land mehrere Tausend Euro.</li>
  <li><b>Zusatzförderung „Sauber Heizen für Alle“:</b> schließt die Lücke bis zur Kostenobergrenze.</li>
</ol>
<p>Liegen die tatsächlichen Kosten Ihres Heizungstausches innerhalb der Obergrenze, tragen Sie keinen
Eigenanteil. Übersteigen sie die Obergrenze, zahlen Sie nur die Differenz.</p>
"""),
        ("Wer ist förderberechtigt?", "voraussetzungen", f"""
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
{A.cta("Förderfähigkeit vorab prüfen lassen",
       "EBZ Energie schätzt mit Ihnen ein, ob Sie die Einkommensgrenzen erfüllen, und zeigt die beste "
       "Alternative, falls nicht. So geht keine Zeit verloren.",
       secondary=("waermepumpe", "Zur Wärmepumpen-Leistungsseite"))}
"""),
        ("Schritt für Schritt: So läuft die Antragstellung ab", "ablauf", f"""
<p>Der Prozess ist in drei Phasen gegliedert. Beteiligt sind Bund, Land und die Abwicklungsstelle
Kommunalkredit Public Consulting (KPC).</p>
{A.steps([
    ("Registrierung auf sauber-heizen.at",
     "Möglich seit 1. Jänner 2026, solange Budget vorhanden ist, spätestens bis 31. Dezember 2026. Sie "
     "benötigen einen Einkommensnachweis (Sozialhilfebescheid, ORF-Beitragsbefreiung, Wohnbeihilfebescheid "
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
        ["31. Dezember 2026", "letztmöglicher Tag für die Registrierung, sofern Budget vorhanden"],
        ["nach positiver Prüfung", "Landesstelle organisiert die Energieberatung"],
        ["nach Antragstellung", "Förderzusage, ab jetzt sind Leistungen förderfähig"],
        ["12 Monate nach Zusage", "Frist für Umsetzung und Endabrechnung"],
    ],
    hl_cols=(0,),
)}
<p>Wird Ihr Antrag abgelehnt, etwa weil die Einkommensgrenze überschritten ist, wird das Projekt nicht
automatisch in die reguläre Kesseltausch-Förderung übernommen. Sie müssten einen neuen, separaten Antrag
über die Sanierungsoffensive stellen. Eine frühzeitige Einschätzung der Einkommenssituation spart daher
Zeit.</p>
"""),
        ("Sauber Heizen für Alle vs. regulärer Kesseltausch", "vergleich", f"""
{A.table(
    ["Kriterium", "Sauber Heizen für Alle", "Kesseltausch (Sanierungsoffensive)"],
    [
        ["Förderquote", "bis zu 100 % innerhalb der Kostenobergrenze", "max. 30 % der Kosten, bis 7.500 €"],
        ["Einkommensgrenze", "unteres Einkommensdrittel", "keine"],
        ["Hauptwohnsitz", "Pflicht, begründet vor 31.12.2024", "nicht nötig"],
        ["Antragsberechtigt", "nur Eigentümer", "Eigentümer, Bauberechtigte, Mieter mit Zustimmung"],
        ["Förderfähige Leistungen", "ab Datum der Antragstellung", "ab 3. Oktober 2025"],
        ["Umsetzungsfrist", "12 Monate nach Förderzusage", "9 Monate nach Registrierung"],
        ["Landesförderung", "in der Obergrenze inkludiert, weitere Kombination teils ausgeschlossen", "zusätzlich kombinierbar"],
    ],
    hl_cols=(1,),
)}
"""),
        ("Wärmepumpe und Photovoltaik: auch mit kleinem Einkommen langfristig sparen", "photovoltaik", f"""
<p>Eine Wärmepumpe braucht Strom. Wer ihn mit einer eigenen {a('photovoltaik', 'Photovoltaikanlage')}
erzeugt, macht sich von steigenden Strompreisen weitgehend unabhängig. Die Wärmepumpe senkt die
Heizkosten, die PV-Anlage die Stromkosten. Photovoltaik wird über den EAG-Investitionszuschuss separat
gefördert, die Calls 2026 starten im April, Juni und Oktober. Wie beide Systeme zusammenarbeiten, lesen
Sie im Ratgeber {a('/photovoltaik-fuer-waermepumpe/', 'Photovoltaik für die Wärmepumpe')}. Für die PV-Anlage
bietet EBZ Energie eine {a('finanzierung', 'Finanzierung')} ab 147 € pro Monat inklusive Speicher an, die
Anlage gehört dabei ab Tag 1 Ihnen.</p>
{A.cta("Gemeinsam die richtige Förderung finden",
       "Wir prüfen die Einkommensgrenzen, begleiten Registrierung und Antrag auf sauber-heizen.at und "
       "installieren die Wärmepumpe förderkonform.",
       primary=("kontakt", "Kostenlose Erstberatung"), secondary=("waermepumpe", "Mehr zur Wärmepumpe"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Sauber Heizen für Alle: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("Einkommensprüfung, Registrierung, Energieberatung, Antrag, Umsetzungsfrist, Endabrechnung: "
                 "EBZ Energie aus Villach nimmt Ihnen diesen Weg ab. Als Fachbetrieb für Wärmepumpen und "
                 "Photovoltaik in Kärnten und der Steiermark begleiten wir Sie mit einem festangestellten Team "
                 "aus zertifizierten Fachkräften von der ersten Frage bis zur warmen Stube."),
        "grid": [
            ("Förderfähigkeits-Check", "Wir prüfen die Einkommensgrenzen und helfen bei den Nachweisen."),
            ("Registrierung und Antrag", "Begleitung auf sauber-heizen.at inklusive Unterlagen und Angebote."),
            ("Förderkonforme Installation", "EHPA-Gütesiegel, GWP unter 750, Vorlauf 55 °C: passend geplant."),
            ("Photovoltaik als Ergänzung", "Auf Wunsch eine PV-Anlage, abgestimmt auf die Wärmepumpe."),
        ],
    },

    "faq": [
        ("Kann ich „Sauber Heizen für Alle“ mit der regulären Kesseltausch-Förderung kombinieren?",
         "„Sauber Heizen für Alle“ enthält bereits die Basisförderung des Bundes und die Landesförderung. Es "
         "ist ein eigenständiges Gesamtpaket, das die reguläre Kesseltausch-Förderung nicht ergänzt, sondern "
         "durch eine deutlich höhere Fördersumme bis zur Kostenobergrenze ersetzt."),
        ("Was passiert, wenn mein Einkommen knapp über der Grenze liegt?",
         "Dann können Sie keinen Antrag auf „Sauber Heizen für Alle“ stellen. Offen bleibt die reguläre "
         "Bundesförderung über die Sanierungsoffensive 2026 mit bis zu 7.500 € (Erdwärme 12.500 €), die mit "
         "Landesförderungen kombinierbar ist. EBZ Energie rechnet beide Wege für Sie durch."),
        ("Muss ich die Energieberatung selbst organisieren?",
         "Nein. Nach positiver Prüfung Ihrer Registrierung organisiert die Landesförderungsstelle automatisch "
         "eine kostenlose Energieberatung. Sie umfasst Erstberatung, Unterstützung bei der Angebotseinholung "
         "und Hilfe bei der Antragstellung; die Beraterin oder der Berater meldet sich bei Ihnen."),
        ("Kann ich als Mieter die Förderung beantragen?",
         "Nein. Bei „Sauber Heizen für Alle“ sind ausschließlich Gebäudeeigentümerinnen und -eigentümer "
         "antragsberechtigt. Beim regulären Kesseltausch der Sanierungsoffensive 2026 können auch Mieter "
         "ansuchen, wenn der Eigentümer dem Heizungstausch zustimmt."),
        ("Wie lange dauert es von der Registrierung bis zur Auszahlung?",
         "Einkommensprüfung, Terminierung der Energieberatung, Angebotseinholung und Antragsprüfung dauern "
         "erfahrungsgemäß mehrere Wochen bis wenige Monate. Danach beginnt die Umsetzungsfrist von 12 Monaten "
         "ab Förderzusage. Je früher Sie sich registrieren, desto mehr Planungssicherheit haben Sie."),
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
                    "Antrag bei „Sauber Heizen für Alle“. Alle Beträge entsprechen dem Stand April 2026 und den "
                    "Vorgaben auf sauber-heizen.at und umweltfoerderung.at. Keine Rechts- oder Steuerberatung, "
                    "maßgeblich sind die offiziellen Förderbedingungen."),
    "sources": [
        ("Sauber Heizen für Alle (Bundesportal, Registrierung)", "https://www.sauber-heizen.at/"),
        ("Umweltförderung (KPC): Förderbedingungen", "https://www.umweltfoerderung.at/"),
    ],
    "related": [
        ("/waermepumpenfoerderung-in-oesterreich/", "Wärmepumpenförderung Österreich 2026: Überblick"),
        ("/sanierungsoffensive-2026/", "Sanierungsoffensive 2026: regulärer Kesseltausch"),
        ("/kosten-einer-waermepumpe/", "Kosten einer Wärmepumpe"),
        ("waermepumpe", "Wärmepumpen-Installateur EBZ Energie"),
    ],
    "cta": {
        "h3": "Einkommensgrenze prüfen",
        "text": "Wir schätzen Ihre Förderfähigkeit ein und begleiten Sie durch Registrierung und Antrag.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Heizungstausch ohne Eigenanteil",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, "
                   "Montage und Förderabwicklung aus einer Hand übernimmt."),
}
