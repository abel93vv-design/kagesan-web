"""Smoke tests de las páginas fijas y de los formularios antispam."""
import time

from django.test import TestCase
from django.urls import reverse

from core.content import PILLARS, SEGMENTS
from core.models import ContactMessage


class RoutesTests(TestCase):
    def test_static_routes_ok(self):
        names = [
            "pages:home", "pages:precios", "pages:glosario", "pages:demo",
            "pages:sobre", "pages:contacto", "pages:aviso-legal",
            "pages:privacidad", "pages:cookies",
        ]
        for name in names:
            with self.subTest(name=name):
                self.assertEqual(self.client.get(reverse(name)).status_code, 200)

    def test_pillar_and_segment_pages_ok(self):
        for slug in PILLARS:
            self.assertEqual(self.client.get(reverse("pages:pillar", args=[slug])).status_code, 200)
        for slug in SEGMENTS:
            self.assertEqual(self.client.get(reverse("pages:segment", args=[slug])).status_code, 200)

    def test_unknown_pillar_is_404(self):
        self.assertEqual(self.client.get("/no-soy-una-pagina").status_code, 404)

    def test_home_has_jsonld(self):
        html = self.client.get(reverse("pages:home")).content.decode()
        self.assertIn('"@type":"SoftwareApplication"', html)
        self.assertIn('"@type":"FAQPage"', html)

    def test_precios_shows_real_prices(self):
        html = self.client.get(reverse("pages:precios")).content.decode()
        for token in ("49 €", "129 €", "A medida"):
            self.assertIn(token, html)

    def test_glosario_has_defined_term_set(self):
        html = self.client.get(reverse("pages:glosario")).content.decode()
        self.assertIn("DefinedTermSet", html)


class ContactFormTests(TestCase):
    def _payload(self, **over):
        data = {
            "nombre": "Ana Ejemplo",
            "email": "ana@example.com",
            "empresa": "Inmo Test",
            "mensaje": "Quiero información sobre los planes.",
            "consentimiento": "on",
            "iniciado": str(int(time.time()) - 5),
            "website": "",
        }
        data.update(over)
        return data

    def test_valid_submission_creates_message_and_redirects(self):
        resp = self.client.post(reverse("pages:contacto"), self._payload())
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactMessage.objects.get().origen, ContactMessage.ORIGIN_CONTACT)

    def test_honeypot_blocks_submission(self):
        resp = self.client.post(reverse("pages:contacto"), self._payload(website="http://spam"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_time_trap_blocks_instant_submission(self):
        resp = self.client.post(
            reverse("pages:contacto"), self._payload(iniciado=str(int(time.time())))
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_demo_form_stores_extra_fields(self):
        data = self._payload(num_agentes="8", num_oficinas="2", mensaje="")
        resp = self.client.post(reverse("pages:demo"), data)
        self.assertEqual(resp.status_code, 302)
        msg = ContactMessage.objects.get()
        self.assertEqual(msg.origen, ContactMessage.ORIGIN_DEMO)
        self.assertEqual(msg.num_agentes, "8")
