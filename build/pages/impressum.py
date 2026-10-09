"""Rechtsseite Impressum (/impressum/).

Quelle: Live-Seite ebz-photovoltaik.at/impressum/ (Stand Oktober 2026). Pflichtangaben
unveraendert uebernommen, Standardabschnitte (Haftung, Urheberrecht, Bildnachweis,
Streitbeilegung) ergaenzt. Offene Angaben des Kunden stehen als HTML-Kommentare
"TODO Kunde" im Dokument.
"""

from common import NAP, AUTHOR, u, a, tel_link, write_page
from layout import page
import components as C

PATH = "/impressum/"
TITLE = "Impressum | EBZ Energie GmbH, Villach"
DESC = ("Impressum der EBZ Energie GmbH, Triglavstraße 15, 9500 Villach: Firmenbuchnummer, UID, "
        "Aufsichtsbehörde, Geschäftsführung, Haftungshinweise und Bildnachweis.")


def _facts():
    rows = [
        ("Firmenwortlaut", NAP["name"]),
        ("Anschrift", f"{NAP['street']}, {NAP['zip']} {NAP['city']}, Österreich"),
        ("Telefon", tel_link()),
        ("E-Mail", f'<a href="mailto:{NAP["email"]}">{NAP["email"]}</a>'),
        ("Geschäftsführung", AUTHOR),
        ("Firmenbuchnummer", "FN 597101 s"),
        ("UID-Nummer", "ATU79039023"),
        ("Wirtschafts-Identifikationsnummer", "9110005291103"),
        ("Aufsichtsbehörde", "Bezirkshauptmannschaft Villach"),
        ("Kammerzugehörigkeit", "Wirtschaftskammer Kärnten"),
    ]
    items = "".join(f"<div><dt>{lbl}</dt><dd>{val}</dd></div>" for lbl, val in rows)
    return f'<dl class="facts" style="margin:24px 0 8px">{items}</dl>'


def build():
    body = "".join([
        C.page_hero(
            eyebrow="Rechtliches",
            h1="Impressum",
            lead=("Angaben gemäß § 5 E-Commerce-Gesetz (ECG), § 14 Unternehmensgesetzbuch (UGB) und "
                  "§ 25 Mediengesetz für die Website ebz-photovoltaik.at."),
            cta=("kontakt", "Kontakt aufnehmen"),
            cta2=("datenschutz", "Datenschutzerklärung"),
        ),
        f"""
  <section class="section">
    <div class="wrap">
      <article class="prose" style="max-width:820px;margin-inline:auto">

        <h2>Medieninhaber und Diensteanbieter</h2>
        <p>Verantwortlich für den Inhalt dieser Website ist die {NAP['name']} mit Sitz in {NAP['city']}, Kärnten.</p>
        {_facts()}
        <!-- TODO Kunde: Firmenbuchgericht (vermutlich Landesgericht Klagenfurt) bestaetigen und ergaenzen. -->
        <!-- TODO Kunde: Fachgruppe bzw. Fachverband in der Wirtschaftskammer Kaernten nennen. -->
        <!-- TODO Kunde: genauen Gewerbewortlaut laut Gewerbeberechtigung (GISA) ergaenzen. Die Live-Seite nennt nur "Handelsgewerbe". -->
        <p>Für alle Anfragen zu Angebot, Montage und Service erreichen Sie uns {NAP['hours']} unter {tel_link()}
        oder per E-Mail an <a href="mailto:{NAP['email']}">{NAP['email']}</a>.</p>

        <h2>Gewerbe und anwendbare Rechtsvorschriften</h2>
        <p>Die {NAP['name']} unterliegt der Gewerbeordnung 1994 (GewO) sowie den für das Gewerbe geltenden
        berufsrechtlichen Vorschriften. Diese sind im Rechtsinformationssystem des Bundes abrufbar unter
        <a href="https://www.ris.bka.gv.at" target="_blank" rel="noopener">www.ris.bka.gv.at</a>.
        Mitglied der Wirtschaftskammer Kärnten. Informationen zu E-Commerce-Gesetz und Mediengesetz finden
        Sie ebenfalls im Rechtsinformationssystem des Bundes.</p>

        <h2>Unternehmensgegenstand</h2>
        <p>Planung, Lieferung, Montage und Service von Photovoltaikanlagen, Batteriespeichern, Wärmepumpen,
        Energiemanagementsystemen und Balkonkraftwerken sowie Beratung zu Energiegemeinschaften für Eigenheim
        und Gewerbe. Montagegebiet: Kärnten und Steiermark, Referenzen in sechs Bundesländern.</p>

        <h2>Blattlinie (§ 25 Mediengesetz)</h2>
        <p>Diese Website informiert über die Leistungen der {NAP['name']} sowie über Technik, Förderungen und
        Wirtschaftlichkeit von Photovoltaik, Stromspeichern, Wärmepumpen und Energiegemeinschaften in Österreich.</p>

        <h2>Haftung für Inhalte</h2>
        <p>Die Inhalte dieser Website wurden mit größter Sorgfalt erstellt und werden laufend aktualisiert.
        Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte übernehmen wir dennoch keine Gewähr.
        Preisangaben, Förderhöhen, Einspeisetarife und Beispielrechnungen sind Richtwerte zum jeweils genannten
        Stand und ersetzen kein individuelles Angebot und keine Rechts-, Steuer- oder Finanzberatung.
        Als Diensteanbieter sind wir gemäß § 16 ECG für eigene Inhalte verantwortlich, nicht jedoch verpflichtet,
        übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die
        auf eine rechtswidrige Tätigkeit hinweisen. Sollten Sie auf rechtswidrige Inhalte aufmerksam werden,
        bitten wir um eine kurze Nachricht. Wir entfernen solche Inhalte umgehend.</p>

        <h2>Haftung für Links</h2>
        <p>Diese Website enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben.
        Für diese fremden Inhalte ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich.
        Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft,
        rechtswidrige Inhalte waren dabei nicht erkennbar. Eine permanente inhaltliche Kontrolle der verlinkten
        Seiten ist ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei Bekanntwerden von
        Rechtsverletzungen entfernen wir derartige Links umgehend.</p>

        <h2>Urheberrecht</h2>
        <p>Die auf dieser Website veröffentlichten Inhalte, Texte, Grafiken, Fotos, Infografiken und Rechner
        unterliegen dem österreichischen Urheberrecht. Jede Verwertung außerhalb der Grenzen des Urheberrechts,
        insbesondere Vervielfältigung, Bearbeitung, Verbreitung und öffentliche Zugänglichmachung, bedarf der
        vorherigen schriftlichen Zustimmung der {NAP['name']}. Downloads und Kopien dieser Seite sind nur für den
        privaten, nicht kommerziellen Gebrauch gestattet. Soweit Inhalte nicht von uns erstellt wurden, werden
        die Urheberrechte Dritter beachtet und entsprechende Inhalte als solche gekennzeichnet.</p>

        <h2>Bildnachweis</h2>
        <ul>
          <li>Projekt- und Teamfotos: {NAP['name']}, eigene Aufnahmen von realisierten Anlagen in Kärnten,
          Steiermark, Oberösterreich, Niederösterreich, Burgenland und Wien.</li>
          <li>Stockfotos: Adobe Stock sowie Pexels (lizenzfreie Nutzung gemäß den jeweiligen Lizenzbedingungen).</li>
          <li>Illustrationen und Symbolbilder: teilweise KI-generiert und als Symbolbilder zu verstehen. Sie zeigen
          keine realen Personen, Kunden oder Anlagen der {NAP['name']}.</li>
          <li>Infografiken und Diagramme: {NAP['name']} in Zusammenarbeit mit KlickNerds.</li>
        </ul>
        <!-- TODO Kunde: Bildnachweis vervollstaendigen (Namen der Fotografen bzw. Urheber einzelner Stockbilder, falls Lizenz dies verlangt). -->

        <h2>Verbraucherstreitbeilegung</h2>
        <p>Die von der Europäischen Kommission betriebene Plattform zur Online-Streitbeilegung
        (ec.europa.eu/consumers/odr) wurde mit 20. Juli 2025 eingestellt und steht nicht mehr zur Verfügung.</p>
        <p>Wir sind nicht verpflichtet und nicht bereit, an Streitbeilegungsverfahren vor einer
        Verbraucherschlichtungsstelle im Sinne des Alternative-Streitbeilegung-Gesetzes (AStG) teilzunehmen.
        Bei Anliegen zu einem Auftrag wenden Sie sich bitte direkt an uns: {tel_link()} oder
        <a href="mailto:{NAP['email']}">{NAP['email']}</a>. Wir finden gemeinsam eine Lösung.</p>

        <h2>Umsetzung der Website</h2>
        <p>Konzeption, Inhalte, Suchmaschinenoptimierung und technische Umsetzung: KlickNerds im Auftrag der
        {NAP['name']}. Hinweise zum Umgang mit personenbezogenen Daten finden Sie in unserer
        {a('datenschutz', 'Datenschutzerklärung')}.</p>

      </article>
    </div>
  </section>""",
    ])
    html = page(TITLE, DESC, PATH, body, include_business_schema=True)
    return write_page("impressum/index.html", html)


if __name__ == "__main__":
    import theme
    theme.write_assets()
    build()
