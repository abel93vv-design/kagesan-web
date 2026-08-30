"""Constructores de JSON-LD. Todas las URL salen de settings.SITE_BASE_URL."""
from __future__ import annotations

import re

from django.conf import settings

ORG_ID = "#organization"
WEBSITE_ID = "#website"
APP_ID = "#software"


def _abs(path: str) -> str:
    if not path:
        return settings.SITE_BASE_URL + "/"
    if path.startswith("http"):
        return path
    return f"{settings.SITE_BASE_URL}{path}"


def _strip_html(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", value or "")).strip()


def organization() -> dict:
    base = settings.SITE_BASE_URL
    same_as = [u for u in (settings.SOCIAL_LINKEDIN, settings.SOCIAL_INSTAGRAM) if u]
    data = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": f"{base}/{ORG_ID}",
        "name": "KageSan CRM",
        "url": base + "/",
        "logo": _abs("/static/img/logo.png"),
        "description": (
            "KageSan CRM es un CRM inmobiliario con matching por IA, pipeline "
            "visual y gestión multi-oficina para agencias y agentes en España."
        ),
        "email": settings.CONTACT_EMAIL,
        "areaServed": "ES",
    }
    if settings.CONTACT_PHONE_TEL:
        data["telephone"] = settings.CONTACT_PHONE_TEL
    if same_as:
        data["sameAs"] = same_as
    return data


def website() -> dict:
    base = settings.SITE_BASE_URL
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"{base}/{WEBSITE_ID}",
        "url": base + "/",
        "name": "KageSan CRM",
        "inLanguage": "es-ES",
        "publisher": {"@id": f"{base}/{ORG_ID}"},
    }


def software_application(name: str, description: str, path: str, offers: list | None = None) -> dict:
    base = settings.SITE_BASE_URL
    data = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "@id": f"{base}/{APP_ID}",
        "name": name,
        "url": _abs(path),
        "description": _strip_html(description),
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "Web",
        "inLanguage": "es-ES",
        "publisher": {"@id": f"{base}/{ORG_ID}"},
        "offers": offers if offers is not None else plan_offers(),
    }
    return data


def plan_offers() -> list[dict]:
    """Offers a partir de core.content.PLANS (importe mensual en EUR)."""
    from core.content import PLANS

    offers = []
    for plan in PLANS:
        offer = {
            "@type": "Offer",
            "name": f"KageSan CRM {plan['name']}",
            "category": plan["name"],
            "priceCurrency": "EUR",
            "url": _abs("/precios"),
        }
        if plan.get("price_eur") is not None:
            offer["price"] = str(plan["price_eur"])
        else:
            offer["priceSpecification"] = {
                "@type": "PriceSpecification",
                "priceCurrency": "EUR",
            }
        offers.append(offer)
    return offers


def defined_term_set(terms) -> dict:
    """terms: iterable de dicts con 'term' y 'definition'."""
    base = settings.SITE_BASE_URL
    return {
        "@context": "https://schema.org",
        "@type": "DefinedTermSet",
        "@id": _abs("/glosario-crm-inmobiliario") + "#glosario",
        "name": "Glosario de CRM inmobiliario",
        "url": _abs("/glosario-crm-inmobiliario"),
        "inLanguage": "es-ES",
        "hasDefinedTerm": [
            {
                "@type": "DefinedTerm",
                "name": t["term"],
                "description": _strip_html(t["definition"]),
                "inDefinedTermSet": _abs("/glosario-crm-inmobiliario") + "#glosario",
            }
            for t in terms
        ],
    }


def breadcrumb(items: list[tuple[str, str]]) -> dict:
    """items: lista de (nombre, ruta)."""
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                "item": _abs(path),
            }
            for i, (name, path) in enumerate(items)
        ],
    }


def faqpage(faqs) -> dict:
    """faqs: iterable de objetos con .question/.answer o de tuplas (q, a)."""
    entities = []
    for faq in faqs:
        if isinstance(faq, (tuple, list)):
            q, a = faq[0], faq[1]
        elif isinstance(faq, dict):
            q = faq.get("question") or faq.get("q")
            a = faq.get("answer") or faq.get("a")
        else:
            q, a = faq.question, faq.answer
        entities.append(
            {
                "@type": "Question",
                "name": _strip_html(q),
                "acceptedAnswer": {"@type": "Answer", "text": _strip_html(a)},
            }
        )
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities,
    }


def person_author(author) -> dict:
    base = settings.SITE_BASE_URL
    data = {
        "@type": "Person" if "Equipo" not in author.display_name else "Organization",
        "@id": f"{base}{author.get_absolute_url()}#author",
        "name": author.display_name,
        "url": _abs(author.get_absolute_url()),
        "worksFor": {"@id": f"{base}/{ORG_ID}"},
    }
    if author.role:
        data["jobTitle"] = author.role
    if author.bio:
        data["description"] = _strip_html(author.bio)
    sameas = [u for u in [author.linkedin_url] if u]
    if sameas:
        data["sameAs"] = sameas
    if author.photo:
        data["image"] = _abs(settings.MEDIA_URL + str(author.photo))
    return data


def profilepage(author) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "ProfilePage",
        "mainEntity": person_author(author),
    }


def blogposting(post) -> dict:
    base = settings.SITE_BASE_URL
    url = _abs(post.get_absolute_url())
    data = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "headline": post.title[:110],
        "description": post.meta_description or _strip_html(post.excerpt),
        "url": url,
        "inLanguage": "es-ES",
        "author": person_author(post.author),
        "publisher": {"@id": f"{base}/{ORG_ID}"},
        "isPartOf": {"@id": f"{base}/{WEBSITE_ID}"},
        "articleSection": post.category.name,
    }
    if post.published_at:
        data["datePublished"] = post.published_at.isoformat()
    if post.updated_at:
        data["dateModified"] = post.updated_at.isoformat()
    if post.cover_image:
        data["image"] = _abs(settings.MEDIA_URL + str(post.cover_image))
    kws = [post.focus_keyword] + post.keyword_list
    if any(kws):
        data["keywords"] = ", ".join([k for k in kws if k])
    return data
