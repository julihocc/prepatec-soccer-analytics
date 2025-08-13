# Guía de Instalación - Notebook to PDF Converter

Guía completa para instalar y configurar las herramientas de conversión de notebooks a PDF.

## Instalación Rápida

### Ubuntu/Debian

```bash
# Instalar dependencias del sistema
sudo apt update
sudo apt install pandoc texlive-xetex texlive-fonts-recommended

# Verificar instalación
python3 herramientas/notebook-to-pdf/convert.py --check-deps
```

### macOS

```bash
# Instalar con Homebrew
brew install pandoc
brew install --cask mactex

# Verificar instalación
python3 herramientas/notebook-to-pdf/convert.py --check-deps
```

### Windows

```powershell
# Instalar con Chocolatey
choco install pandoc
choco install miktex

# O descargar instaladores:
# - Pandoc: https://pandoc.org/installing.html
# - MiKTeX: https://miktex.org/download
```

## Requisitos del Sistema

### Dependencias Obligatorias

#### Pandoc
**Propósito**: Motor de conversión principal
**Versión mínima**: 2.0+
**Instalación**:
```bash
# Ubuntu/Debian
sudo apt install pandoc

# macOS
brew install pandoc

# Verificar
pandoc --version
```

#### LaTeX (al menos uno)
**Propósito**: Generación de PDF
**Opciones**:
- **XeLaTeX** (recomendado): Mejor soporte UTF-8
- **PDFLaTeX**: Más compatible
- **LuaLaTeX**: Tipografía moderna

**Instalación**:
```bash
# Ubuntu/Debian (completo)
sudo apt install texlive-full

# Ubuntu/Debian (mínimo)
sudo apt install texlive-xetex texlive-fonts-recommended

# macOS
brew install --cask mactex
```

### Dependencias Python

**Versión Python**: 3.7+
**Librerías**: Solo estándar de Python

**Librerías utilizadas**:
- `pathlib` - Manejo de rutas
- `subprocess` - Ejecución de comandos
- `json` - Cache inteligente
- `hashlib` - Verificación de cambios
- `argparse` - Interfaz de línea de comandos
- `tempfile` - Archivos temporales
- `time` - Timestamps

## Instalación Detallada

### Ubuntu 20.04/22.04 LTS

```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python (si no está instalado)
sudo apt install python3 python3-pip

# Instalar pandoc
sudo apt install pandoc

# Instalar LaTeX completo (recomendado)
sudo apt install texlive-full

# O instalación mínima (más rápida)
sudo apt install texlive-xetex texlive-latex-recommended texlive-fonts-recommended

# Verificar instalación
python3 --version
pandoc --version
xelatex --version

# Probar herramienta
python3 herramientas/notebook-to-pdf/convert.py --check-deps
```

### macOS (Intel/Apple Silicon)

```bash
# Instalar Homebrew si no está instalado
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar pandoc
brew install pandoc

# Instalar MacTeX (completo, ~4GB)
brew install --cask mactex

# O instalación básica
brew install --cask basictex
sudo tlmgr update --self
sudo tlmgr install xetex fontspec

# Verificar instalación
python3 --version
pandoc --version
xelatex --version

# Probar herramienta
python3 herramientas/notebook-to-pdf/convert.py --check-deps
```

### Windows 10/11

#### Opción 1: WSL (Recomendado)

```bash
# Instalar WSL
wsl --install

# Seguir instrucciones de Ubuntu dentro de WSL
```

#### Opción 2: Nativo

```powershell
# Instalar Chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Instalar dependencias
choco install python3
choco install pandoc
choco install miktex

# Verificar
python --version
pandoc --version
```

### CentOS/RHEL/Rocky Linux

```bash
# Habilitar EPEL
sudo dnf install epel-release

# Instalar pandoc
sudo dnf install pandoc

# Instalar TeX Live
sudo dnf install texlive-scheme-full

# O instalación mínima
sudo dnf install texlive-xetex texlive-collection-fontsrecommended

# Verificar
python3 herramientas/notebook-to-pdf/convert.py --check-deps
```

### Arch Linux

```bash
# Instalar dependencias
sudo pacman -S pandoc texlive-core texlive-bin texlive-fontsrecommended

# Verificar
python herramientas/notebook-to-pdf/convert.py --check-deps
```

## Configuración Avanzada

### Variables de Entorno

```bash
# Agregar a ~/.bashrc o ~/.zshrc

# Motor LaTeX por defecto
export NOTEBOOK_PDF_ENGINE=xelatex

# Timeout personalizado (segundos)
export NOTEBOOK_PDF_TIMEOUT=600

# Directorio de cache
export NOTEBOOK_PDF_CACHE_DIR=$HOME/.notebook-pdf-cache
```

### Configuración por Proyecto

Crear `.notebook-pdf.json` en la raíz del proyecto:

```json
{
  "engine": "xelatex",
  "timeout": 300,
  "output_dir": "dist/pdfs",
  "variables": {
    "geometry": "margin=1.5cm",
    "fontsize": "12pt",
    "papersize": "a4"
  },
  "exclude_patterns": [
    "**/draft-*.ipynb",
    "**/.ipynb_checkpoints/**"
  ]
}
```

### Optimización de Performance

#### LaTeX Package Cache

```bash
# Pre-compilar packages LaTeX comunes
sudo fmtutil-sys --all

# Actualizar font cache
sudo fc-cache -f -v
```

#### Disk Space Optimization

```bash
# Instalación mínima LaTeX (Ubuntu)
sudo apt install texlive-latex-base texlive-xetex \
    texlive-fonts-recommended texlive-latex-recommended

# Limpiar cache después de instalación
sudo apt autoremove
sudo apt autoclean
```

## Verificación de Instalación

### Test Básico

```bash
# Verificar dependencias
python3 herramientas/notebook-to-pdf/convert.py --check-deps

# Output esperado:
# ✓ Todas las dependencias están instaladas
```

### Test de Conversión

```bash
# Crear notebook de prueba
echo '{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": ["# Test\n", "Notebook de prueba"]
    }
  ],
  "metadata": {"kernelspec": {"name": "python3"}},
  "nbformat": 4,
  "nbformat_minor": 4
}' > test.ipynb

# Convertir
python3 herramientas/notebook-to-pdf/convert.py test.ipynb

# Verificar PDF generado
ls -la test.pdf
```

### Test Suite Completa

```bash
# Ejecutar todos los tests
python3 herramientas/notebook-to-pdf/tests/run_tests.py

# Test específico
python3 herramientas/notebook-to-pdf/tests/run_tests.py test_conversion
```

## Solución de Problemas

### Pandoc no encontrado

```bash
# Verificar PATH
echo $PATH
which pandoc

# Ubuntu: Reinstalar
sudo apt remove pandoc
sudo apt install pandoc

# macOS: Reinstalar
brew uninstall pandoc
brew install pandoc
```

### LaTeX no encontrado

```bash
# Verificar instalación LaTeX
which xelatex
which pdflatex

# Ubuntu: Instalar paquetes faltantes
sudo apt install texlive-xetex

# Verificar distribución LaTeX
tex --version
```

### Errores de Fuentes

#### Ubuntu/Debian

```bash
# Instalar fuentes adicionales
sudo apt install fonts-liberation fonts-dejavu-core

# Actualizar cache de fuentes
sudo fc-cache -f -v
```

#### macOS

```bash
# Instalar fuentes del sistema
brew install --cask font-dejavu

# O usar motor más compatible
python3 herramientas/notebook-to-pdf/convert.py contenido/ --engine pdflatex
```

### Permisos Insuficientes

```bash
# Verificar permisos del directorio
ls -la herramientas/notebook-to-pdf/

# Hacer ejecutables si es necesario
chmod +x herramientas/notebook-to-pdf/*.py
chmod +x herramientas/notebook-to-pdf/*.sh
```

### Problemas de Memoria

```bash
# Para sistemas con poca RAM, usar PDFLaTeX
python3 herramientas/notebook-to-pdf/convert.py contenido/ --engine pdflatex

# Convertir notebooks individualmente
for notebook in contenido/**/*.ipynb; do
    python3 herramientas/notebook-to-pdf/convert.py "$notebook"
done
```

## Configuración en Entornos Específicos

### Docker

```dockerfile
FROM ubuntu:22.04

# Instalar dependencias
RUN apt-get update && apt-get install -y \
    python3 \
    pandoc \
    texlive-xetex \
    texlive-fonts-recommended \
    && rm -rf /var/lib/apt/lists/*

# Copiar herramientas
COPY herramientas/notebook-to-pdf /app/tools/

# Verificar instalación
RUN python3 /app/tools/convert.py --check-deps
```

### GitHub Codespaces

```yaml
# .devcontainer/devcontainer.json
{
  "name": "Notebook PDF Converter",
  "image": "mcr.microsoft.com/vscode/devcontainers/python:3",
  "postCreateCommand": "sudo apt update && sudo apt install -y pandoc texlive-xetex",
  "customizations": {
    "vscode": {
      "extensions": ["ms-python.python"]
    }
  }
}
```

### Google Colab

```python
# Instalar en celda de Colab
!apt-get update
!apt-get install -y pandoc texlive-xetex
!python herramientas/notebook-to-pdf/convert.py --check-deps
```

### Jupyter Hub

```bash
# Instalar en imagen base
RUN conda install -c conda-forge pandoc
RUN conda install -c conda-forge texlive-core

# O en post-start hook
#!/bin/bash
if ! command -v pandoc &> /dev/null; then
    mamba install -c conda-forge pandoc texlive-core
fi
```

## Actualizaciones

### Mantener Actualizado

```bash
# Ubuntu/Debian
sudo apt update && sudo apt upgrade pandoc texlive-xetex

# macOS
brew upgrade pandoc
brew upgrade --cask mactex

# Verificar versiones
pandoc --version
xelatex --version
```

### Migración de Versiones

```bash
# Respaldar cache existente
cp .conversion_cache.json .conversion_cache.json.backup

# Limpiar cache si hay problemas
rm .conversion_cache.json

# Regenerar PDFs con nueva versión
python3 herramientas/notebook-to-pdf/smart_convert.py contenido/ --force
```

## Configuración de CI/CD

### GitHub Actions

```yaml
# .github/workflows/pdf-generation.yml
name: Generate PDFs
on: [push, pull_request]

jobs:
  generate-pdfs:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y pandoc texlive-xetex
    
    - name: Generate PDFs
      run: |
        python3 herramientas/notebook-to-pdf/convert.py contenido/
    
    - name: Upload PDFs
      uses: actions/upload-artifact@v3
      with:
        name: pdfs
        path: 'contenido/**/*.pdf'
```

### GitLab CI

```yaml
# .gitlab-ci.yml
generate-pdfs:
  image: ubuntu:22.04
  before_script:
    - apt-get update
    - apt-get install -y python3 pandoc texlive-xetex
  script:
    - python3 herramientas/notebook-to-pdf/convert.py contenido/
  artifacts:
    paths:
      - contenido/**/*.pdf
    expire_in: 1 week
```

## Soporte y Mantenimiento

### Logs de Instalación

```bash
# Guardar log de instalación
{
    echo "=== Instalación $(date) ==="
    python3 --version
    pandoc --version
    xelatex --version
    python3 herramientas/notebook-to-pdf/convert.py --check-deps
} >> installation.log
```

### Monitoreo de Sistema

```bash
# Script de verificación periódica
#!/bin/bash
# health-check.sh

echo "Verificando herramientas..."
python3 herramientas/notebook-to-pdf/convert.py --check-deps

if [ $? -eq 0 ]; then
    echo "✓ Sistema OK"
    exit 0
else
    echo "✗ Sistema requiere atención"
    exit 1
fi
```

Con esta guía de instalación, deberías poder configurar las herramientas en cualquier sistema compatible. Para problemas específicos no cubiertos, consulta la documentación técnica o crea un issue con los detalles del error.
