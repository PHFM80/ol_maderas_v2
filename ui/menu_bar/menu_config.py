# ui/menu_bar/menu_config.py

"""
Configuración de items del menú de navegación.

Estructura de cada item:
{
    "label": str          → Texto del botón (visible)
    "route": str          → Identificador de la vista (para navegar)
    "icon": str (opt)     → Nombre del icono de Flet (ver https://flet.dev/docs/reference/icons/)
    "enabled": bool (opt) → Permite habilitar/deshabilitar por cliente
}

Ejemplo:
    {"label": "Inicio", "route": "home", "icon": "home"},

Iconos Flet populares:
- home              → Casa
- people            → Personas
- description       → Documentos
- settings          → Configuración
- logout            → Cerrar sesión

Ver más en: https://flet.dev/docs/reference/icons/
"""

MENU_ITEMS = [
    {
        "label": "Inicio",
        "route": "home",
        "enabled": True,
    },
    # Agregar más items según necesidades del cliente
]
