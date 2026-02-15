# ui/menu_bar/menu_bar_content.py
from typing import Callable, Optional
from ui.menu_bar.navigation import build_menu_navigation
from ui.menu_bar.dark_light_mode import build_dark_light_mode_button


def build_menu_bar_content(
    active_route: str = "home",
    on_navigate: Optional[Callable[[str], None]] = None,
    on_theme_change: Optional[Callable[[str], None]] = None,
):
    """
    Construye el contenido completo del menu_bar (navegación + acciones).
    
    Args:
        active_route: ruta activa actual
        on_navigate: callback cuando se navega
        on_theme_change: callback cuando cambia el tema
    
    Retorna:
        dict con:
            - navigation: Container con los botones de navegación
            - actions: Botón de tema claro/oscuro
            - menu_buttons: Lista de botones (para actualizar estado después)
    """
    
    navigation, menu_buttons = build_menu_navigation(
        active_route=active_route,
        on_navigate=on_navigate,
    )
    
    return {
        "navigation": navigation,
        "actions": build_dark_light_mode_button(on_theme_change=on_theme_change),
        "menu_buttons": menu_buttons,
    }
