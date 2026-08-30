"""Contexto común disponible en todas las plantillas."""
from datetime import date

from django.conf import settings

from core import schema


# Navegación "Producto": páginas pilar de KageSan CRM.
NAV_PRODUCT = [
    {"slug": "software-crm-inmobiliario", "label": "Software CRM inmobiliario"},
    {"slug": "matching-inteligente-ia", "label": "Matching inteligente con IA"},
    {"slug": "gestion-multi-oficina", "label": "Gestión multi-oficina"},
    {"slug": "integraciones", "label": "Integraciones"},
]

# Páginas por tipo de agencia.
NAV_SEGMENTS = [
    {"slug": "crm-para-agentes-inmobiliarios-independientes", "label": "Agentes independientes"},
    {"slug": "crm-para-agencias-inmobiliarias", "label": "Agencias inmobiliarias"},
    {"slug": "crm-para-franquicias-inmobiliarias", "label": "Franquicias y redes"},
]


def site(request):
    return {
        "SITE_BASE_URL": settings.SITE_BASE_URL,
        "SITE_NAME": settings.SITE_NAME,
        "STAGING": settings.STAGING,
        "ANALYTICS_ENABLED": settings.ANALYTICS_ENABLED,
        "ANALYTICS_GA4_ID": settings.ANALYTICS_GA4_ID,
        "NAV_PRODUCT": NAV_PRODUCT,
        "NAV_SEGMENTS": NAV_SEGMENTS,
        "APP_URL": settings.APP_URL,
        "CONTACT_EMAIL": settings.CONTACT_EMAIL,
        "SUPPORT_EMAIL": settings.SUPPORT_EMAIL,
        "CONTACT_PHONE_DISPLAY": settings.CONTACT_PHONE_DISPLAY,
        "CONTACT_PHONE_TEL": settings.CONTACT_PHONE_TEL,
        "SOCIAL_LINKEDIN": settings.SOCIAL_LINKEDIN,
        "SOCIAL_INSTAGRAM": settings.SOCIAL_INSTAGRAM,
        "LEGAL_ENTITY": settings.LEGAL_ENTITY,
        "LEGAL_TAXID": settings.LEGAL_TAXID,
        "LEGAL_ADDRESS": settings.LEGAL_ADDRESS,
        "CURRENT_YEAR": date.today().year,
        "JSONLD_ORG": schema.organization(),
        "JSONLD_WEBSITE": schema.website(),
    }
