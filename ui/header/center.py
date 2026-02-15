# ui/header/center.py
import flet as ft
from config.theme.theme import theme

def build_header_center(*, app_name: str, view_name: str) -> dict:
    return {
        "app_name": ft.Text(
            app_name,
            style=theme.styles.typography.display(
                color=theme.colors.TEXT_PRIMARY
            ),
        ),
        "view_name": ft.Container(),
    }
