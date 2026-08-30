"""Genera robots.txt, sitemap.xml y llms.txt como archivos reales en la raíz.

Se ejecuta en cada despliegue (.cpanel.yml). En producción Apache sirve estos
archivos directamente; las vistas de config/views.py son el fallback.
"""
from django.conf import settings
from django.core.management.base import BaseCommand

from core import seo


class Command(BaseCommand):
    help = "Genera robots.txt, sitemap.xml y llms.txt en la raíz del proyecto."

    def add_arguments(self, parser):
        parser.add_argument(
            "--check",
            action="store_true",
            help="No escribe; solo muestra lo que se generaría.",
        )

    def handle(self, *args, **options):
        if options["check"]:
            for name, builder in seo.ARTIFACTS.items():
                self.stdout.write(self.style.MIGRATE_HEADING(f"--- {name} ---"))
                self.stdout.write(builder())
            return

        written = seo.write_artifacts(settings.SEO_ARTIFACTS_DIR)
        for path in written:
            self.stdout.write(self.style.SUCCESS(f"escrito {path}"))
        if settings.STAGING:
            self.stdout.write(
                self.style.WARNING("modo staging: robots.txt = Disallow: /")
            )
