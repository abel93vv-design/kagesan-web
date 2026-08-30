"""Punto de entrada para Phusion Passenger (cPanel / Banahosting).

Passenger busca una variable de módulo llamada ``application``.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from config.wsgi import application  # noqa: E402  (import tardío intencionado)

# Alias explícito por si algún entorno espera 'application' en este módulo.
application = application
