"""Lector de ``.env`` y helpers de entorno sin dependencias externas.

Uso::

    from config.env import load_env, env, env_bool, env_list
    load_env(BASE_DIR / ".env")
    DEBUG = env_bool("DJANGO_DEBUG", False)
"""
from __future__ import annotations

import os
from pathlib import Path


def load_env(path: str | os.PathLike) -> None:
    """Carga pares CLAVE=VALOR de un archivo .env en ``os.environ``.

    - No sobrescribe variables ya presentes en el entorno real.
    - Ignora líneas vacías y comentarios (``#``).
    - Admite comillas simples o dobles alrededor del valor.
    - Admite el prefijo ``export ``.
    """
    p = Path(path)
    if not p.exists():
        return
    for raw in p.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[len("export "):]
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]
        if key and key not in os.environ:
            os.environ[key] = value


def env(key: str, default: str | None = None) -> str | None:
    return os.environ.get(key, default)


def env_bool(key: str, default: bool = False) -> bool:
    value = os.environ.get(key)
    if value is None:
        return default
    return value.strip().lower() in ("1", "true", "yes", "on")


def env_int(key: str, default: int) -> int:
    value = os.environ.get(key)
    if value is None or not value.strip():
        return default
    try:
        return int(value.strip())
    except ValueError:
        return default


def env_list(key: str, default: list[str] | None = None, sep: str = ",") -> list[str]:
    value = os.environ.get(key)
    if not value:
        return list(default or [])
    return [item.strip() for item in value.split(sep) if item.strip()]
