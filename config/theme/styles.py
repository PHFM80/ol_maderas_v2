# config/theme/styles.py
import flet as ft
from dataclasses import dataclass, field
import self
from .colors import BaseColors
from .typography import typography  # Exponer FONT_FAMILY desde typography


@dataclass
class AppStyles:
    colors: BaseColors
    typography: object = typography

    # Exponer la familia de fuentes desde typography
    FONT_FAMILY: str = typography.FONT_FAMILY

    BORDER_RADIUS_MD: int = 12
    BORDER_RADIUS_LG: int = 18

    SHADOW_SM: ft.BoxShadow = field(
        default_factory=lambda: ft.BoxShadow(
            spread_radius=0,
            blur_radius=4,
            color=ft.Colors.with_opacity(0.08, "#000000"),
        )
    )

    def card(self) -> dict:
        return {
            "bgcolor": self.colors.SURFACE,
            "border_radius": self.BORDER_RADIUS_MD,
            "border": ft.border.all(1, self.colors.BORDER),
            "shadow": self.SHADOW_SM,
            "padding": 16,
        }

    def input(self) -> dict:
        return {
            "border_color": self.colors.BORDER,
            "focused_border_color": self.colors.PRIMARY,
            "text_style": ft.TextStyle(color=self.colors.TEXT_PRIMARY),
        }
    
