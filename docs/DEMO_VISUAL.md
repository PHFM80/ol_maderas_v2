# 🎨 DEMOSTRACIÓN VISUAL - SISTEMA DE BOTÓN DE MENÚ

## 🎬 Cómo Se Ve en Acción

### Estado Inicial (Vista "home")

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  🏢 Desarrollos y Tecnología    Mi App de Gestión   │
│                     D&T                             │
│                         Empresa ficticia             │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  [🏠 Inicio]  [👥 Clientes]  [📊 Reportes]        ⚙️ │
│      ↑                                             │
│      Botón Activo (PRIMARY_VARIANT)               │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│              Bienvenido al menú                     │
│              Seleccioná una opción en el menú      │
│              para continuar.                        │
│                                                     │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  v1.0.0    contacto@dyt.com +54 9 261 1234 5678   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Después de Clickear "Clientes"

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  🏢 Desarrollos y Tecnología    Mi App de Gestión   │
│                     D&T                             │
│                         Empresa ficticia             │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  [🏠 Inicio]  [👥 Clientes]  [📊 Reportes]        ⚙️ │
│                    ↑                               │
│              Botón Activo Cambió                   │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│              👥 Gestión de Clientes                │
│                                                     │
│              [Generar Reporte]                     │
│                                                     │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  v1.0.0    contacto@dyt.com +54 9 261 1234 5678   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 🎯 Zoom en el Menú

### MenuButton Inactivo

```
┌───────────────────┐
│  👥 Clientes      │  Fondo: transparent
│                   │  Texto: TEXT_PRIMARY (#1A202C light, #F8FAFC dark)
│                   │  Borde: transparent
└───────────────────┘
Padding: 12px (interno)
Altura: 50px
Border Radius: 12px
```

### MenuButton Activo

```
┌═══════════════════┐
║  🏠 Inicio        ║  Fondo: PRIMARY_VARIANT (#4591B8 light, #3498DB dark)
║                   ║  Texto: TEXT_ON_PRIMARY (blanco)
║                   ║  Borde: PRIMARY (2px)
└═══════════════════┘
Padding: 12px (interno)
Altura: 50px
Border Radius: 12px
Sombra: SHADOW_SM
```

---

## 📊 Flujo Interactivo

### Escenario 1: Usuario navega por menú

```
[Usuario ve Inicio resaltado]
            │
            ├─→ Clickea "Clientes"
            │       │
            │       └─→ MenuButton.on_click()
            │           └─→ _on_navigate("clientes")
            │               ├─ Actualiza _current_route
            │               ├─ Itera todos los botones
            │               │  ├─ Inicio: set_active("clientes") → inactivo
            │               │  └─ Clientes: set_active("clientes") → activo
            │               └─ Cambia main_container.content
            │                   └─ Nueva vista de clientes
            │
            └─→ Pantalla actualizada [Clientes resaltado]
```

### Escenario 2: Usuario agrega botón nuevo

```
[Developer abre menu_config.py]
            │
            └─→ Descomenta "Reportes"
                    │
                    └─→ Abre el archivo
                        │
                        └─→ MenuButton aparece automáticamente
                            │
                            └─→ Clickea "Reportes"
                                │
                                └─→ build_main_content("reportes")
                                    │
                                    └─→ VIEWS_MAP["reportes"]()
                                        │
                                        └─→ reportes_view() renderiza
                                            │
                                            └─→ Vista de reportes aparece
```

---

## 🔄 Componentes en Acción

### MenuButton Instance

```python
# Creación (en build_menu_navigation)
MenuButton(
    label="Clientes",
    route="clientes",
    icon="people",
    active_route="home",          # Viene desde _current_route
    on_navigate=_on_navigate,      # Callback a menu.py
)

# Resultado visual
┌────────────────────┐
│  👥 Clientes       │  ← Inactivo (gris)
└────────────────────┘
```

### Después de Navegación

```python
# En _on_navigate() de menu.py
button.set_active("clientes")

# Resultado visual
┌════════════════════┐
║  👥 Clientes       ║  ← Activo (azul)
└════════════════════┘
```

---

## 🎨 Temas Aplicados

### Tema LIGHT (Defecto)

```
MenuButton Inactivo:
┌─────────────────────────────┐
│  🏠 Inicio                  │
│  Fondo: #FFFFFF             │
│  Texto: #1A202C (gris oscuro)
│  Borde: transparent         │
└─────────────────────────────┘

MenuButton Activo:
┌═════════════════════════════┐
║  🏠 Inicio                  ║
║  Fondo: #4591B8 (azul)      ║
║  Texto: #FFFFFF (blanco)    ║
║  Borde: #1487B8 (azul oscuro)║
└═════════════════════════════┘
```

### Tema DARK

```
MenuButton Inactivo:
┌─────────────────────────────┐
│  🏠 Inicio                  │
│  Fondo: transparent         │
│  Texto: #F8FAFC (gris claro)│
│  Borde: transparent         │
└─────────────────────────────┘

MenuButton Activo:
┌═════════════════════════════┐
║  🏠 Inicio                  ║
║  Fondo: #3498DB (azul)      ║
║  Texto: #0F172A (blanco)    ║
║  Borde: #5DADE2 (azul claro)║
└═════════════════════════════┘
```

---

## 📈 Progresión: De Pocos a Muchos Botones

### Inicial (1 botón)

```
Menu Bar:
┌─────────────────────────────────────┐
│  [🏠 Inicio]                    ⚙️  │
└─────────────────────────────────────┘
```

### Con 3 Botones

```
Menu Bar:
┌──────────────────────────────────────────────────────┐
│  [🏠 Inicio]  [👥 Clientes]  [📊 Reportes]       ⚙️  │
└──────────────────────────────────────────────────────┘
```

### Con 6 Botones (Scroll si es necesario)

```
Menu Bar (con spacing de 12px entre botones):
┌────────────────────────────────────────────────────────────────┐
│  [🏠 Inicio] [👥 Clientes] [📊 Reportes] [⚙️ Config]         ⚙️  │
│  [📁 Archivos] [💬 Chat]                                        │
└────────────────────────────────────────────────────────────────┘
```

---

## 🔍 Detalle Técnico: Renderizado

### Primero: Construcción

```
1. menu.py: show_menu()
   └─ build_menu_bar_content(active_route="home", on_navigate=_on_navigate)
       └─ build_menu_navigation(active_route="home", on_navigate)
           └─ Para cada item en MENU_ITEMS:
               └─ MenuButton(...)
                   └─ self._build()
                       └─ ft.Row([icon, text])
```

### Luego: Renderizado

```
2. UI renderiza MenuButton
   ├─ Aplica height=50px
   ├─ Aplica padding=12px
   ├─ Aplica border_radius=12px
   ├─ Aplica bgcolor (si es activo)
   └─ Renderiza Row con icon + text
```

### Finalmente: Interacción

```
3. Usuario clickea
   └─ MenuButton._on_click()
       └─ self.on_navigate("clientes")
           └─ menu.py: _on_navigate("clientes")
               ├─ _current_route = "clientes"
               ├─ Para cada botón:
               │   └─ button.set_active("clientes")
               │       ├─ Actualiza self.is_active
               │       ├─ Actualiza self.bgcolor
               │       ├─ Actualiza colores de texto
               │       └─ self.update()
               └─ Actualiza main_container.content
```

---

## 📝 Código en Acción

### Crear un MenuButton

```python
from ui.buttons.menu_button import MenuButton

# Instancia
btn = MenuButton(
    label="Inicio",
    route="home",
    icon="home",
    active_route="home",  # ← Indica que está activo
    on_navigate=lambda route: print(f"Navega a {route}")
)

# Resultado
btn.height  # 50
btn.is_active  # True
btn.bgcolor  # PRIMARY_VARIANT (azul)
```

### Cambiar Estado

```python
# Usuario navega a otra ruta
btn.set_active("clientes")

# Cambios automáticos
btn.is_active  # False
btn.bgcolor  # transparent
btn.content  # Colores actualizados
btn.update()  # Renderiza cambios
```

---

## 🎯 Casos de Uso

### Caso 1: App Simple (1 módulo)

```
MENU_ITEMS = [
    {"label": "Inicio", "route": "home", "icon": "home"},
]

Resultado:
[🏠 Inicio]  ← Un botón, simple y limpio
```

### Caso 2: App Pequeña (3 módulos)

```
MENU_ITEMS = [
    {"label": "Inicio", "route": "home", "icon": "home"},
    {"label": "Clientes", "route": "clientes", "icon": "people"},
    {"label": "Config", "route": "config", "icon": "settings"},
]

Resultado:
[🏠 Inicio]  [👥 Clientes]  [⚙️ Config]
```

### Caso 3: App Grande (10+ módulos)

```
MENU_ITEMS = [
    {"label": "Inicio", "route": "home", "icon": "home"},
    {"label": "Clientes", "route": "clientes", "icon": "people"},
    {"label": "Productos", "route": "productos", "icon": "shopping_bag"},
    {"label": "Ventas", "route": "ventas", "icon": "attach_money"},
    {"label": "Reportes", "route": "reportes", "icon": "bar_chart"},
    {"label": "Usuarios", "route": "usuarios", "icon": "admin_panel_settings"},
    {"label": "Roles", "route": "roles", "icon": "security"},
    {"label": "Auditoria", "route": "auditoria", "icon": "history"},
    {"label": "Config", "route": "config", "icon": "settings"},
    {"label": "Ayuda", "route": "ayuda", "icon": "help"},
]

Resultado (auto-ajustable):
[🏠 Inicio] [👥 Clientes] [🛍️ Productos] [💵 Ventas] [📊 Reportes] 
[👤 Usuarios] [🔐 Roles] [📜 Auditoria] [⚙️ Config] [❓ Ayuda]
```

---

## 🌈 Personalización Visual

### Cambiar Color de Activo

**Antes:**
```python
bgcolor = PRIMARY_VARIANT  # Azul
```

**Después:**
```python
bgcolor = ACCENT  # Verde
```

**Resultado:**
```
MenuButton Activo con color ACCENT:
┌════════════════════┐
║  👥 Clientes       ║  ← Verde (#02ADB0)
└════════════════════┘
```

### Cambiar Tamaño del Botón

**Antes:**
```python
self.height = 50  # 50px
```

**Después:**
```python
self.height = 60  # 60px
```

**Resultado:**
```
Menu Bar con botones más grandes:
┌────────────────────────────────────┐
│                                    │
│  [🏠 Inicio]  [👥 Clientes]       │
│                                    │
└────────────────────────────────────┘
```

---

## ✨ Animaciones Potenciales (Futuro)

Si agregan animaciones:

```python
# Hover effect
def _on_hover(self, e):
    if e.data == "true":
        self.shadow = SHADOW_LG  # Sombra grande
    else:
        self.shadow = SHADOW_SM  # Sombra pequeña
    self.update()

# Click effect
def _on_click(self, e):
    # Animación de click
    self.scale = 0.95
    self.update()
    # ... callback ...
    # Volver a normal
    self.scale = 1.0
    self.update()
```

**Resultado visual:**
```
Hover: Sombra más pronunciada
┌─────────────────────┐
│  👥 Clientes        │  ← Efecto de profundidad
└─────────────────────┘

Click: Botón se empequeñece y vuelve
[Se presiona levemente]  →  [Vuelve a normal]
```

---

Así se ve en acción el sistema. **Simple, limpio, profesional.** 🎉
