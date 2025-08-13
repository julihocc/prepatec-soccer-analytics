# Notebook to PDF Converter - Herramienta Universal

Convierte notebooks de Jupyter (.ipynb) a PDF usando pandoc con configuración optimizada para contenido educativo en español.

## Descripción

Herramienta profesional para convertir notebooks Jupyter a PDF de alta calidad. Incluye conversión inteligente con cache, múltiples motores LaTeX, y configuración optimizada para documentos educativos.

## Uso Rápido

### Convertidor Inteligente (Recomendado)
```bash
python smart_convert.py contenido/
```

**Características inteligentes:**
- Solo regenera PDFs cuando es necesario
- Cache inteligente con verificación de hash
- Muestra estado detallado con timestamps
- Opciones de forzado y vista previa

### Convertidor Clásico Python
```bash
python convert.py contenido/
```

### Script Shell (Más Rápido)
```bash
./convert.sh contenido/
```

## Instalación

### Dependencias del Sistema
```bash
# Ubuntu/Debian
sudo apt install pandoc texlive-xetex

# macOS (con Homebrew)
brew install pandoc
brew install --cask mactex

# Verificar instalación
python convert.py --check-deps
```

### Dependencias Python
```bash
# Solo librerías estándar de Python 3.7+
# No se requieren instalaciones adicionales
```

## Archivos de la Herramienta

### Scripts Principales
- `smart_convert.py` - **Convertidor inteligente** (recomendado)
- `convert.py` - Convertidor clásico con todas las opciones
- `convert.sh` - Script shell rápido con colores

### Documentación
- `README.md` - Esta guía
- `USAGE_GUIDE.md` - Ejemplos detallados de uso
- `TECHNICAL_DETAILS.md` - Implementación técnica
- `INSTALLATION.md` - Guía de instalación completa

### Tests
- `tests/` - Suite completa de tests
- `tests/run_tests.py` - Ejecutor de tests automatizados

## Formato de Salida

Los PDFs generados incluyen:
- **Formato**: A4/Letter con márgenes de 2cm
- **Fuente**: 11pt optimizada para lectura
- **Codificación**: UTF-8 completa (acentos, ñ, símbolos)
- **Imágenes**: Incrustadas en alta calidad
- **Código**: Sintaxis resaltada preservada

## Ejemplos de Uso

### Uso Básico
```bash
# Convertir un notebook
python smart_convert.py notebook.ipynb

# Convertir directorio completo
python smart_convert.py contenido/

# Ver estado sin convertir
python smart_convert.py contenido/ --status
```

### Opciones Avanzadas
```bash
# Directorio de salida específico
python convert.py contenido/ -o pdfs/

# Motor LaTeX específico
python convert.py contenido/ --engine pdflatex

# Regenerar todo (ignorar cache)
python smart_convert.py contenido/ --force

# Vista previa (dry run)
python convert.py contenido/ --dry-run
```

### Script Shell
```bash
# Hacer ejecutable (primera vez)
chmod +x convert.sh

# Uso básico
./convert.sh contenido/

# Con opciones
./convert.sh contenido/ -o pdfs/ --engine xelatex
./convert.sh contenido/ --dry-run --verbose
```

## Características

### Conversión Inteligente
- **Cache automático**: Solo regenera cuando hay cambios
- **Verificación hash**: Detecta cambios en contenido
- **Timestamps**: Compara fechas de notebook vs PDF
- **Estado detallado**: Muestra qué necesita conversión

### Múltiples Motores
- **XeLaTeX** (default): Mejor soporte para UTF-8 y fuentes
- **PDFLaTeX**: Compatible con sistemas más antiguos  
- **LuaLaTeX**: Alternativa moderna con buena tipografía

### Configuración Educativa
- **Márgenes optimizados**: 2cm para impresión/lectura
- **Fuente legible**: 11pt equilibrada para texto y código
- **Encoding completo**: Soporte para español (ñ, acentos)
- **Código preservado**: Sintaxis highlighting mantenido

### Gestión de Errores
- **Timeouts**: Evita procesos colgados (5 min máximo)
- **Dependencias**: Verificación automática al inicio
- **Logs detallados**: Errores específicos y soluciones
- **Warnings**: Distingue errores de advertencias de fuentes

## Rendimiento

### Tiempos Típicos
- **Notebook pequeño** (1-10 celdas): 3-8 segundos
- **Notebook mediano** (11-50 celdas): 8-20 segundos
- **Notebook grande** (50+ celdas): 20-60 segundos

### Optimizaciones
- **Cache inteligente**: Evita reconversiones innecesarias
- **Procesamiento paralelo**: Script shell más rápido
- **Timeouts**: Evita procesos infinitos
- **Compresión**: PDFs optimizados en tamaño

## Resolución de Problemas

### Error: "pandoc no encontrado"
```bash
# Instalar pandoc
sudo apt install pandoc  # Ubuntu/Debian
brew install pandoc      # macOS
```

### Error: "LaTeX no encontrado"
```bash
# Instalar LaTeX
sudo apt install texlive-xetex  # Ubuntu/Debian
brew install --cask mactex      # macOS
```

### Advertencias de fuentes
- **Síntoma**: Warnings sobre fuentes pero PDF se genera
- **Solución**: Normal, resultado es correcto
- **Alternativa**: Usar `--engine pdflatex` si persiste

### PDFs muy grandes
```bash
# Usar motor alternativo
python convert.py contenido/ --engine pdflatex

# Verificar imágenes en notebooks
# (Imágenes de alta resolución aumentan tamaño)
```

### Notebooks con caracteres especiales
- **Emojis**: Pueden causar warnings (resultado OK)
- **Símbolos matemáticos**: Usar LaTeX math blocks
- **Acentos**: Completamente soportados

## Integración con Proyectos

### Makefile
```makefile
# Agregar a tu Makefile
pdfs:
	python herramientas/notebook-to-pdf/smart_convert.py contenido/

clean-pdfs:
	find contenido/ -name "*.pdf" -delete

.PHONY: pdfs clean-pdfs
```

### CI/CD
```yaml
# GitHub Actions ejemplo
- name: Convert notebooks to PDF
  run: |
    sudo apt install pandoc texlive-xetex
    python herramientas/notebook-to-pdf/convert.py contenido/
```

### Pre-commit Hook
```bash
#!/bin/bash
# .git/hooks/pre-commit
python herramientas/notebook-to-pdf/smart_convert.py contenido/ --dry-run
```

## Ejecutar Tests

```bash
# Todos los tests
python tests/run_tests.py

# Test específico
python tests/run_tests.py test_conversion

# Validar entorno
python tests/run_tests.py --validate

# Test con coverage
python tests/run_tests.py --coverage
```

## Estructura del Proyecto

```
notebook-to-pdf/
├── convert.py              # Convertidor principal
├── smart_convert.py        # Convertidor inteligente
├── convert.sh             # Script shell rápido
├── README.md              # Esta documentación
├── USAGE_GUIDE.md         # Ejemplos detallados
├── TECHNICAL_DETAILS.md   # Detalles técnicos
├── INSTALLATION.md        # Guía de instalación
└── tests/
    ├── run_tests.py       # Ejecutor de tests
    ├── test_conversion.py # Tests de conversión
    ├── test_smart.py      # Tests del convertidor inteligente
    ├── test_shell.py      # Tests del script shell
    └── fixtures/          # Notebooks de prueba
```

## API de Línea de Comandos

### smart_convert.py
```
usage: smart_convert.py [-h] [-o OUTPUT] [--engine {xelatex,pdflatex,lualatex}]
                       [--no-recursive] [--force] [--dry-run] [--status]
                       [--cache-file CACHE_FILE]
                       input

Opciones principales:
  input                 Archivo .ipynb o directorio con notebooks
  -o OUTPUT            Directorio de salida (opcional)
  --engine ENGINE      Motor LaTeX (default: xelatex)
  --status             Solo mostrar estado sin convertir
  --force              Regenerar todos los PDFs
  --dry-run            Vista previa sin ejecutar
```

### convert.py
```
usage: convert.py [-h] [-o OUTPUT] [--engine {xelatex,pdflatex,lualatex}]
                  [--no-recursive] [--dry-run] [--force] [--check-deps]
                  input

Similar a smart_convert.py pero sin cache inteligente.
```

### convert.sh
```
usage: convert.sh [OPTIONS] INPUT

Opciones shell:
  -o, --output DIR     Directorio de salida
  -e, --engine ENGINE  Motor LaTeX
  --no-recursive       No buscar en subdirectorios
  --dry-run           Vista previa
  --force             Regenerar todo
  -v, --verbose       Output detallado
```

## Contribuir

### Reportar Problemas
1. Ejecutar tests: `python tests/run_tests.py`
2. Verificar dependencias: `python convert.py --check-deps`
3. Crear ejemplo mínimo que reproduzca el problema
4. Incluir output completo del error

### Agregar Funcionalidad
1. Escribir tests primero en `tests/`
2. Implementar funcionalidad
3. Verificar que todos los tests pasen
4. Actualizar documentación relevante

### Estándares de Código
- **Python**: PEP 8, type hints, docstrings
- **Shell**: Bash strict mode, funciones modulares
- **Tests**: Casos edge, mocking de dependencias
- **Docs**: Ejemplos ejecutables, troubleshooting

## Licencia

Herramienta educativa para conversión de documentos:
- **Pandoc**: GPL (compatible con uso educativo)
- **LaTeX**: LPPL (libre para documentos)
- **Implementación**: Uso educativo y académico libre

## Arquitectura

```
Jupyter Notebook (.ipynb)
         ↓
    [pandoc]
         ↓
    LaTeX Engine (XeLaTeX/PDFLaTeX/LuaLaTeX)
         ↓
    PDF Optimizado
```

La herramienta actúa como interfaz inteligente sobre pandoc, añadiendo:
- Gestión automática de dependencias
- Configuración optimizada para educación
- Cache y verificación de cambios
- Manejo robusto de errores
- Múltiples interfaces (Python/Shell)

## Roadmap

### Versión 1.1
- [ ] Soporte para configuración por proyecto
- [ ] Templates de PDF personalizados
- [ ] Procesamiento paralelo de múltiples notebooks
- [ ] Integración con Jupyter Lab

### Versión 1.2
- [ ] Generación de tabla de contenidos automática
- [ ] Soporte para notebooks con widgets
- [ ] Optimización de imágenes automática
- [ ] Modo batch para CI/CD

## Comparación con Alternativas

| Herramienta | Pros | Contras |
|-------------|------|---------|
| **Esta herramienta** | Cache inteligente, configuración educativa, robusto | Requiere pandoc+LaTeX |
| `jupyter nbconvert` | Nativo de Jupyter | Sin cache, configuración limitada |
| Exportar desde Jupyter | Simple | Manual, sin optimización |
| Herramientas online | No requiere instalación | Dependencia externa, sin cache |

## Soporte

- **Documentación**: Ver archivos `*.md` incluidos
- **Tests**: `python tests/run_tests.py --help`
- **Debug**: Usar `--verbose` en scripts
- **Issues**: Crear ejemplo mínimo reproducible
