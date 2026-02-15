# config\theme\colors.py 
from dataclasses import dataclass

@dataclass(frozen=True)
class BaseColors:
    PRIMARY: str
    PRIMARY_VARIANT: str
    ACCENT: str

    BACKGROUND: str
    SURFACE: str
    SURFACE_VARIANT: str

    SUCCESS: str
    WARNING: str
    INFO: str
    DANGER: str

    TEXT_PRIMARY: str
    TEXT_SECONDARY: str
    TEXT_MUTED: str
    TEXT_ON_PRIMARY: str
    TEXT_INPUT: str

    BORDER: str
    HOVER: str
    DISABLED: str