"""Vistas a nivel de proyecto: artefactos SEO y páginas de error.

Los artefactos (robots.txt, sitemap.xml, llms.txt) se sirven como archivo real
en producción (Apache) y estas vistas actúan de fallback: si el archivo existe
en la raíz, se devuelve su contenido; si no, se regenera al vuelo.
"""
from pathlib import Path

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from core import seo


def _serve(filename: str, builder, content_type: str) -> HttpResponse:
    path = Path(settings.SEO_ARTIFACTS_DIR) / filename
    if path.exists():
        return HttpResponse(path.read_text(encoding="utf-8"), content_type=content_type)
    return HttpResponse(builder(), content_type=content_type)


def robots_txt(request):
    # En staging siempre Disallow: / aunque exista un archivo antiguo.
    if settings.STAGING:
        return HttpResponse("User-agent: *\nDisallow: /\n", content_type="text/plain")
    return _serve("robots.txt", seo.build_robots_txt, "text/plain")


def sitemap_xml(request):
    return _serve("sitemap.xml", seo.build_sitemap_xml, "application/xml")


def llms_txt(request):
    return _serve("llms.txt", seo.build_llms_txt, "text/plain; charset=utf-8")


# --- Páginas de error con el diseño del sitio ---------------------------
def error_404(request, exception=None):
    return render(request, "404.html", status=404)


def error_403(request, exception=None):
    return render(request, "403.html", status=403)


def error_500(request):
    return render(request, "500.html", status=500)
