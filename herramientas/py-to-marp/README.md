# Convertidor py:percent a Marp

Herramienta especializada para convertir archivos `.py` en formato percent (jupytext) a presentaciones Markdown compatibles con [Marp](https://marp.app/), optimizada para contenido educativo de ciencia de datos.

## 🎯 Características

- ✅ **Conversión automática** de celdas py:percent a slides Marp
- 🎨 **Estilos predefinidos** para diferentes tipos de presentaciones
- 📚 **Optimizado para educación** con estilos específicos para preguntas, código y contenido
- 🔧 **Configuración flexible** con templates determinados
- 📱 **Separación inteligente** de slides basada en estructura del contenido
- 🎯 **Sintaxis highlighting** automático para código Python

## 🚀 Instalación

No requiere instalaciones adicionales, solo Python 3.6+ que ya está en el entorno.

Para exportar a PDF/PNG se recomienda instalar Marp CLI:
```bash
npm install -g @marp-team/marp-cli
```

## 📖 Uso Básico

### Conversión simple
```bash
# Conversión con configuración educativa por defecto
python convert.py contenido/bloque-1/semana-1/configuracion-fundamentos.py

# Con configuración específica
python convert.py archivo.py --config taller

# Con título personalizado
python convert.py archivo.py --title "Mi Presentación Especial"
```

### Usando Makefile (recomendado)
```bash
# Ver ayuda completa
make help

# Convertir archivo específico
make convert FILE=path/to/archivo.py CONFIG=educativo

# Convertir todo un bloque
make convert-bloque BLOQUE=1 CONFIG=taller

# Convertir todo el contenido
make convert-all CONFIG=dark
```

## 🎨 Configuraciones Disponibles

| Configuración | Uso recomendado | Colores principales |
|---------------|-----------------|-------------------|
| `educativo` | Clases regulares, contenido para estudiantes | Azul/Rojo (#3498db/#e74c3c) |
| `ejecutivo` | Presentaciones para directivos/docentes | Azul/Verde (#007bff/#28a745) |
| `taller` | Sesiones prácticas, workshops | Naranja/Púrpura (#fd7e14/#6610f2) |
| `evaluacion` | Exámenes, evaluaciones | Rojo/Gris (#dc3545/#6c757d) |
| `dark` | Presentaciones nocturnas, modo oscuro | Cyan/Amarillo (#17a2b8/#ffc107) |

```bash
# Listar todas las configuraciones
python convert.py --list-configs
```

## 📋 Estructura de Salida

La herramienta genera automáticamente:

1. **Slide de título** con información del curso
2. **Separación inteligente** basada en:
   - Títulos de sesión (`## SESIÓN`)
   - Títulos principales (`# Título`)
   - Preguntas importantes (`## ¿Pregunta?`)
3. **Formateo especial** para:
   - Cajas de preguntas con estilo destacado
   - Código Python con syntax highlighting
   - Contenido resaltado con colores del tema

## 🛠️ Funciones Avanzadas

### Personalización de headers/footers
```bash
python convert.py archivo.py \
  --header "Mi Header Personalizado" \
  --footer "Footer Especial"
```

### Conversión masiva con Makefile
```bash
# Por tipo de configuración
make educativo    # Convierte todo con config educativa
make taller       # Convierte todo con config de taller
make dark         # Convierte todo con config dark

# Por bloque específico
make bloque1 CONFIG=ejecutivo
make bloque2 CONFIG=evaluacion
```

### Exportación a diferentes formatos
```bash
# Después de generar los .md, exportar a PDF
make export-pdf

# O manualmente con marp-cli
marp presentacion.md -o presentacion.pdf
marp presentacion.md --images png -o slides/
```

## 📁 Estructura de Archivos

```
py-to-marp/
├── py_to_marp.py      # Convertidor principal
├── configs.py         # Configuraciones predefinidas
├── convert.py         # Script CLI mejorado
├── Makefile          # Automatización de tareas
└── README.md         # Esta documentación
```

## 🎨 Personalización de Estilos

Para crear una nueva configuración, edita `configs.py`:

```python
MI_CONFIG = MarpConfig(
    theme="default",
    size="16:9",
    paginate=True,
    footer="Mi Footer",
    background_color="#ffffff",
    text_color="#333333",
    primary_color="#custom1",
    secondary_color="#custom2"
)

# Agregar al diccionario CONFIGS
CONFIGS["mi_config"] = MI_CONFIG
```

## 🔄 Flujo de Trabajo Recomendado

1. **Desarrollo**: Editar archivos `.py` en formato percent
2. **Conversión**: `make convert FILE=mi_archivo.py CONFIG=educativo`
3. **Previsualización**: `code mi_archivo.md` o `marp -s mi_archivo.md`
4. **Exportación**: `marp mi_archivo.md -o presentacion.pdf`
5. **Distribución**: Usar PDF para estudiantes, MD para colaboración

## 🐛 Troubleshooting

### El archivo generado no se ve bien
- Verificar que el archivo `.py` esté en formato percent correcto
- Revisar que las celdas markdown tengan `# %% [markdown]`
- Comprobar que las celdas de código tengan `# %%`

### Los slides no se separan correctamente
- Asegurar títulos con formato `# Título` o `## SESIÓN X`
- Usar preguntas con formato `## ¿Pregunta?`
- Verificar estructura jerárquica del contenido

### Problemas de exportación
- Instalar marp-cli: `npm install -g @marp-team/marp-cli`
- Verificar que Node.js esté instalado
- Para PDFs complejos, usar `--allow-local-files`

## 📚 Ejemplos

Ver ejemplos completos en el directorio `contenido/` del proyecto principal.

## 🤝 Contribución

Para mejoras o nuevas configuraciones:
1. Editar `configs.py` para nuevos estilos
2. Modificar `py_to_marp.py` para nueva funcionalidad
3. Actualizar `Makefile` para nuevos comandos
4. Documentar cambios en este README

## 📄 Licencia

Parte del proyecto educativo TEC - Ciencia de Datos aplicada al Fútbol.
