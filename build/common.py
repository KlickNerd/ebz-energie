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

AUTHOR = "Mario Zintl"
AUTHOR_ROLE = "Geschäftsführung EBZ Energie GmbH"

# --- Slug-Verzeichnis -----------------------------------------------------
# Interne Verlinkung IMMER ueber href()/a(), nie hartkodierte Pfade.
S = {
    "home": "/",
    "photovoltaik": "/photovoltaik/",
    "batteriespeicher": "/batteriespeicher/",
    "waermepumpe": "/waermepumpen-installateur/",
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
    "pv_villach": "/photovoltaik-villach/",
    "pv_wolfsberg": "/photovoltaik-wolfsberg/",
    "marktpreis": "/marktpreis-2026/",
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
    "ems": "/assets/img/energiemanagement.png",
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
_FORBIDDEN = ["Subunternehmer", "Ertragsprognose", "Widmanngasse", "Ackerweg", "90 %", "5,0"]


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
