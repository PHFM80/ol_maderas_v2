# config\theme\light.py
from .colors import BaseColors

LightColors = BaseColors(
    # Brand (Identidad)
    PRIMARY="#1487B8",
    PRIMARY_VARIANT="#4591B8",
    ACCENT="#02ADB0",

    # Surfaces (Superficies)
    BACKGROUND="#F5F5F5",
    SURFACE="#FFFFFF",
    SURFACE_VARIANT="#F8F9FA",

    # States (Estados)
    SUCCESS="#5FB3A2",
    WARNING="#F3BA8E",
    INFO="#A4C9D2",
    DANGER="#ED7572",

    # Typography (Tipografía)
    TEXT_PRIMARY="#1A202C",
    TEXT_SECONDARY="#606167",
    TEXT_MUTED="#859DC9",
    TEXT_ON_PRIMARY="#FFFFFF",
    TEXT_INPUT="#1A202C",  # Color oscuro para inputs en tema claro

    # Borders & Dividers (Estructura)
    BORDER="#E0E0E0",

    # Interactive (Interacción)
    HOVER="#D9EDF5",
    DISABLED="#D3D3D3",
)
