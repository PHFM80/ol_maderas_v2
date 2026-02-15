# features/home/home_view.py
import flet as ft
from config.theme.theme import theme


def home_view() -> ft.Control:
    """Vista principal de inicio de la aplicación"""
    
    column = ft.Column(
        controls=[
            # Espacio superior
            ft.Container(height=40),
            
            # Título principal
            ft.Text(
                value="Bienvenido",
                size=32,
                weight="bold",
                color=theme.colors.TEXT_PRIMARY,
            ),
            
            # Subtítulo
            ft.Text(
                value="a tu aplicación de gestión",
                size=16,
                color=theme.colors.TEXT_SECONDARY,
            ),
            
            # Espacio
            ft.Container(height=30),
            
            # Divider
            ft.Divider(height=1),
            
            # Espacio
            ft.Container(height=30),
            
            # Mensaje principal
            ft.Text(
                value="¿Qué deseas hacer?",
                size=18,
                weight="500",
                color=theme.colors.TEXT_PRIMARY,
            ),
            
            # Instrucciones
            ft.Container(
                content=ft.Text(
                    value="Selecciona una opción en el menú de la izquierda para comenzar.",
                    size=14,
                    color=theme.colors.TEXT_SECONDARY,
                    text_align=ft.TextAlign.CENTER,
                ),
                padding=20,
                bgcolor=theme.colors.SURFACE,
                border_radius=theme.styles.BORDER_RADIUS_MD,
            ),
            
            # Espacio flexible para centrar
            ft.Container(expand=True),
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0,
    )
    
    return ft.Container(
        content=column,
        padding=40,
    )
