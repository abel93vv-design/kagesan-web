from django.urls import path, re_path

from core.content import PILLARS, SEGMENTS

from . import views

app_name = "pages"

_PILLAR_RE = "|".join(PILLARS.keys())
_SEGMENT_RE = "|".join(SEGMENTS.keys())

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("precios", views.PreciosView.as_view(), name="precios"),
    path("glosario-crm-inmobiliario", views.GlosarioView.as_view(), name="glosario"),
    path("demo", views.DemoView.as_view(), name="demo"),
    path("sobre-kagesan", views.SobreView.as_view(), name="sobre"),
    path("contacto/", views.ContactView.as_view(), name="contacto"),
    path("aviso-legal/", views.LegalView.as_view(), {"page": "aviso"}, name="aviso-legal"),
    path(
        "politica-de-privacidad/",
        views.LegalView.as_view(),
        {"page": "privacidad"},
        name="privacidad",
    ),
    path(
        "politica-de-cookies/",
        views.LegalView.as_view(),
        {"page": "cookies"},
        name="cookies",
    ),
    re_path(rf"^(?P<slug>{_PILLAR_RE})$", views.PillarDetailView.as_view(), name="pillar"),
    re_path(rf"^(?P<slug>{_SEGMENT_RE})$", views.SegmentDetailView.as_view(), name="segment"),
]
