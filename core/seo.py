"""Generación centralizada de robots.txt, sitemap.xml y llms.txt.

Regla de oro: todas las URL absolutas se construyen desde ``settings.SITE_BASE_URL``
(env ``DJANGO_SITE_URL``), nunca desde el host de la petición.

Estos tres artefactos se materializan como ARCHIVOS REALES en la raíz del
proyecto con ``manage.py generate_seo`` (los sirve Apache directamente en
producción). Las vistas de ``config/views.py`` los regeneran al vuelo como
fallback si el archivo no existe.
"""
from __future__ import annotations

import datetime as _dt
from xml.sax.saxutils import escape

from django.conf import settings
from django.urls import reverse

# Rutas estáticas indexables: (nombre_de_url, changefreq, priority)
STATIC_ROUTES = [
    ("pages:home", "weekly", "1.0"),
    ("pages:pillar", "monthly", "0.9"),   # se expande por slug más abajo
    ("pages:segment", "monthly", "0.8"),  # se expande por slug más abajo
    ("pages:precios", "monthly", "0.9"),
    ("pages:glosario", "monthly", "0.6"),
    ("pages:demo", "monthly", "0.8"),
    ("blog:index", "weekly", "0.8"),
    ("blog:categories", "monthly", "0.5"),
    ("pages:sobre", "yearly", "0.6"),
    ("pages:contacto", "yearly", "0.7"),
    ("blog:author", "monthly", "0.4"),
    ("pages:aviso-legal", "yearly", "0.2"),
    ("pages:privacidad", "yearly", "0.2"),
    ("pages:cookies", "yearly", "0.2"),
]


def _pillar_slugs() -> list[str]:
    from core.content import PILLARS

    return list(PILLARS.keys())


def _segment_slugs() -> list[str]:
    from core.content import SEGMENTS

    return list(SEGMENTS.keys())


def absolute_url(path: str) -> str:
    return f"{settings.SITE_BASE_URL}{path}"


def _iso(value) -> str:
    if value is None:
        return ""
    if isinstance(value, _dt.datetime):
        return value.date().isoformat()
    return value.isoformat()


def sitemap_entries() -> list[dict]:
    """Lista de entradas del sitemap como dicts (loc, lastmod, changefreq, priority)."""
    from core.models import BlogCategory, BlogPost

    entries: list[dict] = []
    seen: set[str] = set()

    def add(path, changefreq, priority, lastmod=None):
        if path in seen:
            return
        seen.add(path)
        entries.append(
            {
                "loc": absolute_url(path),
                "lastmod": _iso(lastmod),
                "changefreq": changefreq,
                "priority": priority,
            }
        )

    for name, changefreq, priority in STATIC_ROUTES:
        if name == "pages:pillar":
            for slug in _pillar_slugs():
                add(reverse("pages:pillar", args=[slug]), changefreq, priority)
            continue
        if name == "pages:segment":
            for slug in _segment_slugs():
                add(reverse("pages:segment", args=[slug]), changefreq, priority)
            continue
        try:
            add(reverse(name), changefreq, priority)
        except Exception:
            continue

    for category in BlogCategory.objects.all():
        add(category.get_absolute_url(), "weekly", "0.5")

    for post in BlogPost.objects.published():
        add(post.get_absolute_url(), "monthly", "0.7", lastmod=post.updated_at or post.published_at)

    return entries


def build_sitemap_xml() -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for entry in sitemap_entries():
        lines.append("  <url>")
        lines.append(f"    <loc>{escape(entry['loc'])}</loc>")
        if entry["lastmod"]:
            lines.append(f"    <lastmod>{entry['lastmod']}</lastmod>")
        lines.append(f"    <changefreq>{entry['changefreq']}</changefreq>")
        lines.append(f"    <priority>{entry['priority']}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def build_robots_txt() -> str:
    if settings.STAGING:
        return "User-agent: *\nDisallow: /\n"
    return (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /admin/\n"
        "Disallow: /contacto/?enviado=\n"
        "Disallow: /demo/?enviado=\n\n"
        f"Sitemap: {absolute_url('/sitemap.xml')}\n"
    )


def build_llms_txt() -> str:
    from core.models import BlogPost

    base = settings.SITE_BASE_URL
    out = [
        "# KageSan CRM",
        "",
        "> KageSan CRM es un CRM inmobiliario (SaaS) para el mercado español. "
        "Centraliza propiedades, clientes, tareas y equipo, y usa inteligencia "
        "artificial para emparejar compradores con propiedades (matching por "
        "score financiero y preferencias), con pipeline visual, gestión "
        "multi-oficina y planes desde un plan gratuito.",
        "",
        "## Páginas principales",
        f"- [Inicio]({base}/): qué es KageSan CRM y para quién.",
        f"- [Software CRM inmobiliario]({base}/software-crm-inmobiliario): funcionalidades del CRM.",
        f"- [Matching inteligente con IA]({base}/matching-inteligente-ia): cómo empareja clientes y propiedades.",
        f"- [Gestión multi-oficina]({base}/gestion-multi-oficina): redes y franquicias sobre un mismo sistema.",
        f"- [Integraciones]({base}/integraciones): portales, WhatsApp, email, web y API.",
        f"- [CRM para agentes independientes]({base}/crm-para-agentes-inmobiliarios-independientes).",
        f"- [CRM para agencias inmobiliarias]({base}/crm-para-agencias-inmobiliarias).",
        f"- [CRM para franquicias y redes]({base}/crm-para-franquicias-inmobiliarias).",
        f"- [Precios]({base}/precios): planes Free, Basic, Pro y Enterprise.",
        f"- [Glosario de CRM inmobiliario]({base}/glosario-crm-inmobiliario).",
        f"- [Demo]({base}/demo): solicitar una demo guiada.",
        f"- [Blog]({base}/blog/): guías sobre CRM, matching y digitalización de agencias.",
        f"- [Contacto]({base}/contacto/).",
        "",
        "## Artículos del blog",
    ]
    posts = list(BlogPost.objects.published()[:50])
    if posts:
        for post in posts:
            summary = (post.meta_description or post.excerpt or "").strip().replace("\n", " ")
            out.append(f"- [{post.title}]({base}{post.get_absolute_url()}): {summary}")
    else:
        out.append("- (aún no hay artículos publicados)")
    out += [
        "",
        "## Contacto",
        f"- Email: {settings.CONTACT_EMAIL}",
    ]
    if settings.CONTACT_PHONE_DISPLAY:
        out.append(f"- Teléfono: {settings.CONTACT_PHONE_DISPLAY}")
    out.append("")
    return "\n".join(out)


ARTIFACTS = {
    "robots.txt": build_robots_txt,
    "sitemap.xml": build_sitemap_xml,
    "llms.txt": build_llms_txt,
}


def write_artifacts(base_dir) -> list[str]:
    """Escribe los tres archivos en ``base_dir``. Devuelve la lista de rutas."""
    from pathlib import Path

    base = Path(base_dir)
    written = []
    for name, builder in ARTIFACTS.items():
        path = base / name
        path.write_text(builder(), encoding="utf-8")
        written.append(str(path))
    return written
