#!/usr/bin/env python3
"""
Script de regeneración QTI para Banco de Preguntas Bloque 2
Convierte banco-preguntas-bloque2.txt a formato QTI para Canvas

Uso:
    python generar_qti.py [--force] [--status]

Este script usa la librería txttoqti para:
1. Detectar cambios en banco-preguntas-bloque2.txt
2. Regenerar automáticamente QTI solo si es necesario
3. Proporcionar feedback claro sobre el estado
"""

import os
import sys
from pathlib import Path

# Importar la librería txttoqti
try:
    from txttoqti import SmartConverter
except ImportError as e:
    print(f"❌ Error: No se puede importar la librería txttoqti.")
    print(f"   Instala con: pip install -e .")
    print(f"   Error específico: {e}")
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
            print(f"❌ Argumento desconocido: {arg}")
            print("Usa --help para ver opciones disponibles")
            sys.exit(1)
    
    return force, status_only

def print_help():
    """Muestra ayuda de uso"""
    print("""
🎯 Generador QTI - Banco de Preguntas Bloque 1

USO:
    python generar_qti.py              # Regenera SIEMPRE (por defecto)
    python generar_qti.py --no-force   # Solo regenera si hay cambios
    python generar_qti.py --status     # Solo mostrar estado
    python generar_qti.py --help       # Esta ayuda

DESCRIPCIÓN:
Este script usa la solución inteligente generalizada para convertir
banco-preguntas-bloque1.txt a formato QTI compatible con Canvas.

COMPORTAMIENTO POR DEFECTO:
• 🔄 SIEMPRE regenera archivos QTI (--force por defecto)
• 📊 Muestra estado detallado con timestamps
• 📁 Auto-navegación de directorios

OPCIONES:
• --no-force   Comportamiento inteligente (solo regenera si hay cambios)
• --status     Solo mostrar estado de archivos sin convertir
• --help       Mostrar esta ayuda

ARCHIVOS:
• banco-preguntas-bloque1.txt         → Archivo fuente
• banco-preguntas-bloque1_kansas.csv  → CSV intermedio generado
• banco-preguntas-bloque1_canvas_qti.zip → Paquete QTI para Canvas
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
        print(f"📁 Cambiando al directorio: {script_dir}")
        os.chdir(script_dir)
    
    # Archivo de trabajo específico
    txt_file = "banco-preguntas-bloque2.txt"
    
    # Verificar que existe el archivo fuente
    if not os.path.exists(txt_file):
        print("❌ Error: Archivo faltante en el directorio:")
        print(f"   {script_dir}")
        print(f"   {txt_file}")
        print(f"\n💡 Asegúrate de que el archivo {txt_file} exista")
        sys.exit(1)
    
    try:
        # Usar el SmartConverter de txttoqti
        converter = SmartConverter()
        qti_file, question_count, regenerated = converter.convert_with_intelligence(
            txt_file,
            output_file=None,  # Usar nombres por defecto
            force=force,
            status_only=status_only
        )
        
        # Mensaje final según el resultado
        if not status_only:
            if regenerated:
                print(f"\n🎉 ¡{question_count} preguntas convertidas exitosamente!")
                print(f"📦 QTI generado: {Path(qti_file).name}")
            else:
                print(f"\n📁 Archivo QTI disponible: {Path(qti_file).name}")
                print(f"✅ {question_count} preguntas - sin cambios necesarios")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()