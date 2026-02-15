# ui/header/header_content.py
from ui.header.left import build_header_left
from ui.header.center import build_header_center
from ui.header.right import build_header_right

def build_header_content(*, app_name: str, view_name: str) -> dict:
    center = build_header_center(
        app_name=app_name,
        view_name=view_name,
    )

    return {
        "left": build_header_left(),
        "app_name": center["app_name"],
        "view_name": center["view_name"],
        "right": build_header_right(),
    }
