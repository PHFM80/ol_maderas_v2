# ⚡ QUICK START - Cómo Usar El Nuevo Sistema

## 🚀 En 3 Pasos: Agrega Un Nuevo Botón de Menú

### Paso 1: Abre `ui/menu_bar/menu_config.py`

Descomenta o copia-pega:
```python
MENU_ITEMS = [
    {
        "label": "Inicio",
        "route": "home",
        "icon": "home",
        "enabled": True,
    },
    {
        "label": "Clientes",      # ← NUEVO BOTÓN
        "route": "clientes",
        "icon": "people",
        "enabled": True,
    },
]
```

### Paso 2: Crea `features/clientes/clientes_view.py`

```python
import flet as ft

def clientes_view() -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text("Gestión de Clientes", size=24, weight="bold"),
            ft.Divider(),
            ft.Text("Aquí irá la lista de clientes..."),
        ],
        spacing=10,
    )
```

### Paso 3: Abre `ui/main/main_content.py`

Agrega la importación y registra:
```python
from features.clientes.clientes_view import clientes_view  # ← Agregar

VIEWS_MAP = {
    "home": home_view,
    "clientes": clientes_view,  # ← Agregar esta línea
}
```

---

## ✅ Listo!

Ejecuta:
```bash
python main.py
```

Deberías ver:
- Nuevo botón "👥 Clientes" en el menú
- Al clickear, aparece la vista de clientes
- El botón se resalta cuando estás en esa vista

---

## 🎨 Personalización Rápida

### Cambiar Icono del Botón

Los iconos disponibles son los de [Flet Icons](https://flet.io/docs/reference/icons/).

Ejemplos:
```python
"icon": "home",           # Casa
"icon": "people",         # Personas
"icon": "bar_chart",      # Gráfico
"icon": "settings",       # Configuración
"icon": "document",       # Documento
"icon": "check_circle",   # Check
"icon": "delete",         # Basura
"icon": "search",         # Lupa
```

### Cambiar Color del Botón Activo

En `ui/buttons/menu_button.py`, método `_get_bg_color()`:

```python
def _get_bg_color(self) -> str:
    if self.is_active:
        return theme.colors.PRIMARY_VARIANT  # ← Cambiar aquí
    return "transparent"
```

Colores disponibles en `config/theme/`:
- `theme.colors.PRIMARY`
- `theme.colors.ACCENT`
- `theme.colors.SUCCESS`
- `theme.colors.WARNING`
- `theme.colors.DANGER`

### Cambiar Altura del Botón

En `ui/buttons/menu_button.py`:

```python
self.height = 50  # ← Cambiar a 60, 70, etc.
```

### Cambiar Espaciado Entre Botones

En `ui/menu_bar/navigation.py`:

```python
container = ft.Row(
    controls=buttons,
    spacing=12,  # ← Cambiar aquí (px)
    alignment=ft.MainAxisAlignment.START,
)
```

---

## 🚫 Deshabilitar Un Botón (Sin Eliminarlo)

En `menu_config.py`:

```python
{
    "label": "Reportes",
    "route": "reportes",
    "icon": "bar_chart",
    "enabled": False,  # ← Cambiar a False
},
```

El botón no aparecerá en el menú pero puede activarse después sin cambiar código.

---

## 🧪 Probando Cambios Rápidamente

Mientras tienes la app abierta:

1. Modifica `menu_config.py`
2. Modifica `main_content.py`
3. **Reinicia la app** (`python main.py`)

(Flet no hace hot-reload, necesitas reiniciar)

---

## ❓ Preguntas Frecuentes

### P: ¿Puedo tener botones sin icono?

**R:** Sí, omite `"icon"` o ponlo en `None`:

```python
{
    "label": "Panel",
    "route": "panel",
    # "icon": None,  # Opcional, funciona sin icono
    "enabled": True,
},
```

### P: ¿Qué pasa si la vista no existe?

**R:** Aparece mensaje de error:
```
Vista 'inexistente' no encontrada
Por favor, selecciona una opción válida del menú.
```

Agrega la vista en `features/` y regístrala en `VIEWS_MAP`.

### P: ¿Puedo reordenar los botones?

**R:** Sí, solo cambia el orden en `MENU_ITEMS`:

```python
MENU_ITEMS = [
    {"label": "Clientes", ...},      # Primero
    {"label": "Inicio", ...},        # Segundo
    {"label": "Reportes", ...},      # Tercero
]
```

### P: ¿Cómo hago que un botón tenga una ruta diferente?

**R:** La `route` es solo el identificador interno. Podes usar cualquier nombre:

```python
{
    "label": "Panel Admin",
    "route": "admin_panel",  # ← Identificador único
    "icon": "admin_panel_settings",
},
```

Luego en `main_content.py`:

```python
from features.admin.admin_panel_view import admin_panel_view

VIEWS_MAP = {
    "admin_panel": admin_panel_view,  # ← Debe coincidir con "route"
}
```

---

## 🎯 Checklist Para Agregar Feature Completa

- [ ] Agregar item en `menu_config.py`
- [ ] Crear carpeta `features/nueva_feature/`
- [ ] Crear archivo `features/nueva_feature/nueva_view.py`
- [ ] Crear función `nueva_view()` en ese archivo
- [ ] Importar función en `ui/main/main_content.py`
- [ ] Agregar entrada en `VIEWS_MAP`
- [ ] Ejecutar `python main.py`
- [ ] Clickear el botón y verificar que funciona
- [ ] Verificar que el botón se resalta cuando estás en esa vista

---

## 📚 Archivos Importantes

| Archivo | Qué Hace |
|---------|----------|
| `ui/menu_bar/menu_config.py` | Define qué botones hay en el menú |
| `ui/buttons/menu_button.py` | El componente del botón (no modificar usually) |
| `ui/main/main_content.py` | Mapea rutas a vistas |
| `features/*/` | Aquí van tus vistas/componentes |
| `ui/menu/menu.py` | Controla la navegación (no tocar) |

---

## 🎓 Ejemplo Completo: Agregar "Reportes"

### 1. `ui/menu_bar/menu_config.py`
```python
MENU_ITEMS = [
    {"label": "Inicio", "route": "home", "icon": "home", "enabled": True},
    {"label": "Reportes", "route": "reportes", "icon": "bar_chart", "enabled": True},
]
```

### 2. Crear `features/reportes/reportes_view.py`
```python
import flet as ft

def reportes_view() -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text("📊 Reportes", size=24, weight="bold"),
            ft.Divider(),
            ft.Text("Generador de reportes"),
            ft.ElevatedButton("Generar Reporte", on_click=lambda e: None),
        ],
        spacing=10,
    )
```

### 3. `ui/main/main_content.py`
```python
from features.reportes.reportes_view import reportes_view

VIEWS_MAP = {
    "home": home_view,
    "reportes": reportes_view,
}
```

### 4. Ejecutar y Probar
```bash
python main.py
```

---

Eso es todo. **¡Así de simple es el sistema!** 🎉

Cualquier duda, revisa la [GUÍA DE INTEGRACIÓN](GUIA_INTEGRACION.md) para más detalles.
