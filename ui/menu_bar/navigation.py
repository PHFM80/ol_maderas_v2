# ui/menu_bar/navigation.py
import flet as ft
from typing import Callable, Optional
from ui.buttons.menu_button import MenuButton
from .menu_config import MENU_ITEMS


def build_menu_navigation(
    active_route: str = "home",
    on_navigate: Optional[Callable[[str], None]] = None,
) -> tuple[ft.Control, list[MenuButton]]:
    """
    Construye dinámicamente la barra de navegación a partir de MENU_ITEMS.
    
    Args:
        active_route: ruta activa actualmente (ej: "home")
        on_navigate: callback cuando se navega (recibe route)
    
    Returns:
        tuple: (container_con_botones, lista_de_botones)
        La lista de botones se retorna para que menu.py pueda actualizarlos
        cuando la ruta activa cambie.
    """
    
    # Filtrar items habilitados
    enabled_items = [item for item in MENU_ITEMS if item.get("enabled", True)]
    
    # Crear botones dinámicamente
    buttons = []
    for item in enabled_items:
        button = MenuButton(
            label=item["label"],
            route=item["route"],
            icon=item.get("icon"),
            active_route=active_route,
            on_navigate=on_navigate,
        )
        buttons.append(button)
    
    # Container con los botones
    container = ft.Row(
        controls=buttons,
        spacing=12,
        alignment=ft.MainAxisAlignment.START,
        wrap=True,  # Permitir que los botones se ajusten a la siguiente línea si es necesario
    )
    
    return container, buttons
