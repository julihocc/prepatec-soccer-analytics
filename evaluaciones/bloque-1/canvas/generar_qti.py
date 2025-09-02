#!/usr/bin/env python3
"""
Script de regeneración QTI para Banco de Preguntas Bloque 1
Convierte banco-preguntas-bloque1.txt a formato QTI para Canvas

Uso:
    python generar_qti.py [--status]
"""

import os
import sys
import hashlib
import re
from pathlib import Path

# Importar la librería txttoqti
try:
    from txttoqti import TxtToQtiConverter
except ImportError as e:
    print("❌ Error: No se puede importar la librería txttoqti.")
    print("   Instala con: uv add git+https://github.com/julihocc/txttoqti.git@main")
    print(f"   Error específico: {e}")
    sys.exit(1)


def convert_to_txttoqti_format(input_file, output_file):
    """Convierte formato Q1: A) B) C) D) RESPUESTA: X al formato txttoqti"""
    with open(input_file, 'r', encoding='utf-8') as f:
        input_text = f.read()
    
    lines = input_text.strip().split('\n')
    converted_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if not line:
            converted_lines.append('')
            i += 1
            continue
        
        # Check for question pattern Q1:, Q2:, etc.
        question_match = re.match(r'^Q(\d+):\s*(.+)$', line)
        if question_match:
            question_num = question_match.group(1)
            question_text = question_match.group(2)
            
            # Convert Q1: to 1.
            converted_lines.append(f"{question_num}. {question_text}")
            i += 1
            
            # Process the choices and answer
            choices = []
            answer_line = None
            
            while i < len(lines):
                line = lines[i].strip()
                if not line:
                    i += 1
                    continue
                
                # Check for choice pattern A), B), C), D)
                choice_match = re.match(r'^([ABCD])\)\s*(.+)$', line)
                if choice_match:
                    choice_letter = choice_match.group(1).lower()
                    choice_text = choice_match.group(2)
                    choices.append(f"{choice_letter}) {choice_text}")
                    i += 1
                    continue
                
                # Check for answer pattern RESPUESTA: X
                answer_match = re.match(r'^RESPUESTA:\s*([ABCD])$', line)
                if answer_match:
                    answer_letter = answer_match.group(1).lower()
                    answer_line = f"Respuesta correcta: {answer_letter}"
                    i += 1
                    break
                
                break
            
            # Add converted content
            converted_lines.extend(choices)
            if answer_line:
                converted_lines.append(answer_line)
            converted_lines.append('')
        else:
            converted_lines.append(line)
            i += 1
    
    converted_text = '\n'.join(converted_lines)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(converted_text)
    
    return output_file


def count_questions(filepath):
    """Cuenta preguntas en el archivo"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        questions = re.findall(r'^Q\d+:', content, re.MULTILINE)
        return len(questions)
    except Exception:
        return 0


def file_changed(filepath, checksum_file=None):
    """Verifica si un archivo ha cambiado"""
    if checksum_file is None:
        checksum_file = filepath + ".checksum"
    
    if not os.path.exists(filepath):
        return True
    
    with open(filepath, 'rb') as f:
        current_checksum = hashlib.md5(f.read()).hexdigest()
    
    if os.path.exists(checksum_file):
        with open(checksum_file, 'r') as f:
            previous_checksum = f.read().strip()
        
        if current_checksum == previous_checksum:
            return False
    
    with open(checksum_file, 'w') as f:
        f.write(current_checksum)
    
    return True


def main():
    """Función principal"""
    
    # Procesar argumentos
    status_only = "--status" in sys.argv
    force = not ("--no-force" in sys.argv)
    
    # Archivos
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    txt_file = "banco-preguntas-bloque1.txt"
    qti_file = "banco-preguntas-bloque1_canvas_qti.zip"
    
    if not os.path.exists(txt_file):
        print(f"❌ Error: Archivo {txt_file} no encontrado")
        sys.exit(1)
    
    question_count = count_questions(txt_file)
    
    if status_only:
        print(f"📊 ESTADO DEL ARCHIVO:")
        print(f"   Fuente: {txt_file}")
        print(f"   Preguntas: {question_count}")
        print(f"   QTI: {qti_file} {'(existe)' if os.path.exists(qti_file) else '(no existe)'}")
        if not force and not file_changed(txt_file):
            print("✅ Sin cambios necesarios")
        else:
            print("🔄 Regeneración requerida")
        return
    
    # Verificar si necesita regeneración
    needs_regeneration = force or file_changed(txt_file) or not os.path.exists(qti_file)
    
    if not needs_regeneration:
        print(f"✅ QTI está actualizado: {qti_file}")
        print(f"📊 {question_count} preguntas - sin cambios necesarios")
        return
    
    try:
        # Convertir formato
        print(f"🔄 Convirtiendo formato de {question_count} preguntas...")
        converted_file = txt_file.replace('.txt', '_txttoqti_format.txt')
        convert_to_txttoqti_format(txt_file, converted_file)
        print(f"✅ Formato convertido")
        
        # Generar QTI
        print(f"🔄 Generando QTI...")
        converter = TxtToQtiConverter()
        result = converter.convert_file(converted_file, qti_file)
        
        if result and os.path.exists(result):
            print(f"\n🎉 ¡{question_count} preguntas convertidas exitosamente!")
            print(f"📦 QTI generado: {Path(result).name}")
            file_size = Path(result).stat().st_size
            print(f"📏 Tamaño: {file_size} bytes")
            
            # Limpiar archivo temporal
            try:
                os.unlink(converted_file)
            except Exception:
                pass
        else:
            print("❌ Error: No se pudo generar el archivo QTI")
            sys.exit(1)
        
    except Exception as e:
        print(f"\n❌ Error durante la conversión: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
