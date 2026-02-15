# ui/layouts/menu_bar_container.py

import flet as ft


class MenuBarContainer(ft.Row):
    def __init__(
        self,
        navigation: ft.Control,
        actions: ft.Control,
    ):
        super().__init__()

        self.expand = True
        self.spacing = 16
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER

        self.controls = [
            # Zona navegación (variable, ocupa más espacio)
            ft.Container(
                content=navigation,
                expand=True,
            ),

            # Zona acciones (fija: theme toggle - sin expand, solo el tamaño que necesita)
            ft.Container(
                content=actions,
                alignment=ft.Alignment(1, 0),  # Right center
            ),
        ]
