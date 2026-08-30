# Despliegue en cPanel — kagesancrm.com (Banahosting)

Checklist **sin terminal**. Sustituye `<USUARIO>` por tu usuario de cPanel y
`<X.Y>` por la versión de Python disponible en "Setup Python App" (3.11, 3.12…).

> **Si kagesancrm.com ya tiene WordPress**, ve primero al apéndice
> "Reemplazar WordPress en el dominio principal" al final de este documento.

## 0. Subir el código a un repositorio remoto (una sola vez)

cPanel clona el proyecto desde un repositorio Git (GitHub, GitLab, Bitbucket).
Desde tu equipo, en la carpeta del proyecto:

```bash
git init
git add .
git commit -m "Web de KageSan CRM"
git branch -M main
git remote add origin git@github.com:abel93vv-design/kagesancrm-web.git
git push -u origin main
```

Para que cPanel pueda clonar un repo **privado**:
- cPanel → **SSH Access** → **Manage SSH Keys** → **Generate a New Key**
  (sin passphrase). Copia la **clave pública**.
- En GitHub: repo → **Settings → Deploy keys → Add deploy key** → pega la clave
  pública (solo lectura).
- Usa la **Clone URL SSH** (`git@github.com:...`) en el paso 3.

(Repo público: usa la Clone URL HTTPS y sáltate la deploy key.)

## 1. Base de datos (MySQL)

1. cPanel → **MySQL Databases**.
2. Crear base de datos: `<USUARIO>_kagesan`.
3. Crear usuario `<USUARIO>_kagesan` con una contraseña fuerte.
4. Añadir el usuario a la base con **ALL PRIVILEGES**.

## 2. Aplicación Python

1. cPanel → **Setup Python App** → **Create Application**.
2. Python version: la más alta disponible (3.11 / 3.12).
3. Application root: `kagesancrm.com` (o la carpeta donde vivirá el código).
4. Application URL: `kagesancrm.com`.
5. Application startup file: `passenger_wsgi.py`.
6. Application Entry point: `application`.
7. Crear. cPanel genera el virtualenv en
   `/home/<USUARIO>/virtualenv/kagesancrm.com/<X.Y>/`.

## 3. Git Version Control

1. cPanel → **Git Version Control** → **Create**.
2. **Clone a Repository**: activado. **Clone URL**: la del paso 0.
3. **Repository Path**: **la MISMA carpeta que el Application root del paso 2**
   → `/home/<USUARIO>/kagesancrm.com`. (Así el deploy se ejecuta ya dentro del
   docroot; el `.cpanel.yml` no tiene que copiar nada.)
4. **Create**. cPanel clona el repo dentro de esa carpeta.
5. Pestaña **Pull or Deploy** → **Update from Remote** → **Deploy HEAD Commit**.

> El `.cpanel.yml` de la raíz detecta solo el virtualenv de la app
> (`$HOME/virtualenv/<basename del Application root>/*/bin`) y hace, dentro de él:
> `pip install -r requirements.txt`, `migrate`, `create_admin`,
> `seed_content --publish`, `collectstatic`, `generate_seo`, `check --deploy`
> y `touch tmp/restart.txt`. No hay rutas de usuario cableadas.

## 4. Variables de entorno

En **Setup Python App** → tu app → **Environment variables**, añade las de
`deploy/.env.example`. Mínimo imprescindible:

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
| `DJANGO_DB_NAME` | `<USUARIO>_kagesan` |
| `DJANGO_DB_USER` | `<USUARIO>_kagesan` |
| `DJANGO_DB_PASSWORD` | (la del paso 1) |
| `DJANGO_DB_HOST` | `localhost` |
| `DJANGO_DB_PORT` | `3306` |
| `DJANGO_EMAIL_HOST` | `mail.kagesancrm.com` |
| `DJANGO_EMAIL_PORT` | `587` |
| `DJANGO_EMAIL_HOST_USER` | `hola@kagesancrm.com` |
| `DJANGO_EMAIL_HOST_PASSWORD` | (la del buzón) |
| `DJANGO_EMAIL_USE_TLS` | `true` |
| `DJANGO_DEFAULT_FROM_EMAIL` | `KageSan CRM <hola@kagesancrm.com>` |
| `DJANGO_CONTACT_RECIPIENTS` | `hola@kagesancrm.com` |
| `KAGESAN_APP_URL` | URL de la app CRM (login/registro) |
| `KAGESAN_CONTACT_EMAIL` | email de contacto real |
| `KAGESAN_LEGAL_ENTITY` / `_TAXID` / `_ADDRESS` | datos para las páginas legales |
| `DJANGO_ADMIN_USER` | `abel` (o el que quieras) |
| `DJANGO_ADMIN_PASSWORD` | una contraseña fuerte |
| `DJANGO_ADMIN_EMAIL` | `hola@kagesancrm.com` |

Con `DJANGO_ADMIN_USER` + `DJANGO_ADMIN_PASSWORD` definidos, el primer deploy
crea el superusuario (no hace falta terminal). Si luego cambias la contraseña
desde el admin, los siguientes deploys **no** la pisan.

Guarda y pulsa **Restart** en la app.

## 5. .htaccess (canónico + seguridad)

1. cPanel → **File Manager** → carpeta pública de `kagesancrm.com` → `.htaccess`.
2. Pega **encima** del bloque que empieza por `# BEGIN cPanel-generated ...
   Passenger` el contenido de `deploy/htaccess-extra.txt`.
3. Guarda. Verifica:
   - `http://kagesancrm.com/` → redirige a `https://kagesancrm.com/` (301).
   - `https://www.kagesancrm.com/` → redirige a `https://kagesancrm.com/` (301).
   - `http://kagesancrm.com/.well-known/acme-challenge/test` → **no** redirige.

## 6. AutoSSL

cPanel → **SSL/TLS Status** → marcar `kagesancrm.com` y `www.kagesancrm.com` →
**Run AutoSSL**. Con el certificado estable, deja la línea
`Strict-Transport-Security` del `.htaccess`.

## 7. Primer despliegue: comprobaciones

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

Cada cambio: **Git Version Control → Pull or Deploy → Update from Remote →
Deploy HEAD Commit**. El `.cpanel.yml` reinstala, migra, resiembra el contenido
(idempotente), recopila estáticos, regenera el SEO y reinicia Passenger.

---

## Apéndice — Reemplazar WordPress en el dominio principal

`kagesancrm.com` sirve hoy un WordPress cuyo docroot es
`/home/<USUARIO>/public_html`. Plan para sustituirlo por esta app sin perder la
posibilidad de volver atrás.

### A. Copia de seguridad (obligatorio, antes de nada)
1. cPanel → **Backup** → *Download a Full Account Backup* (o al menos
   *Home Directory* + la BD de WordPress).
2. En **File Manager**, comprime `public_html` en `wp_backup.zip` y descárgalo.
   En **phpMyAdmin**, exporta la BD de WordPress a `.sql`.

### B. (Recomendado) Validar en un subdominio primero
Monta la app en `staging.kagesancrm.com` (mismos pasos 2-6, con
`DJANGO_STAGING=true` y su propia BD) y compruébala entera. Solo cuando funcione,
haz el cambio en producción.

### C. Cambio en producción
1. **Vaciar `public_html`**: en File Manager, mueve *todo* su contenido
   (incluidos `wp-config.php`, `.htaccess`, `wp-*`) a
   `/home/<USUARIO>/_wp_old/`. **No lo borres**: es tu rollback.
2. **MySQL Databases**: crea BD y usuario **nuevos** para Django
   (`<USUARIO>_kagesan`, ALL PRIVILEGES). No reutilices la de WordPress.
3. **Setup Python App → Create Application**: Python `<X.Y>` ·
   **Application root: `public_html`** · Application URL: `kagesancrm.com` ·
   Startup file: `passenger_wsgi.py` · Entry point: `application`.
4. **Git Version Control → Create**: Clone URL del paso 0 ·
   **Repository Path: `/home/<USUARIO>/public_html`** (= Application root).
5. **Environment variables** (paso 4), con los datos de la BD nueva.
6. **Deploy HEAD Commit**. Revisa el log: debe acabar sin error.
7. **`.htaccess`** de `public_html`: pega `deploy/htaccess-extra.txt` **encima**
   del bloque de Passenger que genera cPanel.
8. **SSL/TLS Status** → *Run AutoSSL*.
9. Comprueba todo (sección 7). Si algo va mal: vuelve a mover el contenido de
   `_wp_old/` a `public_html` y borra el bloque de Passenger del `.htaccess`.
10. Tras unos días estable: borra `/home/<USUARIO>/_wp_old/` y la BD de WordPress.

### Notas
- Estáticos: `collectstatic` escribe en `public_html/staticfiles/` y WhiteNoise
  los sirve; `robots.txt` / `sitemap.xml` / `llms.txt` quedan en `public_html/`
  y los sirve Apache directamente.
- Si WordPress tenía URLs que aquí no existen, añade redirecciones 301 en el
  `.htaccess` para no perder SEO.
