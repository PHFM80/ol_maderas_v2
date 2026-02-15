# Arquitectura Completa de la Aplicación

## 1. Visión General

Este proyecto es una aplicación de escritorio Flet que implementa un sistema **modular, escalable y mantenible** con:

- ✅ Sistema de temas (claro/oscuro) completamente funcional
- ✅ Navegación dinámica basada en menú configurable
- ✅ Componentes UI reutilizables y profesionales
- ✅ Gestión centralizada de estilos y colores
- ✅ Arquitectura de capas clara

## 2. Estructura de Capas

```
┌─────────────────────────────────────────┐
│         PRESENTATION LAYER              │
│  (UI Components, Views, Layouts)        │
├─────────────────────────────────────────┤
│         APPLICATION LAYER               │
│  (Menu, Navigation, Theme Manager)      │
├─────────────────────────────────────────┤
│         CONFIGURATION LAYER             │
│  (Theme, Colors, Typography, Config)    │
├─────────────────────────────────────────┤
│         DATA LAYER (Future)             │
│  (Database, Repositories, Services)     │
└─────────────────────────────────────────┘
```

### 2.1 Presentation Layer

**Responsabilidad:** Renderizar componentes visuales

**Componentes principales:**
- `ui/buttons/` - Botones reutilizables (MenuButton)
- `ui/header/` - Encabezado de la app
- `ui/menu/` - Controlador de menú y navegación
- `ui/menu_bar/` - Barra de navegación y acciones
- `ui/footer/` - Pie de página con información
- `ui/layouts/` - Contenedores y layouts (BaseLayout, MenuBarContainer, etc.)
- `ui/main/` - Router de vistas principales
- `features/` - Vistas específicas (home, clientes, reportes, etc.)

### 2.2 Application Layer

**Responsabilidad:** Lógica de negocio y coordinación

**Archivos clave:**
- `ui/menu/menu.py` - Controlador central (navigation, theme changes)
- `ui/menu_bar/navigation.py` - Constructor dinámico de botones de menú
- `ui/menu_bar/dark_light_mode.py` - Toggle de tema
- `ui/main/main_content.py` - Router de vistas

### 2.3 Configuration Layer

**Responsabilidad:** Centralizar configuración, estilos y temas

**Estructura:**
```
config/
├── app_config.py           # Configuración global (alturas, tamaños)
├── theme/
│   ├── __init__.py
│   ├── theme.py            # ThemeManager (alternador claro/oscuro)
│   ├── light.py            # Paleta de colores claros
│   ├── dark.py             # Paleta de colores oscuros
│   ├── colors.py           # BaseColors (estructura)
│   ├── styles.py           # Estilos reutilizables (card, input)
│   └── typography.py       # Sistema de tipografía
```

### 2.4 Data Layer (Future)

Cuando se implemente, la estructura será:
```
data/
├── database/
├── migrations/
└── repositories/
```

## 3. Flujo de Arquitectura

### 3.1 Inicio de la Aplicación

```
main.py
  └─> main() [async]
      └─> show_menu(page, view_name="home")
          ├─> HeaderContainer
          ├─> MenuBarContainer
          │   ├─> build_menu_navigation() [MENU_ITEMS dinámico]
          │   └─> DarkLightModeButton
          ├─> MainContainer [build_main_content()]
          └─> FooterContainer
```

### 3.2 Flujo de Navegación

```
MenuButton.click()
  └─> _on_navigate(route)
      ├─> Actualizar _current_route
      ├─> button.set_active() para todos los botones
      └─> _main_container.content = build_main_content(route)
```

### 3.3 Flujo de Cambio de Tema

```
DarkLightModeButton.click()
  └─> theme.set_mode("light" | "dark")
      └─> _on_theme_change(mode)
          ├─> Reconstruir Header
          ├─> Reconstruir MenuBar (con nuevo botón)
          ├─> Reconstruir MainContent
          ├─> Reconstruir Footer
          └─> page.update() [Refrescar UI]
```

## 4. Componentes Principales

### 4.1 MenuButton

**Archivo:** `ui/buttons/menu_button.py`

**Características:**
- Botón rectangular compacto (40px alto)
- Muestra solo texto del menú
- Estado activo/inactivo visual (color PRIMARY_VARIANT cuando está activo)
- Responde a callbacks `on_navigate`

**Uso:**
```python
button = MenuButton(
    label="Inicio",
    route="home",
    active_route="home",
    on_navigate=callback_func
)
```

### 4.2 DarkLightModeButton

**Archivo:** `ui/menu_bar/dark_light_mode.py`

**Características:**
- IconButton con iconos sol/luna
- Alterna tema automáticamente
- Ejecuta callback cuando cambia el tema

**Flujo:**
```
Click → theme.set_mode() → _on_theme_change() → Reconstruir todo
```

### 4.3 ThemeManager

**Archivo:** `config/theme/theme.py`

**Características:**
- Singleton global
- Gestiona colores y tipografía según el modo
- `theme.set_mode("light" | "dark")`
- `theme.colors` → acceso a paleta actual
- `theme.styles` → acceso a estilos reutilizables

### 4.4 Configuración de Menú (MENU_ITEMS)

**Archivo:** `ui/menu_bar/menu_config.py`

**Estructura:**
```python
MENU_ITEMS = [
    {
        "label": "Inicio",
        "route": "home",
        "icon": "home",  # Opcional
        "enabled": True,
    },
    # ... más items
]
```

**Nota:** Los botones se crean dinámicamente desde esta configuración.

### 4.5 Router de Vistas

**Archivo:** `ui/main/main_content.py`

**Estructura:**
```python
VIEWS_MAP = {
    "home": home_view,
    "clientes": clientes_view,  # (cuando se implemente)
    # ...
}

def build_main_content(route):
    view_builder = VIEWS_MAP.get(route, home_view)
    return view_builder()
```

## 5. Sistema de Colores y Tipografía

### 5.1 Paleta de Colores

**Colores disponibles** (`theme.colors`):
- `PRIMARY` - Color principal de marca
- `PRIMARY_VARIANT` - Variante del principal (usado para estado activo)
- `ACCENT` - Color de énfasis
- `BACKGROUND` - Fondo general
- `SURFACE` - Superficie de componentes
- `TEXT_PRIMARY` - Texto principal
- `TEXT_SECONDARY` - Texto secundario
- `TEXT_MUTED` - Texto deshabilitado/muted
- `TEXT_ON_PRIMARY` - Texto sobre fondo primario
- `SUCCESS`, `WARNING`, `INFO`, `DANGER` - Estados

### 5.2 Tipografía

**Estilos disponibles** (`theme.styles.typography`):
- `display(color)` - Títulos grandes (32px, bold)
- `section_title(color)` - Títulos de sección (18px, w_600)
- `body(color)` - Contenido principal (16px)
- `label(color)` - Labels e info secundaria (14px, w_500)
- `caption(color)` - Micro-info, versión (12px)
- `button(color)` - Texto de botones (14px, bold)

### 5.3 Ejemplo de Uso

```python
from config.theme.theme import theme

# Usar color
text = ft.Text(
    "Hola",
    color=theme.colors.TEXT_PRIMARY
)

# Usar tipografía
text = ft.Text(
    "Título",
    style=theme.styles.typography.section_title(
        color=theme.colors.PRIMARY
    )
)
```

## 6. Añadir Nuevas Vistas

### Paso 1: Crear archivo de vista

`features/clientes/clientes_view.py`:
```python
import flet as ft
from config.theme.theme import theme

def clientes_view() -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text(
                "Gestión de Clientes",
                style=theme.styles.typography.section_title(
                    color=theme.colors.TEXT_PRIMARY
                ),
            ),
            # ... contenido
        ],
        padding=40,
    )
```

### Paso 2: Registrar en el router

`ui/main/main_content.py`:
```python
from features.clientes.clientes_view import clientes_view

VIEWS_MAP = {
    "home": home_view,
    "clientes": clientes_view,
}
```

### Paso 3: Agregar a MENU_ITEMS

`ui/menu_bar/menu_config.py`:
```python
MENU_ITEMS = [
    {
        "label": "Inicio",
        "route": "home",
        "enabled": True,
    },
    {
        "label": "Clientes",
        "route": "clientes",
        "enabled": True,
    },
]
```

## 7. Patrones de Diseño Utilizados

| Patrón | Ubicación | Propósito |
|--------|-----------|----------|
| **Singleton** | `theme` | Una única instancia global del gestor de temas |
| **Factory** | `build_menu_navigation()` | Crear botones dinámicamente |
| **Registry** | `VIEWS_MAP` | Mapear rutas a vistas |
| **Strategy** | Callbacks `on_navigate` | Inyectar comportamiento en componentes |
| **Component** | `MenuButton`, `FooterContainer` | Reutilizar componentes |
| **State Management** | Variables globales en `menu.py` | Mantener estado de la app |

## 8. Flujo de Actualización de Tema

### Paso a Paso

1. **Usuario hace click** en el botón de tema
2. **DarkLightModeButton._on_click()** se ejecuta
3. **theme.set_mode()** cambia el modo globalmente
4. **_on_theme_change()** en menu.py se dispara (callback)
5. Se reconstruyen todos los componentes:
   - HeaderContainer (nuevo color de fondo)
   - MenuBarContainer (nuevo botón con icono actualizado)
   - MainContent (nueva vista con colores nuevos)
   - FooterContainer (nuevos colores)
6. **page.update()** refresca la UI completamente

### Por qué funciona

- El `theme` es global (`config/theme/theme.py`)
- Todos los componentes leen de `theme.colors` y `theme.styles`
- Cuando cambia `theme.mode`, todos los accesos futuros leen los nuevos valores
- Reconstruir los componentes los "redibuja" con los nuevos colores

## 9. Configuración Global

**Archivo:** `config/app_config.py`

Contiene:
```python
WINDOW_HEIGHT = 900
WINDOW_WIDTH = 1200
HEADER_HEIGHT = 80
MENU_HEIGHT = 80
MAIN_HEIGHT = 560
FOOTER_HEIGHT = 80
```

## 10. Próximas Mejoras

- [ ] Autenticación y gestión de usuarios
- [ ] Base de datos (SQLite o PostgreSQL)
- [ ] Capa de servicios/APIs
- [ ] Validación de formularios
- [ ] Notificaciones/Toast
- [ ] Exportación a PDF/Excel
- [ ] Multiidioma
- [ ] Persistencia de preferencias (tema favorito, etc.)

## 11. Recursos y Referencias

- **Flet Documentation:** https://flet.dev
- **Patrón MVC/MVP:** Aplicable a features/
- **Gestión de Estado:** Variables globales + callbacks

---

**Última actualización:** 15 de febrero de 2026
**Versión:** 1.0.0
