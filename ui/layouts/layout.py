# ui/layouts/layout.py
import flet as ft

from ui.layouts.header_container import HeaderContainer
from ui.layouts.menu_bar_container import MenuBarContainer
from ui.layouts.main_container import MainContainer
from ui.layouts.footer_container import FooterContainer
from ui.layouts.estilos_container import card_container

from config.theme.theme import theme


class BaseLayout(ft.Container):
    def __init__(
        self,
        header: HeaderContainer,
        menu_bar: MenuBarContainer,
        main: MainContainer,
        footer: FooterContainer,
        *,
        window_height: int,
        header_height: int,
        menu_height: int,
        main_height: int,
        footer_height: int,
    ):
        super().__init__()

        # 🔹 Fondo general de la app
        self.height = window_height
        self.expand = True
        self.bgcolor = theme.colors.BACKGROUND
        self.padding = 12

        # 🔹 Columna interna
        self.content = ft.Column(
            spacing=12,
            controls=[
                card_container(content=header, height=header_height),
                card_container(content=menu_bar, height=menu_height),
                card_container(content=main, height=main_height),
                card_container(content=footer, height=footer_height),
            ],
        )
