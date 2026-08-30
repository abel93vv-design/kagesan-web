"""Tests del blog: contenido sembrado, rutas y SEO."""
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from core.models import BlogCategory, BlogPost


class BlogContentTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_content", "--publish", verbosity=0)

    def test_six_posts_published(self):
        self.assertEqual(BlogPost.objects.published().count(), 6)

    def test_four_categories(self):
        self.assertEqual(BlogCategory.objects.count(), 4)

    def test_index_and_categories_ok(self):
        self.assertEqual(self.client.get(reverse("blog:index")).status_code, 200)
        self.assertEqual(self.client.get(reverse("blog:categories")).status_code, 200)
        self.assertEqual(self.client.get(reverse("blog:author")).status_code, 200)

    def test_every_post_and_category_page_ok(self):
        for post in BlogPost.objects.published():
            with self.subTest(slug=post.slug):
                r = self.client.get(post.get_absolute_url())
                self.assertEqual(r.status_code, 200)
                self.assertIn("BlogPosting", r.content.decode())
        for cat in BlogCategory.objects.all():
            self.assertEqual(self.client.get(cat.get_absolute_url()).status_code, 200)

    def test_post_with_faqs_emits_faqpage(self):
        post = BlogPost.objects.get(slug="como-elegir-crm-inmobiliario")
        html = self.client.get(post.get_absolute_url()).content.decode()
        self.assertIn('"@type":"FAQPage"', html)


class SeoArtifactTests(TestCase):
    """Prueba los generadores de core.seo directamente (no la vista, que puede
    servir un archivo ya materializado en disco)."""

    @classmethod
    def setUpTestData(cls):
        call_command("seed_content", "--publish", verbosity=0)

    def test_sitemap_has_domain_and_blog_urls(self):
        from core.seo import build_sitemap_xml

        xml = build_sitemap_xml()
        self.assertIn("https://kagesancrm.com/", xml)
        self.assertIn("/blog/crm-vs-excel-inmobiliaria/", xml)
        self.assertIn("https://kagesancrm.com/precios", xml)

    def test_robots_points_to_sitemap(self):
        from core.seo import build_robots_txt

        self.assertIn("Sitemap: https://kagesancrm.com/sitemap.xml", build_robots_txt())

    def test_llms_txt_lists_posts(self):
        from core.seo import build_llms_txt

        txt = build_llms_txt()
        self.assertIn("# KageSan CRM", txt)
        self.assertIn("/blog/que-es-matching-inmobiliario/", txt)

    def test_llms_view_ok(self):
        self.assertEqual(self.client.get("/llms.txt").status_code, 200)
