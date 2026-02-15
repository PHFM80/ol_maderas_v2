# Guía del Footer y Sistema de Tema

## 1. Componentes del Footer

El footer está dividido en tres secciones: izquierda, centro y derecha.

### 1.1 Footer Izquierdo

**Archivo:** `ui/footer/footer_left.py`

**Contenido:**
- Versión de la aplicación (ej: v1.0.0)
- Tipografía: caption (pequeña)
- Color: TEXT_MUTED

```python
ft.Text(
    "v1.0.0",
    style=theme.styles.typography.caption(color=theme.colors.TEXT_MUTED),
)
```

### 1.2 Footer Centro

**Archivo:** `ui/footer/footer_center.py`

**Contenido:**
- Email de contacto: `dytdigitaliza@gmail.com`
- Teléfono: `+54 9 261 1234 5678`
- Disposición: Columna vertical

```python
ft.Column(
    controls=[
        ft.Text("dytdigitaliza@gmail.com", ...),
        ft.Text("+54 9 261 1234 5678", ...),
    ],
)
```

### 1.3 Footer Derecho

**Archivo:** `ui/footer/footer_right.py`

**Contenido:**
- Nombre de empresa: "D&T"
- Subtítulo: "Desarrollos y Tecnología"
- Logo: `assets/app/logo_32x32.ico`
- Disposición: Row horizontal (texto + logo)

```python
ft.Row(
    controls=[
        ft.Column([
            ft.Text("D&T", ...),
            ft.Text("Desarrollos y Tecnología", ...),
        ]),
        ft.Image(src="assets/app/logo_32x32.ico", width=32, height=32),
    ],
)
```

## 2. Contenedor del Footer

**Archivo:** `ui/layouts/footer_container.py`

### Características

```python
class FooterContainer(ft.Container):
    # Dimensiones
    height = 80  # Altura fija
    padding = ft.padding.symmetric(horizontal=24, vertical=16)
    
    # Estilo
    bgcolor = theme.colors.SURFACE  # Respeta el tema
    border_radius = 0
    
    # Distribución
    Row con 3 columnas:
    - Izquierda: 20%
    - Centro: 60%
    - Derecha: 20%
```

### Distribución Espacial

```
┌─────────────────────────────────────────────────┐
│  v1.0.0      │  email + phone  │  D&T + Logo   │
│   (20%)      │      (60%)      │     (20%)      │
└─────────────────────────────────────────────────┘
              Footer Height: 80px
```

## 3. Sistema de Tema (Dark/Light Mode)

### 3.1 Componente: DarkLightModeButton

**Archivo:** `ui/menu_bar/dark_light_mode.py`

#### Características

```python
class DarkLightModeButton(ft.IconButton):
    # Icono dinámico según el modo
    if theme.mode == "dark":
        icon = ft.Icons.LIGHT_MODE  # 🌞 Sol (cambiar a claro)
    else:
        icon = ft.Icons.DARK_MODE   # 🌙 Luna (cambiar a oscuro)
    
    # Tooltip
    tooltip = "Cambiar tema (claro/oscuro)"
    
    # Callback
    on_click → _on_theme_change(new_mode)
```

#### Ubicación en la UI

```
┌─────────────────────────────────────┐
│  [Botones Menú]      [Sol/Luna 🌙]  │
│  (Navigation)        (Theme Toggle)  │
└─────────────────────────────────────┘
```

El botón está:
- En la barra de menú (MenuBarContainer)
- Alineado a la derecha
- Sin `expand`, ocupa solo el espacio que necesita

### 3.2 ThemeManager

**Archivo:** `config/theme/theme.py`

```python
class ThemeManager:
    def __init__(self, mode: str = "light"):
        self.set_mode(mode)
    
    def set_mode(self, mode: str):
        self.mode = mode
        self.colors = LightColors if mode == "light" else DarkColors
        self.styles = AppStyles(self.colors)

# Instancia global
theme = ThemeManager("dark")  # Inicia en modo oscuro
```

#### Uso Global

```python
# En cualquier parte del código
from config.theme.theme import theme

# Cambiar tema
theme.set_mode("light")

# Acceder a colores
color = theme.colors.PRIMARY
color = theme.colors.TEXT_PRIMARY

# Acceder a estilos
style = theme.styles.typography.label(color=theme.colors.TEXT_PRIMARY)
```

### 3.3 Paletas de Color

#### Modo Oscuro (`config/theme/dark.py`)

```python
PRIMARY: str = "#1E88E5"          # Azul
PRIMARY_VARIANT: str = "#1565C0"  # Azul más oscuro
BACKGROUND: str = "#121212"       # Negro
SURFACE: str = "#1E1E1E"          # Gris oscuro
TEXT_PRIMARY: str = "#FFFFFF"     # Blanco
TEXT_SECONDARY: str = "#B3B3B3"   # Gris claro
TEXT_MUTED: str = "#757575"       # Gris
```

#### Modo Claro (`config/theme/light.py`)

```python
PRIMARY: str = "#1E88E5"          # Azul
PRIMARY_VARIANT: str = "#1565C0"  # Azul más oscuro
BACKGROUND: str = "#FFFFFF"       # Blanco
SURFACE: str = "#F5F5F5"          # Gris muy claro
TEXT_PRIMARY: str = "#212121"     # Negro
TEXT_SECONDARY: str = "#666666"   # Gris medio
TEXT_MUTED: str = "#999999"       # Gris
```

### 3.4 Flujo de Cambio de Tema

#### Paso 1: Usuario Hace Click

```python
# En DarkLightModeButton
def _on_click(self, e):
    new_mode = "light" if theme.mode == "dark" else "dark"
    theme.set_mode(new_mode)  # Cambia globalmente
    self._update_icon()        # Actualiza icono
    self.update()              # Redibuja el botón
    
    if self.on_theme_change:
        self.on_theme_change(new_mode)  # Callback
```

#### Paso 2: Callback _on_theme_change

```python
# En ui/menu/menu.py
def _on_theme_change(new_mode: str):
    global _current_route, _menu_buttons, _main_container, _page, _base_layout
    
    # 1. Reconstruir Header
    new_header = HeaderContainer(...)
    
    # 2. Reconstruir MenuBar
    new_menu_bar = MenuBarContainer(...)
    
    # 3. Reconstruir MainContent
    new_main_content = build_main_content(_current_route)
    _main_container.content = new_main_content
    
    # 4. Reconstruir Footer
    new_footer = FooterContainer(...)
    
    # 5. Actualizar Layout
    _base_layout.bgcolor = theme.colors.BACKGROUND
    _base_layout.content = ft.Column([
        header,
        menu_bar,
        main,
        footer,
    ])
    
    # 6. Refrescar UI
    _page.update()
```

#### Paso 3: Actualización Visual

- Todos los componentes leen del `theme` global
- Se reconstruyen con los nuevos colores
- `page.update()` refresca la UI

### 3.5 Por Qué Funciona

1. **Theme es global:** Una instancia única en `config/theme/theme.py`
2. **Cambio centralizado:** Solo llamar `theme.set_mode()`
3. **Lectura automática:** Los componentes siempre leen `theme.colors`
4. **Reconstrucción:** Al reconstruir, leen los nuevos valores
5. **Actualización:** `page.update()` refresca toda la UI

### 3.6 Componentes que Responden al Tema

| Componente | Qué Cambia | Ubicación |
|-----------|-----------|-----------|
| HeaderContainer | `bgcolor` | Encabezado |
| MenuBarContainer | `bgcolor` botones | Barra de menú |
| MenuButton | Color texto, fondo | Botones del menú |
| MainContent | Colores texto, fondos | Área principal |
| FooterContainer | `bgcolor` | Pie de página |
| DarkLightModeButton | Icono | Botón tema |

## 4. Ejemplo: Crear Footer Personalizado

### Caso: Agregar Redes Sociales

**Archivo:** `ui/footer/footer_social.py`

```python
import flet as ft
from config.theme.theme import theme

def build_footer_social() -> ft.Control:
    """Botones de redes sociales"""
    return ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.FACEBOOK,
                tooltip="Facebook",
                on_click=lambda e: print("Facebook"),
            ),
            ft.IconButton(
                icon=ft.Icons.LINKED_IN,
                tooltip="LinkedIn",
                on_click=lambda e: print("LinkedIn"),
            ),
        ],
        spacing=8,
    )
```

**Actualizar:** `ui/footer/footer_content.py`

```python
from ui.footer.footer_social import build_footer_social

def build_footer_content():
    return {
        "left": build_footer_left(),
        "center": build_footer_center(),
        "right": build_footer_right(),
        "social": build_footer_social(),  # Nuevo
    }
```

## 5. Checklist: Verificar Que Todo Respeta el Tema

- [ ] ¿Todos los textos usan `theme.colors.TEXT_*`?
- [ ] ¿Todos los fondos usan `theme.colors.BACKGROUND` o `SURFACE`?
- [ ] ¿Todos los estilos de tipografía pasan `color=theme.colors.*`?
- [ ] ¿El componente se reconstruye cuando cambia el tema?
- [ ] ¿Se actualiza la UI con `page.update()` o `component.update()`?

## 6. Solución de Problemas

### El tema no cambia en mi componente

**Causa:** El componente no se está reconstruyendo

**Solución:** Asegúrate de que en `_on_theme_change()` reconstruyas el componente

### El color es incorrecto

**Causa:** Estás usando un color literario (ej: `"#FF0000"`) en lugar de `theme.colors.*`

**Solución:** Cambia a `theme.colors.PRIMARY`

### El icono del botón no cambia

**Causa:** Falta llamar `self._update_icon()` después de `theme.set_mode()`

**Solución:** Sigue el patrón en `DarkLightModeButton._on_click()`

---

**Última actualización:** 15 de febrero de 2026
**Versión:** 1.0.0
