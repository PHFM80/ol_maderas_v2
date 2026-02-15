# ui\layouts\header_container.py

import flet as ft


class HeaderContainer(ft.Row):
    def __init__(
        self,
        left: ft.Control,
        app_name: ft.Control,
        view_name: ft.Control,
        right: ft.Control,
    ):
        super().__init__()

        self.expand = True
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.spacing = 0

        self.controls = [
            # Columna izquierda
            ft.Container(
                content=left,
                expand=1,
            ),

            # Columna central (2 filas)
            ft.Container(
                expand=2,
                content=ft.Column(
                    controls=[
                        app_name,
                        view_name,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=2,
                ),
            ),

            # Columna derecha
            ft.Container(
                content=right,
                expand=1,
            ),
        ]