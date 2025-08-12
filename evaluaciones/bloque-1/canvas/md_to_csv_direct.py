#!/usr/bin/env python3
"""
Generador directo de CSV para Kansas State Converter desde MD
Convierte formato MD simplificado directamente a CSV sin JSON intermedio

Uso:
    python md_to_csv_direct.py banco-preguntas-bloque1.md

Genera:
    - Archivo CSV compatible con Kansas State Converter
    - Sin encabezados (como requiere el conversor)
    - Formato: MC,,1.0,pregunta,respuesta_num,opcion_a,opcion_b,opcion_c,opcion_d
"""

import re
import csv
import os
import sys

class MDToCSVConverter:
    def __init__(self):
        self.questions = []
        
    def clean_text(self, text):
        """Limpia texto para CSV eliminando caracteres problemáticos"""
        if not text:
            return ""
        
        # Limpiar texto básico
        text = str(text).strip()
        
        # Normalizar espacios
        text = re.sub(r'\s+', ' ', text)
        
        return text
    
    def map_answer_to_number(self, answer_letter, options):
        """Mapea letra de respuesta (A,B,C,D) a número (1,2,3,4)"""
        answer_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
        return str(answer_map.get(answer_letter, 1))
    
    def parse_md_file(self, md_file):
        """Parse archivo MD y extrae preguntas directamente"""
        if not os.path.exists(md_file):
            raise FileNotFoundError(f"Archivo no encontrado: {md_file}")
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        current_question = None
        
        for line in lines:
            line = line.strip()
            
            if not line:
                continue
            
            # Detectar pregunta (Q1:, Q2:, etc.)
            if re.match(r'^Q\d+:', line):
                # Guardar pregunta anterior si existe
                if current_question:
                    self._save_current_question(current_question)
                
                # Nueva pregunta
                question_num = int(re.search(r'^Q(\d+):', line).group(1))
                question_text = line.split(':', 1)[1].strip()
                
                current_question = {
                    'number': question_num,
                    'text': self.clean_text(question_text),
                    'options': [],
                    'correct_answer': None
                }
                continue
            
            # Detectar opciones (A), B), C), D))
            if re.match(r'^[ABCDE]\)', line) and current_question:
                option_text = line.split(')', 1)[1].strip()
                current_question['options'].append(self.clean_text(option_text))
                continue
            
            # Detectar respuesta correcta (RESPUESTA: B)
            if line.startswith('RESPUESTA:') and current_question:
                answer_letter = line.split(':', 1)[1].strip()
                current_question['correct_answer'] = answer_letter
                continue
        
        # Guardar última pregunta
        if current_question:
            self._save_current_question(current_question)
        
        return self.questions
    
    def _save_current_question(self, question):
        """Valida y guarda pregunta actual"""
        # Validar que tenga respuesta correcta
        if not question['correct_answer']:
            print(f"⚠️  Pregunta {question['number']}: Sin respuesta correcta")
            return
        
        # Validar que tenga al menos 2 opciones
        if len(question['options']) < 2:
            print(f"⚠️  Pregunta {question['number']}: Menos de 2 opciones")
            return
        
        # Asegurar exactamente 4 opciones (completar con vacías si faltan)
        while len(question['options']) < 4:
            question['options'].append("")
        
        # Limitar a 4 opciones máximo
        question['options'] = question['options'][:4]
        
        self.questions.append(question)
    
    def generate_csv_row(self, question):
        """Genera fila CSV para una pregunta"""
        # Formato Kansas State: Tipo, Vacío, Puntos, Pregunta, Respuesta, A, B, C, D
        
        question_type = "MC"  # Multiple Choice
        unused_column = ""    # Columna B vacía pero requerida
        points = "1.0"        # Puntos por pregunta
        question_text = question['text']
        correct_answer_num = self.map_answer_to_number(
            question['correct_answer'], 
            question['options']
        )
        
        # Construir fila
        row = [
            question_type,           # A: MC
            unused_column,          # B: vacía
            points,                 # C: 1.0
            question_text,          # D: texto pregunta
            correct_answer_num,     # E: número respuesta correcta
            question['options'][0], # F: opción A
            question['options'][1], # G: opción B
            question['options'][2], # H: opción C
            question['options'][3]  # I: opción D
        ]
        
        return row
    
    def convert_to_csv(self, md_file, output_file=None):
        """Convierte archivo MD directamente a CSV"""
        
        # Parse del archivo MD
        questions = self.parse_md_file(md_file)
        
        if not questions:
            raise ValueError("No se encontraron preguntas válidas en el archivo MD")
        
        # Generar nombre de salida
        if output_file is None:
            base_name = os.path.splitext(os.path.basename(md_file))[0]
            output_file = f"{base_name}_kansas.csv"
        
        # Escribir CSV (sin encabezados)
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Procesar cada pregunta
            for question in questions:
                row = self.generate_csv_row(question)
                writer.writerow(row)
        
        return output_file, len(questions)
    
    def validate_questions(self, questions):
        """Valida estructura de preguntas"""
        issues = []
        
        for q in questions:
            # Verificar numeración secuencial
            expected_num = questions.index(q) + 1
            if q['number'] != expected_num:
                issues.append(f"Pregunta {q['number']}: Numeración no secuencial (esperado {expected_num})")
            
            # Verificar opciones no vacías
            empty_options = sum(1 for opt in q['options'][:4] if not opt.strip())
            if empty_options > 2:  # Permitir máximo 2 opciones vacías
                issues.append(f"Pregunta {q['number']}: Demasiadas opciones vacías ({empty_options})")
        
        return issues

def main():
    if len(sys.argv) != 2:
        print("Uso: python md_to_csv_direct.py <archivo_md>")
        print("Ejemplo: python md_to_csv_direct.py banco-preguntas-bloque1.md")
        sys.exit(1)
    
    md_file = sys.argv[1]
    
    try:
        converter = MDToCSVConverter()
        output_file, question_count = converter.convert_to_csv(md_file)
        
        # Validar preguntas procesadas
        issues = converter.validate_questions(converter.questions)
        
        print(f"✅ Conversión MD → CSV completada")
        print(f"✅ Archivo MD: {md_file}")
        print(f"✅ CSV generado: {output_file}")
        print(f"✅ Preguntas procesadas: {question_count}")
        
        if issues:
            print(f"\n⚠️  Advertencias encontradas:")
            for issue in issues[:5]:  # Mostrar primeros 5
                print(f"   - {issue}")
            if len(issues) > 5:
                print(f"   ... y {len(issues) - 5} más")
        else:
            print("✅ Sin problemas detectados")
        
        print(f"\n📋 Instrucciones:")
        print(f"1. Ve a: https://canvas.k-state.edu/info/tools/scantron/faq/build-a-scantron-quiz.html")
        print(f"2. Usa el 'Kansas State Classic to Canvas (QTI 2.0) Converter'")
        print(f"3. Sube el archivo: {output_file}")
        print(f"4. Descarga el ZIP generado")
        print(f"5. Importa el ZIP en Canvas como Paquete QTI")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()