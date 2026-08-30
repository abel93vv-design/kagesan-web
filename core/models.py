"""Modelos de la web de KageSan CRM (app ``core``).

Contiene el blog completo, los mensajes de contacto/demo y los testimonios de
la home. Las apps ``apps.blog`` y ``apps.pages`` solo aportan vistas/URLs/plantillas.
"""
from __future__ import annotations

import re

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

User = get_user_model()

WORDS_PER_MINUTE = 220


# ---------------------------------------------------------------------------
# Blog
# ---------------------------------------------------------------------------
class BlogCategory(models.Model):
    name = models.CharField("nombre", max_length=120, unique=True)
    slug = models.SlugField("slug", max_length=140, unique=True)
    tagline = models.CharField("lema", max_length=200, blank=True)
    intro = models.TextField("introducción", blank=True)
    core_url = models.CharField(
        "URL core", max_length=200, blank=True,
        help_text="Ruta interna que esta categoría debe reforzar (ej. /software-crm-inmobiliario).",
    )
    position = models.PositiveIntegerField("posición", default=0)

    class Meta:
        verbose_name = "categoría del blog"
        verbose_name_plural = "categorías del blog"
        ordering = ["position", "name"]

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("blog:entry", args=[self.slug])

    @property
    def published_posts(self):
        return self.posts.filter(status=BlogPost.STATUS_PUBLISHED)


class BlogAuthor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="blog_author", verbose_name="usuario"
    )
    slug = models.SlugField("slug", max_length=140, unique=True)
    display_name = models.CharField("nombre visible", max_length=120)
    role = models.CharField("cargo", max_length=140, blank=True)
    bio = models.TextField("biografía", blank=True)
    photo = models.ImageField("foto", upload_to="blog/autores/", blank=True)
    linkedin_url = models.URLField("LinkedIn", blank=True)
    company_url = models.URLField("web de la empresa", default="https://kagesancrm.com/")

    class Meta:
        verbose_name = "autor del blog"
        verbose_name_plural = "autores del blog"
        ordering = ["display_name"]

    def __str__(self) -> str:
        return self.display_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.display_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("blog:author")


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(
            status=BlogPost.STATUS_PUBLISHED, published_at__lte=timezone.now()
        )


class BlogPost(models.Model):
    STATUS_DRAFT = "borrador"
    STATUS_PUBLISHED = "publicado"
    STATUS_CHOICES = [
        (STATUS_DRAFT, "Borrador"),
        (STATUS_PUBLISHED, "Publicado"),
    ]

    title = models.CharField("título", max_length=200)
    slug = models.SlugField("slug", max_length=220, unique=True)
    status = models.CharField(
        "estado", max_length=12, choices=STATUS_CHOICES, default=STATUS_DRAFT
    )
    published_at = models.DateTimeField("fecha de publicación", null=True, blank=True)

    category = models.ForeignKey(
        BlogCategory, on_delete=models.PROTECT, related_name="posts", verbose_name="categoría"
    )
    author = models.ForeignKey(
        BlogAuthor, on_delete=models.PROTECT, related_name="posts", verbose_name="autor"
    )

    excerpt = models.TextField("extracto", help_text="80-120 palabras.")
    meta_description = models.CharField("meta description", max_length=300, help_text="140-160 caracteres.")
    focus_keyword = models.CharField("palabra clave objetivo", max_length=120)
    secondary_keywords = models.CharField("palabras clave secundarias", max_length=400, blank=True)
    tags = models.CharField("etiquetas", max_length=400, blank=True)
    primary_core_url = models.CharField(
        "URL core principal", max_length=200, blank=True,
        help_text="Ruta interna a la que enlaza el CTA de cierre (ej. /precios).",
    )

    cover_image = models.ImageField("imagen de portada", upload_to="blog/portadas/", blank=True)
    cover_image_alt = models.CharField("alt de la portada", max_length=200, blank=True)
    inline_image = models.ImageField("imagen intercalada", upload_to="blog/intercaladas/", blank=True)
    inline_image_alt = models.CharField("alt de la imagen intercalada", max_length=200, blank=True)

    body = models.TextField(
        "cuerpo",
        help_text="HTML. Usa el token [[IMAGEN]] en una línea para insertar la imagen intercalada.",
    )

    created_at = models.DateTimeField("creado", auto_now_add=True)
    updated_at = models.DateTimeField("actualizado", auto_now=True)

    objects = BlogPostQuerySet.as_manager()

    class Meta:
        verbose_name = "entrada del blog"
        verbose_name_plural = "entradas del blog"
        ordering = ["-published_at", "-created_at"]
        indexes = [models.Index(fields=["status", "published_at"])]

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:220]
        if self.status == self.STATUS_PUBLISHED and self.published_at is None:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("blog:entry", args=[self.slug])

    @property
    def is_published(self) -> bool:
        return self.status == self.STATUS_PUBLISHED and bool(self.published_at)

    @property
    def reading_time(self) -> int:
        words = len(re.sub(r"<[^>]+>", " ", self.body or "").split())
        return max(1, round(words / WORDS_PER_MINUTE))

    @property
    def keyword_list(self) -> list[str]:
        raw = ", ".join(filter(None, [self.secondary_keywords, self.tags]))
        return [k.strip() for k in raw.split(",") if k.strip()]

    @property
    def core_url_absolute(self) -> str:
        path = self.primary_core_url or "/contacto/"
        if path.startswith("http"):
            return path
        return f"{settings.SITE_BASE_URL}{path}"


class BlogFAQItem(models.Model):
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name="faqs", verbose_name="entrada"
    )
    question = models.CharField("pregunta", max_length=240)
    answer = models.TextField("respuesta")
    position = models.PositiveIntegerField("posición", default=0)

    class Meta:
        verbose_name = "FAQ del blog"
        verbose_name_plural = "FAQ del blog"
        ordering = ["position", "id"]

    def __str__(self) -> str:
        return self.question


# ---------------------------------------------------------------------------
# Contacto / demo
# ---------------------------------------------------------------------------
class ContactMessage(models.Model):
    ORIGIN_CONTACT = "contacto"
    ORIGIN_DEMO = "demo"
    ORIGIN_CHOICES = [
        (ORIGIN_CONTACT, "Contacto"),
        (ORIGIN_DEMO, "Solicitud de demo"),
    ]

    nombre = models.CharField(max_length=140)
    email = models.EmailField()
    empresa = models.CharField(max_length=180, blank=True)
    mensaje = models.TextField(blank=True)
    origen = models.CharField(
        "origen", max_length=12, choices=ORIGIN_CHOICES, default=ORIGIN_CONTACT
    )
    num_agentes = models.CharField("nº de agentes", max_length=40, blank=True)
    num_oficinas = models.CharField("nº de oficinas", max_length=40, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    tratado = models.BooleanField("tratado", default=False)

    class Meta:
        verbose_name = "mensaje de contacto"
        verbose_name_plural = "mensajes de contacto"
        ordering = ["-creado_en"]

    def __str__(self) -> str:
        return f"{self.nombre} <{self.email}> ({self.creado_en:%Y-%m-%d})"


# ---------------------------------------------------------------------------
# Testimonios (home)
# ---------------------------------------------------------------------------
class Testimonial(models.Model):
    autor = models.CharField("autor", max_length=140)
    empresa = models.CharField("empresa", max_length=180)
    texto = models.TextField("texto")
    foto = models.ImageField("foto", upload_to="testimonios/", blank=True)
    position = models.PositiveIntegerField("posición", default=0)
    activo = models.BooleanField("activo", default=True)

    class Meta:
        verbose_name = "testimonio"
        verbose_name_plural = "testimonios"
        ordering = ["position", "id"]

    def __str__(self) -> str:
        return f"{self.autor} — {self.empresa}"
