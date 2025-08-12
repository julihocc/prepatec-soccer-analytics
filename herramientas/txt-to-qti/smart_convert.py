#!/usr/bin/env python3
"""
Smart TXT to QTI Converter - Versión Inteligente
Convertidor inteligente que detecta cambios y regenera solo cuando es necesario

Uso:
    python smart_convert.py archivo.txt [archivo_salida.zip]
    python smart_convert.py archivo.txt --force
    python smart_convert.py --status archivo.txt

Características inteligentes:
- 🧠 Detecta automáticamente si hay cambios
- ⚡ Solo regenera cuando es necesario
- 📊 Muestra estado detallado de archivos
- 🔄 Opción de regeneración forzada
- 📁 Auto-navegación de directorios
"""

import sys
import os
import tempfile
from pathlib import Path
import datetime

# Importar los convertidores
from txt_to_csv_direct import TxtToCSVConverter
from csv_to_kansas_qti import KansasQTIGenerator

def get_file_timestamp(file_path):
    """Obtiene el timestamp de modificación de un archivo"""
    try:
        return os.path.getmtime(file_path)
    except OSError:
        return 0

def format_timestamp(timestamp):
    """Formatea timestamp para mostrar"""
    if timestamp == 0:
        return "no existe"
    return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

def get_output_files(txt_file):
    """Genera nombres de archivos de salida basados en el archivo TXT"""
    base_name = Path(txt_file).stem
    dir_name = Path(txt_file).parent
    
    csv_file = dir_name / f"{base_name}_kansas.csv"
    qti_file = dir_name / f"{base_name}_canvas_qti.zip"
    
    return str(csv_file), str(qti_file)

def needs_regeneration(txt_file, csv_file, qti_file):
    """Determina si es necesario regenerar los archivos QTI"""
    
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

def show_file_status(txt_file, csv_file, qti_file):
    """Muestra el estado actual de los archivos"""
    files = {
        "📝 Fuente (TXT)": txt_file,
        "📊 CSV generado": csv_file,
        "📦 QTI Canvas": qti_file
    }
    
    print("📋 Estado actual de archivos:")
    print("-" * 70)
    
    for label, filepath in files.items():
        if os.path.exists(filepath):
            mtime = get_file_timestamp(filepath)
            timestamp = format_timestamp(mtime)
            filename = Path(filepath).name
            print(f"✅ {label:<20}: {filename} ({timestamp})")
        else:
            filename = Path(filepath).name
            print(f"❌ {label:<20}: {filename} (no existe)")
    print()

def convert_with_intelligence(txt_file, output_qti=None, force=False, status_only=False):
    """
    Convierte archivo TXT a QTI con detección inteligente de cambios
    
    Args:
        txt_file: Ruta al archivo .txt con preguntas
        output_qti: Ruta de salida para el archivo .zip QTI (opcional)
        force: Si forzar regeneración aunque no haya cambios
        status_only: Si solo mostrar estado sin convertir
    
    Returns:
        tuple: (archivo_qti_zip, numero_preguntas, regenerated)
    """
    
    # Validar archivo de entrada
    txt_path = Path(txt_file)
    if not txt_path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {txt_file}")
    
    # Generar nombres de archivos de salida
    csv_file, qti_file = get_output_files(txt_file)
    if output_qti:
        qti_file = output_qti
    
    print(f"🎯 Smart Converter - {txt_path.name}")
    print("=" * 60)
    
    # Mostrar estado actual
    show_file_status(txt_file, csv_file, qti_file)
    
    # Si solo queremos ver el estado
    if status_only:
        needs_regen = needs_regeneration(txt_file, csv_file, qti_file)
        if needs_regen:
            print("📝 Evaluación: Necesita regeneración")
        else:
            print("✅ Evaluación: Archivos actualizados")
        return qti_file, 0, False
    
    # Verificar si necesita regeneración
    needs_regen = needs_regeneration(txt_file, csv_file, qti_file)
    
    if not needs_regen and not force:
        print("✅ Los archivos QTI están actualizados.")
        print("   No es necesario regenerar.")
        print()
        print("💡 Opciones:")
        print(f"   python {Path(__file__).name} {txt_file} --force     # Forzar regeneración")
        print(f"   python {Path(__file__).name} --status {txt_file}    # Solo mostrar estado")
        
        # Contar preguntas del archivo existente si existe
        question_count = 0
        if os.path.exists(csv_file):
            try:
                import csv as csv_module
                with open(csv_file, 'r', encoding='utf-8') as f:
                    reader = csv_module.reader(f)
                    question_count = sum(1 for row in reader)
            except:
                question_count = 0
        
        return qti_file, question_count, False
    
    # Proceder con la regeneración
    if force:
        print("🔄 Forzando regeneración...")
    else:
        print("🔄 Los archivos TXT han cambiado. Iniciando regeneración automática...")
    
    print("\n🔄 Regenerando archivos QTI...")
    print("=" * 50)
    
    try:
        # Paso 1: TXT → CSV
        print("📝 Paso 1/2: Convirtiendo TXT → CSV...")
        converter = TxtToCSVConverter()
        result_csv, question_count = converter.convert_to_csv(txt_file, csv_file)
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
        _, qti_count, xml_name = generator.convert_csv_to_kansas_qti(result_csv, qti_file)
        print(f"   ✅ QTI generado: {xml_name}")
        print(f"   ✅ {qti_count} preguntas en el paquete")
        
        # Reporte final
        print("\n" + "=" * 50)
        print("✅ CONVERSIÓN INTELIGENTE COMPLETADA")
        print("=" * 50)
        print(f"📄 Archivo fuente: {Path(txt_file).name}")
        print(f"📊 Preguntas: {question_count}")
        print(f"📝 CSV: {Path(result_csv).name}")
        print(f"📦 QTI: {Path(qti_file).name}")
        print()
        print("📋 Para importar en Canvas:")
        print("1. Ve a tu curso en Canvas")
        print("2. Configuración → Importar contenido del curso")
        print("3. Selecciona 'Paquete QTI'")
        print(f"4. Sube el archivo: {Path(qti_file).name}")
        print("5. Las preguntas aparecerán en tu banco de preguntas")
        
        return qti_file, question_count, True
        
    except Exception as e:
        print(f"\n❌ Error durante la conversión: {e}")
        import traceback
        traceback.print_exc()
        raise

def show_help():
    """Muestra ayuda de uso"""
    print("""
🧠 Smart TXT to QTI Converter - Convertidor Inteligente

CARACTERÍSTICAS INTELIGENTES:
• 🧠 Detecta automáticamente cambios en archivos
• ⚡ Solo regenera cuando es necesario  
• 📊 Muestra estado detallado con timestamps
• 🔄 Opción de regeneración forzada
• 📁 Funciona desde cualquier directorio

USO:
    python smart_convert.py archivo.txt                    # Conversión inteligente
    python smart_convert.py archivo.txt salida.zip         # Con nombre personalizado
    python smart_convert.py archivo.txt --force            # Forzar regeneración
    python smart_convert.py --status archivo.txt           # Solo mostrar estado
    python smart_convert.py --help                         # Esta ayuda

EJEMPLOS:
    # Conversión básica (detecta cambios automáticamente)
    python smart_convert.py preguntas.txt

    # Ver estado sin convertir
    python smart_convert.py --status preguntas.txt
    
    # Forzar regeneración aunque esté actualizado
    python smart_convert.py preguntas.txt --force
    
    # Con nombre de salida personalizado
    python smart_convert.py preguntas.txt mi_examen.zip

VENTAJAS vs convert.py:
✅ Solo regenera si hay cambios reales
✅ Muestra timestamps de todos los archivos  
✅ Feedback más claro sobre qué está pasando
✅ Más rápido para workflows repetitivos
✅ Mejor para integración en scripts automatizados
""")

def main():
    """Función principal"""
    
    args = sys.argv[1:]
    
    if not args or args[0] == '--help':
        show_help()
        return
    
    # Parsing de argumentos
    status_only = False
    force = False
    txt_file = None
    output_qti = None
    
    # Procesar argumentos
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg == '--status':
            status_only = True
            if i + 1 < len(args):
                txt_file = args[i + 1]
                i += 1
        elif arg == '--force':
            force = True
        elif arg.startswith('--'):
            print(f"❌ Opción desconocida: {arg}")
            print("Usa --help para ver opciones disponibles")
            sys.exit(1)
        elif txt_file is None:
            txt_file = arg
        elif output_qti is None:
            output_qti = arg
        else:
            print(f"❌ Demasiados argumentos: {arg}")
            sys.exit(1)
        
        i += 1
    
    if not txt_file:
        print("❌ Error: Debes especificar un archivo TXT")
        print("Uso: python smart_convert.py archivo.txt")
        print("Usa --help para más información")
        sys.exit(1)
    
    try:
        # Ejecutar conversión inteligente
        qti_file, question_count, regenerated = convert_with_intelligence(
            txt_file, 
            output_qti, 
            force=force, 
            status_only=status_only
        )
        
        if not status_only:
            if regenerated:
                print("\n🎉 ¡Archivos QTI actualizados correctamente!")
            else:
                print(f"\n📁 Archivo QTI disponible: {Path(qti_file).name}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()