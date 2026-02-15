# COMPONENTE: BOTÓN DE MENÚ REUTILIZABLE
## Implementación completada

### 📁 Estructura creada:

```
ui/
├── buttons/
│   ├── __init__.py (nuevo)
│   └── menu_button.py (nuevo) ← COMPONENTE GENÉRICO DEL BOTÓN
├── menu_bar/
│   ├── menu_config.py (nuevo) ← CONFIGURACIÓN DE ITEMS
│   ├── navigation.py (actualizado) ← RENDERIZADOR DINÁMICO
│   └── menu_bar_content.py (actualizado)
├── main/
│   └── main_content.py (actualizado) ← GESTOR DE VISTAS
└── menu/
    └── menu.py (actualizado) ← CONTROLADOR DE NAVEGACIÓN

features/
└── home/
    └── home_view.py (sin cambios)
```

---

### 🎛️ ComponenteSistema

**MenuButton** (`ui/buttons/menu_button.py`):
- Botón genérico reutilizable
- Parámetros: `label`, `route`, `icon`, `active_route`, `on_navigate`
- Respeta paleta de colores (theme claro/oscuro)
- Estado activo visible (fondo PRIMARY_VARIANT + borde PRIMARY)
- Soporta icono + texto o solo texto

**Configuración** (`ui/menu_bar/menu_config.py`):
```python
MENU_ITEMS = [
    {"label": "Inicio", "route": "home", "icon": "home", "enabled": True},
    # Agregar más items según cliente
]
```

---

### 🔄 Flujo de Navegación

```
menu.py (main handler)
    ↓
    ├─ _on_navigate(route) ← Cuando clickeas un botón
    │   ├─ Actualiza _current_route
    │   ├─ Llama button.set_active() para todos los botones
    │   └─ Actualiza contenido en main_container
    │
    └─ show_menu() ← Initializa
        ├─ Llama build_menu_bar_content()
        │   ├─ Llama build_menu_navigation()
        │   │   └─ Crea MenuButtons dinámicos desde MENU_ITEMS
        │   └─ Retorna lista de botones + handler
        │
        └─ Pasa _on_navigate como callback a los botones
```

---

### ✨ Características

✅ **Reutilizable**: Un solo componente MenuButton para todos los botones
✅ **Configurable**: Items definidos en MENU_ITEMS (separación de responsabilidades)
✅ **Estado Activo**: Botón resaltado indica dónde está el usuario
✅ **Dinámico**: Soporta icono + texto, solo texto, o solo icono
✅ **Tema Integrado**: Responde automáticamente a claro/oscuro
✅ **Escalable**: Agregar botones = agregar item en MENU_ITEMS
✅ **Limpio**: Arquitectura sin lógica mezclada

---

### 🚀 Cómo usar

**Agregar un nuevo botón de menú:**

1. Abre `ui/menu_bar/menu_config.py`
2. Descomenta o agrega un nuevo item:
```python
{
    "label": "Clientes",
    "route": "clientes",
    "icon": "people",
    "enabled": True,
}
```

3. Crea la vista en `features/clientes/clientes_view.py`
4. Registra en `ui/main/main_content.py`:
```python
from features.clientes.clientes_view import clientes_view

VIEWS_MAP = {
    "home": home_view,
    "clientes": clientes_view,  # ← Agregar aquí
}
```

¡Listo! El botón aparecerá en el menú automáticamente.

---

### 🎨 Ejemplo Visual

Con tema LIGHT y botón "Inicio" activo:
```
┌─────────────────────────────────┐
│ [Inicio*]  [Clientes]  [Reportes] │
│  ^^^^^^                          │
│  Resaltado (PRIMARY_VARIANT)    │
└─────────────────────────────────┘

*Con icono + texto o solo texto según config
```

---

### 📝 Próximas mejoras (opcional)

- [ ] Agregar transiciones/animaciones en cambio de vista
- [ ] Sistema de permisos (mostrar/ocultar botones por rol)
- [ ] Breadcrumb dinámico en header
- [ ] Animación hover en botones (cambio de sombra)
- [ ] Integración con API para cargar MENU_ITEMS dinámicamente
