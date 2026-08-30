"""Filtros de apoyo para SEO en plantillas."""
import json

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="jsonld")
def jsonld(value):
    """Serializa un dict/list a JSON seguro para incrustar en <script type=ld+json>."""
    text = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    # Evita cierres de <script> inesperados.
    text = text.replace("</", "<\\/")
    return mark_safe(text)


@register.filter(name="breadcrumb_jsonld")
def breadcrumb_jsonld(pairs):
    """Convierte [(nombre, ruta), ...] en un dict BreadcrumbList."""
    from core import schema

    return schema.breadcrumb(list(pairs))


@register.filter(name="absolute")
def absolute(path):
    from django.conf import settings

    if not path:
        return settings.SITE_BASE_URL + "/"
    if str(path).startswith("http"):
        return path
    return f"{settings.SITE_BASE_URL}{path}"
