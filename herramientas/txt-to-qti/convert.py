#!/usr/bin/env python3
"""
Convertidor integrado TXT → QTI para Canvas
Script principal que combina ambas etapas de conversión

Uso:
    python convert.py archivo.txt [archivo_salida.zip]

Este script ejecuta automáticamente:
1. TXT → CSV (usando txt_to_csv_direct.py)
2. CSV → QTI (usando csv_to_kansas_qti.py)

Genera un archivo ZIP listo para importar en Canvas LMS.
"""

import sys
import os
import tempfile
from pathlib import Path

# Importar los convertidores
from txt_to_csv_direct import TxtToCSVConverter
from csv_to_kansas_qti import KansasQTIGenerator

def convert_txt_to_qti(txt_file, output_qti=None, keep_csv=False):
    """
    Convierte archivo TXT directamente a QTI ZIP
    
    Args:
        txt_file: Ruta al archivo .txt con preguntas
        output_qti: Ruta de salida para el archivo .zip QTI (opcional)
        keep_csv: Si mantener el archivo CSV intermedio
    
    Returns:
        tuple: (archivo_qti_zip, numero_preguntas, archivo_csv_temporal)
    """
    
    # Validar archivo de entrada
    if not os.path.exists(txt_file):
        raise FileNotFoundError(f"Archivo no encontrado: {txt_file}")
    
    print(f"🔄 Iniciando conversión: {txt_file}")
    
    # Etapa 1: TXT → CSV
    print("📝 Paso 1/2: Convirtiendo TXT → CSV...")
    converter = TxtToCSVConverter()
    
    # Usar archivo temporal para CSV si no se va a mantener
    if keep_csv:
        csv_file, question_count = converter.convert_to_csv(txt_file)
    else:
        # Crear archivo CSV temporal
        base_name = Path(txt_file).stem
        temp_csv = tempfile.NamedTemporaryFile(
            mode='w', 
            suffix='.csv', 
            prefix=f"{base_name}_",
            delete=False
        )
        temp_csv.close()
        csv_file, question_count = converter.convert_to_csv(txt_file, temp_csv.name)
    
    print(f"   ✅ {question_count} preguntas procesadas")
    
    # Validar preguntas
    issues = converter.validate_questions(converter.questions)
    if issues:
        print(f"   ⚠️  {len(issues)} advertencias encontradas:")
        for issue in issues[:3]:  # Mostrar primeras 3
            print(f"      - {issue}")
        if len(issues) > 3:
            print(f"      ... y {len(issues) - 3} más")
    
    # Etapa 2: CSV → QTI
    print("🎯 Paso 2/2: Generando paquete QTI...")
    generator = KansasQTIGenerator()
    
    # Generar nombre de salida si no se especifica
    if output_qti is None:
        base_name = Path(txt_file).stem
        output_qti = f"{base_name}_canvas_qti.zip"
    
    qti_file, qti_count, xml_name = generator.convert_csv_to_kansas_qti(csv_file, output_qti)
    
    print(f"   ✅ QTI generado: {xml_name}")
    print(f"   ✅ {qti_count} preguntas en el paquete")
    
    # Limpiar archivo CSV temporal si no se mantiene
    csv_to_return = csv_file
    if not keep_csv and csv_file != f"{Path(txt_file).stem}_kansas.csv":
        try:
            os.unlink(csv_file)
            csv_to_return = None
        except:
            pass  # Si no se puede eliminar, no es crítico
    
    return qti_file, question_count, csv_to_return

def main():
    """Función principal del script"""
    
    if len(sys.argv) < 2:
        print("Uso: python convert.py <archivo.txt> [archivo_salida.zip]")
        print()
        print("Ejemplos:")
        print("  python convert.py preguntas.txt")
        print("  python convert.py preguntas.txt mi_examen.zip")
        print("  python convert.py banco-preguntas-bloque1.txt")
        print()
        print("El script genera un archivo ZIP listo para importar en Canvas LMS.")
        sys.exit(1)
    
    txt_file = sys.argv[1]
    output_qti = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        # Conversión completa
        qti_file, question_count, csv_file = convert_txt_to_qti(
            txt_file, 
            output_qti, 
            keep_csv=True  # Mantener CSV para debugging
        )
        
        # Reporte final
        print("\n" + "="*50)
        print("✅ CONVERSIÓN COMPLETADA")
        print("="*50)
        print(f"📄 Archivo original: {txt_file}")
        print(f"📊 Preguntas procesadas: {question_count}")
        if csv_file:
            print(f"📝 CSV intermedio: {csv_file}")
        print(f"📦 Paquete QTI: {qti_file}")
        print()
        print("📋 Para importar en Canvas:")
        print("1. Ve a tu curso en Canvas")
        print("2. Configuración → Importar contenido del curso")
        print("3. Selecciona 'Paquete QTI'")
        print(f"4. Sube el archivo: {qti_file}")
        print("5. Las preguntas aparecerán en tu banco de preguntas")
        print()
        print("🎉 ¡Listo para usar!")
        
    except Exception as e:
        print(f"\n❌ Error durante la conversión: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()