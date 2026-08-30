# Web de KageSan CRM

Sitio de marketing y SEO de **KageSan CRM** (CRM inmobiliario con matching por
IA, pipeline visual y gestión multi-oficina). Mismo enfoque técnico que
`Inmocro-web`: proyecto **Django + Passenger** que se despliega en cPanel
(Banahosting) y sustituye al WordPress del dominio.

Dirección visual: lenguaje tipo criteo.com (héroe oscuro, panel bento, tarjetas
muy redondeadas, bloque oscuro de tecnología, footer amplio). Paleta verte
`#136C4F` de KageSan + ámbar `#F59F0A` solo para destacar. Toda la capa visual
vive en `static/css/site.css`.

## Stack

- Django 5.2 + Passenger (`passenger_wsgi.py`, entry `application`).
- WhiteNoise para estáticos.
- SQLite en local; MySQL en producción vía PyMySQL (shim en `config/__init__.py`).
- Configuración por variables de entorno + lector `.env` propio (`config/env.py`).

## Arranque local

```bash
py -m venv .venv
.venv\Scripts\pip install -r requirements-dev.txt
copy .env.example .env
.venv\Scripts\python manage.py migrate
.venv\Scripts\python manage.py seed_content --publish   # autor, categorías, 6 posts, testimonios
.venv\Scripts\python manage.py generate_seo             # robots.txt, sitemap.xml, llms.txt
.venv\Scripts\python manage.py runserver
```

- Admin: <http://127.0.0.1:8000/admin/>. Para crear un superusuario en local:
  `python manage.py createsuperuser` (en producción lo crea `create_admin`
  desde variables de entorno).
- `seed_content` sin `--publish` deja las entradas en borrador.

## Tests

```bash
.venv\Scripts\python manage.py test
```

## Estructura

```
config/       proyecto Django (settings, env, urls, wsgi, middleware, SEO views, sitemaps)
core/         modelos (blog + contacto + testimonios), SEO (robots/sitemap/llms),
              JSON-LD (schema.py), content.py (texto de páginas pilar/segmento/precios/
              glosario/home) y seed_blog.py (los 6 artículos)
apps/pages/   home, pilar, segmento, precios, glosario, demo, sobre, contacto, legales
apps/blog/    blog + autor + templatetags
templates/    base.html, includes/, pages/, blog/, 404/403/500
static/       css/site.css, img/
deploy/       htaccess-extra.txt, .env.example (producción)
_content_src/ borradores en Markdown del equipo de contenido (fuente editorial)
```

## Rutas principales

`/` · `/software-crm-inmobiliario` · `/matching-inteligente-ia` ·
`/gestion-multi-oficina` · `/integraciones` ·
`/crm-para-agentes-inmobiliarios-independientes` · `/crm-para-agencias-inmobiliarias` ·
`/crm-para-franquicias-inmobiliarias` · `/precios` · `/glosario-crm-inmobiliario` ·
`/demo` · `/sobre-kagesan` · `/contacto/` · `/blog/` · `/aviso-legal/` ·
`/politica-de-privacidad/` · `/politica-de-cookies/` · `/robots.txt` ·
`/sitemap.xml` · `/llms.txt` · `/admin/`

## Despliegue

Producción en cPanel/Banahosting: ver **`DEPLOY_CPANEL.md`** (checklist sin
terminal, con apéndice para reemplazar WordPress en `public_html`).

## Pendiente antes de publicar

- Datos de marca reales: `KAGESAN_APP_URL` (login/registro de la app),
  teléfono, redes, razón social / NIF / domicilio (páginas legales).
- `/integraciones`: lista real de portales y del proveedor de WhatsApp/email.
- Casos de éxito y testimonios reales (ahora hay textos "(ejemplo)").
- Confirmar si los importes de `/precios` incluyen IVA.
- Revisión legal de `aviso-legal`, `privacidad` y `cookies`.
