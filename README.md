# 🎨 Base Proyectos - Flet

Aplicación de escritorio moderna construida con **Flet** (framework Python para crear UIs).

## 🚀 Inicio Rápido

```bash
# 1. Activar entorno virtual
venv\Scripts\Activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar la app
python main.py
```

---

## 📚 Documentación

Toda la documentación está en la carpeta [`docs/`](docs/):

### 🎯 Empieza Aquí
- **[docs/GUIA_RAPIDA_DESARROLLADORES.md](docs/GUIA_RAPIDA_DESARROLLADORES.md)** ⭐ **Para desarrolladores - EMPIEZA AQUÍ** (10 min)
- **[docs/00_LEEME_PRIMERO.md](docs/00_LEEME_PRIMERO.md)** - Punto de entrada principal
- **[docs/QUICK_START.md](docs/QUICK_START.md)** - Guía rápida (5 minutos)

### 📖 Documentación Técnica
- **[docs/ARQUITECTURA_COMPLETA.md](docs/ARQUITECTURA_COMPLETA.md)** - Arquitectura y diseño del proyecto
- **[docs/FOOTER_Y_TEMA.md](docs/FOOTER_Y_TEMA.md)** - Footer, colores y sistema de tema claro/oscuro
- **[docs/README_MENU_BUTTON.md](docs/README_MENU_BUTTON.md)** - Resumen del botón de menú
- **[docs/DOCUMENTO_MENU_BUTTON.md](docs/DOCUMENTO_MENU_BUTTON.md)** - Referencia técnica detallada
- **[docs/GUIA_INTEGRACION.md](docs/GUIA_INTEGRACION.md)** - Cómo funciona la integración

### 🔍 Índices y Referencias
- **[docs/INDICE_DOCUMENTACION_COMPLETO.md](docs/INDICE_DOCUMENTACION_COMPLETO.md)** - Índice completo con rutas de aprendizaje
- **[docs/LISTADO_ARCHIVOS.md](docs/LISTADO_ARCHIVOS.md)** - Estructura de carpetas y archivos

### 📊 Sumarios
- **[docs/ESTRUCTURA_ANTES_DESPUES.md](docs/ESTRUCTURA_ANTES_DESPUES.md)** - Cambios detallados
- **[docs/DEMO_VISUAL.md](docs/DEMO_VISUAL.md)** - Ejemplos visuales
- **[docs/RESUMEN_EJECUTIVO.md](docs/RESUMEN_EJECUTIVO.md)** - Para clientes/Project Managers
- **[docs/RESUMEN_COMPLETO.md](docs/RESUMEN_COMPLETO.md)** - Resumen técnico completo

---

## 🎨 Características Completadas

### ✅ Sistema de Botón de Menú
- Botón genérico y reutilizable (`MenuButton`)
- Configuración centralizada (`MENU_ITEMS`)
- Estado activo visible (color PRIMARY_VARIANT)
- Escala a ilimitados botones
- Integración con router dinámico

### ✅ Sistema de Navegación
- Navegación dinámica basada en menú
- Router de vistas (`VIEWS_MAP`)
- Vista de inicio completamente funcional
- Callbacks para actualizar estado

### ✅ Sistema de Tema (Dark/Light Mode)
- Alternador de tema completamente funcional
- Botón de tema en la barra de menú
- Cambio instantáneo de toda la UI
- Colores centralizados (`theme.colors`)
- Tipografía semántica (`theme.styles.typography`)
- Soporte para luz y oscuro

### ✅ Componentes UI
- **Header:** Encabezado profesional con tema
- **Footer:** Footer con 3 secciones (versión, contacto, logo)
- **Menu Bar:** Barra de navegación + botón de tema
- **Menu Button:** Botón rectangular compacto del menú
- **Main Container:** Área principal para vistas

### ✅ Arquitectura
- Separación de capas (Presentation, Application, Configuration)
- Patrón Singleton para Theme Manager
- Factory pattern para botones dinámicos
- Registry pattern para vistas
- Reutilización de componentes

### Interfaz
- ✅ Header con logo y nombre
- ✅ Menú de navegación dinámico
- ✅ Contenido principal (vistas)
- ✅ Footer con información
- ✅ Sistema de temas (light/dark)

---

## 📁 Estructura del Proyecto

```
base_proyectos/
├── main.py                    ← Punto de entrada
├── requirements.txt           ← Dependencias
├── README.md                  ← Este archivo
│
├── docs/                      ← 📚 DOCUMENTACIÓN
│   ├── 00_LEEME_PRIMERO.md
│   ├── QUICK_START.md
│   ├── README_MENU_BUTTON.md
│   └── ... más guías
│
├── config/                    ← Configuración
│   ├── app_config.py
│   └── theme/
│       ├── theme.py
│       ├── colors.py
│       ├── typography.py
│       └── styles.py
│
├── ui/                        ← Componentes UI
│   ├── buttons/
│   │   └── menu_button.py    ← 🆕 Botón reutilizable
│   ├── menu_bar/
│   │   ├── menu_config.py    ← 🆕 Configuración items
│   │   └── navigation.py
│   ├── header/
│   ├── footer/
│   ├── layouts/
│   └── menu/
│
├── features/                  ← Vistas/Funcionalidades
│   └── home/
│       └── home_view.py
│
├── documentacion/             ← Documentación del proyecto
├── data/                      ← Base de datos
└── services/                  ← Lógica de negocio
```

---

## 🎯 Próximos Pasos

### 1. Verifica que funciona
```bash
python main.py
```

### 2. Lee la documentación
Comienza con: [`docs/QUICK_START.md`](docs/QUICK_START.md)

### 3. Agrega tus botones
Sigue los 3 pasos en [`docs/QUICK_START.md`](docs/QUICK_START.md)

---

## 🛠️ Requisitos

- Python 3.8+
- Flet 0.80.3
- FastAPI (para futuro backend)

---

## 📝 Sobre Este Proyecto

Este es un proyecto base profesional para aplicaciones de escritorio con Flet, incluyendo:
- Sistema de tema completo (claro/oscuro)
- Arquitectura modular y escalable
- Componentes reutilizables
- Documentación completa

---

## 📞 Documentación Completa

Necesitas más detalles? Tenemos **13 guías de documentación** en la carpeta `docs/`:

| Guía | Tiempo | Para Quién |
|------|--------|-----------|
| [00_LEEME_PRIMERO.md](docs/00_LEEME_PRIMERO.md) | 5 min | Todos |
| [QUICK_START.md](docs/QUICK_START.md) | 5 min | Desarrolladores |
| [INDICE_DOCUMENTACION.md](docs/INDICE_DOCUMENTACION.md) | 3 min | Encontrar qué leer |
| [GUIA_INTEGRACION.md](docs/GUIA_INTEGRACION.md) | 20 min | Arquitectos |
| [DOCUMENTO_MENU_BUTTON.md](docs/DOCUMENTO_MENU_BUTTON.md) | 15 min | Devs avanzados |
| [RESUMEN_EJECUTIVO.md](docs/RESUMEN_EJECUTIVO.md) | 5 min | PM/Clientes |

👉 **[Ver todas las guías →](docs/)**

---

## 📧 ¿Preguntas?

Toda la documentación está en `docs/` - ahí encontrarás respuestas a todas tus preguntas.

---

**¡Listo para comenzar!** 🚀
