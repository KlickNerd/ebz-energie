"""Rechtsseite Datenschutzerklaerung (/datenschutz/).

Quelle: Live-Seite ebz-photovoltaik.at/datenschutz/ (Stand Oktober 2026). Der Text wurde
vollstaendig und inhaltlich unveraendert uebernommen und nur formatiert (H2/H3, Listen),
NAP vereinheitlicht (Triglavstrasse 15), Gedankenstriche entfernt. Abschnitte zu
WordPress-spezifischen Diensten (Consent-Tool, Google Maps, YouTube) sind mit
"TODO Kunde" markiert, aber nicht geloescht. Ergaenzt wurden neutrale Hinweise zu
Hosting als statische Website, Google Fonts (Laden von Google-Servern) und zur
Uebermittlung der Kontaktformular-Daten. Keine Rechtsberatung.
"""

from common import NAP, AUTHOR, a, tel_link, write_page
from layout import page
import components as C

PATH = "/datenschutz/"
TITLE = "Datenschutzerklärung | EBZ Energie GmbH"
DESC = ("Datenschutzerklärung der EBZ Energie GmbH, Villach: Verantwortlicher, Betroffenenrechte nach DSGVO, Kontaktanfragen, Google Fonts, Hosting und Drittdienste.")

GOOGLE_PRIVACY = "https://www.google.at/intl/de/policies/privacy/"
GOOGLE_PRIVACY_DE = "https://www.google.de/intl/de/policies/privacy"
PRIVACY_SHIELD = "https://www.privacyshield.gov/participant?id=a2zt000000001L5AAI&amp;status=Active"


def build():
    mail = f'<a href="mailto:{NAP["email"]}">{NAP["email"]}</a>'
    body = "".join([
        C.page_hero(
            eyebrow="Rechtliches",
            h1="Datenschutzerklärung",
            lead=("Wie die EBZ Energie GmbH personenbezogene Daten auf dieser Website verarbeitet, welche Rechte "
                  "Sie als Nutzer haben und welche Dienste Dritter eingesetzt werden."),
            cta=("kontakt", "Kontakt aufnehmen"),
            cta2=("impressum", "Impressum"),
        ),
        f"""
  <section class="section">
    <div class="wrap">
      <article class="prose" style="max-width:820px;margin-inline:auto">

        <h2>Datenschutz</h2>
        <p>Personenbezogene Daten (nachfolgend zumeist nur „Daten“ genannt) werden von uns nur im Rahmen der
        Erforderlichkeit sowie zum Zwecke der Bereitstellung eines funktionsfähigen und nutzerfreundlichen
        Internetauftritts, inklusive seiner Inhalte und der dort angebotenen Leistungen, verarbeitet.</p>
        <p>Gemäß Art. 4 Ziffer 1. der Verordnung (EU) 2016/679, also der Datenschutz-Grundverordnung
        (nachfolgend nur „DSGVO“ genannt), gilt als „Verarbeitung“ jeder mit oder ohne Hilfe automatisierter
        Verfahren ausgeführter Vorgang oder jede solche Vorgangsreihe im Zusammenhang mit personenbezogenen
        Daten, wie das Erheben, das Erfassen, die Organisation, das Ordnen, die Speicherung, die Anpassung oder
        Veränderung, das Auslesen, das Abfragen, die Verwendung, die Offenlegung durch Übermittlung, Verbreitung
        oder eine andere Form der Bereitstellung, den Abgleich oder die Verknüpfung, die Einschränkung, das
        Löschen oder die Vernichtung.</p>
        <p>Mit der nachfolgenden Datenschutzerklärung informieren wir Sie insbesondere über Art, Umfang, Zweck,
        Dauer und Rechtsgrundlage der Verarbeitung personenbezogener Daten, soweit wir entweder allein oder
        gemeinsam mit anderen über die Zwecke und Mittel der Verarbeitung entscheiden. Zudem informieren wir Sie
        nachfolgend über die von uns zu Optimierungszwecken sowie zur Steigerung der Nutzungsqualität
        eingesetzten Fremdkomponenten, soweit hierdurch Dritte Daten in wiederum eigener Verantwortung
        verarbeiten.</p>
        <p>Unsere Datenschutzerklärung ist wie folgt gegliedert:</p>
        <ol>
          <li><a href="#verantwortliche">Informationen über uns als Verantwortliche</a></li>
          <li><a href="#rechte">Rechte der Nutzer und Betroffenen</a></li>
          <li><a href="#verarbeitung">Informationen zur Datenverarbeitung</a></li>
        </ol>

        <h2 id="verantwortliche">I. Informationen über uns als Verantwortliche</h2>
        <p>Verantwortlicher Anbieter dieses Internetauftritts im datenschutzrechtlichen Sinne ist:</p>
        <p><strong>{NAP['name']}</strong><br>
        Geschäftsführer {AUTHOR}<br>
        {NAP['street']}<br>
        A-{NAP['zip']} {NAP['city']}<br>
        E-Mail: {mail}<br>
        Telefon: {tel_link()}</p>
        <p>Weitere Angaben zum Unternehmen finden Sie im {a('impressum', 'Impressum')}.</p>

        <h2 id="rechte">II. Rechte der Nutzer und Betroffenen</h2>
        <p>Mit Blick auf die nachfolgend noch näher beschriebene Datenverarbeitung haben die Nutzer und
        Betroffenen das Recht</p>
        <ul>
          <li>auf Bestätigung, ob sie betreffende Daten verarbeitet werden, auf Auskunft über die verarbeiteten
          Daten, auf weitere Informationen über die Datenverarbeitung sowie auf Kopien der Daten (vgl. auch
          Art. 15 DSGVO);</li>
          <li>auf Berichtigung oder Vervollständigung unrichtiger bzw. unvollständiger Daten (vgl. auch
          Art. 16 DSGVO);</li>
          <li>auf unverzügliche Löschung der sie betreffenden Daten (vgl. auch Art. 17 DSGVO), oder, alternativ,
          soweit eine weitere Verarbeitung gemäß Art. 17 Abs. 3 DSGVO erforderlich ist, auf Einschränkung der
          Verarbeitung nach Maßgabe von Art. 18 DSGVO;</li>
          <li>auf Erhalt der sie betreffenden und von ihnen bereitgestellten Daten und auf Übermittlung dieser
          Daten an andere Anbieter/Verantwortliche (vgl. auch Art. 20 DSGVO);</li>
          <li>auf Beschwerde gegenüber der Aufsichtsbehörde, sofern sie der Ansicht sind, dass die sie
          betreffenden Daten durch den Anbieter unter Verstoß gegen datenschutzrechtliche Bestimmungen
          verarbeitet werden (vgl. auch Art. 77 DSGVO).</li>
        </ul>
        <p>Darüber hinaus ist der Anbieter dazu verpflichtet, alle Empfänger, denen gegenüber Daten durch den
        Anbieter offengelegt worden sind, über jedwede Berichtigung oder Löschung von Daten oder die Einschränkung
        der Verarbeitung, die aufgrund der Artikel 16, 17 Abs. 1, 18 DSGVO erfolgt, zu unterrichten. Diese
        Verpflichtung besteht jedoch nicht, soweit diese Mitteilung unmöglich oder mit einem unverhältnismäßigen
        Aufwand verbunden ist. Unbeschadet dessen hat der Nutzer ein Recht auf Auskunft über diese Empfänger.</p>
        <p>Ebenfalls haben die Nutzer und Betroffenen nach Art. 21 DSGVO das Recht auf Widerspruch gegen die
        künftige Verarbeitung der sie betreffenden Daten, sofern die Daten durch den Anbieter nach Maßgabe von
        Art. 6 Abs. 1 lit. f) DSGVO verarbeitet werden. Insbesondere ist ein Widerspruch gegen die
        Datenverarbeitung zum Zwecke der Direktwerbung statthaft.</p>

        <h2 id="verarbeitung">III. Informationen zur Datenverarbeitung</h2>
        <p>Ihre bei Nutzung unseres Internetauftritts verarbeiteten Daten werden gelöscht oder gesperrt, sobald
        der Zweck der Speicherung entfällt, der Löschung der Daten keine gesetzlichen Aufbewahrungspflichten
        entgegenstehen und nachfolgend keine anderslautenden Angaben zu einzelnen Verarbeitungsverfahren gemacht
        werden.</p>

        <h3>Hosting und Server-Logfiles</h3>
        <p>Diese Website wird als statische Website ausgeliefert, also ohne Content-Management-System, ohne
        Datenbank und ohne Nutzerkonten. Beim Aufruf einzelner Seiten verarbeitet der Hosting-Anbieter in
        Server-Logfiles die technisch notwendigen Verbindungsdaten Ihres Endgeräts, insbesondere IP-Adresse,
        Datum und Uhrzeit des Abrufs, abgerufene Datei, übertragene Datenmenge, Browsertyp und Betriebssystem.
        Diese Daten dienen ausschließlich dem sicheren und stabilen Betrieb der Website und werden nicht mit
        anderen Datenquellen zusammengeführt. Rechtsgrundlage ist unser berechtigtes Interesse an einem sicheren
        und funktionsfähigen Internetauftritt (Art. 6 Abs. 1 lit. f) DSGVO).</p>
        <!-- TODO Kunde: Hosting-Anbieter (Name, Sitz) benennen, Speicherdauer der Logfiles und ggf. Auftragsverarbeitungsvertrag pruefen. -->

        <h3>Cookies</h3>
        <!-- TODO Kunde: pruefen, ob noch relevant. Der Abschnitt stammt von der WordPress-Seite mit Consent-Tool (Borlabs Cookie, Schaltflaeche "Cookie-Einstellungen aendern"). Die statische Website setzt nach aktuellem Stand keine eigenen Cookies und hat kein Consent-Tool. -->
        <h4>a) Sitzungs-Cookies/Session-Cookies</h4>
        <p>Wir verwenden mit unserem Internetauftritt sog. Cookies. Cookies sind kleine Textdateien oder andere
        Speichertechnologien, die durch den von Ihnen eingesetzten Internet-Browser auf Ihrem Endgerät ablegt
        und gespeichert werden. Durch diese Cookies werden im individuellen Umfang bestimmte Informationen von
        Ihnen, wie beispielsweise Ihre Browser- oder Standortdaten oder Ihre IP-Adresse, verarbeitet.</p>
        <p>Durch diese Verarbeitung wird unser Internetauftritt benutzerfreundlicher, effektiver und sicherer, da
        die Verarbeitung bspw. die Wiedergabe unseres Internetauftritts in unterschiedlichen Sprachen oder das
        Angebot einer Warenkorbfunktion ermöglicht.</p>
        <p>Rechtsgrundlage dieser Verarbeitung ist Art. 6 Abs. 1 lit b.) DSGVO, sofern diese Cookies Daten zur
        Vertragsanbahnung oder Vertragsabwicklung verarbeitet werden.</p>
        <p>Falls die Verarbeitung nicht der Vertragsanbahnung oder Vertragsabwicklung dient, liegt unser
        berechtigtes Interesse in der Verbesserung der Funktionalität unseres Internetauftritts. Rechtsgrundlage
        ist in dann Art. 6 Abs. 1 lit. f) DSGVO.</p>
        <p>Mit Schließen Ihres Internet-Browsers werden diese Session-Cookies gelöscht.</p>
        <h4>b) Drittanbieter-Cookies</h4>
        <p>Gegebenenfalls werden mit unserem Internetauftritt auch Cookies von Partnerunternehmen, mit denen wir
        zum Zwecke der Werbung, der Analyse oder der Funktionalitäten unseres Internetauftritts zusammenarbeiten,
        verwendet.</p>
        <p>Die Einzelheiten hierzu, insbesondere zu den Zwecken und den Rechtsgrundlagen der Verarbeitung solcher
        Drittanbieter-Cookies, entnehmen Sie bitte den nachfolgenden Informationen.</p>
        <h4>c) Beseitigungsmöglichkeit</h4>
        <p>Sie können die Installation der Cookies durch eine Einstellung Ihres Internet-Browsers verhindern oder
        einschränken. Ebenfalls können Sie bereits gespeicherte Cookies jederzeit löschen. Die hierfür
        erforderlichen Schritte und Maßnahmen hängen jedoch von Ihrem konkret genutzten Internet-Browser ab. Bei
        Fragen benutzen Sie daher bitte die Hilfefunktion oder Dokumentation Ihres Internet-Browsers oder wenden
        sich an dessen Hersteller bzw. Support. Bei sog. Flash-Cookies kann die Verarbeitung allerdings nicht
        über die Einstellungen des Browsers unterbunden werden. Stattdessen müssen Sie insoweit die Einstellung
        Ihres Flash-Players ändern. Auch die hierfür erforderlichen Schritte und Maßnahmen hängen von Ihrem
        konkret genutzten Flash-Player ab. Bei Fragen benutzen Sie daher bitte ebenso die Hilfefunktion oder
        Dokumentation Ihres Flash-Players oder wenden sich an den Hersteller bzw. Benutzer-Support.</p>
        <p>Sollten Sie die Installation der Cookies verhindern oder einschränken, kann dies allerdings dazu
        führen, dass nicht sämtliche Funktionen unseres Internetauftritts vollumfänglich nutzbar sind.</p>

        <h3>Kontaktanfragen / Kontaktmöglichkeit</h3>
        <p>Sofern Sie per Kontaktformular oder E-Mail mit uns in Kontakt treten, werden die dabei von Ihnen
        angegebenen Daten zur Bearbeitung Ihrer Anfrage genutzt. Die Angabe der Daten ist zur Bearbeitung und
        Beantwortung Ihrer Anfrage erforderlich. Ohne deren Bereitstellung können wir Ihre Anfrage nicht oder
        allenfalls eingeschränkt beantworten.</p>
        <p>Rechtsgrundlage für diese Verarbeitung ist Art. 6 Abs. 1 lit. b) DSGVO.</p>
        <p>Ihre Daten werden gelöscht, sofern Ihre Anfrage abschließend beantwortet worden ist und der Löschung
        keine gesetzlichen Aufbewahrungspflichten entgegenstehen, wie bspw. bei einer sich etwaig anschließenden
        Vertragsabwicklung.</p>
        <p>Hinweis zum Kontaktformular dieser Website: Die im Kontaktformular eingegebenen Daten (Name,
        E-Mail-Adresse, Telefonnummer, Postleitzahl, Nachricht, Herkunftsseite) werden verschlüsselt übertragen und per E-Mail
        an {mail} übermittelt. Eine Speicherung in einer Datenbank auf dieser Website findet nicht statt.</p>
        <!-- TODO Kunde: Das Formular wird technisch ueber eine Automatisierungsplattform (Webhook, derzeit n8n bzw. Make) an die E-Mail-Adresse weitergeleitet. Dienstleister benennen und Auftragsverarbeitungsvertrag pruefen. -->
        <!-- TODO Kunde: pruefen, ob noch relevant. Auf der WordPress-Seite war WPForms (Formular-Plugin) im Einsatz. Auf der statischen Website gibt es kein WordPress-Plugin mehr. -->
        <p><small>Muster-Datenschutzerklärung der Anwaltskanzlei Weiß &amp; Partner</small></p>

        <h3>Google Maps</h3>
        <!-- TODO Kunde: pruefen, ob noch relevant. Consent-Schalter der WordPress-Seite: [borlabs-cookie id="googlemaps" type="btn-switch-consent"/]. Auf der statischen Website ist derzeit keine Google-Maps-Karte eingebunden. -->
        <p>Diese Webseite verwendet Google Maps für die Darstellung von Karteninformationen. Bei der Nutzung von
        Google Maps werden von Google auch Daten über die Nutzung der Maps-Funktionen durch Besucher der
        Webseiten erhoben, verarbeitet und genutzt. Nähere Informationen über die Datenverarbeitung durch Google
        können Sie den Datenschutzhinweisen von Google auf
        <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">{GOOGLE_PRIVACY}</a> entnehmen. Dort können Sie
        im Datenschutzcenter auch Ihre Einstellungen verändern, so dass Sie Ihre Daten verwalten und schützen
        können.</p>

        <h3>Datenschutzerklärung für die Nutzung von YouTube</h3>
        <!-- TODO Kunde: pruefen, ob noch relevant. Consent-Schalter der WordPress-Seite: [borlabs-cookie id="youtube" type="btn-switch-consent"/]. Auf der statischen Website sind derzeit keine YouTube-Videos eingebettet. Der Abschnitt stand auf der Live-Seite doppelt und wurde einmal uebernommen. -->
        <p>Plugins der von Google betriebenen Seite YouTube. Betreiber der Seiten ist die YouTube, LLC,
        901 Cherry Ave., San Bruno, CA 94066, USA. Wenn Sie eine unserer mit einem YouTube-Plugin ausgestatteten
        Seiten besuchen, wird eine Verbindung zu den Servern von YouTube hergestellt. Dabei wird dem
        Youtube-Server mitgeteilt, welche unserer Seiten Sie besucht haben.</p>
        <p>Wenn Sie in Ihrem YouTube-Account eingeloggt sind ermöglichen Sie YouTube, Ihr Surfverhalten direkt
        Ihrem persönlichen Profil zuzuordnen. Dies können Sie verhindern, indem Sie sich aus Ihrem
        YouTube-Account ausloggen.</p>
        <p>Weitere Informationen zum Umgang von Nutzerdaten finden Sie in der Datenschutzerklärung von YouTube
        unter <a href="{GOOGLE_PRIVACY_DE}" target="_blank" rel="noopener">{GOOGLE_PRIVACY_DE}</a></p>

        <h3>Google Fonts</h3>
        <p>In unserem Internetauftritt setzen wir Google Fonts zur Darstellung externer Schriftarten ein. Es
        handelt sich hierbei um einen Dienst der Google LLC, 1600 Amphitheatre Parkway, Mountain View, CA 94043
        USA, nachfolgend nur „Google“ genannt.</p>
        <p>Durch die Zertifizierung nach dem EU-US-Datenschutzschild („EU-US Privacy Shield“)
        <a href="{PRIVACY_SHIELD}" target="_blank" rel="noopener">https://www.privacyshield.gov/participant?id=a2zt000000001L5AAI&amp;status=Active</a>
        garantiert Google, dass die Datenschutzvorgaben der EU auch bei der Verarbeitung von Daten in den USA
        eingehalten werden.</p>
        <!-- TODO Kunde: pruefen, ob noch relevant. Das EU-US Privacy Shield ist seit dem EuGH-Urteil vom 16.07.2020 ungueltig, Nachfolger ist das EU-US Data Privacy Framework (seit 10.07.2023). Satz stammt unveraendert von der Live-Seite. -->
        <!-- TODO Kunde: Die Live-Seite enthielt den Satz "Google Fonts werden auf dieser Website lokal geladen." Das trifft auf die statische Website nicht zu (siehe Hinweis unten). Satz deshalb hier auskommentiert, Entscheidung lokal hosten vs. Google-Server beim Kunden. -->
        <p>Hinweis zu dieser Website: Die Schriftarten Sora und Source Sans 3 werden beim Aufruf einer Seite von
        Servern von Google (fonts.googleapis.com, fonts.gstatic.com) geladen. Dabei wird die IP-Adresse Ihres
        Endgeräts an Google übermittelt, damit die Schriftdateien ausgeliefert werden können. Wir verwenden
        Google Fonts im Interesse einer einheitlichen und gut lesbaren Darstellung unserer Website.
        Rechtsgrundlage ist unser berechtigtes Interesse gemäß Art. 6 Abs. 1 lit. f) DSGVO. Welche Daten Google
        dabei verarbeitet, erfahren Sie in den Datenschutzhinweisen von Google unter
        <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">{GOOGLE_PRIVACY}</a>.</p>
        <!-- TODO Kunde: ggf. Google Fonts lokal hosten (Schriftdateien auf eigenem Server), dann entfaellt die Uebermittlung an Google und dieser Absatz ist anzupassen. -->

        <h3>Fragen zum Datenschutz</h3>
        <p>Bei Fragen zur Verarbeitung Ihrer Daten oder zur Ausübung Ihrer Rechte wenden Sie sich bitte an die
        {NAP['name']}, {NAP['street']}, {NAP['zip']} {NAP['city']}, E-Mail {mail}, Telefon {tel_link()}.</p>

      </article>
    </div>
  </section>""",
    ])
    html = page(TITLE, DESC, PATH, body)
    return write_page("datenschutz/index.html", html)


if __name__ == "__main__":
    import theme
    theme.write_assets()
    build()
