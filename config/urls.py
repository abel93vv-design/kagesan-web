"""URLconf raíz de la web de KageSan CRM."""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from config import views as project_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("robots.txt", project_views.robots_txt, name="robots-txt"),
    path("sitemap.xml", project_views.sitemap_xml, name="sitemap-xml"),
    path("llms.txt", project_views.llms_txt, name="llms-txt"),
    path("", include("apps.blog.urls")),
    path("", include("apps.pages.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "config.views.error_404"
handler403 = "config.views.error_403"
handler500 = "config.views.error_500"
