# Guía Rápida para Desarrolladores

Empieza aquí si es tu primer día con el proyecto.

## 1. Estructura Básica en 2 Minutos

```
base_proyectos/
├── main.py                  # Punto de entrada
├── config/                  # Configuración (colores, temas, estilos)
│   └── theme/              # Sistema de tema claro/oscuro
├── ui/                      # Componentes UI
│   ├── buttons/            # MenuButton (botón del menú)
│   ├── header/             # Encabezado
│   ├── footer/             # Pie de página
│   ├── layouts/            # Contenedores (BaseLayout, MenuBarContainer)
│   ├── menu/               # Controlador de navegación
│   └── menu_bar/           # Barra de menú con iconos
├── features/                # Vistas específicas de la app
│   └── home/               # Vista de inicio
└── docs/                    # Documentación
```

## 2. Cómo Ejecutar la App

```bash
# Activar entorno
venv\Scripts\Activate

# Ejecutar
python main.py
```

## 3. Temas Clave

### 3.1 Sistema de Colores Centralizado

**Uso:**
```python
from config.theme.theme import theme

# Acceder a colores
color = theme.colors.PRIMARY
color = theme.colors.TEXT_PRIMARY

# Cambiar tema globalmente
theme.set_mode("light")  # o "dark"
```

### 3.2 Menú Dinámico

**Configuración:**
```python
# ui/menu_bar/menu_config.py
MENU_ITEMS = [
    {"label": "Inicio", "route": "home", "enabled": True},
    {"label": "Clientes", "route": "clientes", "enabled": True},
]
```

Los botones se crean automáticamente desde aquí.

### 3.3 Agregar Nueva Página

**Paso 1:** Crear vista en `features/`
```python
# features/clientes/clientes_view.py
import flet as ft
from config.theme.theme import theme

def clientes_view() -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text("Gestión de Clientes", style=theme.styles.typography.section_title(...)),
            # ... tu contenido
        ]
    )
```

**Paso 2:** Registrar en router
```python
# ui/main/main_content.py
from features.clientes.clientes_view import clientes_view

VIEWS_MAP = {
    "home": home_view,
    "clientes": clientes_view,  # Nuevo
}
```

**Paso 3:** Agregar al menú
```python
# ui/menu_bar/menu_config.py
MENU_ITEMS = [
    {"label": "Inicio", "route": "home"},
    {"label": "Clientes", "route": "clientes"},  # Nuevo
]
```

¡Listo! La navegación es automática.

## 4. Tipografía Semántica

Siempre usa la tipografía correcta:

```python
from config.theme.theme import theme

# Títulos grandes
ft.Text("Mi Título", style=theme.styles.typography.display(color=...))

# Títulos de sección
ft.Text("Sección", style=theme.styles.typography.section_title(color=...))

# Contenido principal
ft.Text("Contenido", style=theme.styles.typography.body(color=...))

# Labels
ft.Text("Label", style=theme.styles.typography.label(color=...))

# Texto pequeño
ft.Text("Mini", style=theme.styles.typography.caption(color=...))
```

## 5. Colores Comunes

```python
from config.theme.theme import theme

# Texto principal
theme.colors.TEXT_PRIMARY

# Texto secundario/muted
theme.colors.TEXT_SECONDARY
theme.colors.TEXT_MUTED

# Color de marca
theme.colors.PRIMARY
theme.colors.PRIMARY_VARIANT

# Fondos
theme.colors.BACKGROUND
theme.colors.SURFACE

# Estados
theme.colors.SUCCESS
theme.colors.WARNING
theme.colors.DANGER
```

## 6. Tema Claro/Oscuro

```python
from config.theme.theme import theme

# Cambiar tema
theme.set_mode("light")   # Claro
theme.set_mode("dark")    # Oscuro

# Obtener modo actual
if theme.mode == "dark":
    print("Modo oscuro")
else:
    print("Modo claro")
```

## 7. Componentes Reutilizables

### MenuButton
```python
from ui.buttons.menu_button import MenuButton

button = MenuButton(
    label="Inicio",
    route="home",
    active_route="home",
    on_navigate=callback,
)
```

### Card Container
```python
from ui.layouts.estilos_container import card_container

card = card_container(content=my_control, height=100)
```

## 8. Debugging

### Ver modo de tema actual
```python
from config.theme.theme import theme
print(f"Tema actual: {theme.mode}")
```

### Ver todos los colores disponibles
```python
from config.theme.theme import theme
import inspect

colors = [attr for attr in dir(theme.colors) if not attr.startswith('_')]
print(colors)
```

### Ver todas las tipografías
```python
from config.theme.theme import theme
import inspect

methods = [m for m in dir(theme.styles.typography) if not m.startswith('_')]
print(methods)  # display, section_title, body, label, caption, button
```

## 9. Errores Comunes

### Error: `AttributeError: 'BaseColors' object has no attribute 'TEXT_VARIANT'`

**Causa:** El color no existe

**Solución:** Usa `TEXT_PRIMARY`, `TEXT_SECONDARY` o `TEXT_MUTED`

### Error: `TypeError: caption() missing 1 required positional argument: 'color'`

**Causa:** Olvidaste pasar el color

**Solución:**
```python
# ❌ Incorrecto
style=theme.styles.typography.caption()

# ✅ Correcto
style=theme.styles.typography.caption(color=theme.colors.TEXT_PRIMARY)
```

### El tema no cambia en mi componente

**Causa:** El componente no se reconstruye

**Solución:** Asegúrate de que tu componente se reconstruya en `_on_theme_change()` en `menu.py`

## 10. Compiling del Proyecto

```bash
# Verificar sintaxis de archivo
python -m py_compile path/to/file.py

# Compiling toda la app
python main.py
```

## 11. Git Workflow

```bash
# Ver cambios
git status

# Agregar cambios
git add .

# Hacer commit
git commit -m "Agregar vista de clientes"

# Pushear a rama desarrollo
git push origin desarrollo
```

## 12. Estructura de un Componente UI

Ejemplo completo:

```python
# features/clientes/clientes_view.py
import flet as ft
from config.theme.theme import theme

def clientes_view() -> ft.Control:
    """Vista de gestión de clientes"""
    
    # Contenido
    content = ft.Column(
        controls=[
            # Título
            ft.Text(
                "Gestión de Clientes",
                style=theme.styles.typography.section_title(
                    color=theme.colors.TEXT_PRIMARY
                ),
            ),
            
            # Contenido
            ft.Container(
                content=ft.Text("Tu contenido aquí"),
                bgcolor=theme.colors.SURFACE,
                padding=20,
                border_radius=8,
            ),
        ],
        spacing=20,
    )
    
    # Envolver en container con padding
    return ft.Container(
        content=content,
        padding=40,
    )
```

## 13. Próximos Pasos

1. **Leer:** `docs/ARQUITECTURA_COMPLETA.md` (20 min)
2. **Entender:** Cómo funciona el flujo de tema en `ui/menu/menu.py`
3. **Practicar:** Crear una nueva vista con 2-3 componentes
4. **Explorar:** Los archivos en `config/theme/` para entender colores y tipografía

## 14. Contacto

- **Email:** dytdigitaliza@gmail.com
- **Versión:** 1.0.0
- **Framework:** Flet 0.80.3

---

**Última actualización:** 15 de febrero de 2026
