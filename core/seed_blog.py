# -*- coding: utf-8 -*-
"""Contenido inicial del blog de KageSan CRM.

Lo consume ``manage.py seed_content``. Con ``--publish`` las 6 entradas entran
publicadas (es lo que hace el despliegue en cPanel); sin la bandera entran en
borrador. Español de España, tono experto y directo.

Fuente: los borradores de ``_content_src/blog/``. Los ``body`` son HTML de
confianza (los edita el equipo desde el admin).
"""

CATEGORIES = [
    {
        "name": "Gestión de leads y cartera",
        "slug": "gestion-de-leads",
        "tagline": "Capturar, calificar y seguir sin que se enfríe nada.",
        "intro": (
            "Cómo dejar de perder oportunidades por falta de seguimiento: captura "
            "centralizada, asignación por reglas, lead scoring y recordatorios."
        ),
        "core_url": "/software-crm-inmobiliario",
        "position": 1,
    },
    {
        "name": "Matching e IA",
        "slug": "matching-e-ia",
        "tagline": "Emparejar clientes y propiedades con criterio, no con memoria.",
        "intro": (
            "Qué es el matching inmobiliario, cómo usa el score financiero y las "
            "preferencias, y qué gana una agencia al automatizar ese cruce."
        ),
        "core_url": "/matching-inteligente-ia",
        "position": 2,
    },
    {
        "name": "Digitalización de agencias",
        "slug": "digitalizacion-de-agencias",
        "tagline": "De Excel y WhatsApp a un sistema real, sin parar la operación.",
        "intro": (
            "Pasos, orden y errores a evitar para que el equipo trabaje de verdad "
            "desde el CRM y no en paralelo con las hojas de cálculo de siempre."
        ),
        "core_url": "/software-crm-inmobiliario",
        "position": 3,
    },
    {
        "name": "Elegir un CRM",
        "slug": "elegir-un-crm",
        "tagline": "Preguntas que evitan migrar dos veces.",
        "intro": (
            "Criterios para comparar CRMs inmobiliarios antes de contratar: "
            "matching, multi-oficina, integraciones, precio y soporte."
        ),
        "core_url": "/precios",
        "position": 4,
    },
]

TESTIMONIALS = [
    {
        "autor": "Dirección",
        "empresa": "Agencia independiente (testimonio de ejemplo)",
        "texto": (
            "Dejamos el Excel en una semana. Ahora todo el equipo trabaja sobre la "
            "misma cartera y el matching nos saca coincidencias que antes se nos escapaban."
        ),
        "position": 1,
    },
    {
        "autor": "Responsable de expansión",
        "empresa": "Red de oficinas (testimonio de ejemplo)",
        "texto": (
            "Damos de alta una oficina nueva en un par de días sobre el mismo "
            "sistema. La central por fin ve datos comparables de todas las sedes."
        ),
        "position": 2,
    },
    {
        "autor": "Agente autónomo",
        "empresa": "Agente independiente (testimonio de ejemplo)",
        "texto": (
            "Empecé con el plan Free para digitalizar mi cartera. El seguimiento "
            "automático hizo que dejara de perder leads por olvido."
        ),
        "position": 3,
    },
]


POSTS = [
    # 1 -----------------------------------------------------------------
    {
        "title": "Cómo automatizar la gestión de leads inmobiliarios",
        "slug": "como-automatizar-gestion-leads-inmobiliarios",
        "category": "gestion-de-leads",
        "focus_keyword": "automatizar gestión de leads inmobiliarios",
        "secondary_keywords": "lead scoring, asignación de leads, seguimiento automático, captura de leads",
        "tags": "leads, automatización, pipeline",
        "meta_description": (
            "Guía práctica para dejar de perder leads por falta de seguimiento: captura, "
            "asignación, calificación y seguimiento automático en una agencia inmobiliaria."
        ),
        "primary_core_url": "/software-crm-inmobiliario",
        "excerpt": (
            "La mayoría de leads inmobiliarios no se pierden por falta de interés, sino por "
            "falta de seguimiento a tiempo. Automatizar la captura, la asignación, la "
            "calificación y el seguimiento libera al agente del trabajo mecánico para que se "
            "concentre en la conversación y el cierre. Te contamos qué se puede automatizar y "
            "qué errores evitar al hacerlo."
        ),
        "body": """
<p>La mayoría de leads inmobiliarios no se pierden por falta de interés del cliente, sino por falta de seguimiento a tiempo. Los primeros minutos tras el primer contacto son los que más influyen en la conversión, y son precisamente los que más se descuidan cuando la gestión depende de que un agente «se acuerde» de responder.</p>
<p>Automatizar la gestión de leads no elimina al agente del proceso: le quita el trabajo mecánico para que se concentre en la parte que sí requiere criterio humano, la conversación con el cliente.</p>

<h2>Las 4 fases que se pueden automatizar</h2>

<h3>1. Captura centralizada</h3>
<p>Cuando los leads llegan por distintos canales —portales, web propia, WhatsApp, referidos— y cada uno se gestiona por separado, es fácil que alguno se pierda. El primer paso es que todos los canales alimenten un único sistema, sin captura manual.</p>

<h3>2. Asignación automática</h3>
<p>En lugar de que el primer agente disponible «se quede» con el lead sin criterio, el sistema lo reparte según reglas: zona, especialización, carga de trabajo actual. Así se evita tanto la sobrecarga de unos como el abandono de leads que «nadie reclama».</p>

<h3>3. Calificación (lead scoring)</h3>
<p>No todos los leads tienen la misma probabilidad de convertirse en cliente. Automatizar la calificación —cruzando capacidad financiera, comportamiento e interacción— permite priorizar el tiempo del equipo comercial en los leads con más probabilidad real de cierre.</p>

<h3>4. Seguimiento programado</h3>
<p>Recordatorios automáticos para contactar, reintentar o hacer seguimiento en los momentos clave, para que ningún lead se enfríe por simple olvido.</p>

<h2>Qué necesitas para implementarlo</h2>
<p>No hace falta un desarrollo a medida. Un <a href="/software-crm-inmobiliario">CRM inmobiliario</a> con asignación por reglas y recordatorios programados cubre estas cuatro fases sin que el equipo necesite conocimientos técnicos.</p>

<h2>Errores comunes al automatizar</h2>
<ul>
  <li>Automatizar la asignación sin definir criterios claros primero: el sistema ejecuta reglas, no las inventa.</li>
  <li>Confundir automatización con impersonalidad: los mensajes automáticos deben seguir sonando humanos.</li>
  <li>No revisar periódicamente las reglas de calificación a medida que cambia el mercado.</li>
</ul>

<h2>Conclusión</h2>
<p>La automatización de leads no reemplaza el criterio comercial del agente: libera su tiempo para usarlo donde aporta valor —la conversación, la negociación y el cierre—. El <a href="/matching-inteligente-ia">matching por IA</a> es el paso siguiente: decidir a quién ofrecer cada propiedad.</p>
""",
        "faqs": [],
    },

    # 2 -----------------------------------------------------------------
    {
        "title": "7 errores comunes al gestionar una cartera de clientes inmobiliarios",
        "slug": "errores-comunes-gestion-cartera-clientes-inmobiliarios",
        "category": "gestion-de-leads",
        "focus_keyword": "errores gestión cartera de clientes inmobiliarios",
        "secondary_keywords": "duplicados de contactos, historial de cliente, seguimiento, clientes fríos",
        "tags": "cartera de clientes, CRM, procesos",
        "meta_description": (
            "Duplicar contactos, perder el historial, no dar seguimiento a tiempo... "
            "Repasamos los errores más frecuentes al gestionar clientes inmobiliarios y cómo evitarlos."
        ),
        "primary_core_url": "/software-crm-inmobiliario",
        "excerpt": (
            "La mayoría de agencias no pierden clientes por falta de propiedades que ofrecer, "
            "sino por errores de gestión que se repiten sin que nadie los identifique como "
            "tal: información repartida, descartes sin registrar, contactos duplicados, "
            "seguimiento que depende de la memoria del agente. Repasamos siete y cómo evitarlos."
        ),
        "body": """
<p>La mayoría de agencias no pierden clientes por falta de propiedades que ofrecer, sino por errores de gestión que se repiten sin que nadie los identifique como tal. Estos son los más frecuentes.</p>

<h2>1. Repartir la información entre varias herramientas</h2>
<p>WhatsApp para hablar, Excel para la cartera, correo para las propuestas formales. Cuando la información de un mismo cliente vive en tres sitios, nadie tiene la foto completa —y menos si el agente que lo atendió está de vacaciones—.</p>
<p><strong>Cómo evitarlo:</strong> centralizar cada cliente en una única ficha, con el historial de interacción incluido.</p>

<h2>2. No registrar el motivo de un descarte</h2>
<p>Un cliente que rechaza una propiedad da información valiosa sobre lo que realmente busca. Si el descarte no queda registrado, se pierde para la próxima propuesta.</p>
<p><strong>Cómo evitarlo:</strong> registrar sistemáticamente el motivo de cada descarte, no solo que ocurrió.</p>

<h2>3. Duplicar contactos</h2>
<p>Un mismo cliente dado de alta dos veces porque contactó por dos canales genera seguimientos contradictorios y una mala experiencia («ya le dije eso a otro agente de la misma agencia»).</p>
<p><strong>Cómo evitarlo:</strong> un sistema con detección de duplicados y captura centralizada por canal.</p>

<h2>4. Seguimiento basado en la memoria del agente</h2>
<p>«Ya le llamaré la semana que viene» es una intención, no un proceso. Sin recordatorios programados, el seguimiento depende de que el agente se acuerde entre otras diez tareas.</p>
<p><strong>Cómo evitarlo:</strong> automatizar los recordatorios según la etapa del cliente en el pipeline.</p>

<h2>5. No diferenciar cualificación real de interés declarado</h2>
<p>Tratar igual a quien «está mirando» que a quien tiene capacidad y urgencia real hace que el equipo pierda tiempo en quien no va a cerrar pronto.</p>
<p><strong>Cómo evitarlo:</strong> aplicar un criterio de calificación (score) que priorice el esfuerzo comercial.</p>

<h2>6. Perder el historial cuando un agente deja la agencia</h2>
<p>Si la relación con el cliente vivía solo en la cabeza o el móvil del agente, se va con él.</p>
<p><strong>Cómo evitarlo:</strong> que toda interacción quede registrada en un sistema propiedad de la agencia, no del agente.</p>

<h2>7. No revisar la cartera de clientes «fríos»</h2>
<p>Clientes que no se convirtieron hace meses pueden volver a estar activos, pero si nadie revisa esa cartera, la oportunidad se pierde por omisión.</p>
<p><strong>Cómo evitarlo:</strong> reportes periódicos que resurjan clientes inactivos según criterios definidos (tiempo, cambios en la cartera disponible, etc.).</p>

<h2>Conclusión</h2>
<p>Ninguno de estos errores es por falta de esfuerzo del equipo: son consecuencia de gestionar con herramientas que no están pensadas para el volumen y la complejidad de una cartera inmobiliaria. Un <a href="/software-crm-inmobiliario">CRM del sector</a> los previene de serie; el paso previo suele ser <a href="/blog/crm-vs-excel-inmobiliaria">dejar el Excel</a>.</p>
""",
        "faqs": [],
    },

    # 3 -----------------------------------------------------------------
    {
        "title": "Qué es el matching inmobiliario y por qué está cambiando el sector",
        "slug": "que-es-matching-inmobiliario",
        "category": "matching-e-ia",
        "focus_keyword": "qué es el matching inmobiliario",
        "secondary_keywords": "matching automático, score financiero, preferencias implícitas, IA inmobiliaria",
        "tags": "matching, inteligencia artificial, cualificación",
        "meta_description": (
            "El matching inmobiliario empareja clientes con propiedades automáticamente usando "
            "IA. Te explicamos cómo funciona y qué gana tu agencia al usarlo."
        ),
        "primary_core_url": "/matching-inteligente-ia",
        "excerpt": (
            "Durante años, emparejar un cliente con la propiedad adecuada dependió de la "
            "memoria y la experiencia del agente. El matching inmobiliario automatiza ese "
            "cruce con score financiero y preferencias explícitas e implícitas, y es una de "
            "las aplicaciones de IA con impacto más directo en el día a día de una agencia."
        ),
        "body": """
<p>Durante años, emparejar un cliente con la propiedad adecuada dependió casi por completo de la memoria y la experiencia del agente: «creo que tengo algo que le puede interesar a fulano». Funciona, pero no escala, y depende de que el agente correcto se acuerde en el momento correcto.</p>
<p>El matching inmobiliario automatiza ese cruce, y es una de las aplicaciones de inteligencia artificial con impacto más directo y medible en el día a día de una agencia.</p>

<h2>Cómo funciona el matching automático</h2>
<p>El sistema analiza dos conjuntos de datos:</p>
<ol>
  <li><strong>El perfil del cliente:</strong> capacidad financiera (score), preferencias declaradas (zona, tipo, presupuesto) y preferencias implícitas (qué ha visto, qué ha descartado, cuánto tiempo ha dedicado a cada ficha).</li>
  <li><strong>La cartera disponible:</strong> características, precio, ubicación y estado de cada propiedad.</li>
</ol>
<p>Cruzando ambos conjuntos, identifica las combinaciones con mayor probabilidad de interés real y las prioriza para el agente, en lugar de dejar que las encuentre a mano.</p>

<h2>Score financiero: lo que separa el matching serio del básico</h2>
<p>No basta con cruzar «presupuesto declarado» con «precio de la propiedad». Un matching robusto evalúa la capacidad financiera real del cliente, evitando ofrecer propiedades fuera de su alcance o, al contrario, descartar oportunidades que sí podría permitirse.</p>

<h2>Preferencias implícitas frente a explícitas</h2>
<p>Un cliente puede decir que busca «algo tranquilo, en las afueras», pero su comportamiento —las fichas que abre y en las que se detiene— puede revelar que prioriza la cercanía al centro. El matching avanzado no se queda con lo que el cliente dice: también aprende de lo que hace.</p>

<h2>Qué gana una agencia con matching automático</h2>
<ul>
  <li><strong>Tiempo:</strong> minutos en lugar de horas revisando cartera.</li>
  <li><strong>Consistencia:</strong> el mismo criterio para toda la cartera, no solo lo que un agente recuerda.</li>
  <li><strong>Oportunidades que antes se perdían:</strong> coincidencias que nadie habría relacionado a mano, sobre todo en carteras grandes o <a href="/gestion-multi-oficina">multi-oficina</a>.</li>
</ul>

<h2>Conclusión</h2>
<p>El matching inmobiliario no sustituye el criterio comercial del agente: le da un punto de partida mucho mejor que «a ver qué se me ocurre». Puedes ver cómo funciona en la página de <a href="/matching-inteligente-ia">matching inteligente con IA</a>.</p>
""",
        "faqs": [],
    },

    # 4 -----------------------------------------------------------------
    {
        "title": "Cómo digitalizar una agencia inmobiliaria paso a paso",
        "slug": "como-digitalizar-una-agencia-inmobiliaria",
        "category": "digitalizacion-de-agencias",
        "focus_keyword": "cómo digitalizar una agencia inmobiliaria",
        "secondary_keywords": "digitalización inmobiliaria, migración de datos, proceso comercial, adopción de CRM",
        "tags": "digitalización, procesos, implantación",
        "meta_description": (
            "Guía práctica para pasar de Excel y WhatsApp a un sistema digital real, sin parar "
            "la operación de tu agencia. Pasos, orden y errores a evitar."
        ),
        "primary_core_url": "/software-crm-inmobiliario",
        "excerpt": (
            "Digitalizar una agencia no es «comprar un software»: es cambiar cómo trabaja el "
            "equipo cada día. Hecho con orden —auditoría, proceso único, sistema del sector, "
            "migración por fases y un responsable de datos— puede completarse en pocas "
            "semanas sin detener la operación."
        ),
        "body": """
<p>Digitalizar una agencia no es «comprar un software», es cambiar la forma en la que el equipo trabaja todos los días. Hecho sin plan, genera resistencia y datos a medio migrar. Hecho con orden, puede completarse en pocas semanas sin detener la operación.</p>

<h2>Paso 1: Audita cómo trabajas hoy realmente</h2>
<p>Antes de elegir herramienta, identifica dónde vive hoy la información: cuántos Excels distintos, quién los actualiza, qué se gestiona solo por WhatsApp. Esta auditoría define qué hay que migrar y qué proceso hay que rediseñar, no solo digitalizar tal cual.</p>

<h2>Paso 2: Define el proceso comercial único</h2>
<p>Decide cuáles son las etapas por las que pasa una oportunidad en tu agencia (contacto, visita, negociación, cierre). Si cada agente tiene su propio proceso mental, la digitalización solo lo hará visible, no lo resolverá.</p>

<h2>Paso 3: Elige un sistema pensado para el sector</h2>
<p>Un CRM genérico exige adaptar tu proceso a su lógica. Un <a href="/software-crm-inmobiliario">CRM inmobiliario</a> ya entiende conceptos como cartera de propiedades, matching o pipeline de cierre, y eso acorta la implementación.</p>

<h2>Paso 4: Migra datos por fases, no todo de golpe</h2>
<p>Empieza por la cartera activa (clientes y propiedades en proceso), no por el histórico completo. Así el equipo empieza a operar rápido en el nuevo sistema mientras el resto se migra en paralelo.</p>

<h2>Paso 5: Forma al equipo con casos reales</h2>
<p>La adopción mejora cuando el equipo ve el sistema resolviendo un caso suyo (su propio cliente, su propia propiedad) en lugar de un ejemplo genérico de formación.</p>

<h2>Paso 6: Define quién mantiene los datos limpios</h2>
<p>Sin un responsable claro de calidad de datos, el sistema se degrada con el tiempo igual que se degradaba el Excel anterior.</p>

<h2>Errores que retrasan una digitalización</h2>
<ul>
  <li>Intentar digitalizar todo el histórico antes de empezar a operar.</li>
  <li>No involucrar al equipo en la elección de la herramienta.</li>
  <li>Elegir un sistema genérico «porque ya lo usábamos en otra empresa».</li>
  <li>No fijar una fecha de corte clara para dejar de usar el sistema antiguo en paralelo.</li>
</ul>

<h2>Conclusión</h2>
<p>La digitalización no se mide por si tienes un software instalado, sino por si el equipo trabaja realmente desde ahí. El orden del proceso importa tanto como la herramienta. Si aún dudas del cambio, compara <a href="/blog/crm-vs-excel-inmobiliaria">CRM frente a Excel</a> y repasa <a href="/blog/como-elegir-crm-inmobiliario">cómo elegir un CRM</a>.</p>
""",
        "faqs": [],
    },

    # 5 -----------------------------------------------------------------
    {
        "title": "CRM vs Excel: por qué tu agencia inmobiliaria necesita dar el salto",
        "slug": "crm-vs-excel-inmobiliaria",
        "category": "digitalizacion-de-agencias",
        "focus_keyword": "CRM vs Excel inmobiliaria",
        "secondary_keywords": "Excel inmobiliario, gestión de cartera, colaboración en equipo, escalabilidad CRM",
        "tags": "CRM, Excel, comparativa",
        "meta_description": (
            "Excel sirve hasta que deja de servir. Comparamos ambas opciones en gestión de "
            "leads, cartera, colaboración en equipo y escalabilidad."
        ),
        "primary_core_url": "/precios",
        "excerpt": (
            "Excel no es una mala herramienta: es una herramienta que no se diseñó para "
            "gestionar una cartera viva con varios agentes a la vez y clientes que necesitan "
            "seguimiento en tiempo real. Funciona al principio; el problema aparece cuando la "
            "agencia crece. Comparativa directa y cómo hacer la transición sin fricción."
        ),
        "body": """
<p>Excel no es una mala herramienta, es una herramienta que no fue diseñada para lo que muchas agencias le piden: gestionar una cartera viva, con varios agentes trabajando a la vez y clientes que necesitan seguimiento en tiempo real. Funciona al principio; el problema aparece cuando la agencia crece.</p>

<h2>Comparativa directa</h2>
<table>
  <thead>
    <tr><th>Aspecto</th><th>Excel</th><th>CRM inmobiliario</th></tr>
  </thead>
  <tbody>
    <tr><td>Colaboración en tiempo real</td><td>Conflictos de versiones, archivos duplicados</td><td>Todo el equipo sobre los mismos datos actualizados</td></tr>
    <tr><td>Seguimiento de leads</td><td>Manual, depende de que alguien revise la hoja</td><td>Recordatorios y automatizaciones</td></tr>
    <tr><td>Matching cliente-propiedad</td><td>Búsqueda manual, propensa a error humano</td><td>Automático, por score y preferencias</td></tr>
    <tr><td>Historial de interacción</td><td>Se pierde o se registra de forma inconsistente</td><td>Centralizado por ficha de cliente</td></tr>
    <tr><td>Visibilidad para dirección</td><td>Hay que pedir el archivo y consolidar a mano</td><td>Dashboards en tiempo real</td></tr>
    <tr><td>Escalabilidad</td><td>Se vuelve inmanejable con el volumen</td><td>Diseñado para crecer con la cartera</td></tr>
    <tr><td>Seguridad y permisos</td><td>Difícil controlar quién ve o edita qué</td><td>Permisos por rol, equipo u oficina</td></tr>
  </tbody>
</table>

<h2>Cuándo Excel todavía «aguanta»</h2>
<p>Si eres un agente con una cartera muy pequeña y trabajas completamente solo, Excel puede cubrir lo básico un tiempo. El problema aparece en tres momentos típicos:</p>
<ul>
  <li>Cuando incorporas a un segundo agente y necesitáis compartir información en tiempo real.</li>
  <li>Cuando el volumen de leads supera lo que puedes seguir manualmente.</li>
  <li>Cuando necesitas cruzar cartera de clientes con cartera de propiedades de forma sistemática.</li>
</ul>

<h2>Lo que realmente cuesta seguir con Excel</h2>
<p>El coste no es solo de tiempo. Cada lead que se enfría por falta de seguimiento y cada coincidencia cliente-propiedad que nadie detectó a tiempo es una venta potencial perdida —y ese coste suele ser mayor que el de una suscripción a un CRM—.</p>

<h2>Cómo hacer la transición sin fricción</h2>
<p>No hace falta migrar todo de golpe. Un CRM inmobiliario permite importar la cartera activa desde Excel y empezar a operar en días, no en meses.</p>

<h2>Conclusión</h2>
<p>La pregunta no es si Excel «funciona», sino cuánto tiempo va a seguir funcionando a medida que tu agencia crece. Cuanto antes se hace el cambio, menos datos hay que migrar. Revisa los <a href="/precios">planes de KageSan</a> (hay uno gratuito) y la guía de <a href="/blog/como-digitalizar-una-agencia-inmobiliaria">digitalización paso a paso</a>.</p>
""",
        "faqs": [],
    },

    # 6 -----------------------------------------------------------------
    {
        "title": "Cómo elegir un CRM inmobiliario: checklist antes de contratar",
        "slug": "como-elegir-crm-inmobiliario",
        "category": "elegir-un-crm",
        "focus_keyword": "cómo elegir un CRM inmobiliario",
        "secondary_keywords": "checklist CRM inmobiliario, comparar CRM, multi-oficina, integraciones, precio CRM",
        "tags": "CRM, checklist, decisión de compra",
        "meta_description": (
            "10 preguntas clave para evaluar un CRM inmobiliario antes de contratarlo: "
            "matching, multi-oficina, integraciones, precio y soporte."
        ),
        "primary_core_url": "/precios",
        "excerpt": (
            "Elegir mal un CRM sale caro dos veces: la suscripción y la migración a otro "
            "sistema meses después. Antes de decidir, conviene evaluar cada opción con las "
            "mismas diez preguntas: del matching automático a cómo escala el precio con tu "
            "crecimiento."
        ),
        "body": """
<p>Elegir mal un CRM sale caro dos veces: el coste de la suscripción y el coste de migrar de nuevo a otro sistema meses después. Antes de decidir, conviene evaluar cada opción con las mismas preguntas.</p>

<h2>1. ¿Está pensado para inmobiliarias o es genérico adaptado?</h2>
<p>Un CRM genérico obliga a «traducir» conceptos como cartera de propiedades o matching a campos personalizados. Uno inmobiliario ya los entiende de fábrica, y eso acelera la implantación.</p>

<h2>2. ¿Tiene matching automático o solo filtros manuales?</h2>
<p>Hay diferencia real entre filtrar a mano por precio y zona y un sistema que cruza automáticamente el perfil financiero y las preferencias del cliente con la cartera disponible.</p>

<h2>3. ¿Escala si pasas de una oficina a varias?</h2>
<p>Aunque hoy seas una sola oficina, confirma si el sistema soporta estructura <a href="/gestion-multi-oficina">multi-oficina</a> con permisos diferenciados, para no tener que migrar si creces.</p>

<h2>4. ¿Qué automatizaciones incluye realmente?</h2>
<p>Pide ejemplos concretos: asignación de leads, recordatorios de seguimiento, flujos configurables. «Automatización» significa algo distinto en cada proveedor.</p>

<h2>5. ¿Qué reportes y dashboards ofrece de serie?</h2>
<p>Comprueba si puedes ver rendimiento por agente y por oficina sin construir el informe a mano cada vez.</p>

<h2>6. ¿Con qué se integra?</h2>
<p>Portales, WhatsApp, email, tu web propia. Un CRM que no se conecta con tus canales se convierte en trabajo administrativo extra. Repasa la página de <a href="/integraciones">integraciones</a>.</p>

<h2>7. ¿Cómo es la curva de aprendizaje para el equipo?</h2>
<p>Un sistema potente que nadie usa no aporta valor. Pregunta por el tiempo medio de onboarding de un agente nuevo.</p>

<h2>8. ¿Cómo escala el precio con tu crecimiento?</h2>
<p>Revisa qué pasa con el coste al superar los límites del plan (propiedades, usuarios, oficinas), no solo el precio de entrada. En KageSan puedes verlo en la página de <a href="/precios">precios</a>.</p>

<h2>9. ¿Qué soporte incluye cada plan?</h2>
<p>Especialmente si tienes estructura multi-oficina: confirma si hay soporte dedicado y en qué plan.</p>

<h2>10. ¿Puedo probarlo antes de comprometerme?</h2>
<p>Un plan gratuito o una <a href="/demo">demo</a> con tu propia cartera dice más que cualquier folleto comercial.</p>

<h2>Checklist rápido</h2>
<ul>
  <li>Pensado específicamente para inmobiliarias.</li>
  <li>Matching automático (no solo filtros manuales).</li>
  <li>Soporta o soportará estructura multi-oficina.</li>
  <li>Automatizaciones concretas y configurables.</li>
  <li>Dashboards y reportes de serie.</li>
  <li>Integraciones con tus canales actuales.</li>
  <li>Onboarding rápido, sin perfil técnico.</li>
  <li>Precio que escala de forma predecible.</li>
  <li>Soporte adecuado a tu estructura.</li>
  <li>Posibilidad de probar antes de pagar.</li>
</ul>

<h2>Conclusión</h2>
<p>Evalúa cada CRM con estas preguntas y con tu propia cartera de ejemplo. KageSan tiene un plan gratuito para hacerlo sin coste.</p>
""",
        "faqs": [
            {"question": "¿Un CRM genérico sirve para una inmobiliaria?",
             "answer": "Puede servir, pero obliga a recrear conceptos del sector (cartera, matching, pipeline de cierre) con campos personalizados. Un CRM inmobiliario los trae de fábrica y acorta la implantación."},
            {"question": "¿Es imprescindible el matching automático?",
             "answer": "No es imprescindible, pero marca la diferencia: filtrar a mano por precio y zona no es lo mismo que cruzar automáticamente score financiero y preferencias con toda la cartera."},
            {"question": "¿Debo elegir ya un plan multi-oficina si tengo una sola sede?",
             "answer": "No necesariamente, pero conviene que el sistema soporte multi-oficina para no migrar si creces. En KageSan la estructura multi-oficina se activa desde el plan Pro."},
            {"question": "¿Cómo comparo el precio entre CRMs?",
             "answer": "Mira cómo escala el coste al superar los límites del plan (propiedades, usuarios, oficinas), no solo el precio de entrada, y si existe un plan gratuito para probar."},
        ],
    },
]
