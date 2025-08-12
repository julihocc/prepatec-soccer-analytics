#!/usr/bin/env python3
"""
Script de regeneración QTI para Banco de Preguntas Bloque 3
Convierte banco-preguntas-bloque3.txt a formato QTI para Canvas

Uso:
    python generar_qti.py [--no-force] [--status] [--help]

Este script usa la solución inteligente generalizada para:
1. Detectar cambios en banco-preguntas-bloque3.txt
2. Regenerar automáticamente CSV y QTI solo si es necesario
3. Proporcionar feedback claro sobre el estado
"""

import os
import sys
from pathlib import Path

# Agregar herramientas al path
current_dir = Path(__file__).parent
project_root = current_dir.parent.parent.parent
tools_path = project_root / "herramientas" / "txt-to-qti"
sys.path.insert(0, str(tools_path))

# Importar el convertidor inteligente
try:
    from smart_convert import convert_with_intelligence
except ImportError as e:
    print("ERROR: No se puede importar el convertidor inteligente.")
    print(f"Verifica que exista: {tools_path}/smart_convert.py")
    print(f"Error específico: {e}")
    sys.exit(1)

def process_arguments():
    """Procesa argumentos de línea de comandos"""
    force = True  # Por defecto siempre fuerza regeneración
    status_only = False
    
    for arg in sys.argv[1:]:
        if arg == "--no-force":
            force = False  # Opción para desactivar regeneración forzada
        elif arg == "--status":
            status_only = True
        elif arg == "--help":
            print_help()
            sys.exit(0)
        else:
            print(f"ERROR: Argumento desconocido: {arg}")
            print("Usa --help para ver opciones disponibles")
            sys.exit(1)
    
    return force, status_only

def print_help():
    """Muestra ayuda de uso"""
    print("""
Generador QTI - Banco de Preguntas Bloque 3

USO:
    python generar_qti.py              # Regenera SIEMPRE (por defecto)
    python generar_qti.py --no-force   # Solo regenera si hay cambios
    python generar_qti.py --status     # Solo mostrar estado
    python generar_qti.py --help       # Esta ayuda

DESCRIPCIÓN:
Este script usa la solución inteligente generalizada para convertir
banco-preguntas-bloque3.txt a formato QTI compatible con Canvas.

COMPORTAMIENTO POR DEFECTO:
- SIEMPRE regenera archivos QTI (--force por defecto)
- Muestra estado detallado con timestamps
- Auto-navegación de directorios

OPCIONES:
- --no-force   Comportamiento inteligente (solo regenera si hay cambios)
- --status     Solo mostrar estado de archivos sin convertir
- --help       Mostrar esta ayuda

ARCHIVOS:
- banco-preguntas-bloque3.txt         -> Archivo fuente
- banco-preguntas-bloque3_kansas.csv  -> CSV intermedio generado
- banco-preguntas-bloque3_canvas_qti.zip -> Paquete QTI para Canvas
""")

def main():
    """Función principal"""
    
    # Procesar argumentos
    force, status_only = process_arguments()
    
    # Cambiar al directorio del script si no estamos ahí
    script_dir = Path(__file__).parent
    current_dir = Path.cwd()
    
    # Si no estamos en el directorio correcto, cambiar ahí
    if current_dir != script_dir:
        print(f"Cambiando al directorio: {script_dir}")
        os.chdir(script_dir)
    
    # Archivo de trabajo específico
    txt_file = "banco-preguntas-bloque3.txt"
    
    # Verificar que existe el archivo fuente
    if not os.path.exists(txt_file):
        print("ERROR: Archivo faltante en el directorio:")
        print(f"   {script_dir}")
        print(f"   {txt_file}")
        print(f"\nAsegurate de que el archivo {txt_file} exista")
        sys.exit(1)
    
    try:
        # Usar el convertidor inteligente generalizado
        qti_file, _, regenerated = convert_with_intelligence(
            txt_file,
            output_qti=None,  # Usar nombres por defecto
            force=force,
            status_only=status_only
        )
        
        # Mensaje final según el resultado
        if not status_only:
            if regenerated:
                print("\nArchivos QTI actualizados usando solucion inteligente")
            else:
                print(f"\nArchivo QTI disponible: {Path(qti_file).name}")
                print("(Usada solucion inteligente - sin cambios necesarios)")
        
    except Exception as e:
        print(f"\nERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()