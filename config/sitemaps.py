"""Sitemap basado en django.contrib.sitemaps (alternativa a la vista propia).

No se enruta por defecto: el sitemap.xml del sitio lo genera core.seo para
garantizar que las URL salen de SITE_BASE_URL. Se deja disponible por si en
el futuro se quiere el sitemap "vivo" de Django.
"""
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from core.content import PILLARS, SEGMENTS
from core.models import BlogCategory, BlogPost


class StaticViewSitemap(Sitemap):
    priority = 0.7
    changefreq = "monthly"
    protocol = "https"

    def items(self):
        return [
            "pages:home",
            "pages:precios",
            "pages:glosario",
            "pages:demo",
            "pages:sobre",
            "pages:contacto",
            "blog:index",
            "blog:categories",
            "blog:author",
        ]

    def location(self, item):
        return reverse(item)


class PillarSitemap(Sitemap):
    priority = 0.9
    changefreq = "monthly"
    protocol = "https"

    def items(self):
        return list(PILLARS.keys())

    def location(self, slug):
        return reverse("pages:pillar", args=[slug])


class SegmentSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"
    protocol = "https"

    def items(self):
        return list(SEGMENTS.keys())

    def location(self, slug):
        return reverse("pages:segment", args=[slug])


class BlogPostSitemap(Sitemap):
    priority = 0.7
    changefreq = "monthly"
    protocol = "https"

    def items(self):
        return BlogPost.objects.published()

    def lastmod(self, obj):
        return obj.updated_at or obj.published_at


class BlogCategorySitemap(Sitemap):
    priority = 0.5
    changefreq = "weekly"
    protocol = "https"

    def items(self):
        return BlogCategory.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()


SITEMAPS = {
    "static": StaticViewSitemap,
    "pillars": PillarSitemap,
    "segments": SegmentSitemap,
    "blog": BlogPostSitemap,
    "categories": BlogCategorySitemap,
}
