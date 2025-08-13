# Guía de Uso - Notebook to PDF Converter

Esta guía proporciona ejemplos detallados de uso para todas las herramientas de conversión de notebooks a PDF.

## Índice

1. [Primeros Pasos](#primeros-pasos)
2. [Convertidor Inteligente](#convertidor-inteligente)
3. [Convertidor Clásico](#convertidor-clásico)
4. [Script Shell](#script-shell)
5. [Casos de Uso Avanzados](#casos-de-uso-avanzados)
6. [Integración con Flujos de Trabajo](#integración-con-flujos-de-trabajo)
7. [Solución de Problemas](#solución-de-problemas)

## Primeros Pasos

### Verificar Instalación

```bash
# Verificar dependencias
python convert.py --check-deps

# Debería mostrar:
# ✓ Todas las dependencias están instaladas
```

### Conversión Básica

```bash
# Convertir un notebook individual
python smart_convert.py mi_notebook.ipynb

# Convertir todos los notebooks en un directorio
python smart_convert.py contenido/
```

## Convertidor Inteligente

El convertidor inteligente (`smart_convert.py`) es la herramienta recomendada para uso diario.

### Características Principales

- **Cache automático**: Solo regenera cuando hay cambios
- **Verificación de hash**: Detecta cambios en contenido
- **Estado detallado**: Muestra qué necesita conversión

### Ejemplos de Uso

#### Ver Estado Sin Convertir

```bash
# Mostrar estado de todos los notebooks
python smart_convert.py contenido/ --status

# Salida esperada:
# Estado de conversión (15 notebooks)
# ============================================================
#        OK | configuracion-fundamentos.ipynb         | Actualizado (245K, 2024-08-12 10:30)
# PENDIENTE | estructuras-control.ipynb               | PDF no existe
#        OK | funciones-modulos.ipynb                 | Actualizado (189K, 2024-08-12 09:15)
```

#### Conversión Normal

```bash
# Conversión inteligente (solo notebooks modificados)
python smart_convert.py contenido/

# Salida esperada:
# Conversión inteligente: 3 notebooks
# ------------------------------------------------------------
# [ 1/ 3] ✓ Convertido: estructuras-control.pdf (156K) (PDF no existe)
# [ 2/ 3] ✓ Convertido: nuevos-datos.pdf (203K) (Contenido modificado)
# [ 3/ 3] ✓ Convertido: estadisticas.pdf (178K) (Notebook más reciente)
```

#### Regenerar Todo

```bash
# Forzar regeneración de todos los PDFs
python smart_convert.py contenido/ --force

# Útil cuando:
# - Cambias configuración de pandoc
# - Actualizas plantillas LaTeX
# - Quieres asegurar consistencia
```

#### Vista Previa

```bash
# Ver qué se convertiría sin ejecutar
python smart_convert.py contenido/ --dry-run

# Salida esperada:
# MODO DRY-RUN: No se realizarán conversiones reales
# [ 1/ 5] [DRY-RUN] Convertiría: notebook1.ipynb -> notebook1.pdf
```

### Configuración de Cache

```bash
# Usar archivo de cache personalizado
python smart_convert.py contenido/ --cache-file .mi_cache.json

# Cache por defecto: .conversion_cache.json
```

## Convertidor Clásico

El convertidor clásico (`convert.py`) ofrece control completo sin cache automático.

### Casos de Uso

- Primera conversión masiva
- Configuración específica de motor
- Integración en scripts automatizados
- Cuando no se desea cache

### Ejemplos de Uso

#### Conversión Básica

```bash
# Convertir directorio completo
python convert.py contenido/

# Convertir archivo específico
python convert.py contenido/bloque-1/semana-1/configuracion.ipynb
```

#### Motor LaTeX Específico

```bash
# Usar XeLaTeX (mejor para UTF-8)
python convert.py contenido/ --engine xelatex

# Usar PDFLaTeX (más compatible)
python convert.py contenido/ --engine pdflatex

# Usar LuaLaTeX (tipografía moderna)
python convert.py contenido/ --engine lualatex
```

#### Directorio de Salida

```bash
# Guardar PDFs en directorio específico
python convert.py contenido/ -o pdfs/

# Estructura resultante:
# pdfs/
# ├── configuracion-fundamentos.pdf
# ├── estructuras-control.pdf
# └── ...
```

#### Control de Recursión

```bash
# Solo archivos del directorio raíz
python convert.py contenido/bloque-1/ --no-recursive

# Recursivo (default)
python convert.py contenido/
```

## Script Shell

El script shell (`convert.sh`) es la opción más rápida para conversiones simples.

### Ventajas

- Ejecución más rápida que Python
- Colores en output para mejor legibilidad
- Manejo nativo de señales del sistema
- Menor uso de memoria

### Ejemplos de Uso

#### Hacer Ejecutable (Primera Vez)

```bash
chmod +x convert.sh
```

#### Uso Básico

```bash
# Conversión simple
./convert.sh contenido/

# Con colores y progreso visual:
# [INFO] Encontrados 15 notebooks
# ------------------------------------------------------------
# [ 1/15] ✓ configuracion-fundamentos.ipynb
# [ 2/15] ✓ estructuras-control.ipynb
```

#### Opciones Avanzadas

```bash
# Output verboso
./convert.sh contenido/ --verbose

# Directorio de salida
./convert.sh contenido/ -o pdfs/

# Motor específico
./convert.sh contenido/ --engine pdflatex

# Vista previa
./convert.sh contenido/ --dry-run
```

#### Combinación de Opciones

```bash
# Conversión completa con configuración específica
./convert.sh contenido/ \
  --output pdfs/ \
  --engine xelatex \
  --verbose \
  --force
```

## Casos de Uso Avanzados

### Procesamiento por Lotes

```bash
# Convertir múltiples directorios
for dir in bloque-*; do
    echo "Procesando $dir..."
    python smart_convert.py "$dir/"
done
```

### Filtrado por Patrones

```bash
# Solo notebooks que contienen "semana" en el nombre
find contenido/ -name "*semana*.ipynb" -exec python convert.py {} \;

# Usando find con smart converter
find contenido/ -name "*.ipynb" | while read notebook; do
    python smart_convert.py "$notebook"
done
```

### Integración con Make

```makefile
# Makefile para automatización
.PHONY: pdfs clean-pdfs update-pdfs

pdfs:
	python herramientas/notebook-to-pdf/smart_convert.py contenido/

clean-pdfs:
	find contenido/ -name "*.pdf" -delete
	rm -f .conversion_cache.json

update-pdfs:
	python herramientas/notebook-to-pdf/smart_convert.py contenido/ --force

# Usar con:
# make pdfs
# make clean-pdfs
# make update-pdfs
```

### Procesamiento Paralelo

```bash
# Usando GNU parallel (si está disponible)
find contenido/ -name "*.ipynb" | parallel python convert.py {}

# Usando xargs para procesamiento en lotes
find contenido/ -name "*.ipynb" | xargs -n 5 -P 4 python convert.py
```

## Integración con Flujos de Trabajo

### Pre-commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "Verificando notebooks..."

# Verificar que los PDFs estén actualizados
python herramientas/notebook-to-pdf/smart_convert.py contenido/ --dry-run

if [ $? -ne 0 ]; then
    echo "Error: algunos notebooks necesitan conversión"
    echo "Ejecuta: make pdfs"
    exit 1
fi

echo "Notebooks OK"
```

### GitHub Actions

```yaml
# .github/workflows/notebooks.yml
name: Convert Notebooks

on: 
  push:
    paths: ['contenido/**/*.ipynb']

jobs:
  convert:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Install dependencies
      run: |
        sudo apt update
        sudo apt install pandoc texlive-xetex
    
    - name: Convert notebooks
      run: |
        python herramientas/notebook-to-pdf/convert.py contenido/
    
    - name: Upload PDFs
      uses: actions/upload-artifact@v3
      with:
        name: notebooks-pdf
        path: 'contenido/**/*.pdf'
```

### VSCode Tasks

```json
// .vscode/tasks.json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Convert Notebooks",
            "type": "shell",
            "command": "python",
            "args": [
                "herramientas/notebook-to-pdf/smart_convert.py",
                "contenido/"
            ],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            },
            "problemMatcher": []
        },
        {
            "label": "Check Notebook Status",
            "type": "shell",
            "command": "python",
            "args": [
                "herramientas/notebook-to-pdf/smart_convert.py",
                "contenido/",
                "--status"
            ],
            "group": "test"
        }
    ]
}
```

## Solución de Problemas

### Dependencias Faltantes

```bash
# Ubuntu/Debian
sudo apt install pandoc texlive-xetex texlive-fonts-recommended

# macOS
brew install pandoc
brew install --cask mactex

# Verificar instalación
python convert.py --check-deps
```

### Errores Comunes

#### Error: "pandoc no encontrado"

```bash
# Verificar instalación
which pandoc
pandoc --version

# Si no está instalado:
sudo apt install pandoc  # Ubuntu/Debian
brew install pandoc      # macOS
```

#### Advertencias de Fuentes

```bash
# Advertencias como estas son normales:
# Warning: Could not load font "DejaVu Sans"

# El PDF se genera correctamente, las advertencias son cosméticas
# Para usar un motor más compatible:
python convert.py contenido/ --engine pdflatex
```

#### Timeout en Conversión

```bash
# Para notebooks muy grandes que tardan >5 minutos
# Editar convert.py y cambiar timeout:
# result = subprocess.run(cmd, timeout=600)  # 10 minutos
```

### Cache Corrupto

```bash
# Si el cache inteligente se corrompe:
rm .conversion_cache.json

# El converter recreará el cache automáticamente
python smart_convert.py contenido/
```

### Problemas de Encoding

```bash
# Para notebooks con caracteres especiales:
# 1. Usar XeLaTeX (mejor soporte UTF-8)
python convert.py contenido/ --engine xelatex

# 2. Verificar encoding del notebook
file -i mi_notebook.ipynb
# Debería mostrar: charset=utf-8
```

### Debug Detallado

```bash
# Para debug más detallado, usar script shell con verbose:
./convert.sh contenido/ --verbose

# O modificar temporalmente los scripts Python para más logging
```

## Configuración Avanzada

### Variables de Entorno

```bash
# Configurar motor por defecto
export NOTEBOOK_PDF_ENGINE=xelatex

# Directorio temporal personalizado
export TMPDIR=/var/tmp

# Timeout personalizado (en segundos)
export NOTEBOOK_PDF_TIMEOUT=600
```

### Personalización de Pandoc

Para modificar la configuración de pandoc, edita los comandos en `convert.py`:

```python
# Configuración actual
cmd = [
    'pandoc',
    str(notebook_path),
    '-o', str(output_path),
    f'--pdf-engine={engine}',
    '--variable', 'geometry:margin=2cm',
    '--variable', 'fontsize=11pt',
    '--variable', 'documentclass=article',
    '--variable', 'papersize=letter'
]

# Ejemplos de personalización:
# Márgenes más pequeños
'--variable', 'geometry:margin=1.5cm',

# Fuente más grande
'--variable', 'fontsize=12pt',

# Formato A4
'--variable', 'papersize=a4',

# Numeración de páginas
'--variable', 'pagestyle=plain',
```

## Monitoreo y Métricas

### Estadísticas de Conversión

```bash
# Ver estadísticas del cache
python -c "
import json
with open('.conversion_cache.json') as f:
    cache = json.load(f)
print(f'Notebooks en cache: {len(cache)}')
for path, info in cache.items():
    print(f'{path}: convertido {info.get(\"converted_at\", \"unknown\")}')
"
```

### Tamaños de Archivos

```bash
# Ver tamaños de PDFs generados
find contenido/ -name "*.pdf" -exec ls -lh {} \; | awk '{print $5, $9}'

# Resumen de tamaños
find contenido/ -name "*.pdf" -exec stat -c%s {} \; | awk '
{
    total += $1
    count++
}
END {
    print "Total PDFs:", count
    print "Tamaño total:", total/1024/1024 "MB"
    print "Promedio:", total/count/1024 "KB"
}'
```

Esta guía cubre los casos de uso más comunes. Para casos específicos no cubiertos, consulta la documentación técnica o ejecuta los scripts con `--help`.
