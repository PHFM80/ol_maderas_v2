# features/common/view_state.py

"""
Estado global para pasar datos entre vistas.
Útil para mensajes de satisfacción, errores, etc.
"""


class ViewState:
    """Estado global para comunicación entre vistas"""
    
    def __init__(self):
        self.message = ""
        self.next_route = "home"  # Ruta a la que ir después
    
    def set_success_message(self, message: str, next_route: str = "home"):
        """Establece un mensaje de éxito"""
        self.message = message
        self.next_route = next_route
    
    def set_error_message(self, message: str, next_route: str = "home"):
        """Establece un mensaje de error"""
        self.message = message
        self.next_route = next_route
    
    def get_message(self) -> str:
        """Obtiene el mensaje"""
        return self.message
    
    def get_next_route(self) -> str:
        """Obtiene la ruta siguiente"""
        return self.next_route
    
    def clear(self):
        """Limpia el estado"""
        self.message = ""
        self.next_route = "home"


# Instancia global del estado
view_state = ViewState()
