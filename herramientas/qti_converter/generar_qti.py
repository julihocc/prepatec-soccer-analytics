#!/usr/bin/env python3
"""
🚀 ULTIMATE AUTO-DETECTING QTI GENERATOR 🚀
Refactored, DRY-compliant, auto-detecting Canvas QTI converter.

This script automatically detects:
- Block number from directory path (bloque-1, bloque-2, bloque-3) 
- Input filename (banco-preguntas-bloqueX.txt)
- Output filename (banco-preguntas-bloqueX_canvas_qti.zip)

Features:
- Zero code duplication (DRY principle applied)
- Auto-detection of block configuration
- Format validation with detailed error reporting
- Smart change detection with MD5 checksums
- Enhanced logging and progress reporting
- Full compatibility with txttoqti v0.2.0+

Usage:
    python generar_qti.py [--status] [--force] [--interactive]
    
Arguments:
    --status        Show current status without conversion
    --force         Force regeneration even if no changes detected
    --interactive   Enable interactive mode for format validation
"""

import sys
import os
from pathlib import Path

# Smart path detection - find the repository root
script_dir = Path(__file__).parent

# Find herramientas directory by walking up the directory tree
current_dir = script_dir
herramientas_dir = None
for _ in range(5):  # Search up to 5 levels up
    potential_herramientas = current_dir / "herramientas"
    if potential_herramientas.exists() and (potential_herramientas / "qti_converter").exists():
        herramientas_dir = potential_herramientas
        break
    current_dir = current_dir.parent

if herramientas_dir is None:
    print("❌ Error: No se puede encontrar el directorio herramientas/qti_converter/")
    print("   Directorio actual:", script_dir)
    sys.exit(1)

# Add herramientas to path and import
sys.path.insert(0, str(herramientas_dir))

try:
    from qti_converter import QtiConverter
except ImportError as e:
    print("❌ Error: No se puede importar la librería QtiConverter.")
    print(f"   Directorio herramientas: {herramientas_dir}")
    print(f"   Error específico: {e}")
    sys.exit(1)


def parse_arguments():
    """Parse command line arguments."""
    args = {
        'status_only': '--status' in sys.argv,
        'force': '--force' in sys.argv,
        'interactive': '--interactive' in sys.argv,
        'help': '--help' in sys.argv or '-h' in sys.argv
    }
    return args


def show_help():
    """Show help message."""
    print(__doc__)


def main():
    """Función principal - La magia del auto-detection! 🎯"""
    
    args = parse_arguments()
    
    if args['help']:
        show_help()
        return
    
    # Initialize auto-detecting QTI converter
    try:
        converter = QtiConverter(script_path=Path(__file__))
    except Exception as e:
        print(f"❌ Error inicializando convertidor: {e}")
        sys.exit(1)
    
    # Show welcome message with auto-detected info
    if not args['status_only']:
        file_info = converter.get_file_info()
        print(f"🚀 GENERADOR QTI AUTO-DETECTOR v2.0")
        print(f"🎯 Auto-detectado: Bloque {file_info['block_num']} - {file_info['block_description']}")
        print(f"📁 Directorio: {Path.cwd().name}")
        print(f"📄 Archivo fuente: {file_info['txt_file']}")
        print(f"📦 Archivo destino: {file_info['qti_file']}")
        print("-" * 60)
    
    # Handle status-only mode
    if args['status_only']:
        converter.show_status()
        return
    
    # Execute conversion
    success = converter.convert(force=args['force'])
    
    if success:
        print("\n🎉 ¡CONVERSIÓN COMPLETADA CON ÉXITO!")
        print("📤 El archivo QTI está listo para subir a Canvas")
        
        file_info = converter.get_file_info()
        if file_info['qti_exists']:
            qti_path = Path(file_info['qti_file'])
            if qti_path.exists():
                file_size = qti_path.stat().st_size
                print(f"📊 Estadísticas finales:")
                print(f"   • Preguntas: {file_info['question_count']}")
                print(f"   • Tamaño QTI: {file_size:,} bytes")
                print(f"   • Bloque: {file_info['block_num']} ({file_info['block_description']})")
    else:
        print("\n❌ CONVERSIÓN FALLIDA")
        print("🔧 Revisa los errores anteriores e intenta nuevamente")
        sys.exit(1)


if __name__ == "__main__":
    main()