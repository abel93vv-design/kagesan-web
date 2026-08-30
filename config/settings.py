"""Configuración de Django para la web de KageSan CRM.

Todo se controla por variables de entorno (ver .env.example). El lector de
.env es propio (config/env.py) y no sobrescribe variables reales del entorno,
por lo que en cPanel basta con definirlas en "Setup Python App".
"""
from __future__ import annotations

import sys
from pathlib import Path

from config.env import env, env_bool, env_int, env_list, load_env

BASE_DIR = Path(__file__).resolve().parent.parent

# Carga .env de la raíz del proyecto (si existe).
load_env(BASE_DIR / ".env")

RUNNING_TESTS = "test" in sys.argv

# --------------------------------------------------------------------------
# Núcleo
# --------------------------------------------------------------------------
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    "django-insecure-solo-para-desarrollo-cambia-esto-en-produccion",
)

DEBUG = env_bool("DJANGO_DEBUG", False)
STAGING = env_bool("DJANGO_STAGING", False)

# HTTPS activo salvo que se desactive explícitamente (Docker en http://localhost).
HTTPS = env_bool("DJANGO_HTTPS", True)

ALLOWED_HOSTS = env_list(
    "DJANGO_ALLOWED_HOSTS",
    ["localhost", "127.0.0.1", "[::1]"] if (DEBUG or RUNNING_TESTS) else [],
)

# URL canónica: fuente de verdad para canonical, og:url, JSON-LD y sitemap.
SITE_BASE_URL = (env("DJANGO_SITE_URL", "https://kagesancrm.com") or "").rstrip("/")
SITE_NAME = "KageSan CRM"

CSRF_TRUSTED_ORIGINS = env_list("DJANGO_CSRF_TRUSTED_ORIGINS", [])
if not CSRF_TRUSTED_ORIGINS and SITE_BASE_URL.startswith("http"):
    CSRF_TRUSTED_ORIGINS = [SITE_BASE_URL]

# --------------------------------------------------------------------------
# Marca / contacto (placeholders; sustituir por datos reales antes de publicar)
# --------------------------------------------------------------------------
APP_URL = (env("KAGESAN_APP_URL", "https://app.kagesancrm.com") or "").rstrip("/")
CONTACT_EMAIL = env("KAGESAN_CONTACT_EMAIL", "hola@kagesancrm.com")
SUPPORT_EMAIL = env("KAGESAN_SUPPORT_EMAIL", "soporte@kagesancrm.com")
CONTACT_PHONE_DISPLAY = env("KAGESAN_CONTACT_PHONE_DISPLAY", "")
CONTACT_PHONE_TEL = env("KAGESAN_CONTACT_PHONE_TEL", "")
SOCIAL_LINKEDIN = env("KAGESAN_SOCIAL_LINKEDIN", "")
SOCIAL_INSTAGRAM = env("KAGESAN_SOCIAL_INSTAGRAM", "")
LEGAL_ENTITY = env("KAGESAN_LEGAL_ENTITY", "[COMPLETAR: razón social]")
LEGAL_TAXID = env("KAGESAN_LEGAL_TAXID", "[COMPLETAR: NIF/CIF]")
LEGAL_ADDRESS = env("KAGESAN_LEGAL_ADDRESS", "[COMPLETAR: domicilio]")

# --------------------------------------------------------------------------
# Aplicaciones
# --------------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "core",
    "apps.blog",
    "apps.pages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "config.middleware.StagingMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "config.context_processors.site",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# --------------------------------------------------------------------------
# Base de datos: MySQL en producción, SQLite en local.
# --------------------------------------------------------------------------
_db_engine = (env("DJANGO_DB_ENGINE", "") or "").lower()
_db_name = env("DJANGO_DB_NAME", "")

if _db_engine in ("mysql", "django.db.backends.mysql") or _db_name:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": _db_name,
            "USER": env("DJANGO_DB_USER", ""),
            "PASSWORD": env("DJANGO_DB_PASSWORD", ""),
            "HOST": env("DJANGO_DB_HOST", "localhost"),
            "PORT": env("DJANGO_DB_PORT", "3306"),
            "OPTIONS": {"charset": "utf8mb4"},
            "CONN_MAX_AGE": env_int("DJANGO_DB_CONN_MAX_AGE", 60),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": env("DJANGO_SQLITE_PATH", "") or (BASE_DIR / "db.sqlite3"),
        }
    }

# --------------------------------------------------------------------------
# Contraseñas / auth
# --------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------------------------------------------------------
# Internacionalización
# --------------------------------------------------------------------------
LANGUAGE_CODE = "es-es"
TIME_ZONE = "Europe/Madrid"
USE_I18N = True
USE_TZ = True

# --------------------------------------------------------------------------
# Estáticos y media
# --------------------------------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

_use_manifest = env_bool(
    "DJANGO_MANIFEST_STATIC", not DEBUG and not RUNNING_TESTS
)
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage.CompressedManifestStaticFilesStorage"
            if _use_manifest
            else "whitenoise.storage.CompressedStaticFilesStorage"
        )
    },
}
WHITENOISE_MAX_AGE = 60 * 60 * 24 * 30

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Carpeta donde se materializan robots.txt / sitemap.xml / llms.txt.
SEO_ARTIFACTS_DIR = BASE_DIR

# --------------------------------------------------------------------------
# Seguridad (activa cuando no hay DEBUG y hay HTTPS)
# --------------------------------------------------------------------------
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "same-origin"
X_FRAME_OPTIONS = "DENY"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

if not DEBUG and HTTPS and not RUNNING_TESTS:
    SECURE_SSL_REDIRECT = True
    _ssl_host = env("DJANGO_SSL_HOST", "")
    if _ssl_host:
        SECURE_SSL_HOST = _ssl_host
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # HSTS: en staging sin preload; en producción con preload.
    SECURE_HSTS_SECONDS = 0 if STAGING else 60 * 60 * 24 * 365
    SECURE_HSTS_INCLUDE_SUBDOMAINS = not STAGING
    SECURE_HSTS_PRELOAD = not STAGING
else:
    SECURE_SSL_REDIRECT = False

# --------------------------------------------------------------------------
# Email: consola en local/staging, SMTP en producción.
# --------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env("DJANGO_DEFAULT_FROM_EMAIL", "KageSan CRM <hola@kagesancrm.com>")
SERVER_EMAIL = DEFAULT_FROM_EMAIL
CONTACT_RECIPIENTS = env_list("DJANGO_CONTACT_RECIPIENTS", ["hola@kagesancrm.com"])

if STAGING or DEBUG or RUNNING_TESTS or not env("DJANGO_EMAIL_HOST", ""):
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = env("DJANGO_EMAIL_HOST", "")
    EMAIL_PORT = env_int("DJANGO_EMAIL_PORT", 587)
    EMAIL_HOST_USER = env("DJANGO_EMAIL_HOST_USER", "")
    EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_HOST_PASSWORD", "")
    EMAIL_USE_TLS = env_bool("DJANGO_EMAIL_USE_TLS", True)
    EMAIL_USE_SSL = env_bool("DJANGO_EMAIL_USE_SSL", False)

# --------------------------------------------------------------------------
# Analítica y terceros (desactivado por defecto)
# --------------------------------------------------------------------------
ANALYTICS_ENABLED = env_bool("ANALYTICS_ENABLED", False) and not STAGING
ANALYTICS_GA4_ID = env("ANALYTICS_GA4_ID", "")

# --------------------------------------------------------------------------
# Logging
# --------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "[{levelname}] {name}: {message}", "style": "{"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple"},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {
        "django.request": {"handlers": ["console"], "level": "ERROR", "propagate": False},
    },
}
