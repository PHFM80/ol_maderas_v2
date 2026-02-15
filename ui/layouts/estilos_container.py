# ui\layouts\estilos_container.py
import flet as ft
from config.theme.theme import theme


def card_container(
    *,
    content: ft.Control,
    height: int | None = None,
    expand: bool | None = None,
) -> ft.Container:
    """
    Wrapper de Card reutilizable.
    La forma y los colores vienen 100% desde theme.styles.card()
    """

    return ft.Container(
        content=content,
        height=height,
        expand=expand,
        margin=8,
        **theme.styles.card(),
    )
