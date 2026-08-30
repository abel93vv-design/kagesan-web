#!/usr/bin/env python
"""Utilidad de línea de comandos de Django para el proyecto KageSan CRM."""
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se ha podido importar Django. ¿Está instalado y activado el "
            "entorno virtual? Ejecuta 'py -m pip install -r requirements-dev.txt'."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
