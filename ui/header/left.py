# ui/header/left.py
import flet as ft
from config.theme.theme import theme

def build_header_left() -> ft.Control:
    return ft.Column(
        spacing=6,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Image(
                src="assets/app/Logo.png",
                width=48,
                height=48,
                fit=ft.BoxFit.CONTAIN,
            ),
            ft.Text(
                "Desarrollos y Tecnología",
                style=theme.styles.typography.section_title(
                    color=theme.colors.TEXT_PRIMARY
                ),
            ),
        ],
    )
