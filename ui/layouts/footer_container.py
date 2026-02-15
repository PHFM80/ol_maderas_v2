# ui/layouts/footer_container.py

import flet as ft
from config.theme.theme import theme


class FooterContainer(ft.Container):
    """Container del footer con theme aplicado"""
    
    def __init__(
        self,
        left: ft.Control,
        center: ft.Control,
        right: ft.Control,
    ):
        super().__init__()

        # Row con contenido del footer
        row = ft.Row(
            controls=[
                # Columna izquierda (20%)
                ft.Container(
                    content=left,
                    expand=20,
                ),

                # Columna central (60%)
                ft.Container(
                    content=center,
                    expand=60,
                ),

                # Columna derecha (20%)
                ft.Container(
                    content=right,
                    expand=20,
                ),
            ],
            spacing=16,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        # Container con estilos del theme
        self.content = row
        self.bgcolor = theme.colors.SURFACE
        self.border_radius = 0
        self.padding = ft.padding.symmetric(horizontal=24, vertical=16)
        self.height = 80
