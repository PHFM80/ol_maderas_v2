import flet as ft
from flet import View
from typing import Optional

import config.app_config as config
from config.theme.theme import theme

from ui.layouts.layout import BaseLayout
from ui.layouts.header_container import HeaderContainer
from ui.header.header_content import build_header_content
from ui.layouts.menu_bar_container import MenuBarContainer
from ui.menu_bar.menu_bar_content import build_menu_bar_content
from ui.footer.footer_content import build_footer_content
from ui.layouts.footer_container import FooterContainer
from ui.main.main_content import build_main_content


# Variables globales para controlar estado
_current_route: str = "home"
_menu_buttons: list = []
_main_container: Optional[ft.Container] = None
_page: Optional[ft.Page] = None
_base_layout: Optional[BaseLayout] = None


def _on_navigate(route: str):
    """
    Handler de navegación cuando se hace click en un botón del menú.
    Actualiza:
    - La ruta activa
    - El estado visual de los botones
    - El contenido principal
    """
    global _current_route, _menu_buttons, _main_container
    
    _current_route = route
    
    # 1) Actualizar estado visual de los botones
    for button in _menu_buttons:
        button.set_active(_current_route)
    
    # 2) Actualizar contenido principal (pasando on_navigate callback)
    if _main_container:
        new_content = build_main_content(_current_route, on_navigate=_on_navigate)
        _main_container.content = new_content
        _main_container.update()


def _on_theme_change(new_mode: str):
    """
    Handler cuando cambia el tema (claro/oscuro).
    Reconstruye TODA la aplicación con el nuevo tema.
    """
    global _current_route, _menu_buttons, _main_container, _page, _base_layout
    
    if not _page or not _base_layout:
        return
    
    # Reconstruir todos los componentes con el nuevo tema
    
    # 1) Header
    header_parts = build_header_content(
        app_name=_page.title,
        view_name=_current_route,
    )
    new_header = HeaderContainer(
        left=header_parts["left"],
        app_name=header_parts["app_name"],
        view_name=header_parts["view_name"],
        right=header_parts["right"],
    )
    
    # 2) Menu bar con nuevo botón de tema
    menu_parts = build_menu_bar_content(
        active_route=_current_route,
        on_navigate=_on_navigate,
        on_theme_change=_on_theme_change,
    )
    _menu_buttons = menu_parts["menu_buttons"]
    
    new_menu_bar = MenuBarContainer(
        navigation=menu_parts["navigation"],
        actions=menu_parts["actions"],
    )
    
    # 3) Main content
    new_main_content = build_main_content(_current_route, on_navigate=_on_navigate)
    _main_container.content = new_main_content
    
    # 4) Footer
    footer_parts = build_footer_content()
    new_footer = FooterContainer(
        left=footer_parts["left"],
        center=footer_parts["center"],
        right=footer_parts["right"],
    )
    
    # 5) Reconstruir el Column del layout con los nuevos componentes
    from ui.layouts.estilos_container import card_container
    
    window_height = config.WINDOW_HEIGHT
    header_height = config.HEADER_HEIGHT
    menu_height = config.MENU_HEIGHT
    main_height = config.MAIN_HEIGHT
    footer_height = config.FOOTER_HEIGHT
    
    _base_layout.bgcolor = theme.colors.BACKGROUND
    _base_layout.content = ft.Column(
        spacing=12,
        controls=[
            card_container(content=new_header, height=header_height),
            card_container(content=new_menu_bar, height=menu_height),
            card_container(content=_main_container, height=main_height),
            card_container(content=new_footer, height=footer_height),
        ],
    )
    
    _page.update()


async def show_menu(page: ft.Page, *, view_name: str = "home"):
    global _current_route, _menu_buttons, _main_container, _page, _base_layout
    
    _page = page  # Guardar referencia a la página
    page.views.clear()
    _current_route = view_name

    # 1) Detectar plataforma
    is_mobile = page.platform == "android"

    if is_mobile:
        # Mobile: todavía no implementado
        pass
    else:
        # 2) Alturas desktop (desde config)
        window_height = config.WINDOW_HEIGHT
        header_height = config.HEADER_HEIGHT
        menu_height = config.MENU_HEIGHT
        main_height = config.MAIN_HEIGHT
        footer_height = config.FOOTER_HEIGHT

    # 3) Header content (inyectado)
    header_parts = build_header_content(
        app_name=page.title,
        view_name=view_name,
    )

    header = HeaderContainer(
        left=header_parts["left"],
        app_name=header_parts["app_name"],
        view_name=header_parts["view_name"],
        right=header_parts["right"],
    )

    # 4) Menu bar content (inyectado con handler de navegación)
    menu_parts = build_menu_bar_content(
        active_route=_current_route,
        on_navigate=_on_navigate,
        on_theme_change=_on_theme_change,
    )
    _menu_buttons = menu_parts["menu_buttons"]
    
    menu_bar = MenuBarContainer(
        navigation=menu_parts["navigation"],
        actions=menu_parts["actions"],
    )

    # 5) Main content (inyectado dinámicamente)
    main_content = build_main_content(_current_route, on_navigate=_on_navigate)
    _main_container = ft.Container(content=main_content, expand=True)

    # 6) Footer content (inyectado)
    footer_parts = build_footer_content()
    footer = FooterContainer(
        left=footer_parts["left"],
        center=footer_parts["center"],
        right=footer_parts["right"],
    )

    # 7) Layout base
    layout = BaseLayout(
        header=header,
        menu_bar=menu_bar,
        main=_main_container,
        footer=footer,
        window_height=window_height,
        header_height=header_height,
        menu_height=menu_height,
        main_height=main_height,
        footer_height=footer_height,
    )
    
    _base_layout = layout  # Guardar referencia al layout

    # 8) Render
    page.views.append(
        View(
            controls=[
                ft.Container(
                    content=layout,
                    expand=True,
                )
            ],
            padding=0,
            spacing=0,
        )
    )

    page.update()
