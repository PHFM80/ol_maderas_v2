# ui\footer\footer_content.py

from ui.footer.footer_left import build_footer_left
from ui.footer.footer_center import build_footer_center
from ui.footer.footer_right import build_footer_right

def build_footer_content():
    return {
        "left": build_footer_left(),
        "center": build_footer_center(),
        "right": build_footer_right(),
    }
