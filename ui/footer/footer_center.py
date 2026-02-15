# ui/footer/footer_center.py

import flet as ft
from config.theme.theme import theme


def build_footer_center() -> ft.Control:
    """Footer centro - contacto"""
    return ft.Column(
        controls=[
            ft.Text(
                "dytdigitaliza@gmail.com",
                style=theme.styles.typography.caption(color=theme.colors.TEXT_PRIMARY),
            ),
            ft.Text(
                "+54 9 261 1234 5678",
                style=theme.styles.typography.caption(color=theme.colors.TEXT_MUTED),
            ),
        ],
        spacing=2,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
