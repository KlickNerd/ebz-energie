"""Standortseite Photovoltaik Klagenfurt (/photovoltaik-klagenfurt/), Slug-Key pv_klagenfurt.

Neue Seite (10.10.2026), optimiert fuer ZWEI Themen am Ort: Photovoltaik (primaer) und Waermepumpe
(sekundaer), siehe build/pages/README_standort.md. Briefing: build/seo/standort_klagenfurt.json/.md.
Primaer "photovoltaik klagenfurt" (50/Monat AT), sekundaer "waermepumpe klagenfurt" (20),
"pv anlage klagenfurt" (10), "solar klagenfurt" (10), "photovoltaik foerderung klagenfurt" (10).

EBZ hat KEINEN Standort in Klagenfurt: Firmensitz nur Triglavstrasse 15, 9500 Villach. Formulierung
durchgehend "Fachbetrieb aus Villach, vor Ort in Klagenfurt"; die FAQ sagt das ausdruecklich.

Lokale Fakten, alle am 10.10.2026 selbst abgerufen:
- Netzbetreiber Stadt: Energie Klagenfurt GmbH (EKG, Stadtwerke Klagenfurt), NICHT Kaernten Netz.
  Antragsportal pv.stw.at; Antrag stellt der Kunde selbst, Elektrofachbetrieb kann bevollmaechtigt
  werden; Angebot mit genehmigter netzwirksamer Einspeiseleistung (kW), Modulleistung (kWp) frei;
  Speicher meldepflichtig; Kleinsterzeugungsanlage bis 0,8 kW nur Meldung; Fertigstellung erfasst der
  Elektrobetrieb im Portal; Inbetriebnahme erst nach Freigabe und Netzzugangsvertrag; Ferraris-Zaehler
  wird getauscht, beim Smart Meter zweiter Messkanal; Abnehmervertrag vor Inbetriebnahme.
  Quelle: https://www.stw.at/privat/energie/stromnetz/photovoltaikanlagen/
- Umland: KNG-Kaernten Netz GmbH ist Verteilernetzbetreiber in Kaernten
  (https://kaerntennetz.at/ueber-uns.htm, https://kaerntennetz.at/pv.htm). Welche Adresse im Umland zu
  welchem Netz gehoert, ist NICHT gemeindeweise belegt: Seite verweist auf Netzgebietskarte/Stromrechnung.
- Einspeisetarif "SonnenCity Klagenfurt": 7 Cent je kWh netto
  (https://www.stw.at/privat/energie/strom/sonnencity-klagenfurt/). Preis kann sich aendern: bei der
  monatlichen OeMAG-Pflege mitpruefen.
- Baurecht: Mitteilungspflicht nach § 7 Abs. 1 lit. a Z 20 K-BO 1996 idF LGBl. Nr. 11/2026 (bauliche
  Anlagen, die erneuerbare Energie erzeugen oder elektrische Energie speichern); Mitteilung schriftlich
  vor Beginn (Katastralgemeinde, Grundstuecksnummer, Kurzbeschreibung); Vollendung binnen zwei Wochen
  melden, bei Speichern Lage und technische Daten. Quellen: Formular Magistrat Villach zur selben
  Bestimmung (https://villach.at/getmedia/fe3178f4-230a-4056-871d-d9412d2329ff/Mitteilung_P7_KBO1996.pdf.aspx),
  Gesetzestext-Wiedergabe forum-media.at (Fassung 21.02.2026); RIS selbst war nicht abrufbar (Bot-Schutz).
  Baubehoerde Stadt: Magistrat der Landeshauptstadt Klagenfurt, Abt. Baurecht (Formularkopf, allerdings
  altes Formular mit ueberholter 16-m2-Grenze: https://stw.at/wp-content/uploads/2024/03/mitteilung_an_baupolizeit.pdf).
  Gemeinsam mit bewilligungspflichtigem Umbau laeuft die PV im Bauverfahren mit (Kundmachung Velden 07.04.2026).
- Sonnenstunden: GeoSphere Austria, Station Klagenfurt Flughafen (ID 48), Jahressummen so_h, Datensatz
  klima-v2-1y: Mittel 2015 bis 2024 = 2.119 h (min 1.902 h 2024, max 2.278 h 2017); 1992 bis 2020 = 2.074 h.
  https://dataset.api.hub.geosphere.at/v1/station/historical/klima-v2-1y?parameters=so_h&station_ids=48
- Ertrag: PVGIS 5.3 (EU-Kommission, JRC), SARAH3 2005 bis 2023, 46.624 N / 14.308 O, 1 kWp, 14 % Verluste,
  hinterlueftet: Sued 30 Grad 1.240 kWh/kWp, Ost 25 Grad 993, West 25 Grad 1.008.
  https://re.jrc.ec.europa.eu/api/v5_3/PVcalc?lat=46.624&lon=14.308&peakpower=1&loss=14&angle=30&aspect=0
- Fernwaerme Stadtwerke Klagenfurt: 90,51 % erneuerbar (Bezugszeitraum 2025, TUeV-geprueft laut STW),
  Anschlussmoeglichkeit adressgenau pruefbar: https://www.stw.at/privat/energie/fernwaerme/unsere-fernwaerme/
- Klimaziel Stadt: Teil der EU-Cities-Mission seit 28.04.2022, bilanzielle Klimaneutralitaet bis 2030:
  https://www.klagenfurt.at/stadtservice/klima-umwelt/klimaschutz

Mangels Quelle WEGGELASSEN: Solarpotenzialkataster KAGIS (ktn.gv.at/kagis.ktn.gv.at nicht erreichbar),
eigene PV-/Speicher-/Heizungstausch-Foerderung der Stadt Klagenfurt (auf klagenfurt.at und stw.at keine
gefunden, Seite sagt nur "uns nicht bekannt"), Kelag-Waermepumpen-Praemie (gilt fuer Kelag-Stromkunden,
hier nicht selbst abgerufen), Entfernungen/Fahrzeiten, Zuordnung einzelner Umlandgemeinden zu einem Netz.

Waermepumpe: Zahlen nur aus build/pages/waermepumpe.py (12.000 bis 22.000 EUR, Altbau 15.000 bis
28.000 EUR, 1 kWh Strom -> 4 bis 5 kWh Waerme, Beispielhaus 12.000 kWh / JAZ 4). Foerderung wie auf
/photovoltaik-villach/ (Vorgabe Koordinator): Bund ausgeschoepft, Land Kaernten 3.000 EUR Pauschale
2026 (KEM-Infoblatt "Foerderungen 2026" auf maria-saal.gv.at und STW-Blog, abgerufen 10.10.2026; die 35 % mit
6.000 EUR Obergrenze galten nur bis 31.12.2025).

Bilder: kein Klagenfurt-Motiv im Repo. Hero = Referenz Krumpendorf am Woerthersee (echtes Projekt im
Einzugsgebiet, Bild und Zahlen gehoeren zusammen), sonst generische Szenen mit ehrlichen Alt-Texten.
Kein Mario-Block (keine belegten Klagenfurt-Aussagen von ihm). Keine Foerderfristen auf der Seite.
"""

if __name__ == "__main__":  # Direktaufruf: build/ in den Suchpfad legen (build_all setzt ihn sonst)
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common import IMG, NAP, CLAIMS, faq_jsonld, u, a, tel_link, write_page, load_reviews, standorte, standort_schema
from layout import page
import components as C

PATH = "/photovoltaik-klagenfurt/"
TITLE = "Photovoltaik Klagenfurt: PV-Anlage und Wärmepumpe | EBZ"
DESC = ("Photovoltaik und Wärmepumpe in Klagenfurt: Planung, Speicher, Montage, Netzantrag bei der "
        "Energie Klagenfurt und Förderung Kärnten. 4,9 Sterne, 300+ Projekte.")

HERO_IMG = IMG["ref_krumpendorf"]
REF_KRUMPENDORF = "/referenzen/projekt-mehrparteienhaus-krumpendorf/"

STADTTEILE = ("Innere Stadt, Annabichl, St. Peter, St. Ruprecht, St. Martin mit Waidmannsdorf, Viktring, "
              "Wölfnitz, Hörtendorf und Welzenegg")
UMLAND = ("Krumpendorf, Pörtschach, Maria Wörth, Keutschach, Moosburg, Maria Saal, Magdalensberg, "
          "Poggersdorf, Grafenstein, Ebenthal, Maria Rain, Köttmannsdorf und Ferlach")
# Nachbar-Standortseiten: werden nur verlinkt, wenn die Seitenquelle schon existiert.
NACHBARN = ("pv_villach", "pv_st_veit", "pv_feldkirchen", "pv_voelkermarkt", "pv_wolfsberg")

FAQ = [
    ("Wer ist in Klagenfurt der Netzbetreiber für meine Photovoltaikanlage?",
     "Im Stromnetz der Stadt Klagenfurt ist es die Energie Klagenfurt GmbH aus der Gruppe der Stadtwerke Klagenfurt, "
     "nicht die Kärnten Netz GmbH. Den Antrag stellen Sie als Anschlussinhaber im Antragsportal der Stadtwerke "
     "(pv.stw.at), den Fachbetrieb können Sie dort bevollmächtigen. Außerhalb dieses Netzgebiets ist in Kärnten in der "
     "Regel die Kärnten Netz GmbH zuständig. Welches Netz zu Ihrer Adresse gehört, steht auf Ihrer Stromrechnung "
     "(Stand Oktober 2026)."),
    ("Brauche ich in Klagenfurt eine Baugenehmigung für eine PV-Anlage auf dem Dach?",
     "In der Regel nicht. Nach § 7 Abs. 1 lit. a Z 20 der Kärntner Bauordnung sind Anlagen, die erneuerbare Energie "
     "erzeugen oder elektrische Energie speichern, mitteilungspflichtig: Die Baubehörde wird vor Beginn schriftlich "
     "informiert, im Stadtgebiet ist das der Magistrat der Landeshauptstadt Klagenfurt, im Umland die jeweilige "
     "Gemeinde. Flächenwidmung, Bebauungsplan und Ortsbild sind trotzdem einzuhalten, die Fertigstellung wird "
     "gemeldet. Sonderfälle klären wir vorab mit der Behörde."),
    ("Was kostet eine PV-Anlage mit Speicher und Montage in Klagenfurt?",
     "Eine Komplettanlage mit rund 10 kWp und Speicher kostet rund 15.000 bis 22.000 Euro vor Förderung, inklusive "
     "Montage und Inbetriebnahme (EBZ-Richtpreis, Stand Oktober 2026). Davon gehen 3.000 Euro Landespauschale Kärnten "
     "und der Zuschuss des Bundes ab. Eine Finanzierung ist ab 147 Euro im Monat* möglich, die Anlage gehört Ihnen "
     "dabei ab dem ersten Tag. Den genauen Preis nennt Ihr Fixangebot nach dem Termin vor Ort."),
    ("Wie viel Strom erzeugt eine Photovoltaikanlage in Klagenfurt?",
     "Das EU-Werkzeug PVGIS rechnet für Klagenfurt mit rund 1.240 kWh je kWp und Jahr bei Südausrichtung und 30 Grad "
     "Neigung und mit rund 1.000 kWh je kWp auf Ost- oder Westdächern mit 25 Grad*. Eine 10-kWp-Anlage liefert damit "
     "rund 10.000 bis 12.400 kWh im Jahr. An der Messstation Klagenfurt Flughafen wurden 2015 bis 2024 im Schnitt "
     "2.119 Sonnenstunden pro Jahr gemessen (GeoSphere Austria). Verschattung durch Gauben, Bäume oder Nachbarhäuser "
     "rechnen wir im 3D-Belegplan für Ihr Dach ein."),
    ("Gibt es eine Photovoltaik-Förderung der Stadt Klagenfurt?",
     "Eine eigene PV-Förderung der Stadt Klagenfurt ist uns nicht bekannt (Stand Oktober 2026). Für Klagenfurter "
     "Haushalte gelten die Programme von Land und Bund: 3.000 Euro Landespauschale Kärnten für eine neue Anlage ab "
     "5 kWp mit Speicher ab 5 kWh, 1.000 Euro für die Speicher-Nachrüstung, dazu vom Bund 150 Euro je kWp bis 10 kWp "
     "und 150 Euro je kWh Speicher. Welche Programme gerade offen sind, steht auf unserer Förderseite."),
    ("Wer nimmt in Klagenfurt meinen überschüssigen Sonnenstrom ab?",
     "Laut Energie Klagenfurt brauchen Sie schon vor der Inbetriebnahme einen Vertrag mit einem Abnehmer. Zur Wahl "
     "stehen die OeMAG (Marktpreis September 2026: 10,168 Cent je kWh, im Juli 6,146 Cent, der Wert schwankt "
     "monatlich), Energieversorger mit eigenem Einspeisetarif, etwa die Stadtwerke Klagenfurt mit SonnenCity "
     "Klagenfurt (7 Cent je kWh netto laut stw.at, Stand Oktober 2026), oder eine Energiegemeinschaft. Am meisten "
     "bringt jede Kilowattstunde, die Sie selbst verbrauchen."),
    ("Was kostet eine Wärmepumpe in Klagenfurt, und passt sie zur Photovoltaik?",
     "Eine Luft-Wasser-Wärmepumpe kostet im Einfamilienhaus rund 12.000 bis 22.000 Euro vor Förderung inklusive "
     "Montage, im Altbau mit Anpassungen 15.000 bis 28.000 Euro*. Ein Beispielhaus mit 12.000 kWh Wärmebedarf braucht "
     "bei Jahresarbeitszahl 4 rund 3.000 kWh Strom im Jahr*. Eine 10-kWp-Anlage in Klagenfurt erzeugt rund 10.000 bis "
     "12.400 kWh*, im Winter allerdings weniger, als die Heizung braucht. Warmwasser und Übergangszeit laufen "
     "weitgehend mit eigenem Strom."),
    ("Fernwärme oder Wärmepumpe: Was ist in Klagenfurt sinnvoll?",
     "Prüfen Sie zuerst, ob Ihre Adresse an die Fernwärme der Stadtwerke Klagenfurt angeschlossen werden kann; laut "
     "Stadtwerken stammte sie 2025 zu 90,51 Prozent aus erneuerbarer Energie. Wo kein Anschluss möglich ist, im "
     "Einfamilienhaus am Stadtrand oder in den Umlandgemeinden, ist die Wärmepumpe meist die naheliegende Lösung, "
     "am besten zusammen mit Photovoltaik. Wir rechnen Ihnen das für Ihr Haus durch."),
    ("Welche Förderung gibt es für eine Wärmepumpe in Klagenfurt?",
     "Beim Bund ist die Förderung für den Heizungstausch ausgeschöpft, neue Registrierungen sind derzeit nicht "
     "möglich. Das Land Kärnten zahlt 2026 eine Pauschale von 3.000 Euro für den Wechsel zur Wärmepumpe im Eigenheim; ob "
     "das Budget reicht und welche Voraussetzungen für Ihr Haus gelten, klären wir vor dem Angebot. Die PV-Anlage dazu wird "
     "getrennt gefördert. Der aktuelle Stand steht auf unserer Förderseite, eine erste Zahl liefert der Förderrechner."),
    ("Ist eine Wärmepumpe in Klagenfurt genehmigungspflichtig?",
     "Die Kärntner Bauordnung führt Anlagen, die erneuerbare Energie erzeugen, als mitteilungspflichtig; dazu zählt "
     "auch Umgebungsenergie, die Quelle der Luft-Wasser-Wärmepumpe. Ob für Ihr Gerät die Mitteilung genügt und wo "
     "die Außeneinheit wegen des Schalls stehen darf, klären wir vor der Montage mit Magistrat oder Gemeinde. Eine "
     "Grundwasser-Wärmepumpe braucht zusätzlich eine wasserrechtliche Bewilligung."),
    ("Hat EBZ Energie ein Büro in Klagenfurt?",
     "Nein. Unser Firmensitz ist die Triglavstraße 15 in 9500 Villach. Für die Beratung kommen wir zu Ihnen nach "
     "Klagenfurt oder ins Umland, weil wir Dach, Zählerschrank und auf Wunsch den Heizraum gleich mit aufnehmen. "
     "Erreichbar sind wir Montag bis Freitag von 10:00 bis 20:00 Uhr, telefonisch oder über das Formular."),
]


def build():
    rating, count, reviews = load_reviews()
    bew = f"{count} Bewertungen" if count else "echten Bewertungen"
    nachbarn = [(k, f"Photovoltaik in {n}") for k, n in standorte(land="ktn", ohne="pv_klagenfurt") if k in NACHBARN]
    body = "".join([
        C.hero(
            eyebrow="Photovoltaik und Wärmepumpe Klagenfurt",
            h1="Photovoltaik in Klagenfurt: PV-Anlage, Speicher und Wärmepumpe vom Fachbetrieb aus Villach",
            lead=("Sonnenstrom für Klagenfurt am Wörthersee, geplant von einem Kärntner Fachbetrieb: EBZ Energie sitzt "
                  "in Villach und kommt zur Beratung zu Ihnen, ins Stadtgebiet genauso wie nach Krumpendorf, Pörtschach, "
                  "Ebenthal oder Maria Saal. Wir prüfen Dach, Zählerschrank und Verbrauch, begleiten den Netzantrag bei "
                  "der Energie Klagenfurt oder der Kärnten Netz und die Mitteilung an die Baubehörde, und zertifizierte "
                  "Fachkräfte montieren. Die Wärmepumpe planen wir auf Wunsch im selben Termin mit."),
            badges=[("Aus Villach", "vor Ort in Klagenfurt"),
                    ("rund 2.100", "Sonnenstunden im Jahr*"),
                    (CLAIMS["ersparnis"], "weniger Stromkosten")],
            img=HERO_IMG,
            img_alt=("Photovoltaikanlage mit 25 kWp auf dem Dach eines Mehrparteienhauses in Krumpendorf am Wörthersee, "
                     "Referenzprojekt von EBZ Energie"),
            float_num=rating,
            float_label=f"Google, {count} Bewertungen" if count else "auf Google",
            cta_secondary=("#waermepumpe", "Wärmepumpe in Klagenfurt"),
        ),
        C.kpis([
            ("rund 2.100 h", "Sonnenschein pro Jahr, Klagenfurt Flughafen*"),
            ("1.000 bis 1.240 kWh", "Jahresertrag je kWp laut PVGIS*"),
            ("3.000 €", "Landespauschale Kärnten für PV mit Speicher"),
            (NAP["rating"], f"Sterne auf Google, {bew}"),
        ]),
        C.text_block(
            eyebrow="Kurz erklärt",
            h2="Lohnt sich Photovoltaik in Klagenfurt?",
            paragraphs=[
                ("Ja. An der Messstation Klagenfurt Flughafen hat GeoSphere Austria von 2015 bis 2024 im Schnitt "
                 "2.119 Sonnenstunden pro Jahr gemessen, zwischen 1.902 Stunden (2024) und 2.278 Stunden (2017). Für "
                 "das Stadtzentrum rechnet PVGIS, das Solarwerkzeug der Europäischen Kommission, mit rund 1.240 kWh "
                 "Jahresertrag je kWp bei Südausrichtung und 30 Grad Neigung und mit rund 1.000 kWh je kWp auf Ost- "
                 "oder Westdächern mit 25 Grad*. Eine Anlage mit 10 kWp liefert damit je nach Dach rund 10.000 bis "
                 "12.400 kWh im Jahr."),
                ("Das sind Richtwerte für freie Dachflächen. Was Ihr Dach in Viktring, Waidmannsdorf, Annabichl oder "
                 "am Wörthersee hergibt, hängt von Gauben, Kaminen, Bäumen und Nachbargebäuden ab. Deshalb bekommen "
                 "Sie von uns einen Projektbericht mit 3D-Belegplan und Statikreport für genau Ihr Haus. Typisch "
                 f"rechnet sich eine Anlage in {CLAIMS['amortisation']}*. Die Stadt selbst will als Teil der EU-Mission "
                 "für klimaneutrale Städte bis 2030 bilanziell klimaneutral werden (Stadt Klagenfurt, klagenfurt.at)."),
            ],
        ),
        C.media_text(
            eyebrow="Netzbetreiber in Klagenfurt",
            h2="Netzanschluss in Klagenfurt: Energie Klagenfurt im Stadtnetz, Kärnten Netz im Umland",
            paragraphs=[
                ("Beim Netzanschluss unterscheidet sich Klagenfurt vom Großteil Kärntens: Das Stromnetz der "
                 "Landeshauptstadt betreibt die Energie Klagenfurt GmbH aus der Gruppe der Stadtwerke Klagenfurt, nicht "
                 "die Kärnten Netz GmbH. Eine Photovoltaikanlage wird dort über das Antragsportal der Stadtwerke "
                 "(pv.stw.at) beantragt. Der Netzbetreiber prüft die Netzsituation und nennt im Angebot die "
                 "genehmigte Einspeiseleistung in kW. Die Modulleistung in kWp können Sie laut Energie Klagenfurt "
                 "frei wählen, solange diese Einspeiseleistung nie überschritten wird. Der Batteriespeicher wird "
                 "mit angemeldet."),
                ("Für den Ablauf heißt das: Den Antrag stellt der Anschlussinhaber selbst, uns können Sie im Portal "
                 "bevollmächtigen. Wir liefern die technischen Daten aus dem Projektbericht und führen Sie durch die "
                 "Schritte. Nach der Montage erfasst der Elektrofachbetrieb die Fertigstellung im Portal, dann "
                 "folgt der Netzzugangsvertrag. Erst mit dieser Freigabe darf die Anlage ans Netz. Wer schon einen "
                 "Smart Meter hat, bekommt den zweiten Messkanal freigeschaltet, ein alter Ferraris-Zähler wird "
                 "getauscht (Energie Klagenfurt, stw.at, Stand Oktober 2026)."),
                ("Außerhalb des Netzgebiets der Energie Klagenfurt ist in Kärnten in der Regel die Kärnten Netz GmbH "
                 "der Verteilernetzbetreiber. Zu welchem Netz Ihre Adresse in Krumpendorf, Ebenthal oder Maria Saal "
                 "gehört, zeigt die Netzgebietskarte der Stadtwerke oder ein Blick auf Ihre Stromrechnung. Wir "
                 "klären das beim ersten Termin."),
            ],
            img=IMG["gen_detail"],
            alt="Montagedetail einer Photovoltaikanlage: Modulklemmen und Unterkonstruktion auf einem Ziegeldach (Symbolbild)",
            bullets=[
                "Stadtnetz: Antrag im Portal der Energie Klagenfurt, Fachbetrieb per Vollmacht eingebunden",
                "Umland: je nach Adresse Energie Klagenfurt oder Kärnten Netz",
                "Inbetriebnahme erst nach Freigabe und Netzzugangsvertrag",
                "Balkonkraftwerke bis 0,8 kW werden nur gemeldet, größere Anlagen beantragt",
            ],
            cta=("kontakt", "Netzanschluss für mein Dach klären"),
            anchor="netzanschluss",
        ),
        C.media_text(
            eyebrow="Baurecht",
            h2="Genehmigung in Klagenfurt: Mitteilung an den Magistrat statt Bauverfahren",
            paragraphs=[
                ("Nach der Kärntner Bauordnung (§ 7 Abs. 1 lit. a Z 20 K-BO 1996, Fassung LGBl. Nr. 11/2026) sind "
                 "bauliche Anlagen, die erneuerbare Energie erzeugen oder elektrische Energie speichern, "
                 "mitteilungspflichtig. Für eine Photovoltaikanlage mit Speicher auf Ihrem Hausdach bedeutet das in "
                 "der Regel: eine schriftliche Mitteilung an die Baubehörde vor Beginn der Arbeiten, mit "
                 "Grundstücksnummer, Katastralgemeinde und kurzer Beschreibung, aber kein Bauverfahren."),
                ("Baubehörde ist im Stadtgebiet der Magistrat der Landeshauptstadt Klagenfurt (Abteilung Baurecht), "
                 "in den Umlandgemeinden die jeweilige Gemeinde. Flächenwidmungsplan, Bebauungsplan und Ortsbild "
                 "gelten auch für mitteilungspflichtige Vorhaben. Nach der Montage wird die Fertigstellung "
                 "gemeldet, beim Speicher mit Lage und technischen Daten. Wird die Anlage zusammen mit einem "
                 "bewilligungspflichtigen Umbau eingereicht oder als Freiflächenanlage geplant, klären wir den Weg "
                 "vorab mit der Behörde."),
            ],
            img=IMG["gen_eigenheim"],
            alt="Einfamilienhaus mit Photovoltaikanlage auf dem Dach (Symbolbild)",
            bullets=[
                "Mitteilung vor Baubeginn, in der Regel ohne Bauverfahren",
                "Stadt: Magistrat Klagenfurt, Umland: die jeweilige Gemeinde",
                "Meldung der Fertigstellung, beim Speicher mit technischen Daten",
            ],
            reverse=True,
            anchor="genehmigung",
        ),
        C.audience_split(
            eyebrow="Für wen wir in Klagenfurt planen",
            h2="Einfamilienhaus, Mehrparteienhaus oder Betrieb: Photovoltaik für Klagenfurt und den Wörthersee",
            intro=("Ein Reihenhaus in Waidmannsdorf braucht eine andere Anlage als ein Wohnhaus mit mehreren Parteien "
                   "in Krumpendorf oder ein Betrieb im Osten der Stadt. Größe, Speicher und Wirtschaftlichkeit "
                   "richten wir nach Ihrem Verbrauch aus."),
            left={
                "img": IMG["pv_card"],
                "alt": "Photovoltaikmodule auf einem Hausdach, montiert von EBZ Energie",
                "title": "Für Ihr Zuhause in Klagenfurt",
                "bullets": [
                    f"Stromkosten um {CLAIMS['ersparnis']} senken",
                    "Speicher, Notstrom, Wallbox und Wärmepumpe als ein System geplant",
                    "3.000 € Landespauschale für PV mit Speicher, Finanzierung ab 147 € im Monat*",
                ],
                "cta": ("kontakt", "Beratung für mein Zuhause"),
            },
            right={
                "img": IMG["gen_gewerbe"],
                "alt": "Betriebsgebäude mit großer Photovoltaikanlage auf dem Dach (Symbolbild)",
                "title": "Für Mehrparteienhaus und Betrieb",
                "bullets": [
                    "Referenz Krumpendorf: 25 kWp und 25 kWh Speicher, in 4 Tagen montiert",
                    "Auslegung nach Lastprofil, hoher Eigenverbrauch am Tag",
                    "Strom im Haus teilen: gemeinschaftliche Erzeugungsanlage oder Energiegemeinschaft",
                ],
                "cta": ("pv_gewerbe", "Photovoltaik für Gewerbe"),
            },
        ),
        C.problem_compare(
            eyebrow="Kosten und Ersparnis",
            h2="Was eine PV-Anlage in Klagenfurt kostet und was sie spart",
            intro=(f"Unser Richtpreis: {CLAIMS['richtpreis_10kwp']} für eine Komplettanlage mit etwa 10 kWp und "
                   "Speicher, inklusive Montage und Inbetriebnahme (Stand Oktober 2026). Dem steht Strom gegenüber, "
                   "den Sie nicht mehr zukaufen: Mit Speicher deckt ein Haushalt einen großen Teil seines Bedarfs "
                   "vom eigenen Dach."),
            bars=[
                ("Stromkosten ohne eigene Anlage", 100, "bad", "voller Netzbezug"),
                ("Stromkosten mit Photovoltaik und Speicher", 15, "good", "bis zu 85 % weniger*"),
            ],
            aside=("Was in Klagenfurt dazukommt", [
                ("▮", "Speicher", "Der Eigenverbrauch steigt von rund 30 auf bis zu 80 Prozent*, auf Wunsch mit Notstrom."),
                ("€", "Förderung", "3.000 € Landespauschale Kärnten für PV ab 5 kWp mit Speicher ab 5 kWh, dazu der Zuschuss des Bundes."),
                ("☀", "Überschuss", "Für eingespeisten Strom brauchen Sie vor der Inbetriebnahme einen Abnehmer: OeMAG, Energieversorger oder Energiegemeinschaft."),
                ("◷", "Finanzierung", "Ab 147 € im Monat*, die Anlage gehört Ihnen ab dem ersten Tag."),
            ]),
        ),
        C.media_text(
            eyebrow="Wärmepumpe Klagenfurt",
            h2="Wärmepumpe in Klagenfurt: erst Fernwärme prüfen, sonst mit Sonnenstrom heizen",
            paragraphs=[
                ("Klagenfurt hat ein Fernwärmenetz der Stadtwerke, das laut Stadtwerken 2025 zu 90,51 Prozent aus "
                 "erneuerbarer Energie gespeist wurde. Ob Ihre Adresse angeschlossen werden kann, lässt sich dort "
                 "online prüfen, und das sollte der erste Schritt sein. Wo kein Anschluss möglich ist, im "
                 "Einfamilienhaus am Stadtrand oder in Gemeinden wie Krumpendorf, Moosburg oder Ebenthal, ersetzt "
                 "meist eine Luft-Wasser-Wärmepumpe den Öl- oder Gaskessel."),
                ("Sie macht aus 1 kWh Strom 4 bis 5 kWh Wärme und kostet inklusive Montage rund 12.000 bis 22.000 € "
                 "vor Förderung, im Altbau mit Anpassungen 15.000 bis 28.000 €*. Ein Beispielhaus mit 12.000 kWh "
                 "Wärmebedarf braucht bei Jahresarbeitszahl 4 rund 3.000 kWh Strom im Jahr*. Eine 10-kWp-Anlage in "
                 "Klagenfurt erzeugt ein Mehrfaches davon, im Winter allerdings weniger, als die Heizung braucht. "
                 "Deshalb legen wir Photovoltaik, Speicher und Wärmepumpe gemeinsam aus und nehmen beim Termin auch "
                 "Heizraum, Heizkörper und den Aufstellort der Außeneinheit auf: In dicht bebauten Siedlungen "
                 "entscheidet der Abstand zu Schlafzimmerfenstern und Nachbargrenze."),
                ("Zur Förderung in Kürze: Beim Bund ist der Topf für den Heizungstausch ausgeschöpft. Das Land "
                 "Kärnten zahlt 2026 eine Pauschale von 3.000 € für den Wechsel zur Wärmepumpe im Eigenheim; ob das "
                 "Budget reicht und welche Voraussetzungen für Ihr Haus gelten, klären wir vor dem Angebot. Den aktuellen Stand lesen Sie unter "
                 + a("foerderungen", "Förderungen im Überblick") + ", eine erste Zahl liefert der "
                 + a("foerderrechner", "Förderrechner") + "."),
            ],
            img=IMG["waermepumpe"],
            alt="Außeneinheit einer Luft-Wasser-Wärmepumpe im Garten eines Einfamilienhauses (Symbolbild)",
            bullets=[
                a("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe") + ": Anlagengröße, Speicher, Steuerung",
                a("/waermepumpe-im-altbau/", "Wärmepumpe im Altbau") + ": Vorlauftemperatur, Heizkörper, Dämmung",
                a("/kosten-einer-waermepumpe/", "Kosten einer Wärmepumpe") + ": vom Gerät bis zur Installation",
                a("/landesfoerderungen-fuer-die-waermepumpe/", "Landesförderungen für die Wärmepumpe") + ": Kärnten und Steiermark",
            ],
            cta=("waermepumpe", "Wärmepumpe vom Fachbetrieb"),
            anchor="waermepumpe",
        ),
        C.media_text(
            eyebrow="Förderung",
            h2="Förderung für Photovoltaik in Klagenfurt: Land Kärnten und Bund in Kürze",
            paragraphs=[
                ("Für Klagenfurt gelten die Programme des Landes Kärnten und des Bundes; eine eigene "
                 "Photovoltaik-Förderung der Stadt ist uns nicht bekannt (Stand Oktober 2026). Das Land zahlt privaten "
                 "Haushalten 3.000 Euro Pauschale für eine neue Anlage ab 5 kWp mit gleichzeitig neuem Speicher ab "
                 "5 kWh und 1.000 Euro für die Nachrüstung eines Speichers. Der Bund fördert 2026 mit 150 Euro je kWp "
                 "bis 10 kWp und 150 Euro je kWh Speicher, europäische Komponenten bringen 10 Prozent Bonus."),
                ("Ab 2027 plant der Bund laut BMWET eine Systemförderung für Speicher und intelligente Steuerung. Was "
                 "gerade offen ist und in welcher Reihenfolge Antrag, Auftrag und Montage laufen müssen, steht auf "
                 "unserer Förderseite, die Einzelheiten zum Landesprogramm im Ratgeber. Die Anträge bereiten wir "
                 "für Sie vor."),
            ],
            img=IMG["foerderung"],
            alt="Beratungsgespräch zur Förderung einer Photovoltaikanlage am Tisch",
            bullets=[
                "Land Kärnten: 3.000 € für PV ab 5 kWp mit Speicher ab 5 kWh, 1.000 € für Speicher-Nachrüstung",
                "Bund 2026: 150 €/kWp bis 10 kWp, 150 €/kWh Speicher, 10 % Bonus für europäische Komponenten",
                a("foerderung_kaernten", "PV-Förderung Kärnten 2026 im Detail"),
                a("foerderrechner", "Förderrechner: Ihre Förderung berechnen"),
            ],
            cta=("foerderungen", "Aktuelle Förderungen 2026"),
            dark=True,
        ),
        C.finance_band(),
        C.reference_cards(
            eyebrow="Referenzen",
            h2="Referenzen am Wörthersee und in Kärnten, mit Zahlen belegt",
            intro=("Unser Projekt im Raum Klagenfurt: das "
                   + a(REF_KRUMPENDORF, "Mehrparteienhaus in Krumpendorf am Wörthersee")
                   + " mit 25 kWp, 25 kWh Speicher und Notstrom, montiert und in Betrieb genommen in vier Tagen. Bild "
                   "und Zahlen gehören jeweils zum selben Projekt."),
            items=[
                {"img": IMG["ref_krumpendorf"],
                 "alt": "Photovoltaikanlage in Ost-West-Ausrichtung auf einem Mehrparteienhaus in Krumpendorf am Wörthersee",
                 "title": "Mehrparteienhaus, Krumpendorf",
                 "specs": "25 kWp in Ost-West-Ausrichtung, 25 kWh Speicher, Notstrom für die wichtigsten Verbraucher.",
                 "result": "4 Tage", "result_sub": "Montage und Inbetriebnahme"},
                {"img": IMG["ref_villach"],
                 "alt": "Photovoltaikanlage mit 10 kWp auf einem Einfamilienhaus in Villach",
                 "title": "Einfamilienhaus, Villach",
                 "specs": "10 kWp in Ost-West-Ausrichtung mit Notstrom, rund 11.000 kWh pro Jahr.",
                 "result": "rund 80 %", "result_sub": "weniger Stromkosten"},
                {"img": IMG["gewerbe_dach"],
                 "alt": "Photovoltaikanlage mit 40 kWp auf dem Trapezblechdach eines Gewerbebetriebs in Oberösterreich",
                 "title": "Gewerbebetrieb, Oberösterreich",
                 "specs": "40 kWp Ost-West auf Trapezblech, 40 kWh Speicher, rund 40.000 kWh pro Jahr.",
                 "result": "13.500 €", "result_sub": "Ersparnis pro Jahr*"},
            ],
        ),
        C.cards_section(
            eyebrow="Anbieter-Check",
            h2="Photovoltaik-Firmen in Klagenfurt vergleichen: sechs Punkte fürs Angebot",
            intro=("EBZ Energie GmbH ist ein Fachbetrieb für Photovoltaik, Speicher und Wärmepumpen mit Sitz in "
                   f"Villach (Triglavstraße 15). Wir beraten und montieren in Klagenfurt am Wörthersee und im Umland, "
                   f"haben {CLAIMS['projekte']} Projekte umgesetzt und {NAP['rating']} Sterne aus {bew} auf Google "
                   "(Stand Oktober 2026). Egal, bei welcher PV-Firma Sie anfragen: Diese sechs Punkte sollten im "
                   "Angebot stehen."),
            cards=[
                {"ic": "✓", "title": "Netz und Behörde geregelt",
                 "text": "Wer begleitet den Antrag im Portal der Energie Klagenfurt oder bei Kärnten Netz und die Mitteilung an Magistrat oder Gemeinde? Das gehört schriftlich ins Angebot."},
                {"ic": "⌖", "title": "Planung für Ihr Dach",
                 "text": "Ein Projektbericht mit 3D-Belegplan und Statikreport zeigt Belegung, Verschattung und Lasten, bevor Sie unterschreiben."},
                {"ic": "€", "title": "Fixpreis mit Stückliste",
                 "text": "Module, Wechselrichter, Speicher, Montage, Arbeiten am Zählerschrank und Inbetriebnahme stehen einzeln im Angebot."},
                {"ic": "◇", "title": "Garantien schwarz auf weiß",
                 "text": "Bei uns: bis zu 30 Jahre Leistungsgarantie und mindestens 10 Jahre Produktgarantie auf die Module."},
                {"ic": "☎", "title": "Ein Ansprechpartner",
                 "text": "Zertifizierte Fachkräfte auf dem Dach und am Zählerschrank, ein fester Ansprechpartner von der Planung bis zur Übergabe."},
                {"ic": "◎", "title": "Referenzen mit Zahlen",
                 "text": "Fragen Sie nach Projekten mit kWp, Speichergröße und Ergebnis, am besten aus Ihrer Gegend.",
                 "link_key": "referenzen", "link_text": "Unsere Referenzen"},
            ],
        ),
        C.facts_panel(
            eyebrow="Kontakt und Einsatzgebiet",
            h2="Fachbetrieb aus Villach, vor Ort in Klagenfurt",
            intro=("Wir haben kein Büro in Klagenfurt und brauchen auch keines: Die Beratung findet bei Ihnen statt, "
                   "dort, wo Dach, Zählerschrank und Heizraum sind."),
            rows=[
                ("Firmensitz", f"{NAP['name']}<br>{NAP['street']}, {NAP['zip']} {NAP['city']}"),
                ("Telefon", tel_link()),
                ("E-Mail", f'<a href="mailto:{NAP["email"]}">{NAP["email"]}</a>'),
                ("Erreichbar", NAP["hours"]),
                ("Google-Bewertung", f"{NAP['rating']} von 5 aus {bew}"),
                ("Klagenfurt", STADTTEILE),
                ("Umland", UMLAND),
                ("Netzbetreiber", "Energie Klagenfurt GmbH im Stadtnetz, sonst in der Regel Kärnten Netz GmbH"),
                ("Baubehörde", "Magistrat der Landeshauptstadt Klagenfurt, im Umland die jeweilige Gemeinde"),
                ("Weitere Regionen", "Montage in ganz Kärnten und der Steiermark, Referenzen in 6 Bundesländern, zum Beispiel "
                 + a("pv_villach", "Photovoltaik in Villach") + "."),
            ],
            actions=[("Anrufen", NAP["phone_href"], ""),
                     ("Beratung anfragen", "#beratung", "")],
        ).replace('<section class="section"', '<section id="standort" class="section"', 1),
        C.reviews_slider(reviews, rating=rating, count=count),
        C.steps_section(
            eyebrow="So läuft es ab",
            h2="Von der Beratung in Klagenfurt bis zur Freigabe durch den Netzbetreiber",
            steps=[
                ("Termin bei Ihnen", "Wir nehmen Dach, Zählerschrank und Verbrauch auf, auf Wunsch auch Heizraum und Heizkörper. Kostenlos und unverbindlich.", ""),
                ("Projektbericht und Fixangebot", "Sie erhalten den Projektbericht mit 3D-Belegplan und Statikreport und ein Angebot mit Stückliste.", ""),
                ("Netz, Baubehörde, Förderung", "Antrag im Portal der Energie Klagenfurt oder bei Kärnten Netz, Mitteilung an Magistrat oder Gemeinde, Anträge bei Land und Bund.", ""),
                ("Montage und Freigabe", "Zertifizierte Fachkräfte montieren. Nach Fertigstellungsmeldung und Netzzugangsvertrag geht die Anlage in Betrieb, wir schulen Sie ein.", ""),
            ],
        ),
        C.faq_section(FAQ),
        C.linkgrid_section(
            "Photovoltaik und Wärmepumpe in Klagenfurt und Kärnten",
            [("photovoltaik", "Photovoltaik für Eigenheim und Gewerbe"),
             ("waermepumpe", "Wärmepumpe vom Fachbetrieb"),
             ("batteriespeicher", "Stromspeicher"),
             ("foerderung_kaernten", "PV-Förderung Kärnten 2026 im Detail"),
             ("foerderrechner", "Förderrechner: Ihre Förderung berechnen"),
             ("/energiegemeinschaft-villach-klagenfurt/", "Energiegemeinschaft Villach und Klagenfurt"),
             ("/photovoltaik-fuer-waermepumpe/", "Photovoltaik für die Wärmepumpe"),
             ("/kosten-einer-solaranlage/", "Was eine Solaranlage kostet"),
             ("/notstrom/", "Notstrom bei Stromausfall"),
             ("balkonkraftwerke", "Balkonkraftwerk mit Montage und Anmeldung"),
             ("finanzierung", "Finanzierung ab 147 € im Monat"),
             (REF_KRUMPENDORF, "Referenz Krumpendorf am Wörthersee")] + nachbarn,
        ),
        C.contact_section(
            headline="Ihr kostenloses Angebot für Photovoltaik in Klagenfurt",
            sub=("Schreiben Sie uns Adresse, Jahresverbrauch und ob eine Wärmepumpe geplant ist. Wir melden uns, "
                 "kommen zu Ihnen nach Klagenfurt oder ins Umland und sagen ehrlich, was auf Ihrem Dach möglich "
                 "ist und was es kostet."),
            page_label="Photovoltaik Klagenfurt",
        ),
        C.finalcta(
            "Sonnenstrom für Ihr Dach in Klagenfurt?",
            "Fordern Sie Ihre kostenlose Beratung an. Sie hören innerhalb eines Werktags von uns, den Termin machen "
            "wir bei Ihnen in Klagenfurt oder im Umland.",
        ),
        _footnote(),
    ])
    html = page(TITLE, DESC, PATH, body, faq_jsonld_str=faq_jsonld(u(PATH), FAQ),
                og_image=HERO_IMG, extra_jsonld=standort_schema(PATH, "Klagenfurt", "Kärnten"))
    return write_page("photovoltaik-klagenfurt/index.html", html)


def _footnote():
    return ("""
  <section class="section--tight" style="padding-bottom:40px">
    <div class="wrap">
      <p class="form-note">*Richtwerte, vor Förderung. Preis, Ersparnis, Eigenverbrauch und Amortisation hängen von
      Verbrauch, Anlagengröße, Ausrichtung und Strompreis ab. Sonnenstunden: GeoSphere Austria, Messstation Klagenfurt
      Flughafen, Mittel der Jahressummen 2015 bis 2024. Ertrag je kWp: PVGIS 5.3 der Europäischen Kommission (Datensatz
      SARAH3, 2005 bis 2023) für Klagenfurt Zentrum mit 14 % Systemverlusten und hinterlüfteter Montage; Ihr Dach kann
      abweichen. Netzanschluss laut Energie Klagenfurt GmbH (stw.at) und Kärnten Netz GmbH, Baurecht laut Kärntner
      Bauordnung 1996, jeweils Stand Oktober 2026. Finanzierung: Beispielkonditionen, vorbehaltlich Bonitätsprüfung.
      Wärmepumpe: Richtwerte aus unseren Ratgebern, Beispielhaus mit 12.000 kWh Wärmebedarf und Jahresarbeitszahl 4;
      Förderhöhe abhängig von Richtlinie, Gebäude und Budget der Fördergeber. Fördersätze, Tarife und OeMAG-Marktpreis
      Stand Oktober 2026, Änderungen vorbehalten. Fachlich geprüft von Mario Zintl, Geschäftsführung EBZ Energie GmbH.</p>
    </div>
  </section>""")


if __name__ == "__main__":
    import theme
    theme.write_assets()
    build()
