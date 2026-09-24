"""Ratgeber: Energiegemeinschaft, Nachteile und worauf Sie achten sollten.

Migriert von ebz-photovoltaik.at/energiegemeinschaft-nachteile/ (Juli 2026) und mit
Fakten aus den Cluster-Artikeln (Netzkosten, Kosten, Beitreten, Kärnten) vertieft:
Zuordnungsquote, laufende Kosten, Smart-Meter-Pflicht, Nahbereich, Vertragsfallen, ElWG.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

ARTICLE = {
    "slug": "energiegemeinschaft-nachteile",
    "path": "/energiegemeinschaft-nachteile/",
    "title": "Energiegemeinschaft: 7 Nachteile ehrlich bewertet | EBZ",
    "description": ("Nachteile einer Energiegemeinschaft: Ersparnis nur auf zugeordnete 25 bis 60 %, 2 bis 8 € "
                    "Gebühr im Monat, Smart-Meter-Pflicht, Nahbereich. Wann es sich lohnt."),
    "eyebrow": "Energiegemeinschaft · Nachteile",
    "crumb_label": "Nachteile",
    "h1": "Energiegemeinschaft: 7 Nachteile ehrlich bewertet und wie Sie sie klein halten",
    "lead": ("Energiegemeinschaften bringen Vorteile, aber sie sind nicht für jeden und in jeder Situation die "
             "beste Lösung. Dieser Ratgeber nennt die Nachteile mit Zahlen, damit Sie eine fundierte "
             "Entscheidung treffen können."),
    "chips": [
        "Ersparnis nur auf <b>25 bis 60 %</b> des Verbrauchs",
        "Gebühr: <b>2 bis 8 €</b> je Monat",
        "<b>Smart Meter</b> mit 15-min-Werten Pflicht",
        "Rabatt nur im <b>Nahbereich</b>",
    ],
    "date_published": "2026-07-22",
    "date_modified": "2026-09-24",
    "hero_img": "gen_hero",
    "hero_alt": "Photovoltaikanlage auf einem Hausdach, Ausgangspunkt für die Abwägung einer Energiegemeinschaft",

    "tldr": [
        "Der wichtigste Nachteil: Vergünstigt wird nur Strom, der zeitgleich erzeugt und verbraucht wird. Ein "
        "Haushalt ohne Tagesverbrauch erreicht etwa 25 Prozent Zuordnungsquote, mit Wärmepumpe, E-Auto oder "
        "Homeoffice 40 bis 60 Prozent.",
        "Die Teilnahme kostet 2 bis 8 Euro je Zählpunkt und Monat, also 25 bis 100 Euro im Jahr. Dem stehen "
        "laut Erfahrungsberichten typisch 100 bis 300 Euro Vorteil gegenüber, bei geringer Zuordnung weniger.",
        "Technische und räumliche Hürden: Smart Meter mit Viertelstundenwerten bei allen Beteiligten, "
        "Netzentgelt-Abschlag nur im Nahbereich (selber Trafo oder Umspannwerk), keine Großunternehmen in der EEG.",
        "Nach dem Beitritt gibt es drei Rechnungen statt einer. Vertragsfallen wie Jahresbindung oder "
        "Austrittsgebühren lassen sich vermeiden, wenn Sie vier Angaben vor der Unterschrift prüfen.",
        "Für Erzeuger mit PV ist die Gemeinschaft in der Regel attraktiv, weil sie dem Überschuss 8 bis 12 Cent "
        "statt 6,146 Cent OeMAG-Tarif bringt. Mit Speicher und Energiemanagement schrumpfen die meisten Nachteile.",
    ],
    "kpis": [
        ("25 %", "Zuordnungsquote eines Haushalts ohne Tagesverbrauch"),
        ("25 bis 100 €", "Kosten der Teilnahme im Jahr"),
        ("3", "Rechnungen nach dem Beitritt: Netz, Lieferant, Gemeinschaft"),
        ("1 bis 3 Monate", "übliche Kündigungsfrist, kein wirtschaftliches Risiko"),
    ],

    "sections": [
        ("Vorteile und Nachteile im Überblick", "ueberblick", f"""
<p>Eine Energiegemeinschaft ist ein sinnvolles Modell, aber kein Selbstläufer. Damit Sie fundiert entscheiden
können, hier die Gegenüberstellung, jeweils mit der Zahl dahinter:</p>
{A.table(
    ["Vorteil", "Nachteil"],
    [
        ["Günstigerer Strom: EG-Bezugspreis typisch 12 bis 16 ct statt 12 bis 20 ct netto beim Lieferanten",
         "Gilt nur für die zugeordnete Menge, typisch 25 bis 60 % des Verbrauchs"],
        ["Netzentgelt minus 57 % (lokal) oder 28 % (regional), E-Abgabe und Förderbeitrag entfallen",
         "Nur im Nahbereich, Grundpauschale und Leistungspreis bleiben"],
        ["Mehr Wert für PV-Überschuss: 8 bis 12 ct statt 6,146 ct OeMAG (Juli 2026)",
         "Nur für den zeitgleich verbrauchten Anteil, der Rest bleibt beim OeMAG-Tarif"],
        ["Lieferant und OeMAG-Vertrag bleiben, Austritt mit 1 bis 3 Monaten Frist",
         "Laufende Gebühr 2 bis 8 € je Monat, drei Rechnungen statt einer"],
        ["Regionale Wertschöpfung, Unabhängigkeit von der Börse",
         "Organisatorischer Aufwand bei Gründung, Smart-Meter-Pflicht, Rechtsrahmen im Umbruch"],
    ],
)}
<p>Die Grundlagen zu Modellen, Ablauf und Ersparnis stehen im {a('eg', 'Leitartikel zur Energiegemeinschaft')}.
Hier geht es nur um die Kehrseite.</p>
"""),
        ("Nachteil 1: Die Ersparnis gilt nur für zugeordneten Strom", "zuordnungsquote", f"""
<p>Das ist der Punkt, den viele unterschätzen. Der Netzbetreiber ordnet für jede Viertelstunde nur die
Menge zu, die in der Gemeinschaft gleichzeitig erzeugt und verbraucht wird. Wird abends viel verbraucht,
aber mittags erzeugt, passt wenig zusammen. Ein Haushalt mit 4.000 kWh Jahresverbrauch, der tagsüber
nicht zuhause ist, bekommt etwa 1.000 kWh zugeordnet, eine Zuordnungsquote von 25 Prozent. Mit
Wärmepumpe, E-Auto oder Homeoffice sind 40 bis 60 Prozent erreichbar.</p>
<p>Was das in Euro bedeutet: Bei Richtwerten von 8 Cent Netznutzung, 0,7 Cent Netzverlust, 1,5 Cent
Elektrizitätsabgabe und 1 Cent Förderbeitrag spart eine lokale EEG rund 7,5 Cent je zugeordneter
Kilowattstunde aus Netz und Abgaben. Kommt ein EG-Preis von 14 Cent* statt 17 Cent* Lieferantenpreis dazu,
sind es rund 10,5 Cent. Bei 1.000 kWh Zuordnung also rund 105 Euro* im Jahr, bei 2.400 kWh rund 250 Euro*.
Die Rechnung Position für Position steht im Artikel
{a('/energiegemeinschaft-netzkosten/', 'Energiegemeinschaft und Netzkosten')}.</p>
{A.box("Der Netzentgelt-Abschlag ist kein Rabatt auf die ganze Stromrechnung. Alles, was Sie außerhalb der "
       "Gemeinschaft vom Lieferanten beziehen, wird weiterhin zum vollen Tarif verrechnet. Entscheidend ist "
       "deshalb nicht der Prozentsatz, sondern die zugeordnete Menge.", label="Wichtig:")}
<p><small>*Richtwerte 2026 für Netzentgelt und Abgaben laut E-Control, EG-Preis und Lieferantenpreis sind
Beispielwerte. Jede Gemeinschaft legt ihre Preise selbst fest.</small></p>
"""),
        ("Nachteil 2 und 3: Aufwand und laufende Kosten", "aufwand-kosten", f"""
<p><b>Organisatorischer Aufwand:</b> Eine Energiegemeinschaft braucht eine Rechtsform (etwa einen Verein),
eine Registrierung als Marktteilnehmer bei ebutilities, einen Vertrag mit dem Netzbetreiber und eine
korrekte Abrechnung der viertelstündlich zugeordneten Mengen. Das ist machbar, aber Arbeit. Wer sie
nicht selbst leisten will, tritt einer bestehenden Gemeinschaft bei (über 11.000 gibt es in Österreich)
oder nutzt eine Plattform, die Verwaltung und Abrechnung übernimmt. Was auf Gründer zukommt, steht im
Artikel {a('/energiegemeinschaft-gruenden/', 'Energiegemeinschaft gründen')}.</p>
<p><b>Laufende Kosten:</b> Die Gemeinschaft ist günstig, aber nicht gratis. Mitglieder zahlen 2 bis 8 Euro
je Zählpunkt und Monat oder 0,5 bis 2 Cent je abgerechneter Kilowattstunde, im Jahr 25 bis 100 Euro.
Bei geringer Zuordnung kann das den Vorteil spürbar schmälern: Wer nur 500 kWh im Jahr zugeordnet
bekommt, spart rund 50 Euro* und zahlt davon einen guten Teil als Gebühr wieder ab. Für kleine Abnehmer
ist deshalb ein Gebührenmodell je Kilowattstunde günstiger als die Pauschale. Alle Kostenarten stehen im
Artikel {a('/energiegemeinschaft-kosten/', 'Energiegemeinschaft: Kosten und Abrechnung')}.</p>
{A.box_dark("Faustregel vor dem Beitritt",
    "Liegt die jährliche Gebühr über 30 Prozent Ihres erwarteten Vorteils, passt die Gemeinschaft nicht zu "
    "Ihrem Verbrauchsprofil. Dann lohnt sich ein anderes Gebührenmodell oder eine andere Gemeinschaft. Der "
    "Energiegemeinschaft-Rechner zeigt den erwarteten Jahresvorteil mit Ihren Zahlen.")}
"""),
        ("Nachteil 4 und 5: Technische und räumliche Voraussetzungen", "voraussetzungen", f"""
<p><b>Smart Meter mit Viertelstundenwerten:</b> Alle Beteiligten brauchen einen Smart Meter, der 15-Minuten-Werte
an den Netzbetreiber übermittelt. Zwar sind in Kärnten und der Steiermark fast alle Haushalte umgerüstet,
standardmäßig sendet der Zähler aber nur Tageswerte. Das Opt-in aktivieren Sie im Kundenportal des
Netzbetreibers, es dauert wenige Tage. Wer früher aus Datenschutzgründen ein Opt-out gewählt hat, muss das
rückgängig machen. Ohne Viertelstundenwerte ist keine Zuordnung möglich.</p>
<p><b>Nahbereich:</b> Den Netzentgelt-Abschlag gibt es nur, wenn Erzeuger und Abnehmer am selben Trafo
(lokal, minus 57 Prozent) oder am selben Umspannwerk (regional, minus 28 Prozent) hängen. Das schränkt die
Auswahl ein: Nicht in jeder Gemeinde gibt es eine passende Gemeinschaft, und ob Ihr Anschluss dazugehört,
entscheidet der Netzbetreiber anhand der Zählpunktnummer, nicht die Postleitzahl. Strom teilen ist zwar
österreichweit möglich, etwa mit Verwandten in Wien, aber als Bürgerenergiegemeinschaft ohne Rabatt und
ohne Abgabenbefreiung. Hinzu kommt: Große Unternehmen ab 250 Mitarbeitern dürfen an einer
Erneuerbaren-Energie-Gemeinschaft nicht teilnehmen. Wie Sie eine Gemeinschaft im richtigen Nahbereich
finden, steht im Artikel {a('/energiegemeinschaft-finden/', 'Energiegemeinschaft finden')}.</p>
"""),
        ("Nachteil 6: Drei Rechnungen und Vertragsfallen", "rechnungen-vertraege", f"""
<p>Nach dem Beitritt bekommen Sie drei Rechnungen statt einer: vom Netzbetreiber (mit reduziertem EG-Anteil),
vom Lieferanten (Reststrom) und von der Gemeinschaft (EG-Strom). Plattformen wie energyfamily fassen die
Gemeinschaftsseite monatlich in einer App zusammen, die Netz- und Lieferantenrechnung bleiben aber
getrennt. Wer einen Stromtarif mit Mindestabnahme oder Grundgebühr hat, sollte prüfen, ob er sich mit
weniger Bezugsmenge noch rechnet.</p>
<p>Vier Punkte tauchen in Verträgen auf, die Sie vor der Unterschrift lesen sollten:</p>
<ul>
  <li><b>Jahresbindungen</b> mit automatischer Verlängerung. Üblich sind Kündigungsfristen von ein bis drei
  Monaten zum Monatsende.</li>
  <li><b>Preisklauseln,</b> die den Einspeisepreis an den OeMAG-Tarif koppeln, sodass er mitsinkt.</li>
  <li><b>Kopplungen</b> an ein bestimmtes Stromprodukt oder Konto desselben Anbieters.</li>
  <li><b>Gebühren für den Austritt</b> oder die Zählpunktabmeldung, die es bei seriösen Gemeinschaften nicht gibt.</li>
</ul>
<p>Ein wirtschaftliches Risiko besteht darüber hinaus nicht: Der Lieferantenvertrag bleibt bestehen, nicht
zugeordnete Mengen werden wie bisher abgerechnet, und Sie können mit ein bis drei Monaten Frist austreten.
Den Ablauf beschreibt der Artikel {a('/energiegemeinschaft-beitreten/', 'Energiegemeinschaft beitreten')}.</p>
{A.cta("Ehrliche Einschätzung gewünscht?",
       "Wir sagen Ihnen vor dem Beitritt, welche Zuordnungsquote bei Ihrem Verbrauchsprofil realistisch ist "
       "und ob sich die Gemeinschaft für Sie rechnet.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("eg_rechner", "Ersparnis berechnen"))}
"""),
        ("Nachteil 7: Der Rechtsrahmen ist im Umbruch", "rechtsrahmen", f"""
<p>Mit 1. Oktober 2026 löst das Elektrizitätswirtschaftsgesetz (ElWG) die bisherigen Regeln des
Erneuerbaren-Ausbau-Gesetzes ab. Bestehende Gemeinschaften laufen weiter und werden übergeführt, doch
welche Marktprozesse die Netzbetreiber zum Stichtag bereitstellen, ist laut Koordinationsstelle noch
offen. Ab 1. Jänner 2027 gilt zudem eine neue Netzentgeltstruktur: Das ElWG ermächtigt die E-Control,
die Abschläge per Verordnung neu festzulegen. Ob die 57 und 28 Prozent bleiben, ist nicht bekannt.</p>
<p>Für die Entscheidung heißt das: Rechnen Sie mit den heutigen Werten, aber planen Sie nicht mit einer
Erhöhung. Positiv ist, dass Bürgerenergiegemeinschaften und Peer-to-Peer-Verträge ab Oktober 2026 im
Nahbereich ebenfalls den reduzierten Netztarif erhalten und die Abgabenbefreiung ausdrücklich bei der
Erneuerbaren-Energie-Gemeinschaft bleibt. Sie bleibt damit das wirtschaftlich stärkste Modell.</p>
"""),
        ("Für wen es sich trotzdem lohnt und wie Sie die Nachteile klein halten", "lohnt-sich", f"""
<p>Für Erzeuger mit einer {a('photovoltaik', 'PV-Anlage')} ist eine Energiegemeinschaft in der Regel attraktiv,
weil sie dem Überschuss mehr Wert gibt: 8 bis 12 Cent statt 6,146 Cent OeMAG-Tarif im Juli 2026, ohne den
OeMAG-Vertrag zu kündigen. Bei 7.000 kWh Überschuss und 60 Prozent Zuordnung sind das rund 160 Euro*
Mehrerlös im Jahr, plus der Vorteil beim eigenen Bezug abends und im Winter. Reine Abnehmer profitieren
ebenfalls, aber weniger stark, und am meisten, wenn sie tagsüber verbrauchen.</p>
<p>Der Hebel gegen den größten Nachteil ist Technik. Ein {a('batteriespeicher', 'Speicher')} verschiebt
Überschuss in die Abendstunden, in denen Abnehmer in der Gemeinschaft mehr brauchen. Ein
Energiemanagementsystem legt steuerbare Lasten wie Wärmepumpe oder Wallbox in die Erzeugungszeiten und
hebt so die Zuordnungsquote. Beides zusammen macht aus 25 Prozent Zuordnung 40 bis 60 Prozent. Für das
Energiemanagementsystem gibt es seit Juni 2026 die {a('/ems-foerderung/', 'EMS-Förderung des Klimafonds')},
und die Teilnahme an einer Energiegemeinschaft ist dort eine der zulässigen Betriebsoptionen.</p>
{A.table(
    ["Situation", "Empfehlung"],
    [
        ["PV-Anlage, Überschuss, Nahbereich mit Abnehmern", "Beitreten: höherer Erlös, kein Risiko, OeMAG bleibt als Auffangnetz"],
        ["Kein PV, Tagesverbrauch (Wärmepumpe, Homeoffice, E-Auto)", "Beitreten: hohe Zuordnungsquote, Netz und Abgaben gespart"],
        ["Kein PV, nur Abendverbrauch, Pauschalgebühr", "Genau rechnen: Gebühr je kWh wählen oder abwarten"],
        ["Verwandte außerhalb des Nahbereichs", "Teilen möglich, aber ohne Rabatt: eher Peer-to-Peer ab Oktober 2026"],
        ["Großunternehmen ab 250 Mitarbeitern", "EEG nicht möglich, Bürgerenergiegemeinschaft prüfen"],
    ],
)}
<p><small>*Beispielrechnung mit 10 Cent EG-Einspeisepreis. Jede Gemeinschaft legt ihre Preise selbst fest.</small></p>
"""),
        ("Fazit: Nachteile der Energiegemeinschaft", "fazit", f"""
<p>Die Nachteile einer Energiegemeinschaft sind real, aber beherrschbar: eine Ersparnis, die nur für die
zugeordnete Menge gilt, Gebühren von 25 bis 100 Euro im Jahr, Smart-Meter-Pflicht, Nahbereich und drei
Rechnungen. Wer die Zuordnungsquote realistisch einschätzt, das Gebührenmodell zum Verbrauchsprofil
wählt und den Vertrag vor der Unterschrift prüft, geht kein Risiko ein. Mit einer eigenen PV-Anlage, einem
Speicher und einem Energiemanagementsystem verschieben Sie die Bilanz klar zu Ihren Gunsten. Wir beraten
Sie ehrlich, ob und wie sich der Schritt für Sie lohnt.</p>
{A.cta("Nachteile minimieren, Vorteile maximieren",
       "Wir zeigen Ihnen kostenlos, wie Sie mit PV, Speicher und Energiemanagement das Beste aus einer "
       "Energiegemeinschaft holen, und sagen ehrlich, wenn sie sich bei Ihnen nicht rechnet.",
       primary=("kontakt", "Kostenlose Beratung sichern"), secondary=("eg_privat", "Zur Energiegemeinschaft mit EBZ"))}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Photovoltaik und Energiegemeinschaft: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("Die meisten Nachteile einer Energiegemeinschaft lassen sich mit der richtigen Technik entschärfen. "
                 "EBZ Energie aus Villach plant PV-Anlage, Speicher und Energiemanagementsystem so, dass Erzeugung "
                 "und Verbrauch bestmöglich zusammenpassen, installiert alles aus einer Hand mit einem "
                 "festangestellten Team aus zertifizierten Fachkräften in Kärnten und der Steiermark und nimmt Sie "
                 "in eine passende Gemeinschaft auf, abgerechnet über die Plattform unseres Partners energyfamily."),
        "grid": [
            ("Ehrliche Einschätzung", "Wir rechnen Zuordnungsquote und Gebühr vor dem Beitritt durch."),
            ("Alles aus einer Hand", "PV, Speicher, Wärmepumpe, Wallbox und EG-Anbindung vom selben Team."),
            ("Abrechnung inklusive", "Zählpunktfreigabe, Aufnahme und monatliche Abrechnung über energyfamily."),
            ("Kurze Kündigungsfrist", "Keine Einrichtungsgebühr, keine Austrittsgebühr, Lieferant bleibt."),
        ],
    },

    "faq": [
        ("Was sind die größten Nachteile einer Energiegemeinschaft?",
         "Erstens gilt die Ersparnis nur für den zeitgleich erzeugten und verbrauchten Anteil, bei einem Haushalt "
         "ohne Tagesverbrauch etwa 25 Prozent. Zweitens kostet die Teilnahme 2 bis 8 Euro je Monat. Dazu kommen "
         "Smart-Meter-Pflicht, Nahbereich, drei Rechnungen und bei einer Gründung der organisatorische Aufwand."),
        ("Lohnt sich eine Energiegemeinschaft für reine Verbraucher?",
         "Ja, wenn der Verbrauch tagsüber anfällt. Abnehmer sparen auf den EG-Strom rund 7,5 Cent je "
         "Kilowattstunde aus Netz und Abgaben (lokale EEG, Richtwerte 2026) plus die Differenz zum "
         "Lieferantenpreis. Wer nur abends zuhause ist, bekommt wenig zugeordnet und sollte die Gebühr gegen den "
         "Vorteil rechnen."),
        ("Warum schwankt die Ersparnis?",
         "Geteilt und vergünstigt wird nur der Strom, der in derselben Viertelstunde erzeugt und verbraucht wird. "
         "Wird abends viel verbraucht, aber mittags erzeugt, passt wenig zusammen. Ein Speicher und ein "
         "Energiemanagementsystem heben die Zuordnungsquote von etwa 25 auf 40 bis 60 Prozent."),
        ("Ist die Abrechnung kompliziert?",
         "Sie bekommen drei Rechnungen: Netzbetreiber, Lieferant für den Reststrom und Gemeinschaft für den "
         "EG-Strom. Der Netzbetreiber ordnet die Mengen automatisch zu, Plattformen wie energyfamily stellen die "
         "Gemeinschaftsabrechnung monatlich in einer App dar. Für Mitglieder ist der Aufwand gering."),
        ("Kann ich Geld verlieren?",
         "Ein wirtschaftliches Risiko besteht praktisch nicht: Lieferant und OeMAG-Vertrag bleiben, nicht "
         "zugeordnete Mengen werden wie bisher abgerechnet, der Austritt ist mit ein bis drei Monaten Frist "
         "möglich. Verlieren können Sie nur die Gebühr, wenn die Zuordnung sehr gering ausfällt."),
        ("Was ist mit der Energiegemeinschaft nach dem ElWG?",
         "Bestehende Gemeinschaften laufen ab 1. Oktober 2026 im neuen Rechtsrahmen weiter. Ab 1. Jänner 2027 "
         "kann die E-Control die Netzentgelt-Abschläge per Verordnung neu festlegen, ob sich die 57 und 28 "
         "Prozent ändern, ist offen. Die Abgabenbefreiung bleibt der Erneuerbaren-Energie-Gemeinschaft vorbehalten."),
        ("Wie kann ich die Nachteile minimieren?",
         "Mit einer gut dimensionierten PV-Anlage, einem Speicher und einem Energiemanagementsystem, das "
         "Erzeugung und Verbrauch aufeinander abstimmt. Dazu: Gebührenmodell zum Verbrauchsprofil wählen, "
         "Nahbereich vorab prüfen lassen und Kündigungsfrist, Preise und Aufteilungsschlüssel vor der "
         "Unterschrift lesen."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team plant und installiert PV-Anlagen, "
                    "Speicher und Energiemanagementsysteme in Kärnten und der Steiermark und begleitet Kunden beim "
                    "Einstieg in Energiegemeinschaften. Die Inhalte werden anhand der Vorgaben von E-Control, OeMAG "
                    "und energiegemeinschaften.gv.at aktualisiert. Keine Rechts- oder Steuerberatung."),
    "sources": [
        ("E-Control: Energiegemeinschaften", "https://www.e-control.at/energiegemeinschaften"),
        ("Koordinationsstelle: FAQs zum ElWG", "https://energiegemeinschaften.gv.at/faqs-zum-elwg/"),
        ("Koordinationsstelle: FAQs", "https://energiegemeinschaften.gv.at/faqs/"),
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/marktpreis"),
        ("oesterreich.gv.at", "https://www.oesterreich.gv.at/"),
    ],
    "related": [
        ("eg", "Energiegemeinschaft: Der Leitartikel"),
        ("/energiegemeinschaft-kosten/", "Energiegemeinschaft: Kosten und Abrechnung"),
        ("/energiegemeinschaft-netzkosten/", "Netzkosten: Was in der Energiegemeinschaft günstiger wird"),
        ("batteriespeicher", "Batteriespeicher: Überschuss in den Abend verschieben"),
    ],
    "cta": {
        "h3": "Rechnet es sich bei Ihnen?",
        "text": "Wir schätzen Zuordnungsquote und Gebühr für Ihr Verbrauchsprofil ehrlich ein, bevor Sie beitreten.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Nachteile kennen, Vorteile nutzen",
    "final_text": ("Kostenlose Erstberatung, ehrliche Zahlen und ein Team aus Villach, das Planung, Montage "
                   "und EG-Anbindung aus einer Hand übernimmt."),
}
