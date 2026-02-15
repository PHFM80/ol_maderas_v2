# TEST: Prueba rápida del sistema de menú
# Ejecuta: python test_menu.py

import flet as ft
from ui.menu.menu import show_menu
import config.app_config as config
from config.theme.theme import theme


async def main(page: ft.Page):
    # 1) Tema base
    page.theme = ft.Theme(
        font_family=theme.styles.FONT_FAMILY,
        color_scheme=ft.ColorScheme(
            primary=theme.colors.PRIMARY,
            secondary=theme.colors.ACCENT,
            surface=theme.colors.SURFACE,
            error=theme.colors.DANGER,
        ),
    )

    page.bgcolor = theme.colors.BACKGROUND
    page.padding = 0
    page.spacing = 0

    # 2) Identidad
    page.title = config.APP_NAME

    # 3) Configuración ventana desktop
    page.window.width = config.WINDOW_WIDTH
    page.window.min_width = config.WINDOW_WIDTH
    page.window.max_width = config.WINDOW_WIDTH
    page.window.height = config.WINDOW_HEIGHT
    page.window.min_height = config.WINDOW_HEIGHT
    page.window.resizable = False
    page.window.left = int((1920 - config.WINDOW_WIDTH) / 2)
    page.window.top = 0

    # 4) Comportamiento general
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.HIDDEN

    # 5) Mostrar menú
    await show_menu(page, view_name="home")


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
