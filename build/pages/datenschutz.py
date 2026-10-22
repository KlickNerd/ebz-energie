"""Rechtsseite Datenschutzerklaerung (/datenschutz/).

Grundlage: Datenschutzerklaerung der alten WordPress-Seite (Muster Weiss & Partner), formatiert, NAP
vereinheitlicht, Gedankenstriche entfernt. Am 21.10.2026 auf die statische Website umgestellt: Hosting IONOS,
Schriften lokal (kein Google Fonts mehr), Cookies nur mit Einwilligung (Google Ads), lokaler Speicher fuer Chat und Cookie-Auswahl, Kontaktformular
ueber Make (Celonis Inc., DPF) und Gmail, neuer Abschnitt Chat-Assistent (Cloudflare, Anthropic). Entfernt:
Abschnitte zu Consent-Tool, Session-/Drittanbieter-Cookies, Google Maps, YouTube und das ungueltige Privacy
Shield. Offene Punkte als "TODO Kunde". Keine Rechtsberatung.
"""

from common import NAP, AUTHOR, a, tel_link, write_page
from layout import page
import components as C

PATH = "/datenschutz/"
TITLE = "Datenschutzerklärung | EBZ Energie GmbH"
DESC = ("Datenschutzerklärung der EBZ Energie GmbH, Villach: Betroffenenrechte, Kontaktformular, Chat-Assistent, Google Ads mit Einwilligung und Hosting.")



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
        Datenbank und ohne Nutzerkonten. Hosting-Anbieter ist die IONOS SE, Elgendorfer Straße 57, 56410 Montabaur,
        Deutschland. Beim Aufruf einzelner Seiten verarbeitet IONOS in Server-Logfiles die technisch notwendigen
        Verbindungsdaten Ihres Endgeräts, insbesondere IP-Adresse, Datum und Uhrzeit des Abrufs, abgerufene Datei,
        übertragene Datenmenge, Browsertyp und Betriebssystem. Diese Daten dienen ausschließlich dem sicheren und
        stabilen Betrieb der Website, werden nicht mit anderen Datenquellen zusammengeführt und nach kurzer Zeit
        gelöscht. Rechtsgrundlage ist unser berechtigtes Interesse an einem sicheren und funktionsfähigen
        Internetauftritt (Art. 6 Abs. 1 lit. f) DSGVO). Mit IONOS besteht ein Vertrag zur Auftragsverarbeitung.</p>
        <!-- TODO Kunde: Auftragsverarbeitungsvertrag im IONOS-Kundenkonto abschliessen (Vertraege und Kuendigungen > Datenschutz), Speicherdauer der Logfiles dort nachlesen. -->

        <h3>Schriftarten</h3>
        <p>Die auf dieser Website verwendeten Schriftarten (Sora und Source Sans 3) sind lokal auf unserem
        Webserver gespeichert. Beim Aufruf einer Seite wird keine Verbindung zu Servern von Google oder anderen
        Anbietern von Schriftarten hergestellt.</p>

        <h3>Cookies und lokaler Speicher</h3>
        <p>Ohne Ihre Zustimmung setzt diese Website keine Cookies. Cookies von Google entstehen nur, wenn Sie im
        Cookie-Hinweis „Alle akzeptieren“ wählen (siehe Google Ads). Ihre Auswahl im Cookie-Hinweis speichert Ihr Browser
        im lokalen Speicher (localStorage), damit der Hinweis nicht bei jedem Seitenaufruf erneut erscheint. Nur wenn Sie den
        Chat-Assistenten nutzen, speichert Ihr Browser den Gesprächsverlauf im lokalen Speicher (localStorage) Ihres
        Endgeräts, damit das Gespräch beim Wechsel auf eine andere Unterseite erhalten bleibt. Diese Daten verlassen
        Ihr Gerät dafür nicht und werden nach sechs Stunden nicht mehr verwendet; Sie können sie jederzeit über die
        Einstellungen Ihres Browsers löschen. Schließen Sie den Hinweis zum Chat-Assistenten, merkt sich Ihr Browser
        das für die laufende Sitzung (sessionStorage). Diese Speicherungen erfolgen nur aufgrund Ihrer Handlung und
        sind für die von Ihnen gewünschte Funktion erforderlich.</p>

        <h3>Google Ads (Conversion-Messung)</h3>
        <p>Mit Ihrer Einwilligung nutzen wir Google Ads der Google Ireland Limited, Gordon House, Barrow Street,
        Dublin 4, Irland. Damit messen wir, ob Besucherinnen und Besucher, die über eine unserer Anzeigen auf die Website
        kommen, eine Anfrage senden (Conversion). Dazu wird das Skript gtag.js von Google geladen; Google setzt Cookies
        und verarbeitet unter anderem Ihre IP-Adresse, Geräte- und Browserinformationen sowie die Information, dass nach
        einem Anzeigenklick eine Anfrage gesendet wurde. Den Inhalt Ihrer Anfrage erhält Google nicht. Eine Übermittlung
        in die USA ist möglich; Google ist nach dem EU-US Data Privacy Framework zertifiziert.</p>
        <p>Ohne Ihre Zustimmung wird das Google-Skript nicht geladen und es werden keine Daten an Google gesendet.
        Rechtsgrundlage ist Ihre Einwilligung (Art. 6 Abs. 1 lit. a) DSGVO, § 165 Abs. 3 TKG 2021). Sie können sie
        jederzeit mit Wirkung für die Zukunft über den Link „Cookie-Einstellungen“ im Fußbereich jeder Seite
        widerrufen. Weitere Informationen: policies.google.com/privacy.</p>
        <!-- TODO Kunde: Google-Ads-Datenverarbeitungsbedingungen im Ads-Konto akzeptieren (Google Ads Data Processing Terms) und Abschnitt rechtlich pruefen lassen. -->

        <h3>Kontaktanfragen / Kontaktmöglichkeit</h3>
        <p>Sofern Sie per Kontaktformular oder E-Mail mit uns in Kontakt treten, werden die dabei von Ihnen
        angegebenen Daten zur Bearbeitung Ihrer Anfrage genutzt. Die Angabe der Daten ist zur Bearbeitung und
        Beantwortung Ihrer Anfrage erforderlich. Ohne deren Bereitstellung können wir Ihre Anfrage nicht oder
        allenfalls eingeschränkt beantworten.</p>
        <p>Rechtsgrundlage für diese Verarbeitung ist Art. 6 Abs. 1 lit. b) DSGVO.</p>
        <p>Ihre Daten werden gelöscht, sofern Ihre Anfrage abschließend beantwortet worden ist und der Löschung
        keine gesetzlichen Aufbewahrungspflichten entgegenstehen, wie bspw. bei einer sich etwaig anschließenden
        Vertragsabwicklung.</p>
        <p>Technische Übermittlung: Die im Kontaktformular eingegebenen Daten (Name, E-Mail-Adresse,
        Telefonnummer, Postleitzahl, Nachricht, Herkunftsseite, Zeitpunkt) werden verschlüsselt an den
        Automatisierungsdienst Make übertragen und von dort per E-Mail an {mail} zugestellt. Make wird von der
        Celonis Inc., One World Trade Center, New York, NY 10007, USA, betrieben; der Versand der E-Mail erfolgt
        über Gmail der Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland. Eine Speicherung in
        einer Datenbank auf dieser Website findet nicht statt. Die Übermittlung in die USA erfolgt auf Grundlage
        des EU-US Data Privacy Framework, nach dem die Anbieter zertifiziert sind.</p>
        <!-- TODO Kunde: Auftragsverarbeitung mit Make (Celonis) und der Agentur KlickNerds, die Make und Gmail fuer EBZ betreibt, schriftlich festhalten. -->

        <h3>Chat-Assistent (KI)</h3>
        <p>Auf dieser Website können Sie Fragen an einen KI-gestützten Chat-Assistenten stellen. Wenn Sie den Chat
        öffnen und eine Nachricht senden, wird der Text Ihrer Nachrichten zusammen mit dem bisherigen
        Gesprächsverlauf über einen Dienst der Cloudflare, Inc., 101 Townsend St., San Francisco, CA 94107, USA,
        an die Anthropic PBC, 548 Market St., San Francisco, CA 94104, USA, übermittelt, die daraus die Antwort
        erzeugt. Dabei verarbeitet Cloudflare technisch die IP-Adresse Ihres Endgeräts. Wir speichern die
        Gesprächsinhalte nicht. Bitte geben Sie im Chat keine sensiblen Daten ein. Der Chat-Assistent kann Fehler
        machen und ersetzt keine verbindliche Beratung oder Förderzusage.</p>
        <p>Wünschen Sie im Chat eine Beratung oder einen Rückruf, werden die von Ihnen genannten Angaben (Name,
        Telefonnummer oder E-Mail-Adresse, Region, Anliegen, gewünschtes Zeitfenster und eine kurze Zusammenfassung
        des Gesprächs) wie beim Kontaktformular über Make per E-Mail an {mail} weitergeleitet.</p>
        <p>Rechtsgrundlage ist unser berechtigtes Interesse an einer schnellen Beantwortung von Fragen zu unseren
        Leistungen (Art. 6 Abs. 1 lit. f) DSGVO), bei Beratungswunsch die Anbahnung eines Vertrags (Art. 6 Abs. 1
        lit. b) DSGVO). Die Übermittlung in die USA erfolgt auf Grundlage des EU-US Data Privacy Framework oder
        der Standardvertragsklauseln der Europäischen Kommission. Die Nutzung des Chats ist freiwillig; alle
        Informationen erhalten Sie auch telefonisch oder per E-Mail.</p>
        <!-- TODO Kunde: Rechtliche Pruefung des Chat-Abschnitts (KI-Anbieter, Uebermittlung USA) durch Rechtsberatung empfohlen. -->

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
