# ui/menu_bar/dark_light_mode.py

import flet as ft
from typing import Optional, Callable
from config.theme.theme import theme


class DarkLightModeButton(ft.IconButton):
    """Botón para alternar entre tema claro y oscuro"""
    
    def __init__(self, on_theme_change: Optional[Callable[[str], None]] = None):
        super().__init__()
        
        self.on_theme_change = on_theme_change
        self.tooltip = "Cambiar tema (claro/oscuro)"
        
        # Establecer icono inicial según el tema actual
        self._update_icon()
        
        self.on_click = self._on_click
    
    def _update_icon(self):
        """Actualizar icono según el tema actual"""
        if theme.mode == "dark":
            self.icon = ft.Icons.LIGHT_MODE  # Mostrar icono de sol (cambiar a claro)
        else:
            self.icon = ft.Icons.DARK_MODE   # Mostrar icono de luna (cambiar a oscuro)
    
    def _on_click(self, e):
        """Handler cuando se hace click en el botón"""
        # Alternar tema
        new_mode = "light" if theme.mode == "dark" else "dark"
        theme.set_mode(new_mode)
        
        # Actualizar icono
        self._update_icon()
        self.update()
        
        # Llamar callback si existe
        if self.on_theme_change:
            self.on_theme_change(new_mode)


def build_dark_light_mode_button(on_theme_change: Optional[Callable[[str], None]] = None) -> ft.Control:
    """Factory function para crear el botón de tema"""
    return DarkLightModeButton(on_theme_change=on_theme_change)


