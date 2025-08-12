#!/usr/bin/env python3
"""
Script de regeneración QTI para Banco de Preguntas Bloque 1
Convierte banco-preguntas-bloque1.txt a formato QTI para Canvas

Uso:
    python generar_qti.py

Este script:
1. Detecta cambios en banco-preguntas-bloque1.txt
2. Regenera automáticamente CSV y QTI si es necesario
3. Proporciona feedback claro sobre el estado
"""

import os
import sys
from pathlib import Path

# Agregar herramientas al path
current_dir = Path(__file__).parent
project_root = current_dir.parent.parent.parent
tools_path = project_root / "herramientas" / "txt-to-qti"
sys.path.insert(0, str(tools_path))

# Importar convertidores
try:
    from txt_to_csv_direct import TxtToCSVConverter
    from csv_to_kansas_qti import KansasQTIGenerator
except ImportError as e:
    print(f"❌ Error: No se pueden importar las herramientas de conversión.")
    print(f"   Verifica que exista: {tools_path}")
    print(f"   Error específico: {e}")
    sys.exit(1)

def get_file_timestamp(file_path):
    """Obtiene el timestamp de modificación de un archivo"""
    try:
        return os.path.getmtime(file_path)
    except OSError:
        return 0

def needs_regeneration():
    """Determina si es necesario regenerar los archivos QTI"""
    txt_file = "banco-preguntas-bloque1.txt"
    csv_file = "banco-preguntas-bloque1_kansas.csv"
    qti_file = "banco-preguntas-bloque1_canvas_qti.zip"
    
    # Verificar que existe el archivo fuente
    if not os.path.exists(txt_file):
        print(f"❌ Error: No se encuentra {txt_file}")
        return False
    
    txt_time = get_file_timestamp(txt_file)
    csv_time = get_file_timestamp(csv_file)
    qti_time = get_file_timestamp(qti_file)
    
    # Si no existen los archivos de salida, necesita regeneración
    if not os.path.exists(csv_file) or not os.path.exists(qti_file):
        return True
    
    # Si el TXT es más nuevo que los archivos generados, necesita regeneración
    if txt_time > csv_time or txt_time > qti_time:
        return True
    
    return False

def show_status():
    """Muestra el estado actual de los archivos"""
    files = {
        "📝 Fuente (TXT)": "banco-preguntas-bloque1.txt",
        "📊 CSV generado": "banco-preguntas-bloque1_kansas.csv", 
        "📦 QTI Canvas": "banco-preguntas-bloque1_canvas_qti.zip"
    }
    
    print("📋 Estado actual de archivos:")
    print("-" * 50)
    
    for label, filename in files.items():
        if os.path.exists(filename):
            mtime = os.path.getmtime(filename)
            import datetime
            timestamp = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
            print(f"✅ {label:<20}: {filename} ({timestamp})")
        else:
            print(f"❌ {label:<20}: {filename} (no existe)")
    print()

def regenerate_qti():
    """Regenera los archivos CSV y QTI"""
    txt_file = "banco-preguntas-bloque1.txt"
    
    print("🔄 Regenerando archivos QTI...")
    print("=" * 50)
    
    try:
        # Paso 1: TXT → CSV
        print("📝 Paso 1/2: Convirtiendo TXT → CSV...")
        converter = TxtToCSVConverter()
        csv_file, question_count = converter.convert_to_csv(txt_file)
        print(f"   ✅ {question_count} preguntas procesadas")
        
        # Mostrar advertencias si las hay
        issues = converter.validate_questions(converter.questions)
        if issues:
            print(f"   ⚠️  {len(issues)} advertencias:")
            for issue in issues[:3]:
                print(f"      - {issue}")
            if len(issues) > 3:
                print(f"      ... y {len(issues) - 3} más")
        
        # Paso 2: CSV → QTI
        print("🎯 Paso 2/2: Generando paquete QTI...")
        generator = KansasQTIGenerator()
        qti_file = "banco-preguntas-bloque1_canvas_qti.zip"
        result_qti, qti_count, xml_name = generator.convert_csv_to_kansas_qti(csv_file, qti_file)
        print(f"   ✅ QTI generado: {xml_name}")
        print(f"   ✅ {qti_count} preguntas en el paquete")
        
        # Reporte final
        print("\n" + "=" * 50)
        print("✅ REGENERACIÓN COMPLETADA")
        print("=" * 50)
        print(f"📄 Archivo fuente: {txt_file}")
        print(f"📊 Preguntas: {question_count}")
        print(f"📝 CSV: {csv_file}")
        print(f"📦 QTI: {qti_file}")
        print()
        print("📋 Para usar en Canvas:")
        print(f"   → Sube el archivo: {qti_file}")
        print("   → Configuración → Importar contenido → Paquete QTI")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error durante la regeneración: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Función principal"""
    print("🎯 Generador QTI - Banco Preguntas Bloque 1")
    print("=" * 50)
    
    # Verificar directorio actual
    current_dir = os.getcwd()
    expected_files = ["banco-preguntas-bloque1.txt"]
    
    if not all(os.path.exists(f) for f in expected_files):
        print("❌ Error: Este script debe ejecutarse desde el directorio:")
        print("   evaluaciones/bloque-1/canvas/")
        print(f"\nDirectorio actual: {current_dir}")
        print("Archivos esperados:", ", ".join(expected_files))
        sys.exit(1)
    
    # Mostrar estado actual
    show_status()
    
    # Verificar si necesita regeneración
    if needs_regeneration():
        print("🔄 Los archivos TXT han cambiado o faltan archivos QTI.")
        print("   Iniciando regeneración automática...\n")
        
        success = regenerate_qti()
        if success:
            print("\n🎉 ¡Archivos QTI actualizados correctamente!")
        else:
            print("\n💥 Error durante la regeneración.")
            sys.exit(1)
    else:
        print("✅ Los archivos QTI están actualizados.")
        print("   No es necesario regenerar.")
        print()
        print("💡 Si quieres forzar la regeneración:")
        print("   python generar_qti.py --force")
        
        # Opción para forzar regeneración
        if len(sys.argv) > 1 and sys.argv[1] == "--force":
            print("\n🔄 Forzando regeneración...")
            success = regenerate_qti()
            if not success:
                sys.exit(1)

if __name__ == "__main__":
    main()