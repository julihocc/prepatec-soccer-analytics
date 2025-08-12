#!/usr/bin/env python3
"""
Tests para el convertidor TXT a CSV
Valida el funcionamiento correcto de txt_to_csv_direct.py
"""

import unittest
import os
import sys
import tempfile
import csv
from pathlib import Path

# Agregar el directorio padre al path para importar el módulo
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

from txt_to_csv_direct import TxtToCSVConverter

class TestTxtToCSVConverter(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.converter = TxtToCSVConverter()
        self.test_dir = Path(__file__).parent
        
    def test_valid_questions(self):
        """Test con archivo de preguntas válidas"""
        test_file = self.test_dir / "test_questions_valid.txt"
        
        # Parse del archivo
        questions = self.converter.parse_txt_file(str(test_file))
        
        # Validaciones
        self.assertEqual(len(questions), 3, "Debe procesar 3 preguntas válidas")
        
        # Verificar primera pregunta
        q1 = questions[0]
        self.assertEqual(q1['number'], 1)
        self.assertEqual(q1['correct_answer'], 'A')
        self.assertEqual(len(q1['options']), 4)
        self.assertTrue(q1['text'].startswith("Esta es una pregunta"))
        
        # Verificar segunda pregunta (solo 2 opciones)
        q2 = questions[1]
        self.assertEqual(q2['number'], 2)
        self.assertEqual(q2['correct_answer'], 'B')
        self.assertEqual(q2['options'][0], "Primera opcion")
        self.assertEqual(q2['options'][1], "Segunda opcion")
        self.assertEqual(q2['options'][2], "")  # Debe completar con vacío
        self.assertEqual(q2['options'][3], "")  # Debe completar con vacío
        
    def test_invalid_questions(self):
        """Test con archivo de preguntas inválidas"""
        test_file = self.test_dir / "test_questions_invalid.txt"
        
        # Parse del archivo
        questions = self.converter.parse_txt_file(str(test_file))
        
        # Solo debe procesar 1 pregunta válida (Q3)
        # Q1 no tiene respuesta, Q4 tiene solo 1 opción
        self.assertEqual(len(questions), 1, "Solo debe procesar 1 pregunta válida")
        
        # Verificar que es la pregunta Q3
        q = questions[0]
        self.assertEqual(q['number'], 3)
        self.assertEqual(q['correct_answer'], 'A')
        
    def test_validation_issues(self):
        """Test de validaciones post-procesamiento"""
        test_file = self.test_dir / "test_questions_invalid.txt"
        
        # Parse y validación
        questions = self.converter.parse_txt_file(str(test_file))
        issues = self.converter.validate_questions(questions)
        
        # Debe detectar numeración no secuencial
        self.assertTrue(len(issues) > 0, "Debe detectar problemas de validación")
        self.assertTrue(any("Numeración no secuencial" in issue for issue in issues))
        
    def test_edge_cases(self):
        """Test con casos especiales"""
        test_file = self.test_dir / "test_questions_edge_cases.txt"
        
        # Parse del archivo
        questions = self.converter.parse_txt_file(str(test_file))
        
        # Debe procesar ambas preguntas
        self.assertEqual(len(questions), 2, "Debe procesar preguntas con casos especiales")
        
        # Verificar que maneja caracteres especiales
        q1 = questions[0]
        self.assertIn("¿Cuál", q1['text'])
        self.assertIn("ñ, á, é", q1['options'][0])
        
    def test_answer_mapping(self):
        """Test del mapeo de respuestas A->1, B->2, etc."""
        # Test directo del método
        self.assertEqual(self.converter.map_answer_to_number('A', []), '1')
        self.assertEqual(self.converter.map_answer_to_number('B', []), '2')
        self.assertEqual(self.converter.map_answer_to_number('C', []), '3')
        self.assertEqual(self.converter.map_answer_to_number('D', []), '4')
        
    def test_clean_text(self):
        """Test de limpieza de texto"""
        # Test espacios múltiples
        self.assertEqual(self.converter.clean_text("  texto   con    espacios  "), "texto con espacios")
        
        # Test texto vacío
        self.assertEqual(self.converter.clean_text(""), "")
        self.assertEqual(self.converter.clean_text(None), "")
        
    def test_csv_generation(self):
        """Test de generación completa de CSV"""
        test_file = self.test_dir / "test_questions_valid.txt"
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tmp_csv:
            output_file, question_count = self.converter.convert_to_csv(str(test_file), tmp_csv.name)
            
            # Verificar que se creó el archivo
            self.assertTrue(os.path.exists(output_file))
            self.assertEqual(question_count, 3)
            
            # Verificar contenido del CSV
            with open(output_file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                rows = list(reader)
                
            self.assertEqual(len(rows), 3, "Debe generar 3 filas CSV")
            
            # Verificar formato de primera fila
            row1 = rows[0]
            self.assertEqual(row1[0], "MC")  # Tipo multiple choice
            self.assertEqual(row1[1], "")    # Campo vacío requerido
            self.assertEqual(row1[2], "1.0") # Puntos
            self.assertEqual(row1[4], "1")   # Respuesta correcta (A=1)
            
            # Limpiar archivo temporal
            os.unlink(output_file)
            
    def test_file_not_found(self):
        """Test con archivo inexistente"""
        with self.assertRaises(FileNotFoundError):
            self.converter.parse_txt_file("archivo_inexistente.txt")
            
    def test_empty_file(self):
        """Test con archivo vacío"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp_file:
            tmp_file.write("")  # Archivo vacío
            tmp_file.flush()
            
            questions = self.converter.parse_txt_file(tmp_file.name)
            self.assertEqual(len(questions), 0, "Archivo vacío debe resultar en 0 preguntas")
            
            os.unlink(tmp_file.name)

class TestCSVFormat(unittest.TestCase):
    """Tests específicos para el formato CSV generado"""
    
    def setUp(self):
        self.converter = TxtToCSVConverter()
        
    def test_csv_row_format(self):
        """Test del formato específico de filas CSV"""
        question = {
            'number': 1,
            'text': 'Pregunta de prueba?',
            'options': ['Opcion A', 'Opcion B', 'Opcion C', 'Opcion D'],
            'correct_answer': 'B'
        }
        
        row = self.converter.generate_csv_row(question)
        
        # Verificar estructura exacta
        expected = [
            'MC',                    # Tipo
            '',                      # Campo vacío
            '1.0',                   # Puntos
            'Pregunta de prueba?',   # Pregunta
            '2',                     # Respuesta correcta (B=2)
            'Opcion A',              # Opción A
            'Opcion B',              # Opción B
            'Opcion C',              # Opción C
            'Opcion D'               # Opción D
        ]
        
        self.assertEqual(row, expected)
        
    def test_csv_row_with_empty_options(self):
        """Test con opciones vacías"""
        question = {
            'number': 1,
            'text': 'Pregunta con 2 opciones?',
            'options': ['Opcion A', 'Opcion B', '', ''],
            'correct_answer': 'A'
        }
        
        row = self.converter.generate_csv_row(question)
        
        # Verificar que las opciones vacías se incluyen
        self.assertEqual(row[7], '')  # Opción C vacía
        self.assertEqual(row[8], '')  # Opción D vacía
        self.assertEqual(row[4], '1') # Respuesta A=1

if __name__ == '__main__':
    # Configurar para mostrar más detalles en los tests
    unittest.main(verbosity=2)