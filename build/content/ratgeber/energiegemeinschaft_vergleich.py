"""Ratgeber: Energiegemeinschaft Vergleich (Anbieter und Plattformen in Österreich, Stand November 2026).

Neuer Artikel (kein WordPress-Vorgänger), erstellt 2026-11-20.
Ziel-Keywords (Google Ads, Österreich, 20.11.2026): energiegemeinschaft vergleich 40, beste energiegemeinschaft
österreich 20, energiegemeinschaft österreich erfahrungen 50, energiegemeinschaft erfahrungen 170,
energiegemeinschaft strompreis 70, eg austria erfahrungen 70, fronius energiegemeinschaft erfahrungen 90;
Markensuchen: fronius energiegemeinschaft 1.300, raiffeisen energiegemeinschaft 480, energiegemeinschaft für
österreich 260, energiegemeinschaft.info 260, ben beg energiegemeinschaft 210, neoom energiegemeinschaft 170,
energyfamily 390.

Faktenbasis: Jede Anbieterzeile stammt ausschließlich von der offiziellen Anbieterseite bzw. dem dort verlinkten
Tarif- oder Preisblatt, abgerufen am 20.11.2026 (URLs in "sources" und in der Tabelle). ElWG-Übergangsphase,
Netzentgelt und Mehrfachteilnahme laut energiegemeinschaften.gv.at (Faktenliste, Abschnitt "VERBINDLICH AB
20.11.2026"). OeMAG-Marktpreise laut Faktenliste.
Eigene Rechnungen (mit * gekennzeichnet): Bruttowerte = netto x 1,2 plus Servicegebühr laut Anbieter;
Grundgebühr je kWh = 48 € / 1.000 kWh.
Weggelassen mangels eigener Belege: Wien Energie, Salzburg AG ENOX.share, Kelag-Gemeinschaften, OurPower,
eFriends. Für "ben" nur die Bezeichnung "BEN - BEG" auf energiegemeinschaft.info belegt.
Interessenkonflikt offen gekennzeichnet: EBZ rechnet Energiegemeinschaften über energyfamily ab.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import article as A
from common import a


def ext(url, label):
    """Externer Quellenlink in Tabellen (nofollow, neuer Tab)."""
    return f'<a href="{url}" rel="nofollow noopener" target="_blank">{label}</a>'


Q_FRONIUS = ext("https://www.fronius-energiegemeinschaft.at/", "fronius-energiegemeinschaft.at")
Q_EGAUSTRIA = ext("https://eg-austria.at/tarife/", "eg-austria.at/tarife")
Q_EGOE = ext("https://eg-oe.at/downloads-2/konditionenuebersicht/", "eg-oe.at, Konditionen")
Q_NEOOM = ext("https://neoom.com/hubfs/2026_03_17_wsbeg_tariffblatt.pdf", "neoom Tarifblatt")
Q_BEGK = ext("https://www.beg-kaernten.at/", "beg-kaernten.at")
Q_EGINFO = ext("https://energiegemeinschaft.info/tarife/", "energiegemeinschaft.info/tarife")
Q_RAIKA = ext("https://www.raiffeisen.at/ktn/de/privatkunden/energiegenossenschaft.html",
              "raiffeisen.at, Kärnten")
Q_EF = ext("https://www.energyfamily.at/preise", "energyfamily.at/preise")
Q_EGON = ext("https://egon.energy/preise/", "egon.energy/preise")
Q_SMART = ext("https://fd.smartenergy.at/fileadmin/user_upload/downloads/Preisblatt_smartCOMMUNITY.pdf",
              "smartCOMMUNITY Preisblatt")

ARTICLE = {
    "slug": "energiegemeinschaft-vergleich",
    "path": "/energiegemeinschaft-vergleich/",
    "cluster": "Energiegemeinschaft",
    "title": "Energiegemeinschaft Vergleich 2026: Tarife, Gebühren | EBZ",
    "description": ("Energiegemeinschaft Vergleich, Stand November 2026: 10 Anbieter und Plattformen mit Bezug "
                    "8,9 bis 12,5 ct netto, Einspeisung 7 bis 10 ct, Gebühren und Bindung."),
    "eyebrow": "Energiegemeinschaft · Vergleich",
    "crumb_label": "Energiegemeinschaft Vergleich",
    "h1": "Energiegemeinschaft Vergleich 2026: 10 Anbieter und Plattformen mit Tarifen, Gebühren und Bindung",
    "lead": ("Fronius, Raiffeisen, neoom, EG Austria und Co. werben mit günstigem Gemeinschaftsstrom. Wir haben die "
             "offiziellen Tarifblätter von zehn Anbietern und Plattformen gelesen und die Werte nebeneinander "
             "gestellt, netto und brutto sauber getrennt. Ohne Ranking, denn die passende Gemeinschaft hängt von "
             "Ihrem Netzgebiet, Ihrer PV-Anlage und Ihrem Verbrauch ab."),
    "chips": [
        "Stand: <b>November 2026</b>",
        "Bezug: <b>8,9 bis 12,5 ct</b> netto",
        "Einspeisung: <b>7 bis 10 ct</b>",
        "Bis zu <b>5 Modelle</b> je Zählpunkt",
    ],
    "date_published": "2026-11-20",
    "date_modified": "2026-11-20",
    "hero_img": "eg_drohne",
    "hero_alt": "Luftaufnahme eines kleinen Dorfes zwischen Feldern und Waldrand im Abendlicht",

    "tldr": [
        "Die Bezugspreise der verglichenen Gemeinschaften liegen laut Anbietern bei 8,9 bis 12,5 Cent je kWh "
        "netto. Mit Servicegebühr und 20 % Umsatzsteuer zahlen Haushalte in den österreichweiten Gemeinschaften "
        "rund 10,7 bis 13,2 Cent brutto, Netzentgelte und Abgaben kommen wie bisher dazu.*",
        "Für eingespeisten PV-Strom zahlen die Gemeinschaften 7 bis 10 Cent je kWh. Der OeMAG-Marktpreis lag im "
        "Juli 2026 bei 6,146 Cent, im Oktober bei 14,874 Cent: Teilen bringt nicht in jedem Monat mehr.",
        "Den Netzentgelt-Rabatt gibt es nur im Nahbereich. Von Oktober bis Dezember 2026 bekommen ihn nur "
        "Mitglieder lokaler oder regionaler EEGs, österreichweite Bürgerenergiegemeinschaften (BEG) bekommen "
        "ihn nicht.",
        "Neue Zuordnungen über mehrere Netzgebiete sind laut Koordinationsstelle voraussichtlich erst ab April "
        "2027 möglich. Fragen Sie vor dem Beitritt, ob Ihr Netzbetreiber schon angebunden ist.",
        "Es gibt nicht die eine beste Energiegemeinschaft: Jeder Zählpunkt darf an bis zu 5 Bürgerenergie-Modellen "
        "teilnehmen, etwa lokal für den Rabatt und österreichweit für die Familie.",
    ],
    "kpis": [
        ("8,9 bis 12,5 ct", "Bezugspreis netto laut Anbietern"),
        ("7 bis 10 ct", "Einspeisepreis laut Anbietern"),
        ("14,874 ct", "OeMAG-Marktpreis Oktober 2026"),
        ("bis zu 5", "Bürgerenergie-Modelle je Zählpunkt"),
    ],

    "sections": [
        ("Energiegemeinschaft Vergleich: Strompreise und Gebühren im Überblick", "tabelle", f"""
<p><b>Eine Energiegemeinschaft ersetzt nur den Energieanteil Ihrer Stromrechnung.</b> Netzentgelte, Abgaben und
Steuern zahlen Sie weiter an Netzbetreiber und Lieferanten, außer Sie bekommen im Nahbereich einen Rabatt. Den
Strom, den die Gemeinschaft in einer Viertelstunde nicht liefern kann, bezieht Ihr Haushalt wie bisher von Ihrem
Lieferanten. Vergleichen Sie den Gemeinschaftspreis deshalb mit dem Energiepreis (Arbeitspreis) Ihres
Lieferanten, nicht mit dem Gesamtpreis pro kWh. Die Grundlagen zu EEG und BEG erklärt der
{a('eg', 'Leitartikel zur Energiegemeinschaft')}.</p>
{A.table(
    ["Anbieter", "Modell und Reichweite", "Bezugspreis", "Gebühren für Abnehmer", "Bindung", "Ohne eigene PV", "Quelle, Stand"],
    [
        ["Fronius Energiegemeinschaft", "BEG, österreichweit (regionsübergreifend)", "8,9 ct netto",
         "keine Mitgliedsbeiträge, keine laufenden Kosten", "keine Angabe", "ja",
         f"{Q_FRONIUS}, November 2026"],
        ["EG Austria (Graz)", "BEG österreichweit, EEG regional, dazu GEA, EVA, P2P",
         "8,95 ct exkl. Steuer, Fixpreis 2026",
         "Servicegebühr 1,00 ct (Austria) bzw. 1,20 ct (regional) je kWh, 12 € je Zählpunkt und Jahr",
         "ohne Bindung", "ja", f"{Q_EGAUSTRIA}, November 2026"],
        ["Energiegemeinschaft für Österreich (EG-OE, Verein, Mattersburg)", "BEG, Zählpunkte in ganz Österreich",
         "10,0 ct netto, 12,0 ct brutto (gültig ab 1.11.2026)",
         "Grundgebühr Bezug 0 € laut Website und Tariftabelle", "Kündigung monatlich",
         "ja", f"{Q_EGOE}, November 2026"],
        ["Bürgerenergiegemeinschaft neoom", "BEG, österreichweit, Anmeldung per App",
         "10,00 ct exkl., 12,00 ct inkl. USt",
         "Servicebeitrag 1,2 ct je kWh brutto, Betriebskosten 1,00 € je Standort und Monat, Kaution bis 50 € möglich",
         "keine Angabe", "ja", f"{Q_NEOOM}, gültig ab 1.1.2026"],
        ["BEG Kärnten", "Bürgerenergiegemeinschaft, laut Anbieter in ganz Österreich offen",
         "12,00 ct inkl. 20 % USt (10,0 ct netto), Fixpreis",
         "keine Anmelde- und keine Grundgebühr", "jederzeit kündbar", "ja",
         f"{Q_BEGK}, Stand August 2026"],
        ["energiegemeinschaft.info (ECS FlexCo)", "BEN - BEG österreichweit und regionale EEGs",
         "BEN - BEG 9,85 ct netto, EEG Privatanschluss 11,00 ct netto",
         "BEG zuzüglich Gemeinschaftsaufschlag (Höhe nicht angegeben)", "keine Angabe", "ja",
         f"{Q_EGINFO}, zuletzt angegeben: 2. Quartal 2026"],
        ["Raiffeisen Energie-Genossenschaften Kärnten", "51 regionale Genossenschaften in Kärnten",
         "12,50 ct netto vor Netzersparnis (1.10. bis 31.12.2026)",
         "Geschäftsanteil 10 €, bei Kündigung zurück", "jederzeit kündbar, Sperrfrist für Anteile", "ja",
         f"{Q_RAIKA}, Stand 1.10.2026"],
    ],
    hl_cols=(2,),
)}
<p>Alle Werte laut den offiziellen Seiten bzw. Tarifblättern der Anbieter, abgerufen am 20. November 2026.
<b>Preise ändern sich</b>, teils jedes Quartal. Wo eine Angabe fehlt, steht "keine Angabe": Fragen Sie vor dem
Beitritt nach. Ein Absatz in der Konditionenübersicht von EG-OE nennt zusätzlich 4 € Teilnahmegebühr je
Bezugszählpunkt, Website und Tariftabelle nennen 0 €: Lassen Sie sich das schriftlich bestätigen.</p>
<p><b>Netto oder brutto?</b> Private Haushalte zahlen beim Bezug in der Regel 20 % Umsatzsteuer auf den Nettopreis.
Rechnet man Servicegebühren je kWh und Umsatzsteuer ein, liegen die österreichweiten Angebote bei rund 10,7 Cent
(Fronius) bis 13,2 Cent (neoom) brutto je kWh.* Bei Raiffeisen Kärnten rechnet der Anbieter die Netzersparnis im
Nahbereich bereits ein: je nach Netzgebiet 9,07 bis 9,85 Cent netto für Privatkunden.</p>
"""),
        ("Einspeisen: Was Gemeinschaften für Ihren PV-Strom zahlen", "einspeisen", f"""
<p><b>Als Erzeuger bekommen Sie den Gemeinschaftspreis nur für die Menge, die in derselben Viertelstunde ein
anderes Mitglied verbraucht.</b> Den Rest nimmt wie bisher Ihr Einspeisevertrag ab, etwa bei der OeMAG. Gebühren
für Erzeuger fallen je kWh oder je Zählpunkt an und mindern den Erlös.</p>
{A.table(
    ["Anbieter", "Einspeisepreis", "Gebühren für Erzeuger", "Quelle"],
    [
        ["Fronius Energiegemeinschaft", "7 ct netto (PV bis 30 kWp)", "keine laufenden Kosten", Q_FRONIUS],
        ["EG Austria", "Vergütung 8,95 ct, laut Anbieter 7,75 ct Ertrag nach Servicegebühr und Steuer",
         "Servicegebühr 1,00 ct je kWh, 12 € je Zählpunkt und Jahr", Q_EGAUSTRIA],
        ["Energiegemeinschaft für Österreich", "7,0 ct exkl. USt (gültig ab 1.11.2025)",
         "4 € netto bzw. 4,80 € brutto je Einspeisezählpunkt und Monat", Q_EGOE],
        ["Bürgerenergiegemeinschaft neoom", "10,00 ct (Privat und Kleinunternehmer), Unternehmen 10,00 ct exkl. USt",
         "Servicebeitrag 1,2 ct je kWh brutto", Q_NEOOM],
        ["BEG Kärnten", "8,0 ct", "keine Grundgebühr", Q_BEGK],
        ["energiegemeinschaft.info", "BEN - BEG: 8 ct netto (6 bis 20 Uhr), 9,00 ct (20 bis 6 Uhr); "
         "EEG PV: 8,50 ct netto (6 bis 20 Uhr), 10,00 ct netto (20 bis 6 Uhr)",
         "Gemeinschaftsabschlag (Höhe nicht angegeben)", Q_EGINFO],
        ["Raiffeisen Energie-Genossenschaften Kärnten", "9,50 ct (1.10. bis 31.12.2026)",
         "einmalige Gebühr je Einspeisezählpunkt (Höhe nicht angegeben)", Q_RAIKA],
    ],
    hl_cols=(1,),
)}
<p><b>Der Vergleich mit der OeMAG fällt je nach Monat anders aus.</b> Der OeMAG-Marktpreis lag im Juli 2026 bei
6,146 Cent, im September bei 10,168 Cent und im Oktober bei 14,874 Cent je kWh. Im Juli lagen alle
Gemeinschaftspreise darüber, im Oktober alle darunter. Der Vorteil der Gemeinschaft ist ein planbarer Preis,
nicht ein garantiert höherer. Wie der OeMAG-Tarif funktioniert, steht unter
{a('/oemag-einspeisetarif/', 'OeMAG-Einspeisetarif')}.</p>
{A.box("Eine feste Grundgebühr je Einspeisezählpunkt wiegt schwer, wenn wenig Strom in der Gemeinschaft "
       "landet. Beispiel: 4 € im Monat sind 48 € im Jahr. Verkaufen Sie 1.000 kWh im Jahr in die Gemeinschaft, "
       "sinkt der Erlös dadurch um 4,8 Cent je kWh, bei 3.000 kWh um 1,6 Cent.*",
       label="Rechenbeispiel:")}
"""),
        ("Plattformen ohne eigenen Tarif: energyfamily, egon, smartCOMMUNITY", "plattformen", f"""
<p><b>Manche Namen, die beim Suchen auftauchen, sind keine Energiegemeinschaften, sondern Software für deren
Abrechnung oder Handelsplätze.</b> Den Strompreis legt dort die jeweilige Gemeinschaft fest oder die Teilnehmenden
vereinbaren ihn selbst. Für Mitglieder zählt dann der Tarif der Gemeinschaft, für Gründer die Plattformgebühr.</p>
{A.table(
    ["Plattform", "Was sie macht", "Kosten laut Anbieter", "Quelle"],
    [
        ["energyfamily (energyfamily GmbH, Amstetten)",
         "Gründung, Verwaltung und Abrechnung, rund 330 aktive Gemeinschaften, rund 15.000 registrierte Nutzer",
         "Starten und Gründen 0 €; im Betrieb 2 ct je kWh für die ersten 350.000 kWh, 1,5 ct bis 700.000 kWh, "
         "1,0 ct darüber, exkl. USt, auf in der EG verbrauchten Strom. Tarife legt die Gemeinschaft fest.",
         Q_EF],
        ["egon (E.GON GmbH)", "Plattform für Energiegemeinschaften, GEA und Peer-to-Peer",
         "1,90 € je Zählpunkt und Monat, Gründungspauschale 390 € inkl. USt, keine Mindestlaufzeit", Q_EGON],
        ["smartCOMMUNITY (Energie Steiermark Kunden GmbH, smartENERGY)",
         "Handelsplattform: Strom verschenken, teilen oder verkaufen, Preis legen die Teilnehmenden fest",
         "2,50 € je Bezugszählpunkt und Monat inkl. USt, 2,00 ct je eingespeister kWh exkl. USt, "
         "Kündigung mit 2 Wochen Frist; laut Preisblatt mit Strom- bzw. Bezugstarif von smartENERGY",
         f"{Q_SMART}, gültig ab 25.9.2025"],
    ],
    hl_cols=(2,),
)}
{A.box("EBZ Energie arbeitet bei der Abrechnung von Energiegemeinschaften mit energyfamily zusammen. "
       "energyfamily steht hier trotzdem nur mit den Angaben der eigenen Website in der Liste, nach denselben "
       "Kriterien wie alle anderen.",
       label="Transparenz:")}
<p>Für Gründer im Nahbereich lohnt der Blick auf die Gebührenmodelle: Eine Gebühr je kWh wächst mit dem
geteilten Strom, eine Gebühr je Zählpunkt bleibt fix. Wie eine Gründung abläuft, steht unter
{a('/energiegemeinschaft-gruenden/', 'Energiegemeinschaft gründen')}, die Peer-to-Peer-Variante unter
{a('/peer-to-peer-strom/', 'Peer-to-Peer-Strom')}.</p>
"""),
        ("Die Anbieter im Einzelnen: Fronius, Raiffeisen, neoom und Co.", "anbieter", f"""
<h3>Fronius Energiegemeinschaft</h3>
<p>Fronius aus Wels hat im Februar 2026 eine österreichweite Bürgerenergiegemeinschaft gegründet. Laut Fronius
beziehen Mitglieder Strom für 8,9 Cent je kWh netto und bekommen für eingespeisten Strom aus PV-Anlagen bis 30 kWp
7 Cent netto, ohne Mitgliedsbeiträge und laufende Kosten. Für die Anmeldung reicht die Zählpunktnummer, der
Netzbetreiber muss online freigeben. Einen Fronius-Wechselrichter setzt die Seite nicht voraus.</p>
<h3>Raiffeisen Energiegemeinschaft</h3>
<p>Hinter "Raiffeisen Energiegemeinschaft" stehen viele regionale Genossenschaften mit eigenen Preisen. In Kärnten
gibt es laut Raiffeisen 51 Energie-Genossenschaften, für Oktober bis Dezember 2026 mit 12,50 Cent netto Bezug vor
Netzersparnis und 9,50 Cent Einspeisung, dazu ein Geschäftsanteil von 10 €. In Oberösterreich betreut Raiffeisen
Energie laut Presseinformation vom 3. September 2026 38 Energiegemeinschaften. Die Preise legt jede Genossenschaft
selbst fest.</p>
<h3>neoom</h3>
<p>Die Bürgerenergiegemeinschaft von neoom ist österreichweit offen, die Anmeldung läuft über die neoom-App.
Strom kostet 10,00 Cent exkl. bzw. 12,00 Cent inkl. USt, für Einspeisung gibt es 10,00 Cent. Dazu kommen 1,2 Cent
Servicebeitrag je bezogener und eingespeister kWh und 1,00 € Betriebskosten je Standort und Monat. Daneben
betreibt neoom lokale Gemeinschaften (KLUUB), die vor Ort gegründet werden.</p>
<h3>EG Austria und Energiegemeinschaft für Österreich</h3>
<p>Die Namen sind leicht zu verwechseln. <b>EG Austria</b> sitzt in Graz und bietet BEG, regionale EEG und weitere
Modelle an, mit 8,95 Cent Fixpreis für 2026. Die <b>Energiegemeinschaft für Österreich</b> (EG-OE) ist ein Verein in
Mattersburg mit 10 Cent netto Bezug und 7 Cent Einspeisung. EG-OE wirbt mit einem stabilen Preis für 20 Jahre;
laut Konditionenübersicht können beide Seiten den Vertrag aber monatlich kündigen, und je Zählpunkt sind höchstens
100.000 kWh im Jahr erlaubt.</p>
<h3>energiegemeinschaft.info und BEN - BEG</h3>
<p>Auf energiegemeinschaft.info (ECS FlexCo) heißt die österreichweite Gemeinschaft "BEN - BEG", daneben gibt es
regionale EEGs. Die Tarife werden quartalsweise angepasst, zuletzt angegeben ist das 2. Quartal 2026 mit 9,85 Cent
netto für BEN - BEG und getrennten Tag- und Nachtpreisen für die Einspeisung.</p>
<h3>BEG Kärnten</h3>
<p>Die BEG Kärnten hat ihren Sitz in Kärnten, steht laut eigener Seite aber in ganz Österreich offen. Sie nennt
12,00 Cent inkl. USt als Fixpreis für den Bezug, 8,0 Cent Einspeisevergütung und keine Grundgebühr.</p>
{A.cta("Welche Gemeinschaft passt zu Ihrer PV-Anlage?",
       "Wir prüfen Netzebene und Netzbetreiber Ihres Zählpunkts und zeigen, ob sich lokal, österreichweit oder "
       "beides lohnt. Eigene Stromtarife verkaufen wir nicht.",
       secondary=("eg_privat", "Energiegemeinschaft mit EBZ"))}
"""),
        ("Checkliste: Worauf Sie beim Vergleich achten", "checkliste", f"""
<ul>
  <li><b>Netzentgelt-Rabatt nur im Nahbereich:</b> Bisher minus 57 % lokal und minus 28 % regional beim
  Netzarbeitspreis. Von Oktober bis Dezember 2026 gilt das nur für Mitglieder lokaler oder regionaler EEGs. Für
  BEG, Peer-to-Peer und Eigenversorgung im Nahbereich ist die Ausweitung ab 1.1.2027 mit der neuen
  Netzentgelt-Verordnung vorgesehen, die Höhe legt die E-Control fest. Österreichweites Teilen bringt keinen
  Rabatt. Details: {a('/energiegemeinschaft-netzkosten/', 'Netzkosten in der Energiegemeinschaft')}.</li>
  <li><b>Einspeisepreis gegen OeMAG halten:</b> 7 bis 10 Cent fix gegen 6,146 Cent (Juli), 10,168 Cent (September)
  und 14,874 Cent (Oktober 2026) bei der OeMAG.</li>
  <li><b>Bindung und Kündigung:</b> Mehrere Anbieter nennen monatliche Kündigung oder keine Bindung, andere machen
  keine Angabe. Langfristige Preisversprechen gelten nur so weit, wie sie im Vertrag stehen.</li>
  <li><b>Alle Gebühren zusammenzählen:</b> Servicegebühr je kWh, Grundgebühr je Zählpunkt, Mitgliedsbeitrag,
  Geschäftsanteil, Kaution. Rechnen Sie auf Ihre erwartete Gemeinschaftsmenge, nicht auf den Jahresverbrauch.</li>
  <li><b>Netto und brutto trennen:</b> Bezugspreise sind oft netto angegeben, Haushalte zahlen 20 % USt dazu.</li>
  <li><b>Abrechnung:</b> Monatlich per E-Mail, App oder Portal? Die Daten des Netzbetreibers kommen laut EG-OE rund
  16 Tage nach Monatsende.</li>
  <li><b>Smart Meter und Datenschutz:</b> Nötig ist ein Smart Meter mit Viertelstundenwerten und Ihre
  Datenfreigabe beim Netzbetreiber. Mit Opt-out ist bei smartCOMMUNITY keine Teilnahme möglich, siehe
  {a('/smart-meter-opt-out/', 'Smart Meter Opt-out')}.</li>
  <li><b>Netzgebiet angebunden?</b> Die Teilnahme klappt nur, wenn Ihr Netzbetreiber die Gemeinschaft
  registriert hat und die Übergangsregeln es erlauben (siehe unten).</li>
</ul>
"""),
        ("Energiegemeinschaft Erfahrungen: Was in der Praxis zählt", "erfahrungen", f"""
<p><b>Die häufigste Enttäuschung ist eine zu hohe Erwartung an die Menge.</b> Die Gemeinschaft liefert nur, was in
derselben Viertelstunde verfügbar ist, den Rest liefert Ihr Lieferant. Laut EG-OE wird der Strom dynamisch nach dem
gemessenen Verbrauch aufgeteilt: Wer in einer Viertelstunde 25 % des Gemeinschaftsverbrauchs hat, bekommt 25 % des
eingespeisten Stroms.</p>
<ul>
  <li><b>Drei Rechnungen statt einer:</b> Netzbetreiber, Lieferant für den Reststrom und Gemeinschaft.</li>
  <li><b>Kein Lieferantenwechsel nötig:</b> Darauf weisen etwa EG Austria, EG-OE und energiegemeinschaft.info
  ausdrücklich hin, der bestehende Liefervertrag deckt den Reststrom.</li>
  <li><b>Zeitversatz:</b> Abrechnung meist monatlich, mit einigen Wochen Verzögerung.</li>
  <li><b>Kaution und Lastschrift:</b> neoom behält sich bis zu 50 € Kaution je Bezugszählpunkt vor, EG-OE zieht per
  SEPA-Lastschrift ein.</li>
</ul>
<p>Weitere Stolpersteine sammelt der Artikel {a('/energiegemeinschaft-nachteile/', 'Nachteile einer Energiegemeinschaft')},
die Schritte zum Beitritt stehen unter {a('/energiegemeinschaft-beitreten/', 'Energiegemeinschaft beitreten')}.
Mit dem {a('eg_rechner', 'Energiegemeinschaft-Rechner')} spielen Sie Ihre eigenen Mengen durch.</p>
"""),
        ("Mehrfachteilnahme: Warum es nicht die eine beste Energiegemeinschaft gibt", "mehrfach", f"""
<p><b>Seit dem ElWG darf jede Erzeugungs- oder Verbrauchsanlage an bis zu 5 Bürgerenergie-Modellen gleichzeitig
teilnehmen.</b> Die Summe der Teilnahmefaktoren je Zählpunkt darf 100 % nicht überschreiten, der Faktor lässt sich
einmal täglich ändern, ab 2028 voraussichtlich mehrmals täglich.</p>
<p>Statt den einen besten Anbieter zu suchen, kombinieren Sie besser: eine lokale EEG für den Netzentgelt-Rabatt
und eine österreichweite Gemeinschaft für den Strom, den Sie mit Familie in einem anderen Bundesland teilen wollen.
Wie das Modell dahinter funktioniert, erklärt der Artikel
{a('/buergerenergiegemeinschaft/', 'Bürgerenergiegemeinschaft')}. Im Mehrparteienhaus kommt die
{a('/gemeinschaftliche-erzeugungsanlage/', 'gemeinschaftliche Erzeugungsanlage')} dazu.</p>
"""),
        ("Übergangsphase nach dem ElWG: Was bis April 2027 gilt", "elwg", f"""
<p><b>Eine BEG darf sich über ganz Österreich erstrecken.</b> In der Übergangsphase seit Oktober 2026 lassen sich
neue Zuordnungen laut Koordinationsstelle vorübergehend nur mit Zählpunkten beim selben Netzbetreiber umsetzen,
netzübergreifend (zum Beispiel Kärnten und Wien) voraussichtlich ab April 2027. Ob bereits registrierte
Gemeinschaften davon betroffen sind, sagt die Koordinationsstelle nicht. Fragen Sie deshalb vor dem Beitritt, ob
Ihr Netzgebiet schon angebunden ist.</p>
<ul>
  <li><b>Bestehende Gemeinschaften</b> wurden mit 1. Oktober 2026 ins neue System überführt.</li>
  <li><b>Abgaben:</b> Den Entfall des Erneuerbaren-Förderbeitrags und die Befreiung von der Elektrizitätsabgabe gibt
  es derzeit nur in der EEG.</li>
  <li><b>Netzentgelt ab 2027:</b> Die Höhe für lokale und regionale BEG, P2P und EVA legt die E-Control per
  Verordnung fest.</li>
</ul>
<p>Was das ElWG sonst ändert, steht unter {a('/elwg-beschluss-oesterreich/', 'ElWG-Beschluss Österreich')}.</p>
"""),
        ("Fazit: Tarif, Reichweite und Gebühren zusammen lesen", "fazit", f"""
<p>Die verglichenen Gemeinschaften liegen beim Bezug zwischen 8,9 und 12,5 Cent netto, bei der Einspeisung zwischen
7 und 10 Cent. Den Unterschied machen oft die Gebühren und die Frage, ob Sie im Nahbereich einen Netzrabatt
bekommen. Wer eine PV-Anlage hat, sollte die Gemeinschaft als Ergänzung zur OeMAG sehen, nicht als Ersatz.</p>
<p>EBZ Energie verkauft keinen Strom und hat keine eigenen Gemeinschaftstarife. Wir planen und montieren die
{a('photovoltaik', 'Photovoltaikanlage')} in Kärnten und der Steiermark, binden sie an eine Gemeinschaft an
(Abrechnung über energyfamily) und helfen bei der Gründung im Nahbereich, auch für
{a('eg_gewerbe', 'Betriebe und Gemeinden')}. Umgesetzte Anlagen zeigen unsere {a('referenzen', 'Referenzen')}.</p>
<p><small>*Eigene Umrechnungen auf Basis der Anbieterangaben: Brutto = Nettopreis mal 1,2 plus Servicegebühr laut
Anbieter, ohne Grundgebühren, Netzentgelte und Abgaben. Alle Anbieterwerte Stand November 2026 (abgerufen am
20.11.2026), Preise ändern sich. Keine vollständige Marktübersicht, keine Wertung.</small></p>
{A.cta("PV-Anlage plus Energiegemeinschaft, ehrlich gerechnet",
       "Wir rechnen Eigenverbrauch, OeMAG und Gemeinschaft für Ihre Anlage durch und binden Sie an, "
       "wo es sich lohnt.",
       primary=("kontakt", "Kostenlose Beratung"), secondary=("eg_privat", "Energiegemeinschaft mit EBZ"))}
"""),
    ],

    "partner": {
        "h2": "Photovoltaik und Energiegemeinschaft aus einer Hand",
        "toc": "Ihr Partner: EBZ Energie",
        "text": ("EBZ Energie aus Villach plant und installiert Photovoltaik, Speicher, Wärmepumpen und "
                 "Energiemanagement in Kärnten und der Steiermark, mit zertifizierten Fachkräften und einem festen "
                 "Ansprechpartner von der Planung bis zur Übergabe. Bei der Energiegemeinschaft nehmen wir Sie in "
                 "eine bestehende Gemeinschaft auf oder bauen mit Ihnen eine eigene im Nahbereich auf, abgerechnet "
                 "über unseren Partner energyfamily. Strom verkaufen wir nicht."),
        "grid": [
            ("Netzebene geprüft", "Lokal, regional oder österreichweit: Wir klären, was für Ihren Zählpunkt geht."),
            ("Ehrlicher Vergleich", "Gemeinschaft und OeMAG nebeneinander, mit Ihren Mengen."),
            ("Anlage plus Anbindung", "PV, Speicher und EMS so geplant, dass mehr Strom geteilt werden kann."),
            ("Kostenlose Erstberatung", "Telefonisch oder vor Ort in Kärnten und der Steiermark."),
        ],
    },

    "faq": [
        ("Welche Energiegemeinschaft ist die beste in Österreich?",
         "Eine beste gibt es nicht, weil Netzgebiet, PV-Anlage und Verbrauch entscheiden. Im Nahbereich bringt eine "
         "lokale oder regionale EEG den Netzentgelt-Rabatt, österreichweite BEGs bieten Bezugspreise von 8,9 bis "
         "10 Cent netto ohne Rabatt. Da jeder Zählpunkt an bis zu 5 Modellen teilnehmen darf, lassen sich beide "
         "kombinieren."),
        ("Wie hoch sind die Kosten für eine Energiegemeinschaft in Österreich?",
         "Laut den verglichenen Anbietern 8,9 bis 12,5 Cent je kWh netto für den Gemeinschaftsstrom, dazu je nach "
         "Anbieter 0 bis 1,2 Cent Servicegebühr je kWh, eine Grundgebühr, ein Mitgliedsbeitrag (zum Beispiel 12 € "
         "im Jahr) oder ein Geschäftsanteil von 10 €. Netzentgelte und Abgaben zahlen Sie weiter. Mehr dazu unter "
         "Energiegemeinschaft Kosten."),
        ("Was kostet der Strom bei der Fronius Energiegemeinschaft?",
         "Laut Fronius 8,9 Cent je kWh netto, ohne Mitgliedsbeiträge und laufende Kosten (Stand November 2026). "
         "Für Einspeisung aus PV-Anlagen bis 30 kWp zahlt Fronius 7 Cent netto. Die Gemeinschaft ist eine "
         "österreichweite BEG, einen Netzentgelt-Rabatt gibt es damit nicht."),
        ("Was zahlt die Raiffeisen Energiegemeinschaft?",
         "Das hängt von der Genossenschaft ab, jede legt ihre Preise selbst fest. In Kärnten gelten laut Raiffeisen "
         "von Oktober bis Dezember 2026 12,50 Cent netto Bezug vor Netzersparnis und 9,50 Cent Einspeisung, dazu "
         "ein Geschäftsanteil von 10 €, der bei Kündigung zurückkommt."),
        ("Bringt Einspeisen in die Energiegemeinschaft mehr als die OeMAG?",
         "Nicht in jedem Monat. Die verglichenen Gemeinschaften zahlen 7 bis 10 Cent fix, die OeMAG zahlte im Juli "
         "2026 6,146 Cent und im Oktober 14,874 Cent. In die Gemeinschaft geht ohnehin nur die Menge, die andere "
         "Mitglieder gleichzeitig verbrauchen, der Rest bleibt beim bisherigen Einspeisevertrag."),
        ("Bekomme ich in einer österreichweiten Energiegemeinschaft einen Netzentgelt-Rabatt?",
         "Nein. Der Rabatt gilt nur im Nahbereich, von Oktober bis Dezember 2026 nur für Mitglieder lokaler oder "
         "regionaler EEGs. Für BEG im Nahbereich ist die Ausweitung ab 1. Jänner 2027 mit der neuen "
         "Netzentgelt-Verordnung vorgesehen, für österreichweites Teilen gibt es keinen Rabatt."),
        ("Kann ich mit der Tante in Wien eine Energiegemeinschaft bilden?",
         "Grundsätzlich ja, über eine österreichweite Bürgerenergiegemeinschaft oder einen Peer-to-Peer-Vertrag. In "
         "der Übergangsphase seit Oktober 2026 lassen sich neue Zuordnungen laut Koordinationsstelle vorerst nur "
         "beim selben Netzbetreiber umsetzen, netzübergreifend voraussichtlich ab April 2027."),
        ("Muss ich für eine Energiegemeinschaft den Stromanbieter wechseln?",
         "Nein. Anbieter wie EG Austria, EG-OE und energiegemeinschaft.info weisen ausdrücklich darauf hin, dass Ihr "
         "Liefervertrag bestehen bleibt und den Reststrom deckt. Die Gemeinschaft liefert nur, was in der jeweiligen "
         "Viertelstunde verfügbar ist. Voraussetzung ist ein Smart Meter mit "
         "Viertelstundenwerten und Ihre Datenfreigabe beim Netzbetreiber."),
    ],

    "author_note": ("Mario Zintl führt die EBZ Energie GmbH in Villach. EBZ plant und installiert Photovoltaik in "
                    "Kärnten und der Steiermark und bindet Anlagen an Energiegemeinschaften an; bei der Abrechnung "
                    "arbeitet EBZ mit energyfamily zusammen. Eigene Stromtarife hat EBZ nicht. Die Anbieterwerte "
                    "stammen von den offiziellen Seiten (Stand November 2026) und ändern sich laufend. Keine Rechts- "
                    "oder Steuerberatung."),
    "sources": [
        ("Koordinationsstelle Energiegemeinschaften: FAQs zum ElWG",
         "https://energiegemeinschaften.gv.at/faqs-zum-elwg/"),
        ("Koordinationsstelle Energiegemeinschaften: Mehrfachteilnahme",
         "https://energiegemeinschaften.gv.at/mehrfachteilnahme/"),
        ("OeMAG: Marktpreis", "https://www.oem-ag.at/de/marktpreis/"),
        ("Fronius Energiegemeinschaft", "https://www.fronius-energiegemeinschaft.at/"),
        ("Fronius: Presseinformation vom 3.2.2026",
         "https://www.fronius.com/de-at/austria/solarenergie/ueber-uns/presse/fronius-gruendet-eigene-energiegemeinschaft-03022026"),
        ("EG Austria: Tarife", "https://eg-austria.at/tarife/"),
        ("Energiegemeinschaft für Österreich: Konditionen Verbraucher, gültig ab 1.11.2026",
         "https://eg-oe.at/wp-content/uploads/Konditionen_Verbraucher_EG-OE_Grundgebuehr_0_EUR_2026.pdf"),
        ("Energiegemeinschaft für Österreich: Konditionen Erzeuger, gültig ab 1.11.2025",
         "https://eg-oe.at/wp-content/uploads/Konditionen_Erzeuger_EG-OE_10-2025-1.pdf"),
        ("neoom: Bürgerenergiegemeinschaft", "https://neoom.com/loesungen/beg"),
        ("neoom: Tarifblatt Bürgerenergiegemeinschaft, gültig ab 1.1.2026",
         "https://neoom.com/hubfs/2026_03_17_wsbeg_tariffblatt.pdf"),
        ("BEG Kärnten", "https://www.beg-kaernten.at/"),
        ("energiegemeinschaft.info: Tarife", "https://energiegemeinschaft.info/tarife/"),
        ("Raiffeisen Kärnten: Energie-Genossenschaft",
         "https://www.raiffeisen.at/ktn/de/privatkunden/energiegenossenschaft.html"),
        ("Raiffeisen OÖ: Presseinformation Energiegemeinschaften, 3.9.2026",
         "https://www.raiffeisen.at/ooe/rlb/de/meine-bank/presse/pressearchiv-2026/energiegemeinschaften.html"),
        ("energyfamily: Preise", "https://www.energyfamily.at/preise"),
        ("egon: Preise", "https://egon.energy/preise/"),
        ("smartENERGY: Preisblatt smartCOMMUNITY, gültig ab 25.9.2025",
         "https://fd.smartenergy.at/fileadmin/user_upload/downloads/Preisblatt_smartCOMMUNITY.pdf"),
    ],
    "related": [
        ("/energiegemeinschaft-beitreten/", "Energiegemeinschaft beitreten: Schritt für Schritt"),
        ("/energiegemeinschaft-kosten/", "Was eine Energiegemeinschaft kostet"),
        ("/buergerenergiegemeinschaft/", "Bürgerenergiegemeinschaft: österreichweit Strom teilen"),
        ("eg_privat", "Energiegemeinschaft mit EBZ: PV-Anlage plus Anbindung"),
    ],
    "cta": {
        "h3": "Energiegemeinschaft passend zur PV-Anlage",
        "text": "Wir prüfen Ihren Zählpunkt und zeigen, welche Gemeinschaft für Sie in Frage kommt.",
        "primary": ("kontakt", "Kostenlose Beratung"),
    },
    "final_h2": "Gemeinschaft, OeMAG oder beides: ehrlich gerechnet",
    "final_text": ("Kostenlose Erstberatung zu Photovoltaik, Speicher und Energiegemeinschaft, mit "
                   "transparenten Zahlen und einem Ansprechpartner aus Villach."),
}
