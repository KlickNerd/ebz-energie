"""Danke-Seite (/danke/): Ziel nach erfolgreich gesendetem Kontaktformular, wie auf der alten WordPress-Seite.

noindex und nicht in der Sitemap. Hier feuert die Google-Ads-Conversion "Anfrage gesendet" (wie auf der alten
Seite: AW-10792977949/uGLzCKDeI5wYEJ2Mv5oo), aber nur, wenn im Cookie-Banner zugestimmt wurde.
"""

from common import NAP, ADS_CONVERSION, write_page, tel_link
from layout import page
import components as C

PATH = "/danke/"


def build():
    body = "".join([
        C.page_hero(
            eyebrow="Anfrage erhalten",
            h1="Danke für Ihre Anfrage",
            lead=(f"Ihre Nachricht ist bei uns in Villach angekommen. Wir melden uns innerhalb eines Werktags bei Ihnen, "
                  f"telefonisch oder per E-Mail. Eilt es? Dann rufen Sie uns an: {NAP['phone_display']}, {NAP['hours']}."),
            cta=("home", "Zur Startseite"), cta2=("referenzen", "Referenzen ansehen"),
        ),
        C.steps_section(
            eyebrow="So geht es weiter",
            h2="Was nach Ihrer Anfrage passiert",
            steps=[
                ("Rückmeldung", "Wir melden uns innerhalb eines Werktags und klären die wichtigsten Eckdaten.", "1 Werktag"),
                ("Termin vor Ort", "Wir sehen uns Dach, Zählerkasten und Verbrauch an, kostenlos und unverbindlich.", "nach Absprache"),
                ("Projektbericht", "Sie erhalten einen Projektbericht mit 3D-Belegplan und Statikreport.", "ca. 1 Woche"),
                ("Festpreisangebot", "Dazu ein transparentes Angebot und den aktuellen Förderstand für Ihr Projekt.", "mit dem Bericht"),
            ],
        ),
        C.linkgrid_section("In der Zwischenzeit lesen", [
            ("referenzen", "Referenzen mit Zahlen"),
            ("foerderrechner", "Förderrechner"),
            ("solarrechner", "Solarrechner"),
            ("finanzierung", "Finanzierung"),
            ("ratgeber", "Ratgeber"),
            ("ueber_uns", "Über EBZ Energie"),
        ]),
    ])
    html = page("Danke für Ihre Anfrage | EBZ Energie",
                "Danke für Ihre Anfrage bei EBZ Energie. Wir melden uns innerhalb eines Werktags.", PATH, body)
    # Google-Ads-Conversion "Anfrage gesendet": wird nur mit Einwilligung gesendet (siehe Cookie-Banner in main.js)
    html = html.replace("</head>", f'  <script>window.EBZ_CONVERSION="{ADS_CONVERSION}";</script>\n</head>', 1)
    html = html.replace('<meta name="robots" content="index,follow,max-image-preview:large">',
                        '<meta name="robots" content="noindex,follow">')
    return write_page("danke/index.html", html)
