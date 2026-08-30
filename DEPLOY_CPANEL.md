# Despliegue en cPanel — kagesancrm.com (Banahosting)

Checklist **sin terminal**. Datos de esta cuenta:

- Usuario de cPanel: **`nivngtjs`**
- Python disponible: **3.12** (3.12.14)
- `kagesancrm.com` es un **dominio nuevo** en una cuenta que ya aloja otros
  proyectos. Hay que darlo de alta antes de crear la app (paso 1).

## 0. Subir el código a GitHub (una sola vez)

Repo **privado** `abel93vv-design/kagesancrm-web`. Desde tu equipo, en la
carpeta del proyecto (el repo local ya está inicializado y con un commit):

```bash
git remote add origin git@github.com:abel93vv-design/kagesancrm-web.git
git push -u origin main
```

Para que cPanel pueda clonar un repo **privado**:
- cPanel → **SSH Access** → **Manage SSH Keys** → **Generate a New Key**
  (sin passphrase). Pulsa **View/Download** en la clave y copia la **clave pública**.
- En GitHub: repo → **Settings → Deploy keys → Add deploy key** → pega la clave
  pública. **Sin** marcar "Allow write access".
- Usa la **Clone URL SSH** (`git@github.com:abel93vv-design/kagesancrm-web.git`)
  en el paso 4.

## 1. Dar de alta el dominio

cPanel → **Domains** → **Create A New Domain**:
- Domain: `kagesancrm.com`
- Deja que cree el document root por defecto: `/home/nivngtjs/kagesancrm.com`
  (desmarca "Share document root" si aparece).

Si el dominio aún no apunta a Banahosting, configura sus DNS (nameservers de
Banahosting) antes de continuar con AutoSSL.

## 2. Base de datos (MySQL)

1. cPanel → **MySQL Databases**.
2. Crear base de datos: `nivngtjs_kagesan`.
3. Crear usuario `nivngtjs_kagesan` con una contraseña fuerte (guárdala).
4. Añadir el usuario a la base con **ALL PRIVILEGES**.

## 3. Aplicación Python

1. cPanel → **Setup Python App** → **Create Application**.
2. Python version: **3.12**.
3. Application root: `kagesancrm.com`  (= `/home/nivngtjs/kagesancrm.com`).
4. Application URL: `kagesancrm.com`.
5. Application startup file: `passenger_wsgi.py`.
6. Application Entry point: `application`.
7. Crear. cPanel genera el virtualenv en
   `/home/nivngtjs/virtualenv/kagesancrm.com/3.12/`.

## 4. Git Version Control

1. cPanel → **Git Version Control** → **Create**.
2. **Clone a Repository**: activado. **Clone URL**:
   `git@github.com:abel93vv-design/kagesancrm-web.git`.
3. **Repository Path**: **la MISMA carpeta que el Application root del paso 3**
   → `/home/nivngtjs/kagesancrm.com`.
4. **Create**. cPanel clona el repo dentro de esa carpeta.
5. Pestaña **Pull or Deploy** → **Update from Remote** → **Deploy HEAD Commit**.

> El `.cpanel.yml` detecta solo el virtualenv de la app
> (`/home/nivngtjs/virtualenv/kagesancrm.com/3.12/bin`) y ejecuta:
> `pip install -r requirements.txt`, `migrate`, `create_admin`,
> `seed_content --publish`, `collectstatic`, `generate_seo`,
> `check --deploy` y `touch tmp/restart.txt`.

## 5. Variables de entorno

En **Setup Python App** → tu app → **Environment variables**, añade (referencia
completa en `deploy/.env.example`):

| Variable | Valor |
| --- | --- |
| `DJANGO_SECRET_KEY` | 50+ caracteres aleatorios |
| `DJANGO_DEBUG` | `false` |
| `DJANGO_ALLOWED_HOSTS` | `kagesancrm.com,www.kagesancrm.com` |
| `DJANGO_SITE_URL` | `https://kagesancrm.com` |
| `DJANGO_HTTPS` | `true` |
| `DJANGO_SSL_HOST` | `kagesancrm.com` |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | `https://kagesancrm.com,https://www.kagesancrm.com` |
| `DJANGO_DB_ENGINE` | `mysql` |
| `DJANGO_DB_NAME` | `nivngtjs_kagesan` |
| `DJANGO_DB_USER` | `nivngtjs_kagesan` |
| `DJANGO_DB_PASSWORD` | (la del paso 2) |
| `DJANGO_DB_HOST` | `localhost` |
| `DJANGO_DB_PORT` | `3306` |
| `DJANGO_EMAIL_HOST` | `mail.kagesancrm.com` |
| `DJANGO_EMAIL_PORT` | `587` |
| `DJANGO_EMAIL_HOST_USER` | `hola@kagesancrm.com` |
| `DJANGO_EMAIL_HOST_PASSWORD` | (la del buzón, tras crearlo en **Email Accounts**) |
| `DJANGO_EMAIL_USE_TLS` | `true` |
| `DJANGO_DEFAULT_FROM_EMAIL` | `KageSan CRM <hola@kagesancrm.com>` |
| `DJANGO_CONTACT_RECIPIENTS` | `hola@kagesancrm.com` |
| `KAGESAN_APP_URL` | URL real de la app CRM (login/registro) |
| `KAGESAN_CONTACT_EMAIL` | email de contacto real |
| `KAGESAN_LEGAL_ENTITY` / `_TAXID` / `_ADDRESS` | datos para las páginas legales |
| `DJANGO_ADMIN_USER` | `abel` (o el que quieras) |
| `DJANGO_ADMIN_PASSWORD` | una contraseña fuerte |
| `DJANGO_ADMIN_EMAIL` | `hola@kagesancrm.com` |

Con `DJANGO_ADMIN_USER` + `DJANGO_ADMIN_PASSWORD` definidos, el primer deploy
crea el superusuario. Si luego cambias la contraseña desde el admin, los
siguientes deploys **no** la pisan.

Guarda y pulsa **Restart** en la app.

## 6. .htaccess (canónico + seguridad)

1. cPanel → **File Manager** → `/home/nivngtjs/kagesancrm.com` → `.htaccess`
   (activa "Show Hidden Files").
2. Pega **encima** del bloque que empieza por `# BEGIN cPanel-generated ...
   Passenger` el contenido de `deploy/htaccess-extra.txt`.
3. Guarda y verifica:
   - `http://kagesancrm.com/` → redirige a `https://kagesancrm.com/` (301).
   - `https://www.kagesancrm.com/` → redirige a `https://kagesancrm.com/` (301).
   - `http://kagesancrm.com/.well-known/acme-challenge/test` → **no** redirige.

## 7. AutoSSL

cPanel → **SSL/TLS Status** → marcar `kagesancrm.com` y `www.kagesancrm.com` →
**Run AutoSSL**. (Requiere que el dominio ya resuelva a Banahosting.) Con el
certificado estable, deja la línea `Strict-Transport-Security` del `.htaccess`.

## 8. Primer despliegue: comprobaciones

- `https://kagesancrm.com/` carga con estilos.
- `https://kagesancrm.com/precios` muestra los 4 planes (0 / 49 / 129 / a medida).
- `https://kagesancrm.com/robots.txt` → contiene `Sitemap: https://kagesancrm.com/sitemap.xml`.
- `https://kagesancrm.com/sitemap.xml` → URLs con dominio `kagesancrm.com` y las 6 de blog.
- `https://kagesancrm.com/llms.txt` → responde.
- `https://kagesancrm.com/blog/` → 6 artículos publicados.
- `https://kagesancrm.com/pagina-inexistente` → 404 con el diseño del sitio.
- Enviar el formulario de `/contacto/` y de `/demo` y confirmar que llega el email.
- Entrar en `https://kagesancrm.com/admin/` con `DJANGO_ADMIN_USER` / `_PASSWORD`.

## Redespliegues

Cada cambio: `git push` desde tu equipo → cPanel **Git Version Control → Pull or
Deploy → Update from Remote → Deploy HEAD Commit**. El `.cpanel.yml` reinstala,
migra, resiembra el contenido (idempotente), recopila estáticos, regenera el
SEO y reinicia Passenger.

---

## Apéndice — si en el futuro el dominio ya tuviera WordPress

No aplica ahora (`kagesancrm.com` es un dominio nuevo y vacío). Si algún día se
despliega sobre un WordPress existente: copia de seguridad completa, mover el
contenido de `public_html` a `_wp_old/`, crear BD nueva para Django, y seguir
los pasos 3-8 con `public_html` como Application root. El contenido de
`_wp_old/` es el rollback hasta que la app esté estable.
