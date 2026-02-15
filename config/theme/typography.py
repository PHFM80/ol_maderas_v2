# config\theme\typography.py
from dataclasses import dataclass
import flet as ft


@dataclass(frozen=True)
class Typography:
    # Fuente base (fallback multiplataforma)
    FONT_FAMILY: str = "Segoe UI, Roboto, Helvetica, Arial, sans-serif"

    # Tamaños
    FONT_SIZE_XS: int = 12
    FONT_SIZE_SM: int = 14
    FONT_SIZE_MD: int = 16
    FONT_SIZE_LG: int = 18
    FONT_SIZE_XL: int = 24

    # --- ESTILOS SEMÁNTICOS ---

    def display(self, color: str) -> ft.TextStyle:
        """App Name / Display"""
        return ft.TextStyle(
            size=self.FONT_SIZE_XL,
            weight=ft.FontWeight.BOLD,
            font_family=self.FONT_FAMILY,
            color=color,
        )

    def section_title(self, color: str) -> ft.TextStyle:
        """View name / títulos de sección"""
        return ft.TextStyle(
            size=self.FONT_SIZE_LG,
            weight=ft.FontWeight.W_600,
            font_family=self.FONT_FAMILY,
            color=color,
        )

    def body(self, color: str) -> ft.TextStyle:
        """Contenido principal"""
        return ft.TextStyle(
            size=self.FONT_SIZE_MD,
            weight=ft.FontWeight.NORMAL,
            font_family=self.FONT_FAMILY,
            color=color,
        )

    def label(self, color: str) -> ft.TextStyle:
        """Labels / info secundaria"""
        return ft.TextStyle(
            size=self.FONT_SIZE_SM,
            weight=ft.FontWeight.W_500,
            font_family=self.FONT_FAMILY,
            color=color,
        )

    def caption(self, color: str) -> ft.TextStyle:
        """Micro-info / versión / placeholders"""
        return ft.TextStyle(
            size=self.FONT_SIZE_XS,
            weight=ft.FontWeight.NORMAL,
            font_family=self.FONT_FAMILY,
            color=color,
        )

    def button(self, color: str) -> ft.TextStyle:
        """Texto de botones CTA"""
        return ft.TextStyle(
            size=self.FONT_SIZE_SM,
            weight=ft.FontWeight.BOLD,
            font_family=self.FONT_FAMILY,
            color=color,
        )


# Instancia global
typography = Typography()
