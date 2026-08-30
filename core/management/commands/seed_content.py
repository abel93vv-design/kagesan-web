"""Carga el contenido inicial del blog de KageSan CRM.

Crea (de forma idempotente):
  - el autor "Equipo KageSan" (con un usuario Django asociado),
  - las categorías del blog,
  - los testimonios de la home (marcados como "ejemplo"),
  - las 6 entradas del blog.

Uso::

    python manage.py seed_content                # entradas en BORRADOR
    python manage.py seed_content --publish      # además las publica
    python manage.py seed_content --refresh      # reescribe el cuerpo de las entradas
"""
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from core.models import (
    BlogAuthor,
    BlogCategory,
    BlogFAQItem,
    BlogPost,
    Testimonial,
)
from core.seed_blog import CATEGORIES, POSTS, TESTIMONIALS

User = get_user_model()

AUTHOR = {
    "username": "equipo-kagesan",
    "display_name": "Equipo KageSan",
    "slug": "equipo-kagesan",
    "role": "Equipo de producto de KageSan CRM",
    "bio": (
        "El equipo de producto de KageSan CRM publica guías sobre gestión "
        "inmobiliaria, matching por IA y digitalización de agencias, a partir "
        "de lo que vemos en el día a día de las inmobiliarias que usan KageSan."
    ),
    "company_url": "https://kagesancrm.com/",
}


class Command(BaseCommand):
    help = "Carga el contenido inicial del blog de KageSan CRM."

    def add_arguments(self, parser):
        parser.add_argument("--publish", action="store_true")
        parser.add_argument("--refresh", action="store_true")

    def handle(self, *args, **options):
        author = self._author()
        categories = self._categories()
        self._testimonials()
        self._posts(author, categories, options["publish"], options["refresh"])
        self.stdout.write(self.style.SUCCESS("seed_content completado."))

    # ------------------------------------------------------------------
    def _author(self):
        user, _ = User.objects.get_or_create(
            username=AUTHOR["username"],
            defaults={"email": "hola@kagesancrm.com", "is_active": False},
        )
        author, _ = BlogAuthor.objects.get_or_create(user=user)
        author.display_name = AUTHOR["display_name"]
        author.slug = AUTHOR["slug"]
        author.role = AUTHOR["role"]
        author.bio = author.bio or AUTHOR["bio"]
        author.company_url = AUTHOR["company_url"]
        author.save()
        self.stdout.write(f"Autor: {author.display_name}")
        return author

    def _categories(self):
        out = {}
        for data in CATEGORIES:
            cat, _ = BlogCategory.objects.get_or_create(slug=data["slug"])
            cat.name = data["name"]
            cat.tagline = data["tagline"]
            cat.intro = data["intro"]
            cat.core_url = data["core_url"]
            cat.position = data["position"]
            cat.save()
            out[data["slug"]] = cat
        self.stdout.write(f"Categorías: {len(out)}")
        return out

    def _testimonials(self):
        for data in TESTIMONIALS:
            obj, _ = Testimonial.objects.get_or_create(
                autor=data["autor"], empresa=data["empresa"]
            )
            obj.texto = data["texto"]
            obj.position = data["position"]
            obj.activo = True
            obj.save()
        self.stdout.write(f"Testimonios: {len(TESTIMONIALS)}")

    def _posts(self, author, categories, publish, refresh):
        created_n = updated_n = skipped_n = 0
        status = BlogPost.STATUS_PUBLISHED if publish else BlogPost.STATUS_DRAFT

        for data in POSTS:
            existing = BlogPost.objects.filter(slug=data["slug"]).first()
            if existing and not refresh:
                if publish and existing.status != BlogPost.STATUS_PUBLISHED:
                    existing.status = BlogPost.STATUS_PUBLISHED
                    existing.save()
                    updated_n += 1
                else:
                    skipped_n += 1
                continue

            fields = {
                "title": data["title"],
                "category": categories[data["category"]],
                "author": author,
                "excerpt": data["excerpt"],
                "meta_description": data["meta_description"],
                "focus_keyword": data["focus_keyword"],
                "secondary_keywords": data["secondary_keywords"],
                "tags": data["tags"],
                "primary_core_url": data["primary_core_url"],
                "body": data["body"].strip(),
                "status": status,
            }
            post, created = BlogPost.objects.update_or_create(
                slug=data["slug"], defaults=fields
            )
            post.faqs.all().delete()
            for i, faq in enumerate(data.get("faqs", [])):
                BlogFAQItem.objects.create(
                    post=post, question=faq["question"], answer=faq["answer"], position=i
                )
            created_n += int(created)
            updated_n += int(not created)

        self.stdout.write(
            f"Entradas: {created_n} creadas, {updated_n} actualizadas, "
            f"{skipped_n} sin cambios ({'publicadas' if publish else 'en borrador'})."
        )
