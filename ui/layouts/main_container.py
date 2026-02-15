# ui\layouts\main_container.py
import flet as ft


class MainContainer(ft.Container):
    def __init__(self, content: ft.Control):
        super().__init__()

        self.expand = True
        self.content = content

