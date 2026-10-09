#!/bin/bash
# =====================================================================
# Puesta en marcha de kagesancrm.com desde la Terminal de cPanel.
# Idempotente: se puede volver a ejecutar sin romper nada.
#
#   curl/clone ya hecho -> bash ~/kagesancrm.com/deploy/bootstrap_cpanel.sh
#
# Hace: app Python (CloudLinux) + BD MySQL + .env de producción +
# instalación + migraciones + contenido + estáticos + SEO + .htaccess +
# reinicio. Las contraseñas generadas se guardan en
# ~/kagesan-credenciales.txt (solo legible por el usuario).
# =====================================================================
set -euo pipefail

DOMAIN="kagesancrm.com"
APP_ROOT="$HOME/$DOMAIN"
PYVER="3.12"
CPUSER="$(whoami)"
DB="${CPUSER}_kagesan"
REPO_URL="git@github-kagesan:abel93vv-design/kagesan-web.git"
CREDS="$HOME/kagesan-credenciales.txt"

say() { printf '\n==> %s\n' "$*"; }
rand() { LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom 2>/dev/null | head -c "${1:-32}" || true; }

# --- 1. Código ------------------------------------------------------
say "1/7 Código en $APP_ROOT"
mkdir -p "$APP_ROOT"
if [ ! -d "$APP_ROOT/.git" ]; then
    TMP="$(mktemp -d)"
    git clone --no-checkout "$REPO_URL" "$TMP/repo"
    mv "$TMP/repo/.git" "$APP_ROOT/.git"
    rm -rf "$TMP"
fi
cd "$APP_ROOT"
git fetch origin
git checkout -f -B main origin/main
echo "Commit: $(git log -1 --oneline)"

# --- 2. App Python --------------------------------------------------
say "2/7 Aplicación Python $PYVER"
if ! cloudlinux-selector get --json --interpreter python 2>/dev/null | grep -q "\"$DOMAIN\""; then
    cloudlinux-selector create --json --interpreter python --version "$PYVER" \
        --app-root "$DOMAIN" --domain "$DOMAIN" --app-uri "/" \
        --startup-file passenger_wsgi.py --entry-point application
    # El selector puede dejar su passenger_wsgi.py de ejemplo: restaurar el nuestro.
    git checkout -f -- passenger_wsgi.py
else
    echo "La app ya existe."
fi
PYBIN=""
for d in "$HOME/virtualenv/$DOMAIN"/*/bin; do [ -x "$d/python" ] && PYBIN="$d"; done
[ -n "$PYBIN" ] || { echo "ERROR: no encuentro el virtualenv en $HOME/virtualenv/$DOMAIN"; exit 1; }
echo "Venv: $PYBIN"

# --- 3. Base de datos + .env ---------------------------------------
say "3/7 Base de datos y .env"
if [ ! -f "$APP_ROOT/.env" ]; then
    DBPASS="$(rand 32)"
    ADMINPASS="$(rand 20)"
    uapi Mysql create_database name="$DB" >/dev/null || true
    if ! uapi Mysql create_user name="$DB" password="$DBPASS" | grep -q "status: 1"; then
        uapi Mysql set_password user="$DB" password="$DBPASS" >/dev/null
    fi
    uapi Mysql set_privileges_on_database user="$DB" database="$DB" privileges="ALL%20PRIVILEGES" >/dev/null

    umask 077
    cat >"$APP_ROOT/.env" <<EOF
DJANGO_SECRET_KEY=$(rand 64)
DJANGO_DEBUG=false
DJANGO_ALLOWED_HOSTS=$DOMAIN,www.$DOMAIN
DJANGO_SITE_URL=https://$DOMAIN
DJANGO_HTTPS=true
DJANGO_SSL_HOST=$DOMAIN
DJANGO_CSRF_TRUSTED_ORIGINS=https://$DOMAIN,https://www.$DOMAIN
DJANGO_DB_ENGINE=mysql
DJANGO_DB_NAME=$DB
DJANGO_DB_USER=$DB
DJANGO_DB_PASSWORD=$DBPASS
DJANGO_DB_HOST=localhost
DJANGO_DB_PORT=3306
DJANGO_ADMIN_USER=abel
DJANGO_ADMIN_PASSWORD=$ADMINPASS
DJANGO_ADMIN_EMAIL=hola@$DOMAIN
EOF
    cat >"$CREDS" <<EOF
KageSan CRM - credenciales generadas $(date '+%F %T')
Admin:  https://$DOMAIN/admin/   usuario: abel   contraseña: $ADMINPASS
MySQL:  base/usuario: $DB   contraseña: $DBPASS
EOF
    chmod 600 "$CREDS"
    umask 022
    echo ".env creado. Credenciales en $CREDS"
else
    echo ".env ya existe; no se toca."
fi

# --- 4. Dependencias y Django --------------------------------------
say "4/7 Dependencias y Django"
"$PYBIN/pip" install -q --upgrade pip
"$PYBIN/pip" install -q -r requirements.txt
"$PYBIN/python" manage.py migrate --noinput
"$PYBIN/python" manage.py create_admin
"$PYBIN/python" manage.py seed_content --publish
"$PYBIN/python" manage.py collectstatic --noinput -v 0
"$PYBIN/python" manage.py generate_seo
"$PYBIN/python" manage.py check --deploy || true

# --- 5. .htaccess --------------------------------------------------
say "5/7 .htaccess"
touch .htaccess
if ! grep -q "Bloque para AÑADIR al .htaccess" .htaccess; then
    cp .htaccess ".htaccess.bak-$(date +%s)"
    { cat deploy/htaccess-extra.txt; echo; cat .htaccess; } > .htaccess.new
    mv .htaccess.new .htaccess
    echo "Bloque añadido (copia de seguridad guardada)."
else
    echo "Ya estaba añadido."
fi

# --- 6. Reinicio ---------------------------------------------------
say "6/7 Reinicio"
mkdir -p tmp && touch tmp/restart.txt
cloudlinux-selector restart --json --interpreter python --app-root "$DOMAIN" >/dev/null 2>&1 || true

# --- 7. Comprobación -----------------------------------------------
say "7/7 Comprobación"
sleep 3
for path in / /precios /blog/ /robots.txt /sitemap.xml; do
    code="$(curl -s -o /dev/null -w '%{http_code}' "https://$DOMAIN$path" || echo ERR)"
    echo "$code  https://$DOMAIN$path"
done
echo
echo "Listo. Contraseña del admin: cat $CREDS  (no la compartas)."
