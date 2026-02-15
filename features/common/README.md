# Módulo Common

El módulo `common` contiene vistas y utilidades genéricas que pueden ser reutilizadas en todo el sistema. Estas vistas están diseñadas para manejar casos comunes como mostrar mensajes de éxito o error.

## Contenido

### 1. `view_state.py`
Este archivo define un estado global para compartir datos entre vistas. Es útil para pasar mensajes dinámicos a las vistas genéricas de satisfacción o error.

#### Uso:
```python
from features.common.view_state import view_state

# Configurar un mensaje de éxito y la ruta siguiente
view_state.set_success_message("Operación completada", next_route="home")

# Configurar un mensaje de error y la ruta siguiente
view_state.set_error_message("Ha ocurrido un error", next_route="retry")

# Obtener el mensaje actual
mensaje = view_state.get_message()

# Limpiar el estado
view_state.clear()
```

---

### 2. `satisfaccion_view.py`
Una vista genérica para mostrar mensajes de éxito.

#### Uso:
```python
from features.common.satisfaccion_view import satisfaccion_view

# Navegar a la vista de satisfacción
on_navigate("satisfaccion")
```

---

### 3. `error_view.py`
Una vista genérica para mostrar mensajes de error.

#### Uso:
```python
from features.common.error_view import error_view

# Navegar a la vista de error
on_navigate("error")
```

---

## Ejemplo de flujo
1. Configurar un mensaje dinámico:
    ```python
    view_state.set_success_message("Cliente guardado exitosamente", next_route="home")
    ```

2. Navegar a la vista genérica:
    ```python
    on_navigate("satisfaccion")
    ```

3. La vista mostrará el mensaje configurado y permitirá continuar a la ruta especificada.