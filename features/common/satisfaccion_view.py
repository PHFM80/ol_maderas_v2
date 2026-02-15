# features/common/satisfaccion_view.py

import flet as ft
from typing import Optional, Callable
from config.theme.theme import theme
from features.common.view_state import view_state


def satisfaccion_view(on_navigate: Optional[Callable[[str], None]] = None) -> ft.Control:
    """Vista genérica de satisfacción/éxito"""
    
    mensaje = view_state.get_message() or "Operación completada satisfactoriamente"
    ruta_siguiente = view_state.get_next_route()
    
    def handle_continue(e):
        """Navegar a la ruta siguiente y limpiar estado"""
        view_state.clear()
        
        if on_navigate:
            on_navigate(ruta_siguiente)
    
    # Contenido de la vista
    content = ft.Column(
        controls=[
            # Emoji de éxito
            ft.Text(
                "✓",
                size=80,
                color=theme.colors.SUCCESS,
            ),
            
            ft.Container(height=20),
            
            # Título
            ft.Text(
                "¡Éxito!",
                style=theme.styles.typography.section_title(
                    color=theme.colors.TEXT_PRIMARY
                ),
            ),
            
            ft.Container(height=10),
            
            # Mensaje dinámico
            ft.Text(
                mensaje,
                style=theme.styles.typography.body(
                    color=theme.colors.TEXT_SECONDARY
                ),
                text_align=ft.TextAlign.CENTER,
            ),
            
            ft.Container(height=40),
            
            # Botón para continuar
            ft.ElevatedButton(
                "Continuar",
                on_click=handle_continue,
                bgcolor=theme.colors.SUCCESS,
                color=theme.colors.TEXT_ON_PRIMARY,
                width=200,
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )
    
    # Envolver en container con padding
    return ft.Container(
        content=content,
        padding=40,
    )
