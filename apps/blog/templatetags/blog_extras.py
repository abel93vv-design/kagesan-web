"""Procesado del cuerpo de los artículos.

``article_data`` recibe un BlogPost y devuelve:
  - ``html``: el cuerpo con ids automáticos en H2/H3 y el token [[IMAGEN]]
    sustituido por la imagen intercalada.
  - ``toc``: lista de secciones para el índice: [{level, id, text}].

El cuerpo lo escribe el equipo en el admin: se trata como HTML de confianza.
"""
import re

from django import template
from django.utils.safestring import mark_safe
from django.utils.text import slugify

register = template.Library()

_HEADING_RE = re.compile(r"<h([23])([^>]*)>(.*?)</h\1>", re.IGNORECASE | re.DOTALL)
_ID_ATTR_RE = re.compile(r'\bid\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
_TAG_RE = re.compile(r"<[^>]+>")
_TOKEN_RE = re.compile(r"(?:<p>\s*)?\[\[IMAGEN\]\](?:\s*</p>)?", re.IGNORECASE)


def _figure_html(post):
    img = getattr(post, "inline_image", None)
    if not img:
        return ""
    alt = (post.inline_image_alt or post.title).replace('"', "&quot;")
    caption = (
        f'<figcaption>{post.inline_image_alt}</figcaption>' if post.inline_image_alt else ""
    )
    return (
        '<figure class="article-figure">'
        f'<img src="{img.url}" alt="{alt}" loading="lazy" width="1200" height="800">'
        f"{caption}</figure>"
    )


@register.simple_tag
def article_data(post):
    body = post.body or ""
    toc = []
    used = set()

    def repl(match):
        level = int(match.group(1))
        attrs = match.group(2) or ""
        inner = match.group(3)
        text = _TAG_RE.sub("", inner).strip()

        found = _ID_ATTR_RE.search(attrs)
        if found:
            anchor = found.group(1)
        else:
            base = slugify(text) or f"seccion-{len(toc) + 1}"
            anchor = base
            i = 2
            while anchor in used:
                anchor = f"{base}-{i}"
                i += 1
            attrs = f'{attrs} id="{anchor}"'
        used.add(anchor)
        toc.append({"level": level, "id": anchor, "text": text})
        return f"<h{level}{attrs}>{inner}</h{level}>"

    html = _HEADING_RE.sub(repl, body)
    html = _TOKEN_RE.sub(_figure_html(post), html)
    return {"html": mark_safe(html), "toc": toc}
