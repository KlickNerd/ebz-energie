"""Gemeinsame Konstanten und Helfer fuer den EBZ-Website-Build.

Statische Website (KEIN WordPress). Ziel: eigenstaendige HTML-Dokumente mit
gemeinsamer externer CSS/JS, deploybar bei jedem Static-Hoster.

Source of Truth fuer verbindliche Fakten: siehe CLAUDE.md, Abschnitt 2.
Diese Werte NICHT ohne Kundenfreigabe aendern.
"""

import json as _json
import os as _os
import re as _re

# Kanonische Domain (fuer canonical/OG/JSON-LD). Interne Links bleiben relativ.
BASE = "https://ebz-photovoltaik.at"

# Optionaler Pfad-Praefix fuer Deploys in einem Unterverzeichnis (z. B. GitHub
# Pages Projektseite "/ebz-energie"). Lokal leer -> alle Links bleiben ab "/".
BASE_PATH = _os.environ.get("EBZ_BASE", "").rstrip("/")

# --- Verbindliche NAP-Daten (nur diese Adresse ist gueltig) ---------------
TEL_DISPLAY = "+43 650 220 26 26"
TEL_HREF = "tel:+436502202626"
EMAIL = "office@ebz-energie.com"

NAP = {
    "name": "EBZ Energie GmbH",
    "street": "Triglavstraße 15",
    "zip": "9500",
    "city": "Villach",
    "region": "Kärnten",
    "country": "AT",
    "phone_display": TEL_DISPLAY,
    "phone_href": TEL_HREF,
    "email": EMAIL,
    "hours": "Mo bis Fr: 10:00 bis 20:00 Uhr",
    "rating": "4,9",
}

# --- Freigegebene Kern-Claims (siehe CLAUDE.md) ---------------------------
CLAIMS = {
    "ersparnis": "bis zu 85 %",            # nie 90 %
    "rating": "4,9",                       # nie 5,0
    "projekte": "300+",
    "bundeslaender": "6 Bundesländer",
    "amortisation": "4 bis 6 Jahre",
    "garantie_leistung": "bis zu 30 Jahre Leistungsgarantie",
    "garantie_produkt": "mindestens 10 Jahre Produktgarantie",
    "finanzierung_ab": "ab 147 €/Monat inkl. Speicher",
    "richtpreis_10kwp": "rund 15.000 bis 22.000 € vor Förderung",
}

# Finanzierung (Quelle: Finanzierungsbeilage "powered by Cloover", Stand September 2026).
# Repraesentative Beispiele, Rate abhaengig von Angebot und Laufzeit; vorbehaltlich Bonitaetspruefung.
FINANZIERUNG = {
    "partner": "Cloover",
    "anzahlung": "0 €",
    "zusage": "unter 2 Minuten",
    "annahmequote": "94 %",
    "laufzeit_max": "25 Jahre",
    "beispiel_klein": {"betrag": "15.000 €", "anlage": "8 kWp", "foerderung": "900 €",
                       "rate": "ab 102 €", "gesamt": "rund 127 €"},
    "beispiel_gross": {"betrag": "25.000 €", "anlage": "10 kWp + 10 kWh Speicher", "foerderung": "3.000 €",
                       "rate": "ab 164 €", "gesamt": "rund 185 €"},
    "strom_heute": "163 €",       # 7.000 kWh x 28 ct / 12
    "strom_mit_pv": "20 bis 30 €",  # Reststrom bei bis zu 80 % Eigenbedarfsdeckung
    "fussnote": ("*Repräsentative Beispiele aus der Finanzierungsbeilage, Stand September 2026: Laufzeit 25 Jahre, "
                 "Rate abhängig von Angebot und Laufzeit, Förderung als Beispiel des Bundes-Investitionszuschusses, "
                 "Stromkosten mit 7.000 kWh pro Jahr und 28 ct/kWh. Alle Angaben freibleibend, Finanzierung "
                 "vorbehaltlich Bonitätsprüfung."),
}

# Kontaktformular: POST (JSON) an den Make-Webhook "EBZ Kontaktformular" (Szenario "EBZ Kontaktformular -> E-Mail",
# ID 6582422): Antwort 200 {"ok": true}, dann Gmail an office@, bei Fehler Slack-Warnung und 3 Wiederholungen.
# Ueberwacht vom "Formular-Waechter" (einmal taeglich im 8-Uhr-Lauf). Fallback im Browser: mailto-Link.
# (Seit 10.10.2026 statt n8n; build/n8n-workflow-kontakt.json ist nur noch Archiv.)
FORM_ENDPOINT = "https://hook.us2.make.com/1fkgm8zywyy6jqswmqibte15sxb349n7"

AUTHOR = "Mario Zintl"
AUTHOR_ROLE = "Geschäftsführung EBZ Energie GmbH"

# --- Slug-Verzeichnis -----------------------------------------------------
# Interne Verlinkung IMMER ueber href()/a(), nie hartkodierte Pfade.
S = {
    "home": "/",
    "photovoltaik": "/photovoltaik/",
    "batteriespeicher": "/batteriespeicher/",
    "waermepumpe": "/waermepumpe/",  # GSC 07-10/2026: alte URL 4 Klicks, Pos. 19 -> Umzug risikofrei, 301 in redirects.txt
    "balkonkraftwerke": "/balkonkraftwerke/",
    "finanzierung": "/finanzierung/",
    "referenzen": "/referenzen/",
    "eg": "/energiegemeinschaft/",
    "eg_privat": "/leistungen/energiegemeinschaft/",
    "eg_gewerbe": "/leistungen/energiegemeinschaft-gewerbe/",
    "eg_rechner": "/energiegemeinschaft-rechner/",
    "ems": "/energiemanagementsystem/",
    "solarrechner": "/solarrechner/",
    "leistungen": "/leistungen/",
    "ratgeber": "/ratgeber/",
    "kontakt": "/kontakt/",
    "ueber_uns": "/ueber-uns/",
    "aktuelles": "/aktuelles/",
    "impressum": "/impressum/",
    "datenschutz": "/datenschutz/",
    "foerderung_at": "/photovoltaik-foerderung-oesterreich-2026/",  # WP-Beitrag; alte Seite /photovoltaik-foerderung-oesterreich/ -> 301
    "foerderung_kaernten": "/photovoltaik-foerderung-kaernten/",  # WP-Beitrag 2026; alte Seite /foerderung-photovoltaik-kaernten/ -> 301
    "foerderung_steiermark": "/foerderung-photovoltaik-steiermark/",
    "foerderungen": "/foerderungen/",  # Hub: alle Foerderungen 2026 (PV, Speicher, Waermepumpe, EMS, Balkon)
    "foerderrechner": "/foerderrechner/",  # Rechner hinter dem Finder-Button der Foerderseite
    "pv_villach": "/photovoltaik-villach/",
    "pv_wolfsberg": "/photovoltaik-wolfsberg/",
    "pv_klagenfurt": "/photovoltaik-klagenfurt/",
    "pv_graz": "/photovoltaik-graz/",
    "pv_steiermark": "/photovoltaik-steiermark/",
    # Ortsseiten aus der gemeinsamen Vorlage (build/pages/standorte.py + build/content/standorte/<datei>.py)
    "pv_spittal": "/photovoltaik-spittal/",
    "pv_feldkirchen": "/photovoltaik-feldkirchen/",
    "pv_st_veit": "/photovoltaik-st-veit/",
    "pv_voelkermarkt": "/photovoltaik-voelkermarkt/",
    "pv_hermagor": "/photovoltaik-hermagor/",
    "pv_leibnitz": "/photovoltaik-leibnitz/",
    "pv_deutschlandsberg": "/photovoltaik-deutschlandsberg/",
    "pv_voitsberg": "/photovoltaik-voitsberg/",
    "pv_weiz": "/photovoltaik-weiz/",
    "pv_murtal": "/photovoltaik-murtal/",
    "pv_leoben": "/photovoltaik-leoben/",
    "pv_suedoststeiermark": "/photovoltaik-suedoststeiermark/",
    "standorte": "/standorte/",  # Uebersicht aller Standortseiten
    "marktpreis": "/marktpreis-2026/",
    "pv_gewerbe": "/photovoltaik-gewerbe/",
    "carport": "/photovoltaik-carport/",
}

# --- Bilder ---------------------------------------------------------------
# Ziel: self-hosted unter /assets/img/ (weg von wp-content). Bis zum Download
# der Originale zeigen die Quell-URLs auf die Live-Mediathek (nur Referenz).
IMG = {
    "hero_home": "/assets/img/hero-photovoltaik-villach.jpg",
    "team_quer": "/assets/img/team-fachbetrieb.jpg",
    "team_beratung": "/assets/img/team-beratung.jpg",
    "mario": "/assets/img/mario-zintl-freigestellt.png",  # echter Freisteller, 2K (Higgsfield)
    "eg_drohne": "/assets/img/energiegemeinschaft-ort.jpg",
    "gewerbe_dach": "/assets/img/gewerbe-dach-ooe.jpg",
    "pv_card": "/assets/img/photovoltaik-anlage.jpg",
    "speicher": "/assets/img/batteriespeicher.png",
    "waermepumpe": "/assets/img/waermepumpe.jpg",
    "ems": "/assets/img/ems-energiemanagement.jpg",  # Higgsfield: Technikraum mit EMS-Display, Speicher, Wechselrichter
    "ems_app": "/assets/img/ems-app.jpg",  # Higgsfield: Energiefluss-App am Smartphone
    "balkon": "/assets/img/balkonkraftwerk.jpg",
    "foerderung": "/assets/img/foerderung.jpg",
    "ref_villach": "/assets/img/referenz-villach.jpg",
    "ref_krumpendorf": "/assets/img/referenz-krumpendorf.jpg",
    # Projekteigene Bilder (nicht aus wp-content), liegen in build/static/img/
    "team_mission": "/assets/img/team-ebz-mission.jpg",
    "logo": "/assets/img/ebz-logo.png",  # weisses Wortmark + Amber-Mark (fuer dunkle Leiste)
    # Higgsfield-generierte Szenen (keine erfundenen Team-Fotos), build/static/img/
    "gen_hero": "/assets/img/pv-hero-roof.jpg",
    "gen_eigenheim": "/assets/img/pv-eigenheim.jpg",
    "gen_gewerbe": "/assets/img/pv-gewerbe.jpg",
    "gen_detail": "/assets/img/pv-montage-detail.jpg",
}

# Quelle -> Zielpfad fuer den Bild-Download (build/fetch_images.py nutzt das).
IMG_SOURCES = {
    "/assets/img/hero-photovoltaik-villach.jpg": BASE + "/wp-content/uploads/2023/10/EBZ-Energie-Photovoltaik-Villach.jpg",
    "/assets/img/team-fachbetrieb.jpg": BASE + "/wp-content/uploads/2026/09/2.jpeg",
    "/assets/img/team-beratung.jpg": BASE + "/wp-content/uploads/2026/09/1.jpeg",
    "/assets/img/mario-zintl.png": BASE + "/wp-content/uploads/2023/12/Zintl_cut.png",
    "/assets/img/energiegemeinschaft-ort.jpg": BASE + "/wp-content/uploads/2026/09/pexels-stepan-vrany-591647707-28169966-1.jpg",
    "/assets/img/gewerbe-dach-ooe.jpg": BASE + "/wp-content/uploads/2026/07/gewerbe-ooe-1.jpg",
    "/assets/img/photovoltaik-anlage.jpg": BASE + "/wp-content/uploads/2023/10/PHOTO-2023-06-23-09-48-56.jpg",
    "/assets/img/batteriespeicher.png": BASE + "/wp-content/uploads/2025/11/Speicher-768x1364.png",
    "/assets/img/waermepumpe.jpg": BASE + "/wp-content/uploads/2026/03/2149250264-1.jpg",
    "/assets/img/energiemanagement.png": BASE + "/wp-content/uploads/2025/11/Gemini_Generated_Image_dndoxkdndoxkdndo.png",
    "/assets/img/balkonkraftwerk.jpg": BASE + "/wp-content/uploads/2024/09/AdobeStock_712663492-web-768x512.jpg",
    "/assets/img/foerderung.jpg": BASE + "/wp-content/uploads/2025/12/pexels-mikhail-nilov-6963888-1024x754.jpg",
    "/assets/img/referenz-villach.jpg": BASE + "/wp-content/uploads/2023/09/EBZ-Photovoltaik-Module1.jpg",
    "/assets/img/referenz-krumpendorf.jpg": BASE + "/wp-content/uploads/2023/10/Stranegger-ref.jpg",
}


# --- Helfer ---------------------------------------------------------------
# Alle Standortseiten in der Reihenfolge der Ortsliste auf der Startseite.
# (Slug-Key, Name, Land, Quelle): Quelle "modul" = eigenes Modul build/pages/standort_<x>.py,
# sonst Dateiname in build/content/standorte/ (gemeinsame Vorlage build/pages/standorte.py).
STANDORTE = [
    ("pv_villach", "Villach", "ktn", "modul"),
    ("pv_klagenfurt", "Klagenfurt", "ktn", "modul"),
    ("pv_spittal", "Spittal an der Drau", "ktn", "spittal"),
    ("pv_feldkirchen", "Feldkirchen", "ktn", "feldkirchen"),
    ("pv_st_veit", "St. Veit an der Glan", "ktn", "st_veit"),
    ("pv_wolfsberg", "Wolfsberg", "ktn", "modul"),
    ("pv_voelkermarkt", "Völkermarkt", "ktn", "voelkermarkt"),
    ("pv_hermagor", "Hermagor", "ktn", "hermagor"),
    ("pv_graz", "Graz", "stmk", "modul"),
    ("pv_leibnitz", "Leibnitz", "stmk", "leibnitz"),
    ("pv_deutschlandsberg", "Deutschlandsberg", "stmk", "deutschlandsberg"),
    ("pv_voitsberg", "Voitsberg", "stmk", "voitsberg"),
    ("pv_weiz", "Weiz", "stmk", "weiz"),
    ("pv_murtal", "Murtal", "stmk", "murtal"),
    ("pv_leoben", "Leoben", "stmk", "leoben"),
    ("pv_suedoststeiermark", "Südoststeiermark", "stmk", "suedoststeiermark"),
]
_STANDORT_MODUL = {"pv_villach": "standort_villach", "pv_klagenfurt": "standort_klagenfurt",
                   "pv_wolfsberg": "standort_wolfsberg", "pv_graz": "standort_graz",
                   "pv_steiermark": "standort_steiermark"}


def standort_exists(key):
    """True, wenn es fuer den Slug-Key schon eine Seitenquelle gibt (sonst wird nicht verlinkt)."""
    here = _os.path.dirname(_os.path.abspath(__file__))
    if key in _STANDORT_MODUL:
        return _os.path.exists(_os.path.join(here, "pages", _STANDORT_MODUL[key] + ".py"))
    for k, _name, _land, src in STANDORTE:
        if k == key:
            return _os.path.exists(_os.path.join(here, "content", "standorte", src + ".py"))
    return False


def standort_link(key, text):
    """Link auf eine Standortseite, oder nur der Text, solange die Seite noch nicht gebaut ist."""
    return a(key, text) if standort_exists(key) else text


def standorte(land=None, ohne=None):
    """Gebaute Standortseiten als (key, name), optional nach Land gefiltert und ohne die eigene Seite."""
    return [(k, n) for k, n, l, _src in STANDORTE
            if (land is None or l == land) and k != ohne and standort_exists(k)]


def href(key_or_path):
    """Relativer Href fuer interne Links (statisch, hoster-unabhaengig)."""
    return S.get(key_or_path, key_or_path)


def u(key_or_path):
    """Absolute URL (fuer canonical/OG/JSON-LD)."""
    path = S.get(key_or_path, key_or_path)
    if path.startswith("http"):
        return path
    return BASE + path


def a(key_or_path, text, cls=None, extra=""):
    c = f' class="{cls}"' if cls else ""
    e = f" {extra}" if extra else ""
    return f'<a href="{href(key_or_path)}"{c}{e}>{text}</a>'


def tel_link(cls=None, label=None):
    c = f' class="{cls}"' if cls else ""
    return f'<a href="{TEL_HREF}"{c}>{label or TEL_DISPLAY}</a>'


def faq_jsonld(page_url, qa_pairs):
    """FAQPage-JSON-LD. qa_pairs: Liste aus (frage, antwort_plaintext)."""
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "@id": page_url.rstrip("/") + "/#faq",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": ans}}
            for q, ans in qa_pairs
        ],
    }
    return _json.dumps(data, ensure_ascii=False, indent=None)


def breadcrumb_jsonld(items):
    """BreadcrumbList. items: Liste aus (name, absolute_url)."""
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": url}
            for i, (n, url) in enumerate(items)
        ],
    }
    return _json.dumps(data, ensure_ascii=False, indent=None)


def article_jsonld(page_url, headline, description, date_published, date_modified, image=None):
    """Article-Schema fuer Ratgeber: Autor Mario Zintl, Publisher EBZ Energie GmbH.

    Auf der statischen Site gibt es kein SEO-Plugin mehr, daher kollidiert das
    Schema mit nichts (die alte 'nur FAQPage'-Regel galt fuer WordPress-Bloecke).
    """
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "@id": page_url.rstrip("/") + "/#article",
        "mainEntityOfPage": page_url,
        "headline": headline,
        "description": description,
        "inLanguage": "de-AT",
        "datePublished": date_published,
        "dateModified": date_modified,
        "author": {
            "@type": "Person",
            "name": AUTHOR,
            "jobTitle": "Geschäftsführer",
            "worksFor": {"@type": "Organization", "name": NAP["name"]},
            "url": BASE + S["ueber_uns"],
        },
        "publisher": {
            "@type": "Organization",
            "name": NAP["name"],
            "url": BASE + "/",
            "logo": {"@type": "ImageObject", "url": BASE + IMG["logo"]},
        },
    }
    if image:
        data["image"] = image if image.startswith("http") else BASE + image
    return _json.dumps(data, ensure_ascii=False, indent=None)


def standort_schema(path, name, land_name, area_name=None, ort_in=None):
    """Breadcrumb + Service-Schema (areaServed = Ort) fuer Standortseiten. Gibt zwei JSON-Strings zurueck."""
    crumbs = breadcrumb_jsonld([("Startseite", u("/")), ("Standorte", u("standorte")), (name, u(path))])
    service = {
        "@context": "https://schema.org", "@type": "Service",
        "@id": u(path).rstrip("/") + "/#service",
        "serviceType": "Photovoltaik, Batteriespeicher und Wärmepumpe: Planung, Montage und Förderabwicklung",
        "name": "Photovoltaik und Wärmepumpe " + (ort_in or f"in {name}"),
        "areaServed": {"@type": "AdministrativeArea", "name": area_name or name,
                       "containedInPlace": {"@type": "AdministrativeArea", "name": land_name}},
        "provider": {"@type": "SolarInstallation", "@id": BASE + "/#business", "name": NAP["name"],
                     "telephone": NAP["phone_display"], "url": BASE + "/",
                     "address": {"@type": "PostalAddress", "streetAddress": NAP["street"], "postalCode": NAP["zip"],
                                 "addressLocality": NAP["city"], "addressCountry": NAP["country"]}},
        "url": u(path),
    }
    return [crumbs, _json.dumps(service, ensure_ascii=False)]


def localbusiness_jsonld():
    """Zentrales LocalBusiness-Schema (auf statischer Site erwuenscht, kein Plugin-Konflikt)."""
    data = {
        "@context": "https://schema.org",
        "@type": "SolarInstallation",
        "@id": BASE + "/#business",
        "name": NAP["name"],
        "image": BASE + IMG["hero_home"],
        "url": BASE + "/",
        "telephone": TEL_DISPLAY,
        "email": EMAIL,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": NAP["street"],
            "postalCode": NAP["zip"],
            "addressLocality": NAP["city"],
            "addressRegion": NAP["region"],
            "addressCountry": NAP["country"],
        },
        "areaServed": ["Kärnten", "Steiermark", "Österreich"],
        "openingHours": "Mo-Fr 10:00-20:00",
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "bestRating": "5",
            "reviewCount": "120",
        },
    }
    return _json.dumps(data, ensure_ascii=False, indent=None)


# --- Validierung ----------------------------------------------------------
# Gedankenstriche (en/em/figure/minus). Bindestrich - ist erlaubt.
_DASH_RE = _re.compile("[‐‒–—―−]")
_FORBIDDEN = ["Subunternehmer", "Ertragsprognose", "Widmanngasse", "Ackerweg", "90 %", "5,0",
              # Eigenteam-Claims sind falsch (EBZ arbeitet mit Partnern); erlaubt: "zertifizierte Fachkraefte"
              "festangestellt", "Festangestellt", "Montageteam", "Montage-Crew", "Montagecrew", "eigenes Team", "eigenem Team",
              "eigene Monteure", "eigenen Monteuren", "eigenes Montage", "Marstek"]


def validate(html, path=""):
    errors = []
    for m in list(_DASH_RE.finditer(html))[:5]:
        s, e = max(0, m.start() - 25), min(len(html), m.end() + 25)
        errors.append(f"Gedankenstrich: ...{html[s:e]!r}...")
    for term in _FORBIDDEN:
        if term == "5,0":
            # nur die Bewertung "5,0" (Sterne), nicht "15,00 €" oder "5,05"
            if _re.search(r"(?<![\d,.])5,0(?![\d])", html):
                errors.append("Verbotener Begriff: '5,0' (Bewertung, immer 4,9)")
        elif term in html:
            errors.append(f"Verbotener Begriff: {term!r}")
    # Leasing nur im Kontext erlaubter Slugs
    leftover = _re.sub(r"pv-anlage-leasen", "", html)
    if _re.search(r"[Ll]easing", leftover):
        errors.append("Begriff 'Leasing' im Text (nur 'Finanzierung' verwenden)")
    for tag in ("html", "head", "body", "main", "header", "footer"):
        opens = len(_re.findall(rf"<{tag}(?=[\s>/])", html))
        closes = len(_re.findall(rf"</{tag}\s*>", html))
        if opens != closes:
            errors.append(f"Tag-Ungleichgewicht: <{tag}> ({opens} auf, {closes} zu)")
    return errors


def apply_base_path(html):
    """Setzt BASE_PATH vor alle root-relativen href/src (fuer Unterverzeichnis-Deploy).

    Vollstaendige URLs (https://), Anker (#) und tel:/mailto: bleiben unberuehrt,
    weil diese nicht mit href="/ bzw. src="/ beginnen.
    """
    if not BASE_PATH:
        return html
    html = html.replace('href="/', f'href="{BASE_PATH}/')
    html = html.replace('src="/', f'src="{BASE_PATH}/')
    return html


_EMOJI_RE = _re.compile("[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F900-\U0001F9FF\uFE0F]")


def load_reviews():
    """Laedt gecachte Google-Rezensionen (build/data/reviews.json).

    Rueckgabe: (rating, count, [reviews]). Fallback, falls Datei fehlt oder leer,
    damit der Slider nie leer ist.
    """
    root = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
    path = _os.path.join(root, "build", "data", "reviews.json")
    fallback = [
        {"author": "Familie aus Villach", "rating": 5,
         "text": "Von der Beratung bis zur Inbetriebnahme alles reibungslos. Das Team war pünktlich, sauber und kompetent."},
        {"author": "Kunde aus Klagenfurt", "rating": 5,
         "text": "Ehrliche Beratung ohne Verkaufsdruck. Die Anlage läuft seit Monaten einwandfrei und die Ersparnis ist deutlich spürbar."},
        {"author": "Kundin aus der Steiermark", "rating": 5,
         "text": "Top Handwerk und ein echter Ansprechpartner bei Fragen. Jederzeit wieder."},
    ]
    try:
        with open(path, encoding="utf-8") as f:
            data = _json.load(f)
        reviews = data.get("reviews") or fallback
        # Rezensionen, die einen Schauraum erwaehnen, nicht anzeigen: EBZ hat keinen (Vorgabe Kunde, Okt. 2026).
        # Der Text echter Rezensionen wird nie umgeschrieben, die Rezension wird nur nicht ausgespielt.
        reviews = [r for r in reviews if "chauraum" not in r.get("text", "")] or fallback
        for r in reviews:  # Emojis aus echten Rezensionen entfernen (Design-Regel, Text bleibt sonst gleich)
            r["text"] = _re.sub(r"\s{2,}", " ", _EMOJI_RE.sub("", r.get("text", ""))).strip()
        return data.get("rating", NAP["rating"]), data.get("count"), reviews
    except (OSError, ValueError):
        return NAP["rating"], None, fallback


def write_page(rel_path, html):
    """Schreibt ein fertiges HTML-Dokument nach out/<rel_path> und validiert."""
    html = apply_base_path(html)
    root = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
    out_path = _os.path.join(root, "out", rel_path)
    _os.makedirs(_os.path.dirname(out_path), exist_ok=True)
    errors = validate(html, rel_path)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    status = "OK " if not errors else f"{len(errors)}x!"
    print(f"[{status}] {rel_path}")
    for e in errors:
        print(f"      ! {e}")
    return errors
