from django.contrib import admin, messages

from .models import (
    BlogAuthor,
    BlogCategory,
    BlogFAQItem,
    BlogPost,
    ContactMessage,
    Testimonial,
)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "empresa", "origen", "creado_en", "tratado")
    list_filter = ("tratado", "origen", "creado_en")
    search_fields = ("nombre", "email", "empresa", "mensaje")
    list_editable = ("tratado",)
    readonly_fields = (
        "nombre", "email", "empresa", "mensaje", "origen",
        "num_agentes", "num_oficinas", "creado_en",
    )
    date_hierarchy = "creado_en"

    def has_add_permission(self, request):
        return False


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("autor", "empresa", "position", "activo")
    list_editable = ("position", "activo")
    search_fields = ("autor", "empresa", "texto")


class BlogFAQItemInline(admin.TabularInline):
    model = BlogFAQItem
    extra = 3


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "position", "core_url")
    list_editable = ("position",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug")


@admin.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):
    list_display = ("display_name", "slug", "role", "user")
    prepopulated_fields = {"slug": ("display_name",)}
    search_fields = ("display_name", "role")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "status", "published_at", "updated_at")
    list_filter = ("status", "category", "author")
    search_fields = ("title", "slug", "focus_keyword", "excerpt")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"
    inlines = [BlogFAQItemInline]
    readonly_fields = ("created_at", "updated_at")
    actions = ["publicar", "pasar_a_borrador"]
    fieldsets = (
        (None, {"fields": ("title", "slug", "status", "published_at", "category", "author")}),
        ("SEO", {"fields": ("meta_description", "focus_keyword", "secondary_keywords", "tags", "primary_core_url")}),
        ("Contenido", {"fields": ("excerpt", "body")}),
        ("Imágenes", {"fields": ("cover_image", "cover_image_alt", "inline_image", "inline_image_alt")}),
        ("Fechas", {"fields": ("created_at", "updated_at")}),
    )

    @admin.action(description="Publicar entradas seleccionadas")
    def publicar(self, request, queryset):
        n = 0
        for post in queryset:
            post.status = BlogPost.STATUS_PUBLISHED
            post.save()
            n += 1
        self.message_user(request, f"{n} entrada(s) publicada(s).", messages.SUCCESS)

    @admin.action(description="Pasar a borrador")
    def pasar_a_borrador(self, request, queryset):
        n = queryset.update(status=BlogPost.STATUS_DRAFT)
        self.message_user(request, f"{n} entrada(s) en borrador.", messages.SUCCESS)
