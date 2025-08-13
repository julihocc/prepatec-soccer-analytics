#!/bin/bash
# 
# Notebook to PDF Converter - Script de Shell
#
# Convertidor rápido de notebooks Jupyter a PDF usando pandoc.
# Versión shell optimizada para uso desde línea de comandos.
#
# Autor: Curso de Ciencia de Datos aplicada al Fútbol
# Versión: 1.0.0

set -euo pipefail

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Variables globales
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENGINE="xelatex"
RECURSIVE=true
DRY_RUN=false
FORCE=false
OUTPUT_DIR=""
VERBOSE=false

# Contadores
CONVERTED=0
SKIPPED=0
FAILED=0

# Función de ayuda
show_help() {
    cat << EOF
Notebook to PDF Converter - Shell Script

USAGE:
    $(basename "$0") [OPTIONS] INPUT

ARGUMENTS:
    INPUT                   Archivo .ipynb o directorio con notebooks

OPTIONS:
    -o, --output DIR       Directorio de salida (opcional)
    -e, --engine ENGINE    Motor LaTeX: xelatex|pdflatex|lualatex (default: xelatex)
    --no-recursive         No buscar recursivamente en subdirectorios
    --dry-run             Mostrar qué se haría sin ejecutar conversiones
    --force               Regenerar PDFs aunque estén actualizados
    -v, --verbose         Output detallado
    -h, --help            Mostrar esta ayuda
    --check-deps          Solo verificar dependencias

EJEMPLOS:
    $(basename "$0") notebook.ipynb                    # Convertir un archivo
    $(basename "$0") contenido/                        # Convertir directorio
    $(basename "$0") contenido/ --no-recursive         # Solo nivel raíz
    $(basename "$0") contenido/ -o pdfs/               # Directorio específico
    $(basename "$0") contenido/ --engine pdflatex      # Motor específico
    $(basename "$0") contenido/ --dry-run              # Vista previa
    $(basename "$0") contenido/ --force                # Regenerar todo

DEPENDENCIAS:
    - pandoc
    - texlive-xetex (o similar)

EOF
}

# Función para logs con colores
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[OK]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_verbose() {
    if [[ "$VERBOSE" == true ]]; then
        echo -e "${NC}[DEBUG] $1"
    fi
}

# Verificar dependencias
check_dependencies() {
    local missing=()
    
    # Verificar pandoc
    if ! command -v pandoc &> /dev/null; then
        missing+=("pandoc")
    fi
    
    # Verificar al menos un motor LaTeX
    local latex_found=false
    for engine in xelatex pdflatex lualatex; do
        if command -v "$engine" &> /dev/null; then
            latex_found=true
            break
        fi
    done
    
    if [[ "$latex_found" == false ]]; then
        missing+=("texlive-xetex (o similar)")
    fi
    
    if [[ ${#missing[@]} -gt 0 ]]; then
        log_error "Dependencias faltantes:"
        for dep in "${missing[@]}"; do
            echo "  - $dep"
        done
        echo
        echo "Instalar en Ubuntu/Debian:"
        echo "  sudo apt install pandoc texlive-xetex"
        return 1
    fi
    
    return 0
}

# Encontrar notebooks
find_notebooks() {
    local input_path="$1"
    local notebooks=()
    
    if [[ -f "$input_path" ]]; then
        if [[ "$input_path" == *.ipynb ]]; then
            notebooks=("$input_path")
        fi
    elif [[ -d "$input_path" ]]; then
        if [[ "$RECURSIVE" == true ]]; then
            while IFS= read -r -d '' file; do
                # Filtrar checkpoints
                if [[ "$file" != *".ipynb_checkpoints"* ]]; then
                    notebooks+=("$file")
                fi
            done < <(find "$input_path" -name "*.ipynb" -type f -print0)
        else
            while IFS= read -r -d '' file; do
                if [[ "$file" != *".ipynb_checkpoints"* ]]; then
                    notebooks+=("$file")
                fi
            done < <(find "$input_path" -maxdepth 1 -name "*.ipynb" -type f -print0)
        fi
    fi
    
    # Ordenar array
    IFS=$'\n' notebooks=($(sort <<<"${notebooks[*]}"))
    unset IFS
    
    printf '%s\n' "${notebooks[@]}"
}

# Convertir un notebook individual
convert_notebook() {
    local notebook_path="$1"
    local output_path="$2"
    
    log_verbose "Convirtiendo: $notebook_path -> $output_path"
    
    # Verificar si existe el notebook
    if [[ ! -f "$notebook_path" ]]; then
        log_error "Archivo no encontrado: $notebook_path"
        ((FAILED++))
        return 1
    fi
    
    # Verificar si es necesario regenerar (a menos que sea force)
    if [[ "$FORCE" == false && -f "$output_path" ]]; then
        if [[ "$notebook_path" -ot "$output_path" ]]; then
            log_verbose "Ya actualizado: $(basename "$output_path")"
            ((SKIPPED++))
            return 0
        fi
    fi
    
    if [[ "$DRY_RUN" == true ]]; then
        echo "[DRY-RUN] Convertiría: $(basename "$notebook_path") -> $(basename "$output_path")"
        return 0
    fi
    
    # Crear directorio de salida si es necesario
    local output_dir
    output_dir="$(dirname "$output_path")"
    mkdir -p "$output_dir"
    
    # Comando pandoc
    local cmd=(
        pandoc
        "$notebook_path"
        -o "$output_path"
        "--pdf-engine=$ENGINE"
        --variable geometry:margin=2cm
        --variable fontsize=11pt
        --variable documentclass=article
        --variable papersize=letter
    )
    
    log_verbose "Ejecutando: ${cmd[*]}"
    
    # Ejecutar conversión con timeout
    local temp_stderr
    temp_stderr=$(mktemp)
    
    if timeout 300 "${cmd[@]}" 2>"$temp_stderr"; then
        # Éxito
        local size_kb=0
        if [[ -f "$output_path" ]]; then
            local size_bytes
            size_bytes=$(stat -c%s "$output_path" 2>/dev/null || echo 0)
            size_kb=$((size_bytes / 1024))
        fi
        
        log_success "Convertido: $(basename "$output_path") (${size_kb}K)"
        ((CONVERTED++))
        rm -f "$temp_stderr"
        return 0
    else
        # Error
        local error_msg
        error_msg=$(cat "$temp_stderr" | head -3 | tr '\n' ' ')
        
        # Simplificar mensajes comunes
        if [[ "$error_msg" == *"font"* ]]; then
            log_warning "Advertencia de fuentes (resultado OK): $(basename "$output_path")"
            # Verificar si el archivo se generó a pesar del warning
            if [[ -f "$output_path" ]]; then
                ((CONVERTED++))
                rm -f "$temp_stderr"
                return 0
            fi
        fi
        
        log_error "Error convertiendo $(basename "$notebook_path"): $error_msg"
        ((FAILED++))
        rm -f "$temp_stderr"
        return 1
    fi
}

# Conversión por lotes
convert_batch() {
    local input_path="$1"
    local notebooks
    
    # Encontrar notebooks
    readarray -t notebooks < <(find_notebooks "$input_path")
    
    if [[ ${#notebooks[@]} -eq 0 ]]; then
        log_error "No se encontraron notebooks en $input_path"
        return 1
    fi
    
    log_info "Encontrados ${#notebooks[@]} notebooks"
    if [[ "$DRY_RUN" == true ]]; then
        log_info "MODO DRY-RUN: No se realizarán conversiones reales"
    fi
    echo "------------------------------------------------------------"
    
    local start_time
    start_time=$(date +%s)
    
    local i=1
    for notebook in "${notebooks[@]}"; do
        # Determinar ruta de salida
        local output_path
        if [[ -n "$OUTPUT_DIR" ]]; then
            local basename_pdf
            basename_pdf="$(basename "${notebook%.ipynb}").pdf"
            output_path="$OUTPUT_DIR/$basename_pdf"
        else
            output_path="${notebook%.ipynb}.pdf"
        fi
        
        # Convertir
        local status="✗"
        if convert_notebook "$notebook" "$output_path"; then
            status="✓"
        fi
        
        printf "[%2d/%d] %s %s\n" "$i" "${#notebooks[@]}" "$status" "$(basename "$notebook")"
        ((i++))
    done
    
    # Resumen final
    local end_time elapsed
    end_time=$(date +%s)
    elapsed=$((end_time - start_time))
    
    echo "------------------------------------------------------------"
    log_info "Completado en ${elapsed}s"
    log_info "Convertidos: $CONVERTED"
    log_info "Ya actualizados: $SKIPPED"
    if [[ $FAILED -gt 0 ]]; then
        log_warning "Fallidos: $FAILED"
    else
        log_info "Fallidos: $FAILED"
    fi
}

# Parsear argumentos
parse_args() {
    local input_path=""
    
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                show_help
                exit 0
                ;;
            --check-deps)
                if check_dependencies; then
                    log_success "Todas las dependencias están instaladas"
                    exit 0
                else
                    exit 1
                fi
                ;;
            -o|--output)
                OUTPUT_DIR="$2"
                shift 2
                ;;
            -e|--engine)
                ENGINE="$2"
                if [[ ! "$ENGINE" =~ ^(xelatex|pdflatex|lualatex)$ ]]; then
                    log_error "Motor no válido: $ENGINE"
                    log_error "Motores válidos: xelatex, pdflatex, lualatex"
                    exit 1
                fi
                shift 2
                ;;
            --no-recursive)
                RECURSIVE=false
                shift
                ;;
            --dry-run)
                DRY_RUN=true
                shift
                ;;
            --force)
                FORCE=true
                shift
                ;;
            -v|--verbose)
                VERBOSE=true
                shift
                ;;
            -*)
                log_error "Opción desconocida: $1"
                echo "Usa -h para ayuda"
                exit 1
                ;;
            *)
                if [[ -z "$input_path" ]]; then
                    input_path="$1"
                else
                    log_error "Argumento extra: $1"
                    exit 1
                fi
                shift
                ;;
        esac
    done
    
    if [[ -z "$input_path" ]]; then
        log_error "Se requiere especificar INPUT (archivo o directorio)"
        echo "Usa -h para ayuda"
        exit 1
    fi
    
    if [[ ! -e "$input_path" ]]; then
        log_error "No existe: $input_path"
        exit 1
    fi
    
    echo "$input_path"
}

# Función principal
main() {
    local input_path
    input_path=$(parse_args "$@")
    
    # Verificar dependencias
    if ! check_dependencies; then
        exit 1
    fi
    
    # Ejecutar conversión
    if ! convert_batch "$input_path"; then
        exit 1
    fi
    
    # Exit code basado en resultados
    if [[ $FAILED -gt 0 ]]; then
        exit 1
    fi
}

# Ejecutar si es llamado directamente
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
