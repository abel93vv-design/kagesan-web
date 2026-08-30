"""Vistas de las páginas fijas: home, pilar, segmento, precios, glosario,
demo, sobre, contacto y legales."""
from django.conf import settings
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.html import strip_tags
from django.views.generic import TemplateView, View

from core import schema
from core.content import (
    DEMO_FAQS,
    DEMO_POINTS,
    GLOSSARY_TERMS,
    HOME_BENTO,
    HOME_FAQS,
    PILLARS,
    PLAN_TABLE,
    PLANS,
    PRECIOS_FAQS,
    SEGMENTS,
)
from core.models import BlogPost, Testimonial

from .forms import ContactForm, DemoForm


def _faq_tuples(faqs):
    return [(f["q"], f["a"]) for f in faqs]


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                "testimonials": Testimonial.objects.filter(activo=True),
                "latest_posts": BlogPost.objects.published().select_related("category")[:3],
                "home_faqs": HOME_FAQS,
                "home_bento": HOME_BENTO,
                "plans": PLANS,
                "meta_title": "KageSan CRM | CRM inmobiliario con matching por IA",
                "meta_description": (
                    "KageSan CRM centraliza propiedades, clientes y equipo, y empareja "
                    "compradores con propiedades con IA. Pipeline visual y gestión "
                    "multi-oficina. Empieza gratis."
                ),
                "canonical_path": "/",
                "jsonld": [
                    schema.software_application(
                        "KageSan CRM",
                        "CRM inmobiliario con matching por IA, pipeline visual y gestión multi-oficina.",
                        "/",
                    ),
                    schema.faqpage(_faq_tuples(HOME_FAQS)),
                ],
            }
        )
        return ctx


class PillarDetailView(TemplateView):
    template_name = "pages/pillar_detail.html"

    def get_context_data(self, slug, **kwargs):
        ctx = super().get_context_data(**kwargs)
        data = PILLARS.get(slug)
        if data is None:
            raise Http404("Página no encontrada.")
        path = reverse("pages:pillar", args=[slug])
        ctx.update(
            {
                "slug": slug,
                "p": data,
                "meta_title": data["meta_title"],
                "meta_description": data["meta_description"],
                "canonical_path": path,
                "breadcrumbs": [("Inicio", "/"), ("Producto", ""), (data["name"], "")],
                "jsonld": [
                    schema.software_application(data["name"], data["meta_description"], path),
                    schema.faqpage(_faq_tuples(data["faqs"])),
                ],
            }
        )
        return ctx


class SegmentDetailView(TemplateView):
    template_name = "pages/segment_detail.html"

    def get_context_data(self, slug, **kwargs):
        ctx = super().get_context_data(**kwargs)
        data = SEGMENTS.get(slug)
        if data is None:
            raise Http404("Página no encontrada.")
        path = reverse("pages:segment", args=[slug])
        ctx.update(
            {
                "slug": slug,
                "s": data,
                "meta_title": data["meta_title"],
                "meta_description": data["meta_description"],
                "canonical_path": path,
                "breadcrumbs": [("Inicio", "/"), (data["name"], "")],
                "jsonld": [schema.faqpage(_faq_tuples(data["faqs"]))],
            }
        )
        return ctx


class PreciosView(TemplateView):
    template_name = "pages/precios.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                "plans": PLANS,
                "plan_table": PLAN_TABLE,
                "precios_faqs": PRECIOS_FAQS,
                "meta_title": "Precios de KageSan CRM | Free, Basic, Pro y Enterprise",
                "meta_description": (
                    "Planes de KageSan CRM: Free (0 €), Basic (49 €/mes), Pro (129 €/mes) y "
                    "Enterprise a medida. Matching por IA en todos los planes."
                ),
                "canonical_path": "/precios",
                "breadcrumbs": [("Inicio", "/"), ("Precios", "")],
                "jsonld": [
                    schema.software_application(
                        "KageSan CRM",
                        "CRM inmobiliario con planes Free, Basic, Pro y Enterprise.",
                        "/precios",
                    ),
                    schema.faqpage(_faq_tuples(PRECIOS_FAQS)),
                ],
            }
        )
        return ctx


class GlosarioView(TemplateView):
    template_name = "pages/glosario.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                "terms": GLOSSARY_TERMS,
                "meta_title": "Glosario de CRM inmobiliario | KageSan CRM",
                "meta_description": (
                    "Pipeline, lead scoring, matching, score financiero... Los términos clave "
                    "de CRM y tecnología inmobiliaria explicados en simple."
                ),
                "canonical_path": "/glosario-crm-inmobiliario",
                "breadcrumbs": [("Inicio", "/"), ("Glosario", "")],
                "jsonld": [schema.defined_term_set(GLOSSARY_TERMS)],
            }
        )
        return ctx


class SobreView(TemplateView):
    template_name = "pages/sobre.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                "meta_title": "Sobre KageSan CRM | El CRM inmobiliario con matching por IA",
                "meta_description": (
                    "Qué es KageSan CRM, para quién y cómo aborda la gestión inmobiliaria: "
                    "matching por IA, pipeline visual y multi-oficina."
                ),
                "canonical_path": "/sobre-kagesan",
                "breadcrumbs": [("Inicio", "/"), ("Sobre KageSan CRM", "")],
            }
        )
        return ctx


class _FormPageView(View):
    """Base para páginas con formulario antispam (contacto / demo)."""

    form_class = None
    template_name = ""
    subject_prefix = ""

    def extra_context(self):
        return {}

    def get(self, request):
        enviado = request.GET.get("enviado") == "1"
        ctx = {"form": self.form_class(), "enviado": enviado}
        ctx.update(self.extra_context())
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            msg = form.save()
            self._notify(msg)
            return redirect(f"{request.path}?enviado=1")
        ctx = {"form": form, "enviado": False}
        ctx.update(self.extra_context())
        return render(request, self.template_name, ctx)

    def _notify(self, msg):
        cuerpo = (
            f"Nuevo mensaje ({msg.get_origen_display()}) en {settings.SITE_BASE_URL}\n\n"
            f"Nombre: {msg.nombre}\n"
            f"Email: {msg.email}\n"
            f"Empresa: {msg.empresa or '-'}\n"
        )
        if msg.origen == msg.ORIGIN_DEMO:
            cuerpo += (
                f"Nº de agentes: {msg.num_agentes or '-'}\n"
                f"Nº de oficinas: {msg.num_oficinas or '-'}\n"
            )
        cuerpo += (
            f"Fecha: {msg.creado_en:%d/%m/%Y %H:%M}\n\n"
            f"Mensaje:\n{strip_tags(msg.mensaje) or '-'}\n"
        )
        send_mail(
            subject=f"{self.subject_prefix}: {msg.nombre}",
            message=cuerpo,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=settings.CONTACT_RECIPIENTS,
            fail_silently=True,
        )


class ContactView(_FormPageView):
    form_class = ContactForm
    template_name = "pages/contacto.html"
    subject_prefix = "[KageSan CRM] Contacto web"

    def extra_context(self):
        return {
            "meta_title": "Contacto | KageSan CRM",
            "meta_description": (
                "Escríbenos para resolver dudas sobre KageSan CRM, planes o integraciones."
            ),
            "canonical_path": "/contacto/",
            "breadcrumbs": [("Inicio", "/"), ("Contacto", "")],
        }


class DemoView(_FormPageView):
    form_class = DemoForm
    template_name = "pages/demo.html"
    subject_prefix = "[KageSan CRM] Solicitud de demo"

    def extra_context(self):
        return {
            "demo_points": DEMO_POINTS,
            "demo_faqs": DEMO_FAQS,
            "meta_title": "Solicita una demo de KageSan CRM",
            "meta_description": (
                "Ve en 20 minutos cómo el matching por IA, el pipeline visual y los reportes "
                "de KageSan CRM organizan tu agencia. Reserva tu demo."
            ),
            "canonical_path": "/demo",
            "breadcrumbs": [("Inicio", "/"), ("Demo", "")],
            "jsonld": [schema.faqpage(_faq_tuples(DEMO_FAQS))],
        }


class LegalView(TemplateView):
    PAGES = {
        "aviso": {
            "template": "pages/legal_aviso.html",
            "title": "Aviso legal | KageSan CRM",
            "description": "Aviso legal y condiciones de uso de kagesancrm.com.",
            "path": "/aviso-legal/",
            "label": "Aviso legal",
        },
        "privacidad": {
            "template": "pages/legal_privacidad.html",
            "title": "Política de privacidad | KageSan CRM",
            "description": "Cómo trata KageSan CRM los datos personales recogidos en kagesancrm.com.",
            "path": "/politica-de-privacidad/",
            "label": "Política de privacidad",
        },
        "cookies": {
            "template": "pages/legal_cookies.html",
            "title": "Política de cookies | KageSan CRM",
            "description": "Información sobre las cookies que utiliza kagesancrm.com.",
            "path": "/politica-de-cookies/",
            "label": "Política de cookies",
        },
    }

    def get_template_names(self):
        return [self.PAGES[self.kwargs["page"]]["template"]]

    def get_context_data(self, page, **kwargs):
        ctx = super().get_context_data(**kwargs)
        meta = self.PAGES[page]
        ctx.update(
            {
                "meta_title": meta["title"],
                "meta_description": meta["description"],
                "canonical_path": meta["path"],
                "breadcrumbs": [("Inicio", "/"), (meta["label"], "")],
            }
        )
        return ctx
