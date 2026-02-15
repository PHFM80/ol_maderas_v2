# ui/main/main_content.py

import flet as ft
from typing import Optional, Callable

# Importar todas las features/vistas disponibles
from features.home.home_view import home_view
from features.common.satisfaccion_view import satisfaccion_view
from features.common.error_view import error_view

# Mapeo de rutas a funciones constructoras de vistas
VIEWS_MAP = {
    "home": home_view,
    "satisfaccion": satisfaccion_view,
    "error": error_view,
    # Agregar más vistas aquí según se desarrollen
    # "reportes": reportes_view,
    # "config": config_view,
}


def build_main_content(view_key: str, on_navigate: Optional[Callable[[str], None]] = None) -> ft.Control:
    """
    Construye dinámicamente el contenido principal basado en la ruta.
    
    Args:
        view_key: identificador de la vista (ej: "home", "cargar_cliente")
        on_navigate: callback para navegación dentro de las vistas
    
    Returns:
        Control de Flet con la vista solicitada o un mensaje de error
    """
    
    if view_key in VIEWS_MAP:
        view_builder = VIEWS_MAP[view_key]
        
        # Verificar si la vista acepta on_navigate como parámetro
        import inspect
        sig = inspect.signature(view_builder)
        
        if 'on_navigate' in sig.parameters:
            return view_builder(on_navigate=on_navigate)
        else:
            return view_builder()
    
    # Vista no encontrada
    return ft.Column(
        controls=[
            ft.Text(
                f"Vista '{view_key}' no encontrada",
                size=18,
                weight="bold",
                color="#ED7572",
            ),
            ft.Text(
                "Por favor, selecciona una opción válida del menú.",
                size=14,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=12,
    )
