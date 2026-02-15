# ui/footer/footer_right.py

import flet as ft
from config.theme.theme import theme


def build_footer_right() -> ft.Control:
    """Footer lado derecho - logo y nombre de empresa"""
    return ft.Row(
        controls=[
            # Nombre de empresa
            ft.Column(
                controls=[
                    ft.Text(
                        "D&T",
                        size=14,
                        weight="bold",
                        color=theme.colors.TEXT_PRIMARY,
                    ),
                    ft.Text(
                        "Desarrollos y Tecnología",
                        style=theme.styles.typography.caption(color=theme.colors.TEXT_MUTED),
                    ),
                ],
                spacing=2,
                horizontal_alignment=ft.CrossAxisAlignment.END,
            ),
            
            # Logo
            ft.Image(
                src="assets/app/logo_32x32.ico",
                width=32,
                height=32,
            ),
        ],
        spacing=12,
        alignment=ft.MainAxisAlignment.END,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
