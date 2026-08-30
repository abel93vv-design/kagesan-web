"""Crea un superusuario a partir de variables de entorno. Idempotente.

Pensado para cPanel sin terminal: define en la app de Python
  DJANGO_ADMIN_USER, DJANGO_ADMIN_PASSWORD y (opcional) DJANGO_ADMIN_EMAIL
y el despliegue (.cpanel.yml) lo crea en el primer deploy.

Si el usuario ya existe, solo se asegura de que sea staff + superuser; NO
cambia la contraseña (así puedes cambiarla luego desde el admin sin que el
siguiente deploy la pise).
"""
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Crea/asegura un superusuario desde DJANGO_ADMIN_USER/PASSWORD/EMAIL."

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ.get("DJANGO_ADMIN_USER", "").strip()
        password = os.environ.get("DJANGO_ADMIN_PASSWORD", "")
        email = os.environ.get("DJANGO_ADMIN_EMAIL", "").strip()

        if not username or not password:
            self.stdout.write("DJANGO_ADMIN_USER/PASSWORD no definidos; no se crea admin.")
            return

        user, created = User.objects.get_or_create(
            username=username, defaults={"email": email}
        )
        user.is_staff = True
        user.is_superuser = True
        if email:
            user.email = email
        if created:
            user.set_password(password)
        user.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Superusuario {'creado' if created else 'verificado'}: {username}"
            )
        )
