# ui\header\right.py
import flet as ft
from config.theme.theme import theme

def build_header_right() -> ft.Control:
    title = theme.styles.typography.section_title(
        color=theme.colors.TEXT_PRIMARY
    )
    sub = theme.styles.typography.label(
        color=theme.colors.TEXT_PRIMARY
    )
    return ft.Column(
        spacing=4,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("Empresa ficticia", style=title, text_align=ft.TextAlign.CENTER),
            ft.Text("de Carlos Fontana", style=sub, text_align=ft.TextAlign.CENTER),
            ft.Text(
                "Av Siempre Viva 321 - Mendoza",
                style=sub,
                text_align=ft.TextAlign.CENTER,
            ),
        ],
    )


