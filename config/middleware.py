"""Middlewares propios."""
from django.conf import settings


class StagingMiddleware:
    """En modo staging añade ``X-Robots-Tag: noindex, nofollow`` a todo.

    El resto del comportamiento de staging (robots.txt = Disallow: /, meta
    noindex, banner, email a consola, sin analítica) se resuelve en las
    plantillas, en las vistas de SEO y en settings.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if getattr(settings, "STAGING", False):
            response["X-Robots-Tag"] = "noindex, nofollow"
        return response
