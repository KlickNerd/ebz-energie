"""Fehlerseite 404 (/404.html): wird vom Webserver (ErrorDocument in .htaccess) und von GitHub Pages ausgeliefert."""

from common import a, write_page
from layout import page
import components as C


def build():
    body = "".join([
        C.page_hero(
            eyebrow="Fehler 404",
            h1="Diese Seite gibt es nicht mehr",
            lead=("Vielleicht hat sich die Adresse mit unserer neuen Website geändert. Hier finden Sie die wichtigsten "
                  "Seiten, oder Sie rufen uns einfach an."),
            cta=("home", "Zur Startseite"), cta2=("kontakt", "Kontakt"),
        ),
        C.linkgrid_section("Häufig gesucht", [
            ("photovoltaik", "Photovoltaik mit Speicher"),
            ("waermepumpe", "Wärmepumpe"),
            ("foerderungen", "Förderungen 2026"),
            ("foerderrechner", "Förderrechner"),
            ("finanzierung", "Finanzierung"),
            ("referenzen", "Referenzen"),
            ("ratgeber", "Ratgeber"),
            ("standorte", "Standorte"),
        ]),
    ])
    html = page("Seite nicht gefunden | EBZ Energie", "Diese Seite gibt es auf ebz-photovoltaik.at nicht mehr. Hier finden Sie die wichtigsten Seiten von EBZ Energie.", "/404.html", body)
    html = html.replace('<meta name="robots" content="index,follow,max-image-preview:large">', '<meta name="robots" content="noindex,follow">')
    return write_page("404.html", html)
