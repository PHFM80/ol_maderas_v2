# config\theme\theme.py

from .light import LightColors
from .dark import DarkColors
from .styles import AppStyles

class ThemeManager:
    def __init__(self, mode: str = "light"):
        self.set_mode(mode)

    def set_mode(self, mode: str):
        self.mode = mode
        self.colors = LightColors if mode == "light" else DarkColors
        self.styles = AppStyles(self.colors)


theme = ThemeManager("dark")
