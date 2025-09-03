#!/usr/bin/env python3
"""
🚀 QTI GENERATOR - txttoqti v0.3.0 Wrapper
Minimal wrapper that uses txttoqti-edu CLI for backward compatibility.

This script provides the same interface as before but uses the official
txttoqti v0.3.0 educational module instead of local implementation.

Features:
- Same command-line interface for backward compatibility
- Uses txttoqti v0.3.0 educational auto-detection system
- Zero maintenance - all functionality handled by txttoqti library
- Enhanced error handling and validation

Usage:
    python generar_qti.py [--status] [--force] [--interactive] [--help]
    
Arguments:
    --status        Show current status without conversion
    --force         Force regeneration even if no changes detected
    --interactive   Enable interactive mode for format validation
    --help          Show help message
"""

import subprocess
import sys
import os
from pathlib import Path


def find_txttoqti_edu():
    """Find txttoqti-edu command in virtual environment or system PATH."""
    # Try virtual environment first
    script_dir = Path(__file__).parent
    
    # Walk up to find repository root with .venv
    current_dir = script_dir
    for _ in range(10):  # Search up to 10 levels up
        venv_bin = current_dir / ".venv" / "bin" / "txttoqti-edu"
        if venv_bin.exists():
            return str(venv_bin)
        current_dir = current_dir.parent
        if current_dir == current_dir.parent:  # Reached filesystem root
            break
    
    # Try system PATH
    try:
        result = subprocess.run(['which', 'txttoqti-edu'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    except:
        pass
    
    return None


def show_help():
    """Show help message."""
    print(__doc__)


def main():
    """Main function - wrapper for txttoqti-edu."""
    
    # Handle help locally for better messaging
    if '--help' in sys.argv or '-h' in sys.argv:
        show_help()
        return
    
    # Find txttoqti-edu command
    txttoqti_edu_path = find_txttoqti_edu()
    
    if not txttoqti_edu_path:
        print("❌ Error: txttoqti-edu no encontrado")
        print("   Instala txttoqti v0.3.0+: pip install git+https://github.com/julihocc/txttoqti.git@v0.3.0")
        print("   O activa el entorno virtual: source .venv/bin/activate")
        sys.exit(1)
    
    # Pass all arguments to txttoqti-edu
    cmd_args = [txttoqti_edu_path] + sys.argv[1:]
    
    try:
        result = subprocess.run(cmd_args)
        sys.exit(result.returncode)
    except Exception as e:
        print(f"❌ Error ejecutando txttoqti-edu: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

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