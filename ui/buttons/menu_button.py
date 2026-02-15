# ui/buttons/menu_button.py
import flet as ft
from typing import Callable, Optional
from config.theme.theme import theme


class MenuButton(ft.Container):
    """
    Botón genérico para el menú de navegación.
    
    Características:
    - Respeta paleta de colores del theme (claro/oscuro)
    - Estado activo visible (resaltado/sobresalido)
    - Soporta icono + texto o solo texto
    - Callback on_navigate cuando se hace click
    """
    
    def __init__(
        self,
        label: str,
        route: str,
        icon: Optional[str] = None,
        active_route: str = "",
        on_navigate: Optional[Callable[[str], None]] = None,
    ):
        super().__init__()
        
        self.label = label
        self.route = route
        self.icon = icon
        self.active_route = active_route
        self.on_navigate = on_navigate
        self.is_active = route == active_route
        
        # Estilos base
        self.height = 40
        self.min_width = 100
        self.clip_behavior = ft.ClipBehavior.ANTI_ALIAS
        self.border_radius = theme.styles.BORDER_RADIUS_MD
        
        # Padding interno
        self.padding = ft.padding.symmetric(horizontal=16, vertical=8)
        
        # Handler de click
        self.on_click = self._on_click
        
        # Construir contenido
        self._build()
        
        # Aplicar estilo activo/inactivo
        self._update_style()
    
    def _build(self):
        """Construir el contenido del botón (solo texto)"""
        # Solo texto
        self.content = ft.Text(
            value=self.label,
            style=theme.styles.typography.label(
                color=self._get_text_color()
            ),
            no_wrap=True,
        )
    
    def _get_text_color(self) -> str:
        """Retorna el color del texto según estado activo/inactivo"""
        if self.is_active:
            return theme.colors.TEXT_ON_PRIMARY
        return theme.colors.TEXT_PRIMARY
    
    def _get_bg_color(self) -> str:
        """Retorna el color de fondo según estado activo/inactivo"""
        if self.is_active:
            return theme.colors.PRIMARY_VARIANT
        return "transparent"
    
    def _get_border_color(self) -> str:
        """Retorna el color del borde según estado activo/inactivo"""
        if self.is_active:
            return theme.colors.PRIMARY
        return "transparent"
    
    def _update_style(self):
        """Actualizar estilos visuales del botón"""
        self.bgcolor = self._get_bg_color()
        # Sin borde, solo fondo
        self.border = None
    
    def set_active(self, active_route: str):
        """Actualizar estado activo del botón"""
        self.active_route = active_route
        self.is_active = self.route == active_route
        self._update_style()
        self._rebuild_content()
        self.update()
    
    def _rebuild_content(self):
        """Reconstruir contenido con colores actualizados"""
        if isinstance(self.content, ft.Text):
            self.content.style = theme.styles.typography.label(
                color=self._get_text_color()
            )
    
    def _on_click(self, e):
        """Handler cuando se hace click en el botón"""
        if self.on_navigate:
            self.on_navigate(self.route)
