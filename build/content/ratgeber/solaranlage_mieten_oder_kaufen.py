"""Ratgeber: Solaranlage mieten, kaufen oder finanzieren? Der ehrliche Vergleich.

Zusammengeführt aus drei alten WordPress-Beiträgen:
  /photovoltaik-mieten/, /solaranlage-mit-speicher-mieten/, /solaranlage-mieten-oder-kaufen/
(alle Jänner 2026). Die alten Beiträge bewarben ein Miet- bzw. Ratenmodell von EBZ;
EBZ bietet heute Kauf und Finanzierung (Eigentum ab Tag 1). Mietmodelle werden hier
neutral als Marktangebot erklärt, nicht als EBZ-Angebot.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a

FN = ("<p><small>*Beispielkonditionen und Richtwerte: Mietraten und Laufzeiten aus marktüblichen "
      "Angeboten, Finanzierungsrate abhängig von Laufzeit und Anlagenkonfiguration, Kaufpreis = "
      "EBZ-Richtpreis für 10 kWp mit Speicher vor Förderung.</small></p>")
FN_KURZ = "<p><small>*Beispielkonditionen, Details siehe Rechenbeispiel.</small></p>"

ARTICLE = {
    "slug": "solaranlage-mieten-oder-kaufen",
    "path": "/solaranlage-mieten-oder-kaufen/",
    "title": "Solaranlage mieten oder kaufen? Vergleich mit Zahlen | EBZ",
    "description": ("Solaranlage mieten, kaufen oder finanzieren? Miete kostet über 20 Jahre 28.800 bis "
                    "43.200 €, Kauf ab 15.000 €. Vergleichstabelle, Rechenbeispiel, 8 Antworten."),
    "eyebrow": "Ratgeber · Finanzierung",
    "crumb_label": "Solaranlage mieten oder kaufen",
    "h1": "Solaranlage mieten, kaufen oder finanzieren? Der ehrliche Vergleich über 20 Jahre",
    "lead": ("Eine 10-kWp-Anlage mit Speicher kostet gekauft 15.000 bis 22.000 Euro, gemietet über 20 Jahre "
             "28.800 bis 43.200 Euro, und gehört Ihnen dann trotzdem nicht. Dieser Ratgeber zeigt, wie "
             "Mietmodelle wirklich funktionieren, wann sich der Kauf rechnet und warum eine Finanzierung "
             "mit Eigentum ab Tag 1 für die meisten Haushalte der bessere Mittelweg ist."),
    "chips": [
        "Miete: <b>120 bis 180 €</b> pro Monat*",
        "Kauf 10 kWp + Speicher: <b>15.000 bis 22.000 €</b>",
        "Finanzierung: <b>ab 147 €</b> pro Monat*",
        "Amortisation: <b>4 bis 6 Jahre</b>",
    ],
    "date_published": "2026-01-15",
    "date_modified": "2026-09-24",
    "hero_img": "gen_eigenheim",
    "hero_alt": "Einfamilienhaus mit Photovoltaikanlage auf dem Dach: Vergleich von Miete, Kauf und Finanzierung",

    "tldr": [
        "Beim Mietmodell installiert ein Anbieter die Anlage auf Ihrem Dach und bleibt Eigentümer. Sie zahlen "
        "je nach Größe 80 bis 200 Euro pro Monat*, meist 15 bis 20 Jahre lang, teils bis zu 25 Jahre.",
        "Über 20 Jahre summiert sich eine Miete von 120 bis 180 Euro auf 28.800 bis 43.200 Euro*. Eine "
        "gekaufte 10-kWp-Anlage mit Speicher kostet 15.000 bis 22.000 Euro vor Förderung.",
        "Förderungen gehen an den Eigentümer der Anlage. Beim Mieten ist das der Anbieter, beim Kauf und bei "
        "der Finanzierung sind das Sie.",
        "Der Kauf rechnet sich am schnellsten: bis zu 85 Prozent weniger Stromkosten, typische Amortisation "
        "in 4 bis 6 Jahren, danach 20 und mehr Jahre nahezu kostenloser Strom.",
        "Die EBZ-Finanzierung ab 147 Euro pro Monat inklusive Speicher* verbindet beides: keine Anschaffung "
        "auf einmal, aber Eigentum und volle Förderung ab dem ersten Tag.",
    ],
    "kpis": [
        ("120 bis 180 €", "Miete pro Monat, 10 kWp mit Speicher*"),
        ("28.800 bis 43.200 €", "Mietkosten über 20 Jahre*"),
        ("15.000 bis 22.000 €", "Kaufpreis 10 kWp mit Speicher vor Förderung"),
        ("ab 147 €", "Finanzierung pro Monat inkl. Speicher*"),
    ],

    "sections": [
        ("Drei Wege zur eigenen Solaranlage: Miete, Kauf, Finanzierung", "drei-modelle", f"""
<p>Wer eine Photovoltaikanlage will, aber die Anschaffung scheut, stößt auf drei Modelle, die auf den
ersten Blick ähnlich klingen und sich wirtschaftlich stark unterscheiden:</p>
<ul>
  <li><b>Miete (auch Pacht- oder Vertragsmodell genannt):</b> Ein Anbieter montiert die Anlage auf Ihrem
  Dach und bleibt deren Eigentümer. Sie zahlen eine fixe Monatsrate und nutzen den Strom. Am Ende der
  Laufzeit gibt es je nach Vertrag eine Kaufoption, eine Verlängerung oder den Rückbau.</li>
  <li><b>Kauf:</b> Sie bezahlen die Anlage einmalig und sind ab der Montage Eigentümer. Förderung,
  Einspeisevergütung und die gesamte Stromersparnis bleiben bei Ihnen.</li>
  <li><b>Finanzierung:</b> Sie kaufen die Anlage, bezahlen sie aber in Monatsraten. Bei der
  {a('finanzierung', 'EBZ-Finanzierung')} gehört die Anlage ab dem ersten Tag Ihnen, mit allen
  Rechten des Käufers, also auch der vollen Förderung.</li>
</ul>
<p>Der entscheidende Unterschied ist nicht die Monatsrate, sondern die Frage: Wem gehört die Anlage, und wer
bekommt Förderung und Erträge? Daran entscheidet sich, was Sie über 20 Jahre wirklich bezahlen. Die
Preisbasis liefert der Ratgeber {a('/kosten-einer-solaranlage/', 'Kosten einer Solaranlage')}.</p>
"""),
        ("Wie ein Mietmodell für Photovoltaik funktioniert", "mietmodell", f"""
<p>Beim Mieten plant, montiert und betreibt ein Anbieter die komplette Anlage. Statt 15.000 bis
22.000 Euro auf einmal zahlen Sie eine Monatsrate zwischen 80 und 200 Euro*, für ein Einfamilienhaus
mit 8 bis 10 kWp und Speicher üblicherweise 120 bis 180 Euro*. Die Anlage bleibt während der gesamten
Laufzeit Eigentum des Anbieters, Sie haben nur das Nutzungsrecht am Strom.</p>
<p>Die Laufzeit ist lang, weil der Anbieter seine Investition über die Rate zurückverdienen muss:
Üblich sind 15 bis 20 Jahre, einzelne Anbieter binden bis zu 25 Jahre. Eine ordentliche Kündigung ist
in dieser Zeit nicht vorgesehen, ein vorzeitiger Ausstieg kostet meist eine Ablöse von mehreren tausend
Euro.</p>
<h3>Was in der Miete üblicherweise enthalten ist</h3>
<ul>
  <li><b>Montage und Inbetriebnahme:</b> Module, Wechselrichter, gegebenenfalls Speicher und Netzanmeldung.</li>
  <li><b>Wartung und Reparatur:</b> Inspektionen, Austausch defekter Komponenten, meist mit Monitoring.</li>
  <li><b>Versicherung:</b> Schutz gegen Sturm, Hagel, Feuer oder Diebstahl, oft mit Ausschlussklauseln.</li>
</ul>
{A.box("Die Leistungsliste im Prospekt ist nicht die Leistungsliste im Vertrag. Prüfen Sie, welche "
       "Reparaturen abgedeckt sind, wer die Einspeisevergütung erhält und was der Vertrag für Hausverkauf, "
       "Verlängerung und Rückbau vorsieht.",
       label="Vor der Unterschrift:")}
"""),
        ("Vorteile und Nachteile der Miete", "miete-vor-nachteile", f"""
<p>Das Mietmodell hat eine klare Zielgruppe: Haushalte, die keine Anschaffung auf einmal stemmen können
und sich um nichts kümmern möchten. Dafür zahlen sie einen deutlichen Aufpreis.</p>
<h3>Vorteile</h3>
<ul>
  <li><b>Keine Anschaffung auf einmal:</b> Ihr Eigenkapital bleibt frei, die Stromproduktion beginnt
  sofort nach der Montage.</li>
  <li><b>Planbare Rate:</b> Die Miete ist über die Laufzeit fixiert, unabhängig von Strompreisen.</li>
  <li><b>Technisches Risiko beim Anbieter:</b> Fällt ein Wechselrichter aus, kümmert sich der Vermieter
  darum.</li>
  <li><b>Für Betriebe:</b> Die Mietrate ist als Betriebsausgabe absetzbar. Privatpersonen können sie
  nicht geltend machen.</li>
</ul>
<h3>Nachteile</h3>
<ul>
  <li><b>Höhere Gesamtkosten:</b> Über 20 Jahre zahlen Sie 28.800 bis 43.200 Euro* für eine Anlage, die
  gekauft 15.000 bis 22.000 Euro kostet. Die Mehrkosten liegen häufig bei 50 bis 100 Prozent.</li>
  <li><b>Die Anlage gehört Ihnen nicht:</b> Größerer Speicher oder Wallbox brauchen die Zustimmung des
  Eigentümers.</li>
  <li><b>Keine Förderung für Sie:</b> Landes- und Bundesförderungen erhält der Eigentümer, also der
  Anbieter. Ob er sie in die Rate einrechnet, entscheidet er.</li>
  <li><b>Einspeisevergütung oft nicht bei Ihnen:</b> Je nach Vertrag fließt sie an den Vermieter oder wird
  mit der Miete verrechnet.</li>
  <li><b>Lange Bindung:</b> 15 bis 25 Jahre ohne ordentliches Kündigungsrecht. Beim Hausverkauf muss der
  Käufer den Vertrag übernehmen, sonst wird eine Ablöse fällig.</li>
  <li><b>Offenes Ende:</b> Kaufoption zum Restwert, Verlängerung oder Rückbau stehen im Kleingedruckten,
  nicht im Prospekt.</li>
</ul>
"""),
        ("Kauf: Eigentum ab dem ersten Tag und die schnellste Amortisation", "kauf", f"""
<p>Beim Kauf investieren Sie einmal und profitieren über die Lebensdauer der Anlage von 25 bis
30 Jahren. Eine {a('/photovoltaik-komplettanlage-10-kwp-mit-speicher-und-montage/', '10-kWp-Komplettanlage mit Speicher und Montage')}
kostet bei EBZ Energie rund 15.000 bis 22.000 Euro vor Förderung. Welche Landes- und Bundesmittel
2026 abgehen, lesen Sie im Ratgeber
{a('/photovoltaik-foerderung-oesterreich-2026/', 'Photovoltaik-Förderung Österreich 2026')}.</p>
<p>Der wirtschaftliche Hebel ist beim Kauf am größten: Die Anlage senkt Ihre Stromkosten um bis zu
85 Prozent, die Einspeisevergütung landet auf Ihrem Konto, und die Investition ist bei unseren Kunden
typischerweise nach 4 bis 6 Jahren amortisiert. Danach liefert die Anlage 20 und mehr Jahre nahezu
kostenlosen Strom. Ob sich der Speicher rechnet, zeigt der Ratgeber
{a('/ab-wann-lohnt-sich-photovoltaik-mit-speicher/', 'Ab wann lohnt sich Photovoltaik mit Speicher')}.</p>
<h3>Was beim Kauf auf Sie zukommt</h3>
<ul>
  <li><b>Wartung und Versicherung:</b> Rechnen Sie mit 200 bis 400 Euro pro Jahr* für Inspektion,
  Versicherung und Rücklagen für einen späteren Wechselrichtertausch.</li>
  <li><b>Garantien fangen das Risiko ab:</b> Bei EBZ Energie bis zu 30 Jahre Leistungsgarantie auf die
  Module und mindestens 10 Jahre Produktgarantie.</li>
  <li><b>Volle Freiheit:</b> Speicher nachrüsten, Wallbox ergänzen, einer Energiegemeinschaft beitreten:
  Sie entscheiden allein. Beim Hausverkauf ist die Anlage wertsteigernder Teil der Immobilie, kein
  Vertrag, der übernommen werden muss.</li>
  <li><b>Die Hürde:</b> Der Betrag muss auf einmal verfügbar sein. Hier setzt die Finanzierung an.</li>
</ul>
{A.cta("Was kostet Ihre Anlage konkret?",
       "Wir planen Ihre Anlage mit Projektbericht, 3D-Belegplan und Statikreport und zeigen Ihnen Kauf "
       "und Finanzierung nebeneinander, mit echten Zahlen für Ihr Dach.",
       secondary=("photovoltaik", "Zur Photovoltaik"))}
"""),
        ("Vergleichstabelle: Miete, Kauf und Finanzierung", "vergleich", f"""
<p>Die Tabelle fasst die drei Modelle für eine 10-kWp-Anlage mit Speicher zusammen: Mietwerte sind
marktübliche Beispielkonditionen, Finanzierungswerte beziehen sich auf die EBZ-Finanzierung.</p>
{A.table(
    ["Kriterium", "Miete", "Kauf", "Finanzierung (EBZ)"],
    [
        ["Eigentum", "Bleibt beim Anbieter, Kaufoption frühestens am Vertragsende",
         "Sie, ab der Montage", "Sie, ab Tag 1"],
        ["Förderung", "Erhält der Anbieter; Weitergabe nicht garantiert",
         "Volle Förderung für Sie", "Volle Förderung für Private"],
        ["Einspeisevergütung", "Je nach Vertrag beim Anbieter oder verrechnet", "Bei Ihnen", "Bei Ihnen"],
        ["Anschaffung", "0 €", "15.000 bis 22.000 € vor Förderung", "Keine Einmalzahlung nötig"],
        ["Monatliche Kosten", "120 bis 180 €* über 15 bis 25 Jahre", "Keine Rate, 200 bis 400 €* Wartung pro Jahr",
         "ab 147 €* inkl. Speicher; Beispiel 25.000 € über 25 Jahre: ab 164 €*"],
        ["Gesamtkosten 20 Jahre", "28.800 bis 43.200 €*, Anlage danach nicht automatisch Ihre",
         "Kaufpreis abzüglich Förderung plus Wartung", "Kaufpreis abzüglich Förderung plus Zinsen und Wartung"],
        ["Flexibilität", "Änderungen nur mit Zustimmung des Anbieters, Hausverkauf mit Vertragsübernahme",
         "Uneingeschränkt", "Uneingeschränkt, Anlage ist Ihr Eigentum"],
        ["Wartung und Reparatur", "Im Vertrag enthalten (Ausschlüsse prüfen)",
         "Ihre Sache, abgesichert durch bis zu 30 Jahre Leistungs- und mind. 10 Jahre Produktgarantie",
         "Wie beim Kauf, gleiche Garantien"],
        ["Bonität", "Prüfung durch den Anbieter", "Keine", "Digitale Prüfung in Minuten, 94 % Annahmequote, kein Grundbucheintrag"],
    ],
    hl_cols=(3,),
)}
{FN}
"""),
        ("Rechenbeispiel: 10 kWp mit Speicher über 20 Jahre", "rechenbeispiel", f"""
<p>Nehmen wir ein Einfamilienhaus in Kärnten mit einer 10-kWp-Anlage und Speicher und rechnen die drei
Modelle über 20 Jahre durch*. Anlage und Stromertrag sind in allen drei Fällen gleich, nur die
Zahlungsströme unterscheiden sich.</p>
{A.steps([
    ("Miete: 28.800 bis 43.200 Euro, ohne Eigentum",
     " Bei 120 bis 180 Euro pro Monat zahlen Sie in 240 Monaten 28.800 bis 43.200 Euro. Wartung und "
     "Versicherung sind enthalten, die Förderung nicht. Nach 20 Jahren gehört die Anlage weiterhin dem "
     "Anbieter: Kaufoption zum Restwert, Verlängerung oder Rückbau."),
    ("Kauf: 15.000 bis 22.000 Euro plus Wartung",
     " Zum Kaufpreis vor Förderung kommen über 20 Jahre 4.000 bis 8.000 Euro für Wartung, Versicherung "
     "und Rücklagen (200 bis 400 Euro pro Jahr). Abzüglich der Förderung, die Sie als Eigentümer erhalten, "
     "bleiben die Gesamtkosten deutlich unter dem Mietmodell. Die Anlage ist ab dem ersten Tag Ihre."),
    ("Finanzierung: ab 164 Euro pro Monat bei 25.000 Euro, Eigentum ab Tag 1",
     " Keine Einmalzahlung, sondern eine fixe Monatsrate: Im repräsentativen Beispiel unseres "
     "Finanzierungspartners kostet eine 10-kWp-Anlage mit 10-kWh-Speicher (25.000 Euro, abzüglich 3.000 Euro "
     "Bundesförderung) über 25 Jahre ab 164 Euro im Monat, mit Reststrom rund 185 Euro. Zum Vergleich: "
     "Ohne PV zahlt ein 4-Personen-Haushalt mit 7.000 kWh heute rund 163 Euro Strom im Monat. Der "
     "Unterschied zur Miete: Die Rate endet mit der Laufzeit, die Anlage gehört von Anfang an Ihnen, die "
     "Förderung fließt auf Ihr Konto."),
])}
<p>Der zweite Blick gilt der Ersparnis: Mit Speicher senken unsere Kunden ihre Stromkosten um bis zu
85 Prozent, beim Kauf ist die Investition typischerweise nach 4 bis 6 Jahren amortisiert. Bei der
Finanzierung deckt die Stromersparnis einen großen Teil der Rate ab. Beim Mietmodell läuft die Rate
dagegen weiter, solange der Vertrag läuft, auch wenn die Anlage längst abbezahlt wäre.</p>
{A.box_dark("Die entscheidende Frage",
    "Nicht „Wie hoch ist die Rate?“, sondern „Wem gehört die Anlage, wenn die Rate endet?“ Bei Miete "
    "lautet die Antwort: dem Anbieter, außer Sie kaufen sie zusätzlich. Bei Kauf und Finanzierung: Ihnen, "
    "und zwar ab dem ersten Tag.")}
{FN}
"""),
        ("Finanzierung: der Mittelweg, bei dem die Anlage Ihnen gehört", "finanzierung", f"""
<p>Die EBZ-Finanzierung ist kein Mietmodell und kein Ratenkauf mit Eigentumsvorbehalt bis zur letzten
Rate. Sie kaufen die Anlage und finanzieren den Kaufpreis über eine Laufzeit, die zu Ihrem Budget passt.
Die Anlage wird mit der Montage Ihr Eigentum: Sie beantragen die Förderung auf Ihren Namen, die
Einspeisevergütung geht auf Ihr Konto, und beim Hausverkauf gehört die Anlage zur Immobilie.</p>
<ul>
  <li><b>Rate ab 147 Euro pro Monat inklusive Speicher*</b>, ohne Anschaffung auf einmal.</li>
  <li><b>Eigentum ab Tag 1</b>, nicht erst am Ende der Laufzeit.</li>
  <li><b>Volle Förderung für Private</b>, weil Sie Eigentümer und Antragsteller sind.</li>
  <li><b>0 € Anzahlung und fixe Rate über die gesamte Laufzeit</b> (bis 25 Jahre), also kein Zinsrisiko.</li>
  <li><b>Kein Grundbucheintrag, kein Banktermin:</b> digitale Finanzierungszusage meist in unter zwei
  Minuten, 94 Prozent Annahmequote, auch für Selbständige und Pensionisten.</li>
  <li><b>Kostenlose Sondertilgung jederzeit</b>, wenn Sie früher zurückzahlen wollen.</li>
  <li><b>Gleiche Technik und Garantien wie beim Kauf:</b> bis zu 30 Jahre Leistungsgarantie,
  mindestens 10 Jahre Produktgarantie, montiert von zertifizierten Fachkräften.</li>
</ul>
<h3>Zwei repräsentative Beispiele unseres Finanzierungspartners Cloover</h3>
{A.table(
    ["", "Kleine Anlage", "Anlage mit Speicher"],
    [
        ["Finanzierungsbetrag", "15.000 € (Beispiel 8 kWp)", "25.000 € (10 kWp + 10 kWh)"],
        ["Abzüglich Bundesförderung (Beispiel)", "900 €", "3.000 €"],
        ["Laufzeit", "25 Jahre", "25 Jahre"],
        ["Monatliche Rate", "ab 102 €*", "ab 164 €*"],
        ["Rate plus Reststrom (rund 25 €)", "rund 127 €*", "rund 185 €*"],
        ["Stromkosten heute ohne PV (7.000 kWh)", "rund 163 € im Monat", "rund 163 € im Monat"],
    ],
    hl_cols=(1, 2),
)}
<p><small>*Repräsentative Beispiele aus der Finanzierungsbeilage, Stand September 2026. Rate abhängig von
Angebot und Laufzeit, Förderhöhe und Zusage variieren. Alle Angaben freibleibend, Finanzierung
vorbehaltlich Bonitätsprüfung.</small></p>
<h3>So läuft die Finanzierung bei EBZ Energie ab</h3>
{A.steps([
    ("Beratung",
     " Wir erfassen Stromverbrauch, Dachflächen und Ihre Ziele und sagen ehrlich, welche Anlagengröße "
     "sich rechnet."),
    ("Projektbericht mit 3D-Belegplan und Statikreport",
     " Sie erhalten ein konkretes Angebot mit den Zahlen für Kauf und Finanzierung nebeneinander."),
    ("Finanzierung digital abschließen",
     " Sie stellen die Anfrage online bei unserem Partner Cloover, die Zusage kommt meist in unter zwei "
     "Minuten, ohne Banktermin. Laufzeit (bis 25 Jahre) und Rate legen wir gemeinsam fest."),
    ("Montage und Inbetriebnahme",
     " Unser Team montiert die Anlage und meldet sie beim Netzbetreiber an. Ab jetzt gehört sie Ihnen."),
    ("Förderung auf Ihren Namen",
     " Wir bereiten die Anträge vor, die Auszahlung geht direkt an Sie."),
])}
<p>Das passt für Haushalte, die keine 15.000 bis 22.000 Euro auf einmal binden wollen, und für Betriebe,
die ihre Liquidität im Geschäft brauchen. Über 300 Projekte in sechs Bundesländern zeigen, dass die
Kombination funktioniert: siehe {a('referenzen', 'unsere Referenzen')}.</p>
{FN_KURZ}
"""),
        ("Checkliste: Welches Modell passt zu Ihnen?", "checkliste", f"""
<p>Sechs Fragen, die die Entscheidung in den meisten Fällen klar machen:</p>
<ol>
  <li><b>Wie lange bleiben Sie in der Immobilie?</b> Bei 10 und mehr Jahren lohnt Eigentum fast immer.
  Bei geplantem Verkauf ist ein Mietvertrag mit Übertragungspflicht ein Risiko.</li>
  <li><b>Ist der Kaufpreis verfügbar?</b> Ja: Kauf. Nein oder lieber nicht binden: Finanzierung.</li>
  <li><b>Wollen Sie die Förderung selbst erhalten?</b> Dann kommt nur Kauf oder Finanzierung infrage.</li>
  <li><b>Planen Sie Erweiterungen (Wallbox, Wärmepumpe, größerer Speicher)?</b> Als Eigentümer
  entscheiden Sie allein.</li>
  <li><b>Soll sich jemand um alles kümmern?</b> Das spricht für Miete oder für einen Kauf mit
  Wartungsvertrag, den Sie jederzeit kündigen können.</li>
  <li><b>Was steht am Vertragsende?</b> Lassen Sie sich Restwert, Rückbaukosten und Übernahmeregeln
  schriftlich geben, bevor Sie einen Mietvertrag unterschreiben.</li>
</ol>
<p>Vergleichen Sie immer die Gesamtkosten über die Laufzeit, nicht die Monatsrate. Ein scheinbar
günstiges Angebot wird durch Nebenkosten, Restwert oder fehlende Förderung schnell zum teuersten.</p>
"""),
        ("Fazit: Eigentum schlägt Miete, Finanzierung schließt die Lücke", "fazit", f"""
<p>Ein Mietmodell löst ein einziges Problem, die fehlende Anschaffungssumme, und schafft dafür drei
neue: höhere Gesamtkosten, keine Förderung und eine Anlage, die Ihnen nach 20 Jahren immer noch nicht
gehört. Der Kauf ist wirtschaftlich die stärkste Variante, mit typischer Amortisation in 4 bis 6 Jahren
und bis zu 85 Prozent geringeren Stromkosten. Wer den Kaufpreis nicht auf einmal binden will, bekommt mit
der Finanzierung ab 147 Euro pro Monat* denselben Vorteil in Raten: Eigentum ab Tag 1, volle Förderung,
fixe Rate ohne Anzahlung und Sondertilgung jederzeit.</p>
{A.cta("Kauf oder Finanzierung? Wir rechnen beides für Ihr Dach",
       "Kostenlose Beratung, Projektbericht mit 3D-Belegplan und Statikreport, und die Zahlen für Kauf und "
       "Finanzierung nebeneinander, ohne Verkaufsdruck.",
       primary=("kontakt", "Jetzt Beratung anfragen"), secondary=("finanzierung", "Zur Finanzierung"))}
{FN_KURZ}
"""),
    ],

    "partner": {
        "h2": "Ihr Partner für Kauf und Finanzierung: EBZ Energie",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und montiert Photovoltaikanlagen, Speicher, Wärmepumpen und "
                 "Wallboxen in Kärnten und der Steiermark, mit einem festangestellten Team aus zertifizierten "
                 "Fachkräften. Wir verkaufen keine Mietverträge: Unsere Kunden werden Eigentümer, entweder "
                 "durch Kauf oder durch die EBZ-Finanzierung ab 147 Euro pro Monat inklusive Speicher*. "
                 "Förderabwicklung, Netzanmeldung und Inbetriebnahme sind in beiden Fällen dabei."),
        "grid": [
            ("Eigentum ab Tag 1", "Auch bei Finanzierung gehört die Anlage sofort Ihnen, nicht erst am Ende der Laufzeit."),
            ("Volle Förderung", "Sie sind Antragsteller, wir bereiten die Anträge vor. Die Auszahlung geht an Sie."),
            ("Fixe Rate, 0 € Anzahlung", "Digitale Zusage in Minuten, kein Grundbucheintrag, Sondertilgung jederzeit kostenlos."),
            ("Bis zu 30 Jahre Leistungsgarantie", "Mindestens 10 Jahre Produktgarantie, 300+ Projekte in 6 Bundesländern."),
        ],
    },

    "faq": [
        ("Lohnt sich das Mieten einer Solaranlage?",
         "Wirtschaftlich in den meisten Fällen nicht. Über 20 Jahre summiert sich eine Miete von 120 bis 180 Euro "
         "pro Monat auf 28.800 bis 43.200 Euro, während eine gekaufte 10-kWp-Anlage mit Speicher 15.000 bis "
         "22.000 Euro vor Förderung kostet. Die Anlage gehört Ihnen am Ende trotzdem nicht. Sinnvoll ist die "
         "Miete nur, wenn weder Kauf noch Finanzierung möglich sind."),
        ("Bekomme ich bei einer gemieteten PV-Anlage Förderung?",
         "In der Regel nicht direkt. Förderungen werden an den Eigentümer der Anlage ausbezahlt, und das ist "
         "beim Mietmodell der Anbieter. Manche Anbieter rechnen die Förderung in die Rate ein, verpflichtet "
         "sind sie dazu nicht. Beim Kauf und bei der EBZ-Finanzierung erhalten Sie die Förderung selbst."),
        ("Was passiert am Ende eines Mietvertrags?",
         "Das regelt der Vertrag. Üblich sind drei Varianten: Kaufoption zum Restwert, Verlängerung oder "
         "Rückbau durch den Anbieter. Manche Verträge sehen einen kostenlosen Übergang vor. Lassen Sie sich "
         "Restwert und Rückbaukosten vor der Unterschrift schriftlich geben."),
        ("Wie funktioniert die Finanzierung bei EBZ Energie?",
         "Sie kaufen die Anlage und bezahlen sie in fixen Monatsraten über unseren Finanzierungspartner Cloover: "
         "0 Euro Anzahlung, Laufzeit bis 25 Jahre, im repräsentativen Beispiel ab 164 Euro im Monat für 10 kWp "
         "mit 10-kWh-Speicher. Die Anlage gehört Ihnen ab dem ersten Tag, Sie erhalten als Privatperson die "
         "volle Förderung, die Zusage kommt digital in wenigen Minuten ohne Grundbucheintrag, und Sondertilgungen "
         "sind jederzeit kostenlos."),
        ("Wie hoch ist die monatliche Miete für eine Solaranlage mit Speicher?",
         "Marktüblich sind 120 bis 180 Euro pro Monat für ein Einfamilienhaus mit 8 bis 10 kWp und Speicher. "
         "Kleinere Anlagen beginnen bei rund 80 Euro, Pakete mit Wallbox können 200 Euro und mehr kosten. "
         "Entscheidend ist die Summe über die Laufzeit von meist 15 bis 20 Jahren, nicht die Rate."),
        ("Kann ich einen Mietvertrag für eine PV-Anlage vorzeitig kündigen?",
         "Meist nicht ohne Ablöse. Mietverträge laufen 15 bis 25 Jahre ohne ordentliches Kündigungsrecht. "
         "Bei Hausverkauf muss der Käufer den Vertrag übernehmen, oder Sie lösen die Anlage zum Restwert ab. "
         "Die Ablösesumme kann mehrere tausend Euro betragen."),
        ("Wer trägt bei Kauf und Finanzierung das Reparaturrisiko?",
         "Sie als Eigentümer, abgesichert durch bis zu 30 Jahre Leistungsgarantie und mindestens 10 Jahre "
         "Produktgarantie bei EBZ Energie. Für Wartung, Versicherung und Rücklagen sollten Sie 200 bis "
         "400 Euro pro Jahr einplanen. Ein Wartungsvertrag ist optional und jederzeit kündbar."),
        ("Ist die Miete einer Solaranlage steuerlich absetzbar?",
         "Für Privatpersonen nicht, weil es sich um private Wohnkosten handelt. Unternehmen können die Mietrate "
         "als Betriebsausgabe absetzen, beim Kauf schreiben sie die Anlage ab. Welche Variante günstiger ist, "
         "klärt Ihre Steuerberatung."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. Sein Team hat über 300 Photovoltaikanlagen "
                    "in sechs Bundesländern geplant und montiert, per Kauf oder Finanzierung, und kennt die "
                    "Vertragsfallen der Mietmodelle aus vielen Beratungsgesprächen. Dieser Ratgeber ist keine "
                    "Finanz- oder Rechtsberatung; maßgeblich sind die konkreten Vertrags- und Förderbedingungen "
                    "in Ihrem Fall."),
    "related": [
        ("finanzierung", "Finanzierung ab 147 € im Monat"),
        ("/kosten-einer-solaranlage/", "Kosten einer Solaranlage 2026"),
        ("/ab-wann-lohnt-sich-photovoltaik-mit-speicher/", "Ab wann lohnt sich PV mit Speicher?"),
        ("batteriespeicher", "Batteriespeicher: Modelle und Preise"),
    ],
    "cta": {
        "h3": "Kauf oder Finanzierung?",
        "text": "Wir rechnen beide Varianten für Ihr Dach durch. Eigentum ab Tag 1, volle Förderung, ehrliche Zahlen.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Ihre Anlage, Ihr Eigentum, Ihre Ersparnis",
    "final_text": ("Kostenlose Erstberatung, Projektbericht mit 3D-Belegplan und Statikreport und ein Team aus "
                   "Villach, das Planung, Montage und Förderabwicklung aus einer Hand übernimmt."),
}
