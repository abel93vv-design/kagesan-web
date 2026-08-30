# -*- coding: utf-8 -*-
"""Contenido editorial de las páginas fijas de KageSan CRM.

Fuente: los borradores en ``_content_src/`` (Markdown del equipo de contenido),
convertidos a estructuras de datos y **reconciliados con el producto real**
(`prop-pal-nexus/src/config/planLimits.ts`): el plan Free son 50 propiedades y
25 clientes, el matching por IA está en todos los planes, y multi-oficina
empieza en el plan Pro (hasta 5 oficinas), sin límite en Enterprise.

Las cifras de resultados / testimonios van marcadas como «(ejemplo)» hasta
disponer de casos reales.
"""

# ---------------------------------------------------------------------------
# Planes  (importe mensual en EUR; None = "a medida")
# ---------------------------------------------------------------------------
PLANS = [
    {
        "slug": "free",
        "name": "Free",
        "price_eur": 0,
        "period": "",
        "tagline": "Para digitalizar tu cartera actual sin coste.",
        "cta": "Empezar gratis",
        "cta_kind": "app",
        "highlighted": False,
        "highlights": [
            "50 propiedades y 25 clientes",
            "1 usuario",
            "Matching por IA incluido",
            "Pipeline visual e importación desde Excel",
            "Histórico de actividad de 7 días",
        ],
    },
    {
        "slug": "basic",
        "name": "Basic",
        "price_eur": 49,
        "period": "/mes",
        "tagline": "Para agentes y equipos pequeños que empiezan a crecer.",
        "cta": "Empezar con Basic",
        "cta_kind": "app",
        "highlighted": False,
        "highlights": [
            "500 propiedades y 100 clientes",
            "3 usuarios",
            "2 portales conectados",
            "10 campos personalizados y 1 API key",
            "Histórico de actividad de 30 días",
        ],
    },
    {
        "slug": "pro",
        "name": "Pro",
        "price_eur": 129,
        "period": "/mes",
        "tagline": "Para agencias con varios equipos y hasta 5 oficinas.",
        "cta": "Empezar con Pro",
        "cta_kind": "app",
        "highlighted": True,
        "highlights": [
            "Propiedades ilimitadas · 500 clientes",
            "10 usuarios · hasta 5 oficinas",
            "5 portales conectados",
            "25 campos personalizados y 2 API keys",
            "Histórico de actividad de 90 días",
        ],
    },
    {
        "slug": "enterprise",
        "name": "Enterprise",
        "price_eur": None,
        "period": "",
        "tagline": "Para redes y franquicias multi-oficina.",
        "cta": "Hablar con ventas",
        "cta_kind": "contact",
        "highlighted": False,
        "highlights": [
            "Todo ilimitado: clientes, usuarios y oficinas",
            "API y campos personalizados sin límite",
            "Histórico de actividad completo",
            "Soporte dedicado e implantación",
        ],
    },
]

# Tabla comparativa. Orden de columnas = Free, Basic, Pro, Enterprise.
PLAN_TABLE = [
    {"label": "Precio", "values": ["0 €", "49 €/mes", "129 €/mes", "A medida"]},
    {"label": "Propiedades", "values": ["50", "500", "Ilimitadas", "Ilimitadas"]},
    {"label": "Clientes", "values": ["25", "100", "500", "Ilimitados"]},
    {"label": "Usuarios del equipo", "values": ["1", "3", "10", "Ilimitados"]},
    {"label": "Oficinas", "values": ["1", "1", "5", "Sin límite"]},
    {"label": "Portales conectados", "values": ["—", "2", "5", "Sin límite"]},
    {"label": "Campos personalizados", "values": ["3", "10", "25", "Sin límite"]},
    {"label": "API keys", "values": ["—", "1", "2", "Sin límite"]},
    {"label": "Pipelines", "values": ["10", "50", "Ilimitados", "Ilimitados"]},
    {"label": "Almacenamiento", "values": ["100 MB", "1 GB", "10 GB", "Sin límite"]},
    {"label": "Matching por IA", "values": ["Sí", "Sí", "Sí", "Sí"]},
    {"label": "Histórico de actividad", "values": ["7 días", "30 días", "90 días", "Completo"]},
]

PRECIOS_FAQS = [
    {"q": "¿El plan Free caduca?",
     "a": "No. Puedes usar el plan Free de forma indefinida mientras tu cartera esté dentro de sus límites (50 propiedades y 25 clientes)."},
    {"q": "¿El matching por IA está en todos los planes?",
     "a": "Sí. El motor de matching está incluido en todos los planes, también en el Free."},
    {"q": "¿Puedo cambiar de plan más adelante?",
     "a": "Sí, puedes subir o bajar de plan en cualquier momento sin perder tu histórico de datos."},
    {"q": "¿Desde qué plan puedo gestionar varias oficinas?",
     "a": "Desde el plan Pro, que admite hasta 5 oficinas. Para redes con más sedes, API sin límite y soporte dedicado, el plan Enterprise no tiene límite de oficinas."},
    {"q": "¿Los precios incluyen IVA?",
     "a": "[COMPLETAR: confirmar si los importes mostrados incluyen o no IVA antes de publicar.]"},
]

# ---------------------------------------------------------------------------
# Páginas pilar
# ---------------------------------------------------------------------------
PILLARS = {
    "software-crm-inmobiliario": {
        "name": "Software CRM inmobiliario",
        "meta_title": "Software CRM inmobiliario con IA | KageSan CRM",
        "meta_description": (
            "Gestiona propiedades, clientes y equipo desde un solo lugar. Matching "
            "automático con IA, pipeline visual y reportes en tiempo real. Empieza gratis."
        ),
        "hero_kicker": "Producto",
        "hero_title": "Software CRM inmobiliario: gestiona tu agencia sin hojas de cálculo ni caos",
        "hero_intro": (
            "Perder un lead por no hacer seguimiento a tiempo, no saber en qué punto está "
            "cada operación o depender de tres Excels para gestionar tu cartera: son los "
            "problemas que KageSan CRM está diseñado para eliminar."
        ),
        "sections": [
            {
                "heading": "Qué hace un CRM inmobiliario y por qué tu agencia lo necesita",
                "body": [
                    "KageSan es un CRM pensado específicamente para agencias inmobiliarias, "
                    "no una herramienta genérica adaptada a la fuerza. Un CRM inmobiliario "
                    "no es solo una agenda de contactos: es el sistema que conecta cuatro cosas.",
                ],
                "bullets": [
                    "La cartera de propiedades (fichas, estado, disponibilidad, oficina asignada).",
                    "La cartera de clientes (compradores, vendedores, propietarios, inquilinos).",
                    "El proceso comercial, desde el primer contacto hasta el cierre.",
                    "El equipo: quién lleva qué, en qué oficina y con qué carga de trabajo.",
                ],
                "body_after": [
                    "Sin un sistema centralizado, esta información vive repartida entre "
                    "WhatsApp, correo, Excel y la memoria del agente. Cuando alguien rota "
                    "de puesto, el conocimiento se va con él.",
                ],
            },
        ],
        "features_heading": "Funcionalidades principales de KageSan CRM",
        "features": [
            {"title": "Propiedades y clientes multi-oficina",
             "text": "Todas las fichas en un único lugar, visibles según permisos por oficina o equipo. Sirve tanto para un agente solo como para una red con varias sedes."},
            {"title": "Matching inteligente con IA",
             "text": "El sistema cruza el score financiero y las preferencias de cada cliente con las propiedades disponibles y prioriza las coincidencias con más probabilidad de cierre."},
            {"title": "Pipeline visual tipo Kanban",
             "text": "Cada oportunidad se mueve por etapas (contacto, visita, negociación, cierre) en un tablero. De un vistazo sabes qué necesita atención hoy."},
            {"title": "Dashboards en tiempo real",
             "text": "Actividad, propiedades más vistas y rendimiento por agente y por oficina, sin pedir un informe a nadie."},
            {"title": "Automatización de tareas",
             "text": "Recordatorios de seguimiento, asignación automática de leads y flujos configurables para que nada se quede sin respuesta."},
        ],
        "audience_heading": "Para quién es KageSan CRM",
        "audience": [
            "Agentes independientes que quieren dejar de gestionar su cartera en Excel.",
            "Agencias pequeñas y medianas que coordinan varios agentes sobre la misma cartera.",
            "Redes multi-oficina y franquicias que necesitan visibilidad central con permisos por sede.",
        ],
        "faqs": [
            {"q": "¿Necesito conocimientos técnicos para usar KageSan CRM?",
             "a": "No. La plataforma está pensada para que cualquier agente inmobiliario, sin formación técnica, empiece a usarla el mismo día."},
            {"q": "¿Puedo probarlo antes de pagar?",
             "a": "Sí. El plan Free incluye la gestión de hasta 50 propiedades y 25 clientes, sin coste y sin tarjeta."},
            {"q": "¿Sirve para una sola oficina o solo para redes grandes?",
             "a": "Para ambos casos. Los planes escalan desde un agente individual hasta estructuras multi-oficina con API y soporte dedicado."},
        ],
        "cta_title": "Prueba KageSan CRM gratis",
        "cta_text": "Digitaliza tu agencia sin cambiar tu forma de trabajar. Empieza con el plan Free o mira una demo guiada.",
    },

    "matching-inteligente-ia": {
        "name": "Matching inteligente con IA",
        "meta_title": "Matching inmobiliario con IA | KageSan CRM",
        "meta_description": (
            "Empareja compradores con propiedades automáticamente según score financiero y "
            "preferencias. Menos tiempo buscando, más tiempo cerrando."
        ),
        "hero_kicker": "Producto",
        "hero_title": "Matching inteligente: la IA que empareja a tus clientes con la propiedad correcta",
        "hero_intro": (
            "Un agente dedica horas cada semana a revisar su cartera para encontrar «qué "
            "propiedad le puede interesar a este cliente». El matching de KageSan hace ese "
            "cruce en segundos y con criterios que un humano no procesa tan rápido: score "
            "financiero, historial de interacción y preferencias explícitas e implícitas."
        ),
        "features_heading": "Cómo funciona el matching inteligente",
        "features": [
            {"title": "1 · Verificación financiera",
             "text": "El sistema evalúa la capacidad de compra del cliente a partir de los datos disponibles y le asigna un score de cualificación real."},
            {"title": "2 · Análisis de preferencias",
             "text": "No solo lo que el cliente dijo que buscaba, también lo que su comportamiento (fichas vistas, tiempo, descartes) revela sobre lo que quiere."},
            {"title": "3 · Cruce automático con la cartera",
             "text": "El motor compara ese perfil con las propiedades disponibles en tiempo real y prioriza las coincidencias más probables."},
            {"title": "4 · Alerta al agente",
             "text": "En lugar de buscar a mano, el agente recibe las coincidencias ya filtradas y ordenadas por relevancia."},
        ],
        "sections": [
            {
                "heading": "Por qué esto importa para tu agencia",
                "bullets": [
                    "Menos tiempo administrativo y más tiempo de venta: el agente deja de hacer de buscador manual.",
                    "Menos oportunidades perdidas: una coincidencia que nadie relacionó a tiempo es una venta que se escapa.",
                    "Mejor experiencia de cliente: propuestas relevantes desde el primer contacto generan confianza.",
                    "Escala con tu cartera: cuanto más volumen gestionas, más valor aporta frente al cruce manual.",
                ],
            },
        ],
        "table": {
            "heading": "Matching con IA frente a búsqueda manual",
            "head": ["", "Búsqueda manual", "Matching con IA (KageSan)"],
            "rows": [
                ["Tiempo por cliente", "15-30 min revisando cartera", "Automático, en segundos"],
                ["Criterio", "Depende de la memoria del agente", "Score financiero + preferencias + comportamiento"],
                ["Consistencia", "Varía según el agente", "Mismo criterio para toda la agencia"],
                ["Escalabilidad", "Limitada por el tiempo disponible", "Escala con el volumen de cartera"],
            ],
        },
        "faqs": [
            {"q": "¿El matching sustituye el criterio del agente?",
             "a": "No, lo complementa. El sistema prioriza las coincidencias más probables; el agente decide cómo y cuándo contactar."},
            {"q": "¿Necesito un volumen mínimo de propiedades para que sea útil?",
             "a": "Es útil desde el primer momento, pero su valor crece con la cartera, que es donde la búsqueda manual se vuelve inviable."},
            {"q": "¿En qué planes está disponible?",
             "a": "El matching por IA está incluido en todos los planes, también en el plan Free."},
        ],
        "cta_title": "Descubre cuántas coincidencias se te están escapando",
        "cta_text": "Prueba el motor de matching con tu propia cartera en el plan Free, o pídenos una demo guiada.",
    },

    "gestion-multi-oficina": {
        "name": "Gestión multi-oficina",
        "meta_title": "CRM multi-oficina para redes inmobiliarias | KageSan CRM",
        "meta_description": (
            "Coordina varias oficinas, equipos y carteras desde un único panel: permisos por "
            "sede, visibilidad centralizada y reportes comparativos."
        ),
        "hero_kicker": "Producto",
        "hero_title": "Gestión multi-oficina: un solo sistema para toda tu red inmobiliaria",
        "hero_intro": (
            "Cuando una agencia crece a varias oficinas, el problema deja de ser «gestionar "
            "propiedades» y pasa a ser «coordinar equipos que no se ven entre sí». KageSan "
            "opera como sistema único de varias oficinas, con permisos diferenciados y visión "
            "consolidada para dirección."
        ),
        "features_heading": "Qué resuelve la gestión multi-oficina en KageSan",
        "features": [
            {"title": "Cartera compartida, visibilidad controlada",
             "text": "Todas las oficinas trabajan sobre el mismo sistema, pero cada equipo ve solo lo que le corresponde. Dirección tiene visión completa de todas las sedes."},
            {"title": "Matching entre oficinas",
             "text": "El motor identifica que un cliente de la sede A encaja con una propiedad de la sede B, algo casi imposible de detectar a mano."},
            {"title": "Reportes comparativos",
             "text": "Rendimiento, propiedades cerradas y tiempo medio de cierre, comparables entre sedes desde un único dashboard."},
            {"title": "Procesos estandarizados",
             "text": "Los pipelines y flujos se configuran una vez y se aplican igual en todas las oficinas, sin que cada sede invente su proceso."},
        ],
        "sections": [
            {
                "heading": "Para quién está pensado",
                "bullets": [
                    "Agencias con 2 o más oficinas físicas.",
                    "Franquicias inmobiliarias que necesitan un estándar común entre franquiciados.",
                    "Redes en crecimiento que quieren evitar la fragmentación de datos antes de que sea un problema.",
                ],
            },
            {
                "heading": "Planes con multi-oficina",
                "body": [
                    "La estructura multi-oficina se activa a medida que la agencia crece, sin migrar de sistema.",
                ],
                "bullets": [
                    "Plan Pro: hasta 5 oficinas, con permisos por sede y reportes comparativos.",
                    "Plan Enterprise: oficinas sin límite, acceso por API y soporte dedicado para la implantación y el día a día.",
                ],
            },
        ],
        "faqs": [
            {"q": "¿Puedo empezar con una oficina y añadir más después?",
             "a": "Sí. La estructura multi-oficina se puede activar cuando la agencia crece, sin necesidad de cambiar de sistema."},
            {"q": "¿Los agentes de una oficina pueden ver los datos de otra?",
             "a": "Solo si así se configura. Los permisos son granulares por oficina, equipo o rol."},
            {"q": "¿Desde qué plan puedo gestionar varias oficinas?",
             "a": "Desde el plan Pro, con hasta 5 oficinas. Para más sedes, API sin límite y soporte dedicado, el plan Enterprise no tiene límite de oficinas."},
        ],
        "cta_title": "Diseñemos la estructura multi-oficina de tu red",
        "cta_text": "Cuéntanos cuántas sedes y equipos tienes y te proponemos la configuración y el plan adecuados.",
    },

    "integraciones": {
        "name": "Integraciones",
        "meta_title": "Integraciones del CRM inmobiliario | KageSan CRM",
        "meta_description": (
            "Conecta KageSan con portales inmobiliarios, WhatsApp, email y tu web. Centraliza "
            "los leads de todos tus canales en un solo CRM."
        ),
        "hero_kicker": "Producto",
        "hero_title": "Integraciones: conecta KageSan con las herramientas que ya usas",
        "hero_intro": (
            "Un CRM que no se conecta con el resto de tus canales se convierte en una tarea "
            "administrativa más. KageSan centraliza los leads y la actividad que generas en "
            "portales, comunicación directa y tu propia web, sin copiar y pegar de un sistema a otro."
        ),
        "notice": (
            "Nota de contenido (pendiente antes de publicar): confirmar la lista real de "
            "portales inmobiliarios integrados, el proveedor de email/WhatsApp y el alcance "
            "de la API pública. No prometer integraciones que aún no existan."
        ),
        "features_heading": "Categorías de integración",
        "features": [
            {"title": "Portales inmobiliarios",
             "text": "Recepción automática de los leads generados en portales, con creación directa de la ficha de cliente y matching inmediato contra la cartera. Disponible desde el plan Basic (2 portales), 5 en Pro y sin límite en Enterprise."},
            {"title": "Comunicación: email y WhatsApp",
             "text": "Seguimiento centralizado de las conversaciones con cada cliente desde su ficha, sin depender de la bandeja de entrada personal de cada agente."},
            {"title": "Web propia de la agencia",
             "text": "Sincronización de la cartera publicada en tu web con el inventario de KageSan, para no mantener dos fuentes de verdad."},
            {"title": "API para integraciones a medida",
             "text": "Claves de API desde el plan Basic (1), 2 en Pro y sin límite en Enterprise, para conectar KageSan con ERPs u otras herramientas propias."},
        ],
        "sections": [
            {
                "heading": "Por qué importa centralizar los canales",
                "body": [
                    "Cada canal sin integrar es un punto donde se pierde información o se "
                    "retrasa el seguimiento: un lead de portal que tarda un día en llegar al "
                    "agente, una conversación de WhatsApp que no queda en la ficha, una "
                    "propiedad vendida que sigue publicada. Integrar los canales en el CRM "
                    "elimina esos huecos.",
                ],
            },
        ],
        "faqs": [
            {"q": "¿Qué portales inmobiliarios están soportados actualmente?",
             "a": "[Completar con la lista real de portales integrados antes de publicar.]"},
            {"q": "¿La integración con WhatsApp requiere una cuenta de WhatsApp Business?",
             "a": "[Confirmar el requisito técnico real (proveedor y tipo de cuenta) antes de publicar.]"},
            {"q": "¿Puedo pedir una integración que no está en la lista?",
             "a": "Sí. Con acceso por API (desde el plan Basic) puedes construir integraciones a medida; en Enterprise el equipo ayuda a diseñarlas."},
        ],
        "cta_title": "Consulta qué integraciones necesita tu agencia",
        "cta_text": "Cuéntanos qué portales y herramientas usas hoy y te decimos cómo se conectan con KageSan.",
    },
}

# ---------------------------------------------------------------------------
# Páginas por tipo de agencia
# ---------------------------------------------------------------------------
SEGMENTS = {
    "crm-para-agentes-inmobiliarios-independientes": {
        "name": "CRM para agentes inmobiliarios independientes",
        "meta_title": "CRM para agentes inmobiliarios independientes | KageSan CRM",
        "meta_description": (
            "Deja de gestionar tu cartera en Excel y WhatsApp. Organiza clientes y "
            "propiedades y deja que la IA te diga a quién ofrecer cada inmueble. Prueba gratis."
        ),
        "hero_kicker": "Para agentes independientes",
        "hero_title": "CRM para agentes inmobiliarios independientes",
        "hero_intro": (
            "Cuando trabajas solo, cada minuto buscando en qué propiedad encaja cada cliente "
            "es un minuto que no dedicas a vender. KageSan te da la estructura de una gran "
            "agencia sin la complejidad, desde el plan gratuito."
        ),
        "problems_heading": "Los problemas que ya conoces",
        "problems": [
            "Clientes repartidos entre el móvil, el correo y una hoja de cálculo.",
            "Se te olvida hacer seguimiento a un lead y se enfría.",
            "No recuerdas qué propiedad le enseñaste ya a cada cliente.",
            "Pierdes tiempo comparando a mano el perfil del cliente con la cartera disponible.",
        ],
        "features_heading": "Cómo te ayuda KageSan",
        "features": [
            {"title": "Toda tu cartera en un solo lugar",
             "text": "Propiedades y clientes organizados, buscables y actualizados, sin archivos sueltos."},
            {"title": "Matching automático",
             "text": "El sistema te sugiere qué cliente puede interesarse por cada propiedad nueva, y al revés, según score financiero y preferencias."},
            {"title": "Seguimiento que no se olvida",
             "text": "Recordatorios automáticos para que ningún lead se quede sin respuesta por falta de tiempo."},
            {"title": "Pipeline visual",
             "text": "Ves de un vistazo en qué fase está cada operación: contacto, visita, negociación, cierre."},
        ],
        "sections": [
            {
                "heading": "Por qué empezar gratis tiene sentido",
                "body": [
                    "El plan Free incluye la gestión de hasta 50 propiedades y 25 clientes, "
                    "sin coste y sin tarjeta. Es suficiente para digitalizar tu cartera actual "
                    "y comprobar el impacto del matching automático antes de decidir si "
                    "necesitas más capacidad.",
                ],
            },
        ],
        "faqs": [
            {"q": "¿Es complicado migrar mi cartera desde Excel?",
             "a": "No. La importación de datos está pensada para que empieces el mismo día."},
            {"q": "¿Tengo que pagar desde el principio?",
             "a": "No. Puedes usar el plan Free de forma indefinida mientras tu cartera esté dentro de sus límites (50 propiedades y 25 clientes)."},
            {"q": "¿Y si crezco y quiero incorporar más agentes?",
             "a": "Puedes cambiar de plan en cualquier momento sin perder tu histórico de datos."},
        ],
        "cta_title": "Organiza tu cartera hoy mismo, sin coste",
        "cta_text": "Crea tu cuenta gratis y prueba el matching con tus propios datos.",
    },

    "crm-para-agencias-inmobiliarias": {
        "name": "CRM para agencias inmobiliarias",
        "meta_title": "CRM para agencias inmobiliarias | KageSan CRM",
        "meta_description": (
            "Coordina a todo tu equipo sobre una misma cartera, con pipelines, reportes y "
            "matching por IA. El CRM para agencias que quieren escalar sin perder el control."
        ),
        "hero_kicker": "Para agencias",
        "hero_title": "CRM para agencias inmobiliarias",
        "hero_intro": (
            "Cuando una agencia pasa de uno a varios agentes, el reto cambia: evitar que dos "
            "agentes contacten al mismo cliente, que una propiedad se quede sin seguimiento, "
            "o que la dirección no tenga visibilidad real. KageSan centraliza la cartera y da "
            "a cada rol la vista que necesita."
        ),
        "features_heading": "Lo que gana tu agencia",
        "features": [
            {"title": "Cartera compartida sin duplicidades",
             "text": "Propiedades y clientes visibles para todo el equipo, con un responsable claro por cada ficha."},
            {"title": "Reparto inteligente de leads",
             "text": "Los nuevos contactos se asignan por reglas (carga de trabajo, especialización, zona), no por quién estaba más cerca del teléfono."},
            {"title": "Visibilidad para dirección",
             "text": "Dashboards con el rendimiento de cada agente, el estado de cada oportunidad y las propiedades con más actividad."},
            {"title": "Matching a nivel de agencia",
             "text": "El motor cruza todos los clientes de la agencia con toda la cartera, detectando coincidencias que un solo agente no vería."},
            {"title": "Procesos estandarizados",
             "text": "Un único pipeline configurado para toda la agencia, para que la forma de trabajar no dependa de cada agente."},
        ],
        "sections": [
            {
                "heading": "Escala sin perder el control",
                "body": [
                    "A medida que la agencia crece —más agentes, más propiedades, más "
                    "clientes—, un sistema central deja de ser una comodidad y pasa a ser la "
                    "condición para no perder oportunidades. El plan Pro está pensado para "
                    "ese momento: cartera sin límite, hasta 5 oficinas, analítica avanzada y "
                    "automatizaciones para que crecer no dependa de contratar más personal "
                    "administrativo.",
                ],
            },
        ],
        "faqs": [
            {"q": "¿Cuántos agentes puedo dar de alta?",
             "a": "Depende del plan: 3 usuarios en Basic, 10 en Pro y sin límite en Enterprise. Para equipos grandes, recomendamos hablar con ventas."},
            {"q": "¿Puedo definir permisos distintos por rol?",
             "a": "Sí. Agentes, responsables de equipo y dirección pueden tener niveles de acceso diferentes."},
            {"q": "¿El reparto de leads se puede personalizar?",
             "a": "Sí. Las reglas de asignación son configurables según los criterios de la agencia."},
        ],
        "cta_title": "Descubre cómo KageSan organiza a todo tu equipo",
        "cta_text": "Pide una demo con tu caso concreto o empieza con el plan Pro.",
    },

    "crm-para-franquicias-inmobiliarias": {
        "name": "CRM para franquicias y redes multi-oficina",
        "meta_title": "CRM para franquicias y redes multi-oficina | KageSan CRM",
        "meta_description": (
            "Un estándar común para todos tus franquiciados: cartera, pipeline y reportes "
            "unificados, con visibilidad centralizada para la central. Solicita una demo."
        ),
        "hero_kicker": "Para franquicias y redes",
        "hero_title": "CRM para franquicias y redes inmobiliarias multi-oficina",
        "hero_intro": (
            "Cuando cada franquiciado gestiona su oficina con su propio sistema —o sin "
            "ninguno—, la central pierde dos cosas a la vez: visibilidad real del negocio y "
            "capacidad de detectar sinergias entre oficinas. KageSan da a las redes un "
            "estándar común sin quitarle a cada oficina su autonomía."
        ),
        "problems_heading": "El reto específico de las redes multi-oficina",
        "problems": [
            "Cada franquiciado con su propio criterio de seguimiento y de reporte.",
            "La central no tiene datos consolidados y fiables en tiempo real.",
            "Un cliente de una oficina que encajaría con una propiedad de otra, y nadie lo detecta.",
            "Incorporar una oficina nueva implica formar desde cero en un sistema distinto cada vez.",
        ],
        "features_heading": "Cómo lo resuelve KageSan",
        "features": [
            {"title": "Un único sistema, permisos por oficina",
             "text": "Cada franquiciado gestiona su cartera y su equipo con autonomía; la central mantiene visibilidad consolidada de toda la red."},
            {"title": "Matching entre oficinas",
             "text": "El motor no se limita a la cartera local: identifica coincidencias entre clientes y propiedades de distintas sedes."},
            {"title": "Reportes comparables",
             "text": "La central compara el rendimiento entre oficinas con los mismos indicadores, porque todas operan sobre el mismo proceso."},
            {"title": "Onboarding estandarizado",
             "text": "Incorporar una oficina es darla de alta en el sistema existente, no implantar una herramienta nueva."},
            {"title": "API y soporte dedicado",
             "text": "El plan Enterprise incluye API para integrar con los sistemas de la central y soporte dedicado para el despliegue en toda la red."},
        ],
        "sections": [
            {
                "heading": "Pensado para crecer con la red",
                "body": [
                    "Tenga la red 3 oficinas o 30, la estructura de KageSan escala sin que "
                    "cada nueva incorporación suponga renegociar el proceso. La central define "
                    "el estándar; cada oficina opera con la flexibilidad que necesita dentro de él.",
                ],
            },
        ],
        "faqs": [
            {"q": "¿Los franquiciados pueden personalizar su pipeline?",
             "a": "Se puede mantener un estándar de red con margen de personalización local; se define según las necesidades de cada franquicia."},
            {"q": "¿Qué pasa con los datos si un franquiciado deja la red?",
             "a": "Se recomienda definir esta política con el equipo comercial al contratar el plan Enterprise, según la estructura contractual de la franquicia."},
            {"q": "¿Hay que migrar todas las oficinas a la vez?",
             "a": "No. La incorporación puede ser progresiva, oficina por oficina."},
        ],
        "cta_title": "Estandaricemos tu red sin quitarle autonomía a cada oficina",
        "cta_text": "Cuéntanos cuántas oficinas tiene la red y te proponemos el despliegue.",
    },
}

# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------
HOME_BENTO = [
    {
        "id": "bt1",
        "label": "Agentes independientes",
        "lead": "Toda tu cartera organizada y el matching por IA sugiriéndote a quién ofrecer cada inmueble. Desde el plan Free.",
        "cards": [
            {"kind": "stat", "title": "Tiempo de búsqueda por cliente",
             "stat": "seg", "stat_pre": "&lt;1", "text": "frente a 15-30 min revisando la cartera a mano <em>(ejemplo)</em>."},
            {"kind": "text", "title": "Qué incluye",
             "text": "50 propiedades, 25 clientes, pipeline visual e importación desde Excel, sin coste.",
             "link_slug": "crm-para-agentes-inmobiliarios-independientes", "link_label": "Ver la página para agentes"},
        ],
    },
    {
        "id": "bt2",
        "label": "Agencias",
        "lead": "Una sola cartera para todo el equipo, reparto de leads por reglas y dashboards de dirección sin pedir informes.",
        "cards": [
            {"kind": "stat", "title": "Coincidencias cliente-propiedad detectadas",
             "stat": "%", "stat_pre": "+30", "text": "que un agente, viendo solo su cartera, no habría relacionado <em>(ejemplo)</em>."},
            {"kind": "text", "title": "Qué incluye",
             "text": "Cartera compartida, permisos por rol, pipeline estandarizado y matching a nivel de agencia. Hasta 5 oficinas en el plan Pro.",
             "link_slug": "crm-para-agencias-inmobiliarias", "link_label": "Ver la página para agencias"},
        ],
    },
    {
        "id": "bt3",
        "label": "Franquicias y redes",
        "lead": "Un estándar común para todos los franquiciados, con visibilidad consolidada para la central y matching entre oficinas.",
        "cards": [
            {"kind": "stat", "title": "Alta de una oficina nueva",
             "stat": "días", "stat_pre": "1-2", "text": "sobre el sistema que ya usa la red, sin implantar nada nuevo <em>(ejemplo)</em>."},
            {"kind": "text", "title": "Qué incluye",
             "text": "Permisos por oficina, reportes comparables, API y soporte dedicado en el plan Enterprise.",
             "link_slug": "crm-para-franquicias-inmobiliarias", "link_label": "Ver la página para franquicias"},
        ],
    },
]

HOME_FAQS = [
    {"q": "¿Necesito conocimientos técnicos para usar KageSan CRM?",
     "a": "No. Cualquier agente inmobiliario puede empezar a usarlo el mismo día, sin formación técnica."},
    {"q": "¿Puedo probarlo gratis?",
     "a": "Sí. El plan Free permite gestionar hasta 50 propiedades y 25 clientes, sin coste y sin tarjeta."},
    {"q": "¿El matching por IA está en todos los planes?",
     "a": "Sí, también en el plan Free. Cambia el volumen de cartera y de equipo, no el acceso al motor de matching."},
    {"q": "¿Sirve para un agente solo y para una red con varias oficinas?",
     "a": "Para ambos. Los planes escalan desde un usuario hasta estructuras multi-oficina con API y soporte dedicado."},
    {"q": "¿Puedo importar mi cartera desde Excel?",
     "a": "Sí. La importación de datos está pensada para empezar a operar el mismo día."},
]

# ---------------------------------------------------------------------------
# Glosario
# ---------------------------------------------------------------------------
GLOSSARY_TERMS = [
    {"term": "CRM inmobiliario",
     "definition": "Sistema que centraliza la gestión de clientes, propiedades y el proceso comercial de una agencia inmobiliaria.",
     "link": "/software-crm-inmobiliario"},
    {"term": "Pipeline de ventas",
     "definition": "Representación visual de las etapas por las que pasa una oportunidad, del primer contacto al cierre (contacto → visita → negociación → cierre).",
     "link": None},
    {"term": "Matching inmobiliario",
     "definition": "Emparejar automáticamente el perfil de un cliente con las propiedades de una cartera según sus preferencias y su capacidad financiera.",
     "link": "/matching-inteligente-ia"},
    {"term": "Lead scoring",
     "definition": "Puntuación de un lead según su probabilidad de conversión, a partir de datos financieros, comportamiento e interacciones previas.",
     "link": None},
    {"term": "Score financiero",
     "definition": "Indicador que resume la capacidad de compra estimada de un cliente, usado para priorizar qué propiedades ofrecerle.",
     "link": "/matching-inteligente-ia"},
    {"term": "Lead",
     "definition": "Contacto que ha mostrado interés en comprar, vender o alquilar una propiedad y que aún no es cliente activo.",
     "link": None},
    {"term": "Cartera de propiedades",
     "definition": "Conjunto de inmuebles que gestiona un agente o una agencia en un momento dado.",
     "link": None},
    {"term": "Multi-oficina / multi-sede",
     "definition": "Estructura en la que una agencia o red opera desde varias oficinas físicas gestionadas desde un sistema común.",
     "link": "/gestion-multi-oficina"},
    {"term": "Kanban (tablero visual)",
     "definition": "Visualización del pipeline en columnas por etapa, para ver de un vistazo el estado de todas las oportunidades abiertas.",
     "link": None},
    {"term": "Dashboard",
     "definition": "Panel de indicadores en tiempo real sobre la actividad comercial: propiedades vistas, oportunidades abiertas, rendimiento por agente.",
     "link": None},
    {"term": "Automatización de tareas",
     "definition": "Acciones que el sistema ejecuta solo (recordatorios, asignación de leads, notificaciones) sin intervención manual.",
     "link": None},
    {"term": "Ficha de propiedad",
     "definition": "Registro individual de un inmueble con sus datos, estado, disponibilidad y oficina o agente asignado.",
     "link": None},
    {"term": "Ficha de cliente",
     "definition": "Registro individual de un cliente con sus datos de contacto, preferencias, historial de interacción y score financiero.",
     "link": None},
    {"term": "API (en contexto CRM)",
     "definition": "Interfaz que permite conectar el CRM con otros sistemas (webs, ERPs, herramientas internas) para intercambiar datos automáticamente.",
     "link": "/integraciones"},
    {"term": "Onboarding",
     "definition": "Proceso de incorporación inicial: de un cliente al pipeline de ventas, o de una agencia u oficina al sistema CRM.",
     "link": None},
    {"term": "Franquicia inmobiliaria",
     "definition": "Modelo en el que oficinas independientes operan bajo una marca y un estándar de proceso comunes.",
     "link": "/crm-para-franquicias-inmobiliarias"},
    {"term": "Proptech",
     "definition": "Sector de tecnología aplicada al mercado inmobiliario: CRM, IA, portales y herramientas de gestión.",
     "link": None},
    {"term": "Tasa de conversión inmobiliaria",
     "definition": "Porcentaje de leads que acaban convirtiéndose en una operación cerrada.",
     "link": None},
    {"term": "Reporte comparativo",
     "definition": "Informe que compara el rendimiento entre agentes, equipos u oficinas usando los mismos indicadores.",
     "link": "/gestion-multi-oficina"},
    {"term": "Preferencias implícitas vs. explícitas",
     "definition": "Explícitas: lo que el cliente dice que busca. Implícitas: lo que su comportamiento (fichas vistas, tiempo de interacción) revela realmente.",
     "link": "/matching-inteligente-ia"},
]

# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------
DEMO_POINTS = [
    "Cómo se organiza la cartera de propiedades y clientes desde el primer día.",
    "El matching por IA funcionando con un caso similar al de tu agencia.",
    "El pipeline visual y cómo se mueve una oportunidad de principio a fin.",
    "Los dashboards y reportes que tendría disponibles tu equipo.",
    "Dudas concretas sobre tu estructura: una oficina, varias, tamaño de equipo.",
]

DEMO_FAQS = [
    {"q": "¿La demo tiene algún coste?", "a": "No, es gratuita y sin compromiso."},
    {"q": "¿Cuánto dura?", "a": "Unos 20 minutos, ajustables según las preguntas del equipo."},
    {"q": "¿Puedo llevar a más personas de mi equipo?", "a": "Sí. Recomendamos incluir a quien vaya a usar el sistema en el día a día."},
    {"q": "¿Puedo probarlo sin esperar a la demo?", "a": "Sí. El plan Free está disponible ahora mismo, sin hablar con nadie."},
]
