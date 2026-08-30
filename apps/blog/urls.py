from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("blog/", views.BlogIndexView.as_view(), name="index"),
    path("blog/categorias/", views.BlogCategoriesView.as_view(), name="categories"),
    path("autor/equipo-kagesan/", views.AuthorProfileView.as_view(), name="author"),
    # Ruta compartida: primero intenta categoría, luego entrada.
    path("blog/<slug:slug>/", views.blog_entry, name="entry"),
]
