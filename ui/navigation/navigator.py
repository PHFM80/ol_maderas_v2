# ui\navigation\navigator.py
import flet as ft
from typing import Dict, Callable, Optional

class Navigator:
    def __init__(self, page: ft.Page, main_container: ft.Container):
        self.page = page
        self.main_container = main_container
        self.routes: Dict[str, Callable[[], ft.Control]] = {}
        self.current_route: Optional[str] = None

    def register_route(self, route_name: str, view_builder: Callable[[], ft.Control]):
        self.routes[route_name] = view_builder

    def navigate(self, route_name: str):
        if route_name in self.routes:
            view = self.routes[route_name]()
            self.main_container.content = view
            self.main_container.update()
            self.current_route = route_name
        else:
            print(f"Ruta no encontrada: {route_name}")