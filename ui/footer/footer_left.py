# ui/footer/footer_left.py

import flet as ft
from config.theme.theme import theme


def build_footer_left() -> ft.Control:
    """Footer lado izquierdo - versión de la app"""
    return ft.Text(
        "v1.0.0",
        style=theme.styles.typography.caption(color=theme.colors.TEXT_MUTED),
    )
