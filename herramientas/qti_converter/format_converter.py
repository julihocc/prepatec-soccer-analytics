"""
Format conversion utilities for QTI question banks.
Converts from internal format (Q1: A) B) C) D) RESPUESTA: X) to txttoqti format.
"""

import re
from typing import List, Tuple


class FormatConverter:
    """Converts between different question bank formats."""
    
    @staticmethod
    def convert_to_txttoqti_format(input_file: str, output_file: str) -> str:
        """
        Convierte formato Q1: A) B) C) D) RESPUESTA: X al formato txttoqti.
        
        Args:
            input_file: Archivo fuente con formato interno
            output_file: Archivo destino con formato txttoqti
            
        Returns:
            str: Ruta del archivo convertido
        """
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
            
            # Buscar patrón de pregunta Q1:, Q2:, etc.
            question_match = re.match(r'^Q(\d+):\s*(.+)$', line)
            if question_match:
                question_num = question_match.group(1)
                question_text = question_match.group(2)
                
                # Convertir Q1: a 1.
                converted_lines.append(f"{question_num}. {question_text}")
                i += 1
                
                # Procesar las opciones y respuesta
                choices = []
                answer_line = None
                
                while i < len(lines):
                    line = lines[i].strip()
                    if not line:
                        i += 1
                        continue
                    
                    # Buscar patrón de opciones A), B), C), D)
                    choice_match = re.match(r'^([ABCD])\)\s*(.+)$', line)
                    if choice_match:
                        choice_letter = choice_match.group(1).lower()
                        choice_text = choice_match.group(2)
                        choices.append(f"{choice_letter}) {choice_text}")
                        i += 1
                        continue
                    
                    # Buscar patrón de respuesta RESPUESTA: X
                    answer_match = re.match(r'^RESPUESTA:\s*([ABCD])$', line)
                    if answer_match:
                        answer_letter = answer_match.group(1).lower()
                        answer_line = f"Respuesta correcta: {answer_letter}"
                        i += 1
                        break
                    
                    break
                
                # Agregar contenido convertido
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
    
    @staticmethod
    def validate_question_format(content: str) -> Tuple[bool, List[str]]:
        """
        Valida el formato de las preguntas.
        
        Args:
            content: Contenido del archivo a validar
            
        Returns:
            tuple: (is_valid, list_of_errors)
        """
        errors = []
        lines = content.strip().split('\n')
        
        question_pattern = re.compile(r'^Q(\d+):\s*(.+)$')
        choice_pattern = re.compile(r'^([ABCD])\)\s*(.+)$')
        answer_pattern = re.compile(r'^RESPUESTA:\s*([ABCD])$')
        
        current_question = None
        found_choices = set()
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue
                
            if question_pattern.match(line):
                current_question = line_num
                found_choices = set()
            elif choice_pattern.match(line):
                if current_question is None:
                    errors.append(f"Línea {line_num}: Opción encontrada sin pregunta")
                else:
                    choice = choice_pattern.match(line).group(1)
                    if choice in found_choices:
                        errors.append(f"Línea {line_num}: Opción {choice} duplicada")
                    found_choices.add(choice)
            elif answer_pattern.match(line):
                if current_question is None:
                    errors.append(f"Línea {line_num}: Respuesta encontrada sin pregunta")
                else:
                    answer = answer_pattern.match(line).group(1)
                    if answer not in found_choices:
                        errors.append(f"Línea {line_num}: Respuesta {answer} no corresponde a ninguna opción")
        
        return len(errors) == 0, errors