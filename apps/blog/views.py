"""Vistas del blog y de la página de autor."""
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from core import schema
from core.models import BlogAuthor, BlogCategory, BlogPost

PAGE_SIZE = 9


def _categories():
    return BlogCategory.objects.all()


class BlogIndexView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        posts = BlogPost.objects.published().select_related("category", "author")
        paginator = Paginator(posts, PAGE_SIZE)
        page = paginator.get_page(self.request.GET.get("page"))
        ctx.update(
            {
                "page_obj": page,
                "posts": page.object_list,
                "categories": _categories(),
                "meta_title": "Blog de KageSan CRM | CRM, matching e IA para inmobiliarias",
                "meta_description": (
                    "Guías sobre gestión de leads, matching por IA y digitalización de "
                    "agencias inmobiliarias, del equipo de KageSan CRM."
                ),
                "canonical_path": "/blog/",
                "breadcrumbs": [("Inicio", "/"), ("Blog", "")],
            }
        )
        return ctx


class BlogCategoriesView(TemplateView):
    template_name = "blog/categories.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                "categories": _categories(),
                "meta_title": "Categorías del blog | KageSan CRM",
                "meta_description": (
                    "Todas las categorías del blog de KageSan CRM: gestión de leads, "
                    "matching e IA, digitalización de agencias y elección de CRM."
                ),
                "canonical_path": "/blog/categorias/",
                "breadcrumbs": [("Inicio", "/"), ("Blog", "/blog/"), ("Categorías", "")],
            }
        )
        return ctx


def _render_category(request, category):
    posts = category.posts.filter(status=BlogPost.STATUS_PUBLISHED).select_related("author")
    paginator = Paginator(posts, PAGE_SIZE)
    page = paginator.get_page(request.GET.get("page"))
    context = {
        "category": category,
        "page_obj": page,
        "posts": page.object_list,
        "categories": _categories(),
        "meta_title": f"{category.name} | Blog de KageSan CRM",
        "meta_description": category.tagline
        or f"Artículos de la categoría {category.name} en el blog de KageSan CRM.",
        "canonical_path": category.get_absolute_url(),
        "breadcrumbs": [("Inicio", "/"), ("Blog", "/blog/"), (category.name, "")],
    }
    return render(request, "blog/category.html", context)


def _render_post(request, post):
    related = (
        BlogPost.objects.published()
        .filter(category=post.category)
        .exclude(pk=post.pk)
        .select_related("author")[:3]
    )
    jsonld = [schema.blogposting(post)]
    if post.faqs.exists():
        jsonld.append(schema.faqpage(post.faqs.all()))
    context = {
        "post": post,
        "related": related,
        "categories": _categories(),
        "meta_title": f"{post.title} | Blog de KageSan CRM",
        "meta_description": post.meta_description,
        "canonical_path": post.get_absolute_url(),
        "og_type": "article",
        "og_image_path": (post.cover_image.url if post.cover_image else None),
        "breadcrumbs": [
            ("Inicio", "/"),
            ("Blog", "/blog/"),
            (post.category.name, post.category.get_absolute_url()),
            (post.title, ""),
        ],
        "jsonld": jsonld,
    }
    return render(request, "blog/post.html", context)


def blog_entry(request, slug):
    """Ruta /blog/<slug>/: resuelve primero a categoría y si no, a entrada."""
    category = BlogCategory.objects.filter(slug=slug).first()
    if category is not None:
        return _render_category(request, category)
    post = get_object_or_404(
        BlogPost.objects.published().select_related("category", "author"), slug=slug
    )
    return _render_post(request, post)


class AuthorProfileView(TemplateView):
    template_name = "blog/author.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        author = BlogAuthor.objects.filter(slug="equipo-kagesan").first()
        if author is None:
            raise Http404("Autor no disponible.")
        posts = author.posts.filter(status=BlogPost.STATUS_PUBLISHED).select_related("category")
        ctx.update(
            {
                "author": author,
                "posts": posts,
                "meta_title": f"{author.display_name} | KageSan CRM",
                "meta_description": (
                    f"{author.display_name}: guías sobre CRM inmobiliario, matching por IA "
                    "y digitalización de agencias."
                ),
                "canonical_path": author.get_absolute_url(),
                "og_type": "profile",
                "breadcrumbs": [
                    ("Inicio", "/"),
                    ("Blog", "/blog/"),
                    (author.display_name, ""),
                ],
                "jsonld": [schema.profilepage(author)],
            }
        )
        return ctx
